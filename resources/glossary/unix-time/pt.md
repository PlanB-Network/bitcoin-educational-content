---
term: TEMPO UNIX

---
Unix Time ou Unix Timestamp representa o número de segundos decorridos desde 1 de janeiro de 1970, à meia-noite UTC (Unix Epoch). Este sistema é utilizado nos sistemas operativos Unix e derivados para marcar o tempo de uma forma universal e normalizada. Permite a sincronização de relógios e a gestão de eventos baseados no tempo, independentemente dos fusos horários.

No contexto do Bitcoin, é utilizado para o relógio local dos nós e, portanto, para o cálculo do NAT (Network-Adjusted Time). O tempo ajustado à rede é uma mediana dos tempos dos nós calculados localmente por cada nó, e esta referência é então utilizada para verificar a validade dos carimbos de data/hora dos blocos. De facto, para que um bloco seja aceite por um nó, o seu carimbo de data/hora deve estar entre o MTP (Median Time Past dos últimos 11 blocos minerados) e o NAT mais 2 horas:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

O Unix Time também é usado para estabelecer timelocks quando estes são baseados em tempo real, em vez de num número de blocos.