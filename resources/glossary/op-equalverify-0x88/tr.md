---
term: OP_EQUALVERIFY (0X88)
definition: OP_EQUAL ve OP_VERIFY'ı birleştirir; değerler farklıysa işlemi geçersiz kılar.
---

OP_EQUAL` ve `OP_VERIFY` işlevlerini birleştirir. Önce yığıttaki en üst iki değerin eşitliğini kontrol eder, ardından sonucun sıfır olmamasını gerektirir, aksi takdirde işlem geçersiz olur. oP_EQUALVERIFY` özellikle Address doğrulama betiklerinde kullanılır.