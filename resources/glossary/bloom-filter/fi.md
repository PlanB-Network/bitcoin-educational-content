---
term: BLOOM FILTER

---
Todennäköisyystietorakenne, jota käytetään testaamaan, kuuluuko jokin elementti joukkoon. Bloom-suodattimet mahdollistavat nopeat jäsenyyden tarkistukset testaamatta koko tietokantaa. Ne ovat erityisen käyttökelpoisia tilanteissa, joissa tila ja nopeus ovat kriittisiä, mutta pieni ja hallittu virhetaso on hyväksyttävä. Bloom-suodattimet eivät tuota vääriä negatiivisia tuloksia, mutta ne tuottavat tietyn määrän vääriä positiivisia tuloksia. Kun suodattimeen lisätään elementti, useat hash-funktiot tuottavat paikkoja bittimassassa. Jäsenyyden tarkistamiseen käytetään samoja hash-funktioita. Jos kaikki vastaavat bitit ovat asetettuina, elementti on todennäköisesti joukossa, mutta riskinä on väärien positiivisten tulosten syntyminen. Bloom-suodattimia käytetään laajalti tietokantojen ja verkkojen alalla. Google käyttää niitä erityisesti pakatun tietokannan hallintajärjestelmässään *BigTable*. Bitcoin-protokollassa niitä käytetään erityisesti BIP37:n mukaisissa SPV-lompakoissa.

> ► *Kun puhutaan erityisesti Bloom-suodattimien käytöstä Bitcoin-tapahtumien yhteydessä, käytetään joskus termiä "Transaction Bloom Filtering".*