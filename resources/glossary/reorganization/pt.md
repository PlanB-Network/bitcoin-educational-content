---
term: REORGANIZAÇÃO

---
Refere-se a um fenómeno em que a blockchain sofre uma modificação da sua estrutura devido à existência de blocos concorrentes à mesma altura. Isto ocorre quando uma parte da blockchain é substituída por outra cadeia que tem uma maior quantidade de trabalho acumulado.

Estas reorganizações fazem parte do funcionamento natural da Bitcoin, onde diferentes mineiros podem encontrar novos blocos quase simultaneamente, dividindo assim a rede Bitcoin em duas. Nesses casos, a rede pode dividir-se temporariamente em cadeias concorrentes. Eventualmente, quando uma dessas cadeias acumula mais trabalho, as outras cadeias são abandonadas pelos nós, e seus blocos tornam-se o que é chamado de "blocos obsoletos" ou "blocos órfãos" Este processo de substituição de uma cadeia por outra é a reorganização.

![](../../dictionnaire/assets/9.webp)

As reorganizações podem ter várias consequências. Em primeiro lugar, se um utilizador tiver uma transação confirmada num bloco que acabou por ser abandonado, mas esta transação não aparecer na cadeia finalmente válida, então a sua transação volta a não ser confirmada. É por isso que é aconselhável esperar sempre pelo menos 6 confirmações para considerar uma transação como verdadeiramente imutável. Após 6 blocos de profundidade, as reorganizações são tão improváveis que a hipótese de uma ocorrer pode ser considerada virtualmente nula.

Além disso, a nível do sistema global, as reorganizações implicam um desperdício do poder computacional dos mineiros. De facto, quando ocorre uma divisão, alguns mineiros estarão na cadeia `A` e outros na cadeia `B`. Se a cadeia `B` é eventualmente abandonada durante uma reorganização, então todo o poder computacional utilizado pelos mineiros nesta cadeia é, por definição, desperdiçado. Se houver muitas reorganizações na rede Bitcoin, a segurança geral da mesma é reduzida. É em parte por isso que aumentar o tamanho do bloco ou reduzir o intervalo entre cada bloco (10 minutos) pode ser perigoso.

> ► *Alguns bitcoiners preferem utilizar "orphan block" para se referirem a um bloco expirado. Além disso, na linguagem comum, um "reorg" é utilizado para se referir a uma "reorganização" O termo "reorganização" é um anglicismo. Para ser mais exato, poder-se-ia falar de uma "ressincronização"