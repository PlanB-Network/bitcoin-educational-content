# Lessons — nl

## 2026-07-03
- Dense math/formal-notation courses (Simplicity, sequent calculus, etc.): translate only surrounding prose; leave all `⟦…⟧`, `σᴸ`, `⊢`, `▵`, `⨾`, combinator names, and formula lines byte-identical, including inside fenced code blocks with mixed English annotations like `{evaluate case for σᴸ}` — do not translate those inline English comments inside code fences, they are part of the verbatim code block.
- Course/article titles that are themselves the name of an external English publication (e.g. "Delving Simplicity" article series) are kept in English even inside translatable link text; only the standalone descriptive course title (`name:` value, top `# heading`) gets translated.
- Register: use informal "je" throughout (consistent with other nl/ course translations, e.g. dev303), even for expert-level/academic content.
- Domain terms kept in English per existing convention (verified via absence of nl glossary overrides + established usage in other nl courses): Taproot, jet(s), witness, combinator(s), SHA-256, Schnorr, NUMS point, bech32m, sum type/product type notation, CMR. Coined Dutch renderings used consistently: "sequentenkalkul" (sequent calculus), "neveneffecten" (side effects), "opzoektabel" (lookup table), "getagde hash" (tagged hash).
- Simplicity technical terms kept in English (untranslated, no italics): combinator names (`iden`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `unit`, `scribe`, `fold-right-n`, `map`, `zip`), system/proper nouns (`Bit Machine`, `Merkle root` → "Merkle-root", `Taproot`, `NUMS point` → "NUMS-punt", `Reader`/`Writer`/`Failure` effect names, `SimplicityHL`, `Rocq`).
- "combinator" stays "combinator" in Dutch (not "combinator" → no native equivalent used); compounds like "kerncombinator" (core combinator), "kerntaal" (core language) work naturally with hyphenation when followed by a proper-noun-like jet/type name (e.g. "half-agg-verify-jet").
- "typing rules" → "typeregels"; "commutative/idempotent/unitary" kept as Dutch adjectives "commutatief/idempotent/unitair" (standard math/CS loanwords, no need to gloss).
- Keep single-letter/short mathematical notation (e.g. `O O H`, `▵`, `⨾`) and Unicode math symbols completely untouched — they are structural, not prose.
- Simplicity-specific jargon (Simplicity, combinator(s), jet(s), Bit Machine, take/drop/iden/injl/injr, Failure-effect, Reader-effect, CMR, TapLeaf) stays in English/untranslated — matches the existing `courses/scr403/nl.md` course file's established usage.
- "side effects" → "neveneffecten" (plural "de Failure- en Reader-neveneffecten"), consistent with `courses/scr403/nl.md`.
- "witness values"/"witness data" → keep "witness" untranslated (e.g. "witness-waarden", "witness-data"), not "getuige" — the course-level nl.md already uses "witness-data" rather than the glossary's "getuige".
- "covenant"/"recursive covenant" → "covenant"/"recursieve covenant(s)" (untranslated noun), matching `courses/scr403/nl.md`.
- "sum type"/"product type"/"unit type" → "somtype"/"producttype"/"unit-type", per established course terminology.
- Simplicity combinator names (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`) stay in English verbatim — they're code-level identifiers even inline in prose.
- Keep the special mathematical symbols (𝟙, 𝟚, ▵, σᴸ, σᴿ, ⟨⟩) byte-identical; don't attempt to transliterate or explain them.
- "jet" (Simplicity native implementation) stays untranslated as a term of art in Dutch, same as "gas model"/"gasmodel" for Ethereum's metering (translated as "gasmodel").
- "denial-of-service" stays in English (common Dutch technical usage); "resource" left in English too, matches established Dutch dev register (e.g. "resourcelimieten", "resourcegebruik").
- "Rocq proof assistant" → "Rocq-bewijsassistent" (translate "proof assistant" as compound, keep "Rocq" verbatim).

## 2026-07-06
- SOC political terminology: render `libertarian(s)` as `libertariër(s)` and adjectival `libertarian` as `libertarisch`; `spontaneous order` → `spontane orde`, `constructivism` → `constructivisme`, `central planning` → `centrale planning`.
- For the `pro-business` / `pro-market` distinction, keep `pro-business` as the English label and translate `pro-market` as `pro-markt` to preserve the conceptual contrast while sounding natural in Dutch.
- For SOC104 political terminology in Dutch: use `libertariër/libertarisch/libertarianisme` for `libertarian/libertarianism`; keep quoted historical English labels such as `libertarian`/`liberalism` when the sentence discusses US terminology itself.
- Keep `sound money` as English in Dutch when used as Austrian/libertarian monetary jargon; translate surrounding explanation normally.
- For the centrism distinction, keep `pro-business` as English and render `pro-market` as `pro-markt` to preserve the contrast used in the source.
- Political-spectrum terms in SOC quizzes: use "links-rechtsas" for "left-right axis", "links-rechtsverdeling" for "left-right divide", "Nolan-diagram"/"Nolan-diamant" for "Nolan diagram/diamond", and "statisme" for "statism".
- "Fiat money system" renders naturally as "fiatgeldsysteem" and "fiat currency" as "fiatgeld" in Dutch educational prose.
- For libertarian taxonomy, use "libertarisme"/"libertair", "anarcho-kapitalisten", and "minarchisten"; keep the informal "je" register in explanatory quiz prose.
- Political-philosophy distinction in SOC courses: keep French `libertaire(s)` as `libertaire(s)`, but translate English `libertarian(s)`/`libertarianism` as `libertariër(s)`/`libertarisme`; use adjective `libertarisch` for `libertarian position/ideal`.
- In SOC104 political terminology, keep the US labels `liberal`/`libertarian` in English when the quiz explicitly contrasts American and European usage; translate the ideology around them as "liberaal", "libertair", "libertariër" only when not naming the US label itself.
- Use "statisme" and "statisten" for `statism`/`statists` in the Nolan-diagram political-philosophy context; avoid "statisch", which means static rather than statist.
- SOC/Bitcoin political-philosophy quizzes: render "welfare state" as "verzorgingsstaat", "libertarian" as "libertair/libertariër", and "consent" as "instemming" when used as the justice principle.
- Keep named cypherpunk texts and embedded source quotations/headlines in English when they function as titles or historical artifacts (e.g. "Cypherpunk Manifesto", "Cypherpunks write code", genesis-block Times headline); translate only the surrounding prose.
- For SOC104 political/economic quizzes: render political families consistently as "libertariërs/libertarisch", "conservatieven/conservatief", "socialisten/socialistisch", and "centristen/centristisch"; use "moreel risico" for "moral hazard" in subsidy/bailout contexts.
