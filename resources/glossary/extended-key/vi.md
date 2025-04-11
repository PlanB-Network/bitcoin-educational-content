---
term: EXTENDED KEY

---
A sequence of characters that combines a key (public or private), its associated chain code, and a series of metadata. An extended key compiles all the elements necessary for deriving child keys into a single identifier. They are used in deterministic and hierarchical wallets and can be of two types: an extended public key (used to derive child public keys) or an extended private key (used to derive both child private and public keys). An extended key thus includes several different pieces of data, described in BIP32, in the order:


- The prefix: `prv` and `pub` are HRP (Human Readable Part) indicating whether it is an extended private key (`prv`) or an extended public key (`pub`). The first letter of the prefix designates the version of the extended key: `x` for Legacy or SegWit V1 on Bitcoin, `t` for Legacy or SegWit V1 on Bitcoin Testnet, `y` for Nested SegWit on Bitcoin, `u` for Nested SegWit on Bitcoin Testnet, `z` for SegWit V0 on Bitcoin, `v` for SegWit V0 on Bitcoin Testnet.
- The depth, which indicates the number of derivations from the master key to reach the extended key;
- The parent fingerprint. This represents the first 4 bytes of the `HASH160` of the parent public key;
- The index. This is the number of the pair among its siblings from which the extended key is derived;
- The chain code;
- A padding byte if it is a private key `0x00`;
- The private or public key;
- A checksum. It represents the first 4 bytes of the `HASH256` of the rest of the extended key.

In practice, the extended public key is used to generate receiving addresses and to observe the transactions of an account without exposing the associated private keys. This can allow, for example, the creation of a so-called "watch-only" wallet. However, it is important to note that the extended public key is sensitive information for the user's privacy, as its disclosure can allow third parties to trace transactions and see the balance of the associated account.