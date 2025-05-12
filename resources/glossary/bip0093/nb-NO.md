---
term: BIP0093
---

Informasjons-BIP som foreslår en standard for lagring og gjenoppretting av seed i en hierarkisk deterministisk portefølje (i henhold til BIP32) ved hjelp av Shamirs hemmelige nøkkeldeling. Denne protokollen definerer "codex32"-formatet, som er inspirert av bech32-formatet, ved å introdusere en strukturert streng som består av et prefiks, en terskelparameter, en identifikator, en delingsindeks, en nyttelast og en kontrollsum (BCH). Metoden gjør det mulig å dele seed i opptil 31 aksjer, hvorav en definert terskel (mellom 1 og 9) kreves for full seed-gjenoppretting.