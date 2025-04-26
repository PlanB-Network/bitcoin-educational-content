---
term: PEER DISCOVERY

---
Prosessi, jossa Bitcoin-verkon solmut ottavat yhteyttä toisiin solmuihin saadakseen tietoa. Kun Bitcoin-solmu käynnistetään ensimmäisen kerran, sillä ei ole tietoa verkon muista solmuista. Sen on kuitenkin luotava yhteyksiä synkronoituakseen lohkoketjuun, jossa on eniten kertynyttä työtä. Näiden vertaisten löytämiseen käytetään useita mekanismeja tärkeysjärjestyksessä:


- Solmu aloittaa tarkastelemalla paikallista `peers.dat`-tiedostoaan, johon on tallennettu tietoja solmuista, joiden kanssa se on aiemmin ollut vuorovaikutuksessa. Jos solmu on uusi, tämä tiedosto on tyhjä, ja prosessi siirtyy seuraavaan vaiheeseen;
- Jos `peers.dat`-tiedostossa ei ole tietoja (mikä on normaalia vasta käynnistetylle solmulle), solmu tekee DNS-kyselyjä DNS-siemenille. Nämä palvelimet tarjoavat luettelon oletettavasti aktiivisten solmujen IP-osoitteista yhteyksien luomista varten. DNS-siementen osoitteet on kovakoodattu Bitcoin Core -koodiin. Tämä vaihe riittää yleensä vertaisten löytämiseen;
- Jos DNS-siemenet eivät vastaa 60 sekunnin kuluessa, solmu voi kääntyä siemensolmujen puoleen. Nämä ovat julkisia Bitcoin-solmuja, jotka on lueteltu lähes tuhannen merkinnän staattisessa luettelossa, joka on integroitu suoraan Bitcoin Coren lähdekoodiin. Uusi solmu käyttää tätä luetteloa luodakseen ensimmäisen yhteyden verkkoon ja saadakseen muiden solmujen IP-osoitteet;
- Siinä erittäin epätodennäköisessä tapauksessa, että kaikki edelliset menetelmät epäonnistuvat, solmun operaattorilla on aina mahdollisuus lisätä solmujen IP-osoitteet manuaalisesti ensimmäisen yhteyden muodostamiseksi.