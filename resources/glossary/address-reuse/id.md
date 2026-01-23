---
term: Penggunaan ulang alamat

definition: Praktik yang tidak disarankan menggunakan alamat Bitcoin yang sama berkali-kali untuk menerima pembayaran, yang merusak privasi dengan memungkinkan pelacakan dana.
---
Penggunaan ulang alamat merujuk pada praktik penggunaan alamat penerima yang sama untuk beberapa UTXO, terkadang dalam beberapa transaksi yang berbeda. Bitcoin biasanya dikunci menggunakan pasangan kunci kriptografi yang berkaitan dengan alamat unik. Karena _blockchain_ bersifat publik, maka mudah untuk melihat bitcoin yang ada di tiap alamat. Apabila alamat yang sama digunakan untuk pembayaran yang berbeda-beda, dapat disimpulkan bahwa semua UTXO yang berkaitan dimiliki oleh pihak yang sama. Oleh karena itu, penggunaan ulang alamat menimbulkan masalah bagi privasi pengguna. Hal ini memungkinkan adanya hubungan deterministik antara beberapa transaksi dan UTXO, dan lalu lintas transaksi ini dapat dilacak secara _on-chain_. Satoshi Nakamoto telah menyebutkan masalah ini dalam _White Paper_-nya:

> *Sebagai firewall tambahan, sepasang kunci baru harus digunakan untuk setiap transaksi agar tidak dapat dikaitkan dengan pemilik yang sama.*

Nakamoto, S. (2008). "*Bitcoin: A Peer-to-Peer Electronic Cash System*". https://bitcoin.org/bitcoin.pdf.

Setidaknya, untuk menjaga privasi, sangat disarankan untuk menggunakan setiap alamat penerima hanya satu kali. Untuk setiap transaksi baru, sebaiknya buatlah alamat baru. Untuk output berupa kembalian, alamat baru juga harus digunakan. Untungnya, berkat dompet yang bersifat deterministik hirarkis (HD), pembuatan alamat menjadi lebih mudah. Semua pasangan kunci yang terkait dengan sebuah dompet dapat dengan mudah dibuat ulang dari suatu _seed_. Ini juga merupakan alasan mengapa perangkat lunak dompet selalu menghasilkan alamat baru yang berbeda ketika Anda menekan tombol "Terima".

