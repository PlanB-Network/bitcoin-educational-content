---
term: BRANCH-AND-BOUND

---
Menetelmä, jota käytetään syötteiden valintaan Bitcoin Core -lompakossa versiosta 0.17 lähtien ja jonka on keksinyt Murch. Branch-and-Bound (BnB) on haku, jolla etsitään UTXO-joukko, joka vastaa täsmälleen transaktiossa täytettävien tuotosten määrää, jotta muutos ja siihen liittyvät maksut voidaan minimoida. Sen tavoitteena on vähentää hukkakriteeriä, jossa otetaan huomioon sekä välittömät kustannukset että muutoksesta odotettavissa olevat tulevat kustannukset. Tämä menetelmä on tarkempi maksujen suhteen verrattuna aiempiin heuristiikkoihin, kuten *Knapsack Solver*. *Branch-and-Bound* on saanut innoituksensa samannimisestä ongelmanratkaisumenetelmästä, jonka Ailsa Land ja Alison Harcourt keksivät vuonna 1960.

> ► *Tätä menetelmää kutsutaan joskus myös "Murchin algoritmiksi" sen keksijän mukaan.*