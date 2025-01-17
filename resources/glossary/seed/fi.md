---
term: SEED

---
Hierarkkisen deterministisen Bitcoin-lompakon yhteydessä siemen on 512-bittinen satunnaisuudesta johdettu tieto. Sitä käytetään deterministisesti ja hierarkkisesti luomaan joukko yksityisiä avaimia ja niitä vastaavia julkisia avaimia Bitcoin-lompakkoa varten. Siemen sekoitetaan usein itse palautuslausekkeeseen. Se on kuitenkin eri tietoa. Siemen saadaan soveltamalla `PBKDF2`-funktiota muistilausekkeeseen ja mahdolliseen salasanaan.

Siemen keksittiin BIP32:n käyttöönoton yhteydessä, ja siinä määritellään hierarkkisen deterministisen lompakon perusteet. Tässä standardissa siemen oli 128 bittiä. Tämä mahdollistaa kaikkien lompakon avainten johtamisen yhdestä ainoasta tiedosta, toisin kuin JBOK-lompakoissa (*Just a Bunch Of Keys*), jotka vaativat uusia varmuuskopioita jokaista luotua avainta varten. BIP39 otti myöhemmin käyttöön tämän siemenen koodauksen, jotta se olisi helpommin ihmisten luettavissa. Tämä koodaus tehdään lauseen muodossa, jota kutsutaan yleisesti muistilausekkeeksi tai palautuslausekkeeksi. Tämä standardi auttaa välttämään virheitä siemenen varmuuskopioinnissa erityisesti tarkistussumman avulla.

Yleisemmin kryptografiassa siemen on satunnainen tieto, jota käytetään lähtökohtana kryptografisten avainten, salausten tai pseudosattumanvaraisten sekvenssien luomisessa. Monien kryptografisten prosessien laatu ja turvallisuus riippuvat siemenen satunnaisuudesta ja luottamuksellisuudesta.

> ► *Englanninkielinen käännös sanalle "graine" on "siemen". Ranskaksi monet käyttävät suoraan englanninkielistä sanaa viittaamaan siemeniin.*