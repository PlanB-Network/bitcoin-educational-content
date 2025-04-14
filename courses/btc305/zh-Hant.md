---
name: Bitcoin 和 BTC 付款伺服器
goal: 為您的企業安裝 BTC Pay 伺服器
objectives: 

  - 瞭解什麼是 btcpayserver。
  - 自行託管和設定 BTC Pay 伺服器。
  - 在您的日常業務中使用 btcpayserver。

---
# Bitcoin 和 BTCPay 伺服器

這是由 Alekos 和 Bas 撰寫的 BTCPay 伺服器操作員介紹課程，並由 melontwist 和 asi0 在 Plan ₿ 課程格式中加以改編。

后话

「這是謊言，我對你的信任破滅了，我會讓你淘汰」。

由 BTCPay 伺服器基金會製作

+++
# 簡介

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## 作者的 Bitcoin 和 BTCPay 伺服器廣受好評

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

讓我們從BTCPay伺服器是什麼和它的來源開始。我們重視透明度和一定的標準，以便在 Bitcoin 空間形成信任。

該領域的一個專案打破了這些價值觀。BTCPay Server 的首席開發人員 Nicolas Dorier 對此耿耿於懷，並承諾要廢除這些價值觀。多年後的今天，我們每天都在努力邁向這個完全開放源碼的未來。

> 這是謊言，我對您的信任破滅了，我會讓您被淘汰。
> Nicolas Dorier
Nicolas 說完這番話之後，就是開始建置的時候了。大量的工作投入到我們現在所稱的 BTCPay 伺服器上。更多的人想幫助這個推動。最知名的有 r0ckstardev、MrKukks、Pavlenex，以及第一個使用軟體的商家 astupidmoose。

開放原始碼是什麼意思？

FOSS 是 Free & Open-Source Software 的縮寫。前者指的是允許任何人複製、修改、甚至散佈軟體版本（甚至為了獲利）。後者是指公開分享原始碼，鼓勵大眾貢獻和改進。

這將帶來經驗豐富的使用者，他們熱衷於貢獻自己已經在使用並從中獲取價值的軟體，久而久之，證明他們的採用率將勝過專屬軟體。這符合 Bitcoin 的精神：「資訊渴望自由」。它將熱情的人們聚集在一起，形成一個社群，而且更有趣。如同 Bitcoin，FOSS 是不可避免的。

### 開始之前

本課程包含多個部分。許多部分將由您的任課老師、您可以存取的 Demo 環境、您自己的託管伺服器，以及可能的網域名稱來處理。如果您獨立完成本課程，請注意標示為 DEMO 的環境將無法使用。

注意。如果您按教室學習本課程，伺服器名稱可能會因您的教室設定而異。因此伺服器名稱中的變數可能會有所不同。

### 課程結構

每章都有目標和知識評估。在本課程中，我們將涵蓋這些內容，並在每個課程區塊(即章節)總結主要特色。插圖的特色在於提供視覺回饋，並在視覺方面強化關鍵概念。每個課程區塊的開始都設定了目標。這些目標不僅僅是一個核對表。這些目標提供您進入新技能的指引。BTCPay伺服器設定的知識評估逐步增加挑戰性。

### 學生可以從課程中獲得什麼？

通過BTCPay伺服器課程，學生可以了解Bitcoin的基本原理、技術和非技術。通過 BTCPay Server 使用 Bitcoin 的廣泛培訓，學生可以操作自己的 Bitcoin 基礎設施。

### 重要網址或聯絡機會

讓 Alekos 和 Bas 撰寫本課程的 BTCPay Server Foundation 位於日本東京。BTCPay 伺服器基金會可透過所列的網站聯絡；


- https://foundation.btcpayserver.org
- 加入官方聊天頻道 :https://chat.btcpayserver.org

## Bitcoin 簡介

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### 透過課堂練習了解 Bitcoin

這是課堂練習，所以如果您自己上這門課程，您就無法執行，但您仍可以透過這個練習來完成。要完成這項任務，最少需要 9 到 11 人。

練習在觀看 BBC 的介紹「How Bitcoin and the Blockchain works」之後開始。

:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::

這項練習需要至少九個人參與。本練習的目的是讓您實際了解 Bitcoin 的運作方式。透過扮演網路中的每個角色，您將能夠以互動和遊戲的方式學習。本練習不涉及 Lightning Network。

### 範例；需要 9 / 11 人

角色為 ：


- 1 位顧客
- 1 商戶
- 7 到 9 個 Bitcoin 節點

**設定如下：**

顧客使用 Bitcoin 從商店購買產品。

**Scenario 1 - 傳統銀行系統**


- 設定：
  - 請參閱附件 Figjam - [活動示意圖](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0) 中的圖表/說明。
  - 找三名學生志願者扮演顧客 (Alice)、商人 (Bob) 和銀行。
- 演出事件發生的順序：
  - 顧客 - 在線上瀏覽商店，發現一件價值 25 美元的商品是他們想要的，並告知商家他們想要購買。
  - Merchant- 要求付款。
  - 客戶 - 傳送卡片資訊給商家
  - 商戶- 將資料轉寄給銀行（同時識別其本人和身份/資料），要求支付
  - 銀行收集客戶和商家（Alice 和 Bob）的資訊，並檢查客戶的餘額是否足夠。
  - 從 Alice 的帳戶中扣除 \$25, 在 Bob 的帳戶中加入 \$24, 從服務中扣除 \$1
  - 商家收到銀行的讚賞後，將商品寄給顧客。
- 評論：
  - Bob 和 Alice 必須與銀行建立關係。
  - 銀行會收集 Bob 和 Alice 的識別資訊。
  - 班克被砍了一刀
  - 銀行必須被信賴一直保管每位參與者的資金。

**Scenario 2 - Bitcoin 系統**


- 設定：
  - 請參閱附件 Figjam - [活動示意圖](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0) 中的圖表/說明。
  - 取代銀行，由九名學生扮演網路中的電腦 (Bitcoin 節點/礦工) 來取代銀行。
- 9 台電腦中的每一台都有過去所有交易的完整歷史記錄（因此結餘準確無偽造），以及一套規則：
  - 驗證交易已正確簽署 (thekeyfitsthelock)
  - 向網路中的對等機構廣播和接收有效的交易，拋棄無效的交易（包括任何試圖花費相同資金兩次的交易）
- 只要所有內容都是有效的，就會以「隨機」電腦傳送的新交易來定期更新/新增記錄（注意：為簡單起見，我們暫時忽略 Proof of Work 的元件），否則會拒絕這些記錄，並繼續像之前一樣，直到下一台「隨機」電腦傳送更新。
  - 如果內容有效，則會獎勵適當的金額。
- 演出事件發生的順序：
  - 顧客 - 在線上瀏覽商店，發現一件價值 25 美元的商品是他們想要的，並告知商家他們想要購買。
  - Merchant- 從顧客的 Wallet 寄出 Invoice/Address 要求付款。
  - 客戶 - 建構一筆交易 (傳送價值 25 美元的 BTC 到商家提供的 Address) 並將其廣播到 Bitcoin 網路。
- 電腦 - 接收交易並驗證：
  - 在 Address 中至少有 25 美元的 BTC 從
  - 交易已正確簽署（由客戶「解鎖」）。
  - 如果不是，則交易不會透過網路傳播；如果是，則會傳播並在等待中保留。
  - 商戶可以檢查交易是否正在等待中。
- 會「隨機」選出一台電腦，建議透過廣播包含交易的「區塊」來最終完成建議的交易；如果交易成功，他們就會收到 BTC 獎勵。
  - 選用/進階 - 不隨機選擇電腦，而是模擬 Mining，方法是讓電腦擲骰子，直到出現預定結果為止（例如，先擲出雙六的電腦會被選中）。
  - 它也可以演算出如果兩台電腦約略同時贏得，導致連鎖分裂時會發生的情況。
  - 電腦會檢查有效性，如果符合規則，就會更新/新增記錄到其分類帳中，並將區塊廣播給對等電腦。
  - 隨機選擇的電腦會因提出有效區塊而獲得獎勵。
  - 商家支票交易已完成；因此，資金已收到，商品已寄送給客戶。
- 評論：
  - 請注意，不需要預先存在的銀行關係。
  - 不需要協力廠商協助；由法規/獎勵措施取代。
  - 直接 Exchange 以外的任何人不得收集資料，參與者之間必須只交換必要的數量（例如運送 Address）。
  - 人與人之間不需要信任（除了寄送物品的商家），在很多方面就像現金購買一樣。
  - 資金直接歸個人所有。
  - 為了簡單起見，Bitcoin Ledger 以美元來描述，但實際上是 BTC。
  - 我們模擬單一交易被廣播，但實際上，網路中有多個交易待處理，區塊同時包含數千個交易。節點也會檢查是否有雙重花費的交易待處理 (如果是這樣的話，除了一個交易之外，我都會丟掉)。
- 作弊情況：
  - 如果客戶沒有 $25 BTC 呢？
    - 他們無法建立交易，因為「解除鎖定」和「Ownership」是同一件事，而且電腦會檢查交易是否有正確的簽章；否則，他們會拒絕它
  - 如果隨機選擇的電腦試圖「改變 Ledger」怎麼辦？
    - 該區塊會被拒絕，因為其他每台電腦都有完整的歷史記錄，並會注意到這項變更，這違反了他們的其中一項規則。
    - 隨機電腦不會獲得獎勵，其區塊中的交易也不會最終完成。

## 知識評估

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### KA 課堂討論

討論第二種情況下課堂練習中的一些過度簡化，並詳細描述實際 Bitcoin 系統的作用。

### KA 詞彙複習

定義上一節介紹的下列關鍵詞：


- 節點
- Mempool
- 難度目標
- 塊

**以小組形式討論一些額外詞彙的意義：**

Blockchain、交易、雙重支出、拜占庭將軍問題、Mining、Proof of Work (PoW)、Hash 功能、Block reward、Blockchain、最長鏈、51% 攻擊、輸出、輸出鎖、變更、Satoshis、公鑰/私鑰、Address、公鑰加密法、數位簽章、Wallet

# BTCPay伺服器介紹

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## 瞭解 BTCPay 伺服器登入畫面

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### 使用 BTCPay 伺服器

本課程區塊的目標是對 BTCPay Server 軟體有一般的了解。在共享環境中，建議跟隨講師的示範，並隨著 BTCPay Server 課程手冊跟隨老師學習。您將學習如何透過多種方法建立 Wallet。範例包括 Hot Wallet 設定和透過 BTCPay Server Vault 連接的硬體錢包。這些目標發生在演示環境中，由您的課程導師展示和提供訪問。

如果您自己學習本課程，您可以在 https://directory.btcpayserver.org/filter/hosts 找到用於 Demo 的第三方主機清單。我們強烈建議不要使用這些第三方選項作為生產環境，但它們可以達到介紹使用 Bitcoin 和 BTCPay 伺服器的目的。

身為 BTCPay Server rockstar 的受訓者，您可能已經有設定 Bitcoin 節點的經驗。本課程將特別針對 BTCPay Server 軟體堆疊進行講解。

BTCPay Server 中的許多選項都以某種形式存在於其他 Bitcoin Wallet 相關軟體中。

### BTCPay 伺服器登入畫面

歡迎您進入 Demo 環境，您會被要求「登入」或「建立您的帳號」。出于安全考虑，服务器管理员可能会关闭创建新账户的功能。BTCPay服務器的標誌和按鈕顏色可以更改，因為BTCPay服務器是開放源碼軟件。第三方主機可以對軟件進行白標，並改變整個外觀。

![image](assets/en/0.webp)

### 建立帳戶視窗

在 BTCPay 伺服器上建立帳號需要有效的電子郵件 Address 字串；example@email.com 將是電子郵件的有效字串。

密碼至少需要 8 個字元，包括字母、數字和字元。設定一次密碼後，您必須驗證輸入的密碼，以確保它與在第一個密碼欄位中輸入的內容正確無誤。

當Email和密碼都正確填寫後，點擊'Create Account'按鈕。這將把Email和密碼保存在講師的BTCPay伺服器上。

![image](assets/en/1.webp)

**！注意！**

如果您自己學習本課程，您可能會在第三方主機上建立此帳戶；因此，我們再次提醒您，切勿將這些帳戶用於生產環境，而只能用於訓練目的。

### 由 BTCPay 伺服器管理員建立帳戶

BTCPay服務器實例的管理員也可以為BTCPay服務器創建帳戶。BTCPay 服務器實例的管理員可以點擊「服務器設置」(1)，點擊「用戶」標籤(2)，然後點擊用戶標籤右上方的 「+ 添加用戶 」按鈕(3)。在目標(4.3)中，您將學習更多關於帳戶的管理員控制。

![image](assets/en/2.webp)

身為管理員，您需要使用者的電子郵件 Address 並設定標準密碼。基於安全理由，建議身為管理員的您告知使用者在使用帳號前應更改此密碼。如果管理員沒有設定密碼，且伺服器上已設定 SMTP，使用者會收到一封附有邀請連結的電子郵件，讓他們自行建立帳號和設定密碼。

### 範例

由講師教授課程時，請按照講師提供的連結，在提供的示範環境中建立您的帳戶。確保您的電子郵件 Address 和密碼已安全儲存；在本課程的其餘示範目標中，您將需要這些登入認證。

您的指導老師可能已事先收集了電子郵件 Address，並在本次練習之前發送了邀請連結。如果有指示，請檢查您的 Email。

在沒有教師的情況下上課時，請使用 BTCPay 伺服器的示範環境建立您的帳戶；請前往

https://Mainnet.demo.btcpayserver.org/login。

此帳號只能用於示範/訓練目的，絕對不能用於商業用途。

### 技能摘要

在本節中，您學習了以下內容：


- 如何透過 Interface 在託管伺服器上建立帳戶。
- 伺服器管理員如何在伺服器設定中手動新增使用者。

### 知識評估

#### KA 概念回顧

請說明使用 Demo Server 作為生產用途不是好主意的原因。

## 管理使用者帳戶

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### BTCPay 伺服器上的帳戶管理

店主建立帳戶後，可以在 BTCPay 伺服器使用者介面的左下方管理帳戶。在帳戶按鈕下方，有多個更高層次的設定。


- 暗/亮模式。
- 隱藏敏感資訊切換鍵。
- 管理帳戶。

![image](assets/en/3.webp)

### 深色和淺色模式

BTCPay 伺服器的使用者可以選擇使用者介面的淺色或深色模式版本。面向客戶的頁面不會改變。它們使用客戶對深色或淺色模式的偏好設定。

### 隱藏敏感資訊切換

隱藏敏感信息按鈕帶來快速簡單的Layer安全保障。當您需要操作您的 BTCPay 伺服器，但在公共場所可能有人潛伏在您的肩膀上時，開啟隱藏敏感資訊，BTCPay 伺服器中的所有值將被隱藏。人們也許能夠從您的肩上看過去，但再也看不到您正在處理的數值。

### 管理帳戶

建立使用者帳戶後，就可以在這裡管理密碼、2fa 或 API kes。

### 管理帳戶 - 帳戶

可選擇使用不同的電子郵件Address更新您的帳戶。為確保您的電子郵件Address正確無誤，BTCPay伺服器允許您發送驗證電子郵件。如果用戶設置了新的Email Address並確認驗證成功，請點擊保存。用戶名仍與之前的Email相同。

使用者可以決定刪除整個帳戶。這可透過按一下「帳戶」標籤上的刪除按鈕來完成。

![image](assets/en/4.webp)

**！注意！**

變更電子郵件後，帳戶的使用者名稱不會變。之前給定的電子郵件 Address 將保留為登入名稱。

### 管理帳戶 - 密碼

學生可能想要變更密碼。他可以前往「密碼」標籤進行此操作。在此，他需要輸入舊密碼，並可將其變更為新密碼。

![image](assets/en/5.webp)

### 雙因素驗證 (2fa)

為了限制密碼被盜的後果，您可以使用雙因素驗證 (2fa)，這是一種較新的安全方法。您可以透過「管理帳戶」和「雙因素驗證」標籤啟動雙因素驗證。使用使用者名稱和密碼登入後，您必須完成第二個步驟。

BTCPay 伺服器允許兩種方式啟用 2FA，基於應用程式的 2FA（Authy、Google、Microsoft authenticators）或透過安全裝置（FIDO2 或 LNURL Auth）。

### 雙因素驗證 - 以應用程式為基礎

根據您手機的作業系統 (Android 或 iOS)，使用者可以選擇下列應用程式；

1.下載雙重認證器；


   - Authy 適用於 [Android](https://play.google.com/store/apps/details?id=com.authy.authy) 或 [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator for [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) 或 [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - 適用於 [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) 或 [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605) 的 Google Authenticator

2.下載並安裝 Authenticator App 之後。


   - 掃描BTCPay伺服器提供的QR碼
   - 或將 BTCPay 伺服器所產生的金鑰手動輸入您的 Authenticator 應用程式。

3.Authenticator 應用程式會為您提供一個唯一代碼。在BTCPay伺服器中輸入獨特代碼以驗證設定，然後點擊 「驗證 」完成整個過程。

![image](assets/en/6.webp)

### 技能摘要

在本節中，您學習了以下內容：


- 帳戶管理選項以及在 BTCPay 伺服器實例上管理帳戶的各種方式。
- 如何設定應用程式 2FA。

### 知識評估

#### KA 概念回顧

說明應用程式式 2FA 如何確保帳戶安全

## 建立新商店

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### 建立商店精靈

當一個新的用戶登錄到BTCPay服務器，環境是空的，需要一個第一個商店。BTCPay 伺服器的導入精靈會讓使用者選擇「建立您的商店」(1)。商店可視為您 Bitcoin 需求的家。一個新的BTCPay伺服器節點將從同步Bitcoin Blockchain開始(2)。根據您運行 BTCPay 伺服器的基礎設施，這可能需要幾個小時到幾天不等。實例的當前版本顯示在您的BTCPay Server UI的右下角。這在疑難排解時非常有用。

![image](assets/en/7.webp)

### 建立商店精靈

跟隨此課程開始時的畫面與前一頁略有不同。由於導師已準備好 Demo 環境，Bitcoin Blockchain 已事先同步，因此您將不會看到節點的同步狀態。

使用者可以決定刪除整個帳戶。這可透過按一下「帳戶」標籤上的刪除按鈕來完成。

![image](assets/en/8.webp)

**！注意！**

BTCPay 伺服器帳戶可以建立無限數量的商店。每個商店都是一個 Wallet 或 「 家 」。

### 範例

首先按一下「建立您的商店」。

![image](assets/en/9.webp)

這將會建立您使用 BTCPay 伺服器的第一個首頁和儀表板。

(1)點擊 「創建您的商店 」後，BTCPay伺服器會要求您為商店命名，可以是任何對您有用的名稱。

![image](assets/en/10.webp)

(2) 接下來必須設定預設的商店貨幣，可以是法定貨幣或以 Bitcoin / Sats 標準計價的貨幣。在示範環境中，我們將設定為美元。

![image](assets/en/11.webp)

(3) 作為商店設置的最後一個參數，BTCPay伺服器要求您設置一個 「首選價格來源 」來比較Bitcoin的價格和當前法定貨幣的價格，以便您的商店在Bitcoin和商店設置的法定貨幣之間顯示正確的Exchange匯率。我們將堅持使用演示示例中的預設值，並將其設置為 Kraken Exchange。BTCPay 伺服器使用 Kraken API 來檢查 Exchange 的匯率。

![image](assets/en/12.webp)

(4) 現在這些商店參數已經設定好了，點擊 「創建 」按鈕，BTCPay伺服器將創建您的第一個商店的儀表板，向導將在此繼續。

![image](assets/en/13.webp)

恭喜您，您已建立了第一個商店，這就是本練習的總結。

![image](assets/en/14.webp)

### 技能摘要

在本節中，您將學習到


- 商店建立和設定預設貨幣，並結合價格來源偏好設定。
- 每個 「商店 」都是一個新的家，與BTCPay伺服器上的其他商店分開。

# 保護 Bitcoin 金鑰簡介

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## 瞭解 Bitcoin 金鑰的產生

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### 產生 Bitcoin 金鑰涉及什麼？

Bitcoin 錢包在建立時，會產生所謂的 "seed"。在上一個目標中，您創建了一個 "seed"，之前產生的一系列單詞也被稱為 Mnemonic 短語。seed 用來衍生出個別的 Bitcoin 金鑰，並用來傳送或接收 Bitcoin。seed 短語絕對不能與第三方或不信任的對等方分享。

seed 的產生是依照業界標準「分層決定性」（HD）架構進行。

![image](assets/en/15.webp)

### 地址

BTCPay 伺服器建立到 generate 一個新的 Address。這減輕了公鑰或Address重複使用的問題。使用相同的公開密鑰可以非常容易地追蹤您的整個支付歷史。將金鑰視為一次性使用的憑證，將可大幅改善您的隱私。我們也使用 Bitcoin 位址，請勿與公開金鑰混淆。

Address 通過 「散列演算法 」從公開金鑰獲得。但是，大多數的錢包和交易都會顯示地址而不是公開密鑰。一般而言，地址比公開金鑰短，通常以`1`、`3`或`bc1`開頭，而公開金鑰則以`02`、`03`或`04`開頭。


- 以 `1.....` 開頭的位址仍然是非常普遍的位址。正如創建新商店一章所述，這些是傳統的位址。這種 Address 類型是用於 P2PKH 交易。P2Pkh 使用 Base58 編碼，這使得 Address 區分大小寫。它的結構是以公開金鑰為基礎，再加上一位數作為識別碼。
- 以`bc1...`開頭的位址正慢慢邁向非常普遍的位址。這些稱為（原生）SegWit 位址。這些位址提供比上述其他位址更好的收費結構。原生 SegWit 位址使用 Bech32 編碼，僅允許使用小寫字母。
- 以 `3...` 開頭的位址通常仍被交易所用來存放位址。這些位址在「建立新儲存、包裝或嵌套的 SegWit 位址」章節中有提到。不過，它們也可以作為「Multisig Address」使用。當作為 SegWit Address 使用時，又可以節省一些交易費用，但比原生 SegWit 少一些。P2SH 位址使用 Base58 編碼。這使得它對大小寫敏感，就像傳統的 Address。
- 以`2...`開頭的位址是 Testnet 位址。它們是用來接收 Testnet Bitcoin (tBTC)。您絕對不能混淆，將 Bitcoin 傳送至這些位址。為了開發目的，您可以 generate 一個 Testnet Wallet。網上有多個龍頭可以獲得 Testnet Bitcoin。切勿購買 Testnet Bitcoin。Testnet Bitcoin 已經被開採。這可能是開發人員改用 Regtest 的理由。這是開發人員的遊樂場環境，缺少某些網路元件。然而，Bitcoin 對於開發目的而言非常有用。

### 公用鑰匙

公開金鑰在現今的實務中使用較少。隨著時間的推移，Bitcoin 使用者已使用位址來取代公開金鑰。它們仍然存在，而且偶爾仍會被使用。一般而言，公開金鑰是比地址長得多的字串。就像地址一樣，它們以特定的識別碼開始。


- 首先，`02...` 和`03...` 是以 SEC 格式編碼的非常標準的公開金鑰識別碼。這些識別碼可以被處理並轉換成接收地址、用於建立 multi-sig 地址或驗證簽章。早期的 Bitcoin 交易使用公開金鑰作為 P2PK 交易的一部分。
- 然而，HD wallets 使用不同的結構。xpub..."、"ypub... 「或 」zpub... "稱為擴展公鑰，而不是 xpub。這些金鑰用來衍生出許多公開金鑰，因為它是 HD Wallet 的一部分。由於您的 xpub 擁有您的整個歷史記錄，也就是過去和未來的交易記錄，所以絕對不要與不信任的人分享這些記錄。

### 技能摘要

在本節中，您學習了以下內容：


- 位址與公開金鑰資料類型的差異，以及使用位址而非公開金鑰的好處。

### 知識評估

說明與 Address 重複使用或公開金鑰方法相比，每次交易使用新地址的好處

## 使用 Hardware Wallet 保護金鑰

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### 儲存 Bitcoin 金鑰

生成 seed 短語後，在本書中生成的 12 - 24 個單詞列表需要適當的備份和安全性，因為這些單詞是恢復訪問 Wallet 的唯一方法。HD wallets 的結構以及它如何使用唯一的 seed 確定地產生位址，您所建立的所有位址都將使用代表您的 seed 或恢復短語的唯一 Mnemonic 字元清單進行備份。

妥善保管您的復原短語。如果有人存取，特別是惡意存取，他們可以移動您的資金。保持 seed 的安全可靠，但也要記住這是相互的。有幾種方法可以儲存 Bitcoin 私密金鑰，每種方法都有其好處和缺點，可以是安全性、隱私性、便利性或實體方式。由於私人金鑰的重要性，Bitcoin 使用者傾向於「自我保管」並安全地保存這些金鑰，而不是使用像銀行這樣的「保管」服務。視使用者而定，他必須使用 Cold 儲存方案或 Hot Wallet。

### Hot 和 Cold 儲存 Bitcoin 金鑰

通常，Bitcoin 錢包以 Hot Wallet 或 Cold Wallet 計值。大多數的取捨在於便利性、易用性和安全風險。這些方法中的每一種也都可以在託管人解決方案中看到。但是，這裡的權衡大多數是基於安全性和隱私權，超出了本課程的範圍。

### Hot Wallet

Hot 電子錢包是透過行動、網路或桌上型軟體與 Bitcoin 進行互動的最便利方式。Wallet 永遠連線至網際網路，讓使用者可以傳送或接收 Bitcoin。然而，這也是它的弱點，Wallet由於始終在線，現在更容易受到黑客或惡意軟件在您的設備上的攻擊。在 BTCPay 伺服器中，Hot 錢包會將私密金鑰儲存在實例上。如果有人惡意存取您的 BTCPay Server 商店，就可能從這個 Address 竊取資金。當 BTCPay 伺服器在託管環境中執行時，您應該在安全配置文件中經常考慮這一點，最好不要在這種情況下使用 Hot-Wallet。當BTCPay伺服器安裝在您擁有的硬體上，並受到您的保護和信任時，風險會顯著降低，但永遠不會消失！

### Cold Wallet

個人將 Bitcoin 移至 Cold Wallet 中，因為它可以將私人密碼匙與網際網路隔離。將網際網路連線從等式中移除可降低惡意軟體、間諜軟體和 SIM 卡交換的風險。只要採取足夠的預防措施避免遺失 Bitcoin 私密金鑰，Cold 儲存裝置的安全性與自主性相信會比 Hot 儲存裝置優勝。Cold 儲存裝置最適合大量的 Bitcoin，由於 Wallet 設定的複雜性，因此不打算經常使用。

如何在 Cold 儲存中儲存 Bitcoin 金鑰有各種方法，從紙錢包到腦錢包、硬體錢包，或從一開始就是 Wallet 檔案。大多數的錢包使用 BIP 39 來 generate seed 詞組。然而，在 Bitcoin 核心軟體內部，尚未就使用它達成共識。Bitcoin 核心軟體仍會 generate 一個 Wallet.dat 檔案，您需要將其儲存於安全的離線位置。

### 技能摘要

在本節中，您將學習到


- Hot 和 Cold 錢包在功能上的差異及其取捨。

### 知識評估 概念回顧


- 什麼是 Wallet？
- Hot 和 Cold 皮夾有什麼不同？
- 說明何謂「產生 Wallet」？

## 使用您的 Bitcoin 按鍵

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### BTCPay 伺服器 Wallet

BTCPay 伺服器包含下列標準 Wallet 功能：


- 交易
- 發送
- 接收
- 重新掃描
- 拉動付款
- 付款方式
- PSBT
- 一般設定

### 交易

管理員可以在交易檢視中查看與此特定儲存庫連接的 On-Chain Wallet 的進出交易。每個交易都有收到和發出的區別。收到的交易將為 Green，發出的交易將為紅色。在 BTCPay 伺服器的交易檢視中，管理員也會看到一組標準的標籤。

| 交易類型說明

| ---------------- | ---------------------------------------------------- |

| 應用程式 | 透過建立的 Invoice | 應用程式收到付款。

| Invoice | 付款是透過 Invoice | 收到的。

| PayJoin | 未付費，Invoice 計時器仍未過期 | Invoice | 未付費，Invoice 計時器仍未過期

| PayJoin-exposed | UTXO was exposed through an Invoice PayJoin proposal | | PayJoin-exposed

| 付款請求 | 付款是透過付款請求收到的

| 付出 | 付款是透過付出或退款寄出的 | 付款是透過付出或退款寄出的 | 付款是透過付出或退款寄出的

### 如何發送

BTCPay服務器的發送功能從您的BTCPay服務器On-Chain Wallet發送交易。BTCPay 伺服器允許多種方式簽署您的交易以花費資金。交易可以用以下方式簽名


- Hardware Wallet
- 支援 PSBT 的錢包
- HD 私密金鑰或復原種子。
- Hot Wallet

#### Hardware Wallet

BTCPay Server內建Hardware Wallet支援，讓您可以使用您的Hardware Wallet與BTCPay Vault，而不會洩漏資訊到第三方應用程式或伺服器。BTCPay 伺服器內的 Hardware Wallet 整合功能可讓您匯入您的 Hardware Wallet，只需在您的裝置上進行簡單的確認，即可花費收到的資金。您的私密金鑰從未離開裝置，所有資金均根據您的 Full node 進行驗證，因此不會發生資料洩漏。

#### 與支援 PSBT 的 Wallet 簽署

PSBT（部分簽章的Bitcoin交易）是仍需完全簽章的Bitcoin交易的交換格式。BTCPay 伺服器支援 PSBT，並可使用相容的硬體和軟體錢包簽章。

建構完整簽署的 Bitcoin 交易要經過以下步驟：


- PSBT 被建構出特定的輸入和輸出，但沒有簽章
- 匯出的 PSBT 可以由支援此格式的 Wallet 匯入
- 可以使用 Wallet 檢查和簽署交易資料。
- 經簽署的 PSBT 檔案會從 Wallet 匯出，並匯入 BTCPay 伺服器。
- BTCPay 伺服器產生最終的 Bitcoin 交易
- 您驗證結果並將其廣播至網路

#### 使用 HD 私密金鑰或 Mnemonic seed 簽署

如果您在使用BTCPay服務器之前已經創建了Wallet，您可以通過在適當的欄位中輸入您的私人密鑰來花費資金。在Wallet> Settings中設定適當的 "AccountKeyPath"；否則，您將無法花費。

#### 使用 Hot Wallet 簽署

如果您在設定商店時建立了新的 Wallet，並將其啟用為 Hot Wallet，它會自動使用儲存在伺服器上的 seed 來簽章。

### RBF (Replace-by-fee)

Replace-by-fee (RBF) 是 Bitcoin 通訊協定的一項功能，允許您取代先前廣播的交易（當時仍未確認）。這允許隨機化您的 Wallet 的交易指紋，或以較高的費率取代，使交易在確認 (Mining) 優先順序的佇列中排得更高。這將有效地取代原本的交易，因為較高的費率將獲得優先處理，一旦確認，原本的交易將無效（無重複花費）。

按下「進階設定」按鈕以檢視 RBF 選項；

![image](assets/en/16.webp)


- Randomize for higher privacy, 允許自動替換交易，以隨機化交易指紋。
- 是，標記 RBF 的交易，並明確地替換（預設不替換，僅由輸入替換）。
- 否，不允許交易被取代。

### 硬幣選擇

硬幣選擇是一種先進的隱私增強功能，可讓您在製作交易時選擇要花費的硬幣。例如，使用剛結合混合的硬幣付款。

硬幣選擇可與 Wallet 標籤功能搭配使用。這可讓您標示收到的資金，使 UTXO 的管理和支出更順暢。

BTCpay 伺服器也支援 BIP-329 標籤管理。BIP-329允許使用標籤；如果您從支援此特定BIP的Wallet轉移並設定標籤，BTCPay伺服器將識別並匯入這些標籤。當遷移伺服器時，這些資訊也可以匯出並匯入新的環境。

### 如何接收

當在BTCPay伺服器中點擊接收按鈕時，會產生一個未使用的Address，可用於接收付款。管理員也可以通過生成一個新的 "Invoice" 來 generate 一個新的 Address。

BTCPay 伺服器總是會要求 generate 下一個可用的 Address，以避免 Address 重複使用。點擊 "generate next available BTC Address "後，BTCPay伺服器會生成一個新的Address和QR。它還允許您直接設置一個Label到Address，以便更好地管理您的地址。

![image](assets/en/17.webp)

![image](assets/en/18.webp)

#### 重新掃描

重新掃描功能依賴 Bitcoin Core 0.17.0 的 "Scantxoutset" 來掃描 Blockchain （稱為 UTXO Set）的當前狀態，尋找屬於配置的衍生方案的硬幣。Wallet rescan 解決了 BTCPay 伺服器使用者遇到的兩個問題。

1.間隙限制問題 - 大多數第三方錢包是許多使用者共用一個節點的輕型錢包。輕型和依賴 Full node 的錢包會限制他們在 Blockchain 上追蹤的沒有餘額的地址數量（通常是 20 個），以防止性能問題。BTCPay 伺服器會為每個 Invoice 產生一個新的 Address。考慮到以上情況，當BTCPay伺服器連續產生20筆未支付的發票後，外部Wallet會假設沒有新的交易發生而停止擷取交易。一旦發票在 21 號、22 號等日期支付，您的外部 Wallet 就不會顯示這些交易。另一方面，在內部，BTCPay 伺服器 Wallet 會追蹤它所產生的任何 Address，以及更大的差距限制。它不依賴第三方，總能顯示正確的餘額。

2.間隙限制解決方案 - 如果您的 [外部/現有 Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet)允許間隙限制配置，簡單的解決方法就是增加間隙限制。但是，大多數的錢包都不允許這樣做。我們知道的唯一允許間隙限制配置的錢包是 Electrum、Wasabi 和 Sparrow Wallet。不幸的是，您很可能會在其他許多錢包上遇到問題。為了獲得最佳的用戶體驗和隱私，請考慮捨棄外部錢包，使用 BTCPay 伺服器內部的 Wallet。

#### BTCPay 伺服器使用 "mempoolfullrbf=1"

BTCPay Server使用 "mempoolfullrbf=1"；我們已將其作為預設添加到您的BTCPay Server設置中。不過，您也可以自行停用此功能。如果沒有 "mempoolfullrbf=1"，如果客戶雙重花費了一個交易而沒有發出RBF的信號，商家只有在確認後才會知道。

管理員可能想要選擇不使用此設定。透過下列字串，您可以變更設定的預設值。

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### BTCPay 伺服器 Wallet 設定

BTCPay Server 中的 Wallet 設定可讓您清楚快速地瞭解 Wallet 的一般設定。如果 Wallet 是使用 BTCPay Server 建立的，則所有這些設定都會預先填入。

![image](assets/en/19.webp)

BTCPay Server 中的 Wallet 設定可讓您清楚快速地瞭解 Wallet 的一般設定。如果Wallet是使用BTCPay Server創建的，所有這些設置都是預先填寫的。BTCPay Server的Wallet設置從Wallet狀態開始。是只看Wallet還是Hot Wallet？根據Wallet的類型，動作可能會有所不同，包括重新掃描Wallet以檢查是否有遺失的交易、從歷史中刪除舊的交易、註冊Wallet的付款連結，或更換和刪除目前附加到商店的Wallet。在 BTCPay 伺服器的 Wallet 設定中，管理員可以為 Wallet 設定標籤，以便更好地管理 Wallet。在此，管理員還可以看到衍生方案、帳號金鑰 (xpub)、指紋和密鑰路徑。Wallet 設定中的付款只有 2 個主要設定。如果交易未能在 Invoice 過期後（設定的分鐘內）確認，則付款無效。當付款交易有 X 數量的確認時，視為 Invoice 已確認。管理員也可以在付款時設定切換顯示建議費用，或在區塊數設定手動確認目標。

![image](assets/en/20.webp)

**！注意！**

如果您自己學習本課程，您可能會在第三方主機上建立此帳戶，因此我們再次提醒您切勿將這些帳戶用於生產環境，而只能用於訓練目的。

### 範例

#### 在 BTCPay 伺服器設定 Bitcoin Wallet

BTCPay 伺服器允許兩種 Wallet 設定方式。一種方式是匯入已存在的 Bitcoin Wallet。匯入的方式有：連接Hardware Wallet、匯入Wallet檔案、輸入擴展公開金鑰、掃瞄Wallet的QR碼，或最不理想的方式，手動輸入先前建立的Wallet復原seed。在 BTCPay 伺服器中，也可以建立新的 Wallet。在生成新的 Wallet 時，有兩種可能的方式配置 BTCPay Server。

BTCPay Server中的Hot Wallet選項允許 "PayJoin 「或 」Liquid "等功能。但是，有一個缺點，為這個 Wallet 產生的恢復 seed 將儲存在伺服器上，任何擁有管理控制權的人都可以在伺服器上取得恢復 seed。由於您的私密金鑰來自於您的復原 seed，因此惡意的人可以取得您目前和未來的資金！

為了降低BTCPay伺服器的這種風險，管理員可以在伺服器設置 > 政策 > 「允許非管理員為他們的商店創建Hot錢包 」設置為 「否」，預設值為 「否」。為了加強 Hot 錢包的安全性，伺服器管理員應該對允許擁有 Hot 錢包的帳戶啟用 2FA 認證。在公共伺服器上儲存私人密碼匙是危險的，而且會帶來風險。有些風險與 Lightning Network 風險類似 (請參閱下一章的 Lightning Network 風險)。

BTCPay伺服器在產生新的Wallet時提供的第二個選擇是通過創建一個Watch-only wallet。BTCPay伺服器會generate您的私人金鑰一次。在用戶確認寫下他們的seed短語後，BTCPay伺服器將從伺服器上清除私人密碼匙。因此，您的商店現在只連接了一個Watch Wallet。要使用您的Watch-only wallet收到的資金，請參閱 如何發送 一章，可以使用BTCPay伺服器Vault，PSBT (Partially Signed Bitcoin Transaction)，或者，最不推薦的，手動提供您的seed短語。

您在上一部分建立了一個新的 「商店」。安裝精靈會繼續要求「設定一個 Wallet」或「設定一個 Lightning 節點」。在本範例中，您將遵循「設定 Wallet」精靈程序 (1)。

![image](assets/en/21.webp)

點擊 "Set up a Wallet "後，精靈會繼續要求您如何繼續；BTCPay伺服器現在提供連接現有Bitcoin Wallet到您的新商店的選項。如果您沒有Wallet，BTCPay伺服器會建議您建立一個新的Wallet。本範例將採用 「創建一個新的Wallet 」的步驟(2)。按照步驟學習如何 「連接現有的Wallet (1)」。

![image](assets/en/22.webp)

**！注意！**

如果您在教室上課，我們目前產生的範例和 seed 僅供教學使用。在這些位址的整個練習過程中，絕不應該有任何要求以外的大量內容。

(1) 按一下「建立新的 Wallet」按鈕，繼續「建立新的 Wallet」精靈。

![image](assets/en/23.webp)

(2) 點選 「建立新的 Wallet 」後，精靈的下一個視窗將會提供 "Hot Wallet「 和 」Watch-only wallet" 兩個選項。如果您跟隨導師，您的環境是共用的 Demo，您只能建立 Watch-only wallet。請注意以下兩張圖的差異。當您在 Demo 環境中跟隨教師，請建立「Watch-only wallet」並繼續使用「New Wallet」精靈。

![image](assets/en/24.webp)

![image](assets/en/25.webp)

(3) 繼續新的Wallet精靈，現在您在創建BTC Watch-only wallet部分。在這裡，我們可以設定 Wallet 「Address 類型」 BTCPay 伺服器允許您選擇您偏好的 Address 類型；在撰寫本課程時，仍建議使用 bech32 位址。有關地址的詳細資訊，請參閱本部分的第一章。


- SegWit (bech32)
  - 本地 SegWit 是以 `bc1q` 開頭的位址。
  - 範例： `bc1qXXXXXXXXXXXXXXXX`
- 傳統
  - 傳統位址是以數字 `1` 開頭的位址。
  - 範例： `15e15hXXXXXXXXXXXXXX`
- Taproot (進階使用者適用)
  - Taproot 位址以 `bc1p` 開頭。
  - 範例： `bc1pXXXXXXXXXXXXXXXXXX`
- SegWit 包裝
  - SegWit wrapped 是以 `3` 開頭的位址。
  - 範例： `37BBXXXXXXXXXXXX`

選擇 SegWit（推薦）作為您的首選 Wallet Address 類型。

![image](assets/en/26.webp)

(4)當設定Wallet的參數時，BTCPay伺服器允許用戶通過BIP39設定一個可選的passphrase，請務必確認您的密碼。

![image](assets/en/27.webp)

(5) 設定Wallet的Address類型，並可能設定一些進階選項後，點擊 「創建」，BTCPay伺服器將generate您的新Wallet。請注意，這是生成seed短語前的最後一個步驟。請確保您只在一個不會被人從您的螢幕上盜取seed短語的環境中進行此步驟。

![image](assets/en/28.webp)

(6) 在精靈的以下畫面中，BTCPay伺服器會為您顯示新產生的Wallet的恢復seed短語；這些是恢復您的Wallet和簽署交易的關鍵。BTCPay Server會生成一個包含12個單詞的seed短語。這些詞彙將在此設置畫面後從伺服器中刪除。這個Wallet特別是Watch-only wallet。建議不要將此 seed 短語以數位或攝影圖片的方式儲存。使用者只有在主動確認寫下 seed 詞組後，才能進一步進入精靈。

![image](assets/en/29.webp)

(7) 點擊 「完成 」並確保新生成的Bitcoin seed短語後，BTCPay伺服器將使用所附的新Wallet更新您的商店，並準備好接收付款。在用戶Interface中，在左側導航菜單中，注意Bitcoin現在是如何高亮並在Wallet下被激活的。

![image](assets/en/30.webp)

### 範例：寫下 seed 詞組

這是使用 Bitcoin 的非常特殊和安全的時刻。如前所述，只有您才能存取或瞭解您的 seed 詞組。當您跟隨教師和教室時，產生的 seed 只應該在本課程中使用。太多的因素、同學的窺視、不安全的系統，以及其他許多因素，使得這些金鑰只能用來教學，而不能被信任。不過，所產生的金鑰仍應儲存在課程範例中。

在目前的情況下，我們要使用的第一個方法，也是最不安全的方法，就是按照正確的順序寫下 seed 詞組。seed 短語卡在提供給學生的教材中，或在 BTCPay 伺服器 GitHub 上找到。我們將使用這張卡片來寫下上一步產生的單字。請確保以正確的順序寫下它們。在您寫下這些詞彙後，請與軟體所給的詞彙進行核對，以確保您寫下的順序正確。寫完後，按一下核取方塊，說明您已正確寫下 seed 詞組。

### 範例：在 Hardware Wallet 上儲存 seed 詞組

在本課程中，我們會觸及在 Hardware Wallet 上儲存 seed 詞組。由導師跟進本課程，有時可能才會包含這樣的裝置。在課程中，導師材料已寫出提供的硬體錢包清單，將符合這項練習。

本範例中，我們將使用 BTCPay Server vault 和 Blockstream Jade Hardware Wallet。

您也可以透過視訊來參考連接 Hardware Wallet 的方法。

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::

下載 BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases

請確保您為您的系統下載正確的檔案。Windows用戶請下載[BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe)套件，Mac用戶請下載[BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg)，Linux用戶請下載[BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

安裝BTCPay Server Vault後，點擊桌面上的圖標啟動軟件。當BTCPay Server Vault安裝完成並首次啟動時，它會要求允許與Web應用程式一起使用。它會要求授予您使用特定BTCPay伺服器的權限。接受這些條件。BTCPay Server Vault現在將搜索硬體設備。一旦找到設備，BTCPay伺服器將認識到Vault正在運行，並已獲取您的設備。

**！注意！**

使用 Hot Wallet 時，除管理員外，切勿將您的 SSH 金鑰或伺服器管理帳戶交給其他人。任何可以存取這些帳號的人都可以存取 Hot Wallet 中的資金。

### 技能摘要

在本節中，您學習了以下內容：


- Bitcoin Wallet 的交易視圖及其各種分類。
- 從 Bitcoin Wallet 傳送時，從硬體到 Hot 錢包都有各種選項。
- 使用大多數錢包時面臨的間隙限制問題，以及如何糾正這個問題。
- 如何在 BTCPay 伺服器內 generate 新 Bitcoin Wallet，包括在 Hardware Wallet 儲存金鑰和備份復原短語。

在此目標中，您已學會如何在 BTCPay 伺服器內 generate 新 Bitcoin Wallet。我們尚未討論如何保護或使用這些金鑰。在此目標的快速概述中，您已學會如何建立第一個商店。您已學會如何 generate 一個 Bitcoin 復原 seed 詞組。

### 知識評估實務複習

描述產生金鑰的方法和保護金鑰的方案，以及安全方案的權衡/風險。

## BTCPay 伺服器 Lightning Wallet

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

當伺服器管理員配置一個新的BTCPay伺服器實例時，他可以設置Lightning Network實現、LND、Core Lightning或Eclair；更詳細的安裝說明請參閱配置BTCPay伺服器部分。

如果在課堂上跟隨，連接一個Lightning節點到您的BTCPay伺服器是通過Custom節點工作的。如果用戶不是BTCPay伺服器的伺服器管理員，則默認不能使用內部的Lightning節點。這是為了保護伺服器擁有者的資金免受損失。服務器管理員可以安裝一個插件，通過LNBank訪問他們的Lightning節點；這不在本書的範圍內；請在官方插件頁面上閱讀更多關於LNBank的資訊。

### 連接內部節點 (伺服器管理員)

伺服器管理員可以使用BTCPay伺服器內部的Lightning節點。無論Lightning實現方式如何，連接內部Lightning節點的方式都是一樣的。

轉到之前的設置商店，點擊左邊菜單中的 "Lightning" Wallet。BTCPay 伺服器提供兩種設定可能性，使用內部節點 (預設只限伺服器管理員) 或自訂節點 (外部連線)。伺服器管理員可點擊 「使用內部節點 」選項。不需要進一步的設定。點擊 「保存 」按鈕，並注意到 「BTC Lightning 節點已更新 」的通知。商店現在已成功獲得 Lightning Network 功能。

### 連接外部節點 (伺服器使用者/儲存庫擁有者)

由於店主預設不允許使用伺服器管理員的Lightning Node。連接需要連接到外部節點，可以是 BTCPay 伺服器設置之前店主擁有的節點，也可以是伺服器管理員提供的 LNBank 外掛，或者是 Alby 之類的託管人解決方案。

進入先前設定的商店，點選左邊功能表中錢包下方的「Lightning」。由於預設不允許店主使用內部節點，因此此選項為灰色。使用自訂節點是店主預設唯一的選項。

BTCPay伺服器需要連接資訊；之前製作的（或託管解決方案）將提供特定於Lightning實施的此資訊。在BTCPay伺服器內，商店擁有者可以使用以下連接；


- C-lightning 透過 TCP 或 Unix domainocket 連線。
- 透過 HTTPS 進行閃電充電
- 透過 HTTPS 的 Eclair
- LND 透過 REST 代理
- 透過 REST API 的 LNDhub

![image](assets/en/31.webp)

點擊 "test connection"（測試連接）以確保您正確輸入連接詳細資料。連接確認無誤後，點擊 「保存」，BTCPay伺服器會顯示商店已更新為Lightning節點。

### 管理內部 Lightning 節點 LND (伺服器管理員)

連接內部 Lightning 節點後，伺服器管理員將注意到儀表板上專為 Lightning 資訊而設的新磁磚。


- 閃電平衡
- 渠道中的 BTC
  - BTC 開放管道
  - BTC 當地餘額
  - BTC 遠端餘額
  - BTC 關閉通道
- BTC On-Chain
  - 確認 BTC
  - BTC 未確認
  - 保留 BTC
- 閃電服務
  - Ride the Lightning (RTL)。

點選「Lightning 服務」磁磚中的「Ride the Lightning Logo」或左邊功能表中錢包下方的「Lightning」，伺服器管理員就可以到達 RTL 進行 Lightning 節點管理。

**注意！**

連接內部 Lightning 節點失敗 - 如果內部連接失敗，請確認：

1.Bitcoin On-Chain 節點完全同步

2.在 「閃電」>「設定」>「BTC 閃電設定 」下，內部閃電節點為 「已啟用」

如果您無法連線到您的閃電節點，請嘗試重新啟動您的伺服器，或閱讀BTCPay伺服器官方文件; https://docs.btcpayserver.org/Troubleshooting/ 了解更多詳情。在您的Lightning節點出現 「在線 」之前，您不能在您的商店中接受Lightning付款。點擊 "Public Node Info "鏈接測試您的Lightning連接。

### 閃電 Wallet

在左側菜單欄的Lightning Wallet選項中，伺服器管理員可以輕鬆訪問RTL、公共節點資訊以及BTCPay伺服器商店特定的Lightning設置。

#### 內部節點資訊

伺服器管理員可以按一下內部節點資訊，並查看其伺服器狀態 (線上/離線) 以及 Clearnet 或 Tor 的連線字串。

![image](assets/en/32.webp)

#### 變更連接

如果店主決定使用 Lightning Settings - Change connection 內的 changed。

在公共節點資訊商店旁邊，擁有者可以找到這個選項。它會帶回外部 Lightning 節點連線的初始設定，填寫新的 Lightning 節點資訊，按一下儲存，然後用新的節點資訊更新商店。

![image](assets/en/33.webp)

#### 服務

如果伺服器管理員決定為 Lightning 實作安裝多種服務，則會在此列出。有了標準的 LND 實作，管理員將有 Ride The Lightning (RTL) 作為節點管理的標準工具。

#### BTC Lightning Wallet 設定

在之前的步驟中將Lightning節點加入商店後，在Lightning Wallet的設定中，店主仍可使用Lightning設定頂端的Toggle選擇停用它。

![image](assets/en/34.webp)

#### 閃電付款選項

店主可為下列項目設定參數，以提升客戶的 Lightning 體驗。


- 以 Satoshis 顯示 Lightning 付款金額。
- 在 Lightning Invoice 中加入私人頻道的跳躍提示。
- 在結帳時統一 On-Chain 和 Lightning 付款 URL/QR 代碼。
- 設定閃電發票的描述範本。

#### LNURL

店主可以選擇使用或不使用LNURL。Lightning Network URL或LNURL是Lightning Payer和收款人之間互動的建議標準。簡而言之，LNURL 是以 lnurl 為前綴的 bech32 編碼 URL。預期 Lightning Wallet 會解碼 URL、聯絡 URL，並等待包含進一步指示的 JSON 物件，最主要的是定義 knurl 行為的標籤。


- 啟用 LNURL
- LNURL 經典模式
  - 為了與 Wallet 相容，Bech32 編碼 (classic) vs 明文 URL (即將推出)
- 允許收款人傳送註解。

### 範例 1

#### 使用內部節點 (管理員) 連線至 Lightning

只有當您是此實例的管理員，或管理員已變更使用者可以使用內部閃光節點的預設設定時，此選項才可用。

作為管理員，點擊左邊菜單欄中的Lightning Wallet。BTCPay伺服器會要求使用兩個連接Lightning節點的選項之一，內部節點或自定義外部節點。點擊使用內部節點，然後點擊保存。

#### 管理您的 Lightning 節點 (RTL)

連接至內部閃電節點後會更新BTCPay伺服器，並顯示 "BTC Lightning node updated "通知，確認您已連接閃電至您的商店。

管理閃光節點是伺服器管理員的工作。這包括


- 管理交易
- 管理流動資金
  - 入境流動資金
  - 出境流動資金
- 管理同儕和通路
  - 連接的同業
  - 頻道費用
  - 頻道狀態
- 頻繁備份通道狀態。
- 檢查路由報告
- 或者，使用 Loop 等服務。

所有的 Lightning 節點管理都是以 RTL 作為標準 (假設您是在 LND 上執行)。管理員可以在 BTCPay 伺服器點選他們的 Lightning Wallet，找到開啟 RTL 的按鈕。BTCPay 伺服器的主儀表板現在已更新為 Lightning Network Tiles，包括快速存取 RTL。

### 範例 2

#### 與 Alby 連接至閃電

與 Alby 等保管人連線時，店主應先建立帳戶，請造訪：https://getalby.com/。

![image](assets/en/35.webp)

建立 Alby 帳戶後，前往您的 BTCPay 伺服器商店。

步驟 1：點選儀表板上的「設定閃電節點」或錢包下方的「閃電」。

![image](assets/en/36.webp)

步驟 2: 插入 Alby 提供的 Wallet 連線憑證。在 Alby 的儀表板上，點選 Wallet。在這裡您可以找到「Wallet 連線憑證」。複製這些認證。將 Alby 提供的連線憑證貼到 BTCPay 伺服器的連線設定欄位。

![image](assets/en/37.webp)

步驟 3: 向BTCPay伺服器提供連接細節後，點擊 "Test Connection "按鈕以確保連接正常。請注意螢幕上方的 "Connection to lightning node successful "訊息。這證明一切運作正常。

![image](assets/en/38.webp)

步驟 4：按一下儲存，您的店鋪現在與 Alby 的閃光節點連接。

![image](assets/en/39.webp)

**！注意！**

永遠不要相信保管人 Lightning 解決方案的價值超過您願意失去的價值。

### 技能摘要

在本節中，您將學習到


- 如何連接內部或外部 Lightning 節點
- 儀表板中各種 Lightning 相關磁磚的內容和功能
- 如何使用電壓突波或 Alby 設定 Lightning Wallet

### 知識評估 實務回顧

描述將 Lightning Wallet 連接到商店的一些不同選項。

# BTCPay 伺服器 Interface

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## 儀表板概觀

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server是一個模組化的軟體套件。然而，每台BTCPay伺服器都會有一些標準，管理員/用戶會與之互動。從儀表板開始。每個BTCPay服務器在登錄後的主要入口。儀表板提供了您的商店的表現，Wallet的當前餘額，以及在過去7天的最後tx的概述。由於這是一個模組化的檢視，外掛程式可以利用這個檢視，並在儀表板上建立自己的磁磚。在本課程中，我們將只討論 BTCPay 伺服器中的標準外掛程式/應用程式及其各自的檢視。

### 儀表板磁磚

在BTCPay伺服器儀表板的主視圖中，有幾個標準的磁磚。這些磁磚是為了讓店主或管理員能夠快速地在一個總覽中管理他的商店。


- Wallet 平衡
- 交易活動
- 閃電餘額 (如果商店已啟用閃電)
- Lightning 服務 (如果商店已啟用 Lightning)
- 最近的交易。
- 近期發票
- 目前活躍的集資
- 店舖績效 / 最暢銷商品。

### Wallet 平衡

Wallet Balance 磁磚提供 Wallet 資金和績效的快速概覽。它可以用 BTC 或法定貨幣以每週、每月或每年的圖表檢視。

![image](assets/en/40.webp)

### 交易活動

在Wallet餘額磁磚旁邊，BTCPay伺服器會顯示待定付款的快速概覽、過去7天的交易金額，以及您的商店是否已發出任何退款。點擊 「管理 」按鈕將進入待付款管理（在BTCPay伺服器 - 付款章節了解更多關於付款的資訊）。

![image](assets/en/41.webp)

### 閃電平衡

只有啟動「閃電」時才會顯示。

當管理員允許Lightning Network訪問時，BTCPay伺服器儀表板現在有一個新的磁磚，包含您的閃電節點資訊。有多少 BTC 在通道中，這是如何平衡本地或遠程（入站或出站流動資金），如果通道正在關閉或開啟，以及有多少 Bitcoin 在閃電節點上持有 On-Chain。

![image](assets/en/42.webp)

### 閃電服務

這只有在閃電啟動時可見。

除了在BTCPay伺服器儀表板上看到您的Lightning餘額，管理員還可以看到Lightning服務磁磚。在這裡，管理員可以找到他們用來管理Lightning節點的工具的快速按鈕；例如，Ride the Lightning是BTCPay Server用來管理Lightning節點的標準工具之一。

![image](assets/en/43.webp)

### 近期交易

最近交易磁磚將顯示您商店最近的交易。只需點擊一下，BTCPay 伺服器實例的管理員現在就可以看到最新的交易，並查看是否需要對其進行關注。

![image](assets/en/44.webp)

### 最近的發票

最近發票磁磚顯示 BTCPay 伺服器產生的 6 張最新發票，包括狀態和 Invoice 金額。該磁磚也包含「檢視全部」按鈕，可輕鬆存取完整的 Invoice 概觀。

![image](assets/en/45.webp)

### 銷售點與集資

由於 BTCPay Server 提供一套標準的外掛或應用程式，Point Of Sale 和 Crowdfund 是 BTCPay Server 的兩個主要外掛。每個商店和Wallet，BTCPay伺服器用戶可以generate他認為合適的銷售點或集資。每個都會創建一個新的儀表板磁磚，顯示插件的性能。

![image](assets/en/46.webp)

請注意 Point of Sale 和 Crowdfund 磁磚之間的微小差異。管理員在銷售點磁磚中看到銷量最高的項目。在 Crowdfund 動態磚，這變成了 Top Perks。這兩個磁磚都有快速按鈕，可管理各自的應用程式，並檢視最近由最高項目或最高獎勵建立的發票。

![image](assets/en/47.webp)

**注意！

餘額圖表和最近交易僅適用於 On-Chain 付款方式。有關 Lightning Network 結餘和交易的資訊在待辦事項中。自BTCPay服務器版本1.6.0起，基本的Lightning Network餘額可用。

### 技能摘要

在本節中，您學習了以下內容：


- 主要登陸頁面上磁磚的核心佈局稱為儀表板。
- 基本瞭解每個瓷磚的內容。

### 知識評估檢閱

從 Dashboard 盡量列出記憶中的磁磚。

## BTCPay 伺服器 - 商店設定

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>

在BTCPay伺服器軟體中，我們知道有兩種類型的設定。BTCPay服務器商店特定設置，可在儀表板下方左側菜單欄中找到設置按鈕；BTCPay服務器設置，可在賬戶上方菜單欄底部找到。BTCPay伺服器的伺服器特定設置只能由伺服器管理員查看。

商店設定包含許多標籤，可將每組設定分類。


- 一般
- 價格
- 結帳外觀
- 存取代幣
- 使用者
- 角色
- Webhooks
- 付款處理器
- 電子郵件
- 表格

### 一般

在「一般設定」標籤中，店主可設定其品牌和付款預設值。在商店初始設定時，會給出商店名稱；這會反映在商店名稱下的一般設定中。店主也可在此設定與品牌相符的網站，以及供管理員在資料庫中辨識的商店 ID。

#### 品牌

由於 BTCPay 伺服器是 FOSS，店主可以自訂品牌以配合其商店。設定品牌顏色、儲存您的品牌標誌，並為公開/面向客戶的頁面 (發票、付款申請、拉動付款) 新增自訂 CSS。

#### 付款方式

在付款設定中，店主可設定其商店預設貨幣（Bitcoin 或任何法定貨幣）。

#### 允許任何人建立發票

此設定適用於 BTCPay 伺服器之上的開發者或建置者。為您的商店開啟此設定後，就能讓外部世界在您的 BTCPay 伺服器實例上建立發票。

#### 在發票上增加附加費（網路費

BTCPay內的一項功能，以保護商家免受Dust攻擊，或客戶日後當商家需要一次移動很多Bitcoin時，推動高成本的費用。例如，客戶創建了一個20$的Invoice，並支付了一部分，支付了20次1$，直到Invoice完全支付。商家現在有一個更大的交易，增加了Mining的成本，以防商家稍後決定移動這些資金。預設情況下，當Invoice分多次交易支付時，BTCPay會在Invoice的總金額上加上額外的網路費用，以支付商家的該筆費用。BTCPay提供多種選項來自定義此保護功能。您可以套用網路費用：


- 只有在客戶為 Invoice 支付超過一次的情況下（在上述示例中，如果客戶為 20\$ 創建了一個 Invoice，並支付了 1\$ ，則現在應付的 Invoice 總額為 19\$ + 網絡費。網絡費用會在第一次付款後使用）。
- 每筆付款（包括第一筆付款，在我們的例子中，總額將為 20\$ + 網絡費，即使是第一筆付款也是如此）
- 永不增加網路費用 (完全停用網路費用)

雖然它可以防止 Dust 交易，但如果溝通不當，也會對企業造成負面影響。客戶可能會有額外的問題，並認為您多收了他們的費用。

#### 如果 Invoice 在?

Invoice 計時器預設為 15 分鐘。該計時器是一種防止波動的保護機制，因為它根據 Bitcoin 鎖定 Bitcoin 金額至法定費率。如果客戶未在定義的時間內支付 Invoice，則 Invoice 會被視為過期。一旦 Blockchain 上顯示交易（0-確認），Invoice 即視為 「已支付」，但當交易達到商家定義的確認次數（通常為 1-6）時，Invoice 即視為 「完成」。計時器可自訂分鐘數。

#### 即使已付金額比預期少 X%，也視為 Invoice 已付？

當客戶使用 Exchange Wallet 直接支付 Invoice 時，Exchange 會收取少量費用。這表示這樣的 Invoice 並未被視為完全完成。Invoice 的狀態為 「部分支付」。如果商家想要接受未付的發票，您可以在此設定百分比率。

### 價格

在BTCPay伺服器中，當產生Invoice時，它總是需要最新和最準確的Bitcoin法幣價格。在 BTCPay 伺服器中建立新商店時，管理員會被要求設定他們偏好的價格來源；商店建立後，店主可以隨時在此頁籤中變更他們的價格來源。

#### 進階速率規則腳本

主要供功能強大的使用者使用。如果開啟，店主可以針對價格行為以及如何向客戶收費建立腳本。

#### 測試

快速測試您偏好的貨幣對。這也包括透過 REST 查詢檢查預設貨幣對的功能。

### 結帳外觀

結帳外觀」標籤以 Invoice 特定設定和預設付款方式開始，並在符合設定要求時啟用特定付款方式。

#### Invoice 設定

預設付款方式。BTCPay 伺服器在標準配置中有三個選項。


- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain & Lightning)

我們可以為商店設定參數，當價格小於 X 時，顧客才會與 Lightning 進行互動；反之亦然，當 X 大於 Y 時，On-Chain 交易總會顯示 On-Chain 付款選項。

![image](assets/en/48.webp)

#### 結帳

從BTCPay伺服器1.7版開始，引入了新的結帳Interface，也就是所謂的結帳V2。由於 1.9 版已標準化，管理員和店主仍可將結帳設定為之前的版本。通過使用 「使用經典結帳 」切換鍵，店主可以將商店設置回之前的結帳體驗。BTCPay 伺服器也有一套精選的預設，適用於線上商務或店內體驗。

![image](assets/en/49.webp)

當客戶與商店互動並產生Invoice時，Invoice會有一個過期時間。預設情況下，BTCPay伺服器將此設定為5分鐘，而管理員可以將此設定為任何他們認為合適的時間。結帳頁面可以通過檢查以下參數進一步自定義：


- 展示彩紙慶祝付款
- 顯示商店標題（名稱和標誌）
- 顯示「Pay in Wallet」按鈕
- 統一 On-Chain 和 off-chain 付款 URL/QR
- 以 Satoshis 顯示閃電付款金額
- 結帳時自動偵測語言

![image](assets/en/50.webp)

當未設定自動偵測語言時，BTCPay伺服器預設會顯示英文。店主可以將預設變更為自己喜歡的語言。

![image](assets/en/51.webp)

按一下下拉選項，店主就可以設定自訂 HTML 標題，顯示在結帳頁面上。

![image](assets/en/52.webp)

為了確保客戶知道自己的付款方式，店主可以明確設定結帳時總是要求用戶選擇自己喜歡的付款方式。當 Invoice 支付完成後，BTCPay 伺服器會允許客戶返回網路商店。店主可以在客戶付款後自動設定此重定向。

![image](assets/en/53.webp)

#### 公開收據

在公開收據設定中，店主可以將收據頁面設定為公開，並在收據頁面上顯示付款清單和收據的 QR 代碼，方便顧客以數位方式取得收據。

![image](assets/en/54.webp)

### 存取代幣

存取權限用於與特定電子商務整合或客製化整合配對。

![image](assets/en/55.webp)

### 使用者

商店使用者是店主管理員工、他們的帳戶以及商店存取權限的地方。員工建立帳戶後，店主可以添加特定用戶到商店作為訪客用戶或店主。要進一步定義員工的角色，請參考下一節 「BTCPay 伺服器商店設定 - 角色」。

![image](assets/en/56.webp)

### 角色

店主可能覺得使用者的標準角色不夠重要。在自訂角色設定中，店主可以定義業務中每個角色的確切需求。

(1) 若要建立新角色，請按一下「+ 新增角色」按鈕。

![image](assets/en/57.webp)

(2) 輸入角色名稱，例如「出納」。

![image](assets/en/58.webp)

(3) 設定角色的個別權限。


- 修改您的商店。
- 管理與您的商店連結的 Exchange 帳戶。
  - 檢視與您的商店連結的 Exchange 帳戶。
- 管理您的拉動付款。
- 建立拉動付款。
  - 建立未核准的拉動付款。
- 修改發票。
  - 檢視發票。
  - 建立 Invoice。
  - 從與商店相關的閃電節點建立發票。
- 檢視您的商店。
  - 檢視發票。
  - 檢視您的付款要求。
  - 修改商店的 webhooks。
- 修改您的付款要求。
  - 檢視您的付款要求。
- 使用與您商店相關的閃光節點。
  - 檢視與您商店相關的閃電發票。
  - 從與商店相關的閃電節點建立發票。
- 將資金存入與您的商店連結的 Exchange 帳戶。
- 從 Exchange 帳戶提款到您的商店。
- 在您商店的 Exchange 帳戶上交易資金。

在建立角色時，角色名稱是固定的，在編輯模式下不能變更。

![image](assets/en/59.webp)

### Webhooks

在BTCPay伺服器內，建立一個新的 "Webhook "是相當容易的。在 BTCPay Server 商店設置 - Webhooks 標籤中，店主可以通過點擊 「+ 創建 Webhook 」輕鬆創建新的 Webhook。Webhooks 允許 BTCPay 伺服器發送與您的商店相關的 HTTP 事件給其他伺服器或電子商務整合。

![image](assets/en/60.webp)

現在您已進入建立 Webhook 的視圖。確保您知道您的有效載荷 URL，並將其粘貼到您的 BTCPay 伺服器。當您貼上有效負載 URL 時，下方會顯示 Webhook 秘訣。複製webhook secret並在端點上提供。一切設定完成後，您可以在 BTCPay Server 中切換到自動重新交付。我們將嘗試在 10 秒、1 分鐘以及 10 分鐘後重新傳送任何失敗的傳送，最多 6 次。您可以在每個事件之間切換，或根據您的需要指定事件。請務必啟用 webhook，並點擊「新增 webhook」儲存。

![image](assets/en/61.webp)

Webhooks與Bitpay API不相容。在BTCPay伺服器中有兩個獨立的IPN（用BitPay的術語："Instant Payment Notifications"）。


- Webhookp
- 通知

僅在透過 Bitpay api 建立發票時使用通知 URL。

### 付款處理器

Payout 處理器與 BTCPay 伺服器中的 Payouts 概念共同運作。支付聚合器可批量處理多筆交易並一次發送。有了支付處理器，店主可以自動化批量支付。BTCPay Server提供兩種自動化支付的方法，On-Chain和off-chain (LN)。

店主可以單擊並分別設定這兩個付款處理器。店主可能只想每 X 小時執行一次 On-Chain 處理器，而 off-chain 則可能每幾分鐘執行一次。對於 On-Chain，您也可以設定應該包含哪一區塊的目標。預設值為 1（或下一個可用區塊）。請注意，設定 off-chain 付款處理器只有間隔計時器，而沒有區塊目標。Lightning Network 的付款是即時的。

![image](assets/en/62.webp)

![image](assets/en/63.webp)

店主只有在 Hot-Wallet 連接到其商店時，才能設定 On-Chain 處理器。

![image](assets/en/64.webp)

在設置支付處理程序後，您可以返回BTCPay伺服器商店設置中的支付處理程序標籤，快速移除或修改該處理程序。

**注意！

支付處理器On-Chain - 鏈上支付處理器只能在配置有Hot Wallet連接的商店上工作。如果沒有連接Hot Wallet，BTCPay伺服器不會持有Wallet的鑰匙，也就無法自動處理支付。

### 電子郵件

BTCPay Server可以使用Email來發送通知，或者當設定正確時，可以恢復在實例上建立的賬戶，標準的BTCPay Server不會在密碼丟失時發送電子郵件，例如。

![image](assets/en/65.webp)

在店主設定電子郵件規則以啟動其商店的特定事件之前，我們必須先設定一些基本的電子郵件設定。BTCPay 伺服器需要這些設定，才能針對您商店的事件或密碼重設發送電子郵件。

BTCPay伺服器使用 「快速填寫 」選項讓您更容易填寫這些資訊：


- Gmail.com
- Yahoo.com
- 郵槍
- 辦公室365
- 發送網格

使用快速填寫選項，BTCPay伺服器會預先填寫SMTP伺服器和連接埠的欄位；現在，店主只需要填寫電子郵件Address、登入（通常等同於您的電子郵件Address）和密碼中的憑證。BTCPay 伺服器在電子郵件設定中提供的進階選項是停用 TLS 憑證安全檢查；預設為啟用。

![image](assets/en/66.webp)

透過電子郵件規則，店主可以設定特定事件，以觸發電子郵件至特定的電子郵件地址。


- 創建 Invoice
- Invoice 收到付款
- Invoice 處理
- Invoice 已過期
- Invoice 已和解
- Invoice 無效
- Invoice 已付款

如果客戶提供了電子郵件 Address，這些觸發器也可以將資訊傳送給客戶。店主可以預先填寫主旨行，以清楚說明這封 Email 發生的原因，以及是什麼觸發因素造成的。

![image](assets/en/67.webp)

### 表格

由於 BTCPay Server 不會收集任何資料，店主可能希望在結帳體驗中加入自訂表單；如此一來，店主就能從客戶身上收集額外的資訊。BTCPay Server 表單生成器由兩部分組成，即表單的可視化和更高級的代碼視圖。

在創建新表單時，BTCPay伺服器會開啟一個新視窗，要求您提供新表單所要求的基本資訊。首先，店主需要給他們的新表單一個明確的名稱，這個名稱在設置後不能更改。

![image](assets/en/68.webp)

在店主為表單命名後，您也可以將「允許公開使用表單」的開關切換到 ON，它就會變成 Green。這樣表單就可以在每個面向客戶的地方使用。舉例來說，如果店主不透過銷售點建立一個獨立的 Invoice，他可能仍想收集顧客的資訊；將此開關切換為 ON 就可以收集這些資訊。

![image](assets/en/69.webp)

每個表單至少有一個新表單欄位。店主可以選擇欄位的類型；


- 正文
- 數量
- 密碼
- 電子郵件
- 網址
- 電話號碼
- 日期
- 隱藏欄位
- 字段集
- 開放備註的文字區域。
- 選項選擇器

每種類型都有其需要填寫的參數。店主可以依自己的喜好設定。在第一個建立的欄位下方，店主可以繼續新增新欄位。

![image](assets/en/70.webp)

#### 進階自訂表單

BTCPay Server 也允許您在程式碼中建立表單。尤其是 JSON。店主可以點擊編輯器旁邊的 CODE 按鈕，進入表單的代碼，而不是看編輯器。在欄位定義中，只能設定下列欄位；欄位的值儲存在 Invoice 的 metadata 中：

| 欄位 | 描述

| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

| .fields.constant | 如果為 True，.value 必須在表單定義中設定，使用者將無法改變欄位的值。(例如：表單定義的版本) | .fields.constant



| .fields.options | 如果 .fields.type 為 select，則會顯示可選值清單。

| .fields.options.text | 此選項的顯示文字 | .fields.options.text | 此選項的顯示文字 | .fields.options.text | 此選項的顯示文字

| .fields.options.value | 如果選取此選項，欄位的值 | .fields.options.value | 欄位的值

| .fields.type=fieldset | 圍繞子代 .fields.fields 建立 HTML fieldset (請參閱下文) | .fields.type=fieldset | 圍繞子代 .fields.fields 建立 HTML fieldset (請參閱下文)

| .fields.name | 欄位的 JSON 屬性名稱，會顯示在 Invoice 的 metadata 裡。

| .fields.value | 欄位的預設值 | .fields.value | 欄位的預設值

| .fields.required | 如果為 true，欄位將為必填欄位。

| .fields.label | 欄位的標籤 | .fields.label | 欄位的標籤

| .fields.helpText | 提供欄位說明的附加文字。                                                                                                                                                                                                                                                                                                                                                                                                           |

| .fields.fields | 您可以以層級結構組織欄位，允許子欄位嵌套在 Invoice 的元資料中。這種結構可以幫助您更好地組織和管理收集到的資訊，使其更容易存取和詮釋。例如，如果您有一個收集客戶資訊的表單，您可以在稱為 customer 的父欄位下將欄位群組。在這個父欄位中，您可能會有名稱、電子郵件和 Address 等子欄位。|

欄位名稱代表在 Invoice 元資料中儲存使用者提供值的 JSON 屬性名稱。某些眾所周知的名稱可以詮釋並修改 Invoice 的設定。

| 欄位名稱 | 描述

| ---------------- | ---------------------- |

| invoice_amount | Invoice 的金額 | invoice_amount | Invoice 的金額

| invoice_currency | Invoice 的貨幣 | invoice_currency | Invoice 的貨幣 | invoice_currency | Invoice 的貨幣

您可以在表單的 URL 中加入查詢字串，例如「?your_field=value」，以自動預先填入 Invoice 的欄位。

以下是此功能的一些使用案例：


- 協助使用者輸入：將已知的客戶資訊預先填入欄位，讓他們更容易完成表單。例如，如果您已經知道客戶的電子郵件 Address，就可以預先填寫電子郵件欄位，以節省他們的時間。
- 個人化：根據客戶偏好或區隔自訂表單。例如，如果您有不同的客戶層級，您可以在表單中預先填入相關資料，例如他們的會員級別或特定優惠。
- 追蹤：使用隱藏欄位和預先填入的值追蹤客戶訪問的來源。例如，您可以為每個行銷管道 (如 Twitter、Facebook、Email) 建立預先填入 utm_media 值的連結。這可協助您分析行銷工作的成效。
- A/B 測試：預先填入不同值的欄位，以測試不同的表單版本，讓您能優化使用者體驗和轉換率。

### 技能摘要

在本節中，您學習了以下內容：


- 商店設定」中標籤的佈局和功能
- 多種選項可微調處理基礎 Exchange 費率、部分付款、輕微少付等情況。
- 自訂結帳外觀，包括依價格而定的主鏈與發票上的 Lightning 啟用。
- 管理不同角色的商店存取層級和權限。
- 設定自動化電子郵件及其觸發器
- 建立自訂表單，以便在結帳時收集額外的客戶資訊。

### 知識評估

#### KA 檢閱

商店設定」和「伺服器設定」有什麼區別？

#### KA 假設

說明您在結帳外觀 > Invoice 設定中可能選擇的一些選項，以及原因。

## BTCPay 伺服器 - 伺服器設定

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay 伺服器包含兩個不同的設定檢視。一個是專門的商店設置，另一個是伺服器設置。後者只有當您是伺服器管理員時才能使用，而非商店所有者。伺服器管理員可以新增使用者、建立自訂角色、設定電子郵件伺服器、設定政策、執行維護任務、檢查 BTCPay 伺服器的所有附加服務、上傳檔案至伺服器或檢查日誌。

### 使用者

如前所述，伺服器管理員可將使用者新增至使用者索引標籤，以邀請使用者使用其伺服器。

### 伺服器範圍自訂角色

BTCPay Server知道兩種自定義角色，在BTCPay Server設置中的特定商店自定義角色和全伺服器自定義角色。兩者都擁有相似的權限；但是，如果通過BTCpay伺服器設置 - 角色標籤設置，應用的角色將是全伺服器的，並應用於多個商店。注意在伺服器設定中的自訂角色有一個 "Server-wide "標籤。

![image](assets/en/71.webp)

### 伺服器範圍自訂角色

全伺服器的自訂角色權限設定；


- 修改您的商店。
- 管理與您的商店連結的 Exchange 帳戶。
  - 檢視與您的商店連結的 Exchange 帳戶。
- 管理您的拉動付款。
- 建立拉動付款。
  - 建立未核准的拉動付款。
- 修改發票。
  - 檢視發票。
  - 建立 Invoice。
  - 從與商店相關的閃電節點建立發票。
- 檢視您的商店。
  - 檢視發票。
  - 檢視您的付款要求。
  - 修改商店的 webhooks。
- 修改您的付款要求。
  - 檢視您的付款要求。
- 使用與您商店相關的閃光節點。
  - 檢視與您商店相關的閃電發票。
  - 從與商店相關的閃電節點建立發票。
- 將資金存入與您的商店連結的 Exchange 帳戶。
- 從 Exchange 帳戶提款到您的商店。
- 在您商店的 Exchange 帳戶上交易資金。

**注意！

在建立角色時，角色名稱是固定的，在編輯模式下不能變更。

### 電子郵件

伺服器範圍的電子郵件設定與特定於商店的電子郵件設定相似。然而，此設定不僅處理商店或管理員日誌的觸發器。此電子郵件設定也可讓 BTCPay 伺服器在登入時恢復密碼。它的工作原理與商店特定設定相似；管理員可以快速填寫他們的電子郵件參數，並輸入他們的電子郵件憑證，伺服器現在可以發送電子郵件。

![image](assets/en/72.webp)

### 政策

BTCPay伺服器政策管理員可以對一些主題進行設置，如現有用戶設置、新用戶設置、通知設置和維護設置。這些都是為了將新用戶註冊為管理員或普通用戶，甚至通過添加到您的服務器標頭從搜索引擎中隱藏BTCPay服務器。

![image](assets/en/73.webp)

#### 現有使用者設定

這裡提供的選項與自訂角色不同。這些額外權限可能會使商店或商店擁有者容易受到攻擊。可加入現有使用者的政策：


- 允許非管理員在其商店中使用內部 Lightning 節點。
  - 這將允許店主使用伺服器管理員的Lightning節點，因此也允許他的資金！請注意，這並不是給予 Lightning 存取權的解決方案。
- 允許非管理員為其商店建立 Hot 錢包。
  - 這將允許任何在您的BTCPay伺服器實例上擁有帳戶的人創建Hot-錢包，並將其恢復的seed存儲在管理員的伺服器上。這可能會使管理員對持有第三方的資金負責！
- 允許非管理員為其商店匯入 Hot 錢包。
  - 與之前建立 Hot 錢包的主題類似，此政策允許匯入 Hot Wallet，但會有在建立 Hot 錢包部分提到的相同危險。

![image](assets/en/74.webp)

#### 新使用者設定

我們可以設定一些重要的設定來管理進入伺服器的新使用者。我們可以為新的註冊設定確認電子郵件、禁止透過登入畫面建立新使用者，以及限制非管理員透過 API 建立使用者。


- 註冊時需要確認電子郵件。
  - 伺服器管理員必須已設定電子郵件伺服器！
- 停用伺服器上的新使用者註冊
- 停用非管理員存取使用者建立 API 端點。

在預設情況下，BTCPay伺服器已打開禁止新用戶註冊，並關閉了非管理員對用戶創建API端點的訪問。這是出於安全方面的考慮，任何隨機找到您伺服器的BTCPay登入帳號的人都無法開始建立帳號。

![image](assets/en/75.webp)

#### 通知設定

![image](assets/en/76.webp)

#### 維護設定

BTCPay Server是GitHub上的開源專案。每當 BTCPay Server 發佈新版本的軟體時，管理員可以收到新版本可用的通知。管理員可能還希望阻止搜索引擎（google，yahoo，duckduckgo）索引BTCPay Server域。由於BTCPay伺服器是FOSS，世界各地的開發者可能想創造新的功能；BTCPay伺服器在開啟時有一個實驗性的功能，管理員可以使用還不是為了生產的功能，純粹是為了測試目的。


- 查看 GitHub 上的版本，並在新的 BTCPay Server 版本可用時通知您。
- 阻止搜尋引擎索引本網站
- 啟用實驗功能。

![image](assets/en/77.webp)

#### 外掛程式

BTCPay Server可以添加插件並擴展其功能集。預設情況下，插件是從 BTCPay Server 插件生成器儲存庫載入的。但是，管理員可以選擇查看預發佈狀態的外掛，如果外掛開發人員允許，伺服器管理員現在可以安裝beta版本的外掛。

![image](assets/en/78.webp)

##### 自訂設定

標準的 BTCPay 伺服器部署將可透過安裝時為其設定的網域接達。然而，伺服器管理員可以重新對應根網域，並顯示從特定商店中創建的其中一個應用程式。伺服器管理員也可以將特定網域對應到特定應用程式。


- 將應用程式顯示在網站的根目錄
  - 顯示要在根網域上顯示的可能應用程式清單。

![image](assets/en/79.webp)


- 將特定網域對應到特定應用程式。
  - 當您點選為特定應用程式設定特定網域時，管理員可根據需要設定指向特定應用程式的多個網域。

![image](assets/en/80.webp)

#### 區塊探索者

BTCPay 伺服器標準配備 Mempool.space 作為交易的 Block explorer。當BTCPay伺服器產生一個新的Invoice，並有一個交易綁定到它，店主可以點擊打開交易；BTCPay伺服器將標準地指向Mempool.空間作為Block explorer；伺服器管理員可以根據自己的喜好進行更改。

![image](assets/en/81.webp)

### 服務

BTCPay服務器設置：服務 "標籤是您的BTCPay伺服器使用的組件的總覽。您的BTCPay伺服器開放的服務可能因部署方法而異。

BTCPay伺服器管理員可以點擊每項服務後面的 "See information"（查看資訊）打開該服務，並進行特定的設置。

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay 開放 LND 的 GRPC 服務供外部使用；您可在此特定設定選單中找到連線資訊；相容的錢包列在此處。BTCPay 伺服器也會提供一個 QR 代碼供連線掃描並在手機 Wallet 中應用。

伺服器管理員可以開啟更多詳細資訊查看；


- 主機詳細資訊
- 使用 SSL
- 馬卡龍
- 管理員Macaroon
- InvoiceMacaroon
- 只讀馬卡龍
- GRPC SSL 密碼套件 (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay 開放 LND 的 REST 服務供外部使用；您可在此找到連線資訊；相容的錢包列於此。相容的錢包包括 Joule、Alby 和 ZeusLN。BTCPay 伺服器會提供一個 QR 代碼供連線使用，掃瞄後即可在相容的 Wallet 中使用。


- REST Uri
- 馬卡龍
- 管理員Macaroon
- InvoiceMacaroon
- 只讀馬卡龍

#### LND seed 備份

LND seed 備份對於您的 LND Wallet 在伺服器損壞時恢復資金非常有用。由於 Lightning 節點是 Hot-Wallet，您可以在此頁面找到 seed 的機密資訊。

LND 記錄了恢復過程。文件請參閱 https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md。

#### 騎乘閃電

Ride the Lightning 是以開源軟體形式建立的 Lightning 節點管理工具。BTCPay Server使用RTL作為其堆疊中的Lightning節點管理組件。BTCPay服務器管理員可以通過服務器設置 - 服務標籤或通過點擊Lightning Wallet訪問RTL。

#### Full node P2P

伺服器管理員可能想要將他們的 Bitcoin 節點連接到行動 Wallet。本頁面提供透過 P2P 通訊協定遠端連接 Full node 的資訊。在撰寫本書時，BTCPay Server 將 Blockstream Green 和 Wasabi Wallet 列為相容的錢包。BTCPay伺服器會提供一個QR碼來進行連接，掃描並在相容的Wallet中進行應用。

#### Full node RPC

本頁面提供透過 RPC 通訊協定遠端連接 Full node 的資訊。

#### SSH

SSH 用於維護目的。BTCPay Server會顯示到達您伺服器的初始連接命令，以及授權連接至您伺服器的SSH公開密鑰。伺服器管理員可能希望通過BTCPay Server的使用者介面關閉SSH變更。

#### 動態 DNS

動態 DNS 允許您有一個穩定的 DNS 名稱指向您的伺服器，即使您的 IP Address 經常改變。如果您在家中架設BTCPay伺服器，並希望有一個清晰的網域來存取您的伺服器，建議您使用動態DNS。

請注意，您需要正確配置您的NAT和BTCPay伺服器安裝，以獲得HTTPS證書。

### 主題

BTCPay Server 標準配備兩種主題：淺色和深色模式。您可以點擊左下方的帳戶，在深色主題或淺色主題之間切換。BTCPay 伺服器管理員可透過提供自訂 CSS 主題來新增他們的主題。

管理員可以透過新增自訂 CSS 或將自訂主題設定為完全自訂來擴充 Light/Dark 主題。

![image](assets/en/83.webp)

#### 伺服器品牌

伺服器管理員可以通過設置一個全伺服器的公司品牌來改變BTCPay伺服器的品牌。由於 BTCPay Server 是 FOSS，伺服器管理員可以為軟件貼上白色標籤，並改變外觀以適應其業務。

![image](assets/en/84.webp)

### 維護

作為一個伺服器管理員，您的用戶希望您能好好地保護伺服器。在BTCPay伺服器的維護標籤中，管理員可以進行一些必要的維護。設置BTCPay服務器實例的域名，重新啟動或清理服務器。最重要的可能是執行更新。

BTCPay Server是一個開源專案，更新頻率高。每個新版本都會在您的BTCPay伺服器通知或BTCPay伺服器官方頻道中公佈。

![image](assets/en/85.webp)

#### 網域名稱

在 BTCPay 伺服器設定完成後，管理員可能會想要改變他原本的網域。在維護標籤中，管理員可以更改網域。在點擊確認並在網域上設置適當的DNS記錄後，BTCPay伺服器會更新並重新啟動以返回到新的網域。

![image](assets/en/86.webp)

#### 重新啟動

重新啟動 BTCPay 伺服器和相關服務。

![image](assets/en/87.webp)

#### 清潔

BTCPay 伺服器使用 Docker 元件執行；隨著更新，可能會有殘留的 Docker 映像檔、暫存檔案等。伺服器管理員可執行 Clean script 來清理這些殘留，並在環境中回收空間。

![image](assets/en/88.webp)

#### 更新

可能是維護標籤中最重要的選項。BTCPay Server由社群建立，因此其更新週期比一般軟體產品更為頻繁。當BTCPay Server有新版本時，管理員將會在他們的通知中心收到通知。點擊更新按鈕，BTCPay伺服器將檢查GitHub的最新版本，更新伺服器並重新啟動。在更新之前，建議伺服器管理員閱讀BTCPay伺服器官方渠道發布的版本說明。

![image](assets/en/89.webp)

### 日誌

面對問題絕非樂事。本文件說明最常見的工作流程和步驟，讓您有效率地找出問題，並自行或在社群協助下解決問題。

找出問題是至關重要的。

#### 複製問題

首先，嘗試確定問題發生的時間。嘗試複製問題。嘗試更新並重新啟動您的伺服器，以驗證是否可以重現您的問題。如果能更好地描述您的問題，請截圖。

##### 更新伺服器

請檢查您的BTCPay伺服器版本是否遠舊於BTCPay伺服器的[最新版本](https://github.com/btcpayserver/btcpayserver/releases)。更新您的伺服器可能會解決問題。

##### 重新啟動伺服器

重新啟動您的伺服器是一個簡單的方法來解決許多最常見的BTCPay伺服器問題。您可能需要SSH進入您的伺服器來重新啟動它。

##### 重新啟動服務

您可能只需要重新啟動 BTCPay 伺服器部署中的特定服務來處理某些問題。例如重新啟動 lets encrypt 容器以更新 SSL 證書。

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

使用 docker ps 找到您想要重新啟動的其他服務名稱。

#### 翻閱記錄

日誌可以提供重要的資訊。在以下段落中，我們將介紹如何獲取 BTCPay 各部分的日誌資訊。

##### BTCPay 日誌

自v1.0.3.8版本起，您可以輕鬆地從前端訪問BTCPay服務器日誌。如果您是伺服器管理員，進入伺服器設定 > 日誌，打開日誌檔案。如果您不知道日誌中的特定錯誤是什麼意思，請在排除故障時提及。

如果您想要更詳細的日誌，並且正在使用 Docker 部署，您可以使用命令列檢視特定 Docker 容器的日誌。請參閱這些 [ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80)進入在 VPS 上執行的 BTCPay 實例的說明。

在下一頁，是 BTCPay 伺服器使用的容器名稱的一般清單。

執行下面的指令，按容器名稱列印日誌。替換容器名稱可檢視其他容器日誌。

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| 容器名稱 | | 日誌

| ------------ | --------------------------------- |

| BTCPayServer | generated_btcpayserver_1 | BTCPayServer | 生成的 BTCPayServer_1

| NBXplorer | generated_nbxplorer_1 | NBXplorer

| bitcoind | btcpayserver_bitcoind | bitcoind

| Postgres | generated_postgres_1 | Postgres_1

| 代理權 | letsencrypt-nginx-proxy-companion | 代理權 | letsencrypt-nginx-proxy-companion |代理權

| Nginx | nginx-gen | nginx-gen

| Nginx | nginx |

| c-lightning | btcpayserver_clightning_bitcoin | btcpayserver_clightning_bitcoin | btcpayserver_clightning_bitcoin

| LND | btcpayserver_lnd_bitcoin | LND

| RTL | generated_lnd_bitcoin_rtl_1 | 生成的比特币。

| Thunderhub | generated_bitcoin_thub_1 | 生成的比特幣

| LibrePatron | librepatron | | LibrePatron

| Tor | tor-gen |

| Tor | Tor |

###### Lightning Network LND - Docker

使用 Docker 時，有幾種方法可以存取您的 LND 日誌。首先以 root 登入：

```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

另外，您也可以使用容器 ID 來快速列印記錄（只需要第一個唯一的 ID 字元，例如最左邊的兩個字元）：

```bash
docker logs 'add your container ID'
```

如果您因為任何原因需要更多原木

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```

您會看到以下內容

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

若要存取這些日誌的未壓縮日誌，請使用 `cat LND.log`，如果您想要另一個，請使用 `cat LND.log.15`。

若要存取`.gzip`格式的壓縮日誌，請使用 `gzip -d LND.log.16.gz`（本例中我們存取`LND.log.16.gz`）。這應該會給您一個新的檔案，您可以在其中執行 `cat LND.log.16`。如果上面的方法行不通，您可能需要先使用 `sudo apt-get install gzip` 安裝 gzip。

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```

或者，使用此

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

您也可以使用 c-lightning CLI 指令取得日誌資訊。

```bash
bitcoin-lightning-cli.sh getlog
```

#### Bitcoin 節點日誌

除了 bitcoind 容器的 [查看日誌](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs)，您也可以使用任何 [bitcoin-cli 指令](https://developer.Bitcoin.org/reference/RPC/index.html)

[(開啟新視窗)](https://developer.Bitcoin.org/reference/RPC/index.html)從您的Bitcoin節點獲取資訊。BTCPay包括一個腳本，讓您可以輕鬆地與您的Bitcoin節點通信。

在 btcpayserver-docker 資料夾內，使用您的節點取得 Blockchain 資訊：

```bash
bitcoin-cli.sh getblockchaininfo
```

### 檔案

BTCPay伺服器擁有本地檔案系統，可直接上載商店（產品）資產、商標和品牌至伺服器。伺服器的檔案系統僅供伺服器管理員存取；商店所有者可在商店層級上載他們的標誌/品牌。

當伺服器管理員進入「檔案儲存」索引標籤時，可以直接上傳到您的伺服器，或將檔案儲存提供者變更為本機檔案系統或 Azure Blob Storage。

![image](assets/en/90.webp)

![image](assets/en/91.webp)

### 技能摘要

在本節中，您學習了以下內容：


- 商店與伺服器設定的差異，尤其是與使用者、角色和電子郵件相關的設定
- 為 Lightning 或 Bitcoin Hot Wallet 的使用和建立、新使用者註冊和電子郵件通知設定伺服器範圍的政策。
- 如何新增自訂主題（而非提供簡單的明暗選項）以及建立自訂標誌
- 透過提供的 GUI 執行簡單的伺服器維護工作
- 排除問題，包括取得任何 Docker 容器或您的節點的詳細資料
- 管理檔案儲存

### 知識評估

#### KA 概念回顧

透過伺服器設定指派的角色與透過商店設定指派的角色有何不同？

#### KA 實務回顧

描述在「政策」標籤中啟用的一些可能用例。

#### KA 實務回顧

描述管理員在 Maintenance（維護）索引標籤中可能會執行的一些例行動作。

## BTCPay 伺服器 - 付款

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Invoice 是賣方向買方發出的收款文件。

在 BTCPay 伺服器中，Invoice 代表必須在定義的時間間隔內以固定的 Exchange 費率支付的文件。發票有到期日，因為它們鎖定了指定時間內的Exchange費率，以保護接收方免受價格波動的影響。

BTCPay Server的核心是能夠作為Bitcoin Invoice管理系統。Invoice是追蹤和管理已收付款的重要工具。

除非您使用內建的 [Wallet](https://docs.btcpayserver.org/Wallet/) 來手動接收付款，否則商店內的所有付款都會顯示在 Invoices 頁面上。此頁面會依日期累積排序付款，是 Invoice 管理和付款疑難排解的核心部分。

![image](assets/en/92.webp)

### 一般

#### Invoice 狀態

下表列出並說明了 BTCPay 中標準的 Invoice 狀態，並建議了常見的操作。行動只是建議。用戶可根據自己的使用情況和業務定義最佳行動方案。

| Invoice 狀態 | 說明 | 動作

| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |

| 新增 | 未支付，Invoice 計時器仍未過期 | 無 | | 新增 | 未支付，Invoice 計時器仍未過期

| 已付款，但未全額付款，Invoice 計時器仍未過期 | 無 | | 新的 (paidPartial)

| 已過期 | 未付費，Invoice 計時器已過期 | 無 |

| Expired (paidPartial) \*\* | 已付款，但不是全額，且已過期 | 聯絡買家安排退款或要求他們支付應付的款項。可選擇將 Invoice 標記為已結算或無效 | | | 已結算或無效

| 過期 (paidLate) | 在 Invoice 計時器過期後全額付款 | 如果可以接受逾期確認，請聯絡買家安排退款或處理訂單。                                    |

| 已結算 (paidOver) | 已支付超過 Invoice 的金額，已結算，並收到足夠數量的確認書 | 聯絡買家安排退還額外金額，或選擇等待買家聯絡您 | 聯絡買家安排退還額外金額，或選擇等待買家聯絡您 | 聯絡買家安排退還額外金額 | 聯絡買家安排退還額外金額

處理中 | 已全額付款，但未收到商店設定中指定的足夠確認金額 | 聯絡買家安排額外金額的退款，或選擇等待買家聯絡您 | 聯絡買家安排額外金額的退款，或選擇等待買家聯絡您 | 聯絡買家安排額外金額的退款，或選擇等待買家聯絡您 | 聯絡買家安排額外金額的退款。

| 處理中 (paidOver) | 付款超過 Invoice 金額，未收到足夠數量的確認 | 等待結算，然後聯絡買家安排退還額外金額，或選擇等待買家聯絡您 | | 處理中 (paidOver) | 付款超過 Invoice 金額，未收到足夠數量的確認

| 已結帳 | 已付款，全額，已收到足夠數量的確認書 | 履行訂單 | 已付款，全額，已收到足夠數量的確認書 | 履行訂單 | 已付款，全額，已收到足夠數量的確認書

| 已結算（已標記） | 狀態已從處理中或無效狀態手動變更為已結算 | 商店管理員已將付款標記為已結算 | 帳戶管理員已將付款標記為已結算

| Invalid\* | 已付款，但未能在商店設定中指定的時間內收到足夠數量的確認 | 在 Blockchain explorer 上檢查交易，如果收到足夠的確認，標記為已結算 | | 已付款，但未能在商店設定中指定的時間內收到足夠數量的確認 | 在 Blockchain explorer 上檢查交易，如果收到足夠的確認，標記為已結算

| 無效（已標記） | 狀態從結算或過期狀態手動變更為無效 | 商店管理員已將付款標記為無效 | 無效（已標記） | 無效（已過期） | 商店管理員已將付款標記為無效

| 無效 (paidOver) | 支付的金額超過 Invoice 的金額，但未能在商店設定中指定的時間內收到足夠數量的確認 | 在 Blockchain 探索器上檢查交易，如果收到足夠的確認，標記為已結算 | | 無效 (paidOver) | 支付的金額超過 Invoice 的金額，但未能在商店設定中指定的時間內收到足夠數量的確認

#### Invoice 詳細資訊

Invoice 詳細資訊頁面包含與 Invoice 相關的所有資訊。

Invoice 資訊會根據 Invoice 狀態、Exchange 比率等自動建立。如果 Invoice 是以產品資訊建立，例如在銷售點應用程式中，則會自動建立產品資訊。

#### Invoice 過濾

可透過搜尋按鈕旁邊的快速篩選器或進階篩選器來篩選發票，進階篩選器可透過按一下上方的 (Help) 連結來切換。使用者可依商店、訂單 ID、項目 ID、狀態或日期篩選發票。

#### Invoice 出口

BTCPay 伺服器發票可以 CSV 或 JSON 格式匯出。關於Invoice匯出和會計的更多資訊。

#### 退還 Invoice

如果您因為任何原因想要退款，您可以輕鬆地從 Invoice 檢視建立退款。

#### 存檔發票

由於BTCPay伺服器沒有Address重複使用的功能，在您商店的Invoice頁面上看到許多過期的發票是很常見的。要從您的視圖中隱藏它們，請在列表中選擇它們並將它們標記為已存檔。已標記為存檔的發票不會被刪除。您的 BTCPay 伺服器仍會偵測到已存檔的 Invoice 付款（paidLate 狀態）。您可以隨時從搜尋篩選器下拉選出已歸檔的發票，以檢視商店已歸檔的發票。

#### 預設貨幣

商店預設貨幣，這是在商店建立精靈中設定的

#### 允許任何人建立 Invoice

如果您要允許外界在您的商店中建立發票，您應該啟用此選項。此選項只有在您使用付款按鈕或透過 API 或第三方 HTML 網站開立發票時才有用。PoS 應用程式是預先授權的，不需要啟用此選項，隨機訪客就可以打開您的 POS 商店並建立 Invoice。

#### 在 Invoice 中加入額外費用（網路費用


- 僅當客戶為 Invoice 付款一次以上時
- 每次付款時
- 絕不增加網路費用

#### 如果在...分鐘後仍未支付全額，Invoice 即失效。

Invoice 計時器預設為 15 分鐘。該計時器是一種防止波動的保護機制，因為它會根據加密貨幣與法定貨幣的匯率鎖定加密貨幣金額。如果客戶在定義的時間內沒有支付 Invoice，Invoice 將被視為過期。Invoice 在 Blockchain 上顯示交易（o-確認）時即視為「已支付」，但在達到商家定義的確認次數（通常為 1-6）時則視為「完成」。計時器是可自訂的。

#### 即使支付的金額比預期少 .%，也視為已支付 Invoice。

在客戶使用 Exchange Wallet 直接支付 Invoice 的情況下，Exchange 會收取少量費用。這表示此 Invoice 並未被視為完全完成。Invoice 會得到 "paid partially" 的狀態。如果商家想要接受未支付的發票，您可以在此設定百分比率

### 請求

付款請求是一項允許BTCPay店主建立長期發票的功能。資金會使用付款時的 Exchange 費率支付給付款請求。這允許用戶在方便的時候進行支付，而無需在支付時與店主協商或驗證 Exchange 費率。

使用者可以分次支付請求。付款請求會一直有效，直到全額支付或店主要求的到期時間。地址永遠不會被重複使用。每次使用者點選付款，都會產生新的 Address，為付款請求建立 Invoice。

店主可以列印付款要求（或匯出Invoice資料）以作記錄和會計之用。BTCPay會在您商店的Invoice清單中自動將發票標示為付款請求。

#### 自訂您的付款要求


- Invoice 金額 - 設定要求的付款金額
- 面額 - 以法定貨幣或加密貨幣顯示請求金額
- 付款數量 - 僅允許單次付款或部分付款
- 到期時間 - 允許付款至某個日期或無需到期時間
- 說明 - 文字編輯器、資料表、嵌入照片與影片
- 外觀 - 使用 CSS 主題的顏色和樣式

![image](assets/en/93.webp)

#### 建立付款要求

在左側功能表中，前往「付款申請」，然後按一下「建立付款申請」。

![image](assets/en/94.webp)

提供請求名稱、金額、顯示面額、相關商店、到期時間和說明（選擇性）

如果要允許部分付款，請選取選項允許收款人以其面額建立發票。

按一下「儲存與檢視」以檢視您的付款要求。

BTCPay 為付款請求建立一個 URL。分享此 URL 以查看您的付款請求。需要多個相同的請求嗎？您可以使用主菜單中的Clone選項複製付款請求。

![image](assets/en/95.webp)

**WARNING**

付款請求依商店而定，這表示每個付款請求在建立時都會與商店相關聯。請務必將 Wallet 連接到付款請求所屬的商店。

#### 付費申請

收款人和請求人可在傳送付款後檢視付款請求的狀態。如果已全額收到付款，狀態會顯示為已結清。如果只支付了部分款項，「應付金額」將顯示應付餘額。

![image](assets/en/96.webp)

#### 自訂付款要求

描述內容可以使用付款請求的文字編輯器進行編輯。如果您想使用額外的顏色主題或自訂 CSS 造型，這兩個選項都可用。

非技術使用者可以使用 [bootstrap theme](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes)。進一步的客製化可透過提供額外的 CSS 程式碼來完成，如下所示。

```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}
#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}
#mainNav .btn-link {
color: white;
}
```

### 拉動付款

傳統上，接收者會分享他們的 Bitcoin Address 來進行 Bitcoin 付款，寄件者稍後會寄錢到這個 Address。這樣的系統稱為 Push 付款，因為發件人在收件人可能無法使用時啟動付款，將付款推送給收件人。

然而，反轉角色又如何呢？

如果不是寄件者推送付款，而是寄件者允許收件者在收件者認為合適的時間拉取付款呢？這就是 Pull 付款的概念。這允許幾種新的應用，例如


- 訂閱服務（訂閱者允許該服務每隔 X 時間提取資金）
- 退款（商戶允許客戶在他們認為合適的時候將退款款項提取到他的 Wallet 中）
- 自由職業者以時間為基礎的計費方式（僱用者允許自由職業者在報告時間時將資金轉入其 Wallet 中）
- 贊助人（贊助人允許接受者每月抽取金錢，繼續支持他們的工作）
- 自動銷售 (Exchange的客戶可讓Exchange每月自動從Wallet抽取資金進行銷售)
- 餘額提款系統 (高流量服務可讓使用者要求從餘額中提款，然後服務可輕鬆地以固定的間隔將所有付款批量支付給許多使用者)

### 付款方式

支付功能與[Pull Payments](https://docs.btcpayserver.org/PullPayments/)相結合。此功能可讓您在 BTCPay 內建立付款。此功能允許您處理拉付（退款、薪水支付或提款）。

#### 範例 1：退款

讓我們從退款的範例開始。客戶在您的商店購買了一件商品，但很遺憾地要退貨。他們想要退款。在BTCPay中，您可以創建一個[退款](https://docs.btcpayserver.org/Refund/)，並為客戶提供鏈接來領取他們的資金。每當客戶提供了他們的Address並領取了資金，就會顯示在Payouts中。

它的第一個狀態是等待批准。店員可檢查是否有多個正在等待，在做出選擇後，您使用「行動」按鈕。

動作按鈕上的選項


- 批准選定的付款
- 批准和發送選定的付款
- 取消選取的付款

下一步是批准並發送所選的付款，因為我們要退款給客戶。檢查客戶的 Address，顯示金額以及我們是否要從退款中扣除費用。完成檢查後，就只剩下簽署交易了。

客戶現在會在索賠頁面上獲得更新。他可以跟蹤交易，因為他會收到 Block explorer 和他的交易連結。交易一經確認，且狀態變更為已完成。

#### 範例 2：薪資

現在讓我們來看看 Salary payout，因為這是由商店內部驅動的，而不是根據客戶的要求。底層是相同的；它使用 Pull 付款。但我們不會建立退款，而是會建立 [Pull Payment](https://docs.btcpayserver.org/PullPayments/)。

在您的BTCPay服務器中進入Pull Payments標籤。在右上方，點擊 Create Pull Payment 按鈕。

現在我們正在建立 Payout，給它一個名稱和所需貨幣的所需金額，填寫 Description，讓員工知道它是關於什麼的。接下來的部分與退款類似。員工填寫目的地 Address，以及他想從這筆付款中索取的金額。他可能會決定分兩次索償，寄到不同的地址，或甚至部分索償到閃電。

如果有多筆等待中的付款，您可以批量簽署並發送。簽署後，付款會移至「進行中」標籤，並顯示「交易」。當網路接受後，付款會移至「已完成」標籤。已完成」標籤純粹用於歷史目的。它保存已處理的付款和屬於它的交易。

### 拉動付款

#### 概念

寄件者設定 Pull 付款時，可以設定許多屬性：


- 拉取請求名稱
- 限額
- 單位 (例如 BTC、SAT、USD)
- 付款方式
  - BTC On-Chain
  - BTC off-chain
- 說明
- 自訂 CSS
- 結束日期（Lightning Network BOLT11 為選購項目）

之後，寄件者可以使用連結與收件者分享拉付，讓收件者建立付款。收款人將選擇他們的付款方式：


- 使用哪種付款方式
- 匯款地點

一旦建立了付款，該付款將計入當期的拉動付款限額。然後，寄件者將透過設定寄送付款的費率來核准付款，並進行付款。

對於寄件者，我們提供了一個簡單易用的方式，從 [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/)批量支付數筆款項。

#### 綠地 API

BTCPay伺服器提供了一個完整的API給發送者和接收者，該API在您的實例的`/docs`頁面中有記錄。(或在文件網站 https://docs.btcpayserver.org)

由於我們的 API 開放了完整的拉動式付款功能，寄件者可以依據自己的需求自動化付款。

### 技能摘要

在本節中，您學習了以下內容：


- 深入瞭解 BTCPay 伺服器的 Invoice 狀態以及可對其執行的動作
- 自訂和管理延長使用壽命的 Invoice 機制，稱為 Requests。
- BTCPay Server獨特的Pull Payment功能所開啟的額外彈性付款可能性，特別是如何處理退款和薪資付款。

### 知識評估

#### KA 概念回顧

發票與付款請求之間有哪些差異，使用後者的理由為何？

#### KA 概念回顧

拉動式付款如何擴展 On-Chain 的典型功能？請說明它們可以實現的一些用例。

## BTCPay 伺服器預設外掛程式

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### 預設外掛程式與應用程式

BTCPay 伺服器附有一套標準的外掛程式 (Apps)，可讓 BTCPay 伺服器成為電子商務付款閘道。隨著銷售點、集資平台和簡易支付按鈕的加入，BTCPay 伺服器將成為一個容易部署的解決方案。

### 銷售點

BTCPay Server的標準外掛之一是Point of Sale (PoS)。有了PoS外掛程式，店主可以直接從BTCPay伺服器建立網路商店，店主不需要第三方電子商務解決方案來經營網路商店。網頁式 PoS 應用程式可讓擁有實體商店的使用者隨時接受 Bitcoin，無需收費或第三方，直接傳送至 Wallet。PoS 可輕鬆顯示在平板電腦或其他支援網頁瀏覽的裝置上。使用者可輕鬆建立主畫面捷徑，快速存取網頁應用程式。

#### 如何建立新的銷售點

BTCPay Server 可讓店主快速建立多種佈局的銷售點。BTCPay Server 認識到並非每家商店都是電子商務，也並非每家商店都是酒吧或餐廳，因此它為您的 PoS 提供多種標準設定。

當店主點擊左邊菜單欄中的 "Point of Sale "時，BTCPay伺服器會要求一個名稱；這個名稱會在左邊菜單欄中顯示。點擊 「創建 」以創建 PoS。

![image](assets/en/97.webp)

#### 更新新建立的銷售點

建立新的 PoS 後，以下畫面將是更新您的銷售點，並為您的商店新增商品。

##### 應用程式名稱

在此給您的銷售點命名將在BTCPay服務器的主菜單中顯示。

##### 顯示標題

當公眾訪問您的商店時，會看到公眾標題或名稱。BTCPay伺服器會將您的商店命名為 "Tea shop"。

![image](assets/en/98.webp)

#### 選擇銷售點風格

BTCPay 伺服器能夠以多種方式顯示其銷售點。


- 產品清單
  - 客戶一次只能購買 1 件產品的商店檢視。
- 有購物車的產品清單。
  - 商店檢視，顧客可以一次購買多項商品，並在螢幕右方取得購物車概觀。
- 僅鍵盤
  - 沒有產品清單，只有直接開票的鍵盤。
- 列印顯示 (可列印產品清單與 QR)
  - 如果您不能經常以數位方式顯示您的產品清單，您需要一個 「離線 」的產品解決方案；BTCPay伺服器有一個打印顯示功能，可以作為一個離線商店。

![image](assets/en/99.webp)

#### 銷售點風格 - 產品清單

![image](assets/en/100.webp)

#### 銷售點風格 - 產品清單 + 購物車

![image](assets/en/101.webp)

#### 銷售點風格 - 僅鍵盤

![image](assets/en/102.webp)

#### 銷售點風格 - 列印顯示

![image](assets/en/103.webp)

#### 貨幣

店主可以為其銷售點設定與整體預設貨幣不同的貨幣。商店的預設貨幣會自動填入此欄位。

#### 說明

向全世界介紹您的商店；您賣什麼，賣多少錢？所有關於您商店的說明都在這裡。

![image](assets/en/104.webp)

#### 產品

當一個銷售點被創建時，一個標準的BTCPay服務器會添加一些項目到商店中以供參考。點擊任何一個標準項目上的編輯按鈕，可以更好地瞭解項目的每個可能選項。

在商店中建立新產品包括下列欄位；


- 標題
- 價格（固定、最低或自訂）
- 圖片網址
- 說明
- 庫存
- ID
- 購買按鈕文字。
- 啟用/停用

店主填入所有新產品欄位後，按一下儲存，您會發現銷售點中的產品部分現在已被填入。請務必在螢幕右上方儲存，以避免店主可能失去新增產品的進度。

店主也可以使用「原始編輯器」來設定產品。原始編輯器需要對 JSON 結構有基本的瞭解。

![image](assets/en/105.webp)

#### 結帳

BTCPay 伺服器允許小規模的 PoS 特定結帳自訂。店主可以設定「Buy for x」文字，或透過加入表單要求特定的客戶資料。

#### 提示

只有某些商店需要銷售提示選項。店主可根據自己的商店情況開啟或關閉此選項。如果商店使用小費開啟，店主可以在字段中設定他們喜歡的小費文字。BTCPay伺服器的小費按百分比計算。店主可以用逗號分隔添加多個百分比。

#### 折扣優惠

身為店主，您可能希望在結帳時給予顧客自訂折扣；折扣的切換選項會在您的商店結帳時出現。但是，我們建議您不要使用自助結帳系統。

#### 自訂付款

當「自訂付款」選項被開啟時，客戶可以輸入他們設定的價格，該價格等於或高於商店產生的原始 Invoice。

#### 額外選項

設定完銷售點的一切後，還剩下一些額外的選項。店主可以輕鬆地透過 Iframe 嵌入他們的 PoS，或嵌入付款按鈕連結至特定的商店項目。為了使剛建立的 PoS 商店風格化，店主可以在附加選項的底部加入自訂 CSS。

#### 刪除此應用程式

如果店主想要從他的BTCPay伺服器中完全刪除銷售點，在更新PoS的底部，店主可以點擊刪除此應用程式按鈕，以完全銷毀他們的PoS應用程式。當點擊 「刪除此應用程式 」時，BTCPay伺服器會要求輸入`DELETE`並點擊刪除按鈕確認。刪除後，店主會回到BTCPay伺服器儀表板。

### BTCPay 伺服器 - 眾人集資

在銷售點外掛程式旁邊，BTCPay 伺服器有創建眾籌基金的選項。就像任何其他的 Crowdfund 平台一樣，店主可以設定目標、創建貢獻獎勵，並根據自己的需求自訂。

#### 如何成立新的集資基金

通過BTCPay服務器左側的主菜單，點擊插件部分下方的Crowdfund插件。BTCPay Server現在會要求為Crowdfund命名；這個名稱也會顯示在左邊的菜單欄中。

![image](assets/en/106.webp)

#### 更新新建立的銷售點

應用程式命名後，下一個畫面就是更新應用程式的內容。

#### 應用程式名稱

在BTCPay服務器的主菜單中，您的Crowdfund的名字將顯示出來。

#### 顯示標題

標題賦予 Crowdfund 給大眾。

#### 標語

給群眾募款一句話，讓大家認清募款的目的。

![image](assets/en/107.webp)

#### 特色圖片 URL

每筆集資都有其主圖像，也就是您能直接辨認的橫幅。如果您有管理權限，此圖片可以存儲在您的伺服器上，管理員可以在BTCPay伺服器的伺服器設置 - 檔案下上傳。如果您是店主，圖片必須通過第三方主機（例如 imgur）上傳至網站。

#### 公開集資

此切換鈕可讓您的集資基金公開，因此對外界可見。為了測試目的或檢視您的主題是否正確套用，您可能需要在建立集資的期間將此選項設定為關閉。

#### 說明

向全世界介紹您的集資，您集資的目的是什麼？在此說明您的集資。

![image](assets/en/108.webp)

#### 集資目標

設定籌款者應為專案賺取的目標，以及目標應以何種貨幣計價。確保如果您的目標設定在兩個日期之間，請將這些目標和結束日期包含在 crowdfund 中的目標下方。

![image](assets/en/109.webp)

#### 福利

福利對您的集資活動有很大的幫助。這是因為福利讓人們有辦法參與您的活動。它們既能發掘自私的動機，也能發掘仁慈的動機。您可以猜到哪一個更重要。

建立新的perk包括以下欄位 ；


- 標題
- 價格（固定、最低或自訂）
- 圖片網址
- 說明
- 庫存
- ID
- 購買按鈕文字。
- 啟用/停用

店主填入新建立的福利的所有欄位後，按一下儲存，您會發現眾人集資中的福利一欄現在已被填入。

![image](assets/en/110.webp)

### BTCPay 伺服器 - 銷售點

#### 貢獻

店主可以選擇如何顯示 Perks、如何排序，甚至與其他 Perks 進行排名。不過，一旦達到 Crowdfunds 的目標，店主可能想要停止捐款流向這個募款活動。因此，他可以切換「達到目標後不允許額外捐款」。這將會停止 Crowdfund 接受捐款。

##### 集資行為

Crowdfund 的標準只將使用 Crowdfund 創建的發票計入目標。但是，在某些情況下，商店所有者可能希望將在此商店開立的所有發票都計入集資。

#### 其他客製化選項

BTCpay Server提供了一些額外的自定義功能。添加聲音，動畫，甚至討論主題到Crowdfund。店主也可以通過輸入自己的自定義 CSS 來改變 Crowdfund 的外觀和感覺。

#### 刪除此應用程式

如果店主想從他的BTCPay伺服器中完全刪除Crowdfund，在更新Crowdfund的底部，店主可以點擊 「刪除此應用程序 」按鈕完全銷毀他們的Crowdfund應用程序。當點擊 "Delete this app "時，BTCPay伺服器會要求輸入`DELETE`並點擊刪除按鈕確認。刪除後，店主會回到BTCPay伺服器儀表板。

### BTCPay 伺服器 - 付款按鈕

易於嵌入的HTML和高度自定義的付款按鈕，讓店主可以收取小費和捐款。在BTCPay伺服器的左邊功能表欄中，插件部分下方，店主可以點擊 「付款按鈕」，然後點擊啟用來創建付款按鈕。

#### 一般設定

在付款按鈕的一般設定中，店主可以設定


- 標準價格
- 預設貨幣
- 預設付款方式
  - 使用商店預設值
  - BTC On-Chain
  - BTC off-chain (閃電)
  - BTC off-chain (LNURL-pay)
- 結帳說明
- 訂單 ID

#### 顯示選項

BTCPay 伺服器的付款按鈕可設定為適合不同風格。按鈕可設定固定或自訂金額，並以滑桿或正負切換顯示。

#### 使用模態

在建立付款按鈕時，店主可以選擇顧客按一下按鈕時的行為，並以模組或新頁面的方式顯示。

**注意！

警告：付款按鈕只能用於小費和捐款

不建議在電子商務整合中使用付款按鈕，因為使用者可以修改訂單相關資訊。對於電子商務，您應該使用我們的 Greenfield API。如果此商店處理商業交易，我們建議您在使用付款按鈕之前先建立一個獨立的商店。

#### 自訂付款按鈕文字

BTCPay Server的付款按鈕預設為 "Pay With BTCPay"。店主可以根據自己的需要設置此文本，並將 BTCPay Server 的標誌更換為自己的標誌。使用 "Pay Button Text 「設置文字，並在 」Pay Button Image URL "下粘貼圖片URL。

##### 圖片尺寸

按鈕中圖片的大小只能設定為三個預設值。


- 146x40px
- 168x46px
- 209x57px

#### 按鈕類型

BTCPay伺服器知道付款按鈕有三種狀態。


- 固定金額
  - 之前設定的價格在按鈕的一般設定中。
- 自訂金額
  - BTCPay 伺服器的 Pay 按鈕有 + 和 - 切換鍵，可設定自訂價格。
  - 當使用自定義金額時，BTCPay伺服器會要求一個最小值、最大值，以及它應該如何逐漸增加。
  - 按鈕可設定為「使用簡易輸入樣式」。
  - 在按鈕和切換按鈕出現在線上時，將按鈕合併在線上。
- 滑桿
  - 類似於自訂數量，但在視覺上有所不同，因為它有一個滑桿，而不是 +/- 切換鍵。
  - 當使用滑桿時，BTCPay伺服器會要求一個最小值、最大值以及逐漸增加的幅度。

**注意！

刪除付款按鈕可在警告說明的頂部進行。

#### 付款通知

伺服器 IPN (即時付款通知) 是為 webhooks 而設，可透過 URL 填入購買後的資料。

#### 電子郵件通知

每當付款發生時，BTCPay伺服器可以通知店主。

#### 瀏覽器重定向

當顧客完成購買時，如果店主有設定，他將會被重定向到這個連結。

#### 進階付款按鈕選項

指定額外的查詢字串參數，Invoice 建立後，這些參數會附加到結帳頁面。例如，`lang=da-DK` 預設會以丹麥語載入結帳頁面。

#### 使用應用程式作為端點

在之前的 PoS 或 Crowdfund 應用程式中，直接將付款按鈕連結至項目。

店主可按下拉式選單，選擇所需的 App；選擇 App 後，店主即可新增需要連結的項目。

#### 生成代碼

由於BTCPay伺服器的付款按鈕是Easily-embeddable HTML，BTCPay伺服器在配置付款按鈕後，會在底部顯示產生的代碼，以便複製到網站中。

店主可以將產生的程式碼複製到自己的網站上，BTCPay伺服器的付款按鈕就會直接在他們的網站上啟動。

#### 付款通知

伺服器 IPN (Instant Payment Notification，即時付款通知) 是為 webhooks 而設，可透過 URL 填入購買資料。

#### 電子郵件通知

每當有付款發生時，BTCPay伺服器可以通知店主。

#### 瀏覽器重定向

當顧客完成購買時，如果店主有設定，他將會被重定向到這個連結。

#### 進階付款按鈕選項

指定額外的查詢字串參數，Invoice 建立後，這些參數會附加到結帳頁面。例如，`lang=da-DK` 預設會以丹麥語載入結帳頁面。

#### 使用應用程式作為端點

直接將付款按鈕連結至之前 PoS 或 Crowdfund 應用程式之一的項目。店主可以點擊下拉式選單，選擇所需的應用程式，選定應用程式後，店主就可以新增需要連結的項目。

#### 生成代碼

由於BTCPay伺服器的付款按鈕是Easily-embeddable HTML，BTCPay伺服器在設定付款按鈕後，會在底部顯示產生的代碼，以供複製到網站上。店主可以將生成的代碼複製到自己的網站上，BTCPay Server的支付按鈕就可以直接在他們的網站上啟用了。

### 技能摘要

在本節中，您將學習到


- 如何使用 BTCPay 伺服器的整合式 PoS 外掛程式輕鬆建立自訂商店
- 如何使用BTCPay伺服器的整合式集資外掛，輕鬆建立自訂的集資應用程式
- 使用 Pay Button 外掛產生自訂付款按鈕的程式碼

### 知識評估

#### KA 檢閱

BTCPay Server 標配的三個內置插件是什麼？請用幾個字描述每種插件的使用方式。

# 設定 BTCPay 伺服器

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## 在 LunaNode 環境中安裝 BTCPay 伺服器的基本瞭解

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### 在託管環境中安裝 BTCPay 伺服器 (LunaNode)

這些步驟將提供在 LunaNode 上開始使用 BTCPay 伺服器的所有必要資訊。如何部署軟體有許多選項。

您可以在 https://docs.btcpayserver.org 找到 BTCPay 伺服器的所有詳細資訊。

#### 我們從哪裡開始？

在本部分中，您將熟習 LunaNode 作為主機供應商，了解使用 BTCPay 伺服器的第一步，並學習如何使用 Lightning Network。在我們完成所有步驟後，您就可以運行一個接受 Bitcoin 的網路商店或集資平台！

這是部署BTCPay伺服器的多種方法之一。詳情請閱讀我們的說明文件、

https://docs.btcpayserver.org。

### BTCPay 伺服器 - LunaNode 部署

#### LunaNode 部署

首先，前往 LunaNode.com 網站，在此建立新帳戶。按一下右上方的「註冊」或使用其首頁上的「開始使用」精靈。

![image](assets/en/111.webp)

在您建立新帳戶後，LunaNode 會寄發一封驗證電子郵件。一旦您驗證帳戶，與 Voltage 相比，您會立即收到充值帳戶餘額的提示。這筆餘額需要用來支付伺服器空間和託管費用。

![image](assets/en/112.webp)

#### 為您的 LunaNode 帳戶增加點數

點選「存入信用額」後，您就可以設定要為帳戶充值多少金額，以及付款方式。LunaNode 和 BTCPay 伺服器的費用在 10 美元到 20 美元/月之間。

相較於 Voltage.cloud，您可以完全存取您的虛擬私人伺服器（VPS），因此對您的伺服器有更多的控制權。在您建立新帳戶後，LunaNode 會寄出一封驗證電子郵件。

一旦您驗證了帳戶，與 Voltage 相比，您現在會立即收到充值帳戶餘額的提示。這筆餘額需要用來支付伺服器空間和寄存費用。

#### 如何部署新伺服器？

在本指南中，我們將透過建立一組 API 金鑰，並使用 LunaNode 製作的 BTCPay 伺服器啟動器來進行設定。

在您的 LunaNode 面板中，按一下右上方的 API。這會開啟一個新的頁面。我們只需要設定 API 金鑰的名稱。其餘的將由 LunaNode 處理，本指南將不會涵蓋。按一下「建立 API 認證」按鈕。

建立 API 認證後，您會得到一長串字母和字元。這就是您的 API 金鑰。

![image](assets/en/113.webp)

#### 如何部署新伺服器？

這些憑證有兩部分，API key 和 API ID；我們兩者都需要。在進行下一步之前，讓我們在瀏覽器中開啟第二個標籤，並前往 https://launchbtcpay.lunanode.com/

這裡會要求您提供 API key 和 API ID。這是為了驗證是否是您提供這台新伺服器。API 金鑰應該仍在您之前的索引標籤中開啟；如果您在下表中向下捲動，就會發現 API ID。

回到有 Launcher 的頁面，在欄位中填入您的 API 金鑰和 ID，然後按一下繼續。

![image](assets/en/114.webp)

在下一步，您可以提供一個域名。如果您已經擁有一個網域名稱，並希望將其用於 BTCPay 伺服器，請確保您也在您的網域名稱上新增 DNS 記錄 (稱為 `A` 記錄)。如果您沒有網域，請使用 LunaNode 提供的網域 (您可以稍後在 BTCPay 伺服器設定中變更)，然後按繼續。

閱讀更多關於設定或變更 BTCPay 伺服器的 DNS 記錄; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### 在 LunaNode 上啟動 BTCPay 伺服器

完成之前的步驟後，我們可以為新伺服器設定所有選項。在此，我們將選擇 Bitcoin (BTC) 作為我們的支援貨幣；我們可以設定電子郵件，以獲得有關加密證書更新的通知；這並非必須的。

本指南的目標是設定 Mainnet 環境（實際環境為 Bitcoin）；然而，LunaNode 也允許您將其設定為 Testnet 或 Regtest，以供開發之用。本指南將保留 Mainnet 選項。

選擇您的 Lightning 實作。LunaNode 提供兩種不同的實作，LND 和 Core Lightning。在本指南中，我們將採用 LND。這兩種實現方式的差異不大，但確實存在差異；如需瞭解更多，建議閱讀廣泛的說明文件；https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln。

![image](assets/en/115.webp)

LunaNode 提供多種虛擬機 (VM) 計劃。這些在價格範圍和伺服器規格上都有所不同。在本指南中，使用 m2 計劃即可；但是，如果您勾選的貨幣不只是 Bitcoin，請考慮至少使用 m4。

加速初始 Blockchain 同步；這是選擇性的，取決於您的需求。還有一些進階選項，例如設定 Lightning 別名、指向特定的 GitHub 發行版或設定 SSH 金鑰；本指南將不會觸及這些選項。

填寫完表格後，您必須點選啟動虛擬機器，Lunanode會開始建立您的新虛擬機器，包括安裝BTCPay伺服器。這個過程需要幾分鐘；一旦您的伺服器準備就緒，LunaNode會給您新BTCPay伺服器的連結。

創建過程結束後，點擊您的BTCPay服務器鏈接；在此，您將被要求創建一個管理員帳戶。

![image](assets/en/116.webp)

### 技能摘要

在本節中，您將學習到


- 在 LunaNode 上建立帳戶並提供資金
- 使用 BTCPay 伺服器啟動器來建立您自己的伺服器

### 知識評估

#### KA 概念回顧

說明在 VPS 上執行 BTCPay 伺服器實例與在託管實例上建立帳戶之間的一些差異。

## 在電壓環境下安裝 BTCPay 伺服器

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

您將熟習 Voltage.cloud 作為主機提供商，了解使用 BTCPay 伺服器的第一步，並學習如何使用 Lightning Network。在我們完成所有步驟後，您就可以運行一個接受 Bitcoin 的網路商店或集資平台！

這是部署BTCPay伺服器的多種方法之一。詳情請閱讀我們的說明文件、

https://docs.btcpayserver.org。

### BTCPay 伺服器 - Voltage.cloud 部署

首先，前往 Voltage.cloud 網站註冊新帳戶。建立帳戶時，您可以註冊 7 天免費試用。點擊右上方的註冊或使用其首頁上的 「免費試用 7 天」。

![image](assets/en/117.webp)

建立帳戶後，按一下儀表板上的 `NODES` 按鈕。一旦我們選擇了節點並建立了一個新的節點，我們就會看到Voltage提供的可能的節點。由於本指南也會介紹LightningNetwork，在Voltage，我們首先要選擇我們的Lightning實現，然後再創建一個BTCPay服務器。點擊 LightningNode。

![image](assets/en/118.webp)

在這裡，您必須選擇想要哪一種 Lightning 節點。Voltage 為您的燈光設定提供了多種選項。這在使用 LunaNode 部署時有所不同。就本指南而言，使用 Lite 節點就足夠了。閱讀更多關於 Voltage.cloud 的差異。

![image](assets/en/119.webp)

為您的節點命名、設定密碼，並保護此密碼。如果此密碼丟失，您將無法存取備份，而 Voltage 也無法復原。建立節點，Voltage 會向您顯示進度。Voltage 已為您建立了 Lightning 節點。現在我們可以建立 BTCPay 伺服器實例，並直接存取 Lightning Network。

點擊儀表板左上方的節點。在此您可以設置您的 BTCPay 伺服器實例的下一部分。進入節點總覽後，點擊 "create new"。您會看到與之前相似的畫面。現在我們選擇 BTCPay Server，而不是 Lightning Node。

Voltage 顯示您 BTCPay 伺服器的地理位置，voltage 主機位於美國西部地區。在此，您還可以看到伺服器的託管費用。點擊 「創建 」並給您的BTCPay服務器命名。啟用 Lightning，Voltage 會顯示上一步所建立的 Lightning 節點。點擊Create，Voltage會創建一個BTCPay伺服器實例。

![image](assets/en/120.webp)

按下建立後，Voltage 會顯示預設的使用者名稱和密碼。這些與您之前在 Voltage 設定的密碼相似。點擊 「登錄到帳戶 」按鈕，您將被重定向到您的BTCPay服務器。

歡迎使用您新的BTCPay伺服器實例。由於我們已在建立過程中設定了 Lightning，因此會顯示 Lightning 已經啟用！

### 技能摘要

在本章中您將學習到


- 在 Voltage.cloud 上建立帳戶
- 讓BTCPay伺服器與帳戶上的Lightning節點一起運作的步驟

### 知識評估

#### KA 概念回顧

Voltage 和 LunaNode 設定之間有哪些主要差異？

## 在 Umbrel 節點上安裝 BTCPay 伺服器

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

這些步驟結束後，您就可以在您的本地網絡上接受閃電付款到您的 BTCPay 商店。如果您在餐廳或企業中運行一個 umbrel 節點，這個過程也同樣適用。如果您想將此商店連接到公共網站，請按照進階練習，將您的 umbrel 節點公開。

https://umbrel.com/

![image](assets/en/121.webp)

### BTCPay 伺服器 - Umbrel 部署

當您的 Umbrel 節點與 Bitcoin Blockchain 完全同步後，前往 Umbrel App Store，在 Apps 下方搜尋 BTCPay Server。

![image](assets/en/122.webp)

點擊BTCPay Server查看App詳情。當 BTCPay Server 的詳細資料開啟時，右下方會顯示應用程式正常執行的需求。它顯示需要Bitcoin和Lightning節點。如果您尚未在Umbrel上安裝Lightning節點，請點擊 「安裝」。這個過程可能需要幾分鐘。

![image](assets/en/123.webp)

安裝您的 Lightning Node 之後：

1.按一下應用程式詳細資訊中的開啟，或 Umbrels 面板中的應用程式。

2.按一下 setup a new node（設定新節點）；您將會看到 24 個恢復閃電節點的字元。

3.把這些寫下來。

![image](assets/en/124.webp)

Umbrel會要求驗證剛才寫下的字。Lightning 節點設定完成後，回到 Umbrel App Store 並找到 BTCPay Server。點擊安裝按鈕，Umbrel會顯示是否已安裝所需的元件，以及BTCPay Server需要存取這些元件。安裝完成後，點擊App詳情右上方的開啟或通過您的Umbrels儀表板開啟BTCPay Server。

Umbrel 會要求確認剛才寫下來的字。

![image](assets/en/125.webp)

**注意！

請確保將這些物品存放在適當的位置，就像之前學習的存放鑰匙一樣。

Lightning 節點設定完成後，返回 Umbrel App Store 並找到 BTCPay Server。點擊安裝按鈕，Umbrel會顯示是否已安裝所需的元件，以及BTCPay Server是否需要存取這些元件。

![image](assets/en/126.webp)

安裝完成後，點擊App詳細資料右上方的開啟或通過您的Umbrels儀表板開啟BTCPay伺服器。

![image](assets/en/127.webp)

### 技能摘要

在本節中，您將學習到


- 在 Umbrel 節點上安裝具有 Lightning 功能的 BTCPay 伺服器的步驟

### 知識評估

#### KA 概念回顧

Umbrel 上的設定與前兩個託管選項有何不同？

# 總結

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>

## 評論與評分

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>
## 課程總結

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>