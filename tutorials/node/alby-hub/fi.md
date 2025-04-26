---
name: Alby Hub
description: Miten käynnistät helposti oman Lightning-solmun?
---
![cover](assets/cover.webp)

Alby Hub on Alby-yhtiön uusin avoimen lähdekoodin ohjelmisto, joka tunnetaan suositusta Lightning-verkkolaajennuksesta. Alby Hub on itsehallinnollinen lompakko, jossa on helpoin käyttää Lightning-solmua, joka on käytettävissä mistä tahansa integroitumaan kymmenien sovellusten kanssa. Alby Hub on helppokäyttöinen käyttöliittymä Lightning-solmujen hallintaan.

Tässä opetusohjelmassa tarkastelemme eri tapoja käyttää Alby Hubia ja kuinka yhdistää se Alby Go -sovellukseen, Albyn mobiilisovellukseen tai Alby-selainlaajennukseen. Tämä mahdollistaa satoshiesi käyttämisen liikkeellä ollessasi, samalla kun hallitset solmuasi itsenäisesti.

![ALBY HUB](assets/fr/01.webp)

## Mikä on Alby Hub?

Alby Hubista on tulossa Alby-ekosysteemin uusi lippulaivatyökalu. Tämä ohjelmisto mahdollistaa käyttäjille oman itsehallittavan lompakon helpon hallinnan integroidulla Lightning-solmulla samalla säilyttäen avaintensa omistuksen (itsehallinta).

Alby Hub on erittäin mukautuva työkalu. Se pystyy vastaamaan sekä aloittelijoiden että edistyneiden käyttäjien tarpeisiin. Aloittelijat voivat käyttää sitä helposti oikean Lightning-solmun omatoimiseen käyttöön ilman, että heidän tarvitsee perehtyä taustalla olevaan monimutkaisuuteen. Kokeneemmille käyttäjille Alby Hubia voidaan käyttää täydellisenä käyttöliittymänä olemassa olevan Lightning-solmun edistyneeseen hallintaan.

Alby Hub on saatavana neljässä eri kokoonpanossa tarpeidesi mukaan:


- Alby Hub Cloud :**

Ihanteellinen aloittelijoille, tämä ensimmäinen vaihtoehto on Albyn pilvivaihtoehto. Se mahdollistaa Hubin käyttöönoton suoraan Albyn hallinnoimalla palvelimella, johon pääsee Alby Hub -käyttöliittymän kautta. Vaikka Alby hallinnoi palvelinta, säilytät suvereniteetin varoihisi, koska avaimesi on salattu salasanalla, jonka vain sinä tiedät. Avaimet on kuitenkin pidettävä salauksenpurkamattomina RAM-muistissa, jotta solmu voi toimia, mikä teoreettisesti altistaa ne riskille, jos joku pääsee fyysisesti palvelimelle. Tämä on mielenkiintoinen kompromissi aloittelijoille, mutta on tärkeää olla tietoinen riskeistä.

Tämän vaihtoehdon suurimpana etuna on, että saat Lightning-solmun toimimaan 24/7 ilman, että sinun tarvitsee itse hallinnoida isännöintiä. Lisäksi Lightning-solmusi varmuuskopiot ovat yksinkertaisempia ja automatisoituja verrattuna itse isännöityihin vaihtoehtoihin, joissa sinun on itse hallinnoitava kanavien varmuuskopioita.

Alby Cloud on maksullinen palvelu [Tarkista heidän hinnoittelunsa](https://albyhub.com/#pricing) saadaksesi lisätietoja. Maksu vähennetään automaattisesti lompakostasi Albyn antaman Lightning-laskun kautta. Tämä tapahtuu NWC-yhteyden kautta, joka konfiguroi solmusi maksamaan automaattisesti Albyn tilaukseesi liittyvät laskut.

- Alby Hub olemassa olevalla solmulla :**

Jos sinulla on jo solmu isännöitynä esimerkiksi Umbrelissa tai Start9:ssä, Alby Hubia voidaan käyttää kehittyneenä hallintakäyttöliittymänä samaan tapaan kuin ThunderHubia tai RTL:ää.


- Alby Hub paikallinen :**

On myös mahdollista asentaa Alby Hub suoraan tietokoneellesi, vaikka tämä vaihtoehto on vähemmän käytännöllinen, koska tietokoneesi on oltava jatkuvasti aktiivinen, jotta Lightning-solmuun voidaan etäyhteydellä päästä. Tämä vaihtoehto voi kuitenkin sopia erityistarpeisiisi.


- Alby Hub henkilökohtaisella palvelimella :**

Edistyneille käyttäjille Alby Hub voidaan ottaa käyttöön henkilökohtaisella palvelimella yksinkertaisella komennolla. Tätä vaihtoehtoa ei käsitellä tässä oppaassa, mutta löydät omat ohjeet [Albyn GitHubista](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Tämä opetusohjelma keskittyy pääasiassa käyttöliittymään, joka on sama valitusta vaihtoehdosta riippumatta. Katsomme myös, miten Alby Hub otetaan käyttöön maksullisella pilvipalveluvaihtoehdolla ja sitten node-in-box-vaihtoehdolla (Umbrel tai Start9).

![ALBY HUB](assets/fr/02.webp)

Jos haluat asentaa paikallisesti tietokoneeseen, [lataa ja asenna ohjelmisto käyttöjärjestelmäsi mukaisesti](https://github.com/getAlby/hub/releases) ja noudata sitten käyttöliittymän ohjeita.

![ALBY HUB](assets/fr/03.webp)

## Luo Alby-tili

Ensimmäinen vaihe on luoda Alby-tili. Vaikka tämä ei ole välttämätöntä Alby Hubin käyttämiseksi, sen avulla voit hyödyntää kaikkia käytettävissä olevia vaihtoehtoja, kuten mahdollisuutta saada Lightning-osoite.

Mene [Albyn viralliselle verkkosivustolle] (https://getalby.com/) ja napsauta "*Luo tili*" -painiketta.

![ALBY HUB](assets/fr/04.webp)

Anna lempinimi ja sähköpostiosoite ja napsauta sitten "*Tilaa*". Tätä sähköpostiosoitetta käytetään kirjautumiseen tilillesi myöhemmin.

![ALBY HUB](assets/fr/05.webp)

Syötä sähköpostitse saamasi vahvistuskoodi.

![ALBY HUB](assets/fr/06.webp)

Kun olet kirjautunut verkkotilillesi, napsauta "*Jatka*"-painiketta.

![ALBY HUB](assets/fr/07.webp)

Napsauta uudelleen "*Jatka*".

![ALBY HUB](assets/fr/08.webp)

## Pilvi hosting vaihtoehto

Sinun täytyy sitten valita itse isännöidyn vaihtoehdon, jossa asennat Alby Hubin omaan laitteeseesi, tai premium-vaihtoehtojen välillä. Aloitan selittämällä, kuinka edetä Pro Cloud -vaihtoehdolla (huomaa, että tämä on maksullinen vaihtoehto, katso yksityiskohdat edellisestä osasta).

Napsauta "*Upgrade*".

![ALBY HUB](assets/fr/09.webp)

Vahvista klikkaamalla "*Tilaa nyt*".

![ALBY HUB](assets/fr/10.webp)

Napsauta "*Launch Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Odota hetki, kun solmusi luodaan.

![ALBY HUB](assets/fr/12.webp)

Ja siinä kaikki, Alby Hub on nyt määritetty. Seuraavassa osiossa näytän, kuinka asennat Alby Hubin olemassa olevaan solmuun. Jos sinulla ei ole vielä Lightning-solmua, voit siirtyä suoraan seuraavaan osioon konfiguroidaksesi Alby Hubin Alby Cloudissa.


![ALBY HUB](assets/fr/13.webp)

## Itsehosting-vaihtoehto

Jos haluat käyttää Alby Hubia olemassa olevan Lightning-solmusi käyttöliittymänä, sinulla on useita vaihtoehtoja: voit asentaa sen palvelimelle, paikallisesti tietokoneellesi tai node-in-boxin (Umbrel tai Start9) kautta. Alby Hubin käyttö näissä kokoonpanoissa on maksutonta. Keskitymme node-in-box -vaihtoehtoon, sillä mielestäni palvelinvaihtoehto ilman fyysistä pääsyä sisältää samanlaisia riskejä kuin pilviversio, ja paikallinen asennus tietokoneelle on usein sopimatonta.

Jotta tämä voidaan ottaa käyttöön Umbrelissa (Start9:ssä vaiheet ovat samat), sinun on ensin määritettävä LND-solmu.

Kirjaudu sisään Umbrel-käyttöliittymään ja siirry sovelluskauppaan.

![ALBY HUB](assets/fr/14.webp)

Etsi "*Alby Hub*" -sovellus.

![ALBY HUB](assets/fr/15.webp)

Asenna se solmuun.

![ALBY HUB](assets/fr/16.webp)

Alby Hub -käyttöliittymäsi on nyt valmis. Voit seurata loput ohjeesta aivan kuin käyttäisit pilvikäyttöliittymää, mutta ilman maksullisen version vaihtoehtoja. Lisäksi toisin kuin pilviversiossa, avaimesi tallennetaan paikallisesti solmullesi, ei Albyn palvelimille.

![ALBY HUB](assets/fr/17.webp)

## Alby Hubin käynnistäminen

Napsauta "*Aloita*"-painiketta.

![ALBY HUB](assets/fr/18.webp)

Alby Hub pyytää sinua valitsemaan salasanan. Tämä salasana on erittäin tärkeä, sillä sitä käytetään lompakkosi salaamiseen. Maksullisessa pilviversiossa avaimesi tallennetaan Alby-palvelimelle, salataan tällä salasanalla, jonka vain sinä tiedät, ja puretaan sitten ja tallennetaan vain RAM-muistiin, jotta transaktiot voidaan tarvittaessa allekirjoittaa.

On siis olennaista valita vahva salasana. Jokainen, jolla on tämä salasana, voi mahdollisesti saada pääsyn solmuusi. Varmista myös, että teet yhden tai useamman fyysisen varmuuskopion tästä salasanasta paperille tai vielä parempi, metallilevyyn lisäturvallisuuden takaamiseksi.

Kun olet valinnut ja tallentanut salasanasi huolellisesti, klikkaa "*Luo salasana*".

![ALBY HUB](assets/fr/19.webp)

Sinulla on nyt pääsy Lightning-solmuun.

![ALBY HUB](assets/fr/20.webp)

Ensimmäinen toimenpide on tallentaa palautuslauseesi, josta avaimesi johdetaan. Voit tehdä tämän napsauttamalla "Asetukset". Tämä lause mahdollistaa lompakon palauttamisen, jos olet ottanut käyttöön automaattiset varmuuskopiot.

![ALBY HUB](assets/fr/21.webp)

Siirry sitten "*Backup*"-välilehdelle. Syötä salasanasi päästäksesi siihen käsiksi.

![ALBY HUB](assets/fr/22.webp)

Sen jälkeen saat käyttöösi 12 sanan palautuslauseen. Tee tästä lauseesta yksi tai useampi fyysinen varmuuskopio paperille tai metallille ja säilytä se turvallisessa paikassa.

![ALBY HUB](assets/fr/23.webp)

Kun olet tallentanut lauseen, vahvista tallennus ruudulla ja napsauta "*Jatka*".

![ALBY HUB](assets/fr/24.webp)

## Miten voin palauttaa pääsyn bitcoineihini?

Ennen kuin lähetät varoja Alby Hubiisi, on tärkeää ymmärtää, kuinka ne voidaan palauttaa ongelmatilanteessa, sekä mitä tietoja tätä palautusta varten tarvitaan. Prosessi vaihtelee palautettavien varojen luonteen ja solmun isännöintitavan mukaan.

Maksullisten pilvipalvelun käyttäjille täydellinen bitcoinien palautus vaatii kolme olennaista elementtiä:

- Palautuslauseesi;
- Pääsy Alby-tilillesi automatisoitujen varmuuskopioiden noutamiseksi.

Jos jompikumpi näistä kahdesta tiedosta puuttuu, bitcoiniesi täydellinen palautus on mahdotonta.

Niille, jotka käyttävät Alby Hubia omalla laitteellaan, palautusprosessi on dokumentoitu [täällä](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).

Jos olet asentanut Alby Hubin olemassa olevaan solmuun, sinun tulee noudattaa kyseisen solmun käyttöjärjestelmän palautusprosessia. Esimerkiksi: Umbrel tarjoaa [vaihtoehdon](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) salata Lightning-kanaviesi viimeisimmän tilan ja tallentaa sen dynaamisesti ja anonyymisti Torin kautta. Huomaa, että vain Alby:n automaattiset varmuuskopiot mahdollistavat Hubisi täydellisen palauttamisen ilman, että kanavia tarvitsee sulkea.


## Osta ensimmäinen Lightning-kanava

Voit nyt seurata Alby Hubin antamia ohjeita. Klikkaa painiketta avataksesi ensimmäisen kanavasi saapuvalle käteiselle.

![ALBY HUB](assets/fr/25.webp)

Valitse "*Avaa kanava*". Jos et aio ryhtyä reitityssolmuksi etkä erityisesti tarvitse sellaista, suosittelen valitsemaan yksityiset kanavat.

![ALBY HUB](assets/fr/26.webp)

Alby Hub luo laskun, jonka voit maksaa. Tämä maksu kattaa kanavasi avaamiseen tarvittavat transaktiomaksut sekä LSP:n (*Lightning Service Provider*) palvelumaksut, joka avaa kanavan solmuun, jolloin voit vastaanottaa maksut välittömästi.

![ALBY HUB](assets/fr/27.webp)

Kun lasku on maksettu ja maksutapahtuma vahvistettu, ensimmäinen Lightning-kanava on perustettu.

![ALBY HUB](assets/fr/28.webp)

"*Solmu*"-välilehdellä näet, että sinulla on nyt saapuvaa käteistä, joten voit vastaanottaa maksuja Lightningin kautta.

![ALBY HUB](assets/fr/29.webp)

Jos haluat vastaanottaa maksun, napsauta "*Lompakko*"-välilehteä ja sitten "*Vastaanota*".

![ALBY HUB](assets/fr/30.webp)

Kirjoita summa ja lisää tarvittaessa kuvaus ja napsauta sitten "*Luo lasku*".

![ALBY HUB](assets/fr/31.webp)

Sain ensimmäisen 120 000 satsin maksun.

![ALBY HUB](assets/fr/32.webp)

Voit tarkistaa lompakkosi saldon palaamalla "*Lompakko*"-välilehdelle. Huomaa, että Alby Hub varaa automaattisesti 354 satsia, kun teet ensimmäisen maksun. Jokaista sen jälkeen avaamaasi Lightning-kanavaa varten Alby Hub varaa automaattisesti varauksen, joka vastaa 1 % kanavan kapasiteetista. Tämä varaus on turvatoimenpide, jonka avulla solmusi voi periä kanavan varat takaisin, jos vertaisesi yrittää petosta. Tästä syystä saldossani näkyy vain 119 646 satelliittia, vaikka olen lähettänyt 120 000 satelliittia.

![ALBY HUB](assets/fr/33.webp)

## Tallettaminen bitcoins onchain

Jos haluat lähtevää käteistä rahaa maksujen suorittamiseen, voit myös avata kanavan itse. Tätä varten tarvitset lompakossasi onchain-bittikolikoita.

Napsauta "*Solmu*"-välilehdeltä "*Talletus*".

![ALBY HUB](assets/fr/34.webp)

Lähetä bitcoineja näytettyyn osoitteeseen. Tämä osoite saadaan aiemmin tallentamastasi palautuslausekkeesta.

![ALBY HUB](assets/fr/35.webp)

Lähetin 72 000 satelliittia. Ne näkyvät nyt kohdassa "*Säästösaldo*", joka sisältää kaikki omistamani varat ketjussa, ei Lightningissa.

![ALBY HUB](assets/fr/36.webp)

## Avaa Lightning-kanava

Nyt kun sinulla on onchain-varoja, voit avata uuden Lightning-kanavan. Kannattaa avata useita kanavia, joissa on riittävästi varoja, jotta voit aina suorittaa maksuja ilman rajoituksia. Useimmat LSP:t (*Lightning-palveluntarjoajat*) vaativat vähintään 150 000 satsia avatakseen kanavan kanssasi.

Napsauta "*Solmu*"-välilehdellä "*Avaa kanava*".

![ALBY HUB](assets/fr/37.webp)

Valitse kanavasi koko. Suosittelen, ettet avaa liian pieniä kanavia, koska kyseessä on Lightning-solmu, eikä kone, jossa avaimesi sijaitsevat, tarjoa samaa turvallisuustasoa kuin laitteistolompakko. Ole siis varovainen niiden määrien kanssa, jotka valitset estettäväksi.

![ALBY HUB](assets/fr/38.webp)

"*Advanced Options*"-valikossa voit valita, millä LSP:llä kanava avataan, tai syöttää manuaalisesti toisen Lightning-solmun.

![ALBY HUB](assets/fr/39.webp)

Napsauta sitten "*Avaa kanava*".

![ALBY HUB](assets/fr/40.webp)

Odota, että kanavasi vahvistetaan onchainissa.

![ALBY HUB](assets/fr/41.webp)

Uusi kanavasi näkyy nyt "*Solmu*"-välilehdellä.

![ALBY HUB](assets/fr/42.webp)

## Solmun hallinta

Lightning-kanavien hallinta on helpompaa kuin luulet. Alby Hubin avulla voit siirtää satseja kulutussaldosi ja on-chain saldosi välillä. Näin voit lisätä käyttö- tai vastaanottokapasiteettia.

![ALBY HUB](assets/fr/66.webp)


## Yhdistä kulusovellus

Nyt kun sinulla on toimiva Lightning-solmu, voit käyttää sitä vastaanottamaan ja käyttämään satelliitteja päivittäin. Vaikka Alby Hubin verkkokäyttöliittymä on kätevä solmun hallinnointiin, se ei ole ihanteellinen nopeiden transaktioiden tekemiseen liikkeellä ollessa. Tätä varten käytämme älypuhelimeemme asennettua Lightning-lompakkosovellusta.

Tässä ohjeessa suosittelen Alby Go -ohjelmaa, joka on erittäin helppokäyttöinen, mutta voit käyttää myös muita yhteensopivia sovelluksia, kuten Zeusta.

![ALBY HUB](assets/fr/43.webp)

Asenna Alby Go siirtymällä laitteesi sovelluskauppaan:


- [Androidille](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Applen puolesta](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Android-käyttäjät voivat asentaa sovelluksen myös `.apk`-tiedoston kautta [saatavilla Albyn GitHubissa](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Kun sovellus on käynnistetty, napsauta "*Connect Wallet*".

![ALBY HUB](assets/fr/46.webp)

Alby Hubissasi, App Store -osiossa, löydä “Alby Go” ja klikkaa “Connect”  
![ALBY HUB](assets/fr/47.webp)  
Klikkaa “Connect with One-Tab Connections”. Tämä mahdollistaa Alby Hubin yhdistämisen muihin sovelluksiin yhdellä napsautuksella Alby Go:n avulla.  

![ALBY HUB](assets/fr/48.webp)  

Alby Hub luo sitten salaisen avaimen yhteyden muodostamiseksi Alby Go hon.


![ALBY HUB](assets/fr/49.webp)

Palaa takaisin Alby Go -sovellukseen, skannaa QR-koodi tai liitä salaisuus.

![ALBY HUB](assets/fr/50.webp)

Napsauta "Valmis*".

![ALBY HUB](assets/fr/51.webp)

Sinulla on nyt etäyhteys Alby Hubin ylläpitämään Lightning-solmuusi älypuhelimestasi, mikä tekee satoshien lähettämisestä ja vastaanottamisesta liikkeellä ollessa helppoa joka päivä.


![ALBY HUB](assets/fr/52.webp)

Tarvittaessa voit hallita tämän yhteyden käyttöoikeuksia suoraan Alby Hubissa napsauttamalla sitä.

![ALBY HUB](assets/fr/53.webp)

Jos haluat vastaanottaa satelliitteja, klikkaa "*Vastaanottaa*".

![ALBY HUB](assets/fr/54.webp)

Muokkaa laskun määrää ja kuvausta napsauttamalla "*Lasku*".

![ALBY HUB](assets/fr/55.webp)

Lataa lasku vastaanottaa satsit.

![ALBY HUB](assets/fr/56.webp)

Voit lähettää satsit napsauttamalla "*lähettää*".

![ALBY HUB](assets/fr/57.webp)

Skannaa lasku, jonka haluat maksaa.

![ALBY HUB](assets/fr/58.webp)

Napsauta sitten "*Maksa*".

![ALBY HUB](assets/fr/59.webp)

Tapahtumasi on vahvistettu.

![ALBY HUB](assets/fr/60.webp)

Klikkaamalla pientä nuolta pääset tapahtumahistoriaan.

![ALBY HUB](assets/fr/61.webp)

Nämä tapahtumat näkyvät myös Alby Hubissa.

![ALBY HUB](assets/fr/62.webp)

## Mukauta Lightning-osoitteesi

Alby tarjoaa sinulle mahdollisuuden käyttää salamaosoitetta. Näin voit vastaanottaa maksuja solmupisteeseesi ilman, että sinun tarvitsee joka kerta luoda laskua manuaalisesti. Alby määrittää sinulle oletusarvoisesti Lightning-osoitteen, mutta voit muokata sitä. Kirjaudu sisään Alby-verkkotilillesi, napsauta nimeäsi oikeassa yläkulmassa ja valitse sitten "*Asetukset*".

![ALBY HUB](assets/fr/63.webp)

Siirry valikkoon "*Lightning Address*".

![ALBY HUB](assets/fr/64.webp)

Muokkaa osoitetta ja vahvista sitten klikkaamalla "*Päivitä salamaosoitteesi*".

![ALBY HUB](assets/fr/65.webp)

Huomaa, että kun osoitteesi on muutettu, se ei enää kuulu sinulle. Varmista siis, ettet enää koskaan lähetä sinne satsia.

Nyt tiedät, miten Lightningia käytetään omassa solmussa Alby Hub -työkalun avulla. Jos löysit tämän opetusohjelman hyödylliseksi, olisin hyvin kiitollinen, jos laittaisit vihreän peukalon alle. Voit myös vapaasti jakaa tätä artikkelia sosiaalisissa verkostoissa. Kiitos paljon!

Jotta ymmärtäisit yksityiskohtaisesti kaikki Salama-mekanismit, joita olemme käsitelleet tässä opetusohjelmassa, suosittelen sinua tutustumaan ilmaiseen koulutukseemme aiheesta :

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
