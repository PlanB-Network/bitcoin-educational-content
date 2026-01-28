---
term: OP_HASH160 (0XA9)

definition: Opcode yang melakukan hash pada elemen teratas dengan SHA256 kemudian RIPEMD160.
---
Mengambil elemen teratas dari _stack_ dan menggantinya dengan _hash_-nya, menggunakan fungsi `SHA256` dan `RIPEMD160` secara berurutan. Proses dua langkah ini menghasilkan _hash_ 160-bit.
