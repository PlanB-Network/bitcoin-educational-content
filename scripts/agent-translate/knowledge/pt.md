# Lessons — pt

## 2026-07-03
- "Witness" (Simplicity/Bitcoin context) → "testemunha" per `resources/glossary/transaction-witness/pt.md`; "witness values" → "valores de testemunha".
- Simplicity-specific jargon (combinator, jet, Reader effect, Failure effect, take/drop/iden, CMR, TapLeaf, PrecomputedTransactionData, batch verification) kept in English — no glossary entries exist, and these are established technical/API identifiers, not general prose.
- "recursive covenant" → "covenant recursivo" (glossary entry title is "Covenant recursivo", `resources/glossary/recursive-covenant/pt.md`); kept "covenant" itself untranslated per that entry's own usage.
- "standardness" (Bitcoin relay-policy term) left untranslated — no established PT equivalent in glossary or prior files.
- Math/notation (⊢, ×, +, superscripts, Xᑉ⁸, etc.) copied byte-identical; only surrounding prose translated.
- Simplicity/Bit Machine jargon (combinator names `iden`, `comp`, `take`, `drop`, `pair`, `case`, `injl`, `injr`, `scribe`, `unit`, `dist`, jet names, `CMR`, `NUMS`, `key-spend`) stays in English/verbatim — no Portuguese calques.
- "carry"/"sum" (adder bits) rendered as "carry"/"soma" — "carry" kept in English since it's the established term in this domain even in pt technical writing; "half-adder"/"full-adder" also left untranslated as compound technical names.
- "Reader"/"Writer"/"Failure" (Simplicity effect names) kept capitalized and untranslated as proper technical terms.
- "key-spend" and "key-path" left in English; "script path" → "caminho de script".
- Register: use Brazilian Portuguese conventions (você, "está impulsionando" not "está a impulsionar", gerund not "a + infinitivo").
- Section headings for the standard course footer are fixed by convention across the repo: "Seção final" (Final Section), "Avaliações & Notas" (Reviews & Ratings), "Exame final" (Final Exam), "Conclusão" (Conclusion) — verified against `courses/his201/pt.md` and `courses/biz101/pt.md`.
- Proper titles of external works cited inline (e.g. the "Delving Simplicity" article series title, the paper title *Simplicity: A New Language for Blockchains*) were kept in English/untranslated even though they appear as link text or emphasis — treated as citable external titles, not prose.
- Simplicity-specific jargon kept in English throughout: combinator names (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `witness`, `scribe`, `disconnect`), "jet(s)", "Bit Machine", "Commitment Merkle Root"/CMR, "NUMS point", effect names (Failure, Reader, Writer). Rendered as-is with Portuguese surrounding prose (e.g. "o efeito Reader", "os jets").
- Markdown table headers ("Combinator | Purpose", "Effect | Commutative | Idempotent | Unitary") were translated to Portuguese ("Combinador | Finalidade", "Efeito | Comutativo | Idempotente | Unitário") while backtick-quoted cell contents (combinator names, formulas) stayed verbatim.
- All fenced ``` code/math-notation blocks, including ones containing English glue prose like "If f : A ⊢ B and g : B ⊢ C, then", were left completely untouched per the hard rule — do not translate text inside code fences even when it reads as natural language.
- Simplicity technical vocabulary kept as-is (not translated): "Simplicity", "jets", "combinator" → "combinador", "case/comp/pair/take/drop/iden/unit/injl/injr" (combinator names verbatim), "DAG" → "DAG" (spelled out as "grafo acíclico direcionado" on first use in an explanation is fine, but keep the acronym "DAG").
- "sum type" → "tipo soma", "product type" → "tipo produto", "unit type" → "tipo unidade" — consistent across all scr403 quizzes.
- "smart-contract" → "contrato inteligente" (per resources/glossary/smart-contract/pt.md).
- "gas model" (Ethereum) → "modelo de gas" (kept "gas" untranslated, standard PT-BR/PT crypto usage).
- "half-adder" → "meio-somador (half-adder)" — gloss with English term in parentheses on first mention since no glossary entry exists.

## 2026-07-06
- In political-philosophy SOC content, render English “libertarian/libertarians” as “libertário/libertários” in Portuguese, but keep French-specific *libertaire/libertaires* untranslated when the text contrasts the Anglo-Saxon and French traditions.
- Political-theory terms in SOC104 quizzes: "Nolan diagram" → "diagrama de Nolan"; "Nolan diamond" → "losango de Nolan" to preserve the geometric distinction.
- Libertarian subtypes: "anarcho-capitalists" → "anarcocapitalistas"; "minarchists" → "minarquistas"; "statism/statists" → "estatismo/estatistas".
- In SOC/libertarianism context, keep French socialist-anarchist `libertaires` as `libertaires` to avoid collision with PT `libertários` for English `libertarians`; gloss once as `libertaires franceses (anarquistas socialistas)` when the source does.
- Quoted cypherpunk slogan "Cypherpunks write code" kept in English/verbatim as a movement motto; translate only the surrounding explanation.
- SOC/libertarian political terms: "libertarian" → "libertário"; "constructivism" → "construtivismo"; "spontaneous order" → "ordem espontânea"; "open/closed society" → "sociedade aberta/fechada".
- "pro-business" vs. "pro-market" rendered as "pró-empresas" vs. "pró-mercado" to preserve the contrast between protecting incumbent firms and defending market processes.
- In SOC/political-economy quizzes, "moral hazard" → "risco moral"; "bailouts" → "resgates" when referring to state/company financial rescues.
- "Libertarian(s)" in political-family labels → "libertário(s)"; keep distinct from "liberal" in Portuguese.
- "sound money" → "moeda sólida" in libertarian/Austrian monetary context; no repo glossary entry found, and it pairs naturally with "moeda fiat" and "padrão-ouro" in pt-BR.
- "pro-business" → "pró-empresas" and "pro-market" → "pró-mercado" to preserve the policy distinction between state-favored firms and free competition.
- In SOC104 political-axis context, render "societal freedoms/sphere" as "liberdades/esfera social" rather than the more literal "societal", matching existing course wording around personal/social freedoms.
- SOC104 political-philosophy terms: "statism" → "estatismo", "spontaneous order" → "ordem espontânea", "laissez-faire" kept as-is, matching existing pt quiz usage.
- In US/Europe liberalism contrast, keep the English labels `liberal`, `libertarian`, and `liberals americanos` when the text is explicitly about the English political labels; translate the philosophy/identity elsewhere as "liberalismo", "liberais clássicos", "libertário(s)".
