---
term: P2SH-P2WSH

---
P2SH-P2WSH significa *Pay to Script Hash - Pay to Witness Script Hash*. É um modelo de script padrão usado para estabelecer condições de gastos em um UTXO, também conhecido como "Nested SegWit".

O P2SH-P2WSH foi introduzido com a implementação do SegWit em agosto de 2017. Este script descreve um P2WSH envolto num P2SH. Ele bloqueia bitcoins com base no hash de um script. A diferença de um P2WSH clássico é que o script está envolvido no `redeemScript` de um P2SH clássico.

Este script foi criado aquando do lançamento do SegWit para facilitar a sua adoção. Permite a utilização desta nova norma, mesmo com serviços ou carteiras que ainda não são nativamente compatíveis com o SegWit. Atualmente, já não é muito relevante utilizar este tipo de scripts SegWit, uma vez que a maioria das carteiras implementou o SegWit nativo. Endereços P2SH-P2WSH são escritos usando a codificação `Base58Check` e sempre começam com `3`, como qualquer endereço P2SH.