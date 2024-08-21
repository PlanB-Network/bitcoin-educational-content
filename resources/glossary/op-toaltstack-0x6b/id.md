---
term: OP_TOALTSTACK (0X6B)
---

Mengambil bagian atas dari tumpukan utama (*main stack*) dan memindahkannya ke tumpukan alternatif (*alt stack*). Opcode ini digunakan untuk menyimpan data sementara untuk digunakan nanti dalam skrip. Item yang dipindahkan dengan demikian dihapus dari tumpukan utama. `OP_FROMALTSTACK` kemudian akan digunakan untuk meletakkannya kembali di atas tumpukan utama.