---
term: OP_VER (0X62)

definition: Opcode nonaktif yang mendorong versi klien, diubah menjadi OP_SUCCESS.
---
_Opcode_ yang akan mendorong versi klien ke dalam _stack_. Opcode ini dinonaktifkan karena jika digunakan, setiap pembaruan akan menyebabkan _hard fork_. BIP342 memodifikasi _opcode_ ini menjadi `OP_SUCCESS`.
