---
term: BIP0093
definition: Codex32 standard allowing a seed to be backed up by splitting it into several parts via Shamir's secret sharing.
---

Informational BIP that suggests a standard for saving and restoring the seed of a hierarchical deterministic wallet (according to BIP32) using Shamir's Secret Sharing.

The protocol defines the “codex32” format, inspired by bech32, which introduces a structured string composed of:
- a prefix,
- a threshold parameter,
- an identifier,
- a share index,
- a payload, and
- a checksum (BCH).

The method allows the seed to be split into up to 31 shares, of which a defined threshold (between 1 and 9) is required for full seed recovery.