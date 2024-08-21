---
termi: OP_NOP (0X61)
---

Ei tuota vaikutusta pinossa tai skriptin tilassa. Se ei suorita liikkeitä, tarkistuksia tai muutoksia. Se yksinkertaisesti ei tee mitään, ellei pehmeän haarukan kautta toisin päätetä. Itse asiassa, sitten kun Satoshi Nakamoto muokkasi niitä vuonna 2010, `OP_NOP`-komennot (`OP_NOP1` (`0XB0`) - `OP_NOP10` (`0XB9`)) ovat käytössä uusien operaatiokoodien lisäämiseksi pehmeän haarukan muodossa.

Näin ollen, `OP_NOP2` (`0XB1`) ja `OP_NOP3` (`0XB2`) on jo käytetty toteuttamaan `OP_CHECKLOCKTIMEVERIFY` ja `OP_CHECKSEQUENCEVERIFY` vastaavasti. Niitä käytetään yhdessä `OP_DROP`-komennon kanssa poistamaan liitetyt ajalliset arvot pinosta, mikä mahdollistaa skriptin suorituksen jatkumisen, oli solmu ajan tasalla tai ei. `OP_NOP`-komennot mahdollistavat siis keskeytyspisteen lisäämisen skriptiin tarkistamaan lisäehtoja, jotka jo ovat olemassa tai voidaan lisätä tulevissa pehmeissä haarukoissa. Tapscriptin myötä `OP_NOP`-komentojen käyttö on korvattu tehokkaammalla `OP_SUCCESS`-komennolla.