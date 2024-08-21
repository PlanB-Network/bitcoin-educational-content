---
termi: WALLET IMPORT FORMAT (WIF)
---

Menetelmä Bitcoinin yksityisen avaimen koodaamiseksi siten, että sitä voidaan helpommin tuoda tai viedä eri lompakoiden välillä. WIF perustuu `Base58Check`-koodaukseen, joka sisältää tiedot versionumerosta, vastaavan julkisen avaimen tiivistämisestä ja kirjoitusvirheiden havaitsemiseen tarkoitetusta tarkistussummasta. WIF-yksityisavain alkaa merkeillä `5` tiivistämättömille avaimille, tai `K` ja `L` tiivistetyille avaimille, ja sisältää kaikki tarvittavat merkit alkuperäisen yksityisavaimen uudelleenmuodostamiseksi. WIF-muoto tarjoaa standardoidun keinon siirtää yksityinen avain eri lompakko-ohjelmistojen välillä.