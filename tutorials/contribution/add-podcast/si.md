---
name: PlanB Network-ට පොඩ්කාස්ට් එකක් එකතු කිරීම
description: PlanB Network-ට නව පොඩ්කාස්ට් එකක් එකතු කරන ආකාරය කෙසේද?
---
![podcast](assets/cover.webp)


PlanB का मिशन Bitcoin पर शीर्ष स्तर के शैक्षिक संसाधन यथासंभव अधिक भाषाओं में प्रदान करना है। साइट पर प्रकाशित सभी सामग्री ओपन-सोर्स है और GitHub पर होस्ट की गई है, जिससे किसी को भी प्लेटफ़ॉर्म को समृद्ध करने में भाग लेने की अनुमति मिलती है।


ඔබ PlanB ජාලය වෙබ් අඩවියට Bitcoin පොඩ්කාස්ට් එකක් එක්කර ඔබේ වැඩසටහන සඳහා දෘශ්‍යතාවය වැඩි කිරීමට බලාපොරොත්තු වන අතර, එය කෙසේදැයි නොදන්නවාද? මේ උපකාරිකාව ඔබ සඳහායි!

![podcast](assets/01.webp)


- Najprej morate imeti GitHub račun. Če ne veste, kako ga ustvariti, smo pripravili podroben vodič, ki vas bo vodil skozi postopek.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- යන්න [PlanB හි දත්ත සඳහා කැපවූ GitHub ගබඩාවට](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts) `resources/podcasts/` කොටසෙහි:

![podcast](assets/02.webp)


- ඉහළ දකුණේ ඇති `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත ක්ලික් කරන්න:

![podcast](assets/03.webp)


- ඔබ PlanB ජාලයේ අන්තර්ගතයට පෙර කිසිදු දායකත්වයක් ලබා දී නැත්නම්, ඔබට මුල් ගබඩාවේ ඔබේ Fork නිර්මාණය කළ යුතුය. ගබඩාවක් Fork කිරීම යනු, ඔබේම GitHub ගිණුමේ එම ගබඩාවේ පිටපතක් නිර්මාණය කිරීමයි, එය ඔබට මුල් ගබඩාවට බලපෑමකින් තොරව ව්‍යාපෘතියේ වැඩ කිරීමට ඉඩ සලසයි. `Fork this repository` බොත්තම ක්ලික් කරන්න:

![podcast](assets/04.webp)


- ඔබ එවිට GitHub සංස්කරණ පිටුවට පැමිණෙනු ඇත:

![podcast](assets/05.webp)


- ඔබේ පොඩ්කාස්ට් සඳහා ෆෝල්ඩරයක් සාදන්න. ایسا کرنے کے لیے، `Name your file...` කොටුවේ, ඔබේ පොඩ්කාස්ට් නම කුඩා අකුරින් සහ ඉරක් (dashes) භාවිතයෙන් ලියන්න. උදාහරණයක් ලෙස, ඔබේ වැඩසටහන "Super Podcast Bitcoin" නම් නම්, ඔබ `super-podcast-Bitcoin` ලෙස ලියිය යුතුය:

![podcast](assets/06.webp)


- Če želite potrditi ustvarjanje mape, preprosto dodajte poševnico za imenom vašega podkasta v istem polju, na primer: `super-podcast-Bitcoin/`. Dodajanje poševnice samodejno ustvari mapo namesto datoteke:

![podcast](assets/07.webp)


- V tej mapi boste ustvarili prvo datoteko YAML z imenom `podcast.yml`:

![podcast](assets/08.webp)


- Izpolnite to datoteko z informacijami o vašem podcastu z uporabo te predloge:


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


මෙන්න එක් එක් ක්ෂේත්‍රය සඳහා පුරවිය යුතු විස්තර:



- `name`**: ඔබේ පොඩ්කාස්ට් එකේ නම සදහන් කරන්න.
- `host`**: පොඩ්කාස්ට් එකේ කථිකයන්ගේ හෝ සභාපතිගේ නම හෝ කුමන්ත්‍රණ නාම ලැයිස්තුගත කරන්න. සෑම නමක්ම කොමාවකින් වෙන් කළ යුතුය.
- `language`**: ඔබේ පොඩ්කාස්ට් එකේ කතා කරන භාෂාවේ භාෂා කේතය සදහන් කරන්න. උදාහරණයක් ලෙස, ඉංග්‍රීසි සඳහා `en`, ඉතාලි සඳහා `it`...



- `links`**: ඔබේ අන්තර්ගතයට සබැඳි ලබා දෙන්න. ඔබට විකල්ප දෙකක් ඇත:
 - `podcast`: ඔබේ පොඩ්කාස්ට් සඳහා සබැඳිය,
 - `twitter`: පොඩ්කාස්ට් එක හෝ එය නිෂ්පාදනය කරන සංවිධානයේ ට්විටර් පැතිකඩට සබැඳිය,
 - `website`: පොඩ්කාස්ට් එක හෝ එය නිෂ්පාදනය කරන සංවිධානයේ වෙබ් අඩවියට සබැඳිය.



- `description`**: Dodajte kratek odstavek, ki opisuje vaš podcast. Opis mora biti v istem jeziku, kot je navedeno v polju `language:`.



- `oznake`**: Dodajte dve oznaki, povezani z vašim podcastom. Primeri:
    - `Bitcoin`
    - `තාක්ෂණය`
    - `ekonomija`
    - `izobraževanje`...



- `contributors`**: Če imate ID sodelavca, ga navedite.


उदाहरणार्थ, तपाईंको YAML फाइल यसरी देखिन सक्छ:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- මෙම ගොනුවට වෙනස්කම් කිරීම අවසන් කළ පසු, ඒවා සුරක්ෂිත කිරීමට `Commit changes...` බොත්තම ක්ලික් කරන්න:

![podcast](assets/10.webp)


- Dodajte naslov za vaše spremembe in kratek opis:

![podcast](assets/11.webp)


- Green `ප්‍රතිසංස්කරණ යෝජනා කරන්න` බොත්තම මත ක්ලික් කරන්න:

![podcast](assets/12.webp)


- ඉන්පසු ඔබේ සියලු වෙනස්කම් සාරාංශ ගත කරන පිටුවකට ඔබ පැමිණෙනු ඇත:

![podcast](assets/13.webp)


- GitHub හි ඔබේ පැතිකඩ රූපය ඉහළ දකුණේ ක්ලික් කරන්න, එවිට `Your Repositories` මත:

![podcast](assets/14.webp)


- ඔබේ Fork PlanB ජාලය ගබඩාවේ තෝරන්න:

![podcast](assets/15.webp)


- ඔබේ නව ශාඛාව සමඟ කවුළුවේ ඉහළින් දැනුම්දීමක් ඔබට දැකිය යුතුය. එය `patch-1` ලෙස නම් කර ඇති බවක් සම්භාව්‍යව පෙනේ. එය ක්ලික් කරන්න:

![podcast](assets/16.webp)


- You are now on your working branch:

![podcast](assets/17.webp)


- යන්න `resources/podcast/` ෆෝල්ඩරයට සහ ඔබ මීට පෙර කමිටුවේ නිර්මාණය කළ පෝඩ්කාස්ට් ෆෝල්ඩරය තෝරන්න: ![podcast](assets/18.webp)
- ඔබේ පොඩ්කාස්ට් ෆෝල්ඩරය තුළ, `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Create new file` මත ක්ලික් කරන්න:

![podcast](assets/19.webp)


- මෙම නව ෆෝල්ඩරය `assets` ලෙස නම් කර එය නිර්මාණය වූ බව `/` එකතු කිරීමෙන් තහවුරු කරන්න:

![podcast](assets/20.webp)


- මෙම `assets` ෆෝල්ඩරය තුළ, `.gitkeep` නමැති ගොනුවක් සාදන්න:

![podcast](assets/21.webp)


- `Commit changes...` බොත්තම මත ක්ලික් කරන්න:

![podcast](assets/22.webp)


- Pustite naslov potrditve kot privzet, in se prepričajte, da je polje `Commit directly to the patch-1 branch` označeno, nato kliknite na `Commit changes`:

![podcast](assets/23.webp)


- `assets` ෆෝල්ඩරයට ආපසු යන්න:

![podcast](assets/24.webp)


- `Add file` බොත්තම මත ක්ලික් කරන්න, එවිට `Upload files` මත:

![podcast](assets/25.webp)


- Nova stran se bo odprla. Povlecite in spustite logotip svojega podkasta v območje. Ta slika bo prikazana na spletnem mestu PlanB Network:

![podcast](assets/26.webp)


- Bodite previdni, slika mora biti kvadratna, da se najbolje prilega naši spletni strani:

![podcast](assets/27.webp)


- Ko slika naložena, preverite, da je polje `Commit directly to the patch-1 branch` označeno, nato kliknite na `Commit changes`:

![podcast](assets/28.webp)


- සැලකිලිමත් වන්න, ඔබේ පින්තූරය `logo` ලෙස නම් කළ යුතු අතර `.webp` ආකෘතියෙන් විය යුතුය. එබැවින් සම්පූර්ණ ගොනු නාමය විය යුතුය: `logo.webp`:

![podcast](assets/29.webp)


- ඔබේ `assets` ෆෝල්ඩරයට ආපසු ගොස් මැදිහත් ගොනුව `.gitkeep` මත ක්ලික් කරන්න:

![podcast](assets/30.webp)


- Datoteko odprite in kliknite na tri majhne pike v zgornjem desnem kotu, nato na `Izbriši datoteko`:

![podcast](assets/31.webp)


- සම කාර්ය ශාඛාවෙම සිටින බව තහවුරු කර, එවිට `Commit changes` බොත්තම ක්ලික් කරන්න:

![podcast](assets/32.webp)


- ඔබේ කැමට්ටුවට ශීර්ෂයක් සහ විස්තරයක් එක් කරන්න, එවිට `Commit changes` මත ක්ලික් කරන්න:

![podcast](assets/33.webp)


- ඔබේ ගබඩාවේ මූලයට ආපසු යන්න:

![podcast](assets/34.webp)


- ඔබේ ශාඛාව වෙනස් වී ඇති බව පෙන්වන පණිවිඩයක් ඔබට දැකිය යුතුය. `Compare & pull request` බොත්තම ක්ලික් කරන්න:

![podcast](assets/35.webp)


- ඔබේ PR සඳහා පැහැදිලි ශීර්ෂයක් සහ විස්තරයක් එක් කරන්න:

![podcast](assets/36.webp)


- `Create pull request` බොත්තම මත ක්ලික් කරන්න:

![podcast](assets/37.webp)

සුභ පැතුම්! ඔබේ PR සාර්ථකව නිර්මාණය කර ඇත. දැන් පරිපාලකයෙකු එය සමාලෝචනය කරනු ඇති අතර, සියල්ල සවිස්තරාත්මකව නිවැරදි නම්, එය PlanB ජාලයේ ප්‍රධාන ගබඩාවට ඒකාබද්ධ කරනු ඇත. ඔබේ පොඩ්කාස්ට් එක දින කිහිපයකින් වෙබ් අඩවියේ පෙනෙනු ඇත.


කරුණාකර ඔබේ PR හි ප්‍රගතිය අනුගමනය කරන්න. පරිපාලකයෙකු අමතර තොරතුරු ඉල්ලා අදහසක් තැබිය හැකිය. ඔබේ PR වලංගු නොවන තෙක්, ඔබට එය PlanB Network GitHub ගබඩායේ `Pull requests` ටැබ් එකේ දී බලන්න පුළුවන්:

![podcast](assets/38.webp)

ඔබේ වටිනා දායකත්වය සඳහා බොහෝම ස්තූතියි! :)