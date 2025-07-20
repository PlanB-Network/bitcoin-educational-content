---
name: PayJoin - 麻雀 Wallet
description: 如何在 Sparrow Wallet 上進行 PayJoin 交易？
---

![tutorial cover image sparrow payjoin](assets/cover.webp)


_**WARNING:** 在 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被查封之後，Samourai Wallet 上的 Payjoins Stowaway 現在只能透過手動交換 PSBT 的方式來運作，前提是雙方使用者都連線到自己的 Dojo。至於 Sparrow，透過 BIP78 進行的 Payjoins 仍然有效。不過，這些工具可能會在未來幾週內重新啟動。在此期間，您可以隨時閱讀這篇文章，瞭解 payjoins._ 的理論功能。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> *迫使 Blockchain 間諜重新思考他們自以為知道的一切。

PayJoin 是特定的 Bitcoin 交易結構，可透過與付款收款人協同合作，增強使用者在消費時的隱私權。有幾種實作可促進 PayJoin 的設定和自動化。在這些實作中，最知名的是 Samourai Wallet 團隊開發的 Stowaway。本教學旨在引導您使用 Sparrow Wallet 軟體進行 Stowaway PayJoin 交易。


## Stowaway 如何運作？


如前所述，Samourai Wallet 提供了一個名為 "Stowaway" 的 PayJoin 工具。可透過 PC 上的 Sparrow Wallet 軟體或 Android 上的 Samourai Wallet 應用程式存取。若要執行 PayJoin，接收者 (同時也是合作者) 必須使用與 Stowaway 相容的軟體，即 Sparrow 或 Samourai Wallet。這兩種軟體是互通的，可以在 Sparrow Wallet 和 Samourai Wallet 之間進行 Stowaway 交易，反之亦然。


Stowaway 依賴於 Samourai 稱為「Cahoots」的交易類別。Cahoot 基本上是多位使用者之間的協同交易，需要 off-chain 資訊 Exchange。目前，Samourai 提供兩種 Cahoots 工具：Stowaway (Payjoins) 和 StonewallX2 (我們將在未來的文章中探討)。


Cahoots 交易涉及使用者之間交換部分已簽署的交易。這個過程可能既冗長又麻煩，尤其是遠端執行時。但是，它仍然可以與其他使用者手動完成，如果合作者距離很近，這會很方便。實際上，這需要手動交換五個 QR 代碼，然後陸續掃描。


在遠端進行時，這個過程會變得太複雜。為了 Address 這個問題，Samourai 開發了一個以 Tor 為基礎的加密通訊協定，稱為 "Soroban"。有了 Soroban，PayJoin 所需的交換就會自動在使用者友善的 Interface 後面進行。這是我們在本文中要探討的第二種方法。


這些加密交換需要在 Cahoots 參與者之間建立連線和驗證。Soroban 的通訊依賴使用者的 Paynyms。如果您不熟悉 Paynyms，我邀請您參考這篇文章以瞭解更多詳細資訊：[BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

簡單來說，Paynym 是與您的 Wallet 相連的唯一識別碼，可使用各種功能，包括加密訊息。Paynym 以識別碼和代表機器人的插圖形式呈現。以下是我在 Testnet 上的範例： ![Paynym Sparrow](assets/en/1.webp)


**總結：**



- _Payjoin_ = 合作交易的特定結構；
- _Stowaway_ = 可在 Samourai 和 Sparrow Wallet 上實作的 PayJoin；
- _Cahoots_ = Samourai 給他們所有合作交易類型的名稱，包括 PayJoin Stowaway；
- _Soroban_ = 在 Tor 上建立的加密通訊協定，允許在 Cahoots 交易中與其他使用者合作。
- _Paynym_ = Wallet 的唯一識別碼，允許與 Soroban 上的其他使用者通訊，以便

進行 Cahoots 交易。


[**-> 進一步瞭解 PayJoin 交易及其效用**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## 如何在 Paynyms 之間建立連接？


要透過 Samourai 或 Sparrow 執行遠端 Cahoots 交易，特別是 PayJoin (Stowaway)，必須使用 Paynym 來「追蹤」您想要合作的使用者。在Stowaway的情況下，這意味著關注您想要發送比特幣的人。


**以下是建立此連線的程序：**


首先，您需要獲得收件人的 Paynym 識別碼。這可以使用他們的暱稱或付款代碼來完成。要做到這一點，從收件人的 Sparrow Wallet，選擇 「工具 」標籤，然後點擊 「顯示 PayNym」。

![Show Paynym](assets/notext/2.webp)

![Paynym Sparrow](assets/en/1.webp)

在您這邊，打開您的 Sparrow Wallet 並進入相同的 `Show PayNym` 選單。如果您是第一次使用您的 Paynym，您需要通過點擊 `Retrieve PayNym` 來獲得一個識別碼。

![Retrieve paynym](assets/notext/3.webp)

接下來，在 「尋找聯絡人 」方塊中輸入合作者的 Paynym 識別碼（其暱稱 "+... 「或其付款代碼 」PM...「），然後點擊 」添加聯絡人 "按鈕。

![add contact](assets/notext/4.webp)

軟體隨後會為您提供「連結連絡人」按鈕。我們的教程不需要點擊這個按鈕。只有當您打算在 BIP47 的情況下向所示的 Paynym 付款時才需要此步驟，這與我們的教程無關。


一旦收件人的 Paynym 被您的 Paynym 跟隨，請朝相反方向重複此操作，使收件人也跟隨您。然後您就可以執行 PayJoin。


## 如何在 Sparrow Wallet 上執行 PayJoin？


如果您已完成這幾個初步步驟，您終於可以執行 PayJoin 交易了！若要執行，請遵循我們的視訊教學：

![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)


**外部資源：**



- https://docs.samourai.io/en/spend-tools#stowaway ；
- https://sparrowwallet.com/docs/spending-privately.html。