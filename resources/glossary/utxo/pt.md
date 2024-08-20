---
term: UTXO
---

Acrônimo para *Unspent Transaction Output* (Saída de Transação Não Gasta). Um UTXO é uma saída de transação que ainda não foi gasta, significando que não foi usada como entrada para uma nova transação. Os UTXOs representam a fração de bitcoins que um usuário possui e que estão atualmente disponíveis para serem gastos. Cada UTXO está associado a um script de saída específico (`scriptPubKey`), que define as condições necessárias para gastar os bitcoins. As transações em Bitcoin consomem esses UTXOs como entradas e criam novos UTXOs como saídas. O modelo UTXO é fundamental para o Bitcoin, pois permite uma fácil verificação de que as transações não estão tentando gastar bitcoins que não existem ou que já foram gastos.