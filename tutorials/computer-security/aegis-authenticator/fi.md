---
name: Aegis Authenticator
description: Miten voit käyttää Aegis Authenticatoria tilien suojaamiseen kaksoistodennuksella?
---

![cover](assets/cover.webp)



Kaksitekijätodennus (2FA) on nykyään välttämätön verkkotilien suojaamisessa. Se lisää salasanan lisäksi toisen tekijän (usein kuusinumeroisen koodin), joka vanhenee 30 sekunnin kuluttua, mikä vaikeuttaa hakkerien toimintaa huomattavasti. Erityisen TOTP-sovelluksen (*Time-based One-Time Password*) käyttäminen on turvallisempaa kuin tekstiviestien lähettäminen, sillä ne voidaan kaapata SIM-kortin vaihtohyökkäyksillä.



Kaikki todennussovellukset eivät kuitenkaan ole samanlaisia. Monet omat ratkaisut (Google Authenticator, Authy jne.) aiheuttavat ongelmia: ne ovat omia ja suljetun lähdekoodin ratkaisuja (niiden turvallisuutta on mahdotonta tarkastaa), ne sisältävät joskus mainonnan seurantalaitteita, ne eivät tarjoa salattua varmuuskopiota koodeistasi, ja ne voivat jopa estää tiliesi viennin ja lukita sinut niiden ekosysteemiin.



Aegis Authenticator on puolestaan ilmainen ja eettinen vaihtoehto näille sovelluksille. Aegis on ilmainen, turvallinen ja avoimen lähdekoodin sovellus, jolla voit hallita kaksivaiheisen todentamisen tunnuksia Androidissa. Sen kehityksessä keskitytään olennaisiin ominaisuuksiin, joita muut sovellukset eivät tarjoa, kuten paikallisten tietojen vankkaan salaukseen ja mahdollisuuteen tehdä turvallisia varmuuskopioita. Kaiken kaikkiaan Aegis tarjoaa paikallisen, tarkastettavissa olevan kaksivaiheisen todennusratkaisun, joka on ihanteellinen kaikille, jotka haluavat säilyttää 2FA-koodiensa täydellisen hallinnan.



## Aegis Authenticatorin esittely



Aegis Authenticator on avoimen lähdekoodin 2FA-sovellus Androidille, joka on julkaistu GPL v3 -lisenssillä. Se erottuu edukseen "Privacy by design" -filosofiansa ansiosta: sovellus toimii täysin offline-tilassa eikä vaadi yhteyttä etäpalveluun. Tämän seurauksena tunnisteesi säilyvät paikallisesti laitteellasi suojatussa kassakaapissa, jonka avain on vain sinulla.



### Tärkeimmät ominaisuudet



**Salattu holvi:** Kaikki OTP-koodisi tallennetaan AES-256-salaiseen holviin (GCM-tila), joka on suojattu käyttäjän määrittelemällä pääsalasanalla. Voit avata holvin lukituksen salasanalla tai biometrisillä tiedoilla (sormenjälki, kasvojentunnistus) lisämukavuuden lisäämiseksi. Ilman salasanaa tiedot olisivat salaamattomia, joten suosittelemme vahvasti salasanan asettamista.



**Edistynyt organisointi:** Aegis pitää monet 2FA-tilisi hyvin järjestyksessä. Voit lajitella merkinnät aakkosjärjestykseen tai haluamaasi järjestykseen, ryhmitellä ne kategorioiden mukaan (esim. Henkilökohtainen, Työ, Sosiaalinen), jotta ne ovat helposti löydettävissä, ja antaa jokaiselle merkinnälle henkilökohtaisen kuvakkeen. Mukana on myös hakupalkki, jonka avulla voit etsiä palvelua tai tiliä heti nimen perusteella.



**Salatut paikalliset varmuuskopiot:** Varmistaaksesi, ettet koskaan menetä pääsyäsi tileihisi, Aegis tarjoaa automaattisia varmuuskopioita kassakaapistasi. Nämä ovat salattuja (salasanan avulla), ja ne voidaan tallentaa haluamaasi paikkaan (sisäinen tallennustila, pilvikansio jne.). Sovellus voi myös viedä tilitietokantasi manuaalisesti tarpeen mukaan salatussa tai salaamattomassa muodossa. Tilien tuonti muista 2FA-sovelluksista on yhtä helppoa (Aegis tukee tuontia Authy-, Google Authenticator-, FreeOTP-, andOTP- jne. sovelluksista).



**Turvallisuus ja yksityisyys:** sovellus on oletusarvoisesti täysin offline-tilassa. Se ei vaadi verkko-oikeuksia - mikä tarkoittaa, että se ei lähetä tietoja ulkomaailmaan, eikä siinä ole mainosseurantalaitteita tai käyttäytymisanalyysimoduuleja. Aegis ei näytä mainoksia, eikä vaadi käyttäjätiliä: heti kun se on asennettu, se toimii ilman rekisteröitymistä. Koska sen lähdekoodi on julkista GitHubissa, yhteisö voi tarkastaa sen vapaasti ja taata, ettei siinä ole haitallisia tai piilotettuja toimintoja.



**Moderni Interface:** Aegis käyttää siistiä Material Designia, jossa on tuki tummille teemoille (mukaan lukien AMOLED-tila) ja jopa valinnainen laattanäkymä, joka näyttää koodisi ruudukkoina. Interface on pelkistetty, ilman hienouksia, ja se estää koodien ruudunkaappauksen turvatoimenpiteenä.



## Asennus



Koska Aegis Authenticator on avointa lähdekoodia, sen kehittäjät suosivat yksityisyyden suojaa suosivia jakelukanavia. Se voidaan asentaa kahdella tavalla:



### Via F-Droid (suositellaan)



Turvallisin ja helpoin tapa on F-Droid, ilmainen vaihtoehtoinen kauppa. Jos F-Droidia ei ole vielä asennettu puhelimeesi, aloita lataamalla se viralliselta verkkosivustolta [F-Droid.org](https://f-droid.org). Sitten :





- Avaa F-Droid ja varmista, että olet päivittänyt arkistot uusimman sovellusluettelon saamiseksi
- Etsi "Aegis Authenticator" F-Droidista. Virallisen sovelluksen pitäisi ilmestyä (julkaisija: Beem Development)
- Aloita asennus painamalla Asenna. Koska Aegis on yksi F-Droidin varmentamista sovelluksista, saat luotettavan ja turvallisen latauksen



Asennus F-Droidin kautta tarjoaa sen edun, että saat automaattiset sovelluspäivitykset heti, kun ne julkaistaan. Lisäksi F-Droid takaa, että sovellus ei sisällä ei-toivottuja omia komponentteja.



### Via GitHub (allekirjoitettu APK)



Jos asennat sovelluksen mieluummin ilman kauppoja, voit ladata virallisen APK:n suoraan projektin GitHub-sivulta. Siirry Aegis-repositoriossa ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)) kohtaan Releases, jossa julkaistaan vakaat versiot.





- Lataa uusin APK-versio
- Varmista ennen APK:n asentamista, että olet sallinut tuntemattomista lähteistä tulevien sovellusten asentamisen laitteellasi (Androidin asetuksissa)
- Kehittäjä on allekirjoittanut GitHubissa olevan APK:n samalla avaimella kuin F-Droidissa



Manuaalisen asennuksen jälkeen sovellus toimii identtisesti. Huomaa, että päivitykset eivät ole automaattisia: sinun on tarkistettava GitHubista säännöllisesti uudet versiot.



### Google Play Store vs. F-Droid



Aegis Authenticator on saatavilla sekä Google Play Storessa että F-Droidissa, joten voit valita asennustavan:



**Google Play Store:**




- ✅ Android-järjestelmään integroidut automaattiset päivitykset
- ✅ Yksinkertainen, tuttu asennus
- ✅ Sama allekirjoitettu APK kuin muilla kanavilla



**F-Droid (suositellaan) :**




- ✅ Ilmainen ja avoimen lähdekoodin myymälä
- ✅ Toistettavissa ja todennettavissa oleva rakenne
- ✅ Google-palvelua ei tarvita
- ✅ Kunnioitus vapaiden ohjelmistojen filosofiaa kohtaan



Valinta näiden kahden vaihtoehdon välillä riippuu mieltymyksistäsi Googlen ekosysteemin suhteen. Jos pidät yksinkertaisuudesta, Play Store on ihanteellinen. Jos haluat yksityisyydensuojan, joka on riippumaton Googlen palveluista, F-Droid on parempi valinta.



## Ensimmäinen kokoonpano



Kun Aegis käynnistetään ensimmäistä kertaa, 2FA-koodin suojaamiseksi ehdotetaan alustavaa konfigurointimenettelyä:



![Configuration initiale Aegis](assets/fr/01.webp)



*Aegis-konfiguroinnin alkuprosessi: tervetulonäyttö, turvavalinnat, pääsalasanan määrittely ja viimeistely*



### Aseta pääsalasana



Aegis pyytää sinua ensin valitsemaan pääsalasanan. Tätä salasanaa käytetään kaikkien holviin tallennettujen tunnisteiden salaamiseen. Suosittelemme, että asetat vahvan ja ainutlaatuisen salasanan, jonka vain sinä tiedät.



**⚠️ Varoitus:** Älä unohda tätä salasanaa - jos kadotat sen, salatut 2FA-koodisi eivät ole enää käytettävissä (takaovea ei ole). Aegis pyytää sinua syöttämään salasanan kahdesti vahvistukseksi.



### Ota käyttöön biometrinen lukituksen avaus (valinnainen)



Jos Android-laitteessasi on sormenjälkilukija tai muu biometrinen tunnistin, Aegis pyytää sinua aktivoimaan biometrisen lukituksen avaamisen. Tämä vaihtoehto on valinnainen mutta erittäin käytännöllinen: sen avulla voit avata sovelluksen lukituksen nopeasti sormenjäljelläsi tai kasvoillasi sen sijaan, että kirjoittaisit salasanan joka kerta.



Huomaa, että biometriset tunnukset ovat lisäpalvelu: pääsalasana tarvitaan edelleen, jos biometrisiä tunnuksia muutetaan tai laite käynnistetään uudelleen.



### Tutustu sovellusasetuksiin



Kun olet päässyt sovelluksen sisään (Interface:n pääikkuna on aluksi tyhjä), tutustu käytettävissä oleviin määritysvaihtoehtoihin. Pääset asetuksiin näytön oikeassa yläkulmassa olevan pudotusvalikon kautta (kolme pystysuoraa pistettä) ja valitse sitten "Settings".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface Aegis-pääkäyttäjä tyhjä alussa, pääsy parametrien valikkoon ja yleiskatsaus käytettävissä oleviin vaihtoehtoihin*



Aegisin asetusvalikossa on useita tärkeitä osioita:





- Ulkonäkö**: Mukauta teemaa (vaalea, tumma, AMOLED), kieltä ja muita visuaalisia asetuksia
- Käyttäytyminen**: Määritä sovelluksen käyttäytyminen, kun se on vuorovaikutuksessa merkintäluettelon kanssa
- Kuvakepaketit**: hallinnoi ja tuo kuvakepaketteja tiliesi ulkoasun mukauttamiseksi
- Turvallisuus**: Salauksen, biometrisen lukituksen avaamisen, automaattisen lukituksen ja muiden turvallisuusparametrien asetukset
- Varmuuskopiot**: Määritä automaattiset varmuuskopiot haluamaasi paikkaan
- Tuonti ja vienti**: Tuo varmuuskopiot muista todennussovelluksista ja vie Aegis-holvisi manuaalisesti
- Tarkastusloki**: Yksityiskohtainen loki kaikista sovelluksen merkittävistä tapahtumista



Tämän selkeän organisaation avulla voit määrittää Aegisin mieltymystesi ja turvallisuustarpeidesi mukaan.



## Lisää 2FA-tili



Kun Aegis on konfiguroitu, siirrytään olennaisiin asioihin: kaksitekijätilien lisäämiseen. Prosessi on yksinkertainen, ja Aegis tarjoaa useita menetelmiä tunnuskoodien integroimiseksi.



### Kolme käytettävissä olevaa lisäysmenetelmää



Paina Aegis Interface:n pääikkunassa oikeassa alakulmassa olevaa **+**-painiketta, jolloin pääset lisäysvaihtoehtoihin. Sinulla on kolme vaihtoehtoa:





- Skannaa QR-koodi**: Skannaa suoraan verkkopalvelun näyttämä QR-koodi
- Skannaa kuva**: Skannaa QR-koodi laitteeseen tallennetusta kuvasta
- Syötä manuaalisesti**: Syötä 2FA-tilin tiedot manuaalisesti



### Käytännön esimerkki: Bitwardenin konfigurointi



Otetaan konkreettinen esimerkki 2FA:n aktivoinnista Bitwardenissa prosessin havainnollistamiseksi:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Esimerkki 2FA:n aktivoinnista Bitwardenissa: Interface-verkkopalvelu todennusvaihtoehtojen ja Aegis-suosituksen* kanssa





- Kirjautuminen sisään ja asetusten käyttäminen**: Kirjaudu sisään Bitwarden-tilillesi ja avaa asetukset, "Turvallisuus"-välilehti
- Palveluntarjoajia koskeva osa**: Siirry "Providers"-osioon ja napsauta "Manage" (Hallitse) "Authenticator app"-osiossa



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Täydellinen prosessi tilin lisäämiseksi: Palvelun näyttämä QR-koodi, salainen avain näkyvissä ja vahvistuskoodi syötetty*





- Skannaa QR-koodi**: Avautuu ponnahdusikkuna, jossa on QR-koodi ja salainen avain
- Aegiksessa**: Käytä "Skannaa QR-koodi" tietojen automaattiseen keräämiseen
- Tarkastus**: Syötä Aegisin luoma 6-numeroinen koodi kenttään "Verification code"
- Aktivointi**: Napsauta "Ota käyttöön" aktivoinnin viimeistelemiseksi



### Lisää tiedot manuaalisesti



Jos haluat tai et pysty skannaamaan QR-koodia, käytä vaihtoehtoa "Syötä manuaalisesti". Lomakkeella voit syöttää :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Uuden 2FA-tilin lisääminen: tyhjä Interface, lisäysvaihtoehdot, manuaalinen syöttölomake ja tili lisätty onnistuneesti*





- Nimi** : Palvelun nimi (esim. Bitwarden, GitHub...)
- Liikkeeseenlaskija** : Liikkeeseenlaskija (usein sama kuin nimi)
- Ryhmä**: Valinnainen, tilien järjestäminen luokittain
- Huomautus** : Henkilökohtaisia huomautuksia tästä tilistä
- Salaisuus** : Palvelun toimittama salainen avain (oletusarvoisesti peitetty)
- Edistyneet**: Lisäparametrit (algoritmi, jakso, numeroiden määrä)



Kun tili on lisätty, se näkyy luettelossasi nykyisellä koodilla ja aikaindikaattorilla, joka näyttää jäljellä olevan ajan ennen uusimista.



### Yleinen yhteensopivuus



Aegis on yhteensopiva kaikkien TOTP- ja HOTP-standardeja käyttävien palveluiden kanssa, mukaan lukien lähes kaikki 2FA:ta tarjoavat sivustot: sosiaaliset verkostot, pankit, salasanahallintajärjestelmät, kryptoalustat jne.



### Sisäänkäynnin järjestäminen



Kun olet lisännyt useita tilejä, arvostat Aegisin organisointityökaluja:





- Mukautettu lajittelu:** Oletusarvoisesti tilit luetellaan aakkosjärjestyksessä, mutta voit muuttaa järjestystä manuaalisesti
- Ryhmät ja luokat:** Luo ryhmiä, joilla erotat henkilökohtaiset tilisi yritystileistäsi, tai ryhmittele ne palvelutyypin mukaan (pankki, sähköposti, sosiaaliset verkostot jne.)
- Mukautetut kuvakkeet:** Aegis yrittää määrittää automaattisesti sopivan kuvakkeen, jos sellainen on saatavilla, muuten voit valita monista yleisistä kuvakkeista tai tuoda kuvan
- Pikahaku:** Yläreunassa olevan hakupalkin avulla voit kirjoittaa muutaman kirjaimen ja suodattaa vastaavia merkintöjä välittömästi



Kun kosketat merkintää, OTP-koodi näytetään täysikokoisena (jos se oli piilotettu) ja voit kopioida sen leikepöydälle pitkällä painalluksella - kätevää, kun haluat liittää sen sovellukseen, johon haluat muodostaa yhteyden.



## Turvallisuus ja varmuuskopiot



Koska turvallisuus on Aegisin ydin, on tärkeää ymmärtää, miten 2FA-koodit suojataan ja miten niiden pysyvyys varmistetaan ongelmatilanteissa.



### Turvallisuusarkkitehtuuri



**Turvallinen salaus**: Kaikki koodit tallennetaan salattuun kassakaappiin käyttäen **AES-256-algoritmia GCM-tilassa**, yhdistettynä pääsalasanasi. Avainten johtaminen perustuu **scrypt**-menetelmään, joka tarjoaa paremman suojan brute-force-hyökkäyksiä vastaan.



**Turvallinen lukituksen avaaminen** : Pääsalasana tarvitaan tietojen salauksen purkamiseen. Biometria (valinnainen) käyttää **Android Secure Keystore**:a ja TEE:tä (Trusted Execution Environment) salausavaimen suojaamiseen.



**Minimaaliset oikeudet**: Aegis toimii oletusarvoisesti offline-tilassa ja vaatii vain pääsyn kameraan (QR-skannaus), biometriikkaan ja vibraattoriin. Mitään tietoja ei kerätä tai jaeta.



### Varmuuskopiointivaihtoehdot



Aegis tarjoaa useita varmuuskopiointistrategioita, jotka sopivat erilaisiin turvallisuus- ja mukavuustarpeisiin:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface sisältää lisätyn tilin, varmuuskopiointihälytyksen, automaattiset varmuuskopiointiasetukset ja varmuuskopiointistrategiat*



**1. Automaattiset paikalliset varmuuskopiot**




- Määritä haluamasi kohdekansio
- Mukautettava taajuus (jokaisen muutoksen jälkeen, päivittäin jne.)
- Salasanalla suojatut salatut tiedostot (.aesvault)
- Yhteensopiva synkronoitujen kansioiden kanssa (Nextcloud, Dropbox jne.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Varmuuskopiointikansioiden valintaprosessi: tiedostoetsintä, kohdekansio ja käyttöoikeus*



**2. Android** pilvivarmistukset




- Valinnainen integrointi Android-varmistusjärjestelmään
- Käytettävissä vain salattuihin kassakaappeihin (turvallisuus säilytetty)
- Läpinäkyvä varmuuskopiointi muiden Android-tietojen kanssa
- Automaattinen palautus laitteen vaihtuessa



**3. Manuaalinen** vienti




- Vienti pyynnöstä **Asetukset > Tuo ja vie** kautta
- Valinta salatun (suositellaan) tai selkeän muodon välillä
- Hyödyllinen migraatioita tai satunnaisia varmuuskopioita varten



### Hyvät turvallisuuskäytännöt





- Pidä useita varmuuskopioita** korruption estämiseksi
- Testaa** varmuuskopiot säännöllisesti yrittämällä palauttamista
- Säilytä palvelun antamat palautuskoodit erillään**
- Pääsalasanasi** tarvitaan edelleen myös pilvivarmistusten yhteydessä
- Suojaa pääsalasanasi**: käytä ainutlaatuista, vahvaa salasanaa, joka on tallennettu salasanahallintaohjelmaan
- Pidä sovelluksesi ajan tasalla** uusimpien tietoturvakorjausten kanssa
- Ota automaattinen lukitus** käyttöön asetuksissa, jotta sovelluksen käyttö on turvallista
- Poista kuvakaappaukset käytöstä** (oletusvaihtoehto) estääksesi koodiesi salakuuntelun
- Käytä biometriikkaa säästeliäästi**: suosi salasanoja kriittisiin käyttöoikeuksiin



## Vertailu muihin sovelluksiin



Miten Aegis pärjää muille suosituille todennussovelluksille?



### Aegis vs. Google Authenticator



**Aegis :**




- ✅ Avoin lähdekoodi ja tarkastettavissa
- ✅ Paikallinen salattu varmuuskopiointi
- ✅ Kehittynyt organisaatio (ryhmät, kuvakkeet, haku)
- ✅ Ei tiedonkeruuta
- ❌ Vain Android



**Google Authenticator :**




- ✅ Saatavilla Androidissa ja iOS:ssä
- ✅ Pilvisynkronointi (vuodesta 2023)
- ❌ Suljettu lähdekoodi
- ❌ Rajoitettu toiminnallisuus
- ❌ Mahdollinen Googlen tiedonkeruu



### Aegis vs. Authy



**Aegis :**




- ✅ Avoin lähdekoodi
- ✅ Tiliä ei tarvita
- ✅ Koodin vienti mahdollista
- ✅ Tietojen kokonaisvalvonta
- ❌ Ei natiivia monilaitesynkronointia



**Authy :**




- ✅ Monen laitteen synkronointi
- ✅ Saatavilla Androidissa ja iOS:ssä
- ❌ Suljettu lähdekoodi
- ❌ Vaatii puhelinnumeron
- ❌ Koodien vienti ei onnistu
- ❌ Työpöytäsovellukset poistetaan maaliskuussa 2024



Aegis sopii erinomaisesti Android-käyttäjille, jotka arvostavat läpinäkyvyyttä, paikallista tietoturvaa ja tietojensa täydellistä hallintaa. Authyn kaltaiset vaihtoehdot sopivat paremmin, jos tarvitset ehdottomasti automaattista usean laitteen synkronointia.




## Päätelmä



Aegis Authenticator on erinomainen ratkaisu niille, jotka etsivät yksityisyyttä suojaavaa, turvallista ja läpinäkyvää 2FA-sovellusta. Avoimen lähdekoodin lähestymistapa yhdistettynä vankkaan salaukseen ja siistiin Interface:ään tekee siitä ensiluokkaisen valinnan verkkotilien suojaamiseen.



Vaikka Aegis rajoittuu Androidiin ja siitä puuttuu natiivipilvisynkronointi, se korvaa nämä rajoitukset "Privacy by design" -filosofiallaan ja täydellisellä tietojen hallinnalla. Digitaalisesta yksityisyydestään huolestuneille käyttäjille Aegis tarjoaa uskottavan ja tehokkaan vaihtoehdon markkinoilla vallitseville omille ratkaisuille.



Verkkotilisi turvallisuuden ei tarvitse olla riippuvainen kaupallisten yritysten hyvästä tahdosta. Aegisin avulla pidät tunnuskoodit hallussasi digitaalisessa kassakaapissa, jonka avain on vain sinulla.



## Resurssit



### Viralliset verkkosivustot




- Virallinen verkkosivusto**: [getaegis.app](https://getaegis.app/) - Hakemuksen esittely ja lataus
- Lähdekoodi**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Virallinen GitHub-tietovarasto
- F-Droid** : [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Asennus ilmaisen kaupan kautta



### Tekninen dokumentaatio




- Holvin dokumentaatio**: [Holvin suunnittelu](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Tekninen kuvaus salauksesta ja turvallisesta arkkitehtuurista
- Virallinen FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Vastauksia usein kysyttyihin kysymyksiin
- Projekti wiki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Täydellinen käyttäjädokumentaatio