---
termi: TIMESTAMP
---

Aikaleimaus, tai "timestamp" englanniksi, on mekanismi, joka sisältää tarkan aikamerkinnän liittämisen tapahtumaan, dataan tai viestiin. Yleisessä tietokonejärjestelmien kontekstissa aikaleimausta käytetään toimintojen kronologisen järjestyksen määrittämiseen ja datan eheyden varmistamiseen ajan myötä.

Bitcoinin tapauksessa aikaleimoja käytetään transaktioiden ja lohkojen kronologian vahvistamiseen. Jokainen lohkoketjun lohko sisältää aikaleiman, joka osoittaa sen luomisen likimääräisen hetken. Satoshi Nakamoto puhuu jopa "aikaleimapalvelimesta" White Paperissaan, kuvaillakseen sitä, mitä me tänään kutsuisimme "lohkoketjuksi". Aikaleimauksen rooli Bitcoinissa on määrittää transaktioiden kronologia, jotta voidaan määrittää ilman keskusviranomaisen puuttumista, mikä transaktio tapahtui ensin. Tämä mekanismi mahdollistaa jokaisen käyttäjän varmistaa, ettei tiettyä transaktiota ole tapahtunut menneisyydessä, ja näin ollen estää pahantahtoisen käyttäjän tekemästä kaksinkertaista kulutusta. Satoshi Nakamoto perustelee tätä mekanismia White Paperissaan kuuluisalla lauseella: "*Ainoa tapa vahvistaa transaktion puuttuminen on olla tietoinen kaikista transaktioista.*" Tämä standardi perustuu Unix-aikaan, joka edustaa sekuntien kokonaismäärää alkaen tammikuun 1. päivästä 1970.

> ► *Bitcoinin lohkojen aikaleimaus on suhteellisen joustavaa, sillä aikaleiman katsotaan olevan kelvollinen, jos se on suurempi kuin 11 edeltävän lohkon mediaaniaika (MTP) ja pienempi kuin solmujen palauttamien aikojen mediaani (verkon säätämä aika) plus 2 tuntia.*