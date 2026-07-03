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
