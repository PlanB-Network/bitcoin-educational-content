---
term: 節點
---

在 Bitcoin 網路中，節點（英文稱為「node」）是運行 Bitcoin 通訊協定用戶端的電腦（例如 Bitcoin Core）。它透過維護 Blockchain 的副本、中繼並驗證交易和新區塊，以及選擇性地參與 Mining 流程來參與網路。所有 Bitcoin 節點的總和代表 Bitcoin 網路本身。


Bitcoin 中有幾種節點類型，包括完整節點 (full nodes) 和輕型節點 (light nodes)。全節點保留 Blockchain 的完整副本，根據共識規則驗證所有交易和區塊，並積極參與交易和區塊在整個網路中的傳播。另一方面，light 節點或 SPV (*Simple Payment Verification*) 節點只保留區塊的標頭，並依賴完整節點取得交易資訊。


> ► *有些人也區分所謂的「剪枝節點」（英文為「pruned node」）。這些是完整節點，會從 Genesis 區塊下載並驗證所有區塊，但只在記憶體中保留最近的區塊*。