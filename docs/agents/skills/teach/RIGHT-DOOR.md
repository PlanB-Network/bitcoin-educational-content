# The Right Door — Plan ₿ Academy routing map

The job: given a learner's **mission** and **level**, hand them the right
**door** into the Plan ₿ Academy catalog — a specific course, tutorial, or
resource that is challenging "just enough".

**Prefer a live read** of the catalog when running inside the content repo
(`courses/*/course.yml` + `courses/*/<lang>.md` headers, `tutorials/`,
`resources/`). The table below is a **fallback snapshot** — accurate at the time
of writing, but it can drift. When in doubt, read the repo.

## Level legend (from `docs/course_ID_rules.md`)

`101–199` beginner · `201–299` intermediate · `301–399` advanced ·
`401–499` developer/expert. Course ID = 3-letter discipline + 3-digit level.

## How to choose the door

1. **Find the learner's intent** (what they want to *do*), then their **level**
   (what they can already do).
2. Pick the lane below that matches the intent.
3. Within the lane, choose the lowest-level course at or just above their current
   ability. Beginners almost always start at **`btc101` — The Bitcoin Journey**.
4. For "how do I actually do X" → point at a `tutorials/<category>/` how-to.
   For "what should I read/listen to" → point at `resources/`.
5. Record the chosen door in `MISSION.md`; link every lesson's CTA to it.

## Lanes (curated fallback)

### Start here — the journey begins
- `btc101` — The Bitcoin Journey · **beginner** — the canonical entry point.
- `btc102` — Getting your first bitcoins · **beginner** — buy, secure, manage.

### Buy, hold & secure (sovereignty basics)
- `scu101` — Update Your Online Security · **beginner**
- `btc204` — Privacy on Bitcoin · **intermediate**
- `scu202` — Improve Your Personal Digital Security · **intermediate**

### Run your own infrastructure (node / self-hosting)
- `btc202` — Setting up your first Bitcoin node · **intermediate**
- `lnp202` — Set up Your First Lightning Node · **intermediate**
- `lnp404` — Navigating Your Node with Terminal · **intermediate**
- `net302` — IP networks: From Theory to Practice · **advanced**

### Lightning Network
- `lnp201` — Lightning Network Theory · **intermediate**
- `lnp202` — Set up Your First Lightning Node · **intermediate**
- `lnp206` — Hands-on with Breez Nodeless SDK · **intermediate**

### Economics & money
- `eco104` — Introduction to Bitcoin & Stablecoin · **beginner**
- `eco201` — Austrian School of Economics Fundamentals · **intermediate**
- `eco205` — The Austrian school of economics · **intermediate**
- `eco203` — Bastiat Economic Thought · **intermediate**
- `eco204` — Hyperinflation Case Studies · **intermediate**
- `his205` — History of Coinage · **intermediate**

### History, philosophy & sociology
- `phi101` — A Philosophical History of Freedom · **beginner**
- `phi203` — Freedom as a Social Project · **beginner**
- `soc104` — What's your Political Leaning? · **beginner**
- `his201` — The History of Bitcoin's Creation · **intermediate**
- `his203` — Bitcoin's Pioneering Era · **intermediate**
- `his204` — The Origins of Laissez-Faire Economics · **intermediate**
- `btc208` — Au cœur de la géopolitique de Bitcoin · **intermediate** (FR)
- `btc303` — Bitcoin Development Philosophy · **advanced**
- `phi305` — Spinoza and Bitcoin · **advanced**

### Mining & energy
- `min101` — Introduction to Bitcoin mining · **beginner**
- `ene101` — Les Fondements thermodynamiques de Bitcoin · **beginner** (FR)
- `min304` — Heat your home while mining bitcoins · **advanced**
- `min306` — Bitaxe Open Source Mining Mastery · **advanced**

### Merchant & business
- `biz101` — Bitcoin for Business · **beginner**
- `biz205` — Biz School (previous edition) · **intermediate**
- `pos305` — Mastering BTC Pay Server · **advanced**

### Cryptography & wallet internals
- `cyp201` — Bitcoin Wallet Architecture · **intermediate**
- `cyp302` — Modern Cryptography Fundamentals · **advanced**

### Developer track
- `dev103` — JavaScript and NodeJS Fundamentals · **beginner**
- `pro101` — Bitcoin Development Fundamentals · **beginner**
- `pro202` — Programming Bitcoin · **intermediate**
- `dev301` — System Programming Fundamentals · **advanced**
- `dev303` — Learning Rust with Bitcoin · **advanced**
- Sidechains / Liquid: `sid202` (intermediate) → `sid302` (advanced) →
  `sid402` / `sid406` (expert)
- Client-side validation: `csv402` — RGB programming · **expert**;
  `csv404` — Tapping into Taproot Assets · **expert**

### Build a community
- `btc304` — How to Create a Bitcoin Community · **advanced**

## Hands-on doors (tutorials)

For "show me how", route to `tutorials/<category>/<slug>/`. Categories present in
the repo: `wallet`, `node`, `mining`, `privacy`, `exchange`, `computer-security`,
`business`, `contribution`. Read the category folder to pick a current slug.

## Reading / listening doors (resources)

For breadth and wisdom, route to `resources/<type>/`: `books`, `podcasts`,
`papers`, `newsletters`, `movies`, `conferences`, `channels`, `glossary`,
`projects`. Seed lesson glossaries from `resources/glossary/`.

## Links

- Course page: `https://planb.academy/courses/<id>` (e.g. `/courses/btc101`)
- Tutorials: `https://planb.academy/tutorials/<category>/<slug>`
- Resources: `https://planb.academy/resources`

> Snapshot taken from 48 courses present in `courses/`. If a course is missing or
> renamed here, the live catalog wins — update this map when you notice drift.
