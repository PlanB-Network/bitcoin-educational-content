---
term: TRANSAKTIO (TX)

---
Bitcoinin yhteydessä transaktio (lyhenne "TX") on lohkoketjuun kirjattu operaatio, joka siirtää bitcoinien omistusoikeuden yhdestä tai useammasta syötteestä yhteen tai useampaan lähtöön. Kukin transaktio kuluttaa panoksina UTXO:ita (Unspent Transaction Outputs), jotka ovat aiempien transaktioiden tuotoksia, ja luo uusia UTXO:ita tuotoksina, joita voidaan käyttää panoksina tulevissa transaktioissa.

Kukin tulo sisältää viittauksen olemassa olevaan tulosteeseen sekä allekirjoitusskriptin (`scriptSig`), joka täyttää viitteenä olevan tulosteen asettamat käyttöehdot (`scriptPubKey`). Tämän avulla bitcoinit voidaan avata. Tuotokset määrittelevät siirretyille bitcoineille uudet käyttöehdot (`scriptPubKey`), usein julkisen avaimen tai osoitteen muodossa, johon bitcoinit nyt liittyvät.