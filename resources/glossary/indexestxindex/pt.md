---
term: INDEXES/TXINDEX/

---
Ficheiros no Bitcoin Core que são dedicados à indexação de todas as transacções presentes na blockchain. Esta indexação permite uma pesquisa rápida de informação detalhada sobre uma transação utilizando o seu identificador (TXID), sem ter de percorrer toda a blockchain. A criação desses arquivos de indexação é uma opção não habilitada por padrão no Bitcoin Core. Se esse recurso não estiver ativado, seu nó indexará apenas as transações associadas às carteiras anexadas ao seu nó. Para habilitar a indexação de todas as transações, você deve definir o parâmetro `-txindex=1` no arquivo `bitcoin.conf`. Esta opção é particularmente útil para aplicações e serviços que frequentemente pesquisam o histórico de transações do Bitcoin.