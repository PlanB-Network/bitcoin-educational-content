---
term: NLOCKTIME

---
Et innebygd felt i transaksjoner som angir en tidsbasert betingelse for at transaksjonen ikke kan legges til en gyldig blokk før. Denne parameteren gjør det mulig å angi et nøyaktig tidspunkt (Unix-tidsstempel) eller et bestemt antall blokker som betingelse for at transaksjonen skal anses som gyldig. Det er altså en absolutt tidslås (ikke relativ). `nLockTime` påvirker hele transaksjonen og muliggjør effektiv tidsverifisering, mens opkoden `OP_CHECKLOCKTIMEVERIFY` bare gjør det mulig å sammenligne den øverste verdien i stakken med `nLockTime`-verdien.