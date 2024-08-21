---
term: OP_PUSHDATA4 (0X4E)
---

Memungkinkan mendorong sejumlah besar data ke dalam tumpukan. Diikuti oleh empat byte (little-endian) yang menunjukkan panjang data yang akan didorong (hingga sekitar 4,3 GB). Opcode ini digunakan untuk memasukkan data yang sangat besar ke dalam skrip, meskipun penggunaannya sangat jarang karena keterbatasan praktis pada ukuran transaksi.