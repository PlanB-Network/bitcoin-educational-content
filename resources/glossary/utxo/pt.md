---
term: UTXO

---
Acrónimo de *Unspent Transaction Output* (saída de transação não gasta). Um UTXO é uma saída de transação que ainda não foi gasta, o que significa que não foi utilizada como entrada para uma nova transação. Os UTXOs representam a fração de bitcoins que um utilizador possui e que estão atualmente disponíveis para serem gastos. Cada UTXO está associado a um script de saída específico (`scriptPubKey`), que define as condições necessárias para gastar os bitcoins. As transacções em Bitcoin consomem estes UTXOs como entradas e criam novos UTXOs como saídas. O modelo UTXO é fundamental para o Bitcoin, pois permite a fácil verificação de que as transações não estão tentando gastar bitcoins que não existem ou que já foram gastos.