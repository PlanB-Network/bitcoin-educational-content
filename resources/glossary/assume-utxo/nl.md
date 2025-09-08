---
term: ASSUME UTXO
---

Een configuratieparameter in de toonaangevende Bitcoin core client die een knooppunt dat net geïnitialiseerd is (maar nog niet de IBD heeft ondergaan) toestaat om de verificatie van transacties en de UTXO set uit te stellen tot een bepaalde momentopname. Het concept is gebaseerd op het gebruik van een UTXO set (een lijst van alle bestaande UTXO's op een bepaald moment) die door Core wordt geleverd en die verondersteld wordt accuraat te zijn, waardoor de node zeer snel gesynchroniseerd kan worden met de keten met het meeste geaccumuleerde werk. Omdat het knooppunt de langdurige IBD-stap overslaat, wordt het zeer snel operationeel voor de gebruiker. Stel dat UTXO de synchronisatie (IBD) in twee delen verdeelt:


- Eerst voert het knooppunt de Header First Sync uit (verificatie van alleen headers) en beschouwt het de UTXO set die door Core is verstrekt als geldig;
- Daarna, als het eenmaal operationeel is, zal het knooppunt op de achtergrond de complete blokgeschiedenis verifiëren en een nieuwe UTXO set bijwerken die het zelf heeft geverifieerd. Als deze nieuwe UTXO set niet overeenkomt met de set die door Core is geleverd, zal er een foutmelding worden gegeven.


Stel daarom dat UTXO de voorbereiding van een nieuw Bitcoin knooppunt versnelt door het transactieverificatieproces uit te stellen en de UTXO set via een bijgewerkte momentopname in Core.