---
term: OP_WITHIN (0XA5)

---
Memeriksa apakah elemen teratas pada _stack_ berada dalam rentang yang ditentukan oleh elemen teratas kedua dan ketiga. Dengan kata lain, `OP_WITHIN` memeriksa apakah elemen teratas lebih besar atau sama dengan elemen kedua teratas dan kurang dari elemen ketiga teratas. Jika kondisi ini benar, maka `1` (_true_) akan didorong ke dalam _stack_, jika tidak, maka elemen `0` (_false_) akan didorong ke dalam _stack_.
