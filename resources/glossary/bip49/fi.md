---
term: BIP49

---
BIP49 on informatiivinen BIP, jossa esitellään johdantomenetelmä, jota käytetään Nested SegWit -osoitteiden luomiseen HD-lompakossa. Ehdotettu johdannaispolku noudattaa BIP43:n ja BIP44:n standardeja, ja tavoitteen syvyydessä on indeksi `49'` (kovennettu johdanto). Esimerkiksi P2SH-P2WPKH-tilin ensimmäinen osoite johdettaisiin polusta: `m/49'/0'/0'/0/0`. Sisäkkäiset SegWit-skriptit keksittiin SegWitin käyttöönoton yhteydessä helpottamaan sen käyttöönottoa. Ne mahdollistavat tämän uuden standardin käytön myös lompakoissa, jotka eivät vielä ole natiivisti yhteensopivia SegWitin kanssa.