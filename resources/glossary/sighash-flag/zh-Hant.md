---
term: SIGHASH 旗幟
---

Bitcoin 交易中的一個參數，它決定交易的哪些元件（輸入和輸出）被相關簽章所涵蓋，從而成為不可變的。SigHash Flag 是添加到每個輸入的數位簽章中的一個位元組。因此，SigHash Flag 的選擇會直接影響交易的哪些部分會被簽章凍結，哪些部分之後仍可修改。此機制可確保簽章依據簽章者的意圖，精確且安全地提交交易資料。主要有三種 SigHash Flag：



- `SIGHASH_ALL` (`0x01`)：簽章適用於交易的所有輸入和輸出，因此完全鎖定它們；



- `SIGHASH_NONE` (`0x02`)：簽章適用於所有輸入，但不適用於所有輸出，允許在簽章之後修改輸出；



- `SIGHASH_SINGLE` (`0x03`)：簽章涵蓋所有輸入，只有一個輸出對應於簽章輸入的索引。


除了這三種 SigHash Flags 之外，修改器 `SIGHASH_ANYONECANPAY` (`0x80`)可以與前面的每一種類型結合。使用此修改器時，只有部分輸入是有符號的，其他部分則可修改。以下是使用修改器的現有組合：



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`)：簽章適用於單一輸入，同時涵蓋交易的所有輸出；



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`)：簽章涵蓋單一輸入，不承諾任何輸出；



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`)：簽章適用於單一輸入，且僅適用於與此輸入具有相同索引的輸出。


> ► *「SigHash」有時使用的同義詞是「Signature Hash Types」。