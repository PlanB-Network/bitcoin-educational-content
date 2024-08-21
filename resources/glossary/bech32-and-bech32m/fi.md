`Bech32` ja `Bech32m` ovat kaksi osoitteen koodausformaattia bitcoineja vastaanottamiseen. Ne perustuvat hieman muokattuun 32-kantaiseen järjestelmään. Ne sisältävät tarkistussumman, joka perustuu virheenkorjausalgoritmiin nimeltä BCH (*Bose-Chaudhuri-Hocquenghem*). Legacy-osoitteisiin verrattuna, jotka on koodattu `Base58check`-muodossa, `Bech32`- ja `Bech32m`-osoitteilla on tehokkaampi tarkistussumma, joka mahdollistaa kirjoitusvirheiden havaitsemisen ja mahdollisesti automaattisen korjauksen. Niiden formaatti tarjoaa myös paremman luettavuuden, käyttäen vain pieniä kirjaimia. Tässä on lisäysmatriisi tässä formaatissa kymmenkantaisesta järjestelmästä:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;
Bech32 ja Bech32m ovat koodausformaattia, joita käytetään edustamaan SegWit-osoitteita. Bech32 on osoitteen koodausformaatti, jonka BIP173 esitteli vuonna 2017. Se käyttää tiettyä merkkijoukkoa, joka koostuu numeroista ja pienistä kirjaimista, minimoimaan kirjoitusvirheet ja helpottamaan lukemista. Bech32-osoitteet alkavat yleensä `bc1`:llä osoittaakseen, että ne ovat natiiveja SegWitille. Tätä formaattia käytetään vain SegWit V0 -osoitteissa, skripteillä P2WPKH (Pay to Witness Public Key Hash) ja P2WSH (Pay to Witness Script Hash). Kuitenkin, Bech32-formaatissa on pieni, odottamaton vika. Kun osoitteen viimeinen merkki on `p`, mikä tahansa määrä `q`-kirjaimia välittömästi sen edellä ei tee tarkistussummasta virheellistä. Tämä ei vaikuta SegWit V0 -osoitteiden (BIP173) olemassa olevaan käyttöön niiden rajoittuessa kahteen määriteltyyn pituuteen. Tämä voisi kuitenkin vaikuttaa Bech32-koodauksen tuleviin käyttötarkoituksiin. Bech32m-formaatti on yksinkertaisesti Bech32-formaatti, jossa tämä virhe on korjattu. Se esiteltiin BIP350:ssä vuonna 2020. Bech32m-osoitteet alkavat myös `bc1`:llä, mutta ne on erityisesti suunniteltu olemaan yhteensopivia SegWit V1:n (Taproot) ja myöhempien versioiden kanssa, skriptillä P2TR (Pay to TapRoot).