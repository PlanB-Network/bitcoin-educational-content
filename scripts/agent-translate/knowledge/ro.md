# Lessons — ro

## 2026-07-03
- Keep Simplicity/Bitcoin technical terms in English as loanwords per existing `courses/scr403/ro.md`: "combinator(i)", "jet(s)", "witness", "case", "take"/"drop", "buffer(e)", "input"/"output", "covenant-uri", "sandbox".
- Standard renderings used elsewhere in this course: "efect Failure"/"efect Reader" (not translated), "compunere condițională"/"compunere paralelă" for conditional/parallel composition, "Commitment Merkle Root (CMR)" left as-is, "sistem de tipuri", "computație" for computation.
- "verification-in-batch" → "verificare în lot"; "unbounded recursion/iteration" → "recursivitate/iterație nemărginită"; "loop unrolling" → "desfășurarea buclelor".
- Plural of English loanwords follows Romanian agglutination with hyphen where natural (e.g. "jets-urile", "covenant-uri", "input-uri") — but bare "jets"/"combinatori" also occur in the reference doc; prefer the Romanian plural "combinatori" (native plural exists) over "combinators".
- Simplicity DSL combinator names (`iden`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`, `copair`, `fold-right-n`, `map`, `zip`, `push-<n`, `pop-<n`) and system terms (`jet`, `CMR`, `Bit Machine`, `NUMS`, `Reader`/`Writer`/`Failure` effects) stay in English verbatim — treated as code/identifiers, not prose.
- English jargon with no crisp 1:1 Romanian equivalent (e.g. "bookkeeping", "midstate", "key-spend", "padding") is translated with a natural Romanian phrase followed by the English term in parentheses on first use in that file, e.g. "contabilizare (bookkeeping)", "stare intermediară (midstate)", "cheltuire prin cheie (key-spend)".
- "half-adder"/"full-adder" rendered as "semi-sumator"/"sumator complet", with the English term kept in parentheses on first mention.
- Diacritics/mathematical notation (⟨⟩, ▵, ⨾, ᶜ, ᑉⁿ, ⊢, ×, ₊/₋ superscripts) copied byte-identical from source, never re-typeset.
- Simplicity domain terms kept in English (verbatim, lowercase): combinator names `iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`; also `jet(s)`, `Merkle`, `DAG`, `Bitcoin Script`, `Liquid`, `Rocq`, `SHA-256`, `AND`/`OR`/`XOR`/`NOT`.
- "jet" → "jet-ul"/"jet-urile" (Romanian agglutination with hyphen), same pattern for other English tech nouns needing RO articles/plurals (e.g. "DAG-uri", "buffere").
- "half-adder" rendered as "semi-sumator (half-adder)" — gloss the RO term once, keep English in parens for searchability.
- "static analysis" → "analiză statică"; "dynamic gas model" → "model dinamic de gas" (gas stays English as an Ethereum-specific term).
- "denial-of-service" kept verbatim (established English term in RO tech writing).
- "Combinator" translates as "combinator" (identical CS/math term in Romanian); keep all nine combinator names (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`) verbatim as code, never translate them.
- No `ro.md` glossary entries exist yet for Taproot/witness/script family terms in this repo — kept "Taproot", "witness", "jet(s)", "NUMS", "TapLeaf", "TapTweak", "Bech32m" verbatim (standard practice for untranslated Bitcoin protocol terms in ro content).
- "tweak"/"tweaking" (BIP-341 key tweaking) rendered as "twist-ui/'twist-uire' (tweaking)" with the English term parenthesized on first use per occurrence, since no established Romanian equivalent exists.
- "sequent calculus" → "calculul secvenților"; "sum type"/"product type" → "tip sumă"/"tip produs"; kept mathematical notation (⟦⟧, σᴸ, σᴿ, ⊢, ▵, ⨾) untouched as required.

## 2026-07-06
- In Romanian political-philosophy prose, render Anglo-Saxon “libertarian” as „libertarian/libertarieni”, and French *libertaire* as „libertar/libertarii” to preserve the course’s contrast between the two traditions.
- For the course’s political-axis vocabulary, use „clivaj stânga-dreapta”, „axa libertate-constrângere”, „statism”, „ordine spontană” and „ordine construită” consistently.
- Translate glossary link text when it is ordinary prose („cryptocurrency” → „criptomonedă”, „inflation” → „inflație”, „cryptography” → „criptografie”, „White Paper” → „Cartea albă”), but keep established technical loanwords such as „peer-to-peer”, „open source”, „cypherpunk”, „fiat” and „bailouts” in English.
- For political-economy quizzes in Romanian, render “moral hazard” as the established economic term “hazard moral” / “hazardul moral”.
- Use “libertarian” → “libertarian” / “libertarieni” for the political family; avoid “liberal” to prevent confusion with Romanian/European liberalism.
- Political-family terms: "conservatism" → "conservatorism", "libertarianism" → "libertarianism", "libertarians" → "libertarieni", "centrism" → "centrism".
- Keep "Federal Reserve" and "laissez-faire" verbatim in Romanian political/economic quiz text.
- In centrist economics context, render "pro-business" as "pro-business" and "pro-market" as "pro-piață" to preserve the contrast.
- "Sound money" can be rendered naturally as "bani solizi" in Romanian Bitcoin/economics material.
- In SOC104 political-theory quizzes, keep the French anarchist term `libertaires` verbatim in Romanian to distinguish it from `libertarieni` for libertarians; use `perspectiva libertaire` when an adjective is needed.
- Render `non-aggression principle` as `principiul non-agresiunii`, `civil disobedience` as `nesupunere civilă`, and `spoliation` as `spoliere` in this context.
- Keep `Green New Deal` verbatim in Romanian political-economy content.
- For `soc104` political/Bitcoin quizzes, keep movement/protocol labels such as `Cypherpunk`, `cypherpunk`, `Bitcoin White Paper`, `genesis`, `fiat`, and `mining` as established Romanian tech/political loanwords rather than forcing calques.
- Render privacy in the cypherpunk/libertarian context as `confidențialitate`, not `intimitate`, to match the technical sense of transaction/data privacy.
- Keep `bailout` in English when referring to bank rescues in the Genesis Block headline context; it is common Romanian financial jargon and preserves the historical phrase's register.
- For political-economy quiz terms, keep English labels `pro-business` and `pro-market` verbatim when they name contrasted ideological positions; translate surrounding prose and Romanian-articulate only generic nouns.
- Render `individualism vs. collectivism` as `individualism versus colectivism` in headings/questions to keep the explicit debate framing clear.
- For SOC104 political-spectrum content, render "Nolan diamond" as "diamantul Nolan" and "Nolan diagram" as "diagrama Nolan"; translate "statism/statists" as "etatism/etatiști".
- For SOC104 political terminology, render “statism/statist” as “etatism/etatist”.
- Render the political current “libertarian/libertarianism” with Romanian forms where grammar requires them: “libertarian”, “libertariană”, “libertarieni”, “libertarianism”.
- Keep institution and program names such as “Cato Institute”, “Mises Institute”, “Libertarian Party”, “New Deal”, “Great Society”, and “Big Government” in English.
