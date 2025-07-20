---
term: 迷你劇本
---

框架，旨在提供一個在 Bitcoin 上安全編寫腳本的框架。Bitcoin 的母語稱為 script。它在實際使用上相當複雜，尤其是複雜的客製化應用程式。最重要的是，它很難驗證腳本的限制。Miniscript 使用 Bitcoin 腳本的子集來簡化腳本的建立、分析和驗證。每個 Miniscript 都與原生腳本一一對等。使用方便使用者的政策語言，然後將其編譯為 miniscript，最後與原生腳本對應。


![](../../dictionnaire/assets/30.webp)


因此，Miniscript 允許開發人員以更安全、更可靠的方式建立複雜的腳本。Miniscript 的基本特性如下：


- 它允許對腳本進行靜態分析，包括它允許的支出條件及其在資源方面的成本；
- 它可以創建遵守共識的腳本；
- 它允許分析不同的支出路徑是否符合節點的標準規則；
- 它為所有 Wallet 軟硬體建立了可理解且可組合的一般標準。


Miniscript 專案由 Peter Wuille、Andrew Poelstra 和 Sanket Kanjalkar 於 2018 年透過 Blockstream 公司推出。Miniscript 在 2022 年 12 月的版本 24.0 中以僅供觀看的模式加入 Bitcoin Core Wallet，然後在 2023 年 5 月的版本 25.0 中完全加入。