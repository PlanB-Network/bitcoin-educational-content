---
nimi: GrapheneOS

kirjeldus: Graphene OS-i õpetus
---

> "[GrapheneOS](https://grapheneos.org/) on privaatsusele ja turvalisusele keskendunud mobiilne operatsioonisüsteem, mis on ühilduv Androidi rakendustega ja arendatud mittetulundusliku avatud lähtekoodiga projektina."

GrapheneOS, mis algselt asutati 2014. aastal nime all 'CopperheadOS', põhineb traditsioonilisel Androidi koodil (AOSP), kuid paljude muudatuste ja täiustustega, mille eesmärk on parandada kasutaja privaatsust ja turvalisust. GrapheneOS annab kasutajale kontrolli oma telefoni üle, mitte suurtele tehnoloogiaettevõtetele.

### Sisukord:

- Sissejuhatus
- Ettevalmistus
- Paigaldamine
- Rakenduste alternatiivid
- Puudused
- Kasulik info

Juhendaja https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md

## Miks kasutada GrapheneOS-i?

Kaasaegsed telefonid on 500–1000 dollari maksvad jälgimis- ja andmekogumisseadmed. Meie elu kõik aspektid läbivad neid ja kahjuks jagatakse palju neist andmetest mingil kujul kolmandate osapooltega.
GrapheneOS on spetsiaalselt ehitatud selle andmejagamise vähendamiseks ja teie seadme turvalisuse parandamiseks potentsiaalsete rünnakuvektorite eest. GrapheneOS-i kontot pole olemas. Te ei vaja seda rakenduste allalaadimiseks või OS-iga suhtlemiseks. Lihtsalt öeldes, te ei ole toode.

GrapheneOS pakub teie Androidi kogemusele lisaturvalisust mõne lihtsa põhiprintsiibi kaudu.

1. **Rünnakupinna vähendamine** - Eemalda tarbetu kood (või bloatware).
2. **Haavatavuse kokkupuute ennetamine** - Võimalda kasutajal piisavalt detailsust, et valida endale sobivad kompromissid.
3. **Liivakasti piiramine** - GrapheneOS tugevdab olemasolevaid Androidi liivakaste, lukustades veelgi iga rakenduse võime suhelda ülejäänud telefoniga.

Lisateavet GrapheneOS-i funktsioonide tehniliste üksikasjade kohta leiate [siit](https://grapheneos.org/features).

### Ülemineku hõlbustamine

Kui olete aastaid olnud sügavalt Google'i või Apple'i ökosüsteemis, võib kogu selle mugavuse kaotamise mõte üleöö olla hirmutav. Kuid mõningate hoolikalt kaalutletud rakenduste installimisotsustega (mida hiljem käsitletakse), saab suure osa sellest eeldatavast raskusest vähendada või kõrvaldada.

Kuigi alternatiivid muutuvad järjest paremaks, võib sellise muutuse mõte siiski olla heidutav. Kui leiate end sellisest olukorrast, on minu parim nõuanne kasutada oma uut GrapheneOS-i seadet mõnda aega kõrvuti oma olemasoleva telefoniga. Sealt saate aeglaselt loobuda 2-3 rakendusest nädalas, kuni leiate end ainult oma GrapheneOS-seadet kasutamas.

Kui võtate selle lähenemise, olge enda suhtes range ja lõpetage kiiresti sõltuvus jälgitavatest alternatiividest. Meie, inimesed, oleme laisad ja valime sageli kõige vähem vastupanu teed. Mäletage, miks te esiteks lülitasite.

**Selle asemel, et maksta oma isiklike andmetega, valisite maksmise oma ajaga ja mõnikord ka oma raskelt teenitud rahaga (sõltuvalt paigaldatavatest alternatiivsetest rakendustest).**

## Alustamine

GrapheneOS on praegu tootmises ainult _(üsna irooniliselt)_ [Google Pixel](https://grapheneos.org/faq#supported-devices) telefonide sarjale. Sellel on siiski hea põhjus. Pixel pakub parimat riistvarapõhist turvalisust, et täiendada operatsioonisüsteemi tugevdamiseks tehtud tööd. See hõlmab asju nagu konkreetsete komponentide isolatsioonid ja kontrollitud käivitamine.

### Seadme valimine

Valides Pixeli, millele soovite GrapheneOS-i paigaldada, veenduge, et kontrollite, kui kaua seade jätkab vaikimisi [turvauuenduste](https://support.google.com/pixelphone/answer/4457705?hl=et#zippy=%2Cpixel-xl-a-a-g-a-g) saamist.
Kirjutamise hetkel on Pixel 6a kõige odavam mudel, millel on hea pikaajaline tugi, garanteeritud kuni juulini 2027. Kui valite selle mudeli, ei tööta OEM avamine tehaseversiooni varude OS-iga. Peate selle uuendama juuni 2022 väljalaske või hilisema versiooni peale õhu kaudu tehtava uuenduse kaudu. Pärast uuendamist peate seadme tehasest lähtestama, et parandada OEM avamist. Kõik teised operaatorilt lukustamata mudelid on kohe karbist välja võttes valmis GrapheneOS-i jaoks.

Seadme valimisel soovite samuti veenduda, et ostate lukustamata versiooni. Teatud operaatorid nagu Verizon tarnivad oma seadmeid, mis on bootloaderiga lukustatud, mis täielikult takistab järgnevat protsessi.

### GrapheneOS-i paigaldamine

GrapheneOS [veebiinstallija](https://grapheneos.org/install/web) muudab kogu protsessi lihtsaks ja selliseks, mille saab igaüks lõpule viia alla 10 minuti.
Järgnevad juhised on lühendatud versioon ülaltoodud lingilt.

Kõik, mida vajate, on:

- Pixel
- USB-kaabel telefonist arvutisse ühendamiseks
- Arvuti veebibrauseri käitamiseks (ükskõik milline Chromiumi-põhine brauser: Chrome, Edge, Brave jne.)

1. Esimene samm on minna **Seaded** > **Telefoni kohta** ja korduvalt koputada ehitusnumbrile, kuni näete, et **'Arendaja režiim'** on aktiveeritud.
2. Seejärel minge **Seaded** > **Süsteem** > **Arendaja valikud** ja lubage **'OEM avamine'**.
3. Nüüd taaskäivitage seade ja hoidke helitugevuse vähendamise nuppu all, samal ajal kui telefon uuesti sisse lülitub.
4. Ühendage telefon oma sülearvutiga ja kui küsitakse autoriseerimist, lubage ühendus.
5. Veebiinstallija lehel klõpsake 'Ava bootloader'.
6. Seejärel näete, et telefoni valikud muutuvad. Kasutage valiku muutmiseks helitugevuse nuppu ja valiku kinnitamiseks toitenuppu.
7. Järgmisena klõpsake veebiinstallija lehel 'Laadi alla väljalase'.
8. Kui see on täielikult alla laaditud, liikuge järgmisele sammule ja klõpsake 'Paigalda väljalase'. See võtab minuti või kaks ja te ei pea telefoni üldse puudutama.
9. Lõpuks liikuge veebiinstallija järgmisele sammule ja klõpsake **Lukusta Bootloader**. Peate valiku muutma ja kinnitama toitenupuga samamoodi nagu protsessi varasemas etapis.
10. Kui näete sõna `Start`, kinnitage see toitenupuga ja seade käivitub teie uude Google-vabasse operatsioonisüsteemi.

![image](assets/2.webp)

GrapheneOS-i alguskuva

_Pärast esmast käivitamist ja seadistamist on hea tava keelata OEM avamine Seaded > Süsteem > Arendaja valikud alt._

_Samuti võiksite kaaluda täiendava, valikulise, kuid soovitatava sammu astumist installi kontrollimiseks Auditor äpi kaudu. Selle sammu lõpuleviimiseks on vaja eraldi Androidi telefoni, millel on äpp paigaldatud. Juhised selle kohta leiate [siit](https://attestation.app/tutorial)._

![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video, mis kirjeldab ülalnimetatud lihtsaid samme

Kui need lihtsad sammud tunduvad liiga keerulised, võiksite kaaluda Pixeli ostmist, millel on GrapheneOS tarkvara [eelinstalleeritud](https://ronindojo.io/en/roninmobile). Pidage lihtsalt meeles, et usaldate teenusepakkujat väikesel määral.

### Eelinstalleeritud Rakendused

Nüüd, kui olete seadistatud, võite märgata, kui paljas GrapheneOS esimesel paigaldamisel tundub. Vaikimisi on teil need rakendused paigaldatud:

![image](assets/3.webp)

Vaikimisi rakendused
Ainsad kaks, millega te ei pruugi tuttav olla, on 'Auditor' ja 'Vanadium'.
- '[Auditor rakendus](https://play.google.com/store/apps/details?id=app.attestation.auditor) kasutab riistvarapõhiseid turvafunktsioone seadme identiteedi, operatsioonisüsteemi autentsuse ja terviklikkuse kontrollimiseks. See kinnitab, et seade kasutab tehase operatsioonisüsteemi lukustatud alglaaduriga ja et operatsioonisüsteemiga ei ole manipuleeritud.'
- [Vanadium](https://github.com/GrapheneOS/Vanadium) on privaatsust ja turvalisust tugevdav Chromiumi veebibrauseri variant.

## Kohandamine

Telefoni seaded on isiklik asi, kuid siin on mõned esimesed asjad, mida ma muudan GrapheneOS-i installimisel, et end rohkem koduselt tunda.

### Taustapildi seadmine ja teema uuendamine

Mine Seaded > Taustapilt ja Stiil. Siit ma:

- Uuendan kodu- ja lukustuskuva taustapilte, kasutades veebist allalaaditud pilte.
- Valin UI-s kasutatavad aktsentvärvid.
- Lülitan sisse Tumeda teema.

### Näita aku protsenti

Mine **Seaded** > **Aku**, seejärel luba **Näita aku protsenti** olekuribal.

### Kontaktide importimine

**Teisest Androidi telefonist** - Mine Kontaktide rakendusse ja otsi Ekspordi VCF valikut.

**iOS-ist** - Kasuta rakendust nagu Export Contact ja kasuta 'vCard' ekspordi valikut, et eksportida VCF fail.
Kui sul on VCF fail, saad selle üle kanda oma GrapheneOS seadmesse, kasutades välist salvestusvõimalust nagu microSD kaart või USB draiv. Kui sul neid käepärast pole, võid valida jagamise ühe paljudest allpool loetletud rakendustest.

![image](assets/4.webp)

Isikupärastatud avakuva


## Alternatiivsed Rakendused

Et muuta oma telefon kasulikuks, tahad sa kindlasti paigaldada mõningaid rakendusi! Järgnevad valikud on kaasatud, kuna olen neid kõiki isiklikult kasutanud või kuna need on saanud tugevaid soovitusi laiemalt privaatsuskogukonnalt. On palju teisi suurepäraseid alternatiive, mida ei ole mainitud, ja [Awesome Privacy](https://awesome-privacy.xyz) pakub uskumatult laia valikut privaatsust säilitavaid rakendusi igat tüüpi seadmetele.

Lihtsalt sellepärast, et rakendus on vaba ja avatud lähtekoodiga tarkvara (FOSS), ei tähenda see, et see oleks vaba potentsiaalsetest privaatsusleketest. Kasuta [Exodus](https://reports.exodus-privacy.eu.org/en/) selleks, et näha, kuidas sinu eelistatud rakendused läbivad nende privaatsusauditeid.

### F-Droid

[F-Droid](https://f-droid.org/) on installitav FOSS rakenduste kataloog Androidile. Klient muudab rakenduste sirvimise, paigaldamise ja uuendamise seadmes lihtsaks. On väärt mainida, et uuendused F-Droidi kaudu võivad mõnikord olla aeglasemad kui teiste rakenduste poodide puhul. See sõltub peamiselt sellest, kas rakendus leitakse peamisest F-Droidi repositooriumist või mõnest kohandatud repositooriumist.

F-Droidi paigaldamiseks lihtsalt mine nende veebilehele oma GrapheneOS telefoni brauseri kaudu ja koputa allalaadimisele. Seejärel laaditakse alla `.apk` fail. Seejärel küsitakse, kas soovid rakendust installida.

Lisaks rakendustele, mis leitakse F-Droidi vaikimisi repositooriumist, võivad paljud avatud lähtekoodiga projektid samuti majutada oma repositooriumit, mida saab lisada F-Droidi rakenduse seadetes. Kui see on nii, siis vastav projekt juhendab sind nende veebilehel vajalike väga lihtsate sammude läbimisel.

![image](assets/5.webp)

F-Droidi avakuva

### Aurora Store
[Aurora Store](https://auroraoss.com/) on FOSS versioon Google Play poest. Aurora välimus ja kasutajakogemus on väga sarnane traditsioonilisele Play Store'ile ning see võimaldab teil alla laadida ja uuendada mis tahes rakendust, mida tavaliselt Google'i valiku kaudu leiate.
Aurora tapjafunktsiooniks on anonüümne sisselogimine. See tähendab, et saate alla laadida mis tahes oma lemmikrakendusi, mis pole saadaval F-Droidi kaudu või otse APK-na, ilma et peaksite olema sisse logitud oma Google'i kontole.

Enne kui kiirustate selle oma vaikimisi installimisvalikuks tegemisega, pidage meeles, et paljud rakendused, millest me üritame eemale hoida, on installitud Play Store'ist. Lihtsalt seetõttu, et need on Aurorast kättesaadavad, ei muuda see asjaolu, et mõned võivad sisaldada jälgimisfunktsioone. See ei pruugi alati võimalik olla, kuid iganes saate, otsige enne Aurora kaudu allalaadimist F-Droidi alternatiivi.

Aurora installimiseks otsige lihtsalt F-Droidist 'Aurora Store'.

Auroral on ka mõned potentsiaalsed rünnakute vektorid, kuna "anonüümsed kontod" on tegelikult loodud ja kontrollitud Aurora poolt. Teoreetiliselt võiksid nad pakkuda pahatahtlikke uuendusi või lükata rakendusi teie telefoni, kuigi installimise käsule seadmes ikkagi peaks nõustuma. Auroral on mõnikord ka probleeme rakenduste mitteilmumisega seoses piirkonna ja seadme valesti lugemisega. Seda saab tavaliselt ümber töötada allpool toodud sammudega.

**Parim nipp** - Mõnikord võib Aurora Store kogeda kiiruspiiranguid, mis piiravad teie võimet rakendusi otsida ja installida. Sellest mööda minemiseks minge **Seaded** > **Rakendused** > **Aurora** > **Ava vaikimisi**, seejärel lisage domeen `play.google.com`. Nüüd, kui navigeerite toote või teenuse veebisaidile, millel on 'Lae alla Play Store'i kaudu' link, avaneb selle rakenduse allalaadimiseks Aurora.

![image](assets/6.webp)

Aurora Store avakuva

### APK allalaadimine

Androidi rakendusi saab samuti alla laadida ja installida `.apk` faili kaudu. See on suurepärane alternatiiv, mis ei nõua kolmandate osapoolte rakenduste poode, lihtsalt laadige fail otse projekti või teenuse veebisaidilt või GitHubi repositooriumist alla.

Selle lähenemise puuduseks on see, et te ei saa automaatseid uuendusi, nii et peate jälgima selle teenuse suhtluskanaleid, et teada saada uutest väljalasetest. Siiski on olemas suurepärane projekt nimega Obtanium, mis püüab seda parandada. [Obtainium](https://github.com/ImranR98/Obtainium) võimaldab teil installida ja uuendada avatud lähtekoodiga rakendusi otse nende väljalasete lehtedelt ning saada teavitusi, kui uued väljalasked on saadaval.

![image](assets/7.webp)

Obtaniumi eelvaade

### Veebirakendused

Ajaks, kui soovite teenust harva kasutada ja ei soovi alla laadida põlisrakendust, võite lihtsalt kasutada veebiversiooni. Paljud veebisaidid pakuvad tänapäeval ka progressiivse veebirakenduse (PWA) tuge. See tähendab, et saate teatud veebisaidi (nt Twitter.com) järjehoidjana oma telefoni avakuval salvestada. Seejärel, kui vajutate ikoonile, avaneb see täisekraanirakendusena ilma tavaliste brauserikogemuse häirivate elementideta. Allpool näete, kuidas see välja näeb.

Selle saavutamiseks Vanadiumis, GrapheneOS-i põhisirvikus, lihtsalt navigeerige valitud veebisaidile, puudutage ekraani paremas ülanurgas kolme vertikaalset punkti ja seejärel puudutage **'Lisa avakuva'**.

Selle lähenemise ainus puudus on see, et kuna see on lihtsalt järjehoidjaga veebileht, ei saa te mingit teavituste vormi. Kuigi mõned võivad seda pidada positiivseks!

![image](assets/8.webp)

Twitter PWA

### Veebibrauserid
Te ei saa eelnevalt pakendatud valikuga, Vanadiumiga, tõesti valesti minna. Rakendus käitub identaalselt mis tahes muu mobiilibrauseriga, mida olen proovinud, ja mul pole kunagi olnud ühilduvusprobleeme.
Kui vajate juurdepääsu Tori põlistele `.onion` saitidele, saate Tori brauseri APK otse nende [veebisaidilt](https://www.torproject.org/download/#android) või F-Droidi kaudu alla laadida.

### VPN-id

Et kaitsta oma veebitegevust uudishimuliku internetiteenuse pakkuja (ISP) eest, on heaks valikuks Virtuaalne Privaatvõrk (VPN). VPN saadab teie internetiliikluse krüpteeritud tunneli kaudu jagatud IP-aadressile, mida kontrollib VPN-teenuse pakkuja, tagamaks, et teie seadme tegevust ei saa teiega seostada.

Järgnevad on 3 hästi respekteeritud valikut, mis võimaldavad teil teenuse eest maksta Bitcoinides ja ilma isiklikku teavet esitamata. Kõik 3 valikut on saadaval F-Droidi kaudu.

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)

### Sõnumivahetus

Viimastel aastatel on krüpteeritud sõnumivahetuslahendused muutunud arvukaks. Probleemiks jääb siiski see, et kui teil pole kontakte, kes seda kasutavad, mis mõte sel on?

Enamik inimesi, kes ei huvitu privaatsuse valdkonnast, kasutavad tõenäoliselt WhatsAppi või iMessage'i. Esimest saab alla laadida Aurora poest, kuid viimane ei tööta GrapheneOS-is (ilmselgelt!).

- [Signal](https://signal.org/) on üks populaarsemaid otsast lõpuni krüpteeritud (E2EE) sõnumivahetusrakendusi, millel on tugev ajalugu ja rikkalik funktsioonide komplekt. Signal nõuab registreerumiseks telefoninumbrit, nii et kui plaanite vestelda inimestega, kellele te ei sooviks oma telefoninumbrit avaldada, võiksite kaaluda mõnda alternatiivi. Signali tuleb alla laadida Aurora poest.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) on suhteliselt uus E2EE sõnumivahetusrakendus. Sellel puudub kasutaja ID, see ei nõua telefoninumbrit ega isiklikku teavet. Inimesed leiavad teid, skaneerides teie isiklikku QR-koodi või külastades teie unikaalset linki. Simplex võimaldab ka edasijõudnud kasutajatel oma serverit käitada, vähendades veelgi sõltuvust mis tahes tsentraliseeritud üksusest. Simplexil puudub lauaarvuti klient, seega ei pruugi see olla sobiv, kui mitme seadme kasutamine on teie prioriteetide nimekirjas. Simplex Androidile on saadaval F-Droidi kaudu.
- [Threema](https://threema.ch/en/faq/libre_installation) pakub sarnast kogemust Simplexiga, kuid on olnud olemas kauem ja seetõttu tundub veidi viimistletum. Threema ei ole tasuta, eluaegne litsents maksab 4,99 dollarit ja seda saab osta Bitcoinidega. Threema pakub veebiklienti ja lauaarvutirakendusi. Androidi rakendus on saadaval F-Droidi kaudu.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) on ametliku Telegrami rakenduse Androidile mitteametlik FOSS-fork. Telegramil on E2EE "salajased vestlused", kuid vaikimisi valik ei ole privaatne. Telegram FOSSi saab alla laadida F-Droidist.

![pilt](assets/9.webp)
Vasakul: Threema
Paremal: Simplex

### Meedia
- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) on platvormideülene Spotify klient, mis ei nõua Premium konto olemasolu. Spotube on saadaval F-Droidi kaudu.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) on suurepärane rakendus, mis võimaldab tasuta striimida muusikat YouTube Musicust. ViMusic on saadaval F-Droidist.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) pakub YouTube'i kogemust ilma tüütute reklaamide ja küsitavate lubadeta. NewPipe'iga saate tellida kanaleid, kuulata taustal ja isegi alla laadida offline vaatamiseks. NewPipe on kättesaadav F-Droidi kaudu.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) on podcastide mängija, mis võimaldab tellida ja hallata kõiki teie lemmiksaateid. AntennaPod on saadaval F-Droidi kaudu.

![image](assets/11.webp)

Vasakul: Spotube
Paremal: ViMusic

### Kaardid

Kui soovite sõidu ajal kasutada GrapheneOS-is kaardirakendust ja saada häälassistentsi, peate installima [RHVoice](https://rhvoice.org/installation/) ja [seadistama](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) selle.

- [Magic Earth](https://www.magicearth.com/) on kaardirakenduse alternatiiv, mis toetab pöördepõhist navigeerimist, 3D ja offline kaarte. Magic Earthi saab alla laadida Aurora poest.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) on kaardirakenduse alternatiiv reisijatele, turistidele, matkajatele ja jalgratturitele, mis põhineb kogukonna loodud OpenStreetMap andmetel. See on privaatsust väärtustav, avatud lähtekoodiga haru Maps.me rakendusest (varasemalt tuntud kui MapsWithMe). See toetab kõiki funktsioone ilma aktiivse internetiühenduseta ja on allalaaditav F-Droidist.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) on veel üks suurepärane kaardirakenduse alternatiiv, mis toetab kõiki eelpool mainitud funktsioone.

![image](assets/13.webp)

Vasakul: Magic Earth
Paremal: Organic Maps

### E-post

- [Proton Mail](https://proton.me/mail) pakub tasuta privaatset e-posti teenust, mis toetab auditeeritud E2EE-d. Proton pakub ka tasulist versiooni, mis toetab kohandatud domeene ja [aliaseid](https://proton.me/support/creating-aliases). Proton Maili saab alla laadida otse APK-na või Aurora kaudu.
- [Tutanota](https://tutanota.com/) pakub samu funktsioone nagu Proton Mail, sealhulgas valikulisi tasulisi teenuseid ja on allalaaditav otse APK-na või F-Droidi kaudu.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) on avatud lähtekoodiga e-posti klient, mis töötab praktiliselt iga e-posti pakkujaga. See toetab mitut kontot, ühtset postkasti ja OpenPGP krüpteerimisstandardit.

![image](assets/15.webp)

Vasakul: Proton Mail
Paremal: Tutanota

### Tootlikkus

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) on failide sünkroniseerimise programm. See sünkroniseerib faile reaalajas kahe või enama seadme vahel, olles kaitstud uudishimulike silmade eest. Teie andmed kuuluvad ainult teile ja teil on õigus valida, kus neid hoitakse, kas neid jagatakse kolmanda osapoolega ja kuidas neid interneti kaudu edastatakse. Syncthing on saadaval F-Droidi kaudu.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) võimaldab kõigil teie seadmetel kodus võrguga ühendudes omavahel lihtsalt suhelda. Saatke hõlpsalt faile, fotosid, lõikelaua andmeid kõikide oma seadmete vahel (isegi iOS-il!). KDE Connecti saab alla laadida F-Droidist.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) on E2EE märkmerakendus, mis võimaldab sünkroniseerida teie mõtteid ja to-do nimekirju kõikide oma seadmetega. Nende tasuta plaan peaks katma enamiku isiklikke kasutusjuhte. Notesnook on saadaval F-Droidis.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) on väga sarnane Notesnookiga, kuid vajab tasulise plaani olemasolu, et pakkuda samaväärset funktsionaalsust. Standard Notes on saadaval läbi F-Droidi.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) on klaviatuuri rakendus, mis võimaldab teil kohandada peaaegu kõike, mida oma telefoni tippimiskogemuse juures ette kujutada võite. Seda saab alla laadida F-Droidi kaudu.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) on Google'i vaikimisi klaviatuuri rakendus. Minu kogemuse põhjal pakub see kaugelt parimat tippimis- ja libistamiskogemust. Kui laadite selle rakenduse alla, veenduge, et keelate täielikult kõik võrguga seotud load. Seda saab alla laadida Aurora kaudu.

![image](assets/17.webp)

Vasakul: Notesnook
Paremal: KDE Connect

### Elustiil

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) on ilusalt kujundatud avatud lähtekoodiga ilmarakendus, mis on saadaval F-Droidi kaudu. See toetab ka mitmesuguseid vidina suurusi, nii et saate oma valitud asukoha ilma kohe oma avakuvalt näha.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) on avatud lähtekoodiga ja privaatsust säilitav tõlkerakendus, mis toetab enam kui 200 keelt. Translate You on saadaval F-Droidi kaudu.
- [Proton Calendar](https://proton.me/calendar/download) on lihtsalt kasutatav E2EE kalender, mis suhtleb sujuvalt teie Protoni e-posti kontodega. Proton Calendari saab alla laadida APK-na või Aurora poest.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) on rakendus pardakaartide, kupongide, kinopiletite ja liikmekaartide jms kuvamiseks ja talletamiseks. Lihtsalt laadige alla vastav `pkpass` või `espass` fail ja avage rakendusega. PassAndroid on saadaval F-Droidi kaudu.

![image](assets/19.webp)
Vasakul: Geometric Weather
Paremal: Proton Calendar

### Turvalisus/Privaatsus

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) pakub tasuta ja E2EE ristplatvormi paroolihalduse lahendust kõigile teie seadmetele. Nende tasuline teenus võimaldab integreerida 2FA koode rakendusse. Bitwardeni serveripoolt saab ise majutada ja Androidi rakendus on saadaval F-Droidi kaudu.
- [Proton Pass](https://proton.me/pass/download) pakub sarnast tasuta teenust nagu Bitwarden, kuid [Proton Unlimited](https://proton.me/pricing) klientidele on kättesaadavad lisatud edasijõudnud funktsioonid. Proton Pass on saadaval APK või Aurora kaudu.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) on kahefaktorilise autentimise rakendus süsteemidele, mis kasutavad ühekordse parooli protokolle. Tokeneid saab hõlpsasti lisada QR-koodi skaneerides. FreeOTP on saadaval F-Droidi kaudu.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) on tasuta, turvaline ja avatud lähtekoodiga rakendus Androidile, et hallata teie 2-etapilise autentimise tokeneid teie veebiteenustele. Aegis on saadaval F-Droidi kaudu.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) on tasuline, platvormideülene teenus, mis krüpteerib teie andmed kohapeal, et saaksite need turvaliselt oma lemmikpilveteenusesse üles laadida. Cryptomatori saab alla laadida F-Droidi kaudu.

![pilt](assets/21.webp)
Vasakul: Proton Pass
Paremal: Bitwarden

### Pilvelahendused

- [Proton Drive](https://proton.me/drive/download) on tasuline E2EE pilvelahendus kõigi teie failide varundamiseks ja salvestamiseks. Kirjutamise hetkel on nad just teatanud Windowsi lauaarvutikliendi väljaandmisest, kuid Maci ja Linuxi kasutajad peavad oma arvutitest sünkroonimiseks jätkuvalt kasutama veebiversiooni (esialgu). Androidi klient on saadaval APK-na või Aurora kaudu.
- [Skiff](https://skiff.com/download) pakub samuti tasulist E2EE pilvesalvestust ja failikoostöö tööriistu. Nad pakuvad Maci ja Windowsi lauaarvutiklienti (samuti veebirakendust) ja nende Androidi kliente tuleb alla laadida Aurorast.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) pakub täielikult varustatud pilvepõhist lahendust koostööks, seadmetevaheliseks sünkroonimiseks ja failihoidlaks. Edasijõudnud kasutajad võivad valida oma vaba ja avatud lähtekoodiga tarkvara ise hostida mis tahes riistvaral, mida nad soovivad. Androidi kliendid saab alla laadida F-Droidi kaudu.
- [Cryptpad](https://cryptpad.fr/) pakub tasuta, veebipõhist, E2EE alternatiivi Google Docsidele.

![pilt](assets/23.webp)

Proton Drive

## Puudused

Avatud lähtekoodiga ja privaatsust säilitavad alternatiivid tehnoloogiakonglomeraatide rakendustele, mida olete harjunud kasutama, on rohked ja mõned neist on sageli paremad kui suletud lähtekoodiga, nuhkvaraga koormatud alternatiivid.

Siiski, kui liigute GrapheneOS-i peale, on mõned mugavused, millest peate loobuma, kuna alternatiive ei ole. Nende hulka kuuluvad:

- **Apple CarPlay/Android Auto** - Peate leppima hea vanamoodse Bluetoothi, USB või Aux'iga.
- **Apple/Google Pay** - Peaaegu kõik kannavad niikuinii oma rahakotti kaasas!
- **Pangarakendused** - Pole nii, et need üldse ei tööta. Mõned töötavad, täiesti laitmatult isegi. Teised töötavad ainult Google Play teenuste lubamisel (loe selle kohta allpool) ja mõned lihtsalt ei tööta üldse. Loe oma panga kohta [siit](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) praeguse olukorra kohta. Ärge muretsege, kui teie oma on nimekirjas, mis ei tööta, pidage meeles, et saate URL-i salvestada veebirakendusena oma avakuval.
- **Push-teavitused** - Enamik rakendusi, mis saadavad teile uuendusi, kui te ei kasuta konkreetset rakendust, teevad seda Google Play teenuste kaudu. Need ei ole GrapheneOS-iga vaikimisi installitud, nii et kui te ei saa kohe teavitust, kui teie sõber teile e-kirja saadab, on see tõenäoliselt põhjus. Hea uudis on see, et mõned ülalmainitud rakendused on rakendanud oma taustühenduse, et perioodiliselt uuendusi kontrollida ja vajadusel teile teavituse anda.

### Liivakastitud Google Play
GrapheneOS sisaldab ühilduvuskihti, mis pakub võimalust paigaldada ja kasutada Google Play ametlikke väljalaskeid standardse rakenduse liivakastis. Google Play ei saa GrapheneOS-is mingisuguseid eriõigusi või privileege võrreldes rakenduse liivakasti mööda hiilimisega ja suure hulga kõrge privileegiga juurdepääsu saamisega.

Kui leiate, et ei saa ilma nende tõuketeavitusteta oma lemmikrakenduse jaoks või teatud "hädavajalik" rakendus on kasutu ilma Play teenusteta, võimaldab GrapheneOS teil need teenused paigaldada täielikult liivakastitud keskkonnas. Paigaldatuna ei nõua need teenused Google'i konto olemasolu töötamiseks ja igaühe õigusi saab rangelt kontrollida.

Enne kui tormate neid esimesel päeval paigaldama, soovitan teil näha, kui kaugele jõuate ilma nendeta. Tõenäoliselt üllatute, kui paljud rakendused toimivad täiesti normaalselt ilma nendeta.

Kui soovite need siiski paigaldada, puudutage lihtsalt eelinstallitud 'Rakendused' rakendust, millele järgneb 'Google Play teenused'. Kaaluge nende paigaldamist koos nende vähem privaatsete rakendustega, mida te ei saa elada ilma, täiesti eraldi kasutajaprofiilis, et pakkuda seda lisakihti eraldatust ülejäänud telefonist.

![image](assets/24.webp)

Play teenuste paigaldamise ekraan

### Profiilid

GrapheneOS võimaldab teil omada eraldi telefoni kogemust oma telefonis. Lisaprofiilid saavad paigaldada oma rakendusi ja teenuseid ning ei saa juurdepääsu omaniku konto failidele või andmetele.
Kui teil on ainult üks või kaks neist hädavajalikest rakendustest, mis nõuavad Play teenuseid, kuid kasutate neid väga harva, võib nende paigaldamine koos Play teenustega eraldi profiilis olla suurepärane idee, et veelgi tugevdada mis tahes väikseid privaatsusprobleeme, mis jäävad nende töötamisest omaniku profiilis.

Selle kasutusjuhu kohta saate rohkem lugeda [siit](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).

Kui otsustate lisada eraldi profiili, mis sobib teie kasutusjuhuga, võib rakendus [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) teile kasulik olla. Insular võimaldab teil hõlpsalt kloonida oma olemasolevaid rakendusi uude profiili ilma vajaduseta minna läbi traditsioonilistest paigaldusteedest, mida varem selles juhendis käsitleti. Insular võimaldab teil ka kiiresti "külmutada" ükskõik millise neist rakendustest, et täielikult keelata kõigi selle rakenduse taustateenuste töötamine.

![image](assets/24.webp)

Kasutajaprofiili haldamise ekraan

### e-SIMid

Kui soovite viia oma telefoni privaatsuse järgmisele tasemele ja omada mobiiliteenust, mis on lahti ühendatud teie pärismaailma identiteedist, võib e-SIM olla teie jaoks. e-SIM on virtuaalne SIM, mille saate veebis osta ja oma telefoni lisada QR-koodi kaudu. Selliseid teenuseid pakkuvad ettevõtted, mida saab anonüümselt maksta Bitcoiniga, hõlmavad [Silent.Link](https://silent.link/) ja [Bitrefill](https://www.bitrefill.com/gb/en/esims/).

e-SIMe ei tohiks vaadelda kui täielikku lahendust telefoni privaatsusele. Need võivad olla kasulikud tööriistad õigetes kätes, kuid palun tehke oma uurimistööd [kompromisside](https://grapheneos.org/faq#cellular-tracking) kohta, mis kaasnevad mis tahes tüüpi mobiiliteenuse kasutamisega, kui teie kavatsus on minna täielikult "võrgust välja".

Liivakastitud Play teenused peavad olema paigaldatud e-SIMi seadistamiseks GrapheneOS-is.

## Varukoopiad
Pärast oma uue de-Googled Pixel telefoni seadistamist on hea mõte luua endale varukoopia. See varukoopia võimaldab teil telefoni taastada identseks seisundiks juhul, kui kaotate telefoni või see varastatakse/kaduma läheb.
Võite valida varukoopiate salvestamise mis tahes välistele andmekandjatele või isehostitavale pilvelahendusele nagu Nextcloud, kuigi mõned kasutajad teatavad erinevatest edukuse tasemetest viimase võimaluse puhul.

Oma esimese varukoopia loomiseks:

1. Minge **Seaded** > **Süsteem** > **Varundamine**, seejärel kirjutage üles oma 12-sõnaline taastekood. See kood on vajalik varukoopiate faili hilisemal kuupäeval dekrüpteerimiseks. Koodi kaotamine tähendab juurdepääsu kaotamist telefoni varukoopiale.
2. Järgmisena valige oma salvestuskoht. Soovitaksin välist USB-draivi või tööstusliku klassi microSD-kaarti.
3. Valige varundatavad andmed. Kui teie määratud salvestusmeedial on ruumi, soovitaksin valida kõik.
4. Puudutage paremas ülanurgas kolme punkti ja valige **Varunda kohe**.

![pilt](assets/26.webp)

Varundamise ekraan

Pidage meeles, et kui teete varukoopiaid välisele salvestusmeediale, on mõistlik seda sammu regulaarselt korrata, et tagada telefoni hiljutiste oluliste uuenduste säilimine, kui halvim peaks juhtuma.

![video](https://www.youtube.com/embed/eyWmcItzisk)

Video, mis kirjeldab varundamisprotsessi

## Järeldus

Viimastel aastatel on GrapheneOS tarkvara märkimisväärselt küpsenud. See on stabiilsem ja ühilduvam kui kunagi varem. Kombineerides seda õitseva avatud lähtekoodiga ja privaatsust säilitava rakenduste ökosüsteemiga, muudab see GrapheneOS-i tõeliselt elujõuliseks alternatiiviks tavapärasele Androidile või iOS-ile, isegi "tavalistele" inimestele nagu sina!

Andmelekkeid ja massjälgimist peetakse tänapäeva maailmas nii tavaliseks, et need vaevu jõuavad pealkirjadesse. Sinu kaitse on sinu enda kätes. Tee peal tuleb teha kohandusi ja ohverdusi, kuid oma kokkupuute vähendamine selliste rikkumistega pole sugugi nii keeruline, kui arvata võib.

Loodan, et see juhend aitab sind sinu teekonnal. Kui leidsid selle juhendi kasuliku ja sooviksid toetada minu tööd, kaalu palun [annetuse](/tips) tegemist.

Kui oled juba GrapheneOS-i kasutaja või saad selleks tänu sellele juhendile, kaalu [annetuse](https://grapheneos.org/donate) tegemist, et toetada nende olulist tööd.

### Lisateave

GrapheneOS on küülikuauk, kuhu võiks kergesti kulutada nädalaid. On nii palju, mida saab õppida ja kohandada, et kohandada kogemust vastavalt oma vajadustele ja ohumudelitele. Allpool on mõned lingid, kust saate oma teekonda jätkata:

- [GrapheneOS ametlik kasutusjuhend](https://grapheneos.org/usage) - Ametlik veebisait
- [GrapheneOS foorum](https://discuss.grapheneos.org/) - Ametlik veebisait
- [GrapheneOS seadete meistriklass](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video 'The Privacy Wayfinder' poolt
- [GrapheneOS üldine podcast](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast 'Watchman Privacy' poolt

täielik krediit: https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md