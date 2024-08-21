---
termi: VIN
---

Erityinen elementti Bitcoin-siirrossa, joka määrittelee varojen lähteen, joita käytetään tulosteiden täyttämiseen. Jokainen `vin` viittaa käyttämättömään tulosteeseen (UTXO) aiemmasta siirrosta. Siirrossa voi olla useita syötteitä, jotka kullakin tunnistetaan yhdistelmällä `txid` (alkuperäisen siirron tunniste) ja `vout` (tulosteen indeksi kyseisessä siirrossa).

Jokainen `vin` sisältää seuraavat tiedot:
* `txid`: edellisen siirron tunniste, joka sisältää tässä käytettävänä syötteenä olevan tulosteen;
* `vout`: tulosteen indeksi edellisessä siirrossa;
* `scriptSig` tai `scriptWitness`: avauskäsikirjoitus, joka tarjoaa tarvittavat tiedot edellisen siirron `scriptPubKey`n asettamien ehtojen täyttämiseen, yleensä tarjoamalla kryptografisen allekirjoituksen;
* `nSequence`: erityinen kenttä, jota käytetään osoittamaan, miten tämä syöte on aika-lukittu, sekä muita vaihtoehtoja kuten RBF.