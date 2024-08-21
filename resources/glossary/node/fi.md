---
termi: NODE
---

Bitcoin-verkossa solmu (tai "node" englanniksi) on tietokone, joka suorittaa Bitcoin-protokollan asiakasohjelmaa (kuten esimerkiksi Bitcoin Core). Se osallistuu verkkoon ylläpitämällä kopion lohkoketjusta, välittämällä ja vahvistamalla siirtoja ja uusia lohkoja, ja valinnaisesti, osallistumalla louhintaprosessiin. Kaikkien Bitcoin-solmujen summa edustaa itse Bitcoin-verkkoa.

Bitcoinissa on useita erityyppisiä solmuja, mukaan lukien täyssolmut ja kevytsolmut. Täyssolmut pitävät yllä täydellistä kopiota lohkoketjusta, vahvistavat kaikki siirrot ja lohkot konsensus sääntöjen mukaisesti, ja osallistuvat aktiivisesti siirtojen ja lohkojen levittämiseen verkossa. Toisaalta, kevytsolmut eli SPV (*Simple Payment Verification*) solmut, säilyttävät vain lohkojen otsikot ja luottavat täyssolmuihin saadakseen siirtotiedot.

> ► *Jotkut tekevät eron niin sanottujen "karsittujen solmujen" ("pruned node" englanniksi) välillä. Nämä ovat täyssolmuja, jotka lataavat ja vahvistavat kaikki lohkot Genesis-lohkosta lähtien, mutta säilyttävät vain viimeisimmät lohkot muistissa.*