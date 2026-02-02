---
term: BIP0385

definition: addr() ja raw() -funktiot tulosskriptien kuvaamiseen osoitteen tai heksadesimaalimuodon mukaan deskriptoreissa.
---
Ottaa käyttöön kuvaajafunktiot `addr(ADDR)` ja `raw(HEX)`. Funktio `addr(ADDR)` mahdollistaa tulostuskomentosarjan kuvaamisen vastaanottavan osoitteen avulla, kun taas funktio `raw(HEX)` mahdollistaa tulostuskomentosarjan määrittelyn käyttäen sen raakaa heksadesimaaliesitystä. BIP385 toteutettiin yhdessä kaikkien muiden kuvaajiin liittyvien BIP:ien kanssa (paitsi BIP386) Bitcoin Coren versiossa 0.17.