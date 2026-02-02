---
term: P2SH-P2WSH
definition: SegWit-script (P2WSH) verpakt in P2SH voor compatibiliteit, adressen beginnen met 3.
---

P2SH-P2WSH staat voor *Betalen aan Script Hash - Betalen aan Getuige Script Hash*. Het is een standaard scriptmodel dat gebruikt wordt om bestedingsvoorwaarden vast te stellen op een UTXO, ook bekend als "Geneste SegWit".


P2SH-P2WSH werd geïntroduceerd met de implementatie van SegWit in augustus 2017. Dit script beschrijft een P2WSH verpakt in een P2SH. Het vergrendelt bitcoins op basis van de Hash van een script. Het verschil met een klassieke P2WSH is dat het script is gewikkeld in de `redeemscript` van een klassieke P2SH.


Dit script is gemaakt bij de lancering van SegWit om de adoptie ervan te vergemakkelijken. Het maakt het gebruik van deze nieuwe standaard mogelijk, zelfs met diensten of wallets die nog niet compatibel zijn met SegWit. Vandaag de dag is het daarom niet meer zo relevant om dit soort ingepakte SegWit scripts te gebruiken, aangezien de meeste wallets native SegWit hebben geïmplementeerd. P2SH-P2WSH adressen worden geschreven met `Base58Check` codering en beginnen altijd met `3`, zoals alle P2SH Address adressen.