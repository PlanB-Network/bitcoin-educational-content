---
name: Satochip
description: Satochip pametno kartico nastavljanje in uporaba
---
![cover](assets/cover.webp)


Hardware Wallet යනු Bitcoin Wallet හි පෞද්ගලික යතුරු කළමනාකරණය කිරීම සහ ආරක්ෂා කිරීම සඳහා කැපවූ ඉලෙක්ට්‍රොනික උපාංගයකි. අන්තර්ජාලයට සම්බන්ධ වීමේ හැකියාව ඇති පොදු-අරමුණු යන්ත්‍රවල ස්ථාපිත කරන ලද මෘදුකාංග පසුම්බි (හෝ Hot පසුම්බි) වලට වඩා, දෘඩාංග පසුම්බි පෞද්ගලික යතුරු භෞතිකව වෙන් කිරීමේ හැකියාව ලබා දෙන අතර, හැකින් කිරීම සහ සොරකම් කිරීමේ අවදානම් අඩු කරයි.


Hardware Wallet का मुख्य लक्ष्य उपकरण की कार्यक्षमताओं को कम करना है ताकि इसके हमले की सतह को कम किया जा सके। एक छोटी हमले की सतह का मतलब है कम संभावित हमले के वेक्टर, यानी सिस्टम में कम कमजोरियाँ जिनका उपयोग हमलावर बिटकॉइन तक पहुँचने के लिए कर सकते हैं।


ඔබේ බිට්කොයින් ආරක්ෂා කිරීමට Hardware Wallet භාවිතා කිරීම නිර්දේශිතය, විශේෂයෙන්ම ඔබට සම්පූර්ණ වටිනාකමක් හෝ ඔබේ මුළු දේපලවල ප්‍රතිශතයක් ලෙස වැදගත් ප්‍රමාණයක් තිබේ නම්.


හාර්ඩ්වෙයා වොලට් භාවිතා කරන්නේ පරිගණකයක හෝ ස්මාර්ට්ෆෝනයක Wallet කළමනාකරණ මෘදුකාංග සමඟ එකට වේ. මෙම මෘදුකාංගය ගනුදෙනු නිර්මාණය කළමනාකරණය කරයි, නමුත් මෙම ගනුදෙනු වල සත්‍යාපනය සඳහා අවශ්‍ය සංකේතාත්මක අත්සන Hardware Wallet තුළ පමණක් සිදු වේ. මෙය අදහස් කරන්නේ පුද්ගලික යතුරු කිසි විටෙකත් අවදානම් පරිසරයකට නිරාවරණය නොවන බවයි.


හාර්ඩ්වෙයා වොලට් භාවිතා කරන්නාට ද්විත්ව ආරක්ෂාවක් ලබා දේ: එක් පැත්තකින්, ඒවා පුද්ගලික යතුරු අන්තර්ජාලයෙන් වෙන්ව තබා දුරස්ථ ප්‍රහාර වලින් ඔබේ බිට්කොයින් ආරක්ෂා කරයි, සහ අනෙක් පැත්තකින්, සාමාන්‍යයෙන් යතුරු ලබා ගැනීමේ උත්සාහයන්ට එරෙහිව වඩා හොඳ භෞතික ප්‍රතිරෝධයක් ලබා දේ. සහ එය නිවැරදිව මෙම ආරක්ෂක මාර්ගෝපදේශ 2 මතයි, එකිනෙකා විවිධ ආකෘති විනිශ්චය කර ශ්‍රේණිගත කළ හැකි වෙන්නේ.


මෙම උපකාරිකාවේ, මම මෙම විසඳුම්වලින් එකක් සොයා ගැනීමට යෝජනා කරමි: Satochip.


## Satochip සඳහා හැඳින්වීම


Satochip යනු *EAL6+* සහතික කළ චිප් එකක් සහිත කාඩ්පතක් ලෙස Hardware Wallet එකක් වන අතර, එය ඉතා උසස් ආරක්ෂක සම්මතයකි (*NXP JCOP*). එය බෙල්ජියම් සමාගමක් විසින් නිෂ්පාදනය කර ඇත.


![SATOCHIP](assets/notext/01.webp)


මෙම ස්මාර්ට් කාඩ්පත €25 කට විකිණේ, එය වෙළඳපොළේ ඇති අනෙකුත් දෘඩාංග පසුම්බිවලට සාපේක්ෂව ඉතාමත්ම අඩු මිලකට ලබා ගත හැක. චිප් එක භෞතික ප්‍රහාරවලට ඉතා හොඳ ප්‍රතිරෝධයක් සහතික කරන ආරක්ෂිත මූලද්‍රව්‍යයකි. තවද, එහි කේතය විවෘත මූලාශ්‍ර (*AGPLv3*) වේ.

කෙසේ වෙතත්, එහි ආකෘතිය නිසා, Satochip හි අනෙකුත් දෘඩාංග වැනි විකල්ප බොහෝ නොමැත. පැහැදිලිවම බැටරියක්, කැමරාවක් හෝ මයික්‍රෝ SD කාඩ් රීඩරයක් නොමැත, එය කාඩ්පතක් බැවින්. මගේ අදහස අනුව එහි විශාලතම අවාසිය Hardware Wallet හි තිරයක් නොමැතිකමයි, එය විශේෂිත වර්ගයේ දුරස්ථ ප්‍රහාර සඳහා වඩාත් අවදානම් කරයි. ඇත්ත වශයෙන්ම, මෙය පරිශීලකයා අන්ධව අත්සන් කිරීමට හා ඔවුන්ගේ පරිගණක තිරය මත දැක ඇති දේ විශ්වාස කිරීමට බල කරයි.


එහි සීමා ඇති වුවද, Satochip එහි අඩු මිල නිසා රසවත් වේ. මෙම Wallet විශේෂයෙන්ම Hardware Wallet screen එකකින් ආරක්ෂා කරන ලද ඉතිරි කිරීමේ Wallet එකකට අමතරව වියදම් කිරීමේ Wallet එකක ආරක්ෂාව වැඩි දියුණු කිරීමට භාවිතා කළ හැක. එය කුඩා ප්‍රමාණයේ බිට්කොයින් තබා ගන්නා සහ වඩාත් සංකීර්ණ උපාංගයකට සියය යුරෝ වියදම් කිරීමට කැමති නොවන අය සඳහා හොඳ විසඳුමක් වේ. තවද, Multisig වින්‍යාසවල, හෝ අනාගතයේදී timelock සමඟ Wallet පද්ධතිවල Satochips භාවිතය රසවත් වාසි ලබා දිය හැක.


Satochip සමාගම තවත් නිෂ්පාදන 2 ක් ද ලබා දේ. Satodime නම්, එය බිට්කොයින් අන්තර්ජාලයෙන් බැහැරව ගබඩා කිරීමට නිර්මාණය කරන ලද බියර කාඩ්පතක් වන අතර, ගනුදෙනු සඳහා අවසර නොදෙයි. එය Wallet කඩදාසි වර්ගයක් වැනි එකක් වන අතර, එය වඩාත් ආරක්ෂිත වන අතර, උදාහරණයක් ලෙස, තෑග්ගක් ලබා දීමට භාවිතා කළ හැක. අවසානයේ, Seedkeeper නම්, එය Mnemonic වාක්‍ය කළමනාකරු වේ. එය අපගේ seed ආරක්ෂිතව සුරැකීමට භාවිතා කළ හැකි අතර එය කඩදාසියක සෘජුවම සටහන් නොකෙරේ.


## Satochip කෙසේ මිලදී ගන්නේද?


Satochip විකිණීමට ලබා ගත හැක [නිල වෙබ් අඩවියෙන්](https://satochip.io/product/satochip/). එය භෞතික වෙළඳසැලකින් මිලදී ගැනීමට, ඔබට [සහතික ලැබූ නැවත විකුණුම්කරුවන්ගේ ලැයිස්තුව](https://satochip.io/resellers/) Satochip වෙබ් අඩවියෙන් සොයා ගත හැක.


Za interakcijo z vašo programsko opremo za upravljanje Wallet, Satochip ponuja dve možnosti: prek NFC komunikacije ali prek čitalnika pametnih kartic. Za možnost NFC poskrbite, da je vaša naprava združljiva s to tehnologijo ali pridobite zunanji NFC čitalnik. Satochip deluje na standardni frekvenci 13,56 MHz. Drugače pa lahko kupite tudi čitalnik pametnih kartic. Enega lahko najdete na spletni strani Satochip ali drugje.


![SATOCHIP](assets/notext/02.webp)


## Kako nastaviti Satochip s Sparrow?


ඔබගේ Satochip ලැබුණු පසු, පළමු පියවර වන්නේ එය විවෘත කර නොමැති බව සහතික කිරීම සඳහා ඇසුරුම් පරීක්ෂා කිරීමයි. Satochip හි ඇසුරුමට මුද්‍රා කිරීමේ ස්ටිකරයක් ඇතුළත් විය යුතුය. මෙම ස්ටිකරය අතුරුදහන් වී ඇත්නම් හෝ හානි වී ඇත්නම්, එය සමාර්ථ කාඩ්පත කුමන්ත්‍රණයකට ලක්වී ඇති අතර සත්‍ය නොවිය හැකි බව පෙන්වයි.

![SATOCHIP](assets/notext/03.webp)

ඔබට Satochip එක ඇතුළත සොයා ගත හැකිය.


![SATOCHIP](assets/notext/04.webp)


Wallet を管理するには、このチュートリアルで Sparrow を使用することをお勧めします。まだソフトウェアをお持ちでない場合は、[公式ウェブサイトを訪れてダウンロードしてください](https://sparrowwallet.com/download/)。また、Sparrow Wallet に関するチュートリアルもご覧いただけます（近日公開予定）。


![SATOCHIP](assets/notext/05.webp)


ඔබේ Satochip කාඩ්පත ස්මාර්ට් කාඩ් කියවනයට ඇතුළත් කරන්න හෝ එය NFC කියවනය මත තබා, කියවනය ඔබේ පරිගණකයට සම්බන්ධ කරන්න, එහි Sparrow විවෘතව ඇත.


![SATOCHIP](assets/notext/06.webp)


Sparrow Wallet විවෘත කර, ඔබ Bitcoin නියුඩ් එකකට නිවැරදිව සම්බන්ධ වී ඇති බව සහතික කරන්න. මෙය කිරීමට, දකුණු පහළ කොටුවේ ටික් එක පරීක්ෂා කරන්න: ඔබ පොදු නියුඩ් එකකට සම්බන්ධ වී ඇත්නම් එය කහ විය යුතුය, Bitcoin Core සඳහා සම්බන්ධතාවයක් සඳහා Green හෝ Electrum සඳහා නිල් විය යුතුය.


![SATOCHIP](assets/notext/07.webp)


Sparrow Wallet මත, "*ගොනුව*" ටැබය ක්ලික් කරන්න.


![SATOCHIP](assets/notext/08.webp)


පසුව "*New Wallet*" මෙනුවේ.


![SATOCHIP](assets/notext/09.webp)


Wallet සඳහා නමක් තෝරා "*Wallet සාදන්න*" ක්ලික් කරන්න.


![SATOCHIP](assets/notext/10.webp)


කොටුව "*Connected Hardware Wallet*" බොත්තම මත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/11.webp)


කොටුව "*Scan...*" බොත්තම මත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/12.webp)


ඔබේ Satochip පෙනිය යුතුය. "*Import Keystore*" මත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/13.webp)


Naslednje, morate nastaviti PIN kodo za odklepanje vašega Satochip. Izberite močno geslo, dolgo med 4 in 16 znakov. Naredite varnostno kopijo tega gesla.


සැලකිලිමත් වන්න, මෙම මුරපදය passphrase එකක් නොවේ. මෙය අදහස් කරන්නේ මෙම මුරපදය නොමැතිව පවා, ඔබේ Mnemonic වාක්‍යය අවශ්‍ය නම් ඔබේ Wallet නැවත මෘදුකාංගයට ආයාත කිරීමට ඉඩ ලබා දෙන බවයි. මුරපදය භාවිතා කරන්නේ Satochip වෙත ප්‍රවේශය ආරක්ෂා කිරීමට පමණි. එය අනෙකුත් දෘඩාංග පසුම්බිවල ඇති PIN කේතයට සමාන වේ.


පස්සේ මුරපදය ඇතුළත් කළ විට, "*Import Keystore*" බොත්තම මත නැවත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/14.webp)


මුරපදය නැවත සටහන් කර, "*Initialize*" බොත්තම ක්ලික් කරන්න.


![SATOCHIP](assets/notext/15.webp)


ඔබට පසුව ඔබේ Mnemonic වාක්‍යය ජනනය කිරීම සඳහා කවුළුවට පැමිණේ. "*generate New*" බොත්තම ක්ලික් කරන්න.


![SATOCHIP](assets/notext/16.webp)

ඔබේ ප්‍රතිසාධන වාක්‍යය කඩදාසි හෝ ලෝහ මාධ්‍යයක ලිවීමෙන් භෞතික පිටපත් එකක් හෝ වැඩි ගණනක් සාදන්න. මෙම වාක්‍යය අමතර ආරක්ෂාවකින් තොරව ඔබේ බිට්කොයින් සඳහා සම්පූර්ණ ප්‍රවේශය ලබා දෙන බැවින්, කවුරුන් හෝ එය සොයා ගන්නේ නම්, ඔවුන්ට ඔබේ Satochip හෝ එහි PIN කේතය නොමැතිව ඔබේ බිට්කොයින් කඩිනමින් සොරා ගත හැකිය. එබැවින්, මෙම උපස්ථයන් ආරක්ෂා කිරීම වැදගත් වේ. තවද, මෙම වාක්‍යය ඔබේ Satochip අහිමි වුවහොත්, හානි වුවහොත්, හෝ ඔබේ PIN කේතය අමතක වුවහොත්, ඔබේ බිට්කොයින් නැවත ලබා ගැනීමට ඔබට ඉඩ සලසයි.

![SATOCHIP](assets/notext/17.webp)


ඔබගේ Bitcoin Wallet සාර්ථකව නිර්මාණය කර ඇත.


![SATOCHIP](assets/notext/18.webp)


කළින් "*Import Keystore*" බොත්තම මත නැවත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/19.webp)


ඔබගේ Wallet දැන් නිර්මාණය වී ඇත. ඔබගේ පුද්ගලික යතුරු දැන් ඔබගේ Satochip හි ස්මාර්ට් කාඩ්පතේ ගබඩා කර ඇත. දිගටම යාමට "*Apply*" බොත්තම ක්ලික් කරන්න.


![SATOCHIP](assets/notext/20.webp)


Sparrow Wallet විසින් කළමනාකරණය කරන මහජන තොරතුරු ආරක්ෂා කිරීම සඳහා, ඔබේ Satochip හි PIN කේතයට අමතරව අමතර මුරපදයක් සකස් කිරීම නිර්දේශ කරයි. මෙම මුරපදය Sparrow Wallet වෙත ප්‍රවේශය ආරක්ෂා කිරීම සහ ඔබේ මහජන යතුරු, ලිපින සහ ගනුදෙනු ඉතිහාසය කිසිදු අනුමත නොකළ ප්‍රවේශයකින් ආරක්ෂා කිරීම සඳහා උපකාරී වේ.


![SATOCHIP](assets/notext/21.webp)


ඔබේ මුරපදය ක්ෂේත්‍ර දෙකේම ඇතුළත් කර, "*මුරපදය සකසන්න*" බොත්තම මත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/22.webp)


අහින්සකව, ඔබේ Satochip දැන් Sparrow Wallet මත වින්‍යාස කර ඇත.


![SATOCHIP](assets/notext/23.webp)


Zdaj, ko je vaš Wallet ustvarjen, lahko odklopite svoj Satochip. Hranite ga na varnem mestu!


## Kako prejeti bitcoine s Satochip?


Wallet එකේ "*Receive*" ටැබය ක්ලික් කරන්න.


![SATOCHIP](assets/notext/24.webp)


Sparrow Wallet ඔබේ Wallet සඳහා Address එකක් ජනනය කරයි. සාමාන්‍යයෙන්, අනෙක් දෘඩාංග පසුම්බි සඳහා, Address එක සෘජුවම උපාංගයේ තිරය මත සත්‍යාපනය කිරීමට "*Display Address*" මත ක්ලික් කිරීම නිර්දේශිත වේ. අවාසනාවකට මෙන්, මෙම විකල්පය Satochip සමඟ ලබා ගත නොහැක, නමුත් ඔබේ අනෙක් පසුම්බි සඳහා එය භාවිතා කිරීමට වග බලා ගන්න.


![SATOCHIP](assets/notext/25.webp)


ඔබට මෙම Address සමඟ ආරක්ෂා කරන ලද බිට්කොයින්වල මූලාශ්‍රය විස්තර කිරීමට "*ලේබලයක්*" එක් කළ හැකිය. මෙය ඔබට ඔබේ UTXO හොඳින් කළමනාකරණය කිරීමට උපකාරී වන හොඳ පුරුද්දකි.


![SATOCHIP](assets/notext/26.webp)


වැඩි විස්තර සඳහා ලේබල් කිරීම පිළිබඳව, මම මෙම වෙනත් උපකාරකයද බලන්න යෝජනා කරමි:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

ඔබට පසුව මෙම Address භාවිතා කර බිට්කොයින් ලබා ගත හැක.


![SATOCHIP](assets/notext/27.webp)

## Kako poslati Bitcoine z Satochip?

Zdaj ko ste prejeli svoj prvi Sats v svojem varnem Wallet s Satochip, jih lahko tudi porabite! Povežite svoj Satochip z računalnikom, zaženite Sparrow Wallet in nato pojdite na zavihek "*Send*" za sestavo nove transakcije.


![SATOCHIP](assets/notext/28.webp)


ඔබට කාසි පාලනය සිදු කිරීමට අවශ්‍ය නම්, එනම්, විශේෂිතව ගනුදෙනුවේ පරිභෝජනය කිරීමට UTXOs තෝරා ගැනීමට, "*UTXOs*" ටැබය වෙත යන්න. ඔබට වියදම් කිරීමට අවශ්‍ය UTXOs තෝරන්න, එවිට "*Send Selected*" මත ක්ලික් කරන්න. ඔබ "*Send*" ටැබයේ එකම තිරයට යළි යොමු කෙරෙනු ඇත, නමුත් ඔබේ ගනුදෙනුව සඳහා UTXOs දැනටමත් තෝරාගෙන ඇත.


![SATOCHIP](assets/notext/29.webp)


ඉලක්කය Address ඇතුළත් කරන්න. "*+ Add*" බොත්තම ක්ලික් කිරීමෙන් ඔබට බහු ලිපින ඇතුළත් කළ හැක.


![SATOCHIP](assets/notext/30.webp)


"*"ලේබල්"*" ලෙස මෙම වියදමේ අරමුණ මතක තබා ගන්න.


![SATOCHIP](assets/notext/31.webp)


Izberite znesek, poslan na ta Address.


![SATOCHIP](assets/notext/32.webp)


ඔබේ ගනුදෙනුවේ ගාස්තු අනුපාතය වත්මන් වෙළඳපොළට අනුව සකසන්න.


![SATOCHIP](assets/notext/33.webp)


ඔබේ ගනුදෙනුවේ සියලු පරාමිතීන් නිවැරදි බව සහතික කර, පසුව "*ගනුදෙනුව තනන්න*" මත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/34.webp)


Če je vse po vašem zadovoljstvu, kliknite na "*Dokončaj transakcijo za podpis*".


![SATOCHIP](assets/notext/35.webp)


"*"සයින්*" මත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/36.webp)


කොටස "*Sign*" මත නැවත ඔබන්න, ඔබේ Satochip අසල.


![SATOCHIP](assets/notext/37.webp)


ඔබේ Satochip හි PIN කේතය ඇතුළත් කර, ඔබේ ගනුදෙනුව අත්සන් කිරීමට "*Sign*" මත නැවත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/38.webp)


ඔබේ ගනුදෙනුව දැන් අත්සන් කර ඇත. එය Bitcoin ජාලයට විකාශය කිරීමට "*Broadcast Transaction*" මත ක්ලික් කරන්න.


![SATOCHIP](assets/notext/39.webp)


ඔබට එය Sparrow Wallet හි "*Transactions*" ටැබ් එකේ සොයා ගත හැක.


![SATOCHIP](assets/notext/40.webp)


සුභ පැතුම්, ඔබ දැන් Satochip භාවිතා කිරීම පිළිබඳව දැනුවත් වේ! මෙම උපකාරකය ප්‍රයෝජනවත් වූවා නම්, පහත අඟුල් සලකුණක් ලබා දීම මම අගය කරනවා. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තුතියි!