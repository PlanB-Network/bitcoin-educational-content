---
termi: BLOOM FILTER
---

Probabilistinen tietorakenne, jota käytetään testaamaan, kuuluuko elementti joukkoon. Bloom-suodattimet mahdollistavat nopeat jäsenyyden tarkistukset testaamatta koko datasettiä. Ne ovat erityisen hyödyllisiä konteksteissa, joissa tila ja nopeus ovat kriittisiä, mutta matala ja hallittu virhetaso on hyväksyttävä. Todellakin, Bloom-suodattimet eivät tuota vääriä negatiiveja, mutta ne tuottavat tietyn määrän vääriä positiiveja. Kun elementti lisätään suodattimeen, useat hajautusfunktiot generoivat positioita bittitaulukossa. Jäsenyyden tarkistamiseksi käytetään samoja hajautusfunktioita. Jos kaikki vastaavat bitit on asetettu, elementti on todennäköisesti joukossa, mutta väärien positiivisten riskillä. Bloom-suodattimia käytetään laajalti tietokantojen ja verkkojen aloilla. On erityisesti tunnettua, että Google käyttää niitä tiivistetyssä tietokannan hallintajärjestelmässään *BigTable*. Bitcoin-protokollassa niitä käytetään erityisesti SPV-lompakoissa BIP37:n mukaisesti.

> ► *Kun puhutaan nimenomaan Bloom-suodattimien käytöstä Bitcoin-siirtojen kontekstissa, termi "Transaction Bloom Filtering" kohtaa joskus.*