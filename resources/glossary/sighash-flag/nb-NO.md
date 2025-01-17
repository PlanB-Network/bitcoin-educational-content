---
term: SIGHASH FLAG

---
En parameter i en Bitcoin-transaksjon som bestemmer hvilke komponenter i en transaksjon (innganger og utganger) som dekkes av den tilhørende signaturen, og som dermed blir uforanderlig. SigHash-flagget er en byte som legges til i den digitale signaturen for hver inngang. Valget av SigHash-flagg påvirker derfor direkte hvilke deler av transaksjonen som fryses av signaturen, og hvilke som fortsatt kan endres i etterkant. Denne mekanismen sikrer at signaturer forplikter transaksjonsdata på en presis og sikker måte i henhold til signatarens intensjon. Det finnes tre hovedtyper av SigHash-flagg:


- `SIGHASH_ALL` (`0x01`): Signaturen gjelder for alle innganger og utganger i transaksjonen, og låser dem dermed helt;
- `SIGHASH_NONE` (`0x02`): Signaturen gjelder for alle innganger, men ingen av utgangene, slik at utgangene kan endres etter signaturen;
- `SIGHASH_SINGLE` (`0x03`): Signaturen dekker alle inndataene og bare én utdata som tilsvarer indeksen til den signerte inndataen.

I tillegg til disse tre SigHash-flaggene kan modifikatoren `SIGHASH_ANYONECANPAY` (`0x80`) kombineres med hver av de foregående typene. Når denne modifikatoren brukes, signeres bare en del av inndataene, mens de andre kan endres. Her er de eksisterende kombinasjonene med modifikatoren:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Signaturen gjelder for én enkelt inngang, men dekker alle transaksjonens utganger;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Signaturen dekker en enkelt inngang, uten å forplikte seg til noen utgang;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Signaturen gjelder for en enkelt inngang og bare for utdata som har samme indeks som denne inngangen.

> et synonym som noen ganger brukes for "SigHash" er "Signature Hash Types"