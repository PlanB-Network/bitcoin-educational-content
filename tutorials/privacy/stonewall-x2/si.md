---
name: Stonewall x2
description: Stonewall x2 ගනුදෙනු අවබෝධ කර ගැනීම සහ භාවිතා කිරීම
---
![cover stonewall x2](assets/cover.webp)


***අවවාදය:** Samourai Wallet හි ආරම්භකයින් අත්අඩංගුවට ගැනීම සහ ඔවුන්ගේ සේවාදායකයන් අප්‍රේල් 24 වැනිදා අත්පත් කර ගැනීමෙන් පසු, Stonewallx2 ගනුදෙනු සම්බන්ධ පාර්ශවයන් අතර PSBTs අතින් හුවමාරු කිරීමෙන් පමණක් ක්‍රියාත්මක වේ, පරිශීලකයින් දෙදෙනාම ඔවුන්ගේම Dojo සම්බන්ධ වී සිටින විට. කෙසේ වෙතත්, මෙම මෙවලම් ඉදිරි සති කිහිපයේදී නැවත ආරම්භ කළ හැකි බවක් ඇත. මේ අතර, Stonewallx2 හි සෞඛ්‍යමය ක්‍රියාකාරිත්වය අවබෝධ කර ගැනීමට සහ ඒවා අතින් සිදු කරන ආකාරය ඉගෙන ගැනීමට ඔබට තවමත් මෙම ලිපිය උපදේශනය කළ හැක.*


_ඔබ Stonewallx2 ක්‍රියාවලිය අතින් සිදු කිරීමට සලකා බලන්නේ නම්, මෙම උපදෙස් මාලාවේ විස්තර කරන ලද ක්‍රියාවලිය සමඟ ඉතා සමාන වේ. ප්‍රධාන වෙනස වන්නේ Stonewallx2 ගනුදෙනු වර්ගය තෝරා ගැනීමේදී: `Online` තෝරන්නේ වෙනුවට, `In Person / Manual` මත ක්ලික් කරන්න. එවිට, Stonewallx2 ගනුදෙනුව නිර්මාණය කිරීමට ඔබට PSBTs අතින් Exchange කළ යුතුය. ඔබේ සහකරු සමඟ භෞතිකව ආසන්නව සිටී නම්, QR කේත අනුපිළිවෙලින් ස්කෑන් කළ හැක. ඔබ දුරස්ථව සිටී නම්, JSON ගොනු ආරක්ෂිත සන්නිවේදන නාලිකාවක් හරහා හුවමාරු කළ හැක. ඉතිරි උපදෙස් මාලාව වෙනස් නොවේ._


_අපි මෙම නඩුවේ සංවර්ධන මෙන්ම සම්බන්ධිත මෙවලම් සම්බන්ධයෙන් ඇතිවන සංවර්ධනද ආසන්නයෙන් අනුගමනය කරමින් සිටිමු. නව තොරතුරු ලබා ගත හැකි වීමත් සමඟ මෙම උපකාරකය යාවත්කාලීන කරන බවට විශ්වාසයෙන් සිටින්න._


_මෙම උපකාරිකාව අධ්‍යාපනික සහ තොරතුරුමය අරමුණු සඳහා පමණක් සපයනු ලැබේ. අපි මෙම මෙවලම් අපරාධමය අරමුණු සඳහා භාවිතා කිරීම අනුමත නොකරන අතර හුරුවනවාද නැත. තමන්ගේ නීතිමය බලප්‍රදේශයේ නීති අනුගමනය කිරීමේ වගකීම සෑම පරිශීලකයෙකුගේම වගකීමයි._


---

> *हरेक खर्च CoinJoin बनाउनुहोस्।*

## Stonewall x2 ගනුදෙනුවක් කුමක්ද?


Stonewall x2 යනු Bitcoin ගනුදෙනුවක විශේෂිත ආකාරයක් වන අතර, වියදමක් දියත් කිරීමේදී පරිශීලක පෞද්ගලිකත්වය වැඩි දියුණු කිරීම සඳහා, එම වියදමට සම්බන්ධ නොවන තෙවන පාර්ශවයකු සමඟ සහයෝගයෙන් ක්‍රියාත්මක වේ. මෙම ක්‍රමය, තෙවන පාර්ශවයකට ගෙවීමක් සිදුකරන අතර, දෙපාර්ශවිකයන් අතර කුඩා CoinJoinක් අනුකරණය කරයි. Stonewall x2 ගනුදෙනු Samourai Wallet යෙදුම සහ Sparrow Wallet මෘදුකාංගය දෙකේම ලබා ගත හැක. දෙකම අන්තර්ක්‍රියාකාරී වේ.


Njegovo delovanje je razmeroma preprosto: za plačilo uporabimo UTXO, ki ga imamo v lasti, in poiščemo pomoč tretje osebe, ki prav tako prispeva s svojim UTXO. Transakcija ima za posledico štiri izhode: dva izmed njih sta enakih zneskov, eden je namenjen prejemnikovemu Address, drugi pa Address, ki pripada sodelavcu. Tretji UTXO se vrne na drug Address sodelavca, kar mu omogoča, da povrne začetni znesek (nevtralno dejanje zanj, modulo Mining pristojbine), in zadnji UTXO se vrne na Address, ki pripada nam, kar predstavlja vračilo iz plačila.


यसरी, Stonewall x2 लेनदेनहरूमा तीन फरक भूमिकाहरू परिभाषित गरिएका छन्:


- යථාර්ථ ගෙවීම සිදු කරන යවන්නා;
- සහකාරයා, ගනුදෙනුවේ සමස්ත අනන්‍යතාවය වැඩි දියුණු කිරීමට බිට්කොයින් ලබා දෙන අතර, අවසානයේදී ඔවුන්ගේ අරමුදල් සම්පූර්ණයෙන්ම නැවත ලබා ගන්නා (Mining ගාස්තු හැර, ඔවුන් සඳහා නිරපේක්ෂ ක්‍රියාවක්);
- ලැබුණුකරු, කුමන හෝ විශේෂිත ගනුදෙනුවක් පිළිබඳව නොදැනුවත් විය හැකි අතර, එමඟින් එවකරුගෙන් ගෙවීමක් බලාපොරොත්තු වේ.


උදාහරණයක් ගනිමු හොඳින් තේරුම් ගැනීමට. ඇලීස් ඇයගේ බගට් එක මිලදී ගැනීමට බේකරි එකට ගොස් ඇත, එය `4,000 Sats` වියදම් වේ. ඇය ඇයගේ ගෙවීම සඳහා බිට්කොයින් වලින් ගෙවීමට කැමති අතර, ඇයගේ ගෙවීම සඳහා නිකුත් කිරීමේ මට්ටමක් පවත්වා ගැනීමට කැමතිය. එබැවින් ඇය ඇයගේ මිතුරා බොබ්ට ඇයව මෙම ක්‍රියාවලිය තුළ සහය වීමට ඇමතීය.

![schema stonewall x2](assets/en/1.webp)

මෙම ගනුදෙනුව විශ්ලේෂණය කිරීමෙන්, බේකර්ට බගට් එක සඳහා ගෙවීමක් ලෙස `4,000 Sats` ලැබී ඇති බව අපට දැකගත හැක. ඇලීස් `10,000 Sats` ආදානයක් ලෙස භාවිතා කර `6,000 Sats` ප්‍රතිදානයක් ලබාගෙන, `-4,000 Sats` ශුද්ධ ශේෂයක් ලබා ගත්තේය, එය බගට් එකේ මිලට සමාන වේ. බොබ් සම්බන්ධයෙන්, ඔහු `15,000 Sats` ආදානයක් ලබා දී `4,000 Sats` සහ `11,000 Sats` ලෙස ප්‍රතිදාන දෙකක් ලබා ගත් අතර, `0` ශේෂයක් ලැබීය.

මෙම උදාහරණයේ, මම හිතාමතාම Mining ගාස්තු නොසලකා හරිමින් අවබෝධය පහසු කළෙමි. වాస్తවයේ, ගනුදෙනු ගාස්තු ගෙවීම් යවන්නා සහ සහකරු අතර සමානව බෙදා ගනු ලැබේ.


## Stonewall සහ Stonewall x2 අතර වෙනස කුමක්ද?


StonewallX2 ගනුදෙනුවක් Stonewall ගනුදෙනුවක් මෙන්ම ක්‍රියා කරයි, නමුත් පළමුවැන්න සහයෝගී වන අතර දෙවනුව එසේ නොවේ. අපි දැක ඇති පරිදි, Stonewall x2 ගනුදෙනුවක් තුළ ගෙවීමේ පිටත තෙවන පාර්ශවයකගේ සහභාගීත්වය අවශ්‍ය වන අතර, ගනුදෙනු රහස්‍යතාව වැඩි දියුණු කිරීමට ඔවුන්ගේ බිට්කොයින් ලබා දේ. සාමාන්‍ය Stonewall ගනුදෙනුවක, සහයෝගීකරුගේ භූමිකාව ගෙන යන්නේ යවන පුද්ගලයා වේ.


අපේ ඇලීස්ගේ බේකරි උදාහරණය නැවත සලකා බලමු. ඇයගේ වියදමට ඇය සමඟ යාමට බොබ් වැනි කෙනෙකු සොයාගත නොහැකි වූවා නම්, ඇය තනිවම ස්ටෝන්වෝල් ගනුදෙනුවක් කළ හැකි විය. එබැවින්, ආදාන UTXO දෙකම ඇයගේ විය, සහ ඇය ප්‍රතිදානයේදී 3 ලබා ගත්තා.

![transaction stonewall](assets/en/2.webp)


බාහිර දෘෂ්ටිකෝණයකින්, ගනුදෙනු රටාව එසේම පවතිනු ඇත.

![Stonewall or Stonewall x2?](assets/en/5.webp)

අදාළව, Samourai වියදම් මෙවලමක් භාවිතා කරන විට තර්කය පහත පරිදි විය යුතුය:


- Če trgovec ne podpira PayJoin Stowaway, se lahko izvede sodelovalna transakcija z drugo osebo, ki ni vključena v plačilo, z uporabo Stonewall x2.
- Če nihče ni najden za izvedbo transakcije Stonewall x2, se lahko transakcija Stonewall izvede samostojno, posnemajoč vedenje transakcije Stonewall x2.
- අවසානයේ, අවසන් විකල්පය වන්නේ Samourai විසින් නඩත්තු කරන සේවාදායකය වන JoinBot සමඟ ගනුදෙනුවක් කිරීමයි, එය ඉල්ලීම මත, Stonewall x2 ගනුදෙනුවක සහකාරයා ලෙස ක්‍රියා කළ හැක.


ඔබට Stonewall X2 ගනුදෙනුවකදී ඔබට සහය වීමට කැමති සහකරුක් සොයා ගැනීමට අවශ්‍ය නම්, යවන අය සහ සහකරුන් සම්බන්ධ කර ගැනීමට Samourai පරිශීලකයින් විසින් නඩත්තු කරන මෙම Telegram කණ්ඩායම (අනධිකෘත) පිවිසිය හැක: [Make Every Spend a CoinJoin](https://t.me/EverySpendACoinjoin).


[**-> Stonewall ගනුදෙනු පිළිබඳව වැඩිදුර ඉගෙන ගන්න**](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


## Stonewall x2 ගනුදෙනුවක අරමුණ කුමක්ද?


Stonewall x2 ව්‍යුහය ගනුදෙනුවට සුවිශේෂී ලෙස එන්ට්‍රොපිය එකතු කරමින් දාම විශ්ලේෂණය ව්‍යාකූල කරයි. පිටතින්, එවැනි ගනුදෙනුව පුද්ගලයින් දෙදෙනෙකු අතර කුඩා CoinJoin ලෙස අර්ථ දැක්විය හැක. නමුත් වාස්තවයෙන්ම, එය ගෙවීමකි. මෙම ක්‍රමය දාම විශ්ලේෂණයේ අනියම්තා ජනනය කරමින්, වරදවා ඇති සලකුණු ද ඇති කරයි.


අපි ආලීස්, බොබ්, සහ බේකර්ගේ උදාහරණයට නැවත යමු. Blockchain හි ගනුදෙනුව මෙසේ පෙනේ:

![stonewall x2 public](assets/en/3.webp)

බාහිර නිරීක්ෂකයෙකු සාමාන්‍ය දාම විශ්ලේෂණ හුරේකාවලට භාරව සිටින විට "ඇලීස් සහ බොබ් කුඩා CoinJoin ක් සිදු කළ අතර, එක් එක් ආදානයක් ලෙස එක් UTXO ක් සහ එක් එක් ප්‍රතිදානයක් ලෙස UTXO දෙකක්" යැයි වැරදි ලෙස තීරණය කළ හැකිය.![misinterpretation stonewall x2](assets/en/4.webp)

මෙම අර්ථකථනය වැරදියි, ඔබ දන්නා පරිදි, UTXO එකක් බේකර්ට යවන ලදී, ඇලීස්ට එකම වෙනස්කම් ප්‍රතිදානයක් ඇති අතර, බොබ්ට දෙකක් ඇත.

![transaction stonewall x2](assets/en/1.webp)

Čeprav zunanji opazovalec uspe identificirati vzorec transakcije Stonewall x2, ne bo imel vseh informacij. Ne bo mogel določiti, kateri od dveh UTXO-jev enakih zneskov ustreza plačilu. Poleg tega ne bo mogel vedeti, ali je plačilo izvedla Alice ali Bob. Nazadnje, ne bo mogel določiti, ali dva vhodna UTXO-ja prihajata od dveh različnih oseb ali če pripadata eni osebi, ki ju je združila. Ta zadnja točka je posledica dejstva, da klasične transakcije Stonewall, o katerih smo govorili zgoraj, sledijo popolnoma enakemu vzorcu kot transakcije Stonewall x2. Od zunaj in brez dodatnih informacij o kontekstu je nemogoče razlikovati transakcijo Stonewall od transakcije Stonewall x2. Vendar pa prve niso kolaborativne transakcije, medtem ko druge so. To dodaja še več dvomov o tem izdatku.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)



## Paynyms අතර සම්බන්ධතාවයක් ස්ථාපිත කර Soroban හරහා සහයෝගයෙන් කටයුතු කිරීමට කෙසේද?


සමූහ (*Cahoots*) ගනුදෙනු වලට සමානව, Stonewall x2 ක්‍රියාවලියක් සිදු කිරීම සඳහා Exchange ක්‍රියාවලියක් අවශ්‍ය වේ, එය යවන පුද්ගලයා සහ සහකරු අතර අර්ධව අත්සන් කළ ගනුදෙනු සඳහා වේ. ඔබේ සහකරු සමඟ භෞතිකව සිටින විට මෙම Exchange ක්‍රියාවලිය අතින් සිදු කළ හැකි අතර, Soroban සන්නිවේදන ප්‍රොටෝකෝලය හරහා ස්වයංක්‍රීයවද සිදු කළ හැක.


ඔබ දෙවන විකල්පය තෝරා ගන්නේ නම්, Stonewall x2 ක්‍රියාත්මක කිරීමට පෙර Paynyms අතර සම්බන්ධතාවයක් ස්ථාපිත කළ යුතුය. මෙය කිරීමට, ඔබේ Paynym එක, ඔබේ සහකරුගේ Paynym එක "අනුගමනය" කළ යුතු අතර, එය විරුද්ධවද සිදු විය යුතුය.


**සහකරුගේ Paynym වෙත ප්‍රවේශ වීම:**


ආරම්භ කිරීමට, ඔබේ සහකරුගේ Paynym හි ගෙවීම් කේතය ලබා ගැනීම අවශ්‍ය වේ. Samourai Wallet යෙදුමේ, ඔබේ සහකරු තම Paynym (කුඩා රොබෝව) අයිකනය තිරයේ ඉහළ වම් පැත්තේ පිහිටා ඇති තැන ඔබන්න, එවිට `+...` සමඟ ආරම්භ වන තම Paynym නාමය ක්ලික් කරන්න. උදාහරණයක් ලෙස, මගේ එක `+namelessmode0aF` වේ.


![samourai paynym](assets/notext/6.webp)

Če vaš sodelavec uporablja Sparrow Wallet, naj klikne na zavihek 'Orodja', nato na 'Prikaži PayNym'.![paynym sparrow](assets/notext/7.webp)

**Samourai Wallet සිට ඔබේ සහකරුගේ PayNym අනුගමනය කිරීම:**


Če uporabljate Samourai Wallet, zaženite aplikacijo in na enak način dostopite do menija 'PayNyms'. Če prvič uporabljate svoj PayNym, boste morali pridobiti njegov identifikator.


![request paynym samourai](assets/notext/8.webp)


එවිට තිරයේ දකුණු පහළ කොනේ ඇති නිල් '+' මත ක්ලික් කරන්න.

![add collaborator paynym](assets/notext/9.webp)

ඔබට පසුව 'PASTE PAYMENT CODE' තෝරාගෙන ඔබේ සහකරුගේ ගෙවීම් කේතය අලවිය හැක, හෝ 'SCAN QR CODE' ඔබා ඔවුන්ගේ QR කේතය ස්කෑන් කිරීමට කැමරාව විවෘත කළ හැක.

![paste paynym identifier](assets/notext/10.webp)


'FOLLOW' බොත්තම මත ක්ලික් කරන්න.

![follow paynym](assets/notext/11.webp)

'YES' මත ක්ලික් කිරීමෙන් තහවුරු කරන්න.

![confirm follow paynym](assets/notext/12.webp)

එවිට මෘදුකාංගය ඔබට 'CONNECT' බොත්තමක් ලබා දෙනු ඇත. අපගේ උපකාරිකාව සඳහා මෙම බොත්තම ක්ලික් කිරීම අවශ්‍ය නොවේ. මෙම පියවර අපගේ උපකාරිකාවට අදාළ නොවන BIP47 හි කොටසක් ලෙස වෙනත් PayNym වෙත ගෙවීම් කිරීමට ඔබ සැලසුම් කරන්නේ නම් පමණක් අවශ්‍ය වේ.

![connect paynym](assets/notext/13.webp)

ඔබේ PayNym ඔබේ සහකරුගේ PayNym අනුගමනය කරන විට, ඔබේ සහකරුටද ඔබ අනුගමනය කළ හැකි වන පරිදි මෙම ක්‍රියාවලිය විරුද්ධ දිශාවෙන් නැවත කරන්න. එවිට ඔබට Stonewall x2 ගනුදෙනුවක් සිදු කළ හැක.


**ඔබේ සහකරුගේ PayNym Sparrow Wallet වෙතින් අනුගමනය කිරීම:**


ඔබ Sparrow Wallet භාවිතා කරන්නේ නම්, ඔබේ Wallet විවෘත කර 'Show PayNym' මෙනුවට ප්‍රවේශ වන්න. ඔබේ PayNym පළමු වරට භාවිතා කරන්නේ නම්, 'Retrieve PayNym' ක්ලික් කිරීමෙන් හඳුනාගැනීමක් ලබා ගැනීමට ඔබට අවශ්‍ය වේ.

![request paynym sparrow](assets/notext/14.webp)

ඉන්පසු ඔබේ සහකරුගේ PayNym හඳුනාගැනීමේ සංකේතය (ඔවුන්ගේ නික්නේම් '+...' හෝ ඔවුන්ගේ ගෙවීම් කේතය 'PM...') 'Contact සොයන්න' කොටුවේ ඇතුළත් කරන්න, සහ 'Contact එකතු කරන්න' බොත්තම මත ක්ලික් කරන්න.

![add contact paynym](assets/notext/15.webp)

එවිට මෘදුකාංගය ඔබට 'Link Contact' බොත්තමක් ලබා දෙනු ඇත. අපගේ උපකාරිකාව සඳහා මෙම බොත්තම ක්ලික් කිරීම අවශ්‍ය නොවේ. මෙම පියවර BIP47 හි කොටසක් ලෙස සඳහන් PayNym වෙත ගෙවීම් කිරීමට ඔබ සැලසුම් කරන්නේ නම් පමණක් අවශ්‍ය වේ, එය අපගේ උපකාරිකාවට අදාළ නොවේ.


ඔබේ PayNym ඔබේ සහකරුගේ PayNym අනුගමනය කරන විට, ඔබේ සහකරුට ද ඔබ අනුගමනය කළ හැකි වන පරිදි මෙම ක්‍රියාවලිය විරුද්ධ දිශාවෙන් නැවත කරන්න. එවිට ඔබට Stonewall x2 ගනුදෙනුවක් සිදු කළ හැක.

## Kako narediti transakcijo Stonewall x2 na Samourai Wallet?


Če ste zaključili prejšnje korake povezovanja Paynyms, ste končno pripravljeni na izvedbo transakcije Stonewall x2! Če želite to narediti, sledite našemu video vodiču na Samourai Wallet:

![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)


## Kako narediti transakcijo Stonewall x2 na Sparrow Wallet?


Če ste zaključili prejšnje korake povezovanja Paynyms, ste končno pripravljeni na izvedbo transakcije Stonewall x2! Če želite to narediti, sledite našemu video vodiču na Sparrow Wallet:

![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)


**බාහිර සම්පත්:**


- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.