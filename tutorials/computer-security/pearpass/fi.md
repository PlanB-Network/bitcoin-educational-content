---
name: PearPass
description: Ota salasanasi takaisin hallintaasi paikallisella, vertaisverkkopohjaisella ja pilvipohjaisella salasanahallintaohjelmalla
---

![cover](assets/cover.webp)



Nykyään, kun jokainen henkilö hallinnoi kymmeniä, jopa satoja verkkotilejä, kirjautumistietojen turvallisuudesta on tullut tietoturvan kannalta keskeinen kysymys. Sosiaaliset verkostot, viestijärjestelmät, ammatilliset palvelut, rahoitusalustat: jokainen näistä käyttöoikeuksista perustuu salaisuuteen, jonka vaarantumisella voi olla vakavia seurauksia elämääsi.



Hyökkäysten kasvavasta määrästä huolimatta huonot käytännöt ovat edelleen laajalle levinneet väestön keskuudessa: heikot salasanat, uudelleen käytetyt salasanat, selkeänä tekstinä tallennetut salasanat tai suunnilleen ulkoa opitut salasanat. Näiden ongelmien ratkaisemiseksi ilman, että elämästä tulee päivittäin monimutkaisempaa, ratkaisu on käyttää salasanahallintaohjelmaa.



Salasanahallintaohjelmia on jo olemassa kymmeniä, ja Plan ₿ Academy tarjoaa opetusohjelman useimpiin niistä. Tässä oppaassa haluan kuitenkin esitellä sinulle yhden, joka erottuu selvästi muista sen toimintatavan suhteen: **PearPass**.



**PearPass on avoimen lähdekoodin, local-first, peer-to-peer-salasanahallintaohjelma, joka on suunniteltu antamaan käyttäjille täydellisen hallinnan tietoihinsa



![Image](assets/fr/01.webp)



## Miksi valita PearPass?



Salasanahallintaohjelma on ohjelmisto, joka luo, tallentaa ja järjestää kaikki salasanasi turvallisesti. Sen sijaan, että muistaisit tai käyttäisit salasanoja uudelleen, sinulla on vain yksi salaisuus, jota voit suojata: pääsalasana, joka salaa koko kassakaappisi. Tämä lähestymistapa mahdollistaa ainutlaatuisten, pitkien ja satunnaisten salasanojen käytön jokaisessa palvelussa, mikä vähentää sekä unohtamisen että vaarantamisen riskiä ja rajoittaa samalla mahdollisen vuodon vaikutuksia. Nykyään se on perustietotekniikkatyökalu, jota kaikkien pitäisi käyttää.



Salasanahallinnassa on kaksi pääluokkaa. Toisaalta on vain paikallisia ohjelmistoja, jotka ovat erittäin turvallisia, koska tietoja ei koskaan tallenneta keskitetylle palvelimelle, mutta eivät ole kovin käytännöllisiä, koska niiden avulla et voi helposti synkronoida tunnistetietojasi useiden laitteiden välillä (tietokone, älypuhelin, tabletti...). Toisaalta pilvipohjaiset salasanahallintaohjelmat tallentavat tunnistetietosi palvelimilleen ja synkronoivat ne kaikkiin laitteisiisi. Niiden tärkein etu on helppokäyttöisyys, mutta ne aiheuttavat kompromisseja turvallisuuden suhteen, koska salasanasi tallennetaan infrastruktuuriin, jota et voi hallita.



PearPass rikkoo tarkoituksella molempia malleja. Se sijoittuu paikallisten hallintajärjestelmien ja pilviratkaisujen väliin: se mahdollistaa salasanojesi synkronoinnin ja takaa, että niitä ei koskaan tallenneta etäpalvelimille. Tämän seurauksena kaikki tunnistetietosi tallennetaan paikallisesti laitteillesi, ja synkronointi useiden koneiden välillä tapahtuu yksinomaan vertaisverkkona. Tämä arkkitehtuuri eliminoi keskitettyihin tietokantoihin liittyvät yksittäiset vikapisteet: ei ole palvelimia, jotka voisivat vaarantaa, eikä kolmannen osapuolen infrastruktuuria, joka pääsisi käsiksi tunnuksiisi. Laitteidesi välinen viestintä on päästä päähän salattua, mikä varmistaa, että vain sinun hallussasi olevat avaimet mahdollistavat pääsyn tietoihin.



![Image](assets/fr/02.webp)



PearPass perustuu nimensä mukaisesti **Pears**:ään, joka on palvelimettomien sovellusten luomiseen ja toteuttamiseen tarkoitettu vertaisteknologiaekosysteemi. Pears tarjoaa suoritusympäristön, jakelumekanismit ja verkkokerrokset, joita tarvitaan täysin hajautettujen sovellusten suorittamiseen ja jotka kykenevät synkronoimaan suoraan vertaisten välillä ilman keskitettyä infrastruktuuria. PearPassin tapauksessa Pears tarjoaa laitteiden löytämisen, salatun yhteyden muodostamisen ja salasanaholvin synkronoinnin koneiden välillä. Tämä lähestymistapa varmistaa, että PearPass pysyy toimivana, joustavana ja riippumattomana kaikista ulkoisista viranomaisista.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Innovatiivisen arkkitehtuurin lisäksi PearPass on täysin avoimen lähdekoodin järjestelmä, ja kaikki sen toiminnot ovat maksuttomia. Secfault Security on myös auditoinut ohjelmiston riippumattomasti. Erityisen arkkitehtuurinsa lisäksi PearPass tarjoaa tietysti kaikki klassiset ominaisuudet, joita hyvältä salasanahallinnalta odotetaan, ja niihin tutustumme tämän oppaan aikana.



Lyhyesti sanottuna, siinä missä perinteiset salasanahallintajärjestelmät pyytävät sinua luottamaan yritykseen ja sen palvelimiin, PearPass noudattaa suvereniteetin logiikkaa: ei pilveä, ei keskitettyjä tilejä, ei välikäsiä. Säilytät yksinomaisen määräysvallan tunnuksistasi ja hyödyt samalla laitteiden välisestä synkronoinnista.



## Miten asennan PearPassin?



PearPass on saatavilla kaikilla alustoilla: Windows, Linux, macOS, Android, iOS ja selainlaajennukset. Pears:ta ei tarvitse asentaa koneellesi: PearPass toimii yksinään.



### Asennus Windows-käyttöjärjestelmään



Windowsissa PearPass toimitetaan klassisena asennusohjelmana. Siirry [viralliselle lataussivulle] (https://pass.pears.com/download) ja napsauta sitten `Lataa Windows-asennusohjelma`-painiketta.



Kun tiedosto on ladattu, avaa asennusohjelma ja noudata ohjatun toiminnon ohjeita. Sovellusta voi sitten käyttää Käynnistä-valikosta tai työpöydän pikakuvakkeen kautta.



![Image](assets/fr/03.webp)



### Asennus macOS-käyttöjärjestelmään



MacOS-käyttöjärjestelmässä PearPass jaetaan levykuvana (`.dmg`). Mene [viralliselle lataussivulle](https://pass.pears.com/download) ja valitse Mac-arkkitehtuuria (Intel tai Apple Silicon) vastaava versio. Kun olet ladannut, avaa `.dmg`-tiedosto ja käynnistä sovellus `Applications`-kansiosta.



Ensimmäisellä käynnistyskerralla macOS näyttää turvaviestin, joka osoittaa, että sovellus on tullut Internetistä: vahvista vain jatkaaksesi.



### Asennus Linuxiin



Linuxissa PearPass on saatavilla `.AppImage`-muodossa, joka takaa laajan yhteensopivuuden useimpien jakeluiden kanssa ilman erityisiä riippuvuuksia. Lataa `.AppImage`-tiedosto [viralliselta lataussivulta](https://pass.pears.com/download) ja käynnistä se sitten suoraan kaksoisnapsauttamalla.



Ympäristöstäsi riippuen voit joutua tekemään tiedostosta suoritettavan tiedoston ominaisuuksien avulla (hiiren oikealla napsautuksella) tai komennolla `chmod +x`. Kun PearPass on hyväksytty, se käynnistyy itsenäisenä sovelluksena.



### Selaimen laajennuksen asennus



PearPass tarjoaa selainlaajennuksen automaattista kirjautumista ja nopeaa pääsyä kassakaappiisi selaillessasi verkkoa. Laajennus on tällä hetkellä saatavilla Google Chromelle ja yhteensopiville selaimille. Voit asentaa sen [viralliselle lataussivulle](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Kun olet lisännyt sen, voit kiinnittää sen työkalupalkkiin nopeaa käyttöä varten. Laajennuksen aktivoiminen edellyttää sitten linkkiä PearPass-sovellukseen, joka on asennettu paikallisesti tietokoneellesi (palaamme tähän myöhemmin opetusohjelmassa).



### Asennus iOS- ja Android-käyttöjärjestelmiin



Lataa sovellus iPhoneen ja Androidiin sovelluskaupasta:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Näiden klassisten asennustapojen lisäksi on myös mahdollista ladata ohjelmisto suoraan GitHub-tietovarastoista kunkin :




- [Työpöytä](https://github.com/tetherto/pearpass-app-desktop);
- [Mobile](https://github.com/tetherto/pearpass-app-mobile);
- [Selaimen laajennus](https://github.com/tetherto/pearpass-app-browser-extension).



Kun PearPass on asennettu yhdelle tai useammalle alustalle, voit siirtyä ensimmäiseen konfigurointiin. Tässä ohjeessa aloitamme ohjelmiston määrittämisen työpöydällä ja synkronoimme sen sitten selainlaajennuksen ja mobiilisovelluksen kanssa.



## Miten luon PearPass-turvakaapin?



Kun käynnistät PearPassin ensimmäisen kerran tietokoneellasi, sovellus ohjaa sinut kahden vaiheen läpi: asetat pääsalasanan ja luot ensimmäisen kassakaapin.



### Aseta pääsalasana



Kun sovellus käynnistetään ensimmäisen kerran työpöydällä, napsauta "Siirry" -painiketta ja sitten "Jatka", jotta pääset esittelynäytön läpi ja pääsalasanan määritysvaiheeseen.



![Image](assets/fr/06.webp)



Seuraavaksi on tärkeää valita pääsalasana. Kuten johdannossa todettiin, tämä salasana on erittäin tärkeä, sillä sen avulla pääset käsiksi kaikkiin muihin hallintaan tallennettuihin salasanoihisi. Teknisesti sitä käytetään tietojen salaamiseen käytettävien salausavainten muodostamiseen.



Pääsalasanaan liittyy kaksi pääasiallista riskiä: katoaminen ja vaarantaminen. Jos menetät salasanan, et voi enää käyttää kirjautumistietojasi. PearPass ei koskaan säilytä pääsalasanaasi: **Jos se katoaa, kirjautumistietosi menetetään pysyvästi**. Palautusmekanismia ei ole. Jos taas tämä salasana vaarantuu ja hyökkääjä pääsee käsiksi johonkin laitteeseesi, hän pääsee käsiksi kaikkiin tileihisi.



Voit rajoittaa katoamisriskiä tekemällä fyysisen varmuuskopion pääsalasanastasi, esimerkiksi paperille, ja säilyttämällä sitä turvallisessa paikassa. Ihannetapauksessa sulje varmuuskopio kirjekuoreen, jotta voit säännöllisesti tarkistaa, ettei siihen ole päästy käsiksi. Toisaalta älä koskaan tee salasanasta digitaalista varmuuskopiota.



Pääsalasanan on oltava vahva, jotta se vähentää vaaran vaarantumisen riskiä. Sen tulisi olla mahdollisimman pitkä, sisältää monenlaisia merkkejä ja se tulisi valita todella satunnaisesti. Vuonna 2025 vähimmäissuositusten mukaan salasanassa on oltava vähintään 13 merkkiä, mukaan lukien isoja ja pieniä kirjaimia, numeroita ja symboleja, edellyttäen, että salasana on satunnainen. Suosittelen kuitenkin vähintään 20 merkkiä, ellei enemmänkin, sisältävää salasanaa, jossa on kaikenlaisia merkkejä, jotta varmistetaan kestävämpi turvallisuustaso.



Kirjoita pääsalasanasi sille varattuun kenttään, vahvista se toisen kerran ja napsauta sitten Jatka-painiketta.



![Image](assets/fr/07.webp)



Tämän jälkeen sinut ohjataan sisäänkirjautumisnäyttöön: kirjoita pääsalasanasi ja tarkista, että kaikki toimii oikein.



![Image](assets/fr/08.webp)



### Luo ensimmäinen kassakaappi



Kun olet kirjautunut sisään, PearPass pyytää sinua luomaan ensimmäisen kassakaapin. Kassakaappi on salattu säiliö, johon salasanasi, tunnuksesi, suojatut muistiinpanosi ja muut tietosi tallennetaan. Jokainen tallelokero on eristetty ja voidaan tunnistaa erillisellä nimellä, jolloin voit järjestää tietosi käyttötarkoituksesi mukaan (henkilökohtainen, ammatillinen, tietyt projektit...).



Napsauta `Luo uusi holvi`-painiketta.



![Image](assets/fr/09.webp)



Valitse tälle holville nimi ja viimeistele luominen napsauttamalla uudelleen `Luo uusi holvi`.



![Image](assets/fr/10.webp)



Kassakaappisi on heti käyttövalmis. Voit aloittaa salasanojen, kirjautumistunnusten tai turvallisten muistiinpanojen lisäämisen heti.



![Image](assets/fr/11.webp)



## Miten voin lisätä kirjautumisen PearPassiin?



Kun olet luonut kassakaapin, voit aloittaa tavaroiden tallentamisen siihen. PearPass tukee monenlaisten esineiden rekisteröintiä:




- kirjautuminen sivustolle tai palveluun ;
- henkilöllisyys: henkilötietosi lomakkeiden nopeaan täyttämiseen, mutta myös henkilöllisyysasiakirjojen tallentamiseen suoraan PearPassiin ;
- luottokortti: luottokorttisi numerot nopeuttaaksesi maksamista, kun teet ostoksia verkossa;
- Wi-Fi: Wi-Fi-verkkojen salasanat ;
- PassPhrase: salainen lause, joka koostuu useista sanoista (varoitus: en suosittele käyttämään sitä wallet Bitcoin-muistilauseisiin);
- huomautus: turvallisten muistiinpanojen luominen ;
- custom: tämän ominaisuuden avulla voit luoda mukautetun elementtityypin, joka on mukautettu erityistarpeisiisi.



Aloita avaamalla PearPass ja kirjaudu sisään pääsalasanallasi.



![Image](assets/fr/12.webp)



Valitse tallelokero, johon haluat tallentaa tämän tunnisteen.



![Image](assets/fr/13.webp)



Napsauta etusivulla painiketta uuden kohteen lisäämiseksi sen mukaan, minkä tyyppisiä tietoja haluat tallentaa. Omassa tapauksessani haluan lisätä käyttäjätunnuksen Plan ₿ Academy-sivuston tililleni, joten napsautan "Luo käyttäjätunnus" -painiketta.



![Image](assets/fr/14.webp)



Kun olet valinnut lisättävän kohteen tyypin, näyttöön tulee lomake, johon voit syöttää kyseiseen palveluun liittyvät tiedot. Tarpeidesi mukaan voit syöttää palvelun nimen, kirjautumistunnuksen, salasanan ja tarvittaessa verkkosivuston osoitteen ja lisähuomautuksia.



PearPassissa on myös salasanageneraattori, jonka avulla voit luoda vahvan salasanan suoraan lomakkeelta. Voit käyttää sitä napsauttamalla kolmea pientä pistettä esittävää kuvaketta `Salasana`-kentässä, valitsemalla haluamasi pituuden ja napsauttamalla sitten `Sijoita salasana`.



Kun kaikki kentät on täytetty, napsauta Tallenna-painiketta tallentaaksesi tunnisteen kassakaappiin.



![Image](assets/fr/15.webp)



Tunniste on nyt tallennettu. Se näkyy valitun kassakaapin kohteiden luettelossa, ja sitä voi tarkastella napsauttamalla sitä.



![Image](assets/fr/16.webp)



Voit muokata elementtiä helposti napsauttamalla sitä ja sitten Muokkaa-painiketta. Voit myös poistaa sen napsauttamalla kolmea pientä pistettä käyttöliittymän oikeassa yläkulmassa ja valitsemalla sitten "Poista elementti".



![Image](assets/fr/22.webp)



Mobiililaitteissa logiikka pysyy samana, mutta käyttöliittymää on mukautettu. Kun olet kirjautunut sisään, valitse haluamasi kassakaappi, napauta `+`-painiketta, valitse luotavan kohteen tyyppi ja täytä sitten tarvittavat tiedot.



![Image](assets/fr/17.webp)



## Miten PearPass järjestetään?



Kuten näimme edellisissä osioissa, PearPassilla voit luoda useita eri holveja. Tämä mahdollistaa eri käyttötarkoitusten erottamisen toisistaan ja muodostaa salasanahallintasi ensimmäisen organisointitason. Etusivulta voit helposti siirtyä holvista toiseen napsauttamalla käyttöliittymän vasemmassa yläkulmassa olevaa nuolta.



![Image](assets/fr/18.webp)



Toinen tapa järjestellä salasanoja, jopa holvin sisällä, on luoda kansioita. Napsauta tätä varten käyttöliittymän vasemmassa sarakkeessa "Kaikki kansiot" -kohdan vieressä olevaa "+"-symbolia ja kirjoita sitten haluamasi kansion nimi.



![Image](assets/fr/19.webp)



Voit tallentaa haluamasi tunnisteet joko suoraan kohteen luomisen yhteydessä tai myöhemmin napsauttamalla Muokkaa-painiketta. Sinun tarvitsee vain valita haluamasi kansio lomakkeen vasemmasta yläkulmasta.



![Image](assets/fr/20.webp)



Kun olet avannut kohteen, esimerkiksi kirjautumisen, voit lisätä sen suosikkeihisi napsauttamalla käyttöliittymän oikeassa yläkulmassa olevaa tähti-kuvaketta. Suosikit löytyvät nopeasti omasta kansiostaan peruskansion lisäksi.



![Image](assets/fr/21.webp)



Lopuksi käyttöliittymän yläosassa on hakupalkki, jonka avulla voit löytää etsimäsi kohteen nopeasti, vaikka holvisi sisältäisi useita tunnuksia.



## Miten synkronoin PearPassin matkapuhelimeeni?



Nyt kun sinulla on toimiva holvi, jossa on tietokoneelle tallennettuja kohteita, haluat todennäköisesti käyttää salasanojasi älypuhelimesta tai muusta laitteesta. PearPassin avulla voit synkronoida managerisi useilla koneilla turvallisesti Pears:n avulla. Selvitetään, miten.



Aloita kirjautumalla lähdekoneella (esimerkiksi tietokoneellasi) holviin pääsalasanallasi. Kun olet etusivulla, napsauta käyttöliittymän oikeassa alareunassa olevaa `Add a Device` (Lisää laite) -painiketta.



![Image](assets/fr/23.webp)



PearPass luo sitten kutsulinkin, joka on saatavana myös QR-koodina, valitun holvin synkronoimiseksi valitsemallasi laitteella.



![Image](assets/fr/24.webp)



Jos haluat synkronoida mobiililaitteella, asenna sovellus ensin ja käynnistä se sitten. Sinua pyydetään luomaan pääsalasana mobiilihallintaasi varten. Voit käyttää samaa salasanaa kuin tietokoneella tai eri salasanaa. Noudata kaikissa tapauksissa samoja suosituksia: vahva, satunnainen salasana, joka on tallennettu fyysiselle tietovälineelle.



![Image](assets/fr/25.webp)



Tämän jälkeen voit halutessasi aktivoida biometrisen tunnistautumisen, jotta sinun ei tarvitse syöttää pääsalasanaasi manuaalisesti aina, kun avaat lukituksen.



![Image](assets/fr/26.webp)



Kirjoita pääsalasana uudelleen ja napsauta sitten Jatka-painiketta.



![Image](assets/fr/27.webp)



Valitse `Load a holvi`-vaihtoehto, napsauta sitten `Scan QR Code` ja skannaa kutsun QR-koodi, jonka PearPass näyttää lähdekoneellasi (tietokoneella).



![Image](assets/fr/28.webp)



Tietokoneen ja matkapuhelimen holvit on nyt synkronoitu. Jokainen toisessa laitteessa lisätty tunniste tallennetaan ja kopioidaan turvallisesti toiseen laitteeseen.



![Image](assets/fr/29.webp)



Matkapuhelimissa voit myös aktivoida automaattisen kenttätäytön. Tee tämä valitsemalla `Asetukset > Lisäasetukset` ja napsauttamalla sitten `Automaattitäyttö`-osiossa olevaa `Set as Default`-painiketta.



![Image](assets/fr/30.webp)



## Miten synkronoin PearPassin selainlaajennuksen kanssa?



Tietokoneen ja älypuhelimen välillä synkronoitu salasanahallinta on jo erittäin käytännöllinen, mutta sen integroiminen suoraan selaimeen on vielä käytännöllisempää. Aloita [lisäämällä virallinen PearPass-laajennus selaimeesi](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Mene paikalliseen koneeseesi asennetusta PearPass-ohjelmistosta kohtaan `Asetukset > Lisäasetukset` ja aktivoi sitten `Activate browser extension` -vaihtoehto.



![Image](assets/fr/32.webp)



PearPass luo token-paritiedoston. Kopioi se.



![Image](assets/fr/33.webp)



Avaa sitten PearPass-laajennus selaimessasi, liitä token-pariliitos ja napsauta `Verify`-painiketta ja sen jälkeen `Complete`.



![Image](assets/fr/34.webp)



Salasanahallintasi on nyt synkronoitu selainlaajennuksen kanssa.



![Image](assets/fr/35.webp)



Voit nyt käyttää sitä helposti yhteyden muodostamiseen eri verkkotileihisi.



![Image](assets/fr/36.webp)



Nyt tiedät, miten PearPass-salasanahallintaohjelmaa käytetään. Tämän työkalun lisäksi päivittäinen digitaalinen turvallisuus riippuu asianmukaisten ratkaisujen oikeasta käytöstä. Jos haluat oppia, miten voit luoda turvallisen, vakaan ja tehokkaan henkilökohtaisen digitaalisen ympäristön, kutsun sinut tutustumaan tähän aiheeseen keskittyvään koulutukseemme:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1