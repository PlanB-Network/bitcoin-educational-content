---
name: Nerdminer
description: Mining Bitcoin ආරම්භ කරන්න ජයග්‍රහණය කිරීමේ අවස්ථාව 0ට ආසන්නයි.
---

![cover](assets/cover.webp)

**ඔබේ NerdMiner_v2 පිහිටුවීම**


මෙම උපකාරිකාවේ, අපි ඔබට NerdMiner_v2 පිහිටුවීම සඳහා අවශ්‍ය පියවර මඟින් මඟ පෙන්වන්නෙමු, එය Bitcoin Mining සඳහා කැපවූ දෘඩාංග උපාංගයක් (ESP-32 S3) වේ.

ඇත්ත වශයෙන්ම, එවැනි උපාංගයක ගණනය කිරීමේ ශක්තිය, ආධුනික හෝ වෘත්තීය මයිනර්වරුන්ගේ ASIC සමඟ තරඟ කිරීමට නොහැක. එහෙත්, NerdMiner යනු Bitcoin Mining ස්පර්ශ කළ හැකි ආකාරයෙන් ඉගෙනුම් උපකරණයක් ලෙස පරිපූර්ණ වේ. සහ කවුරු දන්නවාද, (බොහෝ) වාසනාවක් සමඟ, ඔබට අවහිරයක් සොයා ගැනීමට සහ එයට අදාළ ත්‍යාගය ලබා ගැනීමට හැකි විය හැක. කුතුහලයෙන් පිරි, අපි [ජයග්‍රහණයේ සම්භාවිතාවය ඇස්තමේන්තුව](#estimation-de-la-probabilite-de-gain) කොටසෙහි දැකීමට ඇත. බල පරිභෝජනය සම්බන්ධයෙන්, NerdMiner එකක් 0.5W පරිභෝජනය කරයි; සසඳන විට, LED ලාම්පුවක් සාමාන්‍යයෙන් 20 ගුණයක් වඩා වැඩි පරිභෝජනය කරයි.


Prejden preden gremo skozi različne korake, naštejmo potrebno opremo za izdelavo:



- a [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- [USB-C power Supply](https://amzn.eu/d/gIOot90)
- 3D කේස් එකක්: ඔබට 3D මුද්‍රකයක් තිබේ නම්, ඔබට [3D ගොනුව](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) බාගත කළ හැකිය, නැතිනම් ඔබට [Silexperience ඔන්ලයින් වෙළඳසැලෙන්](https://silexperience.company.site/NerdMiner_V2-p544379757) එකක් මිලදී ගත හැකිය.
- Chrome Browser සමඟ පරිගණකයක්
- අන්තර්ජාල සම්බන්ධතාවයක්
- a Bitcoin Address


NerdMiner කට්ටලය පෙර සකස් කළ අයුරින් විකිණෙන විකිණුම්කරුවන් කිහිප දෙනෙකුගෙන්ද මිලදී ගත හැක:



- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-Miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)


පළමුව, අපි සොෆ්ට්වෙයාර්ය ESP-32 S3 මතට ෆ්ලෑෂ් කිරීමේ ක්‍රමය බලමු, එවිට wifi ජාලය වෙනස් කිරීමට එය නැවත ආරම්භ කරන ආකාරය බලමු. මෙම පියවරවල් Windows පරිශීලකයින් සඳහා වන අතර, ඔබ Linux මෙහෙයුම් පද්ධතියක් භාවිතා කරන්නේ නම්, ඔබේ පද්ධතිය විසින් ESP-32 S3 හඳුනා ගැනීම සඳහා [පූර්ව පියවර](#etapes-preliminaires-pour-utilisateurs-linux) සිදු කරන්න.


**NerdMiner_v2 Programske opreme namestitev** je močno poenostavljena zahvaljujoč uporabi spletnega utripalnika.


## පියවර 1: වෙබ්ෆ්ලෑෂර් සූදානම් කිරීම


Najprej morate iti na [online NM2 flasher](https://bitmaker-hub.github.io/diyflasher/).


එවිට ඔබේ ESP-32 සඳහා අදාළ firmware තෝරන්න. බොහෝ විට එය පෙරනිමි එක වේ: T-Display S3. එවිට "Flash" මත ක්ලික් කරන්න.


**සටහන⚠️ :** ඔබ Chrome බ්‍රවුසරය භාවිතා කිරීම වැදගත් වේ - එය පෙරනිමි ලෙස, ෆ්ලෑෂ් සහ ඔබේ USB වරාය වෙත ප්‍රවේශය භාවිතා කිරීමට ඉඩ සලසයි.


![image](assets/webflasher.webp)


## 2. korak: ESP-32 povežite


Ko webflasher zažene, se bo odprlo pojavno okno, ki bo prikazalo različna USB vrata, ki jih prepozna brskalnik.

ඔබට එවිට ඔබේ ESP-32 සම්බන්ධ කළ හැකි අතර නව වරායයක් පෙන්වනු ඇත (මෙම අවස්ථාවේදී, එය ttyACM0 වරාය වේ). එවිට ඔබ එය තෝරා "connect" මත ක්ලික් කළ යුතුය.


![image](assets/flasher-port-serial.webp)


සොෆ්ට්වෙයාර්ය ඔබගේ ESP32 වෙත තත්පර කිහිපයක් ඇතුළත බාගත කරනු ඇත.


![image](assets/NM2-sucessfully-installed.webp)


## පියවර 3: NerdMiner වින්‍යාසය


Vaša NerdMiner konfiguracija bo izvedena prek pametnega telefona ali računalnika.

WiFi සක්‍රීය කර, ස්ථානීය NerdMinerAP ජාලයට සම්බන්ධ වන්න. ඔබ ස්මාර්ට්ෆෝන් එකක් භාවිතා කරන්නේ නම්, වින්‍යාස ද්වාරය ස්වයංක්‍රීයව විවෘත වේ. නැතහොත්, බ්‍රවුසරයක Address 192.168.4.1 ටයිප් කරන්න.

පසුව "WiFi වින්‍යාස කරන්න" තෝරන්න.


ඔබට දැන් ඔබේ NerdMiner වින්‍යාසගත කළ හැක.

පළමුව, ඔබේ ජාල නාමය තෝරාගෙන සම්බන්ධිත මුරපදය ඇතුළත් කිරීමෙන් ඔබේ WiFi ජාලයට සම්බන්ධ වීම ආරම්භ කරන්න.


එවිට ඔබට සහභාගී වීමට අවශ්‍ය Mining pool තෝරා ගත හැක. ඇත්ත වශයෙන්ම, Bitcoin Mining කර්මාන්තයේ, Exchange හි බ්ලොක් එකක් සොයා ගැනීමේ අවස්ථාව වැඩි කිරීමට ගණනය කිරීමේ ශක්තිය එකතු කිරීම සාමාන්‍යයයි, Hashrate ලබා දුන් ප්‍රමාණයට අනුපාතව ත්‍යාගය බෙදා ගැනීම සඳහා.

NerdMiners සඳහා, ඔබට මෙම පූල් වලින් එකකට සම්බන්ධ වීමට තෝරා ගත හැක:


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

Ko izberete svoj bazen, morate vnesti svoj Bitcoin Address, da prejmete nagrado v primeru, da je (izjemoma) najden blok.


ඉන් අමතරව, NerdMiner ට කාලය නිවැරදිව පෙන්විය හැකි වන පරිදි ඔබේ කාල කලාපය තෝරන්න.

ඔබට දැන් "save" මත ක්ලික් කළ හැක.


![image](assets/wifi-configuration.webp)


චුක්‍රියාව, ඔබ දැන් Bitcoin Mining ජාලයේ කොටසක් වේ!


## NerdMiner Operation


NerdMinerv2 මෘදුකාංගය තුළ තෝරාගත හැකි තිර 3ක් ඇත, ඔබේ තිරයේ දකුණු පැත්තේ ඉහළ බොත්තම ක්ලික් කිරීමෙන් ඒවාට ප්‍රවේශ විය හැක:



- මුල් තිරය ඔබේ NerdMiner හි සංඛ්‍යා ලේඛන වෙත ප්‍රවේශය ලබා දේ.
- දෙවන තිරය කාලය, ඔබේ Hashrate, Bitcoin හි මිල, සහ අවරෝධ උසට ප්‍රවේශය ලබා දේ.
- තෙවැනි තිරය Bitcoin Mining ජාත්‍යන්තර ජාලය පිළිබඳ සංඛ්‍යා ලේඛන වෙත ප්‍රවේශය ලබා දේ.

![image](assets/NM2-screens.webp)


ඔබේ NerdMiner නැවත ආරම්භ කිරීමට, උදාහරණයක් ලෙස WiFi ජාලය වෙනස් කිරීමට, ඔබට ඉහළ බොත්තම තත්පර 5ක් තබා ගත යුතුය.


පහළ බොත්තම වරක් ඔබීමෙන් ඔබේ NerdMiner අක්‍රිය වේ. දෙවරක් ක්ලික් කිරීමෙන් තිර දිශානතිය පෙරළනු ඇත.


### Linux uporabniki: Predhodni koraki


මෙන්න Chrome එකට ඔබේ සීරියල් පෝට් එක Linux මත හඳුනාගන්න ක්‍රම.


1. සම්බන්ධිත වරාය හඳුනා ගන්න:



- ඔබේ ESP-32 පරිගණකයට සම්බන්ධ කරන්න.
- ටර්මිනල් එකක් විවෘත කරන්න.
- පහත විධානය ඇතුළත් කර සියලු වරාය ලැයිස්තුගත කරන්න:
  - `dmesg | grep tty`
  - or `ls /dev/tty*`
- პორტის დასაზუსტებლად, შეგიძლიათ გააგრძელოთ გამორიცხვით, ბრძანების გამეორებით ESP-32-ის გარეშე.


2. සම්බන්ධිත වරායේ අවසරය වෙනස් කරන්න:



- පෙරනිමි ලෙස, අනුක්‍රමික වරාය වෙත ප්‍රවේශය සඳහා root අවසර අවශ්‍ය විය හැක, එබැවින් ඔබේ පරිශීලකයා `dialout` කණ්ඩායමට එක් කිරීමෙන් ඒවා ලබා ගත හැක.
  - `sudo usermod -a -G dialout YOUR_USERNAME`, `YOUR_USERNAME` සමඟ ඔබේ පරිශීලක නාමය ප්‍රතිස්ථාපනය කරන්න.
  - එවිට මෙම පරිශීලකයා ලෙස පිවිසෙන්න, හෝ කණ්ඩායම් වෙනස්කම් බලපැවැත්වෙන බව සහතික කිරීම සඳහා පද්ධතිය නැවත ආරම්භ කරන්න.


දැන් ඔබේ ESP-32 ඔබේ පද්ධතිය විසින් හඳුනාගෙන ඇති බැවින්, මෘදුකාංග ස්ථාපනය සඳහා [පළමු පියවර](#etape-1-preparation-du-webflasher) වෙත ආපසු යා හැක.


## Sklep


In tukaj je! Vaš NerdMiner_v2 je zdaj konfiguriran in pripravljen za uporabo.


Mining සතුටක් සහ ඔබට වාසනාව ලැබේවා!


### ජය ගැනීමේ සම්භාවිතාව ඇස්තමේන්තු කිරීම


අපි Block reward ජය ගැනීමේ සම්භාවිතාව ඇස්තමේන්තු කිරීමේදී විනෝද විය යුතුය. මෙම ඇස්තමේන්තු කිරීම සරල වන අතර සම්භාවිතාවේ විශාලත්වය පමණක් ලබා ගැනීමට උත්සාහ කරයි.

NerdMiner lahko poveže le z bazenom "solo Mining pool", kar pomeni, da bazen ne združuje Hashrate vseh povezanih rudarjev, temveč deluje zgolj kot koordinator.

Zdaj pa recimo, da ima naš NerdMiner Hashrate približno 45kH/s.


Vedeti, da je skupni Hashrate približno 450 EH/s (ali 4,5 x 10^20 zgoščenk na sekundo), lahko upoštevamo, da je verjetnost najti naslednji blok 1 proti 100 milijonov milijard, kar je zelo zelo zelo malo verjetno, da bi se zgodilo. Tako poleg tega, da je izobraževalno orodje in predmet radovednosti, lahko NerdMiner služi kot loterijska srečka v Bitcoin Mining z marginalnimi električnimi stroški 0,5 W--čeprav, kot smo pravkar videli, je verjetnost zmage smešno nizka. Pa vendar, zakaj ne bi izzvali svoje sreče?


### Dodatne informacije


මෙම විෂයය පිළිබඳව වැඩිදුර කියවීමට අවශ්‍ය නම් මෙන්න කිහිපයෙක්:



- [NerdMiner_v2 project page](http://github.com/BitMaker-hub/NerdMiner_v2)
- [සම්පූර්ණ ලේඛනගත කිරීම NerdMiners](https://docs.bitwater.ch/nerd-Miner-v2/)