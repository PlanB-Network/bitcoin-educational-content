---
term: BYSANTINSKE GENERALERS PROBLEM

---
Problemet ble først formulert av Leslie Lamport, Robert Shostak og Marshall Pease i fagtidsskriftet *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"] (https://lamport.azurewebsites.net/pubs/byz.pdf) i juli 1982. Det brukes i dag for å illustrere utfordringene når det gjelder beslutningstaking i et distribuert system som ikke kan stole på noen aktør.

I denne metaforen har en gruppe bysantinske generaler og deres respektive hærer slått leir rundt en by som de ønsker å angripe eller beleire. Generalene er geografisk adskilt fra hverandre og må kommunisere via budbringere for å koordinere strategien. Om de angriper eller trekker seg tilbake spiller ingen rolle, så lenge alle generalene blir enige.

Derfor kan vi vurdere følgende krav:


- Hver general må ta en avgjørelse: angripe eller trekke seg tilbake (ja eller nei);
- Når beslutningen først er tatt, kan den ikke endres;
- Alle generalene må være enige om den samme beslutningen og utføre den synkront.

Dessuten kan en general bare kommunisere med en annen gjennom meldinger som sendes av en kurer, og disse kan bli forsinket, ødelagt, endret eller gå tapt. Og selv om en melding blir levert, kan en eller flere generaler velge (av en eller annen grunn) å svikte den etablerte tilliten og sende en falsk melding, noe som kan skape kaos.

Hvis vi overfører dilemmaet til Bitcoin-blokkjeden, representerer hver general en node i nettverket som må oppnå konsensus om systemets tilstand. Med andre ord må flertallet av deltakerne i et distribuert nettverk være enige og utføre den samme handlingen for å unngå total fiasko. Den eneste måten å oppnå konsensus på i denne typen distribuerte systemer er at minst 2/3 av nettverksnodene er pålitelige og ærlige. Derfor er systemet sårbart hvis flertallet av nettverksdeltakerne bestemmer seg for å handle ondsinnet.

> dette dilemmaet kalles også "problemet med pålitelig kringkasting"