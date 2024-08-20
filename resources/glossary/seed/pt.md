---
term: SEED
---

Dentro do contexto específico de uma carteira Bitcoin determinística hierárquica, uma seed é uma peça de informação de 512 bits derivada de aleatoriedade. É usada para gerar de forma determinística e hierárquica um conjunto de chaves privadas e suas correspondentes chaves públicas, para uma carteira Bitcoin. A seed é frequentemente confundida com a frase de recuperação em si. No entanto, são informações diferentes. A seed é obtida aplicando a função `PBKDF2` à frase mnemônica e qualquer passphrase potencial.

A seed foi inventada com a introdução do BIP32, que define as bases da carteira determinística hierárquica. Neste padrão, a seed era de 128 bits. Isso permite a derivação de todas as chaves em uma carteira a partir de uma única peça de informação, ao contrário das carteiras JBOK (*Just a Bunch Of Keys*), que requerem novos backups para cada chave gerada. O BIP39 introduziu posteriormente uma codificação desta seed para simplificar sua legibilidade por humanos. Essa codificação é feita na forma de uma frase, comumente referida como frase mnemônica ou frase de recuperação. Este padrão ajuda a evitar erros no backup da seed, notavelmente através do uso de um checksum.

De forma mais geral, em criptografia, uma seed é uma peça de dados aleatórios usada como ponto de partida para gerar chaves criptográficas, criptografias ou sequências pseudo-aleatórias. A qualidade e segurança de muitos processos criptográficos dependem da aleatoriedade e confidencialidade da seed.

> ► *A tradução em inglês de "graine" é "seed". Em francês, muitos usam diretamente a palavra em inglês para se referir à seed.*