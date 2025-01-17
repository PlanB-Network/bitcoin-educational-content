---
term: BIP

---
Lyhenne sanoista "Bitcoin Improvement Proposal" Bitcoin-parannusehdotus (Bitcoin Improvement Proposal, BIP) on virallinen prosessi, jossa ehdotetaan ja dokumentoidaan parannuksia ja muutoksia Bitcoin-protokollaan ja sen standardeihin. Koska Bitcoinissa ei ole keskusyksikköä, joka päättäisi päivityksistä, BIP:t antavat yhteisölle mahdollisuuden ehdottaa, keskustella ja toteuttaa parannuksia jäsennellysti ja avoimesti. Jokaisessa BIP:ssä esitetään yksityiskohtaisesti ehdotetun parannuksen tavoitteet, perustelut, mahdolliset vaikutukset yhteensopivuuteen sekä edut ja haitat. Kuka tahansa yhteisön jäsen voi kirjoittaa BIP:t, mutta niiden on oltava muiden kehittäjien ja Bitcoin Core GitHub -tietokantaa ylläpitävien toimittajien hyväksymiä: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun ja Ruben Somsen. On kuitenkin tärkeää ymmärtää, että näiden henkilöiden rooli BIP:n muokkaamisessa ei tarkoita, että he hallitsevat Bitcoinia. Jos joku ehdottaa parannusta, jota ei hyväksytä virallisessa BIP-kehyksessä, hän voi silti esittää sen suoraan Bitcoin-yhteisölle tai jopa luoda haaran, joka sisältää hänen muutoksensa. BIP-prosessin etuna on sen muodollisuus ja keskittäminen, jotka helpottavat keskustelua Bitcoin-käyttäjien välisen hajaannuksen välttämiseksi ja pyrkivät toteuttamaan päivitykset yhteisymmärryksessä. Loppujen lopuksi taloudellisen enemmistön periaate määrää vallan dynamiikan protokollan sisällä.

Rajatarkastusohjelmat luokitellaan kolmeen pääryhmään:


- Standardien seurannan raja-asemat*: Koskevat muutoksia, jotka vaikuttavat suoraan Bitcoin-toteutuksiin, kuten transaktio- ja lohkojen validointisääntöihin;
- Tiedotusrajat*: Antavat tietoja tai suosituksia ehdottamatta suoria muutoksia pöytäkirjaan;
- Käsittele rajatarkastusohjelmat*: Kuvaile muutokset Bitcoinia ympäröivissä menettelyissä, kuten hallintoprosesseissa.

Standardien seurantaan ja tiedottamiseen liittyvät rajatarkastusasemat luokitellaan myös 'kerroksen' mukaan:


- Konsensuskerros*: Tämän kerroksen BIP:t koskevat Bitcoinin konsensussääntöjä, kuten muutoksia lohkoihin tai transaktioiden validointisääntöihin. Nämä ehdotukset voivat olla joko pehmeitä haaroja (taaksepäin yhteensopivia muutoksia) tai kovia haaroja (ei taaksepäin yhteensopivia muutoksia). Esimerkiksi SegWitin ja Taprootin BIP:t kuuluvat tähän luokkaan;
- Vertaispalvelut*: Tämä kerros koskee Bitcoin-solmuverkon toimintaa eli sitä, miten solmut löytävät toisensa ja kommunikoivat keskenään Internetissä.
- API/RPC*: Tämän kerroksen BIP:t koskevat sovellusohjelmointirajapintoja (API) ja etäkäyttökutsuja (RPC), joiden avulla Bitcoin-ohjelmistot voivat olla vuorovaikutuksessa solmujen kanssa;
- Sovelluskerros*: Tämä kerros koskee Bitcoinin päälle rakennettuja sovelluksia. Tämän luokan rajatylittävissä hankkeissa käsitellään yleensä Bitcoin-lompakkostandardien tasolla tehtäviä muutoksia.

BIP:n lähettäminen alkaa idean hahmottelulla ja keskustelulla *Bitcoin-dev*-postituslistalla. Jos idea on lupaava, kirjoittaja laatii BIP:n tiettyä muotoa noudattaen ja lähettää sen Pull Request -pyynnöllä Core GitHub -tietovarastoon. Toimittajat tarkastavat tämän ehdotuksen varmistaakseen, että se täyttää kaikki kriteerit. BIP:n on oltava teknisesti toteuttamiskelpoinen, protokollan kannalta hyödyllinen, vaaditun muotoilun mukainen ja Bitcoinin filosofian mukainen. Jos BIP täyttää nämä ehdot, se liitetään virallisesti BIP:ien GitHub-arkistoon. Sen jälkeen sille annetaan numero. Tämän numeron päättää yleensä toimittaja, usein Luke Dashjr, ja se annetaan loogisesti: Samankaltaisia aiheita käsittelevät BIP:t saavat usein peräkkäiset numerot.

Rajatarkastusohjelmat käyvät läpi erilaisia vaiheita elinkaarensa aikana. Tämänhetkinen tila ilmoitetaan kunkin rajatarkastusaseman otsikossa:


- Luonnos: Ehdotus on vielä luonnos- ja keskusteluvaiheessa;
- Ehdotettu: Rajatarkkailuraportti katsotaan valmiiksi ja yhteisön tarkasteltavaksi;
- Lykätty: Mestari tai päätoimittaja siirtää rajatarkastuksen myöhempään ajankohtaan;
- Hylätty: Rajatarkastusasema luokitellaan hylätyksi, jos siinä ei ole ollut toimintaa kolmeen vuoteen. Sen laatija voi halutessaan jatkaa sitä myöhemmin, jolloin se voi palata luonnosvaiheeseen;
- Peruutettu: Laatija on peruuttanut rajatarkastusaseman;
- Lopullinen: BIP on hyväksytty ja otettu laajalti käyttöön Bitcoinissa;
- Aktiivinen: Ainoastaan prosessin rajatarkastusasemien osalta tämä tila annetaan, kun tietty yhteisymmärrys on saavutettu;
- Korvattu / vanhentunut: Rajatarkastusasema ei ole enää sovellettavissa tai se on korvattu uudemmalla ehdotuksella, joka tekee sen tarpeettomaksi.

![](../../dictionnaire/assets/25.webp)

> ► *BIP on lyhenne sanoista "Bitcoin Improvement Proposal". Ranskaksi se voidaan kääntää "Proposition d'amélioration de Bitcoin". Useimmissa ranskankielisissä teksteissä lyhennettä "BIP" käytetään kuitenkin suoraan yleisenä substantiivina, joskus feminiinissä, joskus maskuliinissa.*