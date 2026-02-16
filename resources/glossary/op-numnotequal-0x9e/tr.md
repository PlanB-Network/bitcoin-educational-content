---
term: OP_NUMNOTEQUAL (0X9E)
definition: Yığının en üstündeki iki öğenin sayısal olarak farklı olup olmadığını kontrol eden opcode.
---

Sayısal olarak eşit olup olmadıklarını kontrol etmek için yığındaki en üstteki iki Elements değerini karşılaştırır. Eğer değerler eşit değilse, yığına `1` (doğru), aksi takdirde `0` (yanlış) değerini iter. Bu `OP_NUMEQUAL` komutunun tersidir.