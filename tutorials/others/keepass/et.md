---
name: KeePass
description: Kuidas seadistada kohalikku paroolihaldurit?
---
![kaas](assets/cover.webp)

Digiajastul peame haldama paljusid veebikontosid, mis hõlmavad meie igapäevaelu erinevaid aspekte, sealhulgas pangandust, finantsplatvorme, e-posti, failihoidlat, tervist, administratsiooni, sotsiaalvõrgustikke, videomänge jne.

Iga sellise konto autentimiseks kasutame identifikaatorit, sageli e-posti aadressi, millele lisandub parool. Silmitsi seistes võimatusega meelde jätta suur hulk unikaalseid paroole, võib tekkida kiusatus kasutada sama parooli või muuta veidi ühist alust, et seda oleks lihtsam meelde jätta. Siiski ohustavad need praktikad tõsiselt teie kontode turvalisust.

Esimene põhimõte paroolide puhul on mitte neid taaskasutada. Iga veebikonto peaks olema kaitstud ainulaadse ja täiesti eristuva parooliga. See on oluline, sest kui ründaja suudab kompromiteerida ühe teie paroolidest, ei soovi te, et tal oleks juurdepääs kõigile teie kontodele. Iga konto jaoks ainulaadse parooli omamine isoleerib potentsiaalsed rünnakud ja piirab nende ulatust. Näiteks, kui kasutate sama parooli videomänguplatvormi ja oma e-posti jaoks ning see parool kompromiteeritakse läbi videomänguplatvormiga seotud õngitsussaidi, võiks ründaja seejärel hõlpsasti juurde pääseda teie e-postile ja võtta kontrolli kõigi teiste veebikontode üle.

Teine oluline põhimõte on parooli tugevus. Parooli peetakse tugevaks, kui seda on raske jõuga lahti murda, st arvata katse-eksituse meetodil. See tähendab, et teie paroolid peavad olema võimalikult juhuslikud, pikad ja sisaldama erinevaid tähemärke (väiketähed, suurtähed, numbrid ja sümbolid).

Nende kahe parooliturvalisuse põhimõtte (ainulaadsus ja robustsus) rakendamine igapäevaelus võib osutuda keeruliseks, kuna on peaaegu võimatu meelde jätta unikaalne, juhuslik ja tugev parool kõigile meie kontodele. Siin tuleb mängu paroolihaldur.

Paroolihaldur genereerib ja hoiab turvaliselt tugevaid paroole, võimaldades teil juurde pääseda kõigile oma veebikontodele ilma, et peaksite neid individuaalselt meelde jätma. Peate meeles pidama ainult ühte parooli, peaparooli, mis annab teile juurdepääsu kõigile halduris salvestatud paroolidele. Paroolihalduri kasutamine suurendab teie veebiturvalisust, kuna see hoiab ära paroolide taaskasutamise ja genereerib süstemaatiliselt juhuslikke paroole. Kuid see lihtsustab ka teie igapäevast kontode kasutamist, keskendades juurdepääsu teie tundlikule teabele.
Selles õpetuses õpime, kuidas seadistada ja kasutada kohalikku paroolihaldurit, et suurendada teie veebiturvalisust. Siin tutvustan teile KeePassi. Kui olete aga algaja ja sooviksite kasutada veebipõhist paroolihaldurit, mis suudab sünkroniseerida mitme seadme vahel, soovitan järgida meie õpetust Bitwardeni kohta:
https://planb.network/tutorials/others/general/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*Ettevaatust: Paroolihaldur on suurepärane paroolide hoiustamiseks, kuid **te ei tohiks kunagi selles hoida oma Bitcoini rahakoti mnemoonilist fraasi!** Pea meeles, et mnemooniline fraas tuleks eksklusiivselt salvestada füüsilisel kujul, nagu paberil või metallil.*

---

## KeePassi tutvustus

KeePass on tasuta ja avatud lähtekoodiga paroolihaldur, mis on ideaalne neile, kes soovivad tasuta ja turvalist lahendust kohalikuks halduseks. See on tarkvara, mis tuleb paigaldada teie arvutisse ja mis, ilma pluginateta, ei suhtle internetiga. See on radikaalselt erinev lähenemine Bitwardenile, mida käsitlesime eelmises õpetuses. Bitwarden, erinevalt KeePassist, võimaldab sünkroniseerimist mitme seadme vahel ja seetõttu nõuab teie paroolide hoidmist veebiserveris.
Vaikimisi ei toeta KeePass brauserilaiendite, nagu Bitwarden, kasutamist; seetõttu peate oma paroolid tarkvarast käsitsi kopeerima ja kleepima. Kuigi see võib tunduda piiranguna, on paroolide kopeerimine ja kleepimine auto-täitmise kasutamise asemel hea praktika teie veebiturvalisuse jaoks.
KeePass on loodud olema nii kergekaaluline kui ka lihtsasti kasutatav, järgides samal ajal kõrgeid turvastandardeid. Tarkvara krüpteerib teie andmebaasi kohapeal, tagamaks teie volituste optimaalse kaitse. KeePass on ka ainus paroolihaldur, mille on valideerinud ANSSI (Prantsuse küberjulgeoleku amet).

Üks KeePassi peamisi eeliseid on selle paindlikkus. Seda saab kasutada mitmel erineval viisil, näiteks USB-mälupulgal ilma vajaduseta installida arvutisse. Lisaks, tänu selle [plugin keskkonnale](https://keepass.info/plugins.html), saab KeePassi kohandada spetsiifilisemate vajaduste rahuldamiseks.
![KEEPASS](assets/notext/01.webp)
## Kuidas KeePassi alla laadida?

KeePassi installimisprotsess sõltub kasutatavast operatsioonisüsteemist. Windowsi või Linuxi kasutajate jaoks on installimine suhteliselt lihtne. Kui aga kasutate macOS-i, on vajalik lisasamm, kuna KeePass on arendatud .NET platvormil, mida macOS otseselt ei toeta. Seetõttu peate seadistama ühilduva keskkonna, mis võimaldab KeePassi käitada Apple'i seadmetes.

Debian/Ubuntu kasutajatele, avage terminal ja sisestage järgmised käsud:

```bash
sudo apt-get update
sudo apt-get install keepass2
```

Fedora jaoks:

```bash
sudo dnf install keepass
```

Arch Linuxi jaoks:

```bash
sudo pacman -S keepass
```

Kui olete Windowsi arvutis, minge [ametlikule KeePassi allalaadimise lehele](https://keepass.info/download.html) ja laadige alla viimane installeri versioon:
![KEEPASS](assets/notext/02.webp)
Klõpsake allalaaditud failil, et seda käivitada, seejärel järgige seadistusviisardi juhiseid installimise lõpuleviimiseks (vt järgmist jaotist).

macOS kasutajate jaoks on installimine veidi keerulisem. Kui soovite kasutada KeePassi originaalversiooni nagu Windowsis, järgige allpool toodud juhiseid. Võite valida ka [KeePassXC](https://keepassxc.org/), alternatiivse versiooni, mis on ühilduv macOS-iga ja pakub veidi erinevat liidest.

KeePassi kasutamiseks vajate .NET rakenduste jaoks jooksuaega. Soovitan selleks installida Mono. Minge [ametlikule Mono lehele](https://www.mono-project.com/download/stable/#download-mac) jaotises "*macOS*", ja klõpsake lingil, et alla laadida installipakett (`.pkg`).
![KEEPASS](assets/notext/03.webp)
Avage allalaaditud `.pkg` fail ja järgige Mono installimiseks oma Maci juhiseid.
![KEEPASS](assets/notext/04.webp)
Seejärel minge ametlikule KeePassi veebisaidile ja laadige alla viimane kaasaskantav versioon `.zip` formaadis.
![KEEPASS](assets/notext/05.webp)
Pärast `.zip` faili allalaadimist topeltklõpsake sellel, et see lahti pakkida. Saate kausta, mis sisaldab mitmeid faile, sealhulgas `KeePass.exe`. Avage terminal, navigeerige KeePassi kausta (asendage `xx` versiooninumbriga):

```bash
cd ~/Downloads/KeePass-2.xx
```

Ja lõpuks, käivitage KeePass Monoga:

```bash
mono KeePass.exe
```

## Kuidas KeePassi installida?

Esimesel käivitamisel saate valida liidese keele.
![KEEPASS](assets/notext/06.webp)
Nõustuge litsentsi tingimustega. ![KEEPASS](assets/notext/07.webp)
Valige kaust, kuhu KeePass installitakse.
![KEEPASS](assets/notext/08.webp)
Võite valikuliselt muuta rakenduse komponente, mis installitakse. Kui teil on piisavalt ruumi, võite lihtsalt valida "*Täisinstallatsioon*".
![KEEPASS](assets/notext/09.webp)
Ja lõpuks võite valida töölauale otsetee lisamise.
![KEEPASS](assets/notext/10.webp)
Klõpsake nuppu "*Installi*".
![KEEPASS](assets/notext/11.webp)
Oodake installimise ajal, seejärel klõpsake nuppu "*Lõpeta*".
![KEEPASS](assets/notext/12.webp)
## Kuidas seadistada KeePassi?

Nüüd jõuate oma KeePassi liidesesse.
![KEEPASS](assets/notext/13.webp)Oma esimese andmebaasi loomiseks klõpsake vahekaardil "*Fail*".
![KEEPASS](assets/notext/14.webp)
Seejärel menüül "*Uus*".
![KEEPASS](assets/notext/15.webp)
Tarkvara loob uue andmebaasi, kuhu teie paroolid salvestatakse. Peate valima selle kausta asukoha. Valige kergesti ligipääsetav asukoht.
![KEEPASS](assets/notext/16.webp)
Seejärel peaksite mõtlema selle kausta regulaarsele varundamisele, et vältida oma volituste kaotamist arvuti kaotuse, kahjustumise või varguse korral. Näiteks võiksite andmebaasi iga nädal USB-pulgale kopeerida. Teie andmebaasi sisaldavat faili nimetatakse `Database.kdbx` (dokument on krüpteeritud teie peaparooliga). Parimate varundamistavade kohta soovitan samuti konsulteerida selle teise õpetusega:

https://planb.network/tutorials/others/general/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Järgneb teie peaparooli valik.
![KEEPASS](assets/notext/17.webp)
Nagu sissejuhatuses nägime, on see parool väga oluline, kuna see annab teile juurdepääsu kõigile teie teistele salvestatud paroolidele andmebaasis. Seda parooli kasutatakse `Database.kdbx` andmebaasi krüpteerimiseks. See esitab kaks peamist riski: kaotus ja kompromiteerimine. Kui kaotate juurdepääsu sellele paroolile, ei saa te enam kõigile oma volitustele juurde pääseda. Kui teie parool varastatakse, saab ründaja lisaks krüpteeritud andmebaasile juurdepääsu kõigile teie kontodele.

Kaotuse riski minimeerimiseks soovitan teha oma peaparoolist füüsilise varukoopia paberil ja hoida seda turvalises kohas. Kui võimalik, pitseerige see varukoopia turvalises ümbrikus, et regulaarselt tagada, et keegi teine pole sellele juurde pääsenud.

Oma peaparooli kompromiteerimise vältimiseks peab see olema äärmiselt tugev. See peaks olema võimalikult pikk, kasutama laia valikut tähemärke ja olema valitud juhuslikult. 2024. aasta minimaalsed soovitused turvalise parooli jaoks on 13 tähemärki, sealhulgas numbrid, väiketähed ja suurtähed, samuti sümbolid, eeldusel, et parool on tõeliselt juhuslik. Siiski soovitan valida vähemalt 20 tähemärgi pikkuse parooli, mis sisaldab kõiki võimalikke tähemärkide tüüpe, et tagada selle turvalisus pikemaks ajaks.

Sisestage oma peaparool vastavasse lahtrisse ja kinnitage see järgmises lahtris, seejärel klõpsake nuppu "*OK*".
![KEEPASS](assets/notext/18.webp)
Nimetage oma andmebaas ja lisage vajadusel kirjeldus. See võib aidata teil eristada erinevaid andmebaase, kui loote mitu, näiteks ühe isiklikuks kasutamiseks ja teise professionaalseks kasutamiseks.
![KEEPASS](assets/notext/19.webp)
Teiste seadete puhul soovitan hoida vaikimisi valikuid. Seejärel klõpsake nuppu "*OK*".
![KEEPASS](assets/notext/20.webp)Seejärel pakub KeePass võimalust printida hädaolukorra leht.
![KEEPASS](assets/notext/21.webp)
Sellel lehel leiate oma andmebaasi asukoha failides, koha, kuhu käsitsi oma peaparooli kirjutada, samuti juhised sellele juurdepääsuks. Seda lehte tuleks usaldada usaldusväärsetele isikutele, kuna see võimaldab juurdepääsu teie volitustele probleemi korral taastada.

Kuna see leht aga annab juurdepääsu teie paroolidele, paljastades teie peaparooli, tuleb seda kasutada ettevaatlikult. On soovitatav hoida seda vähemalt suletud ümbrikus, mis võimaldab perioodilisi kontrolle, et veenduda, kas seda on vaadatud. Te ei ole kohustatud seda lehte kasutama ja võite kaaluda oma lähedaste jaoks muid varundamismeetodeid.
![KEEPASS](assets/notext/22.webp)
Seejärel pääsete juurde oma paroolihaldurile.
![KEEPASS](assets/notext/23.webp)
Enne kui hakkate oma volitusi salvestama, soovitan muuta paroolide genereerimise seadeid. Selleks minge vahekaardile "*Tools*" ja valige "*Generate Password...*".
![KEEPASS](assets/notext/24.webp)
Siin soovitan suurendada genereeritud paroolide pikkust 40 tähemärgini. Nüüd, kui teil on paroolihaldur, kes need teie eest meeles peab, pole põhjust tähemärkide arvu pealt kokku hoida. Lisaks ei pea te paroole käsitsi üles kirjutama, kuna saate neid kopeerida ja kleepida. Seega ei tee see teile vahet, kas teil on väga pikad 40-tähemärgilised paroolid, kuid nende turvalisus on oluliselt suurenenud. Soovitan seda teha ja samuti märkida ruut erimärkide jaoks.
![KEEPASS](assets/notext/25.webp)
Kinnitage, klõpsates väikesel salvestamise ikoonil.
![KEEPASS](assets/notext/26.webp)
Lisage oma parooliprofiilile nimi.
![KEEPASS](assets/notext/27.webp)
## Kuidas oma kontosid KeePassiga turvata?

Uue volituse registreerimiseks oma KeePassi halduris klõpsake lihtsalt võtmikoonil rohelise noolega.
![KEEPASS](assets/notext/28.webp)
Generatsiooni ja salvestamise aknas klõpsake väikesel võtmikoonil ja valige oma 40-tähemärgiline parooliprofiil.
![KEEPASS](assets/notext/29.webp)
Sisestage selle konto kasutajanimi ja pealkiri, et seda oma andmebaasis hõlpsasti leida. ![KEEPASS](assets/notext/30.webp) Samuti on võimalik lisada URL, kui soovite hiljem kasutada otseteid, ja vajadusel märkus. ![KEEPASS](assets/notext/31.webp) Kui kõik on teie rahuloluks, klõpsake parooli salvestamiseks nupul "*OK*". ![KEEPASS](assets/notext/32.webp) Oma KeePassi halduri avalehel leiate oma parooli. ![KEEPASS](assets/notext/33.webp) Parooli kopeerimiseks topeltklõpsake sellel. See jääb teie lõikelauale 12 sekundiks, võimaldades teil selle järgmisel sisselogimisel veebisaidile kleepida. ![KEEPASS](assets/notext/34.webp) Kui soovite pikendada aega, mil parool lõikelauale jääb, klõpsake vahekaardil "*Tööriistad*", seejärel "*Valikud...*". ![KEEPASS](assets/notext/35.webp) Vahekaardil "*Turvalisus*" saate kestust kohandada, muutes sekundite arvu väljal "*Clipboard auto-clear time*". Seejärel klõpsake muudatuste salvestamiseks nupul "*OK*". ![KEEPASS](assets/notext/36.webp) Oma liidese vasakul küljel märkate, et on mitu kausta paroolide organiseerimiseks. ![KEEPASS](assets/notext/37.webp) Teil on võimalus kustutada vaikimisi kaustad või lisada uusi, paremklõpsates ja valides "*Lisa grupp...*". ![KEEPASS](assets/notext/38.webp) Valige uuele kaustale nimi ja valige ikoon. Saate ka importida oma ikoone `.ico` formaadis. Seejärel klõpsake kausta loomise lõpuleviimiseks nupul "*OK*". ![KEEPASS](assets/notext/39.webp) Teie kaust ilmub vasakule. ![KEEPASS](assets/notext/40.webp) Parooli kausta lisamiseks lohistage see lihtsalt andmebaasist soovitud kausta. ![KEEPASS](assets/notext/41.webp) See funktsioon aitab teil oma paroolihaldurit korraldada ja oma mandaate kergemini leida.
Teine viis parooli leidmiseks on kasutada otsingufunktsiooni. Tippige otsinguribale liidese ülaosas identifikaatori pealkiri, mida soovite leida, ja pääsete sellele otse juurde. ![KEEPASS](assets/notext/42.webp) Olge ettevaatlik, kuna KeePass töötab natuke nagu tekstidokument. Enne rakenduse sulgemist, kui olete oma haldurile lisanud uusi üksusi, ärge unustage andmebaasi salvestada. Seda saate teha salvestusikoonil klõpsates või kasutades klaviatuuri otseteed `Ctrl+S`. ![KEEPASS](assets/notext/43.webp)
Kui jätate KeePassi taustal avatuks, ei sulgu tarkvara vaikimisi. Kui aga sulgete KeePassi või lülitate arvuti välja, peate tarkvara uuesti avamisel oma andmebaasi dekrüpteerimiseks sisestama oma peaparooli. ![KEEPASS](assets/notext/44.webp)
See katab KeePassi põhifunktsioonid. Loomulikult on see algajatele mõeldud õpetus vaid põgusalt puudutanud paljusid selle tarkvara saadaolevaid võimalusi. On palju lisafunktsioone, mida uurida, rääkimata [kõigist kogukonna poolt välja töötatud pistikprogrammidest](https://keepass.info/plugins.html), mis võivad KeePassi võimalusi veelgi laiendada.

Kui olete huvitatud õppimast, kuidas oma veebikontode turvalisust 2FA abil oluliselt parandada, et vältida häkkimist, soovitan tutvuda ka selle teise õpetusega:

https://planb.network/tutorials/others/general/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7