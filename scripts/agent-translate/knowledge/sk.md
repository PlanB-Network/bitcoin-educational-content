# Lessons — sk

## 2026-07-03
- Keep all Simplicity combinators verbatim: `case`, `pair`, `iden`, `take`, `drop`, `injl`, `injr`, `comp`, `unit`, `scribe`, `fold`/`fold-right-n`, `map`, `zip`, `copair`, `push-<n`, `pop-<n`. Same for `jet`/`jety`, `CMR`, `NUMS`, `Taproot`, `Schnorr(ov)`, `SHA-256`, `midstate`, `witness` (loc. `vo witnesse`), `tweak`/`Tweaknutie`, effect names `Failure`/`Reader`/`Writer`, `sig-all-hash`, `bip0340-verify`, `SimplicityHL`, `Rocq`, `on-chain`, `Bit Machine` (left English).
- Chosen renderings: combinator → `kombinátor`; core combinators → `kombinátory jadra`; product/sum → `súčin`/`súčet`; half-adder → `polovičná sčítačka`, full-adder → `úplná sčítačka`; carry → `prenos`, carry-in → `vstupný prenos`, sum bit → `súčtový bit`; typing rules → `typovacie pravidlá`, premises/conclusions → `premisy`/`závery`; bookkeeping → `evidencia`; lookup table → `vyhľadávacia tabuľka`; buffer → kept as `buffer`; commutative/idempotent/unitary → `komutatívny`/`idempotentný`/`unitárny` (noun `unitárnosť`); Merkle root/tree → `Merkleho koreň`/`Merkleho strom`; spending → `míňanie`, key-spend/key-path → `míňanie cestou kľúča`, script path → `cesta skriptu`, committed → `zaviazaný`, verifier → `overovateľ`, pruned branch → `prerezaná vetva`.
- Quote a value ONLY when it contains a `: ` (colon+space) — e.g. `answer: "…, ale nie unitárny: …"`. A Slovak clause with `:` that the English lacked still forces quoting; conversely an English-quoted string may become unquotable in Slovak and vice-versa — decide per output string, don't copy the source's quoting blindly.
- `explanation` is a `>-` folded block: `: `, `;`, leading `(` etc. need no quoting there. Wrap at spaces only — never hyphenate a word across a line break (folding turns the newline into a space, corrupting the word).
- Simplicity combinator names (`iden, unit, comp, pair, case, take, drop, injl, injr`), jets, and inline code expressions (`comp f g`, `and ▵ xor`, `case (injl unit) (drop iden)`) stay verbatim — they are identifiers, not prose. Only the surrounding prose is translated (e.g. "the comp combinator" → "kombinátor comp").
- Type-theory terminology used consistently: sum type → "súčtový typ", product type → "súčinový typ", unit type → "jednotkový typ", boolean type → "logický typ", tagged union → "označkované zjednotenie", type former → "konštruktor typu".
- half-adder → "polsčítačka"; carry → "prenos"; empty tuple → "prázdna n-tica".
- Keep protocol/proper names verbatim: Simplicity, Bitcoin Script, Liquid Network, Ethereum, Rocq, SHA-256, DAG, Merkle root (declined as "Merkle rootom"). "gas model" → "gas model"; "denial-of-service" kept as-is.
- "Simplicity" as subject: prefer reflexive passive ("aby sa umožnila...") for purpose clauses so no grammatical gender has to be assigned to the language name.
- For Simplicity course material, keep `Failure`, `Reader`, `Writer`, `witness`, `jet(s)`, `CMR`, `Taproot`, `TapLeaf`, `TapTree`, `TapTweak`, and `NUMS` in English; Slovak quiz files already use these forms.
- Render Simplicity type theory terms consistently as `súčtový typ`, `súčinový typ`, `jednotkový typ`, `typová inferencia`, and `sekvenčný kalkulus`.
- Named monadic effects: keep the identifier English, translate the noun — `Failure effect` → `efekt Failure`, likewise `efekt Reader/State/Writer/IO/Memory/Continuation/Nondeterminism`. Generic `side effects` → `vedľajšie efekty`.
- Keep verbatim (indeclinable): Simplicity, SimplicityHL, Bit Machine, Taproot, Tapscript, TapLeaf, Bitcoin Script, CMR, TxEnv, PrecomputedTransactionData, jet identifiers (`bip0340-verify`, `sig-all-hash`), hex versions (0xbe…), tags like `Simplicity␟Commitment␟iden`. Combinator names `case/take/drop/iden` and access letters `O/I/H` stay as-is.
- Naturalised loanword plurals read best: `jety`, `buffery`, `covenanty`; `witness` kept as term (`witness hodnoty`).
- Standard renderings used: `sekventový kalkul`, `lambda kalkul`, `prirodzená dedukcia`, `Curryho-Howardova korešpondencia`, `De Bruijnove indexy`, `dávková verifikácia` (batch verification), `typ unit`, `typ option`, `súčin/súčet` (product/sum), `orezať` (prune), `štandardnosť` (standardness), `on-chain` (kept).
- `in Simplicity` → `v jazyku Simplicity` (adding the `jazyk` classifier reads naturally since the name is indeclinable); `a Simplicity program` → `program Simplicity` / `program v jazyku Simplicity`.
- Quizz values that stay unquoted may safely contain `;`, `—`, `(` — YAML plain scalars only break on `: ` or ` #`; keep those out of unquoted answers. Preserve the source's per-field quoting style.

## 2026-07-06
- In SOC104 political-economy quizzes, keep `pro-business` and `pro-market` verbatim as labels; use `zástancovia pro-business/pro-market` for advocates.
- Render Hayek's `spontaneous order` as `spontánny poriadok`, `central planning` as `centrálne plánovanie`, and `market process` as `trhový proces`.
- Render Popper's `open society` / `closed society` as `otvorená spoločnosť` / `uzavretá spoločnosť`.
- For political-spectrum SOC material, render `statism` as `etatizmus`, `libertarianism` as `libertarianizmus`, `centrism` as `centrizmus`, and `conservatism` as `konzervativizmus`.
- Use `Nolanov diagram` for `Nolan diagram` and `Nolanov diamant` for `Nolan diamond`; render the top-bottom axis as `os hore-dole` and the left-right axis as `os ľavica-pravica` when naming them explicitly.
- Translate `the Greens` as `Zelení` in political-party context.
- In SOC104 political-economy quizzes, keep `pro-business` and `pro-market` as English course labels in Slovak, framed as `postoj pro-business/pro-market`, then explain them in Slovak.
- Render Austrian/libertarian money terms as `fiat peniaze`, `zdravé peniaze` for `sound money`, `zlatý štandard`, and `odštátnenie peňazí`.
- In SOC104 political-economy quizzes, render `moral hazard` as `morálny hazard`; use `dotácie` for subsidies and `záchranné balíky` for bailouts.
- Render the socialist `dominant/dominated` conflict lens as `dominantní a ovládaní`; `oppressor/oppressed lens` as `optika utláčateľa a utláčaného`.
- For totalitarianism material, use `totalitarizmus`, `totalitné režimy`, `sekulárne náboženstvá`, and `riadená ekonomika` for directed economy.
- In SOC104 political terminology, keep Anglo-American labels like `liberal`, `liberals`, and `libertarians` in English when the point is the transatlantic meaning shift; use Slovak forms (`liberáli`, `libertariáni`, `libertarianizmus`) when referring to the political family outside that label contrast.
- In SOC104 political terminology, keep the French label `libertaires` verbatim for socialist anarchists; use Slovak `libertariáni` / `libertarianizmus` for Anglo-American libertarians.
- Keep `Green New Deal` verbatim in Slovak; render its “collective planetary health” framing as `kolektívny záujem definovaný zdravím planéty` to match the existing course translation.
- For this course, render `equity` in political slogan lists as `rovnosť`, following the existing Slovak `sk.md` wording.
- In political-theory Slovak, render `statism` as `etatizmus` and `statist` as `etatista`; keep this distinct from generic `štátny intervencionizmus`.
- Use `libertarián/libertariánsky` for Anglo-American `libertarian`; keep French `libertaire` as italic `*libertaire*`/`*libertaires*` when the text explicitly contrasts it with libertarianism, and use `libertín` for `libertine`.
- For cypherpunk material in Slovak, keep `Cypherpunks`/`cypherpunk` largely as the movement name, naturalising adjectives as `cypherpunkový` when needed; preserve slogans like `Cypherpunks write code` verbatim.
- In cypherpunk/SOC104 quiz material, render the slogan `Cypherpunks write code` as `Cypherpunkovia píšu kód`; use `cypherpunkový` for adjectival forms and `Cypherpunkovia` for the movement members.
- Keep `Bitcoin White Paper` in English as a title-like Bitcoin term; `white paper` can be lowercased when used generically in prose.
- For SOC104 political philosophy, use `sociálny štát` for `welfare state`, `nátlak` for `coercion`, `donútenie` for `compulsion`, and `konštruktivizmus`/`antikonštruktivistický` for constructivism terminology.
