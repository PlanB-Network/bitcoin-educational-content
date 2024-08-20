---
termo: SEED (BITCOIN)
---

No contexto do Bitcoin, uma seed é um valor de 512 bits usado para derivar todas as chaves privadas e públicas associadas a uma carteira HD (Hierarchical Deterministic). Tecnicamente, a seed é um valor diferente da frase de recuperação (ou mnemônica). A frase, que é tipicamente composta por 12 ou 24 palavras, é gerada de maneira pseudo-aleatória a partir de uma fonte de entropia e completada por um checksum. Esta frase facilita o backup humano ao fornecer uma representação textual do valor na base da carteira.

Para obter a seed real, a frase de recuperação, possivelmente acompanhada por uma passphrase opcional, é processada através do algoritmo PBKDF2 (*Password-Based Key Derivation Function 2*). O resultado deste cálculo é uma seed de 512 bits. É esta seed que é usada para gerar de forma determinística a chave mestra, e então o conjunto inteiro de chaves para a carteira HD, de acordo com o BIP32.

![](../../dictionnaire/assets/31.png)

> ► *No entanto, na linguagem comum, a maioria dos bitcoiners refere-se à frase mnemônica quando falam sobre a "seed", e não ao estado intermediário de derivação que fica entre a frase mnemônica e a chave mestra.*