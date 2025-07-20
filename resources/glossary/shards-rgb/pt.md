---
term: CÁPSULAS (RGB)
---

No contexto do protocolo RGB, um Shard representa um ramo distinto no gráfico acíclico dirigido (DAG) que traça o historial das transições de estado de um Contract. Constitui um subconjunto coerente do conjunto de transições, correspondendo, por exemplo, à sequência de operações necessárias para atestar a validade de um determinado ativo desde o Genesis. Este mecanismo permite isolar segmentos específicos do historial global, para facilitar a verificação do lado do cliente.