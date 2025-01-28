---
term: WTXID

---
Perpanjangan dari TXID tradisional, termasuk data saksi yang diperkenalkan dengan SegWit. Sementara TXID adalah hash dari data transaksi tidak termasuk saksi, WTXID adalah `SHA256d` dari seluruh data transaksi, termasuk saksi. WTXID disimpan dalam pohon Merkle yang terpisah yang akarnya ditempatkan dalam transaksi coinbase. Pemisahan ini memungkinkan untuk menghilangkan kelenturan transaksi TXID.