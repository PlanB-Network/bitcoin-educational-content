---
name: SeedSigner
description: Hardware Wallet, mis on DIY, riigita, taskukohane ja täielikult õhuga varustatud
---

![cover](assets/cover.webp)



SeedSigner on avatud lähtekoodiga Hardware Wallet Bitcoin, mida igaüks saab ise ehitada, kasutades odavaid üldotstarbelisi elektroonilisi komponente. Erinevalt kommertstoodetest, nagu Ledger, Coldcard või Trezor, ei ole tegemist valmis seadmega, mida toodab mõni ettevõte: tegemist on kogukonna projektiga, mis võimaldab igaühel luua oma seadme, kontrollides iga sammu.



SeedSigner on loodud nii, et see on 100% ***air-gapped***: see ei ühendu kunagi internetti, sellel ei ole Wi-Fi ega Bluetooth (Raspberry Pi Zero v1.3 puhul) ja see ei ole kunagi ühendatud arvutiga, et Exchange andmeid edastada. Side toimub eranditult QR-koodi Exchange süsteemi kaudu. Konkreetselt öeldes kuvab teie portfellihaldustarkvara (näiteks Sparrow wallet) allkirjastatava tehingu QR-koodide kujul; te skaneerite neid SeedSigneri kaameraga, seejärel allkirjastab seade tehingu, kasutades teie ajutiselt RAM-i salvestatud isiklikke võtmeid. Lõpuks genereerib seade QR-koodid, mis sisaldavad allkirjastatud tehingut, mida te skannite oma tarkvaraga, et saata see Bitcoin võrku.



![Image](assets/fr/001.webp)



SeedSigner on ka ***stateless***. Teisisõnu, see ei salvesta teie seed või privaatvõtmeid püsivalt, erinevalt teistest riistvaralistest rahakottidest. Iga kord, kui te taaskäivitate seadme, on selle mälu täiesti tühi, välja arvatud juhul, kui te seadet nii seadistate, et see salvestab teie seaded microSD-kaardile. Seega peate oma seed iga kord uuesti sisestama, kui seda kasutate, kõige praktilisem meetod on salvestada see QR-koodi kujul, mida tuleb käivitamisel SeedSigneri kaamera abil skannida. Selline tööviis vähendab märkimisväärselt rünnakupinda: isegi kui varas teie seadme varastab, ei leia ta sealt mingit teavet, sest see on vaikimisi alati tühi.



Teine võimalus oma seed salvestamiseks ja selle kasutamiseks SeedSigneriga on kasutada *SeedKeeper* kiipkaarti koos ühilduva lugejaga. See annab teile väga töökindla *secure element* seed salvestamiseks, kasutades samal ajal SeedSigneri ekraani tehingute allkirjastamiseks. Kuid see konkreetne konfiguratsioon on teise spetsiaalse õpetuse teema. Siinkohal keskendume SeedSigneri põhikasutusele:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Projekt SeedSigner on Bitcoin ökosüsteemis olulisel kohal, kuna see pakub kõigile, kõikjal maailmas, võimalust kasutada oma bitcoinide kaitsmiseks täiustatud turvalisust. Selle peamine eelis on selle kättesaadavus: vajaliku riistvara saab osta vähem kui 50 dollariga. Veelgi enam, see võimaldab piiratud riikides elavatel inimestel ehitada oma Hardware Wallet standardsetest arvutikomponentidest, mida on lihtne leida ja mille suhtes kehtivad vähem regulatiivsed piirangud.



Kuid isegi väljaspool neid konkreetseid kontekste võib SeedSigner olla teie jaoks huvitav valik: see on avatud lähtekoodiga, töötab ilma olekuta ja õhupiirita ning vähendab teie Hardware Wallet Supply ahelaga seotud ründevektoreid.



## 1. Vajalikud seadmed



SeedSigneri ehitamiseks vajate järgmisi komponente:





- Raspberry Pi Zero
    - Soovitatav on versioon 1.3, kuna sellel ei ole Wi-Fi ega Bluetooth, mis tagab täieliku isolatsiooni.
 - W ja v2 versioonid on samuti ühilduvad, kuid sisaldavad Wi-Fi/Bluetooth kiipi. Seetõttu on soovitatav see füüsiliselt deaktiveerida, eemaldades raadiomooduli kaardilt. Operatsioon on suhteliselt lihtne, kuid nõuab täpsust (Zero W puhul piisab peenikestest tangidest, v2 puhul on moodulit varjava metallplaadi eemaldamiseks vaja Hot pliiatsit). Ma ei hakka selles õpetuses üksikasjadesse laskuma, kuid kõik juhised leiate sellest dokumendist: *[WiFi/Bluetooth'i keelamine riistvara abil](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Pange tähele: mõned Raspberry Pi Zero mudelid müüakse ilma eeljootetud GPIO-pinideta. Saate kas osta otse integreeritud viikudega versiooni (lihtsaim lahendus) või osta viikud eraldi ja joota need ise (keerulisem lahendus).
 - Ärge unustage mikro-USB-toite Supply.



![Image](assets/fr/002.webp)





- Waveshare 1,3" ekraan (240×240 px)** (prantsuse keeles)
    - Oluline on valida just see mudel: on olemas ka teisi sarnaseid ekraane, kuid erineva eraldusvõimega. Ilma 240×240 px eraldusvõimeta on ekraan kasutuskõlbmatu.
    - Ekraanil on kolm nuppu ja minijoystick, mis on kasutaja Interface.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**-ga ühilduv kaamera
    - Võimalus 1: standardkaamera koos laia kuldmattega (kontrollige ühilduvust oma korpusega).
    - Võimalus 2: kompaktsem "*Zero*" kaamera, mis on mõeldud spetsiaalselt Pi Zero jaoks.



![Image](assets/fr/004.webp)





- MicroSD** kaart
    - Soovitatav maht: 4-32 GB.





- Elamu (vabatahtlik, kuid soovitatav)** (vabatahtlik, kuid soovitatav)** (vabatahtlik, kuid soovitatav)** (vabatahtlik, kuid soovitatav)** (soovitatav)
    - Kaitseb seadet ja muudab selle kasutamise lihtsaks.
    - Kõige populaarsem mudel on "*Orange Pill Case*", mille [avatud lähtekoodiga STL-failid on saadaval 3D-printimiseks](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Karbid on saadaval ka [projektiga seotud sõltumatute edasimüüjate kaudu](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Neid komponente saab osta eraldi või lihtsuse huvides valida valmispakendid, mis sisaldavad kogu vajalikku riistvara. Mina isiklikult tellisin oma paketi [sellelt Prantsuse saidilt](https://bitcoinbazar.fr/), kuid müüjate nimekirja iga maailma piirkonna kohta leiate ka [SeedSigneri projekti riistvara leheküljelt](https://seedsigner.com/hardware/). Kui eelistate komponente ükshaaval osta, on need saadaval suuremates e-kaubanduse platvormides või eripoodides.



## 2. Tarkvara ettevalmistamine



Kui olete oma riistvara kokku pannud, peate valmistama ette microSD-kaardi, paigaldades sellele SeedSigner süsteemi. Selleks minge oma igapäevasesse personaalarvutisse ja ühendage SeedSignerile mõeldud microSD-kaart.



### 2.1. Lae alla



Mine [projekti ametlikku GitHubi repositooriumi](https://github.com/SeedSigner/seedsigner/releases). Tarkvara uusimast versioonist, laadige alla :




- Teie Pii mudelile vastav .img-pilt.
- Fail "sha256.txt".
- Fail "sha256.txt.sig".



![Image](assets/fr/006.webp)



Enne paigaldamise alustamist kontrollime tarkvara.



### 2.2 Verifitseerimine Linuxi ja macOSi all



Alustage, importides SeedSigner projekti ametlik avalik võti otse Keybase'ist :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal peaks teile teatama, et võti on imporditud või uuendatud. Järgmisena käivitage allkirjafaili kontrollimise käsk (ärge unustage käsku muuta vastavalt teie versioonile, siin `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Kui kõik on korrektne, peaks väljundis olema "Hea allkiri". See tähendab, et fail `.sha256.txt` on allkirjastatud äsja imporditud võtmega ja allkiri on kehtiv. Ignoreerige hoiatusteadet `WARNING: This key is not certified with a trusted signature`: see on normaalne, sest nüüd on teie ülesanne kontrollida, et kasutatud võti kuulub SeedSigner projektile.



Selleks võrrelge kuvatud sõrmejälje viimaseid 16 märki nendega, mis on saadaval [Keybase.io/SeedSigner](https://keybase.io/seedsigner), nende [ametlikus Twitteris](https://twitter.com/SeedSigner/status/1530555252373704707) või [SeedSigner.com](https://seedsigner.com/keybase.txt) avaldatud failis. Kui need identifikaatorid vastavad täpselt, võite olla kindel, et tegemist on tõepoolest projekti võtmega. Kahtluse korral lõpetage kohe ja küsige abi SeedSigneri kogukonnalt (Telegram, X, GitHub...).



Kui võti on valideeritud, saate kontrollida, et allalaaditud kujutist ei ole muudetud (ärge unustage, et käsku muudetaks vastavalt teie versioonile, siin `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Linuxi all on see käsk sisseehitatud.
- Hoiatus: MacOS-i versioonid enne `Big Sur (11)` ei tunne valikut `--ignore-missing`. Sellisel juhul eemaldage see ja ignoreerige hoiatusi puuduvate failide kohta.



Oodatav tulemus on "OK" faili ".img" kõrval. See kinnitab, et üleslaetud pilt on identne projekti poolt avaldatud pildiga ja seda ei ole muudetud.



### 2.3 Windowsi kontrollimine



Windowsis on protseduur sarnane, kuid käsud on erinevad. Alustage [Gpg4win](https://www.gpg4win.org/) installeerimisest ja avage *Kleopatra* rakendus. Impordige SeedSigner projekti avalik võti URL-ilt Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Seejärel avage PowerShell kaustas, kus asuvad teie alla laetud failid (`Shift` + paremklõps > `Open PowerShell here`). Käivitage manifesti allkirja kontrollimiseks järgmine käsk (ärge unustage käsku muuta vastavalt teie versioonile, siin `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Kui kõik on korrektne, peaks väljundis olema "Hea allkiri". See tähendab, et fail `.sha256.txt` on allkirjastatud äsja imporditud võtmega ja allkiri on kehtiv. Ignoreerige hoiatusteadet `WARNING: This key is not certified with a trusted signature`: see on normaalne, sest nüüd on teie ülesanne kontrollida, et kasutatud võti kuulub SeedSigner projektile.



Selleks võrrelge kuvatud sõrmejälje viimaseid 16 märki nendega, mis on saadaval [Keybase.io/SeedSigner](https://keybase.io/seedsigner), nende [ametlikus Twitteris](https://twitter.com/SeedSigner/status/1530555252373704707) või [SeedSigner.com](https://seedsigner.com/keybase.txt) avaldatud failis. Kui need identifikaatorid vastavad täpselt, võite olla kindel, et tegemist on tõepoolest projekti võtmega. Kahtluse korral lõpetage kohe ja küsige abi SeedSigneri kogukonnalt (Telegram, X, GitHub...).



Kui võti on kinnitatud, peate kontrollima, et pildifail ei oleks kahjustatud. Selleks kasutage PowerShellis järgmist käsku :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Näide Raspberry Pi Zero 2 jaoks (ärge unustage käsku muuta vastavalt teie versioonile, siin `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell arvutab seejärel teie pildifaili Hash SHA256. Võrrelge seda Hash vastavat väärtust dokumendis `seedsigner.0.8.6.sha256.txt`.




- Kui need kaks väärtust on rangelt identsed, on kontroll edukas ja te võite jätkata.
- Kui need erinevad, on fail vigastatud või rikutud. Ärge kasutage seda ja alustage allalaadimist uuesti.



![Image](assets/fr/013.webp)



Edukas kontrollimine tagab, et teie `.img` fail on nii autentne (allkirjastatud SeedSigneri poolt) kui ka muutmata (muutmata). Seejärel võite julgelt edasi liikuda järgmise sammu juurde.



### 2.4. Vilguta pilti



Kui sul seda veel ei ole, lae alla [Balena Etcher] tarkvara (https://etcher.balena.io/), siis :




- Sisestage microSD-kaart arvutisse.
- Launch Etcher.
- Valige alla laetud ja kontrollitud .img-faili.
- Valige sihtmärgiks microSD-kaart.
- Klõpsake nuppu "Flash!`.



![Image](assets/fr/014.webp)



Oodake, kuni protsess on lõppenud: teie microSD on kasutusvalmis. Nüüd on aeg kokku panna!



## 3. SeedSigner koost



Kui teie microSD-kaart on ette valmistatud ja tarkvara SeedSigneriga välgustatud, saate jätkata lõpliku kokkupanekuga. Võtke aega, sest mõned osad on haprad (eelkõige laualapp, kaamera ja GPIO-pinid).



### 3.1 Korpuse ettevalmistamine



Kõigepealt avage oma juhtum. Kontrollige, et see oleks puhas ja et 3D-printimise plastijäägid ei oleks sisemiste kinnitusdetailide teel. Vaadake välja :




- Kaamera asukoht (väike ümmargune auk ees).
- Ekraani avamine.
- Väljalõiked Raspberry Pi Zero micro-USB-portide ja microSD-pesa jaoks.



### 3.2 Kaamera paigaldamine



Leidke Raspberry Pi Zero kaamera lintühendust: see on õhuke must riba plaadi küljel, mida saab avada, kui seda veidi tõsta. Tõstke seda ettevaatlikult, ilma seda sundimata: see peaks lihtsalt mõne millimeetri võrra kallinema.



![Image](assets/fr/015.webp)



Asetage kaamera kate sisse. Pruun/vaskne osa peaks olema suunatud allapoole. Veenduge, et see istub kindlalt, ilma väänamata, pistikupesas.



![Image](assets/fr/016.webp)



Sulgege must riba, et lukustada lauakate (tunnete kerget klõpsatust). Kontrollige ettevaatlikult, et see jääks paigale ja ei liiguks.



![Image](assets/fr/017.webp)



Seejärel asetage kaameramoodul korpuse vastavasse avasse. Sõltuvalt mudelist võib see kas otse sisse klõpsata või on vaja väikest liimiriba, mis hoiab seda paigal. Objektiiv peab olema täpselt joondatud, suunaga väljapoole.



### 3.3 Raspberry Pi Zero paigaldamine



Kui kasutate korpust, siis sisestage Raspberry Pi Zero plaat selle sisse. Joondage porte ettevaatlikult ettenähtud avadega.



Seejärel asetage Waveshare'i ekraan Raspberry Pi Zero peale. Pii GPIO-pinid peaksid olema ideaalselt kooskõlas ekraani emasliitmikuga. Suruge kuvar aeglaselt tihvtidele, avaldades ühtlast survet mõlemale küljele, et vältida nende painutamist.



![Image](assets/fr/018.webp)



Kui teil on korpus, lõpetage kokkupanek, lisades esipaneeli ja juhtpuldi.



Lõpuks sisestage väljalülitatud tarkvara sisaldav microSD-kaart Raspberry Pi Zero servas asuvasse pessa. Veenduge, et see klapib paika.



### 3.4 Esimene käivitamine



Ühendage micro-USB toitekaabel spetsiaalsesse porti. Oodake umbes üks minut. SeedSigneri logo peaks ilmuma, millele järgneb avakuva.



![Image](assets/fr/019.webp)



Alustuseks kontrollige, et erinevad komponendid töötavad korralikult, minnes menüüsse `Settings > I/O test`.



![Image](assets/fr/020.webp)



Testige kõiki nuppe ja veenduge, et need reageerivad õigesti. Seejärel klõpsake nupule `KEY1`, et kontrollida, kas kaamera töötab ootuspäraselt. See teeb pildi.



![Image](assets/fr/021.webp)



### 3.5 Kaamera reguleerimine



Sõltuvalt sellest, kuidas olete SeedSigneri paigaldanud, võib kaamera kuvada ümberpööratud pilti. Selle parandamiseks minge valikusse `Settings > Advanced > Camera rotation` ja valige vajadusel 180° pööramine.



![Image](assets/fr/022.webp)



Kui olete muutnud kaamera orientatsiooni või soovite hiljem muuta muid seadeid (näiteks Interface keelt), peate lubama seadete püsimise microSD-kaardil. Vastasel juhul lähevad teie seaded iga kord taaskäivitamisel tagasi vaikimisi, sest Raspberry Pi Zero ei oma püsivat mälu.



Selleks avage menüü "Seaded > Püsiseaded" ja valige "Lubatud".



![Image](assets/fr/023.webp)



Kui kõik toimib, on teie SeedSigner nüüd kasutusvalmis!



## 4. SeedSigner seaded



Enne Bitcoin Wallet loomist konfigureerime SeedSigneri. Kuna see töötab püsiva mäluta Raspberry Pi Zero'l, ei salvestu selle seaded automaatselt, kui te neid microSD-kaardile ei salvesta. Seega veenduge, et olete selle võimaluse sisse lülitanud, vastasel juhul lähevad need seaded taaskäivitamisel kaduma (vt samm 3.5).



### 4.1 Parameetrite menüüle juurdepääs



Käivitage SeedSigner ja oodake, kuni avakuva ilmub. Navigeerige joysticki abil valikule `Settings` ja kinnitage see, vajutades keskmist nuppu. Nüüd sisenete seadete peamenüüsse.



![Image](assets/fr/024.webp)



### 4.2 Portfellihaldustarkvara valimine



Seejärel avage menüü "Koordinaatori tarkvara".



![Image](assets/fr/025.webp)



Koordinaator viitab portfellihaldustarkvarale, millega teie SeedSigner suhtleb QR-koodide kaudu. See tarkvara on paigaldatud kas teie arvutisse või nutitelefoni. See võimaldab teil hallata oma bitcoin'e, kuid ilma, et teil oleks juurdepääs teie privaatvõtmetele. SeedSigner jääb ainsaks seadmeks, mis on võimeline teie tehinguid allkirjastama.



Praegune püsivara versioon toetab mitmeid tarkvarapakette: Sparrow, Specter, BlueWallet, Nunchuk ja Keeper. Minu puhul kasutan **Sparrow wallet**, mida soovitan eriti selle lihtsuse ja rikkaliku funktsionaalsuse tõttu.



Kui te ei tea, kuidas seda paigaldada, saate jälgida seda õpetust:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Lihtsalt valige menüüst soovitud tarkvara.



![Image](assets/fr/026.webp)



### 4.3 Ühikute ja summa kuvamine



Menüüs `Denomination Display` saate valida ühiku, milles summad kuvatakse:




- `BTC`
- mBTC` (milli-Bitcoin või 0,001 BTC)
- gW-20 (satoshi või 1/100 000 000 BTC)



**Sats** seade on üldiselt kõige praktilisem väikeste koguste puhul.



![Image](assets/fr/027.webp)



### 4.4 Täiustatud seaded



Nüüd minge menüüsse "Täiustatud". Siit leiate mitu kasulikku valikut:




- gW-22 network`: tuleb muuta ainult siis, kui soovite kasutada SeedSigner'i Testnet-l.
- qR-koodi tihedus": reguleerib igas QR-koodis sisalduva teabe hulka. Võite jätta vaikimisi väärtuse, kui teil ei ole skaneerimisel raske lugeda.
- `Xpub export`: võimaldab või keelab teie laiendatud avaliku võtme (`xpub`, `ypub`, `zpub`) eksportimise portfellihaldustarkvarasse QR-koodi kaudu (funktsioon, mida me kasutame hiljem, seega jätke see esialgu sisse lülitatud).
- `Skriptitüübid`: määrab skriptitüübid, millega on lubatud teie bitcoinid lukustada. Seda parameetrit ei ole vaja muuta, sest skripti tüüp määratakse otse Sparrow. Siinkohal käsitletakse ainult neid skripte, mida SeedSigneril on lubatud manipuleerida.



### 4.5 Keele valik



Lõpuks saate menüüs "Keel" muuta Interface keelt vastavalt oma eelistustele.



![Image](assets/fr/028.webp)



## 5. seed loomine ja salvestamine



seed (või Mnemonic fraas) on teie Bitcoin portfelli aluseks. Seda kasutatakse teie isiklike võtmete ja aadresside tuletamiseks ning see tagab juurdepääsu teie rahalistele vahenditele. SeedSigner pakub selle genereerimiseks mitu meetodit, mida me käesolevas jaotises uurime.



Enne kui alustame, mõned olulised meeldetuletused:




- See fraas annab teile täieliku ja piiramatu juurdepääsu kõigile teie bitcoinidele.** Igaüks, kes seda fraasi valdab, võib teie raha varastada, isegi ilma füüsilise juurdepääsuta teie SeedSignerile;
- Tavaliselt kasutatakse Wallet taastamiseks 12-sõnalist lauset, kui Hardware Wallet on kadunud või varastatud. Kuid kuna SeedSigner on *statita* seade, ei registreeri ta kunagi teie seed. Seega ei ole teie füüsilised varukoopiad mitte lihtsalt varukoopiad, vaid **ainus viis Wallet kasutamiseks**. Kui te kaotate need varukoopiad, on teie bitcoinid jäädavalt kadunud. Seega varundage need hoolikalt, mitmel andmekandjal ja turvalistes kohtades;
- Kui te alles alustate, soovitan teil tungivalt lugeda seda õpetust, et saada üksikasjalik ülevaade Mnemonic fraasi haldamisega seotud riskidest:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Juurdepääs seed loomise tööriistale



SeedSigneri avalehel minge menüüsse `Tööriistad`.



![Image](assets/fr/029.webp)



Nüüd saate generate oma seed. seed on lihtsalt suur juhuslik number. Mida juhuslikumalt see genereeritakse, seda turvalisem on see. SeedSigner pakub selleks kaks võimalust:




- kaamera": seed tekib foto visuaalsest mürast. Võetakse pilt juhuslikust keskkonnast (objekt, maastik, nägu jne.), mille pikslivarieeringuid kasutatakse generate entroopiaks. See on kiire meetod, kuid ei ole reprodutseeritav.
- nopavisked": visatakse täringut, et tekitada vajalikku entroopiat. See on küll aeganõudvam, kuid reprodutseeritav ja seega kontrollitav. Kui otsustate selle meetodi kasuks, järgige selles õpetuses antud nõuandeid (kontrollsummat ei ole vaja siin arvutada, selle eest hoolitseb SeedSigner):



https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 seed loomine koos fotoga



Kui valite fotomeetodi, klõpsake nupule "Uus seed" (kaamera ikooniga), tehke pilt ja kinnitage see. Seejärel valige oma lause pikkus (12 või 24 sõna), mis ilmub ekraanile salvestamiseks. Järgnevad sammud on identsed osaga 5.3.



### 5.3 seed loomine täringutega



Selles õpetuses kasutame **Nopikrullide** meetodit. Klõpsake nupule `New seed` (täringu ikooniga).



![Image](assets/fr/030.webp)



Seejärel valige oma Mnemonic fraasi pikkus. 12 sõna pakub juba piisavat turvalisust, nii et ma soovitan seda valikut.



![Image](assets/fr/031.webp)



Viska täringut ja sisesta saadud numbrid kursori abil. Vajutage iga sisestuse kinnitamiseks keskmist nuppu. Kui teete vea, saate tagasi minna. Kasutage mitut erinevat täringut, et vähendada tasakaalustamata täringute mõju. Veenduge, et teid ei jälgita selle toimingu ajal.



![Image](assets/fr/032.webp)



Kui olete sisestanud oma 50 visket, genereerib SeedSigner teie lause. **Jälgige hoolikalt selle õpetuse juhiseid, kui te alles alustate:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 seed kuvamine ja salvestamine



Kirjutage hoolikalt oma Mnemonic lause sõnad sobivale füüsilisele alusele (paberile või metallile).



![Image](assets/fr/033.webp)



### 5.5 Varukoopia kontrollimine



Et vältida varundusvigu, palub SeedSigner teil oma varundust kontrollida. Klõpsake nupule `Kontrollima`.



![Image](assets/fr/034.webp)



Seejärel sisestage soovitud sõna vastavalt selle järjekorrale lauses. Näiteks siin pean ma valima kolmandat sõna oma lauses.



![Image](assets/fr/035.webp)



Kui teete vea, teavitab SeedSigner teid sellest ja te peate uuesti alustama, märkides kindlasti oma Mnemonic fraasi, kui see teile antakse. See kontrollsamm tagab, et teie varukoopia on korrektne ja täielik. Pärast kinnitamist kuvatakse ekraanil `Backup Verified`.



![Image](assets/fr/036.webp)



Täielikuma taastamistesti saamiseks järgige seda õpetust :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Mõiste "riigita seade" mõistmine



SeedSigner on püsiva mäluta seade. See tähendab, et teie seed ei ole kunagi seadme sees salvestatud (erinevalt näiteks Ledger, Trezorist või Coldcardist). Niipea, kui lülitate voolu välja, kaob seed täielikult mälust. Kui SeedSigner taaskäivitub, naaseb see tühja olekusse: peate oma tehingute allkirjastamiseks andma sellele uuesti oma seed.



See pakub olulist kaitset. Erinevalt teistest riistvaralistest rahakottidest põhineb SeedSigner füüsilise kaitseta Raspberry Pi Zero'l, sealhulgas *secure element*. Kuid kuna tundlikke andmeid ei salvestata, ei võimaldaks isegi füüsiliselt kahjustatud seade ründajal teie isiklikke võtmeid välja võtta või bitcoine kulutada.



Teisest küljest tähendab selline arhitektuur täiendavat vastutust: ilma varunduseta on teie vahendid lõplikult kadunud. Seepärast soovitan ma **kordset varundamist**. Teil on juba olemas teie taastamislause: see on teie peamine pikaajaline varukoopia, mida tuleb hoida turvalises kohas. Nüüd loome sellest fraasist koopia **QR-koodi** kujul.



Iga kord, kui kasutate SeedSignerit, skaneerite seda QR-koodi seadme kaameraga, nii et seade laeb ajutiselt oma seed mällu, samal ajal kui te oma tehinguid allkirjastate. Ka seda teist, igapäevaseks kasutamiseks mõeldud varukoopiat tuleb hoida ülima ettevaatusega: igaühel, kelle käes see QR-kood on, on täielik juurdepääs teie bitcoinidele.


Samuti soovitan teil hoida oma QR-koodi ja Mnemonic fraasi kahes erinevas kohas, et vältida nõuete esitamise korral nende kaotamist.



Lõpuks on täiustatud ja turvalisem alternatiiv kasutada SeedSignerit koos **SeedKeeperiga**, mis salvestab seed secure element-sse. Lisateavet leiate sellest juhendmaterjalist :



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Peavõti sõrmejälje kirjutamine



Kui kontrollimine on lõpule viidud, kuvab SeedSigner teie Wallet peavõti sõrmejälje. See sõrmejälg tuvastab teie Wallet ja tagab, et kasutate tulevikus õiget taastamislauset. See ei avalda mingit teavet teie privaatvõtmete kohta, nii et saate seda turvaliselt digitaalsel andmekandjal säilitada. Lihtsalt veenduge, et te hoiate kättesaadavat koopiat ja ei kaota seda kunagi.



![Image](assets/fr/037.webp)



Selles etapis saate lisada ka **passphrase BIP39**, et tugevdada oma Wallet turvalisust. Sõltuvalt teie varundusstrateegiast võib see võimalus olla kasulik, kuid sellega kaasnevad ka riskid: kui te kaotate passphrase, on juurdepääs teie bitcoinidele jäädavalt kadunud.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Kui te ei ole veel tuttav passphrase kontseptsiooniga, siis kutsun teid üles lugema seda põhjalikku õpetust sel teemal:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 seed salvestamine QR-vormingus (*SeedQR*)



SeedSigner võimaldab teil muuta oma seed paberil olevaks QR-koodiks, mida nimetatakse *SeedQR*. See meetod lihtsustab teie Wallet ümberlaadimist, kuna sellega välditakse iga sõna käsitsi uuesti kirjutamist.



Selleks vajate tühja paberist või metallist QR-koodi, mis vastab teie Mnemonic lause pikkusele. Kui olete ostnud oma SeedSigner'ile täispaketi, on mallid tavaliselt kaasas. Kui mitte, saate need alla laadida ja välja printida (või käsitsi paljundada) siit :




- [12-sõnaline vorming](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24-sõnaline formaat](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Kompaktformaat 12 sõna](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Kompaktformaat 24 sõna](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Valige seed ekraanil "seed varundamine".



![Image](assets/fr/039.webp)



Seejärel valige `Export as SeedQR`.



![Image](assets/fr/040.webp)



Seejärel valige soovitud formaat (tavaline või kompaktne) vastavalt olemasolevale paberimallile.



![Image](assets/fr/041.webp)



Klõpsake "Alustada", et alustada *SeedQR* loomist. SeedSigner kuvab seejärel rea ruudustikke (A1, A2, B1 jne.), millest igaüks vastab koodi osale.



![Image](assets/fr/042.webp)



Korrigeeri hoolikalt iga musta punkti oma salvestuslehel, seejärel kasuta joysticki, et liikuda edasi järgmise BLOCK juurde. Võtke aega: lihtne valesti paigutamine võib muuta QR-koodi kasutuskõlbmatuks.



Mõned näpunäited:




- Alustage pliiatsiga, et saaksite kõik vead parandada, ja kui olete lõpetanud, kasutage taas musta pliiatsit;
- Vaja on vaid hästi keskendatud punkti ruutu keskel, seda ei ole vaja täielikult täita.



![Image](assets/fr/043.webp)



Seejärel klõpsake nupule `Kinnitage SeedQR` ja skannige oma QR-koodi, et kontrollida, kas see töötab õigesti.



![Image](assets/fr/044.webp)



Kui kuvatakse teade `Success`, on teie *SeedQR* kehtiv: võite jätkata järgmise sammuga.



![Image](assets/fr/045.webp)



**Hoidke seda lehte nii rangelt kui oma taastumisfraasi. Igaüks, kelle valduses on see QR-kood, võib taastada teie isiklikud võtmed ja varastada teie bitcoinid.**



Palju õnne, teie Bitcoin portfell on nüüd käivitatud! Nüüd impordime selle avalikud komponendid **Sparrow wallet**-sse, et seda hõlpsasti hallata.



## 6. Importida Wallet Sparrow-sse



Kui teie SeedSigner on seadistatud ja teie seed on õigesti loodud ja salvestatud, on järgmine samm selle portfelli sidumine haldustarkvaraga, näiteks Sparrow wallet. Teie seed jääb alati võrguühenduseta, sest Sparrow-le edastatakse ainult teie portfelli avalik osa. See võimaldab tarkvaral kuvada teie aadresse, tehinguid ja luua uusi tehinguid, ilma et te saaksite kunagi oma bitcoine kulutada. Oma bitcoinide kulutamiseks peab teie SeedSigner alati allkirjastama Sparrow poolt ettevalmistatud tehingu.



### 6.1 SeedSigneri ettevalmistamine



Sisestage operatsioonisüsteemi sisaldav microSD-mäluseade, lülitage SeedSigner sisse ja laadige seed, mille olete just loonud oma varukoopia QR-koodi abil. Valige avakuval `Scan`, seejärel skaneerige oma SeedQR-i SeedSigneriga.



![Image](assets/fr/046.webp)



Kontrollige, et teie üldvõtme sõrmejälg kattub teie Wallet sõrmejäljega. Kui kasutate passphrase, sisestage see selles etapis.



![Image](assets/fr/047.webp)



See viib teid oma portfelli menüüsse, minu puhul nimega `d4149b27`. Kui olete tagasi avalehel, valige `Seeds`, seejärel valige oma portfellile vastav väljatrükk. Seejärel klõpsake `Export Xpub`.



![Image](assets/fr/048.webp)



Valige portfelli tüüp. Meie puhul on tegemist ühe portfelliga: valige `Single Sig`.



![Image](assets/fr/049.webp)



Järgmisena tuleb valida skriptimisstandard. Uusim ja tehingukulude seisukohalt kõige ökonoomsem on "Taproot". Seepärast soovitan teil valida see standard.



![Image](assets/fr/050.webp)



Ilmub hoiatusteade. See on normaalne: see laiendatud avalik võti (`xpub`) võimaldab teil vaadata kõiki teie seed-st (esimesel kontol) saadud aadresse. See ei võimalda teil oma raha kulutada, kuid näitab teie portfelli struktuuri. Kui see kunagi lekib, on see probleem teie privaatsusele, kuid mitte teie bitcoinide turvalisusele: see võimaldab teil neid näha, kuid mitte kulutada.



Kui olete kuvatud teabega rahul, klõpsake nuppu `I Understand` ja seejärel `Export Xpub`.



SeedSigner genereerib seejärel teie xpubi dünaamilise QR-koodi kujul, mis sisaldab kõiki andmeid, mida vajate oma portfelli haldamiseks Sparrow wallet-s.



![Image](assets/fr/051.webp)



QR-koodi skaneerimise hõlbustamiseks saate kasutada joysticki ekraani heleduse reguleerimiseks.



### 6.2 Uue portfelli importimine Sparrow wallet-sse



Veenduge, et teie arvutisse on paigaldatud Sparrow wallet tarkvara. Kui te ei tea, kuidas seda alla laadida, kontrollida ja õigesti paigaldada, vaadake meie täielikku õpetust sel teemal:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Avage oma arvutis Sparrow wallet, seejärel klõpsake menüüribal "Fail → Import Wallet".



![Image](assets/fr/052.webp)



Liikuge alla "SeedSigner" juurde, seejärel valige "Scan...". Teie veebikaamera avaneb: skaneerige SeedSigneri ekraanil kuvatavat dünaamilist QR-koodi.



![Image](assets/fr/053.webp)



Määrake oma portfellile nimi, seejärel klõpsake nuppu "Loo Wallet". Seejärel palub Sparrow teil määrata parool, et lukustada kohalik juurdepääs sellele Wallet-le. Valige tugev parool: see kaitseb juurdepääsu teie portfelli andmetele Sparrows (avalikud võtmed, aadressid, sildid ja tehingute ajalugu). Seda salasõna ei ole vaja portfelli hilisemaks taastamiseks: selleks on vaja ainult teie Mnemonic fraasi (ja võimalik, et ka passphrase).



Soovitan selle parooli salvestada paroolihaldurisse, et vältida selle kaotamist.



![Image](assets/fr/054.webp)



Teie võtmesalvestus on nüüd edukalt imporditud.



![Image](assets/fr/055.webp)



Seejärel kontrollige, et Sparrow-s kuvatav "Master fingerprint" vastaks teie SeedSigneris eelnevalt märgitud sõrmejäljele.



Teie SeedSigner ja Sparrow wallet on nüüd turvaliselt ühendatud. Sparrow toimib Interface täieliku juhtimisseadmena, samas kui SeedSigner jääb ainsaks seadmeks, mis on võimeline teie tehinguid allkirjastama. Olete nüüd valmis bitcoinide vastuvõtmiseks ja saatmiseks täiesti õhuga kaetud konfiguratsioonis.



## 7. Bitcoinide vastuvõtmine ja saatmine



Teie SeedSigner ja Sparrow wallet on nüüd konfigureeritud koos töötama. Selles viimases osas vaatame, kuidas selle konfiguratsiooni abil bitcoin'e vastu võtta ja saata.



### 7.1 Bitcoinide vastuvõtmine



#### 7.1.1 Vastuvõtu genereerimine Address



Avage oma arvutis Sparrow wallet ja avage oma SeedSigner Wallet, kasutades oma parooli. Veenduge, et tarkvara on ühendatud serveriga (märkus paremal all). Klõpsake külgribal nupule `Vastuvõtmine`.



![Image](assets/fr/056.webp)



Kuvatakse uus Bitcoin Address. Näete :




- Tekst Address (alates `bc1p...`, kui kasutate P2TR nagu mina),
- Vastav QR-kood,
- Välja `Label` oma tehingute jälgimiseks.



Soovitan tungivalt lisada igale Bitcoin kviitungile sildi Wallet. See võimaldab teil hõlpsasti tuvastada iga UTXO päritolu ja parandada teie privaatsuse haldamist. Et süveneda sellesse olulisse teemasse, võite vaadata spetsiaalset koolitust Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Sildi lisamiseks sisestage lihtsalt nimi väljale "Silt" ja kinnitage.



Näiteks:



```txt
Label : Sale of the Raspberry Pi Zero
```



Teie Address on nüüd seotud selle sildiga kõigis Sparrow sektsioonides.



![Image](assets/fr/057.webp)



#### 7.1.2 Address kontroll SeedSigneril



Enne vastuvõtva Address jagamist on väga oluline kontrollida, et see kuulub teie seed juurde. See samm tagab, et teie SeedSigner saab selle Address-ga seotud tehinguid allkirjastada. Samuti kaitseb see võimalike rünnakute eest, mille puhul Sparrow kuvab võltsitud Address. Pidage meeles, et Sparrow töötab ebaturvalises keskkonnas (teie arvutis), millel on palju suurem ründepind kui teie SeedSigneril, mis on täielikult isoleeritud. Seepärast ei tohiks te kunagi pimesi uskuda ühtegi Sparrow-l kuvatavat Address vastuvõtjat, kuni te ei ole seda oma Hardware Wallet abil kontrollinud.



Sparrow-l klõpsake selle suurendamiseks Address QR-koodil: see kuvatakse seejärel täisekraanil.



![Image](assets/fr/058.webp)



Valige SeedSigneri peamenüüst käsk "Skaneerimine". Skaneerige arvuti ekraanil kuvatavat QR-koodi ja valige seejärel seed, mis vastab teie Wallet-le (minu puhul sõrmejälg `d4149b27`).



![Image](assets/fr/059.webp)



Kui skaneeritud Address vastab teie seed-st saadud Address-le, kuvatakse SeedSigneri ekraanil teade: "Address kontrollitud".



![Image](assets/fr/060.webp)



See kinnitab, et Address kuulub teie Wallet-le ja et te saate sellelt julgelt bitcoine vastu võtta.



#### 7.1.3 Raha laekumine



Nüüd saate edastada selle Address (teksti või QR-koodi kujul) isikule või osakonnale, kes peab teile saatma Satss. Kui tehing on võrgus edastatud, ilmub see Sparrow wallet vahekaardile "Tehingud".



![Image](assets/fr/061.webp)



### 7.2 Saada bitcoine



Bitcoinide saatmine SeedSigneriga on 3-etapiline protsess:




- Tehingu loomine Sparrow ;
- Tehingu allkirjastamine SeedSigneril ;
- Tehingu lõplik jaotamine Sparrow kaudu.



Kõik andmevahetused kahe seadme vahel toimuvad eranditult QR-koodide abil.



#### 7.2.1 Tehingu loomine Sparrows



Sparrow wallet-s saate klõpsata vasakpoolsel külgribal vahekaardil "Saada". Ma eelistan siiski kasutada vahekaarti `UTXOs`, mis võimaldab teil harjutada "*Coin Control*". See meetod annab teile täpse kontrolli kasutatavate UTXO-de üle, nii et saate kontrollida teavet, mida te tehingu ajal avalikustate.



Valige vahekaardil `UTXOs` mündid, mida soovite kulutada, ja seejärel klõpsake nuppu `Sendage valitud`.



![Image](assets/fr/062.webp)



Seejärel täitke tehingu väljad:




- Sisestage jaotises "Maksmine" saaja Address või klõpsake kaamera ikoonil, et skaneerida QR-koodi;
- Lisage lahtrisse "Silt" selle kulu jälgimiseks silt;
- Sisestage lahtrisse "Summa" saadetav summa;
- Lõpuks valige tasu määr, mis põhineb praegustel turutingimustel (hinnangud on kättesaadavad [Mempool.space](https://Mempool.space/)).



Kui väljad on täidetud, kontrollige hoolikalt teavet ja vajutage seejärel nuppu "Tehingu loomine >>".



![Image](assets/fr/063.webp)



Kontrollige tehingu üksikasju, et veenduda, et kõik on korrektne, seejärel klõpsake "Tehingu allkirjastamiseks lõpuleviimine".



![Image](assets/fr/064.webp)



Tehing on nüüd valmis, kuid veel allkirjastamata. [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/PSBT) kuvamiseks QR-koodina klõpsake nuppu `Show QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Tehingu allkirjastamine SeedSigneriga



Lülitage oma SeedSigner sisse ja skannige oma SeedQR-i, et pääseda oma portfelli juurde, nagu tavaliselt. Valige avaekraanilt "Skaneerimine" ja skannige seejärel Sparrow-l kuvatavat QR-koodi.



![Image](assets/fr/066.webp)



Seejärel valige oma portfellile sobiv seed.



![Image](assets/fr/067.webp)



SeedSigner tuvastab automaatselt, et tegemist on PSBT-ga, ja kuvab tehingu kokkuvõtte:




   - Saadetud summa,
   - Väljundi aadressid,
   - Sellega seotud tehingukulud.



Klõpsake nupule "Läbivaatamise üksikasjad" ja kontrollige hoolikalt kogu teavet otse SeedSigneri ekraanil. Kõige olulisemad andmed, mida kontrollida, on saadetud summa, saaja Address ja kohaldatud tasude summa.



![Image](assets/fr/068.webp)



Kui kõik on õige, valige "Kinnita PSBT", et allkirjastada tehing vastava(te) privaatvõtme(te) abil.



![Image](assets/fr/069.webp)



Pärast allkirjastamist genereerib SeedSigner uue QR-koodi, mis sisaldab allkirjastatud tehingut ja on valmis Sparrow-ga skaneerimiseks.



![Image](assets/fr/070.webp)



#### 7.2.3 Tehingu edastamine Sparrow-st



Nüüd, kui tehing on kehtiv, tuleb see edastada Bitcoin võrgus, et see jõuaks Miner-ni, kes lisab selle BLOCK-le.



Sparrows klõpsake nuppu `QR Scan`.



![Image](assets/fr/071.webp)



Esitage oma SeedSigneri kuvatud QR-kood (allkirjastatud tehingu kood) veebikaamerale. Sparrow dekodeerib allkirja ja kuvab kõik tehingu üksikasjad. Tehke viimane kontroll, et kõik andmed oleksid õiged, ja seejärel klõpsake nuppu Broadcast Transaction, et edastada tehing Bitcoin võrgus.



![Image](assets/fr/072.webp)



Teie tehing on nüüd saadetud Bitcoin võrku. Te saate jälgida selle kulgu Sparrow wallet vahekaardil "Tehingud".



![Image](assets/fr/073.webp)



Nüüd olete SeedSigneri kasutamise põhitõed omandanud. Oma teadmiste süvendamiseks ja edasijõudnute kasutusvõimaluste uurimiseks kutsun teid üles tutvuma järgmise õpetusega:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Saate toetada ka avatud lähtekoodiga projekti SeedSigner arendamist, tehes annetuse bitcoinides!](https://seedsigner.com/donate/)**



*Krediit: mõned pildid selles õpetuses pärinevad [ametliku SeedSigner projekti veebilehelt](https://seedsigner.com/) ja [GitHub repositooriumist](https://github.com/SeedSigner/seedsigner).*