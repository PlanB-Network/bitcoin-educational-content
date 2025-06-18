---
term: BIP0093
---

Informational BIP that suggests a standard for saving and restoring the seed of a hierarchical deterministic portfolio (according to BIP32) using Shamir's Secret Key Sharing. This protocol defines the "codex32" format, which is inspired by the bech32 format, by introducing a structured string consisting of a prefix, a threshold parameter, an identifier, a sharing index, a payload and a checksum (BCH). The method allows the seed to be split into up to 31 shares, of which a defined threshold (between 1 and 9) is required for full seed recovery.