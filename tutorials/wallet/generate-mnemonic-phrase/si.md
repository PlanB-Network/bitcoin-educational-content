---
name: Mnemonic Phrase - ඩයිස් රෝල්
description: generate කුඹුරුවලින් ඔබේම ප්‍රතිසාධන වාක්‍යය කෙසේද?
---

![cover](assets/cover.webp)


මෙම උපකාරිකාවේ, ඔබට අස්ථානගත වූ Bitcoin Wallet සඳහා සූදානම් වචන මාලාවක් අතින් නිර්මාණය කරන ආකාරය කුසලාන ගැසීම් භාවිතයෙන් ඉගෙන ගත හැකි වේ.


**OPOZORILO:** Generiranje Mnemonic fraze na varen način zahteva, da med njenim ustvarjanjem ne pustite nobene digitalne sledi, kar je skoraj nemogoče. V nasprotnem primeru bi Wallet predstavljal preveliko površino za napad, kar bi znatno povečalo tveganje kraje vaših bitcoinov. **Zato je močno odsvetovano prenašanje sredstev na Wallet, ki je odvisen od obnovitvene fraze, ki ste jo ustvarili sami.** Tudi če sledite temu priročniku do potankosti, obstaja tveganje, da bi bila obnovitvena fraza ogrožena. **Zato tega priročnika ne smete uporabljati za ustvarjanje pravega Wallet.** Uporaba Hardware Wallet za to nalogo je veliko manj tvegana, saj generira frazo brez povezave, in pravi kriptografi so upoštevali uporabo kakovostnih virov entropije.


මෙම උපදෙස් මාලාව අනුගමනය කළ හැක්කේ අත්හදා බැලීමේ අරමුණින් පමණක් කල්පිත Wallet එකක් නිර්මාණය කිරීම සඳහා වන අතර, එය සත්‍ය බිට්කොයින් සමඟ භාවිතා කිරීමේ අරමුණින් නොවේ. කෙසේ වෙතත්, මෙම අත්දැකීම වාසි දෙකක් ලබා දේ:



- Najprej vam omogoča boljše razumevanje mehanizmov na osnovi vašega Bitcoin Wallet;
- දෙවැනිව, එය ඔබට එය කරන්නේ කෙසේද යන්න දැන ගැනීමට හැකි කරවයි. මම කියන්නේ එය එක් දවසක ප්‍රයෝජනවත් වේවි කියලා නෙවෙයි, නමුත් එය විය හැක!


## Mnemonic වාක්‍යය යනු කුමක්ද?


ප්‍රතිසාධන වාක්‍යයක්, සමහර විට "Mnemonic," "seed වාක්‍යය," හෝ "රහස් වාක්‍යය" ලෙසද හැඳින්වෙයි, සාමාන්‍යයෙන් 12 හෝ 24 වචන වලින් සමන්විත අනුක්‍රමයකි, එය අන්තර්ගත වශයෙන් පseudo-අහඹු ලෙස ජනනය කෙරේ. පseudo-අහඹු අනුක්‍රමය සෑම විටම පරීක්ෂා මුදුවකින් සම්පූර්ණ කෙරේ.


Mnemonic වාක්‍යය, විකල්ප passphrase සමඟ, HD (අනුක්‍රමික නියමිත) Wallet සමඟ සම්බන්ධ සියලුම යතුරු නියමිතව ලබා ගැනීමට භාවිතා කරයි. මෙය අර්ථ දක්වන්නේ මෙම වාක්‍යයෙන්, නියමිතව generate කිරීම සහ Bitcoin Wallet හි සියලුම පෞද්ගලික සහ පොදු යතුරු නැවත නිර්මාණය කිරීම, එමඟින්, එයට සම්බන්ධ මුදල් ප්‍රවේශ වීමේ හැකියාව ඇත.

![mnemonic](assets/notext/1.webp)

මෙම වාක්‍යයේ අරමුණ වන්නේ බිට්කොයින් පිටපත් කිරීම සහ ප්‍රතිසාධනය කිරීම සඳහා පහසු ක්‍රමයක් සපයන්නයි. Mnemonic වාක්‍යය ආරක්ෂිත සහ සුරක්ෂිත ස්ථානයක තබා ගැනීම අත්‍යවශ්‍ය වේ, මන්ද මෙම වාක්‍යය අත්පත් කර ගන්නා ඕනෑම කෙනෙකුට Wallet අනුකූල මුදල් වෙත ප්‍රවේශය ලැබෙන බැවිනි. එය සම්භාව්‍ය Wallet සන්දර්භයක භාවිතා කරන විට, සහ විකල්ප passphrase නොමැතිව, එය බොහෝ විට SPOF (Single Point Of Failure) එකක් වේ.

සාමාන්‍යයෙන්, මෙම වාක්‍යය ඔබට ඔබේ Wallet නිර්මාණය කිරීමේදී, මෘදුකාංගය හෝ භාවිතා කරන Hardware Wallet මඟින් සෘජුවම ලබා දේ. කෙසේ වෙතත්, මෙම වාක්‍යය ඔබම generate කිරීමද සම්භවය, එවිට තෝරාගත් සහාය මත ඇතුළත් කර Wallet යතුරු ලබා ගැනීමේ හැකියාව ඇත. මෙම උපකාරක පංතියේදී අපි එය කරන්නේ කෙසේද යන්න ඉගෙන ගනිමු.


## අවශ්‍ය ද්‍රව්‍ය සකස් කිරීම


ඔබේ ප්‍රතිසාධන වාක්‍යය අතින් නිර්මාණය කිරීම සඳහා, ඔබට අවශ්‍ය වේ:



- කඩදාසි පතක්;
- පෑනක් හෝ පෙන්සලක්, සංවිධානය පහසු කිරීම සඳහා විශේෂයෙන් විවිධ වර්ණවලින්;
- කීපයක්ම සීනි, අසමතුලිත සීනික් සම්බන්ධ පක්ෂපාතතාවයේ අවදානම් අවම කිරීම සඳහා;
- [2048 BIP39 වචන ලැයිස්තුව](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) මුද්‍රණය කර ඇත.


ඉන් අනතුරුව, පරිගණකයක් ටර්මිනල් සමඟ භාවිතා කිරීම චෙක්සම් ගණනය කිරීම සඳහා අවශ්‍ය වනු ඇත. මෙය නිසැකවම Mnemonic වාක්‍යය අතින් ජනනය කිරීමෙන් වළකින්නැයි මම උපදෙස් දෙන හේතුවයි. මගේ අදහස අනුව, මෙම උපදෙස්පොතේ සඳහන් සුරක්ෂිතතා මැදිහත්වීම් යටතේ පවා පරිගණකයක මැදිහත්වීම Wallet ක ආරක්ෂාකාරීතාවය සීඝ්‍රයෙන් වැඩි කරයි.


Za eksperimentalni pristop glede "fiktivnega Wallet" je mogoče uporabiti vaš običajni računalnik in njegov terminal. Vendar pa je za bolj rigorozni pristop, ki je namenjen omejevanju tveganj kompromitiranja vaše fraze, idealno uporabiti računalnik, ki ni povezan z internetom (najbolje brez wifi komponente ali RJ45 žične povezave), opremljen z minimalno periferijo (vse naj bo povezano s kablom, da se izognete Bluetoothu), in predvsem, ki deluje na amnezični distribuciji Linuxa, kot je [Tails](https://tails.boum.org/index.fr.html), zagnan iz odstranljivega medija.


![mnemonic](assets/notext/2.webp)


සැබෑ පරිද්දක, ඔබේ වැඩ කටයුතු ස්ථානයේ රහස්‍යභාවය සහතික කිරීම සඳහා, කවුළු බැලීමෙන් දුරස්ව, මිනිසුන්ගේ ගමනාගමනය නොමැති, කැමරා (වෙබ් කැමරා, දුරකථන...) නොමැති ස්ථානයක් තෝරා ගැනීම අත්‍යවශ්‍ය වේ.

Priporočljivo je uporabiti veliko število kock, da se zmanjša vpliv morebitno neuravnotežene kocke na entropijo. Pred uporabo je priporočljivo preveriti kocke: to lahko dosežete tako, da jih preizkusite v posodi s solno nasičeno vodo, kar omogoča, da kocke plavajo. Nato nadaljujte z metanjem vsake kocke približno dvajsetkrat v slani vodi in opazujte rezultate. Če se ena ali dve ploskvi pojavita nesorazmerno v primerjavi z drugimi, podaljšajte test z več meti. Enakomerno porazdeljeni rezultati kažejo, da je kocka zanesljiva. Vendar, če ena ali dve ploskvi redno prevladujeta, je treba te kocke dati na stran, saj bi lahko ogrozile entropijo vaše Mnemonic fraze in posledično varnost vaše Wallet.

වास्तවික තත්ත්වයන්හි, මෙම පරීක්ෂා සිදු කිරීමෙන් පසු, ඔබට අවශ්‍ය එන්ට්‍රොපිය generate කිරීමට සූදානම් විය හැක. මෙම උපකාරිකාවේ කොටසක් ලෙස නිර්මාණය කරන ලද පරීක්ෂණාත්මක කල්පිත Wallet සඳහා, ඔබට ස්වාභාවිකවම මෙම සූදානම් කිරීම් මඟ හැරිය හැක.


## ප්‍රතිසාධන වාක්‍යය පිළිබඳව කිහිපයක් මතක් කිරීමක්


Za začetek bomo pregledali osnove ustvarjanja fraze Mnemonic v skladu z BIP39. Kot je bilo že pojasnjeno, je fraza izpeljana iz psevdo-naključnih informacij določene velikosti, katerim je dodan kontrolni seštevek za zagotovitev njene celovitosti.


මෙම ආරම්භක තොරතුරුයේ ප්‍රමාණය, බොහෝ විට "entropy" ලෙස හැඳින්වෙයි, ඔබ ප්‍රතිසාධන වාක්‍යයේ ලබා ගැනීමට අවශ්‍ය වචන ගණන මගින් තීරණය වේ. සාමාන්‍ය වශයෙන් වඩාත් ප්‍රචලිත ආකෘති වන්නේ 12 සහ 24 වචන වලින් යුත් වාක්‍යයන් වන අතර, ඒවා යුගලව 128 බිට් සහ 256 බිට් වල entropy එකකින් නිර්මාණය වේ. මෙන්න BIP39 අනුව විවිධ entropy ප්‍රමාණ පෙන්වන වගුවක්:


| Phrase (words) | Entropy (bits) | Checksum (bits) | Entropy + Checksum (bits) |
| -------------- | -------------- | --------------- | ------------------------- |
| 12             | 128            | 4               | 132                       |
| 15             | 160            | 5               | 165                       |
| 18             | 192            | 6               | 198                       |
| 21             | 224            | 7               | 231                       |
| 24             | 256            | 8               | 264                       |

ඒ අනුව, එන්ට්‍රොපිය යනු 128 සහ 256 බිට් අතර අහඹු සංඛ්‍යාවකි. මෙම උපකාරිකාවේ, අපි 12-වචන වාක්‍යයක උදාහරණයක් ගනිමු, එහි එන්ට්‍රොපිය 128 බිට් වේ, අර්ථය වන්නේ අපි 128 `0` හෝ `1` අහඹු අනුපිළිවෙලක් generate කරන්නෙමු. මෙය 2 (ද්විතීයික) පදවියේ 128 ඉලක්කම් වලින් සමන්විත සංඛ්‍යාවක් නිරූපණය කරයි.

මෙම එන්ට්‍රොපිය මත පදනම්ව, පරීක්ෂාකේතයක් ජනනය කෙරේ. පරීක්ෂාකේතයක් යනු දත්ත කට්ටලයකින් ගණනය කරන අගයක් වන අතර, එම දත්තය සම්ප්‍රේෂණය හෝ ගබඩා කිරීමේදී එහි අඛණ්ඩතාවය සහ වලංගුභාවය තහවුරු කිරීමට භාවිතා කෙරේ. පරීක්ෂාකේත අල්ගොරිතම දත්තයේ අහඹු දෝෂ හෝ වෙනස්කම් හඳුනා ගැනීමට නිර්මාණය කර ඇත.

Mnemonic වාක්‍යයේ අවස්ථාවේදී, checksum එකේ කාර්යය වන්නේ Wallet මෘදුකාංගයකට වාක්‍යය ඇතුළත් කිරීමේදී ඇතිවන යම් ආදාන දෝෂ හඳුනා ගැනීමයි. වලංගු නොවන checksum එකක් වාක්‍යයේ දෝෂයක් පවතින බව සංකේත කරයි. විරුද්ධව, වලංගු checksum එකක් වාක්‍යය බොහෝ විට නිවැරදි බව පෙන්වයි.


මෙම චෙක්සම් ලබා ගැනීමට, එන්ට්‍රොපිය SHA256 Hash ක්‍රියාවලිය හරහා ගෙන යනු ලැබේ. මෙම මෙහෙයුම ප්‍රතිදානය ලෙස 256-බිට් අනුක්‍රමයක් නිපදවයි, එහි පළමු `N` බිට් පමණක් තබා ගනු ලැබේ, අවශ්‍ය ප්‍රතිසාධන වාක්‍යයේ දිග මත `N` යටපත් වේ (ඉහත වගුව බලන්න). එබැවින්, 12-වචන වාක්‍යයක් සඳහා, Hash හි පළමු 4 බිට් තබා ගනු ලැබේ.

![mnemonic](assets/en/3.webp)

මෙම පළමු බිට් 4, පරීක්ෂා එකතුවක් ලෙස සෑදීමෙන් පසු, මුල් අසමත්‍රතාවයට එකතු කරනු ලැබේ. මෙම අවස්ථාවේදී, ප්‍රතිසාධන වාක්‍යය ප්‍රායෝගිකව සෑදී ඇත, නමුත් එය තවමත් ද්වික පරිපථයකි. මෙම ද්වික අනුපිළිවෙල BIP39 සම්මතයට අනුකූලව වචන වලට පරිවර්තනය කිරීමට, අපි පළමුව මෙම අනුපිළිවෙල 11-බිට් කොටස් වලට බෙදනු ඇත.

![mnemonic](assets/notext/4.webp)

यी प्रत्येक प्याकेटहरूले बाइनरीमा एउटा संख्या प्रतिनिधित्व गर्छन् जसलाई त्यसपछि दशमलव संख्यामा (आधार 10) रूपान्तरण गरिनेछ। हामी प्रत्येक संख्यामा `1` थप्नेछौं, किनभने कम्प्युटिङमा, गणना `0` बाट सुरु हुन्छ, तर BIP39 सूची `1` बाट क्रमांकित गरिएको छ।


![mnemonic](assets/notext/5.webp)


අවසානයේ, දශම සංඛ්‍යාව අපට [2048 BIP39 වචන ලැයිස්තුවේ](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) අදාළ වචනයේ ස්ථානය කියා දෙයි. අපගේ Wallet සඳහා ප්‍රතිසාධන වාක්‍යය සකස් කිරීමට මෙම වචන තෝරා ගැනීම පමණක් ඉතිරිව ඇත.


![mnemonic](assets/notext/6.webp)


දැන්, අභ්‍යාසයට ගමන් කරමු! අපි generate 12-වචන ප්‍රතිසාධන වාක්‍යයක් කරමු. කෙසේ වෙතත්, මෙම මෙහෙයුම 24-වචන වාක්‍යයක් සඳහා සමාන වේ, වෙනස් වන්නේ එය 256 බිට් එන්ට්‍රොපිය සහ 8-බිට් පරීක්ෂා එකතුවක් අවශ්‍ය වන අතර, මෙම කොටසේ ආරම්භයේ පිහිටා ඇති සමානතා වගුවේ සඳහන් වේ.


## 1. korak: Entropija ustvarjanje


ඔබේ කඩදාසි පත, ඔබේ පෑන, සහ ඔබේ සීසම් සූදානම් කරන්න. ආරම්භ කිරීමට, අපට generate 128 බිට්ස් අහඹු ලෙස අවශ්‍ය වන අතර, එනම්, 128 `0`s සහ `1`s එකට අනුපිළිවෙලින් අවශ්‍ය වේ. මෙය කිරීමට, අපි සීසම් භාවිතා කරන්නෙමු.

![mnemonic](assets/notext/7.webp)


Kocke imajo 6 strani, vse z enako verjetnostjo, da se vržejo. Vendar je naš cilj ustvariti binarni rezultat, kar pomeni dva možna izida. Zato bomo vrednost `0` dodelili vsakemu metu, ki pristane na sodo število, in `1` za vsako liho število. Posledično bomo izvedli 128 metov, da ustvarimo našo 128-bitno entropijo. Če kocka pokaže `2`, `4` ali `6`, bomo zapisali `0`; za `1`, `3` ali `5` bo to `1`. Vsak rezultat bo zapisan zaporedno, od leve proti desni in od zgoraj navzdol.


ඊළඟ පියවර පහසු කිරීම සඳහා, අපි බිට් සටහන් හතර සහ තුනකින් සමූහ කරමු, පහත රූපයේ දැක්වෙන පරිදි. සෑම පේළියක්ම බිට් 11 ක් තිබිය යුතුය: බිට් 4 කින් යුත් කට්ටල 2 ක් සහ බිට් 3 කින් යුත් කට්ටලයක්.


![mnemonic](assets/notext/8.webp)


Kot lahko vidite v mojem primeru, je dvanajsta beseda trenutno sestavljena samo iz 7 bitov. Ti bodo v naslednjem koraku dopolnjeni s 4 biti kontrolne vsote, da tvorijo 11 bitov.


![mnemonic](assets/notext/9.webp)


## පියවර 2: පරීක්ෂා එකතුව ගණනය කිරීම


Ta korak je najbolj kritičen pri ročnem generiranju fraze Mnemonic, saj zahteva uporabo računalnika. Kot je bilo že omenjeno, kontrolna vsota ustreza začetku SHA256 Hash, ki je ustvarjen iz entropije. Čeprav je teoretično mogoče izračunati SHA256 ročno za vhod 128 ali 256 bitov, bi ta naloga lahko trajala cel teden. Poleg tega bi bila vsaka napaka v ročnih izračunih odkrita šele na koncu procesa, kar bi vas prisililo, da začnete znova od začetka. Zato je nepredstavljivo, da bi ta korak izvedli le s papirjem in pisalom. Računalnik je skoraj obvezen. Če še vedno želite izvedeti, kako narediti SHA256 ročno, razlagamo, kako to storiti v [tečaju CRYPTO301](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f).


Iz tega razloga močno odsvetujem ustvarjanje ročnega stavka za dejanski Wallet. Po mojem mnenju uporaba računalnika v tej fazi, tudi ob vseh potrebnih previdnostnih ukrepih, nerazumno poveča površino napada Wallet.

චෙක්සම් ගණනය කිරීමේදී හැකි ඉක්මනින් අඩු සලකුණු තැබීම සඳහා, අපි **Tails** නම් කළ හැකි ධාවක ධාවකයකින් අමනේසියානු Linux බෙදාහැරීමක් භාවිතා කරන්නෙමු. මෙම මෙහෙයුම් පද්ධතිය USB කුටියකින් ආරම්භ වන අතර පරිගණකයේ RAM මත පූර්ණයෙන් ක්‍රියා කරයි, Hard ධාවකය සමඟ අන්තර්ක්‍රියා නොකරයි. එබැවින්, න්‍යාය පත්‍රය අනුව, එය පරිගණකය නිවා දැමූ පසු කිසිදු සලකුණක් නොතබයි. කරුණාකර සලකන්න Tails x86_64 වර්ගයේ ප්‍රොසෙසර සමඟ පමණක් අනුකූල වන අතර ARM වර්ගයේ ප්‍රොසෙසර සමඟ නොවේ.

Za začetek, iz vašega običajnega računalnika, [prenesite sliko Tails z njegove uradne spletne strani](https://tails.net/install/index.fr.html). Zagotovite pristnost vašega prenosa z uporabo razvijalčevega podpisa ali orodja za preverjanje, ki ga ponuja spletna stran.

![mnemonic](assets/notext/10.webp)

මුලින්ම, ඔබේ USB කුටිය ආකෘතිගත කිරීමට පසු, [Balena Etcher](https://etcher.balena.io/) වැනි මෙවලමක් භාවිතයෙන් Tails ස්ථාපනය කරන්න.

![mnemonic](assets/notext/11.webp)

Utripa je uspešno potrjena, izklopite računalnik. Nato nadaljujte z odklopom napajanja Supply in odstranite pogon Hard iz matične plošče vašega računalnika. Če je prisotna kartica WiFi, jo je treba odklopiti. Prav tako odstranite vse RJ45 Ethernet kable. Da zmanjšate tveganje uhajanja podatkov, je priporočljivo, da izklopite internetno omarico in izklopite mobilni telefon. Poleg tega poskrbite, da odklopite vse odvečne periferne naprave iz računalnika, kot so mikrofon, spletna kamera, zvočniki ali slušalke, in preverite, da so druge periferne naprave povezane le preko kabla. Vsi ti koraki priprave računalnika niso nujni, vendar preprosto pomagajo zmanjšati površino napada, kolikor je mogoče, v resničnem kontekstu.


පරිගණකය බාහිර උපාංගයකින් ආරම්භ කිරීමට අවසර දීමට ඔබේ BIOS වින්‍යාසගත කර ඇතිදැයි පරීක්ෂා කරන්න. එසේ නොමැතිනම්, මෙම සැකසීම වෙනස් කර, පසුව ඔබේ යන්ත්‍රය නැවත ආරම්භ කරන්න. පරිගණක පරිසරය ආරක්ෂා කරගෙන ඇති විට, Tails OS සමඟ USB කුටියෙන් පරිගණකය නැවත ආරම්භ කරන්න.


Tails පිළිගැනීමේ තිරයේ, ඔබ කැමති භාෂාව තෝරන්න, එවිට `Start Tails` ක්ලික් කිරීමෙන් පද්ධතිය ආරම්භ කරන්න.


![mnemonic](assets/notext/12.webp)


ඩෙස්ක්ටොප් එකෙන්, `Applications` ටැබය ක්ලික් කරන්න.


![mnemonic](assets/notext/13.webp)


සැකිල්ල `Utilities` මෙනුවට යන්න.


![mnemonic](assets/notext/14.webp)


අවසානයේ, `Terminal` යෙදුම මත ක්ලික් කරන්න.


![mnemonic](assets/notext/15.webp)


ඔබ නව හිස් විධාන ටර්මිනලයකට පැමිණෙනු ඇත.


![mnemonic](assets/notext/16.webp)

`echo 10101010101010101010101010101010`

![mnemonic](assets/notext/17.webp)


අමතර ඉඩක් එක්කර, පසුව පහත විධානය ඇතුළත් කරන්න, _පයිප්පයක්_ (`|`) භාවිතා කරමින්:


```plaintext
| shasum -a 256 -0


![mnemonic](assets/notext/18.webp)


උදාහරණයෙහි මගේ එන්ට්‍රොපිය සමඟ, සම්පූර්ණ විධානය මෙසේ වේ:


```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```


මෙම විධානයේ:



- `echo` යෙදී ඇත්තේ බිට් අනුක්‍රමය යැවීමට;
- `|`, _pipe_, se uporablja za usmerjanje izhoda ukaza `echo` v vhod naslednjega ukaza;
- `shasum` SHA (_Secure Hash Algorithm_) පවුලට අයත් හෑෂිං ක්‍රියාවලියක් ආරම්භ කරයි;
- `-a` določite izbiro določenega algoritma zgoščevanja;
- `256` පෙන්වන්නේ SHA256 ඇල්ගොරිතමය භාවිතා කරන බවයි;
- `-0` ආදානය ද්විතීයික සංඛ්‍යාවක් ලෙස විවරණය කිරීමට ඉඩ සලසයි.


ඔබේ ද්විනාරි අනුක්‍රමය කිසිදු ටයිප් කිරීමේ දෝෂයක් නොමැති බව සොයා බැලීමෙන් පසු, විධානය ක්‍රියාත්මක කිරීමට `Enter` යතුර ඔබන්න. එවිට ටර්මිනල් ඔබේ entropy හි SHA256 Hash පෙන්වනු ඇත.


![mnemonic](assets/notext/19.webp)


Trenutno je Hash izražen v šestnajstiški obliki (osnova 16). Na primer, moj je:


```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```


අපගේ Mnemonic වාක්‍යය අවසන් කිරීමට, අපට Hash හි පළමු බිට් 4 පමණක් අවශ්‍ය වන අතර එය පරීක්ෂාකේතය ලෙස ක්‍රියා කරයි. හෙක්සඩෙසිමල් ආකෘතියේදී, සෑම අක්ෂරයක්ම බිට් 4 නියෝජනය කරයි. එබැවින්, අපි Hash හි පළමු අක්ෂරය පමණක් තබා ගන්නෙමු. වචන 24 ක වාක්‍යයක් සඳහා, පළමු අක්ෂර 2 සැලකිල්ලට ගැනීම අවශ්‍ය වේ. මගේ උදාහරණයේ, මෙය අකුරට සමාන වේ: `a`. මෙම අක්ෂරය ඔබේ පත්‍රයේ කොතැනක හෝ සූක්ෂමව සටහන් කර, පසුව ඔබේ පරිගණකය නිවා දමන්න.


මීළඟ පියවර වන්නේ මෙම හෙක්සඩෙසමල් අක්ෂරය (පද 16) ද්විමය අගයක් (පද 2) බවට පරිවර්තනය කිරීමයි, අපගේ වාක්‍යය මෙම ආකෘතියෙන් නිර්මාණය කර ඇත. මෙය කිරීමට, ඔබට පහත පරිවර්තන වගුව භාවිතා කළ හැක:


| Decimal (base 10) | Hexadecimal (base 16) | Binary (base 2) |
| ----------------- | --------------------- | --------------- |
| 0                 | 0                     | 0000            |
| 1                 | 1                     | 0001            |
| 2                 | 2                     | 0010            |
| 3                 | 3                     | 0011            |
| 4                 | 4                     | 0100            |
| 5                 | 5                     | 0101            |
| 6                 | 6                     | 0110            |
| 7                 | 7                     | 0111            |
| 8                 | 8                     | 1000            |
| 9                 | 9                     | 1001            |
| 10                | a                     | 1010            |
| 11                | b                     | 1011            |
| 12                | c                     | 1100            |
| 13                | d                     | 1101            |
| 14                | e                     | 1110            |
| 15                | f                     | 1111            |

මගේ උදාහරණයේ, අකුර `a` යෙදී ඇත්තේ ද්විතීයික සංඛ්‍යාව `1010` වෙතය. මෙම බිට් 4 ක් අපගේ ප්‍රතිසාධන වාක්‍යයේ පරීක්ෂා මුදුව සෑදේ. දැන් ඔබට එය ඔබේ කඩදාසි පත üzerinde දැනට සටහන් කර ඇති එන්ට්‍රොපියට එක් කළ හැක, අවසන් වචනයේ අගට තබමින්.


![mnemonic](assets/notext/20.webp)


ඔබේ Mnemonic වාක්‍යය දැන් සම්පූර්ණයි, නමුත් එය ද්විතීයික ආකෘතියෙන් ඇත. ඊළඟ පියවර වන්නේ එය දශම පද්ධතියට පරිවර්තනය කිරීමයි, එවිට ඔබට එක් එක් අංකය BIP39 ලැයිස්තුවේ අදාළ වචනයක් සමඟ සම්බන්ධ කළ හැක.


## පියවර 3: වචන දශමීය වලට පරිවර්තනය කිරීම


ඔබේ කඩදාසියේ ඇති සෑම ද්විතීයික රේඛාවක්ම දශම සංඛ්‍යාකාරයට පරිවර්තනය කිරීමට, අපි අතින් ගණනය කිරීම පහසු කරන ක්‍රමයක් භාවිතා කරන්නෙමු. දැනට, ඔබේ කඩදාසියේ ද්විතීයික අංක `0` හෝ `1` 11 කින් සමන්විත රේඛා දොළහක් ඇත. දශමයට පරිවර්තනය කිරීමට ඉදිරියට යාමට, සෑම පළමු අංකයකටම එය `1` නම් `1024` අගය පවරන්න, නැතහොත් `0`. දෙවන අංකය සඳහා, එය `1` නම් `512` අගය පවරනු ඇත, නැතහොත් `0`, එසේම එකොළොස්වැනි අංකය දක්වා. අනුකූලතා පහත පරිදි වේ:



- 1st bit: `1024`;
- 2nd bit: `512`;
- 3rd bit: `256`;
- 4th bit: `128`;
- 5th bit: `64`;
- 6th bit: `32`;
- 7th bit: `16`;
- 8වන බිට්: `8`;
- 9th bit: `4`;
- 10th bit: `2`;
- 11වන බිට්: `1`.


සෑම පේළියක් සඳහාම, අපි දශම සංඛ්‍යාත්මක සංඛ්‍යාව ලබා ගැනීමට `1` අංකයට අදාළ අගයන් එකතු කරමු. ද්විමය රේඛාවකට සමාන උදාහරණයක් ගනිමු:


```plaintext
1010 1101 101
```


පරිවර්තනය මෙසේ වේ:

![mnemonic](assets/notext/21.webp)

ප්‍රතිඵලය එවිට වන්නේ:


```plaintext
1389
```


සෑම `1` ට සමාන බිට් එකක් සඳහාම, පහත සඳහන් අනුකූල සංඛ්‍යාව වාර්තා කරන්න. සෑම `0` ට සමාන බිට් එකක් සඳහාම, කිසිවක් වාර්තා නොකරන්න.


![mnemonic](assets/notext/22.webp)

එවිට, සරලව `1`s මගින් වලංගු කරන ලද සියලු සංඛ්‍යා එකතු කර binary රේඛාවක් නියෝජනය කරන දශම සංඛ්‍යාව ලබා ගන්න. උදාහරණයක් ලෙස, මෙන්න මගේ පත්‍රය සඳහා එය මෙහෙම පෙනේ:

![mnemonic](assets/notext/23.webp)


## පියවර 4: Mnemonic වාක්‍යයේ වචන සෙවීම


දශම සංඛ්‍යා වලින් ලබා ගත් පසු, අපට දැන් Mnemonic වාක්‍යය සම්පාදනය කිරීමට ලැයිස්තුවේ අදාළ වචන සොයා ගත හැක. කෙසේ වෙතත්, BIP39 ලැයිස්තුවේ 2048 වචන වල අංකනය `1` සිට `2048` දක්වා වේ. නමුත්, අපගේ ගණනය කළ ද්විතීයික ප්‍රතිඵල `0` සිට `2047` දක්වා වේ. එබැවින්, නිවැරදි කිරීමට අවශ්‍ය එක් ඒකකයක ස්ථාන මාරුවක් ඇත. මෙම ස්ථාන මාරුව නිවැරදි කිරීමට, පෙර ගණනය කළ දශම සංඛ්‍යා දොළහට `1` එකතු කරන්න.


![mnemonic](assets/notext/24.webp)


Po tej prilagoditvi imate rang vsake besede znotraj seznama. Vse, kar ostane, je, da vsako besedo identificirate po njeni številki. Očitno, kot pri vseh drugih korakih, ne smete uporabiti računalnika za izvedbo te pretvorbe. Zato se prepričajte, da ste seznam prej natisnili.


[**-> BIP39 ලැයිස්තුව A4 ආකෘතියෙන් මුද්‍රණය කරන්න.**](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)


Na primer, če je številka, pridobljena iz prve vrstice, 1721, bo ustrezna beseda 1721. na seznamu:


```plaintext
1721. strike
```


![mnemonic](assets/notext/25.webp)

بهذا الأسلوب، نستمر بشكل متتابع مع الكلمات الـ 12 لبناء عبارة Mnemonic الخاصة بنا.


![mnemonic](assets/notext/26.webp)


## පියවර 5: Bitcoin Wallet නිර්මාණය කිරීම


මෙම අවස්ථාවේදී, අපට ඉතිරිව ඇත්තේ අපගේ Mnemonic වාක්‍යය Bitcoin Wallet මෘදුකාංගයකට ආයාත කිරීම පමණි. අපගේ කැමැත්තන් අනුව, මෙය Hot Wallet ලබා ගැනීම සඳහා ඩෙස්ක්ටොප් මෘදුකාංගයකදී, හෝ Cold Wallet සඳහා Hardware Wallet මත සිදු කළ හැක.


![mnemonic](assets/notext/27.webp)


ඔබේ චෙක්සම් වල වලංගුතාවය ඔබට සනාථ කළ හැක්කේ ආනයනය කිරීමේදී පමණි. මෘදුකාංගය `Invalid Checksum` වැනි පණිවිඩයක් පෙන්වන්නේ නම්, එය ඔබේ නිර්මාණ ක්‍රියාවලියට දෝෂයක් ඇතුළු වී ඇති බව අර්ථ දක්වයි. සාමාන්‍යයෙන්, මෙම දෝෂය ඇති වන්නේ අතින් පරිවර්තන සහ එකතු කිරීම් කරන විට වැරදි ගණනයකිරීමකින් හෝ Tails හි ටර්මිනල් එකට ඔබේ entropy ඇතුළත් කරන විට ටයිප් කිරීමේ දෝෂයකින් වේ. මෙම දෝෂ නිවැරදි කිරීමට ක්‍රියාවලිය ආරම්භයෙන් නැවත ආරම්භ කිරීම අවශ්‍ය වේ.


![mnemonic](assets/notext/28.webp)

Wallet නිර්මාණය කිරීමෙන් පසු, ඔබේ ප්‍රතිසාධන වාක්‍යය කඩදාසි හෝ ලෝහ වැනි භෞතික මාධ්‍යයකට ආපසු ගබඩා කිරීමට අමතක නොකරන්න, සහ එහි ජනනය කිරීමේදී භාවිතා කරන ලද සටහන විනාශ කරන්න, කිසිදු තොරතුරු කාන්දුවක් වළක්වා ගැනීමට.


## Coldcards හි ඩයිස් රෝල් විකල්පයේ විශේෂිත අවස්ථාව


Coldcard පවුලේ දෘඩාංග පසුම්බි [Dice Roll නම් වූ විශේෂාංගයක්](https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7) ලබා දේ, ඔබේ Wallet හි ප්‍රතිසාධන වාක්‍යය සූරියන් සමඟ generate කිරීමට. මෙම ක්‍රමය විශිෂ්ටයි, මන්ද එය ඔබට එන්ට්‍රොපි නිර්මාණය පිළිබඳ සෘජු පාලනය ලබා දේ, අපගේ උපකාරක පරිදි පරීක්ෂාකය ගණනය කිරීම සඳහා බාහිර උපාංගයක් භාවිතා කිරීම අවශ්‍ය නොවේ.


කෙසේ වෙතත්, මෙම විශේෂාංගය අසමත් ලෙස භාවිතා කිරීම නිසා මෑතකදී Bitcoin සොරකම් සිදුවීම් වාර්තා වී ඇත. ඇත්ත වශයෙන්ම, අතිශය සීමිත සමානකරණ ගණනක් ප්‍රමාණවත් නොවන අසාධාරණතාවයට හේතු විය හැකි අතර, සෛද්ධාන්තිකව Mnemonic වාක්‍යය බලහත්කාරයෙන් බලන්න සහ සම්බන්ධිත බිට්කොයින් සොරකම් කිරීමේ හැකියාවක් ඇත. මෙම අවදානමෙන් වළකින්න, ප්‍රමාණවත් අසාධාරණතාවයක් සහතික කරන Coldcard මත අවම වශයෙන් 99 සමානකරණ සිදු කරන ලෙස උපදෙස් දෙනු ලැබේ.


Metoda interpretacije rezultatov, ki jo predlaga Coldcard, se razlikuje od tiste, predstavljene v tem priročniku. Medtem ko v priročniku priporočamo 128 metov za dosego 128 bitov varnosti, Coldcard predlaga 99 metov za dosego 256 bitov varnosti. V našem pristopu sta namreč možna le dva izida za vsak met kocke: sodo (`0`) ali liho (`1`). Zato je entropija, ki jo ustvari vsak met, enaka `log2(2)`. V primeru Coldcarda, ki upošteva šest možnih strani kocke (od `1` do `6`), je entropija na met enaka `log2(6)`. Zato moramo v našem priročniku izvesti več metov, da dosežemo enako raven entropije.


```plaintext
Entropy = number of rolls * log2(number of possible outcomes on the dice)

Coldcard :

Entropy = 99 * log2(6)
Entropy = 255.91

Our tutorial :

Entropy = 128 * log2(2)
Entropy = 128
```