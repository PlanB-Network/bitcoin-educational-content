---
name: PlanB Professor
description: Miten lisätä professoriprofiilisi PlanB-verkostoon?
---
![cover](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä mahdollistaa kenen tahansa osallistumisen alustan rikastuttamiseen. Osallistumisen muodot voivat olla moninaisia: olemassa olevien tekstien korjaaminen ja oikoluku, koulutuskurssien tuottaminen, kääntäminen toisille kielille, tiedon päivittäminen tai uusien opetusohjelmien luominen, joita ei vielä ole sivustollamme.

Jos haluat lisätä uuden täydellisen opetusohjelman tai kurssin PlanB-verkostoon, sinun on luotava professoriprofiilisi. Tämä mahdollistaa sinun saada asianmukaiset kreditoinnit tuottamastasi sisällöstä verkkosivustolla.
![tutorial](assets/1.webp)
Jos olet aiemmin osallistunut PlanB-verkoston toimintaan, sinulla on todennäköisesti jo avustajan tunnus. Löydät sen professorikansiostasi, joka on saatavilla [tällä sivulla](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors). Jos näin on, voit jättää tämän opetusohjelman väliin ja aloittaa suoraan osallistumisen.
![tutorial](assets/2.webp)

Tutustutaan yhdessä, miten lisätä uusi professori tässä opetusohjelmassa!

## Edellytykset

**Opetusohjelman seuraamiseen tarvittava ohjelmisto:**
- [GitHub Desktop](https://desktop.github.com/)
- Koodieditori ([VSC](https://code.visualstudio.com/) tai [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/3.webp)
**Edellytykset ennen opetusohjelman aloittamista:**
- [GitHub-tilin](https://github.com/signup) omistaminen.
- Forkin omistaminen [PlanB Networkin lähdekoodirepositoriosta](https://github.com/PlanB-Network/bitcoin-educational-content).

**Jos tarvitset apua näiden edellytysten saavuttamisessa, muut opetusohjelmani opastavat sinua:**
**[Gitin ja GitHubin ymmärtäminen](https://planb.network/tutorials/others/basics-of-github)**
**[GitHub-tilin luominen](https://planb.network/tutorials/others/create-github-account)**
**[Työympäristösi pystyttäminen](https://planb.network/tutorials/others/github-desktop-work-environment)**

## Kuinka luoda uusi professoriprofiili?

- Avaa selain ja siirry forkisi sivulle PlanB-repositoriossa. Forkkisi URL näyttää tältä: `https://github.com/[käyttäjänimi]/bitcoin-educational-content`
![tutorial](assets/4.webp)
- Varmista, että olet päähaarassa `dev` ja klikkaa `Sync fork` -painiketta. Jos forkisi ei ole ajan tasalla, GitHub tarjoaa haarasi päivittämistä. Suorita tämä synkronointi.

- Jos haarasi on toisaalta jo ajan tasalla, GitHub ilmoittaa sinulle:
![tutorial](assets/5.webp)- Avaa GitHub Desktop ja varmista, että forkisi on oikein valittuna ikkunan vasemmassa yläkulmassa:
![tutorial](assets/6.webp)
- Klikkaa `Fetch origin` -painiketta.

- Jos paikallinen repositoriosi on jo ajan tasalla, GitHub Desktop ei ehdota lisätoimia. Muussa tapauksessa `Pull origin` -vaihtoehto ilmestyy. Klikkaa tätä painiketta päivittääksesi paikallisen repositoriosi:
![tutorial](assets/7.webp)
- Varmista, että olet päähaarassa `dev`:
![tutorial](assets/8.webp)
- Klikkaa tätä haaraa, sitten klikkaa `New Branch` -painiketta:
![tutorial](assets/9.webp)
- Varmista, että uusi haara perustuu lähtökohtaiseen varastoon, nimittäin `PlanB-Network/bitcoin-educational-content`.
- Nimeä haara tavalla, joka tekee sen tarkoituksesta selvän, käyttäen väliviivoja erottamaan sanat. Koska tämä haara on tarkoitettu professorin profiilin lisäämiseen, esimerkkinimi voisi olla: `add-professor-[sinun-nimesi]`. Nimen syöttämisen jälkeen klikkaa `Create branch` vahvistaaksesi haaran luomisen:
![opas](assets/10.webp)
- Nyt klikkaa `Publish branch` -painiketta tallentaaksesi uuden työhaaran online-forkiisi GitHubissa:
![opas](assets/11.webp)
- Tässä vaiheessa GitHub Desktopissa sinun tulisi olla uudella haarallasi. Tämä tarkoittaa, että kaikki tietokoneellasi paikallisesti tehdyt muutokset tallennetaan yksinomaan tälle tietylle haaralle. Niin kauan kuin tämä haara pysyy valittuna GitHub Desktopissa, koneellasi paikallisesti näkyvät tiedostot vastaavat tämän haaran tiedostoja (`add-professor-sinun-nimesi`), eivätkä päähaaran (`dev`) tiedostoja:
![opas](assets/12.webp)
- Professorin profiilisi lisäämiseksi avaa tiedostonhallintasi ja navigoi paikalliseen varastoosi, `professors`-kansioon. Löydät sen polusta: `\GitHub\bitcoin-educational-content\professors`.

- Tässä kansiossa, luo uusi kansio nimelläsi tai nimimerkilläsi. Varmista, että kansion nimessä ei ole välilyöntejä. Jos siis nimesi on "Loic Pandul" eikä yksikään toinen professori käytä tätä nimeä, luotava kansio nimetään `loic-pandul`:
![opas](assets/13.webp)
- Helpottaaksesi asioita, voit jo kopioida ja liittää kaikki asiakirjat toisen professorin kansiosta omaan kansioosi. Sen jälkeen jatkamme näiden asiakirjojen muokkaamista mukauttaaksemme ne profiilisi mukaan:
![opas](assets/14.webp)
- Aloita siirtymällä `assets`-kansioon. Poista aiemmin kopioimasi professorin profiilikuva ja korvaa se omalla profiilikuvallasi. On ehdottoman tärkeää, että tämä kuva on `.webp`-muodossa ja että sen tiedostonimi on `profile`, antaen täydellisen tiedostonimen `profile.webp`. Ole tietoinen, että tämä kuva julkaistaan Internetissä ja on kaikkien saavutettavissa: ![opas](assets/15.webp)
- Seuraavaksi avaa `professor.yml`-tiedosto koodieditorillasi (esimerkiksi VSC tai Sublime Text). Saavut kopioituun tiedostoon olemassa olevasta professorista:
![opas](assets/16.webp)
- Sinun täytyy sen jälkeen päivittää olemassa olevat tiedot omillasi:
	- **name:** kirjoita nimesi tai nimimerkkisi;
	- **links:** ilmoita sosiaalisen median tilisi, kuten Twitter ja Nostr, sekä henkilökohtaisen verkkosivustosi URL (valinnainen);
	- **affiliation:** mainitse yrityksen nimi, joka sinua työllistää (valinnainen);
	- **tags:** määrittele erikoisalaasi seuraavasta listasta, tietäen että voit lisätä omia teemojasi. Kuitenkin, varmista että tagien määrä on enintään 4 varmistaaksesi hyvän käyttöliittymän:
	    - yksityisyys,
	    - kryptografia,
	    - bitcoin,
	    - louhinta,
	    - salamaverkko,
	    - talous,
	    - historia,
	    - kauppiaat,
	    - turvallisuus,
	    - ...
	- **tips:** tarjoa Lightning-osoitteesi lahjoituksia varten, jotta tulevien oppaidesi lukijat voivat lähettää sinulle joitakin satseja (valinnainen);
	- **company:** jos omistat yhden, ilmoita yrityksesi nimi (valinnainen). Sinun täytyy sen jälkeen päivittää olemassa olevat tiedot omillasi:
![opas](assets/17.webp)- Sinun tulee myös muokata `contributor-id` tunnistetta. Tämä tunniste käytetään tunnistamaan sinut verkkosivustolla, mutta sitä ei julkaista GitHubin ulkopuolella. Voit vapaasti valita minkä tahansa kahden sanan yhdistelmän, viitaten [englanninkieliseen 2048 sanan listaan BIP39:stä](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Älä unohda lisätä viivaa kahden valitun sanan välille. Esimerkiksi tässä valitsin `crazy-cactus`:
![opas](assets/18.webp)
- Kun olet saanut `professor.yml` dokumentin muokkauksen valmiiksi, klikkaa `File > Save` tallentaaksesi tiedoston. Voit sen jälkeen poistua koodieditoristasi:
![opas](assets/19.webp)
- Professori-kansiossasi voit poistaa dokumentit, jotka on kirjoitettu kielillä, jotka eivät koske sinua, ja jotka alun perin kopioitiin toiselta professorilta. Säilytä vain tiedosto, joka vastaa äidinkieltäsi. Esimerkiksi minun tapauksessani säilytin vain `fr.yml` tiedoston, koska kielesi on ranska: ![opas](assets/20.webp)
- Kaksoisklikkaa tätä tiedostoa avataksesi sen koodieditorissasi.

- Tässä tiedostossa sinulla on mahdollisuus kirjoittaa koko elämäkertasi `bio` osioon ja yhteenveto tai tiivis otsikko `short_bio` alle:
![opas](assets/21.webp)
- Tallennettuasi `fr.yml` dokumentin, sinun tarvitsee luoda kopio tästä tiedostosta seuraaville kahdeksalle kielelle:
    - Saksa (DE);
    - Englanti (EN);
    - Ranska (FR);
    - Espanja (ES);
    - Italia (IT);
    - Portugali (PT);
    - Japani (JA);
    - Vietnam (VI).

- Jatka kopioimalla ja liittämällä alkuperäinen tiedosto, ja käännä jokainen asiakirja vastaavalle kielelle. Jos olet taitava kielessä, voit suorittaa käännöksen manuaalisesti. Muussa tapauksessa voit vapaasti käyttää automaattista käännöstyökalua tai chatbottia:
![opas](assets/22.webp)
- Jos haluat, voit myös säilyttää elämäkerran vain äidinkielelläsi; me hoidamme käännöksen jättämäsi vetopyynnön jälkeen.

- Professori-kansiosi tulisi näyttää tältä:
![opas](assets/23.webp)
```plaintext
etunimi-sukunimi/
├── fr.yml
├── it.yml
├── es.yml
├── en.yml
├── de.yml
├── pt.yml
├── ja.yml
├── vi.yml
├── professor.yml
└── assets/
    └── profile.webp
```
- Palaa nyt GitHub Desktopiin.
- Ikkunasi vasemmalla puolella sinun tulisi nähdä kaikki dokumentteihin tehdyt muutokset, jotka koskevat omaa haaraasi. Varmista, että nämä muutokset ovat oikein:
![opas](assets/24.webp)
- Jos muutokset vaikuttavat sinusta oikeilta, lisää otsikko commitillesi. Commit on tallennus haaraan tehtyihin muutoksiin, johon liittyy kuvaileva viesti, joka mahdollistaa projektin kehityksen seuraamisen ajan myötä.
- Kun otsikko on syötetty, paina sinistä `Commit to [branchisi]` nappia vahvistaaksesi nämä muutokset:
![opas](assets/25.webp)
- Sen jälkeen klikkaa `Push origin` nappia. Tämä lähettää commitisi haarasi kautta forkillesi:
![opas](assets/26.webp)
- Jos olet saanut muutokset tässä haarassa valmiiksi, klikkaa nyt `Preview Pull Request` nappia:
![opas](assets/27.webp)
- Voit tarkistaa vielä viimeisen kerran, että muutoksesi ovat oikein, ja sitten klikata `Create pull request` -painiketta: ![opas](assets/28.webp)- Sinut ohjataan automaattisesti selaimessasi GitHubiin Pull Requestin valmistelusivulle. Pull Request on pyyntö muutosten integroimiseksi haarastasi PlanB Network -repositorion päähaaraan, mikä mahdollistaa muutosten tarkastelun ja keskustelun ennen niiden yhdistämistä: ![opas](assets/29.webp)
- Tällä valmistelusivulla anna otsikko, joka lyhyesti tiivistää muutokset, jotka haluat yhdistää lähde-repositorioon.
- Lisää lyhyt kommentti kuvaamaan näitä muutoksia.
- Näiden vaiheiden suorittamisen jälkeen klikkaa vihreää `Create pull request` -painiketta vahvistaaksesi yhdistämisen pyynnön: ![opas](assets/30.webp)
- PR:si on sen jälkeen näkyvissä PlanB Networkin päärepositorion `Pull Request` -välilehdellä. Sinun tarvitsee nyt vain odottaa, kunnes ylläpitäjä ottaa sinuun yhteyttä vahvistaakseen muutostesi yhdistämisen tai pyytääkseen mahdollisia lisämuutoksia: ![opas](assets/31.webp)
- PR:si yhdistämisen jälkeen päähaaraan suositellaan työhaaran (`add-professor-your-name`) poistamista, jotta historiasi pysyy siistinä haarassasi. GitHub tarjoaa sinulle automaattisesti tämän vaihtoehdon PR-sivullasi: ![opas](assets/32.webp)
- GitHub Desktop -ohjelmistossa voit vaihtaa takaisin haarasi päähaaraan (`dev`): ![opas](assets/8.webp)
- Jos haluat tehdä muutoksia profiiliisi sen jälkeen, kun olet jo lähettänyt PR:si, menettely riippuu PR:si nykyisestä tilasta:
	- Jos PR:si on edelleen avoinna eikä sitä ole vielä yhdistetty, tee muutokset paikallisesti pysyen samalla haaralla. Kun muutokset on viimeistelty, käytä `Push origin` -painiketta lisätäksesi uuden commitin vielä avoimeen PR:iisi;
	- Jos PR:si on jo yhdistetty päähaaraan, sinun on aloitettava prosessi alusta luomalla uusi haara ja lähettämällä uusi PR. Varmista, että paikallinen repositoriosi on synkronoitu PlanB Networkin lähde-repositorion kanssa ennen jatkamista.
