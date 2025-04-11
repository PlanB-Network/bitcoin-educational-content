---
term: TOIPUMISPOLKU

---
Miniscriptiä käyttävässä lompakko-ohjelmistossa, kuten esimerkiksi Liana, palautusreitit viittaavat avainsarjoihin, jotka tulevat käyttöön vasta, kun bitcoinit lukitsevassa skriptissä (timelock) on kulunut tietty aika, jonka bitcoinit ovat olleet käyttämättömiä. Elvytyspolkuja voidaan käyttää vasta, kun timelockit ovat umpeutuneet, joten ne tarjoavat menetelmän varojen palauttamiseen, kun ensisijainen polku ei ole käytettävissä. Tarkastellaan esimerkkiä skriptistä, joka sisältää kaksi erillistä avainta: avain A, joka sallii bitcoinien välittömän käyttämisen, ja avain B, joka sallii niiden käyttämisen 52 560 lohkon timelockin määrittelemän viiveen jälkeen. Tässä esimerkissä avain A on peräisin ensisijaisesta polusta, kun taas avain B on peräisin palautuspolusta.