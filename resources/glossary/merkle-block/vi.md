---
term: Khối Merkle

definition: Cấu trúc cung cấp bằng chứng nhỏ gọn về việc bao gồm một giao dịch trong một khối cho các ứng dụng khách nhẹ.
---
A data structure used in the context of BIP37 (*Transaction Bloom Filtering*) to provide a compact proof of the inclusion of specific transactions in a block. It is notably used for SPV wallets. The Merkle Block contains the block headers, filtered transactions, and a partial Merkle tree, allowing light clients to quickly verify if a transaction belongs to a block without downloading all the transactions.