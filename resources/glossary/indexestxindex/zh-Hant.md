---
term: 索引/txindex/
---

Bitcoin Core 中的檔案專門用於索引 Blockchain 中的所有交易。此索引允許使用交易的識別碼 (txid) 快速搜尋交易的詳細資訊，而無需檢視整個 Blockchain。在 Bitcoin Core 中，創建這些索引檔案是一個預設未啟用的選項。如果未啟用此功能，您的節點將僅索引與附加到您節點的錢包相關的交易。若要啟用所有交易的索引，您必須在 `Bitcoin.conf` 檔案中設定參數 `-txindex=1`。此選項對於經常搜尋 Bitcoin 交易歷史的應用程式和服務特別有用。