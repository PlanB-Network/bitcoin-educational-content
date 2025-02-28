---
term: BIP156

---
Proposta, conhecida como Dandelion, que visa melhorar a privacidade do encaminhamento de transacções na rede Bitcoin para contrariar a desanonimização. Na operação padrão do Bitcoin, as transações são imediatamente transmitidas para vários nós. Se um observador for capaz de ver cada transação retransmitida por cada nó na rede, poderá assumir que o primeiro nó a enviar uma transação é também o nó de origem dessa transação e, portanto, que esta provém do operador do nó. Este fenómeno pode potencialmente permitir que os observadores associem transacções, normalmente anónimas, a endereços IP.

O objetivo do BIP156 é resolver este problema. Para isso, introduz uma fase adicional na difusão para preservar o anonimato antes da propagação pública. Assim, o Dandelion utiliza primeiro uma fase "stem" em que a transação é enviada através de um caminho aleatório de nós, antes de ser difundida para toda a rede na fase "fluff". O caule e a penugem são referências ao comportamento da propagação da transação através da rede, assemelhando-se à forma de um dente-de-leão (*a dandelion* em inglês).

Este método de encaminhamento obscurece o rasto que conduz ao nó de origem, dificultando o rastreio de uma transação através da rede até à sua origem. O Dandelion melhora assim a privacidade, limitando a capacidade dos adversários de desanonimizarem a rede. Este método é ainda mais eficaz quando a transação atravessa, durante a fase "stem", um nó que encripta as suas comunicações na rede, como o Tor ou o *P2P Transport V2*. O BIP156 ainda não foi adicionado ao Bitcoin Core.

![](../../dictionnaire/assets/36.webp)