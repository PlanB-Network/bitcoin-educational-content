---
term: MERKLE BLOCK

---
Tietorakenne, jota käytetään BIP37:n yhteydessä (*Transaction Bloom Filtering*), jotta voidaan esittää tiivis todiste siitä, että tietyt transaktiot sisältyvät lohkoon. Sitä käytetään erityisesti SPV-lompakoissa. Merkle-lohko sisältää lohkon otsikot, suodatetut transaktiot ja osittaisen Merkle-puun, jonka avulla kevyet asiakkaat voivat nopeasti tarkistaa, kuuluuko transaktio lohkoon lataamatta kaikkia transaktioita.