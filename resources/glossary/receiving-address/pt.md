---
termo: ENDEREÇO DE RECEBIMENTO
---

Informação usada para receber bitcoins. Um endereço é geralmente construído através do hash de uma chave pública, usando `SHA256` e `RIMPEMD160`, e adicionando metadados a este resumo. As chaves públicas usadas para construir um endereço de recebimento fazem parte da carteira do usuário e, portanto, são derivadas de sua semente. Por exemplo, os endereços SegWit são compostos pelas seguintes informações:
* Um HRP para designar "bitcoin": `bc`;
* Um separador: `1`;
* A versão do SegWit usada: `q` ou `p`;
* O payload: o resumo da chave pública (ou diretamente a chave pública no caso do Taproot);
* O checksum: um código BCH.

No entanto, um endereço de recebimento também pode representar algo diferente dependendo do modelo de script usado. Por exemplo, os endereços P2SH são construídos usando o hash do script. Os endereços Taproot, por outro lado, contêm a chave pública ajustada diretamente sem hashá-la.

Um endereço de recebimento pode ser representado na forma de uma string alfanumérica ou como um código QR. Cada endereço pode ser usado várias vezes, mas esta é uma prática altamente desencorajada. De fato, para manter um certo nível de privacidade, é aconselhado usar cada endereço Bitcoin apenas uma vez. Um novo endereço deve ser gerado para cada pagamento recebido na carteira. Um endereço é codificado em `Bech32` para endereços SegWit V0, em `Bech32m` para endereços SegWit V1, e em `Base58check` para endereços Legacy. Do ponto de vista técnico, receber bitcoin traduz-se em possuir a chave privada associada a uma chave pública (e, portanto, um endereço). Quando alguém recebe bitcoins, o remetente atualiza a restrição existente sobre seus gastos para que apenas o destinatário possa agora ter esse poder.

![](../../dictionnaire/assets/23.png)