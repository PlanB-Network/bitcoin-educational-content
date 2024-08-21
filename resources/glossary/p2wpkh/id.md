---
term: P2WPKH
---

P2WPKH merupakan singkatan dari *Pay to Witness Public Key Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO. P2WPKH diperkenalkan bersamaan dengan implementasi SegWit pada Agustus 2017.

Skrip ini mirip dengan P2PKH (*Pay to Public Key Hash*), karena juga mengunci bitcoin berdasarkan hash dari kunci publik, yaitu, alamat penerima. Perbedaannya terletak pada bagaimana tanda tangan dan skrip dimasukkan dalam transaksi. Dalam kasus P2WPKH, informasi skrip tanda tangan (`scriptSig`) dipindahkan dari struktur transaksi tradisional ke sebuah bagian terpisah yang disebut `Witness`. Pemindahan ini merupakan fitur dari pembaruan SegWit (*Segregated Witness*) yang membantu mencegah malleability tanda tangan. Transaksi P2WPKH umumnya lebih murah dalam hal biaya dibandingkan dengan transaksi Legacy, karena bagian dalam witness biayanya lebih rendah.

Alamat P2WPKH ditulis menggunakan pengkodean `Bech32` dengan checksum dalam bentuk kode BCH. Alamat ini selalu dimulai dengan `bc1q`. P2WPKH adalah output SegWit versi 0.