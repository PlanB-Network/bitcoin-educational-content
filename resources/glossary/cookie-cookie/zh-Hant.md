---
term: cookie (.cookie)
---

在 Bitcoin Core 中用於 RPC（*遠端程序呼叫*）驗證的檔案。當 bitcoind 啟動時，會產生一個唯一的驗證 cookie 並儲存在此檔案中。希望透過 RPC Interface 與 bitcoind 互動的用戶端或腳本可以使用此 cookie 進行安全驗證。這種機制允許 bitcoind 與外部應用程式（例如 Wallet 軟體）之間進行安全通訊，而不需要手動管理使用者名稱和密碼。每次重新啟動 bitcoind 時，`.cookie`檔會重新產生，關機時則會刪除。