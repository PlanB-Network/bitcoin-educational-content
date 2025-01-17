---
term: SIGHASH_ALL (0X01)

---
Type SigHash-flagg som brukes i Bitcoin-transaksjonssignaturer for å indikere at signaturen gjelder for alle komponenter i transaksjonen. Ved å bruke `SIGHASH_ALL` dekker signatøren alle innganger og alle utganger. Dette betyr at verken inndataene eller utdataene kan endres etter signaturen uten at den blir ugyldig. Denne typen SigHash-flagg er den vanligste i Bitcoin-transaksjoner, ettersom den sikrer fullstendig finalitet og integritet for transaksjonen.