---
term: DNS SEEMNED
---

Esialgsed ühenduspunktid uutele Bitcoin'i sõlmedele võrguga liitumisel. Need seemned, mis on tegelikult spetsiifilised DNS serverid, on nende aadressid püsivalt sisse kodeeritud Bitcoin Core koodi. Kui uus sõlm käivitub, võtab see nende serveritega ühendust, et saada juhuslik nimekiri IP aadressidest, mis eeldatavasti on aktiivsed Bitcoin'i sõlmed. Uus sõlm saab seejärel luua ühendusi nimekirjas olevate sõlmedega, et saada vajalikku teavet oma Esialgse Ploki Allalaadimise (IBD) sooritamiseks ja sünkroniseerimiseks ahelaga, millel on kõige rohkem kogunenud tööd. Alates 2024. aastast on siin nimekiri Bitcoin Core DNS seemnetest ja isikutest, kes vastutavad nende hoolduse eest (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
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

DNS seemned on teine meetod, prioriteedi järjekorras, Bitcoin'i sõlme ühenduste loomiseks. Esimene meetod hõlmab peers.dat faili kasutamist, mille sõlm ise on loonud. See fail on uue sõlme puhul loomulikult tühi, välja arvatud juhul, kui kasutaja on seda käsitsi muutnud.

> ► *Märkus, DNS seemneid ei tohiks segi ajada "seemnesõlmedega", mis on kolmas viis ühenduste loomiseks.*