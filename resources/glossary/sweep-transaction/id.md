---
term: TRANSAKSI SAPUAN

---
Pola atau model transaksi yang digunakan dalam analisis rantai untuk menentukan sifat transaksi. Model ini ditandai dengan konsumsi satu UTXO sebagai input dan produksi satu UTXO sebagai output. Interpretasi dari model ini adalah bahwa kita berada di hadapan transfer sendiri. Pengguna telah mentransfer bitcoin mereka ke diri mereka sendiri, ke alamat lain yang mereka miliki. Karena tidak ada perubahan dalam transaksi, maka sangat kecil kemungkinannya bahwa kita berurusan dengan pembayaran. Memang, ketika pembayaran dilakukan, hampir tidak mungkin bagi pembayar untuk memiliki UTXO yang sama persis dengan jumlah yang diminta oleh penjual, selain biaya transaksi. Umumnya, pembayar dipaksa untuk menghasilkan output kembalian. Kita kemudian tahu bahwa pengguna yang diamati kemungkinan masih memiliki UTXO ini. Dalam konteks analisis rantai, jika kita tahu bahwa UTXO yang digunakan sebagai input dalam transaksi adalah milik Alice, kita dapat mengasumsikan bahwa UTXO yang dihasilkan juga merupakan miliknya.

![](../../dictionnaire/assets/6.webp)

> ► *Dalam bahasa Prancis, "transaksi sapuan" dapat diterjemahkan sebagai "transaksi de balayage".*