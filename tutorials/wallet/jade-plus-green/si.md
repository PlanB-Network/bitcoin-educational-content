---
name: Jade Plus - Green
description: Jade Plus සමඟ Green පහසුවෙන් වින්‍යාස කරන්න
---
![cover](assets/cover.webp)


Jade Plus යනු Blockstream විසින් නිර්මාණය කරන ලද Bitcoin පමණක් වන Hardware Wallet එකකි. මෙය සම්භාව්‍ය Jade හි අනුප්‍රාප්තිකයා වන අතර මෘදුකාංග වැඩිදියුණු කිරීම්, වැඩි විකල්ප සහ වඩාත් සුවිශේෂී භාවිතය සඳහා නැවත නිර්මාණය කරන ලද ආකෘති විශේෂාංග සමඟින් ඇත. මෙම නව අනුවාදය 1.9 අඟල් LCD තිරයක් සමඟින් විශිෂ්ටත්වයෙන් යුක්ත වන අතර, එහි පූර්ව වර්ණ පරාසය වඩාත් පුළුල් වේ. බොත්තම් සහ මෙනු නාවිගේෂන් ද සුදුසුකම් ලබා ඇත.


Jade Plus එක භාවිතා කළ හැකි ආකාර කිහිපයක් ඇත: USB-C වයර් සම්බන්ධතාවයක් හරහා, මයික්‍රෝ SD කාඩ්පතක් (ඇඩැප්ටරයක් අවශ්‍ය වේ) සමඟ "*Air-Gap*" ප්‍රකාරයෙන්, බ්ලූටූත් හරහා හෝ සම්මිලිත කැමරාවට ස්තූතිවන්ත වන QR කේත හුවමාරු කිරීමෙන් පවා. මෙම Hardware Wallet බැටරි බලයෙන් ක්‍රියාත්මක වේ.


මූලික කළු අනුවාදය සඳහා $149.99 සිට ලබා ගත හැකි අතර, "*Genesis Grey*" හෝ "*Lunar Silver*" අනුවාද සඳහා මිල $20 දක්වා ඉහළ යා හැක. එබැවින් Jade Plus යනු, Coldcard Q හෝ Passport V2 වැනි උසස් මට්ටමේ දෘඩාංග පසුම්බිවලට සමාන උසස් ක්‍රියාකාරිතාවන් සහිත, නමුත් මධ්‍යම පරාසයේ ආකෘතිවලට ආසන්නව, සාපේක්ෂව අඩු මිලකට, ආකර්ශනීය තේරීමකි.


![JADE-PLUS-GREEN](assets/fr/01.webp)


Jade Plus večinoma združljiv z večino Wallet upravljavske programske opreme. Tukaj je povzetek združljivosti v času pisanja (januar 2025):


| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Management software
| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |
| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |
| Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |
| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |
| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

මෙම උපදෙස් මාලාවේදී, අපි Jade Plus Blockstream හි Green Wallet ජංගම යෙදුම සමඟ Bluetooth සම්බන්ධතාවයක් හරහා පිහිටුවා භාවිතා කරමු. මෙම පිහිටුවීම ආරම්භකයින් සඳහා ඉතා සුදුසුය. ඔබට වඩා උසස් ආකාරයක් අවශ්‍ය නම්, Sparrow Wallet හි QR කේත ප්‍රකාරය සමඟ Jade Plus භාවිතා කරන මෙම උපදෙස් මාලාව බලන්න:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## ජේඩ් ප්ලස් ආරක්ෂක ආකෘතිය


Jade Plus uporablja varnostni model, ki temelji na "virtualnem varnem elementu", materializiranem z "slepo orakulo". Konkretno ta mehanizem združuje PIN, ki ga izbere uporabnik, skrivnost, ki je gostovana na Jade, in skrivnost, ki jo ima orakula (strežnik, ki ga vzdržuje Blockstream), za ustvarjanje AES-256 ključa, razdeljenega med dve entiteti. Med inicializacijo ECDH Exchange zavaruje komunikacijo z orakulo in šifrira obnovitveno frazo na Hardware Wallet. V praktičnem smislu, ko želite dostopati do seed za podpisovanje transakcij, potrebujete dostop do:




- Jade Plus උපකරණයම;
- PIN številka za odklepanje naprave ;
- සැඟවුණු මන්ත්‍රකාරයාගේ රහසට.


මෙම ආකාරයේ ප්‍රධාන වාසිය වන්නේ දෘඩාංග මට්ටමේ එකම අසාර්ථකතා ලක්ෂ්‍යයක් නොමැති වීමයි, මන්ද යත් ආක්‍රමණකරු ඔබේ Jade වෙත ප්‍රවේශය ලබා ගත් විට, යතුරු ලබා ගැනීම සඳහා එකවරම Jade සහ oracle දෙකම කඩන ලෙසින් අවශ්‍ය වේ. මෙම ආකෘතියෙන් අදහස් වන්නේ Jade Plus සම්පූර්ණයෙන්ම විවෘත මූලාශ්‍ර බවත්, උදාහරණයක් ලෙස Ledger මත භාවිතා කරන Elements සත්‍ය භෞතික ආරක්ෂිත භාවිතය සමඟ සම්බන්ධ සීමා වලින් වළකින බවත් වේ.


මෙම පද්ධතියේ අවාසියාව වන්නේ Jade Plus භාවිතය Blockstream විසින් නඩත්තු කරන oracle එක මත රඳා පවතින බවයි. මෙම oracle එක ප්‍රවේශය නොලැබෙන තත්වයකට පත්වුවහොත්, Hardware Wallet සෘජුවම PIN සමඟ භාවිතා කිරීම අසම්භාව්‍ය වේ. කෙසේ වෙතත්, මෙය ඔබේ බිට්කොයින් නැතිවී යන බව අර්ථ නොදක්වයි, මන්ද ඒවා තවමත් ඔබේ ප්‍රතිසාධන වාක්‍යය භාවිතයෙන් ප්‍රතිසාධනය කළ හැක, එය "*stateless*" ප්‍රකාරයේ Jade Plus තුළ ඇතුළත් කළ හැක. මෙම රඳාපවතිම වටහා ගැනීමට, ඔබේම oracle සේවාදායකය සකස් කර කළමනාකරණය කළ හැක.


## Jade Plus අමුත්තුවක් විවෘත කිරීම


Ko prejmete svoj Jade Plus, preverite, ali sta škatla in Seal v dobrem stanju, da zagotovite, da vaš paket ni bil odprt.


![JADE-PLUS-GREEN](assets/fr/02.webp)


බැඳි පෙට්ටිය තුළ ඔබට හමුවනවා:




- Le Jade Plus;
- USB-C කේබල්;
- පත්‍රිකා ඔබේ Mnemonic වාක්‍යය වචන ලෙස හෝ "*CompactSeedQR*" ලෙස සටහන් කිරීමට;
- ඉහත උපදෙස් භාවිතා කිරීම සඳහා;
- කඹයක්;
- කොටස් කිහිපයක්.


![JADE-PLUS-GREEN](assets/fr/03.webp)


උපකරණය සතු නාවිගේෂන් බොත්තම් 4ක්:




- දකුණු පහළ කෙළවරේ ඇති බොත්තම Jade ක්‍රියාත්මක කරයි;
- උපකරණයේ ඉදිරිපස ඇති විශාල බොත්තම භාවිතා කරනුයේ අයිතමයක් තෝරා ගැනීම සඳහාය;
- ඉහළින් ඇති කුඩා බොත්තම් දෙක ඔබට වමට සහ දකුණට ගමන් කිරීමට ඉඩ සලසයි;
- ඔබට උපාංගයේ ඉහළ ඇති බොත්තම් දෙක එකවර ක්ලික් කිරීමෙන් ද අයිතමයක් තෝරා ගත හැක.


![JADE-PLUS-GREEN](assets/fr/04.webp)


## Bitcoin Wallet නව ආරම්භය සැකසීම


ආරම්භ බොත්තම මත ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/05.webp)


"*Jade සකසන්න*" මත ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/06.webp)


Izberite "Začni nastavitev". Možnost "*Napredna nastavitev*" naredi enako, vendar z dostopom do naprednih nastavitev.


![JADE-PLUS-GREEN](assets/fr/07.webp)


පසුව "*නව Walletක් තනන්න*" මත ක්ලික් කර, නව seedක් generate කරන්න.


![JADE-PLUS-GREEN](assets/fr/08.webp)


කොටුව "*Continue*" මත ක්ලික් කර ඔබේ නව ප්‍රතිසාධන වාක්‍යය පෙන්වන්න.


![JADE-PLUS-GREEN](assets/fr/09.webp)


ඔබේ Jade Plus ඔබේ 12-වචන Mnemonic වාක්‍යය පෙන්වයි. **මෙම Mnemonic ඔබට ඔබේ සියලුම බිට්කොයින් සඳහා සම්පූර්ණ, අනිවාර්ය ප්‍රවේශය ලබා දේ. මෙම වාක්‍යය සතු කාට හෝ ඔබේ මුදල් සොරා ගැනීමට හැක, ඔබේ Jade Plus වෙත භෞතික ප්‍රවේශය නොමැතිව පවා. ඔබේ Jade අහිමිවීම, සොරකම් වීම හෝ කැඩී යාම සිදුවූ විට මෙම 12-වචන වාක්‍යය ඔබේ බිට්කොයින් වෙත ප්‍රවේශය නැවත ලබා දේ. එබැවින් එය සූක්ෂමව සුරැකීම සහ ආරක්ෂිත ස්ථානයක ගබඩා කිරීම ඉතා වැදගත් වේ.


ඔබට එය පෙට්ටියෙන් සපයන ලද පපිරිය මත ලිවිය හැකි අතර, අමතර ආරක්ෂාව සඳහා, මම එය ගිනි, ගංවතුර හෝ කඩාවැටීමෙන් ආරක්ෂා කිරීම සඳහා මල නොබැඳෙන වානේ පදනමක මත කැටයම් කිරීම නිර්දේශ කරමි.


![JADE-PLUS-GREEN](assets/fr/10.webp)


Mnemonic වාක්‍යය සුරැකීම සහ කළමනාකරණය කිරීමේ නිවැරදි ක්‍රමය පිළිබඳව වැඩි විස්තර සඳහා, විශේෂයෙන් ඔබ ආරම්භකයෙකු නම්, මෙම වෙනත් උපකාරකය අනුගමනය කිරීම මම ඉතාමත් නිර්දේශ කරමි:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***නිසැකවම, ඔබ මෙම වචන අන්තර්ජාලයේ බෙදා හරිය යුතු නැත, මම මෙම උපකාරකයෙහි කරන පරිදි. මෙම සාම්පල Wallet භාවිතා කරන්නේ Testnet මත පමණක් වන අතර මෙම උපකාරකය අවසානයේ මකා දමනු ඇත.


ස්කීන් එකේ දකුණු පැත්තේ ඇති ඊතලය මත ක්ලික් කර පහත වචන පෙන්වන්න.


![JADE-PLUS-GREEN](assets/fr/11.webp)


ඔබේ වාක්‍යය සුරක්ෂිත කළ පසු, Jade Plus ඔබගෙන් එය තහවුරු කරන ලෙස ඉල්ලා සිටී. උපාංගයේ ඉහළ ඇති බොත්තම් භාවිතා කර, නිවැරදි වචනය තෝරන්න, සහ මීළඟ වචනයට ගමන් කිරීමට මධ්‍යම බොත්තම ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/12.webp)


## Jade Plus Green Wallet සම්බන්ධ කිරීම


මෙම උපකාරිකාවේදී, අපි Green Wallet යෙදුම භාවිතා කර Jade Plus මත සත්කාරක Wallet කළමනාකරණය කරන්නෙමු. මෙම ක්‍රමය විශේෂයෙන් ආරම්භකයින් සඳහා සුදුසු වේ. ඔබට ඔබේ Bitcoin Wallet වඩා විස්තරාත්මකව කළමනාකරණය කිරීමට අවශ්‍ය නම්, ඔබට Sparrow Wallet ද භාවිතා කළ හැක, එය අපි වෙනම උපකාරිකාවකදී ආවරණය කරමු:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Blockstream Green යෙදුම ස්ථාපනය කිරීම සහ පිහිටුවීම පිළිබඳ උපදෙස් සඳහා, කරුණාකර මෙම වෙනත් උපකාරකයේ පළමු කොටස බලන්න:


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

Blockstream Green යෙදුම මත එක් වරක්, "*නව Wallet වින්‍යාස කරන්න*" බොත්තම ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/13.webp)


"*Hardware Wallet මත තෝරන්න*"


![JADE-PLUS-GREEN](assets/fr/14.webp)


ඔබේ ස්මාර්ට්ෆෝනයේ බ්ලූටූත් සක්‍රීය කරන්න, එවිට "*ඔබේ ජේඩ් සම්බන්ධ කරන්න*" බොත්තම ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/15.webp)


Green යෙදුමට බ්ලූටූත් සම්බන්ධතා ප්‍රවේශය ලබා දිය යුතුය.


![JADE-PLUS-GREEN](assets/fr/16.webp)


යෙදුම ඔබේ Jade Plus සොයමින් පවතී.


![JADE-PLUS-GREEN](assets/fr/17.webp)


Jade Plus මත, "*Bluetooth*" මෙනුව මත ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/18.webp)


Green යෙදුම මත ඔබේ උපාංගය තෝරන්න.


![JADE-PLUS-GREEN](assets/fr/19.webp)


ඔබේ Jade Plus හි යුගල කිරීමේ කේතය තහවුරු කරන්න.


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green vám ponuja test, da zagotovite, da je vaš žad pristen. Kliknite na gumb, da to storite.


![JADE-PLUS-GREEN](assets/fr/21.webp)


Jade මත තහවුරු කරන්න.


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green තහවුරු කරන්නේ ඔබේ උපාංගය සත්‍ය බවයි.


![JADE-PLUS-GREEN](assets/fr/23.webp)


## PIN කේතය සකසීම


Kliknite na gumb "*Nadaljuj*" za izbiro PIN kode za Jade.


![JADE-PLUS-GREEN](assets/fr/24.webp)


PIN කේතය ඔබේ Jade අගුළු හරිනු ඇත. එබැවින්, අනුමත නොකළ භෞතික ප්‍රවේශයට එරෙහි ආරක්ෂාවකි. මෙම PIN කේතය ඔබේ Wallet හි සංකේතමය යතුරු ව්‍යුත්පන්න කිරීමේදී සම්බන්ධ නොවේ. එබැවින්, මෙම PIN කේතයට ප්‍රවේශය නොමැතිව සිටියත්, ඔබේ 12-වචන Mnemonic වාක්‍යය හිමිකර ගැනීමෙන් ඔබට ඔබේ බිට්කොයින් නැවත ප්‍රවේශ විය හැක. අපි හැකි අයුරින් අහඹු PIN කේතයක් තෝරා ගැනීමට නිර්දේශ කරමු. සහ ඔබේ Jade ගබඩා කර ඇති ස්ථානයෙන් වෙනම ස්ථානයක (උදාහරණයක් ලෙස මුරපද කළමනාකරුක) මෙම කේතය සුරැකීමට වග බලා ගන්න.


ඔබේ ජේඩ් සඳහා 6 අංක PIN කේතය තෝරන්න, අංක හරහා ගමන් කිරීමට දකුණු සහ වම් බොත්තම් භාවිතා කර, අංකයක් ඇතුළත් කිරීම තහවුරු කිරීමට මධ්‍ය බොත්තම භාවිතා කරන්න.


![JADE-PLUS-GREEN](assets/fr/25.webp)


ඔබේ PIN අංකය දෙවන වරට තහවුරු කරන්න.


![JADE-PLUS-GREEN](assets/fr/26.webp)


Vaš Bitcoin Wallet je bil ustvarjen.


![JADE-PLUS-GREEN](assets/fr/27.webp)


## Bitcoin ගිණුමක් සාදන්න


ඔබේ Wallet තුළ ගිණුමක් දැන් සාදන්න. "*ගිණුමක් සාදන්න*" බොත්තම ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/28.webp)


"*Standard*" තෝරන්න ඔබට සම්භාව්‍ය තනි-අත්සන Wallet එකක් නිර්මාණය කිරීමට අවශ්‍ය නම්.


![JADE-PLUS-GREEN](assets/fr/29.webp)


වැඩි විස්තර සඳහා "*2FA*" විකල්පය පිළිබඳව, ඔබට මෙම වෙනත් උපකාරකය අනුගමනය කළ හැක:


https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

ඔබේ ගිණුම නිර්මාණය කර ඇත.


![JADE-PLUS-GREEN](assets/fr/30.webp)


Če želite prilagoditi svoj Green Wallet, kliknite na tri majhne pike v zgornjem desnem kotu.


![JADE-PLUS-GREEN](assets/fr/31.webp)


"*නැවත නම් කරන්න*" විකල්පය ඔබේ Wallet හි නම අභිරුචිකරණය කිරීමට ඉඩ සලසයි, එය විශේෂයෙන්ම ප්‍රයෝජනවත් වේ ඔබ එකම යෙදුම මත විශාල වශයෙන් පසුම්බි කළමනාකරණය කරන විට. "*ඒකකය*" මෙනුව ඔබේ Wallet හි මූලික ඒකකය වෙනස් කිරීමට ඉඩ සලසයි. උදාහරණයක් ලෙස, ඔබට එය බිට්කොයින් වෙනුවට සටෝෂි ලෙස පෙන්වීමට තෝරා ගත හැක. අවසානයේ, "*පරාමිතීන්*" මෙනුව ඔබට අනෙකුත් විකල්ප වෙත ප්‍රවේශ වීමට ඉඩ සලසයි. මෙහි, උදාහරණයක් ලෙස, ඔබේ දිගු මහජන යතුර සහ එහි විස්තරකරු සොයා ගත හැක, ඔබේ ජේඩ් එකෙන් Watch-only wallet එකක් පිහිටුවීමට සැලසුම් කරන්නේ නම් ප්‍රයෝජනවත් වේ.


![JADE-PLUS-GREEN](assets/fr/32.webp)


ඔබේ Jade යන්ත්‍රය නිවා දැමීමෙන් පසු නැවත සම්බන්ධ කිරීමට, උපාංගයේ පහළ ඇති on/off බොත්තම ඔබන්න. Green යෙදුමේ මුල් පිටුවෙන් ඔබේ උපාංගය තෝරන්න:


![JADE-PLUS-GREEN](assets/fr/33.webp)


පසුව ඔබේ ජේඩ් උපාංගයේ PIN කේතය ඇතුළත් කරන්න, ඔබ නැවත සම්බන්ධ වනු ඇත.


![JADE-PLUS-GREEN](assets/fr/34.webp)


ඔබේ Jade, Blockstream හි "virtual secure element" හරහා අගුළු විවෘත කරයි (මෙම උපකාරක පඬතියේ පළමු කොටස බලන්න). මෙය Green යෙදුම සමඟ Bluetooth සම්බන්ධතාවයක් අවශ්‍ය කරයි. අගුළු විවෘත කිරීමේදී Bluetooth සම්බන්ධතාවය සමඟ අපහසුතා ඇතිවුවහොත්, උපාංග දෙක වෙන් කර නැවත සම්බන්ධ කිරීමට උත්සාහ කරන්න. ගැටලුව දිගටම පවතිනවා නම්, "*QR Scan*" විකල්පය තෝරා Blockstream වෙබ් අඩවියෙහි [ලබා ඇති උපදෙස්](https://jadefw.blockstream.com/pinqr/index.html) අනුගමනය කිරීමෙන් ඔබේ Jade අගුළු විවෘත කළ හැක.


Preden prejmete svoje prve bitcoine v vaš Wallet, **močno vam svetujem, da izvedete prazen test obnovitve**. Zapišite si nekaj referenčnih informacij, kot so vaš xpub ali prvi prejemni Address, nato izbrišite svoj Wallet v aplikaciji Green in na Jade Plus, medtem ko je še vedno prazen (`Options -> Device -> Factory Reset`). Nato poskusite obnoviti svoj Wallet z uporabo papirnatih varnostnih kopij fraze Mnemonic. Preverite, ali se informacije o piškotkih, ustvarjene po obnovitvi, ujemajo s tistimi, ki ste jih prvotno zapisali. Če se ujemajo, ste lahko prepričani, da so vaše papirnate varnostne kopije zanesljive. Če želite izvedeti več o tem, kako izvesti testno obnovitev, prosimo, preberite ta drugi vadnik :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## බිට්කොයින් ලබා ගන්න


Bitcoin Wallet සකසා ඇති බැවින්, ඔබේ පළමු Sats ලබා ගැනීමට ඔබ සූදානම්! Green යෙදුමේ "*Receive*" බොත්තම ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green Address ප්‍රතිචාරයක් පෙන්වයි, නමුත් එය භාවිතා කිරීමට පෙර, එය අපගේ Wallet සතු බව තහවුරු කිරීමට Jade මත පරීක්ෂා කිරීම අත්‍යවශ්‍ය වේ. මෙය කිරීමට, "*උපකරණය මත තහවුරු කරන්න*" බොත්තම ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/36.webp)


Address මත ඇති Jade එක Green මත ඇති එකට සමානදැයි පරීක්ෂා කරන්න, පසුව තහවුරු කිරීමට බොත්තම ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/37.webp)


ඔබට දැන් Address ගෙවන්නා සමඟ බිට්කොයින් ලබා ගැනීමට Wallet තුළ බෙදා ගත හැක. ගනුදෙනුව ජාලය මත විකාශය කරන විට, එය ඔබේ Wallet තුළ පෙනේ. ගනුදෙනුව නිශ්චිත ලෙස සලකන තෙක් ප්‍රමාණවත් තහවුරු කිරීම් ලැබෙන තෙක් රැඳී සිටින්න.


![JADE-PLUS-GREEN](assets/fr/38.webp)


## බිට්කොයින් යවන්න


ඔබේ Wallet හි බිට්කොයින් සමඟ, දැන් ඔබට බිට්කොයින් යැවිය හැක. "*Send*" මත ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/39.webp)


මීළඟ පිටුවේ, ලාභලාභියාගේ Address ඇතුළත් කරන්න. ඔබට එය අතින් ඇතුළත් කළ හැකි අතර නැතහොත් QR කේතයක් ස්කෑන් කළ හැක.


![JADE-PLUS-GREEN](assets/fr/40.webp)


රැකවරණ මුදල තෝරන්න.


![JADE-PLUS-GREEN](assets/fr/41.webp)


තිරයේ පහළින්, ඔබට මෙම ගනුදෙනුව සඳහා ගාස්තු අනුපාතය තෝරා ගත හැක. යෙදුමේ නිර්දේශ අනුගමනය කිරීම හෝ ඔබේ ගාස්තු අභිරුචිකරණය කිරීමේ විකල්පය ඔබට ඇත. අනෙක් බලාපොරොත්තු වන ගනුදෙනු සමඟ සසඳන විට ගාස්තුව වැඩි වුවහොත්, ඔබේ ගනුදෙනුව වේගයෙන් ක්‍රියාත්මක වේ. ගාස්තු වෙළඳපොළ තොරතුරු සඳහා, කරුණාකර [Mempool.space](https://Mempool.space/) හි "*Transaction Fees*" කොටසට පිවිසෙන්න.


![JADE-PLUS-GREEN](assets/fr/42.webp)


"*"Next"*" මත ක්ලික් කර ගනුදෙනු සාරාංශ තිරය වෙත ප්‍රවේශ වන්න. Address, මුදල සහ ගාස්තු නිවැරදි බව පරීක්ෂා කරන්න.


![JADE-PLUS-GREEN](assets/fr/43.webp)


यदि सबै ठीक भयो भने, Bitcoin नेटवर्कमा लेनदेन हस्ताक्षर र प्रसारण गर्न स्क्रीनको तलमा रहेको Green बटनलाई दायाँतिर स्लाइड गर्नुहोस्।


![JADE-PLUS-GREEN](assets/fr/44.webp)


ඔබ දැන් Jade හි ගනුදෙනුව තහවුරු කිරීමට ඉල්ලා සිටී.


![JADE-PLUS-GREEN](assets/fr/45.webp)


තහවුරු කරන්න ලැබුම්කරුගේ Address නිවැරදි බව. තහවුරු කිරීමට සලකුණ මත ක්ලික් කරන්න.


![JADE-PLUS-GREEN](assets/fr/46.webp)


පිළියෙළ මුදල නිවැරදි බව පරීක්ෂා කර, එවිට වලංගු කරන්න.


![JADE-PLUS-GREEN](assets/fr/47.webp)


ඔබේ ගනුදෙනුව Green වෙතින් අත්සන් කර විකාශනය කර ඇත.


![JADE-PLUS-GREEN](assets/fr/48.webp)


ඔබට සුභ පැතුම්, දැන් ඔබට Jade Plus Blockstream Green ජංගම යෙදුම සමඟ, Bluetooth සම්බන්ධතාවය හරහා පිහිටුවා භාවිතා කරන ආකාරය දැනගන්නට ඇත. මෙම උපකාරකය ප්‍රයෝජනවත් වූවා නම්, Green අඟුලක් පහළින් දමා මට කෘතඥ වන්න. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බෙදා ගැනීම සඳහා ස්තුතියි!


දෙයක් තවත් පියවරක් ඉදිරියට ගෙන යාම සඳහා, මම Jade Plus පිළිබඳ මෙම උපකාරක පංතිය නිර්දේශ කරමි, එහිදී අපි Sparrow Wallet මෘදුකාංගය QR ප්‍රකාරයෙන් වින්‍යාස කරමු. ඔබේ Hardware Wallet හි උසස් සැකසුම් භාවිතා කරන ආකාරය ද ඔබට ඉගෙන ගත හැක:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262