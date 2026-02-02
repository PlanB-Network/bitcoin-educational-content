---
term: Payjoin
definition: Collaboratieve transactie die de privacy verbetert door de ontvanger op te nemen in de inputs.
---

Een specifieke Bitcoin transactiestructuur die de privacy van de gebruiker tijdens een uitgave verbetert door samen te werken met de ontvanger van de betaling. Het unieke van PayJoin ligt in de mogelijkheid om generate een transactie te maken die er op het eerste gezicht gewoon uitziet, maar eigenlijk een mini CoinJoin is tussen twee partijen. Hiervoor betrekt de transactiestructuur de ontvanger van de betaling in de inputs naast de eigenlijke verzender. De ontvanger voegt dus een betaling aan zichzelf toe in het midden van de transactie, waardoor hij betaald kan worden. Bijvoorbeeld, als je een stokbrood koopt voor `6.000 Sats` met een UTXO van `10.000 Sats`, en je kiest voor een PayJoin, dan voegt de bakker een UTXO van `15.000 Sats` aan hen toe als input, die ze volledig terugkrijgen als output, naast jouw `6.000 Sats`.


De PayJoin transactie vervult twee doelen. Ten eerste is het bedoeld om een externe waarnemer te misleiden door een lokvogel te creëren in de ketenanalyse op de Common Input Ownership Heuristic (CIOH). Wanneer een transactie op de Blockchain meerdere ingangen heeft, wordt meestal aangenomen dat al deze ingangen waarschijnlijk tot dezelfde entiteit behoren. Dus wanneer een analist een PayJoin transactie onderzoekt, denkt hij dat alle inputs van dezelfde persoon afkomstig zijn. Deze perceptie is echter onjuist, omdat de ontvanger van de betaling ook bijdraagt aan de inputs naast de daadwerkelijke betaler. Ten tweede misleidt de PayJoin een externe waarnemer ook over het werkelijke bedrag van de betaling. Door de structuur van de transactie te bekijken, zou de analist kunnen denken dat de betaling gelijk is aan het bedrag van een van de outputs. In werkelijkheid komt het bedrag van de betaling met geen van de outputs overeen. Het is eigenlijk het verschil tussen de UTXO van de ontvanger in de output en de UTXO van de ontvanger in de input. In dit geval valt de PayJoin transactie onder steganografie. Het maakt het mogelijk om het werkelijke bedrag van een transactie te verbergen in een valse transactie die als afleiding dient.





> *PayJoin wordt soms ook "P2EP (Pay-to-End-Point)", "Stowaway" of "steganografische transactie" genoemd.*