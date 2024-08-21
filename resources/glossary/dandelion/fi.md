---
termi: DANDELION
---

Ehdotus, jonka tavoitteena on parantaa Bitcoin-verkon transaktioiden reitityksen yksityisyyttä vastustamaan deanonymisointia. Bitcoinin tavallisessa toiminnassa transaktiot lähetetään välittömästi useille solmuille. Tämä ilmiö voi mahdollisesti sallia tarkkailijoiden yhdistää transaktiot, jotka normaalisti ovat anonyymejä, IP-osoitteisiin. BIP156:n tavoitteena on käsitellä tätä ongelmaa. Tätä varten se esittelee lisävaiheen lähetysprosessiin säilyttääkseen anonymiteetin ennen julkista levitystä. Näin ollen Dandelion käyttää ensin "varsi"-vaihetta, jossa transaktio lähetetään satunnaisen solmupolun kautta, ennen kuin se lähetetään koko verkolle "pörrö"-vaiheessa. Varsi ja pörrö viittaavat transaktion leviämisen käyttäytymiseen verkossa, muistuttaen voikukan muotoa. Tämä reititysmenetelmä hämärtää polkua takaisin lähtösolmuun, tehden transaktion jäljittämisen verkossa takaisin alkuperäänsä vaikeaksi.

![](../../dictionnaire/assets/36.png)