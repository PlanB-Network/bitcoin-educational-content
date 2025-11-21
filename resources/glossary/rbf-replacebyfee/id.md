---
term: RBF (REPLACE BY FEE)

---
Mekanisme transaksi yang memungkinkan pengirim untuk mengganti satu transaksi dengan transaksi lain dengan membayar biaya yang lebih tinggi, untuk mempercepat konfirmasinya. Jika transaksi dengan biaya yang terlalu rendah macet, pengirim dapat menggunakan *Replace-by-Fee* untuk meningkatkan biaya dan memprioritaskan transaksi penggantinya di _mempool_.

RBF dapat diterapkan selama transaksi berada dalam _mempool_; sekali berada dalam blok, transaksi tersebut tidak dapat lagi diganti. Pada pengiriman awal, transaksi harus menentukan ketersediaannya untuk diganti dengan menyesuaikan nilai `nSequence` ke angka yang kurang dari `xfffffffffe`. Ini dikenal sebagai "_flag_" RBF. Pengaturan ini menandakan kemungkinan untuk memperbarui transaksi setelah disiarkan, yang kemudian memungkinkan RBF. Namun, terkadang dimungkinkan untuk mengganti transaksi yang belum menandakan RBF. Node yang menggunakan parameter konfigurasi `mempoolfullrbf=1` menerima penggantian ini meskipun RBF awalnya tidak disinyalkan.

Tidak seperti CPFP (*Child Pays For Parent*), di mana penerima dapat bertindak untuk mempercepat transaksi, RBF (*Replace-By-Fee*) memungkinkan pengirim untuk mengambil inisiatif untuk mempercepat transaksi mereka sendiri dengan meningkatkan biaya.
