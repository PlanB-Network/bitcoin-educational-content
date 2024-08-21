---
term: OP_ROLL (0X7A)
---

Memindahkan sebuah item dari tumpukan ke puncak tumpukan, berdasarkan kedalaman yang ditentukan oleh nilai di puncak tumpukan sebelum operasi. Sebagai contoh, jika nilai di puncak tumpukan adalah `4`, `OP_ROLL` akan memilih item keempat dari puncak tumpukan, dan akan memindahkan nilai ini ke puncak. `OP_ROLL` memiliki fungsi yang sama dengan `OP_PICK`, kecuali bahwa ia menghapus item dari posisi aslinya.