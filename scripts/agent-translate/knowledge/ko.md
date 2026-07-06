# Lessons — ko

## 2026-07-03
- Simplicity course terms: keep protocol/language names and named effects in English when they behave like identifiers (`Simplicity`, `Failure 효과`, `Reader 효과`, `Writer 효과`, `jets`), while translating generic type-theory terms as `유닛 타입`, `합 타입`, `곱 타입`, `컴비네이터`, `합성`.
- For Simplicity-specific witness material, use `위트니스` for the general Bitcoin concept but keep the inline identifier `witness` unchanged when referring to the combinator/expression name.
- For SCR403 Korean, keep Simplicity expression identifiers and effect/type names such as `half-adder`, `full-adder`, `Reader`, `Writer`, `Failure`, `unitary`, `CMR`, `jet`, `case`, `scribe`, `iden`, and `comp` in English/code form; translate only the surrounding explanation.
- Use `캐리` and `합` for adder carry/sum prose, matching earlier SCR403 Korean quizzes, while leaving `carry-in`/`carry-out` style compound terms in English when they name the technical signal.
- Render canonical glossary terms as `Taproot`, `슈노르`, `머클 루트`, and `머클 트리`; keep protocol constructions like `NUMS point`, `key-spend`, `key-path`, and `script path` in English for precision.
- `side effect` → 부수 효과; named effects (Failure/Reader/State/Writer/IO/Memory/Continuation/Nondeterminism) stay English + 효과 (e.g. `Failure 효과`).
- `combinator` → 컴비네이터; code identifiers (`take`/`drop`, `jet`) and protocol/product names (Simplicity, SimplicityHL, Bitcoin, Liquid, ASIC, IDE) kept verbatim in English.
- Glossary confirms `transaction` → 트랜잭션, `blockchain` → 블록체인, `signature` → 서명.
- Preserve YAML quoting per-source: 020/en.yml double-quotes every value (values contain parentheses), 019/en.yml leaves them bare — mirror this rather than normalizing.
- For Simplicity course material, keep effect names in English and attach Korean nouns: `Failure 효과`, `Reader 효과`, `Writer 효과`; use `부수 효과` for "side effect".
- Use `컴비네이터` for "combinator", `시퀀트 계산` for "sequent calculus", and keep core combinator/code identifiers (`case`, `take`, `drop`, `iden`, jets) verbatim.
- Use `위트니스`/`witness` consistently for witness concepts depending on existing nearby Korean course style; do not translate witness identifiers or CMR.
- Render "commutative" as `교환 가능`, "idempotent" as `멱등`, and "unit type" as `유닛 타입` in this course.
- For SCR403 Simplicity terms, follow the existing Korean course rendering: combinator → `컴비네이터`, sum type → `합 타입`, product type → `곱 타입`, unit type → `유닛 타입`, boolean → `불리언`.
- Keep Simplicity-specific identifiers and conventional technical terms in English when they are code/protocol terms: `iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `jet`, `DAG`, `Merkle root`, `gas`.
- Quote YAML values that contain an internal colon-space, and quote full values that begin with an inline quoted term like `"'take' ..."` to avoid malformed YAML.

## 2026-07-06
- For SOC104 Korean, render `spontaneous order` as `자생적 질서` and `constructivism` as `구성주의`, matching the existing course body.
- For SOC104 Korean political-family terms, use `리버테리언` for actors/adjectives, `중도주의자`, `보수주의자`, `사회주의자`, and keep proper names like `Hayek`, `Mises`, `Popper`, `Kant`, and `Molinari` in Latin script.
- Render `pro-business`/`pro-market` as `친기업`/`친시장`, and `free market` as `자유시장` in this course context.
- For SOC104 political terminology, keep `liberal`/`libertarian` in English when the quiz contrasts US/European label meanings, while translating the surrounding ideology as `자유주의`/`자유지상주의`.
- Render `paleo-libertarianism` as `팔레오-자유지상주의` and `neo-libertarianism` as `네오-자유지상주의`; keep institution and party names such as `Cato Institute`, `Mises Institute`, and `Libertarian Party` in English.
- For SOC104 political-spectrum quizzes, render `Nolan diagram` as `놀런 도표` and `Nolan diamond` as `놀런 다이아몬드`; keep the distinction because the source uses both forms.
- Render `libertarianism` as `자유지상주의`, `statism` as `국가주의`, `minarchists` as `최소국가주의자`, and `anarcho-capitalists` as `아나코-자본주의자`.
- In political-history context, render `left/right` and `left-wing/right-wing` as `좌우` and `좌파/우파`; render `The Greens` as `녹색당` when referring to the political party family.
- For political-family terminology in SOC104 Korean, render `libertarianism` as `리버테리언주의`, `libertarians` as `리버테리언`, and keep French `libertaire(s)`/`libertines` in Latin form when the lesson explicitly contrasts the untranslated terms.
- In this course, render `statism` as `국가주의`, `fiat currency` as `법정화폐`, and `welfare state` as `복지국가`.
- Render the pro-market distinction as `친기업` for `pro-business` and `친시장` for `pro-market`; render `neoconservatism`/`paleoconservative` as `신보수주의`/`고보수주의` when not used as a quoted self-label.
- For SOC104 political-family quizzes, use `리버테리언`/`리버테리언들` for libertarian actors and `리버테리언주의` only when naming the ideology abstractly; keep `사회주의자`, `보수주의자`, `중도주의자` for the other families.
- Render `moral hazard` as `도덕적 해이`; render `firearms`/`carrying weapons` in policy context as `총기`/`무기 소지` rather than literal weaponry terms.
- In totalitarianism context, render `directed economy` as `통제 경제` to distinguish it from Stalinist `planned economy` (`계획 경제`/`경제를 완전히 계획`).
- For SOC104, keep the French political identifier `libertaires` verbatim, while rendering Anglo-American `libertarian(s)` as `리버테리언` and the doctrine as `리버테리언주의`.
- Match existing SOC104 Korean terminology: `intentional definition` → `의도적 정의`, `structural definition/approach` → `구조적 정의/구조적 접근`, `non-aggression principle` → `비공격 원칙`, and `spoliation` → `수탈`.
- For SOC104 political-family terms, keep established Korean renderings from existing quizzes: `자유지상주의`, `보수주의`, `중도주의`, `사회주의`, `최소국가주의자`, `아나코-자본주의자`.
- Render `non-aggression principle` as `비침해 원칙` in libertarian political-theory contexts; use `자기소유` for `self-ownership`.
- Render `paleoconservative` as `고보수주의자` and `neoconservative` as `신보수주의자` in SOC104 foreign-policy quizzes.
- For monetary terms in SOC104, use glossary-backed `법정화폐` for `fiat money`, and render `sound money` as `건전한 화폐`.
- For SOC104 Korean, use `법정화폐` for fiat money/currency, matching the glossary `법정화폐 (Fiat)`.
- Render the cypherpunk movement as `사이퍼펑크`, but keep proper names/titles such as `Cypherpunk 메일링 리스트`, `Cypherpunk Manifesto`, and the quoted slogan `Cypherpunks write code` in English.
- Render `White Paper` as `백서` in running Korean prose when referring to the Bitcoin white paper.
- Use `구성주의` for constructivism and `자생적 질서` for spontaneous order in SOC104 political-philosophy material.
