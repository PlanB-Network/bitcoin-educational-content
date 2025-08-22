---
term: PRIVÉ TOETS
---

Een private sleutel is een fundamenteel element van asymmetrische cryptografie. Het is een getal (256 bits in de context van Bitcoin) dat een cryptografisch geheim voorstelt. Deze sleutel wordt gebruikt om transacties digitaal te ondertekenen en de Ownership van een Bitcoin publieke sleutel te bewijzen (en bij uitbreiding, een ontvangende Address) door te voldoen aan een `scriptPubKey`. Privé sleutels maken het dus mogelijk bitcoins uit te geven door de UTXO's geassocieerd met de corresponderende publieke sleutel te ontgrendelen. Privé sleutels moeten strikt vertrouwelijk worden gehouden, omdat de openbaarmaking ervan kwaadwillende derden in staat zou kunnen stellen de controle over de bijbehorende fondsen over te nemen.


In het Bitcoin systeem is de private sleutel gekoppeld aan een publieke sleutel door middel van een digitaal handtekeningalgoritme dat gebruik maakt van elliptische krommen (ECDSA of Schnorr). De publieke sleutel wordt afgeleid van de private sleutel, maar het omgekeerde is praktisch onmogelijk te bereiken vanwege de rekenmoeilijkheid die inherent is aan het oplossen van het onderliggende wiskundige probleem (het discrete logaritmeprobleem). De publieke sleutel wordt over het algemeen gebruikt om generate een Bitcoin Address, die wordt gebruikt om bitcoins te vergrendelen met behulp van een script. In cryptografie zijn privésleutels vaak willekeurige of pseudo-willekeurige getallen. In de specifieke context van Bitcoin deterministische en hiërarchische portemonnees, worden private sleutels deterministisch afgeleid van de seed. Privé sleutels worden vaak verward met de seed of met de herstelzin (Mnemonic). Deze Elements zijn echter verschillend.


> in het Engels wordt een privésleutel "private key" genoemd Deze term wordt soms afgekort als "privkey" of "PV"