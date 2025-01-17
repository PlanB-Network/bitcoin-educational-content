---
term: PENGGUNAAN ULANG ALAMAT

---
Penggunaan ulang alamat merujuk pada praktik penggunaan alamat penerima yang sama untuk memblokir beberapa UTXO, terkadang dalam beberapa transaksi yang berbeda. Bitcoin biasanya dikunci menggunakan pasangan kunci kriptografi yang sesuai dengan alamat unik. Karena blockchain bersifat publik, maka mudah untuk melihat alamat mana yang terkait dengan berapa banyak bitcoin. Dalam kasus penggunaan ulang alamat yang sama untuk beberapa pembayaran, dapat dibayangkan bahwa semua UTXO yang terkait adalah milik entitas yang sama. Oleh karena itu, penggunaan ulang alamat menimbulkan masalah bagi privasi pengguna. Hal ini memungkinkan adanya hubungan deterministik antara beberapa transaksi dan UTXO, serta melanggengkan pelacakan dana secara on-chain. Satoshi Nakamoto telah menyebutkan masalah ini dalam Buku Putihnya:

> "*Sebagai firewall tambahan, sepasang kunci baru dapat digunakan untuk setiap transaksi agar tidak terhubung dengan pemilik yang sama*" - Nakamoto, S. (2008). "Bitcoin: Sebuah Sistem Uang Elektronik Peer-to-Peer". Dikonsultasikan di https://bitcoin.org/bitcoin.pdf.
Untuk menjaga privasi seminimal mungkin, sangat disarankan untuk menggunakan setiap alamat penerima hanya satu kali. Untuk setiap pembayaran baru, sebaiknya buatlah alamat baru. Untuk keluaran kembalian, alamat baru juga harus digunakan. Untungnya, berkat dompet yang bersifat deterministik dan hirarkis, penggunaan banyak alamat menjadi sangat mudah. Semua pasangan kunci yang terkait dengan sebuah dompet dapat dengan mudah dibuat ulang dari seed. Ini juga alasan mengapa perangkat lunak dompet selalu menghasilkan alamat baru yang berbeda ketika Anda mengklik tombol "Terima".

> ► *Dalam bahasa Inggris, ini disebut "Address Reuse" (Penggunaan Ulang Alamat)*