---
term: 嘆息_anyprevout
---

在 Bitcoin 中實作新 SigHash Flag 修改器的提案，與 BIP118 一同推出。`SIGHASH_ANYPREVOUT` 可讓交易管理更具彈性，特別是對於 Lightning Network 上的付款通道和 Eltoo 更新等進階應用。`SIGHASH_ANYPREVOUT` 使簽章不與任何特定的先前 UTXO (*Any Previous Output*) 綁定。與 `SIGHASH_ALL`結合使用，可以簽署交易的所有輸出，但不簽署任何輸入。只要符合特定的條件，就可以在不同的交易中重複使用簽章。


> ► *此 SigHash 修改器 SIGHASH_ANYPREVOUT 源自 Joseph Poon 最初於 2016 年提出的 SIGHASH_NOINPUT 概念，以強化其 Lightning Network.* 的概念。