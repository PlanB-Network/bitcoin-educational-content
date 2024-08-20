---
term: INDEXES/TXINDEX/
---

Arquivos no Bitcoin Core que são dedicados à indexação de todas as transações presentes na blockchain. Essa indexação permite a busca rápida de informações detalhadas sobre uma transação usando seu identificador (TXID), sem ter que percorrer toda a blockchain. A criação desses arquivos de indexação é uma opção que não está habilitada por padrão no Bitcoin Core. Se essa funcionalidade não estiver habilitada, seu nó só indexará transações associadas às carteiras vinculadas ao seu nó. Para habilitar a indexação de todas as transações, você deve definir o parâmetro `-txindex=1` no arquivo `bitcoin.conf`. Esta opção é particularmente útil para aplicações e serviços que frequentemente pesquisam pelo histórico de transações do Bitcoin.