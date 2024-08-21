---
term: MERKLE-BLOKKI
---

Tietorakenne, jota käytetään BIP37 (*Transaction Bloom Filtering*) yhteydessä tarjoamaan tiivis todiste tiettyjen transaktioiden sisällyttämisestä lohkoon. Sitä käytetään erityisesti SPV-lompakoissa. Merkle-blokki sisältää lohkon otsikot, suodatetut transaktiot ja osittaisen Merkle-puun, jolloin kevyet asiakasohjelmat voivat nopeasti varmistaa, kuuluuko transaktio lohkoon lataamatta kaikkia transaktioita.