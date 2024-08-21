---
term: MERKLE TREE
---

Merkle Tree adalah sebuah akumulator kriptografi. Ini adalah metode untuk membuktikan keanggotaan sebuah informasi tertentu dalam satu set yang lebih besar. Ini adalah struktur data yang memfasilitasi verifikasi informasi dalam format yang ringkas. Dalam sistem Bitcoin, Merkle Trees digunakan untuk mengelompokkan dan meringkas transaksi dari sebuah blok menjadi satu hash, yang disebut Merkle Root (atau "*Root Hash*"). Setiap transaksi di-hash, kemudian hash-hash yang bersebelahan di-hash bersama secara hierarkis sampai Merkle Root diperoleh.

![](../../dictionnaire/assets/1.png)

Struktur ini memungkinkan verifikasi cepat apakah transaksi spesifik termasuk dalam blok tertentu tanpa harus menganalisis semua transaksi. Sebagai contoh, jika saya hanya memiliki Merkle Root dan saya ingin memverifikasi bahwa `TX 7` memang bagian dari pohon, saya hanya memerlukan bukti-bukti berikut:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
Dengan informasi-informasi ini, saya dapat menghitung node-node perantara sampai ke Merkle Root.

![](../../dictionnaire/assets/2.png)

Merkle Trees secara khusus digunakan untuk node ringan (dikenal sebagai "SPV") yang hanya menyimpan header blok, tetapi tidak transaksi. Struktur ini juga ditemukan dalam protokol UTREEXO, sebuah protokol yang memungkinkan pengondensasian set UTXO dari node, dan dalam MAST Taproot.

> ► *Merkle Tree dinamai menurut Ralph Merkle, seorang kriptografer yang merancang struktur ini pada tahun 1979. Merkle Tree juga dapat disebut sebagai "hash tree". Dalam bahasa Prancis, ini disebut sebagai "Arbre de Merkle" atau "arbre de hachage".*