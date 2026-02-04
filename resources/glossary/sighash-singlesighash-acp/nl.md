---
term: SIGHASH_SINGLE/SIGHASH_ACP
definition: Combinatie die een enkele input ondertekent en alleen de output met dezelfde index.
---

Type SigHash Flag (`0x83`) gecombineerd met de `SIGHASH_ANYONECANPAY` modifier (`SIGHASH_ACP`) gebruikt in Bitcoin transactiehandtekeningen. Deze combinatie specificeert dat de handtekening alleen van toepassing is op een specifieke enkele ingang en alleen op de uitgang die dezelfde index heeft als deze ingang. Andere ingangen en uitgangen kunnen worden toegevoegd of gewijzigd door andere partijen. Deze configuratie is nuttig voor collaboratieve transacties waarbij deelnemers hun eigen inputs kunnen toevoegen om een specifieke output te financieren.