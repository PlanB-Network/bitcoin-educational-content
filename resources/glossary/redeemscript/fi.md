---
term: REDEEMSCRIPT

---
Skripti, jossa määritellään erityisehdot, jotka syötteiden on täytettävä, jotta P2SH-ulostuloon liittyvät varat voidaan avata. P2SH UTXO:ssa `scriptPubKey` sisältää `redeemScript`:n hashin. Kun transaktio haluaa käyttää tämän UTXO:n tulona, sen on annettava selkeä `redeemScript`, joka vastaa `scriptPubKey`:n sisältämää hash-arvoa. Näin ollen `redeemScript` annetaan syötteen `scriptSig`:ssä yhdessä muiden skriptin ehtojen täyttämiseksi tarvittavien elementtien, kuten allekirjoitusten tai julkisten avainten, kanssa. Tämä kapseloitu rakenne varmistaa, että käyttöehtojen yksityiskohdat pysyvät piilossa, kunnes bitcoinit todella käytetään. Sitä käytetään erityisesti Legacy P2SH multisignature -lompakoissa.