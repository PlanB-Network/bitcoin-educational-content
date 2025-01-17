---
term: OVERT ASICBOOST

---
AsicBoostin avoin ja läpinäkyvä versio. AsicBoost on algoritminen optimointitekniikka, jota käytetään Bitcoin-louhinnassa. Avointa versiota käyttävät louhijat manipuloivat ehdokaslohkon `nVersion`-kenttää ja käyttävät tätä muutosta ylimääräisenä nonce-koodina. Tämä menetelmä jättää lohkon varsinaisen `Nonce`-kentän muuttumattomaksi jokaisen hashausyrityksen aikana, mikä vähentää jokaiseen SHA256-laskentaan tarvittavia laskutoimituksia pitämällä jotkin tiedot samoina eri yritysten välillä. Tämä versio on julkisesti havaittavissa, eikä se piilota muutoksiaan muulta verkolta, toisin kuin AsicBoostin Covert-versio.