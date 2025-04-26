---
term: MASTER FINGERPRINT

---
A 4-byte (32-bit) fingerprint of the master private key in a Hierarchical Deterministic (HD) wallet. It is obtained by calculating the `SHA256` hash of the master private key, followed by a `RIPEMD160` hash, a process referred to as `HASH160` on Bitcoin. The Master Fingerprint is used to identify an HD wallet, independently of the derivation paths, but taking into account the presence or absence of a passphrase. It is concise information that allows for referencing the origin of a set of keys, without revealing sensitive information about the wallet.