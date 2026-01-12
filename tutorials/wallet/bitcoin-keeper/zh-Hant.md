---
name: Bitcoin Keeper
description: Bitcoin 移動式 wallet 用於安全，而 multi-sig
---

![cover](assets/cover.webp)



對於任何意識到金融主權利害關係的持有者而言，比特幣的安全管理是一項重大挑戰。在行動 wallet 的簡易性與 multi-sig 解決方案的穩健性之間，對許多使用者而言，技術上的差距似乎令人望而生畏。Bitcoin Keeper 正是定位在這個交叉點上，提供一種循序漸進的安全方法，隨著使用者的發展而發展。



Bitcoin Keeper 是一個開放原始碼的行動應用程式，專門用於 Bitcoin，由 BitHyve 團隊開發。它的目標是讓進階的投資組合管理成為可能，尤其是多重簽章配置，同時維持直覺的介面給初學者使用。該應用程式採用的口號是 「保障今日，規劃明日」，反映了其長期支援的理念。



與管理多種加密貨幣的通用型錢包不同，Bitcoin Keeper 嚴格專注於 Bitcoin。這種只針對比特幣的方式減少了潛在的攻擊面，並大大簡化了使用者體驗。此應用程式也因其原生整合最普遍的硬體錢包及其先進的 UTXO 管理功能而脫穎而出。



## 什麼是 Bitcoin Keeper？



### 理念與目標



Bitcoin Keeper 的設計是為了滿足比特幣使用者希望完全控制自己私鑰的特殊需求。該專案完全擁護 Bitcoin 的基本原則：開放和可審計的源代碼、尊重隱私和用戶主權。使用此應用程式不需要註冊或個人資訊，甚至可以離線執行簽章作業。



其核心目標是提供一個靈活、經得起未來考驗的工具，藉由繼承功能，將 BTC 儲存數年，甚至數代。此應用程式可讓使用者從簡單的行動 wallet 開始，逐漸發展為更安全的多重簽章解決方案。



### 應用程式架構



Bitcoin Keeper 圍繞兩個截然不同的概念組織資金管理。**Hot Wallet** 是簡單的單一鑰匙 wallet，儲存在手機上，專為日常支出和少量金額所設計。金庫**是需要多個鑰匙授權支出的多簽名（Multi-Key）保險箱，專為長期安全儲存而設計。



### 主要功能



Bitcoin Keeper 支援市面上幾乎所有的硬體錢包：Coldcard、Trezor、Ledger、Keystone、BitBox02、Jade、Seedsigner、Passport 和 Coinkite 的 Tapsigner。根據裝置的不同，整合方式也不同：QR 掃描、NFC 連線或檔案匯入。



此應用程式也提供進階的 UTXO 管理功能，包括交易標籤、傳送時手動選擇輸入的投幣控制，以及部分簽章交易的 PSBT 格式支援。



## 安裝與初始設定



Bitcoin Keeper 在 Android 上可透過 Google Play 商店免費下載，在 iOS 上則可透過 App Store 免費下載。列出的發行商為 BitHyve。安裝前，請確定您的裝置沒有惡意軟體、已更新，且未經 root 或越獄。



首次啟動時，應用程式會要求您建立安全 PIN 碼。此密碼可保護 wallet 的存取權，並為本機的敏感資料加密。選擇一個強大的密碼並將其記住。然後您可以啟動生物辨識驗證 (指紋或 Face ID) 以加快解鎖速度。



![Installation et configuration du PIN](assets/fr/01.webp)



應用程式隨後會顯示幾個介紹畫面，解釋其三大支柱：創建 wallet 以傳送和接收比特幣、與硬體 wallet 相容的金鑰管理，以及傳承比特幣的傳統規劃。按下「Get Started」，然後選擇「Start New」來建立新的配置。



![Écrans d'introduction](assets/fr/02.webp)



## 發現介面



Bitcoin Keeper 的介面以四個主要索引標籤為主，可從底部的導覽列存取：



![Les quatre onglets de l'application](assets/fr/03.webp)



錢包**標籤顯示您的錢包及其餘額。這是您存取您的錢包以發送和接收比特幣的地方。標籤 "Hot Wallet 「和 」單鑰匙 「或 」多鑰匙 "可讓您快速識別每個 wallet 的類型。



鑰匙**標籤集中管理您的簽名鑰匙。您可以在這裡找到應用程式產生的行動金鑰，以及所有從硬體錢包匯入的金鑰。這也是您新增簽章裝置的地方。



**Concierge** 標籤提供支援服務：向支援團隊提交問題，並與 Bitcoin 顧問聯繫以獲得個人化協助。



透過 **More**（更多選項）標籤，可以存取個人伺服器連線、金鑰備份、繼承文件、顯示偏好設定和 wallet 管理等設定。



## 連接至您自己的伺服器



為了加強您的機密性，Bitcoin Keeper 讓您可以將應用程式連接到自己的 Electrum 伺服器，而不是使用預設的公共伺服器。



![Configuration du serveur Electrum](assets/fr/04.webp)



從「更多」標籤向下捲動，找到伺服器設定。按「新增伺服器」設定新連線。您可以選擇「Public Server」（預設的公共伺服器）或「Private Electrum」（您自己的伺服器）。



對於私人伺服器，請輸入 URL（例如 Umbrel 節點的 umbrel.local）和連接埠號碼（通常為 50001）。如果您的伺服器支援 SSL，請啟動 SSL。您也可以掃描設定 QR 碼。輸入參數後，按下「連線至伺服器」。



如果您還沒有自己的 Bitcoin 結，請看看我們的 Umbrel 教學，這是一種簡單又經濟實惠的方法，可以讓您旋出自己的結：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## 接收比特幣



從錢包標籤中，按下 wallet，選擇您要接收資金的 wallet。wallet 螢幕會顯示餘額和三個動作按鈕：發送 Bitcoin、接收 Bitcoin 和檢視所有硬幣。



![Réception de bitcoins](assets/fr/05.webp)



按下「接收 Bitcoin」。Bitcoin Keeper 會以 Bech32 格式產生新的接收地址 (以 bc1...開始)，並附上 QR 碼。您可以在此地址中加入標籤，以識別資金來源。透過顯示 QR 碼或複製文字位址，與寄件者分享位址。



每次接收時，應用程式都會自動產生一個新地址，保護您的隱私。必要時可使用「取得新 Address」取得空白地址。



## UTXO 管理



Bitcoin Keeper 可完全查看構成您餘額的 UTXO（未使用的交易輸出）。在 wallet 畫面中，按下「檢視所有硬幣」以存取角落管理員。



![Gestion des UTXO](assets/fr/06.webp)



管理硬幣」畫面會逐一列出每個 UTXO 的數量和標籤。此檢視可讓您追蹤硬幣的來源並加以整理。您可以透過「選擇傳送」選擇特定的 UTXO，與硬幣控制一起傳送，從而避免不同產地的硬幣混在一起。



## 發送比特幣



若要傳送，請選取來源組合，然後按「傳送 Bitcoin」。輸入目的地地址（貼上或透過 QR 碼掃描），並可選擇新增標籤以識別收件人。



![Envoi de bitcoins](assets/fr/07.webp)



下一個畫面允許您輸入要發送的金額。介面會顯示您的可用餘額和法幣換算。選擇充值優先順序：Low（經濟級，~60 分鐘）、Medium 或 High（優先級）。即時顯示以 sats/vbyte 為單位的估計費用。按「傳送」繼續。



![Confirmation et envoi](assets/fr/08.webp)



摘要畫面會顯示所有詳細資訊：wallet 來源、目的地位址、交易優先順序、網路費用、傳送金額和總計。請仔細檢查這些資訊，因為 Bitcoin 交易是不可逆轉的。按「確認並傳送」即可傳送交易。



會出現「傳送成功」確認，並顯示完整的摘要。在「最近交易」歷史記錄中可看到交易及其標籤。



## 儲存您的鑰匙



備份您的恢復金鑰是關鍵的一步。從「更多」標籤移至「備份與復原」部分，然後按一下「復原金鑰」。



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



螢幕會顯示您的備份狀態。若要驗證您的備份，應用程式會要求您確認短語中的特定單字 (例如第 7 個單字)。此驗證可確保您正確寫下復原短語。



在「密鑰回復設定」中，您可以透過「檢視密鑰回復」檢視完整的詞組，並查看密鑰的簽名者指紋。請將您的 12 字短語儲存在紙張上，放在安全的地方，遠離濕氣和火源。切勿將其儲存在連接的裝置上。



## 新增外部鑰匙 (wallet 硬體)



Bitcoin Keeper 的主要資產之一是整合硬體錢包。從「金鑰」標籤，按「新增金鑰」即可新增簽章裝置。



![Ajout d'une clé hardware](assets/fr/10.webp)



選擇「從硬體新增鑰匙」以連接硬體 wallet。本應用程式支援多種裝置：BitBox02、Coldcard、Blockstream Jade、Keystone、Krux、Ledger、Foundation Passport、TwentyTwo Portal、Seedsigner 和 Specter Solutions。



### Tapsigner 配置



Tapsigner 是 Coinkite 推出的 NFC 卡，特別適用於行動裝置。如果您想瞭解更多，我們有專門的教學：



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

若要新增 Tapsigner，請從硬體錢包清單中選取。



![Configuration du Tapsigner](assets/fr/11.webp)



首先輸入印在卡片背面的 6-32 位數 PIN 碼（新卡片的預設值），如果已經設定，則輸入您的 PIN 碼。按 "Proceed「（繼續），當顯示 」Ready to scan"（準備掃描）時，將 Tapsigner 靠近您的手機背面。NFC 通訊會自動匯入公開金鑰。然後您可以加入描述 (例如「Métro Card」) 來識別此金鑰。



## 建立多重組合



設定好金鑰後，您就可以建立結合數個裝置的多重簽章 wallet。從錢包標籤，點選「新增 Wallet」。



![Création d'un nouveau wallet](assets/fr/12.webp)



您有三個選項：針對新的組合，選擇「建立 Wallet」；針對共用儲存庫，選擇「匯入 Wallet」以還原現有的 wallet；或選擇「協作 Wallet」。選擇「建立 Wallet」，然後選擇「Bitcoin Wallet」。



![Sélection du type de wallet](assets/fr/13.webp)



下一個畫面提供不同的配置：「單鍵」、「2 of 3 多鍵 」或 「3 of 5 多鍵」。若要自訂 multi-sig，請按「選擇自訂設定」。例如，選擇 "1 of 2"：需要從兩個可能的按鍵中選取一個簽名。



然後選擇組成您的 Vault 的鑰匙。在我們的例子中，我們將 "Mobile Key「（手機軟體鑰匙）和 」TAPSIGNER"（Metro Card）結合在一起。這種配置提供了備援功能： 如果其中一把鑰匙無法使用，您可以使用另一把鑰匙來使用您的資金。



![Finalisation du wallet multisig](assets/fr/14.webp)



命名您的 wallet（例如 "Test PlanB"），添加可選的描述，並勾選選定的按鍵。按下「建立您的 Wallet」。出現「Wallet 已成功建立」確認訊息，提醒您儲存 wallet 復原檔案。



您的新多重密碼 wallet 現在會出現在錢包標籤中，標籤為「多重鑰匙」，並顯示「1 of 2」。



### 儲存組態檔案



**wallet multisig 與簡單的 wallet 不同，簡單的 wallet 只需恢復短語即可恢復存取權限，而 wallet multisig 則還需要配置檔案來描述保險箱的結構 (哪些金鑰參與，需要多少簽章)。如果沒有這個檔案，即使有所有的復原詞組，您也無法重建您的 wallet。



![Export du fichier de configuration](assets/fr/15.webp)



若要匯出此檔案，請在「錢包」標籤中選取您的 wallet multisig，然後按右上角的「設定」圖示 (齒輪)。在「Wallet 設定」中，按一下「Wallet 配置檔案」。有多種匯出選項可供選擇：





- 匯出 PDF**：產生包含所有 wallet 資訊的 PDF 文件
- 顯示 QR**：顯示可掃瞄的 QR 代碼，以便將組態匯入其他裝置
- Airdrop / 檔案匯出**：透過手機的分享選項匯出檔案
- NFC**：透過 NFC 與相容裝置分享



將此設定檔與您的復原語句分開保存，最好以加密或列印的方式保存。如果您遺失了手機，此檔案與每個參與密鑰的復原短語結合後，您就可以在 Bitcoin Keeper 或任何其他相容軟體上重建 wallet 多重密碼。



## 最佳實踐



### 基金組織



根據比特幣的用途來組織您的比特幣：一個熱門的 wallet Single-Key 用於目前金額有限的支出，一個或多個 Vault Multi-Key 用於長期儲蓄。系統化的 UTXO 標籤將幫助您追蹤資金來源，這對於管理機密性和避免混合不同來源的硬幣特別有用。



保持手機安全：啟動生物特徵鎖、定期執行系統更新，並對已安裝的應用程式保持警覺。並將 Bitcoin Keeper 保持為最新的安全修補程式。



### 備份安全性



在紙張上至少保存兩份每個復原短語的副本，並儲存在不同的地理位置。對於大筆款項，可考慮使用雕刻的防災金屬。切勿將這些短語儲存在連線至網際網路的裝置上，也切勿拍攝。



對於 multi-sig 儲存庫，也請儲存配置檔案 (Wallet 復原檔案)，其中包含參與的公開金鑰和儲存庫結構。此檔案與金鑰恢復短語結合，可讓 wallet 在任何相容的軟體上重建，例如 Sparrow 或 Specter。



## 優點與限制



### 重點介紹





- 僅 Bitcoin 應用程式可降低複雜性與風險
- 本機整合多重簽章儲存庫，並提供逐步指導
- 擴充硬體 wallet 支援 (Tapsigner、Coldcard、Ledger、Jade 等)
- UTXO 和硬幣控制的進階管理
- 可連接到個人 Electrum 伺服器
- 開放、可稽核的原始碼



### 需要考慮的限制條件





- Interface 主要使用英語
- 某些高級功能 (雲端備份、輔助伺服器) 需要升級
- Multisig 配置需要初始訓練



## 總結



Bitcoin Keeper 是管理比特幣的可擴充解決方案。其漸進式方法，從簡單的熱式 wallet 到多重簽章金庫，意味著安全性可隨著需求的改變而升級。Tapsigner 等硬體錢包能夠輕易整合，為強大的配置鋪路，而不會過於複雜。



僅限比特幣的方向、開放源代碼和尊重隱私，使其成為與 Bitcoin 生態系統核心價值一致的選擇。



本教學涵蓋免費版 Bitcoin Keeper 的基本功能。該應用程序還提供高級功能（雲備份、輔助服務器備份、Canary Wallets），這將是一個專門教程的主題。在即將推出的指南中，我們還將探討繼承規劃功能，該功能可讓您準備將您的比特幣傳遞給您的親人，這要歸功於集成到應用程序中的增強金庫和隨附文件。



## 資源





- 官方網站：[bitcoinkeeper.app](https://bitcoinkeeper.app)
- 幫助中心：[help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- 原始碼：[github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)