# Lessons — nb-NO

## 2026-07-03
- Highly mathematical/formal content (Simplicity course): keep all combinator names, type notation (`𝟙`, `𝟚`, `A × B`, `σᴸ`, etc.) and pseudo-code blocks byte-identical; only translate the prose sentences around them, including inline glosses like "hva mangler funksjonstyper" for "it lacks function types".
- "smart contract language" → "smartkontraktspråk" (compound, no space), consistent with glossary `smart-contract` (Smarte kontrakter).
- Keep XOR, Taproot, SHA-256, NUMS, CMR, TapLeaf, TapTweak, Bech32m acronyms/protocol names in English/verbatim per glossary convention (`resources/glossary/taproot/nb-NO.md`, `resources/glossary/xor/nb-NO.md`).
- Domain terms rendered in Norwegian for readability but consistently: "sideeffekt" (side effect), "vitneuttrykk/vitnedata" (witness expression/data), "sekventkalkyle" (sequent calculus), "merket union" (tagged union), "deluttrykk" (subexpression), "beskjæring/beskjære" (pruning/prune), "innløsning" (redemption).
- Tables containing only technical identifiers/English descriptions (e.g. the nine-combinator summary table, the CMR tag-preimage table) were left untranslated since their cell content is code/protocol strings, not prose — translating "Purpose"/"Tag pre-image" column headers or English one-line descriptions there would risk drifting from the deterministic structure checker; left as-is is a judgment call, revisit if reviewer wants headers localized.
- Simplicity combinator names (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`) and formal-methods jargon (jets, DAG, Merkle-rot, Rocq) stay in English/verbatim — no established Norwegian rendering exists.
- "carry bit" → "mentebit", "half-adder" → "halvaddérer" (standard Norwegian CS/EE terms).
- Keep the YAML double-quoting on scalar `answer`/`question` values that start with a capital-inside-quote or contain a colon (source uses `"..."` when the string needs escaping) — mirror it in the translation to preserve structure parity.
- "tagged union" → "merket union"; "sum type" → "sumtype"; "product type" → "produkttype" (compounds, no space, matching Norwegian orthography).
- Simplicity/technical jargon (jets, combinators→kombinatorer, take/drop/iden, CMR, Bit Machine, SimplicityHL) kept mostly as-is or literally translated; "jet" stays English (established Bitcoin dev term), "combinator" → "kombinator".
- "witness values" → "vitneverdier" (per `resources/glossary/transaction-witness/nb-NO.md` term "vitne"); "witness expressions" → "vitneuttrykk".
- "batch verification" → "batch-verifisering" (kept "batch" English, per `resources/glossary/batched-spending/nb-NO.md` using "Batched spending" untranslated).
- "sequent calculus" → "sekvenskalkyle"; "natural deduction" → "naturlig deduksjon"; "lambda calculus" → "lambdakalkyle"; "Curry-Howard correspondence" → "Curry-Howard-korrespondansen".
- Keep proper/product names untranslated: Taproot, TapLeaf, Tapscript, Bit Machine, SimplicityHL, PrecomputedTransactionData, Reader/Failure/State/Writer/IO/Memory/Continuation/Nondeterminism effect names.
- Simplicity/Bitcoin technical vocabulary kept in English (unchanged) throughout: jet, Bit Machine, Reader/Writer/Failure effects, midstate, Merkle root, key-spend/key-path, script path, NUMS point, half-adder/full-adder combinator expressions (`case`, `injl`, `injr`, `take`, `drop`, `pair`, `iden`, `comp`, `unit`, `scribe`, `fold-right-n`, `map`, `zip`, `push-<n`, `pop-<n`), Rocq, SimplicityHL.
- "carry" (bit) → "mente"; "carry-in" → "inngående mente"; verb "to carry" (arithmetically) → "gi mente".
- "sum bit" → "sumbit"; "half-adder"/"full-adder" left untranslated as they name the combinator/circuit, not translated to Norwegian equivalents ("halvaddér"/"helladdér") since surrounding code identifiers reference them literally (e.g. `⨾ half-adder`).
- "commutative/idempotent/unitary" → "kommutativ/idempotent/unitær" (adjective agreement with "effekt(en)").
- Keep all mathematical/Simplicity notation (⟨⟩, ▵, ⨾, σᴸ, σᴿ, Aᑉⁿ, etc.) byte-identical; only surrounding prose is translated.
