---
term: HASH FUNCTION

---
A mathematical function that takes a variable-size input (called a message) and produces a fixed-size output (called hash, hashing, digest, or fingerprint). Hash functions are widely used primitives in cryptography. They exhibit specific properties that make them suitable for use in secure contexts:


- Preimage resistance: it must be very difficult to find a message that produces a specific hash, i.e., to find a preimage $m$ for a hash $h$ such that $h = H(m)$, where $H$ is the hash function;
- Second preimage resistance: given a message $m_1$, it must be very difficult to find another message $m_2$ (different from $m_1$) such that $H(m_1) = H(m_2)$;
- Collision resistance: it must be very difficult to find two distinct messages $m_1$ and $m_2$ such that $H(m_1) = H(m_2)$;
- Tamper resistance: small changes in the input must cause significant and unpredictable changes in the output.

In the context of Bitcoin, hash functions are used for several purposes, including the proof-of-work mechanism (*Proof-of-Work*), transaction identifiers, address generation, checksum calculations, and the creation of data structures such as Merkle trees. On the protocol side, Bitcoin exclusively uses the `SHA256d` function, also named `HASH256`, which consists of a double `SHA256` hash. `HASH256` is also used in the calculation of certain checksums, notably for extended keys (`xpub`, `xprv`...). On the wallet side, the following are also used:


- Simple `SHA256` for checksums of mnemonic phrases;
- `SHA512` within the `HMAC` and `PBKDF2` algorithms used in the process of deriving deterministic and hierarchical wallets;
- `HASH160`, which describes a successive use of a `SHA256` and a `RIPEMD160`. `HASH160` is used in the process of generating receiving addresses (except P2PK and P2TR) and in calculating parent key fingerprints for extended keys.

> ► *In English, it is referred to as a "hash function".*