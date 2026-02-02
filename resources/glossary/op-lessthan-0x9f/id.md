---
term: OP_LESSTHAN (0X9F)

definition: Opcode yang memeriksa apakah elemen pertama pada tumpukan lebih kecil dari yang kedua.
---
Membandingkan dua item paling atas pada _stack_ dan memeriksa apakah item teratas kurang dari item kedua teratas. Jika item teratas kurang dari item kedua teratas, maka _opcode_ akan mendorong `1` (_true_) ke dalam _stack_, jika tidak, _opcode_ akan mendorong `0` (false) ke _stack_.
