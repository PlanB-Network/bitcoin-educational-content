---
term: DNS SEEDS

---
Alkuperäiset yhteyspisteet uusille Bitcoin-solmuille, jotka liittyvät verkkoon. Näiden siementen, jotka ovat itse asiassa erityisiä DNS-palvelimia, osoite on pysyvästi sisällytetty Bitcoin Core -koodiin. Kun uusi solmu käynnistyy, se ottaa yhteyttä näihin palvelimiin saadakseen satunnaisen luettelon oletettavasti aktiivisten Bitcoin-solmujen IP-osoitteista. Uusi solmu voi sitten luoda yhteyksiä luettelossa oleviin solmuihin saadakseen tiedot, joita se tarvitsee suorittaakseen alustavan lohkolatauksen (Initial Block Download, IBD) ja synkronoituakseen ketjun kanssa, jolla on eniten kertynyttä työtä. Vuodesta 2024 lähtien tässä on luettelo Bitcoin Core DNS-siemenistä ja niiden ylläpidosta vastaavista henkilöistä (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- siemen.bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.bitcoin.wiz.biz: Jason Maurice;
- siemen.mainnet.achownodes.xyz: Ava Chow.

DNS-siemenet ovat tärkeysjärjestyksessä toinen tapa, jolla Bitcoin-solmu voi luoda yhteyksiä. Ensimmäisessä menetelmässä käytetään peers.dat-tiedostoa, jonka solmu on itse luonut. Tämä tiedosto on luonnollisesti tyhjä, jos kyseessä on uusi solmu, ellei käyttäjä ole muokannut sitä manuaalisesti.

> ► *Huomaa, DNS-siemeniä ei pidä sekoittaa "siemensolmuihin", jotka ovat kolmas tapa luoda yhteyksiä.*