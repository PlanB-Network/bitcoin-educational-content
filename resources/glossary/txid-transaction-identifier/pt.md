---
term: TXID (IDENTIFICADOR DE TRANSAÇÃO)
---

Um identificador único associado a cada transação Bitcoin. É gerado calculando o hash `SHA256d` dos dados da transação. O TXID serve como uma referência para encontrar uma transação específica dentro do blockchain. Também é usado para se referir a um UTXO, que é essencialmente a concatenação do TXID de uma transação anterior e o índice da saída designada (também chamado de "vout"). Para transações pós-SegWit, o TXID não leva mais em conta a testemunha da transação, o que elimina a maleabilidade.