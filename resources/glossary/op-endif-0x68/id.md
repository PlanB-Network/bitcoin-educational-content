---
term: OP_ENDIF (0X68)
---

Menandai akhir dari struktur kontrol kondisional yang diinisiasi oleh `OP_IF` atau `OP_NOTIF`, biasanya diikuti oleh satu atau lebih `OP_ELSE`. Ini menunjukkan bahwa eksekusi skrip harus dilanjutkan melewati struktur kondisional, terlepas dari cabang mana yang dieksekusi. Dengan kata lain, `OP_ENDIF` berfungsi untuk menandai akhir dari blok kondisional dalam skrip.