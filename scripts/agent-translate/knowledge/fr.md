# Lessons — fr

## 2026-07-03
- Simplicity/Bit Machine jargon (jet, combinator names `iden`, `comp`, `take`, `drop`, `pair`, `case`, `injl`, `injr`, `scribe`, `unit`, `fold-right-n`, `map`, `zip`, `push-<n`, `pop-<n`, Reader/Writer/Failure effect names, CMR, Bit Machine, midstate) stay in English verbatim — no French gloss needed, matches established Simplicity docs usage.
- "commutative/idempotent/unitary" and "commutatif/idempotent/unitaire" — keep as direct cognates; "unitary" → "unitaire" (not "unitary" nor "unaire").
- "NUMS point" → "point NUMS", keep the acronym; parenthetical gloss "Nothing-Up-My-Sleeve" stays in English (quoted) since it's a named cryptographic convention, not translated.
- "carry" (adder bit) → "retenue"; "half-adder"/"full-adder" → "demi-additionneur"/"additionneur complet".
- "lookup table" → "table de correspondance"; "witness" (Simplicity pruning context) → "témoin".
- Simplicity-specific named side effects (`Failure effect`, `Reader effect`, jet names like `bip0340-verify`, `sig-all-hash`, `PrecomputedTransactionData`, `TxEnv`) are treated as identifiers: keep the English name capitalized, translate only the surrounding prose (e.g. "l'effet Failure", "l'effet Reader").
- "combinator" → "combinateur"; "Merkle root" → "racine de Merkle" (per `resources/glossary/merkle-root/fr.md`); "witness" → "témoin" (per `resources/glossary/transaction-witness/fr.md`).
- "covenant" stays "covenant" in French Bitcoin material (per `resources/glossary/recursive-covenant/fr.md`); "recursive covenant" → "covenant récursif".
- Math/notation symbols (⊢, ⁸, ␟, Xᑉ⁸, O/I/H shorthand) and all identifiers (`case`, `iden`, `take`, `drop`, `1 ⊢ 1`) are left byte-identical; only the prose around them is translated.
- Simplicity-specific jargon: "combinator" → "combinateur", "jet" stays "jet" (untranslated, established term), "witness"/"témoin" (standard Bitcoin FR glossary rendering, e.g. `transaction-witness`), "key-spend path" → "chemin de dépense par clé", "NUMS point" → "point NUMS" (kept), "midstate" → "état intermédiaire (midstate)" on first use then "midstate".
- Keep all combinator/function identifiers (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`, `witness`, `dist`, `copair`, etc.), type notation (`𝟙`, `𝟚`, `A × B`, `⊢`), and De Bruijn-style `O`/`I`/`H` notation verbatim — these are code/formal-notation, not prose.
- "sum type" → "type somme", "product type" → "type produit", "tagged union" → "union étiquetée"; keep consistent throughout since the course leans on these terms heavily.
- Bitcoin Script term "concatenative programming language" → "langage de programmation concaténatif" (established CS French rendering).
- Simplicity glossary (Scriptless/scr403 course): keep combinator names, keywords and DSL terms verbatim in French (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `jet(s)`, `DAG`, `gas`) — no translation, matches existing usage in this course.
- Keep math notation identical (𝟙, 𝟚, ⟨⟩, ▵, σᴸ, σᴿ) and unicode operators unchanged.
- A YAML scalar `answer` starting with a colon-containing phrase (e.g. "A tagged union: ...") must be double-quoted in French too when the translated string itself contains a `: ` — otherwise YAML parses it as a mapping.
- "half-adder" → "demi-additionneur"; kept English term in parentheses on first use for clarity, consistent with the course's technical register.
- "gas model" (Ethereum) → kept "gas" untranslated ("modèle de gas"), standard usage in French crypto technical writing.

## 2026-07-06
- In SOC104 political terminology, preserve the French distinction: English `libertaires` → `libertaires` (socialist-anarchist current), English `libertarians` → `libertariens`, and `libertarianism` → `libertarianisme`, matching existing `courses/soc104/fr.md` usage.
- In SOC political-family quizzes, render “libertarian” as “libertarien” (not “libéral”) to preserve the ideology distinct from French liberalism.
- In economic-policy context, “moral hazard” → “aléa moral”, the standard French economics term.
- For healthcare policy questions, prefer “santé” for the policy sector and “soins de santé” for actual access/care delivery.
- In political-economy quiz prose, keep `pro-business` and `pro-market` in English when used as named ideological labels; translate only the surrounding syntax (e.g. "position pro-business", "partisans pro-market").
- In SOC political-economy quizzes, keep `pro-business` and `pro-market` in English when they are contrasted as labels; translate only the explanatory prose around them.
- For the Nolan diagram / political-spectrum context: render "libertarianism" as "libertarianisme", "libertarian" as "libertarien", and "statism" as "étatisme" to avoid confusion with French "libéralisme".
- For SOC/political Bitcoin quiz material, keep the embedded genesis-block headline byte-identical when quoted as the historical message; translate only the surrounding prose/description.
- Keep the cypherpunk slogan “Cypherpunks write code” in English when referenced as a named formula; translate only the surrounding explanation.
- In French SOC/political quizzes, render “libertarian” as “libertarien” and “libertarianism” as “libertarianisme”; keep U.S. labels like `liberal`, `libertarian`, `Big Government`, `New Deal`, `Great Society`, and party/institute names in English when the question is explicitly about the American term.
- “statism/statist” → “étatisme/étatiste”; “spontaneous order” → “ordre spontané”; “federal states” in the U.S. context → “États fédérés”.
