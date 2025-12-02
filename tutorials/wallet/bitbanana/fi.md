---
name: BitBanana
description: Lightning-solmun mobiilihallinta
---

![cover](assets/cover.webp)



Tässä oppaassa opit asentamaan ja konfiguroimaan BitBanana Androidissa, jotta voit hallita Lightning-solmua älypuhelimesta. Näemme, miten sovellus liitetään olemassa olevaan infrastruktuuriin (Umbrel, RaspiBlitz, myNode tai mikä tahansa LND/Core Lightning-solmu), tehdään Lightning-maksuja, hallitaan kanavia etänä, tarkastellaan reititystuloja ja varmuuskopioidaan konfiguraatiot. Saat myös tietoa parhaista tietoturvakäytännöistä solmusi pääsyn suojaamiseksi ja siitä, miten se vertautuu suosittuun vaihtoehtoon Zeusiin.



## Esittelyssä BitBanana



BitBanana on avoimen lähdekoodin Android-mobiilisovellus, joka muuttaa älypuhelimesi täydelliseksi kojelaudaksi Lightning-solmun etähallintaa varten. Toisin kuin Lightning-lompakot, jotka upottavat paikallisen solmun puhelimeen, BitBanana omaksuu 100-prosenttisen etäohjausfilosofian: sovelluksessa ei ole satoshi:tä, ja se muodostaa yhteyden vain olemassa olevaan infrastruktuuriin.



Michael Wünschin MIT-lisenssillä kehittämä sovellus takaa täydellisen läpinäkyvyyden ilman henkilötietojen keräämistä ja todennettuja toistettavia rakennelmia. BitBanana tukee natiivisti LND:a ja Core Lightningia vakio-URI:iden (`lndconnect://` ja `clngrpc://`) kautta, mikä yksinkertaistaa huomattavasti alkuperäistä konfigurointia. Sovellus tunnistaa myös LndHubin ja Nostr Wallet Connectin käyttäjille, joilla ei ole henkilökohtaista solmua, vaikkakin nämä tilat toimivat custodial-periaatteella rajoitetuin toiminnoin.



Käyttöliittymä tarjoaa täyden pääsyn kaikkiin solmun kriittisiin toimintoihin: maksujen lähettäminen ja vastaanottaminen (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), Lightning-kanavien hallinta (avaaminen, sulkeminen, maksujen säätäminen, uudelleentasapainottaminen), edistynyt kolikoiden hallinta ja vartiotornin hallinta. BitBanana toteuttaa myös useita vankkoja tietoturvatasoja: biometrinen lukitus, häivytystila, hätä-PIN ja natiivi Tor-tuki yhteyksien anonymisoimiseksi.



## Tuetut alustat ja asennus



### Asennus



BitBanana on saatavilla yksinomaan Android 8.0:lle tai uudemmalle versiolle. Sovellusta ei ole iOS:ssä, eikä siitä ole suunnitteilla versiota. Tämä rajoitus selittyy projektin historialla: BitBanana on suora seuraaja Zap Androidille, jonka alun perin kehitti Michael Wünsch, joka päätti jatkaa työtään omalla tuotemerkillään. Zap oli erillisten sovellusten perhe (Zap Android, Zap iOS, Zap Desktop), joita eri tekijät kehittivät erillisillä koodipohjilla. BitBanana jatkaa vain Android-haaraa.



Lisäksi iOS-ekosysteemi asettaa merkittäviä lainsäädännöllisiä ja teknisiä rajoitteita muille kuin huoltajille tarkoitetuille Lightning-sovelluksille. Vuonna 2023 Apple hylkäsi Zeus-päivityksen "lisenssirikkomusten" vuoksi, ja vuonna 2024 Phoenix Wallet poistui Yhdysvaltain App Storesta Lightning-palveluntarjoajia koskevien sääntelyepävarmuuksien vuoksi. Nämä esteet selittävät, miksi monet Lightning-kehittäjät suosivat Androidia, joka tarjoaa avoimemman politiikan muille kuin huoltajasovelluksille.



Androidille on saatavilla kolme asennustapaa: Google Play Store (yli 5000 asennusta, automaattiset päivitykset), F-Droid (toistettavat rakennelmat, lähdekoodin tarkistaminen) tai manuaalinen APK GitHubista.



![BitBanana](assets/fr/01.webp)



Virallisella bitbanana.app-sivustolla (vasemmalla) kehutaan, että se on "100-prosenttisesti itsehallinnollinen ja tietojenkeruu on NOLLA". Keskimmäinen näyttö näyttää kolme latausvaihtoehtoa: F-Droid (suositeltava), Google Play ja APK. Oikeanpuoleisessa näytössä näkyy ilmoitusten salliminen maksuhälytyksiä varten.



Sovellus pyytää käyttöoikeuksia: verkko (solmuyhteys), kamera (QR-koodit), NFC (LNURL), taustapalvelut (ilmoitukset), biometria (turvallisuus) ja WireGuard VPN. Ei seurantalaitteita, ei tiedonkeruuta. Ota käyttöön salasana tai biometrinen lukitus käyttöoikeuden turvaamiseksi.



## Alkuperäinen konfigurointi



### Yhteyden muodostaminen LND-solmuun



Jos haluat muodostaa yhteyden BitBanana LND-solmuun (Umbrel, RaspiBlitz, myNode), hanki `lndconnect` URI tai QR-koodi, joka sisältää osoitteen, TLS-sertifikaatin ja todennusmakaronin.



Tässä ohjeessa käytämme LND-solmua umbrelin kautta. Lisätietoja on erillisessä opetusohjelmassamme :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Avaa Lightning Node -sovelluksen oikeassa yläkulmassa oleva valikko ja valitse "Connect wallet".



![BitBanana](assets/fr/04.webp)



Valitse **gRPC (Tor)** muodostaaksesi yhteyden Torin kautta (suositellaan). QR-koodi ja tiedot (Host .onion, Port 10009, Macaroon) tulevat näkyviin.



![BitBanana](assets/fr/02.webp)



Paina BitBanana-palvelussa "CONNECT NODE", skannaa QR-koodi tai liitä URI. Hyväksy kameran käyttöoikeus ja tarkista sitten näytetty .onion-osoite ennen vahvistusta.



**Core Lightning** -yhteys



Jos käytät Core Lightningia (CLN) LND:n sijasta, prosessi pysyy samanlaisena, ja URI `clngrpc://` sisältää keskinäiset TLS-varmenteet. Core Lightning tukee natiivisti BOLT12:ta (tarjoukset), mikä mahdollistaa uudelleenkäytettävät laskut ja toistuvat maksut, joita ei ole saatavilla LND:ssa.



**Yhteys ilman henkilökohtaista solmua (LNbits/hosted)**



Jos sinulla ei ole Lightning-solmua, BitBanana voi muodostaa yhteyden isännöityihin palveluihin LndHubin (BlueWalletin ja LNbitsin käyttämä protokolla) tai Nostr Wallet Connectin (NWC) kautta. Huomaa: nämä tilat toimivat säilytystilassa (palvelu isännöi varojasi) ja niiden toiminnot ovat rajoitettuja. Et voi hallita kanavia tai määrittää reititysmaksuja, ja voit lähettää ja vastaanottaa vain Lightning-maksuja.



Jos haluat lisätietoja LNbitsistä tai Nostr Wallet Connectista, tutustu erilaisiin opetusohjelmiin:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Päivittäinen käyttö



### Interface pääkone



Aloitusnäytössä näkyy Lightning-saldosi, ja vasemmalla ylhäällä olevasta valikosta pääset seuraaviin osioihin: Kanavat, Reititys, Allekirjoita/Varmenna, Solmut, Yhteystiedot, Asetukset, Varmuuskopiointi. Kello-kuvake (ylhäällä oikealla) avaa tapahtumahistorian. Alareunan "Lähetä"- ja "Vastaanota"-painikkeilla voit lähettää ja vastaanottaa satoshisi.



![BitBanana](assets/fr/05.webp)



### Lightning- ja on-chain-maksut



![BitBanana](assets/fr/10.webp)



**Maksun lähettäminen:** Paina "Lähetä"-painiketta aloitusnäytöstä. Maksunäytössä (vasemmalla) voit liittää osoitteen tai maksutiedot "Address tai maksutiedot" -kenttään, ja oikeassa yläkulmassa on QR-skanneri koodien skannausta varten. Voit myös valita Yhteystiedot-osiossa tallennetun yhteystiedon, jotta sinun ei tarvitse skannata joka kerta.



BitBanana tunnistaa älykkäästi kaikki maksuformaatit: lightning Address (sähköpostimuoto, kuten `utilisateur@domaine.com`), LNURL-pay-koodit dynaamisia maksuja varten, LNURL-withdraw varojen nostamista varten ja jopa Keysend-maksut suoraan Lightningin julkiseen avaimeen ilman edeltävää laskua. Sovellus suorittaa tarvittavat LNURL-ratkaisut automaattisesti taustalla.



Kun lasku on ladattu, BitBanana näyttää täydelliset tiedot: tarkan summan, arvioidut reititysmaksut, maksun kuvauksen (jos vastaanottaja on antanut sen) ja laskun päättymispäivän. Vahvistuksen jälkeen maksu reititetään Lightning-kanaviesi kautta. Tämän jälkeen voit tarkastella käytettyä reittiä siirto kerrallaan ja tosiasiallisesti maksettuja maksuja tapahtuman tiedoissa.



**Maksun vastaanottaminen:** Paina "Vastaanota"-painiketta. Valitsimen (oikealla näytöllä) avulla voit valita Lightning- (välitön maksu kanaviesi kautta) ja On-Chain-toiminnon välillä. Lightning-kuittia varten syötä haluamasi summa satosheina (tai jätä 0, jos haluat luoda laskun, jossa ei ole kiinteää summaa maksajan täytettäväksi), ja lisää valinnainen kuvaus, joka näkyy laskussa. BitBanana luo välittömästi Lightning-laskun, jossa on QR-koodi skannausta varten. Voit myös kopioida laskun tekstinä ja lähettää sen sähköpostitse. Heti kun maksu on vastaanotettu, saat push-ilmoituksen, ja maksutapahtuma näkyy välittömästi historiassa kaikkine yksityiskohtineen.



### Kanavat ja reititys



![BitBanana](assets/fr/06.webp)



"Kanavat"-osiossa näytetään lähetys-/vastaanottovalmiudet ja luetellaan kanavasi yksilöllisillä avatareilla. Kukin kanava näyttää likviditeettinsä jaettuna paikallisen ja etätasapainon välillä. Kosketa kanavaa saadaksesi täydelliset tiedot ja toimenpiteet (sulkeminen, reititysmaksujen muuttaminen). Oikealla ylhäällä olevilla kolmella pisteellä pääset "Rebalance"-vaihtoehtoon kanaviesi likviditeetin tasapainottamiseksi uudelleen. "+"-painike avaa uuden kanavan.



Reititysosio (keskusnäyttö) näyttää välitystulot jaksoittain (1D, 1W, 1M, 3M, 6M, 1Y) ja yksityiskohtaisen välityshistorian strategian optimoimiseksi.



Sign/Verify (oikeanpuoleinen ruutu) mahdollistaa viestien salauksen allekirjoittamisen/varmennuksen solmun hallinnan osoittamiseksi.



### Monisolmut ja parametrit



![BitBanana](assets/fr/07.webp)



**Solmujen hallinta**: Luettelo solmuistasi ja painikkeet, joilla voit lisätä solmuja manuaalisesti, skannata QR-koodeja tai vaihtaa solmujen välillä. Voit erityisesti määrittää erityyppisiä yhteyksiä samaan solmuun: LAN, VPN tai Tor.



**Hallitse yhteystietoja**: tallentaa Lightning-yhteystietosi nopeita maksuja varten.



**Asetukset**: mukauta valuutta, kieli, avatarit. Turvallisuus ja yksityisyys -osio: Salaa saldo (piilotustila), Tor (IP:n anonymisointi). Hintaorakkelien, lohkoetsintöjen, mukautettujen maksuestimaattoreiden konfigurointi.



## Edut ja rajoitukset



**Highlights:**




- Täydellinen liikkuvuus: hallitse Lightning-solmua mistä tahansa
- Täydelliset toiminnot: maksut (LNURL, Lightning Address, BOLT 12), kanavanhallinta, kolikoiden hallinta, vartiotornit, monisolmut
- Turvallisuus: PIN-koodi/biometriset tunnukset, häivytystila, hätä-PIN-koodi, natiivi Tor, kuvakaappauksen esto
- Ilmainen, avoin lähdekoodi (MIT), nollaprovisiot, nollatietojen keruu



**Rajoitukset:**




- Vaatii aktiivisen Lightning-solmun (tai LNbitsin holhoustilassa)
- IOS-versiota ei ole suunnitteilla
- Puhelimeen pääsyn turvaaminen on kriittisen tärkeää (makaroonin ylläpitäjä = täydellinen pääsy solmuun)



## Parhaat käytännöt



**Turvallisuus:**




- Aktivoi PIN-koodi/biometrinen lukitus (estää luvattoman pääsyn solmuun)
- Määritä hätä-PIN-koodi (poistaa arkaluonteiset tiedot pakkotilanteessa)
- Älä koskaan jaa kirjautumis-URI:täsi tai makaroonisi
- Häivytystila vihamielisissä ympäristöissä



**Login:**




- VPN mesh (Tailscale, ZeroTier): paras kompromissi nopeuden ja turvallisuuden välillä
- Tor: maksimaalinen luottamuksellisuus, suurempi viiveaika
- Clearnet: vältä, ellei ole välttämätöntä (IP-altistuminen, avoimet portit)



### Varmuuskopiointi ja palauttaminen



Lopuksi on "Varmuuskopiointi"-valikko, jonka avulla voit tallentaa kokoonpanosi puhelimen siirtämistä tai uudelleenasennusta varten.



![BitBanana](assets/fr/08.webp)



**Tärkeää:** Varmuuskopio EI sisällä seed- tai kanavavarmuuskopioita (jotka on tehtävä solmussa). Se sisältää: solmun konfiguraatiot (osoitteet, varmenteet, makaronit), tarrat, yhteystiedot, parametrit. Palauta-painikkeella voit tuoda olemassa olevan varmuuskopion. Vahvistus vaaditaan ennen tallentamista.



![BitBanana](assets/fr/09.webp)



Syötä salaussalasana (oikea näyttö). Järjestelmä avaa tiedostonvalitsimen (vasen näyttö) tallentaakseen `BitBananaBackup_2025-XX-XX-XX.dat`. Vahvistus "Varmuuskopio luotu".



**Turvallisuus:** Säilytä varmuuskopio salattuna (henkilökohtainen pilvi, USB, NAS). Älä koskaan jaa tiedostoja tai salasanoja. Testaa palautus säännöllisesti. Varmuuskopio palauttaa yhteydet, ei varoja.



## BitBanana vs. Zeus: Mitä eroa on?



Jos tutkit Lightning-solmun hallintaan tarkoitettuja mobiilisovelluksia, törmäät todennäköisesti Zeukseen, joka on suosittu vaihtoehto BitBanana-ohjelmalle. Toisin kuin BitBanana, joka keskittyy yksinomaan olemassa olevan solmun etähallintaan, Zeus tarjoaa kattavamman lähestymistavan ja kaksi toimintatapaa: suoraan sovellukseen upotettu Lightning-solmu (upotettu tila, jossa on integroitu LND) ja etäyhteys ulkoiseen solmuun, aivan kuten BitBanana.



Tämä kaksoistoiminnallisuus tekee Zeuksesta erityisen houkuttelevan aloittelijoille, jotka haluavat kokeilla Lightningia ilman aiempaa infrastruktuuria. Sulautettu tila mahdollistaa välittömän käynnistyksen täydellisellä mobiilisolmulla, kun taas edistyneet käyttäjät voivat siirtyä etäyhteyteen, kun heidän henkilökohtainen solmunsa on konfiguroitu. Zeus tukee myös LND:tä ja Core Lightningia etäyhteyttä varten, kuten BitBanana.



Toinen Zeuksen merkittävä etu on sen alustarajat ylittävä saatavuus (iOS ja Android), kun taas BitBanana on yksinomaan Android-pohjainen. Zeus sisältää myös Olympus LSP -infrastruktuurin, joka helpottaa Lightning-maksujen vastaanottamista just-in-time-kanavien kautta, myyntipistejärjestelmän kauppiaille ja integroidun swap-toiminnon likviditeetin hallitsemiseksi.



BitBanana on kuitenkin säilyttänyt erityiset vahvuutensa: yksinkertaisempi ja virtaviivaisempi käyttöliittymä, parempi käyttäjäkokemus (UX), koska se keskittyy yksinomaan kauko-ohjaukseen, ja opettavainen lähestymistapa, jossa on kontekstisidonnaisia selityksiä. Zeus tarjoaa enemmän toimintoja, mutta monimutkaisemman käyttöliittymän kustannuksella. Sovellus soveltuu edelleen erityisesti käyttäjille, jotka haluavat hallita solmua yksinomaan etäältä ilman huoltajatoimintoja.



Jos haluat lisätietoja Zeuksesta, tutustu seuraaviin opetusohjelmiin:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Päätelmä



BitBanana muuttaa Android-älypuhelimesi täydelliseksi Lightning-kojelaudaksi, joka tarjoaa ennennäkemätöntä liikkuvuutta solmujen operaattoreille. Sovellus kattaa kaikki toiminnot: maksut (kaikki muodot), kanavien hallinta, kolikoiden hallinta, vartiotornit, monisolmut ja parannettu turvallisuus (PIN/biometria, Tor, hätä-PIN).



Täysin suvereeni BitBanana ei kerää tietoja eikä vaaranna varojesi luottamuksellisuutta tai valvontaa. Avoin lähdekoodi (MIT) takaa avoimuuden.



## Resurssit



### Viralliset asiakirjat




- [BitBanana verkkosivuilla](https://bitbanana.app)
- [Täydellinen dokumentaatio](https://docs.bitbanana.app)
- [GitHub-lähdekoodi](https://github.com/michaelWuensch/BitBanana)



### Asennus




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)