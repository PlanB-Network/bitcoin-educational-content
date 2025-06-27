---
name: Phoenix
description: Phoenix Wallet ස්ථාපනය කිරීම සහ භාවිතය
---
![cover](assets/cover.webp)


Phoenix යනු ACINQ නම් ප්‍රංශ සමාගමක් විසින් සංවර්ධනය කරන ලද ස්වයං-අධිකාරක Lightning Wallet සහ node එකකි, එය Lightning මත පදනම් වූ මෘදුකාංග විසඳුම් විශේෂඥයි. Wallet හෝ Satoshi වැනි අධිකාරක Lightning පසුම්බි වලින් වෙනස්ව, එහි බිට්කොයින් තෙවන පාර්ශවයක් විසින් රඳවා තබන අතර, Phoenix පරිශීලකයින්ට ඔවුන්ගේ පෞද්ගලික යතුරු සම්පූර්ණයෙන්ම පාලනය කිරීමට හැකියාව සලසයි.


Phoenix ඔබේ දුරකථනයේ සවි කළ සත්‍ය Lightning නියමුවෙකු ලෙස ක්‍රියා කරයි, ස්වයංක්‍රීයව ACINQ හි Lightning නියමුවා සමඟ නාලිකාවක් විවෘත කරයි. මෙම යෙදුම Lightning-KMP මත පදනම්ව ඇති අතර, Kotlin හි Lightning Network හි හරස් වේදිකා ක්‍රියාත්මක කිරීමක් වන අතර, ජංගම පසුම්බි සඳහා සුදුසුකරණය කර ඇත. අනෙකුත් Lightning නියමු විසඳුම්වලට වඩා, Phoenix කළමනාකරණය බොහෝ සරල කරයි. පරිශීලකයාට නාලිකා විවෘත කිරීම සහ වසා දැමීම, Bitcoin නියමුවක් ක්‍රියාත්මක කිරීම හෝ Lightning Network හි ද්‍රවතාවය කළමනාකරණය කිරීම කළ යුතු නැත. Phoenix මෙම සියලු තාක්ෂණික මෙහෙයුම් පසුබිමෙන් කළමනාකරණය කරයි.


මෙම යෙදුම ජංගම Lightning පසුම්බි භාවිතයේ පහසුව සහ පහසුව සමඟ සත්‍ය පුද්ගලික Lightning නියමකගේ ආරක්ෂාව සහ ස්වාධීනත්වය එකතු කරයි. Phoenix මෘදු, අත්භාවිතා කළ හැකි පරිශීලක අත්දැකීමක් විඳිමින් Lightning Network ආරක්ෂිතව, කාර්යක්ෂමව සහ ස්වාධීනව භාවිතා කිරීම සම්භවය කරයි.


වෙනුවට, විශේෂිත ගාස්තු අදාළ වේ:




- ලයිට්නින්ග් හරහා යැවීමේ වියදම මුදලේ 0.4% ක් සහ Sats 4 ක් වේ ;
- ඔබට Lightning හරහා මුදල් ලබා ගැනීමට අවශ්‍ය නම්, මුදලේ 1% ක් අයකෙරේ;
- प्रत्येक च्यानल खोल्न 1000 Sats लागत लाग्छ।


මගේ අදහස අනුව, Phoenix යනු සුරැකුම් Lightning පෝර්ට්ෆෝලියෝ සහ Lightning නියමකයෙකුගේ අතින් කළමනාකරණය අතර විශිෂ්ට මධ්‍යස්ථ විසඳුමක් නිරූපණය කරයි. මෙම යෙදුම, තමන්ගේම LND හෝ Core Lightning කළමනාකරණය කිරීමේ විස්තර සමඟ ගනුදෙනු නොකරන ආරම්භකයින් සහ ප්‍රවීණ පරිශීලකයින් දෙපාර්ශවයටම සුදුසු වේ. එය භාවිතා කරන ආකාරය සොයා බලමු!


![Image](assets/fr/01.webp)


## යෙදුම ස්ථාපනය කරන්න


යාපනය :




- [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.Mainnet) මත;
- [App Store](https://apps.apple.com/fr/app/phoenix-Wallet/id1544097028?l=en-GB) මත.


![Image](assets/fr/02.webp)


ඔබට [ඔවුන්ගේ GitHub ගබඩාවේ apk ගොනුව සමඟ](https://github.com/ACINQ/phoenix/releases) යෙදුම ස්ථාපනය කළ හැක.


![Image](assets/fr/03.webp)


## පොර්ට්ෆෝලියෝ නිර්මාණය


යෙදුම ආරම්භ වූ විට, ඉදිරිපත් කිරීම මඟහරවා ගැනීමට "*Next*" බොත්තම ක්ලික් කරන්න, එවිට "*Start*" මත ක්ලික් කරන්න.


![Image](assets/fr/04.webp)


"*Wallet නවයක් සාදන්න*" තෝරන්න.


![Image](assets/fr/05.webp)


ඒකයි, ඔබේ Lightning Wallet සහ node දැන් නිර්මාණය වී ඇත.


![Image](assets/fr/06.webp)


## Mnemonic වාක්‍යය සුරකින්න


Preden začnemo, moramo shraniti našo 12-besedno Mnemonic frazo. Ta fraza omogoča popoln, neomejen dostop do vseh vaših bitcoinov. Kdor ima to frazo, lahko ukrade vaša sredstva, tudi brez fizičnega dostopa do vašega telefona.


12-වචන වාක්‍යය ඔබේ දුරකථනය අහිමිවීම, සොරකම හෝ කැඩීමේ අවස්ථාවකදී ඔබේ බිට්කොයින් වෙත ප්‍රවේශය නැවත ලබා දේ. එබැවින් එය සූක්ෂමව සුරැකීම සහ ආරක්ෂිත ස්ථානයක ගබඩා කිරීම ඉතාමත් වැදගත් වේ.


ඔබට එය කඩදාසියේ ලියන්න හෝ, අමතර ආරක්ෂාව සඳහා, ගිනි, ගංවතුර හෝ කඩාවැටීමෙන් ආරක්ෂා කිරීමට එය වානේ මත කැටයම් කළ හැකිය. ඔබේ Mnemonic සඳහා මාධ්‍යය තෝරා ගැනීම ඔබේ ආරක්ෂක උපාය මාර්ගය මත රඳා පවතී, නමුත් ඔබ මධ්‍යම ප්‍රමාණයන් අඩංගු වියදම් පෝර්ට්ෆෝලියෝවක් ලෙස Phoenix භාවිතා කරන්නේ නම්, කඩදාසි ප්‍රමාණවත් විය හැකිය.


Mnemonic වාක්‍යය සුරැකීම සහ කළමනාකරණය කිරීමේ නිවැරදි ක්‍රමය පිළිබඳව වැඩි විස්තර සඳහා, විශේෂයෙන් ඔබ ආරම්භකයෙකු නම්, මෙම වෙනත් උපකාරකය අනුගමනය කිරීම ඉතාමත්ම නිර්දේශ කරමි:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Interface හි ඉහළින් පෙන්වන පණිවිඩය "*ඔබේ Wallet සුරකින්න...*" මත ක්ලික් කරන්න.


![Image](assets/fr/07.webp)


පසුව "*Save my Wallet*" මත ක්ලික් කරන්න.


![Image](assets/fr/08.webp)


පසුව "*View my key*" මත ක්ලික් කර ඔබේ Mnemonic වාක්‍යය භෞතික මාධ්‍යයක සුරකින්න.


![Image](assets/fr/09.webp)


Interface හි පහළින් ඇති කොටු දෙක සලකුණු කර, මූලාශ්‍ර පිටපත සාර්ථකව සම්පූර්ණ වී ඇති බව තහවුරු කරන්න.


![Image](assets/fr/10.webp)


## ඇප්ලිකේෂන් සැකසීම


ඔබේ පළමු ගනුදෙනු කිරීමට පෙර, Interface හි වම් පහළ කොනේ ඇති ගියර් රූපය ක්ලික් කිරීමෙන් සැකසුම් අභිරුචිකරණය කළ හැක.


![Image](assets/fr/11.webp)


"*Display*" මෙනුවේ, ඔබට යෙදුම් තේමාව, Bitcoin සඳහා භාවිතා කරන නාමය, සහ ඔබේ දේශීය ෆියට් මුදල් තෝරා ගත හැක.


![Image](assets/fr/12.webp)


"*ගෙවීම් විකල්ප*" හි, ඔබට Lightning ගෙවීම් සඳහා විවිධ උසස් සැකසුම් සොයා ගත හැක. ඔබට පෙරනිමි සැකසුම් තබා ගත හැක.


![Image](assets/fr/13.webp)


"*චැනල් කළමනාකරණය*" හි, ලයිට්නින් චැනල් එකක් විවෘත කිරීමේදී ගෙවීමට සූදානම් වන උපරිම ගාස්තුව සකසන්න.


![Image](assets/fr/14.webp)


"*ප්‍රවේශ පාලන*" මෙනුවේ, ඔබේ දුරකථනයේ යෙදුමට ප්‍රවේශය ආරක්ෂා කිරීමට සත්‍යාපන පද්ධතියක් සක්‍රීය කිරීමට මම දැඩිව නිර්දේශ කරමි. මෙය ඔබේ අන්ලොක් කළ දුරකථනයට ප්‍රවේශය ඇති ඕනෑම අයෙකුට Phoenix වෙත ප්‍රවේශ වීමෙන් සහ ඔබේ බිට්කොයින් සොරා ගැනීමෙන් වළක්වනු ඇත.


![Image](assets/fr/15.webp)


"*Electrum server*" මෙනුවේ, ඔබ Electrs සේවාදායකයෙකු ඇති නම්, ඔබට ඔබේ ගනුදෙනු විකාශය කිරීමට එය සම්බන්ධ කළ හැක.


![Image](assets/fr/16.webp)


ඔබේ සම්බන්ධතා වල රහස්‍යභාවය වැඩි දියුණු කිරීම සඳහා, "*Tor*" මෙනුවෙන් Tor හරහා සම්බන්ධතා සක්‍රීය කරන්න. Tor භාවිතා කිරීමෙන් ඔබේ ගෙවීම් ටිකක් මන්දගාමී විය හැකි අතර, ලැබීමේදී Phoenix යෙදුම ඉදිරිපසට විවෘතව තිබිය යුතු නමුත්, එය ඔබේ පෞද්ගලිකත්වය සැලකිය යුතු ලෙස වැඩි දියුණු කරයි.


![Image](assets/fr/17.webp)


## බිට්කොයින් ලබා ගන්න On-Chain


Ob prvem zagonu imate možnost naložiti svoj Phoenix Wallet z On-Chain sredstvi. Ta prvi polog lahko opravite tudi neposredno iz Lightning (glejte naslednji razdelek), vendar bodo v vsakem primeru veljale dodatne pristojbine za odprtje vašega prvega kanala.


"සමඟ *ලබා ගැනීම* බොත්තම මත ක්ලික් කරන්න."


![Image](assets/fr/18.webp)


Bitcoin ලැබීමේ ලිපිනයක් දැකීමට QR කේතය වමට ඇදන්න. ඔබ Phoenix වෙත තැන්පත් කිරීමට කැමති මුදල එම ලිපිනයට යවන්න.


![Image](assets/fr/19.webp)


On-Chain යටතේ ලැබුණු මුදල පළමුව ඔබේ පෝර්ට්ෆෝලියෝ ශේෂය යටතේ පENDING ලෙස පෙනේ. මුදල් භාවිතා කිරීමට ලබා ගත හැකි වීමට පෙර තහවුරු කිරීම් 3ක් ගත වේ.


![Image](assets/fr/20.webp)


රැකියාවන් ලැබුණු පසු, Phoenix ස්වයංක්‍රීයව ඔබ සඳහා Lightning නාලිකාවක් විවෘත කරයි. දැන් ඔබට Lightning Network හරහා බිට්කොයින් යැවීම සහ ලැබීම කළ හැක.


![Image](assets/fr/21.webp)


## ලයිට්නින්ග් හරහා බිට්කොයින් ලබා ගන්න


Lightning Network මඟින් Sats ලබා ගැනීමට, "*Receive*" බොත්තම ක්ලික් කරන්න.


![Image](assets/fr/22.webp)


Phoenix ustvari Lightning Invoice. Lahko ga skenirate ali pošljete osebi, ki želi prenesti Sats na vas.


![Image](assets/fr/23.webp)


"*සංස්කරණය*" බොත්තම ක්ලික් කිරීමෙන්, ඔබට Invoice මත ගෙවන්නාට පෙනෙන විස්තරයක් එක් කළ හැකි අතර, ගෙවන්නා යැවිය යුතු විශේෂිත මුදලක් නිර්වචනය කළ හැක.


![Image](assets/fr/24.webp)


ඉහත සඳහන් සම්භාව්‍ය ඉන්වොයිසයන් එක වරක් පමණක් භාවිතා කළ හැක. නැවත භාවිතා කළ හැකි ගෙවීම් විකල්පයක් සඳහා, ඔබේ නැවත භාවිතා කළ හැකි QR කේතය, එනම් BOLT12 යෝජනාව භාවිතා කළ හැක.


![Image](assets/fr/25.webp)


Ko Invoice ali BOLT12 යෝජනාව විසඳා ගෙන ඇති විට, ගනුදෙනුව ඔබේ Lightning Wallet මත පෙනෙනු ඇත.


![Image](assets/fr/26.webp)


## Lightning හරහා බිට්කොයින් යවන්න


Zdaj, ko imate Sats na Phoenixu, ste pripravljeni na plačila prek Lightning Network. Začnite s klikom na gumb "*Pošlji*".


![Image](assets/fr/27.webp)


ඔබට විවිධ විකල්ප ලබා ගත හැක. "*QR කේතය ස්කෑන් කරන්න*" මත ක්ලික් කිරීමෙන්, ඔබට Lightning Invoice, BOLT12 යෝජනාවක්, හෝ On-Chain ගෙවීම සඳහා Address ලැබීමක් පවා ස්කෑන් කළ හැක.


![Image](assets/fr/28.webp)


ඔබට මෙම තොරතුරු අතින්ම යතුරුපුවරුව හරහා Interface හි ඉහළින් ඇති ක්ෂේත්‍රයේ ඇතුළත් කළ හැක, හෝ Lightning Address (BOLT12 හෝ LNURL) ඇතුළත් කළ හැක. "*Paste*" බොත්තම භාවිතා කර තොරතුරු සෘජුවම අලවිය හැක.


![Image](assets/fr/29.webp)


Za ta primer sem skeniral Invoice za 10.000 Sats. Za izvedbo plačila preprosto kliknite na "*Plačaj*".


![Image](assets/fr/30.webp)


ගනුදෙනුව සම්පූර්ණයි.


![Image](assets/fr/31.webp)


සුභ පැතුම්, දැන් ඔබට Phoenix වින්‍යාස කිරීම සහ භාවිතා කිරීමේ ආකාරය දැනගන්නට ඇත. මෙම උපකාරිකාව ප්‍රයෝජනවත් වූවා නම්, පහත Green අඟුල් තබා මම කෘතඥ වෙමි. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බෙදා ගැනීම සඳහා ස්තුතියි!


To take things a step further, check out this tutorial on Alby Hub, another innovative and easy-to-use solution for launching your own Lightning node:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

ඉන්පසු Lightning Network හි තාක්ෂණික මෙහෙයුම පිළිබඳව වැඩිදුර දැන ගැනීමට, ඔබට Fanis Michalakisගේ විශිෂ්ට නොමිලේ පුහුණුව Plan ₿ Network මත සොයා ගත හැක:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb