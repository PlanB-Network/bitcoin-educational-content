---
term: IMPRESSÃO DIGITAL MESTRE
---

Uma impressão digital de 4 bytes (32 bits) da chave privada mestre em uma carteira Hierárquica Determinística (HD). É obtida calculando o hash `SHA256` da chave privada mestre, seguido de um hash `RIPEMD160`, um processo referido como `HASH160` no Bitcoin. A Impressão Digital Mestre é usada para identificar uma carteira HD, independentemente dos caminhos de derivação, mas levando em conta a presença ou ausência de uma frase-senha. É uma informação concisa que permite referenciar a origem de um conjunto de chaves, sem revelar informações sensíveis sobre a carteira.