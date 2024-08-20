---
term: UNIX TIME
---

Unix Time ou Timestamp Unix representa o número de segundos que se passaram desde 1 de janeiro de 1970, à meia-noite UTC (Unix Epoch). Este sistema é utilizado em sistemas operacionais Unix e derivados para marcar o tempo de maneira universal e padronizada. Ele permite a sincronização de relógios e o gerenciamento de eventos baseados em tempo, independentemente dos fusos horários.

No contexto do Bitcoin, é utilizado para o relógio local dos nós, e assim para o cálculo do NAT (Network-Adjusted Time). O tempo ajustado pela rede é uma mediana dos tempos dos nós calculada localmente por cada nó, e essa referência é então usada para verificar a validade dos timestamps dos blocos. De fato, para que um bloco seja aceito por um nó, seu timestamp deve estar entre o MTP (Median Time Past dos últimos 11 blocos minerados) e o NAT mais 2 horas:

```text
MTP < Timestamp Válido < (NAT + 2h)
```

Unix Time também é usado para estabelecer timelocks quando eles são baseados em tempo real, em vez de em um número de blocos.