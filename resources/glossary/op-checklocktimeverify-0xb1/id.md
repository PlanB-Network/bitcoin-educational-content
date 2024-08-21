---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Membuat transaksi menjadi tidak valid kecuali semua kondisi ini terpenuhi:
* Tumpukan tidak kosong;
* Nilai di puncak tumpukan lebih besar atau sama dengan `0`;
* Jenis timelock sama antara bidang `nLockTime` dan nilai di puncak tumpukan (waktu nyata atau nomor blok);
* Bidang `nSequence` dari input tidak sama dengan `0xffffffff`;
* Nilai di puncak tumpukan lebih besar atau sama dengan nilai dari bidang `nLockTime` dari transaksi.

Jika salah satu dari kondisi ini tidak terpenuhi, skrip yang mengandung `OP_CHECKLOCKTIMEVERIFY` tidak dapat dipenuhi. Jika semua kondisi ini valid, maka `OP_CHECKLOCKTIMEVERIFY` bertindak sebagai `OP_NOP`, yang berarti tidak melakukan tindakan apa pun pada skrip. Seolah-olah itu menghilang. `OP_CHECKLOCKTIMEVERIFY` dengan demikian memberlakukan batasan waktu pada pengeluaran UTXO yang diamankan dengan skrip yang mengandungnya. Ini dapat dilakukan baik dalam bentuk tanggal waktu Unix atau sebagai nomor blok. Untuk melakukan ini, itu membatasi nilai yang mungkin untuk bidang `nLockTime` dari transaksi yang menghabiskannya, dan bidang `nLockTime` itu sendiri membatasi kapan transaksi dapat dimasukkan dalam blok.

> ► *Opcode ini adalah pengganti untuk `OP_NOP`. Itu ditempatkan pada `OP_NOP2`. Sering kali disebut dengan akronimnya "CLTV". Catatan, `OP_CLTV` tidak boleh dikacaukan dengan bidang `nLockTime` dari sebuah transaksi. Yang pertama menggunakan yang terakhir, tetapi sifat dan tindakan mereka berbeda.*