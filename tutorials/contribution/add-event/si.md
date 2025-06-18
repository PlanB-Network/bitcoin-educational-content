---
name: Načrtujte dogodek na PlanB Network
description: How do I suggest adding a new event on PlanB Network?
---
![event](assets/cover.webp)


PlanBගේ මෙහෙවර වන්නේ Bitcoin පිළිබඳ ඉහළම තත්ත්වයේ අධ්‍යාපනික සම්පත් හැකි ඉක්මනින් බොහෝ භාෂාවන්වලින් ලබා දීමයි. අඩවිය මත ප්‍රකාශිත සියලුම අන්තර්ගතය විවෘත මූලාශ්‍ර සහ GitHub මත සත්කාරක කර ඇති අතර, වේදිකාවේ සම්පත් වර්ධනයට කවුරුන් හෝ දායක විය හැක.


Če želite dodati konferenco Bitcoin na spletno mesto PlanB Network in povečati vidnost svojega dogodka, vendar ne veste kako? Ta vadnica je za vas!

![event](assets/01.webp)


- පළමුව, ඔබට GitHub හි ගිණුමක් තිබිය යුතුය. ඔබට ගිණුමක් නිර්මාණය කරන ආකාරය නොදන්නා නම්, අපි ඔබට මාර්ගෝපදේශ කිරීමට විස්තරාත්මක උපකාරක පඬික්කමක් සකසා ඇත.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Pojdite na [GitHub repozitorij PlanB, namenjen podatkom](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) v razdelku `resources/conference/`:

![event](assets/02.webp)


- ඉහළ දකුණේ ඇති `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත ක්ලික් කරන්න:

![event](assets/03.webp)


- ඔබ PlanB ජාලයේ අන්තර්ගතයට පෙර කිසිදු දායකත්වයක් ලබා දී නොමැති නම්, ඔබට මුල් ගබඩාකරණයේ ඔබේ Fork නිර්මාණය කළ යුතුය. ගබඩාකරණයක් Fork කිරීම යනු, ඔබේම GitHub ගිණුමේ එම ගබඩාකරණයේ පිටපතක් නිර්මාණය කිරීමයි, එය ඔබට මුල් ගබඩාකරණයට බලපෑමකින් තොරව ව්‍යාපෘතියේ වැඩ කිරීමට ඉඩ සලසයි. `Fork this repository` බොත්තම ක්ලික් කරන්න:

![event](assets/04.webp)


- ඔබ එවිට GitHub සංස්කරණ පිටුවට පැමිණෙනු ඇත:

![event](assets/05.webp)


- ඔබේ සමුළුව සඳහා ෆෝල්ඩරයක් සාදන්න. මෙය කිරීමට, `ඔබේ ගොනුව නමක් දෙන්න...` කොටුවේ, ඔබේ සමුළුවේ නම කුඩා අකුරින් සහ ඉරක් (dashes) භාවිතයෙන් ලියන්න. උදාහරණයක් ලෙස, ඔබේ සමුළුව "Paris Bitcoin Conference" නම් නම්, ඔබ `paris-Bitcoin-conference` ලෙස සටහන් කළ යුතුය. එමෙන්ම ඔබේ සමුළුවේ වසරද එක් කරන්න, උදාහරණයක් ලෙස: `paris-Bitcoin-conference-2024`:

![event](assets/06.webp)


- ෆෝල්ඩරය නිර්මාණය කිරීම සනාථ කිරීමට, එමම පෙට්ටිය තුළ ඔබේ නමට පසු සළකුණක් සටහන් කරන්න, උදාහරණයක් ලෙස: `paris-Bitcoin-conference-2024/`. සළකුණක් එක් කිරීමෙන් ස්වයංක්‍රීයව ගොනුවක් වෙනුවට ෆෝල්ඩරයක් නිර්මාණය වේ:

![event](assets/07.webp)


- මෙම ෆෝල්ඩරය තුළ, ඔබ `events.yml` නම් පළමු YAML ගොනුවක් සාදනු ඇත:

![event](assets/08.webp)


- Izpolnite to datoteko z informacijami o vaši konferenci z uporabo te predloge:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
builder:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


उदाहरण के लिए, आपका YAML फ़ाइल इस प्रकार दिख सकता है:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

ඔබේ සංවිධානය සඳහා "*builder*" හඳුනාගැනීමක් තවමත් නොමැති නම්, ඔබට එය මෙම වෙනත් උපකාරකය අනුගමනය කිරීමෙන් එක් කළ හැක.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- මෙම ගොනුවට වෙනස්කම් කිරීම අවසන් වූ විට, `Commit changes...` බොත්තම ක්ලික් කිරීමෙන් ඒවා සුරකින්න:

![event](assets/10.webp)


- Dodajte naslov za svoje spremembe in kratek opis:

![event](assets/11.webp)


- Green `ප්‍රතිසංස්කරණ යෝජනා කරන්න` බොත්තම මත ක්ලික් කරන්න:

![event](assets/12.webp)


- එවිට ඔබේ සියලු වෙනස්කම් සාරාංශ ගත කරන පිටුවකට ඔබ පැමිණෙනු ඇත:

![event](assets/13.webp)


- GitHub प्रोफ़ाइल चित्र पर ऊपर दाईं ओर क्लिक करें, फिर `Your Repositories` पर:

![event](assets/14.webp)


- ඔබේ Fork PlanB ජාලක ගබඩාකරණය තෝරන්න:

![event](assets/15.webp)


- ඔබේ නව ශාඛාව සමඟ කවුළුවේ ඉහළින් දැනුම්දීමක් ඔබට දැකිය යුතුය. එය `patch-1` ලෙස නම් කර ඇති බවක් සම්භාව්‍යව පෙනේ. එය ක්ලික් කරන්න:

![event](assets/16.webp)


- Zdaj ste na svoji delovni veji:

![event](assets/17.webp)


- `resources/conference/` ෆෝල්ඩරයට ආපසු ගොස්, ඔබ පෙර කමිටුවේදී නිර්මාණය කළ ඔබේ සම්මන්ත්‍රණයේ ෆෝල්ඩරය තෝරන්න:

![event](assets/18.webp)


- ඔබේ සම්මන්ත්‍රණයේ ෆෝල්ඩරය තුළ, `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත:

![event](assets/19.webp)


- මෙම නව ෆෝල්ඩරය `assets` ලෙස නම් කර එය නිර්මාණය වූ බව `/` එකක් අගට තබා තහවුරු කරන්න:

![event](assets/20.webp)


- මෙම `assets` ෆෝල්ඩරය තුළ `.gitkeep` නම් ගොනුවක් සාදන්න:

![event](assets/21.webp)


- `Commit changes...` බොත්තම මත ක්ලික් කරන්න:

![event](assets/22.webp)


- කමිටු මාතෘකාව පෙරනිමි ලෙස තබා, `Commit directly to the patch-1 branch` කොටුව සලකුණු කර ඇති බවට වග බලා ගන්න, එවිට `Commit changes` මත ක්ලික් කරන්න:

![event](assets/23.webp)


- `assets` ෆෝල්ඩරයට ආපසු යන්න:

![event](assets/24.webp)


- `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Upload files` මත ක්ලික් කරන්න: ![event](assets/25.webp)
- නව පිටුවක් විවෘත වේ. ඔබේ සම්මන්ත්‍රණය නිරූපණය කරන සහ PlanB ජාලය වෙබ් අඩවියේ පෙන්වනු ලබන රූපයක් ඇදගෙන යා යුතුය:

![event](assets/26.webp)


- එය ලාංඡනයක්, කුඩා රූපයක්, හෝ පෝස්ටරයක් විය හැක:

![event](assets/27.webp)


- රූපය උඩුගත කිරීමෙන් පසු, `Commit directly to the patch-1 branch` කොටුව ටික් කර ඇති බව පරීක්ෂා කරන්න, එවිට `Commit changes` මත ක්ලික් කරන්න:

![event](assets/28.webp)


- සැලකිලිමත් වන්න, ඔබේ රූපය `thumbnail` ලෙස නම් කළ යුතු අතර `.webp` ආකෘතියෙන් විය යුතුය. එබැවින් සම්පූර්ණ ගොනු නාමය විය යුතුය: `thumbnail.webp`:

![event](assets/29.webp)


- ඔබේ `assets` ෆෝල්ඩරයට ආපසු ගොස් මැදිහත් ගොනුව `.gitkeep` මත ක්ලික් කරන්න:

![event](assets/30.webp)


- Datoteko odprite in kliknite na 3 majhne pike v zgornjem desnem kotu, nato na `Izbriši datoteko`:

![event](assets/31.webp)


- තහවුරු කරන්න ඔබ තවමත් ඒම වැඩ කරන ශාඛාවේ සිටිනවාද, එවිට `Commit changes` බොත්තම ක්ලික් කරන්න:

![event](assets/32.webp)


- ඔබේ කැමට්ට ශීර්ෂයක් සහ විස්තරයක් එක් කරන්න, එවිට `Commit changes` මත ක්ලික් කරන්න:

![event](assets/33.webp)


- ඔබේ ගබඩාවේ මූලිකයට ආපසු යන්න:

![event](assets/34.webp)


- ඔබේ ශාඛාව වෙනස් වී ඇති බව පෙන්වන පණිවිඩයක් ඔබට දැකිය යුතුය. `Compare & pull request` බොත්තම ක්ලික් කරන්න:

![event](assets/35.webp)


- PR සඳහා පැහැදිලි මාතෘකාවක් සහ විස්තරයක් එක් කරන්න:

![event](assets/36.webp)


- Kliknite na gumb `Create pull request`:

![event](assets/37.webp)

සුභ පැතුම්! ඔබේ PR සාර්ථකව නිර්මාණය කර ඇත. දැන් පරිපාලකයෙකු එය පරීක්ෂා කරනු ඇත, සහ සියල්ල සරියට ඇති නම්, එය PlanB ජාලයේ ප්‍රධාන ගබඩාවට ඒකාබද්ධ කරනු ඇත. ඔබේ සිදුවීම දින කිහිපයකට පසු වෙබ් අඩවියේ පෙනෙනු ඇත.


ඔබේ PR හි ප්‍රගතිය අනිවාර්යයෙන්ම අනුගමනය කරන්න. පරිපාලකයෙකු අමතර තොරතුරු ඉල්ලා අදහසක් තැබිය හැක. ඔබේ PR වලංගු නොවන තෙක්, ඔබට එය PlanB Network GitHub ගබඩාවේ `Pull requests` ටැබ් එකේදී පරීක්ෂා කළ හැක:

![event](assets/38.webp)

ඔබේ වටිනා දායකත්වය සඳහා බොහෝම ස්තූතියි! :)