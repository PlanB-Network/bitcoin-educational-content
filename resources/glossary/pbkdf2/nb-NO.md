---
term: PBKDF2

---
pBKDF2 står for *Password-Based Key Derivation Function 2*. Det er en metode for å lage kryptografiske nøkler fra et passord ved hjelp av en avledningsfunksjon. Den tar utgangspunkt i et passord og et kryptografisk salt, og bruker iterativt en forhåndsbestemt funksjon (ofte en hash-funksjon som `SHA256` eller en `HMAC`) på disse dataene. Denne prosessen gjentas mange ganger for å generere en kryptografisk nøkkel.

I forbindelse med Bitcoin brukes `PBKDF2` sammen med `HMAC-SHA512`-funksjonen for å lage frøet til en deterministisk og hierarkisk lommebok (frø) fra en gjenopprettingsfrase på 12 eller 24 ord. Det kryptografiske saltet som brukes i dette tilfellet, er BIP39-passordet, og antall iterasjoner er `2048`.