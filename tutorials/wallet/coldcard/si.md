---
name: Cold කාඩ්පත

description: Bitcoin zasebni ključ ustvarjanje, varnostno kopiranje in uporaba z napravo Coldcard in Bitcoin Core
---

![cover](assets/cover.webp)


_Bitcoin පුද්ගලික යතුරක් Coldcard උපාංගයක් සහ Bitcoin Core සමඟ නිර්මාණය කිරීම, ආපසු ගබඩා කිරීම සහ භාවිතා කිරීම_


## Celoten vodnik za ustvarjanje zasebnega ključa z uporabo Coldcard in njegovo uporabo prek Interface vašega Bitcoin Core vozlišča!


Bitcoin ජාල භාවිතයේ මූලික අංගය වන්නේ අසමමිතික කේතනයේ සංකල්පයයි: තරමක් පුද්ගලික සහ තරමක් පොදු යුගලයක් - දත්ත කේතනය සහ විකේතනය කරන, සන්නිවේදනයේ රහස්‍යභාවය සහතික කරන සංකල්පයක්.


Bitcoin の場合、そのようなプライベートキーとパブリックキーのペアを生成することによって、ビットコイン（UTXO または未使用トランザクション出力）を保存し、それらを使うためのトランザクションに署名することができます。


අද, පුද්ගලික යතුරක් සහ එහි zááපස්තාරය BIP 39 භාවිතයෙන් පෙළාත්මක ආකාරයෙන් සෘජුව ජනනය කිරීම සඳහා බොහෝ මෙවලම් ලබා ගත හැකිය - ගුප්තකේතන යතුරු සමඟ Mnemonic වාක්‍යයක් (seed වාක්‍යයක්) සම්බන්ධ කරන ආකාරය තීරණය කරන සම්මතයක්. බොහෝ විට, Mnemonic වාක්‍යය වචන 12 හෝ 24 කින් සමන්විත වේ, එය Wallet සහ එහි බිට්කොයින්ස් ප්‍රතිසාධනය කිරීමට හැකි වන පරිදි ආරක්ෂිතව zááපස්තාරය කළ යුතුය.


මෙම ලිපියෙන්, අපි generate පුද්ගලික යතුරක් Coldcard Mk4 භාවිතයෙන් කෙසේද යන්න ඉගෙන ගනිමු, Bitcoin ලෝකයේ වඩාත් භාවිතා වන සහ ආරක්ෂිත උපාංග අතරින් එකක් වන අතර, උපරිම අසාධාරණතාවය සහතික කිරීම සඳහා දාස් කුඩු ක්‍රමය භාවිතා කරමින්, එය Bitcoin Core සමඟ ගුවන්-අන්තර්ගත ආකාරයෙන් කෙසේ භාවිතා කරන්නේද යන්න!


**සටහන:🧰** මාර්ගෝපදේශය භාවිතා කිරීමට පහත මෙවලම් ලබා ගන්න:



- Coldcard naprava (Mk3 ali Mk4)
- MicroSD කාඩ්පත (4GB ප්‍රමාණය ප්‍රමාණවත් වේ)
- විදුලි බලය පමණක් ඇති චුම්බක USB කේබලය (Mk3 සඳහා කුඩා-usb, Mk4 සඳහා usb-c)
- එක් හෝ වැඩි ගුණාත්මක දාස්


## Mnemonic වාක්‍යයක් Coldcard සමඟ නිර්මාණය කිරීම


අපි පුද්ගලික යතුරක් නිර්මාණය කිරීමේ ක්‍රියාවලිය ආරම්භ කරමු, දැනටමත් PIN එකක් සකසා ඇති නව විවෘත කළ Coldcard එකක් මත පදනම්ව (උපාංග ආරම්භකරණය කිරීමේදී Coldcard මත පියවර අනුගමනය කරන්න).


**සටහන🚨:** දැනටමත් වින්‍යාසය කළ Coldcard එකක පෞද්ගලික යතුර නැවත සකසීමට, මෙම පියවර අනුගමනය කරන්න:

_Advanced/Tools > Danger Zone > seed Functions > Destroy seed > ✓_


**Pozor:** vaš Coldcard bo pozabil zasebni ključ po teh korakih. Prepričajte se, da ste pravilno varnostno kopirali svojo Mnemonic frazo, če jo želite kasneje obnoviti.


## අනුගමනය කළ යුතු පියවර:


Coldcard සමඟ සම්බන්ධ වන්න PIN > New seed Words > 24 Word Dice Roll


සීතකඩ පත්‍රය මත එක් එක් වාරය සඳහා 1 සිට 6 දක්වා ලැබෙන ප්‍රතිඵලය ලියමින්, 100 වාරයක් සූරකන්න. මෙම ක්‍රමය පුහුණු කිරීමෙන්, ඔබ 256 බයිට්ස් අහඹුකම නිර්මාණය කරයි, එමඟින් සම්පූර්ණයෙන්ම අහඹු පෞද්ගලික යතුරක් නිර්මාණය කිරීම ප්‍රියතම වේ. Coinkite සමාගම ඔවුන්ගේ අහඹුකම නිර්මාණ පද්ධතියේ ස්වාධීන සත්‍යාපනය සඳහා අවශ්‍ය ලේඛන සපයයි.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


100 දායිස් රෝල් සම්පූර්ණ වූ විට, ✓ ඔබා එවිට ලබා ගත් වචන 24 ක් අනුපිළිවෙලින් ලියන්න. දෙවරක් සත්‍යාපනය කර ✓ ඔබන්න. අවසානයේ, ඉතිරිව ඇත්තේ Coldcard මත වචන 24 ක සත්‍යාපන පරීක්ෂණය සම්පූර්ණ කිරීම පමණි, හා වොයිලා, ඔබගේ නව පෞද්ගලික යතුර නිර්මාණය වී ඇත!


ඊළඟට, පෙන්වා ඇති පියවර අනුගමනය කරමින් NFC (Mk4) සහ USB ක්‍රියාකාරකම් සක්‍රීය කිරීමට හෝ නොකරීමට තෝරන්න. ප්‍රධාන මෙනුවට පැමිණි විට, දැන් උපාංගයේ ෆාම්වේයර් යාවත්කාලීන කිරීමට වේලාවයි. Advanced/Tools > Upgrade Firmware > Show Version වෙත ගොස්, නිල වෙබ් අඩවියට පිවිසිමෙන් නවතම අනුවාදය සත්‍යාපනය කර බාගත කරන්න. උපරිම ආරක්ෂාවෙන් ප්‍රයෝජන ලබා ගැනීම සඳහා Coldcard යාවත්කාලීන කිරීම නිර්දේශ කෙරේ.


Preden nadaljujete, je priporočljivo, da zabeležite prstni odtis glavnega ključa (XFP), povezanega z zasebnim ključem. Ti podatki omogočajo hitro preverjanje, ali ste v pravilnem Wallet v primeru obnovitve, na primer. Pojdite na Napredno/Orodja > Ogled identitete > Prstni odtis glavnega ključa (XFP) in zapišite niz osmih alfanumeričnih znakov, ki jih dobite. XFP lahko zabeležite na istem mestu kot frazo Mnemonic, saj to niso občutljivi podatki.


**සටහන:💡** ඔබේ Mnemonic වාක්‍ය ආපසුගැන්වීම වෙනත් මෘදුකාංගයක පරීක්ෂා කිරීම නිර්දේශිතය. මෙය ආරක්ෂිතව කිරීමට, අපගේ ලිපිය Bitcoin Wallet ආපසුගැන්වීම Tails සමඟ විනාඩි 5 කට අඩු කාලයකින් සත්‍යාපනය කරන්න කියවන්න.


## Varnostni bonus: "Skrivni stavek" (neobvezno)


passphrase (රහස් වාක්‍යය) යනු ඔබේ බිට්කොයින් ආරක්ෂා කිරීමට Layer ආරක්ෂාවක් එක් කිරීමට Wallet වින්‍යාසයකට එක් කිරීමට හොඳ මූලද්‍රව්‍යයකි. passphrase ක්‍රියා කරන්නේ Mnemonic වාක්‍යයට 25 වන වචනයක් වැනිය. එක් කළ විට, පෞද්ගලික යතුරක් සහ එයට සම්බන්ධ Mnemonic වාක්‍යයක් සමඟ සම්පූර්ණයෙන්ම නව Wallet එකක් නිර්මාණය වේ. නව Mnemonic වාක්‍යය ලිවිය යුතු නැත, මන්ද මෙම Wallet ආරම්භක Mnemonic වාක්‍යය තෝරාගත් passphrase සමඟ එකතු කිරීමෙන් ප්‍රවේශ විය හැක.


ඉලක්කය වන්නේ passphrase Mnemonic වාක්‍යයෙන් වෙනම සටහන් කිරීමයි, මන්ද දෙකම ලබා ගන්නා ආක්‍රමණකරුට මුදල් ලබා ගත හැකි වන අතර. අනෙක් අතට, මෙම අයිතමයන්ගෙන් එකක් පමණක් ලබා ගන්නා ආක්‍රමණකරුට මුදල් ලබා ගත නොහැකි වන අතර, Wallet වින්‍යාසයේ ආරක්ෂාව උපරිම කිරීමේ මෙම විශේෂිත වාසියයි.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## passphrase එකක් Coldcard සමඟ එක් කිරීමේ පියවර:


passphrase > වචන එකතු කරන්න (ආදර්ශනය) > යෙදුම. උපාංගය නව Wallet හි XFP පෙන්වනු ඇත passphrase සමඟ, එය පෙර සඳහන් කරුණු සඳහා passphrase සමඟ සටහන් කළ යුතුය.


**ඉඟිය💡** මෙහි passphrase සම්බන්ධ අමතර සම්පත් ඇත:



- [Here](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) there is the first one by _Trezor_;
- [यहाँ](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) आपको दूसरा _Coinkite_ द्वारा मिल सकता है;
- අවසානයක් [මෙහි](https://armantheparman.com/passphrase/) _armantheparman_ විසින් සොයා ගත හැක.


## Wallet Core එක Bitcoin Core එකට අපනයනය කිරීම


Wallet දැන් Bitcoin ජාලය සමඟ අන්තර්ක්‍රියා කිරීමට මෘදුකාංගයට අපනයනය කිරීමට සූදානම්. මෙම මාර්ගෝපදේශයේ, අපි Bitcoin Core (v24.1) භාවිතා කරමු.


Bitcoin Core සඳහා අපගේ ස්ථාපන සහ වින්‍යාස මාර්ගෝපදේශයන් වෙත යොමු වන්න:



- ඔබේම නියමකය Bitcoin Core සමඟ ක්‍රියාත්මක කිරීම:** https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- Configuring Tor for a Bitcoin Core node:** https://agora256.com/configuration-tor-Bitcoin-core/


Najprej vstavite micro SD kartico v Coldcard, nato izvozite Wallet za Bitcoin Core tako, da sledite tem korakom: Advanced/Tools > Export Wallet > Bitcoin Core. Na micro SD kartico bosta zapisana dva datoteka: Bitcoin-core.sig & Bitcoin-core.txt. Vstavite micro SD kartico v računalnik, kjer je nameščen Bitcoin Core, in odprite .txt datoteko. Videli boste vrstico "For Wallet with master key fingerprint." Preverite, da se osemznakovni XFP ujema s tistim, ki ste ga zapisali ob ustvarjanju vašega zasebnega ključa.'

මූලික Interface හි Bitcoin කෝර් හි Wallet සකස් කිරීම ආරම්භ කිරීමට පෙර, ගොනුවේ උපදෙස් අනුගමනය කිරීමට පෙර, මෙම පියවර අනුගමනය කරන්න: ගොනුව ටැබය වෙත යන්න > Wallet එකක් සාදන්න. ඔබේ Wallet සඳහා නමක් තෝරන්න (කෝර් හි "porte-monnaie" සමඟ හුවමාරු කළ හැකි පදය) සහ පෞද්ගලික යතුරු අක්‍රිය කරන්න, හිස් Wallet එකක් සාදන්න, සහ පින්තූරයේ පෙන්වා ඇති පරිදි Wallet විස්තර පරීක්ෂා කරන්න. එවිට, සාදන්න බොත්තම ඔබන්න.


![create a wallet](assets/guide-agora/3.webp)


Wallet Bitcoin මූලිකය තුළ නිර්මාණය කළ පසු, වින්ඩෝ ටැබය > Console වෙත ගොස්, පිටුවේ ඉහළින් තෝරා ඇති Wallet ඔබ නිර්මාණය කළ එකේ නම පෙන්වන බව සහතික කරන්න.


Zdaj v .txt datoteki, ki jo je prej ustvaril Coldcard, kopirajte vrstico, ki se začne z importdescriptors, nato jo prilepite v konzolo Bitcoin Core. Vrnjeni bi morali biti odziv, ki vključuje vrstico "success": true.


![nodes window](assets/guide-agora/4.webp)


If the response contains "message": "Ranged descriptors should not have a label", erase the entry "label": "Coldcard xxxx0000" in the copied line from the .txt file, then paste the complete line back into the Bitcoin Core console.


ඔබට අවශ්‍ය නම්, Coldcard Github හි [මෙහි](https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md) සමහර උපකාරයක් සොයා ගත හැක.


## Wallet ආනයනය Bitcoin මූලිකයෙහි වලංගු කිරීම


මෙම මෙහෙයුම සාර්ථක වූ බව සහතික කිරීම සඳහා, අවශ්‍ය Wallet, Bitcoin Core වෙත ආයාත කර ඇති බව සත්‍යාපනය කිරීම අවශ්‍ය වේ. මෙය තහවුරු කිරීම සඳහා සරල ක්‍රමයක් නම් Coldcard තුළ ජනනය කරන ලද ලිපින Bitcoin Core තුළ ජනනය කරන ලද ලිපින වලට අනුකූල වන බව සනාථ කිරීමයි.


Bitcoin Core: Prejmi > Ustvari novo prejemno Address

Coldcard: Address Explorer > Address 'bc1q' සමඟ ආරම්භ වන Address තෝරන්න. Coldcard Address 'bc1q' යෙදුම Bitcoin Core හි පෙන්වා ඇති Address සමඟ ගැලපිය යුතුය.

'Air-gapped' මෝඩ්‍යුලයේ ගනුදෙනු ලබා ගැනීම සහ යැවීම


ගනුදෙනුවක් ලබා ගැනීම අතිශය සරලයි; ලබා ගැනීම මත ක්ලික් කරන්න, ගනුදෙනුව ලේබල් කරන්න (විකල්පයක් නමුත් නිර්දේශිතයි), සහ නව ලබා ගැනීමේ Address එකක් සාදන්න. එවිට, Address ය එවන්නා සමඟ බෙදා ගැනීම පමණක් ඉතිරි වේ.


දැන්, මෙම Coldcard + Bitcoin Core සැකසුමේ ප්‍රධාන මූලික අංගය වන්නේ Coldcard සහ එහි පෞද්ගලික යතුර අන්තර්ජාලයට සම්බන්ධ නොවී ගනුදෙනු යැවීමයි, එය Bitcoin හි TBSP (PSBT - අර්ධව අත්සන් කළ Bitcoin ගනුදෙනු) ක්‍රියාවලිය භාවිතා කරන ගුවන්-ඉරිතලා ක්‍රමයක් ලෙස හැඳින්වේ.

අත්‍යවශ්‍යව, අපි ගනුදෙනුවක් ගොඩනැගීමට Bitcoin මූලික Interface භාවිතා කරමු, එය මයික්‍රෝ SD කාඩ්පත හරහා Coldcard වෙත අපනයනය කර, අත්සන් කිරීම සඳහා, පසුව අත්සන් කළ ගනුදෙනු ගොනුව Bitcoin මූලිකයට ආපසු ලබා දී ජාලයට ගනුදෙනුව විකාශනය කරමු. අපි මෙය මෙහෙම කරන්න ඕනේ Wallet Bitcoin මූලිකයට ආයාත කළේ පෞද්ගලික යතුරක් නොමැති නිසා, පමණක් මහජන යතුර (අපට අපගේ ලැබීමේ ලිපින generate කිරීමට ඉඩ සලසයි) නිසා, අපට අපගේ බිට්කොයින් වියදම් කිරීමට මෘදුකාංගයේ ගනුදෙනුවක් සෘජුවම අත්සන් කිරීම අසම්භාව්‍ය වේ.


Prej nadaljujete, se prepričajte, da so vklopljene naslednje možnosti v Nastavitve > Wallet:



- සිකා පාලන විශේෂාංග සක්‍රීය කරන්න
- අනන්‍ය නොවන කාසි වියදම් කරන්න (විකල්ප)
- TBPS පරීක්ෂා සක්‍රීය කරන්න


![option ](assets/guide-agora/5.webp)


### ගුවන්-අන්තර්ගත ප්‍රකාරයට යැවීමේ පියවර:


Pošlji > Vnosi > izberite želeni UTXO, nato vnesite prejemnikov Address v Plačaj. Transakcijska provizija: Izberi... > Po meri > Vnesite transakcijsko provizijo (Bitcoin Core izračuna v Sats/kilobajt namesto sat/bajt kot večina alternativnih Wallet rešitev. Torej 4000 Sats/kilobajt = 4 Sats/bajt). Ustvarite nepodpisano transakcijo > shranite datoteko na vašo micro SD kartico in jo vstavite v Coldcard.


Coldcard හි, Ready to sign ඔබන්න, ගනුදෙනු විස්තර සත්‍යාපනය කරන්න, එවිට ✓ ඔබන්න සහ අත්සන් කළ ගොනු ජනනය වූ විට micro SD කාඩ්පත නැවත පරිගණකයට ඇතුළත් කරන්න.


Bitcoin මූලිකයට නැවත ගොස්, ගොනුව ටැබය > ගොනුවෙන් TBSP පූරණය කරන්න තෝරන්න, සහ අත්සන් කළ ගනුදෙනු ගොනුව .PSBT ඇතුළත් කරන්න. PSBT මෙහෙයුම් කොටුව තිරයේ පෙනෙන අතර, ගනුදෙනුව සම්පූර්ණයෙන්ම අත්සන් කර ඇති බව සහ විකාශය කිරීමට සූදානම් බව තහවුරු කරයි. ඉතිරිව ඇත්තේ විකාශය ගනුදෙනුව ඔබන්න පමණි.


![PSBT operations](assets/guide-agora/6.webp)


### නිගමනය


Coldcard උපාංගය Bitcoin Core සමඟ එකතු කිරීම, ඔබේම node එකක් ධාවනය කරන, ශක්තිමත් වේ. එයට 100 කුඩු රැලි සහ රහස් වාක්‍යයක් සමඟ ජනනය කරන පුද්ගලික යතුරක් එකතු කරන්න, සහ ඔබේ Wallet වින්‍යාසය සංකීර්ණ සහ ශක්තිමත් බලකොටුවක් වේ.


අප හා සම්බන්ධ වීමට නිදහස් වන්න ඔබේ අදහස් සහ ප්‍රශ්න බෙදා ගැනීමට! අපගේ ඉලක්කය දැනුම බෙදා ගැනීම සහ දිනෙන් දින අපගේ අවබෝධය වැඩි කිරීමයි.