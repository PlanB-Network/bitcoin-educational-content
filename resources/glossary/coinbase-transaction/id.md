---
istilah: COINBASE (TRANSAKSI)
---

Transaksi coinbase adalah transaksi khusus dan unik yang termasuk dalam setiap blok dari blockchain Bitcoin. Ini mewakili transaksi pertama dari sebuah blok dan dibuat oleh penambang yang telah berhasil menemukan header yang memvalidasi bukti kerja (*Proof-of-Work*), yaitu, kurang dari atau sama dengan target.

Transaksi coinbase terutama berfungsi dua tujuan: untuk memberikan hadiah blok kepada penambang dan untuk menambahkan unit bitcoin baru ke dalam suplai uang yang beredar. Hadiah blok, yang merupakan insentif ekonomi bagi penambang untuk terlibat dalam bukti kerja, mencakup biaya terkumpul untuk transaksi yang termasuk dalam blok dan jumlah bitcoin yang baru diciptakan ex-nihilo (subsidi blok). Jumlah ini, yang awalnya ditetapkan sebesar 50 bitcoin per blok pada tahun 2009, dibagi dua setiap 210.000 blok (sekitar setiap 4 tahun) selama sebuah peristiwa yang disebut "halving."

Transaksi coinbase berbeda dari transaksi reguler dalam beberapa cara. Pertama, ia tidak memiliki input, berarti tidak ada output transaksi yang ada (UTXO) yang dikonsumsi olehnya. Selanjutnya, skrip tanda tangan (`scriptSig`) untuk transaksi coinbase biasanya berisi sebuah bidang sembarang yang memungkinkan untuk penyertaan data tambahan, seperti pesan kustom atau informasi versi perangkat lunak penambangan. Akhirnya, bitcoin yang dihasilkan oleh transaksi coinbase tunduk pada periode kematangan 100 blok (101 konfirmasi) sebelum dapat dihabiskan, untuk mencegah potensi pengeluaran bitcoin yang tidak ada dalam kasus reorganisasi rantai.

> ► *Tidak ada terjemahan untuk "Coinbase" dalam bahasa Prancis. Oleh karena itu, diterima untuk menggunakan istilah ini secara langsung.*