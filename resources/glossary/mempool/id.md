---
term: MEMPOOL
---

Sebuah singkatan dari istilah "memory" dan "pool". Ini merujuk pada ruang virtual di mana transaksi Bitcoin yang menunggu untuk dimasukkan dalam sebuah blok dikelompokkan bersama. Ketika sebuah transaksi dibuat dan disiarkan di jaringan Bitcoin, pertama-tama transaksi tersebut diverifikasi oleh node-node jaringan. Jika dianggap valid, maka transaksi tersebut ditempatkan dalam Mempool dari setiap node, di mana ia tetap berada sampai dipilih oleh penambang untuk dimasukkan dalam sebuah blok.

Penting untuk dicatat bahwa setiap node dalam jaringan Bitcoin memelihara Mempoolnya sendiri, dan oleh karena itu, bisa ada variasi dalam isi Mempool antar node pada waktu tertentu. Secara khusus, parameter `maxmempool` dalam file `bitcoin.conf` dari setiap node memungkinkan operator untuk mengontrol jumlah RAM (random access memory) yang akan digunakan node mereka untuk menyimpan transaksi yang tertunda di Mempool. Dengan membatasi ukuran Mempool, operator node dapat mencegahnya dari mengonsumsi terlalu banyak sumber daya pada sistem mereka. Parameter ini ditentukan dalam megabita (MB). Nilai default untuk Bitcoin Core hingga saat ini adalah 300 MB.

Transaksi yang ada di Mempool bersifat sementara. Transaksi tersebut tidak seharusnya dianggap tidak dapat diubah sampai mereka dimasukkan dalam sebuah blok, dan setelah sejumlah konfirmasi tertentu. Transaksi ini sering kali bisa digantikan atau dihapus.