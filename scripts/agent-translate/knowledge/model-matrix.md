# Model-Selection Decision Matrix — Agentic Translation of Bitcoin Educational Content

**Scope:** pick the best LLM to run *inside a headless coding-agent harness (omp)* that translates whole markdown/YAML files in place with tool use (read/write/edit). The chosen model must be **both** a strong translator **and** a competent agent (reliable tool-calling, instruction-following, structured output, long context). 30 target languages, grouped into 9 families.

**Evidence date:** 2026-07-03. Note: several leaderboards surfaced models *newer* than the assignment's candidate set (e.g. Claude Opus 4.6/4.7 / "Fable-5", GPT-5.2, Gemini 3.1, DeepSeek-V4, Qwen3.5, Kimi K2.5). Those are **unverifiable** and are excluded; all tiers below use the named candidates. Where a newer iteration only *inherits* a documented property, it is marked `[INFERENCE]`.

---

## 1. TL;DR recommendation (6 bullets)

- **Default workhorse = GPT-5.1.** Best single balance of translation quality (GPT-4.1 was a WMT25 co-leader), S-tier agentic reliability (SWE-bench 77.9, Terminal-Bench 2.0 58.1), rock-solid native tool-calling, 400K context, mid cost ($1.25/$10 per M). (WMT25/Slator; vellum flagship report)
- **Max-quality / low-resource specialist = Gemini 3 Pro.** Its lineage *won* the WMT25 human evaluation overall (Gemini 2.5 Pro, 14 language pairs) and it has the broadest low-resource coverage (only candidate ecosystem with production Kirundi) + 1M context. Gemini **3** Pro fixes 2.5's agentic weakness `[INFERENCE from vellum Gemini-3 report]`. Route all hard/low-resource families here.
- **Safety / reliability anchor = Claude Sonnet 4.5.** Best tool-use score of any candidate (τ²-Bench 84.7) and by far the best prompt-injection resistance (4.7% attack success vs 21.9% GPT-5.1, 12.5% Gemini 3) — use it whenever the source files could contain instructions that might hijack a file-editing agent. (anthropic.com; vellum)
- **Chinese (zh) override = GLM-4.6.** Ranked #1 by COMET on professional Chinese→English translation in a 2026 controlled study (beating GPT-5.0, Claude Sonnet 4.5, Qwen3-Max, Grok-4), is open-weights, 200K context, and ~1/7 the cost of Claude. Best pick when Chinese idiom fidelity or bulk cost dominates. (erytis JCSFT 2026; z.ai)
- **Hypothesis verdict: only *partly* true.** Chinese models have a real, measured edge on **Chinese itself** (and Chinese *specialized* MT models like Tencent Hunyuan-MT / Qwen-MT top automatic metrics), but there is **no robust evidence** that Chinese *general/agentic* LLMs beat Western frontier models on **ja/ko/th/vi/id/hi** — Gemini/GPT lead the broad human MT evals there. Western frontier clearly leads European.
- **rn (Kirundi) is the one unsolved language.** No candidate agentic LLM documents Kirundi support; only Google Translate/Vertex (PaLM2) and Meta NLLB-200 have production coverage. Route to Gemini 3 Pro as least-bad **and mandate human review** (or NLLB-200 pre-translate → LLM post-edit).

---

## 2. Language-family routing table

Legend: **Primary** = default route; **Runner-up** = fallback / override. All 30 languages mapped.

| # | Family | Languages | Primary | Runner-up | 1-line justification (source) |
|---|--------|-----------|---------|-----------|-------------------------------|
| 1 | Western-European Latin | de, es, fr, it, pt, nl, ro | **GPT-5.1** | Gemini 3 Pro / Claude Sonnet 4.5 | Western frontier dominates European MT; GPT-4.5/o1/Claude-Sonnet led Intento's EN→ES/EN→DE LQA, Gemini/GPT/Claude top of WMT25 general LLMs (inten.to 2025; WMT25/Slator). |
| 2 | Slavic (Cyrillic + Latin) | bg, cs, pl, ru, sk, sr-Latn | **GPT-5.1** | Gemini 3 Pro | WMT25 human-eval winner was Gemini 2.5 Pro (won cs among 14 pairs); frontier Western models strongest on ru/pl/cs (aclanthology 2025.wmt-1.1). |
| 3 | Nordic / Finnic | sv, nb-NO, fi, et | **Gemini 3 Pro** | GPT-5.1 | fi/et are agglutinative + mid-resource; WMT25 included En-Et and Gemini lineage led overall; Gemini most robust on lower-resource dirs (WMT25 findings). |
| 4 | Turkic | tr | **GPT-5.1** | Gemini 3 Pro / Qwen3-Max | Turkish is well-resourced; frontier models strong; Qwen-MT explicitly lists Turkish (Turkic focus) as runner-up (qwenlm Qwen-MT). |
| 5 | CJK | zh-Hans, zh-Hant, ja, ko | **Gemini 3 Pro** (ja/ko/zh) | **GLM-4.6** for zh; GPT-5.1 for ja/ko | Gemini 2.5 Pro won WMT25 incl. CJK directions; for **zh specifically** GLM-4.6 has a measured COMET edge on Chinese fidelity + far lower cost (aclanthology 2025.wmt-1.1; erytis JCSFT 2026). |
| 6 | SEA | th, vi, id | **Gemini 3 Pro** | GPT-5.1 / Qwen3-Max | Gemini most robust on lower-resource; Qwen-MT explicitly supports th/vi/id but is not an agent (WMT25; qwenlm Qwen-MT). |
| 7 | Indic | hi, si | **Gemini 3 Pro** | GPT-5.1 / Qwen3-Max | hi well-supported by all; **si (Sinhala) is low-resource** — only Gemini (Google lineage) and Qwen-MT clearly cover it (FLORES-200 sin_Sinh; qwenlm Qwen-MT). |
| 8 | Iranian | fa | **GPT-5.1** | Gemini 3 Pro | Persian is broadly supported (GPT, Gemini, Mistral, Qwen all list fa); lowest-risk of the non-European set (docs.mistral.ai; qwenlm Qwen-MT). |
| 9 | Bantu / African | sw, rn | **sw: Gemini 3 Pro** / **rn: Gemini 3 Pro + human review** | sw: GPT-5.1 / Qwen3-Max | sw (swh_Latn) well-covered (Google, Qwen-MT); **rn (Kirundi) unsupported by every candidate LLM** — only Google Translate/Vertex + NLLB-200 have it (FLORES-200; support.google.com Kirundi 2024). |

**Consolidated route:** GPT-5.1 handles families 1,2,4,8 (18 languages); Gemini 3 Pro handles families 3,5,6,7,9 (12 languages, incl. all low-resource); GLM-4.6 is the zh cost/fidelity override; Claude Sonnet 4.5 is the drop-in safety substitute anywhere untrusted source content is a concern; rn always gets human review.

---

## 3. Master matrix

Tiers: **S** = frontier-best, **A** = strong, **B** = adequate/uneven, **C** = weak/unusable for this axis. Cost tier: `$` budget (input ≤ ~$0.5/M) · `$$` mid · `$$$` premium. Cells carry a short evidence tag → see §7 for URLs. `†` = official tech-report number; `[I]` = `[INFERENCE]`.

| Model | Transl. overall | CJK | SEA | Indic | European | Agentic / tool-use | Long-context | Open-weights? | Cost | Availability |
|-------|-----------------|-----|-----|-------|----------|--------------------|--------------|---------------|------|--------------|
| **Gemini 3 Pro** | **S** — WMT25 lineage winner (WMT25) | **S** (WMT25 CJK) | **A/S** robust low-res | **A** (hi), si ok | **S** | **S** `[I]` big leap over 2.5 (vellum) | **S** 1M | No (API) | `$$$` $2/$12→$4/$18 | Google AI Studio, Vertex, OpenRouter |
| **Gemini 2.5 Pro** | **S** — *overall WMT25 human-eval winner, 14 pairs* | **S** | **A** | **A** | **S** | **B** — τ²-Bench 59.2†, Terminal-Bench 25.3† (weak agent) | **A** 1M | No (API) | `$$` | Vertex, AI Studio |
| **Gemini 2.5 Flash** | **A** | **A** | **A** | **B** | **A** | **B** | **A** 1M | No (API) | `$` | Vertex, AI Studio |
| **GPT-5.1** | **S/A** — GPT lineage (WMT25 GPT-4.1 co-lead) | **A/S** | **A** | **A/B** | **S** | **S** — SWE 77.9, TB2.0 58.1 (vellum); higher prompt-injection 21.9% | **A** 400K; AA-LCR strong `[I]` | No (API) | `$$` $1.25/$10 | OpenAI API, Azure, OpenRouter |
| **GPT-5 (thinking)** | **A/S** | **A** | **A** | **A/B** | **S** | **S** — τ² 80.1†, IFBench 73†, AA-LCR 76† (MiniMax-M2 tbl) | **A** 400K; **best effective long-ctx (AA-LCR 76)** | No (API) | `$$` $1.25/$10 | OpenAI API, Azure |
| **GPT-4.1** | **S** — WMT25 co-leader (Slator) | **A** | **A** | **A** | **S** | **A** — reliable native FC, older | **S** 1M | No (API) | `$$` $2/$8 | OpenAI API, Azure |
| **Claude Opus 4.5** | **A** — WMT25 2nd tier "Claude-4" | **A** | **B/A** | **B** | **S/A** | **S** — SWE 80.9, TB2.0 59.3, **best injection-resistance 4.7%** (anthropic; vellum) | **A** 200K | No (API) | `$$$` $5/$25 | Anthropic API, Bedrock, Vertex, Foundry |
| **Claude Sonnet 4.5** | **A** | **A** | **B/A** | **B** | **S/A** | **S** — **τ²-Bench 84.7† (best of all)**, SWE 77.2†, OSWorld 61.4 | **A/S** 200K; 1M beta `[I]` | No (API) | `$$$` $3/$15 | Anthropic API, Bedrock, Vertex, OpenRouter |
| **DeepSeek-V3.2** | **A** — WMT25 2nd tier; erytis #2 (R1) | **A/S** (zh) | **B** | **B** | **A** (weak legal, inten.to) | **B** — τ²-Telecom **34** (collapses on hard multi-turn tool use); SWE 67.8† | **B** 128K; AA-LCR 69† | **Yes** MIT (671B) | `$` ~10× cheaper | DeepSeek API, HF, OpenRouter |
| **GLM-4.6** | **A** — **COMET #1 on pro ZH→EN** (erytis) | **S** (Chinese fidelity) | **B** | **B/C** (no si `[I]`) | **A/B** | **A** — τ² 75.9†, SWE 68†, TB 40.5† | **A** 200K; AA-LCR 54† | **Yes** open (355B) | `$` ~1/7 Claude | z.ai API, HF, OpenRouter |
| **Qwen3-Max** | **B** general (WMT25 Qwen-3 low) / **S** via Qwen-MT | **A** (zh strong) | **A** (Qwen-MT lists) | **A** (lists si) | **B** | **A** — BFCL/τ² top-tier claims; Qwen3-235B BFCL-v3 71.9† | **A** 256K | No (Max API-only; 235B open Apache-2.0) | `$$` | Alibaba DashScope/ModelStudio, OpenRouter |
| **Kimi K2 Thinking** | **B** `[I]` | **B/A** | **B** | **B** | **B** | **A** — SWE-V 71.3, 200-300 sequential tool calls, τ² 70.3 | **A** 256K; AA-LCR 52† | **Yes** Modified-MIT | `$` | Moonshot API, HF, OpenRouter |
| **MiniMax-M2** | **B** `[I]` | **B** | **B** | **B** | **B** | **A** — #1 OSS composite; τ² 77.2, **τ²-Telecom 87 (best)**, IFBench 72, TB 46.3 | **A/B** ~128-200K `[I]` | **Yes** MIT (230B/10B-active) | `$` (free preview) | MiniMax platform, HF, OpenRouter |
| **Ernie 4.5** | **B** — vendor claims SOTA multiling MT `[I]` | **A** (Chinese-native) `[I]` | **B** | **B** | **B** | **B** `[I]` less-proven agentics | **B** 131K | **Yes** Apache-2.0 (up to 424B) | `$` (99% cheaper claims) | Baidu Qianfan, HF, OpenRouter |
| **Mistral Large 2** | **B** — WMT25 lower (Slator) | **C** (no zh list) | **B** (th/vi/id listed) | **B** (hi only, no si) | **A** Euro focus | **B** — older FC | **B** 128K | **Yes** MRL (non-commercial) | `$$` | Mistral La Plateforme, HF |
| *Tencent Hunyuan-MT* (ref, NON-AGENT) | **S** — *topped WMT25 automatic* metrics | **S** | **A** | **B** | **A** | **C** — translation-only, no agent tooling | — | Yes | `$` | HF (reference/oracle only) |
| *Qwen-MT-turbo* (ref, NON-AGENT) | **S** — 92 langs, strong human eval | **S** | **S** (th/vi/id) | **A** (si) | **A** | **C** — MT API only, not an agent | — | No | `$` $0.5/M out | DashScope (reference/oracle only) |

Cross-model agentic numbers (τ², SWE-bench Verified, Terminal-Bench, IFBench, AA-LCR) are from the **MiniMax-M2 official README table** (values `†` sourced from each model's own tech report); translation tiers from WMT25 + Intento + erytis; specs from official model cards. See §7.

---

## 4. Hypothesis verdict — do Chinese models beat Western models on Asian languages?

**Verdict: PARTIALLY CONFIRMED, and only for Chinese-language content. REFUTED (or unproven) for the other Asian languages among *agentic* models.**

Per-language, with the strongest evidence available:

- **zh-Hans / zh-Hant → CONFIRMED (modest edge).** In a controlled 2026 multi-metric study of professional Chinese→English translation (financial/tech/political texts), **GLM-4.6 ranked #1 by COMET across all prompt settings and DeepSeek-R1 #2**, ahead of ChatGPT-5.0, Claude Sonnet 4.5, Qwen3-Max and Grok-4 (erytis JCSFT, DOI 10.63313/JCSFT.9087). Chinese-idiom fidelity and Taiwan/Mainland register handling also favour Chinese models (cf. Qwen-MT examples). **However**, on the neutral WMT25 human evaluation, Gemini 2.5 Pro was still the *overall* winner including Chinese directions (aclanthology 2025.wmt-1.1), so the edge is real but small and metric-dependent.
- **ja / ko → REFUTED / thin.** No credible neutral benchmark shows a Chinese *general* LLM beating Gemini/GPT/Claude on Japanese or Korean. Gemini 2.5 Pro won WMT25 overall (14 pairs incl. CJK). Qwen-MT claims strong ja/ko human-eval — but **Qwen-MT-turbo is a specialized translation model, not an agent** (see §5), so it can't be routed into the harness. Among agentic candidates, Western frontier is the safe choice for ja/ko.
- **th / vi / id → REFUTED / thin.** These are in FLORES-200 and Qwen-MT lists them, but WMT25/Global-MMLU evidence points to Gemini being the most robust on lower-resource directions; no agentic Chinese model demonstrably leads here. `[Evidence thin — no head-to-head SEA agentic-model MT benchmark found.]`
- **hi / si (Indic) → REFUTED / thin.** hi is well covered by all frontier models; si (Sinhala) is low-resource and best covered by Gemini (Google lineage) or Qwen-MT — not by a clear "Chinese-model wins" signal. `[Evidence thin.]`

**Where the hypothesis is actually true but *unusable*:** the systems that genuinely top Asian-language MT are **Chinese *specialized* MT models — Tencent Hunyuan-MT (topped WMT25 automatic metrics) and Qwen-MT-turbo (92 langs, strong ja/ko/th/zh human eval)**. Both are translation-only and are **not agents** (no reliable tool-calling / file-editing), so they cannot drive the omp harness. They are useful only as a *reference oracle* or a *pre-translate → LLM-post-edit* stage.

**Net:** Use a Chinese model (GLM-4.6/DeepSeek) as a **zh override** and for cost; keep Western frontier (Gemini 3 Pro / GPT-5.1) for every other Asian language. The "Chinese-beats-Western on Asian languages" claim does **not** generalize past Chinese itself for the *agentic* models we can actually deploy.

---

## 5. Agentic caveat — great translators that are weak agents

The harness needs reliable tool-calling, instruction-following, structured output, and resistance to instructions embedded in the very files it edits. Some strong translators fail this gate. Ranked by the severity of the translation↑ / agent↓ tradeoff:

1. **Tencent Hunyuan-MT & Qwen-MT-turbo — UNUSABLE as agents.** Best-in-class MT (Hunyuan-MT topped WMT25 automatic; Qwen-MT 92 langs), but they are dedicated translation endpoints with no/limited tool-calling. **Do not route into omp.** Only viable as a reference or a non-agentic pre-translation stage.
2. **Gemini 2.5 Pro — best translator, weak agent.** *Overall WMT25 human-eval winner*, yet τ²-Bench 59.2 and Terminal-Bench **25.3** (worst of the group) — it stumbles on multi-step tool loops. **Resolution: use Gemini 3 Pro**, which keeps the translation lineage and (per vellum) fixes the agentic gap `[INFERENCE]`. Never deploy 2.5 Pro as the file-editing agent.
3. **DeepSeek-V3.2 — good translator, shaky hard tool-use.** Strong general MT (WMT25 2nd tier; R1 #2 on zh) but **τ²-Telecom 34** vs 78-87 for leaders — it collapses on complex multi-turn tool interactions and degrades on specialized/legal text (inten.to). Acceptable for simple single-file translate-and-write loops with supervision; risky for long multi-tool sessions.
4. **Ernie 4.5 / Mistral Large 2 — adequate translators, unproven/older agents.** Fine for one-shot translation; weaker/older function-calling → keep off the critical path unless supervised. `[INFERENCE on Ernie agentics]`
5. **Qwen3-Max, GLM-4.6, Kimi K2 Thinking, MiniMax-M2 — safe agents.** These *are* competent agents (τ² 70-77, strong tool-calling, IFBench acceptable). GLM-4.6 and MiniMax-M2 in particular are the best open-weights tool-callers; use them without the caveat.

**Prompt-injection note (critical for a file-editing agent):** source markdown/YAML is semi-trusted content the agent reads and rewrites. **Claude (Opus/Sonnet 4.5) has the lowest attack-success rate (4.7%)**, vs Gemini 3 (12.5%) and GPT-5.1 (21.9%) (vellum). For corpora that may contain adversarial or instruction-like text, prefer Claude Sonnet 4.5 as the agent even though its raw translation tier is A rather than S.

---

## 6. Rare / low-resource languages (rn, sw, si, fa)

All four **are present in FLORES-200 / NLLB-200** (run_Latn, swh_Latn, sin_Sinh, pes_Arab) — benchmark presence is not the gap; *deployed* model support is (FLORES-200 README; ai.meta.com NLLB).

- **rn (Rundi / Kirundi) — HIGHEST RISK; effectively unusable solo by any candidate.** No candidate agentic LLM documents Kirundi: **Qwen-MT's 92-language list explicitly excludes it; Mistral excludes it**; GPT/Claude/DeepSeek/GLM/Kimi/MiniMax/Ernie publish no Kirundi support. The only production coverage is **Google Translate (added "Rundi" June 2024, PaLM2)** and **Meta NLLB-200 (run_Latn)**. **Recommendation:** route to **Gemini 3 Pro** (shares Google data lineage → least-bad) **and mandate human review**, or run **NLLB-200 / Google Translate as a pre-translate stage then LLM post-edit**. Treat any unreviewed rn output as unreliable.
- **si (Sinhala) — MODERATE RISK.** Low-resource; covered by **Gemini (Google lineage)** and **Qwen-MT (lists si)**, but *not* by Mistral or most Chinese general models. Degrades least on **Gemini 3 Pro**; Qwen-MT is a strong non-agent reference. Spot-check output.
- **sw (Swahili) — LOW/MODERATE RISK.** Long-standing Google coverage + Qwen-MT lists it + FLORES-200. **Gemini 3 Pro / GPT-5.1** handle it well; usable without special handling, light QA recommended.
- **fa (Persian) — LOW RISK.** Broadly supported (GPT, Gemini, Mistral, Qwen all list Western Persian pes_Arab); frontier quality is good. **GPT-5.1 or Gemini 3 Pro**, no special handling.

**Degrades least overall:** Gemini 3 Pro (Google multilingual lineage is the differentiator for si/sw/rn). **Unusable solo:** rn by every candidate — the single language that requires a non-LLM fallback + human-in-the-loop.

---

## 7. Sources

- WMT25 preliminary results — Slator: https://slator.com/wmt25-preliminary-results-gemini-2-5-pro-gpt-4-1-lead-ai-translation/
- WMT25 General MT Shared Task findings (human eval; "best system overall Gemini 2.5 Pro, won 14 language pairs") — https://aclanthology.org/anthology-files/pdf/wmt.real/2025.wmt-1.1.pdf
- WMT25 preliminary ranking (automatic; Hunyuan-MT tops) — https://arxiv.org/html/2508.14909v2 (PDF: https://arxiv.org/pdf/2508.14909)
- WMT25 shared-task page — https://www2.statmt.org/wmt25/translation-task.html
- Qwen-MT (Qwen3-based, 92 languages, human eval zh/ja/ko/th…) — https://qwenlm.github.io/blog/qwen-mt/
- Alibaba Model Studio MT / Qwen-MT language list — https://www.alibabacloud.com/help/en/model-studio/machine-translation
- Intento "Generative AI for Translation in 2025" (EN→ES/EN→DE LQA) — https://inten.to/blog/generative-ai-for-translation-in-2025/
- Fu & Xu 2026, "Comparing Chinese–English Translation Performance of LLMs" (GLM-4.6 COMET #1, DeepSeek-R1 #2) — https://academics.erytis.com/index.php/jcsft/article/view/602 (DOI 10.63313/JCSFT.9087)
- LMArena / Arena text leaderboard — https://arena.ai/leaderboard/text
- Berkeley Function-Calling Leaderboard (BFCL) V4 — https://gorilla.cs.berkeley.edu/leaderboard.html ; results repo https://github.com/HuanzhiMao/BFCL-Result
- MiniMax-M2 (official cross-model agentic table: τ², SWE-bench, Terminal-Bench, IFBench, AA-LCR, BrowseComp-zh) — https://github.com/MiniMax-AI/MiniMax-M2
- Anthropic — Claude Opus 4.5 — https://www.anthropic.com/news/claude-opus-4-5 ; Claude Sonnet 4.5 — https://www.anthropic.com/news/claude-sonnet-4-5 ; models overview — https://platform.claude.com/docs/en/about-claude/models/overview
- Vellum flagship model report (Opus 4.5 / GPT-5.1 / Gemini 3 agentic + prompt-injection) — https://www.vellum.ai/blog/flagship-model-report ; Gemini 3 benchmarks — https://www.vellum.ai/blog/google-gemini-3-benchmarks
- OpenAI GPT-5 / GPT-5.1 (400K context, $1.25/$10) — https://openai.com/gpt-5 ; GPT-5.1 model card — https://developer.box.com/guides/box-ai/ai-models/openai-gpt-5-1-model-card
- Gemini 3 Pro (1M context, pricing) — https://openrouter.ai/google/gemini-3-pro-preview
- MMLU-ProX multilingual (29 languages) — https://mmluprox.github.io/ ; Global MMLU (ACL 2025) — https://aclanthology.org/2025.acl-long.919.pdf
- DeepSeek-V3.2 release (128K, MIT, function calling) — https://api-docs.deepseek.com/news/news251201 ; HF — https://huggingface.co/deepseek-ai/DeepSeek-V3
- GLM-4.6 (200K, open, ~1/7 cost) — https://z.ai/blog/glm-4.6
- Kimi K2 Thinking (256K, SWE-V 71.3, 200-300 tool calls) — https://huggingface.co/moonshotai/Kimi-K2-Thinking ; https://moonshotai.github.io/Kimi-K2/
- Qwen3 / Qwen3-Max (256K, 119 languages) — https://qwenlm.github.io/blog/qwen3/ ; https://qwen.ai/blog
- Baidu ERNIE 4.5 (open Apache-2.0, 131K, MoE up to 424B) — https://openrouter.ai/baidu/ernie-4.5-300b-a47b ; tech report https://ernie.baidu.com/blog/publication/ERNIE_Technical_Report.pdf
- Mistral language support — https://docs.mistral.ai/resources/languages
- FLORES-200 / NLLB (low-resource presence: run_Latn, swh_Latn, sin_Sinh, pes_Arab) — https://github.com/facebookresearch/flores/blob/main/flores200/README.md ; https://ai.meta.com/research/no-language-left-behind/
- Google Translate Kirundi ("Rundi") support (June 2024) — https://support.google.com/translate/answer/15139004 ; Vertex AI Translation languages — https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs
- BFCL 2025 analysis (Klavis; GLM-4.5 FC 70.85, Claude Opus 4.1 70.36, GPT-5 59.22) — https://klavis.ai/blog/function-calling-and-agentic-ai-in-2025
