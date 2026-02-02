---
term: BIP0008
definition: Methode voor het activeren van soft forks met een automatisch UASF-mechanisme als miners hun steun niet binnen de gestelde tijd signaleren.
---

Ontwikkeld na de debatten over SegWit, die BIP9 gebruikte voor zijn activering, is BIP8 een Soft Fork activeringsmethode die van nature een automatisch UASF (*User-Activated Soft Fork*) mechanisme bevat. Net als BIP9 gebruikt BIP8 Miner signalering, maar voegt de `LOT` (*Lock-in On Time out*) parameter toe. Als `LOT` is ingesteld op `true`, wordt bij het verstrijken van de signaleringsperiode zonder het bereiken van de vereiste drempel, automatisch een UASF geactiveerd, waardoor de Soft Fork geactiveerd wordt. Deze aanpak dwingt mijnwerkers tot samenwerking of riskeert een UASF opgelegd door gebruikers. Bovendien definieert BIP8, in tegenstelling tot BIP9, de signaleringsperiode op basis van blokhoogte, waardoor mogelijke manipulaties via de Hash snelheid door mijnwerkers geëlimineerd worden. BIP8 maakt het ook mogelijk om een variabele stemdrempel in te stellen en introduceert een parameter voor een minimale blokhoogte voor activering, waardoor mijnwerkers tijd hebben om zich voor te bereiden en hun akkoord vooraf te signaleren zonder dat ze per se klaar hoeven te zijn. Wanneer een Soft Fork wordt geactiveerd via BIP8 met de `LOT=true` parameter, gebruikt dit een zeer agressieve methode tegen mijnwerkers die onmiddellijk onder druk worden gezet door een potentiële UASF. Het laat hen inderdaad maar 2 keuzes:


- Wees coöperatief en vergemakkelijk zo het activeringsproces;
- Niet meewerken, in welk geval gebruikers automatisch een UASF uitvoeren om de Soft Fork op te leggen.