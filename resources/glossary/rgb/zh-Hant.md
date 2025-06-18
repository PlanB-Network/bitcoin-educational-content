---
term: RGB
---

分散、保密的 Smart contract 系統，設計與 Bitcoin 和 Lightning Network 搭配使用。RGB 以 Client-side Validation 模式運作，並將 Contract State 的儲存空間與 Blockchain 分離，因此其上只保留加密承諾。如此一來，完整的狀態歷史就保留在連鎖之外，使其具有更高的擴充性和機密性。因此，RGB 可直接在 Bitcoin 上建立複雜的合約，以儲存代用幣、NFT、分散式身分或 DeFi 解決方案。


在 RGB 上，使用 Single-Use Seal 可確保對 Double-spending 的抵抗力，Single-Use Seal 是一種加密機制，可利用 Bitcoin 上的 UTXO 只能使用一次的事實。至於令牌的真實性，則透過用戶端驗證狀態歷史（從 Contract 建立到其最新狀態）來保證。