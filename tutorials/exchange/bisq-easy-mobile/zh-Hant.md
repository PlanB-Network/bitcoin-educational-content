---
name: Bisq Easy Mobile
description: 針對比特幣新使用者的點對點交易協定 - 無中介、無 KYC。
---
![cover](assets/cover.webp)


## 簡介


Bisq Easy](https://bisq.network/bisq-easy/)交易協定是為 [Bisq 2](https://github.com/bisq-network/bisq2) 所設計，也就是 [Bisq v1](https://github.com/bisq-network/bisq) 的繼承者。Bisq 2 將支援多種交易協定、隱私網路和身分。它有助於購買 Bitcoin，且無交易費用和保證金要求。它適用於尋求非 KYC 選項的新 Bitcoin 買家，這些買家希望由熟悉 Bisq 平台、經驗豐富且知識豐富的賣家有效率地加入。


目前，Bisq Easy 是 Bisq 2 的唯一貿易協定。未來將規劃更多的交易協定。在本教程中瞭解有關 Bisq 2 的更多資訊：


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

本簡短指南是上述使用 [Bisq Easy Mobile](https://github.com/bisq-network/bisq-mobile) 應用程式和 Lightning 購買 Bitcoin 教學的補充。


## 1️⃣開始使用


首先，從 [下載頁面](https://bisq.network/downloads/) 下載 Bisq Easy Mobile。建議 Verify 下載。驗證說明也在 [下載頁面](https://bisq.network/downloads/)。安裝完成後，您需要接受「使用者協議」。接下來，請建立一個包含「暱稱」和頭像（以「機器人圖示」代表）的公開個人檔案。使用 Bisq Easy，您也可以在一個用戶端中建立多個使用者設定檔。經過簡短的初始化後，您會進入「主畫面」。該應用程式會直接在主頁面上突出顯示教育材料。點選「開啟交易指南」以熟悉最新資訊。


![image](assets/en/01.webp)


貿易指南以簡單的步驟說明所有相關內容：



- 如何在 Bisq 上輕鬆交易
- 交易流程如何運作
- 關於貿易規則，我需要知道什麼。


另一個重要部分是 **「在 Bisq Easy 上交易的安全性如何？


![image](assets/en/08.webp)


勾選標有「我已閱讀並瞭解」的方塊，然後點選「完成」。


![image](assets/en/02.webp)


## 2️⃣備份您的資料


在我們開始之前，讓我們先處理一些內務管理任務，並建立資料儲存檔案的`備份`。移至`更多` > `備份與還原`，儲存您的個人資料和交易歷史。如果沒有備份而遺失了您的設備，您的聲譽和正在進行的交易將無法恢復。提供`密碼`來加密您的備份。


![image](assets/en/11.webp)


## 3️⃣優惠


從「首頁」畫面，有兩種方式導覽優惠。點選螢幕中間的 `探索報價 ` 或點選底部功能表中的 `報價 `。從那裡，選擇您要交易的「貨幣」。


![image](assets/en/03.webp)


與需要抵押品的 [Bisq 1](https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04)不同，Bisq Easy 完全依賴賣方的信譽作為擔保。雖然這種方式可讓買方在沒有事先擁有 Bitcoin 的情況下首次購買 Bitcoin，但卻高度信任賣方在收到法幣付款後交付 Bitcoin 的能力。因此，Bisq Easy 安全模式僅針對小額交易進行優化，且每筆交易限制為等值 600 美元，以盡量降低風險。在 "Offerbook "部分，選擇付款方式篩選器，並以 Lightning 或 Bitcoin (on-chain) 進行結算。


![image](assets/en/04.webp)


套用`篩選條件`後，從信譽良好的貿易夥伴中選擇合適的報價。賣家預先選擇的付款方式和結算類型 (`Lightning`或`on-chain`) 將會顯示。在繼續之前，請確保這些與您的偏好相符。我們在此選擇 Lightning ⚡ 選項。


![image](assets/en/05.webp)


點擊「確認接受報價」，查看並確認交易詳情。然後，彈出畫面確認您已成功接受要約。點選 `Open Trades` 中的 Show trade。在 "Open Trades 「部分，粘貼您的 」Lightning invoice「，然後點擊 」Send to the seller "進行分享。現在等待賣家的付款帳戶資料。賣家可能需要時間回應。請定期查看聊天視窗中的更新。


![image](assets/en/06.webp)


在聊天中發送簡短的問候。賣家上線時會分享付款細節


![image](assets/en/09.webp)


收到賣家提供的必要付款詳細資料後，繼續完成付款。之後，點擊「確認已付款」按鈕，耐心等待收款確認。️ ⌛️


最後，當賣家確認收到付款時，您也必須確認收到 Bitcoin。至此，在簡易模式下使用 Bisq 完成購買。祝賀您！現在您可以點選「結束交易」按鈕。


![image](assets/en/10.webp)


## 4️⃣Bisq輕鬆解決爭議


如果您的交易出現任何問題，買賣雙方都可以要求調解支援。


**調解員可以做什麼：**

- 協助順利完成交易

- 驗證法幣、altcoin 和 Bitcoin 付款

- 必要時取消交易

- 向管理員報告嚴重違反規則的行為，以便可能封禁使用者


**欺詐賣家的後果:**

視其信譽類型而定：



- BSQ 債券聲譽**：DAO 可能會沒收他們的保稅 BSQ
- 洋蔥 Address 聲譽**：其 Bisq 1 個洋蔥位址可能會被封禁


**重要注意事項：** 由於所有的聲望都與您的使用者個人資料相關，因此封禁會完全取消您的聲望。


## 5️⃣創建您自己的報價


與其接受現有的出價，您可以建立自己的購買出價，讓賣家來找您。如果您在想要交易的市場中找不到任何具有合適溢價或付款方式的出價，這是正確的選擇，不過您需要等待賣家接受。


從「Offers」畫面，點選右下角的綠色「+」圖示。然後選擇 `購買 Bitcoin`，並選擇您的法定貨幣。


設定您的交易參數：



- 固定金額或範圍金額**：選擇您要花費的金額。
- 付款方式**：從可用選項中選擇
- 設定**：選擇 Lightning ⚡ 或 ₿ on-chain


檢視您的詳細資料，然後點選 `建立報價'。您的報價現在就會出現在 `報價簿 `中。


![image](assets/en/07.webp)


*注意：作為 Bisq Easy 上的買方，您不需要信譽，這是關鍵優勢。賣家需承擔信譽要求和風險，這也是他們收取溢價的原因。您的出價只需要有足夠的吸引力，讓有信譽的賣家考慮即可。


發表後，請在 `Offerbook`區等待。當賣家接受您的出價時，您會收到通知。在 "Open Trades"（開放交易）中開放交易，賣家和您可以在這裡交換付款細節。發送您的 Bitcoin 地址或 Lightning 發票給賣家。發送法幣後，確認付款。一旦賣家確認收到，他們會釋放 Bitcoin 以完成交易。


## 🎯 結論


Bisq Easy 讓 Bitcoin 購買無需抵押品，為新買家解決了經典的雞與蛋問題。其中的得失很明顯：您依賴的是賣家的信譽，而非鎖定的資金作為擔保。這種以信任為基礎的方式解釋了典型的 5-15% 溢價，這是對聲譽良好的賣家在建立信任和提供支援方面的投資的補償。雖然系統限制小額交易以控制潛在損失，但始終堅持選擇信譽良好的賣家。對於願意接受這些條款的新手來說，Bisq Easy 為 Bitcoin 提供了一個簡單的切入點。


## Bisq 輕鬆移動資源


[Github](https://github.com/bisq-network/bisq-mobile) | [Website ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)