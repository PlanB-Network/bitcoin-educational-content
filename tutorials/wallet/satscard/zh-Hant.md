---
name: Satscard
description: 使用 Nunchuk 設定和使用 Satscard
---
![cover](assets/cover.webp)


Bitcoin 是一種電子現金系統，可讓我們進行點對點交易。然而，為了確保交易的不變性，必須等待數次確認（通常是 6 次），以避免寄件者試圖重複消費。這種確認延遲有時會造成不便，尤其是當需要類似實體現金的即時終結性時。與現金不同的是，鈔票的擁有權會即時轉移，而 Bitcoin 交易則需要等待一段時間，才能確定為不可逆轉。


這就是 Satscard 的用武之地。它提供了一種方法來實現比特幣的實體和即時傳輸，而無需執行 On-Chain 交易。Satscard 的功能就像一張不記名卡，可以安全地傳輸 Bitcoin Ownership，因此提供了更接近傳統現金的體驗。在本教程中，我將向您介紹這種解決方案。


## 什麼是 Satscard？


Coinkite 的 Satscard 是 Opendime 的繼承者。它是一種 NFC 卡，可以實體傳輸比特幣，類似於鈔票或硬幣。與傳統的 Hardware Wallet 不同，Satscard 是一種不記名卡片，這意味著實際擁有這張卡片就等於擁有 Ownership 的比特幣，而這些比特幣都是用儲存在卡片上的金鑰來保護的。其價格在 6.99 美元到 17.99 美元之間，視所選的設計而定。


![SATSCARD](assets/notext/01.webp)


Satscard 晶片配備 10 個插槽，最多可在 10 個不同的位址上儲存 10 次比特幣。每個插槽獨立運作，理論上只需使用一次即可將比特幣鎖定在其中。若要使用比特幣，只需使用相容的應用程式 (如 Nunchuk) 輸入 Satscard 背面註明的 6 位數驗證碼，即可解除插槽的封鎖。


該卡可確保前擁有者一旦實體放棄 Blockchain 卡，就無法保留 Blockchain 上保護比特幣的私人密碼匙。收件人也可以在 Exchange 時驗證插槽的有效性以及其中儲存的金額。


這個系統對於使用比特幣購買實體商品，或將比特幣作為禮物贈送特別有用。


## 如何購買 Satscard？


Satscard 可在 [Coinkite 官方網站](https://store.coinkite.com/store/category/satscard) 購買。若要在實體商店購買，您也可以在網站上找到 [認證經銷商名單](https://coinkite.com/resellers)。

您還需要一部與 NFC 通訊相容的手機，或一個 USB 裝置，以 13.56 MHz 的標準頻率讀取 NFC 卡。

## 如何在 Satscard 上載入插槽？


當您收到 Satscard 後，第一步是檢查包裝，確保它沒有被打開。如果包裝破損，可能表示卡片已被盜用，而且可能不是真卡。


為了管理 Satscard，我們將使用行動應用程式 **Nunchuk Wallet**。請確保您的智慧型手機與 NFC 相容，然後從 [Google Play 商店](https://play.google.com/store/apps/details?id=io.nunchuk.android)、[App 商店](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) 或直接透過 [`.apk`檔](https://github.com/nunchuk-io/nunchuk-android/releases) 下載 Nunchuk。


![SATSCARD](assets/notext/02.webp)


理論上，您可以直接將 bitcoins 傳送至 Satscard 背面指定的 Address，而無需使用 Nunchuk。不過，我建議您不要這麼做，因為我們會先驗證第一個插槽的 Address 確實來自儲存在 Satscard 中的私人密碼匙，而且它不是詐騙的 Address。


如果您第一次使用 Nunchuk，應用程式會讓您建立一個帳戶。就本教程而言，您無需建立帳號。因此，請選擇 「*以訪客身份繼續*」，即可在沒有帳號的情況下繼續使用。


![SATSCARD](assets/notext/03.webp)


然後按一下「*無輔助 Wallet*」。


![SATSCARD](assets/notext/04.webp)


接下來，按一下「*我自己來探索*」按鈕。


![SATSCARD](assets/notext/05.webp)


進入 Nunchuk 主畫面後，按一下畫面上方的「*NFC*」標誌。


![SATSCARD](assets/notext/06.webp)


將 Satscard 對準手機背面進行掃描。


![SATSCARD](assets/notext/07.webp)


Nunchuk 會顯示與您的 Satscard 第一個插槽相對應的接收 Address。通常，這個 Address 應該與您卡片背面手寫的 Address 相同。複製這個 Address，並用它來傳輸您想要鎖定在這個插槽的 bitcoins。


![SATSCARD](assets/notext/08.webp)


## 如何檢查插槽上的 bitcoins？


交易確認後，您可以使用 Nunchuk 掃描 Satscard 的插槽，檢查插槽的餘額。因此，在交易過程中，比特幣的收款人可以透過 Nunchuk 應用程式，立即確認卡中確實有欠他們的比特幣。


![SATSCARD](assets/notext/09.webp)

如果交易對方沒有 Nunchuk 應用程式，他們仍然可以驗證 Satscard 的有效性。只需啟動智能手機上的 NFC，並將 Satscard 放在裝置背面。這將會在瀏覽器中自動打開 Satscard 網站，在此您可以檢查卡片的有效性以及與之相關的比特幣金額。

![SATSCARD](assets/notext/10.webp)


## 如何從插槽中提取 bitcoins？


現在，Satscard 的第一個插槽已經裝入了一定數量的 bitcoins，您就可以將卡交到收款人手上了。


![SATSCARD](assets/notext/11.webp)


如果您是收件人，您需要安裝 Nunchuk。進入應用程式後，按一下螢幕上方的「*NFC*」標誌。


![SATSCARD](assets/notext/12.webp)


將您的 Satscard 放置在手機背面。


![SATSCARD](assets/notext/13.webp)


Nunchuk 會顯示 Address 上的保證金額。


![SATSCARD](assets/notext/14.webp)


若要解封私人密碼匙並將比特幣移到您擁有的 Address，請按一下「*解封並清查餘額*」按鈕。


![SATSCARD](assets/notext/15.webp)


*Sweep to a Wallet*"選項可讓您直接將比特幣傳送至 Nunchuk 應用程式中已有的 Wallet。若要將資金轉移至不同的接收 Address，請選擇「*提款至 Address*」。


![SATSCARD](assets/notext/16.webp)


輸入您要傳送 Satscard 所保證的 bitcoins 的接收 Address。確保輸入的 Address 是正確的 (這是唯一可以驗證的時候)，然後按一下 "*Create transaction*" 按鈕。


![SATSCARD](assets/notext/17.webp)


輸入您 Satscard 的 PIN 碼。這個 6 位數的密碼會在實體卡的背面註明。


![SATSCARD](assets/notext/18.webp)


將 Satscard 放在智慧型手機背面，同時使用儲存在 NFC 卡上的私人密碼匙簽署交易。


![SATSCARD](assets/notext/19.webp)


您的交易現在已簽署，並在 Bitcoin 網路上廣播，這表示您的 Satscard 上使用的插槽現在是空的。


![SATSCARD](assets/notext/20.webp)


## 如何重複使用 Satscard？


與 Opendime 等單次使用的解決方案不同，Satscard 配備的晶片包含 10 個獨立插槽，一張卡最多可進行 10 次操作。第一個插槽由 Coinkite 在出廠前預先設定，對應於寫在 Satscard 背面的接收 Address。


![SATSCARD](assets/notext/21.webp)

若要啟動其他 9 個插槽，您需要透過 Nunchuk 應用程式 generate 配對鑰匙和 Address。在應用程式首頁，按一下螢幕上方的「*NFC*」標誌。

![SATSCARD](assets/notext/22.webp)


將您的 Satscard 放置在手機背面。


![SATSCARD](assets/notext/23.webp)


Nunchuk 表示卡上沒有啟用的插槽，這是正常的，因為第一個插槽已經使用，第二個插槽尚未產生。若要檢視先前使用過的插槽，請按一下「*檢視未封存插槽*」。強烈建議不要重複使用這些插槽，因為這會導致 Address 重複使用對您的 On-Chain 隱私有害。因此，我們將透過按一下「*是*」按鈕來設定一個新的插槽。


![SATSCARD](assets/notext/24.webp)


現在您需要選擇 generate 主鏈代碼的方式。


Satscard 上的插槽遵循 BIP32 標準，這意味著確保比特幣安全的密碼金鑰的推導不像 BIP39 皮夾那樣依賴 Mnemonic 詞組，而是直接依賴主私密金鑰和主鏈碼。這兩個 Elements 在 HMAC-SHA512 函式中作為 generate 子金鑰對的輸入。每個插槽都有自己的主密鑰和主鏈碼。每個插槽只有一層衍生。


第一個插槽的配對密碼匙是由 Coinkite 預先產生的。這就是為什麼您可以透過 Nunchuk 直接存取，以及為什麼接收 Address 會寫在 NFC 卡背面的原因。然而，對於其他插槽，您必須負責產生鑰匙。


每個插槽的主私密金鑰直接由 Satscard 產生，而主鏈碼則必須由外部提供。對於新插槽的連鎖碼，您有兩個選擇：選擇「*自動*」讓 Nunchuk generate 自動產生，或選擇「*進階*」並在專用空格中輸入，以自行建立連鎖碼。為了讓連鎖代碼有效，它需要儘量隨機。


![SATSCARD](assets/notext/25.webp)


輸入 Satscard 背面註明的 6 位數 PIN 碼。


![SATSCARD](assets/notext/26.webp)


將您的 Satscard 放置在手機背面。


![SATSCARD](assets/notext/27.webp)


一個新的插槽已成功配置。現在您可以看到接收 Address 來存入 bitcoins。若要繼續載入，請依照本教學「*如何在 Satscard 上載入插槽？

每張 Satscard 最多可重複此程序 10 次。


恭喜您，現在您已經可以快速使用 Satscard 了！如果您覺得這篇教學對您有幫助，請在下方留下大拇指，我將不勝感激。歡迎在您的社交網路分享這篇文章。非常感謝