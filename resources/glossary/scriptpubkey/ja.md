---
term: SCRIPTPUBKEY
---

Bitcoin取引の出力部分に位置するスクリプトで、関連するUTXOが使用される条件を定義します。このスクリプトによってビットコインが保護されます。最も一般的な形式では、`scriptPubKey`には、指定されたBitcoinアドレスに対応する秘密鍵の所持の証明を次の取引が提供することを要求する条件が含まれています。これは通常、これらの資金を保護するために使用されたアドレスに関連付けられた公開鍵に対応する署名を要求するスクリプトによって達成されます。取引がこのUTXOを入力として使用しようとするとき、設定された条件を満たし有効なスクリプトを生成するために、`scriptPubKey`と組み合わせられる`scriptSig`を提供する必要があります。

例えば、こちらが典型的なP2PKH `scriptPubKey`です：

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

対応する`scriptSig`は以下のようになります：

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.png)

> ► *このスクリプトは英語では時々「ロッキングスクリプト」とも呼ばれます。*