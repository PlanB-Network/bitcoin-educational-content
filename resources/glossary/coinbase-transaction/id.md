---
term: COINBASE (TRANSAKSI)

---
Transaksi coinbase adalah transaksi khusus dan unik yang disertakan dalam setiap blok blockchain Bitcoin. Transaksi ini merupakan transaksi pertama dalam sebuah blok dan dibuat oleh penambang yang telah berhasil menemukan header yang memvalidasi bukti kerja (*Proof-of-Work*), yaitu kurang dari atau sama dengan target.

Transaksi coinbase memiliki dua tujuan utama: untuk memberikan hadiah blok kepada penambang dan untuk menambahkan unit bitcoin baru ke dalam jumlah uang yang beredar. Hadiah blok, yang merupakan insentif ekonomi bagi para penambang untuk terlibat dalam bukti kerja, termasuk akumulasi biaya untuk transaksi yang termasuk dalam blok dan sejumlah bitcoin yang baru dibuat ex-nihilo (subsidi blok). Jumlah ini, yang awalnya ditetapkan sebesar 50 bitcoin per blok pada tahun 2009, dibagi dua setiap 210.000 blok (kira-kira setiap 4 tahun) selama acara yang disebut "halving"

Transaksi coinbase berbeda dari transaksi biasa dalam beberapa hal. Pertama, ia tidak memiliki input, yang berarti tidak ada output transaksi yang ada (UTXO) yang dikonsumsi olehnya. Selanjutnya, skrip tanda tangan (`scriptSig`) untuk transaksi coinbase biasanya berisi sebuah bidang arbitrer yang memungkinkan penggabungan data tambahan, seperti pesan khusus atau informasi versi perangkat lunak penambangan. Terakhir, bitcoin yang dihasilkan oleh transaksi coinbase tunduk pada periode jatuh tempo 100 blok (101 konfirmasi) sebelum dapat digunakan, untuk mencegah potensi pengeluaran bitcoin yang tidak ada jika terjadi reorganisasi rantai.

> ► *Tidak ada terjemahan untuk "Coinbase" dalam bahasa Prancis. Oleh karena itu, istilah ini dapat digunakan secara langsung.*