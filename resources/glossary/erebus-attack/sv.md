---
term: Erebus-attack
definition: Attack som gör det möjligt för en skadlig internetleverantör att isolera en Bitcoin-nod från nätverket.
---

En mycket sofistikerad form av attack mot Bitcoin-nätverket som gör det möjligt för en illasinnad internetleverantör att isolera specifika Bitcoin-noder. Det är alltså en form av Eclipse-attack. Erebus-attacken utnyttjar Internet-nätverkets struktur, i synnerhet de obligatoriska passagepunkterna (eller "flaskhalsarna") i routningen mellan autonoma system (AS). En angripare kan, genom att kontrollera ett autonomt system, manipulera nätverkstrafiken för att isolera en Bitcoin-nod från resten av nätverket och därigenom få den att tro på ett falskt Blockchain-tillstånd (block eller transaktioner som inte är kända av noden). Denna isolering kan leda till dubbla utgifter eller censur mot den isolerade noden. Den här attacken har blivit mycket svårare sedan Bitcoin Core version 0.20.0 släpptes och Asmap introducerades.