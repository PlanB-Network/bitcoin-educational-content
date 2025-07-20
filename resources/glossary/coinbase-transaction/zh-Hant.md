---
term: 代幣大通
---

Coinbase Transaction 是包含在 Bitcoin Blockchain 每個區塊中的特殊且唯一的交易。它代表區塊的第一筆交易，由成功找到驗證 Proof of Work (*Proof-of-Work*) 的標頭（即小於或等於目標）的 Miner 建立。


Coinbase Transaction 主要有兩個目的：將 Block reward 賦予 Miner，並將新單位的比特幣加入流通貨幣 Supply。Block reward 是礦工從事 Proof of Work 的經濟誘因，包括區塊中包含的交易累計費用，以及確定的新創建比特幣前淨值（區塊補貼）。這一數額最初在 2009 年設定為每個區塊 50 比特幣，在稱為 "Halving" 的活動中，每 210,000 個區塊（約每 4 年）減半一次。


Coinbase Transaction 與一般交易有幾個不同之處。首先，它沒有輸入，這意味著它不會消耗現有的交易輸出 (UTXO)。接下來，Coinbase Transaction 的簽章腳本 (`scriptSig`)通常包含一個任意欄位，允許加入額外的資料，例如自訂訊息或 Mining 軟體版本資訊。最後，Coinbase Transaction 產生的比特幣要經過 100 個區塊（101 次確認）的成熟期才能使用，以防止在鏈重組的情況下，可能花掉不存在的比特幣。


> ► *法語中沒有 "Coinbase "的翻譯。因此，直接使用此術語是可以接受的。