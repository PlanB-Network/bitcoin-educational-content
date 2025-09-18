---
name: Proton Authenticator
description: Miten voin käyttää Proton Authenticatoria tilieni suojaamiseen 2FA:lla?
---
![cover](assets/cover.webp)



Kaksitekijätodennus (two-factor authentication, 2FA) lisää ylimääräisen turvasulun tileillesi vaatimalla salasanasi lisäksi lisätodisteita siitä, että vain sinulla on salasana. 2FA:n ottaminen käyttöön vähentää huomattavasti hakkeroinnin riskiä, vaikka salasanasi vaarantuisi phishingin tai tietovuodon vuoksi. Ilman 2FA:ta hyökkääjä tarvitsisi vain salasanasi päästäkseen tileillesi, mutta 2FA:n avulla hän tarvitsisi myös toisen tekijän, mikä estää useimmat tilivarkausyritykset.



2FA-tyyppejä on erilaisia. Tekstiviestikoodit ovat parempi kuin ei mitään, mutta ne ovat alttiita SIM-kortin vaihtohyökkäyksille ja salakuuntelulle. Emme suosittele tekstiviestejä ensisijaiseksi 2FA-toiminnoksi. Todennussovellukset (TOTP) generate tilapäiset koodit paikallisesti laitteessa, jolloin niitä on paljon vaikeampi siepata. Fyysiset suojausavaimet tarjoavat parhaan suojan, mutta vaativat erillisen laitteiston.



Proton Authenticator on TOTP-todentaja. Se on Protonin vastaus nykyisten sovellusten rajoituksiin: monet niistä ovat patentoituja, sisältävät mainosseurantalaitteita eivätkä tarjoa salattua varmuuskopiointia. Proton Authenticator erottuu edukseen tarjoamalla avoimen lähdekoodin sovelluksen, jossa ei ole mainoksia eikä seurantalaitteita ja jossa on päästä päähän salattu varmuuskopiointi.



## Esittelyssä Proton Authenticator



Proton Authenticator on yksityisyyteen keskittyvistä palveluistaan tunnetun Protonin kehittämä TOTP-todennussovellus mobiililaitteille ja työpöydälle. Kuten kaikki Protonin tuotteet, sovellus on avoimen lähdekoodin sovellus, ja se on käynyt läpi riippumattomat tietoturvatarkastukset. Se on saatavilla ilmaiseksi kaikilla alustoilla (Android, iOS, Windows, macOS, Linux).



Proton Authenticator tarjoaa seuraavat keskeiset ominaisuudet:





- **TOTP-koodien** luominen 2FA-tileillesi, yhteensopiva useimpien Google Authenticatoria, Authyta jne. käyttävien sivustojen kanssa.





- **Valinnainen salattu pilvivarmistus**: voit yhdistää sovelluksen Proton-tiliisi, jolloin voit varmuuskopioida ja synkronoida koodisi päästä päähän -salauksella. Jos kadotat laitteesi, voit yksinkertaisesti liittää uuden laitteen uudelleen ja palauttaa kaikki koodisi.





- **Synkronointi useilla laitteilla**: kirjautumalla Protoniin sovelluksessa 2FA-koodisi synkronoituvat automaattisesti useiden laitteiden välillä päästä päähän -salauksen avulla. IOS:ssä vaihtoehtona on synkronointi iCloudin kautta.





- **Paikallinen lukitus salasanalla tai biometriikalla**: sovellus tarjoaa PIN-koodin ja/tai sormenjälki- tai kasvotunnuksen lukituksen. Vaikka joku pääsisi fyysisesti käsiksi lukitsemattomaan puhelimeesi, hän ei pysty avaamaan Proton Authenticatoria.





- **Ei tiedonkeruuta tai seurantalaitteita**: Proton on sitoutunut siihen, ettei sovelluksen kautta kerätä henkilötietoja. Piilomainontaa tai käyttäytymisanalyysiä ei ole.





- **Helppo tuonti/vienti**: Yksi Proton Authenticatorin vahvuuksista on sen ohjatun tuonnin ohjattu toiminto olemassa olevia tilejä varten, joka on yhteensopiva muiden sovellusten kanssa (Google Authenticator, Authy, Aegis jne.). Voit myös tarvittaessa viedä koodit tiedostoon.



Lyhyesti sanottuna Proton Authenticator pyrkii olemaan tinkimätön 2FA-ratkaisu: turvallinen, yksityinen ja joustava.



## Asennus



Proton Authenticator on saatavilla ilmaiseksi kaikilla alustoilla. Voit ladata sovelluksen viralliselta sivulta: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Virallinen Proton Authenticator -sivu, jossa esitellään sovelluksen pääominaisuudet ja Interface*



Tältä sivulta löydät latauslinkit kaikille käyttöjärjestelmille: Android, iOS, Windows, macOS ja Linux. Napsauta vain haluamaasi käyttöjärjestelmää ja noudata tavallisia asennusvaiheita.



Tässä oppaassa näytämme, miten se asennetaan ja konfiguroidaan macOS:ssä, ja sitten katsomme, miten sovellus asennetaan iOS:ään ja miten koodit synkronoidaan näiden kahden laitteen välillä.



### Asennus macOS-käyttöjärjestelmään



Kun olet ladannut ja asentanut sovelluksen, käynnistä Proton Authenticator. Ensimmäisellä käynnistyskerralla sovellus opastaa sinut muutaman alkumääritysnäytön läpi:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Proton Authenticatorin tervetuliaisnäyttö, jossa on "Turvallisuus jokaisessa koodissa" -viesti ja "Aloita "*-painike



### Alkuperäinen tuonti



Jos Proton Authenticator havaitsee, että olet aiemmin käyttänyt toista 2FA-sovellusta, näyttöön saattaa tulla ohjatun tuonnin ohje. Se tukee suoraa tuontia tietyistä sovelluksista (Google Authenticator, 2FAS, Authy, Aegis jne.). Vaihtoehtoisesti voit ohittaa tämän vaiheen ja lisätä tilisi manuaalisesti myöhemmin.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Ohjattu tuontitoiminto koodien siirtämiseksi muista tunnistautumissovelluksista*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Yhteensopivat tuontisovellukset: authy, Bitwarden Authenticator, Ente Auth ja Google Authenticator*



### Paikallisen sovelluksen suojaus



Aseta lukituksen PIN-koodi tai ota käyttöön biometrinen lukituksen avaus (Touch ID), jos se on käytettävissä. Tämä vaihe on ratkaisevan tärkeä, jotta kukaan Macia käyttävä ei pääse vapaasti käsiksi 2FA-koodeihisi.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Touch ID:n konfigurointinäyttö, jossa on "Suojaa tietosi" -viesti ja "Aktivoi Touch ID "*-painike



### Synkronointivaihtoehdot



Sovelluksen avulla voit myös aktivoida iCloud-synkronoinnin varmuuskopioidaksesi tietosi turvallisesti Apple-laitteiden välillä.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*ICloud-synkronointivaihtoehto, jossa on viesti "Varmuuskopioi tietosi turvallisesti salatulla iCloud-synkronoinnilla "*



Kun nämä vaiheet on suoritettu, Proton Authenticator on käyttövalmis.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface tärkein tyhjä Proton Authenticator ja "Luo uusi koodi" ja "Tuo koodit "* -vaihtoehdot



## Lisää 2FA-tili ProtonMaililla



Seuraavaksi tarkastelemme ensimmäisen 2FA-koodin lisäämistä ProtonMailin esimerkin avulla. Tämä menetelmä toimii samalla tavalla kaikissa palveluissa, jotka tukevat kaksitekijätodennusta.



### Ota 2FA käyttöön ProtonMailissa



Ensinnäkin voit tutustua ProtonMail-oppaaseemme saadaksesi lisätietoja:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Kirjaudu sisään ProtonMail-tilillesi ja siirry suojausasetuksiin. Etsi "Two-factor authentication" -vaihtoehto ja aktivoi se.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMailin asetussivu, jossa on "Authenticator-sovellus"-vaihtoehto "Kahden tekijän todennus "* -osiossa



Aktivoi todentaja napsauttamalla painiketta, ja ProtonMail pyytää sinua valitsemaan todentamissovelluksen.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMail 2FA:n konfigurointi-ikkuna, jossa on "Peruuta" ja "Seuraava "* -painikkeet



ProtonMail näyttää sitten QR-koodin, jonka voit skannata tunnistautumissovelluksella.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMailin QR-koodi, jonka voit skannata tunnistautumissovelluksellasi, ja käytettävissä on myös "Enter key manually instead" -vaihtoehto*



Jos haluat syöttää avaimen manuaalisesti, napsauta "Enter key manually instead" (Syötä avain manuaalisesti sen sijaan) nähdäksesi salaisen avaimen.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*2FA-tietojen syöttäminen manuaalisesti: Avain, aikaväli (30) ja numerot (6)*



### Skannaa QR-koodi Proton Authenticatorilla



Napsauta MacOS:n Proton Authenticatorissa "Luo uusi koodi". Sovellus tarjoaa sinulle useita vaihtoehtoja: **Skannaa QR-koodi** tai **Syötä avain manuaalisesti**.



Skannaa ProtonMailin näytössä näkyvä QR-koodi Macin kameran avulla. Kun olet skannannut QR-koodin, pääset uuden koodin määritysnäyttöön.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Uuden merkinnän luonti-ikkuna, jossa on otsikko (ProtonMail), salaisuus, lähettäjä (Proton), numeroparametrit ja aikavälikentät*



Proton Authenticator täyttää tiedot automaattisesti. Voit halutessasi muokata nimeä ja napsauttaa sitten "Tallenna".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*ProtonMailin (848 812) luotu TOTP-koodi ja jäljellä oleva aika näytetään*



### Validoi kokoonpano



ProtonMail pyytää sinua syöttämään 6-numeroisen koodin, jonka Proton Authenticator luo vahvistaaksesi, että 2FA toimii oikein.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*ProtonMailin vahvistusnäyttö, jossa pyydetään syöttämään 6-numeroinen koodi (848812)*



Kopioi koodi sovelluksesta (napsauttamalla sitä) ja liitä se ProtonMailiin aktivoinnin suorittamiseksi.



Kun ProtonMail on validoinut, se pyytää sinua lataamaan palautuskoodisi. On tärkeää tallentaa ne huolellisesti.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMailin palautuskoodien näyttö, jossa on luettelo pelastuskoodeista ja "Lataa "*-painike



### Hätäkoodit



Kun lisäät tiliä, pidä palvelun antamat palautuskoodit. Useimmat sivustot tarjoavat staattisia, kertakäyttöisiä palautuskoodeja, joita voi säilyttää turvallisessa paikassa. Säilytä nämä varmuuskopiointikoodit Proton Authenticatorin ulkopuolella, jotta voit käyttää tiliäsi, jos menetät pääsyn 2FA-sovellukseen.



## IOS-asennus ja koodin tuonti



Nyt kun olet ottanut Proton Authenticatorin käyttöön macOS:ssä, voit halutessasi käyttää sitä myös iPhonessa tai iPadissa. Näin saat 2FA-koodit useisiin laitteisiin.



### Lataa sovellus iOS:ssä



Mene App Storeen ja etsi "Proton Authenticator". Lataa ja asenna sovellus iOS-laitteeseesi.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Asennusprosessi iOS:ssä: tervetuliaisnäyttö, ohjattu tuonti, yhteensopivien sovellusten valinta ja lopullinen "Tuo koodit Proton Authenticatorista "* -näyttö



### Menetelmä 1: Vienti/tuonti JSON-tiedoston kautta



Jos et käytä automaattista synkronointia (iCloud tai Proton-tili), sinun on siirrettävä koodit manuaalisesti Macista iPhoneen:



**Vaihe 1 - Vie macOS:stä** :



Avaa Macissa Proton Authenticator ja siirry Asetukset (hammasratas-kuvake). Napsauta valikossa "Vie".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Proton Authenticatorin asetusvalikko macOS:ssä, jossa "Vie"-vaihtoehto näkyvissä*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Vienti-ikkuna, jonka tiedostonimi on "Proton_Authenticator_backup_2025" ja "Tallenna "*-painike



Tallenna JSON-tiedosto Macissa. Voit lähettää sen suojatulla sähköpostilla tai tallentaa sen iCloud Driveen, jotta voit käyttää sitä iPhonestasi.



**Vaihe 2 - Tuo iOS** :



Asenna iPhoneen Proton Authenticator ja valitse konfiguroinnin aikana koodien tuominen. Valitse "Proton Authenticator" luettelosta ja tuo JSON-tiedosto.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Tuontiprosessi iOS:ssä: JSON-tiedoston lokalisointi, tuonnin vahvistus ja konfigurointinäytöt Face ID- ja iCloud-vaihtoehdoilla*



### Menetelmä 2: Automaattinen synkronointi



** Proton-tilin kautta (monialustasynkronointia varten)** :



Jos et ole vielä luonut Proton-tiliä ja haluat synkronoida eri käyttöjärjestelmien välillä, sovellus pyytää sinua luomaan tai yhdistämään Proton-tilin.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Laitteen synkronointinäyttö, jossa pyydetään luomaan ilmainen Proton-tili tai yhdistämään olemassa olevaan tiliin*



** iCloudin kautta (vain Applen ekosysteemissä)** :


Jos käytät vain Applen laitteita, voit valita iCloud-synkronoinnin sovelluksen asetuksista. Tämä menetelmä synkronoi koodisi automaattisesti ja turvallisesti kaikkien Apple-laitteidesi välillä ilman Proton-tiliä.



## Salattu varmuuskopiointi ja palautus



Yksi Proton Authenticatorin tärkeimmistä ominaisuuksista on 2FA-koodien varmuuskopiointi, joka varmistaa, että laitteen katoaminen tai vaihtaminen ei tarkoita, että sinun ei tarvitse aloittaa kaikkea alusta.



### End-to-end-salaus



Kun kyseessä on salattu pilvivarmistus Proton Authenticatorilla, TOTP-salaisuutesi salataan paikallisesti laitteellasi ennen kuin ne lähetetään Proton-palvelimelle. Salaus voidaan purkaa vain sinun toimestasi, Proton-tiliisi liitetyillä laitteillasi. Proton AG:lla ei ole avainta lukea rekisteröityjä koodejasi.



Jos valitset iOS:ssä Proton-tilin sijasta iCloudin, tietosi salataan Applen standardien mukaisesti. Androidin paikallisessa varmuuskopioinnissa voit salata varmuuskopiotiedoston valitsemallasi salasanalla.



### Palauttaminen menetyksen sattuessa



Jos puhelimesi katoaa, varastetaan tai vaihdat luuria :



**Kun Protonin varmuuskopiointi on käytössä**: Asenna Proton Authenticator uuteen laitteeseen. Kirjaudu alkuasennuksen aikana samalle Proton-tilille. Sovellus synkronoi ja lataa välittömästi kaikki 2FA-koodisi salatusta varmuuskopiosta.



**ICloud-varmuuskopioinnilla (iOS)**: Yhdistä uusi iPhone/iPad samalla Apple ID:llä ja varmista, että iCloud-avaimenperä on aktivoitu. Kun olet asentanut Proton Authenticatorin, muodosta yhteys iCloudiin. Koodiesi pitäisi synkronoitua iCloudin kautta ja tulla näkyviin.



**Ei pilvivarmistusta**: Sinun on tuotava tilisi manuaalisesti. Jos olet vienyt varmuuskopiotiedoston, käytä Proton Authenticatorin tuontitoimintoa. Pahimmassa tapauksessa, jos sinulla ei ollut varmuuskopiota, sinun on käytettävä kunkin palvelun varmuuskopiointikoodeja tai otettava yhteyttä asiakaspalveluun.



Proton Authenticatorin avulla voit viedä tilisi milloin tahansa joko salattuna tiedostona tai usean tilin QR-koodina. Nämä vaihtoehdot antavat sinulle lisää varmuutta.



## Parhaat käytännöt



2FA-todentajan käyttäminen parantaa turvallisuutta huomattavasti, mutta tiettyjä parhaita käytäntöjä on noudatettava:



### Tallenna hätäkoodit



Kun aktivoit 2FA:n palveluun, saat usein luettelon palautuskoodeista. Pidä ne poissa puhelimestasi (paperilla, salatussa salasanahallinnassa jne.). Jos autentikointilaitteesi katoaa kokonaan, nämä staattiset koodit pelastavat sinut.



### Älä sekoita salasanojasi ja 2FA-koodejasi



On houkuttelevaa käyttää salasanahallintaohjelmaa, joka tallentaa myös TOTP:t. Salasanan ja 2FA-koodin säilyttäminen samassa paikassa luo kuitenkin yhden vikapisteen ja heikentää kaksoistodennusta. Maksimaalisen turvallisuuden saavuttamiseksi monet asiantuntijat suosittelevat kahden tekijän erottamista toisistaan: salasanat turvallisessa hallinnassa ja 2FA-koodit erillisessä sovelluksessa, kuten Proton Authenticatorissa. Integroidun hallinnan käyttäminen on kuitenkin parempi vaihtoehto kuin 2FA:n puuttuminen kokonaan.



### Aktivoi useita 2FA-menetelmiä



Käytä mieluiten useampaa kuin yhtä toista tekijää kriittisillä tileilläsi. Älä epäröi lisätä fyysistä turva-avainta, jos palvelu sallii sen. Katso lisätietoja Yubikeyn fyysisiä avaimia koskevasta oppaasta:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Pidä myös painetut hätäkoodit käsillä.



### Pysy huomaamattomana ja suojaa laitteesi



Älä anna kenenkään tutkia lukitsematonta puhelintasi. Proton Authenticatorin avulla koodisi on suojattu PIN-koodilla/biometrisillä tunnuksilla - älä paljasta tätä PIN-koodia. Varo myös tietojenkalastelua: vaikka käytössäsi olisi 2FA, hyökkääjä voi käyttää koodia petolliselle sivustolle reaaliaikaisesti, jos annat sen.



### Päivitykset ja tarkastukset



Pidä Proton Authenticator ajan tasalla (päivitykset korjaavat mahdolliset puutteet). Koska koodi on avoin, yhteisö tekee epävirallisia tarkastuksia, ja Proton julkaisee virallisten tarkastusten tulokset.



## Vertailu muihin sovelluksiin



Miten Proton Authenticator pärjää muille todennussovelluksille? Tässä on vertaileva yhteenveto:



**Proton Authenticator**: Avoin lähdekoodi, valinnainen E2EE-salattu pilvivarmistus, synkronointi useilla laitteilla, paikallinen lukitus, ei seurantaa, käytettävissä mobiililaitteissa ja työpöydillä.



**Google Authenticator**: Google-tilin kautta vuodesta 2023 lähtien, mutta ilman päästä päähän -salausta (Google voi nähdä avaimet), usean laitteen synkronointi lisätty vuonna 2023, ei sovelluslukitusta oletusarvoisesti, sisältää Googlen seurantalaitteita.



**Aegis Authenticator**: Ei pilvisynkronointia, koodi/biometrinen lukitus, ei seurantaa, vain Android.



**Authy**: Salasanalla salattu pilvivarmistus, mutta suljettu koodi, usean laitteen synkronointi, PIN-lukko/sormenjälki, kerää puhelinnumeron, työpöytäsovellus lopetetaan maaliskuussa 2024.



Löydät Authy-oppaamme alta:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator on yksi kattavimmista ja turvallisimmista saatavilla olevista ratkaisuista: avoin lähdekoodi, usean laitteen salattu synkronointi, ei kaupallista seurantaa.



## Resurssit ja tuki



### Viralliset asiakirjat




- **Virallinen verkkosivusto**: [proton.me/authenticator](https://proton.me/authenticator) - Tuotteen esittely ja lataukset
- **Lataa sivu**: [proton.me/fi/authenticator/download](https://proton.me/fr/authenticator/download) - Linkit kaikille käyttöjärjestelmille
- **Protonituki**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Virallinen 2FA-aktivointiopas
- **Protonin blogi**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Ilmoitus ja yksityiskohtaiset ominaisuudet



### Lähdekoodi ja avoimuus




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Avoimen lähdekoodin koodi
- **Turvatarkastukset**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Riippumattomat tarkastusraportit



### Suositellut turvallisuustestit


Testaa asetukset konfiguroinnin jälkeen:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Tarkista, onko tilisi vaarannettu
- [2FA Directory](https://2fa.directory/) - Luettelo 2FA:ta tukevista palveluista



### Yhteisöt ja keskustelut




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Virallinen Proton-yhteisö
- Yksityisyyden suojaa koskevat oppaat **Foorumi**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Tekniset keskustelut yksityisyyden suojaan liittyvistä kysymyksistä
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Yleisiä vinkkejä yksityisyyden suojaan



### Muut




- [Have I Been Pwned](https://haveibeenpwned.com/) - Tarkista, onko tilisi vaarannettu
- [2FA Directory](https://2fa.directory/) - Luettelo 2FA:ta tukevista palveluista