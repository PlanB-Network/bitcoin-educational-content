---
name: ArkadeOS
description: Arkade 產品組合與 Ark Protocol 完整指南
---

![cover](assets/cover.webp)



Bitcoin 網路面臨一個重大挑戰：可擴充性。雖然主層 (第 1 層) 提供無與倫比的安全性和分散性，但每秒只能處理有限數量的交易。Lightning Network 已經成為一個很有前途的第二層（第 2 層）解決方案，可以實現快速、低成本的支付。然而，Lightning 也有其自身的限制：通道管理、對傳入流動資金的需求，以及可能讓新使用者望而卻步的技術複雜性。



這就是**Ark**的背景，這是一個全新的第 2 層通訊協定，旨在提供簡化的使用者體驗，同時不犧牲主權。 ***ArkadeOS**（或稱 Arkade）是此協定的第一個主要實作，提供下一代 Bitcoin 產品組合。



本教程將引領您進入 Arkade 的世界。我們將探討 Ark 協定如何運作、如何安裝和設定 Arkade wallet，以及如何使用它來即時、保密地傳送和接收比特幣，而且不會有一般 Lightning Network 的摩擦。



## 瞭解方舟通訊協定



在深入了解 Arkade 的使用之前，必須先掌握驅動 Arkade 的 Ark 協定的關鍵概念。Ark 並非獨立的區塊鏈，而是 Bitcoin 上的智慧協調機制。



### VTXO 概念


Ark 的核心是 **VTXO**（虛擬 UTXO）。VTXO 是尚未在 Bitcoin 區塊鏈上公佈的 UTXO：它存在於主鏈 (off-chain) 之外，但由區塊鏈上預先簽署的交易支持。



與中心化交易所的餘額不同，VTXO 真正屬於您。您持有加密證明，即使方舟服務器消失，您也可以隨時在區塊鏈上認領相應的真實比特幣。VTXO 使您能夠在用戶之間即時轉移價值，而無需等待區塊確認。



### ASP (方舟服務供應商) 的角色


Ark 通訊協定以用戶端伺服器模式運作。伺服器稱為 **ASP**（Ark Service Provider）。ASP 扮演傳導者的角色：




- 它為網路提供必要的流動資金。
- 它協調使用者之間的交易。
- 它在區塊鏈上組織結算「回合」。



必須注意的是，ASP 是**非監管**。它從不持有您的私人金鑰，也無法竊取您的資金。它的角色純粹是技術和後勤。如果 ASP 審查您的交易或宕機時，您總是可以透過單邊退出程序來取回您的資金。



### 回合與隱私


方舟上的交易是分批完成的，稱為 **Rounds**。ASP 會定期（例如每隔幾秒）收集所有待定交易，並以單一優化交易將其錨定在 Bitcoin 區塊鏈上。


此機制具有兩大優點：




- 可擴充性**：單筆 on-chain 交易即可驗證數千筆 off-chain 付款，大幅降低使用者的成本。
- 保密性**：每輪都扮演 **CoinJoin** 的角色。所有參與者的資金在以新的 VTXO 形式重新分配之前，都會混入一個共同的池中。這會中斷寄款人與收款人之間的連結，使得外部觀察者即使不是不可能，也很難追蹤到付款。



## ArkadeOS 簡報



ArkadeOS 是將 Ark 通訊協定提供給一般大眾的具體應用程式。它由 Ark Labs 開發，是一個完整的生態系統，包含一個組合 (Wallet)、一個伺服器 (Operator) 和開發者工具。



對於終端使用者而言，Arkade 採用優雅、直覺的 Web wallet (PWA - Progressive Web App) 形式。它將 VTXO 和 rounds 的密碼複雜性隱藏在熟悉的介面後面。有了 Arkade，您就有了接收地址、發送按鈕和交易記錄，就像經典的 wallet，但卻擁有 Ark 的即時性和保密性。



## 安裝與設定



由於 Arkade 是進階式 Web App，因此安裝起來特別容易，而且不一定會牽涉到傳統的應用程式商店。



### 存取與安裝


您可以透過電腦或行動裝置上的任何現代網路瀏覽器 (Chrome、Safari、Brave) 直接存取 Arkade。





- 請造訪應用程式的官方網站： **[arkade.money](https://arkade.money)**。



![arkade homepage](assets/fr/01.webp)



您會看到一系列介紹畫面，向您介紹 Arkade 的主要概念：Bitcoin 的新生態系統、自我保管的重要性以及批次交易的優點。



![arkade onboarding](assets/fr/02.webp)





- 在 Android (Chrome/Brave)** 上 ：按瀏覽器功能表 (三點)，然後選擇「安裝應用程式」或「新增至主畫面」。
- 在 iOS (Safari)** 上：按下分享按鈕 (有向上箭頭的正方形)，然後選擇「在首頁畫面上」。



安裝完成後，Arkade 會像原生應用程式一樣以全螢幕方式啟動，而且沒有位址列。



### 建立投資組合


首次啟動時，系統會要求您設定投資組合。





- 按一下 **「建立新的 Wallet」**。



![create wallet](assets/fr/03.webp)





- wallet 即時建立。與傳統的 Bitcoin 錢包不同，**Arkade 不會使用 12 或 24 個字的復原短語**。相反地，Arkade 會自動產生一個 Nostr (nsec) 格式的**私人密碼匙**，用來備份和還原您的 wallet。請記得立即儲存此金鑰 (請參閱下一節)。





- 您會看到 "Your new wallet is live!"畫面，確認您的 wallet 已準備好使用。點選**「GO TO WALLET」**進入主介面。



進入 wallet 之後，您會進入 Arkade 的主介面。在這裡您可以找到您的餘額、用於傳送和接收資金的按鈕，以及一個「應用程式」標籤，可讓您存取整合的應用程式，例如 Boltz (閃電交換)、LendaSat 和 LendaSwap (借貸服務) 以及 Fuji Money (合成資產)。



![wallet interface](assets/fr/04.webp)



### 連接至 ASP


預設情況下，投資組合會自動設定連線至 Arkade Labs 官方 ASP。您可以前往 ** 設定** > ** 關於**，查看所連線的伺服器位址 (目前為 `https://arkade.computer`)。



在目前的 Arkade (Beta) 版本中，無法手動修改 ASP 伺服器。應用程式會自動連接到官方的 Arkade Labs ASP。在未來，使用者或許可以根據自己的喜好選擇不同的 ASP，但目前還沒有這項功能。



### 備份您的私人密碼匙


**Arkade 使用 Nostr (nsec) 格式的私人密碼匙作為備份和復原方法。要備份您的私人密碼匙 ：





- 從主畫面進入 **設定**。
- 選擇 **「備份與隱私」**。
- 您會看到以「nsec...」格式顯示的 ** 私密金鑰**。這個長字符串是您恢復 wallet 的唯一方法。
- 按 ** "COPY NSEC TO CLIPBOARD" ** 複製私人密碼匙。
- 將密鑰存放在安全的地方**：寫在紙上、儲存在安全的密碼管理器中，或使用任何其他適合您的備份方法。
- Arkade 也提供 **「啟用 Nostr 備份」** 選項。此功能使用 Nostr 通訊協定 (分散式網路) 自動將 wallet 的某些資料加密備份至 Nostr 中繼站。這有助於多台裝置之間的同步，並提供更簡單的 wallet 狀態復原。



**重要**：Nostr 備份只是一項**舒適**功能。它們不會取代您的 nsec 金鑰備份。Nostr 中繼並不保證永久資料儲存。您的 Nsec 私密金鑰仍然是您恢復資金的唯一保證方式。



![backup private key](assets/fr/05.webp)




## 使用 Arkade



設定好 wallet 之後，您就可以探索 Arkade 的功能了。該介面旨在無縫統一不同類型的 Bitcoin 付款（On-chain、Lightning、Ark）。



### 接收資金



要為您的投資組合注資，請按 **「收款 」**。Arkade 提供三種收款方式：





- 方舟付款**：如果寄件者也使用 Arkade，請分享您的 Ark 位址，以進行即時、保密且幾乎免費的轉帳。
- 鏈上存款 (Boarding)**：使用 Bitcoin 位址 (`bc1p...`)，從經典 wallet 或交換所接收。在資金轉換為 VTXOs 之前，請等待確認 (~10 分鐘)。
- Lightning swap**：產生 Lightning 發票，並從外部 wallet Lightning 付款。資金會透過自動交換立即到帳。



![receive amount](assets/fr/06.webp)



收據畫面顯示所有可用選項：QR 代碼、方舟地址、Bitcoin (BIP21) 地址和 Lightning 發票。對於 Lightning 付款，請在交易過程中保持開啟應用程式。



![receive confirmation](assets/fr/07.webp)



### 寄送資金



要發送資金，請按 **「發送 」**，然後貼上收件人地址或掃描 QR 代碼。Arkade 會自動偵測所需的付款類型：





- 方舟**付款：至方舟地址，轉帳即時、私密且幾乎免費（0 SATS 費用）。收款人不需要在線。
- Lightning** 付款：掃描 Lightning 發票 (`lnbc...`)，Arkade 會自動執行交換。ASP 替您支付發票，並從您的 Arkade 結餘中扣款。
- 鏈上支付**：朝向經典的 Bitcoin 位址 (`bc1q...`或`bc1p...`)，Arkade 會啟動「協作產出」，這將包含在下一輪的 on-chain 中。



檢查「簽署交易」畫面的詳細資料，然後用 **「點選簽署」** 確認。



![send payment](assets/fr/08.webp)



**目前的限制 (Beta)**：不足 24 小時前建立的 VTXO 不能用於 on-chain 輸出。如果遇到錯誤，請等到您的 VTXO「成熟」後再使用。



**on-chain 輸出保密性**：以下範例顯示 [mempool.space 上的方舟輸出交易](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb)。我們觀察到一個分散的輸入到 4 個不同的輸出，就像 CoinJoin。對於外部觀察者來說，不可能確定哪個金額屬於哪個使用者。



![transaction ark mempool](assets/fr/11.webp)



## 進階功能



### VTXO 過期管理


Ark 通訊協定的技術特點是 VTXO 有***有限的使用期限。這個時間限制是協定設計的固有特性。到期時間可由各 ASP 伺服器設定；在官方 Arkade Labs ASP 上，此期限約為**4 週 (≈30 天)**。



**此限制可讓方舟伺服器有效管理流動資金，並清理非活躍用戶的 VTXO。到期後，方舟伺服器可從技術上認領 VTXO 樹狀結構中的剩餘資金。



**為了讓您的 VTXO 保持活躍，需要在過期前將其 「刷新」。刷新包括參與新的 「回合」，在該回合中，您接近到期的 VTXO 將被交換為具有新的完整有效期（Arkade Labs ASP 上≈30 天）的新 VTXO。



Arkade 產品組合會自動管理此流程：應用程式會持續監控您的 VTXOs 狀態，並在到期前幾天自動刷新。只要您定期開啟應用程式 (至少每週一次)，您的 VTXOs 就會自動保持活躍。



**如果您超過 4 週未開啟您的投資組合，您的 VTXOs 將會過期。但是，您不會失去您的資金：您仍可選擇通過**單邊退出**收回資金（請參閱下一節）。此程序成本較高且速度較慢，但可確保您的資金仍可收回。



需要定期開啟應用程式使得 Arkade 成為專為日常消費而設計的 **"Hot Wallet"**，而非長期儲存的保險箱。若要儲存比特幣而不需長期使用，請選擇冷冰冰的 wallet 硬體。



**檢查您的 VTXO 的狀態**：您可以在**設定** > **進階**中監控您的 VTXOs 狀態。請參閱 「下次更新」，查看下次自動更新的時間，以及 「虛擬幣」，查看您所有 VTXO 的詳細清單及其到期日。



![vtxo management](assets/fr/09.webp)



### 單邊退出 (Sortie Unilatérale)



單邊退出是方舟協定的**基本加密保證**，即使 ASP 消失、審查您的交易或拒絕合作，也能確保您取回資金。嚴格來說，您的 VTXO 是您擁有的**預先簽署的 Bitcoin 交易**。在絕對緊急情況下，您可以在 Bitcoin 區塊鏈上廣播這些交易，無需任何人授權即可取回您的資金。



**如何運作？這個過程分兩個階段進行。首先，**解鎖**：您在交易樹中依序廣播組成您的 VTXO 的預簽交易。然後是**最終化**：一旦時間鎖過期（通常是 24 小時），您就可以從標準地址收取您的比特幣。



**Current status in Arkade**：在 Beta 版中，還沒有單面輸出的按鈕或簡單的使用者介面。此功能目前需要使用 Arkade SDK 以及 TypeScript 程式設計的技術知識。



**即使無法透過按鍵存取程序，加密保證仍然存在。您的 VTXO 包含合法屬於您的預先簽署交易。正是這種技術保證使 Ark 成為一個**非監護**協定：即使在最壞的情況下，您的資金在技術上仍然是可收回的。Arkade 未來的版本可能會加入簡化的介面。



## 優點與限制



為了將 Arkade 置於正確的環境中，讓我們總結一下它目前的優缺點。



### 重點介紹




- 使用者體驗 (UX)**：不需要像 Lightning 般進行頻道管理、傳入容量或複雜的頻道備份。只需安裝即可使用。
- 隱私** ：預設 CoinJoin 架構提供比標準 on-chain 或 Lightning 交易高得多的匿名性。
- 互通性**：從單一介面支付任何 Bitcoin QR 碼 (On-chain 或 Lightning)。



### 限制條件




- 年輕的協議***：方舟是一項最新的技術。可能存在錯誤。建議不要使用 Ark 來儲存遺失會很嚴重的款項。
- ASP 依賴性**：雖然非監護性，但系統的流動性依賴 ASP 的可用性。如果 ASP 離線，您就無法再進行即時交易（只能輸出您的 on-chain 資金）。
- 僅適用於 Hot Wallet**：需要定期開啟應用程式刷新 VTXO，不適合冷儲存 (Cold 儲存)。



## 比較：Arkade vs Lightning vs Cashu



為了更好地瞭解 Arkade 的定位，讓我們將其與其他兩大擴充能力解決方案進行比較。



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** 是理想的折衷方案：既有 Cashu 的簡單和保密性，又有 Lightning 的主權（非監護）。



## 支援與協助



如果您在使用 Arkade 時遇到任何問題或有任何疑問，應用程式會提供多種支援選項：





- 移至 **設定** > **支援**。
- 您會發現多種選項：
  - 客戶支援**：取得投資組合的協助、報告錯誤或提出問題。
  - 安全聊天**：您的對話是安全且隱私的，並在會談之間保留歷史記錄。
  - 錯誤報告**：報告您遇到的任何問題，包括重現問題的步驟。
  - 追蹤進度**：隨時追蹤您的支援票單和對話。



![support](assets/fr/10.webp)



Arkade 團隊也透過 @arkade_os 頻道活躍於 Telegram，提供支援與整合機會。



## 重要聲明：應用程式處於測試階段



**⚠️ Arkade 目前在 mainnet Bitcoin** 上處於公開測試階段。雖然應用程式可以使用真實的 bitcoins，但必須採取某些預防措施。



### 使用建議




- 使用少量**：避免在 Arkade 上儲存大筆金額。將這台 wallet 用於您的日常支出，並將您的儲蓄放在冷冰冰的 wallet 硬體上。
- 可能的錯誤與限制**：與任何正在開發中的應用程式一樣，Arkade 可能會出現錯誤或意想不到的行為。請透過整合式支援回報任何問題。
- 快速演進** ：應用程式和通訊協定不斷改進。某些功能可能會在未來版本中變更或新增。



### 目前已知的限制




- 24 小時延遲 VTXO**：新建立的 VTXO 不能立即用於 on-chain 輸出。
- ASP 唯一**：目前還無法在應用程式中變更 ASP 伺服器。
- 技術單邊輸出**：目前還沒有單邊輸出的簡化介面（需要 SDK）。



Arkade Labs 團隊正積極在未來版本中放寬這些限制。



## 總結



ArkadeOS 是 Bitcoin 生態系統的一大突破。透過實作 Ark 通訊協定，它證明了 Bitcoin 的基本原則 (不信任、驗證) 與簡單易用是可以相容的。



儘管 Arkade 仍處於起步階段，但它提供了 Bitcoin 支付未來的迷人一瞥：即時、私密且人人皆可使用，無需任何技術前提。它是您日常開支的完美工具，與您的安全儲蓄解決方案 (Cold Wallet) 相輔相成。



我們鼓勵您使用少量的 Arkade 進行測試，親自發現這個新的通訊協定。生態系統發展迅速，而 Arkade 正站在這個創新的最前線。



## 資源



若要瞭解更多資訊，請參閱官方資源：





- Arkade** 網站：[arkadeos.com](https://arkadeos.com)
- 文件**：[docs.arkadeos.com](https://docs.arkadeos.com)
- 方舟**通訊協定：[ark-protocol.org](https://ark-protocol.org)
- 原始碼** ：[GitHub Arkade](https://github.com/arkade-os)