---
term: DNS SEEDS

---
Esialgsed ühenduspunktid uutele Bitcoini sõlmedele, mis liituvad võrguga. Need seemned, mis on tegelikult konkreetsed DNS-serverid, on oma aadressi püsivalt Bitcoin Core'i koodi sisse põimitud. Kui uus sõlme alustab, võtab ta ühendust nende serveritega, et saada juhuslik nimekiri eeldatavalt aktiivsete Bitcoini sõlmede IP-aadressidest. Seejärel saab uus sõlme luua ühendusi selles nimekirjas olevate sõlmedega, et saada teavet, mis on vajalik tema esialgse plokkide allalaadimise (IBD) teostamiseks ja sünkroniseerimiseks selle ahelaga, millel on kõige rohkem kogunenud tööd. Alates 2024. aastast on siin nimekiri Bitcoin Core DNS-seemnetest ja nende hooldamise eest vastutavatest isikutest (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.bitcoin.wiz.biz: Jason Maurice;
- seed.mainnet.achownodes.xyz: Ava Chow.

DNS-seemned on Bitcoini sõlme jaoks tähtsusjärjestuse poolest teine meetod ühenduste loomiseks. Esimene meetod hõlmab peers.dat faili kasutamist, mille sõlme ise on loonud. See fail on uue sõlme puhul loomulikult tühi, kui kasutaja ei ole seda käsitsi muutnud.

> ► *Märkus, DNS-seemneid ei tohi segi ajada "seemnesõlmedega", mis on kolmas viis ühenduste loomiseks.*