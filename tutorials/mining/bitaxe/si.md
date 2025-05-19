---
name: BitAxe සකසීම
description: Kako nastaviti BitAxe?
---

### පෙරමුණ


BitAxe යනු Skot විසින් නිර්මාණය කරන ලද විවෘත මූලාශ්‍ර ව්‍යාපෘතියක් වන අතර [GitHub හි ලබා ගත හැක](https://github.com/skot/bitaxe) එය පිරිවැය ආරක්ෂාකාරී Mining පරීක්ෂණ සඳහා ඉඩ සලසයි.


Obratno je inženiralo delovanje slavnega Antminer S19 podjetja Bitmain, vodilnega na trgu ASIC-ov, specializiranih strojev za Bitcoin Mining. Zdaj je mogoče te zmogljive čipe uporabiti v novih odprtokodnih projektih. Za razliko od Nerdminerja ima BitAxe zadostno računsko moč, da se poveže z Mining pool, kar vam bo omogočilo redno zaslužiti nekaj satoshijev. Nerdminer pa se lahko poveže le s t.i. solopool, ki deluje kot loterijska srečka: imate majhno možnost, da osvojite celoten Block reward.


BitAxe-এর বিভিন্ন সংস্করণ রয়েছে, বিভিন্ন চিপ এবং পারফরম্যান্স সহ:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

මෙම උපකාරිකාවේදී, අපි BitAxe Ultra 204, BM1366 චිප් එකකින් සන්නද්ධ, Antminer S19XP සඳහා භාවිතා කරන, භාවිතා කරමු. මෙය දැනටමත් සිල්ලර වෙළෙන්දා විසින් එකලස් කර, ෆ්ලෑෂ් කර ඇත.


### [ලෙස්ට් වෙළඳසැල් මෙම පිටුවේ ලබා ගත හැක](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


සාමාන්‍යයෙන්, Supply බලය එය සමඟ විකිණේ. එසේ නොමැති නම්, 5V ජැක් කේබල් සහ අවම වශයෙන් 4A සහිත Supply බලය මිලදී ගැනීමට ඔබට අවශ්‍ය වේ.


![signup](assets/1.webp)


### වින්‍යාසය

ඔබේ BitAxe පළමුවෙන් plug කරන විට, එය පෙරනිමි ලෙස Wi-Fi ජාලයකට සම්බන්ධ වීමට උත්සාහ කරයි. උත්සාහ පහක් කළ පසු, එය එහිම Wi-Fi ජාලයේ නම පෙන්වනු ඇත, එවිට ඔබට එයට සම්බන්ධ වී එය වින්‍යාස කළ හැක.

මෙය කිරීමට, ඔබට ඕනෑම පරිගණකයක් හෝ ස්මාර්ට්ෆෝනයක් භාවිතා කළ හැක. ඔබේ Wi-Fi සැකසුම් වෙත යන්න, නව ජාල සොයන්න, සහ ඔබට Bitaxe_XXXX නම් Wi-Fi එකක් පෙනේවි. මෙහි, එය `Bitaxe_A859` වේ. මෙම Wi-Fi ජාලයට සම්බන්ධ වන්න, සහ කවුළුවක් ස්වයංක්‍රීයව විවෘත වේ.


![signup](assets/3.webp)


මෙම කවුළුවේ, ඉහළ වම තෙවන කුඩා තිරස් තීරු මත ක්ලික් කරන්න, එවිට `සැකසුම්` මත ක්ලික් කරන්න.


![signup](assets/4.webp)


ඔබට ඔබේ Wi-Fi ජාල තොරතුරු අතින් ඇතුළත් කිරීමට අවශ්‍ය වන අතර, ස්වයංක්‍රීය සොයා ගැනීමේ පද්ධතියක් නොමැත.


![signup](assets/5.webp)


අදාළව, Wi-Fi හි SSID, එනම්, ඔබේ ජාලයේ නම, මුරපදය, සහ ඔබ තෝරාගත් Mining pool පිළිබඳ තොරතුරු සපයන්න. අවධානයෙන් සිටින්න, මෙහිදී පූල් URL එක එකම ආකාරයෙන් ඉදිරිපත් නොවේ. උදාහරණයක් ලෙස, Braiins සඳහා, සපයන ලද පූල් URL එක මෙසේ වේ: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


ඔබට තිරයේ දැකගත හැකි පරිදි, `stratum+tcp://` සහ `:3333` කොටස් ඉවත් කළ යුතු අතර, `eu.stratum.braiins.com` පමණක් ඉතිරි වේ. එවිට, `Port` ක්ෂේත්‍රයේ, පූලය විසින් ලබා දෙන ලද URL එකේ අග部分යේ අංක 4ක් ඇතුළත් කරන්න, නමුත් `:` නැතිව. මෙහිදී, එය `3333` වේ.


මෙම උපකාරිකාවේ, අපි Braiins Mining pool භාවිතා කරමින් සිටිමු, නමුත් ඔබට වෙනත් එකක් තෝරා ගැනීමට නිදහස් වේ. ඔබට Mining පොකුරු පිළිබඳ අපගේ උපකාරිකා [PlanB ජාල වෙබ් අඩවියෙන්](https://planb.network/en/tutorials/Mining) සොයා ගත හැක.


Naslednje, v `User` vnesite svoj identifikator in nato `Password`, običajno je to `"x"` ali `"Anything123"`.


`Core Voltage` සැකසුම පෙරනිමියෙන්ම `1200` ලෙස තබා තිබිය යුතු අතර, `Frequency` සඳහාද ආරම්භකව පෙරනිමි අගය තබා ගන්න. වැඩි ගණනේ ගණනය කිරීමේ බලය ලබා ගැනීම සඳහා මෙම සැකසුම පසුව සකස් කළ හැකි වේ. කෙසේ වෙතත්, චිප් එකේ උෂ්ණත්වය 65-70°C ඉක්මවා නොයන බව සහතික කිරීම වැදගත් වේ, මන්ද BitAxe එකේ උෂ්ණත්වය වැඩි වුවහොත් කාර්ය සාධනය අඩු කිරීමේ පද්ධතියක් නොමැත. උෂ්ණත්වය 65°C ඉක්මවා ගියහොත්, ඔබේ BitAxe එකට හානි විය හැක.


![signup](assets/7.webp)


ඔබ සියලු සැකසුම් නිවැරදිව ඇතුළත් කළ පසු, පහළ ඇති `Save` බොත්තම ක්ලික් කරන්න, එවිට ඔබේ BitAxe නැවත ආරම්භ කිරීමට, එය විදෙස් කර නැවත සම්බන්ධ කිරීමෙන් පමණක් කරන්න.

ඔබේ තොරතුරු නිවැරදිව ඇතුළත් කර ඇත්නම්, උපාංගය ඉක්මනින් ඔබේ Wi-Fi වෙත සම්බන්ධ විය යුතු අතර, එවිට Mining pool වෙත සම්බන්ධ වී, එහි කුඩා තිරය මත කිසියම් තොරතුරු පෙන්වීමට ආරම්භ කළ යුතුය. එය Mining pool හි ඩෑෂ්බෝඩ් මත පෙනීමට විනාඩි කිහිපයක් ගත විය හැක.

### ඩෑෂ්බෝඩ් සහ තිරය


තෝරෝ විවිධ තිර දර්ශන තුනක් ගොස්සනු ඇත. තුන්වන පිටුවේදී, ඔබට `IP` තොරතුරු දැකගත හැකි වන අතර, එය ඔබට පුවරුවට සම්බන්ධ වීමට ඉඩ දෙන IP Address වේ. මෙහි, Address වන්නේ `192.168.1.19` ය.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


Address ටැක්සා මගින් ඩෑෂ්බෝඩ් වෙත ප්‍රවේශ වීමට, එය ඔබේ අන්තර්ජාල බ්‍රවුසරය තුළ ඇතුළත් කරන්න.


ඩෑෂ්බෝඩ් එකේ, ඔබට සියලුම තොරතුරු කුඩා තිරය මත පෙන්වා ඇති බව සොයා ගත හැකි අතර, දැන් අපි එය විස්තරාත්මකව බලමු.


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

ඔබට Wi-Fi හෝ දියකාමර සැකසුම් ඕනෑම වේලාවක කිසිදු ගැටළුවක් නොමැතිව වෙනස් කළ හැක.

ඔබේ කාමරයේ වාතාශ්‍රය සහ උෂ්ණත්වය අනුව, උෂ්ණත්වය 65°C ඉක්මවන ලෙස නොමැතිව කාර්ය සාධනය වැඩි කිරීමට හෝ අඩු කිරීමට ඔබට අවශ්‍ය විය හැක. ඔබ කාර්ය සාධනය වැඩි කළහොත්, ඔබට වැඩි සතෝෂි උපයන්නට හැකි වන අතර, නමුත් ඔබේ BitAxe වැඩි විදුලි බලයක් පරිභෝජනය කරනු ඇත!