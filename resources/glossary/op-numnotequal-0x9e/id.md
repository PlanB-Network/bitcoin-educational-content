---
term: OP_NUMNOTEQUAL (0X9E)

---
Membandingkan dua elemen paling atas pada tumpukan untuk memeriksa apakah keduanya secara numerik tidak sama. Jika nilainya tidak sama, maka akan `1` (benar) akan didorong ke dalam _stack_, jika tidak, maka _opcode_ akan mendorong `0` (salah) ke atas _stack_. _Opcode_ ini adalah kebalikan dari `OP_NUMEQUAL`.
