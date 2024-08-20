---
termo: SCRIPTSIG
---

Um elemento em uma transação Bitcoin localizado nas entradas. O `scriptSig` fornece os dados necessários para satisfazer as condições estabelecidas pelo `scriptPubKey` da transação anterior da qual os fundos estão sendo gastos. Assim, desempenha um papel complementar ao `scriptPubKey`. Tipicamente, o `scriptSig` contém uma assinatura digital e uma chave pública. A assinatura é gerada pelo proprietário dos bitcoins usando sua chave privada e prova que eles têm a autorização para gastar o UTXO. Neste caso, o `scriptSig` demonstra que o detentor da entrada possui a chave privada correspondente à chave pública associada ao endereço especificado no `scriptPubKey` da transação de saída anterior.

Quando a transação é verificada, os dados do `scriptSig` são executados no correspondente `scriptPubKey`. Se o resultado for válido, significa que as condições para gastar os fundos foram atendidas. Se todas as entradas da transação fornecerem um `scriptSig` que valida seu `scriptPubKey`, a transação é válida e pode ser adicionada a um bloco para execução.

Por exemplo, aqui está um clássico P2PKH `scriptSig`:

```text
<assinatura> <chave pública>
```

O `scriptPubKey` correspondente seria:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <endereço> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *O `scriptSig` também é às vezes chamado de "script de desbloqueio" em inglês.*