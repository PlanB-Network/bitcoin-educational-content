---
term: P2WSH
---

P2WSH merupakan singkatan dari *Pay to Witness Script Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO. P2WSH diperkenalkan bersamaan dengan implementasi SegWit pada Agustus 2017.

Skrip ini mirip dengan P2SH (*Pay to Public Script Hash*), karena juga mengunci bitcoin berdasarkan hash dari sebuah skrip. Perbedaannya terletak pada bagaimana tanda tangan dan skrip dimasukkan ke dalam transaksi. Untuk menghabiskan bitcoin pada jenis skrip ini, penerima harus menyediakan skrip asli, yang disebut `witnessScript` (setara dengan `redeemScript`), bersama dengan tanda tangan yang diperlukan. Mekanisme ini memungkinkan implementasi kondisi pengeluaran yang lebih canggih, seperti multisig.

Dalam konteks P2WSH, informasi skrip tanda tangan (yang `scriptWitness`, setara dengan `scriptSig`) dipindahkan dari struktur transaksi tradisional ke sebuah bagian terpisah yang disebut `Witness`. Pemindahan ini merupakan fitur dari pembaruan SegWit (*Segregated Witness*) yang membantu mencegah malleability tanda tangan. Transaksi P2WSH umumnya lebih murah dalam hal biaya dibandingkan dengan transaksi Legacy, karena bagian dalam witness biayanya lebih rendah.

Alamat P2WSH ditulis menggunakan pengkodean `Bech32` dengan checksum dalam bentuk kode BCH. Alamat ini selalu dimulai dengan `bc1q`. P2WSH adalah output SegWit versi 0.