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
