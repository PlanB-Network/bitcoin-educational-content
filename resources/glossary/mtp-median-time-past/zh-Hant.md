---
term: mtp（過去中位時間）
---

此概念用於 Bitcoin 協定，以確定網路共識 Timestamp 的邊際。MTP 定義為最近 11 個挖掘區塊時間戳記的中值。使用此指標有助於避免節點間對於精確時間出現歧異時的分歧。MTP 最初用於驗證區塊時間戳是否與過去相符。自 BIP113 起，它也被用作網路時間的參考，以驗證時間鎖定交易的有效性 (`nLockTime`、`OP_CHECKLOCKTIMEVERIFY`、`nSequence` 和 `OP_CHECKSEQUENCEVERIFY`)。