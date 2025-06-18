---
name: 標籤 UTXO
description: 如何正確標示您的 UTXO？
---
![cover](assets/cover.webp)


在本教程中，您將發現在 Bitcoin Wallet 中標示 UTXOs 以及硬幣控制所需的一切知識。我們先從理論部分開始，讓您充分了解這些概念，然後再進入實作部分，探討如何在 Bitcoin Wallet 主軟體中具體使用標籤。


## 什麼是 UTXO 標籤？

"標籤」是一種技術，包括將註釋或標籤與 Bitcoin Wallet 內的特定 UTXO 相關聯。這些註釋由 Wallet 軟體本機儲存，絕不會透過 Bitcoin 網路傳輸。因此，標籤是個人管理的工具。


例如，如果我透過 Bisq 與 Charles 進行 P2P 交易時收到一個 UTXO，我可以將它指定為標籤`Bisq P2P Purchase Charles`。


貼上標籤可讓人記住 UTXO 的來源或預期目的地，簡化資金管理並最佳化使用者隱私。當標籤與 「硬幣控制 」功能結合時，標籤功能就變得更加重要。錢幣控制是 Bitcoin 電子錢包中的一個選項，用戶可以手動選擇在創建交易時使用哪些特定的 UTXO 作為輸入。


使用具有硬幣控制功能的 Wallet，再加上 UTXO 標籤，可讓使用者精確區分和選擇交易的 UTXO，從而避免合併不同來源的 UTXO。這種做法可降低「共用輸入 Ownership 啟發式」(CIOH) 所帶來的風險，因為 CIOH 會建議交易的輸入有共用的 Ownership，這可能會損害使用者的隱私。


讓我們回到我來自 Bisq 的無 KYC UTXO 的例子；我想要避免將它與來自受監管 Exchange 平台的 UTXO 結合，例如，來自受監管 Exchange 平台的 UTXO 知道我的身份。透過在我的 no-KYC UTXO 和 KYC UTXO 上貼上不同的標籤，我就能使用硬幣控制功能，輕鬆辨識出哪一個 UTXO 是用來滿足消費的輸入。


## 如何正確標示您的 UTXO？

沒有適合所有人的通用 UTXO 標籤方法。您可以自行定義標籤系統，以便在 Wallet 中輕鬆找到方向。

標籤的一個重要標準是 UTXO 的來源。您只需說明這枚硬幣是如何到達您的 Wallet 的。它是來自 Exchange 平台嗎？客戶的帳單結算？點對點的 Exchange？還是代表購買的零錢？因此，您可以說明：


- `提款 Exchange.com`；
- 付款客戶 David`；
- `P2P購買Charles`；
- 從購買沙發改為購買沙發。

![labelling](assets/en/1.webp)

為了精細您的 UTXO 管理，並遵守您在 Wallet 中的基金分離策略，您可以在標籤中加入額外的指標，以反映這些分離。如果您的 Wallet 包含兩類您不希望混合的 UTXOs，您可以在標籤中整合一個標記，以清楚區分這些群組。


這些分隔標記將取決於您自己的標準，例如 KYC UTXO (知道您的身份) 與 no-KYC (匿名) 之間的區別，或專業與個人資金之間的區別。以之前提到的標記為例，可以翻譯為


- KYC - 提款 Exchange.com`；
- KYC - 付款客戶 David」；
- NO KYC - P2P Purchase Charles`；
- 無 KYC - 由沙發購買變更"。

![labelling](assets/en/2.webp)

無論如何，請記住，好的標籤是您在需要時能夠理解的標籤。如果您的 Bitcoin Wallet 主要用於儲蓄，那麼這些標籤可能在幾十年後才會對您有用。因此，請確保標籤清晰、精確且全面。


此外，建議在整個交易過程中永久標示硬幣。例如，在進行無 KYC UTXO 合併交易時，請務必將所得的 UTXO 不僅標示為「合併」，還特別標示為「無 KYC 合併」，以保持硬幣來源的清晰痕跡。


最後，並不是一定要在標籤上標示日期。大多數 Wallet 軟體已經會顯示交易日期，而且隨時都可以在 Block explorer 上使用其 txid 擷取此資訊。


## 教學：Specter 桌面上的標籤


在 Specter 桌面上連接並開啟您的 Wallet，然後選擇「地址」標籤。


![labelling](assets/notext/3.webp)

在這裡，您會看到您所有地址的列表，以及鎖定在這些地址上的任何比特幣。預設情況下，地址是以其在 `Label` 欄下的索引來識別的。要更改標籤，只需點擊它，輸入所需的標籤，然後點擊藍色圖標確認。

![labelling](assets/notext/4.webp)


您的標籤就會出現在您的地址清單中。


![labelling](assets/notext/5.webp)


您也可以在與寄件者分享接收 Address 時，事先指定標籤。要做到這一點，請存取「接收」標籤，在專用欄位中記下您的標籤。


![labelling](assets/notext/6.webp)


## 教學：在電子圓上貼標籤


在 Electrum Wallet 上，登入您的 Wallet 後，點選「歷史」標籤中您要指定標籤的交易。


![labelling](assets/notext/7.webp)


畫面上會出現一個新視窗。按一下「描述」方塊，然後輸入您的標籤。


![labelling](assets/notext/8.webp)


輸入標籤後，即可關閉此視窗。


![labelling](assets/notext/9.webp)


您的標籤已成功儲存。您可以在「描述」標籤下找到它。


![labelling](assets/notext/10.webp)


在您可以執行硬幣控制的「硬幣」標籤中，您的標籤位於「標籤」欄中。


![labelling](assets/notext/11.webp)


## 教學：在 Green Wallet 上貼標籤


在 Green Wallet 應用程式中，存取您的 Wallet，然後選擇您想要標籤的交易。然後按一下小鉛筆圖示，記下您的標籤。


![labelling](assets/notext/12.webp)


輸入您的標籤，然後按一下 Green「儲存」按鈕。


![labelling](assets/notext/13.webp)


您可以在交易明細和 Wallet 的儀表板上找到您的標籤。


![labelling](assets/notext/14.webp)


## 教學：Samourai Wallet 上的標籤


在 Samourai Wallet 中，您可以使用不同的方法為交易指定標籤。第一種方法是打開 Wallet，選擇您要加入標籤的交易。然後按 「新增 」按鈕，位於 「註釋 」方塊旁邊。


![labelling](assets/notext/15.webp)


輸入您的標籤，然後按一下藍色的「新增」按鈕確認。


![labelling](assets/notext/16.webp)


您可以在交易的詳細資料中找到您的標籤，也可以在 Wallet 的儀表板上找到。


![labelling](assets/notext/17.webp)

對於第二種方法，按一下螢幕右上方的三個小圓點，然後按一下`顯示未使用的交易輸出`功能表。

![labelling](assets/notext/18.webp)


在這裡，您可以找到 Wallet 中所有 UTXO 的完整清單。所顯示的清單與我的存款帳戶有關，但此操作可從專屬功能表導航，複製到 Whirlpool 帳戶。


然後按一下您想要標籤的 UTXO，接著按一下`新增`按鈕。


![labelling](assets/notext/19.webp)


輸入您的標籤，然後按藍色的「新增」按鈕確認。之後您就可以在交易的詳細資料和 Wallet 的儀表板上找到您的標籤。


![labelling](assets/notext/20.webp)


## 教學：在 Sparrow Wallet 上貼標


使用 Sparrow Wallet 軟體，可以用多種方式指定標籤。最簡單的方法是在傳送接收 Address 給發送者時，事先加入標籤。要做到這一點，請在「接收」功能表中，按一下「標籤」欄位，然後輸入您選擇的標籤。只要 Address 收到比特币，这个标签就会被保留并可在整个软件中访问。


![labelling](assets/notext/21.webp)


如果您在收到 Address 時忘記加上標籤，稍後仍可透過「交易」功能表加上標籤。只要在「標籤」欄點選您的交易，然後輸入想要的標籤即可。


![labelling](assets/notext/22.webp)


您也可以選擇從「地址」功能表新增或修改您的標籤。


![labelling](assets/notext/23.webp)


最後，您可以在 `UTXOs` 功能表中檢視您的標籤。Sparrow Wallet 會自動在標籤後面的括號中加入輸出的性質，這有助於區分因變更而產生的 UTXOs 與直接接收的 UTXOs。


![labelling](assets/notext/24.webp)