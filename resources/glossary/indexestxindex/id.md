---
term: INDEXES/TXINDEX/
---

File di Bitcoin Core yang didedikasikan untuk mengindeks semua transaksi yang ada dalam blockchain. Pengindeksan ini memungkinkan pencarian informasi rinci tentang sebuah transaksi dengan cepat menggunakan identifikasinya (TXID), tanpa harus melalui seluruh blockchain. Pembuatan file indeks ini adalah opsi yang tidak diaktifkan secara default di Bitcoin Core. Jika fitur ini tidak diaktifkan, node Anda hanya akan mengindeks transaksi yang terkait dengan dompet yang terhubung ke node Anda. Untuk mengaktifkan pengindeksan semua transaksi, Anda harus mengatur parameter `-txindex=1` dalam file `bitcoin.conf`. Opsi ini sangat berguna untuk aplikasi dan layanan yang sering mencari melalui riwayat transaksi Bitcoin.