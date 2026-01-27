---
name: Heritage
description: 透過 Taproot 腳本整合繼承機制的 Bitcoin 產品組合
---

![cover](assets/cover.webp)



在死亡或喪失工作能力的情況下，如何傳承比特幣對任何加密資產持有者來說都是一大挑戰。如果沒有一個合適的繼承計劃，這些資產對您的親人來說就無法收回。



Heritage 提供了一個優雅的答案，直接在 Bitcoin 區塊鏈上實現死人轉換機制。這個開放原始碼的 wallet 可以設定 on-chain 的繼承條件：如果所有者在定義的期間內不再進行交易，預先指定的替代鑰匙就可以釋放資金。



## 什麼是遺產？



Heritage 是透過 Taproot scripts 原生整合繼承機制的 Bitcoin 產品組合。由 Jérémie Rodon 在 MIT 授權下開發，此開放源碼軟體保證了透明度和耐用性。



Heritage 使用以 Bitcoin 位址編碼的 Taproot 腳本。每個 UTXO 整合了兩種支出條件：





- 主路徑** ：擁有者可以隨時使用他的主索引鍵花費他的 bitcoins
- 替代路徑**：對於每個指定的繼承人，腳本會結合其公開金鑰與時間鎖



每筆業主交易都會自動延遲繼承條款的啟動日期。如果長期沒有活動（死亡、喪失行為能力），則會自動啟動條件。



## 遺產服務（選擇性）



Heritage 提供兩種使用方式：



**Do it yourself（免費）**：單獨的開放原始碼應用程式。您使用自己的節點自主管理一切。此選項提供內建備份存取權限、內建繼承權和您的比特幣獨家控制權。但是，您需要建立自己的警示（行事曆、提醒事項），以免忘記更新時間鎖，而且也沒有自動通知繼承人的功能。



**使用服務（每年0.05%）** ：btc-heritage.com 服務增加了簡化管理的功能：




- 在您的截止期限到期前自動提醒
- 自動通知繼承人，引導他們完成復原程序
- 優先支援
- 簡化描述符管理



費用：每年管理金額的 0.05%，最低 0.5 mBTC/年。第一年免費。



服務保持非監管性：您的私人密碼匙從未離開您的裝置。Heritage 無法存取您的資金。



## Heritage CLI



對於喜歡使用終端機的進階使用者，Heritage 提供命令列工具 (CLI)，用於粒度控制和氣隙機器操作。



![Page Heritage CLI](assets/fr/03.webp)



完整的 CLI 文件可在 [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli) 找到。您可在此找到下載、連線到服務、建立錢包 (使用 Ledger 或本地金鑰)、管理繼承人和交易的說明。



本教學著重於桌面應用程式，對大多數使用者而言，桌面應用程式較容易使用。



## 傳統桌面



Heritage Desktop 是一款圖形化應用程式，具有直觀的介面，可引導使用者完成設定流程的每個步驟。



### 下載



前往 [btc-heritage.com](https://btc-heritage.com)，點選「下載應用程式」。



![Page d'accueil Heritage](assets/fr/01.webp)



選擇與您作業系統相對應的版本（Linux 64bits 或 Windows 64bits）。二進位檔未經數位簽章，可能會觸發安全警告。



![Page de téléchargement](assets/fr/02.webp)



### 在 Linux 上安裝



在 Linux 上，應用程式以 AppImage 格式發行。在執行之前，您需要先安裝`libfuse2`相依性：



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



然後將檔案製成可執行檔案並執行：



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### 首次發射



首次啟動時，上線精靈會提供您三個選擇：



![Onboarding initial](assets/fr/05.webp)





- 設定遺產 Wallet**：使用遺產計劃建立新的 wallet
- 繼承比特幣**：繼承比特幣
- 自己探索**：在沒有協助的情況下探索功能



選擇「設定傳統 Wallet」來建立您的第一台 wallet。



### Bitcoin 網路連線



選擇與 Bitcoin 網路連線的方式：



![Choix connexion](assets/fr/06.webp)





- 使用遺產服務**：管理基礎設施，讓繼承人更輕鬆
- 使用我自己的節點**：連接至您自己的 Bitcoin 核心或 Electrum 節點



在本教程中，我們使用自己的節點。



### 私密金鑰管理



選擇管理私人密碼匙的方式：



![Gestion des clés](assets/fr/07.webp)





- 搭配 Ledger 硬體裝置** ：搭配 wallet 硬體裝置（建議）可達到最高安全性
- 本地儲存密碼**：本地儲存的鑰匙具有密碼保護
- 還原現有的 wallet** ：從現有的 seed 還原



### 節點配置



如果您使用自己的節點，應用程式會引導您完成其設定。請確定您的 Bitcoin 或 Electrum 節點是 .NET 的：




- 已安裝並執行
- 與 Bitcoin 網路同步
- 設定為接受 RPC 連線 (Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



當您的節點準備就緒時，按一下「My Bitcoin node is up and running」（我的 Bitcoin 節點已開始運作）。



### 狀態面板



按一下右上角的「狀態」，然後按一下「開啟組態」以存取連線參數。



![Panneau Status](assets/fr/09.webp)



設定 Electrum 伺服器的 URL (例如 `umbrel.local:50001` 如果您使用 Umbrel)。



![Configuration Electrum](assets/fr/10.webp)



### 創建 wallet



建立連線後，按一下 WALLETS 標籤中的「建立 Wallet」。



![Créer wallet](assets/fr/11.webp)



彈出式視窗解釋 Heritage .NET 的分割架構：



![Architecture split](assets/fr/12.webp)



1. **Key Provider (Offline)**：管理您的私人金鑰並簽署交易。可以是 Ledger 或 wallet 軟體。


2. **Online Wallet**：處理與 Bitcoin 網路同步、位址建立和交易廣播。



填寫建立表格 ：



![Formulaire création wallet](assets/fr/13.webp)





- Wallet 名稱**：一個獨特的名稱來識別您的 wallet
- 金鑰提供者**：本教程選擇本機金鑰儲存
- 新建/恢復**：選擇「新增」，以 generate 新增 seed
- 字數**：建議 24 個字，以獲得最大的安全性



輸入強大的密碼，並選擇線上 Wallet 的選項：



![Options Online Wallet](assets/fr/14.webp)





- 本地節點**：使用您自己的 Electrum 或 Bitcoin 核心節點
- Heritage 服務**：使用 Heritage 服務（建議用於通知功能）



按一下「建立 Wallet」以完成建立。



### Interface 來自 wallet



您的 wallet 已建立。介面會顯示 ：



![Interface wallet](assets/fr/15.webp)





- 平衡
- 傳送與接收按鈕
- 交易歷史
- 遺產配置歷史
- wallet 地址



### 建立繼承人



前往「繼承人」標籤，建立您的繼承人。



![Page Heirs](assets/fr/16.webp)



資訊彈出視窗說明：




- 繼承人是與個人相關的 Bitcoin 公開金鑰
- 每個繼承人都有自己的助記詞組
- 第一個繼承人應該是自己的「備用」（以防主 wallet 遺失）。



#### 建立備份繼承人



按一下「建立繼承人」，並命名為「備份」。



![Création héritier Backup](assets/fr/17.webp)



彈出式視窗解釋為何不含 passphrase 的 12 個字的句子對繼承人來說是安全的：


1. **無法立即存取**：繼承人鑰匙在時間鎖到期前無法存取資金


2. **損害偵測**：如果有人存取短語，您可以更新 Heritage 設定


3. **長期使用便利性**：passphrase 可能會在多年後被遺忘



配置继承人 ：



![Configuration héritier](assets/fr/18.webp)





- 金鑰提供者** ：本地金鑰儲存
- 新增**：產生新的 seed
- 字數**：12 個字



完成建立 ：



![Finalisation héritier](assets/fr/19.webp)





- 繼承人類型**：延伸公開金鑰
- 匯出至服務**：選項，可自動通知繼承人



現在已建立備份繼承人：



![Héritier créé](assets/fr/20.webp)



#### 保存繼承人的助記詞組



按一下備份 Heir，然後按一下「顯示 Mnemonic」：



![Afficher mnemonic](assets/fr/21.webp)



**重要： 記下這 12 個字，並妥善保存。這是找回資金的關鍵。



![Phrase mnémotechnique](assets/fr/22.webp)



#### 從應用程式中移除 seed



寫下詞組後，存取傳承參數 (齒輪圖示)：



![Paramètres héritier](assets/fr/23.webp)



使用「Strip Heir Seed」從應用程式中移除私人密碼匙。確認您已儲存短語。



![Strip Heir Seed](assets/fr/24.webp)



這是一項安全措施：只有公開金鑰會保留在應用程式中，足以設定繼承。



#### 設立第二繼承人



重複此程序以建立第二個繼承人 (例如 "Satoshi")。現在您將有兩個繼承人：



![Deux héritiers](assets/fr/25.webp)





- 備份**：您的個人緊急鑰匙
- Satoshi**：指定繼承人



### 遺產配置



返回您的 wallet，然後按一下「設定」圖示：



![Paramètres wallet](assets/fr/26.webp)



在 「Heritage Configuration（傳統配置）」部分，按一下 「Create（建立）」：



![Heritage Configuration](assets/fr/27.webp)



為每個傳承設定時間限制：



![Configuration délais](assets/fr/28.webp)





- 備份**：180 天 (6 個月) - 到期日：2026-06-18
- Satoshi**：455 天 (15 個月) - 到期日：2027-03-20



**重要**：每位繼承人的延遲時間必須比前一位繼承人更長。第一位繼承人 (Backup) 會先取得資金。



同時配置 ：



![Configuration finale](assets/fr/29.webp)





- 參考日期**：計算前置時間的起始日期
- 最低到期延遲**：交易後的最短延遲時間（建議 10 天）



按一下「建立」以驗證組態。



Heritage 設定現在已啟動：



![Configuration active](assets/fr/30.webp)



它會顯示兩個繼承人各自的最後期限和到期日。



### 儲存描述符



**重要**：保存您的 wallet 描述符。如果沒有這些描述符，即使有記憶詞組，也無法恢復資金。



按一下「備份描述符」：



![Bouton Backup](assets/fr/31.webp)



儲存包含 Bitcoin 描述符的 JSON 檔案：



![Backup descripteurs](assets/fr/32.webp)



這個檔案應該連同它們各自的助記詞組一起傳給您的繼承人。



### 接收比特幣



按一下「接收」以 generate 接收位址：



![Recevoir bitcoins](assets/fr/33.webp)



恭喜您您的 Heritage Wallet 已準備好接收 bitcoins。每個產生的位址都會自動加入您的 Heritage 條件。



收到交易後，您的餘額會更新：



![Solde mis à jour](assets/fr/34.webp)



歷史記錄顯示交易和相關的 Heritage 設定。



---

## 繼承人追討



一旦超過設定的時間，繼承人就可以取回資金。



### 先決條件



繼承人需要：


1.他的 12 個字記憶詞組


2.原始 wallet 描述檔備份檔案 (JSON)



### 建立繼承人 Wallet



在「繼承」標籤中，彈出式視窗提醒您這些先決條件：



![Page Heir Wallets](assets/fr/35.webp)



**請注意**：如果沒有描述符備份檔案，即使使用正確的助記短語，也無法存取資金。



按一下「建立繼承人 Wallet」：



![Créer Heir Wallet](assets/fr/36.webp)



請填寫表格：



![Formulaire Heir Wallet](assets/fr/37.webp)





- 繼承人 Wallet 姓名**：繼承人名稱 wallet
- 金鑰提供者** ：本地金鑰儲存
- 還原**：選取此選項可輸入現有的詞組



輸入繼承人的 12 個字助記短語，並設定 Heritage Provider：



![Entrée mnemonic](assets/fr/38.webp)





- 遺產提供者**：「本地 」使用您自己的節點與備份檔案



載入 JSON 備份檔案，然後按一下「建立繼承人 Wallet」：



![Chargement backup](assets/fr/39.webp)



### Interface 繼承者 Wallet



繼承者 Wallet 已經建立。最初，如果時間鎖未到期，則無繼承權可用：



![Pas d'héritage disponible](assets/fr/40.webp)



一旦延遲結束，且資金已與 Bitcoin 網路同步，它們就會出現在繼承列表中：



![Héritage disponible](assets/fr/41.webp)



介面顯示 ：




- 鑰匙類型與指紋
- 可繼承基金總額
- 目前可花費的金額（若時間鎖尚未過期，則為 0 sat）
- 到期日和失效日期



到達到期日時，「花費」按鈕會將比特幣轉移至個人 wallet。



---

## 最佳實踐



### 儲存描述符



wallet 描述符對於重建您的 Heritage 位址至關重要。 **如果沒有描述符，即使您有記憶詞組，也無法找到您的資金。



### 鑰匙安全性





- 如有可能，請使用 Ledger 作為主鍵
- 切勿將繼承人的判決與您自己的判決存放在同一地方
- 透過多種媒體和地點傳播資訊



### 為您的摯愛提供文件



撰寫清楚的說明，解釋復原過程的每個步驟。您的繼承人在關鍵時刻可能不熟悉 Bitcoin。



## 替代方案



還有其他解決方案可以管理您的比特幣傳輸，包括 Liana 和 Bitcoin Keeper。您可以在下面找到我們的教學：



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## 總結



Heritage 可讓您透過桌面應用程式，以主權方式規劃 Bitcoin 的繼承。執行時需要深思熟慮適當的時間範圍，並確保機密安全。別忘了傳承給您的繼承人：




- 其 12 個字的助記詞組
- 描述符備份檔案
- 復原指示



## 資源





- [Heritage 官方網站](https://btc-heritage.com)
- [文件 CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)