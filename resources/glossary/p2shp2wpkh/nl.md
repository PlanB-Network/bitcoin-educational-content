---
term: P2SH-P2WPKH
---

P2SH-P2WPKH staat voor *Betalen aan Script Hash - Betalen aan Getuige Openbare Sleutel Hash*. Het is een standaard scriptmodel dat gebruikt wordt om bestedingsvoorwaarden vast te stellen op een UTXO, ook bekend als "Geneste SegWit".


P2SH-P2WPKH werd geïntroduceerd met de implementatie van SegWit in augustus 2017. Dit script is een P2WPKH verpakt in een P2SH. Het vergrendelt bitcoins op basis van de Hash van een publieke sleutel. Het verschil met de klassieke P2WPKH is dat het script is gewikkeld in de `redeemscript` van een klassieke P2SH.


Dit script werd gemaakt bij de lancering van SegWit om de adoptie ervan te vergemakkelijken. Het maakt het gebruik van deze nieuwe standaard mogelijk, zelfs met diensten of portemonnees die nog niet compatibel zijn met SegWit. Het is een soort overgangsscript naar de nieuwe standaard. Vandaag de dag is het daarom niet meer zo relevant om dit soort ingepakte SegWit scripts te gebruiken, aangezien de meeste wallets native SegWit hebben geïmplementeerd. P2SH-P2WPKH adressen worden geschreven met `Base58Check` codering en beginnen altijd met `3`, net als alle P2SH Address adressen.


> *`P2SH-P2WPKH` wordt soms ook `P2WPKH-nested-in-P2SH` genoemd.*