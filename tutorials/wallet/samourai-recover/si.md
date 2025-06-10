---
name: Samourai Wallet - Recover
description: Kako obnoviti bitcoine, ki so obtičali na Samourai Wallet?
---

![cover](assets/cover.webp)


සමුරායි Wallet හි ආරම්භකයින් අත්අඩංගුවට ගත් පසු සහ ඔවුන්ගේ සේවාදායකයන් අප්‍රේල් 24 වන දින අත්පත් කර ගැනීමෙන් පසු, යෙදුමේ කීපයක් ක්‍රියාත්මක නොවන අතර, තමන්ගේම ඩෝජෝ නොමැති පරිශීලකයින්ට දැන් ගනුදෙනු විකාශය කළ නොහැක.


Po pomoči več uporabnikom pri obnovi njihovih bitcoinov v zadnjih dneh verjamem, da sem naletel na večino težav, ki se lahko pojavijo med obnovo Samourai Wallet. Zato bo ta vadnica začela s poročilom o stanju, da bi identificirali funkcionalnosti, ki ostajajo operativne, in tiste, ki niso več na voljo znotraj ekosistema Samourai Wallet ter programsko opremo, ki jo je prizadel ta incident. Nato bomo korak za korakom nadaljevali z obnovo Samourai Wallet z uporabo programske opreme Sparrow Wallet. Preučili bomo vse potencialne ovire, s katerimi se srečamo med tem procesom, in videli rešitve za njihovo odpravo. Na koncu, v zadnjem delu, boste odkrili potencialna tveganja za vašo zasebnost po zasegu strežnika.


_[@Louferlou](https://twitter.com/Louferlou)ට විශාල ස්තූතියි, ඔහු පරිශීලකයන් කිහිප දෙනෙකුට ඔවුන්ගේ සුවය ලබා ගැනීමට සහය වූ අතර ඔහුගේ අත්දැකීම් මට බෙදා ගත් අතර, තවම ක්‍රියාත්මක වන දේ තීරණය කිරීමට පරීක්ෂා කිරීමට ද දායක වූවා._


## Ali Samourai Wallet še vedno deluje?


ඔව්, **Samourai Wallet යෙදුම තවම ක්‍රියාත්මක වේ**, නමුත් විශේෂිත කොන්දේසි යටතේ.


පළමුව, ඔබේ ස්මාර්ට්ෆෝනයේ මෘදුකාංගය පෙර ස්ථාපනය කර තිබීම අවශ්‍ය වේ. ගූගල් ප්ලේ ස්ටෝර් මෘදුකාංගය ඉවත් කර ඇති අතර, APK එක අත්අඩංගුවට ගත් වෙබ් අඩවිය මත සත්කාර කර තිබුණි. එබැවින්, මේ මොහොතේ Samourai ස්ථාපනය කිරීම සංකීර්ණ වේ. ඔබට APKs අන්තර්ජාලයෙන් සොයාගත හැකි විය හැක, නමුත් මම ඔබට මූලාශ්‍රය පිළිබඳව විශ්වාසයක් නැති නම් ඒවා බාගත කිරීමෙන් වළකින්නැයි උපදෙස් දෙමි.


සමුරායි Wallet පිටුව දැන් Google Play Store හි නොමැති බැවින් ස්වයංක්‍රීය යාවත්කාලීන කිරීම් අක්‍රීය කිරීම නොහැක. යෙදුම නැවත බාගත කිරීමේ වේදිකාවලට පැමිණේ නම්, කේස් සංවර්ධනය පිළිබඳව වැඩි විස්තර ලබා ගත හැකි වන තෙක් **ස්වයංක්‍රීය යාවත්කාලීන කිරීම් අක්‍රීය කිරීම** සුදුසුය.


If Samourai Wallet is already installed on your smartphone, you should still be able to access the app. To use the Wallet functionality of Samourai, it is essential to connect a Dojo. Previously, users without a personal Dojo depended on Samourai's servers to access Bitcoin Blockchain information and to broadcast transactions. With the seizure of these servers, the app can no longer access this data.

Če prej niste imeli povezanega Dojo, zdaj pa ga imate, ga lahko nastavite za ponovno uporabo aplikacije Samourai. To vključuje preverjanje vaših varnostnih kopij, brisanje Wallet (Wallet, ne aplikacije) in obnovitev Wallet s povezovanjem Dojo z aplikacijo. Za več podrobnosti o teh korakih si lahko ogledate [ta vodič, v razdelku "_Priprava vaše denarnice Samourai_" : CoinJoin - DOJO](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2).

ඔබගේ Samourai යෙදුම දැනටමත් ඔබේම Dojo සමඟ සම්බන්ධ කර තිබුණේ නම්, Wallet කොටස ඔබට පරිපූර්ණ ලෙස ක්‍රියා කරයි. ඔබට තවමත් ඔබේ ශේෂය දැකීමට සහ ගනුදෙනු විකාශය කිරීමට හැකිය. සිදුවන සියල්ලටම පසුව, මම සිතන්නේ Samourai Wallet මේ මොහොතේ හොඳම ජංගම Wallet මෘදුකාංගය බව. පුද්ගලිකව, මම එය භාවිතා කිරීම දිගටම කරගෙන යාමට සැලසුම් කරමි.


ඔබට මුහුණ දිය හැකි ප්‍රධාන ගැටලුව වන්නේ යෙදුමෙන් Whirlpool ගිණුම් ප්‍රවේශය නොමැති වීමයි. සාමාන්‍යයෙන්, Samourai ඔබේ Whirlpool CLI සමඟ සම්බන්ධතාවයක් ස්ථාපිත කිරීමට උත්සාහ කරයි සහ මෙම ගිණුම්වලට ප්‍රවේශය ලබා දීමට පෙර CoinJoin චක්‍ර ආරම්භ කරයි. කෙසේ වෙතත්, මෙම සම්බන්ධතාවය දැන් සිදු නොවන බැවින්, යෙදුම අඛණ්ඩව සොයමින් සිටී Whirlpool ගිණුම්වලට ප්‍රවේශය ලබා දීමකින් තොරව. මෙම අවස්ථාවේදී, Samourai මත තැන්පතු ගිණුම පමණක් තබා ගනිමින්, මෙම ගිණුම් වෙනත් Wallet මෘදුකාංගයකින් ප්‍රතිසාධනය කළ හැක.


### Samourai-ju na voljo še vedno kateri orodja?


අනෙක් අතට, සමහර මෙවලම් සේවාදායකය අක්‍රීය කිරීමෙන් බලපෑමට ලක් වන අතර හෝ සම්පූර්ණයෙන්ම ලබා ගත නොහැක.


විෂය පුද්ගලික වියදම් මෙවලම් සම්බන්ධයෙන් වන විට, ඔබට ඔබේම Dojo තිබේ නම්, සෑම දෙයක්ම සාමාන්‍ය ලෙස ක්‍රියා කරයි. සාමාන්‍ය Stonewall ගනුදෙනු (Stonewall x2 නොව) කිසිදු ගැටළුවකින් තොරව ක්‍රියා කරයි.


Na Twitterju so se pojavili komentarji, da je zasebnost, ki jo ponuja transakcija Stonewall, zdaj morda zmanjšana. Dodana vrednost transakcije Stonewall je v tem, da je po strukturi neločljiva od transakcije Stonewall x2. Ko analitik naleti na ta specifičen vzorec, ne more ugotoviti, ali gre za standardni Stonewall z enim uporabnikom ali Stonewall x2, ki vključuje dva uporabnika. Vendar, kot bomo videli v naslednjih odstavkih, je izvajanje transakcij Stonewall x2 postalo bolj zapleteno zaradi nedostopnosti Sorobana. Nekateri zato menijo, da bi analitik zdaj lahko domneval, da je vsaka transakcija s to strukturo običajen Stonewall. Osebno se s to domnevo ne strinjam. Čeprav so transakcije Stonewall x2 morda manj pogoste (in mislim, da so bile že pred tem dogodkom), dejstvo, da so še vedno možne, lahko razveljavi celotno analizo, ki temelji na predpostavki, da niso.

**[-> Stonewall ගනුදෙනු පිළිබඳව වැඩිදුර ඉගෙන ගන්න.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

Ricochet පිළිබඳව, Testnet මත Dojo එකක් හිමිකර නොගැනීම හේතුවෙන්, සේවාව තවම ක්‍රියාත්මකද යන්න සනාථ කිරීමට මට හැකි වී නැත, සහ මම අධිකාරීන් විසින් පාලනය කළ හැකි Wallet කට `100 000 Sats` වියදම් කිරීමට අවදානමක් නොගන්න කැමති. ඔබට මේ මෙවලම මෑතකදී පරීක්ෂා කිරීමට අවස්ථාව ලැබී ඇත්නම්, අපට මෙම ලිපිය යාවත්කාලීන කළ හැකි වන පරිදි මට සම්බන්ධ වන්න.


ඔබට Ricochet භාවිතා කිරීමට අවශ්‍ය නම්, ඔබට ඕනෑම Wallet මෘදුකාංගයක් සමඟ මෙම මෙහෙයුම අතින්ම සිදු කළ හැකි බව දැන සිටින්න. විවිධ හොප් නිවැරදිව අතින් සිදු කරන ආකාරය ඉගෙන ගැනීමට, මම මෙම වෙනත් ලිපිය අනුගමනය කිරීමට නිර්දේශ කරමි: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589)


JoinBot orodje ni več operativno, saj je bilo v celoti odvisno od sodelovanja Wallet, ki ga upravlja Samourai.


සහයෝගී ගනුදෙනු වෙනත් වර්ග සම්බන්ධයෙන්, සාමාන්‍යයෙන් "cahoots" ලෙස හැඳින්වෙන්නේ, ඒවා තවමත් සම්භවය, නමුත් මැනුවලිව. සේවාදායකය වසා දැමීමට පෙර, ඔබට Stonewall x2 හෝ Stowaway (PayJoin) ගනුදෙනු සිදු කිරීම සඳහා විකල්ප දෙකක් තිබුණි:



- Soroban ජාලය භාවිතා කර PSBTs ස්වයංක්‍රීයව සහ දුරස්ථව Exchange කරන්න;
- Ali pa te izmenjave izvedite ročno s skeniranjem več QR kod.


අවස්ථා කිහිපයක් පරීක්ෂා කිරීමෙන් පසු, Soroban දැන් ක්‍රියා නොකරන බව පෙනේ. මෙම සහයෝගී ගනුදෙනු සිදු කිරීමට, Exchange දත්ත අතින් සිදු කළ යුතුය. මෙම Exchange සිදු කිරීම සඳහා විකල්ප දෙකක් මෙන්න:



- ඔබේ සහකරුට භෞතිකව ආසන්න නම්, ඔබට QR කේත අනුපිළිවෙලින් ස්කෑන් කළ හැක;
- ඔබේ සහකරුගෙන් දුරස්තව සිටී නම්, ඔබට PSBTs පිටත සන්නිවේදන නාලිකාවක් හරහා යෙදුමට Exchange කළ හැක. කෙසේ වෙතත්, මෙම PSBTs වල අඩංගු දත්ත පෞද්ගලිකත්වය සම්බන්ධයෙන් සංවේදී වන බැවින් අවධානයෙන් සිටින්න. Exchange රහස්‍යභාවය සහතික කිරීම සඳහා සංකේතිත පණිවිඩ සේවාවක් භාවිතා කිරීමට මම නිර්දේශ කරමි.


**[-> Stonewall x2 लेनदेनहरूको बारेमा थप जान्नुहोस्।](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)**


**[-> Stowaway लेनदेन के बारे में अधिक जानें।](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**


Kar se tiče Whirlpool, se zdi, da protokol ne deluje več, niti za uporabnike, ki imajo svoj Dojo. Zadnjih nekaj dni sem spremljal svoj RoninDojo in poskusil nekaj osnovnih manipulacij, vendar se Whirlpool CLI ni mogel povezati od izklopa strežnika.


Vendar pa ostajam upanja poln, da se lahko ta protokol v prihodnjih tednih ponovno aktivira ali morda na novo zamisli, odvisno od tega, kako se bo situacija razvijala. Ta premor bi lahko bil priložnost za raziskovanje novih pristopov ali potencialnih izboljšav tega sistema.


### Kateri zunanji orodji so še vedno na voljo?


සමුරායි පරිසරය සම්බන්ධ අනෙකුත් මෙවලම් සම්බන්ධයෙන්, කිහිපයක් තවමත් ලබා ගත හැකි අතර අනෙකුත් කිහිපයක් ලබා ගත නොහැක.


නොමිලේ දාම විශ්ලේෂණ වෙබ් අඩවිය OXT.me දුකින් සලකන්නට වශයෙන් මේ මොහොතේ සඳහා ලබා ගත නොහැක.


Whirlpool Stats Tool Samouraiගේ GitLab හි සත්කාරක වූ බැවින් දැන් බාගත කිරීමට ලබා ගත නොහැක. ඔබ මෙම Python මෙවලම පෙර ඔබේ යන්ත්‍රයේ දේශීයව බාගත කර තිබුණත්, හෝ එය ඔබේ RoninDojo නෝඩ් එකේ ස්ථාපනය කර තිබුණත්, වර්තමානයේදී WST ක්‍රියා නොකරයි. ඇත්ත වශයෙන්ම, එය ක්‍රියාත්මක වීමට OXT.me විසින් සපයන දත්ත මත රඳා පවතින අතර, මෙම වෙබ් අඩවිය දැන් ප්‍රවේශය ලබා ගත නොහැක. වර්තමානයේදී, Whirlpool ප්‍රොටෝකෝලය ක්‍රියාත්මක නොවන බැවින් WST විශේෂයෙන් ප්‍රයෝජනවත් නොවේ.


KYCP.org වෙබ් අඩවිය දැනට ප්‍රවේශ විය නොහැක.


Boltzmann Calculator Python මෙවලම සඳහා කේතය සත්කාරකය වූ GitLab ද අත්අඩංගුවට ගෙන ඇත. මේ මොහොතේ, මෙම මෙවලම බාගත කිරීම තවදුරටත් සම්භව නොවේ. නමුත් ඔබට RoninDojo තිබේ නම්, පෙරවද ආකාරයට Boltzmann Calculator භාවිතා කිරීමට ඔබට හැක.


RoninDojo සඳහා, මෙම node-in-box මෘදුකාංගය Whirlpool CLI සහ WST වැනි විශේෂිත මෙවලම් කිහිපයක් නොමැති වුවද නිවැරදිව ක්‍රියා කරමින් පවතී. Fulcrum හෝ Electrs සඳහා ස්තූතියි, එය තවමත් අනෙකුත් Wallet මෘදුකාංග සඳහා භාවිතා කළ හැක. RoninDojo පිළිබඳව වැඩි විස්තර ලබා ගැනීමට හෝ ඔබට විශේෂිත ප්‍රශ්න තිබේ නම්, [ඔවුන්ගේ ටෙලිග්‍රෑම් කණ්ඩායම](https://t.me/RoninDojoNode) වෙත එක්වන්නැයි මම ඔබට උත්සාහ දරන්නෙමි.


Vendar pa izvorna koda za RoninDojo trenutno ni več dostopna, saj je bila gostovana na Samourai's GitLab. Zato trenutno ni mogoče ročno namestiti na Raspberry Pi.


Watch-only wallet මෘදුකාංග Sentinel සම්බන්ධයෙන්, තත්ත්වය Samourai යෙදුමට සමාන වේ. ඔබට ඔබේම Dojo එකක් තිබේ නම්, කිසිදු ගැටළුවකින් තොරව Sentinel භාවිතා කරගෙන යා හැක. කෙසේ වෙතත්, ඔබට Dojo එකක් නොමැති නම්, සම්බන්ධතාවයක් ස්ථාපිත කිරීමට තවදුරටත් නොහැකි වේ. Samourai ට වඩා වෙනස්ව, Sentinel වෙබ් අඩවිය තවමත් මාර්ගගතව ප්‍රවේශ විය හැක. නමුත් මෙම අඩවිය සහ එහි ලබා දෙන APK පිළිබඳව අවධානයෙන් සිටින්න, මක්නිසාද මේ සම්පත් වත්මන්ව කවුරුන් විසින් පාලනය කරන්නේද යන්න පැහැදිලි නැත.


### Sparrow Wallet කට බලපෑමක් ඇතිද?


Sparrow Wallet සාමාන්‍ය ලෙස ක්‍රියාත්මක වීම දිගටම කරගෙන යයි, දැන් Samourai මෙවලම් ලබා ගත නොහැකි වීම හැර. වර්තමානයේ, Sparrow හරහා coinjoins සිදු කිරීම දැන් නොහැක. ඒ මෙන්ම, සමාජික වියදම් මෙවලම් දැන් ප්‍රවේශ විය නොහැක, මන්ද Sparrow, Samourai මෙන් PSBTs හි අතින් Exchange විකල්පය ලබා නොදෙයි. අනෙකුත් සියලුම කාර්යයන් සඳහා, Sparrow කිසිදු ගැටළුවකින් තොරව ක්‍රියාත්මක වේ. අවශ්‍ය නම් Samourai Wallet ප්‍රතිසාධනය කිරීමට මෙම මෘදුකාංගය භාවිතා කළ හැක.


## Kako obnoviti Samourai Wallet?


අපි පෙර කොටස් වලදී දැක ඇති පරිදි, ඔබට ඔබේම Dojo එකක් තිබේ නම්, මෘදුකාංගය මාරු කිරීම අනිවාර්ය නොවේ. **Samourai ඔබේ දෛනික වියදම් සඳහා විශිෂ්ට Hot Wallet තේරීමක් ලෙස පවතී**. කෙසේ වෙතත්, ඔබට Dojo එකක් නොමැති නම් හෝ වෙනත් මෘදුකාංගයක් තෝරා ගැනීමට කැමති නම්, මම ඔබට මුළුමනින්ම ප්‍රතිසාධන ක්‍රියාවලිය පැහැදිලි කරමින්, ඔබට මුහුණ දිය හැකි ඕනෑම බාධාවක් විස්තර කරමි.


කෙසේ වෙතත්, ඔබේ කාලය ගත කිරීම සහ කිසිදු දෝෂයක් සිදු නොවන බව සහතික කිරීම වැදගත් වේ. මතක තබා ගන්න, ඔබේ පුද්ගලික යතුරු ඔබ සතු බැවින් කිසිදු ඉක්මනක් නැත, සහ Samourai සර්වර් අත්අඩංගුවට ගැනීම මෙයට කිසිඳු ආකාරයකින් බලපෑමක් නොකරයි. කුමක් සිදු වුවත්, ඔවුන්ට ඔබේ පුද්ගලික යතුරු ප්‍රවේශ විය නොහැක.


### passphrase සත්‍යාපනය කරන්න.


ඔබේ Wallet ප්‍රතිසාධනය කිරීමට, ඔබේ passphrase තිබිය යුතුය, ඔබ මූලාශ්‍ර ගොනුව හරහා ප්‍රතිසාධනය කිරීමට තෝරා ගත්තත්. මෙම passphrase වල නිවැරදි බව පරීක්ෂා කිරීමෙන් ආරම්භ කරන්න. ඔබේ Samourai Wallet යෙදුම විවෘත කර, ඉහළ වම පැත්තේ ඇති ඔබේ Paynym අයිකනය මත ක්ලික් කර, පසුව `Settings` තෝරන්න.


![samourai](assets/1.webp)


ඊළඟට, `Troubleshooting` මත ක්ලික් කර `passphrase/backup test` මත ක්ලික් කරන්න.


![samourai](assets/2.webp)


ඔබේ passphrase ඇතුළත් කර `Ok` ක්ලික් කරන්න. එය නිවැරදි නම්, Samurai එය තහවුරු කරනු ඇත. ඔබට පසුව භාවිතා කිරීමට සැලසුම් කරන්නේ නම් ආපසුගත ගොනුව සත්‍යාපනය කිරීමටද විකල්පයක් ඇත.


![samourai](assets/3.webp)


මෙම පියවර විකල්ප වන අතර නිර්දේශිත වේ. එය passphrase නිවැරදි බව තහවුරු කරයි, පසුව ගැටළු ඇති විය හැකි මූලාශ්‍රයක් ඉවත් කරයි. මෙම අවස්ථාවේදී Samourai passphrase වැරදි බව පෙන්වා දුන්නේ නම්, ප්‍රතිසාධනයක් කළ නොහැක. ඔබ passphrase නිවැරදිව ඇතුළත් කර ඇති බව සහතික කර, නැවත පරීක්ෂා කරන්න.


### විකල්පය 1: සෙප්පුව මගින් Wallet නැවත ලබා ගැනීම සඳහා උපස්ථ ගොනුව භාවිතා කරන්න


Od različice 1.8.6 Sparrow Wallet je mogoče neposredno uvoziti vaš Samourai Wallet z uporabo varnostne besedilne datoteke z imenom `samourai.txt`, ki jo vaša aplikacija samodejno ustvari. Ta datoteka vsebuje vse potrebne informacije za obnovitev vašega Wallet in je šifrirana z vašim passphrase za varnost.


ඔබ මෙම විකල්පය තෝරා ගන්නේ නම්, ඔබට ඔබේ යාවත්කාලීන `samourai.txt` ගොනුව සහ ඔබේ passphrase අවශ්‍ය වේ. Samourai Wallet හි මෙම ගොනුව generate කිරීමට, ඉහළ දකුණු කෙළවරේ ඇති කුඩා තිත් තුන මත ක්ලික් කර, පසුව `Export Wallet backup` තෝරන්න.


![samourai](assets/4.webp)

ඊළඟට, `Export to Clipboard` තෝරන්න. ඊට පසු, මෙම ගොනුව ඔබේ පරිගණකයට ආරක්ෂිතව මාරු කිරීමට ඔබට අවශ්‍ය වේ. ගොනුව සංකේතනය කර ඇති නමුත් passphrase පමණක් එය විකේතනය කිරීමට ප්‍රමාණවත් බැවින්, එය සම්ප්‍රේෂණය කිරීමේදී පියවර ගන්නා ලෙස වැදගත් වේ. ඔබ සරල පෙළක් ලෙස සෘජු මාරු කිරීමක් තෝරා ගන්නේ නම්, ඔබේ පරිගණකයේ `samourai.txt` ගොනුවක් සාදන්න සහ පසුව එයට පසුව ක්ලිප්බෝඩ් අන්තර්ගතය අලවන්න. විකල්පයක් ලෙස, ඔබේ දුරකථනයේ ගබඩා කරන ලද ගොනු වලින් `samourai.txt` ගොනුව සෘජුවම ලබා ගැනීමක් විය හැක.

Ko imate dostop do datoteke na svojem računalniku, odprite Sparrow Wallet, kliknite na zavihek `File` in izberite `Import Wallet`, da začnete uvažati svoj Wallet.


![samourai](assets/5.webp)


스크롤하여 `Samourai Backup`으로 이동한 다음, `Import File`을 클릭하고 `samourai.txt` 파일을 선택합니다.


![samourai](assets/6.webp)


Sparrow nato vas bo prosil za geslo za dešifriranje datoteke. To geslo je pravzaprav vaš passphrase. Vnesite ga v ustrezno polje in kliknite na `Import`.


![samourai](assets/7.webp)


Če se na tej stopnji vaš Wallet ne prikaže, je možno, da ste naredili napako pri kopiranju datoteke `samourai.txt` ali pri vnosu passphrase. Za več pomoči lahko preverite razdelek za odpravljanje težav.


![samourai](assets/8.webp)


ස්ක්‍රිප්ට් වර්ගය සඳහා, ඔබ Samourai හි වෙනත් ස්ක්‍රිප්ට් සකසා නොමැති නම්, සාමාන්‍යයෙන් SegWit V0 (ස්වභාවික SegWit / P2WPKH) පමණක් භාවිතා කළ යුතුය. මෙම පෙරනිමි ස්ක්‍රිප්ට් තබා `Import` මත ක්ලික් කරන්න.


![samourai](assets/9.webp)


ඔබේ Wallet නමක් දෙන්න, උදාහරණයක් ලෙස, "Samourai Recovery", සහ පසුව `Create Wallet` මත ක්ලික් කරන්න.


![samourai](assets/10.webp)


ඉන් අනතුරුව Sparrow ඔබගෙන් මුරපදයක් තෝරා ගැනීමට අයදුම් කරනු ඇත. මෙම මුරපදය මෙම පරිගණකයේ ඔබේ Wallet වෙත ප්‍රවේශය ආරක්ෂා කිරීම සඳහා පමණක් වන අතර ඔබේ Wallet යතුරු ව්‍යුත්පන්න කිරීම සඳහා අදාල නොවේ. ශක්තිමත් මුරපදයක් තෝරා ගැනීමට, එය මතක තබා ගැනීමට සටහන් කර ගැනීමට සහ `Set Password` මත ක්ලික් කිරීමට වග බලා ගන්න.


![samourai](assets/11.webp)


Sparrow nato izpelje ključe vašega Wallet in poišče ustrezne transakcije.


![samourai](assets/12.webp)


දැනට, ඔබගේ තැන්පතු ගිණුම පමණක් ප්‍රවේශ විය හැක. ඔබ මෙම ගිණුම සඳහා පමණක් Samourai භාවිතා කර තිබේ නම්, ඔබගේ සියලුම මුදල් දැකිය හැක. කෙසේ වෙතත්, ඔබ Whirlpool ද භාවිතා කර තිබේ නම්, ඔබට `premix`, `postmix`, සහ `badbank` ගිණුම් ලබා ගැනීමට අවශ්‍ය වේ. Sparrow මත, සරලව `Settings` ටැබය ක්ලික් කරන්න, එවිට `Add Accounts...` මත ක්ලික් කරන්න.


![samourai](assets/13.webp)

විවෘත වන කවුළුවෙන්, ඩ්‍රොප්ඩවුන් මෙනුවෙන් `Whirlpool Accounts` තෝරන්න, එවිට `OK` මත ක්ලික් කරන්න.

![samourai](assets/14.webp)


ඔබට එවිට ඔබේ විවිධ Whirlpool ගිණුම් පෙනේවි, සහ Sparrow සම්බන්ධිත බිට්කොයින් භාවිතා කිරීමට අවශ්‍ය යතුරු ලබා ගනු ඇත.


![samourai](assets/15.webp)


Če uporabljate drugo programsko opremo kot Sparrow, na primer Electrum, za obnovitev vašega Samourai Wallet, tukaj so indeksi računov Whirlpool za ročno obnovitev:



- තැන්පතු: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


ඔබට දැන් Sparrow හි ඔබේ බිට්කොයින් වෙත ප්‍රවේශය ඇත. Sparrow Wallet භාවිතා කිරීමට උපකාරය අවශ්‍ය නම්, [අපගේ කැපවූ උපකාරකය](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) පරීක්ෂා කළ හැක.


මම Samourai හි ඔබගේ UTXOs සමඟ සම්බන්ධ කර තිබූ ලේබල් අතින් ආයාත කිරීමද නිර්දේශ කරමි. මෙය පසුව Sparrow හි ප්‍රභල කාසි පාලනයක් සිදු කිරීමට ඔබට ඉඩ සලසයි.


### විකල්පය 2: Mnemonic වාක්‍යය සමඟ Sparrow මත Wallet ප්‍රතිසාධනය කරන්න


Če ne želite izvesti obnovitve z varnostno kopijo, se lahko odločite za bolj tradicionalno metodo, tako da preprosto uporabite svojo 12-besedno obnovitveno frazo in vaš passphrase. Ta druga možnost je pogosto enostavnejša.


Za začetek se prepričajte, da imate pri roki obnovitveno frazo in vaš passphrase. Nato odprite programsko opremo Sparrow Wallet, kliknite na zavihek `File` in izberite `Import Wallet`, da začnete uvažati vaš Wallet.


![samourai](assets/16.webp)


Izberite `Mnemonic Words (BIP39)` in v spustnem meniju kliknite na `Use 12 Words`.


![samourai](assets/17.webp)


Vnesite 12 besed vašega obnovitvenega gesla v pravilnem vrstnem redu.


![samourai](assets/18.webp)


ඔබේ ස්පැරෝව `Invalid Checksum` පණිවිඩයක් පෙන්වන්නේ නම්, එය ප්‍රතිසාධන වාක්‍යයේ පරීක්ෂා මුදුව වලංගු නොවන බව පෙන්වයි, එය ඔබ වචන ඇතුළත් කිරීමේදී දෝෂයක් සිදු කළ බවට ඉඩක් ඇත.


![samourai](assets/19.webp)


Če je vaš stavek pravilen, označite polje `Uporabi passphrase?` in vnesite vaš passphrase v namensko polje. Na koncu, če se zdi vse pravilno, kliknite na gumb `Odkrij Wallet`.


![samourai](assets/20.webp)


Wallet-ට නමක් දෙන්න, උදාහරණයක් ලෙස, "Samourai Recovery", එවිට `Wallet නිර්මාණය කරන්න` මත ක්ලික් කරන්න.


![samourai](assets/21.webp)

එවිට Sparrow ඔබගෙන් මුරපදයක් තෝරා ගැනීමට අයදුම් කරනු ඇත. මෙම මුරපදය මෙම පරිගණකයේ ඔබේ Wallet වෙත ප්‍රවේශය ආරක්ෂා කිරීම පමණක් සිදු කරන අතර ඔබේ Wallet යතුරු ව්‍යුත්පන්න කිරීම සමඟ සම්බන්ධ නොවේ. ශක්තිමත් මුරපදයක් තෝරා ගැනීමට, එය මතක තබා ගැනීමට ලියවා තබා ගැනීමට සහ `Set Password` මත ක්ලික් කිරීමට වග බලා ගන්න.

![samourai](assets/22.webp)


Sparrow nato izpelje ključe za vaš Wallet in poišče ustrezne transakcije.


![samourai](assets/23.webp)


Če se na tej stopnji vaš Wallet ne prikaže, je možno, da ste naredili napako pri vnosu passphrase ali obnovitvene fraze. Za več pomoči lahko preverite namenski razdelek za odpravljanje težav.


Trenutno je dostopen samo vaš depozitni račun. Če ste za ta račun uporabljali samo Samourai, bi morali videti vsa svoja sredstva. Vendar, če ste uporabljali tudi Whirlpool, boste morali izpeljati račune `premix`, `postmix` in `badbank`. Na Sparrow preprosto kliknite na zavihek `Settings`, nato na `Add Accounts...`.


![samourai](assets/24.webp)


වීඩියෝව විවෘත වන විට, ඩ්‍රොප්ඩවුන් ලැයිස්තුවෙන් `Whirlpool Accounts` තෝරන්න, එවිට `OK` මත ක්ලික් කරන්න.


![samourai](assets/25.webp)


ඔබට එවිට ඔබේ විවිධ Whirlpool ගිණුම් පෙනෙන අතර, Sparrow සම්බන්ධිත බිට්කොයින් භාවිතා කිරීමට අවශ්‍ය යතුරු ලබා ගනු ඇත.


![samourai](assets/26.webp)


ඔබේ Samourai Wallet ප්‍රතිසාධනය කිරීමට Electrum වැනි වෙනත් මෘදුකාංගයක් භාවිතා කරන්නේ නම්, අතින් ප්‍රතිසාධනය සඳහා Whirlpool ගිණුම් දර්ශක මෙන්න:



- තැන්පතු: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


ඔබට දැන් Sparrow හි ඔබේ බිට්කොයින් වෙත ප්‍රවේශ විය හැක. Sparrow Wallet භාවිතා කිරීමට උපකාරය අවශ්‍ය නම්, [අපගේ කැපවූ උපකාරකය](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) බලන්න.


මම ඔබේ UTXOs සමඟ සම්බන්ධ කර තිබූ ලේබල් මැනුවල්ව ආයාත කිරීමද නිර්දේශ කරමි. මෙය පසුව Sparrow හි ප්‍රභල කාසි පාලනයක් සිදු කිරීමට ඔබට ඉඩ සලසයි.


### සාමාන්‍යයෙන් මුහුණපාන ගැටළු මොනවාද?


පසුගිය දින කිහිපය තුළ පුද්ගලයන් කිහිප දෙනෙකුට සහය වීමෙන් පසු, ඔබේ Wallet ප්‍රතිසාධනය වළක්වන බොහෝ ගැටළු මම මුහුණ දී ඇතැයි මම විශ්වාස කරමි. පෙර උපකාරිකා මාලාවන්ට පසුවද ඔබේ Wallet වෙත ප්‍රවේශ විය නොහැකි නම්, මෙන්න කීපයක් අමතර නිර්දේශ.

පළමුව සහ ප්‍රධාන වශයෙන්, ප්‍රතිසාධනය ක්‍රියාත්මක වීමට, ප්‍රතිසාධන වාක්‍යය නිවැරදි වීම අත්‍යවශ්‍ය වේ. ඔබේ 12-වචන වාක්‍යය සොයා ගැනීමට නොහැකි නම්, Samourai හි záábackup ගොනුවෙන් ප්‍රතිසාධනය කිරීමට _විකල්පය 1_ භාවිතා කළ හැක. ඔබේ ප්‍රතිසාධන වාක්‍යය සෘජුවම Samourai Wallet තුළ ප්‍රවේශ විය හැකි අතර, `Settings` වෙත ගොස්, `Wallet` තෝරා, අවසානයේ `Show 12-word recovery phrase` තෝරාගැනීමෙන්.


ඊළඟට, ඔබේ passphrase හි ප්‍රතිසාධනයේදී ටයිප් කිරීමේ දෝෂයක් නිවැරදි නොවන ව්‍යුත්පන්න යතුරු ඇති කිරීමට හේතු වන අතර එය Sparrow හි ඔබේ Wallet ප්‍රතිසාධනය වළක්වනු ඇත. **passphrase පරිපූර්ණව නිවැරදි විය යුතුය!**


Za rešitev tega vam najprej svetujem, da preverite veljavnost vašega passphrase v aplikaciji Samourai, kot je opisano v razdelku "_Verify the passphrase_" tega članka:


1. **සමුරයි හි වලංගුකරණය:** සමුරයි passphrase නිවැරදි බව තහවුරු කළහොත්, ආපසු ප්‍රතිසාධනය ආරම්භයෙන්ම නැවත උත්සාහ කරන්න, passphrase නිවැරදිව, දෝෂයකින් තොරව, ස්පැරෝ වෙත ඇතුළත් කිරීම සහතික කරමින්;

2. **passphrase Napaka:** Če Samourai nakaže, da je passphrase napačen, je nesmiselno nadaljevati poskuse na Sparrow. Dokler pravilni passphrase ni najden, je obnova vašega Wallet nemogoča. Če ste trajno izgubili svoj passphrase, obdržite svojo aplikacijo Samourai na varnem. Vse, kar lahko storite, je upanje, da se strežniki ponovno zaženejo, da boste lahko opravili izdatke neposredno iz aplikacije brez potrebe po obnovi. **V tem primeru ne poskušajte povezati Dojo**, saj bi to pomenilo ponastavitev vašega Wallet na Samourai, kar zahteva dostop do passphrase.


අනෙකුත් හමුවූ දෝෂ අතර, බොහෝ දේ Sparrow හි ජාල වින්‍යාසය සමඟ සම්බන්ධ වේ.


මුලින්ම, Sparrow නිවැරදිව `Mainnet` ප්‍රකාරයට සකස් කර ඇති බව සහතික වන්න `Testnet` ප්‍රකාරයට වෙනුවට. ඇත්ත වශයෙන්ම, Sparrow ඔබේ ගනුදෙනු සොයා බැලුවහොත් Testnet මත, කිසිවක් සොයා ගැනීමට නොහැකි වනු ඇත, මන්ද ඔබේ Wallet Mainnet මත පවතී. Testnet යනු Bitcoin හි විකල්ප අනුවාදයක් වන අතර, පරීක්ෂණ සහ සංවර්ධනය සඳහා පමණක් භාවිතා කරන අතර, ප්‍රධාන ජාලය (Mainnet) මෙන්ම, එහිම බ්ලොක් සහ ගනුදෙනු සමඟ වෙනම ජාලයක ක්‍රියාත්මක වේ. ඔබ සිටින ජාලය පරීක්ෂා කිරීමට, `Tools` ටැබය මත ක්ලික් කරන්න, එවිට `Restart In` මත ක්ලික් කරන්න. `Mainnet` විකල්පය පෙන්වා ඇත්නම්, ඔබ ප්‍රධාන ජාලය මත නොවේ. Sparrow Mainnet මත නැවත ආරම්භ කිරීමට එය තෝරන්න, එවිට නැවත ඔබේ ප්‍රතිසාධන ක්‍රියාවලිය ආරම්භ කරන්න.


![samourai](assets/27.webp)

සමහරුට තම නෝඩ් එකට Sparrow සම්බන්ධ කිරීමේදී දුෂ්කරතා මුණගැසී ඇත. Sparrow හි පහළ දකුණු කෙළවරේ, වර්ණවත් ස්විචයක් ඔබේ මෘදුකාංගය Bitcoin නෝඩ් එකකට නිවැරදිව සම්බන්ධ වී ඇතිද යන්න සනිටුහන් කරයි. ඔබේ Samourai ගනුදෙනු ලබා ගැනීමට, මෘදුකාංගය හොඳින් සම්බන්ධ වී තිබීම අත්‍යවශ්‍ය වේ. ස්විචය සක්‍රීය වී ඇති බව, මගේ පහත රූපයේ පරිදි පරීක්ෂා කරන්න (පොදු නෝඩ් එකකට කහ, Bitcoin Core සඳහා Green, සහ Electrum සේවාදායකයකට නිල්).

![samourai](assets/28.webp)


Če stikalo ni aktivirano, kliknite nanj, da ponovno aktivirate povezavo.


![samourai](assets/29.webp)


Če težava ostaja, tukaj je nekaj možnih rešitev:



- Če poskušate povezati na svoj lasten Electrum strežnik (modro) ali vaš Bitcoin Core (Green) in se Sparrow ne more povezati, preverite informacije o povezavi pod `Datoteka > Nastavitve... > Strežnik`;


![samourai](assets/30.webp)



- Če se težava s povezavo nadaljuje, je to lahko posledica nepopolne sinhronizacije vašega vozlišča. Prepričajte se, da sta vaše vozlišče in vaš indeksator 100% sinhronizirana. Če je potrebno kot zadnja možnost, odklopite vaše vozlišče iz Sparrow in se povežite na javno vozlišče;
- Če ste že povezani z javnim vozliščem in povezava ne uspe, poskusite spremeniti vozlišče z izbiro drugega s spustnega seznama.


![samourai](assets/31.webp)


Če ste uspešno obnovili svoj Wallet, vendar se zdi nepopoln, je morda težava povezana z izpeljavo.


ඔබේ Samourai තැන්පතු ගිණුම `P2WPKH` වර්ගයට වඩා වෙනස් ස්ක්‍රිප්ට් වර්ගයක් සමඟ භාවිතා කළහොත් ගැටලුවක් ඇති විය හැක. පෙරනිමි ලෙස, Samourai මෙම ස්ක්‍රිප්ට් වර්ගය භාවිතා කරයි, නමුත් ඔබ එය අතින් වෙනස් කර ඇත්නම්, Sparrow මත ප්‍රතිසාධනය කිරීමේදීද මෙය සකසිය යුතුය.


වෙනත් ලිපි රටා සඳහා ශාඛා ලබා ගැනීමට, ඔබට භාවිතා කරන සෑම ලිපි රටාවක් සඳහාම ප්‍රතිසාධන ක්‍රියාවලිය නැවත කිරීමට අවශ්‍ය වේ. මෙ සඳහා, Sparrow හි `File > New Wallet` වෙත ගොස්, බහින ලැයිස්තුවෙන් වෙනත් ලිපි රටාවක් තෝරන්න, `New or Imported Software Wallet` මත ක්ලික් කරන්න, සහ මුල් උපකාරක පාඩමෙහි පියවරවලට සමානව ක්‍රියා කරන්න.


![samourai](assets/32.webp)


මම මුහුණ දුන් තවත් ව්‍යුත්පන්න ගැටලුවක් Gap Limit අගය සමඟ සම්බන්ධ වේ. මෙම අගය Sparrow වෙත කියා දෙන්නේ එය කොපමණ හිස් ලිපින පසු නව ලිපින ව්‍යුත්පන්න වීම නවත්විය යුතුද යන්නයි. ප්‍රතිසාධනයෙන් පසු, ඔබට කිසියම් ගනුදෙනු අතුරුදහන් වී ඇති බව දැනගතහොත්, මෙය අඩු Gap Limit එකක් නිසා විය හැක. මෙය විසඳීමට, ගැටලුව ඇති කරන ගිණුමට යන්න, උදාහරණයක් ලෙස, postmix ගිණුම (තවත් ගිණුම් කිහිපයක් සම්බන්ධ නම්, මෙම මෙහෙයුම එක් එක් සඳහා නැවත කරන්න).


![samourai](assets/33.webp)


`Settings` ටැබය මත ක්ලික් කර `Advanced...` බොත්තම මත ක්ලික් කරන්න.

![samourai](assets/34.webp)

ක්‍රමයෙන් Gap Limit අගය වැඩි කරන්න, උදාහරණයක් ලෙස, මම මෙහි එය `400` ලෙස සකසා ඇත. එවිට, `Close` බොත්තම මත ක්ලික් කරන්න.


![samourai](assets/35.webp)


`Apply` මත ක්ලික් කරන්න අවසන් කිරීමට. එවිට Sparrow විසින් විශාල සංඛ්‍යාවක් ලිපින ලබාගෙන, එම ලිපින මත අරමුදල් සොයා බැලීම සිදු කරනු ඇත, එය ඔබේ සියලුම ගනුදෙනු ප්‍රතිසාධනය කිරීමට උපකාරී විය යුතුය.


![samourai](assets/36.webp)


එය මම පසුගිය දින කිහිපය තුළ මුහුණ දුන් විවිධ ප්‍රතිසාධන ගැටළු ආවරණය කරයි. මෙම සියලුම විසඳුම් උත්සාහ කිරීමෙන් පසු, ඔබට තවමත් ගැටළු ඇති නම්, මම ඔබට [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) වෙත එක්වීමට ආරාධනා කරමි. මම නිතරම මෙම Discord වෙත පිවිසෙන අතර විසඳුමක් තිබේ නම් මම උදව් කිරීමට සතුටු වෙමි. අනෙක් බිට්කොයින්කරුවන්ටද ඔවුන්ගේ අත්දැකීම් බෙදා ගැනීමට සහ ඔවුන්ගේ සහය ලබා දීමට හැකි වනු ඇත. **ඕනෑම අවස්ථාවක, ඔබේ ප්‍රතිසාධන වාක්‍යය, ඔබේ උපස්ථිත ගොනුව, සහ ඔබේ passphrase රහසිගතව තබා ගැනීම අත්‍යවශ්‍ය වේ**. ඒවා කිසිවෙකුට හුවමාරු නොකරන්න, මන්ද එය ඔවුන්ට ඔබේ බිට්කොයින් සොරා ගැනීමට ඉඩ සලසයි.


සුවය සම්පූර්ණ වූ පසු, ඔබට දැන් ඔබේ බිට්කොයින් වෙත ප්‍රවේශය ඇත. එය හොඳ දෙයක්, නමුත් එය ප්‍රමාණවත් නොවිය හැක. නියත වශයෙන්ම, සේවාදායකයන් අත්අඩංගුවට ගැනීම ඔබේ පෞද්ගලිකත්වය සඳහා නව සම්භාවිත අවදානම් ඇති කරයි. ඊළඟ කොටසෙහිදී, අපි මෙම අවදානම් විස්තරාත්මකව විමසා බලන අතර ඔබේ පෞද්ගලිකත්වය ආරක්ෂා කිරීමට ගත යුතු පියවර සටහන් කරමු.


## ඔබේ ගනුදෙනු වල පෞද්ගලිකත්වය සඳහා ඇති ප්‍රතිවිපාක මොනවාද?


### සමුරායි පරිශීලකයෙකු ලෙස Dojo නොමැතිව


ඔබේම Dojo එකක් සම්බන්ධ නොකර Samourai Wallet භාවිතා කරමින් සිටියදී, යෙදුම ක්‍රියාත්මක වීමට ඔබේ xpubs Samourai සේවාදායකයන් වෙත සන්නිවේදනය කළ යුතු විය. මෙම සේවාදායකයන් අත්අඩංගුවට ගැනීමත් සමඟ, බලධාරීන්ට දැන් මෙම xpubs වෙත ප්‍රවේශය ඇති විය හැක.


මෙම තත්ත්වය සංකල්පිතයි. මෙම xpubs සටහන් කර තිබේද, කිසියම් සම්භාව්‍ය ගබඩා විනාශ කර තිබේද, බලධාරීන් ඒවා ලබාගෙන තිබේද, සහ ඔවුන් ඒවා දාම විශ්ලේෂණය සඳහා භාවිතා කිරීමට සැලසුම් කරන්නේද යන්න අපට නොදනිමු. කෙසේ වෙතත්, එවැනි තත්ත්වයකදී, තමන්ගේම Dojo එකක් සම්බන්ධ නොකළ පරිශීලකයින්ගේ xpubs බලධාරීන් සතුව ඇති නරකම තත්ත්වය සලකා බැලීම ප්‍රජ්ඣාවන්ත වේ.

සඳහා යොමු කිරීමක් ලෙස, xpub යනු ළමා පොදු යතුරු (පොදු යතුර + දාම කේතය) ජනනය කිරීම සඳහා අවශ්‍ය සියලුම Elements අඩංගු අක්ෂර මාලාවකි. එය ශ්‍රේණිගත නියමිත පසුම්බිවලදී generate ලැබීමේ ලිපින සහ ගිණුමක ගනුදෙනු නිරීක්ෂණය කිරීමට භාවිතා කරයි, සම්බන්ධ පුද්ගලික යතුරු අනාවරණය නොකර. මෙය, උදාහරණයක් ලෙස, "නිරීක්ෂණ පමණක්" Wallet නිර්මාණය කිරීම සඳහා ඉඩ සලසයි. කෙසේ වෙතත්, xpubs අනාවරණය කිරීමෙන් පරිශීලකයාගේ පෞද්ගලිකත්වය අවදානමට ලක් විය හැක, මන්ද ඒවා තෙවන පාර්ශවයන්ට ගනුදෙනු හඹා යාමට සහ සම්බන්ධ ගිණුම්වල ශේෂයන් දැකීමට ඉඩ සලසයි.

ඔබේ xpubs දන්නා ඕනෑම කෙනෙකුට එබැවින් ඔබේ Wallet හි සියලුම ලැබීම් ලිපින, අතීතයේ භාවිතා කළ ඒවා, සහ අනාගතයේ ජනනය වන ඒවා දැකිය හැක.


Do uporabnikov brez Dojoja ima potencialno uhajanje vaših xpubov dve glavni posledici:



- ඔබ කළ හැකි coinjoins, ඔබේ xpubs දන්නා කාටත් පෞද්ගලිකත්වය standpoint එකෙන් අඵල නොවන බවට පත් කරයි, එබැවින් ඔබේ කාසි සියලු anonset අහිමි වේ;
- මෙම පුද්ගලයාට ඔබේ Samourai Wallet හි සියලුම ලැබීමේ ලිපින හඹා යා හැක.


එමනිසා, අවාසනාවන්තම තත්ත්වය සලකා බැලීම සහ පෞද්ගලිකත්වය සම්බන්ධයෙන් අවදානම් වන Wallet සමඟ වෙන්වීම වැදගත් වේ. මෙය කිරීමට, Sparrow Wallet වැනි වෙනත් මෘදුකාංගයක් සමඟ නව Wallet එකක් මුල සිටම සාදන්න. ඔබේ උපස්ථයන් වල වලංගුතාවය සනාථ කිරීමෙන් පසු, ගනුදෙනු කිරීමෙන් ඔබේ සියලුම මුදල් මාරු කරන්න. මෙම මෙහෙයුම ඔබේ කාසි වල සලකුණු හැඩය කඩන්නේ නැති නමුත්, ඔබේ නව Wallet හි ලිපින නිවැරදිව බලධාරීන්ට දැන ගැනීම වැළැක්වනු ඇත.


Med tem prenosom priporočam, da se izognete konsolidaciji svojih kovancev. Če predpostavimo, da so vaši xpubs kompromitirani, konsolidacija ne bo imela vpliva z vidika osebe, ki ima dostop do teh xpubs, saj je vaša zasebnost z njimi že kompromitirana. Vendar pa vam svetujem, da ne konsolidirate preveč svojih kovancev, predvsem zato, da zaščitite svojo zasebnost pred drugimi ljudmi. V najslabšem primeru imajo lahko dostop do vaših xpubs samo oblasti, vendar preostali svet o njih ne ve. Tako lahko z vidika drugih konsolidacija vaših kovancev znatno škoduje vaši zasebnosti zaradi Common Input Ownership Heuristic (CIOH).


**සටහන:** නිරපේක්ෂව නිරීක්ෂණය බිඳ දැමීමට, ඔබ මෙම නව Wallet සිට coinjoins ක්‍රියාත්මක කිරීමද සලකා බලන්න.

**අවවාදය:** ඔබේ Samourai Wallet Sparrow Wallet මත සරලව ලබා ගැනීම ප්‍රමාණවත් නොවේ. xpubs කාන්දු වී ඇති අවස්ථාවකදී භාවිතා කිරීමෙන් වළකින්නට ඔබට අලුත් Wallet එකක් අලුත් ප්‍රතිසාධන වාක්‍යයක් සමඟ නිර්මාණය කිරීම අත්‍යවශ්‍ය වේ. ඔබේ පවතින seed Sparrow වෙත ආයාත කළහොත්, ඔබ Wallet කළමනාකරණ මෘදුකාංගය පමණක් වෙනස් කරයි, නමුත් Wallet එක එසේම පවතී.


### Sparrow ali Samourai z Dojo uporabnik


ඔබේ Wallet Sparrow Wallet මත පමණක් කළමනාකරණය කරන්නේ නම්, ඔබේ xpubs කාන්දුවී නොමැති විය හැක, ඔබ මහජන නියැදියක් හෝ ඔබේම Bitcoin නියැදියක් භාවිතා කරනවාද යන්න සම්බන්ධ නැත. එමෙන්ම, ඔබ Samourai යෙදුම භාවිතා කරමින් සිටින්නේ නම් සහ ඔබේ Wallet නිර්මාණය කිරීමේ සිට මෙම යෙදුම ඔබේම Dojo වෙත සම්බන්ධ කර ඇති නම්, ඔබේ xpubs ද ආරක්ෂිත වේ.


කෙසේ වෙතත්, ඔබේම Dojo එකක් **නොමැති කාලයක් තුළ** සහ පසුව ඔබේම Dojo එකක් සමඟ Wallet එක භාවිතා කර ඇත්නම්, Samourai සේවාදායකයන්ට ඔබේ xpubs වෙත ප්‍රවේශය තිබිය හැකි අතර, එබැවින් බලධාරීන්ට ඒවා දැනගත හැකිය. ඔබ මෙම විශේෂිත තත්ත්වයේ සිටිනවා නම්, මම ඔබට පෙර කොටසේ නිර්දේශ අනුගමනය කරන ලෙසත්, ඔබේ xpubs ආරක්ෂාවට භාජනය වී ඇති ලෙස සලකා බලන ලෙසත් උපදෙස් දෙමි.


ඔවුන්ගේම Dojo එකක් සමඟ Sparrow හෝ Samourai සෑම විටම භාවිතා කළ අය සඳහා, ඔබේ කාසි වල anonsets අඩු විය හැකි ප්‍රධාන අවදානම වේ. නරකම අවස්ථාවේදී, Dojo නොමැති සියලුම පරිශීලකයින්ගේ xpubs අධිකාරීන්ගේ අතේ ඇති බව සිතමු, එවිට ඔවුන්ගේ කාසි CoinJoin චක්‍ර හරහා ගමන් කිරීම මෙම අධිකාරීන් විසින් හඹා හැරිය හැක.


To illustrate this, let's take a concrete example. Imagine that you participated in a first cycle of CoinJoin, followed by two additional downstream CoinJoin cycles. If the xpubs of users without a Dojo have not leaked, then the prospective anonset of your coin would be 13.


![samourai](assets/37.webp)


Vendar, če upoštevamo, da so xpubs ušle in da ste naleteli na uporabnika brez doja med začetnim CoinJoin, in nato 2 med prvim navzdolnim CoinJoin, bi bila vaša pričakovana anonset le 10 namesto 13 z vidika oblasti.


![samourai](assets/38.webp)

To zmanjšanje anonseta je težko kvantificirati, saj je odvisno od številnih dejavnikov, in vsaka kovanec je prizadet drugače. Na primer, uporabnik brez Dojo, ki ga srečamo v zgodnjih ciklih, vpliva na potencialni anonset veliko bolj kot tisti, ki ga srečamo v kasnejših ciklih. Da bi vam dali predstavo o situaciji, ki ostaja hipotetična, so najnovejše statistike, ki jih je zagotovil Samourai, pokazale, da je med 85 % in 90 % kovancev, vključenih v coinjoin, prišlo od uporabnikov z Dojo, Sparrow ali Bitcoin Keeper, torej uporabnikov, ki, tudi v najslabšem primeru, ne bi videli svojih xpubs razkritih.

যদিও এই পরিসংখ্যানগুলি যাচাই করা কঠিন, তবে দুটি কারণে এগুলি আমার কাছে সামঞ্জস্যপূর্ণ মনে হয়:



- Sparrow Wallet බහුලව භාවිතා වේ;
- බොහෝ node-in-box මෘදුකාංග Dojo ක්‍රියාත්මක කිරීම් ලබා දේ, සහ Umbrel වැනි මෙම ප්‍රධාන ධාරා මෘදුකාංග අද කාලේ ඉතා ජනප්‍රිය වේ.


ඒ අනුව, විවිධ අංග සලකා බැලිය යුතුය. ඔබේ කාසිවල පෞද්ගලිකත්වය අධිකාරීන්ට සාපේක්ෂව ඉතා වැදගත් නම්, නරකම තත්ත්වයට සූදානම් වීම ප්‍රජ්ඣාවන්ත වන අතර, Dojo නොමැති පරිශීලකයන්ගෙන් xpubs කාන්දුවීමේ හැකියාව නිසා ඔබේ Whirlpool CoinJoin චක්‍ර අනුගමනය කළ නොහැකි බව 100% සහතික කිරීම දුෂ්කරය. මෙම උපකල්පනය ඉතා අසම්භාවිත වුවද, එය අසම්භාවිත නොවේ.


Po drugi strani, če zasebnost vaših kovancev v primerjavi z avtoriteto, ki je potencialno v posesti teh xpubs, ni ključna za vas, potem se lahko situacija obravnava drugače.


මම "අධිකාරියට සම්බන්ධව" යනුවෙන් විශේෂිතව සඳහන් කරන්නේ, සේවාදායකයන් අත්අඩංගුවට ගත් අධිකාරියට පමණක් මෙම xpubs පිළිබඳව දැනුවත් විය හැකි බව මතක තබා ගැනීම වැදගත් බැවිනි. ඔබේ අරමුණ CoinJoin භාවිතා කිරීමේදී ඔබේ බේකර්ට ඔබේ මුදල් අනුගමනය කිරීමට නොහැකි වීම නම්, සේවාදායකය අත්අඩංගුවට ගැනීමට පෙර ඔහුට වඩා හොඳින් දැනුවත් නොවේ.


අවසානයේ, සේවාදායකය අත්අඩංගුවට ගැනීමට පෙර, ඔබේ නாணයෙහි ආරම්භක anonset සලකා බැලීම අත්‍යවශ්‍ය වේ. 40,000 ක පුරෝකථන anonset එකක් ළඟා වූ නாணයක් උදාහරණයක් ලෙස ගනිමු; මෙම anonset එකේ සම්භාව්‍ය අඩු වීම ප්‍රයෝජනවත් නොවේ. ඇත්ත වශයෙන්ම, දැනටමත් ඉතා උසස් මූලික anonset එකක් ඇති විට, Dojo නොමැති කීප දෙනෙකුගේ පවතිම තත්ත්වය මූලිකව වෙනස් කළ හැකි බවක් නොපෙනේ. කෙසේ වෙතත්, ඔබේ නாணයෙහි anonset එක 40 ක් වූවා නම්, එම සම්භාව්‍ය කාන්දුව ඔබේ anonset වලට බරපතල බලපෑමක් ඇති කරමින් සොයා ගැනීමේ හැකියාව ලබා දිය හැක.

Ker je orodje WST zdaj nedelujoče po zaprtju OXT.me, lahko te anonsete le ocenjujete. Za retrospektivni anonset ni preveč skrbi, saj model Whirlpool zagotavlja, da je zelo visok že od prvega CoinJoin, zahvaljujoč zapuščini vaših vrstnikov. Edini primer, kjer bi to lahko predstavljalo težavo, je, če vaš kovanec ni bil premešan več let in je bil premešan na začetku lansiranja bazena. Kar zadeva perspektivni anonset, lahko preučite, kako dolgo je bil vaš kovanec na voljo za coinjoin. Če je bilo to več mesecev, potem verjetno ima izjemno visok perspektivni anonset. Nasprotno pa, če je bil dodan v bazen le nekaj ur pred zasegom strežnikov, je njegov perspektivni anonset verjetno zelo nizek.

[**-> anonsets සහ ඒවාගේ ගණනය කිරීමේ ක්‍රමය පිළිබඳව වැඩිදුර ඉගෙන ගන්න.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


තවත් සලකා බැලිය යුතු අංගයක් වන්නේ මිශ්‍ර කරන ලද කාසිවල anonsets මත ඒකාබද්ධතා වල බලපෑමයි. Whirlpool ගිණුම් Samourai යෙදුම හරහා දැන් ප්‍රවේශ විය නොහැකි බැවින්, බොහෝ පරිශීලකයින් තම Wallet වෙනත් මෘදුකාංග වෙත මාරු කර Whirlpool වෙතින් තම අරමුදල් ආපසු ගැනීමට උත්සාහ කර ඇති බව සම්භාව්‍ය වේ. විශේෂයෙන්ම, ගත වූ සති අන්තයේදී, Bitcoin ජාලයේ ගනුදෙනු ගාස්තු සාපේක්ෂව ඉහළ වූ විට, මිශ්‍ර කිරීමෙන් පසු කාසි ඒකාබද්ධ කිරීම සඳහා ශක්තිමත් තාක්ෂණික හා ආර්ථික ප්‍රේරණයක් තිබුණි. මෙය අදහස් කරන්නේ බොහෝ පරිශීලකයින් වැදගත් ඒකාබද්ධතා සිදු කර ඇති බව සම්භාව්‍ය වේ.


මෙම පසු-මිශ්‍රණ ඒකාබද්ධ කිරීම් සම්බන්ධ ගැටලුව වන්නේ, එය සෑම විටම අනොන්සෙට්ස් අඩු කරන අතර, එය සිදු කරන පරිශීලකයාට පමණක් නොව, ඔවුන්ගේ CoinJoin චක්‍රවලදී ඔවුන් හමුවූ පරිශීලකයන්ටද බලපාන බවයි. මම මෙම පරිසරය නිවැරදිව හෝ ප්‍රමාණවත් ලෙස සනාථ කිරීමට නොහැකි වුවද, එවකට ගනුදෙනු ගාස්තු සම්බන්ධ ආර්ථික ප්‍රතිලාභ අපට අනමාන කිරීමට ඉඩ සලසයි, අනොන්සෙට්ස් පහළ යා හැකි බව.


### Kot Sentinel uporabnik


Delovanje omrežja aplikacije Watch-only wallet Sentinel je podobno kot pri Samourai. Za dostop do vaših informacij Wallet mora aplikacija prenesti xpubs, javne ključe in naslove, ki ste jih posredovali Doju. Če ste vedno uporabljali svoj Dojo na Sentinel, ni težav in lahko brez skrbi nadaljujete z uporabo aplikacije. Vendar, če ste bili odvisni od strežnikov Samourai za vaš Sentinel, je možno, da so bili vaši xpubs izpostavljeni. V tem primeru je priporočljivo slediti istemu postopku spremembe Wallet, ki je priporočljiv za Samourai Wallet, ko ste povezani s strežniki Samourai.


අසම්භාවිත සිදුවීමකදී ඔබේ Dojo Samourai සමඟ භාවිතා කරමින් සිටියදී නමුත් Sentinel සමඟ නොමැති නම්, ඔබේ xpubs ආරක්ෂාවට භාජනය වී ඇති බව සලකා බැලීම වඩාත් සුදුසුය.


## Sklep


මෙම ලිපිය අවසානය දක්වා කියවීම සඳහා ඔබට ස්තූතියි. තොරතුරු අඩු වී ඇතැයි ඔබ සිතන්නේ නම් හෝ යෝජනා ඇති නම්, කරුණාකර ඔබේ අදහස් බෙදා ගැනීමට මට සම්බන්ධ වීමට කටයුතු කරන්න. අමතරව, මෙම උපකාරකය හරහා ඔබේ Samourai Wallet ප්‍රතිසාධනය කිරීමට වැඩි සහය අවශ්‍ය නම්, [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) වෙත එක්වීමට මම ඔබට ආරාධනා කරමි. මම නිතරම මෙම Discord වෙත පිවිසෙන අතර විසඳුමක් තිබේ නම් ඔබට සහය වීමට සතුටු වෙමි. අනෙක් බිට්කොයින්කරුවන්ටත් ඔවුන්ගේ අත්දැකීම් බෙදා ගැනීමට සහ ඔවුන්ගේ සහය ලබා දීමට හැකි වනු ඇත. **ඕනෑම අවස්ථාවක, ඔබේ ප්‍රතිසාධන වාක්‍යය, ඔබේ උපස්ථ ගොනුව, සහ ඔබේ passphrase රහසිගතව තබා ගැනීම අත්‍යවශ්‍ය වේ**. ඒවා කිසිවෙකුට හුවමාරු නොකරන්න, මන්ද එය ඔවුන්ට ඔබේ බිට්කොයින් සොරා ගැනීමට හැකි වේ.