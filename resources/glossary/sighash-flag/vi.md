---
term: SIGHASH FLAG

---
A parameter in a Bitcoin transaction that determines which components of a transaction (inputs and outputs) are covered by the associated signature, thereby becoming immutable. The SigHash Flag is a byte added to the digital signature of each input. Therefore, the choice of SigHash Flag directly affects which parts of the transaction are frozen by the signature and which can still be modified afterwards. This mechanism ensures that signatures precisely and securely commit transaction data according to the signer's intention. There are three main SigHash Flags:


- `SIGHASH_ALL` (`0x01`): The signature applies to all the inputs and outputs of the transaction, thus locking them entirely;
- `SIGHASH_NONE` (`0x02`): The signature applies to all the inputs but none of the outputs, allowing the outputs to be modified after the signature;
- `SIGHASH_SINGLE` (`0x03`): The signature covers all the inputs and only one output corresponding to the index of the signed input.

In addition to these three SigHash Flags, the modifier `SIGHASH_ANYONECANPAY` (`0x80`) can be combined with each of the previous types. When this modifier is used, only a portion of the inputs is signed, leaving the others open to modification. Here are the existing combinations with the modifier:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): The signature applies to a single input while covering all the outputs of the transaction;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): The signature covers a single input, without committing to any output;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): The signature applies to a single input and only to the output having the same index as this input.

> ► *A synonym sometimes used for "SigHash" is "Signature Hash Types".*