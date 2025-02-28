---
term: TRANSACÇÃO (TX)

---
No contexto da Bitcoin, uma transação (abreviada como "TX") é uma operação registada na cadeia de blocos que transfere a propriedade de bitcoins de uma ou mais entradas para uma ou mais saídas. Cada transação consome Unspent Transaction Outputs (UTXOs) como inputs, que são outputs de transacções anteriores, e cria novos UTXOs como outputs, que podem ser utilizados como inputs em transacções futuras.

Cada entrada inclui uma referência a uma saída existente juntamente com um script de assinatura (`scriptSig`) que preenche as condições de gasto (`scriptPubKey`) estabelecidas pela saída que referencia. Isto é o que permite que os bitcoins sejam desbloqueados. As saídas definem novas condições de gasto (`scriptPubKey`) para os bitcoins transferidos, muitas vezes na forma de uma chave pública ou um endereço ao qual os bitcoins estão agora associados.