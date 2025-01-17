---
term: OP_PUSHDATA4 (0X4E)

---
Memungkinkan mendorong data dalam jumlah yang sangat besar ke dalam stack. Diikuti oleh empat byte (little-endian) yang mengindikasikan panjang data yang akan didorong (hingga sekitar 4,3 GB). Opcode ini digunakan untuk memasukkan data yang sangat besar ke dalam skrip, meskipun penggunaannya sangat jarang karena keterbatasan praktis pada ukuran transaksi.