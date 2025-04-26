---
term: P2SH-P2WPKH

---
P2SH-P2WPKH significa *Pay to Script Hash - Pay to Witness Public Key Hash*. É um modelo de script padrão usado para estabelecer condições de gastos em um UTXO, também conhecido como "Nested SegWit".

O P2SH-P2WPKH foi introduzido com a implementação do SegWit em agosto de 2017. Este script é um P2WPKH envolto em um P2SH. Ele bloqueia bitcoins com base no hash de uma chave pública. A diferença do P2WPKH clássico é que o script está envolvido no `redeemScript` de um P2SH clássico.

Este script foi criado aquando do lançamento do SegWit para facilitar a sua adoção. Permite a utilização desta nova norma, mesmo com serviços ou carteiras que ainda não são nativamente compatíveis com o SegWit. Trata-se de uma espécie de script de transição para a nova norma. Atualmente, já não é muito relevante utilizar este tipo de scripts SegWit, uma vez que a maioria das carteiras implementou o SegWit nativo. Endereços P2SH-P2WPKH são escritos usando a codificação `Base58Check` e sempre começam com `3`, como qualquer endereço P2SH.

> ► *`P2SH-P2WPKH` também é por vezes designado `P2WPKH-nested-in-P2SH`.*