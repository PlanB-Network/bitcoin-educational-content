---
term: WTXID

---
Perpanjangan dari TXID tradisional, termasuk data _witness_ yang diperkenalkan dengan SegWit. Sementara TXID adalah _hash_ dari data transaksi tidak termasuk _witness_, WTXID adalah `SHA256d` dari seluruh data transaksi, termasuk _witness_. WTXID disimpan dalam pohon Merkle yang terpisah yang akarnya ditempatkan dalam transaksi _coinbase_. Pemisahan ini memungkinkan untuk menghilangkan maleabilitas transaksi TXID.
