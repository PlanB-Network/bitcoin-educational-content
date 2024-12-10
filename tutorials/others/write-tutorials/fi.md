---
name: Osallistuminen - Oppaat
description: Kuinka ehdottaa uutta opasta PlanB-verkostoon?
---
![kansi](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä tarjoaa mahdollisuuden kenelle tahansa osallistua alustan rikastuttamiseen. Osallistumiset voivat ottaa eri muotoja: olemassa olevien tekstien korjaaminen ja oikoluku, kääntäminen toisille kielille, tiedon päivittäminen tai uusien oppaiden luominen, joita ei vielä ole sivustollamme.

Tässä oppaassa selitän, miten muokata PlanB-verkoston "Oppaat"-osioita. Jos haluat lisätä uuden oppaan tai parantaa olemassa olevaa, tämä artikkeli on sinua varten! Käymme yksityiskohtaisesti läpi, miten osallistua PlanB-verkostoon GitHubin kautta, samalla kun käytämme Obsidiania, kirjoitusvälinettä.

## Edellytykset

Osallistuaksesi PlanB-verkostoon sinulla on 3 vaihtoehtoa riippuen kokemustasostasi GitHubin kanssa:
1. **Kokeneet käyttäjät**: Jatka tuttuja menetelmiäsi ja tutustu tähän oppaaseen perehtyäksesi PlanB-repositorion rakenteeseen, erityisvaatimuksiin ja työnkulkuun.
2. **Aloittelijat, jotka ovat valmiita oppimaan**: Suosittelen oman työympäristön pystyttämistä. Seuraa tätä opasta sekä muita alla lueteltuja artikkeleitamme, jotka opastavat sinua askel askeleelta.
3. **Aloittelijat pieniin muutoksiin**: Tehtäviin, jotka vaativat vähemmän muokkausta, kuten oikolukuun tai korjauksiin, käytä suoraan GitHubin verkkokäyttöliittymää asettamatta kokonaista paikallista ympäristöä.

**Ohjelmistot, joita tarvitset seurataksesi opastani:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Koodieditori ([VSC](https://code.visualstudio.com/) tai [Sublime Text](https://www.sublimetext.com/))
![opas](assets/1.webp)
**Edellytykset ennen oppaan aloittamista:**
- On oltava [GitHub-tili](https://github.com/signup).
- On oltava haara [PlanB-verkoston lähdekoodirepositoriosta](https://github.com/PlanB-Network/bitcoin-educational-content).
- On oltava [professoriprofiili PlanB-verkostossa](https://planb.network/professors) (vain jos ehdotat täydellistä opasta).

**Jos tarvitset apua näiden edellytysten saavuttamisessa, muut oppaani opastavat sinua:**
**[Gitin ja GitHubin ymmärtäminen](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[GitHub-tilin luominen](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Työympäristön pystyttäminen](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
**[Professoriprofiilin luominen](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**
## Minkä tyyppistä sisältöä kirjoittaa PlanB-verkostoon?
Etsimme ensisijaisesti oppaita työkaluista, jotka liittyvät Bitcoiniin tai sen ekosysteemiin. Nämä sisällöt voidaan järjestää kuuden pääkategorian ympärille:
- Lompakko;
- Solmu;
- Louhinta;
- Kauppias;
- Vaihto;
- Yksityisyys.
![opas](assets/2.webp)
Näiden Bitcoinin kanssa erityisesti liittyvien aiheiden lisäksi PlanB etsii myös sisältöä teemoista, jotka korostavat yksilön suvereniteettia, kuten:
- Avoin lähdekoodi -työkalut;
- Tietotekniikka;
- Salaus;
- Energia;
- Matematiikka;
- Taloustiede;
- DIY-projektit;
- LifeHacking...
Esimerkiksi meillä on tällä hetkellä oppaita Tailsista, Nostrista ja GrapheneOS:sta. Nämä työkalut eivät ole suoraan yhteydessä Bitcoiniin, mutta ne ovat järjestelmiä, jotka voivat kiinnostaa meitä digitaalisen maailman itsehallinnon prosessissa. Nämä sisällöt voidaan integroida "Muut"-osion alakategoriaan.
Sinulla on valinta suunnitella opas alusta alkaen tai ottaa aiemmin verkkosivustollasi julkaistu opas (kunhan omistat tekijänoikeudet) jaettavaksi myös PlanB Networkissa, lisäten linkin alkuperäiseen artikkeliin.

Riippumatta valinnastasi, pidä mielessä, että kaikki PlanB Networkissa julkaistu sisältö on vapaan lisenssin [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) alaisuudessa. Tämä lisenssi sallii kenen tahansa kopioida ja mahdollisesti muokata sisältöäsi, kunhan alkuperäinen lähde mainitaan asianmukaisesti.

## Miten ehdottaa opasta PlanB Networkiin?

Kun kaikki on valmista ja paikallinen ympäristösi on hyvin pystytetty omalla PlanB Networkin haarallasi, voit aloittaa oppaan lisäämisen.

### Luo uusi haara

- Avaa selain ja siirry GitHubissa oman haarasi sivulle PlanB-repositoriossa. Tämä on haara, jonka olet perustanut GitHubiin. Haarasi URL näyttäisi tältä: `https://github.com/[käyttäjänimesi]/bitcoin-educational-content`:
![opas](assets/3.webp)
- Varmista, että olet päähaarassa `dev` ja klikkaa sitten `Sync fork` -painiketta. Jos haarasi ei ole ajan tasalla, GitHub tarjoaa haarasi päivittämistä. Suorita tämä päivitys. Jos taas haara on jo ajan tasalla, GitHub ilmoittaa sinulle:
![opas](assets/4.webp)
- Avaa GitHub Desktop -ohjelmisto ja varmista, että haarasi on oikein valittu ikkunan vasemmassa yläkulmassa:
![opas](assets/5.webp)
- Klikkaa `Fetch origin` -painiketta. Jos paikallinen repositoriosi on jo ajan tasalla, GitHub Desktop ei ehdota lisätoimia. Muussa tapauksessa `Pull origin` -vaihtoehto ilmestyy. Klikkaa tätä painiketta päivittääksesi paikallisen repositoriosi: ![opas](assets/6.webp)
- Varmista, että olet päähaarassa `dev`:
![opas](assets/7.webp)
- Klikkaa tätä haaraa, sitten klikkaa `New Branch` -painiketta:
![opas](assets/8.webp)
- Varmista, että uusi haara perustuu lähde-repositorioon, nimittäin `PlanB-Network/bitcoin-educational-content`.
- Nimeä haara siten, että sen tarkoitus on selvä, käyttäen väliviivoja erottamaan sanat. Esimerkiksi, jos tavoitteenamme on kirjoittaa opas Sparrow Wallet -ohjelmiston käytöstä, työhaara tälle oppaalle voitaisiin nimetä: `tuto-sparrow-wallet-loic`. Kun sopiva nimi on syötetty, klikkaa `Create branch` vahvistaaksesi haaran luomisen:
![opas](assets/9.webp)
- Nyt klikkaa `Publish branch` -painiketta tallentaaksesi uuden työhaaran online-haaraasi GitHubissa:
![opas](assets/10.webp)
Nyt, GitHub Desktopissa, sinun tulisi olla uudella haarallasi. Tämä tarkoittaa, että kaikki tietokoneellasi paikallisesti tehdyt muutokset tallennetaan yksinomaan tähän tiettyyn haaraan. Niin kauan kuin tämä haara pysyy valittuna GitHub Desktopissa, koneellasi paikallisesti näkyvät tiedostot vastaavat tämän haaran tiedostoja (`tuto-sparrow-wallet-loic`), eivätkä päähaaran (`dev`) tiedostoja.
![opas](assets/11.webp)
Jokaisen uuden artikkelin julkaisemiseksi, jonka haluat julkaista, sinun on luotava uusi haara `dev`-haarasta. Haara Gitissä on projektin rinnakkaisversio, joka mahdollistaa muutosten tekemisen vaikuttamatta päähaaraan, kunnes työ on valmis yhdistettäväksi.
### Tutoriaalin lisääminen

Nyt kun työhaara on luotu, on aika integroida uusi tutoriaalisi.
- Avaa tiedostonhallintasi ja siirry `bitcoin-educational-content`-kansioon, joka edustaa repositoriosi paikallista kloonia. Normaalisti löydät sen polusta `Documents\GitHub\bitcoin-educational-content`. Tässä hakemistossa on tarpeen löytää sopiva alikansio tutoriaalisi sijoittamiseksi. Kansioiden järjestely heijastaa PlanB Network -verkkosivuston eri osioita. Esimerkissämme, koska haluamme lisätä tutoriaalin Sparrow Walletista, on sopivaa siirtyä seuraavaan polkuun: `bitcoin-educational-content\tutorials\wallet`, joka vastaa verkkosivuston `WALLET`-osiota: ![tutorial](assets/12.webp)
- `wallet`-kansiossa sinun on luotava uusi hakemisto erityisesti tutoriaalillesi. Tämän kansion nimen on evättävä tutoriaalissa käsitelty ohjelmisto, varmistaen sanojen yhdistämisen viivoilla. Esimerkissäni kansio tulee nimetä `sparrow-wallet`:
![tutorial](assets/13.webp)
- Tässä uudessa tutoriaalillesi omistetussa alikansiossa on lisättävä useita elementtejä:
	- Luo `assets`-kansio, joka on tarkoitettu kaikkien tutoriaalisi kuvitusten vastaanottamiseen;
    - Tässä `assets`-kansiossa on luotava 8 alikansiota nimillä `fr`, `de`, `en`, `it`, `es`, `ja`, `vi` ja `pt`, jotta kuvat voidaan luokitella vastaavien kielten mukaan. Sinun on myös lisättävä `notext`-alikansio kuvituksille, jotka eivät tarvitse käännöstä, kuten esimerkiksi ruutukaappaukset;
	- `tutorial.yml`-tiedosto on luotava tallentamaan yksityiskohdat tutoriaalistasi;
	- Markdown-muotoiltu tiedosto on luotava kirjoittamaan itse tutoriaalin sisältö. Tämän tiedoston on oltava nimetty kirjoituskielen koodin mukaan. Esimerkiksi ranskaksi kirjoitetulle tutoriaalille tiedoston nimi olisi `fr.md`.
![tutorial](assets/14.webp)
- Yhteenvetona, tässä on luotavien tiedostojen hierarkia:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (muokattava oikean kategorian mukaan)
        └── sparrow-wallet/ (muokattava tutoriaalin nimen mukaan)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (muokattava sopivan kielikoodin mukaan)
```

- Aloita avaamalla `tutorial.yml`-tiedostosi koodieditorillasi.
- Täytä jokainen kenttä alla määritellyillä tiedoilla:
- **builder**: Anna yrityksen nimi, joka tuottaa ohjelmiston, jolle olet luomassa tutoriaalia;
- **tags**: Määritä joukko avainsanoja, jotka liittyvät läheisesti artikkelisi aiheeseen, helpottaaksesi sen hakua ja indeksointia;
- **category**: Valitse sopiva alakategoria niiden joukosta, jotka ovat saatavilla PlanB-sivustolla, sisällön perusteella. Esimerkiksi, jos kyseessä on opas `WALLET`-osiossa, saatavilla olevat vaihtoehdot ovat `Desktop`, `Hardware` ja `Mobile`;
- **level**: Ilmoita oppaan vaikeustaso valitsemalla yksi seuraavista neljästä kategoriasta:
    - Aloittelija (`beginner`),
    - Keskitaso (`intermediary`),
    - Edistynyt (`advanced`),
    - Asiantuntija (`expert`).
- **professor**: Anna kontribuutori-ID, joka näkyy professoriprofiilissasi. Lisätietoja varten, katso [vastaava opas](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (valinnainen): Jos haluat antaa tunnustusta lähdeweb-sivustolle oppaasta, jonka olet kehittämässä, kuten omalle henkilökohtaiselle sivustollesi, tässä voit lisätä kyseisen linkin.
![opas](assets/15.webp)
- Kun olet saanut muokattua `tutorial.yml`-tiedostoasi, tallenna dokumenttisi klikkaamalla `File > Save`:
![opas](assets/16.webp)
- Nyt voit sulkea koodieditorisi.
- `assets`-kansioon sinun tulee lisätä tiedosto nimeltä `logo.webp`, joka toimii pikkukuvana artikkelillesi. Tämän kuvan tulee olla `.webp`-muodossa ja sen tulee noudattaa neliön mittoja, jotta se sopii käyttöliittymään. Sinulla on vapaus valita ohjelmiston logo, jota oppaasi käsittelee, tai mikä tahansa muu asiaankuuluva kuva, kunhan se on oikeuksista vapaa. Lisäksi, lisää myös kuva nimeltä `cover.webp` samaan sijaintiin. Tämä kuva näytetään oppaasi yläosassa. Varmista, että tämä kuva, kuten logo, noudattaa käyttöoikeuksia ja sopii oppaasi kontekstiin:
![opas](assets/17.webp)
- Nyt voit avata tiedoston, joka tulee isännöimään opastasi, nimettynä kielesi koodilla, kuten `fi.md`. Siirry Obsidianissa, ikkunan vasemmalla puolella, selaa kansiopuuta oppaasi kansioon ja haettuun tiedostoon:
![opas](assets/18.webp)
- Klikkaa tiedostoa avataksesi sen:
![opas](assets/19.webp)
- Aloita täyttämällä `Properties`-osa dokumentin yläosassa. Jos tämä osio puuttuu tiedostostasi (jos dokumentti on täysin tyhjä), voit toistaa sen kopioimalla sen toisesta olemassa olevasta oppaasta: ![opas](assets/20.webp)
- Voit myös lisätä sen manuaalisesti tällä tavalla käyttäen koodieditoriasi:
```markdown
---
name: [Otsikko]
description: [Kuvaus]
---
```
![opas](assets/21.webp)
- Täytä oppaasi nimi ja lyhyt kuvaus siitä:
![opas](assets/22.webp)
- Lisää sitten kansikuvasi oppaasi alkuun. Tee tämä kirjoittamalla:
```markdown
![kansi-sparrow](assets/cover.webp)
```
- Tämä syntaksi on hyödyllinen aina, kun haluat lisätä kuvan oppaaseesi. Huutomerkki osoittaa, että kyseessä on kuva, vaihtoehtoinen teksti (alt) on määritelty hakasulkujen välissä. Kuvan polku on ilmoitettu sulkujen välissä:
![opas](assets/23.webp)
- Jatka oppaasi kirjoittamista kirjoittamalla sisältöäsi. Kun haluat integroida alaotsikon, käytä sopivaa markdown-muotoilua etuliitteenä tekstille `##`:
![opas](assets/24.webp)

### Miten lisätä kaavioita oppaaseen?
`assets`-kansion kielialakansiot on tarkoitettu järjestämään kaaviot ja visuaalit, jotka tulevat mukaan opastukseesi. Jos kuvasi sisältävät tekstiä, varmista, että käännät ne jokaiselle asiaankuuluvalle kielelle, jotta sisältösi on saavutettavissa kansainväliselle yleisölle. Kaavioille, joissa ei ole käännettävää tekstiä tai näyttökaappauksille, sijoita ne suoraan `notext`-alikansioon.
![opastus](assets/25.webp)
Kuviesi nimeäminen on yksinkertaista: laita vain numerot järjestyksessä, jossa ne esiintyvät opastuksessa. Esimerkiksi nimeä ensimmäinen kuvasi `1.webp`, toinen `2.webp` ja niin edelleen.

Jos sama kaavio käännetään useille kielille, säilytä sama tiedostonimi eri käännöksille kielialakansioissa, kuten `en/1.webp`, `fr/1.webp`, `pt/1.webp` jne.

Sinulla on mahdollisuus käyttää erilaisia kuvamuotoja, kuten `jpeg`, `png` tai `webp`. On suositeltavaa valita `webp`-muoto, jotta kuvat ovat kevyempiä.
![opastus](assets/26.webp)
Kaavion lisäämiseksi dokumenttiisi käytä seuraavaa komentoa Markdownissa, varmistaen, että määrität sopivan vaihtoehtoisen tekstin ja kuvan oikean polun:
```markdown
![varpunen](assets/notext/1.webp)
```
Huutomerkki alussa osoittaa, että kyseessä on kuva. Vaihtoehtoinen teksti, joka auttaa saavutettavuudessa ja SEO:ssa, sijoitetaan hakasulkujen väliin. Lopuksi kuvan polku ilmoitetaan sulkeiden sisällä: ![opastus](assets/27.webp)
Jos haluat luoda omat kaaviosi, varmista, että noudatat PlanB Networkin graafista ohjeistusta visuaalisen johdonmukaisuuden varmistamiseksi:
- **Fontti**: Käytä [Rubik](https://fonts.google.com/specimen/Rubik);
- **Värit**:
	- Oranssi: #FF5C00
	- Musta: #000000
	- Valkoinen: #FFFFFF

**On ehdottoman tärkeää, että kaikki opastuksiisi integroidut visuaalit ovat rojaltivapaita tai noudattavat lähdetiedoston lisenssiä**. Lisäksi kaikki PlanB Networkissa julkaistut kaaviot ovat saatavilla CC-BY-SA-lisenssin alaisina, samoin kuin teksti.

**-> Vinkki:** Kun jaat tiedostoja julkisesti, kuten kuvia, on tärkeää poistaa kaikki tarpeeton metadata. Tämä voi sisältää arkaluonteista tietoa, kuten sijaintitiedot, luontipäivämäärät tai tekijän tiedot. Yksityisyytesi suojaamiseksi on suositeltavaa poistaa tämä metadata. Tämän toimenpiteen yksinkertaistamiseksi voit käyttää erikoistyökaluja, kuten [Exif Cleaner](https://exifcleaner.com/), joka tarjoaa mahdollisuuden puhdistaa asiakirjan metadatan yksinkertaisella raahaa ja pudota -toiminnolla.

### Miten tallentaa ja lähettää opastus?

Kun olet saanut opastuksesi kirjoitettua valitsemallasi kielellä, seuraava vaihe on tehdä **Pull Request**. Ylläpitäjä lisää sitten puuttuvat käännökset opastukseesi käyttämällä automatisoitua käännösmenetelmäämme.

- Pull Requestin tekemiseksi avaa GitHub Desktop -ohjelmisto.
- Ohjelmiston tulisi automaattisesti havaita tekemäsi muutokset paikallisesti verrattuna alkuperäiseen repositorioon. Ennen jatkamista, tarkista huolellisesti käyttöliittymän vasemmalla puolella, että nämä muutokset vastaavat täsmälleen sitä, mitä odotit: ![opastus](assets/28.webp)
- Lisää otsikko commitillesi, sitten klikkaa sinistä `Commit to [sinun haara]` -nappia vahvistaaksesi nämä muutokset: ![opastus](assets/29.webp)
Commit on muutosten tallennus haaraan, johon liittyy kuvaileva viesti, mahdollistaen projektin kehityksen seuraamisen ajan myötä. Se on siis eräänlainen välitarkastuspiste.
- Klikkaa sitten `Push origin` -painiketta. Tämä lähettää tekemäsi muutoksen haarallesi: ![tutorial](assets/30.webp) - Jos et ole saanut opastustasi valmiiksi, voit palata siihen myöhemmin ja tehdä uusia muutoksia.
- Jos olet saanut tämän haaran muokkaukset valmiiksi, klikkaa nyt `Preview Pull Request` -painiketta: ![tutorial](assets/31.webp)
- Voit tarkistaa vielä kerran, että muutoksesi ovat oikein, ja sitten klikkaa `Create pull request` -painiketta:
![tutorial](assets/32.webp)
Pull Request on pyyntö integroida muutoksesi haarastasi PlanB Network -repositorion päähaaraan, mikä mahdollistaa muutosten tarkastelun ja keskustelun ennen niiden yhdistämistä.

- Sinut ohjataan automaattisesti selaimessasi GitHubiin Pull Requestisi valmistelusivulle:
![tutorial](assets/33.webp)
- Anna otsikko, joka lyhyesti tiivistää muutokset, jotka haluat yhdistää lähde-repositorioon.
- Lisää lyhyt kommentti kuvaamaan näitä muutoksia.
- Klikkaa vihreää `Create pull request` -painiketta vahvistaaksesi yhdistämisen pyynnön:
![tutorial](assets/34.webp)
PR:si on sen jälkeen näkyvissä PlanB Network -repositorion `Pull Request` -välilehdellä. Sinun tarvitsee nyt vain odottaa, kunnes ylläpitäjä ottaa sinuun yhteyttä vahvistaakseen panoksesi yhdistämisen tai pyytääkseen mahdollisia lisämuutoksia.
![tutorial](assets/35.webp)
PR:si yhdistämisen jälkeen päähaaraan suositellaan työhaaran (`tuto-sparrow-wallet`) poistamista, jotta haarahistoriasi pysyy siistinä haarassasi. GitHub tarjoaa sinulle automaattisesti tämän vaihtoehdon PR:si sivulla:
![tutorial](assets/36.webp)
GitHub Desktop -ohjelmistossa voit vaihtaa takaisin haarasi päähaaraan (`dev`).
![tutorial](assets/7.webp)
Jos haluat tehdä muutoksia panokseesi sen jälkeen, kun olet jo jättänyt PR:si, menettely riippuu PR:si nykyisestä tilasta:
- Jos PR:si on edelleen avoinna eikä sitä ole vielä yhdistetty, tee muutokset paikallisesti pysyen samalla haaralla. Kun muutokset on saatu valmiiksi, käytä `Push origin` -painiketta lisätäksesi uuden commitin edelleen avoimeen PR:si;
- Jos PR:si on jo yhdistetty päähaaraan, sinun on aloitettava prosessi alusta luomalla uusi haara ja jättämällä uusi PR. Varmista, että paikallinen repositoriosi on synkronoitu PlanB Networkin lähde-repositorion kanssa ennen jatkamista.
