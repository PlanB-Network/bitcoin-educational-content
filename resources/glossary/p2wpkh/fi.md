---
termi: P2WPKH
---

P2WPKH tarkoittaa *Maksa todistajan julkisen avaimen hajautusarvoon*. Se on standardi skriptimalli, jota käytetään UTXO:n kulutusehtojen määrittämiseen. P2WPKH otettiin käyttöön SegWitin toteutuksen yhteydessä elokuussa 2017.

Tämä skripti on samankaltainen kuin P2PKH (*Maksa julkisen avaimen hajautusarvoon*), sillä se myös lukitsee bitcoineja perustuen julkisen avaimen, eli vastaanotto-osoitteen, hajautusarvoon. Ero on siinä, miten allekirjoitukset ja skriptit sisällytetään transaktioon. P2WPKH:n tapauksessa allekirjoitusskriptin tiedot (`scriptSig`) siirretään perinteisestä transaktiorakenteesta erilliseen osioon nimeltä `Witness`. Tämä siirto on osa SegWit (*Segregated Witness*) -päivitystä, joka auttaa estämään allekirjoituksen muunneltavuutta. P2WPKH-transaktiot ovat yleensä edullisempia maksujen suhteen verrattuna perinteisiin transaktioihin, koska todistajan osassa oleva osa maksaa vähemmän.

P2WPKH-osoitteet kirjoitetaan käyttäen `Bech32`-koodausta tarkistussummalla, joka on muodossa BCH-koodi. Nämä osoitteet alkavat aina `bc1q`. P2WPKH on versio 0 SegWit-lähtö.