---
term: CHECKSUM
---

Um checksum é um valor calculado a partir de um conjunto de dados, usado para verificar a integridade e validade desses dados durante sua transmissão ou armazenamento. Algoritmos de checksum são projetados para detectar erros acidentais ou alterações não intencionais dos dados, como erros de transmissão ou corrupções de arquivos. Existem vários tipos de algoritmos de checksum, como verificações de paridade, checksums modulares, funções de hash criptográficas ou códigos BCH (*Bose, Ray-Chaudhuri e Hocquenghem*).

No Bitcoin, checksums são usados no nível da aplicação para garantir a integridade dos endereços de recebimento. Um checksum é calculado a partir do payload de um endereço do usuário, e então adicionado a este endereço para detectar possíveis erros durante sua entrada. Um checksum também está presente em frases de recuperação (mnemônico).

> ► *A tradução em inglês de "somme de contrôle" é "checksum". Geralmente é aceito usar diretamente o termo "checksum" em francês.*