---
term: SIGHASH_NONE/SIGHASH_ACP
definition: SigHash-combinatie die een enkele specifieke input ondertekent zonder zich vast te leggen op een output.
---

Type SigHash Flag (`0x82`) gecombineerd met de `SIGHASH_ANYONECANPAY` modifier (`SIGHASH_ACP`) gebruikt in Bitcoin transactiehandtekeningen. Deze combinatie geeft aan dat de handtekening alleen van toepassing is op een specifieke invoer, zonder zich vast te leggen op een uitvoer. Hierdoor kunnen andere deelnemers vrijelijk extra inputs toevoegen en alle outputs van de transactie wijzigen.