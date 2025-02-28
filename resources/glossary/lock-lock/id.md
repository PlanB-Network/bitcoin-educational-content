---
term: LOCK (.LOCK)

---
File yang digunakan dalam Bitcoin Core untuk mengunci direktori data. File ini dibuat ketika bitcoind atau Bitcoin-qt mulai untuk mencegah beberapa contoh perangkat lunak mengakses direktori data yang sama secara bersamaan. Tujuannya adalah untuk mencegah konflik dan kerusakan data. Jika perangkat lunak berhenti secara tidak terduga, file .lock dapat tetap ada dan harus dihapus secara manual sebelum memulai ulang Bitcoin Core.