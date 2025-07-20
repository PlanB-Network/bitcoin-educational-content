---
name: BTC-kartta
description: Etsi paikkoja, joissa voit viettää Sats
---
![cover](assets/cover.webp)



Vaikka monet vähentävät Bitcoin:n edelleen sijoitus- ja keinotteluvälineeksi, sen luoja Satoshi Nakamoto suunnitteli sen ensisijaisesti vertaisverkkomaksujärjestelmäksi. On kuitenkin Hard tärkeää tietää, mihin bitcoineja voi käyttää. Mutta se oli ennen BTC Mapia.



BTC Map perustuu OSM:ään (OpenStreetMap), joka on avoimen lähdekoodin osallistava karttatyökalu, ja tarjoaa yksinkertaisen tavan listata toimipaikat, jotka hyväksyvät maksut BTC:nä, Lightningina tai On-Chain:nä. Maailmanlaajuinen tietokanta, joka on vielä alkutekijöissään, mutta jo nyt olennainen, ja jota bitcoin-asiakkaat ovat täyttäneet ja joka on tarkoitettu bitcoin-asiakkaille.



Mene osoitteeseen [btcmap.org](https://btcmap.org/):



![image](assets/fr/01.webp)



Saatavilla :




- iOS kautta [AppStore](https://apps.apple.com/app/btc-world-map/id6443604345)
- Android kautta [Play Store](https://play.google.com/store/apps/details?id=org.btcmap.app)
- [F-Droid](https://f-droid.org/en/packages/org.btcmap/) androidin avoimen lähdekoodin sovellusluettelo
- lataamalla [apk android](https://github.com/teambtcmap/btcmap-android/releases/latest) suoraan projektin githubista
- verkkosovelluksen kautta selaimesta (tämänhetkinen näkemyksemme)



Tänään keskitymme verkkoversioon. Toistaiseksi se on kokonaan englanninkielinen, joten tarkastellaan eri osioita yhdessä. Ja jos jokin painike tai linkki ei toimi, klikkaa hiiren oikealla painikkeella -> avaa toisessa välilehdessä.



Aloitetaan. Oikealla ylhäällä olevalla pienellä kuun tai auringon kuvakkeella voit vaihtaa vaalean ja tumman teeman välillä.



![image](assets/fr/02.webp)



Sivuston yläosassa olevat eri välilehdet vasemmalta oikealle:




- bTC Map -logo: paluu etusivulle
- "Kartat": tuotteen sydän, jossa on kaksi karttaa (tilat ja yhteisöt)
- "Sovellukset: eri mediat, joihin BTC Map voidaan asentaa"
- "Alueet": yhteisön esittely ja tilastot maanosittain ja maittain
- "Ylläpito": osallistuminen karttojen päivittämiseen ja täydentämiseen
- " Wiki: projektin GitHub-sivusto
- "Tue meitä": lahjoitukset ja sponsorointi ovat hankkeen ainoa tulonlähde



Nämä välilehdet muodostavat muuten tämän oppaan sisällysluettelon.



## MAPS



Sivusto tarjoaa kaksi korttia, joilla on eri tavoitteet. Aloitetaan kuitenkin kuvaamalla työkalut, jotka näkyvät molempien korttien vasemmassa reunassa:



![image](assets/fr/03.webp)





- 1: zoomaus
- 2: pienennä
- 3: suuri näyttö
- 4: paikanna minut (jos selaimesi sallii sen)
- 5: (kauppiaskartta) etsi myymälä nimen perusteella
- 6: (kauppakartta) näyttää vain tehostetut toimipaikat
- 7: paluu etusivulle
- 8: (kauppiaskartta) lisää myymälä
- 9: Vaihda "yhteisön" kortista "kauppiaan" korttiin ja päinvastoin



*huomautus: Tehostetut toimipaikat ovat toimipaikkoja, jotka ovat saaneet vinkin tyytyväiseltä kävijältä tai käyttäjältä, mikä parantaa niiden näkyvyyttä jonkin aikaa*



Huomaat myös, että jokaisen kartan oikeassa yläkulmassa on painike, jolla voit vaihtaa kartan Layer:n. Tässä opetusohjelmassa olen päättänyt jättää tumman version.



## Kauppias Kartta



![image](assets/fr/04.webp)



Kauppiaskartta sisältää luettelon toimipaikoista ympäri maailmaa, jotka hyväksyvät maksun BTC:nä. Näet erilaisia kuvakkeita, jotka ovat ensimmäinen vihje toimipaikan luonteesta (tuoppi baarille, timantti koruliikkeelle...). Otan yhden satunnaisesti.



Jos napsautat tätä teksasilaista maisemataiteilijaa, näkyviin tulee insertti:



![image](assets/fr/05.webp)





- Sinisellä merkitty nimi on laitoksen nimi
- Address ja aukioloajat on ilmoitettu alla, jos ne ovat saatavilla OSM:ssä
- "Navigoi" voi luoda reitin sijaintisi ja laitoksen välille
- "Muokkaa" antaa sinulle mahdollisuuden ehdottaa muutoksia OSM-tiedostoon (vaatii ilmaisen OSM-tilin), esim. nimi, yhteystiedot, aikataulut jne
- "Jaa" vie sinut laajennettuun sivuston kuvaukseen
- "Lisää" avaa seuraavat vaihtoehdot:



![image](assets/fr/06.webp)





- "Soita" on puhelimen pikavalinta, jolla soitetaan laitokseen
- "Verkkosivusto" vie sinut yrityksen verkkosivustolle
- "Näytä tunnisteet" näyttää OSM:ään syötetyt kohteet käynnistämättä hyperlinkkejä tai sovelluksia
- "Tag Issues" ja "Map Legend" ovat tällä hetkellä rikkinäisiä linkkejä
- "View OSM" pyytää sinua avaamaan laitoksen sijainnin OSM-sovelluksessa



Vihdoinkin,





- "Last Surveyed" tarkoittaa päivämäärää, jolloin tiedosto on viimeksi luotu tai päivitetty
- "Boost" antaa sinulle mahdollisuuden tarjota sivustollesi Sats:n maksua vastaan ajallisesti rajoitetun näkyvyysedun
- lopuksi "Tarkista sijainti" vie sinut BTC Map -lomakkeelle, jossa voit ehdottaa luettelon päivittämistä. Katsotaanpa, miltä se näyttää:



![image](assets/fr/07.webp)





- 1: Merkitse tämä ruutu, jos haluat vain vahvistaa, että tiedoston tiedot ovat ajan tasalla (tässä tapauksessa siirry suoraan vaiheeseen 4)
- 2: Ilmoittakaa tässä, mitkä tiedot ovat virheellisiä ja mitä korjausta ehdotatte
- 3 : Kuvailkaa tässä, miten saitte tiedot (käynti, puhelu...)
- 4: Jatka captcha-varmennukseen (isot ja pienet kirjaimet huomioiva)
- 5 : Klikkaa "Lähetä raportti" lähettääksesi ehdotuksesi



## Yhteisön kartta



![image](assets/fr/08.webp)



Yhteisön kartan avulla voit tutustua eri Bitcoin-yhteisöihin ympäri maailmaa, jakaa ne ja esittää ne maantieteellisesti.



![image](assets/fr/09.webp)



Huomaat heti oranssin väriset alueet. Kuten näet, nämä ovat eri Bitcoin-yhteisöjä, jotka on lueteltu BTC Mapissa. Napsauttamalla mitä tahansa niistä vasemmalla painikkeella saat esiin pienen insertin, jossa näkyvät kaikki tarjotut linkit, kuten verkkosivusto ja sosiaalisen verkoston tilit. Kuka tietää, saatat olla keskellä aktiivista Bitcoin-yhteisöä, ja olet vain muutaman klikkauksen päässä liittymisestä siihen, jos siltä tuntuu!



## Muut sivuston välilehdet



**Sovellukset**: Tällä sivulla muistutetaan siitä, millä välineillä BTC Map on saatavilla.



**Stats** tarjoaa useita tilastoja sovelluksesta:




- Kojelauta: tietokantasyötettä koskevat tilastotiedot, kuten luetteloitujen toimipaikkojen määrä tai äskettäin tehtyjen tarkistusten määrä
- Tagger Leaderboard: taulukko käyttäjistä, jotka on asetettu paremmuusjärjestykseen osallistumisen määrän mukaan (liity heihin!)
- Community Leaderboard: yhteisön sijoitukset
- Maa Leaderboard



**Alueet (vyöhykkeet)** antaa sinulle muita tietoja kuin karttoja:




- Yhteisöt: luetellaan eri rekisteröidyt yhteisöt, lomake uuden yhteisön rekisteröintiä varten ja muutamia tilastoja, kaikki ryhmiteltyinä maanosittain
- Maat: muutama maittain ryhmitelty tilasto näyttää toimipaikkojen, osallistujien ja päivitettävien tiedostojen määrän...



**Maintain (ylläpitää)**




- Lisää paikka: lisää paikka, joka hyväksyy Bitcoin-maksuja
- Tarkista sijainti: päivitä/korjaa jo luettelossa olevan laitoksen tiedot
- Lisää yhteisö: Lisää yhteisö (url-osoitteessa on kirjoitusvirhe, pääset lomakkeeseen menemällä Areas -> Communities -> Add Community)
- Avoimet liput: tänne tulevat lisäyksiä, tarkistuksia, sijainteja ja yhteisöjä koskevat pyynnöt, jotka vapaaehtoiset käsittelevät
- Toimintojen merkitseminen: näyttää projektin osallistujien (kuka tahansa käyttäjä, kuten sinä tai minä, voi olla osallistuja) viimeisimmät toimet, kuten viimeisimmät lisätyt, päivitetyt tai jopa poistetut sijainnit....
- Tagging Issues: tässä käyttäjät listaavat kaikki tagging-virheet



**Wiki**: Tämä linkki vie sinut projektin GitHub-sivulle.



**Tuki meille**: Tällä sivulla kerrotaan, miten voit tehdä lahjoituksen (Sats) tai ryhtyä projektin sponsoriksi.



## "Lisää yhteisö



BTC Mapin avulla voit [lisätä oman yhteisön] (https://btcmap.org/communities/add/), katsotaanpa sitä askel askeleelta:




![image](assets/fr/10.webp)





- 1: Yhteisöäsi vastaava vyöhyke
- 2: Yhteisösi nimi
- 3: Verkkosivuston URL-osoite
- 4: Lightning Address, johon voidaan lähettää vihjeitä
- 5: Viittaukset sosiaalisiin verkostoihin, joissa yhteisösi on läsnä
- 6: Sähköpostisi Address, jotta foorumi voi tarvittaessa pyytää sinulta lisätietoja
- 7: Lyhyt kuvaus (esim. saksankielinen yhteisö, Frankfurtin alue)
- 8: Täytä captcha (isot ja pienet kirjaimet huomioidaan)
- 9: Lähetä lomake napsauttamalla "Lähetä yhteisö"



## "Lisää sijainti



[Tällä sivulla](https://btcmap.org/add-location/) näytetään, miten voit itse lisätä Bitcoin-vaatimusten mukaisen kiinteistöluettelon Open Street Mapin avulla. Jos sinulla on ongelmia, voit täyttää lomakkeen, jotta joku muu voi luoda listan puolestasi (tämä voi kestää useita viikkoja). Katsotaanpa:



![image](assets/fr/11.webp)





- 1: Laitoksen nimi
- 2: Fyysinen Address (pakollinen, tarvitset katu-Address:n)
- 3: Merkitse tarkka piste kartalle
- 4 : Mihin luokkaan kasvi kuuluu?
- 5: Mitä Bitcoin-maksuvälineitä on saatavilla (BTC, Lightning, kontaktiton)?



![image](assets/fr/12.webp)





- 6: Verkkosivuston URL-osoite (valinnainen)
- 7: puhelinnumero (vapaaehtoinen)
- 8: Aukioloajat (vapaaehtoinen)
- 9: Koulun X-tili (Twitter), sitten oma tilisi (vapaaehtoinen)
- 10: Mikä tahansa tarpeelliseksi katsomasi yksityiskohta
- 11: Sinun roolisi
  - "Minä olen yrityksen omistaja": Olen yrityksen johtaja
  - "Kävin asiakkaana": Kävin tässä laitoksessa asiakkaana
  - "muu menetelmä
- 12 : Sähköpostisi Address, jos foorumi tarvitsee lisätietoja
- 13: Captcha-tarkistus (suuraakkoset huomioiva)
- 14 : Klikkaa "Lähetä sijainti" lähettääksesi listasi



Sivun alareunassa on useita välilehtiä, jotka voivat myös kiinnostaa, jos Shakespearen kieli ei ole sinulle esteenä. Siellä on Eric Hughesin 9. maaliskuuta 1993 julkaisema Cypherpunks-manifesti tai Satoshi Nakamoton 31. lokakuuta 2008 julkaisema valkoinen kirja.


Jos haluat lisätietoja, käy BTC Mapiin liittyvillä eri verkkoalustoilla.



![image](assets/fr/13.webp)



Siinä kaikki, olemme käyneet yhdessä läpi sivuston tärkeimmät ominaisuudet. Nyt tiedät, mihin käyttää bitcoinisi BTC-kartan ansiosta!