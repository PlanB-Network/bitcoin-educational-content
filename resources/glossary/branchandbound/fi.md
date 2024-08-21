---
termi: BRANCH-AND-BOUND
---

Menetelmä, jota on käytetty syötteiden valitsemiseen Bitcoin Core -lompakossa versiosta 0.17 lähtien ja jonka keksi Murch. Branch-and-Bound (BnB) on haku, jonka tavoitteena on löytää joukko UTXO:ja, jotka vastaavat tarkalleen transaktiossa täytettävien lähtöjen määrää, jotta voidaan minimoida vaihtorahan määrä ja siihen liittyvät maksut. Sen tavoitteena on vähentää hukkakriteeriä, joka ottaa huomioon sekä välittömät kustannukset että vaihtorahasta odotetut tulevat kustannukset. Tämä menetelmä on tarkempi maksujen suhteen verrattuna aiempiin heuristiikkoihin, kuten *Knapsack Solver*. *Branch-and-Bound* on saanut inspiraationsa samannimisestä ongelmanratkaisumenetelmästä, jonka keksivät Ailsa Land ja Alison Harcourt vuonna 1960.

> ► *Tätä menetelmää kutsutaan joskus myös "Murchin algoritmiksi" sen keksijän mukaan.*