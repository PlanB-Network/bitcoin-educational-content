# Lessons — th

## 2026-07-03
- Composition terms come from the canonical course article `courses/scr403/th.md`: sequential = `การประกอบแบบตามลำดับ`, parallel = `การประกอบแบบขนาน`, conditional = `การประกอบแบบมีเงื่อนไข`. "the dual of" stays `เป็น dual ของ` (keep `dual` English).
- `branch` → keep English `branch` (matches `th.md` lines 114/152 and quiz 015). Note: quiz 030 used `สาขา` — the article convention (English `branch`) wins for consistency in this course.
- Keep verbatim (established EN tech terms) for scr403: `Simplicity`, `combinator`, effect names (`Failure`/`Reader`/`Writer`/…`effect`), `exception`, `sum`/`product`/`tagged union`, `recursive covenants`, `unbounded recursion`, `delegation`, `standardness`, `fixed-point`, `loop`/`unroll`, `metered`, `static analysis`, `iteration`, `body`, `encode`, `duplicate`, `abuse`, `jets`, `pure`.
- Prefer localized forms where the article does: run/invoke/execute → `เรียกใช้`; input/output type → `ชนิดอินพุต`/`ชนิดเอาต์พุต`; standalone transaction → `ธุรกรรม` (but compound `transaction environment`/`transaction log` stay English); finite computations → `การคำนวณจำกัด`; completeness → `ความสมบูรณ์`; block-space → `พื้นที่บล็อก`.
- scr403 quizz dirs were renumbered: EN `020` is byte-equivalent to the already-translated TH `022`, and EN `021` to TH `023`. Reuse the existing reviewed TH verbatim for these to stay consistent.
- For Thai Simplicity material, keep protocol/combinator identifiers and algebraic property names in English (`Simplicity`, `Bit Machine`, `CMR`, `NUMS`, `Taproot`, `Schnorr`, `commutative`, `idempotent`, `unitary`) unless the source already marks prose around them for translation.
- Translate Merkle concepts in prose as `ราก Merkle` / `Merkle tree` when mixed with CMR commitments, while preserving `Merkle root` if it is acting as a technical label in an English-heavy phrase.
- For SCR403 Thai, keep core Simplicity terms in English when the course already does: `combinator`, `sum type`, `product type`, `unit type`, `jets`, `static analysis`, `dynamic`, `execution`, `proof assistant`, `formal specification`, `native implementation`.
- Translate composition labels consistently as `การประกอบแบบตามลำดับ`, `การประกอบแบบขนาน`, and `การประกอบแบบมีเงื่อนไข`.
- Render `left-tagged` / `right-tagged` as `ติด tag ซ้าย` / `ติด tag ขวา`; keep boolean literals `false` and `true` in English.
- For SCR403 Thai, follow the existing course precedent: keep technical loanwords like `combinator`, `side effects`, `branch`, `witness`, `transaction environment`, `Failure effect`, `Reader effect`, `CMR`, and `TapLeaf` in English, adding Thai grammar around them.
- Translate "power-of-two block" as `block ที่มีขนาดเป็นกำลังของสอง`; avoid `กำลังสอง`, which means square rather than power of two.
- สำหรับเนื้อหา Simplicity ภาษาไทย ให้คงศัพท์เทคนิคที่เป็นชื่อเฉพาะหรือใช้ในโค้ดเป็นอังกฤษ เช่น `Simplicity`, `combinator`, `jet`, `witness`, `CMR`, `side effect`, `Failure effect`, `Reader effect` แล้วแปลคำอธิบายรอบข้างเป็นไทยเพื่อไม่ให้ชนกับ identifier และสัญกรณ์ในสูตร
- แปล `sum type`, `product type`, `unit type` เป็นบริบทผสมไทย-อังกฤษ เช่น `sum type`, `product type`, `unit type` แทนการบัญญัติไทยล้วน เพื่อรักษาความสอดคล้องกับสัญกรณ์ `A + B`, `A × B`, `𝟙` และหลีกเลี่ยงความกำกวมกับคำทั่วไป
