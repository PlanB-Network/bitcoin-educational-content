---
name: Prispevek - Vadnica z GitHub Desktop (Srednje)
description: Plan ₿ Network මත උපකාරක පුරුකක් යෝජනා කිරීමට සම්පූර්ණ මාර්ගෝපදේශය GitHub Desktop භාවිතයෙන්
---
![cover](assets/cover.webp)


මෙම නව උපකාරකය එකතු කිරීම පිළිබඳ උපකාරකය අනුගමනය කිරීමට පෙර, ඔබට කිහිපයක් මූලික පියවර සම්පූර්ණ කර තිබිය යුතුය. ඔබ එය තවම කර නොමැති නම්, මම ඔබට ප්‍රථමයෙන් මෙම හැඳින්වීමේ උපකාරකය පරීක්ෂා කිරීමට ආරාධනා කරමි, එවිට මෙහි නැවත පැමිණෙන්න:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

ඔබට දැනටමත්:


- ඔබේ උපදේශනය සඳහා තේමාව තෝරාගත්තා;
- Plan ₿ Network කණ්ඩායම අමතන්න [ටෙලිග්‍රෑම් කණ්ඩායම](https://t.me/PlanBNetwork_ContentBuilder) හරහා හෝ paolo@planb.network;
- ඔබේ දායකත්ව මෙවලම් තෝරා ගන්න.


මෙම උපකාරිකාවේදී, GitHub Desktop සමඟ ඔබේ දේශකය Plan ₿ Network මත එක් කිරීම සඳහා ඔබේ දේශීය පරිසරය පිහිටුවන්නේ කෙසේදැයි අපි බලන්නෙමු. ඔබ Git සමඟ දක්ෂ නම්, මෙම ඉතා විස්තරාත්මක උපකාරිකාව ඔබට අවශ්‍ය නොවන්නට පුළුවන්. මම වෙනුවට මෙම වෙනත් උපකාරිකාව උපදෙස් දෙන්නෙමි, එහිදී මම ප්‍රධාන මාර්ගෝපදේශ පමණක් ඉදිරිපත් කරන අතර, විස්තරාත්මක පියවරෙන් පියවර මාර්ගෝපදේශනය නොකරමි:



- අත්දැකීම් ඇති පරිශීලකයින්**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

If you prefer not to set up your local environment, follow this other tutorial designed for beginners, where we make the changes directly via GitHub's web Interface:



- අරඹන්නන් (වෙබ් Interface)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## ප්‍රාථමික අවශ්‍යතා


මෙම උපකාරක පසුපසින් පිවිසීමට අවශ්‍ය මෘදුකාංග:



- [GitHub Desktop](https://desktop.github.com/);
- Obsidian](https://obsidian.md/); වැනි මාර්ක්ඩවුන් ගොනු සංස්කාරකයක්;
- කේත සංස්කාරකයක් ([VSC](https://code.visualstudio.com/) හෝ [Sublime Text](https://www.sublimetext.com/))।


![TUTO](assets/fr/01.webp)


උපදේශය ආරම්භ කිරීමට පෙර අවශ්‍යතා:



- [GitHub ගිණුමක්](https://github.com/signup) ඇති වන්න;
- Ima Fork iz [Plan ₿ Network izvornega repozitorija](https://github.com/PlanB-Network/Bitcoin-educational-content);
- [A professor profile on Plan ₿ Network](https://planb.network/professors) (ඔබ සම්පූර්ණ උපකාරකයක් යෝජනා කරන්නේ නම් පමණක්).


Če potrebujete pomoč pri pridobivanju teh predpogojev, vam bodo moji drugi vodiči pomagali:



එක් වරක් සියල්ල ස්ථාපිත කර ඇති අතර ඔබේ ස්ථානීය පරිසරය ඔබේම Plan ₿ Network හි Fork සමඟ නිවැරදිව සකස් කර ඇති විට, ඔබට උපදේශකය එකතු කිරීම ආරම්භ කළ හැක.


## 1 - නව ශාඛාවක් සාදන්න


ඔබේ බ්‍රවුසරය විවෘත කර ඔබේ Plan ₿ Network ගබඩාවේ Fork පිටුවට යන්න. මෙය ඔබ GitHub හි ස්ථාපිත කළ Fork වේ. ඔබේ Fork හි URL මෙසේ පෙනිය යුතුය: `https://github.com/[your-username]/Bitcoin-educational-content`:


![TUTO](assets/fr/03.webp)


සහතික වන්න ඔබ ප්‍රධාන ශාඛාව `dev` මත සිටින බව, එවිට `Sync Fork` බොත්තම ක්ලික් කරන්න. ඔබේ Fork යාවත්කාලීන නොවේ නම්, GitHub ඔබේ ශාඛාව යාවත්කාලීන කිරීමට යෝජනා කරනු ඇත. මෙම යාවත්කාලීන කිරීම සමඟ ඉදිරියට යන්න. විපරීතව, ඔබේ ශාඛාව දැනටමත් යාවත්කාලීන නම්, GitHub ඔබට දැනුම් දෙනු ඇත:


![TUTO](assets/fr/04.webp)


GitHub Desktop programsko odprite in se prepričajte, da je vaš Fork pravilno izbran v zgornjem levem kotu okna:


![TUTO](assets/fr/05.webp)


Kliknite na gumb `Fetch origin`. Če je vaš lokalni repozitorij že posodobljen, GitHub Desktop ne bo predlagal nobenega dodatnega ukrepa. V nasprotnem primeru se bo prikazala možnost `Pull origin`. Kliknite na ta gumb, da posodobite svoj lokalni repozitorij:


![TUTO](assets/fr/06.webp)


සැබවින්ම ඔබ `dev` ප්‍රධාන ශාඛාවේ සිටින බව තහවුරු කරන්න:


![TUTO](assets/fr/07.webp)


මෙම ශාඛාව මත ක්ලික් කරන්න, එවිට `New Branch` බොත්තම මත ක්ලික් කරන්න:


![TUTO](assets/fr/08.webp)


සැකසීමේදී නව ශාඛාව මූලාශ්‍ර ගබඩාගත කිරීම මත පදනම් වූ බව, එනම් `PlanB-Network/Bitcoin-educational-content`, සහතික කරන්න.


Vejo svojo vejo poimenujte tako, da bo naslov jasno izražal njen namen, pri čemer uporabite vezaje za ločevanje vsake besede. Na primer, če je naš cilj napisati vadnico o uporabi programske opreme Sparrow Wallet. V tem primeru bi lahko delovno vejo, namenjeno pisanju te vadnice, poimenovali: `tuto-sparrow-Wallet-loic`. Ko vnesete ustrezno ime, kliknite na `Create branch`, da potrdite ustvarjanje veje:


![TUTO](assets/fr/09.webp)


Zdaj kliknite na gumb `Publish branch`, da shranite svojo novo delovno vejo v svoj spletni Fork na GitHub:

![TUTORIAL](assets/fr/10.webp)

Zdaj, na GitHub Desktop, bi morali biti na svoji novi veji. To pomeni, da bodo vse spremembe, narejene lokalno na vašem računalniku, izključno shranjene na tej specifični veji. Prav tako, dokler je ta veja izbrana na GitHub Desktop, datoteke, vidne lokalno na vašem računalniku, ustrezajo tistim na tej veji (`tuto-sparrow-Wallet-loic`), in ne tistim na glavni veji (`dev`).


![TUTORIAL](assets/fr/11.webp)


ඔබ ප්‍රකාශයට පත් කිරීමට කැමති සෑම නව ලිපියක් සඳහාම, ඔබට `dev` වෙතින් නව ශාඛාවක් නිර්මාණය කළ යුතුය. Git හි ශාඛාවක් යනු ව්‍යාපෘතියේ සමන්තර අනුවාදයක් වන අතර, එය ප්‍රධාන ශාඛාවට බලපෑමක් නොමැතිව වෙනස්කම් කිරීමට ඔබට ඉඩ සලසයි, කාර්යය ඒකාබද්ධ කිරීමට සූදානම් වන තුරු.


## 2 - උපදේශන ගොනු එකතු කිරීම


දැන් වැඩ කරන ශාඛාව නිර්මාණය කර ඇති බැවින්, ඔබේ නව උපකාරක පංතිය ඒකාබද්ධ කිරීමට වේලාවයි. ඔබට විකල්ප දෙකක් ඇත: අවශ්‍ය ලේඛන නිර්මාණය ස්වයංක්‍රීය කරන මගේ Python ස්ක්‍රිප්ට් එක භාවිතා කිරීම, හෝ එක් එක් ගොනුව මැනුවල්ව නිර්මාණය කිරීම. එක් එක් විකල්පය සඳහා අනුගමනය කළ යුතු පියවර බලමු.


### මගේ Python ස්ක්‍රිප්ට් සමඟ


ඔබේ යන්ත්‍රය මත ස්ථාපනය කළ යුතුය:


- Python 3.8 හෝ ඊට ඉහළ.


ස්ක්‍රිප්ට් එක භාවිතා කිරීමට, එය ගබඩා කර ඇති ෆෝල්ඩරයට යන්න. ස්ක්‍රිප්ට් එක Plan ₿ Network දත්ත ගබඩාවේ පිහිටා ඇත, මාර්ගය: `Bitcoin-educational-content/scripts/tutorial-related/data-creator`.


ෆෝල්ඩරය තුළට ගිය පසු, අවශ්‍ය අනුබද්ධතා ස්ථාපනය කරන්න:


```
pip install -r requirements.txt
```


එවිට විධානය සමඟ මෘදුකාංගය ආරම්භ කරන්න:


```
python3 main.py
```


Interface (GUI) ග්‍රැෆිකල් පරිශීලක අතුරුමුහුණතක් විවෘත වේ. පළමු වරට, ඔබට සියලුම අවශ්‍ය තොරතුරු ඇතුළත් කිරීමට අවශ්‍ය වන අතර, නමුත් පසුව භාවිතා කිරීමේදී, ලිපිය ඔබේ පුද්ගලික තොරතුරු මතක තබා ගනී, එබැවින් ඔබට නැවත එය ඇතුළත් කිරීමට අවශ්‍ය නොවේ.


![DATA-CREATOR-PY](assets/fr/37.webp)


පළමුව, ඔබේ පිටපත් කළ ගබඩාවේ `/tutorials` ෆෝල්ඩරය වෙත දේශීය මාර්ගය ඇතුළත් කරන්න (`.../Bitcoin-educational-content/tutorials/`). ඔබට එය අතින් ඇතුළත් කළ හැකි අතර නැතහොත් ඔබේ ගොනු විමසුම්කරු භාවිතා කරමින් නාවිගේෂණය කිරීමට "Browse" බොත්තම ක්ලික් කළ හැක.


![DATA-CREATOR-PY](assets/fr/38.webp)


ඔබේ උපකාරක පංතිය ලියන භාෂාව තෝරන්න.


![DATA-CREATOR-PY](assets/fr/39.webp)


"Contributor's GitHub ID" ක්ෂේත්‍රයේ, ඔබේ GitHub පරිශීලක නාමය ඇතුළත් කරන්න.


![DATA-CREATOR-PY](assets/fr/40.webp)


ඊළඟට, ඔබට ඔබේ මහාචාර්ය පැතිකඩ පුරවන්න අවශ්‍ය වේ. ඔබට ලබා ගත හැකි විකල්ප කිහිපයක් ඇත:


- "Professor Name" ක්ෂේත්‍රයේ ඔබේ නමෙහි පළමු අකුරු ඇතුළත් කරන්න. එවිට ඔබේ නම පහත "Prof. Suggestions" බහාලුම තුළ පෙනේ. එය ක්ලික් කිරීමෙන් තෝරන්න;
- විකල්ප ලෙස, ඔබට "Prof. Suggestions" බහින ලැයිස්තුව මත සෘජුවම ක්ලික් කර ඔබේ මහාචාර්ය නම තෝරා ගත හැක.


මෙම ක්‍රියාවෙන් ඔබේ මහාචාර්ය UUID සමාන ක්ෂේත්‍රයේ ස්වයංක්‍රීයව පුරවනු ලැබේ.



![DATA-CREATOR-PY](assets/fr/41.webp)


ඔබට තවමත් මහාචාර්ය පැතිකඩක් නොමැති නම්, මෙම උපකාරකය බලන්න:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

පසුව "New Tutorial" බොත්තම ක්ලික් කරන්න.


![DATA-CREATOR-PY](assets/fr/42.webp)


ඔබේ උපකාරකය සඳහා ප්‍රධාන ප්‍රවර්ගයක් තෝරන්න. එවිට, ඔබ තෝරාගත් ප්‍රධාන ප්‍රවර්ගය මත පදනම්ව අදාල උප ප්‍රවර්ගයක් තෝරන්න.


![DATA-CREATOR-PY](assets/fr/43.webp)


ටියුටෝරියලයේ අපහසුතා මට්ටම තීරණය කරන්න.


![DATA-CREATOR-PY](assets/fr/44.webp)


ඔබේ උපකාරකය සඳහා විශේෂයෙන් නිර්මාණය කරන ලද නාමාවලිය සඳහා නමක් තෝරන්න. මෙම ෆෝල්ඩරයේ නම උපකාරකයෙහි ආවරණය වන මෘදුකාංගය පෙන්විය යුතු අතර, වචන වෙන් කිරීමට හයිෆන් භාවිතා කළ යුතුය. උදාහරණයක් ලෙස, ෆෝල්ඩරය `red-Wallet` ලෙස නම් කළ හැක:


![DATA-CREATOR-PY](assets/fr/45.webp)


`project_id` යනු උපකාරකය ආවරණය කරන උපකාරකය පිටුපස ඇති සමාගම හෝ සංවිධානයේ UUID වේ, [ව්‍යාපෘති ලැයිස්තුවේ](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) ලබා ගත හැක. උදාහරණයක් ලෙස, Sparrow Wallet පිළිබඳ උපකාරකයක් සඳහා, එහි `project_id` සොයා ගත හැක: `Bitcoin-educational-content/resources/projects/sparrow/project.yml` ගොනුවේ. මෙම තොරතුරු ඔබේ උපකාරකයේ YAML ගොනුවට එක් කරනු ලබන්නේ Plan ₿ Network, Bitcoin හෝ සබැඳි ව්‍යාපෘතිවල ක්‍රියාකාරී සමාගම් සහ සංවිධානවල දත්ත සමුදායක් පවත්වාගෙන යන බැවිනි. සම්බන්ධ `project_id` එක එක් කිරීමෙන්, ඔබේ අන්තර්ගතය සම්බන්ධිත අ实体යට සම්බන්ධ කරයි.


***යාවත්කාලීන කිරීම:*** ස්ක්‍රිප්ට් එකේ නව අනුවාදයේ, ඔබට අතින් `project_id` ඇතුළත් කිරීමට අවශ්‍ය නැත. ව්‍යාපෘතිය නමෙන් සොයා, අදාළ `project_id` ස්වයංක්‍රීයව ලබා ගැනීමට සෙවීම් ක්‍රියාවලියක් එකතු කර ඇත. "Project Name" ක්ෂේත්‍රයේ ව්‍යාපෘතියේ නම ආරම්භක අකුරු ටයිප් කර සොයන්න, එවිට අවශ්‍ය සමාගම dropdown මෙනුවෙන් තෝරන්න. `project_id` පහත ක්ෂේත්‍රයේ ස්වයංක්‍රීයව පිරවෙනු ඇත. අවශ්‍ය නම්, ඔබට එය අතින් ද ඇතුළත් කළ හැක.


![DATA-CREATOR-PY](assets/fr/46.webp)


ටැග සඳහා, [Plan ₿ Network ටැග ලැයිස්තුව](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) තුළින් පමණක් ඔබේ උපදේශන අන්තර්ගතයට අදාල 2 හෝ 3 මූලික වචන තෝරන්න. මෘදුකාංගය මූලික වචන සෙවීමේ ක්‍රියාවලියක් සහ ඩ්‍රොප්ඩවුන් ලැයිස්තුවක් ද සපයයි.


![DATA-CREATOR-PY](assets/fr/47.webp)


සියලුම තොරතුරු ඇතුළත් කර සත්‍යාපනය කළ පසු, ඔබේ උපකාරක ලිපිගොනු නිර්මාණය තහවුරු කිරීමට "Create Tutorial" ක්ලික් කරන්න. මෙය තේරූ ප්‍රවර්ගයේ ඔබේ උපකාරක ෆෝල්ඩරය සහ සියලුම අවශ්‍ය ලිපිගොනු ස්ථානීයව generate කරනු ඇත.


![DATA-CREATOR-PY](assets/fr/48.webp)


ඔබට දැන් "මගේ Python ස්ක්‍රිප්ට් නොමැතිව" යන උපකණ්ඩායම මඟ හැරිය හැකි අතර, පියවර 3, "YAML ගොනුව පුරවන්න," මඟ හැරිය හැක, මන්ද ස්ක්‍රිප්ට් එක මේවා දැනටමත් ඔබ වෙනුවෙන් සම්පූර්ණ කර ඇත. පියවර 4 වෙත සෘජුවම ගොස් ඔබේ උපකාරකය ලියන්න ආරම්භ කරන්න.


Za več informacij o tem Python skriptu si lahko ogledate tudi [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


### මගේ Python ස්ක්‍රිප්ට් නැතිව


ඔබේ ගොනු කළමනාකරු විවෘත කර `Bitcoin-educational-content` ෆෝල්ඩරය වෙත යන්න, එය ඔබේ ගබඩා භාණ්ඩයේ ස්ථානීය පිටපත නිරූපණය කරයි. සාමාන්‍යයෙන් එය `Documents\GitHub\Bitcoin-educational-content` යටතේ සොයා ගත හැක.


මෙම නාමාවලිය තුළ, ඔබේ උපකාරකය තැබීමට සුදුසු උපෆෝල්ඩරය සොයා ගත යුතුය. ෆෝල්ඩර සංවිධානය Plan ₿ Network වෙබ් අඩවියේ විවිධ අංශ නිරූපණය කරයි. අපගේ උදාහරණයේ, අපි Sparrow Wallet පිළිබඳ උපකාරකයක් එක් කිරීමට අවශ්‍ය බැවින්, අපි පහත මාර්ගය වෙත ගමන් කළ යුතුය: `Bitcoin-educational-content\tutorials\Wallet`, එය වෙබ් අඩවියේ `Wallet` අංශයට අදාළ වේ:


![TUTO](assets/fr/12.webp)


`Wallet` ෆෝල්ඩරය තුළ, ඔබේ උපකාරක පංතිය සඳහා විශේෂිතව නව ඩිරෙක්ටරියක් නිර්මාණය කළ යුතුය. මෙම ෆෝල්ඩරයේ නම උපකාරක පංතියේ ආවරණය වන මෘදුකාංගය මත පදනම් විය යුතු අතර, වචන සම්බන්ධ කිරීම සඳහා ඉරක් භාවිතා කළ යුතුය. මගේ උදාහරණය සඳහා, ෆෝල්ඩරය `sparrow-Wallet` ලෙස නම් කරනු ඇත:


![TUTO](assets/fr/13.webp)


මෙම නව උප-ෆෝල්ඩරය ඔබේ උපකාරකය සඳහා කැපවූ අතර, Elements කිහිපයක් එකතු කිරීමට අවශ්‍ය වේ:


- `assets` ෆෝල්ඩරයක් සාදන්න, ඔබේ උපදේශනය සඳහා අවශ්‍ය සියලු නිර්මාණ සඳහා;
- මෙම `assets` ෆෝල්ඩරය තුළ, ඔබට උපදෙස්පොතේ මුල් භාෂා කේතය අනුව නම් කරන ලද උප-ෆෝල්ඩරයක් සාදන්න අවශ්‍ය වේ. උදාහරණයක් ලෙස, උපදෙස්පොත ඉංග්‍රීසි භාෂාවෙන් ලියන ලද්දේ නම්, මෙම උප-ෆෝල්ඩරය `en` ලෙස නම් කළ යුතුය. උපදෙස්පොතේ සියලු දෘශ්‍ය (රූප, රූප, තිර රූප, ආදිය) එහි තබන්න.
- `tutorial.yml` ගොනුවක් ඔබේ උපකාරකය සම්බන්ධ විස්තර සටහන් කිරීමට නිර්මාණය කළ යුතුය;
- Markdown obliko datoteke je treba ustvariti za pisanje dejanske vsebine vašega vadnice. Ta datoteka mora biti naslovljena v skladu z jezikovno kodo pisanja. Na primer, za vadnico, napisano v francoščini, mora biti datoteka imenovana `fr.md`.


![TUTO](assets/fr/14.webp)


සාරාංශයක් ලෙස, නිර්මාණය කිරීමට ඇති ගොනු පරිපාලනය මෙන්න:


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```


## 3 - YAML ගොනුව පුරවන්න


Izpolnite datoteko `tutorial.yml` tako, da kopirate naslednjo predlogo:


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



- id** : UUID (_Universally Unique Identifier_) එකක් වන අතර එය උපකාරකය අනන්‍යව හඳුනාගනී. ඔබට [සබැඳි මෙවලමක්](https://www.uuidgenerator.net/version4) භාවිතා කර generate කළ හැක. එකම අවශ්‍යතාවය වන්නේ මෙම UUID එක අහඹු විය යුතු අතර වේදිකාවේ වෙනත් UUID සමඟ ගැටුම් වලක්වයි;



- project_id** : මෙහෙයුම් පසුබිම පිළිබඳව ඉදිරිපත් කරන ලද මෙවලම පිළිබඳ උපකාරක පංතියේ සමාගම හෝ සංවිධානයේ UUID [ව්‍යාපෘති ලැයිස්තුවෙන්](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) ලබා ගන්න. උදාහරණයක් ලෙස, ඔබ Green Wallet මෘදුකාංගය පිළිබඳ උපකාරක පංතියක් නිර්මාණය කරන්නේ නම්, මෙම `project_id` පහත ගොනුවේ සොයා ගත හැක: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. මෙම තොරතුරු ඔබේ උපකාරක පංතියේ YAML ගොනුවට එක් කරනුයේ Plan ₿ Network විසින් Bitcoin හෝ සම්බන්ධ ව්‍යාපෘතිවල ක්‍රියාත්මක වන සියලු සමාගම් සහ සංවිධානවල දත්ත සමුදායක් පවත්වාගෙන යන බැවිනි. ඔබේ උපකාරක පංතියට සම්බන්ධිත අංශයේ `project_id` එක එක් කිරීමෙන්, ඔබ Elements අතර සබැඳියක් නිර්මාණය කරයි;



- tags** : 2 හෝ 3 සම්බන්ධිත මූලික පද, පමණක් [Plan ₿ Network ටැග් ලැයිස්තුවෙන්](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) තෝරාගන්න;



- ප්‍රවර්ගය** : Plan ₿ Network වෙබ් අඩවියේ ව්‍යුහය අනුව උපකාරක අන්තර්ගතයට අදාළ උප-ප්‍රවර්ගය (උදාහරණයක් ලෙස, පසුම්බි සඳහා: `ඩෙස්ක්ටොප්`, `හාර්ඩ්වෙයාර්`, `ජංගම`, `උපස්ථ`);



- මට්ටම** : උපකාරක පඬියෙහි අපහසුතා මට්ටම, තෝරාගන්න:
    - `අරඹන්නා`
    - `මධ්‍යස්ථ`
    - `උසස්`
    - `ප්‍රවීණ`



- professor_id** : ඔබේ `professor_id` (UUID) [ඔබේ මහාචාර්ය පැතිකඩ](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) හි පෙන්වා ඇති පරිදි;



- original_language** : උපදෙස් මාලාවේ මුල් භාෂාව (උදාහරණයක් ලෙස, `fr`, `en`, ආදිය);



- ප්‍රමාණය සනාථ කිරීම** : පරීක්ෂාකරණ ක්‍රියාවලිය පිළිබඳ තොරතුරු. පළමු කොටස සම්පූර්ණ කරන්න, ඔබේම උපකාරකය පරීක්ෂාකරණය කිරීම පළමු සනාථ කිරීමක් ලෙස ගණනය වේ:
    - භාෂාව** : පරීක්ෂාකරණයේ භාෂා කේතය (උදාහරණයක් ලෙස, `fr`, `en`, ආදිය).
    - last_contribution_date** : දිනය.
    - urgency** : 1
    - contributor_names** : ඔබේ GitHub හැඳුනුම්පත.
    - nagrada** : 0


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


ඔබගේ `tutorial.yml` ගොනුව සංස්කරණය කිරීම අවසන් වූ විට, `File > Save` ක්ලික් කිරීමෙන් ඔබගේ ලේඛනය සුරකින්න:


![TUTO](assets/fr/16.webp)


ඔබට දැන් ඔබේ කේත සංස්කාරකය වසා දැමිය හැක.


## 4 - Markdown දෝෂාත්මක ලිපිය පුරවන්න


දැන්, ඔබේ භාෂාවේ කේතය සමඟ නම් කරන ලද, ඔබේ උපකාරකය සත්කාර කරන ඔබේ ගොනුව විවෘත කළ හැක, `fr.md` වැනි. Obsidian වෙත යන්න, කවුළුවේ වම් පැත්තේ, ඔබේ උපකාරකය සහ ඔබ සොයන ගොනුව ඇති ෆෝල්ඩරය සොයා ගන්නා තුරු ෆෝල්ඩරය ගස් හරහා ගොස් බලන්න:


![TUTO](assets/fr/18.webp)


දොස්සිය විවෘත කිරීමට එය ක්ලික් කරන්න:


![TUTO](assets/fr/19.webp)


අපි ලේඛනයේ ඉහළින් ඇති `Properties` අංශය පුරවා ආරම්භ කරමු.


![TUTO](assets/fr/20.webp)


Ročno dodajte in izpolnite naslednji blok kode:


```
---
name: [Title]
description: [Description]
---
```


![TUTO](assets/fr/21.webp)


ඔබේ උපකාරක පන්ති නාමය සහ එහි කෙටි විස්තරයක් පුරවන්න:


![TUTO](assets/fr/22.webp)


එවිට, ඔබේ උපදේශනයේ ආවරණ රූපයේ මාර්ගය ආරම්භයේ එකතු කරන්න. මෙය කිරීමට, සටහන් කරන්න:


```
![cover-sparrow](assets/cover.webp)
```


මෙම ව්‍යാകරණය ඔබේ උපකාරකයට රූපයක් එක් කිරීම අවශ්‍ය වන විට ප්‍රයෝජනවත් වනු ඇත. විශ්මය ලකුණක් එය රූපයක් බව පෙන්වයි, විකල්ප පෙළ (alt) වරහන් අතර සඳහන් වේ. රූපය වෙත මාර්ගය වරහන් අතර සඳහන් වේ:


![TUTO](assets/fr/23.webp)


## 5 - ලාංඡනය සහ ආවරණය එක් කරන්න


`assets` ෆෝල්ඩරය තුළ, ඔබට `logo.webp` නම් කරන ලද ගොනුවක් එක් කළ යුතු අතර, එය ඔබේ ලිපිය සඳහා කෙටි රූපයක් ලෙස සේවය කරනු ඇත. මෙම රූපය `.webp` ආකෘතියෙන් විය යුතු අතර, පරිශීලක Interface සමඟ සමාන්විත වීමට වර්ග ප්‍රමාණයක් ගරු කළ යුතුය. ඔබට පසුගිය පාඩම් මාලාවේ ආවරණය කරන ලද මෘදුකාංගයේ ලාංඡනය හෝ වෙනත් අදාල රූපයක් තෝරා ගැනීමට නිදහස් වන අතර, එය හිමිකම් රහිත විය යුතුය. අමතරව, ඒම ස්ථානයේ `cover.webp` ලෙස නම් කරන ලද රූපයක්ද එක් කරන්න. මෙම රූපය ඔබේ පාඩම් මාලාවේ ඉහළින් පෙන්වනු ඇත. මෙම රූපය, ලාංඡනය මෙන්ම, භාවිතා කිරීමේ අයිතිවාසිකම් ගරු කරන අතර ඔබේ පාඩම් මාලාවේ සන්දර්භයට සුදුසු විය යුතුය:

## 6 - උපදේශය ලිවීම සහ දෘශ්‍ය එකතු කිරීම


ඔබේ අධ්‍යාපනික මාර්ගෝපදේශය ලිවීම දිගටම කරගෙන යන්න. උපශීර්ෂිකාවක් එක් කිරීමට අවශ්‍ය වන විට, `##` යන පෙරනිමිය සමඟ පෙළට සුදුසු markdown ආකෘතිය යොදා ගන්න:


![TUTO](assets/fr/24.webp)


`assets` ෆෝල්ඩරයේ භාෂා උපෆෝල්ඩරය ඔබේ උපකාරක පථය සමඟ යා යුතු රූප සහ දෘශ්‍ය සටහන් ගබඩා කිරීමට භාවිතා වේ. හැකි තාක්, ඔබේ අන්තර්ගතය ජාත්‍යන්තර පිරිසකට ප්‍රවේශ විය හැකි ලෙස ඔබේ රූපවල පෙළ ඇතුළත් කිරීමෙන් වළකින්න. නිසැකවම, ඉදිරිපත් කරන ලද මෘදුකාංගය පෙළ අඩංගු වනු ඇත, නමුත් ඔබ මෘදුකාංග තිර රූපවල රූප සටහන් හෝ අමතර සලකුණු එකතු කරනවා නම්, පෙළ නොමැතිව එය කරන්න හෝ, එය අත්‍යවශ්‍ය නම්, ඉංග්‍රීසි භාවිතා කරන්න.


![TUTO](assets/fr/25.webp)


Če želite poimenovati svoje slike, preprosto uporabite številke, ki ustrezajo njihovemu vrstnemu redu pojavljanja v vadnici, oblikovane z dvema števkama (ali tremi števkami, če vaša vadnica vsebuje več kot 99 slik). Na primer, svojo prvo sliko poimenujte `01.webp`, drugo `02.webp` in tako naprej.


ඔබේ රූප අනිවාර්යයෙන්ම `.webp` ආකෘතියෙන් තිබිය යුතුය. අවශ්‍ය නම්, ඔබට [මගේ රූප පරිවර්තක මෘදුකාංගය](https://github.com/LoicPandul/ImagesConverter) භාවිතා කළ හැක.


![TUTO](assets/fr/26.webp)


ඔබේ ලේඛනයට රූපයක් ඇතුළත් කිරීමට, පහත Markdown විධානය භාවිතා කරන්න, නිවැරදි විකල්ප පෙළ සහ රූපයේ නිවැරදි මාර්ගය සඳහන් කිරීම සහතික කරමින්:


```
![sparrow](assets/fr/01.webp)
```


ඉදිරිපිට ඇති විශ්මය ලකුණය එය රූපයක් බව පෙන්වයි. ප්‍රතිවාදී පාඨය, ප්‍රවේශය සහ SEO සඳහා උපකාරී වන, කෝෂ්ඨක අතර තබා ඇත. අවසානයේ, රූපය වෙත මාර්ගය වරන්තු අතර සඳහන් වේ.


ඔබේම රූප සටහන් නිර්මාණය කිරීමට කැමති නම්, දෘශ්‍ය සමාන්ජසතාවය සහතික කිරීම සඳහා Plan ₿ Network හි ග්‍රැෆික් ආකෘතියට අනුකූල වන්න:


- Font**: Use [Rubik](https://fonts.google.com/specimen/Rubik);
- Colors**:
 - Orange: #FF5C00
 - කළු: #000000
 - Belo: #FFFFFF


**ඔබගේ උපකාරක පඬිවලට ඒකාබද්ධ කරන සියලු දෘශ්‍යයන් අයිතිවාසිකම් රහිත හෝ මූලාශ්‍ර ගොනුවේ බලපත්‍රය ගෞරවයෙන් පවතින බව අත්‍යවශ්‍ය වේ**. එසේම, Plan ₿ Network හි ප්‍රකාශයට පත් කරන සියලු ආරේඛන, පෙළ මෙන්ම CC-BY-SA බලපත්‍රය යටතේ ලබා දේ.

**-> උපදෙස්:** රූප වැනි ගොනු මහජනතාවට බෙදා ගැනීමේදී, අවශ්‍ය නොවන මेटා දත්ත ඉවත් කිරීම වැදගත් වේ. මෙය ස්ථානයේ දත්ත, නිර්මාණ දිනයන්, හෝ කතුවරයා පිළිබඳ විස්තර වැනි සංවේදී තොරතුරු අඩංගු විය හැක. ඔබේ පෞද්ගලිකත්වය ආරක්ෂා කිරීම සඳහා, මෙම මेटා දත්ත මකා දැමීම සුදුසුය. මෙම ක්‍රියාවලිය සරල කිරීම සඳහා, [Exif Cleaner](https://exifcleaner.com/) වැනි විශේෂිත මෙවලම් භාවිතා කළ හැක, එය ලේඛනයක මेटා දත්ත සරල ඇදීම සහ අත්හැරීම මඟින් පිරිසිදු කිරීමට ඉඩ සලසයි.

## 7 - ටියුටෝරියලය සුරකින්න සහ ඉදිරිපත් කරන්න


ඔබට ඔබේ උපකාරකය ඔබ කැමති භාෂාවෙන් ලිවීම අවසන් වූ විට, ඊළඟ පියවර වන්නේ **Pull Request** එකක් ඉදිරිපත් කිරීමයි. පරිපාලකයා පසුව ඔබේ උපකාරකයේ අතපසු වූ පරිවර්තන එකතු කිරීමේ කටයුතු සිදු කරනු ඇත, අපගේ මිනිස් සමාලෝචනය සහිත ස්වයංක්‍රීය පරිවර්තන ක්‍රමය සඳහා ස්තූතියි.


ප්‍රතිලාභ ඉල්ලීම (Pull Request) සමඟ ඉදිරියට යාමට, GitHub Desktop මෘදුකාංගය විවෘත කරන්න. ඔබේ ශාඛාවේ ස්ථානීයව සිදු කළ වෙනස්කම් මුල් ගබඩායට සාපේක්ෂව මෘදුකාංගය ස්වයංක්‍රීයව හඳුනා ගත යුතුය. ඉදිරියට යාමට පෙර, Interface හි වම පැත්තේ මෙම වෙනස්කම් ඔබේ අපේක්ෂාවට ගැලපෙන බව කාර්යක්ෂමව පරීක්ෂා කරන්න:


![TUTO](assets/fr/28.webp)


ඔබේ commit සඳහා ශීර්ෂයක් එක් කරන්න, එවිට මෙම වෙනස්කම් වලංගු කිරීමට නිල් `Commit to [your branch]` බොත්තම ක්ලික් කරන්න:


![TUTO](assets/fr/29.webp)


කමිටුව යනු ශාඛාවට සිදු කරන ලද වෙනස්කම් සුරැකීමක් වන අතර, විස්තරාත්මක පණිවිඩයක් සමඟ එය සපයනු ලබයි, කාලයත් සමඟ ව්‍යාපෘතියේ විකාශනය අනුගමනය කිරීමට ඉඩ සලසයි. එය මධ්‍යස්ථ පරීක්ෂණ ස්ථානයක් වැනි එකක් වේ.


පසුව `Push origin` බොත්තම ක්ලික් කරන්න. මෙය ඔබේ කමිටුව ඔබේ Fork වෙත යවනු ඇත:


![TUTO](assets/fr/30.webp)


Če še niste zaključili svojega vodiča, se lahko kasneje vrnete nanj in naredite nove potrditve. Če ste zaključili svoje spremembe za to vejo, kliknite zdaj na gumb `Preview Pull Request`:


![TUTO](assets/fr/31.webp)


ඔබේ වෙනස්කම් නිවැරදි බව අවසන් වරට පරීක්ෂා කළ හැක, එවිට `Create pull request` බොත්තම ක්ලික් කරන්න:


![TUTO](assets/fr/32.webp)


පූල් අයදුමක් යනු Plan ₿ Network ගබඩායේ ප්‍රධාන ශාඛාවට ඔබේ ශාඛාවේ වෙනස්කම් ඒකාබද්ධ කිරීමට කරන අයදුමක් වන අතර, ඒකාබද්ධ කිරීමට පෙර වෙනස්කම් සමාලෝචනය කිරීම සහ සාකච්ඡා කිරීම සඳහා අවස්ථාව ලබා දේ.


Samode samode GitHub brskalnik preusmeri na pripravljalno stran vašega Pull Request:


![TUTO](assets/fr/33.webp)

ඔබ මූලාශ්‍ර ගබඩාව සමඟ ඒකාබද්ධ කිරීමට කැමති වෙනස්කම් සාරාංශ ගත කරන ශීර්ෂයක් සටහන් කරන්න. මෙම වෙනස්කම් විස්තර කරන කෙටි විස්තරයක් එක් කරන්න (ඔබේ උපකාරකය නිර්මාණය කිරීම සමඟ සම්බන්ධිත ගැටළුවක් ඇත්නම්, විශේෂණය `Closes #{issue number}` ලෙස සටහන් කරන්න), එවිට Green `Create pull request` බොත්තම ක්ලික් කර ඒකාබද්ධ ඉල්ලීම තහවුරු කරන්න:

![TUTO](assets/fr/34.webp)


ඔබගේ PR පසු දැනටමත් Plan ₿ Network ප්‍රධාන ගබඩාගත කිරීමේ `Pull Request` ටැබ් එකේ දෘශ්‍යමාන වනු ඇත. ඔබ කළ යුත්තේ පරිපාලකයෙකු ඔබව සම්බන්ධ කර ගැනීමට හෝ ඔබගේ දායකත්වය ඒකාබද්ධ කිරීම තහවුරු කිරීමට හෝ අමතර වෙනස්කම් කිසිවක් ඉල්ලා සිටීමට බලා සිටීම පමණි.


![TUTO](assets/fr/35.webp)


ඔබගේ PR ප්‍රධාන ශාඛාව සමඟ ඒකාබද්ධ වූ පසු, ඔබේ වැඩ කරන ශාඛාව (`tuto-sparrow-Wallet`) මකා දැමීම නිර්දේශ කෙරේ, ඔබේ Fork හි පිරිසිදු ඉතිහාසයක් පවත්වා ගැනීමට. GitHub ඔබට මෙම විකල්පය ස්වයංක්‍රීයව ඔබේ PR පිටුවේදී ලබා දෙනු ඇත:


![TUTO](assets/fr/36.webp)


GitHub Desktop මෘදුකාංගය මත, ඔබට ඔබේ Fork (`dev`) හි ප්‍රධාන ශාඛාවට නැවත මාරු විය හැක.


![TUTO](assets/fr/07.webp)


ඔබේ දායකත්වය PR එකක් ලෙස ඉදිරිපත් කිරීමෙන් පසු වෙනස්කම් කිරීමට කැමති නම්, ක්‍රියාවලිය ඔබේ වර්තමාන PR තත්ත්වය මත රඳා පවතී:


- ඔබගේ PR තවමත් විවෘතව ඇති අතර ඒක එකතු කර නොමැති නම්, ඒම ශාඛාවේ සිටම ස්ථානීයව වෙනස්කම් කරන්න. වෙනස්කම් අවසන් වූ විට, ඔබගේ තවමත් විවෘත PR එකට නව කමිටුවක් එකතු කිරීමට `Push origin` බොත්තම භාවිතා කරන්න;
- ඔබේ PR දැනටමත් ප්‍රධාන ශාඛාව සමඟ ඒකාබද්ධ කර ඇති නම්, ඔබට නව ශාඛාවක් නිර්මාණය කිරීමෙන් පසු, නව PR එකක් ඉදිරිපත් කිරීමෙන් ක්‍රියාවලිය නැවත ආරම්භ කළ යුතුය. ඉදිරියට යාමට පෙර ඔබේ දේශීය ගබඩාව Plan ₿ Network මූලාශ්‍ර ගබඩාව සමඟ සමානීකරණය වී ඇති බව සහතික කරන්න.


ඔබේ උපකාරකය ඉදිරිපත් කිරීමේදී තාක්ෂණික අපහසුතා වලට මුහුණ දෙනවා නම්, [අපගේ දායකත්ව සඳහා කැපවූ ටෙලිග්‍රෑම් කණ්ඩායමෙන්](https://t.me/PlanBNetwork_ContentBuilder) උදව් ඉල්ලීමට අකමැති වන්න එපා. ස්තුතියි!