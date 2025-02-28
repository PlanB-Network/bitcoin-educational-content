---
term: BECH32 JA BECH32M

---
`Bech32` ja `Bech32m` ovat kaksi osoitekoodausmuotoa bitcoinien vastaanottamiseen. Ne perustuvat hieman muunneltuun 32:een. Ne sisältävät tarkistussumman, joka perustuu virheenkorjausalgoritmiin nimeltä BCH (*Bose-Chaudhuri-Hocquenghem*). Verrattuna Legacy-osoitteisiin, jotka on koodattu `Base58check`-menetelmällä, `Bech32`- ja `Bech32m`-osoitteissa on tehokkaampi tarkistussumma, joka mahdollistaa kirjoitusvirheiden havaitsemisen ja mahdollisesti automaattisen korjaamisen. Niiden muoto on myös luettavuudeltaan parempi, sillä niissä käytetään vain pieniä kirjaimia. Tässä on tämän muodon yhteenlaskumatriisi 10:stä lähtien:

&nbsp;

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | q | p | z | r | y | 9 | x | 8 | 8 |

| 8 | g | f | 2 | t | v | d | w | 0 | |

| 16 | s | 3 | j | n | 5 | 4 | k | h | 5 | 4 | k | k | h |

| 24 | c | e | 6 | m | u | a | 7 | l | 6 | m | u | a | 7 | l |

&nbsp;

Bech32 ja Bech32m ovat koodausmuotoja, joita käytetään SegWit-osoitteiden esittämiseen. Bech32 on osoitekoodausmuoto, jonka BIP173 otti käyttöön vuonna 2017. Se käyttää tiettyä numeroista ja pienistä kirjaimista koostuvaa merkkijoukkoa kirjoitusvirheiden minimoimiseksi ja lukemisen helpottamiseksi. Bech32-osoitteet alkavat yleensä kirjaimella `bc1` osoittaakseen, että ne ovat SegWit-alkuperäisiä. Tätä muotoa käytetään vain SegWit V0 -osoitteissa, joissa on skriptit P2WPKH (Pay to Witness Public Key Hash) ja P2WSH (Pay to Witness Script Hash). Bech32-formaatissa on kuitenkin pieni, odottamaton virhe. Aina kun osoitteen viimeinen merkki on "p", sitä välittömästi edeltävien "q"-merkkien lisääminen tai poistaminen ei tee tarkistussummaa tyhjäksi. Tämä ei vaikuta SegWit V0 -osoitteiden (BIP173) nykyiseen käyttöön, koska ne on rajoitettu kahteen määriteltyyn pituuteen. Tämä voi kuitenkin vaikuttaa Bech32-koodauksen tulevaan käyttöön. Bech32m-muoto on yksinkertaisesti Bech32-muoto, jossa tämä virhe on korjattu. Se otettiin käyttöön BIP350-muodossa vuonna 2020. Bech32m-osoitteet alkavat myös kirjaimella `bc1`, mutta ne on suunniteltu erityisesti yhteensopiviksi SegWit V1:n (Taproot) ja sitä uudempien versioiden kanssa käsikirjoituksen P2TR (Pay to TapRoot) avulla.