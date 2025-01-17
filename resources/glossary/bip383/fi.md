---
term: BIP383

---
Otetaan käyttöön funktiot `multi(NUM, KEY, ..., KEY)` ja `sortedmulti(NUM, KEY, ..., KEY)` kuvaajia varten. Nämä funktiot mahdollistavat monimerkkikirjoitusten kuvaamisen kuvaajissa, ja `sortedmulti` lajittelee julkiset avaimet leksikografiseen järjestykseen yhteensopivuuden varmistamiseksi tuonnin aikana. BIP383 toteutettiin yhdessä kaikkien muiden kuvaajiin liittyvien BIP:ien kanssa (paitsi BIP386) Bitcoin Coren versiossa 0.17.