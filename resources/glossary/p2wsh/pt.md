---
term: P2WSH
---

P2WSH significa *Pay to Witness Script Hash* (Pagamento para Testemunha de Hash de Script). É um modelo de script padrão usado para estabelecer condições de gasto em um UTXO. O P2WSH foi introduzido com a implementação do SegWit em agosto de 2017.

Este script é semelhante ao P2SH (*Pay to Public Script Hash*), pois também bloqueia bitcoins com base no hash de um script. A diferença está em como assinaturas e scripts são incluídos na transação. Para gastar os bitcoins neste tipo de script, o destinatário deve fornecer o script original, chamado `witnessScript` (equivalente a `redeemScript`), junto com as assinaturas necessárias. Esse mecanismo permite a implementação de condições de gasto mais sofisticadas, como multisigs.

No contexto do P2WSH, as informações do script de assinatura (o `scriptWitness`, equivalente a `scriptSig`) são movidas da estrutura tradicional da transação para uma seção separada chamada `Witness`. Essa mudança é uma característica da atualização SegWit (*Segregated Witness*) que ajuda a prevenir a maleabilidade de assinaturas. Transações P2WSH geralmente são menos caras em termos de taxas comparadas às transações Legacy, pois a parte no testemunho custa menos.

Endereços P2WSH são escritos usando a codificação `Bech32` com um checksum na forma de código BCH. Esses endereços sempre começam com `bc1q`. P2WSH é uma saída SegWit versão 0.