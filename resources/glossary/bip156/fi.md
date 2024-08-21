---
termi: BIP156
---

Ehdotus, joka tunnetaan nimellä Dandelion, pyrkii parantamaan Bitcoin-verkon transaktioiden reitityksen yksityisyyttä vastustaakseen deanonymisointia. Bitcoinin tavallisessa toiminnassa transaktiot välitetään välittömästi useille solmuille. Jos tarkkailija pystyy näkemään jokaisen solmun välittämän jokaisen transaktion verkossa, he saattavat olettaa, että transaktion ensimmäisenä lähettänyt solmu on myös kyseisen transaktion alkuperäinen solmu ja siten, että se tulee solmun operaattorilta. Tämä ilmiö voisi mahdollisesti sallia tarkkailijoiden yhdistää transaktiot, jotka normaalisti ovat nimettömiä, IP-osoitteisiin.

BIP156:n tavoitteena on käsitellä tätä ongelmaa. Tätä varten se esittelee lisävaiheen lähetysprosessiin säilyttääkseen nimettömyyden ennen julkista levitystä. Näin ollen Dandelion käyttää ensin "varsi"-vaihetta, jossa transaktio lähetetään satunnaisen solmupolun kautta, ennen kuin se lähetetään koko verkkoon "pörrö"-vaiheessa. Varsi ja pörrö viittaavat transaktion leviämisen käyttäytymiseen verkossa, muistuttaen voikukan (*dandelion* englanniksi) muotoa.

Tämä reititysmenetelmä hämärtää polkua takaisin lähtösolmuun, tehden transaktion jäljittämisen verkossa takaisin sen alkuperään vaikeaksi. Dandelion parantaa näin yksityisyyttä rajoittamalla vastustajien kykyä deanonymisoida verkko. Tämä menetelmä on vielä tehokkaampi, kun transaktio ylittää "varsi"-vaiheessa solmun, joka salaa verkkoliikenteensä, kuten Torin tai *P2P Transport V2*:n avulla. BIP156 ei ole vielä lisätty Bitcoin Coreen.

![](../../dictionnaire/assets/36.png)