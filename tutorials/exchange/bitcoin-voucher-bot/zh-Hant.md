---
name: BitcoinVoucherBot
description: 用 Telegram 機器人購買保密的 Bitcoin
---
![image](assets/cover.webp)


_本教學的作者_ [Bitcoin 校園](https://linktr.ee/bitcoincampus_)


# 簡介


BitcoinVoucherBot 是一個工具，用它可以在 Exchange 中以歐元購買比特幣。


### KYC Light


為 Bitcoin 更換歐元的行動是開始研究這個主題的第一步，也是最基本的一步，但顯然也是最困難、最複雜的一步。可以有很多選擇：通過集中式交易所提供 Bitcoin、以 Bitcoin 為主題的聚會、朋友、熟人等等。我們加入 Bitcoiner 社群，**我們絕對建議使用集中式交易所**，以保障個人隱私更受關注。


儘管這種選擇可能不太方便，但重要的是要瞭解交易所會執行「認識您的客戶」(KYC) 法規，因此會為從其購買的每個 Satoshi 指定身份和實體位置。「方便」有一些顯著的副作用。


### 如何執行？


BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot) 服務來了，這是一個 Telegram 機器人，作為我們 SEPA 轉帳和 Sats 購買之間的管道。


### 先決條件


要開始使用 BitcoinVoucherBot，不需要向 Bot 員工透露敏感的個人資訊。 **不需要授權**。


只需要一個已啟動的 Telegram 帳戶和一個銀行帳戶。 **註**：在 Poste Italiane（針對義大利客戶）開設的帳戶或更廣泛而言，充值卡並不適用。


我們在 Telegram 聊天室準備訂單，然後透過銀行轉帳付款，最後透過機器人獲得由第三方公司發行的優惠券，而該公司並不知道購買的對象。


### 機器人啟動與選單


啟動是一個簡單的一次性操作。從 Telegram 搜尋 _@BitcoinVoucherBot_，一進入 Bot 的聊天室，底部就會出現一個大的 _Start/Start_ 按鈕。該操作會引起 Bot 的回應，它會顯示一個它可用的主要命令的菜單。首批歡迎訊息也會出現，建議您仔細閱讀。


**警告**：有幾個騙子冒充原版VoucherBot。如果您不確定要透過 Telegram 搜尋，請從 [官方網站](https://www.bitcoinvoucherbot.com/) 進入 BitcoinVoucherBot 連結


![image](assets/it/01.webp)


按一下左下角的 _Menu_ 按鈕就會出現選項：您可以按一下與命令對應的單字，或在訊息方塊中輸入斜線 `/`，之後再輸入所輸入的命令。


![image](assets/it/02.webp)


主要業務包括




- _/purchase_: 是實際的購買程序。交易完成後，機器人會自動產生 QR Code，準備兌換。
- _/refill_: 在撰寫本教學時可用，但我們不會涵蓋它，因為技術上的原因，此選項稍後可能會被移除。
- _/swap_: 開啟交換程序，可透過便利的 Telegram 機器人或網頁使用。
- _/ap_：累積計劃，可讓您設定 ** 恆定累積計劃 (CAP)**。
- _/lnaddress_: 我們被要求連結一個自己的 LN Address，用於稍後我們會看到的特定程序。
- _/credits_: 檢查 generate 憑證還剩多少點數。
- _/myorders_: 顯示使用機器人下達的訂單 (** 警告** 系統只追蹤最近 10 個下達的訂單，而非整個歷史記錄)。
- _/fees_: 檢查網路費用的指令。要評估它們，最好還是依賴 Mempool.space。
- _/support_：在需要的情況下，彈出聯絡方式以向支援團隊報告問題。


# Bitcoin 採購程序


## 訂單準備


按一下指令功能表中的 _/購買


![image](assets/it/03.webp)


有許多機會出現，但我們選擇 _BTC Vouchers_。


![image](assets/it/04.webp)


BitcoinVoucherBot 允許您購買 Bitcoin onchain、Lightning 和 Liquid。


在此階段選擇 _Onchain & Lightning 🔗⚡️_


![image](assets/it/05.webp)


螢幕會快速變換，VoucherBot 會建議購買面額。最低 100.00 歐元，最高 900.00 歐元。


首次購買時，僅提供 100.00 €、Onchain 和 Lightning 面額。為了提高保密性，我們建議選擇 _Lightning ⚡️_


![image](assets/it/06.webp)


代金券機器人提醒我們已經做出了第一個選擇，為了確認它，我們需要選擇_Proceed_。


![image](assets/it/07.webp)


現在只需選擇付款方式。轉帳方式為電匯**（僅接受 SEPA）**。VoucherBot 建議由一家公司作為收款人，該公司提供兩個銀行帳戶，一個在英國，另一個在瑞士。選擇瑞士銀行來執行此教程


![image](assets/it/08.webp)


此時，我們會被要求輸入 IBAN，也就是開始轉帳到所選擇銀行的 IBAN。這些資訊將構成一個拼圖，讓機器人 (即機器) 將一些資訊拼在一起，使購買過程流暢，而無需人工干预。


IBAN 必須寫在訊息列中、檢查並傳送給機器人。


![image](assets/it/09.webp)


現在與 VoucherBot 聊天時會出現控制訊息。


如果一切正確，請按一下 _Proceed（繼續）繼續。


![image](assets/it/10.webp)


## 付款方式


處理資料所需的片刻之後，VoucherBot 會回覆一則訊息，其中包含完成訂單所需的所有詳細資訊。根據您的銀行要求，相關資訊如下：




- IBAN」，這是存款以及收款人 Address 的必要條件；
- 選擇的金額」先前已通過截止時間，必須滿足截止時間才能讓 VoucherBot 在收到付款時識別訂單；
- `付款原因`，這是付款的原因。 **必須複製並粘貼，不得在轉帳的適當欄位中移除或添加任何內容。付款原因中的任何". 「或」-「都可以用 」空白 "**代替。
- 一個唯一的 `OrderID`，以便在要求任何協助時參考。


然後您就可以透過您的應用程式或銀行進行付款。銀行接受付款後，請記住在與 VoucherBot 的聊天中按下 _Notify payment_。這個簡單的操作會提醒您付款正在進行中。


![image](assets/it/11.webp)


VoucherBot 會回應一則包含非常重要警告的訊息： *不要刪除聊天**，至少在收到購物券之前不要刪除聊天**，因為這是重建訂單並維持訂單的唯一方法。


![image](assets/it/12.webp)


---
請注意




- 只接受 SEPA 電匯；
- 等待時間僅與銀行處理憑證的方式有關（銀行不會像 Bitcoin 一樣全年無休地工作）。收到憑證可能需要幾小時到 3 個工作日；
- 如有任何需求，Bitcoin VoucherBot 在 Telegram 上提供優秀的 [支援](https://t.me/BitcoinVoucherGroup) 服務。


---
## 贖罪


只要付款成功，Bitcoin VoucherBot 就會直接將禮券傳送至聊天內容中。閃電禮券以 QR 代碼的形式出現，印在橙色背景上。


![image](assets/it/31.webp)


這裡有套現所需的所有資料：




- Sats 中的金額，相當於電匯的金額，不包括服務費和網路費；
- 憑證的參考 ID；
- 必須兌換憑證的日期，否則資金將遭到損失，即簽發後 25 天。


您可以使用相容的 Wallet Lightning Network 的掃描功能將 QR 碼定格，或透過 LNURL（也顯示在 QR 碼下方）將禮券兌現。


在本教程中，我們使用 Wallet Of Satoshi，使用 _Send_ 鍵啟動的掃描功能。


![image](assets/it/32.webp)


啟動手機相機，將 QR 代碼框入聊天內容，從 PC 開啟 Telegram


![image](assets/it/34.webp)


在繼續之前，Wallet Of Satoshi 從驗證螢幕，其中包括金額，這完全符合代金券上所表示的金額，並作為說明，BitcoinVoucherBot。要兌現代金券，只需點擊_Receive_


![image](assets/it/35.webp)


Wallet of Satoshi 處理片刻


![image](assets/it/36.webp)


最後，Wallet 結餘中的收款會被報告並立即可用。


**Satoshi 的 Wallet 是保管應用程式：兌現憑證後，建議立即將 Sats 移至 Wallet 非保管.**。


![image](assets/it/37.webp)


### 如何兌現onchain代金券


正如我們在訂單準備中看到的，VoucherBot 允許直接在鏈上購買 Sats，並選擇同名代金券。


**註**：訂單準備和付款不會變，一直都是一樣的。改變的是如何兌現鏈上憑證。


在完成訂單、付款、按_Notify payment_並等待銀行技術時間轉帳之後，VoucherBot會直接將禮券傳送至聊天室，以作回應。


這張禮券也是 QR 碼的形式，但主要顏色是金絲雀黃，而且最重要的是，在描述中說明這是一張 onchain 禮券，可以直接在您的 Wallet onchain 上兌現，要開始兌現程序，您必須點選 _Redeem on Telegram_。onchain代金券也包含閃電代金券的相關資訊：




- 以 Sats 表示的金額，相當於電匯的金額，不含服務費和網路費；
- 優惠券代碼；
- 憑證的參考 ID；
- 必須兌換憑證的日期，否則資金將遭到損失，即簽發後 25 天。


![image](assets/it/22.webp)


**WARNING ⚠️:**按下說明，會開啟另一個機器人的彈出視窗： **Voucher RedeemBot.**


Voucher RedeemBot 是為此目的而提供的工具。無論是第一次使用還是以前的訂單，每次進行新的兌換時都必須點擊 _START_。


![image](assets/it/23.webp)


這時 RedeemBot 會載入上鏈憑證，憑證代碼和參考 ID 可以輕鬆識別。它還解鎖了寫訊息的欄位，並開始與機器人聊天，這其實是邀請我們告訴它我們的 Wallet 的onchain Address。


**註**：此 Address 必須是 SegWit 類型。


![image](assets/it/24.webp)


此時我們打開我們的 Wallet 和 generate a SegWit Address


![image](assets/it/25.webp)


我們複製它


![image](assets/it/26.webp)


並貼到 RedeemBot 的聊天內容中


![image](assets/it/27.webp)


我們現在有一個檢查畫面，以驗證優惠券代碼以及我們傳達給 RedeemBot 的 Address 是否正確。讓我們好好檢查一下，因為按一下 _Proceed_，交易就開始了，如果我們傳達了錯誤的 Address，就沒有辦法再找到它了。


![image](assets/it/28.webp)


交易已經開始，因此在線憑證的 Redeem 程序結束。


![image](assets/it/29.webp)


而在我們的 Wallet 歷史中，可以看到這個數量。


![image](assets/it/30.webp)