# Lessons — hi

## 2026-07-03
- Hindi Simplicity translations should keep protocol/API names and formal terms such as `Simplicity`, `Taproot`, `CMR`, `witness`, `combinator`, `type`, `Reader effect`, and `Failure effect` in English, while translating explanatory prose around them.
- Fenced code blocks and derivation comments inside them must stay byte-identical, even when the comments are English prose.
- Register for scr403 (Simplicity) quizzes is heavy Hinglish: keep technical terms in Latin script (`combinator`, `jet`, `batch verification`, `sum/product type`, `branch`, `signature`, `SimplicityHL`, `covenant`/`recursive covenants`, `delegation`, `completeness theorem`, `side effects`) and only translate the connective prose. This matches existing sibling files (003, 009, 021, 037, 038).
- "effect" (side effect) → transliterate as "इफेक्ट": e.g. `Failure इफेक्ट`, `Reader इफेक्ट` (per 024/025).
- "nine core combinators" → "नौ core combinators" (Hindi numeral word + English term); combinator names (take, drop, case, iden, injl, injr, pair, comp) stay verbatim English.
- YAML gotcha: when the question begins with a quoted identifier like `'take'`/`'case'`, wrap the WHOLE value in double quotes (`question: "'take' combinator..."`), otherwise YAML parses the leading `'...'` as a single-quoted scalar and breaks.
- Punctuation: end Hindi statements with danda "।" but keep the Latin "?" for questions; use em-dash "—" as in source. Keep `reviewed:` boolean and all math/identifiers (`⊢`, `×`, `⟨⟩`, `0xbe`, `TxEnv`, `PrecomputedTransactionData`, `Xᑉ⁸`, polynomials) byte-identical.
- For Simplicity course quizzes, keep protocol/API identifiers and formal terms verbatim: `Simplicity`, `SimplicityHL`, `sig-all-hash`, `bip0340-verify`, `TxEnv`, `PrecomputedTransactionData`, `take`, `drop`, `iden`, `TapLeaf`, and symbolic types such as `1 ⊢ 1`.
- Render named effects as `Failure इफेक्ट` and `Reader इफेक्ट`; keep the effect names in English to match the source terminology while translating the surrounding prose.
- For formal CS terms without a Hindi glossary entry in this course context, prefer consistent Hinglish (`combinator` → `कॉम्बिनेटर`, `type` → `type/टाइप`, `batch verification`, `fixed-point construction`) rather than inventing Sanskritized terms.
- For Simplicity quiz Hindi, keep combinator names, algebraic type expressions, proof/tool names, and protocol terms verbatim (`case`, `injl`, `iden`, `A × B ⊢ B × A`, `Rocq`, `Bit Machine`, `CMR`, `NUMS`, `key-spend`, `key-path`); translate only the surrounding explanatory prose.
- For advanced effect-system terms without a stable Hindi equivalent, keep `commutative`, `idempotent`, `unitary`, `Reader`, `Writer`, and `Failure` in English and attach Hindi grammar around them for consistency.
- For SCR403 Hindi, keep Simplicity-specific identifiers and established CS terms in English/Hinglish when the course precedent does so: `combinator`, `sum type`, `product type`, `unit type`, `static analysis`, `dynamic memory allocation`, `jet`, `DAG`, and code-like names such as `iden`, `comp`, `injl`.
- Keep boolean/logical operator names (`AND`, `XOR`, `NOT`, `false`, `true`) in English when they are concept labels or match notation; translate only surrounding explanatory prose.
