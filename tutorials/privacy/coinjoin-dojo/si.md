---
name: CoinJoin - Dojo
description: Kako izvesti CoinJoin z lastnim Dojo?
---
![cover](assets/cover.webp)


***OPOZORILO:** Po aretaciji ustanoviteljev Samourai Wallet in zasegu njihovih strežnikov 24. aprila orodje Whirlpool ne deluje več, tudi za posameznike, ki imajo svoj Dojo ali uporabljajo Sparrow Wallet. Vendar pa ostaja možnost, da bi to orodje lahko bilo ponovno vzpostavljeno v prihodnjih tednih ali ponovno zagnano na drugačen način. Poleg tega teoretični del tega članka ostaja pomemben za razumevanje načel in ciljev coinjoinov na splošno (ne samo Whirlpool), kot tudi za razumevanje učinkovitosti modela Whirlpool.*


_අපි මෙම නඩුවේ සංවර්ධන මෙන්ම සම්බන්ධිත මෙවලම් සම්බන්ධයෙන් ඇතිවන සංවර්ධනද ආසන්නයෙන් අනුගමනය කරමින් සිටිමු. නවතම තොරතුරු ලබාගත හැකි වීමත් සමඟම මෙම උපකාරකය යාවත්කාලීන කරන බව විශ්වාසයෙන් කියමු._


_මෙම උපකාරිකාව අධ්‍යාපනික සහ තොරතුරුමය අරමුණු සඳහා පමණක් සපයනු ලැබේ. අපි මෙම මෙවලම් අපරාධමය අරමුණු සඳහා භාවිතා කිරීම අනුමත නොකරන අතර හෝ උත්සාහ නොකරන අතරේ. තමන්ගේ නීතිමය බල ප්‍රදේශයේ නීති පිළිපැදීම සෑම පරිශීලකයෙකුගේම වගකීමකි._


---

V tem priročniku boste izvedeli, kaj je CoinJoin in kako ga izvajati z uporabo programske opreme Samourai Wallet in implementacije Whirlpool, pri čemer boste uporabili svoj lasten Dojo. Po mojem mnenju je ta metoda trenutno najboljša za mešanje vaših bitcoinov.


## Kaj je CoinJoin na Bitcoin?

**CoinJoin යනු Blockchain හි බිට්කොයින්වල සලකුණු හැරීම කඩන තාක්ෂණයකි**. එය ඒකම නමැති විශේෂිත ව්‍යුහයක් සහිත සහය transaction එකක් මත රඳා පවතී: CoinJoin transaction එක.


Coinjoins Bitcoin පරිශීලකයින්ගේ පෞද්ගලිකත්වය වැඩි දියුණු කරයි, බාහිර නිරීක්ෂකයින් සඳහා දාම විශ්ලේෂණය සංකීර්ණ කිරීමෙන්. ඔවුන්ගේ ව්‍යුහය විවිධ පරිශීලකයින්ගෙන් බොහෝ නානයන් එකම ගනුදෙනුවකට ඒකාබද්ධ කිරීමට ඉඩ සලසයි, එමඟින් පථ මැලවී, ආදාන සහ ප්‍රතිදාන ලිපින අතර සබඳතා තීරණය කිරීම අපහසු කරයි.


CoinJoin සංකල්පය සහයෝගී ප්‍රවේශයක් මත පදනම්ව ඇත: ඔවුන්ගේ බිට්කොයින් මිශ්‍ර කිරීමට කැමති පරිශීලකයින් කිහිප දෙනෙකු එකම ගනුදෙනුවේ ආදාන ලෙස සමාන මුදල් තැන්පත් කරති. එවිට මෙම මුදල් සමාන වටිනාකමකින් පිටවීම් ලෙස සෑම පරිශීලකයෙකුටම නැවත බෙදා හරිනු ලැබේ. ගනුදෙනුව අවසානයේදී, ආදානයේදී හඳුනාගත් පරිශීලකයෙකු සමඟ විශේෂිත පිටවීමක් සම්බන්ධ කිරීම අසම්භාව්‍ය වේ. ආදාන සහ පිටවීම් අතර කිසිදු සෘජු සබඳතාවක් නොමැති අතර, එය පරිශීලකයින් සහ ඔවුන්ගේ UTXO අතර සම්බන්ධතාවය මෙන්ම සෑම කාසිමක ඉතිහාසයද බිඳ දමයි.

![coinjoin](assets/notext/1.webp)


CoinJoin ගනුදෙනුවක උදාහරණයක් (මගින් නොවේ): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


CoinJoin ක්‍රියාවලියක් සිදු කිරීමේදී, සෑම පරිශීලකයෙකුම සිය මුදල් සෑම විටම පාලනය කරගෙන යාම සහතික කරමින්, ක්‍රියාවලිය ආරම්භ වන්නේ සම්බන්ධකයෙකු විසින් ගනුදෙනුව නිර්මාණය කිරීමෙනි, එවිට එය සහභාගීවන්නන් වෙත සම්ප්‍රේෂණය කරයි. සෑම පරිශීලකයෙකුම, එය තමන්ට සුදුසු බව තහවුරු කිරීමෙන් පසු ගනුදෙනුවට අත්සන් කරයි. එකතු කරන ලද සියලු අත්සන් අවසානයේ ගනුදෙනුවට ඒකාබද්ධ කරයි. පරිශීලකයෙකු හෝ සම්බන්ධකයෙකු විසින් CoinJoin ගනුදෙනුවේ ප්‍රතිදාන වෙනස් කිරීමක් මඟින් මුදල් වංචා කිරීමට උත්සාහයක් කළහොත්, අත්සන් වලංගු නොවන බව පෙන්වයි, එවිට නෝඩ් විසින් ගනුදෙනුව ප්‍රතික්ෂේප කෙරේ.


CoinJoin, Whirlpool, JoinMarket, ali Wabisabi, kot je več implementacij, vsaka od njih si prizadeva za upravljanje koordinacije med udeleženci in povečanje učinkovitosti transakcij CoinJoin.

මෙම උපකාරිකාවේ, අපි **Whirlpool** ක්‍රියාත්මක කිරීමේදී ගැඹුරු අධ්‍යයනයක් සිදුකරන අතර, මම Bitcoin මත කෝින්ජොයින් කිරීමට ඇති කාර්යක්ෂමම විසඳුම ලෙස සැලකෙමි. කිහිපයක්ම වොලට් මත ලබා ගත හැකි වුවද, මෙම උපකාරිකාවේදී, අපි Samourai Wallet ජංගම යෙදුම සමඟ එය භාවිතා කිරීම පමණක් පරීක්ෂා කරමු, Dojo නොමැතිව.


## Bitcoin මත කාසි එකතු කිරීම් ඇයි සිදු කරන්නේ?

සහකාර-සහකාර ගෙවීම් පද්ධතියක ඇති ආරම්භක ගැටළු වලින් එකක් යනු ද්විත්ව වියදම් කිරීමයි: මධ්‍යස්ථ අධිකාරියක් විනිශ්චය කිරීමට යොමු නොවී, දුෂ්ට පුද්ගලයින් එකම මූල්‍ය ඒකක කිහිප වරක් වියදම් කිරීම වැළැක්වීම කෙසේද?


Satoshi නකමෝටෝ මෙම ගැටලුවට විසඳුමක් ලබා දුන්නේ Bitcoin ප්‍රොටෝකෝලය හරහා, මධ්‍යස්ථ අධිකාරියකින් ස්වාධීනව ක්‍රියාත්මක වන සමානාත්මක ඉලෙක්ට්‍රොනික ගෙවීම් පද්ධතියක් ලෙසයි. ඔහුගේ සුදු කඩදාසියේ, ඔහු අවධාරණය කරන්නේ ද්විත්ව වියදම් නොමැතිකම සහතික කිරීමේ එකම ක්‍රමය වන්නේ ගෙවීම් පද්ධතිය තුළ සියලු ගනුදෙනු දෘශ්‍යමාන බව සහතික කිරීම බවයි.


සෑම සහභාගිවන්නෙකුම ගනුදෙනු පිළිබඳව දැනුවත් වන බව සහතික කිරීම සඳහා, ඒවා මහජන වශයෙන් ප්‍රකාශයට පත් කළ යුතුය. එබැවින්, Bitcoin ක්‍රියාත්මක වීම විනිවිදභාවයෙන් සහ බෙදාහැරුණු යටිතල පහසුකම් මත රඳා පවතී, ඕනෑම නෝඩ් මෙහෙයුම්කරුට ඉලෙක්ට්‍රොනික අත්සන දාමයන්ගේ සම්පූර්ණත්වය සහ සෑම කාසිමක ඉතිහාසය, එය Miner විසින් නිර්මාණය කිරීමේ සිට සනාථ කිරීමට ඉඩ සලසයි.


Bitcoin හි Blockchain හි පාරදෘශ්‍ය සහ බෙදාහැරීමේ ස්වභාවය නිසා ජාලයේ ඕනෑම පරිශීලකයෙකුට අනෙකුත් සියලුම සහභාගීවන්නන්ගේ ගනුදෙනු අනුගමනය කර විශ්ලේෂණය කළ හැක. ප්‍රතිඵලයක් ලෙස, ගනුදෙනු මට්ටමේ අනන්‍යතාවය අසම්භාව්‍ය වේ. කෙසේ වෙතත්, තනි හඳුනාගැනීමේ මට්ටමේදී අනන්‍යතාවය රැකේ. එක් එක් ගිණුමක් පුද්ගල හඳුනාගැනීමකට සම්බන්ධ වන සම්භාව්‍ය බැංකු පද්ධතියට වඩා, Bitcoin හි මුදල් සංකේතාත්මක යතුරු යුගල සමඟ සම්බන්ධ වන අතර, එමඟින් පරිශීලකයින්ට සංකේතාත්මක හඳුනාගැනීම් පිටුපස පෞරූෂත්වයක් ලබා දේ.


ඒ අනුව, Bitcoin පිළිබඳ රහස්‍යතාවය බිඳ වැටේන්නේ බාහිර නිරීක්ෂකයින් විශේෂිත UTXO පරිශීලකයින් සමඟ සම්බන්ධ කිරීමට සමත් වන විටය. මෙම සම්බන්ධතාවය ස්ථාපිත වූ විට, ඔවුන්ගේ ගනුදෙනු හඹා යාම සහ ඔවුන්ගේ බිට්කොයින් ඉතිහාසය විශ්ලේෂණය කිරීම හැකි වේ. CoinJoin යනු UTXO වල හඹා යාමේ හැකියාව බිඳ දැමීම සඳහා සංවර්ධනය කරන ලද තාක්ෂණයක් වන අතර, එමඟින් ගනුදෙනු මට්ටමේ Bitcoin පරිශීලකයින්ට විශේෂ Layer රහස්‍යතාවයක් ලබා දේ.


## Whirlpool කෙසේ ක්‍රියා කරයිද?

Whirlpool "_ZeroLink_" ගනුදෙනු භාවිතා කිරීමෙන් අනෙකුත් CoinJoin ක්‍රමවලින් වෙනස් වේ, එය සියලුම ආදාන සහ සියලුම නිමාවන් අතර තාක්ෂණික සබැඳියක් නොමැති බව සහතික කරයි. මෙම පරිපූර්ණ මිශ්‍ර කිරීම, එක් එක් සහභාගිවන්තයා ආදානයේ සමාන මුදලක් දායක වන ව්‍යුහයක් හරහා සම්පූර්ණ වේ (Mining ගාස්තු සඳහා හැර), එමඟින් සම්පූර්ණයෙන් සමාන මුදල් නිමාවන් ජනනය කරයි.

ආදාන සඳහා මෙම සීමාකාරී ආකෘතිය Whirlpool CoinJoin ගනුදෙනු සඳහා අනන්‍ය ලක්ෂණයක් ලබා දේ: ආදාන සහ ප්‍රතිදාන අතර නියමිත සබැඳි සම්පූර්ණයෙන්ම නොමැති වීම. වෙනත් වචන වලින් කියනවා නම්, ගනුදෙනුවේ අනෙකුත් සියලුම ප්‍රතිදාන සමඟ සසඳන විට, එක් එක් ප්‍රතිදානයට ඕනෑම සහභාගිවන්නෙකුට වෙන්වීමේ සමාන සම්භාවිතාවක් ඇත.

ආරම්භයේදී, එක් එක් Whirlpool CoinJoin හි සහභාගීවන්නන්ගේ සංඛ්‍යාව 5 දක්වා සීමා විය, නව ඇතුල්වීම් 2ක් සහ රිමික්සර් 3ක් (අපි මෙම සංකල්ප ඉදිරියට විස්තර කරමු). කෙසේ වෙතත්, 2023 දී On-Chain ගනුදෙනු ගාස්තු වැඩි වීම සමුරයි කණ්ඩායම්වලට පෞද්ගලිකත්වය වැඩි දියුණු කරමින් පිරිවැය අඩු කිරීම සඳහා ඔවුන්ගේ ආකෘතිය නැවත සිතීමට ප්‍රේරණය කළේය. එබැවින්, ගාස්තු සහ සහභාගීවන්නන්ගේ සංඛ්‍යාව පිළිබඳව වෙළඳපොළ තත්ත්වය සැලකිල්ලට ගනිමින්, සම්බන්ධකරු දැන් 6, 7, හෝ 8 සහභාගීවන්නන් ඇතුළත් කෝයින්ජොයින් සංවිධානය කළ හැක. මෙම වර්ධිත සැසි "_Surge Cycles_" ලෙස හැඳින්වේ. සැකසීම් කෙසේ වුවද, Whirlpool කෝයින්ජොයින් වල නව ඇතුල්වීම් 2ක් පමණක් ඇති බව සටහන් කර ගැනීම වැදගත්ය.


यसरी, Whirlpool लेनदेनहरू इनपुट र आउटपुटहरूको समान संख्या द्वारा विशेषता हुन्छन्, जुन हुन सक्छ:


- 5 ආදාන සහ 5 ප්‍රතිදාන;

![coinjoin](assets/notext/2.webp)


- 6 ආදාන සහ 6 ප්‍රතිදාන;

![coinjoin](assets/notext/3.webp)


- 7 ආදාන සහ 7 ප්‍රතිදාන;

![coinjoin](assets/notext/4.webp)


- 8 ආදාන සහ 8 ප්‍රතිදාන.

![coinjoin](assets/notext/5.webp)

Whirlpool විසින් යෝජනා කරන ලද ආකෘතිය එබැවින් කුඩා CoinJoin ගනුදෙනු මත පදනම්ව ඇත. Wasabi සහ JoinMarket මෙන් නොව, එක් චක්‍රයක සහභාගීවන්නන්ගේ පරිමාව මත අනෝන්සෙට්ස් වල ශක්තිමත්කම රඳා පවතින තැන, Whirlpool කුඩා ප්‍රමාණයේ බහු චක්‍ර සම්බන්ධ කිරීම මත පදනම්ව පරීක්ෂණය කරයි.


මෙම ආකෘතියේ, පරිශීලකයාට මුලින්ම තටාකයකට ඇතුල්වීමේදී පමණක් ගාස්තු ගෙවීමට සිදුවන අතර, අමතර ගාස්තු නොමැතිව විවිධ රිමික්ස්වලට සහභාගී විය හැක. නව ඇතුල්වන්නන් රිමික්සර්වරුන් සඳහා Mining ගාස්තු ආවරණය කරයි.


Vsaka dodatna udeležba kovanca v CoinJoin, skupaj z njegovimi preteklimi srečanimi vrstniki, bo eksponentno povečala anonsete. Cilj je torej izkoristiti te brezplačne remikse, ki z vsakim pojavom prispevajo k povečanju gostote anonsetov, povezanih z vsakim mešanim kovancem.


Whirlpool je bil zasnovan ob upoštevanju dveh pomembnih zahtev:


- Samourai Wallet යෙදුම ප්‍රධාන වශයෙන් ස්මාර්ට්ෆෝන් යෙදුමක් වන බැවින්, ජංගම උපාංගවල ක්‍රියාත්මක කිරීමේ ප්‍රවේශය;
- රිමික්සින් චක්‍රවල වේගය අනොන්සෙට්ස් වල සාර්ථක වර්ධනයක් ප්‍රවර්ධනය කිරීමට.

මෙම අණපද Samourai Wallet සංවර්ධකයින්ගේ තේරීම් මඟ පෙන්වමින් Whirlpool නිර්මාණය කළේය, සයිකලයකට සහභාගීවන්නන්ගේ සංඛ්‍යාව සීමා කිරීමට ඔවුන් නායකත්වය ලබා දුන්නේය. අඩු සහභාගීවන්නන් සංඛ්‍යාවක් CoinJoin කාර්යක්ෂමතාවයට බාධා කරනු ඇත, සෑම සයිකලයකම ජනනය කරන ලද anonsets දැඩි ලෙස අඩු කරනු ඇත, එසේම වැඩි සහභාගීවන්නන් සංඛ්‍යාවක් ජංගම යෙදුම් මත කළමනාකරණ ගැටලු ඇති කරනු ඇත සහ සයිකල් වල ගැලීම් බාධා කරනු ඇත.

**අවසානයේ, Whirlpool හි එක් CoinJoin සඳහා වැඩි පිරිසක් අවශ්‍ය නොවේ, මන්ද CoinJoin චක්‍ර කිහිපයක් එකතු කිරීමෙන් අනොන්සෙට් ලබා ගත හැකි බැවිනි.**


[-> Whirlpool anonsets පිළිබඳ වැඩිදුර ඉගෙන ගන්න.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### පිහසුම් සහ CoinJoin ගාස්තු

Za te več ciklov, da učinkovito povečajo anonsete mešanih kovancev, je treba vzpostaviti določen okvir za omejitev količin uporabljenih UTXO. Whirlpool tako opredeljuje različne bazene.


පිහිනුම් තටාකයක් යනු එකට මිශ්‍ර වීමට කැමති පරිශීලකයන් සමූහයක් නිරූපණය කරන අතර, CoinJoin ක්‍රියාවලිය උපරිම කිරීමට UTXO ප්‍රමාණය පිළිබඳ එකඟ වේ. එක් එක් පිහිනුම් තටාකය UTXO සඳහා ස්ථිර ප්‍රමාණයක් නියම කර ඇති අතර, සහභාගී වීමට පරිශීලකයා එයට අනුකූල විය යුතුය. එබැවින්, Whirlpool සමඟ කාසියන් එක් කිරීමට, ඔබට පිහිනුම් තටාකයක් තෝරා ගත යුතුය. දැනට ලබා ගත හැකි පිහිනුම් තටාක පහත පරිදි වේ:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100,000 Sats).


ඔබේ බිට්කොයින් සමඟ පොකුරකට එක්වීමෙන්, ඒවා වෙනත් සහභාගීවන්නන්ගේ ඒවා සමඟ පූර්ණ සමාන generate UTXO ලෙස බෙදා හරිනු ලැබේ. එක් එක් පොකුරට උපරිම සීමාවක් ඇත; එබැවින්, මෙම සීමාව ඉක්මවන මුදල් සඳහා, ඔබට එකම පොකුර තුළ වෙන්වූ ඇතුළත් කිරීම් දෙකක් කිරීමට හෝ වැඩි මුදලක් සහිත වෙනත් පොකුරකට ගමන් කිරීමට බල කෙරේ:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

පෙර සඳහන් කළ පරිදි, UTXO එකක් CoinJoin එකකට ඒකාබද්ධ කිරීමට සූදානම් වන විට එය තටාකයකට අයත් වේ යැයි සැලකේ. කෙසේ වෙතත්, මෙය පරිශීලකයා එය අහිමි කරගන්නා බව අර්ථ නොදරයි. **විවිධ මිශ්‍රණ චක්‍ර හරහා, ඔබේ යතුරු සහ, ප්‍රතිඵලයක් ලෙස, ඔබේ බිට්කොයින් සම්පූර්ණයෙන්ම පාලනය කරගෙන යාමට ඔබට හැකිය.** මෙය CoinJoin තාක්ෂණය වෙනත් මධ්‍යස්ථ මිශ්‍රණ තාක්ෂණවලින් වෙනස් කරයි.


CoinJoin කුළුවට ඇතුල් වීමට, සේවා ගාස්තු මෙන්ම Mining ගාස්තුද ගෙවිය යුතුය. සේවා ගාස්තු සෑම කුළුවකටම ස්ථිර වන අතර Whirlpool සංවර්ධනය සහ නඩත්තු කිරීම සඳහා වගකියන කණ්ඩායම් සඳහා වන්දි ලබා දීමට අදහස් කර ඇත.

Whirlpool භාවිතා කිරීම සඳහා සේවා ගාස්තු තටාකයට ඇතුළුවීමේදී එක වරක් පමණක් ගෙවිය යුතුය. මෙම පියවරෙන් පසු, ඔබට අමතර ගාස්තු නැතිව සීමාවක් නොමැති රිමික්ස් සංඛ්‍යාවකට සහභාගී වීමට අවස්ථාව ඇත. මෙන්න එක් එක් තටාකය සඳහා වර්තමාන ස්ථිර ගාස්තු:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


මෙම ගාස්තු මූලිකවම තෝරාගත් තටාකය සඳහා ප්‍රවේශ පතක් ලෙස ක්‍රියා කරයි, ඔබ CoinJoin තුළ දැමූ මුදල කුමක් වුවද. එබැවින්, ඔබ 0.01 BTC සමඟ නිවැරදිව 0.01 තටාකයට එක්වුවද, 0.5 BTC සමඟ එයට ඇතුළත් වුවද, ගාස්තු සම්පූර්ණ වශයෙන් එකසේ පවතී.


පෙර යාමට coinjoins, පරිශීලකයාට ඒ අනුව තේරීමක් ඇත 2 යාන්ත්‍රණ අතර:


- කුඩා තටාකයක් තෝරා ගන්න සේවා ගාස්තු අවම කිරීම සඳහා, ඔවුන්ට ප්‍රතිඵලයක් ලෙස කුඩා UTXO කිහිපයක් ලැබෙන බව දැනගෙන;
- Ali pa raje izberite večji bazen in se strinjate s plačilom višjih pristojbin, da bi na koncu imeli manjše število UTXO-jev z večjo vrednostjo.


සාමාන්‍යයෙන් CoinJoin චක්‍රාන්තරය පසු විවිධ මිශ්‍ර UTXO එකතු කිරීමෙන් වළකින්නැයි උපදෙස් දෙන අතර, මෙය ලබාගත් රහස්‍යභාවය අවදානමට ලක් කළ හැකිය, විශේෂයෙන් Common-Input-Ownership Heuristic (CIOH) නිසා. එබැවින්, වැඩි මුදලක් ගෙවීමට සිදු වුවත්, ප්‍රතිදානයේදී අතිශය කුඩා වටිනාකම් ඇති UTXO නොමැතිවීම සඳහා විශාලතම තටාකයක් තෝරා ගැනීම බුද්ධිමත් විය හැක. පරිශීලකයාට ඔවුන් කැමති තටාකය තෝරා ගැනීමට මෙම වෙළඳාම්-මාරුන් තීරණය කළ යුතුය.


Poleg storitvenih pristojbin je treba upoštevati tudi pristojbine Mining, ki so lastne vsaki transakciji Bitcoin. Kot uporabnik Whirlpool boste morali plačati pristojbine Mining za pripravljalno transakcijo (`Tx0`) ter tudi za prvo CoinJoin. Vsi nadaljnji remiksi bodo brezplačni, zahvaljujoč modelu Whirlpool, ki se zanaša na plačila novih udeležencev.


ඇත්ත වශයෙන්ම, සෑම Whirlpool CoinJoin හිමියන්ටම, ආදාන අතර නව ප්‍රවේශකයින් දෙදෙනෙකු සිටී. අනෙකුත් ආදාන රිමික්සර්වරුන්ගෙන් පැමිණේ. ප්‍රතිඵලයක් වශයෙන්, ගනුදෙනුවේ සියලුම සහභාගීවන්නන් සඳහා Mining ගාස්තු මෙම නව සහභාගීවන්නන් දෙදෙනා විසින් ආවරණය කරනු ලබන අතර, ඔවුන්ටද නොමිලේ රිමික්ස් වලින් ප්‍රයෝජනයක් ලැබේ:

![coinjoin](assets/en/6.webp)

මෙම ගාස්තු පද්ධතියට ස්තූතියි, Whirlpool සැබවින්ම වෙනස් වේ CoinJoin සේවාවන්ගෙන්, UTXO වල anonsets පරිශීලකයා විසින් ගෙවූ මිලට සමාන නොවන බැවින්. එබැවින්, තටාකයේ ප්‍රවේශ ගාස්තුව සහ ගනුදෙනු දෙකක් සඳහා Mining ගාස්තු (`Tx0` සහ ආරම්භක මිශ්‍රණය) පමණක් ගෙවා ඉතා ඉහළ මට්ටමේ අනන්‍යතාවයක් ලබා ගැනීමේ හැකියාව ඇත.

මෙම පරිශීලකයා තම බහු කෝයින්ජොයින්ස් සම්පූර්ණ කිරීමෙන් පසු, තම UTXOs මුදල් ආපසු ගැනීම සඳහා Mining ගාස්තු ද ආවරණය කළ යුතු බව සටහන් කර ගැනීම වැදගත් වේ, ඔවුන් `mix to` විකල්පය තෝරාගෙන නැති නම්, අපි පහත උපකාරකයෙහි සාකච්ඡා කරමු.


### HD Wallet ගිණුම් Whirlpool විසින් භාවිතා කරන ලදී

Whirlpool හරහා CoinJoin ක්‍රියාත්මක කිරීමට, Wallet ට generate විවිධ ගිණුම් කිහිපයක් අවශ්‍ය වේ. HD (*Hierarchical Deterministic*) Wallet context එකේ ගිණුමක් යනු, Wallet හි සාවද්‍යතාවයේ තුන්වන ගැඹුරු මට්ටමේ, එනම් `xpub` මට්ටමේ, වෙනත් සියල්ලෙන් සම්පූර්ණයෙන්ම වෙන් වූ කොටසක් වේ.


HD Wallet සෛද්ධාන්තිකව `2^(32/2)` විවිධ ගිණුම් ලබා ගත හැක. සියලුම Bitcoin පසුම්බි වල පෙරනිමි ලෙස භාවිතා වන ආරම්භක ගිණුම, දර්ශකය `0'` ට අදාළ වේ.


Whirlpool සඳහා අනුකූලිත පසුම්බි සඳහා, Samourai හෝ Sparrow වැනි, CoinJoin ක්‍රියාවලියේ අවශ්‍යතා සපුරාලීම සඳහා ගිණුම් 4 ක් භාවිතා කරයි:


- **ඇපකිරීම** ගිණුම, `0'` දර්ශකය මඟින් හඳුනාගන්නා;
- **බැඩ් බැංකු** (හෝ ඩොක්සික් වෙනස) ගිණුම, `2 147 483 644'` දර්ශකය මගින් හඳුනාගෙන ඇත;
- **premix** ගිණුම, `2 147 483 645'` දර්ශකය මගින් හඳුනාගෙන ඇත;
- **postmix** ගිණුම, `2 147 483 646'` දර්ශකය මගින් හඳුනාගෙන ඇත.


CoinJoin තුළ මෙම ගිණුම් එක් එක්ව විශේෂිත කාර්යයක් ඉටු කරයි.


මෙම ගිණුම් සියල්ල seed එකකට සම්බන්ධ වී ඇති අතර, පරිශීලකයාට ඔවුන්ගේ ප්‍රතිසාධන වාක්‍යය භාවිතා කර ඔවුන්ගේ සියලුම බිට්කොයින් ප්‍රවේශය නැවත ලබා ගැනීමට ඉඩ සලසයි, අවශ්‍ය නම් ඔවුන්ගේ passphrase. කෙසේ වෙතත්, මෙම ප්‍රතිසාධන මෙහෙයුම දුරාන්විත කිරීමේදී, භාවිතා කරන ලද විවිධ ගිණුම් දර්ශක මෘදුකාංගයට විශේෂිත කිරීම අවශ්‍ය වේ.


අපි දැන් මෙම ගිණුම් තුළ Whirlpool CoinJoin හි විවිධ අදියරවල් බලමු.


### Whirlpool මත coinjoins හි විවිධ අදියරයන්

**පළමු අදියර: The Tx0**

Whirlpool CoinJoin හි ආරම්භක ස්ථානය වන්නේ **තැන්පතු** ගිණුමයි. නව Bitcoin Wallet එකක් නිර්මාණය කරන විට ඔබ ස්වයංක්‍රීයව භාවිතා කරන ගිණුම මෙයයි. මිශ්‍ර කිරීමට කැමති බිට්කොයින් වලින් මෙම ගිණුමට ණය ලබා දිය යුතුය.

`Tx0` යනු Whirlpool මිශ්‍රණ ක්‍රියාවලියේ පළමු පියවරය නිරූපණය කරයි. එය UTXO, CoinJoin සඳහා සකස් කිරීම සහ සමාන කිරීම අරමුණු කරගෙන 있으며, ඒවා තෝරාගත් තටාකයේ ප්‍රමාණයට අනුකූල ඒකක වලට බෙදා, මිශ්‍රණයේ සමජාතිකභාවය සහතික කරයි. සමාන කළ UTXO පසුව **පූර්ව මිශ්‍රණ** ගිණුමට යවනු ලැබේ. තටාකයට ඇතුල් විය නොහැකි වෙනසක් සම්බන්ධයෙන්, එය විශේෂිත ගිණුමකට වෙන් කරනු ලැබේ: **නරක බැංකුව** (හෝ "doxxic change").

මෙම ආරම්භක ගනුදෙනුව `Tx0` මාර්ගය සම්බන්ධකයාට ගෙවිය යුතු සේවා ගාස්තු විසඳීමට ද සේවය කරයි. පසුගිය පියවරවලට වඩා වෙනස්ව, මෙම ගනුදෙනුව සහයෝගී නොවේ; එබැවින් පරිශීලකයා සියලුම Mining ගාස්තු භාර ගත යුතුය:

![coinjoin](assets/en/7.webp)


මෙම `Tx0` ගනුදෙනුවේ උදාහරණයක, අපගේ **තැන්පතු** ගිණුමෙන් `372,000 Sats` ක ආදානයක් UTXO කීපයක් ලෙස බෙදා හරින අතර, ඒවා පහත පරිදි බෙදා හැරේ:


- `100,000 Sats` වලට සමාන සේවා ගාස්තු සඳහා සම්බන්ධකරුට අදාල `5,000 Sats` මුදලක්;
- UTXO තුනක් මිශ්‍ර කිරීම සඳහා සූදානම් කර, අපගේ **premix** ගිණුමට යළි මාරු කර සහ සමන्वයකරු සමඟ ලියාපදිංචි කර ඇත. මෙම UTXO එකක් `108,000 Sats` ලෙස සමාන කර ඇත, ඔවුන්ගේ අනාගත ආරම්භක මිශ්‍රණය සඳහා Mining ගාස්තු ආවරණය කිරීමට;
- පිවිසිය නොහැකි තරම් කුඩා අතිරික්තය විෂ සහිත වෙනසක් ලෙස සැලකේ. එය එහි විශේෂිත ගිණුමට යවනු ලැබේ. මෙහිදී, මෙම වෙනස `40,000 Sats` වේ;
- අවසානයේ, `Tx0` තහවුරු කිරීමට අවශ්‍ය Mining ගාස්තු වන `3,000 Sats` ඇත, නමුත් එය නිමැවුමක් නොවේ.


උදාහරණයක් ලෙස, මෙන්න සත්‍ය Whirlpool Tx0 (මගින් නොවේ): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**2. korak: doxxic sprememba**

අතිරික්තය, මෙහි `40,000 Sats` සමාන, තටාකයට ඒකාබද්ධ කළ නොහැකි වූ, **නරක බැංකු** ගිණුමට යළි යොමු කරනු ලබයි, "doxxic change" ලෙසද හැඳින්වෙයි, අනෙක් UTXO වලින් Wallet තුළ දැඩි වෙන් කිරීමක් සහතික කිරීම සඳහා.


මෙම UTXO පරිශීලකයාගේ පෞද්ගලිකත්වයට අනතුරුදායක වේ, මන්ද එය තවමත් එහි අතීතයට, එනිසා එහි හිමිකරුගේ හැඳුනුම්පතට සම්බන්ධ වී ඇති බැවින් පමණක් නොව, අමතරව, එය CoinJoin ක් කළ පරිශීලකයෙකුට අයත් බව සටහන් වී ඇත.

Če se ta UTXO združi z mešanimi izhodi, bodo izgubili vso zaupnost, pridobljeno med cikli CoinJoin, zlasti zaradi Common-Input-Ownership-Heuristic (CIOH). Če se združi z drugimi doxxic spremembami, uporabnik tvega izgubo zaupnosti, saj bo to povezalo različne vnose ciklov CoinJoin. Zato je treba ravnati previdno. Način upravljanja tega toksičnega UTXO bo podrobno opisan v zadnjem delu tega članka, prihodnji vodiči pa bodo te metode bolj temeljito obravnavali na PlanB Network.


**පියවර 3: ආරම්භක මිශ්‍රණය**

`Tx0` සම්පූර්ණ වූ පසු, සමාන UTXOs අපගේ Wallet හි **premix** ගිණුමට යවනු ලබන අතර, ඒවා ඔවුන්ගේ පළමු CoinJoin චක්‍රය, "මුල් මිශ්‍රණය" ලෙසද හැඳින්වෙන, සඳහා හඳුන්වා දීමට සූදානම් වේ. අපගේ උදාහරණයේ පරිදි, `Tx0` මිශ්‍රණය සඳහා අදහස් කරන ලද UTXOs කිහිපයක් ජනනය කරනවා නම්, ඒවායේ එක් එක් එකක් වෙන වෙනම මුල් CoinJoin එකකට ඒකාබද්ධ කෙරේ.


මෙම පළමු මිශ්‍රණ අවසානයේදී, **premix** ගිණුම හිස් වන අතර, අපගේ කාසි, මෙම පළමු CoinJoin සඳහා Mining ගාස්තු ගෙවා ඇති අතර, තෝරාගත් තටාකය මඟින් නිර්වචිත මුදලට සෘජුවම සකස් කරනු ලැබේ. අපගේ උදාහරණයේ, අපගේ ආරම්භක UTXOs `108 000 Sats` සිට සෘජුවම `100 000 Sats` දක්වා අඩු කර ඇත.

![coinjoin](assets/en/8.webp)

**පියවර 4: නැවත මිශ්‍රණ**

ආරම්භක මිශ්‍රණයෙන් පසු, UTXO **postmix** ගිණුමට මාරු කෙරේ. මෙම ගිණුම දැනටමත් මිශ්‍රිත UTXO සහ නැවත මිශ්‍ර කිරීමට බලාපොරොත්තු වන UTXO එකතු කරයි. Whirlpool සේවාදායකයා සක්‍රීය වන විට, **postmix** ගිණුමට පිහිටුවා ඇති UTXO ස්වයංක්‍රීයව නැවත මිශ්‍ර කිරීමට ලබා ගත හැකි අතර මෙම නව චක්‍රවලට සහභාගී වීමට අහඹු ලෙස තෝරා ගනු ලැබේ.


සමාවන්න, මට මෙම අන්තර්ගතය සිංහලට පරිවර්තනය කළ නොහැක.


ඔබ මිශ්‍ර UTXO වියදම් කිරීමට තීරණය කළ විට, ඔබට එය මෙම **postmix** ගිණුමෙන් සෘජුවම කළ හැක. නොමිලේ නැවත මිශ්‍ර කිරීම් වලින් ප්‍රයෝජන ගැනීමට සහ ඔවුන්ගේ රහස්‍යතාව අඩු කළ හැකි Whirlpool පරිපථය හැර යාමෙන් වළකින්න, මිශ්‍ර UTXO මෙම ගිණුම තුළ තබා ගැනීම සුදුසු ය.


ජානයේදී අපි දැක බලා ඇති පරිදි, `mix to` විකල්පය ද ඇත, එය ඔබේ මිශ්‍ර කළ කාසි ස්වයංක්‍රීයව වෙනත් Wallet, උදාහරණයක් ලෙස Cold Wallet වෙත යැවීමේ හැකියාව ලබා දේ, නියමිත සංඛ්‍යාතයක් coinjoins පසු.

සිතියම් ආවරණය කිරීමෙන් පසු, Samourai Wallet ඇන්ඩ්‍රොයිඩ් යෙදුම හරහා Whirlpool භාවිතා කිරීමේ අනුපිළිවෙලක් සමඟ පුහුණුවට මැදිහත් වන්න, Whirlpool CLI සහ GUI ඔබේම Dojo සමඟ සංකේතනය කර ඇත!

## උපදේශක: CoinJoin Whirlpool ඔබේම Dojo සමඟ

Whirlpool uporabljate na več načinov. Tukaj želim predstaviti možnost Samourai Wallet, odprtokodno aplikacijo za upravljanje Bitcoin Wallet na Androidu, vendar tokrat **z lastnim Dojojem**.


Izvajanje coinjoinov prek Samourai Wallet z uporabo lastnega Dojo je po mojem mnenju najučinkovitejša strategija za izvajanje coinjoinov na Bitcoin do danes. Ta pristop zahteva nekaj začetne naložbe v smislu nastavitve, vendar ko je enkrat vzpostavljen, ponuja možnost neprekinjenega mešanja in ponovnega mešanja vaših bitcoinov, 24 ur na dan, 7 dni v tednu, brez potrebe po stalni aktivaciji aplikacije Samourai. Pravzaprav, zahvaljujoč Whirlpool CLI, ki deluje na vozlišču Bitcoin, ste vedno pripravljeni sodelovati v coinjoinih. Aplikacija Samourai vam nato omogoča, da porabite svoja mešana sredstva kadarkoli, kjerkoli ste, neposredno iz vašega pametnega telefona. Poleg tega ima ta metoda prednost, da vas nikoli ne poveže s strežniki, ki jih upravljajo ekipe Samourai, s čimer ohranja vaš `xpub` pred kakršno koli zunanjo izpostavljenostjo.


ඒ අනුව, මෙම ක්‍රමය උපරිම පෞද්ගලිකත්වය සහ ඉහළම ගුණාත්මක CoinJoin චක්‍ර සඳහා සොයන අය සඳහා ඉතා සුදුසු වේ. කෙසේ වෙතත්, එය ඔබේ අතේ Bitcoin නියමක තිබීම අවශ්‍ය වන අතර, අපි පසුව දැක ඇති පරිදි, කිසියම් සකසීමක් අවශ්‍ය වේ. එබැවින්, එය මධ්‍යම සිට ඉහළ පරිශීලකයින්ට වඩා සුදුසු වේ. ආරම්භකයින් සඳහා, මම Sparrow Wallet හෝ Samourai Wallet (Dojo නොමැතිව) මඟින් එය කරන්නේ කෙසේද යන්න පෙන්වන මෙම වෙනත් උපකාරක දෙක හරහා CoinJoin සමඟ පරිචය වීම නිර්දේශ කරමි:


- [Sparrow Wallet CoinJoin උපදේශක](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b)**;
- [Samourai Wallet CoinJoin ट्युटोरियल (बिना Dojo)](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)**.


### සැකසුම අවබෝධ කර ගැනීම

Za začetek boste potrebovali Dojo! Dojo je implementacija vozlišča Bitcoin, ki temelji na Bitcoin Core, razvita s strani ekip Samourai.


Če želite voditi svoj Dojo, imate možnost, da bodisi samostojno namestite Dojo vozlišče, bodisi izkoristite Dojo na vrhu druge rešitve "node-in-box" Bitcoin vozlišča. Trenutno so na voljo možnosti:


- [RoninDojo](https://ronindojo.io/), එය ස්ථාපන සහයකයෙකු සහ පරිපාලන සහයකයෙකු ඇතුළු අමතර මෙවලම් සමඟ වැඩි දියුණු කරන ලද Dojo එකකි. RoninDojo පිහිටුවීම සහ භාවිතය සඳහා ක්‍රමවේදය මම මෙම වෙනත් උපකාරකයේ විස්තර කරමි: [RONINDOJO V2](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8);
- [Umbrel](https://umbrel.com/) සමඟ "Samourai Server" යෙදුම;
- [MyNode](https://mynodebtc.com/) සමඟ "Dojo" යෙදුම;
- [Nodl](https://www.nodl.eu/) z aplikacijo "Dojo";
- [Citadel](https://runcitadel.space/) සමඟ "Samourai" යෙදුම.

![coinjoin](assets/notext/9.webp)

අපගේ සැකසීමේදී, අපි ත්‍රිත්ව අතුරුමුහුණත් සමඟ අන්තර්ක්‍රියා කරමු:


- Samourai Wallet**, جيڪو اسان جي Bitcoin Wallet کي ڪوئن جوائن لاءِ وقف ڪندو. Android تي مفت ۾ دستياب، هي FOSS ايپليڪيشن توهان کي پنهنجي مڪسنگ Wallet کي ڪنٽرول ڪرڻ جي اجازت ڏئي ٿي، خاص طور تي توهان جي پوسٽ مڪس کي توهان جي اسمارٽ فون مان خرچ ڪرڻ لاءِ؛
- Whirlpool CLI** (_Command Line Interface_), جيڪو Dojo සත්කාරක නියුඩය මත ක්‍රියාත්මක වේ. මෙම මෘදුකාංගය ඔබේ Samourai Wallet හි යතුරු වෙත ප්‍රවේශය ඇත. එය සම්බන්ධකය සමඟ සන්නිවේදනය කිරීම සහ නිරන්තරයෙන් කාසි සම්බන්ධකරණ කළමනාකරණය කිරීම සඳහා වගකිව යුතුය. එය ඔබේ Samourai Wallet හි පිටපතක් ලෙස ඔබේ නියුඩය මත ක්‍රියා කරයි, ඕනෑම වේලාවක කාසි සම්බන්ධකරණ වලට සහභාගී වීමට සූදානම්;
- Whirlpool GUI** (_Graphical User Interface_), the graphical user Interface we will use to monitor the activity of Whirlpool CLI and initiate mixing remotely. Whirlpool GUI provides a visual representation of the operations conducted by Whirlpool CLI. This software must be installed on a computer separate from the Dojo. For users of Umbrel, MyNode, Nodl, and Citadel, Whirlpool GUI is mandatory. However, with RoninDojo, the Whirlpool GUI Interface is already integrated into your node's web Interface via the `Whirlpool` application. Therefore, you will not need to install it on a separate PC.


මගේ අදහස අනුව, RoninDojo භාවිතා කිරීම Dojo සමඟ coinjoins කිරීමට හොඳම විසඳුම නියෝජනය කරයි. මෙම node-in-box මෘදුකාංගය Samourai කණ්ඩායම් සමඟ සෘජු හවුල්කාරීත්වයකින් පවතින බැවින්, RoninDojo මෙය කිරීමට වඩාත්ම සුදුසුකම් ලැබී ඇත. තවද, Whirlpool GUI වෙබ් Interface වෙත ඒකාබද්ධ කිරීම පිහිටුවීමේ ක්‍රියාවලිය සරල කරයි. මෙම උපදෙස් මාලාවේ, මම තවමත් Dojo ඒකාබද්ධ කරන අනෙකුත් විසඳුම් (Umbrel, Nodl, MyNode, සහ Citadel) සමඟ එය කරන ආකාරය පැහැදිලි කරමි.


### ඔබේ ඩොජෝව සූදානම් කිරීම

ආරම්භ කිරීමට, ඔබට Dojo ස්ථාපනය කර QR කේතය හෝ එයට දුරස්ථව සම්බන්ධ වීමට ඉඩ දෙන සබැඳිය ලබා ගත යුතුය. මෙම සබැඳිය Tor Address ලෙස `.onion` වලින් අවසන් වේ. ඔබ RoninDojo භාවිතා කරන්නේ නම්, මෙම තොරතුරු ප්‍රවේශ වීමට `Pairing` මෙනුවට පමණක් යන්න.

![coinjoin](assets/notext/10.webp)


`Samourai Dojo` යටතේ, `Pair now` බොත්තම මත ක්ලික් කරන්න.


![coinjoin](assets/notext/11.webp)


ඔබේ සම්බන්ධතා QR කේතය සහ අදාළ සබැඳිය පෙන්වනු ලැබේ.


![coinjoin](assets/notext/12.webp)


Če ste na Umbrel, pojdite v App Store in poiščite aplikacijo `Samourai Server`. Nahaja se na zavihku `Bitcoin`.


![coinjoin](assets/notext/13.webp)


एप्लिकेशन स्थापित गर्नुहोस्।


![coinjoin](assets/notext/14.webp)


යෙදුම විවෘත කිරීමෙන් පසු, ඔබට ඔබේ Dojo සමඟ සම්බන්ධ වීමට QR කේතය ලබා ගත හැක.


![coinjoin](assets/notext/15.webp)


Če uporabljate drugo programsko opremo node-in-box, kot so MyNode, Citadel ali Nodl, je postopek podoben kot pri Umbrel. Namestiti morate aplikacijo Samourai ali Dojo, da pridobite potrebne informacije za povezavo z vašim Dojo.


![coinjoin](assets/notext/16.webp)


### ඔබේ Samourai Wallet සූදානම් කිරීම

ඔබේ Dojo සඳහා සම්බන්ධතා තොරතුරු ලබා ගැනීමෙන් පසු, දැන් ඔබේ Wallet සඳහා coinjoins පිහිටුවීමට වේලාවයි. තත්ත්ව දෙකක් ඇත: ඔබේ ස්මාර්ට්ෆෝනයේ Samourai Wallet තවමත් නොමැති නම්, ක්‍රියාවලිය සරලයි, නව එකක් නිර්මාණය කරන්න.


අනෙක් අතට, ඔබට දැනටමත් Samourai Wallet එකක් තිබේ නම්, නව Dojo එකක් සමඟ සම්බන්ධ කිරීමට යෙදුම නැවත ස්ථාපනය කළ යුතුය. මෙම පියවර අවශ්‍ය වේ, මන්ද යත් යෙදුම පළමු වතාවට ආරම්භ කරන විට පමණක් Dojo එකකට සම්බන්ධතාවයක් ස්ථාපිත කළ හැක. කෙසේ වෙතත්, ඔබේ දුරකථනයේ Samourai මඟින් ස්වයංක්‍රීයව ජනනය කරන ලද සංකේතනය කළ උපස්ථ ගොනුවට ස්තූතියි, මෙම ක්‍රියාවලිය සරල සහ වේගවත් වේ.


*Če še nikoli niste uporabljali Samourai, lahko te začetne korake preskočite in nadaljujete neposredno z namestitvijo aplikacije.*


පළමුව සහ ප්‍රධාන වශයෙන්, ඔබේ Samourai Wallet යෙදුම යාවත්කාලීන කර ඇති බව සහතික කරන්න. මෙය කිරීමට, Google Play Store පරීක්ෂා කරන්න හෝ `Settings > Other` හි ඔබේ යෙදුමේ අනුවාදය Samourai වෙබ් අඩවියේ ඇති එක සමඟ සසඳන්න.


![coinjoin](assets/notext/17.webp)


සමහරවිට ඔබේ Samourai Wallet ප්‍රතිසාධන වාක්‍යය සහ එය කියවිය හැකි බව සහතික කරන්න. එවිට, එහි නිවැරදි බව තහවුරු කිරීම සඳහා `Settings > Troubleshoot > passphrase/Backup test` වෙත ගමන් කරමින් ඔබේ BIP39 passphrase එකක් පරීක්ෂා කරන්න.


![coinjoin](assets/notext/18.webp)

ඔබේ passphrase ඇතුළත් කර, එහි වලංගුභාවය Samourai තහවුරු කරන බව සනාථ කරන්න.

![coinjoin](assets/notext/19.webp)


ඔබගේ passphrase වලංගු නොවේ නම්, හෝ ඔබගේ ප්‍රතිසාධන වාක්‍යය නොමැති නම්, ක්‍රියාවලිය වහාම නවතා දැමීම අත්‍යවශ්‍ය වේ! **මෙම මෙහෙයුම අතරතුර ඔබේ බිට්කොයින් අහිමි විය හැක.** මෙම අවස්ථාවේදී, ඔබේ මුදල් වෙනත් Wallet වෙත මාරු කිරීම සහ නව හිස් Samourai Wallet සමඟ ආරම්භ කිරීම නිර්දේශ කරයි. ඔබට අවශ්‍ය සියලුම උපස්ථ තොරතුරු ඇති බව සහ ඔබේ passphrase වලංගු බව ඔබට විශ්වාස නම් පමණක් පහත පියවර අනුගමනය කළ යුතුය.


පසුව ඔබේ Wallet හි සංකේතනය කළ උපස්ථයක් සාදමින් එය ඔබේ පසුරු පුවරුවට පිටපත් කරන්න. මෙම මෙහෙයුම සිදු කිරීමට, තිරයේ ඉහළ දකුණු කෙළවරේ පිහිටි කුඩා තිළිණ තුන මත ක්ලික් කර, පසුව `Export Wallet backup` තෝරන්න.


![coinjoin](assets/notext/20.webp)


**මෙම පියවරෙන් පසු, ඔබේ ක්ලිප්බෝඩ් එකට වෙනත් කිසිවක් පිටපත් නොකරන්න!** ඔබේ පිටපත් කළ උපස්ථය තබා ගැනීම අත්‍යවශ්‍ය වේ.


ඔබ පෙර පියවර සාර්ථකව ක්‍රියාත්මක කර ඇත්නම්, දැන් ඔබට ඔබේ Samourai Wallet ආරක්ෂිතව මකා දැමිය හැක. මෙය කිරීමට, මෙහි යන්න: `Settings > Wallet > Secure erase the Wallet`.


![coinjoin](assets/notext/21.webp)


![coinjoin](assets/notext/22.webp)


*Če še nikoli niste uporabljali Samourai in nameščate aplikacijo iz nič, lahko nadaljujete vadnico pri tem koraku.*


ඔබේ Samourai යෙදුම දැන් නැවත සකසන ලදී. යෙදුම විවෘත කර, එය පළමු වරට භාවිතා කරනවා සේ පිහිටුවීමේ පියවර සමඟ ඉදිරියට යන්න.


![coinjoin](assets/notext/23.webp)


මීළඟ පියවරේදී, ඔබේ Dojo වින්‍යාස කිරීම සඳහා කැපවූ පිටුවට ප්‍රවේශ වීමට ඔබට හැකි වේ. `Dojo` විකල්පය තෝරන්න, එවිට ඔබේ Dojo හි ලොගින් තොරතුරු ඇතුළත් කරන්න. මෙය කිරීමට, `Scan QR` ඔබා තොරතුරු ස්කෑන් කිරීමේ විකල්පය ඔබට ඇත.


![coinjoin](assets/notext/24.webp)


*Za nove uporabnike Samourai bo nato potrebno ustvariti Wallet iz nič. Če potrebujete pomoč, lahko preberete navodila za nastavitev novega Samourai Wallet [v tem priročniku, posebej v razdelku "Ustvarjanje Software Wallet"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*


If you are proceeding with the restoration of an already existing Samourai Wallet, select `Restore existing Wallet`, then choose `I have a Samourai backup file`.


![coinjoin](assets/notext/25.webp)

සාමාන්‍යයෙන්, ඔබේ ප්‍රතිසාධන ගොනුව සෑම විටම ඔබේ ක්ලිප්බෝඩ් එකේ තිබිය යුතුය. එවිට ඔබේ ගොනුව නියමිත ස්ථානයට ඇතුළත් කිරීමට `PASTE` මත ක්ලික් කරන්න. එය විකේතනය කිරීමට, ඔබේ Wallet හි BIP39 passphrase ද සටහන් කළ යුතුය, එය පහළින්ම පිහිටා ඇති සටහන් කෙරෙන ක්ෂේත්‍රයේ ඇතුළත් කළ යුතුය. අවසානයේ, `FINISH` මත ක්ලික් කරන්න.

![coinjoin](assets/notext/26.webp)


ඔබ පසුව ඔබේ Samourai Wallet වෙත යළි යොමු කෙරෙන අතර, මේ වතාවේ, එය ඔබේම Dojo එකට සම්බන්ධ වනු ඇත.


![coinjoin](assets/notext/27.webp)


### Whirlpool GUI ස්ථාපනය කිරීම

Zdaj je čas za namestitev Whirlpool GUI, grafičnega uporabniškega vmesnika Interface, ki vam bo omogočil upravljanje vaših CoinJoin ciklov iz vašega običajnega računalnika. Za uporabnike RoninDojo ta korak ni potreben, saj je upravljanje coinjoinov mogoče neposredno prek spletnega Interface v `Apps > Whirlpool`. Vendar, če uporabljate drugo rešitev Bitcoin "node-in-box", je nujno, da nadaljujete s to namestitvijo.

![coinjoin](assets/notext/28.webp)

Pojdite na svoj osebni računalnik in prenesite programsko opremo Whirlpool z uradne spletne strani Samourai Wallet, pri čemer izberite različico, ki ustreza vašemu operacijskemu sistemu.


![coinjoin](assets/notext/29.webp)


Whirlpool GUI ආරම්භ කිරීමට පෙර, ඔබේ යන්ත්‍රයේ JAVA 8 හෝ ඉහළ අනුවාදයක් ස්ථාපනය කිරීම අවශ්‍ය වේ. මෙ සඳහා, [ඔබට OpenJDK ස්ථාපනය කළ හැක](https://adoptium.net/).

![coinjoin](assets/notext/30.webp)

ඔබේ පරිගණකයේ පසුබැසීමේදී Tor daemon හෝ Tor Browser ක්‍රියාත්මක වීමද අවශ්‍ය වේ. සෑම Whirlpool GUI භාවිතා සැසියකට පෙර Tor ආරම්භ කිරීමේ විශේෂයෙන් සැලකිල්ලෙන් සිටින්න. ඔබේ යන්ත්‍රයේ Tor තවමත් ස්ථාපනය කර නොමැති නම්, [නිල ව්‍යාපෘති වෙබ් අඩවියෙන් එය බාගත කර ස්ථාපනය කළ හැක](https://www.torproject.org/download/), එවිට පසුබැසීමේදී එය ආරම්භ කිරීමේ විශේෂයෙන් සැලකිල්ලෙන් සිටින්න.


![coinjoin](assets/notext/31.webp)


JDK ඔබේ පද්ධතියේ ස්ථාපනය කර Tor පසුබැසීමේ ආරම්භ කර ඇති විට, ඔබට Whirlpool GUI ආරම්භ කළ හැක.


![coinjoin](assets/notext/32.webp)


Whirlpool GUI මගින්, ඔබේ Dojo හි ඇති Whirlpool CLI සම්බන්ධ කිරීමට `Advanced: Remote CLI` මත ක්ලික් කරන්න. ඔබේ Whirlpool CLI හි Tor Address අවශ්‍ය වනු ඇත.


![coinjoin](assets/notext/33.webp)


ඔබේ Tor Address Umbrel සහ අනෙකුත් "node-in-box" විසඳුම් මත සොයා ගැනීමට, සරලව Samourai Server හෝ Dojo යෙදුම ආරම්භ කරන්න (භාවිතා කරන මෘදුකාංගය අනුව නම වෙනස් විය හැක). Tor Address යෙදුමේ පිටුවේ සෘජුවම දෘශ්‍යමාන වේ.

![coinjoin](assets/notext/34.webp)

Whirlpool GUI හි, ඔබ පෙර ලබාගත් Tor Address `CLI Address` ක්ෂේත්‍රයේ ඇතුළත් කරන්න. `http://` ප්‍රතිලේඛනය තබා ගන්න, නමුත් අග部分ේ `:8899` වරාය එකතු නොකරන්න. Address ඔබට ලබා දුන් පරිදි පමණක් අලවන්න.

![coinjoin](assets/notext/35.webp)


V polje Tor Proxy vnesite `socks5://127.0.0.1:9050`, če uporabljate Tor daemon, ali `socks5://127.0.0.1:9150`, če uporabljate Tor Browser. Ko se prvič povežete z Whirlpool CLI prek Whirlpool GUI, je možno pustiti polje za API ključ prazno. Če to ni vaša prva povezava, prosimo, vnesite vaš API ključ v za to namenjen prostor. Ta ključ lahko najdete na isti strani kot vaš Tor Address.


![coinjoin](assets/notext/36.webp)


ඔබ සියල්ල පුරවා අවසන් කළ පසු, `Connect` බොත්තම මත ක්ලික් කරන්න. කරුණාකර රැඳී සිටින්න, සම්බන්ධතාවය සඳහා මිනිත්තු කිහිපයක් ගත විය හැක.


![coinjoin](assets/notext/37.webp)


### Samourai Wallet ને Whirlpool GUI સાથે જોડવું

*RoninDojo භාවිතා කරන්නන් සඳහා, ඔබට මෙහිදී උපකාරක පසුබැසීම නැවත ආරම්භ කළ හැක.*


Zdaj bomo seznanili Samourai Wallet, ki smo ga prej konfigurirali, s programsko opremo Whirlpool GUI ali neposredno z RoninDojo za tiste, ki uporabljajo to programsko opremo. Ne glede na to, ali uporabljate Whirlpool GUI ali RoninDojo, boste pozvani, da prilepite ali skenirate podatke za seznanjanje vašega Samourai Wallet.


![coinjoin](assets/notext/38.webp)


මෙම තොරතුරු සොයා ගැනීමට, ඔබේ Wallet හි සැකසුම් වෙත යන්න.


![coinjoin](assets/notext/39.webp)


`Transactions` මත ක්ලික් කරන්න, එවිට `Pair to Whirlpool GUI` මත ක්ලික් කරන්න.


![coinjoin](assets/notext/40.webp)


සමුරායි ඔබට සම්බන්ධතාවය ස්ථාපිත කිරීමට අවශ්‍ය තොරතුරු ලබා දෙනු ඇත. අවධානයෙන් සිටින්න, මෙම දත්ත සංවේදී වේ! ඔබට එය ඔබේ පරිගණකයට මාරු කළ හැකි අතර එය සෘජුවම පිටපත් කිරීමෙන් හෝ QR කේතය සංකේතය මත ක්ලික් කිරීමෙන් පසු ඔබේ පරිගණකයේ වෙබ් කැමරාව භාවිතා කරමින් පෙන්වන QR කේතය ස්කෑන් කිරීමෙන්.


![coinjoin](assets/notext/41.webp)


මෙම මෙහෙයුම සිදු කිරීමෙන් පසු, Whirlpool GUI හි `Initialize GUI` තෝරන්න. කරුණාකර රැඳී සිටින්න, මෙම පියවරට මොහොතක් ගත විය හැක.


![coinjoin](assets/notext/42.webp)


ඔබ Whirlpool GUI හෝ RoninDojo භාවිතා කරනවාද යන්න සලකා බැලීමේදී, ඔබේ Samourai Wallet හි passphrase ඇතුළත් කිරීමට ඔබගෙන් අයදුම් කෙරේ. එය කැපවූ ක්ෂේත්‍රයේ ඇතුළත් කරන්න, එවිට ඉදිරියට යාමට `Login` බොත්තම ඔබන්න.


![coinjoin](assets/notext/43.webp)


Whirlpool CLI मुखपृष्ठमा त्यसपछि तपाईं आइपुग्नुहुनेछ।


![coinjoin](assets/notext/44.webp)


### Whirlpool GUI මඟින් coinjoins ආරම්භ කිරීම

*RoninDojo භාවිතා කරන්නන් සඳහා, අනුගමනය කළ යුතු ක්‍රියාවලිය සමාන වේ. RoninDojo සමඟ ඒකාබද්ධ Whirlpool යෙදුම Interface, පරිගණකයේ Whirlpool GUI මෘදුකාංගය මෙන්ම ඒකාබද්ධ විකල්ප සහ ක්‍රියාකාරිතාවන් ලබා දේ. එබැවින්, ඔබට මෙම උපදෙස් එම ආකාරයෙන් අනුගමනය කළ හැක.*

දැන් සියල්ල සකස් කර ඇති බැවින්, ඔබේ බිට්කොයින් මිශ්‍ර කිරීම ආරම්භ කිරීමට ඔබ සූදානම්. මෙය කිරීමට, ඔබ මිශ්‍ර කිරීමට කැමති බිට්කොයින් ඔබේ Samourai Wallet හි **තැන්පතු** ගිණුමට මාරු කරන්න. මෙම මෙහෙයුම Samourai Wallet යෙදුම හරහා හෝ Whirlpool GUI මඟින් සෘජුවම සිදු කළ හැක. ප්‍රධාන පිටුවෙන්, ඉහළ වමට පිහිටි `+ තැන්පතු` බොත්තම ක්ලික් කරන්න.


![coinjoin](assets/notext/45.webp)


Whirlpool GUI යනු generate ලැබීමේ Address එකක් වේ. එය එක් එක් CoinJoin පොකුරට සහභාගී වීමට අවශ්‍ය අවම මුදලද පෙන්වයි. මෙම මුදල ගාස්තු වෙළඳපොල අනුව වෙනස් වේ. අවශ්‍ය අවම මුදලට වඩා ටිකක් වැඩි මුදලක් තැන්පත් කිරීම සුදුසුය, මන්ද Mining ගාස්තු අඩුවන්නේ නැත්නම්, ඔබේ UTXO අවශ්‍ය පොකුරේ පිළිගනු නොලැබිය හැක. එබැවින්, ඔබේ බිට්කොයින් ලබා දී ඇති Address වෙත යවන්න. නව Address ලබා ගැනීමට, `Renew Address` බොත්තම ක්ලික් කරන්න.


![coinjoin](assets/notext/46.webp)


කැමති.


![coinjoin](assets/notext/47.webp)


CoinJoin චක්‍ර ආරම්භ කිරීමට, ඔබ මිශ්‍ර කිරීමට කැමති UTXOs තෝරා `Premix` බොත්තම ඔබන්න. අවධානයෙන් සිටින්න: ඔබ එකවර විවිධ UTXOs කිහිපයක් තෝරන්නේ නම්, ඒවා `TX0` සූදානම් කිරීමේ ගනුදෙනුවේදී එකට එක් කෙරේ. මෙම එක් කිරීම රහස්‍යතාවය අඩු කිරීමට හේතු විය හැක, විශේෂයෙන්ම UTXOs විවිධ මූලාශ්‍රවලින් පැමිණේ නම්, සාමාන්‍ය ආදාන Ownership හියුරිස්ටික් (CIOH) නිසා.


![coinjoin](assets/notext/48.webp)


Stran za konfiguracijo Whirlpool se odpre. Izberete lahko bazen, v katerega želite vstopiti. Prav tako izberite pristojbine Mining, namenjene `TX0` in prvim coinjoinom. Na dnu te strani vam bo povzetek predstavil količino doxxic sprememb ter količino in število UTXO-jev, ki bodo izenačeni in vključeni v cikle CoinJoin. Če ste zadovoljni s to konfiguracijo, pritisnite gumb `Premix` za začetek ciklov CoinJoin.

![coinjoin](assets/notext/49.webp)


Ko je `TX0` ustvarjen, boste lahko videli svoje izenačene UTXO-je v računu **Premix**, ki čakajo na potrditev. Da bi omogočili samodejno mešanje vaših kovancev 24 ur na dan, 7 dni v tednu, priporočam aktiviranje možnosti `Automatically mix premix & postmix`. To funkcijo boste našli na zavihku `Configuration`, ki se nahaja na levi strani vašega Whirlpool GUI okna.

![coinjoin](assets/notext/50.webp)

කොයින්ජොයින් ආරම්භ කිරීමෙන් පසු, ඔබට Whirlpool GUI සහ Samourai Wallet ඉවත් කළ හැක. ඔබේ නියමිතය සම්බන්ධව තබා ගැනීම පමණක් අවශ්‍ය වේ, අඛණ්ඩ කොයින්ජොයින් වලට සහභාගී වීමට. කෙසේ වෙතත්, ඔබේ CoinJoin චක්‍ර වල ප්‍රගතිය කාලිකව පරීක්ෂා කිරීම සුදුසු වේ. ඔබේ UTXO කිහිපයක් කාලයක් සඳහා CoinJoin සඳහා තේරී නොමැති බව ඔබ දක්නට ලැබුවහොත්, මෙය දෝෂයක් පෙන්විය හැක. මෙම අවස්ථාවේදී, Whirlpool CLI වෙත ගොස් `Start` තෝරා ඔබේ කොයින්ජොයින් සඳහා ලබාගත හැකි බව නැවත ආරම්භ කරන්න.


![coinjoin](assets/notext/51.webp)


ඔබේ මිශ්‍ර UTXO-වල් **Postmix** ගිණුමෙන් Whirlpool GUI මඟින් දැකිය හැක. අමතරව, ඔබට ඒවා සෘජුවම Whirlpool Interface හරහා Samourai Wallet මඟින් දැකීමට සහ වියදම් කිරීමට විකල්පයක් ඇත. මෙම මෙනුවට ප්‍රවේශ වීමට, ඔබේ තිරයේ පහළ ඇති නිල් `+` මත ක්ලික් කරන්න, එවිට `Whirlpool` තෝරන්න.


![coinjoin](assets/notext/52.webp)


Whirlpool ගිණුම් Samourai Wallet මත ඔවුන්ගේ නිල් වර්ණය මඟින් පහසුවෙන් හඳුනාගත හැකිය. මෙය ඔබට ඔබේ මිශ්‍ර UTXO ඕනෑම තැනකින් සහ ඕනෑම වේලාවක, සෘජුවම ඔබේ ස්මාර්ට්ෆෝනයෙන් වියදම් කිරීමට ඉඩ සලසයි.


![coinjoin](assets/notext/53.webp)


ඔබේ ස්වයංක්‍රීය කෝන්ජොයින් සටහන් තබා ගැනීම සඳහා, මම Sentinel යෙදුම හරහා Watch-only wallet සකස් කිරීමද නිර්දේශ කරමි. ඔබේ **Postmix** ගිණුමේ ZPUB එක එක්කර, ඔබේ CoinJoin චක්‍රවල ප්‍රගතිය වත්මන් කාලීනව නිරීක්ෂණය කරන්න. Sentinel භාවිතා කරන ආකාරය තේරුම් ගැනීමට ඔබට අවශ්‍ය නම්, PlanB ජාලයේ මෙම වෙනත් උපකාරකය අනුගමනය කිරීමට මම නිර්දේශ කරමි: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)