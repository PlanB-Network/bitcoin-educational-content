---
name: Ricochet
description: Ricochet ගනුදෙනු අවබෝධ කර ගැනීම සහ භාවිතා කිරීම
---
![cover ricochet](assets/cover.webp)


***අවවාදය:** Samourai Wallet ආරම්භකයින් අත්අඩංගුවට ගෙන, ඔවුන්ගේ සේවාදායකයන් අප්‍රේල් 24 වන දින අත්පත් කර ගැනීමෙන් පසු, Ricochet මෙවලම තවදුරටත් ලබා ගත නොහැක. කෙසේ වෙතත්, මෙම මෙවලම ඉදිරි සති කිහිපය තුළ නැවත ලබා දිය හැකි බවක් ඇත. මේ අතර, ඔබට Ricochet අතින් සිදු කළ හැක. එහි ක්‍රියාකාරිත්වය අවබෝධ කර ගැනීමට සහ අතින් එය කරන්නේ කෙසේද යන්න ඉගෙන ගැනීමට මෙම ලිපියේ සංකල්පවත් කොටස අදාලව පවතී.*


_අපි මෙම නඩුවේ සංවර්ධන මෙන්ම සම්බන්ධිත මෙවලම් සම්බන්ධයෙන් ඇතිවන සංවර්ධනද ආසන්නයෙන් අනුගමනය කරමින් සිටිමු. නව තොරතුරු ලබා ගත හැකි වීමත් සමඟ මෙම උපකාරකය යාවත්කාලීන කරන බවට විශ්වාසවන්ත වන්න._


_මෙම උපකාරිකාව අධ්‍යාපනික සහ තොරතුරුමය අරමුණු සඳහා පමණක් සපයනු ලැබේ. අපි මෙම මෙවලම් අපරාධමය අරමුණු සඳහා භාවිතා කිරීම අනුමත නොකරන අතර හෝ උත්තේජනය නොකරන අතරේ. තමන්ගේ නීතිමය බලප්‍රදේශයේ නීති පිළිපැදීම සෑම පරිශීලකයෙකුගේම වගකීමකි._


---

> ප්‍රිමියම් මෙවලමක්, ඔබේ ගනුදෙනුවට අතිරේක ඉතිහාසය එකතු කරයි. කළු ලැයිස්තු වාරණය කර, අසාධාරණ 3වන පාර්ශව ගිණුම් වසා දැමීම් වලින් ආරක්ෂා වීමට උපකාරී වේ.

## Ricochet kaj je?


Ricochet je tehnika, ki vključuje izvajanje več fiktivnih transakcij samemu sebi, da bi simulirali prenos Bitcoin Ownership. To orodje se razlikuje od drugih Samourai transakcij, saj ne zagotavlja perspektivne anonimnosti, temveč obliko retrospektivne anonimnosti. Ricochet pomaga zamegliti posebnosti, ki bi lahko ogrozile zamenljivost kovanca Bitcoin.


Na primer, če izvedete CoinJoin, bo vaš izhod kovanca iz mešanice tako označen. Orodja za analizo verig lahko zaznajo vzorce transakcij CoinJoin in označijo kovance, ki iz njih izhajajo. Dejansko CoinJoin želi prekiniti zgodovinske povezave kovanca, vendar je njegov prehod skozi coinjoin še vedno zaznaven. Za analogijo je ta pojav podoben šifriranju besedila: čeprav ne moremo dostopati do izvirnega besedila, je zlahka prepoznavno, da je bilo uporabljeno šifriranje.


Natančno, ta oznaka "CoinJoin izhodni kovanec" lahko vpliva na zamenljivost UTXO. Regulirani subjekti, kot so platforme Exchange, lahko zavrnejo sprejem UTXO, ki je bil podvržen CoinJoin, ali celo zahtevajo pojasnila od njegovega lastnika, s tveganjem, da bo njihov račun blokiran ali sredstva zamrznjena. V nekaterih primerih lahko platforma celo prijavi vaše vedenje državnim organom.


To je mesto, kjer pride v poštev metoda Ricochet. Da bi zameglili sled, ki jo pusti CoinJoin, Ricochet izvede štiri zaporedne transakcije, kjer uporabnik prenese svoja sredstva na različne naslove. Po tem zaporedju transakcij orodje Ricochet končno usmeri bitcoine na njihovo končno destinacijo, kot je platforma Exchange. Cilj je ustvariti razdaljo med prvotno transakcijo CoinJoin in končnim dejanjem porabe. Na ta način bodo orodja za analizo verige mislila, da je verjetno prišlo do prenosa Ownership po CoinJoin, zato ni potrebno ukrepati proti pošiljatelju.


![ricochet diagram](assets/en/1.webp)


Ob soočenju z metodo Ricochet bi si lahko predstavljali, da bi programska oprema za analizo verig poglobila svoje preiskave onkraj štirih odbojev. Vendar se te platforme soočajo z dilemo pri optimizaciji praga zaznavanja. Ugotoviti morajo mejo števila skokov, po kateri priznajo, da je verjetno prišlo do spremembe lastništva in da je povezavo s prejšnjim CoinJoin treba prezreti. Vendar je določanje tega praga tvegano: vsako podaljšanje opazovanega števila skokov eksponentno poveča obseg lažnih pozitivnih rezultatov, tj. posameznikov, ki so napačno označeni kot udeleženci v CoinJoin, ko je operacijo dejansko izvedel nekdo drug. Ta scenarij predstavlja veliko tveganje za ta podjetja, saj lažni pozitivni rezultati vodijo v nezadovoljstvo, kar lahko prizadete stranke usmeri k konkurenci. Na dolgi rok preveč ambiciozen prag vodi platformo k izgubi več strank kot njeni konkurenti, kar bi lahko ogrozilo njeno sposobnost preživetja. Zato je za te platforme zapleteno povečati število opazovanih odbojev, in 4 je pogosto zadostno število za nasprotovanje njihovim analizam.


ඒ අනුව, **UTXO එකක් ඔබට අයත් වන විට, පෙර CoinJoin එකකට සහභාගී වීම සඟවා තැබිය යුතු අවස්ථාවලදී Ricochet සඳහා වඩාත් සාමාන්‍ය භාවිතය ඇති වේ**. ඉතාමත් හොඳින්, CoinJoin එකකට ලක්වූ බිට්කොයින් විනිමය කරන ලද ආයතන වෙත මාරු කිරීමෙන් වළකින්න. කෙසේ වෙතත්, වෙනත් විකල්පයක් නොමැති අවස්ථාවක, විශේෂයෙන්ම බිට්කොයින් මුදල් වලට මාරු කිරීමට ඉක්මනින් අවශ්‍ය වන විට, Ricochet ප්‍රභල විසඳුමක් ලබා දේ.


## Kako deluje Ricochet na Samourai Wallet?

Ricochet යනු කෙටියෙන්ම කෙනෙකු තමන්ටම බිට්කොයින් යැවීමේ ක්‍රමයක් වේ. එබැවින් විශේෂිත මෙවලමක් භාවිතා නොකර රිකොෂෙට් එකක් අතින් අනුකරණය කිරීම සම්පූර්ණයෙන්ම හැකියාවක් ඇත. කෙසේ වෙතත්, වැඩි නිවැරදි ප්‍රතිඵලයකින් ප්‍රයෝජන ලබමින් ක්‍රියාවලිය ස්වයංක්‍රීය කිරීමට කැමති අය සඳහා Samourai Wallet යෙදුම හරහා ලබා ගත හැකි Ricochet මෙවලම හොඳ විසඳුමක් වේ.


සමුරායි හි සේවාව ගෙවීම් සහිත බැවින්, රිකොෂෙට් සඳහා සේවා ගාස්තු ලෙස `100,000 Sats` ක වියදමක් ඇති අතර, Mining ගාස්තු වලට අමතරව වේ. එබැවින්, එය විශාල මුදල් මාරු සඳහා වැඩි වශයෙන් නිර්දේශ කෙරේ.


Samourai යෙදුම Ricochet වර්ග දෙකක් ලබා දේ:


- Ojačan Ricochet, ali "staggered delivery," nudi prednost raspoređivanja Samourai naknada za uslugu preko pet uzastopnih transakcija. Ova opcija također osigurava da se svaka transakcija emitira u različito vrijeme i zabilježi u različitom bloku, što blisko oponaša ponašanje promjene Ownership. Iako sporija, ova metoda je poželjna za one koji nisu u žurbi, jer maksimizira učinkovitost Ricochet-a poboljšavajući njegovu otpornost na analizu lanca.
- ක්ලැසික් රිකොෂේ, සියලුම ගනුදෙනු අඩුකළ කාල අන්තරයකින් විකාශනය කිරීමෙන් මෙහෙයුම ඉක්මනින් ක්‍රියාත්මක කිරීමට නිර්මාණය කර ඇත. එබැවින්, මෙම ක්‍රමය වඩාත්ම අඩු පෞද්ගලිකත්වයක් සහ විශ්ලේෂණයට අඩු ප්‍රතිරෝධයක් ලබා දේ. එය හදිසි මාරු සඳහා පමණක් කැමති විය යුතුය.


## Kako izvesti Ricochet na Samourai Wallet?

Samourai Wallet යෙදුමෙන් Ricochet ගනුදෙනුවක් සිදු කිරීමට, අපගේ වීඩියෝ උපකාරකය අනුගමනය කරන්න:

![Ricochet YouTube video tutorial](https://youtu.be/Gsz0zuVo3N4)


Če želite preučiti transakcije Ricochet, izvedene v tej vadnici, so tukaj:


- පළමු Ricochet ගනුදෙනුව: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://Mempool.space/fr/Testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Zadnja transakcija Ricochet: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://Mempool.space/fr/Testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)


**බාහිර සම්පත්:**


- https://docs.samourai.io/en/Wallet/features/ricochet