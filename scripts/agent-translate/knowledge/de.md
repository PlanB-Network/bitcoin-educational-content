# Lessons — de

## 2026-07-03
- Simplicity combinator names/type signatures (`case`, `pair`, `take`, `drop`, `iden`, `comp`, `injl`, `injr`, `scribe`, `dist`, `A × B ⊢ B × A`, `⟨a, b⟩`, jet/CMR names) are formal notation, not prose — keep byte-identical even when unquoted YAML values mix them with German sentences.
- Keep domain terms untranslated: Kombinator, Jet, CMR, Bit Machine, Halbaddierer/Volladdierer (compound is idiomatic German, used instead of "Half-/Full-Adder"), Writer/Reader-Effekt, NUMS-Punkt, Key-Path/Script-Path, Merkle-Wurzel, Taproot, Witness, Midstate.
- "kommutativ/idempotent/unitär" and "Vollständigkeitsbeweis" are the established German renderings for commutative/idempotent/unitary and completeness proof in this course's register.
- Inline code embedded in explanations (e.g. `f ⨾ unit = unit`, `bip0340-verify`) stays verbatim; wrap with backticks only where the source already implies a code token, otherwise leave untouched.
- Simplicity/Bitcoin-Script jargon (Kombinator, Jet, Witness, Failure-Effekt, Reader-Effekt, Covenant, Delegation, CMR, TapLeaf) stays in English/as established terms; only surrounding prose is translated.
- Glossary confirms: "Signatur" for signature, "Zeuge"/"Witness" (transaction-witness/de.md uses both "Zeuge" and "Witness" — prefer "Witness" when paired with technical terms like "Witness-Werte"/"Witness-Ausdrücke" for consistency with Simplicity docs), "Hash-Funktion" for hash function.
- Math/notation (⊢, ×, +, Xᑉ⁸, De Bruijn) and all formula-like expressions preserved verbatim, untranslated.
- "unbounded recursion/iteration" → "unbegrenzte Rekursion/Iteration"; "standardness" left as "Standardness" (established Bitcoin dev jargon, no good German equivalent in use).
- Simplicity core vocabulary (combinator names `iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`, `jet`) and type notation (`𝟙`, `𝟚`, `A + B`, `A × B`, superscript sizes) stay untranslated — treat as identifiers/math.
- "sum type" → "Summentyp", "product type" → "Produkttyp", "tagged union" → "getaggte Vereinigung", "left/right-tagged" → "links-/rechts-getaggt".
- "sequential/parallel composition" → "sequentielle/parallele Komposition"; "combinator" → "Kombinator".
- "half-adder" → "Halbaddierer"; "carry" → "Übertrag(sbit)"; "gas model" (Ethereum) → "Gas-Modell" (kept, capitalized as German noun).
- "Rocq proof assistant" → "Beweisassistent Rocq" (name kept, generic noun translated).
- Heavy type-theory/Simplicity vocabulary has no repo glossary entry: rendered "combinator"→"Kombinator", "sum type"→"Summentyp", "product type"→"Produkttyp", "unit type"→"Unit-Typ" (kept "Unit" untranslated, common German CS usage), "sequent calculus"→"Sequenzenkalkül", "witness expression"→"Witness-Ausdruck", "jets"/"Reader effect"/"Failure effect"/"Writer effect" left in English (established English technical terms in this domain, no natural German equivalent in use).
- Kept "Taproot", "Bitcoin Script", "key-spend path"→"Key-Spend-Pfad", "script path"→"Skriptpfad" consistent with existing glossary/taproot/de.md style (compound nouns with hyphens for English-German mashups, e.g. "Kombinator-Vollständigkeit", "Commitment-Merkle-Root").
- Kept all math/pseudocode blocks, tables headers (English column names like "Combinator | Purpose"), and identifiers fully verbatim — these are inside fenced code or table syntax, not prose.
- Rendered inline math prose terms consistently throughout: "principal type"→"principal-Typ" (kept English adjective, common in German type-theory writing) since no established German rendering found.
