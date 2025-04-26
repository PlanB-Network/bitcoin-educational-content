---
term: SIMPLIFIED PAYMENT VERIFICATION

---
Method allowing light clients to verify Bitcoin transactions without downloading the entire blockchain. A node using SPV only downloads the block headers, which are much lighter than the complete blocks. When it needs to verify a transaction, the SPV node requests a Merkle proof from full nodes to confirm that the transaction is included in a specific block. This approach is efficient for devices with limited resources, such as smartphones, but it implies a dependence on full nodes, which can reduce security and increase the required trust.

> ► *The acronym "SPV" is often used to refer to this method.*