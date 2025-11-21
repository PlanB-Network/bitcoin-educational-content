---
term: OP_ROLL (0X7A)

---
Memindahkan item dari _stack_ ke bagian atas _stack_, berdasarkan kedalaman yang ditentukan oleh nilai di bagian atas tumpukan sebelum operasi. Sebagai contoh, jika nilai di bagian atas tumpukan adalah `4`, `OP_ROLL` akan memilih item keempat dari bagian atas tumpukan, dan akan memindahkan nilai ini ke bagian atas. `OP_ROLL` memiliki fungsi yang sama dengan `OP_PICK`, kecuali bahwa ia akan menghilangkan elemen dari posisi semula.
