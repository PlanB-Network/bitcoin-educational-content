---
name: Trezor Model One
description: Hardware Wallet Model One -mallin käyttöönotto ja käyttö
---
![cover](assets/cover.webp)



*Kuvan luotto: [Trezor.io](https://trezor.io/)*



Trezor Model One on ensimmäinen koskaan julkaistu Hardware Wallet, jonka SatoshiLabs julkaisi vuonna 2014. Yli kymmenen vuoden olemassaolon jälkeen se on edelleen mielenkiintoinen valinta erityisesti käyttäjille, jotka etsivät teknisesti ja budjetin kannalta helppokäyttöistä Hardware Wallet:tä. Trezorin virallisella verkkosivustolla sen hinta on 49 euroa. Se on yksi ainoista laitteistolompakoista tässä hintaluokassa. Se sijoittuu keskelle noin 20 euron hintaisia lähtötason laitteita, kuten Tapsigner, josta usein puuttuu näyttö, ja noin 80 euron hintaisia keskitason laitteita, kuten Ledger Nano S Plus tai Trezor Safe 3.



Model Onessa on 0,96-tuumainen yksivärinen OLED-näyttö ja kaksi fyysistä painiketta. Se toimii ilman akkua ja käyttää ainoastaan mikro-USB-liitäntää Exchange:n virran ja datan syöttämiseen.



![Image](assets/fr/01.webp)



Model One -mallin suurin haittapuoli on Secure Elementin puuttuminen, mikä tekee siitä alttiin erilaisille fyysisille hyökkäyksille, joista osa on suhteellisen helppo toteuttaa. Näihin hyökkäyksiin voi kuulua apukanavien analysointi laitteen PIN-koodin määrittämiseksi tai edistyneempiä tekniikoita salatun seed:n poimimiseksi, jotta se voidaan murtaa myöhemmin. Huomaa, että nämä hyökkäykset edellyttävät fyysistä pääsyä laitteeseen. Tätä haavoittuvuutta voidaan kuitenkin vähentää huomattavasti käyttämällä vankkaa passphrase BIP39:ää. Jos valitset tämän Hardware Wallet:n, suosittelen vahvasti passphrase:n määrittämistä.



Model One tarjoaa kaksi tärkeää etua:




- Se perustuu täysin avoimen lähdekoodin arkkitehtuuriin. Toisin kuin uudemmissa malleissa, joissa on Secure Element, kaikki Model One -laitteiston ja -ohjelmiston osat ovat tarkastettavissa;
- Se on varustettu näytöllä. Tietääkseni tämä on markkinoiden ainoa Hardware Wallet tässä hintaluokassa, jossa on näyttö. Tämä on erittäin tärkeä ominaisuus, sillä sen avulla voidaan tarkistaa allekirjoitetut tiedot ja vastaanotto-osoitteet, mikä estää monia digitaalisia hyökkäyksiä.



Trezor Model One voi siis olla viisas valinta aloittelijoille ja keskitason käyttäjille, joiden budjetti on rajallinen. On kuitenkin tärkeää olla tietoinen sen rajoituksista fyysisen suojan osalta, koska Secure Element puuttuu. Jos budjettisi on rajallinen, tämä on hyvä vaihtoehto, mutta jos sinulla on varaa valita parempi malli, kuten Trezor Safe 3, jonka hinta on 79 euroa, se on suositeltavampi, koska se sisältää Secure Elementin.



## Trezor Model One -mallin purkaminen



Kun saat Model One -mallisi, varmista, että laatikko ja Seal ovat ehjät, jotta voit varmistaa, että pakettia ei ole avattu. Laitteen aitouden ja eheyden ohjelmistovarmennus suoritetaan myös, kun laite otetaan käyttöön myöhemmin.



Laatikon sisältö sisältää:




- Trezor Model One;
- Kartonkia Mnemonic-lauseen, tarrojen ja ohjeiden kirjaamiseen;
- USB-A-mikro-USB-kaapeli.



![Image](assets/fr/02.webp)



Laitteessa navigointi on hyvin yksinkertaista:




- Vahvista ja siirry seuraaviin vaiheisiin hiiren kakkospainikkeella;
- Käytä vasenta painiketta palataksesi takaisin.



## Edellytykset



Tässä opetusohjelmassa näytän, miten Trezor Model Onea käytetään [Sparrow Wallet -salkunhallintaohjelmiston](https://sparrowwallet.com/download/) kanssa. Jos et ole vielä asentanut tätä ohjelmistoa, tee se nyt. Jos tarvitset apua, meillä on myös yksityiskohtainen ohje Sparrow Wallet -ohjelmiston konfiguroinnista :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Tarvitset myös Trezor Suite -ohjelmiston Model Onen konfigurointiin, sen aitouden tarkistamiseen ja laiteohjelmiston asentamiseen. Käytämme tätä ohjelmistoa vain tähän, ja sen jälkeen sitä tarvitaan vain laiteohjelmistopäivityksiin. Wallet:n päivittäiseen hallintaan käytämme yksinomaan Sparrow Wallet -ohjelmistoa, koska se on optimoitu Bitcoin:lle ja helppokäyttöinen myös aloittelijoille (Sparrow tukee vain Bitcoin:tä, ei altcoineja).



[Lataa Trezor Suite virallisilta sivuilta](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Suosittelen vahvasti, että tarkistat molempien ohjelmien aitouden (GnuPG:llä) ja eheyden (Hash:lla) ennen niiden asentamista koneellesi. Jos et tiedä, miten tämä tehdään, voit seurata tätä toista ohjetta :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Model One -mallin käynnistäminen



Liitä Model One tietokoneeseen, johon Trezor Suite ja Sparrow Wallet on jo asennettu.



![Image](assets/fr/04.webp)



Avaa Trezor Suite ja napsauta sitten "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Valitse "*Bitcoin-only firmware*" ja napsauta sitten "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite asentaa sitten laiteohjelmiston Model One -malliisi. Odota asennuksen aikana.



![Image](assets/fr/07.webp)



Napsauta "*Jatka*".



![Image](assets/fr/08.webp)



## Bitcoin-salkun luominen



Klikkaa Trezor Suiten "*Luo uusi Wallet*" -painiketta.



![Image](assets/fr/09.webp)



Hyväksy Hardware Wallet:n käyttöehdot.



![Image](assets/fr/10.webp)



Klikkaa Trezor Suitessa "*Jatka varmuuskopiointia*".



![Image](assets/fr/11.webp)



Ohjelmisto antaa ohjeet Mnemonic-lauseen hallintaan.



Tämä Mnemonic antaa sinulle täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lause, voi varastaa varojasi, vaikka hänellä ei olisi fyysistä pääsyä Trezor Model One -laitteeseesi.



24 sanan lause palauttaa pääsyn bitcoineihisi, jos Hardware Wallet häviää, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.



Voit kirjoittaa sen laatikossa olevaan pahviin, tai jos haluat lisätä turvallisuutta, suosittelen kaiverrusta ruostumattomasta teräksestä valmistettuun alustaan, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta.



Vahvista ohjeet ja napsauta sitten painiketta "*Luo Wallet varmuuskopio*".



![Image](assets/fr/12.webp)



Model One luo Mnemonic-lauseesi satunnaislukugeneraattorin avulla. Varmista, ettei sinua tarkkailla tämän toiminnon aikana. Kirjoita näytöllä esitetyt sanat haluamallesi fyysiselle välineelle. Turvallisuusstrategiastasi riippuen voit harkita useiden täydellisten fyysisten kopioiden tekemistä lauseesta (mutta ennen kaikkea älä jaa sitä). On tärkeää pitää sanat numeroituina ja juoksevassa järjestyksessä.



***Ei näitä sanoja saa tietenkään koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkiä Wallet käytetään vain Testnet:ssä, ja se poistetaan ohjeen lopussa



Jos haluat lisätietoja oikeasta tavasta tallentaa ja hallita Mnemonic-lauseesi, suosittelen lämpimästi seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Siirry seuraaviin sanoihin napsauttamalla hiiren kakkospainiketta. Kun olet kirjoittanut kaikki sanat, siirry seuraavaan vaiheeseen napsauttamalla uudelleen oikeaa painiketta.



![Image](assets/fr/13.webp)



Hardware Wallet näyttää jälleen kerran kaikki sanasi. Tarkista, että olet kirjoittanut ne kaikki ylös.



![Image](assets/fr/14.webp)



## PIN-koodin asettaminen



Seuraavaksi tulee PIN-koodin vaihe. PIN-koodi avaa Trezorisi lukituksen. Se suojaa siis luvattomalta fyysiseltä käytöltä. PIN-koodi ei osallistu Wallet:n salausavainten johtamiseen. Joten vaikka PIN-koodia ei olisikaan saatavilla, 12-sanaisen Mnemonic-lauseen hallussapidon avulla voit saada bitcoinisi takaisin.



Klikkaa Trezor Suitessa "*Jatka PIN-koodiin*" ja sitten "*Set PIN*" -painiketta.



![Image](assets/fr/15.webp)



Vahvista Model One.



![Image](assets/fr/16.webp)



Suosittelemme valitsemaan mahdollisimman satunnaisen PIN-koodin. Muista tallentaa tämä koodi erilliseen paikkaan siitä, missä Trezor on tallennettu (esim. salasanahallintaohjelmaan). Voit määrittää 8-50-numeroisen PIN-koodin. Suosittelen, että valitset mahdollisimman pitkän PIN-koodin turvallisuuden parantamiseksi.



PIN-koodi on syötettävä tietokoneen Trezor Suite -ohjelmassa napsauttamalla numeroita vastaavia pisteitä Trezor Model One -mallissa näkyvän näppäimistön kokoonpanon mukaisesti.



Tätä erityistä PIN-koodin syöttötapaa tarvitaan aina, kun avaat Trezor Model One -lukituksen joko Trezor Suiten tai Sparrow Wallet:n kautta.



![Image](assets/fr/17.webp)



Kun olet valmis, napsauta "*Enter PIN*" -painiketta.



![Image](assets/fr/18.webp)



Kirjoita PIN-koodi uudelleen vahvistaaksesi.



![Image](assets/fr/19.webp)



Klikkaa Trezor Suiten "*Complete setup*" -painiketta.



![Image](assets/fr/20.webp)



Model One -mallisi konfigurointi on nyt valmis. Voit halutessasi muuttaa Hardware Wallet:n nimeä ja kotisivua.



![Image](assets/fr/21.webp)



Trezor Suite -ohjelmistoa ei enää tarvita, paitsi Hardware Wallet:n säännöllisiä laiteohjelmistopäivityksiä varten tai jos haluat tehdä palautustestin. Käytämme nyt Sparrow'ta salkun hallintaan, sillä tämä ohjelmisto soveltuu erinomaisesti vain Bitcoin:n käyttöön.



## Salkun määrittäminen Sparrow Wallet:ssä



Aloita lataamalla ja asentamalla Sparrow Wallet [virallisilta verkkosivuilta](https://sparrowwallet.com/) tietokoneellesi, jos et ole jo tehnyt sitä.



Kun olet avannut Sparrow Wallet:n, varmista, että ohjelmisto on yhdistetty Bitcoin-solmuun, mikä näkyy Interface:n oikeassa alakulmassa olevasta rastista. Jos sinulla on ongelmia Sparrow'n yhdistämisessä, suosittelen tutustumaan tämän ohjeen alkuun:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Napsauta välilehteä "*File*" ja sitten "*New Wallet*".



![Image](assets/fr/22.webp)



Nimeä salkkusi ja napsauta sitten "*Luo Wallet*".



![Image](assets/fr/23.webp)



Valitse avattavasta "*Script Type*"-valikosta skriptityyppi, jota käytetään bitcoinien suojaamiseen. Suosittelen "*Taproot*", tai jos se ei onnistu, "*Native SegWit*".



![Image](assets/fr/24.webp)



Napsauta "*Connected Hardware Wallet*" -painiketta. Model One -mallisi on tietenkin oltava kytkettynä tietokoneeseen.



![Image](assets/fr/25.webp)



Napsauta "*Scan*"-painiketta. Model One -mallisi pitäisi tulla näkyviin.



Kun yhdistät Model One -mallin tietokoneeseen, jossa Sparrow Wallet on avoinna, sinua pyydetään syöttämään passphrase BIP39 Sparrowiin. Tätä kehittynyttä vaihtoehtoa käsitellään tulevassa opetusohjelmassa. Toistaiseksi voit yksinkertaisesti valita "*Toggle passphrase Off*" (passphrase pois päältä*) estääksesi Trezoria pyytämästä passphrase:n syöttämistä aina käynnistyksen yhteydessä.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Napsauta "*Import Keystore*".



![Image](assets/fr/27.webp)



Näet nyt Wallet:n tiedot, mukaan lukien ensimmäisen tilisi laajennettu julkinen avain. Napsauta "*Apply*"-painiketta viimeistelläksesi Wallet:n luomisen.



![Image](assets/fr/28.webp)



Valitse vahva salasana, jolla varmistat pääsyn Sparrow Wallet:ään. Tämä salasana takaa turvallisen pääsyn Sparrow Wallet -tietoihin ja suojaa julkisia avaimia, osoitteita, tarroja ja tapahtumahistoriaa luvattomalta käytöltä.



Suosittelen, että tallennat tämän salasanan salasanahallintaan, jotta et unohda sitä.



![Image](assets/fr/29.webp)



Ja nyt salkkusi on tuotu Sparrow Wallet:aan!



![Image](assets/fr/30.webp)



Ennen kuin saat ensimmäiset bitcoinit Wallet:ään, **suositan vahvasti, että teet tyhjän palautustestin**. Kirjoita muistiin joitakin viitetietoja, kuten xpub, ja nollaa sitten Trezor Model One, kun Wallet on vielä tyhjä. Yritä sitten palauttaa Wallet Trezorilla paperisten varmuuskopioiden avulla. Tarkista, että palautuksen jälkeen luotu xpub vastaa alun perin kirjoittamaasi xpubia. Jos se täsmää, voit olla varma, että paperiset varmuuskopiot ovat luotettavia.



Jos haluat lisätietoja palautustestin suorittamisesta, suosittelen, että tutustut tähän toiseen opetusohjelmaan:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Miten vastaanottaa bitcoineja Trezor Model One -laitteella?



Napsauta Sparrow'ssa välilehteä "*Vastaanottaa*".



![Image](assets/fr/31.webp)



Ennen kuin käytät Sparrow Wallet:n ehdottamaa Address:tä, tarkista se Trezorin näytöltä. Näin voit varmistaa, että Sparrow'n näyttämä Address ei ole huijaus ja että Hardware Wallet:ssä on todellakin yksityinen avain, jota tarvitaan tällä Address:llä suojattujen bitcoinien käyttämiseen. Tämä auttaa sinua välttämään useita hyökkäystyyppejä.



Voit tehdä tämän tarkistuksen napsauttamalla painiketta "*Display Address*".



![Image](assets/fr/32.webp)



Tarkista, että Trezorissasi näkyvä Address vastaa Sparrow Wallet:ssä olevaa Address:tä. Tämä tarkistus kannattaa tehdä myös juuri ennen Address:n välittämistä lähettäjälle, jotta voit olla varma sen oikeellisuudesta. Voit vahvistaa sen painamalla oikeaa painiketta.



![Image](assets/fr/33.webp)



Voit myös lisätä "*Label*" kuvaamaan tämän Address:n avulla suojattavien bitcoinien lähdettä. Tämä on hyvä käytäntö, jonka avulla voit paremmin hallita UTXO:tasi.



![Image](assets/fr/34.webp)



Voit sitten käyttää tätä Address:ää bitcoinien vastaanottamiseen.



![Image](assets/fr/35.webp)



## Kuinka lähettää bitcoineja Trezor Model One -laitteella?



Nyt kun olet saanut ensimmäiset satssisi Model One -varmistetussa Wallet:ssa, voit myös käyttää ne! Kytke Trezor tietokoneeseen, käynnistä Sparrow Wallet ja siirry sitten "*lähettää*"-välilehdelle luodaksesi uuden tapahtuman.



![Image](assets/fr/36.webp)



Jos haluat *kolikoiden hallintaa*, eli valita tarkkaan, mitä UTXO:ta haluat käyttää transaktiossa, siirry "*UTXO:t*"-välilehdelle. Valitse UTXO:t, jotka haluat käyttää, ja napsauta sitten "*Send Selected*". Sinut ohjataan samalle "*Lähettää*"-välilehdelle, mutta UTXOt on jo valittu tapahtumaa varten.



![Image](assets/fr/37.webp)



Syötä määränpää Address. Voit myös syöttää useita osoitteita napsauttamalla "*+ Lisää*"-painiketta.



![Image](assets/fr/38.webp)



Kirjoita "*Label*", jotta muistat tämän menon tarkoituksen.



![Image](assets/fr/39.webp)



Valitse tälle Address:lle lähetettävä summa.



![Image](assets/fr/40.webp)



Säädä maksutapahtuman maksuprosentti kulloisenkin markkinatilanteen mukaan. Voit esimerkiksi käyttää [Mempool.space](https://Mempool.space/) sopivan maksun valitsemiseen.



Varmista, että kaikki tapahtumaparametrit ovat oikein, ja napsauta sitten "*Luo tapahtuma*".



![Image](assets/fr/41.webp)



Jos olet tyytyväinen kaikkeen, napsauta "*Viimeistele tapahtuma allekirjoittamista varten*".



![Image](assets/fr/42.webp)



Napsauta "*Sign*".



![Image](assets/fr/43.webp)



Napsauta Trezor Model One -mallisi vieressä olevaa "*Sign*"-painiketta.



![Image](assets/fr/44.webp)



Tarkista tapahtuman parametrit Hardware Wallet-näytöltä, mukaan lukien vastaanottajan vastaanottava Address, lähetetty summa ja maksu. Kun maksutapahtuma on tarkistettu Trezorissa, allekirjoita se hiiren kakkospainikkeella.



![Image](assets/fr/45.webp)



Tapahtumasi on nyt allekirjoitettu. Tarkista vielä kerran, että kaikki on kunnossa, ja klikkaa sitten "*Broadcast Transaction*" lähettääksesi sen Bitcoin-verkkoon.



![Image](assets/fr/46.webp)



Löydät sen Sparrow Wallet:n "*Transaktiot*"-välilehdeltä.



![Image](assets/fr/47.webp)



Onneksi olkoon, olet nyt perillä Trezor Model One:n peruskäytöstä Sparrow Wallet:n kanssa! Jos haluat mennä askeleen pidemmälle, suosittelen tätä kattavaa opetusohjelmaa Hardware Wallet Trezorin käytöstä passphrase BIP39:n kanssa turvallisuuden vahvistamiseksi :



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Jos löysit tämän ohjeen hyödylliseksi, olisin kiitollinen, jos jättäisit Green-peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos paljon!