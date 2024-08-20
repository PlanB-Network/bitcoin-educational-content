---
term: P2WPKH
---

P2WPKH significa *Pay to Witness Public Key Hash* (Pagar para Testemunhar Hash da Chave Pública). É um modelo de script padrão usado para estabelecer condições de gasto em um UTXO. O P2WPKH foi introduzido com a implementação do SegWit em agosto de 2017.

Este script é semelhante ao P2PKH (*Pay to Public Key Hash*, Pagar para Hash da Chave Pública), pois também bloqueia bitcoins com base no hash de uma chave pública, isto é, um endereço de recebimento. A diferença reside em como as assinaturas e scripts são incluídos na transação. No caso do P2WPKH, a informação do script de assinatura (`scriptSig`) é movida da estrutura tradicional da transação para uma seção separada chamada `Witness` (Testemunha). Esse movimento é uma característica da atualização SegWit (*Segregated Witness*, Testemunha Segregada) que ajuda a prevenir a maleabilidade de assinaturas. As transações P2WPKH geralmente são menos caras em termos de taxas comparadas às transações Legacy, pois a parte no testemunho custa menos.

Os endereços P2WPKH são escritos usando a codificação `Bech32` com um checksum na forma de código BCH. Esses endereços sempre começam com `bc1q`. P2WPKH é uma saída SegWit versão 0.