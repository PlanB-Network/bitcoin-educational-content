---
term: SETTINGS.JSON
---

Bitcoin Core 中用來儲存圖形使用者 Interface (GUI) 設定的檔案。它保留了用戶配置的相關資訊，例如打開的錢包。當 Bitcoin Core 重新啟動時，此檔案可自動重新開啟應用程式關閉前啟用的錢包。如果 Wallet 透過 GUI 關閉，也會從此檔案中移除，因此下次啟動時不會自動重新開啟。