---
term: P2PKH
---

P2PKH significa *Pay to Public Key Hash* (Pagar para Hash da Chave Pública). É um modelo padrão de script usado para estabelecer condições de gasto em um UTXO. Permite bloquear bitcoins em um hash de uma chave pública, isto é, em um endereço de recebimento. Este script está associado ao padrão Legacy e foi introduzido nas primeiras versões do Bitcoin por Satoshi Nakamoto.

Ao contrário do P2PK, onde a chave pública é explicitamente incluída no script, o P2PKH usa uma impressão digital criptográfica da chave pública. Este script inclui o hash `RIPEMD160` do `SHA256` da chave pública e estipula que, para acessar os fundos, o destinatário deve fornecer uma chave pública que corresponda a este hash, bem como uma assinatura digital válida gerada a partir da chave privada associada. Os endereços P2PKH são codificados usando o formato `Base58Check`, o que lhes confere robustez contra erros tipográficos por meio do uso de um checksum. Esses endereços sempre começam com o número `1`.