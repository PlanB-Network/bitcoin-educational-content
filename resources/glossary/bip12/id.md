---
term: BIP12
---

Proposal oleh Gavin Andresen untuk meningkatkan fleksibilitas dan privasi dari skrip transaksi Bitcoin. BIP ini menyarankan implementasi sebuah opcode skrip baru, yang dinamakan `OP_EVAL`, yang memungkinkan evaluasi skrip yang terkandung dalam data dari `scriptSig` selama proses validasi transaksi. Modifikasi utama dari BIP12 adalah untuk memungkinkan penyertaan satu skrip di dalam skrip lain. Teknik ini memungkinkan penciptaan kondisi yang lebih kompleks yang dapat diverifikasi pada saat pengeluaran, tanpa perlu mengungkapkannya kepada pengguna yang mengirim bitcoin ke alamat yang digunakan. BIP12 kemudian digantikan oleh proposal yang lebih aman, terutama BIP16 (P2SH), yang menawarkan metode berbeda untuk mencapai tujuan yang sama seperti `OP_EVAL`.