---
term: P2PKH
---

P2PKH staat voor *Betalen aan Openbare Sleutel Hash*. Het is een standaard scriptmodel dat wordt gebruikt om bestedingsvoorwaarden op een UTXO vast te stellen. Het maakt het mogelijk om bitcoins vast te zetten op een Hash van een publieke sleutel, dus op een ontvangende Address. Dit script wordt geassocieerd met de Legacy-standaard en werd geïntroduceerd in de vroege versies van Bitcoin door Satoshi Nakamoto.


In tegenstelling tot P2PK, waar de openbare sleutel expliciet in het script is opgenomen, gebruikt P2PKH een cryptografische vingerafdruk van de openbare sleutel. Dit script bevat de `RIPEMD160` Hash van de `SHA256` van de openbare sleutel en bepaalt dat, om toegang te krijgen tot het geld, de ontvanger een openbare sleutel moet verstrekken die overeenkomt met deze Hash, evenals een geldige digitale handtekening gegenereerd uit de bijbehorende privésleutel. P2PKH adressen zijn gecodeerd met het `Base58Check` formaat, wat ze robuust maakt tegen typografische fouten door het gebruik van een controlesom. Deze adressen beginnen altijd met het getal `1`.