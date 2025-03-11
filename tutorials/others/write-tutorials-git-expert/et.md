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

Selles kogenud Git-kasutajatele mõeldud õpetuses võtame lühidalt kokku peamised sammud ja olulised suunised uue Plan ₿ Networki õpetuse pakkumiseks. Kui te ei ole Gitiga ja GitHubiga kursis, soovitan teil selle asemel jälgida ühte neist kahest teisest üksikasjalikumast juhendmaterjalist, mis viivad teid samm-sammult edasi :


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

### 2 - Uue haru loomine


- Veenduge, et olete `dev` harus.
- Loo uus haru kirjeldava nimega (nt `tuto-green-wallet-loic`).
- Avaldage see haru oma võrguharul.

```
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
    - Markdown-fail, mis sisaldab õpetust ja on nimetatud vastavalt keelekoodile (nt `fr.md`, `en.md` jne).

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

### 4 - Täitke YAML-faili


- Täiendage faili `tutorial.yml` järgmiselt:

```
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
```

Siin on nõutavad väljad:


- id**: UUID (_Universally Universally Unique Identifier_), mis identifitseerib õpetuse üheselt. Selle saate genereerida [veebipõhise tööriistaga](https://www.uuidgenerator.net/version4). Ainus piirang on see, et see UUID peab olema juhuslik, et see ei satuks vastuollu mõne teise platvormi UUID-ga;
- project_id** : Õpetuses esitatud tööriista taga oleva ettevõtte või organisatsiooni UUID [projektide nimekirjast](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Näiteks kui teete õpetust Green Wallet tarkvara kohta, siis leiate selle `project_id` järgmisest failist: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. See teave lisatakse teie õpetuse YAML-faili, sest Plan ₿ Network haldab andmebaasi kõigi Bitcoini või sellega seotud projektidega tegelevate ettevõtete ja organisatsioonide kohta. Lisades oma juhendmaterjalile lingitud üksuse `project_id`, loote kahe elemendi vahel lingi;
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

```
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

### 5 - Sisu kirjutamine


- Täitke Markdown-faili omadusi :
    - Pealkiri (`nimi`).
    - Lühikirjeldus (`description`).
- Lisage õpetuse algusesse kaanepilt, kasutades Markdowni süntaksit (asendage "roheline" näidatud tööriista nimega):

```
![cover-green](assets/cover.webp)
```


- Kirjutage õpetuse sisu Markdownis :
    - Kasutage hästi struktureeritud pealkirju (`##`), loetelusid ja lõike.
    - Sisestage visuaalid, kasutades Markdowni süntaksit :

```
![nom-image](assets/en/001.webp)
```


- Asetage diagrammid ja pildid vastavasse keele alamkataloogi, faili `/assets`.

### 6 - Salvesta ja esita juhendmaterjal


- Salvestage oma muudatused lokaalselt, luues kirjeldava sõnumiga commit.
- Lükake muudatused oma GitHubi harusse.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Kui olete lõpetanud, looge GitHubis Pull Request (PR), et teha ettepanek oma muudatuste integreerimiseks.
- Lisage PR-ile pealkiri ja lühikirjeldus. Märkige kommentaaris vastav teema number.

### 7 - Korrektuur ja ühendamine


- Oodake kinnitust või tagasisidet administraatorilt.
- Vajaduse korral tehke parandusi ja lükake uusi kommiteid.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Kui PR on ühendatud, saate oma tööharu kustutada.

## Sisu loomise standardid


- Platvormil toetatud vormindamine** :
    - Klassikaline Markdown: nimekirjad, lingid, pildid, tsitaadid, paksus, kursiiv jne.
    - LaTeX (ainult plokk, mitte inline): piiritletud `$$$`.
    - Inline-kood: Süntaks ühe tagurpidi märgiga.
    - Koodiplokid: Süntaks kolme tagantjärgi, näiteks :

```
print("Hello, Bitcoin!")
```


- Illustratsioonid ja diagrammid** :
    - Kõik pildid peavad olema WebP-vormingus. Vajaduse korral kasutage nende teisendamiseks seda tasuta tööriista: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Nimetage visuaalid kahe või kolme numbriga (nt `001.webp`, `002.webp`).
    - Mobiili- või riistvara rahakotiõpetuse jaoks kasutage mock-up'e.
    - Kasutage ainult ise loodud või kasutustasuta visuaalset materjali.
    - Veenduge, et need on asjakohased ja kvaliteetsed.
- Graafiline harta** :
    - Font: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Värviplaan ₿ Võrk :
        - Oranž: `#FF5C00`
        - Must: `#000000`
        - Valge: `#FFFFFFFF`

Kui teil on tehnilisi raskusi oma õpetuse esitamisel, siis paluge julgelt abi [meie spetsiaalses Telegrami grupis](https://t.me/PlanBNetwork_ContentBuilder). Suur tänu!