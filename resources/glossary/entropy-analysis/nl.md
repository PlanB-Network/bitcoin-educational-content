---
term: ENTROPIE (ANALYSE)
---

In de specifieke context van ketenanalyse is entropie ook de naam van een indicator, afgeleid van Shannon entropie, uitgevonden door LaurentMT. Deze indicator maakt het mogelijk om het gebrek aan kennis te meten dat analisten hebben over de exacte configuratie van een Bitcoin transactie. Met andere woorden, hoe hoger de entropie van een transactie, hoe moeilijker het wordt voor analisten om de bewegingen van bitcoins tussen inputs en outputs te identificeren.


In de praktijk laat entropie zien of, vanuit het perspectief van een externe waarnemer, een transactie meerdere mogelijke interpretaties heeft, alleen gebaseerd op de hoeveelheden inputs en outputs, zonder rekening te houden met andere externe of interne patronen en heuristieken. Een hoge entropie staat dan synoniem voor een betere vertrouwelijkheid van de transactie.


Entropie wordt gedefinieerd als de binaire logaritme van het aantal mogelijke combinaties. Hier wordt de formule gebruikt waarbij $E$ staat voor de entropie van de transactie en $C$ voor het aantal mogelijke interpretaties:


$$
E = \log_2(C)
$$


Rekening houdend met de waarden van de UTXO's die betrokken zijn bij de transactie, vertegenwoordigt het aantal interpretaties $C$ het aantal manieren waarop inputs geassocieerd kunnen worden met outputs. Met andere woorden, het bepaalt het aantal interpretaties dat een transactie kan oproepen vanuit het gezichtspunt van een externe waarnemer die de transactie analyseert.