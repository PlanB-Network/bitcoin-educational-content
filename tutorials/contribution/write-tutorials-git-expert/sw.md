---
name: Mchango - Mafunzo ya Git (ya hali ya juu)
description: Mwongozo kwa watumiaji wa hali ya juu wa kutoa mafunzo kuhusu Plan ₿ Academy ukitumia Git
---
![cover](assets/cover.webp)


Kabla ya kufuata mafunzo haya kuhusu kuongeza mafunzo mapya, unahitaji kuwa umekamilisha hatua chache za awali. Ikiwa bado hujafanya hivyo, tafadhali angalia mafunzo haya ya utangulizi kwanza, kisha urudi hapa:


https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Tayari una:



- Chagua mada kwa ajili ya mafunzo yako;
- Niliwasiliana na timu ya Plan ₿ Academy kupitia [kundi la Telegram](https://t.me/PlanBNetwork_ContentBuilder) au paolo@planb.network;
- Chagua zana zako za michango.


Katika mafunzo haya kwa watumiaji wenye uzoefu wa Git, tutafupisha kwa ufupi hatua muhimu na miongozo muhimu ya kutoa mafunzo mapya ya Plan ₿ Academy. Ikiwa hujui Git na GitHub, ninapendekeza ufuate mojawapo ya mafunzo mengine 2 ya kina ambayo yatakupeleka hatua kwa hatua:



- Kiwango cha kati (GitHub Desktop):


https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- Wanaoanza (kiolesura cha wavuti):


https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Zana zilizopendekezwa


Kwa kuhariri faili za Markdown:



- Obsidian (Bila malipo, si chanzo huria)
- Weka alama kwenye Maandishi (Bila Malipo, chanzo huria)
- Zettlr (Bila malipo, chanzo huria)
- Typora (Payware, ~€15, sio chanzo huria)


Kwa Git:



- Git (Bila malipo, chanzo huria)
- GitHub Desktop (Bila malipo, chanzo huria)
- Sourcetree (Bila malipo, si chanzo huria)


Kwa kuhariri faili za YAML:



- Msimbo wa Studio ya Kuonekana (Bila Malipo, chanzo huria)
- Maandishi Mafupi (Bila malipo yenye mapungufu, si chanzo huria)


Ili kuunda michoro na taswira:



- Canva (Bila malipo na chaguo za kulipia, si programu huria)
- Inkscape (Bila malipo, chanzo huria)
- Penpot (Bila malipo, chanzo huria)


## Mtiririko wa kazi


### 1 - Sanidi mazingira yako ya karibu



- Lazima uwe na fork yako mwenyewe ya [hifadhi ya Plan ₿ Academy kwenye GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Sawazisha tawi kuu (`dev`) la fork yako na hazina chanzo.
- Sasisha nakala yako ya ndani.


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
- Unda tawi jipya lenye jina linaloelezea (k.m. `tuto-green-wallet-loic`).
- Chapisha tawi hili kwenye fork yako mtandaoni.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - Ongeza hati za mafunzo


***Kumbuka:*** Unaweza kuendesha hatua za 3 na 4 kiotomatiki kwa kutumia [Python GUI yangu script](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Iendeshe moja kwa moja kutoka kwenye folda yake katika nakala yako ya ndani, kisha ujaze sehemu zinazohitajika kwenye GUI. Kwa maelezo zaidi kuhusu jinsi ya kusakinisha na kuitumia, angalia [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


Ukitaka kuifanya kwa mikono, fuata hatua hizi:



- Tafuta folda inayofaa katika hazina ya ndani (k.m. `mafunzo/wallet`).
- Unda saraka iliyotengwa kwa ajili ya mafunzo yenye jina wazi (k.m. `kijani-wallet`). Jina la folda hii pia litaamua njia ya URL ya mafunzo. Inapaswa kuwa katika herufi ndogo, bila herufi maalum (isipokuwa vistari) na bila nafasi.
- Ongeza vipengee vifuatavyo kwenye saraka hii:
    - Folda ndogo inayoitwa `assets` yenye:
        - Picha mbili za `.webp`:
            - `logo.webp`: Nembo ya mafunzo (muundo wa mraba wenye usuli). Nembo hii lazima iwakilishe programu au zana iliyowasilishwa. Ikiwa mafunzo hayahusu zana maalum (k.m.: mwongozo wa jumla wa kutengeneza kifungu cha kumbukumbu), unaweza kuchagua taswira inayofaa (k.m.: aikoni ya jumla).
            - `cover.webp`: Picha ya jalada inayoonyeshwa mwanzoni mwa mafunzo.
        - Folda ndogo yenye msimbo wa lugha asilia ya mafunzo. Kwa mfano, ikiwa mafunzo yameandikwa kwa Kiingereza, folda hii ndogo inapaswa kuitwa `en'. Weka taswira zote za mafunzo (michoro, picha, picha za skrini, n.k.) kwenye folda hii.
    - Faili ya `tutorial.yml` iliyo na metadata (mwandishi, lebo, kategoria, kiwango cha ugumu, n.k.).
    - Faili ya Markdown iliyo na mafunzo, yenye jina kulingana na msimbo wa lugha (k.m. `fr.md`, `en.md`, nk.).


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



- id**: UUID (_Kitambulisho cha Unique cha Ulimwenguni_) kinachotambua mafunzo kwa njia ya kipekee. Unaweza kuitengeneza kwa kutumia [zana ya mtandaoni](https://www.uuidgenerator.net/version4). Sharti pekee ni kwamba UUID hii iwe nasibu ili kuepuka migogoro na UUID nyingine kwenye mfumo;



- project_id**: UUID ya kampuni au shirika nyuma ya chombo kilichowasilishwa katika mafunzo [kutoka kwenye orodha ya mradi](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Kwa mfano, ikiwa unaunda mafunzo kuhusu programu ya Green Wallet, unaweza kupata `project_id` hii katika faili ifuatayo: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Taarifa hii imeongezwa kwenye faili ya YAML ya mafunzo yako kwa sababu Plan ₿ Academy inahifadhi hifadhidata ya makampuni na mashirika yote yanayofanya kazi kwenye Bitcoin au miradi inayohusiana. Kwa kuongeza `project_id` ya huluki iliyounganishwa na mafunzo yako, unaunda kiungo kati ya vipengele hivyo viwili;



- lebo**: Maneno muhimu 2 au 3 yanayohusiana na maudhui ya mafunzo, yaliyochaguliwa pekee [kutoka kwenye orodha ya lebo ya Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- kategoria**: Kategoria ndogo inayolingana na maudhui ya mafunzo, kulingana na muundo wa tovuti ya Plan ₿ Academy (kwa mfano, kwa wallets: `desktop`, `hardware`, `mobile`, `backup`);



- kiwango**: Kiwango cha ugumu wa mafunzo, kilichochaguliwa kutoka:
    - 'mwanzilishi'
    - `wa kati`
    - 'ya hali ya juu'
    - 'mtaalamu'



- profesa_id**: `Profesa_id` wako (UUID) kama inavyoonyeshwa kwenye [wasifu wako wa profesa](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);



- lugha_asili**: Lugha asili ya mafunzo (k.m., `fr`, `en`, n.k.);



- usomaji sahihi**: Taarifa kuhusu mchakato wa usomaji sahihi. Kamilisha sehemu ya kwanza, kwani usomaji sahihi wa mafunzo yako mwenyewe unahesabiwa kama uthibitisho wa kwanza:
    - lugha**: Msimbo wa lugha wa usomaji sahihi (k.m., `fr`, `en`, nk.).
    - tarehe_ya_mchango_wa_mwisho**: Tarehe ya siku.
    - dharura**: 1
    - majina_ya_mchangiaji**: Kitambulisho chako cha GitHub.
    - zawadi**: 0


Kwa maelezo zaidi kuhusu kitambulisho chako cha mwalimu, tafadhali rejelea mafunzo yanayolingana:


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


### 5 - Andika maudhui



- Kamilisha sifa za faili ya Markdown kwa kutumia:
    - Cheo (`jina`).
    - Maelezo mafupi (`maelezo`).
- Ongeza picha ya jalada juu ya mafunzo kwa kutumia sintaksia ya Markdown (badilisha "kijani" na jina la kifaa kilichoonyeshwa):


```
![cover-green](assets/cover.webp)
```



- Andika maudhui ya mafunzo katika Markdown:
    - Tumia vichwa vya habari vilivyopangwa vizuri (`##`), orodha na aya.
    - Ingiza taswira kwa kutumia sintaksia ya Markdown:


```
![nom-image](assets/en/001.webp)
```




- Weka michoro na picha katika folda ndogo ya lugha inayolingana, katika `/assets`.


### 6 - Hifadhi na uwasilishe mafunzo



- Hifadhi mabadiliko yako ndani ya eneo lako kwa kuunda ahadi yenye ujumbe unaoelezea.
- Sukuma mabadiliko kwenye GitHub yako fork.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- Ukishamaliza, tengeneza Ombi la Kuvuta (PR) kwenye GitHub ili kupendekeza ujumuishaji wa marekebisho yako.
- Ongeza kichwa na maelezo mafupi kwenye PR. Taja nambari inayolingana ya suala kwenye maoni.


### 7 - Kusahihisha na kuunganisha



- Subiri uthibitisho au maoni kutoka kwa msimamizi.
- Ikiwa ni lazima, fanya marekebisho na uboreshe ahadi mpya.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- Mara tu PR ikiwa imeunganishwa, unaweza kufuta tawi lako linalofanya kazi.


## Viwango vya uundaji wa maudhui



- Uumbizaji unaungwa mkono kwenye mfumo**:
    - Alama ya Kawaida: orodha, viungo, picha, nukuu, herufi nzito, italiki, n.k.
    - LaTeX (kizuizi pekee, si ndani ya mstari): imepunguzwa na `$$`.
    - Msimbo wa ndani: Sintaksia yenye tiki moja ya mgongo.
    - Vizuizi vya msimbo: Sintaksia yenye vibandiko vitatu vya mgongo, kwa mfano:


```
print("Hello, Bitcoin!")
```



- Vielelezo na michoro**:
    - Picha zote lazima ziwe katika umbizo la WebP. Tumia zana hii ya bure kuzibadilisha inapohitajika: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Taja taswira zenye tarakimu 2 au 3 (k.m. `001.webp`, `002.webp`).
    - Kwa mafunzo ya simu au vifaa vya wallet, tumia mock-ups.
    - Tumia taswira zilizotengenezwa na wewe mwenyewe au zisizo na mrahaba pekee.
    - Hakikisha zinafaa na zina ubora wa hali ya juu.
- Hati ya michoro**:
    - Fonti: [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - Rangi Plan ₿ Academy:
        - Chungwa: `#FF5C00`
        - Nyeusi: `#000000`
        - Nyeupe: `#FFFFFF`


Ikiwa unapata shida ya kiufundi katika kuwasilisha mafunzo yako, tafadhali usisite kuomba usaidizi kuhusu [kikundi chetu maalum cha Telegram kwa michango](https://t.me/PlanBNetwork_ContentBuilder). Asante sana!