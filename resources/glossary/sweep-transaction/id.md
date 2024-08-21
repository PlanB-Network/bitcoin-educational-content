---
istilah: SWEEP TRANSACTION
---

Pola atau model transaksi yang digunakan dalam analisis rantai untuk menentukan sifat transaksi. Model ini ditandai dengan penggunaan satu UTXO sebagai input dan produksi satu UTXO sebagai output. Interpretasi dari model ini adalah bahwa kita berada dalam keadaan transfer diri. Pengguna telah mentransfer bitcoin mereka kepada diri mereka sendiri, ke alamat lain yang mereka miliki. Karena tidak ada perubahan dalam transaksi, sangat tidak mungkin bahwa kita sedang berurusan dengan pembayaran. Memang, ketika pembayaran dilakukan, hampir mustahil bagi pembayar untuk memiliki UTXO yang tepat sesuai dengan jumlah yang dibutuhkan oleh penjual, ditambah dengan biaya transaksi. Umumnya, pembayar oleh karena itu dipaksa untuk menghasilkan output kembalian. Kita kemudian tahu bahwa pengguna yang diamati kemungkinan masih memiliki UTXO ini. Dalam konteks analisis rantai, jika kita tahu bahwa UTXO yang digunakan sebagai input dalam transaksi milik Alice, kita dapat berasumsi bahwa UTXO di output juga miliknya.

![](../../dictionnaire/assets/6.png)

> ► *Dalam bahasa Prancis, "sweep transaction" dapat diterjemahkan sebagai "transaction de balayage".*