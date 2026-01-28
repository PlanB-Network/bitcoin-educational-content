---
term: SIGHASH_NONE/SIGHASH_ACP

definition: SigHash-kombinasjon som signerer kun én spesifikk input uten å binde seg til noen output.
---
Type SigHash-flagg (`0x82`) kombinert med modifikatoren `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) som brukes i Bitcoin-transaksjonssignaturer. Denne kombinasjonen indikerer at signaturen kun gjelder for en spesifikk input, uten å forplikte seg til noen output. Dette gjør at andre deltakere fritt kan legge til flere innganger og endre alle transaksjonens utganger.