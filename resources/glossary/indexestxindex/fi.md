---
termi: INDEXES/TXINDEX/
---

Tiedostot Bitcoin Core:ssa, jotka on omistettu indeksoimaan kaikki lohkoketjussa olevat transaktiot. Tämä indeksointi mahdollistaa nopean haun tietyn transaktion yksityiskohtaisista tiedoista käyttäen sen tunnistetta (TXID), ilman että koko lohkoketjun läpikäynti on tarpeen. Näiden indeksointitiedostojen luominen ei ole oletusarvoisesti käytössä Bitcoin Core:ssa. Jos tätä ominaisuutta ei ole otettu käyttöön, solmusi indeksoi vain ne transaktiot, jotka liittyvät solmuusi liitettyihin lompakoihin. Kaikkien transaktioiden indeksoinnin mahdollistamiseksi sinun on asetettava parametri `-txindex=1` `bitcoin.conf`-tiedostoon. Tämä vaihtoehto on erityisen hyödyllinen sovelluksille ja palveluille, jotka usein etsivät tietoja Bitcoinin transaktiohistoriasta.