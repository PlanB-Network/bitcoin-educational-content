---
term: COINBASE (TRANSACÇÃO)

---
A transação coinbase é uma transação especial e única incluída em cada bloco da cadeia de blocos Bitcoin. Representa a primeira transação de um bloco e é criada pelo mineiro que encontrou com sucesso um cabeçalho que valida a prova de trabalho (*Proof-of-Work*), ou seja, menor ou igual ao objetivo.

A transação coinbase tem essencialmente dois objectivos: atribuir a recompensa do bloco ao mineiro e adicionar novas unidades de bitcoins à massa monetária em circulação. A recompensa do bloco, que é o incentivo económico para os mineiros se envolverem na prova de trabalho, inclui as taxas acumuladas para as transacções incluídas no bloco e um determinado montante de bitcoins recém-criados ex-nihilo (subsídio de bloco). Este montante, inicialmente fixado em 50 bitcoins por bloco em 2009, é reduzido para metade a cada 210 000 blocos (aproximadamente a cada 4 anos) durante um evento designado por "halving"

A transação coinbase difere das transacções normais de várias formas. Primeiro, ela não tem uma entrada, o que significa que nenhuma saída de transação existente (UTXO) é consumida por ela. Em seguida, o script de assinatura (`scriptSig`) para a transação coinbase contém normalmente um campo arbitrário que permite a incorporação de dados adicionais, tais como mensagens personalizadas ou informações sobre a versão do software de mineração. Finalmente, os bitcoins gerados pela transação coinbase estão sujeitos a um período de maturidade de 100 blocos (101 confirmações) antes de poderem ser gastos, para evitar o potencial gasto de bitcoins inexistentes no caso de uma reorganização da cadeia.

> ► *Não existe tradução de "Coinbase" em francês. Por conseguinte, é aceite a utilização direta deste termo.*