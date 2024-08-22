---
term: BIP21
---

Nils SchneiderとMatt Coralloによって書かれた提案で、これはLuke Dashjrによって書かれたBIP20に基づいており、そのBIP20はNils Schneiderによって書かれた別の文書から来ています。BIP21は、支払いを容易にするためにURI（*Uniform Resource Identifier*）に受信アドレスをどのようにエンコードすべきかを定義しています。例えば、BIP21に従ったBitcoin URIで、「*Pandul*」というラベルの下で0.1 BTCを送ってもらいたい場合は、以下のようになります：

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

この標準化により、リンクをクリックしたりQRコードをスキャンしてパラメータを初期化することで、Bitcoin取引のユーザーエクスペリエンスが向上します。BIP21標準は現在、Bitcoinウォレットソフトウェアで広く採用されています。