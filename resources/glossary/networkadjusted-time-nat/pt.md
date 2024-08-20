---
termo: TEMPO AJUSTADO DA REDE (NAT)
---

Estimativa do tempo universal estabelecida nos relógios dos nós da rede. Cada nó calcula seu NAT tomando a mediana das diferenças de tempo entre seu relógio local (UTC) e aqueles dos nós aos quais está conectado, adicionando então ao seu relógio local a mediana dessas diferenças, até um máximo de 70 minutos. O tempo ajustado da rede é, portanto, uma mediana dos tempos dos nós calculada localmente por cada nó. Esse quadro de referência é então usado para verificar a validade dos timestamps dos blocos. De fato, para que um bloco seja aceito por um nó, seu timestamp deve estar entre o MTP (tempo médio dos últimos 11 blocos minerados) e o NAT mais 2 horas:

```text
MTP < Timestamp Válido < (NAT + 2h)
```