---
term: OP_WITHIN (0XA5)
definition: Bir değerin diğer iki değer tarafından tanımlanan bir aralıkta olup olmadığını kontrol eden opcode.
---

Yığındaki en üst elemanın ikinci ve üçüncü üst Elements tarafından tanımlanan aralıkta olup olmadığını kontrol eder. Başka bir deyişle, `OP_WITHIN` en üstteki elemanın ikinciden büyük veya eşit ve üçüncüden küçük olup olmadığını kontrol eder. Bu koşul doğruysa, yığına `1` (doğru) basar, aksi takdirde `0` (yanlış) basar.