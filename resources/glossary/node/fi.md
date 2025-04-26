---
term: NODE

---
Bitcoin-verkossa solmu (englanniksi "node") on tietokone, joka käyttää Bitcoin-protokollan asiakasohjelmaa (kuten esimerkiksi Bitcoin Corea). Se osallistuu verkkoon ylläpitämällä kopiota lohkoketjusta, välittämällä ja vahvistamalla transaktioita ja uusia lohkoja sekä osallistumalla valinnaisesti louhintaprosessiin. Kaikkien Bitcoin-solmujen summa muodostaa itse Bitcoin-verkon.

Bitcoinissa on useita erilaisia solmuja, kuten täyssolmuja ja kevyitä solmuja. Täydelliset solmut säilyttävät täydellisen kopion lohkoketjusta, tarkistavat kaikki transaktiot ja lohkot konsensussääntöjen mukaisesti ja osallistuvat aktiivisesti transaktioiden ja lohkojen levittämiseen verkossa. Kevyet solmut eli SPV-solmut (*Simple Payment Verification*) säilyttävät vain lohkojen otsikot ja ovat riippuvaisia täysistä solmuista saadakseen transaktiotiedot.

> ► *Jotkut erottavat toisistaan myös niin sanotut "karsitut solmut" ("pruned node" englanniksi). Nämä ovat täysiä solmuja, jotka lataavat ja tarkistavat kaikki lohkot Genesis-lohkosta, mutta pitävät muistissa vain viimeisimmät lohkot.* *