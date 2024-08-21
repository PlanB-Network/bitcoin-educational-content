---
term: PENGGUNAAN ULANG ALAMAT
---

Penggunaan ulang alamat merujuk pada praktik menggunakan alamat penerima yang sama untuk memblokir beberapa UTXO, terkadang dalam beberapa transaksi yang berbeda. Bitcoin biasanya dikunci menggunakan pasangan kunci kriptografi yang sesuai dengan alamat unik. Karena blockchain bersifat publik, mudah untuk melihat alamat mana yang terkait dengan berapa banyak bitcoin. Dalam kasus menggunakan alamat yang sama untuk beberapa pembayaran, wajar untuk membayangkan bahwa semua UTXO terkait milik entitas yang sama. Oleh karena itu, penggunaan ulang alamat menimbulkan masalah bagi privasi pengguna. Hal ini memungkinkan adanya tautan deterministik antara beberapa transaksi dan UTXO, serta memperpanjang pelacakan dana on-chain. Satoshi Nakamoto sudah menyebutkan masalah ini dalam White Paper-nya:

> "*Sebagai firewall tambahan, sepasang kunci baru bisa digunakan untuk setiap transaksi agar mereka tidak terhubung ke pemilik yang sama.*" - Nakamoto, S. (2008). "Bitcoin: Sistem Kas Elektronik Peer-to-Peer". Dikonsultasikan di https://bitcoin.org/bitcoin.pdf.

Untuk menjaga privasi setidaknya pada tingkat minimal, sangat disarankan untuk menggunakan setiap alamat penerima hanya sekali. Untuk setiap pembayaran baru, sebaiknya menghasilkan alamat baru. Untuk output kembalian, alamat baru juga harus digunakan. Beruntungnya, berkat dompet deterministik dan hierarkis, telah menjadi sangat mudah untuk menggunakan berbagai alamat. Semua pasangan kunci yang terkait dengan dompet dapat dengan mudah dihasilkan kembali dari seed. Ini juga alasan mengapa perangkat lunak dompet selalu menghasilkan alamat baru yang berbeda ketika Anda mengklik tombol “Terima”.

> ► *Dalam bahasa Inggris, ini disebut "Address Reuse".*