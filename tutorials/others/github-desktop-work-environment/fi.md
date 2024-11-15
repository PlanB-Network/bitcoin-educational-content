---
name: GitHub Desktop
description: Miten pystytät paikallisen työympäristösi?
---
![github](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä mahdollistaa kenen tahansa osallistumisen alustan rikastuttamiseen. Osallistumiset voivat ottaa eri muotoja: olemassa olevien tekstien korjaaminen ja oikoluku, kääntäminen toisille kielille, tiedon päivittäminen tai uusien opastusten luominen, joita ei vielä ole sivustollamme.

Jos haluat osallistua PlanB-verkkoon, sinun on käytettävä GitHubia ehdottaaksesi muutoksia. Tähän on kaksi vaihtoehtoa:
- **Osallistu suoraan GitHubin verkkokäyttöliittymän kautta**: Tämä on yksinkertaisin menetelmä. Jos olet aloittelija tai aiot tehdä vain muutamia pieniä muutoksia, tämä vaihtoehto on todennäköisesti paras sinulle;
- **Osallistu paikallisesti käyttäen Git**: Tämä menetelmä sopii paremmin, jos aiot tehdä säännöllisiä tai merkittäviä panostuksia PlanB-verkkoon. Vaikka paikallisen Git-ympäristön pystyttäminen tietokoneellesi saattaa aluksi vaikuttaa monimutkaiselta, tämä lähestymistapa on tehokkaampi pitkällä aikavälillä. Se mahdollistaa joustavamman muutosten hallinnan. Jos olet uusi tässä, älä huoli, **selitämme koko prosessin ympäristösi pystyttämiseksi tässä opastuksessa** (lupaus, sinun ei tarvitse kirjoittaa yhtään komentoriviä ^^).

Jos sinulla ei ole aavistustakaan, mikä GitHub on, tai jos haluat oppia lisää Gitin ja GitHubin teknisistä termeistä, suosittelen, että luet johdantoartikkelimme tutustuaksesi näihin käsitteisiin.

https://planb.network/tutorials/others/basics-of-github



- Aloittaaksesi tarvitset tietenkin GitHub-tilin. Jos sinulla on jo tili, voit kirjautua sisään, muussa tapauksessa voit käyttää opastustamme uuden tilin luomiseen.

https://planb.network/tutorials/others/create-github-account



## Vaihe 1: Asenna GitHub Desktop

- Mene osoitteeseen https://desktop.github.com/ ladataksesi GitHub Desktop -ohjelmiston. Tämä ohjelmisto mahdollistaa helpon vuorovaikutuksen GitHubin kanssa ilman terminaalin käyttöä:
![github-desktop](assets/1.webp)
- Kun käynnistät ohjelmiston ensimmäisen kerran, sinua pyydetään yhdistämään GitHub-tilisi. Tee tämä napsauttamalla `Kirjaudu sisään GitHub.comiin`:
![github-desktop](assets/2.webp)
- Selaimessasi avautuu todennussivu. Anna sähköpostiosoitteesi ja salasana, jotka valitsit tilisi luomisen yhteydessä, ja napsauta sitten `Kirjaudu sisään` -painiketta:
![github-desktop](assets/3.webp)
- Napsauta `Valtuuta työpöytä` vahvistaaksesi yhteyden tilisi ja ohjelmiston välillä:
![github-desktop](assets/4.webp)
- Sinut ohjataan automaattisesti takaisin GitHub Desktop -ohjelmistoon. Napsauta `Valmis`: ![github-desktop](assets/5.webp)
- Jos olet juuri luonut GitHub-tilisi, sinut ohjataan sivulle, joka ilmoittaa, ettet ole vielä luonut yhtään varastoa. Tässä vaiheessa jätä GitHub Desktop -ohjelmisto hetkeksi sivuun; palaamme siihen myöhemmin: ![github-desktop](assets/6.webp)

## Vaihe 2: Asenna Obsidian

Siirrytään asentamaan kirjoitusohjelmistoa. Tässä sinulla on useita vaihtoehtoja. Tarvitset ohjelmiston, joka tukee Markdown-tiedostojen muokkaamista, sillä PlanB-verkko käyttää tätä muotoa tekstitiedostoissaan varastossaan.
On olemassa lukuisia ohjelmistoja, jotka on erikoistunut Markdown-tiedostojen muokkaamiseen, kuten Typora, joka on suunniteltu erityisesti kirjoittamiseen. Vaikka se ei ole ihanteellinen, on myös mahdollista valita koodieditori, kuten Visual Studio Code (VSC) tai Sublime Text. Kirjoittajana kuitenkin suosin Obsidian-ohjelmiston käyttöä. Katsotaan yhdessä, miten asentaa ja aloittaa sen käyttö.
- Siirry osoitteeseen https://obsidian.md/download ja lataa ohjelmisto: ![github-desktop](assets/7.webp)
- Asenna Obsidian, käynnistä ohjelmisto, valitse kielesi ja klikkaa sitten `Quick Start`: ![github-desktop](assets/8.webp)
- Saavut Obsidian-ohjelmistoon. Tällä hetkellä sinulla ei ole avoinna yhtään tiedostoa: ![github-desktop](assets/9.webp)

## Vaihe 3: Forkkaa PlanB Network -repositorio

- Siirry PlanB Network -datan repositorioon seuraavassa osoitteessa: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Tältä sivulta, klikkaa `Fork`-nappia ikkunan oikeassa yläkulmassa: ![github-desktop](assets/11.webp)
- Luontimenussa voit jättää oletusasetukset. Varmista, että `Copy the dev branch only` -ruutu on valittu, ja klikkaa sitten `Create fork` -nappia: ![github-desktop](assets/12.webp)
- Saavut sitten omaan forkkiisi PlanB Network -repositoriosta: ![github-desktop](assets/13.webp)
Tämä forkki muodostaa erillisen repositorion alkuperäisestä, vaikka se tällä hetkellä sisältääkin samat tiedot. Työskentelet nyt tässä uudessa repositoriossa.

Olemme tavallaan tehneet kopion PlanB Network -lähderepositoriosta. Forkkisi (kopio) ja alkuperäinen repositorio kehittyvät nyt toisistaan riippumatta. Alkuperäisessä repositoriossa muut avustajat voivat lisätä uusia tietoja, kun taas sinä, omassa forkissasi, jatkat omilla muutoksillasi.
Näiden kahden repositorion johdonmukaisuuden ylläpitämiseksi on tarpeen synkronoida ne ajoittain, jotta ne saavat samat tiedot. Lähettääksesi muutoksesi lähderepositorioon, käytät niin kutsuttua **Pull Request** -toimintoa. Ja integroidaksesi muutoksia lähderepositoriosta forkkiisi, käytät GitHubin web-käyttöliittymässä saatavilla olevaa **Sync fork** -komentoa.
![github-desktop](assets/14.webp)

## Vaihe 4: Kloonaa forkki

- Palaa GitHub Desktop -ohjelmistoon. Tähän mennessä forkisi pitäisi näkyä `Your repositories` -osiossa. Jos et näe sitä heti, käytä kaksoisnuolinappia päivittääksesi listan. Kun forkisi ilmestyy, klikkaa sitä valitaksesi sen:
![github-desktop](assets/15.webp)
- Klikkaa sitten sinistä nappia: `Clone [käyttäjänimi]/bitcoin-educational-content`:
![github-desktop](assets/16.webp)
- Säilytä oletuspolku. Vahvistaaksesi, klikkaa sinistä `Clone`-nappia:
![github-desktop](assets/17.webp)
- Odota, kun GitHub Desktop kloonaa forkisi paikallisesti:
![github-desktop](assets/18.webp)
- Kloonattuasi varaston, ohjelmisto tarjoaa sinulle kaksi vaihtoehtoa. Sinun tulee valita ensimmäinen: `Osallistu pääprojektiin`. Tämä valinta mahdollistaa tulevan työsi esittämisen panoksena pääprojektille (`PlanB-Network/bitcoin-educational-content`), eikä pelkästään henkilökohtaisen haarasi (`[käyttäjänimi]/bitcoin-educational-content`) muokkauksena. Kun vaihtoehto on valittu, klikkaa `Jatka`: ![github-desktop](assets/19.webp)
- GitHub Desktopisi on nyt oikein konfiguroitu. Nyt voit jättää ohjelmiston auki taustalle seurataksesi tekemiämme muutoksia.
![github-desktop](assets/20.webp)
Mitä olemme saavuttaneet tässä vaiheessa, on paikallisen kopion luominen varastostasi, joka on isännöity GitHubissa. Muistutuksena, tämä varasto on haarautuma PlanB Networkin lähdevarastosta. Voit tehdä muutoksia tähän paikalliseen kopioon, kuten lisätä tutoriaaleja, käännöksiä tai korjauksia. Kun nämä muutokset on tehty, käytät **Push origin** -komentoa lähettääksesi paikalliset muutoksesi GitHubissa isännöityyn haarahasi.

Voit myös hakea muutoksia haarasta, esimerkiksi synkronoinnin aikana PlanB Networkin varaston kanssa. Tätä varten käytät **Fetch origin** -komentoa ladataksesi muutokset paikalliseen kopioosi (kloniisi), ja sitten **Pull origin** -komentoa yhdistääksesi ne työhösi. Tämä mahdollistaa pysymisen ajan tasalla projektin viimeisimmistä kehityksistä samalla tehokkaasti osallistuen.

![github-desktop](assets/21.webp)
## Vaihe 5: Luo uusi Obsidian-vaultti

- Avaa Obsidian-ohjelmisto ja klikkaa pientä vaultti-ikonia ikkunan vasemmassa alakulmassa:
![github-desktop](assets/22.webp)
- Klikkaa `Avaa`-painiketta avataksesi olemassa olevan kansion vaulttina: ![github-desktop](assets/23.webp)
- Tiedostonhallintasi avautuu. Sinun tulee paikantaa ja valita kansio nimeltä `GitHub`, joka pitäisi löytyä `Dokumentit`-kansiostasi tiedostojesi joukosta. Tämä polku vastaa sitä, jonka asetit vaiheessa 4. Valittuasi kansion, vahvista sen valinta. Vaulttisi luominen Obsidianissa käynnistyy sitten ohjelmiston uudella sivulla:

![github-desktop](assets/24.webp)
-> **Huomio**, on tärkeää olla valitsematta `bitcoin-educational-content`-kansiota luodessasi uutta vaulttia Obsidianissa. Sen sijaan, valitse yläkansio, `GitHub`. Jos valitset `bitcoin-educational-content`-kansion, konfiguraatiokansio `.obsidian`, joka sisältää paikalliset Obsidian-asetuksesi, integroituu automaattisesti varastoon. Haluamme välttää tämän, sillä Obsidian-konfiguraatioidesi siirtäminen PlanB Networkin varastoon ei ole tarpeellista. Vaihtoehtona on lisätä `.obsidian`-kansio `.gitignore`-tiedostoon, mutta tämä menetelmä muokkaisi myös lähdevaraston `.gitignore`-tiedostoa, mikä ei ole toivottavaa.

- Ikkunan vasemmalla puolella voit nähdä tiedostopuun eri GitHub-varastoistasi, jotka on kloonattu paikallisesti.
- Klikkaamalla kansioitten nimien vieressä olevia nuolia, voit laajentaa ne päästäksesi käsiksi varastojen alikansioihin ja niiden dokumentteihin:
![github-desktop](assets/25.webp)
- Älä unohda asettaa Obsidiania tummaan tilaan: "Valo houkuttelee ötököitä" ;)

## Vaihe 6: Asenna koodieditori
Suurin osa muokkauksistasi kohdistuu Markdown-muotoisiin tiedostoihin (`.md`). Näiden asiakirjojen muokkaamiseen voit käyttää Obsidian-ohjelmistoa, josta keskustelimme aiemmin. PlanB Network käyttää kuitenkin myös muita tiedostomuotoja, ja sinun on muokattava joitakin niistä.

Esimerkiksi uuden oppaan luomisen yhteydessä sinun on luotava YAML (`.yml`) tiedosto syöttääksesi oppaasi tagit, otsikon ja opettaja-ID:si. Obsidian ei tarjoa mahdollisuutta tällaisten tiedostojen muokkaamiseen, joten tarvitset koodieditorin.

Tähän on saatavilla useita vaihtoehtoja. Vaikka tietokoneesi vakionotepad-ohjelmaa voidaan käyttää näihin muokkauksiin, tämä ratkaisu ei ole ihanteellinen siistiin työhön. Suosittelen valitsemaan tähän tarkoitukseen erityisesti suunniteltua ohjelmistoa, kuten [VS Code](https://code.visualstudio.com/download) tai [Sublime Text](https://www.sublimetext.com/download). Sublime Text on erityisen kevyt, joten se on enemmän kuin riittävä tarpeisiimme.
- Asenna jompikumpi näistä ohjelmista ja pidä se sivussa tulevia muokkauksiasi varten. ![github-desktop](assets/26.webp)
Onnittelut! Työympäristösi on nyt valmis osallistumaan PlanB Networkiin. Voit nyt tutustua muihin erityisoppaisiimme kunkin panostustyypin (kääntäminen, oikoluku, kirjoittaminen.

https://planb.network/tutorials/others

..) osalta.
