---
term: SIGHASH_ANYPREVOUT

---
Proposal for the implementation of a new SigHash Flag modifier in Bitcoin, introduced with BIP118. `SIGHASH_ANYPREVOUT` allows for greater flexibility in transaction management, especially for advanced applications like payment channels on the Lightning Network and the Eltoo update. The `SIGHASH_ANYPREVOUT` enables the signature not to be tied to any specific previous UTXO (*Any Previous Output*). Used in combination with `SIGHASH_ALL`, it would allow signing all the outputs of a transaction, but none of the inputs. This would enable the reuse of the signature for different transactions, as long as certain specified conditions are met.

> ► *This SigHash modifier SIGHASH_ANYPREVOUT is derived from the idea of SIGHASH_NOINPUT initially proposed by Joseph Poon in 2016 to enhance his concept of the Lightning Network.*