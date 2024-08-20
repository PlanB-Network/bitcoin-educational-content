---
term: BLOCKS INDEX
---

Uma estrutura de dados LevelDB no Bitcoin Core que cataloga metadados sobre todos os blocos. Cada entrada neste índice fornece detalhes como o identificador do bloco, sua altura na blockchain, o ponteiro para o bloco no banco de dados e outros metadados. Essa indexação permite a rápida recuperação de um bloco armazenado na memória.