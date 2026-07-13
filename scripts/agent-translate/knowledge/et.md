# Lessons — et

## 2026-07-03
- Keep Simplicity algebraic effect names in English (`Failure effect`, `Reader effect`, `State effect`, etc.) and translate only the surrounding explanation; they behave as named technical constructs.
- Keep Simplicity implementation terms such as `jet`, `SimplicityHL`, `TapLeaf`, `CMR`, `tagged SHA-256`, `tagged midstates`, and `covenant` in English when no Estonian glossary entry localises them; inflect with Estonian endings only when needed for readability.
- Translate mathematical/type-theory prose consistently with existing SCR403 Estonian quizzes: `unit type` → `ühiktüüp`, `product type` → `korrutistüüp`, `sum type` → `summatüüp`, `combinator` → `kombinaator`, and `conditional/parallel composition` → `tingimuslik/paralleelne kompositsioon`.
- Keep Simplicity core combinator identifiers (`iden`, `comp`, `take`, `drop`, `pair`, `case`, `injl`, `injr`, `unit`) verbatim in Estonian prose; inflect around them rather than translating the identifiers.
- Render Simplicity effect properties as `kommutatiivne`, `idempotentne`, and `unitaarne`; use `unitaarsus` for the property noun.
- For Taproot/Simplicity path terminology, prefer `võtmetee` and `skriptitee`; keep `NUMS`, `CMR`, `UTXO`, `jet`, `tweak`, and protocol names verbatim unless the glossary explicitly localizes them.
- Simplicity (scr403) core terms, aligned with `courses/scr403/et.md`: sum/product/unit type = `summatüüp` / `korrutistüüp` / `ühiktüüp`; boolean type = `tõeväärtustüüp`; combinators = `kombinaatorid` (core = `põhikombinaatorid`); false/true = `väär` / `tõene`; hash = `räsi`; truth table = `tõesustabel`; half-adder = `poolsummaator`; carry = `ülekanne`.
- Keep combinator names (`iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `scribe`) and all code/math (`f ▵ g`, `case (injl unit) (drop iden)`, `𝟙`, `𝟚`, `A⁴ = A² × A²`, `σᴸ⟨⟩`) byte-verbatim; attach Estonian case endings with a hyphen (`take-kombinaator`, `AND-i tõesustabel`).
- "Simplicity" is an invariant modifier before a noun (`Simplicity avaldis`, `Simplicity tüübid`); declined forms follow the course: inessive `Simplicitys` ("in Simplicity"), adessive `Simplicityl` ("Simplicity has").
- `jet` (Simplicity jets) has no glossary entry — treat as an Estonian loan with stem `jeti-`: sg `jet`, pl nom `jetid`, pl gen `jetide`.
- DAG → `suunatud atsükliline graaf`; keep the acronym and add hyphenated endings (`DAG-idena`, `DAG-vormingut`). Ethereum "gas" model → keep `gas` as `gas-mudel`.
- Simplicity efektinimed `Failure`, `Reader` ja `Writer` jäta ingliskeelseks ning kääna sidekriipsuga: `Failure-efekt`, `Reader-efekt`, `Writer-efekt`.
- Simplicity `jets` renderda eesti tekstis kui `jetid`/`jette`; koodis ja kombinaatorinimedes jäta algkuju muutmata.
- Tüübinimed: `unit type` → `ühiktüüp`, `sum type` → `summatüüp`, `product type` → `korrutistüüp`, `tuple` → `ennik`.

## 2026-07-06
- Political-family terms in SOC104: use `libertaarne`/`libertaarid` for libertarian, `tsentristlik`/`tsentristid` for centrist, `sotsialistlik`/`sotsialistid` for socialist, and `konservatiivne`/`konservatiivid` for conservative.
- In economic-policy contexts, render `moral hazard` as `moraalirisk`.
- For SOC104 totalitarianism vocabulary, use `totalitarism`, `totalitaarne režiim`, `klassikaline despotism`, `isiksusekultus`, and `majanduslik autarkia`.
- In SOC104 political-family quizzes, render `libertarianism` as `libertarism`, `libertarians` as `libertaarid`, and use `libertaarne` as the adjective.
- Render `non-aggression principle` as `mitteagressiivsuse põhimõte`; use `mitteagressioon` for the value in short lists.
- Render `minarchist/minarchism` as `minarhist/minarhism` and `anarcho-capitalist/anarcho-capitalism` as `anarhokapitalist/anarhokapitalism`.
- For Austrian/libertarian monetary prose, keep `Federal Reserve` and `Fiat` invariant; render `sound money` as `usaldusväärne raha` unless a glossary entry says otherwise.
- For Nolan-diagram political vocabulary, render `statism/statist` as `etatism`/`etatist`, while translating the explanatory phrase as state use of legislation to control or shape society.
- For libertarian political terms in SOC104, use the glossary-aligned `libertarism`, adjective `libertaarne`, and person `libertaarlane`; derive `paleolibertarism`/`paleolibertaarlane` and `neolibertarism` analogously.
- In US political context, keep proper program/party/institute names such as `New Deal`, `Great Society`, `Cato Institute`, `Mises Institute`, and `Libertarian Party` in English; translate only surrounding prose.
- Political-philosophy quizzes: render `statism` as `riigikesksus`; use `riiklik kontroll` for descriptive “state control” axis wording.
- Render `Nolan diamond` as `Nolani romb` and `Nolan diagram` as `Nolani diagramm`.
- Use `libertarism` for `libertarianism`, `libertaar` for `libertarian`, and the established forms `minarhist` / `anarhokapitalist`.
- For SOC104’s contrast between French `libertaires` and Anglophone `libertarians`, render `libertaires` as `libertäärid` and `libertarians` as `libertariaanid`; use `libertarism` for `libertarianism`.
- Keep `Green New Deal` as the untranslated proper name in Estonian prose.
- Render Bastiat/Friedman `spoliation` as `riisumine` in this political-economy context.
- Keep the genesis-block embedded newspaper headline byte-exact (`The Times 03/Jan/2009...`) and translate only the surrounding explanation, because it is the historical message committed in the block.
- Use glossary-canonical `Cypherpunks` for the community/name; in running Estonian prose, hyphenate or apostrophize case endings as needed (`Cypherpunks'id`, `Cypherpunki manifest`).
- Use glossary-canonical capitalized `Fiat` as the term, including compounds such as `Fiat-raha` and `Fiat-valuuta`.
- For SOC104 political philosophy, render `libertarian(s)` as `libertaarne` / `libertaarid`, matching existing Estonian Bitcoin-course usage.
- In Hayek/Popper context, use `spontaanne kord` for `spontaneous order`, `konstruktivism` for `constructivism`, and `avatud ühiskond` / `suletud ühiskond` for `open society` / `closed society`.
- For the pro-business vs. pro-market contrast, use `ettevõtlusmeelne` vs. `turumeelne`; keep the distinction between protecting incumbent firms and defending the market process.
- For Kant's `Sapere aude`, keep the Latin motto verbatim and render the explanatory phrase as `Julge ise mõelda`; translate Kantian `minority` as `alaealisus`.
