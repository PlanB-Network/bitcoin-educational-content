---
term: P2SH
---

P2SH staat voor *Pay to Script Hash*. Het is een standaard scriptmodel dat wordt gebruikt om de bestedingsvoorwaarden op een UTXO vast te stellen. In tegenstelling tot P2PK- en P2PKH-scripts, waarbij de bestedingsvoorwaarden vooraf zijn gedefinieerd, kunnen met P2SH willekeurige bestedingsvoorwaarden en aanvullende functionaliteiten in een transactiescript worden geïntegreerd.


Technisch gezien bevat de `scriptPubKey` in een P2SH transactie de cryptografische Hash van een `redeemscript`, in plaats van expliciete bestedingsvoorwaarden. Deze Hash wordt verkregen met een `SHA256` Hash. Bij het versturen van bitcoins naar een P2SH Address, wordt de onderliggende `redeemscript` niet onthuld. Alleen de Hash wordt meegenomen in de transactie. P2SH adressen zijn gecodeerd in `Base58Check` en beginnen met het nummer `3`. Wanneer de ontvanger de ontvangen bitcoins wil uitgeven, moet hij een `redeemscript` opgeven die overeenkomt met de Hash in de `scriptPubKey`, samen met de benodigde gegevens om aan de voorwaarden van deze `redeemscript` te voldoen. In een P2SH script met meerdere handtekeningen zou het script bijvoorbeeld handtekeningen van meerdere privésleutels kunnen vereisen.


Het gebruik van P2SH biedt meer flexibiliteit, omdat het de constructie van willekeurige scripts mogelijk maakt zonder dat de verzender de details kent. P2SH werd in 2012 geïntroduceerd met BIP16.