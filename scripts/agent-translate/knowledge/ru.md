# Lessons — ru

## 2026-07-03
- "jet" → «джет» (transliteration, not «форсунка»/«реактивный»); "combinator" → «комбинатор» — both are the established Russian Bitcoin-dev rendering, confirmed via web search and consistent with how the community writes about Simplicity.
- "Commitment Merkle Root (CMR)" → «корень Меркла обязательств (CMR)» — keep the `CMR` abbreviation itself untranslated/unchanged everywhere it recurs (formulas, prose), matching `resources/glossary/merkle-root/ru.md` ("Корень Меркла") and `resources/glossary/commitment/ru.md` ("Обязательство").
- Taproot machinery (Taproot, TapLeaf, TapBranch, TapTree, TapTweak, NUMS point, bech32m, key-spend/script-spend path) stays untransliterated per `resources/glossary/taproot/ru.md` convention — only surrounding prose is translated (e.g. "путь key-spend", "NUMS-точка").
- "sum type" / "product type" → «тип-сумма» / «тип-произведение» (hyphenated compound, not «суммарный тип»); "tagged union" glossed inline as «размеченное объединение» on first use only.
- "witness expression" / "witness data" → «выражение-свидетель» / «данные свидетеля», consistent with `resources/glossary/transaction-witness/ru.md` using «свидетель» for witness (not a transliteration).
- Sequent calculus / Gentzen → «секвенциальное исчисление Генцена»; Curry-Howard → «соответствие Карри — Ховарда» (em dash with spaces, standard RU typographic convention for compound proper names).
- Simplicity combinator/type names (`comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `iden`, `unit`, `and`, `xor`, `scribe`) stay untranslated (they're code identifiers, not prose), even outside backtick spans — matches source convention.
- "jet(s)" → «джет(ы)» (transliteration), gloss as "джеты (jets)" on first mention per file since no glossary entry exists.
- Keep Unicode math glyphs (𝟙, 𝟚, ⟨⟩, ▵, σᴸ, σᴿ, superscripts) byte-identical; only translate surrounding prose.
- "sum type" → «суммарный тип», "product type" → «тип произведения», "tagged union" → «помеченное объединение», "DAG" kept as Latin acronym (не «ДАГ»).
- When the translated answer/value contains a colon (e.g. "A tagged union: ..."), wrap it in double quotes exactly as the English source did, to keep valid YAML.
- Simplicity-specific terms kept in English/Latin script (proper nouns of the spec, no established RU equivalent): `Bit Machine`, `SimplicityHL`, `TapLeaf`, `CMR`/`Commitment Merkle Root`, `Reader`/`Failure` (effect names), `PrecomputedTransactionData`, `TxEnv`.
- `jet` → transliterated as `джет`/`джеты` (declines like a Russian noun); no RU glossary entry exists for it.
- `witness` → `свидетель` (matches `resources/glossary/transaction-witness/ru.md` "Транзакционный свидетель"); "witness values" → "значения свидетеля".
- `covenant` → `ковенант` (per `resources/glossary/recursive-covenant/ru.md`); `Taproot`/`Tapscript` stay untranslated per glossary.
- `sequent calculus` (Gentzen) → `секвенциальное исчисление`; `natural deduction` → `естественный вывод`; `Curry-Howard correspondence` → `соответствие Карри-Ховарда`.
- Preserve the source's per-field YAML quoting exactly (some quiz files quote `question`/`answer`/`wrong_answers`, others don't) — copy the quoting style line-by-line rather than normalizing it.
- Simplicity core-combinator identifiers (`case`, `injl`, `injr`, `pair`, `copair`, `take`, `drop`, `iden`, `comp`, `scribe`, `unit`, `dist`, `fold-right-n`, `map`, `zip`, `push-<n`, `pop-<n`) stay in Latin script even outside backticks — they're code, not prose (confirmed against the `fr` translations of the same quiz set).
- "Bit Machine", "Reader"/"Writer" (effect names), "Failure", "Rocq", "NUMS", "Taproot", "CMR" stay untranslated as proper nouns/acronyms.
- "jet" → "джет"; "combinator" → "комбинатор"; "half-adder" → "полусумматор"; "full-adder" → "полный сумматор" (translate in prose, but keep literal `half-adder` when it appears as a bare combinator-name token inside a formal expression, e.g. `⨾ half-adder`).
- "witness" (Bitcoin tx witness / Simplicity witness expressions) → "свидетель", matching `resources/glossary/transaction-witness/ru.md`; "Merkle root/tree" → "корень Меркла"/"дерево Меркла" per `resources/glossary/merkle-root/`, `merkle-tree/`.
- "bookkeeping" (Bit Machine implementing combinators without copying data) → "учёт"/"за счёт учёта, без копирования данных".
- "key-path spend" / "script path" → "трата по пути ключа" / "путь скрипта"; "internal key" → "внутренний ключ".
