---
name: Bitcoin Core (macOS & Windows)
description: Bitcoin Core මැක් හෝ වින්ඩෝස් මත ස්ථාපනය කරන්න
---

ඔබේ සාමාන්‍ය පරිගණකය මත Bitcoin Core ස්ථාපනය කළ හැකි නමුත් එය වඩාත් සුදුසු නොවේ. ඔබේ පරිගණකය පැය 24/7 ක් ක්‍රියාත්මක කිරීමට ඔබට කණගාටු නොමැති නම්, එය හොඳින් ක්‍රියා කරනු ඇත. ඔබට පරිගණකය අක්‍රිය කිරීමට අවශ්‍ය නම්, එය නැවත ක්‍රියාත්මක කරන සෑම විටම මෘදුකාංගය සමකාලීන වීමට බලා සිටීම කනස්සල්ලක් වේ.


Ta navodila so namenjena uporabnikom Mac ali Windows. Uporabniki Linuxa verjetno ne bodo potrebovali moje pomoči, vendar so navodila za Linux zelo podobna tistim za Mac.


## පැහැදිලිව ආරම්භ කරන්න


ඉතාමත් වශයෙන්, ඔබට මැලවෙයාර් නොමැති පිරිසිදු පරිගණකයක් භාවිතා කිරීමට අවශ්‍ය වේ. ඔබ Hardware Wallet භාවිතා කළත්, මැලවෙයාර් ඔබේ කාසි වංචා කිරීමට හැකි වේ.


ඔබට පැරණි පරිගණකයක් පිරිසිදු කළ හැකි අතර, එය කැපවූ Bitcoin පරිගණකයක් ලෙස භාවිතා කළ හැක, හෝ කැපවූ පරිගණකයක්/ලැප්ටොප් එකක් මිලදී ගත හැක.


## Hard ධාවකය


Bitcoin Core ඔබේ ඩ්‍රයිව් එකේ ගිගාබයිට් 400 ක් පමණ දත්ත ගත කරනු ඇති අතර, එය වර්ධනය වීමට පවත්නා වේ. ඔබේ අභ්‍යන්තර ඩ්‍රයිව් එක භාවිතා කළ හැකි නමුත්, ඔබට බාහිර Hard ඩ්‍රයිව් එකක්ද සම්බන්ධ කළ හැක. මම දෙකම විකල්ප පැහැදිලි කරමි. ඉතාමත් සුදුසු ලෙස, ඔබ solid-state ඩ්‍රයිව් එකක් භාවිතා කළ යුතුය. ඔබට පැරණි පරිගණකයක් තිබේ නම්, එහි අභ්‍යන්තරව මෙවැනි එකක් නොමැති විය හැක. සරලව 1 හෝ 2 ටෙරාබයිට් බාහිර SSD එකක් මිලදී ගෙන එය භාවිතා කරන්න. සාමාන්‍ය ඩ්‍රයිව් එක වැඩ කරනු ඇත, නමුත් ඔබට ගැටළු ඇති විය හැකි අතර එය බොහෝමයක් මන්දගාමී වේ.


![image](assets/1.webp)


## Bitcoin Core ඩවුන්ලෝඩ් කරන්න


pojdi na Bitcoin.org (poskrbi, da ne greš na Bitcoin.com, ki je stran s shitcoinom v lasti Rogerja Vera, ki ljudi zavaja, da kupujejo Bitcoin Cash namesto Bitcoin)


එතැනට ගිය පසු, මෘදුකාංගය ලබා ගැනීමට කොහෙද යන්න ඡේදය නොපෙනේ. සම්පත් මෙනුවට ගොස් "Bitcoin Core" ක්ලික් කරන්න, පහත දැක්වෙන පරිදි:


![image](assets/2.webp)


මෙය ඔබව බාගත කිරීමේ පිටුවට ගෙන යනු ඇත:


![image](assets/3.webp)


කොළපට Bitcoin මූලික බොත්තම බාගන්න:


![image](assets/4.webp)


ඔබේ පරිගණකය අනුව තෝරා ගත හැකි විකල්ප කිහිපයක් ඇත. මෙම මාර්ගෝපදේශයට අදාල පළමු දෙක වන්නේ; වම් තීරුවේ Windows හෝ Mac තෝරන්න. ඔබ එය ක්ලික් කිරීමෙන් පසු, එය බාගත වීම ආරම්භ වන අතර, බොහෝ විට ඔබේ බාගත කිරීම් නාමාවලියට යනු ඇත.


## බාගත කිරීම සත්‍යාපනය කරන්න (කොටස 1)


ඔබට විවිධ නිකුතු වල හෑෂ් අඩංගු ගොනුව අවශ්‍යයි. මෙම ගොනුව Bitcoin.org හි බාගත පිටුවේ තිබුණි, නමුත් දැන් bitcoincore.org/en/download වෙත ගෙන යාමට ඇත:


![image](assets/5.webp)


ඔබට SHA256 ද්වීමාණික හෑෂ් ගොනුව අවශ්‍ය වේ. මෙම ගොනුව Bitcoin මූලිකාංගයේ විවිධ බාගත කිරීම් පැකේජවල SHA256 හෑෂ් අඩංගු වේ.


ඊළඟට, අපිට Hash ලෙස Bitcoin මූලික බාගත කිරීම සිදු කර, ගොනුවේ සඳහන් Hash සමඟ එය සසඳන්න අවශ්‍ය වේ. එවිට bitcoincore.org අනුව බාගත කිරීම අපේක්ෂිත දේට සමාන බව අපට දැනගත හැක.


නැවත Downloads නාමාවලියට යන්න සහ මෙම විධානය ක්‍රියාත්මක කරන්න (Full node Bitcoin බාගත කිරීමේ ගොනු නාමය සමඟ X ගණන් ප්‍රතිස්ථාපනය කරන්න):


```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```


Dobili boste izhod Hash. Zabeležite si ga in ga primerjajte z Hash, ki je v datoteki SHA256SUMS.


Če so izhodi enaki, ste skoraj preverili, da noben del podatkov ni bil spremenjen. Še vedno moramo biti prepričani, da datoteka SHA256SUMS ni zlonamerna.


Če želimo nadaljevati z naslednjim korakom, moramo imeti na računalniku nameščen gpg.


ඒ සඳහා, මගේ SHA256/gpg මාර්ගෝපදේශය බලන්න, සහ "gpg බාගත කිරීම" කොටසට මැද භාගය පමණට ගොස්, ඔබේ මෙහෙයුම් පද්ධතියේ උපශීර්ෂිකාව සොයන්න. එවිට මෙහි නැවත පැමිණෙන්න.


## ජනතා යතුර ලබා ගන්න


ආපසු බාගත කිරීමේ පිටුවට, SHA256 Hash අත්සන ගොනුව ලබා ගන්න


![image](assets/6.webp)


එය ක්ලික් කර, ගොනුව තැටියට සුරකින්න, වඩාත් සුදුසු Downloads නාමාවලියට.


මෙම ගොනුවේ, SHA256SUMS ගොනුවේ අත්සන් තබා ඇති විවිධ පුද්ගලයන්ගේ අත්සන් අඩංගු වේ.


Želimo, da je javni ključ glavnega razvijalca, Wladimir J. van der Laan, v ključnem obroču našega računalnika. ID njegovega javnega ključa je:

1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964


I'm sorry, but I need the specific text you want translated. Could you please provide it?


```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```


Iz zanimanja lahko kadar koli vidite, kateri ključi so v računalnikovem obesku za ključe, s tem ukazom:


```bash
gpg --list-keys
```


## පිටුබැඳීම සනාථ කරන්න (භාග 2)


අපට මහජන යතුර තිබෙන නිසා, අපි දැන් Bitcoin Core බාගත කිරීමේ හෑෂ් සහ ඒවා සඳහා වූ අත්සන අඩංගු SHA256SUMS ගොනුව සත්‍යාපනය කළ හැක.


ටර්මිනල් හෝ CMD නැවත විවෘත කර, ඔබ Downloads නාමාවලිය තුළ සිටින බව සහතික කර ගන්න. එතැන් සිට, මෙම විධානය ක්‍රියාත්මක කරන්න:


```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```


පළමුව සඳහන් කරන ලද ගොනුව වන්නේ අත්සන ගොනුවේ නිවැරදි අක්ෂර වින්‍යාසයයි. දෙවනුව සඳහන් කරන ලද ගොනුව වන්නේ හෑෂ් ගොනුවේ අක්ෂර වින්‍යාසයයි. ගොනු දෙකම එකම නාමාවලිය තුළ තිබිය යුතු අතර ඔබ ගොනු ඇති නාමාවලිය තුළ සිටිය යුතුය, නැතහොත්, ගොනුවකට සම්පූර්ණ මාර්ගය ටයිප් කළ යුතුය.


To je izhod, ki bi ga morali dobiti


![image](assets/7.webp)


ඒ අනතුරු ඇඟවීමේ පණිවිඩය නොසලකා හැරීම ආරක්ෂිතය – එය ඔබට මතක් කරන එකක් පමණක් වන අතර ඔබ වැදගත් කොටසක Wladimir හමුවී ඔහුගේ මහජන යතුර කුමක්දැයි පුද්ගලිකව අසන ලදිද, එවිට ඔබේ පරිගණකයට මෙම යතුර සම්පූර්ණයෙන් විශ්වාස කිරීමට කියා ඇත.


Če ste prejeli to sporočilo, zdaj veste, da datoteka SHA256SUMS.asc ni bila spremenjena po tem, ko jo je Wladimir podpisal.


## Bitcoin මූලිකය ස්ථාපනය කරන්න


ඔබට වැඩසටහන ස්ථාපනය කරන ආකාරය පිළිබඳ විස්තරාත්මක උපදෙස් අවශ්‍ය ව shouldn't.


![image](assets/8.webp)


## Bitcoin කෝර් ධාවනය කරන්න


Mac මත, ඔබට අනතුරු ඇඟවීමක් ලැබිය හැක (Apple තවමත් anti-Bitcoin වේ)


![image](assets/9.webp)


OK ක්ලික් කරන්න, එවිට ඔබේ පද්ධති කැමැත්ත විවෘත කරන්න.


![image](assets/10.webp)


කොන්ත්‍රාත්‍රා සහ පෞද්ගලිකත්ව අයිකනය ක්ලික් කරන්න:


![image](assets/11.webp)


පසුව "open anyway" ක්ලික් කරන්න:


![image](assets/12.webp)


දෝෂය නැවත පෙනේවි, නමුත් මේ වතාවේ ඔබට OPEN බොත්තමක් ලබා ගත හැක. එය ක්ලික් කරන්න.


![image](assets/13.webp)


Bitcoin කෝර් should load and you’ll be presented with some options:


![image](assets/14.webp)


Tukaj lahko izberete uporabo privzete poti, kamor bo Blockchain prenesen, ali pa izberete zunanji pogon. Priporočam, da ne spreminjate privzete poti, če boste uporabljali notranji pogon, saj to olajša nastavitev, ko nameščate drugo programsko opremo za komunikacijo z Bitcoin Core.


ඔබට කපා දැමූ නියුඩ් එකක් ක්‍රියාත්මක කිරීමට තෝරා ගත හැක, එය අවකාශය සුරකියි, නමුත් ඔබේ නියුඩ් සමඟ ඔබට කළ හැකි දේ සීමා කරයි. ඕනෑම විටෙක, ඔබ සම්පූර්ණ Blockchain බාගත කරමින් එය සත්‍යාපනය කරමින් සිටින බැවින්, ඔබට අවකාශය තිබේ නම්, ඔබ බාගත කළ දේ තබා ගන්න, සහ එය වලක්වා ගත හැකි නම් කපා දැමීමෙන් වළකින්න.


ඔබ තහවුරු කළ පසු, Blockchain බාගත කිරීම ආරම්භ වේ. එය දින ගණනාවක් ගත වේ.


![image](assets/15.webp)


ඔබට කැමති නම් පරිගණකය නිවා දමා නැවත බාගත කිරීමට පැමිණිය හැක, එය කිසිදු හානියක් නොකරයි.