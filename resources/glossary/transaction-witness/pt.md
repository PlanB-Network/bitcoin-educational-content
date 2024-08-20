---
term: TRANSACTION WITNESS
---

Refere-se a um componente das transações Bitcoin que foi movido com o soft fork SegWit para abordar o problema da maleabilidade de transações. O testemunho contém as assinaturas e chaves públicas necessárias para desbloquear os bitcoins gastos em uma transação. Em transações Legacy, o testemunho representava a soma de `scriptSig` de todas as entradas. Em transações SegWit, o testemunho representa a soma de `scriptWitness` para cada entrada, e essa parte da transação agora é movida para uma árvore Merkle separada dentro do bloco.

Antes do SegWit, as assinaturas poderiam ser ligeiramente alteradas sem serem invalidadas antes de uma transação ser confirmada, o que mudava o identificador da transação. Isso dificultava a construção de vários protocolos, pois uma transação não confirmada poderia ver seu identificador mudar. Ao separar os testemunhos, o SegWit torna as transações não maleáveis, pois qualquer alteração nas assinaturas não afeta mais o identificador da transação (TXID), mas apenas o identificador do testemunho (WTXID). Além de resolver o problema da maleabilidade, essa separação permite um aumento na capacidade de cada bloco.

> ► *Em inglês, "témoin" é traduzido como "witness".*