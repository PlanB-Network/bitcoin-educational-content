---
用語SCRIPTSIG

---
インプットに位置するビットコイン取引の要素。scriptSig`は、資金が使用される前のトランザクションの `scriptPubKey` によって設定された条件を満たすために必要なデータを提供する。したがって、 `scriptSig` は `scriptPubKey` を補完する役割を果たす。通常、`scriptSig`はデジタル署名と公開鍵を含む。署名はビットコインの所有者が秘密鍵を使用して生成し、UTXOを使用する権限を持っていることを証明する。この場合、`scriptSig`は、入力の所有者が、前の送信トランザクションの `scriptPubKey` で指定されたアドレスに関連付けられた公開鍵に対応する秘密鍵を持っていることを示す。

トランザクションが検証されると、 `scriptSig` のデータが対応する `scriptPubKey` で実行される。結果が有効であれば、資金を使うための条件が満たされたことを意味する。トランザクションのすべての入力が `scriptPubKey` を検証する `scriptSig` を提供する場合、トランザクションは有効であり、実行のためにブロックに追加することができる。

例えば、これは古典的なP2PKHの `scriptSig` である：

```text
<signature> <public key>
```

対応する `scriptPubKey` は次のようになる：

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> scriptSig`は英語では "unlocking script "と呼ばれることもある。