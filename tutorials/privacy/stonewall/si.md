---
name: Stonewall
description: Stonewall ගනුදෙනු අවබෝධ කර ගැනීම සහ භාවිතා කිරීම
---
![cover stonewall](assets/cover.webp)


***අවවාදය:** Samourai Wallet ආරම්භකයින් අත්අඩංගුවට ගෙන ඔවුන්ගේ සේවාදායකයන් අප්‍රේල් 24 වන දින අත්පත් කර ගැනීමෙන් පසු, Samourai Wallet යෙදුම නිවැරදිව ක්‍රියාත්මක කිරීමට දැන් ඔබේම Dojo එකකට සම්බන්ධතාවයක් අවශ්‍ය වේ. මෙයට අමතරව, Stonewall ගනුදෙනු කිසිදු බලපෑමකට ලක් නොවන අතර කිසිදු ගැටළුවකින් තොරව තවමත් සිදු කළ හැක. ඇත්ත වශයෙන්ම, මෙම වර්ගයේ ගනුදෙනු ස්වයංක්‍රීයව සිදු කරනු ලබන අතර, Soroban හරහා බාහිර සහයෝගය හෝ සම්බන්ධතාවයක් අවශ්‍ය නොවේ.*


_අපි මෙම නඩුවේ සංවර්ධන මෙන්ම සම්බන්ධ මෙවලම් සම්බන්ධ සංවර්ධන ආසන්නයෙන් අනුගමනය කරමින් සිටිමු. නව තොරතුරු ලබා ගත හැකි වන විට මෙම උපකාරකය යාවත්කාලීන කරන බව විශ්වාස කරන්න._


_මෙම උපකාරිකාව අධ්‍යාපනික සහ තොරතුරුමය අරමුණු සඳහා පමණක් සපයනු ලැබේ. අපි මෙම මෙවලම් අපරාධමය අරමුණු සඳහා භාවිතා කිරීම අනුමත නොකරන අතර හුරුන් නොදෙමු. තමන් පදිංචි ප්‍රදේශයේ නීති පිළිපැදීමේ වගකීම සෑම පරිශීලකයෙකුගේම වගකීමයි._


---

> *Blockchain විශ්ලේෂණයේ උපකල්පන මතකම් කඩන්න, ඔබේ ගනුදෙනු වල යවන්නා සහ ලැබන්නා අතර ගණිතමය සනාථ කළ හැකි සැකයක් සමඟ.*

## Stonewall ගනුදෙනුවක් කුමක්ද?

Stonewall je posebna oblika transakcije Bitcoin, namenjena povečanju zasebnosti uporabnika med transakcijo, tako da posnema CoinJoin med dvema strankama, ne da bi to dejansko bila. Pravzaprav ta transakcija ni sodelovalna. Uporabnik jo lahko sestavi sam, pri čemer kot vhodne podatke uporabi le svoje UTXO-je. Zato lahko ustvarite Stonewall transakcijo za katero koli priložnost, ne da bi se morali usklajevati z drugim uporabnikom.


Stonewall ගනුදෙනුවක් ක්‍රියාත්මක වන්නේ මෙසේය: ආදානය ලෙස, යවන පුද්ගලයාට අයත් UTXO 2ක් භාවිතා කරයි. ප්‍රතිදානය ලෙස, ගනුදෙනුව ප්‍රතිදාන 4ක් නිපදවයි, ඒ අතරින් 2ක් සම්පූර්ණයෙන්ම එකම මුදලක් වනු ඇත. අනෙක් 2ක් වෙනසක් වනු ඇත. එකම මුදලක් වන ප්‍රතිදාන 2 අතරින්, එකක් පමණක් සත්‍යයෙන්ම ගෙවීම් ලැබුණු පුද්ගලයාට යනු ඇත.


Stonewall ගනුදෙනුවක කාර්යභාර 2ක් පමණක් ඇත:


- පිවිසුම්කරු, සැබෑ ගෙවීම සිදු කරන පුද්ගලයා;
- ප්‍රතිලාභකයා, කුමන විශේෂිත ස්වභාවයක් ඇති ගනුදෙනුවක්ද යන්න නොදැනුවත් විය හැකි අතර, එවකයාගෙන් ගෙවීමක් බලාපොරොත්තු වනු ඇත.


මෙම ගනුදෙනු ව්‍යුහය තේරුම් ගැනීම සඳහා උදාහරණයක් ගනිමු. ඇලීස් ඇයගේ බගට් මිලදී ගැනීමට බේකරි වෙත ගොස් ඇත, එය `4,000 Sats` වියදම් වේ. ඇය ඇයගේ ගෙවීමේදී නිරිතරතාවයක් පවත්වාගෙන යමින් බිට්කොයින් වලින් ගෙවීමට කැමතියි. එබැවින්, ඇය ගෙවීම සඳහා ස්ටෝන්වෝල් ගනුදෙනුවක් නිර්මාණය කිරීමට තීරණය කරයි.

![transaction stonewall bakery](assets/en/1.webp)

මෙම ගනුදෙනුව විශ්ලේෂණය කිරීමේදී, අපට දැකගත හැකිය බේකර්ට බාගට් එක සඳහා ගෙවීමක් ලෙස `4,000 Sats` ලැබී ඇති බව. ඇලීස් 2 UTXOs ආදාන ලෙස භාවිතා කළාය: එකක් `10,000 Sats` සහ එකක් `15,000 Sats`. ප්‍රතිදානය ලෙස, ඇය ලබා ගත්තේ 3 UTXOs: එකක් `4,000 Sats`, එකක් `6,000 Sats`, සහ එකක් `11,000 Sats`. මෙම ගනුදෙනුවේදී ඇලීස්ගේ ශුද්ධ ශේෂය `-4,000 Sats` වන අතර, එය බාගට් එකේ මිලට සමාන වේ.


මෙම උදාහරණයේදී, මම හිතාමතාම Mining ගාස්තු අත්හැර දැමුවෙමි අවබෝධය පහසු කිරීම සඳහා. වාස්තවිකත්වයේ, ගනුදෙනු ගාස්තු සම්පූර්ණයෙන්ම යවන පුද්ගලයා විසින් ආවරණය කරනු ලබයි.


## Kakšna je razlika med Stonewall in Stonewall x2?

Stonewall ගනුදෙනුව StonewallX2 ගනුදෙනුව මෙන්ම ක්‍රියාත්මක වේ, එකම වෙනස වන්නේ පසුගිය ගනුදෙනුවට සහයෝගය අවශ්‍ය වීමයි, සාම්ප්‍රදායික Stonewall ගනුදෙනුවට වඩා, "x2" නාමකරණය එම නිසාය. ඇත්ත වශයෙන්ම, Stonewall ගනුදෙනුව බාහිර සහයෝගය අවශ්‍ය නොවී ක්‍රියාත්මක කළ හැක: යවන්නාට එය වෙනත් පුද්ගලයෙකුගේ සහය නොමැතිව සිදු කළ හැක. කෙසේ වෙතත්, Stonewall x2 ගනුදෙනුව සඳහා, "සහයෝගිකයා" ලෙස හැඳින්වෙන අමතර සහභාගිවෙකු, ක්‍රියාවලියට එක් වේ. සහයෝගිකයා තමන්ගේම බිට්කොයින් යවන්නාගේ බිට්කොයින් සමඟ ආදානය ලෙස දායක කරයි, සහ (Mining ගාස්තු අඩු කර) සම්පූර්ණ මුදල ප්‍රතිදානය ලෙස ලබා ගනී.


Poglejmo si še enkrat naš primer z Alice v pekarni. Če bi želela opraviti transakcijo Stonewall x2, bi morala Alice pri ustvarjanju transakcije sodelovati z Bobom (tretjo osebo). Vsak bi zagotovil vhod UTXO. Bob bi nato prejel celoten znesek svojega vhoda kot izhod. Pek bi prejel plačilo za svojo bageto na enak način kot pri transakciji Stonewall, medtem ko bi Alice prejela nazaj svoje začetno stanje, zmanjšano za strošek bagete.

![transaction stonewall x2](assets/en/2.webp)


බාහිර දෘෂ්ටිකෝණයකින්, ගනුදෙනුවේ රටාව සම්පූර්ණයෙන්ම ඒකම තැන රැඳී තිබෙනු ඇත.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)


සාරාංශයෙන්, Stonewall සහ Stonewall x2 ගනුදෙනු සමාන ව්‍යුහයක් බෙදා ගනී. එයින් දෙකේ වෙනස ඔවුන්ගේ සහයෝගී ස්වභාවයයි. Stonewall ගනුදෙනුව තනිවම සංවර්ධනය කරයි, සහයෝගය අවශ්‍ය නොවේ. එයට විරුද්ධව, Stonewall x2 ගනුදෙනුව ක්‍රියාත්මක කිරීමට පුද්ගලයින් දෙදෙනෙකු අතර සහයෝගය මත රඳා පවතී.


[**-> Stonewall x2 ගනුදෙනු පිළිබඳව වැඩිදුරටත් ඉගෙන ගන්න**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)


## Stonewall ගනුදෙනුවක අරමුණ කුමක්ද?

ස්ටෝන්වෝල් ව්‍යුහය ගනුදෙනුවට සාර්වජනිකව entropy එකක් එක් කරමින් දාම විශ්ලේෂණය වසන් කරයි. බාහිර දෘෂ්ටිකෝණයකින්, එවැනි ගනුදෙනුවක් පුද්ගලයින් දෙදෙනෙකු අතර කුඩා CoinJoin ලෙස අර්ථ දැක්විය හැක. නමුත් වාස්තු විද්‍යාත්මකව, ස්ටෝන්වෝල් x2 ගනුදෙනුව මෙන්ම, එය ගෙවීමකි. එබැවින් මෙම ක්‍රමය දාම විශ්ලේෂණයේ අනියම්තා නිර්මාණය කරයි, සහ වරදවා ඇති සලකුණු වලට පවා හේතු විය හැක.


Ponovno si oglejmo Alicin primer v pekarni. Transakcija na Blockchain bi bila prikazana takole:

![Stonewall or Stonewall x2 ?](assets/en/4.webp)

බාහිර නිරීක්ෂකයෙකු සාමාන්‍ය දාම විශ්ලේෂණ හුරේකාවලට භාරව සිටින විට "*මිනිසුන් දෙදෙනෙකු කුඩා CoinJoin ක් සිදු කර ඇති අතර, එක් UTXO ක් බැගින් ආදානයක් ලෙස සහ UTXOs දෙක බැගින් ප්‍රතිදානයක් ලෙස ඇත*" යැයි වැරදි ලෙස නිගමනය කළ හැකිය.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)

මෙම අර්ථකථනය වැරදියි, ඔබ දන්නා පරිදි, UTXO එක බේකර්ට යවන ලදී, ආදානයේ ඇති UTXO 2 ක් ඇලීස්ගෙන් පැමිණි අතර, ඇය වෙනස්කම් පිටවීම් 3 ක් ලබා ගත්තේය.


![transaction stonewall baker](assets/en/1.webp)

ආසන්න පරිවේක්ෂකයෙකුට Stonewall ගනුදෙනුවේ රටාව හඳුනා ගැනීමට හැකි වුවත්, ඔවුන්ට සියලුම තොරතුරු නොමැත. එකම මුදල් ප්‍රමාණයේ UTXO දෙකෙන් කුමක් ගෙවීම සඳහා අදාල වේද යන්න ඔවුන්ට තීරණය කළ නොහැක. තවද, ආදානයේ UTXO දෙක වෙන වෙනම පුද්ගලයින් දෙදෙනෙකුගෙන් පැමිණිද, නැතහොත් ඒවා එක් පුද්ගලයෙකුට අයත්ද යන්න ඔවුන්ට තීරණය කළ නොහැක. මෙම අවසාන කරුණ, අපි ඉහත කතා කළ Stonewall x2 ගනුදෙනු, Stonewall ගනුදෙනු ලෙසම රටාවක් අනුගමනය කරන බැවින් වේ. පිටත සිට සහ පරිසරය පිළිබඳ අමතර තොරතුරු නොමැතිව, Stonewall ගනුදෙනුවක් Stonewall x2 ගනුදෙනුවක්ද යන්න වෙනස් කිරීමට නොහැක. කෙසේ වෙතත්, පළමු ඒවා සහයෝගී ගනුදෙනු නොවේ, නමුත් දෙවන ඒවා වේ. මෙය මෙම වියදම පිළිබඳ තවත් සැකයක් එක් කරයි.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)

## Kako izvesti transakcijo Stonewall na Samourai Wallet?

Stowaway හෝ Stonewall x2 (cahoots) ගනුදෙනු වලට වඩා, Stonewall ගනුදෙනුව සඳහා Paynyms භාවිතා කිරීම අවශ්‍ය නොවේ. එය සෘජුවම, කිසිදු සූදානම් කිරීමේ පියවරකින් තොරව කළ හැක. මෙය කිරීමට, Samourai Wallet පිළිබඳ අපගේ වීඩියෝ උපකාරකය අනුගමනය කරන්න:

![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)


## Kako opraviti transakcijo Stonewall na Sparrow Wallet?

Stowaway හෝ Stonewall x2 (cahoots) ගනුදෙනු වලට වඩා, Stonewall ගනුදෙනුව සඳහා Paynyms භාවිතා කිරීම අවශ්‍ය නොවේ. එය සෘජුවම, කිසිදු සූදානම් කිරීමේ පියවරකින් තොරව කළ හැක. මෙය කිරීමට, Sparrow Wallet පිළිබඳ අපගේ වීඩියෝ උපකාරකය අනුගමනය කරන්න:

![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)



**බාහිර සම්පත්:**


- https://docs.samourai.io/en/spend-tools#stonewall.