---
term: SCRIPTSIG

---
Um elemento em uma transação Bitcoin localizado nas entradas. O `scriptSig` fornece os dados necessários para satisfazer as condições estabelecidas pelo `scriptPubKey` da transação anterior a partir da qual os fundos estão sendo gastos. Assim, ele desempenha um papel complementar ao `scriptPubKey`. Normalmente, o `scriptSig` contém uma assinatura digital e uma chave pública. A assinatura é gerada pelo proprietário dos bitcoins usando sua chave privada e prova que ele tem autorização para gastar o UTXO. Neste caso, o `scriptSig` demonstra que o detentor do input possui a chave privada correspondente à chave pública associada ao endereço especificado no `scriptPubKey` da transação de saída anterior.

Quando a transação é verificada, os dados do `scriptSig` são executados no `scriptPubKey` correspondente. Se o resultado for válido, significa que as condições para gastar os fundos foram cumpridas. Se todas as entradas da transação fornecerem um `scriptSig` que valide o seu `scriptPubKey`, a transação é válida e pode ser adicionada a um bloco para execução.

Por exemplo, aqui está um `scriptSig` clássico de P2PKH:

```text
<signature> <public key>
```

A `scriptPubKey` correspondente seria:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *O `scriptSig` também é por vezes designado por "unlocking script" em inglês.*