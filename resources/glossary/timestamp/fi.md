---
term: HORODATAGE
---

Aikaleimaus eli "Timestamp" on mekanismi, jolla tapahtumaan, dataan tai viestiin liitetään tarkka aikamerkki. Yleisesti ottaen tietokonejärjestelmissä aikaleimausta käytetään toimintojen aikajärjestyksen määrittämiseen ja tietojen eheyden todentamiseen ajan kuluessa.


Bitcoin:n tapauksessa aikaleimoja käytetään transaktioiden ja lohkojen aikajärjestyksen määrittämiseen. Jokainen lohko Blockchain:ssä sisältää Timestamp:n, joka osoittaa sen likimääräisen luomisen ajankohdan. Satoshi Nakamoto puhuu valkoisessa kirjassaan jopa "Timestamp-palvelimesta" kuvaamaan sitä, mitä kutsuisimme nykyään "Blockchain:ksi". Bitcoin:n aikaleimauksen tehtävänä on määrittää transaktioiden aikajärjestys, jotta ilman keskusviranomaisen puuttumista asiaan voidaan määrittää, mikä transaktio saapui ensin. Tämän mekanismin avulla kukin käyttäjä voi todentaa, ettei transaktiota ole ollut aiemmin, ja estää siten pahantahtoisen käyttäjän tekemän kaksinkertaisia menoja. Satoshi Nakamoto perustelee tätä mekanismia valkoisessa kirjassaan kuuluisalla lauseella: "*Tämä standardi perustuu Unix-aikaan, joka edustaa 1. tammikuuta 1970 lähtien kuluneiden sekuntien kokonaismäärää.


> ► *Lohkojen aikaleimat ovat suhteellisen joustavia Bitcoin:ssa, sillä jotta Timestamp:n katsotaan olevan voimassa, sen on yksinkertaisesti oltava suurempi kuin sitä edeltävien 11 lohkon mediaaniaika (MTP) ja pienempi kuin solmujen palauttamien aikojen mediaani (verkkokorjattu aika) lisättynä kahdella tunnilla.*