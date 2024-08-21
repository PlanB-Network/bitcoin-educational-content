---
termi: TRANSAKTIO (TX)
---

Bitcoinin kontekstissa transaktio (lyhennettynä "TX") on lohkoketjuun kirjattu toimenpide, joka siirtää bitcoinien omistajuuden yhdestä tai useammasta syötteestä yhteen tai useampaan tulosteeseen. Jokainen transaktio kuluttaa käyttämättömiä transaktioulosteita (UTXOita) syötteinä, jotka ovat aikaisempien transaktioiden tulosteita, ja luo uusia UTXOita tulosteina, joita voidaan käyttää syötteinä tulevissa transaktioissa.

Jokainen syöte sisältää viittauksen olemassa olevaan tulosteeseen yhdessä allekirjoitusskriptin (`scriptSig`) kanssa, joka täyttää tulosteen asettamat käyttöehdot (`scriptPubKey`). Tämä mahdollistaa bitcoinien vapauttamisen. Tulosteet määrittelevät uudet käyttöehdot (`scriptPubKey`) siirretyille bitcoineille, usein julkisen avaimen tai osoitteen muodossa, johon bitcoinit nyt liittyvät.