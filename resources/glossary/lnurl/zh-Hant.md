---
term: LNURL
---

通訊協定，指定了一系列功能，旨在簡化Lightning節點和客戶端以及第三方應用程式之間的互動。此協定基於HTTP，可為各種操作創建鏈結，如付款請求、提款請求或其他增強用戶體驗的功能。每個 LNURL 都是以 bech32 編碼的 URL，前綴為 `lnurl`，當掃描此 URL 時，會觸發 Lightning Wallet 上的一系列自動動作。


例如，LNURL-withdraw (LUD-03) 可讓您透過掃描 QR 代碼從服務中提取資金，而無需手動 generate 和 Invoice。或 LNURL-auth (LUD-04) 可讓您使用 Lightning Wallet 上的私人密碼匙而非密碼連線至線上服務。