---
name: Electrum

description: Täielik Electrumi juhend algajast eksperdiks
---

![kaas](assets/cover.webp)

Kirjeldus Electrumi kohta

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

> "Pean ütlema, kui ma selle juhendi leidsin, olin ma šokeeritud. Palju õnne Arman the Parman'ile selle eest. Oleks olnud kahju, kui seda siin ei oleks majutatud ja tõlgitud võimalikult paljudesse keeltesse. Ausalt, andke sellele tüübile jootraha." Rogzy

Originaalpostitus:

![Electrum Desktop Wallet (Mac / Linux) - laadige alla, kontrollige, ühendage oma noodiga.](https://youtu.be/wHmQNcRWdHM)

![Bitcoin'i tehing Electrumiga](https://youtu.be/-d_Zd7VcAfQ)

## Miks Electrum?

See on üksikasjalik juhend Electrum Bitcoin Wallet'i kasutamiseks, lahendustega kõigile selle lõksudele ja eripäradele - midagi, mida olen välja töötanud pärast mitmeid aastaid kasutamist ja õpilastele Bitcoin'i turvalisuse/privaatsuse õpetamist. Electrum ei ole parim Bitcoin'i rahakott inimesele, kes soovib hoida kõike võimalikult lihtsana ja eelistab jääda algaja tasemele. Selle asemel on see mõeldud inimesele, kes on või soovib saada "võimsaks" kasutajaks.

Uuele Bitcoin'i kasutajale on see suurepärane ainult juhul, kui kogenud kasutaja juhendab neid. Üksi õppides oleks see ohutu, eeldusel, et nad võtavad oma aega ja kasutavad seda testimiskeskkonnas esialgu ainult väikese hulga satoshi'dega. See juhend toetab seda ettevõtmist, kuid on hea viide ka kõigile teistele.

> Hoiatus: See juhend on suur. Ärge üritage seda kõike ühe päevaga teha. On parim salvestada juhend ja aja jooksul järk-järgult läbi töötada.

## Electrumi allalaadimine

Ideaaljuhul kasutage oma Bitcoin'i tehingute jaoks pühendatud Bitcoin'i arvutit (Minu juhend selle kohta https://armantheparman.com/mint/) _(SAMUTI saadaval privaatsuse jaotises)_. Alguses on täiesti sobiv harjutada väikeste summadega "määrdunud" arvutis (kes teab, kui palju peidetud pahavara teie tavaline arvuti aastate jooksul kogunud on – te ei soovi oma Bitcoin'i rahakotte neile paljastada).

Hankige Electrum aadressilt https://electrum.org/.

Klõpsake ülaosas vahekaardil Laadi alla.

Klõpsake allalaadimislingil, mis vastab teie arvutile. Iga Linuxi või Maci arvuti saab kasutada Pythoni linki (punane ring). Linuxi arvuti Intel või AMD kiibiga saab kasutada Appimage'i (roheline ring; see on nagu Windowsi käivitatav fail). Raspberry Pi seadmel on ARM mikroprotsessor ja see saab kasutada ainult Pythoni versiooni (punane ring), mitte Appimage'i, kuigi Pi'd jooksevad Linuxil. Sinine ring on Windowsi jaoks ja must ring Maci jaoks.

![pilt](assets/1.webp)

## Electrumi kontrollimine

Allalaadimise "kontrollimise" eesmärk on veenduda, et ükski bitt andmetest pole muudetud. See hoiab ära "häkitud" pahatahtliku tarkvara versiooni kasutamise. Selle võib vahele jätta, eeldusel, et kasutate allalaaditud koopiat ainult harjutamiseks, st. ärge kasutage rahakotte, mis hoiavad tõsist raha. Kui olete valmis Electrumi kasutama oma tegelike vahendite jaoks, peaksite oma koopia kustutama ja alustama otsast peale, kontrollides seekord oma allalaadimist.
Selleks kasutame avaliku/privaatvõtme krüptograafia tööriistu – gpg, mille kohta oleme kirjutanud juhendi siin (https://armantheparman.com/gpg/). Gpg tööriist on saadaval kõikides Linuxi operatsioonisüsteemides. Maci ja Windowsi jaoks vaadake gpg linki allalaadimisjuhiste jaoks.

Lisaks Electrum tarkvara allalaadimisele on turvalisuse huvides vajalik ka tarkvara DIGITAALNE ALLKIRI. See on tekstijada (tegelikult on see number, mis on kodeeritud tekstina), mille arendaja on loonud oma PRIVAATSE gpg võtmega. Kasutades gpg programmi, saame seejärel "testida" ALLKIRJA tema AVALIKU võtmega (mis on loodud arendaja privaatvõtmest), millele kõigil on juurdepääs, võrreldes allalaaditud FAILIGA.

Teisisõnu, kolme sisendi (allkiri, avalik võti ja andmefail) abil saame tõese või vääratulemuse, et kinnitada, et failiga ei ole manipuleeritud.

Allkirja saamiseks klõpsake faili, mille olete alla laadinud, vastaval lingil (vt värvilisi nooli):

![image](assets/2.webp)

Lingil klõpsates võib fail automaatselt alla laadida teie allalaadimiskausta või see võib avaneda brauseris. Kui see avaneb brauseris, peate faili salvestama. Saate paremklõpsata ja valida „salvesta nimega“. Olenevalt operatsioonisüsteemist või brauserist võib teil olla vaja paremklõpsata valgel alal, mitte tekstil.

Allpool on näha, milline näeb välja allalaaditud tekst. Näete, et seal on mitu allkirja – need on erinevate inimeste allkirjad. Võite kontrollida igaüht või mõnda. Ma näitan teile, kuidas kontrollida ainult arendaja oma.

![image](assets/3.webp)

Järgmisena peate saama ThomasV avaliku võtme – ta on peamine arendaja. Saate selle otse temalt, tema Keybase kontolt, Githubist või kellegi teise käest, võtmehoidlast või Electrumi veebisaidilt.

Selle saamine Electrumi veebisaidilt on tegelikult kõige vähem turvaline viis, sest kui see veebisait on pahatahtlik (just see, mida me kontrollime), miks me saame avaliku võtme just sellelt (avalik võti võib olla võlts)?

Praegu lihtsuse huvides näitan teile siiski, kuidas seda veebisaidilt saada, kuid pidage seda meeles. Siin on koopia (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) GitHubis, mida saate võrrelda.

Kerige lehte veidi allapoole, et leida link ThomasV avalikule võtmele (allpool punane ring). Klõpsake seda ja laadige alla või kui see avab brauseris mõne teksti, paremklõpsake salvestamiseks.

![image](assets/4.webp)

Nüüd on teil 3 uut faili, tõenäoliselt kõik allalaadimiskaustas. Pole oluline, kus need asuvad, kuid protsessi lihtsustamiseks on parem, kui panete need kõik samasse kausta.

Kolm faili:

1. Electrumi allalaadimine
2. Allkirjafail (tavaliselt on see sama failinimi nagu Electrumi allalaadimisel, lisatud ".asc")
3. ThomasV avalik võti.

Avage terminal Macis või Linuxis või käsurida (CMD) Windowsis.

Liikuge allalaadimiskausta (või sinna, kuhu panite kolm faili). Kui te ei tea, mida see tähendab, õppige sellest lühikesest videost Linuxi/Maci jaoks (https://www.youtube.com/watch?v=AO0jzD1hpXc) ja sellest Windowsi jaoks (https://www.youtube.com/watch?v=9zMWXD-xoxc). Pidage meeles, et Linuxi arvutites on katalooginimed tõstutundlikud.
Terminalis tippige see, et importida ThomasV avalik võti oma arvuti "võtmehoidlasse" (võtmehoidla on abstraktne mõiste – tegelikult on see lihtsalt fail teie arvutis):
```bash
gpg --import ThomasV.asc
```

Veenduge, et failinimi ühtib sellega, mida olete alla laadinud. Pange tähele, et tegemist on kahekordse sidekriipsuga, mitte ühekordsega. Samuti pange tähele, et enne ja pärast “--import” on tühik. Seejärel vajutage <enter>.

Fail peaks importima. Kui saate veateate, kontrollige, kas olete kataloogis, kus fail tegelikult asub. Praeguses kataloogis olemise kontrollimiseks (Macis või Linuxis) tippige pwd. Praeguses kataloogis olevate failide nägemiseks (Macis või Linuxis) tippige ls. Peaksite nägema tekstifaili “ThomasV.asc”, võimalik, et teiste failide seas.

Seejärel käivitame käsu allkirja kontrollimiseks.

```bash
gpg --verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Pange tähele, et siin on 4 “elementi”, igaüks eraldatud tühikuga. Ma olen teksti vaheldumisi rasvases kirjas esile tõstnud, et aidata teil näha. Neli elementi on:

1. gpg programm
2. --verify valik
3. allkirjafaili failinimi
4. programmi failinimi

Huvitav on see, et mõnikord võite jätta ära 4. elemendi ja arvuti arvab, mida te mõtlete. Ma pole kindel, aga usun, et see töötab ainult siis, kui failinimed erinevad ainult lõpus oleva “asc” poolest.

Ärge lihtsalt kopeerige failinimesid, mida siin näitasin – veenduge, et need ühtiksid teie süsteemis oleva faili nimega.

Vajutage <enter>, et käsk käivitada. Peaksite nägema “good signature from ThomasV”, mis näitab edu. Ilmnevad mõned vead, kuna meil pole teiste inimeste allkirjade avalikke võtmeid, mis on allkirjafailis (see allkirjade ühes failis kombineerimise süsteem võib hilisemates versioonides muutuda). Samuti on allpool hoiatus, mida me võime ignoreerida (see hoiatab meid, et me pole arvutile selgesõnaliselt öelnud, et usaldame ThomasV avalikku võtit).

Nüüd on meil kontrollitud Electrumi koopia, mida on ohutu kasutada.

## Electrumi käivitamine

### Electrumi käivitamine, kui kasutate Pythonit

Kui olete alla laadinud Pythoni versiooni, siis nii see töötab. Allalaadimislehel näete seda:

![image](assets/5.webp)

Linuxi puhul on hea mõte esmalt oma süsteemi uuendada:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Kopeerige esile tõstetud kollane tekst, kleepige see terminali ja vajutage <enter>. Teilt küsitakse teie parooli, võimalik, et kinnitust jätkamiseks, ja seejärel installitakse need failid (“sõltuvused”).

Peate ka lahtipakitud faili ekstraktima valitud kataloogi. Seda saab teha graafilise kasutajaliidese kaudu või käsurealt (roosaga esile tõstetud käsk) – pidage meeles, et teie failinimed võivad erineda. (Pange tähele, et kui me eelmises jaotises allalaadimist kontrollisime, kontrollisime zip-faili, mitte ekstraktitud kataloogi.)

On võimalus “installida” kasutades PIP programmi, kuid see on tarbetu ja lisab lisasamme ning failide installimist. Lihtsalt käivitage programm terminali kaudu, et kõik see vahele jätta.

Sammud (Linux) on:

1. navigeerige kataloogi, kus failid on ekstraktitud
2. tippige: ./run_electrum

Macis on sammud samad, kuid võib-olla peate esmalt installima Python3 ja kasutama käsku käivitamiseks:

```bash
```bash
python3 ./run_electrum
```

Kui Electrum on käivitatud, jääb terminaliaken avatuks. Kui te selle sulgete, lõpetab see Electrumi programmi. Lihtsalt minimeerige see, kasutades Electrumit.

### Electrumi käivitamine Appimage'iga

See on natuke lihtsam, kuid mitte nii lihtne kui Windowsi käivitatav fail. Olenevalt teie Linuxi versioonist võivad Appimage failidel vaikimisi olla atribuudid seatud nii, et süsteem ei luba neid käivitada. Me peame seda muutma. Kui teie Appimage töötab, võite selle sammu vahele jätta. Liikuge terminali kasutades faili asukohta, seejärel käivitage see käsk:

```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

“sudo” annab superkasutaja õigused; “chmod” on käsk režiimi muutmiseks, muutes, kes saab lugeda, kirjutada või käivitada; “ug+x” tähendab, et me muudame kasutaja ja grupi õigusi, lubades käivitamist.

Kohandage failinime, et see vastaks teie versioonile.

Seejärel saab Electrumi käivitada, topeltklõpsates Appimage ikoonil.

### Electrumi käivitamine Maciga

Lihtsalt topeltklõpsake allalaaditud failil (see on “draiv”). Avaneb aken. Lohistage Electrumi ikoon aknas oma töölauale või sinna, kuhu soovite programmi hoida. Seejärel saate “väljutada” draivi ja kustutada draivi (allalaaditud faili).

Programmi käivitamiseks lihtsalt topeltklõpsake seda. Võite saada mõned Maci-spetsiifilised “hoidja” veateated, mida tuleb eirata.

### Electrumi käivitamine Windowsiga

Hoolimata sellest, et ma vihkan Windowsit kõige rohkem, on see kõige lihtsam meetod. Lihtsalt topeltklõpsake käivitataval failil, et seda käivitada.

## Alustage dummy rahakotiga

Kui laadite Electrumi esimest korda, avaneb aken nagu see:

![image](assets/6.webp)

Hiljem valime teie serveri käsitsi, kuid praegu jätke vaikimisi ja ühendage automaatselt.

Seejärel looge dummy rahakott – ärge kunagi pange sellesse rahakotti vahendeid. Selle dummy rahakoti eesmärk on läbida tarkvara ja veenduda, et kõik töötab hästi enne, kui laadite oma päris rahakoti. Me üritame vältida privaatsuse kogemata loovutamist päris rahakotiga. Kui te lihtsalt harjutate, võib loodud rahakotti pidada niikuinii dummy rahakotiks.

Võite jätta nimeks “default_wallet” või muuta selle milleks iganes soovite ja klõpsake järgmine. Hiljem, kui teil on mitu rahakotti, saate neid selles etapis leida ja avada, klõpsates esmalt “Choose…”

![image](assets/7.webp)

Valige “Standard wallet” ja <Next>:

![image](assets/8.webp)

Seejärel valige “I already have a seed”. Ma ei taha, et te harjuksite looma Electrumi seemet, kuna see kasutab oma protokolli, mis ei ühildu teiste rahakottidega – seetõttu me ei klõpsa “new seed”.

![image](assets/9.webp)

Minge aadressile https://iancoleman.io/bip39/ ja looge dummy seeme. Kõigepealt muutke sõnade arvu 12-ks (mis on tavaline praktika), seejärel klõpsake “generate” ja kopeerige kastis olevad sõnad lõikelauale.

![image](assets/10.webp)

Seejärel kleepige sõnad Electrumisse. Siin on näide:

![image](assets/11.webp)

Electrum otsib sõnu, mis vastavad oma protokollile. Me peame sellest mööda minema. Klõpsake valikutel ja valige BIP39 Seed:

![image](assets/12.webp)
Seeme muutub seejärel kehtivaks. (Enne seda ootas Electrum Electrumi seemet, seega seda seemet peeti kehtetuks). Enne järgmisele klõpsamist pange tähele teksti, mis ütleb "Checksum OK". See on oluline (tegeliku rahakoti puhul, mida võite hiljem kasutada), et näeksite seda enne jätkamist, kuna see kinnitab sisestatud seemne kehtivust. Hoiatus allpool võib jääda tähelepanuta, see on Electrumi arendajate nurin BIP39 ja nende "FUD'ey" väidete üle, et nende versioon (mis ei ühildu teiste rahakottidega) on parem.

> Kiire kõrvalepõige oluliseks hoiatuseks. Kontrollsumma eesmärk on veenduda, et olete oma seemne sisestanud ilma trükivigadeta. Kontrollsumma on seemne viimane osa (12. sõna on kontrollsumma sõna), mis matemaatiliselt määratakse seemne esimese osa (11 sõna) järgi. Kui te alustuses midagi valesti tippiksite, ei klapi kontrollsumma sõna matemaatiliselt ja rahakoti tarkvara hoiatab teid hoiatusega. See ei tähenda, et seemet ei saaks kasutada funktsionaalse Bitcoin Wallet'i loomiseks. Kujutage ette, et loote rahakoti trükiveaga, laadite rahakoti bitcoinidega ja ühel päeval võib teil tekkida vajadus rahakott taastada, kuid kui te seda teete, ei taasloo te trükiviga – taastate vale rahakoti! On üsna ohtlik, et Electrum lubab teil jätkata rahakoti tegemist, kui teie kontrollsumma on kehtetu, seega olge hoiatatud, see on teie vastutus veenduda. Teised rahakotid ei lase teil jätkata, mis on palju turvalisem. See on üks asju, mida ma mõtlen, kui ütlen, et Electrumi kasutamine on korras, kui õpite seda õigesti kasutama (Electrumi arendajad peaksid selle parandama).

Pange tähele, et kui soovite lisada paroolilause, on selle valimise võimalus selles valikute aknas, kohe üleval.

OK klõpsamise järel viiakse teid tagasi kohta, kus tippisite seemnefraasi. Kui valisite paroolilause valiku, EI sisesta te seda seemnesõnadega (selle jaoks tuleb järgmine viip).

Kui te ei palunud paroolilauset, näete järgmisena seda ekraani – rohkem valikuid teie rahakoti skripti tüübi ja tuletustee kohta, mille kohta saate lugeda siit (https://armantheparman.com/public-and-private-keys/), kuid lihtsalt jätke vaikimisi seaded ja jätkake.

![image](assets/13.webp)

> Lisainfo jaoks: Esimene valik võimaldab teil valida legacy (aadressid algavad "1"), pay-to-script-hash (aadressid algavad "3") või bech32/native segwit (aadressid algavad "bc1q") vahel. Kirjutamise hetkel ei toeta Electrum veel taprooti (aadressid algavad "bc1p"). Teine valik selles aknas võimaldab teil muuta tuletusteed. Soovitan seda mitte kunagi muuta, eriti enne, kui mõistate, mida see tähendab. Inimesed rõhutavad tuletustee üleskirjutamise tähtsust, et saaksite vajadusel oma rahakoti taastada, kuid kui jätate selle vaikimisi, siis tõenäoliselt saate hakkama, nii et ärge paanitsege – kuid siiski on hea tava tuletustee üles kirjutada.

Järgmisena antakse teile võimalus lisada PAROOL. See ei ole segamini ajada "PAROOLILAUSEGA". Parool lukustab faili teie arvutis. Paroolilause on osa privaatvõtme koostisest. Kuna see on dummy rahakott, võite parooli tühjaks jätta ja jätkata.

![image](assets/14.webp)
Teile kuvatakse hüpikaken uue versiooni teavitustega (soovitan valida ei). Seejärel genereerib rahakott ise end ja on kasutusvalmis (aga pidage meeles, et see rahakott on mõeldud kustutamiseks, see on lihtsalt dummy rahakott).
![image](assets/15.webp)

On mõned asjad, mida soovitan teil teha, et seadistada tarkvarakeskkond (vajalik ainult üks kord):

### Muutke ühikud BTC-ks

Minge ülemisele menüüle, tööriistad –> electrum eelistused, ja seal üldkaardi all leiate võimaluse muuta "baasühik" BTC-ks.
Luba Aadresside ja Müntide vaheleht

Minge ülemisele menüüle, vaade ja valige "näita aadresse". Seejärel minge tagasi vaatesse ja valige "näita münte".

### Luba Oneserver

Vaikimisi ühendub Electrum juhusliku sõlmega. See ühendub ka paljude teiste sekundaarsete sõlmedega. Ma pole kindel, milliseid andmeid nende sekundaarsete sõlmedega vahetatakse, kuid me ei soovi, et see juhtuks, privaatsuse huvides. Isegi kui määrate sõlme, näiteks oma sõlme, ühendatakse ka mitmete teiste sõlmedega ja ma pole kindel, millist teavet jagatakse. Sellest hoolimata on seda lihtne vältida. Enne kui näitan teile, kuidas määrata oma sõlm, sunnime Electrumi ühenduma korraga ainult ühe serveriga.

> Seda saab teha käsurealt määrates "oneserver", kuid ma ei soovita seda viisi. Ma näitan alternatiivi, mis ma arvan, et on pikas perspektiivis lihtsam ja tõenäolisem, et ei lase teil kogemata teiste sõlmedega ühenduda.

Põhjus, miks kasutame dummy rahakotti, on see, et kui oleksime laadinud oma päris rahakoti, oma päris bitcoinidega, oleksime nüüdseks juhusliku sõlmega tahtmatult ühendunud (isegi kui valisime alguses "määra server käsitsi", ühendub see siiski mingil põhjusel nende teiste sekundaarsete sõlmedega (hei Electrumi arendajad, peaksite seda parandama). Kui meie rahakott oleks privaatne, oleks see katastroof.

Samuti ei saa me allpool näidatud samme teha ilma esmalt mingit tüüpi rahakotti laadimata. (Me kavatseme redigeerida konfiguratsioonifaili, mis saab täidetud ja redigeerimiseks valmis alles pärast rahakoti laadimist).

**Sulgege Electrum (OLULINE, kui te seda ei tee, kustutatakse järgmised tehtavad muudatused).**

### LINUX/MAC Konfiguratsioonifail

Avage terminal Linuxis või Macis (Windowsi juhised hiljem):

Te peaksite automaatselt olema kodukaustas. Sealt navigeerige peidetud electrumi seadete kausta (see erineb rakenduse asukohast).

```bash
cd .electrum
```

Märkige punkt enne "electrum", mis näitab, et see on peidetud kaust.

Teine viis sinna jõudmiseks on tippida:

```bash
cd ~/.electrum
```

kus "~" tähistab teie kodukataloogi teed. Praeguse kataloogi täieliku tee näete käsu "pwd" abil.

Olles ".electrum" kataloogis, tippige "nano config" ja vajutage <enter>.

Tekstiredaktor avaneb (nimega nano) konfiguratsioonifailiga avatuna. Hiir siin palju ei tööta. Kasutage nooleklahve, et jõuda reani, mis ütleb:

```json
"oneserver": false,
```

Muutke "false" "true"-ks; ja ärge rikkuge süntaksit (ärge kustutage koma ega semikoolonit).

Vajutage <ctrl> x, väljumiseks, seejärel "y" salvestamiseks, seejärel <enter>, mis kinnitab muudatuste tegemist ilma failinime muutmata.
Nüüd käivitage Electrum uuesti. Seejärel klõpsake alumises paremas nurgas olevat ringi, mis avab võrguseaded. Seejärel näete ülevaate vahelehel ülaosas "ühendatud 1 sõlmega" - see näitab, et ühendus on edukas.
Just selle all näete tekstivälja ja seal on serveri aadress. Praegu olete ühendatud selle juhusliku sõlmega. Järgmises jaotises räägime rohkem sõlmele ühendamisest.

### Windowsi konfiguratsioonifail

Windowsi konfiguratsioonifaili leidmine on natuke keerulisem. Kataloog on: `C:/Users/Parman/AppData/Roaming/Electrum`

Ilmselgelt peate "Parman" asendama oma arvuti kasutajanimega.

Sel kaustas leiate konfiguratsioonifaili. Avage see tekstiredaktoriga ja muutke rida:

```json
"oneserver": false,
```

Muutke "false" "true"-ks; ärge rikkuge süntaksit (ärge kustutage koma või semikoolonit).

Seejärel salvestage fail ja väljuge.

## Ühendage Electrum sõlmega

Järgmisena soovime ühendada meie proovirahakoti valitud sõlmega. Kui te pole veel valmis sõlme käitama, võite teha ühe järgmistest:

1. Ühendage sõbra isikliku sõlmega (nõuab Tor-i)
2. Ühendage usaldusväärse ettevõtte sõlmega
3. Ühendage juhusliku sõlmega (ei ole soovitatav).

Muuseas, siin on juhised oma sõlme käitamiseks ja need on põhjused, miks peaksite seda tegema (kõik õpetused sõlme jaotises või meie tasuta kursustel).

### Ühendage sõbra sõlmega Tor-i kaudu (Juhend tulekul.)

### Ühendage usaldusväärse ettevõtte sõlmega

Selleks ainus põhjus oleks, kui peate pääsema juurde plokiahelale ja teil pole oma sõlme saadaval (või sõbra oma).

Ühendame Bitaroo sõlmega - Meile on öeldud, et nad ei kogu andmeid. Nad on ainult Bitcoiniga tegelev vahetusplatvorm, mida juhib kirglik Bitcoin'i toetaja. Nendega ühendamine nõuab natuke usaldust, kuid see on parem kui ühendamine juhusliku sõlmega, mis võib olla jälgimisettevõte.

Pääsete võrguseadetele ligi, klõpsates rahakna alumises paremas osas olevat ringi (punane näitab, et pole ühendatud, roheline näitab, et on ühendatud ja sinine näitab, et on ühendatud Tor-i kaudu).

![image](assets/16.webp)

Kui klõpsate ringi ikoonil, ilmub hüpikaken: Teie rahakott näitab "ühendatud 1 sõlmega", kuna me sundisime seda varem.

Tühjendage märkeruut "vali server automaatselt" ja seejärel Serveri väljal tippige Bitaroo üksikasjad nagu näidatud:

![image](assets/17.webp)

Sulgege aken ja nüüd peaksime olema ühendatud Bitaroo sõlmega. Kinnitamiseks peaks ring olema roheline. Klõpsake seda uuesti ja kontrollige, et serveri üksikasjad poleks muutunud tagasi juhuslikuks sõlmeks.

### Ühendage oma sõlmega

Kui teil on oma sõlm, on see suurepärane. Kui teil on ainult Bitcoin Core ja mitte Electrum SERVER, siis te ei saa veel Electrum WALLET'it oma sõlmega ühendada.

> Märkus: Electrum Server ja Electrum Wallet on erinevad asjad. Server on tarkvara, mis on vajalik selleks, et Electrum Wallet saaks suhelda Bitcoin'i plokiahelaga - ma ei tea, miks see nii kujundati - võib-olla kiiruse pärast, aga ma võin eksida.
Kui käitate sõlmetarkvara paketti nagu MyNode (mida ma soovitan inimestel alustuseks kasutada), Raspiblitz (soovitatav, kui muutute edasijõudnumaks) või Umbrel (isiklikult ei soovita veel, kuna olen kogenud liiga palju probleeme), siis saate oma rahakoti lihtsalt ühendada, sisestades arvuti (Raspberry Pi) IP-aadressi, mis jooksutab sõlme, pluss koolon ja 50002, nagu on näidatud eelmises jaotises olevas pildis. (Allpool näitan teile, kuidas leida oma sõlme IP-aadressi).

Avage võrguseaded (klõpsake alumises paremas nurgas rohelist või punast ringi). Eemaldage linnuke "vali server automaatselt" ruudust, seejärel sisestage oma IP-aadress, nagu mina olen teinud, teie oma on erinev, kuid koolon ja "50002" peaksid olema samad.

![image](assets/18.webp)

Sulgege aken ja nüüd peaksime olema teie sõlmega ühendatud. Kinnitamiseks klõpsake ringi uuesti ja kontrollige, et serveri andmed poleks tagasi muutunud suvaliseks sõlmeks.

Mõnikord, hoolimata kõigest õigesti tegemisest, tundub, et ühendus ei toimi. Siin on asjad, mida proovida...

- Uuendage Electrumi ja oma sõlmetarkvara uuemale versioonile
- Proovige kustutada vahemälu kausta ".electrum" kataloogis
- Proovige võrguseadetes porti muuta 50002-lt 50001-le
- Kasutage Tori kaudu ühenduse loomiseks seda juhendit alternatiivina (https://armantheparman.com/tor/)
- Installige sõlmele Electrum Server uuesti

## OMA SÕLME IP-AADRESSI LEIDMINE

IP-aadress ei ole midagi, mida tavaline kasutaja tavaliselt teab, kuidas otsida ja kasutada. Olen aidanud paljudel inimestel sõlme käitada ja seejärel oma rahakotid sõlmega ühendada – tõrkeotsinguks tundub tihti olevat selle IP-aadressi leidmine.

MyNode'i jaoks saate brauseriaknas tippida: `mynode.local`

Mõnikord "mynode.local" ei tööta (veenduge, et te ei tippiks seda Google'i otsinguribale. Et sundida navigeerimisriba tajuma teie teksti aadressina, mitte otsinguna, eelnege tekstiga `http://` nagu see: `http://mynode.local`. Kui see ei tööta, proovige seda "s"-ga, nagu see: `https://mynode.local`.

See võimaldab seadmele juurdepääsu ja saate klõpsata seadete lingil (vaadake allpool minu sinist "ringi"), et näidata seda ekraani, kus asub IP-aadress:

![image](assets/19.webp)

See leht laaditakse ja näete sõlme IP-d (sinine "ring")

![image](assets/20.webp)

Siis tulevikus saate tippida 192.168.0.150 või http://192.168.0.150 oma brauserisse.

Raspiblitz'i jaoks (kui ei ühendata ekraani), on vaja erinevat meetodit (mis töötab ka MyNode'i jaoks):

Logige sisse oma ruuteri veebilehele – siit leiame kõigi ühendatud seadmete IP-aadressid. Ruuteri veebileht on IP-aadress, mille sisestate veebibrauserisse. Minu oma on:

    http://192.168.0.1

Ruuteri sisselogimisandmete saamiseks võite vaadata kasutusjuhendit või mõnikord isegi ruuteri enda peal olevat kleebist. Otsige kasutajanime ja parooli. Kui te seda ei leia, proovige Kasutaja: "admin" Parool: "password"

Kui olete sisse logitud, näete oma ühendatud seadmeid ja nende nimede põhjal võib olla selge, milline on teie sõlm. IP-aadress on seal.
### Kui esimesed kaks meetodit ebaõnnestuvad, siis viimane töötab, kuid see on tüütu:
Esmalt leidke oma võrgus oleva seadme IP-aadress (praegune arvuti sobib).

Macis leiate selle võrgueelistustest:

![image](assets/21.webp)

Meid huvitavad esimesed 4 elementi (192.168.0), mitte neljas element, "166", mida näete pildil (teie oma erineb).

Linuxi puhul kasutage käsurida:

```bash
ifconfig | grep inet
```

See vertikaalne joon on "pipe" sümbol ja leiate selle <delete> klahvi alt. Näete mõningast väljundit ja IP-aadressi. (Ignoreerige 127.0.0.1, see pole see, ja ignoreerige ka võrgumaski)

Windowsis avage käsuviip (cmd) ja tippige:

```bash
ipconfig/all
```

ja vajutage Enter. IP-aadressi leiate väljundist.

See oli lihtne osa. Raske osa on nüüd leida teie sõlme IP-aadress – me peame pakkuma brute-force meetodil. Oletame näiteks, et teie arvuti IP-aadress algab 192.168.0.xxx-ga, siis oma sõlme jaoks proovige brauseris: `https://192.168.0.2`

Väikseim võimalik number on 2 (0 tähendab ükskõik millist seadet ja 1 kuulub ruuterile) ja suurim, ma usun, on 255 (see juhtub olema 11111111 binaarkoodis, suurim number, mida 1 bait suudab hoida).

Ükshaaval töötage oma teed ülespoole 255 suunas. Lõpuks peatute õigel numbril, mis laadib teie MyNode lehe (või RaspiBlitz lehe). Siis teate, millist numbrit sisestada oma Electrumi võrguseadetes, et ühenduda oma sõlmega.

See näeb välja umbes selline (veenduge, et lisate järel kooloni ja numbri):

![image](assets/22.webp)

> On kasulik teada, et need IP-aadressid on SISESED teie koduvõrgus. Keegi väljaspool ei saa neid näha ja need ei ole tundlikud. Need on nagu telefonilaiendid suures organisatsioonis, mis suunavad teid erinevatele telefonidele.

## Kustuta mängurahakott

Nüüd oleme edukalt ühendatud ainult ühe sõlmega. Nii laadib Electrum vaikimisi edaspidi. Peaksite nüüd kustutama mängurahakoti (Menüü: fail –> kustuta), juhul kui saadate kogemata vahendeid sellele ebaturvalisele rahakotile (See on ebaturvaline, kuna me ei loonud seda turvalisel viisil).

## Tee harjutusraha rahakott

Pärast mängurahakoti kustutamist alustage uuesti ja tehke uus, samal viisil, ainult seekord kirjutage üles seemnefraasid ja hoidke neid suhteliselt turvaliselt.

On hea mõte õppida, kuidas Electrum töötab selle harjutusraha rahakotiga, ilma tülikate riistvararahakottideta (mis on vajalikud kõrge turvalisuse jaoks). Pange sellesse rahakotti ainult väike summa bitcoini – eeldage, et kaotate selle raha. Kui olete osav, õppige siis kasutama Electrumi koos riistvararahakotiga.

Uues rahakotis, mille olete loonud, näete aadresside loendit. Rohelisi nimetatakse "vastuvõtu aadressideks". Need on kolme asja tulemus:

- Seemnefraas
- Paroolifraas
- Tuletustee

Teie uuel rahakotil on vastuvõtu aadresside komplekt, mida saab matemaatiliselt ja korduvalt luua igas tarkvararahakotis, mis omab seemet, paroolifraasi ja tuletusteed. Neid on 4,3 miljardit! Rohkem kui vajate. Electrum näitab teile esimesi 20 ja seejärel rohkem, kui kasutate esimesi ära.
Rohkem teavet Bitcoin'i privaatvõtmete kohta leiate sellest juhendist.
![image](assets/23.webp)

See erineb oluliselt mõnest teisest rahakotist, mis esitavad korraga ainult ühe aadressi.

Kuna sisestasite rahakoti loomisel seemnefraasi, on Electrumil iga aadressi privaatvõti ja nende aadresside kasutamine on võimalik.

Pange tähele, et on olemas ka kollased aadressid, mida nimetatakse "vahetus aadressideks" – need on lihtsalt teine aadresside komplekt erinevast matemaatilisest harus (neid on veel 4,3 miljardit). Rahakott kasutab neid automaatselt ülejääva raha tagasi rahakotti saatmiseks vahetusrahana. Näiteks, kui võtate 1,5 bitcoini ja kulutate 0,5 kaupmehele, peab ülejäänud 1,0 kuhugi minema. Teie rahakott kulutab selle järgmisele tühjale kollasele vahetus aadressile – vastasel juhul läheb see kaevurile! Lisateabe saamiseks selle kohta (UTXO-d) vaadake seda juhendit. (https://armantheparman.com/utxo/)

Järgmisena minge tagasi Ian Colmani privaatvõtme veebisaidile ja sisestage seeme (selle genereerimise asemel). Näete allpool, et privaat- ja avaliku võtme teave muutub; kõik allpool sõltub lehekülje ülaosas olevast.

> Pidage meeles, et te ei tohiks "kunagi" sisestada seemet oma päris Bitcoin'i rahakoti jaoks arvutisse – pahavara võib selle varastada. Me kasutame lihtsalt harjutamiseks mõeldud rahakotti, seega praegu on see korras.

Kerige alla ja muutke tuletusteed BIP84 (segwit) vastavaks teie Electrumi rahakotiga, klõpsates BIP84 vahekaardil.

![image](assets/24.webp)

Selle all näete konto laiendatud privaatvõtit ja konto laiendatud avalikku võtit:

![image](assets/25.webp)

Minge Electrumisse ja võrrelge, et need ühtivad. Üleval on menüü, rahakott –> teave:

![image](assets/26.webp)

See hüppab üles:

![image](assets/27.webp)

Pange tähele, et kaks avalikku võtit ühtivad.

Järgmisena võrrelge aadresse. Minge tagasi Ian Colemani saidile ja kerige alla:

![image](assets/28.webp)

Pange tähele, et need ühtivad Electrumi aadressidega.

Nüüd kontrollime vahetus aadresse. Kerige natuke üles tuletustee juurde ja muutke viimane 0 üheks:

![image](assets/29.webp)

Nüüd kerige alla ja võrrelge, et aadressid ühtivad Electrumi kollaste aadressidega

Miks me seda tegime?

Võtsime seemnesõnad ja panime need läbi kahe erineva sõltumatu tarkvaraprogrammi, et veenduda, et need annavad meile sama teabe. See vähendab oluliselt riski, et pahatahtlik kood varitseb sees ja annab meile valesid privaat- või avalikke võtmeid või aadresse.

Järgmine samm on vastu võtta väike test ja kulutada see rahakotis ühelt aadressilt teisele.

## Rahakoti testimine (õppige seda kasutama)

Siin näitan teile, kuidas vastu võtta UTXO oma rahakotti ja seejärel liigutada seda (kulutada) teisele aadressile rahakotis. See on väga väike summa, mille kaotamise pärast me ei muretse.

Sellel on mitu eesmärki.

- See tõestab, et teil on võim uues rahakotis münte kulutada.
- See demonstreerib, kuidas kasutada Electrumi tarkvara kulutuse tegemiseks (ja mõningaid funktsioone), enne kui lisame ohutuse huvides lisakomplekssust (kasutades riistvara rahakotti või õhulõhega arvutit)
- See tugevdab mõtet, et teil on palju aadresse, mille vahel valida, et vastu võtta ja kulutada, samas rahakotis.
Ava oma test Electrum Rahakott ja klõpsa aadresside vahekaardil, seejärel paremklõpsa esimesel aadressil ja vali Kopeeri –> Aadress:
![image](assets/30.webp)

Aadress on nüüd sinu arvuti mälus.

Mine nüüd vahetusplatvormile, kus sul on mõningaid bitcoine, ja võtame välja väikese summa sellele aadressile, ütleme 50 000 satsi. Ma kasutan näitena Coinbase'i, kuna see on kõige levinum vahetusplatvorm, kuigi nad on Bitcoinile vaenulikud, ja mul on vastumeelne sisse logida vanasse hüljatud kontosse selleks otstarbeks.

Logi sisse ja klõpsa nupul Saada/Vasta, mis tänase seisuga asub veebilehe paremas ülanurgas.

![image](assets/31.webp)

Ilmselgelt pole mul Coinbase'is vahendeid, kuid kujuta ette, et siin on vahendid ja järgi juhiseid: Kleebi aadress Electrumist "Saaja" väljale, nagu ma olen teinud. Samuti pead valima summa (soovitan umbes 50 000 satsi). Ära pane "valikulist sõnumit" – Coinbase kogub piisavalt sinu andmeid (ja müüb neid), pole vaja neid aidata. Lõpuks klõpsa "Jätka". Pärast seda ma ei tea, milliseid hüpikaknaid sa veel saad, oled iseenda hooleks, kuid meetod on sarnane kõikide vahetusplatvormide puhul.

![image](assets/32.webp)

Sõltuvalt vahetusplatvormist võid sa näha satse oma rahakotis kohe või mõne tunni/päeva viivitusega.

Pane tähele, et Electrum näitab sulle saabunud münte isegi siis, kui need pole blockchainis kinnitatud. Sinu omatavad mündid loetakse Bitcoin Node'i ootelolevate nimekirjast ehk "mempoolist". Kui need jõuavad blokki, näed sa vahendeid kinnitatuna.

Nüüd, kui meil on meie rahakotis UTXO, peaksime selle märgistama. Ainult meie näeme seda märgistust, see pole avaliku pearaamatu jaoks oluline. Kõik meie Electrumi märgistused on nähtavad ainult arvutis, mida kasutame. Tegelikult saame salvestada faili ja kasutada seda kõigi meie märgistuste taastamiseks teises arvutis, kus töötab sama rahakott.

### Tee UTXO-le märgistus

Mul oli vaja annetust sellele test rahakotile, tänu @Sathoarder'ile, kes andis mulle elava UTXO (10 000 satsi), ja teine isik (anonüümne) annetas samale aadressile (5000 satsi). Pane tähele, et esimese aadressi saldo on 15 000 satsi ja kokku on 2 tehingut (parempoolses veerus). Allpool on saldo 10 000 satsi kinnitatud ja veel 5000 satsi on kinnitamata (endiselt mempoolis).

![image](assets/33.webp)

Nüüd, kui läheme mündi vahekaardile, näeme kahte "saabunud münti" ehk UTXO-d. Mõlemad on samal aadressil.

![image](assets/34.webp)

Tagasi aadressi vahekaardile minnes, kui topeltklõpsad "märgistuste" alal aadressi kõrval, saad sisestada teksti, seejärel vajuta <enter>, et salvestada:

![image](assets/35.webp)

See on hea praktika, et saaksid jälgida, kust su mündid pärinevad, kas need on KYC-vabad või mitte, ja kui palju iga UTXO sind maksma läks (juhul, kui pead müüma ja arvutama maksu, mis sinult valitsuse poolt varastatakse).
Ideaaljuhul peaksite vältima mitme mündi kogunemist samale aadressile. Kui otsustate seda siiski teha (mis ei ole soovitatav), saate iga mündi märgistada eraldi, kasutades aadressi meetodit, mitte märgistada kõiki sama sildiga. Tegelikult ei saa te minna "müntide" vahekaardile ja seal silte muuta (ei, see oleks liiga intuitiivne!). Peate minema ajaloo vahekaardile, leidma tehingu, märgistama selle ja seejärel näete silte mündi sektsioonis. Kõik mündi sektsioonis nähtavad sildid pärinevad kas aadressi siltidest VÕI ajaloo siltidest, kuid iga ajaloo silt tühistab mis tahes aadressi sildi. Siltide varundamiseks faili saate need menüüst eksportida, minnes rahakott–>sildid–>eksport.

Järgmisena kulutame mündid esimeselt aadressilt teisele aadressile. Paremklõpsake esimesel aadressil ja valige "kuluta" (Tegelikult pole see antud stsenaariumis vajalik, kuid kujutage ette, et meil on palju münte paljudel aadressidel; kasutades seda funktsiooni, saame sundida rahakotti kulutama ainult neid münte, mida me tahame. Kui soovime valida mitu münti mitmel aadressil, saame aadresse valida vasakklõpsuga, hoides all käsu klahvi, seejärel paremklõpsata ja valida "kuluta":

![image](assets/36.webp)

Kui olete seda teinud, ilmub rahakoti akna allosas roheline riba, mis näitab valitud müntide arvu ja kogu kulutamiseks saadaolevat summat.

Samuti on võimalik kulutada üksikuid münte aadressil ja jätta teised samal aadressil kulutamata, kuid see on ebasoovitatav, kuna jätate münte aadressile, mis on krüptograafiliselt nõrgenenud ühe mündi kulutamise tõttu (teine põhjus, miks mitte panna mitu münti ühele aadressile, peale privaatsuse põhjuste, on see, et kui kulutate ühe, peaksite kulutama kõik, mis muutub tarbetult kulukaks). Siin on, kuidas valida üksik münt ühiselt aadressilt, kuid ärge tehke seda:

![image](assets/37.webp)

Nüüd on meil valitud kaks münti kulutamiseks. Järgmisena otsustame, kuhu neid kulutada. Saatame need teisele aadressile. Peame aadressi kopeerima nii:

![image](assets/38.webp)

Seejärel minge "Saada" vahekaardile ja kleepige teine aadress "maksa" väljale. Kirjelduse lisamine pole vajalik; võite, kuid seda saab teha hiljem siltide muutmisel. Summa jaoks valige "Max", et kulutada kõik valitud mündid. Seejärel klõpsake "Maksa" ja seejärel klõpsake ilmuval hüpikaknal nuppu "täpsem".

![image](assets/39.webp)

Alati klõpsake selles etapis "täpsem", et saada täielik kontroll ja kontrollida täpselt, mis tehingus on. Siin on tehing:

![image](assets/40.webp)

Näeme kahte sisemist valget kasti/akent. Ülemine on sisendite aken (milliseid münte kulutatakse) ja alumine on väljundid (kuhu mündid lähevad).

Pange tähele, et staatus (üleval vasakul) on praegu "allkirjastamata". "Saadetud summa" on 0, kuna mündid kantakse üle rahakoti sees. Tasu on 481 satsi. Pange tähele, et kui see oleks 480 satsi, jäetaks viimane null ära, näiteks 0.0000048 ja väsinud silmale võib see tunduda 48 satsina – olge ettevaatlik (midagi, mida Electrumi arendajad peaksid parandama).
Tehingu suurus viitab andmete suurusele baitides, mitte bitcoini kogusele. "Asenda tasu abil" on vaikimisi sisse lülitatud ja see võimaldab teil tehingu uuesti saata kõrgema tasuga, kui see on vajalik. LockTime võimaldab teil kohandada, millal tehing kehtib – ma pole sellega veel mänginud, kuid soovitan seda mitte kasutada, kui te täielikult ei mõista, mida teete, ja olete harjutanud väikeste summadega.

Allpool on meil mõned keerukad kaevandamistasu kohandamise tööriistad. Kõik, mida peate sisemiste ülekannete jaoks tegema, on seada see minimaalsele tasule 1 sat/bait. Lihtsalt tippige number käsitsi sihtmääruse väljale. Sobiva tasu kontrollimiseks välismakse jaoks võite külastada https://mempool.space, et näha, kui hõivatud mempool on, ja mõned soovitatud tasud kuvatakse.

![image](assets/41.webp)

Olen valinud 1 sat/bait.

Sisendaknas näeme kahte kirjet. Esimene on 5000 sati annetus. Vasakul näeme selle tehingu räsi (mida saame blockchainis otsida). Selle kõrval on „21“ – see näitab, et see on väljund märgistatud 21 selles tehingus (tegelikult on see 22. väljund, kuna esimene on märgistatud nulliga).

Siin on midagi märkimisväärset: UTXOd eksisteerivad ainult tehingu sees. UTXO kulutamiseks peame selle viitama ja panema selle viite uue tehingu sisendisse. Väljundid muutuvad seejärel uuteks UTXOdeks ja vana UTXO muutub STXOks (kulutatud tehingu väljund).

Teine rida on 10 000 sati annetus. Selle kõrval on tehingu räsi, millest see pärineb, „0“, kuna see on selle tehingu esimene (ja võib-olla ainus) väljund.

Alumises aknas näeme meie aadressi. Pange tähele, et sisendite bitcoini kogusumma ei ühti täielikult väljundite kogusummaga. Erinevus läheb kaevurile. Kaevur vaatab kõigi blokki kaevandatavate tehingute erinevust ja lisab selle numbri oma tasule. (Kaevandamistasud on sel viisil täielikult ahelast lahti ühendatud ja algavad uut elu).

Kui me kaevandamistasu kohandame, muutub väljundi väärtus automaatselt.

> Siin on väärt märkimist: Pange tähele tehinguaknas aadresside värvi. Pidage meeles, et rohelised aadressid on loetletud teie aadressi vahekaardil. Kui aadress on tehinguaknas roheliselt (või kollaselt) esile tõstetud, siis on Electrum selle aadressi ära tundnud kui oma oma. Kui aadressil pole esiletõstmist, siis on see väline aadress (väljaspool praegu avatud rahakotti) ja peaksite seda eriti hoolikalt kontrollima.

Kui olete kõik tehingus kontrollinud ja olete kindel, et olete rahul, milliseid münte kulutate ja kuhu mündid lähevad, võite klõpsata "finalise".

![image](assets/42.webp)

Pärast "finalise" klõpsamist ei saa te enam muudatusi teha – kui vajate, peate selle sulgema ja alustama uuesti. Pange tähele, et "finalise" nupp on muutunud "export" nupuks ja ilmunud on uued nupud: "save", "combine", "sign" ja "broadcast". "Broadcast" nupp on hall, kuna tehing on allkirjastamata ja seega selles etapis kehtetu.

Kui klõpsate sign, kui teil on rahakoti jaoks parool, palutakse teil see sisestada ja seejärel muutub staatus (paremal üleval) "Unsigned" pealt "Signed" peale. Seejärel muutub "Broadcast" nupp saadavaks.
Pärast saatmist võite tehinguakna sulgeda. Kui lähete aadressi vahekaardile, näete nüüd, et esimene aadress on tühi ja teisel aadressil on 1 UTXO.
Märkus: Kõiki neid muudatusi näete isegi enne, kui tehing on kaevandatud blokki ehk "kinnitatud". See on seetõttu, et Electrum uuendab saldosid/tehinguid mitte ainult plokiahela andmete, vaid ka mempooli andmete põhjal. Mitte kõik rahakotid ei tee seda.

Tuleb märkida, et saatmise asemel võime tehingu salvestada hilisemaks. Seda saab salvestada kas allkirjastamata või allkirjastatud olekus.

Klõpsake nuppu "export" (paradoksaalselt, ÄRGE klõpsake nuppu "save"), ja näete mitmeid valikuid. Tehing on kodeeritud tekstina ja seetõttu saab seda salvestada mitmel viisil.

![image](assets/43.webp)

Salvestamine QR-koodina on väga huvitav. Kui valite selle, ilmub QR:

![image](assets/44.webp)

Seejärel saate QR-koodist foto teha. Selle abil saab teha mitmeid asju, kuid praegu öelgem lihtsalt, et laadite selle hiljem rahakotti tagasi. Võite Electrumi sulgeda, rahakoti uuesti laadida ja minna menüüsse Tools:

![image](assets/45.webp)

See laadib üles teie arvuti kaamera. Seejärel näitate kaamerale oma telefoni fotot QR-koodist ja see laadib tehingu tagasi täpselt nii, nagu te selle jättsite.

Salvestatud tehingute laadimine ei ole intuitiivne, seega pange erilist tähelepanu. Tehingu laadimine ei ole "tööriist", vaid valik on peidetud tööriistade menüüsse (veel üks asi, mida Electrumi arendajad peaksid parandama).

Sarnane protsess on võimalik ka failina salvestatud tehinguga. Proovige harjutada mõlema meetodiga samas rahakotis. Ma ei käi seda siin läbi, kuid saate seda funktsiooni kasutada tehingu edastamiseks sama rahakoti vahel erinevatel arvutitel, multisignatuuriga rahakottide vahel ning riistvara rahakottidele ja neilt. Siin on mõned juhised.

Nüüd, tagasi "save" nupu juurde – see ei ole viis, kuidas tehinguteksti salvestada. See tegelikult ütleb Electrumi rahakotile, et tunnistada seda tehingut kohalikul arvutil esitatud makseks. Kui teete seda kogemata, näete tehingut väikese arvuti ikooniga. Võite paremklõpsata ja kustutada tehingu – ärge muretsege, bitcoine sel viisil kustutada ei saa. Electrum unustab siis, et see tehing kunagi toimus, ja "tagastab" satoshi'd tagasi ning kuvab satoshi'd õiges kohas, kus need tegelikult asuvad.

### Muudatusaadressid

Muudatusaadressid on huvitavad. Peate mõistma UTXOsid, et mõista seda selgitust. Kui kulutate aadressile summa, mis on väiksem kui UTXO, siis ülejäänud bitcoin läheb kaevurile, kui ei ole määratud muudatusväljundit.

Teil võib olla 6.15 bitcoini UTXO ja soovite kulutada 0.15 bitcoini, et annetada mõnele maailma kusagil türannilise "demokraatliku" valitsuse poolt rõhutud protestijale. Siis võtaksite 6.15 bitcoini (kasutades Electrumis funktsiooni "spend from"), ja paneksite selle tehingusse.

Te kleepiksite protestijate aadressi väljale "pay to", võib-olla paneksite väljale "description" "EndTheFed & WEF", ja summa jaoks paneksite 0.15 bitcoini ning klõpsaksite "pay", seejärel "advanced".
Tehingute ekraanil, sisestusaknas, näete te 6.15 bitcoini UTXO-d. Väljundaknas näete aadressi, mis ei ole esile tõstetud (see on protestijate aadress), kõrval on 0.15 bitcoini. Näete ka kollast aadressi, millel on veidi vähem kui 6.0 bitcoini. See on muudatusaadress, mille rahakott on automaatselt valinud ühest oma enda kollasest muudatusaadressist. Muudatusaadressi eesmärk on võimaldada rahakotil sinna muudatusmünte panna, segamata segi saaja aadresse, mille jaoks teil võib olla plaane või millele olete saatnud arveid. Kui neid kasutatakse hiljem näiteks klientide poolt, ei soovi te, et teie rahakott neid automaatselt kasutaks ja täidaks. See on segadusse ajav ja halb privaatsuse jaoks.
Pange tähele, et kui kohandate kaevandustasu, kohandub automaatselt muudatusväljundi summa, mitte maksesumma.

### Käsitsi muudatus või maksa mitmele

See on Electrumi tõeliselt huvitav funktsioon. Ligipääs sellele toimub nii.

![pilt](assets/46.webp)

Seejärel saate sisestada mitu sihtkohta UTXO saldole, mida kulutate, nagu see:

![pilt](assets/47.webp)

Kleepige aadress, tippige koma, seejärel tühik, seejärel summa, seejärel <enter>, seejärel tehke seda uuesti. ÄRGE SISESTAGE SUMMASID “SUMMA” AKENDESSE – Electrum täidab siin kogusumma, kui tippite üksikud summad “Maksa” aknasse.

See võimaldab teil käsitsi määrata, kuhu muudatus läheb (nt konkreetne aadress teie rahakotis või teises rahakotis), või võite korraga maksta mitmele inimesele. Kui teie kogusumma ei ole piisavalt suur, et vastata UTXO suurusele, loob Electrum teile siiski lisamuudatusväljundi.

Maksa mitmele funktsioon võimaldab ka luua oma “PayJoins” või “CoinJoins” – väljaspool selle artikli ulatust, kuid mul on siin juhend. (https://armantheparman.com/cj/)

## Rahakotid

Tahan demonstreerida ainult vaatamise rahakotti kasutades Electrumit. Selleks pean esmalt määratlema “rahakott”. Bitcoinis kasutatakse sõna “rahakott” kahe tähendusega:

- Tüüp A, “rahakott” – viitab tarkvarale, mis näitab teie aadresse ja saldosid, nt Electrum, Blue Wallet, Sparrow Wallet jne.

- Tüüp B, “rahakott” – viitab unikaalsele aadresside kogumile, mis on seotud meie seemnefraasi/passfraasi/derivaaditeega kombinatsiooniga. Ühes rahakotis on 8,6 miljardit aadressi (4,3 miljardit saaja aadressi ja 4,3 miljardit muudatusaadressi). Kui muudate seemnefraasis, passfraasis või derivaaditees midagi, saate kasutamata rahakoti uute ja kõik unikaalsete 8,6 miljardi tühja aadressiga.

Millist tüüpi keegi viitab, kui kasutab sõna “rahakott”, on kontekstist ilmne.

## Ainult vaatamise rahakott – harjutus

Pole täiesti ilmne, milleks vaatamise rahakott on mõeldud, kuid alustan selgitamisest, mis see on, kuidas teha harjutusraha, ja siis tuleme selle eesmärgi juurde tagasi hiljem, kui selgitan rohkem riistvara rahakottide kohta. (Põhjaliku ülevaate riistvara rahakoti kasutamisest ja erinevatest brändidest vaata siit.)
Me hakkame looma näidis tavalist rahakotti (seekord lisame veidi keerukust paroolilausega) ja seejärel selle vastavat jälgimisrahakotti. Kui soovite, võite kopeerida täpselt selle, mille mina tegin, või luua oma – see rahakott on mõeldud ära viskamiseks; ärge seda tegelikult kasutage. Alustage 12-sõnalise seemne genereerimisega Ian Colemani veebilehel.
Pange tähele alloleval ekraanipildil olevaid 12 juhuslikku sõna ja seda, et olen sisestanud paroolilause paroolilause väljale:

PAROOLILAUSE: “Craig Wright on valetaja ja petis ning kuulub vangi. Samuti tuleks Ross Ulbricht kohe vanglast vabastada.”

Paroolilause võib olla kuni 100 tähemärki pikk ja ideaalis peaks see olema ühemõtteline ning mitte liiga lühike – see, mida ma kasutasin, on lihtsalt lõbu pärast – ma üldiselt soovitan vältida suurtähti ja sümboleid, et vähendada oma stressi proovides kombinatsioone, kui teil kunagi oleks probleeme oma paroolilause meenutamisega.

![image](assets/48.webp)

Järgmisena, Electrumis, minge menüüsse file–>new/restore. Sisestage uue rahakoti loomiseks unikaalne nimi ja klõpsake "next".

![image](assets/49.webp)

Järgmised sammud peaksid teile nüüdseks tuttavad olema, nii et loetlen need ilma piltideta:

- Standard wallet
- I already have a seed
- Kopeerige ja kleepige 12 sõna kasti või sisestage need käsitsi.
- Klõpsake options ja valige BIP39, samuti klõpsake paroolilause märkeruutu (“extend this seed with custom words”)
- Sisestage oma paroolilause täpselt nii, nagu tegite Ian Colemani lehel
- Jätke vaikimisi skripti semantika ja tuletustee
- Pole vaja lisada parooli (lukustab rahakoti)

Nüüd minge tagasi Ian Colemani lehele, alla "derivation path" sektsiooni ja klõpsake "BIP 84" vahekaarti, et valida samad skripti semantikad nagu Electrumi vaikeseaded (Native Segwit).

![image](assets/50.webp)

Laiendatud privaat- ja avalikud võtmed on just allpool ning need muutuvad, kui teete muudatusi tuletusteel (või miski muu lehe ülaosas).

![image](assets/51.webp)

Näete ka "BIP32 laiendatud privaat-/avalikke võtmeid" – neid võib praegu ignoreerida.

Konto laiendatud privaatvõtit saab kasutada teie rahakoti täielikuks taastamiseks. Konto laiendatud avalik võti, aga, suudab toota ainult piiratud versiooni samast rahakotist (jälgimisrahakott) – Kui panete selle võtme Electrumisse, toodab see siiski kõik 8,6 miljardit aadressi, mida seeme või laiendatud privaatvõti oleksid andnud, kuid Electrumil ei ole kättesaadavad ühtegi privaatvõtit, seega kulutamine pole võimalik. Tehkem seda nüüd, et näidata punkti:

Kopeerige "konto laiendatud avalik võti" lõikelauale.

Seejärel minge Electrumisse, jätke praegu tehtud rahakott avatuks ja minge file–>new/restore. Rahakoti tegemise protsess on veidi erinev kui varem:

- Standard wallet
- Use a master key
- Kleepige laiendatud avalik võti kasti ja jätkake
- Pole vaja sisestada paroolilauset; see on juba osa laiendatud avalikust võtmest
- Pole vaja sisestada skripti semantikat ja tuletusteed
- Pole vaja lisada parooli (lukustab rahakoti)

Kui rahakott laadib, peaksite märkama, et täpselt samad aadressid on laetud nagu varem, kui seeme sisestati. Peaksite samuti märkama pealkirjareal üleval, et see ütleb "watching wallet". See rahakott võimaldab teil näha oma aadresse ja saldosid (saldo kontrollimiseks läbi sõlme), kuid te ei saa TEHA tehinguid (kuna jälgimisrahakotil pole privaatvõtmeid).
Siis mis on selle mõte?
Üks põhjus, ja mitte peamine, on see, et saate potentsiaalselt jälgida oma rahakoti ja selle jääki arvutis ilma, et peaksite oma privaatvõtmeid arvuti pahavarale paljastama.

Teine põhjus on see, et see on VAJALIK maksete tegemiseks, kui otsustate hoida oma privaatvõtmed arvutist eemal; ma selgitan:

> Riistvaralised rahakotid (HWW) loodi selleks, et seade saaks turvaliselt hoida teie privaatvõtmeid (lukustatud PIN-koodiga), mitte kunagi paljastada võtmeid arvutile (isegi kui see on ühendatud arvutiga kaabli kaudu) ja need ise ei saa ühenduda internetiga. Selline seade ei saa iseseisvalt tehinguid teha, kuna kõik bitcoin'i tehingud algavad viitega UTXO-le (kasutamata tehingu väljund) blockchain'is (mis asub sõlmes). Rahakott peab täpsustama, millises tehingu ID-s UTXO asub ja milline tehingu väljund on see, mida kulutatakse. Alles pärast sisendi täpsustamist saab üldse luua uue tehingu, rääkimata selle allkirjastamisest. Riistvaralised rahakotid ei saa tehinguid luua, kuna neil puudub juurdepääs ühelegi UTXO-le – need ei ole millegagi ühendatud! Tavaliselt ekstraheeritakse HWW-st laiendatud avalik võti ja aadressid kuvatakse seejärel arvutis – paljud inimesed on tuttavad Ledgeri tarkvara või Trezor Suite'iga, mis näitavad aadresse ja jääke nende arvutis – see on jälgimisrahakott. Need programmid saavad luua tehinguid, kuid nad ei saa allkirjastada. Nad saavad lasta tehinguid allkirjastada ainult HWW-dega, mis on nendega ühendatud. HWW võtab jälgimisrahakotist uue genereeritud tehingu, allkirjastab selle ja seejärel saadab selle tagasi arvutisse, et edastada sõlmele. HWW ei saa ise edastada, seda teeb tema seotud jälgimisrahakott. Sel viisil koostöötavad kaks rahakotti (avaliku võtme rahakott arvutis ja privaatvõtme rahakott HWW-s), et genereerida, allkirjastada ja edastada, samal ajal tagades, et privaatvõtmed püsivad isoleerituna ja eemal internetiga ühendatud seadmest.

## Osaliselt Allkirjastatud Bitcoin'i Tehingud (PSBTs)

On võimalik, et tehing luuakse ja salvestatakse faili, hiljem laaditakse uuesti, allkirjastatakse, salvestatakse, laaditakse hiljem uuesti ja seejärel lõpuks edastatakse – ma ei ütle, et keegi peaks seda tegema; see on lihtsalt midagi, mis on võimalik.

Nüüd kaaluge 3-st 5-st multisignatuuri rahakotti – 5 privaatvõtit loovad rahakoti ja 3 on vajalikud tehingu täielikuks allkirjastamiseks (Lisateave multisignatuuri rahakoti võtmete kohta siin). On võimalik, et 5 erineval arvutil on igaühel viiest privaatvõtmest üks.

Arvuti üks võib genereerida tehingu ja selle allkirjastada. Seejärel võib see salvestada selle faili ja saata e-postiga arvutile 2. Arvuti 2 saab seejärel allkirjastada ja võib-olla salvestada faili QR-koodina ning edastada QR-i Zoomi kõne kaudu arvutile 3 teisel pool maailma. Arvuti 3 saab QR-i jäädvustada, laadida tehingu Electrum'i ja allkirjastada tehingu. Pärast esimest kahte allkirja oli tehing PSBT (osaliselt allkirjastatud bitcoin'i tehing). Pärast 3. allkirja sai tehingust täielikult allkirjastatud ja kehtiv, valmis edastamiseks.

PSBT-de kohta lisateabe saamiseks vaadake seda juhendit. (https://armantheparman.com/psbt/)

## Riistvaraliste Rahakottide Kasutamine Electrum'iga

Mul on juhend üldiselt riistvaraliste rahakottide kasutamise kohta, mida ma arvan, et oleks oluline uutele HWW-de kasutajatele lugeda. (https://armantheparman.com/using-hwws/)
Siin on juhendid erinevate HWW-de (riistvaraliste rahakottide) ühendamiseks Sparrow Bitcoin Wallet'iga, mida leiate siit. (https://armantheparman.com/hwws/)
See saab olema minu esimene juhend, mis näitab, kuidas kasutada riistvaralist rahakotti koos Electrumiga – ma kasutan näitamiseks ColdCard riistvaralist rahakotti. See ei ole mõeldud olema detailne juhend ColdCard'i kohta spetsiifiliselt, see juhend asub siin. Ma lihtsalt näitan Electrumi-spetsiifilisi punkte. (https://armantheparman.com/cc/)

### Ühendamine mikro SD-kaardi kaudu (õhulõhega)

Enne oma päris rahakoti ühendamist ColdCard'i kaudu, loodan, et olete läbinud varasemad sammud, laadinud Electrumi näidisrahakoti ja seadistanud võrguparameetrid.

Seejärel sisestage ColdCard'is SD-kaart. Eeldan, et olete juba loonud oma seemne. Kui pääsete rahakotile ligi paroolifraasiga, rakendage see nüüd. Kerige alla ja valige menüü Advanced/Tools –> Export Wallet –> Electrum Wallet.

Võite alla kerida ja lugeda sõnumit. See pakub alati võimalust valida “1”, et sisestada mitte-nullist konto number (midagi, mis on osa tuletusteest), kuid kui järgisite minu nõuannet, pole te vaikimisi tuletusteid muutnud, nii et te ei soovi mitte-nullist konto numbrit; lihtsalt vajutage jätkamiseks märkeruutu.

Seejärel valige skripti semantika. Enamik inimesi valib “Native Segwit”.

See ütleb “Electrum rahakoti fail kirjutatud” ja kuvab faili nime. Tehke sellest vaimne märkus.

Seejärel võtke mikro SD-kaart välja ja pange see Electrumiga arvutisse.

Mõned operatsioonisüsteemid avavad automaatselt failihalduri, kui sisestate mikroSD. Paljud inimesed näevad uut rahakoti faili ja topeltklõpsavad seda, imestades, miks see ei tööta. See pole suurepärane disain. Tegelikult peate failihalduri ignoreerima (sulgege see) ja avama rahakoti faili kasutades Electrumi:

Avage Electrum. Kui see on juba avatud mõne teise rahakotiga, valige file –> new. Otsime seda akent:

![image](assets/52.webp)

Siin on nipp, see pole intuitiivne. Klõpsake “choose”. Seejärel navigeerige mikroSD-kaardi failisüsteemis ja leidke rahakoti fail ning avage see.

Nüüd olete avanud oma riistvaralise rahakoti vastava jälgimisrahakoti. Tore.

### Ühendamine USB-kaabli kaudu.

See meetod peaks olema lihtsam, kuid Linuxi arvutite jaoks on see palju raskem. Midagi, mida nimetatakse “Udev reegliteks”, tuleb uuendada. Siin on kuidas (detailne juhend https://armantheparman.com/gpg-articles/ ), ja lühidalt:

On hea mõte veenduda, et süsteem on ajakohane. Siis:

```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

seejärel...

```bash
python3 -m pip install ckcc-protocol
```

Kui saate veateate, veenduge, et pip oleks installitud. Saate seda kontrollida (pip –version) abil ja saate selle installida (sudo apt install python3-pip)

Loo või muuda olemasolevat faili, /etc/udev/rules.d/

Nagu see:

```bash
sudo nano /etc/udev/rules.d
```

Tekstiredaktor avaneb. Kopeerige tekst siit ja kleepige see rules.d faili, salvestage ja väljuge.

![image](assets/53.webp)

Seejärel käivitage need käsud üksteise järel:

```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```
Kui saate sõnumi "group plugdev" juba eksisteerib, siis on kõik korras, jätkake. Pärast teist käsku ei saa te tagasisidet/vastust, lihtsalt jätkake kolmanda käsuga.
Võib olla vajalik ColdCard arvutist lahti ühendada ja seejärel uuesti ühendada.

Kui pärast kõike seda ei õnnestu ColdCardiga ühendust saada, prooviksin ma tarkvara uuendada (juhend tuleb varsti, kuid praegu leiate juhised tootja veebisaidilt).

Järgmisena looge uus rahakott:

- Standardne rahakott
- Kasutage riistvaraseadet
- See skannib ja tuvastab teie ColdCardi. Jätkake.
- Valige skripti semantika ja tuletustee
- Otsustage, kas rahakoti fail peaks olema krüpteeritud (soovitatav)

### Tehingud ColdCardiga

Kaabliga ühendatuna on tehingud lihtsad. Tehingute allkirjastamine on sujuv.

Kui kasutate seadet õhulõhega viisil, peate käsitsi edastama salvestatud tehingu seadmete vahel kasutades microSD kaarti. On mõned nüansid.

Pärast tehingu loomist ja lõpetamist peate klõpsama alumises vasakus nurgas asuvat eksportimise nuppu. Näete "salvesta faili", mis vastupidiselt intuitiivsusele, ei ole see, mida me tahame. Tegelikult peate esmalt minema kõige viimase menüüvalikuni, mis ütleb "riistvararahakottide jaoks", ja seejärel selle valiku sees leidma teise "salvesta faili" ja valima selle. Seejärel salvestage fail microSD-le, võtke kaart välja ja pange see ColdCardi. Pidage meeles, et võib olla vajalik rakendada paroolifraasi, et valida õige rahakott. Ekraan ütleb valmis allkirjastamiseks. Klõpsake linnukesel, uurige tehingut ja jätkake kinnitamisega linnukese abil. Kui olete valmis, võtke kaart välja ja pange see tagasi arvutisse.

Seejärel peame avama tehingu kasutades Electrumi. Funktsioon on peidetud menüüs tööriistad –> laadi tehing. Navigeerige failisüsteemis ja leidke fail. Iga allkirjastamise korral on kolm faili. Algne salvestatud fail, mille Watching Wallet tegi, ja kaks, mille tegi ColdCard (ma ei tea, miks ta seda teeb). Üks ütleb "allkirjastatud" ja teine "lõplik". See pole intuitiivne, kuid "allkirjastatud" fail pole kasulik, me peame avama "lõpliku" tehingu.

Kui olete selle laadinud, saate klõpsata "edasta" ja makse tehakse.

## Electrumi ja peidetud ".electrum" kataloogi uuendamine

Electrum asub teie arvutis kahes kohas. On rakendus ise ja on peidetud konfiguratsioonikaust. See kaust asub erinevates kohtades sõltuvalt teie operatsioonisüsteemist:

Windows:

> C:/Users/teie_kasutajanimi_siia/AppData/Roaming/Electrum

Mac:

> /Users/teie_kasutajanimi_siia/.electrum

Linux:

> /home/teie_kasutajanimi_siia/.electrum

Pange tähele, et Linuxis ja Macis enne "electrum" on punkt – see näitab, et kataloog on peidetud. Samuti pange tähele, et see kataloog luuakse (automaatselt) alles siis, kui käivitate Electrumi esimest korda. Kataloog sisaldab electrumi konfiguratsioonifaili ja ka kataloogi, mis hoiab kõiki teie salvestatud rahakotte.

Kui kustutate Electrumi programmi oma arvutist, jääb peidetud kataloog alles, kui te seda aktiivselt ka ei kustuta.
Electrumi uuendamiseks järgite sama protseduuri, mida kirjeldasin alguses allalaadimiseks ja kontrollimiseks. Seejärel on teil arvutis kaks programmi koopiat ja saate käivitada kumbagi – iga programm pääseb juurde samale peidetud Electrumi kaustale oma konfiguratsiooni ja rahakoti juurdepääsu jaoks. Kõik salvestatud asjad, nagu baasühik, vaikimisi sõlmele ühendamiseks, muud eelistused ja rahakottidele juurdepääs, jäävad alles, kuna kõik see on salvestatud sellesse kausta.

### Oma Electrumi ja rahakottide teise arvutisse viimine

Selleks võite programmi failid kopeerida USB-draivile ja samuti kopeerida .electrum kataloogi. Seejärel kopeerige või viige need uude arvutisse. Te ei pea programmi uuesti kontrollima. Veenduge, et kopeeriksite .electrum kataloogi vaikimisi asukohta (pidage meeles seda kopeerida ENNE Electrumi esmakordset käivitamist selles arvutis, vastasel juhul täidetakse tühi vaikimisi .electrum kaust ja võite segadusse sattuda).

## Sildid

Nagu ma varem selgitasin, on aadressi vahekaardil siltide veerg. Saate seal topeltklõpsata ja sisestada endale märkmeid (see on ainult teie arvutis, mitte avalik ja mitte plokiahelas).

![image](assets/54.webp)

Oma Electrumi rahakoti teise arvutisse viimisel võite soovida kõiki neid märkmeid mitte kaotada. Saate need varundada faili, kasutades menüüd, rahakott–> sildid –> eksport, ja seejärel uues arvutis, kasutage rahakott–>sildid–>import.

## Näpunäited:

Kui leiate selle ressursi kasulikuks ja soovite toetada seda, mida ma teen Bitcoini jaoks, võite siia annetada mõned satsid:

Staatiline Lightning aadress: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/