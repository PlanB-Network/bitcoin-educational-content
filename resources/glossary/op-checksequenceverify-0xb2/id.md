---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Transaksi menjadi tidak valid jika salah satu dari karakteristik ini diamati:


- Tumpukannya kosong;
- Nilai di bagian atas tumpukan kurang dari `0`;
- Bendera disable untuk nilai di bagian atas tumpukan tidak terdefinisi dan; Versi transaksi kurang dari `2` atau; Bendera disable untuk bidang `nSequence` dari input disetel atau; Jenis penguncian waktu tidak sama antara bidang `nSequence` dengan nilai di bagian atas tumpukan (waktu nyata atau jumlah blok) atau; Nilai di bagian atas tumpukan lebih besar daripada nilai bidang `nSequence` dari input.

Jika salah satu atau beberapa dari karakteristik ini diamati, skrip yang berisi `OP_CHECKSEQUENCEVERIFY` tidak dapat dipenuhi. Jika semua kondisi valid, maka `OP_CHECKSEQUENCEVERIFY` bertindak sebagai `OP_NOP`, yang berarti tidak melakukan tindakan apa pun pada skrip. Seolah-olah script tersebut menghilang. dengan demikian, `OP_CHECKSEQUENCEVERIFY` memberikan batasan waktu relatif terhadap pengeluaran UTXO yang diamankan dengan skrip yang berisi skrip tersebut. Ini dapat dilakukan dalam bentuk waktu nyata atau dalam bentuk sejumlah blok. Untuk melakukan ini, ia membatasi nilai yang mungkin untuk bidang `nSequence` dari input yang membelanjakannya, dan bidang `nSequence` ini sendiri membatasi kapan transaksi yang menyertakan input ini dapat disertakan dalam sebuah blok.

> ► *Opcode ini adalah pengganti `OP_NOP`. Ini ditempatkan pada `OP_NOP3`. Ini sering disebut dengan singkatan "CSV". Catatan, `OP_CSV` tidak boleh disamakan dengan bidang `nSequence` dari sebuah transaksi. Yang pertama menggunakan yang kedua, tetapi sifat dan tindakan mereka berbeda.*