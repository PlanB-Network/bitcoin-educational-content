---
term: sighash_all/sighash_acp
---

Bitcoin 交易簽章中使用的 SigHash Flag (`0x81`)與 `SIGHASH_ANYONECANPAY` 修改器 (`SIGHASH_ACP`)結合的類型。這個組合指定簽章適用於所有輸出，而只適用於交易的特定輸入。`SIGHASH_ALL | SIGHASH_ANYONECANPAY`允許其他參與者在交易的初始簽章之後增加額外的輸入。這在合作性的情境中特別有用，例如集資交易，不同的貢獻者可以加入他們自己的輸入，同時保留初始簽署者承諾的輸出的完整性。