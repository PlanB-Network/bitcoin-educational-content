---
term: BLOCO DE MERKLE

---
Uma estrutura de dados utilizada no contexto do BIP37 (*Transaction Bloom Filtering*) para fornecer uma prova compacta da inclusão de transacções específicas num bloco. É utilizada nomeadamente para as carteiras SPV. O bloco Merkle contém os cabeçalhos dos blocos, as transacções filtradas e uma árvore Merkle parcial, permitindo aos clientes ligeiros verificar rapidamente se uma transação pertence a um bloco sem descarregar todas as transacções.