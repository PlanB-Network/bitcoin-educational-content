---
term: CHECKSUM

---
Uma soma de controlo é um valor calculado a partir de um conjunto de dados, utilizado para verificar a integridade e a validade desses dados durante a sua transmissão ou armazenamento. Os algoritmos de soma de controlo são concebidos para detetar erros acidentais ou alterações não intencionais dos dados, tais como erros de transmissão ou corrupção de ficheiros. Existem vários tipos de algoritmos de soma de controlo, como verificações de paridade, somas de controlo modulares, funções de hash criptográficas ou códigos BCH (*Bose, Ray-Chaudhuri e Hocquenghem*).

No Bitcoin, as somas de verificação são usadas no nível da aplicação para garantir a integridade dos endereços recebidos. Uma soma de controlo é calculada a partir da carga útil do endereço de um utilizador e depois adicionada a este endereço para detetar possíveis erros durante a sua entrada. Uma soma de controlo está também presente nas frases de recuperação (mnemónica).

> ► *A tradução inglesa de "somme de contrôle" é "checksum". É geralmente aceite a utilização direta do termo "checksum" em francês.*