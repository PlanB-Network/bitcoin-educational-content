---
name: Vihmavarju
description: Avasta ja paigalda Umbrel - Sinu Bitcoin sõlme ja koduserver
---

![cover](assets/cover.webp)



## Sissejuhatus



### Mis on Bitcoin-sõlm?



Bitcoin-sõlm on arvuti, mis osaleb Bitcoin võrgus, kasutades Bitcoin Core tarkvara või alternatiivset klienti. Selle roll on võrgu toimimise ja turvalisuse seisukohalt oluline:





- Blockchain ladustamine**: Hoiab Blockchain täielikku ja ajakohastatud koopiat Bitcoin
- Tehingu kontrollimine**: valideerib iga tehingu ja ploki vastavalt protokolli reeglitele
- Teabe levitamine**: Jagab uusi tehinguid ja plokke teiste sõlmedega
- Konsensuse saavutamine**: Aitab kaasa võrgueeskirjade kohaldamisele



Oma Bitcoin-sõlme haldamine on oluline samm finantssõltumatuse suunas, pakkudes mitmeid olulisi eeliseid:





- Konfidentsiaalsus**: Jagage oma tehinguid ilma teie andmeid kolmandatele osapooltele avaldamata
- Vastupanu tsensuurile**: Keegi ei saa teid takistada Bitcoin kasutamast
- Sõltumatu kontroll**: Teie tehingute kontrollimiseks ei ole vaja usaldada teiste inimeste sõlmi
- Konsensuse saavutamine**: Bitcoin võrgueeskirjade kohaldamisele kaasaaitamine
- Võrgustiku tugi**: Hakka aktiivselt osalema võrgu levitamises ja detsentraliseerimises



### Vihmavarju: Bitcoin sõlme käivitamiseks lihtne lahendus



Umbrel on avatud lähtekoodiga operatsioonisüsteem, mis lihtsustab Bitcoin sõlme paigaldamist ja haldamist. Samuti muudab see teie arvuti isiklikuks ja privaatseks koduserveriks, muutes selle hõlpsasti võõrustatavaks :





- Täielik Bitcoin sõlmpunkt
- Bitcoin olulised rakendused (Electrs, Mempool.space)
- Muud isiklikud teenused (pilvesalvestus, voogedastus, VPN jne.)



Tänu oma elegantsele ja intuitiivsele Interface kasutajale Interface teeb Umbrel isehostitavad teenused kõigile kättesaadavaks, säilitades samas täieliku kontrolli oma andmete üle.



## Vihmavarju paigaldamise võimalused



Umbrel pakub oma lahenduse kasutamiseks kahte peamist võimalust: võtmevõimalus (Umbrel Home) ja tasuta avatud lähtekoodiga versioon (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: võtmed kätte lahendus



Umbrel Home on eelkonfigureeritud koduserver, mis on spetsiaalselt loodud optimaalse kasutuskogemuse tagamiseks. See kõik-ühes riistvaralahendus sisaldab järgmist:



**Hardvara omadused**




- Suure jõudlusega protsessor, mis on optimeeritud isehostimiseks
- Eelinstalleeritud kiire SSD-mälu
- Vaikne jahutussüsteem
- Kompaktne, elegantne disain
- Integreeritud USB- ja Ethernet-pordid



**Eksklusiivsed eelised**




- Plug-and-play paigaldus: ühenda ja käivita
- Premium-tugi koos spetsiaalse abiga
- Garanteeritud automaatsed uuendused
- Integreeritud migratsiooni viisard
- Täielik riistvara garantii
- Täielik toetus kõikidele funktsioonidele



**Hind**: 399 € (hind võib sõltuvalt hooajast erineda)



### UmbrelOS: avatud lähtekoodiga versioon



UmbrelOS on Umbreli operatsioonisüsteemi vaba, avatud lähtekoodiga versioon. See paindlik lahendus võimaldab teil kasutada oma riistvara, kasutades samal ajal Umbreli põhifunktsioone.



**Eelised**




- Täiesti tasuta
- Avatud, kontrollitav lähtekood
- Valikuvabadus
- Täiustatud kohandamisvõimalused



**toetatavad platvormid**




- Raspberry Pi 5: populaarne ja taskukohane lahendus
- X86 süsteemid: Tavaliste arvutite või serverite jaoks
- Virtuaalne masin: Testimiseks või kasutamiseks olemasolevas infrastruktuuris



**Piirangud




- Ainult ühenduse toetus
- Mõned täiustatud funktsioonid on reserveeritud Umbrel Home'ile
- Rohkem tehnilist algkonfiguratsiooni
- Jõudlus sõltub valitud riistvarast



See versioon on ideaalne :




- Tehnilised kasutajad
- Need, kes juba omavad ühilduvaid seadmeid
- Inimesed, kes tahavad õppida ja katsetada
- Arendajad, kes soovivad projekti panustada



Ametlikud paigalduslingid :




- [Paigaldamine Raspberry Pi 5-le](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Paigaldamine x86 süsteemidesse (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Virtuaalmasina paigaldamine](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



Selles õpetuses keskendume UmbrelOS-i paigaldamisele Raspberry Pi 5-le, kuid põhiprintsiibid on sarnased ka teiste platvormide puhul.



## Umbrel OS paigaldamine Raspberry Pi 5-le



### Vajalikud komponendid



Selle paigalduse jaoks on vaja :





- Raspberry Pi 5 (4 GB või 8 GB RAM)
- Ametlik Raspberry Pi võimsus Supply (stabiilsuse jaoks ülioluline!)
- MicroSD-kaart (vähemalt 32 GB)
- MicroSD-kaardi lugeja
- Väline SSD andmesalvestuseks
- Ethernet-kaabel
- USB-kaabel SSD-plaadi ühendamiseks



### Paigaldamise sammud



**Laadi alla UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Külasta [ametlik kodulehekülg](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- UmbrelOS uusim versioon Raspberry Pi 5 jaoks alla laadida



**Balena Etcher** paigaldus



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Lae alla ja paigalda [Balena Etcher](https://www.balena.io/etcher/) oma arvutisse



**MicroSD-kaardi** ettevalmistamine



![Insertion carte microSD](assets/fr/03.webp)




- Sisestage microSD-kaart arvuti kaardilugejasse



**Pildi vilkumine**



![Flashage UmbrelOS](assets/fr/04.webp)




- Balena Etcher'i käivitamine
- Valige allalaaditud UmbrelOS-kujutis
- Valige sihtkohaks oma microSD-kaart
- Klõpsake "Flash!" ja oodake, kuni protsess on lõppenud
- Kaardi turvaline väljaviskamine



**microSD-kaardi paigaldamine



![Installation microSD](assets/fr/05.webp)




- Sisestage microSD-kaart oma Raspberry Pi 5-sse



**Perifeerne ühendus**



![Connexion périphériques](assets/fr/06.webp)




- Ühendage väline SSD-plaat vabasse USB-porti
- Ühendage Ethernet-kaabel Pi ja ruuteri vahel



**Võimsus sisse



![Démarrage du Pi](assets/fr/07.webp)




- Ühendage ametlik Raspberry Pi toide Supply
- Oodake paar minutit, kuni süsteem käivitub



**Esimene juurdepääs**



![Accès interface web](assets/fr/08.webp)




- Avage samasse võrku ühendatud seadmes brauser
- Umbreli Interface veebisait on kättesaadav aadressil: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Kui `umbrel.local` ei tööta, peate leidma oma Raspberry Pi IP Address kohalikus võrgus. Saate :




- Vaadake oma ruuteri Interface
- Kasutades võrgu skannerit nagu nmap
- Kasutage oma arvuti terminalis käsku `arp -a`



## Esimene samm Umbrelil



Kui teie Umbrel on käivitatud ja brauseri kaudu kättesaadav, järgige järgmisi samme, et alustada:



### Esialgne konfiguratsioon



**Loo oma konto**



![Création compte](assets/fr/10.webp)




- Valige kasutajanimi
- Määrake turvaline parool
- Teie Umbrelile juurdepääsuks on vaja järgmisi volitusi



**Konto kinnitamine



![Confirmation compte](assets/fr/11.webp)




- Klõpsake "Järgmine", et pääseda oma armatuurlauale



** Interface avastamine**



![Interface Umbrel](assets/fr/12.webp)




- Juurdepääs Umbrel App Store'ile
- Avastage mitmeid olemasolevaid rakendusi
- Alustame Bitcoin jaoks oluliste rakenduste paigaldamisega



### Bitcoin rakenduste paigaldamine



**Bitcoin sõlme**



![Bitcoin Node](assets/fr/13.webp)




- Esimene paigaldatav rakendus
- Laadige alla ja kontrollige kogu Blockchain Bitcoin



**Valimised**



![Installation Electrs](assets/fr/14.webp)




- Electrumi server Bitcoin rahakottide ühendamiseks
- Sünkroniseerib oma Bitcoin sõlme



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Interface ekraan Blockchain jaoks
- Jälgib tehinguid ja plokke reaalajas



## Tehingu jälgimine Mempool.space abil



Mempool.space on avatud lähtekoodiga Blockchain explorer, mis pakub Bitcoin võrgu visualiseerimist reaalajas. See võimaldab teil jälgida oma tehinguid ja mõista, kuidas tehingud võrgus levivad.



### Mempool ja kinnituste mõistmine



"Mempool" (mälupool) on nagu virtuaalne ooteruum, kus kõik kinnitamata Bitcoin tehingud hoitakse enne blokki lisamist. Siin on näha, kuidas tehingut töödeldakse:



1. **Raadiosaade**: Kui te saadate tehingu, edastatakse see esmalt Bitcoin võrgus


2. **Ootab Mempool**: Ootab, et Miner valitakse kulude alusel


3. **Esimene kinnitus**: Alaealine lisab selle plokki (1. kinnitus)


4. **Lisakinnitused**: Iga uus plokk, mis kaevandatakse pärast teie tehingut sisaldavat plokki, lisab kinnituse



Soovitatav kinnituste arv sõltub summast :




- Väikeste koguste puhul: 1-2 kinnitust võib piisata
- Suurte koguste puhul: 6 kinnitust peetakse üldiselt väga turvaliseks



### Avasta Interface alates Mempool.space



1. **Etuleht** annab teile ülevaate Bitcoin võrgustikust:




   - Hiljuti kaevandatud plokid
   - Erinevate prioriteetide kuluhinnangud
   - Mempool praegune olukord



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Tehingu otsimine**: Konkreetse tehingu jälgimiseks sisestage selle identifikaator (txid) lehekülje ülaosas asuvasse otsinguribale.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analüüsige tehingu üksikasju



Kui teie tehing on leitud, esitab Mempool.space teile täieliku analüüsi:



1. **Vajalik teave** :




   - Staatus (kinnitatud või kinnitamata)
   - Makstud kulud (Sats/vB)
   - Eeldatav kinnitamise aeg



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Tehingu struktuur** :




   - Sisendite ja väljundite visuaalne kujutamine
   - Asjaomaste aadresside üksikasjalik loetelu
   - Ülekantud summad



3. **Tehnilised andmed** :




   - Tehingu kaal
   - Virtuaalne suurus
   - Kasutatav vorming ja versioon
   - Muud spetsiifilised metaandmed



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Mempool.space'i kasutamise eelised Umbrelil



1. **Saladuse hoidmine**: Teie taotlused lähevad läbi teie enda sõlme


2. **Sõltumatus**: Ei ole vaja toetuda kolmanda osapoole teenusele


3. **Lootlikkus**: Juurdepääs andmetele isegi siis, kui avalikud veebilehitsejad ei tööta



Selle rakenduse abil saate tõhusalt jälgida oma tehinguid, mõista, kuidas tasud mõjutavad kinnituse kiirust, ja saada paremat ülevaadet Bitcoin võrgu toimimisest.



## Wallet Bitcoin ühendamine oma sõlmpunktiga



### Elektrite konfiguratsioon



**Lokaalne ühendus



![Connexion locale](assets/fr/18.webp)




- Kasutamiseks kohalikus võrgus
- Kiirem ja lihtsam seadistamine



**kaugühendus Tor'i kaudu**



![Connexion Tor](assets/fr/19.webp)




- Et oma sõlmpunktile ükskõik kust ligi pääseda
- Turvalisem ja privaatsem



### Ühendus Sparrow Wallet-ga



**Juurdepääs parameetritele



![Paramètres Sparrow](assets/fr/20.webp)




- Avatud varblane Wallet
- Mine seadistused > Server
- Klõpsake nuppu "Olemasoleva ühenduse muutmine"



**Võimalus valida ühenduse tüüp



Sparrow pakub kolme ühendusrežiimi:



***Üldine server***




- Ühendus avalike serveritega (nt blockstream.info, Mempool.space)
- Lihtne, kuid vähem privaatne



***Bitcoin Core***




- Otsene ühendus Bitcoin sõlmpunktiga
- Privaatne, kuid aeglasem



***Privaatne Electrum***




- Ühendage oma Electrs serveriga
- Ühendab konfidentsiaalsuse ja jõudluse



**Valimiste** konfiguratsioon



Valige oma ühenduse tüüp, kasutades eelnevalt nähtud Electrs rakenduses kuvatavat teavet:



Mõlemal juhul jätke valikud "Use SSL" ja "Use proxy" märkimata.



**Lokaalne ühendus


Host: umbrel.local


Sadama number: 50001



**kaugühendus (Tor)**


Host : [teie-Address-onion]


Sadama number: 50001



Tor-ühendus on vajalik, kui soovite oma sõlme kasutada väljaspool kohalikku võrku.



![Configuration connexion](assets/fr/21.webp)


Lisateavet Sparrow Wallet tarkvara kohta leiate põhjalikust juhendmaterjalist :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Kokkuvõte



Teie vihmavarju on nüüd kasutusvalmis. Te osalete aktiivselt Bitcoin võrgus, säilitades samal ajal täieliku kontrolli oma andmete üle. Tutvuge julgelt paljude teiste rakendustega, mis on saadaval Umbrel App Store'is, et laiendada oma koduserveri võimalusi.



## Kasulikud ressursid



### Ametlikud dokumendid




- [Ametlik vihmavarju veebileht](https://umbrel.com)
- [Umbrel dokumentatsioon](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoin rakendused




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### Ühendus




- [Foorumi vihmavarju](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitteri vihmavarju](https://twitter.com/umbrel)