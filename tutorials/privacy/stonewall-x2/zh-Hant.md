---
name: 石牆 x2
description: 瞭解並使用 Stonewall x2 交易
---
![cover stonewall x2](assets/cover.webp)


***警告：** 在 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被查封之後，Stonewallx2 的交易只能透過手動方式在相關各方之間交換 PSBT 來運作，前提是兩位使用者都連線到自己的 Dojo。然而，這些工具有可能在未來幾週內重新啟動。在此期間，您仍然可以參考這篇文章來了解 Stonewallx2 的理論操作，並學習如何手動進行。


如果您正在考慮手動執行一個Stonewallx2，程序與本教程中描述的非常相似。主要的差異在於 Stonewallx2 交易類型的選擇：不要選擇「線上」，請點選「親自/手動」。然後，您需要手動 Exchange PSBTs 來建立 Stonewallx2 交易。如果您與合作夥伴距離很近，您可以連續掃描 QR 代碼。如果距離較遠，則可透過安全通訊通道交換 JSON 檔案。本教學的其他內容保持不變。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> *讓每次花費都是 CoinJoin.*

## 什麼是 Stonewall x2 交易？


石牆 x2 是一種特殊形式的 Bitcoin 交易，旨在透過與未參與該消費的第三方合作，在消費期間增加使用者隱私。此方法模擬兩個參與者之間的迷你 CoinJoin，同時向第三方付款。石牆 x2 交易可在 Samourai Wallet 應用程式和 Sparrow Wallet 軟體上使用。兩者均可互通。


其操作相對簡單：我們使用自己擁有的 UTXO 付款，並尋求第三方的協助，第三方也會使用自己的 UTXO 付款。交易會產生四個輸出：兩個輸出的金額相等，一個輸出到收款人的 Address，另一個輸出到合作人的 Address。第三個 UTXO 返回給合作者的另一個 Address，讓他們取回初始金額（對他們來說是中性的動作，模擬 Mining 費用），最後一個 UTXO 返回給屬於我們的 Address，構成付款的變更。


因此，在石牆 x2 交易中定義了三種不同的角色：


- 寄件者，實際付款者；
- 合作者，提供比特幣以改善交易的整體匿名性，同時在交易結束時完全收回他們的資金 (對他們而言是中性的行為，模擬 Mining 費用)；
- 收款人可能不知道交易的具體性質，只是期望從寄件人處收到付款。


讓我們舉一個例子來更好地理解。Alice 去麵包店買她的長棍麵包，價格是 `4,000Sats`。她想用比特幣付款，同時保持一定的隱私。因此她打電話給她的朋友 Bob，Bob 會在這個過程中協助她。

![schema stonewall x2](assets/en/1.webp)

通過分析這筆交易，我們可以看到麵包師傅確實收到了`4,000 Sats`，作為長棍的付款。Alice 使用了`10,000 Sats` 作為輸入，並收到了`6,000 Sats` 作為輸出，結果淨餘額為`-4,000 Sats`，相當於長棍的價格。至於 Bob，他提供了`15,000 Sats` 作為輸入，並收到兩筆輸出：一筆是`4,000 Sats`，另一筆是`11,000 Sats`，結餘為`0`。

在這個範例中，我故意忽略了 Mining 的費用，以便於理解。實際上，交易費用是由付款寄送者與合作者平分。


## 石牆與石牆 x2 有何不同？


StonewallX2 交易的運作方式與 Stonewall 交易完全相同，只是前者是合作式的，而後者則不是。正如我們所見，Stonewall X2 交易涉及第三方的參與，而第三方是在支付之外的，他們會提供自己的比特幣來加強交易隱私。在典型的石牆交易中，合作者的角色是由發件人扮演的。


讓我們重溫一下愛麗絲在麵包店的例子。如果她找不到像鮑勃這樣的人陪她一起消費，她可以單獨完成石牆交易。因此，兩個輸入的 UTXO 會是她的，而她在輸出時會收到 3 個。

![transaction stonewall](assets/en/2.webp)


從外部觀點來看，交易模式會維持不變。

![Stonewall or Stonewall x2?](assets/en/5.webp)

因此，在使用 Samourai 支出工具時，邏輯應該如下：


- 如果商家不支援 PayJoin Stowaway，則可以使用石牆 x2 與支付外部的其他人進行協同交易。
- 如果找不到人進行石牆 x2 交易，可以模仿石牆 x2 交易的行為，單獨進行石牆交易。
- 最後，最後一個選擇是與由 Samourai 所維護的伺服器 JoinBot 進行交易，JoinBot 可以應要求成為石牆 x2 交易的合作者。


如果您想尋找願意協助您進行石牆 X2 交易的合作者，您也可以造訪這個由 Samourai 使用者維護的 Telegram 群組 (非官方)，以連結發送者與合作者：[Make Every Spend a CoinJoin](https://t.me/EverySpendACoinjoin).


[**-> 進一步瞭解石牆交易**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


## 石牆 x2 交易的目的是什麼？


石牆 x2 結構為交易增加了大量的熵，混淆了連鎖分析。從外觀來看，這樣的交易可解釋為兩個人之間的一小筆 CoinJoin。但實際上，它是一種付款。這種方法會在連鎖分析中產生不確定性，甚至導致錯誤的線索。


讓我們回到 Alice、Bob 和 Baker 的例子。Blockchain 上的交易如下所示：

![stonewall x2 public](assets/en/3.webp)

外部觀察者依賴一般的鏈式分析啟發法，可能會錯誤地得出「Alice 和 Bob 執行了一個小型的 CoinJoin，各以一個 UTXO 作為輸入，並各自以兩個 UTXO 作為輸出」！[誤解石牆 x2](assets/en/4.webp)

這個解釋是不對的，因為大家都知道，有一個 UTXO 傳送給 Baker，Alice 只有一個變更輸出，而 Bob 有兩個。

![transaction stonewall x2](assets/en/1.webp)

即使外部觀察者成功識別出 Stonewall x2 交易的模式，他們也無法掌握所有資訊。他們無法確定兩筆相同金額的 UTXO 中，哪一筆與付款相符。此外，他們也無法知道付款的人是 Alice 還是 Bob。最後，他們也無法判斷這兩個輸入的 UTXOs 是來自兩個不同的人，還是屬於一個合併了這兩個 UTXOs 的人。最後一點是由於我們在上面討論過的經典石牆交易，與石牆 x2 交易的模式完全相同。從外面看，如果沒有關於上下文的額外資訊，我們不可能區分石牆交易和石牆 x2 交易。但是，前者不是合作交易，而後者是合作交易。這就更增加了這項支出的疑慮。

![Stonewall or Stonewall x2 ?](assets/en/5.webp)



## 如何在 Paynyms 之間建立連線，以便透過 Soroban 進行協作？


如同其他在Samourai (*Cahoots*)上的合作交易，執行石牆x2涉及到發送者與合作者之間的部分簽署交易的Exchange。這個 Exchange 可以手動完成 (如果您和合作者在一起)，或是透過 Soroban 通訊協定自動完成。


如果您選擇第二個選項，您需要在Paynym之間建立連線，才能執行石牆X2。要做到這一點，您的 Paynym 必須「跟隨」您合作者的 Paynym，反之亦然。


**取得合作者的 Paynym：**


首先，您必須取得合作夥伴的 Paynym 付款代碼。在 Samourai Wallet 應用程式中，您的合作夥伴必須按下位於螢幕左上方的 Paynym 圖示 (小機器人)，然後按下他們的 Paynym 暱稱，以 `+...`開頭。例如，我的是 `+namelessmode0aF`。


![samourai paynym](assets/notext/6.webp)

如果您的合作者正在使用 Sparrow Wallet，他們應該點擊 「工具 」標籤，然後點擊 「顯示 PayNym」。

**Following your collaborator's PayNym from Samourai Wallet:**


如果您使用的是 Samourai Wallet，請啟動應用程式，以相同方式進入「PayNyms」功能表。如果這是您第一次使用 PayNym，您需要取得其識別碼。


![request paynym samourai](assets/notext/8.webp)


然後按一下螢幕右下方的藍色「+」。

![add collaborator paynym](assets/notext/9.webp)

然後，您可以選擇「PASTE PAYMENT CODE」貼上合作夥伴的付款代碼，或按「SCAN QR CODE」開啟相機掃瞄他們的 QR 代碼。

![paste paynym identifier](assets/notext/10.webp)


按一下「追蹤」按鈕。

![follow paynym](assets/notext/11.webp)

按一下「YES」確認。

![confirm follow paynym](assets/notext/12.webp)

然後，軟體會提供您一個「連線」按鈕。我們的教程不需要點擊這個按鈕。只有當您打算作為 BIP47 的一部分向其他 PayNym 付款時才需要此步驟，這與我們的教程無關。

![connect paynym](assets/notext/13.webp)

一旦您的 PayNym 跟隨合作者的 PayNym，請朝相反方向重複此過程，以便合作者也能跟隨您。然後您就可以執行石牆 x2 交易。


**Following your collaborator's PayNym from Sparrow Wallet:**


如果您使用 Sparrow Wallet，請打開 Wallet，進入「顯示 PayNym」功能表。如果您是第一次使用 PayNym，您需要點擊 "Retrieve PayNym "來獲取一個識別碼。

![request paynym sparrow](assets/notext/14.webp)

然後在「尋找聯絡人」方塊中輸入合作者的 PayNym 識別碼（其暱稱「+...」或其付款代碼「PM...」），並點擊「新增聯絡人」按鈕。

![add contact paynym](assets/notext/15.webp)

軟體隨後會為您提供「連結連絡人」按鈕。我們的教程不需要點擊此按鈕。只有當您打算作為 BIP47 的一部分向指定的 PayNym 付款時才需要此步驟，這與我們的教程無關。


一旦您的 PayNym 跟隨合作者的 PayNym，請朝相反方向重複此過程，以便合作者也能跟隨您。然後您就可以執行石牆 x2 交易。

## 如何在 Samourai Wallet 上進行石牆 x2 交易？


如果您已完成之前連接 Paynyms 的步驟，您終於可以進行石牆 x2 交易了！要做到這一點，請按照我們的視頻教程 Samourai Wallet：

![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)


## 如何在 Sparrow Wallet 上進行石牆 x2 交易？


如果您已完成之前連接 Paynyms 的步驟，您終於可以進行石牆 x2 交易了！要做到這一點，請按照我們的麻雀Wallet的視頻教程：

![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)


**外部資源：**


- https://sparrowwallet.com/docs/spending-privately.html；
- https://docs.samourai.io/en/spend-tools#stonewallx2。