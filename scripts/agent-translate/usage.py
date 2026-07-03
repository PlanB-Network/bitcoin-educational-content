#!/usr/bin/env python3
"""Subscription-usage governor for the translation batch.

Wraps `agent-sub-usage` (JSON probe of Claude/Codex subscription windows) and
freezes the batch when the 5-hour rolling windows are near their cap, resuming at
the window reset.

Rules (config: threshold=80, hard=95):
  - SOFT freeze: every provider the batch actually uses is >= `threshold`% of its
    5h window  (matches "les deux subs à 80% -> freeze").
  - HARD freeze: any in-use provider is >= `hard`% (backstop against blowing a
    window, e.g. if the other provider is idle/unauthed).
On freeze, sleep until the earliest relevant 5h reset (+buffer), then re-check.

The snapshot is cached (`poll_interval` s) because the probe is slow (~5s).
Fails OPEN: if the probe errors, the batch proceeds (never blocks on a broken probe).
"""
from __future__ import annotations

import json
import subprocess
import time

SUBS = ("anthropic", "openai")
FIVE_H = "5-hour-usage-limit"
WEEKLY = "weekly-usage-limit"


def provider_of(model: str) -> str:
    m = (model or "").lower()
    if "gpt" in m or "codex" in m or m.startswith(("o1", "o3", "o4")):
        return "openai"
    if "sonnet" in m or "opus" in m or "haiku" in m or "claude" in m:
        return "anthropic"
    return "unknown"


def snapshot(timeout: int = 30) -> dict:
    out = subprocess.run(["agent-sub-usage"], capture_output=True, text=True, timeout=timeout)
    return json.loads(out.stdout)


def _window(data: dict, sub: str, key: str = FIVE_H) -> tuple[float, float, bool]:
    """(used_percent, seconds_until_reset, available) for a sub's window."""
    s = data.get(sub) or {}
    w = s.get(key) or {}
    avail = bool(s.get("available")) and bool(w.get("available", True))
    return float(w.get("used_percent", 0)), float(w.get("seconds_until_reset", 0)), avail


class Governor:
    def __init__(self, in_use: set[str], *, threshold: float = 80, hard: float = 95,
                 poll_interval: int = 60, reset_buffer: int = 120, log=print, enabled: bool = True):
        self.in_use = {p for p in in_use if p in SUBS} or set(SUBS)
        self.threshold = threshold
        self.hard = hard
        self.poll_interval = poll_interval
        self.reset_buffer = reset_buffer
        self.log = log
        self.enabled = enabled
        self._cache: dict | None = None
        self._cache_ts = 0.0

    def fresh(self, force: bool = False) -> dict:
        if force or self._cache is None or (time.time() - self._cache_ts) > self.poll_interval:
            try:
                self._cache = snapshot()
                self._cache_ts = time.time()
            except Exception as e:  # noqa: BLE001 — fail open
                self.log(f"⚠ usage probe failed ({type(e).__name__}); proceeding without gate")
                self._cache = self._cache or {}
                self._cache_ts = time.time()
        return self._cache

    def status_line(self) -> str:
        d = self.fresh()
        parts = []
        for sub in SUBS:
            u5, _, av = _window(d, sub)
            uw, _, _ = _window(d, sub, WEEKLY)
            if not av and sub not in self.in_use:
                continue
            tag = "●" if sub in self.in_use else "○"
            parts.append(f"{tag}{sub[:4]} 5h {u5:.0f}% wk {uw:.0f}%")
        return "usage " + " · ".join(parts) if parts else "usage n/a"

    def _freeze_reason(self, d: dict) -> tuple[bool, float]:
        """(should_freeze, seconds_to_wait)."""
        used = {p: _window(d, p) for p in self.in_use}
        avail = {p: v for p, v in used.items() if v[2]}
        if not avail:
            return False, 0.0
        hard_hit = [p for p, (u, _s, _a) in avail.items() if u >= self.hard]
        all_soft = all(u >= self.threshold for (u, _s, _a) in avail.values())
        if hard_hit:
            wait = min(avail[p][1] for p in hard_hit)
            return True, wait
        if all_soft:
            wait = min(v[1] for v in avail.values())
            return True, wait
        return False, 0.0

    def gate(self) -> None:
        """Block while the in-use windows are capped. No-op when disabled."""
        if not self.enabled:
            return
        while True:
            d = self.fresh()
            freeze, wait = self._freeze_reason(d)
            if not freeze:
                return
            wait = max(60.0, min(wait + self.reset_buffer, 3900.0))  # cap ~65 min
            mins = wait / 60
            self.log(f"❄ FREEZE — in-use subs at/over limit ({self.status_line()}). "
                     f"Resuming in ~{mins:.0f} min (window reset).")
            time.sleep(wait)
            self.fresh(force=True)

    def preflight(self) -> bool:
        """Log a one-line usage summary at start; return False only if a hard block
        is active with no headroom on every in-use sub."""
        d = self.fresh(force=True)
        self.log(self.status_line())
        freeze, _ = self._freeze_reason(d)
        if freeze:
            self.log("… starting frozen; the batch will wait for the next window reset.")
        return True


def percents(data: dict) -> dict:
    """Per-sub used_percent for the 5h and weekly windows (for before/after deltas)."""
    out = {}
    for sub in SUBS:
        u5, _, _ = _window(data, sub)
        uw, _, _ = _window(data, sub, WEEKLY)
        out[sub] = {"5h": u5, "weekly": uw}
    return out


def aggregate_sessions(sessions_dir) -> dict:
    """Sum omp session-file token usage per model. One .jsonl per omp session; each
    assistant `message` line carries a `usage` object. Returns
    {model: {provider, input, output, cacheRead, cacheWrite, cost, messages}}."""
    from pathlib import Path
    agg: dict = {}
    sdir = Path(sessions_dir)
    if not sdir.exists():
        return agg
    for f in sdir.glob("*.jsonl"):
        for ln in f.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                e = json.loads(ln)
            except ValueError:
                continue
            if e.get("type") != "message":
                continue
            m = e.get("message") or {}
            if m.get("role") != "assistant":
                continue
            u = m.get("usage") or {}
            model = m.get("model") or "?"
            a = agg.setdefault(model, {"provider": m.get("provider") or provider_of(model),
                                       "input": 0, "output": 0, "cacheRead": 0,
                                       "cacheWrite": 0, "cost": 0.0, "messages": 0})
            a["input"] += int(u.get("input", 0) or 0)
            a["output"] += int(u.get("output", 0) or 0)
            a["cacheRead"] += int(u.get("cacheRead", 0) or 0)
            a["cacheWrite"] += int(u.get("cacheWrite", 0) or 0)
            a["cost"] += float((u.get("cost") or {}).get("total", 0.0) or 0.0)
            a["messages"] += 1
    return agg


if __name__ == "__main__":
    g = Governor(set(SUBS))
    print(g.status_line())
    import sys
    d = g.fresh(force=True)
    print(json.dumps({p: {"5h_used%": _window(d, p)[0], "5h_reset_s": _window(d, p)[1]} for p in SUBS}, indent=2))
    sys.exit(0)
