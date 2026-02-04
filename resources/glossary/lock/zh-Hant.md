---
term: 鎖定 (.lock)
definition: 防止多個Bitcoin Core實例同時訪問同一個目錄的文件。
---

Bitcoin Core 中用於鎖定資料目錄的檔案。它在 bitcoind 或 Bitcoin-qt 啟動時建立，以防止軟體的多個實體同時存取相同的資料目錄。目的是防止衝突和資料損毀。如果軟體意外停止，.lock 檔案可能會保留，必須在重新啟動 Bitcoin Core 之前手動刪除。