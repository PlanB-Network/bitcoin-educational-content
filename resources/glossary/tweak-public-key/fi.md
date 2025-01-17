---
term: TWEAK (JULKINEN AVAIN)

---
Kryptografian alalla julkisen avaimen "virittäminen" tarkoittaa avaimen muuttamista käyttämällä lisäarvoa, jota kutsutaan "viritykseksi", siten, että sitä voidaan käyttää alkuperäisen yksityisen avaimen ja virityksen ollessa tiedossa. Teknisesti katsoen viritys on skalaarinen arvo, joka lisätään alkuperäiseen julkiseen avaimeen. Jos $P$ on julkinen avain ja $t$ on tweak, tweakattu julkinen avain on:

$$
P' = P + tG
$$

Missä $G$ on käytetyn elliptisen käyrän generaattori. Tämän operaation avulla voidaan saada uusi julkinen avain, joka on johdettu alkuperäisestä avaimesta, säilyttäen samalla tietyt kryptografiset ominaisuudet, jotka tekevät siitä käyttökelpoisen. Tätä menetelmää käytetään esimerkiksi Taproot-osoitteissa (P2TR), jotta voidaan käyttää joko perinteisellä Schnorr-allekirjoituksella tai täyttämällä jokin Merkle-puussa (MAST) esitetyistä ehdoista.

![](../../dictionnaire/assets/26.webp)