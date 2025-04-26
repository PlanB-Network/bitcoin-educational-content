---
term: DANDELION

---
Ehdotus, jonka tarkoituksena on parantaa transaktioiden reitityksen yksityisyyttä Bitcoin-verkossa nimettömyyden poistamisen torjumiseksi. Bitcoinin vakiotoiminnassa transaktiot lähetetään välittömästi useisiin solmuihin. Tämä ilmiö voi mahdollisesti antaa tarkkailijoille mahdollisuuden yhdistää normaalisti anonyymit transaktiot IP-osoitteisiin. BIP156:n tavoitteena on puuttua tähän ongelmaan. Tätä varten se ottaa käyttöön lisävaiheen lähetysprosessissa anonymiteetin säilyttämiseksi ennen julkista levittämistä. Dandelion käyttää siis ensin "stem"-vaihetta, jossa transaktio lähetetään satunnaisen solmupolun kautta, ennen kuin se lähetetään koko verkkoon "fluff"-vaiheessa. Varsi ja pörröisyys viittaavat transaktion etenemiseen verkossa ja muistuttavat voikukan muotoa. Tämä reititysmenetelmä peittää lähdesolmuun johtavan polun, jolloin on vaikea jäljittää tapahtumaa verkon läpi takaisin sen alkuperään.

![](../../dictionnaire/assets/36.webp)