---
term: INSCRIPTIONS
---

Ordinals Theoryの文脈では、inscriptions（インスクリプションズ）は、sats（サトシ）に任意のコンテンツを刻印し、それらをネイティブなBitcoinデジタルアーティファクトに変えるものです。インスクリプションズは、Taproot入力のスクリプト内の情報の内容をこの方法で公開するトランザクションを通じて行われます：

```text
OP_0
OP_IF
<ここにデータ>
OP_ENDIF
```

これらのデジタルアーティファクトは、NFTのように、取引や保持が可能です。