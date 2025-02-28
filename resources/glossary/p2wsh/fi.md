---
term: P2WSH

---
P2WSH tarkoittaa *Pay to Witness Script Hash*. Se on vakioskriptimalli, jota käytetään UTXO:n käyttöehtojen määrittämiseen. P2WSH otettiin käyttöön SegWitin käyttöönoton myötä elokuussa 2017.

Tämä skripti on samanlainen kuin P2SH (*Pay to Public Script Hash*), sillä se myös lukitsee bitcoineja skriptin hashin perusteella. Ero on siinä, miten allekirjoitukset ja skriptit sisällytetään transaktioon. Käyttääkseen bitcoineja tämäntyyppiseen skriptiin vastaanottajan on toimitettava alkuperäinen skripti, nimeltään `witnessScript` (vastaa `redeemScript`), sekä vaaditut allekirjoitukset. Tämä mekanismi mahdollistaa monimutkaisempien tuhlausedellytysten, kuten multisigien, toteuttamisen.

P2WSH:n yhteydessä allekirjoitusskriptitiedot (`scriptWitness`, joka vastaa `scriptSig`) siirretään perinteisestä transaktiorakenteesta erilliseen osioon nimeltä `Witness`. Tämä siirto on SegWit-päivityksen (*Segregated Witness*) ominaisuus, joka auttaa estämään allekirjoitusten väärentämisen. P2WSH-tapahtumat ovat yleensä edullisempia maksujen osalta verrattuna Legacy-tapahtumiin, koska todistajan osuus maksaa vähemmän.

P2WSH-osoitteet kirjoitetaan käyttäen `Bech32`-koodausta, jossa on BCH-koodin muodossa oleva tarkistussumma. Nämä osoitteet alkavat aina kirjaimella `bc1q`. P2WSH on SegWit-version 0 lähtö.