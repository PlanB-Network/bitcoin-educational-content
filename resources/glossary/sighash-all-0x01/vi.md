---
term: SIGHASH_ALL (0X01)

---
Type of SigHash Flag used in Bitcoin transaction signatures to indicate that the signature applies to all components of the transaction. By using `SIGHASH_ALL`, the signer covers all the inputs and all the outputs. This means that neither the inputs nor the outputs can be modified after the signature without invalidating it. This type of SigHash Flag is the most common in Bitcoin transactions, as it ensures complete finality and integrity of the transaction.