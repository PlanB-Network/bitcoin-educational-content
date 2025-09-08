---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Membuat transaksi tidak sah kecuali semua persyaratan ini terpenuhi:

- _Stack_ tidak kosong;
- Nilai di bagian atas _stack_ lebih besar atau sama dengan `0`;
- Jenis penguncian waktu adalah sama antara bidang `nLockTime` dan nilai di bagian atas _stack_ (waktu nyata atau nomor blok);
- Bidang `nSequence` pada input tidak sama dengan `xffffffff`;
- Nilai di bagian atas tumpukan lebih besar dari atau sama dengan nilai bidang `nLockTime` dari transaksi.

Jika salah satu dari kondisi ini tidak terpenuhi, skrip yang berisi `OP_CHECKLOCKTIMEVERIFY` tidak dapat dipenuhi. Jika semua kondisi ini valid, maka `OP_CHECKLOCKTIMEVERIFY` bertindak sebagai `OP_NOP`, yang berarti tidak melakukan tindakan apa pun pada skrip. Seolah-olah skrip tersebut menghilang. dengan demikian, `OP_CHECKLOCKTIMEVERIFY` memberikan batasan waktu pada pengeluaran UTXO yang diamankan dengan skrip yang berisi skrip tersebut. Ini dapat dilakukan dalam bentuk tanggal waktu Unix atau sebagai nomor blok. Untuk melakukan ini, ia membatasi nilai yang mungkin untuk bidang `nLockTime` dari transaksi yang membelanjakannya, dan bidang `nLockTime` ini sendiri membatasi kapan transaksi dapat dimasukkan ke dalam blok.

> ► *Opcode ini adalah pengganti `OP_NOP`. Ini ditempatkan pada `OP_NOP2`. Ini sering disebut dengan singkatan "CLTV". Catatan, `OP_CLTV` tidak dapat disamakan dengan bidang `nLockTime` dari sebuah transaksi. Meskipun `OP_CLTV` menggunakan nilai dari `nLockTime`, keduanya memiliki sifat dan cara kerja yang berbeda.
