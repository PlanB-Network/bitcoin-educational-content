---
termi: BIP21
---

Ehdotuksen kirjoittivat Nils Schneider ja Matt Corallo, pohjautuen BIP20:een, jonka kirjoitti Luke Dashjr, ja se puolestaan perustui toiseen Nils Schneiderin kirjoittamaan dokumenttiin. BIP21 määrittelee, miten vastaanotto-osoitteet tulisi koodata URIeihin (*Uniform Resource Identifier*) maksujen helpottamiseksi. Esimerkiksi Bitcoin URI, joka noudattaa BIP21-standardia ja jossa pyytäisin nimikkeellä “*Pandul*” lähettämään minulle 0.1 BTC, näyttäisi tältä:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

Tämä standardisointi parantaa Bitcoin-siirtojen käyttökokemusta mahdollistamalla linkin klikkaamisen tai QR-koodin skannaamisen parametrien aloittamiseksi. BIP21-standardi on nykyään laajalti käytössä Bitcoin-lompakko-ohjelmistoissa.