---
用語SCRIPTPUBKEY

---
ビットコイン取引の出力部分にあるスクリプトで、関連するUTXOを使用できる条件を定義する。このスクリプトはビットコインを保護する。最も一般的な形式では、`scriptPubKey`は、次のトランザクションが指定されたビットコインアドレスに対応する秘密鍵を所有していることの証明を提供することを要求する条件を含む。これは、資金を確保するために使用されるアドレスに関連する公開鍵に対応する署名を要求するスクリプトによって達成されることが多い。トランザクションがこのUTXOを入力として使用しようとする場合、そのトランザクショ ンは`scriptSig`を提供しなければならず、それがいったん`scriptPubKey` と組み合わされると、設定された条件を満たし、有効なスクリプトを生成する。

例えば、これは古典的なP2PKHの `scriptPubKey` である：

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

対応する`scriptSig`は次のようになる：

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> 英語では "locking script "と呼ばれることもある。