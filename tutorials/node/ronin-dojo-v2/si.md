---
name: RoninDojo v2
description: ඔබේ RoninDojo v2 Bitcoin නියමකරු Raspberry Pi මත ස්ථාපනය කිරීම
---
![cover RoninDojo v2](assets/cover.webp)


***අවවාදය:** Samourai Wallet හි ආරම්භකයින් අත්අඩංගුවට ගැනීම සහ ඔවුන්ගේ සේවාදායකයන් අප්‍රේල් 24 වන දින අත්පත් කර ගැනීමත් සමඟ, RoninDojo හි Whirlpool වැනි විශේෂාංග කිහිපයක් දැන් ක්‍රියාත්මක නොවේ. කෙසේ වෙතත්, මෙම මෙවලම් නැවත ස්ථාපිත කිරීම හෝ වෙනස්ව නැවත ආරම්භ කිරීම ඉදිරි සති කිහිපය තුළ සිදුවිය හැක. තවද, RoninDojo කේතය Samourai ගිට්ලෑබ් හි සත්කාරකත්වය ලබා ඇති බැවින්, එය ද අත්පත් කරගෙන ඇති බැවින්, දුරස්ථව කේතය බාගත කිරීම මේ වන විට නොහැක. RoninDojo කණ්ඩායම් කේතය නැවත ප්‍රකාශයට පත් කිරීමේ වැඩපිළිවෙලේ නිරත විය හැක.*


_අපි මෙම නඩුවේ සංවර්ධන මෙන්ම සම්බන්ධිත මෙවලම් සම්බන්ධයෙන් ඇතිවන සංවර්ධන ආසන්නයෙන් අනුගමනය කරමින් සිටිමු. නව තොරතුරු ලබා ගත හැකි වන විට මෙම උපකාරකය යාවත්කාලීන කරන බව විශ්වාසයෙන් කියමු._


_මෙම උපකාරිකාව අධ්‍යාපනික සහ තොරතුරුමය අරමුණු සඳහා පමණක් සපයනු ලැබේ. අපි මෙම මෙවලම් අපරාධමය අරමුණු සඳහා භාවිතා කිරීම අනුමත නොකරන අතර හෝ උත්තේජනය නොකරන අතරේ. තමන්ගේ නීතිමය බල ප්‍රදේශයේ නීති පිළිපැදීමේ වගකීම සෑම පරිශීලකයෙකුගේම වගකීමයි._


---

> Bitcoin සමඟ පෞද්ගලිකත්වය භාවිතා කරන්න.

v prejšnjem vodiču smo že razložili postopek za namestitev in uporabo RoninDojo v1. Vendar so ekipe RoninDojo v zadnjem letu lansirale različico 2 svoje implementacije, kar je pomenilo pomembno prelomnico v arhitekturi programske opreme. Namreč, oddaljili so se od distribucije Linux Manjaro v prid Debianu. Posledično ne ponujajo več vnaprej konfigurirane slike za samodejno namestitev na Raspberry Pi. Kljub temu pa obstaja metoda za ročno namestitev. To sem uporabil za svoj lasten vozlišče in od takrat RoninDojo v2 deluje odlično na mojem Raspberry Pi 4. Zato ponujam nov vodič o tem, kako ročno namestiti RoninDojo v2 na Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## විෂය සටහන:


- RoninDojo kaj je?
- RoninDojo v2 සඳහා ස්ථාපනය කිරීමට කුමන දෘඩාංගය තෝරා ගත යුතුද?
- Raspberry Pi 4 එක එකතු කරන්නේ කෙසේද?
- Kako namestiti RoninDojo v2 na Raspberry Pi 4?
- Kako uporabljati svoj vozlišče RoninDojo v2?


## RoninDojo kaj je?

Dojo je sprva popolna implementacija vozlišča Bitcoin, ki temelji na jedru Bitcoin in jo razvijajo ekipe Samourai Wallet. To rešitev je mogoče namestiti na katero koli opremo. Za razliko od drugih implementacij jedra je Dojo posebej optimiziran za integracijo z okoljem aplikacij za Android Samourai Wallet. Kar zadeva RoninDojo, je to pripomoček, zasnovan za olajšanje namestitve in upravljanja Dojo, pa tudi različnih drugih dopolnilnih orodij. Skratka, RoninDojo obogati osnovno implementacijo Dojo z integracijo številnih dodatnih orodij, hkrati pa poenostavi njegovo namestitev in upravljanje.


Ronin හි "*Tanto*" නම් [node-in-box විසඳුමක්](https://ronindojo.io/en/products) ද ඇත, එය ඔවුන්ගේ කණ්ඩායම විසින් එකතු කරන ලද පද්ධතියක දැනටමත් ස්ථාපනය කර ඇති RoninDojo සමඟ ඇති උපාංගයකි. Tanto යනු ගෙවීම් කළ යුතු විකල්පයක් වන අතර, තාක්ෂණික සංකීර්ණතා වලට මුහුණ දීමට කැමති නොවන අය සඳහා රසවත් විය හැක. නමුත් RoninDojo හි මූලාශ්‍ර කේතය විවෘත වන බැවින්, එය ඔබේම දෘඩාංගය මත යෙදවීම ද සම්භවය. මෙම විකල්පය, වඩා ආර්ථිකමය, එහෙත් අමතර ක්‍රියාකාරකම් කිහිපයක් අවශ්‍ය වන අතර, අපි මෙම උපකාරක පොතේ ඒවා ආවරණය කරමු.

RoninDojo යනු Dojo එකක් වන අතර එය Whirlpool CLI ඔබේ Bitcoin නියුඩ් සමඟ පහසුවෙන් ඒකාබද්ධ කිරීමට ඉඩ සලසයි, හොඳම CoinJoin අත්දැකීම ලබා දීම සඳහා. Whirlpool CLI සමඟ, ඔබේ පුද්ගලික පරිගණකය ක්‍රියාත්මකව තබා ගැනීමට අවශ්‍ය නොවී, ඔබේ බිට්කොයින් නිරන්තරයෙන් නැවත මිශ්‍ර කිරීම, දිනකට පැය 24, සතියේ දින 7 ක්, සිදු කිරීම හැකි වේ.


Whirlpool CLI ට අධිකව, RoninDojo ඔබේ Dojo හි ක්‍රියාකාරකම් වර්ධනය කිරීමට විවිධ මෙවලම් ඇතුළත් කරයි. මෙහි, Boltzmann ගණකය ඔබේ ගනුදෙනු වල පෞද්ගලිකත්ව මට්ටම විශ්ලේෂණය කරයි, Electrum සේවාදායකය ඔබේ Bitcoin පසුම්බි ඔබේ නියැදියට සම්බන්ධ කිරීමට ඉඩ සලසයි, සහ Mempool සේවාදායකය ඔබේ ගනුදෙනු ස්ථානීයව, තොරතුරු හෙළි නොකර, බලන්නට ඔබට ඉඩ සලසයි.


V primerjavi z drugimi rešitvami za vozlišča, kot je Umbrel, je RoninDojo očitno osredotočen na rešitve On-Chain in orodja za zasebnost. Za razliko od Umbrel, RoninDojo ne podpira nastavitve Lightning vozlišča niti integracije bolj splošnih strežniških aplikacij. Čeprav RoninDojo ponuja manj vsestranskih orodij kot Umbrel, ima vse bistvene funkcionalnosti za upravljanje vaše dejavnosti On-Chain.


ඔබට Umbrel විසින් ලබා දෙන Lightning Network සම්බන්ධ හෝ පොදු කාර්යයන් අවශ්‍ය නොවේ නම්, සහ Whirlpool හෝ Mempool වැනි මූලික මෙවලම් සහිත සරල, ස්ථායි නෝඩයක් සොයන්නේ නම්, RoninDojo යනු ඉතා සුදුසු විසඳුමක් විය හැක. Umbrel, Lightning Network සහ බහුකාර්යතාවය දෙසට මිනි මල්ටිටාස්කින් සර්වර් එකක් බවට පත්වන අතර, Samourai Wallet දර්ශනයට අනුකූලව RoninDojo, පරිශීලක පෞද්ගලිකත්වය සඳහා මූලික මෙවලම් මත අවධානය යොමු කරයි.


හෝද, දැන් අපි RoninDojo සටහන් කර ඇති බැවින්, මෙම නියමය සකස් කරන්නේ කෙසේදැයි එකට බලමු.


## RoninDojo v2 සඳහා ස්ථාපනය කිරීමට කුමන දෘඩාංගය තෝරා ගත යුතුද?

RoninDojo ponuja sliko za samodejno namestitev svoje programske opreme na [RockPro64](https://ronindojo.io/en/download). Vendar pa se naš vodič osredotoča na postopek ročne namestitve na Raspberry Pi 4. Čeprav je bil Raspberry Pi 5 nedavno lansiran in bi moral biti ta vodič teoretično združljiv s tem novim modelom, ga še nisem imel priložnosti osebno preizkusiti in nisem našel nobenih povratnih informacij iz skupnosti. Takoj ko pridobim Pi 5 in združljive komponente, bom posodobil ta vodič, da vas obvestim. Medtem priporočam, da dajete prednost Pi 4, saj deluje popolnoma za moj vozlišče.

මගේ කොටස සඳහා, මම 8 GB RAM එකකින් සන්නද්ධ Raspberry Pi මත RoninDojo ක්‍රියාත්මක කරමි. සමහර ප්‍රජා සාමාජිකයින්ට 4 GB RAM පමණක් ඇති උපාංගවල එය ක්‍රියාත්මක කිරීමට හැකි වූ නමුත්, මම මෙම වින්‍යාසය ස්වයං පරීක්ෂා කර නැත. කුඩා මිල වෙනස සැලකිල්ලට ගත් විට, 8 GB RAM අනුවාදය තෝරා ගැනීම බුද්ධිමත් බව පෙනේ. ඔබේ Raspberry Pi අනාගතයේදී වෙනත් භාවිත සඳහා නැවත භාවිතා කිරීමට සැලසුම් කරන්නේ නම් මෙය ප්‍රයෝජනවත් විය හැක.

රොනින්ඩොජෝ කණ්ඩායම් විසින් මෙම සිද්ධිය හා SSD ඇඩැප්ටරය සම්බන්ධයෙන් නිතර ගැටළු වාර්තා කර ඇති බව සලකන්න. මමත් මෙම ගැටළු මුහුණ දී ඇත. **එබැවින්, ඔබේ නෝඩයේ SSD සඳහා USB කේබල් එකක් සමඟ සජ්ජිත කේස් වලින් වළකින්නැයි දැඩිව නිර්දේශ කරනු ලැබේ.** එහි වෙනුවට, ඔබේ රැස්බෙරි පයි සඳහා විශේෂයෙන් නිර්මාණය කරන ලද ගබඩා විශාලකරණ කාඩ්පතක් කැමති වන්න:


![storage expansion card RPI4](assets/notext/1.webp)


Če želite shraniti Bitcoin Blockchain, boste potrebovali SSD, ki je združljiv s kartico za razširitev shranjevanja, ki ste jo izbrali. Trenutno (februar 2024) smo v prehodni fazi. Pričakuje se, da čez nekaj mesecev 1 TB diski ne bodo več zadostovali za vse večjo velikost Blockchain, še posebej glede na različne aplikacije, ki jih nameravate vključiti v svoj vozlišče. Nekateri zato priporočajo vlaganje v 2 TB SSD za mir v duši na dolgi rok. Vendar pa, glede na trend zniževanja cen SSD-jev iz leta v leto, drugi predlagajo, da se zadovoljite z 1 TB diskom, ki bi moral zadostovati za eno ali dve leti, pri čemer trdijo, da bodo do takrat, ko bo postal zastarel, stroški 2 TB modelov verjetno zmanjšani. Izbira je torej odvisna od vaših osebnih preferenc. Če nameravate obdržati svoj RoninDojo za daljše obdobje in želite v prihodnjih letih preprečiti kakršno koli tehnično ravnanje, se zdi možnost 2 TB SSD najbolj preudarna, saj vam ponuja udobno mejo za prihodnost.


අමතරව, ඔබට විවිධ කුඩා සංරචක අවශ්‍ය වනු ඇත:


- රැස්බෙරි පයි සහ ඔබේ ගබඩා විස්තාරණ කාඩ්පත තබා ගැනීමට පංකාවකින් සන්නද්ධ නඩුවක්. SSD විස්තාරණ කාඩ්පත සහ අනුකූල නඩුව දෙකම අඩංගු කට්ටල අන්තර්ජාලයෙන් ලබා ගත හැක;
- Vaš Raspberry Pi napajalni kabel;
- අවම වශයෙන් 16 GB මයික්‍රෝ SD කාඩ්පතක් (8 GB කාඩ්පතක් තාක්ෂණිකව ප්‍රමාණවත් විය හැකි නමුත්, 8 සහ 16 GB කාඩ්පත් අතර මිල වෙනස බොහෝ විට නොසැලකිය හැකි වේ);
- RJ45 ඉතර්නෙට් කේබලයක් ජාල සම්බන්ධතාවය සඳහා.


![node material](assets/notext/2.webp)


## Raspberry Pi 4 එක එකතු කරන ආකාරය කෙසේද?

ඔබේ නෝඩ් එකේ සම්මන්ත්‍රණය තෝරාගත් දෘඩාංගය අනුව වෙනස් වේ, විශේෂයෙන් කේස් වර්ගය අනුව. කෙසේ වෙතත්, සම්මන්ත්‍රණයේ අනුගමනය කළ යුතු පියවරවල පොදු රූපරේඛාව සාමාන්‍යයෙන් සමාන වේ.

ඔබේ SSD එක ගබඩා විස්තාරණ කාඩ්පතට ස්ථාපනය කිරීමෙන් ආරම්භ කරන්න, පසුපස ඇති ලොක් කිරීමේ ත්‍රිවිධ කුරුටු ගැට සුරක්ෂිත කිරීමේදී අවධානයෙන් සිටින්න.


![assembly1](assets/notext/3.webp)


පසුව ඔබේ Raspberry Pi විශාලන කාඩ්පතට සවි කරන්න.


![assembly2](assets/notext/4.webp)


ඉන්ධන පංකාව Raspberry Pi වෙතද සවි කරන්න.


![assembly3](assets/notext/5.webp)


විවිධ සංරචක සම්බන්ධ කර, නිවැරදි පින් භාවිතා කිරීමට අවධානය යොමු කරමින්, ඔබේ කේස් මාර්ගෝපදේශය වෙත යොමු වන්න. කේස් නිෂ්පාදකයින් බොහෝ විට විධානය සඳහා වීඩියෝ උපකාරක පවසා ඇත. මගේ කේස් එකේ, මට මතකය/අක්‍රිය කිරීමේ බොත්තමක් සහිත අමතර විස්තාරණ කාඩ්පතක් ඇත. මෙය Bitcoin නෝඩයක් සාදීමට අත්‍යවශ්‍ය නොවේ. මම මෙය ප්‍රධාන වශයෙන් භාවිතා කරන්නේ විදුලි බොත්තමක් ලබා ගැනීමටයි.


ඔබ මෙන්ම මමත්, මතක තබා ගන්න, ඔබට on/off බොත්තමක් සහිත විස්තාරණ කාඩ්පතක් තිබේ නම්, කුඩා "Auto Power On" ජම්පරය ස්ථාපනය කිරීමට අමතක නොකරන්න. මෙය ඔබේ නියැදිය ස්වයංක්‍රීයව ආරම්භ වීමට ඉඩ සලසයි, එය විදුලි බලය ලබා දුන් වහාම. විශේෂයෙන් විදුලි කප්පාදුවක් සිදුවූ විට මෙම විශේෂාංගය විශේෂයෙන් ප්‍රයෝජනවත් වේ, මන්ද එය ඔබේ නියැදිය ඔබේ අතින් මැනුවල් මැදිහත් වීමකින් තොරව නැවත ආරම්භ කිරීමට ඉඩ සලසයි.


![assembly4](assets/notext/6.webp)


Prejden ko vstavite vso strojno opremo v ohišje, je pomembno preveriti pravilno delovanje vašega Raspberry Pi, kartice za razširitev pomnilnika in ventilatorja tako, da jih vklopite.


![assembly5](assets/notext/7.webp)


අවසානයේ, ඔබේ Raspberry Pi එහි කේස් එක තුළ ස්ථාපනය කරන්න. අවධානයෙන් සිටින්න, පසුව කරන පියවරකදී micro SD කාඩ්පත Raspberry Pi හි සුදුසු පෝට් එකට එක් කිරීමට අවශ්‍ය වනු ඇත. ඔබේ කේස් එක micro SD කාඩ්පත ඇතුළත් කිරීමට විවෘත කිරීමකින් යුක්ත නම් (මගේ ඡායාරූපයේ පෙන්වා ඇති පරිදි), දැන් කේස් එක වසා දැමීමට ඔබට හැකිය. කෙසේ වෙතත්, ඔබේ කේස් එක micro SD පෝට් එකට සෘජු ප්‍රවේශයක් නොමැති නම්, micro SD කාඩ්පත සකස් කර ඇතුළත් කරන තුරු ඔබට රැඳී සිටිය යුතු අතර, එවිට වින්‍යාසය අවසන් කළ හැක.


![assembly6](assets/notext/8.webp)


## Kako namestiti RoninDojo v2 na Raspberry Pi 4?


### 1. korak: බූට් කළ හැකි මයික්‍රෝ SD එක සූදානම් කරන්න

ඔබේ දෘඩාංගය එකතු කිරීමෙන් පසු, ඊළඟ පියවර වන්නේ RoninDojo ස්ථාපනය කිරීමයි. මෙ සඳහා, අපි ඔබේ පරිගණකයෙන් බූට් කළ හැකි මයික්‍රෝ SD කාඩ්පතක් සූදානම් කරමු, එය සඳහා සුදුසු ඩිස්ක් රූපය එය මත දැමීමෙන්.

ඔබට _**Raspberry Pi Imager**_ මෘදුකාංගය භාවිතා කළ යුතු වන අතර, එය Raspberry Pi සමඟ භාවිතා කිරීම සඳහා ක්ෂුද්‍ර SD කාඩ්පතක මෙහෙයුම් පද්ධති බාගත කිරීම, වින්‍යාස කිරීම සහ ලිවීම පහසු කිරීම සඳහා නිර්මාණය කර ඇත. මෙම මෘදුකාංගය ඔබේ පෞද්ගලික පරිගණකයේ ස්ථාපනය කිරීමෙන් ආරම්භ කරන්න:


- Ubuntu/Debian සඳහා: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Windows සඳහා: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Mac සඳහා: https://downloads.raspberrypi.org/imager/imager_latest.dmg


සොෆ්ට්වෙයාර්ය ස්ථාපනය කළ පසු, එය විවෘත කර, ඔබේ පුද්ගලික පරිගණකයට ඔබේ මයික්‍රෝ SD කාඩ්පත ඇතුළත් කරන්න. Raspberry Pi Imager Interface වෙතින්, `CHOOSE OS` තෝරන්න:


![choose OS](assets/notext/9.webp)


ඊළඟට, `Raspberry Pi OS (other)` මෙනුවට යන්න:


![choose OS others](assets/notext/10.webp)


`Raspberry Pi OS (Legacy, 64-bit) Lite` නම් මෙහෙයුම් පද්ධතිය, එය `0.3 GB` විශාලත්වයෙන්:


![choose OS Legacy Lite](assets/notext/11.webp)


ඔපරේටින් පද්ධතිය තෝරා ගැනීමෙන් පසු, ඔබ Raspberry Pi Imager හි ප්‍රධාන මෙනුවට යළි යොමු කෙරේ. `CHOOSE STORAGE` මත ක්ලික් කරන්න:


![choose storage](assets/notext/12.webp)


ඔබේ මයික්‍රෝ SD කාඩ්පත තෝරන්න:


![choose micro sd](assets/notext/13.webp)


මෙහෙයුම් පද්ධතිය සහ මයික්‍රෝ SD කාඩ්පත තෝරාගෙන `NEXT` මත ක්ලික් කරන්න:


![choose next](assets/notext/14.webp)


නව කවුළුවක් පෙනෙනු ඇත. `EDIT CONFIGURATION` තෝරන්න:


![edit settings](assets/notext/15.webp)


මෙම කවුළුවේ, `GENERAL` ටැබය වෙත ගොස් පහත සකසීම් කරන්න (එය ක්‍රියාත්මක වීමට ඉතා වැදගත් වේ):


- විකල්පය සක්‍රීය කර `RoninDojo` ලෙස සත්කාරක නාමය පවරන්න;
- උපයෝග කරන්න `පරිශීලක නාමය සහ මුරපදය සකසන්න`, `pi` ලෙස පරිශීලක නාමය ඇතුළත් කරන්න, මුරපදයක් තෝරන්න, සහ මෙම තොරතුරු සටහන් කර ගන්න, මක්නිසාද එය පසුව අවශ්‍ය වනු ඇත. මෙම අක්තපත්‍ර තාවකාලික වන අතර පසුව මකා දමනු ඇත;
- අක්‍රිය කරන්න `Wi-Fi වින්‍යාස කරන්න`;
- `Set locale settings` omogočite in izberite svoj časovni pas ter vrsto tipkovnice, ki ustreza vašemu računalniku;


![general settings](assets/notext/16.webp)


SERVICES ටැබ් එකේ, `Enable SSH` කොටුව මත ක්ලික් කර `Use a password for authentication` තේරීමක් කරන්න:


![services settings](assets/notext/17.webp)


ඉන් අමතරව, `OPTIONS` ටැබය තුළ, දුරසංවේදනය අක්‍රිය කර ඇති බව සහතික කරන්න:


![options settings](assets/notext/18.webp)


`SAVE` මත ක්ලික් කරන්න:


![settings save](assets/notext/19.webp)

`YES` ක්ලික් කිරීමෙන් බූට් කළ හැකි මයික්‍රෝ SD කාඩ්පත නිර්මාණය කිරීම ආරම්භ කරන්න:

![settings yes](assets/notext/20.webp)


සියලුම දත්ත මයික්‍රෝ SD කාඩ්පතෙන් මකා දැමෙන බව පණිවිඩයක් ඔබට දැනුම් දෙනු ඇත. ක්‍රියාව ආරම්භ කිරීමට `YES` මත ක්ලික් කිරීමෙන් තහවුරු කරන්න:


![overwrite micro SD](assets/notext/21.webp)


පොදු මෘදුකාංගය ඔබේ මයික්‍රෝ SD කාඩ්පත සකස් කිරීම අවසන් කරන තුරු රැඳී සිටින්න:


![writing micro SD](assets/notext/22.webp)


කාර්යය අවසන් වූ බව පෙන්වන පණිවිඩය පෙනෙන විට, ඔබට මයික්‍රෝ SD කාඩ්පත ඔබේ පරිගණකයෙන් ඉවත් කළ හැක:


![writing micro SD completed](assets/notext/23.webp)


### පියවර 2: Node එකේ සම්පූර්ණ සංග්‍රහය සම්පූර්ණ කරන්න

Zdaj lahko vstavite micro SD kartico v ustrezna vrata vašega Raspberry Pi.


![micro SD](assets/notext/24.webp)


පසුව, ඔබේ Raspberry Pi එක ඔබේ රවුටරයට Ethernet කේබලය භාවිතයෙන් සම්බන්ධ කරන්න. අවසානයේ, බල කේබලය සම්බන්ධ කර බල බොත්තම (ඔබේ සැකසුම එකක් ඇතුළත් නම්) ඔබා ඔබේ නෝඩය ක්‍රියාත්මක කරන්න.


### 3. korak: SSH povezavo vzpostavite z vozliščem

පළමුව, ඔබේ නියුඩයේ IP Address සොයා ගැනීම අවශ්‍ය වේ. _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ හෝ _[Angry IP Scanner](https://angryip.org/)_ වැනි මෙවලමක් භාවිතා කිරීමේ විකල්පය ඔබට ඇත, හෝ ඔබේ රවුටරයේ පරිපාලන Interface පරීක්ෂා කරන්න. IP Address `192.168.1.??` ආකාරයේ විය යුතුය. **පහත සියලුම විධාන සඳහා, `[IP]` ඔබේ නියුඩයේ සැබෑ IP Address සමඟ ප්‍රතිස්ථාපනය කරන්න**, (කොටස් ඉවත් කරමින්).**


ටර්මිනල් එකක් ආරම්භ කරන්න.


IP Address සමඟ දැනට සම්බන්ධ වී ඇති සම්භාව්‍ය යතුරක් ඉවත් කිරීමට, විධානය ක්‍රියාත්මක කරන්න:

`ssh-keygen -R [IP]`.


මෙම විධානයට අනුගමනය වන දෝෂයක් බරපතල නොවේ; එය සරලවම ඔබේ හඳුනාගත් සත්කාරක ලැයිස්තුවේ යතුර නොපවතින බව අර්ථ දක්වයි (ඒක ඉතාමත්ම සම්භාව්‍යයි). උදාහරණයක් ලෙස, ඔබේ නියුඩ් එකේ IP එක `192.168.1.40` නම්, විධානය මෙසේ වෙනස් වේ: `ssh-keygen -R 192.168.1.40`.


ඊළඟට, ඔබේ නියුඩ් සමඟ SSH සම්බන්ධතාවයක් ස්ථාපනය කිරීම සඳහා විධානය ක්‍රියාත්මක කරන්න:

`ssh pi@[IP]`.

සත්‍යතාවය පිළිබඳව සත්කාරකයාගේ සත්‍යතාවය පිළිබඳ පණිවිඩයක් පෙනේ: `The authenticity of host '[IP]' can't be established.` මෙය ඔබ සම්බන්ධ වීමට උත්සාහ කරන උපාංගයේ සත්‍යතාවය, හඳුනාගත් මහජන යතුරක් නොමැතිව, සත්‍යතාවය තහවුරු කළ නොහැකි බව පෙන්වයි. නව සත්කාරකයකට පළමු වරට SSH හරහා සම්බන්ධ වීමේදී, මෙම පණිවිඩය සෑම විටම පෙනේ. එහි මහජන යතුර ඔබේ දේශීය නාමාවලියට එක් කිරීමට `yes` ලෙස ප්‍රතිචාර දක්විය යුතු අතර, එය මෙම නෝඩයට අනාගත SSH සම්බන්ධතා අතරතුර මෙම අනතුරු ඇඟවීමේ පණිවිඩය පෙනීම වැළැක්වනු ඇත. එබැවින්, `yes` ටයිප් කර `enter` ඔබා සත්‍යතාවය තහවුරු කරන්න.

ඔබට පසුව ඔබේ මුරපදය ඇතුළත් කරන ලෙස අසනු ඇත, පළමුවේ පියවර 1 දී තාවකාලික ලෙස සකසා ඇති එක. `enter` සමඟ සත්‍යාපනය කරන්න. එවිට ඔබේ node වෙත SSH හරහා සම්බන්ධ වීමට ඔබට හැකි වේ.


සාරාංශයෙන්, ක්‍රියාත්මක කිරීමට ඇති විධාන මෙන්න:


- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- තාවකාලික මුරපදය ඇතුළත් කර සත්‍යාපනය කරන්න.


### චරියාව 4: යාවත්කාලීන කිරීම සහ සූදානම

You are now connected to your node via an SSH session. On your terminal, the command prompt should be: `pi@RoninDojo:~ $`. To start, update the list of available packages and install updates for existing packages with the following command:

`sudo apt update && sudo apt upgrade -y`


අලුත් කිරීම් සම්පූර්ණ වූ පසු, *Git* සහ *Dialog* ස්ථාපනය කිරීමට විධානය භාවිතා කරන්න:

`sudo apt install git dialog -y`


ඊළඟට, _RoninOS_ Git ගබඞයෙහි `master` ශාඛාව පිටපත් කිරීමට ක්‍රියාත්මක කරන්න:

`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`


Skripti `customize-image.sh` ukazom zaženite:

`cd /opt/RoninOS/ && sudo ./customize-image.sh`


**ස්ක්‍රිප්ට් එක බාධාවකින් තොරව ක්‍රියාත්මක වීමට ඉඩ දීම සහ එහි ක්‍රියාවලිය අවසන් වන තුරු ඉවසීම වැදගත් වේ**, එය විනාඩි 10 ක් පමණ ගත වේ. `Setup is complete` පණිවිඩය පෙනෙන විට, ඔබට ඊළඟ පියවරට යා හැක.


### 5. korak: RoninOS ආරම්භ කිරීම

Zaženite RoninOS z ukazom:

`sudo systemctl start ronin-setup`


ලොග් ගොනුවේ රේඛා ප්‍රදර්ශනය කිරීමට විධානය:

`tail -f /home/ronindojo/.logs/setup.logs`


Na tej točki je **pomembno, da pustite RoninOS zagnati in počakate, da** konča z delovanjem. To traja približno 40 minut. Ko se prikaže `All RoninDojo feature installations complete!`, lahko nadaljujete na korak 6.


### චරියාව 6: RoninUI වෙත ප්‍රවේශ වීම සහ අක්තපත්‍ර වෙනස් කිරීම

ස්ථාපනය සම්පූර්ණ කිරීමෙන් පසු, ඔබේ නෝඩ් එකට බ්‍රවුසරයක් හරහා සම්බන්ධ වීමට, ඔබේ පුද්ගලික පරිගණකය ඔබේ නෝඩ් එක සමඟ එකම දේශීය ජාලයට සම්බන්ධ වී ඇති බව සහතික කරන්න. ඔබේ යන්ත්‍රයේ VPN එකක් භාවිතා කරන්නේ නම්, තාවකාලිකව එය අක්‍රිය කරන්න. ඔබේ බ්‍රවුසරයේ නෝඩ් Interface වෙත ප්‍රවේශ වීමට, URL තීරුවේ ඇතුළත් කරන්න:


- ඔබේ නෝඩයේ IP Address සෘජුවම, උදාහරණයක් ලෙස, `192.168.1.??`;
- Ali, ටයිප් කරන්න `ronindojo.local`.


RoninUI मुखपृष्ठमा एक पटक, तपाईंलाई सेटअप सुरु गर्न संकेत गरिनेछ। यो गर्नका लागि, `Let's start` बटनमा क्लिक गर्नुहोस्।


![lets start](assets/notext/25.webp)


Na tej stopnji vam RoninUI predstavi vaše `root` geslo. Pomembno je, da ga hranite na varnem. Lahko se odločite za fizično varnostno kopijo na papirju ali pa ga shranite v [upravitelju gesel](https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-1562bd55930f).


![root password](assets/notext/26.webp)


`root` මුරපදය සුරැකීමෙන් පසු, `I have backed up Root user credentials` කොටුවට ලකුණු කර `Continue` මත ක්ලික් කර ඉදිරියට යන්න.


![confirm root password](assets/notext/27.webp)


Naslednji korak vključuje ustvarjanje uporabniškega gesla, ki bo uporabljeno tako za dostop do RoninUI spletnega Interface kot za vzpostavitev SSH sej z vašo vozliščem. Izberite močno geslo in poskrbite, da ga boste varno shranili. To geslo boste morali vnesti dvakrat, preden kliknete na `Finish` za potrditev. Kar zadeva uporabniško ime, je priporočljivo obdržati privzeto izbiro, `ronindojo`. Če se odločite, da ga spremenite, ne pozabite ustrezno prilagoditi ukazov v naslednjih korakih.


![user credentials](assets/notext/28.webp)


Ko ta dejanja dokončate, počakajte, da se vaš vozlišče inicializira. Nato boste dostopali do spletnega vmesnika RoninUI Interface. Skoraj ste na koncu postopka, ostalo je le še nekaj majhnih korakov!

![Ronin UI](assets/notext/29.webp)


### පියවර 7: තාවකාලික අක්තපත්‍ර ඉවත් කරන්න

ඔබේ පුද්ගලික පරිගණකයේ නව ටර්මිනල් එකක් විවෘත කර, පහත විධානය භාවිතයෙන් ඔබේ නෝඩ් සමඟ SSH සම්බන්ධතාවයක් ස්ථාපිත කරන්න:

`SSH ronindojo@[IP]`


Če je na primer IP Address vašega vozlišča `192.168.1.40`, bo ustrezen ukaz:

`SSH ronindojo@192.168.1.40`


ඔබ පසුගිය පියවරේදී ඔබේ පරිශීලක නාමය වෙනස් කළේ නම්, පෙරනිමි පරිශීලක නාමය (`ronindojo`) වෙනුවට වෙනත් එකක් භාවිතා කරමින්, මෙම නව නාමය විධානයේ භාවිතා කිරීමට වග බලා ගන්න. උදාහරණයක් ලෙස, ඔබ `planb` ලෙස පරිශීලක නාමය තෝරාගෙන ඇති අතර IP Address `192.168.1.40` නම්, ඇතුල් වීමට විධානය වන්නේ:

`SSH planb@192.168.1.40`

ඔබට පරිශීලක මුරපදය ඇතුළත් කරන ලෙස ඉල්ලා සිටිනු ඇත. එය ඇතුළත් කර `enter` ඔබා සත්‍යාපනය කරන්න. එවිට ඔබට RoninCLI Interface වෙත ප්‍රවේශ විය හැක. ඔබේ යතුරුපුවරුවේ අණ සලකුණු යතුරු භාවිතා කර `Exit RoninDojo` විකල්පය වෙත ගමන් කර `enter` ඔබා එය තෝරන්න.

![RoninCLI](assets/notext/30.webp)


මෙම අවස්ථාවේදී, ඔබේ node හි terminal මත, `ronindojo@RoninDojo:~ $` වැනි විධාන ඉඟියක් සමඟ සිටී. bootable micro SD කාඩ්පතේ වින්‍යාසය දුරදිග යාමේදී නිර්මාණය කළ තාවකාලික පරිශීලකයා ඉවත් කිරීමට, පහත විධානය ඇතුළත් කර `enter` ඔබන්න:

`sudo deluser --remove-home pi`


ඔබේ පරිශීලක මුරපදය තහවුරු කිරීමට ඔබට ආමන්ත්‍රණය කෙරේ. එය ඇතුළත් කර `enter` ඔබා සත්‍යාපනය කරන්න. මෙහෙයුම අවසන් වන තුරු රැඳී සිටින්න, එවිට ටර්මිනල් එකෙන් පිටවීමට `exit` විධානය භාවිතා කරන්න.


සුභ පැතුම්! ඔබේ RoninDojo v2 නියමුවා දැන් වින්‍යාසය කර ඇති අතර භාවිතා කිරීමට සූදානම්. එය IBD (*Initial Block Download*) ආරම්භ කරනු ඇත, Genesis කොටසෙන් Bitcoin Blockchain බාගත කිරීම සහ සත්‍යාපනය කිරීම සඳහා ඉදිරියට යනු ඇත. මෙම පියවර 2009 ජනවාරි 3 සිට සිදු කරන ලද සියලුම Bitcoin ගනුදෙනු ලබා ගැනීම සම්බන්ධ වේ, සහ කාලයක් ගත වේ. Blockchain සම්පූර්ණයෙන්ම බාගත කිරීමෙන් පසු, දර්ශකය දත්ත ගබඩාව සංකෝචනය කිරීමට ඉදිරියට යනු ඇත. IBD කාලය සෑහෙන වශයෙන් වෙනස් විය හැක. මෙම ක්‍රියාවලිය අවසන් වූ විට ඔබේ RoninDojo නියමුවා සම්පූර්ණයෙන් ක්‍රියාත්මක වනු ඇත.


**ඔබ පැරණි RoninDojo v1 නියුඩ් එකකින්** මෙම නව අනුවාදයට මෙම උපදෙස් මාලාව සමඟ මාරු වන්නේ නම්, එම SSD එක භාවිතා කරමින්, ඔබේ නියුඩ් එක ස්වයංක්‍රීයව තැටියේ ඇති දත්ත හඳුනාගෙන නැවත භාවිතා කළ යුතු අතර IBD නැවත සිදු කිරීමේ අවශ්‍යතාවයෙන් ඔබව මුදවා ගනී. මෙම අවස්ථාවේදී, ඔබේ නියුඩ් එක නවතම බ්ලොක් සමඟ නැවත සමානුපාතික වන තෙක් ඔබට බලා සිටිය යුතුය.


### පියවර 8: "veth* fix"

Če naletite na napako z vašim RoninDojo v2 na Raspberry Pi, kjer po enostavni namestitvi vaš vozlišče nenadoma postane nedosegljivo prek SSH, vendar se po preprostem ponovnem zagonu obnovi, potem morate slediti temu koraku 8. To pogosta napaka se lahko enostavno odpravi z rešitvijo, ki jo je razvila skupnost: "_veth fix_". Ta manjši popravek trajno odpravi nenadne prekinitve povezave. Tukaj je, kako ga uporabiti.


ඔබේ පුද්ගලික පරිගණකයේ නව ටර්මිනල් එකක් විවෘත කර, පහත විධානය භාවිතයෙන් ඔබේ නෝඩ් එක සමඟ SSH සම්බන්ධතාවයක් ස්ථාපිත කරන්න:

`SSH ronindojo@[IP]`


Če je na primer IP vašega vozlišča Address `192.168.1.40`, bi bil ustrezen ukaz:

`SSH ronindojo@192.168.1.40`


ඔබට පරිශීලක මුරපදය ඇතුළත් කිරීමට ඉල්ලනු ලැබේ. එය ඇතුළත් කර `enter` ඔබා සත්‍යාපනය කරන්න. එවිට ඔබට RoninCLI Interface වෙත ප්‍රවේශ විය හැක. ඔබේ යතුරුපුවරුවේ ඊතල භාවිතා කර `Exit RoninDojo` විකල්පය වෙත ගොස් `enter` ඔබා එය තෝරන්න.


මෙම අවස්ථාවේදී, ඔබේ node හි ටර්මිනල් එකේ, පහත පරිදි command prompt එකක් ඇත: `ronindojo@RoninDojo:~ $`. veth* විසඳුම යෙදීමට, පහත විධානය ටයිප් කර `enter` ඔබන්න:

`sudo nano /etc/dhcpcd.conf`


ඔබගේ මුරපදය නැවත තහවුරු කර `enter` ඔබන්න.


`dhcpcd.conf` फाइलमा तपाईं पुग्नुहुनेछ। तपाईंले निम्न पाठलाई प्रतिलिपि गर्न आवश्यक छ, तारांकन चिह्न समावेश गर्न सुनिश्चित गर्दै, र फाइलको तल थप्नुहोस्:

`denyinterfaces veth*`


ඒ සඳහා, ඔබේ යතුරුපුවරුවේ පහළ ඊතලය භාවිතා කර ගොනුවේ පහළට ගමන් කරන්න, එවිට ඔබේ මවුස් එකේ දකුණු ක්ලික් භාවිතා කර ස්වාධීන රේඛාවක පෙළ අලවන්න.


පෙළ එකතු කිරීමෙන් පසු, පිටවීම ආරම්භ කිරීමට `ctrl X` ඔබන්න, වෙනස්කම් සුරැකීම තහවුරු කිරීමට `ctrl Y` අනුගමනය කරන්න, සහ අවසන් කිරීමට සහ විධාන ඉඟියට නැවත යාමට `enter` ඔබන්න. වෙනස්කම් නිවැරදිව යෙදුණාදැයි සහතික කර ගැනීමට, සුදුසු විධානය භාවිතා කර `dhcpcd.conf` ගොනුව නැවත විවෘත කරන්න.


Če želite dokončati uporabo popravka, znova zaženite svoj vozlišče z izvajanjem:

`sudo reboot now`


මෙම අවස්ථාවේදී, ඔබේ ටර්මිනල් වසා දැමිය හැක. ඔබේ RoninDojo නැවත ආරම්භ කිරීමට අවශ්‍ය කාලය ලබා දී, ඊට පසු ඔබේ බ්‍රවුසරයේ ග්‍රැෆිකල් Interface හරහා නැවත සම්බන්ධ විය හැක. මෙම ක්‍රියාවලිය මුහුණ දුන් දෝෂය නිවැරදි කළ යුතුය.


## Kako uporabljati svoj RoninDojo v2 vozlišče?


### ඔබේ Wallet මෘදුකාංගය Electrs වෙත සම්බන්ධ කිරීම

Vaša na novo nameščena in sinhronizirana vozlišča boste najprej uporabili za oddajanje svojih transakcij v omrežje Bitcoin. Verjetno boste želeli povezati svoje različne denarnice z vašim vozliščem, da boste lahko svoje transakcije oddajali zaupno. To lahko storite prek Electrum Rust strežnika (electrs). Ta aplikacija je običajno prednameščena na vašem RoninDojo vozlišču. Če ni, jo lahko ročno namestite prek RoninCLI Interface v `Applications > Manage Applications > Install Electrum Server`.


Če želite pridobiti Tor Address vašega strežnika Electrum, iz spletnega vmesnika RoninUI Interface, pojdite na:

`ජෝඩු කිරීම > Electrum සේවාදායකය > දැන් ජෝඩු කරන්න`

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

ඔබට පසුව Wallet මෘදුකාංගයේ `.onion` වලින් අවසන් වන `Hostname` Address ඇතුළත් කිරීමට අවශ්‍ය වන අතර, ඒ සමඟ `50001` වරායද ඇතුළත් කළ යුතුය. ![hostname](assets/notext/33.webp)

Na primer, na Sparrow Wallet, preprosto pojdite na zavihek:

`File > Preferences > Server > Private Electrum`


![Sparrow](assets/notext/34.webp)


### ඔබේ Wallet මෘදුකාංගය Samourai Dojo වෙත සම්බන්ධ කිරීම

Electrs භාවිතා කිරීමේ විකල්පයක් ලෙස, Dojo ඔබේ ගැළපෙන Software Wallet සෘජුවම ඔබේ RoninDojo නියුඩ්ට සම්බන්ධ කිරීමට ඉඩ සලසයි. Samourai Wallet සහ Sentinel වැනි පසුම්බි මෙම ක්‍රියාකාරිතාවය ලබා දේ.


සම්බන්ධතාවය ස්ථාපිත කිරීමට, ඔබට ඔබේ Dojo හි QR කේතය පමණක් ස්කෑන් කළ යුතුය. RoninUI හරහා මෙම QR කේතය ප්‍රවේශ වීමට, මෙහිට යන්න:

`සමූහ කිරීම > සමුරයි දෝජෝ > දැන් සමූහ කරන්න`

![Samourai Dojo](assets/notext/35.webp)

ඔබේ Samourai Wallet ඔබේ Dojo වෙත සම්බන්ධ කිරීමට, යෙදුම් ස්ථාපනය කිරීමේදී මෙම QR කේතය ස්කෑන් කරන්න:


![Samourai Wallet connection](assets/notext/36.webp)


Če ste že imeli Samourai Wallet pred nastavitvijo vašega Ronin Dojo, je potrebno narediti varnostno kopijo vašega Wallet, odstraniti in nato ponovno namestiti aplikacijo Samourai Wallet, preden obnovite vaš Wallet. Ob zagonu ponovno nameščene aplikacije boste imeli možnost povezave z novim Dojo. **Bodite previdni, ta postopek nosi tveganje izgube vaših bitcoinov, če ni pravilno izveden!** Prepričajte se, da imate varnostno kopijo vašega Samourai Wallet v vaših datotekah in preverite veljavnost vašega passphrase preko `Nastavitve > Odpravljanje težav > passphrase`. Prav tako je pomembno, da imate berljivo varnostno kopijo vaše obnovitvene fraze in vašega passphrase. Za večjo natančnost pri tem postopku je priporočljivo slediti temu podrobnemu priročniku: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).


### Uporaba lastnega Mempool.space Block explorer

Block explorer Bitcoin Blockchain හි අමු තොරතුරු සංවිධානාත්මක සහ පහසුවෙන් කියවිය හැකි ආකාරයකට පරිවර්තනය කරයි. *Mempool.space* වැනි මෙවලම් සමඟ, ගනුදෙනු විශ්ලේෂණය කිරීම, විශේෂිත ලිපින සොයන්න, හෝ ජාලයේ මෙන්පූල්ස් වල සාමාන්‍ය ගාස්තු අනුපාත සජීවීව උපදෙස් ලබා ගැනීමේ හැකියාව ඇත.


කෙසේ වෙතත්, මාර්ගගත අවරෝධ සොයාගන්නාකරුවන් භාවිතා කිරීමෙන් ඔබේ පෞද්ගලිකත්වයට අවදානම් ඇති අතර තෙවන පාර්ශවයන් විසින් සපයන දත්ත පිළිබඳ විශ්වාසය සම්බන්ධ වේ. ඇත්ත වශයෙන්ම, ඔබේම නියමුවා හරහා නොයන මෙම සේවා භාවිතා කිරීමෙන්, ඔබේ ගනුදෙනු පිළිබඳ තොරතුරු අහඹුවෙන් හෙළි කළ හැකි අතර, අඩවි හිමිකරු විසින් ඉදිරිපත් කරන තොරතුරු වල නිවැරදිභාවය මත රඳා පවතී.

මෙම අවදානම් අඩු කිරීම සඳහා, ඔබේම *Mempool.space* උදාහරණය Tor ජාලය හරහා, ඔබේ නෝඩය මත සෘජුවම සත්කාරක කරමින් භාවිතා කිරීම නිර්දේශ කෙරේ. මෙම විසඳුම ඔබේ පෞද්ගලිකත්වය සහ ඔබේ දත්තයේ ස්වයංපෝෂිතභාවය ආරක්ෂා කරයි.

මෙය කිරීමට, *Mempool Space Visualizer* RoninUI වෙතින් ස්ථාපනය කිරීමෙන් ආරම්භ කරන්න. වෙබ් Interface මත, `Dashboard` ටැබය වෙත ගොස් `Mempool Space` යටතේ ඇති `Manage` මත ක්ලික් කරන්න:

`Dashboard > Mempool Space > Manage`

![Manage mempool](assets/notext/37.webp)

පසුව `Mempool visualizer ස්ථාපනය කරන්න` බොත්තම මත ක්ලික් කරන්න:

![install mempool](assets/notext/38.webp)

ඔබේ පරිශීලක මුරපදය තහවුරු කරන්න:

![password mempool](assets/notext/39.webp)

ඇන්ස්ථාපනය සම්පූර්ණ වන තුරු රැඳී සිටින්න, එවිට නැවත `Manage` බොත්තම මත ක්ලික් කරන්න:

![Mempool Manage](assets/notext/40.webp)

`.onion` ලින්ක් එකක් ලබාගෙන Tor ජාලය හරහා ඔබේම *Mempool.space* ආකෘතියට ප්‍රවේශ විය හැක.

![Mempool link](assets/notext/41.webp)

මම ඔබට උපදෙස් දෙන්නේ මෙම සබැඳිය Tor බ්‍රවුසරයේ ඔබේ ප්‍රියතමයන් අතර සුරකින්න හෝ ඔබේ ස්මාර්ට්ෆෝනයේ Tor බ්‍රවුසර යෙදුමට එකතු කරන්න, ඕනෑම තැනකින් පහසු සහ ආරක්ෂිත ප්‍රවේශය සඳහා. ඔබට තවමත් Tor බ්‍රවුසරය නැත්නම්, මෙතනින් බාගත කළ හැක: [https://www.torproject.org/download/](https://www.torproject.org/download/)

![Mempool Tor](assets/notext/42.webp)


### Whirlpool භාවිතා කරමින් ඔබේ බිට්කොයින් මිශ්‍ර කිරීම

ඔබේ RoninDojo නියමුවා _WhirlpoolCLI_ සමඟ ඒකාබද්ධ වේ, එය Whirlpool කාසි සම්බන්ධකරණයන් ස්වයංක්‍රීය කිරීම සක්‍රීය කරන command-line Interface එකක් වන අතර _WhirlpoolGUI_, _WhirlpoolCLI_ සමඟ අන්තර්ක්‍රියා කිරීමට නිර්මාණය කරන ලද දෘශ්‍ය Interface එකක් වේ.


CoinJoin izvajanje prek Whirlpool zahteva, da je uporabljena aplikacija aktivna za izvajanje remiksov. Ta pogoj je lahko omejujoč za tiste, ki želijo doseči visoke ravni anonsetov. Dejansko mora naprava, ki gosti aplikacijo z integriranim Whirlpool, ostati neprekinjeno vklopljena. To pomeni, da mora vaš računalnik ali pametni telefon ostati vklopljen s stalno odprtim Samourai ali Sparrow, če želite sodelovati v remiksih 24 ur na dan. Rešitev za to omejitev je uporaba _WhirlpoolCLI_ na napravi, ki je vedno vklopljena, kot je vozlišče Bitcoin, kar omogoča, da se vaši kovanci remiksajo brez prekinitve in brez potrebe po vklopu druge naprave.


සමුරායි Wallet සහ රොනින්ඩොජෝ v2 සමඟ කාසි එකතු කිරීමේ ක්‍රියාවලිය A සිට Z දක්වා පියවරෙන් පියවර මඟ පෙන්වීම සඳහා විස්තරාත්මක උපකාරකයක් සකස් කරමින් පවතී.


CoinJoin සහ එහි Bitcoin මත භාවිතය පිළිබඳ ගැඹුරු අවබෝධයක් සඳහා, මම ඔබට මෙම වෙනත් ලිපියද පරීක්ෂා කිරීමට ආරාධනා කරමි: Bitcoin මත CoinJoin අවබෝධය සහ භාවිතය, එහිදී මෙම කාර්මිකය පිළිබඳ ඔබට අවශ්‍ය සියලුම දැනුම විස්තර කරමි.


https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

### Whirlpool Stat Tool (WST) භාවිතා කිරීම


Whirlpool සමඟ coinjoins සිදු කිරීමෙන් පසු, ඔබේ මිශ්‍ර UTXOs සඳහා ලබා ගත් පෞද්ගලිකත්ව මට්ටම නිවැරදිව ඇගයීම ප්‍රයෝජනවත් වේ. මෙය කිරීමට, ඔබට Python මෙවලම *Whirlpool Stat Tool* භාවිතා කළ හැක. මෙම මෙවලම ඔබේ UTXOs හි අපේක්ෂිත සහ ප්‍රතිලාභ ලකුණු මැනීමට, ඒවායේ විච්චේදන අනුපාතය විශ්ලේෂණය කිරීමේදී ඉඩ සලසයි.


ඔබේ මෙම anonsets ගණනය කිරීමේ ක්‍රමවේදයන් පිළිබඳ අවබෝධය වැඩි දියුණු කිරීම සඳහා, මම නිර්දේශ කරන්නේ ලිපිය කියවීමට: REMIX - Whirlpool, එය මෙම දර්ශකවල ක්‍රියාකාරිත්වය විස්තර කරයි.


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



WST මෙවලමට ප්‍රවේශ වීමට, RoninCLI වෙත යන්න. මෙය කිරීමට, ඔබේ පුද්ගලික පරිගණකයේ ටර්මිනල් එකක් විවෘත කර, පහත විධානය භාවිතයෙන් ඔබේ නියුඩ් සමඟ SSH සම්බන්ධතාවයක් ස්ථාපිත කරන්න:

`SSH ronindojo@[IP]`


Če je na primer IP vašega vozlišča Address `192.168.1.40`, bi bil ustrezen ukaz:

`SSH ronindojo@192.168.1.40`


ඔබේ පරිශීලක නාමය 6 වන පියවරේදී වෙනස් කළේ නම්, පෙරනිමි පරිශීලක නාමය (`ronindojo`) වෙනුවට වෙනත් නාමයක් භාවිතා කරන්නේ නම්, මෙම නව නාමය විධානයේ භාවිතා කරන්න. උදාහරණයක් ලෙස, ඔබේ පරිශීලක නාමය ලෙස `planb` තෝරාගෙන ඇති අතර IP Address `192.168.1.40` නම්, ඇතුල් විය යුතු විධානය වන්නේ:

`SSH planb@192.168.1.40`


ඔබට පරිශීලක මුරපදය ඇතුළත් කරන ලෙස ඉල්ලා සිටිනු ඇත. එය ඇතුළත් කර `enter` ඔබා සත්‍යාපනය කරන්න. එවිට ඔබට RoninCLI Interface වෙත ප්‍රවේශ විය හැක. ඔබේ යතුරුපුවරුවේ අනුසාර යතුරු භාවිතා කර `Samourai Toolkit` මෙනුව වෙත ගමන් කර `enter` ඔබා එය තෝරන්න:


![Samourai Toolkit](assets/notext/43.webp)


ඉන්පසු `Whirlpool Stat Tool` තෝරන්න:


![WST](assets/notext/44.webp)


WST ආරම්භ කිරීමෙන් පසු, මෙවලම ස්වයංක්‍රීය ස්ථාපනය සමඟ ඉදිරියට යනු ඇත. මෙම පියවරේදී රැඳී සිටින්න. භාවිතා කිරීමේ උපදෙස් ගමන් කරනු ඇත. ස්ථාපනය අවසන් වූ විට, WST ටර්මිනල් වෙත ප්‍රවේශ වීමට ඕනෑම යතුරක් ඔබන්න:


![WST commands](assets/notext/45.webp)


පහත විධාන ඉඟිය ප්‍රදර්ශනය වේ:

`wst#/tmp>`


Če želite zapustiti ta Interface in se vrniti v meni RoninCLI, preprosto vnesite:

`නික්මන්න`


මුලින්ම, OXT වෙතින් දත්ත ලබා ගැනීමේදී රහස්‍යතාව සහතික කිරීම සඳහා Tor භාවිතා කිරීමට ප්‍රොක්සි වින්‍යාස කිරීම අවශ්‍ය වේ. විධානය ඇතුළත් කරන්න:

`socks5 127.0.0.1:9050`


Nato prenesite informacije o bazenu, ki vsebujejo vašo transakcijo:

`download 0001`

`0001` ට ඔබට රුචිකර පූල් එකේ නාමය වෙනස් කරන්න. නාම කේත WST මත පහත පරිදි වේ:


- පූල් 0.5 බිට්කොයින්ස්: `05`
- Bazeni 0.05 bitcoinov: `005`
- පූල් 0.01 බිට්කොයින්: `001`
- 0.001 bitcoins එකතු කරන්න: `0001`


`load 0001` කමාන්ඩ් එකේ `0001` ඔබේ පොකුරේ කේතය සමඟ ප්‍රතිස්ථාපනය කිරීමෙන් පසු දත්ත පූරණය කරන්න.


![WST loading](assets/notext/46.webp)


බාගත කිරීම සම්පූර්ණ වන තුරු රැඳී සිටින්න, එය විනාඩි කිහිපයක් ගත විය හැක. දත්ත බාගත වූ පසු, ඔබේ කාසිවල anonset ලකුණු දැන ගැනීමට, `score` විධානය ඔබේ txid (ඇතුළත කෝෂ්ඨක නැතිව) සමඟ ක්‍රියාත්මක කරන්න:

`score [txid]`


![WST score](assets/notext/47.webp)


WST nato prikaže retrospektivno oceno (_Backward-looking metrics_), ki ji sledi perspektivna ocena (_Forward-looking metrics_). Poleg anonset ocen bo WST prav tako nakazal stopnjo difuzije vaše transakcije znotraj sklada glede na njen anonset.


**ඔබේ නාණය සඳහා අපේක්ෂිත ලකුණ ගණනය කළ යුත්තේ ඔබේ මුල් මිශ්‍රණයේ txid සිට වන අතර, ඔබේ නවතම මිශ්‍රණයෙන් නොව. විපරීතව, UTXO හි පසුගාමී ලකුණ ගණනය කරන්නේ අවසන් චක්‍රයේ txid සිටය.**


### Boltzmann කැල්කියුලේටරය භාවිතා කිරීම

Boltzmann කැල්කියුලේටරය Bitcoin ගනුදෙනුවක් විශ්ලේෂණය කිරීම සඳහා මෙවලමක් වන අතර, එහි ඇන්ට්‍රොපි මට්ටම මැනීමේ හැකියාව සහිතව, අනෙකුත් උසස් මිනුම් ලබා දේ. මෙම දත්ත ගනුදෙනුවක පෞද්ගලිකත්වය ප්‍රමාණවත් ලෙස ඇගයීමට සහ සම්භාව්‍ය දෝෂ හඳුනා ගැනීමට උපකාරී වේ. මෙම මෙවලම දැනටමත් ඔබේ RoninDojo නියමක සමඟ ඒකාබද්ධ කර ඇති අතර, ප්‍රවේශ වීමට සහ භාවිතා කිරීමට පහසු වේ.


Prej kot podrobno opišemo postopek uporabe Boltzmannovega kalkulatorja, je pomembno razumeti pomen teh kazalnikov, njihov način izračuna in njihovo uporabnost. Čeprav so uporabni za katero koli transakcijo Bitcoin, so ti kazalniki še posebej koristni za ocenjevanje kakovosti transakcije CoinJoin.


**මූලික සූචකය** මෘදුකාංගය ගණනය කරන පළමු සූචකය වන්නේ `nb combinations` යන මෙවලමේ යටතේ දැක්වෙන, සම්භාව්‍ය සංයෝජන සංඛ්‍යාවයි. සම්බන්ධ UTXO වටිනාකම් මත පදනම්ව, මෙම සූචකය ආදාන සහ ප්‍රතිදාන සම්බන්ධ කළ හැකි ක්‍රම සංඛ්‍යාව ප්‍රමාණවත් කරයි. වෙනත් වචන වලින් කියනවා නම්, ගනුදෙනුවක් generate කළ හැකි සම්භාව්‍ය අර්ථකථන සංඛ්‍යාව තීරණය කරයි. උදාහරණයක් ලෙස, Whirlpool 5x5 ආකෘතියට අනුව CoinJoin ව්‍යුහගත කරන ලද එකක් `1496` සම්භාව්‍ය සංයෝජන ඉදිරිපත් කරයි:

![combinations](assets/notext/50.webp)

ක්‍රෙඩිට්: KYCP


**දෙවන දර්ශකය** ගණනය කරන්නේ ගනුදෙනුවක එන්ට්‍රොපිය, `Entropy` ලෙස නම් කර ඇත. ගනුදෙනුවක ඉහළ සංඛ්‍යාතය ඇති විකල්ප සංයෝජන ගණනක් තිබේ නම්, එහි එන්ට්‍රොපියට යොමු වීම වඩාත් සම්බන්ධීකාරක වේ. මෙය විකල්ප සංයෝජන ගණනේ ද්විතීයික ලෝගාරිත්මය ලෙස නිර්වචනය කර ඇත. මෙහි භාවිතා කරන සූත්‍රය මෙසේය:


- $E$: ගනුදෙනුවේ එන්ට්‍රොපි;
- $C$: ගනුදෙනුව සඳහා ඇති හැකියාවන්ගෙන් සමන්විත සංයෝජන සංඛ්‍යාව.

$$E = \log_2(C)$$


ගණිතයේ, ද්වීමය ලොගාරිත්මය (පද 2 ලොගාරිත්මය) යනු 2 කට බලයක් ලබා දීමේ විපරීත මෙහෙයුමට අනුකූල වේ. වෙනත් ආකාරයකින් කියනවා නම්, $x$ හි ද්වීමය ලොගාරිත්මය යනු $x$ ලබා ගැනීමට 2 කට උත්පාදනය කළ යුතු පූර්වකය වේ. එබැවින්, මෙම දර්ශකය බිට් වලින් පළ වේ. පෙර සඳහන් කළ පරිදි, Whirlpool 5x5 ආකෘතියට අනුව ව්‍යුහගත CoinJoin ගනුදෙනුවක් සඳහා එන්ට්‍රොපිය ගණනය කිරීමේ උදාහරණය ගනිමු, එය `1496` කට සමාන සම්භාව්‍ය සංයෝජන සංඛ්‍යාවක් ලබා දේ:

$$ C = 1496 $$

$$ E = \log_2(1496) $$

$$ E \approx 10.5469 \text{ bits}$$


यसरी, यो CoinJoin कारोबारले 10.5469 बिट्सको एन्ट्रपी देखाउँछ, जुन धेरै सन्तोषजनक मानिन्छ। यो मान जति उच्च हुन्छ, कारोबारले त्यति नै धेरै फरक व्याख्याहरूलाई स्वीकार्छ, यसरी यसको गोपनीयताको स्तर बढाउँछ।


අපි තවත් සාම්ප්‍රදායික ගනුදෙනුවක් සමඟ අමතර උදාහරණයක් ගනිමු, එක ඇතුළත් කිරීමක් සහ ප්‍රතිදාන දෙකක් සහිතව: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

මෙම ගනුදෙනුවේ සිදුවන එකම හැඩය වන්නේ: `(inp 0) > (Outp 0 ; Outp 1)` යන්නයි. එම නිසා, එහි ඇන්ට්‍රොපිය `0` ලෙස ස්ථාපිත වේ:

$$ C = 1 $$

$$ E = \log_2(1) $$

$$ E \approx 0 \text{ bits}$$

**Boltzmann කැල්කියුලේටරය** විසින් ලබා දෙන තුන්වන දර්ශකය `Wallet කාර්යක්ෂමතාව` ලෙස නම් කර ඇත. මෙම දර්ශකය, සමාන සැකසීමකදී සිතන ලද උපරිම ගනුදෙනුව සමඟ සසඳා, ගනුදෙනුවේ කාර්යක්ෂමතාව ඇගයීමට උපකාරී වේ. මෙය අපට උපරිම ඇන්ට්‍රොපිය පිළිබඳ සංකල්පය සාකච්ඡා කිරීමට හේතු වේ, එය විශේෂිත ගනුදෙනු ව්‍යුහයකින් සංකල්පිතව ලබා ගත හැකි උපරිම ඇන්ට්‍රොපියට සමාන වේ. එබැවින්, Whirlpool 5x5 CoinJoin ව්‍යුහයක් සඳහා, උපරිම ඇන්ට්‍රොපිය `10.5469` ලෙස සකස් කර ඇත. ගනුදෙනුවේ කාර්යක්ෂමතාව පසුව මෙම උපරිම ඇන්ට්‍රොපිය විශ්ලේෂණය කරන ලද ගනුදෙනුවේ සැබෑ ඇන්ට්‍රොපිය සමඟ මුහුණ දීමෙන් ගණනය කරයි. භාවිතා කරන සූත්‍රය මෙසේ වේ:


- $ER$: لین دین کی اصل اینٹروپی، بٹس میں ظاہر کی گئی؛
- $EM$: දී ඇති ගනුදෙනු ව්‍යුහයක් සඳහා ඇති හැකි උපරිම එන්ට්‍රොපිය, බිට් වලින්ද;
- $Ef$: ගනුදෙනුවේ කාර්යක්ෂමතාවය, බිට් වලින්.

$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$

$$Ef = 0 \text{ bits}$$


මෙම දර්ශකය ද ශතකයක් ලෙස ප්‍රකාශ කරයි, එහි සූත්‍රය එවිට:


- $CR$: සත්‍ය සම්භාව්‍ය සංයෝජන සංඛ්‍යාව;
- $CM$: enake strukture največje možno število kombinacij;
- $Ef$: කාර්යක්ෂමතාවය ප්‍රතිශතයක් ලෙස පළ කර ඇත.

$$Ef = \frac{CR}{CM}$$

$$Ef = \frac{1496}{1496}$$

$$Ef = 100\%$$


`100%` කාර්යක්ෂමතාවක් එසේ නම් පෙන්වන්නේ එම ගනුදෙනුවේ ව්‍යුහය මත පෞද්ගලිකත්වය සඳහා ඇති උපරිම හැකියාව උපරිම කරයි.


**සිව්වන දර්ශකය**, ඇන්ට්‍රොපි ඝනත්වය, හෝ `ඇන්ට්‍රොපි ඝනත්වය`, ගනුදෙනුවේ එක් එක් ආදාන හෝ ප්‍රතිදානයට සම්බන්ධ ඇන්ට්‍රොපිය පිළිබඳ දෘෂ්ටිකෝණයක් ලබා දේ. විවිධ ප්‍රමාණයේ ගනුදෙනු වල කාර්යක්ෂමතාව ඇගයීමට සහ සසඳා බැලීමට මෙම දර්ශකය ප්‍රයෝජනවත් වේ. එය ගණනය කිරීමට, ගනුදෙනුවේ මුළු ඇන්ට්‍රොපිය, සම්බන්ධිත මුළු ආදාන සහ ප්‍රතිදාන ගණනින් බෙදන්න. Whirlpool 5x5 CoinJoin උදාහරණය ගනිමින්:


- $ED$: බිට් වලින් පළ කරන ලද ඇන්ට්‍රොපි ඝනත්වය;
- $E$: ගනුදෙනුවේ ඇන්ට්‍රොපිය බිට් වලින් පළ කරයි;
- $T$: ගනුදෙනුවේ ආදාන සහ ප්‍රතිදාන සංඛ්‍යාව.

$$T = 5 + 5 = 10$$

$$ED = \frac{E}{T}$$

$$ED = \frac{10.5469}{10}$$

$$ED = 1.054 \text{ bits}$$

**පස්වන තොරතුරු කෑල්ල** බෝල්ට්ස්මන් ගණකය මඟින් ලබා දෙන ලද්දේ ආදාන සහ නිමාවන් අතර ගැලපීමේ සම්භාවිතාවන්ගේ වගුවයි. මෙම වගුව `බෝල්ට්ස්මන් ලකුණ` හරහා, විශේෂිත ආදානයක් ලබා දී ඇති නිමාවකට සම්බන්ධ වී ඇති සම්භාවිතාව පෙන්වයි. Whirlpool CoinJoin උදාහරණය ගතහොත්, සම්භාවිතාව වගුව සෑම ආදානයක් සහ නිමාවක් අතර සම්බන්ධතාවයේ අවස්ථා විශේෂිත කරමින්, ගනුදෙනුවේ සම්බන්ධතා පිළිබඳව ඇති අස්ථිරතාවය හෝ අනාවැකිය හැකි බව පෙන්වයි:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Tukaj je jasno, da ima vsak vnos enako možnost, da je povezan s katerim koli izhodom, kar krepi dvoumnost in zaupnost transakcije. Vendar pa je v primeru preproste transakcije z enim vnosom in dvema izhodoma situacija drugačna:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

මෙහි, අපි දකින්නේ ප්‍රතිදානයක් ආදානය 0 වෙතින් පැමිණීමේ සම්භාවිතාව 100% වන බවයි. එබැවින් අඩු සම්භාවිතාවක් වැඩි රහස්‍යභාවයට පරිවර්තනය වේ, ආදාන සහ ප්‍රතිදාන අතර සෘජු සබඳතා දුර්වල කිරීමෙන්.


**සැවොමට ලබා දෙන ලද හයවැනි තොරතුර** නියමිත සබැඳි ගණන සහ මෙම සබැඳි වල අනුපාතය වේ. මෙම දර්ශකය විශ්ලේෂණය කරන ලද ගනුදෙනුවේ ආදාන සහ ප්‍රතිදාන අතර සම්බන්ධතා කීයක් 100% සම්භාවිතාවක් සහිතව අවිවාදිත බව හෙළි කරයි. අනුපාතය, එමෙන්ම, ගනුදෙනුවේ සම්පූර්ණ සබැඳි අතර මෙම නියමිත සබැඳි වල බර පිළිබඳ දෘෂ්ටිකෝණයක් ලබා දේ.


උදාහරණයක් ලෙස, Whirlpool-වර්ගයේ CoinJoin ගනුදෙනුවක් නියත සබැඳි නොපෙන්වයි, එබැවින් දර්ශකයක් සහ 0% අනුපාතයක් පෙන්වයි. අනෙක් අතට, අපගේ දෙවන විමසු ගනුදෙනුව (එක ඇතුළත් කිරීමක් සහ පිටවීම් දෙකක් සහිත) දී, දර්ශකය 2 ලෙස සකසා ඇති අතර අනුපාතය 100% දක්වා ළඟා වේ. එබැවින්, ශූන්‍ය දර්ශකයක් ඇතුළත් කිරීම් සහ පිටවීම් අතර සෘජු සහ නිර්වචනීය සබැඳි නොමැතිකම නිසා විශිෂ්ට රහස්‍යභාවය සලකුණු කරයි.


**RoninDojo හි Boltzmann ගණකය වෙත ප්‍රවේශ වීමේ ආකාරය කෙසේද?**

*Boltzmann Calculator* මෙවලමට ප්‍රවේශ වීමට, RoninCLI වෙත යන්න. ایسا کرنے کے لیے, ඔබේ පුද්ගලික පරිගණකයේ ටර්මිනල් එකක් විවෘත කර, පහත විධානය භාවිතා කර ඔබේ නෝඩ් සමඟ SSH සම්බන්ධතාවයක් ස්ථාපිත කරන්න: `SSH ronindojo@[IP]`


ඔබේ නෝඩ් IP Address `192.168.1.40` නම්, සුදුසු විධානය වන්නේ:

`SSH ronindojo@192.168.1.40`


ඔබේ පරිශීලක නාමය 6 වන පියවරේදී වෙනස් කළේ නම්, පෙරනිමි පරිශීලක නාමය (`ronindojo`) වෙනුවට වෙනත් එකක් භාවිතා කරමින්, මෙම නව නාමය විධානයේ භාවිතා කිරීමට වග බලා ගන්න. උදාහරණයක් ලෙස, ඔබේ පරිශීලක නාමය ලෙස `planb` තෝරාගෙන ඇති අතර IP Address `192.168.1.40` නම්, ඇතුල් විය යුතු විධානය වන්නේ:

`SSH planb@192.168.1.40`


ඔබට පරිශීලක මුරපදය ඇතුළත් කරන ලෙස ඉල්ලා සිටිනු ඇත. එය ඇතුළත් කර `enter` ඔබා සත්‍යාපනය කරන්න. එවිට ඔබට RoninCLI Interface වෙත ප්‍රවේශ විය හැක. ඔබේ යතුරුපුවරුවේ අරෝ ආදර්ශ භාවිතා කර `Samourai Toolkit` මෙනුව වෙත ගමන් කර `enter` ඔබා එය තෝරන්න:


![Samourai Toolkit](assets/notext/43.webp)


එවිට `Boltzmann Calculator` තෝරන්න:


![boltzmann](assets/notext/49.webp)


ඔබ මෘදුකාංගයේ මුල් පිටුවට පැමිණෙනු ඇත:


![boltzmann home](assets/notext/51.webp)


txid ගනුදෙනුව ඔබ අධ්‍යයනය කිරීමට කැමති නම් ඇතුළත් කර `enter` යතුර ඔබන්න:


![boltzmann txid](assets/notext/52.webp)


එවිට ගණකය ඔබට අප පෙර සාකච්ඡා කළ සියලු සංඥා ලබා දේ:


![boltzmann result](assets/notext/53.webp)


### RoninDojo v2 හි අනෙකුත් විශේෂාංග

Vaš RoninDojo vozel vključuje različne druge funkcije. Zlasti imate možnost skeniranja določenih informacij, da jih upoštevate. Na primer, včasih vaš Samourai Wallet, povezan z RoninDojo, morda ne prikazuje bitcoinov, ki jih dejansko imate. Če stanje kaže 0, medtem ko ste prepričani, da imate bitcoine v tem Wallet, lahko to situacijo pojasni več razlogov, kot je napaka v poteh izpeljave. Toda eden od vzrokov je lahko tudi, da vaš vozel ne spremlja pravilno vaših naslovov. Da bi rešili to težavo, lahko zagotovite, da vaš vozel resnično sledi vašemu `xpub` z uporabo orodja _xpub tool_. Za dostop do tega orodja prek RoninUI sledite poti:

`අලුත්වැඩියා කිරීම > XPUB මෙවලම`


ඇතුළත් කරන්න `xpub` ගැටලුව ඇති කරමින් ඇති අතර මෙම තොරතුරු සත්‍යාපනය කිරීමට `Check` බොත්තම ක්ලික් කරන්න:

![xpub tool](assets/notext/54.webp)

සියලුම ගනුදෙනු නිවැරදිව ලැයිස්තුගත කර ඇති බව සහතික කරන්න. ඔබේ Wallet සඳහා භාවිතා කරන ව්‍යුත්පන්න වර්ගය ගැලපෙන බව තහවුරු කිරීමද වැදගත් වේ. මෙය එසේ නොවේ නම්, `Retype` මත ක්ලික් කරන්න, එවිට ඔබේ අවශ්‍යතා අනුව `BIP44`, `BIP49`, හෝ `BIP84` තෝරන්න.

මෙම මෙවලමෙන් එහා, RoninUI හි `Maintenance` ටැබය අනෙකුත් ප්‍රයෝජනවත් විශේෂාංග වලින් පිරී ඇත:


- ටැන්සැක්ෂන් මෙවලම*: ලබා දී ඇති ටැන්සැක්ෂනයක විස්තර පරීක්ෂා කිරීමට ඉඩ සලසයි;
- Address මෙවලම*: ඔබේ ඩොජෝව විසින් දෙන ලද Address එකක් හඹා යාම තහවුරු කිරීමට ඉඩ සලසයි;
- බ්ලොක් නැවත පරීක්ෂා කිරීම*: ඔබේ නියමය නියමිත බ්ලොක් පරාසයක නව පරීක්ෂණයක් සිදු කිරීමට බල කරයි.


`Push Tx` ටැබය RoninUI හි තවත් රසවත් විශේෂාංගයක් වන අතර, Bitcoin ජාලයේ අත්සන් කළ ගනුදෙනුවක් විකාශනය කිරීමට හැකියාව සලසයි. ගනුදෙනුව හෙක්සඩෙසමල් ආකාරයෙන් ඇතුළත් කළ යුතුය.


ඔබේ RoninUI පුවරුවේ ලබා ගත හැකි අනෙක් ටැබ් සම්බන්ධයෙන්:


- `Apps`: Whirlpool යෙදුම සත්කාර කරයි, සහ අනාගතයේ නව යෙදුම් ඒකාබද්ධ කිරීමට නිසැකවම භාවිතා කරනු ඇත;
- `ලොග්`: ඔබේ මෘදුකාංගයේ සිදුවීම් ලොග් වලට සජීවී ප්‍රවේශය ලබා දේ;
- `System Info`: ඔබේ නෝඩය පිළිබඳ පොදු තොරතුරු ලබා දේ, උදාහරණයක් ලෙස CPU උෂ්ණත්වය, ගබඩා ඉඩ භාවිතය, හෝ RAM දත්ත. ඔබේ නෝඩය නැවත ආරම්භ කිරීමට හෝ නිවා දැමීමට `Reboot` සහ `Shut down` විකල්ප ද සොයා ගනු ඇත;
- `සැකසුම්`: ඔබට ඔබේ පරිශීලක මුරපදය වෙනස් කිරීමට ඉඩ සලසයි.


ඔබට එය ලැබී ඇත! මෙම උපකාරකය අවසානය දක්වා අනුගමනය කිරීම සඳහා ඔබට ස්තූතියි. ඔබට එය සතුටුදායක වූවා නම්, එය සමාජ මාධ්‍යයෙහි බෙදා ගැනීමට මම ඔබට උනන්දුවක් දක්වන්නෙමි. තවද, ඔබට අවස්ථාවක් ලැබුණහොත්, අපගේ ප්‍රජාවට මෙම නොමිලේ සහ විවෘත මූලාශ්‍ර මෘදුකාංග ලබා දෙන සංවර්ධකයින්ට පරිත්‍යාගයක් මඟින් සහය වීමට සලකා බලන්න: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). RoninDojo පිළිබඳ ඔබේ දැනුම ගැඹුරු කිරීමට සහ වැඩි සම්පත් සොයා ගැනීමට, පහත සඳහන් බාහිර සම්පත් වෙත සබැඳි උපදෙස් ලබා ගැනීම මම ඉතාමත් නිර්දේශ කරමි.


**බාහිර සම්පත්:**


- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)