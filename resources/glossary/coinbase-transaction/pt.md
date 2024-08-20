---
termo: COINBASE (TRANSAÇÃO)
---

A transação coinbase é uma transação especial e única incluída em cada bloco da blockchain do Bitcoin. Ela representa a primeira transação de um bloco e é criada pelo minerador que conseguiu encontrar um cabeçalho validando a prova de trabalho (*Proof-of-Work*), ou seja, menor ou igual ao alvo.

A transação coinbase serve principalmente dois propósitos: premiar o minerador com a recompensa do bloco e adicionar novas unidades de bitcoins ao suprimento de dinheiro em circulação. A recompensa do bloco, que é o incentivo econômico para os mineradores se engajarem na prova de trabalho, inclui as taxas acumuladas pelas transações incluídas no bloco e uma quantidade determinada de bitcoins recém-criados do nada (subvenção do bloco). Esse montante, inicialmente estabelecido em 50 bitcoins por bloco em 2009, é reduzido pela metade a cada 210.000 blocos (aproximadamente a cada 4 anos) durante um evento chamado "halving".

A transação coinbase difere das transações regulares de várias maneiras. Primeiro, ela não tem uma entrada, significando que nenhum output de transação existente (UTXO) é consumido por ela. Em seguida, o script de assinatura (`scriptSig`) para a transação coinbase tipicamente contém um campo arbitrário permitindo a incorporação de dados adicionais, como mensagens personalizadas ou informações sobre a versão do software de mineração. Finalmente, os bitcoins gerados pela transação coinbase estão sujeitos a um período de maturidade de 100 blocos (101 confirmações) antes que possam ser gastos, para prevenir o potencial gasto de bitcoins inexistentes em caso de uma reorganização da cadeia.

> ► *Não há tradução para "Coinbase" em Português. Portanto, é aceitável usar este termo diretamente.*