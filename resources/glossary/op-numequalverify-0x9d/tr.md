---
term: OP_NUMEQUALVERIFY (0X9D)
definition: OP_NUMEQUAL ve OP_VERIFY'ı birleştirir; sayısal değerler farklıysa başarısız olur.
---

OP_NUMEQUAL` ve `OP_VERIFY` işlemlerini birleştirir. Yığındaki en üstteki iki Elements değerini sayısal olarak karşılaştırır. Değerler eşitse, `OP_NUMEQUALVERIFY` doğru sonucu yığından kaldırır ve kodun yürütülmesine devam eder. Değerler eşit değilse, sonuç yanlış olur ve kod hemen başarısız olur.