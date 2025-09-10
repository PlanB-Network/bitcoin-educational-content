---
name: PayJoin
description: Wat is een PayJoin op Bitcoin?
---
![Payjoin thumbnail - steganography](assets/cover.webp)








## PayJoin Transacties op Bitcoin begrijpen


PayJoin is een specifieke structuur van de Bitcoin transactie die de privacy van de gebruiker tijdens een betaling verbetert door samen te werken met de ontvanger van de betaling.


In 2015 noemde [LaurentMT](https://twitter.com/LaurentMT) deze methode voor het eerst "steganografische transacties" in een document dat [hier](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt) toegankelijk is. Deze techniek werd later overgenomen door de Samourai Wallet, die de eerste client werd die het implementeerde met de Stowaway tool in 2018. Het concept van PayJoin wordt ook gevonden in [BIP79](https://github.com/Bitcoin/bips/blob/master/bip-0079.mediawiki) en [BIP78](https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki). Er worden verschillende termen gebruikt om naar PayJoin te verwijzen:


- PayJoin
- Verstekeling
- P2EP (Pay-to-End-Point)
- Steganografische transactie


Het unieke van PayJoin ligt in de mogelijkheid om generate een transactie te laten uitvoeren die op het eerste gezicht gewoon lijkt, maar eigenlijk een mini CoinJoin is tussen twee partijen. Om dit te bereiken betrekt de transactiestructuur de ontvanger van de betaling naast de feitelijke verzender in de invoer. De ontvanger neemt een betaling aan zichzelf op in het midden van de transactie, waardoor hij betaald kan worden.


Laten we een concreet voorbeeld nemen: als je een stokbrood koopt voor `4000 Sats` met een UTXO van `10.000 Sats` en je kiest voor een PayJoin, dan zal je bakker een UTXO van `15.000 Sats` toevoegen die bij hen hoort als input, die ze volledig zullen ontvangen als output, bovenop jouw `4000 Sats`:

![Payjoin transaction diagram](assets/en/1.webp)


In dit voorbeeld voert de bakker `15.000 Sats` in als input en komt uit met `19.000 Sats`, met een verschil van precies `4000 Sats`, wat de prijs van het stokbrood is. Aan jouw kant voer je `10.000 Sats` in en komt uit op `6.000 Sats` als output, wat neerkomt op een saldo van `-4000 Sats`, wat de prijs van het stokbrood is. Om het voorbeeld te vereenvoudigen, heb ik de Mining kosten in deze transactie bewust weggelaten.


## Wat is het doel van een PayJoin transactie?


Een PayJoin transactie dient twee doelen die gebruikers in staat stellen om de privacy van hun betaling te verbeteren.

Ten eerste heeft PayJoin als doel een externe waarnemer te misleiden door een lokvogel te creëren in de ketenanalyse. Dit wordt mogelijk gemaakt door de Common Input Ownership Heuristic (CIOH). Gewoonlijk, wanneer een transactie op Blockchain meerdere ingangen heeft, wordt aangenomen dat al deze ingangen waarschijnlijk toebehoren aan dezelfde entiteit of gebruiker. Dus, wanneer een analist een PayJoin transactie onderzoekt, wordt hem wijsgemaakt dat alle inputs van dezelfde persoon afkomstig zijn. Deze perceptie is echter onjuist omdat de ontvanger van de betaling ook inputs bijdraagt naast de daadwerkelijke betaler. Daarom wordt de ketenanalyse afgeleid naar een interpretatie die onjuist blijkt te zijn.


PayJoin maakt het ook mogelijk om een externe waarnemer te misleiden over het werkelijke bedrag van de betaling die is gedaan. Door de transactiestructuur te bekijken, zou de analist kunnen geloven dat de betaling gelijk is aan het bedrag van een van de outputs. In werkelijkheid komt het bedrag van de betaling echter niet overeen met een van de outputs. Het is eigenlijk het verschil tussen de output UTXO van de ontvanger en de input UTXO van de ontvanger. In die zin valt de PayJoin transactie onder steganografie. Het maakt het mogelijk om het werkelijke bedrag van een transactie te verbergen in een valse transactie die als afleiding dient.


Let op onze definitie van **Stenografie**:

> Steganografie is een techniek om informatie op zo'n manier in andere gegevens of objecten te verbergen dat de aanwezigheid van de verborgen informatie niet waarneembaar is. Een geheime boodschap kan bijvoorbeeld verborgen worden in een punt in een tekst die er niets mee te maken heeft, waardoor het niet met het blote oog waarneembaar is (dit is de techniek van micropoint). In tegenstelling tot encryptie, die informatie onbegrijpelijk maakt zonder de decryptiesleutel, verandert steganografie de informatie niet. Het blijft in het zicht. Het doel is eerder om het bestaan van de geheime boodschap te verbergen, terwijl encryptie duidelijk de aanwezigheid van verborgen informatie onthult, hoewel deze ontoegankelijk is zonder de sleutel.

Laten we teruggaan naar ons voorbeeld van een PayJoin transactie voor de betaling van een baguette.

![Payjoin transaction schema from the outside](assets/en/2.webp)

Bij het zien van deze transactie op Blockchain, zou een externe waarnemer die de gebruikelijke heuristieken van ketenanalyse volgt, het als volgt interpreteren: "*Alice voegde 2 UTXO's samen als input van de transactie om `19.000 Sats` te betalen aan Bob*."

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

Deze interpretatie is duidelijk onjuist omdat, zoals je al weet, de twee ingevoerde UTXO's niet aan dezelfde persoon toebehoren. Bovendien is de werkelijke waarde van de betaling niet `19.000 Sats`, maar eerder `4.000 Sats`. De analyse van de externe waarnemer is dus gericht op een foutieve conclusie, waardoor de privacy van de belanghebbenden gewaarborgd blijft.![PayJoin transactiediagram](assets/nl/1.webp)

Als je een echte PayJoin transactie wilt analyseren, hier is er een die ik heb uitgevoerd op de Testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://Mempool.space/fr/Testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)







**Externe bronnen:**


- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki.
- https://payjoin.org/
https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

