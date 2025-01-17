---
term: WTXID

---
Uma extensão do TXID tradicional, incluindo dados de testemunha introduzidos com o SegWit. Enquanto o TXID é um hash dos dados da transação excluindo a testemunha, o WTXID é o `SHA256d` de todos os dados da transação, incluindo a testemunha. Os WTXIDs são armazenados em uma árvore Merkle separada, cuja raiz é colocada na transação da coinbase. Esta separação permite a remoção da maleabilidade da transação do TXID.