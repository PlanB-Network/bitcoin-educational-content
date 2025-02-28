---
term: ENDEREÇO DE RECEPÇÃO

---
Informação usada para receber bitcoins. Um endereço é normalmente construído através do hashing de uma chave pública, usando `SHA256` e `RIMPEMD160`, e adicionando metadados a este digest. As chaves públicas usadas para construir um endereço de receção fazem parte da carteira do utilizador e são, portanto, derivadas da sua semente. Por exemplo, os endereços SegWit são compostos pelas seguintes informações:


- Um PRH para designar "bitcoin": `bc`;
- Um separador: `1`;
- A versão do SegWit utilizada: `q` ou `p`;
- A carga útil: o resumo da chave pública (ou diretamente a chave pública no caso do Taproot);
- A soma de controlo: um código BCH.

No entanto, um endereço de receção também pode representar outra coisa, dependendo do modelo de script utilizado. Por exemplo, os endereços P2SH são construídos usando o hash do script. Os endereços Taproot, por outro lado, contêm a chave pública ajustada diretamente, sem fazer o hash.

Um endereço de receção pode ser representado sob a forma de uma cadeia alfanumérica ou de um código QR. Cada endereço pode ser usado várias vezes, mas esta é uma prática altamente desencorajada. De facto, para manter um certo nível de privacidade, é aconselhável usar cada endereço Bitcoin apenas uma vez. Um novo endereço deve ser gerado para cada pagamento recebido na carteira. Um endereço é codificado em `Bech32` para endereços SegWit V0, em `Bech32m` para endereços SegWit V1, e em `Base58check` para endereços Legacy. De um ponto de vista técnico, receber bitcoin traduz-se em possuir a chave privada associada a uma chave pública (e, portanto, um endereço). Quando alguém recebe bitcoins, o remetente actualiza a restrição existente sobre os seus gastos para que apenas o destinatário possa agora ter este poder.

![](../../dictionnaire/assets/23.webp)