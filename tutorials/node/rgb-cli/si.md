---
name: RGB CLI
description: Kako ustvarim in Exchange pametne pogodbe na RGB?
---
![cover](assets/cover.webp)


මෙම උපකාරිකාවේ, LNP/BP සංගමය විසින් නිර්මාණය කරන ලද `RGB` විධාන රේඛා මෙවලම භාවිතා කරමින් Contract ලිවීමේ පියවරෙන් පියවර ක්‍රියාවලිය අනුගමනය කරමු. අරමුණ වන්නේ CLI ස්ථාපනය කිරීම සහ ක්‍රියාත්මක කිරීම, Schema සංග්‍රහය, Interface සහ Interface Implementation ආයාත කිරීම, එවිට RGB වත්කමක් නිකුත් කිරීමේ ආකාරය පෙන්වීමයි. අපි මූලික තර්කය, සංග්‍රහය සහ රාජ්‍ය වලංගුකරණය ඇතුළුව බලන්නෙමු. මෙම උපකාරිකාව අවසානයේදී, ඔබට ක්‍රියාවලිය නැවත නිපදවා ඔබේම RGB ගිවිසුම් නිර්මාණය කළ හැකි විය යුතුය.


## RGB ප්‍රොටෝකෝලය මතක් කිරීම


RGB යනු Bitcoin මත ක්‍රියාත්මක වන සහ Smart contract ක්‍රියාකාරිතාව සහ ඩිජිටල් සම්පත් කළමනාකරණය අනුකරණය කරන, එහි පදනම වන Blockchain අධික බර නොදැමීමේ ප්‍රොටෝකෝලයකි. සාම්ප්‍රදායික On-Chain ස්මාර්ට් කොන්ත්‍රාත් (උදාහරණයක් ලෙස Ethereum මත) වලට වඩා, RGB "*Client-side Validation*" පද්ධතියක් මත රඳා පවතී: දත්ත සහ තත්ත්ව ඉතිහාසයන්ගේ බහුතරය සම්බන්ධ පාර්ශවකරුවන් විසින් පමණක් හුවමාරු කරනු ලබන අතර ගබඩා කරනු ලබන අතර, Bitcoin Blockchain කුඩා ක‍්‍රිප්ටෝග‍්‍රැෆික් ව්‍යාජයන් පමණක් සත්කාරකය ( *Tapret* හෝ *Opret* වැනි යාන්ත්‍රණ හරහා) ලෙස පවතී. RGB ප්‍රොටෝකෝලය තුළ, Bitcoin Blockchain එබැවින් කාල සටහන් සේවාදායකය සහ Double-spending ආරක්ෂණ පද්ධතියක් ලෙස පමණක් සේවය කරයි.


RGB Contract යනු විකාශනය වන රාජ්‍ය යන්ත්‍රයක් ලෙස ව්‍යුහගත වේ. එය Genesis සමඟ ආරම්භ වේ, එය Supply, ටිකර් හෝ අනෙකුත් මेटාදත්ත වැනි ආරම්භක රාජ්‍යය (විස්තර කිරීම) අර්ථ දක්වන Schema දැඩිව වර්ගීකරණය කර සම්පාදනය කරන පරිදි අර්ථ දක්වයි. රාජ්‍ය සංක්‍රමණ සහ අවශ්‍ය නම්, රාජ්‍ය දිගුවන් පසුව මෙම රාජ්‍යය සංශෝධනය කිරීමට හෝ දිගු කිරීමට යෙදවනු ලැබේ. RGB20 (විනියෝග කළ හැකි සම්පත් මාරු කිරීම) හෝ RGB21 (අද්විතීය සම්පත් නිර්මාණය කිරීම) වැනි සෑම මෙහෙයුමක්ම *තනි-භාවිත මුද්‍රා* සම්බන්ධ කරයි. මේවා Bitcoin UTXOවලින් off-chain රාජ්‍යයන්ට සම්බන්ධ කර, ද්විත්ව වියදම් වළක්වා, රහස්‍යතාවය සහ පරිමාණය සහතික කරයි.


RGB ප්‍රොටෝකෝලය කෙසේ ක්‍රියා කරන්නේද යන්න පිළිබඳව වැඩිදුර දැන ගැනීමට, මම ඔබට මෙම සම්පූර්ණ පුහුණු පාඨමාලාව අනුමත කරමි:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

RGB की आंतरिक तर्क Rust पुस्तकालयों पर आधारित है जिसे आप, डेवलपर्स के रूप में, अपने प्रोजेक्ट्स में *Client-side Validation* भाग को प्रबंधित करने के लिए आयात कर सकते हैं। इसके अलावा, LNP/BP टीम अन्य भाषाओं के लिए बाइंडिंग पर काम कर रही है, लेकिन यह अभी तक अंतिम रूप नहीं दिया गया है। इसके अलावा, Bitfinex जैसी अन्य संस्थाएँ अपने स्वयं के एकीकरण स्टैक विकसित कर रही हैं, लेकिन हम इनके बारे में किसी अन्य ट्यूटोरियल में बात करेंगे। फिलहाल, `RGB` CLI आधिकारिक संदर्भ है, भले ही यह अपेक्षाकृत अप्रशिक्षित है।


## RGB CLI මෙවලම ස්ථාපනය සහ ඉදිරිපත් කිරීම


ප්‍රධාන විධානය සරලව `RGB` ලෙස හැඳින්වේ. එය `git` මෙන් මතකයට ගෙන ඒමට නිර්මාණය කර ඇති අතර, ගිවිසුම් ක්‍රියාත්මක කිරීම, ඒවා කැඳවීම, සම්පත් නිකුත් කිරීම ආදී කටයුතු සඳහා උප-විධාන සමඟින් ඇත. Bitcoin Wallet දැනට ඒකාබද්ධ කර නොමැති නමුත් ඉක්මනින් නිකුත් කෙරෙන අනුවාදයක (0.11) ඒකාබද්ධ කෙරෙනු ඇත. මෙම ඊළඟ අනුවාදය මගින් පරිශීලකයින්ට ඔවුන්ගේ පසුම්බි (විස්තරකාරකයන් හරහා) සෘජුවම `RGB` මගින් නිර්මාණය කිරීමට සහ කළමනාකරණය කිරීමට හැකි වන අතර, PSBT ජනනය, අත්සන් කිරීම සඳහා බාහිර දෘඩාංග (උදා. Hardware Wallet) සමඟ අනුකූලතාව, සහ Sparrow වැනි මෘදුකාංග සමඟ අන්තර්ක්‍රියාකාරිත්වය ඇතුළත් වේ. මෙය සම්පත් නිකුත් කිරීම සහ මාරු කිරීමේ සම්පූර්ණ තත්ත්වය සරල කරනු ඇත.


### Cargo මඟින් ස්ථාපනය කිරීම


Orodje namestimo v Rust z:


```bash
cargo install rgb-contracts --all-features
```


(සටහන: පෙට්ටිය `RGB-contracts` ලෙස නම් කර ඇත, සහ ස්ථාපිත විධානය `RGB` ලෙස නම් කරනු ලැබේ. `RGB` නම් පෙට්ටියක් දැනටමත් තිබුණේ නම්, ගැටුමක් ඇති විය හැකි බැවින් නම මෙසේ ඇත)


ස්ථාපනය විශාල සංඛ්‍යාවක අනුභවයන් සංග්‍රහ කරයි (උදාහරණයක් ලෙස, විධාන විච්ඡේදනය, Electrum ඒකාබද්ධ කිරීම, ශූන්‍ය-දැනුම් සාක්ෂි කළමනාකරණය, ආදිය).


එක් වරක් ස්ථාපනය සම්පූර්ණ වූ විට, :


```bash
rgb
```


`RGB` ක්‍රියාත්මක කිරීම (වාද නොමැතිව) ලබා ගත හැකි උප-විධාන ලැයිස්තුවක් පෙන්වයි, `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, ආදී. ඔබට ස්ථානීය ගබඩා නාමාවලිය (සියලුම ලොග, රූපලේඛන සහ ක්‍රියාත්මක කිරීම් අඩංගු Stash) වෙනස් කළ හැක, ජාලය තෝරා ගත හැක (Testnet, Mainnet) හෝ ඔබේ Electrum සේවාදායකය වින්‍යාස කළ හැක.


![RGB-CLI](assets/fr/01.webp)


### නියාමකයන්ගේ පළමු සමාලෝකනය


කොමන්ඩ් එක ක්‍රියාත්මක කරන විට, ඔබට `RGB20` Interface එකක් දැනටමත් පෙරනිමි ලෙස ඒකාබද්ධ වී ඇති බව පෙනේ:


```bash
rgb interfaces
```


Če ta Interface ni integriran, klonirajte:


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


එය සංග්‍රහ කරන්න:


```bash
cargo run
```


පසුව ඔබ කැමති Interface ආනයනය කරන්න:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Vendar pa nam je povedano, da noben Schema še ni bil uvožen v programsko opremo. Prav tako ni Contract v Stash. Če ga želite videti, zaženite ukaz:


```bash
rgb schemata
```


ඔබට පසුව විශේෂිත සැකිලි ලබා ගැනීමට ගබඩාව පිටපත් කළ හැක:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


මෙම repository එකේ `src/` නාමාවලිය තුළ, Rust ගොනු කිහිපයක් (උදාහරණයක් ලෙස `nia.rs`) අඩංගු වේ, එමගින් ව්‍යුහයන් නිර්වචනය කරයි (NIA "*Non Inflatable Asset*" සඳහා, UDA "*Unique Digital Asset*" සඳහා, ආදිය). සංග්‍රහය සඳහා, ඔබට පසුව ධාවනය කළ හැක:


```bash
cd rgb-schemata
cargo run
```


මෙය සම්පාදිත රූපලේඛන වලට අදාළ `.RGB` සහ `.rgba` ගොනු කිහිපයක් ජනනය කරයි. උදාහරණයක් ලෙස, ඔබට `NonInflatableAsset.RGB` සොයාගත හැකිය.


### Schema සහ Interface Implementation ආනයනය කිරීම


ඔබට දැන් `RGB` වෙත සටහන ආයාත කළ හැක:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


මෙය දේශීය Stash වෙත එකතු කරයි. අපි පහත විධානය ක්‍රියාත්මක කළහොත්, දැන් Schema පෙනෙන බව අපට පෙනේ:


```bash
rgb schemata
```


## Contract නිර්මාණය (නිකුත් කිරීම)


නව සම්පතක් නිර්මාණය කිරීමට ආකාර දෙකක් ඇත:




- या तो हम Rust में एक स्क्रिप्ट या कोड का उपयोग करते हैं जो Schema फ़ील्ड्स (Global State, Owned States, आदि) को भरकर Contract बनाता है और एक `.RGB` या `.rgba` फ़ाइल उत्पन्न करता है;
- අනෙකා `issue` උප-විධානය සෘජුවම භාවිතා කරන්න, ටෝකනයේ ගුණාංග විස්තර කරන YAML (හෝ TOML) ගොනුවක් සමඟ.


ඔබට `examples` ෆෝල්ඩරය තුළ Rust හි උදාහරණ සොයා ගත හැකි අතර, එය `ContractBuilder` එකක් කෙසේ ගොඩනඟන්නේද යන්න පැහැදිලි කරයි, `Global State` (සම්පත් නාමය, ටිකර්, Supply, දිනය, ආදිය) පුරවන්න, Owned State (එය UTXO කුමකට පැවරෙනවාද යන්න) නිර්වචනය කරන්න, එවිට මෙය සියල්ල *Contract Consignment* එකක් බවට සංග්‍රහය කර, ඔබට Stashකට අපනයනය, වලංගු කිරීම සහ ආයාත කිරීම කළ හැකිය.


වෙනත් ක්‍රමය වන්නේ `ticker`, `name`, `Supply` ආදී අභිරුචිකරණය කිරීමට YAML ගොනුවක් අතින් සංස්කරණය කිරීමයි. ගොනුව `RGB20-demo.yaml` ලෙස නම් කර ඇතැයි فرض කරන්න. ඔබට විශේෂිත කළ හැක:




- `spec`: ticker, name, precision ;
- `terms`: pravno obvestilo ;
- `issuedSupply` : නිකුත් කරන ලද ටෝකන ප්‍රමාණය ;
- `assignments`: Single-Use Seal (*Seal Definition*) සහ විවෘත ප්‍රමාණය සදහන් වේ.


Tukaj je primer datoteke YAML za ustvarjanje:


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-CLI](assets/fr/05.webp)


පසුව සරලව විධානය ක්‍රියාත්මක කරන්න :


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


මගේ අවස්ථාවේ, අනන්‍ය Schema හඳුනාගැනීමකරු (තනි උද්ධෘත ලකුණු තුළ සවිකරන්න) වන්නේ `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` සහ මම කිසිදු නිකුත්කරුක් දැමූයේ නැත. එසේනම් මගේ ඇණවුම වන්නේ :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


If you don't know the Schema ID, run the command :


```bash
rgb schemata
```


CLI නව Contractක් නිකුත් කර ඇති අතර එය Stashට එක් කර ඇති බව පිළිතුරු දෙයි. අපි පහත විධානය ටයිප් කළහොත්, නව Contractක් දැන් ඇති බව, නිකුත් කළ එකට අදාළව දැක ගත හැක:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


එවිට, ඊළඟ විධානය ගෝලීය රාජ්‍යයන් (නම, ටිකර්, Supply...) සහ අයිති රාජ්‍යයන්ගේ ලැයිස්තුව, එනම් වෙන්කිරීම් (උදාහරණයක් ලෙස, UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1` හි නිර්වචිත මිලියන 1 `PBN` ටෝකන) ප්‍රදර්ශනය කරයි.


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## අපනයන, ආනයන සහ වලංගුකරණය


Contract මෙම භාවිතා කරන්නන් සමඟ බෙදා ගැනීම සඳහා, එය Stash වෙතින් :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


`myContractPBN.RGB` දත්ත ගොනුව වෙනත් පරිශීලකයෙකුට ලබා දිය හැකි අතර, ඔහුට එය Stash වෙත එක් කිරීමට පහත විධානය භාවිතා කළ හැක:


```bash
rgb import myContractPBN.rgb
```


Ob uvozu, če gre za preprosto *Contract Consignment*, bomo dobili sporočilo "`Importing Consignment RGB`". Če gre za večji *State Transition Consignment*, bo ukaz drugačen (`RGB accept`).


වලංගුතාවය සහතික කිරීම සඳහා, ඔබට දේශීය වලංගුකරණ ක්‍රියාවලියද භාවිතා කළ හැක. උදාහරණයක් ලෙස, ඔබට ධාවනය කළ හැක :


```bash
rgb validate myContract.rgb
```


### Stash භාවිතය, සත්‍යාපනය සහ ප්‍රදර්ශනය


Kot opomnik, Stash je lokalni inventar shem, vmesnikov, implementacij in pogodb (Genesis + prehodi). Vsakič, ko zaženete "import", dodate element v Stash. Ta Stash si lahko podrobno ogledate s ukazom :


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


මෙය generate ගොනුවක් වන අතර සම්පූර්ණ Stash විස්තර අඩංගු වේ.


## මාරු කිරීම සහ PSBT


Če želite izvesti prenos, boste morali upravljati lokalni Bitcoin Wallet za upravljanje obveznosti `Tapret` ali `Opret`.


### generate an Invoice


බොහෝ අවස්ථාවලදී, Contract හි සහභාගීවන්නන් (උදාහරණයක් ලෙස ඇලීස් සහ බොබ්) අතර අන්තර්ක්‍රියාව Invoice එකක් ජනනය කිරීම හරහා සිදු වේ. ඇලීස්ට බොබ් විසින් කිසියම් දෙයක් ක්‍රියාත්මක කිරීමට (ටෝකන් මාරු කිරීමක්, නැවත නිකුත් කිරීමක්, DAO එකක ක්‍රියාවක්, ආදිය) අවශ්‍ය නම්, ඇලීස් බොබ්ට ඇයගේ උපදෙස් විස්තර කරන Invoice එකක් සෑදේ. එසේ නම් අපට ඇත:




- Alice** (Invoice හි නිකුත්කරු) ;
- බොබ්** (Invoice ලබා ගෙන ක්‍රියාත්මක කරන).


Za razliko od drugih ekosistemov, RGB Invoice ni omejen na pojem plačila. Lahko vključi katero koli zahtevo, povezano z Contract: preklic ključa, glasovanje, ustvarjanje gravure (*gravura*) na NFT itd. Ustrezno operacijo je mogoče opisati v Contract Interface. Ustrezno operacijo je mogoče opisati v Contract Interface.


පහත විධානය RGB Invoice එකක් ජනනය කරයි:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


සමඟ :




- `$Contract`: Contract හඳුනාගැනීම (*ContractId*) ;
- `$Interface`: Interface භාවිතා කිරීමට (උදා. `RGB20`) ;
- `$ACTION`: Interface හි විශේෂිත කරන ලද මෙහෙයුමේ නම (සරල හුවමාරු කළ හැකි ටෝකන් මාරු කිරීම සඳහා, මෙය "Transfer" විය හැක). Interface දැනටමත් පෙරනිමි ක්‍රියාවක් සපයන්නේ නම්, ඔබට මෙහි නැවත ඇතුළත් කිරීමට අවශ්‍ය නොවේ;
- `$STATE`: ස්ථානයේ දත්ත මාරු කිරීමට (උදාහරණයක් ලෙස, මාරු කරන ලද ෆන්ජිබල් ටෝකනයක් නම් ටෝකන ප්‍රමාණයක්);
- `$Seal`: ප්‍රතිලාභීගේ (ඇලීසගේ) Single-Use Seal, එනම් UTXO කට පැහැදිලි යොමු කිරීමකි. බොබ් මෙම තොරතුරු භාවිතා කර Witness Transaction සකසනු ඇත, සහ අදාළ ප්‍රතිදානය එවිට ඇලීසට අයත් වනු ඇත (*blinded UTXO* හෝ කේතනය නොකළ ආකාරයෙන්).


උදාහරණයක් ලෙස, පහත විධාන සමඟ


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI යනු generate සහ Invoice වැනි :


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


To lahko prenesete Bobu prek katerega koli kanala (besedilo, QR koda itd.).


### Making a transfer


Za prenos iz tega Invoice :




- බොබ් (ඔහුගේ Stash හි ටෝකන අත්හිටුවා ඇති) Bitcoin Wallet එකක් ඇත. ඔහුට Bitcoin ගනුදෙනුවක් (PSBT ආකාරයෙන්, උදාහරණයක් ලෙස `tx.PSBT`) සකස් කිරීමට අවශ්‍ය වන අතර එහිදී අවශ්‍ය RGB ටෝකන පිහිටා ඇති UTXOs වියදම් කරන අතර, මුදල් සඳහා එක් UTXO (Exchange) එකක්ද ඇතුළත් වේ;
- බොබ් පහත විධානය ක්‍රියාත්මක කරයි:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- මෙය `Consignment.RGB` ගොනුවක් ජනනය කරයි, එය අඩංගු වේ :
 - ඇලිස්ට ටෝකන සත්‍ය බව පෙන්වන සංක්‍රමණ ඉතිහාසය;
 - නව මාරුව Single-Use Seal ටෝකන ඇලීසට මාරු කරයි ;
 - Witness Transaction (අත්සන නොකළ).
- බොබ් මෙම `Consignment.RGB` ගොනුව ඇලීසට යවයි (ඊ-තැපැල්, හුවමාරු සේවාදායකය හෝ RGB-RPC ප්‍රොටෝකෝලයක්, ස්ටෝම්, ආදිය මඟින්);
- Alice prejme `Consignment.RGB` in ga sprejme v svojem Stash :


```bash
alice$ rgb accept consignment.rgb
```




- CLI මාරුවේ වලංගුභාවය පරීක්ෂා කර Aliceගේ Stash වෙත එය එක් කරයි. වලංගු නොවේ නම්, විධානය අසාර්ථක වන අතර විස්තරාත්මක දෝෂ පණිවිඩ ලබා දේ. නැතහොත්, එය සාර්ථක වන අතර, සාම්පල ගනුදෙනුව Bitcoin ජාලය මත තවමත් විකාශය කර නොමැති බව වාර්තා කරයි (Bob, Aliceගේ Green ආලෝකය බලා සිටී);
- Kot potrditev ukaz `accept` vrne podpis (*plačilni list*), ki ga lahko Alice pošlje Bobu, da mu pokaže, da je potrdila *Consignment* ;
- බොබ්ට පසුව Bitcoin ගනුදෙනුව අත්සන් කර ප්‍රකාශයට පත් කළ හැක (`--publish`):


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- මෙම ගනුදෙනුව On-Chain තහවුරු වීමත් සමගම, සම්පත් Ownership ඇලීස් වෙත මාරු වූ ලෙස සැලකේ. ගනුදෙනුවේ Mining අධීක්ෂණය කරන ඇලීස්ගේ Wallet, එහි Stash තුළ නව Owned State පෙනේ.


ඔබ දැන් RGB Contract නිකුත් කිරීම සහ මාරු කිරීම කෙසේද යන්න දන්නවා. මෙම උපකාරකය ප්‍රයෝජනවත් වූවා නම්, Green අඟුලක් පහළට දාන්නට මම ඉතාමත්ම කෘතඥ වනු ඇත. කරුණාකර මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තුතියි!


මම තවදුරටත් මෙම වෙනත් උපකාරකය නිර්දේශ කරමි, එහිදී මම RGB-අනුකූල Lightning node එකක් Exchange ටෝකන වෙත සනාථව almost launch කරන ආකාරය පැහැදිලි කරමි:


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea