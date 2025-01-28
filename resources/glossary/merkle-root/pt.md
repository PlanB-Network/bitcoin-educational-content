---
term: RAIZ DE MERKLE

---
Digesto ou "top hash" de uma árvore de Merkle, que representa um resumo de todas as informações presentes na árvore. Uma árvore de Merkle é uma estrutura de acumulação criptográfica, por vezes também designada por "árvore de hash". No contexto da Bitcoin, as árvores de Merkle são utilizadas para organizar as transacções dentro de um bloco e para facilitar a verificação rápida da inclusão de uma transação específica. Assim, nos blocos de Bitcoin, a raiz de Merkle é obtida através do hash sucessivo das transacções em pares até restar apenas um hash (a raiz de Merkle). Este é então incluído no cabeçalho do bloco correspondente. Esta árvore de hash também se encontra no UTREEXO, uma estrutura que permite condensar o conjunto de nós UTXO, e no MAST Taproot.