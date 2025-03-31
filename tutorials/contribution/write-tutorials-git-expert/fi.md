---
name: Contribution - Git-opastus (edistyneet)
description: Opas edistyneille käyttäjille, joka tarjoaa opastuksen Plan ₿ Network with Git -ohjelmasta
---
![cover](assets/cover.webp)

Ennen kuin seuraat tätä ohjeistusta uuden ohjeen lisäämisestä, sinun on suoritettava muutama alustava vaihe. Jos et ole vielä tehnyt sitä, tutustu ensin tähän johdantooppaaseen ja palaa sitten tänne :

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Sinulla on jo :


- Valitse opetusohjelmasi teema;
- Ota yhteyttä Plan ₿ Network -tiimiin [Telegram-ryhmässä] (https://t.me/PlanBNetwork_ContentBuilder) tai paolo@planb.network ;
- Valitse osallistumisvälineesi.

Tässä kokeneille Git-käyttäjille suunnatussa opetusohjelmassa kerromme lyhyesti keskeiset vaiheet ja olennaiset ohjeet uuden Plan ₿ Network -oppaan tarjoamiseksi. Jos Git ja GitHub eivät ole sinulle tuttuja, suosittelen sen sijaan seuraamaan yhtä näistä kahdesta muusta yksityiskohtaisemmasta opetusohjelmasta, jotka vievät sinut askel askeleelta :


- Keskitason (GitHub Desktop)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Aloittelijoille (verkkokäyttöliittymä)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Ehdotetut työkalut

Markdown-tiedostojen muokkaamiseen :


- Obsidian** (ilmainen, ei avointa lähdekoodia)
- Mark Text** (ilmainen, avoin lähdekoodi)
- Zettlr** (ilmainen, avoin lähdekoodi)
- Typora** (maksullinen, ~15 €, ei avointa lähdekoodia)

Gitille :


- Git** (ilmainen, avoin lähdekoodi)
- GitHub Desktop** (ilmainen, avoin lähdekoodi)
- Sourcetree** (ilmainen, ei avoin lähdekoodi)

YAML-tiedostojen muokkaamiseen :


- Visual Studio Code** (ilmainen, avoin lähdekoodi)
- Sublime Text** (ilmainen rajoituksin, ei avointa lähdekoodia)

Kaavioiden ja visuaalisten esitysten luominen :


- Canva** (ilmainen ja maksullisia vaihtoehtoja, ei avointa lähdekoodia)
- Inkscape** (ilmainen, avoin lähdekoodi)
- Penpot** (ilmainen, avoin lähdekoodi)

## Työnkulut

### 1 - Määritä paikallinen ympäristö


- Sinulla on oltava oma haarasi [Plan ₿ Network -tietovarastosta GitHubissa](https://github.com/PlanB-Network/bitcoin-educational-content).
- Synkronoi haarasi päähaara (`dev`) lähdekoodivaraston kanssa.
- Päivitä paikallinen kloonisi.

```
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

### 2 - Luo uusi haara


- Varmista, että olet `dev`-haarassa.
- Luo uusi haara kuvaavalla nimellä (esim. `tuto-green-wallet-loic`).
- Julkaise tämä haara verkkohaarassasi.

```
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Lisää opetusdokumentit

***Huomautus:*** Voit automatisoida vaiheet 3 ja 4 käyttämällä [Python GUI -skriptiäni](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Suorita se suoraan sen kansiosta paikallisessa kloonissasi ja täytä sitten vaaditut kentät graafisessa käyttöliittymässä. Lisätietoja sen asentamisesta ja käyttämisestä on [README]-julkaisussa(https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Jos haluat tehdä sen manuaalisesti, noudata seuraavia ohjeita :


- Etsi sopiva kansio paikallisesta arkistosta (esim. `tutorials/wallet`).
- Luo opetusohjelmalle oma hakemisto, jolla on selkeä nimi (esim. `green-wallet`). Tämä kansion nimi määrittää myös opetusohjelman URL-polun. Sen tulisi olla pienaakkosin, ilman erikoismerkkejä (paitsi väliviivoja) ja ilman välilyöntejä.
- Lisää tähän hakemistoon seuraavat kohteet:
    - Alikansio nimeltä `assets`, joka sisältää :
        - Kaksi .webp-kuvaa:
            - `logo.webp`: (neliön muotoinen ja taustalla). Logon on edustettava esiteltyä ohjelmistoa tai työkalua. Jos opetusohjelma ei koske tiettyä työkalua (esim. yleinen opas muistisanojen luomiseen), voit valita sopivan visuaalisen ilmeen (esim. yleisen kuvakkeen).
            - `cover.webp`: Kannen kuva, joka näytetään opetusohjelman alussa.
        - Alikansio, jossa on opetusohjelman alkuperäisen kielen koodi. Jos opetusohjelma on esimerkiksi kirjoitettu englanniksi, tämän alikansion nimi on `en'. Sijoita kaikki opetusohjelman visuaalinen materiaali (kaaviot, kuvat, kuvakaappaukset jne.) tähän kansioon.
    - `tutorial.yml`-tiedosto, joka sisältää metatietoja (tekijä, tunnisteet, kategoria, vaikeustaso jne.).
    - Markdown-tiedosto, joka sisältää opetusohjelman ja joka on nimetty kielikoodin mukaan (esim. `fr.md`, `en.md`, jne.).

```
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

### 4 - Täytä YAML-tiedosto


- Täydennä `tutorial.yml`-tiedosto seuraavasti:

```
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

professor_id:

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributor_names:
      - 
    reward:
```

Tässä ovat pakolliset kentät:

- **id** : UUID (_Universally Unique Identifier_), joka yksilöi tutoriaalin. Voit luoda sen käyttämällä [verkkotyökalua](https://www.uuidgenerator.net/version4). Ainoa vaatimus on, että tämä UUID on satunnainen, jotta vältytään ristiriidoilta toisen UUID:n kanssa alustalla;

- **project_id** : Yrityksen tai organisaation UUID, joka liittyy tutoriaalissa esiteltyyn työkaluun [projektien luettelosta](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Jos esimerkiksi luot oppaan Green Wallet -ohjelmistosta, voit löytää tämän `project_id` seuraavasta tiedostosta: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Tämä tieto lisätään tutoriaalin YAML-tiedostoon, koska Plan ₿ Network ylläpitää tietokantaa kaikista Bitcoinin tai siihen liittyvien projektien kanssa toimivista yrityksistä ja organisaatioista. Lisäämällä oppaasi liittyvän yksikön `project_id`, luot linkin kahden elementin välille;

- **tags** : 2 tai 3 aiheeseen liittyvää avainsanaa, jotka valitaan yksinomaan [Plan ₿ Networkin avainsanaluettelosta](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category** : Alakategoria, joka vastaa tutoriaalin sisältöä Plan ₿ Network -sivuston rakenteen mukaisesti (esimerkiksi lompakoille: `desktop`, `hardware`, `mobile`, `backup`);

- **level** : Tutoriaalin vaikeustaso, valittavissa seuraavista:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id** : Sinun `professor_id` (UUID), joka näkyy [professoriprofiilissasi](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language** : Oppaan alkuperäinen kieli (esimerkiksi `fr`, `en`, jne.);

- **proofreading** : Tietoja oikolukuprosessista. Täytä ensimmäinen osa, koska oman oppaan oikoluku lasketaan ensimmäiseksi tarkistukseksi:
    - **language** : Oikoluvun kielikoodi (esimerkiksi `fr`, `en`, jne.).
    - **last_contribution_date** : Tämän päivän päivämäärä.
    - **urgency** : 1
    - **contributor_names** : Sinun GitHub ID.
    - **reward** : 0

Lisätietoja opettajatunnuksesta saat vastaavasta ohjeesta :

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
  - wallets
  - software
  - keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
  - language: fr
    last_contribution_date: 2024-11-20
    urgency: 1
    contributor_names:
      - LoicPandul
    reward: 0
```

### 5 - Kirjoita sisältö


- Täydennä Markdown-tiedoston ominaisuudet komennolla :
    - Otsikko (`name`).
    - Lyhyt kuvaus (`description`).
- Lisää kansilehden kuva ohjeen yläosaan Markdown-syntaksilla (korvaa "vihreä" näytetyn työkalun nimellä):

```
![cover-green](assets/cover.webp)
```


- Kirjoita opetusohjelman sisältö Markdown-kielellä :
    - Käytä hyvin jäsenneltyjä otsikoita (`##`), luetteloita ja kohtia.
    - Sisällytä visuaalisia elementtejä Markdown-syntaksin avulla :

```
![nom-image](assets/en/001.webp)
```


- Sijoita kaaviot ja kuvat vastaavaan kieliseen alikansioon `/assets`.

### 6 - Tallenna ja lähetä opetusohjelma


- Tallenna muutoksesi paikallisesti luomalla komento, jossa on kuvaava viesti.
- Työnnä muutokset GitHub-haarukkaan.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Kun olet valmis, luo Pull Request (PR) GitHubiin ehdottaaksesi muutosten integrointia.
- Lisää PR:lle otsikko ja lyhyt kuvaus. Mainitse kommentissa vastaava ongelmanumero.

### 7 - Tarkistaminen ja yhdistäminen


- Odota vahvistusta tai palautetta ylläpitäjältä.
- Tee tarvittaessa korjauksia ja siirrä uudet toimitukset.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Kun PR on yhdistetty, voit poistaa työhaarasi.

## Sisällön luomista koskevat standardit


- Alustan tukema muotoilu** :
    - Klassinen Markdown: luettelot, linkit, kuvat, lainaukset, lihavointi, kursivointi jne.
    - LaTeX (vain lohko, ei inline): erotetaan `$$`:lla.
    - Rivikoodi: Syntaksi, jossa on yksi takaviiva.
    - Koodilohkot: Syntaksi, jossa on kolme takaviivaa, esimerkiksi :

```
print("Hello, Bitcoin!")
```


- Kuvitukset ja kaaviot** :
    - Kaikkien kuvien on oltava WebP-muodossa. Käytä tätä ilmaista työkalua niiden muuntamiseen tarvittaessa: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Nimeä kuvatunnukset 2- tai 3-numeroisin numeroin (esim. `001.webp`, `002.webp`).
    - Mobiililompakon tai laitteiston lompakon opetusohjelmissa kannattaa käyttää malleja.
    - Käytä vain itse luotua tai rojaltivapaata kuvamateriaalia.
    - Varmista, että ne ovat merkityksellisiä ja laadukkaita.
- Graafinen charter** :
    - Fontti: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Värit Suunnitelma ₿ Verkko :
        - Oranssi: `#FF5C00`
        - Musta: `#000000`
        - Valkoinen: `#FFFFFFFF`

Jos sinulla on teknisiä ongelmia opetusohjelmasi lähettämisessä, älä epäröi pyytää apua [omassa Telegram-ryhmässämme](https://t.me/PlanBNetwork_ContentBuilder). Kiitos paljon!