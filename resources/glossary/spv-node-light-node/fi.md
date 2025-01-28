---
term: SPV-SOLMU (VALOSOLMU)

---
SPV-solmu (*Simple Payment Verification*), jota kutsutaan joskus "kevyeksi solmuksi", on Bitcoin-solmun kevyt asiakasohjelma, jonka avulla käyttäjät voivat validoida transaktioita ilman koko lohkoketjun tallentamista. Sen sijaan SPV-solmu tallentaa vain lohkootsikot ja saa tarvittaessa tietoja tietyistä transaktioista kyselemällä täysiltä solmuilta. Tämän todentamisperiaatteen mahdollistaa Bitcoin-lohkojen transaktioiden rakenne, joka on järjestetty kryptografiseen akkuun (Merkle Tree).

Tämä lähestymistapa on edullinen laitteissa, joissa resurssit ovat rajalliset, kuten matkapuhelimissa. SPV-solmut ovat kuitenkin riippuvaisia täydellisistä solmuista tietojen saatavuuden osalta, mikä merkitsee ylimääräistä luottamusta ja näin ollen heikompaa turvallisuutta verrattuna täydellisiin solmuihin. SPV-solmut eivät voi validoida transaktioita itsenäisesti, mutta ne voivat tarkistaa, sisältyykö transaktio lohkoon, tutustumalla Merkle-todistuksiin.