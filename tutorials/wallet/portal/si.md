---
name: පෝර්ටල්
description: TwentyTwo-Devices Hardware Wallet Portal සකසමින් සහ භාවිතා කිරීම
---
![cover](assets/cover.webp)


Portal යනු TwentyTwo Devices විසින් නිර්මාණය කරන ලද Bitcoin Hardware Wallet වේ, බිට්කොයින් භාවිතා කරන්නන් සඳහා විවෘත මූලාශ්‍ර දෘඩාංග පසුම්බි නිර්මාණය කිරීමේ විශේෂඥ සමාගමකි. Magical Bitcoin ව්‍යාපෘතිය ([ඉදිරියට BDK ලෙස නම් කරන ලදී](https://github.com/bitcoindevkit)) නිර්මාතෘ Alekos Filini විසින් ආරම්භ කරන ලද අතර Blockstream සහ BHB Network සඳහා වැඩ කර ඇති TwentyTwo Devices, පරිශීලක ස්වයංපෝෂිතභාවය, සරලභාවය සහ ආරක්ෂාව මත අවධානය යොමු කිරීමට අරමුණු කරයි.


Portal-ය වෙනත් දෘඩාංග පසුම්බි වලින් වෙනස් කරන්නේ එහි ස්වභාවික ස්මාර්ට්ෆෝන් ඒකාබද්ධතාවයයි. එය කේබල් හෝ බැටරි නැතිව ක්‍රියා කරයි. එය තමන්ට බලය ලබා ගැනීමට සහ ඕනෑම අනුකූල ජංගම Wallet සමඟ සන්නිවේදනය කිරීමට NFC තාක්ෂණය භාවිතා කරයි. එහි ආකර්ෂණීය නිර්මාණය ආරෝග්‍යමය භාවිතය සඳහා සංකල්පිත වේ. වටකුරු කොටස ස්මාර්ට්ෆෝනයේ පිටුපස තබා, ඔබේ ගනුදෙනු වල විස්තර පරීක්ෂා කිරීම සඳහා තිරයක් හෙළි කරයි, එමගින් විශේෂිත බොත්තම සමඟ ඒවා අත්සන් කිරීමේ හැකියාව ලබා දේ.


![Image](assets/fr/01.webp)


සම්පූර්ණයෙන්ම විවෘත මූලාශ්‍ර, Portal යන්ත්‍රාංගය Rust හි ලියන ලද ෆර්ම්වේර් මත පදනම්ව ඇති අතර යතුරු සහ ගනුදෙනු කළමනාකරණය සඳහා BDK (Bitcoin Dev Kit) භාවිතා කරයි. එය €89 කට [නිල වෙබ් අඩවියේ](https://store.twenty-two.xyz/products/portal-hardware-Wallet) විකිණේ.


Lekha likhane ke samay, Portal Nunchuk aur Bitcoin Keeper applications ke saath compatible hai. Is tutorial mein, hum ise Nunchuk ke saath configure karenge.


## Unboxing


ඔබේ Portal එක ලැබුණු විට, පෙට්ටිය සහ එය සීල් කර ඇති ලේබලය හොඳ තත්ත්වයේ පවතින බව පරීක්ෂා කරන්න. ඇතුළත, ඔබේ Portal එක සීල් කළ කවරයකින් සපයා ඇත.


සැතින් Seal අඛණ්ඩ බව සහතික කර, කවරය විවෘත කර නොමැති බව තහවුරු කරන්න. කවරය මත විශාල අකුරින් පෙන්වා ඇති අනන්‍ය අංකය නිල් Seal යට කළු පැහැයෙන් ලියා ඇති අංකයට, පෙට්ටියේ ලේබලය මත ඇති අංකයට, සහ ඔබ පළමුවරට ආරම්භ කරන විට ඔබේ තිරය මත පෙනෙන අංකයට අනුකූල විය යුතුය.


![Image](assets/fr/02.webp)


## Nunchuk ස්ථාපනය


Wallet පෝර්ටලය මත සත්කාරක Wallet කළමනාකරණය කිරීමට, අපි Nunchuk යෙදුම භාවිතා කිරීමට යනවා. යෙදුම [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) හෝ එහි [`.apk` ගොනුව](https://github.com/nunchuk-io/nunchuk-android/releases) හරහා සෘජුවම බාගන්න.


![Image](assets/fr/03.webp)


ඔබ Nunchuk පළමු වරට භාවිතා කරන්නේ නම්, යෙදුම ඔබට ගිණුමක් සාදන්න කියා ඉල්ලා සිටී. මෙම උපකාරකය සඳහා, එකක් සාදන අවශ්‍යතාවයක් නොමැත. ගිණුමකින් තොරව දිගටම යාමට "*අමුත්තා ලෙස දිගටම යන්න*" තෝරන්න.


![Image](assets/fr/04.webp)


## පෝර්ටල් වින්‍යාසය


Nunchuk මුල් තිරයේ, තිරයේ ඉහළින් ඇති "*NFC*" ලාංඡනය මත ක්ලික් කරන්න.


![Image](assets/fr/05.webp)


ඔබේ ස්මාර්ට්ෆෝන් එකේ පිටුපසට ඔබේ පෝර්ටලය තබා එය සක්‍රීය කරන්න.


![Image](assets/fr/06.webp)


Nunchuk ඔබේ Portal හඳුනා ගනු ඇත. එවිට "*Continue*" මත ක්ලික් කරන්න.


![Image](assets/fr/07.webp)


Za ustvarjanje novega Wallet izberite "*generate seed na Portalu*" in nato kliknite na "*Nadaljuj*".


![Image](assets/fr/08.webp)


Mnemonic වාක්‍යයක් සඳහා 12- හෝ 24- වචන අතරින් තෝරා ගත හැක. දෙකම සමාන ආරක්ෂාවක් ලබා දෙන බැවින්, සුරැකීමට පහසු එක, එනම් 12 වචන, තෝරා ගත හැක.


![Image](assets/fr/09.webp)


Potem boste pozvani, da izberete geslo. Geslo odklene vaš Portal. Zato zagotavlja zaščito pred nepooblaščenim fizičnim dostopom. To geslo ni vključeno v izpeljavo kriptografskih ključev vašega Wallet. Torej, tudi brez dostopa do tega gesla, vam bo posedovanje vaše 12- ali 24-besedne fraze Mnemonic omogočilo ponovno pridobitev dostopa do vaših bitcoinov. Priporočljivo je, da izberete geslo, ki je čim bolj naključno in dovolj dolgo. Poskrbite, da boste to geslo shranili na ločenem mestu od tistega, kjer je shranjen vaš Portal (npr. v upravitelju gesel).


![Image](assets/fr/10.webp)


ඔබේ Portal එක ඔබේ 12-වචන Mnemonic වාක්‍යය පෙන්වනු ඇත. මෙම Mnemonic ඔබට ඔබේ සියලුම බිට්කොයින් සඳහා සම්පූර්ණ, සීමාවන් රහිත ප්‍රවේශය ලබා දේ. මෙම වාක්‍යය අත්පත් කර ගන්නා ඕනෑම කෙනෙකුට, ඔබේ Portal එකට භෞතික ප්‍රවේශය නොමැතිව පවා, ඔබේ මුදල් සොරා ගත හැක.


12-වචන වාක්‍යය ඔබේ බිට්කොයින් නැතිවීම, සොරකම හෝ ඔබේ Portal කඩාවැටීමේ අවස්ථාවකදී ප්‍රවේශය නැවත ලබා දේ. එබැවින් එය සූක්ෂමව සුරැකීම සහ ආරක්ෂිත ස්ථානයක ගබඩා කිරීම ඉතා වැදගත් වේ.


ඔබට එය කඩදාසි කැබැල්ලක ලියන්න පුළුවන්, හෝ අමතර ආරක්ෂාව සඳහා, මම එය ගිනි, ගංවතුර හෝ කඩා වැටීමෙන් ආරක්ෂා කිරීම සඳහා මල නොබැඳෙන වානේ පදනමක කැටයම් කිරීම නිර්දේශ කරමි.


Mnemonic වාක්‍යය සුරැකීම සහ කළමනාකරණය කිරීමේ නිවැරදි ක්‍රමය පිළිබඳ වැඩි විස්තර සඳහා, විශේෂයෙන් ඔබ ආරම්භකයෙකු නම්, මෙම වෙනත් උපකාරකය අනුගමනය කිරීම මම ඉතාමත් නිර්දේශ කරමි:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**නැවතත්, ඔබ මෙම වචන අන්තර්ජාලයේ බෙදා හදා ගත යුතු නැත, මම මෙම උපකාරිකාවේ කරන පරිදි. මෙම සාම්පල Wallet භාවිතා කරන්නේ Testnet මත පමණක් වන අතර උපකාරිකාව අවසානයේදී මකා දමනු ඇත.**_


ඔබේ Portal මත ඇති බොත්තම තදින් ඔබා ඊළඟ වචන වෙත ගමන් කරන්න. අන්තර්ක්‍රියාව නිසි ලෙස හඳුනාගැනෙන ලෙස ඔබේ සම්පූර්ණ ඇඟිල්ල බොත්තම මත තබා සෙකන් කිහිපයක් පුරා පීඩනය තබා ගන්න.


![Image](assets/fr/11.webp)


ඔබේ Portal පසුව ඔබ Nunchuk හි ඇතුළත් කළ මුරපදය තහවුරු කරනු ඇත.


![Image](assets/fr/12.webp)


ඔබ දැන් ඔබේ Portal සකස් කිරීම සහ ඔබේ Mnemonic වාක්‍යය නිර්මාණය කිරීම අවසන් කර ඇත!


![Image](assets/fr/13.webp)


## Bitcoin Wallet කටයුතු සැකසීම


Nunchuk මත, "*Continue*" මත ක්ලික් කරන්න, තවමත් ඔබේ දුරකථනයේ පසුපසට ඔබේ Portal අල්ලාගෙන.


![Image](assets/fr/14.webp)


මෙම උපදෙස් මාලාවේ, මම තනි අත්සන Wallet සකසන අතර, එබැවින් මම මෙම විකල්පය තෝරමින් සිටිමි.


![Image](assets/fr/15.webp)


Wallet (අංක 0) හි පළමු ගිණුම, එනම් පෙරනිමි ගිණුම භාවිතා කරන්න. එවිට Nunchuk ඔබගෙන් එය අගුළු හරින ලෙස ඔබේ Portal මුරපදය තහවුරු කරන ලෙස ඉල්ලා සිටියි.


![Image](assets/fr/16.webp)


පෝර්ටලය මත, ඔබේ xpub Nunchuk වෙත අපනයනය කිරීම තහවුරු කරන්න. මෙය ඔබට Wallet ඔබේ ස්මාර්ට්ෆෝන් එකෙන් කළමනාකරණය කිරීමට ඉඩ සලසයි, පෝර්ටලය නොමැතිව බිට්කොයින් වියදම් කිරීමට නොහැකි වන අතර. තහවුරු කිරීමට බොත්තම ඔබන්න.


සටහන් කරන්න ඔබේ අවස්ථාවේ සඳහන් කරන ලද ව්‍යුත්පන්න මාර්ගය මගේ මාර්ගයෙන් වෙනස් වනු ඇත, මන්ද මෙම උපකාරක පංතිය Testnet මත ක්‍රියාත්මක වේ.


![Image](assets/fr/17.webp)


ඔබේ Wallet නමක් දක්වන්න, උදාහරණයක් ලෙස "*Portal*", එවිට "*Continue*" මත ක්ලික් කරන්න.


![Image](assets/fr/18.webp)


එවිට Nunchuk ඔබට ඔබේ විස්තරකරු ඉදිරිපත් කරයි. ආපසු පිටපතක් සෑදීම හොඳ අදහසකි. විස්තරකරුට ඔබට බිට්කොයින් වියදම් කිරීමට ඉඩ නොදෙන්නත්, එය Wallet ප්‍රතිසාධනයකදී ඔබේ Mnemonic වාක්‍යයෙන් ඔබේ යතුරු වල ව්‍යුහ මාර්ග හඹා යාමට ඉඩ දෙයි. එය ආරක්ෂිත ස්ථානයක තබා ගන්න, එහි කාන්දුව ආරක්ෂක ගැටලුවක් නොවිය හැකි නමුත්, එය රහස්‍යතා ගැටලුවක් නියෝජනය කරයි.


කලින් "*Done*" මත ක්ලික් කරන්න.


![Image](assets/fr/19.webp)


Zdaj boste morali generate javne ključe za vaš Bitcoin Wallet. Če želite to narediti, kliknite na gumb "*Ustvari nov Wallet*".


![Image](assets/fr/20.webp)


කළින් "*Create new Wallet*" මත නැවත ක්ලික් කරන්න. එවිට "*Create a new Wallet using existing keys*" විකල්පය තෝරන්න.


![Image](assets/fr/21.webp)


Wallet සඳහා නමක් තෝරන්න සහ "*Continue*" මත ක්ලික් කරන්න.


![Image](assets/fr/22.webp)


ඔබේ Portal තෝරන්න මෙම නව යතුරු කට්ටලය සඳහා අත්සන් කිරීමේ උපාංගය ලෙස, එවිට "*Continue*" මත ක්ලික් කරන්න.


![Image](assets/fr/23.webp)


Če je vse po vašem zadovoljstvu, potrdite ustvarjanje.


![Image](assets/fr/24.webp)


ඔබට පසුව ඔබේ Wallet වින්‍යාස ගොනුව සුරකින්න පුළුවන්. මෙම ගොනුවේ අඩංගු වන්නේ ඔබේ මහජන යතුරු පමණක් වන අතර, කවුරුන් හෝ එය ප්‍රවේශ වුවහොත්, ඔවුන්ට ඔබේ බිට්කොයින් සොරා ගැනීමට නොහැකි වනු ඇත. කෙසේ වෙතත්, ඔවුන්ට ඔබේ සියලුම ගනුදෙනු හඹා යාමට හැකි වනු ඇත. එබැවින් මෙම ගොනුව ඔබේ පෞද්ගලිකත්වයට පමණක් අවදානමක් ඉදිරිපත් කරයි. සමහර අවස්ථාවල, ඔබේ Wallet ප්‍රතිසාධනය කිරීම සඳහා අත්‍යවශ්‍ය විය හැක.


![Image](assets/fr/25.webp)


ඒ ගැන කියන්න තියෙන්නේ එතනින් ඉවරයි!


![Image](assets/fr/26.webp)


## Portal සමඟ බිට්කොයින් ලබා ගැනීමට මම කෙසේද?


බිට්කොයින් ලබා ගැනීමට, ඔබේ Wallet තෝරන්න.


![Image](assets/fr/27.webp)


Generated Address භාවිතා කිරීමට පෙර, එය Portal තිරය මත පරීක්ෂා කරන්න. මෙය කිරීමට, "*Receive*" මත ක්ලික් කරන්න.


![Image](assets/fr/28.webp)


තෙවන ලපුවල ක්ලික් කර, "*Address PORTAL හරහා සත්‍යාපනය කරන්න*" තෝරන්න. එවිට ඔබේ මුරපදය ඇතුළත් කරන්න.


![Image](assets/fr/29.webp)


ඔබේ දුරකථනයේ පිටුපස ඔබේ Portal තබා, පසුව බොත්තම ඔබා තහවුරු කරන්න.


![Image](assets/fr/30.webp)


පෝර්ටලයේ පෙන්වන Address ඔබේ Nunchuk හි ඇති එකට ගැලපෙන බව සහතික කර, පසුව නැවත බොත්තම ඔබන්න. ලිපින සමාන නම්, ඔබට මෙම Address ගෙවීම්කරුට ලබා දිය හැක.


![Image](assets/fr/31.webp)


එක් වර payerගේ ගනුදෙනුව විකාශය වීමෙන් පසු, ඔබේ Wallet මත එය පෙනෙනු ඇත.


![Image](assets/fr/32.webp)


කොණවල් "*බලන්න*" ක්ලික් කරන්න.


![Image](assets/fr/33.webp)


ඔබේ නව UTXO තෝරන්න.


![Image](assets/fr/34.webp)


"*Tags*" අසල "*+*" මත ක්ලික් කර ඔබේ UTXO ට ටැගයක් එක් කරන්න. මෙය හොඳ පුරුද්දක් වන අතර, එය ඔබේ කාසි කොතැනින් පැමිණියේද යන්න මතක තබා ගැනීමට සහ අනාගතයේ වියදම් කිරීමේදී ඔබේ පෞද්ගලිකත්වය උපරිම කිරීම සඳහා උපකාරී වේ.


![Image](assets/fr/35.webp)


දැනට පවතින ටැගයක් තෝරන්න හෝ නවයක් සාදන්න, එවිට "*Save*" මත ක්ලික් කරන්න. ඔබේ කොටස් වඩා සංවිධානාත්මක ආකාරයකින් සකස් කිරීමට "*collections*" ද සාදන්න පුළුවන්.


![Image](assets/fr/36.webp)


## Bitcoine Portal භාවිතයෙන් යැවීමට කෙසේද?


Zdaj, ko imate bitcoine v svojem Wallet, jih lahko tudi pošljete. Če želite to narediti, kliknite na izbrani Wallet.


![Image](assets/fr/37.webp)


"*Send*" බොත්තම මත ක්ලික් කරන්න.


![Image](assets/fr/38.webp)


මුදල තෝරා "*ඉදිරියට*" ක්ලික් කරන්න.


![Image](assets/fr/39.webp)


ඔබේ අනාගත ගනුදෙනුවට එහි අරමුණ මතක් කිරීමට "*සටහනක්*" එක් කරන්න.


![Image](assets/fr/40.webp)


පසුව ලබාගන්නා පුද්ගලයාගේ Address ලබා දී ඇති ක්ෂේත්‍රයේ ඇතුළත් කරන්න. ඔබට තිරයේ ඉහළ දකුණු කෙළවරේ ඇති අයිකනය ක්ලික් කිරීමෙන් QR කේතයක් ලෙස කේතගත කළ Address එකක්ද ස්කෑන් කළ හැක. පසුව "*Create Transaction*" බොත්තම ක්ලික් කරන්න.


![Image](assets/fr/41.webp)


ඔබේ ගනුදෙනු විස්තර පරීක්ෂා කර, එවිට ඔබේ පෝර්ටලය අසල ඇති "*සහයෝගය*" බොත්තම ක්ලික් කර, ඔබේ මුරපදය ඇතුළත් කරන්න.


![Image](assets/fr/42.webp)


ඔබේ දුරකථනයේ පිටුපසට ඔබේ Portal තබන්න. ලැබුම්කරුගේ Address සහ මුදල නිවැරදි බව පරීක්ෂා කරන්න. එසේ නම්, ඉදිරියට යාමට බොත්තම ඔබන්න.


![Image](assets/fr/43.webp)


පරිවර්තනය: ඔබේ ගනුදෙනුව අත්සන් කිරීමට, ගනුදෙනු ගාස්තුව නිවැරදි බව පරීක්ෂා කර, පසුව බොත්තම නැවත ඔබන්න.


![Image](assets/fr/44.webp)


ඔබේ ගනුදෙනුව අත්සන් කර ඇත. එහි විස්තර අවසන් වරට Nunchuk මත පරීක්ෂා කළ හැකි අතර, පසුව එය Bitcoin ජාලය මත විකාශය කිරීමට "*Broadcast transaction*" බොත්තම ක්ලික් කරන්න.


![Image](assets/fr/45.webp)


ඔබේ ගනුදෙනුව දැන් තහවුරු කිරීම සඳහා බලාපොරොත්තු වෙමින් පවතී.


![Image](assets/fr/46.webp)


චෙත්තිරිය, ඔබ දැන් Portal භාවිතා කිරීමේ හැකියාව ලබාගෙන ඇත! මෙම උපකාරකය ප්‍රයෝජනවත් වූවා නම්, Green අඟුලක් පහළින් දමා යන්න. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තුතියි!


වැඩිදුර තොරතුරු ලබා ගැනීමට, HD පසුම්බි කෙසේ ක්‍රියා කරන්නේද යන්න පිළිබඳව අපගේ සම්පූර්ණ පුහුණු පාඨමාලාව බලන්න:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f