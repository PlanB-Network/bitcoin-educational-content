---
name: Vihmavari Nostr
description: Nostri rakenduste konfigureerimine ja kasutamine Umbrelil
---

![cover](assets/cover.webp)



## Eeltingimused: Vihmavarju paigaldamine



Umbrel on avatud lähtekoodiga platvorm, mis võimaldab teil hõlpsasti majutada Bitcoin rakendusi ja muid teenuseid oma isiklikus serveris. See on kõik-ühes lahendus, mis lihtsustab oluliselt Bitcoin sõlmede ja detsentraliseeritud rakenduste isehostimist.



Veenduge, et olete paigaldanud Umbreli, järgides meie paigaldusjuhendit:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Sissejuhatus Nostrisse



**Nostr** on avatud, detsentraliseeritud võrguprotokoll, mis on mõeldud sotsiaalsete võrgustike loomiseks. Selle nimi tähendab _"Notes and Other Stuff Transmitted by Relays"_. See võimaldab igaühel avaldada sõnumeid (märkmeid), mida hallatakse JSON-sündmuste kujul, ja levitada neid tsentraliseeritud platvormi asemel releeserverite kaudu. Iga kasutaja omab paari krüptograafilisi võtmeid (privaatne/avalik), mis on identifikaatoriks: avalik võti (npub) identifitseerib kasutaja ja privaatne võti (nsec) võimaldab sõnumeid allkirjastada. Tänu sellisele hajutatud arhitektuurile pakub **Nostr tsensuurikindlust** ja suurt paindlikkust: saate kasutada mitut klienti ja ühendada nii palju releesid, kui soovite, sõltumata ühest serverist.



Lühidalt öeldes on Nostr detsentraliseeritud kommunikatsiooniprotokoll, kus **kliendid** (kasutaja rakendused) saadavad ja võtavad sündmusi vastu **relayers** (serverid) kaudu. See protokoll on alates 2023. aastast olnud Bitcoin kogukonna seas eriti populaarne tänu detsentraliseerimise ja andmete suveräänsuse väärtustele.



**Märkus:** Nostri kasutamiseks on vaja oma privaatvõtit (mis on loodud Nostri kliendiga või spetsiaalse laienduse abil). **Mitte kunagi jagage oma isiklikku võtit**, sest see võimaldaks kellelgi teid jäljendada. Hoidke seda turvalises kohas ja kasutage turvalisi võtmehaldusvahendeid (vt nõuannet allpool).



## Nostri vihmavarjurakendused



Umbrel pakub integreeritud rakenduste ökosüsteemi, et kasutada Nostr-i kõiki eeliseid teie isiklikus sõlmes. Me tutvustame üksikasjalikult peamiste Nostriga seotud rakenduste kasutamist: **Nostr Relay**, **noStrudel**, **Snort** ja **Nostr Wallet Connect**. Igaüks neist vastab konkreetsele vajadusele: _Nostr Relay_ on **privaatne releeserver**, _noStrudel_ ja _Snort_ on **Nostr-kliendid** (liidesed märkmete lugemiseks/avaldamiseks), samas kui _Nostr Wallet Connect_ on vahend teie **Lightning portfelli** ühendamiseks Nostriga.



### Nostr Relay - Sinu isiklik relee Umbrelil



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** on Umbreli ametlik rakendus oma **omase Nostr relee** jooksutamiseks oma sõlmes. Peamine eesmärk on saada **privaatne** ja usaldusväärne relee, et **tagada kogu oma Nostr** tegevust reaalajas. Teisisõnu, kasutades seda isiklikku releed lisaks avalikele releedele, tagate, et kõik teie märkmed, sõnumid ja reaktsioonid kopeeritakse koju, turvaliselt tsensuuri või andmekaotuse eest.



**Installeerimine:** Installige Umbrel App Store'ist (kategooria _Sotsiaalsed_), installige _Nostr Relay_. Pärast käivitamist jookseb rakendus taustal (docker service).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Umbreli kaudu näete selle Interface veebi: see annab põhiteavet ja eelkõige teie relee URL-i (üleval paremal), mille peate edasiseks kasutamiseks kopeerima. Saadaval on ka sünkroonimisnupp (maakera ikoon).



**Kasutada oma Umbrel relee :



**Lisandage relee oma Nostr-kliendile:** Lisage oma kliendirakenduses (nt Damus iOS-i, Amethyst Androidis, Snort või noStrudel Umbrelis jne) oma privaatse relee URL, mille te eelnevalt kopeerisite. Umbreli relee kuulab vaikimisi porti **4848**. Kui pääsete sellele ligi kohalikus võrgus, annab see URL-i nagu: `ws://umbrel.local:4848` (või kasutage Umbreli kohalikku IP-d).



Kui kasutate Tailscale'i (vt allpool), saate kasutada isegi MagicDNS-i DNS-pseudonime (tavaliselt `umbrel` või automaatselt genereeritud nime), et pääseda sellele ligi kõikjalt, alati pordist 4848.



Kui eelistate Tor'i, hankige oma Umbrel'i .onion Address ja kasutage seda port 4848 kaudu Toriga ühilduva brauseri või kliendi kaudu (vt Tor'i osa)



Kui URL on lisatud teie Nostr-kliendi releekonfiguratsiooni, ühenduge selle releega. Te peaksite oma kliendis nägema, et Umbreli relee on ühendatud (tavaliselt on see tähistatud Green punktiga vms).



**Sünkroniseeri ajalugu (valikuline)**: Interface veebis _Nostr Relay_ on Umbrel, klõpsake **globe** 🌐 ikoonil (lehekülje ülaosas). See toiming sunnib teie Umbreli relee ühendust võtma teie teiste releedega (need, mis on teie kliendis konfigureeritud), et **importida teie vanu avalikke** tegevusi. See tähendab, et varasemad märkmed, mida olete avalike releede kaudu avaldanud või lugenud, laaditakse alla ja salvestatakse ka teie privaatsesse releesse. Palun oodake sünkroniseerimist.



**Kasutage Nostr-i tavapäraselt:** Nüüdsest alates edastatakse kõik uued tegevused (avaldatud märkmed, reaktsioonid, krüpteeritud privaatsõnumid jne), mida te Nostr-is teostate, nagu tavaliselt avalikele releedele **ja paralleelselt teie Umbrel-relele**. Kui teie Nostr-klient on õigesti konfigureeritud, saadab ta iga sündmuse kõigile releedele (sealhulgas teie omale). Teie privaatne relee toimib reaalajas varukoopiana. Isegi ajutise katkestuse korral saavad teie kliendid tänu sellele releele puuduvaid andmeid hiljem uuesti sünkroniseerida. see annab teile täieliku kontrolli oma Nostr-andmete üle



Umbreli _Nostr Relay_ põhineb avatud lähtekoodiga **nostr-rs-relay** projektil (Rust protokolli rakendamine). See toetab kogu Nostr-protokolli ja mitmeid standardseid NIP-e (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33 jne), tagades maksimaalse ühilduvuse klientidega.



### noStrudel - Nostr klient uurijatele



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** on võimsale kasutajale orienteeritud Nostr veebiklient, mis on ideaalne Nostr-võrgustiku üksikasjalikuks mõistmiseks ja uurimiseks. See on omamoodi liivakast sündmuste ja releede kontrollimiseks ning protokolli täiustatud funktsioonide katsetamiseks. Interface on inglise keeles ja suhteliselt tehniline, mistõttu on see ideaalne kogenud kasutajatele, kes on uudishimulikud Nostr'i sisemise toimimise suhtes.



**Installatsioon:** Installige _noStrudel_ Umbrel App Store'ist (kategooria _Social_). Kui see on käivitatud, saab sellele ligi oma brauseri kaudu Umbreli Address (nt `http://umbrel.local` või selle .onion/Tailscale kaudu, vt välise juurdepääsu osa).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Releede konfigureerimine:** Kui avate noStrudeli, näete üleval paremas nurgas nuppu "Setup Relays". Klõpsake sellel, et konfigureerida oma releed.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Sisestage sellele lehele oma Umbreli relee URL, mille te varem kopeerisite. Saate lisada ka teisi rakenduse poolt vaikimisi pakutud releesid. Kui olete oma releed konfigureerinud, klõpsake jätkamiseks vasakus allosas "Logi sisse".



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Võimalus:** noStrudel pakub teile mitmeid ühendusvõimalusi. Meie puhul valime "Privaatne võti" ja kleebime sisse oma eelnevalt loodud Nostr privaatse võtme. Kui teil ei ole veel võtit, võite installida [Nostr Connect] laienduse (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj), et luua ja/või salvestada oma Nostr võtmed ja seega turvalisemalt suhelda erinevate Nostr rakendustega.



![Interface principale de noStrudel](assets/fr/07.webp)



Kui olete ühendatud, saate noStrudeli abil oma märkmeid Nostri kaudu jagada. Interface annab teile juurdepääsu :





- Täielik Nostr armatuurlaud koos märkuste ajaskaala, teavituste, sõnumite, profiiliotsinguga
- Relee haldamine ja ühenduse staatus
- Täiustatud vahendid sündmuste ja nende JSON-sisu uurimiseks
- Ajastufiltrite ja PIN-koodide seadistamisvõimalused



**Tipp:** _noStrudel_is saate seadistada _timeline-filtreid_ või testida erinevaid _NIPs (Nostr Implementation Possibilities)_. Näiteks kontrollige NIP-05 (detsentraliseeritud identifikaatorid) või uuemate funktsioonide toetust. See teeb _noStrudel_ suurepäraseks tööriistaks katsetamiseks kontrollitud keskkonnas.



### Snort - Modern Nostr klient Umbrelil



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** on veel üks Umbrelil saadaval olev Nostri veebiklient, mis pakub kaasaegset, kiiret ja lihtsat **Interface** detsentraliseeritud sotsiaalvõrgustikuga suhtlemiseks. Erinevalt noStrudelist, mis on suunatud võimsatele kasutajatele, on _Snort_ eesmärk lihtsa kasutuse poole, ilma funktsionaalsust ohverdamata. See on ehitatud Reactis ja pakub klassikalisi sotsiaalvõrgustikke meenutavat puhas UX-i, mis muudab selle igapäevaseks kasutamiseks sobivaks.



**Installatsioon:** Installige _Snort_ Umbrel App Store'ist (kategooria _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Kui avate Snorti, näete vasakus alumises nurgas nuppu "Registreeri".



![Options de connexion dans Snort](assets/fr/10.webp)



Saate valida, kas registreeruda või ühendada olemasoleva kontoga (mida me selle õpetuse jaoks ka teeme).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort pakub mitmeid ühendusmeetodeid. Saate kasutada eelnevalt paigaldatud Nostr Connect laiendust või muid olemasolevaid meetodeid. Kui olete ühendunud, saate rakendust täies ulatuses kasutada.



Interface alates _Snort_ pakub :





- **Postitused/Kõnelused/Globaalne** ekraan, et navigeerida oma märkmete, teemakohaste arutelude või globaalse voo vahel
- Vahelehti **Teavitused**, **Teateid** (DM), **Haigete**, **Profiil** jne.
- **+** või _Kirjuta_ nupp uue märkuse avaldamiseks
- **Tellimuste (järgnevate)** ja **loendite** haldamine
- Releede haldamise menüü releede lisamiseks/eemaldamiseks ja nende kättesaadavuse jälgimiseks



**Soovitatav relee konfiguratsioon:** Umbreli relee lisamiseks minge valikusse Seaded - Releed. Sisestage oma relee URL (`ws://umbrel:4848` või muu URL sõltuvalt teie konfiguratsioonist) Snorti releede loendisse. Nii avaldab Snort teie märkmed lisaks avalikule releele ka teie privaatsele releele.



### Nostr Wallet Connect - ühendage oma Lightning Wallet Nostriga



**Nostr Wallet Connect (NWC)** on rakendus, mis **ühendab teie Umbrel (Lightning)**-sõlme ühilduvate Nostr-rakendustega, et teha Lightning-makseid (näiteks saata _zaps_, need mikromaksed sisu "meeldimise" eest). Selles õpetuses vaatame, kuidas ühendada noStrudel oma Lightning-sõlmega, et teha makseid otse Interface-st.



**Installatsioon ja seadistamine:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Installige _Nostr Wallet Connect_ Alby poest Umbrelil.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



NoStrudelis klõpsake oma profiilil üleval paremas nurgas ja seejärel nupul "hallata".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Klõpsake "Lightning" ja seejärel "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Valige olemasolevate ühendusvõimaluste hulgast "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Klõpsake nupule "Connect", et suunata teid automaatselt oma Umbrel Nostr Wallet Connect seanssi.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Nostr Wallet Connect lehel saate :




   - Määrake oma maksimaalne eelarve
   - Autoriseeringute valideerimine
   - Määrake ühenduse kehtivusaeg


Klõpsake ühendamiseks nuppu "ühenda".



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Teid suunatakse ümber noStrudelile koos kinnitussõnumiga: nüüd saate oma Wallet/LND sõlme kaudu kogu maailma zappida!



Tänu NWC-le algavad sinu **Välgatusmaksed Nostri** kaudu (zapsid preemiapostidele, _Väärtus väärtuse eest_ maksed jne) **su enda sõlme** kaudu. Te ei pea enam iga kord oma tehinguid läbi väliste teenuste suunama või oma telefonist QR-koodi skaneerima. Kasutajakogemus on oluliselt paranenud, jäädes samas _valdkonnavaba_ ja privaatsussõbralikuks.



Kui soovite teada, kuidas luua oma Lightning-sõlme Umbrelil, siis soovitan vaadata seda teist põhjalikku õpetust:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Täiustatud konfiguratsioon ja turvalisus



Umbreli ja Nostri kasutamine koos edasijõudnute tasemel nõuab erilist tähelepanu **turvalisusele** ja **ühendatavusele**. Siin on mõned näpunäited, kuidas kaitsta oma konfiguratsiooni ja saada sellele optimaalne juurdepääs, kus iganes te ka ei viibiksite.



### Turvaline väline juurdepääs: Tor ja Tailscale



Turvalisuse huvides on teie Umbrel vaikimisi kättesaadav ainult teie kohalikus võrgus (ja Tor'i kaudu). Nostriga suhtlemiseks väljaspool kodu on teil kaks eelistatud lahendust: **Tor** (anonüümne juurdepääs sibulavõrgu kaudu) ja **Tailscale** (privaatne VPN-võrk).





- Juurdepääs Tori kaudu:** Umbrel konfigureerib automaatselt **Tori teenuse (.onion)** oma Interface veebi ja rakenduste jaoks. See tähendab, et saate Interface Umbrelile (sh _noStrudel_ või _Snort_) pääseda kõikjalt, kasutades Tori brauserit, ilma oma avalikku IP-d paljastamata. _Tori kasutatakse selleks, et pääseda Umbreli teenustele juurde väljaspool teie kohalikku võrku, ilma et teie seade oleks avatud internetile ([Setup Tor on your system - Guides - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww)). _ Selle võimaluse kasutamiseks minge Umbreli seadistustesse ja otsige välja oma Umbreli .onion URL (või skaneerige esitatud QR-kood). Tor-brauseris pääsete sellele .onion Address: saate sama Interface kui kohapeal. Seejärel saate kasutada oma Nostr-rakendusi nagu kodus.


**Nostr relee Tor'i kaudu:** Kui soovite, et teie Nostr relee oleks teie klientidele (või volitatud sõpradele) Tor'i kaudu kättesaadav, on see võimalik. Umbrel ei paku relee .onion Address otse, kuid kuna see töötab pordil 4848, saate kas :





    - Kasutage UI Umbrel'i .onion Address ja konfigureerige oma klient ühenduma selle Interface kaudu (WebSocket'i puhul ebapraktiline),





    - Või** avage port 4848 eraldi sibulateenusena. See nõuab Umbreli Tor-konfiguga mängimist (reserveeritud edasijõudnutele, kes tunnevad end hästi SSH-ga). Alternatiivina võiks kaaluda **Tor-tunnelit** mõnes teises serveris, mis suunab Umbrelisse: isiklikuks kasutamiseks on aga kõige lihtsam kasutada Tailscale'i.





- Juurdepääs Tailscale'i kaudu:** [Tailscale](https://tailscale.com/) on võrgusilma VPN-lahendus, mis loob virtuaalse privaatvõrgu teie seadmete ja Umbreli vahel. Eelis: see töötab nagu oleksite LAN-is, kuid üle interneti, krüpteeritult ja ilma keerulise seadistamiseta. **Tailscale määrab teie Umbrelile kindla IP- ja privaatse domeeninime, sõltumata selle võrgu asukohast ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. Praktikas, kui olete paigaldanud Tailscale'i Umbrelile (Umbrel App Store'ist, kategooria _Networking_) **ja** oma seadmetes (mobiil, arvuti...), saate Umbrelile ligi Address kaudu nagu `100.x.y.z` (Tailscale IP) või nime kaudu nagu `umbrel.tailnet123.ts.net`.


nostr_ puhul on Tailscale äärmiselt kasulik: teie mobiil, kui sellel on Tailscale aktiivne, saab ühendust `ws://umbrel:4848` (tänu MagicDNSile) või otse Tailscale'i IP ja port 4848, et kasutada releed. Kliendid nagu Damus või Amethyst näevad teie Umbrel'i nii, nagu oleks see samas kohalikus võrgus. **Nipp:** Võta Tailscale'is kasutusele valik **MagicDNS**, et kasutada hostinime `umbrel`, selle asemel, et IP-d meelde jätta. See tagab sujuva ühenduse teie releega isegi siis, kui olete liikvel ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Lisaks võimaldab Tailscale juurdepääsu Interface Umbrelile (ja seega ka _noStrudel/Snort_ veebiklientidele) lihtsa brauseri kaudu, kasutades privaatset IP-d või määratud domeeninime. Tor brauserit ei ole vaja ja andmeedastuskiirused on üldiselt paremad kui Tor-võrgu kaudu.




**Märkus: Tor ja Tailscale ei välista teineteist. Võite hoida Tori aktiivsena anonüümse juurdepääsu või konkreetsete teenuste jaoks ning kasutada Tailscale'i igapäevaselt selle lihtsuse tõttu. Mõlemal juhul ei pea te oma marsruuteril pori avama, mis tugevdab turvalisust.



### Nostr relee turvamine (soovitatavad tavad)



Kui te majutate Nostr-redelit Umbrelil, eriti edasijõudnute kontekstis, rakendage kindlasti mõningaid häid tavasid:





- Privaatne või piiratud relee:** Vaikimisi on teie Umbreli relee privaatne (ei ole avalikult teatavaks tehtud) ja kui pääsete sellele ligi ainult Tailscale'i või oma LANi kaudu, jääb see võõrastele kättesaamatuks. **Hoidke link konfidentsiaalsena ** Ärge edastage seda avalikes Nostr-võrkudes, kui te ei soovi vabatahtlikult teisi kasutajaid võõrustada, mis on hoopis teine teema (modereerimine, ribalaius jne). Isiklikuks kasutamiseks soovitame piirata juurdepääsu endale ja vajadusel mõnele usaldusväärsele sõbrale ja pereliikmele.





- Whitelist / Auth**: Nostr-rs-relay rakendamine toetab **NIP-42** autentimismehhanismi ning avalike võtmete _valgeid nimekirju_. Nende valikute lubamisega saate piirata oma releed nii, et see **võtab ainult teatud (teie)** võtmetega allkirjastatud sündmusi või et kliendid peavad avaldamiseks autentima. selle seadistamine nõuab relee `config.toml` konfiguratsioonifaili redigeerimist Umbrelis (SSH kaudu Docker-konteineris). _ See on edasijõudnud manipulatsioon, kuid näiteks saate loetleda lubatud kuulutused (`pubkey_whitelist`). Nii ei saa ta isegi siis, kui keegi sinu relee avastab, seal midagi avaldada, kui ta ei ole selles nimekirjas.





- Uuendused ja hooldus:** Hoidke oma Umbrel ja _Nostr Relay_ rakendus ajakohasena. Uuendused võivad sisaldada jõudluse parandusi (nt parem rämpsposti käsitlemine) ja turvaparandusi. Umbrelil kontrollige regulaarselt App Store'i, et leida uuendusi _Nostr Relay_ jaoks, ja rakendage neid vajaduse korral.





- Jälgimine ja piirangud:** Jälgige, kuidas teie releed kasutatakse. Kui avate selle teistele, jälgige oma Umbreli koormust (CPU/RAM mälu), sest relee võib kiiresti koguda palju andmeid. nostr-rs-relay pakub konfigureeritavaid **kiiruse ja salvestusruumi piiranguid** (`limiidid` konfiguratsioonis, nt sündmuste arv sekundis, sündmuste maksimaalne suurus, vanade sündmuste puhastamine...). Erakasutuseks ei pea te neid tõenäoliselt puudutama, kuid olge teadlik, et need parameetrid on olemas, kui te neid vajate ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Nostr-võtmete turvamine:** Seda punkti on juba mainitud, kuid see on ülioluline: ärge kunagi sisestage oma Nostr-võtmeid Interface-i, mida te ei usalda täielikult. Selle asemel kasutage tundlike toimingute allkirjastamiseks brauseripikendusi või väliseid seadmeid (näiteks Nostr _allkirjastajad_ eraldi telefonides). Umbrelil saavad teie veebikliendid, nagu _Snort_ ja _noStrudel_, töötada ilma teie salajase võtme teadmata, NIP-07 kaudu. Kasutage seda võimalust, et ühendada mugavus ja turvalisus.




Neid nõuandeid järgides on teie Umbreli sõlme integreerimine Nostriga nii võimas **ja** turvaline. Teil on täielik keskkond: Bitcoin-sõlm Lightning-maksete jaoks, privaatne Nostr-relee andmete suveräänsuse tagamiseks ja suure jõudlusega Nostr-veebikliendid, et navigeerida selles uues detsentraliseeritud sotsiaalvõrgustikus. Nautige Nostr'i avastamist koos Umbreliga!