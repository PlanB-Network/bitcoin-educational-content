---
term: BIP0085
definition: Method allowing several mnemonic phrases for different wallets to be derived from a single master seed.
---

BIP85 provides a solution to unify the derivation of multiple Bitcoin wallets using a single master seed.
It enables deriving entropy from a root key to generate multiple mnemonic phrases for different wallets, all without compromising security.
The goal of BIP85 is to facilitate the management and backup of multiple Bitcoin wallets: instead of securing several different mnemonic phrases, one root seed is sufficient to derive them all.