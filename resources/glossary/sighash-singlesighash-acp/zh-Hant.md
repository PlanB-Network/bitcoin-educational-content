---
term: sighash_single/sighash_acp
---

Bitcoin 交易簽章中使用的 SigHash Flag (`0x83`)與 `SIGHASH_ANYONECANPAY` 修改器 (`SIGHASH_ACP`)結合的類型。這個組合指定簽章只適用於特定的單一輸入，並且只適用於與此輸入有相同索引的輸出。其他方可以添加或修改其他輸入和輸出。此組態對於合作式交易非常有用，參與者可以加入自己的輸入來資助特定的輸出。