---
term: P2WPKH

---
P2WPKH tarkoittaa *Pay to Witness Public Key Hash*. Se on vakioskriptimalli, jota käytetään UTXO:n käyttöehtojen määrittämiseen. P2WPKH otettiin käyttöön SegWitin käyttöönoton myötä elokuussa 2017.

Tämä skripti on samanlainen kuin P2PKH (*Pay to Public Key Hash*), sillä se myös lukitsee bitcoineja julkisen avaimen eli vastaanottavan osoitteen hash-arvon perusteella. Ero on siinä, miten allekirjoitukset ja skriptit sisällytetään transaktioon. P2WPKH:n tapauksessa allekirjoituksen käsikirjoitustiedot (`scriptSig`) on siirretty perinteisestä transaktiorakenteesta erilliseen osioon nimeltä `Witness`. Tämä siirto on SegWit-päivityksen (*Segregated Witness*) ominaisuus, joka auttaa estämään allekirjoitusten väärentämisen. P2WPKH-tapahtumat ovat yleensä edullisempia maksujen osalta verrattuna Legacy-tapahtumiin, koska todistajan osuus maksaa vähemmän.

P2WPKH-osoitteet kirjoitetaan käyttäen `Bech32`-koodausta ja BCH-koodin muodossa olevaa tarkistussummaa. Nämä osoitteet alkavat aina kirjaimella `bc1q`. P2WPKH on SegWit-version 0 tuotos.