---
name: 代客 Bitcoin
description: Valet 將非保管型 Lightning 節點帶入您的口袋
---

![cover_valet](assets/cover.webp)



## 簡介


Valet 是一款輕巧、可自行保管的 Bitcoin 和 Lightning wallet，可為初學者提供簡單方便的上線程序。它是特別為服務 Bitcoin 社區和循環經濟而量身打造，尤其是偏遠地區。


它是**Simple Bitcoin Wallet (SBW)**的fork，具有稱為**Fiat Channels**的先進託管 Lightning 通道功能，旨在讓任何人都能接受 Lightning 付款，而不會有波動風險。


Valet 目前僅適用於 Android 裝置，可從數個開放原始碼的應用程式商店下載並安裝。然而，由於開發者隱私權與 KYC 的考量，Valet 並未在**Google Play 商店**。



## 下載並安裝 Valet


Valet 可以從 Standard Sats' GitHub 頁面下載 APK 檔案。[Standard Sats](https://standardsats.github.io/) 是開發 Valet 的公司。


若要下載 Valet，請造訪 Standard Sats [GitHub 頁面](https://github.com/standardsats/valet/releases)，並找出**最新**的版本 (這通常是最頂端的版本)。


👉前往 **Assets**，然後按一下副檔名只有 **.apk** 的檔案。您的下載將會自動開始。


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 下載完成後，請移至裝置的 ** 檔案管理員** > **下載**，然後選取 Valet apk 檔案。


![Select_valet_apk](assets/en/002.webp)


👉安裝，幾秒鐘後，您的應用程式就準備好了，並會出現在您的首頁畫面中。


![valet_icon_on_homescreen](assets/en/003.webp)


另外，您也可以從 **F-Droid** 應用程式商店下載 Valet。如果您的裝置上沒有 F-Droid 應用程式，您可以 [在此](https://f-droid.org/en/) 下載並安裝。


👉在您的主螢幕中，開啟 F-Droid，搜尋 **Valet**。從出現的兩個選項中選取第一個有**紫色和白色圖示的選項**，然後按一下 **下載**。


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉下載完成後，按一下 ** 安裝**，並依照螢幕上的指示操作。安裝完成後，您可以按一下 ** 開啟**，從 F-Droid 啟動 Valet，或從裝置的首頁畫面啟動。



## 建立 Bitcoin Wallet


您只需兩個簡單步驟，即可在 Valet 上設定 Bitcoin wallet。


從裝置的首頁畫面或 F-Droid 應用程式啟動 Valet。wallet 設定畫面將會出現，其中有兩個選項： **Create New Wallet** 和 **Restore Existing Wallet**。


👉選擇 **建立新的 Wallet**，立即就會建立新的 wallet，並將您重定向到首頁。


![set_up_a\_new_wallet](assets/en/006.webp)



## 備份您的種子詞組


👉在 wallet 首頁中，按一下**Green 卡**，該卡上刻有**「點選儲存 wallet 復原短語，以防遺失或更換裝置」。


![seed_phrase_green_card](assets/en/007.webp)


👉將會顯示一組 12 個英文字。按照 1 到 12 的順序將其寫在紙上，並妥善保管。


![the_seed_phrase](assets/en/008.webp)


### 請注意 ⚠️：


請注意下列要素：


- 正如您已經知道的，Valet 是一種自我監護的 wallet，因此您的 seed 詞組是恢復您的 Wallet 的唯一通道。
- 如果您遺失了 seed 詞組，您將永遠***無法存取您的 wallet。
- 如果有人得到您的 seed 詞組，他們就能無可挽回地偷走您所有的 Bitcoin。


因此，您需要寫下 12 個字的 seed 詞組，並將其保存在安全的位置。您絕對不應該截圖、將它儲存在電子郵件的草稿中，或儲存在任何曾經連線到網際網路的電子裝置上。


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## 代客收發 Bitcoin


Valet 是具有 on-chain 和 Lightning Bitcoin 功能的自保管 wallet。這表示您可以透過**On-chain**或**Lightning Network**接收 Bitcoin 並將其傳送出 Valet。


但是，為了能夠通過 Lightning 接收或發送 Bitcoin，您需要使用您的 on-chain Bitcoins 作為 Liquidity 建立一個 Lightning 通道。或者您可以從供應商處購買一些 Lightning 通道流動性。



## 產生鏈上 Bitcoin Address


若要透過 on-chain 接收 Bitcoin，您需要產生一個 Bitcoin 位址。


👉在 wallet 首頁，您會看到一張**橘色**和一張**紫色卡片**，分別標示為 **Bitcoin**和 **Lightning**。


👉按一下標有 **Bitcoin** 的橙色卡片。您會被重新導向到顯示 Bitcoin 位址的螢幕。


![click_on_Bitcoin_card](assets/en/009.webp)


👉您可以 ** 複製** 地址並傳送給寄送 Bitcoin 的人，或按一下 ** 分享** 按鈕，透過社交媒體或其他通訊管道將 QR 代碼傳送給對方。


👉您也可以按一下 ** 編輯** 按鈕，設定應該寄到該地址的 Bitcoin 數量。


**注意：** 就像發票一樣，編輯功能在以下情況下非常有用：您可能希望在某個時間點收到特定數量的 Bitcoin 到某個地址；但是，這並不表示該地址不能收到更高或更低的數量。


點選 **更多新地址**，以產生新的隨機地址。


![generating_a\_bitcoin_add](assets/en/010.webp)


👉您也可以點擊wallet首頁底部的**接收**按鈕，生成on-chain Bitcoin地址。然後選擇**接收到比特幣地址**，繼續上面的相同過程。


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## 透過 On-chain 傳送 Bitcoin


透過 on-chain 從 Valet wallet 傳送 Bitcoin 是一項簡單直接的工作。


👉在 wallet 首頁下方，按一下 **Send** 按鈕，輸入 Bitcoin 位址，或按一下 **Scan**，掃描位址 QR 碼，然後按一下 **Ok**。


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 輸入您要傳送的 Bitcoin 金額。您可以手動輸入以 Sats 或法幣計算的金額，也可以按一下 **Max** 來使用您所有的 on-chain 結餘。


👉您也可以調整您要為交易支付的費用，方法是按一下標示 ** 費用** 的綠色小方塊，然後向右或向左滑動白點，分別增加或減少費用。按一下 **Ok** 以傳送交易。


![enter_amount_and_fee_rate](assets/en/015.webp)



## 設定 Lightning Network 通道


如上文所述，Valet 是一個自我監護的 Bitcoin 和 Lightning wallet；因此，要能夠透過 Lightning 網路傳送和接收 Bitcoin，您必須先設定一個 Lightning 通道，步驟如下：


👉 在首頁畫面中，按一下標示為 **Lightning** 的 ** 紫色卡片**。您將會進入一個有以下選項的頁面：



- 掃描節點 QR
- 在 LNBIG.COM 購買
- 在 BITREFILL.COM 購買
- 請求 LN 圖形重新同步。


當您選擇 **Purchase from lnbig.com** 或 **Purchase from bitrefill.com**，您將會被重定向到這些公司的網站，在那裡您可以購買幾種容量的入站流動性。請暫時忽略最後一個選項 **Request LN graph resync**。


因此，我們的選擇是 ** 掃描節點 QR**。此時，您必須已決定並獲得您要開啟通道的節點的 ** QR 代碼**。您可以開啟通道到您所選擇的任何公共節點。查看 [1ML](https://1ml.com/) 或 [Amboss](https://amboss.space/)，選擇您所選擇的任何公共節點，並掃描您所選擇節點的相關 QR 代碼。


![channel_opening_options](assets/en/016.webp)


您將自動跳轉到下一個頁面，您必須在此為您的頻道注資。同樣地，自我監護 Lightning 網路的使用要求您使用 Bitcoin 為頻道提供資金。這表示您的 on-chain wallet 中必須有 Bitcoin，才能為 Lightning 通道提供資金。請參考 [Hacken](https://hacken.io/discover/lightning-network/) 的這篇文章，閱讀更多關於 Lightning network 的資訊。


![fund_channel](assets/en/017.webp)


👉輸入您要為頻道提供資金的 Bitcoin 的 ** 數量**，或按一下 **Max** 以使用您所有的 on-chain Bitcoin 結餘。您可以調整**費用**，或保留預設費用設定，然後按一下 **確定**。


**注意：** 您為通道提供的資金將是您的新通道的容量（即該通道可進行交易的 Sats 總量）。


同樣重要的是，當您開啟通道時，請使用超過 **100,000 Sats** 作為資金額。這是因為很多 Lightning 節點都要求至少 100,000 Sats 的容量，才能開啟通往它們的通道。因此，為了避免試誤，只要使用高於這個範圍的金額即可。


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉此時，當您檢查您的 wallet 首頁時，您會看到您的注資金額已從**Bitcoin 卡**轉移到**Lightning 卡**。在您的交易記錄上，您會看到資金交易正在處理中。


![channel_funding_processing](assets/en/020.webp)


👉 如果您點擊 Lightning 卡，您會看到顯示您的 Lightning 通道正在開啟的資訊。您也會在交易清單上看到**通道資金交易**。等待您的資金交易在 blockchain 上確認，您的 Lightning 通道就準備好了。


![channel_opening](assets/en/021.webp)


👉確認資金交易後，請立即點擊首頁上的**閃電卡**，即可看到您的閃電通道資訊如下：



- RANDOM SET OF NUMBERS SEPARED BY DOTS:** 這些是節點的 IP 位址。(分別為 IPV4 和 IPV6）
- CAPACITY:** 此為可透過此通道傳送及接收的 Sats 總容量。
- CAN SEND:** 這是您目前可以傳送的 Sats 數量。您會注意到它與**容量**的數字幾乎相同。這是因為您尚未透過該通道發送任何付款。
- CAN RECEIVE:** 這是您目前可以接收到此頻道的 Sats 數量。(這時候幾乎沒有，因為要接收，您必須先送出一些 Sats 來建立一個進入的 Liquidity）。
- REFUNDABLE:** 這項顯示當您關閉您的頻道時，支付回您 on-chain 位址的金額。這也被稱為您的 **頻道本地餘額**。請注意，這筆款項只比頻道容量略少，這是因為關閉頻道時，您必須支付費用才能在 blockchain 上公佈關閉交易，就像您為頻道注資時所做的一樣。因此，系統已扣除您要支付的近似最低金額)。
- VALUE IN FLIGHT:** 當有人傳送一些 sats 到您的頻道，或是您嘗試傳送一些 sats 給某人，不論什麼原因，交易延遲了，通常都會顯示在這個欄位。


![channel_info](assets/en/022.webp)


## 透過您的頻道傳送 Sats


透過 Lightning Network 傳送 Sats 是一項簡單直接的工作。


👉在首頁底部，點擊**發送**，然後在提供的欄位中**粘貼**閃電發票（您必須已經複製），或者點擊**掃描**掃描閃電發票二維碼。


![click_send_or_scan](assets/en/023.webp)


大多數Lightning發票都有預先輸入的付款金額。但在少數情況下，它可能是開放式發票，您必須填寫金額。


👉以 **Dollars** 或 **Sats** 輸入金額，或點選 **Max**，使用您 Lightning 通道上的所有餘額，然後點選 **Ok**。只要找到好的路徑，您的付款就會發送，並在幾秒鐘內完成。請留意首頁是否已完成付款。完成後會有綠色的核取標記。


![enter_the_amount](assets/en/024.webp)


## 透過您的頻道接收 Sats


在您的閃電通道上接收付款主要取決於您是否有一個入站Liquidity。打開通道後，您至少要發送一些 Sats 以 ** 在通道連接的另一端創建入站流動資金**，才能接收付款。要確認您是否可以接收 Sats 以及您可以接收的 Sats 數量，請勾選您通道資訊中的 ** 可以接收** 欄位。這將顯示您在每個時間點收到的 Sats 數量。


現在，假設您已從頻道傳送出一些 Sats，您現在有了入站的流動性，並且可以接收 Sats。


要在 Lightning 通道上接收，您必須生成發票。與使用地址的 Bitcoin on-chain 不同，Lightning 網路使用發票。在 Valet 上生成發票有兩種途徑。


#### 方案 1


👉在首頁底部，按一下 **接收**，選擇 **接收至 Lightning 發票**。在發票中填入要接收的金額，然後按一下 **確定**。複製發票或與付款人分享 QR 碼。


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### 方案 2


點選 wallet 首頁上的紫色 Lightning 卡。點選您頻道上的任何位置，就會彈出選項清單。選擇 **接收到頻道**，然後輸入您要接收的金額（Sats 或美元）。在填寫發票時，您也會看到您可以收到多少 Sats（入貨容量）。按一下 **Ok** 並複製發票或與付款人分享 QR 代碼。


![receive_to_channel](assets/en/028.webp)


**注意：** 第一個選項是通用選項，這表示如果您有多個作用中的頻道，並且使用第一個選項，系統會自動選擇您的其中一個頻道來接收 Sats。


因此，在這種情況下，如果您要接收 Sats 到特定頻道，最好使用第二個選項。


### 您的頻道彈出選項說明


點選您的頻道時，會顯示下列選項欄位：


![channel_pop_ups](assets/en/029.webp)


**SHARE LIGHTNING CHANNEL DETAILS:** 此功能可讓您分享您的頻道詳細資訊，例如遠端對等 ID、本端頻道 ID、資金交易、建立日期等。


**您可以隨時關閉您的閃電通道。要關閉您的通道，系統會檢查您自己通道一側的 Bitcoin 結餘（記住 **「可以發送 」** 欄位，也稱為您的本地結餘），然後將其發送回給您。在 Valet 中，當通道關閉時，您可以選擇要將 Bitcoin 送到哪裡。因此，**關閉通道至 wallet** 是您的兩個選項之一。


👉按一下此選項，然後選擇 **Bitcoin**。頻道關閉將會開始，您的頻道 Bitcoin 結餘將會傳回 wallet 的 on-chain 位址。


![close_channel_to_wallet](assets/en/030.webp)


**CLOSE CHANNEL TO ADDRESS:** 這是關閉頻道的第二個選項。當您選擇此選項時，系統會提示您輸入一個 wallet 位址，您頻道上的 Bitcoin 結餘將會傳送到該位址。請注意，在此選項中，您只能掃描要關閉頻道的 Bitcoin 位址的 QR 代碼。目前沒有手動貼上地址的選項。


👉點擊此選項，掃描 Bitcoin 位址，然後點擊 **Ok**。通道關閉將會開始，您的 Lightning Bitcoin 結餘將會傳送到您掃描的地址。


![scan_address_and_Ok](assets/en/031.webp)


**RECEIVE TO CHANNEL:** 這與產生發票的功能相同，但在某些情況下，您可能擁有多個通道，包括 Fiat 通道 (可在 Valet wallet 中取得的一種獨特 Lightning 通道)。因此，如果您開通了多個渠道，此選項可確保您能收到特定渠道的付款。


**REFILL FROM OTHER CHANNELS:**此選項可讓您從其他現有頻道補足一個頻道的餘額。舉例來說，如果您有兩個不同的 Lightning 頻道 (A、B)，而頻道 A 的 Bitcoin 結餘已用罄，則可使用此選項，輕鬆自頻道 B 自動補充頻道 A 的結餘。


**DIRECT NOT PRIVATE RECEIVE:** 這也是一個產生發票接收付款的選項，但當您使用這個選項時，寄件者會直接付款給您。這意味著，付款不會像一般的 Lightning 付款一樣，在到達您手上之前跳過不同的節點。因此，在本質上，發件人知道他們支付的是您，知道您的通道 ID 等。當您收到來自您信任的來源的付款，並且不需要維護您的隱私時，通常可以使用此選項。


## 託管和 Fiat 頻道


與許多其他 Bitcoin wallet 產品一樣，Valet 是一款簡單輕巧的 Bitcoin 和 Lightning wallet。但它有一個獨特的 Lightning 功能，使它有別於其他大多數的 Bitcoin wallet。這項功能稱為 **託管和 Fiat 頻道**。


Fiat 通道是 Lightning 實現的一種類型，可以輕鬆登入和使用 Lightning 網絡。它是一種託管解決方案，允許完全匿名，就像普通的 Lightning 通道一樣。Fiat 通道技術還可以在 Lightning 網絡上創建 Bitcoin 衍生工具。例如，使用 Fiat 通道，商家可以接受價值穩定的 Bitcoin 付款，而無需擔心 Bitcoin 的波動性。


目前在 Valet 上實現的法定貨幣通道可以創建由 Sats 支持的穩定合成法定貨幣。它使用主機-客戶關係，其中主機是提供此服務的任何 Lightning 節點，客戶是 Valet 用戶。這是一種託管解決方案，因為所有的 Sats 都在主機端；但是，發票生成、傳輸路由和預成像生成仍然發生在客戶端，就像在普通的 Lightning 通道中一樣。


開啟 Fiat 通道的過程與開啟 Lightning 通道相同。唯一的顯著不同是，在這種情況下，客戶（代客操作用戶）無需投入任何流動資金 on-chain 來創建通道容量。主機會為客戶設定通道容量和路由所有付款。


若要開啟 Fiat 通道，請按一下 wallet 首頁上的紫色 **Lightning 卡**。選擇 **Scan Node QR**（此時您必須已確認要開啟頻道的主機，並取得該節點的 QR。您可以開啟 Fiat 頻道的主機節點範例是標準 Sats 的 SATM 節點)。


**注意：** 需要注意的是，任何人都可以成為主機。您所需要的只是運行一個帶有 **Fiat channel 插件** 和 **Hedging 服務**的 Lightning 節點。Fiat channel 是*Standard Sats* 的開放源碼專案。請參閱 [這裡](https://github.com/standardsats/fiat-channels-rfc) 和 [這裡](https://standardsats.github.io/)。


下面的 SATM 節點 QR：


![SATM_node_QR](assets/en/032.webp)


👉 掃描結點 QR 後，按一下 ** 請求美元法幣通道** 或 ** 請求歐元法幣通道** (這是您的法幣結餘將以的法幣面額報價)。目前請選擇美元，然後按一下 **確定**。通道將自動打開，您可以馬上開始接收 Sats。您看，就是這麼簡單！！！


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉進入您的 wallet 首頁，您會看到一張標籤為**USD**的**淺綠色**卡，那是您的**Fiat 通道**。


![fiat_channel_card](assets/en/035.webp)


**Attention:** 當您在法幣通道上接收 Sats 時，您所接收的 Sats 的法幣價值將被鎖定為穩定的餘額，而 Sats 的交易量則隨 Bitcoin 的價格浮動。此解決方案主要是為想要接受 Sats 付款，但又不想面對 Bitcoin 的波動性挑戰的商家所設計。這有助於他們隨時保持價值穩定，同時仍能在 Lightning 網路上進行交易，享受 Bitcoin 作為 Lightning Network 交換媒介的全球覆蓋和快速結算。


當您的 Fiat 頻道建立後，以下是您會看到的 Value 欄位，以及它們各自的意義：


![fiat_channel_info](assets/en/036.webp)



- RANDOM SET OF NUMBERS SEPARED BY DOTS:** 這些是節點的 IP 位址。(分別為 IPV4 和 IPV6）
- 伺服器價格：** 這是主機向您提供服務的 Bitcoin 市場價格。這通常與主要市場價格略有不同，因為主機可能會增加微小的溢價。這完全由主機決定；因此，這也會因主機而異。
- FIAT BALANCE：** 這是您在此頻道上收到的每個 Sat 的鎖定穩定法幣值。請記住，如前所述，只要您在 Fiat 頻道上接收到 Sats，接收時的 Sats 法幣值就會立即鎖定為此欄位中的合成穩定法幣值。您的**法幣餘額**值不會隨 Bitcoin 市價波動。每當您要從這個管道付款時，您只能傳送相當於這個法幣餘額的 Sats。因此可以將此視為以 Sats 為後盾的數位法幣。
- CAPACITY:** 此為可透過此通道傳送及接收的 Sats 總容量。(這也是由主機設定。與一般 Lightning 通道不同的是，主機可視情況調整此容量）。
- CAN SEND:** 這是根據您的法幣餘額，您在每個點可以發送的 Sats 量。這與您在一般 Lightning 頻道所擁有的完全不同，因為這個值會隨著 Bitcoin 價格浮動。因此，您在這裡看到的是您的法幣餘額在任何時候根據**伺服器匯率**所產生的 Sats 價值。
- CAN RECEIVE:** 這是您目前可以接收到此頻道的 Sats 數量。在您建立頻道後，此值應該與頻道容量相同。
- VALUE IN FLIGHT:** 當有人傳送一些 sats 到您的頻道，或當您嘗試傳送一些 sats 給某人，不論什麼原因，交易延遲了，通常會顯示在這個欄位。


以下是有關 Fiat 渠道的重要注意事項：



- 與一般 Lightning 頻道不同的是，當您開啟 fiat 頻道時，您可以立即開始接收 Sats，但無法發送。只有當您收到 Sats 後，才能發送 Sats。
- 在任何時候，所傳送的資產都是 Sats。*Fiat Balance* 只是在任何時間點收到的 Bitcoin 值的合成 IOU 代表。因此，它不是 token 的創造物或新的加密貨幣。
- Fiat 渠道對於因擔心 Bitcoin 的波動性而對接受 Bitcoin 支付持懷疑態度的商家/企業而言，大多數是有用的。對於希望以 Bitcoin 支付員工薪資的公司來說，這也可能是有用的，因為他們不用承擔 Bitcoin 波動的後果，因為 Bitcoin 波動會使他們的薪資資本不穩定。對於居住在主要使用 Bitcoin 的地區，但有固定生活費用的個人而言，這也可能很有用。
- 請注意沒有標示為 **REFUNDABLE** 的欄位。技術上來說，這是因為您無法關閉 Fiat 頻道。您只能將 Fiat 頻道的餘額用於正常的 Lightning 頻道，才能停止使用該頻道。


### 您的 Fiat Channel 彈出式選項說明


當您點選您的 Fiat Lightning 頻道時，下列欄位將會顯示：


![fiat_channel_pop_up](assets/en/037.webp)


**SHARE HOSTED CHANNEL DETAILS:** 此功能可讓您分享 Fiat 頻道的詳細資訊，例如遠端對等 ID、本機頻道 ID、建立日期等。


**EXPORT CHANNEL STATE:** 這可以讓您匯出通道在任何時候的狀態。這在修正通道錯誤時通常很有用，如果有需要，主機可能會要求您分享。


**DRAIN CHANNEL BALANCE：** 如前所述，您在技術上無法關閉 Fiat 通道，但您可以將通道的餘額排到現有的正常 Lightning 通道中。這會自動將相當於您 Fiat 結餘的 Sat 移到您的正常 Lightning 頻道。


**RECEIVE TO CHANNEL:**這與產生發票是一樣的，但在某些情況下，用戶可能有一個以上的Fiat通道與不同的Hosts，包括正常的Lightning通道。因此，如果用戶開通了多個渠道，此選項可確保用戶可以向特定渠道收款。


**REFILL FROM OTHER CHANNELS:** 此選項允許使用者從其他現有頻道重新填滿一個頻道。因此，使用此選項，您可以從一般頻道或您擁有的其他 Fiat 頻道重新填滿您的 Fiat 頻道，就像您可以放水一樣。


**DIRECT NOT PRIVATE RECEIVE:** 這也是一個產生發票收取付款的選項，但當您使用這個選項時，寄件者會直接付款給您。這表示付款在到達您手上之前，不會跳過不同的節點。因此，在本質上，寄件者知道他們支付的是您，也知道您的通道 ID 等等。當您收到來自您信任的來源的付款，且不需要維護您的隱私時，通常可以使用此選項。


## 代客設定：


與其他應用程式一樣，Valet 也有應用程式設定，您可以依自己的喜好調整。您可以從主畫面存取設定頁。


👉 在首頁畫面中，按一下位於畫面右上角的 **Gear** 圖示以存取設定。以下是設定區中的元件。


![settings_icon](assets/en/038.webp)


**LOCAL CHANNEL BACKUP IS ENABLED:**如果這是**Disabled,**您應該啟用它，因為這是當您卸載和重新安裝Valet時恢復正常Lightning頻道的唯一方法。我們稍後會解釋這一點。所以點擊這個，給Valet權限進入您的**媒體存儲**，因為那是備份檔案保存的地方。


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**儲存本地備份的位置：** 只要您允許 Valet 使用您的儲存空間，此欄位將會自動設定為在您的 **Downloads** 資料夾中儲存本地備份。但您也可以點擊此處並選擇任何您想要的資料夾。


**Manage CHAIN WALLETS** 這是一個有點技術性的問題，除非您有足夠的經驗，否則您不需要為此煩惱。這裡的預設設定就很好。


**ADD HARDWARE WALLET:**您也不應該為此麻煩，除非您有想要連接和監控的硬體 wallet。使用此設定，您可以掃描和連接您的硬體 wallet，例如 Trezor 或 Cold 卡，並監視其活動。這是一項僅供觀察的功能，這表示您無法從此處對硬體 wallet 執行交易。您只能觀察和監控 wallet 的活動、餘額等。


**SET CUSTOM ELECTRUM NODE:** 這也是技術性的問題，除非您有足夠的知識，否則不應該為此麻煩。預設設定已經很好了。


**BITCOIN UNITS：** 這是您希望 Bitcoin 結餘的顯示方式。第一個選項以 Satoshi 顯示您的餘額，例如：1,000,000 Sats，而第二個選項以 BTC 小數點顯示，例如：0.01BTC


**USE PIN AUTHENTICATION** 如果勾選此方塊，則必須設定 PIN 或指紋，您必須輸入此 PIN 或指紋才能登入 wallet，並驗證交易。


**USE TOR CONNECTION:** 如果您勾選此方塊，您的交易將透過 Tor 網路進行。它增加了一層額外的隱私，但可能會導致延遲支付吞吐量，特別是對於閃電支付。


**VIEW BIP39 RECOVERY PHRASE:** 在這裡您可以存取您的 12 個字的 seed 備份短語。因此，如果您之前沒有寫下來，或是找不到寫下來的地方，只要您還能存取 Wallet，就可以從這裡複製。


**USAGE STATISTICS：** 這會顯示您自 wallet 建立以來的所有交易和活動摘要。


![usage_stats](assets/en/041.webp)


## Wallet 回收


Valet 是非保管型 wallet，因此如果您遺失裝置或卸載 wallet 應用程式，您需要進行 wallet 復原才能取回您的 Bitcoins 和 Lightning 頻道。在本教程的開頭，我們提到寫下您的**12字seed詞組**的重要性，因為這是恢復您的wallet的關鍵。沒有客戶服務代表可以幫您恢復 wallet。


恢復您的 Valet wallet 需要兩個重要工具，這取決於您是否有一個活躍的 Lightning 頻道。對於沒有使用正常 Lightning 頻道的使用者，只需要他們的 **12 個字的 seed 詞組**，按照以下簡單步驟即可：


👉 安裝新的 Valet 應用程式，並啟動/啟動應用程式。


👉選擇 **還原現有的 Wallet**


![restore_existing_wallet](assets/en/042.webp)


👉選擇 **僅恢復詞組**。


![select_recovery_phrase](assets/en/043.webp)


👉 輸入 12 個字的復原短語，然後按一下 **確定**。


![input_12_words](assets/en/044.webp)


您的 wallet 將被恢復。在這種情況下，只會恢復您的 on-chain Bitcoin 結餘。


但是，如果您有一個啟動中的正常閃電通道，並且您只用復原短語復原您的 wallet，您的閃電通道將被強制關閉，並且您在該通道上的任何 Bitcoin 結餘將自動傳送至您的 on-chain 結餘。


另一個恢復Valet wallet的方法，特別是如果您在卸載Valet之前開啟了一個正常的Lightning頻道，是**使用保存在您設備上的本地備份文件，以及您的12個字的seed短語**。如果您使用這兩個方法，您的 Lightning 頻道狀態將會恢復，因此您的 Lightning 頻道不會被強制關閉。


步驟如下：


安裝新的 Valet 應用程式，並啟動/啟動應用程式。


👉選擇 **還原現有的 Wallet**。


👉選擇 **備份 + 復原短語**。


![select_backup_and_recovery_seed](assets/en/045.webp)


👉從手機的檔案管理員中選取備份檔案。(預設總是儲存在您的 **Downloads** 資料夾）。


![local_backup_file_in_download_folder](assets/en/046.webp)


選取正確的備份檔案後，系統會顯示提示，確認**「備份檔案已存在」**，然後會要求您輸入 12 個字的 seed 詞組。


![enter_12_words](assets/en/047.webp)


👉 輸入 12 個字的復原短語，然後按一下 **OK**。您將進入 wallet 首頁。


👉等待 Bitcoin 網路同步化 (**SYNC**) 以及 Lightning 節點同步化 (**LN Sync**) 完成，您的 wallet 將會完全恢復，包括您的 Lightning 頻道。


![LN_sync](assets/en/048.webp)


## 總結


Valet 是令人振奮的 wallet 解決方案，其功能適合新使用者的上線。它也有一個 Fiat 通道，這是一種不算太新的技術，可確保在 Bitcoin 標準上整合法語經營的企業。


今天就下載 Valet，試試看吧!!!🧡