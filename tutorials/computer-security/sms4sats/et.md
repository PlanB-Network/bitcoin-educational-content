---
name: SMS4Sats
description: Saate ja saadate SMS-i anonüümselt, makstes Bitcoin Lightning'is
---

![cover](assets/cover.webp)



SMS-kinnitus on muutunud paljude veebiteenuste jaoks kohustuslikuks. Ükskõik, kas tegemist on konto loomisega platvormil, registreerimise kinnitamisega või identiteedi kinnitamisega, veebilehed nõuavad peaaegu süstemaatiliselt telefoninumbrit. See laialt levinud tava tekitab suure probleemi kõigile, kes soovivad säilitada oma eraelu puutumatust: teie isiklik number muutub alaliseks tunnuseks, mis seob teie erinevad digitaalsed tegevused teie tegeliku identiteediga ja avab ukse soovimatutele kommertspäringutele.



**SMS4Sats** vastab sellele probleemile, pakkudes ajutisi telefoninumbreid SMS-sõnumite vastuvõtmiseks ja saatmiseks. Teenus paistab silma registreerimisvaba mudeli ja Lightning Network kaudu toimuva eksklusiivse Bitcoin maksmise poolest. Mõne satši eest saate ühekordse numbri, mis võimaldab teil registreerimist kinnitada ilma oma isiklikku numbrit avaldamata.



See õpetus juhatab teid läbi kolme SMS4Satsi funktsiooni: kinnitussõnumi vastuvõtmine, anonüümse SMSi saatmine ja ajutise numbri rentimine mitmeks tunniks.



## Mis on SMS4Sats?



SMS4Sats on võrguteenus, mis on kättesaadav aadressil [sms4sats.com](https://sms4sats.com), võimaldades anonüümset SMS-ide haldamist Bitcoin Lightning'i makse kaudu. Teenus pakub kolme erinevat funktsiooni: ühekordsete kinnituskoodide vastuvõtmine, SMSide saatmine mis tahes numbrile ja ajutiste numbrite rentimine mitmeks tunniks.



### Filosoofia ja tegevusmudel



Projekti eesmärk on tagada maksimaalne konfidentsiaalsus ja finantssõltumatus. Kuna SMS4Sats ei nõua konto loomist ja võtab vastu ainult Bitcoin Lightning makseid, siis ei ole vaja isikuandmeid esitada. Ei mingit e-posti aadressi, ei mingit krediitkaarti, ei mingit isiklikku teavet ei nõuta. Teenustele juurdepääsuks on vaja ainult Lightning-makseid.



Teenus toetab üle 400 saidi ja rakenduse umbes 120 riigis, mis katab enamiku tavalistest kontrollivajadustest. Selline ulatuslik geograafiline katvus võimaldab registreeringute valideerimist mitmesugustel platvormidel, alates sotsiaalvõrgustikest kuni sõnumiteenusteni.



### Tingimuslik maksemudel



SMS4Sats kasutab SMS-vastuvõtufunktsiooni jaoks tingimuslikke välkarveid (hodl-arveid). See mehhanism tagab, et teilt võetakse tasu ainult siis, kui SMS on tegelikult vastu võetud. Kui sõnumit ei saabu ettenähtud aja jooksul (maksimaalselt 20 minutit), tühistatakse makse automaatselt ja satoshis tagastatakse teie wallet-le. See garantii ei kehti saatmis- ja rendifunktsioonide kohta, mida ei tagastata.



## Kolm SMS4Satsi omadust



SMS4Satsi kasutajaliides on korraldatud kolme vahekaardi ümber, mis vastavad kolmele erinevale kasutusviisile: **RECEIVE** kinnituskoodide vastuvõtmiseks, **SEND** anonüümse SMS-i saatmiseks ja **RENT** ajutise numbri rentimiseks.



### SMS-i vastuvõtmine



Peamine funktsioon võimaldab teil saada ajutise numbri, et saada unikaalne kinnituskood. Kui kood on saadud ja kasutatud, on number jäädavalt deaktiveeritud.



### Saada SMS



See funktsioon võimaldab teil saata SMS-i mis tahes telefoninumbrile ilma oma identiteeti avaldamata. Vastuvõtja saab sõnumi anonüümselt numbrilt.



### Rentida aktus



Kasutajatele, kellel on vaja saada mitu SMS-sõnumit ühele numbrile, pakub SMS4Sats ajutist rendivõimalust. See võimalus võimaldab teil rendiperioodi jooksul vastu võtta ja saata mitu sõnumit.



**Hinnamärkus** : Käesolevas õpetuses näidatud hinnad on soovituslikud. Need varieeruvad vastavalt numbri riigile, sihtteenusele ja hetkenõudlusele. Näiteks SMS Prantsusmaale Telegram võib sõltuvalt tingimustest maksta 1500-5000 satšit. Kontrollige alati enne maksmist välkarvete täpset summat.



## Saate kontrollsõnumi



Vaatame üksikasjalikult, kuidas kasutada SMS4Satsi kinnituskoodi saamiseks, mida illustreerib Telegram konto loomine.



### 1. samm: valige riik ja teenus



Mine [sms4sats.com](https://sms4sats.com) ja jää vahekaardile **RECEIVE**. Valige rippmenüüst soovitud numbri riik. Kui teie tellimuse sihtteenus on loetletud, valige see, et optimeerida vastuvõtuvõimalusi.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



Selles näites valime riigiks Prantsusmaa ja sihtteenuseks Telegram. Järgmise sammu jätkamiseks klõpsake nuppu **NEXT**.



### 2. samm: makske välkarvega arve



Välkarve kuvatakse QR-koodi kujul. Summa varieerub vastavalt valitud riigile ja teenusele. Skaneerige QR-koodi oma Lightning wallet-ga või kopeerige arve käsitsi maksmiseks.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Pange tähele olulist sõnumit: "No SMS Code = No Payment". Kui te ei saa SMS-i, tühistatakse teie makse automaatselt ja teile makstakse raha tagasi maksimaalselt 20 minuti jooksul.



### 3. samm: saada ajutine number



Kui makse on kinnitatud, kuvatakse kohe ajutine telefoninumber. Loendur näitab SMSi kättesaamiseni jäänud aega.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Kopeerige see number (siin +33 7 74 70 09 66), et kasutada seda teenuse puhul, millele soovite registreeruda.



### Samm 4: Kasutage sihtteenuse numbrit



Sisestage ajutine number rakenduses või veebisaidil, kus te loote oma konto. Meie Telegram näites sisestage number, kinnitage see ja oodake kinnituskoodi.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Protsess on identne tavapärase registreerimisega: sisestate numbri, Telegram saadab SMS-i teel kinnituskoodi ja seejärel lõpetate konto loomise.



### 5. samm: Kontrollikoodi hankimine



Tagasi SMS4Satsi kasutajaliidesesse. Niipea, kui SMS on vastu võetud, kuvatakse automaatselt aktiveerimiskood. Selle hõlpsaks kopeerimiseks klõpsake **COPY CODE**.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Registreerimise lõpuleviimiseks sisestage see kood sihttelefonil. Seejärel deaktiveeritakse ajutine number lõplikult.



## Saada anonüümne SMS



SMS4Sats võimaldab teil saata SMS-sõnumeid ka suvalisele numbrile ilma oma identiteeti paljastamata.



### 1. samm: sõnumi kirjutamine



Klõpsake vahekaardil **SENDA**. Sisestage sihtkoha telefoninumber koos rahvusvahelise numbrikoodiga ja kirjutage oma sõnum (maksimaalselt 1600 tähemärki).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Maksmiseks klõpsake nuppu **JÄRGMINE**.



### 2. samm: makske ja saatke



Makske kuvatav Lightning arve. Kui makse on kinnitatud, saadetakse SMS kohe saajale.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Sõnumi saatmise kinnitamiseks kuvatakse kinnituskood. Vastuvõtja saab SMS-i anonüümselt numbrilt.



## Rentida ajutine number



Kui on vaja kasutada mitu SMS-sõnumit samal numbril, võimaldab funktsioon RENT rentida numbri mitmeks tunniks.



### Rendikonfiguratsioon



Klõpsake vahekaardil **RENT**. Valige riik ja kestus.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Tähtis märkida:**




- Hinnad varieeruvad sõltuvalt riigist ja viibimise pikkusest
- Erinevalt ühekordselt kasutatavatest SMS-sõnumitest ei saa renditavat raha tagasi maksta**
- Renditud numbrid ei tööta üldiselt Telegram-ga
- See valik sobib mitme teenuse järjestikuse tellimiseks



Kui olete klõpsanud **NEXT** ja tasunud välkarve, saate numbri, mida saate kasutada rendiperioodi jooksul SMS-sõnumite vastuvõtmiseks ja saatmiseks.



## Eelised ja piirangud



### Tähtsündmused



**Personaalseid andmeid ei ole vaja**: Registreerimata mudel tagab, et isikuandmeid ei koguta.



**Kolme lisafunktsiooni**: Vastuvõtmine, saatmine ja rentimine katavad enamiku vajadustest.



**Maksmine ainult Bitcoin** : Lightning Network võimaldab koheseid ja pseudonüümseid tehinguid.



**Automaatne hüvitamine**: Hodl-arvete süsteem tagab, et maksate ainult siis, kui SMS saabub.



### Piirangud, millega tuleb arvestada



**Relatiivne SMS-kanali turvalisus**: SMS-koodid ei ole usaldusväärne autentimismeetod ja neid ei tohiks kasutada tundlike kontode puhul.



**Muutujate ühilduvus**: Paljud saidid tuvastavad ja blokeerivad virtuaalseid numbreid. Vajalik võib olla mitu katset.



**Mitte korduvkasutatavad numbrid**: Pärast ühekordset kasutamist võetakse number ringlusse ja seda ei saa taastada.



**Mitte tagastatavad renditehingud**: Erinevalt ühekordsetest SMS-sõnumitest ei ole rentimisel raha-tagastamisgarantiid.



## Parimad tavad



### Kasutage Tor'i rohkem privaatsust



SMS4Sats on kättesaadav [Tor] kaudu(sms4sat6y7lkqq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). See konfiguratsioon maskeerib teie IP-aadressi teenusele juurdepääsul.



### Vältida kriitilisi kontosid



Ärge kunagi kasutage oma oluliste kontode (pank, peamine e-posti aadress) jaoks ühekordset numbrit. Kui need platvormid nõuavad hiljem oma numbri uuesti valideerimist, kaotate juurdepääsu kontole.



### Eraldage oma digitaalsed identiteedid



Pseudonüümsete kontode puhul ühendage ajutine number ühekordselt kasutatava e-posti aadressi ja brauseriga, mida te tavaliselt ei kasuta.



### Valige tugev 2FA



Kui teie konto on loodud, aktiveerige tugevamad autentimislahendused: TOTP-rakendus (Aegis, Ente Auth) või FIDO2 füüsiline turvavõti.



## Kokkuvõte



SMS4Sats on terviklik lahendus konfidentsiaalsete SMSide haldamiseks. Olenemata sellest, kas soovite saada kinnituskoodi, saata anonüümset sõnumit või rentida ajutist numbrit, vastab teenus tänu Bitcoin Lightning'is tasumisele paljudele konfidentsiaalsusvajadustele.



Pidage siiski meeles selle piiranguid: teenus ei taga absoluutset anonüümsust ja ei sobi tundlike või pikaajaliste kontode jaoks. SMS4Sats on mõistlikult ja oma piiranguid teadvustades praktiline vahend oma telefonikõnede üle kontrolli taastamiseks.



## Ressursid





- [SMS4Sats ametlikul kodulehel](https://sms4sats.com)
- [Service FAQ](https://sms4sats.com/faq)
- [Tori aadress](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)