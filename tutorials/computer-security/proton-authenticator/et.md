---
name: Proton Authenticator
description: Kuidas ma saan kasutada Proton Authenticatorit oma kontode kaitsmiseks 2FAga?
---
![cover](assets/cover.webp)



Kahefaktoriline autentimine (2FA) lisab teie kontodele täiendava turvatõkke, nõudes lisaks paroolile täiendavat tõendit, et ainult teil on see olemas. 2FA aktiveerimine vähendab oluliselt häkkimisriski, isegi kui teie parool on ohustatud andmepüügi või andmete lekke tõttu. Ilma 2FA-ta oleks ründajale kontodele juurdepääsuks vaja ainult teie parooli; 2FA-ga on vaja ka teist tegurit, mis nurjab enamiku kontovarguskatseid.



On olemas erinevaid 2FA tüüpe. SMS-koodid on paremad kui mitte midagi, kuid need on endiselt haavatavad SIM-koodi vahetamise ja pealtkuulamise rünnakute suhtes. Me ei soovita SMS-i kui esmast 2FA-d. Autentimisrakendused (TOTP) generate ajutised koodid lokaalselt teie seadmes, mistõttu on neid palju raskem pealtkuulata. Füüsilised turvavõtmed pakuvad parimat turvalisust, kuid nõuavad spetsiaalset riistvara.



Proton Authenticator on TOTP-autentifikaator. See on Protoni vastus olemasolevate rakenduste piirangutele: paljud neist on patenteeritud, sisaldavad reklaami jälgimisseadmeid ja ei paku krüpteeritud varundust. Proton Authenticator eristub sellest, pakkudes avatud lähtekoodiga rakendust, mis ei sisalda reklaame ega jälgimisseadmeid ning millel on läbivalt krüpteeritud varundamine.



## Proton Authenticator'i tutvustamine



Proton Authenticator on privaatsusele suunatud teenuste poolest tuntud Protoni poolt välja töötatud mobiil- ja töölaua TOTP-autentimisrakendus. Nagu kõik Protoni tooted, on ka see rakendus avatud lähtekoodiga ja läbinud sõltumatu turvaauditi. See on tasuta saadaval kõigil platvormidel (Android, iOS, Windows, macOS, Linux).



Proton Authenticator pakub järgmisi põhifunktsioone:





- **TOTP-koodide** genereerimine teie 2FA-kontode jaoks, mis ühildub enamiku saitidega, mis kasutavad Google Authenticatorit, Authy-d jne.





- **Valikuline krüpteeritud pilves varundamine**: saate rakenduse siduda oma Proton-kontoga, et varundada ja sünkroniseerida oma koode otsast lõpuni krüpteeritult. Kui kaotate oma seadme, ühendage lihtsalt uus seade, et taastada kõik oma koodid.





- **Mitme seadme sünkroniseerimine**: kui logite rakenduses Protonisse sisse, sünkroonitakse teie 2FA-koodid automaatselt mitme seadme vahel otsast lõpuni krüpteerimise abil. IOS-i puhul on alternatiiviks sünkroniseerimine iCloudi kaudu.





- **Kohalik lukustamine parooli või biomeetria abil**: rakendus pakub PIN-koodi ja/või sõrmejälje/näotuvastuse lukustamist. Seega isegi kui keegi pääseb füüsiliselt teie lukustamata telefonile ligi, ei saa ta Proton Authenticatorit avada.





- **Andmete kogumine ja jälgimisseadmed puuduvad**: Proton on võtnud endale kohustuse mitte koguda rakenduse kaudu isikuandmeid. Ei ole varjatud reklaami ega käitumisanalüüsi.





- **Lihtne import/eksport**: üks Proton Authenticatori tugevatest külgedest on olemasolevate kontode importimise viisard, mis ühildub teiste rakendustega (Google Authenticator, Authy, Aegis jne). Vajadusel saate oma koodid ka faili eksportida.



Lühidalt öeldes on Proton Authenticatori eesmärk olla kompromissitu 2FA lahendus: turvaline, privaatne ja paindlik.



## Paigaldamine



Proton Authenticator on saadaval tasuta kõigil platvormidel. Rakenduse allalaadimiseks minge ametlikule lehele: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Proton Authenticatori ametlik lehekülg, mis näitab rakenduse põhifunktsioone ja Interface*



Sellel leheküljel leiate allalaadimislingid kõigi operatsioonisüsteemide jaoks: Android, iOS, Windows, macOS ja Linux. Lihtsalt klõpsake valitud operatsioonisüsteemil ja järgige standardseid paigaldusetappe.



Selles õpetuses näitame teile, kuidas seda macOS-i paigaldada ja seadistada ning seejärel vaatame, kuidas paigaldada rakendus iOS-i ja sünkroonida oma koodid kahe seadme vahel.



### Paigaldamine macOS-i



Kui olete rakenduse alla laadinud ja paigaldanud, käivitage Proton Authenticator. Esimesel käivitamisel juhatab rakendus teid läbi mõne esialgse seadistusekraani:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Proton Authenticatori tervitusekraan koos sõnumi "Turvalisus igas koodis" ja nupuga "Alusta "*



### Esialgne import



Kui Proton Authenticator tuvastab, et olete varem kasutanud mõnda muud 2FA-rakendust, võib ilmuda importimisviisard. See toetab otsest importi teatavatest rakendustest (Google Authenticator, 2FAS, Authy, Aegis jne). Te võite selle sammu ka vahele jätta ja lisada oma kontod hiljem käsitsi.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Impordivõti koodide ülekandmiseks teistest autentimisrakendustest*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Ühilduvad impordirakendused: authy, Bitwarden Authenticator, Ente Auth ja Google Authenticator*



### Kohaliku rakenduse kaitse



Määrake avamise PIN-kood või lubage biomeetriline avamine (Touch ID), kui see on saadaval. See samm on oluline, et keegi, kes kasutab teie Mac'i, ei saaks tasuta juurdepääsu teie 2FA-koodidele.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Touch ID seadistusekraan koos sõnumi "Kaitske oma andmeid" ja nupuga "Aktiveeri Touch ID "*



### Sünkroniseerimise valikud



Rakendus võimaldab teil aktiveerida ka iCloudi sünkroniseerimise, et varundada oma andmeid turvaliselt oma Apple'i seadmete vahel.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*ICloudi sünkroonimisvõimalus sõnumiga "Varundage oma andmeid turvaliselt krüpteeritud iCloudi sünkroonimisega "*



Kui need sammud on lõpetatud, on Proton Authenticator kasutusvalmis.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface peamine tühi Proton Authenticator koos valikutega "Loo uus kood" ja "Impordi koodid "*



## 2FA konto lisamine ProtonMailiga



Vaatame nüüd, kuidas lisada oma esimene 2FA-kood, kasutades ProtonMaili näitel. See meetod töötab samamoodi kõigi kahefaktorilist autentimist toetavate teenuste puhul.



### 2FA aktiveerimine ProtonMailis



Kõigepealt saate lisateavet meie ProtonMaili juhendi kohta:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Logige sisse oma ProtonMaili kontole ja minge turvasätete juurde. Otsige valik "Kahefaktoriline autentimine" ja aktiveerige see.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMaili seadete lehekülg, kus on valik "Authenticator app" jaotises "Two-factor authentication "*



Vajutage nupule autentimaatori aktiveerimiseks ja ProtonMail palub teil valida autentimisrakendus.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMail 2FA konfiguratsiooniaken koos nuppudega "Cancel" ja "Next "*



ProtonMail kuvab seejärel QR-koodi, mida saate skannida oma autentimisrakendusega.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMaili QR-kood, mida saate skannida oma autentimisrakendusega, kusjuures saadaval on valik "Sisesta võti käsitsi "*



Kui soovite võtme käsitsi sisestada, klõpsake salajase võtme kuvamiseks nuppu "Sisestage võti hoopis käsitsi".



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*2FA teabe käsitsi sisestamine: Võti, intervall (30) ja numbrid (6)*



### Skaneeri QR-kood Proton Authenticatoriga



MacOS-i Proton Authenticatoris klõpsake nuppu "Loo uus kood". Rakendus pakub teile mitmeid võimalusi: **Skaneeri QR-kood** või **Ettesta võti käsitsi**.



Kasutage oma Maci kaamerat, et skannida ProtonMaili ekraanil kuvatavat QR-koodi. Kui olete QR-koodi skaneerinud, jõuate uue koodi konfigureerimise ekraanile.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Uue kirje loomise aken pealkirja (ProtonMail), saladuse, saatja (Proton), numbriliste parameetrite ja intervalli väljadega*



Proton Authenticator täidab andmed automaatselt. Soovi korral saate nime kohandada, seejärel klõpsake nuppu "Salvesta".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*ProtonMaili jaoks loodud TOTP-kood (848 812) koos järelejäänud aja kuvamisega*



### Kinnitage konfiguratsioon



ProtonMail palub teil sisestada 6-kohaline kood, mille on genereerinud Proton Authenticator, et kinnitada 2FA nõuetekohast toimimist.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*ProtonMaili valideerimisekraan, kus palutakse sisestada 6-kohaline kood (848812)*



Kopeerige kood rakendusest (klõpsates sellel) ja kleepige see ProtonMaili, et aktiveerimine lõpule viia.



Pärast kinnitamist palub ProtonMail teil laadida alla oma taastamiskoodid. Oluline on need hoolikalt salvestada.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMaili taastamiskoodide ekraan koos päästekoodide loeteluga ja nupuga "Download "*



### Hädaolukorra koodid



Konto lisamisel hoidke teenuse pakutavaid taastamiskoode. Enamik saite pakub staatilisi, ühekordselt kasutatavaid taastamiskoode, mida saab hoida turvalises kohas. Hoidke neid varukoode väljaspool Proton Authenticatorit, et saaksite oma kontole juurde pääseda, kui kaotate juurdepääsu 2FA-rakendusele.



## IOS-i paigaldamine ja koodi importimine



Nüüd, kui olete Proton Authenticator'i seadistanud macOSis, võite seda kasutada ka iPhone'is või iPadis. Siin on, kuidas saada oma 2FA-koodid mitmesse seadmesse.



### Rakenduse allalaadimine iOS-is



Mine App Store'i ja otsi "Proton Authenticator". Laadige rakendus alla ja installige see oma iOS-seadmesse.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Installeerimisprotsess iOS-i puhul: tervitusekraan, importimisviisard, ühilduvate rakenduste valik ja lõplik ekraan "Impordi koodid Proton Authenticatorist "*



### Meetod 1: Eksport/import JSON-faili kaudu



Kui te ei kasuta automaatset sünkroonimist (iCloud või Proton konto), peate oma koodid käsitsi Macilt iPhone'ile üle kandma:



**Samm 1 - Ekspordi macOS-st** :



Avage Macil Proton Authenticator ja minge seadistustesse (hammasratta ikoon). Klõpsake menüüs "Export".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Proton Authenticatori seadete menüü macOS-i puhul, kus valik "Export" on nähtav*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Ekspordi aken failinimega "Proton_Autenticator_backup_2025" ja nupp "Salvesta "*



Salvestage JSON-faili Macis. Saate selle saata turvalise e-kirjaga või salvestada selle iCloud Drive'i, et pääseda sellele ligi iPhone'ist.



**Samm 2 - importimine iOS-i** :



Installige oma iPhone'ile Proton Authenticator ja valige seadistamise ajal koodide importimine. Valige nimekirjast "Proton Authenticator" ja importige JSON-faili.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Impordiprotsess iOS-is: JSON-faili lokaliseerimine, impordi kinnitamine ja seadistusekraanid koos Face ID ja iCloudi valikutega*



### Meetod 2: Automaatne sünkroniseerimine



**Proton konto kaudu (mitme platvormi sünkroniseerimiseks)** :



Kui te ei ole veel Proton-kontot sisse seadnud ja soovite sünkroonida erinevate operatsioonisüsteemide vahel, palub rakendus teil luua või ühendada Proton-konto.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Seadme sünkroonimisekraan, kus palutakse luua tasuta Proton konto või ühendada olemasolevaga*



**ICloudi kaudu (ainult Apple'i ökosüsteemi jaoks)** :


Kui kasutate ainult Apple'i seadmeid, saate rakenduse seadetes valida iCloudi sünkroniseerimise. See meetod sünkroonib teie koodid automaatselt ja turvaliselt kõigi teie Apple'i seadmete vahel, ilma et oleks vaja Proton'i kontot.



## Krüpteeritud varundamine ja taastamine



Üks Proton Authenticatori peamisi funktsioone on 2FA-koodide läbiv varundamine, mis tagab, et seadme kaotamise või vahetamise korral ei pea uuesti alustama.



### Lõppkrüpteerimine



Proton Authenticatoriga krüpteeritud pilves varundamise puhul krüpteeritakse teie TOTP-saladused enne nende saatmist Protoni serverisse lokaalselt teie seadmes. Dekrüpteerimine on võimalik ainult teie poolt, teie seadmetes, mis on ühendatud teie Protoni kontoga. Proton AG-l ei ole teie registreeritud koodide lugemise võtit.



Kui valite iOS-i puhul Proton-konto asemel iCloudi, on teie andmed krüpteeritud vastavalt Apple'i standarditele. Androidi kohalik varundamine võimaldab teil varundusfaili krüpteerida teie valitud parooliga.



### Kaotuse korral taastamine



Kui teie telefon on kadunud, varastatud või te vahetate mobiiltelefoni:



**Kui Proton varundamine on lubatud**: Paigaldage Proton Authenticator uude seadmesse. Esialgse seadistamise ajal logige sisse samasse Proton-kontole. Rakendus sünkroonib ja laeb kohe kõik teie 2FA-koodid krüpteeritud varukoopiast alla.



**ICloudi varundamisega (iOS)**: Ühendage uus iPhone/iPad sama Apple ID-ga ja veenduge, et aktiveerite iCloudi võtmehoidja. Pärast Proton Authenticatori installimist ühendage iCloudiga. Teie koodid peaksid iCloudi kaudu sünkroonima ja ilmuma.



**Ei pilvevarundust**: Te peate oma kontod käsitsi importima. Kui olete eksportinud varukoopiafaili, kasutage Proton Authenticatori funktsiooni Import. Halvimal juhul, kui teil ei olnud varukoopiat, peate kasutama iga teenuse varukoopiakoode või võtma ühendust klienditoega.



Proton Authenticator võimaldab teil igal ajal eksportida oma kontosid kas krüpteeritud failina või mitme konto QR-koodina. Need võimalused annavad teile lisakindlust.



## Parimad tavad



2FA-autentifikaatori kasutamine suurendab oluliselt teie turvalisust, kuid tuleb järgida teatavaid parimaid tavasid:



### Salvesta oma hädaolukorra koodid



Kui te aktiveerite 2FA teenuse puhul, antakse teile sageli taastamiskoodide nimekiri. Hoidke neid telefonist eemal (paberil, krüpteeritud paroolihalduris jne). Autentimisseadme täieliku kadumise korral päästavad need staatilised koodid teid.



### Ärge segage oma paroole ja 2FA-koode kokku



On ahvatlev kasutada paroolihaldurit, mis salvestab ka TOTPi. Parooli ja 2FA-koodi hoidmine samas kohas loob aga ühe veapunkti ja nõrgestab topeltautentimist. Maksimaalse turvalisuse tagamiseks soovitavad paljud eksperdid eraldada kaks tegurit: paroolid turvalises halduris ja 2FA-koodid eraldi rakenduses, näiteks Proton Authenticatoris. Integreeritud halduri kasutamine on siiski parem kui 2FA puudumine.



### Aktiveerige mitu 2FA meetodit



Ideaalis kasutage oma kriitiliste kontode puhul rohkem kui ühte teist tegurit. Ärge kõhkle lisamast füüsilist turvavõti, kui teenus seda võimaldab. Lisateavet leiate meie juhendmaterjalist Yubikey füüsiliste võtmete kohta:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Samuti hoidke käepärast trükitud hädaolukorra koodid.



### Jääge diskreetseks ja kaitske oma seadet



Ärge laske kellelgi oma lukustamata telefoni otsida. Proton Authenticatoriga on teie koodid kaitstud PIN/biomeetria abil - ärge avaldage seda PIN-koodi. Samuti olge ettevaatlik andmepüügi suhtes: isegi 2FA puhul võib ründaja kasutada koodi, kui annate selle reaalajas petturile.



### Uuendused ja auditid



Hoidke Proton Authenticator ajakohasena (uuendused parandavad võimalikke vigu). Kuna kood on avatud, viib kogukond läbi mitteametlikke auditeid ja Proton avaldab ametlike auditite tulemused.



## Võrdlus teiste rakendustega



Kuidas on Proton Authenticator võrreldav teiste autentimisrakendustega? Siin on võrdlev kokkuvõte:



**Prooton Authenticator**: Avatud lähtekoodiga, valikuline E2EE krüpteeritud pilves varundamine, sünkroniseerimine mitme seadmega, kohalik lukustamine, jälgimine puudub, saadaval mobiilis ja lauaarvutis.



**Google Authenticator**: 2023. aastal lisatud mitme seadme sünkroniseerimine, vaikimisi ei ole rakenduste lukustamist, sisaldab Google'i jälgimisseadmeid, varundamine Google'i konto kaudu alates 2023. aastast.



**Aegis Authenticator**: Avatud lähtekoodiga, ainult kohalik varundamine, pilves sünkroniseerimine puudub, kood/biomeetriline lukk, jälgimine puudub, ainult Android.



**Authy**: Omandiõiguslik, parooliga krüpteeritud pilvevarundus, kuid suletud kood, sünkroniseerimine mitme seadmega, PIN-lukk/ sõrmejälg, kogub telefoninumbri, töölaua rakendus lõpetatakse märtsis 2024.



Allpool leiate meie juhendi Authy kohta:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator on üks terviklikumaid ja turvalisemaid lahendusi: avatud lähtekood, krüpteeritud sünkroniseerimine mitme seadme vahel, ei mingeid kommertslike järelmeetmeid.



## Ressursid ja toetus



### Ametlikud dokumendid




- **Ametlik veebileht**: [proton.me/authenticator](https://proton.me/authenticator) - Toote esitlus ja allalaadimine
- **Allalaadimisleht**: [proton.me/en/autenticator/download](https://proton.me/fr/authenticator/download) - Lingid kõikidele operatsioonisüsteemidele
- **Prootonite toetus**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Ametlik 2FA aktiveerimisjuhend
- **Proton blogi**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Teadaanne ja üksikasjalikud funktsioonid



### Lähtekood ja läbipaistvus




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Avatud lähtekood
- **Turvaauditid**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Sõltumatud auditiaruanded



### Soovitatavad ohutuskatsed


Pärast konfigureerimist testige oma seadistust:




- [Have I Been Pwned](https://haveibeenpwned.com/) - kontrollige, kas teie kontod on kompromiteeritud
- [2FA Directory](https://2fa.directory/) - 2FA-d toetavate teenuste loetelu



### Kogukonnad ja arutelud




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Protoni ametlik kogukond
- **Privaatsusjuhiste foorum**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Tehnilised arutelud eraelu puutumatuse küsimustes
- **Reddit r/privaatsus**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Üldised nõuanded privaatsuse kohta



### Muud




- [Have I Been Pwned](https://haveibeenpwned.com/) - kontrollige, kas teie kontod on kompromiteeritud
- [2FA Directory](https://2fa.directory/) - 2FA-d toetavate teenuste loetelu