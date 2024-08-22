---
term: SCRIPTSIG
---

Bitcoin取引の入力部分に位置する要素。`scriptSig`は、資金が使われる前の取引の`scriptPubKey`によって設定された条件を満たすために必要なデータを提供します。したがって、`scriptPubKey`に補完的な役割を果たします。通常、`scriptSig`にはデジタル署名と公開鍵が含まれています。この署名は、ビットコインの所有者が自分の秘密鍵を使用して生成し、UTXOを使用する権限があることを証明します。この場合、`scriptSig`は入力の保持者が、前の送金取引の`scriptPubKey`で指定されたアドレスに関連付けられた公開鍵に対応する秘密鍵を持っていることを示します。

取引が検証されると、`scriptSig`からのデータは対応する`scriptPubKey`で実行されます。結果が有効であれば、資金を使用する条件が満たされたことを意味します。取引のすべての入力がそれぞれの`scriptPubKey`を検証する`scriptSig`を提供する場合、取引は有効とみなされ、実行のためにブロックに追加することができます。

例えば、こちらが典型的なP2PKH `scriptSig`です：

```text
<signature> <public key>
```

対応する`scriptPubKey`は以下のようになります：

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *`scriptSig`は英語では時々「unlocking script」とも呼ばれます。*