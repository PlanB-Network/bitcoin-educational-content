---
termo: BIP156
---

Proposta, conhecida como Dandelion, que visa melhorar a privacidade do roteamento de transações na rede Bitcoin para contrariar a desanonimização. Na operação padrão do Bitcoin, as transações são imediatamente transmitidas para múltiplos nós. Se um observador consegue ver cada transação retransmitida por cada nó na rede, ele pode assumir que o primeiro nó a enviar uma transação é também o nó de origem dessa transação, e, portanto, que ela vem do operador do nó. Esse fenômeno poderia potencialmente permitir que observadores vinculassem transações, normalmente anônimas, com endereços IP.

O objetivo do BIP156 é abordar essa questão. Para fazer isso, introduz uma fase adicional na transmissão para preservar o anonimato antes da propagação pública. Assim, Dandelion primeiro utiliza uma fase "stem" (caule) onde a transação é enviada através de um caminho aleatório de nós, antes de ser transmitida para toda a rede na fase "fluff" (pluma). O caule e a pluma são referências ao comportamento da propagação da transação através da rede, assemelhando-se à forma de um dente-de-leão (*dandelion* em inglês).

Este método de roteamento obscurece o rastro que leva de volta ao nó de origem, tornando difícil rastrear uma transação através da rede até sua origem. Dandelion, assim, melhora a privacidade limitando a capacidade dos adversários de desanonimizar a rede. Este método é ainda mais eficaz quando a transação cruza, durante a fase "stem", um nó que criptografa suas comunicações de rede, como com Tor ou *P2P Transport V2*. O BIP156 ainda não foi adicionado ao Bitcoin Core.

![](../../dictionnaire/assets/36.png)