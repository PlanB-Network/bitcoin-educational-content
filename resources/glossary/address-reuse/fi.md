---
term: ADRESSIN KIERRÄTYS

---
Osoitteen uudelleenkäytöllä tarkoitetaan käytäntöä, jossa samaa vastaanottoosoitetta käytetään useiden UTXO:iden estämiseen, joskus useiden eri tapahtumien sisällä. Bitcoineja lukitaan tyypillisesti kryptografisella avainparilla, joka vastaa yksilöllistä osoitetta. Koska lohkoketju on julkinen, on helppo nähdä, mihin osoitteisiin liittyy kuinka monta bitcoinia. Jos samaa osoitetta käytetään uudelleen useisiin maksuihin, on järkevää kuvitella, että kaikki siihen liittyvät UTXO:t kuuluvat samalle taholle. Osoitteiden uudelleenkäyttö aiheuttaa siis ongelman käyttäjän yksityisyydelle. Se mahdollistaa determinististen yhteyksien luomisen useiden transaktioiden ja UTXO:iden välille sekä säilyttää ketjussa tapahtuvan rahastojen seurannan. Satoshi Nakamoto mainitsi tämän ongelman jo valkoisessa kirjassaan:

> "*Lisäpalomuurina voitaisiin käyttää uutta avainparia jokaista transaktiota varten, jotta niitä ei voitaisi yhdistää yhteiseen omistajaan.*" - Nakamoto, S. (2008). "Bitcoin: Peer-to-Peer sähköinen rahajärjestelmä". Luettu osoitteessa https://bitcoin.org/bitcoin.pdf.
Yksityisyyden säilyttämiseksi on erittäin suositeltavaa käyttää kutakin vastaanottavaa osoitetta vain kerran. Jokaista uutta maksua varten on syytä luoda uusi osoite. Myös muutostuloja varten olisi käytettävä uutta osoitetta. Onneksi determinististen ja hierarkkisten lompakoiden ansiosta useiden osoitteiden käyttäminen on tullut erittäin helpoksi. Kaikki lompakkoon liittyvät avainparit voidaan helposti luoda uudelleen siemenestä. Tästä syystä lompakko-ohjelmistot luovat myös aina uuden, eri osoitteen, kun napsautat "Vastaanota"-painiketta.

> ► *Englanniksi sitä kutsutaan "Address Reuse".*