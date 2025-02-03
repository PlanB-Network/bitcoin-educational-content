---
term: BIP21

---
Nils Schneiderin ja Matt Corallon kirjoittama ehdotus, joka perustuu Luke Dashjrin kirjoittamaan BIP20:een, joka puolestaan perustuu Nils Schneiderin kirjoittamaan asiakirjaan. BIP21:ssä määritellään, miten vastaanottavat osoitteet tulisi koodata URI:iin (*Uniform Resource Identifier*) maksujen helpottamiseksi. Esimerkiksi BIP21:n mukainen Bitcoin-URI, jossa pyytäisin nimellä "*Pandul*" lähettämään minulle 0,1 BTC, näyttäisi seuraavalta:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

Tämä standardointi parantaa Bitcoin-tapahtumien käyttökokemusta, sillä sen avulla parametrit voidaan käynnistää napsauttamalla linkkiä tai skannaamalla QR-koodi. BIP21-standardi on nyt laajalti käytössä Bitcoin-lompakko-ohjelmistoissa.