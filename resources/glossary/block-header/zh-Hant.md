---
term: 擋板蓋
---

區塊標頭是一種資料結構，是構建 Bitcoin 區塊的主要元件。每個區塊由標頭和交易清單組成。區塊標頭包含確保區塊在 Blockchain 中完整性和有效性的關鍵資訊。區塊標頭包含 80 位元組的元資料，並由下列 Elements：


- 塊版本；
- 上一區塊的 Hash；
- 交易的 Merkle Tree 根；
- 區塊 Timestamp；
- 難度目標；
- Nonce.


例如，以下是 2023 年 4 月 15 日由 Foundry USA 開採的十六進位格式的區塊編號 785,530 的標頭：


```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```


如果我們細分這個標頭，就能認清：


- 版本：


```text
00e0ff3f
```



- 之前的 Hash：


```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```



- Merkle Root：


```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```



- Timestamp：


```text
bcb13a64
```



- 目標：


```text
b2e00517
```



- Nonce：


```text
43f09a40
```


若要有效，區塊的標頭必須在使用 `SHA256d` 散列後，產生小於或等於目標難度的 Hash。


> ► *在英文中，它被稱為「Block Header」。