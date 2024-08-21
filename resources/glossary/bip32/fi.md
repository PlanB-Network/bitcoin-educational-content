---
termi: BIP32
---

BIP32 esitteli hierarkkisen deterministisen lompakon (HD-lompakko) käsitteen. Tämä ehdotus mahdollistaa avainparien hierarkian luomisen yhteisestä `master seed` -siemenestä, käyttäen yksisuuntaisia johdannaisfunktioita. Jokainen luotu avainpari voi itse olla muiden lasten avainten vanhempi, muodostaen näin puumaisen (hierarkkisen) rakenteen. BIP32:n etuna on, että se mahdollistaa useiden eri avainparien hallinnan tarvitsemalla vain yhden siemenen niiden uudelleengenerointiin. Tämä innovaatio on erityisesti auttanut torjumaan osoitteen uudelleenkäytön ongelmaa, joka on vakava käyttäjän yksityisyyden kannalta. BIP32 mahdollistaa myös alahaarojen luomisen saman lompakon sisällä sen hallinnan helpottamiseksi.