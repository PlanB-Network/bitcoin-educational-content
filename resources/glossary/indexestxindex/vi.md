---
term: Indexes/txindex/

definition: Các tệp Bitcoin Core lập chỉ mục tất cả các giao dịch để tìm kiếm nhanh theo mã nhận dạng.
---
Files in Bitcoin Core that are dedicated to indexing all transactions present in the blockchain. This indexing allows for quick searching of detailed information about a transaction using its identifier (TXID), without having to go through the entire blockchain. The creation of these indexing files is an option not enabled by default in Bitcoin Core. If this feature is not enabled, your node will only index transactions associated with wallets attached to your node. To enable indexing of all transactions, you must set the parameter `-txindex=1` in the `bitcoin.conf` file. This option is particularly useful for applications and services that frequently search through the transaction history of Bitcoin.