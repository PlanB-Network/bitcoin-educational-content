---
name: Lihtne sisselogimine
description: Pseudonimede abil kaitstud identiteet
---
![cover](assets/cover.webp)

## Sisselogimine = e-posti aadress = privaatsuse kaotamine


Digimaailmas on saanud tavaks, et iga platvormi jaoks, millele soovitakse juurdepääsu, tuleb luua konto.

Iga selline teenus nõuab sisselogimist, mis on tavaliselt seotud _kasutajanime_ ja _salasõna_ paariga. Sageli on kasutajanimi kasutaja isiklik e-posti aadress.


Kui kasutate igal sisselogimisel oma isiklikku e-posti Address, on lihtne ette kujutada esimest tagajärge: konfidentsiaalsuse kaotamine, mis muutub oluliseks, kui Address koosneb aadressist _name.surname@serviceemail.com_.


Avatud lähtekoodiga tööriistade arendajad on loonud rea rakenduste komplekte, mis on sündinud just selleks, et kasutajad saaksid natuke privaatsust tagasi: nad logivad endiselt sisse, kuid kasutavad oma isiklikku identiteeti paljastava tööriista asemel aliase.


Kõige lihtsam neist, mida ma isiklikult olen proovinud ja veel katsetan, on [Simple Login](https://simplelogin.io/).


## Alias


E-posti alias lihtsalt asendab teie e-posti Address osa _nimi.perekonnanimi_ fiktiivse nimega. Kasutaja jaoks ei muutu midagi; alias-teenus edastab e-kirju tavalisele Address-le ja tavalisest Address-st nagu tavaliselt. Igaüks võib jätkata oma postkasti kasutamist nagu alati, kuid selle asemel, et näidata oma tegelikku nime, näitab see tundmatut kasutajat. See teenus peab olema tõhus ja seni on Simple Login osutunud just selliseks.


Kui külastate Simple Login'i veebilehte esimest korda, peate looma konto (ka siin!), kasutades "ametlikku" e-posti aadressi Address. Siin tuleb sisestada e-post, parool ja lahendada captcha.


![image](assets/it/02.webp)


Simple Login saadab kinnitussõnumi näidatud e-posti aadressile Address. Kinnitusnupule klõpsamise asemel on soovitatav kopeerida link ja kleepida see Address ribale.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Kohe avaneb lihtsa sisselogimise armatuurlaud, millel on lühike juhendmaterjal navigeerimiseks.


![image](assets/it/05.webp)


Tuleb märkida, et Simple Login aktiveerib automaatselt uudiskirja tellimise, mida saab vastava käsuga deaktiveerida.


![image](assets/it/06.webp)


## Seaded


Teenuse funktsioonide avastamiseks võite kohe vaadata _Settings_. Simple Login algab kõigi aktiivsete valikutega, kaasa arvatud _Premium_, mis jäävad kasutatavaks 10 päevaks. Kui prooviperiood on lõppenud, on teil võimalus luua selle profiiliga 10 varjunime ja te saate otse siduda oma Protoni e-posti, sest Simple Login on ostetud Šveitsi e-posti teenusepakkuja poolt.


![image](assets/it/07.webp)


Saate määrata rea parameetreid või kontrollida, kas teie e-posti privaatsus on juba ohustatud.


![image](assets/it/08.webp)


Lõpuks saate eksportida oma profiili varukoopia või importida selle mõnelt teiselt teenusepakkujalt.


![image](assets/it/09.webp)


### Töö E-post


Need, kes kasutavad isikliku domeeniga e-kirju tööpostina, saavad luua oma isikliku domeeni.


![image](assets/it/10.webp)


Peapaneelilt, valides _Postkastid_, on võimalik lisada ka teisi e-posti aadresse ja kasutada ka vastavalt loodud varjunimesid. Selles õpetuses otsustasin näiteks luua profiili _gmail.com_ postkastiga ja seejärel siduda sellega _proton.me_ Address.


![image](assets/it/11.webp)


Uue Address lisamine, eriti kui see kuulub Proton teenusepakkujale, näitab juhendatud protseduur võimalust siseneda _sudo_-režiimi, superkasutajaks. Simple Login palub sisestada selle postkasti parooli, et tõestada seaduslikku Ownership.


⚠️ **Mina isiklikult ei soovita seda teha**. ⚠️


![image](assets/it/12.webp)


**Parem on pääseda e-postkasti -> kopeerida link kinnitamiseks ja kleepida see URL-ribale -> ja saada kinnitus ilma parooli avaldamata.**


![image](assets/it/13.webp)


Kahest sisestatud aadressist saab üks vaikimisi ja teine on sekundaarne, kuid neid saab hõlpsasti vahetada ja seade on armatuurlaual hõlpsasti tuvastatav.


![image](assets/it/14.webp)


Pärast teise e-posti Address lisamist (valikuline), vaatame, mida me saame teha Simple Loginiga.


## Pseudonimede loomine


Paneelis on esimene menüüvalik märgitud _Alias_, kus saate neid luua. Teil on võimalus generate aliase juhuslikult valida, klõpsates nupule Random Alias, mis on järgmisel pildil kujutatud Green nupp. See funktsioon loob unikaalse ja intrigeeriva e-posti Address.


![image](assets/it/24.webp)


Kui aga soovite teenuseid eristada, andes neile erinevad nimed, peate valima _Uue kohandatud varjunimi_. Seda tehes saate anda aliasile selle teenuse nime, millele soovite juurdepääsu (sotsiaalmeedia, teenusepakkujad, veebisündmused, juhuslikult kohatud võõrad inimesed jne). Ülejäänu tegeleb Simple Login.

Naljaga pooleks (aga mitte päris, kui tõtt öelda) otsustasin luua pangale varjunime ja nimetasin selle `BANK`. Kuigi on tõsi, et mu pank teab minust kõike, on minu jaoks lõbus nendega suhelda, kasutades neile arusaamatut e-posti Address. Simple Login genereerib tõepoolest juhusliku nime, mis on meie valitud nimest eraldatud `.`ga


Siin võib saada uus e-posti Address:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- ja nii edasi


Valida saab rohkem kui ühe domeeni: avalikud domeenid on saadaval tasuta paketiga, samas kui teised domeenid, mis on märgitud kui privaatsed (sealhulgas _@simplelogin.com_), laiendavad kasutajate valikut, kes otsustavad tellida tasulise paketi.


![image](assets/it/15.webp)


Kui juhuslik sufiks ja domeen on valitud, saate määrata, kas see uus (ja kummaline) Address peaks toimima aliasina ainult ühe isikliku e-postkasti jaoks või kõigi jaoks. Alias saab valmis ja aktiivseks pärast klõpsamist nupul _Create_


![image](assets/it/16.webp)


Uus e-kiri Address on loodud ja see on nüüd nähtav, valmis saatmiseks (panka!) lihtsalt kopeerides.


![image](assets/it/18.webp)


Siinkohal saate keskenduda iga teenuse või platvormi jaoks, millele soovite juurdepääsu ja kus e-posti aadress on konto loomiseks vajalik parameeter, aliase loomisele.


![image](assets/it/19.webp)


Privaatsuse austajate jaoks on olemas ka võimalus generate e-posti Address jaoks, mis põhineb UUID-protokollidel (mitte identifitseeritavatel nimedel), mis loob unikaalse 128-bitise identifikaatori, mida tsentraliseeritud osapooled ei kontrolli. Selle funktsiooni, mis on kasulik tundlike kontode puhul, leiate menüüst _Random Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Nagu näete, on tegemist e-posti Address-ga, mis nõuab nõuetekohast haldamist.


Kui te muudate oma meelt ja ei soovi enam aliase kasutada, klõpsake lihtsalt iga üksiku aliase käsul _More_ ja valige _Delete_.


![image](assets/it/23.webp)


## Aliase haldamine


Pseudonimede loomine on lihtne, nagu ka nende haldamine, mis nõuab vaid veidi hoolt ja distsipliini. Kogu liiklus liigub tegelikult ikkagi läbi selle e-posti postkasti, mille me alguses oleme määratlenud ametliku postkastina. Teated ja olulised teated platvormidelt jõuavad jätkuvalt Gmaili, Protoni või mis iganes e-posti teenusepakkuja kaudu.


Tulemuseks on aga see, et meil on säilinud peamine Address, mida me võime alates varjunimede loomise hetkest vabalt otsustada, kellele me seda avaldame ja kellele mitte.


Pseudonüüm töötab nii vastuvõtmisel kui ka saatmisel: teine kasutaja saab tõepoolest vastuse aadressilt alias.preoccupy789@8shield.net, kui see on selle konkreetse vastuvõtja jaoks valitud pseudonüüm.


## Plussid


Üldiselt on varjunimede kasutamine tõhus viis oma identiteedi ja privaatsuse kaitsmiseks. Andmevahendajad ja veebisaidid koguvad sageli e-posti aadresse, et jälgida kasutajate harjumusi ja käitumist. Kuigi varjunimi ei tee teid täiesti jälgimatuks, on selle järjepidev kasutamine positiivne samm teie andmete kaitsmise suunas. Pealegi on meie "globaalses digitaalkülas", kus häkkimine, andmete müük ja turvarikkumised on liiga tavalised, väga tõenäoline, et e-posti aadress, mida kasutate erinevatel veebisaitidel registreerimiseks, on juba ohustatud või sihtmärgiks võetud.


Ainulaadne pseudonüüm, mida kasutatakse iga sisselogimise puhul, **määrab meile kohe, milline platvorm saadab meie postkasti rämpsposti (või veel hullemat), sest e-posti identifitseeritakse sellega seotud varjunime järgi**. Teil pole aimugi, kui palju rämpsposti ja andmepüügi saadetakse nn usaldusväärsetest kanalitest, sest need on institutsionaalsed, kuni te ei hakka kasutama pseudonime pankade, postiteenuste või mõne kohustusliku valitsuse teenuse jaoks konkreetset pseudonime. Kui rämpsposti saatja (või veel hullem) on tuvastatud, teate, et sait on ohustatud, võttes kõik ettevaatusabinõud, et kaitsta kõiki sellele konkreetsele veebisaidile esitatud andmeid (mõelge krediitkaartidele!), mis võivad rikkumisest aru saada nädalaid hiljem.


Simple Login'i puhul on sellel tööriistal järgmised omadused:



- mobiilirakendus (samuti F-Droidilt) ja brauseripikendus, et hallata varjunimesid igas olukorras;
- kahefaktoriline autentimine iga uue pseudonüümi puhul, mis suurendab sõltumatust teenusest endast;
- PGP-tugi (_Premium-kasutajatele);
- iga tüüpi aliase (kohandatud, juhuslik ja UUID) lihtne loomine;
- sektori tasuta plaanide hulgas on võimalus kasutada varjunimesid rohkemate "ametlike" e-postkastidega. Teised konkurendid piirduvad vaid ühega.


## Miinused


- 10 varjunime ei pruugi olla piisav, kui kavatsete kasutada Simple Login'i ulatuslikult. Sellisel juhul on tasuline pakett, mis on üsna taskukohane, kasulik, et suurendada võimalike varjunimede arvu.
- Pseudonime ei ole võimalik luua konkreetse nime ja domeeniga. Juhuslik järelliide, mis lisatakse meie poolt valitud nime järele, tekitab Address, mida võib parimal juhul nimetada veidraks. Traditsiooniline sotsiaalmeedia keeldub tavaliselt sellist tüüpi e-posti aadressidega loodud kontode andmisest. Nostr parandab selle!
- Kui kasutate kellelegi sõnumi saatmiseks varjunime, võib see kergesti sattuda vastuvõtja rämpsposti kausta. Esimese sammuna on soovitatav kasutada pseudonüümi vastuvõtmiseks, nagu ka konto loomisel, meililistiga liitumisel jne.