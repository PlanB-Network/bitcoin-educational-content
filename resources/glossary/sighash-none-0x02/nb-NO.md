---
term: SIGHASH_NONE (0X02)

---
Type SigHash-flagg som brukes i Bitcoin-transaksjonssignaturer for å indikere at signaturen gjelder for alle inndataene i transaksjonen, men ikke for noen av utdataene. Bruken av `SIGHASH_NONE` innebærer at signatøren kun forplikter seg til inndataene, slik at utdataene forblir ubestemte eller kan endres etter signering. Denne typen signatur er nyttig i tilfeller der signatøren ønsker å gi andre parter fullmakt til å bestemme hvordan bitcoinsene skal distribueres i transaksjonen.