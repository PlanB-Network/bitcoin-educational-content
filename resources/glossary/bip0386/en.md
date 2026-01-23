---
term: BIP0386
definition: tr() functions for describing Taproot outputs in descriptors.
---

Introduces descriptor functions for Taproot. It defines the functions `tr(KEY)` and `tr(KEY, TREE)` for finding Taproot outputs, where `KEY` is the internal key and `TREE` is an optional script path tree. BIP386 was implemented in Bitcoin Core version 22.0.

