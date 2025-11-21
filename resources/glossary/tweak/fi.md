---
term: TWEAK
---

Kryptografiassa julkisen avaimen "virittäminen" tarkoittaa sen muuttamista lisäarvolla, jota kutsutaan "viritykseksi", siten, että sitä voidaan käyttää, jos tiedetään sekä alkuperäinen yksityinen avain että viritys. Teknisesti katsoen tweak on skalaarinen arvo, joka lisätään alkuperäiseen julkiseen avaimeen. Jos $P$ on julkinen avain ja $t$ on tweak, tweakattu julkinen avain on :


$$
P' = P + tG
$$


Missä $G$ on käytetyn elliptisen käyrän generaattori. Tämä operaatio tuottaa uuden julkisen avaimen, joka on johdettu alkuperäisestä, säilyttäen kuitenkin tietyt kryptografiset ominaisuudet, jotka mahdollistavat sen käytön. Tätä menetelmää käytetään esimerkiksi Taproot (P2TR) -osoitteissa, jotta voidaan käyttää joko perinteisellä Schnorr-allekirjoituksella tai täyttämällä jokin Merkle Tree:n eli niin sanotun "MASTin" edellytyksistä.