---
term: TIMESTAMP

---
Aikaleimaus on mekanismi, jossa tapahtumaan, dataan tai viestiin liitetään tarkka aikamerkintä. Tietokonejärjestelmien yleisessä yhteydessä aikaleimausta käytetään toimintojen aikajärjestyksen määrittämiseen ja tietojen eheyden todentamiseen ajan kuluessa.

Bitcoinin tapauksessa aikaleimoja käytetään transaktioiden ja lohkojen kronologian määrittämiseen. Lohkoketjun jokainen lohko sisältää aikaleiman, joka osoittaa sen likimääräisen luontihetken. Satoshi Nakamoto puhuu valkoisessa kirjassaan jopa "aikaleimapalvelimesta" kuvaillakseen sitä, mitä nykyään kutsumme "lohkoketjuksi" Aikaleimauksen tehtävänä Bitcoinissa on määrittää transaktioiden aikajärjestys, jotta ilman keskusviranomaisen puuttumista voidaan määrittää, mikä transaktio tehtiin ensin. Tämän mekanismin avulla kukin käyttäjä voi todentaa, ettei transaktiota ole ollut aiemmin, ja näin estää pahantahtoisen käyttäjän tekemän kaksinkertaisen kulutuksen. Satoshi Nakamoto perustelee tätä mekanismia valkoisessa kirjassaan kuuluisalla lauseella: "*Ainut tapa vahvistaa transaktion puuttuminen on olla tietoinen kaikista transaktioista*" Tämä standardi perustuu Unix-aikaan, joka edustaa 1. tammikuuta 1970 lähtien kuluneiden sekuntien kokonaismäärää.

> ► *Bitcoinin lohkojen aikaleimaus on suhteellisen joustava, sillä jotta aikaleima voidaan katsoa kelvolliseksi, sen on yksinkertaisesti oltava suurempi kuin 11 edeltävän lohkon mediaaniaika (MTP) ja pienempi kuin solmujen palauttamien aikojen mediaani (verkostosovitettu aika) lisättynä kahdella tunnilla.*