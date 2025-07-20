---
term: SCRIPTSIG
---

Bitcoin 交易中位於輸入的一個元素。`scriptSig` 提供必要的數據，以滿足正在使用資金的上一個交易的 `scriptPubKey` 所設定的條件。因此，它對 `scriptPubKey` 起著補充的作用。通常，`scriptSig` 包含數位簽章和公開金鑰。簽章是由比特幣擁有人使用他們的私人密碼匙產生的，並證明他們有權花費 UTXO。在這種情況下，`scriptSig` 證明了輸入的持有者擁有與前一個輸出交易的`scriptPubKey` 中指定的 Address 相關的公開密鑰相對應的私人密鑰。


當交易被驗證時，來自「scriptSig」的資料會在相應的「scriptPubKey」中執行。如果結果有效，表示已符合花費資金的條件。如果交易的所有輸入都提供了能驗證其 `scriptPubKey` 的 `scriptSig`，則表示交易有效，可以加入區塊執行。


例如，這裡有一個經典的 P2PKH `scriptSig`：


```text
<signature> <public key>
```


相應的 `scriptPubKey` 應該是：


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


![](../../dictionnaire/assets/35.webp)


> ► *`scriptSig`有時在英文中也稱為「解鎖腳本」。