---
name: Ente Auth
description: Avoimen lähdekoodin, päästä päähän salattu 2FA-todentaja
---
![cover](assets/cover.webp)



Kaksitekijätodennuksesta (2FA) on tullut välttämätön verkkotilien suojaamisessa. Tavanomaisen salasanasi lisäksi se edellyttää väliaikaista koodia, jonka yleensä luo oma sovellus. Tämä TOTP-mekanismi (Time-Based One-Time Password, aikaperusteinen kertakäyttösalasana) takaa, että vaikka salasanasi vaarantuisi, hyökkääjä ei pääse tilillesi ilman tätä 30 sekunnin välein uusittavaa toista tekijää.



Oikean todennussovelluksen valinta ei kuitenkaan ole helppoa. Vaikka Google Authenticator on suosittu, sillä on suuria rajoituksia: omaa koodia on mahdotonta tarkastaa, synkronointi ilman päästä päähän -salausta ja riski koodien täydellisestä katoamisesta, jos puhelimessa ilmenee ongelmia. Muut ratkaisut, kuten Authy, vaativat puhelinnumeron eivätkä takaa täydellistä luottamuksellisuutta.



**Ente Auth** on nykyaikainen ja turvallinen vaihtoehto. Tämä ilmainen, avoimen lähdekoodin ja monialustainen sovellus, jonka on kehittänyt [Ente Photosin] (https://ente.io) takana oleva tiimi, tarjoaa päästä päähän salattuja pilvivarmistuksia ja saumatonta synkronointia kaikkien laitteidesi välillä. Toisin kuin omistajakohtaiset ratkaisut, Ente Auth antaa sinulle täydellisen hallinnan tunnuskoodeista vaarantamatta yksityisyyttäsi.



Tässä oppaassa näytämme vaihe vaiheelta, miten Ente Auth asennetaan ja käytetään ja miksi tämä ratkaisu eroaa perinteisistä tunnistautujista.



## Esittelyssä Ente Auth



Ente Auth -palvelun on kehittänyt tiimi, joka on kehittänyt Ente Photos -palvelun, joka on päästä päähän salattu ja yksityisyyden suojaan sopiva valokuvien tallennuspalvelu. Ente-filosofialle uskollisena (Ente tarkoittaa malayalamin kielellä "minun", mikä symboloi tietojen hallintaa) Ente Auth suunniteltiin siten, että käyttäjät saavat takaisin täyden hallinnan kaksitekijätodennuskoodeistaan.



### Tärkeimmät ominaisuudet



**Vakiomuotoiset TOTP-koodit**: Ente Auth tuottaa tilapäisiä koodeja, jotka ovat yhteensopivia useimpien palveluiden kanssa (GitHub, Google, Binance, ProtonMail jne.). Voit lisätä niin monta 2FA-tiliä kuin tarvitset, ja sovellus laskee koodit annettujen salaisuuksien perusteella.



**Loppuun asti salattu pilvivarmistus**: Koodisi tallennetaan turvallisesti verkkoon. Vain sinä voit purkaa ne - salausavain johdetaan salasanastasi ja se on vain sinun tiedossasi. Ente (palvelin) ei tiedä salaisuuksiasi tai edes tilisi nimiä, sillä kaikki salataan asiakaspuolella nollatietoarkkitehtuurin avulla.



**Monien laitteiden synkronointi**: Voit asentaa Ente Authin useisiin laitteisiin (älypuhelin, tabletti, tietokone) ja käyttää koodejasi kaikilla laitteilla. Kaikki muutokset siirtyvät automaattisesti ja välittömästi muihin laitteisiisi salatun pilven kautta, mikä antaa sinulle suurta joustavuutta päivittäisessä työssäsi.



**Minimalistinen, intuitiivinen Interface**: Sovellus tarjoaa virtaviivaisen Interface:n, joka on helppo oppia myös muille kuin teknisille käyttäjille. 2FA-tileillä näkyy palvelun nimi, käyttäjätunnuksesi ja 6-numeroinen koodi, jotka päivittyvät reaaliajassa. Ente Auth näyttää myös seuraavan koodin muutamaa sekuntia etukäteen, jotta vältyt siltä, että koodi jää liian lyhyeksi vanhentumisen vuoksi.



**Avoin lähde ja tarkastettu**: Ente Authin lähdekoodi on [julkinen GitHubissa](https://github.com/ente-io/auth) AGPL v3.0 -lisenssillä. Kuka tahansa kehittäjä voi tarkastaa sen virheiden tai ei-toivotun käyttäytymisen löytämiseksi. Toteutettu salaus on ollut [riippumattoman ulkoisen auditoinnin kohteena](https://ente.io/blog/cryptography-audit/), mikä on tae sovelluksen turvallisuuden vakavuudesta.



### Edut ja rajoitukset



**Hyötyjä:**




- Sisäänrakennettu yksityisyys päästä päähän -salauksella
- Turvallinen synkronointi kaikkien laitteiden välillä
- Tarkastettavissa oleva avoin lähdekoodi
- Interface selkeä, intuitiivinen käyttäjä Interface
- Automaattinen varmuuskopiointi koodien katoamisen estämiseksi
- Saatavilla kaikilla alustoilla (mobiili ja työpöytä)



**Rajat:**




- Synkronointi edellyttää Internet-yhteyttä
- Edistyneet käyttäjät saattavat suosia 100 % offline-ratkaisuja, kuten Aegis (vain Android)
- Suhteellisen uusi verrattuna vakiintuneisiin ratkaisuihin



## Asennus



Ente Auth on saatavilla useimmilla suosituilla alustoilla. Voit ladata sovelluksen [virallisilta verkkosivuilta](https://ente.io/auth) tai virallisista kaupoista.



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth -lataussivu, jossa on kaikki saatavilla olevat alustat*



### Android


Sinulla on useita vaihtoehtoja:




- Google Play Store**: Etsi "Ente Auth" klassista asennusta varten
- F-Droid**: Saatavilla avoimen lähdekoodin Android-sovellusluettelosta, jossa taataan tarkistettu rakenne eikä omaa sisältöä
- Manuaalinen asennus** : APK-tiedostot voi ladata [projektin GitHub-sivulta](https://github.com/ente-io/auth/releases), jossa on integroitu ilmoitus uusista versioista



### iOS (iPhone/iPad)


Asenna Ente Auth suoraan Applen App Storesta etsimällä sovelluksen nimi. IOS-sovellusta voi käyttää myös Macissa, jossa on Apple Silicon -järjestelmäpiiri (M1/M2), Mac App Storen kautta.



### Tietokoneet (Windows, macOS, Linux)


Ente Auth tarjoaa natiivit työpöytäsovellukset. Käy [ente.io/download](https://ente.io/download) tai [GitHubin Releases-osiossa](https://github.com/ente-io/auth/releases) :





- Windows**: EXE-asennusohjelma toimitetaan
- macOS**: Vedä ja pudota DMG-levykuva sovelluksissa
- Linux** : Useita formaatteja saatavilla (AppImage portable, .deb Debian/Ubuntu, .rpm Fedora/Red Hat)



**Huomautus:** Tämä opetusohjelma perustuu Ente Auth v4.4.4:ään ja uudempiin versioihin. Aikaisemmissa versioissa voi olla pieniä Interface eroja.



### Interface Web


Ilman asennusta voit käyttää koodejasi [auth.ente.io](https://auth.ente.io) kautta millä tahansa selaimella. Interface-verkkopalvelun käyttö rajoittuu koodien tarkasteluun (hyödyllistä vianmäärityksessä), sillä tilien lisääminen edellyttää turvallisuussyistä mobiili- tai työpöytäsovellusta.



## Ensimmäinen kokoonpano



### Tilin luominen



Kun käynnistät Ente Authin ensimmäisen kerran, sinulla on kaksi vaihtoehtoa:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Ente Auth -etusnäyttö ja tilin luomisvaihtoehdot*



**Tilillä (suositellaan)**: Valitse "Luo tili" ja anna sähköpostiosoitteesi Address ja salasana. **Tärkeää**: tämä salasana toimii pääsalasanana tietojen salauksessa. Valitse vahva, yksilöllinen salasana, sillä tavanomaista nollausmenettelyä ei ole ilman tietojen menetystä. Jos kadotat sen, salattuja tietojasi ei voi enää palauttaa.



**Offline-tila**: Valitse "Käytä ilman varmuuskopioita", jos haluat käyttää sovellusta paikallisesti ilman pilveä. Tässä tilassa koodit pysyvät laitteessa, mutta sinun on vietävä ne manuaalisesti, jotta ne eivät katoa.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Sähköpostivarmennusprosessi ja 24-sanaisen palautusavaimen luominen*



Sähköpostivarmennusta voidaan pyytää tilin luomisen vahvistamiseksi ja palautuksen mahdollistamiseksi uudella laitteella. Ente Auth toimittaa sinulle myös 24 sanan palautusavaimen (joka perustuu BIP39-menetelmään). **On ehdottoman tärkeää, että tallennat tämän avaimen** turvalliseen paikkaan: se on ainoa keino palauttaa tietosi, jos unohdat salasanasi.



### Paikallinen turvallisuus



Suosittelen vahvasti paikallisen suojauksen käyttöönottoa koodin tai biometristen tunnusten avulla. Siirry kohtaan **Asetukset → Suojaus → Lukitusnäyttö** ja määritä :





- Biometrinen lukituksen avaus**: Face ID, sormenjälki riippuen laitteesi ominaisuuksista
- Sovelluskohtainen PIN-koodi/salasana**
- Automaattisen lukituksen viive**: esim. "Heti" tai 30 sekunnin käyttämättömyyden jälkeen



Tämä suojaus estää koodien luvattoman käytön, jos joku pääsee käsiksi lukitsemattomaan puhelimeesi. Huomaa, että tämä lukitus on lisäeste: tietosi pysyvät päästä päähän salattuina myös ilman tätä suojausta.



## 2FA-tilien lisääminen



### Vakiomenettely



Uuden 2FA-tilin lisäämiseksi otetaan konkreettinen esimerkki 2FA:n aktivoimisesta Bull Bitcoin -laitteeseen:



![Configuration du premier compte](assets/fr/04.webp)



*Ente Authin pää Interface on valmis lisäämään ensimmäisen 2FA*-tilin



**Käyttökohteen puoli (Bull Bitcoin)**: Kirjaudu sisään Bull Bitcoin -tilillesi, siirry turvallisuusasetuksiin ja ota käyttöön kaksitekijätodennus.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* turvallisuusasetusten valikko



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Mahdollisuus ottaa kaksitekijätodennus käyttöön Bull Bitcoin*:ssä



Tämän jälkeen palvelu näyttää QR-koodin, jonka voit skannata tunnistautumissovelluksella:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Bull Bitcoin:n luoma QR-koodi, joka skannataan todentamislaitteella*



**In Ente Auth**: Napsauta "Enter a setup key" ja skannaa sitten Bull Bitcoin:n näyttämä QR-koodi. Ente Auth tunnistaa tilin automaattisesti ja täyttää kentät.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Bull Bitcoin -tilin tietojen määrittäminen Ente Auth*:ssa



Voit muokata palvelun nimeä ja käyttäjätunnusta, jotta se olisi helpompi löytää. Lisäasetukset (SHA1-algoritmi, 30s jakso, 6 numeroa) ovat yleensä oletusarvoisesti oikein.



**Palvelupuolen validointi**: Palaa Bull Bitcoin:een ja syötä Ente Authin luoma 6-numeroinen koodi aktivoinnin viimeistelemiseksi.



![Saisie du code 2FA](assets/fr/09.webp)



*Syötä Ente Authin luoma koodi 2FA*-aktivoinnin vahvistamiseksi



![2FA activée](assets/fr/10.webp)



*Vahvistus onnistuneesta 2FA-aktivoinnista Bull Bitcoin:ssa*



**Varmuuskopiointikoodit**: Bull Bitcoin antaa sinulle palautuskoodit. **Säilytä ne turvalliseen paikkaan, erillään autentikointilaitteesta.



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Vaihtoehto generate hätävarakoodeille Bull Bitcoin*:ssä



![Codes de récupération](assets/fr/12.webp)



*Luettelo talteenottokoodeista, jotka on säilytettävä turvallisessa paikassa*



### Organisaatio ja hallinto



Ente Auth tarjoaa useita käytännöllisiä ominaisuuksia:



**Pikakopio**: Paina koodia kopioidaksesi sen automaattisesti leikepöydälle.



**Ympäristöherkät toimet**: Paina ja pidä painettuna (tai napsauta hiiren kakkospainikkeella työpöydällä) muokataksesi, poistaaksesi, jakaaksesi tai kiinnittääksesi merkinnän.



**Tagit ja haku**: Järjestä tilejäsi tunnisteilla (henkilökohtainen/ammattimainen, palveluluokittain) ja käytä hakupalkkia nopeaan suodatukseen.



![Création d'un tag](assets/fr/17.webp)



*Tunnisteen luontiprosessi: kontekstivalikko ja luontiikkuna*



![Tag appliqué](assets/fr/18.webp)



*Tunniste "Bitcoin" onnistuneesti sovellettu Bull Bitcoin*-tilille



**Automaattiset kuvakkeet**: [Simple Icons] -kuvakepaketin (https://simpleicons.org/) integroinnin ansiosta jokainen merkintä voidaan kuvata palvelun logolla.



**Tilapäinen turvallinen yhteiskäyttö**: Turvallinen jakaminen on ainutlaatuinen Ente Auth -ominaisuus, jonka avulla voit lähettää 2FA-koodin kollegalle paljastamatta sen taustalla olevaa salaisuutta. generate salattu linkki, joka on voimassa enintään 2, 5 tai 10 minuuttia - vastaanottaja näkee koodin reaaliajassa, mutta ei voi viedä sitä tai käyttää tilitietoja. Tämä menetelmä sopii erinomaisesti tekniseen apuun tai tilapäiseen yhteistyöhön, sillä se tarjoaa turvallisuustason, joka ei ole mahdollinen pelkän kuvakaappauksen tai tekstiviestin avulla.



![Partage sécurisé](assets/fr/19.webp)



*Interface tilapäinen turvallinen yhteiskäyttö: valitse kesto (5 min)*



**Turvallinen vienti/tuonti**: Ente Auth mahdollistaa koodien viennin muihin sovelluksiin tai niiden tuonnin Google Authenticatorista ja muista ratkaisuista. Vienti tapahtuu salatun tiedoston tai QR-koodin kautta, mikä takaa tietojesi siirrettävyyden turvallisuudesta tinkimättä.



**BIP39-elvytysavain**: Sovellus luo automaattisesti 24-sanaisen palautuslausekkeen BIP39 (Bitcoin Improvement Proposal) -standardin mukaisesti, joka on identtinen kryptovaluuttalompakoiden kanssa. Tämä lause on lopullinen palautusavaimesi, jonka avulla voit palauttaa kaikki koodisi, vaikka unohtaisit pääsalasanasi.



## Konfigurointi ja asetukset



Ente Auth tarjoaa lukuisia mukautusvaihtoehtoja, jotka ovat käytettävissä sovelluksen asetusten kautta:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Yleiskatsaus Ente Auth*:ssa käytettävissä olevista parametreista



### Tilien ja tietojen hallinta



![Paramètres de sécurité](assets/fr/14.webp)



*Edistyneet suojausvaihtoehdot: sähköpostivarmennus, PIN-koodi, aktiiviset istunnot*



Suojausasetusten avulla voit :




- Ota käyttöön sähköpostivarmennus uusille yhteyksille
- Aktivoi kulkuavain
- Näytä aktiiviset istunnot eri laitteilla
- PIN-koodin tai biometristen tunnisteiden määrittäminen



### Interface ja käyttömahdollisuudet



![Paramètres généraux](assets/fr/15.webp)



*Interface parametrit ja sovelluksen mukauttaminen*



Yleisiä asetuksia ovat :




- Kieli**: Interface monikielinen
- Näyttö**: Suuret kuvakkeet, kompakti tila
- Yksityisyys**: Piilota koodit, nopea haku
- Telemetria**: Virheraportointi (voidaan poistaa käytöstä)



## Varmuuskopiointi ja synkronointi



### Miten salaus toimii



Kun lisäät tilin yhdistetyn Ente-tilin kanssa, sovellus salaa nämä arkaluonteiset tiedot välittömästi paikallisesti pääavaimellasi (joka on peräisin salasanastasi). Tämän jälkeen salatut tiedot lähetetään Ente-palvelimelle tallennettavaksi.



Tämän mekanismin ansiosta koodiesi päästä päähän salattu pilvivarmistus on aina käytettävissä. Jos kadotat laitteesi, asenna Ente Auth uudelleen ja muodosta yhteys uudelleen: sovellus lataa ja purkaa kaikki koodisi automaattisesti.



### Monen laitteen synkronointi



Jos käytät Ente Authia sekä älypuhelimessa että tietokoneessa, kaikki lisäykset tai muutokset toisessa laitteessa näkyvät sekunneissa toisessa laitteessa. Tämä synkronointi tapahtuu Enten pilven kautta, mutta koska tiedot ovat päästä päähän salattuja, palvelin näkee vain lukukelvottoman salatun sisällön.



![Synchronisation mobile](assets/fr/16.webp)



*Synkronointidemo: sama Bull Bitcoin -tili käytettävissä mobiilissa ja työpöydällä*



Synkronointi on saumatonta: asenna Ente Auth älypuhelimeesi, kirjaudu sisään tunnuksillasi, ja kaikki 2FA-koodisi (tässä Bull Bitcoin) näkyvät automaattisesti. Yllä olevassa esimerkissä näkyy täydellinen synkronointi työpöydän ja matkapuhelimen välillä - sama Bull Bitcoin -koodi on käytettävissä molemmissa laitteissa.



Mitä tulee luottamuksellisuuteen, Ente tai mikään kolmas osapuoli ei pääse käsiksi 2FA-salaisuuksiisi. Jopa metatiedot (tunnisteet, muistiinpanot, palvelun nimet) salataan ennen lähettämistä. Tämä nollatietoarkkitehtuuri varmistaa, että vain sinä voit purkaa koodisi.



### Offline-käyttö



Synkronointi edellyttää Internetiä, mutta Ente Auth toimii täydellisesti offline-tilassa kaikilla laitteilla, koska kaikki tiedot tallennetaan paikallisesti. Offline-muutokset asetetaan jonoon ja synkronoidaan heti, kun yhteys palautuu.



## Turvallisuus ja yksityisyys



### Kryptografiset takuut



Ente Auth perustuu vankkaan päästä päähän -salaukseen ja nollatietoarkkitehtuuriin. Koodit salataan ainoastaan sinun hallussasi olevalla avaimella, joka on johdettu pääsalasanastasi käyttäen kehittyneitä avainten johdannaisfunktioita.



**Nollatietoarkkitehtuuri: Ente ei pääse fyysisesti käsiksi tietoihin. Jopa metatiedot (palveluiden nimet, tunnisteet, muistiinpanot) salataan asiakkaan puolella ennen siirtoa. Tällä lähestymistavalla varmistetaan, että palvelimiin kohdistuvan hyökkäyksen tai viranomaispyynnön yhteydessä Ente voi paljastaa vain salattuja tietoja, joita ei voi lukea ilman salasanaasi.



**Lokaali salaus**: Salausprosessi tapahtuu kokonaan laitteessasi ennen kuin se lähetetään pilveen. Enten palvelimet vastaanottavat ja tallentavat vain salattuja tietoja, joten luvaton pääsy on mahdotonta jopa palvelun ylläpitäjille.



### Avoimuus ja tarkastukset



Koska koodi on [avointa lähdekoodia] (https://github.com/ente-io/auth), yhteisö voi tarkistaa, ettei siinä ole takaovia. Ente on teettänyt [useita ulkoisia tarkastuksia](https://ente.io/blog/cryptography-audit/) validoidakseen sen toteutuksen turvallisuuden:





- Cure53** (Saksa): Sovellusten ja salausjärjestelmien tietoturvatarkastus
- Symbolic Software** (Ranska): Erikoistunut salausasiantuntemus
- Fallible** (Intia): Tunkeutumistestaus ja haavoittuvuusanalyysi



Nämä tunnustettujen yritysten suorittamat riippumattomat tarkastukset takaavat, että Ente Authin salaustekniikan toteutus on parhaiden turvallisuuskäytäntöjen mukainen eikä siinä ole kriittisiä puutteita.



### Tietosuojakäytäntö



Ente Auth soveltaa [esimerkillistä tietosuojakäytäntöä] (https://ente.io/privacy/), joka perustuu minimaaliseen tiedonkeruuseen. Vain palvelun toiminnan kannalta ehdottoman välttämättömät tiedot säilytetään: sähköpostiosoitteesi Address tunnistautumista ja tilin palauttamista varten.



**Ei seurantaa tai telemetriaa**: Toisin kuin useimmat sovellukset, Ente Auth ei kerää käyttömittareita, ei tunnistetietoja eikä käyttäytymistietoja. Sovellus toimii ilman tungettelevia mainos- tai analytiikkaseurantalaitteita.



**GDPR-vaatimustenmukaisuus**: Ente noudattaa täysin Euroopan yleistä tietosuoja-asetusta. Sinulla on milloin tahansa oikeus tutustua tietoihin, korjata tai poistaa ne. Tietojen vienti](https://ente.io/take-control/) on vain napsautuksen päässä, ja tilisi pysyvä poistaminen poistaa kaikki tietosi palvelimilta.



**Keskitetty, turvallinen varastointi**: Näin taataan optimaalinen saatavuus ja vältetään riippuvuus yhdestä pilvipalveluntarjoajasta.



Enten liiketoimintamalli perustuu maksulliseen Ente Photos -palveluun, minkä ansiosta voimme tarjota Ente Auth -palvelun **maksutta ja rajoituksetta** vaarantamatta yksityisyyttäsi rahanarvoistamalla tietojasi. Tämä lähestymistapa takaa palvelun kestävyyden ilman, että se perustuu mainontaan tai henkilötietojen jälleenmyyntiin.



## Vertailu muihin ratkaisuihin



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth on yksi harvoista ratkaisuista, jossa yhdistyvät kaikki edut: lähdekoodin läpinäkyvyys, salattu pilvivarmistus ja alustarajat ylittävä synkronointi.



## Suositellut käyttötapaukset



### Yksittäiset käyttäjät



Ente Auth on ihanteellinen turvallisuustietoisille henkilöille, jotka aktivoivat 2FA:n järjestelmällisesti. Sinun ei enää tarvitse huolehtia siitä, että kadotat koodisi puhelinta vaihtaessasi tai että sinun ei tarvitse valita mukavuuden ja turvallisuuden välillä.



### Perhe- ja monilaitekäyttö



Sovellus pääsee oikeuksiinsa, jos käytät useita laitteita. Voit tallentaa koodit älypuhelimiin ja tabletteihin tai jakaa tiettyjä perhekoodeja (Netflix, perhepilvi) synkronoidusti ja turvallisesti.



### Ammattimainen käyttö



Arkaluonteisia tilejä hallinnoiville tiimeille Ente Auth helpottaa yhteistyötä säilyttäen samalla tietoturvan "Organisaatio ja hallinta" -osioon integroitujen kehittyneiden jako-ominaisuuksien ansiosta.



## Parhaat käytännöt





- Tallenna hätäkoodit**: Pidä kunkin palvelun antamat palautuskoodit poissa puhelimestasi.





- Käytä vahvaa pääsalasanaa**: Ente Auth -pääsalasanasi on oltava ainutlaatuinen ja vahva, sillä se suojaa kaikkia koodejasi.





- Aktivoi paikallinen suojaus**: Määritä PIN-koodi tai biometriikka estämään luvaton fyysinen pääsy.





- Älä räätälöi liikaa**: Vältä pitkälle meneviä muutoksia, jotka voivat vaarantaa synkronoinnin.





- Pidä hakemus ajan tasalla**: Päivitykset korjaavat tietoturva-aukkoja ja parantavat toiminnallisuutta.





- Testin palauttaminen**: Tarkista toisinaan, että voit palauttaa koodit toisella laitteella.



## Päätelmä



Ente Auth on nykyaikainen, kattava ratkaisu kaksitekijätodennukseen. Yhdistämällä turvallisuuden, avoimuuden ja helppokäyttöisyyden tämä avoimen lähdekoodin sovellus vastaa vaativien käyttäjien tarpeisiin mukavuudesta tinkimättä.



Toisin kuin omistajakohtaiset ratkaisut, jotka lukitsevat sinut vaikeaselkoiseen ekosysteemiin, Ente Auth antaa sinulle takaisin tunnistautumistietojesi hallinnan ja suojaa sinua vahingossa tapahtuvalta katoamiselta salattujen varmuuskopioidensa ansiosta.



Olitpa sitten yksityishenkilö, joka haluaa turvata henkilökohtaiset tilinsä, tai tiimi, joka hallinnoi yrityksen käyttöoikeuksia, Ente Auth on fiksu valinta, kun haluat modernisoida digitaalisen tietoturvan lähestymistapasi yksityisyydestä tinkimättä.



## Resurssit ja tuki



### Viralliset asiakirjat




- Virallinen verkkosivusto**: [ente.io/auth](https://ente.io/auth)
- Ohjekeskus**: [help.ente.io/auth](https://help.ente.io/auth)
- Tekninen blogi**: [ente.io/blog](https://ente.io/blog)



### Lähdekoodi ja avoimuus




- GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- Kryptografian tarkastus**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Yhteisö




- Keskustelu**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- Reddit**: [r/enteio](https://reddit.com/r/enteio)