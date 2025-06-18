---
term: 原始交易
---

已建立並簽署的 Bitcoin 交易，以二進位形式存在。原始交易 (*raw TX*) 是交易在網路中廣播之前的最終表示形式。此交易包含將其納入區塊的所有必要資訊：


- 版本；
- 旗幟
- 輸入；
- 輸出；
- 鎖定時間
- 證人


所謂「*原始交易*」是指原始資料經過 SHA256 Hash 函式兩次傳送至交易的 txid 的 generate。這些資料隨後會用在區塊的 Merkle Tree 中，將交易整合到 Blockchain 中。


> ► *此概念有時也稱為「序列化交易」。在法文中，這些詞彙可分別翻譯為「transaction brute」和「transaction sérialisée」*。