---
term: OP_SUCCESS

---
OP_SUCCESS` edustaa sarjaa op-koodeja, jotka olivat aiemmin poissa käytöstä ja jotka on nyt varattu Tapscriptin tulevaa käyttöä varten. Niiden perimmäisenä tavoitteena on helpottaa skriptikielen päivityksiä ja laajennuksia sallimalla uusien toiminnallisuuksien käyttöönotto pehmeiden haarojen kautta. Kun jokin näistä opkoodeista esiintyy komentosarjassa, se merkitsee komentosarjan kyseisen osan automaattista onnistumista riippumatta siitä, millaisia tietoja tai ehtoja siinä on. Tämä tarkoittaa, että komentosarjan suoritus jatkuu epäonnistumatta edellisistä toiminnoista riippumatta.

Näin ollen kun `OP_SUCCESS`-operaatiokoodiin lisätään uusi op-koodi, se tarkoittaa välttämättä edellisiä rajoittavamman säännön lisäämistä. Päivitetyt solmut voivat tällöin tarkistaa tämän säännön noudattamisen, ja päivittämättömät solmut eivät hylkää siihen liittyviä transaktioita ja niihin sisältyviä lohkoja, koska `OP_SUCCESS` validoi tämän osan käsikirjoituksesta. Näin ollen hard forkia ei synny.

Vertailun vuoksi `OP_NOP` (*No Operation*) toimii myös komentosarjassa sijoitussalpaajina, mutta niillä ei ole vaikutusta komentosarjan suorittamiseen. Kun `OP_NOP`-operaatio kohdataan, skripti yksinkertaisesti jatkuu muuttamatta pinon tilaa tai skriptin etenemistä. Keskeinen ero on siis niiden vaikutuksessa suoritukseen: `OP_SUCCESS` takaa onnistuneen läpikäynnin kyseisessä komentosarjan osassa, kun taas `OP_NOP` on neutraali eikä vaikuta pinoon eikä komentosarjan kulkuun. Nämä op-koodit nimetään `OP_SUCCESSN`, jossa `N` on numero, jota käytetään erottamaan `OP_SUCCESS`.