---
name: SMS4Sats
description: 以 Bitcoin Lightning 付款，匿名收發簡訊
---

![cover](assets/cover.webp)



SMS 驗證已成為許多線上服務的必備功能。無論是在平台上建立帳號、驗證註冊或確認身份，網站幾乎都有系統地要求輸入電話號碼。這種普遍的做法對任何希望保護個人隱私的人來說都是一大問題：您的個人號碼會成為一個永久性的識別碼，將您的各種數位活動與您的真實身分連結起來，並為不想要的商業邀約大開方便之門。



**SMS4Sats**針對這個問題，提供可接收和傳送簡訊的臨時電話號碼。這項服務的特色在於其免註冊模式以及透過 Lightning Network 獨家支付 Bitcoin。只需支付幾個銅子，您就可以獲得一個一次性號碼，讓您可以在不透露個人號碼的情況下驗證註冊。



本教學引導您使用 SMS4Sats 的三項功能：接收驗證簡訊、傳送匿名簡訊，以及租用臨時號碼數小時。



## 什麼是 SMS4Sats？



SMS4Sats 是可在 [sms4sats.com](https://sms4sats.com) 上存取的線上服務，可透過 Bitcoin Lightning 付款進行匿名簡訊管理。該服務提供三種不同的功能：接收單次使用的驗證碼、發送簡訊至任何號碼，以及租用臨時號碼數小時。



### 理念與營運模式



該專案的設計旨在確保最大程度的機密性和財務主權。SMS4Sats 不需要建立帳戶，只接受 Bitcoin Lightning 付款，因此完全不需要提供個人資料。不需要電子郵件地址、信用卡或個人資料。只需使用 Lightning 付款即可使用服務。



這項服務支援約 120 個國家的 400 多個網站和應用程式，涵蓋大多數常見的驗證需求。如此廣泛的地理涵蓋範圍，可驗證從社交網路到訊息服務等各種平台上的註冊。



### 有條件付款模式



SMS4Sats 的 SMS 接收功能使用有條件的 Lightning 發票 (hodl invoices)。此機制可確保您只有在實際收到 SMS 時才會被收取費用。如果在規定的時間內（最多 20 分鐘）沒有訊息傳達，付款會自動取消，衛星也會退回到您的 wallet。此保證不適用於傳送和租借功能，這些功能是不退費的。



## 三顆 SMS4Sats 的特色



SMS4Sats 介面有三個頁籤，分別對應三種不同的用途： **RECEIVE** 接收驗證碼，**SEND** 傳送匿名簡訊，**RENT** 租用臨時號碼。



### 接收簡訊



主要功能是讓您取得臨時號碼，以接收唯一的驗證碼。一旦收到並使用驗證碼，該號碼就會永久停用。



### 傳送簡訊



此功能可讓您在不透露身份的情況下，傳送簡訊至任何電話號碼。收件人將收到來自匿名號碼的訊息。



### 出租表演



對於需要使用單一號碼接收多條簡訊的使用者，SMS4Sats 提供臨時租用選項。此選項允許您在租用期間接收和發送多條訊息。



** 價格說明** ：本教程中顯示的價格為指示性價格。它們根據號碼所在國家、目標服務和當前需求而有所不同。例如，發送一條 SMS 到法國 Telegram 的費用在 1,500 到 5,000 薩托希之間，視情況而定。在支付之前，請務必檢查 Lightning 發票的確切金額。



## 接收驗證簡訊



讓我們以建立 Telegram 帳戶為例，詳細瞭解如何使用 SMS4Sats 接收驗證碼。



### 步驟 1：選擇國家和服務



前往 [sms4sats.com](https://sms4sats.com)，並停留在 **RECEIVE** 標籤上。從下拉式功能表中選擇所需號碼的國家/地區。如果列出了您訂閱的目標服務，請選擇該服務以增加接收的機會。



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



在本範例中，我們選擇法國為國家，Telegram 為目標服務。按一下 **NEXT** 進入下一步。



### 步驟 2：支付 Lightning 發票



Lightning 發票以 QR 碼的形式顯示。金額根據所選的國家和服務而有所不同。用您的Lightning wallet掃描QR碼，或複製發票手動支付。



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



請注意重要訊息：「無 SMS 編碼 = 無付款」。如果您未收到 SMS，您的付款將自動取消，並在最長 20 分鐘內退還。



### 步驟 3：取得臨時號碼



確認付款後，會立即顯示臨時電話號碼。計數器會顯示接收 SMS 的剩餘時間。



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



複製此號碼（此處為 +33 7 74 70 09 66），以便在您想要註冊的服務上使用。



### 步驟 4：使用目標服務上的號碼



在您建立帳戶的應用程式或網站上輸入臨時號碼。在我們的 Telegram 例子中，輸入號碼、確認並等待驗證碼。



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



過程與傳統註冊相同：您輸入號碼，Telegram 會以 SMS 傳送驗證碼，然後您就可以完成帳號建立。



### 步驟 5：擷取驗證碼



回到 SMS4Sats 介面。一收到 SMS，啟動碼就會自動顯示。點選 **COPY CODE** 即可輕鬆複製。



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



在目標服務上輸入此代碼以完成註冊。之後，臨時號碼就會永久停用。



## 傳送匿名簡訊



SMS4Sats 也可讓您發送 SMS 訊息到任何號碼，而不會透露您的身份。



### 步驟 1：撰寫訊息



按一下 **SEND** 標籤。輸入目的地電話號碼及其國際撥號碼並撰寫訊息（最多 1600 個字元）。



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



按一下 **NEXT** 繼續付款。



### 步驟 2：付款並傳送



支付顯示的 Lightning 發票。付款一經確認，SMS 即會立即傳送給收款人。



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



顯示確認碼以確認訊息已傳送。收件人會收到來自匿名號碼的簡訊。



## 租用臨時號碼



對於需要使用同一號碼發送多條 SMS 訊息的用途，租用功能可讓您租用一個號碼數小時。



### 租賃配置



按一下 **RENT** 標籤。選擇國家和期限。



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**重要注意事項：**




- 價格依國家及停留時間而有所不同
- 租用費不可退還**，與單次使用的 SMS 訊息不同
- 租用的號碼通常無法使用 Telegram
- 此選項適合連續訂閱幾項服務



點選 **NEXT** 並支付 Lightning 發票後，您就會得到一個號碼，在租用期間可以用來接收和傳送簡訊。



## 優點與限制



### 重點介紹



** 無需個人資料**：免註冊模式保證不會收集任何個人資訊。



**三種附加功能**：接收、傳送和租借功能涵蓋大部分需求。



** 僅使用 Bitcoin 付款** ：Lightning Network 允許即時和假名交易。



**自動報銷**：當接收 SMS 訊息時，hodl 發票系統保證您只有在 SMS 到達時才付款。



### 需要考慮的限制條件



**Relative SMS 通道安全性**：簡訊代碼並非穩健的驗證方法，不應用於敏感帳戶。



**變更相容性**：許多網站會偵測並封鎖虛擬號碼。可能需要多次嘗試。



**不可重複使用的號碼**：單次使用後，號碼會回收，無法再使用。



**不可退款的租用**：與一次性 SMS 訊息不同，租用不提供退款保證。



## 最佳實踐



### 使用 Tor 以獲得更多隱私



SMS4Sats 可透過 [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion) 存取。此設定可在存取服務時遮蔽您的 IP 位址。



### 避免關鍵帳戶



切勿將一次性號碼用於您的重要帳戶（銀行、主要電子郵件）。如果這些平台要求您日後重新驗證您的號碼，您將失去存取帳戶的權利。



### 分離您的數位身分



對於假名帳號，請將臨時號碼與一次性電子郵件地址和與您平常使用的瀏覽器隔離。



### 選擇堅固的 2FA



建立帳戶後，請啟動更強的驗證解決方案：TOTP 應用程式 (Aegis, Ente Auth) 或 FIDO2 實體安全金鑰。



## 總結



SMS4Sats 是機密簡訊管理的完整解決方案。無論您是要接收驗證碼、傳送匿名訊息或租用臨時號碼，這項服務都能滿足各種保密需求，這都歸功於 Bitcoin Lightning 的付款方式。



但請記住它的限制：該服務不保證絕對匿名，也不適合敏感或長期帳戶。明智地使用 SMS4Sats 並了解其限制，它是您重新控制電話通訊的實用工具。



## 資源





- [SMS4Sats 官方網站](https://sms4sats.com)
- [服務常見問題](https://sms4sats.com/faq)
- [Tor 位址](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)