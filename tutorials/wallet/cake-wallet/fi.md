---
name: Kakku Wallet
description: Ohje Cake Wallet:stä ja hiljaisista maksuista
---

![cover](assets/cover.webp)


Tässä oppaassa tutustutaan [**Cake Wallet**](https://cakewallet.com/): avoimen lähdekoodin, ei-vartiointipainotteinen, yksityisyyteen keskittyvä monivaluuttainen Wallet, joka on saatavilla Androidille, iOS:lle, macOS:lle, Linuxille ja Windowsille. Tutustumme sen Bitcoin-spesifisiin yksityisyysominaisuuksiin, käymme läpi Bitcoin:n lähettämisen/vastaanottamisen **Silent Payments**:n (parannettu On-Chain:n yksityisyysprotokolla) kautta ja tarkastelemme PayJoin v2:n toteutusta asynkronisia tapahtumia varten.


## 🎉 Tärkeimmät ominaisuudet



- [**Silent Payments (BIP-352)**](https://BIPs.dev/352/) parantaa aiempia [BIP 47 maksukoodeja](https://silentpayments.xyz/docs/comparing-proposals/bip47/), joita kutsutaan myös nimellä "PayNyms", uudelleenkäytettävillä salakäyttöisillä osoitteilla. Kun lähettäjä käyttää Hiljaisen maksun Address:ääsi, hänen Wallet:nsä saa eri avaimia käyttäen yksilöllisen kertaluonteisen Address:n, joka yhdistetään yksilölliseksi kertaluonteiseksi Taproot Address:ksi. Blockchain-tietueet osoittavat toisiinsa liittymättömiä tapahtumia, mikä estää saapuvien maksujen yhdistämisen. Hiljaiset maksut tarjoavat monia etuja, kuten seuraavat:
    - Uudelleenkäytettävät osoitteet: generate ei tarvitse luoda uutta Address-osoitetta jokaista tapahtumaa varten, mikä tarjoaa paremman käyttökokemuksen ja lisää yksityisyyttä
    - Kustannusten nousu on nolla: Hiljaiset maksut eivät lisää tapahtumien kokoa tai kustannuksia.
    - Parannettu anonymiteetti: Ulkopuoliset tarkkailijat eivät voi yhdistää tapahtumia Silent Payment Address:ään.
    - Lähettäjän ja vastaanottajan välistä vuorovaikutusta ei tarvita: Transaktiot voidaan tehdä ilman osapuolten välistä viestintää.
    - Yksilölliset osoitteet kutakin maksua varten: Address:n vahingossa tapahtuvan uudelleenkäytön riskin poistaminen.
    - Palvelinta ei tarvita: Hiljaiset maksut voidaan suorittaa ilman omaa palvelinta.
- PayJoin v2** lieventää tapahtumagraafien analysointia yhdistämällä lähettäjien ja vastaanottajien syötteet yhdeksi tapahtumaksi. Kakku Wallet toteuttaa kaksi ratkaisevan tärkeää edistysaskelta:
    - Asynkroniset tapahtumat**: Lähettäjän ja vastaanottajan ei enää tarvitse olla verkossa samanaikaisesti yksityisen tapahtuman suorittamiseksi.
    - Palvelimetön viestintä**: Kummankaan osapuolen ei tarvitse käyttää PayJoin-palvelinta, mikä poistaa merkittävän teknisen esteen.
- Coin Control** mahdollistaa manuaalisen UTXO-valinnan tapahtumien aikana. Näin estetään osoitteiden tahaton yhdistäminen, kun käytetään useita eri alkuperää olevia UTXO:ita.
- TOR**-tuki, jonka avulla käyttäjät voivat reitittää verkkoliikenteensä Tor-verkon kautta
- RBF** (Replace-By.Fee) avulla voit mukauttaa maksua tapahtuman lähettämisen jälkeen.


## 1️⃣ Wallet:n asentaminen


Cake Wallet tarjoaa laajan valikoiman alustatukea. Voit valita Android-, iOS / macOS-, Linux- ja Windows-käyttöjärjestelmien välillä.  Aloita osoitteessa https://docs.cakewallet.com/get-started/ ja valitse käyttöjärjestelmäsi.


![image](assets/en/01.webp)


Asennuksen jälkeen aseta `PIN` (4 tai 6 numeroa). Tämän jälkeen näet:


1. "Luo uusi Wallet" (uusille käyttäjille)

2. `Restore Wallet` (olemassa oleville lompakoille)


![image](assets/en/02.webp)


Seuraavalla näytöllä voit valita laajan valikoiman kryptovaluuttoja. Valitse `Bitcoin` ja napauta `Next` ja anna `Wallet name` Wallet:n tunnistamiseksi. Napauttamalla `Advanced Settings` (Lisäasetukset) saat näkyviin valikoiman `Privacy Stettings` (Tietosuoja-asetukset). Tee nämä muutokset:



- Fiat API:** valitse `Tor Only` (reitittää hintapyynnöt Torin kautta)
- Vaihto:** valitse `Tor Only` (anonymisoi Exchange-liikenteen)


Oletusarvoisesti luodaan BIP-39 seed-tyyppi, ja on mahdollista vaihtaa Electrum seed-tyyppiin. Johdannaispolut ovat seuraavat:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Jos haluat lisätä ylimääräisen Layer:n, voit perustaa passphrase:n.  passphrase:n päätarkoitus on tarjota lisäsuojaa fyysisiä hyökkäyksiä vastaan. Vaikka hyökkääjä löytäisi seed-lauseen, hän ei voi käyttää Wallet:ta ilman oikeaa passphrase:tä. Toisin sanoen seed-lause yksinään edustaa yhtä Wallet:ta, kun taas seed-lause ja passphrase luovat täysin erilaisen Wallet:n, jolla ei ole yhteyttä alkuperäiseen. Tämä ominaisuus mahdollistaa myös passphrase:llä suojatut "salaiset lompakot" ja antaa sinulle uskottavan mahdollisuuden kieltää tekosi. Pakkotilanteessa voit paljastaa seed-lausekkeen ja pitää suuremmat varat turvassa passphrase:llä suojatussa Wallet:ssa.


Jos käytät jo omaa solmua, vaihda `Add New Custom Node` ja anna `Node Address`, jotta voit validoida transaktiot ja lohkot omassa infrastruktuurissasi. Kun olet valmis, napauta `Continue` ja `Next` luodaksesi Wallet:n.


![image](assets/en/03.webp)


Seuraavalla näytöllä näet vastuuvapauslausekkeen:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Jos haluat oppia parhaat käytännöt Mnemonic-lauseen tallentamiseen, tutustu tähän ohjeeseen:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Napauta `Ymmärrän. Näytä minulle seed` ja tallenna nämä sanat turvalliseen paikkaan! Napauta sitten `Varmenna seed` ja vahvistuksen jälkeen `Avaa Wallet`.


## 2️⃣ Asetukset


Ennen kuin sukellamme syvemmälle, katsomme ensin "Aloitusnäyttöä" ja "Asetuksia".


Aloitusnäytössä näkyy eri kohteita:



- hampurilaisvalikko tuo meidät asetuksiin
- Käytettävissä oleva saldo
- Hiljainen maksukortti aloittaa hiljaisen maksun Address:ään lähetettyjen tapahtumien skannauksen
- PayJoin-kortti PayJoin:n käyttöönotto yksityisyyden suojaamiseksi ja maksujen säästämiseksi
- alareunassa ovat pikanäppäimet "Wallet Overview", "Receive", "Swap" Bitcoin:n ja muiden valuuttojen välillä, "Send" ja "Buy"


![image](assets/en/11.webp)


Asetukset-valikko avautuu napauttamalla hampurilaisvalikon kuvaketta. Katsotaanpa vaihtoehtoja.


![image](assets/en/05.webp)


### A - Yhteys ja synkronointi 🔗


Täällä voimme yhdistää Wallet:n uudelleen, hallita solmuja ja muodostaa yhteyden omaan solmuun (suositeltavaa). `Silent Payments Scanning` -vaihtoehdon avulla voimme mukauttaa skannausta määrittämällä joko `Scan from BLOCK height` tai `Scan from date`.


![image](assets/en/06.webp)


Alpha-ominaisuutena on myös mahdollisuus ottaa käyttöön sisäänrakennettu Tor, jolloin liikenne reititetään Tor-verkon kautta.


### B - Hiljaisten maksujen asetukset 🔈


Voimme kytkeä Hiljaiset maksut -kortin päälle aloitusnäytössä tämän ominaisuuden näyttämiseksi. Jos otat käyttöön "Aina skannaus", Wallet voi jatkuvasti tarkkailla Blockchain:tä saapuvien hiljaisten maksujen varalta. Voimme määrittää skannausparametrit, jotta voimme mukauttaa skannausprosessin tarpeisiimme edellä kuvatulla tavalla.


![image](assets/en/07.webp)


### C - Turvallisuus ja varmuuskopiointi 🗝️


Wallet:n suojaamiseksi voimme luoda varmuuskopion noudattamalla sovelluksen sisäisiä ohjeita. Näin varmistamme, että meillä on turvallinen kopio yksityisistä avaimista, jotta voimme palauttaa Wallet:n, jos se katoaa tai varastetaan. Lisäksi voimme tarkastella seed-lauseemme ja yksityisiä avaimiamme, vaihtaa PIN-koodimme, ottaa käyttöön biometrisen todennuksen, allekirjoittaa/varmentaa ja määrittää 2FA:n Layer lisäsuojaa varten.


![image](assets/en/08.webp)


**Huomautus**: Syyskuusta 2025 alkaen sormenjälkibiometrisen todennuksen on Android-laitteissa toimittava vähintään luokan 2 biometrisen toteutuksen avulla, lisätietoja on [täällä](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Tämä vaatimus voi kuitenkin muuttua tulevaisuudessa.


### D - Tietosuoja-asetukset 🔒


Voimme myös parantaa Wallet:n tietoturvaa käyttämällä Tor-verkkoa salataksemme internetyhteytemme ja turvataksemme yksityisyytemme, kun käytämme ulkoisia lähteitä. Lisäksi voimme estää kuvakaappaukset pitämään Wallet:n tiedot luottamuksellisina, ottaa käyttöön automaattisesti luodut osoitteet, jotta voimme luoda uudet osoitteet jokaista transaktiota varten, ja poistaa osto-/myyntitoimet käytöstä luvattomien transaktioiden estämiseksi. Lisäksi voimme `Enable PayJoin`, joka on toinen yksityisyyden suojaa koskeva ominaisuus, jota tarkastelemme myöhemmin.


![image](assets/en/09.webp)


### E - Muut asetukset 🔧


Muiden asetusten avulla voimme hallita maksuprioriteettia ja asettaa oletusmaksutason tapahtumillemme. Näin voimme hallita Hiljaisiin maksuihimme liittyviä tapahtumamaksuja ottaen huomioon verkon nykyisen käytön.


![image](assets/en/10.webp)


## 3️⃣ Vastaanottaminen ₿itcoin käyttäen Silent Maksut


Bitcoin:n vastaanottamiseen on saatavilla useita vaihtoehtoja ja Address-tyyppejä. `SegWit (P2WPKH)` *(alkaen bc1q....)* on oletusvaihtoehto.  Valitaan tässä esimerkissä `Silent Payments`.


Jos haluat vastaanottaa hiljaisen maksun, napauta ensin Kakku Wallet:n `Vastaanota` -kuvaketta. Syötä seuraavaksi summa, jonka odotat saavasi. Voit määrittää Address-tyypin napauttamalla `Vastaanottaa` uudelleen näytön yläosassa ja valitsemalla sitten vaihtoehdoista `Hiljaiset maksut`.


Päänäytöllä näkyy uudelleenkäytettävä Silent Payment QR-koodi ja Address. Kuten odotettua, Address on melko pitkä:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Käytä nyt BIP-352-yhteensopivaa Wallet:tä (kuten Blue Wallet) tämän QR-koodin skannaamiseen ja lähetä maksu. Näet, että Wallet saa hiljaisesta Address:stä ainutlaatuisen määränpään Address:n.


![image](assets/en/13.webp)


## 4️⃣ Lähettäminen ₿itcoin käyttäen Silent Maksut


Koska Blue Wallet voi vain "lähettää" hiljaisia maksuja, käytämme toista BIP 352 -yhteensopivaa Wallet:a vastaanottavana osapuolena. Tämä prosessi on samanlainen kuin tavallisessa Bitcoin-tapahtumassa.



- Napauta aloitusnäytön kohtaa "Lähetä"
- joko liittämällä uudelleenkäytettävän `sp1qq...` Address:n tai skannaamalla QR-koodi suoraan sovelluksessa.
- Valitse, kuinka paljon haluat käyttää käytettävissä olevasta saldostasi
- Vahvista maksutapahtuma napauttamalla näytön alareunassa olevaa `Send`


Kun olemme syöttäneet `sp1qq...` Address:n, Wallet johtaa automaattisesti taustalla vastaavan `bc1p...` Taproot Address:n (P2TR), jota käytetään hiljaiseen maksuun.


Voimme halutessamme kirjoittaa sisäisen huomautuksen jokaisesta tapahtumasta, säätää maksuasetuksia tai valita tietyt UTXO:t tapahtumaa varten Coin Control -ominaisuuden avulla.


![image](assets/en/14.webp)


vahvista tapahtuma pyyhkäisemällä oikealle.


Kun olet lähettänyt tapahtuman, sinulta kysytään, haluatko lisätä kyseisen yhteystiedon Address-kirjaasi.


![image](assets/en/15.webp)


## 6️⃣ PayJoin


Käydään läpi, mistä PayJoin:ssä on kyse (https://docs.cakewallet.com/cryptos/Bitcoin/#PayJoin):


_Payjoin v2 on Bitcoin:n yksityisyyttä suojaava ja maksuja säästävä ominaisuus, jonka avulla tapahtuman lähettäjä ja vastaanottaja voivat yhdessä luoda yhden tapahtuman. Tämä transaktio sisältää syötteet *kummaltakin* lähettäjältä ja vastaanottajalta, mikä murtaa Bitcoin:n yleisimmät valvontatekniikat ja mahdollistaa paremman skaalautumisen ja maksusäästöt joissakin tilanteissa._


Jos haluat oppia lisää PayJoin:stä, voit tutustua myös seuraavaan opetusohjelmaan.


https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

PayJoin:n käyttäminen edellyttää molemmilta osapuolilta PayJoin-yhteensopivaa Wallet:a, ja vastaanottajalla on oltava vähintään yksi Coin tai lähtö Wallet:ssaan. Aloita noudattamalla seuraavia ohjeita:


1. Napauta Hampurilaisvalikko ja napauta sitten Tietosuoja-painiketta

2. Kytke "Käytä PayJoin" -vaihtoehto pois päältä

3.  Napauta aloitusnäytössä kohtaa "Vastaanota", jolloin näyttöön tulee PayJoin QR-koodi ja kopiointipainike (kun valittuna on SegWit)


![image](assets/en/16.webp)


## 7️⃣ Muut ominaisuudet


On olemassa useita muita ominaisuuksia, kuten Multi currency `Swaps`, `Buy and Sell` -vaihtoehdot eri myyjien yhteyksien kanssa ja Cake-kohtaiset ohjelmat, kuten `Cake Pay`, jonka avulla voit ostaa prepaid-kortteja tai lahjakortteja.


![image](assets/en/17.webp)


## 🎯 Päätelmät


Tämä on arvostelumme Cake Wallet:stä, joka tarjoaa käytännöllistä Bitcoin:n yksityisyyttä hiljaisten maksujen (BIP-352) ja PayJoin v2:n kaltaisten ominaisuuksien ansiosta.


Hiljaiset maksut korvaavat kertakäyttöiset osoitteet uudelleenkäytettävillä salaisilla osoitteilla, joilla estetään saapuvien maksutapahtumien yhdistäminen On-Chain:een. Vaikka aiempien versioiden synkronointiongelmat ovat parantuneet huomattavasti, hiljaisten maksujen skannaaminen ja havaitseminen vaatii enemmän laskennallisia vaatimuksia, mikä lisää resursseja ja kaistanleveyttä.


PayJoin v2 häiritsee ketjuanalyysia yhdistämällä lähettäjän ja vastaanottajan syötteet yhdeksi transaktioksi ilman lisämaksuja tai keskitettyä koordinointia. Tämä rikkoo Ownership:n yhteisen syötteen heuristiikan, mikä on merkittävä etu, koska sen ansiosta ei voida olettaa, että kaikki syötteet kuuluvat lähettäjälle.


Käyttäjille, joille on tärkeää taloudellinen anonymiteetti, Cake Wallet on varteenotettava vaihtoehto. Se sisällyttää yksityisyysprotokollat suoraan ydintoimintoihinsa, jolloin ne ovat käytettävissä ilman teknistä monimutkaisuutta. Julkisten lohkoketjujen valvonnan lisääntyessä tämän kaltaiset työkalut auttavat säilyttämään transaktioiden yksityisyyden siellä, missä sillä on eniten merkitystä. Näiden standardien laajempi käyttöönotto Wallet:ssä olisi tervetullutta kehitystä.


## 📚 Resurssit


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://BIPs.dev/352/](https://BIPs.dev/352/)


https://PayJoin.org/