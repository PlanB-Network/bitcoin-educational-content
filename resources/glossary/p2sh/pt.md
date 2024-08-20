---
term: P2SH
---

P2SH significa *Pay to Script Hash* (Pagamento para Hash de Script). É um modelo de script padrão usado para estabelecer condições de gasto em um UTXO. Diferentemente dos scripts P2PK e P2PKH, onde as condições de gasto são predefinidas, o P2SH permite a integração de condições de gasto arbitrárias e funcionalidades adicionais dentro de um script de transação.

Tecnicamente, em uma transação P2SH, o `scriptPubKey` contém o hash criptográfico de um `redeemScript`, em vez de condições explícitas de gasto. Esse hash é obtido usando um hash `SHA256`. Ao enviar bitcoins para um endereço P2SH, o `redeemScript` subjacente não é revelado. Apenas seu hash é incluído na transação. Os endereços P2SH são codificados em `Base58Check` e começam com o número `3`. Quando o destinatário deseja gastar os bitcoins recebidos, ele deve fornecer um `redeemScript` que corresponda ao hash presente no `scriptPubKey`, juntamente com os dados necessários para satisfazer as condições deste `redeemScript`. Por exemplo, em um script multisignature P2SH, o script poderia exigir assinaturas de várias chaves privadas.

O uso de P2SH oferece mais flexibilidade, pois permite a construção de scripts arbitrários sem que o remetente conheça os detalhes. O P2SH foi introduzido em 2012 com o BIP16.