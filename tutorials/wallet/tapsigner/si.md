---
name: Tapsigner
description: ටැප්සයිනර් එකක් Nunchuk සමඟ සකස් කිරීම සහ භාවිතා කිරීම
---
![cover](assets/cover.webp)


Hardware Wallet යනු Bitcoin Wallet හි පෞද්ගලික යතුරු කළමනාකරණය සහ ආරක්ෂාව සඳහා කැපවූ ඉලෙක්ට්‍රොනික උපාංගයකි. අන්තර්ජාලයට සම්බන්ධ වීමේ හැකියාව ඇති පොදු-අරමුණු යන්ත්‍රවල ස්ථාපිත කරන ලද මෘදුකාංග පසුම්බි (හෝ Hot පසුම්බි) වලට වඩා, දෘඩාංග පසුම්බි පෞද්ගලික යතුරු භෞතිකව වෙන් කිරීමේ හැකියාව ලබා දෙන අතර, හැකින් සහ සොරකම් කිරීමේ අවදානම් අඩු කරයි.


Hardware Wallet का मुख्य लक्ष्य उपकरण की कार्यक्षमताओं को कम करना है ताकि इसके हमले की सतह को कम किया जा सके। एक छोटी हमले की सतह का मतलब है कम संभावित हमले के वेक्टर, यानी सिस्टम में कम कमजोर बिंदु जिन्हें हमलावर बिटकॉइन तक पहुंचने के लिए शोषण कर सकते हैं।


ඔබේ බිට්කොයින් ආරක්ෂා කිරීම සඳහා Hardware Wallet භාවිතා කිරීම නිර්දේශිතය, විශේෂයෙන්ම ඔබට සම්පූර්ණ වටිනාකමක් හෝ ඔබේ මුළු දේපලවල ප්‍රතිශතයක් ලෙස වැදගත් ප්‍රමාණයක් තිබේ නම්.


හාර්ඩ්වෙයා වොලට් භාවිතා කරන්නේ පරිගණකයක හෝ ස්මාර්ට්ෆෝනයක Wallet කළමනාකරණ මෘදුකාංගයක් සමඟ එකට වේ. මෙම මෘදුකාංගය ගනුදෙනු නිර්මාණය කළමනාකරණය කරයි, නමුත් මෙම ගනුදෙනු වල සත්‍යාපනය සඳහා අවශ්‍ය ක්‍රිප්ටෝග්‍රැෆි සහිත්‍යමය අත්සන Hardware Wallet තුළ පමණක් සිදු වේ. මෙය අදහස් කරන්නේ පුද්ගලික යතුරු කිසි විටෙකත් අවදානම් පරිසරයකට හෙළා නොදැමීමයි.


හාර්ඩ්වෙයා වොලට් සපයන ද්විත්ව ආරක්ෂාව: එක් පැත්තකින්, ඒවා ඔබේ බිට්කොයින් දුරස්ථ ප්‍රහාර වලින් ආරක්ෂා කරයි පුද්ගලික යතුරු අන්තර්ජාලයෙන් බැහැර තබා, සහ අනෙක් පැත්තකින්, ඒවා සාමාන්‍යයෙන් යතුරු ලබා ගැනීමේ උත්සාහයන්ට එරෙහිව වඩා හොඳ භෞතික ප්‍රතිරෝධය සපයයි. සහ එය නිවැරදිව මෙම ආරක්ෂක මාර්ග 2 මතයි, එකිනෙකා විවිධ ආකෘති විනිශ්චය කර සහ ශ්‍රේණිගත කළ හැකි.


මෙම උපදෙස් මාලාවේ, මම මෙම විසඳුම් වලින් එකක් සොයා බැලීමට යෝජනා කරමි: Coinkite විසින් නිර්මාණය කරන ලද Tapsigner.


## Tapsigner සඳහා හැඳින්වීම


Tapsigner Coinkite podjetja, ki je znano tudi po izdelavi Coldcards, je Hardware Wallet, zasnovan v obliki NFC kartice.


![TAPSIGNER NUNCHUK](assets/notext/01.webp)


Tapsigner BIP32 අනුව මහා පෞද්ගලික යතුරක් සහ දාම කේතයක් සමඟ යුගලයක් ගබඩා කිරීමට ඉඩ සලසයි, ක‍්‍රිප්ටෝග‍්‍රාෆි යතුරු ගසක් නිර්මාණය කිරීමට. මෙම යතුරු ගනුදෙනු අත්සන් කිරීමට භාවිතා කළ හැකි අතර, Tapsigner දුරකථනයක් හෝ NFC කාඩ් කියවනයක් මත තබා ඇත.

Ta NFC kartica se prodaja za $19.99, kar je zelo ugodno v primerjavi z drugimi denarnicami na trgu. Vendar pa zaradi svoje oblike Tapsigner ne ponuja toliko možnosti kot druge naprave. Očitno ni baterije, kamere ali bralnika micro SD kartic, saj je to kartica. Po mojem mnenju je njegova največja pomanjkljivost pomanjkanje zaslona na Hardware Wallet, kar ga naredi bolj ranljivega za določene vrste oddaljenih napadov. To namreč prisili uporabnika, da podpisuje na slepo in zaupa temu, kar vidi na zaslonu svojega računalnika.


එහි සීමා ඇති වුවද, Tapsigner වටිනාකම අඩු වීම නිසා රසවත් විය හැක. මෙම Wallet විශේෂයෙන්ම Hardware Wallet screen එකකින් ආරක්ෂා කරන ලද ඉතිරි කිරීමේ Wallet එකකට අමතරව වියදම් කිරීමේ Wallet එකක ආරක්ෂාව වැඩි දියුණු කිරීමට භාවිතා කළ හැක. එය කුඩා ප්‍රමාණයේ බිට්කොයින් තබා ගන්නා සහ වඩාත් සංකීර්ණ උපාංගයකට සියය යුරෝ වියදම් කිරීමට කැමති නොවන අය සඳහා හොඳ විසඳුමක් නියෝජනය කරයි. තවද, Multisig වින්‍යාසවල, හෝ අනාගතයේදී timelock සමඟ Wallet පද්ධතිවල Tapsigner භාවිතය රසවත් ප්‍රතිලාභ ලබා දිය හැක.


## ටැප්සයිනර් එකක් මිලදී ගැනීම කෙසේද?


Tapsigner හි මිලදී ගැනීම [නිල Coinkite වෙබ් අඩවියෙන්](https://store.coinkite.com/store/category/tapsigner) ලබා ගත හැක. එය භෞතික වෙළඳසැලකින් මිලදී ගැනීමට, [සහතික ලත් නැවත විකිණුම්කරුවන්ගේ ලැයිස්තුව](https://coinkite.com/resellers) වෙබ් අඩවියේ සොයා ගත හැක.


ඔබට NFC සන්නිවේදන සඳහා අනුකූල දුරකථනයක් හෝ 13.56 MHz ප්‍රමිතී තරංග ආවර්තනයේදී NFC කාඩ්පත් කියවීමට USB උපාංගයක් අවශ්‍ය වනු ඇත.


## Kako inicializirati Tapsigner z Nunchuk?


ඔබගේ Tapsigner ලබාගෙන ඇති විට, පළමු පියවර වන්නේ එය විවෘත කර නොමැති බව සහතික කිරීම සඳහා ඇසුරුම පරීක්ෂා කිරීමයි. ඇසුරුම හානියට පත් වී ඇත්නම්, එය කාඩ්පත ආරක්ෂා වී නොමැති බව සහ සත්‍ය නොවනු ඇතැයි පෙන්විය හැක. CoinKite ඔබගේ Tapsigner රේඩියෝ තරංග අවහිර කරන කේස් එකක් සමඟ ලබා දෙනු ඇත. එය ඔබගේ ඇසුරුම තුළ පවතින බව සහතික කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/02.webp)


Wallet කළමනාකරණය කිරීම සඳහා, අපි **Nunchuk Wallet** ජංගම යෙදුම භාවිතා කරන්නෙමු. ඔබේ ස්මාර්ට්ෆෝනය NFC අනුකූල වන බව සහතික කර, පසුව [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) හෝ එහි [`.apk` ගොනුව](https://github.com/nunchuk-io/nunchuk-android/releases) හරහා සෘජුවම Nunchuk බාගන්න.


![TAPSIGNER NUNCHUK](assets/notext/03.webp)

ඔබ Nunchuk පළමු වරට භාවිතා කරන්නේ නම්, යෙදුම ඔබට ගිණුමක් තනන්න කියා ඉල්ලා සිටියි. මෙම උපකාරිකාව සඳහා, එකක් තැනීම අවශ්‍ය නොවේ. එබැවින්, ගිණුමකින් තොරව ඉදිරියට යාමට "*අමුත්තා ලෙස දිගටම කරගෙන යන්න*" තෝරන්න.

![TAPSIGNER NUNCHUK](assets/notext/04.webp)


පසුව "*Unassisted Wallet*" මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/05.webp)


ඊළඟට, "*මම මගේම මඟ පෙන්වන්නම්*" බොත්තම මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/06.webp)


Nunchuk में, "*Keys*" टैब के बगल में "*+*" बटन पर क्लिक करें।


![TAPSIGNER NUNCHUK](assets/notext/07.webp)


"*"NFC යතුර එකතු කරන්න*" තෝරන්න.


![TAPSIGNER NUNCHUK](assets/notext/08.webp)


පසුව "*Add TAPSIGNER*" මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/09.webp)


"*ඉදිරියට*" මත ක්ලික් කර, ඔබේ Tapsigner NFC කාඩ්පත ඔබේ ස්මාර්ට්ෆෝන් එකට එරෙහිව තබන්න.


![TAPSIGNER NUNCHUK](assets/notext/10.webp)


Če je vaš Tapsigner nov, bo Nunchuk ponudil, da ga inicializira. Kliknite na "*Da*".


![TAPSIGNER NUNCHUK](assets/notext/11.webp)


ඔබ දැන් ඔබේ generate ඔබේ මාස්ටර් සංකේත කේතය තෝරා ගත යුතුය.


Tapsigner BIP32 ප්‍රමිතිය භාවිතා කරයි. මෙය ඔබේ බිට්කොයින් ආරක්ෂා කරන ඔබේ සංකේතාත්මක යතුරු ව්‍යුත්පන්න කිරීම Mnemonic වාක්‍යයක (BIP39 පසුම්බි වැනි) මත රඳා නොසිට, මහාචාර්ය පෞද්ගලික යතුර සහ මහාචාර්ය දාම කේතය මත සෘජුවම රඳා පවතින බව අර්ථ දක්වයි. මෙම Elements දෙක HMAC කාර්යය හරහා ගෙන යාමෙන් ඔබේ Wallet ඉතිරි කොටස නියමිතව සහ පරිමාණාත්මකව ව්‍යුත්පන්න කරයි.


මාස්ටර් පෞද්ගලික යතුර ඔබේ Tapsigner හි ඒකාබද්ධ TRNG (*සැබෑ අහඹු සංඛ්‍යා ජනකය*) මඟින් සෘජුවම ජනනය වේ. අනෙක් අතට, මාස්ටර් සංකේත සංකේතය පිටතින් ලබා දිය යුතුය. මෙම පියවරේදී, ඔබට තේරීමක් ඇත: "*Automatic*" මත ක්ලික් කිරීමෙන් එය ස්වයංක්‍රීයව Nunchuk generate කිරීමට ඉඩ දෙන්න, හෝ "*Advanced*" තෝරා එය ලබා දී ඇති ක්ෂේත්‍රයේ ඇතුළත් කිරීමෙන් generate ඔබම කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/12.webp)


ඊළඟට, ඔබට PIN කේතයක් තෝරා ගත යුතුය. "*Starting PIN*" ප්‍රදේශයේ, ඔබේ Tapsigner හි පිටුපස ලිය ඇති PIN කේතය ඇතුළත් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/13.webp)


ඔබේ Tapsigner එකට භෞතික ප්‍රවේශය ආරක්ෂා කිරීමට PIN කේතයක් තෝරන්න. මෙම PIN කේතය Wallet ප්‍රතිසාධන ක්‍රියාවලියට කිසිදු භූමිකාවක් නොවෙයි. එහි එකම කාර්යය වන්නේ ගනුදෙනු අත්සන් කිරීමට ඔබේ Tapsigner එක අගුළු ඇරීමයි. එය අමතක නොකරන ලෙස මෙම PIN කේතය සුරකින්න. "*Continue*" මත ක්ලික් කර ඉදිරියට යන්න.


![TAPSIGNER NUNCHUK](assets/notext/14.webp)

ඔබේ Tapsigner කාඩ්පත දැන් ආරම්භ කිරීමට ඔබේ දුරකථනයේ පිටුපස තබන්න.

![TAPSIGNER NUNCHUK](assets/notext/15.webp)


Nunchuk nato generate obnovitveno datoteko za vaš Wallet, kar vam omogoča, da ponovno pridobite dostop do svojih bitcoinov v primeru, da izgubite svojo NFC kartico. Ta datoteka je šifrirana z varnostno kodo, napisano na zadnji strani vašega Tapsignerja. Za obnovitev vaših bitcoinov boste nujno potrebovali to datoteko in kodo za njeno dešifriranje. Zato je pomembno, da naredite papirnato kopijo te kode, saj bo dostop do te kode izgubljen, če izgubite svojo NFC kartico, ker je trenutno napisana samo na kartici. Poskrbite tudi za ustvarjanje več varnostnih kopij vaše šifrirane obnovitvene datoteke.


![TAPSIGNER NUNCHUK](assets/notext/16.webp)


Wallet සඳහා නමක් තෝරන්න.


![TAPSIGNER NUNCHUK](assets/notext/17.webp)


ඔබේ Wallet හි පදනම දැන් සකසා ඇත. ඔබේ Tapsigner හි සත්‍යතාවය සනාථ කිරීමට, ඕනෑම වේලාවක, "*Run health check*" බොත්තම ක්ලික් කළ හැක.


![TAPSIGNER NUNCHUK](assets/notext/18.webp)


ඔබේ PIN අංකය ඇතුළත් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/19.webp)


Potem postavite svojo kartico na zadnjo stran telefona.


![TAPSIGNER NUNCHUK](assets/notext/20.webp)


## Kako ustvariti Wallet na Tapsignerju?


Nunchuk මුල් පිටුවට ආපසු ගිය විට, ඔබේ Tapsigner ලියාපදිංචි වී ඇති බව ඔබට ලබා ගත හැකි අත්සන් කිරීමේ උපාංගවල දැකිය හැක.


![TAPSIGNER NUNCHUK](assets/notext/21.webp)


Zdaj boste morali generate ključe za vaš Bitcoin Wallet. To naredite tako, da kliknete na gumb "*+*" desno od zavihka "*Wallets*".


![TAPSIGNER NUNCHUK](assets/notext/22.webp)


"Wallet නවයක් සෑදීම" මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/23.webp)


Potem izberite možnost "*Ustvari nov Wallet z uporabo obstoječih ključev*".


![TAPSIGNER NUNCHUK](assets/notext/24.webp)


Wallet සඳහා නමක් තෝරා "*Continue*" මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/25.webp)


ඔබේ Tapsigner තෝරාගෙන මෙම නව යතුරු කට්ටලය සඳහා අත්සන් කිරීමේ උපාංගය ලෙස තෝරන්න, එවිට "*Continue*" මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/26.webp)


če je vse po vašem zadovoljstvu, potrdite ustvarjanje.


![TAPSIGNER NUNCHUK](assets/notext/27.webp)

ඔබට පසුව ඔබේ Wallet හි වින්‍යාස ගොනුව සුරකින්න පුළුවන්. මෙම ගොනුවේ ඇතුළත් වන්නේ විශේෂයෙන්ම ඔබේ මහජන යතුරු පමණක් වන අතර, කවුරුන් හෝ එය ප්‍රවේශ වුවහොත්, ඔවුන්ට ඔබේ බිට්කොයින් සොරාගත නොහැක. කෙසේ වෙතත්, ඔවුන්ට ඔබේ සියලුම ගනුදෙනු අනුගමනය කළ හැක. එබැවින්, මෙම ගොනුව ඔබේ පෞද්ගලිකත්වයට පමණක් අවදානමක් ඉදිරිපත් කරයි. සමහර අවස්ථාවල, ඔබේ Wallet නැවත ලබා ගැනීමට අත්‍යවශ්‍ය විය හැක.

![TAPSIGNER NUNCHUK](assets/notext/28.webp)


අහින්සකව, ඔබේ Wallet සාර්ථකව නිර්මාණය කර ඇත!


![TAPSIGNER NUNCHUK](assets/notext/29.webp)


ඔබේ Tapsigner භාවිතා නොකරන විට, අනුමත නොකළ කියවීම් වලින් ආරක්ෂා කිරීමට රේඩියෝ තරංග අවහිර කරන Coinkite විසින් සපයන කේස් එකේ එය ගබඩා කිරීමට මතක තබා ගන්න.


## Kako prejeti bitcoine na Tapsigner?


බිට්කොයින් ලබා ගැනීමට, ඔබේ Wallet මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/30.webp)


එවිට නිපදවන ලද Address භාවිතා කර බිට්කොයින් ලබා ගන්න. ඔබ පෙර මෙම Wallet මත බිට්කොයින් ලබාගෙන ඇත්නම්, නව හිස් ලැබීමේ Addressක් generate කිරීමට "*Receive*" බොත්තම ක්ලික් කළ යුතුය.


![TAPSIGNER NUNCHUK](assets/notext/31.webp)


එක් වරක් යවන්නාගේ ගනුදෙනුව විකාශය කළ විට, ඔබේ Wallet මත එය පෙනේ.


![TAPSIGNER NUNCHUK](assets/notext/32.webp)


කොටස "*කාසි බලන්න*" මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/33.webp)


ඔබේ නව UTXO තෝරන්න.


![TAPSIGNER NUNCHUK](assets/notext/34.webp)


"*Tags*" අසල "*+*" මත ක්ලික් කර ඔබේ UTXO ට ලේබලයක් එක් කරන්න. මෙය හොඳ පුරුද්දක් වන අතර, එය ඔබේ නානය මූලය මතක තබා ගැනීමට සහ අනාගත වියදම් සඳහා ඔබේ පෞද්ගලිකත්වය උපරිම කිරීමට උපකාරී වේ.


![TAPSIGNER NUNCHUK](assets/notext/35.webp)


පවතින ටැගයක් තෝරන්න හෝ නවයක් සාදන්න, එවිට "*සුරකින්න*" මත ක්ලික් කරන්න. ඔබට ඔබේ කාසි වඩාත් සංවිධානාත්මක ආකාරයකින් සකස් කිරීමට "*එකතුවක්*" සාදන විකල්පයද ඇත.


![TAPSIGNER NUNCHUK](assets/notext/36.webp)


## Kako poslati bitcoine z uporabo Tapsignerja?


Zdaj, ko imate bitcoine v svojem Wallet, jih lahko tudi pošljete. Če želite to narediti, kliknite na izbrani Wallet.


![TAPSIGNER NUNCHUK](assets/notext/37.webp)


"*යවන්න*" බොත්තම මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/38.webp)


රැකියාව සඳහා මුදල තෝරන්න, එවිට "*Continue*" මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/39.webp)


ඔබේ අනාගත ගනුදෙනුවට එහි අරමුණ මතක තබා ගැනීමට "*සටහන*" එකතු කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/40.webp)

ඊළඟට, නියමිත ක්ෂේත්‍රයේ ලාභලාභියාගේ Address අතින් ඇතුළත් කරන්න.

![TAPSIGNER NUNCHUK](assets/notext/41.webp)


Na vrhu desne strani zaslona lahko kliknete na ikono in skenirate QR kodo, kodirano z Address.


![TAPSIGNER NUNCHUK](assets/notext/42.webp)


"*"*ගනුදෙනුව නිර්මාණය කරන්න*"* බොත්තම මත ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/43.webp)


තැපැල් යැවීමේ විස්තර සනාථ කර, එවිට ඔබේ Tapsigner අසල ඇති "*Sign*" බොත්තම ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/44.webp)


ඔබේ PIN අංකය ඇතුළත් කර එය අගුළු විවෘත කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/45.webp)


පසුව Tapsigner ඔබේ ස්මාර්ට්ෆෝනයේ පිටුපස තබන්න.


![TAPSIGNER NUNCHUK](assets/notext/46.webp)


ඔබේ ගනුදෙනුව දැන් අත්සන් කර ඇත. සියල්ල නිවැරදි බව අවසන් වරට පරීක්ෂා කර, එවිට "*Broadcast Transaction*" මත ක්ලික් කර Bitcoin ජාලය මත එය විකාශය කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/47.webp)


ඔබේ ගනුදෙනුව දැන් තහවුරු කිරීම සඳහා බලාපොරොත්තු වේ.


![TAPSIGNER NUNCHUK](assets/notext/48.webp)


## Wallet ටැප්සයිනර් අහිමි වූ විට එය නැවත ලබා ගැනීමේ ක්‍රමය කෙසේද?


ඔබේ Tapsigner එක අහිමි වී ඇත්නම්, කාඩ්පතේ පිටුපස සටහන් කර ඇති කේතය භාවිතයෙන් ඔබේ Wallet නැවත ලබා ගත හැක. එබැවින් මෙම කේතය Tapsigner එකෙන් වෙනම සුරැකීම වැදගත් වේ, මන්ද කාඩ්පත අහිමි වුවහොත්, මෙම කේතය වෙත ප්‍රවේශය ද අහිමි වනු ඇත. ඔබට Wallet හි සංකේතිත උපස්ථය ද අවශ්‍ය වනු ඇත.


Za obnovitev bomo uporabili aplikacijo Nunchuk, vendar imejte v mislih, da to pomeni začasno zavarovanje vaših sredstev v Hot Wallet. Če je vaš Tapsigner zavaroval večje zneske, razmislite o sledenju istemu postopku obnove z novim Coldcard namesto tega.


Nunchuk යෙදුම විවෘත කර "*Keys*" ටැබය අසල ඇති "*+*" බොත්තම ක්ලික් කරන්න.


![TAPSIGNER NUNCHUK](assets/notext/49.webp)


"*NFC යතුර එකතු කරන්න*" තෝරන්න.


![TAPSIGNER NUNCHUK](assets/notext/50.webp)


"*"TAPSIGNER යතුර zábackup එකෙන් නැවත ලබා ගන්න*" යන්න තෝරන්න.


![TAPSIGNER NUNCHUK](assets/notext/51.webp)


ඔබට පසුව ඔබේ උපාංගයේ ගොනු විමසුම්කරු වෙත යළියොමුවනු ඇත. ඔබේ Wallet හි සංකේතනය කළ උපස්ථ ගොනුව සොයා තෝරන්න. සාමාන්‍යයෙන්, මෙම ගොනුවේ නම `backup...` ලෙස ආරම්භ වේ.


![TAPSIGNER NUNCHUK](assets/notext/52.webp)


ආපසු ගොනුව විකේතනය කරන මුරපදය ඇතුළත් කරන්න. මෙම මුරපදය මුලින්ම ඔබේ Tapsigner හි පිටුපස සටහන් කළ එකට අනුකූල වේ.


![TAPSIGNER NUNCHUK](assets/notext/53.webp)

Potem izberite ime za svoje okrevanje Wallet.

![TAPSIGNER NUNCHUK](assets/notext/54.webp)


You have now regained access to your bitcoins. Your Wallet is now managed as a Hot Wallet visible in the "*Keys*" tab of the Nunchuk app. Next, you need to create a new set of cryptographic keys in the "*Wallets*" section by associating this key with it. To do this, you can follow the steps again in the "*How to create a Wallet on a Tapsigner?*" part of this tutorial.


![TAPSIGNER NUNCHUK](assets/notext/55.webp)


ඔබේ Tapsigner එක අහිමි වී ඇත්නම්, ඔබ සතු වෙනත් Wallet එකකට, ඉතාමත් සුදුසු ලෙස Hardware Wallet එකකින් ආරක්ෂා කරමින්, ඔබේ බිට්කොයින් වහාම මාරු කරන ලෙස මම දැඩිව උපදෙස් දෙමි. ඇත්ත වශයෙන්ම, ඔබ අහිමි කළ Tapsigner එක වැරදි අතට පත්වී ඇති හැකියාවක් ඇත. එබැවින් ඔබ නවතම ලබා ගත් Wallet එක හිස් කිරීම සහ එය භාවිතා කිරීම නවතා දැමීම වැදගත් වේ.


සුභ පැතුම්, ඔබ දැන් Tapsigner භාවිතා කිරීමේ වේගය වැඩි කර ඇත! ඔබට මෙම උපකාරකය ප්‍රයෝජනවත් වූවා නම්, පහත අඟුල් ලකුණක් තැබීමට මම ස්තූතිවන්ත වෙමි. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තූතියි!