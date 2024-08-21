---
termi: CHECKSUM
---

Checksum on laskettu arvo joukolle dataa, jota käytetään varmistamaan kyseisen datan eheys ja validius sen siirron tai tallennuksen aikana. Checksum-algoritmit on suunniteltu havaitsemaan satunnaiset virheet tai tahattomat datan muutokset, kuten siirtohäiriöt tai tiedostojen korruptoitumiset. Olemassa on erilaisia checksum-algoritmeja, kuten pariteettitarkistukset, modulaariset checksumit, kryptografiset hajautusfunktiot tai BCH-koodit (*Bose, Ray-Chaudhuri ja Hocquenghem*).

Bitcoinissa checksumeja käytetään sovellustasolla varmistamaan vastaanotto-osoitteiden eheys. Checksum lasketaan käyttäjän osoitteen kuormasta, ja se lisätään tähän osoitteeseen mahdollisten virheiden havaitsemiseksi sen syötön aikana. Checksum on myös läsnä palautuslausekkeissa (mnemoniikka).

> ► *Englanninkielinen käännös termille "somme de contrôle" on "checksum". Yleisesti hyväksytään, että termi "checksum" käytetään suoraan ranskaksi.*