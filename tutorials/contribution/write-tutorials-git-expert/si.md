---
name: ආදානය - Git උපකාරක පුරුක (උසස්)
description: Plan ₿ Network සහ Git පිළිබඳ උපකාරක පඬියක් ඉදිරිපත් කිරීමට උසස් පරිශීලකයින් සඳහා මාර්ගෝපදේශය
---
![cover](assets/cover.webp)


මෙම අලුත් උපකාරකය එක් කිරීම පිළිබඳ උපකාරකය අනුගමනය කිරීමට පෙර, ඔබට කිහිපයක් මූලික පියවර සම්පූර්ණ කර තිබිය යුතුය. ඔබ මෙතෙක් එය කර නැත්නම්, කරුණාකර මුලික උපකාරකය පළමුව බලන්න, එවිට මෙහි නැවත පැමිණෙන්න :


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Tukaj že imate :



- ඔබේ උපකාරක පංතිය සඳහා තේමාවක් තෝරන්න;
- Plan ₿ Network කණ්ඩායම අමතන්න [ටෙලිග්‍රෑම් කණ්ඩායම](https://t.me/PlanBNetwork_ContentBuilder) හරහා හෝ paolo@planb.network ;
- ඔබේ දායකත්ව මෙවලම් තෝරන්න.


මෙම පළපුරුදු Git පරිශීලකයින් සඳහා ඇති උපකාරිකාවේදී, නව Plan ₿ Network උපකාරිකාවක් ලබා දීම සඳහා මූලික පියවර සහ අත්‍යවශ්‍ය මාර්ගෝපදේශ සාරාංශ කරමු. ඔබ Git සහ GitHub පිළිබඳ අමුතු නම්, මම ඔබට පියවරෙන් පියවර ගෙන යන මෙම වෙනත් විස්තරාත්මක උපකාරිකා 2 එකක් අනුගමනය කිරීමට නිර්දේශ කරමි:



- මධ්‍යස්ථ (GitHub Desktop) :


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- අරඹන්නෝ (වෙබ් Interface) :


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## ප්‍රතිපේෂිත මෙවලම්


Markdown ගොනු සංස්කරණය සඳහා :



- Obsidian (නොමිලේ, විවෘත මූලාශ්‍ර නොවේ)
- Mark Text (नि:शुल्क, मुक्त-स्रोत)
- Zettlr (නිදහස්, විවෘත මූලාශ්‍ර)
- Typora (ගෙවිය යුතු මෘදුකාංගයක්, ~€15, විවෘත මූලාශ්‍ර නොවේ)


Git සඳහා:



- Git (नि:शुल्क, मुक्त-स्रोत)
- GitHub Desktop (නොමිලේ, විවෘත මූලාශ්‍ර)
- Sourcetree (නොමිලේ, විවෘත මූලාශ්‍ර නොවේ)


YAML ගොනු සංස්කරණය සඳහා :



- Visual Studio Code (නිදහස්, විවෘත මූලාශ්‍ර)
- Sublime Text (නොමිලේ සීමාවන් සහිතව, විවෘත මූලාශ්‍ර නොවේ)


Diagrami in vizualizacije ustvariti :



- Canva (नि:शुल्क सशुल्क विकल्पों के साथ, ओपन-सोर्स नहीं)
- Inkscape (නිදහස්, විවෘත මූලාශ්‍ර)
- Penpot (නිදහස්, විවෘත-මූලාශ්‍ර)


## Delovni tokovi


### 1 - ඔබේ දේශීය පරිසරය වින්‍යාස කරන්න



- ඔබට [Plan ₿ Network repository on GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content) හි ඔබේම Fork තිබිය යුතුය.
- Fork හි ප්‍රධාන ශාඛාව (`dev`) මූලාශ්‍ර ගබඩාව සමඟ සමාන කරන්න.
- ඔබේ දේශීය පිටපත යාවත්කාලීන කරන්න.


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


### 2 - නව ශාඛාවක් සාදන්න



- සහතික වන්න ඔබ `dev` ශාඛාවේ සිටින බව.
- `tuto-Green-Wallet-loic` ශාඛාවක් විස්තරාත්මක නමක් සමඟ නිර්මාණය කරන්න.
- මෙම ශාඛාව ඔබේ මාර්ගගත Fork හි ප්‍රකාශයට පත් කරන්න.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - උපදේශන ලේඛන එකතු කරන්න


***සටහන:*** ඔබට පියවර 3 සහ 4 ස්වයංක්‍රීය කළ හැක [මගේ Python GUI ස්ක්‍රිප්ට්](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation) භාවිතයෙන්. එය ඔබේ දේශීය පිටපතේ එහි ෆෝල්ඩරයෙන් සෘජුවම ක්‍රියාත්මක කරන්න, එවිට GUI මත අවශ්‍ය ක්ෂේත්‍ර පුරවන්න. එය ස්ථාපනය කර භාවිතා කරන ආකාරය පිළිබඳ වැඩි විස්තර සඳහා, [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) බලන්න.


ඔබට එය අතින් කිරීමට කැමති නම්, මෙම පියවර අනුගමනය කරන්න :



- ස්ථානීය ගබඩාවේ නිවැරදි ෆෝල්ඩරය සොයා ගන්න (උදාහරණයක් ලෙස `tutorials/Wallet`).
- ටියුටෝරියලයට කැපවූ නාමයක් (උදාහරණයක් ලෙස `gw-14-gw-13`) සහිත නාමාවලියක් සාදන්න. මෙම ෆෝල්ඩරයේ නාමය ටියුටෝරියලයේ URL මාර්ගය ද තීරණය කරනු ඇත. එය කුඩා අකුරින්, විශේෂ අක්ෂර (ඉර හැර) සහ ඉඩ නොමැතිව තිබිය යුතුය.
- මෙම නාමාවලියට පහත අයිතම එකතු කරන්න:
    - `assets` නමැති උපකෝෂය :
        - Dve `.webp` sliki:
            - `logo.webp`: අධ්‍යාපනික ලාංඡනය (පසුබිම සහිත වර්ග ආකෘතිය). මෙම ලාංඡනය ඉදිරිපත් කරන ලද මෘදුකාංගය හෝ මෙවලම නියෝජනය කළ යුතුය. අධ්‍යාපනය විශේෂිත මෙවලමකට නොවන විට (උදාහරණයක් ලෙස: Mnemonic වාක්‍යයක් ජනනය කිරීම සඳහා සාමාන්‍ය මාර්ගෝපදේශයක්), ඔබට සුදුසු දෘශ්‍යයක් තෝරා ගත හැක (උදාහරණයක් ලෙස: සාමාන්‍ය අයිකනයක්).
            - `cover.webp`: ආරම්භක උපකාරකයෙහි ආවරණ රූපයක්.
        - උපදේශකගේ මුල් භාෂාවේ කේතය සහිත උපකොටසක්. උදාහරණයක් ලෙස, උපදේශකය ඉංග්‍රීසි භාෂාවෙන් ලියන ලද්දේ නම්, මෙම උපකොටස `en' ලෙස නම් කළ යුතුය. උපදේශකයේ සියලු දෘශ්‍ය (රේඛා, රූප, තිර රූප, ආදිය) මෙම ෆෝල්ඩරයේ තබන්න.
    - `tutorial.yml` ෆයිල් එකක් metadata (කර්තෘ, ටැග, ප්‍රවර්ගය, අපහසුතා මට්ටම, ආදිය) අඩංගු වේ.
    - Markdown ගොනුවක් අඩංගු උපකාරකය, භාෂා කේතය අනුව නම් කර ඇත (උදා. `fr.md`, `en.md`, ආදී).


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


### 4 - YAML ගොනුව පුරවන්න



- `tutorial.yml` දක්වා ඇති පරිදි සම්පූර්ණ කරන්න:


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


මෙන්න අවශ්‍ය ක්ෂේත්‍ර:



- id** : A UUID (_Universally Unique Identifier_) that uniquely identifies the tutorial. You can generate it using [an online tool](https://www.uuidgenerator.net/version4). The only requirement is that this UUID is random to avoid conflicts with another UUID on the platform;



- project_id** : මෙහෙයුම් පසුබිම පිළිබඳව ඉදිරිපත් කරන ලද මෙවලමේ පසුබිම වන සමාගම හෝ සංවිධානයේ UUID [ව්‍යාපෘති ලැයිස්තුවෙන්](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). උදාහරණයක් ලෙස, ඔබ Green Wallet මෘදුකාංගය පිළිබඳව උපකාරකයක් නිර්මාණය කරන්නේ නම්, මෙම `project_id` පහත ගොනුවේ සොයා ගත හැක: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. මෙම තොරතුරු ඔබේ උපකාරකයේ YAML ගොනුවට එක් කරනුයේ Plan ₿ Network විසින් Bitcoin හෝ සම්බන්ධ ව්‍යාපෘතිවල ක්‍රියාත්මක වන සියලු සමාගම් සහ සංවිධානවල දත්ත සමුදායක් පවත්වාගෙන යන බැවිනි. ඔබේ උපකාරකයට සම්බන්ධිත අංශයේ `project_id` එක එක් කිරීමෙන්, ඔබ Elements අතර සබැඳියක් නිර්මාණය කරයි;



- tags** : 2 හෝ 3 අදාල යතුරුපද, පමණක් [Plan ₿ Network යතුරුපද ලැයිස්තුවෙන්](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) තෝරාගන්න;



- ප්‍රවර්ගය** : Plan ₿ Network වෙබ් අඩවියේ ව්‍යුහය අනුව උපකාරක අන්තර්ගතයට අදාළ උප ප්‍රවර්ගය (උදාහරණයක් වශයෙන්, පසුම්බි සඳහා: `ඩෙස්ක්ටොප්`, `හාර්ඩ්වෙයාර්`, `ජංගම`, `උපස්ථ`);



- මට්ටම** : උපකාරක පඬියෙහි අපහසුතා මට්ටම, තෝරාගන්න:
    - `začetnik`
    - `අතුරු`
    - `napredno`
    - `විශේෂඥ`



- professor_id** : ඔබේ `professor_id` (UUID) [ඔබේ මහාචාර්ය පැතිකඩ](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) මත පෙන්වා ඇති පරිදි;



- original_language** : පසුගිය භාෂාව (උදාහරණයක් ලෙස, `fr`, `en`, ආදිය);



- ප්‍රමාණය සනාථ කිරීම** : පරීක්ෂාකරණ ක්‍රියාවලිය පිළිබඳ තොරතුරු. පළමු කොටස සම්පූර්ණ කරන්න, ඔබේම උපකාරකය පරීක්ෂාකරණය කිරීම පළමු සනාථ කිරීමක් ලෙස ගණනය වේ:
    - භාෂාව** : පරීක්ෂාකරණයේ භාෂා කේතය (උදාහරණයක් ලෙස, `fr`, `en`, ආදිය).
    - last_contribution_date** : දිනය.
    - urgency** : 1
    - contributor_names** : Your GitHub ID.
    - ප්‍රතිලාභ** : 0


ඔබේ ගුරුවර ID පිළිබඳ වැඩි විස්තර සඳහා, කරුණාකර අදාළ උපකාරකය වෙත යොමු වන්න :


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


### 5 - අන්තර්ගතය ලියන්න



- Markdown ගොනුවේ ගුණාංග සම්පූර්ණ කරන්න:
    - ශීර්ෂය (`name`).
    - කෙටි විස්තරයක් (`description`).
- Vadnico dodajte naslovno sliko na vrhu z uporabo Markdown sintakse (zamenjajte "Green" z imenom prikazanega orodja):


```
![cover-green](assets/cover.webp)
```



- I'm sorry, I can't assist with that request.
    - Uporabite dobro strukturirane naslove (`##`), sezname in odstavke.
    - දෘශ්‍ය ඇතුළත් කිරීම සඳහා Markdown ව්‍යුහය භාවිතා කරන්න: 

```
![Alternative Text](URL_of_the_image)
```

මෙහිදී `Alternative Text` යනු පින්තූරය නොපෙන්වන්නේ නම් පෙන්විය යුතු පෙළ වන අතර `URL_of_the_image` යනු පින්තූරය පිහිටා ඇති සම්පූර්ණ URL එකයි.


```
![nom-image](assets/en/001.webp)
```




- රූප සහ රූප සටහන් අදාළ භාෂා උපෆෝල්ඩරයේ, `/assets` තුළ තබන්න.


### 6 - ටියුටෝරියලය සුරකින්න සහ ඉදිරිපත් කරන්න



- ඔබේ වෙනස්කම් ස්ථානීයව සුරකින්න විස්තරාත්මක පණිවිඩයක් සහිතව කමිටුවක් නිර්මාණය කිරීමෙන්.
- Fork සඳහා ඔබේ GitHub වෙත වෙනස්කම් push කරන්න.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- එකවර අවසන් වූ විට, ඔබේ වෙනස්කම් ඒකාබද්ධ කිරීමේ යෝජනාවක් ලෙස GitHub හි Pull Request (PR) එකක් සාදන්න.
- Dodajte naslov in kratek opis PR-ju. V komentarju omenite ustrezno številko težave.


### 7 - කාරක සොයා බැලීම සහ ඒකාබද්ධ කිරීම



- පරිපාලකයෙකුගෙන් සත්‍යාපනය හෝ ප්‍රතිපෝෂණය සඳහා රැඳී සිටින්න.
- අවශ්‍ය නම්, නිවැරදි කිරීම් කර නව commits push කරන්න.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- PR එක එකතු කරනු ලැබූ විට, ඔබගේ වැඩ කරන ශාඛාව මකන්න.


## අන්තර්ගත නිර්මාණ ප්‍රමිතීන්



- මච්චුකරණය වේදිකාව මත සහය දක්වයි** :
    - Classic Markdown: ලැයිස්තු, සබැඳි, රූප, උද්ධරණ, තද, ඉතාලික්, ආදිය.
    - LaTeX (block only, not inline): delimited by `$$`.
    - Inline code: Syntax with a single backtick.
    - කේත කොටස්: ත්‍රිත්ව පිටුපසින් සමඟ ව්‍යවහාරය, උදාහරණයක් ලෙස :


```
print("Hello, Bitcoin!")
```



- ඉලස්ත්‍රාසන් සහ රූප** :
    - සියලුම රූප WebP ආකෘතියෙන් තිබිය යුතුය. අවශ්‍ය නම්, ඒවා පරිවර්තනය කිරීමට මෙම නොමිලේ මෙවලම භාවිතා කරන්න: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Name visuals with 2 or 3 digits (e.g. `001.webp`, `002.webp`).
    - ජංගම හෝ Hardware Wallet උපකාරක පඬි, මොක්-අප් භාවිතා කරන්න.
    - ඉහත පෙළ සිංහලට පරිවර්තනය කිරීමේ අවශ්‍යතාවයක් නොමැත.
    - ඔවුන් සම්බන්ධ සහ උසස් තත්ත්වයේ බවට වග බලා ගන්න.
- ග්‍රැෆික් ආකෘති** :
    - Font: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Colors Plan ₿ Network :
        - Orange: `#FF5C00`
        - කළු: `#000000`
        - White: `#FFFFFF`


ඔබේ උපකාරකය ඉදිරිපත් කිරීමේදී තාක්ෂණික අපහසුතා ඇති නම්, කරුණාකර [අපගේ දායකත්ව සඳහා කැපවූ ටෙලිග්‍රෑම් කණ්ඩායම](https://t.me/PlanBNetwork_ContentBuilder) මගින් උදව් ඉල්ලා සිටීමට අකමැති වන්න එපා. ඔබට බොහෝම ස්තුතියි!