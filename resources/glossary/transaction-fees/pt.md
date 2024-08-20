---
term: TAXAS DE TRANSAÇÃO
---

As taxas de transação representam uma soma que visa compensar os mineradores por sua participação no mecanismo de prova de trabalho. Essas taxas incentivam os mineradores a incluir transações nos blocos que criam. Elas resultam da diferença entre o total de entradas e o total de saídas em uma transação:

```text
taxas = entradas - saídas
```

Elas são expressas em `sats/vBytes`, significando que as taxas não dependem da quantidade de bitcoins enviados, mas do peso da transação. São livremente escolhidas pelo remetente de uma transação e determinam sua velocidade de inclusão em um bloco por meio de um mecanismo de leilão. Por exemplo, digamos que eu faça uma transação com uma entrada de `100.000 sats`, uma saída de `40.000 sats` e outra saída de `58.500 sats`. O total das saídas é `98.500 sats`. As taxas alocadas a esta transação são de `1.500 sats`. O minerador que incluir minha transação pode criar `1.500 sats` em sua transação coinbase em troca dos `1.500 sats` que eu não recuperei em minhas saídas.

Transações com taxas mais altas, relativas ao seu tamanho, são tratadas como prioridade pelos mineradores, o que pode acelerar o processo de confirmação. Por outro lado, transações com taxas mais baixas podem ser atrasadas durante períodos de alta congestão. Vale ressaltar que as taxas de transação do Bitcoin são distintas da recompensa do bloco, que é um incentivo adicional para os mineradores. A recompensa do bloco consiste em novos bitcoins criados com cada bloco minerado (subvenção do bloco), bem como as taxas de transação coletadas. Enquanto a subvenção do bloco diminui ao longo do tempo devido ao limite de oferta total de bitcoins, as taxas de transação continuarão a desempenhar um papel crucial em incentivar os mineradores a participar.

No nível do protocolo, nada impede os usuários de incluir transações sem taxas em um bloco. Na realidade, esse tipo de transação sem taxas é excepcional. Por padrão, os nós do Bitcoin não retransmitem transações com taxas inferiores a `1 sat/vBytes`. Se algumas transações sem taxas passaram, é porque foram integradas diretamente pelo minerador vencedor, sem atravessar a rede de nós. Por exemplo, a seguinte transação não inclui taxas:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Neste exemplo específico, foi uma transação iniciada pelo diretor do pool de mineração F2Pool. Como um usuário regular, o limite inferior atual é, portanto, `1 sat/vBytes`.
Também é necessário considerar os limites de purga. Durante períodos de alta congestão, os mempools dos nós purgam suas transações pendentes abaixo de um certo limiar, a fim de respeitar seu limite de RAM alocado. Este limite é livremente escolhido pelo usuário, mas muitos deixam o valor padrão do Bitcoin Core em 300 MB. Ele pode ser modificado no arquivo `bitcoin.conf` com o parâmetro `maxmempool`.
> ► *Em inglês, referimo-nos a isso como "transaction fees".*