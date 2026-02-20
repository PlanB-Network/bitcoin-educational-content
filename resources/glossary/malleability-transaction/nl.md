---
term: Malleability (transactie)
definition: Mogelijkheid om de structuur van een transactie te wijzigen zonder het effect ervan te veranderen, maar door de TXID te wijzigen.
---

Verwijst naar de mogelijkheid om de structuur van een Bitcoin transactie lichtjes te wijzigen, zonder het effect ervan te veranderen, maar met wijziging van de transactie-identificatie (*txid*). Deze eigenschap kan kwaadwillig worden misbruikt om belanghebbenden te misleiden over de status van een transactie en zo problemen zoals dubbele uitgaven te veroorzaken. Misleiding werd mogelijk gemaakt door de flexibiliteit van de gebruikte digitale handtekening. De SegWit Soft Fork werd met name geïntroduceerd om deze misleidbaarheid van Bitcoin transacties te voorkomen, waardoor de implementatie van de Lightning Network gecompliceerd werd. Dit wordt bereikt door de vervormbare gegevens van de transactie te verwijderen uit de txid berekening.


> ► *Hoewel zeldzaam, wordt de term "veranderlijkheid" soms gebruikt om naar hetzelfde concept te verwijzen.*