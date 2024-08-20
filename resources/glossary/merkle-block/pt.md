---
term: MERKLE BLOCK
---

Uma estrutura de dados utilizada no contexto do BIP37 (*Transaction Bloom Filtering*) para fornecer uma prova compacta da inclusão de transações específicas em um bloco. É notavelmente usado para carteiras SPV. O Merkle Block contém os cabeçalhos de bloco, transações filtradas e uma árvore de Merkle parcial, permitindo que clientes leves verifiquem rapidamente se uma transação pertence a um bloco sem a necessidade de baixar todas as transações.