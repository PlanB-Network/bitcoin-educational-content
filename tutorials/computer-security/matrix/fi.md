---
name: Matrix
description: Opas Matrixin, turvallisen, avoimen ja hajautetun viestintäalustan ymmärtämiseen, konfigurointiin ja käyttöön.
---

![cover](assets/cover.webp)



## Mikä on Matrix?



Matrix on **hajautettu viestintäprotokolla**, joka on suunniteltu mahdollistamaan viestien, tiedostojen ja ääni-/videopuheluiden vaihto käyttäjien ja sovellusten välillä ilman riippuvuutta keskusyrityksestä. Toisin kuin perinteiset viestialustat, Matrix on **avoin infrastruktuuri**, joka on verrattavissa sähköpostiin: kuka tahansa voi valita palvelimen tai ylläpitää sitä itse, mutta säilyttää samalla kyvyn vaihtaa tietoja muun verkon kanssa.



Matrixille on ominaista kolme perusperiaatetta:



### Protokolla, ei sovellus



Matrix ei ole WhatsAppin tai Telegram:n kaltainen sovellus.


Se on standardoitu kieli, jota monet sovellukset voivat käyttää.


Toisin sanoen monet erilaiset Element-ohjelmistot, FluffyChat, Cinny, Nheko ja muut, tarjoavat pääsyn samaan Matrix-verkkoon.



Tämä takaa täydellisen vapauden: sovelluksen vaihtaminen ilman yhteyksien katoamista, liitäntöjen moninaisuus ja riippumattomuus yhdestä toimittajasta.



![capture](assets/fr/03.webp)



### Hajautettu, yhdistetty verkko



Matrixin rakenne perustuu **federaatioon**, malliin, jossa useat itsenäiset palvelimet tekevät yhteistyötä keskenään.


Kukin palvelin (nimeltään _homeserver_) voi isännöidä käyttäjiä, ylläpitää chat-huoneita ja synkronoida viestejä verkon muiden palvelimien kanssa.


Näin :





- mikään yksittäinen taho ei hallitse koko järjestelmää;
- palvelin voi kadota vaikuttamatta muuhun verkkoon;
- kukin organisaatio tai yksityishenkilö voi hallinnoida omaa tilaansa.



Tämä malli takaa **korkean kestävyyden** ja heijastaa teknologisen suvereniteetin arvoja.



![capture](assets/fr/03.webp)



### Turvallinen, salattu järjestelmä



Matrix tukee **loppupäästä-päähän-salausta (E2EE)** yksityistä vaihtoa ja salattuja ryhmiä varten.


Viestejä voivat lukea vain osallistujat, eivät välipalvelimet.


Tämä lähestymistapa mahdollistaa viestinnän paljastamatta viestien sisältöä kolmannelle osapuolelle, säilyttäen samalla protokollan avoimuuden ja mahdollisuuden ylläpitää omaa palvelinta.



![capture](assets/fr/05.webp)



### Ainutlaatuinen yhteentoimivuus



Yksi Matrixin suurimmista eduista on sen kyky toimia **siltana eri viestintäjärjestelmien välillä**. _siltojen_ ansiosta on mahdollista yhdistää :





- Telegram
- WhatsApp
- Signal
- Messenger
- Slack
- Keskustelu
- IRC, XMPP jne.



Tämä mahdollistaa useille eri alustoille hajautettujen yhteisöjen yhdistämisen ja samalla infrastruktuurin hallinnan säilyttämisen.



![capture](assets/fr/06.webp)



## Miten Matrix toimii?



Tässä osassa esitellään Matrix-verkon sisäinen rakenne, jotta ymmärretään, miten käyttäjät, palvelimet ja sovellukset ovat vuorovaikutuksessa tässä hajautetussa ekosysteemissä. Matrix perustuu kolmeen keskeiseen elementtiin: _kotipalvelimet_, identiteetit ja _asiakkaat_, joita käytetään viestintään.



### Palvelimet: kotipalvelimet



Matrix toimii itsenäisillä palvelimilla, joita kutsutaan _kotipalvelimiksi_.


Kukin kotipalvelin hallinnoi :





- sen isännöimät käyttäjätilit,
- yksityiset keskustelut ja oleskelutilat, joihin nämä käyttäjät osallistuvat,
- synkronointi muiden verkkopalvelimien kanssa.



Kaikki Matrix-verkkoon liitetyt kotipalvelimet vaihtavat automaattisesti viestejä ja tapahtumia yhteisistä olohuoneista. Esim:





- palvelimelle A rekisteröitynyt käyttäjä voi keskustella palvelimella B olevan käyttäjän kanssa,
- salonki voi olla hajautettu kymmenille palvelimille,
- kukaan ei voi hallita salonkia tai koko yhteisöä.



Tämä malli on erittäin joustava, ja sen avulla jokainen organisaatio tai yksityishenkilö voi hallita omaa infrastruktuuriaan.



### Matriisitunnisteet



Jokaisella käyttäjällä on yksilöllinen tunniste, nimeltään **MXID** (_Matrix ID_), joka muistuttaa osoitetta:



```bash
@nomdutilisateur:serveur.xyz
```



Se koostuu :





- käyttäjänimi, jota edeltää **@***
- sen palvelimen nimi, jolla tili on luotu, jota edeltää **:**



Esimerkkejä:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Tämä tunniste mahdollistaa yhteydenpidon minkä tahansa muun Matrix-käyttäjän kanssa riippumatta siitä, mistä palvelimesta se on peräisin.



### Matrix-asiakkaat (sovellukset)



Matrixin käyttöä varten sinun on muodostettava yhteys sovellukseen nimeltä **client Matrix**.



Tunnetuimpia ovat :





- Elementti (web, mobiili, työpöytä)
- FluffyChat (mobiili)
- Cinny (minimalistinen web/desktop)
- Nheko (työpöytä)



Nämä sovellukset ovat vain rajapintoja :





- tarkastella viestejä,
- lähettää tekstiä, kuvia tai tiedostoja,
- liittyä messuille tai luoda niitä,
- soittaa audio/videopuheluita.



Kaikki sovellukset kommunikoivat palvelimien kanssa saman standardoidun protokollan avulla.



### Huoneet ja yksityisviestit (DM)



Matrixissa vaihto tapahtuu **huoneissa** :





- huone voi olla julkinen tai yksityinen
- siihen mahtuu kaksi ihmistä tai tuhansia
- se voidaan jakaa usean palvelimen kesken
- sillä on yksilöllinen tunniste, joka alkaa kirjaimella **!**



Yksityisviestit ovat yksinkertaisesti kahden osallistujan keskusteluhuoneita, joihin viitataan usein nimellä **DM (Direct Messages)**.



Salonkien synkronointi tapahtuu reaaliajassa osallistuvien palvelimien välillä, mikä takaa saumattoman kokemuksen ja säilyttää samalla hajautuksen.



## Miksi käyttää Matrixia?



Matrix ei ole vain vaihtoehto keskitetyille sanomanvälitysjärjestelmille: se on teknologia, joka vastaa todellisiin tarpeisiin digitaalisen riippumattomuuden, turvallisuuden ja yhteentoimivuuden osalta. On monia syitä, miksi yhä useammat ihmiset, yritykset ja laitokset valitsevat tämän protokollan viestintään.



### Viestinnän hallinta takaisin



Useimmat viestialustat toimivat keskitetyn mallin mukaisesti: yksi toimija hallitsee palvelimia, pääsyä, tietoja ja käyttösääntöjä. Tämä malli merkitsee täydellistä riippuvuutta toimittajasta.


Matrixilla on erilainen lähestymistapa.


Kuka tahansa voi valita, missä isännöi tiliään, tai jopa ottaa käyttöön oman palvelimensa. Mikään taho ei voi estää käyttäjää, vaatia tunkeilevaa tunnistamista tai määrätä toimintatapojen muutosta.


Tämä arkkitehtuuri antaa autonomian takaisin sekä yksilöille että organisaatioille. Viestintä ei enää perustu luottamukseen yritystä kohtaan vaan avoimeen, dokumentoituun ja todennettavissa olevaan protokollaan.



### Turvallinen, salattu viestintä



Matrix tukee päästä päähän -salausta yksityisille keskusteluille ja ryhmille. Tämä mekanismi varmistaa, että vain osallistujat voivat lukea viestejä, vaikka ne kulkisivat kolmannen osapuolen palvelimien kautta federaatiossa.



Protokolla käyttää Megolm/Olm-algoritmia, joka on suunniteltu erityisesti tarjoamaan vahvaa tietoturvaa hajautetuissa, useita laitteita sisältävissä ympäristöissä.



Tämä mahdollistaa :





- suojella arkaluonteisia keskusteluja,
- estää luvattoman käytön (myös isäntäpalvelimelta),
- säilyttää luottamuksellisuus pitkällä aikavälillä.



Salaus ei ole vaihtoehto: se on protokollan keskeinen osa.



### Ei enää riippuvainen yhdestä sovelluksesta



Matrix ei ole sovellus vaan protokolla.



Tämä asiakkaiden moninaisuus takaa :





- yksilöllisiin tarpeisiin mukautettu valinta,
- mahdollisuus käyttää Matrixia millä tahansa laitteella,
- ei riippuvuutta yhdestä ohjelmistosta.



Jos asiakas on sopimaton tai lakkaa ylläpitämästä tiliä, voit yksinkertaisesti valita toisen asiakkaan: tili jatkaa toimintaansa normaalisti.



### Eri yhteisöjen yhdistäminen ja yhteenliittäminen



Federaation avulla eri palvelimet voivat työskennellä yhdessä, vaikka niitä hallitaan itsenäisesti.


Näin :





- organisaatio voi hallita omaa kotipalvelinta,
- yksityishenkilöt voivat liittyä julkisiin palvelimiin,
- kaikki voivat kommunikoida keskenään kuin olisivat samalla alustalla.



Tämän joustavuuden ansiosta on mahdollista luoda viestintätiloja, jotka soveltuvat kaikkiin tarpeisiin: tiimeihin, yhdistyksiin, yhteisöihin, instituutioihin tai avoimen lähdekoodin projekteihin.



Matrix on erityisen suosittu teknisissä piireissä, aktivistikollektiivien, tutkijoiden, hallitusten ja yhä useammin Bitcoin-yhteisöjen keskuudessa.



### Ainutlaatuinen yhteentoimivuus viestimissä



Yksi Matrixin suurimmista eduista on sen kyky **laajentaa** vaihtoja sillan avulla, joka pystyy yhdistämään :





- WhatsApp
- Telegram
- Signal
- Slack
- Keskustelu
- IRC
- XMPP
- ja monet muut alustat



Matrixista tulee näin viestinnän yhdistävä kerros, joka kokoaa yhteen useita eri sovelluksiin hajallaan olevia yhteisöjä.



Yhteentoimivuus vähentää pirstaleisuutta ja yksinkertaistaa yhteistyötä.



### Vapaa, avoin ja kestävä protokolla



Matrix-protokolla on täysin avoimen lähdekoodin ja avoimesti kehitetty.


Tämä takaa useita etuja:





- standardin jatkuva kehittäminen,
- kuka tahansa voi tarkistaa koodin,
- riippumattomuus kaupallisista tai poliittisista muutoksista,
- pitkän aikavälin kestävyys.



Toisin kuin proprietääriset sanomanvälitysjärjestelmät, Matrixin tulevaisuus ei ole riippuvainen yhdestä ainoasta yrityksestä vaan maailmanlaajuisesta yhteisöstä ja avoimesta standardista.



## Miten luon Matrix-tilin?



Matrix-tilin luominen on yksinkertaista eikä vaadi teknisiä taitoja. Käyttäjät voivat liittyä olemassa olevaan palvelimeen, luoda käyttäjätunnuksen ja aloittaa keskustelun heti. Tässä osiossa kuvataan keskeiset vaiheet.



### Valitse palvelin (julkinen tai yksityinen)



Matrix on federoitu verkko: siinä on lukuisia palvelimia (kotipalvelimia), joita hallinnoivat eri organisaatiot, yhteisöt tai yksityishenkilöt. Palvelimen valinta määrää vain sen, _missä_ tili sijaitsee, mutta ei estä yhteydenpitoa koko verkon kanssa.


**Vaihtoehtoja on kaksi:**



### - Käytä julkista palvelinta



Tämä on yksinkertaisin ratkaisu.


Esimerkkejä suosituista palvelimista:





- _matrix.org_ (tunnetuin)
- _envs.net_
- temaattiset yhteisöpalvelimet (tekniikka, yksityisyys, avoin lähdekoodi...)



Nämä palvelimet sopivat aloitteleville käyttäjille, jotka haluavat rekisteröityä nopeasti.



### - Käytä yksityistä palvelinta



Ihanteellinen :





- organisaatio,
- perhe,
- avoimen lähdekoodin hanke,
- työryhmä,
- tai suvereeniin, itse isännöityyn käyttöön.



Tässä tapauksessa jonkun on hallinnoitava palvelinta (Synapse, Dendrite, Conduit...).


Valitsitpa minkä tahansa palvelimen, käyttäjät voivat keskustella keskenään federaation ansiosta.



### Luo tili askel askeleelta



Koska Matrix on avoin protokolla, useat sovellukset voivat käyttää sitä.


Kuten edellä on kuvattu, ne tarjoavat erilaisia käyttöliittymiä ja toimintoja vaatimusten mukaan:





- Element**: täydellisin asiakasohjelma, saatavilla kaikilla alustoilla.
- FluffyChat**: yksinkertainen, moderni ja ihanteellinen kännyköille.
- Nheko**: kevyt, ergonominen asiakasohjelma tietokoneille.
- SchildiChat**: Element-muunnos ergonomisilla parannuksilla.
- NeoChat**: integroitu KDE-ekosysteemiin.



Asiakkaan valinta ei vaikuta tiliin: kaikki toimivat millä tahansa Matrix-palvelimella.



### Klassiset vaiheet :





- Avaa valittu sovellus. Meidän tapauksessamme teemme sen [Element](app.element.io) -ohjelmalla.
- Valitse "Luo tili".



![cover-kali](assets/fr/10.webp)



Yksinkertaisuuden vuoksi voit luoda Matrix-tilin käyttämällä **Google, Facebook, Apple, GitHub tai GitLab**. Nämä palvelut tietävät vain, että heidän tilinsä on käytetty Matrixin käyttämiseen: tätä kutsutaan **sosiaaliseksi yhteydeksi**.



Voit rekisteröityä myös manuaalisesti valitsemalla **käyttäjätunnuksen**, **salasanan** ja **sähköpostiosoitteen**.



Valitusta palvelimesta riippuen saatetaan vaatia **captcha** sekä **käyttöehtojen** hyväksyminen.



Kun rekisteröinti on vahvistettu, lähetetään vahvistussähköposti.


Aktivoi tilisi klikkaamalla linkkiä ja avaa verkkosovellus (Element) liittyäksesi ensimmäisiin Matrix-keskusteluihisi.



![cover-kali](assets/fr/11.webp)



Sinulla on nyt tili ja käytät Elementin verkkoversiota.



## Lisää ensimmäinen yhteystietosi



Voidaksesi kommunikoida jonkun henkilön kanssa Matrixissa sinun tarvitsee vain tietää hänen täydellinen tunnuksensa, jota kutsutaan **Matrix ID**:ksi.



Esimerkki:



`@alice:matrix.org @bened:monserveur.bj`



### Lisää yhteyshenkilö



Voit kutsua ystäviä ryhmäkeskusteluun napsauttamalla oikeassa yläkulmassa olevaa i-kehää. Tämä avaa oikeanpuoleisen paneelin. Napsauta "Ihmiset"-painiketta näyttääksesi luettelon tämän huoneen jäsenistä: sinun pitäisi olla tällä hetkellä ainoa läsnäolija.



![cover-kali](assets/fr/12.webp)



Napsauta "Kutsu tähän huoneeseen" ihmisluettelon yläosassa, jolloin avautuu kehote, jonka avulla voit kutsua ystäväsi mukaan Matrixiin. Jos he ovat jo kirjautuneet sisään Matrixiin, syötä heidän Matrix-tunnuksensa. Jos he eivät ole, syötä heidän sähköpostiosoitteensa, niin heidät kutsutaan mukaan.



Ystäväjärjestelmää ei ole: yhteyshenkilö on yksinkertaisesti henkilö, jonka kanssa on avattu keskustelu.



![cover-kali](assets/fr/13.webp)



Kutsuttu henkilö voi joko hyväksyä tai hylätä kutsun. Jos hän hyväksyy kutsun, hänen pitäisi liittyä huoneeseen. Mitä enemmän, sitä parempi!



![cover-kali](assets/fr/14.webp)



### Oman palvelimen perustaminen



Matrix pääsee oikeuksiinsa, kun sitä käytetään yhdessä henkilökohtaisen palvelimen kanssa.


Oman kotipalvelimen käyttöönoton ansiosta voit :





- säilyttää tietojen täydellinen hallinta,
- määritellä omat käyttösääntönsä,
- isännöi useita tilejä (ystävät, tiimi, yhteisö),
- ja varmistaa maksimaalinen joustavuus rajoitusten tai sensuurin tapauksessa.



**Valittavat ratkaisut:**





- Synapse**: historiallinen ja täydellisin toteutus.
- Dendrite**: kevyempi, tehokkaampi ja suunniteltu protokollan tulevaisuutta varten.
- Conduit**: minimalistinen versio, joka on helppo ottaa käyttöön.



**Vedellytykset:**





- verkkotunnus,
- kone tai VPS,
- vähintään järjestelmänhallintataitoja.



Vaikka se vaatii hieman konfigurointia, oman palvelimen hallinta tekee Matrixista suvereenin ja kestävän työkalun.



### Liittyminen ensimmäisiin messuihin



Matrix luottaa vahvasti _huoneisiin_ (olohuoneisiin).


On julkisia, yksityisiä, yhteisöllisiä, teknisiä, paikallisia ja kansainvälisiä messuja.



**Kolme tapaa liittyä salonkiin:**



1. **Kutsulinkin** kautta (usein "matrix.to"-URL-osoitteen muodossa).


2. **Haetaan salongin nimeä** sovelluksessa.


3. **Syöttämällä koko ohjelman ID**, esim. :


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Kun chat-huoneeseen on liitytty, se käyttäytyy kuin klassinen uutisryhmä, ja siinä on historiatiedot, salaus, tiedostot, reaktiot ja audio-/videopuhelut käytetystä ohjelmasta riippuen.



![capture](assets/fr/09.webp)



## Jatketaan matkaa



Kun hallitset perusasiat, Matrix tarjoaa monia kehittyneitä mahdollisuuksia. Halusitpa sitten liittää muita viestijärjestelmiä, isännöidä omaa palvelinta tai organisoida yhteisön, ekosysteemi on erittäin rikas.



### Sillat (WhatsApp, Telegram, Signal jne.)



Silta yhdistää Matrixin muihin sanomanvälitysjärjestelmiin.


Sen avulla voit lähettää ja vastaanottaa viestejä :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Keskustelu
- Slack**
- IRC** (IRC)
- ja monet muut



### Mitä sillat voivat tehdä





- Keskitä kaikki keskustelut Matrixiin
- Avoimen käyttöliittymän tarjoaminen vuorovaikutusta varten omien palvelujen kanssa
- Hallitse monialustaista yhteisöä yhdestä paikasta käsin



Jotkut sillat ovat virallisia, toiset yhteisöllisiä.


Osastosta riippuen ne voivat vaatia :





- henkilökohtainen palvelin,
- lisäkonfiguraatio,
- tai olemassa olevan julkisen sillan käyttö.



### Matrixin käyttäminen Bitcoin-organisaatiossa, yhteisössä tai projektissa



Matrix ei ole vain henkilökohtainen työkalu.


Sitä voidaan käyttää työryhmien jäsentämiseen, paikallisyhteisöjen organisointiin tai projektiviestinnän hallintaan.



**Käyttöesimerkkejä:**





- Avoimen lähdekoodin yhteisöt
- Bitcoin- ja Lightning-ekosysteemihankkeet
- Opiskelija- tai kehittäjäryhmät
- Kansalaisjärjestöt
- Riippumattomat tiedotusvälineet
- Paikalliset ryhmät ja yhdistykset



**Miksi tämä on kiinnostavaa?





- 100 % avoimen lähdekoodin** työkalu
- Suvereeni ja hajautettu** viestintä
- Tilat on järjestetty **loungeihin**, **alaryhmiin**, **yksityisiin loungeihin** jne.
- Integroi Nextcloudin, GitLabin, Mattermostin tai mukautettujen bottien kanssa
- Oikeuksien ja moderoinnin hienosäädetty hallinta



Matrixista tulee tällöin viestinnän tukipilari kaikille rakenteille, jotka haluavat pysyä riippumattomina suurista keskitetyistä alustoista.



## Päätelmä



Matrix edustaa nykyaikaista, avointa ja turvallista ratkaisua reaaliaikaiseen viestintään ja tarjoaa hajautetun vaihtoehdon perinteisille alustoille. Sen federoidun arkkitehtuurin ja kehittyneiden salausprotokollien ansiosta käyttäjät voivat säilyttää tietojensa hallinnan ja nauttia samalla sujuvasta, yhteentoimivasta kokemuksesta. Matrix tarjoaa vankan ja skaalautuvan kehyksen nykypäivän tarpeisiin mukautettujen viestintäympäristöjen rakentamiseen, olipa kyse sitten henkilökohtaisesta, ammatillisesta tai yhteisöllisestä käytöstä.



Jos haluat lisätietoja ja tutustua kaikkiin Matrixin tarjoamiin ominaisuuksiin, voit tutustua viralliseen dokumentaatioon, joka on saatavilla täällä :


[https://matrix.org/docs/](https://matrix.org/docs/)