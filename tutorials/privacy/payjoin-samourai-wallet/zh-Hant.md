---
name: PayJoin - Samourai Wallet
description: 如何在 Samourai Wallet 上執行 PayJoin 交易？
---
![samourai payjoin cover](assets/cover.webp)


*** 注意：** Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押後，Samourai Wallet 上的 Payjoins Stowaway 只能透過手動交換 PSBT 的方式運作，前提是雙方使用者都連線到自己的 Dojo。至於 Sparrow，透過 BIP78 進行的 Payjoins 仍然有效。不過，這些工具有可能在未來幾週內重新推出。在此期間，您仍可閱讀這篇文章，瞭解 Stowaway.* 的理論功能。


如果您打算手動執行 Stowaway，程序與本教程中描述的非常相似。主要差異在於 Stowaway 交易類型的選擇：請點選「親自/手動」，而不是選擇「線上」。然後，您需要手動 Exchange PSBT 來建立 Stowaway 交易。如果您與合作夥伴距離很近，您可以連續掃描 QR 碼。如果距離較遠，則可透過安全通訊通道交換 JSON 檔案。本教學的其他內容保持不變。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> *迫使 Blockchain 間諜重新思考他們自以為知道的一切。

PayJoin 是特定的 Bitcoin 交易結構，可透過與付款收款人合作，在消費期間增強使用者隱私。有幾種實作可以促進 PayJoin 的設定與自動化。在這些實作中，最知名的是由 Samourai Wallet 團隊開發的 Stowaway。本教學說明如何使用 Samourai Wallet 應用程式執行 Stowaway PayJoin 交易。


## Stowaway 如何運作？


如前所述，Samourai Wallet 提供了一個名為 "Stowaway" 的 PayJoin 工具。它可透過 PC 上的 Sparrow Wallet 軟體或 Android 上的 Samourai Wallet 應用程式存取。要執行 PayJoin，同時也是合作者的接收者必須使用與 Stowaway 相容的軟體，即 Sparrow 或 Samourai。這兩種軟體是互通的，可以在 Sparrow Wallet 和 Samourai Wallet 之間進行 Stowaway 交易，反之亦然。


Stowaway 依靠 Samourai 稱為 "Cahoots "的交易類別。Cahoot 基本上是多個使用者之間的合作交易，需要 off-chain 資訊 Exchange。到目前為止，Samourai 提供了兩種 Cahoots 工具：Stowaway（Payjoins）和 StonewallX2（我們將在未來的文章中探討）。


Cahoots 交易涉及使用者之間交換部分已簽署的交易。這個過程可能既冗長又麻煩，尤其是遠端執行時。但是，它仍然可以與另一位使用者手動進行，如果合作者的距離很近，這會很方便。實際上，這需要手動交換五個 QR 代碼，然後陸續掃描。


在遠端進行時，這個過程會變得太複雜。為了 Address 這個問題，Samourai 開發了一套以 Tor 為基礎的加密通訊協定，稱為「Soroban」。有了 Soroban，PayJoin 所需的交換就會自動在使用者友善的 Interface 後面進行。這是我們在本文中要研究的第二種方法。


這些加密交換需要在 Cahoots 參與者之間建立連線和驗證。因此，Soroban 的通訊是以使用者的 Paynyms 為基礎。如果您不熟悉 Paynyms，我邀請您參閱這篇文章以瞭解更多細節：[BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)



簡單來說，Paynym 是與您的 Wallet 連結的唯一識別碼，可使用各種功能，包括加密訊息。Paynym 以識別碼和代表機器人的插圖形式呈現。以下是我在 Testnet 上的範例： ![paynym samourai Wallet](assets/en/1.webp)


**總結：**


- _Payjoin_ = 合作交易的特定結構；
- _Stowaway_ = 可在 Samourai 和 Sparrow Wallet 上實作的 PayJoin；
- _Cahoots_ = Samourai 給他們所有合作交易類型的名稱，包括 PayJoin Stowaway；
- _Soroban_ = 在 Tor 上建立的加密通訊協定，允許在 Cahoots 交易中與其他使用者合作；
- _Paynym_ = Wallet 的唯一識別碼，允許與 Soroban 上的其他使用者通訊，以便進行 Cahoots 交易。


[**-> 進一步瞭解 PayJoin 交易及其效用**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## 如何在 Paynyms 之間建立連接？


要透過 Samourai 進行遠端 Cahoots 交易，特別是 PayJoin (Stowaway)，必須使用 Paynym 來「追蹤」您要合作的使用者。在偷渡的情況下，這意味著跟蹤您要寄送比特幣的對象。


**以下是建立此連線的程序：**


首先，您需要獲取收件人 Paynym 的 PayJoin 付款代碼。在 Samourai Wallet 應用程式中，收件人必須點選位於螢幕左上方的 Paynym 圖示 (小機器人)，然後點選他們的 Paynym 暱稱，以 `+...`開頭。例如，我的是 `+namelessmode0aF`。如果您的合作夥伴使用 Sparrow Wallet，我邀請您點選這裡參考我們的專用教學。


![connexion paynym samourai](assets/notext/2.webp)


然後，您的合作者將被重定向到他們的 Paynym 頁面。從那裡，他們可以與您分享他們的 Paynym 認證或分享他們的 QR 代碼供您掃描。要這樣做，他們必須點擊屏幕右上方的小 「分享 」圖標。

![partager paynym samourai](assets/en/1.webp)


在您這邊，啟動您的 Samourai Wallet 應用程式，以相同的方式進入 "PayNyms" 功能表。如果這是您第一次使用 Paynym，您需要取得識別碼。


![demander un paynym](assets/notext/3.webp)


然後按一下螢幕右下方的藍色「+」。

![ajouter paynym collaborateur](assets/notext/4.webp)

然後，您可以選擇「COLLER LE CODE PAIEMENT」貼上合作夥伴的付款代碼，或按下「SCANNEZ LE CODE QR」開啟相機掃瞄他們的 QR 代碼。[貼上 paynym 識別碼](assets/notext/5.webp)


按一下 `SUIVRE` 按鈕。

![follow paynym](assets/notext/6.webp)

按一下「是」以確認。

![confirm follow paynym](assets/notext/7.webp)

軟體隨後會為您提供一個 `SE CONNECTER` 按鈕。我們的教程不需要點擊這個按鈕。只有當您打算作為BIP47的一部分向其他Paynym付款時才需要這一步驟，這與我們的教程無關。

![connect paynym](assets/notext/8.webp)

一旦收件人的 Paynym 被您的 Paynym 跟隨，請朝相反方向重複此操作，使收件人也跟隨您。然後您就可以執行 PayJoin。


## 如何在 Samourai Wallet 上進行 PayJoin？


如果您已完成這些初步步驟，您終於可以執行 PayJoin 交易了！若要執行，請遵循我們的視訊教學：


![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)


**外部資源：**


- https://docs.samourai.io/en/spend-tools#stowaway。