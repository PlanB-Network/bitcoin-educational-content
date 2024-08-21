---
termi: P2WSH
---

P2WSH tarkoittaa *Maksa todistusskriptin hajautusarvoon*. Se on standardi skriptimalli, jota käytetään UTXO:n käyttöehtojen määrittämiseen. P2WSH otettiin käyttöön SegWitin toteutuksen yhteydessä elokuussa 2017.

Tämä skripti on samankaltainen kuin P2SH (*Maksa julkisen skriptin hajautusarvoon*), sillä se myös lukitsee bitcoineja skriptin hajautusarvon perusteella. Ero on siinä, miten allekirjoitukset ja skriptit sisällytetään transaktioon. Jotta bitcoinit tällaisesta skriptistä voisi käyttää, vastaanottajan on toimitettava alkuperäinen skripti, jota kutsutaan `witnessScript` (vastaa `redeemScript`), yhdessä vaadittujen allekirjoitusten kanssa. Tämä mekanismi mahdollistaa monimutkaisempien käyttöehtojen, kuten multisigien, toteuttamisen.

P2WSH:n kontekstissa allekirjoitusskriptin tiedot (eli `scriptWitness`, vastaa `scriptSig`) siirretään perinteisestä transaktiorakenteesta erilliseen osioon nimeltä `Witness`. Tämä siirto on SegWit-päivityksen (*Segregated Witness*) ominaisuus, joka auttaa estämään allekirjoituksen muuntelun. P2WSH-transaktiot ovat yleensä edullisempia maksujen suhteen verrattuna perinteisiin transaktioihin, sillä witness-osiossa oleva osa maksaa vähemmän.

P2WSH-osoitteet kirjoitetaan käyttäen `Bech32`-koodausta, jossa on tarkistussumma BCH-koodin muodossa. Nämä osoitteet alkavat aina `bc1q`-alkuisina. P2WSH on SegWitin versio 0 -tulos.