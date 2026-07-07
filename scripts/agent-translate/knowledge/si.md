# Lessons — si

## 2026-07-03
- For Sinhala Simplicity/type-theory quizzes with no Sinhala glossary entries, keep specialized terms such as `combinator`, `product type`, `sum type`, `unit type`, `value`, `input`/`output`, `jets`, `DAG`, `static analysis`, and `gas model` in English, translating only the surrounding prose.
- If a YAML scalar starts with a quoted English term such as `'take'`, wrap the entire Sinhala value in double quotes so the embedded single quotes remain text and the YAML stays valid.
- The `scr403/quizz` si set follows an OLDER, shifted numbering: some English quizzes already have an exact si translation under a different number (e.g. en `017` = si `018`, en `025` = si `027`). Before translating a quiz, grep existing `*/si.yml` for the topic and reuse the wording verbatim for consistency; the offset is NOT constant.
- Register: keep technical nouns/identifiers in English inside Sinhala sentence frames — `Simplicity`, `combinator`, `branch`, `input`/`output`, effect names (`Failure`/`Reader`/`Writer` effect), `jet`, `Taproot`, `CMR`, `type`, `signature`, `exception`, `commutative`, `idempotent`. Translate ordinary verbs/adjectives (e.g. `predictable` → `පුරෝකථනය කළ හැකි`, `useful` → `ප්‍රයෝජනවත්`, `important` → `වැදගත්`). Do NOT add invented `(English gloss)` parentheticals not present in the source.
- YAML gotcha: a plain scalar cannot start with `'`. When a question naturally begins with a quoted term (e.g. `'case' combinator ...`), wrap the whole value in double quotes; this keeps valid YAML without changing the parsed structure.
- Render `e.g.,` as `උදා.,` (matches existing si files).
- In Sinhala Simplicity material, keep protocol/product/function names and effect names in English: Simplicity, SimplicityHL, Taproot/TapLeaf/Tapscript, Schnorr, CMR, jets, Reader effect, Failure effect, `bip0340-verify`, `sig-all-hash`, `PrecomputedTransactionData`.
- Translate “combinator” as “සංයෝජකය” in prose, but keep code-like combinators/access notation such as `take`, `drop`, `iden`, O/I/H verbatim.
- For Simplicity/formal-methods quiz terms such as `commutative`, `idempotent`, `unitary`, `jet`, `CMR`, `NUMS`, and combinator names, keep the English term in Sinhala prose and attach Sinhala particles/suffixes around it; translating them risks obscuring the term-of-art.
