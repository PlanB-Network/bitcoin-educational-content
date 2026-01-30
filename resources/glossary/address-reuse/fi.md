---
term: Osoitteen uudelleenkäyttö

definition: Ei-suositeltu käytäntö, jossa käytetään samaa Bitcoin-osoitetta useita kertoja maksujen vastaanottamiseen, mikä vahingoittaa yksityisyyttä sallimalla varojen jäljittämisen.
---
Osoitteen uudelleenkäytöllä tarkoitetaan käytäntöä, jossa samaa vastaanottoosoitetta käytetään useiden UTXO:iden estämiseen, joskus useiden eri tapahtumien sisällä. Bitcoineja lukitaan tyypillisesti kryptografisella avainparilla, joka vastaa yksilöllistä osoitetta. Koska lohkoketju on julkinen, on helppo nähdä, mihin osoitteisiin liittyy kuinka monta bitcoinia. Jos samaa osoitetta käytetään uudelleen useisiin maksuihin, on järkevää kuvitella, että kaikki siihen liittyvät UTXO:t kuuluvat samalle taholle. Osoitteiden uudelleenkäyttö aiheuttaa siis ongelman käyttäjän yksityisyydelle. Se mahdollistaa determinististen yhteyksien luomisen useiden transaktioiden ja UTXO:iden välille sekä säilyttää ketjussa tapahtuvan rahastojen seurannan. Satoshi Nakamoto mainitsi tämän ongelman jo valkoisessa kirjassaan:

> *Lisäpalomuurina jokaista tapahtumaa varten tulisi käyttää uutta avainparia, jotta niitä ei voitaisi yhdistää samaan omistajaan.*

Nakamoto, S. (2008). "*Bitcoin: A Peer-to-Peer Electronic Cash System*". https://bitcoin.org/bitcoin.pdf.

Yksityisyyden säilyttämiseksi on erittäin suositeltavaa käyttää kutakin vastaanottavaa osoitetta vain kerran. Jokaista uutta maksua varten on syytä luoda uusi osoite. Myös muutostuloja varten olisi käytettävä uutta osoitetta. Onneksi determinististen ja hierarkkisten lompakoiden ansiosta useiden osoitteiden käyttäminen on tullut erittäin helpoksi. Kaikki lompakkoon liittyvät avainparit voidaan helposti luoda uudelleen siemenestä. Tästä syystä lompakko-ohjelmistot luovat myös aina uuden, eri osoitteen, kun napsautat "Vastaanota"-painiketta.
