---
term: TRANSACTION (TX)
---

No contexto do Bitcoin, uma transação (abreviada como "TX") é uma operação registrada na blockchain que transfere a propriedade de bitcoins de uma ou mais entradas para uma ou mais saídas. Cada transação consome Saídas de Transação Não Gastas (UTXOs) como entradas, que são saídas de transações anteriores, e cria novas UTXOs como saídas, que podem ser usadas como entradas em transações futuras.

Cada entrada inclui uma referência a uma saída existente junto com um script de assinatura (`scriptSig`) que cumpre as condições de gasto (`scriptPubKey`) estabelecidas pela saída que referencia. É isso que permite que os bitcoins sejam desbloqueados. As saídas definem novas condições de gasto (`scriptPubKey`) para os bitcoins transferidos, frequentemente na forma de uma chave pública ou um endereço ao qual os bitcoins agora estão associados.