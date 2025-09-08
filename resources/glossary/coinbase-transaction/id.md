---
term: COINBASE (TRANSAKSI)

---
Transaksi _coinbase_ adalah transaksi khusus dan unik yang disertakan dalam setiap blok _blockchain_ Bitcoin. Transaksi ini merupakan transaksi pertama dalam sebuah blok dan dibuat oleh penambang yang telah berhasil menemukan _header_ yang memvalidasi bukti kerja (*Proof-of-Work*) kurang dari atau sama dengan target.

Transaksi _coinbase_ memiliki dua tujuan utama: untuk memberikan _block reward_ kepada penambang dan untuk menambahkan unit bitcoin baru ke dalam jumlah uang yang beredar. _Block reward_, yang merupakan insentif ekonomi bagi para penambang untuk terlibat dalam bukti kerja, termasuk akumulasi biaya untuk transaksi yang termasuk dalam blok dan sejumlah bitcoin yang diciptakan (subsidi blok). Jumlah ini, yang awalnya ditetapkan sebesar 50 bitcoin per blok pada tahun 2009, dan berkurang menjadi setengahnya setiap 210.000 blok (kira-kira setiap 4 tahun) melalui mekanisme yang disebut "_halving_"

Transaksi _coinbase_ berbeda dari transaksi biasa dalam beberapa hal. Pertama, transaksi ini tidak memiliki input, yang berarti tidak ada output transaksi (UTXO) yang dikonsumsi. Selanjutnya, skrip tanda tangan (`scriptSig`) untuk transaksi _coinbase_ biasanya berisi sebuah bidang arbitrer yang memungkinkan penggabungan data tambahan, seperti pesan khusus atau informasi versi perangkat lunak penambangan. Terakhir, bitcoin yang dihasilkan oleh transaksi _coinbase_ tunduk pada _maturity period_ 100 blok (101 konfirmasi) sebelum dapat digunakan, untuk mencegah potensi pengeluaran bitcoin yang tidak ada jika terjadi reorganisasi rantai.

> ► *Tidak ada terjemahan untuk "Coinbase" dalam bahasa Indonesia. Oleh karena itu, istilah ini dapat digunakan secara langsung.*
