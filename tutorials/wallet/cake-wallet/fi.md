---
name: Kakku Wallet
description: Ohje Cake Wallet:stä ja hiljaisista maksuista
---

![cover](assets/cover.webp)


Tässä oppaassa tutustutaan [**Cake Wallet**](https://cakewallet.com/): avoimeen lähdekoodiin perustuvaan, yksityisyyden suojaan keskittyvään, monivaluuttaiseen wallet:een, joka on saatavilla Androidille, iOS:lle, macOS:lle, Linuxille ja Windowsille. Tutustumme sen Bitcoin-kohtaisiin yksityisyysominaisuuksiin, käymme läpi Bitcoin:n lähettämisen/vastaanottamisen **Silent Payments**:n (parannettu on-chain:n yksityisyysprotokolla) kautta ja tarkastelemme PayJoin v2:n toteutusta asynkronisia tapahtumia varten.


## 🎉 Tärkeimmät ominaisuudet



- [**Silent Payments (BIP-352)**](https://bips.dev/352/) parantaa aiempia [BIP 47 maksukoodeja](https://silentpayments.xyz/docs/comparing-proposals/bip47/), joita kutsutaan myös nimellä "PayNyms", uudelleenkäytettävillä salakäyttöisillä osoitteilla. Kun lähettäjä käyttää Silent Payment -osoitettasi, hänen wallet:nsa saa eri avaimia käyttäen yksilöllisen kertakäyttöisen osoitteen, joka yhdistetään yksilölliseksi kertakäyttöiseksi Taproot-osoitteeksi. Lohkoketjun tietueet näyttävät toisiinsa liittymättömät tapahtumat, mikä estää saapuvien maksujen yhdistämisen. Hiljaiset maksut tarjoavat useita etuja, kuten:
    - Uudelleenkäytettävät osoitteet: generate:n ei tarvitse luoda uutta osoitetta jokaista tapahtumaa varten, mikä parantaa käyttäjäkokemusta ja lisää yksityisyyttä
    - Kustannusten nousu on nolla: Hiljaiset maksut eivät lisää tapahtumien kokoa tai kustannuksia.
    - Parannettu anonymiteetti: Ulkopuoliset tarkkailijat eivät voi yhdistää tapahtumia Silent Payment -osoitteeseen.
    - Lähettäjän ja vastaanottajan välistä vuorovaikutusta ei tarvita: Transaktiot voidaan tehdä ilman osapuolten välistä viestintää.
    - Yksilölliset osoitteet kutakin maksua varten: Poistaa osoitteen tahattoman uudelleenkäytön riskin.
    - Palvelinta ei tarvita: Hiljaiset maksut voidaan suorittaa ilman omaa palvelinta.
- PayJoin v2** lieventää tapahtumagraafien analysointia yhdistämällä lähettäjien ja vastaanottajien syötteet yhdeksi tapahtumaksi. Kakku Wallet toteuttaa kaksi kriittistä edistysaskelta:
    - Asynkroniset tapahtumat**: Lähettäjän ja vastaanottajan ei enää tarvitse olla verkossa samanaikaisesti yksityisen tapahtuman suorittamiseksi.
    - Palvelimetön viestintä**: Kummankaan osapuolen ei tarvitse käyttää Payjoin-palvelinta, mikä poistaa merkittävän teknisen esteen.
- Coin Control** mahdollistaa manuaalisen UTXO-valinnan tapahtumien aikana. Näin estetään osoitteiden tahaton yhdistäminen, kun käytetään useita eri alkuperää olevia UTXO:ita.
- TOR**-tuki, jonka avulla käyttäjät voivat reitittää verkkoliikenteensä Tor-verkon kautta
- RBF** (Replace-By.Fee) avulla voit mukauttaa maksua tapahtuman lähettämisen jälkeen.


## 1️⃣ Wallet:n asentaminen


Cake Wallet tarjoaa laajan valikoiman alustatukea. Voit valita Android-, iOS / macOS-, Linux- ja Windows-käyttöjärjestelmien välillä.  Aloita osoitteessa https://docs.cakewallet.com/get-started/ ja valitse käyttöjärjestelmäsi.


![image](assets/en/01.webp)


Asennuksen jälkeen aseta `PIN` (4 tai 6 numeroa). Tämän jälkeen näet:


1. `Luo uusi Wallet` (uusille käyttäjille)

2. `Restore Wallet` (olemassa oleville lompakoille)


![image](assets/en/02.webp)


Seuraavalla näytöllä voit valita laajan valikoiman kryptovaluuttoja. Valitse `Bitcoin` ja napauta `Next` ja anna `Wallet name` wallet:n tunnistamiseksi. Napauttamalla `Advanced Settings` (Lisäasetukset) saat näkyviin valikoiman `Privacy Stettings` (Tietosuoja-asetukset). Tee nämä muutokset:



- Fiat API:** valitse `Tor Only` (reitittää hintapyynnöt Torin kautta)
- Swap:** valitse `Tor Only` (anonymisoi vaihtoliikenteen)


Oletusarvoisesti luodaan BIP-39 seed-tyyppi, jonka voi vaihtaa Electrum seed-tyyppiin. Johdannaispolut ovat seuraavat:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Jos haluat lisätä ylimääräisen turvakerroksen, voit asentaa passphrase:n.  passphrase:n päätarkoitus on tarjota lisäsuojaa fyysisiä hyökkäyksiä vastaan. Vaikka hyökkääjä löytäisi seed-lauseen, hän ei voi käyttää wallet:tä ilman oikeaa passphrase:ää. Toisin sanoen seed-lause yksinään edustaa yhtä wallet:tä, kun taas seed-lause ja passphrase luovat täysin erilaisen wallet:n, jolla ei ole yhteyttä alkuperäiseen. Tämä ominaisuus mahdollistaa myös passphrase:llä suojatut "salaiset lompakot" ja antaa sinulle uskottavan mahdollisuuden kieltää tekosi. Pakkotilanteessa voit paljastaa seed-lausekkeen ja pitää suuremmat varat turvassa passphrase:llä suojatussa wallet:ssä.


Jos käytät jo omaa solmua, vaihda `Add New Custom Node` ja anna `Node Address`, jotta voit validoida transaktiot ja lohkot omassa infrastruktuurissasi. Kun olet valmis, napauta `Continue` ja `Next` luodaksesi wallet:n.


![image](assets/en/03.webp)


Seuraavalla näytöllä näet vastuuvapauslausekkeen:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Jos haluat oppia parhaat käytännöt muistisääntölauseen tallentamiseen, tutustu tähän ohjeeseen:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Napauta `Ymmärrän. Näytä minulle seed` ja tallenna nämä sanat turvalliseen paikkaan! Napauta sitten `Varmenna seed` ja vahvistuksen jälkeen `Avaa Wallet`.


## 2️⃣ Asetukset


Ennen kuin sukellamme syvemmälle, katsomme ensin "Aloitusnäyttöä" ja "Asetuksia".


Aloitusnäytössä näkyy eri kohteita:



- hampurilaisvalikko tuo meidät asetuksiin
- Käytettävissä oleva saldo
- Hiljaiset maksut -kortti aloittaa hiljaisen maksun osoitteeseen lähetettyjen maksutapahtumien skannauksen
- Payjoin-kortti "mahdollistaa" Payjoinin yksityisyyden suojan ja maksujen säästämisen ominaisuutena
- alareunassa ovat pikakuvakkeet "Wallet yleiskatsaus", "vastaanotto", "vaihto" Bitcoin:n ja muiden valuuttojen välillä, "lähetys" ja "osto"


![image](assets/en/11.webp)


Asetukset-valikko avautuu napauttamalla hampurilaisvalikon kuvaketta. Katsotaanpa vaihtoehtoja.


![image](assets/en/05.webp)


### A - Yhteys ja synkronointi 🔗


Täällä voimme yhdistää wallet:n uudelleen, hallita solmuja ja muodostaa yhteyden omaan solmuun (suositeltavaa). `Silent Payments Scanning` antaa meille mahdollisuuden mukauttaa skannausta määrittämällä joko `Scan from block height` tai `Scan from date`.


![image](assets/en/06.webp)


Alpha-ominaisuutena on myös mahdollisuus ottaa käyttöön sisäänrakennettu Tor, jolloin liikenne reititetään Tor-verkon kautta.


### B - Hiljaisten maksujen asetukset 🔈


Voimme kytkeä Hiljaiset maksut -kortin päälle aloitusnäytössä tämän ominaisuuden näyttämiseksi. Jos otat käyttöön "Aina skannaus" -toiminnon, wallet tarkkailee jatkuvasti lohkoketjua saapuvien Hiljaisten maksujen varalta. Voimme määrittää skannausparametreja, jotta voimme mukauttaa skannausprosessin tarpeisiimme edellä kuvatulla tavalla.


![image](assets/en/07.webp)


### C - Turvallisuus ja varmuuskopiointi 🗝️


wallet:n suojaamiseksi voimme luoda varmuuskopion noudattamalla sovelluksen sisäisiä ohjeita. Näin varmistamme, että meillä on turvallinen kopio yksityisistä avaimista, jotta voimme palauttaa wallet:n, jos se katoaa tai varastetaan. Lisäksi voimme tarkastella seed-lauseemme ja yksityisiä avaimiamme, vaihtaa PIN-koodimme, ottaa käyttöön biometrisen todennuksen, allekirjoittaa/varmentaa ja määrittää 2FA:n lisäsuojausta varten.


![image](assets/en/08.webp)


**Huomautus**: Syyskuusta 2025 alkaen sormenjälkibiometrisen todennuksen on Android-laitteissa toimittava vähintään luokan 2 biometrisen toteutuksen avulla, lisätietoja on [täällä](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Tämä vaatimus voi kuitenkin muuttua tulevaisuudessa.


### D - Tietosuoja-asetukset 🔒


Voimme myös parantaa wallet:n tietoturvaa käyttämällä Tor-verkkoa salataksemme internet-yhteytemme ja turvataksemme yksityisyytemme, kun käytämme ulkoisia lähteitä. Lisäksi voimme estää kuvakaappaukset pitämään wallet:n tiedot luottamuksellisina, ottaa käyttöön automaattisesti luodut osoitteet, jotta voimme luoda uudet osoitteet jokaista transaktiota varten, ja poistaa osto-/myyntitoimet käytöstä estääksemme luvattomat transaktiot. Lisäksi voimme "ottaa PayJoin:n käyttöön", joka on toinen yksityisyydensuojaominaisuus, jota tarkastelemme myöhemmin.


![image](assets/en/09.webp)


### E - Muut asetukset 🔧


Muiden asetusten avulla voimme hallita maksuprioriteettia ja asettaa oletusmaksutason tapahtumillemme. Näin voimme hallita Hiljaisiin maksuihimme liittyviä tapahtumamaksuja ottaen huomioon verkon nykyisen käytön.


![image](assets/en/10.webp)


## 3️⃣ Vastaanottaminen ₿itcoin käyttäen Silent Maksut


Bitcoin:n vastaanottamiseen on käytettävissä useita vaihtoehtoja ja osoitetyyppejä. `Segwit (P2WPKH)` *(alkaen bc1q....)* on oletusvaihtoehto.  Valitaan tässä esimerkissä `Silent Payments`.


Jos haluat vastaanottaa hiljaisen maksun, napauta ensin Kakku Wallet:n `Vastaanota`-kuvaketta. Syötä seuraavaksi summa, jonka odotat saavasi. Voit määrittää osoitetyypin napauttamalla `Vastaanottaa` uudelleen näytön yläreunassa ja valitsemalla sitten vaihtoehdoista `Hiljaiset maksut`.


Päänäytöllä näkyy uudelleenkäytettävä Silent Payment QR-koodisi ja osoitteesi. Osoite on odotetusti melko pitkä:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Skannaa nyt tämä QR-koodi BIP-352-yhteensopivalla wallet:lla (kuten Blue Wallet) ja lähetä maksu. Näet, että wallet johtaa yksilöllisen kohdeosoitteen hiljaisesta osoitteestasi.


![image](assets/en/13.webp)


## 4️⃣ Lähettäminen ₿itcoin käyttäen Silent Maksut


Koska Blue Wallet voi vain "lähettää" hiljaisia maksuja, käytämme toista BIP 352 yhteensopivaa wallet:ta vastaanottavana osapuolena. Prosessi on samanlainen kuin tavallisessa Bitcoin-tapahtumassa.



- Napauta aloitusnäytön kohtaa "Lähetä"
- joko liittämällä uudelleenkäytettävän `sp1qq...`-osoitteemme tai skannaamalla QR-koodi suoraan sovelluksessa.
- Valitse, kuinka paljon haluat käyttää käytettävissä olevasta saldostasi
- Vahvista maksutapahtuma napauttamalla näytön alareunassa olevaa `Send`


Kun olemme syöttäneet `sp1qq...-osoitteen, wallet johtaa automaattisesti taustalla vastaavan `bc1p...-osoitteen Taproot:lle (P2TR), jota käytetään hiljaiseen maksuun.


Voimme halutessamme kirjoittaa sisäisen huomautuksen jokaisesta tapahtumasta, säätää maksuasetuksia tai valita tietyt UTXO:t tapahtumaa varten Coin Control -ominaisuuden avulla.


![image](assets/en/14.webp)


vahvista tapahtuma pyyhkäisemällä oikealle.


Kun olet lähettänyt maksutapahtuman, sinulta kysytään, haluatko lisätä kyseisen henkilön osoitekirjaasi.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Käydään läpi, mistä PayJoin:ssä on kyse (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 on Bitcoin:n yksityisyyttä suojaava ja maksuja säästävä ominaisuus, jonka avulla tapahtuman lähettäjä ja vastaanottaja voivat yhdessä luoda yhden tapahtuman. Tämä transaktio sisältää syötteet *kummaltakin* lähettäjältä ja vastaanottajalta, mikä murtaa Bitcoin:n yleisimmät valvontatekniikat ja mahdollistaa paremman skaalautumisen ja maksusäästöt joissakin tilanteissa._


Jos haluat oppia lisää PayJoin:stä, voit tutustua myös seuraavaan opetusohjelmaan.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

PayJoin:n käyttäminen edellyttää molemmilta osapuolilta PayJoin-yhteensopivaa wallet:a, ja vastaanottajalla on oltava wallet:ssaan vähintään yksi kolikko tai lähtö. Seuraa seuraavia ohjeita:


1. Napauta Hampurilaisvalikko ja napauta sitten Tietosuoja-painiketta

2. Vaihda "Käytä Payjoin-vaihtoehtoa"

3.  Napauta aloitusnäytössä `Vastaanottaa`, jolloin näyttöön tulee PayJoin QR-koodi ja kopiointipainike (kun valittu Segwit)


![image](assets/en/16.webp)


## 6️⃣ Muut ominaisuudet


On olemassa useita muita ominaisuuksia, kuten Multi currency `Swaps`, `Buy and Sell` -vaihtoehdot eri myyjien yhteyksien kanssa ja Cake-kohtaiset ohjelmat, kuten `Cake Pay`, jonka avulla voit ostaa prepaid-kortteja tai lahjakortteja.


![image](assets/en/17.webp)


## 🎯 Päätelmät


Tämä on arvostelumme Cake Wallet:sta, joka tarjoaa käytännön Bitcoin-suojaa hiljaisten maksujen (BIP-352) ja Payjoin v2:n kaltaisten ominaisuuksien ansiosta.


Hiljaiset maksut korvaavat kertakäyttöiset osoitteet uudelleenkäytettävillä salaisilla osoitteilla, joilla estetään saapuvien maksutapahtumien on-chain-linkitys. Vaikka aiempien versioiden synkronointiongelmat ovat parantuneet huomattavasti, hiljaisten maksujen skannaaminen ja havaitseminen vaatii enemmän laskentatehoa, mikä vaatii enemmän resursseja ja kaistanleveyttä.


Payjoin v2 häiritsee ketjuanalyysia yhdistämällä lähettäjän ja vastaanottajan syötteet yhdeksi transaktioksi ilman lisämaksuja tai keskitettyä koordinointia. Tämä rikkoo yleisen panosten omistusoikeusheuristiikan, mikä on merkittävä etu, koska sen ansiosta ei voida olettaa, että kaikki panokset kuuluvat lähettäjälle.


Käyttäjille, joille taloudellinen anonymiteetti on tärkeintä, Cake Wallet on varteenotettava vaihtoehto. Se sisällyttää yksityisyysprotokollat suoraan ydintoimintoihinsa, jolloin ne ovat käytettävissä ilman teknistä monimutkaisuutta. Julkisten lohkoketjujen valvonnan lisääntyessä tämän kaltaiset työkalut auttavat säilyttämään transaktioiden yksityisyyden siellä, missä sillä on eniten merkitystä. Näiden standardien laajempi käyttöönotto wallet:ssä olisi tervetullutta kehitystä.


## 📚 Resurssit


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/