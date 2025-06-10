---
name: CoinJoin - Samourai Wallet
description: Kako izvesti CoinJoin na Samourai Wallet?
---
![cover](assets/cover.webp)


***OPOZORILO:** Po aretaciji ustanoviteljev Samourai Wallet in zasegu njihovih strežnikov 24. aprila, orodje Whirlpool ne deluje več, tudi za posameznike, ki imajo svoj Dojo ali uporabljajo Sparrow Wallet. Vendar pa ostaja možnost, da bi to orodje lahko bilo ponovno vzpostavljeno v prihodnjih tednih ali ponovno zagnano na drugačen način. Poleg tega teoretični del tega članka ostaja relevanten za razumevanje načel in ciljev coinjoinov na splošno (ne samo Whirlpool), kot tudi za razumevanje učinkovitosti modela Whirlpool.*


_අපි මෙම සිද්ධියේ සංවර්ධන මෙන්ම සම්බන්ධිත මෙවලම් සම්බන්ධයෙන් සිදුවන සංවර්ධන ආසන්නයෙන් අනුගමනය කරමින් සිටිමු. නව තොරතුරු ලබා ගත හැකි වන විට මෙම උපකාරකය යාවත්කාලීන කරන බව විශ්වාසයෙන් කියමු._


_මෙම උපකාරිකාව අධ්‍යාපනික සහ තොරතුරුමය අරමුණු සඳහා පමණක් සපයනු ලැබේ. අපි මෙම මෙවලම් අපරාධමය අරමුණු සඳහා භාවිතා කිරීම අනුමත නොකරන අතර හෝ උනන්දු නොකරන අතරේ. තමන්ගේ නීතිමය බලප්‍රදේශයේ නීති පිළිපැදීමේ වගකීම සෑම පරිශීලකයෙකුගේම වගකීමයි._


---

> *a Bitcoin Wallet සඳහා වීථිවල*

මෙම උපකාරිකාවේ, ඔබ CoinJoin යනු කුමක්ද සහ Samourai Wallet මෘදුකාංගය සහ Whirlpool ක්‍රියාත්මක කිරීම භාවිතා කරමින් එය කෙසේ සිදු කරන බව ඉගෙන ගන්නාවා.


## Kaj je CoinJoin na Bitcoin?

**CoinJoin යනු Blockchain හි බිට්කොයින්වල සලකුණු හැරීම කඩන තාක්ෂණයකි**. එය ඒකම නමැති විශේෂිත ව්‍යුහයක් සහිත සහය transaction එකක් මත රඳා පවතී: CoinJoin transaction එක.


Coinjoins Bitcoin භාවිතා කරන්නන්ගේ පෞද්ගලිකත්වය වැඩි දියුණු කරයි, බාහිර නිරීක්ෂකයින් සඳහා දාම විශ්ලේෂණය සංකීර්ණ කරමින්. ඔවුන්ගේ ව්‍යුහය විවිධ භාවිතා කරන්නන්ගෙන් බොහෝ නානාවිධ කාසි එකම ගනුදෙනුවකට ඒකාබද්ධ කිරීමට ඉඩ සලසයි, එමඟින් පථ සඟවා, ආදාන සහ ප්‍රතිදාන ලිපින අතර සබඳතා තීරණය කිරීම අපහසු කරයි.


CoinJoin සම්මතය සහයෝගී ප්‍රවේශයකට පදනම්ව ඇත: ඔවුන්ගේ බිට්කොයින් මිශ්‍ර කිරීමට කැමති පරිශීලකයින් කිහිප දෙනෙකු එකම ගනුදෙනුවේ ආදාන ලෙස සමාන මුදල් තැන්පත් කරති. මෙම මුදල් පරිශීලකයෙකුට සමාන වටිනාකමකින් නිමාවූ ප්‍රතිදාන ලෙස නැවත බෙදා හැරේ. ගනුදෙනුව අවසානයේදී, ආදානයේ දැනටමත් පරිශීලකයෙකු සමඟ විශේෂිත ප්‍රතිදානයක් සම්බන්ධ කිරීම අසම්භාව්‍ය වේ. ආදාන සහ ප්‍රතිදාන අතර කිසිදු සෘජු සබැඳියක් නොමැති අතර, පරිශීලකයින් සහ ඔවුන්ගේ UTXO අතර සම්බන්ධතාවය, මෙන්ම සෑම කාසිමක ඉතිහාසයම බිඳ දැමේ.

![coinjoin](assets/notext/1.webp)


CoinJoin ගනුදෙනුවක උදාහරණයක් (මගින් නොවේ): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


CoinJoin ක්‍රියාවලියක් සිදු කිරීමේදී, සෑම පරිශීලකයෙකුම සිය මුදල් සෑම විටම පාලනය කරගෙන යාම සහතික කරමින්, ක්‍රියාවලිය ආරම්භ වන්නේ සම්බන්ධකයෙකු විසින් ගනුදෙනුව නිර්මාණය කිරීමෙන් වන අතර, එය පසුව සහභාගීවන්නන් වෙත සම්ප්‍රේෂණය කරයි. සෑම පරිශීලකයෙකුම පසුව, එය තමන්ට සුදුසු බව තහවුරු කිරීමෙන් පසු ගනුදෙනුවට අත්සන් කරයි. එකතු කළ සියලු අත්සන් අවසානයේ ගනුදෙනුවට ඒකාබද්ධ කරයි. පරිශීලකයෙකු හෝ සම්බන්ධකයෙකු විසින් CoinJoin ගනුදෙනුවේ ප්‍රතිදාන වෙනස් කිරීමෙන් මුදල් වංචා කිරීමට උත්සාහයක් කළහොත්, අත්සන් වලංගු නොවන බව පෙන්වනු ඇත, එවිට නෝඩයන් විසින් ගනුදෙනුව ප්‍රතික්ෂේප කරනු ඇත.


CoinJoin හි කීපයක් ක්‍රියාත්මක කිරීම් ඇත, උදාහරණ ලෙස Whirlpool, JoinMarket, හෝ Wabisabi, එක් එක් කටයුතුකරුවන් අතර සම්බන්ධතා කළමනාකරණය කිරීම සහ CoinJoin ගනුදෙනු වල කාර්යක්ෂමතාව වැඩි කිරීම අරමුණු කරගෙන.

මෙම උපකාරිකාවේ, අපි **Whirlpool** ක්‍රියාත්මක කිරීමේදී ගැඹුරු අවධානයක් යොමු කරමු, මම Bitcoin මත කෝයින්ජොයින්ස් කිරීමට ඇති කාර්යක්ෂමම විසඳුම ලෙස සැලකුවෙමි. කිහිපයක්ම වොලට්ස් මත ලබා ගත හැකි වුවද, මෙම උපකාරිකාවේදී, Dojo නොමැතිව Samourai Wallet ජංගම යෙදුම සමඟ එය භාවිතා කිරීම පමණක් අපි පරීක්ෂා කරමු.


## Zakaj izvajati coinjoins na Bitcoin?

සමහරක් සමකාලීන ගෙවීම් පද්ධති සමඟ ඇති ආරම්භක ගැටළුවක් වන්නේ ද්විත්ව වියදම් කිරීමයි: මධ්‍යස්ථ අධිකාරියක් මැදිහත් නොවී, දුෂ්ට පුද්ගලයින්ට එකම මූල්‍ය ඒකක කිහිප වතාවක් වියදම් කිරීම වැළැක්වීම කෙසේද?


Satoshi නකමොටෝ මෙම ගැටලුවට විසඳුමක් ලබා දුන්නේ Bitcoin ප්‍රොටෝකෝලය හරහා, මධ්‍යස්ථ අධිකාරියකින් ස්වාධීනව ක්‍රියාත්මක වන සමානාත්මක ඉලෙක්ට්‍රොනික ගෙවීම් පද්ධතියක් මඟිනි. ඔහුගේ සුදු කඩදාසියේ, ගෙවීම් පද්ධතිය තුළ සියලු ගනුදෙනු දැකිය හැකි බව සහතික කිරීම මඟින් ද්විත්ව වියදම් නොමැතිකම සහතික කිරීමේ එකම ක්‍රමය බව ඔහු අවධාරණය කරයි.


සෑම සහභාගිවන්නෙකුම ගනුදෙනු පිළිබඳව දැනුවත් වන බව සහතික කිරීම සඳහා, ඒවා මහජන වශයෙන් ප්‍රකාශයට පත් කළ යුතුය. එබැවින්, Bitcoin ක්‍රියාකාරීත්වය පෙනී පවතින සහ බෙදා හැරූ යටිතල පහසුකම් මත රඳා පවතින අතර, ඕනෑම නෝඩ් මෙහෙයුම්කරුට Miner විසින් නිර්මාණය කරන ලද සෑම කාසිමක ඉලෙක්ට්‍රොනික අත්සන දාම සහ ඉතිහාසය සම්පූර්ණයෙන්ම සනාථ කිරීමට ඉඩ සලසයි.


Bitcoin හි Blockchain හි පාරදෘශ්‍ය සහ බෙදා හැරීමේ ස්වභාවය යනු ඕනෑම ජාල පරිශීලකයෙකුට අනෙකුත් සියලුම සහභාගීවන්නන්ගේ ගනුදෙනු අනුගමනය කර විශ්ලේෂණය කළ හැකි බවයි. ප්‍රතිඵලයක් ලෙස, ගනුදෙනු මට්ටමේ අනන්‍යතාවය අසම්භාව්‍ය වේ. කෙසේ වෙතත්, පුද්ගලික හඳුනාගැනීම මට්ටමේදී අනන්‍යතාවය ආරක්ෂා කරයි. සම්භාව්‍ය බැංකු පද්ධතියේ සෑම ගිණුමක්ම පුද්ගල හඳුනාගැනීමකට සම්බන්ධ වන අතර, Bitcoin හිදී, මුදල් සංකේතමය යතුරු යුගල සමඟ සම්බන්ධ වන අතර, එමඟින් පරිශීලකයින්ට සංකේතමය හඳුනාගැනීම් පිටුපස පසුනම් අනන්‍යතාවයක් ලබා දේ.


ඒ අනුව, Bitcoin පිළිබඳ රහස්‍යතාවය බිඳ වැටේන්නේ බාහිර නිරීක්ෂකයින් විශේෂිත UTXO පරිශීලකයින් සමඟ සම්බන්ධ කිරීමට සමත් වන විටයි. මෙම සම්බන්ධතාවය ස්ථාපිත වූ විට, ඔවුන්ගේ ගනුදෙනු හඹා යාම සහ ඔවුන්ගේ බිට්කොයින් ඉතිහාසය විශ්ලේෂණය කිරීම සම්භවය වේ. CoinJoin යනු UTXO සලකුණු හැරීමේ තාක්‍ෂණයක් නිර්මාණය කරන ලද්දක් වන අතර, එමඟින් ගනුදෙනු මට්ටමේ Bitcoin පරිශීලකයින්ට විශේෂ Layer රහස්‍යතාවයක් ලබා දේ.


## Whirlpool කෙසේ ක්‍රියා කරයිද?

Whirlpool "_ZeroLink_" ගනුදෙනු භාවිතා කිරීමෙන් අනෙකුත් CoinJoin ක්‍රමවලින් වෙනස් වේ, එය සියලුම ආදාන සහ සියලුම නිමාවන් අතර තාක්ෂණික සබඳතාවක් නොමැති බව සහතික කරයි. මෙම පරිපූර්ණ මිශ්‍ර කිරීම, එක් එක් සහභාගිවන්නා ආදානයේ සමාන මුදලක් දායක වන ව්‍යුහයක් හරහා සම්පූර්ණ වේ (Mining ගාස්තු සඳහා හැර), එමඟින් සම්පූර්ණයෙන් සමාන මුදල් නිමාවන් ජනනය කරයි.

ආදාන සඳහා මෙම සීමාකාරී ආකෘතිය Whirlpool CoinJoin ගනුදෙනු සඳහා අනන්‍ය ලක්ෂණයක් ලබා දේ: ආදාන සහ ප්‍රතිදාන අතර නියමිත සබැඳි සම්පූර්ණයෙන්ම නොමැති වීම. වෙනත් වචන වලින් කියනවා නම්, ගනුදෙනුවේ අනෙකුත් සියලුම ප්‍රතිදාන සමඟ සසඳන විට, එක් එක් ප්‍රතිදානය ඕනෑම සහභාගිවන්නෙකුට පිරිනැමීමේ සමාන සම්භාවිතාවක් ඇත.

Na začetku je bilo število udeležencev v vsakem Whirlpool CoinJoin omejeno na 5, z 2 novima udeležencema in 3 remixerji (te koncepte bomo pojasnili kasneje). Vendar pa je povečanje transakcijskih provizij On-Chain, opaženo leta 2023, spodbudilo ekipe Samourai k ponovnemu premisleku o njihovem modelu za izboljšanje zasebnosti ob zmanjšanju stroškov. Tako lahko koordinator, upoštevajoč tržno situacijo provizij in število udeležencev, zdaj organizira coinjoin-e, ki vključujejo 6, 7 ali 8 udeležencev. Te izboljšane seje se imenujejo "_Surge Cycles_". Pomembno je omeniti, da ne glede na konfiguracijo v Whirlpool coinjoin-ih vedno sodelujeta le 2 nova udeleženca.


यसरी, Whirlpool लेनदेनहरू समान इनपुट र आउटपुटको संख्याद्वारा विशेषता हुन्छन्, जुन हुन सक्छ:


- 5 ආදාන සහ 5 ප්‍රතිදාන;

![coinjoin](assets/notext/2.webp)


- ආදාන 6 ක් සහ ප්‍රතිදාන 6 ක්;

![coinjoin](assets/notext/3.webp)


- 7 ආදාන සහ 7 ප්‍රතිදාන;

![coinjoin](assets/notext/4.webp)


- 8 ආදාන සහ 8 ප්‍රතිදාන.

![coinjoin](assets/notext/5.webp)

Whirlpool විසින් යෝජනා කරන ලද ආකෘතිය එබැවින් කුඩා CoinJoin ගනුදෙනු මත පදනම්ව ඇත. Wasabi සහ JoinMarket මෙන් නොව, එහි anonsets වල ශක්තිමත්කම තනි චක්‍රයක සහභාගීවන්නන්ගේ පරිමාව මත රඳා පවතින අතර, Whirlpool කුඩා ප්‍රමාණයේ චක්‍ර කිහිපයක් සම්බන්ධ කිරීම මත පදනම්ව පවතී.


මෙම ආකෘතියේ, පරිශීලකයාට මුලින්ම තටාකයකට ඇතුල්වීමේදී පමණක් ගාස්තු ගෙවීමට සිදුවේ, එමඟින් අමතර ගාස්තු නැතිව විවිධ රිමික්ස් වලට සහභාගී විය හැක. නව ඇතුල්වන්නන් රිමික්ස්කරුවන් සඳහා Mining ගාස්තු ආවරණය කරයි.


CoinJoin සමඟ එක් එක් අමතරයෙන්, නාණයක් සහභාගී වන සෑම අවස්ථාවකම, අතීතයේ හමුවූ එහි සමානවරුන් සමඟ, anonsets ගුණාත්මකව වර්ධනය වේ. එබැවින් අරමුණ වන්නේ මෙම නිදහස් රිමික්ස් වලින් ප්‍රයෝජනය ගැනීමයි, එය සෑම අවස්ථාවකම, එක් එක් මිශ්‍රිත නාණය සමඟ සම්බන්ධිත anonsets හි ඝනත්වය ශක්තිමත් කිරීමට දායක වේ.


Whirlpool යන්ත්‍රය නිර්මාණය කරන ලද්දේ වැදගත් අවශ්‍යතා දෙකක් සැලකිල්ලට ගනිමින්:


- Samourai Wallet යනු ප්‍රධාන වශයෙන් ස්මාර්ට්ෆෝන් යෙදුමක් වන බැවින්, ජංගම උපාංගවල ක්‍රියාත්මක කිරීමේ ප්‍රවේශය;
- රිමික්සින් සයිකල් වල වේගය අනොන්සෙට්ස් වල සාර්ථක වර්ධනයක් ප්‍රවර්ධනය කිරීමට.

මෙම අණපනත් Samourai Wallet සංවර්ධකයින් Whirlpool නිර්මාණය කිරීමේදී මඟ පෙන්වූ අතර, සයිකලයකට එක්වන පිරිසගේ සංඛ්‍යාව සීමා කිරීමට ඔවුන්ට හේතු විය. අඩු පිරිසක් එක්වීම CoinJoin කාර්යක්ෂමතාවයට බාධා කරනු ඇත, සෑම සයිකලයකදීම ජනිත වන anonsets ගණන දැඩිව අඩු කරනු ඇත, එසේම වැඩි පිරිසක් එක්වීම ජංගම යෙදුම් මත කළමනාකරණ ගැටළු ඇති කරනු ඇත සහ සයිකල් ප්‍රවාහය බාධා කරනු ඇත.

**අවසානයේ, Whirlpool මත CoinJoin සඳහා වැඩි පිරිසක් අවශ්‍ය නොවේ, මන්ද CoinJoin චක්‍ර කිහිපයක් එකතු කිරීමෙන් අනොන්සෙට්ස් ලබා ගත හැකි බැවිනි.**


[-> Whirlpool anonsets පිළිබඳව වැඩිදුරටත් ඉගෙන ගන්න.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### පිහිනුම් තටාක සහ CoinJoin ගාස්තු

මෙම බහු චක්‍ර සාර්ථකව මිශ්‍ර කරන ලද නාණයවල anonsets වැඩි කිරීමට, UTXO භාවිතා කරන ප්‍රමාණ සීමා කිරීමට විශේෂිත රාමුවක් ස්ථාපිත කළ යුතුය. Whirlpool එබැවින් විවිධ තටාක අර්ථ දක්වයි.


පිහිනුම් තටාකයක් යනු එකට මිශ්‍ර වීමට කැමති පරිශීලක කණ්ඩායමක් නිරූපණය කරන අතර, CoinJoin ක්‍රියාවලිය උපරිම කිරීමට UTXO ප්‍රමාණය පිළිබඳ එකඟ වේ. එක් එක් පිහිනුම් තටාකය UTXO සඳහා ස්ථිර ප්‍රමාණයක් නියම කර ඇති අතර, සහභාගී වීමට පරිශීලකයා එයට අනුකූල විය යුතුය. එබැවින්, Whirlpool සමඟ කාසියන් එක් කිරීමට, ඔබට පිහිනුම් තටාකයක් තෝරා ගත යුතුය. දැනට ලබා ගත හැකි පිහිනුම් තටාක පහත පරිදි වේ:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100,000 Sats).


ඔබේ බිට්කොයින් සමඟ පොකුරකට එක්වීමෙන්, ඒවා වෙනත් සහභාගීවන්නන්ගේ ඒවා සමඟ සම්පූර්ණයෙන් සමාන generate UTXO ලෙස බෙදා හරිනු ලැබේ. එක් එක් පොකුරකට උපරිම සීමාවක් ඇත; එබැවින්, මෙම සීමාව ඉක්මවන මුදල් සඳහා, ඔබට එකම පොකුර තුළ වෙන්වූ ඇතුළත් කිරීම් දෙකක් කිරීමට හෝ වැඩි මුදලක් සහිත වෙනත් පොකුරක් වෙත ඔබේ අවධානය යොමු කිරීමට බල කෙරේ:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

පෙර සඳහන් කළ පරිදි, UTXO එකක් CoinJoin එකකට ඒකාබද්ධ කිරීමට සූදානම් වන විට එය තටාකයකට අයත් වේ යැයි සැලකේ. කෙසේ වෙතත්, මෙය පරිශීලකයා එය අහිමි කර ගන්නා බව අර්ථ නොදක්වයි. **විවිධ මිශ්‍රණ චක්‍රාන්විතයන් හරහා, ඔබේ යතුරු සහ, ප්‍රතිඵලයක් ලෙස, ඔබේ බිට්කොයින් සම්පූර්ණයෙන්ම පාලනය කරගෙන යාමට ඔබට හැකිය.** මෙය CoinJoin තාක්ෂණය වෙනත් මධ්‍යස්ථ මිශ්‍රණ තාක්ෂණවලින් වෙනස් කරයි.


CoinJoin කුළුවට ඇතුල් වීමට, සේවා ගාස්තු මෙන්ම Mining ගාස්තුද ගෙවිය යුතුය. සේවා ගාස්තු සෑම කුළුවකටම ස්ථිර වන අතර Whirlpool සංවර්ධනය සහ නඩත්තු කිරීම සඳහා වගකියන කණ්ඩායම් සඳහා වන්දි ගෙවීමේ අරමුණින් වේ.

Whirlpool භාවිතා කිරීම සඳහා සේවා ගාස්තු තටාකයට ඇතුල්වීමේදී එක වරක් පමණක් ගෙවිය යුතුය. මෙම පියවරෙන් පසු, ඔබට අමතර ගාස්තු නැතිව සීමාවක් නොමැතිව රිමික්ස් වලට සහභාගී වීමට අවස්ථාව ඇත. මෙන්න එක් එක් තටාකය සඳහා වර්තමාන ස්ථිර ගාස්තු:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


මෙම ගාස්තු මූලික වශයෙන්ම තෝරාගත් තටාකය සඳහා ප්‍රවේශ පත්‍රයක් ලෙස ක්‍රියා කරයි, ඔබ CoinJoin තුළ දැමූ මුදල නොසලකා හරිමින්. එබැවින්, ඔබ 0.01 BTC සමඟ නිවැරදිව 0.01 තටාකයට එක්වුවද, 0.5 BTC සමඟ එයට ඇතුළත් වුවද, ගාස්තු නිරපේක්ෂ වශයෙන් එකසේ පවතී.


පෙර යන්න coinjoins, පරිශීලකයාට එබැවින් තේරීමක් ඇත 2 යාන්ත්‍රණ අතර:


- සෙවිකා ගාස්තු අවම කිරීම සඳහා කුඩා තටාකයක් තෝරන්න, ඔවුන්ට ප්‍රතිඵලයක් ලෙස කුඩා UTXO කිහිපයක් ලැබෙන බව දැනගෙන;
- Ali pa raje večji bazen, pri čemer se strinjate z višjimi pristojbinami, da bi na koncu imeli zmanjšano število UTXO-jev z večjo vrednostjo.


CoinJoin චක්‍රාන්තරයෙන් පසු මිශ්‍ර UTXO කිහිපයක් එක් කිරීමෙන් වළකින්නැයි සාමාන්‍යයෙන් උපදෙස් දෙන අතර, මෙය Common-Input-Ownership Heuristic (CIOH) නිසා ලබාගත් රහස්‍යභාවය අවදානමට ලක් විය හැක. එබැවින්, වැඩි මුදලක් ගෙවීමට සිදු වුවත්, ප්‍රතිදානය ලෙස අතිශය කුඩා වටිනාකම් ඇති UTXO නොමැතිවීම සඳහා විශාලතම තටාකයක් තෝරා ගැනීම බුද්ධිමත් විය හැක. පරිශීලකයාට ඔවුන් කැමති තටාකය තෝරා ගැනීම සඳහා මෙම妥協යන් තරයේ සලකා බැලිය යුතුය.


සේවා ගාස්තු වලට අමතරව, ඕනෑම Bitcoin ගනුදෙනුවකට අන්තර්ගත Mining ගාස්තු ද සලකා බැලිය යුතුය. Whirlpool පරිශීලකයෙකු ලෙස, ඔබට සකස් කිරීමේ ගනුදෙනුව (`Tx0`) සඳහා Mining ගාස්තු ගෙවීමට ද, පළමු CoinJoin සඳහා ද අවශ්‍ය වේ. Whirlpool මෝඩලය නව ප්‍රවේශකයින්ගේ ගෙවීම් මත රඳා පවතින බැවින්, ඉන්පසු සිදුවන සියලුම නැවත මිශ්‍ර කිරීම් නොමිලේ වේ.


ඇත්ත වශයෙන්ම, සෑම Whirlpool CoinJoin හිම, ආදාන අතර නව ප්‍රවේශකයන් දෙදෙනෙකු සිටී. අනෙකුත් ආදාන රිමික්සර්වරුන්ගෙන් පැමිණේ. එම නිසා, ගනුදෙනුවේ සියලුම සහභාගීවන්නන් සඳහා Mining ගාස්තු මෙම නව සහභාගීවන්නන් දෙදෙනා විසින් ආවරණය කරනු ලබන අතර, ඔවුන්ටද නිදහස් රිමික්ස් වලින් ප්‍රයෝජනයක් ලැබේ:

![coinjoin](assets/en/6.webp)

මෙම ගාස්තු පද්ධතියට ස්තූතියි, Whirlpool සැබවින්ම වෙනස් වේ CoinJoin සේවාවන්ගෙන්, UTXO වල anonsets පරිශීලකයා විසින් ගෙවනු ලබන මිලට සමානුපාතික නොවන බැවින්. එබැවින්, තටුකාරකයේ ප්‍රවේශ ගාස්තුව සහ ගනුදෙනු දෙකක් සඳහා Mining ගාස්තු ( `Tx0` සහ ආරම්භක මිශ්‍රණය) පමණක් ගෙවා ඉතා ඉහළ මට්ටමේ අනන්‍යතාවයක් ලබා ගැනීමේ හැකියාව ඇත.

Mining ගාස්තු ආවරණය කිරීම සඳහා පරිශීලකයාට ඔවුන්ගේ UTXOs මුල්‍ය එකතුවෙන් ඉවත් කිරීමටත්, ඔවුන්ගේ බහු කෝයින්ජොයින්ස් සම්පූර්ණ කිරීමෙන් පසු, `mix to` විකල්පය තෝරා නොමැති නම්, එය සටහන් කර ගැනීම වැදගත්ය, අපි පහත උපකාරකයෙහි සාකච්ඡා කරමු.


### HD Wallet ගිණුම් Whirlpool විසින් භාවිතා කරන ලදී.

Whirlpool හරහා CoinJoin ක්‍රියාත්මක කිරීමට, Wallet ට generate විවිධ ගිණුම් කිහිපයක් අවශ්‍ය වේ. HD (*Hierarchical Deterministic*) Wallet සන්දර්භය තුළ ගිණුමක් යනු අනෙකුත් සියල්ලෙන් සම්පූර්ණයෙන්ම වෙන්වූ කොටසක් වන අතර, මෙම වෙන්වීම සිදුවන්නේ Wallet හි පරිපාටියේ තුන්වන ගැඹුරු මට්ටමේදී, එනම් `xpub` මට්ටමේදීය.


HD Wallet lahko teoretično izpelje do `2^(32/2)` različnih računov. Začetni račun, ki se privzeto uporablja na vseh Bitcoin denarnicah, ustreza indeksu `0'`.


Za denarnice, prilagojene za Whirlpool, kot sta Samourai ali Sparrow, se uporabljajo 4 računi za izpolnjevanje potreb procesa CoinJoin:


- **ඇපකිරීම** ගිණුම, `0'` දර්ශකය මගින් හඳුනාගෙන ඇත;
- **බැඩ් බැංකුව** (හෝ ඩොක්සික් වෙනස) ගිණුම, `2 147 483 644'` දර්ශකය මඟින් හඳුනාගෙන ඇත;
- **premix** ගිණුම, `2 147 483 645'` දර්ශකය මඟින් හඳුනාගෙන ඇත;
- **postmix** ගිණුම, `2 147 483 646'` දර්ශකය මගින් හඳුනාගෙන ඇත.


CoinJoin ක්‍රියාවලියේදී මෙම ගිණුම් එක් එක්ව විශේෂිත කාර්යයක් ඉටු කරයි.


මෙම ගිණුම් සියල්ල seed එකකට සම්බන්ධ වී ඇති අතර, පරිශීලකයාට ඔවුන්ගේ බිට්කොයින් සියල්ල නැවත ලබා ගැනීමට ඔවුන්ගේ නැවත ලබා ගැනීමේ වාක්‍යය සහ, අදාළ නම්, ඔවුන්ගේ passphrase භාවිතා කිරීමට ඉඩ සලසයි. කෙසේ වෙතත්, මෙම නැවත ලබා ගැනීමේ මෙහෙයුම දුරාන්විත සොෆ්ට්වෙයාර් වෙත භාවිතා කරන ලද විවිධ ගිණුම් දර්ශක විශේෂිත කිරීම අවශ්‍ය වේ.


අපි දැන් මෙම ගිණුම් තුළ Whirlpool CoinJoin හි විවිධ අදියරවල් බලමු.


### Whirlpool මත coinjoins හි විවිධ අදියරන්

**පළමු අදියර: Tx0**

Whirlpool CoinJoin එකක ආරම්භක ස්ථානය වන්නේ **තැන්පතු** ගිණුමයි. නව Bitcoin Wallet එකක් නිර්මාණය කරන විට ඔබ ස්වයංක්‍රීයව භාවිතා කරන ගිණුම මෙය වේ. මිශ්‍ර කිරීමට කැමති බිට්කොයින් මෙම ගිණුමට ණය කළ යුතුය.

`Tx0` යනු Whirlpool මිශ්‍රණ ක්‍රියාවලියේ පළමු පියවර නිරූපණය කරයි. එය UTXO, CoinJoin සඳහා සකස් කිරීම සහ සමාන කිරීම අරමුණු කර ගනී, තෝරාගත් තටාකයේ ප්‍රමාණයට අනුකූල ඒකකවලට ඒවා බෙදා, මිශ්‍රණයේ සමජාතිකභාවය සහතික කිරීම සඳහා. සමාන කළ UTXO පසුව **පූර්ව මිශ්‍රණ** ගිණුමට යවනු ලැබේ. තටාකයට ඇතුල් විය නොහැකි වෙනසක් සම්බන්ධයෙන්, එය විශේෂිත ගිණුමකට වෙන් කරනු ලැබේ: **නරක බැංකුව** (හෝ "doxxic change").

මෙම ආරම්භක ගනුදෙනුව `Tx0` මාර්ගය සම්බන්ධකයාට ගෙවිය යුතු සේවා ගාස්තු විසඳීමටද සේවය කරයි. පසුගිය පියවරවලට වඩා වෙනස්ව, මෙම ගනුදෙනුව සහයෝගී නොවේ; එබැවින් පරිශීලකයා සියලුම Mining ගාස්තු භාරගත යුතුය:

![coinjoin](assets/en/7.webp)


මෙම `Tx0` ගනුදෙනුවේ උදාහරණයක, අපගේ **තැන්පතු** ගිණුමෙන් `372,000 Sats` ක ආදානයක් UTXO ලෙස විවිධ නිමැවුම් ලෙස බෙදා හැරේ, එය පහත පරිදි බෙදා හැරේ:


- `100,000 Sats` සඳහා කූළයේ ප්‍රවේශය සඳහා අදාළ සේවා ගාස්තු සඳහා සම්බන්ධකරුට අදහස් කරන `5,000 Sats` මුදලක්;
- Three UTXO prepared for mixing, redirected to our **premix** account and registered with the coordinator. These UTXO are equalized at `108,000 Sats` each, to cover the Mining fees for their future initial mix;
- අමතරය, පොකුරට ඇතුල් විය නොහැකි, කුඩා වීම නිසා, විෂ සහිත වෙනසක් ලෙස සැලකේ. එය එහි විශේෂිත ගිණුමට යවනු ලැබේ. මෙහිදී, මෙම වෙනස `40,000 Sats` වේ;
- අවසානයේ, `3,000 Sats` යන ඒවා ප්‍රතිදානයක් නොවන නමුත් `Tx0` තහවුරු කිරීමට අවශ්‍ය Mining ගාස්තු වේ.


උදාහරණයක් ලෙස, මෙන්න සත්‍ය Whirlpool Tx0 (මගින් නොවේ): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**පියවර 2: doxxic වෙනස**

අමතරය, එය තටාකයට ඒකාබද්ධ කළ නොහැකි වූ, මෙහි `40,000 Sats` සමාන වන අතර, **නරක බැංකු** ගිණුමට යළි යොමු කරනු ලබයි, "doxxic change" ලෙසද හැඳින්වේ, අනෙකුත් UTXO වලින් Wallet තුළ දැඩි වෙන් කිරීමක් සහතික කිරීම සඳහා.


Ta UTXO je nevaren za zasebnost uporabnika, saj ni le še vedno povezan s svojo preteklostjo in s tem morda z identiteto svojega lastnika, ampak je dodatno označen kot pripadajoč uporabniku, ki je izvedel CoinJoin.

Če se ta UTXO združi z mešanimi izhodi, bodo izgubili vso zaupnost, pridobljeno med cikli CoinJoin, zlasti zaradi Common-Input-Ownership-Heuristic (CIOH). Če se združi z drugimi doxxic spremembami, uporabnik tvega izgubo zaupnosti, saj bo to povezalo različne vnose ciklov CoinJoin. Zato je treba ravnati previdno. Način upravljanja s tem toksičnim UTXO bo podrobno opisan v zadnjem delu tega članka, prihodnji vodiči pa bodo te metode podrobneje obravnavali na PlanB Network.


**පියවර 3: ආරම්භක මිශ්‍රණය**

`Tx0` සම්පූර්ණ වූ පසු, සමාන කළ UTXOs අපගේ Wallet හි **premix** ගිණුමට යවනු ලබන අතර, ඒවා ඔවුන්ගේ පළමු CoinJoin චක්‍රය, "මුල් මිශ්‍රණය" ලෙසද හැඳින්වෙයි, වෙත හඳුන්වා දීමට සූදානම් වේ. අපගේ උදාහරණයේ පරිදි, `Tx0` මිශ්‍ර කිරීම සඳහා බහු UTXOs ජනනය කරන්නේ නම්, ඒවායේ එක් එක් එකක් වෙන වෙනම මුල් CoinJoin වෙත ඒකාබද්ධ කෙරේ.


මෙම පළමු මික්ස් අවසානයේදී, **premix** ගිණුම හිස් වන අතර, මෙම පළමු CoinJoin සඳහා Mining ගාස්තු ගෙවා ඇති අපගේ කාසි, තෝරාගත් තටාකය විසින් නිර්වචිත මුදලට සෘජුවම සකස් කරනු ලැබේ. අපගේ උදාහරණයේ, අපගේ ආරම්භක UTXOs `108 000 Sats` ලෙසින් `100 000 Sats` දක්වා සෘජුවම අඩු කර ඇත.

![coinjoin](assets/en/8.webp)

**පියවර 4: නැවත මිශ්‍ර කිරීම්**

මුල් මිශ්‍රණයෙන් පසු, UTXO මාරු කරනු ලබන්නේ **postmix** ගිණුමටය. මෙම ගිණුම දැනටමත් මිශ්‍රණය කළ UTXO සහ නැවත මිශ්‍රණය සඳහා බලාපොරොත්තු වන UTXO එකතු කරයි. Whirlpool පාරිභෝගිකයා සක්‍රීය වන විට, **postmix** ගිණුමේ UTXO ස්වයංක්‍රීයව නැවත මිශ්‍රණය සඳහා ලබා ගත හැකි අතර මෙම නව චක්‍රවලට සහභාගී වීමට අහඹු ලෙස තෝරා ගනු ලැබේ.


සමහර විට, මතක් කිරීමක් ලෙස, නැවත මිශ්‍ර කිරීම් 100% නොමිලේ වේ: අමතර සේවා ගාස්තු හෝ Mining ගාස්තු අවශ්‍ය නොවේ. **පෝස්ට්මික්ස්** ගිණුම තුළ UTXOs තබා ගැනීමෙන් ඔවුන්ගේ වටිනාකම අඛණ්ඩව පවත්වාගෙන යාමට සහ ඔවුන්ගේ අනෝන්සෙට්ස් වැඩි දියුණු කිරීමට එකවරම උපකාරී වේ. එබැවින් මෙම කාසි බහු CoinJoin චක්‍රවලට සහභාගී වීමට ඉඩ දීම වැදගත් වේ. එය ඔබට කිසිවක් වැය නොවේ, සහ එය ඔවුන්ගේ අනන්‍යතාව මට්ටම් වැඩි කරයි.


ඔබ මිශ්‍ර UTXOs වියදම් කිරීමට තීරණය කරන විට, ඔබට එය මෙම **postmix** ගිණුමෙන් සෘජුවම කළ හැක. නිදහස් නැවත මිශ්‍ර කිරීම් වලින් ප්‍රයෝජන ගැනීමට සහ ඔවුන්ගේ රහස්‍යතාව අඩු කළ හැකි Whirlpool පරිපථයෙන් පිටවීම වැළැක්වීමට මිශ්‍ර UTXOs මෙම ගිණුම තුළ තබා ගැනීම සුදුසුය.


ජාතික අපේක්ෂාවන්ට අනුව, අපි පසුපසින් දැක්වෙන උපකාරකය තුළ දැක බලා ගන්නා පරිදි, `mix to` විකල්පය ද ඇත, එය ඔබේ මිශ්‍ර කළ කාසි ස්වයංක්‍රීයව වෙනත් Wallet, උදාහරණයක් ලෙස Cold Wallet වෙත යැවීමේ හැකියාව ලබා දේ, කාසි එකතු කිරීම් ගණනක් නිර්වචනය කිරීමෙන් පසු.

සම්මුඛ Wallet ඇන්ඩ්‍රොයිඩ් යෙදුම හරහා Whirlpool භාවිතා කිරීම පිළිබඳ උපකාරක පසුගිය සංකල්පය ආවරණය කිරීමෙන් පසු, දැන් පුහුණුවට පිවිසෙමු!


## අනුපිළිවෙල: CoinJoin Whirlpool මත Samourai Wallet

Whirlpool භාවිතා කිරීම සඳහා විවිධ විකල්ප ඇත. මෙහි මම හඳුන්වා දෙන්නට කැමති Wallet විකල්පය Samourai (Dojo නොමැතිව), Android මත විවෘත මූලාශ්‍ර Bitcoin Wallet කළමනාකරණ යෙදුමකි.


Dojo නොමැතිව Samourai මත මිශ්‍ර කිරීමේ වාසිය වන්නේ එය අතිශය පහසුවෙන් කළමනාකරණය කළ හැකි අතර, ඉක්මනින් පිහිටුවිය හැකි අතර, Android දුරකථනයක් සහ අන්තර්ජාල සම්බන්ධතාවයක් හැර වෙනත් උපාංගයක් අවශ්‍ය නොවන බවයි.


Vendar pa ima ta metoda dve pomembni pomanjkljivosti:


- Coinjoins केवल तभी होंगे जब Samourai पृष्ठभूमि में चल रहा हो और कनेक्टेड हो। इसका मतलब है कि यदि आप अपने बिटकॉइन्स को 24/7 मिक्स और रीमिक्स करना चाहते हैं, तो आपको लगातार Samourai को चालू रखना होगा;
- ඔබේම Dojo එක සම්බන්ධ කිරීමට ප්‍රවේශම් නොවී Whirlpool සමඟ Samourai Wallet භාවිතා කළහොත්, ඔබේ යෙදුම Samourai කණ්ඩායම් විසින් නඩත්තු කරන සේවාදායකය වෙත සම්බන්ධ වීමට සිදු වන අතර, ඔබේ Wallet හි `xpub` ඔවුන්ට අනාවරණය වනු ඇත. ඔබේ ගනුදෙනු සොයා ගැනීමට ඔබේ යෙදුම සඳහා මෙම අනන්‍ය තොරතුරු අවශ්‍ය වේ.


මෙම සීමා ජය ගැනීමට අදාළ හොඳම විසඳුම වන්නේ ඔබේම Dojo එකක්, Whirlpool CLI අවස්ථාවක් සමඟ, ඔබේ පුද්ගලික Bitcoin නියමක මත ක්‍රියාත්මක කිරීමයි. මෙලෙසින්, ඔබට කිසිදු තොරතුරු කාන්දුවක් වළක්වා, සම්පූර්ණ ස්වාධීනත්වයක් ලබා ගත හැකිය. පහත දැක්වෙන උපකාරකය විශේෂිත ඉලක්ක සඳහා හෝ ආරම්භකයින් සඳහා ප්‍රයෝජනවත් වුවත්, ඔබේ CoinJoin සැසිය සත්‍යයෙන්ම උපරිම කිරීමට, ඔබේම Dojo එකක් භාවිතා කිරීම නිර්දේශිත වේ. මෙම වින්‍යාසය පිහිටුවීම පිළිබඳ විස්තරාත්මක මාර්ගෝපදේශයක් PlanB ජාලය මත ඉක්මනින් ලබා ගත හැකි වේ.


### Samourai Wallet ස්ථාපනය කිරීම

Za začetek boste seveda potrebovali aplikacijo Samourai Wallet. Lahko jo prenesete neposredno z uradne spletne strani z uporabo APK-ja, iz njihovega GitLaba ali iz trgovine Google Play Store.


### Software Wallet සෑදීම

මෘදුකාංගය ස්ථාපනය කිරීමෙන් පසු, ඔබට Samourai මත Bitcoin Wallet එකක් නිර්මාණය කිරීමට ඉදිරියට යාමට අවශ්‍ය වේ. ඔබට දැනටමත් එකක් තිබේ නම්, ඔබට ඊළඟ පියවරට සෘජුවම පැනිය හැක.


កម្មវិធីត្រូវបានបើកឡើង, ចុចប៊ូតុង `Start` ពណ៌ខៀវ។ បន្ទាប់មកអ្នកនឹងត្រូវបានស្នើឱ្យជ្រើសរើសទីតាំងមួយនៅក្នុងឯកសារទូរស័ព្ទរបស់អ្នកដែលការបម្រុងទុកដែលបានអ៊ិនគ្រីបនៃ Wallet ថ្មីរបស់អ្នកនឹងត្រូវបានរក្សាទុក។


![samourai](assets/notext/9.webp)

ටෝර් සක්‍රීය කිරීමට සමාන කණුව මත ක්ලික් කරන්න. මෙම අවස්ථාවේදී, ඔබට විශේෂිත ඩොජෝ එකක් තෝරා ගැනීමේ විකල්පය ද ඇත. කෙසේ වෙතත්, මෙම උපකාරක පාඩමෙන්, අපි පෙරනිමි ඩොජෝ සමඟ දිගටම යමු; එබැවින් ඔබට විකල්පය අක්‍රීය කළ හැක. ටෝර් සම්බන්ධ වූ විට, `නව Wallet එකක් සාදන්න` බොත්තම ඔබන්න.

![samourai](assets/notext/10.webp)


Samourai Wallet nato vas pozove, da nastavite BIP39 passphrase. To dodatno geslo je zelo pomembno, saj neposredno vpliva na izpeljavo vaših zasebnih ključev. Možna izguba tega passphrase bi povzročila nezmožnost dostopa do vaših bitcoinov, zaradi česar bi bili nepopravljivo izgubljeni. Za obnovitev vašega Samourai Wallet je nujno imeti tako vašo 12-besedno obnovitveno frazo kot tudi passphrase.


එබැවින්, ශක්තිමත් passphrase තෝරා ගැනීම සහ ඔබේ බිට්කොයින් ආරක්ෂාව සහතික කිරීම සඳහා කඩදාසි මත හෝ ලෝහ මාධ්‍යයක මත එක් හෝ වැඩි ගණනක් භෞතික පිටපත් සෑදීම අත්‍යවශ්‍ය වේ. මෙම කාර්යයන් අවසන් කිරීමෙන් පසු, `මම අහිමි වීමේ අවස්ථාවේ දැනුවත් වෙමි...` කොටුවට ලකුණු කර, `NEXT` බොත්තම ඔබන්න.


![samourai](assets/notext/11.webp)


ඔබට පසුව අංක 5 සිට 8 දක්වා අංකයන්ගෙන් සමන්විත PIN කේතයක් නිර්වචනය කළ යුතුය. මෙම කේතය ඔබේ දුරකථනයේ Wallet වෙත ප්‍රවේශය ආරක්ෂා කරනු ඇත. ඔබට Samourai යෙදුම විවෘත කිරීමට අවශ්‍ය සෑම විටම එය ඉල්ලා සිටිනු ඇත. ශක්තිමත් PIN කේතයක් තෝරා ගන්නා අතර මතක තබා ගැනීම සඳහා පිටපතක් තබා ගැනීමට වග බලා ගන්න. එවිට, ඔබට `NEXT` බොත්තම ඔබන්න පුළුවන්.


![samourai](assets/notext/12.webp)


Samourai ඔබට තහවුරු කිරීම සඳහා ඔබේ PIN කේතය නැවත ඇතුළත් කිරීමට ආරාධනා කරනු ඇත. එය ඇතුළත් කර, පසුව `FINALIZE` ඔබන්න.


![samourai](assets/notext/13.webp)


Nato boste dostopali do svoje obnovitvene fraze, sestavljene iz 12 besed. Ta fraza vam omogoča obnovitev vašega Wallet s prej vnesenim passphrase. Močno priporočamo, da naredite eno ali več kopij te fraze na fizičnih medijih, kot so papir ali kovinski material, da zagotovite varnost vaših bitcoinov v primeru težave.


මෙම උපස්ථිතියන් සෑදීමෙන් පසු, ඔබේ නව Samourai Wallet හි Interface වෙත ඔබ නියම වේ.


![samourai](assets/notext/14.webp)


ඔබට ඔබේ PayNym Bot ලබා ගැනීමට අවස්ථාවක් ඇත. ඔබට අවශ්‍ය නම් එය ඉල්ලා සිටිය හැක, එහෙත් එය අපගේ උපකාරක පංතිය සඳහා අත්‍යවශ්‍ය නොවේ.


![samourai](assets/notext/15.webp)

Wallet මත බිට්කොයින් ලබා ගැනීමට පෙර, ඔබේ Wallet ආපසුගත කිරීම් (passphrase සහ ප්‍රතිසාධන වාක්‍යය) වල වලංගුභාවය නැවත පරීක්ෂා කිරීම දැඩිව නිර්දේශ කරයි. passphrase සත්‍යතාවය තහවුරු කිරීමට, තිරයේ ඉහළ වමට පිහිටි ඔබේ PayNym Bot හි අයිකනය තෝරා, පසුව මාර්ගය අනුගමනය කළ හැක:

```plaintext
Settings > Troubleshooting > Passphrase/backup test
```


ඔබේ passphrase ඇතුළත් කර සත්‍යාපනය සිදු කරන්න.


![samourai](assets/notext/16.webp)


Samourai බලාපොරොත්තු වන්නේ එය වලංගුදැයි තහවුරු කිරීමට.


![samourai](assets/notext/17.webp)


ඔබේ ප්‍රතිසාධන වාක්‍යයේ පිටපත සත්‍යාපනය කිරීමට, තිරයේ ඉහළ වමට පිහිටි ඔබේ PayNym Bot අයිකනයට ප්‍රවේශ වන්න, සහ මෙම මාර්ගය අනුගමනය කරන්න:

```plaintext
Settings > Wallet > Show 12-word recovery phrase
```


Samourai ඔබේ ප්‍රතිසාධන වාක්‍යය සමඟ කවුළුවක් පෙන්වනු ඇත. එය ඔබේ භෞතික ආපසු සුරැකුම සමඟ සමාන බවට වග බලා ගන්න.


ඉදිරියට ගොස් සම්පූර්ණ ප්‍රතිසාධන පරීක්ෂණයක් සිදු කිරීමට, ඔබේ Wallet හි සාක්ෂිකරු මූලද්‍රව්‍යයක් සටහන් කරන්න, උදාහරණයක් ලෙස `xpubs` එකක්, එවිට ඔබේ Wallet මකන්න (එය තවමත් හිස් නම්). ඉලක්කය වන්නේ ඔබේ භෞතික ආපස්සටු පමණක් භාවිතා කරමින් මෙම හිස් Wallet නැවත පිහිටුවීමට උත්සාහ කිරීමයි. නැවත පිහිටුවීම සාර්ථක නම්, එය ඔබේ ආපස්සටු වලංගු සහ විශ්වාසනීය බව පෙන්වයි.


### බිට්කොයින් ලබා ගැනීම

ඔබේ Wallet නිර්මාණය කිරීමෙන් පසු, ඔබ `0'` දර්ශකය මඟින් හඳුනාගත් තනි ගිණුමකින් ආරම්භ කරනු ඇත. මෙය අපි පෙර කොටස්වලදී කතා කළ **තැන්පතු** ගිණුමයි. කෝයින්ජොයින් සඳහා අදහස් කරන බිට්කොයින් මෙම ගිණුමට මාරු කිරීමට ඔබට අවශ්‍ය වේ.


මෙය කිරීමට, තිරයේ දකුණු පහළ කොටසේ පිහිටි නිල් `+` සංකේතය මත ක්ලික් කරන්න.


![samourai](assets/notext/18.webp)


පසුව Green `Receive` බොත්තම ක්ලික් කරන්න.


![samourai](assets/notext/19.webp)


Samourai bo samodejno generate nov prazen Address za prejemanje bitcoinov.


![samourai](assets/notext/20.webp)


ඔබට බිට්කොයින් මිශ්‍ර කිරීමට එතැනට යැවිය හැක.


![samourai](assets/notext/21.webp)


### Tx0 නිර්මාණය කිරීම

කියමන් තහවුරු වූ විට, අපට coinjoins ක්‍රියාවලිය ආරම්භ කළ හැක. මෙය කිරීමට, තිරයේ දකුණු පහළ කොටසේ ඇති නිල් `+` බොත්තම ක්ලික් කරන්න.


![samourai](assets/notext/22.webp)


පසුව නිල් වර්ණයෙන් ඇති `Whirlpool` මත ක්ලික් කරන්න.


![samourai](assets/notext/23.webp)


Whirlpool ආරම්භ වන තුරු සහ Samourai අවශ්‍ය ගිණුම් නිර්මාණය කරන තුරු රැඳී සිටින්න.


![samourai](assets/notext/24.webp)


ඔබ එවිට Whirlpool මුල් පිටුවට පැමිණෙනු ඇත. `Start` මත ක්ලික් කරන්න.

![samourai](assets/notext/25.webp)

CoinJoin චක්‍රවලවලට යැවීමට ඔබට අවශ්‍ය **තැන්පතු** ගිණුමෙන් UTXO තෝරන්න, පසුව `Next` මත ක්ලික් කරන්න.


![samourai](assets/notext/26.webp)


මීළඟ පියවරේදී, ඔබට `Tx0` සඳහා සහ ඔබේ පළමු මිශ්‍රණය සඳහා වෙන් කිරීමට ගාස්තු මට්ටම තෝරා ගත යුතුය. මෙම සැකසුම ඔබේ `Tx0` සහ ඔබේ ආරම්භක CoinJoin (හෝ ආරම්භක කෝයින්ජොයින්) තහවුරු කිරීමට ගතවන වේගය තීරණය කරයි. `Tx0` සහ ආරම්භක මිශ්‍රණය සඳහා Mining ගාස්තු ඔබේ වගකීම වන නමුත් පසුකාලීන නැවත මිශ්‍රණ සඳහා Mining ගාස්තු ගෙවීමට ඔබට අවශ්‍ය නොවේ. ඔබට `Low`, `Normal`, හෝ `High` විකල්ප අතර තේරීමක් ඇත.


![samourai](assets/notext/27.webp)


V istem oknu imate možnost izbrati bazen, v katerega boste vstopili. Glede na to, da sem sprva izbral UTXO od `454,258 Sats`, je moja edina možna izbira bazen `100,000 Sats`. Ta stran vam prav tako predstavi storitvene pristojbine bazena, poleg pristojbin Mining, kar vam omogoča, da poznate skupne stroške za ta cikel CoinJoin. Če vam vse ustreza, izberite ustrezen bazen in nadaljujte s klikom na moder gumb `VERIFY CYCLE DETAILS`.


![samourai](assets/notext/28.webp)


ඔබට පසුව ඔබේ CoinJoin චක්‍රය පිළිබඳ සියලු විස්තර දැක ගත හැක:


- UTXOs කීයක් පූල් එකට ඇතුළු වේවිද;
- විවිධ ගාස්තු;
- doxxic වෙනස්වීමේ ප්‍රමාණය...


තොරතුරු සනාථ කර, එවිට Green `START CYCLE` බොත්තම මත ක්ලික් කරන්න.


![samourai](assets/notext/29.webp)


වින්ඩෝවක් පෙනී යනු ඇත ඔබට CoinJoin චක්‍රයට ඔබගේ ඇතුළත් වීමෙන් ඇතිවන විෂ ව්‍යුහය "නොවියදම් කළ හැකි" ලෙස සලකුණු කිරීමට. `YES` තෝරා ගැනීමෙන්, මෙම UTXO ඔබේ Wallet තුළ දෘශ්‍යමාන නොවන අතර අනාගත ගනුදෙනු සඳහා තෝරා ගත නොහැක. කෙසේ වෙතත්, එය ඔබේ Wallet හි UTXO ලැයිස්තුවේ ප්‍රවේශය ලැබිය හැකි අතර එහි තත්ත්වය අතින් වෙනස් කළ හැක. ඔබේ පෞද්ගලිකත්වය පසුව අඩු කළ හැකි කිසියම් සැලසුම් දෝෂයක් වලක්වා ගැනීමට මෙම විකල්පය තෝරා ගැනීම නිර්දේශ කරයි. ඔබ `NO` තෝරා ගන්නේ නම්, විෂ ව්‍යුහය ඔබේ Wallet තුළ භාවිතයට ලබා ගත හැක. මෙම විෂ ව්‍යුහය කළමනාකරණය කිරීම සහ භාවිතා කිරීම පිළිබඳව වැඩිදුරටත් ඉගෙන ගැනීමට අවශ්‍ය නම්, මම ඔබට මෙම උපකාරකයේ අවසාන කොටස කියවීමට උපදෙස් දෙමි.


![samourai](assets/notext/30.webp)


Samourai nato odda vaš Tx0.


![samourai](assets/notext/31.webp)


### "Coinjoins izdelava"

Tx0 प्रसारित भएपछि, तपाईं यसलाई Whirlpool मेनुको `Transactions` ट्याबमा फेला पार्न सक्नुहुन्छ।


![samourai](assets/notext/32.webp)

ඔබගේ UTXOs මිශ්‍ර කිරීමට සූදානම්ව ඇති අතර ඒවා **Premix** ගිණුමට අදාළ වන `Mixing in progress...` ටැබ් එකේ ඇත.

![samourai](assets/notext/33.webp)


`Tx0` එක තහවුරු වූ විට, ඔබේ UTXO ස්වයංක්‍රීයව සම්බන්ධකය සමඟ ලියාපදිංචි වන අතර, ආරම්භක මිශ්‍රණ ස්වයංක්‍රීය ආකාරයෙන් අනුක්‍රමිකව ආරම්භ වේ.


![samourai](assets/notext/34.webp)


Z izbiro zavihka `Remixing`, ki ustreza računu **Postmix**, boste opazili UTXO-je, ki so rezultat začetnih mešanj. Ti kovanci bodo ostali pripravljeni za nadaljnje mešanje, kar ne bo povzročilo dodatnih stroškov. Priporočam, da si ogledate ta drugi članek, da se naučite več o procesu mešanja in učinkovitosti cikla CoinJoin: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


![samourai](assets/notext/35.webp)


UTXO को रीमिक्सिंगलाई अस्थायी रूपमा निलम्बन गर्न यसको दायाँमा रहेको पज बटन थिचेर सम्भव छ। यसलाई फेरि रीमिक्सिंगको लागि योग्य बनाउन, उही बटनलाई दोस्रो पटक क्लिक गर्नुहोस्। यो महत्त्वपूर्ण छ कि एकै समयमा प्रति प्रयोगकर्ता र प्रति पूल मात्र एक CoinJoin प्रदर्शन गर्न सकिन्छ। यसरी, यदि तपाईंसँग CoinJoin को लागि तयार `100 000 Sats` का 6 UTXOs छन् भने, तिनीहरूमध्ये मात्र एकलाई मिक्स गर्न सकिन्छ। UTXO मिक्स गरेपछि, Samourai Wallet ले प्रत्येक सिक्काको रीमिक्सिंगलाई विविधता र सन्तुलन गर्नको लागि तपाईँको उपलब्धताबाट नयाँ UTXO लाई अनियमित रूपमा चयन गर्दछ।


![samourai](assets/notext/36.webp)


ඔබේ UTXOs නැවත මිශ්‍ර කිරීම සඳහා අඛණ්ඩව ලබා ගත හැකි බව සහතික කිරීම සඳහා, Samourai යෙදුම පසුබැසීමේදී සක්‍රීයව තබා ගැනීම අවශ්‍ය වේ. Whirlpool ක්‍රියාත්මක වන බව තහවුරු කරන දැනුම්දීමක් ඔබේ දුරකථනයේ දැකිය යුතුය. යෙදුම වසා දැමීම හෝ ඔබේ දුරකථනය නිවා දැමීම coinjoins නවතී.


### සිකිලි සම්පූර්ණ කිරීම

ඔබගේ මිශ්‍රිත බිට්කොයින් වියදම් කිරීමට, Whirlpool මෙනු ටැබ් වල `Remixing` ලෙස සටහන් කළ **Postmix** ගිණුමට යන්න.


![samourai](assets/notext/37.webp)


කොණේ දකුණු පහළින් පිහිටි නිල් Whirlpool ලාංඡනය මත ක්ලික් කරන්න.


![samourai](assets/notext/38.webp)


පසුව `Spend Mixed UTXOs` මත ක්ලික් කරන්න.


![samourai](assets/notext/39.webp)


ඔබට පසුව ලාභාගාමීගේ Address සහ යැවිය යුතු මුදල ඇතුළත් කළ හැක, Samourai Wallet සමඟ කරන වෙනත් ගනුදෙනුවක් සඳහා මෙන්ම. නිල් පසුබිම Whirlpool ගිණුමකින් මුදල් වියදම් කරන බව, සහ **තැන්පතු** ගිණුමෙන් නොවන බව දක්වයි.


![samourai](assets/notext/40.webp)


Z zgornjim desnim klikom na 3 majhne pike imate možnost izbrati določene UTXO-je.

![samourai](assets/notext/41.webp)

වින්ඩෝවෙහි ඉහළ දකුණු කෙළවරේ ඇති සුදු චතුරස්‍රය මත ක්ලික් කිරීමෙන්, ඔබේ කැමරාව සමඟ ලැබෙන Address හි QR කේතය ස්කෑන් කළ හැක.


![samourai](assets/notext/42.webp)


ඔබේ වියදම් ගනුදෙනුව සඳහා අවශ්‍ය තොරතුරු ඇතුළත් කර, එවිට නිල් `VERIFY TRANSACTION` බොත්තම මත ක්ලික් කරන්න.


![samourai](assets/notext/43.webp)


මීළඟ පියවරේදී, ඔබේ ගනුදෙනුවට සම්බන්ධ ගාස්තු අනුපාතය වෙනස් කිරීමේ විකල්පය ඔබට ඇත. ඔබට සමාන කොටුව පරීක්ෂා කිරීමෙන් Stonewall විකල්පය සක්‍රීය කළ හැක. Stonewall විකල්පය තෝරා ගැනීමට නොහැකි නම්, එය ඔබේ **Postmix** ගිණුමට මෙම විශේෂිත ගනුදෙනු ව්‍යුහය සඳහා ප්‍රමාණවත් UTXO එකක් නොමැති බව අර්ථ දක්වයි.


[-> Stonewall ගනුදෙනු පිළිබඳව වැඩිදුරටත් ඉගෙන ගන්න.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


If everything is to your satisfaction, click on the Green `SEND ... BTC` button.


![samourai](assets/notext/44.webp)


Samourai तब आपके लेन-देन पर हस्ताक्षर करेगा और इसे नेटवर्क पर प्रसारित करेगा। आपको बस इतना करना है कि जब तक इसे Miner द्वारा एक ब्लॉक में जोड़ा नहीं जाता, तब तक प्रतीक्षा करें।


![samourai](assets/notext/45.webp)


### SCODE භාවිතා කිරීම

කලින් කිසි විටෙක, Samourai Wallet කණ්ඩායම් "SCODEs" ලබා දේ. SCODE යනු තටාකයේ සේවා ගාස්තු සඳහා වට්ටමක් ලබා දෙන ප්‍රවර්ධන කේතයකි. Samourai Wallet විශේෂ අවස්ථා වලදී එම කේත පරිශීලකයින්ට විශේෂ අවස්ථා වලදී ලබා දේ. මම ඔබට [Samourai Wallet අනුගමනය කිරීමට](https://twitter.com/SamouraiWallet) සමාජ මාධ්‍ය ඔස්සේ උපදෙස් දෙමි, එවිට අනාගත SCODES මග හැරී නොයයි.


Če želite uporabiti SCODE na Samourai, pred začetkom novega cikla CoinJoin pojdite v meni Whirlpool in izberite tri majhne pike, ki se nahajajo v zgornjem desnem kotu zaslona.


![samourai](assets/notext/46.webp)


SCODE (promo code) Whirlpool ක්ලික් කරන්න.


![samourai](assets/notext/47.webp)


SCODE එක විවෘත වූ කවුළුවේ ඇතුළත් කර, පසුව `OK` මත ක්ලික් කිරීමෙන් වලංගු කරන්න.


![samourai](assets/notext/48.webp)


Whirlpool خودبخود بند ہوجائے گا۔ Samourai کے لوڈ ہونے کا انتظار کریں، پھر دوبارہ Whirlpool مینو کھولیں۔


![samourai](assets/notext/49.webp)


Prepričajte se, da je vaš SCODE pravilno registriran, tako da še enkrat kliknete na tri majhne pike in nato izberete `SCODE (promo koda) Whirlpool`. Če je vse v redu, ste pripravljeni začeti nov cikel Whirlpool s popustom na stroške storitev. Pomembno je omeniti, da so ti SCODE-i začasni: veljajo le nekaj dni, preden postanejo zastareli.


## Kako vedeti kakovost naših CoinJoin koles?

CoinJoin සඳහා සත්‍යයෙන්ම කාර්යක්ෂම වීමට, ආදාන සහ නිමාවන්ගේ ප්‍රමාණ අතර හොඳ ඒකාකාරතාවයක් පෙන්වීම අත්‍යවශ්‍ය වේ. මෙම ඒකාකාරතාවය බාහිර නිරීක්ෂකයෙකුගේ දෘෂ්ටියේ ඇති විය හැකි අර්ථකථන සංඛ්‍යාව වැඩි දියුණු කරයි, එමඟින් ගනුදෙනුව වටා ඇති අනියමතාවය වැඩි කරයි. CoinJoin මඟින් ජනිත වන මෙම අනියමතාවය ප්‍රමාණවත් කිරීමට, ගනුදෙනුවේ entropy ගණනය කිරීමට හැකි වේ.


මෙම සූචකයන් පිළිබඳ ගැඹුරු විමසුමක් සඳහා (Whirlpool ආකෘතිය යනු coinjoins සඳහා වැඩිම සමරූපතාවය ගෙන එන එකක් ලෙස පිළිගැනේ), මම ඔබට උපකාරකය වෙත යොමු කරමි: [BOLTZMANN CALCULATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe)


Naslednje se oceni učinkovitost več ciklov CoinJoin glede na obseg skupin, v katerih je kovanec skrit. Velikost teh skupin določa tako imenovane anonsete. Obstajata dve vrsti anonsetov: prvi ocenjuje pridobljeno zasebnost proti retrospektivni analizi (od sedanjosti do preteklosti) in drugi proti prospektivni analizi (od preteklosti do sedanjosti). Za podrobno razlago teh dveh kazalnikov vas vabim, da si ogledate vadnico: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## पोस्टमिक्स कैसे प्रबंधित करें?

CoinJoin चक्रहरू प्रदर्शन गरेपछि, तपाईंको UTXOs लाई **postmix** खातामा राख्नु नै उत्तम रणनीति हो, तिनीहरूको भविष्यको प्रयोगको लागि पर्खँदै। तपाईंले तिनीहरूलाई खर्च गर्न आवश्यक नपरेसम्म तिनीहरूलाई अनिश्चितकालसम्म रिमिक्स गर्न दिनु पनि सल्लाहयोग्य छ।


සමහර පරිශීලකයින් තම මිශ්‍රිත බිට්කොයින් Hardware Wallet මඟින් ආරක්ෂිත Wallet වෙත මාරු කිරීම සලකා බලන්නට පුළුවන්. මෙය සම්භවය, නමුත් ලබාගත් රහස්‍යතාවයට හානි නොකරන ලෙස Samourai Wallet හි නිර්දේශයන් නිවැරදිව අනුගමනය කිරීම වැදගත් වේ.


UTXOs එකතු කිරීම වඩාත්ම සාමාන්‍යයෙන් සිදු කරන වැරදි ලෙස සැලකේ. CIOH (*Common-Input-Ownership-Heuristic*) වලක්වා ගැනීම සඳහා, එකම ගනුදෙනුවක මිශ්‍ර UTXOs සහ අමිශ්‍ර UTXOs එකට එකතු කිරීමෙන් වළකින්න. මෙය ඔබේ Wallet තුළ UTXOs කාර්යක්ෂමව කළමනාකරණය කිරීම අවශ්‍ය කරයි, විශේෂයෙන් ලේබල් කිරීමේ සම්බන්ධයෙන්. CoinJoin ඉක්මවා, UTXOs එකතු කිරීම සාමාන්‍යයෙන් නරක පුරුද්දක් වන අතර, නිසි ලෙස කළමනාකරණය නොකළ විට රහස්‍යතාවය අහිමි වීමකට හේතු වේ.

Prav tako morate biti pozorni na konsolidacijo mešanih UTXO-jev med seboj. Zmerne konsolidacije so možne, če imajo vaši mešani UTXO-ji pomembne anonsete, vendar bo to neizogibno zmanjšalo zasebnost vaših kovancev. Poskrbite, da konsolidacije ne bodo prevelike ali izvedene po nezadostnem številu remiksov, saj to tvega vzpostavitev deducibilnih povezav med vašimi UTXO-ji pred in po ciklih CoinJoin. V primeru dvoma o teh operacijah je najboljša praksa, da ne konsolidirate postmix UTXO-jev, temveč jih prenesete enega po enega na vaš Hardware Wallet, pri čemer vsakič ustvarite nov prazen Address. Še enkrat, ne pozabite pravilno označiti vsakega prejetega UTXO.


It is also advised against transferring your postmix UTXOs to a Wallet using uncommon scripts. For example, if you enter Whirlpool from a Multisig Wallet using `P2WSH` scripts, there's little chance you'll be mixed with other users having the same type of Wallet originally. If you exit your postmix to this same Multisig Wallet, the privacy level of your mixed bitcoins will be greatly diminished. Beyond scripts, there are many other Wallet fingerprints that can trick you.


Bitcoin ගනුදෙනුවක් සමඟ, ලැබීමේ ලිපින නැවත භාවිතා නොකිරීමද සුදුසුය. සෑම නව ගනුදෙනුවක්ම නව හිස් Address මත ලැබිය යුතුය.


සරලම සහ ආරක්ෂිතම විසඳුම වන්නේ ඔබේ මිශ්‍ර UTXO පසුමිශ්‍ර ගිණුම තුළ විවේකීව තබා, ඒවා නැවත මිශ්‍ර කරමින් පමණක් වියදම් කිරීමට ස්පර්ශ කිරීමයි. Samourai සහ Sparrow පසුම්බි සංකේත විශ්ලේෂණය සම්බන්ධ සියලුම අවදානම් වලට එරෙහිව අමතර ආරක්ෂණ ලබා දේ. මෙම ආරක්ෂණ ඔබට දෝෂ කිරීමට ඉවසා ගැනීමට උපකාරී වේ.


## Kako upravljati s toksičnimi spremembami?

ඊළඟට, ඔබ CoinJoin තටාකයට ඇතුල් විය නොහැකි doxxic වෙනස කළමනාකරණය කිරීමේදී සැලකිලිමත් විය යුතුය. Whirlpool භාවිතයෙන් ඇතිවන මෙම විෂ UTXO, ඔබ හා CoinJoin භාවිතය අතර සබඳතාවයක් ස්ථාපිත කරන බැවින් ඔබේ පෞද්ගලිකත්වයට අවදානමක් ඇති කරයි. එබැවින්, ඒවා අවධානයෙන් කළමනාකරණය කිරීම හා විශේෂයෙන් මිශ්‍ර UTXO සමඟ ඒවා එකතු නොකිරීම අත්‍යවශ්‍ය වේ. ඒවා භාවිතා කිරීම සඳහා සලකා බැලිය හැකි විවිධ උපාය මාර්ග මෙන්න:


- ඔවුන් කුඩා තටාකවල මිශ්‍ර කරන්න:** ඔබේ විෂ සහිත UTXO එකමෙන්ම කුඩා තටාකයකට ඇතුළු වීමට ප්‍රමාණවත් නම්, එය මිශ්‍ර කිරීම සලකා බලන්න. මෙය බොහෝ විට හොඳම විකල්පය වේ. කෙසේ වෙතත්, තටාකයකට ප්‍රවේශ වීමට විෂ සහිත UTXO කිහිපයක් එකට එක් නොකරන ලෙස ඉතා වැදගත් වේ, මන්ද මෙය ඔබේ විවිධ ඇතුළත් කිරීම් සම්බන්ධ කළ හැක.
- ඔවුන් "නොවියදම් කළ හැකි" ලෙස සලකුණු කරන්න:** තවත් ක්‍රමයක් නම් ඔවුන් භාවිතා කිරීම නවතා, ඔවුන්ගේ කැපවූ ගිණුමේ "නොවියදම් කළ හැකි" ලෙස සලකුණු කිරීම සහ HODL පමණක් කිරීමයි. මෙය ඔබට අහඹු ලෙස ඔවුන් වියදම් නොකරන බව සහතික කරයි. Bitcoin හි අගය වැඩි වුවහොත්, ඔබේ විෂ UTXO සඳහා වඩා සුදුසු නව තටාක හටගත හැක;
- පරිත්‍යාග කරන්න:** Bitcoin සහ එයට සම්බන්ධ මෘදුකාංග මත වැඩ කරන සංවර්ධකයින්ට, සමාන පරිත්‍යාග, කුඩා පරිමාණවත්, සලකා බලන්න. ඔබට BTC පිළිගන්නා සංවිධාන වෙත පරිත්‍යාග කළ හැක. ඔබේ විෂ සහිත UTXO කළමනාකරණය කිරීම අතිශය සංකීර්ණ ලෙස පෙනේ නම්, පරිත්‍යාගයක් කිරීමෙන් ඒවා ඉවත් කළ හැක;
- ගිෆ්ට් කාඩ් මිලදී ගන්න:** [Bitrefill](https://www.bitrefill.com/) වැනි වේදිකා ඔබට විවිධ වෙළෙන්දන් වෙතින් භාවිතා කළ හැකි ගිෆ්ට් කාඩ් සඳහා bitcoins Exchange කිරීමට ඉඩ සලසයි. මෙය ඔබේ විෂ සහිත UTXOs අහිමි නොවී සම්බන්ධ වටිනාකම අහිමි නොවී ඉවත් කිරීමට ක්‍රමයක් විය හැක;
- ඔවුන් Monero මත ඒකාබද්ධ කරන්න:** Samourai Wallet දැන් BTC සහ XMR අතර පරමාණුක හුවමාරු සේවාවක් ලබා දේ. මෙය විෂ සහිත UTXO කළමනාකරණය සඳහා Monero මත ඒකාබද්ධ කිරීම සඳහා ඉතා සුදුසු වේ, KYC හරහා ඔබේ පෞද්ගලිකත්වය ආපසු Bitcoin වෙත යැවීමට පෙර අහිමි නොකර, කෙසේ වෙතත්, මෙම විකල්පය Mining ගාස්තු සහ ද්‍රවතා සීමා නිසා අතිරේකය සම්බන්ධයෙන් වියදම් සහිත විය හැක;
- ඔවුන් Lightning Network වෙත යවන්න:** මෙම UTXOs Lightning Network වෙත මාරු කිරීම, අඩු ගනුදෙනු ගාස්තු වලින් ප්‍රයෝජන ලබා ගැනීම සඳහා රසවත් විකල්පයක් විය හැක. කෙසේ වෙතත්, මෙම ක්‍රමය ඔබේ Lightning භාවිතය අනුව විශේෂිත තොරතුරු අනාවරණය කළ හැකි බැවින්, අවධානයෙන් ක්‍රියාත්මක කළ යුතුය.


මෙම විවිධ තාක්ෂණයන් ක්‍රියාත්මක කිරීම පිළිබඳ විස්තරාත්මක උපදෙස් PlanB ජාලය මත ඉක්මනින් ලබා දෙනු ලැබේ.


**අමතර සම්පත්:**

[Samourai Wallet වීඩියෝ උපකාරකය](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Documentation - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Twitter thread on coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blog post on coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).