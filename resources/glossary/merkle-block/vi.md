---
term: MERKLE BLOCK

---
A data structure used in the context of BIP37 (*Transaction Bloom Filtering*) to provide a compact proof of the inclusion of specific transactions in a block. It is notably used for SPV wallets. The Merkle Block contains the block headers, filtered transactions, and a partial Merkle tree, allowing light clients to quickly verify if a transaction belongs to a block without downloading all the transactions.