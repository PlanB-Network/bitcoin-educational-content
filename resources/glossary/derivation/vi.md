---
term: DERIVATION

---
Refers to the process of generating child key pairs from a parent key pair (private key and public key) and a chain code within a deterministic and hierarchical (HD) wallet. This process allows for the segmentation of branches and the organization of a wallet into different levels with numerous child key pairs, which can all be recovered by knowing only the basic recovery information (the mnemonic phrase and any potential passphrase). To derive a child key, the `HMAC-SHA512` function is used with the parent chain code and the concatenation of the parent key and a 32-bit index. There are two types of derivations:


- Normal derivation, which uses the parent public key as the basis of the `HMAC-SHA512` function;
- Hardened derivation, which uses the parent private key as the basis of the `HMAC-SHA512` function;

The result of HMAC-SHA512 is divided into two: the first 256 bits become the child key (private or public after processing through ECDSA), and the remaining 256 bits become the child chain code.