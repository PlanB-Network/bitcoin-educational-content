---
termo: RESYNCHRONIZATION
---

Refere-se a um fenômeno no qual o blockchain passa por uma modificação de sua estrutura devido à existência de blocos concorrentes na mesma altura. Isso ocorre quando uma parte do blockchain é substituída por outra cadeia com uma maior quantidade de trabalho acumulado.

Essas ressincronizações são parte do funcionamento natural do Bitcoin, onde diferentes mineradores podem encontrar novos blocos quase simultaneamente, dividindo assim a rede Bitcoin em duas. Nestes casos, a rede pode temporariamente dividir-se em cadeias concorrentes. Eventualmente, quando uma dessas cadeias acumula mais trabalho, as outras cadeias são abandonadas pelos nós, e seus blocos tornam-se o que chamamos de "blocos obsoletos" ou "blocos órfãos". Este processo de substituição de uma cadeia por outra é a ressincronização.

![](../../dictionnaire/assets/9.png)

Ressincronizações podem ter várias consequências. Primeiro, se um usuário teve uma transação confirmada em um bloco que acaba sendo abandonado, mas esta transação não é encontrada na cadeia válida finalmente, então sua transação torna-se não confirmada novamente. É por isso que é aconselhado sempre esperar por pelo menos 6 confirmações para considerar uma transação como verdadeiramente imutável. Após 6 blocos de profundidade, ressincronizações são tão improváveis que a chance de uma ocorrer pode ser considerada praticamente nula.

Além disso, no nível do sistema global, ressincronizações implicam um desperdício do poder computacional dos mineradores. De fato, quando uma divisão ocorre, alguns mineradores estarão na cadeia `A`, e outros na cadeia `B`. Se a cadeia `B` é eventualmente abandonada durante uma ressincronização, então todo o poder computacional empregado pelos mineradores nesta cadeia é, por definição, desperdiçado. Se houver muitas ressincronizações na rede Bitcoin, a segurança geral da rede é, portanto, reduzida. É parcialmente por isso que aumentar o tamanho do bloco ou reduzir o intervalo entre cada bloco (10 minutos) pode ser perigoso.

> ► *Alguns bitcoiners preferem usar "bloco órfão" para se referir a um bloco expirado. Além disso, mesmo sendo um anglicismo, na linguagem comum, uma "reorganização" ou um "reorg" é frequentemente preferido em vez de "ressincronização".*