---
term: OP_PUSHDATA2 (0X4D)

definition: Opcode yang mendorong hingga 65 KB data ke tumpukan.
---
Memungkinkan mendorong sejumlah besar data ke dalam _stack_. Diikuti oleh dua byte (_little-endian_) yang menentukan panjang data yang akan didorong (hingga sekitar 65 KB). _Opcode_ ini digunakan untuk memasukkan data yang lebih besar ke dalam skrip.
