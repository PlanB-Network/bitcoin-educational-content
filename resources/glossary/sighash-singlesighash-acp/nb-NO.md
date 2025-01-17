---
term: SIGHASH_SINGLE/SIGHASH_ACP

---
Type SigHash-flagg (`0x83`) kombinert med modifikatoren `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) som brukes i Bitcoin-transaksjonssignaturer. Denne kombinasjonen spesifiserer at signaturen kun gjelder for en spesifikk enkelt inngang og kun for utgangen som har samme indeks som denne inngangen. Andre innganger og utganger kan legges til eller endres av andre parter. Denne konfigurasjonen er nyttig for samarbeidstransaksjoner der deltakerne kan legge til sine egne inndata for å finansiere en bestemt utdata.