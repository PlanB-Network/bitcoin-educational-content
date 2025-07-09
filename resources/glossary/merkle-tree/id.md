---
term: POHON MERKLE

---
Pohon Merkle adalah sebuah akumulator kriptografi yang merupakan sebuah metode untuk membuktikan keanggotaan dari sebuah informasi dalam sebuah himpunan yang lebih besar. Ini adalah struktur data yang memfasilitasi verifikasi informasi dalam format yang ringkas. Dalam sistem Bitcoin, Pohon Merkle digunakan untuk mengelompokkan dan memadatkan transaksi-transaksi dalam sebuah blok ke dalam sebuah _hash_ tunggal, yang disebut dengan Akar Merkle (atau "*Root Hash*"). Setiap transaksi di-_hash_, kemudian _hash_ yang berdekatan di-_hash_ bersama secara hierarkis sampai Akar Merkle diperoleh.

![](../../dictionnaire/assets/1.webp)

Struktur ini memungkinkan verifikasi cepat apakah sebuah transaksi tertentu termasuk dalam blok tertentu tanpa harus menganalisa semua transaksi. Sebagai contoh, jika saya hanya memiliki Akar Merkle dan saya ingin memverifikasi bahwa `TX 7` memang merupakan bagian dari pohon tersebut, saya hanya membutuhkan bukti-bukti berikut ini:


- `TX 7`;
- `HASH 8`;
- `HASH 5-6`;
- `HASH 1-2-3-4`.

Dengan potongan-potongan informasi ini, saya dapat menghitung node perantara hingga Akar Merkle.

![](../../dictionnaire/assets/2.webp)

Pohon Merkle terutama digunakan untuk node ringan (dikenal sebagai "SPV") yang hanya menyimpan _header_ blok, tetapi tidak menyimpan transaksinya. Struktur ini juga ditemukan dalam protokol UTREEXO, sebuah protokol yang memungkinkan untuk memadatkan kumpulan node UTXO dan dalam MAST Taproot.
