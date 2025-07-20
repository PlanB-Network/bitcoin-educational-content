---
term: PATHFINDING
---

Prosess som brukes av en node for å finne den optimale veien for ruting av en betaling gjennom Lightning Channel-nettverket. Pathfinding utføres av betalernoden, som må velge de mest egnede mellomliggende nodene for å nå mottakeren. Dette valget er basert på en rekke kriterier, for eksempel gebyrer, kanalkapasitet og tidssperrer.


Pathfinding-algoritmer bygger en graf over nettverkstopologien ut fra sladderdataene og evaluerer de ulike mulige rutene mellom betaler- og mottakernoden. Disse rutene rangeres fra best til dårligst i henhold til ulike kriterier. Noden tester deretter disse rutene til den lykkes med å utføre betalingen på en av dem.