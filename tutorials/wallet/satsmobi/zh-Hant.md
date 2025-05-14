---
name: Sats.mobi

description: A 電報可存取的保管 Wallet
---

![cover](assets/cover.webp)


_本教學的作者_ [Bitcoin 校園](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi 是在 Telegram 上運作的 Wallet，具有 Lightning Network（托管）Wallet 的所有功能，外加一系列非常有趣的特性。它源自於現已停產的 LightningTipBot 的 Fork，繼承了它的所有功能，同時加入了更多當前的功能，從而使它更現代化。和 LNTipBot 一樣，Sats.Mobi 也奉行開放源碼的理念。只要從這個 [資源庫](https://github.com/massmux/SatsMobiBot)克隆 Wallet，就可以獨立配置和管理 Wallet。


如果您喜歡簡單地使用它，在 Telegram 上開始聊天就會顯示它是一個機器人。


## 設定

從 Telegram 搜尋列尋找「satsmobi」，就會出現 [機器人](@SatsMobiBot) 的連結。


**注意**：如果您不確定是否要透過 Telegram 搜尋，請使用以下 [連結](https://t.me/SatsMobiBot) 安全地存取機器人


![image](assets/it/01.webp)


您只需按下 _START_ 即可開始。


![image](assets/it/02.webp)


若要探索 Wallet，您可以選擇左下方的 _Menu_。


![image](assets/it/03.webp)


現在選擇主要指令中的 _/help_。


![image](assets/it/04.webp)


Sats.Mobi 以顯示訊息的方式歡迎我們，列出所有主要功能。啟動時，機器人也會建立一個 LN Address，連結到 Telegram 上選擇的句柄（預設是唯一的）。可以看到用這個 Wallet 發送和接收 Sats 的指令，以及稍後我們會看到的其他功能。您也可以看看 _/advanced_ 功能表。


![image](assets/it/05.webp)


值得注意的是，Sats.Mobi 也創建了一個匿名的 LN Address，用於獲取隱私。該機器人使用命令工作：只需點擊相應的單詞，或在消息欄中鍵入斜線"/"，然後輸入要執行的命令。即使 Wallet 剛建立，選擇例如 _/transactions_


![image](assets/it/06.webp)


此指令會顯示最新的交易清單，在此特殊情況下等於零。


![image](assets/it/07.webp)


## 接收 Sats

建立 Invoice 和接收 Sats 的指令是 _/invoice_。Sats.Mobi完全以Satoshi運作，Satoshi是Bitcoin的最小單位；因此，若要建立Invoice，必須在訊息列中以Sats寫入金額，然後在與機器人聊天時傳送。

![image](assets/it/08.webp)


在下面的例子中，選擇接收 210 Sats 的金額。


![cover](assets/it/09.webp)


在等待 Invoice 準備好之後，就可以以文字和 QR 碼的形式顯示。支付 Invoice，Wallet 會顯示餘額。如果由於某種原因，總額沒有更新，請寫入 _/balance_，然後按 `enter` 鍵。


![image](assets/it/10.webp)


## 傳送 Sats


雖然 Sats 是極為珍貴的資產，不應輕易放棄，但 Sats.Mobi 讓這部分變得吸引人，執行一些簡短的測試（即幾筆試用交易）並不成問題。


### 支付 Invoice


支付 Invoice 的最簡單方法是複製訊息字串 `lnbc1xxxxx` 並在輸入 _/pay_ 指令後將其貼到訊息列。 **正確的語法**需要在指令後面留一個空格。


![image](assets/it/11.webp)


Wallet 會傳送訊息要求確認。按一下 _Pay_，Invoice 即完成付款。


![image](assets/it/12.webp)


Sats.Mobi 可以依賴高效率且連線良好的 Lightning 節點，很少會發生付款失敗的情況，因為它總是能找到正確的路由。


### 使用手機輕鬆付款


在 Telegram 上瀏覽，Sats.Mobi 也可在手機上使用。使用手機付款最方便的功能是掃描 QR 碼，但這款 Wallet 在設計上缺乏此功能，因為它不是獨立的應用程式，而是包含在社交網路中。因此，Sats.Mobi 的程式設計盡可能便利行動體驗：它確實能夠解碼圖像，像是您要付款的 Invoice QR 代碼所拍攝的照片。


例如，假設您想要支付 50 Sats 的 Invoice。


![image](assets/it/20.webp)


當這些顯示給我們時，我們可以拍下相關 QR 代碼的照片。


![image](assets/it/21.webp)


然後，我們在手機上開啟 Telegram，並在與 Sats.Mobi 聊天時，附上剛拍攝的 QR 代碼照片。


![cover](assets/it/22.webp)


一旦選定，我們就會將它傳送給機器人：


![image](assets/it/23.webp)

Sats.Mobi 會解碼照片並**立即提出付款要求**，並附上正確的描述。聊天會要求確認，若要繼續，您必須按 _/pay_。

![image](assets/it/24.webp)


請稍候，以便處理付款。


![image](assets/it/25.webp)


已支付 50 Sats 的 Invoice，這是在不使用攝影機及其整合掃描功能的情況下取得的成果。


### Sats.Mobi 在 Telegram 群組中


![image](assets/it/27.webp)


在讓 LNTipBot 聲名大噪的功能中，Sats.Mobi 也為 Telegram 帶來了這些功能，其中之一就是讓群組中的成員獲得有趣的互動體驗。

群主可以邀請機器人加入群聊，然後將 Sats.Mobi 提名為管理員。從那一刻起，樂趣就開始了，因為成員可以開始獎勵其他使用者對群組的貢獻。


- _/tip_ 藉由回覆訊息來新增小費；
- _/send_ 傳送指定 LN Address 或 Telegram 句柄為收件者的資金；
- _/faucet_ (在 _/advanced_ 功能表中) 允許建立一連串的提示，小組中速度最快的成員可以點選 _/collect_ 來收集這些提示；
- _/tipjar_ (在 _/advanced_ 功能表中) 會建立另一種傳送方式，可以傳送給群組中的使用者。


每種指令都有其語法，在主指令功能表中有說明。


如果我們不是群組的擁有者呢？沒問題：只要請創始人邀請 Sats.Mobi，將其加入為群組的管理員，就可以了！


## 銷售點 (POS)


當 Sats.Mobi 首次啟動時，機器人也會為使用者建立另一項功能： **POS**。使用者可使用 _/pos_ 指令或點選控制台右下方的相關按鈕啟動「裝置」。事實上，POS 是一個網頁應用程式，會在 Telegram 聊天室中以彈出方式開啟。


![image](assets/it/14.webp)


Interface 會在左上方顯示使用者的個人 Telegram 手柄，使用方式與所有 POS 機相同：在鍵盤上輸入金額。假設我們要收取 21 歐分的服務費。由於 Sats.Mobi 只管理 Sats，要在腦中進行轉換並不容易。相反地，POS 會顯示歐元為記帳單位，同時顯示等值的 Satoshi。


![image](assets/it/15.webp)

按一下 _/OK_ 會顯示 Invoice，可透過 QR 碼顯示給顧客，或透過即時通訊以字串形式傳送，因此可以付款。

![image](assets/it/16.webp)

![image](assets/it/17.webp)


當然，POS 也可以在手機上使用，存取方式與前述相同。


![image](assets/it/18.webp)


在手機螢幕上也能很好地顯示：


![image](assets/it/19.webp)


## 附加功能


Sats.Mobi Wallet 還具備其他功能，如我們所見，它將 Wallet 的概念擴展到收發付款的操作之外：


- _/nostr_: 將 Wallet 連接到您自己的 Nostr 使用者，以接收 zaps；
- _/cashback_: 顯示一個代碼，可向商家出示該代碼以獲得購物現金回贈；
- _/buy_：在機器人內啟動引導程序，允許以歐元購買 Sats；
- _/activatecard_：要求啟用 NFC 借記卡，可透過 Sats.Mobi Wallet 充值，並可為其啟用通知；
- _/link_：為您自己的 Zeus 或 Blue Wallet 建立連結，可作為此 Wallet 的遙控器。


## 總結

Sats.Mobi 是一款使用起來既愉快又有趣的 Wallet，它讓您回想起使用 LNTipBot 時的經驗，使用 LNBits 更先進的功能。不過，請務必記住，**它是一種保管服務**。因此，它應該用來持有很少的 Sats，它不是您 Lightning Network 資金的主要 Wallet。還有一個內在容量限制，等於 500,000 Sats，建議不要超過這個限制。


如果您正在尋找非攜帶型 Lightning Network 皮夾，絕對建議您看看其他產品。


---
### 文件


- [Github](https://github.com/massmux/SatsMobiBot)
- 播放清單 [視訊](https://www.youtube.com/results?search_query=Sats.mobi) 示範