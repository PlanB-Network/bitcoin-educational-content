---
term: P2SH

---
P2SH significa *Pay to Script Hash*. É um modelo de script padrão utilizado para estabelecer condições de despesa num UTXO. Ao contrário dos scripts P2PK e P2PKH, em que as condições de despesa são predefinidas, o P2SH permite a integração de condições de despesa arbitrárias e funcionalidades adicionais num script de transação.

Tecnicamente, numa transação P2SH, o `scriptPubKey` contém o hash criptográfico de um `redeemScript`, em vez de condições de despesa explícitas. Este hash é obtido usando um hash `SHA256`. Ao enviar bitcoins para um endereço P2SH, o `redeemScript` subjacente não é revelado. Apenas o seu hash é incluído na transação. Os endereços P2SH são codificados em `Base58Check` e começam com o número `3`. Quando o destinatário deseja gastar os bitcoins recebidos, ele deve fornecer um `redeemScript` que corresponda ao hash presente na `scriptPubKey`, juntamente com os dados necessários para satisfazer as condições deste `redeemScript`. Por exemplo, num script P2SH multisignature, o script pode requerer assinaturas de múltiplas chaves privadas.

A utilização do P2SH oferece mais flexibilidade, uma vez que permite a construção de scripts arbitrários sem que o remetente conheça os pormenores. O P2SH foi introduzido em 2012 com o BIP16.