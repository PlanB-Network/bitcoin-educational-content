---
term: Sökvägsfinnande
definition: Process för att bestämma den optimala vägen för att dirigera en betalning på Lightning-nätverket.
---

Process som används av en nod för att bestämma den optimala vägen för att dirigera en betalning genom Lightning channel-nätverket. Pathfinding utförs av betalarnoden, som måste välja de lämpligaste mellanliggande noderna för att nå mottagaren. Detta val baseras på ett antal kriterier, t.ex. avgifter, kanalkapacitet och tidslås.


Pathfinding-algoritmerna bygger upp en graf över nätverkstopologin utifrån skvallerdata och utvärderar de olika möjliga vägarna mellan betalaren och mottagarnoden. Dessa rutter rangordnas från bäst till sämst enligt olika kriterier. Noden testar sedan dessa vägar tills den lyckas genomföra betalningen på en av dem.