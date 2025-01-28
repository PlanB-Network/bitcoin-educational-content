---
term: TIMELOCK

---
En smartkontraktprimitive som gjør det mulig å sette en tidsbasert betingelse som må oppfylles for at en transaksjon skal legges til i en blokk. Det finnes to typer tidssperrer på Bitcoin:


- Den absolutte tidslåsen, som angir et nøyaktig tidspunkt før transaksjonen ikke kan inkluderes i en blokk;
- Den relative tidslåsen, som angir en forsinkelse fra aksept av en tidligere transaksjon.

Tidssperren kan defineres enten som en dato uttrykt i Unix-tid eller som et blokknummer. Til slutt kan tidslåsen gjelde for en transaksjonsutgang ved å bruke en spesifikk opkode i låseskriptet (`OP_CHECKLOCKTIMEVERIFY` eller `OP_CHECKSEQUENCEVERIFY`), eller for en hel transaksjon ved å bruke spesifikke transaksjonsfelt (`nLockTime` eller `nSequence`).