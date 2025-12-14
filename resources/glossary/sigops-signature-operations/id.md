---
term: SIGOPS (SIGNATURE OPERATIONS)

---
Mengacu pada operasi tanda tangan digital yang diperlukan untuk validasi transaksi. Setiap transaksi Bitcoin dapat berisi beberapa input, yang masing-masing mungkin memerlukan satu atau lebih tanda tangan untuk dianggap valid. Verifikasi tanda tangan ini dilakukan melalui penggunaan opcode tertentu yang disebut "_sigops_". Secara khusus, hal ini mencakup `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG`, dan `OP_CHECKMULTISIGVERIFY`. Operasi-operasi ini membebankan beban kerja tertentu pada node jaringan yang harus memverifikasinya. Untuk mencegah serangan DoS melalui penggelembungan jumlah _sigops_ secara artifisial, protokol ini memberikan batasan pada jumlah _sigops_ yang diizinkan per blok, untuk memastikan bahwa beban validasi tetap dapat dikelola oleh node. Batas ini saat ini ditetapkan pada maksimum 80.000 _sigops_ per blok. Untuk menghitungnya, node mengikuti aturan ini:

`scriptPubKey`, `OP_CHECKSIG` dan `OP_CHECKSIGVERIFY` dihitung sebagai 4 _sigops_. Opcode `OP_CHECKMULTISIG` dan `OP_CHECKMULTISIGVERIFY` dihitung sebagai 80 _sigops_. Selama penghitungan, operasi-operasi ini dikalikan dengan 4 ketika mereka bukan bagian dari input SegWit (untuk P2WPKH, jumlah _sigops_ adalah 1);

Dalam `redeemScript`, opcode `OP_CHECKSIG` dan `OP_CHECKSIGVERIFY` juga dihitung sebagai 4 _sigops_, `OP_CHECKMULTISIG` dan `OP_CHECKMULTISIGVERIFY` diperhitungkan sebagai `4n` jika mendahului `OP_n`, atau 80 _sigops_ jika tidak;

Untuk `witnessScript`, `OP_CHECKSIG` dan `OP_CHECKSIGVERIFY` bernilai 1 sigop, `OP_CHECKMULTISIG` dan `OP_CHECKMULTISIGVERIFY` dihitung sebagai `n` jika diperkenalkan oleh `OP_n`, atau 20 _sigops_ jika tidak;

Dalam skrip Taproot, _sigops_ diperlakukan secara berbeda dibandingkan dengan skrip tradisional. Alih-alih menghitung secara langsung setiap operasi tanda tangan, Taproot memperkenalkan anggaran _sigops_ untuk setiap input transaksi, yang sebanding dengan ukuran input tersebut. Anggaran ini adalah 50 sigops ditambah dengan ukuran byte dari saksi input. Setiap operasi tanda tangan mengurangi anggaran ini sebesar 50. Jika eksekusi operasi tanda tangan menurunkan anggaran di bawah nol, skrip tidak valid. Metode ini memungkinkan fleksibilitas yang lebih besar pada skrip Taproot, dengan tetap menjaga perlindungan terhadap potensi penyalahgunaan yang berhubungan dengan _sigops_, dengan menghubungkannya secara langsung dengan bobot input. Dengan demikian, skrip Taproot tidak termasuk dalam batas 80.000 _sigops_ per blok.
