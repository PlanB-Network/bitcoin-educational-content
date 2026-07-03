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
