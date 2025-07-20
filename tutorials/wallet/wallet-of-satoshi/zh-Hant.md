---
name: Satoshi 的 Wallet
description: 入門最簡單的保管 Wallet
---
![cover](assets/cover.webp)

_本教學的作者_ [Bitcoin 校園](https://linktr.ee/bitcoincampus_)


## 下載、設定及使用 Satoshi 的 Wallet


Satoshi 的 Wallet 是 Lightning Network 的 Wallet，保管，使用非常簡單。

就 [BTC105 - Finding Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) 課程而言，它是用來 Redeem Lightning Network 的憑證。


**永遠記住**_不是你的鑰匙，不是你的硬幣_


託管式錢包不允許使用者完全控制其資金。除了初學者之外，通常不建議使用。WoS 應該用作過渡性 Wallet 或存放零用錢，而不是用於長期的資金累積。


---

Wallet of Satoshi（WoS）是一種託管產品，但它有一定的聲譽。舉例來說，我們可以合理地求助 WoS 這樣的工具，以增加我們接收流動資金的能力。我們暫時將代我們管理通道流動性的 「髒活 」委託給 WoS。一旦達到一定數量，我們就會清空 WoS On-Chain 到我們的非監控 Wallet。


**警告⚠️：建議在繼續之前先完整閱讀本教學**


### 下載 Satoshi 的 Wallet


前往 Play 商店下載 WoS


![image](assets/it/01.webp)


**注意：** WoS 只能從官方商店下載。如果裝置的作業系統是程式化的，在開啟 WoS 之前，會有一個由作業系統自行驗證的部分。驗證階段結束後，選擇 _Open_。


![image](assets/it/02.webp)


Satoshi 的 Wallet 會開啟以下畫面，必須按一下_Start_（開始）。


![image](assets/it/03.webp)


### 註冊 WoS 帳戶


此時，Wallet 已經開始運作，但為了更安全起見，我們會繼續設定登入帳號：在裝置故障或遺失的情況下，需要登入帳號才能恢復資金。因此，請選擇左上方的功能表。


![image](assets/it/04.webp)


整個功能表視窗開啟，您必須在其中依喜好設定貨幣（Satoshi 的 Wallet 預設以美元為參考貨幣）和主題顏色（淺色/深色）。請勿使用其他指令。


由於 WoS 是保管工具，因此我們無法以 Mnemonic 短語備份 Wallet，但我們可以讓 WoS 在行動裝置遺失或無法使用的情況下，透過點選 _ 登入/註冊_ 來追回我們的資金。

出現一個視窗，要求我們輸入電子郵件 Address。它可以是 ** 個 Proton 郵件**（建議使用），但必須是功能性的，因為一旦手機遺失/被盜或損壞，它將允許我們取回 Wallet 中的資金。


![image](assets/it/08.webp)


Satoshi 的 Wallet 已傳送訊息至指定的電子郵件收件匣。


![image](assets/it/09.webp)


在信箱中，我們會發現兩個單字，我們需要在應用程式提供的空格中輸入、改寫這兩個單字。


- 請勿啟動翻譯器：字句仍為英文**
- 重寫這兩個字，注意大寫/小寫**


![image](assets/it/10.webp)


轉錄兩個單字後，按一下 _OK_。


![image](assets/it/11.webp)


結果應該是一個影像出現在頂端，並有核取標記符號進行驗證。


![image](assets/it/12.webp)


而在設定部分，紅色的 _ 登入/註冊_ 欄現在會顯示使用者的電子郵件 Address。


![image](assets/it/13.webp)


### 接收付款


若要在 WoS 上接收，按一下 _Receive_，就會出現一系列指令。


![image](assets/it/14.webp)


您可以收到


- 經由 LN-Address **a**
- 透過 LN，透過設定 Invoice **b**
- on chain (WoS 支援 Bitcoin 網路，但有付費的海底交換) **c**
- 透過掃描 LNurl-p **d** 的 QR 代碼


![image](assets/it/15.webp)


### 建立 Invoice


按一下 _Receive_（接收），然後選擇帶有 Lightning Network 符號的指令。


![image](assets/it/16.webp)


Invoice 創建功能表會出現，我們按一下 _Add Amount_ 寫入精確的金額，並加入說明，在本範例中為「我的第一個 Invoice」。


![image](assets/it/17.webp)


使用鍵盤，我們設定金額。


![image](assets/it/18.webp)


以獲得 Invoice 的付款。收到的付款是這樣的


![image](assets/it/19.webp)


### 從 POS 收款


Satoshi 的 Wallet 有一個預設功能，特別適合商家使用：POS。讓我們看看如何啟動它。


從主畫面，選擇右上方的功能表。


![image](assets/it/20.webp)


然後選擇 _ 銷售點。


![image](assets/it/21.webp)


使用最新版的 WoS，請務必選擇 _Keypad_。


![image](assets/it/22.webp)

然後在鍵盤上輸入金額，在下面的範例中等於 10 美分 / 118 Sats。加入收藏的說明，在此例中為「我第二次使用 POS」。一個大的 Green 按鈕會亮起，點擊它

![image](assets/it/23.webp)


將 generate 的 Invoice 展示給客戶。


![image](assets/it/24.webp)


這筆款項也會被收取！


![image](assets/it/25.webp)


### 發送付款


簡單是 WoS 主畫面的優點。若要支付 Invoice，請按一下_Send_。


![image](assets/it/26.webp)


第一次使用時，WoS 會要求存取攝影機的權限


![image](assets/it/27.webp)


從這一刻開始，攝影機啟動


![image](assets/it/28.webp)


框選 Invoice，我們看到已要求支付 210 Sats。如果請求人設定了說明，也會讀取說明。這個畫面是摘要，也是要求確認：WoS 「要求授權 」發送付款，點擊 Green _Send_ 按鈕即可授權。


![image](assets/it/29.webp)


當付款到達目的地時，WoS 會以下列畫面通知


![image](assets/it/30.webp)


在主畫面上，按一下 _History_（就在餘額下方），交易清單就會出現


![image](assets/it/31.webp)


#### 恢復 WoS 帳戶


現在，我們來看看如何將 WoS 安裝到新的裝置上；這在之前安裝 Wallet 的手機被竊、遺失或無法操作的情況下也很有用。重新安裝之後，您必須重新執行剛才所說的帳號註冊程序，但有一個不同的地方：在要求使用之前設定的電子郵件登入的最後，WoS會出現這樣的畫面：


![image](assets/it/33.webp)


訊息警告我們已寄出一封電子郵件，內含重新啟動帳戶的程序。您必須打開您的電子郵件收件匣。


**重要**：從個人電腦開啟電子郵件，或在任何情況下，從與您要復原 WoS 帳戶的裝置不同的裝置開啟。在收件匣中，我們會發現一則顯示 QR 碼的訊息。


![image](assets/it/34.webp)


當 QR 碼被鑲入後，在 WoS 的主頁面上就會顯示已恢復的帳戶，以及餘額和歷史記錄。