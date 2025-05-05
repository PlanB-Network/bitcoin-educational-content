---
name: Prispevek - GitHub spletni vodič (začetnik)
description: Plan ₿ Network ටියුටෝරියල් සඳහා සම්පූර්ණ මාර්ගෝපදේශය GitHub වෙබ් සමඟ
---
![cover](assets/cover.webp)


මෙම නව උපකාරකය එකතු කිරීම පිළිබඳ උපකාරකය අනුගමනය කිරීමට පෙර, ඔබට කිහිපයක් මූලික පියවර සම්පූර්ණ කර තිබිය යුතුය. ඔබ එය දැනටමත් කර නොමැති නම්, කරුණාකර පළමුව මෙම හැඳින්වීමේ උපකාරකය බලන්න, එවිට මෙහි නැවත පැමිණෙන්න:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

ඔබට දැනටමත් ඇත :




- ඔබේ උපකාරක පංතිය සඳහා තේමාවක් තෝරන්න;
- Plan ₿ Network ekipo kontaktirajte prek [Telegram skupine](https://t.me/PlanBNetwork_ContentBuilder) ali paolo@planb.network ;
- ඔබේ දායකත්ව මෙවලම් තෝරන්න.


V tem vadnici bomo pogledali, kako dodati svojo vadnico v Plan ₿ Network z uporabo spletne različice GitHub. Če ste že obvladali Git, ta zelo podrobna vadnica morda ni potrebna za vas. Namesto tega vam priporočam, da si ogledate eno od teh drugih 2 vadnic, kjer podrobno opisujem smernice, ki jih je treba upoštevati, in korake za izvajanje sprememb iz lokalnega :




- अनुभवी उपयोगकर्ता** :


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- අතරමැදි (GitHub Desktop)** :


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## ප්‍රාථමික අවශ්‍යතා


පහසුකම් පෙර පාඩම් ආරම්භ කිරීමට පෙර :




- [GitHub ගිණුමක්](https://github.com/signup) ඇති වන්න;
- ආශ්‍රිත ගබඩාවේ [Plan ₿ Network මූලාශ්‍රය](https://github.com/PlanB-Network/Bitcoin-educational-content) හි Fork එකක් ගන්න;
- [Ape profil učitelja na Plan ₿ Network](https://planb.network/professors) (samo če ponujate celoten tutorial).


Če potrebujete pomoč pri pridobivanju teh predpogojev, vam bodo moji drugi vodiči pomagali:



https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

එක් වරක් සියල්ල ස්ථාපිත කර, ඔබට Plan ₿ Network ගබඩාවේ Fork ලැබුණු පසු, ඔබට උපකාරකය එකතු කිරීමට ආරම්භ කළ හැක.


## 1 - නව ශාඛාවක් සාදන්න


ඔබේ බ්‍රවුසරය විවෘත කර ඔබේ Fork පිටුවට Plan ₿ Network ගබඩාවේ යන්න. මෙය ඔබ GitHub හි ස්ථාපිත කළ Fork වේ. ඔබේ Fork හි URL මෙසේ පෙනිය යුතුය: `https://github.com/[your-username]/Bitcoin-educational-content` :


![GITHUB](assets/fr/01.webp)


පිළිබඳව විශ්වාසවන්ත වන්න ඔබ ප්‍රධාන `dev` ශාඛාවේ සිටින බව, එවිට "*Sync Fork*" බොත්තම ක්ලික් කරන්න. ඔබේ Fork යාවත්කාලීන නොවන්නේ නම්, GitHub ඔබට ඔබේ ශාඛාව යාවත්කාලීන කිරීමට අයදුම් කරනු ඇත. මෙම යාවත්කාලීන කිරීම සමඟ ඉදිරියට යන්න:


![GITHUB](assets/fr/02.webp)


`dev` ශාඛාව මත ක්ලික් කරන්න, එවිට එහි මාතෘකාව එහි අරමුණ පැහැදිලිව පෙන්වෙන පරිදි ඔබේ කාර්ය ශාඛාව නම් කරන්න, වචන වෙන් කිරීමට ඉරක් භාවිතා කරන්න. උදාහරණයක් ලෙස, අපේ අරමුණ Green Wallet භාවිතා කිරීම පිළිබඳ උපකාරක පංතියක් ලිවීම නම්, ශාඛාව මෙසේ නම් කළ හැක: `tuto-Green-Wallet-loic`. සුදුසු නමක් ඇතුළත් කිරීමෙන් පසු, ඔබේ නව ශාඛාව `dev` මත පදනම්ව නිර්මාණය කිරීම තහවුරු කිරීමට "*Create branch*" මත ක්ලික් කරන්න:


![GITHUB](assets/fr/03.webp)


ඔබ දැන් ඔබේ නව කාර්ය ශාඛාවෙහි සිටිය යුතුය:


![GITHUB](assets/fr/04.webp)


මෙම අර්ථය වන්නේ ඔබ කරන ඕනෑම වෙනස්කම් එම විශේෂිත ශාඛාවෙහි පමණක් සුරකිනු ඇත.


ඔබ ප්‍රකාශයට පත් කිරීමට සැලසුම් කරන සෑම නව ලිපියක් සඳහාම, `dev` වෙතින් නව ශාඛාවක් සාදන්න.


Git හි ශාඛාවක් යනු ව්‍යාපෘතියේ සමන්තර අනුවාදයක් නිරූපණය කරන අතර, ඔබේ කාර්යය ඒකාබද්ධ කිරීමට සූදානම් වන තුරු ප්‍රධාන ශාඛාවට බලපෑමකින් තොරව වෙනස්කම් මත වැඩ කිරීමට ඔබට ඉඩ සලසයි.


## 2 - උපදේශන ගොනු එක් කරන්න


දැන් වැඩ කරන ශාඛාව නිර්මාණය කර ඇති බැවින්, ඔබේ නව උපකාරක පංතිය ඒකාබද්ධ කිරීමට වේලාවයි.


ඔබේ ශාඛා ගොනු තුළ, ඔබේ උපකාරකය තැබීම සඳහා සුදුසු උපකෝෂය සොයා ගත යුතුය. ගොනු සංවිධානය Plan ₿ Network වෙබ් අඩවියේ විවිධ අංශයන් නිරූපණය කරයි. අපගේ උදාහරණයේ, අපි Green Wallet පිළිබඳ උපකාරකයක් එකතු කරන බැවින්, පහත මාර්ගය වෙත යන්න: `Bitcoin-educational-content\tutorials\Wallet` එය වෙබ් අඩවියේ `Wallet` අංශයට අදාළ වේ:


![GITHUB](assets/fr/05.webp)


V mapi `Wallet` ustvarite nov imenik, namenjen posebej vašemu priročniku. Ime te mape naj jasno označuje programsko opremo, obravnavano v priročniku, pri čemer uporabite vezaje za povezovanje besed. Za moj primer bo mapa imenovana `Green-Wallet`. Kliknite na "*Add File*" nato na "*Create new file*" :


![GITHUB](assets/fr/06.webp)


ඇතුල් කරන්න ෆෝල්ඩරයේ නම සහිත `/` එය ෆෝල්ඩරයක් ලෙස නිර්මාණය කිරීම තහවුරු කිරීමට.


![GITHUB](assets/fr/07.webp)


මෙම නව උපසංචිකාවට ඔබේ උපකාරකය සඳහා, ඔබට විවිධ අයිතම එකතු කළ යුතුය:




- ඔබේ උපදේශනය සඳහා අවශ්‍ය සියලු නිර්මාණ සඳහා `assets` ෆෝල්ඩරයක් සාදන්න;
- මෙම `assets` ෆෝල්ඩරය තුළ, උපකාරිකාවේ මුල් භාෂා කේතය අනුව නමකරණය කරන ලද උපෆෝල්ඩරයක් සාදන්න. උදාහරණයක් ලෙස, උපකාරිකාව ඉංග්‍රීසි භාෂාවෙන් ලියන ලද්දේ නම්, මෙම උපෆෝල්ඩරය `en` ලෙස නම් කළ යුතුය. උපකාරිකාවේ දෘශ්‍ය (රූප, රූප, තිර රූප, ආදිය) සියල්ල මෙම ෆෝල්ඩරය තුළ තබන්න.
- `tutorial.yml` ෆයිල් එකක් නිර්මාණය කළ යුතුය ඔබේ උපකාරක පන්ති විස්තර සටහන් කිරීමට;
- ඔබේ උපදේශනයේ සත්‍ය අන්තර්ගතය ලිවීමට අනිවාර්යයෙන්ම මාර්ක්ඩවුන් ගොනුවක් තැනිය යුතුය. මෙම ගොනුව එය ලියන භාෂාවේ කේතය අනුව නම් කළ යුතුය. උදාහරණයක් ලෙස, ප්‍රංශ භාෂාවෙන් ලියන ලද උපදේශනයක් සඳහා, ගොනුව `fr.md` ලෙස නම් කළ යුතුය.


සාරාංශයක් ලෙස, මෙන්න ගොනු අනුක්‍රමය (අපි ඊළඟ කොටසෙහි ඒවා නිර්මාණය කරගෙන යාමට පටන් ගන්නෙමු):


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - YAML ගොනුව පුරවන්න


ඉතින් YAML ගොනුවෙන් ආරම්භ කරමු. නව ගොනුවක් නිර්මාණය කිරීම සඳහා පෙට්ටිය තුළ `tutorial.yml` ඇතුළත් කරන්න :


![GITHUB](assets/fr/08.webp)


`tutorial.yml` දෝෂාත්මකව පිරවීමට පහත අච්චුය පිටපත් කරන්න:


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



- id** : UUID (_Universally Unique Identifier_) එකක් වන අතර එය උපකාරකය සුවිශේෂී ලෙස හඳුනාගනී. ඔබට [මාර්ගගත මෙවලමක්](https://www.uuidgenerator.net/version4) භාවිතයෙන් එය generate කළ හැක. එකම අවශ්‍යතාවය වන්නේ මෙම UUID එක අහඹු විය යුතු අතර වේදිකාවේ වෙනත් UUID සමඟ ගැටුම් වලක්වීමයි;



- project_id** : මෙහෙයුම් පසුබිම පිළිබඳව ඉදිරිපත් කරන ලද මෙවලමේ පසුපස ඇති සමාගම හෝ සංවිධානයේ UUID [ව්‍යාපෘති ලැයිස්තුවෙන්](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). උදාහරණයක් ලෙස, ඔබ Green Wallet මෘදුකාංගය පිළිබඳව උපකාරකයක් නිර්මාණය කරන්නේ නම්, මෙම `project_id` පහත ගොනුවේ සොයා ගත හැක: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. මෙම තොරතුරු ඔබේ උපකාරකයේ YAML ගොනුවට එක් කරනුයේ Plan ₿ Network විසින් Bitcoin හෝ සම්බන්ධ ව්‍යාපෘතිවල ක්‍රියාත්මක වන සියලු සමාගම් සහ සංවිධානවල දත්ත සමුදායක් පවත්වාගෙන යන බැවිනි. ඔබේ උපකාරකය සමඟ සම්බන්ධිත ඒකකයේ `project_id` එක එක් කිරීමෙන්, ඔබ Elements අතර සබැඳියක් නිර්මාණය කරයි;



- tags** : 2 හෝ 3 සම්බන්ධිත මූලපද, පමණක් [Plan ₿ Network ටැග ලැයිස්තුවෙන්](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) තෝරාගන්න;



- ප්‍රවර්ගය** : Plan ₿ Network වෙබ් අඩවියේ ව්‍යුහය අනුව උපකාරක අන්තර්ගතයට අදාළ උප-ප්‍රවර්ගය (උදාහරණයක් ලෙස, පසුම්බි සඳහා: `ඩෙස්ක්ටොප්`, `හාර්ඩ්වෙයාර්`, `ජංගම`, `උපස්ථ`);



- මට්ටම** : උපකාරක පඬියෙහි අපහසුතා මට්ටම, තෝරාගන්න:
    - `začetnik`
    - `අතුරු`
    - `ਉਨਤ`
    - `විශේෂඥ`



- professor_id** : ඔබේ `professor_id` (UUID) [ඔබේ මහාචාර්ය පැතිකඩ](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) මත පෙන්වා ඇති පරිදි;



- original_language** : උපදෙස් මාලාවේ මුල් භාෂාව (උදාහරණයක් ලෙස, `fr`, `en`, ආදිය);



- ප්‍රතිසංස්කරණය** : ප්‍රතිසංස්කරණ ක්‍රියාවලිය පිළිබඳ තොරතුරු. පළමු කොටස සම්පූර්ණ කරන්න, ඔබේම උපකාරකය ප්‍රතිසංස්කරණය කිරීම පළමු සත්‍යාපනයක් ලෙස ගණන් ගනී:
    - භාෂාව** : පරීක්ෂාකරණයේ භාෂා කේතය (උදාහරණයක් ලෙස, `fr`, `en`, ආදිය).
    - last_contribution_date** : දිනේ දිනය.
    - urgency** : 1
    - contributor_names** : Your GitHub ID.
    - ප්‍රසාදය** : 0


ඔබේ ගුරු හැඳුනුම්පත පිළිබඳ වැඩි විස්තර සඳහා, කරුණාකර අදාළ උපකාරකය වෙත යොමු වන්න :


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


Ko končate z urejanjem datoteke `tutorial.yml`, shranite dokument s klikom na gumb "*Commit changes...*":


![GITHUB](assets/fr/09.webp)


ශීර්ෂය සහ විස්තරයක් එක් කරන්න, සහ මෙම උපකාරක පඨයේ ආරම්භයේදී ඔබ නිර්මාණය කළ ශාඛාවට වගුව සිදු කරන බව සහතික කරන්න. එවිට "*Commit changes*" මත ක්ලික් කිරීමෙන් තහවුරු කරන්න.


![GITHUB](assets/fr/10.webp)


## 4 - छवियों के लिए उपफ़ोल्डर बनाना


කළින් "*Add File*" මත ක්ලික් කරන්න, එවිට "*Create new file*" මත ක්ලික් කරන්න :


![GITHUB](assets/fr/11.webp)


`assets` පසු `/` යොදා ෆෝල්ඩරය සාදන්න:


![GITHUB](assets/fr/12.webp)


මෙම පියවර `/assets` ෆෝල්ඩරය තුළ නැවත කරන්න භාෂා උපෆෝල්ඩරය නිර්මාණය කිරීමට, උදාහරණයක් ලෙස ඔබේ උපකාරකය ප්‍රංශ භාෂාවෙන් නම් `fr`:


![GITHUB](assets/fr/13.webp)


මෙම ෆෝල්ඩරය තුළ, GitHub ඔබේ ෆෝල්ඩරය (නැතහොත් හිස්ව පවතින) තබා ගැනීමට `.gitkeep` නමැති කාලීන ගොනුවක් සාදන්න. එවිට "*Commit changes...*" මත ක්ලික් කරන්න.


![GITHUB](assets/fr/14.webp)


ඔබ නිවැරදි ශාඛාවෙහි සිටින බව නැවත පරීක්ෂා කර, "*Commit changes*" මත ක්ලික් කරන්න.


![GITHUB](assets/fr/15.webp)


## 5 - Markdown දොසියාව සෑදීම


Zdaj bomo ustvarili datoteko, ki bo gostila vaš vadnico, poimenovano v skladu z vašo jezikovno kodo, na primer `fr.md`, če pišemo v francoščini. Pojdite v mapo z vašo vadnico:


![GITHUB](assets/fr/16.webp)


කොටස "Add file*" මත ක්ලික් කරන්න, එවිට "Create new file*" මත ක්ලික් කරන්න.


![GITHUB](assets/fr/17.webp)


Poimenujte datoteko z vašo jezikovno kodo. V mojem primeru, ker je vadnica napisana v francoščini, poimenujem svojo datoteko `fr.md`. Pripona `.md` označuje, da je datoteka v formatu Markdown.


![GITHUB](assets/fr/18.webp)


අපි ලේඛනයේ ඉහළින් ඇති `Properties` කොටස පුරවා ආරම්භ කරමු. පහත කේත කොටස අතින් එක් කර පුරවන්න (`name:` සහ `description:` යතුරු ඉංග්‍රීසි භාෂාවෙන් තබා ගත යුතු නමුත් ඒවායේ අගයන් ඔබේ උපකාරකය සඳහා භාවිතා කරන භාෂාවෙන් ලියිය යුතුය):


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


Izpolnite ime vašega vadnice in kratek opis:


![GITHUB](assets/fr/20.webp)


nato dodajte pot do naslovne slike na začetku vašega vodiča. To storite tako, da upoštevate:


```
![cover-green](assets/cover.webp)
```


මෙම වාක්‍ය ව්‍යුහය ඔබේ උපකාරකයට රූපයක් එක් කිරීමට අවශ්‍ය වන විට ප්‍රයෝජනවත් වනු ඇත. විශ්මය ලකුණක් රූපයක් සලකුණු කරයි, එහි විකල්ප පෙළ (alt) වර්ග කොටුව තුළ සඳහන් වේ. රූපය වෙත මාර්ගය කොටුව තුළ සඳහන් වේ:


![GITHUB](assets/fr/21.webp)


මෙම ගොනුව සුරකින්න "*Commit changes...*" බොත්තම මත ක්ලික් කරන්න.


![GITHUB](assets/fr/22.webp)


ඔබ නිවැරදි ශාඛාවෙහි සිටින බව පරීක්ෂා කර, commit එක තහවුරු කරන්න.


![GITHUB](assets/fr/23.webp)


ඔබේ භාෂා කේතය අනුව ඔබේ උපකාරක ෆෝල්ඩරය දැන් මෙසේ පෙනිය යුතුය:


![GITHUB](assets/fr/24.webp)


## 6 - ලාංඡනය සහ ආවරණය එක් කරන්න


`assets` ෆෝල්ඩරය තුළ, ඔබට `logo.webp` නම් කරන ලද ගොනුවක් එක් කිරීමට අවශ්‍ය වන අතර, එය ඔබේ ලිපිය සඳහා කෙටි රූපයක් ලෙස සේවය කරනු ඇත. මෙම රූපය `.webp` ආකෘතියෙන් විය යුතු අතර, පරිශීලක Interface සමඟ ගැලපෙන පරිදි චතුරස්‍ර වශයෙන් විය යුතුය.


ඔබට අධ්‍යාපනික මාර්ගෝපදේශයේ භාවිතා කරන මෘදුකාංග ලාංඡනය, හෝ වෙනත් සම්බන්ධිත රූපයක්, රජයේ බලපත්‍ර නොමැති නම් තෝරා ගත හැක. අමතරව, `cover.webp` නමින් රූපයක් එකම ස්ථානයේ එක් කරන්න. මෙය ඔබේ මාර්ගෝපදේශයේ ඉහළින් ප්‍රදර්ශනය කෙරේ. මෙම රූපය, ලාංඡනය මෙන්ම, භාවිතා කිරීමේ අයිතිවාසිකම් ගරු කරන අතර ඔබේ මාර්ගෝපදේශයේ පරිපූර්ණතාවයට සුදුසු විය යුතුය.


ඔබේ දේශීය ගොනු වලින් රූප එකතු කිරීමට `/assets` ෆෝල්ඩරයට, ඒවා ඇදගෙන යා හැක. ඔබ `/assets` ෆෝල්ඩරය තුළ සහ නිවැරදි ශාඛාවෙහි සිටින බව සහතික කරගෙන, "*Commit changes*" මත ක්ලික් කරන්න.


![GITHUB](assets/fr/26.webp)


ඔබ දැන් ඡායාරූප ෆෝල්ඩරය තුළ පෙනෙන බව දැකිය යුතුය.


![GITHUB](assets/fr/27.webp)


## 7 - ट्यूटोरियल लेखन


ඔබේ උපකාරකය ලියන්න දිගටම `fr.md` ගොනුවේ භාෂා කේතය සමඟ Markdown ගොනුවේ ඔබේ අන්තර්ගතය සටහන් කරමින්. ගොනුවට ගොස් පෑන අයිකනය මත ක්ලික් කරන්න :


![GITHUB](assets/fr/28.webp)


ඔබේ උපදෙස් ලියන්න ආරම්භ කරන්න. උපශීර්ෂකයක් එක් කරන විට, `##` යන පෙරනිමිය භාවිතා කරමින් නිවැරදි Markdown ආකෘතිය භාවිතා කරන්න:


![GITHUB](assets/fr/29.webp)


"*"සංස්කරණය*" සහ "*"පෙරදසුන*" දසුන් අතර විකල්ප වන්න rendering හොඳින් දෘශ්‍යමය කිරීමට."


![GITHUB](assets/fr/30.webp)


ඔබේ කාර්යය සුරකින්න, "*Commit Changes...*" මත ක්ලික් කරන්න, ඔබ නිවැරදි ශාඛාවෙහි සිටින බව සහතික කරගෙන, පසුව නැවත "*Commit Changes*" මත ක්ලික් කිරීමෙන් තහවුරු කරන්න.


![GITHUB](assets/fr/31.webp)


## 8 - දෘශ්‍යයන් එක් කරන්න


`/assets` ෆෝල්ඩරයේ භාෂා උපෆෝල්ඩරය (මගේ උදාහරණයේ: `/assets/en`) ඔබේ උපකාරක පෙළට අමතරව රූප සටහන් සහ දෘශ්‍යයන් ගබඩා කිරීමට භාවිතා වේ. හැකි තාක්, ඔබේ අන්තර්ගතය ජාත්‍යන්තර පිරිසකට ප්‍රවේශ විය හැකි වන පරිදි ඔබේ රූපවල පෙළ ඇතුළත් කිරීමෙන් වළකින්න. නිකම්ම, ඉදිරිපත් කරන ලද මෘදුකාංගය පෙළ අඩංගු වනු ඇත, නමුත් ඔබ මෘදුකාංග තිර රූපවල රූප සටහන් හෝ අමතර සංකේත ඇතුළත් කරනවා නම්, පෙළ නොමැතිව හෝ, අත්‍යවශ්‍ය නම්, ඉංග්‍රීසි භාවිතා කරන්න.


ඔබේ රූප නම් කිරීමට, සරලවම ඒවා පෙනී සිටින අනුපිළිවෙලට අනුකූලව සංඛ්‍යා භාවිතා කරන්න, ඒවා දෙකේ ඉලක්කම් ලෙස (හෝ ඔබේ උපදේශනයේ රූප 99 කට වඩා අඩංගු නම් තුනේ ඉලක්කම් ලෙස) ආකෘතිගත කර ඇත. උදාහරණයක් ලෙස, ඔබේ පළමු රූපය `01.webp`, දෙවන රූපය `02.webp`, එසේම ඉදිරියට නම් කරන්න.


ඔබේ රූප `.webp` ආකෘතියෙන් පමණක් විය යුතුය. අවශ්‍ය නම්, ඔබට [මගේ රූප පරිවර්තන මෘදුකාංගය](https://github.com/LoicPandul/ImagesConverter) භාවිතා කළ හැක.


![GITHUB](assets/fr/32.webp)


Zdaj, ko ste dodali svoje slike v podmapo, lahko izbrišete navidezno datoteko `.gitkeep`. Odprite to datoteko, kliknite na tri majhne pike v zgornjem desnem kotu, nato na "*Delete file*".


![GITHUB](assets/fr/33.webp)


ඔබේ වෙනස්කම් "*Commit changes...*" මත ක්ලික් කිරීමෙන් සුරකින්න.


![GITHUB](assets/fr/34.webp)


Če želite vstaviti diagram iz svoje podmape v svoj uredniški dokument, uporabite naslednji ukaz Markdown, pri čemer pazite, da navedete ustrezno nadomestno besedilo in pravilno pot slike za svoj jezik:


```
![green](assets/fr/01.webp)
```


Začetni klicaj označuje sliko. Nadomestno besedilo, ki pomaga pri dostopnosti in referenciranju, je postavljeno med oglate oklepaje. Na koncu je pot do slike navedena med oklepaji.


![GITHUB](assets/fr/35.webp)


Če želite ustvariti svoje lastne sheme, se prepričajte, da upoštevate grafične smernice Plan ₿ Network za zagotovitev vizualne doslednosti:




- Font**: Use [Rubik](https://fonts.google.com/specimen/Rubik);
- Colours** :
 - Orange: #FF5C00
 - Črna : #000000
 - සුදු: #FFFFFF


**ඔබේ උපකාරක පඬිවලට ඒකාබද්ධ කරන සියලු දෘශ්‍ය පටවල් මූලාශ්‍ර ගොනුවේ බලපත්‍රය ගරු කරන හෝ මූල්‍ය අයිතියෙන් තොර විය යුතුය**. එබැවින්, Plan ₿ Network හි ප්‍රකාශිත සියලු ආරේඛන CC-BY-SA බලපත්‍රයක් යටතේ ලබා දී ඇති අතර, පෙළ මෙන්ම.


**-> උපදෙස්:** රූප වැනි ගොනු මහජනතාව සමඟ බෙදා ගැනීමේදී, අතිරේක මेटා දත්ත ඉවත් කිරීම වැදගත් වේ. මෙය ස්ථානයේ දත්ත, නිර්මාණ දිනයන් සහ කතෘ විස්තර වැනි සංවේදී තොරතුරු අඩංගු විය හැක. ඔබේ පෞද්ගලිකත්වය ආරක්ෂා කිරීම සඳහා, මෙම මेटා දත්ත ඉවත් කිරීම හොඳ අදහසකි. මෙම මෙහෙයුම සරල කිරීම සඳහා, [Exif Cleaner](https://exifcleaner.com/) වැනි විශේෂිත මෙවලම් භාවිතා කළ හැකි අතර, එය සරල ඇදීම සහ අත්හැරීමකින් ලේඛනයක මेटා දත්ත පිරිසිදු කිරීමට ඔබට හැකියාව ලබා දෙයි.


## 9 - උපදේශනය යෝජනා කරන්න


ඔබේ උපදේශකය ඔබ කැමති භාෂාවෙන් ලිවීම අවසන් වූ විට, ඊළඟ පියවර වන්නේ **Pull Request** එකක් ඉදිරිපත් කිරීමයි. පරිපාලකයා පසුව ඔබේ උපදේශකයට අතපසුවී ඇති පරිවර්තන එකතු කරනු ඇත, අපගේ ස්වයංක්‍රීය පරිවර්තන ක්‍රමය මිනිස් පරීක්ෂාකරණය සමඟ භාවිතා කරමින්.


Pull Request සමඟ ඉදිරියට යාම සඳහා, ඔබේ සියලු වෙනස්කම් සුරක්ෂිත කිරීමෙන් පසු, "*Contribute*" බොත්තම මත ක්ලික් කරන්න, එවිට "*Open pull request*" මත ක්ලික් කරන්න :


![GITHUB](assets/fr/36.webp)


Pull Request යනු Plan ₿ Network ගබඩාශාලාවේ ප්‍රධාන ශාඛාවට ඔබේ ශාඛාවෙන් වෙනස්කම් ඒකාබද්ධ කිරීමට කරන ඉල්ලීමක් වන අතර, ඒවා ඒකාබද්ධ කිරීමට පෙර වෙනස්කම් සමාලෝචනය කිරීම සහ සාකච්ඡා කිරීම සඳහා අවස්ථාව ලබා දේ.


මීට පෙර, Interface හි පහළින් මෙම වෙනස්කම් ඔබ අපේක්ෂා කළ දේවල් බවට විශේෂයෙන්ම සැලකිල්ලෙන් පරීක්ෂා කරන්න:


![GITHUB](assets/fr/37.webp)


සහතික වන්න, Interface හි ඉහළින්, ඔබේ වැඩ කරන ශාඛාව Plan ₿ Network ගබඩාවේ `dev` ශාඛාව (ප්‍රධාන ශාඛාව වන) වෙත ඒකාබද්ධ කර ඇති බව.


ඔබගේ වෙනස්කම් මූලාශ්‍ර ගබඩාව සමඟ ඒකාබද්ධ කිරීමට කැමති බව සාරාංශ ගත කරන මාතෘකාවක් ඇතුළත් කරන්න. මෙම වෙනස්කම් විස්තර කරන කෙටි අදහසක් එක් කරන්න (ඔබේ උපකාරකය නිර්මාණය කිරීම සමඟ සම්බන්ධිත ගැටලුවක් ඇත්නම්, `Closes #{issue number}` ලෙස අදහසක් ලෙස සටහන් කිරීමට මතක තබා ගන්න), එවිට Green "*Create pull request*" බොත්තම ක්ලික් කර ඒකාබද්ධ කිරීමේ ඉල්ලීම තහවුරු කරන්න:


![GITHUB](assets/fr/38.webp)


ඔබගේ PR පසුව Plan ₿ Network ප්‍රධාන ගබඩායේ "*Pull Request*" ටැබ් හි දෘශ්‍යමාන වනු ඇත. දැන් ඔබ කළ යුත්තේ පරිපාලකයෙකු ඔබව සම්බන්ධ කරගෙන ඔබගේ දායකත්වය ඒකාබද්ධ කර ඇති බව තහවුරු කරන තුරු හෝ අමතර වෙනස්කම් කිසිවක් ඉල්ලා සිටින තුරු රැඳී සිටීම පමණි.


![GITHUB](assets/fr/39.webp)


ඔබේ PR ප්‍රධාන ශාඛාව සමඟ ඒකාබද්ධ කිරීමෙන් පසු, ඔබේ කාර්ය ශාඛාව මකා දැමීම නිර්දේශ කරමු (මගේ උදාහරණයේ: `tuto-Green-Wallet`) ඔබේ Fork හි පිරිසිදු ඉතිහාසයක් පවත්වා ගැනීමට. GitHub ඔබට මෙම විකල්පය ස්වයංක්‍රීයව ඔබේ PR පිටුවේදී ලබා දෙනු ඇත:


![GITHUB](assets/fr/40.webp)


ඔබේ දායකත්වය PR එකක් ලෙස ඉදිරිපත් කිරීමෙන් පසු වෙනස්කම් කිරීමට කැමති නම්, ඔබේ PR එකේ වර්තමාන තත්ත්වය මත පියවර අනුගමනය කළ යුතුය:




- ඔබගේ PR තවමත් විවෘතව ඇති අතර ඒක එකතු කර නොමැති නම්, ඒම වැඩ ශාඛාවේම වෙනස්කම් කරන්න. කමිටු වෙනස්කම් ඔබගේ තවමත් විවෘත PR එකට එකතු කරනු ලැබේ;
- ඔබේ PR දැනටමත් ප්‍රධාන ශාඛාව සමඟ ඒකාබද්ධ කර ඇති අවස්ථාවක, ඔබට නව ශාඛාවක් නිර්මාණය කිරීමෙන් ආරම්භයෙන්ම ක්‍රියාවලිය නැවත කිරීමට අවශ්‍ය වේ, එවිට නව PR එකක් ඉදිරිපත් කරන්න. ඔබේ Fork, Plan ₿ Network මූලාශ්‍ර ගබඩාවේ `dev` ශාඛාව සමඟ සමානුකූලීකරණය වී ඇති බවට වග බලා ගන්න.


ඔබේ උපකාරකය ඉදිරිපත් කිරීමේදී තාක්ෂණික අපහසුතා ඇතිවන්නේ නම්, කරුණාකර [අපගේ දායකත්ව සඳහා කැපවූ ටෙලිග්‍රෑම් කණ්ඩායම](https://t.me/PlanBNetwork_ContentBuilder) මගින් උපකාර ඉල්ලා සිටීමට කමක් නොමැත. බොහෝම ස්තුතියි!