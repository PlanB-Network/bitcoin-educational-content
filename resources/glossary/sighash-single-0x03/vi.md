---
term: SIGHASH_SINGLE (0X03)

---
Type of SigHash Flag used in Bitcoin transaction signatures to indicate that the signature applies to all the inputs of the transaction and to only one output, corresponding to the index of the same input signed. Thus, each input signed with `SIGHASH_SINGLE` is specifically linked to a particular output. The other outputs are not committed by the signature and can therefore be modified later. This type of signature is useful in complex transactions, where participants want to link certain inputs to specific outputs, while leaving flexibility for the other outputs of the transaction.