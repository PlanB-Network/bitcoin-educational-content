---
term: BIP32

---
BIP32 esitteli hierarkkisen deterministisen lompakon (HD-lompakko) käsitteen. Tämän ehdotuksen avulla voidaan luoda hierarkkinen avainparien hierarkia yhteisestä "master-siemenestä" käyttäen yksisuuntaisia derivointifunktioita. Kukin luotu avainpari voi itse olla muiden lapsiavainten vanhempi, jolloin muodostuu puumainen (hierarkkinen) rakenne. BIP32:n etuna on se, että se mahdollistaa useiden erilaisten avainparien hallinnan siten, että tarvitaan vain yksi siemen, jonka avulla ne voidaan luoda uudelleen. Tämä innovaatio on erityisesti auttanut torjumaan osoitteiden uudelleenkäyttöä, joka on vakava ongelma käyttäjien yksityisyyden kannalta. BIP32 mahdollistaa myös alihaarojen luomisen saman lompakon sisällä sen hallinnan helpottamiseksi.