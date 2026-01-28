---
term: OP_TOALTSTACK (0X6B)

definition: Opcode yang memindahkan bagian atas tumpukan utama ke tumpukan alternatif.
---
Mengambil bagian atas dari _stack_ utama dan memindahkannya ke _stack_ alternatif. _Opcode_ ini digunakan untuk menyimpan data sementara untuk digunakan nanti dalam skrip. Item yang dipindahkan akan dihapus dari _stack_ utama. `OP_FROMALTSTACK` kemudian akan digunakan untuk meletakkannya kembali di atas _stack_ utama.
