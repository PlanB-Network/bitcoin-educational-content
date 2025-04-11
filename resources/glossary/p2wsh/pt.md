---
term: P2WSH

---
P2WSH significa *Pay to Witness Script Hash*. É um modelo de script padrão usado para estabelecer condições de gastos em um UTXO. O P2WSH foi introduzido com a implementação do SegWit em agosto de 2017.

Este script é semelhante ao P2SH (*Pay to Public Script Hash*), uma vez que também bloqueia bitcoins com base no hash de um script. A diferença reside na forma como as assinaturas e os scripts são incluídos na transação. Para gastar os bitcoins neste tipo de script, o destinatário deve fornecer o script original, chamado `witnessScript` (equivalente a `redeemScript`), juntamente com as assinaturas necessárias. Esse mecanismo permite a implementação de condições de gasto mais sofisticadas, como multisigs.

No contexto do P2WSH, a informação do script de assinatura (o `scriptWitness`, equivalente ao `scriptSig`) é movida da estrutura tradicional da transação para uma secção separada chamada `Witness`. Esta mudança é uma caraterística da atualização SegWit (*Segregated Witness*) que ajuda a prevenir a maleabilidade da assinatura. As transacções P2WSH são geralmente menos dispendiosas em termos de taxas em comparação com as transacções Legacy, uma vez que a parte da testemunha custa menos.

Os endereços P2WSH são escritos usando a codificação `Bech32` com uma soma de controlo na forma de código BCH. Estes endereços começam sempre com `bc1q`. P2WSH é uma saída SegWit versão 0.