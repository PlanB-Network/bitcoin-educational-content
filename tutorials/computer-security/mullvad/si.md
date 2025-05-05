---
name: Mullvad VPN
description: VPN බිට්කොයින් වලින් ගෙවා සකස් කිරීම
---
![cover](assets/cover.webp)


VPN ("*වර්චුවල් පෞද්ගලික ජාලය*") යනු ඔබේ දුරකථනය හෝ පරිගණකය සහ VPN සපයන්නෙකු විසින් කළමනාකරණය කරන දුරස්ථ සේවාදායකය අතර ආරක්ෂිත සහ සංකේතනය කළ සම්බන්ධතාවයක් ස්ථාපිත කරන සේවාවකි.


_tehnično gledano, ko se povežete z VPN, se vaš internetni promet preusmeri skozi šifriran tunel do strežnika VPN. Ta postopek otežuje tretjim osebam, kot so ponudniki internetnih storitev (ISP) ali zlonamerni akterji, prestrezanje ali branje vaših podatkov. Strežnik VPN nato deluje kot posrednik, ki se v vašem imenu poveže s storitvijo, ki jo želite uporabljati. Vaši povezavi dodeli nov IP Address, kar pomaga skriti vaš pravi IP Address pred spletnimi mesti, ki jih obiščete. Vendar pa, v nasprotju s tem, kar lahko nakazujejo nekateri spletni oglasi, uporaba VPN ne omogoča anonimnega brskanja po internetu, saj zahteva določeno stopnjo zaupanja v ponudnika VPN, ki lahko vidi ves vaš promet._

![MULLVAD VPN](assets/fr/01.webp)

VPN භාවිතා කිරීමේ වාසි ගණනාවක් ඇත. පළමුවෙන්ම, එය VPN සපයන්නා ඔබේ තොරතුරු බෙදා නොගන්නේ නම්, ISP හෝ රජයන්ගෙන් ඔබේ මාර්ගගත ක්‍රියාකාරකම්වල පෞද්ගලිකත්වය ආරක්ෂා කරයි. දෙවැනිව, එය ඔබේ දත්ත ආරක්ෂා කරයි, විශේෂයෙන්ම ඔබ MITM ("**man-in-the-middle**") ප්‍රහාර වලට බරපතල වන මහජන Wi-Fi ජාල වෙත සම්බන්ධ වූ විට. තෙවැනිව, ඔබේ IP Address සඟවා, VPN එකක් භූගෝලීය සීමා සහ සෙන්සර් කිරීම වටහා ගෙන, ඔබේ ප්‍රදේශයේ නොලැබෙන හෝ අවහිර කරන ලද අන්තර්ගතයට ප්‍රවේශ වීමට ඉඩ සලසයි.


Kot lahko vidite, VPN prenese tveganje opazovanja prometa na ponudnika VPN. Zato je pri izbiri ponudnika VPN pomembno upoštevati osebne podatke, ki so potrebni za registracijo. Če ponudnik zahteva informacije, kot so vaša telefonska številka, e-pošta Address, podatki o bančni kartici ali še huje, vaša poštna Address, se poveča tveganje povezovanja vaše identitete z vašim prometom. V primeru kompromisa ponudnika ali pravnega zasega bi bilo enostavno povezati vaš promet z vašimi osebnimi podatki. Zato je priporočljivo izbrati ponudnika, ki ne zahteva nobenih osebnih podatkov in sprejema anonimna plačila, na primer z bitcoini.


මෙම උපදෙස් මාලාවේ, මම සරල, කාර්යක්ෂම, සාධාරණ මිලකට ලබා ගත හැකි VPN විසඳුමක් ඉදිරිපත් කරන්නෙමි, එය භාවිතා කිරීමට කිසිදු පුද්ගලික තොරතුරු අවශ්‍ය නොවේ.


## Mullvad VPN සඳහා හැඳින්වීම

Mullvad VPN යනු ස්වීඩන් සේවාවක් වන අතර එය පරිශීලක පෞද්ගලිකත්වය සඳහා Commitment සඳහා විශේෂිත වේ. ප්‍රධාන ධාරා VPN සපයන්නන්ට වඩා වෙනස්ව, Mullvad ලියාපදිංචි වීමේදී කිසිදු පුද්ගලික දත්තයක් අවශ්‍ය නොවේ. විද්‍යුත් Address ලිපිනයක්, දුරකථන අංකයක්, හෝ නමක් ලබා දීමට අවශ්‍ය නොවේ; එහි වෙනුවට, Mullvad ඔබට ගෙවීම් සහ සේවාව ප්‍රවේශ වීම සඳහා භාවිතා කරන අනන්‍ය ගිණුම් අංකයක් පවරයි. අමතරව, Mullvad ඔවුන්ගේ සේවාදායකයන් හරහා ගමන් කරන කිසිදු ක්‍රියාකාරකම් ලඝු-ලේඛන තබා නොමැති බව පවසයි.

![MULLVAD VPN](assets/notext/02.webp)

Za plačilo ni nujno potrebno zagotoviti podatkov o kreditni kartici, saj Mullvad sprejema Bitcoin plačila (na verigi samo na njihovi uradni strani, vendar obstaja neuradna metoda za plačilo prek Lightning). Sprejemajo tudi gotovinska plačila po pošti.


Mullvad VPN svojo edinstvenost izkazuje tudi z odprtostjo in varnostjo. Njihova programska oprema je odprtokodna, redno pa izvajajo neodvisne varnostne preglede, da ocenijo svoje aplikacije in infrastrukturo, katerih rezultati so [objavljeni na njihovi spletni strani](https://mullvad.net/fr/blog/tag/audits). Podjetje, ki stoji za Mullvadom, ima sedež na Švedskem, državi, znani po strogih zakonih o zasebnosti. Izključno uporabljajo strežnike v lastni režiji, s čimer odpravljajo tveganja, povezana z uporabo storitev v oblaku tretjih oseb, kot so hyperscalerji AWS, Google Cloud ali Microsoft Azure.


විශේෂාංග සම්බන්ධයෙන්, Mullvad හොඳ VPN සේවාදායකයකින් අපේක්ෂා කරන සියල්ලක් ලබා දේ, VPN විසන්ධි වුවහොත් ඔබේ ගමනාගමනය ආරක්ෂා කරන ඝාතක ස්විචයක්, විශේෂිත යෙදුම් සඳහා VPN අක්‍රිය කිරීමට විකල්පයක්, සහ ඔබේ ගමනාගමනය බහු VPN සේවාදායකයන් හරහා මාර්ගගත කිරීමට හැකියාවක් ඇතුළුව.


ස්වාභාවිකවම, මෙම සේවා ගුණාත්මකභාවය වියදමක් සමඟ පැමිණේ, නමුත් සාධාරණ මිලක් බොහෝ විට ගුණාත්මකභාවය සහ අවංකභාවය සඳහා සංඥාවක් වේ. එය සමාගමට ඔබේ පුද්ගලික දත්ත තෙවන පාර්ශවයන්ට විකිණීමට අවශ්‍ය නොවන ව්‍යාපාරික ආකෘතියක් ඇති බව සංඥා දක්වයි. Mullvad VPN සමාගම මාසිකව 5 යුරෝවක් ලෙස සමාන මිලක් ලබා දේ, විවිධ උපාංග 5 දක්වා භාවිතා කළ හැක.

![MULLVAD VPN](assets/notext/03.webp)

ප්‍රධාන ධාරා VPN සපයන්නන්ට වඩා වෙනස්ව, Mullvad සමාගම නැවත නැවතත් ස්වයංක්‍රීය දායකත්වයක් වෙනුවට සේවාව සඳහා ප්‍රවේශ කාලය මිලදී ගැනීමේ ආකෘතියක් ඇත. ඔබ තෝරාගත් කාල සීමාව සඳහා බිට්කොයින් වලින් එක් වරක් ගෙවීමක් පමණක් සිදු කරයි. උදාහරණයක් ලෙස, ඔබ එක් වසරක ප්‍රවේශය මිලදී ගත් විට, ඔබට එම කාලය සඳහා සේවාව භාවිතා කළ හැකි අතර, එමෙන්ම ඔබේ ප්‍රවේශ කාලය නැවත නවීකරණය කිරීමට Mullvad වෙබ් අඩවියට නැවත යාමට සිදු වේ.

IVPN සමඟ සැසඳූ විට, තවත් උසස් තත්ත්වයේ VPN සපයන්නෙකු වන Mullvad ටිකක් ආර්ථිකමය වේ. උදාහරණයක් ලෙස, IVPN සමඟ වසර තුනක මිලදී ගැනීමක් තෝරා ගත්තත්, මාසික වියදම සමාන වන්නේ සෙ. 5.40 ක් පමණ වේ. කෙසේ වෙතත්, IVPN කිහිපයක් අමතර සේවා ලබා දෙන අතර Mullvad හි (සම්මත සැලැස්ම) වඩා අඩු මිලකට සැලැස්මක් ද ඇත, නමුත් මෙය උපාංග 2 කට පමණක් සීමා වන අතර "බහු-හොප්" ප්‍රොටෝකෝලය ව්‍යතීර්ණ වේ.

Prav tako sem izvedel nekaj neformalnih testov hitrosti za primerjavo IVPN in Mullvad. Čeprav je IVPN pokazal rahlo premoč v smislu zmogljivosti, so bile hitrosti pri Mullvad še vedno zelo zadovoljive. V primerjavi z glavnimi ponudniki VPN sta se IVPN in Mullvad izkazala za vsaj tako učinkovita, če ne celo boljša v nekaterih primerih.


## Mullvad VPN računalniku kako namestiti?


Obiščite [uradno spletno stran Mullvad](https://mullvad.net/en/download/) in kliknite na meni "*Downloads*".

![MULLVAD VPN](assets/notext/04.webp)

Windows හෝ macOS පරිශීලකයින් සඳහා, මෘදුකාංගය සෘජුවම අඩවියෙන් බාගත කර, ස්ථාපන විශාරදයා විසින් ලබා දෙන උපදෙස් අනුගමනය කර ස්ථාපනය සම්පූර්ණ කරන්න.

![MULLVAD VPN](assets/notext/05.webp)

Linux භාවිතා කරන්නන් සඳහා, ඔබේ බෙදාහැරීම සඳහා විශේෂිත උපදෙස් ["*Linux*"](https://mullvad.net/en/download/vpn/linux) කොටසෙන් සොයා ගත හැක.

![MULLVAD VPN](assets/notext/06.webp)

ස්ථාපනය සම්පූර්ණ වූ පසු, ඔබට ඔබේ ගිණුම් හැඳුනුම් අංකය ඇතුළත් කිරීමට අවශ්‍ය වේ. මෙම උපකාරක පංතියේ පසුගිය කොටස් වලදී අපි මෙය ලබා ගැනීමේ ක්‍රමය බලන්නෙමු.


## How to install Mullvad VPN on a smartphone?


Prenesite Mullvad VPN iz svoje trgovine z aplikacijami, bodisi iz [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) za uporabnike iOS, [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) za Android ali [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). Če uporabljate Android, imate tudi možnost prenosa `.apk` datoteke neposredno s [spletnega mesta Mullvad](https://mullvad.net/en/download/vpn/android).

![MULLVAD VPN](assets/notext/07.webp)

යෙදුම පළමු වරට භාවිතා කිරීමේදී, ඔබ පිටවී යනු ඇත. සේවාව සක්‍රීය කිරීමට ඔබේ ගිණුම් හැඳුනුම්පත ඇතුළත් කළ යුතුය.

![MULLVAD VPN](assets/notext/08.webp)

අපි දැන් ඔබේ උපාංගවල Mullvad සක්‍රීය කිරීමට ගමන් කරමු.


## Mullvad VPN සඳහා ගෙවීම සහ සක්‍රීය කිරීම කෙසේද?


Pojdite na [uradno spletno stran Mullvad](https://mullvad.net/) in kliknite na gumb "*Get Started*".

![MULLVAD VPN](assets/notext/09.webp)

"*generate ගිණුම් අංකය*" බොත්තම මත ක්ලික් කරන්න.

![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.

![MULLVAD VPN](assets/notext/11.webp)

පසුව "*ඔබේ ගිණුමට කාලය එක් කරන්න*" බොත්තම ක්ලික් කරන්න.

![MULLVAD VPN](assets/notext/12.webp)

ඔබේ ගිණුමේ පිවිසුම් පිටුවට එවිට ඔබ පැමිණෙනු ඇත. ඔබේ ගිණුම් අංකය ඇතුළත් කර "*Log in*" බොත්තම මත ක්ලික් කරන්න.

![MULLVAD VPN](assets/notext/13.webp)

ඔබේ ගෙවීම් ක්‍රමය තෝරන්න. මම බිට්කොයින් වලින් ගෙවීම කිරීමට නිර්දේශ කරමි, මන්ද ඔබට 10% වට්ටමක් ලැබෙන අතර, එය මාසිකව €4.50 දක්වා පහල යයි. ඔබ Lightning හරහා ගෙවීමට කැමති නම්, මම ඊළඟ කොටසෙහි විකල්ප ක්‍රමයක් සපයන්නෙමි.

![MULLVAD VPN](assets/notext/14.webp)

කොටුව "*Address එකවර ගෙවීමක් සාදන්න*" බොත්තම මත ක්ලික් කරන්න.

![MULLVAD VPN](assets/notext/15.webp)

Potem plačajte z vašim Bitcoin Wallet navedeni znesek prejemnemu Address, ki vam je bil dan.

![MULLVAD VPN](assets/notext/16.webp)

ඔබේ ගෙවීම තහවුරු වූ පසු, වෙබ් අඩවිය ඔබේ ගෙවීම හඳුනා ගැනීමට මිනිත්තු කිහිපයක් ගත විය හැක. Mullvad විසින් ගෙවීම හඳුනා ගත් පසු, "*No time left*" යන සඳහන් කිරීම වෙනුවට, ඔබේ දායකත්වයේ කාලය පිටුවේ ඉහළ වමට පෙනෙනු ඇත.

![MULLVAD VPN](assets/notext/17.webp)

ඔබට පසුව VPN සක්‍රීය කිරීමට මෘදුකාංගය මත ඔබේ ගිණුම් අංකය ඇතුළත් කළ හැක.

![MULLVAD VPN](assets/notext/18.webp)

ඔබේ ජංගම යෙදුම මත VPN සක්‍රීය කිරීමට, ක්‍රියාවලිය සම්පූර්ණයෙන්ම එකම වේ. ඔබට අවශ්‍ය වන්නේ ඔබේ ගිණුම් අංකය ඇතුළත් කිරීම පමණි.

![MULLVAD VPN](assets/notext/19.webp)

## Mullvad VPN සඳහා Lightning සමඟ ගෙවීමේ ආකාරය කෙසේද?


ඔබට තේරුම් ගත් පරිදි, Mullvad තවමත් Lightning Network හරහා ගෙවීම් පිළිගන්නේ නැත. කෙසේ වෙතත්, [Lounès](https://x.com/louneskmt) ගේ නිර්දේශයක් නිසා, මම මෙම සීමාව වටහා ගත හැකි අනෛතික සේවාවක් සොයා ගත්තා. [vpn.sovereign.engineering](https://vpn.sovereign.engineering/) හි ලබා ගත හැකි මෙම සේවාව, Lightning මත ඔබේ ගෙවීම් පිළිගනිමින්, Mullvad සඳහා වලංගු සැලැස්මක් ඔබට ලබා දේ.

![MULLVAD VPN](assets/notext/20.webp)

ඔබට මෙම වෙබ් අඩවියෙහි විවිධ විකල්ප 2ක් ඇත: ඔබට වෙබ් අඩවි කළමනාකරුට විශ්වාස කළ හැකි අතර ඔබේ ගිණුම් අංකය සෘජුවම ඇතුළත් කළ හැකි අතර, එවිට ඔබේ Mullvad පැකේජය ස්වයංක්‍රීයව වලංගු කිරීමට "*Log in*" මත ක්ලික් කරන්න. නැතහොත්, ඔබට "*Heck yeah!*" බොත්තම මත ක්ලික් කර Lightning හි වවුචරයක් මිලදී ගත හැකි අතර, එවිට ඔබේ පැකේජය ලබා ගැනීමට නිල Mullvad වෙබ් අඩවියෙහි එය භාවිතා කළ හැක. ![MULLVAD VPN](assets/notext/21.webp) මෙම අවස්ථා දෙකේම, ඔබට ඔබේ පැකේජයේ කාල සීමාව තෝරා ගැනීමට අයදුම් කරනු ඇත. ඔබට මාස 6 සහ වසර 1 අතර තෝරා ගත හැක. ![MULLVAD VPN](assets/notext/22.webp) එවිට "*Top-up with Lightning*" බොත්තම මත ක්ලික් කරන්න. ![MULLVAD VPN](assets/notext/23.webp) මිලදී ගැනීම අවසන් කිරීමට, ඔබේ Lightning Wallet සමඟ Invoice ගෙවන්න. ![MULLVAD VPN](assets/notext/24.webp) ඔබ වවුචරයක් මිලදී ගැනීමට තීරණය කළේ නම්, Mullvad වෙබ් අඩවියේ, ඔබේ ගිණුමේ ලබා ගත හැකි ගෙවීම් ක්‍රම අතර "*Voucher*" තෝරන්න. එවිට, vpn.sovereign.engineering වෙබ් අඩවියෙන් ඔබට ලැබුණු වවුචර අංකය නියමිත කොටුවේ ඇතුළත් කරන්න. ![MULLVAD VPN](assets/notext/25.webp) ## Mullvad VPN භාවිතා කිරීම සහ වින්‍යාස කිරීම කෙසේද?


දැන් ඔබට සක්‍රීය ගිණුමක් ඇති අතර Mullvad මෘදුකාංගය හෝ යෙදුම තුළ ඔබේ ගිණුම් අංකය ඇතුළත් කර ඇති බැවින්, ඔබේ VPN සේවාවන් සම්පූර්ණයෙන්ම භුක්ති විඳිය හැක. ![MULLVAD VPN](assets/notext/26.webp) VPN එකෙන් වෙන් වීමට, "*Disconnect*" බොත්තම මත ක්ලික් කරන්න. ![MULLVAD VPN](assets/notext/27.webp) "*Disconnect*" බොත්තම අසල ඇති කුඩා රතු ඊතලය, වර්තමාන ස්ථානය වෙනස් නොකර සර්වර් වෙනස් කිරීමට ඔබට ඉඩ සලසයි. ![MULLVAD VPN](assets/notext/28.webp) ඔබේ VPN සර්වර් සඳහා නගර වෙනස් කිරීමට අවශ්‍ය නම්, නව ස්ථානයක් තෝරා ගැනීමට "*Switch location*" මත ක්ලික් කරන්න. ![MULLVAD VPN](assets/notext/29.webp) තිරයේ ඉහළින්, ඔබේ උපාංගයේ නාමය සහ ඔබේ පැකේජයේ ඉතිරි කාලය ඔබට දැක ගත හැක. ![MULLVAD VPN](assets/notext/30.webp) කුඩා මිනිසාගේ අයිකනය මත ක්ලික් කිරීමෙන්, ඔබේ ගිණුම පිළිබඳ විස්තරාත්මක තොරතුරු වෙත ප්‍රවේශ විය හැක. ![MULLVAD VPN](assets/notext/31.webp) සැකසුම් වෙත ප්‍රවේශ වීමට, ගියර් රෝදය මත ක්ලික් කරන්න. ![MULLVAD VPN](assets/notext/32.webp) "*User Interface settings*" මෙනුව තුළ, ඔබේ මෘදුකාංගයේ සැකසුම්, Interface භාෂාව සහ ඔබේ පද්ධතියේ එහි හැසිරීම ඇතුළුව අභිරුචිකරණය කළ හැක. ![MULLVAD VPN](assets/notext/33.webp) "*VPN settings*" මෙනුව තුළ, ඔබේ VPN සම්බන්ධ විකල්ප සොයා ගත හැක. ඔබේ යන්ත්‍රය ආරම්භ වන විට ඔබේ VPN සම්බන්ධතාව ස්වයංක්‍රීයව ආරම්භ වන පරිදි "*Launch app on start-up*" සහ "*Auto-connect*" විකල්ප සක්‍රීය කිරීමට මම නිර්දේශ කරමි.

![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.

![MULLVAD VPN](assets/notext/35.webp)

අවසානයේ, "*Split tunneling*" මෙනුව ඔබේ යන්ත්‍රයේ විශේෂිත යෙදුම් තෝරා ගැනීමට ඉඩ සලසයි, ඒ සඳහා අන්තර්ජාල ගමනාගමනය VPN හරහා මාර්ගගත නොවේ.

![MULLVAD VPN](assets/notext/36.webp)

ඔබේ Mullvad ගිණුමේ සාරාංශයක් ලබා ගැනීමට සහ විවිධ සම්බන්ධිත උපාංග කළමනාකරණය කිරීමට, ඔබට වෙබ් අඩවියේ "*Devices*" මෙනුව ක්ලික් කළ හැක.

![MULLVAD VPN](assets/notext/37.webp)

අහෝ, ඔබට දැන් Mullvad VPN සම්පූර්ණයෙන්ම භුක්ති විඳීමට අවශ්‍ය සියලු දේ ඇත. Mullvad සමඟ සමාන විශේෂාංග සහ මිල ගණන් لحاظයෙන් වෙනත් VPN සපයන්නෙකු සොයා ගැනීමට ඔබට උනන්දුවක් ඇත්නම්, IVPN පිළිබඳ අපගේ උපකාරකයද පරීක්ෂා කිරීමට මම නිර්දේශ කරමි:


https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68