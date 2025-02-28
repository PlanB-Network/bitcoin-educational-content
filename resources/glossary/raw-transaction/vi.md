---
term: RAW TRANSACTION

---
A Bitcoin transaction that is built and signed, existing in its binary form. A raw transaction (*raw TX*) is the final representation of a transaction, just before it is broadcasted on the network. This transaction contains all the necessary information for its inclusion in a block:


- The version;
- The flag;
- The inputs;
- The outputs;
- The locktime;
- The witness.

What is referred to as a "*raw transaction*" represents the raw data that is passed through the SHA256 hash function twice to generate the transaction's TXID. These data are then used in the block's Merkle tree to integrate the transaction into the blockchain.

> ► *This concept is also sometimes called "Serialized Transaction". In French, these terms could respectively be translated as "transaction brute" and "transaction sérialisée".*