---
term: WTXID
---

Sebuah perluasan dari TXID tradisional, termasuk data saksi yang diperkenalkan dengan SegWit. Sementara TXID adalah hash dari data transaksi yang tidak termasuk saksi, WTXID adalah `SHA256d` dari seluruh data transaksi, termasuk saksi. WTXID disimpan dalam sebuah pohon Merkle terpisah yang akarnya ditempatkan dalam transaksi coinbase. Pemisahan ini memungkinkan penghapusan kemampuan transaksi TXID untuk dimanipulasi.