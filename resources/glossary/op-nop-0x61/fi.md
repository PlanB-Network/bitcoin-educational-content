---
term: OP_NOP (0X61)

---
Ei vaikuta pinoon tai komentosarjan tilaan. Se ei suorita siirtoja, tarkistuksia tai muutoksia. Se ei yksinkertaisesti tee mitään, ellei toisin päätetä pehmeän haarautumisen kautta. Sen jälkeen, kun Satoshi Nakamoto muutti niitä vuonna 2010, `OP_NOP`-komentoja (`OP_NOP1` (`0XB0`) - `OP_NOP10` (`0XB9`)) käytetäänkin uusien opkoodien lisäämiseen pehmeän haarautumisen muodossa.

Näin ollen `OP_NOP2` (`0XB1`) ja `OP_NOP3` (`0XB2`) on jo käytetty `OP_CHECKLOCKTIMEVERIFY`- ja `OP_CHECKSEQUENCEVERIFY`-toimintojen toteuttamiseen. Niitä käytetään yhdessä `OP_DROP`:n kanssa poistamaan pinosta niihin liittyvät ajalliset arvot, jolloin skriptin suoritus voi jatkua riippumatta siitä, onko solmu ajan tasalla vai ei. `OP_NOP`-komennot mahdollistavat siis keskeytyskohdan lisäämisen komentosarjaan sellaisten lisäehtojen tarkistamiseksi, jotka ovat jo olemassa tai joita voidaan lisätä tulevien pehmeiden haarojen yhteydessä. Tapscriptin jälkeen `OP_NOP` on korvattu tehokkaammalla `OP_SUCCESS`-käskyllä.