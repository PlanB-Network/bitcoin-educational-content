---
term: P2WPKH
definition: Native SegWit-script dat bitcoins vergrendelt op de hash van een publieke sleutel, bc1q-adressen.
---

P2WPKH staat voor *Pay to Witness Public Key Hash*. Het is een standaard scriptmodel dat wordt gebruikt om bestedingsvoorwaarden vast te stellen voor een UTXO. P2WPKH werd geïntroduceerd met de implementatie van SegWit in augustus 2017.


Dit script lijkt op P2PKH (*Betalen aan Openbare Sleutel Hash*), omdat het ook bitcoins vergrendelt op basis van de Hash van een openbare sleutel, dus een ontvangende Address. Het verschil zit in de manier waarop handtekeningen en scripts worden opgenomen in de transactie. In het geval van P2WPKH is de informatie over het handtekeningscript (`scriptSig`) verplaatst van de traditionele transactiestructuur naar een aparte sectie genaamd `Witness`. Deze verplaatsing is een eigenschap van de SegWit (*Gesegregeerde Getuige*) update die helpt om vervalsing van handtekeningen te voorkomen. P2WPKH transacties zijn over het algemeen goedkoper in termen van kosten vergeleken met Legacy transacties, omdat het deel in de getuige minder kost.


P2WPKH adressen worden geschreven met `Bech32` codering met een checksum in de vorm van BCH code. Deze adressen beginnen altijd met `bc1q`. P2WPKH is een versie 0 SegWit uitgang.