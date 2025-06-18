---
name: Blockstream Green - 2FA
description: Green Wallet මත 2/2 Multisig සකසමින්
---
![cover](assets/cover.webp)


Software Wallet යනු පරිගණකයක, ස්මාර්ට්ෆෝනයක හෝ වෙනත් අන්තර්ජාල සම්බන්ධිත උපාංගයක ස්ථාපිත කරන යෙදුමක් වන අතර, ඔබට ඔබේ Bitcoin Wallet යතුරු කළමනාකරණය කිරීමට සහ ආරක්ෂා කිරීමට හැකියාව සලසයි. පුද්ගලික යතුරු වෙන් කරන දෘඩාංග පසුම්බිවලට වඩා, "Hot" පසුම්බි එබැවින් සයිබර් ප්‍රහාරවලට නිරාවරණය විය හැකි පරිසරයක ක්‍රියාත්මක වන අතර, මාරාන්තික හා සොරකම් අවදානම වැඩි කරයි.


සොෆ්ට්වෙයා වොලට් භාවිතා කළ යුත්තේ සාමාන්‍ය බිට්කොයින් ප්‍රමාණයන් කළමනාකරණය කිරීම සඳහා, විශේෂයෙන් දිනපතා ගනුදෙනු සඳහා වේ. Bitcoin සම්පත් සීමිත පුද්ගලයින් සඳහා, Hardware Wallet හි ආයෝජනය අනුපාතික නොවිය හැකි පුද්ගලයින් සඳහා, ඒවාත් රසවත් විකල්පයක් විය හැක. කෙසේ වෙතත්, අන්තර්ජාලයට නිරන්තරව නිරාවරණය වීම නිසා, ඔබේ දිගුකාලීන ඉතිරිකිරීම් හෝ විශාල අරමුදල් ගබඩා කිරීම සඳහා ඒවා අඩු ආරක්ෂිත වේ. පසුගිය අවස්ථාව සඳහා, හාර්ඩ්වෙයා වොලට් වැනි වඩාත් ආරක්ෂිත විසඳුම් තෝරා ගැනීම හොඳය.


V tem priročniku vam bom pokazal, kako izboljšati varnost Hot Wallet z uporabo možnosti "*2FA*" na Blockstream Green.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Blockstream Green හඳුන්වා දීම


Blockstream Green je Software Wallet, ki je na voljo na mobilnih napravah in namizju. Prej znan kot *Green Address*, je ta Wallet postal projekt Blockstream po njegovem prevzemu leta 2016.


Green යනු ආරම්භකයින් සඳහා ආකර්ෂණීය වන විශේෂයෙන් භාවිතා කිරීමට පහසු යෙදුමකි. එය හොඳ Bitcoin Wallet එකක අත්‍යවශ්‍ය ලක්ෂණ සියල්ලම, RBF (*Replace-by-fee*), Tor සම්බන්ධතාවයක් සඳහා විකල්පයක්, ඔබේම node එකක් සම්බන්ධ කිරීමේ හැකියාව, SPV (*Simple Payment Verification*), නාමයෙළි කිරීම සහ පාලනය ඇතුළත් කරයි.


Blockstream Green මෙන්ම Liquid Network, Blockstream විසින් සංවර්ධනය කරන ලද වේගවත් Confidential Transactions සඳහා Sidechain Bitcoin මෙන්ම ප්‍රධාන Blockchain පිටතට සහය දක්වයි. මෙම උපකාරක පංතියේදී, අපි Bitcoin පිළිබඳව පමණක් අවධානය යොමු කරමු, නමුත් Green මත Liquid භාවිතා කරන ආකාරය ඉගෙන ගැනීමට මම තවත් උපකාරක පංතියක්ද සකසා ඇත:


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## 2/2 Multisig විකල්පය (2FA)


Green මත, ඔබට සම්භාව්‍ය "*singlesig*" Hot Wallet නිර්මාණය කළ හැක. නමුත් ඔබට "*2FA Multisig*" විකල්පයද ඇත, එය ඔබේ Hot Wallet ආරක්ෂාව වැඩි දියුණු කරන අතර එහි දෛනික කළමනාකරණය අතිශය සංකීර්ණ නොකරයි.


Torej boste nastavili 2/2 Multisig Wallet, kar pomeni, da bo vsaka transakcija zahtevala podpis dveh ključev. Prvi ključ, izpeljan iz vaše 12- ali 24-besedne fraze Mnemonic, je lokalno zaščiten s PIN kodo na vašem telefonu. Imate popoln nadzor nad tem ključem. Drugi ključ je shranjen na strežnikih Blockstreama in njegova uporaba za podpis zahteva avtentikacijo, ki jo je mogoče doseči prek kode, prejete po e-pošti, SMS-u, telefonskem klicu ali, kot bomo videli v tem priročniku, prek avtentikacijske aplikacije (Authy, Google Authenticator itd.).


ඔබේ ස්වයංපාලනය Blockstream අසාර්ථක වීමේ අවස්ථාවක (උදාහරණයක් ලෙස, සමාගමේ බංකොලොත් වීම හෝ දෙවන යතුර තබා ඇති සේවාදායකයන් විනාශ වීමේ අවස්ථාවක) සහතික කිරීම සඳහා, ඔබේ Multisig සඳහා කාල සීමාකරණ යාන්ත්‍රණයක් යොදා ඇත. මෙම යාන්ත්‍රණය 2/2 Multisig එක වසරක් (හෝ නිවැරදිව 51,840 කොටස්, නමුත් මෙම අගය වෙනස් කළ හැක) පමණින් 1/2 Multisig බවට පරිවර්තනය කරයි, එවිට ඔබේ Wallet සඳහා බිට්කොයින් වියදම් කිරීමට ඔබේ දේශීය යතුර පමණක් අවශ්‍ය වේ. එබැවින්, ඔබ Blockstream සේවාදායකයන් හෝ 2FA සත්‍යාපනයට ප්‍රවේශය අහිමි කර ගත් විට, ඔබේ යෙදුම සමඟ ඔබේ බිට්කොයින් නිදහස්ව භාවිතා කිරීමට අවුරුදු එකක් උපරිමයෙන් බලා සිටින්නට සිදු වේ, Blockstream මත රඳා නොසිට.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


Ta metoda bistveno poveča varnost vašega Hot Wallet, hkrati pa vam omogoča nadzor nad vašimi bitcoini in olajša njihovo vsakodnevno uporabo. Vendar pa zahteva redne osvežitve časovne ključavnice za ohranjanje varnosti 2FA. 360-dnevno odštevanje, med katerim so vaša sredstva zaščitena z 2FA, se začne takoj, ko prejmete bitcoine. Če po 360 dneh od tega prejema ne izvedete transakcije s temi sredstvi, bodo vaši bitcoini zaščiteni le z vašim lokalnim ključem, brez 2FA.


මෙම සීමාව 2FA විකල්පය Wallet වියදම් කිරීම සඳහා වඩා සුදුසු කරයි, එහි නිතර ගනුදෙනු ස්වයංක්‍රීයව කාල සීමා නැවත නවීකරණය කරයි. දිගුකාලීන ඉතිරි කිරීමේ Wallet සඳහා, මෙය ගැටලුවක් විය හැක, ඔබට කාල සීමාව කල් ඉකුත් වීමට පෙර වසරකට එක් වරක් ඔබටම ස්විප් ගනුදෙනුවක් කිරීම ගැන සිතන්න අවශ්‍ය වන බැවින්.


මෙම ආරක්ෂක ක්‍රමයෙහි තවත් අවාසියක් වන්නේ ඔබට අල්ප සංඛ්‍යාත ලිපි රචනා ආකෘති භාවිතා කළ යුතු වීමයි. මෙය අර්ථ දක්වන්නේ, රහස්‍යතාවය පිළිබඳව, දේවල් වඩාත් සංකීර්ණ වන බවයි: ඔබ මෙන්ම ලිපි රචනා වර්ගය භාවිතා කරන පුද්ගලයින් ඉතා සුළු ප්‍රමාණයක් වන අතර, එය ඔබේ Wallet ඇඟිලි සලකුණ හඳුනා ගැනීමට පිටත නිරීක්ෂකයෙකුට පහසු වේ. තවද, මෙම ලිපි රචනා විශාල ප්‍රමාණය නිසා වැඩි ගනුදෙනු වියදම් සිදුවනු ඇත.


ඔබට 2FA විකල්පය භාවිතා නොකර "*singlesig*" Wallet එකක් Green මත සකස් කිරීමට අවශ්‍ය නම්, මම ඔබට මෙම වෙනත් උපකාරකය පරීක්ෂා කිරීමට ආරාධනා කරමි:


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Blockstream Green මෘදුකාංගය ස්ථාපනය කිරීම සහ වින්‍යාස කිරීම


පළමු පියවර වන්නේ Green යෙදුම බාගත කිරීමයි. ඔබේ යෙදුම් අලෙවියට යන්න:



- [Android සඳහා](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


ඇන්ඩ්‍රොයිඩ් පරිශීලකයින් සඳහා, ඔබට Blockstream හි GitHub හි [ලබා ගත හැකි](https://github.com/Blockstream/green_android/releases) `.apk` ගොනුව හරහා යෙදුම ස්ථාපනය කළ හැක.


![GREEN 2FA MULTISIG](assets/fr/04.webp)


Zaženite aplikacijo, nato označite polje "Sprejemam pogoje...*".


![GREEN 2FA MULTISIG](assets/fr/05.webp)


ඔබ Green පළමු වරට විවෘත කරන විට, ගෘහ පිටුව Wallet එකක් වින්‍යාස නොකළව පෙනේ. පසුව, ඔබ පසුබැසීම හෝ පසුබැසීමේ පසුබැසීමක් නිර්මාණය කළහොත්, ඒවා මෙම Interface තුළ පෙනේ. Wallet එකක් නිර්මාණය කිරීමට පෙර, ඔබේ අවශ්‍යතා සඳහා යෙදුම් සැකසුම් සකසන්නැයි මම ඔබට උපදෙස් දෙමි. "යෙදුම් සැකසුම්" මත ක්ලික් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/06.webp)


"*වැඩිදියුණු පෞද්ගලිකත්වය*" විකල්පය, Android හි පමණක් ලබා ගත හැකි, පරිශීලක පෞද්ගලිකත්වය වැඩි දියුණු කරයි, තිර රූප ගත කිරීම් අක්‍රිය කිරීම සහ යෙදුම් පෙරදසුන් සඟවා ඇත. එය ඔබේ දුරකථනය අගුළු දැමුණු විටම යෙදුම් ප්‍රවේශය ස්වයංක්‍රීයව අගුළු දමයි, ඔබේ දත්ත අනාවරණය වීම වඩා දුෂ්කර කරයි.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


ඔබේ පෞද්ගලිකත්වය වැඩි දියුණු කිරීමට කැමති අය සඳහා, යෙදුම ඔබේ ගමනාගමනය Tor හරහා rooting කිරීමේ විකල්පය ලබා දේ, එය ඔබේ සම්බන්ධතා සියල්ල සංකේතනය කර ඔබේ ක්‍රියාකාරකම් හඹා යාම අපහසු කරයි. මෙම විකල්පය යෙදුමේ මෙහෙයුම ටිකක් මන්දගාමී කළ හැකි නමුත්, ඔබේම සම්පූර්ණ නෝඩ් එකක් භාවිතා නොකරන්නේ නම්, ඔබේ පෞද්ගලිකත්වය ආරක්ෂා කිරීම සඳහා ඉතා නිර්දේශිත වේ.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


Green Wallet හිමිකරුවන්ට තමන්ගේම සම්පූර්ණ නෝඩයක් ඇති පරිශීලකයින් සඳහා, එය Electrum සේවාදායකයක් හරහා එයට සම්බන්ධ වීමේ හැකියාව ලබා දේ, Bitcoin ජාල තොරතුරු සහ ගනුදෙනු බෙදාහැරීම පිළිබඳ සම්පූර්ණ පාලනය සහතික කරමින්.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


තවත් විකල්ප විශේෂාංගයක් "*SPV Verification*" විකල්පය වන අතර, එය ඔබට Blockchain දත්ත සෘජුවම සත්‍යාපනය කිරීමට ඉඩ සලසන අතර, එමඟින් Blockstream හි පෙරනිමි නියුඩය විශ්වාස කිරීමට ඇති අවශ්‍යතාව අඩු කරයි, එහෙත් මෙම ක්‍රමය Full node හි සියලුම සහතික ලබා නොදේ.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


ඔබේ අවශ්‍යතා සඳහා මෙම සැකසුම් සකසා අවසන් වූ පසු, "*Save*" බොත්තම ක්ලික් කර යෙදුම නැවත ආරම්භ කරන්න.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Ustvarite Bitcoin Wallet na Blockstream Green


ඔබ දැන් Bitcoin Wallet එකක් නිර්මාණය කිරීමට සූදානම්. "*Get Started*" බොත්තම මත ක්ලික් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/12.webp)


ඔබට ස්ථානීය Software Wallet එකක් නිර්මාණය කිරීම හෝ Hardware Wallet හරහා Cold Wallet එකක් කළමනාකරණය කිරීම අතරින් තෝරා ගත හැක. මෙම උපකාරිකාව සඳහා, අපි Hot Wallet එකක් නිර්මාණය කිරීමට අවධානය යොමු කරමු, එබැවින් ඔබ "*මෙම උපාංගයේ*" විකල්පය තෝරා ගත යුතුය.


![GREEN 2FA MULTISIG](assets/fr/13.webp)


ඔබට පසුව පවතින Bitcoin Wallet එකක් ප්‍රතිස්ථාපනය කිරීමට හෝ නව එකක් නිර්මාණය කිරීමට තෝරා ගත හැක. මෙම උපකාරිකාව සඳහා, අපි නව Wallet එකක් නිර්මාණය කරමු. කෙසේ වෙතත්, ඔබේ පැරණි දුරකථනය අහිමි වීමෙන් පසු, උදාහරණයක් ලෙස, පවතින Bitcoin Wallet එකක් එහි Mnemonic වාක්‍යයෙන් නැවත ජනනය කිරීමට අවශ්‍ය නම්, ඔබට දෙවන විකල්පය තෝරා ගත යුතුය.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


ඔබට පසුව 12-වචන හෝ 24-වචන Mnemonic වාක්‍යයක් අතරින් තෝරා ගත හැක. මෙම වාක්‍යය ඔබේ දුරකථනය සමඟ ඇතිවන ගැටලුවක් ඇති විට, ඕනෑම අනුකූල මෘදුකාංගයකින් ඔබේ Wallet වෙත ප්‍රවේශය නැවත ලබා ගැනීමට ඔබට හැකියාව ලබා දේ. වර්තමානයේ, 24-වචන වාක්‍යයක් තෝරා ගැනීම 12-වචන වාක්‍යයකට වඩා වැඩි ආරක්ෂාවක් ලබා නොදෙයි. එබැවින්, මම ඔබට 12-වචන Mnemonic වාක්‍යයක් තෝරා ගැනීමට නිර්දේශ කරමි.


Green nato vam bo zagotovil vaš Mnemonic stavek. Preden nadaljujete, se prepričajte, da vas nihče ne opazuje. Kliknite na "*Prikaži obnovitveni stavek*", da ga prikažete na zaslonu.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**මෙම Mnemonic ඔබට ඔබේ සියලුම බිට්කොයින් සඳහා සම්පූර්ණ, සීමාවන් රහිත ප්‍රවේශය ලබා දේ**. මෙම වාක්‍යය සතු කවරෙකුට හෝ ඔබේ මුදල් සොරාගත හැක, ඔබේ දුරකථනයට භෞතික ප්‍රවේශය නොමැතිව පවා (Green මත 2/2 Wallet කේස් එකක කල් ඉකුත් වූ කාල සීමාව හෝ 2FA යටතේ).


To vam omogoča obnovitev dostopa do vaših lokalnih ključev v primeru izgube, kraje ali poškodbe vašega telefona. Zato je zelo pomembno, da ga skrbno varnostno kopirate **na fizični medij (ne digitalni)** in ga shranite na varno mesto. Lahko ga zapišete na kos papirja, ali za dodatno varnost, če gre za velik Wallet, priporočam graviranje na nosilec iz nerjavečega jekla, da ga zaščitite pred tveganjem požara, poplave ali zrušitve (za Hot Wallet, zasnovan za varovanje majhne količine bitcoinov, je verjetno dovolj preprosta papirnata varnostna kopija).


*ඔබට මෙම වචන අන්තර්ජාලයේ බෙදා හදා ගැනීමට කිසි විටෙකත් නොහැකි බව පැහැදිලියි, මම මෙම උපකාරිකාවේ කරන පරිදි. මෙම සාම්පල Wallet, Testnet මත පමණක් භාවිතා කරනු ඇති අතර උපකාරිකාව අවසානයේදී මකා දමනු ඇත.*


![GREEN 2FA MULTISIG](assets/fr/16.webp)


ඔබේ Mnemonic වාක්‍යය භෞතික මාධ්‍යයක නිවැරදිව සටහන් කර අවසන් වූ විට, "*Continue*" මත ක්ලික් කරන්න. එවිට Green Wallet ඔබේ Mnemonic වාක්‍යයේ වචන කිහිපයක් තහවුරු කරන ලෙස ඔබගෙන් ඉල්ලා සිටින අතර එය නිවැරදිව සටහන් කර ඇති බවට සහතික වීමටයි. හිස්තැන් පුරවන්න.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


ඔබේ උපාංගයේ PIN කේතය තෝරන්න, එය ඔබේ Green Wallet අගුළු විවෘත කිරීමට භාවිතා කරනු ඇත. මෙය අනුමත නොකළ භෞතික ප්‍රවේශයට එරෙහිව ඔබේ ආරක්ෂාවයි. මෙම PIN කේතය ඔබේ Wallet හි සංකේතාත්මක යතුරු නිර්ණය කිරීමේදී සම්බන්ධ නොවේ. එබැවින්, මෙම PIN කේතයට ප්‍රවේශය නොමැතිව සිටියද, ඔබේ 12- හෝ 24-වචන Mnemonic වාක්‍යය හිමිකර ගැනීමෙන් ඔබට ඔබේ ස්ථානීය යතුරු නැවත ලබා ගැනීමට හැකි වේ.


අපි ככל האפשר אקראי 6-ספרתי קוד PIN לבחור ממליצים. הקפד לשמור את הקוד הזה כדי שלא תשכח אותו, אחרת תיאלץ לאחזר את ה-Wallet מה-Mnemonic. לאחר מכן תוכל להוסיף אפשרות חסימה ביומטרית כדי להימנע מהצורך להזין את ה-PIN בכל פעם שאתה משתמש בו. באופן כללי, ביומטריה פחות מאובטחת בהרבה מה-PIN עצמו. לכן, כברירת מחדל, אני ממליץ לך לא להגדיר אפשרות ביטול נעילה זו.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


ඔබේ PIN කේතය තහවුරු කිරීමට එය දෙවන වරටත් ඇතුළත් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Pocakajte, da se vaš Wallet ustvari, nato kliknite gumb "*Ustvari račun*".


![GREEN 2FA MULTISIG](assets/fr/20.webp)


ඔබට පසුව සම්මත තනි අත්සන Wallet හෝ දෙකේ-ගුණිත සත්‍යාපනය (2FA) මඟින් ආරක්ෂිත Wallet අතරින් තෝරා ගත හැක. මෙම උපකාරිකාවේ, අපි දෙවන විකල්පය තෝරන්නෙමු.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


ඔබේ Bitcoin Multisig Wallet දැන් Green යෙදුම භාවිතයෙන් නිර්මාණය කර ඇත!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## 2FA සකසීම


ඔබේ ගිණුම මත ක්ලික් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


කොටුව Green මත ක්ලික් කරන්න "*ඔබේ ගිණුමේ ආරක්ෂාව වැඩි දියුණු කිරීම සඳහා 2FA එකතු කරන්න*".


![GREEN 2FA MULTISIG](assets/fr/24.webp)


ඔබට පසුව 2/2 Multisig හි දෙවන යතුරට ප්‍රවේශ වීම සඳහා සත්‍යාපන ක්‍රමය තෝරා ගත හැකි වේ. මෙම උපකාරිකාව සඳහා, අපි සත්‍යාපන යෙදුමක් භාවිතා කරමු. ඔබට මෙම වර්ගයේ යෙදුමක් පිළිබඳව පළපුරුද්දක් නැති නම්, Authy පිළිබඳ අපගේ උපකාරිකාව අනුගමනය කිරීමට මම නිර්දේශ කරමි:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

"*Authenticator Application*" තෝරන්න.


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green පසුව QR කේතයක් සහ ප්‍රතිසාධන යතුරක් පෙන්වනු ඇත. මෙම යතුර ඔබේ Authy යෙදුම අහිමි වූ අවස්ථාවේදී ඔබේ 2FA වෙත ප්‍රවේශය නැවත ලබා ගැනීමට ඉඩ සලසයි. මෙම යතුරේ ආරක්ෂිත උපස්ථයක් සෑදීම සුදුසුය, එහෙත් ඉහත විස්තර කළ පරිදි කාල සීමාව අවසන් වූ පසු ඔබට ඔබේ බිට්කොයින් නැවත ලබා ගැනීමේ හැකියාව ඇත.


ඔබේ සත්‍යාපන යෙදුමට නව කේතයක් එක් කර, Green විසින් සපයන ලද QR කේතය ස්කෑන් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*ඔබ කිසිවිටෙක මෙම යතුර සහ QR කේතය අන්තර්ජාලයේ බෙදා හරිය යුතු නැත, මම මෙම උපකාරිකාවේ කරන පරිදි. මෙම සාම්පල Wallet, Testnet මත පමණක් භාවිතා කරනු ඇති අතර උපකාරිකාව අවසානයේදී මකා දැමෙනු ඇත.*


"*Continue*" බොත්තම මත ක්ලික් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/27.webp)


ඔබේ සත්‍යාපන යෙදුම මත ඇති අංක 6ක ඩයිනමික් කේතය ඇතුළත් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


දැන් 2-කාණ්ඩ සත්‍යාපනය සක්‍රීය කර ඇත.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


S tem menijem lahko nastavite tudi trajanje časovne zaklepanja. Ta odštevanje se začne takoj, ko so bitcoini prejeti, in ko časovna zaklepka poteče, lahko svoja sredstva porabite samo z lokalnim ključem, brez potrebe po 2FA. Privzeto trajanje je nastavljeno na 12 mesecev, vendar je za varčevalni Wallet smiselno izbrati 15 mesecev, da zmanjšate pogostost obnove časovne zaklepanja. Nasprotno pa je za porabni Wallet morda boljša 6-mesečna časovna zaklepka, saj se bo pogosto obnavljala z vašimi dnevnimi transakcijami, krajša časovna zaklepka pa zmanjša čakanje v primeru težave z 2FA. Vi se odločite, katero trajanje časovne zaklepanja vam najbolj ustreza.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


ඔබට දැන් මෙම මෙනුවෙන් පිටවිය හැක. ඔබේ Multisig Wallet සූදානම්!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## ඔබේ Wallet සකස් කිරීම Blockstream Green මත


Če želite prilagoditi svoj Wallet, kliknite na tri majhne pike v zgornjem desnem kotu.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


"*Rename*" විකල්පය ඔබට ඔබේ Wallet හි නම අභිරුචිකරණය කිරීමට ඉඩ සලසයි, එය විශේෂයෙන්ම ප්‍රයෝජනවත් වේ ඔබ එකම යෙදුම මත විශාල වශයෙන් පසුම්බි කළමනාකරණය කරන විට.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


"*ඒකකය*" මෙනුව ඔබට ඔබේ Wallet හි මූලික ඒකකය වෙනස් කිරීමට ඉඩ සලසයි. උදාහරණයක් ලෙස, ඔබට එය බිට්කොයින් වෙනුවට සතෝෂි ලෙස පෙන්වීමට තෝරා ගත හැක.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


"*සැකසුම්*" මෙනුව ඔබේ Bitcoin Wallet හි විවිධ විකල්ප වෙත ප්‍රවේශය ලබා දේ.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


මෙහි, උදාහරණයක් ලෙස, ඔබේ දිගු සමාජික යතුර සහ එහි *විස්තරකරු* සොයා ගත හැක, ඔබ මෙම Wallet වෙතින් පමණක් නිරීක්ෂණ මාදිලියෙන් Wallet එකක් පිහිටුවීමට සැලසුම් කරන්නේ නම් ප්‍රයෝජනවත් වේ.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


Wallet PIN කේතය වෙනස් කිරීම සහ ජෛවමාන සම්බන්ධතාවයක් සක්‍රීය කිරීමද ඔබට කළ හැක.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Blockstream Green භාවිතා කිරීම


දැන් ඔබේ Bitcoin Wallet පිහිටුවා ඇති බැවින්, ඔබේ පළමු Sats ලබා ගැනීමට සූදානම්! සරලව "*Receive*" බොත්තම ක්ලික් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Green පසුව ඔබේ Wallet හි Address ලබා ගන්නා පළමු හිස් තැන පෙන්වනු ඇත. ඔබ සම්බන්ධිත QR කේතය ස්කෑන් කළ හැකි අතර, බිට්කොයින් යැවීමට Address සෘජුවම පිටපත් කළ හැක. මෙම වර්ගයේ Address හි ගෙවීම්කරු විසින් යැවිය යුතු මුදල විශේෂිත නොවේ. කෙසේ වෙතත්, ඔබට විශේෂිත මුදලක් ඉල්ලා සිටින Address එකක් generate කළ හැක, ඉහළ දකුණු කෙළවරේ ඇති කුඩා ලප තුන මත ක්ලික් කිරීමෙන්, පසුව "*Request amount*" මත ක්ලික් කිරීමෙන්, අවශ්‍ය මුදල ඇතුළත් කිරීමෙන්.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


Ko je transakcija predvajana v omrežju, se bo pojavila v vašem Wallet.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


ප්‍රතිලාභය නිශ්චිත ලෙස සලකා බැලීමට ප්‍රමාණවත් තහවුරු කිරීම් ලැබෙන තුරු රැඳී සිටින්න.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Wallet හි බිට්කොයින් සමඟ, ඔබට දැන් බිට්කොයින් යැවිය හැක. "*Send*" මත ක්ලික් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/42.webp)


මීළඟ පිටුවේ, ලාභීගේ Address ඇතුළත් කරන්න. ඔබට එය අතින් ඇතුළත් කළ හැකි අතර නැතහොත් QR කේතයක් ස්කෑන් කළ හැක.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


රැකවරණ මුදල තෝරන්න.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


තිරයේ පහළින්, ඔබට මෙම ගනුදෙනුව සඳහා ගාස්තු අනුපාතය තෝරා ගත හැක. යෙදුමේ නිර්දේශ අනුගමනය කිරීම හෝ ඔබේ ගාස්තු අභිරුචිකරණය කිරීමේ විකල්පය ඔබට ඇත. අනෙක් බලාපොරොත්තු වන ගනුදෙනු සමඟ සසඳන විට ගාස්තුව වැඩි වීමෙන්, ඔබේ ගනුදෙනුව වේගයෙන් ක්‍රියාත්මක වේ. ගාස්තු වෙළඳපොළ තොරතුරු සඳහා, කරුණාකර [Mempool.space](https://Mempool.space/) හි "*Transaction Fees*" කොටසට පිවිසෙන්න.


![GREEN 2FA MULTISIG](assets/fr/45.webp)


"*Next*" මත ක්ලික් කර ගනුදෙනු සාරාංශ තිරය වෙත ප්‍රවේශ වන්න. Address, මුදල සහ ගාස්තු නිවැරදි බව පරීක්ෂා කරන්න.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


If all goes well, slide the Green button at the bottom of the screen to the right to sign and broadcast the transaction on the Bitcoin network.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


මෙය ඔබේ සත්‍යාපන කේතය ඇතුළත් කළ යුතු වේ Blockstream විසින් තබා ඇති දෙවන Multisig යතුර අගුළු හරින. ඔබේ සත්‍යාපන යෙදුම මත පෙන්වන 6 අංක කේතය ඇතුළත් කරන්න.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


ඔබේ ගනුදෙනුව දැන් ඔබේ Bitcoin Wallet පුවරුවේ පෙනෙන අතර, තහවුරු කිරීමක් බලාපොරොත්තු වේ.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


Zdaj veste, kako enostavno nastaviti 2/2 Multisig Wallet z uporabo Blockstream Green-ove možnosti 2FA!


ඔබට මෙම උපකාරිකාව ප්‍රයෝජනවත් වූවා නම්, Green අඟුලක් පහළින් දමා යාමට මම කෘතඥ වන්නෙමි. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තූතියි!


Priporočam tudi, da si ogledate ta drugi obsežen vodič o mobilni aplikaciji Blockstream Green za nastavitev Liquid Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a