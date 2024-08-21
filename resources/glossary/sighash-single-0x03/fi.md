---
termi: SIGHASH_SINGLE (0X03)
---

SigHash-lipun tyyppi, jota käytetään Bitcoin-siirtojen allekirjoituksissa osoittamaan, että allekirjoitus koskee kaikkia siirron syötteitä ja vain yhtä tulostetta, joka vastaa saman syötteen indeksiä, johon on allekirjoitettu. Näin ollen jokainen `SIGHASH_SINGLE`-lipulla allekirjoitettu syöte on erityisesti linkitetty tiettyyn tulosteeseen. Muut tulosteet eivät ole allekirjoituksen sitomia ja niitä voidaan siksi muokata myöhemmin. Tämän tyyppinen allekirjoitus on hyödyllinen monimutkaisissa siirroissa, joissa osallistujat haluavat linkittää tiettyjä syötteitä tiettyihin tulosteisiin, jättäen samalla joustavuutta siirron muiden tulosteiden osalta.