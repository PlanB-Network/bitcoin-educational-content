---
term: Stack
definition: LIFO-datastructuur die in Bitcoin Script wordt gebruikt om tijdelijke elementen op te slaan en te manipuleren tijdens de uitvoering.
---

In de context van de scripttaal die gebruikt wordt om bestedingsvoorwaarden toe te voegen aan Bitcoin UTXO's, is de stack een LIFO (*Last In, First Out*) datastructuur die gebruikt wordt om tijdelijke Elements op te slaan tijdens de uitvoering van het script. Elke bewerking in het script manipuleert deze stapels, waarbij Elements kan worden toegevoegd (*push*) of verwijderd (*pop*). Scripts gebruiken stacks om uitdrukkingen te evalueren, tijdelijke variabelen op te slaan en voorwaarden te beheren.


Bij het uitvoeren van een Bitcoin script kunnen 2 stapels gebruikt worden: de hoofdstapel en de alt (alternatieve) stapel. De hoofdstapel wordt gebruikt voor de meeste scriptbewerkingen. Het is op deze stack dat scriptbewerkingen gegevens toevoegen, verwijderen of manipuleren. De alternatieve stack daarentegen wordt gebruikt om gegevens tijdelijk op te slaan tijdens de uitvoering van het script. Met specifieke opcodes, zoals `OP_TOALTSTACK` en `OP_FROMALTSTACK`, kun je Elements overbrengen van de hoofd-stack naar de alternatieve stack en vice versa.


Wanneer een transactie bijvoorbeeld gevalideerd wordt, worden handtekeningen en publieke sleutels naar de hoofdstapel geduwd en verwerkt door opeenvolgende opcodes om te verifiëren dat de handtekeningen overeenkomen met de transactiesleutels en gegevens.