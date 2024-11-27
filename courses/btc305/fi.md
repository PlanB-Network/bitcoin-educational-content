---
name: Bitcoin ja BTCPay Server
goal: Asenna BTCPay Server yrityksellesi
objectives:
  - Ymmärrä, mikä btcpayserver on.
  - Isännöi ja määritä BTCPay Server itse.
  - Käytä btcpayserveria päivittäisessä liiketoiminnassasi.
---

# Bitcoin ja BTCPay Server

Tämä on johdantokurssi BTCPay Serverin käyttöön, jonka ovat kirjoittaneet Alekos ja Bas, ja joka on mukautettu Plan ₿-kurssimuotoon melontwistin ja asi0:n toimesta.

KESKENERÄINEN TARINA

"Tämä on valheita, luottamukseni teihin on murtunut, teen teidät tarpeettomiksi".

Tuottanut BTCPay Server Foundation

+++

# Johdanto

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Kriittinen suosio kirjoittajan Bitcoin ja BTCPay Server -teokselle

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Aloitetaan siitä, mikä BTCPay Server on ja mistä se sai alkunsa. Arvostamme läpinäkyvyyttä ja tiettyjä standardeja luottamuksen muodostamiseksi Bitcoin-alueella.
Eräs projekti alalla rikkoi nämä arvot. BTCPay Serverin pääkehittäjä, Nicolas Dorier, otti tämän henkilökohtaisesti ja lupasi tehdä heidät tarpeettomiksi. Tässä me nyt olemme monta vuotta myöhemmin ja työskentelemme kohti tätä tulevaisuutta, täysin avoimen lähdekoodin parissa, joka päivä.

> Tämä on valheita, luottamukseni teihin on murtunut, teen teidät tarpeettomiksi.
> Nicolas Dorier

Nicolaksen sanojen jälkeen oli aika ryhtyä rakentamaan. Paljon työtä on tehty sen eteen, mitä nyt kutsutaan BTCPay Serveriksi. Yhä useammat ihmiset halusivat auttaa tässä työssä. Tunnetuimpia ovat r0ckstardev, MrKukks, Pavlenex ja ensimmäinen kauppias, joka käytti ohjelmistoa, astupidmoose.

Mitä avoin lähdekoodi tarkoittaa, ja mitä sellaisen projektin tekemiseen kuuluu?

FOSS tarkoittaa vapaata ja avoimen lähdekoodin ohjelmistoa. Ensimmäinen viittaa ehtoihin, jotka sallivat kenen tahansa kopioida, muokata ja jopa levittää versioita (jopa voittoa tavoitellen) ohjelmistosta. Jälkimmäinen viittaa lähdekoodin avoimeen jakamiseen, kannustaen yleisöä osallistumaan ja parantamaan sitä.
Tämä tuo mukanaan kokeneita käyttäjiä, jotka ovat innokkaita osallistumaan ohjelmistoon, josta he jo saavat arvoa, osoittaen ajan myötä voittavansa omistusoikeudellisen ohjelmiston käyttöönotossa. Se on linjassa Bitcoinin eetoksen kanssa, että "tiedon kuuluu olla vapaa". Se tuo yhteen intohimoisia ihmisiä, jotka muodostavat yhteisön ja on yksinkertaisesti hauskempaa. Kuten Bitcoin, FOSS on väistämätön.

### Ennen kuin aloitamme

Tämä kurssi koostuu useista osista. Monet niistä käsitellään luokkahuoneopettajasi toimesta, saat käyttöösi DEMO-ympäristöt, isännöidyn palvelimen itsellesi ja mahdollisesti verkkotunnuksen. Jos suoritat tämän kurssin itsenäisesti, ole tietoinen siitä, että DEMO-ympäristöt eivät ole käytettävissäsi.
HUOM. Jos seuraat tätä kurssia luokkahuoneessa, palvelinten nimet saattavat vaihdella luokkahuoneen asetusten mukaan. Palvelinten nimissä saattaa olla eroja tämän vuoksi.

### Kurssin rakenne

Jokaisella luvulla on tavoitteet ja tiedon arvioinnit. Tällä kurssilla käymme läpi nämä ja jokaisen oppituntikokonaisuuden (eli luvun) päätteeksi on yhteenveto avainominaisuuksista. Esitykset on varustettu kuvituksilla visuaalisen palautteen tarjoamiseksi ja keskeisten käsitteiden vahvistamiseksi visuaalisesti. Tavoitteet asetetaan kunkin oppituntikokonaisuuden alussa. Nämä tavoitteet menevät pelkän tarkistuslistan yli. Ne tarjoavat sinulle oppaan uuden taitosetin pariin. Tiedon arvioinnit ovat asteittain haastavampia BTCPay Serverin asetusten suhteen.

### Mitä opiskelijat saavat kurssilla?

BTCPay Server -kurssilla opiskelija voi ymmärtää Bitcoinin perusperiaatteet, sekä tekniset että ei-tekniset. Laaja koulutus Bitcoinin käyttöön BTCPay Serverin kautta mahdollistaa opiskelijoiden oman Bitcoin-infrastruktuurin operoinnin.

### Tärkeät verkkosivustot tai yhteydenottomahdollisuudet

BTCPay Server Foundation, joka mahdollisti Alekosin ja Basin tämän kurssin kirjoittamisen, sijaitsee Tokiossa, Japanissa. BTCPay Server -säätiöön voi ottaa yhteyttä listatun verkkosivuston kautta;

- https://foundation.btcpayserver.org
- liity virallisiin chat-kanaviin: https://chat.btcpayserver.org

## Johdanto Bitcoiniin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Bitcoinin ymmärtäminen luokkahuoneharjoituksen kautta

Tämä on luokkahuoneharjoitus, joten jos otat tämän kurssin itse, et voi suorittaa sitä, mutta voit silti käydä läpi tämän harjoituksen. Tämän tehtävän suorittamiseen vaadittava henkilömäärä on 9–11.

Harjoitus alkaa katsomalla johdanto "Miten Bitcoin ja lohkoketju toimivat" BBC:ltä.

![how bitcoin and the blockchain works](https://youtu.be/mhE_vvwAiRc)

Tähän harjoitukseen tarvitaan vähintään yhdeksän henkilön osallistuminen. Tämän harjoituksen tarkoituksena on fyysisesti saada käsitys siitä, miten Bitcoin toimii. Toimimalla kunkin roolin mukaisesti verkossa, saat interaktiivisen ja leikkisän tavan oppia. Tämä harjoitus ei sisällä Lightning Networkia.

### Esimerkki; Vaatii 9 / 11 henkilöä

Roolit ovat:

- 1 Asiakas
- 1 Kauppias
- 7–9 Bitcoin-noodia

**Asetelma on seuraava:**

Asiakas ostaa tuotteen kaupasta Bitcoinilla.

**Skenaario 1 - Perinteinen pankkijärjestelmä**

- Asetelma:
  - Katso kaaviot/selitykset liitetyssä Figjamissa - [Toimintakaavio](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Hanki kolme opiskelijavapaaehtoista toimimaan Asiakkaan (Alice), Kauppiaan (Bob) ja Pankin rooleissa.
- Näyttele tapahtumien kulku:
  - Asiakas- selaa kauppaa verkossa ja löytää $25 maksavan tuotteen, jonka haluaa, ja ilmoittaa Kauppiaalle haluavansa ostaa
  - Kauppias- pyytää maksua.
  - Asiakas- lähettää korttitiedot Kauppiaalle
  - Kauppias- välittää tiedot Pankille (identifioi sekä omat että asiakkaan tiedot/informaation) pyytäen maksua
  - Pankki kerää tietoja Asiakkaasta ja Kauppiaasta (Alice ja Bob) ja tarkistaa, että asiakkaan saldo riittää.
  - Vähentää \$25 Alicen tililtä, lisää \$24 Bobin tilille, ottaa \$1 palvelumaksun
  - Kauppias saa peukalon ylös Pankilta ja toimittaa tuotteen asiakkaalle.
- Kommentit:
  - Bobin ja Alicen on oltava suhteessa pankkiin.
  - Pankki kerää tunnistetietoja sekä Bobista että Alicesta.
  - Pankki ottaa osuuden.
  - Pankkiin on luotettava kummankin osapuolen rahojen säilyttäjänä koko ajan.

**Skenaario 2 - Bitcoin-järjestelmä**

- Asetelma:
  - Katso kaaviot/selitykset liitetyssä Figjamissa - [Toimintakaavio](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Korvaa Pankki yhdeksällä opiskelijalla, jotka toimivat Tietokoneen (Bitcoin-solmut/Louhijat) roolissa verkossa pankin korvaamiseksi. - Jokaisella yhdeksästä Tietokoneesta on täydellinen historiallinen kirjaus kaikista aiemmista tehdyistä transaktioista (näin ollen tarkat saldot ilman väärennöksiä), sekä joukko sääntöjä:
  - Varmista, että transaktio on asianmukaisesti allekirjoitettu (avain sopii lukkoon)
  - Lähetä ja vastaanota kelvollisia transaktioita verkon vertaisilta, hylkää kelvottomat (mukaan lukien kaikki, jotka yrittävät käyttää samoja varoja kahdesti)
- Päivitä/Lisää kirjauksia säännöllisesti uusilla transaktioilla, jotka on vastaanotettu "satunnaiselta" tietokoneelta, edellyttäen, että kaikki sisällöt ovat kelvollisia (huom: jätämme nyt huomiotta Proof of Work -komponentin tässä yksinkertaisuuden vuoksi), muutoin hylkää nämä ja jatka kuten ennen seuraavaan "satunnaiseen" tietokoneen päivitykseen
  - Oikea määrä palkittiin, jos sisällöt olivat kelvollisia.
- Näyttele tapahtumien sarja:
  - Asiakas- selaa kauppaa verkossa ja löytää tuotteen, jonka hinta on 25 dollaria ja jonka hän haluaa ostaa, ja ilmoittaa Kauppiaalle haluavansa ostaa
  - Kauppias- pyytää maksua lähettämällä asiakkaalle laskun/osoitteen lompakostaan.
  - Asiakas- rakentaa transaktion (lähettää 25 dollarin arvosta BTC:tä Kauppiaan antamaan osoitteeseen) ja lähettää sen Bitcoin-verkkoon.
- Tietokoneet- vastaanottavat transaktion ja varmistavat:
  - Lähettävästä osoitteesta löytyy vähintään 25 dollarin arvosta BTC:tä
  - Transaktio on asianmukaisesti allekirjoitettu (“avattu” asiakkaan toimesta)
  - Jos näin ei ole, transaktiota ei välitetä verkossa, ja jos on, se välitetään ja pidetään odottamassa.
  - Kauppiaat voivat tarkistaa, että transaktio on odottamassa ja vireillä.
- Yksi tietokone valitaan “satunnaisesti” ehdottamaan ehdotetun transaktion viimeistelyä lähettämällä “lohkon”, joka sisältää sen; jos se tarkistetaan, he saavat BTC-palkkion.
  - VAIHTOEHTOINEN/EDISTYNYT - tietokoneen satunnaisen valinnan sijaan simuloimaan louhintaa antamalla Tietokoneiden heittää noppaa, kunnes jokin ennalta määrätty tulos tapahtuu (esim. ensimmäinen, joka heittää kaksi kuutosta, valitaan)
  - Voidaan myös esittää, mitä tapahtuisi, jos kaksi Tietokonetta voittaisi suunnilleen samanaikaisesti, mikä johtaisi ketjun jakautumiseen.
  - Tietokoneet tarkistavat kelvollisuuden, päivittävät/lisäävät kirjauksia kirjanpitoihinsa, jos säännöt täyttyvät, ja lähettävät lohkon vertaisilleen.
  - Satunnaisesti valittu tietokone saa palkkion kelvollisen lohkon ehdottamisesta.
  - Kauppias tarkistaa, että transaktio on viimeistelty; näin ollen varat on vastaanotettu, ja tuote on lähetetty asiakkaalle.
- Kommentit:
  - Huomaa, että ennalta olemassa olevaa pankkisuhdetta ei tarvittu.
  - Kolmatta osapuolta ei tarvittu avuksi; korvattu koodilla/kannustimilla.
  - Kukaan ulkopuolinen ei kerää tietoja suorasta vaihdosta, ja osallistujien välillä on vaihdettava vain tarvittava määrä tietoja (esim. toimitusosoite).
  - Luottamusta ihmisten välillä ei vaadita (muuta kuin että Kauppias lähettää tuotteen), monin tavoin kuin käteisostossa.
  - Rahat omistavat suoraan yksilöt.
  - Bitcoin-kirjanpito esitetään dollareissa yksinkertaisuuden vuoksi, mutta todellisuudessa se on BTC.
  - Simuloimme yhden transaktion lähettämistä, mutta todellisuudessa verkossa on vireillä useita transaktioita, ja lohkot sisältävät kerralla tuhansia transaktioita. Solmut tarkistavat myös, ettei vireillä ole kaksinkertaisia maksutransaktioita (hylkäisin kaikki paitsi yhden, jos näin olisi).
- Huijausskenaariot:
  - Entä jos asiakkaalla ei olisikaan ollut 25 dollarin arvoista BTC:tä?
    - Hän ei olisi voinut luoda transaktiota, koska “avaaminen” ja “omistaminen” ovat sama asia, ja tietokoneet tarkistavat, että transaktio on asianmukaisesti allekirjoitettu; muutoin ne hylkäävät sen.
- Mitä jos satunnaisesti valittu tietokone yrittää "muuttaa kirjanpitoa"? - Lohko hylättäisiin, koska jokaisella muulla tietokoneella on täydellinen historia ja he huomaisivat muutoksen, mikä rikkoisi yhtä heidän säännöistään.
  - Satunnainen tietokone ei saisi palkkiota, eikä yhtään sen lohkon transaktiota vahvistettaisi.

## Tiedon arviointi

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### KA Luokkakeskustelu

Keskustele joistakin yksinkertaistuksista, jotka tehtiin luokkatehtävässä toisen skenaarion alla, ja kuvaile mitä todellinen Bitcoin-järjestelmä tekee yksityiskohtaisemmin.

### KA Sanaston kertaus

Määrittele seuraavat keskeiset termit, jotka esiteltiin edellisessä osiossa:

- Solmu
- Mempool
- Vaikeustavoite
- Lohko

**Keskustele ryhmänä joistakin lisätermien merkityksistä:**

Lohkoketju, Transaktio, Kahdenkertainen kulutus, Bysanttilaisten kenraalien ongelma, Louhinta, Proof of Work (PoW), Hahmofunktio, Lohkopalkkio, Lohkoketju, Pisin ketju, 51% hyökkäys, Lähtö, Lähdön lukitus, Muutos, Satoshit, Julkinen/Yksityinen avain, Osoite, Julkisen avaimen kryptografia, Digitaalinen allekirjoitus, Lompakko

# BTCPay Serverin esittely

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## BTCPay Serverin kirjautumisnäkymän ymmärtäminen

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Työskentely BTCPay Serverin kanssa

Tämän kurssiosan tavoitteena on ymmärtää yleisesti BTCPay Server -ohjelmiston toimintaa. Jaetussa ympäristössä suositellaan seuraamaan opettajan esittelyä ja seuraamaan mukana BTCPay Server -kurssikirjassa. Opit luomaan lompakon useilla eri menetelmillä. Esimerkkejä sisältävät Hot wallet -asetukset ja laitteistolompakot, jotka on yhdistetty BTCPay Server Vaultin kautta. Nämä tavoitteet tapahtuvat Demo-ympäristössä, joka näytetään ja johon pääsyn antaa kurssin opettaja.

Jos seuraat tätä kurssia itseksesi, voit löytää listan kolmannen osapuolen isännöijistä Demo-tarkoituksiin osoitteessa https://directory.btcpayserver.org/filter/hosts. Suosittelemme vahvasti välttämään näiden kolmannen osapuolen vaihtoehtojen käyttöä tuotantoympäristöinä, mutta ne palvelevat oikeita tarkoituksia Bitcoinin ja BTCPay Serverin käytön esittelyssä.

BTCPay Server -kivijalkakoulutettavana sinulla saattaa olla aiempaa kokemusta Bitcoin-solmun asettamisesta. Tämä kurssi puhuu erityisesti BTCPay Server -ohjelmistopinosta.

Monet BTCPay Serverin vaihtoehdoista ovat olemassa jossain muodossa muissa Bitcoin-lompakko-ohjelmistoissa.

### BTCPay Serverin kirjautumisnäyttö

Tervetuloa Demo-ympäristöön, sinua pyydetään 'Kirjautumaan sisään' tai 'Luomaan uusi tili'. Palvelimen ylläpitäjät voivat poistaa uusien tilien luomisen käytöstä turvallisuussyistä. BTCPay Serverin logoja ja painikkeiden värejä voidaan muuttaa, koska BTCPay Server on avoimen lähdekoodin ohjelmisto. Kolmas osapuoli voi White-label-ohjelmiston ja muuttaa koko ulkoasun.

![kuva](assets/en/0.webp)

### Tilin luomisen ikkuna

Tilin luominen BTCPay Serveriin vaatii kelvollisen sähköpostiosoitteen; esimerkki@email.com olisi kelvollinen merkkijono sähköpostille.

Salasanan on oltava vähintään 8 merkkiä pitkä, mukaan lukien kirjaimet, numerot ja merkit. Salasanan asettamisen jälkeen sinun on vahvistettava kirjoitettu salasana varmistaaksesi, että se on oikein verrattuna ensimmäiseen salasanakenttään kirjoitettuun.
Kun sekä Sähköposti- että Salasana-kentät on täytetty oikein, klikkaa "Luo tili" -painiketta. Tämä tallentaa sähköpostin ja salasanan opettajan BTCPay Server -instanssiin.
![image](assets/en/1.webp)

**!Huomio!**

Jos seuraat tätä kurssia omatoimisesti, tilin luominen olisi jotain, mitä saatat tehdä kolmannen osapuolen isännöinnissä; siksi mainitsemme jälleen, ettei näitä tule käyttää tuotantoympäristöinä vaan ainoastaan koulutustarkoituksiin.

### Tilin luominen BTCPay Serverin ylläpitäjän toimesta

BTCPay Server -instanssin ylläpitäjä voi myös luoda tilejä BTCPay Serverille. BTCPay Server -instanssin ylläpitäjä voi klikata "Palvelimen Asetukset" (1), klikata "Käyttäjät"-välilehteä (2) ja klikata "+ Lisää käyttäjä" -painiketta (3) Käyttäjät-välilehden oikeassa yläkulmassa. Tavoitteessa (4.3) opit lisää ylläpitäjän hallinnasta Tileihin liittyen.

![image](assets/en/2.webp)

Ylläpitäjänä tarvitset käyttäjän sähköpostiosoitteen ja asetat vakiosalasanan. On suositeltavaa, että ylläpitäjänä informoit käyttäjää, että heidän tulisi vaihtaa tämä salasana ennen tilin käyttöä turvallisuussyistä. Jos ylläpitäjä EI aseta Salasanaa ja SMTP on asetettu palvelimelle, käyttäjä saa sähköpostiin kutsulinkin, jolla he voivat luoda tilinsä ja asettaa salasanan itse.

### Esimerkki

Kun seuraat kurssia opettajan johdolla, seuraa opettajan antamaa linkkiä ja luo tilisi tarjotussa Demo-ympäristössä. Varmista, että sähköpostiosoitteesi ja salasanasi ovat turvallisesti tallennettu; tarvitset nämä kirjautumistiedot loppukurssin demo-tavoitteisiin.

Opettajasi on saattanut kerätä sähköpostiosoitteen etukäteen ja lähettänyt kutsulinkin ennen tätä harjoitusta. Jos näin on ohjeistettu, tarkista sähköpostisi.

Kun otat kurssin ilman opettajaa, luo tilisi käyttäen BTCPay Serverin demo-ympäristöä; mene osoitteeseen

https://mainnet.demo.btcpayserver.org/login.

Tätä tiliä tulisi käyttää ainoastaan demonstraatio-/koulutustarkoituksiin eikä koskaan liiketoimintaan.

### Taitojen Yhteenveto

Tässä osiossa opit seuraavat asiat:

- Miten luoda tili isännöidylle palvelimelle käyttöliittymän kautta.
- Miten palvelimen ylläpitäjä voi manuaalisesti lisätä käyttäjiä palvelimen asetuksissa.

### Tiedon arviointi

#### KA Konseptuaalinen katsaus

Anna syitä, miksi Demo-palvelimen käyttäminen tuotantotarkoituksiin on huono idea.

## Käyttäjätilin hallinta

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Tilinhallinta BTCPay Serverissä

Kun kaupan omistaja on luonut tilinsä, hän voi hallita sitä BTCPay Serverin käyttöliittymän vasemmassa alakulmassa. Tilinapin alla on useita korkeamman tason asetuksia.

- Tumma/Vaalea tila.
- Piilota arkaluonteiset tiedot -vaihtoehto.
- Hallitse tiliä.

![image](assets/en/3.webp)

### Tumma ja Vaalea tila

BTCPay Serverin käyttäjät voivat valita käyttöliittymän Tumman tai Vaalean version. Asiakkaalle näkyvät sivut eivät muutu. Ne käyttävät asiakkaan suosimia asetuksia tumman tai vaalean tilan suhteen.

### Piilota arkaluonteiset tiedot -vaihtoehto

Piilota arkaluonteiset tiedot -painike tuo nopean ja yksinkertaisen turvallisuustason. Kun sinun tarvitsee käyttää BTCPay Serveriäsi, mutta ympärilläsi saattaa olla ihmisiä kurkkimassa olkapääsi yli julkisessa tilassa, kytke päälle Piilota arkaluonteiset tiedot, ja kaikki arvot BTCPay Serverissä piilotetaan. Joku saattaa pystyä kurkkimaan olkapääsi yli, mutta ei enää näe käsittelemiäsi arvoja.

### Hallitse tiliä

Kun käyttäjätili on luotu, tässä on paikka hallita salasanoja, kaksivaiheista tunnistautumista tai API-avaimia.

### Hallinnoi tiliä - Tili

Voit halutessasi päivittää tilisi eri sähköpostiosoitteella. Varmistaaksesi sähköpostiosoitteesi oikeellisuuden, BTCPay Server mahdollistaa varmistussähköpostin lähettämisen. Klikkaa tallenna, jos käyttäjä asettaa uuden sähköpostiosoitteen ja vahvistaa varmistuksen toimineen. Käyttäjänimi pysyy samana kuin aiempi sähköposti.

Käyttäjä voi päättää poistaa koko tilinsä. Tämän voi tehdä klikkaamalla poista-painiketta Tilin-välilehdellä.

![kuva](assets/en/4.webp)

**!Huom!**

Sähköpostin vaihtamisen jälkeen tilin käyttäjänimi ei muutu. Aiemmin annettu sähköpostiosoite säilyy kirjautumisnimenä.

### Hallinnoi tiliä - Salasana

Opiskelija saattaa haluta vaihtaa salasanansa. Hän voi tehdä tämän menemällä Salasana-välilehdelle. Täällä hänen on kirjoitettava vanha salasanansa ja hän voi vaihtaa sen uuteen.

![kuva](assets/en/5.webp)

### Kaksivaiheinen tunnistautuminen (2fa)

Rajoittaaksesi varastetun salasanan seurauksia, voit käyttää kaksivaiheista tunnistautumista (2fa), suhteellisen uutta turvallisuusmenetelmää. Voit aktivoida kaksivaiheisen tunnistautumisen Hallinnoi tiliä -kohdasta ja kaksivaiheisen tunnistautumisen välilehdeltä. Sinun on suoritettava toinen vaihe kirjautumisen jälkeen käyttäjänimelläsi ja salasanallasi.

BTCPay Server mahdollistaa 2FA:n käyttöönoton kahdella tavalla, sovelluspohjainen 2FA (Authy, Google, Microsoft autentikaattorit) tai turvalaitteiden kautta (FIDO2 tai LNURL Auth).

### Kaksivaiheinen tunnistautuminen - Sovelluspohjainen

Mobiililaitteesi käyttöjärjestelmän (Android tai iOS) perusteella käyttäjät voivat valita seuraavista sovelluksista;

1. Lataa kaksivaiheinen autentikaattori;
   - Authy [Androidille](https://play.google.com/store/apps/details?id=com.authy.authy) tai [iOS:lle](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator [Androidille](https://play.google.com/store/apps/details?id=com.azure.authenticator) tai [iOS:lle](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator [Androidille](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) tai [iOS:lle](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Sovelluksen lataamisen ja asentamisen jälkeen.
   - Skannaa BTCPay Serverin tarjoama QR-koodi
   - Tai syötä BTCPay Serverin generoima avain manuaalisesti autentikaattorisovellukseesi.
3. Autentikaattorisovellus tarjoaa sinulle uniikin koodin. Syötä uniikki koodi BTCPay Serveriin varmistaaksesi asetuksen, ja klikkaa vahvista suorittaaksesi prosessin loppuun.

![kuva](assets/en/6.webp)

### Taitojen yhteenveto

Tässä osiossa opit seuraavat asiat:

- Tilinhallintavaihtoehdot ja erilaiset tavat hallita tiliä BTCPay Server -instanssissa.
- Miten asettaa sovelluspohjainen 2FA.

### Tiedon arviointi

#### KA Konseptuaalinen katsaus

Kuvaile, miten sovelluspohjainen 2FA auttaa turvaamaan tilisi

## Luo uusi kauppa

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Luo kauppasi velho

Kun uusi käyttäjä kirjautuu sisään BTCPay Serveriin, ympäristö on tyhjä ja tarvitsee ensimmäisen kaupan. BTCPay Serverin käyttöönotto-opas antaa käyttäjälle mahdollisuuden ’Luo kauppasi’ (1). Kauppaa voidaan pitää Kotina Bitcoin-tarpeillesi. Uusi BTCPay Server Node aloittaa Synkronoimalla Bitcoin-lohkoketjun (2). Riippuen siitä, millä infrastruktuurilla ajat BTCPay Serveria, tämä voi kestää muutamasta tunnista muutamaan päivään. Instanssin nykyinen versio näkyy BTCPay Serverin käyttöliittymän oikeassa alakulmassa. Tämä on hyödyllistä viitteenä vianmäärityksessä.
![kuva](assets/en/7.webp)

### Luo kauppasi -opas

Tämän kurssin seuraaminen alkaa hieman erilaiselta näytöltä kuin edellisellä sivulla. Koska ohjaajasi on valmistellut Demo-ympäristön, Bitcoin-lohkoketju on synkronoitu etukäteen, ja siksi et näe noden synkronointitilaa.

Käyttäjä voi päättää poistaa koko tilinsä. Tämä voidaan tehdä napsauttamalla poista-painiketta Tilivälilehdellä.

![kuva](assets/en/8.webp)

**!Huom!**

BTCPay Server -tilit voivat luoda rajattoman määrän kauppoja. Jokainen kauppa on lompakko tai ”koti”.

### Esimerkki

Aloita napsauttamalla "Luo kauppasi".

![kuva](assets/en/9.webp)

Tämä luo ensimmäisen Kotisi ja hallintapaneelin BTCPay serverin käyttöön.

(1) Napsautettuasi "Luo kauppasi", BTCPay Server vaatii sinua nimeämään kaupan; tämä voi olla mikä tahansa sinulle hyödyllinen.

![kuva](assets/en/10.webp)

(2) Seuraavaksi on asetettava oletuskaupan valuutta, joko fiat-valuutta tai Bitcoin / Sats -standardiin nimetty. Demoympäristössä asetamme sen USD:ksi.

![kuva](assets/en/11.webp)

(3) Viimeisenä parametrina kaupan asetuksissa, BTCPay Server vaatii sinua asettamaan "Suosituin hintalähde" vertaamaan Bitcoinin hintaa nykyiseen fiat-hintaan, jotta kauppasi näyttää oikean vaihtokurssin Bitcoinin ja kaupassa asetetun fiat-valuutan välillä. Pysymme oletuksessa Demoesimerkissä ja asetamme tämän Kraken-vaihtoon. BTCPay Server käyttää Krakenin API:a tarkistaakseen vaihtokurssit.

![kuva](assets/en/12.webp)

(4) Nyt kun nämä kaupan parametrit on asetettu, napsauta Luo-painiketta, ja BTCPay Server luo ensimmäisen kauppasi hallintapaneelin, jossa opas jatkuu.

![kuva](assets/en/13.webp)

Onnittelut, olet luonut ensimmäisen kauppasi, ja tämä päättää tämän harjoituksen.

![kuva](assets/en/14.webp)

### Taitojen Yhteenveto

Tässä osiossa opit:

- Kaupan luomisen ja oletusvaluutan määrittämisen yhdistettynä hintalähteen asetusten kanssa.
- Jokainen "Kauppa" on uusi koti erillään muista tämän BTCPay Server -asennuksen kaupoista.

# Johdanto Bitcoin-avainten Turvaamiseen

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Ymmärrys Bitcoin-avainten Luomisesta

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Mitä bitcoin-avainten luomiseen sisältyy?

Bitcoin-lompakot, kun ne luodaan, luovat niin kutsutun "siemenen". Viimeisessä tavoitteessa loit "siemenen", Sarja sanoja, jotka on luotu aiemmin, tunnetaan myös nimellä mnemoniset lauseet. Siementä käytetään johdattamaan yksittäisiä Bitcoin-avaimia ja käytetään Bitcoinin lähettämiseen tai vastaanottamiseen. Siemenlauseita ei koskaan tulisi jakaa kolmansien osapuolien tai luottamattomien vertaisten kanssa.
Siemenluonti suoritetaan teollisuusstandardin mukaisesti, joka tunnetaan nimellä "Hierarkkinen Deterministinen" (HD) kehys.
![kuva](assets/en/15.webp)

### Osoitteet

BTCPay Server on suunniteltu luomaan uusi Osoite. Tämä lievittää julkisen avaimen tai Osoitteen uudelleenkäytön ongelmaa. Saman Julkisen avaimen käyttäminen tekee koko maksuhistoriasi seuraamisen erittäin helpoksi. Avainten ajatteleminen kertakäyttöisinä kuponkeina parantaisi merkittävästi yksityisyyttäsi. Käytämme myös Bitcoin Osoitteita, älä sekoita näitä Julkisiin avaimiin.

Osoite johdetaan Julkisesta avaimesta "hashing-algoritmin" kautta. Useimmat lompakot ja transaktiot kuitenkin näyttävät Osoitteita näiden julkisten avainten sijaan. Osoitteet ovat yleensä lyhyempiä kuin julkiset avaimet ja alkavat yleensä `1`, `3`, tai `bc1`, kun taas julkiset avaimet alkavat `02`, `03`, tai `04`.

- Osoitteet, jotka alkavat `1.....`, ovat edelleen hyvin yleisiä osoitteita. Kuten luvussa Uuden kaupan luominen mainittiin, nämä ovat perintöosoitteita. Tämä osoitetyyppi on tarkoitettu P2PKH-transaktioille. P2Pkh käyttää Base58-koodausta, mikä tekee osoitteesta kirjainkoosta riippuvaisen. Sen rakenne perustuu julkiseen avaimen lisäksi yhteen tunnisteena toimivaan numeroon.

- Osoitteet, jotka alkavat `bc1...`, ovat hitaasti siirtymässä hyvin yleisiksi osoitteiksi. Näitä kutsutaan (natiiveiksi) SegWit Osoitteiksi. Nämä tarjoavat paremman maksurakenteen kuin muut mainitut Osoitteet. Natiivit SegWit Osoitteet käyttävät Bech32-koodausta ja sallivat vain pienet kirjaimet.

- Osoitteet, jotka alkavat `3...`, ovat yleisesti edelleen käytössä vaihtoalustoilla talletusosoitteina. Näitä osoitteita mainitaan luvussa Uuden kaupan luominen, käärittyinä tai sisäkkäisinä SegWit-osoitteina. Ne voivat kuitenkin toimia myös "Multisig Osoitteena". Kun niitä käytetään SegWit-osoitteena, transaktiomaksuissa on jälleen säästöjä, vaikkakin vähemmän kuin Natiivissa SegWitissä. P2SH Osoitteet käyttävät Base58-koodausta. Tämä tekee niistä kirjainkoosta riippuvaisia, kuten perintöosoite.

- Osoitteet, jotka alkavat `2...`, ovat Testnet-osoitteita. Ne on tarkoitettu vastaanottamaan testnet bitcoinia (tBTC). Sinun ei pitäisi koskaan sekoittaa näitä ja lähettää Bitcoineja näihin osoitteisiin. Kehitystarkoituksiin voit luoda testnet-lompakon. Verkossa on useita hanoja, joista saa testnet Bitcoinia. Älä koskaan osta Testnet Bitcoinia. Testnet Bitcoinia louhitaan. Tämä saattaa olla syy kehittäjälle käyttää Regtestiä sen sijaan. Tämä on kehittäjille tarkoitettu leikkikenttäympäristö, josta puuttuu tiettyjä verkkokomponentteja. Bitcoin on kuitenkin kehitystarkoituksiin erittäin hyödyllinen.

### Julkiset Avaimet

Julkisia avaimia käytetään käytännössä nykyään vähemmän. Ajan myötä bitcoinin käyttäjät ovat korvanneet ne Osoitteilla. Ne kuitenkin edelleen ovat olemassa ja niitä käytetään satunnaisesti. Julkiset avaimet ovat yleensä paljon pidempiä merkkijonoja kuin osoitteet. Kuten osoitteidenkin kohdalla, ne alkavat tietyllä tunnisteella.

- Ensinnäkin, `02...` ja `03...` ovat hyvin standardoituja julkisen avaimen tunnisteita, jotka on koodattu SEC-muodossa. Näitä voidaan käsitellä ja muuntaa osoitteiksi vastaanottoa varten, käyttää luomaan multi-sig osoitteita tai varmentamaan allekirjoituksen. Bitcoinin alkuaikojen transaktiot käyttivät julkisia avaimia osana P2PK-transaktioita.

- HD-lompakot käyttävät kuitenkin erilaista rakennetta. `xpub...`, `ypub...` tai `zpub...` kutsutaan laajennetuiksi julkisiksi avaimiksi, yleisemmin xpubiksi. Näitä avaimia käytetään johdettujen julkisten avainten luomiseen, koska ne ovat osa HD-lompakkoa. Koska xpubisi pitää kirjaa koko historiastasi, tarkoittaen menneitä ja tulevia transaktioita, älä jaa näitä luotettomien osapuolien kanssa.

### Taitoyhteenveto

Tässä osiossa opit seuraavat:

- Eroavaisuudet osoitteiden ja julkisen avaimen tietotyyppien välillä sekä osoitteiden käytön hyödyt julkisiin avaimiin verrattuna.

### Tietämyksen arviointi

Kuvaile tuoreiden osoitteiden käytön hyötyä jokaiselle transaktiolle verrattuna osoitteen uudelleenkäyttöön tai julkisen avaimen menetelmiin

## Avainten turvaaminen laitteistolompakolla

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Bitcoin-avainten säilyttäminen

Siemenlauseen luomisen jälkeen, 12 - 24 sanasta koostuva lista, joka tässä kirjassa on luotu, vaatii asianmukaiset varmuuskopiot ja turvatoimet, sillä nämä sanat ovat ainoa tapa palauttaa pääsy lompakkoon. HD-lompakoiden rakenne ja se, miten se deterministisesti luo osoitteita käyttäen tätä yhtä siementä, kaikki luomasi osoitteet varmuuskopioidaan käyttäen tätä yhtä mnemonic-sanojen listaa, joka edustaa siemen- tai palautusfraasia.

Pidä palautusfraasisi turvassa. Jos joku pääsee siihen käsiksi, erityisesti pahantahtoisesti, he voivat siirtää varojasi. Siemenen pitäminen turvassa ja muistaminen ovat toisilleen yhteisiä. Bitcoinin yksityisavainten säilyttämiseen on useita menetelmiä, joilla kullakin on etuja ja haittoja, joko turvallisuuden, yksityisyyden, mukavuuden tai fyysisten keinojen osalta. Yksityisavainten tärkeyden vuoksi bitcoinin käyttäjät yleensä säilyttävät ja pitävät näitä avaimia turvallisesti "omassa hallussaan" käyttämättä "huoltajapalveluita" kuten pankkeja. Käyttäjästä riippuen hänen on käytettävä joko kylmäsäilytysratkaisua tai kuumaa lompakkoa.

### Kuuman ja kylmän säilytyksen bitcoin-avaimet

Yleensä bitcoin-lompakot jaetaan Kuumaan Lompakkoon tai Kylmään Lompakkoon. Useimmat kompromissit liittyvät mukavuuteen, käytön helppouteen ja turvallisuusriskiin. Kukin näistä menetelmistä voidaan nähdä myös huoltajapalvelun ratkaisussa. Kuitenkin kompromissit tässä ovat enimmäkseen turvallisuuteen ja yksityisyyteen liittyviä ja menevät tämän kurssin soveltamisalan ulkopuolelle.

### Kuuma lompakko

Kuumat lompakot ovat kätevin tapa olla vuorovaikutuksessa Bitcoinin kanssa mobiilin, verkon tai työpöytäohjelmiston kautta. Lompakko on aina yhteydessä internetiin, mikä mahdollistaa käyttäjien lähettää tai vastaanottaa Bitcoinia. Tämä on kuitenkin myös sen heikkous, sillä lompakko, koska se on aina verkossa, on nyt alttiimpi hyökkäyksille hakkerien tai laitteeseesi kohdistuvan haittaohjelman toimesta. BTCPay Serverissä kuumat lompakot säilyttävät yksityiset avaimet instanssissa. Kuka tahansa, joka pääsee käsiksi BTCPay Serverin kauppaasi, voisi varastaa varoja tästä osoitteesta, jos on pahantahtoinen. Kun BTCPay Server toimii isännöidyssä ympäristössä, sinun tulisi aina ottaa tämä huomioon turvallisuusprofiilissasi ja mieluiten ei käyttää Kuuma-lompakkoa tällaisessa tapauksessa. Kun BTCPay Server on asennettu omalle laitteistolle, jonka olet turvannut ja johon luotat, riskiprofiili laskee merkittävästi, mutta se ei koskaan katoa!

### Kylmä lompakko

Ihmiset siirtävät Bitcoininsa kylmään lompakkoon, koska se voi eristää yksityiset avaimet internetistä. Internet-yhteyden poistaminen yhtälöstä vähentää haittaohjelmien, vakoiluohjelmien ja SIM-vaihtojen riskiä. Kylmäsäilytystä pidetään turvallisempana kuin kuumaa säilytystä turvallisuuden ja autonomian osalta, kunhan riittävät varotoimet otetaan käyttöön välttääkseen Bitcoinin yksityisavainten menettämisen. Kylmäsäilytys sopii parhaiten suurille Bitcoin-määrille, joita ei ole tarkoitus käyttää usein lompakon asetuksen monimutkaisuuden vuoksi.

On olemassa erilaisia menetelmiä, miten säilyttää Bitcoin-avaimia kylmäsäilytyksessä, paperilompakoista aivolompakoihin, laitteistolompakoihin tai, alusta alkaen, lompakkotiedostoon. Useimmat lompakot käyttävät BIP 39:ää siemenlauseen luomiseen. Kuitenkin Bitcoin-ydinohjelmistossa ei ole vielä päästy yksimielisyyteen sen käytöstä. Bitcoin Core -ohjelmisto luo edelleen Wallet.dat-tiedoston, jonka sinun on säilytettävä turvallisessa offline-sijainnissa.

### Taitojen yhteenveto

Tässä osiossa opit:

- Eroavaisuudet kuumien ja kylmien lompakoiden välillä toiminnallisuuden ja niiden kompromissien osalta.
- Mikä on lompakko?
- Mikä on ero kuumien ja kylmien lompakoiden välillä?

- Kuvaile, mitä tarkoitetaan "lompakon luomisella"?

## Käyttäen Bitcoin-avaimiasi

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### BTCPay Server -lompakko

BTCPay Server koostuu seuraavista vakio lompakko-ominaisuuksista:

- Tapahtumat
- Lähetä
- Vastaanota
- Uudelleenskannaus
- Vetomaksut
- Maksut
- PSBT
- Yleiset asetukset

### Tapahtumat

Ylläpitäjät voivat nähdä tietyn kaupan yhteydessä olevaan on-chain lompakkoon liittyvät sisään- ja ulostulevat tapahtumat tapahtumanäkymässä. Jokaisella tapahtumalla on ero saapuvien ja lähtevien välillä. Saapuvat ovat vihreitä ja lähtevät tapahtumat ovat punaisia. BTCPay Serverin tapahtumanäkymässä ylläpitäjät näkevät myös joukon vakioleimoja.

| Tapahtuman Tyyppi | Kuvaus                                                 |
| ----------------- | ------------------------------------------------------ |
| App               | Maksu vastaanotettiin sovelluksen luoman laskun kautta |
| invoice           | Maksu vastaanotettiin laskun kautta                    |
| payjoin           | Ei maksettu, laskun ajastin ei ole vielä päättynyt     |
| payjoin-exposed   | UTXO paljastettiin laskun payjoin-ehdotuksen kautta    |
| payment-request   | Maksu vastaanotettiin maksupyynnön kautta              |
| payout            | Maksu lähetettiin maksun tai hyvityksen kautta         |

### Miten Lähettää

BTCPay-palvelimen lähetystoiminto lähettää tapahtumia BTCPay-palvelimen on-chain lompakostasi. BTCPay Server mahdollistaa useita tapoja allekirjoittaa tapahtumasi varojen käyttämiseksi. Tapahtuman voi allekirjoittaa;

- Laitteistolompakko
- PSBT:tä tukevat lompakot
- HD yksityisavain tai palautus siemenet.
- Kuuma lompakko

#### Laitteistolompakko

BTCPay Server tukee sisäänrakennettua laitteistolompakkoa, joka mahdollistaa laitteistolompakkosi käytön BTCPay Vaultin kanssa ilman tietojen vuotamista kolmansien osapuolien sovelluksiin tai palvelimiin. Laitteistolompakon integraatio BTCPay Serveriin mahdollistaa laitteistolompakkosi tuonnin ja saapuvien varojen käytön yksinkertaisella vahvistuksella laitteellasi. Yksityisavaimet eivät koskaan poistu laitteesta, ja kaikki varat validoidaan täysnodiasi vasten, joten tietovuotoa ei tapahdu.

#### Allekirjoitus lompakolla, joka tukee PSBT:tä

PSBT (Partially Signed Bitcoin Transactions) on Bitcoin-tapahtumien vaihtoformaatti, joka vaatii vielä täydellisen allekirjoituksen. PSBT:tä tuetaan BTCPay Serverissä, ja sen voi allekirjoittaa yhteensopivilla laitteisto- ja ohjelmistolompakoilla.

Täysin allekirjoitetun Bitcoin-tapahtuman rakentaminen etenee seuraavasti:

- PSBT luodaan tietyillä syötteillä ja tulosteilla, mutta ilman allekirjoituksia
- Viedy PSBT voidaan tuoda lompakkoon, joka tukee tätä formaattia
- Tapahtuman tiedot voidaan tarkastella ja allekirjoittaa käyttäen lompakkoa
- Allekirjoitettu PSBT-tiedosto viedään lompakosta ja tuodaan BTCPay Serveriin
- BTCPay Server tuottaa lopullisen Bitcoin-tapahtuman
- Tarkistat tuloksen ja lähetät sen verkkoon

#### Allekirjoitus HD Yksityisavaimella tai mnemonic siemenellä

Jos olet luonut lompakon aiemmin käyttäen BTCPay Serveriä, voit käyttää varoja syöttämällä yksityisavaimen asianmukaiseen kenttään. Aseta asianmukainen "AccountKeyPath" lompakko> Asetukset; muuten et voi käyttää.

#### Allekirjoitus kuumalla lompakolla

Jos loit uuden lompakon kauppasi perustamisen yhteydessä ja otit sen käyttöön kuumana lompakkona, se käyttää automaattisesti palvelimella säilytettyä siementä allekirjoitukseen.

### RBF (Replace-By-Fee)

Replace-By-Fee (RBF) on Bitcoin-protokollan ominaisuus, joka mahdollistaa aiemmin lähetetyn siirron korvaamisen (kun se on vielä vahvistamaton). Tämä mahdollistaa lompakkosi siirtojäljen satunnaistamisen tai korvaamisen korkeammalla maksutaksalla, jotta siirto siirtyy korkeammalle vahvistusjonossa (louhinnan prioriteetissa). Tämä korvaa tehokkaasti alkuperäisen siirron, sillä korkeampi maksutaksa saa etusijan, ja kun se vahvistetaan, alkuperäinen siirto mitätöidään (ei kaksinkertaista kulutusta).
Paina "Lisäasetukset"-painiketta nähdäksesi RBF-vaihtoehdot;

![kuva](assets/en/16.webp)

- Satunnaista suuremman yksityisyyden vuoksi, mahdollistaa siirron automaattisen korvaamisen siirtojäljen satunnaistamiseksi.
- Kyllä, Merkitse siirto RBF:lle ja korvattavaksi nimenomaisesti (Ei korvata oletuksena, vain syötteen perusteella)
- Ei, Älä salli siirron korvaamista.

### Kolikoiden Valinta

Kolikoiden valinta on edistynyt yksityisyyttä parantava ominaisuus, joka mahdollistaa haluamiesi kolikoiden valitsemisen siirtoa tehdessä. Esimerkiksi maksaminen kolikoilla, jotka ovat tuoreita yhdistelmäsekoituksesta.

Kolikoiden valinta toimii natiivisti lompakon merkintäominaisuuden kanssa. Tämä mahdollistaa saapuvien varojen merkitsemisen sujuvampaan UTXO-hallintaan ja kulutukseen.

BTCpay Server tukee myös BIP-329:ää merkintöjen hallintaan. BIP-329 mahdollistaa merkintöjen asettamisen; jos siirrät lompakosta, joka tukee tätä tiettyä BIP:iä ja asetat merkintöjä, BTCPay Server tunnistaa nämä ja tuo ne sisään. Palvelimia siirrettäessä tämä tieto voidaan myös viedä ja tuoda uuteen ympäristöön.

### Miten Vastaanottaa

Kun BTCPay Serverissa painetaan vastaanota-painiketta, se luo käyttämättömän osoitteen, jota voidaan käyttää maksujen vastaanottamiseen. Ylläpitäjät voivat myös luoda uuden osoitteen luomalla uuden "Laskun".

BTCPay Server pyytää aina luomaan seuraavan käytettävissä olevan osoitteen välttääkseen osoitteen uudelleenkäytön. Kun klikattiin "Luo seuraava käytettävissä oleva BTC-osoite", BTCPay Server loi uuden osoitteen ja QR-koodin. Se mahdollistaa myös suoraan osoitteelle Merkinnän asettamisen paremman osoitteiden hallinnan vuoksi.

![kuva](assets/en/17.webp)

![kuva](assets/en/18.webp)

#### Uudelleenskannaus

Uudelleenskannausominaisuus perustuu Bitcoin Core 0.17.0:n "Scantxoutset"-toimintoon skannata nykyisen lohkoketjun tila (kutsutaan UTXO Setiksi) kolikoille, jotka kuuluvat määritettyyn johdannaisjärjestelmään. Lompakon uudelleenskannaus ratkaisee kaksi ongelmaa, joita BTCPay Serverin käyttäjät kohtaavat.

1. Gap limit -ongelma - Useimmat kolmannen osapuolen lompakot ovat kevytlompakoita, jotka jakavat solmun monen käyttäjän kesken. Kevyet ja täyden solmun varassa toimivat lompakot rajoittavat seurattavien saldoa vailla olevien osoitteiden määrää (tyypillisesti 20) lohkoketjussa suorituskykyongelmien estämiseksi. BTCPay Server luo uuden osoitteen jokaiselle laskulle. Edellä mainitun huomioon ottaen, kun BTCPay Server on luonut 20 peräkkäistä maksamatonta laskua, ulkoinen lompakko lopettaa siirtojen noutamisen olettaen, ettei uusia siirtoja ole tapahtunut. Ulkoinen lompakkosi ei näytä niitä, kun laskut maksetaan 21., 22. jne. Toisaalta sisäisesti BTCPay Serverin lompakko seuraa mitä tahansa luomaansa osoitetta paljon suuremmalla gap limitillä. Se ei ole riippuvainen kolmannesta osapuolesta ja voi aina näyttää oikean saldon.
2. Ratkaisu gap-limit ongelmaan - Jos [ulkoinen/olemassa oleva lompakko](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) mahdollistaa gap-limitin konfiguroinnin, helppo korjaus on sen kasvattaminen. Valitettavasti suurin osa lompakoista ei kuitenkaan salli tätä. Ainoat lompakot, jotka meidän tietoomme sallivat gap-limitin konfiguroinnin, ovat Electrum, Wasabi ja Sparrow Wallet. Valitettavasti todennäköisesti kohtaat ongelmia monien muiden lompakoiden kanssa. Parhaan käyttäjäkokemuksen ja yksityisyyden takaamiseksi harkitse ulkoisten lompakoiden hylkäämistä ja BTCPay Serverin sisäisen lompakon käyttöä.

#### BTCPay Server käyttää “mempoolfullrbf=1”

BTCPay Server käyttää “mempoolfullrbf=1”; olemme lisänneet tämän oletusarvona BTCPay Server -asetuksiisi. Olemme kuitenkin tehneet siitä myös fragmentin, jonka voit itse poistaa käytöstä. Ilman “mempoolfullrbf=1”, jos asiakas tekee kaksinkertaisen maksun transaktiolla, joka ei merkitse RBF:ää, kauppias saisi tiedon vasta vahvistuksen jälkeen.

Ylläpitäjä saattaa haluta poistaa tämän asetuksen käytöstä. Seuraavalla merkkijonolla voit muuttaa oletusasetusta.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### BTCPay Serverin lompakon asetukset

BTCPay Serverin sisällä olevat lompakon asetukset tarjoavat selkeän ja nopean yleiskatsauksen lompakkosi yleisistä asetuksista. Kaikki nämä asetukset on esitäytetty, jos lompakko on luotu BTCPay Serverin avulla.

![kuva](assets/en/19.webp)

BTCPay Serverin lompakon asetukset alkavat lompakon tilalla. Onko se Vain katselu -tai Kuuma lompakko? Lompakon tyypistä riippuen toiminnot voivat vaihdella puuttuvien transaktioiden uudelleenskannauksesta, vanhojen transaktioiden karsimisesta historiasta, lompakon rekisteröimisestä maksulinkkejä varten tai nykyisen kauppaan liitetyn lompakon korvaamisesta ja poistamisesta. BTCPay Serverin lompakon asetuksissa ylläpitäjät voivat asettaa lompakolle Nimen paremman lompakon hallinnan takaamiseksi. Täällä Ylläpitäjä näkee myös Johdatuskaavion, tilin avaimen (xpub), Sormenjäljen ja Avainpolun. Maksuasetuksissa lompakon asetuksissa on vain 2 pääasetusta. Maksu on mitätön, jos transaktio ei vahvistu (asetetut minuutit) laskun erääntymisen jälkeen. Katsotaan lasku vahvistetuksi, kun maksutransaktiolla on X määrä vahvistuksia. Ylläpitäjät voivat myös asettaa kytkimen näyttämään suositellut maksut maksuissa tai asettaa manuaalisen vahvistustavoitteen lohkojen määrässä.

![kuva](assets/en/20.webp)

**!Huom!**

Jos seuraat tätä kurssia omatoimisesti, tämän tilin luominen olisi jotain, mitä saatat tehdä kolmannen osapuolen isännöinnissä, siksi mainitsemme jälleen, että näitä ei tulisi käyttää tuotantoympäristöissä, vaan ainoastaan koulutustarkoituksiin.

### Esimerkki

#### Bitcoin-lompakon perustaminen BTCPay Serveriin

BTCPay Server mahdollistaa kahdenlaisen lompakon asetuksen. Toinen tapa on tuoda jo olemassa oleva Bitcoin-lompakko. Tuonti voidaan tehdä yhdistämällä laitteistolompakko, tuomalla lompakkotiedosto, syöttämällä Laajennettu julkinen avain, skannaamalla lompakon QR-koodi tai vähiten suosittu, syöttämällä aiemmin luotu Lompakon palautussiemen käsin. BTCPay Serverissä on myös mahdollista luoda uusi lompakko. BTCPay Serverin uuden lompakon konfiguroinnissa on kaksi mahdollista tapaa.
BTCPay Serverin kuuma lompakko -vaihtoehto mahdollistaa ominaisuudet kuten 'Payjoin' tai 'Liquid'. On kuitenkin haittapuoli: tämän lompakon luomiseen käytetty palautusavain (recovery seed) tallennetaan palvelimelle, josta kuka tahansa, jolla on ylläpitäjän oikeudet, voi hakea palautusavaimen. Koska yksityinen avaimesi johdetaan palautusavaimestasi, pahantahtoinen toimija voisi päästä käsiksi nykyisiin ja tuleviin varoihisi!
Tällaisen riskin lieventämiseksi BTCPay Serverissä ylläpitäjä voi asettaa palvelimen asetuksissa > Käytännöt > "Salli ei-ylläpitäjien luoda kuumia lompakoita kaupoilleen" ei-asetukseen, kuten oletusarvoisesti on. Kuuman lompakon turvallisuuden parantamiseksi palvelimen ylläpitäjän tulisi ottaa käyttöön 2FA-tunnistautuminen tileille, joilla saa olla kuuma lompakko. Yksityisten avainten säilyttäminen julkisella palvelimella on vaarallista ja sisältää riskejä. Osa riskeistä on samankaltaisia kuin Lightning Network -riskeissä (katso seuraava luku Lightning Network -riskeistä).

Toinen vaihtoehto, jonka BTCPay Server tarjoaa uuden lompakon luomiseen, on luoda Vain-luku -lompakko (Watch-Only wallet). BTCPay Server luo yksityiset avaimet kerran. Kun käyttäjä vahvistaa kirjoittaneensa alas Seed Phrase -lauseensa, BTCPay Server poistaa yksityiset avaimet palvelimelta. Tuloksena kaupallesi on nyt yhdistetty Vain-luku -lompakko. Saapuneiden varojen käyttämiseksi Vain-luku -lompakostasi, katso luku Miten lähetetään, joko käyttämällä BTCPay Server Vaultia, PSBT:tä (osittain allekirjoitettu bitcoin-siirto) tai, vähiten suositeltuna, antamalla manuaalisesti Seed Phrase -lauseesi.

Loit uuden 'Kaupan' viime osassa. Asennusvelho jatkaa pyytämällä "Aseta lompakko" tai "Aseta Lightning node". Tässä esimerkissä seuraat "Aseta lompakko" -velhoprosessia (1).

![kuva](assets/en/21.webp)

Kun klikkaat "Aseta lompakko", velho jatkaa pyytämällä, miten haluat jatkaa; BTCPay Server tarjoaa nyt mahdollisuuden yhdistää olemassa olevan Bitcoin-lompakon uuteen kauppaasi. Jos sinulla ei ole lompakkoa, BTCPay Server ehdottaa uuden luomista. Tämä esimerkki seuraa "luo uusi lompakko" -vaiheita (2). Seuraa vaiheita oppiaksesi, miten "Yhdistä olemassa oleva lompakko (1).

![kuva](assets/en/22.webp)

**!Huom!**

Jos otat tämän kurssin luokkahuoneessa, nykyinen esimerkki ja luomamme siemen (seed) on vain opetustarkoituksiin. Näissä osoitteissa ei pitäisi koskaan olla merkittäviä määriä muita kuin harjoitusten vaatimat.

(1) Jatka "Uusi lompakko" -velhoa klikkaamalla "Luo uusi lompakko" -painiketta.

![kuva](assets/en/23.webp)

(2) "Luo uusi lompakko" -painiketta klikattuasi seuraavassa ikkunassa velho tarjoaa vaihtoehtoja "Kuuma lompakko" ja "Vain-luku lompakko". Jos seuraat ohjeita opettajan kanssa, ympäristösi on jaettu Demo, ja voit luoda vain Vain-luku lompakon. Huomaa alla olevien kuvien välinen ero. Koska olet Demo-ympäristössä seuraamassa opettajaa, luo "Vain-luku lompakko" ja jatka "Uusi Lompakko" -velhoa.

![kuva](assets/en/24.webp)

![kuva](assets/en/25.webp)

(3) Jatkaessasi uuden lompakon velhoa, olet nyt BTC:n Vain-luku lompakon luontiosiossa. Tässä voimme asettaa lompakon "Osoitetyypin". BTCPay Server mahdollistaa haluamasi osoitetyypin valitsemisen; tämän kurssin kirjoitushetkellä suositellaan edelleen bech32-osoitteiden käyttöä. Opi lisää osoitteista tämän osan ensimmäisessä luvussa.

- Segwit (bech32)
- Native SegWit -osoitteet alkavat merkkijonolla `bc1q`.
  - Esimerkki: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Legacy-osoitteet alkavat numerolla `1`.
  - Esimerkki: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Kokeneille käyttäjille)
  - Taproot-osoitteet alkavat merkkijonolla `bc1p`.
  - Esimerkki: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit wrapped
  - Segwit wrapped -osoitteet alkavat numerolla `3`.
  - Esimerkki: `37BBXXXXXXXXXXXXXXX`

Valitse segwit (suositeltu) ensisijaiseksi lompakon osoitetyypiksesi.

![kuva](assets/en/26.webp)

(4) Kun asetat Walletin parametreja, BTCPay Server mahdollistaa käyttäjille valinnaisen salasanan asettamisen BIP39:n kautta, varmista salasanasi.

![kuva](assets/en/27.webp)

(5) Asetettuasi Walletin osoitetyypin ja mahdollisesti joitakin edistyneitä asetuksia, klikkaa Luo, ja BTCPay Server generoi uuden Walletisi. Huomaa, että tämä on viimeinen vaihe ennen Seed-lausekkeesi generointia. Varmista, että teet tämän ympäristössä, jossa kukaan ei voi varastaa seed-lauseketta katsomalla näyttöäsi.

![kuva](assets/en/28.webp)

(6) Seuraavalla velho-sivulla BTCPay Server näyttää sinulle vasta luodun Walletisi palautus-seed-lausekkeen; nämä ovat avaimet Walletisi palauttamiseen ja transaktioiden allekirjoittamiseen. BTCPay Server generoi 12 sanan seed-lausekkeen. Nämä sanat poistetaan palvelimelta tämän asetussivun jälkeen. Tämä Wallet on erityisesti vain-seuranta Wallet. On suositeltavaa, ettei tätä seed-lauseketta säilytetä digitaalisesti tai valokuvan muodossa. Käyttäjät voivat jatkaa velhossa vain, jos he aktiivisesti tunnustavat kirjoittaneensa seed-lausekkeensa ylös.

![kuva](assets/en/29.webp)

(7) Klikkaamalla Valmis ja turvattuasi vasta generoidun Bitcoin-seed-lausekkeen, BTCPay Server päivittää kauppasi uudella Walletilla ja on valmis vastaanottamaan maksuja. Käyttöliittymässä vasemmassa navigointivalikossa huomaa, kuinka Bitcoin on nyt korostettu ja aktivoitu Walletin alla.

![kuva](assets/en/30.webp)

### Esimerkki: Seed-lausekkeen kirjoittaminen ylös

Tämä on erittäin erityinen ja turvallinen hetki käyttää Bitcoinia. Kuten aiemmin mainittiin, vain sinulla tulisi olla pääsy tai tieto seed-lausekkeestasi. Kun seuraat ohjeita opettajan ja luokan kanssa, generoitua seediä tulisi käyttää vain tässä kurssissa. Liian monet tekijät, luokkatovereiden uteliaat silmät, turvattomat järjestelmät ja monet muut tekevät näistä avaimista vain opetustarkoituksiin sopivia ja luottamattomia. Generoidut avaimet tulisi kuitenkin silti säilyttää kurssiesimerkkejä varten.

Ensimmäinen menetelmä, jota käytämme nykyisessä tilanteessa, myös vähiten turvallinen, on kirjoittaa seed-lauseke oikeassa järjestyksessä. Seed-lausekekortti on kurssimateriaalissa, joka on annettu opiskelijalle tai löytyy BTCPay Serverin GitHubista. Käytämme tätä korttia kirjoittaaksemme generoidut sanat edellisessä vaiheessa. Varmista, että kirjoitat ne oikeassa järjestyksessä. Kun olet kirjoittanut ne ylös, tarkista ne ohjelmiston antamia vastaan varmistaaksesi, että kirjoitit ne oikeassa järjestyksessä. Kun olet kirjoittanut sen ylös, klikkaa valintaruutua, joka ilmoittaa, että olet kirjoittanut seed-lausekkeesi oikein.

### Esimerkki: Seed-lausekkeen säilyttäminen laitteistolompakossa

Tällä kurssilla käsitellään seed-lausekkeen säilyttämistä laitteistolompakossa. Tällaisen laitteen sisällyttäminen kurssiin opettajan toimesta ei aina ole mahdollista. Kurssimateriaaleissa on kirjoitettu lista laitteistolompakoista, jotka sopisivat tähän harjoitukseen.
Tässä esimerkissä käytämme BTCPay Server vaultia ja Blockstream Jade -laitelompakkoa.
Voit myös seurata mukana videolta, jossa näytetään, miten laitelompakko yhdistetään.
![BTCPay Server - Kuinka yhdistää laitelompakkosi BTCPay Vaultiin.](https://youtu.be/s4qbGxef43A)

Lataa BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Varmista, että lataat järjestelmällesi oikeat tiedostot. Windows-käyttäjien tulisi ladata [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe) paketti, Mac-käyttäjien ladata [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), ja Linux-käyttäjien tulisi ladata [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

BTCPay Server Vaultin asentamisen jälkeen, käynnistä ohjelmisto napsauttamalla kuvaketta työpöydälläsi. Kun BTCPay Server Vault on asennettu oikein ja käynnistetty ensimmäistä kertaa, se pyytää lupaa käyttää Web-sovelluksia. Se pyytää antamaan pääsyn tiettyyn BTCPay Serveriin, jota työskentelet. Hyväksy nämä ehdot. BTCPay Server Vault alkaa nyt etsiä laitteistoa. Kun laite on löydetty, BTCPay Server tunnistaa, että Vault on käynnissä ja on hakenut laitteesi.

**!Huom!**

Älä anna SSH-avaimiasi tai palvelimen ylläpitäjätiliä kenellekään muulle paitsi ylläpitäjille, kun käytät hot walletia. Kenellä tahansa, jolla on pääsy näihin tileihin, on pääsy Hot Walletin varoihin.

### Taitojen Yhteenveto

Tässä osiossa opit seuraavat asiat:

- Bitcoin-lompakon transaktionäkymä ja sen erilaiset luokittelut.
- Eri vaihtoehdot Bitcoin-lompakosta lähettämiseen, laitteistosta hot walletteihin.
- Gap limit -ongelma, joka ilmenee useimmissa lompakoissa, ja miten se korjataan.
- Kuinka luoda uusi Bitcoin-lompakko BTCPay Serverissä, mukaan lukien avainten tallentaminen laitelompakkoon ja palautuslausekkeen varmuuskopiointi.

Tässä tavoitteessa olet oppinut, miten luoda uusi Bitcoin-lompakko BTCPay Serverissä. Emme ole vielä käsitelleet, miten näitä avaimia turvataan tai käytetään. Tämän tavoitteen pikakatsauksessa olet oppinut, miten perustaa ensimmäinen kauppa. Olet oppinut, miten luoda Bitcoin Recovery Seed -lause.

### Tietämyksen Arvioinnin Käytännön Katsaus

Kuvaile menetelmä avainten luomiseksi ja järjestelmä niiden turvaamiseksi, sekä turvajärjestelmän kauppaehdot/riskit.

## BTCPay Server Lightning Wallet

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Kun palvelimen ylläpitäjä ottaa käyttöön uuden BTCPay Server-instanssin, hän voi perustaa salamaverkon toteutuksen, LND:n, Core Lightningin tai Eclairin; katso Osa BTCPay Serverin määrittämisestä tarkemmat asennusohjeet.
Jos luokkahuone seuraa mukana, Lightning-noodin yhdistäminen BTCPay Serveriisi toimii Custom-noodin kautta. Käyttäjä, joka ei ole palvelimen ylläpitäjä BTCPay Serverillä, ei oletusarvoisesti pysty käyttämään sisäistä Lightning-noodia. Tämä on suojatakseen palvelimen omistajaa menettämästä varojaan. Palvelimen ylläpitäjät voivat asentaa Pluginin antaakseen pääsyn Lightning-noodiinsa LNBankin kautta; tämä on tämän kirjan ulkopuolella; lue lisää LNBankista virallisella plugin-sivulla.

### Yhdistä sisäinen nood (palvelimen ylläpitäjä)

Palvelimen ylläpitäjä voi käyttää BTCPay Serverin sisäistä Lightning-noodia. Riippumatta Lightning-toteutuksesta, yhdistäminen sisäiseen Lightning-noodiin on sama.

Siirry aiemmin asetettuun kauppaan ja klikkaa vasemmassa valikossa "Lightning"-lompakkoa. BTCPay Server tarjoaa kaksi asennusmahdollisuutta, käyttäen sisäistä noodia (vain palvelimen ylläpitäjä oletuksena) tai custom-noodia (ulkoinen yhteys). Palvelimen ylläpitäjät voivat klikata "Käytä sisäistä noodia" -vaihtoehtoa. Lisäkonfiguraatiota ei vaadita. Klikkaa "tallenna"-painiketta ja huomaa ilmoitus, joka sanoo, "BTC Lightning nood päivitetty". Kaupalla on nyt onnistuneesti Lightning-verkon ominaisuudet.

### Yhdistä ulkoinen nood (kaupan omistaja/palvelimen käyttäjä)

Koska kaupan omistajat eivät oletusarvoisesti saa käyttää palvelimen ylläpitäjän Lightning-noodia, yhteys on muodostettava ulkoiseen noodiin, joko noodiin, joka on kaupan omistajan hallussa ennen BTCPay Serverin asetusta, LNBank-plugin, jos palvelimen ylläpitäjä on tehnyt sen saataville, tai holhousratkaisu kuten Alby.

Siirry aiemmin asetettuun kauppaan ja klikkaa vasemmassa valikossa "Lightning" lompakoiden alla. Koska kaupan omistajat eivät oletusarvoisesti saa käyttää sisäistä noodia, tämä vaihtoehto on harmaana. Custom-noodin käyttö on ainoa oletusarvoisesti saatavilla oleva vaihtoehto kaupan omistajille.

BTCPay Server tarvitsee yhteystiedot; aiemmin tehty (tai holhousratkaisu) toimittaa nämä tiedot Lightning-toteutukseen liittyen. BTCPay Serverissä kaupan omistajat voivat käyttää seuraavia yhteyksiä;

- C-lightning TCP:n tai Unixdomainsocketconnectionin kautta.
- Lightning Charge HTTPS:n kautta
- Eclair HTTPS:n kautta
- LND REST proxyn kautta
- LNDhub REST API:n kautta

![kuva](assets/en/31.webp)

Klikkaa "testaa yhteys" varmistaaksesi, että olet syöttänyt yhteystiedot oikein. Kun yhteys vahvistetaan toimivaksi, klikkaa tallenna, ja BTCPay Server näyttää, että kauppa on päivitetty Lightning-noodilla.

### Hallinnoi sisäistä Lightning-noodia LND (Palvelimen ylläpitäjä)

Yhdistettyään sisäisen Lightning-noodin, palvelimen ylläpitäjät huomaavat uusia ruutuja kojelaudalla erityisesti Lightning-tiedot varten.

- Lightning-saldo
- BTC kanavissa
  - BTC avaavat kanavat
  - BTC paikallinen saldo
  - BTC etäsaldo
  - BTC sulkevat kanavat
- BTC On-chain
  - BTC vahvistettu
  - BTC vahvistamaton
  - BTC varattu
- Lightning-palvelut
  - Ride the Lightning (RTL).

Klikkaamalla joko Ride the Lightning -logoa "Lightning-palvelut" ruudussa tai "Lightning" lompakoiden alla vasemmassa valikossa, palvelimen ylläpitäjät voivat saavuttaa RTL:n Lightning-noodin hallintaa varten.

**Huomaa!**

Yhdistäminen sisäiseen Lightning-noodiin epäonnistuu - Jos sisäinen yhteys epäonnistuu, varmista:

1. Bitcoin on-chain nood on täysin synkronoitu
2. Sisäinen lightning-noodi on "Käytössä" kohdassa "Lightning" > "Asetukset" > "BTC Lightning Asetukset"
   Jos et pysty muodostamaan yhteyttä Lightning-noodiisi, yritä käynnistää palvelimesi uudelleen tai lue lisätietoja BTCPay Serverin virallisesta dokumentaatiosta; https://docs.btcpayserver.org/Troubleshooting/ . Et voi hyväksyä Lightning-maksuja kaupassasi ennen kuin Lightning-noodisi näkyy "Online"-tilassa. Kokeile testata Lightning-yhteyttäsi napsauttamalla "Public Node Info" -linkkiä.

### Lightning-lompakko

Vasemman valikkopalkin Lightning-lompakko-vaihtoehdosta palvelimen ylläpitäjät löytävät helposti pääsyn RTL:ään, heidän julkiseen nooditietoonsa ja Lightning-asetuksiin, jotka ovat erityisiä heidän BTCPay Server -kaupalleen.

#### Sisäinen nooditieto

Palvelimen ylläpitäjät voivat napsauttaa sisäistä nooditietoa ja tarkastella palvelimensa tilaa (Online/ Offline) sekä yhteysmerkkijonoa Clearnetille tai Torille.

![kuva](assets/en/32.webp)

#### Yhteyden vaihto

Jos kaupan omistaja päättää käyttää muutoksia Lightning-asetuksissa - Vaihda yhteyttä.
Julkisen nooditiedon vieressä kaupan omistajat löytävät tämän vaihtoehdon. Se palauttaa alkuperäisen asetuksen ulkoiselle lightning-noodiyhteydelle, täytä uudet Lightning-nooditiedot, napsauta tallenna ja päivitä kauppa uusilla nooditiedoilla.

![kuva](assets/en/33.webp)

#### Palvelut

Jos palvelimen ylläpitäjä päättää asentaa useita palveluita Lightning-toteutusta varten, ne luetellaan täällä. Standardin LND-toteutuksen yhteydessä ylläpitäjillä on Ride The Lightning (RTL) standardityökaluna noodinhallintaan.

#### BTC Lightning -lompakon asetukset

Lisättyään Lightning-noodin kauppaan aiemmassa vaiheessa, Lightning-lompakon asetuksissa kaupan omistajat voivat silti päättää poistaa sen käytöstä kaupassaan käyttämällä Togglea Lightning-asetusten yläosassa.

![kuva](assets/en/34.webp)

#### Lightning-maksuvaihtoehdot

Kaupan omistajat voivat asettaa parametreja seuraaville parantaakseen Lightning-kokemusta asiakkailleen.

- Näytä Lightning-maksusummat Satosheina.
- Lisää hyppyvihjeitä yksityisiin kanaviin Lightning-laskuun.
- Yhdistä on-chain ja Lightning-maksu URL/QR-koodit kassalla.
- Aseta kuvausmalli Lightning-laskuille.

#### LNURL

Kaupan omistajat voivat valita käyttävätkö he LNURL:ää vai eivät. Lightning Network URL eli LNURL on ehdotettu standardi Lightning-maksajan ja -saajan välisille vuorovaikutuksille. Lyhyesti sanottuna LNURL on bech32-koodattu URL, joka on etuliitteellä lnurl. Lightning-lompakon odotetaan purkavan URL:n, ottavan yhteyttä URL:ään ja odottavan JSON-objektia, jossa on lisäohjeita, erityisesti tagi, joka määrittelee lnurl:n käyttäytymisen.

- Ota LNURL käyttöön
- LNURL Classic Mode
  - Lompakon yhteensopivuuden vuoksi, Bech32-koodattu (klassinen) vs. selväkielinen URL (tuleva)
- Salli maksajan lisätä kommentti.

### Esimerkki 1

#### Yhdistä Lightningiin sisäisen noodin kautta (Ylläpitäjä)

Tämä vaihtoehto on käytettävissä vain, jos olet tämän instanssin ylläpitäjä tai jos ylläpitäjä on muuttanut oletusasetuksia, joissa käyttäjät voivat käyttää sisäistä lightning-noodia.

Ylläpitäjänä, napsauta Lightning Wallet -kohtaa vasemmassa valikkopalkissa. BTCPay Server pyytää käyttämään yhtä kahdesta vaihtoehdosta Lightning-noodin yhdistämiseen, sisäinen nood tai mukautettu ulkoinen nood. Napsauta Käytä sisäistä noodia ja napsauta tallenna.

#### Lightning-noodisi hallinta (RTL)

Yhdistettyäsi sisäiseen lightning-noodiin, BTCPay Server päivittyy ja näyttää ilmoituksen "BTC Lightning nood päivitetty", vahvistaen nyt yhdistäneesi Lightningin kauppaasi.

Lightning-noodin hallinta on palvelimen ylläpitäjän tehtävä. Tämä sisältää.

- Hallitse transaktioita
- Likviditeetin hallinta
  - Sisääntuleva likviditeetti
  - Ulosmenevä likviditeetti
- Vertaisten ja kanavien hallinta
  - Yhdistetyt vertaiset
  - Kanavamaksut
  - Kanavan tila
- Säännölliset varmuuskopioiden tekemiset kanavatiloista.
- Reititysraporttien tarkistaminen
- Vaihtoehtoisesti voit käyttää palveluita, kuten Loop.

Kaikki salamaverkkosolmun hallinta tehdään standardina RTL:n kautta (olettaen, että käytät LND-toteutusta). Ylläpitäjät voivat klikata Lightning Walletiaan BTCPay Serverissä ja löytää painikkeen RTL:n avaamiseksi. BTCPay Serverin päävalikko on nyt päivitetty salamaverkon tiilillä, mukaan lukien nopea pääsy RTL:ään.

### Esimerkki 2

#### Yhdistä salamaverkkoon Albyn avulla

Kun yhdistetään holhoojan, kuten Albyn kanssa, kauppiaiden tulisi ensin luoda tili, käy osoitteessa: https://getalby.com/

![kuva](assets/en/35.webp)

Alby-tilin luomisen jälkeen, siirry BTCPay Server kauppaasi.

Vaihe 1: Klikkaa 'Aseta salamaverkkosolmu' Dashboardissa tai 'Salamaverkko' lompakoiden alla.

![kuva](assets/en/36.webp)

Vaihe 2: Syötä lompakkoyhteystietosi, jotka Alby on antanut. Albyn Dashboardissa, klikkaa Wallet. Täältä löydät "Wallet Connection Credentials". Kopioi nämä tiedot. Liitä Albyn antamat tiedot Yhteyskonfiguraatiokenttään BTCPay Serverissä.

![kuva](assets/en/37.webp)

Vaihe 3: Kun olet antanut BTCPay Serverille yhteystiedot, klikkaa "Testaa yhteyttä" -painiketta varmistaaksesi, että yhteys toimii asianmukaisesti. Huomaa "Yhteys salamaverkkosolmuun onnistui" -viesti näytön yläosassa. Tämä vahvistaa, että kaikki toimii järjestyksessä.

![kuva](assets/en/38.webp)

Vaihe 4: Klikkaa tallenna, ja kauppasi on nyt yhdistetty salamaverkkosolmuun Albyn kautta.

![kuva](assets/en/39.webp)

**!Huom!**

Älä luota holhoojan salamaverkkoratkaisuun enemmän kuin olet valmis menettämään.

### Taitojen Yhteenveto

Tässä osiossa opit:

- Miten yhdistää sisäinen tai ulkoinen salamaverkkosolmu
- Eri salamaverkkoon liittyvien tiilien sisällöt ja toiminnot Dashboardissa
- Miten konfiguroida salamaverkkolompakko käyttäen Voltage Surgea tai Albya

### Tiedon arviointi Käytännön katsaus

Kuvaile joitakin vaihtoehtoja salamaverkkolompakon yhdistämiseksi kauppaasi.

# BTCPay Server Käyttöliittymä

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Dashboardin yleiskatsaus

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server on modulaarinen ohjelmistopaketti. Kuitenkin, on olemassa standardeja, joita jokainen BTCPay Server tulee sisältämään ja joita Ylläpitäjä/käyttäjät tulevat käyttämään. Aloittaen Dashboardista. Jokaisen BTCPay Serverin pääsykohde kirjautumisen jälkeen. Dashboard tarjoaa yleiskatsauksen siitä, miten kauppasi suoriutuu, lompakon nykyisen saldon ja viimeisimmät tx:t viimeisen 7 päivän ajalta. Koska se on modulaarinen näkymä, Pluginien on mahdollista hyödyntää tätä näkymää hyödykseen ja luoda omia tiilejään Dashboardiin. Tässä oppikirjassa puhumme vain standardi plugineista/ sovelluksista ja niiden vastaavista näkymistä läpi BTCPay Serverin.

### Dashboardin Tiilet

BTCPay Serverin päävalikon näkymässä on useita standarditiilejä saatavilla. Nämä tiilet on tarkoitettu kaupan omistajalle tai Ylläpitäjälle hallitakseen kauppaansa nopeasti yhdessä yleiskatsauksessa.

- Lompakon saldo
- Tapahtumatoiminta
- Salamaverkon saldo (jos salamaverkko on käytössä kaupassa)
- Salamaverkon palvelut (jos salamaverkko on käytössä kaupassa)
- Viimeaikaiset tapahtumat.
- Viimeaikaiset laskut
- Käynnissä olevat joukkorahoitukset
- Kaupan suorituskyky / myydyimmät tuotteet.

### Lompakon saldo

Lompakon Saldo -laatta tarjoaa nopean yleiskatsauksen lompakkosi varoihin ja suorituskykyyn. Sen voi tarkastella joko BTC:ssä tai Fiat-valuutassa viikoittaisena, kuukausittaisena tai vuosittaisena graafina.
![kuva](assets/en/40.webp)

### Tapahtumatoiminta

Lompakon Saldo -laatan vieressä BTCPay Server näyttää nopean yleiskatsauksen odottavista maksuista, viimeisen 7 päivän aikana tapahtuneiden Tapahtumien määrästä, ja onko kauppasi myöntänyt hyvityksiä. Hallinta-painikkeen klikkaaminen vie sinut odottavien maksujen hallintaan (lisätietoja maksuista BTCPay Server - Maksut -luvussa).

![kuva](assets/en/41.webp)

### Salama Saldo

Tämä näkyy vain, kun Salama on aktivoitu.

Kun Ylläpitäjä on sallinut Salama-verkon käytön, BTCPay Serverin hallintapaneelissa on nyt uusi laatta, jossa on tietoa Salama-nodestasi. Kuinka paljon BTC:tä on kanavissa, miten tämä jakautuu paikallisesti tai etäisesti (sisääntuleva tai ulostuleva likviditeetti), ovatko kanavat sulkeutumassa tai avautumassa, ja kuinka paljon bitcoinia on pidetty on-chain Salama-nodessa.

![kuva](assets/en/42.webp)

### Salama Palvelut

Tämä näkyy vain, kun salama on aktiivinen.

BTCPay Serverin hallintapaneelissa Salama-saldon näkemisen lisäksi ylläpitäjät näkevät myös Salama Palvelut -laatan. Täällä ylläpitäjät voivat löytää nopeita painikkeita työkaluille, joita he käyttävät Salama-nodensa hallintaan; esimerkiksi Ride the Lightning on yksi BTCPay Serverin vakiotyökaluista Salama-noden hallintaan.

![kuva](assets/en/43.webp)

### Viimeaikaiset Tapahtumat

Viimeaikaisten tapahtumien laatta näyttää kauppasi viimeisimmät tapahtumat. Yhdellä klikkauksella BTCPay Serverin instanssin Ylläpitäjä voi nyt nähdä viimeisimmän tapahtuman ja tarkistaa, tarvitaanko siihen huomiota.

![kuva](assets/en/44.webp)

### Viimeaikaiset laskut

Viimeaikaisten laskujen laatta näyttää kuusi viimeisintä BTCPay Serverillä luotua laskua, mukaan lukien tilan ja laskun määrän. Laatta sisältää myös "Näytä kaikki" -painikkeen, jolla pääsee helposti käsiksi koko Laskujen yleiskatsaukseen.

![kuva](assets/en/45.webp)

### Kassapiste ja Joukkorahoitukset

Koska BTCPay Server tarjoaa joukon vakio-liitännäisiä tai sovelluksia, Kassapiste ja Joukkorahoitus ovat kaksi BTCPay Serverin pääliitännäistä. Jokaiselle kaupalle ja lompakolle BTCPay Serverin käyttäjä voi luoda niin monta Kassapistettä tai Joukkorahoitusta kuin katsoo sopivaksi. Kumpikin luo uuden hallintapaneelin laatikon, joka näyttää liitännäisten suorituskyvyn.

![kuva](assets/en/46.webp)

Huomaa pieni ero Kassapisteen ja Joukkorahoituksen laatikon välillä. Ylläpitäjä näkee Kassapisteen laatikossa myydyimmät tuotteet. Joukkorahoituslaatikossa tämä muuttuu Parhaiksi Eduiksi. Molemmissa laatikoissa on nopeita painikkeita vastaavan sovelluksen hallintaan ja viimeaikaisten laskujen tarkasteluun, jotka on luotu myydyimmistä tuotteista tai parhaista eduista.

![kuva](assets/en/47.webp)

**!?Huomio!?**

Saldojen graafit ja viimeaikaiset tapahtumat ovat saatavilla vain on-chain maksutavalle. Tiedot Salama-verkon saldoista ja tapahtumista ovat työn alla. BTCPay Serverin version 1.6.0 mukaan perustiedot Salama-verkon saldoista ovat saatavilla.

### Taitojen Yhteenveto

Tässä osiossa opit seuraavat asiat:

- Laattojen perusasettelu pääsivulla tunnetaan nimellä Hallintapaneeli.
- Perustiedot kunkin laatikon sisällöstä.

### Tiedon Arvioinnin Yhteenveto

Listaa muististasi niin monta laatikkoa kuin voit Hallintapaneelista.

## BTCPay Server - Kaupan asetukset

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
BTCPay Server -ohjelmistossa tunnemme kaksi tyyppiä asetuksia. BTCPay Serverin kauppakohtaiset asetukset, jotka löytyvät vasemman valikon alapuolelta Dashboardin alta, ja BTCPay Serverin yleiset asetukset, jotka löytyvät valikon alaosasta juuri Accountin yläpuolelta. Vain palvelimen ylläpitäjät voivat tarkastella BTCPay Serverin palvelinkohtaisia asetuksia.
Kaupan asetukset koostuvat monista välilehdistä, jotka kategorisoivat kunkin asetussarjan.

- Yleiset
- Kurssit
- Kassan Ulkoasu
- Pääsytunnukset
- Käyttäjät
- Roolit
- Webhookit
- Maksuprosessorit
- Sähköpostit
- Lomakkeet

### Yleiset

Yleiset asetukset -välilehdellä kaupan omistajat asettavat brändäyksensä ja maksuoletukset. Kaupan alustavassa asetuksessa kaupalle annettiin nimi; tämä heijastuu Yleiset asetukset -kohdassa Kaupan Nimen alla. Täällä kaupan omistaja voi myös asettaa verkkosivustonsa vastaamaan brändäystä ja Kaupan ID:n, jotta ylläpitäjä tunnistaa sen tietokannassa.

#### Brändäys

Koska BTCPay Server on FOSS, kaupan omistaja voi tehdä mukautetun brändäyksen vastaamaan omaa kauppaansa. Aseta brändin väri, tallenna brändisi logot ja lisää mukautettua CSS:ää julkisille/asiakkaalle näkyville sivuille (Laskut, Maksupyynnöt, Vetomaksut)

#### Maksu

Maksuasetuksissa kaupan omistajat voivat asettaa kauppansa oletusvaluutan (joko Bitcoinissa tai missä tahansa fiat-valuutassa).

#### Salli kenen tahansa luoda laskuja

Tämä asetus on tarkoitettu kehittäjille tai rakentajille BTCPay Serverin päällä. Tämän asetuksen kytkeminen päälle kaupallesi mahdollistaa ulkopuolisten luoda laskuja BTCPay Server -instanssissasi.

#### Lisää lisämaksu (verkkomaksu) laskuihin

Ominaisuus BTCPayssa suojatakseen kauppiaita pölyhyökkäyksiltä tai asiakkailta, jotka aiheuttavat korkeita kuluja myöhemmin, kun kauppiaan täytyy siirtää suuri määrä bitcoineja kerralla. Esimerkiksi asiakas loi 20 dollarin laskun ja maksoi sen osittain, maksamalla 1 dollarin 20 kertaa, kunnes lasku oli kokonaan maksettu. Kauppiaalla on nyt suurempi transaktio, mikä lisää louhintakustannuksia, jos kauppias päättää siirtää nuo varat myöhemmin. Oletuksena BTCPay lisää lisäverkkokustannuksen kokonaislaskun määrään kattamaan tuon kulun kauppiaalle, kun lasku maksetaan useassa transaktiossa. BTCPay tarjoaa useita vaihtoehtoja mukauttaa tätä suojatoimintoa. Voit soveltaa verkkomaksua:

- Vain jos asiakas tekee enemmän kuin yhden maksun laskulle (Yllä olevassa esimerkissä, jos asiakas loi 20\$ laskun ja maksoi 1\$, kokonaismaksuvelka on nyt 19\$ + verkkomaksu. Verkkomaksu lisätään ensimmäisen maksun jälkeen)
- Jokaisesta maksusta (mukaan lukien ensimmäinen maksu, esimerkissämme kokonaismäärä olisi heti 20\$ + verkkomaksu, jopa ensimmäisestä maksusta)
- Älä koskaan lisää verkkomaksua (poistaa verkkomaksun kokonaan käytöstä)

Vaikka se suojaa pölytransaktioilta, se voi myös heijastua kielteisesti yrityksiin, jos sitä ei kommunikoida kunnolla. Asiakkailla saattaa olla lisäkysymyksiä ja he saattavat ajatella, että heitä veloitetaan liikaa.

#### Lasku vanhenee, jos koko summaa ei ole maksettu jälkeen?

Laskun ajastin on oletuksena asetettu 15 minuuttiin. Ajastin on suojamekanismi volatiliteettia vastaan, koska se lukitsee Bitcoin-määrän Bitcoinin ja fiat-valuutan kurssien mukaan. Jos asiakas ei maksa laskua määritellyssä ajassa, lasku katsotaan vanhentuneeksi. Lasku katsotaan "maksetuksi" heti, kun transaktio näkyy lohkoketjussa (0-vahvistusta) mutta "valmiiksi" kun se saavuttaa kauppiaan määrittelemän vahvistusten määrän (yleensä 1-6). Ajastin on mukautettavissa minuuteittain.

#### Katsotaan lasku maksetuksi, vaikka maksettu summa on X% vähemmän kuin odotettu?

Kun asiakas käyttää vaihtopalvelun lompakkoa maksamaan suoraan laskusta, vaihto ottaa pienen maksun. Tämä tarkoittaa, että tällaista laskua ei katsota täysin suoritetuksi. Lasku saa tilan "osittain maksettu". Voit asettaa prosenttiosuuden tässä, jos kauppias haluaa hyväksyä alimaksetut laskut.

### Hinnat

BTCPay Serverissä, kun lasku luodaan, tarvitaan aina uusin ja tarkin Bitcoinista fiat-valuuttaan hinta. Uutta kauppaa luodessa BTCPay Serverissä, ylläpitäjiltä kysytään heidän haluamaansa hintalähdettä; kaupan perustamisen jälkeen kaupan omistajat voivat aina muuttaa hintalähdettään tässä välilehdessä.

#### Edistynyt hinnan sääntöjen käsikirjoitus

Pääasiassa voimakäyttäjien käyttämä. Jos tämä on käytössä, kaupan omistajat voivat luoda käsikirjoituksia hinnan käyttäytymisestä ja siitä, miten asiakkailta veloitetaan.

#### Testaus

Nopea testauspaikka haluamillesi valuuttapareille. Tämä sisältää myös toiminnon oletusvaluuttaparien tarkistamiseen REST-kyselyn kautta.

### Kassan ulkoasu

Kassan ulkoasuvälilehti alkaa laskukohtaisilla asetuksilla ja oletusmaksutavalla ja mahdollistaa tiettyjen maksutapojen käytön, kun asetetut vaatimukset täyttyvät.

#### Laskun asetukset

Oletusmaksutavat. BTCPay Serverin vakioasetuksissa on kolme vaihtoehtoa.

- BTC (ketjussa)
- BTC (LNURL-pay)
- BTC (ketjun ulkopuolella & Lightning)

Voimme asettaa parametreja kaupallemme, jossa asiakas vuorovaikuttaa vain Lightningin kanssa, kun hinta on alle X määrän ja päinvastoin ketjussa tapahtuville transaktioille, kun X on suurempi kuin Y, aina esitetään ketjussa tapahtuvan maksun vaihtoehto.

![kuva](assets/en/48.webp)

#### Kassa

BTCPay Serverin 1.7 julkaisussa esiteltiin uusi Kassa-käyttöliittymä, jota kutsutaan Checkout V2:ksi. Koska julkaisu 1.9 standardoitiin, ylläpitäjät ja kaupan omistajat voivat silti asettaa kassan edelliseen julkaisuun. Käyttämällä vaihtoehtoa "Käytä klassista kassaa", kaupan omistaja voi palauttaa kaupan aiempaan kassa-kokemukseen. BTCPay Serverillä on myös valikoima esiasetuksia verkkokaupalle tai myymäläkokemukselle.

![kuva](assets/en/49.webp)

Kun asiakas vuorovaikuttaa kaupan kanssa ja luo laskun, laskulla on vanhentumisaika. Oletuksena BTCPay Server asettaa tämän 5 minuutiksi, ja ylläpitäjä voi asettaa tämän mihin tahansa pitää sopivana. Kassasivua voidaan edelleen mukauttaa tarkistamalla seuraavat parametrit:

- Juhli maksua näyttämällä konfettia
- Näytä kaupan otsikko (nimi ja logo)
- Näytä "Maksa lompakossa" -painike
- Yhdistä ketjussa ja ketjun ulkopuolella tapahtuvat maksut URL/QR-koodit
- Näytä Lightning-maksujen määrät Satosheina
- Automaattinen kielen tunnistus kassalla

![kuva](assets/en/50.webp)

Kun Automaattinen kielen tunnistus ei ole asetettu, BTCPay Server näyttää oletuksena englannin. Kaupan omistaja voi muuttaa tätä oletusta haluamalleen kielelle.

![kuva](assets/en/51.webp)

Napsauta pudotusvalikkoa ja kaupan omistajat voivat asettaa mukautetun HTML-otsikon, joka näytetään kassasivulla.

![kuva](assets/en/52.webp)

Jotta asiakas tietää maksutapansa, kaupan omistaja voi nimenomaisesti asettaa kassansa aina vaatimaan käyttäjiä valitsemaan haluamansa maksutavan. Kun lasku on maksettu, BTCPay Server sallii asiakkaan palata verkkokauppaan. Kaupan omistajat voivat asettaa tämän uudelleenohjauksen tapahtumaan automaattisesti sen jälkeen, kun asiakas on maksanut.

![kuva](assets/en/53.webp)

#### Julkinen kuitti

Julkisen kuitin asetuksissa kaupan omistaja voi asettaa kuitin sivut julkisiksi ja näyttää maksulistan kuitusivulla sekä kuitin QR-koodin, jotta asiakas pääsee siihen helposti digitaalisesti.
![kuva](assets/en/54.webp)

### Pääsytunnukset

Pääsytunnukset ovat käytössä tietyissä e-kaupan integraatioissa tai räätälöidyissä integraatioissa pariliitoksen muodostamiseksi.

![kuva](assets/en/55.webp)

### Käyttäjät

Kaupan käyttäjät ovat henkilöitä, joita kaupan omistaja voi hallinnoida: henkilökuntansa jäseniä, heidän tilejään ja pääsyään kauppaan. Henkilökunnan jäsenten luotua tilinsä, kaupan omistaja voi lisätä tiettyjä käyttäjiä kauppaan joko vierailijoina tai omistajina. Henkilökunnan roolin tarkempi määrittely löytyy seuraavasta osiosta nimeltä "BTCPay Serverin kaupan asetukset - Roolit".

![kuva](assets/en/56.webp)

### Roolit

Kaupan omistaja saattaa pitää käyttäjien vakiorooleja riittämättöminä. Mukautetuissa rooliasetuksissa kaupan omistaja voi määritellä tarkat tarpeet kullekin roolille liiketoiminnassaan.

(1) Luodaksesi uuden roolin, klikkaa "+ Lisää rooli" -painiketta.

![kuva](assets/en/57.webp)

(2) Anna roolille nimi, esimerkiksi "Kassanhoitaja".

![kuva](assets/en/58.webp)

(3) Määritä yksittäiset oikeudet roolille.

- Muokkaa kauppojasi.
- Hallinnoi kauppoihisi liitettyjä vaihtotilejä.
  - Katsele kauppoihisi liitettyjä vaihtotilejä.
- Hallinnoi vetomaksujasi.
- Luo vetomaksuja.
  - Luo hyväksymättömiä vetomaksuja.
- Muokkaa laskuja.
  - Katsele laskuja.
  - Luo lasku.
  - Luo laskuja kauppoihisi liitetyistä salamaverkon solmuista.
- Katsele kauppojasi.
  - Katsele laskuja.
  - Katsele maksupyyntöjäsi.
  - Muokkaa kauppojesi webkoukkuja.
- Muokkaa maksupyyntöjäsi.
  - Katsele maksupyyntöjäsi.
- Käytä kauppoihisi liitettyjä salamaverkon solmuja.
  - Katsele kauppoihisi liitettyjä salamaverkon laskuja.
  - Luo laskuja kauppoihisi liitetyistä salamaverkon solmuista.
- Talleta varoja kauppoihisi liitettyihin vaihtotileihin.
- Nosta varoja kauppojesi vaihtotileiltä kauppaasi.
- Käy kauppaa kauppasi vaihtotileillä.

Kun rooli on luotu, sen nimi on kiinteä eikä sitä voi muuttaa muokkaustilassa.

![kuva](assets/en/59.webp)

### Webkoukut

BTCPay Serverissa on suhteellisen helppoa luoda uusi "Webkoukku". BTCPay Serverin kaupan asetuksissa - Webkoukut-välilehdellä kaupan omistaja voi helposti luoda uuden webkoukun klikkaamalla "+ Luo Webkoukku". Webkoukut mahdollistavat BTCPay Serverin lähettämään HTTP-tapahtumia kauppaasi liittyen muihin palvelimiin tai e-kaupan integraatioihin.

![kuva](assets/en/60.webp)

Olet nyt näkymässä, jossa voit luoda Webkoukun. Varmista, että tiedät Payload URL:si ja liitä tämä BTCPay Serveriisi. Payload URL:si liittämisen jälkeen alla näkyy webkoukun salaisuus. Kopioi webkoukun salaisuus ja anna se päätepisteessä. Kun kaikki on asetettu, voit vaihtaa BTCPay Serverissä automaattiseen uudelleentoimitukseen. Yritämme toimittaa uudelleen kaikki epäonnistuneet toimitukset 10 sekunnin, 1 minuutin ja enintään 6 kertaa 10 minuutin jälkeen. Voit vaihtaa jokaisen tapahtuman välillä tai määrittää tarpeidesi mukaiset tapahtumat. Varmista, että webkoukku on käytössä ja tallenna se klikkaamalla Lisää webkoukku.

![kuva](assets/en/61.webp)

Webkoukut eivät ole yhteensopivia Bitpay API:n kanssa. BTCPay Serverissä on kaksi erillistä IPN:ää (BitPayn termein: "Instant Payment Notifications").

- Webhookp
- Ilmoitukset

Käytä vain Ilmoitus URL:ää, kun luot laskuja Bitpay API:n kautta.

### Maksuprosessorit

Maksuprosessorit toimivat yhdessä Maksujen käsittelyn konseptin kanssa BTCPay Serverissa. Maksuaggregaattori niputtaa useita siirtoja ja lähettää ne kerralla. Maksuprosessoreiden avulla kaupan omistaja voi automatisoida niputetut maksut. BTCPay Server tarjoaa kaksi automatisoitujen maksujen menetelmää, On-chain ja Off-chain (LN).
Kaupan omistaja voi klikata ja konfiguroida molemmat maksuprosessorit erikseen. Kaupan omistaja saattaa haluta ajaa on-chain prosessorin vain joka X tunti, kun taas off-chain saattaa toimia muutaman minuutin välein. On-chain osalta voit myös asettaa tavoitteen, mihin lohkoon sen tulisi sisältyä. Oletusarvoisesti tämä on asetettu 1 (tai seuraava saatavilla oleva lohko). Huomaa, että Off-chain maksuprosessorin asettaminen sisältää vain aikavälin ajastimen eikä lohkon kohdetta. Salamaverkon maksut ovat välittömiä.

![kuva](assets/en/62.webp)
![kuva](assets/en/63.webp)

Kaupan omistajat voivat konfiguroida on-chain prosessorin vain, jos heillä on Hot-wallet yhdistettynä kauppaansa.

![kuva](assets/en/64.webp)

Maksuprosessorin asettamisen jälkeen voit nopeasti poistaa tai muokata sitä palaamalla Maksuprosessori-välilehteen BTCPay Serverin Kaupan asetuksissa.

**!?Huomio!?**

Maksuprosessori on-chain - Onchain maksuprosessori toimii vain kaupassa, joka on konfiguroitu Hot walletin kanssa yhdistettynä. Jos Hot walletia ei ole yhdistetty, BTCPay Server ei hallitse lompakon avaimia eikä pysty käsittelemään maksuja automaattisesti.

### Sähköpostit

BTCPay Server voi käyttää sähköposteja ilmoituksiin tai, kun asetettu oikein, palauttamaan tilejä, jotka on luotu instanssissa, sillä vakiona BTCPay Server ei lähetä sähköpostia, kun salasana on kadonnut, esimerkiksi.

![kuva](assets/en/65.webp)

Ennen kuin kaupan omistaja voi asettaa sähköpostisääntöjä laukaistavaksi tietyissä kauppansa tapahtumissa, meidän on määritettävä joitakin perussähköpostiasetuksia. BTCPay Server tarvitsee nämä asetukset lähettääkseen sähköposteja tapahtumista kauppasi perusteella tai salasanan nollaukseen.

BTCPay Server on helpottanut tämän tiedon täyttämistä käyttämällä "Pikatäyttö"-vaihtoehtoa:

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Käyttämällä pikatäyttövaihtoehtoa, BTCPay Server täyttää SMTP-palvelimen ja portin kentät esivalmiiksi; nyt kaupan omistajan tarvitsee vain täyttää omat tietonsa sähköpostiosoitteeseen, kirjautumiseen (joka on yleensä sama kuin sähköpostiosoitteesi) ja salasanaasi. BTCPay Serverin tarjoama edistynyt vaihtoehto sähköpostiasetuksissa on TLS-sertifikaatin turvatarkastusten poistaminen käytöstä; oletusarvoisesti tämä on käytössä.

![kuva](assets/en/66.webp)

Sähköpostisääntöjen avulla kaupan omistaja voi asettaa tiettyjä tapahtumia laukaisemaan sähköposteja tietyille sähköpostiosoitteille.

- Lasku Luotu
- Lasku Sai Maksun
- Lasku Käsittelyssä
- Lasku Vanhentunut
- Lasku Selvitetty
- Lasku Virheellinen
- Laskun Maksu Selvitetty

Jos asiakas on antanut sähköpostiosoitteen, nämä laukaisimet voivat myös lähettää tiedon asiakkaalle. Kaupan omistajat voivat esitäyttää Aihe-rivin selventääkseen, miksi tämä sähköposti lähetettiin ja mikä laukaisi sen.

![kuva](assets/en/67.webp)

### Lomakkeet

Koska BTCPay Server ei kerää mitään tietoja, kaupan omistaja saattaa haluta lisätä mukautetun lomakkeen kassakokemukseensa; näin kaupan omistaja voi kerätä lisätietoja asiakkaaltaan. BTCPay Serverin Lomakkeenrakentaja koostuu kahdesta osasta, visuaalisesta ja edistyneemmästä koodinäkymästä lomakkeille.
Kun luot uuden lomakkeen, BTCPay Server avaa uuden ikkunan, jossa pyydetään perustietoja siitä, mitä uudella lomakkeellasi halutaan pyytää. Aluksi kauppiaan on annettava selvä nimi uudelle lomakkeelleen, tätä nimeä EI voi muuttaa sen asettamisen jälkeen.
![kuva](assets/en/68.webp)

Kun kauppias on antanut lomakkeelle nimen, voit myös kytkeä vaihtoehdon "Salli lomakkeen käyttö julkisesti" päälle, jolloin se muuttuu vihreäksi. Tämä mahdollistaa lomakkeen käytön kaikissa asiakkaalle näkyvissä paikoissa. Esimerkiksi, jos kauppias luo erillisen laskun ei myyntipisteen kautta, hän saattaa silti haluta kerätä tiedot asiakkaalta; tämän vaihtoehdon kytkeminen päälle mahdollistaa tietojen keräämisen.

![kuva](assets/en/69.webp)

Jokainen lomake alkaa vähintään yhdellä Uusi lomakekenttä -vaihtoehdolla. Kauppias voi valita kentän tyypin;

- Teksti
- Numero
- Salasana
- Sähköposti
- URL
- Puhelinnumerot
- Päivämäärä
- Piilotetut kentät
- Kenttäryhmä
- Tekstialue avoimille kommenteille.
- Valintavalitsin

Jokainen tyyppi sisältää täytettävät parametrit. Kauppias voi asettaa ne mielensä mukaan. Ensimmäisen luodun kentän alapuolelle kauppiaat voivat lisätä uusia kenttiä tähän yhteen lomakkeeseen.

![kuva](assets/en/70.webp)

#### Edistyneet mukautetut lomakkeet

BTCPay Server mahdollistaa myös lomakkeiden rakentamisen koodissa. Erityisesti JSON-muodossa. Editorin sijaan kauppiaat voivat klikata KOODI-painiketta editorin vieressä ja siirtyä lomakkeidensa koodiin. Kentän määrittelyssä voidaan asettaa vain seuraavat kentät; kenttien arvot tallennetaan laskun metatietoihin:

| Kenttä                | Kuvaus                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .fields.constant      | Jos tosi, .value on asetettava lomakkeen määrittelyssä, eikä käyttäjä voi muuttaa kentän arvoa. (esimerkki: lomakkeen määrittelyn versio)                                                                                                                                                                                                                                                                                                                            |
| .fields.type          | HTML-syötetyyppi teksti, radio, valintaruutu, salasana, piilotettu, painike, väri, päivämäärä, datetime-local, kuukausi, viikko, aika, sähköposti, numero, vaihtelu, haku, url, valinta, puhelin                                                                                                                                                                                                                                                                     |
| .fields.options       | Jos .fields.type on select, valittavissa olevien arvojen luettelo                                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.options.text  | Tämän vaihtoehdon näytettävä teksti                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.options.value | Kentän arvo, jos tämä vaihtoehto on valittu                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.type=fieldset | Luo HTML-kenttäryhmän lasten .fields.fields ympärille (katso alla)                                                                                                                                                                                                                                                                                                                                                                                                   |
| .fields.name          | Kentän JSON-ominaisuuden nimi, kuten se näkyy laskun metatiedoissa                                                                                                                                                                                                                                                                                                                                                                                                   |
| .fields.value         | Kentän oletusarvo                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.required      | jos tosi, kenttä on pakollinen                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| .fields.label         | Kentän otsikko                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| .fields.helpText      | Lisäteksti, joka tarjoaa selityksen kentälle.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| .fields.fields        | Voit järjestää kenttäsi hierarkiaan, jolloin alikentät voidaan sijoittaa laskun metatietoihin. Tämä rakenne voi auttaa sinua järjestämään ja hallinnoimaan kerättyjä tietoja paremmin, mikä tekee niiden käyttämisestä ja tulkitsemisesta helpompaa. Esimerkiksi, jos sinulla on lomake, joka kerää asiakastietoja, voit ryhmitellä kentät yläkentän alle, jota kutsutaan asiakkaaksi. Tässä yläkentässä saattaisi olla alikenttiä kuten nimi, sähköposti ja osoite. |

Kentän nimi edustaa JSON-ominaisuuden nimeä, joka tallentaa käyttäjän antaman arvon laskun metatietoihin. Jotkin tunnetut nimet voidaan tulkita ja muuttaa laskun asetuksia.

| Kentän nimi      | Kuvaus          |
| ---------------- | --------------- |
| invoice_amount   | Laskun summa    |
| invoice_currency | Laskun valuutta |

Voit esitäyttää laskun kenttiä automaattisesti lisäämällä kyselymerkkijonoja lomakkeen URL-osoitteeseen, kuten "?your_field=arvo".

Tässä joitakin käyttötapauksia tälle ominaisuudelle:

- Käyttäjän syötteen avustaminen: Esitäytä kentät tunnetuilla asiakastiedoilla, jotta heidän on helpompi täyttää lomake. Esimerkiksi, jos tiedät jo asiakkaan sähköpostiosoitteen, voit esitäyttää sähköpostikentän säästääksesi heidän aikaansa.
- Personointi: Mukauta lomake asiakkaan mieltymysten tai segmentoinnin perusteella. Esimerkiksi, jos sinulla on erilaisia asiakastasoja, voit esitäyttää lomakkeen relevantilla tiedolla, kuten heidän jäsenyystasonsa tai erityistarjouksensa.
- Seuranta: Seuraa asiakaskäyntien lähdettä käyttämällä piilotettuja kenttiä ja esitäytettyjä arvoja. Esimerkiksi voit luoda linkkejä, joissa on esitäytettyjä utm_media arvoja kullekin markkinointikanavalle (esim. Twitter, Facebook, Sähköposti). Tämä auttaa analysoimaan markkinointiponnistelujesi tehokkuutta.
- A/B-testaus: Esitäytä kentät eri arvoilla testataksesi eri lomakeversioita, jotta voit optimoida käyttäjäkokemuksen ja konversioasteet.

### Taitojen Yhteenveto

Tässä osiossa opit seuraavat:

- Välilehtien asettelun ja toiminnot Kaupan Asetuksissa
- Lukuisia vaihtoehtoja hienosäätääksesi perustana olevien vaihtokurssien, osamaksujen, pienien alimaksujen ja muun käsittelyä.
- Mukauta kassan ulkoasua, mukaan lukien hintariippuvainen pääketju vs. Lightningin mahdollistaminen laskuissa.
- Hallitse kaupan pääsyn tasoa ja oikeuksia eri rooleissa.
- Määritä automaattiset sähköpostit ja niiden laukaisijat
- Luo mukautettuja lomakkeita keräämään lisätietoja asiakkaalta kassalla.

### Tietämyksen Arvioinnit

#### KA Arvostelu

Mikä on ero Kaupan Asetusten ja Palvelimen Asetusten välillä?

#### KA Hypoteettinen

Kuvaile joitakin vaihtoehtoja, joita saatat valita Kassan Ulkoasu > Laskun Asetuksissa, ja miksi.

## BTCPay Server - Palvelimen asetukset

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server koostuu kahdesta erilaisesta asetusnäkymästä. Toinen on omistettu Kaupan asetuksille ja toinen Palvelimen asetuksille. Jälkimmäinen on saatavilla vain, jos olet Palvelimen ylläpitäjä eikä kaupan omistajille. Palvelimen ylläpitäjät voivat lisätä käyttäjiä, luoda mukautettuja rooleja, määrittää sähköpostipalvelimen, asettaa käytäntöjä, suorittaa ylläpitotehtäviä, tarkistaa kaikki BTCPay Serveriin liitetyt palvelut, ladata tiedostoja palvelimelle tai tarkistaa Lokit.

### Käyttäjät

Kuten aiemmin mainittiin, Palvelimen Ylläpitäjät voivat kutsua käyttäjiä palvelimelleen lisäämällä heidät Käyttäjät-välilehteen.

### Palvelinlaajuiset mukautetut Roolit

BTCPay Server tuntee kahdenlaisia mukautettuja rooleja, kauppakohtaiset mukautetut roolit ja palvelinlaajuiset Mukautetut roolit BTCPay Serverin asetuksissa. Molemmilla on samankaltainen joukko oikeuksia; kuitenkin, jos asetettu BTCpay Serverin Asetukset - Roolit -välilehden kautta, sovellettu rooli on palvelinlaajuinen ja soveltuu useisiin kauppoihin. Huomaa "Palvelinlaajuinen" tagi mukautetuissa rooleissa Palvelimen asetuksissa.

### Palvelinkohtaiset mukautetut roolit

Palvelinkohtaisen mukautetun roolin oikeudet:

- Muokkaa myymälöitäsi.
- Hallinnoi myymälöihisi linkitettyjä vaihtotilejä.
  - Katso myymälöihisi linkitettyjä vaihtotilejä.
- Hallinnoi vetomaksujasi.
- Luo vetomaksuja.
  - Luo hyväksymättömiä vetomaksuja.
- Muokkaa laskuja.
  - Katso laskuja.
  - Luo lasku.
  - Luo laskuja myymälöihisi liitetyistä salamaverkon solmuista.
- Katso myymälöitäsi.
  - Katso laskuja.
  - Katso maksupyyntöjäsi.
  - Muokkaa myymälöiden web-koukkuja.
- Muokkaa maksupyyntöjäsi.
  - Katso maksupyyntöjäsi.
- Käytä myymälöihisi liitettyjä salamaverkon solmuja.
  - Katso myymälöihisi liitettyjä salamaverkon laskuja.
  - Luo laskuja myymälöihisi liitetyistä salamaverkon solmuista.
- Talleta varoja myymälöihisi linkitettyihin vaihtotileihin.
- Nosta varoja vaihtotileiltä myymälääsi.
- Käy kauppaa myymäläsi vaihtotileillä.

**!?Huomio!?**

Kun rooli on luotu, nimi on kiinteä eikä sitä voi muuttaa muokkaustilassa.

### Sähköposti

Palvelinkohtaiset sähköpostiasetukset ovat samankaltaiset kuin myymäläkohtaiset sähköpostiasetukset. Tämä asetus kuitenkin käsittelee paitsi myymälöiden tai ylläpitäjän lokien laukaisijoita. Tämä sähköpostiasetus mahdollistaa myös salasanan palauttamisen BTCPay Serverissa kirjautumisen yhteydessä. Se toimii samalla tavalla kuin myymäläkohtaiset asetukset; ylläpitäjät voivat nopeasti täyttää sähköpostiparametrinsa, syöttää sähköpostitunnuksensa, ja palvelin voi nyt lähettää sähköposteja.

### Käytännöt

BTCPay Serverin käytäntöjen ylläpitäjät voivat asettaa joitakin asetuksia aiheista kuten Olemassa olevien käyttäjien asetukset, Uusien käyttäjien asetukset, Ilmoitusasetukset ja Ylläpitoasetukset. Nämä on tarkoitettu rekisteröimään uusia käyttäjiä joko ylläpitäjänä tai tavallisina käyttäjinä tai jopa piilottamaan BTCPay Serverin hakukoneilta lisäämällä palvelimen otsikkoon.

#### Olemassa olevien käyttäjien asetukset

Täällä saatavilla olevat vaihtoehdot ovat erillään mukautetuista rooleista. Nämä lisäoikeudet saattavat tehdä myymälän tai myymälän omistajan alttiiksi hyökkäyksille. Olemassa oleville käyttäjille voidaan lisätä käytäntöjä:

- Salli ei-ylläpitäjien käyttää sisäistä salamaverkon solmua myymälöissään.
  - Tämä mahdollistaisi myymälän omistajien käyttää palvelimen ylläpitäjän salamaverkon solmua ja siten hänen varojaan! Varo, tämä ei ole ratkaisu salamaverkon käyttöoikeuden antamiseen.
- Salli ei-ylläpitäjien luoda kuumia lompakoita myymälöihinsä.
  - Tämä mahdollistaisi kenelle tahansa tilin omistavalle henkilölle BTCPay Server -instanssissasi luoda kuumia lompakoita ja tallentaa niiden palautuskoodin ylläpitäjän palvelimelle. Tämä saattaisi tehdä ylläpitäjästä vastuullisen kolmansien osapuolien varojen säilyttämisestä!
- Salli ei-ylläpitäjien tuoda kuumia lompakoita myymälöihinsä.
  - Samankaltainen aiheeseen kuin kuumien lompakoiden luominen, tämä käytäntö sallii kuumien lompakoiden tuonnin, samoilla vaaroilla mainittuna kuumien lompakoiden luomisosiossa.

#### Uusien käyttäjien asetukset

Voimme asettaa joitakin tärkeitä asetuksia hallitaksemme palvelimelle saapuvia uusia käyttäjiä. Voimme asettaa vahvistussähköpostin uusille rekisteröinneille, poistaa käytöstä uusien käyttäjien luomisen kirjautumisnäytössä ja rajoittaa ei-ylläpitäjien pääsyä käyttäjän luontiin API:n kautta.

- Vaadi vahvistussähköposti rekisteröityessä.
  - Palvelimen ylläpitäjän on asetettava sähköpostipalvelin!
- Poista käytöstä uusien käyttäjien rekisteröinti palvelimella
- Estä ei-ylläpitäjien pääsy käyttäjän luontiin API-päätepisteessä.

Oletuksena BTCPay Server on ottanut käyttöön Uusien käyttäjien rekisteröinnin poistamisen käytöstä ja kytkenyt pois ei-ylläpitäjien pääsyn käyttäjän luontiin API-päätepisteessä. Tämä on turvallisuusnäkökulmasta, jotta mikään satunnainen henkilö, joka saattaa löytää BTCPay-kirjautumisen palvelimeltasi, ei voi alkaa luomaan tilejä.

#### Ilmoitusasetukset

![image](assets/en/76.webp)

#### Ylläpitoasetukset

BTCPay Server on avoimen lähdekoodin projekti, joka elää GitHubissa. Aina kun BTCPay Server julkaisee uuden version ohjelmistosta, ylläpitäjille voidaan ilmoittaa, että uusi versio on saatavilla. Ylläpitäjät saattavat myös haluta estää hakukoneita (google, yahoo, duckduckgo) indeksoimasta BTCPay Serverin verkkotunnusta. Koska BTCPay Server on FOSS, kehittäjät ympäri maailmaa saattavat haluta luoda uusia ominaisuuksia; BTCPay Serverillä on kokeellinen ominaisuus, joka kun kytketään päälle, ylläpitäjä voi käyttää tuotantoon tarkoitettuja ominaisuuksia vielä puhtaasti testaustarkoituksiin.

- Tarkista julkaisut GitHubissa ja ilmoita, kun uusi BTCPay Server -versio on saatavilla.
- Estä hakukoneita indeksoimasta tätä sivustoa
- Ota käyttöön kokeelliset ominaisuudet.

![image](assets/en/77.webp)

#### Lisäosat

BTCPay Server voi lisätä lisäosia ja laajentaa ominaisuusvalikoimaansa. Lisäosat ladataan oletusarvoisesti BTCPay Serverin plugin-builder-repositoriosta. Ylläpitäjä voi kuitenkin halutessaan nähdä lisäosat esijulkaisutilassa, ja jos lisäosan kehittäjä sallii sen, palvelimen ylläpitäjä voi nyt asentaa lisäosien beta-versioita.

![image](assets/en/78.webp)

##### Mukautusasetukset

Vakio BTCPay Server -asennus on saavutettavissa asennuksen yhteydessä määritetyn verkkotunnuksen kautta. Palvelimen ylläpitäjä voi kuitenkin uudelleenmäärittää juuriverkkotunnuksen ja näyttää jonkin luoduista sovelluksista tietyssä kaupassa. Palvelimen ylläpitäjä voi myös määrittää tiettyjä verkkotunnuksia tiettyihin sovelluksiin.

- Näytä sovellus verkkosivuston juuressa
  - Näyttää mahdollisten juuriverkkotunnuksessa näytettävien sovellusten luettelon.

![image](assets/en/79.webp)

- Määritä tiettyjä verkkotunnuksia tiettyihin sovelluksiin.
  - Kun klikkaat asettaaksesi tietyn verkkotunnuksen tietyille sovelluksille, ylläpitäjä voi määrittää niin monta verkkotunnusta tietyille sovelluksille kuin tarvitaan.

![image](assets/en/80.webp)

#### Lohkotutkijat

BTCPay Server toimii oletusarvoisesti mempool.space -lohkotutkijan kanssa transaktioita varten. Kun BTCPay Server luo uuden laskun ja siihen liittyy transaktio, kaupan omistaja voi klikata avatakseen transaktion; BTCPay Server osoittaa oletusarvoisesti mempool.spaceen lohkotutkijana; palvelimen ylläpitäjä voi muuttaa tätä omien mieltymystensä mukaan.

![image](assets/en/81.webp)

### Palvelut

BTCPay Serverin asetukset: Palvelut-välilehti on yleiskatsaus komponenteista, joita BTCPay Server käyttää. BTCPay Serverin tarjoamat palvelut voivat vaihdella käyttöönoton menetelmästä riippuen.

BTCPay Serverin ylläpitäjä voi klikata "Näe tiedot" kunkin palvelun takana avatakseen sen ja asettaakseen tiettyjä asetuksia.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay tarjoaa LND:n GRPC-palvelun ulkopuoliseen käyttöön; löydät yhteystiedot tästä erityisestä asetusvalikosta; yhteensopivat lompakot on lueteltu täällä. BTCPay Server tarjoaa myös QR-koodin yhteyden muodostamiseen, skannaa ja sovella mobiililompakossa.

Palvelimen ylläpitäjät voivat avata lisätietoja nähdäkseen;

- Isäntätiedot
- SSL:n käyttö
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Cipher suite (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay tarjoaa LND:n REST-palvelun ulkopuoliseen käyttöön; löydät yhteystiedot täältä; yhteensopivat lompakot on lueteltu täällä. Yhteensopivien lompakoiden joukossa ovat Joule, Alby ja ZeusLN. BTCPay Server tarjoaa QR-koodin yhteyden muodostamiseen, skannaa ja sovella yhteensopivassa lompakossa.

- REST Uri
- Macaroon
- AdminMacaroon- InvoiceMacaroon
- ReadonlyMacaroon

#### LND Seed Backup

LND seed -varmuuskopio on hyödyllinen, jos haluat palauttaa varasi LND-lompakostasi palvelimen korruptoitumisen sattuessa. Koska Lightning-node on Hot-wallet, löydät luottamukselliset seed-tiedot tältä sivulta.

LND dokumentoi palautusprosessin. Katso https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md dokumentaatiosta.

#### Ride The Lightning

Ride the Lightning on avoimen lähdekoodin ohjelmistona rakennettu Lightning-noden hallintatyökalu. BTCPay Server käyttää RTL:ää Lightning-noden hallintakomponenttina pinossaan. BTCPay Serverin ylläpitäjät voivat saavuttaa RTL:n palvelimen asetusten kautta - Palvelut-välilehdeltä tai napsauttamalla Lightning-lompakkoa.

#### Full node P2P

Palvelimen ylläpitäjät saattavat haluta yhdistää Bitcoin-nodensa mobiililompakkoon. Tällä sivulla esitetään tietoja, miten yhdistää etäyhteydellä full nodeen P2P-protokollan kautta. Kirjan kirjoitushetkellä BTCPay Server listaa Blockstream Greenin ja Wasabi-lompakon yhteensopiviksi lompakoiksi. BTCPay Server antaa QR-koodin yhteyden muodostamiseen, skannaa ja sovella yhteensopivaan lompakkoon.

#### Full node RPC

Tällä sivulla esitetään tietoja, miten yhdistää etäyhteydellä full nodeen RPC-protokollan kautta.

#### SSH

SSH:ta käytetään ylläpitotarkoituksiin. BTCPay Server näyttää alkuperäisen yhteyskomennon palvelimeesi ja SSH-julkiset avaimet, jotka on valtuutettu yhdistämään palvelimeesi. Palvelimen ylläpitäjät saattavat haluta kytkeä SSH-muutokset pois päältä BTCPay Serverin käyttöliittymän kautta.

#### Dynaaminen DNS

Dynaaminen DNS mahdollistaa vakaa DNS-nimen osoittamisen palvelimeesi, vaikka IP-osoitteesi muuttuisi säännöllisesti. Tämä on suositeltavaa, jos isännöit BTCPay Serveria kotona ja haluat selkeän verkkotunnuksen päästäksesi palvelimeesi.

Huomaa, että sinun on määritettävä NAT ja BTCPay Server -asennuksesi oikein saadaksesi HTTPS-sertifikaatin.

### Teema

BTCPay Server tarjoaa vakiona kaksi teemaa: Vaalea ja Tumma tila. Näiden välillä voi vaihtaa napsauttamalla Tilini vasemmassa alakulmassa ja vaihtelemalla Tumma teema tai Vaalea teema. BTCPay Serverin ylläpitäjät voivat lisätä oman teemansa tarjoamalla mukautetun CSS-teeman.

Ylläpitäjät voivat laajentaa Vaalea/Tumma teemaa lisäämällä oman mukautetun CSS:nsä tai asettamalla oman teemansa täysin mukautetuksi.

![kuva](assets/en/83.webp)

#### Palvelimen Brändäys

Palvelimen ylläpitäjät voivat muuttaa BTCPay Serverin brändäystä asettamalla yrityksesi laajuisen brändäyksen. Koska BTCPay Server on FOSS, palvelimen ylläpitäjät voivat white label -merkitä ohjelmiston ja muuttaa sen ulkonäköä sopimaan liiketoimintaansa.

![kuva](assets/en/84.webp)

### Ylläpito

Palvelimen ylläpitäjänä käyttäjäsi odottavat sinun pitävän hyvää huolta palvelimesta. BTCPay Serverin Ylläpito-välilehdellä ylläpitäjä voi suorittaa joitakin olennaisia ylläpitotoimia. Aseta verkkotunnus BTCPay Server -instanssille, Käynnistä uudelleen tai puhdista palvelin. Mahdollisesti tärkeintä, suorita päivitykset.

BTCPay Server on avoimen lähdekoodin projekti ja päivittyy usein. Jokainen uusi julkaisu ilmoitetaan joko BTCPay Serverin ilmoitusten tai virallisten kanavien kautta, joiden kautta BTCPay Server viestii.

![kuva](assets/en/85.webp)

#### Verkkotunnus

Kun BTCPay Server on asennettu, ylläpitäjä saattaa haluta vaihtaa alkuperäisestä verkkotunnuksestaan. Ylläpito-välilehdellä ylläpitäjä voi vaihtaa verkkotunnuksen. Napsauttamalla vahvista ja asettamalla asianmukaiset DNS-tietueet verkkotunnukseen, BTCPay Server päivittyy ja käynnistyy uudelleen palatakseen uuteen verkkotunnukseen.

![kuva](assets/en/86.webp)

#### Uudelleenkäynnistys

Käynnistä BTCPay Server ja siihen liittyvät palvelut uudelleen.

![kuva](assets/en/87.webp)

#### Puhdistus

BTCPay Server toimii Docker-komponenttien kanssa; päivitysten yhteydessä voi jäädä jäljelle Docker-kuvia, väliaikaistiedostoja jne. Palvelimen ylläpitäjät voivat siivota nämä ja vapauttaa tilaa ympäristössään suorittamalla Puhdistus-skriptin.
![kuva](assets/en/88.webp)

#### Päivitys

Mahdollisesti tärkein vaihtoehto Ylläpito-välilehdessä. BTCPay Server on yhteisön rakentama, ja siksi sen päivityssyklit ovat tiheämpiä kuin useimmissa ohjelmistotuotteissa. Kun BTCPay Serverillä on uusi julkaisu, ylläpitäjät saavat ilmoituksen ilmoituskeskuksessaan. Päivityspainiketta napsauttamalla BTCPay Server tarkistaa GitHubista uusimman julkaisun, päivittää palvelimen ja käynnistää sen uudelleen. Ennen päivittämistä palvelimen ylläpitäjien neuvotaan aina lukemaan julkaisutiedot, jotka jaetaan BTCPay Serverin virallisten kanavien kautta.

![kuva](assets/en/89.webp)

### Lokit

Ongelman kohtaaminen ei ole koskaan hauskaa. Tässä asiakirjassa selitetään yleisimmät työnkulut ja vaiheet ongelmasi tehokkaaseen tunnistamiseen ja ratkaisemiseen itse tai yhteisön avulla.

Ongelman tunnistaminen on ratkaisevan tärkeää.

#### Ongelman toistaminen

Ensinnäkin yritä määrittää, milloin ongelma tapahtuu. Yritä toistaa ongelma. Yritä päivittää ja käynnistää palvelimesi uudelleen varmistaaksesi, että voit toistaa ongelmasi. Jos se kuvaa ongelmaasi paremmin, ota näyttökuva.

##### Palvelimen päivittäminen

Tarkista BTCPay Serverin versionsi, jos se on paljon vanhempi kuin BTCPay Serverin [uusin versio](https://github.com/btcpayserver/btcpayserver/releases). Palvelimen päivittäminen saattaa ratkaista ongelman.

##### Palvelimen uudelleenkäynnistäminen

Palvelimen uudelleenkäynnistäminen on helppo tapa ratkaista monia yleisimpiä BTCPay Serverin ongelmia. Sinun saattaa tarvita SSH-yhteys palvelimeesi sen uudelleenkäynnistämiseksi.

##### Palvelun uudelleenkäynnistäminen

Joissakin tapauksissa saattaa riittää, että käynnistät uudelleen tietyn palvelun BTCPay Server -asennuksessasi. Esimerkiksi lets encrypt -säiliön uudelleenkäynnistäminen SSL-sertifikaatin uusimiseksi.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Käytä docker ps -komentoa löytääksesi eri palvelun nimen, jonka haluaisit käynnistää uudelleen.

#### Lokien läpikäyminen

Lokit voivat tarjota olennaista tietoa. Seuraavissa kappaleissa kuvaamme, miten saat lokitietoja BTCPayn eri osista.

##### BTCPay Lokit

Versiosta v1.0.3.8 lähtien voit helposti päästä käsiksi BTCPay Serverin lokeihin etupuolelta. Jos olet palvelimen ylläpitäjä, mene Palvelimen Asetukset > Lokit ja avaa lokitiedosto. Jos et tiedä, mitä tietty virhe lokeissa tarkoittaa, mainitse se vianmäärityksessä.

Jos haluat yksityiskohtaisempia lokeja ja käytät Docker-asennusta, voit tarkastella tiettyjen Docker-säiliöiden lokeja komentoriviltä. Katso nämä [ohjeet ssh-yhteyden muodostamiseksi](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) BTCPay-instanssiin, joka toimii VPS:llä.

Seuraavalla sivulla yleinen lista säiliönimistä, joita käytetään BTCPay Serverissä.

Suorita alla olevat komennot tulostaaksesi lokit säiliönimen perusteella. Korvaa säiliön nimi nähdäksesi muiden säiliöiden lokit.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Lokit        | Säiliön Nimi                      |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker

LND-lokien tarkastelu Dockeria käyttäen onnistuu muutamalla tavalla. Kirjaudu ensin root-käyttäjänä:

```bash
sudo su -
Siirry oikeaan hakemistoon:
cd btcpayserver-docker
# Etsi kontin name:
docker ps
Tulosta lokit kontin nimellä:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Vaihtoehtoisesti voit nopeasti tulostaa lokit käyttämällä kontin ID:tä (tarvitaan vain ensimmäiset uniikit ID-merkit, kuten kaksi vasemmanpuoleisinta merkkiä):

```bash
docker logs 'lisää konttisi ID'
```

Jos tarvitset jostain syystä enemmän lokeja

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Näet jotakin tällaista

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Päästäksesi käsiksi pakkaamattomiin lokeihin, käytä `cat lnd.log` tai jos haluat toisen, käytä `cat lnd.log.15`.

Päästäksesi käsiksi pakattuihin lokeihin `.gzip`-muodossa, käytä `gzip -d lnd.log.16.gz` (tässä tapauksessa käsittelemme `lnd.log.16.gz`). Tämän pitäisi antaa sinulle uusi tiedosto, jossa voit tehdä `cat lnd.log.16`. Jos yllä oleva ei toimi, saatat tarvita asentaa gzip ensin komennolla `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Etsi c-lightning kontin ID.
docker logs 'lisää konttisi ID tähän'
```

vaihtoehtoisesti käytä tätä

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Voit myös saada lokitietoja c-lightning cli-komennolla.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Bitcoin Node Lokit

Bitcoind-konttisi lokien tarkastelun lisäksi voit käyttää mitä tahansa [bitcoin-cli komentoja](https://developer.bitcoin.org/reference/rpc/index.html)

[(avautuu uudessa ikkunassa)](https://developer.bitcoin.org/reference/rpc/index.html) saadaksesi tietoja bitcoin-nodestasi. BTCPay sisältää skriptin, joka mahdollistaa kommunikoinnin Bitcoin-nodesi kanssa helposti.

btcpayserver-docker-kansiossa, saat blockchain-tiedot nodestasi käyttäen:

```bash
bitcoin-cli.sh getblockchaininfo
```

### Tiedostot

BTCPay Serverilla on paikallinen tiedostojärjestelmä ja se lataa kaupan (tuote) omaisuutta, logoja ja brändäystä suoraan palvelimelle. Palvelimen tiedostojärjestelmä on vain palvelimen ylläpitäjien saavutettavissa; kaupan omistajat voivat ladata omat logonsa/brändäyksensä kaupan tasolla.
Kun palvelimen ylläpitäjä on Tiedostovarasto-välilehdessä, on mahdollista suoraan ladata palvelimellesi tai vaihtaa tiedostovaraston tarjoajaa paikalliseen tiedostojärjestelmään tai Azure Blob Storageen.

![kuva](assets/en/90.webp)

![kuva](assets/en/91.webp)

### Taitojen Yhteenveto

Tässä osiossa opit seuraavat asiat:

- Erot kaupan ja palvelimen asetuksissa, erityisesti käyttäjien, roolien ja sähköpostien osalta
- Aseta palvelinlaajuiset politiikat Lightningin tai Bitcoinin hot walletin käytölle ja luomiselle, uusien käyttäjien rekisteröinnille ja sähköposti-ilmoituksille.
- Miten lisätä mukautettuja teemoja (sen sijaan, että käytettäisiin vain yksinkertaisia vaaleita/pimeitä vaihtoehtoja) sekä luoda mukautettuja logoja
- Suorita yksinkertaisia palvelimen ylläpitotehtäviä GUI:n kautta
- Vianmääritys, mukaan lukien Docker-säiliöiden tai solmusi yksityiskohtien hankkiminen
- Hallitse tiedostovarastoa

### Tiedon Arviointi

#### KA Käsitteellinen Katsaus

Mikä on ero roolien määrittelyssä palvelimen kautta verrattuna kaupan asetuksiin, ja kuvaile potentiaalinen käyttötarkoitus toiselle yli toisen?

#### KA Käytännön Katsaus

Kuvaile mahdollisia käyttötapauksia, jotka ovat mahdollisia Politiikat-välilehdessä.

#### KA Käytännön Katsaus

Kuvaile toimia, joita ylläpitäjä saattaa säännöllisesti tehdä Ylläpito-välilehdessä.

## BTCPay Server - Maksut

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Lasku on asiakirja, jonka myyjä laatii ostajalle maksun keräämiseksi.

BTCPay Serverissa lasku edustaa asiakirjaa, joka on maksettava määritellyssä aikavälissä kiinteällä vaihtokurssilla. Laskuilla on viimeinen voimassaolopäivä, koska ne lukitsevat vaihtokurssin määrätyksi ajaksi suojatakseen vastaanottajaa hintavaihteluilta.

BTCPay Serverin ydin on toimia Bitcoin-laskujen hallintajärjestelmänä. Lasku on olennainen työkalu vastaanotetun maksun seurantaan ja hallintaan.

Ellet käytä sisäänrakennettua [Wallet](https://docs.btcpayserver.org/Wallet/) -lompakkoa maksujen manuaaliseen vastaanottoon, kaikki kaupan sisällä tehdyt maksut näytetään Laskut-sivulla. Tämä sivu lajittelee maksut päivämäärän mukaan ja on keskeinen osa laskujen hallintaa ja maksuongelmien selvittämistä.

![kuva](assets/en/92.webp)

### Yleistä

#### Laskun tilat

Alla oleva taulukko luettelee ja kuvailee BTCPayn standardilaskun tiloja ja ehdottaa yleisiä toimenpiteitä. Toimenpiteet ovat vain suosituksia. Käyttäjien on määriteltävä parhaat toimintatavat omien käyttötapauksiensa ja liiketoimintansa kannalta.

| Laskun Tila                    | Kuvaus                                                                                                                           | Toimenpide                                                                                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Uusi                           | Ei maksettu, laskun aikaraja ei ole vielä umpeutunut                                                                             | Ei toimenpiteitä                                                                                                                                                    |
| Uusi (paidPartial)             | Maksettu, ei täysin, laskun aikaraja ei ole vielä umpeutunut                                                                     | Ei toimenpiteitä                                                                                                                                                    |
| Vanhentunut                    | Ei maksettu, laskun aikaraja umpeutunut                                                                                          | Ei toimenpiteitä                                                                                                                                                    |
| Vanhentunut (paidPartial) \*\* | Maksettu, ei täydessä määrässä, ja umpeutunut                                                                                    | Ota yhteyttä ostajaan järjestääksesi palautuksen tai pyytääksesi heitä maksamaan erääntyneet maksut. Vaihtoehtoisesti merkitse lasku selvitettyksi tai mitätöidyksi |
| Vanhentunut (paidLate)         | Maksettu, täydessä määrässä, laskun aikarajan jälkeen                                                                            | Ota yhteyttä ostajaan järjestääksesi palautuksen tai käsittele tilaus, jos myöhäiset vahvistukset hyväksytään.                                                      |
| Settled (paidOver)             | Maksettu laskun määrää suurempi summa, selvitetty, saatu riittävä määrä vahvistuksia                                             | Ota yhteyttä ostajaan järjestääksesi ylimääräisen summan palautuksen, tai odota vaihtoehtoisesti, että ostaja ottaa sinuun yhteyttä                                 |
| Processing                     | Maksettu täysimääräisesti, mutta ei ole saanut riittävää määrää vahvistuksia kaupan asetuksissa määritellyllä tavalla            | Ota yhteyttä ostajaan järjestääksesi ylimääräisen summan palautuksen, tai odota vaihtoehtoisesti, että ostaja ottaa sinuun yhteyttä                                 |
| Processing (paidOver)          | Maksettu laskun määrää suurempi summa, ei ole saanut riittävää määrää vahvistuksia                                               | Odota selvitystä, sitten ota yhteyttä ostajaan järjestääksesi ylimääräisen summan palautuksen, tai odota vaihtoehtoisesti, että ostaja ottaa sinuun yhteyttä        |
| Settled                        | Maksettu täysimääräisesti, saatu riittävä määrä vahvistuksia kaupassa                                                            | Toteuta tilaus                                                                                                                                                      |
| Settled (marked)               | Tila manuaalisesti muutettu selvitettyksi käsittelyssä tai virheellisessä tilassa                                                | Kaupan ylläpitäjä on merkinnyt maksun selvitetyksi                                                                                                                  |
| Invalid\*                      | Maksettu, mutta ei ole saanut riittävää määrää vahvistuksia kaupan asetuksissa määritellyssä ajassa                              | Tarkista transaktio lohkoketjun tutkijassa, jos se on saanut riittävät vahvistukset, merkitse selvitetyksi                                                          |
| Invalid (marked)               | Tila manuaalisesti muutettu virheelliseksi selvitetystä tai vanhentuneesta tilasta                                               | Kaupan ylläpitäjä on merkinnyt maksun virheelliseksi                                                                                                                |
| Invalid (paidOver)             | Maksettu laskun määrää suurempi summa, mutta ei ole saanut riittävää määrää vahvistuksia kaupan asetuksissa määritellyssä ajassa | Tarkista transaktio lohkoketjun tutkijassa, jos se on saanut riittävät vahvistukset, merkitse selvitetyksi                                                          |

#### Laskun tiedot

Laskun tiedot -sivu sisältää kaikki laskuun liittyvät tiedot.

Laskutiedot luodaan automaattisesti perustuen laskun tilaan, vaihtokurssiin jne. Tuotetiedot luodaan automaattisesti, jos lasku on luotu tuotetietojen kanssa, kuten Point of Sale -sovelluksessa.

#### Laskujen suodattaminen

Laskuja voidaan suodattaa nopeiden suodattimien avulla, jotka sijaitsevat hakupainikkeen vieressä tai edistyneiden suodattimien avulla, jotka voidaan ottaa käyttöön napsauttamalla (Apua) -linkkiä yläosassa. Käyttäjät voivat suodattaa laskuja kaupan, tilausnumeron, tuotenumeron, tilan tai päivämäärän mukaan.

#### Laskujen vienti

BTCPay Serverin laskut voidaan viedä CSV- tai JSON-muodossa. Lisätietoja laskujen viennistä ja kirjanpidosta.

#### Laskun palauttaminen

Jos haluat mistä tahansa syystä tehdä palautuksen, voit helposti luoda palautuksen laskunäkymästä.

#### Laskujen arkistointi

BTCPay Serverin "ei osoitteen uudelleenkäyttö" -ominaisuuden seurauksena on yleistä nähdä monia vanhentuneita laskuja kauppasi laskusivulla. Piilottaaksesi ne näkymästäsi, valitse ne luettelosta ja merkitse ne arkistoiduiksi. Arkistoituina merkittyjä laskuja ei poisteta. Arkistoituun laskuun tehty maksu havaitaan edelleen BTCPay Serverissäsi (paidLate-tila). Voit milloin tahansa tarkastella kauppasi arkistoituja laskuja valitsemalla arkistoidut laskut hakusuodattimen pudotusvalikosta.

#### Oletusvaluutta

Kaupan oletusvaluutta, tämä asetettiin kaupan luontivelhossa

#### Salli kenen tahansa luoda lasku

Sinun tulisi ottaa tämä vaihtoehto käyttöön, jos haluat sallia ulkopuolisten luoda laskuja kaupassasi. Tämä vaihtoehto on hyödyllinen vain, jos käytät maksupainiketta tai jos laskutat API:n tai kolmannen osapuolen HTML-verkkosivuston kautta. PoS-sovellus on esivaltuutettu eikä tarvitse tätä toimintoa satunnaisen vierailijan avataksesi PoS-kauppasi ja luodaksesi laskun.

#### Lisää lisämaksu (verkkomaksu) laskuun

- Vain jos asiakas tekee enemmän kuin yhden maksun laskulle
- Jokaisesta maksusta
- Älä koskaan lisää verkkomaksua

#### Lasku vanhenee, jos koko summaa ei ole maksettu .. minuutin jälkeen.

Laskurin aikaraja on oletuksena asetettu 15 minuuttiin. Aikaraja on suojamekanismi volatiliteettia vastaan, sillä se lukitsee kryptovaluutan määrän krypto-fiat -kurssien mukaan. Jos asiakas ei maksa laskua määritellyssä ajassa, lasku katsotaan vanhentuneeksi. Lasku katsotaan "maksetuksi" heti, kun transaktio näkyy lohkoketjussa (0-vahvistusta), mutta "valmiiksi" kun se saavuttaa kauppiaan määrittelemän vahvistusten määrän (yleensä 1-6). Aikarajaa voi muokata.

#### Pidä lasku maksettuna, vaikka maksettu summa olisi ..% odotettua vähemmän.

Tilanteessa, jossa asiakas käyttää vaihtopalvelun lompakkoa maksamaan suoraan laskusta, vaihto ottaa pienen maksun. Tämä tarkoittaa, että tällaista laskua ei katsota täysin suoritetuksi. Laskun tilaksi tulee "osittain maksettu". Jos kauppias haluaa hyväksyä alimaksetut laskut, voit asettaa prosenttiosuuden tässä

### Pyyntöjä

Maksupyynnöt ovat ominaisuus, joka mahdollistaa BTCPay-kaupan omistajille pitkäaikaisten laskujen luomisen. Varat maksetaan maksupyynnölle käyttäen maksuhetken vaihtokurssia. Tämä mahdollistaa käyttäjien maksaa omalla ajallaan ilman tarvetta neuvotella tai varmistaa vaihtokurssit kaupan omistajan kanssa maksuhetkellä.

Käyttäjät voivat maksaa pyynnöt osamaksuina. Maksupyyntö pysyy voimassa kunnes se on maksettu kokonaan tai jos kaupan omistaja vaatii vanhentumisajan. Osoitteita ei koskaan uudelleenkäytetä. Uusi osoite luodaan joka kerta, kun käyttäjä klikkaa maksaa luodakseen laskun maksupyynnölle.

Kaupan omistajat voivat tulostaa maksupyynnöt (tai viedä laskutiedot) kirjanpitoa ja laskentaa varten. BTCPay automaattisesti merkitsee laskut Maksupyynnöiksi kauppasi laskulistalla.

#### Mukauta Maksupyynnöt

- Laskun Summa - Aseta Pyydetty Maksusumma
- Valuutta - Näytä Pyydetty Summa Fiatissa tai Kryptovaluutassa
- Maksun Määrä - Salli vain yksittäiset maksut tai osamaksut
- Vanhentumisaika - Salli maksut tiettyyn päivämäärään asti tai ilman vanhentumista
- Kuvaus - Tekstieditori, Datataulukot, Upota Kuvia & Videoita
- Ulkoasu - Väri ja Tyyli CSS-teemoilla

![kuva](assets/en/93.webp)

#### Luo Maksupyyntö

Vasemmassa valikossa, mene kohtaan Maksupyyntö ja klikkaa "Luo Maksupyyntö".

![kuva](assets/en/94.webp)

Anna Pyyntönimi, Summa, Näyttövaluutta, Liitetty Kauppa, Vanhentumisaika & Kuvaus (Valinnainen)

Valitse vaihtoehto Salli maksajan luoda laskuja heidän valuutassaan, jos haluat sallia osamaksut.

Klikkaa Tallenna & Katsele tarkastellaksesi maksupyyntöäsi.

BTCPay luo URL-osoitteen maksupyynnölle. Jaa tämä URL nähdäksesi maksupyyntösi. Tarvitsetko useita samanlaisia pyyntöjä? Voit kopioida maksupyynnöt käyttämällä Kloonaa-vaihtoehtoa päävalikossa.

![kuva](assets/en/95.webp)

**VAROITUS**

Maksupyynnöt ovat kauppakohtaisia, mikä tarkoittaa, että jokainen maksupyyntö liittyy kauppaan luomisen yhteydessä. Varmista, että sinulla on lompakko yhdistettynä kauppaasi, johon maksupyyntö kuuluu.

#### Maksettu Pyyntö

Maksaja ja pyytäjä voivat tarkastella maksupyynnön tilaa maksun lähettämisen jälkeen. Tila näkyy Maksettuna, jos maksu on vastaanotettu kokonaan. Jos vain osamaksuja on tehty, Velka näyttää jäljellä olevan summan.

![kuva](assets/en/96.webp)

#### Mukauta Maksupyynnöt

Kuvaussisältöä voidaan muokata maksupyynnön tekstieditorilla. Molemmat vaihtoehdot ovat käytettävissä, jos haluat käyttää lisäväriteemoja tai mukautettua CSS-tyyliä.
Ei-tekniset käyttäjät voivat käyttää [bootstrap-teemaa](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Lisämuokkauksia voidaan tehdä tarjoamalla lisää CSS-koodia, kuten alla näytetään.

```css
:root {
  --btcpay-font-family-base: "Source Sans Pro", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --btcpay-primary: #7d4698;
  --btcpay-primary-accent: #59316b;
  --btcpay-body-text: #333a41;
  --btcpay-body-bg: #fff;
  --btcpay-bg-tile: #f8f9fa;
}

#mainNav {
  color: white;
  background: lineaarinen-gradientti(#59316b, #331840);
}

#mainNav .btn-link {
  color: white;
}
```

### Pull-maksut

Perinteisesti vastaanottaja jakaa Bitcoin-osoitteensa tehdäkseen Bitcoin-maksun, ja lähettäjä lähettää myöhemmin rahaa tähän osoitteeseen. Tällaista järjestelmää kutsutaan Push-maksuksi, koska lähettäjä aloittaa maksun, kun taas vastaanottaja voi olla tavoittamattomissa, työntäen maksun vastaanottajalle.

Entäpä jos roolit kääntyisivät?

Entä jos sen sijaan, että lähettäjä työntäisi maksun, lähettäjä sallisi vastaanottajan vetää maksun silloin, kun vastaanottaja pitää sitä sopivana? Tämä on Pull-maksun konsepti. Tämä mahdollistaa useita uusia sovelluksia, kuten:

- Tilauspalvelu (jossa tilaaja sallii palvelun vetää rahaa joka x ajanjakson jälkeen)
- Hyvitykset (jossa kauppias sallii asiakkaan vetää hyvitysrahat lompakkoonsa, kun he pitävät sitä sopivana)
- Aikaan perustuva laskutus freelancereille (jossa palkkaaja sallii freelancerin vetää rahaa lompakkoonsa, kun aikaa raportoidaan)
- Tukeminen (jossa tukija sallii saajan vetää rahaa joka kuukausi jatkaakseen heidän työnsä tukemista)
- Automaattinen myynti (jossa pörssin asiakas sallisi pörssin vetää rahaa lompakostaan myydäkseen automaattisesti joka kuukausi)
- Saldojen nostojärjestelmä (jossa suurivolyymisen palvelun käyttäjät voivat pyytää nostoja saldostaan, palvelu voi sitten helposti ryhmitellä kaikki maksut monille käyttäjille kiintein väliajoin)

### Maksut

Maksutoiminnallisuus on sidoksissa [Pull Payments](https://docs.btcpayserver.org/PullPayments/)-toimintoon. Tämä ominaisuus mahdollistaa maksujen luomisen BTCPay:ssä. Tämä ominaisuus mahdollistaa pull-maksujen (hyvitykset, palkanmaksut tai nostot) käsittelyn.

#### Esimerkki 1: Hyvitys

Aloitetaan hyvitysesimerkillä. Asiakas on ostanut tuotteen kaupastasi, mutta valitettavasti hänen täytyy palauttaa tuote. He haluavat hyvityksen. BTCPay:ssä voit luoda [Hyvityksen](https://docs.btcpayserver.org/Refund/) ja tarjota asiakkaalle linkin varojensa vaatimiseen. Kun asiakas on antanut osoitteensa ja vaatinut varat, se näkyy Maksuissa.

Ensimmäinen tila on Odottaa hyväksyntää. Kaupan työntekijät voivat tarkistaa, jos useita odottaa, ja valinnan jälkeen käytetään Toiminnot-painiketta.

Toiminnot-painikkeen vaihtoehdot

- Hyväksy valitut maksut
- Hyväksy & lähetä valitut maksut
- Peruuta valitut maksut

Seuraava vaihe on Hyväksy & lähetä valitut maksut, koska haluamme hyvittää asiakkaalle. Tarkista Asiakkaan Osoite, näyttää summan ja haluammeko, että maksut vähennetään hyvityksestä vai ei. Kun olet tehnyt tarkistukset, jäljellä on vain transaktion allekirjoitus.
Asiakas saa nyt päivityksiä Vaatimussivulla. Hän voi seurata tapahtumaa, sillä hänelle tarjotaan linkki lohkoketjuselaimelle ja hänen tapahtumalleen. Kun tapahtuma on vahvistettu ja tila muuttuu Valmiiksi.

#### Esimerkki 2: Palkka

Keskitytään nyt palkanmaksuun, sillä se tapahtuu kaupan sisältä eikä asiakkaan pyynnöstä. Periaate on sama; käytetään Vetomaksuja. Mutta sen sijaan, että loisimme hyvityksen, teemme [Vetomaksun](https://docs.btcpayserver.org/PullPayments/).

Siirry BTCPay-palvelimesi Vetomaksut-välilehteen. Yläoikealla, klikkaa Luo Vetomaksu -nappia.

Nyt olemme luomassa Maksatusta, anna sille nimi ja haluttu summa halutussa valuutassa, täytä Kuvaus, jotta työntekijä tietää mistä on kyse. Seuraava osa on samanlainen kuin hyvityksissä. Työntekijä täyttää Kohdeosoitteen ja summan, jonka hän haluaa vaatia tästä Maksatuksesta. Hän saattaa päättää tehdä siitä 2 erillistä vaatimusta, eri osoitteisiin, tai jopa osittain vaatia lightning-verkon kautta.

Jos odottavia Maksatuksia on useita, voit niputtaa nämä allekirjoitettaviksi ja lähetettäviksi. Kun allekirjoitus on tehty, maksatukset siirtyvät Käynnissä-välilehteen ja näyttävät Tapahtuman. Kun verkko hyväksyy maksatuksen, se siirtyy Valmiiksi-välilehteen. Valmiiksi-välilehti on puhtaasti historiallisia tarkoituksia varten. Se pitää sisällään käsitellyt Maksatukset ja niihin kuuluvan tapahtuman.

### Vetomaksut

#### Käsite

Kun lähettäjä määrittää Vetomaksun, hän voi määrittää useita ominaisuuksia:

- Vetopyynnön Nimi
- Raja-arvo
- Yksikkö (kuten BTC, SAT, USD)
- Maksutavat
  - BTC On-chain
  - BTC Off-chain
- Kuvaus
- Mukautettu CSS
- Päättymispäivä (valinnainen Lightning Network BOLT11:lle)

Tämän jälkeen lähettäjä voi jakaa vetomaksun linkin avulla vastaanottajalle, joka mahdollistaa vastaanottajan luoda maksatuksen. Vastaanottaja valitsee maksatuksensa:

- Minkä maksutavan käyttää
- Minne rahat lähetetään

Kun maksatus on luotu, se lasketaan vetomaksun nykyisen jakson raja-arvoon. Lähettäjä hyväksyy sitten maksatuksen asettamalla hinnan, jolla maksatus lähetetään, ja jatkaa maksun suorittamista.

Lähettäjälle tarjoamme helppokäyttöisen tavan niputtaa useiden maksatusten maksaminen [BTCPay Sisäisestä Lompakosta](https://docs.btcpayserver.org/Wallet/).

#### Greenfield API

BTCPay-palvelin tarjoaa täyden API:n sekä lähettäjälle että vastaanottajalle, joka on dokumentoitu instanssisi `/docs`-sivulla. (tai dokumentaatiosivustolla https://docs.btcpayserver.org)

Koska API tarjoaa täyden pääsyn vetomaksuihin, lähettäjä voi automatisoida maksunsa tarpeidensa mukaan.

### Taitojen Yhteenveto

Tässä osiossa opit seuraavat:

- Syvällinen ymmärrys BTCPay-palvelimen laskun tiloista sekä toiminnoista, joita niille voidaan suorittaa
- Määrittele ja hallinnoi pidennetyn eliniän laskumekanismeja, tunnetaan pyyntöinä.
- Lisäjoustavat maksuvaihtoehdot, jotka BTCPay-palvelimen ainutlaatuinen Vetomaksu-ominaisuus avaa, erityisesti miten käsitellä hyvityksiä ja palkanmaksuja.

### Tiedon Arviointi

#### KA Käsitteellinen Katsaus

Mitkä ovat joitakin eroja laskujen ja maksupyyntöjen välillä, ja mikä voisi olla hyvä syy käyttää jälkimmäistä?

#### KA Käsitteellinen Katsaus

Miten vetomaksut laajentavat sitä, mitä tyypillisesti voidaan tehdä on-chain? Kuvaile joitakin käyttötapauksia, joita ne mahdollistavat.

## BTCPay-palvelimen Oletuslisäosat

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Oletuslaajennukset ja -sovellukset

BTCPay-palvelin sisältää vakiojoukon laajennuksia (sovelluksia), jotka voivat muuttaa BTCPay-palvelimen e-commerce-maksuyhdyskäytäväksi. Lisäyksinä ovat Point Of Sale, joukkorahoitus-alusta ja helppokäyttöinen Pay-nappi, BTCPay-palvelin muuttuu helposti käyttöönotettavaksi ratkaisuksi.

### Point Of Sale

Yksi BTCPay-palvelimen vakio laajennuksista on Point of Sale (PoS). PoS-laajennuksen avulla kaupan omistaja voi luoda Webshopin suoraan BTCPay-palvelimesta, kaupan omistajan ei tarvitse käyttää kolmannen osapuolen e-commerce-ratkaisuja Webshopin pyörittämiseen. Web-pohjainen PoS-sovellus mahdollistaa käyttäjille, joilla on kivijalkakauppoja, Bitcoinien vastaanottamisen ilman maksuja tai kolmatta osapuolta, suoraan heidän lompakkoonsa. PoS voidaan näyttää helposti tableteilla tai muilla web-selailua tukevilla laitteilla. Käyttäjät voivat helposti luoda kotinäytön pikakuvakkeen päästäkseen web-sovellukseen nopeasti.

#### Kuinka luoda uusi Point Of Sale

BTCPay-palvelin mahdollistaa kaupan omistajille Point of Sale -pisteen luomisen nopeasti monilla eri asetteluilla. BTCPay-palvelin tunnistaa, että jokainen kauppa ei ole e-commerce, eikä jokainen kauppa ole baari tai ravintola, ja se tarjoaa useita vakioasetuksia PoS:lle.

Kun kaupan omistaja klikkaa "Point of Sale" vasemmassa valikossa, BTCPay-palvelin pyytää nyt nimeä; tämä nimi näkyy vasemmassa valikossa. Klikkaa Luo luodaksesi PoS:n.

![kuva](assets/en/97.webp)

#### Päivitä vasta luotu Point of Sale

Uuden PoS:n luomisen jälkeen seuraava näyttö on Point of Sale -pisteesi päivittäminen ja tuotteiden lisääminen kauppaasi.

##### Sovelluksen nimi

Tässä annettu nimi Point of Sale -pisteellesi näkyy BTCPay-palvelimen päävalikossa.

##### Näyttöotsikko

Yleisö näkee julkisen otsikon tai nimen vierailessa kaupassasi. BTCPay-palvelin nimeää vakiona kauppasi "Teekaupaksi". Korvaa tämä omalla kauppasi nimellä.

![kuva](assets/en/98.webp)

#### Valitse Point Of Sale -tyyli

BTCPay-palvelin pystyy näyttämään Point Of Sale -pisteensä monella eri tavalla.

- Tuotelista
  - Kauppanäkymä, jossa asiakkaat voivat ostaa vain yhden tuotteen kerrallaan.
- Tuotelista ostoskorilla.
  - Kauppanäkymä, jossa asiakkaat voivat ostaa useita tuotteita kerralla ja saada ostoskorin yhteenvedon näytön oikealle puolelle.
- Näppäimistö ainoastaan
  - Ei tuoteluetteloa, vain näppäimistö suoraa laskutusta varten.
- Tulostusnäkymä (Tulostettava tuotelista QR-koodilla)
  - Jos et aina voi näyttää tuoteluetteloasi digitaalisesti, tarvitset "offline"-ratkaisun tuotteille; BTCPay-palvelimella on tulostusnäkymä toimimaan Offline-kauppana.

![kuva](assets/en/99.webp)

#### Point Of Sale -tyyli - Tuotelista

![kuva](assets/en/100.webp)

#### Point Of Sale -tyyli - Tuotelista + Ostoskori

![kuva](assets/en/101.webp)

#### Point Of Sale -tyyli - Näppäimistö ainoastaan

![kuva](assets/en/102.webp)

#### Point Of Sale -tyyli - Tulostusnäkymä

![kuva](assets/en/103.webp)

#### Valuutta

Kaupan omistaja voi asettaa Point of Sale -pisteelleen eri valuutan kuin hänen yleisesti asettamansa oletusvaluutan. Kaupan oletusvaluutta täyttää tämän kentän automaattisesti.

#### Kuvaus

Kerro maailmalle kaupastasi; mitä myyt ja kuinka paljon? Kaikki, mikä selittää kauppasi, menee tähän.

#### Tuotteet

Kun myyntipiste luodaan, vakio BTCPay Server lisää muutaman tuotteen kauppaan viitteeksi. Napsauta minkä tahansa vakiotuotteen Muokkaa-painiketta ymmärtääksesi paremmin jokaisen mahdollisen vaihtoehdon tuotteelle.

Uuden tuotteen luominen kauppaasi koostuu seuraavista kentistä;

- Otsikko
- Hinta (kiinteä, minimi tai mukautettu)
- Kuvan URL
- Kuvaus
- Varasto
- ID
- Osta-painikkeen teksti
- Ota käyttöön/Poista käytöstä

Kun kaupan omistaja on täyttänyt kaikki uuden tuotteen kentät, napsauta tallenna, ja huomaat, että Tuotteet-osio myyntipisteessä alkaa täyttyä. Varmista aina tallentavasi näytön oikeasta yläkulmasta, jotta kaupan omistajat eivät menetä edistystään tuotteiden lisäämisessä.

Kaupan omistajat voivat myös käyttää "Raakamuokkainta" tuotteidensa määrittämiseen. Raakamuokkain vaatii perustason ymmärrystä JSON-rakenteista.

#### Kassa

BTCPay Server mahdollistaa pieniä myyntipiste-spesifisiä kassan mukautuksia. Kaupan omistaja voi asettaa "Osta x:llä" tekstin tai pyytää tiettyjä asiakastietoja lisäämällä lomakkeita.

#### Tipit

Kaikki kaupat eivät tarvitse tippien vaihtoehtoa myynneissään. Kaupan omistajat voivat ottaa tämän käyttöön tai poistaa käytöstä tarpeidensa mukaan. Jos kauppa käyttää tippejä, kaupan omistaja voi asettaa haluamansa tekstin tippi-kenttään. BTCPay Serverin tipit toimivat prosenttiosuuden mukaan. Kaupan omistajat voivat lisätä useita prosenttiosuuksia pilkulla erotettuna.

#### Alennukset

Kaupan omistajana saatat haluta antaa asiakkaalle mukautetun alennuksen kassalla; alennusten vaihtoehto tulee saataville kauppasi kassalla. Tämä on kuitenkin erittäin suositeltavaa vastaan itsepalvelukassoille.

#### Mukautetut Maksut

Kun Mukautetut Maksut -vaihtoehto on otettu käyttöön, asiakas saa syöttää asettamansa hinnan, joka on yhtä suuri tai suurempi kuin kaupan luoma alkuperäinen lasku.

#### Lisävaihtoehdot

Kun olet asettanut kaiken myyntipisteellesi, jäljellä on joitakin ylimääräisiä vaihtoehtoja. Kaupan omistajat voivat helposti upottaa myyntipisteensä Iframeen tai upottaa maksupainikkeen, joka linkittää tiettyyn kaupan tuotteeseen. Luodun myyntipisteen tyylin määrittämiseksi omistajat voivat lisätä mukautettua CSS:ää lisävaihtoehtojen alaosaan.

#### Poista tämä sovellus

Jos kaupan omistaja haluaa poistaa myyntipisteen kokonaan BTCPay Serveristaan, myyntipisteen päivittämisen alaosassa kaupan omistajat voivat napsauttaa Poista tämä sovellus -painiketta tuhotakseen myyntipiste-sovelluksensa kokonaan. Kun napsautetaan "Poista tämä sovellus", BTCPay Server pyytää vahvistusta kirjoittamalla `DELETE` ja vahvistamalla napsauttamalla Poista-painiketta. Poistamisen jälkeen kaupan omistaja palaa BTCPay Serverin hallintapaneeliin.

### BTCPay Server - Joukkorahoitus

Myyntipisteen lisäosan vieressä, BTCPay Server tarjoaa mahdollisuuden luoda joukkorahoituksen. Aivan kuten mikä tahansa muu joukkorahoitus-alusta, kaupan omistajat voivat asettaa tavoitteen, luoda etuja panostuksille ja mukauttaa sitä tarpeidensa mukaan.

#### Kuinka perustaa uusi joukkorahoitus

Napsauta Joukkorahoitus-lisäosaa BTCPay Serverin päävalikossa vasemmalla Plugin-osion alapuolella. BTCPay Server pyytää nyt nimeä joukkorahoitukselle; tämä nimi näkyy myös vasemmassa valikossa.

#### Päivitä vasta luotu myyntipiste

Kun sovellukselle on annettu nimi, seuraava näyttö on päivittää sovellus saamaan kontekstin.

#### Sovelluksen nimi

Antamasi nimi joukkorahoituksellesi näkyy BTCPay Serverin päävalikossa.

#### Näyttöotsikko

Otsikko on annettu joukkorahoituskampanjalle yleisölle.

#### Iskulause

Anna joukkorahoituskampanjalle ytimekäs kuvaus, josta selviää, mistä keräyksessä on kyse.

![kuva](assets/en/107.webp)

#### Pääkuvan URL

Jokaisella joukkorahoituskampanjalla on pääkuva, se yksi banneri, jonka tunnistat suoraan. Tämän kuvan voi tallentaa palvelimellesi, jos sinulla on hallinnolliset oikeudet, ylläpitäjät voivat ladata sen BTCPay Serverin asetuksista - Tiedostot. Kun olet kaupan omistaja, kuva on ladattava verkkoon kolmannen osapuolen isännöinnin kautta (esimerkiksi imgur)

#### Tee joukkorahoituskampanja julkiseksi

Tämä valitsin tekee joukkorahoituskampanjastasi julkisen ja siten näkyvän ulkomaailmalle. Testaustarkoituksia varten tai nähdäksesi, onko teemasi sovellettu oikein, saatat haluta pitää tämän asetuksen POIS PÄÄLTÄ joukkorahoituskampanjan rakentamisen ajan.

#### Kuvaus

Kerro maailmalle joukkorahoituskampanjastasi, mihin olet keräämässä varoja? Kaikki, mikä selittää joukkorahoituskampanjasi, kuuluu tänne.

![kuva](assets/en/108.webp)

#### Joukkorahoituskampanjan tavoite

Aseta tavoite, kuinka paljon varainkeruun tulisi tuottaa projektille ja missä valuutassa tavoite tulisi ilmoittaa. Varmista, että jos tavoitteesi on asetettu päivämäärien välille, sisällytä nämä tavoite- ja päättymispäivät joukkorahoituskampanjan Tavoitteet-kohtaan.

![kuva](assets/en/109.webp)

#### Edut

Edut auttavat paljon joukkorahoituskampanjassasi. Tämä johtuu siitä, että edut tarjoavat ihmisille tavan osallistua kampanjaasi. Ne vetoavat sekä itsekkäisiin että hyväntekeväisyyteen liittyviin motivaatioihin. Ja ne mahdollistavat pääsyn tukijoidesi lompakkoon, ei vain heidän hyväntekeväisyyskassaan -- voit arvata kumman he pitävät tärkeämpänä.

Uuden edun luominen koostuu seuraavista kentistä;

- Otsikko
- Hinta (kiinteä, minimi tai mukautettu)
- Kuvan URL
- Kuvaus
- Varasto
- ID
- Osta-painikkeen teksti
- Ota käyttöön/Poista käytöstä

Kun kaupan omistaja on täyttänyt kaikki uuden edun luomiseen tarvittavat kentät, klikkaa tallenna, ja huomaat, että Edut-osio joukkorahoituskampanjassa alkaa täyttyä.

![kuva](assets/en/110.webp)

### BTCPay Server - Maksupiste

#### Osallistumiset

Kaupan omistajat voivat valita, miten Edut näytetään, miten ne järjestetään tai jopa rankataan muihin etuihin nähden. Kuitenkin, kun joukkorahoituskampanjan tavoitteet on saavutettu, kaupan omistajat saattavat haluta lopettaa lahjoitusten virtaamisen tähän keräykseen. Siksi hän voi ottaa käyttöön "Älä salli lisäosallistumisia tavoitteen saavuttamisen jälkeen". Tämä pysäyttää joukkorahoituskampanjan lahjoitusten vastaanottamisen.

##### Joukkorahoituskampanjan käyttäytyminen

Joukkorahoituskampanjan standardi laskee tavoitteeseen vain ne laskut, jotka on luotu joukkorahoituskampanjaa varten. Saattaa kuitenkin olla tilanteita, joissa kaupan omistaja haluaa kaikkien tässä kaupassa tehtyjen laskujen laskettavan joukkorahoituskampanjan hyväksi.

#### Lisävaihtoehdot mukauttamiseen

BTCpay Server tarjoaa muutamia lisämukautuksia. Lisää ääniä, animaatioita tai jopa keskusteluketjuja joukkorahoituskampanjaasi. Kaupan omistajat saattavat myös muuttaa joukkorahoituskampanjan ulkoasua syöttämällä oman mukautetun CSS:nsä.

#### Poista tämä sovellus

Jos kaupan omistaja haluaa täysin poistaa joukkorahoituskampanjan BTCPay Serveristään, joukkorahoituskampanjan päivittämisen alaosassa kaupan omistajat voivat klikata "Poista tämä sovellus" -painiketta poistaakseen joukkorahoituskampanjasovelluksensa kokonaan. Kun klikkaat "Poista tämä sovellus", BTCPay Server pyytää vahvistusta kirjoittamalla `DELETE` ja vahvistamalla klikkaamalla Poista-painiketta. Poistamisen jälkeen kaupan omistaja palaa BTCPay Serverin hallintapaneeliin.

### BTCPay Server - Maksupainike

Helppokäyttöiset HTML-maksupainikkeet, jotka voi upottaa sivuille ja jotka ovat laajasti muokattavissa, mahdollistavat kaupan omistajille kärkien ja lahjoitusten vastaanottamisen. BTCPay Serverin vasemmassa valikossa, Plugins-osion alapuolella, kaupan omistajat voivat klikata "Pay Button" ja valita Enable luodakseen Maksupainikkeen.

#### Yleiset Asetukset

Maksupainikkeen Yleisissä Asetuksissa kaupan omistajat voivat määrittää

- Vakiohinnan
- Oletusvaluutan
- Oletusmaksutavan
  - Käytä kaupan oletusta
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Kassan kuvaus
- Tilaus ID

#### Näyttöasetukset

BTCPay Serverin Maksupainiketta voidaan mukauttaa eri tyyleihin sopivaksi. Painikkeet voivat olla kiinteällä tai mukautetulla summalla, joko näytettynä liukusäätimellä tai plus ja miinus -vaihtoehdoilla.

#### Käytä Modaalia

Luodessaan maksupainiketta kaupan omistajat voivat valita sen käyttäytymisen, kun asiakas klikkaa sitä, ja näyttää sen modaali-ikkunassa tai uudella sivulla.

**!?Huomio!?**

Varoitus: Maksupainiketta tulisi käyttää vain kärkiin ja lahjoituksiin

Maksupainikkeen käyttöä e-commerce-integraatioissa ei suositella, koska käyttäjä voi muokata tilaukseen liittyviä tietoja. E-commerceen tulisi käyttää Greenfield API:tamme. Jos tämä kauppa käsittelee kaupallisia transaktioita, suosittelemme luomaan erillisen kaupan ennen maksupainikkeen käyttöä.

#### Mukauta Maksupainikkeen Teksti

Oletuksena BTCPay Serverin maksupainike sanoo "Pay With BTCPay". Kaupan omistajat voivat määrittää tämän tekstin haluamakseen ja vaihtaa BTCPay Serverin logon omaansa. Aseta teksti käyttämällä "Pay Button Text" ja liitä kuvan URL "Pay Button Image URL" alle.

##### Kuvan koko

Painikkeen kuvan koko voidaan asettaa vain kolmeen oletusarvoon.

- 146x40px
- 168x46px
- 209x57px

#### Painiketyyppi

BTCPay Server tuntee kolme tilaa Maksupainikkeelle.

- Kiinteä Summa
  - Aiemmin asetettu hinta on painikkeen yleisissä asetuksissa.
- Mukautettu Summa
  - BTCPay Serverin Maksupainikkeessa on + ja - -vaihtoehdot mukautetun hinnan asettamiseksi.
  - Mukautetun summan käyttäessä BTCPay Server pyytää Min, Max ja kuinka asteittain sen tulisi kasvaa.
  - Painikkeet voidaan asettaa "Käytä Yksinkertaista syöttötyyliä". Tämä poistaa +/- Vaihtoehdot.
  - Sovita painike inline, jossa painike ja vaihtoehdot näkyvät rivissä.
- Liukusäädin
  - Samankaltainen kuin mukautettu summa, mutta visuaalisesti erilainen, sillä siinä on liukusäädin +/- vaihtoehtojen sijaan.
  - Liukusäädintä käytettäessä BTCPay Server pyytää Min, Max ja kuinka asteittain sen tulisi kasvaa.

**!?Huomio!?**

Maksupainikkeen poistaminen voidaan tehdä yläosassa varoituskuvausten kohdalla.

#### Maksuilmoitukset

Server IPN (Instant Payment Notification) on tarkoitettu webhooksille ja siihen voidaan täyttää URL, johon ostotiedot lähetetään.

#### Sähköposti-ilmoitukset

Aina kun maksu tapahtuu, BTCPay Server voi ilmoittaa kaupan omistajalle.

#### Selaimen uudelleenohjaus

Kun asiakas on suorittanut ostoksen, hänet ohjataan tähän linkkiin, jos kaupan omistaja on sen asettanut.

#### Edistyneet Maksupainikkeen Asetukset

Määritä lisäkyselymerkkijonoparametrit, jotka tulisi liittää kassasivulle laskun luomisen jälkeen. Esimerkiksi `lang=da-DK` lataisi kassasivun oletuksena tanskaksi.

#### Käytä Sovellusta Päätepisteenä

Linkitä maksupainike suoraan johonkin tuotteeseen PoS- tai Crowdfund-sovelluksissa aiemmin.
Kauppiaat voivat klikata pudotusvalikkoa ja valita haluamansa sovelluksen; kun sovellus on valittu, kauppias voi lisätä kohteen, joka tulee linkittää.

#### Generoitu koodi

Koska BTCPay Serverin maksunappi on helposti upotettavaa HTML-koodia, BTCPay Server näyttää konfiguroinnin jälkeen alaosassa generoidun koodin, jonka voi kopioida verkkosivustolle.

Kauppiaat voivat kopioida generoidun koodin verkkosivustolleen, ja BTCPay Serverin maksunappi on suoraan aktiivinen heidän verkkosivustollaan.

#### Maksuilmoitukset

Palvelimen IPN (Instant Payment Notification) on tarkoitettu webhooksille ja siihen voidaan täyttää URL, johon ostotiedot lähetetään.

#### Sähköposti-ilmoitukset

Aina kun maksu tapahtuu, BTCPay Server voi ilmoittaa kauppiaalle.

#### Selaimen uudelleenohjaus

Kun asiakas on suorittanut ostoksen, hänet ohjataan tähän linkkiin, jos kauppias on sen asettanut.

#### Lisäasetukset maksunapille

Määritä lisäkyselymerkkijono-parametrit, jotka tulisi liittää kassasivulle laskun luomisen jälkeen. Esimerkiksi `lang=da-DK` lataisi kassasivun oletuksena tanskaksi.

#### Käytä sovellusta päätepisteenä

Linkitä maksunappi suoraan kohteeseen jossakin PoS- tai Crowdfund-sovelluksessa aiemmin. Kauppiaat voivat klikata pudotusvalikkoa ja valita haluamansa sovelluksen, kun sovellus on valittu, kauppias voi lisätä kohteen, joka tulee linkittää.

#### Generoitu koodi

Koska BTCPay Serverin maksunappi on helposti upotettavaa HTML-koodia, BTCPay Server näyttää konfiguroinnin jälkeen alaosassa generoidun koodin, jonka voi kopioida verkkosivustolle. Kauppiaat voivat kopioida generoidun koodin verkkosivustolleen ja BTCPay Serverin maksunappi on suoraan aktiivinen heidän verkkosivustollaan.

### Taitojen yhteenveto

Tässä osiossa opit:

- Miten käyttää BTCPay Serverin integroitua PoS-lisäosaa helposti luodaksesi mukautetun kaupan
- Miten käyttää BTCPay Serverin integroitua Crowdfund-lisäosaa helposti luodaksesi mukautetun joukkorahoitussovelluksen
- Generoimaan koodin mukautetulle maksunapille käyttäen Pay Button -lisäosaa

### Tiedon arviointi

#### KA-arvostelu

Mitkä ovat kolme sisäänrakennettua lisäosaa, jotka tulevat vakiona BTCPay Serverin kanssa? Kuvaile lyhyesti, miten kutakin voidaan käyttää.

# BTCPay Serverin konfigurointi

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Perustiedot BTCPay Serverin asentamisesta LunaNode-ympäristöön

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### BTCPay Serverin asentaminen isännöidylle ympäristölle (LunaNode)

Nämä vaiheet tarjoavat kaikki tarvittavat tiedot BTCPay Serverin käyttöönotosta LunaNodessa. Ohjelmiston voi ottaa käyttöön monin eri tavoin.
Löydät kaikki tiedot BTCPay Serveristä osoitteesta https://docs.btcpayserver.org.

#### Mistä aloitamme?

Tässä osassa tutustut LunaNodeen isäntänä, opit ensimmäiset askeleet BTCPay Serverisi käytössä ja opit, miten toimia Lightning Networkin kanssa. Kun olemme käyneet läpi kaikki vaiheet, voit pyörittää verkkokauppaa tai joukkorahoitusplatformia, joka hyväksyy Bitcoinin!

Tämä on yksi monista tavoista ottaa BTCPay Server käyttöön. Lue dokumentaatiomme lisätietoja varten,

https://docs.btcpayserver.org.

### BTCPay Server - LunaNoden käyttöönotto

#### LunaNoden käyttöönotto

Ensin, mene LunaNode.com -verkkosivustolle, jossa luomme uuden tilin. Klikkaa oikeassa yläkulmassa olevaa "Sign Up" -painiketta tai käytä "Get Started" -opasta heidän kotisivullaan.
![image](assets/en/111.webp)

Kun olet luonut uuden tilin, LunaNode lähettää vahvistussähköpostin. Kun olet vahvistanut tilin, verrattuna Voltageen, sinulle esitetään välittömästi mahdollisuus lisätä saldoa tilillesi. Tätä saldoa tarvitaan palvelintilan ja hosting-kustannusten maksamiseen.

![image](assets/en/112.webp)

#### Lisää saldoa LunaNode-tilillesi

Kun olet klikannut "Deposit credit", voit asettaa haluamasi summan, jonka haluat lisätä tilillesi, ja miten haluat maksaa sen. LunaNode ja BTCPay Server maksavat 10$USD ja 20$USD välillä kuukaudessa.
Verrattuna Voltage.cloudiin, saat täyden pääsyn Virtuaaliseen Yksityiseen Palvelimeesi (VPS tästä eteenpäin) ja siten enemmän kontrollia palvelimeesi. Kun olet luonut uuden tilin, LunaNode lähettää vahvistussähköpostin.
Kun olet vahvistanut tilin, verrattuna Voltageen, sinulle esitetään välittömästi mahdollisuus lisätä saldoa tilillesi. Tätä saldoa tarvitaan palvelintilan ja hosting-kustannusten maksamiseen.

#### Kuinka ottaa käyttöön uusi palvelin?

Tässä oppaassa käymme läpi asennuksen luomalla joukon API-avaimia ja käyttämällä LunaNoden tekemää BTCPay Server -käynnistäjää.

LunaNode-kojelaudassasi, klikkaa API oikeassa yläkulmassa. Tämä avaa uuden sivun. Meidän tarvitsee vain asettaa nimi API-avaimelle. Loput hoitaa LunaNode eikä niitä käsitellä tässä oppaassa. Klikkaa "Create API Credential" -painiketta.
API-tunnisteiden luomisen jälkeen saat pitkän kirjainten ja merkkien jonon. Tämä on API-avaimesi.

![image](assets/en/113.webp)

#### Kuinka ottaa käyttöön uusi palvelin?

Näissä tunnisteissa on 2 osaa, API-avain ja API-ID; tarvitsemme molemmat. Ennen kuin siirrymme seuraavaan vaiheeseen, avataan toinen välilehti selaimessa ja mennään osoitteeseen https://launchbtcpay.lunanode.com/

Täällä sinua pyydetään antamaan API-avain ja API-ID. Tämä varmistaa, että juuri sinä otat käyttöön tämän uuden palvelimen. API-avaimen pitäisi edelleen olla avoinna edellisessä välilehdessä; jos vierität alaspäin taulukossa, löydät API-ID:n.

Palaa takaisin sivulle, jossa on Launcher, täytä kentät API-avaimellasi ja ID:lläsi ja klikkaa jatka.

![image](assets/en/114.webp)

Seuraavassa vaiheessa voit antaa verkkotunnuksen. Jos sinulla on jo verkkotunnus ja haluat käyttää sitä BTCPay Serverille, varmista, että lisäät myös DNS-tietueen (kutsutaan `A`-tietueeksi) verkkotunnukseesi. Jos sinulla ei ole verkkotunnusta, käytä sen sijaan LunaNoden tarjoamaa verkkotunnusta (voit muuttaa tätä myöhemmin BTCPay Serverin asetuksissa) ja klikkaa Jatka.

Lue lisää DNS-tietueen asettamisesta tai muuttamisesta BTCPay Serverille; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Käynnistä BTCPay Server LunaNodessa

Edellisten vaiheiden jälkeen voimme asettaa kaikki vaihtoehdot uudelle palvelimellemme. Tässä vaiheessa valitsemme tuetuksi valuutaksi Bitcoinin (BTC); voimme asettaa sähköpostin saadaksemme ilmoituksia salausvarmenteiden uusimisesta; tämä ei ole pakollista.
Tämä opas keskittyy Mainnet-ympäristön (oikean maailman Bitcoin) pystyttämiseen; kuitenkin LunaNode mahdollistaa myös Testnetin tai Regtestin käytön kehitystarkoituksiin. Tässä oppaassa pidämme vaihtoehdon Mainnetissa.

Valitse Lightning-toteutuksesi. LunaNode tarjoaa kaksi erilaista toteutusta, LND ja Core Lightning. Tässä oppaassa valitsemme LND:n. Toteutusten välillä on pieniä, mutta todellisia eroja; lisätietoja tästä suosittelemme lukemaan kattavan dokumentaation; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![kuva](assets/en/115.webp)

LunaNode tarjoaa useita Virtuaalikone (VM) -paketteja. Nämä eroavat hintaluokissa ja palvelimen teknisissä tiedoissa. Tähän oppaaseen riittää m2-paketti; kuitenkin, jos olet valinnut Bitcoinin lisäksi muita valuuttoja, harkitse vähintään m4:n käyttöä.

Nopeuta alkuperäisen lohkoketjun synkronointia; tämä on valinnainen ja riippuu tarpeistasi. On olemassa edistyneitä vaihtoehtoja, kuten Lightning Alias -asetuksen määrittäminen, tietyn GitHub-julkaisun osoittaminen tai SSH-avainten asettaminen; näitä ei käsitellä tässä oppaassa.

Lomakkeen täyttämisen jälkeen sinun on napsautettava Launch VM, ja Lunanode alkaa luoda uutta VM:ääsi, johon on asennettu BTCPay Server. Tämä prosessi kestää muutaman minuutin; kun palvelimesi on valmis, LunaNode antaa sinulle linkin uuteen BTCPay Serveriisi.

Luomisprosessin jälkeen napsauta linkkiä BTCPay Serveriisi; täällä sinua pyydetään luomaan Ylläpitäjän tili.

![kuva](assets/en/116.webp)

### Taitojen Yhteenveto

Tässä osiossa opit:

- Luomaan ja rahoittamaan tilin LunaNodessa
- Käyttämään BTCPay Server Launcheria oman palvelimesi luomiseen

### Tiedon arviointi

#### KA Konseptuaalinen katsaus

Kuvaile joitakin eroja BTCPay Server -instanssin ajamisessa VPS:llä verrattuna tilin luomiseen isännöidyllä instanssilla.

## BTCPay Serverin asentaminen Voltage-ympäristöön

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Tutustut hosting-palveluntarjoajaan Voltage.cloud, opit BTCPay Serverisi ensiaskeleet ja opit käyttämään Lightning Networkia. Kun olemme käyneet läpi kaikki vaiheet, voit pyörittää verkkokauppaa tai joukkorahoitus-alustaa, joka hyväksyy Bitcoinin!

Tämä on yksi monista tavoista ottaa käyttöön BTCPay Server. Lue lisää dokumentaatiostamme,
https://docs.btcpayserver.org.

### BTCPay Server - Voltage.cloud käyttöönotto

Mene ensin verkkosivulle Voltage.cloud ja rekisteröidy uudeksi käyttäjäksi. Kun luot tiliä, voit rekisteröityä 7 päivän ilmaiseen kokeiluun. Voit joko napsauttaa "Sign Up" yläoikealla tai käyttää "Try a free 7 day trial" heidän kotisivullaan.

![kuva](assets/en/117.webp)

Kun olet luonut tilin, napsauta `NODES`-painiketta hallintapaneelissasi. Kun olemme valinneet Solmut ja luoneet uuden solmun, meille esitellään mahdolliset solmut, joita Voltage tarjoaa. Koska tämä opas käsittelee myös LightningNetworkia, meidän on ensin valittava Lightning-toteutuksemme ennen kuin luomme BTCPay Serverin. Napsauta LightningNode.

![kuva](assets/en/118.webp)
Tässä sinun tulee valita, minkä tyyppisen Lightning-noden haluat. Voltage tarjoaa monia vaihtoehtoja valaistusasetuksillesi. Tämä eroaa esimerkiksi LunaNoden käyttöönotosta. Tämän oppaan tarkoituksessa Lite Node riittää. Lue lisää eroista Voltage.cloud-sivustolla.
![image](assets/en/119.webp)

Anna nodellesi nimi, aseta salasana ja suojaa tämä salasana. Jos menetät tämän salasanan, menetät pääsyn varmuuskopioihisi, eikä Voltage voi palauttaa sitä. Luo node, ja Voltage näyttää edistymisen. Voltage on luonut Lightning-nodesi. Voimme nyt luoda BTCPay Server -instanssin ja päästä suoraan Lightning-verkkoon.

Napsauta Nodes kohtaa hallintapaneelin vasemmassa yläkulmassa. Täällä voit asettaa seuraavan osan BTCPay Server -instanssistasi. Napsauta "luo uusi", kun olet nodien yleisnäkymässä. Saat samankaltaisen näytön kuin aiemmin. Nyt valitsemme Lightning Noden sijaan BTCPay Serverin.

Voltage näyttää BTCPay Serverisi maantieteellisen sijainnin, Voltage isännöi Yhdysvaltain länsialueella. Täällä näet myös palvelimen isännöinnin hinnan. Napsauta Luo ja anna BTCPay Serverillesi nimi. Ota Lightning käyttöön, ja Voltage näyttää edellisessä vaiheessa luodun Lightning-noden. Napsauta Luo, ja Voltage luo BTCPay Server -instanssin.

![image](assets/en/120.webp)

Kun olet napsauttanut luo, Voltage näyttää oletuskäyttäjänimen ja salasanan. Nämä ovat samankaltaiset kuin aiemmin Voltage:ssa asettamasi salasana. Napsauta Kirjaudu sisään -painiketta, niin sinut ohjataan BTCPay Serveriisi.

Tervetuloa uuteen BTCPay Server -instanssiisi. Koska olemme jo asettaneet Lightningin luomisprosessissa, se näyttää, että Lightning on jo otettu käyttöön!

### Taitojen yhteenveto

Tässä luvussa opit:

- Tilin luomisen Voltage.cloud-sivustolla
- Askeleet BTCPay Serverin käyttöönottoon yhdessä Lightning-noden kanssa tililläsi

### Tiedon arviointi

#### KA Käsitteellinen katsaus

Mitkä ovat joitakin keskeisiä eroja Voltage- ja LunaNode-asetusten välillä?

## BTCPay Serverin asentaminen Umbrel-nodelle

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Näiden vaiheiden lopussa voit vastaanottaa lightning-maksuja BTCPay-kauppaasi paikallisverkossasi. Tämä prosessi pätee myös, jos käytät umbrel-nodea ravintolassa tai yrityksessä. Jos haluat yhdistää tämän kaupan julkiselle verkkosivustolle, noudata Edistynyttä harjoitusta altistaaksesi umbrel-nodesi julkisesti.

https://umbrel.com/

![image](assets/en/121.webp)

Kun Umbrel-nodesi on täysin synkronoitu Bitcoin-lohkoketjun kanssa, siirry Umbrel App Storeen ja etsi BTCPay Server sovellusten alta.

![image](assets/en/122.webp)

Napsauta BTCPay Serveriä nähdäksesi sovelluksen tiedot. Kun BTCPay Serverin tiedot ovat auki, oikeassa alakulmassa näkyy sovelluksen asianmukaiseen toimintaan vaadittavat vaatimukset. Siinä näytetään, että se vaatii Bitcoin- ja Lightning-noden. Jos et ole asentanut Lightning Nodea Umbrelillesi, napsauta Asenna. Tämä prosessi voi kestää muutaman minuutin.

![image](assets/en/123.webp)

Lightning Noden asentamisen jälkeen:

1. Napsauta avaa sovellustiedot tai sovellus Umbrelin hallintapaneelissa.
2. Napsauta aseta uusi node; sinulle näytetään 24 sanaa lightning-nodesi palauttamiseksi.
3. Kirjoita nämä ylös.

![image](assets/en/124.webp)
Umbrel pyytää vahvistusta juuri kirjoitetuista sanoista. Kun Lightning-solmu on asennettu, palaa Umbrelin sovelluskauppaan ja etsi BTCPay Server. Klikkaa asennuspainiketta, ja Umbrel näyttää, ovatko vaaditut komponentit asennettu ja että BTCPay Server vaatii pääsyn näihin komponentteihin. Asennuksen jälkeen klikkaa Avaa sovellustietojen oikeassa yläkulmassa tai avaa BTCPay Server Umbrelin hallintapaneelista.

Umbrel pyytää vahvistusta juuri kirjoitetuista sanoista.

![kuva](assets/en/125.webp)

**!?Huomio!?**

Muista säilyttää nämä asianmukaisessa paikassa, kuten aiemmin opit avaimia säilyttäessäsi.

Kun Lightning-solmu on asennettu, palaa Umbrelin sovelluskauppaan ja etsi BTCPay Server. Klikkaa asennuspainiketta, ja Umbrel näyttää, ovatko vaaditut komponentit asennettu ja että BTCPay Server vaatii pääsyn näihin komponentteihin.

![kuva](assets/en/126.webp)

Asennuksen jälkeen klikkaa Avaa sovellustietojen oikeassa yläkulmassa tai avaa BTCPay Server Umbrelin hallintapaneelista.

![kuva](assets/en/127.webp)

### Taitojen Yhteenveto

Tässä osiossa opit:

- Askeleet BTCPay Serverin asentamiseen Lightning-toiminnallisuudella Umbrel-solmuun

### Tiedon Arviointi

#### KA Käsitteellinen Katsaus

Miten asennus Umbrelissa eroaa kahdesta aiemmasta isännöidystä vaihtoehdosta?

# Yhteenveto

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Arvioi kurssi
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Kurssin Yhteenveto

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![kuva](assets/en/128.webp)

Sinulla tulisi myös olla yleinen ymmärrys siitä, mikä Bitcoin on, miten se toimii ja miten se voi skaalautua toisen kerroksen ratkaisujen, kuten Lightning-verkon, avulla. Tällä kurssilla kävimme laajasti läpi, miten kuka tahansa voi käyttää BTCPay Serveriä, alkaen alkuperäisestä asennuksesta kaupan luomiseen ja monimutkaiseen laskutuksen hallintaan, tullakseen taloudellisesti itsevaltaiseksi yksilöksi tai kauppiaaksi.

Onnittelut kurssin suorittamisesta. Toivomme, että olet nauttinut sisällöstä ja jatkat BTCPay Serverin käyttöä ja tutkimista, ja olet yhtä innostunut Bitcoinin ja kasvavan rakentajien ja osallistujien yhteisön lupaavasta tulevaisuudesta kuin mekin.

> **FOSS on väistämätön.**

### Sanasto

| Termi                                              | Määritelmä                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 51% hyökkäys                                       | Toiminta, jossa tarkoituksella rakennetaan uusi pisin lohkoketju korvaamaan lohkoketjussa olevat lohkot. Tämä mahdollistaa jo lohkoketjuun louhittujen transaktioiden korvaamisen. Tällainen hyökkäys on helpoin suorittaa, kun sinulla on enemmistö louhintatehosta, minkä vuoksi sitä kutsutaan "Enemmistöhyökkäykseksi" tai "51% hyökkäykseksi".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AccountKey                                         | Tiliavain uudelleen perustamiseen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| AccountKeyPath                                     | Polku juuresta tiliavaimelle, joka on etuliitteenä pääjulkisen avaimen sormenjäljellä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Osoite                                             | Bitcoin-osoitteet tiivistävät tiedon, joka on tarpeen maksun vastaanottajalle maksamiseen. Nykyaikainen osoite koostuu kirjainten ja numeroiden sarjasta, joka alkaa bc1:llä ja näyttää esimerkiksi tältä: bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Osoite on lyhennelmä vastaanottajan lukituskomennosta, jota lähettäjä voi käyttää varojen siirtämiseen vastaanottajalle. Useimmat osoitteet edustavat joko vastaanottajan julkista avainta tai jonkinlaista komentoa, joka määrittelee monimutkaisempia käyttöehtoja. Edellä mainittu esimerkki on bech32-osoite, joka koodaa todistusohjelman lukitsemaan varat julkisen avaimen hajautusarvoon (katso Pay-to-Witness-Public-Key-Hash). On myös vanhempia osoitemuotoja, jotka alkavat 1:llä tai 3:lla ja käyttävät Base58Check-osoitteen koodausta edustaakseen julkisen avaimen hajautusarvoja tai komentohajautusarvoja.      |
| Osoitteen Tyyppi                                   | Osoite voi edustaa useita erilaisia komentoja. Osoitteet koodataan ja niille annetaan etuliite niiden komentotyypin välittämiseksi. Perinteiset osoitteet käyttävät Base58-koodausta, ja kun perinteinen osoite on julkisen avaimen hajautusarvo, niin sanottu P2PKH-osoite, se alkaa ‘1’:llä. Harvemmin perinteinen osoite on komennon hajautusarvo, jolloin se alkaa ‘3’:lla. Tällä hetkellä kaikki SegWit-osoitteet on koodattu Bech32:ssa ja alkavat etuliitteellä ‘bc1’.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Sovellus                                           | BTCPay Serverilla on laajennuksia, jotka saattavat toimia itsenäisinä sovelluksina.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| BIP 329                                            | Lompakon tunnisteiden vienti/tuonti                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| BIP49                                              | Määrittelee johdatuskaavan HD-lompakoille käyttäen P2WPKH-nested-in-P2SH (BIP 141) serialisointimuotoa erillisille todistustapahtumille.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Bitcoin-osoite                                     | Alfanumeerinen merkkijono, johon lähetät bitcoinisi, joten se "asuu" nyt siellä. On tunnistetieto, joka koostuu noin 33 kirjaimen ja numeron yhdistelmästä. Nykyisessä protokollaversiossa osoite alkaa 1:llä, 3:lla tai b:llä. Vastaanottajan osoitteen omistaminen on välttämätön osa bitcoin-siirron aloittamista. Bitcoin-osoitteet luodaan julkisista avaimista ja useita osoitteita voidaan luoda yhdestä julkisten avainten sarjasta yksityisyyden parantamiseksi. Bitcoin-osoitteet toimivat samalla tavalla kuin sähköpostiosoitteet; jos haluat lähettää viestin, sinun on tiedettävä, minne se menee, sama pätee bitcoiniin. Ennen bitcoin-siirron lähettämistä, varmista, että vastaanottajan osoite on tarkka, sillä bitcoin-siirrot ovat peruuttamattomia ja saatat lähettää bitcoineja osoitteeseen, joka ei kuulu vastaanottajalle.                                      |
| bitcoin versus Bitcoin                             | Bitcoin on rahaverkko, ja bitcoin (pienellä alkukirjaimella) on rahayksikkö Bitcoin-verkossa. Käytät bitcoin-valuuttaa tai -tokenia suorittaaksesi tapahtumia Bitcoin-verkossa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Lohko                                              | Lohko on Bitcoin-lohkoketjun tietorakenne, joka koostuu otsikosta ja joukosta Bitcoin-siirtoja. Lohko on merkitty aikaleimalla ja se sitoutuu tiettyyn edeltäjään (vanhempaan) lohkoon. Kun lohkon otsikko on hajautettu, se tarjoaa työn todistuksen, joka tekee lohkoketjusta todennäköisesti muuttumattoman. Lohkojen on noudatettava verkoston konsensuksen määrittelemiä sääntöjä lohkoketjun laajentamiseksi. Kun lohko liitetään lohkoketjuun, mukana olevat siirrot katsotaan saaneen ensimmäisen vahvistuksensa.                                                                                                                                                                                                                                                                                                                                                                |
| Lohkotutkija                                       | Verkkotyökalu, jonka avulla voit etsiä reaaliaikaista ja historiallista tietoa lohkoketjusta, mukaan lukien tietoja lohkoista, siirroista, osoitteista ja muusta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Lohkon Tiiviste                                    | Lohkon tiiviste on lohkon datan SHA-256 tiiviste ja se esitetään yleensä heksadesimaalimuodossa. Lohkon tiivistettä voidaan pitää erittäin suurena numerona. Jotta Proof-of-Work-vaatimus täyttyisi, lohkon tiivisteen on oltava tietyn kynnyksen alapuolella. Näin ollen kaikki lohkon tiivisteet alkavat nollasarjalla, jonka jälkeen seuraa alfanumeerinen merkkijono. Joissakin lohkoissa on jopa kaksikymmentä johtavaa nollaa, kun taas aikaisemmissa lohkoissa niitä on ollut niinkin vähän kuin kahdeksan. Vaadittavien nollien määrä karkeasti osoittaa louhinnan vaikeuden sillä hetkellä, kun lohko julkaistiin.                                                                                                                                                                                                                                                              |
| Lohkon Korkeus                                     | Jokainen lohko on numeroitu nousevassa järjestyksessä, alkaen nollasta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Lohkopalkkio                                       | Koostuu lohkon subventiosta (uudesti luotu bitcoin) ja kaikkien lohkoon sisältyvien transaktioiden transaktiomaksujen summasta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Lohkon Koko                                        | Jokaisella lohkolla on rajoitettu määrä dataa, jonka se voi sisältää. Data, joka ei mahdu tiettyyn lohkoon, kirjataan yhteen seuraavista lohkoista. Bitcoin-lohkojen osalta niiden koko oli aiemmin 1mb, mutta pehmeän haarukan jälkeen lohkon koko voi teknisesti olla jopa 4mb dataa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Lohkon Subventio                                   | Uuden bitcoinin määrä, joka on mintattu jokaisessa lohkossa. Jokainen tuotettu ja lohkoketjuun lisätty lohko mahdollistaa lohkon luojan mintata tietyn määrän uutta bitcoinia. Subventio alkoi 50 BTC:stä per lohko, ja se puolittuu joka 210 000 lohkon tai suunnilleen 4 vuoden välein.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Lohkoketju                                         | Hajautettu loki tai tietokanta kaikista Bitcoin-transaktioista. Transaktiot ryhmitellään erillisiksi päivityksiksi, joita kutsutaan lohkoiksi, rajoitettuna jopa 4 miljoonaan painoyksikköön. Lohkoja tuotetaan noin joka 10. minuutti stokastisen prosessin, louhinnan, kautta. Jokainen lohko sisältää laskennallisesti intensiivisen "proof of work" -todistuksen. Proof of work -vaatimusta käytetään säätämään lohkojen välejä ja suojaamaan lohkoketjua hyökkäyksiltä, jotka pyrkivät kirjoittamaan historian uudelleen: hyökkääjän olisi voitettava olemassa oleva proof of work korvatakseen jo julkaistut lohkot, mikä tekee jokaisesta lohkosta todennäköisesti muuttumattoman, kun se on haudattu seuraavien lohkojen alle.                                                                                                                                                   |
| BTCPAY Server Vault                                | Optimaalisen tasapainon saavuttamiseksi käytettävyyden, turvallisuuden ja yksityisyyden välillä on suositeltavaa käyttää BTCPay Server Walletia laitteistolompakon kanssa. BTCPay Vault on rakennettu siltaamaan laitteistolompakko ja BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Bysanttilaisten kenraalien ongelma                 | Peliteorian ongelma, joka kuvailee vaikeutta, joka hajautetuilla osapuolilla on saavuttaa konsensus ilman luotettua keskusosapuolta. Nimi tulee skenaariosta, jossa useat kenraalit piirittävät Bysanttia. He ovat saartaneet kaupungin, mutta heidän on yhdessä päätettävä, milloin hyökätä. Jos kaikki kenraalit hyökkäävät samaan aikaan, he voittavat, mutta jos he hyökkäävät eri aikoihin, he häviävät. Kenraaleilla ei ole turvallisia kommunikaatiokanavia keskenään, koska kaikki lähettämät tai vastaanotetut viestit ovat saattaneet tulla kaapatuiksi tai petollisesti lähetetyiksi Bysantin puolustajien toimesta. Miten kenraalit voivat järjestäytyä hyökätäkseen samaan aikaan?                                                                                                                                                                                          |
| Sensuuri                                           | Kontrolli siitä, mitä tietoa voidaan välittää massoille. Bitcoinin osalta sensuuri tarkoittaa kolmansien osapuolien kykyä pysäyttää transaktio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Vaihtoraha                                         | UTXO:jen osa, joka palautetaan lähettäjän lompakkoon, yleensä eri osoitteen kautta. Vastaa syötteiden summaa miinus käytetty määrä ja transaktiomaksu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Child Pays For Parent (CPFP)                       | Tekniikka, jossa käyttäjä käyttää matalan siirtomaksun vahvistamatonta siirtoa lapsitransaktiossa, jolla on korkea siirtomaksu, jotta louhijat kannustetaan sisällyttämään molemmat siirrot lohkoon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Coinbase Transaction                               | Jokaisen lohkon ensimmäinen siirto, joka jakaa lohkopalkkion ja siirtomaksut kenelle tahansa, joka on louhinut lohkon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Coincidence of Wants                               | Taloudellinen ilmiö, jossa kahdella osapuolella on kummallakin esine, jota toinen haluaa, joten he vaihtavat nämä esineet suoraan ilman rahallista välinettä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Cold Storage                                       | Tapa hallita tietoja ilman internet-yhteyttä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Cold Wallet                                        | Bitcoin-lompakon tyyppi, joka säilyttää yksityiset avaimet turvallisesti offline-tilassa, yleensä fyysisellä laitteella. Tunnettu myös nimellä laitelompakko, ja se suojaa digitaalisia bitcoinejasi online-hakkereilta käyttämällä flash-aseman kaltaista laitetta, joka ei ole yhdistetty internetiin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Command Line Interface (CLI)                       | Vuorovaikutus laitteen tai tietokoneohjelman kanssa käyttäjän tai asiakkaan komentojen kautta, ja vastaukset laitteelta tai ohjelmalta tekstirivien muodossa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Commitment Transaction                             | Sitoutumistransaktio on Bitcoin-siirto, jonka molemmat kanavakumppanit ovat allekirjoittaneet, ja joka koodaa kanavan viimeisimmän saldon. Joka kerta kun kanavan kautta tehdään uusi maksu tai välitetään maksu, kanavan saldo päivittyy, ja uusi sitoutumistransaktio allekirjoitetaan molempien osapuolten toimesta. Tärkeää on, että kanavassa Alicesin ja Bobin välillä sekä Alice että Bob pitävät omaa versiotaan sitoutumistransaktiosta, joka on myös toisen osapuolen allekirjoittama. Kanava voidaan milloin tahansa sulkea joko Alicen tai Bobin toimesta, jos he esittävät sitoutumistransaktionsa Bitcoin-lohkoketjuun. Vanhan (vanhentuneen) sitoutumistransaktion esittäminen katsotaan huijaukseksi (eli protokollarikkomukseksi) Lightning-verkossa ja voi johtaa siihen, että toinen osapuoli voi vaatia kaikki kanavan varat itselleen rangaistustransaktion kautta. |
| Confirmation                                       | Kun siirto on sisällytetty lohkoon, sillä on yksi vahvistus. Heti kun toinen lohko louhitaan lohkoketjuun, siirrolla on kaksi vahvistusta, ja niin edelleen. Kuusi tai useampi vahvistus katsotaan riittäväksi todisteeksi siitä, että siirtoa ei voi peruuttaa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Crowdfund (CF)                                     | BTCPay Serverin oletuslaajennus, joka mahdollistaa kaupan omistajalle helpon tavan luoda tyypillinen joukkorahoitusverkkosivusto. He voivat helposti asettaa tavoitteen, luoda etuja lahjoituksista ja mukauttaa sitä tarpeidensa mukaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Cryptography                                       | Erityinen järjestelmä, jossa alkuperäinen viesti muutetaan niin, että vain tarkoitetut vastaanottajat voivat vastaanottaa sen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Dashboard                                          | BTCPay Serverin keskeinen aloitussivu. Se tarjoaa yleiskatsauksen kaikista kaupan toiminnoista, jotka näkyvät useilla yhteenvetolaatoilla.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Demo                                               | Viittaa virtuaaliseen ympäristöön, jossa ohjelmistodemot tapahtuvat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Deployment                                         | Ohjelmiston käyttöönotto kattaa kaikki toimenpiteet, jotka tekevät ohjelmistojärjestelmän käyttövalmiiksi. Yleinen käyttöönottoprosessi koostuu useista toisiinsa liittyvistä toiminnoista mahdollisine siirtymineen niiden välillä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Johdannaispolku                                    | Tieto, joka kertoo hierarkkisen deterministisen (HD) lompakon, miten johdetaan tietty avain avainpuun sisällä. Johdannaispolkuja käytetään Bitcoin-standardina ja ne otettiin käyttöön HD-lompakoiden yhteydessä osana BIP 32:ta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Vaikeusasteen Säätö                                | Vaikeustason säätö, joka tapahtuu joka 2016 lohkon jälkeen (noin kahden viikon välein) yrittäen varmistaa, että lohkoja louhitaan keskimäärin kerran joka 10. minuutti. Se luo siis jatkuvan ajan lohkojen välille ja jatkuvan uusien bitcoinien liikkeellelaskun verkkoon (lohkopalkkion kautta).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Vaikeustavoite                                     | Käytetään louhinnassa, ja se on numero, jonka alle lohkon tiivisteen on oltava, jotta lohko voidaan lisätä lohkoketjuun.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Digitaalinen Allekirjoitus                         | Digitaalinen allekirjoitus on matemaattinen järjestelmä digitaalisten viestien tai asiakirjojen aitouden ja eheyden varmistamiseksi. Sitä voidaan pitää kryptografisena sitoumuksena, jossa viesti ei ole piilotettu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Jaettavuus                                         | Hyödykkeen ominaisuus, joka voidaan jakaa pienempiin määriin menettämättä arvoa. Koska taloudelliset transaktiot tapahtuvat usein vaihtelevissa määrissä, valuutan on oltava jaettavissa, jotta sitä voidaan käyttää laajasti taloudessa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Docker                                             | Ohjelmisto, joka pakkaa ohjelmistot standardoiduiksi yksiköiksi, kutsutaan säiliöiksi, joissa on kaikki, mitä ohjelmisto tarvitsee toimiakseen, mukaan lukien kirjastot, järjestelmätyökalut, koodi ja suoritusaika.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Kahdenkertainen Kulutus                            | Tuloksena on, että jotakin rahaa onnistutaan kuluttamaan useammin kuin kerran. Bitcoin suojaa kahdenkertaiselta kulutukselta varmistamalla, että jokainen lohkoketjuun lisätty transaktio noudattaa konsensussääntöjä; tämä tarkoittaa tarkistamista, etteivät transaktion syötteet ole aiemmin kulutettu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Kestävyys                                          | Rahan ominaisuus, jossa valuutta voi säilyttää alkuperäisen tilansa ajan yli ja kestää toistuvaa käyttöä. Kestävän valuutan on kestettävä mahdolliset vahingot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Electrum                                           | Electrum on yksi suosituimmista Bitcoin-lompakoista, luotu vuonna 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Laajennettu julkinen avain (Xpub)                  | Laajennettu julkinen avain, tunnetaan myös nimellä Xpub, on julkinen avain, joka toimii vanhempana avaimille, jotka on johdettu xpubista HD-lompakon ominaisuutena. Tämä Xpub on standardi, joka esiteltiin BIP 32:ssa. Lompakot käyttävät sitä kulissien takana julkisten avainten johtamiseen. Xpubin jakamista ei neuvota vastaan, varasi eivät ole suorassa vaarassa siirtyä, xpub ei voi johtaa yksityisiä avaimia. Xpubin jakamisen hyöty voi olla esimerkiksi joukkorahoitustarkoituksissa BTCPay Serverissä. Xpub jaetaan online-keinoin, kun taas yksityiset avaimet pysyvät offline-tilassa HWW:ssä.                                                                                                                                                                                                                                                                           |
| F.U.D.                                             | Lyhenne sanoista Pelko, epävarmuus ja epäilys; Yleensä tarkoituksellisesti herätetty asettamaan kilpailija epäedulliseen asemaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Maksu                                              | Lightning Networkin kontekstissa solmut veloittavat reititysmaksuja muiden käyttäjien maksujen välittämisestä. Yksittäiset solmut voivat asettaa omat maksupolitiikkansa, jotka lasketaan kiinteän base_fee:n ja maksun määrästä riippuvan fee_rate:n summana. Bitcoinin kontekstissa transaktion lähettäjä maksaa transaktiomaksun louhijoille transaktion sisällyttämisestä lohkoon. Bitcoinin transaktiomaksuihin ei sisälly perusmaksua ja ne riippuvat lineaarisesti transaktion painosta, mutta eivät määrästä.                                                                                                                                                                                                                                                                                                                                                                    |
| Fiat                                               | Hallituksen liikkeeseen laskema valuutta, joka ei ole tuettu tavaralla, kuten kullalla.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Finite                                             | Viittaa Bitcoinin rajalliseen tarjontaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Fork                                               | Muutos protokollassa tai koodissa. Forkit esitellään yleensä projektin päivittämiseksi. Avointen lähdekoodien yhteisössä forkit ovat olemassa, koska monet yksilöt päättävät ladata ja suorittaa samaa ohjelmistoa eri aikoina eivätkä aina päivitä sitä. Jos kaksi käyttäjää lataa ja suorittaa version 1 ohjelmistosta, ja vain toinen käyttäjä päivittää sen, kun versio 2 julkaistaan, päivittänyt käyttäjä suorittaa version 1 forkin.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Funding Transaction                                | Transaktio, jota käytetään maksukanavan avaamiseen. Rahoitustransaktion arvo (bitcoineina) on tarkalleen maksukanavan kapasiteetti. Rahoitustransaktion tuloste on 2-of-2 multisignatuuriskripti (multisig), jossa kumpikin kanavakumppani hallitsee yhtä avainta. Sen multisig-luonteen vuoksi sitä voi käyttää vain molempien kanavakumppaneiden yhteisellä suostumuksella. Se tullaan lopulta käyttämään yhdessä sitoumusten transaktioista tai sulkemistransaktiossa.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Fungible                                           | Olla jotakin (kuten rahaa tai hyödykettä) sellaista luontoa, että yksi osa tai määrä voidaan korvata toisella samanarvoisella osalla tai määrällä velan maksamisessa tai tilin selvittämisessä                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Gap Limit                                          | Viittaa standardimäärään julkisia osoitteita, joita tarkistetaan transaktioita varten lohkoketjussa tilin saldon laskemiseksi. Osoitteen gap limitin ylittäviä transaktioita ei havaita.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Genesis Block                                      | Ensimmäinen lohko Bitcoin-lohkoketjussa. Satoshi Nakamoto, Bitcoinin luoja, louhi Genesis-lohkon 3. tammikuuta 2009 ja sisällytti siihen päivän Financial Times -lehden otsikon, “Chancellor on brink of second bailout for banks.”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Github                                             | Alusta ja pilvipohjainen palvelu ohjelmistokehitykseen ja versionhallintaan käyttäen Gitiä, joka mahdollistaa kehittäjien koodin tallentamisen ja hallinnan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Gossip Protocol                                    | LN-noodit lähettävät ja vastaanottavat tietoa Lightning Networkin topologiasta juoruviestien kautta, jotka vaihdetaan vertaistensa kanssa. Juoruprotokolla on pääasiassa määritelty BOLT #7:ssä ja määrittelee node_announcement, channel_announcement ja channel_update -viestien muodon. Roskapostin estämiseksi node announcement -viestejä välitetään vain, jos noodilla on jo kanava, ja channel announcement -viestejä välitetään vain, jos kanavan rahoitustransaktio on vahvistettu Bitcoin-verkossa. Yleensä Lightning-noodit yhdistävät kanavakumppaneihinsa, mutta on myös hyväksyttävää yhdistää mihin tahansa muuhun Lightning-noodiin käsittelemään juoruviestejä.                                                                                                                                                                                                         |
| Gresham's Law                                      | Laki, jonka mukaan “huono raha syrjäyttää hyvän”. Toisin sanoen taloudessa, jossa käytetään kahta valuuttaa, ihmiset käyttävät huonoa rahaa, joka jatkuvasti menettää arvoaan, ja pitävät hyvää rahaa, joka säilyttää arvonsa. Näin ollen huono raha hallitsee käytössä ja päivittäisissä transaktioissa, kun taas hyvä raha hallitsee säästöissä ja pitkän aikavälin sijoituksissa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Halving                                            | Tapahtuma, joka vähentää bitcoinin liikkeeseenlaskunopeuden puoleen joka 210 000 lohkon jälkeen (noin neljän vuoden välein).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Hard Fork                                          | Konsensusmuutos, joka ei ole taaksepäin yhteensopiva. Taaksepäin yhteensopimattomuus tapahtuu, kun aiemmin kelpaamaton käyttäytyminen hyväksytään kelvolliseksi. Jotta konsensus säilyisi hard forkissa, kaikkien solmujen on päivitettävä itsensä. Muutoin vanhat solmut hylkäävät siirrot tai lohkot kelvottomina vanhojen sääntöjen mukaan, kun taas päivitetyt solmut hyväksyvät ne kelvollisina. Tästä syystä Bitcoinissa vältetään hard forkeja kaikin keinoin.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Hardware Wallet (HWW)                              | Erityistyyppinen Bitcoin-lompakko, joka tallentaa käyttäjän yksityiset avaimet turvallisessa laitteistossa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Hash Function                                      | Kryptografinen hajautusfunktio on matemaattinen algoritmi, joka kuvaa mielivaltaisen kokoiset tiedot kiinteän kokoiseksi bittijonoksi (hajautusarvoksi) ja on suunniteltu yksisuuntaiseksi toiminnoksi, eli toiminnoksi, jota on käytännössä mahdoton kääntää. Ainoa tapa luoda syötetiedot uudelleen ihanteellisen kryptografisen hajautusfunktion tuloksesta on yrittää brute-force-hakua mahdollisilla syötteillä nähdäkseen, tuottavatko ne osuman.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Hash Rate                                          | Mittaus siitä, kuinka monta hajautusta louhijat tuottavat yhteensä sekunnissa Bitcoin-verkossa. Yksittäinen hajautus on yritys luoda Proof-of-Work lohkolle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Hot Wallet                                         | Laite, jolla on ulkoisia yhteyksiä, erityisesti internetiin. Hot wallet on Bitcoin-lompakko, joka yhdistää internetiin. Nämä lompakot ovat kätevämpiä päivittäiseen käyttöön, mutta eivät ole yhtä turvallisia kuin kylmäsäilytysvaihtoehdot, koska ne ovat vuorovaikutuksessa internetin kanssa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Initial Block Download (IBD)                       | Prosessi, jossa rakennetaan koko Bitcoin-lohkoketju alusta. Kun uusi solmu perustetaan ja liittyy verkkoon, se yhdistää muihin solmuihin ja pyytää niiltä lohkoja. Uusi solmu käsittelee nämä lohkot ja rakentaa lohkoketjun, kunnes se on saavuttanut ja on synkronoitu verkon kanssa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Invoice                                            | Kaupallinen asiakirja, jonka myyjä antaa ostajalle liittyen myyntitapahtumaan ja joka ilmaisee tuotteet, määrät ja tuotteista tai palveluista sovitut hinnat, jotka myyjä on toimittanut ostajalle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Know Your Customer (KYC)                           | Lait, jotka on tarkoitettu estämään rahoituslaitosten käyttö laittomiin rahansiirtoihin vaatimalla, että kaikki rahoitustilit voidaan yksilöidä yksilöihin tai organisaatioihin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Layer 2                                            | Verkko, joka on rakennettu lohkoketjun päälle, esim. Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Legacy Address                                     | Legacy-osoitteet käyttävät Base58-koodausta, ja kun legacy-osoite on julkisen avaimen hajautus, niin kutsuttu P2PKH-osoite, se alkaa ‘1’:llä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Lightning Network                                  | Protokolla Bitcoinin päällä. Se luo maksukanavien verkoston, joka mahdollistaa luottamuksettomien maksujen välittämisen verkoston kautta HTLC:iden ja sipulireitityksen avulla. Lightning Networkin muita komponentteja ovat juoruprotokolla, siirtokerros ja maksupyynnöt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Liquidity                                          | Usean ominaisuuden mittaus tietyn omaisuuserän tilauskirjassa tietyllä markkinalla. Likviditeetti on indikaattori siitä, kuinka paljon suuri tilaus vaikuttaa omaisuuserän hintaan markkinoilla. Likviditeetiltään suuremmalla omaisuuserällä on syvempi tilauskirjan syvyys. Tämä tarkoittaa, että se pystyy absorboimaan enemmän tilauksia pienemmillä hintaliikkeillä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pisin Ketju                                        | Lohkoketju, jonka rakentaminen on vaatinut eniten työtä. Nimetty näin, koska intuitiivisesti lohkoketju, jossa on enemmän lohkoja, on vaatinut enemmän energiaa rakentaa kuin ketju, jossa on vähemmän lohkoja. Tarkemmin sanottuna se on ketju, jonka tuottaminen on vaatinut eniten työtä, joten parempi nimi olisi voinut olla "painavin ketju."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Pääketju                                           | Lightning Networkin kontekstissa viittaa Bitcoin-verkkoon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Vaihdon Väline                                     | Hyödykkeen tyyppi, joka helpottaa muiden hyödykkeiden ja palveluiden vaihtoa taloudessa. Historiallisesti esimerkiksi simpukankuoret, helmet ja kulta ovat toimineet vaihdon välineinä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Mempool                                            | Lyhenne sanoista "memory pool", väliaikainen säilytyspaikka solmulle vastaanotetuille transaktioille.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Louhija                                            | Solmu, joka osallistuu lohkoketjun rakentamiseen lisäämällä uusia lohkoja hashauksen prosessin kautta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Louhinta                                           | Prosessi, jossa rakennetaan lohko viimeaikaisista Bitcoin-transaktioista ja ratkaistaan laskennallinen ongelma työn todisteena. Se on prosessi, jonka kautta jaettu bitcoin-kirjanpito (eli Bitcoin-lohkoketju) päivitetään ja johon uudet transaktiot sisällytetään. Se on myös prosessi, jonka kautta uusi bitcoin lasketaan liikkeelle. Joka kerta kun uusi lohko luodaan, louhiva solmu saa uutta bitcoinia kyseisen lohkon coinbase-transaktiossa.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Moniallekirjoitus (multisig)                       | Käsikirjoitus, joka vaatii useampaa kuin yhtä allekirjoitusta varojen käytön valtuuttamiseen. Maksukanavat koodataan aina multisig-osoitteiksi, jotka vaativat yhden allekirjoituksen kultakin maksukanavan osapuolelta. Kahden osapuolen maksukanavan standarditapauksessa käytetään 2-of-2 multisig-osoitetta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Solmu                                              | Tietokone, joka osallistuu verkkoon. Erityisesti Bitcoin- tai Lightning-verkkoihin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Lähtö                                              | Bitcoinien paketti, joka luodaan bitcoin-transaktiossa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Lähdön Lukitus                                     | Joukko vaatimuksia, jotka on asetettu lähdölle. Nämä vaatimukset on täytettävä, jotta lähtöä voidaan käyttää transaktiossa. Yleisin esimerkki on yksinkertainen vaatimus yksityisen avaimen hallussapidosta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| P2SH Osoite                                        | P2SH-osoitteet ovat Base58Check-koodauksia 20-tavuisesta skriptin hashista. P2SH-osoitteet alkavat "3":lla. P2SH-osoitteet piilottavat kaiken monimutkaisuuden, jotta maksun lähettäjä ei näe skriptiä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| P2WPKH Osoite                                      | "Native SegWit v0" osoiteformaatti, P2WPKH-osoitteet ovat bech32-koodattuja ja alkavat "bc1q":lla.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| P2WSH Osoite                                       | "Native SegWit v0" skriptiosoiteformaatti, P2WSH-osoitteet ovat bech32-koodattuja ja alkavat "bc1q":lla.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Osittain Allekirjoitettu Bitcoin Transaktio (PSBT) | Bitcoin-standardi, joka helpottaa allekirjoittamattomien transaktioiden siirrettävyyttä, mikä mahdollistaa useiden osapuolten helposti allekirjoittaa saman transaktion. Tämä on hyödyllisintä, kun useat osapuolet haluavat lisätä syötteitä samaan transaktioon. PSBT esiteltiin BIP 174:ssä, ja se mahdollistaa käyttäjien helpommin allekirjoittaa transaktioita kylmäsäilylaitteella ja sitten lähettää allekirjoitetun transaktion laitteesta, joka on yhdistetty internetiin.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Reitinhaku                                         | Prosessi maksureitin löytämiseksi lähteestä määränpäähän Lightning-verkossa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pay-to-Public-Key-Hash (P2PKH)                     | P2PKH on tyyppiä output, joka lukitsee bitcoinin julkisen avaimen hashiin. Output, joka on lukittu P2PKH-skriptillä, voidaan avata (kuluttaa) esittämällä hashia vastaava julkinen avain ja digitaalinen allekirjoitus, jonka vastaava yksityinen avain on luonut.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Pay-to-Script-Hash (P2SH)                          | P2SH on monipuolinen output-tyyppi, joka mahdollistaa monimutkaisten Bitcoin-skriptien käytön. P2SH:n avulla monimutkainen skripti, joka määrittelee ehdot outputin kuluttamiselle (lunastusskripti), ei esitetä lukitsevassa skriptissä. Sen sijaan arvo lukitaan skriptin hashiin, joka on esitettävä ja täytettävä outputin kuluttamiseksi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pay-to-Taproot (P2TR)                              | Taproot, joka aktivoitui marraskuussa 2021, on uusi output-tyyppi, joka lukitsee bitcoinin puuhun, jossa on kulutusehtoja, tai yhteen juuriehtoon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Pay-to-Witness-Public-Key-Hash (P2WPKH)            | P2WPKH on P2PKH:n SegWit-vastine, jossa käytetään erillistä todistajaa. Allekirjoitus P2WPKH-outputin kuluttamiseksi sijoitetaan todistajapuuhun ScriptSig-kentän sijaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pay-to-Witness-Script-Hash (P2WSH)                 | P2WSH on P2SH:n SegWit-vastine, jossa käytetään erillistä todistajaa. Allekirjoitus ja skripti P2WSH-outputin kuluttamiseksi sijoitetaan todistajapuuhun ScriptSig-kentän sijaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Payjoin                                            | Erityistyyppinen Bitcoin-siirto, jossa sekä lähettäjä että vastaanottaja antavat panoksia rikkoakseen yleisen panoksen omistusolettamuksen, oletuksen, jota käytetään poistamaan yksityisyyttä bitcoin-käyttäjiltä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Maksukanava                                        | Rahoitussuhde kahden solmun välillä Lightning-verkossa, luotu käyttäen bitcoin-siirtoa, joka maksaa moniallekirjoitusosoitteeseen. Kanavakumppanit voivat käyttää kanavaa lähettääkseen bitcoineja edestakaisin toisilleen ilman, että kaikkia siirtoja tarvitsee lisätä Bitcoin-lohkoketjuun. Tyypillisessä maksukanavassa vain kaksi siirtoa, rahoitussiirto ja sitoutumissiirto, lisätään lohkoketjuun. Kanavan kautta lähetetyt maksut eivät kirjaudu lohkoketjuun ja sanotaan tapahtuvan "off-chain".                                                                                                                                                                                                                                                                                                                                                                               |
| Maksupyyntö                                        | Ominaisuus, joka mahdollistaa BTCPay-kaupan omistajien luoda pitkäikäisiä laskuja. Maksupyyntöön maksetut varat käyttävät maksuhetken vaihtokurssia. Tämä mahdollistaa käyttäjien suorittaa maksuja heidän mukavuutensa mukaan ilman, että heidän tarvitsee neuvotella tai varmistaa vaihtokurssit kaupan omistajan kanssa maksuhetkellä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Maksatus                                           | Maksatusominaisuus on sidottu Pull Payments -toimintoon. Tämä ominaisuus mahdollistaa pull payment -maksujen (hyvitykset, palkanmaksut tai nostot) käsittelyn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Lisäosa                                            | Ohjelmistolisä, joka asennetaan ohjelmaan parantamaan sen ominaisuuksia.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Point Of Sale (PoS)                                | BTCPay Serverin oletuslisäosa, joka mahdollistaa kaupan omistajan luoda verkkokaupan suoraan BTCPay Serverista. Kaupan omistajan ei tarvitse mitään kolmannen osapuolen e-commerce-ratkaisuja pyörittääkseen verkkokauppaa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Kannettavuus                                       | Hyödykkeen kykyä kuljettaa helposti paikasta toiseen. Kannettavuus on tärkeä ominaisuus äänen rahalle; jotta raha voidaan laajasti hyväksyä ja siten käyttää, sen on kyettävä liikkumaan rajat yli, yksilöiden välillä ja pitkiä matkoja suhteellisen helposti.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Proof Of Work (PoW)                                | Data, jonka löytäminen vaatii merkittävää laskentatehoa, ja jonka kuka tahansa voi helposti todentaa todistaakseen työmäärän, joka sen tuottamiseen vaadittiin. Bitcoinissa louhijoiden on löydettävä numeerinen ratkaisu SHA-256 -algoritmiin, joka täyttää verkoston laajuisen tavoitteen, kutsuttuna vaikeustavoitteeksi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Nimimerkki                                         | Keinotekoinen nimi, jota yksilöt käyttävät suojatakseen henkilöllisyytensä tai rakentaakseen mainetta erillään todellisesta henkilöllisyydestään. Julkisia avaimia käytetään sallimaan Bitcoin-käyttäjien vastaanottaa bitcoineja samalla pysyen nimimerkillä suhteessa lohkoketjuun.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Julkisen ja yksityisen avaimen kryptografia        | Käsittää avainparin, joka tunnetaan julkisena avaimena ja yksityisenä avaimena, jotka liittyvät yksikköön, joka tarvitsee todentaa henkilöllisyytensä sähköisesti tai allekirjoittaa tai salata dataa. Julkinen avain julkaistaan ja vastaava yksityinen avain pidetään salassa. Data, joka on salattu julkisella avaimella, voidaan purkaa vain vastaavalla yksityisellä avaimella.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Julkinen/Yksityinen Avain                          | Avainpari, jota käytetään julkisen avaimen kryptografiassa. Julkinen avain jaetaan avoimesti muiden kanssa, ja sitä voidaan pitää tilinumerona, kun taas yksityinen avain pidetään salassa ja sitä voidaan pitää salasanana.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pull-maksu                                         | Perinteisesti Bitcoin-maksun tekemiseksi vastaanottaja jakaa bitcoin-osoitteensa ja lähettäjä lähettää myöhemmin rahaa tähän osoitteeseen. Tällaista järjestelmää kutsutaan push-maksuksi, koska lähettäjä aloittaa maksun, kun taas vastaanottaja voi olla tavoittamattomissa, käytännössä työntäen maksun vastaanottajalle. Tyypillisen skenaarion sijaan, jossa lähettäjä "työntää" maksun, lähettäjä sallii vastaanottajan vetää maksun silloin, kun vastaanottaja pitää sitä sopivana.                                                                                                                                                                                                                                                                                                                                                                                              |
| Kaninkolo                                          | Viittaus Liisa Ihmemaassa, jossa sankari aloittaa seikkailunsa astumalla kaninkoloon. Bitcoinin yhteydessä se viittaa näennäisesti loputtomiin aiheisiin, joita tutkii ja näkee uudessa valossa, kun on alkanut ymmärtää Bitcoinia.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Vastaanottaa                                       | Prosessi, jossa bitcoineja lähetetään annettuun osoitteeseen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Rekisteröityä                                      | Prosessi, jossa luodaan tili tai kirjaudutaan palveluun tyypillisesti valitsemalla käyttäjänimi ja salasana.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Korvaa Maksulla (RBF)                              | Bitcoin-siirto voidaan merkitä RBF:ksi, jotta lähettäjä voi korvata tämän siirron toisella samankaltaisella siirrolla, joka maksaa korkeamman maksun. Tämä mekanismi on olemassa, jotta käyttäjät voivat reagoida, jos verkko tulee ruuhkautuneeksi ja maksut nousevat odottamatta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Repositorio                                        | Versiohallintajärjestelmissä repositorio on tietorakenne, joka tallentaa metadataa tiedostojen tai hakemistorakenteen joukolle.[1] Riippuen käytössä olevasta versiohallintajärjestelmästä, onko se hajautettu, kuten Git tai Mercurial, vai keskitetty, kuten Subversion, CVS tai Perforce, koko tietojoukko repositoriossa voidaan kopioida jokaisen käyttäjän järjestelmään tai sitä voidaan ylläpitää yhdellä palvelimella.[2] Joitakin metadataa, jota repositorio sisältää, ovat muun muassa historiallinen muutoskirja repositoriossa, joukko commit-objekteja ja joukko viittauksia commit-objekteihin, kutsutaan päiksi.                                                                                                                                                                                                                                                        |
| Rescan                                             | Prosessi, jossa skannataan nykyisen UTXO-setin tila kolikoille, jotka kuuluvat aiemmin määritettyyn johdannaiskaavaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Revokation Key                                     | Jokainen peruutettavissa oleva sekvenssin kypsyys sopimus (RSMC) sisältää kaksi peruutusavainta. Kumpikin kanavakumppani tuntee yhden peruutusavaimen. Tietäen molemmat peruutusavaimet, RSMC:n tuotto voidaan käyttää ennalta määritellyn aikarajan sisällä. Neuvotellessa uudesta kanavatilasta, vanhat peruutusavaimet jaetaan, näin "peruuttaen" vanhan tilan. Peruutusavaimia käytetään estämään kanavakumppaneita lähettämästä vanhaa kanavatilaa.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Routing                                            | Prosessi, jossa käytetään Lightning Networkin polkua maksun tekemiseen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Routing Fees                                       | Lightning Networkissa, maksut, joita veloitetaan muiden käyttäjien maksujen välittämisestä. Yksittäiset solmut voivat asettaa omat maksupolitiikkansa, jotka lasketaan kiinteän base_fee:n ja maksun määrästä riippuvan fee_rate:n summana.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Salability                                         | Kuinka helposti hyödyke voidaan myydä markkinoilla milloin tahansa sen haltija haluaa, vähimmäisellä hinnan menetyksellä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Satoshi (sat)                                      | Satoshi on pienin yksikkö (nimellisarvo), joka voidaan kirjata bitcoinin blockchainiin. Yksi satoshi on 1/100 miljoonasosa (0.00000001) bitcoinista ja se on nimetty Bitcoinin luoja, Satoshi Nakamoton mukaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Satoshi Nakamoto                                   | Nimi, jota käytti henkilö tai henkilöryhmä, joka suunnitteli Bitcoinin ja loi sen alkuperäisen viiteimplementaation. Implementaation osana he kehittivät myös ensimmäisen blockchain-tietokannan. Prosessissa he olivat ensimmäisiä, jotka ratkaisivat digitaalisen valuutan kaksinkertaisen kulutuksen ongelman. Heidän todellinen henkilöllisyytensä pysyy tuntemattomana.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Satoshi Per Byte                                   | Yksikkö, jolla mitataan transaktion prioriteettia, määriteltynä transaktion maksuna satosheina jaettuna transaktion koolla tavuina.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Satoshi Per Verabyte                               | Samankaltainen käsite kuin Satoshi Per Byte, mutta uudemmille osoitteille, jotka käyttävät Segwit-tekniikkaa. Yhtä suuri kuin transaktion koko Weight-yksiköissä jaettuna neljällä. Weight-yksiköt lasketaan ottamalla transaktion koko (ilman todistajaa) kertaa kolme, lisättynä transaktion kokoon sisältäen todistajan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Scarcity                                           | Hyödykkeen ominaisuus, jota ei voida tuottaa kustannustehokkaasti. Niukkuus ei riipu olemassa olevien hyödykeyksiköiden määrästä, vaan pikemminkin lisäyksiköiden tuottamisen kustannuksista.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Script                                             | Bitcoin käyttää transaktioissaan skriptausjärjestelmää nimeltä Bitcoin Script. Se muistuttaa Forth-ohjelmointikieltä, on yksinkertainen, pinoon perustuva ja käsitellään vasemmalta oikealle. Se on tarkoituksella Turing-epätäydellinen, ilman silmukoita tai rekursiota.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Seed Phrase                                        | Sanojen lista, joka tallentaa kaiken tarvittavan tiedon Bitcoin-varojen palauttamiseksi ketjussa. Lompakko-ohjelmisto tyypillisesti generoi siemenlauseen ja ohjeistaa käyttäjää kirjoittamaan sen paperille. Jos käyttäjän tietokone hajoaa tai kovalevy vioittuu, he voivat ladata saman lompakko-ohjelmiston uudelleen ja käyttää paperivarmuuskopiota bitcoiniensa takaisin saamiseksi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Segregated Witness (SegWit)                        | Segregated Witness (SegWit) on päivitys Bitcoin-protokollaan, joka otettiin käyttöön vuonna 2017. Se lisää uuden todisteen allekirjoituksille ja muille transaktioiden valtuutustodisteille. Tämä uusi todistekenttä on vapautettu transaktion tunnisteen laskennasta, mikä ratkaisee suurimman osan kolmansien osapuolien transaktioiden muunneltavuudesta. Segregated Witness otettiin käyttöön pehmeänä haarautumisena (soft fork), ja se on tekninen muutos, joka tekee Bitcoinin protokollan säännöistä rajoittavampia.                                                                                                                                                                                                                                                                                                                                                             |
| Self-Sovereignty                                   | Malli digitaalisten identiteettien hallintaan, jossa yksilöillä tai yrityksillä on yksinomainen omistusoikeus hallita tilejään ja henkilökohtaisia tietojaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Send                                               | Bitcoinien siirtoprosessi osoitteeseen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Sensitivity Mode                                   | Aktivoitavissa kaupan asetuksista, aktivointi saa aikaan numeeristen arvojen (esim. bitcoin-määrä) peittämisen kaikissa näkymissä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Server Settings                                    | Asetukset BTCPay Serverissä, jotka ovat voimassa palvelimen laajuisesti (toisin kuin Store Settings, jotka ovat rajattuja yhden kaupan laajuuteen).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| SHA-256                                            | Kryptografinen hajautusfunktio. Kuuluu turvallisten hajautusfunktioiden (SHA) perheeseen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Shopify                                            | Kanadalainen monikansallinen e-kauppayritys, jonka pääkonttori on Ottawassa, Ontariossa. Shopify on sen omaisuutta olevan e-kauppa-alustan nimi verkko- ja myymäläpistejärjestelmille.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SMTP                                               | Simple Mail Transfer Protocol on Internet-standardi sähköpostin lähettämisen viestintäprotokolla.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Soft Fork                                          | Protokollapäivitys, joka on yhteensopiva sekä vanhojen että uusien solmujen kanssa, mahdollistaen molempien jatkavan saman ketjun käyttöä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Software Stack                                     | Tietotekniikassa ratkaisupino tai ohjelmistopino on joukko ohjelmistoalijärjestelmiä tai komponentteja, jotka tarvitaan täydellisen alustan luomiseen siten, että sovellukset eivät tarvitse lisäohjelmistoa toimiakseen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Store                                              | Kauppa BTCPay Serverissä voidaan nähdä "kotina" tietylle bitcoin-lompakolle, laajentuen kaikilla BTCPay Serverin ominaisuuksilla.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Store Settings                                     | Asetukset BTCPay Serverissä, jotka ovat spesifisiä kaupalle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Taproot                                            | Päivitys Bitcoiniin, joka esittelisi useita uusia ominaisuuksia. Päivitys on kuvattu BIPeissä 340, 341 ja 342, ja se esittelee Schnorrin allekirjoitusjärjestelmän, Taprootin ja Tapscriptin. Yhdessä nämä päivitykset tuovat uusia, tehokkaampia, joustavampia ja yksityisempiä tapoja siirtää bitcoineja.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Thier's Law                                        | Laki, jonka mukaan hyvä raha syrjäyttää huonon rahan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Third-Party Host                                   | Kun yksilön tai yrityksen verkkosivusto toimii toisen yrityksen omistamilla ja hallinnoimilla palvelimilla. Vaihtoehtona on, että verkkosivustosi isännöidään omilla palvelimillasi omassa datakeskuksessasi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Timelock                                           | Timelock on tyyppiä oleva este, joka rajoittaa tiettyjen bitcoinien käyttöä ennen määrättyä tulevaa aikaa tai lohkokorkeutta. Timelockit ovat merkittävässä roolissa monissa Bitcoin-sopimuksissa, mukaan lukien maksukanavat ja HTLC:t.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Topologia                                          | Lightning Networkin topologia kuvaa Lightning Networkin muotoa matemaattisena graafina. Graafin solmut ovat Lightning-solmuja (verkon osallistujat/vertaiset). Graafin reunat ovat maksukanavia. Lightning Networkin topologia lähetetään julkisesti gossip-protokollan avulla, lukuun ottamatta ilmoittamattomia kanavia. Tämä tarkoittaa, että Lightning Network voi olla merkittävästi suurempi kuin ilmoitettu kanavien ja solmujen määrä. Topologian tunteminen on erityisen kiinnostavaa maksujen lähteeseen perustuvassa reititysprosessissa, jossa lähettäjä löytää reitin.                                                                                                                                                                                                                                                                                                      |
| Tapahtuma                                          | Tapahtumat ovat tietorakenteita, joita Bitcoin käyttää siirtämään bitcoineja yhdestä osoitteesta toiseen. Useita tuhansia tapahtumia aggregoidaan lohkoon, joka sitten kirjataan (louhitaan) lohkoketjuun. Jokaisen lohkon ensimmäinen tapahtuma, jota kutsutaan coinbase-tapahtumaksi, luo uusia bitcoineja.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Tapahtuma-ID                                       | Kirjain- ja numeroyhdistelmä, joka tunnistaa tietyn tapahtuman lohkoketjussa. Merkkijono on yksinkertaisesti tapahtuman kaksinkertainen SHA-256 -tiiviste. Tätä tiivistettä voidaan käyttää tapahtuman etsimiseen solmusta tai lohkojen tutkijasta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Kahden tekijän tunnistautuminen (2FA)              | Identiteetin ja pääsyn hallinnan turvamenetelmä, joka vaatii kaksi tunnistautumismuotoa resurssien ja tietojen käyttöön, usein toisen laitteen lisäksi standardin kirjautumissalasanan lisäksi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Sensuroimaton                                      | Ominaisuus, jonka mukaan mikään taho ei pysty kumoamaan Bitcoin-tapahtumaa tai mustalistamaan lompakkoa tai osoitetta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Takavarikoimaton                                   | Ominaisuus, jonka mukaan mikään taho ei voi ottaa bitcoineja toiselta taholta vastoin heidän tahtoaan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Käyttämättömät Tapahtuma-Outputit (UTXO)           | Vielä käyttämättömät outputit, joten ne ovat käytettävissä uusissa tapahtumissa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Käyttäjäkokemus (UX)                               | Miten käyttäjä interactoi ja kokee tuotteen, järjestelmän tai palvelun. Se sisältää henkilön käsitykset hyödyllisyydestä, helppokäyttöisyydestä ja tehokkuudesta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Käyttöliittymä (UI)                                | Ihmisen ja tietokoneen vuorovaikutuksen ja kommunikaation piste laitteessa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Todennettavissa                                    | Hyödykkeen ominaisuus, joka voidaan helposti erottaa huijauksista ja väärennöksistä.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Virtuaalinen                                       | Olemassa tai simuloitu tietokoneessa tai tietokoneverkossa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Virtuaalikone (VM)                                 | Tietotekniikassa virtuaalikone on tietokonejärjestelmän virtualisointi tai emulointi. Virtuaalikoneet perustuvat tietokonearkkitehtuureihin ja tarjoavat fyysisen tietokoneen toiminnallisuuden. Niiden toteutukset voivat sisältää erikoistunutta laitteistoa, ohjelmistoa tai molempien yhdistelmän.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Virtuaalinen yksityinen palvelin                   | Virtuaalinen yksityinen palvelin on virtuaalikone, jota myydään palveluna Internet-isäntäpalvelun toimesta. Termillä "virtuaalinen omistettu palvelin" on samankaltainen merkitys. Virtuaalinen yksityinen palvelin suorittaa oman käyttöjärjestelmänsä kopion, ja asiakkailla voi olla superkäyttäjätason pääsy kyseiseen käyttöjärjestelmäinstanssiin, joten he voivat asentaa lähes minkä tahansa ohjelmiston, joka toimii kyseisessä käyttöjärjestelmässä                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Volatiliteetti                                     | Mittari, joka kuvaa omaisuuserän hinnan vaihtelun asteen ajan kuluessa. Omaisuuserät, jotka kokevat suuria hinnanmuutoksia säännöllisesti, ovat volatiilisempia, kun taas omaisuuserät, joilla on vakaampi hinta, ovat vähemmän volatiilisia.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Lompakko                                           | Bitcoin-lompakot säilyttävät käyttäjän avaimia, mahdollistaen käyttäjien vastaanottaa bitcoineja, allekirjoittaa siirtoja ja tarkistaa tilinsä saldon. Yksityiset ja julkiset avaimet, jotka bitcoin-lompakko sisältää, palvelevat kahta erillistä toimintoa, mutta ne on sidottu yhteen luomisvaiheessa. Bitcoin-lompakot sisältävät käyttäjän avaimia, ei heidän varsinaisia bitcoinejaan. Käsitteellisesti lompakko on kuin avainnippu siinä mielessä, että se pitää sisällään monta paria yksityisiä ja julkisia avaimia. Näitä avaimia käytetään siirtojen allekirjoittamiseen, mahdollistaen käyttäjän todistaa omistavansa siirtojen tulosteet lohkoketjussa, eli heidän bitcoininsa. Kaikki bitcoin on tallennettu lohkoketjuun siirtojen tulosteiden muodossa.                                                                                                                  |
| Wasabi Lompakko                                    | Avointa lähdekoodia oleva, ei-huoltaja, yksityisyyteen keskittyvä Bitcoin-lompakko Desktopille, joka toteuttaa luottamuksetonta CoinJoinia.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Vain seuranta -lompakko                            | Bitcoin-lompakot, jotka mahdollistavat bitcoiniesi seurannan kylmässä säilytyksessä samalla kun estävät varojen käytön. Tämä johtuu siitä, että vain seuranta -lompakot eivät säilytä tai käytä yksityisiä avaimia, ja ovat siksi kykenemättömiä valtuuttamaan minkäänlaisia käyttäjän puolesta tehtäviä menoja.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Valas                                              | Bitcoinin kontekstissa valas on henkilö, joka omistaa suuren määrän bitcoineja.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| White-Label                                        | White-label -tuote on tuote tai palvelu, jonka yksi yritys tuottaa ja jonka muut yritykset brändäävät uudelleen näyttääkseen siltä, kuin he olisivat sen tehneet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Whitepaper                                         | Esittelee uuden idean tai aiheen keskustelua varten. Bitcoinin whitepaper esitteli Bitcoinin “Vertaisverkkoon perustuvana elektronisena käteisjärjestelmänä”, joka “ei vaadi luotettuja kolmansia osapuolia”. Satoshi Nakamoto julkaisi whitepaperin 31. lokakuuta 2008 sähköpostilistalle, joka koostui kryptografeista ja cypherpunkeista.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Wrapped Segwit                                     | Suunnittelutoteutus, joka sisältyi SegWit-päivitykseen ja jonka tarkoituksena oli mahdollistaa lompakoiden ja muiden Bitcoin-ohjelmistojen helpompi tuki SegWitille. Tämän saavuttamiseksi kaksi alkuperäistä SegWit-skriptiä, P2WPKH ja P2WSH, käytetään “redeemScriptinä” P2SH-siirrossa, tuottaen wrapped SegWit -skriptityypit P2SH-P2WPKH ja P2SH-P2WSH vastaavasti.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

![kuva](assets/en/129.webp)
