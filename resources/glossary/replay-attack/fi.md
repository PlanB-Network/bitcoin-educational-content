---
term: REPLAY ATTACK
---

Bitcoin:n yhteydessä toistohyökkäys tapahtuu, kun yhdessä Blockchain:ssa tehty pätevä tapahtuma toistetaan ilkivaltaisesti toisessa Blockchain:ssa, jolla on sama tapahtumahistoria. Toisin sanoen yhdellä kanavalla lähetetty tapahtuma voidaan toistaa toisella kanavalla ilman ensimmäisen tapahtuman lähettäjän suostumusta.


Otetaan esimerkiksi hypoteettinen Hard Fork Bitcoin:sta, jonka nimi on "*BitcoinBis*". Jos suoritat maksun bitcoineilla ostaaksesi patongin leipurilta todellisessa Blockchain Bitcoin:ssa, sama leipuri voisi toistaa tämän laillisen tapahtuman *BitcoinBis*:ssä saadakseen saman summan kryptovaluuttoina tässä Fork:ssä ilman, että sinä itse toimit.


Tämäntyyppinen hyökkäys voi tapahtua vain, jos Blockchain haarautuu kahdella itsenäisellä ketjulla, jotka säilyvät ajan myötä. Tyypillisesti tämä on tilanne Hard Fork:n tapauksessa. Jotta replay-hyökkäys olisi mahdollinen, kahdella lohkoketjulla on oltava yhteinen historia, ja monistetun transaktion on käytettävä syötteenä UTXO:ita, jotka on luotu aiemmista transaktioista, jotka tapahtuivat ennen kahden ketjun jakautumista, tai aiemmista transaktioista, jotka on jo itse uusittu aiemmassa replay-hyökkäyksessä.


Yleisesti ottaen tietojenkäsittelyssä toistohyökkäys koostuu voimassa olevan tiedon sieppaamisesta ja uudelleenkäytöstä järjestelmän huijaamiseksi toistamalla alkuperäinen lähetys. Tämä voi joskus johtaa identiteettivarkauteen verkossa.


> ► *Jos kyseessä on Bitcoin-tapahtuman toistohyökkäys, tähän viitataan joskus yksinkertaisesti "toistotapahtumana". "*