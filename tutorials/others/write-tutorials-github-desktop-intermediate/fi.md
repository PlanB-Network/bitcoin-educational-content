---
name: Contribution - Tutorial GitHub Desktopilla (keskitaso)
description: Täydellinen opas opetusohjelman ehdottamiseen Plan ₿ -verkossa GitHub Desktopin avulla
---
![cover](assets/cover.webp)

Ennen kuin seuraat tätä ohjeistusta uuden ohjeen lisäämisestä, sinun on suoritettava joitakin alustavia vaiheita. Jos et ole vielä tehnyt sitä, pyydän sinua tutustumaan ensin tähän johdanto-oppaaseen ja palaamaan sitten tänne:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Olette jo:


- Valitse opetusohjelmasi teema;
- Ota yhteyttä Plan ₿ Network -tiimiin [Telegram-ryhmässä] (https://t.me/PlanBNetwork_ContentBuilder) tai paolo@planb.network;
- Valitsemasi osallistumisvälineet.

Tässä oppaassa katsotaan, miten voit lisätä oppaasi Plan ₿ -verkkoon perustamalla paikallisen ympäristön GitHub Desktopin avulla. Jos hallitset jo Gitin, tämä hyvin yksityiskohtainen opetusohjelma ei ehkä ole sinulle tarpeen. Suosittelen pikemminkin tutustumaan tähän toiseen opetusohjelmaan, jossa esittelen vain tärkeimmät suuntaviivat ilman yksityiskohtaisia vaihe vaiheelta annettavia ohjeita:


- Kokeneet käyttäjät**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Jos et halua perustaa paikallista ympäristöä, seuraa tätä toista aloittelijoille suunnattua ohjetta, jossa teemme muutokset suoraan GitHubin web-käyttöliittymän kautta:


- Aloittelijoille (verkkokäyttöliittymä)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Edellytykset

Tämän ohjeen seuraamiseen tarvittava ohjelmisto:


- [GitHub Desktop](https://desktop.github.com/);
- Markdown-tiedostoeditori, kuten [Obsidian](https://obsidian.md/);
- Koodieditori ([VSC](https://code.visualstudio.com/) tai [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Edellytykset ennen opetusohjelman aloittamista:


- Sinulla on [GitHub-tili](https://github.com/signup);
- Ota haara [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- On [professorin profiili Plan ₿ Network -verkossa](https://planb.network/professors) (vain jos ehdotat täydellistä opetusohjelmaa).

Jos tarvitset apua näiden edellytysten hankkimisessa, muut opetusohjelmani auttavat sinua:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb

Kun kaikki on kunnossa ja paikallinen ympäristösi on kunnolla asennettu Plan ₿ Networkin oman haarukan kanssa, voit aloittaa opetusohjelman lisäämisen.

## 1 - Luo uusi haara

Avaa selaimesi ja siirry Plan ₿ Network -tietovaraston haarukan sivulle. Tämä on haarautuminen, jonka olet perustanut GitHubiin. Haarautumisesi URL-osoitteen pitäisi näyttää seuraavalta: `https://github.com/[käyttäjätunnuksesi]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Varmista, että olet päähaarassa `dev` ja napsauta sitten `Synkronoi haarautuminen`-painiketta. Jos haarasi ei ole ajan tasalla, GitHub tarjoaa sinulle mahdollisuutta päivittää haarasi. Jatka päivitystä. Jos haarasi on jo ajan tasalla, GitHub ilmoittaa siitä sinulle:

![TUTO](assets/fr/04.webp)

Avaa GitHub Desktop -ohjelmisto ja varmista, että haarautumisesi on oikein valittu ikkunan vasemmassa yläkulmassa:

![TUTO](assets/fr/05.webp)

Napsauta `Hae alkuperä`-painiketta. Jos paikallinen arkistosi on jo ajan tasalla, GitHub Desktop ei ehdota lisätoimia. Muussa tapauksessa `Pull origin` -vaihtoehto tulee näkyviin. Napsauta tätä painiketta päivittääksesi paikallisen arkistosi:

![TUTO](assets/fr/06.webp)

Tarkista, että olet todellakin päähaarassa `dev`:

![TUTO](assets/fr/07.webp)

Napsauta tätä haaraa ja napsauta sitten `Uusi haara`-painiketta:

![TUTO](assets/fr/08.webp)

Varmista, että uusi haara perustuu lähdekoodivarastoon, nimittäin `PlanB-Network/bitcoin-educational-content`.

Nimeä sivukonttorisi niin, että otsikosta käy selvästi ilmi sen tarkoitus, ja erota jokainen sana toisistaan viivaimilla. Sanotaan esimerkiksi, että tavoitteenamme on kirjoittaa Sparrow Wallet -ohjelmiston käyttöä koskeva opetusohjelma. Tässä tapauksessa tämän ohjeen kirjoittamiseen omistetun työhaaran nimi voisi olla: `tuto-sparrow-wallet-loic`. Kun sopiva nimi on syötetty, klikkaa `Luo haara` vahvistaaksesi haaran luomisen:

![TUTO](assets/fr/09.webp)

Napsauta nyt `Publish branch`-painiketta tallentaaksesi uuden työhaarasi GitHubin online-haaraan:

![TUTORIAL](assets/fr/10.webp)

Nyt GitHubin työpöydällä sinun pitäisi olla uudessa haarassasi. Tämä tarkoittaa, että kaikki tietokoneellasi paikallisesti tehdyt muutokset tallennetaan yksinomaan tähän haaraan. Niin kauan kuin tämä haara on valittuna GitHub Desktopissa, koneellasi paikallisesti näkyvät tiedostot vastaavat tämän haaran (`tuto-sparrow-wallet-loic`) tiedostoja, eivätkä päähaaran (`dev`) tiedostoja.

![TUTORIAL](assets/fr/11.webp)

Jokaista uutta artikkelia varten, jonka haluat julkaista, sinun on luotava uusi haara `dev`:stä. Gitissä haara on projektin rinnakkaisversio, jonka avulla voit tehdä muutoksia vaikuttamatta päähaaraan, kunnes työ on valmis yhdistettäväksi.

## 2 - Ohjetiedostojen lisääminen

Nyt kun työhaara on luotu, on aika integroida uusi opetusohjelma. Sinulla on kaksi vaihtoehtoa: voit käyttää Python-skriptiäni, joka automatisoi tarvittavien dokumenttien luomisen, tai luoda jokaisen tiedoston manuaalisesti. Tarkastelemme kummankin vaihtoehdon vaiheita.

### Python-skriptilläni

Sinun on asennettava koneellesi:
- Python 3.8 tai uudempi.

Käyttääksesi skriptiä siirry kansioon, johon se on tallennettu. Skripti löytyy Plan ₿ Networkin tietovarastosta seuraavasta polusta: `bitcoin-educational-content/scripts/tutorial-related/data-creator`.

Kun olet kansiossa, asenna riippuvuudet:

```bash
pip install -r requirements.txt
```

Seuraavaksi käynnistä ohjelmisto seuraavalla komennolla:

```bash
python3 main.py
```

Graafinen käyttöliittymä (GUI) avautuu. Ensimmäisellä käyttökerralla sinun on syötettävä kaikki tarvittavat tiedot, mutta seuraavilla käyttökerroilla skripti muistaa henkilökohtaiset tietosi, joten sinun ei tarvitse syöttää niitä uudelleen.

![DATA-CREATOR-PY](assets/fr/37.webp)

Aloita syöttämällä paikallinen polku `/tutorials`-kansioon kloonatussa tietovarastossasi (`.../bitcoin-educational-content/tutorials/`). Voit syöttää sen manuaalisesti tai napsauttaa "Browse"-painiketta selaillaksesi tiedostojenhallinnassa.

![DATA-CREATOR-PY](assets/fr/38.webp)

Valitse kieli, jolla kirjoitat ohjeesi.

![DATA-CREATOR-PY](assets/fr/39.webp)

Kirjoita kenttään "Contributor's GitHub ID" GitHub-tunnuksesi.

![DATA-CREATOR-PY](assets/fr/40.webp)

Kenttään "PBN professor's ID" syötä tunnisteesi käyttämällä BIP39-listan sanoja, kuten ne näkyvät [professoriprofiilissasi](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![DATA-CREATOR-PY](assets/fr/41.webp)

Jos sinulla ei ole vielä professoriprofiilia, katso tämä opas:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Napsauta sitten "New Tutorial" -painiketta.

![DATA-CREATOR-PY](assets/fr/42.webp)

Valitse opetusohjelmallesi pääkategoria. Valitse sen jälkeen sopiva alakategoria valitsemasi pääkategorian perusteella.

![DATA-CREATOR-PY](assets/fr/43.webp)

Määritä opetusohjelman vaikeustaso.

![DATA-CREATOR-PY](assets/fr/44.webp)

Valitse nimi erityisesti opetusohjelmaasi varten luodulle hakemistolle. Hakemiston nimen tulisi kuvastaa opetusohjelmassa käsiteltävää ohjelmistoa ja sanojen tulisi olla yhdistettyinä tavuviivoin. Esimerkiksi hakemiston nimi voisi olla `red-wallet`:

![DATA-CREATOR-PY](assets/fr/45.webp)

`project_id` on opetusohjelmassa käsitellyn työkalun takana olevan yrityksen tai organisaation UUID, joka on saatavilla [projektiluettelosta](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Esimerkiksi Sparrow Wallet -opetusohjelmassa löydät `project_id` tiedostosta: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Tämä tieto lisätään opetusohjelmasi YAML-tiedostoon, koska Plan ₿ Network ylläpitää Bitcoinin ja siihen liittyvien projektien aktiivisten yritysten ja organisaatioiden tietokantaa. Lisäämällä opetusohjelmaan liittyvän `project_id`:n, yhdistät sisällön vastaavaan tahoon.

***Päivitys:*** Skriptin uudessa versiossa `project_id`:tä ei tarvitse enää syöttää manuaalisesti. Hakutoiminto on lisätty, jolloin voit etsiä projektia nimellä ja hakea automaattisesti vastaavan `project_id`:n. Kirjoita projektin nimi kenttään "Project Name", etsi se ja valitse haluamasi yritys avattavasta valikosta. `project_id` täytetään automaattisesti alla olevaan kenttään. Voit myös syöttää sen manuaalisesti tarvittaessa.

![DATA-CREATOR-PY](assets/fr/46.webp)

Avainsanoja varten valitse 2 tai 3 merkityksellistä avainsanaa, jotka liittyvät opetusohjelmasi sisältöön, valiten ne ainoastaan [Plan ₿ Network -avainsanalistasta](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Ohjelmisto sisältää myös hakutoiminnon avainsanojen etsimiseksi avattavasta valikosta.

![DATA-CREATOR-PY](assets/fr/47.webp)

Kun kaikki tiedot on syötetty ja tarkistettu, napsauta "Create Tutorial" -painiketta vahvistaaksesi opetusohjelman tiedostojen luomisen. Tämä luo opetusohjelmallesi hakemiston ja kaikki tarvittavat tiedostot valitun kategorian sisälle.

![DATA-CREATOR-PY](assets/fr/48.webp)

Voit nyt ohittaa alaluvun "Ilman Python-skriptiäni" sekä vaiheen 3 "YAML-tiedoston täyttäminen", koska skripti on jo suorittanut nämä toimenpiteet automaattisesti puolestasi. Jatka suoraan vaiheeseen 4 ja aloita opetusohjelmasi kirjoittaminen.

Lisätietoja tästä Python-skriptistä löydät myös [README-tiedostosta](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Ilman Python-skriptiäni

Avaa tiedostonhallinta ja siirry kansioon `bitcoin-educational-content`, joka edustaa paikallista kloonia repositoriostasi. Sen pitäisi löytyä yleensä sijainnista `Documents\GitHub\bitcoin-educational-content`.

Tässä hakemistossa sinun on löydettävä oikea alikansio opetusmateriaalisi sijoittamiseen. Kansiorakenne vastaa Plan ₿ Network -verkkosivuston eri osioita. Esimerkissämme, koska haluamme lisätä opetusohjelman Sparrow Walletista, meidän tulee siirtyä seuraavaan polkuun: `bitcoin-educational-content\tutorials\wallet`, joka vastaa verkkosivuston `WALLET`-osiota:

![TUTO](assets/fr/12.webp)

Sinun on luotava `wallet`-kansion sisälle uusi hakemisto, joka on varattu nimenomaan opetusohjelmallesi. Tämän kansion nimen tulisi muistuttaa opetusohjelmassa käsiteltävää ohjelmistoa, ja varmista, että sanat liitetään toisiinsa katkoviivoilla. Esimerkissäni kansio on nimeltään `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

Tähän uuteen, opetusohjelmallesi omistettuun alikansioon on lisättävä useita elementtejä:


- Luo `assets`-kansio, johon on tarkoitus tallentaa kaikki opetusohjelmaasi varten tarvittavat kuvitukset;
- Tähän `assets`-kansioon sinun on luotava alikansio, joka on nimetty opetusohjelman alkuperäisen kielikoodin mukaan. Jos opetusohjelma on esimerkiksi kirjoitettu englanniksi, tämän alikansion on oltava nimeltään `en`. Sijoita sinne kaikki opetusohjelman visuaalinen materiaali (kaaviot, kuvat, kuvakaappaukset jne.).
- Tutorial.yml-tiedosto on luotava tallentamaan opetusohjelmaan liittyvät yksityiskohdat;
- Ohjeen varsinaista sisältöä varten on luotava markdown-muotoinen tiedosto. Tämä tiedosto on otsikoitava kirjoituksen kielikoodin mukaisesti. Esimerkiksi ranskaksi kirjoitetun opetusohjelman tiedoston nimi on `fr.md`.

![TUTO](assets/fr/14.webp)

Yhteenvetona voidaan todeta, että tässä on luotavien tiedostojen hierarkia:

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Täytä YAML-tiedosto

Täytä `tutorial.yml`-tiedosto kopioimalla seuraava malli:

```yaml
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

credits:
  professor: 

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributors_id:
      - 
    reward:
````

Tässä ovat pakollisten kenttien tiedot:


- **id**: UUID (_Universally Unique Identifier_), jolla opetusohjelma voidaan yksilöidä yksiselitteisesti. Voit luoda sen [online-työkalulla](https://www.uuidgenerator.net/version4). Ainoa vaatimus on, että tämän UUID-tunnuksen on oltava satunnainen, jotta se ei ole ristiriidassa alustan toisen UUID-tunnuksen kanssa;
- **project_id**: UUID sen yrityksen tai organisaation UUID, joka on opetusohjelmassa esitellyn työkalun takana [projektiluettelosta](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Jos esimerkiksi luot Sparrow Wallet -ohjelmistoa koskevan opetusohjelman, löydät tämän `project_id`:n seuraavasta tiedostosta: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Tämä tieto lisätään opetusohjelmasi YAML-tiedostoon, koska Plan ₿ Network ylläpitää tietokantaa kaikista yrityksistä ja organisaatioista, jotka toimivat Bitcoinin tai siihen liittyvien hankkeiden parissa. Lisäämällä opetusohjelmaasi liittyvän yhteisön `project_id`:n luot linkin näiden kahden elementin välille;
- **tags**: 2 tai 3 relevanttia avainsanaa, jotka liittyvät opetusohjelman sisältöön ja jotka on valittu yksinomaan [Plan ₿ Networkin tunnisteiden luettelosta](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: Plan ₿ Network -verkkosivuston rakenteen mukainen opetusohjelman sisältöä vastaava alaluokka (esimerkiksi lompakoiden osalta: `desktop`, `hardware`, `mobile`, `backup`);
- **level**: Oppaan vaikeustaso, muun muassa:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: Sinun `contributor_id` (BIP39 sanat), joka näkyy [professoriprofiilissasi](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **language**: Tutoriaalin alkuperäinen kieli (esimerkiksi `fr`, `en` jne.);
- oikoluku**: Tietoa oikolukuprosessista. Täytä ensimmäinen osa, sillä oman opetusohjelmasi oikolukeminen lasketaan ensimmäiseksi validoinniksi:
    - kieli**: Oikoluvun kielikoodi (esimerkiksi `fr`, `en` jne.).
    - **last_contribution_date**: Tämän päivän päivämäärä.
    - **urgency**: Jätä tyhjäksi.
    - **contributors_id**: GitHub-tunnuksesi.
    - **reward**: Jätä tyhjäksi.

Lisätietoja professorin tunnuksesta saat vastaavasta ohjeesta:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Tässä on esimerkki valmiista `tutorial.yml`-tiedostosta Blockstream Green -lompakkoa koskevaa opetusohjelmaa varten:

```yaml
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Otsikko]
description: [Kuvaus]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```