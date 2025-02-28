---
term: hrp
---
HRPは「Human Readable Part」の略で、bech32およびbech32m（SegWit v0およびSegWit v1）の受信アドレスの構成要素である。HRPとは、アドレスのうち、人間が読みやすく解釈しやすいように特別にフォーマットされた部分を指す。例えば、bech32 ビットコインアドレスを例にとってみよう：

```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```

このアドレスでは、最初の `bc` が HRP を表す。この接頭辞により、提示された文字列がビットコインアドレスであり、それ以外のものでないことをすぐに識別できる。