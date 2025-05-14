---
name: ටෝර් බ්‍රවුසරය
description: Kako uporabljati brskalnik Tor?
---
![cover](assets/cover.webp)


එහි නම යෙදී ඇති පරිදි, බ්‍රවුසරයක් යනු අන්තර්ජාලය නාවික කිරීම සඳහා භාවිතා කරන මෘදුකාංගයකි. එය පරිශීලකයාගේ යන්ත්‍රය සහ වෙබ් අතර ද්වාරයක් ලෙස කටයුතු කරමින්, වෙබ් අඩවිවල කේතය අන්තර්ක්‍රියාත්මක සහ කියවිය හැකි පිටු වලට පරිවර්තනය කරයි. ඔබේ බ්‍රවුසරය තෝරා ගැනීම ඉතා වැදගත් වන අතර, එය ඔබේ නාවික අත්දැකීමට පමණක් නොව, ඔබේ මාර්ගගත ආරක්ෂාව සහ පෞද්ගලිකත්වය සඳහාද බලපායි.


බ්‍රවුසරය සෙවුම් යන්ත්‍රය සමඟ ගැලපෙන ලෙස නොමැතිව සිටින්න. බ්‍රවුසරය යනු ඔබ අන්තර්ජාලයට ප්‍රවේශ වීමට භාවිතා කරන මෘදුකාංගය (Chrome හෝ Firefox වැනි), එසේම සෙවුම් යන්ත්‍රය යනු Google හෝ Bing වැනි සේවාවක් වන අතර, එය ඔබට මාර්ගගතව තොරතුරු සොයා ගැනීමට උපකාරී වේ.


Danes je Google Chrome daleč najbolj uporabljan brskalnik. Leta 2024 predstavlja približno 65 % svetovnega trga. Chrome je cenjen zaradi svoje hitrosti in zmogljivosti, vendar ni nujno najboljša izbira za vsakogar, še posebej, če vam je zasebnost prioriteta. Chrome pripada Googlu, podjetju, ki je znano po zbiranju in analizi ogromnih količin podatkov o svojih uporabnikih. In res, njihov lastni brskalnik je v središču njihove strategije nadzora. Ta programska oprema je osrednja komponenta v večini vaših spletnih interakcij. Obvladovanje zbiranja podatkov na vašem brskalniku je pomembno vprašanje za Google.

![TOR BROWSER](assets/notext/01.webp)

*Source: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*


බ්‍රවුසරවල විශාල පවුල් කිහිපයක් ඇත, සෑම එකක්ම විශේෂිත රෙන්ඩරින් එන්ජිමක් මත පදනම්ව ඇත. Google Chrome, Microsoft Edge, Brave, Opera, හෝ Vivaldi වැනි බ්‍රවුසර සියල්ලම Google විසින් සංවර්ධනය කරන ලද Chrome හි සැහැල්ලු සහ විවෘත මූලාශ්‍ර අනුවාදයක් වන Chromium බ්‍රවුසර මත ස්ථාපිත වේ. මෙම සියලුම බ්‍රවුසර WebKit හි Fork වන Blink රෙන්ඩරින් එන්ජිම භාවිතා කරයි, එය KHTML වෙතින් උත්පන්න වේ. වෙළඳපොළේ Chromium හි ප්‍රබලත්වය Blink සඳහා ප්‍රාථමිකව තම වෙබ් අඩවි ඔප්ටිමයිස් කිරීමේ傾向ය ඇති නිසා, එයින් උත්පන්න වන බ්‍රවුසර විශේෂයෙන්ම කාර්යක්ෂම වේ.


Safari, Apple's browser, uporablja WebKit, ki prav tako izvira iz KHTML.


Po drugi strani pa brskalniki, kot so Mozilla Firefox, LibreWolf in Tor Browser, temeljijo na Gecko, drugačnem pogonu za upodabljanje, ki izvira iz brskalnika Netscape.


සමීප බ්‍රවුසරය තෝරා ගැනීම ඔබේ අවශ්‍යතා මත රඳා පවතී. නමුත් ඔබේ පෞද්ගලිකත්වය, එනම් ඔබේ ආරක්ෂාව ගැන අවම වශයෙන් කාරුණික නම්, සාමාන්‍ය භාවිතය සඳහා Firefox සහ තවත් පෞද්ගලිකත්වයක් සඳහා Tor Browser යොදා ගැනීමට මම නිර්දේශ කරමි. මෙම උපකාරිකාවේ, මම ඔබට Tor Browser සමඟ පහසුවෙන් ආරම්භ කිරීමේ ආකාරය පෙන්වන්නෙමි.

![TOR BROWSER](assets/notext/02.webp)


## ටෝර් බ්‍රවුසරයට හැඳින්වීම


ටෝර් බ්‍රවුසරය යනු ආරක්ෂිත සහ හැකි තරම් පෞද්ගලික අන්තර්ජාල නාවිගේෂනය සඳහා විශේෂිතව නිර්මාණය කරන ලද බ්‍රවුසරයකි. මෙම බ්‍රවුසරය ෆයර්ෆොක්ස් මත පදනම්ව ඇති අතර, එබැවින් ගෙකෝ රෙන්ඩරින් එන්ජිම මත පදනම්ව ඇත.

Tor Browser Tor ජාලය භාවිතා කර ඔබේ ගමනාගමනය කේතනය කර relay සේවාදායක කිහිපයක් හරහා මාර්ගගත කර ගමනාන්තයට සම්ප්‍රේෂණය කරයි. "*onion routing*" ලෙස හැඳින්වෙන මෙම බහු-ස්ථර මාර්ගගත කිරීමේ ක්‍රියාවලිය ඔබේ සැබෑ IP Address සඟවා තබා ගැනීමට උපකාරී වන අතර, ඔබේ ස්ථානය සහ මාර්ගගත ක්‍රියාකාරකම් හඳුනා ගැනීම අපහසු කරයි. කෙසේ වෙතත්, Tor ජාලය භාවිතා නොකරන සම්මත බ්‍රවුසරයකට වඩා බ්‍රවුසිං අනිවාර්යයෙන්ම මන්දගාමී වේ, එය සෘජු නොවන බැවින්.

වෙනත් බ්‍රවුසර වලට වඩා, Tor බ්‍රවුසරය ඔබේ මාර්ගගත ක්‍රියාකාරකම් හඹා යාම වැළැක්වීමට විශේෂාංග ඒකාබද්ධ කරයි, උදාහරණයක් ලෙස, සෑම පිවිසුණු වෙබ් අඩවියක්ම වෙන් කිරීම සහ වසා දැමීමේදී කුකීස් සහ ඉතිහාසය ස්වයංක්‍රීයව මකා දැමීම. එය සෙවීම් කරන වෙබ් අඩවි වෙත සියලුම පරිශීලකයන් හැකි ඉක්මනින් සමාන ලෙස පෙනෙන පරිදි, ෆින්ගර්ප්‍රින්ට් කිරීමේ අවදානම් අවම කිරීමටත් නිර්මාණය කර ඇත.


Tor Browser lahko zelo dobro uporabite za dostop do standardne spletne strani (`.com`, `.org`, itd.). V tem primeru je vaš promet anonimiziran s prehodom skozi več Tor vozlišč, preden doseže izhodno vozlišče, ki komunicira s končno stranjo na odprtem spletu.

![TOR BROWSER](assets/notext/03.webp)

ඔබට `.onion` වලින් අවසන් වන සඟවා ඇති සේවා ප්‍රවේශ වීමට Tor Browser භාවිතා කළ හැක. මෙම තත්ත්වයේදී, සියලුම ගමනාගමනය Tor ජාලය තුළම රැඳී සිටින අතර, පිටවීමේ නියමකින් තොරව, පරිශීලකයා සහ ගමනාන්ත සේවාදායකයා සඳහා සම්පූර්ණ පෞද්ගලිකත්වය සහතික කරයි. මෙවැනි ක්‍රියාකාරීත්වය විශේෂයෙන්ම "*අඳුරු ජාලය*" ලෙස sometimes හැඳින්වෙන, සම්ප්‍රදායික සෙවුම් යන්ත්‍ර මඟින් දර්ශනය නොකෙරෙන අන්තර්ජාලයේ කොටසකට ප්‍රවේශ වීමට භාවිතා වේ.

![TOR BROWSER](assets/notext/04.webp)


## Kakšna je razlika med omrežjem Tor in brskalnikom Tor?


ටෝර් ජාලය සහ ටෝර් බ්‍රවුසරය වෙන්ව හඳුනාගත යුතු දෙවල් වන අතර, ඒවා එකිනෙකට සමාන වේ. ටෝර් ජාලය යනු relay සේවාදායකයන්ගෙන් සමන්විත ගෝලීය යටිතල පහසුකමක් වන අතර, එය පරිශීලකයින් විසින් ක්‍රියාත්මක කරනු ලබන අතර, අන්තර්ජාල ගමනාගමනය අවසන් ගමනාන්තය වෙත යොමු කිරීමට පෙර කිහිපයක් nodes හරහා ගමන් කිරීමෙන් අනන්‍යතාවය රහිත කරයි. මෙය ප්‍රසිද්ධ ලූනු මාර්ගගත කිරීමයි.


අනෙක් අතට, Tor බ්‍රවුසරය යනු මෙම ජාලයට පහසු ආකාරයෙන් ප්‍රවේශ වීමට පහසුකම් සපයන විශේෂිත බ්‍රවුසරයකි. එය Tor ජාලයට සම්බන්ධ වීමට අවශ්‍ය සියලුම සැකසුම් පෙරනිමි ලෙස ඒකාබද්ධ කර ඇති අතර, පෞද්ගලිකත්වය සහ ආරක්ෂාව උපරිම කිරීමේදී පරිචිත බ්‍රවුසිං අත්දැකීමක් ලබා දීමට Firefox හි වෙනස් කළ අනුවාදයක් භාවිතා කරයි.


ටෝර් ජාලය ටෝර් බ්‍රවුසරය මගින් පමණක් භාවිතා නොවේ. එය ඔවුන්ගේ සන්නිවේදන ආරක්ෂා කිරීමට විවිධ මෘදුකාංග සහ යෙදුම් මගින් භාවිතා කළ හැකිය. උදාහරණයක් ලෙස, ඔබේ Bitcoin නියමකය මත ටෝර් ජාලය හරහා සන්නිවේදන සක්‍රීය කිරීමෙන් ඔබේ IP Address වෙනත් පරිශීලකයන්ගෙන් සඟවා තබා ගැනීමට සහ ඔබේ Bitcoin-සම්බන්ධ ගමනාගමනය පිළිබඳව ඔබේ අන්තර්ජාල සේවා සපයන්නාගේ නිරීක්ෂණය වැළැක්වීමට හැකිය.

සාරාංශය වශයෙන්, Tor ජාලය යනු අපගේ අන්තර්ජාල ගවේෂණය තුළ පෞද්ගලිකත්වය සපයන යටිතල පහසුකම් වන අතර, Tor බ්‍රවුසරය යනු අපගේ වෙබ් ගවේෂණයේ කොටසක් ලෙස මෙම ජාලය භාවිතා කිරීමට අපට ඉඩ සලසන මෘදුකාංගය වේ.


## Kako namestiti Tor Browser?


ටෝර් බ්‍රවුසරය Windows, Linux, සහ macOS සඳහා පරිගණක සඳහා, මෙන්ම Android සඳහා ස්මාර්ට්ෆෝන් සඳහා ලබා ගත හැක. ඔබේ පරිගණකයේ ටෝර් බ්‍රවුසරය ස්ථාපනය කිරීමට, [නිල ටෝර් ව්‍යාපෘති වෙබ් අඩවිය](https://www.torproject.org/) වෙත පිවිසෙන්න.

![TOR BROWSER](assets/notext/05.webp)

"*Tor Browser බාගන්න*" බොත්තම මත ක්ලික් කරන්න.

![TOR BROWSER](assets/notext/06.webp)

ඔබේ මෙහෙයුම් පද්ධතිය සඳහා සුදුසු අනුවාදය තෝරන්න.

![TOR BROWSER](assets/notext/07.webp)

ස්ථාපනය ආරම්භ කිරීමට ක්‍රියාත්මය කළ හැකි ගොනුව මත ක්ලික් කරන්න, එවිට ඔබේ භාෂාව තෝරන්න.

![TOR BROWSER](assets/notext/08.webp)

තැන්පත් කිරීම් සිදු කරන ලද ෆෝල්ඩරය තෝරන්න, එවිට "*Install*" බොත්තම ක්ලික් කරන්න.

![TOR BROWSER](assets/notext/09.webp)

ස්ථාපනය සම්පූර්ණ වන තුරු රැඳී සිටින්න.

![TOR BROWSER](assets/notext/10.webp)

අවසානයේ, "*Finish*" බොත්තම මත ක්ලික් කරන්න.

![TOR BROWSER](assets/notext/11.webp)


## Kako uporabljati Tor Browser?


ටෝර් බ්‍රවුසරය සම්මත බ්‍රවුසරයක් ලෙස භාවිතා කරයි.

![TOR BROWSER](assets/notext/12.webp)

Ob prvem zagonu vam brskalnik prikaže stran, ki vas vabi k povezavi v omrežje Tor. Preprosto kliknite na gumb "*Connect*", da vzpostavite povezavo.

![TOR BROWSER](assets/notext/13.webp)

Če želite, da se programska oprema samodejno poveže v omrežje Tor med vašimi prihodnjimi uporabami, označite možnost "*Vedno se poveži samodejno*".

![TOR BROWSER](assets/notext/14.webp)

Tor ජාලයට සම්බන්ධ වූ විට, ඔබ මුල් පිටුවට පැමිණෙනු ඇත.

![TOR BROWSER](assets/notext/15.webp)

අන්තර්ජාලයෙහි සෙවීමක් සිදු කිරීමට, සරලව සෙවුම් තීරුවේ ඔබේ විමසුම ඇතුළත් කර "*enter*" යතුර ඔබන්න.

![TOR BROWSER](assets/notext/16.webp)

Potem boste rezultate iz iskalnika dobili na enak način kot pri drugih brskalnikih.

![TOR BROWSER](assets/notext/17.webp)

DuckDuckGo上的"*Onionize*"选项允许您通过Tor网络上的隐藏服务使用搜索引擎，方法是访问其`.onion` Address。

![TOR BROWSER](assets/notext/18.webp)


## Kako nastaviti Tor Browser?


ඔබේ බ්‍රවුසර තිරයේ ඉහළින්, ඔබේ ප්‍රියතමයන් ආයාත කිරීම සඳහා විකල්පයක් සොයා ගත හැකිය. මෙය ඔබේ පැරණි බ්‍රවුසරයෙන් පොත් සලකුණු ස්වයංක්‍රීයව Tor බ්‍රවුසරයට ඒකාබද්ධ කිරීමට ඉඩ සලසයි.

![TOR BROWSER](assets/notext/19.webp)

ඔබට සංචාරය කරන වෙබ් පිටුවේ ඉහළ දකුණු කෙළවරේ පිහිටා ඇති තාරකා අයිකනය ක්ලික් කිරීමෙන් නව පිටු සලකුණු එකතු කිරීමේ විකල්පය ද ඇත.

![TOR BROWSER](assets/notext/20.webp)

මෙනුවේ දකුණු පැත්තේ, ඔබට විවිධ විකල්ප ලබා ගත හැක.

![TOR BROWSER](assets/notext/21.webp)The "*New identity*" button allows you to change your Tor identity. Specifically, this enables you to start a new user session on Tor, meaning changing your IP address and resetting cookies and open sessions.

![TOR BROWSER](assets/notext/22.webp)

"*Bookmarks*" මෙනුව ඔබට ඔබේ පොත් සලකුණු කළමනාකරණය කිරීමට ඉඩ සලසයි.

![TOR BROWSER](assets/notext/23.webp)

"*ඉතිහාසය*" ඔබට ඔබේ බ්‍රවුසිං ඉතිහාසය වෙත ප්‍රවේශ වීමට ඉඩ සලසයි, ඔබ එය සැකසුම් වල සක්‍රීය කර ඇති නම්.

![TOR BROWSER](assets/notext/24.webp)

"*උපසම්පාදන සහ තේමාවන්*" මෙනුව ඔබේ බ්‍රව්සරයේ පෙනුම අභිරුචිකරණය කිරීමට හෝ දිගුවක් එක් කිරීමට ඉඩ සලසයි. Tor බ්‍රව්සරය Mozilla Firefox මත පදනම්ව ඇති බැවින්, ඔබට Firefox සඳහා ලබා ගත හැකි තේමාවන් සහ දිගුවන් භාවිතා කළ හැක.

![TOR BROWSER](assets/notext/25.webp)

අවසානයේ, "*සැකසුම්*" බොත්තම ඔබට ඔබේ බ්‍රව්සරයේ සැකසුම් වෙත ප්‍රවේශ වීමට අවස්ථාව ලබා දේ.

![TOR BROWSER](assets/notext/26.webp)

සැකසුම් වල "*General*" ටැබ් එකේ, Tor Browser පරිශීලක Interface අභිරුචිකරණය කිරීමට ඉඩ දෙන විවිධ විකල්ප ඇත.

![TOR BROWSER](assets/notext/27.webp)

V zavihku "*Domov*" lahko izberete spremembo privzete strani, ki se prikaže ob odpiranju Tor Browserja in ob odpiranju novih zavihkov.

![TOR BROWSER](assets/notext/28.webp)

"*Search*" ටැබ් එකේ, ඔබට සෙවුම් යන්ත්‍රය තෝරා ගත හැක. Tor Browser පෙරනිමි ලෙස DuckDuckGo, පරිශීලකයන්ගේ පෞද්ගලිකත්වය ආරක්ෂා කිරීමට මූලික වූ සෙවුම් යන්ත්‍රයක්, ලෙස සකසා ඇත, නමුත් ඔබට උදාහරණයක් ලෙස Google හෝ Startpage තෝරා ගත හැක.

![TOR BROWSER](assets/notext/29.webp)

ඔබට ඔබේ සෙවුම් යන්ත්‍රයේ කෙටි මාර්ග සකස් කළ හැක.

![TOR BROWSER](assets/notext/30.webp)

උදාහරණයක් ලෙස, ඔබේ සෙවීමේ පදය, "*Bitcoin*" වැනි, "*@wikipedia*" ලෙස ටයිප් කළ හැක, බ්‍රවුසරයේ සෙවීමේ තීරුව තුළ.

![TOR BROWSER](assets/notext/31.webp)

මෙම විශේෂාංගය පසුව ඔබේ පදය සෘජුවම විකිපීඩියා අඩවිය මත සෙවීමක් සිදු කරයි.

![TOR BROWSER](assets/notext/32.webp)

ඔබට එබැවින් විවිධ වෙබ් අඩවි සඳහා වෙනත් අභිරුචි කෙටි මාර්ග සකස් කළ හැක.


ඊළඟට, "*රහස්‍යතා සහ ආරක්ෂාව*" ටැබය තුළ, ඔබට රහස්‍යතා සහ ආරක්ෂාවට සම්බන්ධ සියලු සැකසුම් සොයා ගත හැක.

![TOR BROWSER](assets/notext/33.webp)

ඔබට ඔබේ බ්‍රවුසිං ඉතිහාසය තබා ගැනීම හෝ මකා දැමීමේ විකල්පය ඇත.

![TOR BROWSER](assets/notext/34.webp)

ඔබට විවිධ වෙබ් අඩවි සඳහා ලබා දෙන ප්‍රවේශ අවසරයන් කළමනාකරණය කළ හැක.

![TOR BROWSER](assets/notext/35.webp)

ඔබේ බ්‍රවුසරයේ සමස්ත ආරක්ෂාව සඳහා, "*Safer*" සහ "*Safest*" මාදිලි ඔබට ඔබගේ සංචාරය කරන වෙබ් අඩවි විසින් ක්‍රියාත්මක කරන වෙබ් ක්‍රියාකාරකම් සහ ස්ක්‍රිප්ට් සකසන්න ඉඩ සලසයි. මෙය දුර්වලතා පරිභවය අවම කරයි, නමුත් එමඟින් වෙබ් අඩවි වල ප්‍රදර්ශනය සහ අන්තර්ක්‍රියාකාරිත්වය ද බලපානු ඇත. ![TOR BROWSER](assets/notext/36.webp) ඔබට අනෙකුත් ආරක්ෂිත විකල්ප සොයාගත හැක, අනතුරුදායක අන්තර්ගත අවහිරකාරකයක් සහ HTTPS පමණක් මාදිලිය ඇතුළුව, එය සත්‍ය වශයෙන්ම මෙම ප්‍රොටෝකෝලය ගරු කරන අඩවි සමඟ සම්බන්ධතා සහතික කරයි. ![TOR BROWSER](assets/notext/37.webp) අවසානයේ, "*Connection*" ටැබ් එකේ, ඔබට Tor ජාලයට සම්බන්ධ වීම සම්බන්ධ සියලු සැකසුම් සොයාගත හැක. මෙය ඔබට Tor වෙත ප්‍රවේශය සීමා කර ඇති ප්‍රදේශවලින් Tor වෙත ප්‍රවේශ වීම සඳහා පාලමක් සකසන්න හැකි ස්ථානයයි. ![TOR BROWSER](assets/notext/38.webp) මෙන්න, ඔබ දැන් අන්තර්ජාලය ආරක්ෂිත සහ පුද්ගලික ආකාරයකින් සංචාරය කිරීමට සූදානම්! මොනවාද අන්තර්ජාලයෙහි පුද්ගලිකත්වය ඔබට රුචිකත්වයක් නම්, මම මල්වඩ් VPN පිළිබඳ මෙම වෙනත් උපකාරකය සොයාගැනීමටත් නිර්දේශ කරමි:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8