---
name: Intambwe - Inyigisho ya Git (iteye imbere)
description: Inyobora ku bakoresha bateye imbere gutanga inyigisho kuri Plan ₿ Academy na Git
---
![cover](assets/cover.webp)


Imbere yo gukurikira iyi nyigisho yo kwongerako inyigisho nshasha, ukeneye kuba wararangije intambwe nkeyi z’intango. Niba utarabikora, ndagusavye banza urabe iyi nyigisho y’intango, hanyuma ugaruke hano:


https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Usanzwe ufise:



- Hitamwo insiguro y’inyigisho yawe;
- Yashikirije ikigo ca Plan ₿ Academy biciye ku [umugwi wa Telegram](https://t.me/Uwukora_Ibirimwo) canke paolo@planb.network ;
- Hitamwo ibikoresho vyawe vy’intererano.


Muri iyi nyigisho y'abakoresha ba Git bazi utuntu n'utundi, tuzoca irya n'ino intambwe nyamukuru n'ingingo ngenderwako z'ingenzi zo gutanga inyigisho nshasha ya Plan ₿ Academy. Niba utazi Git na GitHub, ndagusavye gukurikira imwe muri izi zindi nyigisho 2 zizogutwara intambwe ku yindi:



- Ivy'imbere (GitHub Desktop):


https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- Abatanguje (urubuga):


https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Ibikoresho vyerekanwa


Kugira ngo uhindure amadosiye ya Markdown:



- Obsidian (Ubuntu, si inkomoko yuguruye)
- Inyandiko y'ikimenyetso (Ubuntu, inkomoko yuguruye)
- Zettlr (Ubuntu, inkomoko yuguruye)
- Typora (Igikoresho co kwishura, ~€15, si inkomoko yuguruye)


Ku bwa Git:



- Git (Ubuntu, inkomoko yuguruye)
- GitHub Desktop (Ubuntu, inkomoko yuguruye)
- Igiti c'inkomoko (Ku buntu, si inkomoko yuguruye)


Ku guhindura amadosiye ya YAML:



- Kode ya Visual Studio (Ku buntu, inkomoko yuguruye)
- Umwandiko mwiza (Ubuntu n'imipaka, si inkomoko yuguruye)


Kugira ngo ureme ibishushanyo n'ibishushanyo:



- Canva (Ku buntu n'amahitamwo yishurwa, si inkomoko yuguruye)
- Inkscape (Ubuntu, inkomoko yuguruye)
- Penpot (Ubuntu, inkomoko yuguruye)


## Ugutemba kw'ibikorwa


### 1 - Gutunganya ibidukikije vyawe



- Utegerezwa kuba ufise fork yawe bwite y’[ububiko bwa Plan ₿ Academy kuri GitHub]
- Guhuza ishami ry'ingenzi (`dev`) rya fork yawe n'ububiko bw'inkomoko.
- Vugurura clone yawe yo mu karere.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - Gukora ishami rishasha



- Raba neza ko uri kw'ishami rya `dev`.
- Rema ishami rishasha rifise izina ridondora (nk'akarorero `tuto-icatsi kibisi-wallet-loic`).
- Sohora iri shami kuri fork yawe yo kuri Internet.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - Wongereko inyandiko z'inyigisho


***Iciyumviro:*** Ushobora gukoresha intambwe za 3 na 4 ukoresheje [GUI yanje ya Python script] Ikoreshe uhereye kuri dosiye yayo muri clone yawe yo mu karere, hanyuma wuzuze ibikenewe kuri GUI. Kugira ngo umenye vyinshi ku buryo woyishiramwo no kuyikoresha, raba [SOMA](https://github.com/Irezo-ya-PlanB/ibirimwo-ivy’inyigisho-vy’ibice/blob/dev/scripts/ibijanye n’inyigisho/Irema-ry’inyigisho-nshasha/SOMA-INYUMA.md).


Niba ushaka kubikora n'amaboko, kurikiza izi ntambwe:



- Rondera dosiye ibereye mu bubiko bw'aho hantu (nk'akarorero `inyigisho/wallet`).
- Rema ububiko bwihariye inyigisho bufise izina ritomoye (nk'akarorero `green-wallet`). Izina ry'ububiko rizogena inzira ya URL y'inyigisho. Ikwiye kuba mu nyuguti ntoyi, ata nyuguti zidasanzwe (kiretse uturongo) kandi ata n’ibibanza.
- Yongerako ibi bikurikira kuri ubu bubiko:
    - Ububiko buto bwitwa `itunga` burimwo:
        - Amashusho abiri `.webp`:
            - `logo.webp`: Ikimenyetso c'inyigisho (uburyo bw'akarongo n'inyuma). Ico kimenyetso kigomba guserukira porogarama canke igikoresho kigaragazwa. Niba inyigisho idasanzwe ku gikoresho (nk'akarorero: ubuyobozi rusangi bwo gutanga amajambo y'ukwibuka), ushobora guhitamwo ikintu kibereye (nk'akarorero: ikimenyetso rusangi).
            - `cover.webp`: Ishusho y'igipfukisho yerekanwa mu ntango y'inyigisho.
        - Dosiye ntoyi irimwo kode y'ururimi rw'umwimerere rw'inyigisho. Nk'akarorero, nimba inyigisho yanditswe mu congereza, iyi dosiye ntoyi ikwiye kwitwa `en'. Shira ibishushanyo vyose vy’inyigisho (ibishushanyo, amashusho, amafoto, n’ibindi) muri iyi dosiye.
    - Dosiye `tutorial.yml` irimwo amakuru (umwanditsi, ibimenyetso, urutonde, urugero rw'ingorane, n'ibindi).
    - Dosiye ya Markdown irimwo inyigisho, yitwa hakurikijwe kode y'ururimi (nk'akarorero `fr.md`, `en.md`, n'ibindi).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - Uzuza dosiye ya YAML



- Uzuza dosiye `inyigisho.yml` nk'uko bikurikira:


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


Akira ahantu hakenewe:



- id**: UUID (_Ikimenyetso kidasanzwe co kw'isi yose_) kigaragaza inyigisho mu buryo bwihariye. Ushobora kuyihingura ukoresheje [igikoresho co kuri Internet](https://www. Igisabwa conyene ni uko iyo UUID iba random kugira ngo ntihagire amakimbirane n’iyindi UUID iri kuri platform;



- project_id**: UUID y’ishirahamwe canke ishirahamwe riri inyuma y’igikoresho kigaragazwa mu nyigisho [bivuye ku rutonde rw’imigambi](https://github.com/PlanB-Network/bitcoin-ivy’inyigisho-ibirimwo/igiti/dev/ibikoresho/imigambi). Nk'akarorero, nimba uriko urahingura inyigisho yerekeye porogarama ya Green Wallet, ushobora gusanga iyi `project_id` muri dosiye ikurikira: `bitcoin-ibirimwo-inyigisho/ibikoresho/imigambi/blockstream/project.yml`. Aya makuru yongerwa kuri dosiye ya YAML y’inyigisho yawe kubera ko Plan ₿ Academy ibungabunga urutonde rw’amashirahamwe yose n’imiryango yose ikora kuri Bitcoin canke imigambi ijana. Mu kwongerako `project_id` y'ikintu gihuye n'inyigisho yawe, urema ihuriro hagati y'ivyo bintu bibiri;



- tags**: amajambo y’ingenzi 2 canke 3 ajanye n’ibirimwo mu nyigisho, yatowe gusa [ku rutonde rw’amajambo ya Plan ₿ Academy]



- category**: Urutonde ruto rujanye n’ibirimwo mu nyigisho, hakurikijwe imiterere y’urubuga rwa Plan ₿ Academy (nk’akarorero, ku bikoresho vya wallet: `ibiro`, `ibikoresho`, `iminwe`, `ivy’inyuma`);



- urugero**: Urugero rw'ingorane z'inyigisho, rwatowe muri:
    - 'umutanguzi`
    - `hagati`
    - `biteye imbere`
    - 'umuhinga'



- professor_id**: `id_y'umwigisha` wawe (UUID) nk'uko vyerekanywe kuri [umwirondoro wawe w'umwigisha](https://github.com/Ikiganiro-PlanB/ibirimwo-ivy'inyigisho/igiti/dev/abaporofeseri);



- ururimi_rw'umwimerere**: Ururimi rw'umwimerere rw'inyigisho (nk'akarorero, `fr`, `en`, n'ibindi);



- gukosora**: Amakuru yerekeye ingene umuntu akora ivyo gukosora. Uzuza igice ca mbere, nk'uko gukosora inyigisho yawe bwite biharurwa nk'ukwemeza kwa mbere:
    - ururimi**: Ururimi rwo gukosora (nk'akarorero, `fr`, `en`, n'ibindi).
    - itariki_yanyuma_y'intererano**: Itariki y'umusi.
    - vyihutirwa**: 1
    - amazina_y'abaterankunga**: Indangamuntu yawe ya GitHub.
    - impembo**: 0


Kubindi bisobanuro ku bijanye n'ikarata yawe y'umwigisha, urashobora kuraba inyigisho ihuye:


https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

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


### 5 - Kwandika ibirimwo



- Uzuza ibiranga dosiye ya Markdown na:
    - Umutwe (`izina`).
    - Insobanuro ngufi (`insobanuro`).
- Yongerako ishusho y'igipfukisho hejuru y'inyigisho ukoresheje insiguro ya Markdown (subiriza "icatsi kibisi" n'izina ry'igikoresho kigaragazwa):


```
![cover-green](assets/cover.webp)
```



- Wandike ibirimwo mu nyigisho muri Markdown:
    - Koresha imitwe itunganijwe neza (`##`), urutonde n'ingingo.
    - Injiza amashusho ukoresheje insiguro ya Markdown:


```
![nom-image](assets/en/001.webp)
```




- Shira ibishushanyo n'amashusho mu rurimi rujanye n'ivyo, muri `/assets`.


### 6 - Bika kandi wohereze inyigisho



- Bika amahinduka yawe mu karere ukoresheje ubutumwa budondora.
- Sunika amahinduka kuri GitHub yawe fork.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- Uhejeje, rema Pull Request (PR) kuri GitHub kugira ngo usabe ugushiramwo ivyo wahinduye.
- Wongereko umutwe n’insobanuro ngufi kuri PR. Vuga inomero y’ikinyamakuru ihuye n’ico mu vyo uvuga.


### 7 - Gukosora no gufatanya



- Rindira kwemezwa canke inyishu iva ku muyobozi.
- Niba ari ngombwa, nukosore kandi usunike amasezerano mashasha.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- Iyo PR imaze guhurizwa hamwe, urashobora gukuraho ishami ryawe rikora.


## Ivyagezwe vyo kurema ibirimwo



- Imiterere ishigikiwe ku rubuga**:
    - Markdown ya kera: urutonde, amahuza, amashusho, amajambo asubiwemwo, amajambo akomeye, amajambo ateye igomwe, n'ibindi.
    - LaTeX (ibara gusa, atari mu murongo): igabanywa na `$$`.
    - Kode y’umurongo: Inyuguti zifise akamenyetso kamwe k’inyuma.
    - Amabara y'amakode: Inyuguti zifise ibimenyetso bitatu vy'inyuma, nk'akarorero:


```
print("Hello, Bitcoin!")
```



- Ivyerekanwa n'ibishushanyo**:
    - Amashusho yose ategerezwa kuba ari mu buryo bwa WebP. Koresha iki gikoresho c’ubuntu kugira ngo ubihindure iyo bisabwe: [Igihinduzi c’Amashusho](https://github.com/LoicPandul/Igihinduzi c’Amashusho).
    - Izina ry'ibishushanyo rifise imibare 2 canke 3 (nk'akarorero `001.urubuga`, `002.urubuga`).
    - Ku nyigisho za wallet zikoreshwa kuri telefone ngendanwa canke ku bikoresho, koresha ibigereranyo.
    - Koresha gusa amashusho wiremye canke ataco utanga.
    - Raba neza ko zifise akamaro kandi zifise akamaro kanini.
- Igitabo c'ibishushanyo**:
    - Imyandikire: [IBM Plex Sans] (IBM+Plex+Sans).
    - Amabara Plan ₿ Academy:
        - Umutuku: `#FF5C00`
        - Ikirabura: `#000000`
        - Umweru: `#FFFFFF`


Niba ufise ingorane z’ubuhinga zo gutanga inyigisho yawe, ndagusavye ntukekeranye gusaba imfashanyo kuri [umugwi wacu wihariye wa Telegram ku bijanye n’intererano](https://t.me/PlanBNetwork_ContentBuilder). Murakoze cane!