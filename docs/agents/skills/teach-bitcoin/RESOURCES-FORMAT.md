# RESOURCES.md format

`RESOURCES.md` is the curated set of trusted sources for this topic. Knowledge in
lessons is drawn from here, not from parametric guesses. Wisdom comes from the
communities listed here.

For Bitcoin topics, the **first and highest-trust source is this repo's own
content** — the relevant Plan ₿ Academy course / tutorial / resource. List those
before reaching for external material.

## Structure

```md
# {Topic} Resources

## Knowledge

- [Plan ₿ Academy: btc101 — The Bitcoin Journey](https://planb.academy/en/courses/UUID-FROM-course.yml) · `courses/btc101/en.md`
  The canonical beginner course. Use for: monetary value proposition, transactions, wallets, mining overview.
- [Bitcoin: A Peer-to-Peer Electronic Cash System — Satoshi Nakamoto (2008)](https://bitcoin.org/bitcoin.pdf)
  Primary source. Use for: the original design rationale, double-spend, proof-of-work.
- [BIP-39 wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt)
  Use for: seed phrase mechanics.

## Wisdom (Communities)

- [Plan ₿ Network nodes & meetups](https://planb.network/) — local, hands-on practice with peers.
- [Bitcoin StackExchange](https://bitcoin.stackexchange.com/) — high-signal Q&A, moderated.
```

## Rules

- **Repo content first.** Cite the matching Plan ₿ Academy course/tutorial/
  resource (link the website *and* the repo path) before external sources.
- **Link by UUID, not slug.** Every planb.academy link uses the content's UUID
  (the `id:` in its `course.yml`/`tutorial.yml`), never the human slug like
  `/courses/btc101` — a slug URL 404s. See the **Links** rules in `RIGHT-DOOR.md`.
- **High-trust only.** Prefer primary sources (whitepaper, BIPs, mailing list),
  recognized experts, peer-reviewed work, and well-moderated communities. Leave
  out marketing dressed as education and price/speculation content.
- **Annotate every entry.** One line: what it covers and when to reach for it.
- **Group by Knowledge / Wisdom.** A resource may appear in only one group.
- **Surface gaps.** If no good source exists for an area the mission needs, add a
  `## Gaps` section listing what is missing — it drives future search.
- **Prune ruthlessly.** Remove sources that proved wrong, shallow, or off-mission.
- **Record community preferences.** If the learner opts out of communities, note
  it so future sessions stop proposing them.
