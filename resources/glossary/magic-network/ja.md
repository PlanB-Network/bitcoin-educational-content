---
term: MAGIC NETWORK
---

Bitcoinプロトコルで使用される定数で、ノード間で交換されるメッセージの特定のネットワーク（mainnet、testnet、regtest...）を識別するために使われます。これらの値は、データストリーム内での識別を容易にするために、各メッセージの始まりに記載されています。Magic Networkは、通常の通信データにはめったに存在しないように設計されています。実際、これら4バイトはASCIIでは稀で、UTF-8では無効であり、データストレージ形式に関係なく非常に大きな32ビット整数を生成します。Magic Networkは（リトルエンディアン形式で）以下の通りです：
* Mainnet:

```text
f9beb4d9
```

* Testnet:

```text
0b110907
```

* Regtest:

```text
fabfb5da
```

> ► *これらの4バイトは、時に「Magic Number」、「Magic Bytes」、または「Start String」とも呼ばれます。*