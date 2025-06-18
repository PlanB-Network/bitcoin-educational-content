---
name: Blockstream Green - Liquid
description: Liquid Network Sidechain මත Wallet සකසමින්
---
![cover](assets/cover.webp)


Bitcoin ප්‍රොටෝකෝලය හිතාමතාම තාක්ෂණික සීමා ඇති කර ඇති අතර එය ජාලයේ විකේන්ද්‍රණය පවත්වා ගැනීමට සහ ආරක්ෂාව සියලුම පරිශීලකයින් අතර බෙදා හැරීමට උපකාරී වේ. කෙසේ වෙතත්, මෙම සීමා සමහර විට පරිශීලකයින්ට අපහසුතාවයක් විය හැකි අතර, විශේෂයෙන්ම එකවර ගනුදෙනු විශාල ප්‍රමාණයක් නිසා තදබදය ඇති විට. Bitcoin හි විශාලත්වය පිළිබඳ වාදය දිගු කාලයක් තිස්සේ ප්‍රජාව බෙදමින් පවතින අතර, විශේෂයෙන්ම Blocksize යුද්ධය අතරතුර. මෙම සිදුවීමෙන් පසු, Bitcoin ප්‍රජාව තුළ විශාලත්වය off-chain විසඳුම් මගින් සහ Layer දෙවන පද්ධති මත සහතික කළ යුතු බව පුළුල් වශයෙන් පිළිගැනේ. මෙම විසඳුම් අතර sidechains ඇතුළත් වන අතර, Lightning Network වැනි අනෙකුත් පද්ධති සමඟ සැසඳීමේදී තවමත් ස نسبිතව අසමත් සහ අඩු ලෙස භාවිතා වේ.


Sidechain යනු ප්‍රධාන Bitcoin Blockchain සමඟ සමන්තරව ක්‍රියාත්මක වන ස්වාධීන Blockchain එකකි. එය "*two-way peg*" නම් යාන්ත්‍රණයක් හේතුවෙන් Bitcoin එකක් ලෙස ගිණුම් ඒකකයක් භාවිතා කරයි. මෙම පද්ධතිය මූලික ශෘංඛලයේ බිට්කොයින් අගය ප්‍රතිනිර්මාණය කිරීම සඳහා Sidechain මත අගය ප්‍රතිනිර්මාණය කිරීම සඳහා බිට්කොයින් අගය අගුළු දැමීමේ හැකියාව සලසයි, එහිදී ඔවුන් මුල් බිට්කොයින් වලින් ආධාරිත ටෝකන ලෙස සංසරණය වේ. මෙම ටෝකන සාමාන්‍යයෙන් මූලික ශෘංඛලයේ අගුළු දැමූ බිට්කොයින් සමඟ අගය සමානතාවය පවත්වාගෙන යයි, සහ Bitcoin මත අරමුදල් ප්‍රතිසාධනය කිරීම සඳහා ක්‍රියාවලිය ප්‍රතිවර්තනය කළ හැකිය.


සයිඩ්චේන්වල අරමුණ වන්නේ වේගවත් ගනුදෙනු, අඩු ගාස්තු හෝ ස්මාර්ට් කොන්ත්‍රාත් සඳහා සහය වැනි අමතර ක්‍රියාකාරකම් හෝ තාක්ෂණික වැඩිදියුණු කිරීම් ලබා දීමයි. මෙම නව්‍යතා සෘජුවම Bitcoin Blockchain මත ක්‍රියාත්මක කළ නොහැකි වන අතර එය විකේන්ද්‍රීකරණය හෝ ආරක්ෂාව අඩු නොකරයි. එබැවින්, සයිඩ්චේන්වලින් Bitcoin හි අඛණ්ඩතාවය සුරක්ෂිත කරමින් නව විසඳුම් පරීක්ෂා කිරීම සහ විමසා බැලීම සම්භවය. කෙසේ වෙතත්, මෙම ප්‍රොටෝකෝලයන්ට බොහෝ විට විශේෂයෙන්ම විකේන්ද්‍රීකරණය සහ ආරක්ෂාව සම්බන්ධයෙන්, තෝරාගත් ආණ්ඩුකරණ ආකෘතිය සහ එකඟතා ක්‍රමය අනුව, සමාවීම් අවශ්‍ය වේ.


අද, හොඳින් හැඳින්වෙන Sidechain වන්නේ Liquid විය හැක. මෙම උපකාරිකාවේ, මම පළමුව ඔබට Liquid කුමක්ද කියා කියන්නෙමි, එවිට Blockstream Green යෙදුම සමඟ පහසුවෙන් භාවිතා කිරීම ආරම්භ කිරීමට ඔබට මග පෙන්වන්නෙමි, එවිට ඔබට එහි සියලුම වාසි භුක්ති විඳිය හැක.


![LIQUID GREEN](assets/fr/01.webp)


## Kaj je Liquid Network?


Liquid යනු Bitcoin සඳහා Sidechain අධිස්ථරයක් වන සම්මේලිත Sidechain එකක් වන අතර, ගනුදෙනු වේගය, රහස්‍යභාවය සහ කාර්ය සාධනය වැඩි දියුණු කිරීම සඳහා Blockstream විසින් සංවර්ධනය කරන ලදී. එය ප්‍රධාන දාමයේ බිට්කොයින් අගුළු දැමීමට සහ ප්‍රතිඵලයක් ලෙස Liquid බිට්කොයින් (L-BTC) නිර්මාණය කිරීමට සම්මේලනයක් මත ස්ථාපිත ද්විපාර්ශවික සම්මත කිරීමේ ක්‍රමයක් භාවිතා කරයි, මුල් බිට්කොයින් මගින් ආධාරිතව සිටියදී Liquid මත පරිසරය වන ටෝකන.


![LIQUID GREEN](assets/fr/02.webp)


Liquid Network Bitcoin පරිසර පද්ධතියෙන් පිළිගත් අංශ වලින් සමන්විත සහභාගීකාරකයන්ගේ සංගමයකට රඳා පවතී, ඔවුන් කොටස් වල සත්‍යාපනය සහ ද්විපාර්ශ්වික සම්බන්ධතා කළමනාකරණය කරයි. L-BTC ට අමතරව, Liquid ස්ථාවර නානය සහ අනෙකුත් ක්‍රිප්ටෝමුද‍්‍රා වැනි අනෙකුත් ඩිජිටල් වත්කම් නිකුත් කිරීම ද සක්‍රීය කරයි.


![LIQUID GREEN](assets/fr/03.webp)


## Blockstream Green හඳුන්වා දීම


Blockstream Green je Software Wallet, ki je na voljo na mobilnih napravah in namizju. Prej znan kot *Green Address*, je ta Wallet postal projekt Blockstream po njegovem prevzemu leta 2016.


Green යනු ආරම්භකයින් සඳහා ආකර්ෂණීය වන විශේෂයෙන් භාවිතා කිරීමට පහසු යෙදුමකි. එය හොඳ Bitcoin Wallet හි සියලුම මූලික විශේෂාංග ලබා දේ, RBF (*Replace-by-fee*) ඇතුළුව, Tor සම්බන්ධතාවය විකල්පයක්, ඔබේම නියැදිය සම්බන්ධ කිරීමට හැකියාව, SPV (*Simple Payment Verification*), නාන ටැග් කිරීම සහ පාලනය.


Blockstream Green podpira tudi Liquid Network, in to bomo raziskali v tej vadnici. Če želite uporabiti Green za druge aplikacije, vam priporočam, da si ogledate tudi te druge vadnice:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Blockstream Green යෙදුම ස්ථාපනය කිරීම සහ වින්‍යාස කිරීම


පළමු පියවර වන්නේ Green යෙදුම බාගත කිරීමයි. ඔබේ යෙදුම් ගබඩාවට යන්න:



- [Android සඳහා](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![LIQUID GREEN](assets/fr/04.webp)


Android පරිශීලකයින් සඳහා, ඔබට Blockstream හි GitHub හි [ලබා ගත හැකි](https://github.com/Blockstream/green_android/releases) `.apk` ගොනුව හරහා යෙදුම ස්ථාපනය කළ හැක.


![LIQUID GREEN](assets/fr/05.webp)


ප්‍රයෝගය ආරම්භ කරන්න, එවිට "මම කොන්දේසි පිළිගන්නවා...*" කොටුව පරීක්ෂා කරන්න.


![LIQUID GREEN](assets/fr/06.webp)


Ko prvič odprete Green, se domači zaslon prikaže brez konfiguriranega Wallet. Kasneje, če ustvarite ali uvozite denarnice, se bodo pojavile v tem Interface. Preden nadaljujete z ustvarjanjem Wallet, priporočam, da prilagodite nastavitve aplikacije svojim potrebam. Kliknite na "Nastavitve aplikacije".


![LIQUID GREEN](assets/fr/07.webp)


"*වර්ධිත පෞද්ගලිකත්වය*" විකල්පය, Android මත පමණක් ලබා ගත හැකි, තිර රූප අක්‍රිය කිරීම සහ යෙදුම් පෙරදසුන් සඟවා පෞද්ගලිකත්වය වර්ධනය කරයි. එය ඔබේ දුරකථනය අගුළු දැමූ විටම යෙදුම් ප්‍රවේශය ස්වයංක්‍රීයව අගුළු දමන අතර, ඔබේ දත්ත අනාවරණය වීම වඩා දුෂ්කර කරයි.


![LIQUID GREEN](assets/fr/08.webp)


ඔබේ පෞද්ගලිකත්වය වැඩිදියුණු කිරීමට කැමති අය සඳහා, යෙදුම ඔබේ ගමනාගමනය Tor හරහා rooting කිරීමේ විකල්පය ලබා දේ, එය ඔබේ සම්බන්ධතා සියල්ල සංකේතනය කර ඔබේ ක්‍රියාකාරකම් හඹා යාම අපහසු කරයි. මෙම විකල්පය යෙදුමේ මෙහෙයුම ටිකක් මන්දගාමී කළ හැකි නමුත්, ඔබේම සම්පූර්ණ නියමුවා භාවිතා නොකරන්නේ නම්, ඔබේ පෞද්ගලිකත්වය ආරක්ෂා කිරීම සඳහා ඉතා නිර්දේශිත වේ.


![LIQUID GREEN](assets/fr/09.webp)


Green Wallet හිමිකරුවන්ට තමන්ගේම සම්පූර්ණ නෝඩයක් ඇති පරිශීලකයින් සඳහා, එලෙක්ට්රම් සේවාදායකය හරහා එයට සම්බන්ධ වීමේ විකල්පය ලබා දේ, Bitcoin ජාල තොරතුරු සහ ගනුදෙනු ප්‍රචාරණය පිළිබඳ සම්පූර්ණ පාලනය සහතික කරමින්. නමුත් මෙම විශේෂාංගය සම්භාව්‍ය Bitcoin පසුම්බි සඳහා වන අතර, ඔබ Liquid භාවිතා කරන්නේ නම් ඔබට එය අවශ්‍ය නොවේ.


![LIQUID GREEN](assets/fr/10.webp)


තවත් විකල්ප විශේෂාංගයක් "*SPV Verification*" විකල්පය වන අතර, එය ඔබට Blockstream හි පෙරනිමි නියුඩය විශ්වාස කිරීමට අවශ්‍යතාවය අඩු කරමින්, සෘජුවම Blockchain දත්ත සත්‍යාපනය කිරීමට ඉඩ සලසයි, එහෙත් මෙම ක්‍රමය Full node හි සියලුම සහතික ලබා නොදේ. නැවතත්, මෙය ඔබගේ onchain Bitcoin පසුම්බි වලට පමණක් බලපාන අතර, Liquid සඳහා නොවේ.


![LIQUID GREEN](assets/fr/11.webp)


Ko te nastavitve prilagodite svojim potrebam, kliknite gumb "*Shrani*" in znova zaženite aplikacijo.


![LIQUID GREEN](assets/fr/12.webp)


## Ustvarite Liquid Wallet na Blockstream Green


ඔබ දැන් Liquid Wallet එකක් නිර්මාණය කිරීමට සූදානම්. "*Get Started*" බොත්තම ක්ලික් කරන්න.


![LIQUID GREEN](assets/fr/13.webp)


ඔබට ස්ථානීය Software Wallet එකක් නිර්මාණය කිරීම හෝ Hardware Wallet හරහා Cold Wallet එකක් කළමනාකරණය කිරීම අතරින් තේරිය හැක. මෙම උපකාරිකාව සඳහා, අපි Liquid මත Hot Wallet එකක් නිර්මාණය කිරීම මත අවධානය යොමු කරමු, එබැවින් ඔබ "*මෙම උපාංගය මත*" විකල්පය තෝරන්න. ඔබට Liquid Wallet එක ආරක්ෂා කිරීම සඳහා Blockstream Jade වැනි අනුකූල Hardware Wallet එකක් ද භාවිතා කළ හැක.


![LIQUID GREEN](assets/fr/14.webp)


ඔබට පසුව පවතින Bitcoin Wallet එකක් ප්‍රතිස්ථාපනය කිරීමට හෝ නව එකක් නිර්මාණය කිරීමට තෝරා ගත හැක. මෙම උපකාරිකාව සඳහා, අපි නව Wallet එකක් නිර්මාණය කරමු. කෙසේ වෙතත්, ඔබට පවතින Liquid Wallet එකක් එහි Mnemonic වාක්‍යයෙන් නැවත ජනනය කිරීමට අවශ්‍ය නම්, උදාහරණයක් ලෙස ඔබේ Hardware Wallet අහිමි වීමෙන් පසු, ඔබට දෙවන විකල්පය තෝරා ගත යුතුය.


![LIQUID GREEN](assets/fr/15.webp)


Nato lahko izberete med 12-besedno ali 24-besedno frazo Mnemonic. Ta fraza vam bo omogočila obnovitev dostopa do vašega Wallet iz katere koli združljive programske opreme v primeru težave z vašim telefonom. Trenutno izbira 24-besedne fraze ne ponuja večje varnosti kot 12-besedna fraza. Zato vam priporočam, da izberete 12-besedno frazo Mnemonic.


Green ඔබට ඔබේ Mnemonic වාක්‍යය ලබා දෙනු ඇත. ඉදිරියට යාමට පෙර, ඔබව නිරීක්ෂණය කරමින් නොමැති බව සහතික වන්න. එය තිරය මත පෙන්වීමට "*ප්‍රතිසාධන වාක්‍යය පෙන්වන්න*" ක්ලික් කරන්න.


![LIQUID GREEN](assets/fr/16.webp)


**මෙම Mnemonic ඔබට ඔබේ සියලුම බිට්කොයින් සඳහා සම්පූර්ණ, අනිවාර්ය නොවන ප්‍රවේශය ලබා දේ ** මෙම Mnemonic හිමිකරුවෙකුට, ඔබේ දුරකථනයට භෞතික ප්‍රවේශය නොමැතිව පවා, ඔබේ මුදල් සොරාගත හැක.


එය ඔබේ දුරකථනය අහිමිවීම, සොරකම හෝ කැඩීමේ අවස්ථාවකදී ඔබේ බිට්කොයින් ප්‍රවේශය නැවත ලබා දේ. එබැවින් එය **භෞතික මාධ්‍යයක (ඩිජිටල් නොව)** සූක්ෂමව ආපසු ගබඩා කිරීම ඉතා වැදගත් වේ සහ ආරක්ෂිත ස්ථානයක ගබඩා කිරීම. ඔබට එය කඩදාසියක ලිවිය හැක, හෝ අමතර ආරක්ෂාව සඳහා, මෙය විශාල Wallet නම්, මම එය ගිනි, ගංවතුර හෝ කඩා වැටීමේ අවදානමෙන් ආරක්ෂා කිරීම සඳහා මල නොබැඳෙන වානේ සහායකයකට කැටයම් කිරීම නිර්දේශ කරමි (සීමිත ප්‍රමාණයක් බිට්කොයින් ආරක්ෂා කිරීමට නිර්මාණය කරන ලද Hot Wallet සඳහා, සරල කඩදාසි ආපසු ගබඩා කිරීම ප්‍රමාණවත් විය හැක).


*නිසැකවම, ඔබ මෙම වචන අන්තර්ජාලයේ බෙදා හදා නොකළ යුතුය, මම මෙම උපකාරිකාවේ කරන පරිදි. මෙම සාම්පල Wallet භාවිතා කරන්නේ Liquid හි Testnet සඳහා පමණක් වන අතර උපකාරිකාව අවසානයේදී මකා දමනු ඇත.*


![LIQUID GREEN](assets/fr/17.webp)


ඔබේ Mnemonic වාක්‍යය භෞතික මාධ්‍යයක නිවැරදිව සටහන් කර අවසන් වූ විට, "*Continue*" මත ක්ලික් කරන්න. Green Wallet පසුව ඔබට Mnemonic වාක්‍යයේ වචන කිහිපයක් තහවුරු කරන ලෙස අයදුම් කරනු ඇත, ඔබ ඒවා නිවැරදිව සටහන් කර ඇති බවට විශ්වාස කිරීම සඳහා. අස්ථානවල හිස්තැන් පුරවන්න.


![LIQUID GREEN](assets/fr/18.webp)


ඔබේ උපාංගයේ PIN කේතය තෝරන්න, එය ඔබේ Green Wallet අගුළු හරින සඳහා භාවිතා කෙරේ. මෙය අනුමත නොකළ භෞතික ප්‍රවේශයට එරෙහිව ඔබේ ආරක්ෂාවයි. මෙම PIN කේතය ඔබේ Wallet හි සංකේතාත්මක යතුරු නිර්ණය කිරීමේදී සම්බන්ධ නොවේ. එබැවින්, මෙම PIN කේතයට ප්‍රවේශය නොමැතිව, ඔබේ 12- හෝ 24-වචන Mnemonic වාක්‍යය හිමිකර ගැනීමෙන් ඔබට ඔබේ බිට්කොයින් නැවත ප්‍රවේශ විය හැක.


අපි ככל האפשר אקראי 6-ספרתי PIN קוד לבחור ממליצים. הקפד לשמור את הקוד הזה כדי שלא תשכח אותו, אחרת תיאלץ לאחזר את ה-Wallet מה-Mnemonic. לאחר מכן תוכל להוסיף אפשרות חסימה ביומטרית כדי להימנע מהצורך להזין את ה-PIN בכל פעם שאתה משתמש בו. באופן כללי, ביומטריה פחות בטוחה בהרבה מה-PIN עצמו. לכן, כברירת מחדל, אני ממליץ לך לא להגדיר אפשרות נעילה זו.


![LIQUID GREEN](assets/fr/19.webp)


ඔබේ PIN කේතය තහවුරු කිරීමට එය දෙවන වරක් ඇතුළත් කරන්න.


![LIQUID GREEN](assets/fr/20.webp)


ඔබේ Wallet නිර්මාණය වන තුරු රැඳී සිටින්න, එවිට "*ගිණුමක් සාදන්න*" බොත්තම ක්ලික් කරන්න.


![LIQUID GREEN](assets/fr/21.webp)


"*Active*" බොක්ස් එකේ, "*Liquid Bitcoin*" තෝරන්න. එවිට ඔබට මෙම උපකාරිකාවේ අපි භාවිතා කරන සම්මත තනි අත්සන Wallet හෝ දෙකේ-ගුණක සත්‍යාපනය (2FA) මඟින් ආරක්ෂිත Wallet අතර තෝරා ගත හැක.


![LIQUID GREEN](assets/fr/22.webp)


ඒකයි, ඔබේ Liquid Wallet, Green යෙදුම භාවිතයෙන් නිර්මාණය කර ඇත!


![LIQUID GREEN](assets/fr/23.webp)


ඔබගේ පළමු බිට්කොයින් ඔබගේ Liquid Wallet මත ලැබීමට පෙර, **මම ඔබට හිස් ප්‍රතිසාධන පරීක්ෂණයක් සිදු කිරීමට දැඩිව උපදෙස් දෙමි**. ඔබගේ xpub හෝ පළමු ලැබීමේ Address වැනි යම් සංකේත තොරතුරු සටහන් කර ගන්න, එවිට ඔබගේ Wallet Green යෙදුම මත තවමත් හිස්ව ඇති අතර මකන්න. එවිට ඔබේ Wallet Green මත ඔබේ කඩදාසි උපස්ථ භාවිතයෙන් ප්‍රතිසාධනය කිරීමට උත්සාහ කරන්න. ප්‍රතිසාධනයෙන් පසු ජනනය කරන ලද කුකී තොරතුරු ඔබ මුලින්ම සටහන් කර ගත් එකට ගැලපේදැයි පරීක්ෂා කරන්න. එසේ නම්, ඔබේ කඩදාසි උපස්ථ විශ්වාසදායක බවට ඔබට විශ්වාස කළ හැකිය. ප්‍රතිසාධන පරීක්ෂණයක් සිදු කරන ආකාරය පිළිබඳව වැඩිදුරටත් දැන ගැනීමට, කරුණාකර මෙම වෙනත් උපකාරකය අනුගමනය කරන්න:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## ඔබේ Liquid Wallet පිහිටුවීම


Če želite prilagoditi svoj Wallet, kliknite na tri majhne pike v zgornjem desnem kotu.


![LIQUID GREEN](assets/fr/24.webp)


"*Rename*" විකල්පය ඔබේ Wallet හි නම අභිරුචිකරණය කිරීමට ඉඩ සලසයි, එය විශේෂයෙන්ම ප්‍රයෝජනවත් වේ ඔබ එකම යෙදුම මත වාණිජිකා කිහිපයක් කළමනාකරණය කරන විට.


![LIQUID GREEN](assets/fr/25.webp)


"*Unit*" මෙනුව ඔබට ඔබේ Wallet හි මූලික ඒකකය වෙනස් කිරීමට ඉඩ සලසයි. උදාහරණයක් ලෙස, ඔබට එය බිට්කොයින් වෙනුවට සතෝෂි ලෙස පෙන්වීමට තෝරා ගත හැක.


![LIQUID GREEN](assets/fr/26.webp)


"*සැකසුම්*" මෙනුව ඔබේ Bitcoin Wallet හි විවිධ විකල්ප වෙත ප්‍රවේශය ලබා දේ.


![LIQUID GREEN](assets/fr/27.webp)


මෙහි, උදාහරණයක් ලෙස, ඔබේ *විස්තරකරු* සොයා ගත හැකි අතර, ඔබ Liquid Wallet සිට Watch-only wallet එකක් පිහිටුවීමට සැලසුම් කරන්නේ නම් එය ප්‍රයෝජනවත් විය හැක.


![LIQUID GREEN](assets/fr/28.webp)


Wallet PIN එක වෙනස් කිරීම සහ ජෛවමාන සම්බන්ධතාවයක් සක්‍රීය කිරීම ද කළ හැක.


![LIQUID GREEN](assets/fr/29.webp)


## Uporaba vašega Liquid Wallet


Zdaj, ko je vaš Liquid Wallet nastavljen, ste pripravljeni na prejem prvega L-Sats!


ඔබට තවම L-BTC නොමැති නම්, ඔබට විකල්ප කිහිපයක් ඇත. පළමු විකල්පය නම් ඔබට සෘජුවම එවීමයි. කවුරුන් හෝ Liquid හිදී ඔබට බිට්කොයින් වලින් ගෙවීම් කිරීමට කැමති නම්, ඔවුන්ට ලැබීමේ Address ලබා දෙන්න. අනෙක් විකල්පය නම් Exchange ඔබේ බිට්කොයින් ඔන්චේන් හෝ Lightning Network හි L-BTC සඳහා. මෙය කිරීමට, [Boltz වැනි පාලමක්](https://boltz.Exchange/) භාවිතා කළ හැක. සරලවම ඔබේ Liquid Address අඩවියේ ඇතුළත් කරන්න, එවිට ගෙවීම් Lightning Network හරහා හෝ ඔන්චේන් මඟින් සිදු කරන්න.


![LIQUID GREEN](assets/fr/30.webp)


generate a Liquid Address, "*Receive*" බොත්තම මත ක්ලික් කරන්න.


![LIQUID GREEN](assets/fr/31.webp)


Green පසුව ඔබේ Wallet හි Address ලබා ගන්නා පළමු හිස් තැන පෙන්වනු ඇත. ඔබ සම්බන්ධිත QR කේතය ස්කෑන් කළ හැකි අතර, නැතහොත් L-BTC යැවීමට Address සෘජුවම පිටපත් කළ හැක.


![LIQUID GREEN](assets/fr/32.webp)


කියමන් ජාලය මත විකාශය කරන විට, එය ඔබේ Wallet හි පෙනේ.


![LIQUID GREEN](assets/fr/33.webp)


පිළිගැනීම් ප්‍රමාණවත් ලෙස ලැබෙන තුරු ගනුදෙනුව නිශ්චිත ලෙස සලකා බැලීමට රැඳී සිටින්න. Liquid හිදී, පිළිගැනීම් වේගවත් විය යුතු අතර, මිනිත්තුවකට එක් වාරයක් වශයෙන් අවහිරතාවයක් ප්‍රකාශයට පත් කරයි.


![LIQUID GREEN](assets/fr/34.webp)


L-Sats සමඟ ඔබේ Liquid Wallet තුළ, දැන් ඔබට ඒවා යැවිය හැක. "*Send*" මත ක්ලික් කරන්න.


![LIQUID GREEN](assets/fr/35.webp)


මීළඟ පිටුවේ, ලාභලාභියාගේ Liquid Address ඇතුළත් කරන්න. ඔබට එය අතින් ඇතුළත් කළ හැකි අතර එහි QR කේතය ස්කෑන් කළ හැක.


![LIQUID GREEN](assets/fr/36.webp)


රැකවරණ මුදල තෝරන්න.


![LIQUID GREEN](assets/fr/37.webp)


"*Next*" මත ක්ලික් කර ගනුදෙනු සාරාංශ තිරය වෙත ප්‍රවේශ වන්න. Address, මුදල සහ ගාස්තු නිවැරදි බව පරීක්ෂා කරන්න.


![LIQUID GREEN](assets/fr/38.webp)


यदि सबै ठीक भयो भने, Bitcoin नेटवर्कमा लेनदेन हस्ताक्षर र प्रसारण गर्न स्क्रीनको तलमा रहेको Green बटनलाई दायाँतिर स्लाइड गर्नुहोस्।


![LIQUID GREEN](assets/fr/39.webp)


ඔබේ ගනුදෙනුව දැන් ඔබේ Bitcoin Wallet පුවරුවේ පෙනෙන අතර, තහවුරු කිරීමක් බලාපොරොත්තු වේ.


![LIQUID GREEN](assets/fr/40.webp)


අපි දැන් ඔබට Blockstream Green යෙදුම සමඟ Liquid Sidechain පහසුවෙන් භාවිතා කරන ආකාරය දන්නවා!


ඔබට මෙම උපකාරිකාව ප්‍රයෝජනවත් වූවා නම්, Green අඟුලක් පහළින් තැබීමට මම කෘතඥ වෙමි. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තූතියි!


Jaz tudi priporočam, da si ogledate ta drugi obsežen vodič o mobilni aplikaciji Blockstream Green za nastavitev onchain Bitcoin Hot Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143