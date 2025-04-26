---
term: DANDELION

---
Uma proposta destinada a melhorar a privacidade do encaminhamento de transacções na rede Bitcoin para contrariar a desanonimização. No funcionamento normal da Bitcoin, as transacções são imediatamente transmitidas a vários nós. Este fenómeno pode potencialmente permitir que os observadores associem transacções, normalmente anónimas, a endereços IP. O objetivo do BIP156 é resolver este problema. Para isso, introduz uma fase adicional no processo de difusão para preservar o anonimato antes da propagação pública. Assim, o Dandelion utiliza primeiro uma fase "stem" em que a transação é enviada através de um caminho aleatório de nós, antes de ser difundida para toda a rede na fase "fluff". O caule e a penugem são referências ao comportamento da propagação da transação através da rede, assemelhando-se à forma de um dente-de-leão. Este método de encaminhamento obscurece o rasto que conduz ao nó de origem, dificultando o rastreio de uma transação através da rede até à sua origem.

![](../../dictionnaire/assets/36.webp)