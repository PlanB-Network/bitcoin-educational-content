---
termi: BIP49
---

BIP49 on informatiivinen BIP, joka esittelee johdannaisen menetelmän, jota käytetään luomaan sisäkkäisiä SegWit-osoitteita HD-lompakossa. Ehdotettu johdannaispolku noudattaa BIP43:n ja BIP44:n standardeja, indeksillä `49'` (vahvistettu johdannainen) tavoitteen syvyydessä. Esimerkiksi ensimmäinen osoite P2SH-P2WPKH-tililtä johdettaisiin polusta: `m/49'/0'/0'/0/0`. Sisäkkäiset SegWit-skriptit keksittiin SegWitin käynnistyessä helpottamaan sen omaksumista. Ne mahdollistavat tämän uuden standardin käytön, jopa lompakoissa, jotka eivät vielä ole natiivisti yhteensopivia SegWitin kanssa.