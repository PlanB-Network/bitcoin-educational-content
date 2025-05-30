---
name: Blockstream Green - පරීක්ෂණය-සමග පමණක්
description: Watch-only wallet කාර්යය වින්‍යාසය
---
![cover](assets/cover.webp)


මෙම උපකාරිකාවේ, ඔබට Blockstream Green යෙදුම භාවිතා කරමින් ජංගම දුරකථනයේ "නිරීක්ෂණය පමණක්" Wallet එකක් පහසුවෙන් පිහිටුවන්නේ කෙසේද යන්න සොයා ගත හැකිය.


## Kaj je Watch-only wallet?


Wallet, ali "Watch-only wallet", samo za branje, je vrsta programske opreme, zasnovana za omogočanje uporabniku opazovanje transakcij, povezanih z enim ali več specifičnimi javnimi ključi Bitcoin, brez dostopa do ustreznih zasebnih ključev.


මෙම වර්ගයේ යෙදුම Bitcoin Wallet නිරීක්ෂණය කිරීමට අවශ්‍ය දත්ත පමණක් ගබඩා කරයි, විශේෂයෙන් එහි ශේෂය සහ ගනුදෙනු ඉතිහාසය බලන්න, නමුත් එයට පෞද්ගලික යතුරු වෙත ප්‍රවේශයක් නොමැත. ප්‍රතිඵලයක් ලෙස, නිරීක්ෂණය-පමණක් යෙදුම මගින් Wallet හි ඇති බිට්කොයින් වියදම් කිරීම අසම්භවය.


![GREEN-WATCH-ONLY](assets/fr/01.webp)


Watch-only običajno uporabljamo v povezavi z Hardware Wallet. To omogoča, da se zasebni ključi Wallet varno shranijo na strojno opremo, ki ni povezana z internetom in ima zelo majhno površino za napade, s čimer se zasebni ključi izolirajo od potencialno ranljivih okolij. Aplikacija watch-only pa izključno shranjuje razširjeni javni ključ (`xpub`, `zpub`, itd.) Bitcoin Wallet. Ta nadrejeni ključ se ne more uporabiti za iskanje povezanih zasebnih ključev in zato ne more biti uporabljen za porabo Bitcoinov. Omogoča pa izpeljavo otroških javnih ključev in prejemnih naslovov. Zahvaljujoč znanju Hardware Wallet o varnih naslovih Wallet lahko aplikacija watch-only sledi tem transakcijam na omrežju Bitcoin, kar uporabniku omogoča spremljanje njegovega stanja in generate novih prejemnih naslovov, ne da bi moral vsakič povezati svoj Hardware Wallet.


මෙම උපකාරිකාවේ, මම ඔබට ජනප්‍රියම නරඹන-පමණක් ජංගම Wallet විසඳුම්වලින් එකක් හඳුන්වා දීමට කැමතියි: **Blockstream Green**.


![GREEN-WATCH-ONLY](assets/fr/02.webp)


## Blockstream Green හඳුන්වා දීම


Blockstream Green යනු ජංගම සහ ඩෙස්ක්ටොප් සඳහා ලබා ගත හැකි මෘදුකාංග යෙදුමකි. පෙර Green Address ලෙස හැඳින්වූ මෙම Wallet, 2016 දී මිලදී ගැනීමෙන් පසු Blockstream ව්‍යාපෘතියක් විය.


Green යනු භාවිතා කිරීමට ඉතා පහසු යෙදුමක් වන අතර, එය විශේෂයෙන් ආරම්භකයින් සඳහා සුදුසු වේ. එය Hot වොලට්, දෘඩාංග වොලට් සහ Liquid Sidechain වොලට් කළමනාකරණය වැනි කාර්යයන්ගේ පරාසයක් ලබා දේ.


මෙම උපකාරිකාවේ, අපි Watch-only wallet එකක් නිර්මාණය කිරීම පිළිබඳ පමණක් අවධානය යොමු කරමු. Green හි වෙනත් භාවිතා පිළිබඳ විමසා බැලීමට, කරුණාකර අපගේ අනෙකුත් කැපවූ උපකාරිකා බලන්න:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

## Blockstream Green යෙදුම ස්ථාපනය කිරීම සහ වින්‍යාස කිරීම


පළමු පියවර වන්නේ Green යෙදුම බාගත කිරීමයි. ඔබේ යෙදුම් ගබඩාවට යන්න:



- [Android සඳහා](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN-WATCH-ONLY](assets/fr/03.webp)


Android පරිශීලකයින් සඳහා, ඔබට Blockstream හි GitHub හි [ලබා ගත හැකි](https://github.com/Blockstream/green_android/releases) `.apk` ගොනුව හරහා යෙදුම ස්ථාපනය කළ හැක.


![GREEN-WATCH-ONLY](assets/fr/04.webp)


ප්‍රයෝගය ආරම්භ කර, "මම කොන්දේසි පිළිගන්නවා...*" කොටුව පරීක්ෂා කරන්න.


![GREEN-WATCH-ONLY](assets/fr/05.webp)


ඔබ Green පළමු වරට විවෘත කරන විට, මුල් තිරය Wallet එකක් වින්‍යාස නොකළව පෙනේ. පසුව, ඔබ පසුබැසීමක් හෝ ආයාත කිරීමක් කළහොත්, ඒවා මෙම Interface තුළ පෙනේ. Wallet එකක් නිර්මාණය කිරීමට පෙර, මම ඔබට යෙදුම් සැකසුම් ඔබේ අවශ්‍යතා සඳහා සකසන්නැයි උපදෙස් දෙමි. "යෙදුම් සැකසුම්" මත ක්ලික් කරන්න.


![GREEN-WATCH-ONLY](assets/fr/06.webp)


"*වර්ධිත පෞද්ගලිකත්වය*" විකල්පය, Android මත පමණක් ලබා ගත හැකි, තිර රූප අක්‍රිය කිරීම සහ යෙදුම් පෙරදසුන් සඟවා පෞද්ගලිකත්වය වර්ධනය කරයි. එය ඔබේ දුරකථනය අගුළු දැමූ විටම යෙදුම් ප්‍රවේශය ස්වයංක්‍රීයව අගුළු දැමීමෙන්, ඔබේ දත්ත අනාවරණය වීම වඩාත් දුෂ්කර කරයි.


![GREEN-WATCH-ONLY](assets/fr/07.webp)


ඔබගේ පෞද්ගලිකත්වය වැඩිදියුණු කිරීමට කැමති අය සඳහා, යෙදුම ඔබේ ගමනාගමනය Tor හරහා rooting කිරීමේ විකල්පය ලබා දේ, එය ඔබේ සම්බන්ධතා සියල්ල සංකේතනය කර ඔබේ ක්‍රියාකාරකම් හඹා යාම අපහසු කරයි. මෙම විකල්පය යෙදුමේ මෙහෙයුම ටිකක් මන්දගාමී කළ හැකි වුවද, ඔබේම සම්පූර්ණ නියමුවා භාවිතා නොකරන්නේ නම්, ඔබේ පෞද්ගලිකත්වය ආරක්ෂා කිරීම සඳහා ඉතා නිර්දේශිත වේ.


![GREEN-WATCH-ONLY](assets/fr/08.webp)


Green Wallet uporabnikom, ki imajo svoj popoln vozlišče, ponuja možnost povezave z njim prek strežnika Electrum, kar zagotavlja popoln nadzor nad informacijami omrežja Bitcoin in distribucijo transakcij.


![GREEN-WATCH-ONLY](assets/fr/09.webp)


තවත් විකල්ප විශේෂාංගයක් "*SPV Verification*" විකල්පය වන අතර, එය ඔබට Blockchain දත්ත සෘජුවම සත්‍යාපනය කිරීමට ඉඩ සලසන අතර, එමඟින් Blockstream හි පෙරනිමි නියුඩය විශ්වාස කිරීමට ඇති අවශ්‍යතාව අඩු කරයි, එහෙත් මෙම ක්‍රමය Full node හි සියලුම සහතික ලබා නොදෙයි.


![GREEN-WATCH-ONLY](assets/fr/10.webp)


ඔබගේ අවශ්‍යතා සඳහා මෙම සැකසුම් සකසා අවසන් වූ විට, "*සුරකින්න*" බොත්තම ක්ලික් කර යෙදුම නැවත ආරම්භ කරන්න.


![GREEN-WATCH-ONLY](assets/fr/11.webp)


## Watch-only wallet Blockstream Green මත සාදන්න


ඔබ දැන් Watch-only wallet එකක් සාදන්න සූදානම්. "*Get Started*" බොත්තම ක්ලික් කරන්න.


![GREEN-WATCH-ONLY](assets/fr/12.webp)


ඔබට Wallet වර්ග කිහිපයක් අතරින් තෝරා ගත හැකි වේ. මෙම උපකාරිකාව සඳහා, අපි Watch-only wallet එකක් නිර්මාණය කිරීමට අවශ්‍ය වන අතර, ඒ සඳහා අදාළ බොත්තම ක්ලික් කරන්න.


![GREEN-WATCH-ONLY](assets/fr/13.webp)


"එකල සත්‍යකාරකය" විකල්පය තෝරන්න.


![GREEN-WATCH-ONLY](assets/fr/14.webp)


පසුව "*Bitcoin*" තෝරන්න. මගේ කොටස සඳහා, මම මෙම උපකාරකය Testnet Wallet මත කරමින් සිටින නමුත් ක්‍රියාවලිය Mainnet මත සමාන වේ.


![GREEN-WATCH-ONLY](assets/fr/15.webp)


ඔබට විශාලිත මහජන යතුරක් (`xpub`, `zpub`, ආදිය) හෝ ප්‍රතිදාන ස්ක්‍රිප්ට් විස්තරකාරකය ලබා දීමට අයදුම් කරනු ඇත.


![GREEN-WATCH-ONLY](assets/fr/16.webp)


අදාළ Wallet වෙතින් ඔබට මෙය ලබා ගැනීමට අවශ්‍ය වනු ඇත, ඔබේ Watch-only wallet හරහා ඔබට මෙය හඹා යාමට අවශ්‍ය වේ. දිගු සජාතීය යතුර ආරක්ෂාව සම්බන්ධයෙන් සංවේදී නොවේ, එය පෞද්ගලික යතුරු වෙත ප්‍රවේශය ලබා නොදෙන බැවින්, නමුත් එය ඔබේ රහස්‍යතාවය සඳහා සංවේදී වේ, එය ඔබේ සියලුම සජාතීය යතුරු හෙළි කරන බැවින්, එමඟින් ඔබේ සියලුම Bitcoin ගනුදෙනු හෙළි වේ.


Recimo, da uporabljate Sparrow Wallet za upravljanje vašega Wallet na Hardware Wallet, boste te informacije našli v razdelku "*Nastavitve*". Iskanje teh informacij bo odvisno od programske opreme za upravljanje Wallet, ki jo uporabljate, vendar je običajno v nastavitvah.


![GREEN-WATCH-ONLY](assets/fr/17.webp)


ඔබේ දිගු මහජන යතුර පිටපත් කර Green යෙදුමට ඇතුළත් කර "Connect" මත ක්ලික් කරන්න.


![GREEN-WATCH-ONLY](assets/fr/18.webp)


ඔබට එවිට මෙම යතුර සමඟ සම්බන්ධිත ශේෂය සහ ගනුදෙනු ඉතිහාසය දැකිය හැකි වේ.


![GREEN-WATCH-ONLY](assets/fr/19.webp)


"*Receive*" මත ක්ලික් කිරීමෙන්, ඔබට generate ලබා ගැනීමක් Address ලබා ගැනීමට Hardware Wallet මත බිට්කොයින් ලබා ගැනීමට හැකියාව ඇත. කෙසේ වෙතත්, බිට්කොයින් අගුළු දැමීමට පෙර, ජනනය කරන ලද Address සමඟ සම්බන්ධිත පෞද්ගලික යතුර Hardware Wallet තිරය මත පළමුව පරීක්ෂා නොකළහොත් මෙම විකල්පය භාවිතා කිරීමෙන් වළකින්නැයි මම උපදෙස් දෙමි. මෙය අනුගමනය කළ යුතු හොඳ පුරුද්දකි.


![GREEN-WATCH-ONLY](assets/fr/20.webp)


"*Balayer*" විකල්පය ඔබට Green යෙදුමෙන් මුදල් වියදම් කිරීමට පෞද්ගලික යතුරක් අතින් ඇතුළත් කිරීමට ඉඩ සලසයි. ඉතා විශේෂිත අවස්ථාවල හැර, මෙම කාර්යය භාවිතා කිරීම මම නිර්දේශ නොකරමි, මන්දයත් එය ඔබේ පෞද්ගලික යතුර දුරකථනයක හෙළි කිරීමට ඔබව බල කරයි, එය ඔබේ Hardware Wallet ට වඩා පරිගණක ප්‍රහාර වලට ඉතාමත් අසුරේන වේ.


![GREEN-WATCH-ONLY](assets/fr/21.webp)


Zdaj veste, kako enostavno nastaviti Watch-only wallet na svojem pametnem telefonu! To je priročno orodje za spremljanje Wallet na Hardware Wallet, ne da bi ga morali vsakič povezati in odkleniti.


ඔබට මෙම උපකාරිකාව ප්‍රයෝජනවත් වූවා නම්, පහත Green අඟුලක් තැබීමට මම කෘතඥ වෙමි. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තූතියි!


මම ඔබට Hot Wallet සකසන Blockstream Green යෙදුම පිළිබඳව මෙම වෙනත් සම්පූර්ණ උපකාරකයද පරීක්ෂා කරන ලෙසද නිර්දේශ කරමි:


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143