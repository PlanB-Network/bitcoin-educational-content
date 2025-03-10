---
name: Panus - GitHubi töölaua õpetus (vahepealne)
description: Täielik juhend Plan ₿ Network tutorials koos GitHub Desktopiga
---
![cover](assets/cover.webp)

Enne uue õpetuse lisamise õpetuse järgimist peate olema läbinud mõned esialgsed sammud. Kui te pole seda veel teinud, vaadake esmalt seda sissejuhatavat õpetust ja tulge siis siia tagasi:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Sul on juba olemas :


- Valige oma õpetuse jaoks teema;
- Võtke ühendust Plan ₿ Network meeskonnaga [Telegram grupi](https://t.me/PlanBNetwork_ContentBuilder) või paolo@planb.network kaudu;
- Valige oma panustamise vahendid.

Selles õpetuses vaatame, kuidas lisada oma õpetus Plan ₿ Network'ile, konfigureerides oma lokaalse keskkonna GitHub Desktopiga. Kui olete Gitiga juba kursis, ei pruugi see väga üksikasjalik õpetus teile vajalik olla. Selle asemel soovitan teil vaadata seda teist õpetust, kus ma esitan ainult üldised suunised, ilma üksikasjalike samm-sammult juhenditeta :


- Kogenud kasutajad** :

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Kui te ei soovi oma lokaalset keskkonda konfigureerida, järgige seda teist, algajatele mõeldud õpetust, kus me teeme muudatused otse GitHubi veebiliidese kaudu :


- Algajad (veebiliides)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Eeltingimused

Selle õpetuse järgimiseks vajalik tarkvara :


- [GitHub Desktop](https://desktop.github.com/);
- Markdown-failide redaktor, näiteks [Obsidian](https://obsidian.md/);
- Koodiredaktor ([VSC](https://code.visualstudio.com/) või [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Eeltingimused enne õpetuse alustamist :


- Kas teil on [GitHubi konto](https://github.com/signup);
- On olemas [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- Omada [õpetaja profiili Plan ₿ Network](https://planb.network/professors) (ainult juhul, kui pakute täielikku õpetust).

Kui vajate abi nende eelduste hankimisel, siis aitavad teid minu teised õpetused:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Kui kõik on paigas ja teie kohalik keskkond on seadistatud oma Plan ₿ Network forkiga, võite alustada õpetuse lisamist.

## 1 - Uue haru loomine

Avage oma brauser ja navigeerige oma hargnemislehele Plan ₿ Network repositooriumis. See on teie poolt GitHubis loodud haru. Teie hargnemise URL peaks välja nägema selline: `https://github.com/[teie-kasutajanimi]/bitcoin-õppematerjal` :

![TUTO](assets/fr/03.webp)

Veenduge, et olete peamisel `dev` harul, seejärel klõpsake nupul `Sync fork`. Kui teie haru ei ole ajakohane, palub GitHub teil oma haru uuendada. Jätkake selle uuendamisega. Kui aga teie haru on juba ajakohane, teavitab GitHub teid sellest:

![TUTO](assets/fr/04.webp)

Avage GitHubi töölaud ja veenduge, et teie fork on õigesti valitud akna vasakus ülanurgas:

![TUTO](assets/fr/05.webp)

Klõpsake nupul "Tooge päritolu". Kui teie kohalik repositoorium on juba ajakohane, ei paku GitHub Desktop mingeid täiendavaid meetmeid. Vastasel juhul ilmub valik `Pull origin`. Klõpsake sellel nupul, et oma kohalikku repositooriumi uuendada:

![TUTO](assets/fr/06.webp)

Kontrollige, et te olete `dev` põhiharus:

![TUTO](assets/fr/07.webp)

Klõpsake sellel harul, seejärel klõpsake nupule "Uus haru":

![TUTO](assets/fr/08.webp)

Veenduge, et uus haru põhineb lähtekirjanduse repositooriumil, st `PlanB-Network/bitcoin-educational-content`.

Nimetage oma filiaal nii, et pealkiri oleks selge, kasutades sidekriipsu, et eraldada iga sõna. Ütleme näiteks, et meie eesmärk on kirjutada õpetus Sparrow rahakoti kasutamise kohta. Sellisel juhul võiks selle õpetuse kirjutamisele pühendatud tööharu nimetada: `tuto-sparrow-wallet-loic`. Kui olete sisestanud sobiva nime, klõpsake haru loomise kinnitamiseks nuppu `Loo haru`:

![TUTO](assets/fr/09.webp)

Nüüd klõpsa nupule `Publish branch`, et salvestada oma uus tööharu GitHubi veebiharule:

![TUTO](assets/fr/10.webp)

Nüüd peaksite GitHubi töölaual olema oma uues harus. See tähendab, et kõik teie arvutis lokaalselt tehtud muudatused salvestatakse ainult sellesse konkreetsesse harusse. Samuti, seni kuni see haru on GitHubi töölaual valitud, vastavad teie arvutis lokaalselt nähtavad failid selle haru (`tuto-sparrow-wallet-loic`), mitte põhiharu (`dev`) failidele.

![TUTO](assets/fr/11.webp)

Iga uue artikli jaoks, mida soovite avaldada, peate looma uue haru `dev`st. Haru on Gitis projekti paralleelversioon, mis võimaldab teil teha muudatusi, ilma et see mõjutaks põhiharu, kuni töö on valmis ühendamiseks.

## 2 - Lisa õpetusfailid

Nüüd, kui tööharu on loodud, on aeg integreerida oma uus õpetus. Teil on kaks võimalust: kasutada minu Python-skripti, mis automatiseerib vajalike dokumentide loomise, või luua iga fail käsitsi. Vaatame mõlema võimaluse puhul järgitavaid samme.

### Minu Python skriptiga

Teil on vaja paigaldada :


- Python 3.8 või uuem ;
- Skripti jaoks vajalikud sõltuvused. Käivita :

```bash
pip install customtkinter appdirs
````
Pour utiliser le script, rendez-vous dans le dossier où il est stocké. Le script se trouve dans le dépôt de data de Plan ₿ Network sous le chemin : `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.
Une fois dans le dossier, exécutez la commande :
```

python new-tutorial-creation.py

```
Une interface graphique (GUI) va s'ouvrir. La première fois, vous devrez entrer toutes les informations nécessaires, mais lors des utilisations ultérieures du script, vos informations personnelles seront mémorisées, ce qui vous évite de devoir les saisir de nouveau.
![TUTO](assets/fr/37.webp)
Commencez par indiquer le chemin local menant au dossier `/tutorials` sur votre clone du dépôt (`.../bitcoin-educational-content/tutorials/`). Vous pouvez le noter manuellement ou cliquer sur le bouton "Browse" pour naviguer via votre explorateur de fichiers.
![TUTO](assets/fr/38.webp)
Sélectionnez la langue dans laquelle vous rédigerez votre tutoriel.
![TUTO](assets/fr/39.webp)
Choisissez une catégorie principale pour votre tutoriel.
![TUTO](assets/fr/40.webp)
Ensuite, sélectionnez une sous-catégorie appropriée, en fonction de la catégorie principale que vous avez choisie.
![TUTO](assets/fr/41.webp)
Déterminez un niveau de difficulté pour le tutoriel.
![TUTO](assets/fr/42.webp)
Choisissez le nom du répertoire spécialement créé pour votre tutoriel. Le nom de ce dossier devrait refléter le logiciel abordé dans le tutoriel, en utilisant des tirets pour relier les mots. Par exemple, le dossier pourrait s'appeler `red-wallet` :
![TUTO](assets/fr/43.webp)
Le `project_id` est l'UUID de l'entreprise ou de l'organisation derrière l'outil présenté dans le tutoriel, disponible [dans la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, pour un tutoriel sur le logiciel Sparrow Wallet, vous trouverez ce `project_id` dans le fichier : `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Cette information est ajoutée au fichier YAML de votre tutoriel car Plan ₿ Network maintient une base de données des entreprises et organisations actives sur Bitcoin ou des projets connexes. En ajoutant le `project_id` associé à votre tutoriel, vous créez un lien entre votre contenu et l'entité concernée.
***Mise à jour :*** Dans la nouvelle version du script, vous n'avez plus besoin de saisir manuellement le `project_id`. Une fonction de recherche a été ajoutée pour trouver le projet par son nom et récupérer automatiquement le `project_id` correspondant. Tapez le début du nom du projet dans la case "Project name" pour le rechercher, puis sélectionnez l'entreprise souhaitée dans le menu déroulant. Le `project_id` sera automatiquement renseigné dans la case en dessous. Vous avez également la possibilité de le noter manuellement si nécessaire.
![TUTO](assets/fr/44.webp)
Pour les tags, sélectionnez 2 ou 3 mots-clés pertinents en relation avec le contenu de votre tutoriel, en les choisissant exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).
![TUTO](assets/fr/45.webp)
Dans la case "Contributor's GitHub ID", inscrivez votre identifiant GitHub.
![TUTO](assets/fr/46.webp)
Pour la case "PBN professor's ID", saisissez votre identifiant en utilisant les mots de la liste BIP39, tel qu'il apparaît sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).
![TUTO](assets/fr/47.webp)
Pour plus de détails sur votre identifiant de professeur, veuillez consulter le tutoriel suivant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Une fois toutes les informations saisies et vérifiées, cliquez sur "Create Tutorial" pour valider la création des fichiers de votre tutoriel. Cela générera en local le dossier de votre tutoriel et tous les fichiers nécessaires dans le dossier de la catégorie sélectionnée.
![TUTO](assets/fr/48.webp)
Vous pouvez maintenant passer outre la sous-partie "Sans mon script Python", ainsi que l'étape 3 "Remplir le fichier YAML", car le script a déjà effectué ces actions automatiquement pour vous. Passez directement à l'étape 4 et à la rédaction de votre tutoriel.
Pour plus d'informations sur ce script Python, vous pouvez également [consulter son README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).
### Sans mon script Python
Ouvrez votre gestionnaire de fichiers et dirigez-vous vers le dossier `bitcoin-educational-content`, qui représente le clone local de votre dépôt. Vous devriez normalement le trouver sous `Documents\GitHub\bitcoin-educational-content`.
Au sein de ce répertoire, il sera nécessaire de localiser le sous-dossier adéquat pour le placement de votre tutoriel. L'organisation des dossiers reflète les différentes sections du site web Plan ₿ Network. Dans notre exemple, puisque nous souhaitons ajouter un tutoriel sur Sparrow Wallet, il convient de se rendre dans le chemin suivant : `bitcoin-educational-content\tutorials\wallet` qui correspond à la section `WALLET` sur le site web :
![TUTO](assets/fr/12.webp)
Au sein du dossier `wallet`, il faut créer un nouveau répertoire spécifiquement dédié à votre tutoriel. Le nom de ce dossier doit évoquer le logiciel traité dans le tutoriel, en veillant à relier les mots par des tirets. Pour mon exemple, le dossier sera intitulé `sparrow-wallet` :
![TUTO](assets/fr/13.webp)
Dans ce nouveau sous-dossier dédié à votre tutoriel, il faut ajouter plusieurs éléments :
- Créez un dossier `assets`, destiné à recevoir toutes les illustrations nécessaires à votre tutoriel ;
- Au sein de ce dossier `assets`, il faut créer un sous-dossier nommé selon le code de langue originale du tutoriel. Par exemple, si le tutoriel est rédigé en anglais, ce sous-dossier doit être nommé `en`. Placez-y tous les visuels du tutoriel (schémas, images, captures d’écran, etc.).
- Un fichier `tutorial.yml` doit être créé pour y consigner les détails relatifs à votre tutoriel ;
- Un fichier en format markdown est à créer pour y rédiger le contenu effectif de votre tutoriel. Ce fichier doit être intitulé selon le code de la langue de rédaction. Par exemple, pour un tutoriel rédigé en français, le fichier devra s'appeler `fr.md`.
![TUTO](assets/fr/14.webp)
Pour résumer, voici la hiérarchie des fichiers à créer :
```

bitcoin-educational-content/

└── juhendid/

└── rahakott/ (vahetage õigesse kategooriasse)

└ └── varblik-võru/ (modify with tuto name)

├── vara/

│ ├── en/ (vahetage sobiv keelekood)

├─ tutorial.yml

└── fr.md (tuleb muuta vastavalt vastavale keelekoodile)

```
## 3 - Remplir le fichier YAML
Remplissez le fichier `tutorial.yml` en copiant le modèle suivant :
```

id:

project_id:

sildid:

-

-

-

kategooria:

tase:

krediit:

professor:

# Metaandmete korrektuur

originaal_keel:

korrektuur:


  - keel:

viimane_makse_kuupäev:

kiireloomulisus:

toetajad_id:

-

tasu:

````

Siin on nõutavad väljad:


- id**: UUID (_Universally Universally Unique Identifier_), mis identifitseerib õpetuse üheselt. Selle saate genereerida [veebipõhise tööriistaga](https://www.uuidgenerator.net/version4). Ainus piirang on see, et see UUID peab olema juhuslik, et see ei satuks vastuollu mõne teise platvormi UUID-ga;
- project_id** : Õpetuses esitatud tööriista taga oleva ettevõtte või organisatsiooni UUID [projektide nimekirjast](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Näiteks kui teete õpetust Sparrow Wallet tarkvara kohta, siis leiate selle `project_id` järgmisest failist: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. See teave lisatakse teie õpetuse YAML-faili, sest Plan ₿ Network säilitab andmebaasi kõigi Bitcoini või sellega seotud projektidega tegelevate ettevõtete ja organisatsioonide kohta. Lisades oma juhendmaterjalile lingitud üksuse `project_id`, loote kahe elemendi vahel lingi;
- sildid**: 2 või 3 asjakohast märksõna, mis on seotud õpetuse sisuga ja mis on valitud eranditult [Plan ₿ Network tag'ide nimekirjast](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- kategooria** : Õpetuse sisule vastav alamkategooria vastavalt kava ₿ võrgu struktuurile (nt rahakottide puhul: `desktop`, `hardware`, `mobile`, `backup`) ;
- tase** : Õpetuse raskusaste, alates :
    - algaja`
    - "vahepealne
    - "Edasijõudnud
    - "ekspert
- professor**: Teie `contributor_id` (BIP39 sõnad), nagu on näidatud [teie õpetaja profiilis](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- originaal_keel** : Õpetuse originaalkeel (nt `fr`, `en` jne.) ;
- korrektuur**: Teave korrektuuriprotsessi kohta. Täitke esimene osa, sest teie enda juhendmaterjali korrektuur loetakse esimeseks kinnitamiseks:
    - keel**: Keelekoodi korrektuur (nt "fr", "en" jne).
    - viimane_makse_kuupäev**: Tänane kuupäev.
    - kiireloomulisus** : Jäta tühjaks.
    - toetajad_id** : Teie GitHubi ID.
    - tasu** : Jäta tühjaks.

Lisateavet õpetaja ID kohta leiate vastavast juhendmaterjalist :

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Siin on näide `tutorial.yml` failist, mis on valminud Blockstream Green rahakoti õpetuse jaoks:

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
```

Kui olete lõpetanud oma faili `tutorial.yml` redigeerimise, salvestage oma dokument, klõpsates nupule `File > Save` :

![TUTO](assets/fr/16.webp)

Nüüd võite sulgeda koodiredaktori.

## 4 - Täitke Markdown-faili

Nüüd saate avada oma õpetusfaili, mille nimeks on teie keelekood, näiteks `en.md`. Minge Obsidian'i akna vasakul pool ja kerige kaustapuu alla oma õpetuskausta ja soovitud faili juurde :

![TUTO](assets/fr/18.webp)

Klõpsake faili avamiseks sellel:

![TUTO](assets/fr/19.webp)

Alustame dokumendi ülaosas asuva jaotise "Omadused" täitmisega.

![TUTO](assets/fr/20.webp)

Lisage käsitsi ja täitke järgmine koodiplokk:

```markdown
---
name: [Titre]
description: [Description]
---
```

![TUTO](assets/fr/21.webp)

Täitke oma õpetuse nimi ja lühikirjeldus:

![TUTO](assets/fr/22.webp)

Seejärel lisage tee kaanepildile oma õpetuse alguses. Selleks märkige :

```markdown
![cover-sparrow](assets/cover.webp)
```

See süntaks on kasulik alati, kui teil on vaja lisada pilt oma õpetusele. Hüüumärk tähistab pilti, mille alternatiivne tekst (alt) on määratud nurksulgude vahele. Sulgude vahel on märgitud pildi tee:

![TUTO](assets/fr/23.webp)

## 5 - Lisage logo ja kate

Kausta `assets` sisse tuleb lisada fail nimega `logo.webp`, mis on teie artikli pisipildiks. See pilt peab olema `.webp` formaadis ja ruudukujuline, et see sobiks kasutajaliidesega. Võite vabalt valida õpetuses käsitletava tarkvara logo või mõne muu asjakohase pildi, kui see on kasutustasuta. Lisaks lisage samasse kohta pilt pealkirjaga `cover.webp`. See kuvatakse teie õpetuse ülaosas. Veenduge, et see pilt, nagu ka logo, austaks kasutusõigusi ja oleks teie õpetuse konteksti sobiv:

![TUTO](assets/fr/17.webp)

## 6 - Õpetuse kirjutamine ja visuaalide lisamine

Jätkake oma õpetuse sisu kirjutamist. Kui soovite lisada alapealkirja, rakendage asjakohast markdown-vormingut, lisades tekstile eesliite `##` :

![TUTO](assets/fr/24.webp)

Kausta `assets` allkausta language kasutatakse teie õpetusega kaasas olevate diagrammide ja visuaalsete materjalide salvestamiseks. Vältige võimaluse korral teksti lisamist oma piltidele, et muuta sisu rahvusvahelisele publikule kättesaadavaks. Loomulikult sisaldab esitletav tarkvara teksti, kuid kui lisate tarkvara ekraanipiltidele skeeme või lisamärkusi, siis tehke seda ilma tekstita või kui see on hädavajalik, siis kasutage inglise keelt.

![TUTO](assets/fr/25.webp)

Piltide nimetamiseks kasutage lihtsalt numbreid, mis vastavad nende esinemise järjekorrale õpetuses ja on vormistatud kahekohalise numbriga (või kolmekohalise numbriga, kui teie õpetus sisaldab rohkem kui 99 pilti). Näiteks nimetage oma esimene pilt `01.webp`, teine `02.webp` jne.

Teie pildid peavad olema ainult .webp formaadis. Vajaduse korral võite kasutada [minu pildikonversioonitarkvara](https://github.com/LoicPandul/ImagesConverter).

![TUTO](assets/fr/26.webp)

Diagrammi lisamiseks oma dokumenti kasutage Markdownis järgmist käsku, hoolitsedes nii sobiva alternatiivse teksti kui ka õige pildi tee määramise eest:

```markdown
![sparrow](assets/fr/01.webp)
```

Alguses olev hüüumärk tähistab pilti. Alternatiivne tekst, mis aitab ligipääsetavust ja viitamist, on paigutatud nurksulgude vahele. Lõpuks on sulgude vahel näidatud pildi tee.

Kui soovite luua omaenda skeeme, järgige kindlasti Plan ₿ Network graafilisi suuniseid, et tagada visuaalne järjepidevus:


- Font**: [Rubik](https://fonts.google.com/specimen/Rubik);
- Värvid** :
 - Oranž: #FF5C00
 - Must : #000000
 - Valge: #FFFFFF

**On oluline, et kõik teie õppematerjalidesse integreeritud visuaalid oleksid autoriõiguseta või järgiksid lähtefailide litsentsi**. Seetõttu on kõik Plan ₿ Network'is avaldatud diagrammid tehtud kättesaadavaks CC-BY-SA litsentsi alusel, samamoodi nagu tekst.

**-> Vihje:** Kui jagate faile avalikult, näiteks pilte, on oluline eemaldada üleliigsed metaandmed. Need võivad sisaldada tundlikku teavet, näiteks asukohaandmed, loomise kuupäevad ja autori andmed. Privaatsuse kaitsmiseks on hea mõte need metaandmed eemaldada. Selle toimingu lihtsustamiseks saate kasutada spetsiaalseid tööriistu, näiteks [Exif Cleaner] (https://exifcleaner.com/), mis võimaldab dokumendi metaandmeid lihtsa lohistamisega puhastada.

## 7 - Salvesta ja tee ettepanek õpetuse kohta

Kui olete lõpetanud oma õpetuse kirjutamise valitud keeles, on järgmine samm esitada **Tõmbepäring**. Seejärel lisab administraator teie õpetusele puuduvad tõlked, kasutades meie automaatset tõlkemeetodit koos inimtoimelise korrektuuriga.

Pull Request'i tegemiseks avage GitHub Desktop. Tarkvara peaks automaatselt tuvastama kõik muudatused, mida olete teinud lokaalselt oma harus algsesse repositooriumi. Enne jätkamist kontrollige hoolikalt kasutajaliidese vasakul poolel, et need muudatused vastaksid teie ootustele:

![TUTO](assets/fr/28.webp)

Lisage oma muudatuste pealkiri, seejärel klõpsake sinist nuppu `Commit to [your branch]`, et need muudatused kinnitada:

![TUTO](assets/fr/29.webp)

Commit on harus tehtud muudatuste kirje, millele on lisatud kirjeldav sõnum, mis võimaldab teil jälgida projekti arengut aja jooksul. See on omamoodi vahepealne kontrollpunkt.

Seejärel klõpsake nupule "Push origin". See saadab teie faili oma hargnemisele:

![TUTO](assets/fr/30.webp)

Kui te ei ole oma õpetust veel lõpetanud, võite hiljem selle juurde tagasi tulla ja teha uusi kommenteerimisi. Kui olete selle haru redigeerimise lõpetanud, klõpsake nupule `Preview Pull Request`:

![TUTO](assets/fr/31.webp)

Saate veelkord kontrollida, et teie muudatused on õiged, seejärel klõpsake nupule `Create pull request` (loo tõmbetaotlus):

![TUTO](assets/fr/32.webp)

Pull Request on taotlus, mis on tehtud teie haru muudatuste integreerimiseks Plan ₿ Network'i repositooriumi põhiharusse, mis võimaldab muudatusi enne nende ühendamist üle vaadata ja arutada.

Teid suunatakse automaatselt teie brauseris GitHubi oma Pull Requesti ettevalmistamise lehele :

![TUTO](assets/fr/33.webp)

Sisestage pealkiri, mis võtab lühidalt kokku muudatused, mida soovite allikarepositooriumiga ühendada. Lisage lühike kommentaar, mis kirjeldab neid muudatusi (kui teie juhendmaterjali loomisega on seotud probleemi number, ärge unustage märkida kommentaariks `Lõpetab #{väljaande number}`), seejärel vajutage rohelisele nupule `Loo pull request`, et kinnitada ühinemispäring:

![TUTO](assets/fr/34.webp)

Seejärel on teie PR nähtav plaani ₿ võrgu peamise repositooriumi vahekaardil `Pull Request`. Nüüd peate vaid ootama, kuni administraator võtab teiega ühendust, et kinnitada, et teie panus on ühendatud, või nõuda edasisi muudatusi.

![TUTO](assets/fr/35.webp)

Pärast oma PR-i ühendamist peaharuga soovitame kustutada oma tööharu (`tuto-sparrow-wallet`), et säilitada oma haru puhas ajalugu. GitHub pakub teile seda võimalust automaatselt teie PR-lehel:

![TUTO](assets/fr/36.webp)

GitHubi töölaual saate liikuda tagasi oma haru peaharule (`dev`).

![TUTO](assets/fr/07.webp)

Kui soovite oma panust muuta pärast seda, kui olete oma PR-i juba esitanud, sõltuvad järgitavad sammud teie PR-i hetkeseisust:


- Kui teie PR on veel avatud ja seda ei ole veel ühendatud, tehke muudatused lokaalselt, jäädes samasse harusse. Kui muudatused on lõpetatud, kasutage nuppu `Push origin`, et lisada oma veel avatud PR-ile uus kinnitus;
- Kui teie PR on juba ühendatud põhiharuga, peate protsessi uuesti alustama, luues uue haru ja esitades seejärel uue PR-i. Veenduge, et teie kohalik repositoorium on enne jätkamist sünkroniseeritud Plan ₿ võrgu lähtekoodide repositooriumiga.

Kui teil on tehnilisi raskusi oma õpetuse esitamisel, siis paluge julgelt abi [meie spetsiaalses Telegrami grupis](https://t.me/PlanBNetwork_ContentBuilder). Suur tänu!