---
name: 僅供哨兵監視
description: 什麼是 Watch-only wallet 以及如何使用？
---

![cover](assets/cover.webp)


---

**\*警告：** 在 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押之後，Sentinel 應用程式仍可繼續運作，但**必須使用您自己的 Dojo** 才能存取 Blockchain 資訊和廣播交易。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> 請妥善保管您的私人密碼匙。

在這篇文章中，我們將探討您需要瞭解的有關純手錶錢包的一切。我們會討論它們的運作方式，並檢視市面上不同的應用程式。最後，我們將針對最受歡迎的 Watch-only wallet 應用程式之一提供詳細的教學：Sentinel.


## 什麼是 Watch-only wallet？


Watch-only wallet 或唯讀 Wallet 是一種軟體，其設計目的是允許使用者觀察與一個或多個特定 Bitcoin 公開金鑰相關的交易，而無需存取對應的私人金鑰。


此類應用程式僅保留監控 Bitcoin Wallet 所需的資料，包括檢視其餘額和交易歷史，但無法存取私密金鑰。因此，不可能在僅用於監控的應用程式上花費 Wallet 中持有的比特幣。

![watch-only](assets/en/1.webp)

唯讀一般與 Hardware Wallet 搭配使用。這樣就可以將 Wallet 的私密金鑰「Cold」儲存在未連接網際網路的裝置上，其攻擊面最小，可將私密金鑰與可能易受攻擊的環境隔離。另一方面，僅供觀看的應用程式則專門儲存 Bitcoin Wallet 的擴充公開金鑰 (`xpub`、`zpub`等)。這個母金鑰不允許發現相關的私密金鑰，因此也不允許使用比特幣。但是，它允許子公開金鑰和接收地址的推導。有了 Hardware Wallet 所保護的 Wallet 位址的知識，專用監控應用程式就可以在 Bitcoin 網路上追蹤這些交易，提供使用者監控其餘額和 generate 新接收位址的能力，而不必每次都連上他們的 Hardware Wallet。


## 使用哪種 Watch-only wallet？


目前，由 Samourai Wallet 的團隊所開發的 [Sentinel](https://sentinel.watch/)，是最全面的專用監視應用程式。它包含了優良 Watch-only wallet 的所有基本功能：



- 支援延伸金鑰、公開金鑰和位址；
- 能夠將多個帳戶或錢包組織為收藏集；
- 生成地址，以便在一個人的 Hardware Wallet 上接收比特幣，而不需要直接使用它；
- 離線建構和廣播交易的能力；
- 可選擇連接到自己的 Bitcoin 節點；
- 整合 Tor 以增強隱私。

Sentinel 的獨特缺點在於該應用程式僅適用於 Android，且不支援多重簽章錢包。因此，如果您擁有 Android 裝置，而且您的 Wallet 是經典的單一簽章，我建議您使用 Sentinel。

對於想要追蹤多重簽章 Wallet 的人來說，Blue Wallet 是我所知道的唯一一款為這類型錢包提供只看不動模式的應用程式，而且 Android 和 iOS 都可以使用。


對於尋找 Sentinel 替代方案的 iOS 使用者而言，[Green Wallet](https://blockstream.com/Green/)或 [Blue Wallet](https://bluewallet.io/watch-only/)可能是不錯的選擇，儘管它們的手錶專用功能不如 Sentinel 全面。

![watch-only](assets/notext/2.webp)


## 如何使用 Sentinel Watch-only wallet？


### 安裝與設定


首先安裝 Sentinel 應用程式。您可以從 Google Play 商店或使用 [可從官方網站下載的 APK](https://sentinel.watch/download/)。


![watch-only](assets/notext/3.webp)


首次開啟應用程式時，您可以在以下兩者之間進行選擇：



- `連線到 Dojo`；
- `連線到 Samourai 的伺服器`。


Dojo 由 Samourai 團隊開發，是完整的 Bitcoin 節點版本，可單獨安裝，或一鍵加入節點盒中解決方案，例如 [Umbrel](https://umbrel.com/)、[RoninDojo](https://ronindojo.io/)。


[**-> 探索如何在 Raspberry Pi 上安裝 RoninDojo v2.**](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)


如果您有自己的 Dojo，您可以在此階段連接它。如此一來，您在檢查 Bitcoin 網路交易資訊時，將享有最高等級的隱私權。


![watch-only](assets/notext/4.webp)


否則，可以選擇 Samourai 的預設伺服器。您也可以選擇是否透過 Tor 連線。


![watch-only](assets/notext/5.webp)


然後您就會到達 Sentinel 的主頁面。


![watch-only](assets/notext/6.webp)


要開始使用，您可以設定應用程式。按一下右上角的三個小圓點，然後按一下「設定」。


![watch-only](assets/notext/7.webp)

通過選擇 `用戶 PIN 碼`，您可以選擇設置密碼，以確保訪問您的 Watch-only wallet。您也可以變更將餘額轉換為法定貨幣的參考貨幣，甚至可以啟動`隱藏法定貨幣值`選項來隱藏法定貨幣值。為了提高安全性，您可以啟動 `禁止螢幕截圖`，這可以防止對您的 Sentinel 應用程式進行任何螢幕截圖，從而避免在外部螢幕上洩露任何資訊。

![watch-only](assets/notext/8.webp)


在此設定功能表中，您也可以選擇備份您的 Sentinel。


### 使用 Watch-only wallet


從首頁，按下藍色的 `NEW` 按鈕，新增一個新的擴充公開金鑰來追蹤。接下來，您可以選擇掃描密鑰的 QR 碼，或直接貼上密鑰 (`xpub`、`zpub`...) ，方法是選擇 `Paste Pubkey`。


![watch-only](assets/notext/9.webp)


一般而言，您的 Wallet 的 `xpub` 可透過您使用的 Wallet 管理軟體直接存取。例如，如果您使用 Sparrow 管理 Hardware Wallet，則可在 `Settings` 標籤的 `Keystore` 部分找到此資訊。


![watch-only](assets/notext/10.webp)


在 Sentinel 中輸入擴充公開金鑰後，應用程式會讓您建立新的集合。集合代表一組組織在一起的延伸公開金鑰。這個選項讓您不僅可以列出所有的 `xpubs` ，還可以將它們有序地分類。例如，如果您的 Samourai Wallet 有多個帳戶（存款、premix、postmix......），您可以將所有這些帳戶集中在 `Samourai` 集合下。對於為您的家人管理的錢包，您可以建立一個名為 `Family` 的集合。


選擇「建立新集合」。然後輸入一個您剛剛整合的擴充金鑰的名稱。例如，如果我掃描我的 Samourai Wallet 的存款帳戶，我會將這個金鑰命名為 `Deposit`。按一下 `SAVE` 完成。


![watch-only](assets/notext/11.webp)


接下來，為這個收藏集指定一個名稱，然後按螢幕右上方的驗證圖示來儲存收藏集。現在您的收藏集可在 Sentinel 主畫面上看到。


![watch-only](assets/notext/12.webp)


如果您想要新增另一個擴充的公開金鑰，請再次點選 `NEW`，然後輸入您的金鑰。


![watch-only](assets/notext/13.webp)

接下來，系統會提示您選擇要將這把鑰匙整合到哪個收藏集，或是建立一個新的收藏集。例如，以我為例，我特別為我的 Ledger Wallet 設定了一個收藏集。

![watch-only](assets/notext/14.webp)


若要詳細檢視某個收藏集的延伸金鑰，只需按一下該收藏集。然後，您可以瀏覽不同的索引標籤，檢視交易歷史。


![watch-only](assets/notext/15.webp)


在集合中，點選右上方的三個小圓點，然後點選「檢視未使用的輸出」，即可存取追蹤 Wallet 所持有的 UTXOs 清單。


![watch-only](assets/notext/16.webp)


### 從 Sentinel 傳送和接收比特幣


與任何好的 Watch-only wallet 一樣，Sentinel 允許您 generate 接收地址在追蹤的 Wallet 上接收比特幣。但 Sentinel 還提供另一項進階功能：建立並廣播 Partially Signed Bitcoin Transaction (PSBT)。因此，持有私鑰的 Wallet 可以簽署此交易，一旦簽署，Sentinel 就可以在 Bitcoin 網路上廣播。讓我們看看如何做到這一切。


***如果持有私鑰的 Wallet (例如 Hardware Wallet)沒有明確確認某個 Address 隸屬於它，那麼向這個 Address 發送比特幣就是一種高風險的做法。事實上，如果沒有這個確認，就無法保證 Address 真正屬於您的 Wallet。因此，應該謹慎使用 Watch-only wallet 的接收功能，牢記發送的資金有可能會丟失。


若要透過 Sentinel 接收比特幣，請選擇感興趣的收藏集，然後點選您想要轉帳的擴充公開金鑰對應的標籤。


![watch-only](assets/notext/17.webp)


最後，按一下螢幕左下方的箭頭圖示。Sentinel 會為您產生空白的接收 Address。您可以複製它，或使用 QR 碼掃描它。


![watch-only](assets/notext/18.webp)


要從 Sentinel 進行 generate PSBT，從而啟動消費交易，請前往您要付款的 Wallet 的擴展鑰匙。以我在 Samourai Wallet 上的存款帳戶為例。然後點擊位於螢幕右下方的箭頭圖示。


![watch-only](assets/notext/19.webp)


輸入與交易相關的所有參數：



- 輸入收件人的 Address（按一下 QR 碼圖示，您可以選擇掃描此 Address）；
- 指定要傳送至此 Address 的金額；
- 確定交易費用。


填寫完交易的所有必要欄位後，按「COMPOSE UNSIGNED TRANSACTION」按鈕。


![watch-only](assets/notext/20.webp)


然後，您將存取 PSBT，它代表已建構但未簽署的 Bitcoin 交易，因為 Sentinel 無法存取您的私人密碼鑰匙。您可以選擇複製此交易、匯出為 `.PSBT` 檔案，或透過動畫 QR 碼掃描。


![watch-only](assets/notext/21.webp)


然後，到您擁有私人金鑰的 Wallet 簽署交易（Samourai、Hardware Wallet...）。


![watch-only](assets/notext/22.webp)


交易簽署完成後，您可以返回 Sentinel 將其廣播。要執行此操作，請從主選單按一下右上方的三個小圓點，然後按一下「廣播交易」。


![watch-only](assets/notext/23.webp)


您可以選擇以三種不同的方式輸入已簽署的 PSBT：



- 直接從剪貼簿貼上；
- 從 `.PSBT` 檔案匯入；
- 透過 QR 代碼掃描。


![watch-only](assets/notext/24.webp)


一旦在灰色框中輸入已簽署的交易，您就可以按 Green `BROADCAST TRANSACTION` 按鈕，在 Bitcoin 網路上廣播。Sentinel 會給您它的 txid。


![watch-only](assets/notext/25.webp)