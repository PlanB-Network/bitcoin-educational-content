---
term: P2WPKH

---
P2WPKH adalah singkatan dari *Bayar untuk Menyaksikan Public Key Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan ketentuan pengeluaran pada UTXO. P2WPKH diperkenalkan dengan implementasi SegWit pada bulan Agustus 2017.

Skrip ini mirip dengan P2PKH (*Bayar ke Public Key Hash*), karena juga mengunci bitcoin berdasarkan hash dari public key, yaitu alamat penerima. Perbedaannya terletak pada bagaimana tanda tangan dan skrip disertakan dalam transaksi. Dalam kasus P2WPKH, informasi skrip tanda tangan (`scriptSig`) dipindahkan dari struktur transaksi tradisional ke bagian terpisah yang disebut `Saksi`. Langkah ini merupakan fitur dari pembaruan SegWit (*Segregated Witness*) yang membantu mencegah pemalsuan tanda tangan. Transaksi P2WPKH umumnya lebih murah dalam hal biaya dibandingkan dengan transaksi Legacy, karena bagian dalam saksi lebih murah.

Alamat P2WPKH ditulis menggunakan pengkodean `Bech32` dengan checksum berupa kode BCH. Alamat-alamat ini selalu dimulai dengan `bc1q`. P2WPKH adalah keluaran SegWit versi 0.