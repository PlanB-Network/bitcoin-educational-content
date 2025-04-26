---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Gjør transaksjonen ugyldig med mindre alle disse vilkårene er oppfylt:


- Stakken er ikke tom;
- Verdien øverst i stakken er større enn eller lik `0`;
- Typen tidslås er den samme mellom feltet `nLockTime` og verdien øverst i stakken (sanntid eller blokknummer);
- Feltet `nSequence` i inndataene er ikke lik `0xffffffffff`;
- Verdien øverst i stakken er større enn eller lik verdien i feltet `nLockTime` i transaksjonen.

Hvis en av disse betingelsene ikke er oppfylt, kan ikke skriptet som inneholder `OP_CHECKLOCKTIMEVERIFY` tilfredsstilles. Hvis alle disse betingelsene er gyldige, fungerer `OP_CHECKLOCKTIMEVERIFY` som en `OP_NOP`, noe som betyr at den ikke utfører noen handling på skriptet. Det er som om den forsvinner. `OP_CHECKLOCKTIMEVERIFY` pålegger dermed en tidsbegrensning på bruken av UTXO-en som er sikret med skriptet som inneholder den. Dette kan gjøres enten i form av en Unix-tidsdato eller som et blokknummer. For å gjøre dette begrenser den de mulige verdiene for `nLockTime`-feltet i transaksjonen som bruker den, og dette `nLockTime`-feltet begrenser i seg selv når transaksjonen kan inkluderes i en blokk.

> ► *Denne opkoden er en erstatning for `OP_NOP`. Den ble plassert på `OP_NOP2`. Den blir ofte referert til med akronymet "CLTV". Merk: `OP_CLTV` må ikke forveksles med `nLockTime`-feltet i en transaksjon. Førstnevnte bruker sistnevnte, men deres natur og handlinger er forskjellige*