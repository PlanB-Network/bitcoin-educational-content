---
term: IMPRESSÃO DIGITAL PRINCIPAL

---
Uma impressão digital de 4 bytes (32 bits) da chave privada mestre em uma carteira Hierarchical Deterministic (HD). É obtida calculando o hash `SHA256` da chave privada mestre, seguido por um hash `RIPEMD160`, um processo referido como `HASH160` no Bitcoin. O Master Fingerprint é utilizado para identificar uma carteira HD, independentemente dos caminhos de derivação, mas tendo em conta a presença ou ausência de uma frase-chave. É uma informação concisa que permite referenciar a origem de um conjunto de chaves, sem revelar informações sensíveis sobre a carteira.