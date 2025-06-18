---
name: seed Signer

description: ඔබේ seed අත්සනකරු පිහිටුවීම
---

![cover](assets/cover.webp)


## පද්ධතිය:


**Raspberry Pi Zero (verzija 1.3)**


Za popolnoma zračno ločeno rešitev poskrbite, da uporabite različico 1.3 brez WiFi ali Bluetooth zmogljivosti, vendar bo deloval kateri koli model Raspberry Pi 2/3/4 ali Zero.


සටහන: Raspberry Pi සාමාන්‍යයෙන් පිහියන් සවි කර නොමැතිව පැමිණේ; පිහියන් සවිකිරීම සඳහා එය සෝඩරින් කළ යුතුය, නැතහොත් "GPIO Hammer" නම් කරන ලද දෙයක් භාවිතා කළ හැක.

GPIO Hammer


Če vaše spajkanje ni povsem na ravni, ali pa še nimate spajkalnika, lahko namesto spajkanja uporabite "GPIO Hammer".


**LCD WaveShare 1,3 අඟල් තිරය 240 × 240 පික්සල්**


WaveShare LCD Hat 1.3″ 240×240 pxl LCD


**සටහන:** Waveshare තිරය සූක්ෂමව තෝරන්න; 240×240 පික්සල් විභජනයක් ඇති ආකෘතිය මිලදී ගැනීමට විශ්වාසවන්ත වන්න.


**Pi Zero සමඟ අනුකූල කැමරා මොඩියුලය**


Raspberry Pi Camera Aokin/AuviPal 5MP 1080p with OV5647 Sensor Video Camera Module; OV5647 සෙන්සර් මොඩියුලය සහිත අනෙකුත් වෙළඳ නාම ද ක්‍රියාත්මක විය හැක, නමුත් Orange Pill ආවරණය සමඟ අනුකූල නොවිය හැක.


**සටහන:** ඔබට විශේෂයෙන් Raspberry Pi Zero සඳහා අනුකූල කැමරා රිබන් කේබලයක් අවශ්‍ය වේ.


**MicroSD කාඩ්පතක් අවම වශයෙන් 4 GB ධාරිතාවක් සහිත**


විශාල සම්පත්: https://seedsigner.com/explainers/


## මෙමෘදුකාංග:


සොෆ්ට්වෙයා ස්ථාපනය


1. "seedsigner_x_x_x.img.zip" නවතම ගොනුව බාගන්න

නවතම නිකුතුව

2. "seedsigner_x_x_x.img.zip" ගොනුව අන්සීල් කරන්න

3. Balena Etcher හෝ සමාන මෙවලමක් භාවිතා කරමින් අනුසන්ධිත .img රූප ගොනුව microsd කාඩ්පතට ලිවියන්න.

BALENA ETCHER

4. SeedSigner හි microsd කාඩ්පත ස්ථාපනය කරන්න.

SeedSigner GPG Public Key

seedsigner_pubkey.gpg


## උපදේශක වීඩියෝව


_මාර්ගෝපදේශය Southerbitcoiner වෙතින් ගත්, Cole විසින් නිර්මාණය කරන ලදි_


### SeedSigner: විවෘත මූලාශ්‍ර, ස්වයංක්‍රීය Hardware Wallet/අත්සන කිරීමේ උපාංගය ආවරණය කරන වීඩියෝ මාර්ගෝපදේශ එකතුවක්


![image](assets/1.webp)


SeedSigner යනු ඔබට මුල සිටම ගොඩනගා ගත හැකි Bitcoin අත්සන කිරීමේ උපාංගයකි. අපහසු ලෙස ඇසෙන නමුත්, මෙම කොටස් 4ක මාලාව ඔබට උපකාරී වනු ඇත :) මම ඔබට කොටස 1 සහ 2 බලන්න යෝජනා කරමි, එවිට ඔබට ඩෙස්ක්ටොප් (කොටස 3 බලන්න) හෝ ජංගම උපාංගයක් (කොටස 4 බලන්න) භාවිතා කිරීමට අවශ්‍යද යන්න තීරණය කළ හැක.


ඔබට අවශ්‍ය සියලුම දේ පහත දැක්වේ. වෙනත් ප්‍රයෝජනවත් සබැඳි වලට SeedSigner වෙබ් අඩවිය, ඔවුන්ගේ Github, ඔවුන්ගේ Keybase, නවතම නිකුතුව, සහ දෘඩාංග අවශ්‍යතා ඇතුළත් වේ.


### 1. Kako zgraditi SeedSigner:


V tem videu vam pokažem, kako prenesti in preveriti programsko opremo SeedSigner, kateri deli so potrebni in kako sestaviti vaš SeedSigner.


![video](https://youtu.be/mGmNKYOXtxY)


### භාගය 2: ඔබේ SeedSigner පරීක්ෂා කිරීම


Preden sem uporabil svoj SeedSigner, sem opravil nekaj testov, da se prepričam, da ne počne nič zlonamernega. Mislil sem, da bom delil tudi ta korak. Tukaj je, kako preveriti, da vaš SeedSigner izvozi pravilen Wallet (xpub), kako preveriti matematiko metov kock SeedSignerja in kako preveriti bip-85 otroška semena SeedSignerja.


![video](https://youtu.be/34W1IyTyXZE)


### භාගය 3: SeedSigner Sparrow Wallet (ඩෙස්ක්ටොප්) සමඟ භාවිතා කරන ආකාරය


SeedSigner සීඩ් ජනනය කිරීමට සහ Bitcoin ගනුදෙනු වලට අත්සන් කිරීමට හැකි වේ. නමුත් එය ස්වයංක්‍රීයව ගනුදෙනු ගොඩනැගීමට හැකි නොවේ. ඔබේ SeedSigner සමඟ Wallet "සංවිධායකයෙකු" භාවිතා කළ යුතුය. මෙන්න ඔබේ SeedSigner සමඟ Sparrow Wallet භාවිතා කරන ආකාරය:


![video](https://youtu.be/IQb8dh-VTOg)


භාගය 4: SeedSigner Blue Wallet (ජංගම) සමඟ භාවිතා කරන ආකාරය


SeedSigner සීඩ් ජනනය කිරීමට සහ Bitcoin ගනුදෙනු වලට අත්සන් කිරීමට හැකි වේ. නමුත් එය තනිව ගනුදෙනු නිර්මාණය කිරීමට හැකි නොවේ. ඔබේ SeedSigner සමඟ Wallet "සංවිධායකයෙකු" භාවිතා කළ යුතුය. මෙන්න ඔබේ SeedSigner සමඟ Blue Wallet භාවිතා කරන ආකාරය:


![video](https://youtu.be/x0Ee35Ct0r4)


To so vsi vodniki SeedSigner, za zdaj! Sporočite mi, če menite, da kaj manjka. To so na mojem seznamu za potencialne videoposnetke:



- SeedSigner celoten pregled. Ali je to dobra izbira za napravo za podpisovanje? Prednosti/slabosti?
- Bip-85 සමඟ SeedSigner භාවිතා කරන ආකාරය
- SeedSigner සමඟ Jim මාමා වීමට කෙසේද?


මෙම වටිනාකම් සොයා ගත්තාද? අනාගත වීඩියෝ සඳහා අරමුදල් ලබා දීමට උපකාරී වීමට ඉඟියක් යැවීමට සලකා බලන්න:

https://www.southernbitcoiner.com/donate/