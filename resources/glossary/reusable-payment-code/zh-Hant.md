---
term: 可重複使用的付款代碼
---

在 BIP47 中，可重複使用的付款代碼是由 Bitcoin Wallet 產生的靜態識別碼，可進行通知交易並衍生出獨特的地址。這避免了地址的重複使用而導致隱私權的損失，而無需為每次付款手動推導和傳輸新的、未使用的地址。在 BIP47 中，可重複使用的付款代碼建構如下：


- 位元組 0 對應版本；
- 位元組 1 是位元欄位，用於在特定使用情況下加入資訊；
- 位元組 2 表示公開金鑰中 `y` 的奇偶校驗；
- 從位元組 3 到位元組 34，您可以找到公開金鑰的 `x` 值；
- 從位元組 35 到位元組 66，是與公開金鑰相關的鏈碼；
- 從位元組 67 到位元組 79，有零填充。


人可讀部分 (Human-Readable Part, HRP) 通常會加在付款代碼的開頭，而校驗和則會加在付款代碼的結尾，然後再以 base58 編碼。因此，付款代碼的結構與擴充金鑰的結構相當類似。以下是我自己的 BIP47 付款代碼，以 base58 為例：


```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```


在 BIP47 的 PayNym 實作中，付款代碼也可以用與機器人圖像相關的識別碼形式來表示。下面是我的例子：


```text
+throbbingpond8B1
```


使用 PayNym 實作的付款代碼目前可在個人電腦上的 Sparrow Wallet 和行動裝置上的 Samourai Wallet 上使用。