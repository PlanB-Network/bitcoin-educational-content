# Lessons — cs

## 2026-07-03
- Simplicity type theory (scr403): `sum type` → "součtový typ", `product type` → "součinový typ", `combinator` → "kombinátor", `tagged union` → "tagované sjednocení", `unit type` → "jednotkový typ", `boolean type` → "booleovský typ".
- Keep combinator/code identifiers verbatim in prose (iden, unit, comp, pair, case, take, drop, injl, injr, and, xor, scribe) and all math glyphs (𝟙, 𝟚, ×, +, ▵, σᴸ, σᴿ, ⟨⟩, A²/A⁴, →).
- Keep boolean literals `false`/`true` verbatim (they name Simplicity's two boolean values, mapped to 0/1) rather than translating to nepravda/pravda.
- `jets` → declined Czech "jety" (sg. "jet"); reads naturally and stays consistent.
- `Simplicity` is treated as a masculine proper name for verb agreement (e.g. "Simplicity vylučuje/používá"); `Bitcoin Script`, `Liquid Network`, `Rocq`, `DAG`, `gas`, `SHA-256`, `denial-of-service` stay verbatim.
- In Simplicity material, keep `witness` untranslated in Czech compounds (`witness hodnoty`, `witness výrazy`) to match existing course terminology.
- Simplicity effect names stay English with a Czech prefix: `efekt Failure`, `efekt Reader`, `efekt State`, etc. (don't translate the effect's proper name).
- `jets` → declined Czech plural `jety`/`jetů`; `witness` kept as loanword (`witness hodnoty`, plural `witnesy`).
- Type-algebra vocab: `sum type` → `součtový typ`, `product` → `součin`, `option type` → `typ option`; keep math glyphs `⊢ × +` and superscripts verbatim.
- Keep verbatim: `Taproot`, `Schnorr`, `Bitcoin Script`, `Tapscript`, `Bit Machine`, `SimplicityHL`, code ids (`take`/`drop`/`iden`, `bip0340-verify`, `PrecomputedTransactionData`, `TxEnv`); `Merkle` → `Merkleho kořen/strom`.
- Preserve each file's original YAML quoting per-field (several quizzes double-quote only `question`, leave `answer`/`wrong_answers` as plain scalars) — match it exactly and avoid introducing `: ` in plain scalars.
- Simplicity combinators/macros stay verbatim as code (`case`, `injl`, `injr`, `iden`, `take`, `drop`, `pair`, `comp`, `unit`, `scribe`, `push-<n`, `pop-<n`, `fold-right-n`, `map`, `zip`, `bip0340-verify`, `sig-all-hash`, `half-adder`, `f ⨾ unit = unit`); type signatures and math (`A × B ⊢ B × A`, `Aᑉⁿ`, `⟨…⟩`, `#ᶜ(comp f g)`, `tag∥tag`) are byte-identical.
- "jet" → "jet" (kept, no Czech equivalent); "combinator" → "kombinátor"; "core combinator/language" → "kombinátor jádra / jazyk jádra".
- Type theory: "sum type" → "součtový typ", "product type" → "součinový typ", "total/partial function" → "totální/parciální funkce".
- Digital logic: "full-adder" → "úplná sčítačka", "half-adder" → "poloviční sčítačka" (prose only; the `half-adder` combinator inside code stays English), "carry" → "přenos", "sum bit" → "součtový bit".
- Taproot/crypto (per glossary): "Merkle root" → "Merkleho kořen", "Schnorr signature" → "Schnorrův podpis", "key-path/script-path" → "cesta klíče / cesta skriptu", "committed" → "zavázaný"; kept verbatim: NUMS, CMR, UTXO, on-chain, Rocq, Bit Machine, Writer/Reader/Failure effects, midstate.
- YAML gotcha: keep source quoting — values with a colon+space (e.g. `dist : (A+B)…`, or `…: zahození volání…`) must stay double-quoted; unquoted values starting with `⟨`, `(`, or `push-<n` parse fine.

## 2026-07-06
- In SOC104 political philosophy, keep `pro-business` and `pro-market` verbatim in Czech prose; explain them around them as `spojenectví mezi velkými podniky a státem` versus `svobodná konkurence bez státního zvýhodňování`, matching `courses/soc104/cs.md`.
- In SOC104 political terminology, keep the French term `libertaires` verbatim in Czech prose to distinguish it from Czech `libertariáni`.
- For `intentional definitions`, use `intencionální definice`; for `structural definitions`, use `strukturální definice`.
- In the Bastiat/Friedman context, `spoliation` can be rendered as `spoliace` to preserve the technical political-economy sense rather than softening it to ordinary theft.
- In SOC104 Czech political-family quizzes, keep `libertarian` as `libertariánský` / `libertariáni`, consistent with the course text; use `libertarianismus` for the ideology.
- For the totalitarianism chapter, use `sekulární náboženství`, `kvazináboženský`, `potlačené svobody`, `vláda jedné strany`, and `řízená ekonomika`.
- In societal-debate framing, render `dominants and dominated` as `dominantní a ovládaní`; `oppressor/oppressed lens` as `optika utlačovatelů a utlačovaných`.
- In subsidy/economics quizzes, render `moral hazard` as `morální hazard` and `bailouts` as `záchranné balíčky`.
- In soc104 political-economy quizzes, keep `pro-business` and `pro-market` verbatim in Czech, matching the course translation.
- Render Hayek's `spontaneous order` as `spontánní řád` and `constructed order` as `konstruovaný řád`; `constructivism` as `konstruktivismus`.
- For Kant/Popper vocabulary in this course: `state of minority` → `stav nezletilosti`, `open society` → `otevřená společnost`, `closed society` → `uzavřená společnost`.
- In SOC/cypherpunk quizzes, keep exact historical slogans/titles embedded as artifacts verbatim: genesis block headline `The Times 03/Jan/2009 Chancellor on the brink of a second bank bailout`, motto `Cypherpunks write code`, and `Bitcoin White Paper`.
- Follow glossary capitalization for movement terms: use `Cypherpunks` as the group name; use `Manifest šifrantů` for Eric Hughes's manifesto where translating the title.
- Use glossary forms `Genesis block` and `White paper` in prose, declining only by Czech case endings when needed (`Genesis blocku`).
- Political taxonomy: keep French *libertaire(s)* untranslated and italicized when contrasting with Anglo-American libertarians; translate `libertarianism` as `libertarianismus` and adherents as `libertariáni`.
- In monetary/Bitcoin context, `sound money` reads naturally as `zdravé peníze`; keep `fiat`, `peer-to-peer`, `FOSS`, `White Paper`, and `Cypherpunks` as glossary-backed terms when linked.
- Preserve historically embedded artifacts verbatim when they function as protocol/history evidence, e.g. the Genesis Block headline `The Times 03/Jan/2009 Chancellor on the brink of a second bank bailout.`
- In SOC104, render `Nolan diagram` as `Nolanův diagram` and `Nolan diamond` as `Nolanův kosočtverec`, matching the Czech course file.
- For this political-theory course, keep `fiat` in `fiat měna` / `systém fiat peněz`; use `etatismus` / `etatistický` for `statism` / `statist`.
- In SOC104 political-family material, render `statism` as `etatismus`, `statist` as `etatista`, and `statistický` only when meaning statistical is intended; use `etatistický` for the ideology.
- For the transatlantic terminology distinction, keep American `liberals` and labels like `liberal`/`libertarian` in English when the quiz is explicitly about the English term's meaning, but translate ordinary Czech category names as `liberál`/`libertarián`.
- `spontaneous order` → `spontánní řád`; `laissez-faire`, `Big Government`, `New Deal`, `Great Society`, Cato Institute, Mises Institute, and Libertarian Party stay verbatim.
