---
term: P2PKH

---
P2PKH significa *Pay to Public Key Hash*. É um modelo de script padrão utilizado para estabelecer condições de despesa num UTXO. Permite bloquear bitcoins num hash de uma chave pública, ou seja, num endereço de receção. Este script está associado ao padrão Legacy e foi introduzido nas primeiras versões do Bitcoin por Satoshi Nakamoto.

Ao contrário do P2PK, em que a chave pública é explicitamente incluída no script, o P2PKH utiliza uma impressão digital criptográfica da chave pública. Este script inclui o hash `RIPEMD160` do `SHA256` da chave pública e estipula que, para aceder aos fundos, o destinatário deve fornecer uma chave pública que corresponda a este hash, bem como uma assinatura digital válida gerada a partir da chave privada associada. Os endereços P2PKH são codificados usando o formato `Base58Check`, o que lhes confere robustez contra erros tipográficos através do uso de um checksum. Estes endereços começam sempre com o número `1`.