---
term: OP_ENDIF (0X68)

---
Menandai akhir dari struktur kontrol bersyarat yang dimulai oleh `OP_IF` atau `OP_NOTIF`, biasanya diikuti oleh satu atau beberapa `OP_ELSE`. Ini menunjukkan bahwa eksekusi skrip harus berlanjut di luar struktur bersyarat, terlepas dari cabang mana yang dieksekusi. Dengan kata lain, `OP_ENDIF` berfungsi untuk menggambarkan akhir dari blok bersyarat dalam skrip.