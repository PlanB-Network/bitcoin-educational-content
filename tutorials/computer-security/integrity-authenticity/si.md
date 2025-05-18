---
name: GnuPG
description: Kako preveriti celovitost in pristnost programske opreme?
---
![cover](assets/cover.webp)


සොෆ්ට්වෙයාර් බාගත කිරීමේදී, එය වෙනස් කර නොමැති බව සහ එය නිල මූලාශ්‍රයෙන් පැමිණ ඇති බව සහතික කිරීම ඉතා වැදගත් වේ. මෙය Bitcoin සම්බන්ධ සොෆ්ට්වෙයාර් සඳහා විශේෂයෙන් සත්‍ය වේ, උදාහරණයක් ලෙස Wallet සොෆ්ට්වෙයාර්, ඔබේ මුදල් වෙත ප්‍රවේශය ලබා දෙන යතුරු ආරක්ෂා කිරීමට ඔබට ඉඩ සලසයි. මෙම උපකාරකය තුළ, සොෆ්ට්වෙයාර් ස්ථාපනය කිරීමට පෙර එහි අඛණ්ඩතාවය සහ සත්‍යතාවය සනාථ කරන ආකාරය අපි බලන්නෙමු. අපි Sparrow Wallet උදාහරණයක් ලෙස භාවිතා කරමු, බිට්කොයින්කරුවන් අතර ප්‍රියතම Wallet සොෆ්ට්වෙයාර්, නමුත් ක්‍රියාවලිය වෙනත් සොෆ්ට්වෙයාර් සඳහාද සමාන වේ.


අඛණ්ඩතාව තහවුරු කිරීම යනු බාගත කළ ගොනුව වෙනස් කර නොමැති බව සහතික කිරීම සඳහා එහි ඩිජිටල් ගිලිප්ප (උදාහරණයක් ලෙස, එහි Hash) නිල සංවර්ධකයා විසින් සපයන ලද එක සමඟ සසඳීමයි. එම දෙකම ගැලපේ නම්, එය මුල් ගොනුවට සමාන බවත්, එය ප්‍රහාරකයෙකු විසින් විනාශ කර නොමැති හෝ වෙනස් කර නොමැති බවත් අර්ථ දක්වයි.


අනෙක් අතට, සත්‍යතාවය තහවුරු කිරීම යනු ගොනුව සත්‍ය වශයෙන්ම නිල සංවර්ධකයාගෙන් පැමිණ ඇති බව සහිත කිරීමයි, වංචාකාරයෙකුගෙන් නොව. මෙය ඩිජිටල් අත්සනක් තහවුරු කිරීමෙන් සිදු කරයි. මෙම අත්සන මෘදුකාංගය සත්‍ය සංවර්ධකයාගේ පෞද්ගලික යතුරෙන් අත්සන් කරන ලද බව පෙන්වයි.


මෙම පරීක්ෂා සිදු නොකළහොත්, වෙනස් කළ කේතයක් අඩංගු මාලවේයාර් ස්ථාපනය කිරීමේ අවදානමක් ඇත. මෙම කේතය ඔබේ පෞද්ගලික යතුරු වැනි තොරතුරු සොරා ගැනීමට හෝ ඔබේ ගොනු වෙත ප්‍රවේශය අවහිර කිරීමට හැකි වේ. විවෘත මූලාශ්‍ර මෘදුකාංගය සම්බන්ධයෙන් විශේෂයෙන්ම ව්‍යාජ අනුවාද බෙදා හැරිය හැකි බැවින් මෙම ප්‍රහාර වර්ගය ඉතා පොදු වේ.


මෙම සත්‍යාපනය සිදු කිරීමට, අපි මෙවලම් දෙකක් භාවිතා කරන්නෙමු: අඛණ්ඩතාව සත්‍යාපනය කිරීමට හැෂ් ක්‍රියාකාරකම්, සහ සත්‍යාපනය සත්‍යතාවය සත්‍යාපනය කිරීමට PGP ප්‍රොටෝකෝලය ක්‍රියාත්මක කරන විවෘත මූලාශ්‍ර මෙවලමක් වන GnuPG.


## ප්‍රාථමික අවශ්‍යතා


Če uporabljate **Linux**, je GPG prednameščen na večini distribucij. Če ni, ga lahko namestite z naslednjim ukazom:


```bash
sudo apt install gnupg
```


**macOS** සඳහා, ඔබට Homebrew පැකේජ් කළමනාකරු දැනටමත් ස්ථාපනය කර නැත්නම්, පහත විධාන සමඟ එය කරන්න:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


පසුව මෙම විධානයෙන් GPG ස්ථාපනය කරන්න:


```bash
brew install gnupg
```

**Windows** සඳහා, ඔබට GPG නොමැති නම්, ඔබට [Gpg4win](https://www.gpg4win.org/) මෘදුකාංගය ස්ථාපනය කළ හැක.

![GnuPG](assets/notext/01.webp)


## ලේඛන බාගත කිරීම


Za začetek bomo potrebovali različne dokumente. Obiščite uradno stran [Sparrow Wallet v razdelku "*Prenos*"](https://sparrowwallet.com/download/). Če želite preveriti drugo programsko opremo, pojdite na spletno stran te programske opreme.


![GnuPG](assets/notext/02.webp)


ඔබට [ව්‍යාපෘතියේ GitHub ගබඩාවට](https://github.com/sparrowwallet/sparrow/releases) යා හැක.


![GnuPG](assets/notext/03.webp)


ඔබේ මෙහෙයුම් පද්ධතියට අදාළ මෘදුකාංගය සඳහා ස්ථාපකය බාගන්න.


![GnuPG](assets/notext/04.webp)


ඔබට ගොනුවේ Hash, "*SHA256SUMS*" හෝ "*MANIFEST*" ලෙස හඳුන්වන, අවශ්‍ය වනු ඇත.


![GnuPG](assets/notext/05.webp)


දැන්වීම් `.asc` ආකෘතියේ ලිපියද බාගත කරන්න.


![GnuPG](assets/notext/06.webp)


සියලුම ගොනු එකම ෆෝල්ඩරයක තබා ඇති බව සහතික වන්න.


අවසානයේ, ඔබට සංවර්ධකයාගේ පොදු යතුර අවශ්‍ය වන අතර, අපි PGP අත්සන සත්‍යාපනය කිරීමට එය භාවිතා කරමු. මෙම යතුර බොහෝ විට මෘදුකාංගයේ වෙබ් අඩවියෙන්, ව්‍යාපෘතියේ GitHub ගබඩාවේ, සමහර විට සංවර්ධකයාගේ සමාජ මාධ්‍ය මඟින් හෝ Keybase වැනි විශේෂිත අඩවිවලින් ලබා ගත හැක. Sparrow Wallet සදහා, ඔබට සංවර්ධක Craig Rawගේ පොදු යතුර [Keybase හි](https://keybase.io/craigraw) සොයා ගත හැක. එය ටර්මිනල් එකෙන් සෘජුවම බාගත කිරීමට, විධානය ක්‍රියාත්මක කරන්න:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## හස්තය සනාථ කිරීම


**Windows**, **macOS**, සහ **Linux** මත අත්සන සත්‍යාපනය කිරීමේ ක්‍රියාවලිය සමාන වේ. සාමාන්‍යයෙන්, ඔබ පෙර පියවරේදී මහජන යතුර ආයාත කර ඇත, නමුත් එසේ නොමැති නම්, විධානය සමඟ එය කරන්න:


```bash
gpg --import [key path]
```


[key path] මගින් සංවර්ධකයාගේ පොදු යතුරු ගොනුවේ ස්ථානය සොයා ගන්න.


![GnuPG](assets/notext/08.webp)


හස්තය පහත විධානයෙන් සනාථ කරන්න:


```bash
gpg --verify [file.asc]
```


[file.asc] ට අත්සන ගොනුවේ මාර්ගය සමඟ ප්‍රතිස්ථාපනය කරන්න. Sparrow සඳහා, මෙම ගොනුව "*sparrow-2.0.0-manifest.txt.asc*" ලෙස 2.0.0 අනුවාදය සඳහා නම් කර ඇත.


![GnuPG](assets/notext/09.webp)


ඔත්තු ලිපිය වලංගු නම්, GPG ඔබට මෙය දක්වනු ඇත. මෙය ගොනුවේ සත්‍යතාවය තහවුරු කරන බැවින්, ඔබට ඊළඟ පියවරට ගමන් කළ හැක.


![GnuPG](assets/notext/10.webp)


## Hash සත්‍යාපනය කිරීම

හෙවත් මෘදුකාංගයේ සත්‍යතාවය තහවුරු කර ඇති බැවින්, එහි අඛණ්ඩතාවය තහවුරු කිරීමද අවශ්‍ය වේ. අපි මෘදුකාංගයේ Hash සංස්කරණය සංවර්ධකයා විසින් සපයන ලද Hash සමඟ සසඳන්නෙමු. එම දෙකම ගැලපේ නම්, එය මෘදුකාංග කේතය වෙනස් කර නොමැති බව සහතික කරයි.


**Windows** මත, ටර්මිනල් එකක් විවෘත කර පහත විධානය ක්‍රියාත්මක කරන්න:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


`[ස්ථානය]` ස්ථානයෙන් ස්ථාපකය.


![GnuPG](assets/notext/11.webp)


ටර්මිනල්ය බාගත කළ මෘදුකාංගයේ Hash ආපසු ලබා දේ.


![GnuPG](assets/notext/12.webp)


සමහර සොෆ්ට්වෙයා සඳහා, SHA256 වෙනුවට වෙනත් Hash ක්‍රියාකාරකමක් භාවිතා කිරීම අවශ්‍ය විය හැක. මෙම අවස්ථාවේ, විධානයේ Hash ක්‍රියාකාරකමේ නම සරලව මාරු කරන්න.


පසුව ප්‍රතිඵලය "*sparrow-2.0.0-manifest.txt*" ගොනුවේ අදාළ අගය සමඟ සසඳන්න.


![GnuPG](assets/notext/13.webp)


මගේ අවස්ථාවේ, අපි දකින්නේ එම හෑෂ් දෙකම සම්පූර්ණයෙන් ගැලපෙන බවයි.


**macOS** සහ **Linux** මත, Hash සත්‍යාපන ක්‍රියාවලිය ස්වයංක්‍රීය වේ. Windows මත පරික්‍ෂා කළ යුතු ලෙස හෑෂ් දෙක අතර ගැලපීම අතින් පරීක්ෂා කිරීම අවශ්‍ය නොවේ.


මෙම විධානය **macOS** මත සරලව ක්‍රියාත්මක කරන්න:


```bash
shasum --check [file name] --ignore-missing
```


`[file name]` ස්ථානයේ ස්ථාපකයේ නම යොදන්න. උදාහරණයක් ලෙස, Sparrow Wallet සඳහා:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


ඔබේ හෑෂ් එකතු වනවා නම්, ඔබට පහත ප්‍රතිදානය දැකිය යුතුය:


```bash
Sparrow-2.0.0.dmg: OK
```


**Linux**-ზე, ბრძანება მსგავსია:


```bash
sha256sum --check [file name] --ignore-missing
```


ඔබේ හෑෂ් එකතු වනවා නම්, ඔබ පහත ප්‍රතිදානය දැකිය යුතුය:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


ඔබ දැන් බාගත කළ මෘදුකාංගය සත්‍ය සහ අඛණ්ඩ බවට විශ්වාසයි. ඔබේ යන්ත්‍රය මත එය ස්ථාපනය කිරීමට ඔබට ඉදිරියට යා හැක.


ඔබට මෙම උපකාරිකාව ප්‍රයෝජනවත් වූවා නම්, පහත අඟුල් මුරය සඳහා ස්තූතියි. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තූතියි!


Priporočam tudi ogled tega drugega vodiča o VeraCrypt, programski opremi, ki omogoča šifriranje in dešifriranje pomnilniških naprav.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5