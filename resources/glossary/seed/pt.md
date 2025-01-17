---
term: SEMENTE

---
No contexto específico de uma carteira Bitcoin determinística hierárquica, uma semente é um pedaço de informação de 512 bits derivado da aleatoriedade. Ela é usada para gerar deterministicamente e hierarquicamente um conjunto de chaves privadas, e suas correspondentes chaves públicas, para uma carteira Bitcoin. A semente é frequentemente confundida com a própria frase de recuperação. No entanto, são informações diferentes. A semente é obtida através da aplicação da função `PBKDF2` à frase mnemónica e a qualquer frase-chave potencial.

A semente foi inventada com a introdução do BIP32, que define as bases da carteira determinística hierárquica. Nesta norma, a semente era de 128 bits. Isto permite a derivação de todas as chaves numa carteira a partir de um único pedaço de informação, ao contrário das carteiras JBOK (*Just a Bunch Of Keys*), que requerem novas cópias de segurança para cada chave gerada. O BIP39 introduziu mais tarde uma codificação desta semente para simplificar a sua leitura por humanos. Esta codificação é feita sob a forma de uma frase, normalmente designada por frase mnemónica ou frase de recuperação. Esta norma ajuda a evitar erros na cópia de segurança da semente, nomeadamente através da utilização de uma soma de controlo.

Em termos mais gerais, na criptografia, uma semente é um dado aleatório utilizado como ponto de partida para gerar chaves criptográficas, cifras ou sequências pseudo-aleatórias. A qualidade e a segurança de muitos processos criptográficos dependem da aleatoriedade e da confidencialidade da semente.

> ► *A tradução inglesa de "graine" é "seed". Em francês, muitos utilizam diretamente a palavra inglesa para se referirem à semente.*