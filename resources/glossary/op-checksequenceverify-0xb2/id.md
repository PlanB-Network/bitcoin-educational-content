---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Membuat transaksi menjadi tidak valid jika salah satu dari karakteristik berikut ini diamati:
* Stack kosong;
* Nilai di puncak stack kurang dari `0`;
* Bendera nonaktif untuk nilai di puncak stack tidak didefinisikan dan; Versi transaksi kurang dari `2` atau; Bendera nonaktif untuk bidang `nSequence` dari input diatur atau; Tipe timelock tidak sama antara bidang `nSequence` dan nilai di puncak stack (waktu nyata atau jumlah blok) atau; Nilai di puncak stack lebih besar dari nilai bidang `nSequence` dari input.

Jika satu atau lebih dari karakteristik ini diamati, skrip yang mengandung `OP_CHECKSEQUENCEVERIFY` tidak dapat dipenuhi. Jika semua kondisi valid, maka `OP_CHECKSEQUENCEVERIFY` bertindak sebagai `OP_NOP`, yang berarti tidak melakukan tindakan apa pun pada skrip. Seolah-olah itu menghilang. `OP_CHECKSEQUENCEVERIFY` dengan demikian memberlakukan batasan waktu relatif pada pengeluaran UTXO yang diamankan dengan skrip yang mengandungnya. Ini dapat dilakukan baik dalam bentuk waktu nyata atau sebagai jumlah blok. Untuk melakukan ini, itu membatasi nilai yang mungkin untuk bidang `nSequence` dari input yang menghabiskannya, dan bidang `nSequence` ini sendiri membatasi kapan transaksi yang mencakup input ini dapat dimasukkan dalam blok.

> ► *Opcode ini adalah pengganti untuk `OP_NOP`. Itu ditempatkan pada `OP_NOP3`. Sering kali disebut dengan akronim "CSV". Catatan, `OP_CSV` tidak boleh dikacaukan dengan bidang `nSequence` dari sebuah transaksi. Yang pertama menggunakan yang terakhir, tetapi sifat dan tindakan mereka berbeda.*