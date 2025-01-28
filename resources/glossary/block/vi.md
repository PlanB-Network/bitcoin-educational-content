---
term: BLOCK

---
Data structure in the Bitcoin system. A block contains a set of valid transactions and metadata contained in its header. Each block is linked to the next by the hash of its header, thus forming the blockchain. The blockchain acts as a timestamping server that allows every user to know all past transactions, in order to verify the non-existence of a transaction and prevent double spending. Transactions are organized in a Merkle tree. This cryptographic accumulator allows for the production of a digest of all the transactions in a block, called the "Merkle root." The header of a block contains 6 elements:


- The version of the block;
- The imprint of the previous block;
- The root of the Merkle tree of transactions;
- The timestamp of the block;
- The difficulty target;
- The nonce.

For a block to be valid, it must have a header that, once hashed with `SHA256d`, produces a digest that is less than or equal to the difficulty target.