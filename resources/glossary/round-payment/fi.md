---
termi: PYÖREÄ MAKSU
---

Sisäinen heuristiikka Bitcoinin ketjuanalyysiin, joka mahdollistaa hypoteesin muodostamisen transaktion tulosteiden luonteesta perustuen pyöreisiin summiin. Yleensä, kun kohdataan yksinkertainen maksukaava (1 syöte ja 2 tulostetta), jos toinen tulosteista käyttää pyöreää summaa, se edustaa maksua. Poissulkemisen kautta, jos toinen tuloste edustaa maksua, toinen edustaa vaihtorahaa. Näin ollen voidaan tulkita, että on todennäköistä, että transaktion syöttänyt käyttäjä yhä omistaa vaihtorahaksi tunnistetun tulosteen.

On huomattava, että tätä heuristiikkaa ei aina voida soveltaa, koska suurin osa maksuista tehdään edelleen fiat-valuutoissa. Todellakin, kun kauppias Ranskassa hyväksyy bitcoineja, yleensä he eivät näytä vakaita hintoja satosheina. He pikemminkin valitsisivat hinnan muuntamisen euroista bitcoineiksi maksettavaksi heidän POS-järjestelmänsä kautta (kuten BTCPay Server, esimerkiksi). Siksi transaktion tulosteessa ei pitäisi olla pyöreää numeroa. Siitä huolimatta analyytikko voisi yrittää tehdä tämän muunnoksen ottamalla huomioon vaihtokurssin, joka oli voimassa, kun transaktio lähetettiin verkkoon. Jos jonain päivänä bitcoinista tulee suosituin laskentayksikkö vaihdoissamme, tämä heuristiikka voisi muuttua vielä hyödyllisemmäksi analyyseissä.

![](../../dictionnaire/assets/11.png)