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

## 2026-07-06
- For SOC104 Hindi quizzes, match the course precedent’s heavy Hinglish register: keep `Bitcoin`, `fiat`, `Cypherpunk(s)`, `libertarian`, `centralization`, `coercion`, `consent`, `privacy`, `market/state`, and similar philosophy/political terms in English while translating connective prose.
- Preserve the Genesis block newspaper headline verbatim in English when it is cited as the embedded message; translate only the surrounding explanation.
- For SOC104 Hindi quizzes, translate standard political concepts into natural Hindi (`statism` → `राज्यवाद`, `political/cultural conservatism` → `राजनीतिक/सांस्कृतिक रूढ़िवाद`, `spontaneous order` → `स्वस्फूर्त व्यवस्था`, `left/right` → `वामपंथ/दक्षिणपंथ`) while preserving proper nouns such as `Nolan diagram`, `Cato Institute`, `Mises Institute`, and named parties.
- For US/Europe ideology labels with ambiguous local meanings, keep the quoted English word when the question is about the term itself (`'liberal'`, `'libertarian'`), but use Hindi/transliterated forms in explanatory prose when they function as ordinary concepts (`लिबर्टेरियन`, `शास्त्रीय उदारवादी`).
- For SOC104 Hindi, keep recurring political-philosophy labels in consistent Hinglish when no glossary entry exists: `libertarian` → `लिबर्टेरियन`, `conservative` → `कंजरवेटिव`, `centrist` → `मध्यमार्गी`, and leave `libertaire` as the French term to avoid confusing it with `libertarian`.
- Render the course’s main axis as `स्वतंत्रता-बलप्रयोग`; use `statism` consistently for the doctrine when contrasting it with libertarianism, with surrounding Hindi prose.
- SOC104 Hindi: keep French `libertaires` in Latin script to distinguish it from English `libertarians`/`libertarianism`, and translate the surrounding prose.
- For political-economy SOC104 terms, prefer standard Hindi renderings: `private property` → `निजी संपत्ति`, `capitalism` → `पूंजीवाद`, `socialism` → `समाजवाद`, `state` → `राज्य`, while keeping named course labels like `Green New Deal`, `utopian socialism`, and `scientific socialism` in English.
- In the Bastiat/Friedman context, render `spoliation` as `लूट` rather than a literal legalistic term.
- For SOC104 Hindi quizzes, keep named political frameworks and ideology labels in English/Hinglish when they function as course labels: `Nolan diagram`, `Nolan diamond`, `Libertarianism`, `Conservatism`, `Socialism`, `Centrism`, `statism`, `authoritarian`, `anarcho-capitalists`, and `minarchists`; translate the explanatory prose around them.
- Use glossary-canonical `Fiat` for the term, rendering phrases like `Fiat currency` as `Fiat मुद्रा` rather than fully localizing the term.
- For SOC104 Hindi, mirror the existing course register: keep political-family terms and formal theory labels in Hinglish/English (`conservatism`, `libertarians`, `centrism`, `technocracy`, `non-aggression principle`, `minarchists`, `anarcho-capitalists`) and translate connective prose.
- Keep paired course terms `pro-business`/`pro-market`, `free market`, `fiat money`, `sound money`, `gold standard`, `Federal Reserve`, and `Bitcoin` in Latin script for consistency with the Hindi course file.
- For SOC104 political-philosophy quizzes in Hindi, render `libertarian` as `लिबर्टेरियन`, while translating related school labels as `केंद्रवादी`, `रूढ़िवादी`, `समाजवादी`, `व्यक्तिवाद`, and `सामूहिकतावाद`.
- Translate non-identifier theory terms when natural Hindi is clear: `axiom` → `स्वयंसिद्ध`, `constructivism` → `निर्माणवाद`, `spontaneous order` → `स्वस्फूर्त व्यवस्था`, `open society`/`closed society` → `खुला समाज`/`बंद समाज`.
- Keep contrast labels such as `pro-business` and `pro-market` in Latin script, then translate the surrounding explanation and economics vocabulary.
- For SOC104 Hindi political quizzes, render `totalitarianism` as `सर्वसत्तावाद` / `सर्वसत्तावादी शासन`, `classical despotism` as `शास्त्रीय निरंकुशता`, and keep named political-family labels in consistent Hinglish where natural: `कंजरवेटिव`, `लिबर्टेरियन`, `मध्यमार्गी`, `समाजवादी`.
- Translate `moral hazard` as `नैतिक जोखिम` in the subsidies/economics context.
- For “dominants/dominated” and “oppressor/oppressed” in SOC104, use paired Hindi terms `प्रभुत्वशाली/अधीनस्थ` and `उत्पीड़क/उत्पीड़ित` to preserve the analytical contrast.
