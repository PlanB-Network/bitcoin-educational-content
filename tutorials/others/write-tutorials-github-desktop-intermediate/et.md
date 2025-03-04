---
name: Panus - õpetus GitHubi töölaua abil (vahepealne)
description: Täielik juhend, kuidas teha ettepanek õpetuse kohta Plan ₿ Network kasutades GitHubi töölauda
---
![cover](assets/cover.webp)

Enne selle uue õpetuse lisamist käsitleva õpetuse järgimist peate olema teinud mõned esialgsed sammud. Kui te pole seda veel teinud, siis kutsun teid üles kõigepealt tutvuma selle sissejuhatava õpetusega ja seejärel tulema siia tagasi:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Te olete juba:


- Valige oma õpetuse teema;
- Võtke ühendust Plan ₿ Networki meeskonnaga [Telegrami grupi](https://t.me/PlanBNetwork_ContentBuilder) või paolo@planb.network kaudu;
- Valige oma panuse vahendid.

Selles õpetuses näeme, kuidas lisada oma õpetus Plan ₿ võrgustikku, luues oma kohaliku keskkonna GitHubi töölaua abil. Kui te juba oskate Git'i, ei pruugi see väga üksikasjalik õpetus teile vajalik olla. Ma soovitan pigem tutvuda selle teise õpetusega, kus ma esitan ainult peamised suunised, ilma üksikasjalike samm-sammult juhenditeta:


- Kogenud kasutajad**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Kui te ei soovi oma lokaalset keskkonda luua, järgige seda teist, algajatele mõeldud õpetust, kus me teeme muudatused otse GitHubi veebiliidese kaudu:


- Algajad (veebiliides)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Eeltingimused

Selle õpetuse jälgimiseks vajalik tarkvara:


- [GitHub Desktop](https://desktop.github.com/);
- Markdown-failide redaktor nagu [Obsidian](https://obsidian.md/);
- Koodiredaktor ([VSC](https://code.visualstudio.com/) või [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Eeltingimused enne õpetuse alustamist:


- Kas teil on [GitHubi konto](https://github.com/signup);
- On olemas [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- Omama [professori profiili Plan ₿ Network](https://planb.network/professors) (ainult juhul, kui te esitate täieliku õpetuse).

Kui vajate abi nende eelduste hankimisel, siis minu teised õpetused aitavad teid:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
Kui kõik on paigas ja teie kohalik keskkond on korralikult seadistatud koos oma Plan ₿ Networki haruga, võite alustada õpetuse lisamist.

## 1 - Uue haru loomine

Avage oma brauser ja suunduge Plan ₿ Networki repositooriumi hargnemise lehele. See on teie poolt GitHubis loodud haru. Teie hargnemise URL peaks välja nägema järgmiselt: `https://github.com/[teie-kasutajanimi]/bitcoin-õppematerjal`:

![TUTO](assets/fr/03.webp)

Veenduge, et olete põhiharul `dev`, seejärel klõpsake nupule `Sync fork`. Kui teie haru ei ole ajakohane, pakub GitHub teile oma haru uuendamist. Jätkake selle uuendamisega. Kui aga teie haru on juba ajakohane, teavitab GitHub teid sellest:

![TUTO](assets/fr/04.webp)

Avage GitHubi töölaua tarkvara ja veenduge, et teie haru on õigesti valitud akna vasakus ülanurgas:

![TUTO](assets/fr/05.webp)

Klõpsake nupul "Tooge päritolu". Kui teie kohalik repositoorium on juba ajakohane, ei paku GitHub Desktop mingeid lisategevusi. Vastasel juhul ilmub valik `Pull origin`. Klõpsake sellel nupul, et oma kohalikku repositooriumi uuendada:

![TUTO](assets/fr/06.webp)

Kontrollige, et olete tõepoolest peamisel harul `dev`:

![TUTO](assets/fr/07.webp)

Klõpsake sellel harul, seejärel klõpsake nupule "Uus haru":

![TUTO](assets/fr/08.webp)

Veenduge, et uus haru põhineb lähtematerjalide repositooriumil, nimelt `PlanB-Network/bitcoin-educational-content`.

Nimetage oma filiaal nii, et pealkirjast oleks selgelt näha selle eesmärk, kasutades iga sõna eraldamiseks mõttekriipsu. Ütleme näiteks, et meie eesmärk on kirjutada õpetus Sparrow Wallet tarkvara kasutamise kohta. Sellisel juhul võiks selle õpetuse kirjutamisele pühendatud tööharu nimetada: `tuto-sparrow-wallet-loic`. Kui sobiv nimi on sisestatud, klõpsake haru loomise kinnitamiseks nuppu `Create branch`:

![TUTO](assets/fr/09.webp)

Nüüd klõpsake nupule `Publish branch`, et salvestada oma uus tööharu GitHubi veebiharule:

![TUTORIAL](assets/fr/10.webp)

Nüüd peaksite GitHubi töölaual leidma oma uue haru. See tähendab, et kõik teie arvutis lokaalselt tehtud muudatused salvestatakse ainult sellele konkreetsele harule. Samuti, seni kuni see haru on GitHubi töölaual valitud, vastavad teie masinas lokaalselt nähtavad failid selle haru (`tuto-sparrow-wallet-loic`), mitte põhiharu (`dev`) failidele.

![TUTORIAL](assets/fr/11.webp)

Iga uue artikli jaoks, mida soovite avaldada, peate looma uue haru `dev`st. Haru on Gitis projekti paralleelversioon, mis võimaldab teil teha muudatusi, ilma et see mõjutaks põhiharu, kuni töö on valmis ühendamiseks.

## 2 - Juhendfailide lisamine

Nüüd, kui tööharu on loodud, on aeg integreerida oma uus õpetus. Teil on kaks võimalust: kasutada minu Python-skripti, mis automatiseerib vajalike dokumentide loomise, või luua iga fail käsitsi. Vaatame mõlema võimaluse puhul järgitavaid samme.

### Minu Python skriptiga

Peate oma arvutisse installima:
- Python 3.8 või uuema versiooni.

Skripti kasutamiseks minge kausta, kuhu see on salvestatud. Skript asub Plan ₿ Networki andmehoidlas järgmisel teel: `bitcoin-educational-content/scripts/tutorial-related/data-creator`.

Kui olete kaustas, installige sõltuvused:

```bash
pip install -r requirements.txt
```

Seejärel käivitage tarkvara järgmise käsuga:

```bash
python3 main.py
```

Graafiline kasutajaliides (GUI) avaneb. Esmakordsel käivitamisel peate sisestama kõik vajalikud andmed, kuid järgmistel kasutuskordadel salvestab skript teie isikliku teabe, nii et te ei pea seda uuesti sisestama.

![DATA-CREATOR-PY](assets/fr/37.webp)

Alustage kohaliku tee sisestamisest `/tutorials` kausta teie kloonitud repositooriumis (`.../bitcoin-educational-content/tutorials/`). Selle saab sisestada käsitsi või klõpsata nupul "Browse", et sirvida seda failihalduris.

![DATA-CREATOR-PY](assets/fr/38.webp)

Valige keel, milles hakkate oma õpetust kirjutama.

![DATA-CREATOR-PY](assets/fr/39.webp)

Sisestage lahtrisse "Contributor's GitHub ID" oma GitHubi identifikaator.

![DATA-CREATOR-PY](assets/fr/40.webp)

Lahtrisse "PBN professor's ID" sisestage oma identifikaator, kasutades BIP39 loendi sõnu, nagu see on nähtav [teie professori profiilis](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![DATA-CREATOR-PY](assets/fr/41.webp)

Kui teil pole veel professori profiili, vaadake seda juhendit:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Seejärel klõpsake nuppu "New Tutorial".

![DATA-CREATOR-PY](assets/fr/42.webp)

Valige oma õpetuse jaoks peamine kategooria. Seejärel valige vastavalt peamisele kategooriale sobiv alamkategooria.

![DATA-CREATOR-PY](assets/fr/43.webp)

Määrake õpetuse raskusaste.

![DATA-CREATOR-PY](assets/fr/44.webp)

Valige spetsiaalselt teie õpetuse jaoks loodud kausta nimi. Kausta nimi peaks kajastama õpetuses käsitletavat tarkvara ja sõnu tuleks eraldada sidekriipsudega. Näiteks võib kausta nimi olla `red-wallet`:

![DATA-CREATOR-PY](assets/fr/45.webp)

`project_id` on õpetuses käsitletava tööriista taga oleva ettevõtte või organisatsiooni UUID, mis on saadaval [projektide loendis](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Näiteks Sparrow Walleti õpetuse jaoks leiate `project_id` faili `bitcoin-educational-content/resources/projects/sparrow/project.yml` seest. See teave lisatakse teie õpetuse YAML-faili, kuna Plan ₿ Network haldab Bitcoini või sellega seotud projektide aktiivsete ettevõtete ja organisatsioonide andmebaasi. Lisades oma õpetusele seotud `project_id`, loote sisu ja vastava organisatsiooni vahelise seose.

***Uuendus:*** Skripti uues versioonis pole enam vaja käsitsi `project_id` sisestada. Lisatud on otsingufunktsioon, et leida projekt nime järgi ja hankida automaatselt vastav `project_id`. Tippige välja "Project Name" algusesse projekti nimi, otsige see üles ja valige soovitud ettevõte rippmenüüst. `project_id` täidetakse automaatselt allolevasse lahtrisse. Vajadusel saate selle ka käsitsi sisestada.

![DATA-CREATOR-PY](assets/fr/46.webp)

Siltide jaoks valige 2 või 3 asjakohast märksõna, mis on seotud teie õpetuse sisuga, valides need ainult [Plan ₿ Networki siltide loendist](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Tarkvara sisaldab ka märksõnade otsingufunktsiooni koos rippmenüüga.

![DATA-CREATOR-PY](assets/fr/47.webp)

Kui kõik andmed on sisestatud ja üle kontrollitud, klõpsake nuppu "Create Tutorial", et kinnitada õpetuse failide loomine. See loob kohapeal teie õpetuse kausta ja kõik vajalikud failid valitud kategooria sees.

![DATA-CREATOR-PY](assets/fr/48.webp)

Nüüd võite vahele jätta alajaotuse "Ilma minu Python-skriptita" ja ka 3. sammu "YAML-faili täitmine", kuna skript on need toimingud juba automaatselt teie eest teinud. Jätkake otse 4. sammuga ja alustage oma õpetuse kirjutamist.

Lisateavet selle Python-skripti kohta leiate ka [README-failist](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Sans mon script Python
Ouvrez votre gestionnaire de fichiers et dirigez-vous vers le dossier `bitcoin-educational-content`, qui représente le clone local de votre dépôt. Vous devriez normalement le trouver sous `Documents\GitHub\bitcoin-educational-content`.
Au sein de ce répertoire, il sera nécessaire de localiser le sous-dossier adéquat pour le placement de votre tutoriel. L'organisation des dossiers reflète les différentes sections du site web Plan ₿ Network. Dans notre exemple, puisque nous souhaitons ajouter un tutoriel sur Sparrow Wallet, il convient de se rendre dans le chemin suivant : `bitcoin-educational-content\tutorials\wallet` qui correspond à la section `WALLET` sur le site web :
![TUTO](assets/fr/12.webp)

Kausta `wallet` sees tuleb luua uus kataloog, mis on spetsiaalselt pühendatud teie õpetusele. Selle kausta nimi peaks meenutama õpetuses käsitletavat tarkvara, ühendades sõnad kindlasti kriipsudega. Minu näite puhul saab kausta pealkirjaks `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

Sellesse uude alamkataloogi, mis on pühendatud teie õpetusele, tuleb lisada mitu elementi:


- Looge kaust `assets`, mis on mõeldud kõigi teie õpetuse jaoks vajalike illustratsioonide jaoks;
- Selles kaustas `assets` tuleb luua alamkaust, mille nimi vastab õpetuse algsele keelekoodile. Näiteks kui õpetus on kirjutatud inglise keeles, peab selle alamkataloogi nimi olema `en`. Asetage sinna kõik õpetuse visuaalsed materjalid (diagrammid, pildid, ekraanipildid jne).
- Tuleb luua fail `tutorial.yml`, et salvestada oma õpetusega seotud üksikasjad;
- Markdown-vormingus fail tuleb luua, et kirjutada oma õpetuse tegelik sisu. See fail peab olema pealkirjastatud vastavalt kirjutamise keelekoodile. Näiteks prantsuse keeles kirjutatud õpetuse puhul peab faili nimi olema `fr.md`.

![TUTO](assets/fr/14.webp)

Kokkuvõttes on siin failide hierarhia, mida tuleb luua:

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

## 3 - Täitke YAML-faili

Täitke fail `tutorial.yml`, kopeerides järgmise malli:

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

Siin on esitatud andmed kohustuslike väljade kohta:


- **id**: UUID (_Universally Universally Unique Identifier_), mis võimaldab juhendmaterjali üheselt identifitseerida. Selle saate genereerida [veebipõhise tööriistaga](https://www.uuidgenerator.net/version4). Ainus nõue on, et see UUID oleks juhuslik, et vältida konflikti mõne teise UUID-ga platvormil;
- **project_id**: UUID: õpetuses esitatud tööriista taga oleva ettevõtte või organisatsiooni UUID [projektide nimekirjast](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Näiteks kui te loote õpetust Sparrow Wallet tarkvara kohta, leiate selle `project_id` järgmisest failist: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. See teave lisatakse teie õpetuse YAML-faili, sest Plan ₿ Network haldab andmebaasi kõigi Bitcoini või sellega seotud projektidega tegelevate ettevõtete ja organisatsioonide kohta. Lisades `project_id` teie juhendmaterjaliga seotud üksuse, loote kahe elemendi vahel lingi;
- **tags**: 2 või 3 asjakohast märksõna, mis on seotud õpetuse sisuga ja mis on valitud eranditult [Plan ₿ Network'i siltide nimekirjast](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: Õpetuse sisule vastav alamkategooria vastavalt Plan ₿ Network saidi struktuurile (näiteks rahakottide puhul: `desktop`, `hardware`, `mobile`, `backup`);
- **level**: Õpetuse raskusaste:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: Teie `contributor_id` (BIP39 sõnad), nagu on näidatud [teie professori profiilis](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **original_language**: Õpetuse originaalkeel (näiteks `fr`, `en` jne);
- **proofreading***: Teave korrektuuriprotsessi kohta. Täitke esimene osa, sest teie enda juhendmaterjali korrektuur loetakse esimeseks kinnitamiseks:
    - **language**: Korrektuuri keelekood (näiteks `fr`, `en` jne).
    - **last_contribution_date**: Tänane kuupäev.
    - **urgency**: Jäta tühjaks.
    - **contributors_id**: Teie GitHub ID.
    - **reward**: Jäta tühjaks.

Lisateavet oma professori identifikaatori kohta leiate vastavast juhendmaterjalist:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Siin on näide valminud `tutorial.yml` failist Blockstream Green rahakoti õpetuse jaoks:

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
name: [pealkiri]
description: [Kirjeldus]
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