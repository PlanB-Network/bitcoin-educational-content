---
name: be-BOP
description: Käytännön opas liiketoimintasi rahaksi muuttamiseen be-BOP:n avulla
---

![cover-bebop](assets/cover.webp)



**be-BOP** on verkkokauppa-alusta, joka on suunniteltu yrittäjille, jotka haluavat myydä verkossa ja sen ulkopuolella täysin itsenäisesti ja hyväksyä maksuja Bitcoin:ssa, pankkitilin kautta ja käteisellä. Ratkaisu on hyödyllinen myös kaikenlaisille organisaatioille, jotka haluavat kerätä lahjoituksia tai hyödyntää eri toimintojaan.



Ratkaisu on yksinkertainen, kevyt ja itsenäinen. Se mahdollistaa verkkokaupan perustamisen myös ympäristössä, jossa perinteiset rahoituspalvelut ovat rajalliset tai puuttuvat kokonaan. **be-BOP** on suunniteltu toimimaan tehokkaasti pankkien kanssa tai ilman niitä, ja se käyttää Bitcoin:tä maksuinfrastruktuurina.



Tässä opetusohjelmassa käymme askel askeleelta läpi :





- Luo ensimmäinen verkkokauppasi **be-BOP**:n avulla
- Henkilökohtaistakaa vitriininne ja tuotteenne
- Määritä käytettävissä olevat maksutavat
- Ymmärrä parhaat käytännöt tehokkaaseen verkkomyyntiin **be-BOP**:n avulla



Tämä opetusohjelma ei vaadi kehittyneitä teknisiä taitoja. Se on suunnattu kehittäjille sekä käsityöläisille, kauppiaille, osuuskunnille tai yrittäjille, jotka haluavat aloittaa digitaalisen kaupankäynnin suvereenisti ja joustavasti.



## Edellytykset be-BOP:n asentamiseksi omalle palvelimellesi



Ennen kuin aloitat be-BOP:n asentamisen, varmista, että sinulla on seuraava tekninen infrastruktuuri. Nämä Elements ovat välttämättömiä, jotta alusta toimisi oikein:



### S3-yhteensopiva varastointi



be-BOP käyttää tallennusjärjestelmää tiedostojen (kuten tuotekuvien) hallintaan. Tämä edellyttää pääsyä S3-palveluun, kuten :





- [MinIO](https://min.io/) itsepalveluperiaatteella toimiva
- Amazon S3 (AWS)
- Scaleway Object Storage



Sinun on määritettävä ämpäri ja annettava seuraavat tiedot:





- S3_BUCKET**: kauhan nimi
- S3_ENDPOINT_URL**: pääsylinkki S3-palveluun
- S3_KEY_ID** ja S3_KEY_SECRET: pääsykoodisi
- S3_REGION**: S3-palvelun alue



### MongoDB-tietokanta ReplicaSet-tilassa



be-BOP käyttää MongoDB:tä myymälä-, käyttäjä-, tuote- ja muiden tietojen tallentamiseen.



Sinulla on kaksi vaihtoehtoa:





- Asenna MongoDB paikallisesti ja ota **ReplicaSet-tila käyttöön**
- Käytä verkkopalvelua, kuten **MongoDB Atlas**



Tarvitset seuraavat muuttujat:





- MONGODB_URL**: tietokantayhteys Address
- MONGODB_DB**: tietokannan nimi



## Node.js-ympäristö



be-BOP toimii Node.js:n kanssa. Varmista, että sinulla on **Node.js**-versio 18 tai uudempi ja **Corepack** käytössäsi (tarvitaan paketinhallintaohjelmien kuten pnpm:n hallintaan). Käsky on `corepack enable`



### Git LFS asennettu



Joitakin resursseja (kuten suuria kuvia) hallitaan Git LFS:n (Large File Storage) avulla. Varmista, että Git LFS on asennettu koneellesi komennolla `git lfs install`. Kun nämä ennakkoedellytykset ovat kunnossa, voit siirtyä seuraavaan vaiheeseen: be-BOP:n lataamiseen ja konfigurointiin.



**Huomautus:** Ohjelmiston käyttöönoton tekninen opas on saatavilla erillisessä oppaassa.



## Super-Admin-tilin luominen



Kun be-BOP käynnistetään ensimmäistä kertaa, luodaan **Super Admin**-tili. Tällä tilillä on kaikki back-office-toimintojen hallintaan tarvittavat valtuudet. Luo tili noudattamalla seuraavia ohjeita:





- Siirry osoitteeseen `yourresiteweb/admin/login`
- Luo super-admin-tili, jolla on turvallinen käyttäjätunnus ja salasana



Tämä tili antaa sinulle pääsyn kaikkiin back-office-toimintoihin. Kun olet luonut tilin, voit kirjautua sisään syöttämällä käyttäjätunnuksesi ja salasanasi.



![login](assets/fr/001.webp)



## Back-Office-konfigurointi ja tietoturva



Ennen kuin konfiguroit Interface-toimistoyhteyden, sinun on luotava yksilöllinen Hash. Tämä suojaa haitallisilta toimijoilta, jotka yrittävät varastaa yhteyslinkin Interface:n ylläpitäjään.



Luodaksesi Hash:n, siirry osoitteeseen `/admin/Settings`. Määrittele tietoturvaa koskevassa osiossa (esim. "Admin Hash") yksilöllinen merkkijono (Hash). Rekisteröinnin jälkeen back-office-URL-osoite muutetaan (esim. `/admin-yourhash/login`), jotta asiattomien henkilöiden pääsy rajoitetaan.



![hash-login](assets/fr/002.webp)



2.2. Aktivoi huoltotila (tarvittaessa)



Vielä /admin/Settings, (Settings > General via Interface graphics) Tarkista "enable maintenance mode" vaihtoehto sivun alareunassa.



![maintenance-mode](assets/fr/003.webp)



Tarvittaessa voit määrittää luettelon valtuutetuista IPv4-osoitteista (pilkulla erotettuna), jotta etutoimistoon pääsee käsiksi huollon aikana. Järjestelmänvalvojat pääsevät edelleen takatoimistoon.



![ip-bebop](assets/fr/004.webp)



## Viestintäasetukset



Jotta be-BOP voi lähettää ilmoituksia (esim. tilauksista, rekisteröinneistä tai järjestelmäviesteistä), sinun on määritettävä vähintään yksi viestintätapa. Käytettävissä on kaksi vaihtoehtoa: sähköposti (SMTP) tai Nostr.



### SMTP-konfigurointi (sähköposti)



be-BOP voi lähettää sähköposteja SMTP-palvelimen kautta. Tarvitset voimassaolevat SMTP-tunnukset, jotka sähköpostipalvelu (esim. Mailgun, Gmail jne.) usein antaa.



Sinun on tiedettävä seuraavaa:



SMTP_HOST: SMTP-palvelimen Address (esim. smtp.mailgun.org)



SMTP_PORT: käytettävä portti (usein 587 tai 465)



SMTP_USER: käyttäjänimesi (yleensä sähköpostiosoite Address)



SMTP_PASSWORD: salasanasi tai API-avaimesi



SMTP_FROM: sähköpostin Address, joka näkyy lähettäjänä




### Nostr-konfiguraatio



be-BOP:n avulla voit lähettää ilmoituksia Nostr-protokollan, hajautetun sanomanvälitysinfrastruktuurin, kautta. Tätä varten tarvitset generate tai Supply Nostrin yksityisen avaimen (NSEC). Voit generate tämän avaimen suoraan be-BOP:n Interface:n kautta, Nostrille omistetussa osiossa. Kun nämä Elements on määritetty oikein, be-BOP pystyy automaattisesti lähettämään viestejä ja hälytyksiä käyttäjillesi.



## Yhteensopivat maksutavat



be-BOP on yhteensopiva useiden maksuratkaisujen kanssa, joten voit tarjota asiakkaillesi enemmän joustavuutta. Seuraavassa kerrotaan, mitä tarvitset, jotta voit määrittää sinulle parhaiten sopivan maksutavan.



### Bitcoin Onchain



be-BOP:n avulla voit hyväksyä Bitcoin-maksuja suoraan Blockchain:lla (On-Chain:llä), yksinkertaisesti ja turvallisesti.



**Konfiguroinnin vaiheet:**





- Siirry **Maksuasetukset** -valikkoon
- Napsauta **Bitcoin Nodeless** päästäksesi On-Chain-maksuparametreihin.
- Täytä seuraavat kentät:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Vinkki:** Laajennetun julkisen avaimesi (Zpub) saat Bitcoin Wallet:n (Sparrow wallet, BlueWallet, Specter jne.) lisäasetuksista. Varmista, että Wallet on **ei vain luku**, jos aiot käyttää tapahtumahistoriaa.



### Lightning Network



be-BOP voi myös hyväksyä välittömiä Bitcoin-maksuja Lightning Network:n ansiosta. Tällä hetkellä käytettävissä on kaksi kokoonpanovaihtoehtoa:



**Phoenixd**



Mene `Maksuasetukset`-valikkoon, klikkaa `Phoenixd`



![phoenixd](assets/fr/006.webp)



Tämän jälkeen sinun on syötettävä **salasana tai token-todennus**, joka yhdistää sinut Phoenixd-instanssiin, Acinqin kehittämään backendiin, jonka avulla voit hallita Lightning-maksuja omalla solmulla, mutta ilman maksukanavien hallinnan monimutkaisuutta.



**Swiss Bitcoin Pay**



Jos et halua hallita Lightning-solmua itse, **Swiss Bitcoin Pay** on käyttövalmis, helposti konfiguroitava ratkaisu, joka sopii erinomaisesti Lightning-maksujen hyväksymisen aloittamiseen ilman monimutkaista infrastruktuuria.



Konfigurointivaiheet :





- Klikkaa "Maksuasetukset"-valikossa `Swiss Bitcoin Pay`
- Kirjaudu sisään sveitsiläiselle Bitcoin Pay -tilillesi (tai luo tili, jos sinulla ei vielä ole sellaista).
- Syötä Swiss Bitcoin Payn toimittama API-avain ja napsauta sitten "Tallenna"



Kun be-BOP on perustettu, se lähettää automaattisesti generate Lightning -laskut asiakkaillesi, ja saat maksut suoraan Swiss Bitcoin Pay -tilillesi. Tämä ratkaisu on ihanteellinen käyttäjille, jotka haluavat välttää henkilökohtaisen solmupisteen teknisen monimutkaisuuden ja hyväksyä samalla nopeita ja edullisia maksuja.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Bitcoin:n lisäksi be-BOP:n avulla voit hyväksyä käteismaksuja myös PayPalin kautta, joka on tunnettu ja laajalti käytetty kansainvälinen ratkaisu.



Konfigurointivaiheet :





- Siirry valikkoon `Maksuasetukset`
- Klikkaa `PayPal
- Syötä Paypal-tilillesi (kehittäjäosio) `Client ID` ja `Secret`
- Valitse haluamasi valuutta (esim. **USD**, **EUR**, **XOF** jne.)
- Napsauta `save



![paypal](assets/fr/008.webp)



**Huomaa:** Sinulla on oltava PayPal-liiketoimintatili, jotta voit käyttää generate-tunnuksia. Saat ne [kehittäjä]portaalin kautta (https://developer.paypal.com)



### SumUp



Ohjelmisto integroi nyt **SumUp**-maksuratkaisun, jonka avulla voit hyväksyä luottokorttimaksuja yksinkertaisesti, turvallisesti ja tehokkaasti. Tämän toiminnallisuuden hyödyntäminen edellyttää alustavaa konfigurointia. Seuraavassa on vaiheet, jotka on numeroitu selkeää ja asteittaista käyttöönottoa varten:





- Aloita syöttämällä **API Key**, luottamuksellinen avain, jonka SumUp toimitti sinulle, kun loit kehittäjätilisi. Se luo turvallisen yhteyden SumUp-tilisi ja ohjelmiston välille.
- Täytä `Merchant Code` -kenttään ainutkertainen koodi, joka tunnistaa yrityksesi SumUp-alustalla. Tämä koodi on välttämätön, jotta transaktiot voidaan yhdistää yritykseesi.
- Valitse `Valuutta`-kentässä päävaluutta, jota käytät tapahtumissasi (esim. **EUR**, **USD**, **CDF** jne.).
- Kun kaikki kentät on täytetty oikein, tallenna asetukset napsauttamalla Tallenna-painiketta. Tämän jälkeen järjestelmä luo linkin SumUp-tiliisi, ja ohjelmistosi on valmis hyväksymään maksuja.



![payment-sumup](assets/fr/009.webp)



Tämän konfiguroinnin jälkeen **SumUp**-integraatio on aktiivinen ja toiminnassa, jolloin voit nopeasti nostaa rahaa ja seurata tapahtumia suoraan ohjelmistosta.



### Raita



be-BOP tarjoaa myös täydellisen integraation **Stripe**:n kanssa, joka on yksi suosituimmista verkkomaksualustoista. Stripen avulla voit hyväksyä verkkomaksuja luottokortilla, digitaalisella Wallet:llä ja useilla muilla maksutavoilla. Näin se aktivoidaan:





- Syötä Stripen kojelaudassa annettu **salattu avain**.
- Täytä **Julkinen avain** -kenttä, jonka Stripe myös tarjoaa.
- Valitse **päävaluutta**.
- Tallenna kokoonpano ja napsauta sitten `Save`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Huomaa:** Toimintaasi sovellettavan arvonlisäverojärjestelmän tunteminen on välttämätöntä (esim. myyjän maan arvonlisäverollinen myynti, vapautus perustelujen mukaan tai myynti ostajan maan arvonlisäverokannalla), jotta **be-BOP**:n laskutusvaihtoehdot voidaan konfiguroida oikein.



## Valuuttakokoonpano



**be-BOP** tarjoaa kehittynyttä valuutanhallintaa ja on mukautettu monivaluuttaympäristöihin ja erityisiin kirjanpitovaatimuksiin. Taloustoimien ja raportoinnin yhdenmukaisuuden varmistamiseksi on tärkeää määrittää järjestelmässä käytettävät eri valuutat oikein. Seuraavassa on vaiheet, joita on noudatettava tätä konfigurointia varten:





- Valitse **päävaluutta** (`Päävaluutta`)
- Valitse `Sekundaarivaluutta
- Määritä **viitevaluutta** (`Hinnan viitevaluutta`)
- Ilmoita "kirjanpitovaluutta



Kun kaikki valuutat on määritetty oikein, ohjelmisto varmistaa monivaluuttatapahtumien automaattisen ja tarkan muuntamisen säilyttäen samalla kirjanpidon johdonmukaisuuden.



![settings-currencies](assets/fr/011.webp)



## Palautusyhteyden konfigurointi sähköpostitse tai Nostr:n kautta



Varmista edelleen `/admin/settings` -moduulin **ARM** kautta, että super-admin-tilillä on **sähköposti Address** tai **palautuspub**, mikä helpottaa menettelyä, jos unohdat salasanasi.



![settings-users](assets/fr/012.webp)



## Kieliasetukset



Ohjelmistossa on monikielisyysominaisuudet, jotta se soveltuu kansainväliselle yleisölle ja parantaa käyttäjäkokemusta. Monikielisen toiminnallisuuden aktivoimiseksi on tärkeää määrittää käytettävissä olevat kielet ja määrittää **esiasetuskieli**.



![settings-languages](assets/fr/13.webp)



## Interface ja identiteetin konfigurointi be-BOP:ssa



**be-BOP** tarjoaa suunnittelijoille kaikki työkalut, joita he tarvitsevat verkkosivuston suunnitteluun. Ensimmäinen vaihe on avata asetusten `/Admin > Merch > Layout` -osio. Aloita määrittelemällä **Top Bar**, **Navbar** ja **Footer**.



### Le Top Bar



**Top Bar** -konfiguraation avulla voit muokata ohjelmistosi visuaalista identiteettiä näyttämällä tärkeimmät tiedot heti Interface:n ensimmäisellä rivillä. Tämä vahvistaa brändin tunnistettavuutta ja tarjoaa käyttäjille selkeän kontekstin.



#### Konfigurointivaiheet :





- Kirjoita `Brand name`-kenttään yrityksesi, organisaatiosi tai tuotteesi nimi. Tämä nimi näkyy Interface:n yläosassa ja edustaa tärkeintä visuaalista identiteettiäsi.
- Ilmoita verkkosivuston otsikko**: valitun otsikon tulisi tiivistää alustan tarkoitus. Otsikko voi näkyä otsikossa tai selaimen välilehdessä.
- Lisää verkkosivuston kuvaus**: Tähän voit kirjoittaa lyhyen kuvauksen aloitteestasi. Tämä kuvaus auttaa käyttäjiä käyttämään työkalua ja sitä voidaan käyttää myös hakukoneoptimointitarkoituksiin.



Kun nämä tiedot on syötetty, **Top Bar** näyttää selkeän, ammattimaisen ja johdonmukaisen esityksen ratkaisustasi.



#### Linkit yläpalkissa



Yläpalkin Linkit-osiossa voit lisätä pikakuvakkeita tärkeille sivuille sovelluksessasi tai ulkoisilla sivustoilla. Nämä linkit näkyvät suoraan yläpalkissa ja tarjoavat käyttäjillesi nopean ja jäsennellyn pääsyn.



#### Konfigurointivaiheet :





- Kirjoita linkin nimi (Teksti)**: Kirjoita "Teksti"-kenttään linkin nimi tai nimike sellaisena kuin se näkyy (esim. Etusivu, Yhteystiedot, Ohje...).
- Ilmoita linkki Address (Url)**: Kirjoita kohdesivun (sisäinen tai ulkoinen) Address kokonaisuudessaan `Url`-kenttään.
- Lisää tarvittaessa muita linkkejä**: Kullakin määritysrivillä voit lisätä lisälinkin käyttämällä `Text`- ja `Url`-kenttiä.
- Tallenna linkit**: Kun kaikki linkit on syötetty, tallenna ne napsauttamalla "Lisää yläpalkin linkki" -painiketta.



Tämän kokoonpanon avulla voit tarjota selkeän, sujuvan ja helppokäyttöisen navigoinnin verkkosivustosi eri osioissa tai täydentäviin resursseihin.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



**Navbar**-osiossa voit määrittää be-BOP:n päänavigointivalikon, joka sijaitsee yleensä Interface:n sivulla tai yläosassa. Tämä valikko ohjaa käyttäjiä sovelluksen eri sivuille ja toimintoihin. Linkkien konfigurointi on yksinkertaista ja intuitiivista. Näin se toimii:





- Kirjoita linkin nimi (`Text`)**: Aloita konfigurointirivillä täyttämällä `Text`-kenttä. Tämä vastaa navigointipalkissa näkyvän linkin nimeä (esimerkkejä: *Dashboard*, *Users*, *Settings*...).
- Kirjoita linkki Address (`Url`)**: `Text`-kentän vieressä on `Url`-kenttä. Kirjoita tähän kenttään sen sivun Address, johon linkin pitäisi ohjata. Tämä voi olla sisäinen reitti tai linkki ulkoiselle sivulle.
- Lisää tarvittaessa useita linkkejä**: Ensimmäisen rivin alapuolella on käytettävissä uudet `Text`- ja `Url`-kentät, joihin voit lisätä niin monta linkkiä kuin haluat. Kukin rivi edustaa ylimääräistä navigointilinkkiä.
- Tallenna linkit**: Kun olet syöttänyt kaikki Elements:t, napsauta `Lisää navigaattorilinkki`-painiketta tallentaaksesi ja näyttääksesi tulokset navigaatiopalkissa.



Tämä kokoonpano mahdollistaa tehokkaan rakenteellisen pääsyn ohjelmiston eri osiin, mikä parantaa ergonomiaa ja käyttäjäkokemusta.



![navbar](assets/fr/015.webp)



### Alatunniste



**Jalkatunniste**-osiossa voit mukauttaa ohjelmiston alatunnisteen lisäämällä siihen hyödyllisiä tietoja tai linkkejä. Ennen linkkien määrittämistä aloita aktivoimalla tietty vaihtoehto:





- Ota käyttöön "Powered by be-BOP "** -merkintä: aktivoi `Näytä Powered by be-BOP`-painike, jotta tämä merkintä näkyy alatunnisteessa.
- Kirjoita linkin nimi (`Text`)**: täytä `Text`-kenttä, joka vastaa linkin sanamuotoa alatunnisteessa (esimerkkejä: *Ehdot*, *Turva*, *Yhteydenotto*...).
- Ilmoita linkki Address (`Url`)**: Kirjoita `Url`-kenttään kohdesivun Address (sisäinen tai ulkoinen).
- Lisää tarvittaessa lisää linkkejä**: käytä lisärivejä luodaksesi niin monta linkkiä kuin haluat.
- Tallenna linkit**: Tallenna linkit napsauttamalla "Lisää alatunnisteen linkki" -painiketta.



![footer](assets/fr/016.webp)



### Visuaalinen personointi



**⚠️ Muista asettaa logot vaaleille ja tummille teemoille sekä favicon, kautta** `Admin > Merch > Pictures`.



Näin voit mukauttaa sivustosi ulkoasua ja tunnelmaa:



#### Siirry Kuvat-osioon



Valikko `Admin` > `Merch` > `Pictures`.



#### Lisää uusi kuva



Napsauta `Uusi kuva`.



#### Valitse paikallinen tiedosto



Napsauta `Choose Files` ja valitse sitten kuva Hard-levyltäsi.



#### Valitse tuotava tiedosto



Kaksoisnapsauta tuotavaa kuvaa (vaalea logo, tumma logo tai favicon).



#### Kuvan nimeäminen



Täytä `Kuvan nimi`-kenttä.



#### Lisää kuva



Napsauta `Add` viimeistelläksesi tuonnin.



![pictures](assets/fr/017.webp)



### Myyjän identiteetin asennus



#### Identiteetin asetukset



Tähän osioon pääset valikosta `Admin > Identity` (tai `Settings > Identity`), ja tässä osiossa voit määrittää yrityksesi hallinnolliset ja oikeudelliset tiedot.



#### Oikeudelliset tiedot





- Toiminimi**: yrityksen virallinen nimi.
- Yritystunnus**: oikeudellinen tunniste tai rekisteröintinumero (RCCM, SIRET...).



#### Liiketoiminta Address





- Street**: postinumero Address (katu, numero...).
- Maa**: maa.
- Osavaltio**: maakunta tai alue.
- Kaupunki**: kaupunki.
- Postinumero**: postinumero.



#### Yhteystiedot





- Sähköposti**: ammattimainen sähköposti Address.
- Puhelin**: yrityksen puhelinnumero.



#### Pankkitili





- Tilinomistajan nimi**: tilinomistajan nimi.
- Tilinhaltija Address**: tilinhaltijan Address.
- IBAN**: International Bank Account Number.
- BIC**: SWIFT/BIC-koodi.



![bank-account](assets/fr/019.webp)



#### Laskutus





- Napsauta `Fill with main shop informations` (Täytä tärkeimmät myymälän tiedot) tietojen esitäyttämiseksi.
- Very-top-right issuer information**: kenttä laskuissa näkyviä oikeudellisia/verotuksellisia tietoja varten.
- Tallenna muutokset napsauttamalla `Update`.



**Huomautus:** voit myös syöttää Invoice:ssa näytettäviä lisätietoja tarpeidesi mukaan.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Fyysinen myymälä Address



Niille, joilla on fyysinen myymälä, voit lisätä erityisen täyden Address:n kohdassa `Admin > Settings > Identity` tai erillisessä osiossa. Näin se voidaan näyttää virallisissa asiakirjoissa ja tarvittaessa alatunnisteessa.



![seller-id](assets/fr/021.webp)



## Tuotehallinta



### Uuden tuotteen luominen



Mene kohtaan `Admin > Merch > Tuotteet` lisätäksesi tai muuttaaksesi tuotetta. Täytä seuraavat kentät:



#### Perustiedot





- Tuotteen nimi**: tuotteen nimi (esim. *BOP T-paita limited edition*).
- Etana**: URL-tunniste ilman välilyöntejä (esim. `tshirt-bop-edition-limitee`).
- Alias** *(valinnainen)*: hyödyllinen, kun haluat lisätä tuotteen nopeasti koriin erillisen kentän kautta.



![product-config](assets/fr/028.webp)



#### Hinnoittelu





- Hintamäärä**: tuotteen hinta (esim. `25.00`).
- Hintavaluutta**: valuutta (EUR, USD, BTC jne.).
- Erikoistuotteet** :
  - tämä on ilmainen tuote.
  - tämä on maksullinen tuote.



#### Tuotevaihtoehdot





- Yksittäinen tuote (standalone-tuote)**: vain yksi lisäys mahdollista tilausta kohti (esim. lahjoitus, pääsylippu).
- Tuote vaihteluineen** :
  - Älä tarkista `Standalone`.
  - Tarkista `Tuotteessa on lieviä vaihteluita (ei varastoeroja)`.
  - Lisää :
    - Nimi** (esim. *Koko*),
    - Arvot** (esim. S, M, L, XL),
    - Hintaerot** tarvittaessa (esim.: `+2 USD` XL:lle).



![product-details](assets/fr/029.webp)



## Varastojen hallinnointi



### Lisäasetukset tuotetta luotaessa (varasto, toimitus, liput jne.)



#### Tuote, jonka varastotilanne on rajallinen



Jos tuotetta ei ole saatavana rajoittamattomia määriä, tarkista `Tuotetta on rajoitetusti varastossa`. Tämä aktivoi jäljellä olevien määrien automaattisen seurannan. Kun tämä ruutu on valittuna, näkyviin tulee kenttä, jossa ilmoitetaan **saatavilla oleva varasto**.



Järjestelmä hallinnoi :





- Varattu varasto** → korissa olevat tuotteet, joita ei ole vielä maksettu
- Myyty varasto** → jo ostetut tuotteet



**Korin varausaika**: Kun asiakas lisää tuotteen koriinsa, se "varataan" rajoitetuksi ajaksi. Voit muuttaa tätä aikaa osoitteessa: `Admin > Config > Korin varaus` (arvo minuutteina)



#### Toimitettava tuote?



Tarkista `Tuotteessa on fyysinen osa, joka toimitetaan asiakkaan Address:een`. Tämä on hyödyllinen kaikille fyysisesti lähetettäville tuotteille (kirjat, t-paidat jne.)



#### Muut vaihtoehdot





- Lippu**: rasti, jos tuote on tapahtuman lippu
- Varaus**: tarkista, onko kyseessä varausaika (esim. istunto, tapaaminen)



![product-options](assets/fr/030.webp)



### Toiminta-asetukset (alhaalla)



Tässä osassa määritellään, **missä** ja **miten** tuotetta voi tarkastella ja ostaa:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Tarkista vain ne kanavat, joita haluat käyttää.



## CMS-sivujen ja widgettien luominen ja mukauttaminen



### Pakolliset CMS-sivut



Siirry kohtaan `Admin > Merch > CMS`. Näet luettelon olemassa olevista sivuista ja voit lisätä uusia sivuja valitsemalla **Add CMS page**.



CMS-sivut ovat tärkeitä :





- Informoi kävijöitäsi (esim. käyttöehdot)
- Noudattaa lakia (esim. tietosuojakäytäntö)
- Selitä tietyt myymälän ominaisuudet (esim. IP-keräys, 0 % alv)



Voit lisätä muita sivuja tarpeen mukaan:





- Tietoa meistä / Keitä me olemme
- Tue meitä / Lahjoitukset
- FAQ
- Ota yhteyttä
- jne.



**Vinkki: Klikkaa kutakin linkkiä tai kuvaketta muuttaaksesi kunkin sivun **sisältöä**, **nimikettä** tai **seonäkyvyyttä**.



### Ulkoasu ja grafiikka Elements



Siirry osoitteeseen : `Admin > Merch > Layout`. Voit muokata sivustosi visuaalista Elements:ää:



![product-options](assets/fr/032.webp)



#### Yläpalkki





- Muokkaa tai poista linkkejä (EX: KOTISIVU, MEISTÄ,...)
- Navigointi sivuston keskeisten osioiden välillä



#### Navbar (päänavigointipalkki)





- Läsnä harmaalla alueella yläpalkin alapuolella
- Sisältää nopean pääsyn : `Config`, `Maksuasetukset`, `Transaktio`, `Solmujen hallinta`, `Widgetit`, jne.
- Vain johtajat



#### Alatunniste





- Muokattavissa kohdasta `Admin > Merch > Layout`
- Sisältää: yhteystiedot, hyödyllisiä linkkejä, oikeudellisia ilmoituksia...



#### Mukauta visuaalista ilmettä



Mene osoitteeseen: `Admin > Merch > Kuvat`



Voit :





- Vaihda **päälogo**
- Muokkaa tai lisää ulkoasua **kuvat**



#### Sivuston kuvaus



Se on myös muokattavissa kohdassa `Kuvat`, ja sen avulla voit näyttää **yhteenvedon tai iskulauseen** otsikossa tai alatunnisteessa teemasta riippuen.



**Huomautus:** Näin voit mukauttaa ulkoasun brändisi identiteetin mukaan (koulutus-, kaupallinen tai yhteisöllinen).



### Widgettien integroiminen CMS-sivuihin



Widgetit** rikastuttavat CMS-sivuja dynaamisella tai visuaalisella Elements:lla.



#### Widgetin luominen



Mene osoitteeseen: `Admin > Widgets`



Esimerkkejä käytettävissä olevista widgeteistä:





- Haasteet**: haasteet tai tehtävät
- Tunnisteet**: luokat tai avainsanat
- Sliders**: kuvakarusellit
- Tekniset tiedot** : Tekniset tiedot taulukot
- Lomakkeet**: lomakkeet (yhteydenotto, palaute jne.)
- Lähtölaskenta**: ajastimet
- Galleriat**: Kuvagalleriat
- Pistetaulukot**: käyttäjien sijoitukset



![widgets](assets/fr/033.webp)



#### Integrointi CMS-sivuihin



Käytä CMS-sivujesi sisällössä **lyhytkoodeja**:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Tämänhetkiset parametrit** :





- `slug`: widgetin yksilöllinen tunniste
- `display=img-1`: tuotekohtainen kuva
- `width`, `height`, `fit`: kuvan mitat ja tyyli
- autoplay=3000`: aika ms kahden dian välillä



**Hyötyjä** :





- Helppo lisätä (kopioi ja liitä)
- Dynaaminen: kaikki widgetin muutokset heijastuvat automaattisesti
- Kehittäjää ei tarvita



## Tilausten hallinta ja raportointi



### Tilauksen seuranta



Voit tarkastella ja hallita aiempia tilauksia osoitteessa: tilaukset"



Täältä löydät **täydellisen luettelon sivustollasi tehdyistä tilauksista**.



![orders](assets/fr/034.webp)



#### Visualisointi ja haku



Interface:n avulla voit etsiä ja suodattaa tilauksia useiden kriteerien mukaan:





- tilausnumero: tilausnumero
- tuotenimi: tuotteen tunniste tai nimi
- payment Mean": käytetty maksutapa (kortti, krypto jne.)
- `Email`: asiakkaan sähköpostiosoite



Nämä suodattimet helpottavat nopeita hakuja ja kohdennettua hallintaa.



#### Kunkin tilauksen yksityiskohdat



Klikkaamalla tilausta pääset käsiksi täydelliseen tiedostoon, joka sisältää :





- Tilatut tuotteet
- Asiakastiedot
- Toimitus Address (tarvittaessa)
- Tilaukseen liittyvät muistiinpanot



#### Mahdolliset toimenpiteet tilauksen osalta



Voit :





- Vahvista tilaus (jos se on vireillä)
- Peruuttaa tilaus (ongelman tai asiakkaan pyynnöstä)
- Lisää **merkinnät** (sisäistä organisointia varten)
- Konsultoi / lisää **sisäisiä huomautuksia**



**Huomautus:** Tämä kohta on olennaisen tärkeä hyvän logistiikan ja asiakassuhteiden kannalta.



### Raportointi ja vienti



Myynti- ja maksutilastojen käyttö :


järjestelmänvalvoja > Asetukset > Raportointi



![reporting](assets/fr/035.webp)



Täältä löydät yleiskatsauksen liiketoiminnastasi **kuukausi- ja vuosiraporttien** muodossa.



#### Raportin sisältö



Kertomukset on jaettu osiin:





- Tilauksen tiedot**: tilausten lukumäärä, tila (vahvistettu, peruutettu, vireillä), kehitys
- Tuotetiedot**: myydyt tuotteet, määrät, suositut tuotteet
- Maksutiedot**: kerätyt määrät, erittely maksutavan mukaan



#### Tietojen vienti



Jokaisessa osiossa on **Export CSV** -painike, jonka avulla voit :





- Lataa tiedot CSV-muodossa
- Avaa ne Excelissä, Google Sheetsissä jne.
- Arkistointi hallinnollista tai kirjanpitokäyttöä varten
- Käytä niitä sisäisiin raportteihin



**Huomautus:** ihanteellinen suorituskyvyn seurantaan, kirjanpitoon ja esityksiin.



## Nostr Messaging -konfiguraatio (valinnainen)



![nostr-config](assets/fr/036.webp)



Alusta tukee **Nostr**-protokollaa tiettyjä kehittyneitä toimintoja varten:





- Hajautetut ilmoitukset
- Kirjaudu sisään ilman salasanaa
- Interface kevyt hallinto



### Nostrin yksityisen avaimen luominen ja lisääminen



Siirry osoitteeseen :


admin > Solmujen hallinta > Nostr





- Napsauta **Luo nsec**, jos sinulla ei ole sellaista.
- Järjestelmä voi generate sen automaattisesti.
- Vaihtoehtoisesti voit käyttää olemassa olevaa avainta (esim. Damus- tai Amethyst-avainta).



Seuraava:





- Kopioi `nsec`-avain
- Lisää se tiedostoon `.env.local` (tai `.env`): ```env NOSTR_PRIVATE_KEY=YourNsecIciKey



### Nostrin avulla aktivoidut ominaisuudet



Kun se on määritetty, käytettävissä on useita toimintoja:



**ilmoitukset Nostrin kautta**





- Lähetä hälytyksiä tilauksista, maksuista tai järjestelmän tapahtumista
- Järjestelmänvalvojille tai käyttäjille



**Interface kevyt hallinto**





- Pääsy Nostr-asiakasohjelman kautta
- Mahdollistaa nopean, mobiiliystävällisen hallinnan



**Yhteys ilman salasanaa**





- Kirjaudu sisään suojatun linkin kautta (lähetetään Nostrin kautta)
- Suurempi käyttäjäturvallisuus ja sujuvuus



## Suunnittelu ja teeman muokkaus



Jos haluat mukauttaa myymälän ulkoasun graafiseen työjärjestykseesi, siirry osoitteeseen: aihe: `Admin > Merch > Teema`



Täältä löydät kaikki vaihtoehdot, joilla voit **luoda** ja **määrittää** mukautetun teeman.



### Teeman luominen



![theme](assets/fr/037.webp)



Kun luot tai muokkaat teemaa, voit määrittää :





- Värit**: painikkeille, taustoille, tekstille, linkeille jne.
- Kirjasimet**: valikoima kirjasimia otsikoille, kappaleille ja valikoille
- Graafiset tyylit**: rajaukset, marginaalit, välit, lohkomuodot



### Mukautettavat osiot



Sivuston jokainen osa voidaan säätää itsenäisesti:





- Otsikko**: ylänavigointipalkki
- Runko**: pääsisältö
- Alatunniste** : sivun alareuna



**Huomaa:** Tämä tarkkuus takaa sivuston visuaalisen ilmeen ja brändisi identiteetin yhdenmukaisuuden.



### Teeman aktivointi



Kun teema on määritetty :





- Klikkaa **Tallenna**
- Aktivoi se myymälän **pääteemaksi**



**Huomaa:** Aktiivinen teema on se, joka näkyy kävijöille.



## Sähköpostimallien määrittäminen



Alustan avulla voit muokata käyttäjille automaattisesti lähetettäviä sähköpostiviestejä. Siirry osoitteeseen: asetukset > Mallit`: `Admin > Asetukset > Mallit`



![emails-templates](assets/fr/038.webp)



### Mallien luominen / muokkaaminen



Jokaisessa sähköpostiviestissä (tilausvahvistus, unohtunut salasana jne.) on :





- Aihe**: sähköpostin aihe (esim. "Tilauksesi on vahvistettu")
- HTML-runko**: Sähköpostissa näkyvä HTML-sisältö



**Huomaa:** voit lisätä tekstiä, kuvia, linkkejä jne. tarpeen mukaan.



### Dynaamisten muuttujien käyttö



Jos haluat tehdä sähköposteista dynaamisia, lisää muuttujia kuten :





- `{Tilausnumero}}` : korvataan todellisella tilausnumerolla
- `{invoiceLink}}}` : linkki Invoice:een
- `{websiteLink}}`: Verkkosivustosi URL-osoite



**Huomaa:** Nämä tunnisteet korvataan automaattisesti lähetettäessä.



### Edistyneet vinkit





- Luo sähköpostiviestejä, jotka ovat **responsiivisia**, jotta niitä on helppo lukea mobiililaitteilla
- Lisää **toimintopainikkeita** (maksu, lataus, tilauksen seuranta)
- Testaa sähköpostiviestejäsi lähettämällä ne itsellesi ennen julkaisemista



## Tiettyjen tunnisteiden ja widgettien määrittäminen



### Tagien hallinta



Tunnisteiden avulla voit jäsentää ja rikastuttaa sisältöäsi. Niiden käyttäminen: `Admin > Widgets > Tag`



![tags-config](assets/fr/039.webp)



### Tunnisteen luominen



Täytä seuraavat kentät:





- Tag Name**: tagin nimi näytetään
- Slug**: yksilöllinen tunniste (ei välilyöntejä tai aksentteja)
- Tag Family**: ryhmittelee tagit kategorioiden mukaan



![targsconfig](assets/fr/040.webp)



#### Saatavilla olevat perheet :





- creators`: tekijät tai tuottajat
- vähittäiskauppiaat: myyjät tai myyntipisteet
- `Temporal`: ajanjaksot tai päivämäärät
- tapahtumat: liitännäistapahtumat



### Valinnaiset kentät



Näitä kenttiä voidaan käyttää tunnisteen rikastamiseen ikään kuin se olisi sisältösivu:





- Otsikko
- Alaotsikko
- Lyhyt** sisältö
- Koko sisältö** (ranskaksi)
- CTA:t** (toimintopainikkeet)



### Tunnisteiden käyttäminen



Tunnisteet voivat olla :





- Tuotteille kohdennettu
- Integroitu CMS-sivuihin tunnisteella: [Tag=slug?display=var-1]



## Ladattavien tiedostojen konfigurointi



Voit tarjota asiakkaillesi ladattavia asiakirjoja: `Admin > Merch > Tiedostot`



### Tiedoston lisääminen



1. Napsauta **Uusi tiedosto**


2. Ilmoita :




   - Tiedoston nimi** (esim. *Asennusopas*)
   - Ladattava tiedosto** (PDF, kuva, Word...)



**Huomautus:** Kun se on lisätty, alusta luo automaattisesti **pysyvän linkin**.



### Linkin käyttäminen



Tämä linkki voidaan sitten lisätä :





- CMS**-sivu (tekstilinkkinä tai painikkeena)
- **sähköpostiohjelma** (mallin kautta)
- **tuoteseloste** (esim. käyttöohjeen lataus)



Se on ihanteellinen *käyttäjän käsikirjojen, teknisten oppaiden, tuoteselosteiden...* tarjoamiseen ilman ulkoista hostingia.



## Nostr-bot



Alusta tarjoaa kehittyneen integraation **Nostr**-protokollaan automaattisen botin kautta.



Siirry osoitteeseen : node Management > Nostr



### Tärkeimmät ominaisuudet



#### Releiden hallinta





- Lisää tai poista botin käyttämiä **releitä**
- Optimoi lähetettyjen viestien **laajuus** ja **luotettavuus**



#### Automaattinen esittelyviesti





- Aktivoi automaattinen viesti **ensimmäisen käyttäjän vuorovaikutuksen yhteydessä**
- Ihanteellinen :
  - Palvelun esittely
  - Lähetä hyödyllinen linkki (esim. UKK, yhteystiedot, tilaus)



#### `npub-julkaisun sertifiointi





- Lisää **logo** ja **julkinen nimi**
- Linkki **varmistettuun verkkotunnukseen**
- Parantaa Nostr-identiteettisi uskottavuutta ja tunnettuutta



### Nostr-botin käyttötapaukset





- **Tilausvahvistusten** lähettäminen sinulle
- Automaattinen reagointi **tapahtumiin (esim. uusi tilaus)**
- Luodaan **hajautettu asiakasvuorovaikutus**



## Käännösmerkintöjen ylikuormitus



be-BOP on monikielinen (FR, EN, ES...), mutta voit mukauttaa käännökset tarpeisiisi.



Voit tehdä tämän osoitteessa: asetukset > Kieli



### Lataaminen ja muokkaaminen



Käännöstiedostot ovat JSON-muodossa. Voit :





- Lataa** kielitiedostot
- Olemassa olevien tekstien muuttaminen**
- Lisää** omia käännöksiäsi



Linkki alkuperäisiin tiedostoihin :


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Esimerkki:** korvaa `Add to cart` sanoilla `Ajouter au panier` tai `Acheter`.



## Tiimityö ja myyntipiste (POS)



### Käyttäjien ja käyttöoikeuksien hallinta



#### Roolien luominen



Mene osoitteeseen: asetukset > Asetukset > ARM



Klikkaa **Luo rooli** luodaksesi roolin (esim. `Super Admin`, `POS`, `Ticket checker`).



Jokainen rooli sisältää :





- kirjoitusoikeus**: kirjoitusoikeus
- lukuoikeus**: lukuoikeus
- kielletty pääsy**: jaksot interdites



#### Käyttäjän luominen



Lisää samassa valikossa `Admin > Asetukset > ARM` käyttäjä, jolla on :





- kirjaudu sisään
- alias
- sähköpostin palautus
- (valinnainen) `recovery npub` Nostrin kautta tapahtuvaa yhteyttä varten



Määritä aiemmin määritelty rooli.



![pos-users](assets/fr/045.webp)



Vain lukuoikeudet** -käyttäjät näkevät valikot *kirjaimin* eivätkä voi muokata sisältöä.



## Myyntipisteen (POS) konfigurointi



### POS-roolin määrittäminen



Jos haluat antaa käyttäjälle pääsyn kassakoneeseen, määritä rooli `Myyntipiste (POS)` in: `Admin > Config > ARM`



Hän voi muodostaa yhteyden suojatun URL-osoitteen kautta: `/pos` tai `/pos/touch` kautta



### POS-kohtaiset ominaisuudet



Be-BOP tarjoaa Interface:n, joka on tarkoitettu fyysiseen myyntiin (myymälä, tapahtuma jne.).



#### Nopea lisäys aliaksen kautta



`/cart`-kentässä voit lisätä tuotteen:





- Skannaamalla **viivakoodi** (ISBN, EAN13)
- Syöttämällä **tuotteen alias** manuaalisesti



**Huomaa:** tuote lisätään automaattisesti ostoskoriin.



#### Maksuvälineet



POS tukee :





- Laji
- Luottokortti
- Lightning Network (salaus)
- Muut kokoonpanon mukaan



Käytettävissä on kaksi edistynyttä vaihtoehtoa:





- ALV-vapautus** : sovelletaan perusteluihin (kansalaisjärjestöt, ulkomaalaiset...)
- Lahja-alennus**: poikkeuksellinen alennus, johon on pakollinen huomautus



#### Asiakaspuolen näyttö



URL-osoite `/pos/session` on tarkoitettu **toisen näytön** (HDMI, tabletti...) käyttöön:



Juliste:





- Käynnissä olevat tuotteet
- Kokonaismäärä
- Maksutapa
- Sovelletut alennukset



**Huomaa:** Asiakas seuraa tilausta suorana lähetyksenä, kun taas myyjä kirjaa sen `/pos`-tietoihin.



### POS-yhteenveto



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Kiitos, että seuraat tätä ohjetta huolellisesti.