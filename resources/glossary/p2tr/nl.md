---
term: P2TR
definition: Taproot-script dat uitgaven toestaat via een publieke sleutel of Merkle-scripts, bc1p-adressen.
---

P2TR staat voor *Betalen aan Taproot*, wat een standaard scriptmodel is dat wordt gebruikt om bestedingsvoorwaarden vast te stellen voor een UTXO (Onbestede Transactie Output). Het werd geïntroduceerd met de implementatie van Taproot in november 2021. P2TR gebruikt het Schnorr-protocol om cryptografische sleutels samen te voegen, evenals Merkle trees voor alternatieve scripts, bekend als MAST (*Merkelized Alternative Script Tree*). In tegenstelling tot traditionele transacties waarbij de bestedingsvoorwaarden openbaar zijn (soms op het moment van ontvangen, soms op het moment van uitgeven), maakt P2TR het mogelijk om complexe scripts te verbergen achter een enkele ogenschijnlijke openbare sleutel.


Technisch gezien vergrendelt een P2TR script bitcoins op een unieke Schnorr publieke sleutel, aangeduid als $K$. Deze sleutel $K$ is echter eigenlijk een aggregaat van een publieke sleutel $P$ en een publieke sleutel $M$, de laatste wordt berekend uit de Merkle Root van een lijst met `scriptPubKey`. De bitcoins die vergrendeld zijn met een P2TR script kunnen op twee verschillende manieren uitgegeven worden: ofwel door het publiceren van een handtekening voor de publieke sleutel $P$, ofwel door te voldoen aan één van de scripts die in de Merkle Tree staan. De eerste optie wordt het "*sleutelpad*" genoemd en de tweede het "*scriptpad*".


P2TR stelt gebruikers dus in staat om bitcoins naar een publieke sleutel of naar meerdere scripts naar keuze te sturen. Een ander voordeel van dit script is dat, hoewel er meerdere manieren zijn om een P2TR uitgang uit te geven, alleen de manier die gebruikt wordt onthuld hoeft te worden op het moment van uitgeven, waardoor de ongebruikte alternatieven privé blijven. P2TR is een versie 1 SegWit uitgang, wat betekent dat de handtekeningen voor P2TR ingangen worden opgeslagen in de getuige van een transactie, en niet in de `scriptSig`. P2TR adressen gebruiken een `Bech32m` codering en beginnen met `bc1p`.