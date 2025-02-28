---
term: BLOK MERKLE

---
Struktur data yang digunakan dalam konteks BIP37 (*Transaction Bloom Filtering*) untuk memberikan bukti ringkas tentang penyertaan transaksi tertentu dalam sebuah blok. Struktur ini terutama digunakan untuk dompet SPV. Blok Merkle berisi header blok, transaksi yang difilter, dan pohon Merkle parsial, yang memungkinkan klien ringan untuk dengan cepat memverifikasi apakah suatu transaksi termasuk dalam blok tanpa mengunduh semua transaksi.