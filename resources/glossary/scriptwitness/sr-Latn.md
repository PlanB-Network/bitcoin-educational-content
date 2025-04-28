---
term: SCRIPTWITNESS
---

Element u SegWit transakcijskim unosima koji sadrži potpise i javne ključeve potrebne za otključavanje bitcoina poslatih u transakciji. Slično `scriptSig` kod Legacy transakcija, `scriptWitness` se, međutim, ne nalazi na istom mestu. Zapravo, ovaj deo, nazvan "witness" (`*witness*` na engleskom), premješten je u zasebnu bazu podataka kako bi se rešio problem promenljivosti transakcija. Svaki SegWit ulaz ima svoj `scriptWitness`, i svi `scriptWitness` Elements zajedno čine `Witness` polje transakcije.


> ► *Pazite da ne pomešate `scriptWitness` sa `witnessScript`. Dok `scriptWitness` sadrži podatke svedoka za bilo koji SegWit ulaz, `witnessScript` definiše uslove trošenja P2WSH ili P2SH-P2WSH UTXO i predstavlja skriptu za sebe, slično kao `redeemscript` za P2SH izlaz.*