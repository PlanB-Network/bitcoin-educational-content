---
term: Wallet import format (WIF)
definition: Base58Check encoding method for a Bitcoin private key to facilitate its import or export between wallets.
---

A method for encoding a Bitcoin private key in a way that it can be imported or exported more easily between different wallets. The WIF is based on `Base58Check` encoding, which includes information about the version, the compression of the corresponding public key, and a checksum for error detection in typing. A WIF private key starts with the characters `5` for uncompressed keys, or `K` and `L` for compressed keys, and contains all the characters necessary to reconstruct the original private key. The WIF format provides a standardized means to transfer a private key between different wallet software.