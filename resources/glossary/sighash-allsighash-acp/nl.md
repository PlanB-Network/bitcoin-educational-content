---
term: SIGHASH_ALL/SIGHASH_ACP
---

Type SigHash Flag (`0x81`) gecombineerd met de `SIGHASH_ANYONECANPAY` modifier (`SIGHASH_ACP`) gebruikt in Bitcoin transactiehandtekeningen. Deze combinatie specificeert dat de handtekening van toepassing is op alle uitgangen en alleen op een specifieke ingang van de transactie. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` staat andere deelnemers toe om extra invoer aan de transactie toe te voegen na de initiële handtekening. Dit is vooral handig in samenwerkingsscenario's, zoals crowdfundingtransacties, waarbij verschillende deelnemers hun eigen invoer kunnen toevoegen terwijl de integriteit van de uitvoer die door de oorspronkelijke ondertekenaar is vastgelegd, behouden blijft.