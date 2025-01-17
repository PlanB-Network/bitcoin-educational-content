---
term: UTXO SET

---
Refererer til samlingen av alle eksisterende UTXO-er på et gitt tidspunkt. Med andre ord er det en stor liste over alle de ulike bitcoinsene som venter på å bli brukt. Hvis du legger sammen alle UTXO-ene i UTXO-settet, får vi den totale pengemassen av bitcoins i omløp. Hver node i Bitcoin-nettverket vedlikeholder sitt eget UTXO-sett i sanntid. Det oppdateres etter hvert som nye gyldige blokker bekreftes, med transaksjonene de inkluderer, som forbruker noen UTXO-er fra UTXO-settet og skaper nye i retur.

Dette UTXO-settet oppbevares av hver node, slik at de raskt kan kontrollere om UTXO-ene som er brukt i transaksjoner, faktisk er legitime. Dette gjør at de kan oppdage og avvise forsøk på dobbeltbruk. UTXO-settet er ofte kjernen i bekymringene rundt Bitcoins desentralisering, ettersom størrelsen naturlig nok øker svært raskt. Siden en del av UTXO-settet må oppbevares i RAM for å verifisere transaksjoner innen rimelig tid, kan UTXO-settet gradvis gjøre det for kostbart å drive en hel node. UTXO-settet har også en betydelig innvirkning på IBD (*Initial Block Download*). Jo mer av UTXO-settet som kan plasseres i RAM, desto raskere er IBD. På Bitcoin Core lagres UTXO-settet i mappen `/chainstate`.

> på engelsk kan "UTXO set" oversettes til "UTXO-sett"