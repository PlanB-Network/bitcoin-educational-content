---
name: Authy 2FA
description: 2FA යෙදුමක් භාවිතා කරන ආකාරය?
---
![cover](assets/cover.webp)


අද වන විට, දෙකේ-සාධක සත්‍යාපනය (2FA) අධිකාරිය නොමැති ප්‍රවේශය මගින් ඔන්ලයින් ගිණුම් ආරක්ෂා කිරීමේ ආරක්ෂාව වැඩි දියුණු කිරීම සඳහා අත්‍යවශ්‍ය වී ඇත. සයිබර් ප්‍රහාර වැඩිවීමත් සමඟ, ඔබේ ගිණුම් ආරක්ෂා කිරීමට පමණක් මුරපදයක් මත විශ්වාස කිරීම සමහර විට ප්‍රමාණවත් නොවේ. 2FA මුරපදයට අමතරව දෙවන සත්‍යාපන ආකාරයක් අවශ්‍ය කිරීමෙන් අමතර Layer ආරක්ෂාවක් හඳුන්වා දෙයි. මෙම සත්‍යාපනය SMS මගින් යවන කේතයක්, කැපවූ යෙදුමක් මගින් ජනනය කරන ගතික කේතයක්, හෝ භෞතික ආරක්ෂක යතුරක් භාවිතා කිරීම වැනි විවිධ ආකාර ගත හැක. 2FA භාවිතය, ඔබේ මුරපදය සොරා ගැනීමේ අවස්ථාවකදී පවා, ඔබේ ගිණුම් අවභාවිතා වීමේ අවදානම දැඩි ලෙස අඩු කරයි.


## 2FA preko aplikacij za preverjanje pristnosti


V drugih vadnicah bomo raziskali druge rešitve, kot so fizični varnostni ključi, vendar v tej predlagam, da se posebej osredotočimo na aplikacije za 2FA. Delovanje teh aplikacij je precej preprosto: ko je 2FA aktiviran na računu, boste ob vsakem prijavljanju morali vnesti ne le svoje običajno geslo, temveč tudi 6-mestno kodo. To kodo ustvari vaša aplikacija za 2FA. Pomembna značilnost te 6-mestne kode je, da ni statična; nova koda se ustvari v aplikaciji vsakih 30 sekund.

![AUTHY 2FA](assets/notext/01.webp)

කේතය සෑම තත්පර 30 කට වරක් නවීකරණය කිරීම මගින් ආක්‍රමණකරුට ඔබේ ගිණුමට ප්‍රවේශ වීම ඉතා දුෂ්කර වේ. මෙම පද්ධතිය ආක්‍රමණකරුවන්ට සොරාගත් හෝ අල්ලාගත් කේතයක් නැවත භාවිතා කිරීම වැළැක්වයි, මන්ද එය ඉක්මනින් කල් ඉකුත් වේ. එබැවින්, ආක්‍රමණකරුට කේතය ලබා ගැනීමට හැකි වුවහොත්, නව කේතයක් අවශ්‍ය වන තෙක් ඉතා කෙටි කාල පරාසයකදී පමණක් එය භාවිතා කළ හැක. තවද, කේතය මෙතරම් නිතර වෙනස් වීම මගින් කේතය බිඳ හෙලීම සඳහා බලහත්කාරීව අනුමාන කිරීමට උත්සාහ කරන හෑකර්වරයෙකුට ලබා ගත හැකි කාලය දැඩි ලෙස අඩු කරයි.


ආධාරක යෙදුම් හරහා 2FA එසේම ඔබේ මාර්ගගත ගිණුම්වල ආරක්ෂාව සුවිශේෂී ලෙස වැඩි දියුණු කිරීමට පහසුවෙන් භාවිතා කළ හැකි සහ නොමිලේ ක්‍රමයක් නියෝජනය කරයි.


2FA සකස් කිරීම සඳහා බොහෝ යෙදුම් ඇත, ඒ අතර Google Authenticator සහ Microsoft Authenticator වඩාත් ප්‍රසිද්ධය. කෙසේ වෙතත්, මෙම උපකාරිකාවේදී, මම ඔබට අඩු ප්‍රසිද්ධියක් ඇති වෙනත් විසඳුමක් වන Authy හඳුන්වා දීමට කැමතියි. මෙම සියලුම යෙදුම් TOTP (*Time based One Time Password*) ප්‍රොටෝකෝලය භාවිතා කරමින් ක්‍රියාත්මක වන අතර, ඒවා භාවිතා කිරීම සමාන වේ.

Authy විශාල තාක්ෂණ සමාගම් වලින් ලබා දෙන අනෙකුත් විසඳුම්වලට වඩා කිහිපයක් වාසි ලබා දේ. ප්‍රධාන වශයෙන්ම, එය ඔබට ඔබේ 2FA ටෝකන බහු උපාංග හරහා සංකේතනය කිරීමට ඉඩ සලසයි, එය දුරකථනය අහිමි වීමේ හෝ වෙනස් කිරීමේ අවස්ථාවකදී ප්‍රයෝජනවත් විය හැක. Authy ඔබට generate සංකේතිත උපස්ථයක් සකසා එය මාර්ගගතව ගබඩා කිරීමටද ඉඩ සලසයි, එය ඔබේ ප්‍රාථමික උපාංගය අහිමි වුවහොත් පවා ඔබේ ටෝකන වෙත ප්‍රවේශය අහිමි නොවන බව සහතික කරයි. පරිශීලක Interface දෘෂ්ටිකෝණයෙන්, මම පුද්ගලිකව සොයා ගන්නේ Authy එහි විකල්පවලට වඩා වඩාත් සතුටුදායක සහ අත්භූත අත්දැකීමක් ලබා දෙන බවයි.


## Kako namestiti Authy?


Na svojem pametnem telefonu pojdite v trgovino z aplikacijami (Google Play Store ali Apple Store) in poiščite "*Twilio Authy Authenticator*".



- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)

![AUTHY 2FA](assets/notext/02.webp)

යෙදුම පළමු වරට ආරම්භ කිරීමේදී, ඔබට ගිණුමක් සාදන්න අවශ්‍ය වේ. ඔබේ රටේ අමතර අංක කේතය, මෙන්ම ඔබේ දුරකථන අංකය තෝරන්න, එවිට "*Submit*" මත ක්ලික් කරන්න.

![AUTHY 2FA](assets/notext/03.webp)

ඔබේ විද්‍යුත් තැපෑල් Address ඇතුළත් කර කේතය ප්‍රතිසාධනය කරන්න.

![AUTHY 2FA](assets/notext/04.webp)

ඉ-තැපෑලක් ඔබට එවනු ලැබේ ඔබේ Address සත්‍යාපනය කිරීමට. තහවුරු කිරීමට ලැබුණු අංක 6 ඇතුළත් කරන්න.

![AUTHY 2FA](assets/notext/05.webp)

ඔබේ දුරකථන අංකය සනාථ කිරීමට ලබා ගත හැකි ක්‍රම දෙකෙන් එකක් තෝරන්න. ඔබ SMS ලැබීම සඳහා තෝරා ගන්නේ නම්, ඔබේ අංකය සනාථ කිරීමට පණිවිඩය මඟින් ලැබෙන අංක 6ක කේතය ඇතුළත් කරන්න.

![AUTHY 2FA](assets/notext/06.webp)

චිත්‍රපට, ඔබේ Authy ගිණුම නිර්මාණය කර ඇත!

![AUTHY 2FA](assets/notext/07.webp)

## Authy කෙසේ වින්‍යාස කරන්නේද?


Za začetek pojdite v nastavitve aplikacije s klikom na tri majhne pike, ki se nahajajo v zgornjem desnem kotu zaslona.

![AUTHY 2FA](assets/notext/08.webp)

පසුව "*Settings*" මත ක්ලික් කරන්න.

![AUTHY 2FA](assets/notext/09.webp)

"*My Account*" ටැබ් තුළ, ඔබට ඔබේ ගිණුම වෙනස් කිරීමට විකල්පයක් ඇත. "*App Protection*" තේරීමෙන් යෙදුමට PIN කේතයක් එක් කිරීමට මම නිර්දේශ කරමි. මෙය ඔබේ යෙදුමට ප්‍රවේශ වීමට අමතර Layer ආරක්ෂාවක් එක් කරයි.

![AUTHY 2FA](assets/notext/10.webp)

"*ගිණුම්*" ටැබ් එකේ, ඔබට ඔබේ ටෝකන සඳහා ආපසු සුරැකුමක් සකස් කළ හැක. මෙම ආපසු සුරැකුම, ගැටළුවක් ඇති වූ විට ඔබේ කේතයන් ප්‍රතිසාධනය කිරීමට ඉඩ සලසයි. එය ඔබ අර්ථ දක්වන මුරපදයක් භාවිතයෙන් සංකේතනය කර ඇත. මෙම මුරපදය ශක්තිමත් සහ ආරක්ෂිත ස්ථානයක තබා ගැනීම වැදගත් වේ. ඔබට, උදාහරණයක් ලෙස, ඒකාකාර Authy ගිණුමක් සහිත දෙවන උපාංගයක් වැනි වෙනත් ප්‍රතිසාධන ක්‍රම තිබේ නම්, මෙම ආපසු සුරැකුම සකස් කිරීම අනිවාර්ය නොවිය හැක.

![AUTHY 2FA](assets/notext/11.webp)In the "*Devices*" tab, you can see all the devices synchronized with your Authy account. You have the option to disable the use of multiple devices, which restricts access to your account to that device only. If you use only one device, this can increase the security of your account, but make sure you have another backup method in case you lose that device.


ඔබට වෙනත් උපාංග එකතු කිරීම ඉඩ දීමට කැමති නම්, නව උපාංගයක් එකතු කිරීමට පෙර ඔබේ Authy ගිණුමේ දැනට අනුමත කළ උපාංගවලින් තහවුරු කිරීම අවශ්‍ය කරන විකල්පය සක්‍රීය කිරීමට මම ඔබට උපදෙස් දෙමි.

![AUTHY 2FA](assets/notext/12.webp)

නව උපාංගයක් එක් කිරීමට, පෙර කොටසේ ඉදිරිපත් කළ ස්ථාපන ක්‍රියාවලිය එම අයදුම්පත් භාවිතා කරමින් නැවත සිදු කරන්න. එවිට ඔබේ ප්‍රධාන උපාංගයෙන් මෙම නව ප්‍රවේශය තහවුරු කරන ලෙස ඔබගෙන් ඉල්ලා සිටිනු ඇත.


## Kako nastaviti 2FA na računu?


ඇකවුන්ට් එකක Authy වැනි යෙදුමක් හරහා 2FA සත්‍යාපන කේතයක් සකසන්න, එම ඇකවුන්ට් එක මෙම විශේෂාංගය සහය දක්වන්නට තිබිය යුතුය. අද කාලේ, බොහෝමයක් මාර්ගගත සේවා මෙම 2FA විකල්පය ලබා දෙන නමුත්, මෙය සෑම විටම එසේ නොවේ. මම වෙනත් උපකාරකයකදී ඉදිරිපත් කළ Proton mail ගිණුම උදාහරණයක් ලෙස ගනිමු:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)

Na splošno boste to možnost 2FA našli v nastavitvah svojega računa, pogosto pod razdelkom "*Geslo*" ali "*Varnost*".

![AUTHY 2FA](assets/notext/14.webp)

ඔබේ Proton තැපැල් ගිණුම මත මෙම විකල්පය සක්‍රීය කරන විට, ඔබට QR කේතයක් ඉදිරිපත් කෙරේ. එවිට ඔබේ Authy යෙදුම සමඟ මෙම QR කේතය ස්කෑන් කළ යුතුය.

![AUTHY 2FA](assets/notext/15.webp)

Authy මත, "*+*" බොත්තම ක්ලික් කරන්න.

![AUTHY 2FA](assets/notext/16.webp)

"*QR කේතය ස්කෑන් කරන්න*" මත ක්ලික් කරන්න. එවිට වෙබ් අඩවියේ QR කේතය ස්කෑන් කරන්න.

![AUTHY 2FA](assets/notext/17.webp)

ඔබට අවශ්‍ය නම් ඔබේ පරිශීලක නාමය සකසන්නද හැකිය. වෙනස්කම් සිදු කිරීමෙන් පසු, "*SAVE*" බොත්තම ක්ලික් කරන්න.

![AUTHY 2FA](assets/notext/18.webp)

Authy nato prikaže vašo dinamično 6-mestno kodo, specifično za ta račun, ki se osveži vsakih 30 sekund.

![AUTHY 2FA](assets/notext/19.webp)

මෙම කේතය වෙබ් අඩවියේ ඇතුළත් කර 2FA පිහිටුවීම අවසන් කරන්න.

![AUTHY 2FA](assets/notext/20.webp)

කීප වෙබ් අඩවි 2FA සක්‍රීය කිරීමෙන් පසු ඔබට ප්‍රතිසාධන කේත ලබා දෙනු ඇත. මෙම කේත ඔබේ Authy යෙදුමට ප්‍රවේශය අහිමි වූ විට ඔබේ ගිණුමට ප්‍රවේශ වීමට ඉඩ සලසයි. මම එය ආරක්ෂිත ස්ථානයක සුරැකීමට නිර්දේශ කරමි.

![AUTHY 2FA](assets/notext/21.webp)Your account is now secured with two-factor authentication via the Authy app.

![AUTHY 2FA](assets/notext/22.webp)

හරියටම Authy මගින් ජනනය කරන ගතික කේතය සපයන්න, ඔබ ගිණුමට ප්‍රවේශ වීමේදී සෑම වරකම අවශ්‍ය වේ. දැන් මෙම 2FA ක්‍රමයට අනුකූල සියලුම ගිණුම් ආරක්ෂා කළ හැක. Authy මත නව ගිණුමක් එක් කිරීමට, යෙදුමේ ඉහළ දකුණු කෙළවරේ ඇති කුඩා ලප 3 ක් මත ක්ලික් කරන්න.

![AUTHY 2FA](assets/notext/23.webp)

පසුව "*Add Account*" මත ක්ලික් කරන්න.

![AUTHY 2FA](assets/notext/24.webp)

පළමු ගිණුම සඳහා භාවිතා කළ ඒම පියවර අනුගමනය කරන්න. ඔබේ විවිධ ගතික කේත Authy මුල් පිටුවේ දෘශ්‍යමාන වේ.