---
term: BLOCKS/REV*.DAT

---
Nama file dalam Bitcoin Core yang menyimpan informasi yang dibutuhkan untuk membalikkan perubahan yang dibuat pada set UTXO yang ditetapkan oleh blok yang ditambahkan sebelumnya. Setiap file diidentifikasi dengan nomor unik yang sama dengan file blk*.dat yang terkait dengannya. File rev * .dat berisi data pembalikan yang sesuai dengan blok yang disimpan dalam file blk * .dat. Data ini pada dasarnya adalah daftar semua UTXO yang dihabiskan sebagai input dalam sebuah blok. File pembalikan ini memungkinkan node untuk kembali ke keadaan sebelumnya jika terjadi reorganisasi blockchain yang menyebabkan blok yang divalidasi sebelumnya dibuang.