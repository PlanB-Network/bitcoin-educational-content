---
term: Timestamp

definition: Mechanisme dat een tijdstip koppelt aan een gebeurtenis om de chronologie van transacties en blokken vast te stellen.
---

Timestamping, of "Timestamp" in het Engels, is een mechanisme om een precieze tijdmarkering te associëren met een gebeurtenis, data of bericht. In de algemene context van computersystemen wordt tijdstempeling gebruikt om de chronologische volgorde van bewerkingen te bepalen en om de integriteit van gegevens in de loop van de tijd te controleren.


In het specifieke geval van Bitcoin worden tijdstempels gebruikt om de chronologie van transacties en blokken vast te stellen. Elk blok in Blockchain bevat een tijdstempel dat de geschatte tijd aangeeft waarop het is aangemaakt. Satoshi Nakamoto heeft het in zijn witboek zelfs over een "tijdstempelserver" om te beschrijven wat we vandaag de dag "Blockchain" zouden noemen. De rol van timestamping op Bitcoin is het bepalen van de chronologie van transacties, zodat zonder tussenkomst van een centrale autoriteit bepaald kan worden welke transactie als eerste aankwam. Dit mechanisme stelt elke gebruiker in staat om te verifiëren of een transactie in het verleden niet heeft plaatsgevonden, en zo te voorkomen dat een kwaadwillende gebruiker een dubbele uitgave doet. Dit mechanisme wordt gerechtvaardigd door Satoshi Nakamoto in zijn Witboek met de beroemde zin: "*Deze standaard is gebaseerd op de Unix-tijd, die staat voor het totale aantal seconden dat is verstreken sinds 1 januari 1970.*"


> ► *Bloktijdstempels zijn relatief flexibel op Bitcoin, omdat een tijdstempel alleen als geldig wordt beschouwd als deze groter is dan de mediaan van de tijd van de 11 voorafgaande blokken (MTP) en kleiner dan de mediaan van de door de knooppunten teruggezonden tijden (voor netwerk gecorrigeerde tijd) plus 2 uur.*