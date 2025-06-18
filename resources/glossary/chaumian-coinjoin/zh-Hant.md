---
term: CHAUMIAN CoinJoin
---

一個 CoinJoin 協定，利用 David Chaum 的盲簽名和 Tor 來進行參與者與協調者伺服器之間的通訊。Chaumian CoinJoin 的目標是確保參與者知道協調者無法竊取比特幣，也無法將輸入和輸出連結在一起。


為了達到這個目的，使用者將他們的輸入和一個加密的 blinded 接收 Address 提交給協調者。這個 Address 一旦 unblinded，目的是接收比特幣作為 CoinJoin 的輸出。協調者會簽署這些代幣，並將它們交還給使用者。之後，使用者以新的 Tor 身份匿名重新連線到協調者的伺服器，並以明文揭露他們的輸出地址，以便交易建構。協調者可以驗證所有這些接收地址都來自合法的使用者，因為他之前已經用自己的私人金鑰簽署了他們的 blinded 版本。但是，他無法將特定的輸出 Address 與特定的輸入使用者聯繫起來。因此，即使從協調者的角度來看，輸入和輸出之間也沒有任何連結。一旦交易由協調者建構完成，他就會將交易傳回給參與者，參與者在確認他們的輸出確實在此交易中之後，簽署此交易以解鎖他們的輸入。參與者將簽名傳送給協調員。一旦收集到所有簽名，協調者就可以在 Bitcoin 網路上廣播 CoinJoin 交易。


![](../../dictionnaire/assets/38.webp)


此方法可確保協調人在整個 CoinJoin 過程中，既不會危及參與者的匿名性，也不會竊取比特幣。


很難確定是誰最先在Bitcoin上提出CoinJoin的想法，也很難確定是誰有在此背景下使用David Chaum的盲簽名的想法。通常認為是Gregory Maxwell在[2013年BitcoinTalk上的一則消息](https://bitcointalk.org/index.php?topic=279249.0)中最先討論的：


> *"通過使用Chaum盲簽名：使用者連線並提供輸入（並變更地址），以及他們希望將私人硬幣傳送至的加密 blinded 版本的 Address；伺服器簽署代幣並將其傳回。使用者以匿名方式重新連線，解除輸出位址的遮罩，並將其傳回伺服器。伺服器可以看到所有的輸出都經由他簽署，因此，所有的輸出都來自有效的參與者。之後，人們再重新連線並簽名。

Maxwell, G. (2013, August 22)。 *CoinJoin: Bitcoin 現實世界的隱私*.BitcoinTalk 論壇. https://bitcointalk.org/index.php?topic=279249.0

然而，還有其他更早的提法，包括Chaum's signatures在混合背景下的使用，以及coinjoins的使用。[2011年6月，Duncan Townsend在BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0)上展示了一個混合器，它使用Chaum簽名的方式與現代的Chaumian Coinjoins非常相似。在同一主題中，有[hashcoin回應Duncan Townsend的訊息](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793)來改善他的混合器。這則訊息正好提出了最接近coinjoins的方式。在 [Alex Mizrahi 在 2012 年的訊息](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry) 中也有提到類似的系統，當時他正在為 Tenebrix 的創造者提供建議。CoinJoin」這個名詞本身應該不是 Greg Maxwell 發明的，而是來自 Peter Todd 的想法。