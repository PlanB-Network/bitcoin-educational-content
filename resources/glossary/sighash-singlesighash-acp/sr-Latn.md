---
term: SIGHASH_SINGLE/SIGHASH_ACP
---

Tip zastavice SigHash (`0x83`) kombinovan sa modifikatorom `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) korišćen u Bitcoin potpisima transakcija. Ova kombinacija specificira da se potpis odnosi samo na određeni pojedinačni ulaz i samo na izlaz koji ima isti indeks kao taj ulaz. Drugi ulazi i izlazi mogu biti dodati ili modifikovani od strane drugih strana. Ova konfiguracija je korisna za kolaborativne transakcije gde učesnici mogu dodati svoje ulaze za finansiranje određenog izlaza.