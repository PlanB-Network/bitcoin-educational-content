---
term: sighash_all (0x01)
---

在 Bitcoin 交易簽章中使用的 SigHash Flag 種類，表示簽章適用於交易的所有元件。透過使用 `SIGHASH_ALL`，簽章者涵蓋了所有的輸入和所有的輸出。這表示在簽章之後，輸入或輸出都不能被修改而不會失效。這種類型的 SigHash Flag 在 Bitcoin 交易中是最常見的，因為它可以確保交易的完全最終性及完整性。