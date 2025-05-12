---
term: hrp (人類可讀部分)
---

HRP 代表「人類可讀部分」，是 bech32 和 bech32m (SegWit v0 和 SegWit v1) 接收位址的元件。HRP 是指 Address 中特別格式化以方便人類讀取和詮釋的部分。以 bech32 Bitcoin Address 為例：


```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```


在此 Address 中，首字母 `bc` 代表 HRP。這個前綴可以讓人快速識別出所顯示的字串是 Bitcoin Address，而不是其他東西。