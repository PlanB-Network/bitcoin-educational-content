---
term: TXID (IDENTIFICADOR DE TRANSACÇÃO)

---
Um identificador único associado a cada transação Bitcoin. É gerado pelo cálculo do hash `SHA256d` dos dados da transação. O TXID serve como uma referência para encontrar uma transação específica dentro da blockchain. Também é usado para se referir a um UTXO, que é essencialmente a concatenação do TXID de uma transação anterior e o índice da saída designada (também chamada de "vout"). Para transacções pós-SegWit, o TXID já não tem em conta a testemunha da transação, o que elimina a maleabilidade.