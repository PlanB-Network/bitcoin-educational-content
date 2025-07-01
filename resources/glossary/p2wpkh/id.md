---
term: P2WPKH

---
P2WPKH adalah singkatan dari *Pay to Witness Public Key Hash*, yang adalah model skrip standar yang digunakan untuk menetapkan ketentuan pengeluaran pada UTXO. P2WPKH diperkenalkan dengan implementasi SegWit pada bulan Agustus 2017.

Skrip ini mirip dengan P2PKH (*Pay to Public Key Hash*), karena juga mengunci bitcoin berdasarkan _hash_ dari _public key_, yaitu alamat penerima. Perbedaannya terletak pada bagaimana tanda tangan dan skrip disertakan dalam transaksi. Dalam kasus P2WPKH, informasi skrip tanda tangan (`scriptSig`) dipindahkan dari struktur transaksi tradisional ke bagian terpisah yang disebut `Saksi`. Langkah ini merupakan fitur dari pembaruan SegWit (*Segregated Witness*) yang membantu mencegah pemalsuan tanda tangan. Transaksi P2WPKH umumnya lebih murah dalam hal biaya dibandingkan dengan transaksi Legacy, karena bagian dalam _witness_ lebih murah.

Alamat P2WPKH ditulis menggunakan pengkodean `Bech32` dengan _checksum_ berupa kode BCH. Alamat-alamat ini selalu dimulai dengan `bc1q`. P2WPKH adalah keluaran SegWit versi 0.
