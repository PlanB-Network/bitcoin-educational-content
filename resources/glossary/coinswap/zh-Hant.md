---
term: COINSWAP
---

用戶之間秘密轉移 Ownership 的協定。此方法旨在將擁有的比特幣從一個人轉移至另一個人，反之亦然，而此 Exchange 並未在 Blockchain 上明顯可見。Coinwap 使用智慧契約來進行轉移，而不需要雙方之間的信任。


讓我們想像一個天真的例子 (這並不可行)，Alice 和 Bob。Alice 持有 1 個以私人密碼匙 $A$ 加密的 BTC，Bob 也持有 1 個以私人密碼匙 $B$ 加密的 BTC。理論上，他們可以透過外部通訊管道 Exchange 他們的私人密碼匙來進行秘密轉移。然而，這種天真的方法在信任方面有很高的風險。沒有任何東西可以防止 Alice 在 Exchange 之後保留一份 $A$ 私密金鑰的副本，並在金鑰到了 Bob 手中之後，用它來竊取比特幣。更重要的是，在 Exchange 中無法保證 Alice 不會收到 Bob 的私密金鑰 $B$ 而永遠不會傳遞她的私密金鑰 $A$。因此，這個 Exchange 依賴雙方之間過度的信任，無法有效確保 Ownership 的安全、秘密傳輸。


為了解決這些問題，並讓互不信任的雙方能夠換幣，我們要使用 Smart contract 系統，讓 Exchange 成為「原子」。這些可以是 HTLC (*Hash Time-Locked Contracts*) 或 PTLC (*Point Time-Locked Contracts*)。這兩種通訊協定的運作方式類似，使用時間鎖定系統，確保 Exchange 成功完成或完全取消，從而保護雙方資金的完整性。HTLC 和 PTLC 的主要差異在於 HTLC 使用哈希值和預先影像來確保交易安全，而 PTLC 則使用 Adaptor Signatures。


在 Alice 和 Bob 之間使用 HTLC 或 PTLC 進行交換硬幣的情況下，Exchange 會以安全的方式進行：要不成功，雙方都會收到對方的 BTC，要不失敗，雙方都會保留自己的 BTC。這使得任何一方都無法欺騙或竊取對方的 BTC。


在此情況下，適配器簽章的使用尤其有趣，因為它使免除傳統腳本成為可能（這種機制有時被稱為"_scriptless scripts_"）。這可降低與 Exchange 相關的成本。適配器簽章的另一大優點是不需要交易雙方使用共同的 Hash，從而避免了在某些類型的 Exchange 中揭示雙方之間的直接聯繫。