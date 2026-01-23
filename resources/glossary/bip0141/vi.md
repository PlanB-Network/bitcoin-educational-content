---
term: BIP0141

definition: Giới thiệu SegWit (Segregated Witness), tách chữ ký khỏi phần còn lại của giao dịch để giải quyết tính dễ bị uốn nắn (malleability).
---
Introduced the concept of Segregated Witness (SegWit) which gave its name to the SegWit soft fork. BIP141 introduces a major modification to the Bitcoin protocol aimed at solving the transaction malleability problem. SegWit separates the witness (signature data) from the rest of the transaction data. This separation is achieved by inserting the witnesses into a separate data structure, committed in a new Merkle tree, which is itself referenced in the block via the coinbase transaction, making SegWit compatible with older versions of the protocol.