---
name: Zeus Swap
description: On-Chain 和 Lightning Network 比特幣之間的非監護 Exchange 服務
---

![cover](assets/cover.webp)



Bitcoin 生態系統呈現了二元性：主網路 (On-Chain) 提供最大的安全性，而 Lightning Network 則可進行即時交易。這種兩層 Layer 架構造成了一個實際的挑戰：如何在沒有中央中介的情況下，在這兩層之間有效率地轉移資金？



問題很具體：您收到一筆 Lightning 付款，但希望將其保存在 Cold 儲存空間中；或者相反，您擁有 On-Chain 比特幣，但需要 Lightning 流動資金。傳統的解決方案涉及手動開啟/關閉 Lightning 通道（成本高且技術性強）或需要 KYC 的集中式平台。



Zeus Swap 透過自動化、非監管的 Exchange 服務解決了這個問題。它由 Zeus LSP 開發，可讓您將 On-Chain 比特幣雙向轉換為 Lightning Satoshis，而無需將資金委託給中介。這個過程使用原子契約 (HTLC) 保證 Exchange 會完成或取消。



創新之處在於其簡易性：只需點選幾下，即可獲得 Exchange，保留您的財務主權，無需註冊或 KYC。



## 什麼是 Zeus Swap？



Zeus Swap 是 Zeus LSP 開發的流動性 Exchange 服務，可在 Bitcoin 主網路和 Lightning Network 之間進行原子交換。它是一種技術基礎設施，利用海底掉期和反向掉期促進 On-Chain BTC 和 Lightning Satoshis 之間的雙向兌換，同時保留操作的非保管性。



### 技術架構



Zeus Swap 使用 Boltz 的開放原始碼 Bitcoin/Lightning 原子交換技術。該協定使用 Hash 時間鎖定合約 (HTLC)：鎖定資金的合約有兩種釋放條件（揭露密碼秘密或時間到期）。



對於海底交換 (On-Chain → Lightning)，使用者將比特幣傳送至結合 Lightning Invoice 的 Hash 的 Address。Zeus LSP 只會透過支付對應的 Invoice，揭示自動解鎖比特幣的預映像來解鎖這些資金。這種機制保證了原子性。



對於反向交換 (Lightning → On-Chain)，使用者支付 Zeus LSP 的 Lightning Invoice，顯示預先影像，使準備好的 Bitcoin 交易能釋放至目的地 Address。



有關 Lightning Network 如何運作的詳細資訊，請參閱我們的專用課程 ：



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### 商業模式



Zeus LSP 擔任市場莊家，維持 On-Chain 和 Lightning 的流動性以承兌掉期。對於掉期交易，Zeus 會收取可變費用（通常為 0.1% 至 0.5%，視方向和條件而定），再加上 Bitcoin 的 Mining 費用，並在驗證前透明顯示。



身為 Lightning Service Provider，Zeus 憑藉其在隨選通道開通、高效路由和客製化流動性解決方案方面的專業知識，優化了成本。



### 整合



Zeus Wallet 原生整合了該服務，無需離開 Interface Bitcoin/Lightning 即可實現交換。這消除了在應用程式之間複製和粘貼的摩擦。



獨立的 Interface 網路仍可存取所有錢包，保證最大的使用彈性。



## 主要功能



### 雙向交換



Zeus Swap 提供兩種類型的 Exchange：



**Submarine swaps (On-Chain → Lightning)**：從您的 Bitcoin 儲備注入 Lightning 流動資金，對於供給行動 Wallet 或 Lightning 節點而不需手動開啟通道非常有用。



**Reverse swaps (Lightning → On-Chain)**：將 Lightning Satoshis 轉換成 On-Chain bitcoins 長期儲存，避免代價高昂的通道關閉。



### 使用者介面



**Interface web** (swaps.zeuslsp.com)：簡化的體驗，無需註冊，有即時顯示費用和狀態的導覽流程。



**Zeus Wallet 整合**：從應用程式直接交換，自動管理發票和地址，消除處理錯誤。



### 安全與復原



每次交換都會產生唯一的 Contract，其參數不可變：Hash Lightning、超時、退款 Address。若發生故障，可透過提供的 Address 自動恢復，與 Zeus LSP 無關。



**Zeus Swaps Rescue Key**：在 On-Chain → Lightning 交換期間，Zeus 會自動產生一個通用的復原金鑰，取代舊的個別退款檔案。此獨特的金鑰可在任何裝置上使用，並適用於用其建立的所有交換。請務必下載此金鑰並保存在安全的位置，以便在交換失敗時恢復您的資金。



### 網路最佳化



Zeus Swap 可根據網路條件自動調整到期時間和 Mining 費用。Zeus 用戶可從進階選項中獲益：選擇 LSP、自訂延遲、與其他服務相容 (Boltz)。



## 安裝與使用



### 存取方法



**Interface web** (swaps.zeuslsp.com)：與所有錢包相容的通用解決方案，無需安裝，適合偶爾使用。



**Zeus 應用程式** (iOS/Android)：結合 Wallet 與交換的整合體驗，適合一般使用者使用。



請參閱我們的 Zeus 教學，瞭解更多關於這個完整的 Wallet ：



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### 網頁設定



**On-Chain → Lightning**：此過程會先在 Interface web Zeus Swap 上設定交換。使用者可以使用 On-Chain 和 Lightning 欄位之間的箭頭來反轉交換的方向。



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap：金額選擇 (Sats 50,000 → Sats 49,648 費用後)，透明顯示網路費用 (Sats 302) 和 Zeus 服務 (Sats 50)。



在此過程中，Zeus 會提供您下載通用復原密鑰：



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Zeus Swaps 救援金鑰的下載對話方塊 - 可取代舊有個別報銷檔案的通用金鑰*。



如果您已經擁有金鑰，Zeus 允許您檢查金鑰：



![Vérification de la clé existante](assets/fr/03.webp)



*Interface 檢查現有 Zeus Swaps 救援金鑰*的有效性



設定完成後，Zeus 會產生 Bitcoin 車廠 Address 並顯示說明 ：



![Adresse de dépôt et instructions](assets/fr/04.webp)



*交換完成頁面：QR 代碼和 Bitcoin Address 用於發送 50,000 Satss，並提醒 24 小時有效日期*



然後，交換等待 Bitcoin 確認：



![Attente de confirmation](assets/fr/05.webp)



*狀態「Mempool 中的交易」- 等待 Bitcoin 確認以完成交換*



一旦確認，交換就會自動完成：



![Swap réussi](assets/fr/06.webp)



*確認成功：扣除網路和服務費用後，Lightning 收到 49,648 Sats*



### 使用 Zeus 應用程式



**Lightning → On-Chain**：Zeus 應用程式提供反向掉期的整合體驗 (Lightning 至 Bitcoin)。



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Zeus 主螢幕顯示 Lightning (69,851 Sats) 和 On-Chain (38,018 Sats) 的餘額，可透過側邊選單存取交換*。



![Configuration du swap reverse](assets/fr/08.webp)



*Interface 反向交換建立：50,000 Sats Lightning → 49,220 Sats On-Chain，清楚顯示網路費用 (530 Sats) 和服務 (250 Sats)。使用者可以手動輸入一個 Bitcoin 接收 Address，或透過「generate On-Chain Address」按鈕自動從 Wallet Zeus 輸入一個 generate。



![Finalisation du swap mobile](assets/fr/09.webp)



*最終完成畫面：閃電 Invoice 付款畫面，包含「PAY THIS Invoice」、9.96 秒的閃電付款成功確認，以及 49,162 張等待確認的 Sats 結餘報表*。



### 監控與安全



每個交換都有唯一的識別碼，可即時追蹤。完整的進度顯示，到期日自動提醒。根據網路狀況自動提出充電建議。



## 優點與限制



### 優點





- 簡單**：只需點擊幾下就可對換，無需手動操作通道
- 非保管**：無需 KYC、無帳戶、資金從未託付給第三方
- 透明度**：在驗證前明確顯示費用（0.1% 到 0.5% + minage 取決於使用者測試 - 在每次交換時查看當前費用）
- 行動整合**：Zeus Wallet 中的原生體驗



### 限制條件





- 失效時間**：最長 24-48 小時，若 Bitcoin 未及時確認則失效
- 金額限制**：最低 25,000 Sats，Zeus LSP 流動性依條件不定
- 追蹤 On-Chain**：透過 Blockchain 分析可能識別的 HTLC 指令碼
- 需要確認**：Bitcoin 驗證需時至少 10 分鐘



## 最佳實踐



### 時間與成本





- 請注意 Mempool.space 的低壅塞時段
- 偏好週末和非繁忙時間，以降低 Mining 成本
- 計算獲利能力：小額相對於直接開啟通路



### 安全性





- 仔細檢查 Bitcoin 位址（建議複製貼上）
- 備份 Zeus Swaps 救援金鑰**：下載救援金鑰並將其儲存於安全的地方
- 文件：Contract ID、退款 Address、有效日期
- 使用適當的 Mining 費用進行及時確認



### 使用策略





- 平衡 On-Chain/Lightning 流動性以符合您的需求
- Zeus Swap 用於一次性調整，直接渠道用於永久需求



## 與其他交換服務的比較



### Zeus Swap vs Boltz Exchange



Zeus Swap 使用 Boltz 的後端技術，但做了一些重要的改進：



**Zeus Swap 優惠** ：




- Interface 統一**：Zeus 中的本機整合 Wallet vs Interface 網路技術 Boltz
- WebSocket API**：即時更新 vs. 手動輪詢
- 自動管理**：自動帳單和 Address 管理
- 行動支援**：僅針對智慧型手機與桌上型電腦進行最佳化
- Swagger 文件**：供開發人員使用的完整 REST API



**Boltz 依舊具有優勢**，可完全獨立使用任何 Bitcoin/Lightning 設定。



Zeus Swap 將經過驗證的 Boltz 技術轉換為主流使用者體驗，相當於原始通訊協定與使用者友善應用程式之間的差異。



### Zeus Swap vs Phoenix/Breez (整合交換)



Phoenix 和 Breez 整合了透明的交換功能，向終端使用者隱藏了技術上的複雜性。Phoenix 使用自動換入/換出系統，用戶不需要明確區分 Bitcoin 層：他 「發送至 Bitcoin Address」，應用程式在後台處理交換。



這種極度簡化的方式非常適合初學者，但卻限制了對操作的理解和控制。Zeus Swap 採用了更具教育性的哲學：使用者了解他們是在兩個不同的層之間進行交換，逐步培養他們對兩個-Layer Bitcoin 生態系統的了解。



## 費用和限額的詳細比較 (2024)



⚠️ **警告**：根據市場狀況和服務更新，費用可能會隨時間改變。在驗證交換之前，請務必檢查 Interface 中顯示的費用。




| 服務 | 潛水艇互換 (BTC→LN) | 逆向互換 (LN→BTC) | 最低金額 |
| ------------- | ----------------------- | --------------------- | --------------- |
| **Zeus Swap** | ~0.1% + 挖礦費用 | 0.5% + 挖礦費用 | 25,000 sats |
| **Boltz** | 0.2% + 挖礦費用 | 0.5% + 挖礦費用 | 50,000 sats |
| **Phoenix** | 僅挖礦費用 | 0.4% 固定 | 10,000 sats |
| **Breez** | 0.25% + 網路費用 | 0.5% + 挖礦費用 | 50,000 sats |

Zeus Swap 在易用性和技術控制之間取得了平衡：比 Boltz 更容易上手，比 Phoenix/Breez 更靈活，採用嚴格的非監控方式。



## 總結



Zeus Swap 代表了 Bitcoin 生態系統的重大創新，優雅地解決了主網路與 Lightning Network 之間互通性的挑戰。這項服務結合了原子交換的加密穩健性與易於使用的使用者體驗，使 Bitcoin 雙 Layer 管理民主化，同時又不損害金融主權的原則。



Zeus Swap 的非監護架構承襲自成熟的 Boltz 技術，可確保您的資金在整個交換過程中由您專屬控制。這種方法尊重 Bitcoin 的精神，同時提供主流採用所需的使用者便利性。價格透明化和 KYC 流程的缺失強化了這一獨特的價值主張。



對於現代的 Bitcoin 使用者而言，Zeus Swap 是根據需求優化流動資金分配的策略工具：On-Chain 安全儲存可作長期儲蓄，「閃電 」可用於日常消費和微交易。這種靈活性將 Bitcoin 管理從技術限制轉變為競爭優勢。



在經驗豐富的 Zeus LSP 團隊和 Boltz 開放原始碼社群的支援下，Zeus Swap 未來的演進有望在成本、處理時間和使用者體驗方面持續改善。這項服務是 Bitcoin 基礎架構趨於成熟的大趨勢的一部分，在此趨勢下，技術的複雜性對終端使用者而言變得透明。



## 資源



### 官方文件




- [Zeus Swap - 入口網站](https://swaps.zeuslsp.com)
- [Zeus Wallet - 行動應用程式](https://zeusln.app)
- [Blog Zeus - 公告與教學](https://blog.zeusln.com)
- [Zeus技術文件](https://docs.zeusln.app)



### 社群與支援




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)