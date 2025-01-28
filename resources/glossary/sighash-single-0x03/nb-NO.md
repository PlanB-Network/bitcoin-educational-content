---
term: SIGHASH_SINGLE (0X03)

---
Type SigHash-flagg som brukes i Bitcoin-transaksjonssignaturer for å indikere at signaturen gjelder for alle inndataene i transaksjonen og bare én utdata, som tilsvarer indeksen for den samme signerte inndataen. Dermed er hver inngang som er signert med `SIGHASH_SINGLE` spesifikt knyttet til en bestemt utgang. De andre utdataene er ikke bundet av signaturen og kan derfor endres senere. Denne typen signatur er nyttig i komplekse transaksjoner der deltakerne ønsker å knytte bestemte inndata til bestemte utdata, samtidig som de andre utdataene i transaksjonen skal være fleksible.