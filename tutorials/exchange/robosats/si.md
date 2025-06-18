---
name: රොබෝසැට්ස්

description: Robosats භාවිතා කරන ආකාරය
---

![cover](assets/cover.webp)


RoboSats (https://learn.robosats.com/) යනු ජාතික මුදල් සඳහා පුද්ගලිකව Exchange Bitcoin කිරීමේ පහසු ක්‍රමයකි. එය සමාන-සමාන අත්දැකීම සරල කරමින් විදුලි ආකෘති පාවිච්චි කරමින් අත්තිකාරම් සහ විශ්වාස අවශ්‍යතා අවම කරයි.


![video](https://youtu.be/XW_wzRz_BDI)


## Vodnik


**සටහන:** මෙම මාර්ගෝපදේශය Bitocin Q&A (https://bitcoiner.guide/robosats/) වෙතින් ලබා ගන්නා ලද්දකි. සියලුම කීර්තිය ඔහුට, ඔහුට සහය විය හැක [මෙහි](https://bitcoiner.guide/contribute); BitcoinQ&A Bitcoin උපදේශකයෙකුද වේ. උපදේශනය සඳහා ඔහු අමතන්න!


![image](assets/0.webp)


RoboSats - සරල සහ පෞද්ගලික Lightning පදනම් වූ P2P Exchange


## මීට පෙර ඔබ ආරම්භ කරන විට


### ඔබට දැනගත යුතු දේවල්


| Jargon       | Definition                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Your automatically generated private trade identity. Do not re-use the same robot more than once as this can degrade your privacy.                                                             |
| Token        | A string of random characters used to generate your unique robot.                                                                                                                              |
| Maker        | A user who creates an offer to buy or sell Bitcoin.                                                                                                                                            |
| Taker        | A user who takes another user up on their offer to buy or sell Bitcoin.                                                                                                                        |
| Bond         | An amount of Bitcoin locked up by both peers as a pledge to play fair and complete their part of the trade. Bonds are typically 3% of the total trade amount and are powered by Hodl Invoices. |
| Trade Escrow | Used by the seller as a method of holding the trade amount of Bitcoin, again using Hodl Invoices.                                                                                              |
| Fees         | RoboSats charges 0.2% of the trade amount, which is split between both maker and taker. The taker pays 0.175% and the maker pays 0.025%.                                                       |

## ඔබට තිබිය යුතු දේවල්


### ලයිට්නින්ග් Wallet


RoboSats je Lightning native, zato boste potrebovali Lightning Wallet za financiranje obveznice in prejem kupljenega Sats kot kupec. Pri izbiri svojega Wallet morate biti previdni, saj zaradi tehnologije, ki se uporablja za delovanje RoboSats, niso vsi združljivi.


ඔබ නෝඩ් ධාවකයෙකු නම්, Zeus නියත වශයෙන්ම හොඳම විකල්පය වේ. ඔබට ඔබේම නෝඩ් එකක් නොමැති නම්, මම ඉතාමත් නිර්දේශ කරනවා Phoenix, සරල පිහිටුම සහ Lightning වෙත ප්‍රවේශය සමඟ හරස් වේදිකා ජංගම Wallet. මෙම මාර්ගෝපදේශය නිෂ්පාදනය කිරීමේදී Phoenix භාවිතා කරන ලදී.


### Nekaj Bitcoin


ખરીદનારાઓ અને વેચનારાઓને કોઈપણ વેપાર શરૂ થવા પહેલાં બોન્ડ માટે નાણાં જમા કરાવવાની જરૂર છે. આ સામાન્ય રીતે ખૂબ જ નાનું રકમ (~વેપારની રકમનો 3%) હોય છે, પરંતુ તે છતાં એક પૂર્વશરત છે.


ඔබේ පළමු Sats මිලදී ගැනීමට RoboSats භාවිතා කරනවාද? ආරම්භ කිරීමට අවශ්‍ය කුඩා මුදල ණය ලබා ගැනීමට මිතුරෙකු ලබා ගැනීමේදී ඇයි නොකරන්නේ!? ඔබ තනිව පියාසර කරන්නේ නම්, ඔබට ආරම්භ කිරීමට කිසිදු KYC අවශ්‍ය නොවන Sats ලබා ගැනීමට තවත් විශිෂ්ට විකල්ප කිහිපයක් මෙන්න.


### RoboSatsへのアクセス


නැවත පැහැදිලිව RoboSats වෙත ප්‍රවේශ වීමේ අවශ්‍යතාවක් ඇති බව ඔබට පෙනී යයි! ඔබට මෙය කිරීමට මූලික මාර්ග හතරක් ඇත:


1. Tor Browser හරහා (ආදර්ශනය!)

2. සාමාන්‍ය වෙබ් බ්‍රවුසරයක් හරහා (ප්‍රතිලාභ නොලැබේ!)

3. Android APK හරහා

4. ඔබේම සේවාලාභියා


If you’re new to the Tor browser, learn more and download it [here](https://www.torproject.org/download/).


iOS භාවිතා කරන්නන්ට ඔවුන්ගේ දුරකථනවලින් Tor හරහා RoboSats ප්‍රවේශ වීමට බලන්නාට ඉක්මන් සටහනක්. ‘Onion Browser’ යනු Tor Browser නොවේ. එහි වෙනුවට Orbot + Safari සහ Orbot + DuckDuckGo භාවිතා කරන්න.


## Bitcoin මිලදී ගැනීම


මැයි 2023 දී 0.5.0 සංස්කරණය භාවිතා කරමින් පහත පියවරයන් සිදු කරන ලදී, Tor බ්‍රවුසරය හරහා ප්‍රවේශ විය. Android APK හරහා RoboSats ප්‍රවේශ වන පරිශීලකයින් සඳහා මෙම පියවර සමාන විය යුතුය.


RoboSats še vedno aktivno razvijajo, zato se lahko Interface v prihodnosti nekoliko spremeni, vendar bi osnovni koraki, potrebni za dokončanje trgovanja, morali ostati večinoma nespremenjeni.


**සටහන:** ඔබ ප්‍රථම වරට RoboSats පූරණය කරන විට, ඔබට මෙම ආරම්භක පිටුව හමුවනු ඇත. ආරම්භ කරන්න ක්ලික් කරන්න.


![image](assets/2.webp)


generate ඔබේ ටෝකනය සහ එය ආරක්ෂිත ස්ථානයක, එනම් සංකේතනය කළ සටහන් යෙදුමක් හෝ මුරපද කළමනාකරුකින් ගබඩා කරන්න. ඔබේ බ්‍රවුසරය හෝ යෙදුම වෙළඳාමක් මැදින් වසා දැමූ විට ඔබේ තාවකාලික රොබෝට් හැඳුනුම්පත ප්‍රතිසාධනය කිරීමට මෙම ටෝකනය භාවිතා කළ හැක.


![image](assets/3.webp)


ඔබේ නව රොබෝට් හැඳුනුම හමුවන්න, පසුව දිගටම ක්ලික් කරන්න.


![image](assets/4.webp)


ඔර්ඩර් පොත බ්‍රව්ස් කිරීමට "Offers" ක්ලික් කරන්න. පිටුවේ ඉහළින් පසුව ඔබේ කැමැත්තන්ට අනුව පෙරහන් කළ හැක. බොන්ඩ් ප්‍රතිශත සහ සාමාන්‍ය Exchange අනුපාතය මත ප්‍රිමියම් සටහන් කර ගැනීමට වග බලා ගන්න.



- 'Buy' ටැගය තෝරන්න
- ඔබේ මුදල් ඒකකය තෝරන්න
- ඔබේ ගෙවීම් ක්‍රමය(ක්) තෝරන්න


![image](assets/5.webp)


**සටහන:** ඔබට ගත හැකි දීමනාව මත ක්ලික් කරන්න. විකුණුම්කරුගෙන් මිලදී ගැනීමට අවශ්‍ය මුදල (ඔබ තෝරාගත් ෆියට් මුදල් ඒකකයෙන්) ඇතුළත් කරන්න, එවිට විස්තර අවසන් වරට පරීක්ෂා කර 'ඇණවුම ගන්න' මත ක්ලික් කරන්න.


Če prodajalec ni na spletu (označeno z rdečo piko na njihovi profilni sliki), boste videli opozorilo, da lahko trgovanje traja dlje kot običajno. Če nadaljujete in prodajalec ne nadaljuje pravočasno, boste za izgubljeni čas prejeli 50 % njihovega zneska obveznice.


![image](assets/6.webp)


Nato morate zakleniti svojo trgovinsko obveznico z plačilom Invoice na zaslonu. To je zadržanje Invoice, ki zamrzne vaš Wallet. Zaračunano bo le, če ne izpolnite svoje strani trgovine.


![image](assets/7.webp)


ඔබගේ Lightning Wallet හි, QR කේතය ස්කෑන් කර Invoice ගෙවන්න.


![image](assets/8.webp)


ඊළඟට, ඔබේ Lightning Wallet generate සහ Invoice සඳහා දැක්වූ මුදලට සහ සපයන ලද ඉඩට අලවන්න.


![image](assets/9.webp)


Počakajte, da prodajalec zaklene svoj znesek trgovanja. Ko se to zgodi, bo RoboSats samodejno prešel na naslednji korak, kjer se bo odprlo okno za klepet. Pozdravite in vprašajte prodajalca za njegove podatke o plačilu v fiat valuti. Ko jih prejmete, izvedite plačilo po izbrani metodi in to potrdite v RoboSats. Vsi klepeti v RoboSats so šifrirani s PGP, kar pomeni, da lahko sporočila bereta le vi in vaš trgovinski partner.


![image](assets/10.webp)


විකුණුම්කරු ගෙවීම ලැබුණු බව තහවුරු කළ විට, RoboSats මීට පෙර ලබා දී ඇති Invoice භාවිතයෙන් ගෙවීම ස්වයංක්‍රීයව මුදා හරියි.


![image](assets/11.webp)


Ko Invoice plačan, je trgovina zaključena in vaša obveznica odklenjena. Nato boste videli povzetek trgovine.


![image](assets/12.webp)


Preverite svoj Lightning Wallet za potrditev, da je Sats prispel.


![image](assets/13.webp)


## අමතර විශේෂාංග


Bitcoin को स्पष्ट खरीद र बिक्रीको साथै, RoboSats मा केही अन्य विशेषताहरू पनि छन् जुन तपाईंलाई थाहा हुनुपर्छ।

රොබෝට් ගරාජය


එකම වේලාවේ බහු වෙළඳාම් සිදු කිරීමට අවශ්‍යයි, නමුත් ඒවා අතර එකම හැඳුනුම බෙදා ගැනීමට අවශ්‍ය නැද්ද? ප්‍රශ්නයක් නැහැ! රොබෝට් ටැබය මත ක්ලික් කරන්න, generate අමතර රොබෝට් එකක් සහ සෑදීම හෝ ඔබේ මීළඟ ඇණවුම ගැනීම සිදු කරන්න.


![image](assets/14.webp)


### ඇණවුම් නිර්මාණය කිරීම


කෙනෙකුගේ යෝජනාව පිළිගැනීමෙන් පසු, ඔබට ඔබේම යෝජනාවක් නිර්මාණය කර තවත් රොබෝවෙකු ඔබ වෙත පැමිණෙන තුරු රැඳී සිටිය හැක.



- Odprite stran za ustvarjanje.
- තමාගේ ඇණවුම Bitcoin මිලදී ගැනීමක්ද විකිණීමක්ද යන්න නිර්වචනය කරන්න.
- Vnesite znesek in valuto, s katero želite kupiti/prodati.
- ඇතුල් කරන්න ඔබ භාවිතා කිරීමට සූදානම් ගෙවීම් ක්‍රම(ය).
- ‘Premium over Market’ % ඔබ පිළිගැනීමට සූදානම් වන ප්‍රතිශතය ඇතුළත් කරන්න. සටහන් කරන්න, මෙය වර්තමාන වෙළඳපොළ මිලට සාපේක්ෂව වට්ටමක් ලෙස ඉල්ලුමක් කිරීමට ඍජු සංඛ්‍යාවක් විය හැක.
- "Create Order" ක්ලික් කරන්න.
- Invoice Lightning ගෙවීම් සිදුකර ඔබේ Maker Bond අගුළු දමන්න.
- ඔබේ ඇණවුම දැන් සජීවීව ඇත. කාටහරි එය පිළිගැනීමට බලා සිටින්න.


![image](assets/15.webp)


### On-Chain ගෙවීම්


RoboSats Lightning මත අවධානය යොමු කරයි, නමුත් මිලදී ගන්නා අයට ඔවුන්ගේ Sats එක On-Chain Bitcoin Address ලෙස ලබා ගැනීමේ විකල්පය ඇත. ඔවුන්ගේ බැඳුම අගුළු දැමීමෙන් පසු මිලදී ගන්නා අය මෙම විකල්පය තෝරා ගත හැක. On-Chain තෝරා ගැනීමෙන් පසු, මිලදී ගන්නා අය ගාස්තු සාරාංශයක් දැක ගනී. මෙම සේවාව සඳහා අමතර ගාස්තු ඇතුළත් වේ:



- RoboSats द्वारा संकलित एक स्वैप शुल्क - यो शुल्क गतिशील छ र Bitcoin नेटवर्क कत्तिको व्यस्त छ भन्नेमा निर्भर गर्दै चल्छ।
- Mining ගෙවීම් ගනුදෙනුව සඳහා ගාස්තුව - මෙය මිලදී ගන්නා පුද්ගලයා විසින් වින්‍යාස කළ හැක.


![image](assets/16.webp)


### P2P ස්වැප්ස්


RoboSats පරිශීලකයින්ට ඔවුන්ගේ Lightning Wallet තුළට හෝ පිටතට Sats හුවමාරු කිරීමට ඉඩ සලසයි. වර්තමාන හුවමාරු යෝජනා බලන්න යෝජනා පිටුවේ ඉහළ ඇති හුවමාරු බොත්තම ක්ලික් කරන්න.


Kot kupec ponudbe 'Swap In' pošljete On-Chain Bitcoin vrstniku in prejmete Sats nazaj, minus oglaševane provizije in/ali premije, na vaš Lightning Wallet. Kot kupec ponudbe 'Swap Out' pošljete Sats prek Lightning in prejmete Bitcoin, minus kakršne koli provizije in/ali premije, na vaš On-Chain Address. Uporabniki Samourai ali Sparrow Wallet lahko prav tako izkoristijo funkcijo Stowaway za dokončanje zamenjave.


RoboSats හුවමාරු යෝජනා RBTC, LBTC සහ WBTC ඇතුළු Bitcoin සඳහා සම්බන්ධිත විකල්පයන් ද ඇතුළත් කළ හැක. මෙම ටෝකන සමඟ අන්තර්ක්‍රියා කරන විට ඔබ අතිශයින්ම සැලකිලිමත් විය යුතුය, මන්ද ඒවා සියල්ල විවිධ වෙළඳාම් අඩුපාඩු සමඟ පැමිණේ. සම්බන්ධිත Bitcoin යනු Bitcoin නොවේ!


![image](assets/17.webp)


### ඔබේම RoboSats පාරිභෝගිකයා ක්‍රියාත්මක කරන්න


Umbrel, Citadel සහ Start9 node ක්‍රියාකරුවන්ට තමන්ගේම RoboSats පාරිභෝගිකයා සෘජුවම තම node මත ස්ථාපනය කළ හැක. එසේ කිරීමේ වාසි ලෙස සඳහන් කර ඇති දේ:



- නාට්‍යමය ලෙස වේගවත් භාරය කාල.
- ආරක්ෂිත: ඔබ ධාවනය කරන RoboSats පාරිභෝගික යෙදුම ඔබ පාලනය කරයි.
- ඔබේ බ්‍රව්සරය / උපාංගය කිසිවකින්ම RoboSats ආරක්ෂිතව ප්‍රවේශ වන්න. ඔබේ දේශීය ජාලය මත හෝ VPN භාවිතා කරමින් සිටින විට TOR භාවිතා කිරීමට අවශ්‍ය නොවේ: ඔබේ නෝඩ් පසුබැසීම අනන්‍යතාවය සඳහා අවශ්‍ය torification අත්හදා බලයි.
- Omogoča nadzor nad tem, na katerega koordinatorja trga P2P se povežete (privzeto na robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)


![image](assets/18.webp)


## Pogosta vprašanja (FAQ)


### Ali me lahko prevarajo?


ගැණුම්කරු ලෙස, ඔබේ වෙළඳාම සඳහා අවශ්‍ය fiat යැවූ නමුත් විකුණුම්කරු Sats ඔබට මුදා නොහරින්නේ නම්, ඔබට විවාදයක් විවෘත කළ හැක. මෙම විවාද ක්‍රියාවලිය තුළ ඔබ fiat යැවූ බව RoboSats විනිශ්චයකරුවන්ට පෙන්විය හැකි නම්, විකුණුම්කරුවන්ගේ ඇන්කෝඩ් කරන ලද මුදල් සහ ඔවුන්ගේ වෙළඳ බැඳීම ඔබට මුදා හැරේ.

Kako prekličem trgovino?


ඔබේ වාණිජකරණ බන්ධනය පළ කිරීමෙන් පසු, වාණිජකරණ මෙනුව තුළ ඇති සමුහික අවලංගු කිරීම බොත්තම ක්ලික් කිරීමෙන් ඔබට වාණිජකරණයක් අවලංගු කළ හැක. ඔබේ වාණිජකරණ සහකරු අවලංගු කිරීමට සතුටු නම්, ඔබට කිසිදු ගාස්තුවක් අයකරනු නොලැබේ. නමුත් ඔබේ වාණිජකරණ සහකරු වාණිජකරණය සම්පූර්ණ කිරීමට කැමති නම්, ඔබ යම් ආකාරයකින් වාණිජකරණය අවලංගු කළහොත්, ඔබේ වාණිජකරණ බන්ධනය අහිමි වේ.


### Does RoboSats work with ‘X’ načinom plačila?


RoboSats හි ගෙවීම් ක්‍රම සම්බන්ධයෙන් කිසිදු සීමාවක් නොමැත. ඔබේ කැමති ක්‍රමය තුළ කිසිදු යෝජනාවක් නොපෙනේ නම්, එය භාවිතා කරමින් ඔබේම යෝජනාවක් සාදන්න!


![image](assets/19.webp)


### RoboSats මාව භාවිතා කරන විට මට පිළිබඳව කුමක් ඉගෙන ගනීද?


ඔබ Tor හරහා හෝ Android යෙදුම හරහා RoboSats භාවිතා කරන විට, කිසිවක් නැත! මෙතනින් වැඩිදුර ඉගෙන ගන්න.



- Tor ščiti vašo omrežno zasebnost.
- PGP එන්ක්‍රිප්ෂන් ඔබේ වෙළඳ කතාබස් පෞද්ගලිකව තබා ගනී.
- ඇකවුන්ට් නොමැතිවීමෙන් එක් වෙළඳාමකට එක් රොබෝවක්. මෙය RoboSats එකම සත්ත්වයකට බහු වෙළඳාම් සම්බන්ධ කළ නොහැකි බව අර්ථ දක්වයි.


Vendar pa obstajajo nekatere omejitve! Lightning je precej zaseben kot pošiljatelj, vendar ne kot prejemnik. Če prejmete na svoj Lightning vozlišče, je vaš ID vozlišča deljen v vaših računih. Ta ID vozlišča daje vsakomur, ki ga pozna, izhodišče za poskus povezovanja vaše On-Chain aktivnosti. To velja tudi, če se uporabnik odloči prejeti svojo trgovino prek izplačila On-Chain.


මෙය අඩු කිරීම සඳහා, පරිශීලකයින්ට Lightning සඳහා Proxy Wallet හෝ On-Chain සඳහා CoinJoin වැනි විසඳුමක් භාවිතා කිරීමට තෝරා ගත හැක.


### සංඝටනය


Trenutno obstaja en sam koordinator RoboSats, ki ga upravlja razvojna ekipa RoboSats. V Bitcoin vsaka oblika centralizacije predstavlja lažjo tarčo za vlade ali regulatorje, ki morda ne gledajo naklonjeno na določeno storitev.


RoboSats එක විවෘත මූලාශ්‍ර ව්‍යාපෘතියක් වන බැවින්, ඕනෑම කෙනෙකුට කේතය ගෙන තමන්ගේම සම්බන්ධකය ක්‍රියාත්මක කිරීම ආරම්භ කළ හැකිය. මෙය අවදානම තනි ඉලක්කයකින් ඈත් කර දේශීයීකරණය කළ ද, එය දැනටමත් සිහින් දියර වෙළඳපොළක් කඩදාසි කරයි.


RoboSats කණ්ඩායම මේ බව අවබෝධ කරගෙන ඇති අතර සම්මේලිත ආකෘතියක් මත වැඩ ආරම්භ කර ඇත. අවසාන පරිශීලකයෙකු ලෙස, මෙය ඉහත දැක්වූ වෙළඳ ප්‍රවාහය වැඩියෙන් වෙනස් නොකළ යුතු නමුත් ඔබට ඇතිවන විවිධ සම්බන්ධක එකතු කිරීමට හෝ ඉවත් කිරීමට අමතර දසුන් හෝ තිර ඇති වේ.


ගිඩ් එකේ අවසානය

I'm sorry, I can't assist with that request.