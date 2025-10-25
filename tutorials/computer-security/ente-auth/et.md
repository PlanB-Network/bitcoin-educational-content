---
name: Ente Auth
description: Avatud lähtekoodiga, otsast lõpuni krüpteeritud 2FA autentifikaator
---
![cover](assets/cover.webp)



Kahefaktoriline autentimine (2FA) on muutunud hädavajalikuks meie võrgukontode kaitsmisel. Lisaks tavapärasele paroolile on vaja ajutist koodi, mille tavaliselt genereerib spetsiaalne rakendus. See mehhanism, mida nimetatakse TOTP (Time-Based One-Time Password), tagab, et isegi kui teie salasõna on ohustatud, ei saa ründaja teie kontole ligi ilma selle teise, iga 30 sekundi tagant uuendatava faktorita.



Õige autentimisrakenduse valimine ei ole siiski triviaalne. Kuigi Google Authenticator on populaarne, on tal suured piirangud: patenteeritud koodi on võimatu kontrollida, sünkroniseerimine ilma otsast lõpuni krüpteerimiseta ja koodide täieliku kadumise oht, kui telefoniga tekib probleem. Teised lahendused, näiteks Authy, nõuavad telefoninumbrit ja ei taga täielikku konfidentsiaalsust.



**Ente Auth** paistab silma kui kaasaegne ja turvaline alternatiiv. See tasuta, avatud lähtekoodiga, platvormideülene rakendus, mille on välja töötanud [Ente Photos] (https://ente.io) taga olev meeskond, pakub läbivalt krüpteeritud pilves varukoopiaid ja sujuvat sünkroniseerimist kõigi teie seadmete vahel. Erinevalt patenteeritud lahendustest annab Ente Auth teile täieliku kontrolli oma autentimiskoodide üle, ilma et teie privaatsust ohustataks.



Selles õpetuses näitame teile samm-sammult, kuidas paigaldada ja kasutada Ente Auth'i ning miks see lahendus erineb traditsioonilistest autentimisvahenditest.



## Ente Auth'i tutvustamine



Ente Auth on välja töötatud meeskonna poolt, kes on välja töötanud Ente Photos, lõpuni krüpteeritud ja privaatsussõbraliku fotode salvestamise teenuse. Vastavalt Ente filosoofiale ("Ente" tähendab malajalaami keeles "minu", mis sümboliseerib kontrolli oma andmete üle) on Ente Auth loodud selleks, et anda kasutajatele tagasi täielik kontroll nende kahefaktorilise autentimise koodide üle.



### Peamised omadused



**Standardsed TOTP-koodid**: Ente Auth genereerib ajutisi koode, mis ühilduvad enamiku teenustega (GitHub, Google, Binance, ProtonMail jne). Saate lisada nii palju 2FA-kontosid kui vaja ja rakendus arvutab koodid esitatud saladuste põhjal.



**Komplektne krüpteeritud pilves varundamine**: Teie koodid salvestatakse turvaliselt võrgus. Ainult teie saate neid dekrüpteerida - krüpteerimisvõti tuleneb teie paroolist ja on teada ainult teile. Ente (server) ei tea teie saladusi ega isegi teie konto pealkirju, sest kõik on krüpteeritud kliendi poolel, kasutades nullteabe arhitektuuri.



**Multi-seadmete sünkroniseerimine**: Saate paigaldada Ente Auth mitmesse seadmesse (nutitelefon, tahvelarvuti, arvuti) ja pääseda oma koodidele ligi kõigis seadmetes. Kõik muudatused levivad automaatselt ja koheselt teie teistesse seadmetesse krüpteeritud pilve kaudu, mis annab teile suure paindlikkuse igapäevatöös.



**Minimalistlik, intuitiivne Interface**: Rakendus pakub lihtsustatud Interface, mida on lihtne õppida ka mittetehnilistel kasutajatel. 2FA-kontod kuvatakse koos teenuse nime, teie sisselogimise ja 6-kohalise koodiga, mida ajakohastatakse reaalajas. Ente Auth kuvab ka järgmise koodi paar sekundit ette, et vältida lühikese aja möödumist.



** Avatud allikas ja auditeeritud**: Ente Auth'i lähtekood on [avalik GitHubis](https://github.com/ente-io/auth) AGPL v3.0 litsentsi alusel. Iga arendaja saab seda auditeerida, et kontrollida vigade või soovimatu käitumise olemasolu. Rakendatud krüptograafia on läbinud [sõltumatu välisauditi](https://ente.io/blog/cryptography-audit/), mis on garantii rakenduse turvalisuse tõsiseltvõetavuse kohta.



### Eelised ja piirangud



**Hüvitised:**




- Disainitud privaatsus koos läbiva krüpteerimisega
- Turvaline sünkroniseerimine kõigi teie seadmete vahel
- Auditeeritav avatud lähtekood
- Interface selge, intuitiivne kasutaja Interface
- Automaatne varundamine koodide kadumise vältimiseks
- Kättesaadav kõigil platvormidel (mobiil- ja lauaarvuti)



**Piirangud:**




- Sünkroonimiseks on vaja internetiühendust
- Edasijõudnud kasutajad võivad eelistada 100% offline lahendusi nagu Aegis (ainult Android)
- Suhteliselt uus võrreldes väljakujunenud lahendustega



## Paigaldamine



Ente Auth on saadaval kõige populaarsematel platvormidel. Rakenduse saate alla laadida [ametlikust veebisaidist](https://ente.io/auth) või ametlikest kauplustest.



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth allalaadimisleht koos kõigi olemasolevate platvormidega*



### Android


Teil on mitu võimalust:




- **Google Play Store**: Otsi "Ente Auth" klassikalise paigalduse jaoks
- **F-Droid**: Saadaval Androidi avatud lähtekoodiga rakenduste kataloogist, mille puhul on tagatud kontrollitud konstruktsioon ja mille sisu ei ole kaitstud
- **Käsitsi paigaldamine**: APK-faile saab alla laadida [projekti GitHubi lehelt](https://github.com/ente-io/auth/releases) koos integreeritud teavitusega uutest versioonidest



### iOS (iPhone/iPad)


Installige Ente Auth otse Apple App Store'ist, otsides rakenduse nime. IOS-i rakendust saab käivitada ka Apple Silicon'i kiibiga (M1/M2) varustatud Macidel Mac App Store'i kaudu.



### Arvutid (Windows, macOS, Linux)


Ente Auth pakub originaalseid töölauarakendusi. Külastage [ente.io/download](https://ente.io/download) või [Releases section of GitHub](https://github.com/ente-io/auth/releases) :





- **Windows**: Komplektis on EXE-installatsiooniprogramm
- **macOS**: Lohistage ja laske DMG-ketta kujutis rakendustes
- **Linux**: Saadaval on mitu formaati (AppImage portable, .deb Debian/Ubuntu jaoks, .rpm Fedora/Red Hat jaoks)



**Märkus:** See õpetus põhineb Ente Auth v4.4.4 ja hilisematel versioonidel. Varasemates versioonides võib olla väiksemaid Interface erinevusi.



### Interface Web


Ilma installimiseta saate oma koodidele ligi [auth.ente.io](https://auth.ente.io) kaudu mis tahes brauserist. Interface veebis on piiratud koodide vaatamisega (kasulik tõrkeotsinguks), kuna kontode lisamine nõuab turvalisuse huvides mobiil- või töölauarakendust.



## Esimene konfiguratsioon



### Konto loomine



Ente Auth'i esmakordsel käivitamisel on teil kaks võimalust:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Ente Auth avakuva koos konto loomise võimalustega*



**Kontoga (soovitatav)**: Valige "Create Account" ja sisestage oma e-posti aadress Address ja parool. **Tähtis**: see parool on teie andmete krüpteerimise põhiparool. Valige tugev ja unikaalne parool, kuna tavapärane andmete kaotamiseta lähtestamise protseduur puudub. Kui te selle valesti ära panete, on teie krüpteeritud andmed taastamatuks muutunud.



**Offline-režiim**: Valige "Kasuta ilma varukoopiateta", et kasutada rakendust lokaalselt ilma pilveta. Selles režiimis jäävad teie koodid seadmesse, kuid nende kaotamise vältimiseks peate need käsitsi eksportima.



![Vérification email et récupération de clé](assets/fr/03.webp)



*E-posti kinnitamise protsess ja 24-sõnalise taastamisvõtme genereerimine*



Konto loomise kinnitamiseks ja uue seadme taastamise võimaldamiseks võib nõuda e-posti kinnitust. Ente Auth annab teile ka 24-sõnalise taastamisvõtme (mis põhineb BIP39 meetodil). **See võti** tuleb kindlasti turvalisse kohta salvestada: see on teie ainus vahend andmete taastamiseks, kui te unustate oma parooli.



### Kohalik turvalisus



Soovitan tungivalt võimaldada kohalikku kaitset koodiga või biomeetria abil. Mine **Settings → Security → Lockscreen** ja konfigureeri :





- **Biomeetriline avamine**: Face ID, sõrmejälg sõltuvalt seadme võimalustest
- Rakendusspetsiifiline PIN-kood/parool
- **Autolukustuse viivitus**: nt "Kohe" või pärast 30 sekundit tegevusetust



See kaitse takistab volitamata juurdepääsu teie koodidele, kui keegi pääseb teie lukustamata telefonile ligi. Pange tähele, et see lukk on täiendav takistus: teie andmed jäävad lõpuni krüpteerituks ka ilma selle kaitseta.



## 2FA kontode lisamine



### Tavapärane menetlus



Uue 2FA-konto lisamiseks võtame konkreetse näite 2FA aktiveerimisest Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Ente Authi peamine Interface valmis esimese 2FA* konto lisamiseks



**Servicepool (Bull Bitcoin)**: Logige sisse oma Bull Bitcoin kontole, minge turvasätetele ja lubage kahefaktoriline autentimine.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* turvasätete menüü



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Kahefaktorilise autentimise lubamise võimalus Bull Bitcoin* puhul



Teenus kuvab seejärel QR-koodi, mida saate skannida oma autentimisrakendusega:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Bull Bitcoin poolt genereeritud QR-kood, mida saab skaneerida autentimisseadmega*



**In Ente Auth**: Klõpsake "Sisestage seadistamisvõti", seejärel skannige QR-koodi, mida kuvab Bull Bitcoin. Ente Auth tunneb konto automaatselt ära ja täidab väljad.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Bull Bitcoin konto üksikasjade seadistamine Ente Auth*s



Saate kohandada teenuse nime ja oma kasutajanime, et seda oleks lihtsam leida. Täiustatud seaded (SHA1 algoritm, 30s periood, 6 numbrit) on üldiselt vaikimisi õiged.



**teeninduspoolne valideerimine**: Pöörduge tagasi Bull Bitcoin juurde ja sisestage Ente Auth poolt genereeritud 6-kohaline kood, et aktiveerimine lõpule viia.



![Saisie du code 2FA](assets/fr/09.webp)



*Sisestage Ente Auth poolt loodud kood, et kinnitada 2FA* aktiveerimine



![2FA activée](assets/fr/10.webp)



*Kinnitus 2FA eduka aktiveerimise kohta Bull Bitcoin* puhul



**Tagavarakoodid**: Bull Bitcoin annab teile taastamiskoodid. **Salvestage need turvalisse kohta, autentimisseadmest eraldi.**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Võimalus kasutada generate hädaolukorra varukoode pulli Bitcoin puhul*



![Codes de récupération](assets/fr/12.webp)



*Taastamiskoodide nimekiri, mida hoida turvalises kohas*



### Organisatsioon ja juhtimine



Ente Auth pakub mitmeid praktilisi funktsioone:



**Pikakoopia**: Vajutage koodi, et kopeerida see automaatselt lõikelauale.



**Kontekstitundlikud tegevused**: Vajutage ja hoidke all (või tehke töölaual paremklõps), et kirjet muuta, kustutada, jagada või kinnitada.



**Tagid ja otsing**: Korraldage oma kontod siltide abil (isiklik/professionaalne, teenusekategooria järgi) ja kasutage otsinguriba kiireks filtreerimiseks.



![Création d'un tag](assets/fr/17.webp)



*Sildi loomise protsess: kontekstmenüü ja loomise dialoog*



![Tag appliqué](assets/fr/18.webp)



*Silt "Bitcoin" edukalt rakendatud Bull Bitcoin* kontole



**Automaatilised ikoonid**: Tänu [Simple Icons] ikoonipaketi (https://simpleicons.org/) integreerimisele saab iga kirjet illustreerida teenuse logoga.



**Ajutine turvaline jagamine**: Turvaline jagamine on ainulaadne Ente Auth funktsioon, mis võimaldab teil edastada 2FA-koodi kolleegile ilma selle aluseks olevat saladust avaldamata. generate krüpteeritud link, mis kehtib maksimaalselt 2, 5 või 10 minutit - saaja näeb koodi reaalajas, kuid ei saa seda eksportida ega juurdepääsu kontoandmetele. See meetod on ideaalne tehnilise abi või ajutise koostöö jaoks, pakkudes turvalisuse taset, mida lihtsa ekraanipildi või tekstisõnumi abil ei ole võimalik saavutada.



![Partage sécurisé](assets/fr/19.webp)



*Interface ajutine turvaline jagamine: valige kestus (5 min)*



**Turvaline eksport/import**: Ente Auth võimaldab teil eksportida oma koode teistesse rakendustesse või importida neid Google Authenticatorist ja teistest lahendustest. Eksport toimub krüpteeritud faili või QR-koodi kaudu, mis tagab teie andmete teisaldatavuse ilma turvalisust ohustamata.



**BIP39 taastamise võti**: Rakendus genereerib automaatselt 24-sõnalise taastumisfraasi vastavalt BIP39 (Bitcoin Improvement Proposal) standardile, mis on identne krüptoraha rahakottidega. See fraas on teie lõplik taastamisvõti, mis võimaldab teil taastada kõik oma koodid isegi siis, kui te unustate oma põhiparooli.



## Konfigureerimine ja seaded



Ente Auth pakub arvukaid kohandamisvõimalusi, mis on kättesaadavad rakenduse seadete kaudu:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Ülevaade Ente Auth*s saadaval olevatest parameetritest



### Konto ja andmete haldamine



![Paramètres de sécurité](assets/fr/14.webp)



*Täiustatud turvavalikud: e-posti kinnitamine, PIN-kood, aktiivsed seansid*



Turvasätted võimaldavad teil :




- Võimaldage uute ühenduste jaoks e-posti kinnitamine
- Aktiveeri passkey
- Vaadake aktiivseid seansse oma erinevates seadmetes
- PIN-koodi või biomeetria seadistamine



### Interface ja kasutusvõimalused



![Paramètres généraux](assets/fr/15.webp)



*Interface parameetrid ja rakenduse kohandamine*



Üldised seaded hõlmavad :




- **Keel**: Interface mitmekeelne
- **Näita**: Suured ikoonid, kompaktne režiim
- **Privaatsus**: Peida koodid, kiire otsing
- **Telemetria**: Veateade (saab välja lülitada)



## Varundamine ja sünkroniseerimine



### Kuidas krüpteerimine toimib



Kui lisate konto ühendatud Ente-kontoga, krüpteerib rakendus need tundlikud andmed koheselt lokaalselt, kasutades teie (paroolist tuletatud) üldvõtit. Seejärel saadetakse krüpteeritud andmed salvestamiseks Ente serverisse.



Tänu sellele mehhanismile on teie koodide lõpuni krüpteeritud pilvevarukoopia alati kättesaadav. Kui kaotate oma seadme, installige lihtsalt Ente Auth uuesti ja ühendage see uuesti: rakendus laeb automaatselt alla ja dekrüpteerib kõik teie koodid.



### Mitme seadme sünkroniseerimine



Kui kasutate Ente Auth'i nii nutitelefonis kui ka arvutis, ilmuvad kõik täiendused või muudatused ühes seadmes sekundite jooksul ka teises seadmes. See sünkroniseerimine käib läbi Ente pilve, kuid kuna andmed on otsast lõpuni krüpteeritud, näeb server ainult loetamatut krüpteeritud sisu.



![Synchronisation mobile](assets/fr/16.webp)



*Sünkroniseerimise demo: sama Bull Bitcoin konto, mis on kättesaadav nii mobiilis kui ka töölaual*



Sünkroniseerimine on sujuv: installige Ente Auth oma nutitelefonile, logige sisse oma volitustega ja kõik teie 2FA-koodid (siin Bull Bitcoin) ilmuvad automaatselt. Ülaltoodud näide näitab täiuslikku sünkroniseerimist töölaua- ja mobiiltelefoni vahel - sama Bull Bitcoin kood on mõlemas seadmes kättesaadav.



Mis puutub konfidentsiaalsusesse, siis ei Ente ega ükski kolmas isik ei pääse ligi teie 2FA-saladustele. Isegi metaandmed (sildid, märkmed, teenuste nimed) krüpteeritakse enne saatmist. See nullteabe arhitektuur tagab, et ainult teie saate oma koode dešifreerida.



### Kasutamine võrguühenduseta



Sünkroonimine eeldab internetiühendust, kuid Ente Auth töötab igas seadmes täiesti offline, sest kõik andmed on salvestatud lokaalselt. Offline-muudatused pannakse järjekorda ja sünkroniseeritakse kohe, kui ühendus taastub.



## Turvalisus ja privaatsus



### Krüptograafilised tagatised



Ente Auth põhineb tugeval otsast-otsani krüpteerimisel, mille arhitektuur on null-teadmistega. Teie koodid on krüpteeritud ainult teie käes oleva võtmega, mis on tuletatud teie peaparoolist, kasutades täiustatud võtme tuletamise funktsioone.



**Nulltunnetuse arhitektuur:** Ente ei pääse füüsiliselt ligi teie andmetele. Isegi metaandmed (teenuste nimed, sildid, märkused) krüpteeritakse kliendi poolel enne edastamist. See lähenemisviis tagab, et teie serveritele suunatud rünnaku või valitsuse nõudmise korral saab Ente avaldada ainult krüpteeritud andmeid, mida ei saa lugeda ilma teie paroolita.



**Lokaalne krüpteerimine**: Krüpteerimine toimub täielikult teie seadmes, enne kui see saadetakse pilve. Ente serverid võtavad vastu ja salvestavad ainult krüpteeritud andmeid, mis muudab volitamata juurdepääsu võimatuks isegi teenuse administraatorite jaoks.



### Läbipaistvus ja auditid



Kuna kood on [avatud lähtekoodiga](https://github.com/ente-io/auth), saab kogukond kontrollida tagauste puudumist. Ente on teostanud [mitu välisauditit](https://ente.io/blog/cryptography-audit/), et kinnitada selle rakendamise turvalisust:





- **Cure53** (Saksamaa): Rakenduse ja krüptograafilise turvalisuse audit
- **Symbolic Software** (Prantsusmaa): Spetsiaalsed krüptograafilised teadmised
- **Fallible** (India): Penetratsioonitestimine ja haavatavuse analüüs



Need tunnustatud firmade poolt läbiviidud sõltumatud auditid tagavad, et Ente Auth'i krüptograafiline rakendamine vastab parimatele turvatavadele ja et selles ei ole kriitilisi puudusi.



### Privaatsuspoliitika



Ente Auth kohaldab [eeskujulikku privaatsuspoliitikat](https://ente.io/privacy/), mis põhineb minimaalsel andmekogumisel. Säilitatakse ainult teenuse toimimiseks hädavajalikku teavet: teie e-posti aadress Address autentimiseks ja konto taastamiseks.



**Ei jälgimist ega telemeetriat**: Erinevalt enamikust rakendustest ei kogu Ente Auth kasutusmõõdikuid, ei tuvasta kokkupõrkeandmeid ega käitumisandmeid. Rakendus töötab ilma pealetükkiva reklaami või analüütiliste jälgimisseadmeteta.



**GDPR vastavus**: Ente täidab täielikult Euroopa isikuandmete kaitse üldmäärust. Teil on õigus oma andmetega igal ajal tutvuda, neid parandada või kustutada. Andmete eksport](https://ente.io/take-control/) on vaid ühe klõpsu kaugusel ja teie konto lõplik kustutamine kustutab kõik teie andmed serveritest.



**Detsentraliseeritud, turvaline ladustamine**: Teie krüpteeritud andmed on replitseeritud 3 erinevas riigis asuvale 3 teenusepakkujale, mis tagab optimaalse kättesaadavuse, vältides samal ajal sõltuvust ühest pilveteenuse pakkujast.



Ente ärimudel põhineb tasulisel Ente Photos teenusel, mis võimaldab meil pakkuda Ente Auth ** tasuta ja piiranguteta**, ilma et teie andmete rahaks muutmise kaudu kahjustataks teie privaatsust. Selline lähenemisviis tagab teenuse jätkusuutlikkuse, ilma et see tugineks reklaamile või isikuandmete edasimüügile.



## Võrdlus teiste lahendustega



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth paistab silma kui üks väheseid lahendusi, mis ühendab endas kõik eelised: lähtekoodi läbipaistvus, krüpteeritud pilves varundamine ja platvormideülene sünkroniseerimine.



## Soovituslikud kasutusjuhud



### Individuaalsed kasutajad



Ente Auth on ideaalne turvatundlikele inimestele, kes süstemaatiliselt aktiveerivad 2FA. Te ei pea enam muretsema, et kaotate oma koodid telefoni vahetamisel või peate valima mugavuse ja turvalisuse vahel.



### Perekonna ja mitme seadme kasutamine



Rakendus saab oma osa, kui kasutate mitut seadet. Saate salvestada oma koodid nutitelefonidesse ja tahvelarvutitesse või jagada teatud perekondlikke koode (Netflix, perepilv) sünkroonselt ja turvaliselt.



### Professionaalne kasutamine



Tundlikke kontosid haldavate meeskondade jaoks hõlbustab Ente Auth koostööd, säilitades samal ajal turvalisuse, tänu oma täiustatud jagamisfunktsioonidele, mis on integreeritud jaotisse "Organisatsioon ja haldamine".



## Parimad tavad





- **Salvestage oma hädaolukorra koodid**: Hoidke iga teenuse pakutavad taastamiskoodid telefonist eemal.





- **Kasutage tugevat põhiparooli**: Teie Ente Auth peaparool peab olema unikaalne ja tugev, sest see kaitseb kõiki teie koode.





- **Aktiveerige kohalik kaitse**: Konfigureerige PIN-kood või biomeetria, et vältida volitamata füüsilist juurdepääsu.





- **Ärge kohandage liiga palju**: Vältige täiustatud muudatusi, mis võivad ohustada sünkroniseerimist.





- **Hoidke taotlus ajakohasena**: Uuendused parandavad turvaauke ja parandavad funktsionaalsust.





- **Katse taastamine**: Kontrollige aeg-ajalt, kas saate oma koodid taastada mõnes teises seadmes.



## Kokkuvõte



Ente Auth on kaasaegne ja terviklik lahendus kahefaktorilise autentimise jaoks. Kombineerides turvalisuse, läbipaistvuse ja kasutusmugavuse, vastab see avatud lähtekoodiga rakendus nõudlike kasutajate vajadustele, ilma et see ohverdaks mugavust.



Erinevalt patenteeritud lahendustest, mis lukustavad teid läbipaistmatusse ökosüsteemi, annab Ente Auth teile tagasi kontrolli oma autentimisandmete üle, kaitstes teid samal ajal juhusliku kadumise eest tänu krüpteeritud varukoopiatele.



Olenemata sellest, kas olete üksikisik, kes soovib kaitsta oma isiklikke kontosid, või meeskond, kes haldab ettevõtte juurdepääsu, on Ente Auth arukas valik, et ajakohastada oma lähenemist digitaalsele turvalisusele, ilma privaatsust ohustamata.



## Ressursid ja toetus



### Ametlikud dokumendid




- **Ametlik veebileht**: [ente.io/auth](https://ente.io/auth)
- **Abikeskus**: [help.ente.io/auth](https://help.ente.io/auth)
- **Tehniline blogi**: [ente.io/blog](https://ente.io/blog)



### Lähtekood ja läbipaistvus




- **GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- **Krüptograafia audit**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Ühendus




- **Arutelu**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**: [r/enteio](https://reddit.com/r/enteio)