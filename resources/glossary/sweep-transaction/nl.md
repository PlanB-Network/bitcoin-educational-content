---
term: Sweep-transactie
definition: Transactiepatroon met een enkele UTXO input en een enkele output, kenmerkend voor een zelfoverdracht.
---

Patroon- of transactiemodel dat wordt gebruikt bij ketenanalyse om de aard van de transactie te bepalen. Dit model wordt gekenmerkt door de consumptie van een enkele UTXO als input en de productie van een enkele UTXO als output. De interpretatie van dit model is dat we te maken hebben met een zelfoverdracht. De gebruiker heeft zijn bitcoins aan zichzelf overgedragen, naar een andere Address die hij bezit. Aangezien er geen verandering is in de transactie, is het zeer onwaarschijnlijk dat we te maken hebben met een betaling. Bij een betaling is het namelijk bijna onmogelijk voor de betaler om een UTXO te hebben die precies overeenkomt met het bedrag dat de verkoper nodig heeft, naast de transactiekosten. Over het algemeen wordt de betaler daarom gedwongen om een wisselgeldoutput te produceren. We weten dan dat de waargenomen gebruiker waarschijnlijk nog steeds in het bezit is van deze UTXO. In de context van een ketenanalyse, als we weten dat het UTXO dat gebruikt is als input in de transactie, toebehoort aan Alice, kunnen we aannemen dat het UTXO in de output ook aan haar toebehoort.





