---
name: Slipstream
description: Slipstream භාවිතයෙන් අත්සන් කළ ගනුදෙනුවක් Bitcoin ජාලයට විකාශය නොකර, කෙළින්ම miner කෙනෙකු වෙත යැවීම
---

![කවරය](assets/cover.webp)

සාමාන්‍යයෙන්, ඔබ ගනුදෙනුවකට අත්සන් කළ විට, එය ජාලයේ සෑම Bitcoin node එකකටම ස්වයංක්‍රීයව විකාශය වේ. ඉන්පසු එය mined වීමට බලා සිටී.

නමුත්, එය block එකක නොමැති තාක් කාලය තුළ, ඔබේ private key ලබාගත් ප්‍රහාරකයෙකුට එය ප්‍රතිස්ථාපනය කර අරමුදල් සොරකම් කළ හැක. ඔබ ColdCard hardware wallet එකක් භාවිතා කරන විට මෙය සාමාන්‍යයෙන් සිදුවිය හැකි අවස්ථාවකි.

Mining සමාගමක් වන MARA හි Slipstream මෙවලම, ගනුදෙනුව ජාලයට විකාශය කිරීම මඟහැරීමට ඔබට ඉඩ සලසයි: එය කෙළින්ම (සහ පමණක්) miner කෙනෙකු වෙත යවනු ලැබේ, එම miner එය පුද්ගලිකව තබා ගෙන ජාලයේ එය නිරාවරණය වීම වළක්වයි. ගනුදෙනුව mined වීමට සමහර විට වැඩි කාලයක් ගත විය හැක, නමුත් එය replacement attack එකකට එරෙහිව ආරක්ෂා වේ.

පහතින්, අපි [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) පරිශීලකයින්ට මෙන්ම [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) wallet පරිශීලකයින්ටද, [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) පිටුව හරහා miner MARA හි Slipstream මෙවලම භාවිතා කිරීමට ඉඩ සලසන නිබන්ධනයක් ලබා දෙමු.

⚠️ **අවවාදයයි**: මෙම මෙවලම අදහස් කර ඇත්තේ විශේෂිත profile කිහිපයක් සඳහා පමණි, ප්‍රධාන වශයෙන් Liana wallets, miniscript wallets සහ multisig වර්ග කිහිපයක් සඳහායි. Wizardsardine, අරමුදල් දැනටමත් සොරකම් වීමේ තීරණාත්මක අවදානමක ඇති wallets සඳහා මෙය භාවිතා කිරීම **පැහැදිලිවම අනුමත නොකරයි**; උදාහරණයක් ලෙස random number generator දුර්වලතාවයට ලක් වූ ColdCard device එකක ජනනය කළ recovery phrase ඇති wallets. එවැනි අවස්ථාවක, ප්‍රහාරකයාට එරෙහි තරඟය තත්පර කිහිපයක ප්‍රශ්නයක් වන අතර, එක් miner කෙනෙකු වෙත පමණක් යවන ගනුදෙනුවක් සාමාන්‍යයෙන් විකාශය කරන ගනුදෙනුවකට වඩා තහවුරු වීමට බොහෝ වැඩි කාලයක් ගනී. මෙය ඔබට අදාල නම්, පළමුව අපගේ කැපවූ නිබන්ධනය කියවන්න:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Liana පරිශීලකයින් සඳහා

Liana, [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) පිටුව ප්‍රකාශයට පත් කරන Wizardsardine විසින් නඩත්තු කරනු ලබයි, එබැවින් මාර්ගය සෘජුයි: ඔබ ගනුදෙනුව විකාශය කිරීම වෙනුවට අත්සන් කළ PSBT file එක export කරයි.

*පූර්ව අවශ්‍යතාව: ඔබේ Liana wallet එකේ අරමුදල් තිබිය යුතුය.*

### පියවර 1: Liana සමඟ ඔබේ ගනුදෙනුව නිර්මාණය කරන්න

සාමාන්‍ය පරිදි, destination address එක, විස්තරය, සහ ප්‍රමාණය (මෙහි, wallet එකේ ලබාගත හැකි උපරිම ප්‍රමාණය) එකතු කර ඔබේ ගනුදෙනුව ගොඩනගන්න.

Fee rate එක සකසීමට:

- පහළ වම් පස ඇති "Coins selection" යටතේ ඇති කුඩා කොටුව ක්ලික් කර, ඔබ වියදම් කිරීමට කැමති coins තෝරන්න;
- ඉන්පසු fee rate එක ඇතුළත් කරන්න. මෙම පිටුවේ විස්තර කර ඇති පරිදි, යෝජිත rate එකට වඩා බොහෝ ඉහළ fees සකසන්න: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

අවසානයේ, "Next" ක්ලික් කරන්න.

![Liana තුළ ගනුදෙනුව ගොඩනැගීම](assets/fr/01.webp)

### පියවර 2: ඔබේ ගනුදෙනු විස්තර පරීක්ෂා කරන්න

"Sign" ක්ලික් කිරීමට පෙර, ඔබේ ගනුදෙනු විස්තර පරීක්ෂා කරන්න; විශේෂයෙන්:

- යවන ප්‍රමාණය;
- transaction fees සඳහා වෙන් කළ satoshis ගණන;
- නමුත් සියල්ලටම වඩා, ඔබ අරමුදල් යවන address එක ("address poisoning" attacks වළක්වා ගැනීමට address එකේ පළමු 5/6 අක්ෂර, අවසන් 5/6, සහ මැද 5/6 අක්ෂර පරීක්ෂා කිරීමට මතක තබා ගන්න).

![ගනුදෙනු විස්තර පරීක්ෂා කිරීම](assets/fr/02.webp)

### පියවර 3: අත්සන් කරන wallets තෝරන්න

ඊළඟට, ඔබේ ගනුදෙනුවට අත්සන් කිරීමට අවශ්‍ය software සහ/හෝ hardware wallets තෝරන්න. ඉක්මන් මතක් කිරීමක්: 2-of-2 multisig wallet එකක් වන විට, ඔබට 2 න් 2 signatures අවශ්‍ය වේ.

### පියවර 4: ඔබේ ගනුදෙනුවේ PSBT file එක export කරන්න

Bitcoin ගනුදෙනුව දැන් අදාළ keys මඟින් අත්සන් කර ඇත. "Broadcast" ක්ලික් නොකරන්න; එසේ කළහොත් එය සම්පූර්ණ ජාලය සමඟ බෙදාගනු ඇති අතර, ඔබ ColdCard hardware wallet එකක් භාවිතා කරන්නේ නම්, ඔබේ ගනුදෙනුව පොදුවේ නිරාවරණය වී ඔබේ අරමුදල් අවදානමට ලක් වේ.

දැන් ඔබට "Export" ක්ලික් කර, PSBT file එක ඔබේ පරිගණකයේ දේශීයව සුරැකිය හැක.

![Liana වෙතින් PSBT file එක export කිරීම](assets/fr/03.webp)

### පියවර 5: outofband.wizardsardine.com හරහා ගනුදෙනුව miner වෙත යවන්න

දැන් අවසාන පියවරයන්. ගනුදෙනුව miner වෙත යැවීමට, ඔබ කළ යුත්තේ PSBT file එක ගෙන නියමිත ප්‍රදේශයට drag and drop කිරීම පමණි.

![PSBT file එක outofband.wizardsardine.com මත දැමීම](assets/fr/04.webp)

ඉන්පසු ගනුදෙනුව පහත පරිදි පෙන්වනු ලැබේ.

![queue එකේ ඇති ගනුදෙනුව](assets/fr/05.webp)

### පියවර 6: Slipstream හරහා ගනුදෙනුව යවන්න

අවසානයේ, ගනුදෙනුව Slipstream හරහා MARA වෙත යවීමට "Send" ක්ලික් කිරීම පමණයි කළ යුතු.

![Slipstream හරහා ගනුදෙනුව යැවීම](assets/fr/06.webp)

තත්පර කිහිපයක් ඇතුළත, ගනුදෙනුව "Sending" සිට "Accepted" වෙත මාරු වේ:

![Slipstream විසින් ගනුදෙනුව පිළිගැනීම](assets/fr/07.webp)

ඉතිරිව ඇත්තේ transaction identifier (TXID) පිටපත් කර, එය mined වන ආකාරය නැරඹීමට [mempool.space](https://mempool.space/) තුළ අලවීම පමණි:

![mempool.space මත TXID සොයා බැලීම](assets/fr/08.webp)

කරුණාකර සටහන් කරන්න: miner වන MARA, block එකක් mine කර ඔබේ ගනුදෙනුව එයට ඇතුළත් කරන තෙක් ගනුදෙනුව "Transaction not found" ලෙස පෙන්වනු ඇත. මෙයට විනාඩි දස ගණනක්, නැතහොත් පැය ගණනක් පවා ගත විය හැක, මන්ද MARA සතුව Bitcoin ජාලයේ hash rate එකෙන් ආසන්න වශයෙන් 4.5% ක් පමණක් ඇත. 2026 අගෝස්තු 4 වනදා වන විට, මෙය සාමාන්‍යයෙන් පැය 3 සහ විනාඩි 45 කට වරක් mined වන එක් block එකකට සමාන වේ.

## වෙනත් wallets පරිශීලකයින් සඳහා

ඔබ [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) භාවිතා නොකරන නමුත් මෙවලම තවමත් භාවිතා කිරීමට කැමති නම්, මෙහි 2-of-2 multisig wallet එකක් භාවිතා කරන නිබන්ධනයක් ඇත. මෙය කිරීමට, අපි [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) software wallet එක භාවිතා කරමු.

*පූර්ව අවශ්‍යතාව: ඔබේ Sparrow wallet එකේ අරමුදල් තිබිය යුතුය.*

### පියවර 1: ඔබේ ගනුදෙනුව නිර්මාණය කරන්න

[Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) සමඟ, ඔබේ multisig wallet එකේ ගනුදෙනුව නිර්මාණය කරන්න. මෙම පිටුවේ විස්තර කර ඇති පරිදි, යෝජිත rate එකට වඩා බොහෝ ඉහළ fees සකසන්න: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

නිර්මාණය කළ පසු, "Create Transaction" ක්ලික් කරන්න.

![Sparrow තුළ ගනුදෙනුව නිර්මාණය කිරීම](assets/fr/09.webp)

### පියවර 2: ඔබේ ගනුදෙනුව අවසන් කරන්න

ඔබේ ගනුදෙනුව අවසන් කිරීමට, දැන් එයට අත්සන් කළ යුතුය. මෙය කිරීමට, "Finalize Transaction for Signing" ක්ලික් කරන්න.

![අත්සන් කිරීම සඳහා ගනුදෙනුව අවසන් කිරීම](assets/fr/10.webp)

### පියවර 3: ඔබේ විවිධ keys සමඟ ඔබේ ගනුදෙනුවට අත්සන් කරන්න

දැන් ගනුදෙනුවට අත්සන් කිරීමට කාලයයි. මෙය කිරීමට, ඔබ භාවිතා කරන software හෝ hardware wallet(s) සමඟ එයට අත්සන් කිරීම පමණි.

![multisig keys සමඟ ගනුදෙනුවට අත්සන් කිරීම](assets/fr/11.webp)

### පියවර 4: අත්සන් කළ ගනුදෙනුව download කරන්න, එය ජාලයට විකාශය නොකරන්න

Bitcoin ගනුදෙනුව දැන් අපගේ 2-of-2 multisig හි keys දෙකම මඟින් අත්සන් කර ඇත. "Broadcast Transaction" ක්ලික් නොකරන්න; එසේ කළහොත් එය සම්පූර්ණ ජාලය සමඟ බෙදාගනු ඇති අතර, ඔබ ColdCard hardware wallet එකක් භාවිතා කරන්නේ නම්, ඔබේ ගනුදෙනුව පොදුවේ නිරාවරණය වී ඔබේ අරමුදල් අවදානමට ලක් වේ.

![අත්සන් කළ ගනුදෙනුව, සූදානම් නමුත් විකාශය කර නැත](assets/fr/12.webp)

### පියවර 5: අත්සන් කළ transaction script එක පෙන්වන්න, නැතහොත් PSBT file එක download කරන්න

අත්සන් කළ Bitcoin ගනුදෙනුව පෙන්වීමට, දැන් "View Final Transaction" ක්ලික් කරන්න. ඉන්පසු ඔබට අත්සන් කළ Bitcoin transaction script එක පිටපත් කළ හැක:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![අත්සන් කළ transaction script එක පෙන්වීම](assets/fr/13.webp)

ඔබට transaction file එක download කිරීමට අවශ්‍ය නම්, ඔබට මෙවැනි දෙකෙන් එකක් කළ හැක:

- "File" ක්ලික් කර, ඉන්පසු "Save transaction…" ක්ලික් කරන්න;
- නැතහොත් පහළ දකුණු පස ඇති network connection button එක (කහ බොත්තම) ක්ලික් කර, ඉන්පසු "Save Final Transaction" ක්ලික් කරන්න.

ඉන්පසු ගනුදෙනුව ඔබේ පරිගණකයේ දේශීයව සුරැකෙනු ඇත.

![අවසන් ගනුදෙනුව දේශීයව සුරැකීම](assets/fr/14.webp)

### පියවර 6: outofband.wizardsardine.com හරහා ගනුදෙනුව miner වෙත යවන්න

දැන් අවසාන පියවරයන්. ගනුදෙනුව miner වෙත යැවීමට, ඔබ කළ යුත්තේ:

- [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) වෙත යන්න;
- පෙර පියවරේ පිටපත් කළ අත්සන් කළ transaction script එක අලවා, පහළ ඇති "ADD TO QUEUE" ක්ලික් කරන්න;

![transaction script එක මෙවලමට අලවීම](assets/fr/15.webp)

- නැතහොත් file එක ගෙන නියමිත ප්‍රදේශයට drag and drop කරන්න.

![transaction file එක මෙවලම මත දැමීම](assets/fr/16.webp)

ඉන්පසු ගනුදෙනුව පහත පරිදි පෙන්වනු ලැබේ.

![queue එකේ ඇති ගනුදෙනුව](assets/fr/17.webp)

ඔබේ ගනුදෙනුවේ මුළු input amount of satoshis නොදන්නා බව (ඒ නිසා fees සඳහා satoshis ගණන ගණනය කළ නොහැකි බව) පණිවිඩයක් කියන්නේ නම්, ඔබ සරලවම මුළු input amount of satoshis අතින් ඇතුළත් කළ යුතුය. එය සොයා ගැනීමට, Sparrow තුළ diagram එකේ මැද ඔබේ ගනුදෙනුවේ display එක මත ක්ලික් කිරීම පමණයි කළ යුතු:

![Sparrow තුළ පෙන්වන මුළු input amount](assets/fr/18.webp)

ඉන්පසු එම ප්‍රමාණය (අපගේ උදාහරණයේ sats 15,904) [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) මෙවලමට ඇතුළත් කරන්න:

![මුළු input amount අතින් ඇතුළත් කිරීම](assets/fr/19.webp)

අවසානයේ, fee rate එක නිවැරදි බව පරීක්ෂා කරන්න.

### පියවර 7: Slipstream හරහා ගනුදෙනුව යවන්න

අවසානයේ, ගනුදෙනුව Slipstream හරහා MARA වෙත යවීමට "Send" ක්ලික් කිරීම පමණයි කළ යුතු.

![Slipstream හරහා ගනුදෙනුව යැවීම](assets/fr/20.webp)

තත්පර කිහිපයක් ඇතුළත, ගනුදෙනුව "Sending" සිට "Accepted" වෙත මාරු වේ:

![Slipstream විසින් ගනුදෙනුව පිළිගැනීම](assets/fr/21.webp)

ඉතිරිව ඇත්තේ transaction identifier (TXID) පිටපත් කර, එය mined වන ආකාරය නැරඹීමට [mempool.space](https://mempool.space/) තුළ අලවීම පමණි:

![mempool.space මත TXID සොයා බැලීම](assets/fr/22.webp)

කරුණාකර සටහන් කරන්න: miner වන MARA, block එකක් mine කර ඔබේ ගනුදෙනුව එයට ඇතුළත් කරන තෙක් ගනුදෙනුව "Transaction not found" ලෙස පෙන්වනු ඇත. මෙයට විනාඩි දස ගණනක්, නැතහොත් පැය ගණනක් පවා ගත විය හැක, මන්ද MARA සතුව Bitcoin ජාලයේ hash rate එකෙන් ආසන්න වශයෙන් 4.5% ක් පමණක් ඇත. 2026 අගෝස්තු 4 වනදා වන විට, මෙය සාමාන්‍යයෙන් පැය 3 සහ විනාඩි 45 කට වරක් mined වන එක් block එකකට සමාන වේ.
