---
name: Sats.mobi

description: ටෙලිග්‍රාම්-ප්‍රවේශ කළ හැකි අනුශාසක Wallet
---

![cover](assets/cover.webp)


_මෙම උපකාරකය ලියා ඇතිේ_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)  විසිනි.


## Sats.Mobi

SatsMobi je Wallet, ki deluje na Telegramu in vključuje vse funkcionalnosti Lightning Network (skrbniški) Wallet, poleg tega pa še vrsto zelo zabavnih funkcij. Izvira iz Fork zdaj že ukinjenega LightningTipBot, podedoval je vse njegove funkcije in dodal še bolj sodobne, kar ga naredi bolj modernega. Tako kot LNTipBot tudi Sats.Mobi sprejema filozofijo odprte kode. Wallet je mogoče konfigurirati in upravljati neodvisno s kloniranjem iz tega [repozitorija](https://github.com/massmux/SatsMobiBot).


ඔබ එය සරලව භාවිතා කිරීමට කැමති නම්, Telegram මත කතාබස් ආරම්භ කිරීමෙන් එය බොට් එකක් බව හෙළි වේ.


## සැකසුම්

ටෙලිග්‍රෑම් සෙවුම් තීරුවෙන් "satsmobi" සොයන්න, එවිට [බොට්](@SatsMobiBot) වෙත සබැඳිය පෙනේ.


**අවධානය**: ඔබට Telegram හරහා සෙවීම පිළිබඳව විශ්වාස නොමැති නම්, පහත [සබැඳිය](https://t.me/SatsMobiBot) භාවිතයෙන් බොට්ටුව ආරක්ෂිතව ප්‍රවේශ වන්න.


![image](assets/it/01.webp)


ඔබට ආරම්භ කිරීමට අවශ්‍ය සියල්ල _START_ ඔබන්නයි.


![image](assets/it/02.webp)


Wallet හඳුනා ගැනීමට, ඔබට වම් පහළින් _Menu_ තෝරා ගත හැක.


![image](assets/it/03.webp)


Zdaj izberite _/help_ med glavnimi ukazi.


![image](assets/it/04.webp)


Sats.Mobi nas pozdravi z prikazom sporočila, ki našteva vse glavne funkcionalnosti. Ob zagonu je bot ustvaril tudi LN Address, povezan z izbranim imenom na Telegramu (ki je privzeto edinstveno). Vidni so ukazi za pošiljanje in prejemanje Sats s tem Wallet, kot tudi druge funkcije, ki jih bomo videli kasneje. Zanimivo je tudi pogledati meni _/advanced_.


![image](assets/it/05.webp)


Sats.Mobi විසින් පෞද්ගලිකත්වය ලබා ගැනීම සඳහා අනාමික LN Address එකක්ද නිර්මාණය කර ඇති බව දැකිය හැක. බොට් එක විධාන සමඟ ක්‍රියා කරයි: සම්බන්ධ වචනය මත ක්ලික් කරන්න, හෝ පණිවිඩ තීරුවේ "/" ලකුණ ටයිප් කර, ඔබට ක්‍රියාත්මක කිරීමට අවශ්‍ය විධානය ඇතුළත් කරන්න. Wallet නව නිර්මාණයක් වුවත්, උදාහරණයක් ලෙස _/transactions_ තෝරන්න.


![image](assets/it/06.webp)


මෙම විධානය නවතම ගනුදෙනු ලැයිස්තුව පෙන්වයි, මෙම විශේෂිත අවස්ථාවේ ශුන්‍යයට සමාන වේ.


![image](assets/it/07.webp)


## Sats ලබා ගැනීම

Invoice සහ Sats ලබා ගැනීමට _/invoice_ විධානය භාවිතා කරන්න. Sats.Mobi, Bitcoin හි කුඩාම ඒකකය වන Satoshi තුළ පමණක් ක්‍රියාත්මක වේ; එබැවින්, Invoice නිර්මාණය කිරීමට, Sats හි මුදල පණිවිඩ තීරුවේ ලිවිය යුතු අතර එය බොට් සමඟ ඇති කතාබස් තුළ යැවිය යුතුය.

![image](assets/it/08.webp)


ඊළඟ උදාහරණයේ, 210 Sats ක ප්‍රමාණයක් ලබා ගැනීමට තීරණය කරන ලදී.


![cover](assets/it/09.webp)


Nekaj trenutkov po čakanju, da se Invoice pripravi, je na voljo kot besedilo in kot QR koda. Po plačilu Invoice, Wallet pokaže stanje. Če iz nekega razloga skupni znesek ni posodobljen, napišite _/balance_ in pritisnite tipko `enter`.


![image](assets/it/10.webp)


## Sats යවමින්


Sats izjemno dragocena sredstva, od katerih se ne bi smeli zlahka ločiti, vendar Sats.Mobi naredi to privlačno, saj izvajanje nekaj kratkih testov (tj. nekaj poskusnih transakcij) ne bo problem.


### Invoice ගෙවීමක්


Invoice ගෙවීම සඳහා සරලම ක්‍රමය වන්නේ පණිවිඩ පේළියට `lnbc1xxxxx` පණිවිඩ පේළිය පිටපත් කර _/pay_ විධානය ටයිප් කිරීමෙන් පසු එය අලවීමයි. **නිවැරදි ව්‍යാകරණය** සඳහා විධානයෙන් පසු ඉඩක් තැබීම අවශ්‍ය වේ.


![image](assets/it/11.webp)


Wallet තහවුරු කිරීමක් ඉල්ලා පණිවිඩයක් යවයි. _Pay_ මත ක්ලික් කිරීමෙන් Invoice ගෙවීම් සිදු වේ.


![image](assets/it/12.webp)


Sats.Mobi lahko računa na učinkovit in dobro povezan Lightning vozlišče, plačila redko ne uspejo, ker vedno uspe najti pravilno usmerjanje.


### ජංගම දුරකථනයෙන් සුවපහසු ලෙස ගෙවීම


ටෙලිග්‍රෑම් මත බ්‍රවුසිං කිරීමේදී, Sats.Mobi ජංගම දුරකථනයේද ලබා ගත හැක. ජංගම දුරකථනයෙන් ගෙවීම් කිරීම සඳහා ඇති වඩාත් පහසු ක්‍රියාවලිය QR කේතයක් ස්කෑන් කිරීමයි, නමුත් මෙම Wallet එය නිර්මාණය අනුව නොමැත, එය ස්වයංපෝෂිත යෙදුමක් නොව සමාජ ජාලයක අඩංගු බැවින්. Sats.Mobi එබැවින් ජංගම අත්දැකීම හැකි ඉක්මනින් පහසු කිරීමට වැඩසටහන්ගත කර ඇත: එය ඇත්ත වශයෙන්ම ඔබ ගෙවීමට අවශ්‍ය Invoice හි QR කේතයෙහි ඡායාරූපයක් ලෙස ගත් රූපයක් විකේතනය කළ හැක.


සිතන්න, උදාහරණයක් ලෙස, ඔබට Invoice 50 Satsක් ගෙවීමට අවශ්‍ය වේ.


![image](assets/it/20.webp)


කළාපය අපට පෙන්වූ විට, අපට සම්බන්ධ QR කේතයෙහි ඡායාරූපයක් ගත හැක.


![image](assets/it/21.webp)


Nato odpremo Telegram na mobilnem telefonu in v klepetu z Sats.Mobi priložimo pravkar posneto fotografijo QR kode.


![cover](assets/it/22.webp)


එකක් තෝරාගත් පසු, අපි එය බොට්ට යවමු:


![image](assets/it/23.webp)

Sats.Mobi ඡායාරූපය විකේතනය කර **කඩිනමින් ගෙවීම් ඉල්ලීම ඉදිරිපත් කරයි**, නිවැරදි විස්තරය සමඟ. කතාබස් තහවුරු කිරීම ඉල්ලා සිටී, ඉදිරියට යාමට ඔබ _/pay_ ඔබා යුතුය.

![image](assets/it/24.webp)


කරුණාකර ගෙවීම සම්පූර්ණ වීමට මොහොතක් රැඳී සිටින්න.


![image](assets/it/25.webp)


Invoice සඳහා 50 Sats ගෙවා ඇත, කැමරාව සහ එහි ඒකාබද්ධ ස්කෑනින් ක්‍රියාකාරිත්වය භාවිතා නොකරමින් ලබාගත් ප්‍රතිඵලයකි.


### Sats.Mobi ටෙලිග්‍රෑම් කණ්ඩායම්වලදී


![image](assets/it/27.webp)


LNTipBot ප්‍රසිද්ධ කළ විශේෂාංග අතර Sats.Mobi Telegram වෙත ගෙන එන්නේ, කණ්ඩායමක සාමාජිකයින් සඳහා අත්දැකීම විනෝදජනක සහ අන්තර්ක්‍රියාත්මක කරන එකකි.

මालिकहरूले බොට්ටා සමූහ කතාබස්ට එක්වීමට ආරාධනා කළ හැකි අතර පසුව Sats.Mobi පරිපාලක ලෙස නිර්දේශ කළ හැකිය. එම මොහොතේ සිට, විනෝදය ආරම්භ වේ, මන්ද සමූහයට ඔවුන්ගේ දායකත්වය සඳහා සාමාජිකයින්ට අනෙකුත් පරිශීලකයින්ට සම්මාන ලබා දිය හැකිය.


- _/tip_ sporočilu doda napotek z odgovorom;
- _/send_ යවන ලද්දේ LN Address හෝ Telegram හසුරුවක් ලාභියා ලෙස සදහන් කරමින්;
- _/faucet_ (in the _/advanced_ menu) omogoča ustvarjanje serije napitnin, ki jih lahko najhitrejši člani skupine zberejo s klikom na _/collect_;
- _/tipjar_ (in the _/advanced_ menu) creates another type of distribution that can be sent to users in the group.


यी प्रत्येक आदेशहरूको आफ्नै वाक्यविन्यास छ, जुन मुख्य आदेश मेनुमा व्याख्या गरिएको छ।


In če nismo lastnik skupine? Ni problema: samo prosite ustanovitelja, da povabi Sats.Mobi, ga doda kot skrbnika skupine, in vse je pripravljeno!


## විකුණුම් ස්ථානය (POS)


කළමනාකරණය Sats.Mobi පළමු වරට ආරම්භ කරන විට, බොට් එක භාවිතා කරන්නාට වෙනත් විශේෂාංගයක්ද නිර්මාණය කරයි: **POS**. "උපාංගය" භාවිතා කරන්නා විසින් _/pos_ විධානයෙන් හෝ පහළ දකුණු කෙළවරේ ඇති පාලකයෙහි සම්බන්ධ බොත්තම ක්ලික් කිරීමෙන් සක්‍රීය කරයි. ඇත්ත වශයෙන්ම, POS යනු වෙබ් යෙදුමක් වන අතර, එය Telegram කතාබස් මත පෝප්-අප් එකක් ලෙස විවෘත වේ.


![image](assets/it/14.webp)


Interface භාවිතා කරන්නාගේ පුද්ගලික ටෙලිග්‍රෑම් හෑන්ඩලය ඉහළ වමෙන් පෙන්වයි සහ සියලුම POS භාවිතා කරන ආකාරයටම සරලව භාවිතා කරයි: යතුරු පුවරුවේ මුදල ටයිප් කිරීමෙන්. දැන් අපි සේවාවක් සඳහා යුරෝ සෙන්ට් 21 ක් එකතු කිරීමට අවශ්‍ය බව සිතමු. Sats.Mobi ස්වභාවිකව Sats පමණක් කළමනාකරණය කරන බව දැනගෙන, ඔබේ හිස තුළ පරිවර්තනය කිරීම පහසු නැත. එයට විරුද්ධව, POS එකක ගිණුම් ඒකකය ලෙස යුරෝ පෙන්වයි, ඒ සමගම Satoshi හි සමාන මුදල පෙන්වයි.


![image](assets/it/15.webp)

_/OK_ මත ක්ලික් කිරීමෙන් QR කේතයක් හරහා පාරිභෝගිකයාට පෙන්විය හැකි හෝ තත්ක්ෂණික පණිවිඩ මඟින් සටහනක් ලෙස යැවිය හැකි Invoice පෙන්වයි, එවිට එය ගෙවිය හැක.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


ස්වභාවිකවම, POS දුරකථන මත ද ලබා ගත හැකි අතර, පෙර දැක්වූ ආකාරයටම ප්‍රවේශ විය හැක.


![image](assets/it/18.webp)


එය ජංගම දුරකථන තිරය මතද හොඳින් පෙන්වා ඇත:


![image](assets/it/19.webp)


## අමතර විශේෂාංග


Sats.Mobi Wallet-এর অফারটি সম্পূর্ণ করার জন্য আরও অন্যান্য বৈশিষ্ট্য রয়েছে, যা আমরা দেখেছি, Wallet-এর ধারণাটিকে পেমেন্ট গ্রহণ এবং পাঠানোর কার্যক্রমের বাইরে প্রসারিত করে:


- _/nostr_: Wallet සම්බන්ධ කිරීමට ඔබේම Nostr පරිශීලකයාට zaps ලබා ගැනීමට;
- _/cashback_: වෙළඳාමකදී මිලදී ගැනීමක් සඳහා මුදල් ආපසු ලබා ගැනීමට වෙළෙන්දාට ඉදිරිපත් කළ හැකි කේතයක් පෙන්වයි;
- _/buy_: začne voden postopek znotraj bota, ki omogoča nakup Sats za evre;
- _/activatecard_: NFC ඩෙබිට් කාඩ්පතක් සක්‍රීය කිරීම සඳහා ඉල්ලීමක් කිරීමට, Sats.Mobi Wallet හරහා නැවත ආරෝපණය කළ හැකි අතර එය සඳහා දැනුම්දීම් සක්‍රීය කළ හැක;
- _/link_: ඔබේම Zeus හෝ Blue Wallet සඳහා සබැඳියක් නිර්මාණය කරයි, එය මෙම Wallet සඳහා දුරස්ථ පාලක ලෙස භාවිතා කළ හැක.


## Sklep

Sats.Mobi යනු භාවිතා කිරීමට සතුටුදායක සහ විනෝදජනක Wallet එකක් වන අතර, LNBits හි වඩාත් උසස් ක්‍රියාකාරකම් භාවිතා කරමින් LNTipBot සමඟ ඇති වූ අත්දැකීම් නැවත ලබා දේ. කෙසේ වෙතත්, **එය භාරකාර සේවාවක් බව මතක තබා ගැනීම වැදගත්ය**. එබැවින්, ඉතා සුළු Sats පමණක් තබා ගැනීමට එය භාවිතා කළ යුතු අතර, ඔබේ Lightning Network මුදල් සඳහා ප්‍රධාන Wallet එකක් නොවේ. එමෙන්ම, 500,000 Sats ට සමාන අභ්‍යන්තර ධාරිතා සීමාවක් ඇත, එම සීමාව ඉක්මවා නොයෑමට උපදෙස් දෙනු ලැබේ.


Če iščete ne-hrambene denarnice Lightning Network, je vsekakor priporočljivo pogledati druge izdelke.


---
### ප්‍රලේඛනය


- [Github](https://github.com/massmux/SatsMobiBot)
- [ভিডিওগুলির](https://www.youtube.com/results?search_query=Sats.mobi) ডেমোর প্লেলিস্ট