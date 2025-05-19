---
name: 質子 Wallet
description: 安裝和使用 Proton Bitcoin Wallet
---
![cover](assets/cover.webp)


Proton 是一家專精於數位隱私的瑞士公司，由歐洲核子研究中心 (CERN) 科學家於 2014 年創立。Proton 以其開放原始碼解決方案而聞名，提供一整套服務，包括 Proton Mail、Proton VPN 和 Proton Drive。


Proton 最近推出了 Proton Wallet，這是一款開放原始碼、可自行保管的 Bitcoin Wallet，可做為行動應用程式或網頁用戶端，並與您的 Proton 帳戶連結。Wallet 的功能就目前而言相對經典，具備良好 Bitcoin Wallet 應有的基本工具，例如 RBF (*Replace-by-fee*)、標籤或加入 BIP39 passphrase 的功能。


這個 Wallet 的特殊功能是可以使用收件者的電子郵件 Address 來傳送比特幣，Proton 會自動產生一個空白的 Bitcoin Address 連接到使用者的 Wallet。Proton 計畫在未來增加新功能，包括 Lightning 和 Coinjoins（可能使用 Whirlpool，根據他們 GitHub 儲存庫上的活動顯示）。


## 建立 Proton 帳戶


要使用 Proton Wallet，您需要一個 Proton 帳戶。您可以按照本教學中創建 Proton 信箱的第一個步驟（僅 「*創建 Proton 帳戶*」部分）免費創建一個帳戶。帳號設定完成後，您就可以繼續本教學的其他部分。


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## 連接至 Proton Wallet


前往 [Proton Wallet 網站](https://proton.me/Wallet) 並點選「*Get Proton Wallet*」按鈕。


![Image](assets/fr/01.webp)


選擇「*免費*」訂閱選項，然後按一下「*登入*」。


![Image](assets/fr/02.webp)


輸入與您的 Proton 帳戶相關聯的電子郵件和密碼以登入。


![Image](assets/fr/03.webp)


現在應該會顯示您的帳戶。按一下「*立即開始使用 Proton Wallet*」。


![Image](assets/fr/04.webp)


## 建立 Bitcoin Wallet


選擇您帳戶的預設法定貨幣，然後按一下「*建立新 Wallet*」。


![Image](assets/fr/05.webp)


您的 Bitcoin Wallet 現在已經建立。理論上您可以馬上開始使用它，但首先儲存您的 Mnemonic 是非常重要的。要做到這一點，請點擊 Interface 右上角的 「*保存您的 Wallet*」。


![Image](assets/fr/06.webp)


如果您還沒有在 Proton 上進行設定，您會被要求為您的帳號設定備份，並使用 2FA 方法保護您的帳號。這些安全措施雖然適用於您的整個 Proton 帳戶，但當您的 Bitcoin Wallet 帳戶整合到其中時，這些安全措施就更為重要。我強烈建議您實施這些措施。


![Image](assets/fr/07.webp)


若要儲存您的 Mnemonic 詞組，請按一下「*備份此 Wallet 的 seed 詞組*」。


![Image](assets/fr/08.webp)


輸入您的 Proton 密碼。


![Image](assets/fr/09.webp)


然後按一下「*檢視 Wallet seed 樂句*」以顯示您的 Wallet 的 Mnemonic 樂句。


![Image](assets/fr/10.webp)


Proton Wallet 顯示您的 12 字 Mnemonic 短語。 **這個 Mnemonic 讓您可以完全不受限制地存取您所有的 bitcoins**。任何擁有此短語的人都可以盜取您的資金，即使沒有進入您的 Proton 帳戶。如果您丟失了您帳戶的訪問權限，這 12 個字的短語可以用來恢復您對比特幣的訪問權限。因此，小心保存並存放在安全的地方是非常重要的。


您可以將它寫在一張紙上，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。


![Image](assets/fr/11.webp)


如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_** 當然，您絕對不應該對這些文字拍照，這與我在本教程中所做的不同。


儲存短語後，按一下「*完成*」按鈕。


![Image](assets/fr/12.webp)


## 探索 Interface


Proton Wallet 的 Interface 非常直觀。在左側，您可以找到您的不同錢包及其相關帳戶。*Primary*" 帳戶是您的主要帳戶。為了保密起見，透過 Proton 電子郵件 Address 收到的比特幣會被放置在一個單獨的帳戶中，命名為 "*Bitcoin via Email*"。


![Image](assets/fr/13.webp)


若要新增帳號，請按一下「*新增帳號*」。


![Image](assets/fr/14.webp)


若要建立新的 Wallet，請按一下「*Wallets*」旁邊的「*+*」符號。


![Image](assets/fr/15.webp)


這時您可以將 BIP39 passphrase 加入新的 Wallet。


![Image](assets/fr/16.webp)


若要加深您對 passphrase 的認識，我建議您參考這篇教學：


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## 接收比特幣


要在您的 Wallet 中接收比特幣，請在 Interface 左側選擇所需帳戶，然後點擊 「*接收*」按鈕。


![Image](assets/fr/17.webp)


Proton Wallet 會自動產生新的空白 Address。


![Image](assets/fr/18.webp)


交易完成後，您可以在「*交易*」中找到它。按一下「*+新增*」，為交易指定一個標籤。


![Image](assets/fr/19.webp)


## 發送比特幣


現在您的 Wallet 中已有比特幣，您可以發送它們了。在 Interface 的左側選擇您要發送的帳戶，然後點擊 「*發送*」。


![Image](assets/fr/20.webp)


輸入收件人的 Bitcoin Address。您可以按一下小標誌掃描 QR 碼。若要傳送至電子郵件 Address，請直接在此欄位輸入。輸入 Bitcoin Address 後，按一下小箭頭，然後按「*確認*」。


![Image](assets/fr/21.webp)


輸入要傳送的金額，可以是法定貨幣或 bitcoins，然後按一下「*Review*」。


![Image](assets/fr/22.webp)


根據目前的市場情況選擇交易費用。


![Image](assets/fr/23.webp)


在交易中加入標籤，然後再檢查所有細節。如果一切正確無誤，請按一下「*確認並傳送*」以簽署並傳送交易。


![Image](assets/fr/24.webp)


您的交易現在會出現在您帳戶的 「*交易*」部分，等待確認。


![Image](assets/fr/25.webp)


## 登入應用程式


除了網頁用戶端之外，Proton Wallet也可透過行動應用程式存取。只要將 Wallet 連結至您的 Proton 帳戶，您就可以在網路用戶端和行動應用程式之間同步您的 Wallet。


從應用程式商店下載 Proton Wallet：




- [On the App Store](https://apps.apple.com/us/app/proton-Wallet-secure-btc/id6479609548)；
- [On Google Play Store](https://play.google.com/store/apps/details?id=me.proton.Wallet.android).


![Image](assets/fr/26.webp)


安裝完成後，點選「*登入*」並輸入您的電子郵件 Address 和 Proton 密碼。


![Image](assets/fr/27.webp)


然後您就可以存取您的 Bitcoin Wallet，功能與網頁用戶端相同。


![Image](assets/fr/28.webp)


恭喜您，現在您知道如何設定和使用 Proton Wallet。如果您覺得這篇教學有用，請在下方留下 Green 的拇指，我將不勝感激。歡迎在您的社交網路分享這篇文章。感謝您的分享！


若要更進一步，我建議您參考 Blockstream 最新 Hardware Wallet Jade Plus 的教學：


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262