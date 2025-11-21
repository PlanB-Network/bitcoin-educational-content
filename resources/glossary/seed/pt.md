---
term: GRÃOS
---

No contexto específico de uma carteira determinística hierárquica Bitcoin, um seed é um pedaço de informação de 512 bits derivado de um evento aleatório. É utilizado para determinar de forma determinística e hierárquica um conjunto de chaves privadas, e as suas correspondentes chaves públicas, para uma carteira Bitcoin. O seed é frequentemente confundido com a própria frase de recuperação. Mas não é a mesma coisa. O seed é obtido pela aplicação da função `PBKDF2` à frase Mnemonic e a qualquer passphrase.


O seed foi inventado com o BIP32, que definiu os fundamentos da carteira determinística hierárquica. Nesta norma, o seed media 128 bits. Isto permite que todas as chaves de um portfólio sejam derivadas de uma única informação, ao contrário dos portfólios JBOK (*Just a Bunch Of Keys*), que requerem novos backups para cada chave gerada. A BIP39 propôs então uma codificação deste seed, para simplificar a sua leitura por humanos. Esta codificação assume a forma de uma frase, geralmente designada por frase Mnemonic ou frase de recuperação. Esta norma evita erros aquando da gravação do seed, graças, nomeadamente, à utilização de uma soma de controlo.


Fora do contexto do Bitcoin, na criptografia em geral, um seed é um valor inicial utilizado para as chaves criptográficas generate ou, mais genericamente, qualquer tipo de dados produzidos por um gerador de números pseudo-aleatórios. Este valor inicial deve ser aleatório e imprevisível para garantir a segurança do sistema criptográfico. De facto, o seed introduz entropia no sistema, mas o processo de geração que se segue é determinístico.


> ► *Na linguagem comum, a maioria dos bitcoiners referem-se à frase Mnemonic quando falam da "seed", e não ao estado de derivação intermédio que se situa entre a frase Mnemonic e a chave-mestra*