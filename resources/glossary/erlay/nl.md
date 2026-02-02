---
term: Erlay
definition: Protocol dat de efficiëntie van transactiedoorgifte verbetert om het bandbreedteverbruik te verminderen.
---

Voorgesteld netwerkprotocol om de efficiëntie van het doorgeven van onbevestigde transacties tussen Bitcoin knooppunten te verbeteren.


Momenteel wordt elke transactie verspreid via een systeem waarbij elk knooppunt de transactie waarvan het op de hoogte is naar al zijn peers uitzendt. Het probleem is dat dit leidt tot veel redundantie en bandbreedtegebruik voor duplicaten. Veel transactie broadcasts zijn onnodig, omdat de ontvanger al op de hoogte is van deze transacties, en elk knooppunt hoeft maar één keer op de hoogte te zijn van elke transactie. Erlay stelt voor om het aantal peers waarnaar een node direct transacties verstuurt waarvan het op de hoogte is standaard te beperken tot 8 en vervolgens een verzoeningsproces te gebruiken op basis van de minisketch bibliotheek om ontbrekende transacties efficiënter te delen.


Erlay zou het bandbreedtegebruik met ongeveer 40% verminderen, waardoor de Full node werking toegankelijker zou worden voor gebruikers met beperkte internetverbindingen en zo een betere netwerkdecentralisatie zou bevorderen. Dit protocol zou ook een bijna constant bandbreedteverbruik hebben als het aantal verbindingen toeneemt. Dit betekent dat het voor knooppuntbeheerders veel eenvoudiger zou zijn om een zeer groot aantal verbindingen van hun peers te accepteren, wat de veiligheid van het Bitcoin netwerk zou verhogen door het risico van opzettelijke of onopzettelijke partitionering te verminderen. Daarnaast zou Erlay het moeilijker maken om te bepalen van welk knooppunt een transactie afkomstig is, waardoor de vertrouwelijkheid voor gebruikers van knooppunten die niet onder Tor werken toeneemt.


Erlay wordt voorgesteld in BIP330.