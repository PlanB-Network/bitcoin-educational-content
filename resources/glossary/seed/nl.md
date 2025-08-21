---
term: GRAAN
---

In de specifieke context van een hiërarchische deterministische Bitcoin portefeuille is een seed een 512-bit stukje informatie afgeleid van een willekeurige gebeurtenis. Het wordt gebruikt om deterministisch en hiërarchisch generate een set van private sleutels, en hun corresponderende publieke sleutels, voor een Bitcoin portfolio. De seed wordt vaak verward met de herstelzin zelf. Maar het is niet hetzelfde. De seed wordt verkregen door de `PBKDF2` functie toe te passen op de Mnemonic zin en elke passphrase.


De seed werd uitgevonden met BIP32, dat de basis legde voor de hiërarchische deterministische portfolio. In deze standaard mat de seed 128 bits. Hierdoor kunnen alle sleutels in een portfolio worden afgeleid uit een enkel stuk informatie, in tegenstelling tot JBOK (*Just a Bunch Of Keys*) portfolio's, die nieuwe back-ups vereisen voor elke gegenereerde sleutel. BIP39 stelde vervolgens een codering voor van deze seed, om het lezen ervan door mensen te vereenvoudigen. Deze codering heeft de vorm van een woordgroep, over het algemeen een Mnemonic woordgroep of herstelwoordgroep genoemd. Deze standaard voorkomt fouten bij het opslaan van de seed, vooral dankzij het gebruik van een checksum.


Buiten de context van Bitcoin, in cryptografie in het algemeen, is een seed een initiële waarde die gebruikt wordt om generate cryptografische sleutels, of ruimer, elk type van gegevens geproduceerd door een pseudo-willekeurige getallengenerator. Deze initiële waarde moet willekeurig en onvoorspelbaar zijn om de veiligheid van het cryptografisch systeem te garanderen. seed introduceert inderdaad entropie in het systeem, maar het generatieproces dat volgt is deterministisch.


> ► *In het gewone spraakgebruik verwijst de meerderheid van de bitcoiners naar de Mnemonic zin als ze het hebben over de "seed", en niet naar de tussenliggende afleidingstoestand die ligt tussen de Mnemonic zin en de hoofdsleutel.*