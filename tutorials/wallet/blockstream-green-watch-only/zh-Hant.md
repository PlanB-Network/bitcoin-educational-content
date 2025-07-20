---
name: Blockstream Green - 僅供觀看
description: Watch-only wallet 配置
---
![cover](assets/cover.webp)


在本教程中，您將發現如何使用 Blockstream Green 應用程式在行動裝置上輕鬆設定「僅限觀看」的 Wallet。


## 什麼是 Watch-only wallet？


唯讀 Wallet 或「Watch-only wallet」是一種軟體，其設計目的是允許使用者觀察與一個或多個特定 Bitcoin 公開金鑰相關的交易，而無需存取對應的私人金鑰。


這類應用程式僅儲存監控 Bitcoin Wallet 所需的資料，尤其是查看其餘額和交易歷史，但無法存取私鑰。因此，Wallet 所持有的比特幣不可能花在僅用於監控的應用程式上。


![GREEN-WATCH-ONLY](assets/fr/01.webp)


唯讀一般與 Hardware Wallet 搭配使用。這可讓 Wallet 的私密金鑰安全地儲存在不連接網際網路、攻擊面極小的硬體上，因此可將私密金鑰與可能易受攻擊的環境隔離。另一方面，僅用於監控的應用程式則專門儲存 Bitcoin Wallet 的擴充公開金鑰 (`xpub`、`zpub`等)。這個父密鑰不能用來尋找相關的私密金鑰，因此也不能用來花比特幣。但是，它可以推導出子公開密鑰和接收地址。由於 Hardware Wallet 知道安全的 Wallet 位址，只看不寫的應用程式可以追蹤 Bitcoin 網路上的這些交易，讓使用者可以監控他的餘額和 generate 新的接收位址，而不必每次都連接他的 Hardware Wallet。


在本教程中，我要向您介紹最受歡迎的手錶專用行動 Wallet 解決方案之一： **Blockstream Green**。


![GREEN-WATCH-ONLY](assets/fr/02.webp)


## 介紹 Blockstream Green


Blockstream Green 是一款可在手機和桌面上使用的軟體應用程式。前身為 Green Address，此 Wallet 在 2016 年被收購後，成為 Blockstream 的專案。


Green 是一款非常易用的應用程式，因此特別適合初學者使用。它提供一系列功能，例如管理 Hot 錢包、硬體錢包和 Liquid Sidechain 錢包。


在本教程中，我們將專注於建立 Watch-only wallet。若要探索 Green 的其他用途，請參閱我們的其他專用教學：


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

## 安裝和設定 Blockstream Green 應用程式


第一步當然是下載 Green 應用程式。前往您的應用程式商店：



- [For Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)；
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN-WATCH-ONLY](assets/fr/03.webp)


對於 Android 使用者，您也可以透過 `.apk` 檔案 [Blockstream 的 GitHub 上提供](https://github.com/Blockstream/green_android/releases) 安裝應用程式。


![GREEN-WATCH-ONLY](assets/fr/04.webp)


啟動應用程式，然後勾選「我接受條件...*」方塊。


![GREEN-WATCH-ONLY](assets/fr/05.webp)


當您第一次打開 Green 時，主螢幕會出現沒有設定的 Wallet。之後，如果您建立或匯入錢包，它們就會出現在這個 Interface 中。在繼續建立 Wallet 之前，我建議您調整應用程式設定以符合您的需求。按一下「應用程式設定」。


![GREEN-WATCH-ONLY](assets/fr/06.webp)


*Enhanced Privacy*" 選項只適用於 Android，可透過停用螢幕截圖和隱藏應用程式預覽來增強隱私。它也會在手機鎖定時自動鎖定應用程式存取權，讓您的資料更難曝光。


![GREEN-WATCH-ONLY](assets/fr/07.webp)


對於希望加強隱私權的人，應用程式提供透過 Tor 將您的流量根植於 Tor 網路的選項，這個網路會加密您所有的連線，讓您的活動難以被追蹤。雖然這個選項可能會稍微拖慢應用程式的運作速度，但為了保護您的隱私，我們強烈建議您使用這個選項，尤其是當您沒有使用自己的完整節點時。


![GREEN-WATCH-ONLY](assets/fr/08.webp)


對於擁有自己完整節點的用戶，Green Wallet 提供了通過 Electrum 伺服器與之連接的可能性，保證了對 Bitcoin 網絡資訊和交易分配的完全控制。


![GREEN-WATCH-ONLY](assets/fr/09.webp)


另一個替代功能是「*SPV Verification*」選項，它允許您直接驗證某些 Blockchain 資料，從而減少信任 Blockstream 預設節點的需要，不過這種方法無法提供 Full node 的所有保證。


![GREEN-WATCH-ONLY](assets/fr/10.webp)


根據您的需要調整這些設定後，按一下「*儲存*」按鈕並重新啟動應用程式。


![GREEN-WATCH-ONLY](assets/fr/11.webp)


## 在 Blockstream Green 上建立 Watch-only wallet


現在您已準備好建立 Watch-only wallet。按一下「*開始*」按鈕。


![GREEN-WATCH-ONLY](assets/fr/12.webp)


您可以選擇幾種類型的 Wallet。在本教程中，我們要建立一個 Watch-only wallet，因此請按一下對應的按鈕。


![GREEN-WATCH-ONLY](assets/fr/13.webp)


選擇「單一簽名」選項。


![GREEN-WATCH-ONLY](assets/fr/14.webp)


然後選擇「*Bitcoin*」。就我而言，我是在 Testnet Wallet 上進行本教學，但在 Mainnet 上的步驟仍然相同。


![GREEN-WATCH-ONLY](assets/fr/15.webp)


您會被要求提供擴充的公開金鑰 (`xpub`、`zpub` 等) 或輸出腳本描述符。


![GREEN-WATCH-ONLY](assets/fr/16.webp)


因此，您需要透過您的 Watch-only wallet 從您想要追蹤的 Wallet 擷取這些資訊。擴充的公開金鑰在安全性上並不敏感，因為它不允許存取私人金鑰，但在您的機密性上卻很敏感，因為它會揭露您所有的公開金鑰，因此也會揭露您所有的 Bitcoin 交易。


比方說，您使用 Sparrow Wallet 來管理 Hardware Wallet 上的 Wallet，您可以在「*設定*」中找到此資訊。找到此資訊取決於您使用的 Wallet 管理軟體，但通常都在設定中。


![GREEN-WATCH-ONLY](assets/fr/17.webp)


複製您的擴展公開金鑰並將其輸入 Green 應用程式，然後按一下「連線」。


![GREEN-WATCH-ONLY](assets/fr/18.webp)


然後您就可以看到與此金鑰相關的餘額以及交易歷史。


![GREEN-WATCH-ONLY](assets/fr/19.webp)


通過點擊 「*接收*」，您可以 generate 接收 Address 在您的 Hardware Wallet 上接收比特幣。但是，我建議在使用這個選項鎖定比特幣之前，不要先在 Hardware Wallet 螢幕上檢查它是否有與生成的 Address 相關聯的私密金鑰。這是一個很好的做法。


![GREEN-WATCH-ONLY](assets/fr/20.webp)


*Balayer*" 選項可讓您手動輸入私人密碼匙，直接從 Green 應用程式支出資金。除非在非常特殊的情況下，否則我不建議使用此功能，因為這需要您在手機上透露私人密碼匙，而手機比 Hardware Wallet 更容易受到電腦攻擊。


![GREEN-WATCH-ONLY](assets/fr/21.webp)


現在您知道如何在智慧型手機上輕鬆設定 Watch-only wallet！它是在 Hardware Wallet 上監控 Wallet 的便利工具，無需每次連接和解鎖。


如果您覺得本教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。非常感謝


我也建議您看看這篇有關 Blockstream Green 應用程式設定 Hot Wallet 的其他綜合教學：


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143