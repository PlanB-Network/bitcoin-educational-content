---
termi: OVERT ASICBOOST
---

Avoimen ja läpinäkyvän version AsicBoostista. AsicBoost on algoritminen optimointitekniikka, jota käytetään Bitcoin-louhinnassa. Louhijat, jotka käyttävät Overt-versiota, manipuloivat ehdokaslohkon `nVersion`-kenttää ja käyttävät tätä muutosta lisänoncena. Tämä menetelmä jättää lohkon varsinaisen `Nonce`-kentän muuttumattomaksi jokaisen hajautusyrityksen aikana, vähentäen siten tarvittavien laskelmien määrää jokaiselle SHA256:lle, pitämällä osan tiedoista samana yritysten välillä. Tämä versio on julkisesti havaittavissa eikä se piilota muutoksiaan muulta verkostolta, toisin kuin AsicBoostin Covert-versio.