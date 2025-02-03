---
term: FUNÇÃO HASH

---
Uma função matemática que recebe uma entrada de tamanho variável (designada por mensagem) e produz uma saída de tamanho fixo (designada por hash, hashing, digest ou impressão digital). As funções de hash são primitivas amplamente utilizadas em criptografia. Apresentam propriedades específicas que as tornam adequadas para utilização em contextos seguros:


- Resistência à pré-imagem: deve ser muito difícil encontrar uma mensagem que produza um hash específico, ou seja, encontrar uma pré-imagem $m$ para um hash $h$ tal que $h = H(m)$, onde $H$ é a função hash;
- Resistência à segunda pré-imagem: dada uma mensagem $m_1$, deve ser muito difícil encontrar outra mensagem $m_2$ (diferente de $m_1$) tal que $H(m_1) = H(m_2)$;
- Resistência à colisão: deve ser muito difícil encontrar duas mensagens distintas $m_1$ e $m_2$ tais que $H(m_1) = H(m_2)$;
- Resistência à violação: pequenas alterações na entrada devem causar alterações significativas e imprevisíveis na saída.

No contexto do Bitcoin, as funções hash são utilizadas para vários fins, incluindo o mecanismo de prova de trabalho (*Proof-of-Work*), identificadores de transação, geração de endereços, cálculos de soma de verificação e a criação de estruturas de dados como árvores Merkle. No lado do protocolo, o Bitcoin usa exclusivamente a função `SHA256d`, também chamada de `HASH256`, que consiste em um hash `SHA256` duplo. o `HASH256` também é usado no cálculo de certos checksums, principalmente para chaves estendidas (`xpub`, `xprv`...). Do lado da carteira, também são usados os seguintes:


- Simples `SHA256` para checksums de frases mnemónicas;
- `SHA512` dentro dos algoritmos `HMAC` e `PBKDF2` utilizados no processo de derivação de carteiras determinísticas e hierárquicas;
- `HASH160`, que descreve uma utilização sucessiva de um `SHA256` e um `RIPEMD160`. o `HASH160` é utilizado no processo de geração de endereços de receção (exceto P2PK e P2TR) e no cálculo das impressões digitais da chave-mãe para chaves alargadas.

> ► *Em inglês, é designada por "hash function"