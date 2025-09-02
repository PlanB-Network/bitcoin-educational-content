---
name: LibreWolf
description: LibreWolf-yksityisyysselaimen käyttö
---

![cover](assets/cover.webp)



Jokainen klikkaus, jokainen haku, jokainen vierailtu sivusto: selaimestasi on tullut kehittynyt vasikka, joka syöttää maailmanlaajuista kaupallista valvontajärjestelmää. Google Chrome, jota käyttää yli 3 miljardia ihmistä, muuttaa päivittäisen selaamisesi tuottoisiksi tiedoiksi mainosjätille. Jopa Firefox, vaikka se on "eettisen" selaimen maineessa, aktivoi oletusarvoisesti telemetriamekanismit, jotka välittävät selaustottumuksesi Mozillalle.



Tämä todellisuus herättää olennaisen kysymyksen: onko edelleen mahdollista selata vapaasti Internetiä ilman jatkuvaa vakoilua ja profilointia? Onneksi vastaus on kyllä, kiitos yhteisöprojektien, jotka asettavat käyttäjän takaisin keskiöön.



LibreWolf ilmentää tätä digitaalisen vastarinnan filosofiaa. Riippumattomien kehittäjien yhteisön ideoima selain muuttaa Firefoxin todelliseksi kilveksi verkkovalvontaa vastaan. Siinä missä kaupalliset selaimet pyrkivät hyödyntämään huomiosi rahaksi, LibreWolf tekee päinvastoin: se tekee sinusta näkymättömän jäljittäjille ja säilyttää samalla sujuvan ja modernin selauskokemuksen.



Tässä opetusohjelmassa selvitämme, miten LibreWolf voi muuttaa tapasi surffailla verkossa ja tarjota vankan suojan seurantaa vastaan suorituskykyä tai verkkoyhteensopivuutta uhraamatta.



![LIBREWOLF](assets/fr/01.webp)


*Web-selaimen markkinaosuus: Chrome hallitsee 65 prosentin markkinaosuudella, ja sen jälkeen tulevat Safari ja Edge. Tämä valta-asema herättää kysymyksiä verkon monimuotoisuudesta ja yksityisyydestä*



## Esittelyssä LibreWolf



**FreeWolf** on Mozilla Firefoxista johdettu avoimen lähdekoodin verkkoselain, jota kehittää ja ylläpitää vapaiden ohjelmistojen harrastajien riippumaton yhteisö. Sen päätavoitteena on tarjota selausta, jossa keskitytään käyttäjän yksityisyyteen, turvallisuuteen ja vapauteen.



Konkreettisesti LibreWolf käyttää Firefoxin Gecko-moottoria, mutta sen filosofia on täysin erilainen: siinä missä Firefoxin on tasapainotettava yksityisyyden suoja ja helppokäyttöisyys, LibreWolf valitsee yksityisyyden suojan oletuksena. Projekti poistaa kaiken, mikä saattaa loukata yksityisyyttäsi (telemetria, tiedonkeruu, sponsoroidut moduulit) ja integroi samalla parannetut tietoturva-asetukset.



### Tavoitteet: yksityisyys ja vapaus



LibreWolf pyrkii maksimoimaan suojan seurantaa ja sormenjälkien ottamista vastaan ja parantamaan samalla selaimen turvallisuutta. Sen päätavoitteet ovat seuraavat:





- Poista kaikki telemetria ja tiedonkeruu** Firefoxista
- Poista käytöstä toiminnot, jotka ovat käyttäjän vapauden** vastaisia, kuten omat DRM-moduulit
- Käytä yksityisyys-/turva-asetuksia** ja erityisiä korjauksia alusta alkaen
- Yhteisön kehitys takaa avoimuuden ja riippumattomuuden** kaupallisista intresseistä



Lyhyesti sanottuna LibreWolf esittelee itsensä "Firefoxina, jollainen se olisi ollut, jos yksityisyys olisi ollut etusijalla" - selaimena, joka kunnioittaa sinua oletusarvoisesti ilman lisäkonfiguraatioita.



### Tärkeimmät ominaisuudet



LibreWolf tarjoaa heti alusta alkaen useita yksityisyyteen tähtääviä ominaisuuksia:



**Ei telemetriaa tai tiedonkeruuta:** Toisin kuin Chrome tai Firefox, jotka lähettävät tiettyjä käyttötilastoja, LibreWolf ei kerää mitään tietoja selaamisestasi. Ei kaatumisraportteja, ei käyttäjätutkimuksia, ei sponsoroituja ehdotuksia.



**LibreWolf integroi natiivisti uBlock Origin -laajennuksen, joka on yksi markkinoiden parhaista mainosten esto- ja seurantaohjelmista. Oletusarvoisesti LibreWolf suodattaa aggressiivisesti kaiken, mikä saattaa seurata sinua verkossa (tungettelevat mainokset, seurantaskriptit, kryptovaluutta Mining).



**Esimerkkihakukone oletusarvoisesti:** LibreWolf käyttää oletusarvoisesti DuckDuckGoa alkuperäisenä hakukoneena, joka ei säilytä hakuhistoriaa. Saatavilla on myös muita yksityisyyteen suuntautuneita vaihtoehtoja (Searx, Qwant, Whoogle).



**Vahvistettu sormenjälkien vastainen suojaus:** Sormenjälkien avulla selain voidaan tunnistaa yksiselitteisesti sen kokoonpanon perusteella, jopa ilman evästeitä. Tätä vastaan LibreWolf aktivoi Tor-projektin RFP-teknologian (Resist Fingerprinting), jotta selaimesi olisi mahdollisimman yleinen. Testit osoittavat, että tavallinen Firefox on ~90 % yksilöllinen työkaluissa, kuten coveryourtracks.eff.org, verrattuna vain ~10-20 %:iin LibreWolfissa (nämä luvut ovat suuntaa-antavia ja voivat vaihdella ohjelmisto- ja laitteistokokoonpanon ja asennettujen laajennusten mukaan).



![LIBREWOLF](assets/fr/07.webp)


*EFF-testisivu [Cover Your Tracks](https://coveryourtracks.eff.org/) TEST YOUR BROWSER -painikkeella. Tätä sivua käytetään suojauksen arviointiin jäljittäjiä ja sormenjälkiä vastaan



![LIBREWOLF](assets/fr/08.webp)


*Cover Your Tracks -testin tulos. Näyttöön tulee viesti "sinulla on vahva suojaus verkkoseurantaa vastaan", mikä osoittaa LibreWolf.*-suojan tehokkuuden



**LibreWolf aktivoi tiukat suojausasetukset oletusarvoisesti. Firefoxin Enhanced Tracking Protection on nostettu Strict-tasolle estämään tuhansia jäljittäjiä, kolmannen osapuolen evästeitä ja haitallista sisältöä. Se aktivoi myös sivuston ja evästeiden eristämisen (*Total Cookie Protection*), jotta tiedot voidaan jakaa jokaiseen verkkotunnukseen, ja rajoittaa WebRTC:tä (rajoittamalla *ICE-ehdokkaita* ja reitittämällä välityspalvelimen kautta, kun välityspalvelin on käytössä) IP Address -vuodon riskin vähentämiseksi.



**Nopeat moottoripäivitykset:** Projekti seuraa Firefoxin kehitystä hyvin tarkasti: LibreWolf perustuu aina Firefoxin viimeisimpään vakaaseen versioon, ja ylläpitäjät pyrkivät julkaisemaan uuden version 24-72 tunnin sisällä jokaisesta virallisesta Firefox-julkaisusta.



## Edut ja haitat



### Edut





- Ei telemetriaa tai ei-toivottuja yhteyksiä:** LibreWolf ei lähetä käyttötietoja, mikä takaa yksityisyytesi täydellisen kunnioittamisen.





- Avoin lähdekoodi ja yhteisöllisyys:** Hanke on 100-prosenttisesti avointa lähdekoodia, ja sitä ylläpitävät vapaaehtoiset. Tämä riippumattomuus takaa, että mikään mainosmalli ei vaikuta kehitykseen.





- Ennalta määritetty yksityisyyden suojaa varten:** LibreWolf säästää arvokasta aikaa: sinun ei tarvitse käyttää tunteja Firefoxin asetusten koventamiseen, kaikki on jo tehty.





- Oma mainosten esto/seuranta:** uBlock Origin on integroitu vakiona, joten sinun ei tarvitse tehdä mitään suojellaksesi itseäsi mainoksilta ja virheiltä.





- Erinomainen sormenjälkien vastainen suojaus:** RFP:n ja lukuisten yksityisyysasetusten ansiosta LibreWolf vähentää merkittävästi digitaalista jalanjälkeäsi verkossa.





- Parempi suorituskyky ja keveys:** Poistamalla telemetria ja tietyt epäolennaiset ominaisuudet LibreWolf voi olla hieman nopeampi ja vähemmän virtaa kuluttava kuin tavallinen Firefox.



### Haitat ja rajoitukset





- Ei sisäänrakennettuja automaattisia päivityksiä:** LibreWolf ei päivitä itseään. Sinun on asennettava uudet versiot heti, kun ne julkaistaan, pysyäksesi turvassa.





- Yhteensopivuuden heikkeneminen tiettyjen palveluiden kanssa:** LibreWolfin erittäin tiukkojen asetusten vuoksi LibreWolf voi kohdata ongelmia tietyillä verkkosivustoilla. Netflix- ja Disney+-suoratoistoalustat eivät toimi, koska LibreWolf poistaa Widevine DRM:n oletusarvoisesti käytöstä.





- Ei sisäänrakennettua anonyymiä verkkoa:** Toisin kuin Tor Browser, LibreWolf ei itse reititä liikennettä Torin tai VPN:n kautta. Jos tarvitset verkon anonymiteettiä, sinun on määritettävä välityspalvelin/VPN manuaalisesti.





- Ei-pysyvät evästeet ja istunnot (oletus):** Luottamuksellisuussyistä LibreWolf poistaa evästeet, historiatiedot ja sivuston tiedot aina, kun suljet selaimesi. Sinun on kirjauduttava tilillesi uudelleen joka kerta, kun kirjaudut sisään.





- Ei mobiiliversiota tai pilvisynkronointia:** LibreWolf on saatavilla vain työpöydällä (Windows, Linux, macOS). Mobiilisovellusta ei ole, eikä näin ollen myöskään tilien tai kirjanmerkkien synkronointia pilven kautta.



## LibreWolfin asentaminen



**Official website:** [librewolf.net](https://librewolf.net)



LibreWolf on saatavilla kaikille yleisimmille työpöytäkäyttöjärjestelmille: Linux, Windows ja macOS. Voit ladata LibreWolfin virallisilta verkkosivuilta:



![LIBREWOLF](assets/fr/02.webp)


*LibreWolfin etusivu (librewolf.net), jossa näkyy selaimen logo, sininen Asenna-painike sekä lähdekoodi- ja dokumentaatiolinkit. Suuri sininen nuoli osoittaa Asenna-painikkeeseen*



Napsauta "Asennus"-painiketta saadaksesi yksityiskohtaiset ohjeet käyttöjärjestelmääsi varten:



![LIBREWOLF](assets/fr/03.webp)


*Käyttöjärjestelmän valintasivu LibreWolf.* latausta varten



Asennus vaihtelee käyttöjärjestelmästä riippuen:



### Linuxissa


LibreWolf tarjoaa rakennelmia monille jakeluille. Debian/Ubuntussa ja johdannaisissa on saatavilla virallinen APT-tietovarasto. Vaihtoehtoisesti LibreWolf julkaistaan Flatpak-versiona Flathubissa:


```
flatpak install flathub io.gitlab.librewolf-community
```



### Windowsissa


Lataa asennusohjelma (.exe) viralliselta verkkosivustolta tai käytä:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### MacOS:ssä


LibreWolf on saatavilla .dmg-pakettina Macille. Lataa levykuva viralliselta verkkosivustolta ja vedä LibreWolf-sovellus Applications-kansioon. Vaihtoehtoisesti voit asentaa sen Homebrew:n kautta.




## Konfigurointi ja ensimmäinen käyttö



Ensimmäisellä käynnistyskerralla huomaat tutun Firefox Interface:n, paitsi että se on pelkistetympi: etusivulla on vain hakupalkki eikä sponsoroituja ehdotuksia. Työkalurivillä näkyy uBlock Origin -kuvake - merkki siitä, että esto on aktiivinen.



![LIBREWOLF](assets/fr/04.webp)


*LibreWolfin etusivu laajennuksineen ja valikkoineen. Sininen nuoli oikeassa yläkulmassa osoittaa valikkokuvakkeen (kolme vaakapalkkia)



LibreWolf lataa sivusi automaattisesti "strict"-tilassa (jäljittämisen vastaisessa tilassa), ja oletushakukoneeksi tulee DuckDuckGo. Voit kokeilla vierailla seurantaan liittyvällä testisivustolla (esim. amiunique.org) tarkkaillaksesi näkyvää jalanjälkeä - sen pitäisi olla paljon yleisempi kuin tavallisella selaimella.



### Yksityisyysasetukset



LibreWolf on jo valmiiksi optimaalisesti konfiguroitu yksityisyyden suojaamiseksi. Valikko → Asetukset → Yksityisyys ja turvallisuus -kohdassa näet, että LibreWolf on asetettu Enhanced Tracking Protection -tilaan: Strict. Tämä tila estää:




- Sivustojen väliset seurantalaitteet
- Kolmannen osapuolen evästeet
- Tunnettu seurantasisältö
- Cryptomining
- Digitaaliset sormenjälkitunnistimet



![LIBREWOLF](assets/fr/05.webp)


*Turvallisuus ja yksityisyys -välilehti, jossa näkyvät LibreWolf.*:n suojausasetukset



WebRTC on poistettu käytöstä (estää IP-vuodot), ja Total Cookie Protection on käytössä. Telemetria ja Firefox-kyselyt on poistettu kokonaan käytöstä.



### Evästeiden ja historian hallinta



Oletusarvoisesti LibreWolf poistaa evästeet ja paikallisen tallennustilan aina, kun se suljetaan. Jos tämä käyttäytyminen häiritsee sinua, voit säätää sitä kohdassa Tietosuoja ja turvallisuus → Evästeet ja sivuston tiedot poistamalla valinnan "Poista evästeet ja sivuston tiedot LibreWolfia suljettaessa".



![LIBREWOLF](assets/fr/06.webp)


*Sama sivu hieman alempana, jossa näkyy vaihtoehto evästeiden poistamiseksi selaimen sulkemisen yhteydessä*



### Hyödyllisten laajennusten lisääminen



Periaatteessa LibreWolf ei suosittele tarpeettomien laajennusten lisäämistä, koska jokainen laajennus voi olla seurantavektori. Jotkut hyvämaineiset laajennukset voivat kuitenkin parantaa käyttökokemustasi:




- Firefox Multi-Account Containers** (Mozilla) lokeroituun selaamiseen
- Decentraleyes** tai **LocalCDN** palvelemaan yhteisiä kirjastoja paikallisesti



Vältä erityisesti "ilmaisia VPN-laajennuksia" tai epäilyttäviä välityspalvelimia - uBlock Origin kattaa jo 99 % tarpeistasi.



## Jokapäiväinen käyttö



### Päivittäinen verkkoselailu


Käytä LibreWolfia päivittäiseen Internet-toimintaasi. Suurin ero muihin selaimiin verrattuna on se, että jätät paljon vähemmän mainosjälkiä. Hyväksy evästeet" -bannerit katoavat monilta sivustoilta uBlockin suodatuslistojen ansiosta.



### Käytä yksityisiä välilehtiä lokerointiin


Vaikka LibreWolf poistaa kaiken istunnon lopussa, voi olla hyödyllistä avata yksityinen selainikkuna (Ctrl+Shift+P) tiettyjä tehtäviä varten istunnon aikana, jotta voit eristää tietyn identiteetin.



### Hyödynnä usean tilin kontteja


Multi-Account Containers -laajennuksen asentaminen voi auttaa sinua segmentoimaan toimintosi vesitiiviisiin siiloihin. Voit esimerkiksi määritellä "Banking"-kontin pankkisivustoillesi, "Social Networks"-kontin Facebookille/Twitterille jne. Jokaisella kontilla on omat evästeet, istunnot ja eristetty tallennus. Jokaisella säiliöllä on omat evästeet, istunnot ja eristetty tallennus.



### Hienosäädetty käyttöoikeuksien hallinta sivustoittain


LibreWolfin avulla voit hallita sivustoille antamiasi käyttöoikeuksia (sijainti, kamera, mikrofoni, ilmoitukset) tapauskohtaisesti. Myönnä käyttöoikeuksia vain sivustoille, joihin luotat, ja vain tarvittaessa.



## Parhaat käytännöt LibreWolfin kanssa



1. **Pitäkää LibreWolf ajan tasalla:** Tarkistakaa sivustolta säännöllisesti uudet versiot, erityisesti Firefoxin vakaan julkaisun jälkeen.



2. **Vältä henkilökohtaisen identiteetin ja yksityisen selailun sekoittamista:** Ihannetapauksessa sinun ei pitäisi kirjautua henkilökohtaisilla tileilläsi samaan istuntoon, jossa teet arkaluonteista tutkimusta.



3. **Älä ylikuormita LibreWolfia turhilla laajennuksilla:** Jokainen asentamasi laajennus voi aiheuttaa tietoturva- tai sormenjälkiriskejä.



4. **Käytä lisäksi VPN:ää tai Tor-välityspalvelinta:** LibreWolf ei tee sinusta anonyymiä Internet-palveluntarjoajallesi. Verkon anonymiteettiä varten voit käyttää LibreWolfia luotettavan VPN:n takana.



5. **Tallenna tärkeät tietosi:** Kirjanmerkit, salasanat, jos ne on tallennettu paikallisesti. Harkitse ulkoista salasanahallintaohjelmaa (KeePassXC, Bitwarden) selaimen perussalasanahallintaohjelman sijaan.



## Vertailu muihin selaimiin



LibreWolf on osa yksityisyyteen suuntautuneiden selainten "työkalupakkia":



**LibreWolf vs. Firefox:** LibreWolf saapuu jo valmiiksi kovetettuna ja ilman telemetriaa. Firefox säilyttää usean laitteen synkronoinnin ja erittäin suuren käyttäjäkunnan edut, mutta vaatii manuaalista konfigurointia Librewolfin luottamuksellisuuden tason saavuttamiseksi.



**Brave käyttää Chrome/Chromium-koodia ja integroi liiketoimintamallin valinnaisen mainosohjelman kautta. LibreWolf, joka on yhteisön Fork Firefoxille, säilyttää Mozillan vapaan ekosysteemin eikä sillä ole siteitä Googleen.



**LibreWolf vs. Tor Browser:** Tor Browser on korvaamaton anonymiteetin säilyttämiseksi tehokkaan valvonnan edessä, mutta se on hidas ja epämukava jokapäiväisessä käytössä. LibreWolf on paljon nopeampi ja käytännöllisempi klassisen webin jokapäiväiseen selaamiseen.



**LibreWolf vs. Mullvad Browser:** Mullvad Browser menee vielä pidemmälle standardisoinnissa, mutta sen hinnaksi jää huonompi käytettävyys (kirjautumisevästeen säilyttäminen on mahdotonta). LibreWolf löytää tasapainon: hyvin yksityinen, mutta käyttökelpoinen päivittäin.



## Päätelmä



LibreWolf on erinomainen ratkaisu niille, jotka etsivät erittäin yksityistä "arkipäivän" selainta menemättä kuitenkaan niin pitkälle kuin Torin äärimmäinen anonymiteetti. Se on ihanteellinen valinta aktivisteille, toimittajille, kehittäjille tai tehokäyttäjille, jotka haluavat klassista verkkoselausta (nopeaa, yhteensopivaa nykyaikaisten sivustojen kanssa) ja samalla välttyä mainosten seurannalta ja Big Techiltä.



Vaikka sillä on tiettyjä rajoituksia (ei automaattisia päivityksiä, heikentynyt yhteensopivuus tiettyjen palveluiden kanssa), LibreWolf on arvokas työkalu kaikille, jotka haluavat saada digitaalisen yksityisyytensä takaisin hallintaansa. Sen helppokäyttöisyys ja oletusasetukset tekevät siitä viisaan valinnan yksityisyydestä tietoisille käyttäjille.



## Resurssit



### Viralliset asiakirjat




- [LibreWolfin virallinen verkkosivusto](https://librewolf.net)
- [Lähdekoodi Codebergissä](https://codeberg.org/librewolf)
- [Virallinen FAQ](https://librewolf.net/docs/faq)



### Oppaat ja vertailut




- [Tietosuojaoppaat](https://www.privacyguides.org/en/desktop-browsers/)
- [Vertailevat yksityisyystestit](https://privacytests.org)



### Yhteisön tuki




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)