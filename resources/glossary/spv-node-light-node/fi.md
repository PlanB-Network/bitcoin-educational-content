---
termi: SPV-NODE (KEVYT NODE)
---

SPV (*Simple Payment Verification*) node, jota joskus kutsutaan "kevyeksi nodeksi", on kevyt Bitcoin-noden asiakasohjelma, joka mahdollistaa käyttäjille transaktioiden vahvistamisen ilman, että heidän tarvitsee tallentaa koko lohkoketjua. SPV-node tallentaa ainoastaan lohkojen otsikot ja hankkii tietoa tiettyjä transaktioita koskien kyselyillä täysnodeilta tarvittaessa. Tämä vahvistusperiaate on mahdollinen Bitcoin-lohkojen transaktioiden rakenteen ansiosta, jotka on järjestetty kryptografisessa kumuloijassa (Merkle-puu).

Tämä lähestymistapa on edullinen resurssien kannalta rajoitetuille laitteille, kuten matkapuhelimille. Kuitenkin, SPV-nodet luottavat täysnodeihin tiedon saatavuudessa, mikä tarkoittaa lisättyä luottamustason tarvetta ja siten vähemmän turvallisuutta verrattuna täysnodeihin. SPV-nodet eivät voi vahvistaa transaktioita itsenäisesti, mutta ne voivat tarkistaa, sisältyykö transaktio lohkoon konsultoimalla Merkle-todisteita.