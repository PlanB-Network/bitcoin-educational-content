---
name: Wallet of Satoshi - 自行保管
description: 瞭解如何設定 Wallet of Satoshi 組合的自保管模式
---

![cover](assets/cover.webp)



*** 不是你的鑰匙，就不是你的錢幣* 不只是一句說話，而是 Bitcoin 的基本原則，也就是說，如果你無法控制解鎖比特幣的 ** 私密鑰匙**，你就無法真正擁有它們。



許多使用者通常一開始使用 ** 監護 wallet**，然後轉換到 ** 自行監護 wallet**，由他們自行控制私密金鑰。


在本教程中，我們將不會為您介紹全新的自我監護 wallet。相反地，我們會向您介紹 ***Wallet of Satoshi*** wallet 的一項新功能： **自監控模式**。



這項新整合的目的是讓使用者能夠保留對其私人金鑰的控制，同時受益於簡易性和流暢的使用者體驗。



在進入核心問題之前，讓我們先來檢視一下 Wallet of Satoshi (WoS) 所提供的特殊自我監護模式。



## 自行保管模式的特點



WoS 自托管模式的簡單性和流動性消除了打開 Lightning 通道、管理節點的複雜性...但這怎麼可能呢？



Wallet of Satoshi 的自我保管模式由 **Spark** 提供。這是 Lightspark 使用 **statechains** 技術為 Bitcoin 打造的 Layer 2 解決方案。



因此，您不會直接在 Lightning Network 上進行交易。**LN**網路與**Spark**之間的互動是透過**原子交換**進行。



例如，Bob 希望使用 WoS 支付 Lightning 發票。他轉移他的 satoshi，但在後台，這些 satoshi 會被路由到 Spark 上的 **Spark Service Provider (SSP)**，再由 SSP 在 Lightning 網路上執行付款。



相反，Alice 希望直接從其 WoS 投資組合中獲取資金。在這種情況下，**SSP** 會透過 LN 接收 sats，並立即存入 Alice 的投資組合。



因此，需要注意的是，要從 WoS 的簡單性及流動性中獲益，您需要依賴 Spark 的伺服器。然而，就安全性而言，如果 SSP 變得惡意或不可用，您有**單邊退出**機制，這項安全措施允許您在 Bitcoin on-chain 上收回您的資金 (即使這可能會很緩慢且成本高昂) , 保證與私人 Lightning 節點相媲美的自我監護體驗。



考慮到所有這些參數，您就可以決定要在 WoS 自保管中保留多少 sats。



如果您是 Wallet of Satoshi 的新使用者，自然需要下載行動版 wallet 應用程式。不過，如果您已經在使用，而且想知道如何使用 ** 自我監護模式**，請直接前往本教學的 ** 自我監護模式設定** 章節。



## 開始使用 Wallet of Satoshi



前往您的應用程式商店下載 WoS。



![screen](assets/fr/03.webp)



下載完成後開啟應用程式，然後按下 **Start**。



![screen](assets/fr/04.webp)



您將被重定向到應用程序的主介面。事實上，當您首次進入 WoS 時，投資組合已經運作，並預設以託管模式系統開啟。



![screen](assets/fr/05.webp)



即使您不想在託管模式下使用 WoS，我們也建議您先進行設定。要這樣做，請參閱本教程。



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

接下來讓我們來看看 WoS 在自我監護時的配置。



## 自我監護模式配置



按一下主介面右上角的漢堡包功能表 (3-bar圖示)。



![screen](assets/fr/06.webp)



然後在出現的功能表中，按一下 ** 開啟自我監護 Wallet** 子功能表。



![screen](assets/fr/07.webp)



WoS 會立即告訴您 * 自行保管模式附有復原短語。此外，您必須自行負責您的資金安全*。



![screen](assets/fr/08.webp)



勾選「**我了解**」按鈕 (1)，然後按下**開啟自行保管 Wallet** 按鈕 (2)，此按鈕顯示為亮黃色。



![screen](assets/fr/09.webp)



### 建立自我監護組合



按一下 ** 開啟自行保管 Wallet** 按鈕後，按一下 ** 建立新 Wallet** 按鈕。



![screen](assets/fr/10.webp)



WoS 將為您建立自我監護組合，同樣也是在同一個應用程式中。您可以在方便的時候隨時切換**監護**模式（某些地區提供）和**自我監護**模式。



![screen](assets/fr/11.webp)



創建後，您將被轉到 WoS 自行保管的主介面。您會發現，WoS 託管投資組合與 WoS 自行託管投資組合的總覽和介面並無差異。



### 儲存您的助記詞組



點選位於螢幕上方 Wallet of Satoshi 名稱與漢堡選單之間的 **Keychain + Backup Wallet** 圖示。



![screen](assets/fr/12.webp)



WoS 提供兩種不同的方式來儲存您的 12 個單字 (助記詞組)： **透過 Google Drive 備份**和**手動備份**。



雖然我們建議您使用最安全的手動備份，但我們也會教您如何透過 Google Drive 備份。



#### 透過 Google Drive 備份



按一下 **Google Drive Backup** 按鈕。



![screen](assets/fr/13.webp)



如果您選擇使用 Google Drive 備份，您的 Google 帳戶很有可能會外洩。惡意個人將可存取包含您的 12 個字的檔案，進而取得您的 wallet。



加入密碼來加密包含您的 12 個單字的檔案，當然是增加額外安全層級的好方法。



因此，請在進階選項中啟動 ** 使用密碼加密** 按鈕。



![screen](assets/fr/14.webp)



在出現的新介面上，設定一個強密碼，然後再確認一次。



![screen](assets/fr/15.webp)



重要的是要記住，一旦您選擇了密碼，就一定不能忘記或丟失寫密碼的媒介。如果您忘記或遺失了密碼，您將永遠無法存取您的 12 個字，因此也無法存取您的資金。



選擇密碼後，選擇一個 Google 帳戶進行備份，然後授權給 WoS 所需的存取權限。



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



等待幾秒鐘。賓果！您的備份已成功完成。



![screen](assets/fr/18.webp)



您總是可以選擇第二種備份方法來進行額外的備份：手動備份。


#### 手動備份



如果您選擇手動備份，我們強烈建議您參考本教程，其中探討了安全備份您的助記語句的最佳做法，這樣您就不會失去對比特幣的存取權。



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

按下 **Manual Backup** 按鈕。



![screen](assets/fr/19.webp)



在接下來的介面上，WoS 會提醒您在進行手動備份之前要注意的幾項安全預防措施。



啟動 ** I understand** 按鈕，然後按下 **Next** 按鈕。



![screen](assets/fr/20.webp)



接下來您會看到 12 個單字。儲存它們，然後按下**下一步**按鈕。



![screen](assets/fr/21.webp)



在這個新介面上，按照正確的順序按下單字。



![screen](assets/fr/22.webp)



最後，按一下**下一步**按鈕。恭喜您！您的備份現已完成。



![screen](assets/fr/23.webp)



## 自我保管組合恢復



當您在更換電話或其他原因後，想要復原或還原您的 WoS 自行保管 wallet 時，請遵循以下步驟。



若要開啟 WoS 投資組合，請點選主介面右上角的漢堡選單。


在出現的功能表中，按一下 ** 開啟自行保管 Wallet** 子功能表。


在出現的新介面上，按下 **Restore Existing Wallet** 按鈕。



![screen](assets/fr/24.webp)



選擇還原方法並進行下一步。



![screen](assets/fr/25.webp)



### 透過 Google Drive 還原



1.按下 **Restore From Google Drive** 按鈕。


2.選擇 Google 帳戶，並讓 WoS 擷取儲存在 Google Drive 上的復原資料。


3.然後從包含 12 個單字的檔案中輸入您的加密密碼（當然，如果您之前已定義過密碼）。


4.請稍等片刻讓還原生效，然後您就可以再次存取您的投資組合。



### 手動修復



1.按下 **Restore Manually** 按鈕。


2.然後輸入 12 個記憶詞組的單字，將每個單字寫在起始數字前面。


3.請稍等片刻讓還原生效，然後您就可以再次存取您的投資組合。




### 在 WoS 託管和 WoS 自行託管之間轉移 bitcoins



當您的 WoS 託管 wallet 中有比特幣 (sats) 並建立了 WoS 自託管 wallet，您的資金就不會流失。更好的是，您可以將它們轉移到您的自保管投資組合中，反之亦然。



要做到這一點：


您可以複製您的閃電 WoS 自行保管地址或您建立的發票。



![screen](assets/fr/26.webp)



現在打開您保管的 wallet，然後按下 **Envoyer** 按鈕。



然後貼上地址或發票。第二次按下 **Envoyer**。



回到您自行保管的投資組合，您會發現您確實收到了資金。



![screen](assets/fr/27.webp)



## 發送和接收比特幣



至於在自我託管模式下傳送和接收比特幣，就像一般的概述和介面一樣，它們和透過 WoS 託管 wallet 傳送和接收比特幣沒有什麼不同。



請參閱在 Plan₿ 網路上使用 Wallet of Satoshi 的基本教學。



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

現在您可以在自監控模式下自行設定和操作 Wallet of Satoshi。



如果您覺得本教程有用，請在下方給我留下綠色拇指。非常感謝