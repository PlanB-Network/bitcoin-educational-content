---
name: CoinJoin - Sparrow Wallet
description: Kako izvesti CoinJoin na Sparrow Wallet?
---
![cover](assets/cover.webp)


***OPOZORILO:** Po aretaciji ustanoviteljev Samourai Wallet in zasegu njihovih strežnikov 24. aprila, orodje Whirlpool ne deluje več, tudi za posameznike, ki imajo svoj Dojo ali uporabljajo Sparrow Wallet. Vendar pa ostaja možnost, da bi to orodje lahko bilo ponovno vzpostavljeno v prihodnjih tednih ali ponovno zagnano na drugačen način. Poleg tega teoretični del tega članka ostaja pomemben za razumevanje načel in ciljev coinjoinov na splošno (ne samo Whirlpool), kot tudi za razumevanje učinkovitosti modela Whirlpool.*


_අපි මෙම නඩුවේ සංවර්ධන මෙන්ම සම්බන්ධිත මෙවලම් සම්බන්ධයෙන් ඇතිවන සංවර්ධනද ආසන්නයෙන් අනුගමනය කරමින් සිටිමු. නව තොරතුරු ලබාගත හැකි වන විට මෙම උපකාරකය යාවත්කාලීන කරන බව විශ්වාසයෙන් කියමු._


_මෙම උපකාරිකාව අධ්‍යාපනික සහ තොරතුරුමය අරමුණු සඳහා පමණක් සපයනු ලැබේ. අපි මෙම මෙවලම් අපරාධමය අරමුණු සඳහා භාවිතා කිරීම අනුමත නොකරන අතර හෝ උත්තේජනය නොකරන අතරේ. තමන්ගේ නීතිමය බල ප්‍රදේශයේ නීති වලට අනුකූලව කටයුතු කිරීම සෑම පරිශීලකයෙකුගේම වගකීමකි._


---

මෙම උපකාරිකාවේ, ඔබ CoinJoin යනු කුමක්ද සහ Sparrow Wallet මෘදුකාංගය සහ Whirlpool ක්‍රියාත්මක කිරීම භාවිතා කරමින් එය කෙසේ සිදු කරන බව ඉගෙන ගන්නාවා.


## Kaj je CoinJoin na Bitcoin?

**CoinJoin යනු Blockchain හි බිට්කොයින්වල සලකුණු හැරීම කඩන තාක්ෂණයකි**. එය ඒකම නමැති විශේෂිත ව්‍යුහයක සහයෝගී ගනුදෙනුවක් මත පදනම්ව ඇත: CoinJoin ගනුදෙනුව.


Coinjoins Bitcoin පරිශීලකයින්ගේ පෞද්ගලිකත්වය වැඩි දියුණු කරයි, බාහිර නිරීක්ෂකයින් සඳහා දාම විශ්ලේෂණය සංකීර්ණ කිරීමෙන්. ඔවුන්ගේ ව්‍යුහය විවිධ පරිශීලකයින්ගෙන් බොහෝ නානය එක් ගනුදෙනුවකට ඒකාබද්ධ කිරීමට ඉඩ සලසයි, එමඟින් පථ අඳුරු කරමින් ආදාන සහ ප්‍රතිදාන ලිපින අතර සබඳතා තීරණය කිරීම අපහසු කරයි.


CoinJoin සංකල්පය සහයෝගී ආකාරයකට පදනම්ව ඇත: ඔවුන්ගේ බිට්කොයින් මිශ්‍ර කිරීමට කැමති පරිශීලකයින් කිහිප දෙනෙකු එකම ගනුදෙනුවේ ආදාන ලෙස සමාන මුදල් තැන්පත් කරති. එවිට මෙම මුදල් සමාන වටිනාකමකින් පිටවීම් ලෙස සෑම පරිශීලකයෙකුටම නැවත බෙදා හරිනු ලැබේ. ගනුදෙනුව අවසානයේදී, ආදානයේදී හඳුනාගත් පරිශීලකයෙකු සමඟ විශේෂිත පිටවීමක් සම්බන්ධ කිරීම අසම්භාව්‍ය වේ. ආදාන සහ පිටවීම් අතර කිසිදු සෘජු සබඳතාවක් නොමැති අතර, එය පරිශීලකයින් සහ ඔවුන්ගේ UTXO අතර සම්බන්ධතාවය මෙන්ම සෑම කාසිමක ඉතිහාසයද බිඳ හෙලයි.

![coinjoin](assets/notext/1.webp)


CoinJoin ගනුදෙනුයක උදාහරණයක් (මගින් නොවේ): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


CoinJoin ක්‍රියාවලියක් සිදු කිරීමේදී, සෑම පරිශීලකයෙකුම සිය මුදල් සෑම විටම පාලනය තබා ගැනීම සහතික කරමින්, ක්‍රියාවලිය ආරම්භ වන්නේ සම්බන්ධකයෙකු විසින් ගනුදෙනුව නිර්මාණය කිරීමෙනි, එවිට එය සෑම සහභාගිවන්නෙකුටම සම්ප්‍රේෂණය කරයි. සෑම පරිශීලකයෙකුම, එය තමන්ට සුදුසු බව තහවුරු කිරීමෙන් පසු ගනුදෙනුවට අත්සන් කරයි. එකතු කළ සියලු අත්සන් අවසානයේ ගනුදෙනුවට ඒකාබද්ධ කරයි. පරිශීලකයෙකු හෝ සම්බන්ධකයෙකු විසින් CoinJoin ගනුදෙනුවේ ප්‍රතිදාන වෙනස් කිරීමක් මඟින් මුදල් වංචා කිරීමට උත්සාහයක් කළහොත්, අත්සන් වලංගු නොවන බව පෙන්වනු ඇත, එවිට නෝඩ් විසින් ගනුදෙනුව ප්‍රතික්ෂේප කරනු ඇත.


CoinJoin, Whirlpool, JoinMarket, or Wabisabi වැනි ක්‍රියාත්මක කිරීම් කිහිපයක් ඇත, සභාගිවන්නන් අතර සම්බන්ධතා කළමනාකරණය කිරීම සහ CoinJoin ගනුදෙනු වල කාර්යක්ෂමතාව වැඩි කිරීම අරමුණු කරගනිමින්.


V tem vadnici se osredotočamo na implementacijo **Whirlpool**, ki jo štejem za najučinkovitejšo rešitev za izvajanje coinjoinov na Bitcoin. Čeprav je na voljo na več denarnicah, ta vadnica izključno raziskuje njeno uporabo s programsko opremo Sparrow Wallet Desktop.

## Zakaj izvajati CoinJoins na Bitcoin?


ඕනෑම සමක පිරිසකට-පිරිසකට ගෙවීම් පද්ධතියක මුල් ගැටළුවක් වන්නේ Double-spending: මධ්‍යස්ථ අධිකාරියක් නැතිව විනිශ්චය සඳහා, දුෂ්ට පුද්ගලයින් එකම මූල්‍ය ඒකක කිහිප වතාවක් වියදම් කිරීමෙන් වළක්වා ගැනීම කෙසේද?


Satoshi නකමොටෝ මෙම ගැටලුවට විසඳුමක් ලබා දුන්නේ Bitcoin ප්‍රොටෝකෝලය හරහා, මධ්‍යස්ථ අධිකාරියකින් ස්වාධීනව ක්‍රියාත්මක වන සමානාත්මක ඉලෙක්ට්‍රොනික ගෙවීම් පද්ධතියක් ලෙසයි. ඔහුගේ සුදු කඩදාසියේ, ගෙවීම් පද්ධතිය තුළ සියලු ගනුදෙනු දෘශ්‍යමාන බව සහතික කිරීම Double-spending නොමැතිකම සහතික කිරීමේ එකම මාර්ගය බව ඔහු අවධාරණය කරයි.


සෑම සහභාගිවන්නෙකුම ගනුදෙනු පිළිබඳව දැනුවත් වන බව සහතික කිරීමට, ඒවා මහජන වශයෙන් ප්‍රකාශයට පත් කළ යුතුය. එබැවින්, Bitcoin ක්‍රියාකාරීත්වය පාරදෘශ්‍ය සහ බෙදාහැරූ යටිතල පහසුකම් මත රඳා පවතින අතර, ඕනෑම නෝඩ් මෙහෙයුම්කරුට ඉලෙක්ට්‍රොනික අත්සන දාමයන්ගේ සම්පූර්ණත්වය සහ සෑම කාසිමක ඉතිහාසය, එය Miner විසින් නිර්මාණය කිරීමේ සිට සනාථ කිරීමට ඉඩ සලසයි.


Bitcoin හි Blockchain හි පාරදෘශ්‍ය සහ බෙදා හැරීමේ ස්වභාවය යනු ඕනෑම ජාල භාවිතා කරන්නෙකුට අනෙකුත් සියලුම සහභාගීවන්නන්ගේ ගනුදෙනු අනුගමනය කර විශ්ලේෂණය කළ හැකි බවයි. ඒ අනුව, ගනුදෙනු මට්ටමේ අනන්‍යතාවය අසම්භාවිතයි. කෙසේ වෙතත්, පුද්ගලික හඳුනාගැනීම මට්ටමේ අනන්‍යතාවය ආරක්ෂා කරයි. සම්ප්‍රදායික බැංකු පද්ධතියේ සෑම ගිණුමක්ම පුද්ගලික හැඳුනුම්පතකට සම්බන්ධ වන අතර, Bitcoin හිදී, මුදල් සංකේතමය යතුරු යුගල් සමඟ සම්බන්ධ වන අතර, එමඟින් පරිශීලකයින්ට සංකේතමය හඳුනාගැනීම් පිටුපස පසුනම්කමක් ලබා දේ.


එබැවින්, Bitcoin පිළිබඳ රහස්‍යභාවය බිඳ වැටේන්නේ බාහිර නිරීක්ෂකයින් විශේෂිත UTXO පරිශීලකයින් සමඟ සම්බන්ධ කිරීමට සමත් වන විටයි. මෙම සම්බන්ධතාවය ස්ථාපිත වූ විට, ඔවුන්ගේ ගනුදෙනු හඹා යාම සහ ඔවුන්ගේ බිට්කොයින් ඉතිහාසය විශ්ලේෂණය කිරීම හැකි වේ. CoinJoin යනු UTXO වල හඹා යාමේ හැකියාව බිඳ දැමීමට සංවර්ධනය කරන ලද ක්‍රමවේදයක් වන අතර, එමඟින් ගනුදෙනු මට්ටමේ Bitcoin පරිශීලකයින්ට විශේෂ Layer රහස්‍යභාවයක් ලබා දේ.


## Whirlpool කෙසේ ක්‍රියා කරයිද?


Whirlpool अन्य CoinJoin ක්‍රමවලින් වෙනස් වන්නේ "_ZeroLink_" ගනුදෙනු භාවිතා කිරීමෙනි, එය සියලුම ආදාන සහ සියලුම නිමාවන් අතර තාක්ෂණික සම්බන්ධයක් නොමැති බව සහතික කරයි. මෙම පරිපූර්ණ මිශ්‍ර කිරීම, එක් එක් සහභාගිවන්තියා ආදානයේ සමාන මුදලක් දායක වන ව්‍යුහයක් මඟින් සකස් කරනු ලබන අතර (Mining ගාස්තු හැර), එමඟින් සම්පූර්ණයෙන් සමාන මුදල් නිමාවන් ජනනය කරයි.


ආදාන මත මෙම සීමාකාරී ආකල්පය Whirlpool CoinJoin ගනුදෙනු සඳහා අනන්‍ය ලක්ෂණයක් ලබා දේ: ආදාන සහ ප්‍රතිදාන අතර නියමිත සබැඳි සම්පූර්ණයෙන්ම නොමැති වීම. වෙනත් වචන වලින්, සෑම ප්‍රතිදානයක්ම ගනුදෙනුවේ අනෙකුත් සියලුම ප්‍රතිදාන සමඟ සසඳන විට, ඕනෑම සහභාගිවන්නෙකුට පිරිනැමීමේ සමාන සම්භාවිතාවක් ඇත.

ආරම්භයේදී, එක් එක් Whirlpool CoinJoin හි සහභාගීවන්නන්ගේ සංඛ්‍යාව 5 දක්වා සීමා විය, නව ප්‍රවේශකයින් 2ක් සහ රිමික්සර් 3ක් (අපි මෙම සංකල්ප ඉදිරියට විස්තර කරමු). කෙසේ වෙතත්, 2023 දී දැක්වූ On-Chain ගනුදෙනු ගාස්තු වැඩිවීම Samourai කණ්ඩායම්වලට පෞද්ගලිකත්වය වැඩි දියුණු කරමින් පිරිවැය අඩු කිරීම සඳහා ඔවුන්ගේ ආකෘතිය නැවත සිතීමට ප්‍රේරණ විය. එබැවින්, ගාස්තු සහ සහභාගීවන්නන්ගේ සංඛ්‍යාව පිළිබඳව වෙළඳපොළ තත්ත්වය සැලකිල්ලට ගනිමින්, සම්බන්ධකරු දැන් 6, 7, හෝ 8 සහභාගීවන්නන් ඇතුළත් coinjoins සංවිධානය කළ හැක. මෙම වර්ධිත සැසි "_Surge Cycles_" ලෙස හැඳින්වේ. සැකසීම කුමක් වුවත්, Whirlpool coinjoins හි නව ප්‍රවේශකයින් 2ක් පමණක් සිටින බව සටහන් කර ගැනීම වැදගත්ය.


අදාළව, Whirlpool ගනුදෙනු සමාන සංඛ්‍යාත ආදාන සහ ප්‍රතිදාන මගින් ලක්ෂණය කරනු ලබන අතර, එය විය හැක:


- 5 ආදාන සහ 5 ප්‍රතිදාන;

![coinjoin](assets/notext/2.webp)


- 6 ආදාන සහ 6 ප්‍රතිදාන;

![coinjoin](assets/notext/3.webp)


- 7 ආදාන සහ 7 ප්‍රතිදාන;

![coinjoin](assets/notext/4.webp)


- 8 ආදාන සහ 8 ප්‍රතිදාන.

![coinjoin](assets/notext/5.webp)

Whirlpool විසින් යෝජනා කරන ලද ආකෘතිය එබැවින් කුඩා CoinJoin ගනුදෙනු මත පදනම්ව ඇත. Wasabi සහ JoinMarket මෙන් නොව, එක් චක්‍රයකදී සහභාගීවන්නන්ගේ පරිමාව මත anonsets හි ශක්තිමත්කම රඳා පවතින අතර, Whirlpool කුඩා ප්‍රමාණයේ චක්‍ර කිහිපයක් සම්බන්ධ කිරීම මත පදනම්ව පවතී.


මෙම ආකෘතියේ, පරිශීලකයාට මුලින්ම තටාකයකට ඇතුල්වීමේදී පමණක් ගාස්තු අයකරන අතර, අමතර ගාස්තු නැතිව විවිධ රිමික්ස්වලට සහභාගී විය හැක. නව ප්‍රවේශකයින්ට රිමික්ස්කරුවන් සඳහා Mining ගාස්තු භාරගත යුතුය.


CoinJoin සමඟ එක් එක් නව කාසි සහභාගී වීමකදී, එහි අතීතයේ හමුවූ සමාන කාසි සමඟ, anonsets ගුණාත්මකව වර්ධනය වේ. එබැවින් අරමුණ වන්නේ මෙම නොමිලේ ඇති remixes වලින් ප්‍රයෝජනය ගැනීමයි, ඒවා එක් එක් අවස්ථාවකදී, එක් එක් මිශ්‍රිත කාසිය සමඟ සම්බන්ධිත anonsets වල ඝනත්වය ශක්තිමත් කිරීමට දායක වේ.


Whirlpool යන්ත්‍රය නිර්මාණය කරන ලද්දේ වැදගත් අවශ්‍යතා දෙකක් සැලකිල්ලට ගනිමින්:


- Samourai Wallet යනු ප්‍රධාන වශයෙන් ස්මාර්ට්ෆෝන් යෙදුමක් වන බැවින්, ජංගම උපාංගවල ක්‍රියාත්මක කිරීමේ ප්‍රවේශය;
- රිමික්සින් සයිකල් වල වේගය අනොන්සෙට්ස් වල වැදගත් වර්ධනයක් ප්‍රවර්ධනය කිරීමට.


මෙම අණපද Whirlpool නිර්මාණය කිරීමේදී Samourai Wallet සංවර්ධකයින්ගේ තේරීම් මඟ පෙන්වීය, ඔවුන්ට සයිකල් එකකට සහභාගීවන්නන්ගේ සංඛ්‍යාව සීමා කිරීමට හේතු විය. අඩු සහභාගීවන්නන් සංඛ්‍යාවක් CoinJoin කාර්යක්ෂමතාවයට බාධා කළේය, සෑම සයිකලයකදීම ජනිත වන anonsets දැඩි ලෙස අඩු කරමින්, එසේම වැඩි සහභාගීවන්නන් සංඛ්‍යාවක් ජංගම යෙදුම් මත කළමනාකරණ ගැටළු ඇති කළ අතර සයිකල් වල ප්‍රවාහය බාධා කළේය.


**Končno, ni potrebe po visokem številu udeležencev na CoinJoin na Whirlpool, saj so anonseti narejeni preko akumulacije več ciklov CoinJoin.**

[-> Whirlpool anonsets පිළිබඳව වැඩිදුරටත් ඉගෙන ගන්න.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### CoinJoin කුලු සහ ගාස්තු

බහුවිධ චක්‍ර සාර්ථකව මිශ්‍ර කළ නාණයවල anonsets වැඩි කිරීමට, භාවිතා කරන UTXOs ප්‍රමාණ සීමා කිරීමට විශේෂිත රාමුවක් ස්ථාපිත කළ යුතුය. Whirlpool මෙම අරමුණ සඳහා විවිධ තටාක අර්ථ දක්වයි.


පිහිනුම් තටාකයක් යනු එකට මිශ්‍ර වීමට කැමති පරිශීලක කණ්ඩායමක් නියෝජනය කරන අතර, CoinJoin ක්‍රියාවලිය උපරිම කිරීමට UTXOs ප්‍රමාණය පිළිබඳ එකඟ වේ. එක් එක් පිහිනුම් තටාකය UTXO සඳහා ස්ථිර ප්‍රමාණයක් නියම කර ඇති අතර, සහභාගී වීමට පරිශීලකයා එයට අනුකූල විය යුතුය. එබැවින්, Whirlpool සමඟ කාසි සම්බන්ධ කිරීමට, ඔබට පිහිනුම් තටාකයක් තෝරා ගත යුතුය. දැනට ලබා ගත හැකි පිහිනුම් තටාක පහත පරිදි වේ:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100,000 Sats).


ඔබේ බිට්කොයින් සමඟ පොකුරකට එක්වීමෙන්, ඒවා generate UTXOs ලෙස බෙදා හරින අතර, ඒවා පොකුරේ අනෙකුත් සහභාගීවන්නන්ගේ ඒවා සමඟ පූර්ණ සමාන වේ. එක් එක් පොකුරකට උපරිම සීමාවක් ඇත; එබැවින්, මෙම සීමාව ඉක්මවන මුදල් සඳහා, ඔබට එකම පොකුර තුළ වෙන්වූ ඇතුළත් කිරීම් දෙකක් කිරීමට හෝ වැඩි මුදලක් සහිත වෙනත් පොකුරකට ගමන් කිරීමට බල කෙරේ:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

පෙර සඳහන් කළ පරිදි, UTXO එකක් CoinJoin එකකට ඒකාබද්ධ කිරීමට සූදානම් වන විට එය තටාකයකට අයත් වේ යැයි සැලකේ. කෙසේ වෙතත්, මෙය පරිශීලකයා එය අත්හැර දමන බව අර්ථ දක්වන්නේ නැත. **විවිධ මිශ්‍රණ චක්‍ර හරහා, ඔබේ යතුරු සහ, ඒ අනුව, ඔබේ බිට්කොයින් සම්පූර්ණයෙන්ම පාලනය කරගෙන යාමට ඔබට හැකිය.** මෙය CoinJoin තාක්ෂණය වෙනත් මධ්‍යස්ථ මිශ්‍රණ තාක්ෂණවලින් වෙනස් කරයි.


CoinJoin කුළුවට ඇතුළුවීමට, සේවා ගාස්තු මෙන්ම Mining ගාස්තුද ගෙවිය යුතුය. සේවා ගාස්තු සෑම කුළුවකටම ස්ථිර වන අතර Whirlpool සංවර්ධනය සහ නඩත්තු කිරීම සඳහා වගකියන කණ්ඩායම් සඳහා වන්දි ලබා දීමට අදහස් කරයි. Sparrow Wallet පරිශීලකයින් සඳහා, මෙම ගාස්තු Samourai කණ්ඩායම් විසින් Sparrow සංවර්ධකයින්ට ලබා දේ.


Whirlpool භාවිතා කිරීම සඳහා සේවා ගාස්තු තටාකයට ඇතුළු වීමේදී වරක් ගෙවිය යුතුය. මෙම පියවර සම්පූර්ණ වූ විට, අමතර ගාස්තු නොමැතිව සීමාවක් නොමැති රිමික්ස් සංඛ්‍යාවකට සහභාගී වීමට ඔබට අවස්ථාව ඇත. මෙන්න සෑම තටාකයකම වත්මන් ස්ථිර ගාස්තු:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


මෙම ගාස්තු මූලික වශයෙන් ක්‍රියා කරන්නේ තෝරාගත් තටාකයට ප්‍රවේශ පත්‍රයක් ලෙසයි, ඔබ CoinJoin තුළ දැමූ මුදල කුමක් වුවත්. එසේ නම්, ඔබ 0.01 BTC සමඟ නිවැරදිව 0.01 තටාකයට එක්වුවත් හෝ 0.5 BTC සමඟ ඇතුළත් වුවත්, ගාස්තු සම්පූර්ණ වශයෙන් එකසේ පවතී.


කොයින්ජොයින්ස් සමඟ ඉදිරියට යාමට පෙර, එම නිසා පරිශීලකයාට යාමට පෙර 2 යාන්ත්‍රණ අතර තේරීමක් ඇත:


- සෙවිකා ගාස්තු අවම කිරීම සඳහා කුඩා තටාකයක් තෝරන්න, ඔවුන්ට ප්‍රතිලාභ ලෙස කුඩා UTXO කිහිපයක් ලැබෙන බව දැන සිටිමින්;
- Ali pa raje izberite večji bazen in se strinjate s plačilom višjih pristojbin, da bi na koncu imeli manjše število UTXO-jev z večjo vrednostjo.


සාමාන්‍යයෙන් CoinJoin චක්‍රයන් පසු විවිධ මිශ්‍ර UTXO එකතු කිරීමෙන් වළකින්නැයි උපදෙස් දෙන අතර, මෙය ලබාගත් රහස්‍යභාවය අවදානමට ලක් කළ හැකි අතර, විශේෂයෙන් Common-Input-Ownership Heuristic (CIOH) නිසාය. එබැවින්, වැඩි ගාස්තුවක් ගෙවීමට සිදු වුවත්, වැඩි පූල් එකක් තෝරා ගැනීම සුදුසු විය හැක, ප්‍රතිදානය ලෙස අතිශය කුඩා වටිනාකම් ඇති UTXO නොමැතිවීම සඳහා. පරිශීලකයාට ඔවුන් කැමති පූල් එක තෝරා ගැනීම සඳහා මෙම වෙළඳපොළ මාරු කිරීම් තීරණය කළ යුතුය.


සේවා ගාස්තු වලට අමතරව, ඕනෑම Bitcoin ගනුදෙනුවකට අයත් Mining ගාස්තු ද සලකා බැලිය යුතුය. Whirlpool පරිශීලකයෙකු ලෙස, ඔබට සකස් කිරීමේ ගනුදෙනුව (`Tx0`) සඳහා Mining ගාස්තු සහ පළමු CoinJoin සඳහා ගෙවීමට අවශ්‍ය වේ. Whirlpool මෝඩලය නව ප්‍රවේශකයින්ගේ ගෙවීම් මත රඳා පවතින බැවින්, පසුව සිදු කරන සියලුම රිමික්ස් නොමිලේ වනු ඇත.


ඇත්ත වශයෙන්ම, සෑම Whirlpool CoinJoin හිමියන්ටම, ආදාන අතර නව ප්‍රවේශකයින් දෙදෙනෙකු සිටී. අනෙකුත් ආදාන රිමික්සර්වරුන්ගෙන් පැමිණේ. එම නිසා, ගනුදෙනුවේ සියලුම සහභාගීවන්නන් සඳහා Mining ගාස්තු මෙම නව සහභාගීවන්නන් දෙදෙනා විසින් ආවරණය කරනු ලබන අතර, ඔවුන්ටද නොමිලේ රිමික්ස් වලින් ප්‍රයෝජනයක් ලැබේ:

![coinjoin](assets/en/6.webp)

මෙම ගාස්තු පද්ධතියට ස්තූතියි, Whirlpool සැබවින්ම වෙනස් වේ CoinJoin සේවාවන්ගෙන්, UTXO වල anonsets පරිශීලකයා විසින් ගෙවූ මිලට සමානුපාතික නොවන බැවින්. එබැවින්, තටුකාරකගේ ප්‍රවේශ ගාස්තු සහ දෙකක් සඳහා Mining ගාස්තු පමණක් ගෙවා ඉතා ඉහළ මට්ටමේ අනන්‍යතාවයක් ලබා ගැනීමේ හැකියාව ඇත ( `Tx0` සහ මුල් මිශ්‍රණය).


මෙමගින් සටහන් කළ යුතු වන්නේ, පරිශීලකයා තම බහු කෝයින්ජොයින්ස් සම්පූර්ණ කිරීමෙන් පසු, තම UTXOs මුදල් තැන්පත් කරගැනීම සඳහා Mining ගාස්තු ද ආවරණය කළ යුතු වන බවයි, ඔවුන් `mix to` විකල්පය තෝරා නොමැති නම්, එය අපි පහත උපකාරකයෙහි සාකච්ඡා කරමු.


### HD Wallet ගිණුම් Whirlpool විසින් භාවිතා කරන ලදී.

Whirlpool හරහා CoinJoin ක්‍රියාත්මක කිරීමට, Wallet ට generate විවිධ ගිණුම් කිහිපයක් අවශ්‍ය වේ. HD (Hierarchical Deterministic) Wallet සන්දර්භය තුළ ගිණුමක් යනු සම්පූර්ණයෙන්ම අනෙක් ගිණුම් වලින් වෙන්වූ කොටසක් වන අතර, මෙම වෙන්වීම සිදුවන්නේ Wallet හි පරිපාලන ව්‍යුහයේ තුන්වන ගැඹුරු මට්ටමේදී, එනම්, `xpub` මට්ටමේදීය.

HD Wallet සංකල්පයෙන් සෛද්ධාන්තිකව `2^(32/2)` විවිධ ගිණුම් ලබා ගත හැක. සියලුම Bitcoin පසුම්බි වල පෙරනිමි ලෙස භාවිතා කරන ආරම්භක ගිණුම, දර්ශකය `0'` ට අනුකූල වේ.


Whirlpool සඳහා අනුකූලිත පසුම්බි සඳහා, Samourai හෝ Sparrow වැනි, CoinJoin ක්‍රියාවලියේ අවශ්‍යතා සපුරාලීම සඳහා ගිණුම් 4 ක් භාවිතා කරයි:


- **ඇපකිරීම** ගිණුම, `0'` දර්ශකය මගින් හඳුනාගන්නා;
- **බැඩ් බැංකු** (හෝ ඩොක්සික් වෙනස්කම්) ගිණුම, `2 147 483 644'` දර්ශකය මගින් හඳුනාගෙන ඇත;
- **premix** ගිණුම, `2 147 483 645'` දර්ශකය මගින් හඳුනාගෙන ඇත;
- **postmix** ගිණුම, `2 147 483 646'` දර්ශකය මඟින් හඳුනාගෙන ඇත.


CoinJoin තුළ මෙම ගිණුම් සෑම එකක්ම විශේෂිත කාර්යයක් ඉටු කරයි.


මෙම සියලුම ගිණුම් seed එකකට සම්බන්ධ වේ, එය පරිශීලකයාට ඔවුන්ගේ සියලුම බිට්කොයින් නැවත ලබා ගැනීමට, ඔවුන්ගේ නැවත ලබා ගැනීමේ වාක්‍යය සහ, අදාල නම්, ඔවුන්ගේ passphrase භාවිතා කිරීමෙන් ඉඩ සලසයි. කෙසේ වෙතත්, මෙම නැවත ලබා ගැනීමේ මෙහෙයුම අතරතුර, භාවිතා කරන ලද විවිධ ගිණුම් දර්ශක මෘදුකාංගයට විශේෂිත කිරීම අවශ්‍ය වේ.


අපි දැන් මෙම ගිණුම් තුළ Whirlpool CoinJoin හි විවිධ අදියරවල් බලමු.


### Whirlpool මත coinjoins හි විවිධ අදියරයන්

**පළමු අදියර: Tx0**

Whirlpool CoinJoin යාන්ත්‍රයේ ආරම්භක ස්ථානය වන්නේ **තැන්පතු** ගිණුමයි. ඔබ නව Bitcoin Wallet එකක් සාදන විට ස්වයංක්‍රීයව භාවිතා කරන ගිණුම මෙයයි. ඔබ මිශ්‍ර කිරීමට කැමති බිට්කොයින් මෙම ගිණුමට ණය කළ යුතුය.


`Tx0` Whirlpool මිශ්‍රණ ක්‍රියාවලියේ පළමු අදියර නිරූපණය කරයි. එය CoinJoin සඳහා UTXO සකස් කිරීම සහ සමාන කිරීම අරමුණු කර ගනී, මිශ්‍රණයේ සමානත්වය සහතික කිරීම සඳහා, තෝරාගත් තටාකයේ ප්‍රමාණයට අනුකූල ඒකකවලට ඒවා බෙදීමෙන්. සමාන කළ UTXO පසුව **පූර්ව මිශ්‍රණ** ගිණුමට යවයි. තටාකයට ඇතුළු විය නොහැකි වෙනසක් සම්බන්ධයෙන්, එය විශේෂිත ගිණුමකට වෙන් කරයි: **නරක බැංකුව** (හෝ "doxxic change").


මෙම ආරම්භක ගනුදෙනුව `Tx0` මාර්ගය සම්බන්ධකයාට ගෙවිය යුතු සේවා ගාස්තු විසඳීමට ද සේවය කරයි. පසුගිය අදියරවලට වඩා වෙනස්ව, මෙම ගනුදෙනුව සහයෝගී නොවේ; එබැවින් පරිශීලකයා සම්පූර්ණ Mining ගාස්තු භාරගත යුතුය:

![coinjoin](assets/en/7.webp)

මෙම `Tx0` ගනුදෙනුවේ උදාහරණයේදී, අපගේ **තැන්පතු** ගිණුමෙන් `372,000 Sats` ආදානයක් විවිධ පිටත් වන UTXO වෙත බෙදා හරින අතර, ඒවා පහත පරිදි බෙදා හැරේ:


- `100,000 Sats`-ට පිවිසීම සඳහා, සේවා ගාස්තු සඳහා සම්බන්ධකරුට අදාල `5,000 Sats` මුදලක්;
- මූලික මිශ්‍රණය සඳහා UTXO තුනක් සකසා, අපගේ **premix** ගිණුමට යළියොමුවී සම්බන්ධකය සමඟ ලියාපදිංචි කර ඇත. මෙම UTXO සමාන කර ඇත `108,000 Sats` බැගින්, ඔවුන්ගේ අනාගත මූලික මිශ්‍රණය සඳහා Mining ගාස්තු ආවරණය කිරීම සඳහා;
- අතිරික්තය, එය අධික ලෙස කුඩා බැවින් තටාකයට ඇතුල් විය නොහැකි වන අතර, විෂමය වෙනසක් ලෙස සැලකේ. එය එහි විශේෂිත ගිණුමට යවනු ලැබේ. මෙහි, මෙම වෙනස `40,000 Sats` වේ;
- අවසානයේ, `3,000 Sats` ක් ඇත, එහෙත් එය නිමැවුමක් නොවන අතර, `Tx0` තහවුරු කිරීමට අවශ්‍ය Mining ගාස්තු වේ.


උදාහරණයක් ලෙස, මෙන්න සත්‍ය Tx0 Whirlpool (මගින් නොවන): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**2. korak: Strupena sprememba**

අතිරික්තය, තටාකයට ඒකාබද්ධ වීමට නොහැකි වූ, මෙහි `40,000 Sats` සමාන වන අතර, **නරක බැංකු** ගිණුමට, "විෂ ව්‍යුහය" ලෙසද හැඳින්වෙයි, වෙනත් UTXOs වලින් Wallet තුළ දැඩි වෙන් කිරීමක් සහතික කිරීම සඳහා යළි මාරු කෙරේ.


यो UTXO प्रयोगकर्ताको गोपनीयताको लागि खतरनाक छ किनभने यो मात्र यसको विगतसँग सधैं जोडिएको छैन, र त्यसैले सम्भवतः यसको मालिकको पहिचानसँग पनि, तर थप रूपमा, यो CoinJoin प्रदर्शन गरेको प्रयोगकर्तासँग सम्बन्धित भएको रूपमा नोट गरिएको छ।


මෙම UTXO එකතු කරන ලද්දේ මිශ්‍ර ප්‍රතිදාන සමඟ නම්, පසුගිය CoinJoin චක්‍රවලදී ලබා ගත් සියලුම පෞද්ගලිකත්වය අහිමි වනු ඇත, විශේෂයෙන් CIOH (*Common-Input-Ownership-Heuristic*) නිසා. එය අනෙකුත් විෂ සහිත වෙනස්කම් සමඟ එකතු කරන ලද්දේ නම්, පරිශීලකයාට පෞද්ගලිකත්වය අහිමි වීමේ අවදානමක් ඇත, මන්ද මෙය CoinJoin චක්‍රවල විවිධ ඇතුල්කිරීම් සම්බන්ධ කරනු ඇත. එබැවින් එය අවධානයෙන් සලකා බැලිය යුතුය. මෙම විෂ UTXO කළමනාකරණය කරන ආකාරය මෙම ලිපියේ අවසාන කොටසේ විස්තර කරනු ඇත, සහ අනාගත උපකාරක පංති PlanB ජාලය මත මෙම ක්‍රමවලට ගැඹුරින් පිවිසෙනු ඇත.


**3. korak: Začetno mešanje**

`Tx0` සම්පූර්ණ කිරීමෙන් පසු, සමාන කළ UTXOs අපගේ Wallet හි **premix** ගිණුමට යවනු ලබන අතර, ඒවා CoinJoin හි පළමු චක්‍රය සඳහා හඳුන්වා දීමට සූදානම් වේ, "මුල් මිශ්‍රණය" ලෙසද හැඳින්වේ. අපගේ උදාහරණය මෙන්, `Tx0` මිශ්‍ර කිරීම සඳහා බහු UTXOs ජනනය කරන විට, ඒවායේ එක් එක් එකක් වෙන වෙනම මුල් CoinJoin එකකට ඒකාබද්ධ කෙරේ.

Na koncu teh začetnih mešanj bo račun **premix** prazen, medtem ko bodo naši kovanci, ki so plačali pristojbine Mining za ta prvi CoinJoin, prilagojeni natančno na znesek, določen z izbranim bazenom. V našem primeru bodo naši začetni UTXO-ji `108 000 Sats` zmanjšani na natančno `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**පියවර 4: නැවත මිශ්‍ර කිරීම්**

මුල් මිශ්‍රණයෙන් පසු, UTXO **postmix** ගිණුමට මාරු කෙරේ. මෙම ගිණුම දැනටමත් මිශ්‍රිත UTXO සහ නැවත මිශ්‍ර කිරීමට බලාපොරොත්තු වන UTXO එකතු කරයි. Whirlpool පාරිභෝගිකයා සක්‍රීය වන විට, **postmix** ගිණුමේ පිහිටා ඇති UTXO ස්වයංක්‍රීයව නැවත මිශ්‍ර කිරීමට ලබා ගත හැකි අතර මෙම නව චක්‍රවලට සහභාගී වීමට අහඹු ලෙස තෝරා ගනු ලැබේ.


සමීක්ෂණයක් ලෙස, නැවත මිශ්‍ර කිරීම් 100% නොමිලේ: අමතර සේවා ගාස්තු හෝ Mining ගාස්තු අවශ්‍ය නොවේ. **පෝස්ට්මික්ස්** ගිණුමේ UTXOs තබා ගැනීමෙන් ඔවුන්ගේ වටිනාකම අඛණ්ඩව පවත්වා ගනී, සහ ඒ සමගම ඔවුන්ගේ අනෝන්සෙට්ස් වැඩි දියුණු කරයි. එබැවින් මෙම කාසි බහු CoinJoin චක්‍රවලට සහභාගී වීමට ඉඩ දීම වැදගත් වේ. එය ඔබට කිසිවක් වැය නොවේ, සහ එය ඔවුන්ගේ අනන්‍යතාව මට්ටම් වැඩි කරයි.


ඔබ මිශ්‍ර UTXO වියදම් කිරීමට තීරණය කරන විට, ඔබට එය මෙම **postmix** ගිණුමෙන් සෘජුවම කළ හැක. නිදහස් නැවත මිශ්‍ර කිරීම් වලින් ප්‍රයෝජන ගැනීමට සහ ඔවුන්ගේ පෞද්ගලිකත්වය අඩු කළ හැකි Whirlpool පරිපථයෙන් පිටවීම වැළැක්වීමට මිශ්‍ර UTXO මෙම ගිණුමේ තබා ගැනීම සුදුසුය.


ජානයේදී අපි දැක බලාගන්නා පරිදි, `mix to` විකල්පය ද ඇත, එය ඔබේ මිශ්‍ර කළ කාසි ස්වයංක්‍රීයව වෙනත් Wallet, උදාහරණයක් ලෙස Cold Wallet, වෙත යැවීමේ හැකියාව ලබා දේ, නියමිත සංඛ්‍යාතයක් coinjoins පසු.


සිතියම් සාකච්ඡා කිරීමෙන් පසු, Sparrow Wallet ඩෙස්ක්ටොප් මෘදුකාංගය හරහා Whirlpool භාවිතය පිළිබඳ උපකාරකය සමඟ පුහුණුවට මුලපිරෙමු!


## Vodič: CoinJoin Whirlpool na Sparrow Wallet

Whirlpool uporabljate na več načinov. Prva možnost, ki vam jo želim predstaviti, je možnost Sparrow Wallet, odprtokodna programska oprema za upravljanje Bitcoin Wallet za računalnike.

Sparrow භාවිතා කිරීමේ වාසිය වන්නේ ආරම්භ කිරීමට ඉතා පහසු වීම, ඉක්මනින් පිහිටුවීම, සහ පරිගණකයක් සහ අන්තර්ජාල සම්බන්ධතාවයක් හැර වෙනත් උපකරණ අවශ්‍ය නොවීමයි. කෙසේ වෙතත්, සුවිශේෂී අවාසියක් ඇත: Sparrow ආරම්භ කර සම්බන්ධ වූ විට පමණක් coinjoins සිදු වේ. මෙය අදහස් කරන්නේ ඔබේ බිට්කොයින් 24/7 මිශ්‍ර කිරීමට සහ නැවත මිශ්‍ර කිරීමට අවශ්‍ය නම්, ඔබේ පරිගණකය නිතරම ක්‍රියාත්මක තබා ගත යුතුය.


### Sparrow Wallet ස්ථාපනය කරන්න

ආරම්භ කිරීමට, ඔබට නිසැකවම Sparrow Wallet මෘදුකාංගය අවශ්‍ය වනු ඇත. ඔබට එය සෘජුවම [නිල වෙබ් අඩවියෙන්](https://sparrowwallet.com/download/) හෝ [ඔවුන්ගේ GitHub](https://github.com/sparrowwallet/sparrow/releases) මඟින් බාගත කළ හැක.


මෘදුකාංගය ස්ථාපනය කිරීමට පෙර, ඔබ නවතමයෙන් බාගත කළ ක්‍රියාත්මක කළ හැකි ගොනුවේ අත්සන සහ අඛණ්ඩතාව සනාථ කිරීම වැදගත් වේ. Sparrow මෘදුකාංගය ස්ථාපනය කිරීමේ ක්‍රියාවලිය සහ සනාථ කිරීම පිළිබඳ වැඩි විස්තර අවශ්‍ය නම්, මම ඔබට මෙම වෙනත් උපකාරකය කියවීමට උපදෙස් දෙමි: *[The Sparrow Wallet Guides](https://planb.network/tutorials/Wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)*


### Software Wallet සාදන්න

මෘදුකාංගය ස්ථාපනය කිරීමෙන් පසු, ඔබට Bitcoin Wallet එකක් නිර්මාණය කිරීමට ඉදිරියට යාමට අවශ්‍ය වේ. කාන්ඩායම් වලට සහභාගී වීමට, Software Wallet (ඊට "Hot Wallet" ලෙසද හැඳින්වේ) භාවිතය අත්‍යවශ්‍ය බව සටහන් කර ගැනීම වැදගත් වේ. එබැවින්, **Hardware Wallet මඟින් ආරක්ෂා කරන ලද Wallet සමඟ කාන්ඩායම් සිදු කිරීම නොහැකි වේ**.


čeprav to ni nujno, je v primeru, da nameravate mešati večje količine, zelo priporočljivo izbrati uporabo močnega BIP39 passphrase za ta Wallet.


Wallet නවයක් නිර්මාණය කිරීමට, Sparrow විවෘත කරන්න, එවිට `ගොනුව` ටැබය සහ `නව Wallet` ක්ලික් කරන්න.


![sparrow](assets/notext/9.webp)


Izberite ime za to Wallet, na primer: "CoinJoin Wallet". Kliknite na gumb `Ustvari Wallet`.


![sparrow](assets/notext/10.webp)


පෙරනිමි සැකසුම් අත්හැර, `New or Imported Software Wallet` බොත්තම ක්ලික් කරන්න.


![sparrow](assets/notext/11.webp)


Ko dostopate do okna za ustvarjanje Wallet, priporočam izbiro zaporedja 12 besed, saj je to povsem dovolj. Izberite `generate New` za generate novo obnovitveno frazo in kliknite na `Use passphrase`, če želite dodati BIP39 passphrase. Pomembno je, da naredite fizično varnostno kopijo vaših obnovitvenih informacij, bodisi na papirju ali na kovinski podlagi, da zagotovite varnost vaših bitcoinov.


![sparrow](assets/notext/12.webp)

ඔබේ ප්‍රතිසාධන වාක්‍ය කේතය පිටපත් කිරීමේ වලංගුකම සහතික කර, `Confirm Backup...` මත ක්ලික් කිරීමට පෙර. එවිට Sparrow ඔබට නැවත ඔබේ වාක්‍ය ඇතුළත් කරන ලෙස ඉල්ලා සිටින අතර, ඔබ එය සටහන් කරගෙන ඇති බව තහවුරු කරයි. මෙම පියවර සම්පූර්ණ වූ විට, `Create Keystore` මත ක්ලික් කිරීමෙන් ඉදිරියට යන්න.

![sparrow](assets/notext/13.webp)


පෙරනිමි ලෙස යෝජිත ව්‍යුත්පන්න මාර්ගය තබා `Import Keystore` ඔබන්න. මගේ උදාහරණයේ, මම මෙම උපකාරය සඳහා Testnet භාවිතා කරන බැවින් ව්‍යුත්පන්න මාර්ගය ස්වල්පයක් වෙනස් වේ. ඔබට පෙනිය යුතු ව්‍යුත්පන්න මාර්ගය මෙසේය:

```plaintext
m/84'/0'/0'
```


![sparrow](assets/notext/14.webp)


ඊට පසු, Sparrow ඔබේ නව Wallet හි ව්‍යුත්පන්න විස්තර පෙන්වනු ඇත. ඔබ passphrase සකසා ඇති නම්, ඔබේ `Master fingerprint` සටහන් කර ගැනීම ඉතාමත්ම නිර්දේශ කරනු ලැබේ. මෙම මහාචාර්ය යතුරු සලකුණ සංවේදී දත්ත නොවුවද, ඔබට පසුව නිවැරදි Wallet වෙත ප්‍රවේශ වීම සහ passphrase ඇතුළත් කිරීමේ දෝෂ නොමැතිකම තහවුරු කිරීම සඳහා මෙය ප්‍රයෝජනවත් වනු ඇත.


`Apply` බොත්තම මත ක්ලික් කරන්න.


![sparrow](assets/notext/15.webp)


Sparrow vás vabi, da ustvarite geslo za vaš Wallet. To geslo bo potrebno za dostop do njega prek programske opreme Sparrow Wallet. Izberite močno geslo, naredite njegovo varnostno kopijo in nato kliknite na `Set Password`.


![sparrow](assets/notext/16.webp)


### බිට්කොයින් ලබා ගැනීම

ඔබේ Wallet නිර්මාණය කිරීමෙන් පසු, ආරම්භකව ඔබට `0'` දර්ශකය සහිත තනි ගිණුමක් ඇතිවනු ඇත. මෙය අපි පෙර කොටස්වලදී කතා කළ **තැන්පතු** ගිණුමයි. මෙය මිශ්‍ර කිරීමට බිට්කොයින් යැවිය යුතු ගිණුමයි.


To do this, select the `Receive` tab on the left side of the window. Sparrow will automatically generate a new blank Address to receive bitcoins.


![sparrow](assets/notext/17.webp)


Address සඳහා ලේබලයක් ඇතුළත් කළ හැකි අතර, පසුව බිට්කොයින් එයට මිශ්‍ර කිරීමට යැවිය හැක.


![sparrow](assets/notext/18.webp)


### Tx0 සෑදීම

ඔබේ ගනුදෙනුව තහවුරු වූ පසු, ඔබට `UTXOs` ටැබය වෙත යා හැක.


![sparrow](assets/notext/19.webp)


ඊළඟට, ඔබ CoinJoin චක්‍ර සඳහා ඉදිරිපත් කිරීමට කැමති UTXO(ව) තෝරන්න. එකවර බහු UTXO තෝරා ගැනීමට, ඔබේ කැමති UTXO මත ක්ලික් කරන විට `Ctrl` යතුර ඔබාගෙන සිටින්න.


![sparrow](assets/notext/20.webp)


එවිට කවුළුවේ පහළින් ඇති `Mix Selected` බොත්තම මත ක්ලික් කරන්න. මෙම බොත්තම ඔබේ Interface මත පෙනෙන්නේ නැත්නම්, එය Hardware Wallet සමඟ ආරක්ෂා කරන ලද Wallet මත ඔබ සිටින බැවිනි. Sparrow සමඟ coinjoins කිරීමට ඔබට Software Wallet භාවිතා කළ යුතුය.

![sparrow](assets/notext/21.webp)

වින්ඩෝවක් විවෘත වේ Whirlpool කෙසේ ක්‍රියා කරන්නේද යන්න පැහැදිලි කිරීමට. මෙය මම පෙර කොටස්වල විස්තර කළ දේ සරල කිරීමකි. ඉදිරියට යාමට `Next` මත ක්ලික් කරන්න.


![sparrow](assets/notext/22.webp)


මීළඟ පිටුවේදී, ඔබට "SCODE" එකක් ඇතුළත් කළ හැකිය, ඔබට එකක් තිබේ නම්. SCODE යනු දියුණුවීම් කේතයකි, එය තටාකයේ සේවා ගාස්තු සඳහා වට්ටමක් ලබා දේ. Samourai Wallet විශේෂ අවස්ථාවලදී එම කේත ලබා දේ. මම ඔබට [Samourai Wallet අනුගමනය කරන්න](https://twitter.com/SamouraiWallet) සමාජ මාධ්‍ය ඔස්සේ යෝජනා කරමි, එවිට ඔබට අනාගත SCODES මග හැරෙන්නේ නැත.


එම පිටුවේ, ඔබට `Tx0` සඳහා ගාස්තු අනුපාතය සහ ඔබේ ආරම්භක මිශ්‍රණය සකසන්න අවශ්‍ය වේ. මෙම තේරීම ඔබේ සූදානම් ගනුදෙනුව සහ ඔබේ පළමු CoinJoin සඳහා තහවුරු කිරීමේ වේගය බලපානු ඇත. `Tx0` සහ ආරම්භක මිශ්‍රණය සඳහා Mining ගාස්තු සඳහා ඔබ වගකිව යුතු බව මතක තබා ගන්න, නමුත් පසුකාලීන නැවත මිශ්‍රණ සඳහා Mining ගාස්තු ඔබට ගෙවීමට අවශ්‍ය නොවේ. ඔබේ කැමැත්තන්ට අනුව `Premix Priority` සළකුණ සකසන්න, එවිට `Next` මත ක්ලික් කරන්න.


![sparrow](assets/notext/23.webp)


V tem novem oknu boste imeli možnost izbrati bazen, v katerega želite vstopiti, z uporabo spustnega seznama. V mojem primeru, ko sem sprva izbral UTXO iz `456 214 Sats`, je moja edina možna izbira bazen `100 000 Sats`. Ta Interface vas tudi obvešča o storitvenih stroških, ki jih je treba plačati, ter o številu UTXO-jev, ki bodo vključeni v bazen. Če se vam pogoji zdijo zadovoljivi, nadaljujte s klikom na `Predogled Premix`.


![sparrow](assets/notext/24.webp)


මෙම පියවරෙන් පසු, Sparrow ඔබගෙන් ඔබේ Wallet සඳහා මුරපදය ඇතුළත් කරන ලෙස ඉල්ලා සිටී, එය ඔබ මෘදුකාංගය මත නිර්මාණය කරන විට ස්ථාපිත කළ එකයි. මුරපදය ඇතුළත් කළ පසු, ඔබේ `Tx0` හි පෙරදසුනට ප්‍රවේශ විය හැක. ඔබේ කවුළුවේ වම් පැත්තේ, Sparrow විසින් Whirlpool භාවිතා කිරීමට අවශ්‍ය විවිධ ගිණුම් (`තැන්පතු`, `Premix`, `Postmix`, සහ `Badbank`) ජනනය කර ඇති බව ඔබට පෙනේ. ඔබට ඔබේ `Tx0` හි ව්‍යුහය, විවිධ ප්‍රතිදාන සමඟ දැකීමටද අවස්ථාව ලැබේ:


- සේවා ගාස්තු;
- සමීකෘත UTXOs දියත් කිරීමට අදහස් කර ඇත;
- විෂ සහිත වෙනස (Doxxic Change).


![sparrow](assets/notext/25.webp)


ඔබට ගනුදෙනුව කැමති නම්, ඔබේ `Tx0` විකාශනය කිරීමට `Broadcast Transaction` මත ක්ලික් කරන්න. නැතහොත්, ඇතුළත් කළ දත්ත මකා දමා නිර්මාණ ක්‍රියාවලිය ආරම්භයෙන් ආරම්භ කිරීමට `Clear` තෝරාගෙන මෙම `Tx0` හි පරාමිතීන් සකස් කිරීමේ විකල්පය ඔබට ඇත.


### කොයින්ජොයින්ස් කිරීම

Tx0 විකාශනය කළ විට, ඔබේ UTXOs `Premix` ගිණුම තුළ මිශ්‍ර කිරීමට සූදානම් වනු ඇත.

![sparrow](assets/notext/26.webp)


`Tx0` තහවුරු වූ විට, ඔබේ UTXO සමුහය සමන්විතකරු සමඟ ලියාපදිංචි වන අතර, ආරම්භක මිශ්‍රණ ස්වයංක්‍රීයව අනුපිළිවෙලින් ආරම්භ වේ.


![sparrow](assets/notext/27.webp)


`Postmix` ගිණුම පරීක්ෂා කිරීමෙන්, ඔබ මුල් මික්ස් වලින් ඇති වූ UTXOs නිරීක්ෂණය කරනු ඇත. මෙම කාසි පසුකාලීන නැවත මික්ස් කිරීම සඳහා සූදානම්ව පවතිනු ඇත, එමඟින් කිසිදු අමතර ගාස්තු අයකර නොමැත.


![sparrow](assets/notext/28.webp)


`Mixes` स्तम्भमा, तपाईंको प्रत्येक सिक्काले गरेको सिक्काको संख्या देख्न सम्भव छ। हामीले निम्न खण्डहरूमा देख्नेछौं, वास्तवमा महत्त्वपूर्ण कुरा पुनःमिश्रणहरूको संख्या मात्र होइन, तर सम्बन्धित अनोनसेटहरू हुन्, यद्यपि यी दुई सूचकहरू आंशिक रूपमा सम्बन्धित छन्।


![sparrow](assets/notext/29.webp)


සිකිලි මැදිහත්වීම් තාවකාලිකව නවතා දැමීමට, සරලව `Stop Mixing` මත ක්ලික් කරන්න. `Start Mixing` තේරීමෙන් ඔබට ඕනෑම වේලාවක මෙහෙයුම් නැවත ආරම්භ කිරීමට විකල්පය ලැබෙනු ඇත.


![sparrow](assets/notext/30.webp)


ඔබේ UTXOs නැවත මිශ්‍ර කිරීම සඳහා අඛණ්ඩව ලබා ගත හැකි බව සහතික කිරීම සඳහා, Sparrow මෘදුකාංගය ක්‍රියාත්මක තබා ගැනීම අවශ්‍ය වේ. මෘදුකාංගය වසා දැමීම හෝ ඔබේ පරිගණකය නිවා දැමීම coinjoins නවත්වනු ඇත. මෙම ගැටලුව වළක්වා ගැනීම සඳහා විසඳුමක් වන්නේ ඔබේ මෙහෙයුම් පද්ධතියේ සැකසුම් හරහා නිදන කාර්ය අක්‍රිය කිරීමයි. අමතරව, Sparrow ඔබේ පරිගණකය ස්වයංක්‍රීයව නිදන තත්ත්වයට යාම වළක්වා ගැනීම සඳහා විකල්පයක් ලබා දේ, එය ඔබට `Tools` ටැබය යටතේ ඇති `Prevent Computer Sleep` හි සොයා ගත හැක.


![sparrow](assets/notext/31.webp)


### සිකිලි සම්පූර්ණ කිරීම

ඔබේ මිශ්‍රිත බිට්කොයින් වියදම් කිරීමට, ඔබට විකල්ප කිහිපයක් ඇත. සෘජුම ක්‍රමය වන්නේ `Postmix` ගිණුමට ප්‍රවේශ වීම සහ `Send` ටැබය තෝරා ගැනීමයි.


![sparrow](assets/notext/32.webp)


මෙම කොටස තුළ, ඔබට ගමනාන්තය Address, යැවිය යුතු මුදල, සහ ගනුදෙනු ගාස්තු ඇතුළත් කිරීමට විකල්පය ඇත, Sparrow Wallet සමඟ කරන වෙනත් ගනුදෙනුවක් සඳහා මෙන්ම. ඔබට අවශ්‍ය නම්, `Privacy` බොත්තම ක්ලික් කිරීමෙන් Stonewall වැනි උසස් පෞද්ගලිකත්ව විශේෂාංග වලින්ද ප්‍රයෝජන ගත හැක.


![sparrow](assets/notext/33.webp)


[-> Stonewall ගනුදෙනු පිළිබඳව වැඩිදුරටත් ඉගෙන ගන්න.](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


ඔබගේ වියදම් කිරීමට නියමිත කාසි වඩාත් නිවැරදිව තෝරා ගැනීමට කැමති නම්, `UTXOs` ටැබය වෙත යන්න. ඔබට විශේෂයෙන්ම පරිභෝජනය කිරීමට අවශ්‍ය UTXOs තෝරන්න, එවිට ගනුදෙනුව ආරම්භ කිරීමට `Send Selected` බොත්තම ඔබන්න.


![sparrow](assets/notext/34.webp)

අවසන් වශයෙන්, Sparrow හි ලබා ගත හැකි `Mix to...` විකල්පය, අමතර ගාස්තු නොමැතිව, තෝරාගත් UTXO එකක් CoinJoin චක්‍රවලින් ස්වයංක්‍රීයව ඉවත් කිරීමට ඉඩ සලසයි. මෙම විශේෂාංගය, UTXO එකක් ඔබේ `Postmix` ගිණුමට නැවත එක් නොකරන, නමුත් වෙනත් Wallet කට සෘජුවම මාරු කරන, රිමික්ස් සංඛ්‍යාවක් තීරණය කිරීමට ඉඩ සලසයි. මෙම විකල්පය බොහෝ විට Cold Wallet කට මික්ස් කරන ලද බිට්කොයින් ස්වයංක්‍රීයව යැවීමට භාවිතා වේ.

මෙම විකල්පය භාවිතා කිරීමට, Sparrow මෘදුකාංගය තුළ ඔබේ CoinJoin Wallet සමඟ ලාභලාභ Wallet විවෘත කිරීමෙන් ආරම්භ කරන්න.


![sparrow](assets/notext/35.webp)


Potem pojdite na zavihek `UTXOs` in nato kliknite na gumb `Mix to...` na dnu okna.


![sparrow](assets/notext/36.webp)


වින්ඩෝවක් විවෘත වේ, ඩ්‍රොප්ඩවුන් ලැයිස්තුවෙන් ගමනාන්තය Wallet තෝරා ගැනීමෙන් ආරම්භ කරන්න.


![sparrow](assets/notext/37.webp)


Izberite prag CoinJoin, nad katerim bo dvig izveden samodejno. Ne morem vam dati natančnega števila remiksov, ki jih je treba izvesti, saj se to razlikuje glede na vašo osebno situacijo in cilje zasebnosti, vendar se izogibajte izbiri prenizkega praga. Priporočam, da si ogledate ta drugi članek, da izveste več o postopku remiksanja: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-Whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


ඔබට `Index range` විකල්පය එහි පෙරනිමි අගය `Full` මත තබා හැරිය හැක. මෙම කාර්යය විවිධ ගනුදෙනුකරුවන්ගෙන් එකවර මිශ්‍ර කිරීම සඳහා ඉඩ සලසයි, නමුත් එය අපි මෙම උපකාරක පාඩමෙන් කිරීමට අවශ්‍ය නොවේ. `Mix to...` විකල්පය අවසන් කර සක්‍රීය කිරීමට, `Restart Whirlpool` ඔබන්න.


![sparrow](assets/notext/38.webp)


කෙසේ වෙතත්, `Mix to` විකල්පය භාවිතා කිරීමේදී අවධානයෙන් සිටින්න, මක්නිසාද ඔබේ `Postmix` ගිණුමෙන් මිශ්‍ර කරන ලද කාසි ඉවත් කිරීමෙන් ඔබේ පෞද්ගලිකත්වය කඩකිරීමේ අවදානම සීඝ්‍රයෙන් වැඩි විය හැක. මෙම සම්භාවිතාව සඳහා හේතු පහත කොටස්වල විස්තර කර ඇත.


## CoinJoin චක්‍රවල අපගේ ගුණාත්මකභාවය කෙසේදැයි දැන ගැනීමට කෙසේද?

Za CoinJoin, da bi bil resnično učinkovit, je bistveno, da predstavlja dobro homogenost med količinami vhodov in izhodov. Ta enotnost povečuje število možnih interpretacij v očeh zunanjega opazovalca, s čimer se povečuje negotovost okoli transakcije. Za kvantificiranje te negotovosti, ki jo ustvari CoinJoin, se lahko zatečemo k izračunu entropije transakcije. Za poglobljeno raziskovanje teh kazalnikov vas napotujem na vadnico: [BOLTZMANN CALCULATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe). Model Whirlpool je priznan kot tisti, ki prinaša največjo homogenost v coinjoinih.

Nato se oceni učinkovitost več ciklov CoinJoin glede na velikost skupin, v katerih je skovan kovanec. Velikost teh skupin določa, kar imenujemo anonsets. Obstajata dve vrsti anonsets: prva ocenjuje pridobljeno zasebnost proti retrospektivni analizi (od sedanjosti do preteklosti) in druga proti prospektivni analizi (od preteklosti do sedanjosti). Za podrobno razlago teh dveh kazalnikov vas vabim, da si ogledate vadnico: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## पोस्टमिक्स को कसरी व्यवस्थापन गर्ने?

CoinJoin චක්‍ර පූර්ණ කිරීමෙන් පසු, ඔබේ UTXOs **postmix** ගිණුම තුළ තබා ගනිමින්, ඒවා භාවිතා කිරීමට ඔබට අවශ්‍ය වන තුරු රැඳී සිටීම හොඳම උපාය මාර්ගය වේ. ඒවා ඔබට වියදම් කිරීමට අවශ්‍ය වන තුරු අඛණ්ඩව නැවත මිශ්‍ර කිරීමට ඉඩ දීම පවා උපදේශනීය වේ.


සමහර පරිශීලකයින් තම මිශ්‍රිත බිට්කොයින් Hardware Wallet මඟින් ආරක්ෂිත Wallet වෙත මාරු කිරීම සලකා බලන්නට පුළුවන්. මෙය කළ හැකි නමුත් ලබා ගත් රහස්‍යතාවයට හානි නොවීමට Samourai Wallet හි නිර්දේශ නිවැරදිව අනුගමනය කිරීම වැදගත් වේ.


UTXOs එකතු කිරීම වඩාත්ම සාමාන්‍යයෙන් සිදුවන වැරදි වේ. CIOH (*Common-Input-Ownership-Heuristic*) වලක්වා ගැනීම සඳහා, එකම ගනුදෙනුවක මිශ්‍ර UTXOs නොමිශ්‍ර UTXOs සමඟ එකතු කිරීමෙන් වළකින්න. මෙය Wallet තුළ ඔබේ UTXOs කාර්යක්ෂමව කළමනාකරණය කිරීම, විශේෂයෙන් ලේබල් කිරීමේ අර්ථයෙන්, අවශ්‍ය වේ. CoinJoin ඉක්මවා, UTXOs එකතු කිරීම සාමාන්‍යයෙන් නරක පුරුද්දක් වන අතර, නිසි ලෙස කළමනාකරණය නොකළ විට පෞද්ගලිකත්වය අහිමි වීමට හේතු වේ.


Pomembno je biti previden pri konsolidaciji mešanih UTXO-jev med seboj. Zmerne konsolidacije so izvedljive, če imajo vaši mešani UTXO-ji pomembne anonsete, vendar bo to neizogibno zmanjšalo zaupnost vaših kovancev. Poskrbite, da konsolidacije ne bodo prevelike ali izvedene po nezadostnem številu remiksov, saj to tvega vzpostavitev deducibilnih povezav med vašimi UTXO-ji pred in po ciklih CoinJoin. V primeru dvoma o teh manipulacijah je najboljša praksa, da ne konsolidirate postmix UTXO-jev, temveč jih prenesete enega po enega na vaš Hardware Wallet, pri čemer vsakič ustvarite nov prazen Address. Ponovno se spomnite, da pravilno označite vsak prejeti UTXO.

Prav tako se odsvetuje prenos vaših postmix UTXO-jev na Wallet z uporabo neobičajnih skript. Na primer, če vstopite v Whirlpool iz Multisig Wallet z uporabo skript `P2WSH`, je malo verjetnosti, da boste pomešani z drugimi uporabniki, ki imajo enak tip Wallet prvotno. Če dvignete svoj postmix na ta isti Multisig Wallet, bo raven zasebnosti vaših mešanih bitcoinov močno zmanjšana. Poleg skript obstaja še veliko drugih prstnih odtisov Wallet, ki vas lahko zavedejo.

Bitcoin ගනුදෙනුවක් සමඟ මෙන්ම, ලැබීමේ ලිපින නැවත භාවිතා නොකිරීමද වැදගත් වේ. සෑම නව ගනුදෙනුවක්ම නව, හිස් Address මත ලැබිය යුතුය.


සරලම සහ ආරක්ෂිතම විසඳුම වන්නේ ඔබේ මිශ්‍ර UTXO-වලට ඔවුන්ගේ **postmix** ගිණුම තුළ විවේක ගැනීමට ඉඩ දීමයි, ඔවුන් නැවත මිශ්‍ර කිරීමට ඉඩ දීම සහ වියදම් කිරීමට පමණක් ඔවුන්ට ස්පර්ශ කිරීමයි. Samourai සහ Sparrow පසුම්බි මෙම සියලුම දාම විශ්ලේෂණ සම්බන්ධ අවදානම් වලට එරෙහිව අමතර ආරක්ෂණ ලබා දේ. මෙම ආරක්ෂණ ඔබට දෝෂ කිරීමට ඉවසා ගැනීමට උපකාරී වේ.


## Kako upravljati s toksičnimi spremembami?

ඊළඟට, ඔබ CoinJoin පොකුණට ඇතුල් විය නොහැකි doxxic වෙනස කළමනාකරණය කිරීමේදී අවධානයෙන් සිටිය යුතුය. Whirlpool භාවිතයෙන් ඇතිවන මෙම විෂ UTXO, ඔබේ පෞද්ගලිකත්වයට අවදානමක් ඇති කරයි, මන්ද ඒවා ඔබ හා CoinJoin භාවිතය අතර සබඳතාවයක් ස්ථාපිත කරයි. එබැවින්, ඒවා අවධානයෙන් කළමනාකරණය කිරීම හා විශේෂයෙන් මිශ්‍ර UTXO සමඟ ඒවා එකතු නොකිරීම අත්‍යවශ්‍ය වේ. ඒවා භාවිතා කිරීම සඳහා සලකා බැලිය හැකි විවිධ උපාය මාර්ග මෙන්න:


- ඔවුන් කුඩා තටාකවල මිශ්‍ර කරන්න:** ඔබේ විෂ සහිත UTXO එකක් පමණක් කුඩා තටාකයකට ඇතුළු වීමට ප්‍රමාණවත් නම්, එය මිශ්‍ර කිරීම සලකා බලන්න. මෙය බොහෝ විට හොඳම විකල්පය වේ. කෙසේ වෙතත්, තටාකයකට ප්‍රවේශ වීමට විෂ සහිත UTXO කිහිපයක් එකට එක් නොකරන ලෙස ඉතා වැදගත් වේ, මන්ද මෙය ඔබේ විවිධ ඇතුළත් කිරීම් සම්බන්ධ කළ හැක;
- ඔවුන් "නොවියදම් කළ හැකි" ලෙස සලකන්න: ** තවත් ආකාරයක් නම්, ඔවුන් භාවිතා නොකිරීම, ඔවුන්ගේ කැපවූ ගිණුමේ "නොවියදම් කළ හැකි" ලෙස සලකන්න, සහ සරලව HODL. මෙය ඔබට අහඹු ලෙස ඔවුන් වියදම් නොකරන බව සහතික කරයි. Bitcoin හි අගය වැඩි වුවහොත්, ඔබේ විෂ UTXO සඳහා වඩා සුදුසු නව තටාක හටගත හැක;
- Naredite donacije:** Razmislite o donacijah, tudi skromnih, razvijalcem, ki delajo na Bitcoin in povezanih programskih opremah. Lahko tudi donirate organizacijam, ki sprejemajo BTC. Če se vam zdi upravljanje vaših toksičnih UTXO-jev preveč zapleteno, se jih lahko preprosto znebite z donacijo;
- ගිෆ්ට් කාඩ් මිලදී ගන්න:** [Bitrefill](https://www.bitrefill.com/) වැනි වේදිකා ඔබට විවිධ වෙළෙන්දන් වෙත භාවිතා කළ හැකි ගිෆ්ට් කාඩ් සඳහා bitcoins Exchange කිරීමට ඉඩ සලසයි. මෙය ඔබේ විෂ සහිත UTXOs අහිමි නොවී සම්බන්ධ වටිනාකම නැතිවීමේ ක්‍රමයක් විය හැක.
- ඔවුන් Monero මත ඒකාබද්ධ කරන්න:** Samourai Wallet දැන් BTC සහ XMR අතර පරමාණුක හුවමාරු සේවාවක් ලබා දේ. මෙය විෂ සහිත UTXO මොනෙරෝ මත ඒකාබද්ධ කිරීම සඳහා ඉතා සුදුසු වේ, CIOH හරහා ඔබේ පෞද්ගලිකත්වය ආපසු Bitcoin වෙත යැවීමට පෙර අහිමි නොකර. කෙසේ වෙතත්, Mining ගාස්තු සහ ද්‍රවතා සීමාකිරීම් හේතුවෙන් අතිරේක මුදලක් ගෙවිය යුතු බැවින් මෙම විකල්පය වියදම් සහිත විය හැක.
- ඔවුන් Lightning Network වෙත යවන්න:** මෙම UTXO මාරු කිරීම Lightning Network වෙත, ගනුදෙනු ගාස්තු අඩු කිරීමේ වාසියක් ලබා ගැනීම සඳහා රසවත් විකල්පයක් විය හැක. කෙසේ වෙතත්, මෙම ක්‍රමය ඔබේ Lightning භාවිතය මත පදනම්ව විශේෂිත තොරතුරු අනාවරණය කළ හැකි බැවින්, අවධානයෙන් පුරුදු විය යුතුය.


මෙම විවිධ තාක්ෂණයන් ක්‍රියාත්මක කිරීම පිළිබඳ විස්තරාත්මක උපදෙස් PlanB ජාලය මත ඉක්මනින් ලබා දෙනු ඇත.


**අමතර සම්පත්:**

[Sparrow Wallet වීඩියෝ උපකාරකය](https://planb.network/tutorials/Wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

[Samourai Wallet වීඩියෝ උපකාරකය](https://planb.network/tutorials/Wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Documentation - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Twitter Thread on CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blog Post on CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).