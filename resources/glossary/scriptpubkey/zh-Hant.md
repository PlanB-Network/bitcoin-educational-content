---
term: SCRIPTPUBKEY
---

位於 Bitcoin 交易輸出部分的腳本，定義了相關 UTXO 可以被花費的條件。這個腳本因此可以確保比特幣的安全。在其最常見的形式中，`scriptPubKey` 包含一個條件，要求下一個交易提供與指定的 Bitcoin Address 對應的私鑰的擁有證明。這通常是透過腳本來達成，腳本要求與用來保護這些資金的 Address 相關的公開金鑰相對應的簽章。當交易嘗試使用這個 UTXO 作為輸入時，它必須提供一個 `scriptSig`，這個 `scriptSig` 與 `scriptPubKey` 結合後，就會符合設定的條件，並產生一個有效的腳本。


例如，這裡有一個經典的 P2PKH `scriptPubKey`：


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


相應的 `scriptSig` 應該是：


```text
<signature> <public key>
```


![](../../dictionnaire/assets/35.webp)


> ► *此腳本有時在英文中也被稱為「鎖定腳本」*。