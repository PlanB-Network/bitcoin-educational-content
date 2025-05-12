---
term: BIP
---

Bitcoin Improvement Proposal（Bitcoin 改善提案）的縮寫。Bitcoin 改善提案 (BIP) 是對 Bitcoin 協定及其標準提出改善和變更建議並加以記錄的正式流程。由於 Bitcoin 沒有一個中央實體來決定更新，BIP 允許社群以結構化和透明的方式提出、討論和實施改進。每個 BIP 詳細說明了建議改進的目標、理由、對相容性的潛在影響，以及優點和缺點。BIP 可以由社群中的任何成員撰寫，但必須經過其他開發人員和維護 Bitcoin Core GitHub 資料庫的編輯核准：Bryan Bishop、Jon Atack、Luke Dashjr、Mark Erhardt (Murch)、Olaoluwa Osuntokun 和 Ruben Somsen。然而，重要的是要了解這些人在編輯 BIP 中的角色並不表示他們控制了 Bitcoin。如果有人提出的改進建議未被正式的 BIP 架構所接受，他們仍然可以直接將其提交給 Bitcoin 社群，甚至創建包含其修改的 Fork。BIP 程序的優點在於它的正式性和集中性，這有助於爭論，避免 Bitcoin 使用者之間的分裂，尋求以一致同意的方式實現更新。歸根結柢，是經濟大多數原則決定了協定內的權力動態。


BIP 分為三大類：


- 標準軌道 BIP*：與直接影響 Bitcoin 實作的修改有關，例如交易和區塊驗證規則；
- 資訊性 BIP*：提供資訊或建議，但不建議直接變更規程；
- 流程 BIP*：說明 Bitcoin 相關程序的變更，例如治理程序。


標準軌跡和資訊性 BIP 也以 "Layer "分類：


- 共識 Layer*：此 Layer 中的 BIP 涉及 Bitcoin 的共識規則，例如區塊或交易驗證規則的修改。這些提案可以是 Soft 分叉 (向後相容的修改) 或 Hard 分叉 (非向後相容的修改)。例如，SegWit 和 Taproot 的 BIP 就屬於這一類；
- 對等服務*：此 Layer 關係到 Bitcoin 節點網路的運作，也就是節點如何在網際網路上相互尋找與通訊。
- API/RPC*：此 Layer 的 BIP 關係到應用程式介面 (API) 和遠端程序呼叫 (RPC)，可讓 Bitcoin 軟體與節點互動；
- 應用程式 Layer*：此 Layer 與建立在 Bitcoin 之上的應用程式有關。此類別中的 BIP 通常處理 Bitcoin Wallet 標準層級的修改。


提交 BIP 的流程是先在 *Bitcoin-dev* 郵件列表上構思並討論想法。如果想法很有前途，作者就會依照特定格式起草 BIP，並透過核心 GitHub 套件庫上的 Pull Request 提交。編輯會審閱此提案，確認其符合所有標準。BIP 必須在技術上可行、對協定有益、符合規定的格式，並與 Bitcoin 的理念一致。如果 BIP 符合這些條件，它就會被正式整合到 BIP 的 GitHub 儲存庫中。然後，它會被分配一個編號。編號通常由編輯（通常是 Luke Dashjr）決定，並依邏輯分配：處理類似主題的 BIP 通常會獲得連續編號。


BIP 在其生命週期中會經歷不同的狀態。目前的狀態會在每個 BIP 的標頭中指定：


- 草案：提案仍在起草和辯論階段；
- 建議：BIP 被認為是完整的，並可供社區審核；
- 擱置：BIP 由冠軍或編輯暫緩處理；
- 拒絕：如果 BIP 在 3 年內沒有任何活動，則會被歸類為已拒絕。其作者可選擇稍後恢復，使其恢復草案狀態；
- 撤回：BIP 已由作者撤回；
- 最後：BIP 在 Bitcoin 上被接受並廣泛實施；
- 活躍：僅針對製程 BIP，一旦達成某種共識，即會指定此狀態；
- 已取代/過時：BIP 已不再適用，或已被較新的提案取代，使其不再需要。


![](../../dictionnaire/assets/25.webp)


> ► *BIP是「Bitcoin改善提案」的縮寫。在法文中，可翻譯為 "Proposition d'amélioration de Bitcoin"。然而，大多數法語文本直接將縮寫 "BIP "用作普通名詞，有時是女性名詞，有時是男性名詞*。