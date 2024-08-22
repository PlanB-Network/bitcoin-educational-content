---
term: HRP (HUMAN READABLE PART)
---

HRPは、「Human Readable Part」（人間が読みやすい部分）を意味し、bech32およびbech32m（SegWit v0およびSegWit v1）の受信アドレスのコンポーネントです。HRPは、人間が容易に読み取り、解釈できるように特別にフォーマットされたアドレスの部分を指します。例えば、bech32ビットコインアドレスを見てみましょう：

```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```

このアドレスにおいて、最初の`bc`がHRPを表しています。この接頭辞により、提示された文字列がビットコインアドレスであることを迅速に識別でき、それ以外のものではないことがわかります。