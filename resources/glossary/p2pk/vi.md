---
term: P2PK

---
P2PK stands for *Pay to Public Key*. It is a standard script model used on Bitcoin to establish spending conditions on a UTXO. It allows for locking bitcoins directly onto a public key, rather than an address.

Technically, the P2PK script contains a public key and an instruction that demands a corresponding digital signature to unlock the funds. When the owner wishes to spend the bitcoins, they must provide a signature produced with the associated private key. This signature is verified using the ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK was often used in the early versions of Bitcoin, notably by Satoshi Nakamoto. It is almost no longer used today.