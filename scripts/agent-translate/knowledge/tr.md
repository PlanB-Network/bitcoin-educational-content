# Lessons — tr

## 2026-07-03
- scr403 quiz folder numbers are NOT aligned across languages — the same quiz can live under different `NNN/` in `en.yml` vs `tr.yml`. Before translating a scr403 quiz, `grep` its question text across `courses/scr403/quizz/**/tr.yml`; a canonical Turkish rendering often already exists and should be reused verbatim for consistency.
- Simplicity terminology settled in tr: "sum type" → "toplam tür", "tagged union" → "etiketli birleşim", "product type" → "çarpım türü", "combinator" → "kombinatör", "side effect" → "yan etki". Keep effect/type names (`Failure`, `Reader`, `State`, `jet`, `SimplicityHL`, `ASIC`, `sandbox`, `framework`, `IDE`) in English.
- Simplicity terimlerinde `Failure`, `Reader`, `Writer`, `witness`, `jet`, `CMR`, `Commitment Merkle Root`, `TapLeaf`, `TapTree`, `TapTweak` ve `NUMS` gibi protokol/uygulama adlarını koru; açıklayıcı Türkçe sözcükleri yalnızca çevresindeki düz yazıda kullan.
- `witness` için düz yazıda "tanık" kullan; `witness` kombinatör adını ve kod içi kullanımları değiştirme.
- `batch verification` için bağlantı metni ve başlıkta "toplu doğrulama"; `cross-input signature aggregation` için "girdiler arası imza toplama" kullanılabilir.
- Simplicity tür kuramı terimlerinde `combinator` → `kombinatör`, `sum type` → `toplam türü`, `product type` → `çarpım türü`, `unit type` → `birim türü`, `boolean type` → `Boole türü` kullan.
- Simplicity ifadeleri ve Boole literal'leri kod gibi korunmalı: `iden`, `unit`, `comp`, `pair`, `case`, `take`, `drop`, `injl`, `injr`, `false`, `true` çevrilmez.
- `covenant` için glossary Türkçede İngilizce terimi koruyor; Türkçe ekleri kesme işaretiyle kullan, örn. `özyinelemeli covenant'lar`.
- Gentzen/Curry-Howard bağlamında `sequent calculus` terimini İngilizce bırak; yalnızca çevresindeki düz yazıyı çevir.
- Simplicity combinators, type expressions, and identifiers should stay unsuffixed in Turkish; prefer forms like `... ifadesinin`, `... değeri`, or `... fonksiyonu` instead of attaching Turkish apostrophes directly to `case`, `CMR`, `Aⁿ`, `push-<n`, etc.
- In Simplicity arithmetic quizzes, render `half-adder` as `yarım-toplayıcı` and `full-adder` as `tam-toplayıcı`; keep Boolean operators `OR` and `XOR` unchanged.
- For effect-law terminology, use `değişmeli` for commutative, `idempotent` for idempotent, and `birimsel` for unitary.
