---
term: Replay attack
definition: Aanval waarbij een geldige transactie van de ene blockchain wordt gereproduceerd op een andere die dezelfde geschiedenis deelt.
---

In de context van Bitcoin treedt een replay aanval op wanneer een geldige transactie op een Blockchain kwaadwillig wordt gereproduceerd op een andere Blockchain die dezelfde transactiegeschiedenis heeft. Met andere woorden, een transactie die op het ene kanaal wordt uitgezonden, kan op een ander kanaal worden gereproduceerd zonder toestemming van de verzender van de eerste transactie.


Laten we het voorbeeld nemen van een hypothetische Hard Fork uit Bitcoin, genaamd "*BitcoinBis*". Als je een betaling doet in bitcoins om een baguette te kopen van een bakker op het echte Blockchain Bitcoin, zou diezelfde bakker die legitieme transactie kunnen herspelen op *BitcoinBis* om hetzelfde bedrag in cryptocurrencies te krijgen op dit Fork, zonder enige actie van jouw kant.


Dit type aanval kan alleen voorkomen bij Blockchain vertakkingen met 2 onafhankelijke ketens die in de tijd blijven bestaan. Dit zou typisch het geval zijn bij Hard Fork. Om een replay aanval mogelijk te maken, moeten de 2 blockchains een gemeenschappelijke geschiedenis hebben, en de gedupliceerde transactie moet als input UTXO's gebruiken die gemaakt zijn van eerdere transacties die plaatsvonden voordat de twee ketens splitsten, of van eerdere transacties die zelf al gereplayed zijn in een eerdere replay aanval.


Over het algemeen bestaat een replay-aanval in computers uit het onderscheppen en hergebruiken van geldige gegevens om een systeem te misleiden door de oorspronkelijke overdracht te herhalen. Dit kan soms leiden tot identiteitsdiefstal op een netwerk.


> ► *In het geval van een replay aanval op een Bitcoin transactie, wordt dit soms simpelweg een "replay transactie" genoemd. "*