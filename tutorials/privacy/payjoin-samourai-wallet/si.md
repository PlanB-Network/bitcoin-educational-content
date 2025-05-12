---
name: PayJoin - Samourai Wallet
description: Kako izvesti PayJoin transakcijo na Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)


***අවධානය:** Samourai Wallet හි ආරම්භකයින් අත්අඩංගුවට ගත් පසු සහ ඔවුන්ගේ සේවාදායකයන් අප්‍රේල් 24 වන දින අත්පත් කර ගැනීමෙන් පසු, Samourai Wallet හි Payjoins Stowaway කාර්යය, සම්බන්ධ පාර්ශවයන් අතර PSBT අතින් හුවමාරු කිරීමෙන් පමණක් ක්‍රියාත්මක වේ, එම පරිශීලකයින් දෙදෙනාම ඔවුන්ගේම Dojo වෙත සම්බන්ධ වී සිටින පසුතැවෙනි. Sparrow සඳහා, BIP78 හරහා Payjoins තවමත් ක්‍රියාත්මක වේ. කෙසේ වෙතත්, මෙම මෙවලම් ඉදිරි සති කිහිපය තුළ නැවත ආරම්භ විය හැක. මේ අතර, Stowaway හි සෞද්ධාන්තික ක්‍රියාකාරිත්වය තේරුම් ගැනීමට ඔබට තවමත් මෙම ලිපිය කියවිය හැක.*


_Če nameravate Stowaway izvesti ročno, je postopek zelo podoben tistemu, opisanemu v tem priročniku. Glavna razlika je v izbiri vrste transakcije Stowaway: namesto da izberete `Online`, kliknite na `In Person / Manual`. Nato boste morali ročno Exchange PSBT-je, da sestavite transakcijo Stowaway. Če ste fizično blizu svojega sodelavca, lahko zaporedno skenirate QR kode. Če ste na daljavo, lahko JSON datoteke izmenjate prek varnega komunikacijskega kanala. Ostali del priročnika ostaja nespremenjen._


_අපි මෙම නඩුවේ සංවර්ධන මෙන්ම සම්බන්ධිත මෙවලම් සම්බන්ධයෙන් ඇතිවන සංවර්ධන ආසන්නයෙන් අනුගමනය කරමින් සිටිමු. නව තොරතුරු ලබා ගත හැකි වන්නේ නම් මෙම උපකාරකය යාවත්කාලීන කරන බවට විශ්වාස කරන්න._


_මෙම උපකාරිකාව අධ්‍යාපනික සහ තොරතුරුමය අරමුණු සඳහා පමණක් සපයනු ලැබේ. අපි මෙම මෙවලම් අපරාධමය අරමුණු සඳහා භාවිතා කිරීම අනුමත නොකරන අතර හුරුවන්නෙමු. තමන්ගේ බල ප්‍රදේශයේ නීති පිළිපැදීම සෑම පරිශීලකයෙකුගේම වගකීමකි._


---

> *Blockchain හරහා හෙළිදරව්වන් සියල්ල නැවත සලකා බැලීමට බල කරන්න.*

PayJoin යනු ගෙවීම් ලැබුම්කරු සමඟ සහයෝගයෙන් වියදමක් දියත් කිරීමේදී පරිශීලක පෞද්ගලිකත්වය වැඩි දියුණු කරන විශේෂ Bitcoin ගනුදෙනු ව්‍යුහයකි. PayJoin සකස් කිරීම සහ ස්වයංක්‍රීය කිරීම පහසු කරන ක්‍රියාත්මක කිරීම් කිහිපයක් ඇත. මෙම ක්‍රියාත්මක කිරීම් අතර, සමුරයි Wallet හි කණ්ඩායම් විසින් සංවර්ධනය කරන ලද Stowaway යනු හොඳින් දන්නා එකකි. මෙම උපකාරකය සමුරයි Wallet යෙදුම භාවිතා කර Stowaway PayJoin ගනුදෙනුවක් කෙසේ සිදු කරන බව විස්තර කරයි.


## Stowaway කෙසේ ක්‍රියා කරයිද?


Kot je bilo omenjeno prej, Samourai Wallet ponuja orodje PayJoin z imenom "Stowaway." Dostopno je prek programske opreme Sparrow Wallet na PC-ju ali aplikacije Samourai Wallet na Androidu. Za izvedbo PayJoin mora prejemnik, ki prav tako deluje kot sodelavec, uporabiti programsko opremo, združljivo s Stowaway, in sicer Sparrow ali Samourai. Ti dve programski opremi sta interoperabilni, kar omogoča transakcijo Stowaway med Sparrow Wallet in Samourai Wallet ter obratno.


Stowaway "Cahoots" ලෙස Samourai හඳුන්වන ගනුදෙනු ප්‍රවර්ගයකට මඟ බලයි. Cahoot යනු මූලිකවම බහු පරිශීලකයින් අතර සහයෝගී ගනුදෙනුවක් වන අතර, off-chain තොරතුරු Exchange අවශ්‍ය වේ. අද දක්වා, Samourai Cahoots මෙවලම් දෙකක් ලබා දේ: Stowaway (Payjoins) සහ StonewallX2 (අපි අනාගත ලිපියකදී විමසා බලමු).


Cahoots ගනුදෙනු යනු පරිශීලකයින් අතර අර්ධව අත්සන් කළ ගනුදෙනු හුවමාරු කිරීමයි. මෙම ක්‍රියාවලිය දිගු සහ අපහසු විය හැකි අතර, විශේෂයෙන් දුරස්ථව සිදු කරන විට. කෙසේ වෙතත්, එය තවමත් වෙනත් පරිශීලකයෙකු සමඟ අතින් සිදු කළ හැකි අතර, සහකාරීන් භෞතිකව ආසන්නව සිටින විට පහසු වේ. ප්‍රයෝගිකව, මෙය අනුපිළිවෙලින් ස්කෑන් කිරීමට QR කේත පහක් අතින් හුවමාරු කිරීම සම්බන්ධ වේ.


දුරස්ථව සිදු කරන විට, මෙම ක්‍රියාවලිය අතිශය සංකීර්ණ වේ. මෙම ගැටලුව Address කිරීමට, Samourai විසින් "Soroban" නම් Tor මත පදනම් වූ සංකේතගත සන්නිවේදන ප්‍රොටෝකෝලයක් සංවර්ධනය කර ඇත. Soroban සමඟ, PayJoin සඳහා අවශ්‍ය හුවමාරු පරිශීලක හිතකාමී Interface පිටුපස ස්වයංක්‍රීය වේ. මෙම ලිපියේ අපි අධ්‍යයනය කරන දෙවන ක්‍රමය මෙය වේ.


මෙම සංකේතනය කළ හුවමාරු සඳහා Cahoots සහභාගීවන්නන් අතර සම්බන්ධතාවයක් සහ සත්‍යාපනයක් ස්ථාපිත කිරීම අවශ්‍ය වේ. එබැවින් Soroban සන්නිවේදන පරිශීලකයින්ගේ Paynyms මත පදනම්ව ඇත. ඔබ Paynyms පිළිබඳව හුරු නැති නම්, වැඩි විස්තර සඳහා මෙම ලිපිය අධ්‍යයනය කිරීමට මම ඔබට ආරාධනා කරමි: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)



සරලව කියනවා නම්, Paynym යනු ඔබේ Wallet සමඟ සම්බන්ධ වූ අනන්‍ය හඳුනාගැනීමකි, එය සංකේතනය කළ පණිවිඩ යැවීම ඇතුළු විවිධ ක්‍රියාකාරකම් සඳහා ඉඩ සලසයි. Paynym එක හඳුනාගැනීමක් සහ රොබෝවක් නිරූපණය කරන චිත්‍රයක් ලෙස ඉදිරිපත් කරයි. මෙන්න Testnet හි මගේ උදාහරණයක්: ![paynym samourai Wallet](assets/en/1.webp)


**සාරාංශය:**


- _Payjoin_ = සහකාරී ගනුදෙනු වල විශේෂිත ව්‍යුහය;
- _Stowaway_ = PayJoin ක්‍රියාත්මක කිරීම Samourai සහ Sparrow Wallet හි ලබා ගත හැක;
- _Cahoots_ = Samourai විසින් සියලුම ඔවුන්ගේ සහයෝගී ගනුදෙනු සඳහා දී ඇති නම, PayJoin Stowaway ඇතුළුව;
- _Soroban_ = Tor මත ස්ථාපිත කේතනය කළ සන්නිවේදන ප්‍රොටෝකෝලයක් වන අතර, Cahoots ගනුදෙනුවක සන්දර්භයෙන් අනෙකුත් පරිශීලකයින් සමඟ සහයෝගය ලබා දේ;
- _Paynym_ = Wallet का एक अद्वितीय पहचानकर्ता जो सोरोबान पर किसी अन्य उपयोगकर्ता के साथ संचार की अनुमति देता है, ताकि एक Cahoots लेनदेन किया जा सके।


[**-> PayJoin ගනුදෙනු සහ ඒවායේ ප්‍රයෝජන ගැන වැඩිදුර ඉගෙන ගන්න**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Paynyms අතර සම්බන්ධතාවයක් ස්ථාපිත කිරීම කෙසේද?


සමූහය මඟින් විශේෂයෙන් PayJoin (Stowaway) දුරස්ථ Cahoots ගනුදෙනුවක් සිදු කිරීමට, ඔබට සහයෝගයෙන් කටයුතු කිරීමට අදහස් කරන පරිශීලකයා "අනුගමනය" කිරීම අවශ්‍ය වේ, ඔවුන්ගේ Paynym භාවිතා කරමින්. Stowaway කේස් එකකදී, මෙය ඔබට බිට්කොයින් යැවීමට අවශ්‍ය පුද්ගලයා අනුගමනය කිරීමයි.


**මෙම සම්බන්ධතාවය ස්ථාපිත කිරීම සඳහා ක්‍රමවේදය මෙන්න:**


ආරම්භ කිරීමට, ඔබට PayJoin සඳහා ලාභගාමියාගේ Paynym ගෙවීම් කේතය ලබා ගත යුතුය. Samourai Wallet යෙදුම තුළ, ලාභගාමියා ඔවුන්ගේ Paynym (කුඩා රොබෝව) අයිකනය තිරයේ ඉහළ වම් පැත්තේ පිහිටා ඇති තැපෑල මත ටැප් කළ යුතු අතර, පසුව `+...` සමඟ ආරම්භ වන ඔවුන්ගේ Paynym නාමය මත ක්ලික් කළ යුතුය. උදාහරණයක් ලෙස, මගේ එක `+namelessmode0aF` වේ. ඔබේ සහකරු Sparrow Wallet භාවිතා කරන්නේ නම්, මෙතැන ක්ලික් කිරීමෙන් අපගේ කැපවූ උපකාරකය අනුගමනය කිරීමට මම ඔබට ආරාධනා කරමි.


![connexion paynym samourai](assets/notext/2.webp)


ඔබේ සහකරු ඔවුන්ගේ Paynym පිටුවට යළි යොමු කෙරේ. එතනින්, ඔවුන්ට ඔවුන්ගේ Paynym අක්තපත්‍ර ඔබ සමඟ හුවමාරු කිරීමට හෝ ඔබට ස්කෑන් කිරීමට ඔවුන්ගේ QR කේතය හුවමාරු කිරීමට හැකිය. මෙය කිරීමට, ඔවුන්ට ඔවුන්ගේ තිරයේ ඉහළ දකුණු කෙළවරේ පිහිටි කුඩා "share" අයිකනය ක්ලික් කළ යුතුය.

![partager paynym samourai](assets/en/1.webp)


ඔබගේ පැත්තෙන්, ඔබේ Samourai Wallet යෙදුම ආරම්භ කර "PayNyms" මෙනුවට එම ආකාරයෙන් පිවිසෙන්න. මෙය ඔබේ Paynym පළමු වරට භාවිතා කිරීම නම්, ඔබට හඳුනාගැනීමේ අංකය ලබා ගැනීමට අවශ්‍ය වේ.


![demander un paynym](assets/notext/3.webp)


පසුව තිරයේ දකුණු පහළ කොනේ ඇති නිල් "+" මත ක්ලික් කරන්න.

![ajouter paynym collaborateur](assets/notext/4.webp)

ඔබට පසුව ඔබේ සහකරුගේ ගෙවීම් කේතය අලවිය හැක `COLLER LE CODE PAIEMENT` තෝරා, හෝ ඔවුන්ගේ QR කේතය ස්කෑන් කිරීමට කැමරාව විවෘත කළ හැක `SCANNEZ LE CODE QR` ඔබා.![paste paynym identifier](assets/notext/5.webp)


S klikom na gumb `SUIVRE`.

![follow paynym](assets/notext/6.webp)

`YES` මත ක්ලික් කිරීමෙන් තහවුරු කරන්න.

![confirm follow paynym](assets/notext/7.webp)

එවිට මෘදුකාංගය ඔබට `SE CONNECTER` බොත්තමක් ලබා දෙනු ඇත. අපගේ උපකාරිකාව සඳහා මෙම බොත්තම ක්ලික් කිරීම අවශ්‍ය නොවේ. මෙම පියවර අපගේ උපකාරිකාවට අදාළ නොවන BIP47 හි කොටසක් ලෙස වෙනත් Paynym වෙත ගෙවීම් කිරීමට ඔබ සැලසුම් කරන්නේ නම් පමණක් අවශ්‍ය වේ.

![connect paynym](assets/notext/8.webp)

සම්ප්‍රාප්තයාගේ Paynym ඔබේ Paynym විසින් අනුගමනය කරන ලද විට, මෙම මෙහෙයුම විරුද්ධ දිශාවෙන් නැවත කරන්න, එවිට සම්ප්‍රාප්තයාද ඔබ අනුගමනය කරයි. එවිට ඔබට PayJoin ක් කළ හැක.


## Kako narediti PayJoin na Samourai Wallet?


ඔබ මෙම පූර්ව කටයුතු සම්පූර්ණ කර ඇති නම්, ඔබ අවසානයේදී PayJoin ගනුදෙනුව සිදු කිරීමට සූදානම්! මෙය කිරීමට, අපගේ වීඩියෝ උපකාරකය අනුගමනය කරන්න:


![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)


**බාහිර සම්පත්:**


- https://docs.samourai.io/en/spend-tools#stowaway.