---
term: BIP0049
---

BIP49 是一個資訊性 BIP，介紹在 HD Wallet 中用於 generate Nested SegWit 位址的衍生方法。建議的衍生路徑遵循 BIP43 和 BIP44 的標準，在目標深度處加上索引 `49'`（硬化衍生）。例如，P2SH-P2WPKH 帳號的第一個 Address 將從路徑中衍生：`m/49'/0'/0'/0/0`.嵌套 SegWit 腳本是在 SegWit 推出時為了方便採用而發明的。它們允許使用這個新的標準，甚至在尚未與 SegWit 原生相容的錢包上。