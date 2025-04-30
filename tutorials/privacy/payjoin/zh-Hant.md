---
name: PayJoin
description: 什麼是 Bitcoin 上的 PayJoin？
---
![Payjoin thumbnail - steganography](assets/cover.webp)


*** 注意：** Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押後，Samourai Wallet 上的 Payjoins Stowaway 只能透過手動交換 PSBT 的方式運作，前提是雙方使用者都連線到自己的 Dojo。至於 Sparrow，透過 BIP78 進行的 Payjoins 仍然有效。不過，這些工具有可能在未來幾週內重新推出。在此期間，您仍可閱讀這篇文章，瞭解 payjoins.* 的理論功能。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---
## 瞭解 PayJoin 在 Bitcoin 上的交易


PayJoin 是 Bitcoin 交易的特定結構，透過與付款收款人協同合作，在付款過程中增強使用者隱私。


2015 年，[LaurentMT](https://twitter.com/LaurentMT) 在一份可存取 [here](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt) 的文件中首次提到此方法為「隱藏交易」。此技術後來被 Samourai Wallet 採用，並在 2018 年成為第一個使用 Stowaway 工具實現此技術的用戶端。PayJoin 的概念也見於 [BIP79](https://github.com/Bitcoin/bips/blob/master/bip-0079.mediawiki) 和 [BIP78](https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki)。有幾個詞語用來指 PayJoin：


- PayJoin
- 偷渡
- P2EP（付費到終點）
- 隱匿式交易


PayJoin 的獨特之處在於它能夠 generate 一種乍看之下很普通的交易，但實際上是雙方之間的迷你 CoinJoin。為了達到這個目的，交易結構讓收款人與實際寄款人一起參與輸入。收款人在交易中間包含了對自己的付款，這使得他們可以獲得付款。


讓我們舉一個具體的例子：如果您用`10,000 Sats`的 UTXO 買了一根`4000 Sats`的法棍，並選擇了 PayJoin，您的麵包師傅會在您的`4000 Sats`之外，加上屬於他們的`15,000 Sats`的 UTXO 作為輸入，他們會全額收到作為輸出：

![Payjoin transaction diagram](assets/en/1.webp)


在這個例子中，麵包師傅以 `15,000 Sats` 作為輸入，最後以 `19,000 Sats` 作為輸出，差額正好是 `4000 Sats`，也就是法棍的價格。在您這邊，您輸入 `10,000 Sats`，最後輸出 `6,000 Sats`，餘額為 `-4000 Sats`，也就是法棍的價格。為了簡化範例，我故意省略此交易中的 Mining 費用。


## PayJoin 交易的目的是什麼？


PayJoin 交易有兩個目的，可讓使用者提高付款的隱私性。

首先，PayJoin 旨在透過在連鎖分析中製造誘餌來誤導外部觀察者。這是透過共同輸入 Ownership 啟發式 (CIOH) 來實現的。通常，當 Blockchain 上的交易有多個輸入時，我們會假設所有這些輸入都可能屬於同一個實體或使用者。因此，當分析師檢查 PayJoin 交易時，他們會相信所有的輸入都來自同一個人。然而，這種想法是不正確的，因為收款人也會與實際付款人一起提供輸入。因此，連鎖分析會轉向錯誤的詮釋。


此外，PayJoin 也可以欺騙外部觀察者，讓他們不知道實際的付款金額。透過檢查交易結構，分析師可能會相信付款金額等同於其中一個輸出的金額。然而，實際上，付款金額並不等同於任何一項輸出。它實際上是收款人的輸出 UTXO 與收款人的輸入 UTXO 之間的差額。在這個意義上，PayJoin 交易屬於隱藏術的範疇。它允許在作為誘餌的偽造交易中隱藏交易的實際金額。


請注意我們對**速記**的定義：

> 隱含技術（Steganography）是一種將資訊隱藏在其他資料或物件中，使人無法察覺隱藏資訊存在的技術。例如，可以將秘密訊息隱藏在與文字無關的點中，使肉眼無法察覺（這就是微點技術）。加密技術會使資訊在沒有解密鑰匙的情況下無法被理解，而隱匿技術則不同，它不會修改資訊。它仍然顯示在眾目睽睽之下。它的目的是隱藏秘密訊息的存在，而加密則明顯揭示了隱藏資訊的存在，儘管沒有密鑰是無法獲取的。

讓我們回到支付法棍的 PayJoin 交易範例。

![Payjoin transaction schema from the outside](assets/en/2.webp)

看到 Blockchain 上的這筆交易，外部觀察者如果遵循鏈分析的一般啟發式方法，會將其解讀為： 「*Alice 合併了 2 個 UTXO 作為交易的輸入，支付給 Bob `19,000 Sats`*」 ：「*Alice合併了2個UTXO作為交易的輸入，以支付`19,000 Sats`給Bob*」。

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

這種解釋顯然是不正確的，因為您已經知道，這兩筆輸入的 UTXO 並不屬於同一人。此外，付款的實際價值不是`19,000 Sats`，而是`4,000 Sats`。外部觀察者的分析因此指向錯誤的結論，確保利益相關者的機密性。![PayJoin 交易圖](assets/en/1.webp)

如果您想分析真正的 PayJoin 交易，以下是我在 Testnet 上執行的交易：[8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://Mempool.space/fr/Testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)


[**-> 探索我們如何用 Samourai Wallet 製作 PayJoin 的教學**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-samourai-Wallet-48a5c711-ee3d-44db-b812-c55913080eab)


[**-> 探索我們如何使用 Sparrow Wallet 製作 PayJoin 的教學**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-sparrow-Wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)



**外部資源：**


- https://docs.samourai.io/en/spend-tools#stowaway；
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki。