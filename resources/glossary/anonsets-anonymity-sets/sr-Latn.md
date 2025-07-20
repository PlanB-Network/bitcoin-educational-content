---
term: ANONSETS (ANONYMITY SETS)
---

Anonsetovi služe kao indikatori za procenu nivoa privatnosti određenog UTXO. Konkretno, oni mere broj neodvojivih UTXO-ova unutar skupa koji uključuje novčić koji se proučava. Pošto je potrebna grupa identičnih UTXO-ova, anonsetovi se generalno računaju unutar ciklusa coinjoin-a. Oni omogućavaju, gde je to prikladno, da se proceni kvalitet coinjoin-a. Veliki anonset znači povećan nivo anonimnosti, jer postaje teško razlikovati određeni UTXO unutar skupa. Postoje dve vrste anonsetova:


- Prospektivni skup anonimnosti;
- Retrospektivni skup anonimnosti.


Prvi pokazuje veličinu grupe među kojom je skriven proučavani UTXO, znajući UTXO na ulazu. Ovaj indikator omogućava merenje otpornosti privatnosti novčića protiv analize od prošlosti ka sadašnjosti (od ulaza ka izlazu). Na engleskom, naziv ovog indikatora je "*forward anonset*" ili "*forward-looking metrics*."


![](../../dictionnaire/assets/39.webp)


Drugi pokazatelj označava broj mogućih izvora za dati novčić, znajući UTXO na izlazu. Ovaj indikator omogućava merenje otpornosti privatnosti novčića protiv analize od sadašnjosti ka prošlosti (od izlaza ka ulazu). Na engleskom, naziv ovog indikatora je "*backward anonset*" ili "*backward-looking metrics*."


![](../../dictionnaire/assets/40.webp)


> ► *U francuskom jeziku je opšteprihvaćeno korišćenje termina “anonset.” Međutim, mogao bi se prevesti kao “ensemble d'anonymat” ili “potentiel d'anonymat.” U engleskom i francuskom jeziku, termin “score” se takođe ponekad koristi za označavanje anonseta (prospective score i retrospective score).*