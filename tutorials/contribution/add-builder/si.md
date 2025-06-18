---
name: බිල්ඩර්වරයෙකු එක් කිරීම
description: PlanB Network හි නව ගොඩනැගින්නෙකු එක් කිරීමට යෝජනා කිරීමේ ආකාරය කෙසේද?
---
![builder](assets/cover.webp)


PlanB හි මෙහෙවර වන්නේ Bitcoin පිළිබඳ ඉහළම තත්ත්වයේ අධ්‍යාපනික සම්පත් හැකි ඉක්මනින් බොහෝ භාෂාවන්වලින් ලබා දීමයි. අඩවිය මත ප්‍රකාශිත සියලුම අන්තර්ගතය විවෘත මූලාශ්‍ර සහ GitHub හි සත්කාරක වන අතර, එය වේදිකාව වර්ධනය කිරීමට ඕනෑම කෙනෙකුට සහභාගී විය හැක.


ඔබගේ සමාගම හෝ මෘදුකාංගය PlanB ජාලය අඩවියට නව Bitcoin "builder" එකක් එක් කිරීමට සහ දෘශ්‍යතාව ලබා දීමට අවශ්‍යද, නමුත් කෙසේදැයි නොදන්නවාද? මේ උපකාරකය ඔබ සඳහායි!

![builder](assets/01.webp)


- Najprej morate imeti GitHub račun. Če ne veste, kako ustvariti račun, smo pripravili podroben vodič, ki vas bo vodil skozi postopek.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- [PlanB වෙත අදාළ දත්ත සඳහා GitHub ගබඩාවට යන්න](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/builders) `resources/builder/` කොටසෙහි:

![builder](assets/02.webp)


- ඉහළ දකුණේ ඇති `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත ක්ලික් කරන්න:

![builder](assets/03.webp)


- Če še nikoli niste prispevali k vsebini PlanB Network, boste morali ustvariti svoj Fork iz izvirnega repozitorija. Forkanje repozitorija pomeni ustvarjanje kopije tega repozitorija na vašem lastnem GitHub računu, kar vam omogoča delo na projektu, ne da bi vplivali na izvirni repozitorij. Kliknite na gumb `Fork this repository`:

![builder](assets/04.webp)


- ඔබ පසුව GitHub සංස්කරණ පිටුවට පැමිණෙනු ඇත:

![builder](assets/05.webp)


- ඔබේ සමාගම සඳහා ෆෝල්ඩරයක් සාදන්න. මෙය කිරීමට, `ඔබේ ගොනුව නම් කරන්න...` කොටුවේ, ඔබේ සමාගමේ නම කුඩා අකුරින් සහ ඉරක් වෙනුවට ඉරක් යොදා ලියන්න. උදාහරණයක් ලෙස, ඔබේ සමාගම "Bitcoin Baguette" නම් නම්, ඔබ `Bitcoin-baguette` ලෙස ලියිය යුතුය:

![builder](assets/06.webp)


- ෆෝල්ඩරය නිර්මාණය වලංගු කර ගැනීමට, ඔබේ නම පසුතැවෙමින් එම කොටුව තුළ සරලව සලකුණක් එක් කරන්න, උදාහරණයක් ලෙස: `Bitcoin-baguette/`. සලකුණක් එක් කිරීමෙන් ස්වයංක්‍රීයව ෆෝල්ඩරයක් නිර්මාණය වේ, ගොනුවක් නොව:

![builder](assets/07.webp)


- මෙම ෆෝල්ඩරය තුළ, ඔබ `builder.yml` නම් පළමු YAML ගොනුවක් සාදනු ඇත:

![builder](assets/08.webp)


- Izpolnite to datoteko z informacijami o vašem podjetju z uporabo te predloge:


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


මෙන්න සෑම යතුරක් සඳහාම පුරවිය යුතු දේ:


- `name`: ඔබේ සමාගමේ නම (අනිවාර්යය);
- `Address` : ඔබේ ව්‍යාපාරයේ ස්ථානය (විකල්ප);
- `language` : ඔබේ ව්‍යාපාරය ක්‍රියාත්මක වන රටවල් හෝ සහය දක්වන භාෂා (විකල්ප);
- `links` : ඔබේ ව්‍යාපාරයේ විවිධ නිල සබැඳි (විකල්ප);
- `tags` : 2 ව්‍යාපාරය සඳහා සුදුසු පද (අනිවාර්ය);
- `category` : ඔබේ ව්‍යාපාරය ක්‍රියාත්මක වන ක්ෂේත්‍රය හොඳින් විස්තර කරන කාණ්ඩය පහත විකල්ප අතරින්:
 - `Wallet`,
 - `ආධාරක ව්‍යුහය`,
 - `Exchange`,
 - `izobraževanje`,
 - `service`,
 - `ප්‍රජාවන්`,
 - `konferenca`,
 - `ප්‍රතිචාරය`,
 - `ආයෝජනය`,
 - `node`,
 - `Mining`,
 - `news`,
 - `නිෂ්පාදකයා`.


උදාහරණයක් ලෙස, ඔබේ YAML ගොනුව මෙසේ පෙනෙන්නට පුළුවන්:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![builder](assets/09.webp)


- මෙම ගොනුවට වෙනස්කම් කිරීම අවසන් වූ විට, `Commit changes...` බොත්තම ක්ලික් කිරීමෙන් ඒවා සුරකින්න:

![builder](assets/10.webp)


- ඔබේ වෙනස්කම් සඳහා මාතෘකාවක් එක් කරන්න, කෙටි විස්තරයක් සමඟ:

![builder](assets/11.webp)


- Green `ප්‍රතිසංස්කරණ යෝජනා කරන්න` බොත්තම මත ක්ලික් කරන්න:

![builder](assets/12.webp)


- ඔබේ සියලු වෙනස්කම් සාරාංශ කරන පිටුවකට පසුව එන්න:

![builder](assets/13.webp)


- GitHub प्रोफ़ाइल चित्र पर ऊपर दाईं ओर क्लिक करें, फिर `Your Repositories` पर क्लिक करें:

![builder](assets/14.webp)


- Izberite svoj Fork iz skladišča PlanB Network:

![builder](assets/15.webp)


- ඔබේ නව ශාඛාව සමඟ කවුළුවේ ඉහළින් දැනුම්දීමක් ඔබට දැකිය යුතුය. එය `patch-1` ලෙස නම් කර ඇති බවක් සම්භාව්‍යව ඇත. එය ක්ලික් කරන්න:

![builder](assets/16.webp)


- ඔබ දැන් ඔබේ කාර්ය ශාඛාවේ සිටී (**ඔබේ පෙර වෙනස්කම් ලෙසම එකම ශාඛාවේ සිටින බව සහතික වන්න, මෙය වැදගත් වේ!**):

![builder](assets/17.webp)


- Pojdite nazaj v mapo `resources/builders/` in izberite mapo vašega podjetja, ki ste jo pravkar ustvarili v prejšnji potrditvi:

![builder](assets/18.webp)


- ඔබේ ව්‍යාපාරයේ ෆෝල්ඩරය තුළ, `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත:

![builder](assets/19.webp)


- මෙම නව ෆෝල්ඩරය `assets` ලෙස නම් කර එය නිර්මාණය වූ බව `/` එකක් අගට තබා තහවුරු කරන්න:

![builder](assets/20.webp)


- මෙම `assets` ෆෝල්ඩරය තුළ, `.gitkeep` නමැති ගොනුවක් සාදන්න:

![builder](assets/21.webp)


- `Commit changes...` බොත්තම මත ක්ලික් කරන්න:

![builder](assets/22.webp)


- විකල්ප ලෙස සමාජාත්මක, සහයෝගී, සහ සෘජු ප්‍රතිචාර ලබා දීම සඳහා, ඔබට පහත පියවර අනුගමනය කළ හැක: `Commit directly to the patch-1 branch` කොටුව සලකුණු කර ඇති බව සහතික කර, පසුව `Commit changes` මත ක්ලික් කරන්න: ![builder](assets/23.webp)
- `assets` ෆෝල්ඩරයට ආපසු යන්න:

![builder](assets/24.webp)


- `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Upload files` මත ක්ලික් කරන්න:

![builder](assets/25.webp)


- Nova stran se bo odprla. Povlecite in spustite sliko vašega podjetja ali vaše programske opreme v to območje. Ta slika bo prikazana na spletnem mestu PlanB Network:

![builder](assets/26.webp)


- එය ලාංඡනයක් හෝ අයිකනයක් විය හැක:

![builder](assets/27.webp)


- Ko je slika naložena, preverite, da je polje `Commit directly to the patch-1 branch` označeno, nato kliknite na `Commit changes`:

![builder](assets/28.webp)


- Bodite previdni, vaša slika mora biti kvadratna, imenovana mora biti `logo` in mora biti v formatu `.webp`. Celotno ime datoteke mora biti torej: `logo.webp`:

![builder](assets/29.webp)


- ඔබේ `assets` ෆෝල්ඩරයට ආපසු ගොස් `.gitkeep` අතුරු ගොනුව මත ක්ලික් කරන්න:

![builder](assets/30.webp)


- Datoteko odprite in kliknite na tri majhne pike v zgornjem desnem kotu, nato na `Izbriši datoteko`:

![builder](assets/31.webp)


- තහවුරු කරන්න ඔබ තවමත් එකම වැඩ කරන ශාඛාවෙම සිටිනවාද, එවිට `Commit changes` බොත්තම ක්ලික් කරන්න:

![builder](assets/32.webp)


- ඔබේ කමිටුවට මාතෘකාවක් සහ විස්තරයක් එක් කරන්න, එවිට `Commit changes` මත ක්ලික් කරන්න:

![builder](assets/33.webp)


- ඔබේ සමාගමේ ෆෝල්ඩරයට ආපසු යන්න:

![builder](assets/34.webp)


- `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත ක්ලික් කරන්න:

![builder](assets/35.webp)


- Ustvarite novo datoteko YAML in jo poimenujte z oznako vašega maternega jezika. Ta datoteka bo uporabljena za opis graditelja. Na primer, če želim napisati svoj opis v angleščini, bom to datoteko poimenoval `en.yml`:

![builder](assets/36.webp)


- Izpolnite to datoteko YAML z uporabo te predloge:

```yaml
description: |

contributors:
-
```



- `contributors` යතුර සඳහා, ඔබ PlanB ජාලයට ඔබේ දායක හඳුනාගැනීමේ සලකුණ එකතු කළ හැක. ඔබට එවැනි එකක් නොමැති නම්, මෙම ක්ෂේත්‍රය හිස්ව තබන්න.
- `description` යතුර සඳහා, ඔබේ සමාගම හෝ ඔබේ මෘදුකාංගය විස්තර කරන කෙටි වගුවක් එකතු කළ යුතුය. විස්තරය ගොනුවේ නම ලෙසම භාෂාවෙන් තිබිය යුතුය. මෙම විස්තරය අඩවිය මගින් සහය දක්වන සියලුම භාෂාවන්ට පරිවර්තනය කිරීමට ඔබට අවශ්‍ය නොවේ, PlanB කණ්ඩායම් තම ආකෘතිය භාවිතා කරමින් එය සිදු කරනු ඇත. උදාහරණයක් ලෙස, ඔබේ ගොනුව මෙසේ පෙනෙන්නට ඇත:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![builder](assets/37.webp)


- `Commit changes` බොත්තම මත ක්ලික් කරන්න:

![builder](assets/38.webp)


- `Commit directly to the patch-1 branch` කොටුව සලකුණු කර ඇති බව සහතික කර, ශීර්ෂයක් එක්කර, පසුව `Commit changes` මත ක්ලික් කරන්න:

![builder](assets/39.webp)


- ඔබේ සමාගම් ෆෝල්ඩරය දැන් මෙසේ පෙනිය යුතුය:

![builder](assets/40.webp)


- Če je vse po vašem zadovoljstvu, se vrnite na korenino vašega Fork:

![builder](assets/41.webp)


- ඔබේ ශාඛාව වෙනස් වී ඇති බව පෙන්වන පණිවිඩයක් ඔබට දැකිය යුතුය. `Compare & pull request` බොත්තම ක්ලික් කරන්න:

![builder](assets/42.webp)


- PR සඳහා පැහැදිලි ශීර්ෂයක් සහ විස්තරයක් එක් කරන්න:

![builder](assets/43.webp)


- `Create pull request` බොත්තම මත ක්ලික් කරන්න:

![builder](assets/44.webp)

සුභ පැතුම්! ඔබේ PR සාර්ථකව නිර්මාණය කර ඇත. දැන් පරිපාලකයෙකු එය සමාලෝචනය කරනු ඇති අතර, සියල්ල සරියට ඇති නම්, එය PlanB ජාලයේ ප්‍රධාන ගබඩාවට ඒකාබද්ධ කරනු ඇත. ඔබේ ගොඩනැගීමේ පැතිකඩ දින කිහිපයකට පසු වෙබ් අඩවියේ පෙනෙනු ඇත.


ඔබේ PR හි ප්‍රගතිය අනිවාර්යයෙන්ම අනුගමනය කරන්න. පරිපාලකයෙකු අමතර තොරතුරු ඉල්ලා අදහසක් තැබිය හැක. ඔබේ PR වලංගු නොවන තෙක්, ඔබට එය PlanB Network GitHub ගබඩායේ `Pull requests` ටැබ් එකේ පරීක්ෂා කළ හැක:

![builder](assets/45.webp)

Vaš dragoceni prispevek zelo cenimo! :)