---
name: Bacca
description: Ledger Live මෘදුකාංගය නොමැතිව Ledger සකසීම
---
![cover](assets/cover.webp)


Če uporabljate Ledger, ste verjetno ugotovili, da morate za začetno konfiguracijo naprave uporabiti programsko opremo Ledger Live, da preverite njeno pristnost in nanjo namestite aplikacijo Bitcoin. Vendar pa po tej konfiguraciji mnogi bitcoinerji raje uporabljajo specializirano programsko opremo za upravljanje Bitcoin Wallet, kot sta Sparrow ali Liana, namesto Ledger Live. Čeprav Ledger proizvaja odlične strojne denarnice, ki hitro vključujejo najnovejše funkcije Bitcoin, njihova programska oprema ni nujno prilagojena specifičnim potrebam bitcoinerjev. Dejansko Ledger Live vključuje številne funkcije, namenjene altcoinom, medtem ko so možnosti, namenjene upravljanju Bitcoin Wallet, omejene. Toda težava s Sparrow in Liana (zaenkrat) je, da ne omogočajo namestitve aplikacije Bitcoin na Ledger.


ඔබේ Ledger ආරම්භක වින්‍යාසය අතරතුර Ledger Live භාවිතා කිරීම අවශ්‍යතාවය වළක්වා ගැනීමට, ඔබට Bacca මෙවලම (හෝ "Ledger ස්ථාපකය") භාවිතා කළ හැක. මෙම මෘදුකාංගය ඔබට Bitcoin යෙදුම ස්ථාපනය කිරීමට සහ යාවත්කාලීන කිරීමට, ඔබේ Ledger හි සත්‍යතාවය සනාථ කිරීමට, සහ පසුව උපාංගයේ ෆාර්ම්වේයර් යාවත්කාලීන කිරීමට ඉඩ සලසයි. Bacca නිර්මාණය කළේ Antoine Poinsot (Darosior), Chaincode Labs හි Bitcoin Core සංවර්ධකයෙකු, Revault සහ Liana හි සහ-ස්ථාපකයෙකු, සහ Pythcoiner.


මෙම උපකාරිකාවේ, මම ඔබට මෙම මෙවලම භාවිතා කරන ආකාරය පෙන්වන්නම්, එවිට ඔබට Ledger Live මෘදුකාංගය අවශ්‍ය නොවී, Ledger උපාංග භුක්ති විඳිය හැක. එය සියලු උපාංගවල ක්‍රියා කරයි: Nano S Classic, Nano S Plus, Nano X, Flex සහ Stax.


---
*කරුණාකර සලකන්න මෙම මෙවලම තවමත් නවීන වන අතර, එහි සංවර්ධකයින් එය **පරීක්ෂණ අදියරේ** පවතින බව විශේෂිත කරති. ඔවුන් එය පරීක්ෂණ අරමුණු සඳහා පමණක් භාවිතා කරන ලෙසත්, සැබෑ Bitcoin Wallet සත්කාරකය සඳහා අදහස් කරන උපකරණයක් සඳහා නොවන ලෙසත් නිර්දේශ කරති, එහෙත් එය කිරීමට හැකියාව ඇත. මෙම සම්බන්ධයෙන්, මෙම මෙවලමේ සංවර්ධකයින්ගේ නිර්දේශ අනුගමනය කරන ලෙස මම නිර්දේශ කරමි, ඒවා ඔවුන්ගේ GitHub ගබඩායේ README හි විශේෂිත කර ඇත [මෙහි](https://github.com/darosior/ledger_installer).*


---
## ප්‍රාථමික අවශ්‍යතා


ඔබේ පරිගණකයේ, Bacca භාවිතා කිරීමට ඔබට මෙවලම් දෙකක් අවශ්‍ය වේ:




- Git ;
- Rust.


če ste jih že namestili, lahko ta korak preskočite.


**Linux:**


ලිනක්ස් බෙදාහැරීමක, Git සාමාන්‍යයෙන් පෙර ස්ථාපනය කර ඇත. Git ඔබේ පද්ධතියේ ස්ථාපනය කර ඇතිදැයි පරීක්ෂා කිරීමට, ඔබට ටර්මිනල් එකේ පහත විධානය ටයිප් කළ හැක :


```bash
git --version
```


Če Git ni nameščen v vašem sistemu, tukaj je ukaz za namestitev na Debian:


```bash
sudo apt install git
```


අවසන් වශයෙන්, ඔබේ Rust සංවර්ධන පරිසරය ස්ථාපනය කිරීමට, විධානය භාවිතා කරන්න :


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Windows:**


Git ස්ථාපනය කිරීමට, [ව්‍යාපෘතියේ නිල වෙබ් අඩවිය](https://git-scm.com/) වෙත යන්න. මෘදුකාංගය බාගත කර ස්ථාපන උපදෙස් අනුගමනය කරන්න.


![BACCA](assets/fr/01.webp)


Rust [නිල වෙබ් අඩවියෙන්](https://www.Rust-lang.org/tools/install) ස්ථාපනය කිරීමට ඒම මාර්ගයෙන්ම ඉදිරියට යන්න.


![BACCA](assets/fr/02.webp)


**MacOS:**


Če Git še ni nameščen v vašem sistemu, odprite terminal in za namestitev zaženite naslednji ukaz:


```bash
git --version
```


If Git ni nameščen v vašem sistemu, se bo odprlo okno, ki vam bo ponudilo namestitev Xcode, ki vključuje Git. Preprosto sledite navodilom na zaslonu, da nadaljujete z namestitvijo.


Rust ස්ථාපනය කිරීමට, පහත විධානය ක්‍රියාත්මක කරන්න:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Bacca ස්ථාපනය


ටර්මිනල් එකක් විවෘත කර, මෘදුකාංගය සුරක්ෂිත කිරීමට අවශ්‍ය ෆෝල්ඩරයට යන්න, එවිට පහත විධානය ක්‍රියාත්මක කරන්න:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


සොෆ්ට්වෙයා නාමාවලියට යන්න:


```bash
cd ledger_installer
```


ඉන්පසු Cargo භාවිතා කරමින් ව්‍යාපෘතිය සම්පාදනය කර Bacca GUI ක්‍රියාත්මක කරන්න:


```bash
cargo run -p ledger_manager_gui
```


ඔබට දැන් Interface මෘදුකාංගයට ප්‍රවේශය ඇත.


![BACCA](assets/fr/03.webp)


## Ledger සකසමින්


මීට පෙර ඔබ ආරම්භ කරන විට, ඔබේ Ledger නවයි නම්, PIN කේතය සකසා ගෙන, ප්‍රතිසාධන වාක්‍යය සුරැකීම සිදුකර ඇති බව සහතික වන්න. මෙම ආරම්භක පියවර සඳහා ඔබට Ledger Live අවශ්‍ය නොවේ. එය බලය ලබා දීමට ඔබේ Ledger USB කේබල් මඟින් සම්බන්ධ කරන්න. මෙම පියවර දෙක සිදු කරන ආකාරය පිළිබඳව ඔබට විශ්වාස නොමැති නම්, ඔබේ ආකෘතිය සඳහා විශේෂිත උපකාරකයේ ආරම්භය වෙත යොමු විය හැක:


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Bacca භාවිතා කිරීම


ඔබේ Ledger පරිගණකයට සම්බන්ධ කර, ඔබ සකසා ඇති PIN කේතය භාවිතයෙන් එය අගුළු අරින්න. Bacca ඔබේ Ledger ස්වයංක්‍රීයව හඳුනා ගත යුතුය.


![BACCA](assets/fr/04.webp)


ඔබේ Ledger හි සත්‍යතාවය තහවුරු කිරීමට, "*Check*" බොත්තම ක්ලික් කරන්න. දිගටම ක්‍රියාත්මක වීමට ඔබේ Ledger උපාංගයේ සම්බන්ධතාවය අනුමත කළ යුතුය.


![BACCA](assets/fr/05.webp)


Bacca vam bo nato sporočil, ali je vaš Ledger pristen. Če ni, to pomeni, da je bila naprava bodisi ogrožena bodisi ponarejena. V tem primeru jo takoj prenehajte uporabljati.


![BACCA](assets/fr/06.webp)


"*Apps*" मेनू में, आप अपने Ledger पर पहले से इंस्टॉल किए गए एप्लिकेशन की सूची देख सकते हैं।


![BACCA](assets/fr/07.webp)


Bitcoin යෙදුම ස්ථාපනය කිරීමට, "*Install*" මත ක්ලික් කරන්න, එවිට ඔබේ Ledger මත ස්ථාපනයට අනුමැතිය දිය යුතුය.


![BACCA](assets/fr/08.webp)


යෙදුම හොඳින් ස්ථාපනය කර ඇත.


![BACCA](assets/fr/09.webp)


Če nimate nameščene najnovejše različice aplikacije Bitcoin, bo Bacca namesto oznake "*Latest*" prikazal gumb "*Update*". Preprosto kliknite na ta gumb, da posodobite aplikacijo.


![BACCA](assets/fr/10.webp)


Zdaj, ko je vaš Ledger pravilno konfiguriran z najnovejšo različico aplikacije Bitcoin, ste pripravljeni uvoziti in uporabljati vaš Wallet na programski opremi za upravljanje, kot sta Sparrow ali Liana, brez potrebe po uporabi Ledger Live!


ඔබට මෙම උපකාරිකාව ප්‍රයෝජනවත් වූවා නම්, Green අඟුලක් පහළින් දමා මම කෘතඥ වෙමි. මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. බොහෝම ස්තූතියි!


මම ඔබට GnuPG පිළිබඳ මෙම උපකාරකයද බලන්න යෝජනා කරමි, එය ඔබේ මෘදුකාංගය ස්ථාපනය කිරීමට පෙර එහි අඛණ්ඩතාවය සහ සත්‍යතාවය පරීක්ෂා කරන ආකාරය පැහැදිලි කරයි. මෙය වැදගත් පුරුද්දකි, විශේෂයෙන් Liana හෝ Sparrow වැනි Wallet කළමනාකරණ මෘදුකාංග ස්ථාපනය කරන විට:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc