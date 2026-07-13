# Lessons — es

## 2026-07-03
- "jets" (Simplicity execution shortcuts) stays untranslated as "los jets" — no established Spanish equivalent in the glossary.
- "witness"/"witness expression" kept as "testigo"/"expresión de testigo" for the noun, but the `witness` combinator name itself stays in English/code font since it's an identifier.
- "covenant" kept as "covenant" (English loanword, per `resources/glossary/covenant/es.md`); "recursive covenant" → "covenant recursivo" (glossary uses "pacto recursivo" as prose gloss, but "covenant" is the term actually used across the corpus).
- Math/notation tables (Combinator/Tag pre-image/CMR rule/Effect classification tables) were left with English column headers and cell content untouched since they are technical notation, not prose — only surrounding prose was translated.
- "sequent calculus" → "cálculo de secuentes"; "Curry-Howard correspondence" → "correspondencia de Curry-Howard" (standard Spanish math terminology).
- Simplicity core-combinator names (`iden`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`, `unit`, `copair`) stay in English/verbatim as code identifiers, never translated or transliterated.
- Domain terms kept in English with a parenthetical Spanish gloss on first use per file: "búfer (buffer)" not needed for common loanwords like "búfer", but less common ones like "jet", "Merkle root" → "raíz de Merkle", "midstate" → "estado intermedio (midstate)", "tweak" → "ajuste (tweak)", "key-spend"/"key-path" → "gasto por clave"/"vía de clave", "witness" → "testigo (witness)".
- "half-adder"/"full-adder" rendered as "semisumador"/"sumador completo" but the literal combinator-code token `half-adder` inside pseudo-code expressions (e.g. `⨾ half-adder`) is left verbatim since it's part of a formal expression, not prose.
- "Bit Machine" → "Máquina de Bits" (proper noun, consistently capitalized).
- "Nothing-Up-My-Sleeve" kept in English with Spanish gloss "(sin trampa a la vista)" on first mention.
- Simplicity/Bitcoin Script formal-semantics vocabulary: keep "combinador(es)" for combinator(s), "tipo suma"/"tipo producto" for sum/product type, "raíz de Merkle" for Merkle root, "grafos acíclicos dirigidos (DAG)" for DAG, "semisumador" for half-adder, "acarreo" for carry, "asistente de pruebas" for proof assistant.
- Keep untranslated verbatim: combinator/type names and code identifiers (iden, unit, comp, pair, case, take, drop, injl, injr, and, xor, scribe), jets (kept as "jets", not translated), math notation (𝟙, 𝟚, ▵, ⟨⟩, σᴸ, σᴿ), and proper nouns (Rocq, Liquid Network → "red Liquid").
- "jet" stays untranslated in Spanish Bitcoin/Simplicity technical content (no established Spanish equivalent in this domain).
- Simplicity/Bitcoin technical vocabulary stays in English: `jet`, `covenant`, `combinator` → "combinador" is translated (standard CS Spanish term), but `jet`, `Taproot`, `Tapscript`, `TapLeaf`, `CMR`, `Bit Machine`, `SimplicityHL`, effect names (`Failure`, `Reader`, `State`, `Writer`, `IO`, `Memory`, `Continuation`, `Nondeterminism`) stay untranslated/capitalized as in source.
- "witness values" → "valores testigo" (consistent with glossary's "datos testigo" for witness data); "witness expressions" → "expresiones testigo".
- "batch verification" → "verificación por lotes".
- "Commitment Merkle Root (CMR)" → "Raíz de Merkle de Compromiso (CMR)".
- Type notation (`A + B`, `A × C ⊢ D`, `1 ⊢ 1`, etc.) and math symbols left byte-identical; only surrounding prose translated.

## 2026-07-06
- In SOC political-economy quizzes, render "pro-business" as "proempresarial" and "pro-market" as "promercado" to preserve the contrast between state-backed firms and free-market process.
- Render Popper's "open society" / "closed society" as "sociedad abierta" / "sociedad cerrada"; keep the terms lowercase unless the source treats them as titles.
- In SOC political-philosophy quizzes, render "libertarian/libertarianism" as "libertario/libertarismo"; use "liberalismo clásico" only for classical liberalism.
- "Welfare state" → "Estado del bienestar"; "sound money" → "dinero sólido" in Spanish monetary/political context.
- Keep "laissez-faire" untranslated; render "pro-business"/"pro-market" as "pro-empresa"/"pro-mercado" for contrastive political-economy questions.
- For SOC104 political terminology, follow existing `courses/soc104/es.md`: `statism` → `estatismo`, `libertarianism` → `libertarismo`, `libertarian` → `libertario`, `paleo-libertarianism` → `paleo-libertarismo`.
- Preserve US institution names in English when the Spanish course does so: `Cato Institute`, `Mises Institute`, `Libertarian Party`; translate only surrounding role descriptions.
- In political-philosophy course content, render English “libertarian/libertarianism” as “libertario/libertarismo”; keep the French left-anarchist term as italicized *libertaire(s)* to avoid Spanish ambiguity.
- Render “pro-business” as “proempresa” and “pro-market” as “promercado” when the text contrasts corporate-state alliance with free-market principles.
- Keep “fiat” as the loanword in monetary contexts: “dinero fiat” / “moneda fiat”, rather than “fiduciario”, when contrasting state money with Bitcoin.
- Historical quoted artifacts embedded in Bitcoin (e.g. the genesis-block Times headline) stay verbatim in English inside quotes; translate only the surrounding explanatory prose.
- In SOC104 political-theory quizzes, keep French socialist-anarchist `libertaires` as "libertaires" to preserve the source's contrast with right-libertarian `libertarians`, rendered as "libertarianos" / "libertarianismo".
- In political-economy quiz context, "moral hazard" → "riesgo moral" (standard Spanish term); keep it in quotes only when the English source puts the term in quotes.
