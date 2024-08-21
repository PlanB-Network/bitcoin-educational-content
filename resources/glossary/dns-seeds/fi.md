---
termi: DNS SEEDS
---

Alkuperäiset yhteyspisteet uusille Bitcoin-noduille, kun ne liittyvät verkkoon. Nämä siemenet, jotka ovat itse asiassa tiettyjä DNS-palvelimia, on pysyvästi sisällytetty Bitcoin Core -koodiin. Kun uusi node käynnistyy, se ottaa yhteyttä näihin palvelimiin saadakseen satunnaisen listan oletettavasti aktiivisten Bitcoin-nodien IP-osoitteista. Uusi node voi sitten muodostaa yhteyksiä tämän listan nodeihin saadakseen tarvittavat tiedot suorittaakseen alkuperäisen lohkon latauksen (IBD) ja synkronoitumaan ketjun kanssa, jolla on eniten kumuloitunutta työtä. Vuodesta 2024 alkaen tässä on lista Bitcoin Core DNS siemenistä ja henkilöistä, jotka vastaavat niiden ylläpidosta (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNS siemenet ovat toinen menetelmä, prioriteettijärjestyksessä, Bitcoin-noden yhteyksien muodostamiseksi. Ensimmäinen menetelmä sisältää peers.dat-tiedoston käyttämisen, jonka node itse on luonut. Tämä tiedosto on luonnollisesti tyhjä uuden noden tapauksessa, ellei käyttäjä ole manuaalisesti muokannut sitä.

> ► *Huomaa, DNS siemeniä ei tule sekoittaa "siirtonodeihin" (seed nodes), jotka ovat kolmas tapa muodostaa yhteyksiä.*