---
name: Tailscale
description: Täiustatud Tailscale õpetus
---
![cover](assets/cover.webp)



## 1. Sissejuhatus



Tailscale on järgmise põlvkonna VPN, mis loob teie seadmete vahel krüpteeritud võrgusilma. See võimaldab teil ühendada kaugmasinad nii, nagu oleksid need samas kohalikus võrgus, ilma keerulise seadistamise või portide avamiseta.



Self-hostingu puhul määrab Tailscale igale seadmele fikseeritud privaatse IP-aadressi virtuaalses võrgus, pakkudes stabiilset juurdepääsu teie teenustele isegi siis, kui teie avalik IP muutub. See tähendab, et saate oma servereid hallata eemalt, ilma et teie teenused oleksid otse internetile avatud.



** Peamised rakendused:**




- Isikliku serveri haldamine väljastpoolt
- Umbrel/Lightning sõlmede haldamine kiiremini kui Tor
- Turvaline juurdepääs Raspberry Pi või NAS-ile
- Ühendage oma teenustega SSH või HTTP kaudu ilma keerulise võrgukonfiguratsioonita



Selline lihtsusele keskenduv lähenemisviis võimaldab isehosteritele turvalist juurdepääsu oma teenustele, vältides traditsiooniliste VPNide lõkse.



## 2. Kuidas Tailscale töötab



Erinevalt traditsioonilistest VPNidest, mis suunavad kogu liikluse läbi keskserveri, loob Tailscale võrgusilma, kus seadmed suhtlevad omavahel otse. Keskne server tegeleb ainult autentimise ja võtme jagamisega, ilma et ta näeks kasutaja andmeid.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Joonis 1: Traditsiooniline VPN, mille puhul kogu liiklus liigub läbi keskserveri*



WireGuardil põhinev iga seade genereerib ise oma krüptograafilised võtmed. Koordineerimisserver jagab avalikud võtmed sõlmedele, mis seejärel loovad omavahel otsast lõpuni krüpteeritud tunneleid. Tailscale kasutab tulemüüride läbimiseks NAT-i ületamist ja viimase abinõuna DERP-redelit, mis säilitab krüpteerimise.



![VPN maillé (mesh)](assets/fr/02.webp)


*Joonis 2: Tailscale võrgusilma võrk, kus seadmed suhtlevad üksteisega otse*



Kogu side on krüpteeritud WireGuardiga. Tailscale näeb ainult metaandmeid (ühendused), kuid mitte kunagi andmevahetuse sisu. Suurema suveräänsuse tagamiseks võimaldab Headscale koordineerimisserveril olla isehostitav.



**Turvalisus ja konfidentsiaalsus:** Tänu WireGuardile on kogu side Tailscale'is otsast lõpuni krüpteeritud. Tailscale ei saa teie andmevahetust lugeda - ainult teie seadmetel on vajalikud privaatvõtmed. Teenus näeb ainult metaandmeid: IP-aadressid, seadmete nimed, ühenduse ajatemplid ja peer-to-peer-ühenduse logid (ilma sisuta).



See arhitektuur sõltub aga võrgu koordineerimise osas Tailscale Incist. Selle sõltuvuse kõrvaldamiseks pakub Headscale avatud lähtekoodiga alternatiivi, mis võimaldab teil ise hallata juhtimisserverit, kasutades samal ajal Tailscale'i ametlikke kliente, tagades seega täieliku suveräänsuse teie võrguinfrastruktuuri üle, kuid seda tehnilisema konfiguratsiooni hinnaga.



**Tailscale'i sisemise toimimise, sealhulgas juhtimistasandi haldamise, NAT-i ületamise ja DERP-redelite üksikasjaliku selgituse saamiseks soovitame lugeda suurepärase artikli [How Tailscale Works] (https://tailscale.com/blog/how-tailscale-works) ametlikus blogis. Selles artiklis selgitatakse põhjalikult tehnilisi kontseptsioone, mis teevad Tailscale'i nii võimsaks.



## 3. Tailscale'i paigaldamine



Tailscale töötab **sagedamates** operatsioonisüsteemides (Windows, macOS, Linux, iOS, Android). Installeerimine on väidetavalt "kiire ja lihtne" kõigil platvormidel. Alustame Interface ja konto loomisest, seejärel läheme edasi erinevate keskkondade paigaldusprotseduuride juurde.



### 3.1 Tailscale konto loomine



Mine aadressile [https://tailscale.com/](https://tailscale.com/) ja klõpsa nupule "Get Started" lehekülje paremas ülaosas.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Tailscale'i koduleht selgitab kontseptsiooni ja pakub tasuta algust*



Tailscale'i kasutamiseks peate esmalt looma konto identiteedi pakkuja kaudu:



![Page de connexion Tailscale](assets/fr/04.webp)


*Tailscale'iga ühendatava identiteedipakkuja valik (Google, Microsoft, GitHub, Apple jne)*



Pärast sisselogimist küsib Tailscale teilt teavet teie kasutusotstarbe kohta:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Vorm, et paremini mõista teie kasutusjuhtumit (isiklik või professionaalne)*



Kui olete oma konto loonud, saate Tailscale'i oma seadmetele paigaldada:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale võimaldab paigaldada rakenduse erinevatesse süsteemidesse*



### 3.2 Paigaldamine erinevatele platvormidele





- Windowsis ja macOSis:** Lihtsalt laadige graafiline rakendus alla Tailscale'i ametlikult veebisaidilt ja installige see (.msi-fail Windowsis, .dmg-fail Macis). Pärast installimist käivitab rakendus graafilise Interface, mis võimaldab teil (brauseri kaudu) ühendada oma Tailscale'i kontoga, et masinat autentida.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*MacBooki ühendamine sabavõrku*



![Connexion réussie](assets/fr/09.webp)


*Kinnitus, et seade on ühendatud Tailscale*-võrguga





- Linuxis (Debian, Ubuntu jne):** Teil on mitu võimalust. Kõige lihtsam meetod on käivitada ametlik paigaldusskript: näiteks Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



See skript lisab ametliku Tailscale'i repositooriumi ja installib paketi. Võite ka [lisada APT repositooriumi käsitsi](https://pkgs.tailscale.com) või kasutada tavalisi Snap või apt pakette. Pärast paigaldamist käivitub daemon `tailscaled` taustal. Seejärel peate **autentifitseerima sõlme** (vt allpool Interface CLI vs. veeb). Teistes distributsioonides (Fedora, Arch...) on pakett saadaval ka standardrepositooriumide või universaalse installeerimisskripti kaudu. Peata serveri puhul kasutage CLI: näiteks `sudo tailscale up --auth-key <key>`, kui kasutate eelnevalt genereeritud autentimisvõtit, või lihtsalt `tailscale up` interaktiivse sisselogimise puhul (mis annab URL-i, mida külastada seadme autentimiseks).





- ARM-põhistel süsteemidel (Raspberry Pi jne):** Me kasutame üldiselt Linuxi, seega sama lähenemine nagu eespool (skript või pakett). Pange tähele, et Tailscale toetab ARM32/ARM64 arhitektuuri ilma probleemideta. Paljud kasutajad installivad Tailscale'i Raspberry Pi OS-i kaudu apt või kergete distributsioonide (DietPi jne) abil, et pääseda oma Pi-le igal pool ligi.





- IOS ja Android:** Tailscale pakub **ametlikke** mobiilirakendusi. Lihtsalt installige *Tailscale* [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) või [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Tailscale'i paigaldamise sammud iPhone'ile: tervitus, privaatsus, teavitused, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Ühendage tailnetiga, valige konto ja valideerige iPhone'is*



Kui rakendus on paigaldatud, palub see esimesel käivitamisel autentimist valitud teenusepakkuja kaudu (Google, Apple ID, Microsoft jne, sõltuvalt sellest, mida kasutate Tailscale'i jaoks) - see on sama protseduur nagu teistel platvormidel, tavaliselt suunatakse ümber OAuthi veebilehele. Pärast seda loob mobiilirakendus VPN-i (iOS-i puhul peate nõustuma VPN-i konfiguratsioonilisaga). Seejärel võib rakendus töötada taustal, andes teile juurdepääsu oma tailnetile ükskõik kust. *Pange tähele:* Mobiilis saab teil olla korraga ainult **üks aktiivne VPN** - seega veenduge, et teil ei ole samal ajal ühendatud teist VPN-i, sest muidu ei saa Tailscale oma VPN-i luua. Androidis saate luua eraldi tööprofiili, kui soovite teatud kasutusviise isoleerida (nt profiili, kus Tailscale on aktiivne konkreetse rakenduse jaoks).



### 3.3 Mitme seadme lisamine ja valideerimine



Kui esimene seade on ühendatud, palub Tailscale teil lisada oma võrku teisi seadmeid:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface näitab esimest ühendatud seadet ja ootab teisi seadmeid*



Kui olete lisanud mitu seadet, saate kontrollida, et need saavad omavahel suhelda:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Kinnitus, et seadmed saavad omavahel suhelda pingi kaudu*



Seejärel pakub Tailscale välja lisakonfiguratsioone, et parandada teie kogemust:



![Suggestions de configuration](assets/fr/14.webp)


*Soovitused DNS-i seadistamiseks, seadmete jagamiseks ja juurdepääsu haldamiseks*



### 3.4 Administratsiooni armatuurlaud



Veebihalduskonsool võimaldab teil vaadata ja hallata kõiki ühendatud seadmeid:



![Tableau de bord des machines](assets/fr/15.webp)


*Ühendatud seadmete loetelu koos nende omaduste ja olekuga*



**Interface Web vs Interface CLI:** Tailscale pakub kahte teineteist täiendavat viisi võrguga suhtlemiseks: **Interface veebihaldus** ja **käsurea klient (CLI)**.





- Interface Web (halduskonsool)**: see veebikonsool, millele pääseb ligi aadressil [https://login.tailscale.com](https://login.tailscale.com), on teie Tailscale'i võrgu keskne armatuurlaud. Selles on loetletud kõik seadmed (*Masinad*), nende online/offline staatus, nende Tailscale'i IP-aadressid ja palju muud. Siin saate **haldada seadmeid** (ümber nimetada, võtmeid aeguda, marsruute lubada, sõlme keelata), **haldada kasutajaid** (organisatsioonilises kontekstis) ja määratleda turvanõudeid (ACL). Siin saate ka konfigureerida globaalseid valikuid, nagu MagicDNS, sildid või auth-klahvid (generate-eelsed auth-klahvid seadmete automaatseks lisamiseks). Interface veeb on väga mugav ülevaate saamiseks ja muudatuste kohaldamiseks, mida levitatakse koordineerimisserveri kaudu kõigile sõlmpunktidele. *Näide:* **allvõrgu marsruudi** või **väljumissõlme** aktiveerimine toimub ühe klõpsuga konsoolis, kui asjaomane sõlme on end selliseks kuulutanud.





- Interface käsurea (CLI):** Käsk `tailscale` on CLI-s saadaval igas seadmes, kuhu Tailscale on paigaldatud. See CLI võimaldab teil teha kõike lokaalselt: ühendada (`tailscale up`), kontrollida olekut (`tailscale status`, et näha, millised eakaaslased on ühendatud), siluda (`tailscale ping <ip>`) ja nii edasi. Mõned funktsioonid on isegi **eksklusiivsed CLI jaoks** või on arenenumad, näiteks:





  - `tailscale up --advertise-routes=192.168.0.0/24`, et reklaamida alamvõrgu marsruuti,
  - `tailscale up --advertise-exit-node`, et pakkuda oma masinat väljumissõlmeks,
  - `tailscale set --accept-routes=true` (või `--exit-node=<IP>`), et tarbida marsruuti või kasutada väljumissõlme,
  - `tailscale ip -4`, et kuvada seadme Tailscale IP,
  - `tailscale lock/unlock` (kui kasutatakse *tailnet-lock*, täiustatud turvafunktsiooni),
  - või `tailscale file send <node>`, et kasutada **Taildrop** (faili edastamine seadmete vahel).


CLI on väga kasulik serverites, kus puudub Interface graafika, ja teatavate tegevuste skriptimiseks. **Kasutamise erinevused:** Enamik põhikonfiguratsioone saab teha kas veebi või CLI kaudu. Näiteks seadme lisamine toimub kas konsooli kaudu küsides või käivitades seadmel `tailscale up` ja valideerides veebi kaudu. Samamoodi saab seadme ümbernimetamist teha konsooli kaudu või käsuga `tailscale set --hostname`. **Kokkuvõttes** on veebikonsool ideaalne võrgu globaalseks haldamiseks (eriti mitme masina/kasutaja puhul), samas kui CLI on mugav konkreetse masina peene kontrollimiseks, automatiseerimisskriptide jaoks või kasutamiseks süsteemis, millel puudub GUI (graafiline kasutajaliides).



## 4. Tailscale'i kasutamine Umbrelil



Umbrel on populaarne isehostinguplatvorm (mida kasutatakse eelkõige Bitcoin/Lightning sõlmede ja muude isehostetavate teenuste jaoks selle App Store'i kaudu). Umbreli paigaldamiseks ja seadistamiseks soovitame teil jälgida meie spetsiaalset õpetust:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Umbreli ja Tailscale'i koos kasutamine on eriti huvitav kasutusjuhtum, kuna Umbrel integreerib loomupäraselt Tailscale'i mooduli, mida on lihtne kasutusele võtta. Siin on toodud, kuidas Tailscale integreerub Umbreliga ja mida see toob kaasa:



### 4.1 Vihmavarju paigaldamine ja seadistamine





- Tailscale'i paigaldamine Umbrelile:** Umbrelil on App Store'is ametlik Tailscale'i rakendus. Installeerimine ei saaks olla lihtsam:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Tailscale rakenduse lehekülg Umbrel App Store'is*



Avage Interface veebi vihmavarju kaudu App Store, otsige **Tailscale** ja klõpsake *Install*. Mõni sekund hiljem on rakendus paigaldatud Umbrelile. Kui avate selle, kuvab Umbrel lehe, mis võimaldab teil siduda oma sõlme Tailscale'iga.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Tailscale ühendusekraan Umbrel's Interface*'s



Lihtsalt **klõpsake nupule "Logi sisse "**, mis suunab teid Tailscale'i autentimislehele:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Ühendage Tailscale'iga identiteedipakkuja kaudu*



Saate autentida oma Tailscale'i konto kaudu (Google/GitHub jne) või sisestada oma e-posti aadressi. Tavaliselt palub Interface Umbrelil külastada [https://login.tailscale.com](https://login.tailscale.com) ja logida sisse - see autentib Umbrel Tailscale'i rakendust.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Kinnitus, et Umbreli seade on ühendatud Tailscale'i võrku*



Kui see on tehtud, on teie Umbrel teie Tailscale'i võrgus ja ilmub teie konsooli nime all (nt *umbrel*). Seejärel saate kopeerimiseks klõpsata oma seadmete IP Address, otsida IPv6 Address või oma seadmega seotud MagicDNS-i.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Tailscale'i halduskonsool, mis näitab mitmeid ühendatud seadmeid, sealhulgas Umbrel*




### 4.2 Kaugjuurdepääs Umbreli teenustele



Kui Umbrel on ühendatud Tailscale'ile, **suudate Interface Umbrelile ja sellel töötavatele rakendustele ligi pääseda kõikjalt, nagu oleksite kohalikus võrgus**. See on üks peamisi eeliseid Tori ees.



Juurdepääs on märkimisväärselt lihtne: selle asemel, et kasutada `umbrel.local` (mis töötab ainult teie kohalikus võrgus), kasutate oma Umbreli Tailscale IP Address (`http://100.x.y.z`) otse mis tahes seadmest, mis on ühendatud teie tailnetiga. See toimib olenemata sellest, kus te olete või millist internetiühendust kasutate (4G, avalik Wi-Fi, ettevõtte võrk).



**Näited Umbrel-hostitud rakendustest, mis on kättesaadavad Tailscale'i kaudu:**





- Interface peamine vihmavarju**: Juurdepääs oma Umbreli armatuurlauale, lihtsalt sisestades brauserisse `http://100.x.y.z`
- Bitcoin sõlme**: Bitcoin sõlme haldamine ilma viivituseta, sünkroniseerimise ja statistika vaatamine
- Välgussõlm**: Kasutage ThunderHubi, RTLi või teisi Lightningi haldusliideseid, mis reageerivad kohe
- Mempool**: Vaadake Bitcoin tehinguid ja Mempool ilma Tori viivitusteta
- noStrudel**: Juurdepääs oma Nostr-teenustele, mida majutab Umbrel



**Konnake välised rahakotid oma Bitcoin või välgumihklidega Tailscale'i kaudu:**



Tailscale võimaldab ka teistesse seadmetesse paigaldatud Bitcoin ja Lightning rahakottidel otse teie Umbrel-sõlme ühendada:





- Sparrow wallet (Bitcoin)**: See väline Wallet Bitcoin saab Tailscale IP Address abil otse ühendada oma Umbreli Electrumi serveriga:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Privaatse Electrumi serveri konfigureerimine Sparrow wallet-s, kasutades Umbreli Tailscale IP Address*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Electrumi serveri varjunimede loetelu Sparrow-s koos Umbrel Tailscale IP Address*-ga



Lugege meie täielikku juhendit Sparrow wallet konfigureerimiseks koos Bitcoin sõlmega:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (välk)**: See Wallet mobiilne välk saab ühendada oma välgussõlme Umbrelil. Selle asemel, et konfigureerida lõpp-punkti `.onion', määrake lihtsalt oma Umbreli Tailscale IP ja Lightning API port. Võrreldes Toriga on ühendus kohene.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Zeuse konfigureerimine Lightning-sõlmega ühenduse loomiseks Tailscale* IP Address kaudu



Zeuse konfigureerimiseks koos oma Lightning-sõlmega vt meie üksikasjalikku õpetust:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Lisateavet Lightning Network ja selle tööpõhimõtete kohta Umbrelil leiate veebilehelt:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Eelised võrreldes Toriga



Umbrel pakub algselt kaugjuurdepääsu Tori kaudu (pakkudes oma veebiteenuste jaoks .onion-aadresse). Kuigi Tori eeliseks on konfidentsiaalsus (anonüümsus) ja see ei nõua registreerimist, leiavad paljud kasutajad, et **Tor on igapäevaseks kasutamiseks aeglane ja ebastabiilne** (leheküljed laadivad aeglaselt, ajakatkestused jne) - *"Umbrel Tori kaudu on nii aeglane "* kurdavad mõned.



Tailscale pakub üldiselt **kiiremat, madala latentsusega** ühendust, kuna liiklus liigub otse (või kiire relee kaudu), selle asemel, et põrgatada läbi 3 Tor-sõlme. Veelgi enam, Tailscale pakub "kohaliku võrgu" kogemust: kasutatakse privaatseid IP-sid ja rakendusi saab otse kaardistada (nt SMB võrgukettale \100.x.y.z).



See tähendab, et Tori eeliseks on detsentraliseeritud ja "out of the box" Umbrelil, samas kui Tailscale eeldab usaldust kolmanda osapoole (või hosting headscale) suhtes. Tor on kasulik ka kliendita juurdepääsuks (mis tahes Tor-brauserist saab Umbreli kasutajaliidesega konsulteerida, samas kui Tailscale nõuab juurdepääsu võimaldavale seadmele paigaldatud klienti).



**Kokkuvõttes** pakub Tailscale interaktiivseks kasutamiseks (Lightning wallets, sagedased veebiliidesed) võrreldes Toriga märgatavat mugavust ja kiirust, kuid selle hinnaga, et see on veidi sõltuvuses väljastpoolt. Paljud inimesed otsustavad kasutada *kumbagi*: Tailscale'i igapäevaselt ja Tor'i varuvariandina või selleks, et jagada juurdepääsu kellegagi, kutsumata teda oma VPN-i.



### 4.4 Ohutus



Kasutades Tailscale'i koos Umbreliga, väldite Umbreli kokkupuudet Internetiga. Umbreli sõlmpunkt on kättesaadav ainult teie teistele autenditud seadmetele Tailnetis, mis vähendab märkimisväärselt rünnakupinda (ükski port ei ole võõrastele avatud, puudub oht, et veebiteenust võidakse rünnata Interneti kaudu).



Side on krüpteeritud (WireGuard) lisaks mis tahes krüpteerimisele, mida teie teenused juba teevad (nt isegi sisemine HTTP on tunnelis). Saate endiselt rakendada Tailscale ACL-i, et näiteks takistada teatud tailneti seadme juurdepääsu Umbrelile, kui soovite võrku partitsioneerida. Umbrel ise ei näe vahet - ta arvab, et teenindab kohalikku.



---

Selle osa lõpetuseks: Tailscale'i integreerimine Umbrelisse võtab vaid paar klõpsu ja **parandab oluliselt teie isehostitava sõlme ligipääsetavust**. Saate Umbreli ja selle teenuseid hallata kõikjalt, turvaliselt ja tõhusalt, nagu oleksite kodus. See on eriti kasulik lahendus reaalajas töötavate rakenduste (Lightning) jaoks, mis kannatavad Tor'i latentsuse all, või üldisemalt iga isehosteri jaoks, kes otsib lihtsat privaatset ühendust. Kõik see ilma ühegi pordi** paljastamiseta teie kastis ja ilma keerulise võrgukonfigureerimiseta.



## 5. Täiustatud juhtimine ja kasutusjuhud



### 5.1 Tailscale täiustatud funktsioonid



**Võrgu haldamine:** Administreerimiskonsool (login.tailscale.com) võimaldab teil hallata oma seadmeid, vaadata ühendusi ja konfigureerida juurdepääsureegleid.



**MagicDNS:** Lahendab automaatselt seadmete nimed (nt `raspberrypi.tailnet.ts.net`), et vältida IP-aadresside meeldejätmist.



**ACL ja juurdepääsukontroll:** Määrake täpselt, kes saab teie võrgus millele juurdepääsu JSON-reeglite abil, mis on ideaalne teatud seadmete isoleerimiseks või konkreetsetele teenustele juurdepääsu piiramiseks.



**Device Sharing võimaldab teil kutsuda kedagi konkreetsele masinale juurdepääsu, andmata talle juurdepääsu kogu teie võrgule.



**Alavõrgu marsruuter:** Tailscale'i masin võib toimida terve alamvõrgu väravana, võimaldades juurdepääsu mitte-Tailscale'i seadmetele (IoT, printerid jne.) ühe seadistatud masina kaudu.



**Sõlme väljumine:** Kasutage masinat Interneti-väravana, et väljuda selle IP-ga. Kasulik avaliku Wi-Fi puhul või geograafilistest piirangutest möödahiilimiseks.



**Taildrop:** Turvaline alternatiiv AirDropile, mis võimaldab teil edastada faile oma Tailscale-seadmete vahel, olenemata nende platvormist või asukohast. Erinevalt AirDropist, mis on piiratud Apple'i ökosüsteemi ja füüsilise lähedusega, töötab Taildrop kõigi teie seadmete vahel (Windows, Mac, Linux, Android, iOS), isegi kui need asuvad eri riikides. Failid edastatakse seadmete vahel otse, kasutades otsast lõpuni krüpteerimist, ilma et need läbiksid keskset serverit. Kasutage sõltuvalt süsteemist käsurealt `tailrop faili cp` või graafilist Interface rakendust.



### 5.2 Võrdlus teiste lahendustega



**Vs OpenVPN:** Tailscale on palju lihtsam konfigureerida (ei ole vaja avada porte, ei ole vaja hallata sertifikaate), kuid see eeldab sõltuvust kolmanda osapoole teenusest. OpenVPN on täielikult kontrollitav, kuid nõuab rohkem teadmisi.



** Otsese konkurendina töötab ZeroTier Layer 2 (Ethernet), võimaldades ringhäälingut/multisaadet, samas kui Tailscale töötab Layer 3 (IP). ZeroTier pakub suuremat võrgu paindlikkust, samas kui Tailscale eelistab lihtsat kasutust.



**Vs Tor:** Tor pakub anonüümsust, mida Tailscale ei paku, kuid on palju aeglasem. Tor on detsentraliseeritud ja ei nõua kontot, samas kui Tailscale on kiirem ja pakub LANi sarnast kogemust.



**Vs WireGuard käsitsi:** Tailscale automatiseerib kõik võtmete ja ühenduste haldamise, mida WireGuard toorelt nõuab, et tegeleksite käsitsi. See on sisuliselt WireGuard + lihtsustatud haldus Layer.



Kokkuvõtteks võib öelda, et Tailscale on kaasaegne, lihtsusele orienteeritud lahendus, mis sobib ideaalselt isiklikuks kasutamiseks ja väikestele meeskondadele. Täieliku kontrolli puristidele pakub Headscale isehostimise alternatiivi.



## 6. Kokkuvõte



**Tailscale'i eelised:** Tailscale pakub mitmeid eeliseid isehostingu jaoks:





- Lihtsus ja jõudlus** - Kiire paigaldus kõigil platvormidel ilma keerulise võrgukonfiguratsioonita. Liiklus järgib kõige otsesemat teed teie masinate vahel (P2P võrgusilm), kasutades WireGuard-protokolli jõudlust ja ilma keskse serverita, mis piiraks läbilaskevõimet.
- Turvalisus ja paindlikkus** - otsast lõpuni krüpteerimine, vähendatud rünnakupind ja täiustatud funktsioonid (ACL, SSO/MFA autentimine). Töötab isegi NATide taga või liikvel olles, alamvõrgu marsruuterid ja väljumissõlmed, et kohandada võrk vastavalt teie vajadustele.



**Piirangud:** Pidage ka meeles:





- Väline sõltuvus** - Teenus tugineb oma standardversioonis Tailscale Inc. infrastruktuurile. Seda sõltuvust saab vältida Headscale'i kaudu (isehostitav alternatiiv).
- Muud piirangud** - Osaliselt suletud lähtekood, tasuta versiooni piirangud teatud edasijõudnud kasutusaladel, Layer 2 (broadcast/multicast) toetuse puudumine ja vajadus internetiühenduse loomiseks.



**Tailscale sobib ideaalselt üksikutele isehosteritele ja väikestele meeskondadele, arendajatele, kes vajavad juurdepääsu hajutatud ressurssidele, VPN-i algajatele ja mobiilsetele kasutajatele. Täielikku kontrolli vajavate ettevõtete jaoks võivad olla eelistatumad teised lahendused, näiteks Headscale või WireGuard otse.



**Esita Headscale täielikku isehostimist, API- ja DevOps-integratsiooni (Terraform) või alternatiive nagu Innernet (sarnane, kuid täielikult isehostitav) ja Netmaker.



Tailscale on tänu oma lihtsusele ja tõhususele hädavajalik vahend isehostingu jaoks, mis muudab teie privaatse infrastruktuuri nii kättesaadavaks, nagu oleks see pilves, säilitades samal ajal kontrolli kodus.



## 7. Kasulikud ressursid



### Ametlikud dokumendid





- Tailscale Dokumentatsioonikeskus**: [docs.tailscale.com](https://docs.tailscale.com) - Täielik ingliskeelne dokumentatsioon, paigaldusjuhendid, õpetused ja tehnilised viited.
- Kuidas Tailscale töötab**: [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) - Üksikasjalik artikkel, mis selgitab Tailscale'i sisemist toimimist.
- Muudatused**: [tailscale.com/changelog](https://tailscale.com/changelog) - Uuenduste ja uute funktsioonide jälgimine.



### Praktilised juhendid





- Kodulabori** õpetused: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Konkreetsed juhendid isemajutamiseks.
- Väljumissõlme konfigureerimine**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Üksikasjalik juhend Exit Node'i konfigureerimiseks.
- Kasutage Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Failide edastamine Tailscale'i seadmete vahel.



### Võrdlused





- Tailscale vs. muud lahendused**: [tailscale.com/compare](https://tailscale.com/compare) - üksikasjalikud võrdlused teiste VPN- ja võrgulahendustega (ZeroTier, OpenVPN jne).



### Ühendus





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - arutelud, küsimused ja tagasiside.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - kliendi lähtekood, kus saab jälgida arengut ja teatada probleemidest.
- Arutelu**: [discord.gg/tailscale](https://discord.gg/tailscale) - kasutajate ja arendajate kogukond.



Tailscale pakub regulaarselt uut sisu ja funktsioone. Vaadake nende [ametlikku blogi] (https://tailscale.com/blog/) viimaste uudiste ja juhtumiuuringute kohta.