---
termi: OSOITTEEN UUDELLEENKÄYTTÖ
---

Osoitteen uudelleenkäyttö viittaa käytäntöön, jossa samaa vastaanotto-osoitetta käytetään useiden UTXO:iden estämiseen, joskus useiden eri siirtojen yhteydessä. Bitcoinit lukitaan tyypillisesti käyttäen kryptografista avainparia, joka vastaa uniikkia osoitetta. Koska lohkoketju on julkinen, on helppo nähdä, mitkä osoitteet ovat yhdistetty kuinka moniin bitcoineihin. Saman osoitteen uudelleenkäytössä useisiin maksuihin on järkevää kuvitella, että kaikki liitetyt UTXO:t kuuluvat samalle taholle. Siksi osoitteen uudelleenkäyttö aiheuttaa ongelman käyttäjän yksityisyydelle. Se mahdollistaa deterministiset linkit useiden siirtojen ja UTXO:iden välillä sekä edistää on-chain varojen seurantaa. Satoshi Nakamoto mainitsi jo tämän ongelman White Paperissaan:

> "*Lisäsuojana voitaisiin käyttää jokaista siirtoa varten uutta avainparia, jotta ne eivät liittyisi yhteiseen omistajaan.*" - Nakamoto, S. (2008). "Bitcoin: Vertaisverkkoon perustuva elektroninen käteisjärjestelmä". Konsultoitu osoitteessa https://bitcoin.org/bitcoin.pdf.

Yksityisyyden säilyttämiseksi vähimmäistasolla on vahvasti suositeltavaa käyttää kutakin vastaanotto-osoitetta vain kerran. Jokaista uutta maksua varten on sopivaa generoida uusi osoite. Myös vaihtorahojen osalta tulisi käyttää uutta osoitetta. Onneksi determinististen ja hierarkkisten lompakoiden ansiosta monien osoitteiden käyttäminen on muuttunut erittäin helpoksi. Kaikki lompakkoon liitetyt avainparit voidaan helposti uudelleengeneroida siemenestä. Tämä on myös syy, miksi lompakko-ohjelmisto aina generoi uuden, erilaisen osoitteen, kun klikkaat "Vastaanota" -painiketta.

> ► *Englanniksi sitä kutsutaan "Address Reuse".*