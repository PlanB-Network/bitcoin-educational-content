---
term: MEMPOOL

---
Sebuah kontraksi dari istilah "memori" dan "pool". Ini mengacu pada ruang virtual di mana transaksi Bitcoin yang menunggu dimasukkan ke dalam blok dikelompokkan bersama. Ketika sebuah transaksi dibuat dan disiarkan di jaringan Bitcoin, transaksi tersebut diverifikasi terlebih dahulu oleh node-node jaringan. Jika dianggap valid, transaksi tersebut akan ditempatkan di Mempool setiap node, di mana transaksi tersebut akan tetap berada hingga dipilih oleh penambang untuk dimasukkan ke dalam blok.

Penting untuk diperhatikan bahwa setiap node dalam jaringan Bitcoin memiliki Mempool-nya sendiri, dan oleh karena itu, mungkin terdapat variasi dalam konten Mempool antara node yang berbeda pada waktu tertentu. Khususnya, parameter `maxmempool` dalam file `bitcoin.conf` pada setiap node memungkinkan operator untuk mengontrol jumlah RAM (random access memory) yang akan digunakan oleh node mereka untuk menyimpan transaksi yang tertunda dalam Mempool. Dengan membatasi ukuran Mempool, operator node dapat mencegahnya mengkonsumsi terlalu banyak sumber daya pada sistem mereka. Parameter ini ditentukan dalam satuan megabyte (MB). Nilai default untuk Bitcoin Core hingga saat ini adalah 300 MB.

Transaksi yang ada di Mempool bersifat sementara. Transaksi tersebut tidak boleh dianggap tidak dapat diubah sampai transaksi tersebut dimasukkan ke dalam blok, dan setelah sejumlah konfirmasi. Transaksi-transaksi ini sering kali dapat diganti atau dihapus.