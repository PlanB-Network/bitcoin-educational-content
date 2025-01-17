---
term: PYÖRÄMAKSU

---
Bitcoinin ketjuanalyysin sisäinen heuristiikka, joka mahdollistaa hypoteesin tekemisen transaktion tuotosten luonteesta kierrosmäärien perusteella. Yleensä yksinkertaisen maksumallin (1 tulo ja 2 lähtöä) kohdalla, jos yksi tuloista käyttää pyöreän summan, se edustaa maksua. Eliminoimalla voidaan todeta, että jos toinen tuotos edustaa maksua, toinen edustaa muutosta. Näin ollen voidaan tulkita, että on todennäköistä, että maksutapahtuman syöttävällä käyttäjällä on edelleen hallussaan tuloste, joka on tunnistettu vaihtorahaksi.

On huomattava, että tämä heuristiikka ei ole aina sovellettavissa, koska suurin osa maksuista suoritetaan edelleen fiat-valuuttayksiköissä. Kun ranskalainen kauppias hyväksyy bitcoinin, hän ei yleensä näytä vakaita hintoja satsissa. He valitsevat mieluummin euromääräisen hinnan ja bitcoineina maksettavan summan välisen muuntamisen POS-järjestelmänsä kautta (kuten esimerkiksi BTCPay Serverin kautta). Siksi transaktiotulosteessa ei pitäisi olla pyöreää lukua. Analyytikko voisi kuitenkin yrittää tehdä tämän muunnoksen ottamalla huomioon valuuttakurssin, joka oli voimassa, kun transaktio lähetettiin verkkoon. Jos bitcoinista tulee jonain päivänä ensisijainen laskentayksikkö pörsseissämme, tästä heuristiikasta voi tulla vieläkin hyödyllisempi analyyseissä.

![](../../dictionnaire/assets/11.webp)