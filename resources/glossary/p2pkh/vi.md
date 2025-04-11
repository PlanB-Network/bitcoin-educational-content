---
term: P2PKH

---
P2PKH stands for *Pay to Public Key Hash*. It is a standard script model used to establish spending conditions on a UTXO. It allows for locking bitcoins on a hash of a public key, that is, on a receiving address. This script is associated with the Legacy standard and was introduced in the early versions of Bitcoin by Satoshi Nakamoto.

Unlike P2PK, where the public key is explicitly included in the script, P2PKH uses a cryptographic fingerprint of the public key. This script includes the `RIPEMD160` hash of the `SHA256` of the public key and stipulates that, to access the funds, the recipient must provide a public key that matches this hash, as well as a valid digital signature generated from the associated private key. P2PKH addresses are encoded using the `Base58Check` format, which gives them robustness against typographical errors through the use of a checksum. These addresses always start with the number `1`.