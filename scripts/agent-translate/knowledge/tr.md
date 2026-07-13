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

## 2026-07-06
- soc104 siyaset felsefesi bağlamında `libertarian/libertarianism` için tutarlı olarak `liberteryen/liberteryenizm` kullan; `özgürlükçü` genel sıfatı Cypherpunk gibi geniş bağlamlarda kalabilir.
- Fransız `libertaire` terimini Türkçeye çevirmeden bırak; sosyalist anarşist geleneği `liberteryen`den ayırmak için başlıklarda ve açıklamalarda aynen korunmalı.
- `statism` için `devletçilik`, `constructivism` için `inşacılık`, `spontaneous order` için `kendiliğinden düzen`, `fiat currency/money` için `itibari para` kullan.
- soc104 siyaset terminolojisinde `libertarian` → `liberteryen`, `libertarianism` → `liberteryenizm`, `paleo-libertarianism` → `paleo-liberteryenizm`, `neo-libertarianism` → `neo-liberteryenizm` kullan; `Liberal`, `Cato Institute`, `Mises Institute`, `Libertarian Party`, `New Deal`, `Great Society` özel/yerleşik adlarını koru.
- soc104 bağlamında `statism` → `devletçilik`, `statist` → `devletçi`; `legislate on X` için “X konusunda yasa yapmak” kullan, “yasalaştırmak” yalnızca “make legal/legalize” anlamına kaymasın.
- For soc104 political-family quizzes, use: `libertarian` → `liberteryen`, `conservative` → `muhafazakâr`, `socialist` → `sosyalist`, `centrist` → `merkezci`; keep the register academic and neutral.
- Render `moral hazard` as `ahlaki tehlike` in Turkish economics/policy contexts.
- For totalitarianism terminology in soc104, use `totalitarizm`, `totaliter rejim`, `güdümlü ekonomi`, and `seküler dinler`.
- soc104 political terminology: `constructivism` → `inşacılık`, `anti-constructivism` → `inşacılık karşıtlığı`; keep existing `libertarian` rendering as `liberteryen`.
- For soc104 monetary contrast, render `market money/currency` as `piyasa parası` and `state money` as `devlet parası`; use `fiat para` for fiat money/currency.
- In cypherpunk context, render the motto `Cypherpunks write code` as `Cypherpunklar kod yazar`, while keeping proper names like `Bitcoin White Paper` in English.
- In SOC104 political-philosophy quizzes, keep French `libertaire` distinct from English `libertarian`: render `libertaires` as `libertaire'ler` / `Fransız libertaire'leri`, and `libertarians` / `libertarianism` as `liberteryenler` / `liberteryenizm`.
- Render Rothbard's `non-aggression principle` as `saldırmazlık ilkesi`; translate `spoliation` in the Bastiat/Friedman political-economy sense as `yağma`.
- Keep contemporary policy names like `Green New Deal` in English when used as named concepts, while translating the surrounding explanation.
- SOC104 Turkish terminology follows the course translation: `constructivism` → `inşacılık`, `constructivists` → `inşacılar`, `spontaneous order` → `kendiliğinden düzen`, and `central planning` → `merkezi planlama`.
- SOC104 Turkish terminology follows existing course `tr.md`: `Nolan Diagram` → `Nolan diyagramı`, `Nolan diamond` → `Nolan elması`, `statism/statist` → `devletçilik/devletçi`, `libertarianism/libertarian` → `liberteryenizm/liberteryen`.
- Political-axis wording in SOC104: `left-right axis` → `sol-sağ ekseni`, `top-bottom/vertical axis` → `üst-alt/dikey eksen`, `economic freedoms` → `ekonomik özgürlükler`, `personal freedoms` → `kişisel özgürlükler`.
- SOC104 keeps `fiat money/currency` as `itibari para`; `minarchists` as `minarşistler`; `anarcho-capitalists` as `anarko-kapitalistler`.
- SOC104 siyaset terimlerinde `neoconservative` için `neomuhafazakâr`, `paleoconservative` için `paleomuhafazakâr` kullan; Türkçe çoğul/ekleri bu gövdelere getir.
- SOC104 bağlamında `libertarianism` → `liberteryenizm`, `libertarians` → `liberteryenler`, `minarchists` → `minarşistler`, `anarcho-capitalists` → `anarko-kapitalistler`.
- `self-ownership` için düz yazıda mevcut Türkçe kullanımla uyumlu olarak `kişinin kendine sahip olması` tercih et.
