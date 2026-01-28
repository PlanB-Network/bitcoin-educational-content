---
term: UTXO

definition: Output transaksi yang belum dihabiskan yang mewakili sebagian bitcoin yang tersedia untuk digunakan sebagai input.
---
Singkatan dari *Unspent Transaction Output*. UTXO adalah output transaksi yang belum dibelanjakan, yang berarti belum digunakan sebagai input untuk transaksi baru. UTXO mewakili sebagian kecil bitcoin yang dimiliki pengguna dan saat ini tersedia untuk dibelanjakan. Setiap UTXO dihubungkan dengan sebuah skrip output tertentu (`scriptPubKey`), yang mendefinisikan kondisi yang diperlukan untuk membelanjakan bitcoin yang bersangkutan. Transaksi dalam Bitcoin menggunakan UTXO ini sebagai input dan membuat UTXO baru sebagai output. Model UTXO sangat penting untuk Bitcoin, karena model ini memungkinkan verifikasi yang mudah bahwa transaksi tidak mencoba untuk membelanjakan bitcoin yang tidak ada atau telah dibelanjakan.
