---
term: SIGHASH_ALL/SIGHASH_ACP
---

Tip zastavice SigHash (`0x81`) kombinovan sa modifikatorom `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) korišćen u Bitcoin potpisima transakcija. Ova kombinacija specificira da se potpis odnosi na sve izlaze i samo na određeni ulaz transakcije. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` omogućava drugim učesnicima da dodaju dodatne ulaze u transakciju nakon njenog inicijalnog potpisa. Ovo je posebno korisno u kolaborativnim scenarijima, kao što su transakcije grupnog finansiranja, gde različiti doprinosioci mogu dodati svoje ulaze dok očuvaju integritet izlaza koje je inicijalni potpisnik potvrdio.