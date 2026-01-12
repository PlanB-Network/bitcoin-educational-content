---
name: White Noise
description: Yksityinen, hajautettu viestisovellus, joka perustuu Nostr- ja MLS-protokolliin
---

![cover](assets/cover.webp)




## Johdanto



"Vaikeuksien keskellä on mahdollisuus". Tämä Albert Einsteinin sitaatti muistuttaa meitä siitä, että ongelmat eivät ole lopullisia, vaan ne sisältävät uusien, innovatiivisten ratkaisujen siemeniä.



Tässä oppaassa esittelemämme ratkaisun käyttöönoton taustalla olevat motiivit kuvaavat tätä täydellisesti. Se on **White Noise**, joka on syntynyt välttämättömyydestä.



Sen perustajan Max Hillebrandin sanoin, joista *Bitcoin Magazine* kertoo: "Käynnistimme tämän hankkeen vaihtoehtojen puutteessa." Hän selittää, että "nykyiset salaussovellukset ovat tehottomia suuressa mittakaavassa: 100 henkilön lisääminen ryhmäkeskusteluun hidastaa salausta huomattavasti. Hajautetut alustat eivät puolestaan tarjoa yksityistä viestinvälitystä. Lopuksi Nostr:n avoin releverkko antaa kaikille mahdollisuuden levittää ideoita, mutta suorien viestien suojaus on edelleen dramaattisen riittämätön. Tajusimme: vapauden suojelemiseksi meidän oli yhdistettävä nämä järjestelmät."



## Mikä on White Noise?



White Noise on voittoa tavoittelemattoman tiimin kehittämä avoimen lähdekoodin viestisovellus. Sovellus edistää turvallisuutta, yksityisyyttä ja hajauttamista. Toisin kuin perinteiset sovellukset, se ei vaadi puhelinnumeroa eikä sähköpostiosoitetta.


White Noise:n erityispiirteenä on kahden perustavanlaatuisen protokollan - Nostr ja MLS - integrointi, jotka muodostavat sen teknisen perustan.



Nostr (Notes and Other Stuff Transmitted by Relays) on hajautettu, avoimen lähdekoodin protokolla, joka on suunniteltu vastustamaan sensuuria.  Protokollassa käytetään releitä, avainpareja ja asiakkaita.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Valkoisen kohinan avulla voit jopa valita omat releasetuksesi yksityisyyden maksimoimiseksi.



MLS (Messaging Layer Security) on puolestaan tietoturvaprotokolla, joka mahdollistaa viestien päästä päähän -salauksen. Toisin sanoen viesteihin pääsee käsiksi vain päätepisteissä eli viestin lähettäjällä ja vastaanottajalla. Tämä tarkoittaa, että viestien reitittämiseen osallistuvat välittäjät eivät pääse käsiksi niiden sisältöön.



Tässä on nopea vertailu White Noise:n ja tunnetuimpien viestisovellusten välillä.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## White Noise:n käytön aloittaminen



### White Noise asennus



Mene [White Noise:n verkkosivustolle](https://www.whitenoise.chat/) ja napsauta sitten **Lataus**.



![screen](assets/fr/03.webp)



White Noise on tällä hetkellä saatavilla vain mobiililaitteissa.


Paina avautuvassa uudessa käyttöliittymässä :





- **Zapstore**- tai **Android APK** -painiketta, jos haluat ladata sen Androidille ;
- **iOS TestFlight**-painiketta, jos käytät iPhonea.



![screen](assets/fr/04.webp)



Tässä oppaassa teemme Android-latauksen.


Jos päätät ladata **Zapstoren** kautta, sinut ohjataan sinne. Kun olet Zapstoressa, kirjoita hakupalkkiin **White Noise**. Jatka sitten lataamista napsauttamalla **Asenna**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Jos päätät ladata APK-tiedoston, sinut ohjataan White Noise:n GitHub-arkistoon, josta voit valita oikean version älypuhelimeesi.



Saatavilla olevat APK-tiedostot ovat :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), sopii uusimpiin puhelimiin, joissa on 64-bittinen prosessori;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) sopii vanhemmille puhelimille, joissa on 32-bittinen prosessori.



Sinulla on myös **.sha256**-tiedostoja, jotka ovat vain tarkistussummia, joilla varmistetaan latauksen eheys.



![screen](assets/fr/07.webp)



Kun lataus on valmis, asenna ja avaa sovellus.



![screen](assets/fr/08.webp)



### Käyttäjätilin alkuasetukset



Jos haluat muodostaa ensimmäisen yhteyden White Noise:aan, paina **Registeröi**-painiketta.



![screen](assets/fr/09.webp)



Määritä seuraavaksi profiilisi valitsemalla profiilikuva, nimi ja lisäämällä lyhyt kuvaus itsestäsi. Sinun ei tarvitse täyttää todellista henkilöllisyyttäsi (nimi ja valokuva).


Huomaa, että White Noise valitsee sinulle automaattisesti nimen (pseudonyymin), jonka voit pitää tai muuttaa. Paina lopuksi **End**-painiketta.



![screen](assets/fr/10.webp)



Sinut ohjataan White Noise:n **kotinäyttöön**, jossa keskustelusi on lueteltu. Tilisi on nyt perustettu ja valmis käytettäväksi. Voit jakaa profiilisi tai etsiä ystäviä aloittaaksesi keskustelun.



![screen](assets/fr/11.webp)




### White Noise-liitäntöjen löytäminen



Pääkäyttöliittymässä näytön yläreunassa näkyy :



Vasemmassa yläkulmassa oleva profiilikuvake on profiilikuvasi pikkukuva tai profiilinimesi ensimmäinen kirjain. Pääset tilisi asetuksiin napsauttamalla sitä.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



Oikeassa yläkulmassa on kuvake uuden keskustelun aloittamista varten.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Käyttäjätilin asetukset



Pääset asetuksiin painamalla vasemmassa yläkulmassa olevaa profiilikuvaketta.



![screen](assets/fr/16.webp)



**Asetukset** -käyttöliittymän yläreunassa on kuvasi ja profiilinimesi, jonka jälkeen julkinen avaimesi, jonka voit jakaa sen vieressä olevan QR-koodin avulla.



![screen](assets/fr/17.webp)



Aivan alapuolella on **Vaihda tili**-painike, jonka avulla voit muodostaa yhteyden toiseen profiiliin sovelluksessa.



![screen](assets/fr/18.webp)



Sitten on ensimmäinen osio, jossa on neljä (4) alavalikkoa, kuten :





- Muokkaa profiilia**



Tässä alivalikossa voit muokata profiilin nimeä, Nostr-osoitetta (NIP-05).... Muista klikata **Save** tallentaaksesi muutokset.



![screen](assets/fr/19.webp)





- Profiilin avaimet**



Täällä sinulla on pääsy julkisiin ja yksityisiin (salaisiin) avaimiin. Kuten White Noise muistuttaa, yksityistä avaintasi ei saa missään tapauksessa paljastaa.



![screen](assets/fr/20.webp)





- Verkkovirtarele



Tässä alivalikossa voit lisätä tai poistaa **yleisiä releitä** (releet, jotka on määritelty käytettäväksi kaikissa Nostr-sovelluksissasi), **laatikkoreleitä** ja **avainpakettireleitä**.



Voit poistaa releen napauttamalla sen edessä olevaa **roskat**-kuvaketta tai lisätä uuden releen napauttamalla **+** (plus) -kuvaketta.



![screen](assets/fr/21.webp)





- Irrottaminen**



Voit katkaista tilisi yhteyden sovellukseen napsauttamalla tätä alivalikkoa. Varmista kuitenkin, että olet tallentanut yksityiset avaimesi offline-tilaan, muuten et voi kirjautua myöhemmin uudelleen.



![screen](assets/fr/22.webp)




Toinen osio tarjoaa alavalikot:





- Sovellusasetukset



Täällä voit määrittää sovelluksen ulkoasun (teema ja näyttökieli) ja jopa poistaa tietoja, jos koet, että ne on vaarannettu, tai jos koet itse olevasi vaarassa.



![screen](assets/fr/23.webp)





- Lahjoita White Noise:lle



Voit tukea White Noise:n takana olevaa tiimiä (voittoa tavoittelematon järjestö) lahjoituksilla heidän Lightning-osoitteensa tai Bitcoin:n hiljaisen maksun osoitteen kautta.



![screen](assets/fr/24.webp)



Lopuksi, aivan alareunassa ovat **kehittäjän asetukset**.



![screen](assets/fr/25.webp)




## Aloita keskustelu



Katsotaanpa nyt, miten keskustelu aloitetaan. Tätä kirjoitettaessa White Noise tarjoaa kolme viestintävaihtoehtoa. Tutustumme vuorollaan **yksityisiin keskusteluihin** (**Chat 1:1**), eli vain sinun ja yhden toisen henkilön väliseen keskusteluun, **ryhmäkeskusteluihin** ja **Multimediatiedostojen lähettämiseen**.




### Kissa 1:1



Jos haluat lisätä uuden kirjeenvaihtajan, napsauta pääkäyttöliittymässä uuden keskustelun aloittamista koskevaa kuvaketta.


Skannaa sitten julkisen avaimen QR-koodi (1) tai liitä uuden kirjeenvaihtajasi julkinen avain (2) hakupalkkiin löytääksesi hänet.



![screen](assets/fr/26.webp)



Napauta sitten **Aloita keskustelu**-painiketta aloittaaksesi keskustelun kirjeenvaihtajasi kanssa. Voit myös **seurata** kirjeenvaihtajaasi tai kutsua hänet ryhmäkeskusteluun painamalla **Lisää ryhmään** -painiketta.



![screen](assets/fr/27.webp)



Ensimmäinen viestisi uudelle kirjeenvaihtajalle on kuin kutsupyyntö. Kirjeenvaihtajan on hyväksyttävä tämä pyyntö, ennen kuin voit viestiä hänen kanssaan. Jos hän kieltäytyy, keskustelu ei ole mahdollista.



![screen](assets/fr/28.webp)



Lisäksi niin kauan kuin he eivät hyväksy kutsuasi, he eivät voi lukea alkuperäisen viestisi sisältöä.



Kun hän hyväksyy kutsun, hän voi vastata sinulle, ja voitte kommunikoida saumattomasti ja turvallisesti.



![screen](assets/fr/29.webp)



Lisäksi keskustelussa on lisätoimintoja.



Voit painaa pitkään tietyn viestin kohdalla näyttääksesi vaihtoehtoja, kuten :




- reagoida viestiin hymiöllä (1) ;
- voit vastata viestiin **suoralla lainauksella** painamalla **Vastaaminen** (2) ;
- kopioi viesti painamalla **Kopioi** (3).



![screen](assets/fr/30.webp)





- poista viesti **Poista**-painikkeella vain, jos se on peräisin sinulta.



![screen](assets/fr/31.webp)



Voit tehdä haun keskustelun sisällä.



Napsauta kirjeenvaihtajan avataria näytön yläreunassa päästäksesi "keskustelutietoihin" ja napauta **Haku keskustelussa**-painiketta.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Kirjoita avautuvaan hakupalkkiin sana, jota haluat etsiä, ja käynnistä haku. Tämän jälkeen näet hakusanasi korostettuna **liioilla kirjaimilla**.



![screen](assets/fr/34.webp)




### Ryhmäkeskustelut



White Noise:ssä voidaan luoda keskusteluryhmiä.



Voit tehdä tämän koskettamalla uuden keskustelun käynnistyskäyttöliittymän kuvaketta ja valitsemalla sitten **Uusi ryhmäkeskustelu**. Kirjoita sitten hakupalkkiin sen ensimmäisen jäsenen julkinen avain, jonka haluat lisätä ryhmään.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Jos tämä vaihtoehto ei toimi, kirjoita **Aloita uusi keskustelu** -käyttöliittymästä hakupalkkiin sen ensimmäisen jäsenen julkinen avain, jonka haluat lisätä ryhmään. Voit myös skannata hänen julkiseen avaimeensa liittyvän QR-koodin.



Tällä kertaa napauta **Keskustelun aloittaminen**-painiketta napsauttamisen sijasta **Lisää ryhmään**-painiketta.



![screen](assets/fr/37.webp)



Napauta avautuvassa ponnahdusvalikossa **Uusi ryhmäkeskustelu**.



![screen](assets/fr/38.webp)



Paina sitten **Jatka** (sinun ei tarvitse syöttää sen julkista avainta uudelleen).



![screen](assets/fr/39.webp)



Ryhmän luojana olet automaattisesti sen ylläpitäjä. Täytä ryhmän tiedot, kuten **ryhmän nimi ja kuvaus**, ja napsauta sitten **Luo ryhmä**-painiketta.



![screen](assets/fr/40.webp)



Käyttäjä, jonka lisäät ensimmäiseksi jäseneksi, ja kaikki muut myöhemmin lisäämäsi käyttäjät saavat ilmoituksen, jossa heitä pyydetään liittymään ryhmään. Heidän on hyväksyttävä klikkaamalla **Accept** (Hyväksy**) liittyäkseen ryhmään.



![screen](assets/fr/41.webp)



On myös mahdollista lisätä uusi jäsen, jonka kanssa jo keskustelet olemassa olevaan ryhmään. Voit tehdä niin napsauttamalla kirjeenvaihtajan avataria näytön yläreunassa, jolloin pääset "keskustelutietoihin", ja napauttamalla **Lisää ryhmään**-painiketta.



![screen](assets/fr/42.webp)



**Valitse** esiin tulevassa uudessa käyttöliittymässä ryhmä, johon haluat lisätä hänet, ja napauta **Lisää ryhmään**. Sinun tarvitsee enää vain odottaa, että se suostuu liittymään ryhmään.



![screen](assets/fr/43.webp)



Huomaa, että vain ryhmän ylläpitäjä voi muokata ryhmän tietoja ja lisätä tai poistaa jäseniä. Lisäksi avaimen kierto estää kiellettyjä jäseniä purkamasta tulevia viestejä.



Jos haluat poistaa jäsenen, napauta ryhmän pääkäyttöliittymässä ryhmän yläreunassa olevaa ryhmäkuvaketta päästäksesi ryhmän tietoliittymään.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Napsauta sitten jäsenen nimeä ja **Poista ryhmästä**. Tästä käyttöliittymästä voit myös lähettää hänelle viestin, seurata häntä tai lisätä hänet toiseen ryhmään.



![screen](assets/fr/46.webp)



### Multimediatiedostojen lähettäminen



Tällä hetkellä White Noise:ssä voidaan jakaa vain valokuvia käyttäjien kesken. Olitpa sitten yksityisessä keskustelussa tai ryhmäkeskustelussa, sinun täytyy :





- paina tekstiviestin syöttökentän vasemmalla puolella olevaa **plus (+)** -symbolia.



![screen](assets/fr/47.webp)





- klikkaa sitten alareunassa olevaa ruutua **Kuvat** päästäksesi galleriaan.



![screen](assets/fr/48.webp)





- valitse lähetettävät kuvat.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Tärkeimmät muistettavat seikat



White Noise tarjoaa hyvän luottamuksellisuustason ja erinomaisen turvallisuuden. Toisaalta se on hyvin tuore sovellus, joka ei ole vielä kovin yleinen ja joka on vielä lapsenkengissä. Näin ollen on vielä liian aikaista tehdä aktiivisia johtopäätöksiä. On mahdollista, että käytön aikana ilmenee muutamia toimintahäiriöitä.



Tällä hetkellä siitä puuttuu tiettyjä toimintoja (ei ääni- tai videopuheluita, ei ääni- tai videomultimediatiedostojen lähettämistä) verrattuna suosittuihin viestisovelluksiin.



White Noise on kuitenkin edelleen mielenkiintoinen vaihtoehto keskusteluihin, joissa luottamuksellisuus on ensiarvoisen tärkeää (esim. perheen, läheisten ystävien tai yhteisen asian puolesta toimivien aktivistien kanssa), vaikka sen asentaminen (vaihtoehtoisten sovelluskauppojen tai APK-tiedostojen kautta) ja opettelu (avainparien, asiakkaiden ja välittäjien käsitteen hallitseminen Nostr-protokollan avulla) vaatii hieman vaivaa.



Nyt tiedät, miten White Noise:n avulla voit viestiä turvallisesti ystäviesi ja perheesi kanssa. Anna meille peukku ylöspäin, jos tämä opetusohjelma on mielestäsi hyödyllinen.



Suosittelemme Tox Chat -ohjelmaa, jonka avulla voit keskustella ilman välikäsiä hajautetun Tox-protokollan välityksellä.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3