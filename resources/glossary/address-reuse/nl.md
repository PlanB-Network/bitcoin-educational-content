---
term: Adreshergebruik
definition: Een ongeraden praktijk van het meerdere keren gebruiken van hetzelfde Bitcoin-adres voor het ontvangen van betalingen, wat privacy schaadt door het mogelijk maken van het traceren van middelen.
---

Address hergebruik verwijst naar de praktijk om dezelfde ontvangende Address te gebruiken om meerdere UTXO's te blokkeren, soms binnen verschillende transacties. Bitcoins worden meestal geblokkeerd met een cryptografisch sleutelpaar dat overeenkomt met een unieke Address. Aangezien de Blockchain openbaar is, is het eenvoudig te zien welke adressen bij hoeveel bitcoins horen. Omdat de Blockchain openbaar is, is het eenvoudig om te zien welke adressen geassocieerd zijn met hoeveel bitcoins. In het geval van hergebruik van dezelfde Address voor meerdere betalingen, is het redelijk om je voor te stellen dat alle geassocieerde UTXO's aan dezelfde entiteit toebehoren. Daarom vormt hergebruik van Address een probleem voor de privacy van de gebruiker. Het maakt deterministische koppelingen tussen meerdere transacties en UTXO's mogelijk, en bestendigt het volgen van On-Chain fondsen. Satoshi Nakamoto noemde dit probleem al in zijn witboek:


> *Als extra firewall moet voor elke transactie een nieuw sleutelpaar worden gebruikt om te voorkomen dat ze aan een gemeenschappelijke eigenaar worden gekoppeld.*


Nakamoto, S. (2008). "*Bitcoin: A Peer-to-Peer Electronic Cash System*". https://bitcoin.org/bitcoin.pdf.

Om de privacy minimaal te houden, is het sterk aan te raden om elke ontvangen Address slechts één keer te gebruiken. Voor elke nieuwe betaling is het gepast om generate een nieuwe Address te geven. Voor uitvoer van wijzigingen moet ook een nieuwe Address worden gebruikt. Gelukkig is het dankzij deterministische en hiërarchische wallets erg gemakkelijk geworden om een veelheid aan adressen te gebruiken. Alle sleutelparen die geassocieerd zijn met een Wallet kunnen eenvoudig opnieuw gegenereerd worden vanaf de seed. Dit is ook de reden waarom Wallet software altijd een nieuwe, andere Address genereert wanneer je op de knop "Ontvangen" klikt.

