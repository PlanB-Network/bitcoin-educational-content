---
name: Voltz
description: 專為您的企業設計的多合一 Lightning wallet。
---

![cover](assets/cover.webp)



Voltz 平台的想法來自一群比特幣玩家，他們希望提供自己的比特幣 wallet 服務。其結果是一個完整的基礎設施，可以在零售點接受比特幣。在本教程中，我們將帶您參觀 Voltz 以及該平台所提供的比特幣整合可能性。



## 開始使用 Voltz



Voltz 是一個完整的平台，提供許多擴充功能，可將比特幣整合為您業務中的銷售點或市場。



前往 [Voltz] 平台 (https://www.voltz.com/en)，點選「Try now」按鈕建立帳號。



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ 設定一個強大的字母數字密碼非常重要，可增加您抵禦暴力攻擊的機會，並檢查您是否確實在 Voltz 官方網站填寫登入資料，以防釣魚網站。



Voltz 介面與 LnBits 平台非常相似。



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz 事實上是建立在 LnBits 伺服器上；請參閱我們的教學，學習如何架設您自己的 LnBits 伺服器，並在上面建立您的解決方案。



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

該平台可讓您有效管理多個投資組合。根據預設，當您註冊時，您會自動擁有一個 Lightning 投資組合。但是，您可以添加其他投資組合。



![wallets](assets/fr/03.webp)



### 可攜性



Voltz 並不局限於網頁介面：在**行動存取**部分，您可以將使用中的 Voltz wallet 連接到 Zeus 或 Blue Wallet 等應用程式。



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

為此，您需要在平台上安裝並啟動 **LndHub** 延伸功能。



![lndhub](assets/fr/04.webp)



選擇您使用中的 Voltz 產品組合，並根據您希望授予的權利，掃描適當的 QR 代碼。




- 發票 QR 代碼只允許您讀取您的投資組合記錄和 generate 新發票。
- 管理員 QR 代碼可讓您檢視歷史記錄、generate 發票，也可支付 Lightning 發票。



![qrs](assets/fr/05.webp)



在本教程中，我們將 Voltz wallet 連接到 Blue Wallet 應用程式。



![connect](assets/fr/06.webp)



一旦我們的投資組合被連接，所有執行的動作都會在 Blue Wallet 和 Voltz 之間同步。例如，當您在 Blue Wallet 上執行 generate 發票時，您在 Voltz 上也會有歷史記錄。



![sync](assets/fr/07.webp)



在**投資組合配置**部分，您可以找到最基本的參數，例如自訂投資組合名稱以及您希望收取付款的貨幣。



![config](assets/fr/08.webp)



### 擴展



Voltz 平台的特色之一是它的模組化，讓您可以啟用您所需要的擴充套件。您可以在**擴充套件**選單中找到擴充套件清單。



![extensions](assets/fr/09.webp)



在這些擴充功能中，TPoS 是您可以用來保存庫存和向客戶收款的銷售點終端機。



![tpos](assets/fr/10.webp)



從銷售終端，您可以 ：




- 獲得可以與客戶和合作夥伴分享的網頁；
- 管理產品庫存；
- 生成 Lightning 發票；
- 透過 Bolt 卡以現金付款。



該擴充套件有免費版本和付費版本，可提供更多的進階功能。若要建立 POS 終端機，請點選擴充套件標誌下方的 ** 開啟** 按鈕，然後點選 ** 新增 POS**。



![new_tpos](assets/fr/11.webp)



定義您的銷售點名稱，然後連接您的 Voltz wallet 到您的終端機來收取付款。您可以勾選**啟動酬金**方塊來啟動酬金。如果您希望向顧客發出收據，也可以啟動發票列印選項 (此功能仍在開發中，因此可能會有故障)。



當您想要將您國家的稅項直接套用在產品上時，銷售點終端機也包含稅務設定。



![tpos](assets/fr/12.webp)



一旦建立您的 POS 終端機，您就可以新增預先設定的產品和服務，以確保您和您的客戶都能享有順暢的付款和會計體驗。



![product](assets/fr/13.webp)



透過定義產品名稱、添加圖片和設定銷售價格來創建您的產品。  您可以將產品分類，方便追蹤。您可以直接將稅項套用至特定產品。如果產品沒有套用稅項，則會自動套用在銷售點終端機建立階段設定的稅項。



![products](assets/fr/14.webp)



您可以按一下 ** 匯入/匯出** 按鈕，從 JSON 格式自動匯入產品清單。



![exports](assets/fr/15.webp)



點選**新標籤**圖示，透過連結進入結帳區域，或點選**QR code**圖示，透過 QR code 與客戶分享您的 POS 平台。



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



您的客戶可以在此介面上查閱目錄及付款。



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



在可用的擴充功能群組中，您還可以找到**Invoice**和**Payment Link**擴充功能等工具，讓您可以用特定產品開具 generate 發票，不需透過 POS 終端機即可收取獨立付款。



## 追蹤您的付款



在 **Payments** 功能表中，Voltz 可讓您概觀各種投資組合的付款情況。


您可以透過 ：




- 狀態。
- 標籤：例如**TPOS**用於銷售點支付，**lnhub**通過Zeus和Blue Wallet錢包中的移動連接。
- 收藏組合。
- 進出付款總額。
- 一個明確的時期。



![payments](assets/fr/22.webp)



## 更多選項



Voltz 也是您可以建立自己的解決方案的基礎架構。在**擴充套件**部分，您可以找到在 Voltz 和 LnBits 生態系統裡開發自己的擴充套件的指南。



![build](assets/fr/23.webp)



如果您想要在生態系統之外開發解決方案，但仍要使用他們的基礎架構，在**節點的 URL** 部分，您會找到 API 金鑰和文件資訊，並附有您可以使用這些資料做什麼的範例。



您可以使用 Voltz wallet 從您的應用程式建立 Lightning 發票、支付 Lightning 發票、解碼和驗證發票。



![keys](assets/fr/24.webp)



現在您已經很好的掌握了 Voltz。如果您喜歡本教程，我們相信您會在我們的課程中學到更多關於比特幣整合到您的業務中的最佳方法和工具：Bitcoin for businesses.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a