---
termi: OP_SUCCESS
---

`OP_SUCCESS` edustaa sarjaa operaatiokoodeja, jotka olivat aiemmin poistettu käytöstä ja ovat nyt varattu tulevaa käyttöä varten Tapscriptissä. Niiden lopullisena tavoitteena on helpottaa skriptikielen päivityksiä ja laajennuksia, sallimalla uusien toiminnallisuuksien käyttöönotto pehmeiden haarautumisten (soft forks) kautta. Kun skriptissä kohdataan yksi näistä operaatiokoodeista, se merkitsee kyseisen osan automaattista onnistumista skriptissä, riippumatta läsnä olevista tiedoista tai ehdoista. Tämä tarkoittaa, että skripti jatkaa suoritustaan ilman epäonnistumista, riippumatta aiemmista operaatioista.

Näin ollen, kun uusi operaatiokoodi lisätään `OP_SUCCESS`-kohtaan, se välttämättä edustaa aiempaa rajoittavamman säännön lisäystä. Päivitetyt solmut voivat sitten varmistaa tämän säännön noudattamisen, ja päivittämättömät solmut eivät hylkää näihin liittyviä transaktioita ja niitä sisältäviä lohkoja, koska `OP_SUCCESS` vahvistaa skriptin kyseisen osan. Siksi kovaa haarautumista (hard fork) ei tapahdu.

Vertailun vuoksi, `OP_NOP` (*Ei Operaatiota*) toimii myös paikkamerkkeinä skriptissä, mutta ne eivät vaikuta skriptin suoritukseen. Kun `OP_NOP` kohdataan, skripti yksinkertaisesti jatkuu muuttamatta pinon tilaa tai skriptin etenemistä. Keskeinen ero on siis niiden vaikutuksessa suoritukseen: `OP_SUCCESS` takaa onnistuneen läpimenon kyseisestä skriptin osasta, kun taas `OP_NOP` on neutraali eikä vaikuta joko pinoon tai skriptin kulkuun. Nämä operaatiokoodit on merkitty `OP_SUCCESSN`, missä `N` on numero, jota käytetään erottamaan `OP_SUCCESS`.