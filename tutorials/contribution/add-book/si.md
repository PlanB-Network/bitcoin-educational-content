---
name: PlanB Network-ට පොතක් එකතු කිරීම
description: PlanB ජාලයට නව පොතක් එක් කිරීමට කෙසේද?
---
![book](assets/cover.webp)


PlanBගේ මෙහෙවර වන්නේ Bitcoin පිළිබඳ ඉහළම තත්ත්වයේ අධ්‍යාපනික සම්පත් හැකි ඉක්මනින් බොහෝ භාෂාවන්වලින් ලබා දීමයි. අඩවියෙහි ප්‍රකාශිත සියලුම අන්තර්ගතය විවෘත මූලාශ්‍ර සහ GitHub හි සත්කාරක වන අතර, කවුරුන්ට හෝ වේදිකාවේ සම්පත් වර්ධනයට දායක විය හැක.


**ඔබගේ කෘතියේ දෘශ්‍යතාවය වැඩි දියුණු කරමින් PlanB ජාලය වෙබ් අඩවියට Bitcoin සම්බන්ධ පොතක් එක් කිරීමට අවශ්‍යද, නමුත් කෙසේදැයි නොදන්නවාද? මෙම උපකාරිකාව ඔබ සඳහායි!**

![book](assets/01.webp)


- පළමුව, ඔබට GitHub ගිණුමක් තිබිය යුතුය. ඔබට ගිණුමක් නිර්මාණය කරන ආකාරය නොදන්නා නම්, අපි ඔබට මාර්ගෝපදේශ කිරීම සඳහා විස්තරාත්මක උපකාරක පථයක් සකසා ඇත.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- [GitHub හි PlanB වෙත විශේෂිත දත්ත සඳහා ඇති ගබඩාවට යන්න](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) `resources/books/` කොටසෙහි:

![book](assets/02.webp)


- ඉහළ දකුණේ ඇති `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත ක්ලික් කරන්න:

![book](assets/03.webp)


- ඔබ PlanB ජාලයේ අන්තර්ගතයට පෙර කිසිදු දායකත්වයක් ලබා දී නැත්නම්, ඔබට මුල් ගබඩාවේ ඔබේ Fork නිර්මාණය කළ යුතුය. ගබඩාවක් Fork කිරීම යනු, ඔබේම GitHub ගිණුමේ එම ගබඩාවේ පිටපතක් නිර්මාණය කිරීමයි, එය ඔබට මුල් ගබඩාවට බලපෑමකින් තොරව ව්‍යාපෘතියේ වැඩ කිරීමට ඉඩ සලසයි. `Fork this repository` බොත්තම ක්ලික් කරන්න:

![book](assets/04.webp)


- ඔබ එවිට GitHub සංස්කරණ පිටුවට පැමිණෙනු ඇත:

![book](assets/05.webp)


- ඔබේ පොත සඳහා ෆෝල්ඩරයක් සාදන්න. ایسا کرنے کے لیے، `Name your file...` කොටුවේ, ඔබේ පොතේ නම කුඩා අකුරින් සහ ඉරක් (dashes) භාවිතා කරමින් ලියන්න. උදාහරණයක් ලෙස, ඔබේ පොත "*My Bitcoin Book*" නම් නම්, ඔබ `my-Bitcoin-book` ලෙස සටහන් කළ යුතුය:

![book](assets/06.webp)


- ඔබේ පොතේ නමට පසු සලකුණක් එකතු කිරීමෙන්, නව ෆෝල්ඩරයක් නිර්මාණය වීම සනාථ කිරීමට, එම පෙට්ටිය තුළ, උදාහරණයක් ලෙස: `my-Bitcoin-book/`. සලකුණක් එකතු කිරීමෙන් ස්වයංක්‍රීයව ෆෝල්ඩරයක් නිර්මාණය වේ, ගොනුවක් වෙනුවට:

![book](assets/07.webp)


- මෙම ෆෝල්ඩරය තුළ, ඔබ `book.yml` නම් පළමු YAML ගොනුවක් සාදනු ඇත:

![book](assets/08.webp)


- Izpolnite to datoteko z informacijami o vaši knjigi z uporabo te predloge:


```yaml
author:
level:
tags:
-
-
```


මෙන්න එක් එක් ක්ෂේත්‍රය සඳහා පුරවිය යුතු විස්තර:


- `ලේඛකයා`**: පොතේ ලේඛකයාගේ නම සදහන් කරන්න.
- `level`**: පොත හොඳින් කියවීමට සහ තේරුම් ගැනීමට අවශ්‍ය මට්ටම සදහන් කරන්න. පහත මට්ටම් අතරින් මට්ටමක් තෝරන්න:
 - `začetnik`
 - `අතරමැදි`
- `උසස්` - `විශේෂඥ`
- `tags`**: ඔබේ පොතට සම්බන්ධිත ටැග් දෙකක් හෝ තුනක් එක් කරන්න. උදාහරණයක් ලෙස:
    - `Bitcoin`
    - `zgodovina`
    - `teknologija`
    - `ekonomija`
    - `අධ්‍යාපන`...


उदाहरण के लिए, आपका YAML फ़ाइल इस प्रकार दिख सकता है:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- මෙම ගොනුවට වෙනස්කම් කිරීම අවසන් වූ විට, `Commit changes...` බොත්තම ක්ලික් කිරීමෙන් ඒවා සුරකින්න:

![book](assets/10.webp)


- Dodajte naslov za vaše spremembe in kratek opis:

![book](assets/11.webp)


- Green `ප්‍රතිසංස්කරණ යෝජනා කරන්න` බොත්තම මත ක්ලික් කරන්න:

![book](assets/12.webp)


- ඔබේ සියලු වෙනස්කම් සාරාංශගත කරන පිටුවකට පසුව එන්න:

![book](assets/13.webp)


- GitHub प्रोफ़ाइल चित्र पर ऊपर दाईं ओर क्लिक करें, फिर `Your Repositories` पर:

![book](assets/14.webp)


- ඔබේ Fork PlanB ජාලය ගබඩාවේ තෝරන්න:

![book](assets/15.webp)


- ඔබේ නව ශාඛාව සමඟ කවුළුවේ ඉහළින් දැනුම්දීමක් ඔබට දැකිය යුතුය. එය `patch-1` ලෙස නම් කර ඇති බවක් සම්භාවිතයි. එය ක්ලික් කරන්න:

![book](assets/16.webp)


- You are now on your working branch:

![book](assets/17.webp)


- `resources/books/` ෆෝල්ඩරයට ආපසු ගොස්, ඔබ පෙර කමිටුවේදී නිර්මාණය කළ ඔබේ පොතේ ෆෝල්ඩරය තෝරන්න:

![book](assets/18.webp)


- ඔබේ පොතේ ෆෝල්ඩරය තුළ, `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත:

![book](assets/19.webp)


- To poimenujte novo mapo `assets` in potrdite njeno ustvarjanje z dodajanjem poševnice `/` na koncu:

![book](assets/20.webp)


- V tej mapi `assets` ustvarite datoteko z imenom `.gitkeep`:

![book](assets/21.webp)


- `Commit changes...` බොත්තම මත ක්ලික් කරන්න:

![book](assets/22.webp)


- Pustite naslov potrditve kot privzet, in se prepričajte, da je polje `Commit directly to the patch-1 branch` označeno, nato kliknite na `Commit changes`:

![book](assets/23.webp)


- `assets` ෆෝල්ඩරයට ආපසු යන්න:

![book](assets/24.webp)


- `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Upload files` මත:

![book](assets/25.webp)


- නව පිටුවක් විවෘත වේවි. ඔබේ පොතේ ආවරණ රූපය එම ප්‍රදේශයට ඇදගෙන යන්න. මෙම රූපය PlanB ජාලය වෙබ් අඩවියේ පෙන්වනු ලැබේ:

![book](assets/26.webp)


- සැලකිලිමත් වන්න, රූපය පොතක ආකෘතියෙන් විය යුතුය, අපගේ වෙබ් අඩවියට හොඳින් අනුකූල වීමට, උදාහරණයක් ලෙස:

![book](assets/27.webp)


- රූපය උඩුගත කිරීමෙන් පසු, `Commit directly to the patch-1 branch` කොටුව සලකුණු කර ඇති බව සහතික කර, පසුව `Commit changes` මත ක්ලික් කරන්න:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- මීට පසු ඔබේ `assets` ෆෝල්ඩරයට ආපසු ගොස් `.gitkeep` මැදිහත් ගොනුව මත ක්ලික් කරන්න:

![book](assets/30.webp)


- ගොනුව මත එක් වරක් ක්ලික් කිරීමෙන්, ඉහළ දකුණු කෙළවරේ ඇති කුඩා ලප 3 මත ක්ලික් කර, පසුව `ගොනුව මකන්න` මත ක්ලික් කරන්න:

![book](assets/31.webp)


- ඒකම වැඩ කරන ශාඛාවෙම තවමත් සිටින බව සහතික කර, පසුව `Commit changes...` බොත්තම මත ක්ලික් කරන්න:

![book](assets/32.webp)


- ඔබේ කමිටුවට ශීර්ෂයක් සහ විස්තරයක් එක් කරන්න, එවිට `Commit changes` මත ක්ලික් කරන්න:

![book](assets/33.webp)


- ඔබේ පොතේ ෆෝල්ඩරයට ආපසු යන්න:

![book](assets/34.webp)


- `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත ක්ලික් කරන්න:

![book](assets/35.webp)


- පොතේ විස්තරය සඳහා භාවිතා කිරීමට, පොතේ භාෂා සංකේතය සමඟ නමකරණය කර නව YAML ගොනුවක් සාදන්න. උදාහරණයක් ලෙස, මම මගේ විස්තරය ඉංග්‍රීසි භාෂාවෙන් ලිවීමට අවශ්‍ය නම්, මම මෙම ගොනුව `en.yml` ලෙස නම් කරමි:

![book](assets/36.webp)


- මීළඟ YAML ගොනුව මෙම අච්චු ආකෘතිය භාවිතයෙන් පුරවන්න:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


මෙම ක්ෂේත්‍රය සඳහා පුරවිය යුතු විස්තර මෙන්න:


- `title`**: පොතේ නම උද්ධෘත ලකුණු තුළ සදහන් කරන්න.
- `publication_year`**: පොත මුද්‍රණය වූ වර්ෂය සදහන් කරන්න.
- `cover`**: ඔබ මේ වන විට සංස්කරණය කරමින් සිටින YAML ගොනුවේ භාෂාවට අනුකූලව, ආවරණ රූපයට අදාළ ගොනුවේ නම සදහන් කරන්න. උදාහරණයක් ලෙස, ඔබ `en.yml` ගොනුව සංස්කරණය කරමින් සිටින අතර, ඔබ පෙර ඇතුළත් කළ ඉංග්‍රීසි ආවරණ රූපය `cover_en.webp` නම් නම්, මෙම ක්ෂේත්‍රයේ `cover_en.webp` ලෙස සදහන් කරන්න.
- `description`**: පොත පිළිබඳ කෙටි වාක්‍යයක් එක් කරන්න. විස්තරය YAML ගොනුවේ මාතෘකාවෙන් සදහන් භාෂාවෙන්ම විය යුතුය.
- `contributors`**: Če imate ID sodelavca, ga dodajte.


උදාහරණයක් ලෙස, ඔබේ YAML ගොනුව මෙසේ පෙනෙන්නට පුළුවන්:


```yaml