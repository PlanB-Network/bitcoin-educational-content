---
name: Bull Bitcoin Wallet
description: Selvitä, miten Wallet Bull Bitcoin:tä käytetään
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Tämä BTC Sessionsin opetusvideo opastaa sinut Bull Bitcoin Wallet:n käyttöönottoon ja käyttöön!!*


Tässä oppaassa käydään läpi Bull Bitcoin Wallet:n asennus, konfigurointi ja käyttö. Opit lähettämään ja vastaanottamaan varoja Bitcoin On-Chain-, Liquid- ja Lightning-verkoissa sekä siirtämään Bitcoin:ta niiden välillä. wallet:n laajat ominaisuudet tekevät siitä tehokkaan, kaiken kattavan työkalun Bitcoin:n hallintaan. Aloitetaan.


## Johdanto


Bull Bitcoin Wallet, jonka on kehittänyt [Bull Bitcoin](https://www.bullbitcoin.com/), on **itseohjautuva** Bitcoin wallet, mikä tarkoittaa, että sinulla on täysi määräysvalta yksityisiin avaimiisi ja siten varoihisi ilman riippuvuutta kolmannesta osapuolesta. Avoimen lähdekoodin ja Cypherpunk-filosofiaan perustuvassa Wallet:ssä yhdistyvät yksinkertaisuus, luottamuksellisuus ja kehittyneet ominaisuudet, kuten verkkojen väliset swapit ja PayJoin-tuki. Sen avulla voit hallita bitcoinejasi kolmessa verkossa: **Bitcoin onchain**, **Liquid** ja **Lightning**, joista jokainen on räätälöity erityisiin käyttötarkoituksiin. [BullBitcoin GitHubissa](https://github.com/orgs/SatoshiPortal/projects/49) voit tutustua ajankohtaisiin aiheisiin ja tuleviin kehityskohteisiin. Koska hanke on 100-prosenttisesti avointa lähdekoodia ja "rakennettu julkisesti", voit myös lähettää ehdotuksia ja havaitsemiasi virheitä. Vaikka jotkut lompakot tukevat nykyään useita verkkoja, Bull Bitcoin Wallet erottuu muista integroimalla yksityisyysominaisuudet syvällisesti kaikkiin verkkoihin, mikä tekee siitä tehokkaan työkalun Bitcoin:n hallintaan kaikissa tärkeimmissä verkoissa


## 1️⃣ Edellytykset


Ennen kuin aloitat **Bull Bitcoin Wallet**:n käytön, varmista, että sinulla on seuraavat osat:



- Yhteensopiva älypuhelin**: **iOS** (iPhone tai iPad) tai **Android** -laite
- Internet-yhteys
- Turvallinen varmuuskopiointiväline**: Kirjoita **palautuslauseke** (12 sanaa) paperille tai metallille ja säilytä se turvallisessa paikassa.
- Perustiedot**: Bitcoin:n käsitteiden (osoitteet, transaktiot, maksut) vähimmäistuntemus on hyödyllistä, vaikka tämä opetusohjelma selittääkin jokaisen vaiheen aloittelijoille.


## 2️⃣ Asennus


Voit asentaa sovelluksen kautta:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(iOS-laitteille)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (Android-laitteille)


Android-käyttäjillä on myös vaihtoehtoisia vaihtoehtoja:



- Lataa APK suoraan [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) -sivulta tai
- Asenna Nostr-yhteensopivan [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap) kautta


Kun olet asentanut sovelluksen, seuraa tervetuliaisnäyttöä ja määritä tilisi.


## 3️⃣ Alustava konfigurointi


Kun avaat sen, sinulle näytetään seuraavat vaihtoehdot:



- `Luo uusi Wallet`
- `Recover Wallet` ja
- `Lisäasetukset`


Aloitetaan napauttamalla `Lisäasetukset`.


Täällä voimme määrittää lisäasetukset ennen wallet:n luomista tai palauttamista:


1. Ota käyttöön `Tor proxy` reitittääksesi liikenteen Tor-verkon kautta.

1. [Orbot-sovellus](https://orbot.app/en/) on asennettava ja sen on oltava käynnissä, ennen kuin se otetaan käyttöön

2. Tor Proxy koskee vain Bitcoin:ta (ei Liquid:ta), ja se voi johtaa hitaampaan yhteyteen.

2. Aseta `Custom Electrum Server`, tai

3. Säädä `Recover Bull` -asetuksia. Lisätietoja [Recover Bull](https://recoverbull.com/) -asetuksista on myöhemmin.


Kun olet tehnyt kaikki valinnaiset säädöt, napauta `Done`. Jos haluat käyttää olemassa olevaa Wallet:tä uudelleen, napsauta `Recover Wallet` ja täytä 12 sanaa palautuslausetta.


Muussa tapauksessa napsauta `Create a New Wallet`.


![image](assets/en/01.webp)


## 4️⃣ Aloitusnäyttö


Ennen kuin sukellamme syvemmälle, katsomme aloitusnäyttöä, jotta voimme orientoitua:



- "transaktioiden yleiskatsaus" ja "asetusvalikko" sijaitsevat yläreunassa.
- Käytettävissä oleva saldo -kohdassa on yksityisyysvaihtoehto, joka voidaan kytkeä päälle tai pois päältä.
- Pääset "Bitcoin Bull Exchange" -palveluun "Osta, myy tai maksa" (tämä riippuu lainkäyttöalueesta ja saattaa vaatia KYC-tunnistusta).
- varojen siirto lompakoiden välillä
- `Turvallinen Bitcoin` vastaa Onchain Bitcoin Wallet
- "Pikamaksut" Lightning- / Liquid Network:n kautta *(Huomautus: Bull Bitcoin Wallet mahdollistaa maksujen suorittamisen ja vastaanottamisen Lightningin kautta.) Lightningin kautta vastaanotetut varat tallennetaan [*Liquid-verkkoon](https://liquid.net/) (Wallet-pikamaksuihin) [*Boltz-vaihdon](https://boltz.exchange/) kautta tapahtuvan automaattisen vaihdon ansiosta. Näin voit olla vuorovaikutuksessa Lightningin kanssa ilman likviditeettikanavien hallintaa ja pysyä samalla omahallinnossa.) *)
- varojen lähettäminen ja vastaanottaminen


![image](assets/en/02.webp)


Tehdään ensin joitakin tärkeitä asetuksia ja aloitetaan varmuuskopioinnista.


## 5️⃣ Varmuuskopiointi


Aloita varmuuskopiointi napauttamalla sovelluksen oikeassa yläkulmassa olevaa hammasratas-kuvaketta (⚙) ja valitsemalla "Wallet Backup". Näyttöön tulee kaksi tapaa wallet:n suojaamiseen: `Salattu holvi` ja `Fyysinen varmuuskopiointi`. Tutustutaan kumpaankin.


![image](assets/en/03.webp)


### Fyysinen varmuuskopiointi


Napauta `Fyysinen varmuuskopiointi`, niin näet luettelon 12 sanasta, jotka edustavat palautus- tai seed-lauseesi. Ota huomioon seuraavat:



- Kirjoita "toipumislauseesi" ylös äärimmäisen huolellisesti. Kirjoita se paperille tai metallille ja säilytä sitä turvallisessa paikassa (tallelokerossa, offline-paikassa). Tämä lauseke on ainoa keinosi päästä käsiksi bitcoineihisi, jos laitteesi katoaa tai sovellus poistetaan.
- On myös tärkeää huomata, että kuka tahansa, jolla on tämä lause, voi varastaa kaikki bitcoinisi. Älä koskaan säilytä niitä digitaalisesti:
- Ei kuvakaappausta
- Ei pilvi-, sähköposti- tai viestinnän varmuuskopioita
- Ei kopiointia/liittämistä (riski tallentaa leikepöydälle)


![image](assets/en/25.webp)


Seuraavassa ruudussa sinun on laitettava sana oikeaan järjestykseen varmistaaksesi, että seed-lause on oikein. Saat vahvistuksen, kun testi on valmis ja se on onnistunut.


! **Tämä kohta on kriittinen**. Lisätietoja :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Salattu holvi


On myös mahdollista tehdä salattu, anonyymi varmuuskopio pilvipalveluun. Mutta emmekö maininneet viimeisessä kappaleessa, että pilvivarmistukset ovat riskialttiita ja niitä tulisi välttää? Bull Bitcoin-tiimi on kuitenkin kehittänyt nokkelan tavan tehdä prosessista turvallinen. Näin se toimii:


`Recoverbull` on varmuuskopiointiprotokolla, joka yksinkertaistaa Bitcoin wallet:n suojaamista jakamalla varmuuskopioinnin kahteen osaan. Ensin wallet:n varmuuskopiotiedosto salataan laitteessa vahvan salausavaimen avulla. Voit tallentaa tämän salatun tiedoston minne haluat, kuten Google Driveen tai laitteeseesi. Toiseksi Recoverbull Key Server tallentaa tiedoston avaamiseen tarvittavan salausavaimen. Palauttaaksesi wallet:n tarvitset sekä salatun varmuuskopiotiedoston että avaimen, johon pääset käsiksi PIN-koodin tai salasanan avulla. Tämä rakenne varmistaa, että pelkkä pilvivarmistuskopiosi on käyttökelvoton ja että pelkkä avainpalvelin on käyttökelvoton ilman tiettyä varmuuskopiotiedostoa. Näin varasi pysyvät turvassa, vaikka toinen osa vaarantuisi.


Ajattele sitä kuin tallelokeroa. Salattu varmuuskopiotiedosto on *laatikko*, jota voit säilyttää missä tahansa (kuten Google Drivessa). Recovery PIN-koodisi on *avain*, jonka Recoverbull Key Server tallentaa erikseen. Varkaan olisi saatava sekä tietty laatikko että tietty avain avatakseen sen. Tämä rakenne varmistaa, että vaikka joku saisi varmuuskopiotiedostosi, se on hyödytön ilman palvelimen avainta, ja palvelimen avain on hyödytön ilman ainutlaatuista varmuuskopiotiedostoasi.


Lisätietoja `Recoverbull` wallet -varmistusprotokollasta [täällä](https://recoverbull.com/).


Vahvista oletuspalvelimen käyttö napauttamalla `Salattu holvi` ja sitten `Jatka`. Yhteys ohjataan `Tor`-verkon kautta yksityisyyden ja anonymiteetin varmistamiseksi.


**PIN-koodien ymmärtäminen**



- `App Unlock PIN`**:** Valinnainen PIN-koodi, joka on asetettu kohdassa `Settings > Security PIN` (Asetukset > Suojaus PIN) sovelluksen lukitsemiseksi puhelimessa.
- `Recovery PIN`**:** Pakollinen PIN-koodi, joka luotiin `Encrypted Vault` varmuuskopiointiprosessin aikana ja jota käytetään varmuuskopiotiedoston salauksen purkamiseen palautuksen aikana.


Nämä ovat kaksi erillistä PIN-koodia. Älä unohda palautus-PIN-koodia, sillä se on välttämätön wallet:n palauttamiseksi."


**Palautus PIN-asetus:**



- Sinun on luotava PIN-koodi tai salasana saadaksesi takaisin pääsyn wallet:een.
- PIN-koodin/salasanan on oltava vähintään 6-numeroinen (vältä esimerkiksi yksinkertaisia sarjoja, kuten 123456, joita ei hyväksytä).
- Ilman tätä PIN-koodia wallet:n palautus on mahdotonta.


Valitse seuraavaksi holvin tarjoaja:



- `Google Drive` tai
- "mukautettu sijainti" (esim. laitteesi)


![image](assets/en/04.webp)


Tallenna nyt `backup-tiedosto`. Napauta seuraavaksi `Test Recovery`, valitse tallennettu varmuuskopiotiedosto tai holvi ja napauta sitten `Decrypt Vault`. Anna `PIN` tai `Salasana`. Jos kaikki toimi, näyttöön tulee `Testaus suoritettu onnistuneesti`.


### Tuonti- / vientitarrat


Nyt kun olemme luoneet varmuuskopiomme, katsotaanpa `Labels`.  Bull Bitcoin wallet parantaa yksityisyyttä ja organisointia antamalla käyttäjille mahdollisuuden luoda mukautettuja tarroja vastaanotto-osoitteita ja tapahtumia varten. Nämä merkinnät auttavat sinua luokittelemaan varojasi, sillä merkityn osoitteen osoitteeseen lähetetyt tapahtumat perivät kyseisen merkinnän, ja voit myös merkitä lähtevät tapahtumat, jotta voit seurata niiden muutoksia. wallet tukee täysin [BIP-329](https://bip329.org/) -standardia, mikä tarkoittaa, että voit viedä kaikki tarrat tiedostoon ja tuoda ne toiseen wallet:aan. Tämä ominaisuus varmistaa, että voit saumattomasti varmuuskopioida tapahtumahistoriasi ja luokittelusi tai siirtää ne wallet:n eri versioiden välillä menettämättä henkilökohtaista organisaatiotasi.


![image](assets/en/05.webp)


## 6️⃣ Asetukset


Kun ensisijainen varmuuskopio on turvattu, tutustutaan muihin asetuksissa käytettävissä oleviin ominaisuuksiin.


### A - Pääsyn varmistaminen


Jos haluat suojata sovelluksen, siirry kohtaan `Asetukset` ja valitse `Turva-PIN` valitaksesi PIN-koodin. Luo vahva PIN-koodi, jolla lukitset pääsyn wallet:een. Vaikka tämä vaihe on valinnainen, se on erittäin suositeltavaa luvattoman käytön estämiseksi, jos joku muu käyttää puhelintasi.


![image](assets/en/06.webp)


### B - Yhteys henkilökohtaiseen solmuun (valinnainen)


Wallet BullBitcoin muodostaa oletusarvoisesti yhteyden Electrum-palvelimiin: Bull Bitcoin:n hallinnoimaan ensimmäiseen ja Blockstreamin toissijaiseen palvelimeen, joiden molempien ei katsota pitävän lokitietoja, mikä vähentää jäljitysriskiä.


Jos haluat lisätä luottamuksellisuutta, voit liittää sovelluksen omaan Bitcoin-solmuun Electrum-palvelimen kautta. Napauta tätä varten "Asetukset" > "Bitcoin-asetukset" > "Electrum Server-asetukset" ja syötä palvelimen osoite ja tunnistetiedot napauttamalla "+ Lisää oma palvelin".


![image](assets/en/07.webp)


### C - Valuutta


Käytettävissä oleva saldo näytetään päänäytöllä sekä sats- että USD-määräisenä. Jos haluat muuttaa tätä, siirry kohtaan `Asetukset` > `Valuutta`. Siellä voit vaihtaa välillä `sats/BTC` ja valita `esiasetetun fiat-valuutan`.


![image](assets/en/08.webp)


### D - Bitcoin Asetukset


Bitcoin Asetukset -valikko tarjoaa syvän pääsyn wallet:n keskeisiin konfiguraatioihin ja tietoihin. Täällä voit tarkastella `Secure Bitcoin`- ja `Instant payments -lompakoiden` perustietoja, mikä antaa sinulle täyden läpinäkyvyyden ja hallinnan. Tämän valikon tärkeimpiä ominaisuuksia ovat mm:



- Wallet Tiedot:** Siirry suojatun Bitcoin:n tai pikamaksujen wallet:n kohdalle nähdäksesi tarkat tiedot.
- Wallet Fingerprint:** wallet:n yksilöllinen tunniste.
- Julkinen avain (Pubkey):** Avain, jota käytetään generate:n Bitcoin-vastaanotto-osoitteisiin.
- Descriptor:** Tekninen yhteenveto wallet:n rakenteesta.
- Derivation Path:** Erityinen polku, jota käytetään generate:n kaikkiin osoitteisiin yksityisestä pääavaimesta.
- Address-näkymä:** Käyttää luetteloa käyttämättömistä vastaanotto-osoitteista ja muuttaa osoitteita (tulossa pian)


Lisäksi sinulla on mahdollisuus:



- "Ota automaattinen siirto käyttöön" -asetuksilla voit asettaa suurimman mahdollisen välittömän wallet-saldon, joka siirretään sitten automaattisesti turvalliseen Bitcoin wallet:een.
- Tuo yleisiä lompakoita `Mnemonic`-lauseen kautta tai tuo `watch-only`-lauseella
- Yhdistä `Hardware-lompakot`: tällä hetkellä tuettuja laitteita ovat ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade ja Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Suoraan wallet:stä pääset [Bull Bitcoin-pörssiin](https://www.bullbitcoin.com/), jonka avulla voit ostaa, myydä ja maksaa Bitcoin:tä poistumatta sovelluksesta. Tämä integraatio tarjoaa kätevän ratkaisun Bitcoin-tarpeidesi hallintaan. Huomaa, että pörssin ja sen palveluiden käyttöä voidaan rajoittaa lainkäyttöalueesi mukaan, ja Know Your Customer (KYC) -tarkistuksen suorittaminen voi olla tarpeen, jotta voit noudattaa sääntelystandardeja ja käyttää alustan kaikkia ominaisuuksia.


Pääset alkuun napauttamalla oikeassa alakulmassa olevaa `Exchange` ja sen jälkeen `Liitäydy` tai `Login` tilillesi.


Pörssi tarjoaa seuraavat [ominaisuudet](https://www.bullbitcoin.com/):



- Osta Bitcoin itsesäilytyksellä pankkitililtäsi
- Muu kuin huoltajuus
- Yksityishenkilöt tai yritykset
- Välitön nosto
- Ei piilotettuja maksuja
- Lightning Network saatavilla
- Ei tapahtumarajoituksia
- Toistuvat ostovaihtoehdot


![image](assets/en/09.webp)


Lisätietoja saat tästä opetusohjelmasta:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Varojen vastaanottaminen


Varojen vastaanottaminen **Bull Bitcoin Wallet**:n avulla on suoraviivaista ja joustavaa, sillä se tukee kolmea erilaista verkkoa, jotka on räätälöity eri käyttötarkoituksiin:



- Bitcoin (onchain)-verkko turvallista pitkäaikaissäilytystä varten.
- Liquid-verkko nopeisiin ja luottamuksellisempiin maksutapahtumiin.
- Lightning-verkko välittömiin ja edullisiin maksuihin.


Sovellus luo automaattisesti sopivan osoitteen tai laskun valitun verkon perusteella. Näin menetellään kunkin verkon osalta.


### Vastaanotto Onchainin kautta (Bitcoin-verkko)


Jos haluat vastaanottaa on-chain-varoja, voit joko valita aloitusnäytöstä "Turvallinen Bitcoin Wallet" ja napauttaa "Vastaanota" tai napauttaa pääpainiketta "Vastaanota" ja valita sitten "Bitcoin-verkko".


Vastaanotto-osoitteen luomiseen on kaksi ensisijaista tapaa:


**Default Mode (URI, jossa on ylimääräisiä syöttöparametreja)


Oletusarvoisesti wallet luo [BIP21 URI](https://bips.dev/21/). Tämä on standardoitu muoto, joka sisältää enemmän tietoa kuin pelkkä osoite, kuten summan, henkilökohtaisen huomautuksen ja PayJoin-parametreja yksityisyyden suojaamiseksi. Tämä kattava URI koodataan QR-koodiksi ja annetaan kopioitavaksi. Muoto näyttää tältä: `bitcoin:<osoite>?<parametri1>=<arvo1>&<parametri2>=<arvo2>`.



- Muita syöttöparametreja:**
    - Summa:** Määritä pyydetty summa BTC:nä, sats:na tai fiat-valuuttana.
    - Viesti:** Lisää henkilökohtainen viesti, joka näkyy lähettäjälle.
    - PayJoin:** Ota tämä vaihtoehto käyttöön, jos haluat parantaa yksityisyyttä yhdistämällä sekä lähettäjän että vastaanottajan syötteet tapahtumassa.


Esimerkki URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Tärkeä huomautus: Älä lähetä varoja tässä opetusohjelmassa mainittuihin osoitteisiin, wallet poistetaan.*


![image](assets/en/10.webp)


**Kopioi tai skannaa vain Address -vaihtoehto käytössä


Kun "Vain Address:n kopiointi tai skannaus"-vaihtoehto on käytössä, sovellus luo yksinkertaisen Bitcoin-osoitteen SegWit-muodossa (bech32).


Esimerkki:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Vaikka kirjoittaisit summan tai huomautuksen, niitä ei sisällytetä QR-koodiin tai kopioituun osoitteeseen.


![image](assets/en/11.webp)


### Vastaanotto Liquid Network:n kautta


Voit vastaanottaa maksun Liquid Network:lle. Kun olet "Vastaanottaa"-näytöllä, sinulla on samat kaksi vaihtoehtoa maksupyynnön luomiseksi:


**1. Yksinkertainen Address:** Kopioi tavallinen Liquid-osoite. Tämä on wallet:n yksilöllinen tunniste Liquid-verkossa, eikä se sisällä mitään erityistä määrää tai viestiä.


Esimerkki Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Yksityiskohtainen maksupyyntö (URI):** Jos haluat strukturoidumman pyynnön, voit määrittää summan ja henkilökohtaisen huomautuksen. Nämä tiedot koodataan automaattisesti jaettavaksi URI:ksi ja sitä vastaavaksi QR-koodiksi.



- Summa:** Voit määrittää summan Bitcoin (BTC), Satoshina (Sats) tai fiat-valuutassa.
- Huomaa:** Lisää henkilökohtainen viesti, joka yksilöi tapahtuman.


**Esimerkki URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Suorita tapahtuma loppuun antamalla lähettäjälle "osoite" tai "URI". Voit tehdä tämän kopioimalla sen leikepöydällesi tai antamalla heidän skannata QR-koodin suoraan näytöltäsi.


![image](assets/en/12.webp)


### Vastaanotto Lightningin kautta



Bull Bitcoin Wallet:n avulla voit myös lähettää ja vastaanottaa maksuja Lightning Network:n kautta. Tärkeä ominaisuus on, että Lightningin kautta vastaanotetut varat vaihdetaan automaattisesti ja tallennetaan Liquid Network:ään Instant Payments Wallet:n sisällä. Tämä palvelu toimii Boltz:n avulla. Tämän rakenteen ansiosta voit nauttia Lightningin nopeudesta ja alhaisista kustannuksista ilman likviditeettikanavien hallinnointiin liittyvää monimutkaisuutta, ja samalla voit säilyttää varojasi täysin itse. Vaikka tämä hybridilähestymistapa on itsesäilyttävä ja välttää kanavien hallinnoinnin monimutkaisuuden, se tuo mukanaan kolmannen osapuolen palvelun (Boltz), pienen swap-maksun ja riippuvuuden Liquid Network:n funktionaalisten toimijoiden liitosta avainten haltijoina, mikä eroaa perinteisestä, ei-säilyttävästä Lightning wallet:sta, jossa sinä hallinnoit omia kanavia. Lisätietoja Liquid:stä ja sen hallintomallista saat täältä:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Rajoitukset:**
    - Vähimmäissumma:** Laskun vähimmäissumma on pakollinen. Tarkista sovelluksesta nykyinen raja
    - Maksut:** Sinä, vastaanottaja, olet vastuussa pienestä vaihtomaksusta. Tämä maksu vähennetään lähettäjän siirtämästä summasta, ja se voi muuttua
- Edut:**
    - Omahuoltajuus:** Varasi ovat aina hallinnassasi Liquid-verkossa.
    - Vältä korkeat On-Chain-maksut:** Käyttämällä Lightningia ja tallentamalla Liquid-kanavaan vältät perinteisen Lightning-kanavan avaamiseen liittyvät on-chain-maksut. Voit siirtää varoja on-chain-kanavaan myöhemmin, kun kertynyt määrä oikeuttaa kulut.
    - Vinkki:** Kustannustehokkain maksutapahtuma kahden Bull Bitcoin-käyttäjän välillä on **Liquid-verkon käyttäminen suoraan**, jolloin vältät Lightning-vaihtomaksut kokonaan.


Jotta voit saada maksun, sinun on tehtävä generate "salamalasku":


1. "Syötä summa "**:** Määritä summa, jonka haluat vastaanottaa Bitcoin (BTC), Satoshina (Sats) tai fiat-valuuttana.

2. `Add a Note` **(Valinnainen):** Lisää muistio tai huomautus. Tämä upotetaan laskuun ja näytetään tapahtumahistoriassa, kun maksu on suoritettu, jolloin se on helpompi tunnistaa.

3. `Invoice Voimassaolo`**:** Lightning-lasku on aikasidonnainen ja päättyy **12 tunnin** kuluttua. Jos sitä ei makseta tämän ajan kuluessa, se mitätöityy, ja sinun on generate hankittava uusi lasku.


Anna lasku lähettäjälle kopioimalla se leikepöydällesi tai antamalla hänen skannata näytölläsi näkyvä QR-koodi.


![image](assets/en/13.webp)


## 9️⃣ Varojen lähettäminen


Voit siirtyä lähetysnäyttöön suoraan etusivulta tai mistä tahansa lompakostasi. Bull Bitcoin Wallet yksinkertaistaa prosessia tunnistamalla automaattisesti kohdeverkon - `Bitcoin`, `Liquid` tai `Lightning` - syöttämäsi osoitteen tai laskun perusteella, riippumatta siitä, onko se liimattu vai skannattu QR-koodilla.


### On-Chain Siirto Bitcoin-verkon kautta


Varojen lähettäminen on-chain tarkoittaa, että transaktiosi kirjataan suoraan Bitcoin-lohkoketjuun. Tämä menetelmä sopii parhaiten suurempiin siirtoihin tai ei-aikaherkkiin siirtoihin. Voit aloittaa napauttamalla `Lähetyspainiketta` alhaalla oikealla ja skannaamalla tai syöttämällä `standardin Bitcoin-osoitteen`.


Jos antamaasi osoitteeseen ei sisälly tiettyä summaa, sinua pyydetään täyttämään tiedot lähetysnäytöllä. Voit määrittää summan haluamassasi yksikössä, kuten BTC:nä, satosheina tai vastaavassa fiat-yksikössä. Sinulla on myös mahdollisuus lisätä henkilökohtainen huomautus, joka on yksityinen muistio, johon voit viitata ja joka auttaa sinua tunnistamaan tapahtuman myöhemmin. Tätä merkintää ei jaeta vastaanottajan kanssa.


Sitä vastoin, jos skannaamasi tai liittämäsi maksupyyntö sisältää jo kaikki tarvittavat tiedot, kuten BIP21 URI:n ja ennalta määritetyn summan, wallet ohittaa tietojen syöttönäytön ja vie sinut suoraan vahvistusnäyttöön maksun hyväksymiseksi.


![image](assets/en/14.webp)


Ennen kuin maksutapahtuma lähetetään, sinulle näytetään vahvistusnäyttö. On erittäin tärkeää, että tarkastelet jokaisen parametrin huolellisesti ja kiinnität huomiota vastaanottajan osoitteeseen, lähetettävään summaan ja verkkomaksuihin. Tämä näyttö tarjoaa myös tehokkaita työkaluja tapahtuman mukauttamiseen.


Voit valvoa maksuja kahdella ensisijaisella tavalla. Ensimmäinen tapa on valita haluamasi tapahtumanopeus, kuten matala, keskitaso tai korkea, jolloin wallet laskee automaattisesti sopivan maksun. Toinen menetelmä mahdollistaa tarkemman ohjauksen, kun voit asettaa tietyn maksun joko absoluuttisena kokonaismääränä satosheina tai suhteellisena maksuna tavua kohti, jolloin saat arvioidun vahvistusajan.


Edistyneemmille käyttäjille wallet tarjoaa useita asetuksia tapahtuman hienosäätöä varten. oletusarvoisesti käytössä on `Replace-by-Fee` (RBF), joka on arvokas ominaisuus, jonka avulla voit nopeuttaa tapahtumaa, jos se juuttuu mempooliin, lähettämällä sen uudelleen korkeammalla maksulla. Voit myös manuaalisesti valita, mistä "Unspent Transaction Outputs" (UTXO) -tapahtumalähteistä kulutetaan. Tämä on tehokas työkalu UTXO-konsolidaatioon, strategiaan, jossa yhdistät useita pieniä panoksia yhdeksi suuremmaksi panokseksi. Vaikka tämä saattaa maksaa enemmän maksuja tämänhetkisestä tapahtumasta, se voi alentaa merkittävästi tulevien tapahtumien maksuja, erityisesti jos verkkomaksujen odotetaan nousevan.


![image](assets/en/15.webp)


PayJoin yritetään automaattisesti, kun skannaat vastaanottajan maksupyynnön (BIP21 URI), joka sisältää parametrin `pj=`. Jos liität pelkän osoitteen ilman lisäparametreja, tämä ominaisuus ei aktivoidu. Tämä yhteistoiminnallinen menetelmä parantaa yksityisyyttä yhdistämällä sekä lähettäjän että vastaanottajan syötteet, murtamalla yhteisen syötteen omistusheuristiikan ja mahdollistamalla paremman skaalautumisen ja maksusäästöt joissakin tilanteissa.


### Lähettäminen Liquid Network:ään


Liquid Network on suunniteltu nopeisiin ja luottamuksellisiin maksutapahtumiin, joissa maksut ovat minimaaliset. Kun lähetät varoja Liquid:n kautta, ne nostetaan pikamaksujen Wallet:stä. Prosessi on yksinkertainen: syötät tai skannaat vain vastaanottajan Liquid-osoitteen.


Jos osoitteessa ei ole määritetty summaa, sinua pyydetään antamaan se lähetysnäytössä. Voit antaa summan BTC:nä, satoshina tai fiatina. Liquid:n keskeinen etu on sen matala vähimmäiskynnys. Kuten on-chain-tapahtumissa, voit lisätä valinnaisen henkilökohtaisen huomautuksen omia tietojasi varten. Jos maksupyyntö sisältää jo summan, wallet siirtyy suoraan vahvistusnäyttöön.


Liquid-tapahtuman vahvistusnäytöllä tarkastelet tapahtuman yksityiskohtia. Maksut ovat huomattavan alhaiset, ja ne lasketaan tapahtuman monimutkaisuuden perusteella. Ne ovat tyypillisesti noin 0,1 sat/vB, mikä yksinkertaisessa transaktiossa on vain 20-40 satoshia (esimerkiksi 26 satoshia 21. joulukuuta 2025).


![image](assets/en/16.webp)


### Lähettäminen Lightning Network:een


Voit joko skannata salaman Address (esim. "runningbitcoin@rizful.com"), jolloin voit määrittää summan ja valinnaisen huomautuksen vastaanottajalle, tai skannata laskun, jossa on ennalta määritetty summa, jolloin pääset suoraan vahvistusnäyttöön.


*Huomaa, että vähimmäismäärät ja maksut ovat voimassa.*


Bull Bitcoin Wallet lähettää Lightning-maksuja nostamalla varoja "Pikamaksut Wallet:stä" (Liquid:ssä) ja vaihtamalla ne "Boltz:n" kautta. Tämä hybridimenetelmä on täysin omahoitoinen, ja sillä vältetään erillisen Lightning-kanavan hallinnoinnista aiheutuvat korkeat on-chain-maksut, mutta se edellyttää vaihtomaksun maksamista. Edullisinta on lähettää suoraan vastaanottajan Liquid-osoitteeseen, jos tämä käyttää myös Bull Bitcoin wallet:ta.


## 🔟 Varojen siirtäminen lompakoiden välillä


Bull Bitcoin:n avulla voit siirtää Bitcoin:n turvallisen Bitcoin:n ja wallet:n sekä Liquid Network:ssä olevan Wallet:n tai ulkoisen Wallet:n välillä. Siirron suorittamiseksi siirry vain `Transfer`-osioon, valitse lähde- ja kohdelompakot, syötä summa, jonka haluat siirtää, ja vahvista tapahtuma.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Bull Bitcoin Wallet:n talteenotto


Tässä osiossa kerrotaan, miten saat Bull Bitcoin Wallet-varat takaisin käyttöösi, jos kadotat laitteesi, poistat sovelluksen tai haluat yksinkertaisesti vaihtaa uuteen laitteeseen. Kuten jo selitettiin, on olemassa kaksi ensisijaista palautusmenetelmää: käyttämällä ainutlaatuista `Recoverbull`-menetelmää ja käyttämällä tavallista `BIP39 seed -lausetta`.


### Menetelmä 1: Recoverbull


Yhteenveto: Wallet varmuuskopiot salataan paikallisesti. Salattu tiedosto voidaan tallentaa pilvitallennukseen tai toiseen laitteeseen. Salausavain tallennetaan Recoverbull Key Server -palvelimelle. Molemmat säilytetään erillään, ja ne on yhdistettävä wallet:n palauttamiseksi.


Aluksi poistan Wallet:n kaikkine varoineen ja asennan wallet:n uudelleen. Laskeudumme jälleen `Tervetuloa-näytölle`. Tällä kertaa valitsemme vaihtoehdon `Recover Wallet`. Siirry sitten `Encrypted Vault` -menetelmään, vahvista, että käytät `Default Key server` -avainpalvelinta, ja valitse sijainti tai `Vault provider`, johon olet tallentanut varmuuskopiotiedoston.


![image](assets/en/18.webp)


Se ilmoittaa, että holvin tuonti onnistui. Napauta `Decrypt Vault`-painiketta ja syötä `PIN`. Seuraavalla näytöllä näytetään "saldot" ja "talteen otettujen tapahtumien määrä".


![image](assets/en/19.webp)


### Menetelmä 2: siemenlause


Tässä menetelmässä käytetään wallet:n master recovery -lausetta, joka on vakiomuotoinen 12 sanan luettelo, joka toimii varojen lopullisena varmuuskopiona. Se on yleisin tapa palauttaa Bitcoin wallet, koska se ei ole sidottu mihinkään tiettyyn palveluun tai palvelimeen. Kunhan sinulla on tämä lauseke, voit palauttaa wallet:n millä tahansa yhteensopivalla laitteella, vaikka sinulla ei olisi pääsyä Bull Bitcoin-avainpalvelimeen.


Valitse Tervetuloa-näytöstä "Palauta Wallet". Valitse tällä kertaa `Fyysinen varmuuskopiointi`. Sovellus esittää sanaruudukon. Valitse huolellisesti jokainen sana 12-sanaisesta seed-lauseesta oikeassa järjestyksessä. Ole huolellinen, sillä yksikin virhe johtaa virheelliseen wallet:een.


## 1️⃣2️⃣ Hardware Wallet:n liittäminen


Korkeimman turvallisuustason saavuttamiseksi monet Bitcoin-käyttäjät säilyttävät varansa "kylmäsäilytyksessä". Tämä tarkoittaa, että Bitcoin:aa ohjaavat yksityiset avaimet säilytetään laitteessa, joka ei ole koskaan yhteydessä internetiin. wallet (tai allekirjoituslaite) on fyysinen laite, joka on suunniteltu juuri tähän tarkoitukseen. Se toimii ikään kuin digitaalisena holvina avaimillesi ja varmistaa, etteivät ne ole koskaan alttiina verkossa olevan tietokoneen tai älypuhelimen mahdollisille uhkille.


Yhdistämällä wallet-laitteiston Bull Bitcoin-sovellukseen saat molempien maailmojen parhaat puolet: yksityisten avainten tinkimättömän kylmävarastoinnin turvallisuuden yhdistettynä Bull Bitcoin wallet:n tehokkaisiin ominaisuuksiin ja käyttäjäystävälliseen käyttöliittymään saldojen tarkastelua ja tapahtumien hallintaa varten. Tässä viimeisessä luvussa näytämme, miten laitteistokäyttöinen wallet, kuten [Coldcard Q](https://coldcard.com/q), liitetään Bull Bitcoin wallet:een. Tässä oppaassa ei käsitellä Coldcard Q:n käyttöönottoa perusteellisesti; voit tutustua siihen täällä:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Wallet:n tuonti


![image](assets/en/26.webp)


Valitse ensin Coldcard Q:n päävalikosta `Export Wallet` ja valitse sitten `Bull Wallet`. Coldcard-korttiisi tulee generate QR-koodi.


![image](assets/en/20.webp)


Avaa Bull Bitcoin Wallet ja siirry kohtaan `Asetukset` > `Bitcoin-asetukset` > `Import wallet` ja valitse puhelimessasi `Coldcard Q` ja napauta `Avaa kamera` skannataksesi tämän QR-koodin tuodaksesi laitteistosi wallet:n julkiset avaimet.


![image](assets/en/21.webp)


### Vastaanotto Coldcard Q:lla


Jotta voit vastaanottaa Bitcoin:n yhdistetyllä Coldcard Q:lla, laitteen ei tarvitse olla fyysisesti yhdistettynä puhelimeen. Bull Bitcoin Wallet on jo tuonut tarvittavat julkiset avaimet, joten se voi käyttää generate-osoitteita yksinään.


1. Napauta tuotua Coldcard Q -signointilaitetta ja valitse `Vastaanottaa`.

2. Sovellus näyttää automaattisesti tuoreen Bitcoin-osoitteen Coldcardin wallet-osoitteesta.

3. Käytä tätä osoitetta varojen vastaanottamiseen. Bitcoin kiinnitetään suoraan laitteiston wallet:n avaimiin, vaikka laite oli prosessin aikana offline-tilassa.


![image](assets/en/22.webp)


### Lähettäminen Coldcard Q:lla


Bitcoin:n lähettäminen Coldcard Q -kortin kanssa edellyttää fyysistä vahvistusta, jotta voit hyväksyä minkä tahansa tapahtuman. Vaikka Bull Wallet -sovellusta käytetään tapahtuman luomiseen, lopullinen allekirjoitus voidaan luoda vain itse laitteistolla wallet.


Avaa Kortti Q wallet ja napauta Lähetä. Avaa sitten kamera ja skannaa vastaanottavan osoitteen QR-koodi. Skannauksen jälkeen syötä lähetettävä summa ja säädä maksuprioriteetti tarpeen mukaan.


Lisää vaihtoehtoja löydät Lisäasetukset-kohdasta. Täältä löydät vaihtoehdon `Replace by Fee` (RBF), joka on oletusarvoisesti aktivoitu ja jonka avulla voit nopeuttaa jumissa olevaa maksutapahtumaa myöhemmin. Käytössäsi on myös vaihtoehto `Coin Control`, jonka avulla voit valita manuaalisesti tietyt UTXO:t, jotka haluat käyttää.


Kun olet tarkistanut kaikki tiedot, napauta `Show PSBT` valmistellaksesi tapahtumaa.


![image](assets/en/23.webp)


Napauta Coldcard Q:n Skannaa-painiketta ja skannaa puhelimessa näkyvä QR-koodi kameran avulla. Coldcardin näytöllä näkyvät sitten kaikki tapahtuman tiedot. Tarkista huolellisesti summa, vastaanottajan osoite ja muutososoitteesi. Jos kaikki on oikein, allekirjoita tapahtuma painamalla Coldcard Q:n Enter-painiketta. Seuraavaksi näytölle ilmestyy allekirjoitetun tapahtuman QR-koodi.


![image](assets/en/24.webp)


Napauta Bull wallet:ssä "Olen valmis" ja napauta sitten "Kamera"-painiketta skannataksesi Coldcard Q:n "allekirjoitetun tapahtuman" QR-koodin. Bull Wallet näyttää nyt yhteenvetonäytön allekirjoitetusta tapahtumasta. Tarkista se vielä kerran ja napauta sitten `Broadcast` Transaction. Tämä viimeistelee prosessin lähettämällä tapahtuman Bitcoin-verkkoon, ja rahasi ovat matkalla.


## 🎯 Päätelmät


Olet nyt suorittanut matkasi Bull Bitcoin Wallet:n läpi. Sovellus tuo tehokkaat yksityisyys- ja tietoturvatyökalut suoraan käden ulottuville, ja kehittyneet ominaisuudet ovat helppokäyttöisiä. Se auttaa sinua pysymään yksityisenä sellaisilla ominaisuuksilla kuin `PayJoin`, joka piilottaa transaktiosi lohkoketjuun, ja `Tor-integraatio`, joka peittää verkkotoimintasi uteliailta katseilta. Jos haluat täydellisen hallinnan, voit muodostaa yhteyden omaan henkilökohtaiseen Bitcoin-solmuun, jolloin et ole enää riippuvainen kolmannen osapuolen palvelimista, ja käyttää `Hardware wallet` -laitteistoa, jolla voit pitää yksityiset avaimesi täysin offline-tilassa ja turvassa. Älykkäät varmuuskopiointivaihtoehdot ja saumaton tuki Bitcoin:lle, Liquid:lle ja Lightningille tekevät Bull Bitcoin Wallet:sta vahvan, kaiken kattavan valinnan kaikille, jotka haluavat pitää varansa yksityisinä, turvallisina ja täysin omassa hallinnassaan.


## 📚 Bull Wallet Resurssit


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Verkkosivusto ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)