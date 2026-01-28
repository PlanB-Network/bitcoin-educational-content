---
term: SIGHASH_NONE (0X02)

definition: Cờ SigHash trong đó chữ ký bao gồm tất cả các đầu vào nhưng không có đầu ra nào của giao dịch.
---
Type of SigHash Flag used in Bitcoin transaction signatures to indicate that the signature applies to all the inputs of the transaction, but to none of its outputs. The use of `SIGHASH_NONE` implies that the signer commits only to the inputs, allowing the outputs to remain undetermined or modifiable after signing. This type of signature is useful in cases where the signer wishes to authorize other parties to decide how the bitcoins will be distributed in the transaction.