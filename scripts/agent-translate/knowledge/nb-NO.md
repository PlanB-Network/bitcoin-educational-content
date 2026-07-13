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

## 2026-07-06
- In Bastiat/social-philosophy SOC content, render “spoliation” as “plyndring” (and “legal spoliation” as “legal/juridisk/lovlig plyndring” according to local context), matching existing nb-NO course translations.
- Keep French “libertaire(s)” untranslated when contrasted with “libertarian/libertarianere”; translating both would erase the course’s conceptual distinction.
- For SOC104 political philosophy quizzes, render `libertarian(s)` as `libertarianer(e)` and `libertarian` adjective as `libertariansk`, with `libertarianisme` for the doctrine.
- Keep `pro-business` and `pro-market` as English policy labels, adding Norwegian compounds around them where needed (e.g. `Pro-business-forkjempere`, `pro-market-synet`) to avoid confusing them with generic “næringslivsvennlig”/“markedsvennlig”.
- `spontaneous order` → `spontan orden`; `constructed/constructivist order` context → `konstruktivisme` / `sosial orden`, preserving Hayek/Popper philosophical register.
- Political term "statism" → "statisme" (not "statistikk/statistisk"); use compounds like "statisme-paradigme" / "statisme-postulat" and phrasing like "statsorienterte termer" when translating "statist terms".
- Keep the French political label *libertaire* untranslated and italicized when contrasted with English/Norwegian "libertarianer", to preserve the conceptual distinction between socialist anarchism and libertarianism.
- Render "libertarian" consistently as "libertarianer" and "libertarianism" as "libertarianisme" in political-philosophy context; avoid "liberalist" because the course explicitly distinguishes these terms.
- In political-economy quizzes, keep contrastive English labels like `pro-business` and `pro-market` untranslated when the distinction itself is being tested; translate the explanatory prose around them.
- `sound money` → `solide penger`; `fiat money` → `fiatpenger`; keep `Federal Reserve` and `Bitcoin` verbatim.
- `non-aggression principle` → `ikke-aggresjonsprinsippet`; `self-ownership` → `selveierskap`; `night-watchman state` → `nattvekterstaten`.
- For SOC/political-theory quizzes, render "statism" as "statisme" and "statist" as "statist"/"statistisk" depending on noun/adjective use.
- Keep US institution and party names verbatim: Cato Institute, Mises Institute, Libertarian Party, New Deal, Great Society, Big Government.
- Render "paleo-libertarianism" as "paleo-libertarianisme" and "neo-libertarianism" as "neo-libertarianisme"; use "libertarianer/libertariansk" for person/adjective, but keep quoted English labels like 'libertarian' when the question is about the US term itself.
- Political-theory quiz terms: “Nolan diamond” → “Nolan-diamanten” and “Nolan diagram” → “Nolan-diagrammet”; keep Nolan as proper name and hyphenate compounds.
- In SOC/political philosophy context, “libertarianism/libertarian” → “libertarianisme/libertariansk”, “statism/statist” → “statisme/statist”, “minarchist” → “minarkist”, and “anarcho-capitalist” → “anarkokapitalist”.
- Monetary terms in civic/political prose: “fiat money system” → “fiatpengesystemet”, “fiat currency” → “fiatvaluta”, and “money creation” → “pengeskaping”.
- In SOC/libertarian political quiz material, render “libertarian” as “libertariansk” and “libertarians” as “libertarianere”; avoid “liberalistisk” unless the source says liberal/liberalism.
- Keep “Cypherpunk” capitalized when naming the movement/list/manifesto, but use Norwegian inflection for people: “cypherpunkere/cypherpunkerne”.
- Render “constructivism/anti-constructivism” as “konstruktivisme/anti-konstruktivisme” in political-philosophy contexts.
- In political-family SOC104 quizzes, render “libertarian(s)” as “libertarianer(e)” and adjectival “libertarian” as “libertariansk”; use “sentrister/sentristisk” for centrists/centrist.
- In this political context, “statist” means state-centered/etatistisk, not “statistisk” (statistical).
- Keep the economics term “moral hazard” in English in nb-NO prose; explain around it in Norwegian rather than forcing “moralsk hasard”.
