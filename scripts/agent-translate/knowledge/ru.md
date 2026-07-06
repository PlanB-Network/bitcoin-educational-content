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

## 2026-07-06
- `welfare state` → «государство всеобщего благосостояния» in SOC/political-economy context, not a literal «социальное государство» when the course stresses fiscal/monetary pillars.
- `cypherpunk(s)` → «шифропанк(и)»; keep the slogan `Cypherpunks write code` in English when quoted as the movement’s formula, translating only surrounding prose.
- The genesis-block headline `The Times 03/Jan/2009 Chancellor on the brink of a second bank bailout` is a historical embedded message; keep the quoted headline byte-identical in explanations while translating the paraphrased answer.
- `statism` in political-philosophy prose → «этатизм»; `statist` → «этатистский» / «этатист», not «государственничество».
- In this course context, `libertarian` → «либертарианец» / «либертарианство», while French `libertaire` is kept as `libertaire` to preserve the explicit contrast with Anglo-Saxon libertarianism.
- `cypherpunk(s)` follows the glossary canonical term «шифропанк(и)»; names of manifestos, institutes, book titles, and slogans such as `Cypherpunks write code` can remain in English when they function as proper titles/quoted formulas.
- In SOC/political-economy quiz context, "moral hazard" → «моральный риск»; keep it as the established economics term, not «моральная опасность».
- For social policy quizzes, "gay marriage" → «однополый брак» rather than colloquial «гей-брак».
- In SOC104 political-philosophy quizzes, render French `libertaires` as «либертеры» to distinguish them from libertarians («либертарианцы»/«либертарианство»), while preserving the left-anarchist sense.
- `Green New Deal` → «Зелёный новый курс» in Russian prose.
- In Bastiat/Friedman-style political economy context, `spoliation` can be rendered as «грабёж»/«форма грабежа» rather than a neutral «экспроприация».
- SOC104 political-spectrum terms: `Nolan diagram` → «диаграмма Нолана», `Nolan diamond` → «ромб Нолана», `statism` → «этатизм», `libertarianism` → «либертарианство».
- SOC104 libertarian-family terms: `anarcho-capitalists` → «анархо-капиталисты», `minarchists` → «минархисты».
- In this Russian SOC104 context, `left-right axis/divide` is rendered as «ось/деление левые–правые» with an en dash, while `top-bottom` is «верх–низ».
- In Russian political-economy prose, keep `pro-business` and `pro-market` in Latin script when they are contrasted as labels; translate only the surrounding explanation.
- `sound money` in libertarian/Bitcoin monetary context → «твёрдые деньги».
- In SOC/political philosophy quizzes, keep `pro-business` and `pro-market` as Latin-script policy labels; translate the surrounding explanation (e.g. «сторонники pro-market»), rather than forcing them into Russian paraphrases.
- Kant's "state of minority" in the Enlightenment context → «состояние несовершеннолетия»/«несовершеннолетие», the standard Russian philosophical rendering.
- Hayek's "spontaneous order" → «спонтанный порядок»; "central planning" → «центральное планирование».
- In `soc104`, keep American political labels/institution names in English where the Russian course text does: `liberals`, `Big Government`, `New Deal`, `Great Society`, `Cato Institute`, `Mises Institute`, `Libertarian Party`.
