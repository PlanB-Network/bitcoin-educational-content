---
term: MERKLE ROOT
---

Digest ou "top hash" de uma árvore de Merkle, que representa um resumo de todas as informações presentes na árvore. Uma árvore de Merkle é uma estrutura acumuladora criptográfica, às vezes também chamada de "árvore de hash". No contexto do Bitcoin, árvores de Merkle são usadas para organizar transações dentro de um bloco e facilitar a verificação rápida da inclusão de uma transação específica. Assim, nos blocos do Bitcoin, a raiz de Merkle é obtida ao se fazer o hash das transações em pares sucessivamente até que apenas um hash permaneça (a raiz de Merkle). Este é então incluído no cabeçalho do bloco correspondente. Esta árvore de hash também é encontrada no UTREEXO, uma estrutura que permite condensar o conjunto UTXO dos nós, e no MAST Taproot.