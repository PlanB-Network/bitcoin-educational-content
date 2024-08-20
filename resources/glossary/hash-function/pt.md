---
termo: FUNÇÃO HASH
---

Uma função matemática que recebe uma entrada de tamanho variável (chamada de mensagem) e produz uma saída de tamanho fixo (chamada de hash, hashing, digest ou impressão digital). As funções hash são primitivas amplamente utilizadas em criptografia. Elas exibem propriedades específicas que as tornam adequadas para uso em contextos seguros:
* Resistência a pré-imagem: deve ser muito difícil encontrar uma mensagem que produza um hash específico, ou seja, encontrar uma pré-imagem $m$ para um hash $h$ tal que $h = H(m)$, onde $H$ é a função hash;
* Resistência a segunda pré-imagem: dado uma mensagem $m_1$, deve ser muito difícil encontrar outra mensagem $m_2$ (diferente de $m_1$) tal que $H(m_1) = H(m_2)$;
* Resistência a colisão: deve ser muito difícil encontrar duas mensagens distintas $m_1$ e $m_2$ tal que $H(m_1) = H(m_2)$;
* Resistência a adulteração: pequenas alterações na entrada devem causar mudanças significativas e imprevisíveis na saída.

No contexto do Bitcoin, as funções hash são usadas para vários propósitos, incluindo o mecanismo de prova de trabalho (*Proof-of-Work*), identificadores de transações, geração de endereços, cálculos de checksum e a criação de estruturas de dados como árvores de Merkle. No lado do protocolo, o Bitcoin usa exclusivamente a função `SHA256d`, também denominada `HASH256`, que consiste em um duplo hash `SHA256`. `HASH256` também é usado no cálculo de certos checksums, notavelmente para chaves estendidas (`xpub`, `xprv`...). No lado da carteira, também são usados:
* `SHA256` simples para checksums de frases mnemônicas;
* `SHA512` dentro dos algoritmos `HMAC` e `PBKDF2` usados no processo de derivação de carteiras determinísticas e hierárquicas;
* `HASH160`, que descreve um uso sucessivo de um `SHA256` e um `RIPEMD160`. `HASH160` é usado no processo de geração de endereços de recebimento (exceto P2PK e P2TR) e no cálculo de impressões digitais de chaves pai para chaves estendidas.

> ► *Em inglês, é referido como "hash function".*