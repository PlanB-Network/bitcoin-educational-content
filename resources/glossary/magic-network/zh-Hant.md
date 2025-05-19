---
term: MAGIC NETWORK
---

Bitcoin 協定中用於識別節點間交換訊息的特定網路 (Mainnet、Testnet、regtest...) 的常量。這些值刻在每個訊息的開頭，以方便在資料流中識別。Magic Networks 被設計成很少出現在一般通訊資料中。事實上，這 4 個位元組在 ASCII 中並不常見，在 UTF-8 中也無效，而且無論資料儲存格式為何，generate 都是一個非常大的 32 位元整數。Magic Networks 是 (以 little-endian 格式表示)：


- Mainnet：


```text
f9beb4d9
```



- Testnet：


```text
0b110907
```



- Regtest：


```text
fabfb5da
```


> ► *這 4 個位元組有時也稱為「神奇數字」、「神奇位元組」或「起始字串」*。