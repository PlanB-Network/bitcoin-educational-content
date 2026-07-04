# Lessons — sv

## 2026-07-03
- Simplicity combinator/primitive names (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`, `and`, `xor`) stay verbatim as code identifiers — never translated or declined.
- Math notation (𝟙, 𝟚, ⟨⟩, ▵, σᴸ, σᴿ, superscripts) kept byte-identical.
- "carry bit" → "minnessiffra-biten" (adder context); "half-adder" → "halvadderare".
- "Rocq proof assistant" → "beviskontrollsystemet Rocq" (adds a generic Swedish descriptor before the proper name, kept the name itself in English/unchanged).
- "gas model" (Ethereum) → "gasmodell"; "denial-of-service via resource exhaustion" → "överbelastningsattacker via resursuttömning".
- Keep Simplicity/Bitcoin protocol jargon untranslated: "kombinator" (combinator, Swedish CS term), but "jet", "Failure effect"/"Reader effect" (as "Failure-effekten"/"Reader-effekten" with Swedish suffix -en), "case", "take"/"drop"/"iden", "covenant" (as "rekursiva covenants", per glossary `recursive-covenant` which uses "avtal"/"covenant" interchangeably but source docs favor keeping "covenant").
- "Merkle Root", "Taproot", "TapLeaf", "Tapscript", "Schnorr" stay in English per `resources/glossary/*/sv.md` convention (borrowed English terms, capitalized as proper nouns).
- "witness values" -> "vittnesvärden" (per glossary `transaction-witness` -> "vittne").
- Formal notation (⊢, ×, +, Xᑉ⁸, superscripts) copied verbatim — never touch math/type-theory symbols.
- "jets" kept as-is (untranslated technical noun, no Swedish plural suffix needed since it functions as a loanword in this domain).
- No glossary entries exist for Simplicity-specific CS/type-theory jargon (combinator, sum/product/unit type, sequent calculus). Rendered as: "kombinator", "summtyp", "produkttyp", "unit-typ", "sekvenskalkyl", "typinferens", "föravtryck" (pre-image). Kept as-is in English where Swedish CS usage typically does too: "jet", "witness", "buffer" (as "buffert"), "CMR", "TapLeaf/TapTweak/TapTree".
- Reference tables (`| Combinator | Purpose |` etc.) have their header row and prose cell values translated, but code-identifier cells (tag pre-images, CMR formulas, hex values) stay verbatim. Watch for the `|---|---|` separator row directly below the header — easy to drop by accident when swapping just the header line.
- "Failure effect" / "Reader effect" / "Writer effect" kept in English as proper names (capitalized), consistent with how "Bit Machine" is also left untranslated as a proper name.
- "block space" left untranslated (established English loanword in Swedish Bitcoin writing); "standardness" also left untranslated as a technical term with no established Swedish rendering.
- Simplicity core-combinator identifiers (`iden`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `unit`, `scribe`, `copair`, `fold-right-n`, `map`, `zip`), formal type judgements (`A × B ⊢ B × A`), and expression fragments like `case (injl iden) (injr iden)` are treated as code/notation and left byte-identical even outside fenced/inline code markup — only surrounding prose is translated.
- Domain jargon (`carry`, `jet`, `NUMS point`, `CMR`, `Reader`/`Writer`/`Failure` effects, `Bit Machine`, `key-path`/`key-spend`, `half-adder`/`full-adder`, `push-<n`/`pop-<n`, `midstate`) is kept in English inline within Swedish prose (established convention in Bitcoin/crypto Swedish technical writing); compose Swedish grammar around them with hyphenation, e.g. "carry-bitarna", "half-adderns", "key-path-signatur".
- "hand off / hand to" in a computation-trace context → "skicka vidare till"; "stage" → "steg".
