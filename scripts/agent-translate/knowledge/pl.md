# Lessons — pl

## 2026-07-03
- Simplicity combinator names stay verbatim as code identifiers: `iden, unit, comp, pair, case, take, drop, injl, injr` (also `and`, `xor`, `scribe`). Never translate.
- Type-theory terms for Simplicity: sum type → "typ sumy", product type → "typ iloczynu", unit type → "typ jednostkowy", boolean type → "typ logiczny"; "tagged union" → "unia tagowana"; "former"/constructor → "konstruktor".
- Keep math/notation glyphs untouched: `𝟙 𝟚 × + ▵ σᴸ σᴿ ⟨⟩`, exponents like `𝟚²⁵⁶`, and gate names `AND/XOR/OR/NOT`.
- "jet/jets" (Simplicity native impls) → "jet/jety" (kept English root, Polish inflection); "half-adder" → "półsumator", carry → "przeniesienie".
- Per repo glossary: "Merkle root" → "korzeń Merkle"; keep "Bitcoin Script", "Liquid Network", "Ethereum", "SHA-256", "Rocq", "DAG" (plural "DAG-i") verbatim.
- In Simplicity material, keep named effects in English as `Failure`, `Reader`, and `Writer`, but inflect the surrounding Polish phrase: `efekt Failure`, `efekt Reader`, `efekt Writer`.
- Render Simplicity `jets` as Polish `jety` in prose; keep inline code identifiers and jet names unchanged.
- Keep `Commitment Merkle Root (CMR)` in English as a Simplicity-specific commitment term; translate only surrounding explanation.
- Simplicity monadic effect names stay English, prefixed with `efekt`: `efekt Failure`, `efekt Reader`, `efekt State`, `efekt Writer`, `efekt IO`, `efekt Memory`, `efekt Continuation`, `efekt Nondeterminism`.
- `witness` kept verbatim (per glossary): `wartości witness`, `wyrażenia witness`, `transakcja witness`.
- `jet`/`jets` kept and declined as a Polish noun (`do jeta`, `poprzez jets`); combinator names (`take`, `drop`, `iden`, `case`, `O/I/H`) and identifiers (`bip0340-verify`, `sig-all-hash`, `TxEnv`, `PrecomputedTransactionData`) stay verbatim.
- Terminology: `sequent calculus` → `rachunek sekwentów`; `Curry-Howard` kept; `covenant` → `kowenant`; `sum/product type` → `typ sumy`/`produkt`; `tagged union` → `unia oznaczona`; `unit type` → `typ jednostkowy`; `Merkle root` → `Korzeń Merkle`.
- `on-chain`/`off-chain` kept verbatim; `CMR` acronym kept (plural `CMR-y`).
- Simplicity course (scr403): keep combinator names verbatim as identifiers — `iden`, `comp`, `take`, `drop`, `pair`, `case`, `injl`, `injr`, `copair`, `unit`, `scribe`, `fold-right-n`, `map`, `zip`, `push-<n`, `pop-<n`, and `half-adder`/`full-adder` (they appear both as prose and inside literal expressions like `half-adder⟨1,1⟩`). Decline them lightly in Polish (np. „dwa half-addery", „foldów").
- Keep verbatim: `jet` → "jet"; effect/monad names `Writer`, `Reader`, `Failure`; type `unit`; `CMR`, `NUMS`, `midstate`, `tag∥tag`, `bip0340-verify`, `sig-all-hash`, `SHA-256`, `Rocq`, `SimplicityHL`, `Taproot`, `BIP-0341`.
- Term renderings used: sum/product type → „typ sumowy/produktowy"; carry (bit) → „(bit) przeniesienia", carry-in → „przeniesienie wejściowe", sum bit → „bit sumy"; bookkeeping (Bit Machine) → „operacje porządkowe"; commutative/idempotent/unitary → „przemienny/idempotentny/unitarny"; Merkle root → „korzeń Merkle"; pruned branch → „przycięta gałąź"; witness → „świadek"; key-spend / key-path spend → „wydatek ścieżką klucza", script path → „ścieżka skryptu"; discrete log → „logarytm dyskretny"; on-chain → „on-chain".
- YAML: mirror source quoting — double-quote any scalar whose value contains `: ` (colon+space); plain scalars beginning with `⟨`, `(` or `push-<n` are valid and match the source. `explanation: >-` folded blocks: keep all content lines at a uniform 2-space indent, and do not split an inline `` `...` `` backtick span across a fold line (so its content stays byte-identical).
