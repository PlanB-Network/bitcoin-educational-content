---
termi: BIP
---

Lyhenne sanoista "Bitcoin Improvement Proposal" eli Bitcoinin parannusehdotus. Bitcoin Improvement Proposal (BIP) on muodollinen prosessi ehdottaa ja dokumentoida parannuksia sekä muutoksia Bitcoin-protokollaan ja sen standardeihin. Koska Bitcoinilla ei ole keskitettyä tahoa päätöksenteolle päivityksistä, BIP:t mahdollistavat yhteisön ehdottaa, keskustella ja toteuttaa parannuksia rakenteellisella ja läpinäkyvällä tavalla. Jokainen BIP yksilöi ehdotetun parannuksen tavoitteet, perustelut, mahdolliset yhteensopivuusvaikutukset sekä edut ja haitat. BIP:t voivat olla kenen tahansa yhteisön jäsenen kirjoittamia, mutta ne on hyväksyttävä muiden kehittäjien ja Bitcoin Core GitHub-tietokannan ylläpitäjien toimesta: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun ja Ruben Somsen. On kuitenkin tärkeää ymmärtää, että näiden henkilöiden rooli BIP:ien muokkaajina ei tarkoita, että he hallitsisivat Bitcoinia. Jos joku ehdottaa parannusta, jota ei hyväksytä virallisessa BIP-rakenteessa, hän voi silti esittää sen suoraan Bitcoin-yhteisölle tai jopa luoda haaran, joka sisältää hänen muutoksensa. BIP-prosessin etu on sen muodollisuus ja keskitetty lähestymistapa, jotka helpottavat keskustelua Bitcoin-käyttäjien jakautumisen välttämiseksi, pyrkien toteuttamaan päivityksiä yhteisymmärryksessä. Lopulta taloudellinen enemmistö määrittää protokollan voimadynamiikan.

BIP:t luokitellaan kolmeen pääkategoriaan:
* *Standards Track BIPs*: Koskevat muutoksia, jotka vaikuttavat suoraan Bitcoinin toteutuksiin, kuten transaktioiden ja lohkojen validointisääntöihin;
* *Informational BIPs*: Tarjoavat tietoa tai suosituksia ilman suoria muutosehdotuksia protokollaan;
* *Process BIPs*: Kuvaavat muutoksia Bitcoinin ympärillä oleviin prosesseihin, kuten hallintoprosesseihin.

Standards Track ja Informational BIP:t luokitellaan myös "Kerroksen" mukaan:
* *Consensus Layer*: BIP:t tässä kerroksessa koskevat Bitcoinin konsensus-sääntöjä, kuten muutoksia lohko- tai transaktiovalidointisääntöihin. Nämä ehdotukset voivat olla joko pehmeitä haarautumisia (taaksepäin yhteensopivia muutoksia) tai kovia haarautumisia (ei-taaksepäin yhteensopivia muutoksia). Esimerkiksi SegWitin ja Taprootin BIP:t kuuluvat tähän kategoriaan;
* *Peer Services*: Tämä kerros koskee Bitcoin-solmujen verkon toimintaa, eli sitä, miten solmut löytävät ja kommunikoivat keskenään Internetissä.
* *API/RPC*: Tämän kerroksen BIP:t koskevat Application Programming Interfaces (API) ja Remote Procedure Calls (RPC), jotka mahdollistavat Bitcoin-ohjelmiston vuorovaikutuksen solmujen kanssa;
* *Applications Layer*: Tämä kerros liittyy Bitcoinin päälle rakennettuihin sovelluksiin. Tämän kategorian BIP:t käsittelevät yleensä muutoksia Bitcoin-lompakoiden standardien tasolla.

BIP:n esittämisprosessi alkaa idean konseptualisoinnista ja keskustelusta *Bitcoin-dev* postituslistalla. Jos idea on lupaava, tekijä laatii BIP:n tietyssä muodossa ja esittää sen Pull Requestin kautta Core GitHub-repositorioon. Toimittajat tarkistavat ehdotuksen varmistaakseen, että se täyttää kaikki kriteerit. BIP:n on oltava teknisesti toteutettavissa, hyödyllinen protokollalle, noudatettava vaadittua muotoilua ja oltava Bitcoinin filosofian mukainen. Jos BIP täyttää nämä ehdot, se integroidaan virallisesti BIP:ien GitHub-repositorioon. Sille annetaan sitten numero. Tämän numeron päättää yleensä toimittaja, usein Luke Dashjr, ja se annetaan loogisesti: samankaltaisia aiheita käsittelevät BIP:t saavat usein peräkkäisiä numeroita.

BIP:t käyvät läpi eri tiloja elinkaarensa aikana. Nykyinen tila on määritelty kunkin BIP:n otsikossa:
* Luonnos: Ehdotus on vielä luonnostelun ja keskustelun vaiheessa;
* Ehdotettu: BIP katsotaan valmiiksi ja se on yhteisön arvioitavissa;
* Lykätty: BIP on pantu toistaiseksi syrjään joko aloitteen tekijän tai toimittajan toimesta;
* Hylätty: BIP luokitellaan hylätyksi, jos sille ei ole osoitettu toimintaa 3 vuoteen. Sen tekijä voi päättää jatkaa sitä myöhemmin, mikä mahdollistaisi sen paluun luonnosvaiheeseen;
* Peruutettu: BIP on peruutettu sen tekijän toimesta;
* Lopullinen: BIP on hyväksytty ja laajalti toteutettu Bitcoinissa;
* Aktiivinen: Vain prosessi-BIPeille, tälle statukselle annetaan merkintä, kun tietty yhteisymmärrys on saavutettu;
* Korvattu / Vanhentunut: BIP ei ole enää sovellettavissa tai se on korvattu uudemmalla ehdotuksella, joka tekee siitä tarpeettoman.

![](../../dictionnaire/assets/25.png)

> ► *BIP on lyhenne sanoista "Bitcoin Improvement Proposal". Suomeksi sen voi kääntää "Bitcoinin parannusehdotukseksi". Kuitenkin useimmissa suomenkielisissä teksteissä käytetään suoraan lyhennettä "BIP" yleisnimenä.*