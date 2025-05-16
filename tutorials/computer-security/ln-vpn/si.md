---
name: LN VPN

description: ඔබේ VPN සකසන්න
---

![image](assets/cover.webp)


LN VPN යනු අභිරුචිකරණය කළ හැකි VPN සේවාවක් වන අතර එය මිනිත්තු ගෙවීම් පමණක් පිළිගනී. අද, මම ඔබට එය භාවිතා කරන ආකාරය සහ අන්තර්ජාලය සෙවීමේදී අඩු සලකුණු තැබීමේ ආකාරය පෙන්වන්නෙමි.


තවදුරටත් ගුණාත්මක VPN සේවා සපයන්නන් බොහෝමයි, සහ අපි මෙම ලිපියෙහි (hyperlink) සවිස්තර විමර්ශනයක් සිදු කර ඇත. කෙසේ වෙතත්, LN VPN විශේෂත්වයෙන් පෙනී යයි, සහ අපට එය ඔබට හඳුන්වා දීමේ අවස්ථාව මග හැරිය නොහැකි විය.


බොහෝ VPN සේවා සපයන්නන්, ProtonVPN සහ Mullvad වැනි, බිට්කොයින් සමඟ ගෙවීම් කිරීමේ විකල්පය ලබා දෙන නමුත් ගිණුමක් තනන්නා සහ දිගු හෝ කෙටි කාලයක් සඳහා සැලැස්මක් මිලදී ගැනීම අවශ්‍ය වේ, එය සෑම කෙනෙකුගේම අයවැයට ගැලපෙන්නේ නැති විය හැක.


LN VPN omogoča uporabo VPN po potrebi za čas, krajši od ene ure, zahvaljujoč implementaciji plačil Bitcoin prek Lightning Network. Takojšnja in anonimna, lightning plačila odpirajo svet možnosti za mikroplačila.


සටහන💡: **මෙම මාර්ගෝපදේශය LN VPN භාවිතා කරන ආකාරය විස්තර කරයි Linux Ubuntu 22.04 LTS පද්ධතියකින්.**


## අවශ්‍යතා: Wireguard


සරල වචන වලින්, Wireguard භාවිතා කරන්නේ ඔබේ පරිගණකය සහ දුරස්ථ සේවාදායකය අතර ආරක්ෂිත මාර්ගයක් නිර්මාණය කිරීමටයි, එමඟින් ඔබ අන්තර්ජාලය බ්‍රව්ස් කරනු ඇත. මෙම මාර්ගෝපදේශය අනුගමනය කිරීමෙන් ඔබ Contract වන කාලය තුළ ඔබේ ලෙස පෙනෙනුයේ මෙම සේවාදායකයේ IP Address වේ.


Wireguard නිල ස්ථාපන මාර්ගෝපදේශය: https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## අවශ්‍යතා: Lightning Bitcoin Wallet


Če še nimate Lightning Bitcoin Wallet, brez skrbi, tukaj smo za vas pripravili zelo preprost vodnik. (oddelek z navodili LN vam lahko pomaga)


## 1. korak: Contract a najem


https://lnvpn.com වෙත ගොස්, VPN මාර්ගයේ පිටවීමේ IP හි රට සහ කාලසීමාව තෝරා ගත යුතුය. මෙම පරාමිතීන් සකස් කිරීමෙන් පසු, Pay with lightning මත ක්ලික් කරන්න.


![image](assets/1.webp)


Invoice විදුලි කුණ්ඩලියක් ප්‍රදර්ශනය කරනු ඇත, සහ ඔබට අවශ්‍ය වන්නේ ඔබේ Wallet විදුලි කුණ්ඩලියෙන් එය ස්කෑන් කිරීම පමණි.


Ko Invoice එක ගෙවී ගිය පසු, ඔබට ඔබේ Wireguard වින්‍යාස සැකසුම් ජනනය වීමට තත්පර කිහිපයක් සිට විනාඩි දෙකක් දක්වා රැඳී සිටිය යුතුය. එය ටිකක් වැඩි කාලයක් ගත වුවහොත්, බිය නොවන්න, අපි මෙම ක්‍රියාවලිය දස දහස් වරක් සිදු කර ඇති අතර, සමහර විට එය ටිකක් වැඩි කාලයක් ගත වේ.

Naslednje besedilo je bilo prevedeno v angleščino, pri čemer je bila ohranjena enaka postavitev markdown kot v izvirnem besedilu:


මීළඟ තිරය පෙනී යනු ඇති අතර ඔබට "ගොනුවක් ලෙස බාගන්න" මත ක්ලික් කිරීමෙන් ඔබේ වින්‍යාස ගොනුව ලබා ගත හැක, එය lnvpn-xx-xx.conf වැනි නමක් ඇති වන අතර "xx" වර්තමාන දිනයට අදාළ වේ.

![image](assets/2.webp)


## චරණය 2: සංග්‍රහය සක්‍රීය කරන්න


Najprej boste morali preimenovati konfiguracijsko datoteko, pridobljeno v prejšnjem koraku, da jo bo Wireguard lahko samodejno prepoznal.


ඔබේ බාගත කිරීම් ෆෝල්ඩරයට යන්න, ටර්මිනල් කවුළුවක හෝ ගොනු විමසුම්කාරකය සමඟ, සහ lnvpn-xx-xx.conf ගොනුව wg0.conf ලෙස මෙහෙම නැවත නම් කරන්න:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


ඔන්න! සංග්‍රහය සක්‍රීයයි!


## පියවර 3: සත්‍යාපනය කරන්න


Uporabite spletno storitev, kot je whatismyip, da preverite, ali je vaš javni IP Address zdaj tisti iz VPN-ja, ki ste ga pravkar aktivirali.


## චරියාව 4: අක්‍රිය කරන්න


ඔබගේ කුලී ගිවිසුම කල් ඉකුත් වූ විට, අන්තර්ජාලයට ප්‍රවේශය නැවත ලබා ගැනීමට සම්බන්ධතාවය අක්‍රීය කළ යුතුය. ඔබට LN VPN සමඟ කුලී ගිවිසුමක් ස්ථාපිත කිරීමට අවශ්‍ය ඕනෑම වේලාවක පියවර 1 සිට 3 දක්වා නැවත කිරීමට හැකිය.


ටැනල් අක්‍රිය කරන්න:


```
$ sudo ip link delete dev wg0
```


ඔබට එය ඇත! දැන් ඔබ LN VPN, අනන්‍ය VPN සේවාවක් භාවිතා කරන ආකාරය දන්නවා!