---
term: 方針
---

一種以使用者為導向的高階語言，允許在 Miniscript 的框架內簡單指定 UTXO 解鎖的條件。政策是消費規則的抽象描述。然後可以編譯成 miniscript，與 Bitcoin 原生腳本語言的操作一一對應。


![](../../dictionnaire/assets/30.webp)


政策語言與 miniscript 語言略有不同。例如，假設一個安全系統的主要路徑是金鑰 A，復原路徑是金鑰 B，但時間鎖是一年（約 52,560 個區塊）。在政策中，這將是


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


一旦編譯成 miniscript，它就會是：


```plaintext
andor(pk(B),older(52560),pk(A))
```


而一旦轉換成原生腳本，就會是這樣：


```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```