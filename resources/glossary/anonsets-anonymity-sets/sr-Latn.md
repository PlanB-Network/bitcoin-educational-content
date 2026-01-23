---
term: Anonsets (skupovi anonimnosti)
definition: Indikatori koji mere stepen privatnosti UTXO brojanjem broja nerazlučivih UTXO-a u setu, tipično nakon coinjoin.
---
Anonseti služe kao indikatori za procenu stepena privatnosti određenog UTXO-a. Preciznije, oni mere broj neprepoznatljivih UTXO-a unutar skupa koji uključuje posmatranu jedinicu. Pošto je neophodno raspolagati grupom identičnih UTXO-a, anonseti se uglavnom izračunavaju u okviru ciklusa coinjoin-a. Oni omogućavaju, po potrebi, procenu kvaliteta coinjoin-a. Veliki anonset znači viši nivo anonimnosti, jer postaje teško razlikovati određeni UTXO unutar skupa.

Postoje dve vrste anonseta: forward anonset (forward-looking metrics); i backward anonset (backward-looking metrics). Termin "*score*" se ponekad takođe koristi za označavanje anonseta.

Prvi pokazuje veličinu grupe u kojoj se krije analizirani izlazni UTXO, pri poznatom ulaznom UTXO-u. Ovaj indikator omogućava merenje otpornosti privatnosti novčića na analizu od prošlosti ka sadašnjosti (od ulaza ka izlazu). Drugi pokazuje broj mogućih izvora za dati novčić, pri poznatom izlaznom UTXO-u. Ovaj indikator omogućava merenje otpornosti privatnosti novčića na analizu od sadašnjosti ka prošlosti (od izlaza ka ulazu).
















