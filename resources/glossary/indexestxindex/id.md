---
term: INDEXS/TXINDEX/

---
File dalam Bitcoin Core yang didedikasikan untuk mengindeks semua transaksi yang ada dalam blockchain. Pengindeksan ini memungkinkan pencarian cepat informasi detail mengenai sebuah transaksi dengan menggunakan pengenalnya (TXID), tanpa harus menelusuri seluruh blockchain. Pembuatan file pengindeksan ini merupakan opsi yang tidak diaktifkan secara default di Bitcoin Core. Jika fitur ini tidak diaktifkan, node Anda hanya akan mengindeks transaksi yang terkait dengan wallet yang terhubung dengan node Anda. Untuk mengaktifkan pengindeksan semua transaksi, Anda harus mengatur parameter `-txindex=1` dalam file `bitcoin.conf`. Opsi ini sangat berguna untuk aplikasi dan layanan yang sering mencari riwayat transaksi Bitcoin.