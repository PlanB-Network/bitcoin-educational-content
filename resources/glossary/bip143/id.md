---
term: BIP143

---
Memperkenalkan cara baru dalam melakukan hashing transaksi untuk verifikasi tanda tangan dalam skrip pasca-SegWit. Tujuannya adalah untuk meminimalkan operasi yang berlebihan selama verifikasi dan untuk memasukkan nilai UTXO dalam input dalam tanda tangan. Hal ini memecahkan dua masalah utama dengan algoritma hashing transaksi yang asli:


- Pertumbuhan kuadratik hashing data dengan jumlah tanda tangan;
- Tidak adanya nilai input dalam tanda tangan, yang menimbulkan risiko pada dompet perangkat keras, terutama terkait pengetahuan tentang biaya transaksi yang terjadi.

Karena pembaruan SegWit, yang dijelaskan di BIP141, memperkenalkan bentuk transaksi baru yang skripnya tidak akan diverifikasi oleh node lama, BIP143 mengambil kesempatan ini untuk mengatasi masalah ini tanpa memerlukan hard fork. Oleh karena itu, BIP143 adalah bagian dari soft fork SegWit.