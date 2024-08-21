---
term: RBF (REPLACE-BY-FEE)
---

Mekanisme transaksional yang memungkinkan pengirim untuk menggantikan satu transaksi dengan transaksi lain dengan membayar biaya yang lebih tinggi, untuk mempercepat konfirmasinya. Jika sebuah transaksi dengan biaya terlalu rendah terhenti, pengirim dapat menggunakan *Replace-By-Fee* untuk meningkatkan biaya dan memprioritaskan transaksi penggantinya di mempool.

RBF berlaku selama transaksi berada di mempool; setelah berada dalam blok, transaksi tersebut tidak lagi dapat digantikan. Pada saat pengiriman awal, transaksi harus menentukan ketersediaannya untuk digantikan dengan menyesuaikan nilai `nSequence` menjadi angka kurang dari `0xfffffffe`. Ini dikenal sebagai "flag" RBF. Pengaturan ini menandakan kemungkinan pembaruan transaksi setelah disiarkan, yang selanjutnya memungkinkan RBF. Namun, terkadang mungkin untuk menggantikan transaksi yang tidak menandakan RBF. Node yang menggunakan parameter konfigurasi `mempoolfullrbf=1` menerima penggantian ini meskipun RBF tidak awalnya ditandai.

Berbeda dengan CPFP (*Child Pays For Parent*), di mana penerima dapat bertindak untuk mempercepat transaksi, RBF (*Replace-By-Fee*) memungkinkan pengirim untuk mengambil inisiatif mempercepat transaksi mereka sendiri dengan meningkatkan biaya.