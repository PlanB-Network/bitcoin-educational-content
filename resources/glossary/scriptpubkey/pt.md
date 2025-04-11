---
term: SCRIPTPUBKEY

---
Um script localizado na parte de saída de uma transação Bitcoin que define as condições em que o UTXO associado pode ser gasto. Este script, portanto, protege os bitcoins. Em sua forma mais comum, o `scriptPubKey` contém uma condição que exige que a próxima transação forneça prova de posse da chave privada correspondente a um endereço Bitcoin especificado. Isso geralmente é alcançado por um script que exige uma assinatura correspondente à chave pública associada ao endereço usado para proteger esses fundos. Quando uma transação tenta utilizar este UTXO como entrada, deve fornecer um `scriptSig` que, uma vez combinado com o `scriptPubKey`, satisfaz as condições estabelecidas e produz um script válido.

Por exemplo, aqui está um `scriptPubKey` clássico de P2PKH:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

O `scriptSig` correspondente seria:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *Este script também é por vezes referido como "locking script" em inglês.*