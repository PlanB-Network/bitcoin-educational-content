---
term: CoinJoin
---

CoinJoin 是一種用來破解比特幣可追蹤性的技術。它依賴於具有同名特定結構的協作交易：CoinJoin 交易。CoinJoin 交易可增加外部觀察者分析交易的難度，有助於改善 Bitcoin 使用者的隱私保護。這種結構允許在單一交易中混合多種硬幣，使輸入和輸出地址之間的聯繫難以確定。


CoinJoin 的一般操作如下：希望混合存入一個金額作為交易輸入的不同使用者。這些輸入會產生相同金額的不同輸出。在交易結束時，無法確定哪個輸出是屬於哪個使用者的。技術上來說，CoinJoin 交易的輸入和輸出之間沒有任何連結。每個使用者和每個 UTXO 之間的連結是中斷的，就像每個硬幣的歷史一樣。


![](../../dictionnaire/assets/4.webp)


為了允許 CoinJoin 而不讓任何使用者隨時失去對其資金的控制，交易會先由一個協調器建立，然後傳送給每個使用者。每個人在確認交易適合自己後，在自己這邊簽名，然後將所有簽名加入交易中。如果用戶或協調者試圖透過修改 CoinJoin 交易的輸出來盜取他人的資金，則簽名將無效，交易將被節點拒絕。當參與者的輸出記錄是使用Chaum的盲簽名來避免與輸入的連結時，這稱為 "Chaumian CoinJoin"。


此機制可增加交易的機密性，而無需修改 Bitcoin 協定。CoinJoin 的特定實作，例如 Whirlpool、JoinMarket 或 Wabisabi，提供了促進參與者之間協調過程的解決方案，並提高了 CoinJoin 交易的效率。以下是 CoinJoin 交易的範例：


```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```


很難確定是誰最先在Bitcoin上提出CoinJoin的想法，也很難確定是誰有在這種情況下使用David Chaum的盲簽名的想法。通常認為是Gregory Maxwell在[2013年BitcoinTalk上的一則消息](https://bitcointalk.org/index.php?topic=279249.0)中最先討論的：

使用 Chaum 盲簽名：使用者連線並提供輸入（和變更地址），以及他們希望傳送私人硬幣的 Address 的加密 blinded 版本；伺服器簽署代幣並將其傳回。使用者以匿名方式重新連線，解除輸出地址的遮罩，並將其傳回伺服器。伺服器可以看到所有的輸出都經由它簽署，因此所有的輸出都來自有效的參與者。之後，人們重新連線並簽署。

Maxwell, G. (2013, August 22)。 *CoinJoin: Bitcoin 現實世界的隱私*.BitcoinTalk 論壇. https://bitcointalk.org/index.php?topic=279249.0


然而，Chaum簽名在混合以及硬幣接合方面都有較早的提及。[2011年6月，Duncan Townsend在BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0)上展示了一個混合器，它使用Chaum簽名的方式與現代的Chaumian Coinjoins非常相似。在同一主題中，有[hashcoin回應Duncan Townsend的訊息](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793)來改善他的混合器。這則訊息提出了最接近coinjoins的方式。在 [Alex Mizrahi 在 2012 年的訊息](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry) 中也有提到類似的系統，當時他正在為 Tenebrix 的創造者提供建議。CoinJoin」一詞本身並非由 Greg Maxwell 發明，而是來自 Peter Todd 的想法。


> ► *術語 "CoinJoin "沒有法文翻譯。一些比特幣玩家也使用 "mix"、"mixing 「或 」mixage "來指代 CoinJoin 交易。混合反而是 CoinJoin 核心使用的流程。此外，重要的是不要混淆通過 Coinjoins 進行的混合和通過在過程中佔有比特幣的中心參與者進行的混合。這與 CoinJoin 毫無關係，在 CoinJoin 中，用戶不會在過程中失去對比特幣的控制。