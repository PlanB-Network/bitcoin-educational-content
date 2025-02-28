---
name: Panus - Git õpetus (edasijõudnutele)
description: Juhend edasijõudnud kasutajatele, et pakkuda õpetust Plan ₿ Network koos Gitiga
---
![cover](assets/cover.webp)

Enne uue õpetuse lisamise õpetuse järgimist peate olema läbinud mõned esialgsed sammud. Kui te pole seda veel teinud, vaadake esmalt seda sissejuhatavat õpetust ja tulge siis siia tagasi:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Sul on juba olemas :


- Valige oma õpetuse jaoks teema;
- Võtke ühendust Plan ₿ Network meeskonnaga [Telegram grupi](https://t.me/PlanBNetwork_ContentBuilder) või paolo@planb.network kaudu;
- Valige oma panustamise vahendid.

Selles kogenud Git-kasutajatele mõeldud õpetuses võtame lühidalt kokku peamised sammud ja olulised suunised uue Plan ₿ Networki õpetuse pakkumiseks. Kui te ei ole Giti ja GitHubiga tuttav, siis soovitan teil selle asemel jälgida ühte neist 2-st teisest, üksikasjalikumast õpetusest, mis viivad teid samm-sammult edasi :


- Vahepealne (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Algajad (veebiliides)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Soovitatavad vahendid

Markdown-failide redigeerimiseks :


- Obsidian** (tasuta, mitte avatud lähtekoodiga)
- Mark Text** (tasuta, avatud lähtekoodiga)
- Zettlr** (tasuta, avatud lähtekoodiga)
- Typora** (tasuline tarkvara, ~15€, mitte avatud lähtekoodiga)

Giti jaoks :


- Git** (tasuta, avatud lähtekoodiga)
- GitHub Desktop** (tasuta, avatud lähtekoodiga)
- Sourcetree** (tasuta, mitte avatud lähtekoodiga)

YAML-failide redigeerimiseks :


- Visual Studio Code** (tasuta, avatud lähtekoodiga)
- Sublime Text** (piirangutega tasuta, mitte avatud lähtekoodiga)

Diagrammide ja visuaalide loomiseks :


- Canva** (tasuta ja tasulised võimalused, mitte avatud lähtekoodiga)
- Inkscape** (tasuta, avatud lähtekoodiga)
- Penpot** (tasuta, avatud lähtekoodiga)

## Töökorraldused

### 1 - Kohaliku keskkonna konfigureerimine


- Teil peab olema oma haru [Plan ₿ Network repository on GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Sünkroniseeri oma hargnemise põhiharu (`dev`) allikarepositooriumiga.
- Uuendage oma kohalikku klooni.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Uue haru loomine


- Veenduge, et olete `dev` harus.
- Loo uus haru kirjeldava nimega (nt `tuto-green-wallet-loic`).
- Avaldage see haru oma võrguharul.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Lisage juhendmaterjalid

***Märkus:*** Sammud 3 ja 4 saab automatiseerida, kasutades [minu Python GUI skripti](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Käivitage see otse selle kaustast oma kohalikus kloonis, seejärel täitke nõutavad väljad GUI-s. Lisateavet selle paigaldamise ja kasutamise kohta leiate [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Kui soovite seda käsitsi teha, järgige järgmisi samme :


- Leidke kohalikust repositooriumist sobiv kaust (nt `tutorials/wallet`).
- Loo õpetusele pühendatud kataloog selge nimega (nt `green-wallet`). See kausta nimi määrab ka õpetuse URL-tee. See peaks olema väiketähtedega, ilma erimärkideta (v.a. sidekriips) ja tühikuteta.
- Lisage sellesse kataloogi järgmised elemendid:
    - Alamkaust nimega `assets`, mis sisaldab :
        - Kaks "webp" pilti:
            - `logo.webp`: Tutoriali logo (ruudukujuline taustaga). See logo peab esindama esitatud tarkvara või tööriista. Kui juhendmaterjal ei ole konkreetselt mingi tööriista kohta (nt: üldine juhendmärksõna genereerimiseks), võite valida sobiva visuaalse kujunduse (nt: üldine ikoon).
            - `cover.webp`: Kaanepilt, mis kuvatakse õpetuse alguses.
        - Alamkataloog, mis sisaldab õpetuse algkeele koodi. Näiteks kui õpetus on kirjutatud inglise keeles, peaks selle alamkataloogi nimi olema `en'. Asetage kõik õpetuse visuaalsed materjalid (diagrammid, pildid, ekraanipildid jne) sellesse kausta.
    - Metaandmeid (autor, sildid, kategooria, raskusaste jne) sisaldav fail `tutorial.yml`.
    - Markdown-fail, mis sisaldab õpetust ja mille nimi vastab keelekoodile (nt `fr.md`, `en.md` jne).

```bash
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Täitke YAML-faili


- Täiendage faili `tutorial.yml` järgmiselt:

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
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

sildid:


  - rahakotid
  - tarkvara
  - võtmed

kategooria: mobiilne

tase: algaja

krediit:

professor: pretty-private

# Metaandmete korrektuur

originaal_keel: fr

korrektuur:


  - keel: fr

last_contribution_date: 2024-11-20

kiireloomulisus:

toetajad_id:


      - LoicPandul

tasu:

```
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# Looge kirjeldava sõnumiga kinnitus

git commit -m "Lisa rohelise rahakoti õpetus"

# Lükake oma muudatused kahvlile

git push origin tuto-green-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Loo commit, mis kirjeldab tehtud parandusi

git commit -m "Parandused pärast rohelise rahakoti õpetuse läbivaatamist"

# Lükake parandusi oma kahvlile

git push origin tuto-green-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Tere, Bitcoin!")

```