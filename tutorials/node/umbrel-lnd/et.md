---
name: Umbrel LND
description: Täiustatud õpetus Lightning Network Daemon (LND) paigaldamiseks ja konfigureerimiseks Umbrelil
---
![cover](assets/cover.webp)




## Sissejuhatus



See edasijõudnute õpetus viib teid samm-sammult läbi Lightning Node (LND) rakenduse paigaldamise, konfigureerimise ja kasutamise teie Umbrel-sõlmes. Saate teada, kuidas avada kanaleid, hallata oma likviidsust ja sünkroonida oma sõlme mobiilirakendusega.



## 1. Eeltingimus: toimiv Bitcoin vihmavarju sõlmpunkt



Enne Lightning'i kasutuselevõttu peab teil olema Umbrelil täielikult toimiv Bitcoin sõlmpunkt. See hõlmab Umbreli paigaldamist (Raspberry Pi, NAS-i või muule masinale) ja Blockchain Bitcoin täielikku sünkroniseerimist.



Umbreli paigaldamiseks ja Bitcoin sõlme konfigureerimiseks soovitame jälgida meie spetsiaalset õpetust :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Veenduge, et teie Bitcoin-sõlm on ajakohane ja töötab korralikult, sest Lightning Network tugineb sellele kõigi off-chain tehingute tegemiseks.



## 2. Lightning Network tutvustus



Lightning Network on teine Layer protokoll, mille eesmärk on kiirendada ja vähendada Bitcoin tehingute maksumust, teostades neid väljaspool peamist Blockchain protokolli.



Konkreetsemalt öeldes kasutab Lightning sõlmede vaheliste maksekanalite võrgustikku: kaks kasutajat avavad kanali, blokeerides On-Chain BTC (esialgne tehing), seejärel saavad nad selle kanali piires koheselt teha Exchange makseid. Neid off-chain tehinguid ei registreerita Blockchain-s, mistõttu on nende kiirus ja praktiliselt nullkulu.



Makseid saab suunata läbi mitme kanali (tänu vahendussõlmedele), et jõuda mis tahes vastuvõtjani võrgus, võimaldades peaaegu piiramatus ulatuses koheseid tehinguid. Lightning pakub seega väga kiireid ja odavaid tehinguid, mis on ideaalsed igapäevaste maksete või mikrotehingute tegemiseks, kergendades samal ajal Blockchain Bitcoin koormust.



Töötamiseks peab Lightning-sõlm olema püsivalt ühendatud võrku ja suhtlema teiste Lightning-sõlmedega. On olemas erinevaid tarkvaralisi rakendusi (LND, Core Lightning, Eclair jne), mis kõik ühilduvad omavahel. Umbrel kasutab LND (Lightning Network Daemon) osana oma ametlikust Lightning Node'i rakendusest. See õpetus keskendub LND-le.



Lightning Network täieliku teoreetilise sissejuhatuse saamiseks soovitame teil läbida meie spetsiaalne kursus :



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

See kursus annab teile põhjaliku ülevaate Lightning Network põhimõistetest, enne kui liigute edasi LND sõlme kasutamise praktikasse.



## 3. Miks ise hostida LND?



Oma Lightning-sõlme (LND) haldamine Umbrelil annab teile täieliku suveräänsuse oma rahaliste vahendite ja kanalite üle, võrreldes hoiustatud või poolhoiustatud lahendustega.



### Välklahenduste võrdlus :



**Solutions custodiales (ex: Wallet of Satoshi)** :




- Teie Lightning bitcoin'eid haldab usaldusväärne kolmas osapool
- Lihtne kasutada, puudub tehniline keerukus
- Operaator hoiab teie raha ja saab jälgida teie tehinguid
- Te ohverdate kontrolli ja konfidentsiaalsuse



**Tarbijaportfellid, mis ei ole tooraineportfellid (nt Phoenix, Breez)** :




- Kasutajad säilitavad oma isiklikud võtmed ja seega Ownership oma BTC-d
- Täielik sõlme haldamine puudub - rakendus haldab kanaleid taustal
- Kompromiss lihtsuse ja suveräänsuse vahel
- Sõltuvus tarnijate infrastruktuurist likviidsuse tagamiseks
- Tehnilised piirangud (üks nutitelefon ei saa suunata makseid teistele)



**Iseseisev LND sõlmpunkt (Umbrel)** :




- Maksimaalne suveräänsus: teie On-Chain ja off-chain BTCd on täielikult teie kontrolli all
- Kanalite avamisse või maksete haldamisse ei ole kaasatud ühtegi kolmandat osapoolt
- Suurem konfidentsiaalsus (teie kanalid ja tehingud on teada ainult teile ja teie otsestele kolleegidele)
- Kasutusvabadus: ühendage oma teenused ja rahakotid
- Võimalus suunata tehinguid teiste jaoks (mikrotasu)
- Suuremad tehnilised kohustused (hooldus, likviidsuse haldamine, varundamine)



Lühidalt öeldes annab LND isehostimine teile maksimaalse kontrolli, kuid nõuab rohkem tehnilisi oskusi. See on kompromiss mugavuse ja suveräänsuse vahel.



## 4. Samm-sammult õpetus



### 4.1 Lightning Node'i rakenduse paigaldamine ja konfigureerimine Umbrelil



Kui teie Umbrel-sõlm (Bitcoin) on sünkroonitud, järgige järgmisi samme :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Installige Lightning Node'i rakendus Interface Umbrel'i jaotisest "App Store".



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) võetakse teie Umbrelil kasutusele rakendusena. Kui te seda esimest korda avate, näete hoiatussõnumit, mis teavitab teid, et Lightning on eksperimentaalne tehnoloogia.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Saate valida uue sõlme loomise või varukoopiast taastamise vahel/seed. Esmakordsel paigaldamisel valige uue sõlme loomine. Lightning Node app generate 24-sõnaline Mnemonic fraas (teie seed Lightning): kirjutage see väga hoolikalt üles (ideaalis offline, paberil), sest seda kasutatakse vajadusel Lightning-fondide taastamiseks.



**Märkus:** Umbreli uuemates versioonides annab Lightning-rakenduse paigaldamine selle 24-sõnalise seed (Bitcoin Umbreli sõlme ise ei paku).



![Interface principale de Lightning Node](assets/fr/04.webp)



Pärast initsialiseerimist pääsete Lightning Node'i peamise Interface juurde.



![Paramètres de l'application](assets/fr/05.webp)



Rakenduse seadetest leiate mitmeid olulisi valikuid:




   - Vaadake oma sõlme ID-d (teie sõlme unikaalne identifikaator)
   - Välise Wallet ühendamine (Connect Wallet)
   - Vaata salajasi sõnu
   - Juurdepääs täiustatud seadetele
   - Kanalite taastamine
   - Lae alla kanali varukoopia faili
   - Automaatse varundamise lubamine
   - Konfigureeri varundamine Tor'i kaudu (Backup over Tor)



Need valikud on olulised teie Lightning-sõlme turvalisuse ja haldamise jaoks. Veenduge, et aktiveerite automaatsed varukoopiad ja hoiate oma salajasi sõnu turvaliselt.



**Kasutatavad ressursid:**




- [Umbrel Community](https://community.umbrel.com) - arutelufoorum, kus kasutajad saavad jagada Umbreli ja selle ökosüsteemiga seotud probleeme ja lahendusi


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Lightning Node rakenduse funktsioonide kirjeldus Umbrelil
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Ametlik LND dokumentatsioon

### 4.2 Välgukanali avamine



Kui LND on käivitunud ja töötab, saate avada oma esimese Lightning-kanali. Kvaliteetsete sõlmede leidmiseks, millega ühenduda:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) on ekspluateerija usaldusväärsete sõlmede leidmiseks, et avada kanaleid.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Näiteks [ACINQ-sõlm] (https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) on tunnustatud sõlme, millel on suurepärane kättesaadavuse ja likviidsuse statistika.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Selle õpetuse jaoks avame kanali [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Ühendamiseks vajalikud andmed (pubkey@ip:port) on toodud nende Amboss'i lehel.



Kanali avamiseks :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Vajutage Lightning Node'i avalehel nupule "+ OPEN CHANNEL"



![Configuration du canal](assets/fr/10.webp)



Kanali konfiguratsioonilehel :




   - Sisestage Ambossist kopeeritud sõlme ID (formaat: pubkey@ip:port)
   - Määrake kanali läbilaskevõime suurus (mõnel sõlmpunktil nagu ACINQ on miinimummäärad, nt 400k Sats)
   - Vajaduse korral kohandada avamistehingute tasusid



![Canal en cours d'ouverture](assets/fr/11.webp)



Kui tehing on saadetud, kuvatakse kanal avalehel "avanevana". Oodake On-Chain tehingu kinnitust.



![Détails du canal](assets/fr/12.webp)



Klõpsake kanalil, et vaadata selle üksikasju:




   - Praegune staatus
   - Koguvõimsus
   - Likviidsuse jaotus (sissetulev/väljaminev)
   - Kaugse sõlme avalik võti
   - Ja muu tehniline teave



### Lightning Network+ kasutamine sissetuleva likviidsuse saamiseks



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ on saadaval Umbrel App Store'is, et lihtsustada sissetuleva raha saamist.



![Interface principale de LN+](assets/fr/14.webp)



Peamine Interface pakub kolme olulist võimalust:




- "Likviidsusvahetuslepingud: uurige olemasolevaid vahetuslepingute pakkumisi"
- "Open For Me": filtreeri vahetustehingud, mille jaoks oled abikõlblik
- "To Docs": juurdepääs dokumentatsioonile



![Message d'erreur LN+](assets/fr/15.webp)



Märkus: Kui teil ei ole veel kanalit avatud, näete seda veateadet, kui klõpsate nupule "Ava minu jaoks".



![Liste des swaps disponibles](assets/fr/16.webp)



Leheküljel "Likviidsuse vahetustehingud" on näha kõik võrgus kättesaadavad vahetustehingute pakkumised.



![Swaps éligibles](assets/fr/17.webp)



"Ava mulle" filtreerib ainult need vahetused, mille puhul teie sõlme vastab nõutud tingimustele.



![Détails d'un swap](assets/fr/18.webp)



Näide vahetuse üksikasjadest :




- Pentagoni konfiguratsioon (5 osalejat)
- Võimsus 300k Sats kanali kohta
- Eelduseks: vähemalt 10 avatud kanalit koguvõimsusega 1M Sats
- Vabad kohad: 4/5



### 4.3 Sünkroniseerimine mobiilirakendusega (Zeus)



Lightning-sõlme kaugjuhtimiseks (nutitelefon) saate kasutada Zeus (avatud lähtekoodiga rakendus, mis on saadaval iOS/Androidil).



**Zeuse konfiguratsioon koos vihmavarjuga :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Veenduge, et teie Umbrel-sõlm on ligipääsetav (vaikimisi Tor'i kaudu).


Avage Interface vihmavarju rakenduses Lightning Node, seejärel klõpsake nupul "Connect Wallet", nagu on näidatud noolega.



![Page de connexion avec QR code](assets/fr/20.webp)



Ilmub QR-kood, mis sisaldab teie LND juurdepääsuandmeid lndconnect-formaadis. See QR-kood sisaldab eriti palju teavet, seega ärge kartke seda lugemise hõlbustamiseks suurendada.



![Configuration initiale de Zeus](assets/fr/21.webp)



Teie telefonis :




   - Avatud Zeus
   - Klõpsake avalehel "Täpsem seadistamine", et ühendada oma Lightning-sõlm
   - Valige parameetrites "Loo või ühenda Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



Zeus:




   - Valige ühenduse tüübiks "LND (REST)"
   - Võite kas skaneerida QR-koodi (soovitatav meetod) või sisestada andmed käsitsi. (Ärge kartke Umbrel QR-koodi suurendada, kuna see on väga tihe)
   - Oluline: aktiveeri valik "Use Tor", kui su Umbrel on ligipääsetav ainult Tor'i kaudu (vaikimisi)
   - Konfigureerimise salvestamine



Teie Zeus on nüüd ühendatud teie Umbrel-sõlmega ja võimaldab teil teha välkmakseid, vaadata oma kanaleid, saldosid jne, jäädes samal ajal täielikult ise hallatavaks.



**Täiustatud ühendusvõimalused:**



Vaikimisi on Zeus ↔ Umbrel ühendus Tor'i kaudu. Kiirema ühenduse jaoks on kaks alternatiivi:



**Lightning Node Connect (LNC)** :




   - Lightning Labs'i krüpteeritud ühendusmehhanism
   - Installige Lightning Terminal rakendus Umbrelile (sisaldab LNC juurdepääsu)
   - generate ühendus QR-kood Lightning Terminalis (Connect → Connect Zeus via LNC)
   - Skaneerige see Zeusesse (valige ühenduse tüübiks "LNC")



**VPN Tailscale**:




   - Lihtsalt konfigureeritav võrgusilma VPN
   - Paigalda Tailscale Umbrel (App Store) ja oma mobiiltelefonile
   - Ühendage Zeus Tailscale'i privaatse IP kaudu Tor Address asemel



Need valikud ei ole kohustuslikud ja Tor + Zeus lahendus töötab enamasti hästi.



> **Kasutatavad ressursid:**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Ametlik juhend Zeuse ühendamiseks Umbreliga
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus avatud lähtekoodiga projekt
> - [Umbrel Community - Zeuse ühendamine Tailscale'i kaudu](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Juhend Zeuse ühendamiseks Umbreliga Tailscale'i abil

## 5. Ohutus ja parimad tavad



Isehostitava Lightning-sõlme haldamine nõuab erilist tähelepanu turvalisusele.



### Varundamine ja turvalisus teie sõlme jaoks



**Vajalikud varundustüübid**



Teie Lightning Umbrel-sõlme jaoks on vaja kahte tüüpi varukoopiaid:



**seed lause (24 sõna)**




- On-Chain vahendite tagasisaamine
- Vajalik, et taastada oma Wallet Lightning
- Ülimalt turvaliseks salvestamiseks (offline, paberil)



**Static Channel Backup (SCB)**-faili




- Sisaldab Lightning kanali teavet
- Võimaldab kanalite sunniviisilist sulgemist õnnetuse korral
- **Oluline:** Ärge kunagi salvestage faili `channel.db` käsitsi (karistuste oht)



**Manuaalne varundamise protseduur**



Kanalite käsitsi salvestamiseks :


1. Juurdepääs Lightning Node menüüle (kolm punkti "⋮" "+ Open Channel" kõrval)


2. Lae alla kanali varundatud fail


3. Eksportida uus SCB pärast iga kanali muutmist


4. Säilitada SCB-d turvaliselt (krüpteeritud andmekandjad, asukohaväline koopia)



**Umbrel** automaatne varundussüsteem



Umbrelil on keerukas automaatne varundussüsteem, mis tagab :



*Andmekaitse:*




- Kliendipoolne krüpteerimine enne edastamist
- Saatmine Tor-võrgu kaudu
- Andmed, mida on täiendatud juhusliku täitmisega
- Teie seadme ainulaadne krüpteerimisvõti



*Tõhustatud turvalisus:*




- Kohene varundamine staatuse muutumisel
- Juhuslike ajavahemike järel tehtud "peibutus"-varukoopiad
- Varukoopia suuruse muutuste varjamine
- Kaitse ajaanalüüsi vastu



*Taastamisprotsess:*




- Teie seed vihmavarju identifikaator ja võti
- Täielik taastamine võimalik ainult Mnemonic fraasiga
- Viimaste varukoopiate automaatne taastamine
- Kanalite seadete ja andmete taastamine



### Õnnetuse taastamine



Kui sõlme kaotatakse (riistvaraline rike, vigane SD-kaart) :




- Paigaldage vihmavarju uuesti
- Sisestage oma 24-sõnaline seed Lightning rakenduses
- SCB-faili importimine taastamise ajal



LND võtab ühendust iga teie vanade kanalite partneriga, et sulgeda need ja saada tagasi teie osa On-Chain vahenditest. Kanalid suletakse lõplikult (vajadusel avatakse uuesti).



### Kättesaadavus ja pettusekaitse



Ideaalis jätke oma sõlme võimalikult sageli online. Pikaajalise puudumise korral:




- Pahatahtlik partner võib üritada edastada vana kanali staatust
- Välk näeb ette "protestiperioodi" (umbes 2 nädalat LND puhul)
- Kui te kavatsete pikalt eemal olla, seadistage Watchtower



**Watchtower konfiguratsioon:**




- LND täiustatud seadetes lisage usaldusväärse Watchtower serveri URL-aadress
- Võite kasutada avalikku teenust või paigaldada oma Watchtower




Kui soovite rohkem teada saada, kuidas seadistada ja kasutada vaatetorne, soovitame vaadata meie spetsiaalset õpetust :



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Muud parimad tavad





- **Tarkvarauuendused:** Hoidke Umbrel ja LND ajakohasena (turvaparandused)
- **Riistvaraline kaitse:** Kasutage stabiilset süsteemi (Raspberry Pi koos SSD-ga, mini-PC) ja UPSi
- **Võrgu turvalisus:** Hoidke vaikimisi Tor konfiguratsioon, muutke Umbrel admini parool (vaikimisi: "moneyprintergobrrr")
- **Krüpteerimine:** Võimaluse korral lülitage sisse ketta krüpteerimine



## 6. Lisavahendid



Umbreli Lightning Node'i rakendus pakub kanaleid haldamiseks põhitõdesid, kuid kolmanda osapoole tööriistad pakuvad täiustatud funktsioone.



### ThunderHub



Interface kaasaegne veebipõhine Lightning-sõlme haldussüsteem, mis on paigaldatav Umbrel App Store'i kaudu.



**omadused:**




- Kanalite reaalajas visualiseerimine (võimsused, saldod)
- Integreeritud tasakaalustamise vahendid
- Mitme teekonnaga arveldamise (MPP) tugi
- QR-koodi genereerimine LNURL
- Tehingute haldamine On-Chain



ThunderHub sobib ideaalselt aktiivse marsruuterimissõlme jälgimiseks ja lihtsa tasakaalustamise teostamiseks.



### Ride The Lightning (RTL)



Interface veebi ühildub mitmete Lightning rakendustega (LND, Core Lightning, Eclair).



**Kõrgpunktid:**




- Mitme sõlme haldamine
- Kontekstitundlikud armatuurlauad
- Toetus allveelaevade vahetamiseks (Lightning Loop)
- 2-faktoriline autentimine
- Ekspordi/impordi kanali varukoopiaid



RTL on täielik "Šveitsi armee nuga" Lightning-sõlme haldamiseks eksperdikesksema lähenemisega.



### Muud kasulikud vahendid





- **Lightning Shell**: Käsurea (lncli) brauseri kaudu
- **BTC RPC Explorer ja Mempool**: Blockchain jälgimine
- **LNmetrics & Torq**: Marsruudi jõudluse analüüs
- **Amboss & 1ML**: oma sõlme "sotsiaalne" haldamine (aliased, kontaktid, võrguanalüüs)



Neid tööriistu saab paigaldada vaid paari klikiga Umbrel App Store'i kaudu, ilma keeruliste seadistusteta.



**Lisavahendid:**




- [ThunderHub.io - Omadused](https://thunderhub.io) - Ülevaade ThunderHubi omadustest
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL dokumentatsioon
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - Praktiline juhend tasakaalustamise kohta
- [Guide "Managing Lightning Nodes"](https://github.com/openoms/lightning-node-management) - Täiustatud dokumentatsioon elektrikasutajatele



## Kokkuvõte



Oma LND sõlme käivitamine Umbrelil on oluline samm finantssõltumatuse suunas. Kuigi see nõuab suuremat tehnilist kaasatust kui hoiulahendus, on Lightning Network kontrolli, konfidentsiaalsuse ja aktiivse osalemise osas saadav kasu märkimisväärne.



Kui te järgite seda juhendit, peaksite nüüd suutma paigaldada LND, avada kanaleid, hallata oma likviidsust ja pääseda oma sõlmpunktile kaugjuurdepääsu. Tutvuge järk-järgult täiustatud funktsioonide ja lisavahenditega, kui saate ökosüsteemiga paremini tuttavaks.



Pidage meeles, et teie rahaliste vahendite turvalisus sõltub teie kaitsemeetmetest ja tavadest. Võtke aega, et mõista kõiki aspekte enne suurte summade sidumist.