---
name: Blockstream Green - 桌面
description: 在電腦上使用 Green Wallet
---
![cover](assets/cover.webp)


在本教程中，我們將探討如何使用電腦上的 Blockstream Green 軟體來管理 Hardware Wallet 上的安全 Wallet。使用 Hardware Wallet 時，必須在電腦上使用軟體來管理 Wallet。此管理軟體無法存取私密金鑰；它僅用於查詢您的 Wallet 結餘、generate 接收位址，以及建立和分發由 Hardware Wallet 簽署的交易。Green 只是管理 Bitcoin Hardware Wallet 的眾多解決方案之一。


在 2024 年，Blockstream Green 僅與 Ledger Nano S（舊版）、Ledger Nano X、Trezor One、Trezor T 和 Blockstream Jade 裝置相容。


## 介紹 Blockstream Green


Blockstream Green 是一款可在手機和桌面上使用的軟體應用程式。前身為 Green Address，此 Wallet 在 2016 年被收購後，成為 Blockstream 的專案。


Green 是一款非常易用的應用程式，特別適合初學者使用。它提供各種功能，例如管理 Hot 錢包、硬體錢包以及 Liquid Sidechain 上的錢包。您也可以用它來設定 Watch-only wallet。


![GREEN-DESKTOP](assets/fr/01.webp)


在本教程中，我們將僅專注於在電腦上使用該軟體。若要探索 Green 的其他用途，請參閱我們的其他專用教學：


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## 安裝和設定 Blockstream Green 軟體


首先在電腦上安裝 Blockstream Green 軟體。前往 [官方網站](https://blockstream.com/Green/)，點選「*立即下載*」按鈕。然後依照您的作業系統進行安裝。


![GREEN-DESKTOP](assets/fr/02.webp)


啟動應用程式，然後勾選「我接受條件...*」方塊。


![GREEN-DESKTOP](assets/fr/03.webp)


當您第一次打開 Green 時，主螢幕會出現沒有設定的 Wallet。之後，如果您建立或匯入錢包，它們就會出現在這個 Interface 中。在繼續建立 Wallet 之前，我建議您調整應用程式的設定以符合您的需求。點擊左下角的設置圖標。


![GREEN-DESKTOP](assets/fr/04.webp)


在 "*General*"（一般*）功能表中，您可以變更軟體語言，並根據需要啟動實驗功能。


![GREEN-DESKTOP](assets/fr/05.webp)


在「*網路*」功能表中，您可以啟用透過 Tor 連線，這個網路會加密您所有的連線，讓您的活動難以被追蹤。雖然這個選項可能會稍微拖慢應用程式的運作速度，但為了保護您的隱私，我們強烈建議您使用這個選項，尤其是當您沒有使用自己的完整節點時。


![GREEN-DESKTOP](assets/fr/06.webp)


對於擁有自己完整節點的用戶，Green提供了通過Electrum伺服器與之連接的選擇，保證了對Bitcoin網路資訊和交易發佈的完全控制。要這樣做，請點選 「*自訂伺服器與驗證*」選單，然後輸入您的 Electrum 伺服器詳細資料。


![GREEN-DESKTOP](assets/fr/07.webp)


另一個替代功能是「*SPV 驗證*」選項，它允許您直接驗證某些 Blockchain 資料，從而減少信任 Blockstream 預設節點的需要，不過此方法無法提供 Full node 的所有保證。此選項也可以在「*自訂伺服器與驗證*」功能表中找到。


![GREEN-DESKTOP](assets/fr/08.webp)


根據您的需求調整這些參數後，您就可以退出此 Interface。


## 在 Blockstream Green 上匯入 Bitcoin Wallet


現在您可以匯入您的 Bitcoin Wallet。按一下「**開始**」按鈕。


![GREEN-DESKTOP](assets/fr/09.webp)


您可以選擇建立本機 Software Wallet 或透過 Hardware Wallet 管理 Cold Wallet。在本教程中，我們將專注於管理 Hardware Wallet，因此您需要選擇「*On Hardware Wallet*」選項。


*Watch-only*" 選項可讓您匯入擴充的公開金鑰 (`xpub`)，以檢視 Wallet 交易，但無法花費相關的資金。


![GREEN-DESKTOP](assets/fr/10.webp)


如果您使用的是 Jade，請按一下對應的按鈕。否則，請選擇「*連接不同的硬體裝置*」。對於 Ledger 使用者，請確定您在 Hardware Wallet 上安裝「*Bitcoin Legacy*」應用程式，因為 Green 只支援此版本。


![GREEN-DESKTOP](assets/fr/11.webp)


將您的 Hardware Wallet 連接到電腦，然後選擇 Green。


![GREEN-DESKTOP](assets/fr/12.webp)


等待 Green 匯入您的 Wallet 資訊，之後您就可以存取。


![GREEN-DESKTOP](assets/fr/13.webp)


此時，有兩種可能的情況。如果您曾經使用過 Hardware Wallet，您應該會看到您的帳號出現在軟體上。但如果您跟我一樣，剛剛透過產生 Mnemonic 詞組來初始化您的 Hardware Wallet，還沒使用過，您就需要建立一個帳號。按一下「*建立帳號*」。


![GREEN-DESKTOP](assets/fr/14.webp)


如果您想使用經典的 Wallet，請選擇「*Standard*」。


![GREEN-DESKTOP](assets/fr/15.webp)


現在您可以存取您的帳戶。


![GREEN-DESKTOP](assets/fr/16.webp)


## 將 Hardware Wallet 與 Blockstream Green 搭配使用


現在您的 Bitcoin Wallet 已設定完成，您已準備好接收第一台 Sats！只要按一下「*接收*」按鈕即可。


![GREEN-DESKTOP](assets/fr/17.webp)


按一下「*Copy Address*」按鈕以複製 Address，或掃描它的 QR 代碼。


![GREEN-DESKTOP](assets/fr/18.webp)


一旦交易在網路中廣播，它就會出現在您的 Wallet 中。等到您收到足夠的確認，就可以認為交易無法更改。


![GREEN-DESKTOP](assets/fr/19.webp)


比特幣已經儲存在 Wallet 中，現在您可以發送比特幣了。點擊 "*Send*"按鈕。


![GREEN-DESKTOP](assets/fr/20.webp)


在下一頁，輸入收件人的 Address。您可以手動輸入或使用網路攝影機掃描 QR 碼。


![GREEN-DESKTOP](assets/fr/21.webp)


選擇付款金額。


![GREEN-DESKTOP](assets/fr/22.webp)


在畫面底部，您可以選擇此交易的收費率。您可以選擇遵循應用程式的建議或自訂費用。相對於其他待處理的交易，費用越高，您的交易處理速度就越快。有關收費市場資訊，請瀏覽 [Mempool.space](https://Mempool.space/) 中的「*交易費用*」部分。


![GREEN-DESKTOP](assets/fr/23.webp)


如果您希望在交易中特別選擇使用哪些 UTXO，請按一下「*手動選擇硬幣*」按鈕。


![GREEN-DESKTOP](assets/fr/24.webp)


檢查您的交易參數，如果一切符合您的期望，請按一下「*下一步*」。


![GREEN-DESKTOP](assets/fr/25.webp)


再次檢查 Address、金額和費用是否正確，然後按一下「*確認交易*」。


![GREEN-DESKTOP](assets/fr/26.webp)


確定 Hardware Wallet 畫面上的所有交易參數都正確，然後用它簽署交易。


![GREEN-DESKTOP](assets/fr/27.webp)


交易從 Hardware Wallet 簽署後，Green 會自動將其廣播至 Bitcoin 網路。您的交易隨後會出現在 Bitcoin Wallet 的儀表板上，等待確認。


![GREEN-DESKTOP](assets/fr/28.webp)


現在您知道如何在 Hardware Wallet 上輕鬆設定 Blockstream Green，以管理您的 Bitcoin Wallet。


如果您覺得本教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。非常感謝


我也建議您參閱 Blockstream Green 手機應用程式設定 Hot Wallet 的其他綜合教學：


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143