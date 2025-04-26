---
term: TESTEMUNHA DE TRANSACÇÃO

---
Refere-se a um componente das transacções Bitcoin que foi movido com o soft fork SegWit para resolver a questão da maleabilidade da transação. A testemunha contém as assinaturas e chaves públicas necessárias para desbloquear os bitcoins gastos em uma transação. Nas transacções Legacy, a testemunha representava a soma do `scriptSig` de todas as entradas. Nas transacções SegWit, a testemunha representa a soma de `scriptWitness` para cada entrada, e esta parte da transação é agora movida para uma árvore Merkle separada dentro do bloco.

Antes do SegWit, as assinaturas podiam ser ligeiramente alteradas sem serem invalidadas antes de uma transação ser confirmada, o que alterava o identificador da transação. Isto dificultava a construção de vários protocolos, uma vez que uma transação não confirmada podia ver o seu identificador alterado. Ao separar as testemunhas, o SegWit torna as transacções não maleáveis, uma vez que qualquer alteração nas assinaturas já não afecta o identificador da transação (TXID), mas apenas o identificador da testemunha (WTXID). Para além de resolver o problema da maleabilidade, esta separação permite um aumento da capacidade de cada bloco.

> ► *Em inglês, "témoin" traduz-se por "testemunha".*