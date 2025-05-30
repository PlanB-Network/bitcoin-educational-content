---
name: Sparrow Wallet - Multisig
description: Sparrow මත බහු-අත්සන පෝර්ට්ෆෝලියෝ එකක් සාදන්න
---
![cover](assets/cover.webp)



බහු-අත්සන Wallet (සමහර විට "*Multisig*" ලෙස හැඳින්වේ) යනු Bitcoin Wallet ව්‍යුහයක් වන අතර, වියදමක් අනුමත කිරීමට විවිධ යතුරු වලින් බහු සංකේත අත්සන් අවශ්‍ය වේ. සාමාන්‍ය ("*singlesig*") Wallet එකක් මෙන් නොව, එක් පුද්ගලික යතුරක් UTXO එකක් අගුළු ඇරීමට ප්‍රමාණවත් වන Multisig එක **m-of-n** ආකෘතියක් මත පදනම්ව ඇත: Wallet සමඟ සම්බන්ධ _n_ යතුරු වලින්, _m_ අනිවාර්යයෙන්ම සෑම ගනුදෙනුවක්ම සහ-අත්සන් කළ යුතුය.



මෙම යාන්ත්‍රණය, පෝර්ට්ෆෝලියෝවක් පාලනය කිරීම, සමාන්තර සත්කාරකයන් හෝ උපාංග අතර බෙදා ගැනීමට හැකියාව සලසයි. උදාහරණයක් ලෙස, 2-අතුරින්-3 වින්‍යාසයකදී, ස්වාධීන යතුරු කට්ටල තුනක් ජනනය කෙරේ, නමුත් මුදල් මුදා හැරීමට අවශ්‍ය වන්නේ දෙකක් පමණි. මෙම ව්‍යුහය, යතුරක් අත්හැරීම හෝ අහිමි වීම සම්බන්ධයෙන් ඇති අවදානම් දැඩි ලෙස අඩු කරයි: එක් යතුරකට ප්‍රවේශය ඇති හොරාකරු Wallet හි සියල්ලම හිස් කළ නොහැක, සහ එක් යතුරක් අහිමි කරන පරිශීලකයෙකුට ඉතිරි දෙක සමඟ තවමත් ඔහුගේ මුදල් ප්‍රවේශ විය හැක.



![Image](assets/fr/01.webp)



Vendar pa ta večja varnost prinaša večjo kompleksnost. Nastavitev Multisig Wallet zahteva zavarovanje več Mnemonic fraz (ena na podpisni faktor) in razširjenih javnih ključev ("*xpub*"). Dejansko, če uporabljate Multisig 2-od-3 Wallet, za pridobitev Wallet morate imeti vse tri Mnemonic fraze ali vsaj dve od treh fraz. Ampak, če imate le dve od treh fraz, potrebujete tudi dostop do treh *xpubs*, brez katerih bo nemogoče pridobiti javne ključe, potrebne za dostop do bitcoinov, ki jih varujejo.



සාරාංශයක් ලෙස, Multisig පෝර්ට්ෆෝලියෝ එකක් ප්‍රතිසාධනය කිරීමට, ඔබ කළ යුතුයි :




- Ali pa dostopite do vseh Mnemonic stavkov, povezanih z vsakim podpisnim dejavnikom;
- Mnemonic වචන අවම සංඛ්‍යාව තාප්පය මගින් අවශ්‍ය වන පරිදි ඇති කර, අත්සන් කිරීමට හැකි වන අතර, අවශ්‍ය මහජන යතුරු ලබා ගැනීම සඳහා සියලුම සාධකවල xpubs වෙත ප්‍රවේශය ද ඇති විය යුතුය.



![Image](assets/fr/02.webp)



Multisig පෝර්ට්ෆෝලියෝ උපස්ථ කළමනාකරණය *ප්‍රතිදාන ස්ක්‍රිප්ට් විස්තරකාරකයන්* මඟින් පහසු කරයි, එය අරමුදල් ප්‍රවේශය සඳහා අවශ්‍ය සියලුම මහජන දත්ත එකට සමූහ කරයි. කෙසේ වෙතත්, මෙම ක්‍රියාකාරිතාව තවමත් සියලුම පෝර්ට්ෆෝලියෝ කළමනාකරණ මෘදුකාංගවල ක්‍රියාත්මක කර නොමැත.



Multisig බිට්කොයින් හිමිකරුවන්ට වඩාත්ම සුදුසු වේ, ආරක්ෂාව වැඩි දියුණු කිරීම හෝ මුදල් එකතු කළ කළමනාකරණය සඳහා: සමාගම්, සංගම්, පවුල්, හෝ විශාල ප්‍රමාණයක් බිට්කොයින් තබා ඇති තනි පරිශීලකයින්. එය විකේන්ද්‍රිත ආණ්ඩුකාරකම් යෝජනා සෑදීමට භාවිතා කළ හැකි අතර, උදාහරණයක් ලෙස, අත්සන් බලය කළමනාකරුවන් හෝ කණ්ඩායම් සාමාජිකයින් අතර බෙදා හැරීමට.



V tem priročniku se bomo naučili, kako ustvariti in uporabljati klasični večpodpisni Wallet z **Sparrow Wallet**. Če želite ustvariti prilagojen večpodpisni portfelj s časovnimi zaklepi, priporočam uporabo Liana:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## අවශ්‍යතා



Za ta vadnico vam bom pokazal, kako narediti Multisig z [Sparrow Wallet programsko opremo za upravljanje portfelja](https://sparrowwallet.com/download/). Če te programske opreme še niste namestili, to storite zdaj. Če potrebujete pomoč, imamo tudi podrobno vadnico o konfiguriranju Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Za nastavitev večpodpisnega Wallet boste potrebovali različne strojne denarnice. Za Multisig 2-de-3, na primer, bi lahko uporabili:




- Trezor Model One;
- Ledger ಫ್ಲೆಕ್ಸ್;
- කෝල්ඩ්කාර්ඩ් MK3.



![Image](assets/fr/03.webp)



Multisig වින්‍යාසය තුළ Hardware Wallet විවිධ නිෂ්පාදන භාවිතා කිරීම හොඳ අදහසකි. මෙය විශේෂිත ආකෘතියක් බරපතල ගැටළුවකට මුහුණ දුන් විට, එය ඔබේ Multisig හි සමස්ත ආරක්ෂාවට බලපා නොමැති බව සහතික කරයි. තවද, එය සෑම උපාංගයකම විශේෂිත වාසියන්ගෙන් ඔබට ප්‍රයෝජන ලබා ගැනීමට ඉඩ සලසයි. උදාහරණයක් ලෙස, මගේ වින්‍යාසය තුළ:





- Trezor Model One සම්පූර්ණයෙන්ම විවෘත මූලාශ්‍රය වන අතර, seed ජනනය සත්‍යාපනය කිරීමේ හැකියාව ලබා දේ. කෙසේ වෙතත්, එය ආරක්ෂිත මූලද්‍රව්‍යයකින් සන්නද්ධ නොවන බැවින්, භෞතික ප්‍රහාර සඳහා අරක්ෂිත නොවේ;





- Ledger Flex pa ima, po drugi strani, koristi od neverodostojne lastniške programske opreme, vendar vključuje Secure Element, ki ponuja odlično fizično zaščito;





- Coldcard සජ්ජිතය ආරක්ෂිත මූලද්‍රව්‍යයකින් සමන්විත වන අතර එහි කේතය සෙවිය හැක. එය අපගේ වින්‍යාසය සඳහා රසවත් තේරීමක් වන අතර, එය අනෙකුත් ආකෘති වල නොමැති සත්‍යාපන විශේෂාංග ලබා දේ.



Multisig Wallet කෙටුම්පත් කිරීමට පෙර, සෑම Hardware Walletක්ම නිවැරදිව කෙටුම්පත් කර ඇති බව සහතික කර ගන්න (Mnemonic ජනනය සහ සුරැකීම, PIN නිර්වචනය). විස්තරාත්මක උපදෙස් සඳහා, සෑම Hardware Walletක් සඳහාම අපගේ උපකාරක පංති අනුගමනය කළ හැක, උදාහරණයක් ලෙස :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

ජා අපි මෙම උපකාරක පංතියේ පසුව දකින්නෙමු, Multisig වින්‍යාසයට Hardware Wallet සමඟ සම්බන්ධ නොවන, නමුත් එහි පුද්ගලික යතුරු ඔබේ පරිගණකයේ ගබඩා වන සාධකයක් ඒකාබද්ධ කිරීමද සම්භවය. මෙම ක්‍රමය, ස්පෂ්ටවම, දෘඪාංග පසුම්බිවල පමණක් භාවිතය වඩාත් ආරක්ෂිතයි, නමුත් එය විශේෂිත අවස්ථාවලදී සම්බන්ධ විය හැක. උදාහරණයක් ලෙස, Multisig 2-de-3 සඳහා, ඔබට දෘඪාංග පසුම්බි දෙකක් සහ Software Wallet එකක් තෝරා ගත හැක.



## Multisig පෝර්ට්ෆෝලියෝ එකක් නිර්මාණය කිරීම



Sparrow Wallet විවෘත කරන්න, "*ගොනුව*" ටැබය මත ක්ලික් කරන්න, එවිට "*නව Wallet*" තෝරන්න.



![Image](assets/fr/04.webp)



Vašemu večpodpisnemu portfelju dodelite ime, nato kliknite na "*Ustvari Wallet*" za potrditev.



![Image](assets/fr/05.webp)



"*Policy Type*" වර්ගය යටතේ ඇති ඩ්‍රොප්-ඩවුන් මෙනුවෙන් "*Multi Signature*" විකල්පය තෝරන්න.



![Image](assets/fr/06.webp)



ඉහළ දකුණු කෙළවරේ, දැන් ඔබේ Multisig හි මුළු යතුරු ගණන, මෙන්ම වියදමක් අනුමත කිරීමට අවශ්‍ය සහා-අත්සන්කරුවන් ගණන නිර්වචනය කළ හැක. මගේ උදාහරණයේ, මෙය 2-අතුරින්-3 යෝජනා ක්‍රමයකි.



![Image](assets/fr/07.webp)



වින්ඩෝවෙහි පහළින්, Sparrow Wallet තුළ "*Keystore*" තුනක් පෙන්වයි. සෑම එකක්ම යතුරු කට්ටලයක් නියෝජනය කරයි. මෙහි, මම ත්‍රිත්ව දෘඪාංග පෝර්ට්ෆෝලියෝ භාවිතා කරන බැවින්, සෑම "*Keystore*" එකක්ම ඒවාට එකට සමාන වේ. දැන් අපි ඒවා වින්‍යාස කරමු.



Začnem s Coldcard. V zavihku "*Keystore 1*" izberem možnost "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



On the Coldcard, once the device is unlocked, I go to the "*Settings*" menu, then to "*Multisig Wallets*".



![Image](assets/fr/09.webp)



මෙම මෙනුවෙන් ඔබට Coldcard සහභාගී වන Multisig පෝර්ට්ෆෝලියෝ කළමනාකරණය කළ හැක. මම නව එකක් නිර්මාණය කිරීමට අවශ්‍ය බැවින්, "*Export XPUB*" තෝරමි.



![Image](assets/fr/10.webp)



"*ගිණුම් අංකය*" ක්ෂේත්‍රය සඳහා, ඔබ එක් ගිණුමක් පමණක් කළමනාකරණය කරනවා නම්, ඔබට එය හිස්ව තබා තහවුරු කිරීමේ බොත්තම ඔබා සෘජුවම සත්‍යාපනය කළ හැක.



![Image](assets/fr/11.webp)



Coldcard nato generate datoteko, ki vsebuje vaš xpub, shranjeno na kartici Micro SD.



![Image](assets/fr/12.webp)



මෙම මයික්‍රෝ SD කාඩ්පත ඔබේ පරිගණකයට ඇතුල් කරන්න. Sparrow Wallet හි, "*Coldcard Multisig*" අසල ඇති "*Import File...*" බොත්තම ක්ලික් කරන්න, එවිට කාඩ්පතේ Coldcard මඟින් නිර්මාණය කරන ලද ගොනුව තෝරන්න.



![Image](assets/fr/13.webp)



ඔබේ xpub සාර්ථකව ආයාත කර ඇත. දැන් අපි අනෙක් ද්විත්ව දෘඩාංග පසුම්බි සමඟ ක්‍රියාවලිය නැවත සිදු කරන්නෙමු.



![Image](assets/fr/14.webp)



Ledger Flex සඳහා, මම "*Keystore 2*" තෝරන අතර, පසුව "*Connected Hardware Wallet*" මත ක්ලික් කරමි. Ledger පරිගණකයට සම්බන්ධ වී ඇති බව, අගුළු විවෘත කර ඇති බව සහ Bitcoin යෙදුම විවෘත කර ඇති බව සහතික කරන්න.



![Image](assets/fr/15.webp)



පසුව "*Scan...*" බොත්තම මත ක්ලික් කරන්න.



![Image](assets/fr/16.webp)



ඔබේ දෘඩාංග පෝර්ට්ෆෝලියෝවෙහි නම අසල, "*Import Keystore*" මත ක්ලික් කරන්න.



![Image](assets/fr/17.webp)



දෙවන අත්සනකරු දැන් නිවැරදිව Sparrow Wallet හි ලියාපදිංචි වී ඇත.



![Image](assets/fr/18.webp)



මම Multisig වින්‍යාසය අවසන් කිරීමට Trezor One සමඟ සමාන ක්‍රමය නැවත කරනවා.



![Image](assets/fr/19.webp)



මගේ වින්‍යාසය තුළ අපි මෙම අවස්ථාව ආවරණය නොකරමු, නමුත් ඔබේ Multisig තුළ Sparrow (Hot Wallet) හි Software Wallet හරහා අත්සනක් ඇතුළත් කිරීමට අවශ්‍ය නම්, "*New or Imported Software Wallet*" බොත්තම ක්ලික් කරන්න.



දැන් ඔබේ සියලුම අත්සන උපකරණ Sparrow Wallet වෙත ආයාත කර ඇති බැවින්, "*Apply*" ක්ලික් කිරීමෙන් Multisig නිර්මාණය අවසන් කළ හැක.



![Image](assets/fr/20.webp)



තම Sparrow Wallet Wallet වෙත ප්‍රවේශය ආරක්ෂා කිරීමට ශක්තිමත් මුරපදයක් තෝරන්න. මෙම මුරපදය ඔබේ මහජන යතුරු, ලිපින, ලේබල් සහ ගනුදෙනු ඉතිහාසය අනුමත නොකළ ප්‍රවේශයෙන් ආරක්ෂා කරයි.



මෙම මුරපදය අහිමි වීමෙන් වළකින්න, මුරපද කළමනාකරු වැනි ආරක්ෂිත ස්ථානයක එය සුරකින්න.



![Image](assets/fr/21.webp)



## Multisig පෝර්ට්ෆෝලියෝවක් ආපසු ගබඩා කිරීම



Zdaj bomo shranili naš *Output Script Descriptor* na Coldcard (to velja samo za uporabnike s Coldcard v njihovem Multisig), predvsem pa bomo obdržali varnostno kopijo na neodvisnem mediju.



*විස්තරකරු* ඔබේ Multisig පෝර්ට්ෆෝලියෝවෙහි සියලු xpubs, generate යතුරු භාවිතා කරන ව්‍යුත්පන්න මාර්ගයන් සහිතව අඩංගු වේ. කොටස 1 හි අපි දැකපු දේ මතක තබා ගන්න: Multisig පෝර්ට්ෆෝලියෝව නැවත පිහිටුවීමට, ඔබට **සියලුම** Mnemonic වාක්‍ය තිබිය යුතුය, නැතහොත් අත්සන සීමාවට ළඟා වීමට අවශ්‍ය අවම සංඛ්‍යාව පමණක් තිබිය යුතුය. කෙසේ වෙතත්, දෙවන අවස්ථාවේදී, අතුරු අත්සනකරුවන්ගේ **xpubs** තිබීමද අත්‍යවශ්‍ය වේ. *විස්තරකරු* ඔබේ සියලු Multisig xpubs අඩංගු වේ.



Če to ni jasno, si samo zapomnite tole: za pridobitev Multisig potrebujete minimalno število Mnemonic fraz za vsak uporabljen Hardware Wallet, odvisno od praga (v mojem primeru: 2 frazi), kot tudi *Descriptor*.



මෙම *විස්තරකරු* හි පුද්ගලික යතුරු නොමැති අතර, මහජන යතුරු පමණක් අඩංගු වේ. මෙය අරමුදල් වෙත ප්‍රවේශය ලබා නොදෙන බවයි. එබැවින්, ඔබේ බිට්කොයින් සඳහා සම්පූර්ණ ප්‍රවේශය ලබා දෙන Mnemonic වාක්‍යවලට වඩා මෙය එතරම් අවදානම් නොවේ. *විස්තරකරු* සම්බන්ධ අවදානම සම්පූර්ණයෙන්ම රහස්‍යභාවය සම්බන්ධ වේ:妥 compromise වීමේ අවස්ථාවක, තෙවන පාර්ශවයක් ඔබේ සියලු ගනුදෙනු නිරීක්ෂණය කළ හැකි නමුත් ඔබේ අරමුදල් වියදම් කළ නොහැක.



මම දැඩිව නිර්දේශ කරනවා ඔබට මෙම *විස්තරකරු* කිහිපයක් පිටපත් කිරීමට, සහ ඒවා ඔබේ Multisig හි සෑම අත්සන් කිරීමේ උපාංගයක් සමඟ තබා ගැනීමට. උදාහරණයක් ලෙස, මගේ අවස්ථාවේදී, මම *විස්තරකරු* කඩදාසිය මත මුද්‍රණය කර Coldcard සමඟ පිටපතක්, තවත් එකක් Trezor සමඟ, සහ එකක් Ledger සමඟ තබා ගන්නවා. මම මෙම *විස්තරකරු* PDF ගොනුවක් ලෙස USB කුටිය තුනක් මත සුරකින්නෙමි, සෑම දෘඩාංග පෝර්ට්ෆෝලියම සමඟ එකක් එක්ක. මෙහෙම කරලා, මම මෙම *විස්තරකරු* කිසිදාක අහිමි නොවීමේ හැකියාව උපරිම කරමි, සහ සෑම උපාංගයක් සමඟම පිටපත් දෙකක් (එක භෞතික සහ එක ඩිජිටල්) තිබීමේ විශ්වාසය ඇති කරමි.



ඔබගේ Multisig පෝර්ට්ෆෝලියෝ නිර්මාණය වූ පසු, Sparrow ස්වයංක්‍රීයව ඔබට මෙම *විස්තරකරු* ලබා දේ. එය පෙළක් සහ QR කේතයක් ලෙස සුරැකීමට "*PDF සුරකින්න...*" බොත්තම ක්ලික් කරන්න.



![Image](assets/fr/22.webp)



ඔබට එවිට මෙම PDF මුද්‍රණය කර ඔබේ USB කුටීර වලට පිටපත් කළ හැක.



![Image](assets/fr/23.webp)



අපි මෙම *විස්තරකරු* Coldcard තුළද ලියාපදිංචි කරමු (ඔබේ වින්‍යාසය තුළ එකක් භාවිතා කරනවා නම්). මෙය Coldcard එකට පසුව අත්සන් කරන ලද සෑම ගනුදෙනුවක්ම මුල් Wallet: නිවැරදි xpubs, නිවැරදි Address ආකෘතිය, නිවැරදි ව්‍යුහ මාර්ගය සමඟ අනුකූල වන බව සනාථ කිරීමට ඉඩ සලසයි... මෙම ආයාත කරන ලද *විස්තරකරු* නොමැතිව, Coldcard එකට Exchange ලිපින පැහැරගෙන නොමැති බව හෝ PSBT සෙල්ලම් කර නොමැති බව තහවුරු කළ නොහැක.



මෙය Multisig හි Coldcard එක ඉතා ආකර්ෂණීය කරන්නේ මෙයයි: එය විශේෂිත සංකීර්ණ ප්‍රහාරවලට එරෙහිව අමතර පරීක්ෂණ ලබා දේ, අනෙක් දෘඩාංග පසුම්බි ඉඩ නොදෙන (ඔබ එය අත්සන් කිරීමට භාවිතා කරන බව සපයන ලද්දේ නම්).



Sparrow හි, "*Settings*" මෙනුවට ප්‍රවේශ වීමෙන් පසු, "*Export...*" මත ක්ලික් කරන්න.



![Image](assets/fr/24.webp)



"*Coldcard Multisig*" විකල්පය අසල, "*Export File...*" මත ක්ලික් කර Micro SD කාඩ්පතට පෙළ ගොනුව සුරකින්න.



![Image](assets/fr/25.webp)



පසුව කාඩ්පත Coldcard තුළට ඇතුළත් කරන්න. "*Settings*" මෙනුවට යන්න, එවිට "*Multisig Wallets*" තෝරන්න, සහ "*Import from SD*" තෝරන්න.



![Image](assets/fr/26.webp)



සැකසූ ගොනුව තෝරා ආයාත කිරීම තහවුරු කරන්න.



![Image](assets/fr/27.webp)



ඔබේ නව ආනයන කරන ලද Multisig හි නම මත ක්ලික් කරන්න.



![Image](assets/fr/28.webp)



Multisig කාර්යය වින්‍යාස පරාමිතීන් පරීක්ෂා කර, ලියාපදිංචිය තහවුරු කරන්න.



![Image](assets/fr/29.webp)



ඔබේ Multisig දැන් නිවැරදිව ඔබේ Coldcard හි සුරක්ෂිත කර ඇත. එකම Multisig හි කීපයක් Coldcards තිබේ නම්, සෑම එකක් සඳහාම මෙම ක්‍රියාවලිය නැවත කරන්න.



Mnemonic වාක්‍යයන් සුරැකීම සඳහා විශේෂ අවධානය යොමු කිරීමට අමතරව, *විස්තරකරු* සුරැකීම අමතක නොකරන්න. ඔබ නවකයෙකු නම්, ඒවා නිවැරදිව සුරැකීම සහ කළමනාකරණය කිරීම කෙසේද යන්න ඉගෙන ගැනීමට මෙම වෙනත් උපකාරකය අනුගමනය කරන ලෙස මම ඉතා නිර්දේශ කරමි:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

ඔබේ Multisig මත ඔබේ පළමු බිට්කොයින් ලබා ගැනීමට පෙර, **මම ඔබට හිස් ප්‍රතිසාධන පරීක්ෂණයක් සිදු කරන ලෙස දැඩිව උපදෙස් දෙමි**. පළමු ලැබීම් Address වැනි යම් යොමු තොරතුරු සටහන් කර ගන්න, එවිට Wallet තවම හිස්ව ඇති අතර ඔබේ දෘඩාංග පසුම්බි යළි සකසන්න. ඊළඟට, ඔබේ Multisig Wallet දෘඩාංග පසුම්බි මත ඔබේ Mnemonic වාක්‍ය පත්‍ර පිටපත් භාවිතයෙන් යළි පිහිටුවීමට උත්සාහ කරන්න, එවිට Sparrow මත *විස්තරකරු* භාවිතා කරන්න. ප්‍රතිසාධනයෙන් පසු ජනනය කරන ලද පළමු Address ඔබ මුලින් සටහන් කර ගත් එකට ගැලපේදැයි පරීක්ෂා කරන්න. එසේ නම්, ඔබේ පත්‍ර පිටපත් විශ්වාසදායක බවට ඔබට විශ්වාස කළ හැක.



Za več informacij o tem, kako izvesti test obnovitve, predlagam, da si ogledate ta drugi vadnik:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## ඔබේ Multisig මත බිට්කොයින් ලබා ගන්න



ඔබේ Wallet දැන් බිට්කොයින් ලබා ගැනීමට සූදානම්. Sparrow හි, "*Receive*" ටැබය ක්ලික් කරන්න.



![Image](assets/fr/30.webp)



Sparrow Wallet විසින් ජනනය කරන ලද Address භාවිතා කිරීමට පෙර, ඔබේ දෘඩාංග පසුම්බිවල තිරය මත එය සෘජුවම පරීක්ෂා කිරීමට කාලය ගත කරන්න. මෙය Address වෙනස් වී නොමැති බව සහ ඔබේ උපාංග සම්බන්ධිත මුදල් වියදම් කිරීමට අවශ්‍ය පෞද්ගලික යතුරු අත්හිටුවා ඇති බව සහතික කරයි. මෙය ඔබට ප්‍රහාරක ව්‍යුහ රටා කිහිපයකින් ආරක්ෂා වීමට උපකාරී වේ.



Za to naredite, kliknite na "*Prikaži Address*", da prikažete Address na vašem Trezorju ali Ledger, ko je povezan s kablom.



![Image](assets/fr/31.webp)



Coldcart සමඟ, මෙම සත්‍යාපනය Sparrow සමඟ කිසිදු අන්තර්ක්‍රියාවකින් තොරව සිදු කළ හැක. සරලව "*Address Explorer*" මෙනුව විවෘත කරන්න, එවිට ඔබේ Multisig පහළම තැන තෝරන්න.



![Image](assets/fr/32.webp)



Multisig විසින් ජනනය කරන ලද පිළිගැනීමේ ලිපින ඔබට පසුව දැක ගත හැකි වේ.



![Image](assets/fr/33.webp)



පරීක්ෂා කරන්න Address එකක් එක් එක් Hardware Wallet මත පෙන්වා ඇති Wallet හි Sparrow එකට සමාන වේ. Address ගෙවන්නා සමඟ බෙදා ගැනීමට පෙර, එහි අඛණ්ඩතාවය සහතික කිරීම සඳහා මෙය කිරීම සුදුසුය.



ඔබට පසුව මෙම Address සඳහා "*ලේබලයක්*" පවරා, ලැබුණු බිට්කොයින්වල ආරම්භය සලකුණු කළ හැක. ඔබේ UTXO කළමනාකරණය සංවිධානය කිරීමේ මෙය හොඳ ක්‍රමයකි.



![Image](assets/fr/34.webp)



මෙය සනාථ කර ඇති විට, ඔබට bitcoins ලබා ගැනීමට Address භාවිතා කළ හැක.



![Image](assets/fr/35.webp)



## ඔබේ Multisig සමඟ බිට්කොයින් යැවීම



Zdaj, ko ste prejeli svoje prve Satse na vašem Multisig Wallet, jih lahko tudi porabite! V Sparrow pojdite na zavihek "*Send*", da ustvarite novo transakcijo.



![Image](assets/fr/36.webp)



ඔබ *Coin Control* භාවිතා කිරීමට කැමති නම්, එනම් ඔබ වියදම් කිරීමට කැමති UTXOs අතින් තෝරා ගැනීමට, "*UTXOs*" ටැබය වෙත යන්න. ඔබ වියදම් කිරීමට කැමති UTXOs තෝරන්න, එවිට "*Send Selected*" මත ක්ලික් කරන්න. ඔබ ස්වයංක්‍රීයවම "*Send*" ටැබය වෙත යොමු කෙරෙන අතර, UTXOs දැනටමත් පූර්ණ කර ඇත.



![Image](assets/fr/37.webp)



ඉලක්කය Address ඇතුළත් කරන්න. "*+ Add*" ක්ලික් කිරීමෙන් බහු ලිපින එකතු කළ හැක.



![Image](assets/fr/38.webp)



ඔබේ ගනුදෙනු හොඳින් හඳුනා ගැනීමට පහසු වන පරිදි, මෙම වියදමේ අරමුණ විස්තර කිරීමට "*ලේබලයක්*" එක් කරන්න.



![Image](assets/fr/39.webp)



ඇතැම් Address වෙත යැවිය යුතු මුදල ඇතුළත් කරන්න.



![Image](assets/fr/40.webp)



ගැටළුවලට අනුව ආරෝපණ අනුපාතය සකසන්න. උදාහරණයක් ලෙස, සුදුසු ආරෝපණ මට්ටමක් තෝරා ගැනීමට [Mempool.space](https://Mempool.space/) වෙත උපදෙස් ලබා ගන්න.



සියලුම ගනුදෙනු පරාමිතීන් පරීක්ෂා කිරීමෙන් පසු, "*Create Transaction*" මත ක්ලික් කරන්න.



![Image](assets/fr/41.webp)



ඔබට සියල්ල සමඟ සතුටු නම්, "*අත්සන් කිරීම සඳහා ගනුදෙනුව අවසන් කරන්න*" මත ක්ලික් කරන්න.



![Image](assets/fr/42.webp)



स्क्रीनको तल, तपाईंले देख्नुहुनेछ कि स्प्यारो २ हस्ताक्षरहरूको प्रतीक्षा गर्दैछ। यो सामान्य हो: यहाँ प्रयोग गरिएको Wallet एक Multisig 2-de-3 हो।



![Image](assets/fr/43.webp)



මම මගේ Coldcard සමඟ අත්සන් කිරීම ආරම්භ කරමි. මෙය කිරීමට, මම Micro SD කාඩ්පත පරිගණකයට ඇතුළත් කර, පසුව "*Save Transaction*" මත ක්ලික් කරමි.



![Image](assets/fr/44.webp)



ගනුදෙනුව අත්සන් කිරීමට ඔබේ Hardware Wallet වෙත සම්ප්‍රේෂණය කිරීමේ ක්‍රම 3ක් ඇත, එවිට Sparrow වෙතින් එය ලබා ගැනීම. පළමුව Micro SD කාඩ්පතක් භාවිතා කිරීමයි, අපි මෙහිදී Coldcard සඳහා එය කරමු. දෙවනුව කේබල් සම්බන්ධතාවයක් මඟින්, අපි දෙවන අත්සන සඳහා (Ledger සහ Trezor) එය භාවිතා කරමු. අවසානයේ, QR කේත සන්නිවේදනය භාවිතා කිරීමේ හැකියාව ඇත, Coldcard Q, Jade Plus හෝ Passport V2 වැනි කැමරා-සන්නද්ධ උපාංග සඳහා.



Ko PSBT (*Partially Signed Bitcoin Transaction*) මයික්‍රෝ SD එකේ සුරක්ෂිත කර ඇති විට, මම එය Coldcard MK3 වෙත ඇතුළත් කර, "*Ready to Sign*" මෙනුව තෝරමි.



![Image](assets/fr/45.webp)



ඔබේ Hardware Wallet තිරය මත, ගනුදෙනු පරාමිතීන් සූක්ෂමව පරීක්ෂා කරන්න: ලැබුම්කරුගේ Address, යවන ලද මුදල, සහ ගාස්තු. ගනුදෙනුව තහවුරු කර ඇති විට, අත්සනට ඉදිරියට යාමට වලංගු කරන්න.



![Image](assets/fr/46.webp)



පසුව Micro SD කාඩ්පත ඔබේ පරිගණකයට නැවත සම්බන්ධ කර, Sparrow හි "*Load Transaction*" මත ක්ලික් කරන්න. Coldcard මගින් අත්සන් කරන ලද PSBT ඔබේ ගොනු වලින් තෝරන්න.



![Image](assets/fr/47.webp)



You can see that the Coldcard signature has been added. I'm now going to use a second device, in this case the Ledger, to perform the second signature required. I connect it, unlock it, then click on "*Sign*" on Sparrow.



![Image](assets/fr/48.webp)



කොටස "*Sign*" මත ඔබා ඔබේ Hardware Wallet නම අසල.



![Image](assets/fr/49.webp)



පළමු වරට ඔබේ Ledger මෙම Multisig සමඟ භාවිතා කරන විට, Sparrow ඔබගෙන් සත්‍යාපනය කරන ලෙස ඉල්ලා සිටී. Coldcard සමඟ මෙන්ම, මෙම පියවරය පසුව අන්ධව අත්සන් කිරීමෙන් වළකින්න. මෙම තොරතුරු සත්‍යාපනය කිරීමට, Ledger තිරය මත පෙන්වන xpub ඔබේ අනෙක් දෘඩාංග පසුම්බි මගින් සපයන xpub සමඟ සසඳන්න.



![Image](assets/fr/50.webp)



Address, ලැබුණුකරුගේ, මාරුකළ මුදල සහ ගනුදෙනු ගාස්තුව පරීක්ෂා කර, ගනුදෙනුව අත්සන් කරන්න.



![Image](assets/fr/51.webp)



ස්ක्रीन එක ඔබා අත්සන් කරන්න.



![Image](assets/fr/52.webp)



Sparrow zdaj ima oba podpisa, ki sta potrebna za sprostitev sredstev iz portfelja Multisig. Preverite transakcijo še zadnjič, in če je vse v redu, kliknite na "*Broadcast Transaction*", da jo oddate prek omrežja.



![Image](assets/fr/53.webp)



ඔබට මෙම ගනුදෙනුව Sparrow Wallet හි "*Transactions*" ටැබ් එකේ සොයා ගත හැක.



![Image](assets/fr/54.webp)



සුභ පැතුම්, ඔබ දැන් Sparrow මත multisignature Wallet එකක් පිහිටුවා භාවිතා කරන ආකාරය දන්නවා. මෙම උපකාරකය ප්‍රයෝජනවත් වූවා නම්, Green අඟුලක් පහළින් දමා මට කෘතඥ වන්න. කරුණාකර මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බෙදා ගැනීම සඳහා ස්තුතියි!



තව දුරටත් යාමට, මම ඔබට Bitcoin Wallet, passphrase BIP39 හි ආරක්ෂාව වැඩි දියුණු කිරීම සඳහා වෙනත් ක්‍රමයක් පිළිබඳ මෙම උපකාරකය අනුගමනය කිරීමට නිර්දේශ කරමි:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7