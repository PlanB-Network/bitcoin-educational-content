---
term: EXTRA-Nonce
---

用於區塊 Coinbase Transaction 的 `scriptSig` 中的欄位，除了直接在每個區塊的標頭中找到的經典 Nonce 外，它允許測試更多的可能性，以便 Hash 低於難度目標。


修改 Coinbase Transaction 中的額外 Nonce 會改變此交易的識別碼，因此也會改變區塊中所有交易的 Merkle Root，這也會修改區塊標頭。這可讓 Miner 在經典 Nonce 的範圍已經用盡時，繼續搜尋切細值，而不會改變其候選區塊的結構。


在 Mining 池中，extra-Nonce 通常分為兩部分：一部分由池產生以識別每個切換器，另一部分則由切換器在尋找有效共享時修改。這可讓池中不同的切換器同時以整個 nonces 範圍處理相同的候選區塊，而不會在池層級重複相同的工作。