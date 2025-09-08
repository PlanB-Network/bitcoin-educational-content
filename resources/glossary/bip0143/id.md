---
term: BIP0143

---
Memperkenalkan cara baru melakukan _hashing_ transaksi untuk verifikasi tanda tangan dalam skrip pasca-SegWit. Tujuannya adalah untuk meminimalkan beban operasi yang berlebihan selama verifikasi dan untuk memasukkan nilai UTXO dalam input dalam tanda tangan. Hal ini memecahkan dua masalah utama dengan algoritma _hashing_ transaksi sebelumnya:


- Pertumbuhan kuadratik _hashing_ data dengan jumlah tanda tangan;
- Tidak adanya nilai input dalam tanda tangan, yang menimbulkan risiko pada dompet perangkat keras, terutama terkait pengetahuan tentang biaya transaksi yang terjadi.

Karena pembaruan SegWit, yang dipaparkan di BIP141, memperkenalkan bentuk transaksi baru yang skripnya tidak akan diverifikasi oleh node lama, BIP143 mengambil kesempatan ini untuk mengatasi masalah ini tanpa memerlukan _hard fork_. Oleh karena itu, BIP143 adalah bagian dari _soft fork_ SegWit.
