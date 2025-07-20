---
term: BIP0113
---

對所有時間鎖操作 (`nLockTime`、`OP_CHECKLOCKTIMEVERIFY`、`nSequence` 及 `OP_CHECKSEQUENCEVERIFY`)的計算方式做了修改。它規定要評估時間鎖的有效性，現在必須將它們與 MTP (*Median Time Past*) 比較，MTP 是最近 11 個區塊的時間戳記的中位數值。以前，只使用前一個區塊的 Timestamp。此方法讓系統更具可預測性，並防止礦工操控時間參考。BIP113 於 2016 年 7 月 4 日透過 Soft Fork 推出，與 BIP68 和 BIP112 並列，首次使用 BIP9 方法啟用。