---
name: Trezor Shamir Backup
description: Yhden ja useamman osakkeen Mnemonic-lauseet Trezorissa
---
![cover](assets/cover.webp)



*Kuvan luotto: [Trezor.io](https://trezor.io/)*



## Trezorin uudet varmuuskopiointivaihtoehdot



Vuodesta 2023 lähtien Trezor on tarjonnut uutta varmuuskopiointimuotoa nimeltä ***Single-share Backup***, joka korvaa vähitellen useimmissa salkuissa käytetyn klassisen BIP39-pohjaisen lähestymistavan. Toisin kuin perinteiset 12- tai 24-sanaiset Mnemonic-lauseet, tämä uusi muoto perustuu yhteen 20-sanalauseeseen, joka on johdettu SatoshiLabsin kehittämästä standardista: **SLIP39**. Tavoitteena on parantaa varmuuskopioinnin kestävyyttä ja luettavuutta ja mahdollistaa samalla sujuva siirtyminen hajautettuun varmuuskopiointimalliin.



Tätä hajautettua mallia kutsutaan ***Multi-share Backup***. Se perustuu samaan periaatteeseen, mutta sen sijaan, että se tuottaisi yhden Mnemonic-lauseen, se jaetaan useisiin pätkiin, joita kutsutaan ***osakkeiksi***, joista kukin on oma Mnemonic-lauseensa. Jotta salkku voidaan palauttaa, tietty määrä näitä *osuuksia* (määritelty *kynnysarvolla*) on yhdistettävä uudelleen. Esimerkiksi 3/5-järjestelmässä 3 *osaa* viidestä palauttaa salkun. Huomaa, että Trezorin hajautettu varmuuskopiointijärjestelmä eroaa Multisig-lompakoista. Bitcoinien käyttämiseen tarvitaan vain Hardware Wallet Trezor. Tarvitaan vain yksi allekirjoitus. Jakelu koskee vain Mnemonic-lauseen eli varmuuskopion tasoa.



![Image](assets/fr/01.webp)



Tämä järjestelmä ratkaisee Mnemonic-lauseen yhden vikapisteen ongelman ilman Multisig- tai passphrase-rajatarkastusaseman39 hallintaan liittyviä haittoja. Palauttamisprosessi ei enää perustu yhteen tietoon vaan useisiin tietoihin, ja lisäetuna on myös häviön sietokyky kynnysarvon ansiosta.



Käyttäjät, jotka ovat luoneet salkun *Single-share Backup*:lla, voivat milloin tahansa vaihtaa *Multi-share Backup*:iin ilman, että heidän tarvitsee siirtää salkkuaan. Vastaanotto-osoitteet ja tilit pysyvät identtisinä. *Multi-share*-järjestelmä vaikuttaa vain varmuuskopiointiin, kun taas muu salkku pysyy ennallaan.



Multi-share Backup* on käytettävissä Trezor Model T:ssä, Safe 3:ssa ja Safe 5:ssä. Trezor Model One ei tue tätä ominaisuutta.



**Tärkeä huomautus:** Trezorin *Multi-share*-järjestelmä on kryptografisesti turvallinen, koska se käyttää *Shamirin salaisen jakamisen* järjestelmää jakeluun. Emme suosittele soveltamaan vastaavaa järjestelmää manuaalisesti jakamalla klassisen Mnemonic-lauseen itse. Se on huono käytäntö, joka lisää merkittävästi bitcoinien varastamisen ja menettämisen riskiä, joten älä tee sitä. Klassinen Mnemonic-lause tallennetaan kokonaisuudessaan.



## Shamirin salainen jakaminen SLIP39:ssä



Trezorin *Multi-share*-varmuuskopioinnin taustalla oleva kryptografinen mekanismi on *Shamir's Secret Sharing Scheme* (SSSS). Sen periaate on seuraava: salainen tieto (tässä tapauksessa salkun seed) muunnetaan matemaattiseksi polynomiksi. Tämän jälkeen lasketaan useita tämän polynomin pisteitä, joista jokaisesta tulee osake. Alkuperäinen salainen tieto rekonstruoidaan polynomi-interpoloinnin avulla keräämällä vähimmäismäärä pisteitä (kynnysarvo).



Mitään salaista tietoa ei voida päätellä kynnysarvon alittavasta osuuksien määrästä, mikä takaa täydellisen teoreettisen salaisen tiedon turvallisuuden. Toisin sanoen edes hyökkääjä, jolla on rajaton laskentateho, ei voi arvata seed:tä, jos kynnysarvoa ei saavuteta.



SLIP39 käyttää tätä järjestelmää seed-salkun jakamiseen. Kukin osake on 20 sanan lause, joka on muodostettu 1024 sanan luettelosta (joka eroaa BIP39:n luettelosta).



## Multi-share-varmuuskopioinnin määrittäminen Trezorissa



Kun luot salkkuasi Trezorissa, sinulla on kolme eri vaihtoehtoa:




- Käytä klassista BIP39 Mnemonic-lauseen 12 tai 24 sanaa;
- Käytä yhden jakajan Mnemonic-lauseen (SLIP39);
- Konfiguroi useita Mnemonic-lauseita Multi-share (SLIP39) -tilassa.



Jos valitset yhden osakkeen SLIP39 Mnemonic -lauseen, voit myöhemmin päivittää sen usean osakkeen lauseeksi ilman, että sinun tarvitsee nollata salkkuasi. Toisaalta, jos aloitat klassisella BIP39-salkulla (12- tai 24-sanaisella lauseella), et voi muuntaa sitä suoraan Multi-share-salkuksi. Sinun on luotava uusi Multi-share-salkku tyhjästä ja siirrettävä varoja vanhasta salkusta uuteen salkkuun yhdellä tai useammalla Bitcoin-tapahtumalla. Tämä on monimutkaisempi ja kalliimpi toimenpide. Jos haluat tehdä tämän siirtymisen, suosittelen, että ostat uuden Hardware Wallet Trezorin, jotta vältät seed:n syöttämisen salkkuohjelmistoon.



Tässä oppaassa tarkastelemme ensin, miten moniosakkeita perustetaan salkkua luotaessa, ja seuraavassa osassa katsotaan, miten yhden osakkeen salkku muunnetaan moniosakkeeksi olemassa olevassa salkussa.



Jos tarvitset apua laitteesi alkuasennuksessa, meillä on myös yksityiskohtainen ohje jokaiselle Trezor-mallille:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Uudesta salkusta



Olet nyt saanut valmiiksi Trezorin alkukonfiguroinnin ja olet valmis luomaan portfolion. Klikkaa Trezor Suitessa "*Luo uusi Wallet*" -painiketta.



![Image](assets/fr/02.webp)



Valitse vaihtoehto "*Multi-share Backup*" ja napsauta sitten "*Create Wallet*".



![Image](assets/fr/03.webp)



Hyväksy Trezorin käyttöehdot ja vahvista salkun luominen.



![Image](assets/fr/04.webp)



Klikkaa Trezor Suitessa "*Jatka varmuuskopiointia*".



![Image](assets/fr/05.webp)



Lue ohjeet huolellisesti, vahvista ne ja napsauta sitten "*Luo Wallet varmuuskopio*".



![Image](assets/fr/06.webp)



Jos haluat lisätietoja oikeasta tavasta tallentaa ja hallita Mnemonic-lauseita, suosittelen lämpimästi seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Valitse Trezorissa niiden osakkeiden kokonaismäärä, jotka haluat määrittää. Yleisimmät määritykset ovat 2-de-3 ja 3-de-5. Tässä esimerkissä luon 2-de-3-kokoonpanon, joten valitsen 3 osaketta. Kukin osake edustaa 20 sanan Mnemonic-lausetta.



**Safe 5 -käyttäjille**, vaikka näytöllä lukee "*Tap jatka*", sinun on itse asiassa pyyhkäistävä ylöspäin vahvistaaksesi



![Image](assets/fr/07.webp)



Vahvista sitten kynnysarvo eli osakkeiden määrä, joka tarvitaan Wallet:n ja sen sisältämien bitcoinien takaisin saamiseksi.



![Image](assets/fr/08.webp)



Trezor luo eri osakkeet (Mnemonic-lauseet) satunnaislukugeneraattorinsa avulla. Varmista, ettei sinua tarkkailla tämän toiminnon aikana. Kirjoita näytöllä annetut sanat haluamallesi fyysiselle välineelle. On tärkeää, että sanat ovat numeroituja ja juoksevassa järjestyksessä.



Suosittelen, että merkitset jokaisen osakkeen muistiin erilliselle tietovälineelle ja hallitset niiden säilytystä huolellisesti, jotta vältät useiden osakkeiden pääsyn samaan paikkaan. Esimerkiksi omani kaltaisessa 2:sta 3:een -kokoonpanossa yksi vaihtoehto olisi säilyttää yksi osuus kotonani, toinen luotettavalla ystävällä ja viimeinen pankin kassakaapissa. Säilytyspaikkojen valinta riippuu henkilökohtaisesta turvallisuusstrategiastasi.



Näytön yläreunassa näkyy, mitä jakoa parhaillaan katselet.



näitä sanoja ei tietenkään saa koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkiä Wallet käytetään vain Testnet:ssa ja se poistetaan opetusohjelman lopussa.



![Image](assets/fr/09.webp)



Voit siirtyä seuraaviin sanoihin napsauttamalla näytön alareunaa. Voit siirtyä taaksepäin liu'uttamalla alaspäin. Kun olet kirjoittanut kaikki sanat ylös, pidä sormi näytöllä siirtyäksesi seuraavaan osakkeeseen ja toista toiminto.



![Image](assets/fr/10.webp)



Jokaisen jaetun äänitteen lopussa sinua pyydetään valitsemaan Mnemonic-lauseen sanat, jotta voit varmistaa, että olet kirjoittanut ne oikein.



![Image](assets/fr/11.webp)



Ja se siitä, olet onnistuneesti varmuuskopioinut salkkusi käyttämällä Multi-share-vaihtoehtoa. Voit nyt jatkaa lopuilla määritysohjeilla.



### Olemassa olevan yhden osakkeen salkun osalta



Jos sinulla on jo Trezor Wallet, jossa on yhden osakkeen varmuuskopio (SLIP39 Mnemonic-lause, ei klassinen BIP39-lause), ja haluat parantaa Wallet-varmuuskopiosi saatavuutta ja turvallisuutta, voit perustaa monen osakkeen järjestelmän ilman, että sinun tarvitsee siirtää bitcoinejasi.



Voit tehdä tämän yhdistämällä ja avaamalla Hardware Wallet:n lukituksen. Siirry Trezor Suitessa kohtaan Asetukset.



![Image](assets/fr/12.webp)



Siirry "*Laite*"-välilehdelle.



![Image](assets/fr/13.webp)



Napsauta sitten "*Luo Multi-share Backup*".



![Image](assets/fr/14.webp)



Lue ohjeet ja napsauta sitten "*Luo Multi-share Backup*".



![Image](assets/fr/15.webp)



Tämän jälkeen sinun on syötettävä nykyinen Mnemonic-lauseesi (single-share) Trezorin näytölle. Valitse sanojen määrä (oletusarvo on 20).



![Image](assets/fr/16.webp)



Kirjoita sitten Trezorin näytön näppäimistöllä jokainen sana nykyisestä Mnemonic-lauseestasi.



![Image](assets/fr/17.webp)



Tämän jälkeen voit valita Multi-share-varmuuskopion kokoonpanon edellisessä osassa annettujen ohjeiden mukaisesti.



![Image](assets/fr/18.webp)



Kun olet luonut Multi-share-varmuuskopion, sinun on päätettävä, mitä tehdä alkuperäiselle Single-share Mnemonic -lauseelle. Koska Bitcoin-salkku pysyy samana, tämä yksittäinen lause mahdollistaa aina pääsyn siihen. Tämä riippuu tietoturvastrategiastasi, mutta yleisesti ottaen on suositeltavaa tuhota tämä lauseke, jotta tämä yksittäinen vikapiste poistuu, mikä on juuri Multi-share-varmuuskopioinnin tavoite. Jos päätät tuhota sen, varmista, että teet sen turvallisesti, sillä **se antaa edelleen pääsyn bitcoineihisi**.



Onneksi olkoon, olet nyt perillä Trezor-laitteiston lompakoiden Single-share- ja Multi-share-varmuuskopioiden käytöstä. Jos haluat viedä Wallet:n tietoturvan askeleen pidemmälle, tutustu tähän BIP39-salasanoja käsittelevään oppaaseen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Jos löysit tämän ohjeen hyödylliseksi, olisin kiitollinen, jos jättäisit Green peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos paljon!



## Lisäresurssit





- [SLIP-0039: Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup on Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).