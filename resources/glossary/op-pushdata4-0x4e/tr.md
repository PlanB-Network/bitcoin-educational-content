---
term: OP_PUSHDATA4 (0X4E)
definition: Yığına çok büyük miktarda veri ekleyen opcode (nadir kullanılır).
---

Yığına çok büyük miktarda veri itilmesine izin verir. Bunu, itilecek verinin uzunluğunu (yaklaşık 4,3 GB'a kadar) gösteren dört bayt (little-endian) takip eder. Bu işlem kodu, komut dosyalarına çok büyük veriler eklemek için kullanılır, ancak işlem boyutundaki pratik sınırlamalar nedeniyle kullanımı son derece nadirdir.