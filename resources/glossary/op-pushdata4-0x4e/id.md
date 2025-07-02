---
term: OP_PUSHDATA4 (0X4E)

---
Opcode yang memungkinkan mendorong data dalam jumlah yang sangat besar ke dalam _stack_. Diikuti oleh empat byte (_little-endian_) yang mengindikasikan panjang data yang akan didorong (hingga sekitar 4,3 GB). _Opcode_ ini digunakan untuk memasukkan data yang sangat besar ke dalam skrip, meskipun penggunaannya sangat jarang karena keterbatasan praktis pada ukuran transaksi.
