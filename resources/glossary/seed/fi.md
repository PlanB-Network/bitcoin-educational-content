---
termi: SEED
---

Tietyssä hierarkkisen deterministisen Bitcoin-lompakon kontekstissa siemen (seed) on 512-bittinen tieto, joka on johdettu satunnaisuudesta. Sitä käytetään deterministisesti ja hierarkkisesti luomaan joukko yksityisiä avaimia ja niitä vastaavia julkisia avaimia Bitcoin-lompakkoon. Siementä sekoitetaan usein palautuslausekkeen kanssa. Kuitenkin, se on eri tieto. Siemen saadaan soveltamalla `PBKDF2`-funktiota muistilauseeseen ja mahdolliseen salalauseeseen.

Siemen keksittiin BIP32:n esittelyn yhteydessä, joka määrittelee hierarkkisen deterministisen lompakon perustat. Tässä standardissa siemen oli 128 bittiä. Tämä mahdollistaa kaikkien lompakon avainten johdannan yhdestä tietokappaleesta, toisin kuin JBOK (*Just a Bunch Of Keys*, Vain joukko avaimia) -lompakot, jotka vaativat uusia varmuuskopioita jokaiselle luodulle avaimelle. BIP39 myöhemmin esitteli tämän siemenen koodauksen, jotta sen ihmislukukelpoisuus yksinkertaistuisi. Tämä koodaus tehdään lauseen muodossa, jota yleisesti kutsutaan muistilauseeksi tai palautuslauseeksi. Tämä standardi auttaa välttämään virheitä siemenen varmuuskopioinnissa, erityisesti käyttämällä tarkistussummaa.

Yleisemmin kryptografiassa siemen on satunnaisesta datasta peräisin oleva tietokappale, jota käytetään lähtökohtana kryptografisten avainten, salauksien tai pseudo-satunnaisten sekvenssien generoimiseen. Monien kryptografisten prosessien laatu ja turvallisuus riippuvat siemenen satunnaisuudesta ja luottamuksellisuudesta.

> ► *Ranskan kielen sana "graine" käännetään englanniksi "seed". Ranskassa monet käyttävät suoraan englanninkielistä sanaa viitatakseen siemeneen.*