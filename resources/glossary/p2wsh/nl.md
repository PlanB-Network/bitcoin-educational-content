---
term: P2WSH
definition: Native SegWit-script dat bitcoins vergrendelt op de hash van een script, bc1q-adressen.
---

P2WSH staat voor *Pay to Witness Script Hash*. Het is een standaard scriptmodel dat wordt gebruikt om bestedingsvoorwaarden op een UTXO vast te stellen. P2WSH werd geïntroduceerd met de implementatie van SegWit in augustus 2017.


Dit script lijkt op P2SH (*Betalen aan Publiek Script Hash*), omdat het ook bitcoins vergrendelt op basis van de Hash van een script. Het verschil zit hem in de manier waarop handtekeningen en scripts worden opgenomen in de transactie. Om de bitcoins uit te geven aan dit type script, moet de ontvanger het originele script leveren, genaamd `witnessScript` (gelijk aan `redeemscript`), samen met de vereiste handtekeningen. Dit mechanisme maakt het mogelijk om meer geavanceerde bestedingsvoorwaarden te implementeren, zoals multisigs.


In de context van P2WSH wordt de handtekening script informatie (het `scriptWitness`, gelijkwaardig aan `scriptSig`) verplaatst van de traditionele transactie structuur naar een aparte sectie genaamd `Witness`. Deze verplaatsing is een eigenschap van de SegWit (*Gesegregeerde Getuige*) update die helpt om vervalsing van handtekeningen te voorkomen. P2WSH transacties zijn over het algemeen goedkoper in termen van kosten vergeleken met Legacy transacties, omdat het deel in de getuige minder kost.


P2WSH adressen worden geschreven met `Bech32` codering met een checksum in de vorm van BCH code. Deze adressen beginnen altijd met `bc1q`. P2WSH is een versie 0 SegWit uitvoer.