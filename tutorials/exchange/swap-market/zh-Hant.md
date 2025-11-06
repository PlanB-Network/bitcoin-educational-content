---
name: 交換市場
description: Bitcoin 和 Lightning 交換服務聚合器
---

![cover](assets/cover.webp)



在 Bitcoin on-chain 和 Lightning Network 之間轉移資金通常需要手動開啟 Lightning 通道（技術性且成本高昂），或者使用有 KYC 的集中式掉期平台。SwapMarket 提供了另一種選擇：透過有競爭力的供應商進行無信託原子掉期，無需 KYC。



創新：雖然供應商是中介，但 HTLC (*Hash 時間鎖定合約*) 在數學上可保證您的資金仍在您的控制之下。幾個提供者（Boltz、ZEUS Swaps、Eldamar、Middle Way）的聚合創造了價格競爭。Interface 網路開放源碼可自行託管。



## 什麼是 SwapMarket？



SwapMarket 是 2024 年推出的開放源碼聚合器，其功能是比較 Bitcoin/Lightning 掉期供應商。用戶可即時比較條件（費用、流動性、限額）並選擇最佳提供商。



### 技術架構



**前端客戶端**：100% 客戶端應用程式 (fork Boltz Web App) 託管在 GitHub 頁面上。程式碼在瀏覽器中執行，無需後端伺服器。歷史記錄儲存於本機 (cookies/快取)。公開且可稽核的原始碼。



**Provider discovery** ：src/configs/mainnet.ts`中的硬編碼清單。透過 Pull Request 或電子郵件新增提供者。



**獨立的後端**：每個供應商都有自己的 Boltz 後端。介面即時查詢 API，即時比較報價。



**HTLC 原子掉期**：Hash 時間鎖定合約保證原子性：不是掉期執行，就是雙方各自收回資金。數學上已消除交易對手風險。



### 經營理念



SwapMarket 透過在提供者之間建立費用和流動性的競爭來減少集中化。無需 KYC、開放源代碼可自行託管、多個獨立運營商可避免單點故障。



## 主要功能



### 供應商市場



介面顯示所有作用中的提供商：提供商名稱、應用費用（百分比和/或固定）、可用的最低/最高金額，以及支援的掉期類型。應用程式可直接查詢配置檔中引用的每個提供商的 API，以即時擷取報價。提供商之間的競爭保證了最佳費率，標準掉期的費率通常約為 0.5%。



### 雙向交換



**Swap-in (on-chain → Lightning)**：將 on-chain BTC 兌換成 Lightning Satoshis。用例：為移動式 wallet Lightning 供電、在節點上獲得傳入容量，或擁有即時流動性。



**Swap-out (Lightning → on-chain)**：將 Lightning Satoshis 轉換為 on-chain BTC。用例：將 wallet Lightning 清空至冷庫，或重新平衡各層之間的流動性。



### 安全與復原



**Trustless 原子交換**：HTLC 可保證交換完全完成，或每一方都能收回其權益。交易對手的風險在數學上被消除。



**Repayment 機制**：每個交換都有時間鎖定。如果交換失敗，資金會在到期後自動退回。使用者始終保留取回比特幣的選擇權。



**恢復金鑰**：SwapMarket 可讓您匯出正在進行中的交換的恢復金鑰。如果發生問題，這些金鑰可用於從任何裝置完成或取消交換。



## 安裝與存取



### Interface 網頁



SwapMarket 不需要安裝。可透過瀏覽器存取 https://swapmarket.github.io。若要達到最高保密性，請使用 Brave、Firefox 與反追蹤擴充套件，或 LibreWolf。建議使用 Tor 瀏覽器進行網路匿名。



無需註冊、電子郵件或身份驗證。



### 自行託管（選擇性）



對於希望不依賴官方 GitHub Pages 網域的技術使用者，SwapMarket 可以在本機執行：



**Via npm** ：


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Via Docker** ：


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



應用程式將可在 `http://localhost:3000` 存取。自行託管可保證完全控制介面，消除官方網域審查的風險，並允許在執行前審核原始碼。



### 初始設定



**Wallet Lightning**：請確定您擁有可運作的 wallet Lightning (Phoenix、Zeus、BlueWallet 等)。對於換入，您將 generate 一張 Lightning 發票。對於換出，您將支付一張 Lightning 發票。



**Wallet on-chain**：對於換入，您需要 wallet Bitcoin on-chain 來發送資金。若要換出，請準備 Bitcoin 收款地址。



**可選配置**：SwapMarket 在瀏覽器 cookie 中儲存交換歷史和偏好設定。無需建立帳戶。



## 存取設定與救援金鑰



在您進行第一次交換之前，我們強烈建議您下載您的 **Rescue Key**。此緊急金鑰可讓您在發生技術問題或無法存取您的裝置時恢復您的資金。



### 存取參數



從 SwapMarket 主頁面，點擊介面右上方交換表格旁邊的齒輪圖示 (⚙️)。



![Accès aux paramètres](assets/fr/01.webp)



### 頁面設定



設定」頁面開啟，顯示多個設定選項：





- 面額**：可選擇 BTC 或 sats
- 小數分隔符**：小數分隔符 (, 或 .)
- 音訊/瀏覽器通知**：音訊和瀏覽器通知
- 救援金鑰** ：下載復原金鑰
- 日誌**：檢視、下載或刪除日誌



![Page Settings](assets/fr/02.webp)



### 下載救援鑰匙



按一下「救援金鑰」旁邊的**下載**按鈕。



**Important points** ：




- 救援鑰匙是一個**一站式緊急鑰匙**，適用於您未來所有的交換。
- 將此金鑰存放在**安全且永久**的地方 (密碼管理員、數位安全保險箱)
- 若發生交換問題（超時、技術故障），此金鑰可讓您恢復資金



## 逐步建立交換



### 交換：閃電 → Bitcoin



第一個範例說明如何將 Lightning Satoshis 轉換成 on-chain bitcoins。



**步驟 1：交換組態



從主頁面，選擇交換表格 ：




- LIGHTNING** (上方欄位)：輸入您希望以 sats Lightning 寄送的金額 (例如：30,000 sats)
- BITCOIN** (下方欄位)：扣除費用後自動顯示您將收到的金額（例如：29,320 sats）



在底部欄位，貼上您希望收到資金的**收款 Bitcoin 位址**。請仔細檢查此地址。



預設提供商通常是 Boltz Exchange。網路費用和提供商費用會清楚顯示。



![Configuration swap-out](assets/fr/03.webp)



**第 2 步：供應商選擇**



按一下提供者下拉式功能表 (預設值：「Boltz Exchange」)，以顯示所有可用的流通量提供者。



開啟一個模式視窗，顯示比較表：




- 狀態**：Green 指示器，如果提供者處於活動狀態
- 別名**：供應商名稱（Boltz Exchange、Middle Way、Eldamar、ZEUS Swaps）
- 費用**：提供者收取的費用（一般介於 0.49% 和 0.5% 之間）。
- 最大交換**：接受的最大掉期金額



比較費用和最高金額，然後選擇您中意的提供商。



**請注意**：提供商選擇介面不會顯示每個提供商的**最低金額。此資訊只會在選擇醫療服務提供者後，出現在掉期建立介面中。最低和最高金額可能因提供商而異，也可能隨時間改變。 **在您進行交換時，請務必檢查這些限制**：如果您希望交換的金額超出了提供商的限制，您可以選擇另一個更適合您交易的提供商。



![Sélection du provider](assets/fr/04.webp)



**第 3 步：建立交換和 Lightning** 付款



按一下黃色的 **「CREATE ATOMIC SWAP」** 按鈕。SwapMarket 將在 generate 發出一張**Lightning 發票** (BOLT11) 讓您從 wallet Lightning 付款。



頁面顯示 ：




- 交換 ID**：唯一的交換識別碼 (例如：J4ymFIMVR6Hm)
- 狀態**："swap.created" (已建立交換，等待付款)
- QR 代碼**：使用您的 wallet Lightning 掃描它
- Invoice Lightning**：以「lnbc」開頭的字串（例：lnbc300u1p50whiv...gn5dk2szgqkvfkzc）



用您的 wallet Lightning（Phoenix、Zeus、BlueWallet 等）支付此發票。要支付的精確金額會顯示出來（例如：30,000 sats）。



![Paiement Lightning](assets/fr/05.webp)



**步驟 4：確認與接受**



一旦確認 Lightning 付款，SwapMarket 即時收到您的付款，供應商會向您的地址廣播 Bitcoin 交易。



狀態變更為 **"invoice.settled "**（發票已付），並顯示確認訊息。



您的 on-chain 比特幣將在交易確認後立即可用（通常是幾分鐘到幾小時，取決於提供商選擇的 mining 費用）。



![Confirmation swap-out](assets/fr/06.webp)



您可以點擊 **「OPEN CLAIM TRANSACTION」**，在區塊鏈瀏覽器上查看 Bitcoin 交易。



### 換入：Bitcoin → Lightning



第二個範例顯示如何將 on-chain bitcoins 兌換成 Lightning Satoshis。



**步驟 1：交換組態



從主頁面，選擇交換表格 ：




- BITCOIN** (上方欄位)：輸入您希望以 sats Bitcoin 寄送的金額 (例如：63,400 sats)
- LIGHTNING** （底部欄位）：扣除費用後自動顯示您將收到的金額（例如：62 884 sats）



在底部欄位，貼上由 wallet Lightning 產生的 Lightning** 發票 (BOLT11)，或使用您的 LNURL 位址 (如果您的 wallet 支援)。



![Configuration swap-in](assets/fr/07.webp)



**步驟 2：救援金鑰檢查**



按一下 ** "CREATE ATOMIC SWAP" ** 後，會出現一個模式視窗，要求您驗證救援金鑰。



![Modal Rescue Key](assets/fr/08.webp)



**Boltz 救援金鑰**：由於您已在初始設定時上傳了復原金鑰 (請參閱前一節)，請按一下 **「VERIFY EXISTING KEY」** 按鈕以匯入您儲存的金鑰。



選擇先前下載的救援金鑰檔案。驗證成功後，介面會自動切換到下一步。



**步驟 3：Bitcoin** 存入地址



SwapMarket 現在會生成一個 ** 獨特的 Bitcoin 位址**，其中包含與您的 Lightning 發票相連的 HTLC 合約。



頁面顯示 ：




- 交換 ID**：唯一識別碼 (例如：1kGmB6JyGqU4)
- 狀態**："invoice.set" (發票已設定，等待付款 Bitcoin)
- QR 代碼**：Bitcoin 車廠地址
- Bitcoin** 位址：通常以 "bc1p... "開頭。(例：bc1p5mvtwxapjkds...9d4n9f)
- 黃色警告** ：「請確保您的交易在建立此交換後 ~24 小時內確認！」



這段 ~24 小時的時間是 HTLC 合約的**超時**。如果您的 Bitcoin 交易在這段時間內未被確認，交換將會失敗，您需要使用救援金鑰來取回您的資金。



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



您可以按一下 **「地址 」** 按鈕複製地址，或直接從 wallet on-chain 掃描 QR 代碼。



**步驟 4：傳送比特幣**



從您的 wallet Bitcoin on-chain 中，寄出**完全**所示的金額（例如 63,400 sats）到所生成的地址。



**重要**：使用適當的 mining 費用以保證快速確認。如果費用太低，而交易停留在 mempool 超時 (~24h) 之後，交換就會失敗。



一旦交易被傳送，SwapMarket 會偵測到它在 mempool 中，並顯示 ：




- 狀態** ："transaction.mempool
- 訊息**：「交易在 mempool 中 - 等待確認以完成交換」



![Transaction en mempool](assets/fr/10.webp)



**步驟 5：確認與閃電**接收



只要 Bitcoin 交易收到第一次確認，提供商就會自動支付您的 Lightning 發票。您會立即在您的 wallet Lightning 上收到 Satoshis。



狀態變更為 **"transaction.claim.pending "**，然後顯示確認訊息：



![Confirmation swap-in](assets/fr/11.webp)



您的 「閃電」(Lightning) Satoshis 可立即在您的 wallet 中使用。



## 優點與限制



### 優點



**費率競爭**：提供商的彙集創造了自然的競爭，將費用拉低（0.49% 至 0.5%）。



**保密性**：無需 KYC、100% 客戶端介面（不傳輸個人資料）、與 Tor 瀏覽器相容。



**非監護**：HTLC 在數學上保證您資金的獨家控制權。要麼交換成功，要麼您拿回您的比特幣。



**Open-source self-hostable**：可稽核的公開程式碼，可在本機部署，以最大程度抵抗審查。



### 限制條件



**流動性有限**：活躍供應商數量有限（Boltz、Eldamar、MiddleWay 視期而定）。最高金額可能有限。



**到期時間**：逾時時間從 24 小時到 48 小時。如果 on-chain 交易在到期前未確認，則需要手動復原。



**Interface 集中化**：雖然可自行託管，但官方介面託管在 GitHub 頁面上。如果 GitHub 審查 repo，透過 swapmarket.github.io 的存取將被封鎖（解決方案：自行託管）。



**on-chain 軌跡**：HTLC 腳本有可能被進階區塊鏈分析識別。



## 最佳實踐



### 安全設定



**下載您的救援金鑰**：在您第一次進行交換之前，請從 Settings 下載您的 Rescue Key（救援密鑰）（請參閱上文的專用部分）。這個獨一無二的金鑰將適用於您未來的所有交換，讓您可以在發生問題時恢復您的資金。



**使用 Tor 瀏覽器**：為了獲得最大的保密性，請透過 Tor 瀏覽器存取 SwapMarket 以隱藏您的 IP 位址。



**考慮自我託管**：對於技術使用者來說，執行您自己的 SwapMarket 範例可免除對官方 GitHub Pages 網域的依賴。



### 交換優化



**Keep an eye on the mempool**：在換入之前檢查 mempool.space。選擇活動較少的時間，將 mining 成本降至最低。



**檢查地址**：對於交換，請仔細檢查您的收件地址。使用複製和貼上，並檢查前 5 個和後 5 個字元。



** 用少量**進行測試：從允許的最小值 (25,000 到 50,000 sats) 開始。當您熟練掌握後，再逐漸增加。



**記錄您的交換**：記下每個掉期的 ID、贖回地址和到期日。這些資訊有助於追蹤和在出現技術問題時恢復。



### 使用策略



**平衡您的現金流**：使用 SwapMarket，根據您的實際需求調整您在 on-chain (儲蓄、長期保障) 和 Lightning (日常支出、即時付款) 之間的分配。



**計算盈利能力**：對於永久性的 Lightning 流動資金需求，比較重複掉期與直接開設 Lightning 通道的累計成本。SwapMarket 擅長於一次性調整，不一定適用於大規模的定期流動。



## SwapMarket vs Boltz：有何差異？



### Boltz：技術與服務



**Boltz 是透過 HTLC 在 Bitcoin、Lightning 和 Liquid 之間實作原子交換的開放原始碼技術** (GitHub 上的 `boltz-backend`)。



**關鍵點**：所有 SwapMarket 供應商 (Boltz Exchange、ZEUS Swaps、Eldamar、Middle Way) 都部署了自己的 Boltz 後端實例。因此基礎技術是相同的。Boltz 後端的漏洞可能會影響所有供應商，但系統的開放源碼特性允許社群稽核。



**Boltz Exchange** 是由 Boltz 團隊營運的單一服務，而 **SwapMarket** 則將數家全部使用 Boltz 技術的供應商集合在一起，創造出具有競爭力的價格環境。



如需詳細資訊，請參閱我們的 Boltz 和 Zeus Swap 教學：



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### 主要差異



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarket 的優點**：價格競爭、後端實例多樣化、即時比較。



**Technological alternatives** (not SwapMarket compatible)：Lightning Loop (Lightning Labs)、Muun Wallet、NLoop、Breez Wallet。這些解決方案使用各自的海底交換實作。



**建議**：使用 Boltz Exchange 以簡化操作，或使用 SwapMarket 以透過競爭優化成本。兩者的安全性相當（HTLC 非監控）。



## 總結



SwapMarket 透過將多個提供者彙集到單一介面來促進 Bitcoin/Lightning 交換。HTLC 架構保證了交換的非監管性，沒有 KYC 可保護機密性，可自行託管的開放原始碼加強了對審查的抵抗力。



供應商之間的競爭提高了費率，並使流動資金的來源成倍增加。為了優化雙層管理 (on-chain 節省、Lightning 支出)，SwapMarket 是一個實用的工具，可維護金融主權和保密性。



## 資源



### 官方文件




- [SwapMarket - 網路應用程式](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [技術文件](https://docs.boltz.exchange/)
- [Guide self-hosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### 相關專案




- [Boltz Exchange](https://boltz.exchange) - 原始原子交換服務
- [ZEUS Swaps](https://zeusln.com) - 閃電交換提供者