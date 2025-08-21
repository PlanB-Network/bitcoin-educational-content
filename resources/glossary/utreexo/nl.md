---
term: UTREEXO
---

Protocol ontworpen door Tadge Dryja om de UTXO verzameling van Bitcoin knooppunten te comprimeren met behulp van een accumulator gebaseerd op Merkle bomen. In tegenstelling tot de klassieke UTXO set die veel opslagruimte vereist, vermindert Utreexo het benodigde geheugen drastisch door alleen de Merkle Tree wortels op te slaan. Hierdoor kan het knooppunt het bestaan van UTXO's die gebruikt worden in transactie-inputs verifiëren, zonder de complete set UTXO's te hoeven bewaren. Door Utreexo te gebruiken, bewaart elk knooppunt alleen een cryptografische vingerafdruk die Merkle Root wordt genoemd. Wanneer een transactie wordt gedaan, levert de gebruiker de bewijzen van Ownership van de UTXO's en de bijbehorende Merkle-paden. Zo kan het knooppunt transacties verifiëren zonder de hele UTXO set op te slaan. Laten we een voorbeeld nemen met een diagram om dit mechanisme te begrijpen:


![](../../dictionnaire/assets/15.webp)


In dit voorbeeld heb ik met opzet de UTXO set gereduceerd tot 4 UTXO's om het begrip te vergemakkelijken. In werkelijkheid is het belangrijk om je voor te stellen dat er bijna 140 miljoen UTXO's op Bitcoin staan op het moment dat je deze regels schrijft. In dit diagram hoeft de Utreexo node alleen Merkle Root in RAM te houden. Als het een transactie ontvangt die UTXO nr. 3 (in zwart) uitgeeft, zou het bewijs bestaan uit het volgende Elements:


- UTXO 3;
- Hash 4;
- Hash 1-2.


Met deze door de transactieverzender verzonden informatie voert het Utreexo-knooppunt de volgende verificaties uit:


- Het berekent de afdruk van UTXO 3, wat Hash 3 oplevert;
- Het verbindt Hash 3 met Hash 4;
- Het berekent hun imprint, waardoor het Hash 3-4 krijgt;
- Het verbindt Hash 3-4 met Hash 1-2;
- Het berekent hun afdruk, waardoor het de Merkle Root krijgt.


Als de Merkle Root die het via zijn proces verkrijgt dezelfde is als de Merkle Root die het in zijn RAM heeft opgeslagen, dan is het ervan overtuigd dat UTXO nr. 3 inderdaad deel uitmaakt van de UTXO set.

Deze methode vermindert de RAM-vereisten voor Full node operators. Utreexo heeft echter beperkingen, waaronder een toename van de blokgrootte door extra bewijzen en de mogelijke afhankelijkheid van Utreexo-knooppunten van brugknooppunten om ontbrekende bewijzen te verkrijgen. Brugknooppunten zijn traditionele volledige knooppunten die de nodige bewijzen leveren aan Utreexo-knooppunten, waardoor volledige verificatie mogelijk is. Deze aanpak biedt een compromis tussen efficiëntie en decentralisatie, waardoor transactievalidatie toegankelijker wordt voor gebruikers met beperkte middelen.