---
term: Ronde betaling
definition: Heuristiek voor ketenanalyse die de betaling identificeert aan de hand van het ronde bedrag in een transactie.
---

Een interne heuristiek voor ketenanalyse op Bitcoin die een hypothese mogelijk maakt over de aard van de uitgangen van een transactie gebaseerd op ronde bedragen. In het algemeen, wanneer we worden geconfronteerd met een eenvoudig betalingspatroon (1 input en 2 outputs), als een van de outputs een rond bedrag uitgeeft, dan vertegenwoordigt het de betaling. Door eliminatie, als een uitgang de betaling vertegenwoordigt, vertegenwoordigt de andere de verandering. Daarom kan worden geïnterpreteerd dat het waarschijnlijk is dat de gebruiker die de transactie invoert nog steeds de uitgang bezit die is geïdentificeerd als het wisselgeld.


Opgemerkt moet worden dat deze heuristiek niet altijd van toepassing is, omdat de meeste betalingen nog steeds in fiatvaluta worden gedaan. Sterker nog, wanneer een winkelier in Frankrijk Bitcoin accepteert, geeft hij over het algemeen geen stabiele prijzen in Sats weer. Ze kiezen liever voor een conversie tussen de prijs in euro's en het bedrag in bitcoins dat moet worden betaald via hun verkooppunt (zoals BTCPay Server, bijvoorbeeld). Daarom zou er geen rond getal in de transactie-uitvoer moeten staan. Toch zou een analist kunnen proberen om deze conversie te maken door rekening te houden met de Exchange koers die van kracht was toen de transactie werd uitgezonden op het netwerk. Als op een dag Bitcoin de voorkeurs rekeneenheid wordt in onze uitwisselingen, kan deze heuristiek nog nuttiger worden voor analyses.


