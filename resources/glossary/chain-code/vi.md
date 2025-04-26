---
term: CHAIN CODE

---
In the context of hierarchical deterministic (HD) derivation of Bitcoin wallets, the chain code is a 256-bit cryptographic salt value used to generate child keys from a parent key, according to the BIP32 standard. The chain code is used in combination with the parent key and the child's index to deterministically generate a new pair of keys (private key and public key) without revealing the parent key or other derived child keys.

Therefore, there is a unique chain code for each pair of keys. The chain code is obtained either by hashing the wallet's seed and taking the right half of the bits. In this case, it is referred to as a master chain code, associated with the master private key. Alternatively, it can be obtained by hashing a parent key with its parent chain code and an index, then keeping the right bits. This is then referred to as a child chain code.

It is impossible to derive keys without knowing the chain code associated with each parent pair. It introduces pseudo-random data into the derivation process to ensure that the generation of cryptographic keys remains unpredictable to attackers while being deterministic for the wallet holder.

> ► *In English, a "code de chaîne" is called a "chain code", and a "code de chaîne maître" is called a "master chain code".*