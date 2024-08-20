---
termo: DANDELION
---

Uma proposta destinada a melhorar a privacidade do roteamento de transações na rede Bitcoin para contrariar a desanonimização. Na operação padrão do Bitcoin, as transações são imediatamente transmitidas para múltiplos nós. Esse fenômeno pode potencialmente permitir que observadores vinculem transações, normalmente anônimas, com endereços IP. O objetivo do BIP156 é abordar essa questão. Para isso, introduz uma fase adicional no processo de transmissão para preservar o anonimato antes da propagação pública. Assim, Dandelion primeiro utiliza uma fase "stem" (caule) onde a transação é enviada através de um caminho aleatório de nós, antes de ser transmitida para toda a rede na fase "fluff" (pluma). As fases stem e fluff são referências ao comportamento da propagação da transação pela rede, assemelhando-se à forma de um dente-de-leão. Este método de roteamento obscurece o rastro que leva de volta ao nó de origem, tornando difícil rastrear uma transação através da rede até sua origem.

![](../../dictionnaire/assets/36.png)