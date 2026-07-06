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

## 2026-07-06
- For SOC104 Thai, use course-established political terms: `statism` → `รัฐนิยม`, `spontaneous order` → `ระเบียบที่เกิดขึ้นเอง`, `limited government` → `รัฐบาลจำกัด`.
- Keep school/movement labels in English when the Thai course does: `liberalism`, `libertarianism`, `paleo-libertarianism`, `neo-libertarianism`, `American liberals`, `Big Government`, `interventionism`, `protectionism`, `think tank`.
- Render U.S. federal-state contrast as `รัฐบาลกลาง` vs `รัฐย่อย`, matching the SOC104 Thai article.
- For SOC104 Thai, follow `courses/soc104/th.md` terminology: `totalitarianism` → `เบ็ดเสร็จนิยม` / `ระบอบเบ็ดเสร็จ`, `libertarian` → `ลิเบอร์ทาเรียน`, `conservative` → `อนุรักษนิยม`, `centrist` → `สายกลาง`, and keep `moral hazard`, `bailouts`, `economic autarky`, `ideology` as English loan/technical terms when the course does.
- For SOC104 Thai, keep course loanwords already established in `courses/soc104/th.md`: `cypherpunk`, `fiat`, `constructivism`, `interventionism`, `manifesto`, `mailing list`, `white paper`, `code`, `protocol`, and `commodity`, with Thai grammar around them.
- Preserve the historical Genesis Block headline exactly in English: `The Times 03/Jan/2009 Chancellor on the brink of a second bank bailout.` Translate only the surrounding explanation.
- Render libertarian terminology consistently as `ลิเบอร์ทาเรียน`; use `ความยินยอม` for consent, `การบังคับ` for coercion, `รัฐสวัสดิการ` for welfare state, and `เงินตลาด` / `เงินรัฐ` for market money / state money.
- For SOC104 Thai, keep `libertaires` and `libertarianism` in English when matching the course article; render political actors as `กลุ่ม libertaires` and `ลิเบอร์ทาเรียน`, and keep `self-ownership` English.
- Use the course's political-analysis terms consistently: `คำนิยามเชิงโครงสร้าง` / `คำนิยามเชิงเจตนา`, `วิสัยทัศน์แบบองค์รวม` or `หลักองค์รวม` for holism, and `การปล้น` for spoliation.
- For SOC104 Thai, follow `courses/soc104/th.md`: keep `Nolan diagram` and `Nolan diamond` in English rather than translating them as Thai labels.
- Keep ideology/group labels already used as English loans or mixed forms in the SOC104 article: `ลิเบอร์ทาเรียน`, `รัฐนิยม`, `anarcho-capitalists`, `minarchists`, `Greens`, and `เงิน fiat`.
- For SOC104 Thai, render `libertarian(s)` as `ลิเบอร์ทาเรียน` rather than broader Thai liberal terms, to avoid confusion with liberalism/libertaire distinctions.
- Render Hayek’s `spontaneous order` as `ระเบียบเกิดเอง` in quiz prose; use `การวางแผนจากศูนย์กลาง` for `central planning`.
- Keep `constructivism` as the English loanword in question text and capitalize `Constructivism` at sentence start in explanations, while translating the surrounding definition into Thai.
- Render `individualism` / `collectivism` as `ปัจเจกนิยม` / `รวมหมู่นิยม`; use `สังคมเปิด` / `สังคมปิด` for Popper’s open/closed society distinction.
- For SOC104 Thai political-family quizzes, follow `courses/soc104/th.md`: conservatism = `อนุรักษนิยม`, libertarian/libertarianism = `ลิเบอร์ทาเรียน`/`libertarianism` depending on source-style context, centrism/centrists = `สายกลาง`, statism = `รัฐนิยม`.
- Keep course-established English political-economy terms when used as labels: `interventionism`, `isolationist`, `minarchist(s)`, `anarcho-capitalist(s)`, `laissez-faire`, `pro-business`, `pro-market`, `corporatism`, `crony capitalism`, `dogmatism`/`dogma`, `sound money`, `fiat`, `self-ownership`, `non-aggression`.
- Render `societal sphere` as `ขอบเขตสังคม` and `economic sphere` as `ขอบเขตเศรษฐกิจ`, matching the SOC104 article's Nolan Diagram terminology.
