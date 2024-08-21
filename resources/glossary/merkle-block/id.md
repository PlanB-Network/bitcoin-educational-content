---
term: MERKLE BLOCK
---

Struktur data yang digunakan dalam konteks BIP37 (*Transaction Bloom Filtering*) untuk memberikan bukti kompak tentang inklusi transaksi tertentu dalam sebuah blok. Ini secara khusus digunakan untuk dompet SPV. Merkle Block berisi header blok, transaksi yang difilter, dan pohon Merkle parsial, memungkinkan klien ringan untuk cepat memverifikasi apakah sebuah transaksi termasuk dalam sebuah blok tanpa harus mengunduh semua transaksi.