---
term: TAXAS DE TRANSACÇÃO

---
As taxas de transação representam um montante que visa compensar os mineiros pela sua participação no mecanismo de prova de trabalho. Estas taxas incentivam os mineiros a incluir transacções nos blocos que criam. Resultam da diferença entre o montante total de entradas e o montante total de saídas de uma transação:

```text
fees = inputs - outputs
```

São expressas em `sats/vBytes`, o que significa que as taxas não dependem da quantidade de bitcoins enviados, mas do peso da transação. São escolhidas livremente pelo remetente de uma transação e determinam a sua velocidade de inclusão num bloco através de um mecanismo de leilão. Por exemplo, digamos que eu faça uma transação com uma entrada de `100.000 sats`, uma saída de `40.000 sats`, e outra saída de `58.500 sats`. O total das saídas é de `98.500 sats`. As taxas atribuídas a esta transação são de `1.500 sats`. O mineiro que inclui a minha transação pode criar `1.500 sats` na sua transação coinbase em troca dos `1.500 sats` que eu não recuperei nos meus outputs.

As transacções com taxas mais elevadas, relativamente à sua dimensão, são tratadas como prioritárias pelos mineiros, o que pode acelerar o processo de confirmação. Por outro lado, as transacções com taxas mais baixas podem ser atrasadas durante períodos de grande congestionamento. Vale a pena notar que as taxas de transação da Bitcoin são distintas do subsídio por bloco, que é um incentivo adicional para os mineiros. A recompensa do bloco consiste em novos bitcoins criados com cada bloco minerado (subsídio de bloco), bem como nas taxas de transação cobradas. Embora o subsídio de bloco diminua ao longo do tempo devido ao limite de oferta total de bitcoins, as taxas de transação continuarão a desempenhar um papel crucial no incentivo à participação dos mineiros.

Ao nível do protocolo, nada impede os utilizadores de incluírem transacções sem taxas num bloco. Na realidade, este tipo de transação sem taxas é excecional. Por padrão, os nós Bitcoin não retransmitem transações com taxas menores que `1 sat/vBytes`. Se algumas transações sem taxas passaram, é porque foram integradas diretamente pelo minerador vencedor, sem atravessar a rede de nós. Por exemplo, a seguinte transação não inclui taxas:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Neste exemplo específico, foi uma transação iniciada pelo diretor do pool de mineração F2Pool. Como utilizador regular, o limite inferior atual é, portanto, `1 sat/vBytes`.

É igualmente necessário ter em conta os limites da purga. Durante os períodos de elevado congestionamento, os mempools dos nós purgam as suas transacções pendentes abaixo de um determinado limiar, a fim de respeitar o seu limite de RAM atribuído. Este limite é escolhido livremente pelo usuário, mas muitos deixam o valor padrão do Bitcoin Core em 300 MB. Ele pode ser modificado no arquivo `bitcoin.conf` com o parâmetro `maxmempool`.

> ► *Em inglês, designa-se por "transaction fees"