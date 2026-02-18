---
term: BIP0386

definition: Các hàm tr() để mô tả các đầu ra Taproot trong các descriptor.
---
Introduces descriptor functions for Taproot. It defines the functions `tr(KEY)` and `tr(KEY, TREE)` for finding Taproot outputs, where `KEY` is the internal key and `TREE` is an optional tree of script paths. BIP386 was implemented in Bitcoin Core version 22.0.