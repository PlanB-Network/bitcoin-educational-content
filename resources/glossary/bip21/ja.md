---
用語BIP21

---
Nils SchneiderとMatt Coralloによって書かれた提案で、Luke Dashjrによって書かれたBIP20に基づいている。BIP21は、支払いを容易にするために、受信アドレスをURI（*Uniform Resource Identifier*）でどのようにエンコードすべきかを定義している。例えば、私が "*Pandul*"というラベルの下で0.1 BTCを送るように要求するBIP21に従ったビットコインURIは次のようになります：

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

この標準化により、リンクをクリックするかQRコードをスキャンしてパラメータを開始できるようになり、ビットコイン取引のユーザーエクスペリエンスが向上した。BIP21標準は現在、ビットコインウォレットソフトウェアに広く採用されている。