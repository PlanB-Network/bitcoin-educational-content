---
name: BitcoinVoucherBot P2P
description: 如何使用 BitcoinVoucherBot 買賣 Bitcoin P2P
---

![image](assets/cover.webp)



我們仍然聽到BitcoinVoucherBot，一個Telegram機器人的創建，通過SEPA銀行轉帳購買Bitcoin無[KYC](https://planb.academy/resources/glossary/kyc-know-your-customer)。不幸的是，自 2025 年 11 月起，集中形式的 BitcoinVoucherBot 已不再提供無需 KYC 的服務。



在本指南中，我們將探討新的實作方式，讓使用者可以直接在新的 P2P (Peer-To-Peer) 市場上買賣 Bitcoin，因此不需要 KYC。為了對抗日益威脅數位自由和隱私的新限制，開發人員創造了這個擴充功能，讓使用者可以透過 P2P (Peer-To-Peer) 以高度匿名的方式買賣 Bitcoin。讓我們一起看看這種新的交換方式是如何運作的。



要使用這項服務，您必須透過 Lightning Network 進行轉帳。因此，請確保您的 wallet 支援此通訊協定，並允許您使用「LNURL」或「Lightning Address」來接收和傳送資金。



在支援的錢包中，我們可以找到





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodial with swap to Non-Custodial)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



或任何具有「Lightning Address」並產生 Bolt11 發票的 wallet。目前不支援 generate 具有 Bolt12 發票的錢包。如需詳細資訊，請參閱 [Bolt](https://planb.academy/resources/glossary/bolt) 的定義。



在本教程中，鑒於其易於立即使用，我們將採用 Wallet of Satoshi。



**注意**：Wallet of Satoshi 雖然在初學者中很受歡迎，但它是託管式的，對資金的控制有限；只能暫時使用，請立即轉換為非託管式以獲得完全的主權。自 2025 年 10 月起，它在 iOS/Android 上包含全球穩定的自我保管模式（更新應用程式），具有自主私鑰、模式間切換、自訂 Lightning 位址和 seed 12 字元備份。不過，在鞏固之前，它仍是一個臨時解決方案，長期管理上還是偏好 wallet 非保管式的成熟方案。



非常好！現在我們可以開始我們的旅程，這將引導您逐步建立您的帳戶、管理購買和銷售匹配，以及使用您的限制區域。



## Wallet 和註冊



首先，如果您的智慧型手機尚未安裝，請下載 Wallet of Satoshi。





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



如果您從未使用過 Wallet of Satoshi，並想要瞭解其運作方式，我建議您遵循本教學，以便正確啟用 Wallet of Satoshi，並安全備份。



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

現在您的 wallet 已經準備就緒，您可以開始發送少量的 sats。請記住，為了完成您的 P2P (Peer-To-Peer) 平台註冊，您需要發送 1000 個 sats 作為控制措施：這是為了建立一道屏障，防止任何虛擬匹配（詐騙）類型的攻擊，防止任何人在沒有任何垃圾郵件過濾器的情況下進行註冊。



![image](assets/it/02.webp)



我們現在可以打開P2P（Peer-To-Peer）平台進行註冊。您可以從桌上型電腦或智慧型手機上的瀏覽器登入，透過 Telegram BitcoinVoucherBot 或 .onion 連結來提供更高的隱私度。



如果您選擇使用 Tor .onion 連結，我也建議您使用「Tor Browser」。如果您還不知道它，您可以在這個連結了解更多資訊：



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

現在選擇您要如何到達平台。





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [PC 桌面 / 瀏覽器 智慧型手機](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



您將被重定向至主頁面。



按下「Get Starter」立即開始使用



![image](assets/it/03.webp)



在下一個畫面中，您必須選擇一個密碼並輸入（方格 A），然後重複輸入（方格 B）。我建議您立即將這個密碼儲存到備份媒體，可以是安全的數位裝置，例如「Bitwarden」：



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

或將您的密碼儲存在紙張介質上（**警告**：這不是一個好的解決方案，但如果是作為臨時解決方案，也是可以的）。



勾選說明您不是機器人的驗證方塊（方塊 C）。請注意 請勿啟用 RSA 加密，除非您確實知道它是什麼以及如何運作。在此階段您不需要做任何事情。按一下「產生頭像」（"Generate Avatar"）（方格 D）。



![image](assets/it/04.webp)



現在您必須支付 1000 sats 以完成註冊。



1.從頂部開始，首先看到您隨機產生且極為重要的 "Avatar ID"。請小心保存，就像我建議您保存密碼一樣。


2.然後，您必須在下面的欄位中輸入您的 "Lightning Address"。如果您購買 Bitcoin，這將允許您接收付款，或獲得退款。如果您使用的是 Wallet Of Satoshi，您可以點擊接收來複製您的 Address。


3.勾選您聲明自己不是機器人的驗證方塊。


4.支付 1000 sats 以進入您的限制區。如果您無法框選，請用滑鼠點選（在電腦上）或用手指點選（在瀏覽器/Telegram 智慧型手機上），複製您需要貼到 Wallet of Satoshi 的地址，並完成發票付款。



![image](assets/it/05.webp)



這是您的 LNURL Address。



![image](assets/it/06.webp)



恭喜您！!您已經永久建立了您的頭像，您可以在這裡檢視摘要。我再次建議您小心保存您的 「頭像 」和密碼，正如我之前所建議的。



按一下 `I've saved my credentials, continue` (翻譯為：「我已儲存我的憑證，請繼續」)



![image](assets/it/07.webp)



現在您已進入平台的中心，在這裡您可以查看所有交易匹配及其詳細資訊。為了讓您看得更清楚，下面您可以從桌上型電腦看到網站內固有的圖片。





- 「類型」（"Type「）定義了是 」賣出"（"Sell「）銷售還是 」買入"（"Buy"）購買
- 「金額」（"Amount「）：如果匹配屬於 」賣出 「類型，則表示使用者要賣出多少 sats；如果匹配屬於 」買入 "類型，則表示使用者願意買入多少 Bitcoin。
- 「含保證金的 BTC 價格」(」BTC Price with Margin")：顯示價格時考慮了標記值上方應用的保證金。
- 「保證金」（"Margin"）是應用在市價上的百分比，如果是負號 (-)，您會在市價上獲得折扣，如果是正號 (+)，則會在市價上獲得溢價。
- 「方法」（"Method"）表示用戶偏好的付款方式。
- 「創造者」是使用者在平台上使用的獨特頭像。
- "Rep" (信譽) 使用者的信譽等級從 -5 不可靠到 +5 非常可靠。
- 「狀態」（"Status"）：表示匹配的狀態。在範例截圖中，所有的匹配都顯示為 「開啟」（"Open"）。
- 「過期」（"Expiration"）：顯示距離比賽過期還剩多少時間，如果沒有人選擇，比賽就會取消。



![image](assets/it/08.webp)



在右上方按一下您的頭像以存取您的個人資料。



![image](assets/it/09.webp)



在這裡您可以看到您的虛擬人像名稱、使用者 ID、建立日期和聲望，這些都會對您在談判中的行為產生正面或負面的影響。



![image](assets/it/10.webp)



在「設定」部分，您可以檢視註冊時輸入的「Lightning Address」，並在必要時進行變更。您也可以選擇建立公開金鑰，如前所述，只有在您具備適當技能的情況下才能建立公開金鑰。它是用來加密您直接從電腦與對方交換的訊息。



強烈建議使用 Telegram 通知功能。啟動此功能後，會出現一個 QR 代碼，可讓您將其與 Telegram 應用程式相結合：如此一來，您就能直接在 Telegram 的機器人聊天室中，即時收到與您的比賽相關的所有動作通知。



![image](assets/it/11.webp)



最後，您會發現您的推薦區塊，裡面有您所邀請的使用者所產生的收入。在這裡，您可以使用按鈕分享您的連結或 QR 代碼，再往下一點，您可以檢視匹配清單，追蹤您的聲譽以及相對應的分數。



![image](assets/it/12.webp)



## 建立訂單以購買 Bitcoin



進入市場：從主導覽列，按一下購物車符號「市場」("Marketplace「) 來開啟訂購簿。然後開始新訂單：按下「新訂單」按鈕 (」New Order")，開始處理。



![image](assets/it/13.webp)





- 設定訂單詳細資料：
- 選擇選項 「購買 Bitcoin」("Buy Bitcoin")。
- 輸入您想要的 sats 數量。
- 定義價格邊際（與市值相差 -20% 到 +20%）。
- 選擇付款方式（即時 SEPA 等）。
- 表示首選貨幣。
- 確認訂單：按一下「建立訂單」(「確認訂單」) 進入申請階段。



![image](assets/it/14.webp)



需支付訂金：啟動訂單需支付相等於總金額 10% 的訂金，另加服務費。




- 訂金支付：訂單建立時，系統會自動產生一張 Lightning 發票。訂金只是臨時性的，當訂單完成後會退還。
- 主要功能：
- 保證金：訂單價值的 10%。
- 服務費：使用平台的費用。
- 時間限制：您有 5 分鐘時間付款，否則交易失效。



![image](assets/it/15.webp)



付款成功後，該訂單將出現在賬簿中，所有用戶都可以看到，用戶可以選擇並接受該訂單。要建立賣出訂單，您只需點擊 「賣出 Bitcoin」（"Sell Bitcoin"），輸入您要賣出的 satoshi 數量，設定保證金，選擇付款方式和貨幣，然後進行 10% 的保證金作為押金。完成後，您的配對將會在清單中顯示。



![image](assets/it/16.webp)



## 如何接受訂單



1.賣家可以看到書中所有可用訂單的清單。


2.檢查詳細資料：每張訂單都會顯示下列資訊：




  - Bitcoin 的數量、
  - 價格邊際利潤、
  - 付款方式、
  - 使用者口碑。



![image](assets/it/17.webp)



3.按一下訂單，即可開啟包含所有資訊的完整工作表。


4.按下「出售 Bitcoin」(「出售 Bitcoin」) 接受建議。



![image](assets/it/18.webp)



## 賣家要求的訂金



訂單被接受後，系統會產生一張付款發票。訂金包括



- 訂單總金額、



- 服務委員會。



訂金必須在規定的時限內支付，否則交易將不予確認。



![image](assets/it/19.webp)



## 傳送付款指示



存款完成後，交易會出現在賣家的個人儀表板上，賣家必須提供詳細資料給買家，才能完成法幣付款。



1.賣家會在其面板中顯示進行中的交易。


2.按一下「提交付款指示」。


3.輸入法幣付款的所有必要資訊（IBAN、收款人、地址、付款原因等）。


4.按一下「傳送訊息」("Send Message")，將資料傳送給買方。



![image](assets/it/20.webp)



## 付款程序



買方會在平台聊天中收到一則包含所有必要資料的訊息，以便以法定貨幣付款：




- 銀行詳細資料：IBAN 以及賣方帳戶持有人的姓名和地址。
- 精確金額：要轉移的精確法幣金額。
- 因果/描述：要包含在交易中的文字。
- 時限：完成付款的最後期限。



轉帳在 P2P 系統之外進行，必須透過個人的銀行機構進行。



⚠️ **重要說明：** 只有在您透過銀行實際安排轉帳或法幣付款後，才能在平台上進行確認。



![image](assets/it/21.webp)



## 確認付款方式



這一步驟對買家來說非常重要，應該在確認付款已經寄出後才執行。



1.接收資料：買方已收到賣方的付款指示。


2.付款執行：從個人銀行帳戶安排法幣轉帳。


3.驗證：檢查操作是否已正確處理。


4.在平台上確認：點擊交易頁面上的 "Confirm fiat payment"(「確認法幣支付」)。


確認付款」按鈕會出現在交易部分，只有在確認付款確已寄出後才可使用。



![image](assets/it/22.webp)



流程的最後一個步驟是賣方確認收到法定貨幣付款，之後會將沙特貨幣發放給買方。



![image](assets/it/23.webp)



## 總結



希望這篇教學能幫助您使用新的方法來交易比特幣，甚至只是購買比特幣，無論是為了自己的價值儲存，或是開始將日常支付帶入生活。不過，要應付我們的數位世界即將發生的事情，這仍然是一扇需要探索的門。



控制我們的機構所套的繩子越來越緊，誕生了一個越來越受控制的網際網路。透過購買 P2P，您可以完全匿名，不留任何痕跡，也不會受到第三方的後續影響。