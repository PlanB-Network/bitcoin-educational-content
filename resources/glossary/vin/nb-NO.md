---
term: VIN

---
Et spesifikt element i en Bitcoin-transaksjon som spesifiserer kilden til midlene som brukes til å tilfredsstille utgangene. Hver `vin` refererer til en ubrukt output (UTXO) fra en tidligere transaksjon. En transaksjon kan inneholde flere innganger, som hver identifiseres av en kombinasjon av `txid` (identifikatoren til den opprinnelige transaksjonen) og `vout` (indeksen til utgangen i den transaksjonen).

Hver `vin` inneholder følgende informasjon:


- `txid`: identifikatoren til den forrige transaksjonen som inneholder utdataene som her brukes som input;
- `vout`: indeksen for utdata i forrige transaksjon;
- `scriptSig` eller `scriptWitness`: et opplåsingsskript som gir de nødvendige dataene for å oppfylle betingelsene som stilles av `scriptPubKey` for den forrige transaksjonen som pengene brukes på, vanligvis ved å gi en kryptografisk signatur;
- `nSequence`: et spesifikt felt som brukes til å angi hvordan denne inngangen er tidslåst, i tillegg til andre alternativer som RBF.