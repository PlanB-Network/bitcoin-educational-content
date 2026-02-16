---
term: Resynchronisatie
definition: Vervanging van een deel van de blockchain door een concurrerende keten met meer geaccumuleerd werk.
---

Verwijst naar een fenomeen waarbij de Blockchain een verandering van zijn structuur ondergaat door het bestaan van concurrerende blokken op dezelfde hoogte. Dit gebeurt wanneer een deel van de Blockchain wordt vervangen door een andere keten met een grotere hoeveelheid geaccumuleerd werk.


Deze hersynchronisaties maken deel uit van de natuurlijke werking van Bitcoin, waarbij verschillende miners bijna gelijktijdig nieuwe blokken kunnen vinden, waardoor het Bitcoin netwerk in tweeën wordt gesplitst. In zulke gevallen kan het netwerk zich tijdelijk opsplitsen in concurrerende ketens. Uiteindelijk, wanneer één van deze ketens meer werk verzamelt, worden de andere ketens verlaten door de nodes en worden hun blokken zogenaamde "verouderde blokken" of "weesblokken" Dit proces van het vervangen van een keten door een andere is resynchronisatie.





Hersynchronisaties kunnen verschillende gevolgen hebben. Ten eerste, als een gebruiker een transactie bevestigd had in een blok dat verlaten blijkt te zijn, maar deze transactie wordt niet teruggevonden in de uiteindelijk geldige keten, dan wordt zijn transactie opnieuw onbevestigd. Daarom wordt geadviseerd om altijd minstens 6 bevestigingen af te wachten om een transactie als echt onveranderlijk te beschouwen. Na 6 blokken diep zijn hersynchronisaties zo onwaarschijnlijk dat de kans dat er één optreedt als vrijwel nihil kan worden beschouwd.


Bovendien betekenen hersynchronisaties op globaal systeemniveau een verspilling van de rekenkracht van de mijnwerkers. Bij een splitsing zullen sommige mijnwerkers on chain `A` zijn en andere on chain `B`. Als keten `B` uiteindelijk verlaten wordt tijdens een hersynchronisatie, dan is alle rekenkracht van de mijnwerkers op deze keten per definitie verspild. Als er te veel hersynchronisaties zijn op het Bitcoin netwerk, wordt de algemene veiligheid van het netwerk dus verminderd. Dit is deels de reden waarom het vergroten van de blokgrootte of het verkleinen van het interval tussen elk blok (10 minuten) gevaarlijk kan zijn.


> sommige bitcoiners gebruiken liever "Orphan block" om te verwijzen naar een verlopen blok. En hoewel het een anglicisme is, wordt in de omgangstaal vaak de voorkeur gegeven aan "reorganisatie" of "reorg" boven "hersynchronisatie"