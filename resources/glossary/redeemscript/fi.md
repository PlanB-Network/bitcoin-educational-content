---
termi: REDEEMSCRIPT
---

Skripti, joka määrittelee tarkat ehdot, jotka syötteiden on täytettävä varojen vapauttamiseksi, jotka liittyvät P2SH-lähtöön. P2SH UTXO:ssa `scriptPubKey` sisältää `redeemScript`-skriptin hajautusarvon. Kun transaktio haluaa käyttää tätä UTXO:a syötteenä, sen on toimitettava selvä `redeemScript`, joka vastaa `scriptPubKey`-sisältämää hajautusarvoa. `redeemScript` annetaan näin ollen syötteen `scriptSig`-osassa yhdessä muiden elementtien kanssa, jotka ovat tarpeen skriptin ehtojen täyttämiseksi, kuten allekirjoitukset tai julkiset avaimet. Tämä kapseloitu rakenne varmistaa, että kulutusehtojen yksityiskohdat pysyvät piilossa kunnes bitcoinit todella kulutetaan. Sitä käytetään erityisesti Legacy P2SH moniallekirjoituslompakoissa.