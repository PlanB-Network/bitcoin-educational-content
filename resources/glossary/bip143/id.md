---
term: BIP143
---

Memperkenalkan cara baru dalam meng-hash transaksi untuk verifikasi tanda tangan dalam skrip pasca-SegWit. Tujuannya adalah untuk meminimalkan operasi redundan selama verifikasi dan untuk memasukkan nilai dari UTXO dalam input ke dalam tanda tangan. Ini menyelesaikan dua masalah utama dengan algoritma hashing transaksi asli:
* Pertumbuhan kuadratik dari peng-hash-an data dengan jumlah tanda tangan;
* Ketidakhadiran nilai input dalam tanda tangan, yang menimbulkan risiko bagi dompet hardware, terutama berkaitan dengan pengetahuan tentang biaya transaksi yang dikeluarkan.
Sejak pembaruan SegWit, yang dijelaskan dalam BIP141, memperkenalkan bentuk transaksi baru yang skripnya tidak akan diverifikasi oleh node lama, BIP143 memanfaatkan kesempatan ini untuk mengatasi masalah ini tanpa memerlukan hard fork. Oleh karena itu, BIP143 merupakan bagian dari soft fork SegWit.