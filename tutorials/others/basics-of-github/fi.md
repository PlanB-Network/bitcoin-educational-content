---
name: GitHubin perusteet
description: Gitin ja GitHubin perusteiden ymmärtäminen
---

![cover](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusmateriaaleja Bitcoinista, saatavilla mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, tarjoten kenelle tahansa mahdollisuuden osallistua alustan rikastuttamiseen. Osallistuminen voi ottaa eri muotoja: olemassa olevien tekstien korjaaminen ja oikoluku, kääntäminen toisille kielille, tiedon päivittäminen tai uusien opastusten luominen, joita ei vielä ole sivustollamme.

Jos haluat osallistua PlanB-verkostoon, sinun on käytettävä Gitia ja GitHubia. Jos nämä työkalut ovat sinulle tuntemattomia tai niiden toiminta vaikuttaa epäselvältä, älä huoli, tämä artikkeli on sinua varten! Käymme yhdessä läpi Gitin ja GitHubin perusteet sekä niihin liittyvän teknisen jargonin, jotta voit käyttää näitä työkaluja tehokkaasti jälkeenpäin.

## Mikä on Git?

Git on versionhallintajärjestelmä, joka on suunniteltu erityisesti ohjelmistoprojektien hallintaan. Linus Torvaldsin vuonna 2005 luoma Git on nopeasti tullut ohjelmistokehitysteollisuuden standardiksi versionhallinnassa. Mutta mitä se tarkalleen ottaen tarkoittaa?
![git](assets/1.webp)
Ydintasolla Git mahdollistaa kehittäjien seurata projektin lähdekoodiin ajan myötä tehtyjä muutoksia. Tämä tarkoittaa, että jokaisen koodissa tapahtuvan muutoksen myötä Git tallentaa projektista uuden version. Jos virhe tapahtuu tai kokeellinen ominaisuus ei toimi odotetusti, on mahdollista palata koodin aiempaan tilaan, ikään kuin tiedostojen aikakoneella.

Yksi Gitin keskeisistä ominaisuuksista on haarojen hallinta. Haara on eräänlainen rinnakkaislinja, jossa kehittäjät voivat työskennellä riippumattomasti projektin muusta osasta. Tämä helpottaa suuresti uusien ominaisuuksien lisäämistä tai virheiden korjaamista häiritsemättä pääkoodia. Kun muutokset on testattu ja hyväksytty, ne voidaan yhdistää päähaaraan.

Yksi Gitin erityispiirteistä on sen kyky toimia hajautetusti. Jokaisella kehittäjällä on täydellinen kopio projektista omalla tietokoneensa kovalevyllä, mikä mahdollistaa työskentelyn offline-tilassa ja muutosten yhdistämisen myöhemmin, kun Internet-yhteys on saatavilla. Tämä vähentää ristiriitojen riskiä ja mahdollistaa useiden kehittäjien samanaikaisen työskentelyn samassa projektissa törmäämättä toisiinsa.
Alun perin Git oli suunniteltu ensisijaisesti ohjelmistokehitysprojekteja varten. Kuitenkin sitä voidaan käyttää myös sisällöntuotantoprojektien hallintaan. Sen sijaan, että tehtäisiin yhteistyötä koodin parissa, tehdään yhteistyötä tekstin parissa. Ja juuri tämä menetelmä on PlanB-verkoston valitsema sisällön hallintaan! Git helpottaa yhteistyötä kurssien ja opastusten kirjoittamisessa, sillä se mahdollistaa tarkkojen muutosten seurannan, tehokkaan versionhallinnan ja mahdollistaa myös sisällön tarkistamisen ja parantamisen muiden osallistujien toimesta.
## Mikä on GitHub?

GitHub on Git-versionhallintajärjestelmään perustuva lähdekoodin hallinta- ja isännöintialusta, josta juuri keskustelimme. Vuonna 2008 käynnistetty GitHub sai nopeasti suosiota ja on tullut kehittäjien keskuudessa välttämättömäksi viitepisteeksi maailmanlaajuisesti. Mutta miten GitHub eroaa Gitistä, ja miksi se on niin keskeinen sisällöntuotantomme kannalta?
![github](assets/2.webp)
Ensinnäkin on tärkeää ymmärtää, että GitHub on rakennettu Gitin päälle (josta keskustelimme edellisessä osiossa). Vaikka Git on työkalu, joka seuraa koodimuutoksia, GitHub on online-palvelu, joka isännöi, jakaa ja hallinnoi tätä koodia.

Kuvittele Git eräänlaisena lokikirjana, jota jokainen kehittäjä käyttää omalla tietokoneellaan tallentaakseen kaikki projektinsa muutokset. GitHub puolestaan on kuin julkinen kirjasto, jossa kaikki nämä lokikirjat voidaan jakaa, verrata ja yhdistää.
Gitin ja GitHubin välisen perustavanlaatuisen eron muodostaa niiden toiminto: Git on työkalu, jota jokainen kehittäjä käyttää paikallisesti koodiversioidensa hallintaan, kun taas GitHub on online-alusta, joka isännöi näitä versioita ja helpottaa yhteistyötä.
GitHub on paljon muutakin kuin pelkkä koodin isännöintipalvelu. Se on yhteistyöalusta, joka mahdollistaa kehittäjien tehokkaan yhteistyön. Ja todellakin, PlanB Network käyttää tätä alustaa isännöimään paitsi kaikkea verkkosivuston toimintaa ohjaavaa koodia, myös – ja tämä on meille kiinnostavaa – kaikkea sisältöä (oppaat, koulutukset, resurssit...).

## Joitakin teknisiä termejä

Gitin ja GitHubin parissa törmäät komentoihin ja ominaisuuksiin, joiden nimet saattavat vaikuttaa monimutkaisilta. Tässä viimeisessä osassa tarjoan yksinkertaisia määritelmiä ymmärtääksesi tekniset termit, joita saatat kohdata käyttäessäsi Gitia ja GitHubia:

- **Fetch origin:** Komento, joka noutaa viimeisimmät tiedot ja muutokset etävarastosta yhdistämättä niitä paikalliseen työhösi. Se päivittää paikallisen varastosi uusilla haaroilla ja sitoumuksilla, jotka ovat läsnä etävarastossa.

- **Pull origin:** Komento, joka noutaa päivitykset etävarastosta ja integroi ne välittömästi paikalliseen haaraasi synkronoidakseen sen. Tämä yhdistää haun ja yhdistämisen vaiheet yhdeksi komennoksi.
- **Sync Fork:** Ominaisuus GitHubissa, joka mahdollistaa projektisi haarukan päivittämisen uusimmilla muutoksilla lähdevarastosta. Tämä varmistaa, että projektisi kopio pysyy ajan tasalla pääkehityksen kanssa.
- **Push origin:** Komento, jota käytetään lähettämään paikalliset muutoksesi etävarastoon.

- **Pull Request:** Pyyntö, jonka avustaja lähettää ilmoittaakseen, että he ovat työntäneet muutoksia haaraan etävarastossa ja toivovat näiden muutosten tarkastelua ja mahdollisesti yhdistämistä varaston päähaaraan.

- **Commit:** Muutostesi tallentaminen. Sitoumus on kuin välitön tilannevedos työstäsi tietyllä hetkellä, mikä mahdollistaa muutoshistorian säilyttämisen. Jokaiseen sitoumukseen sisältyy kuvaileva viesti, joka selittää, mitä on muutettu.

- **Branch:** Varaston rinnakkaisversio, joka mahdollistaa muutosten tekemisen vaikuttamatta päähaaraan (usein kutsutaan "main" tai "master"). Haarat helpottavat uusien ominaisuuksien kehittämistä ja virheiden korjaamista ilman vakaiden koodien häirintäriskiä.

- **Merge:** Yhdistäminen koostuu muutosten integroimisesta yhdestä haarasta toiseen. Sitä käytetään esimerkiksi työhaaran muutosten lisäämiseen päähaaraan, mikä mahdollistaa eri panosten lisäämisen.

- **Fork:** Varaston haarauttaminen tarkoittaa kyseisen varaston kopion luomista omalle GitHub-tilillesi, mikä mahdollistaa projektin parissa työskentelyn vaikuttamatta alkuperäiseen varastoon. Haarautunut projekti voi joko lähteä omille teilleen ja muuttua alkuperäisestä projektista erilaiseksi, tai se voi säännöllisesti synkronoitua alkuperäisen projektin kanssa osallistuakseen siihen.

- **Clone:** Varaston kloonaaminen tarkoittaa paikallisen kopion tekemistä tietokoneellesi, mikä antaa sinulle pääsyn kaikkiin tiedostoihin ja historiaan. Tämä mahdollistaa projektin suoran työstämisen paikallisesti.

- **Repository:** Varastotila projektille GitHubissa. Varasto sisältää kaikki projektin tiedostot sekä kaikkien niihin tehtyjen muutosten historian. Se on GitHubissa säilytyksen ja yhteistyön perusta.

- **Issue:** Työkalu tehtävien ja vikojen seurantaan GitHubissa. Issuet mahdollistavat ongelmien raportoinnin, parannusehdotusten tekemisen tai uusien ominaisuuksien keskustelun. Kukin issue voidaan osoittaa, merkitä ja kommentoida.

Tämä lista ei selvästikään ole tyhjentävä. Gitin ja GitHubin erityisiä teknisiä termejä on monia muitakin. Kuitenkin tässä mainitut ovat pääasiallisia, joita kohtaat usein.
Tämän artikkelin lukemisen jälkeen on mahdollista, että jotkin Gitin ja GitHubin näkökohdat ovat edelleen epäselviä sinulle. Kannustan sinua aloittamaan näiden työkalujen käytön itse. Käytännön harjoittelu on usein paras tapa ymmärtää, miten kone toimii! Ja aloittaaksesi, voit tutustua näihin kahteen muuhun oppaaseen:
**[Luo GitHub-tilisi](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Aseta paikallinen ympäristösi valmiiksi osallistuaksesi PlanB Networkiin](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**