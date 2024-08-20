---
term: SCRIPTPUBKEY
---

Um script localizado na parte de saída de uma transação Bitcoin que define as condições sob as quais o UTXO associado pode ser gasto. Este script, portanto, protege os bitcoins. Na sua forma mais comum, o `scriptPubKey` contém uma condição que exige que a próxima transação forneça prova de posse da chave privada correspondente a um endereço Bitcoin especificado. Isso é frequentemente alcançado por um script que exige uma assinatura correspondente à chave pública associada ao endereço usado para proteger esses fundos. Quando uma transação tenta usar este UTXO como entrada, ela deve fornecer um `scriptSig` que, uma vez combinado com o `scriptPubKey`, atende às condições estabelecidas e produz um script válido.

Por exemplo, aqui está um clássico P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <endereço> OP_EQUALVERIFY OP_CHECKSIG
```

O `scriptSig` correspondente seria:

```text
<assinatura> <chave pública>
```

![](../../dictionnaire/assets/35.png)

> ► *Este script também é às vezes referido como "script de bloqueio" em inglês.*