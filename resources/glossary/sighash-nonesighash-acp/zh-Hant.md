---
term: sighash_none/sighash_acp
---

Bitcoin 交易簽章中使用的 SigHash Flag (`0x82`)與 `SIGHASH_ANYONECANPAY` 修改器 (`SIGHASH_ACP`)結合的類型。這個組合表示簽章只適用於特定的輸入，而不承諾任何輸出。這允許其他參與者自由地增加額外的輸入，並修改所有交易的輸出。