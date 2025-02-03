---
term: VIN

---
Bitcoin-tapahtuman erityinen elementti, joka määrittelee lähteen, josta varat on käytetty tuotosten tyydyttämiseen. Jokainen `vin` viittaa edellisen transaktion käyttämättömään tuotokseen (UTXO). Transaktio voi sisältää useita tuloja, joista jokainen tunnistetaan yhdistelmällä `txid` (alkuperäisen transaktion tunniste) ja `vout` (kyseisen transaktion tuotoksen indeksi).

Jokainen `vin` sisältää seuraavat tiedot:


- `txid`: sen edellisen tapahtuman tunniste, joka sisälsi tässä syötteenä käytetyn tuotoksen;
- `vout`: edellisen tapahtuman tulosteen indeksi;
- `scriptSig` tai `scriptWitness`: lukituksen avaava komentosarja, joka antaa tarvittavat tiedot sen edellisen tapahtuman, jonka varoja käytetään, `scriptPubKey`:n asettamien ehtojen täyttämiseksi, yleensä antamalla salakirjoituksen;
- `nSequence`: erityinen kenttä, jota käytetään osoittamaan, miten tämä tulo on aikalukittu, sekä muita vaihtoehtoja, kuten RBF.