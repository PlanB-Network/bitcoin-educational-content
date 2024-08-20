---
termo: P2SH-P2WPKH
---

P2SH-P2WPKH significa *Pay to Script Hash - Pay to Witness Public Key Hash*. É um modelo de script padrão usado para estabelecer condições de gasto em um UTXO, também conhecido como "Nested SegWit".

P2SH-P2WPKH foi introduzido com a implementação do SegWit em agosto de 2017. Esse script é um P2WPKH envolvido dentro de um P2SH. Ele bloqueia bitcoins com base no hash de uma chave pública. A diferença do P2WPKH clássico é que o script está envolvido no `redeemScript` de um P2SH clássico.

Esse script foi criado no lançamento do SegWit para facilitar sua adoção. Ele permite o uso desse novo padrão, mesmo com serviços ou carteiras que ainda não são nativamente compatíveis com SegWit. É um tipo de script de transição em direção ao novo padrão. Hoje, portanto, não é mais muito relevante usar esses tipos de scripts SegWit envolvidos, uma vez que a maioria das carteiras implementou o SegWit nativo. Endereços P2SH-P2WPKH são escritos usando a codificação `Base58Check` e sempre começam com `3`, como qualquer endereço P2SH.

> ► *`P2SH-P2WPKH` também é às vezes chamado de `P2WPKH-aninhado-em-P2SH`.*