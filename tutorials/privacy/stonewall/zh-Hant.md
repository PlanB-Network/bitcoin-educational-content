---
name: Stonewall
description: 瞭解並使用石牆交易
---
![cover stonewall](assets/cover.webp)


**繼 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被查封之後，使用 Samourai Wallet 應用程式現在需要連線到您自己的道場才能正常運作。除此之外，石牆交易完全不受影響，仍然可以順利進行。事實上，這些類型的交易是自主進行的，不需要外部協作或透過 Soroban.** 連線。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> **打破 Blockchain 分析的假設，在交易的寄件者和收件者之間提出數學上可證明的疑問。**

## 什麼是石牆交易？

Stonewall 是一種特殊形式的 Bitcoin 交易，目的在於透過模仿雙方之間的 CoinJoin 來增加交易過程中的使用者隱私，但實際上並不是 CoinJoin。事實上，這種交易不是協作性的。使用者可以單獨構建它，只涉及自己的 UTXO 作為輸入。因此，您可以在任何場合建立石牆交易，而不需要與其他使用者協調。


石牆交易的操作如下：作為輸入，寄件者使用 2 個屬於他們的 UTXO。作為輸出，交易會產生 4 個輸出，其中 2 個會是完全相同的金額。另外 2 個則是變更。在 2 個相同金額的輸出中，只有一個會實際送到收款人手中。


石牆交易中只有 2 個角色：


- 寄件者，實際付款者；
- 收款人可能不知道交易的具體性質，只是期望從寄件人處收到付款。


讓我們舉一個例子來了解這個交易結構。Alice 去麵包店買她的法棍，花了 `4,000 Sats`。她想用比特币支付，同时保持一定的支付隐私。因此，她決定創建一個石牆交易來支付。

![transaction stonewall bakery](assets/en/1.webp)

分析這筆交易，我們可以看到麵包師傅確實收到了 `4,000 Sats` 作為長棍麵包的付款。Alice 使用 2 個 UTXO 作為輸入：一個是 `10,000 Sats` ，另一個是 `15,000 Sats`。作為輸出，她收到 3 個 UTXO：一個是 `4,000 Sats`，一個是 `6,000 Sats`，一個是 `11,000 Sats`。Alice在這次交易中的淨餘額為`-4,000 Sats`，相當於長棍麵包的價格。


在這個範例中，我故意省略 Mining 的費用，以方便理解。實際上，交易費用完全由寄件人負擔。


## 石牆與石牆 x2 有何不同？

石牆交易的運作方式與石牆X2交易相同，唯一的差異是後者需要合作，與經典的石牆交易不同，因此有「X2」的稱號。事實上，Stonewall 交易無需外部合作即可執行：發送人無需他人協助即可執行。但是，在石牆 x2 交易中，有一個被稱為 「合作者 」的額外參與者加入了交易過程。合作者將自己的比特幣與寄件者的比特幣一起作為輸入，並將全部金額作為輸出（扣除 Mining 費用）。


我們再來看看 Alice 在麵包店的例子。如果她想要進行石牆 x2 交易，Alice 在建立交易時就必須與 Bob（第三方）合作。他們各自提供一個輸入 UTXO。然後，鮑勃就會收到全額的輸入作為輸出。麵包師傅會以與石牆交易相同的方式收到長棍的付款，而 Alice 則會收到減去長棍成本後的初始餘額。

![transaction stonewall x2](assets/en/2.webp)


從外部的角度來看，交易的模式會完全維持不變。

![Stonewall or Stonewall x2 ?](assets/en/3.webp)


總而言之，石牆交易和石牆 x2 交易具有相同的結構。兩者的區別在於其合作性。Stonewall 交易是單獨開發的，不需要合作。相反，石牆 x2 交易則依賴兩個人的合作來實施。


[**-> 進一步瞭解石牆 x2 交易**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)


## 石牆交易的目的是什麼？

石牆結構為交易增加了大量的熵，模糊了鏈式分析。從外部的角度來看，這樣的交易可以解釋為兩個人之間的小 CoinJoin。但實際上，就像石牆 x2 交易一樣，它是一種付款。因此，這種方法會造成連鎖分析的不確定性，甚至可能導致錯誤的線索。


讓我們重溫 Alice 在麵包店的例子。Blockchain 上的交易如下：

![Stonewall or Stonewall x2 ?](assets/en/4.webp)

外部觀察者依賴一般的連鎖分析啟發法，可能會錯誤地得出「*兩個人執行了一個小型的 CoinJoin，每個人有一個 UTXO 作為輸入，每個人有兩個 UTXO 作為輸出*」的結論。

![Stonewall or Stonewall x2 ?](assets/en/5.webp)

這個解釋是不對的，因為大家都知道，有一個 UTXO 傳送給麵包師，輸入中的 2 個 UTXO 來自 Alice，而她收到 3 個變更輸出。


![transaction stonewall baker](assets/en/1.webp)

即使外部觀察者能夠識別石牆交易的模式，他們也不會掌握所有資訊。他們無法確定兩筆金額相同的 UTXOs 中，哪一筆與付款相符。此外，他們也無法確定輸入的兩個 UTXO 是否來自兩個不同的人，或是屬於一個將它們合併的人。最後一點是由於我們上面談到的石牆 x2 交易與石牆交易的模式完全相同。從外面看，如果沒有關於背景的額外資訊，我們不可能區分石牆交易和石牆 x2 交易。然而，前者不是合作交易，而後者則是。這就更增加了這項支出的疑點。

![Stonewall or Stonewall x2 ?](assets/en/3.webp)

## 如何在 Samourai Wallet 上進行石牆交易？

與Stowaway或Stonewall x2 (cahoots)交易不同，Stonewall交易不需要使用Paynyms。它可以直接完成，不需要任何準備步驟。要做到這一點，請按照我們的視頻教程 Samourai Wallet：

![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)


## 如何在 Sparrow Wallet 上進行石牆交易？

與Stowaway或Stonewall x2 (cahoots)交易不同，Stonewall交易不需要使用Paynyms。它可以直接完成，不需要任何準備步驟。要做到這一點，請按照我們的麻雀Wallet的視頻教程：

![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)



**外部資源：**


- https://docs.samourai.io/en/spend-tools#stonewall。