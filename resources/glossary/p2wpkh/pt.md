---
term: P2WPKH

---
P2WPKH significa *Pay to Witness Public Key Hash*. É um modelo de script padrão usado para estabelecer condições de gastos em um UTXO. O P2WPKH foi introduzido com a implementação do SegWit em agosto de 2017.

Esse script é semelhante ao P2PKH (*Pay to Public Key Hash*), pois também bloqueia bitcoins com base no hash de uma chave pública, ou seja, um endereço de recebimento. A diferença reside na forma como as assinaturas e os scripts são incluídos na transação. No caso do P2WPKH, a informação do script de assinatura (`scriptSig`) é movida da estrutura tradicional da transação para uma secção separada chamada `Witness`. Esta mudança é uma caraterística da atualização SegWit (*Segregated Witness*) que ajuda a prevenir a maleabilidade da assinatura. As transacções P2WPKH são geralmente menos dispendiosas em termos de taxas em comparação com as transacções Legacy, uma vez que a parte da testemunha custa menos.

Os endereços P2WPKH são escritos usando a codificação `Bech32` com uma soma de controlo na forma de código BCH. Estes endereços começam sempre com `bc1q`. P2WPKH é uma saída SegWit versão 0.