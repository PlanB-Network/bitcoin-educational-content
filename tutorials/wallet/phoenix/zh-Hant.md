---
name: 鳳凰城
description: 安裝和使用 Phoenix Wallet
---
![cover](assets/cover.webp)


Phoenix 是由 ACINQ 開發的自我保管型 Lightning Wallet 和節點，ACINQ 是一家專門提供基於 Lightning 軟體解決方案的法國公司。與 Satoshi 的 Wallet 等託管式 Lightning 錢包（比特幣由第三方託管）不同，Phoenix 可讓使用者保留對其私密金鑰的完全控制權。


Phoenix 作為真正的 Lightning 節點嵌入您的手機，自動與 ACINQ 的 Lightning 節點開啟通道。該應用程式基於 Lightning-KMP，是 Kotlin 中 Lightning Network 的跨平台實現，針對手機錢包進行了優化。與其他 Lightning 節點解決方案不同，Phoenix 大大簡化了管理。用戶無需處理通道開啟和關閉、運行 Bitcoin 節點或管理 Lightning Network 上的流動性。Phoenix 會在後台處理所有這些技術操作。


此應用程式結合了行動 Lightning 錢包的易用性與便利性，以及真正個人 Lightning 節點的安全性與主權。Phoenix 使安全、高效、自主地使用 Lightning Network 成為可能，同時享受流暢、直觀的用戶體驗。


作為回報，需要支付一定的費用：




- 透過 Lightning 傳送的費用為金額的 0.4% 另加 4 Sats ；
- 如果需要現金透過 Lightning 收取，則收取金額的 1%；
- 開啟每個通道需要 1000 Sats。


在我看來，Phoenix 是介於託管 Lightning 投資組合和手動管理 Lightning 節點之間的一個出色的中間解決方案。這個應用程式同樣適合那些不喜歡處理管理自己的 LND 或 Core Lightning 細節的初學者和高級用戶。讓我們來看看如何使用它！


![Image](assets/fr/01.webp)


## 安裝應用程式


前往應用程式商店並安裝 Phoenix .NET Framework：




- 在 [Google Play 商店](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.Mainnet)；
- 在 [App Store](https://apps.apple.com/fr/app/phoenix-Wallet/id1544097028?l=en-GB) 上。


![Image](assets/fr/02.webp)


您也可以安裝應用程式 [使用其 GitHub 套件庫上的 apk 檔案](https://github.com/ACINQ/phoenix/releases)。


![Image](assets/fr/03.webp)


## 建立投資組合


應用程式啟動後，按一下「*下一步*」按鈕以跳過簡報，然後按一下「*開始*」。


![Image](assets/fr/04.webp)


選擇「*建立新的 Wallet*」。


![Image](assets/fr/05.webp)


就這樣，您的 Lightning Wallet 和節點就建立好了。


![Image](assets/fr/06.webp)


## 保存 Mnemonic 短語


在開始之前，我們需要儲存 12 個字的 Mnemonic 詞組。這個短語讓您可以完全不受限制地存取您所有的 bitcoins。任何擁有這個短語的人都可以盜取您的資金，即使沒有實體存取您的手機。


當您的手機遺失、被竊或損壞時，這 12 個字的短語可恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。


您可以將其寫在紙上，或者為了增加安全性，將其刻在不銹鋼上，以防止火災、水災或倒塌。Mnemonic 的媒介選擇取決於您的安全策略，但如果您將鳳凰城當作包含中等金額的消費組合，紙張應該就足夠了。


如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

按一下 Interface 頂端顯示的訊息「*儲存您的 Wallet...*」。


![Image](assets/fr/07.webp)


然後按一下「*儲存我的 Wallet*」。


![Image](assets/fr/08.webp)


然後按一下「*檢視我的鑰匙*」，並將您的 Mnemonic 詞組儲存於實體媒體上。


![Image](assets/fr/09.webp)


檢查 Interface 底部的兩個方塊，確認備份已成功完成。


![Image](assets/fr/10.webp)


## 應用程式設定


在進行第一次交易之前，您可以按一下 Interface 左下方的齒輪圖示，自訂設定。


![Image](assets/fr/11.webp)


在「*顯示*」功能表中，您可以選擇應用程式主題、Bitcoin 使用的面額，以及您的當地法定貨幣。


![Image](assets/fr/12.webp)


在 「*付款選項*」中，您可以找到 Lightning 付款的各種進階設定。您可以保留預設設定。


![Image](assets/fr/13.webp)


在 「*通道管理*」中，設定開啟 Lightning 通道時您準備支付的最高費用。


![Image](assets/fr/14.webp)


在 「*存取控制*」功能表中，我強烈建議您啟動一個認證系統，以確保您手機上應用程式的存取安全。這將防止任何有權進入您未鎖定手機的人進入 Phoenix 並竊取您的比特幣。


![Image](assets/fr/15.webp)


在「*Electrum 伺服器*」功能表中，如果您有 Electrs 伺服器，您可以連接它來廣播您的交易。


![Image](assets/fr/16.webp)


要提高連接的保密性，請在 "*Tor*"菜單中啟用通過 Tor 進行連接。雖然使用 Tor 可能會稍微拖慢您的付款速度，而且接收時需要在前台開啟 Phoenix 應用程式，但它會大幅增加您的隱私。


![Image](assets/fr/17.webp)


## 接收比特幣 On-Chain


首次使用時，您可以選擇用On-Chain資金充值您的Phoenix Wallet。您也可以直接從 Lightning 進行首次存款（請參閱下一節），但無論哪種情況，開通第一個通道都需要支付額外費用。


按一下「*接收*」按鈕。


![Image](assets/fr/18.webp)


掃描右側的 QR 代碼，顯示接收 Address 的 Bitcoin。將您希望存入 Phoenix 的金額傳送給它。


![Image](assets/fr/19.webp)


On-Chain 收到的金額首先會在您的投資組合餘額下顯示為待定。資金需要經過 3 次確認才能使用。


![Image](assets/fr/20.webp)


收到資金後，Phoenix 會自動為您開啟一個 Lightning 通道。現在您可以透過 Lightning Network 傳送和接收比特幣了。


![Image](assets/fr/21.webp)


## 透過 Lightning 接收比特幣


若要透過 Lightning Network 接收 Sats，請按一下「*接收*」按鈕。


![Image](assets/fr/22.webp)


Phoenix 會產生一個 Lightning Invoice。您可以掃描它，或是將它寄給希望將 Sats 轉移給您的人。


![Image](assets/fr/23.webp)


按一下「*編輯*」按鈕，您可以新增付款人在 Invoice 上可以看到的說明，並定義付款人必須寄送的特定金額。


![Image](assets/fr/24.webp)


上述經典發票只能使用一次。若要選擇可重複使用的付款方式，您可以使用可重複使用的 QR 代碼，這是 BOLT12 的優惠。


![Image](assets/fr/25.webp)


一旦 Invoice 或 BOLT12 報價結算，交易就會顯示在您的 Lightning Wallet 上。


![Image](assets/fr/26.webp)


## 透過 Lightning 傳送 bitcoins


現在您已在 Phoenix 上安裝 Sats，您已準備好透過 Lightning Network 進行付款。首先按一下「*送出*」按鈕。


![Image](assets/fr/27.webp)


有多種選項可供您選擇。點擊 「*掃描 QR 代碼*」，您可以掃描 Lightning Invoice、BOLT12 報價，甚至是接收 Address 以進行 On-Chain 付款。


![Image](assets/fr/28.webp)


您也可以透過鍵盤在 Interface 頂端的欄位中手動輸入這些資訊，或是輸入 Lightning Address（BOLT12 或 LNURL）。您也可以使用「*Paste*」按鈕直接貼上資訊。


![Image](assets/fr/29.webp)


在這個範例中，我掃描了一個 Invoice 換取 10,000 Sats。要付款，只需點擊 "*Pay*"。


![Image](assets/fr/30.webp)


交易完成。


![Image](assets/fr/31.webp)


恭喜您，現在您知道如何設定和使用 Phoenix 了。如果您覺得本教學有用，請在下方留下 Green 拇指。歡迎在您的社交網路分享這篇文章。感謝您的分享！


若要更進一步，請參考 Alby Hub 的教學，這是另一個創新且易於使用的解決方案，可讓您啟動自己的 Lightning 節點：


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

若要瞭解更多關於 Lightning Network 的技術操作，您可以在 Plan ₿ Network 上找到 Fanis Michalakis 優秀的免費訓練：


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb