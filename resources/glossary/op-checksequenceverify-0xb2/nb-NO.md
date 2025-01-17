---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Gjør transaksjonen ugyldig hvis en av disse egenskapene er observert:


- Stakken er tom;
- Verdien på toppen av stakken er mindre enn `0`;
- Deaktiveringsflagget for verdien øverst i stakken er udefinert og; Transaksjonsversjonen er mindre enn `2` eller; Deaktiveringsflagget for `nSequence`-feltet i inndataene er satt eller; Tidssperretypen er ikke den samme mellom `nSequence`-feltet og verdien øverst i stakken (sanntid eller antall blokker) eller; Verdien øverst i stakken er større enn verdien i `nSequence`-feltet i inndataene.

Hvis en eller flere av disse egenskapene er observert, kan ikke skriptet som inneholder `OP_CHECKSEQUENCEVERIFY` tilfredsstilles. Hvis alle betingelsene er gyldige, fungerer `OP_CHECKSEQUENCEVERIFY` som en `OP_NOP`, noe som betyr at den ikke utfører noen handling på skriptet. Det er som om den forsvinner. `OP_CHECKSEQUENCEVERIFY` pålegger dermed en relativ tidsbegrensning på bruken av UTXO-en som er sikret med skriptet som inneholder den. Dette kan gjøres enten i form av sanntid eller som et antall blokker. For å gjøre dette begrenser den de mulige verdiene for `nSequence`-feltet i inndataene som bruker den, og dette `nSequence`-feltet begrenser i seg selv når transaksjonen som inkluderer denne inndataen, kan inkluderes i en blokk.

> ► *Denne opkoden er en erstatning for `OP_NOP`. Den ble plassert på `OP_NOP3`. Den blir ofte referert til med akronymet "CSV". Merk: `OP_CSV` må ikke forveksles med `nSequence`-feltet i en transaksjon. Førstnevnte bruker sistnevnte, men de er av forskjellig art og har forskjellige handlinger*