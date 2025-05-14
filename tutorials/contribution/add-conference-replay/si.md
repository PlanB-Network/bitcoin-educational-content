---
name: සම්මන්ත්‍රණ ප්‍රතිඋපස්ථාපනය එකතු කිරීම
description: Kako dodati ponovitev konference na PlanB Network?
---
![conference](assets/cover.webp)


PlanBගේ මෙහෙවර වන්නේ Bitcoin පිළිබඳ ඉහළම තත්ත්වයේ අධ්‍යාපනික සම්පත් හැකි ඉක්මනින් බොහෝ භාෂාවන්වලින් ලබා දීමයි. අඩවියේ ප්‍රකාශිත සියලුම අන්තර්ගතය විවෘත මූලාශ්‍ර සහ GitHub හි සත්කාරක වන අතර, ඕනෑම කෙනෙකුට වේදිකාවේ සම්පත් වර්ධනයට දායක විය හැක.


ඔබගේ Bitcoin සම්මන්ත්‍රණයේ නැවත ප්‍රචාරණය PlanB ජාලය වෙබ් අඩවියට එක් කිරීමට සහ මෙම සිදුවීමට දෘශ්‍යතාව ලබා දීමට අවශ්‍යද, නමුත් කෙසේදැයි නොදන්නවාද? මෙම උපකාරකය ඔබ සඳහායි!


කෙසේ වෙතත්, ඔබ අනාගතයේ සිදුවන සමුළුවක් එක් කිරීමට අවශ්‍ය නම්, අඩවියට නව සිදුවීමක් එක් කිරීමේ ආකාරය අපි විස්තර කරන මෙම වෙනත් උපකාරකය කියවීමට මම ඔබට උපදෙස් දෙමි.


https://planb.network/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- පළමුව, ඔබට GitHub හි ගිණුමක් තිබිය යුතුය. ඔබට ගිණුමක් නිර්මාණය කරන ආකාරය නොදන්නා නම්, අපි ඔබට මාර්ගෝපදේශ කිරීමට විස්තරාත්මක උපකාරක පථයක් සකසා ඇත.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Pojdite na [GitHub repozitorij PlanB, namenjen podatkom](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) v razdelku `resources/conference/`:

![conference](assets/02.webp)


- Zgornji desni kot kliknite na gumb `Dodaj datoteko`, nato na `Ustvari novo datoteko`:

![conference](assets/03.webp)


- ඔබ PlanB ජාලයේ අන්තර්ගතයට පෙර කිසිදු දායකත්වයක් නොකළේ නම්, ඔබට මුල් ගබඩාවේ ඔබේ Fork නිර්මාණය කළ යුතුය. ගබඩාවක් Fork කිරීම යනු ඔබේම GitHub ගිණුමේ එම ගබඩාවේ පිටපතක් නිර්මාණය කිරීමයි, එය ඔබට මුල් ගබඩාවට බලපෑමකින් තොරව ව්‍යාපෘතියේ වැඩ කිරීමට ඉඩ සලසයි. `Fork this repository` බොත්තම ක්ලික් කරන්න:

![conference](assets/04.webp)


- ඔබ පසුව GitHub සංස්කරණ පිටුවට පැමිණෙනු ඇත:

![conference](assets/05.webp)


- ඔබේ සමුළුව සඳහා ෆෝල්ඩරයක් සාදන්න. මෙය කිරීමට, `ඔබේ ගොනුව නම් කරන්න...` කොටුවේ, ඔබේ සමුළුවේ නම කුඩා අකුරින් සහ ඉරක් (dashes) භාවිතයෙන් ලියන්න. උදාහරණයක් ලෙස, ඔබේ සමුළුව "Paris Bitcoin Conference" නම් නම්, ඔබ `paris-Bitcoin-conference` ලෙස සටහන් කළ යුතුය. එමෙන්ම ඔබේ සමුළුවේ වසරද එක් කරන්න, උදාහරණයක් ලෙස: `paris-Bitcoin-conference-2024`:

![conference](assets/06.webp)


- ෆෝල්ඩරය නිර්මාණය කිරීම සනාථ කිරීමට, එමම කොටුවේ ඔබේ නමට පසු සළකුණක් සටහන් කරන්න, උදාහරණයක් ලෙස: `paris-Bitcoin-conference-2024/`. සළකුණක් එක් කිරීමෙන් ස්වයංක්‍රීයව ගොනුවක් වෙනුවට ෆෝල්ඩරයක් නිර්මාණය වේ:

![conference](assets/07.webp)


- මෙම ෆෝල්ඩරය තුළ, ඔබ `conference.yml` නම් පළමු YAML ගොනුවක් සාදනු ඇත:

![conference](assets/08.webp)

Izpolnite to datoteko z informacijami, povezanimi z vašo konferenco, z uporabo te predloge:

```yaml
year:
name:
builder:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


උදාහරණයක් ලෙස, ඔබේ YAML ගොනුව මෙසේ පෙනෙන්නට පුළුවන්:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


ඔබේ සංවිධානය සඳහා "*builder*" හඳුනාගැනීමක් තවමත් නොමැති නම්, ඔබට එය මෙම වෙනත් උපකාරකය අනුගමනය කිරීමෙන් එක් කළ හැක.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- මෙම ගොනුවට වෙනස්කම් කිරීම අවසන් කළ පසු, ඒවා සුරැකීමට `Commit changes...` බොත්තම ක්ලික් කරන්න:

![conference](assets/10.webp)


- ඔබේ වෙනස්කම් සඳහා මාතෘකාවක් එක් කරන්න, සහ කෙටි විස්තරයක්:

![conference](assets/11.webp)


- Green `ප්‍රතිසංස්කරණ යෝජනා කරන්න` බොත්තම මත ක්ලික් කරන්න:

![conference](assets/12.webp)


- ඔබේ සියලු වෙනස්කම් සාරාංශ කරන පිටුවකට පසුව එන්න:

![conference](assets/13.webp)


- GitHub පිළිවෙලේ ඉහළ දකුණේ ඇති ඔබේ පැතිකඩ රූපය මත ක්ලික් කරන්න, එවිට `Your Repositories` මත:

![conference](assets/14.webp)


- ඔබගේ Fork PlanB ජාලය ගබඩාවේ තෝරන්න:

![conference](assets/15.webp)


- ඔබේ නව ශාඛාව සමඟ කවුළුවේ ඉහළින් දැනුම්දීමක් ඔබට දැකිය යුතුය. එය `patch-1` ලෙස නම් කර ඇති බවක් විය හැක. එය ක්ලික් කරන්න:

![conference](assets/16.webp)


- ඔබ දැන් ඔබේ වැඩ කරන ශාඛාවෙහි සිටී:

![conference](assets/17.webp)


- `resources/conference/` ෆෝල්ඩරයට ආපසු ගොස්, ඔබ පෙර කමිටුවේදී නිර්මාණය කළ ඔබේ සම්මන්ත්‍රණයේ ෆෝල්ඩරය තෝරන්න:

![conference](assets/18.webp)


- ඔබේ සම්මන්ත්‍රණයේ ෆෝල්ඩරය තුළ, `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත ක්ලික් කරන්න:

![conference](assets/19.webp)


- මෙම නව ෆෝල්ඩරය `assets` ලෙස නම් කර එය නිර්මාණය වූ බව `/` එකක් අගට තබා තහවුරු කරන්න:

![conference](assets/20.webp)


- මෙම `assets` ෆෝල්ඩරය තුළ, `.gitkeep` නමැති ගොනුවක් සාදන්න:

![conference](assets/21.webp)


- Kliknite na gumb `Commit changes...`:

![conference](assets/22.webp)


- කමිටු මාතෘකාව පෙරනිමි ලෙස තබා, `Commit directly to the patch-1 branch` කොටුව සලකුණු කර ඇති බවට වග බලා ගන්න, එවිට `Commit changes` මත ක්ලික් කරන්න:

![conference](assets/23.webp)


- `assets` ෆෝල්ඩරයට ආපසු යන්න:

![conference](assets/24.webp)


- `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Upload files` මත:

![conference](assets/25.webp)


- නව පිටුවක් විවෘත වේ. ඔබේ සමුළුව නිරූපණය කරන සහ PlanB ජාලය වෙබ් අඩවියේ පෙන්වනු ලබන රූපයක් ඇදගෙන යන්න: ![conference](assets/26.webp)
- එය ලාංඡනයක්, කුඩා රූපයක්, හෝ පෝස්ටරයක් විය හැක:

![conference](assets/27.webp)


- Ko slika naložena, preverite, da je polje `Commit directly to the patch-1 branch` označeno, nato kliknite na `Commit changes`:

![conference](assets/28.webp)


- සැලකිලිමත් වන්න, ඔබේ රූපය `thumbnail` ලෙස නම් කර තිබිය යුතු අතර `.webp` ආකෘතියෙන් තිබිය යුතුය. එබැවින් සම්පූර්ණ ගොනු නාමය විය යුතුය: `thumbnail.webp`:

![conference](assets/29.webp)


- ඔබේ `assets` ෆෝල්ඩරයට ආපසු ගොස් `.gitkeep` මැදිහත්වීම් ගොනුව මත ක්ලික් කරන්න:

![conference](assets/30.webp)


- Datoteko odprite in kliknite na 3 majhne pike v zgornjem desnem kotu, nato na `Izbriši datoteko`:

![conference](assets/31.webp)


- තහවුරු කරන්න ඔබ තවමත් එකම කාර්ය ශාඛාවේ සිටින බව, එවිට `Commit changes` බොත්තම ක්ලික් කරන්න:

![conference](assets/32.webp)


- ඔබේ කමිටුවට මාතෘකාවක් සහ විස්තරයක් එක් කරන්න, එවිට `Commit changes` මත ක්ලික් කරන්න:

![conference](assets/33.webp)


- ඔබේ සම්මන්ත්‍රණ ෆෝල්ඩරයට ආපසු යන්න:

![conference](assets/34.webp)


- කොටුව `Add file` මත ක්ලික් කරන්න, එවිට `Create new file` මත:

![conference](assets/35.webp)


- Ustvarite novo markdown (.md) datoteko in jo poimenujte z oznako vašega maternega jezika. Ta datoteka bo uporabljena za ponovitve vaših konferenc. Na primer, če želim napisati opise konferenc v angleščini, bom to datoteko poimenoval en.md:

![conference](assets/36.webp)


- මෙම සැකිල්ල ඔබේ සම්මන්ත්‍රණයේ වින්‍යාසයට අනුව අනුකූල කරමින් මෙම markdown ගොනුව පුරවන්න:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- ඔබේ ලේඛනයේ ආරම්භයේ, "ඉදිරි කාරක" හි, `name:` ක්ෂේත්‍රය ඔබේ සම්මන්ත්‍රණයේ නම සහ නැවත ප්‍රදර්ශන වර්ෂය සමඟ පුරවන්න. `description:` ක්ෂේත්‍රයෙහි, ගොනුවේ භාෂාවෙන් ඔබේ සිදුවීම පිළිබඳ කෙටි විස්තරයක් ලියන්න. උදාහරණයක් ලෙස, `en.md` නම් ගොනුවක් සඳහා, විස්තරය ඉංග්‍රීසි භාෂාවෙන් විය යුතුය. PlanB ජාලක කණ්ඩායම ඔබේ විස්තරය ඔවුන්ගේ ආකෘතිය භාවිතයෙන් පරිවර්තනය කිරීමට කටයුතු කරනු ඇත.
- පළමු මට්ටමේ මාතෘකා, `#` මගින් සලකුණු කර ඇති, දර්ශන අනුව සම්මන්තරණය සංවිධානය කිරීමට භාවිතා කරයි. උදාහරණයක් ලෙස, ප්‍රධාන වේදිකාව සඳහා `# Main Stage` සහ වැඩමුළු සඳහා කැපවූ වේදිකාවක් සඳහා `# Workshop Room`.



- දෙවන මට්ටමේ මාතෘකා, ද්විත්ව `##` මගින් සලකුණු කර ඇති, විවිධ නැවත ප්‍රspardha වීඩියෝවන් වෙන් කිරීමට භාවිතා වේ. සම්මන්ත්‍රණ අඛණ්ඩව අර්ධ දිනයක් පුරා චිත‍්‍රගත කර තිබේ නම්, උදාහරණයක් ලෙස, `## සිකුරාදා උදෑසන` ලෙස සලකුණු කරන්න. සම්මන්ත්‍රණ වෙන්ව චිත‍්‍රගත කර විකාශය කර තිබේ නම්, සම්මන්ත්‍රණය සෘජුවම දෙවන මට්ටමේ මාතෘකාවක් ලෙස නම් කරන්න.



- Under each second-level title, insert a link to the corresponding replay video. The syntax should be: `![video](https://youtu.be/XXXXXXXXXXXX)`, replacing `XXXXXXXXXXXX` with the actual video link.



- If the format allows (individual conferences), you can add the names of the speakers. To do this, add the `Speaker:` field followed by the name or pseudonym of the speaker under the video link. In case of multiple speakers, separate each name with a comma, like this for example: `Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- මෙම ගොනුවට ඔබේ වෙනස්කම් සම්පූර්ණ වූ විට, `Commit changes...` බොත්තම ක්ලික් කිරීමෙන් ඒවා සුරකින්න:

![conference](assets/38.webp)


- Dodajte naslov za vaše spremembe in kratek opis:

![conference](assets/39.webp)


- `Commit changes` මත ක්ලික් කරන්න:

![conference](assets/40.webp)


- ඔබේ සම්මන්ත්‍රණ ෆෝල්ඩරය දැන් මෙසේ පෙනිය යුතුය:

![conference](assets/41.webp)


- Če je vse po vašem zadovoljstvu, se vrnite na korenino vašega Fork:

![conference](assets/42.webp)


- ඔබේ ශාඛාව වෙනස්කම් වලට ලක්ව ඇති බව පෙන්වන පණිවිඩයක් ඔබට දැකිය යුතුය. `Compare & pull request` බොත්තම මත ක්ලික් කරන්න:

![conference](assets/43.webp)


- PR සඳහා පැහැදිලි මාතෘකාවක් සහ විස්තරයක් එක් කරන්න:

![conference](assets/44.webp)


- `Create pull request` බොත්තම මත ක්ලික් කරන්න:

![conference](assets/45.webp)

සුභ පැතුම්! ඔබේ PR සාර්ථකව නිර්මාණය කර ඇත. දැන් පරිපාලකයෙකු එය සමාලෝචනය කරනු ඇත, සහ සියල්ල සාර්ථක නම්, එය PlanB ජාලයේ ප්‍රධාන ගබඩාවට ඒකාබද්ධ කරනු ඇත. ඔබේ සම්මන්ත්‍රණයේ නැවත ප්‍රspardhanaya කිහිප දිනකින් වෙබ් අඩවියේ පෙනෙනු ඇත.


කරුණාකර ඔබේ PR හි ප්‍රගතිය අනුගමනය කරන්න. පරිපාලකයෙකු අමතර තොරතුරු ඉල්ලා අදහසක් තැබිය හැකි බව සම්භාව්‍ය වේ. ඔබේ PR වලංගු නොවන තෙක්, ඔබට එය PlanB ජාලයේ GitHub ගබඩාවේ `Pull requests` ටැබය යටතේ බලන්න පුළුවන:

![conference](assets/46.webp)


ඔබේ වටිනා දායකත්වය සඳහා බොහෝම ස්තූතියි! :)