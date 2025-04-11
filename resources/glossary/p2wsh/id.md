---
term: P2WSH

---
P2WSH adalah singkatan dari *Bayar untuk Menyaksikan Script Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan ketentuan pengeluaran pada UTXO. P2WSH diperkenalkan dengan implementasi SegWit pada bulan Agustus 2017.

Skrip ini mirip dengan P2SH (*Bayar ke Public Script Hash*), karena ia juga mengunci bitcoin berdasarkan hash dari sebuah skrip. Perbedaannya terletak pada bagaimana tanda tangan dan skrip disertakan dalam transaksi. Untuk membelanjakan bitcoin pada jenis skrip ini, penerima harus menyediakan skrip asli, yang disebut `witnessScript` (setara dengan `redeemScript`), bersama dengan tanda tangan yang diperlukan. Mekanisme ini memungkinkan implementasi kondisi pembelanjaan yang lebih canggih, seperti multisig.

Dalam konteks P2WSH, informasi skrip tanda tangan (`scriptWitness`, setara dengan `scriptSig`) dipindahkan dari struktur transaksi tradisional ke bagian terpisah yang disebut `Witness`. Langkah ini merupakan fitur dari pembaruan SegWit (*Segregated Witness*) yang membantu mencegah kelenturan tanda tangan. Transaksi P2WSH umumnya lebih murah dalam hal biaya dibandingkan dengan transaksi Legacy, karena bagian dalam saksi lebih murah.

Alamat P2WSH ditulis menggunakan pengkodean `Bech32` dengan checksum berupa kode BCH. Alamat-alamat ini selalu dimulai dengan `bc1q`. P2WSH adalah keluaran SegWit versi 0.