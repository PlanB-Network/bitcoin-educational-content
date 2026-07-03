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
