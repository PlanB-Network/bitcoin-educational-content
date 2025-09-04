---
name: Mchango - Mafunzo ya Git (ya juu)
description: Mwongozo kwa watumiaji wa hali ya juu ili kutoa mafunzo kwenye Plan ₿ Network na Git
---
![cover](assets/cover.webp)


Kabla ya kufuata mafunzo haya juu ya kuongeza mafunzo mapya, unahitaji kuwa umekamilisha hatua chache za awali. Ikiwa bado hujafanya hivyo, tafadhali angalia mafunzo haya ya utangulizi kwanza, kisha urudi hapa:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Tayari unayo:



- Chagua mada ya mafunzo yako;
- Iliwasiliana na timu ya Plan ₿ Network kupitia [Telegram group](https://t.me/PlanBNetwork_ContentBuilder) au paolo@planb.network ;
- Chagua zana zako za mchango.


Katika mafunzo haya kwa watumiaji wenye uzoefu wa Git, tutafanya muhtasari wa hatua muhimu na miongozo muhimu ya kutoa mafunzo mapya ya Plan ₿ Network. Ikiwa hujui Git na GitHub, ninapendekeza ufuate mojawapo ya mafunzo haya mengine 2 ya kina ambayo yatakuchukua hatua kwa hatua:



- Kati (Desktop ya GitHub):


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- Wanaoanza (mtandao Interface):


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Zana zilizopendekezwa


Kwa kuhariri faili za Markdown:



- Obsidian (Bure, sio chanzo wazi)
- Weka alama kwenye maandishi (Bure, chanzo-wazi)
- Zettlr (Bure, chanzo-wazi)
- Typora (Payware, ~€15, si chanzo huria)


kwa Git:



- Git (Bure, chanzo-wazi)
- GitHub Desktop (Bure, chanzo-wazi)
- Sourcetree (Bure, sio chanzo wazi)


Kwa kuhariri faili za YAML:



- Msimbo wa Studio unaoonekana (Bure, chanzo-wazi)
- Maandishi Madogo (Bila na vikwazo, sio chanzo-wazi)


Ili kuunda michoro na taswira:



- Canva (Bila malipo na chaguzi zilizolipwa, sio chanzo wazi)
- Inkscape (Bure, chanzo-wazi)
- Penpot (Bure, chanzo wazi)


## Mitiririko ya kazi


### 1 - Sanidi mazingira ya eneo lako



- Ni lazima uwe na Fork yako mwenyewe ya [Plan ₿ Network hazina kwenye GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content).
- Sawazisha tawi kuu (`dev`) la Fork yako na hazina ya chanzo.
- Sasisha mshirika wako wa karibu.


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


### 2 - Unda tawi jipya



- Hakikisha uko kwenye tawi la `dev`.
- Unda tawi jipya kwa jina la maelezo (k.m. `tuto-Green-Wallet-loic`).
- Chapisha tawi hili kwenye mtandao wako wa Fork.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - Ongeza hati za mafunzo


***Kumbuka:*** Unaweza kubadilisha hatua ya 3 na 4 otomatiki kwa kutumia [hati yangu ya Python GUI](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Iendeshe moja kwa moja kutoka kwa folda yake kwenye mwambaa wako wa karibu, kisha ujaze sehemu zinazohitajika kwenye GUI. Kwa maelezo zaidi kuhusu jinsi ya kuisakinisha na kuitumia, angalia [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


Ikiwa ungependa kuifanya kwa mikono, fuata hatua hizi:



- Tafuta folda inayofaa katika hazina ya ndani (k.m. `mafunzo/Wallet`).
- Unda saraka inayotolewa kwa mafunzo yenye jina wazi (k.m. `Green-Wallet`). Jina la folda hii pia litabainisha njia ya URL ya mafunzo. Inapaswa kuwa katika herufi ndogo, isiyo na herufi maalum (isipokuwa viambatisho) na hakuna nafasi.
- Ongeza vitu vifuatavyo kwenye saraka hii:
    - Folda ndogo inayoitwa `assets` iliyo na:
        - Picha mbili za `.webp`:
            - `logo.webp`: Nembo ya mafunzo (umbizo la mraba lenye usuli). Nembo hii lazima iwakilishe programu au zana iliyowasilishwa. Ikiwa mafunzo si mahususi kwa zana (k.m.: mwongozo wa jumla wa kutengeneza maneno ya Mnemonic), unaweza kuchagua taswira inayofaa (k.m.: ikoni ya jumla).
            - `cover.webp`: Picha ya jalada lililoonyeshwa mwanzoni mwa mafunzo.
        - Folda ndogo iliyo na msimbo wa lugha asili ya mafunzo. Kwa mfano, ikiwa somo limeandikwa kwa Kiingereza, folda hii inapaswa kupewa jina `en'. Weka taswira zote za mafunzo (michoro, picha, picha za skrini, n.k.) kwenye folda hii.
    - Faili ya `tutorial.yml` iliyo na metadata (mwandishi, lebo, kitengo, kiwango cha ugumu, n.k.).
    - Faili ya Markdown iliyo na mafunzo, iliyopewa jina kulingana na msimbo wa lugha (k.m. `fr.md`, `en.md`, n.k.).


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


### 4 - Jaza faili ya YAML



- Kamilisha faili ya `tutorial.yml` kama ifuatavyo:


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


Hapa kuna sehemu zinazohitajika:



- **id**: UUID (_Kitambulisho cha Kipekee cha Universally_) ambacho hutambulisha mafunzo kwa njia ya kipekee. Unaweza generate kwa kutumia [zana ya mtandaoni](https://www.uuidgenerator.net/version4). Sharti pekee ni kwamba UUID hii ni ya nasibu ili kuepusha migongano na UUID nyingine kwenye jukwaa;



- **project_id**: UUID ya kampuni au shirika nyuma ya zana iliyowasilishwa kwenye mafunzo [kutoka kwenye orodha ya mradi](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Kwa mfano, ikiwa unaunda mafunzo kuhusu programu ya Green Wallet, unaweza kupata `project_id` hii katika faili ifuatayo: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Maelezo haya yanaongezwa kwenye faili ya mafunzo yako ya YAML kwa sababu Plan ₿ Network ina hifadhidata ya makampuni na mashirika yote yanayofanya kazi kwenye Bitcoin au miradi inayohusiana. Kwa kuongeza `project_id` ya huluki iliyounganishwa kwenye mafunzo yako, unaunda kiungo kati ya Elements mbili;



- **tags**: Maneno muhimu 2 au 3 yanayohusiana na maudhui ya mafunzo, yaliyochaguliwa pekee [kutoka kwa orodha ya lebo za Plan ₿ Network](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- **kategoria**: Kitengo kidogo kinacholingana na maudhui ya mafunzo, kulingana na muundo wa tovuti ya Plan ₿ Network (kwa mfano, kwa pochi: `desktop`, `hardware`, `mobile`, `chelezo`);



- **kiwango**: Kiwango cha ugumu cha mafunzo, kilichochaguliwa kutoka:
    - `Mwanzo`
    - `katikati`
    - `advanced`
    - `mtaalam`



- **professor_id**: `professor_id` (UUID) yako kama inavyoonyeshwa kwenye [wasifu wako wa profesa](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- **lugha_asilia**: Lugha asilia ya mafunzo (k.m., `fr`, `en`, n.k.);



- **kusahihisha**: Taarifa kuhusu mchakato wa kusahihisha. Kamilisha sehemu ya kwanza, kwani kusahihisha mafunzo yako mwenyewe kunahesabiwa kama uthibitisho wa kwanza:
    - **lugha**: Msimbo wa lugha wa kusahihisha (k.m., `fr`, `en`, n.k.).
    - **tarehe_ya_mwisho_mchango**: Tarehe ya siku.
    - **dharura**: 1
    - **contributor_names**: Kitambulisho chako cha GitHub.
    - **malipo**: 0


Kwa maelezo zaidi kuhusu kitambulisho chako cha mwalimu, tafadhali rejelea mafunzo yanayolingana:


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


### 5 - Andika yaliyomo



- Kamilisha mali ya faili ya Markdown na:
    - Kichwa (`jina`).
    - Maelezo mafupi (`maelezo`).
- Ongeza picha ya jalada juu ya mafunzo kwa kutumia syntax ya Markdown (badilisha "Green" na jina la zana iliyoonyeshwa):


```
![cover-green](assets/cover.webp)
```



- Andika maudhui ya mafunzo katika Markdown:
    - Tumia vichwa vilivyoundwa vyema (`##`), orodha na aya.
    - Ingiza taswira kwa kutumia syntax ya Markdown:


```
![nom-image](assets/en/001.webp)
```




- Weka michoro na picha katika folda ndogo ya lugha inayolingana, katika `/assets`.


### 6 - Hifadhi na uwasilishe mafunzo



- Hifadhi mabadiliko yako ndani ya nchi kwa kuunda ahadi na ujumbe wa maelezo.
- Sukuma mabadiliko kwenye GitHub Fork yako.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- Mara baada ya kumaliza, unda Ombi la Kuvuta (PR) kwenye GitHub ili kupendekeza ujumuishaji wa marekebisho yako.
- Ongeza kichwa na maelezo mafupi kwa PR. Taja nambari inayolingana ya suala kwenye maoni.


### 7 - Kusahihisha na kuunganisha



- Subiri uthibitisho au maoni kutoka kwa msimamizi.
- Ikibidi, fanya masahihisho na sukuma ahadi mpya.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- Mara tu PR imeunganishwa, unaweza kufuta tawi lako linalofanya kazi.


## Viwango vya kuunda maudhui



- **Uumbizaji unatumika kwenye jukwaa**:
    - Classic Markdown: orodha, viungo, picha, quotes, ujasiri, italiki, nk.
    - LaTeX (zuia pekee, sio ndani): imetengwa na `$$`.
    - Msimbo wa ndani: Sintaksia yenye tiki moja.
    - Vizuizi vya msimbo: Sintaksia yenye vijiti vitatu, kwa mfano:


```
print("Hello, Bitcoin!")
```



- **Vielelezo na michoro**:
    - Picha zote lazima ziwe katika umbizo la WebP. Tumia zana hii isiyolipishwa ili kuzibadilisha ikihitajika: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Taja taswira zenye tarakimu 2 au 3 (k.m. `001.webp`, `002.webp`).
    - Kwa mafunzo ya simu au Hardware Wallet, tumia dhihaka.
    - Tumia taswira zilizoundwa mwenyewe au zisizo na mrabaha pekee.
    - Hakikisha yanafaa na ya ubora wa juu.
- **Hati ya picha**:
    - Fonti: [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - Rangi Plan ₿ Network:
        - Chungwa: `#FF5C00`
        - Nyeusi: `#000000`
        - Nyeupe: `#FFFFFF`


Iwapo una matatizo ya kiufundi kuwasilisha mafunzo yako, tafadhali usisite kuomba usaidizi kwenye [kikundi chetu maalum cha Telegram kwa michango](https://t.me/PlanBNetwork_ContentBuilder). Asante sana!
