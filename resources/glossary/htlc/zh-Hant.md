---
term: HTLC
---

代表 "*Hashed Timelock Contract*"。這是主要用於 Lightning 的 Smart contract 機制。有時也會出現在原子交換中。基本上，HTLC 使金錢轉移以揭露一個秘密為條件，也包含一個時間條件，以在交易失敗時保護寄件者的金錢。


在 Lightning 上，HTLC 允許您通過多個通道將比特幣發送至與您沒有直接通道的節點，沿途不需要信任。每個節點之間的付款條件是提供預先映像（散列後與協定值對應的密碼）。如果最終收款人提供此預先映像，它就可以領取資金，而且必然會使每個中間節點都能逐級領取資金。


舉例來說，如果 Alice 想要寄 1 BTC 給 David，但與 David 沒有直接的管道，她必須透過 Bob 和 Carol，因為他們彼此之間有付款管道。以下是交易的運作方式：




- 大衛給愛麗絲一個 Invoice 閃電。其中包含只有大衛知道的秘密 $s$（前影像）的 Hash $h$。所以我們有$h = \text{Hash}(s)$ ；
- Alice 與 Bob 創建了一個 HTLC，Bob 提出向她發送 1 BTC，條件是 Bob 向她提供與 Hash $h$ 對應的秘密 $s$（前圖像）；
- Bob 與 Carol 建立了一個 HTLC，Carol 提出向他發送 1 BTC，條件是她提供相同的秘密 $s$ ；
- Carol 與 David 建立了一個 HTLC，如果他揭示 $s$ 前圖像，David 會再提供 1 BTC；
- David向Carol透露$s$ (只有他知道)以獲得1 BTC。Carol現在可以使用$s$從Bob處獲得BTC。而現在知道 $s$ 的 Bob 也對 Alice 做同樣的事情。


最後，Alice 透過 Bob 和 Carol 傳送了 1 BTC 給 David (對後者來說是中性的動作)，任何人都不需要信任對方，因為一切都由 HTLC 的條件串聯保障。


HTLC 因此可以實現所謂的「原子式」交換：轉帳不是完全成功，就是失敗，資金會被退回。這就保證了交易的安全性，即使是在不需要信任的多個參與者之間。