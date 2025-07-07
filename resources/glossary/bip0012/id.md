---
term: BIP0012

---
BIP12 merupakan proposal dari Gavin Andresen untuk meningkatkan fleksibilitas dan privasi skrip transaksi Bitcoin. BIP ini menyarankan implementasi sebuah _opcode_ skrip baru, bernama `OP_EVAL`, yang memungkinkan evaluasi sebuah skrip yang terdapat di dalam data `scriptSig` selama proses validasi transaksi. Modifikasi utama dari BIP12 adalah untuk mengizinkan penyertaan satu skrip di dalam skrip lainnya. Teknik ini memungkinkan pembuatan ketentuan yang lebih kompleks, sehingga dapat diverifikasi pada saat bitcoin digunakan, tanpa perlu mengungkapkannya kepada pengguna yang mengirimkan bitcoin ke alamat yang digunakan. BIP12 kemudian digantikan oleh proposal yang lebih aman, seperti BIP16 (P2SH), yang memperkenalkan metode yang berbeda untuk mencapai tujuan yang sama dengan `OP_EVAL`.
