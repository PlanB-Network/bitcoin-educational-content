---
termo: P2SH-P2WSH
---

P2SH-P2WSH significa *Pay to Script Hash - Pay to Witness Script Hash*. É um modelo de script padrão usado para estabelecer condições de gasto em um UTXO, também conhecido como "Nested SegWit".

P2SH-P2WSH foi introduzido com a implementação do SegWit em agosto de 2017. Este script descreve um P2WSH envolvido dentro de um P2SH. Ele bloqueia bitcoins com base no hash de um script. A diferença de um P2WSH clássico é que o script é envolvido no `redeemScript` de um P2SH clássico.

Este script foi criado no lançamento do SegWit para facilitar sua adoção. Ele permite o uso deste novo padrão, mesmo com serviços ou carteiras que ainda não são nativamente compatíveis com SegWit. Hoje, portanto, não é mais muito relevante usar esses tipos de scripts SegWit envolvidos, uma vez que a maioria das carteiras implementou o SegWit nativo. Os endereços P2SH-P2WSH são escritos usando a codificação `Base58Check` e sempre começam com `3`, como qualquer endereço P2SH.