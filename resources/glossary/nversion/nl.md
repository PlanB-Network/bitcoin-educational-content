---
term: nVersion
definition: Veld dat de versie van het transactieformaat aangeeft, noodzakelijk voor het activeren van nSequence.
---

Het `nVersion` veld in een Bitcoin transactie wordt gebruikt om de versie van het gebruikte transactieformaat aan te geven. Het stelt het netwerk in staat om onderscheid te maken tussen verschillende evoluties van het transactieformaat in de tijd en om de bijbehorende regels toe te passen. Dit veld heeft geen invloed op de consensusregels. Dit betekent dat een waarde die aan dit veld wordt toegekend er niet toe leidt dat de transactie ongeldig wordt verklaard. Het `nVersion` veld heeft echter standaardisatieregels die momenteel alleen de waarden `1` en `2` accepteren. Voorlopig is dit veld alleen nuttig voor de activering van het `nSequence` veld.