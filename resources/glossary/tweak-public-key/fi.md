---
termi: TWEAK (JULKINEN AVAIN)
---

Kryptografian alalla julkisen avaimen "tweakkaaminen" tarkoittaa tämän avaimen muokkaamista lisäämällä siihen additiivinen arvo, jota kutsutaan "tweakiksi", niin että se pysyy käytettävissä alkuperäisen yksityisen avaimen ja tweakin tiedolla. Teknisesti tweak on skalaariarvo, joka lisätään alkuperäiseen julkiseen avaimeseen. Jos $P$ on julkinen avain ja $t$ on tweak, muokattu julkinen avain muodostuu seuraavasti:

$$
P' = P + tG
$$

Missä $G$ on käytetyn elliptisen käyrän generaattori. Tämä toimenpide mahdollistaa uuden julkisen avaimen saamisen alkuperäisestä avaimesta säilyttäen tietyt kryptografiset ominaisuudet, jotka tekevät siitä käyttökelpoisen. Esimerkiksi tätä menetelmää käytetään Taproot-osoitteissa (P2TR) mahdollistamaan kulutus joko esittämällä Schnorr-allekirjoitus perinteisellä tavalla tai täyttämällä yhden Merkle-puussa mainitun ehdot, jota kutsutaan myös "MASTiksi".

![](../../dictionnaire/assets/26.png)