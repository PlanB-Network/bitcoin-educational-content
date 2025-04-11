---
term: SIGHASH_ALL/SIGHASH_ACP

---
Type SigHash-flagg (`0x81`) kombinert med modifikatoren `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) som brukes i Bitcoin-transaksjonssignaturer. Denne kombinasjonen spesifiserer at signaturen gjelder for alle utganger og bare for en bestemt inngang i transaksjonen. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` gjør det mulig for andre deltakere å legge til flere innganger til transaksjonen etter den første signaturen. Det er spesielt nyttig i samarbeidsscenarioer, for eksempel crowdfunding-transaksjoner, der ulike bidragsytere kan legge til sine egne inndata samtidig som integriteten til utdataene som den opprinnelige signatøren har forpliktet seg til, opprettholdes.