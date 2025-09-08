---
name: Orioni brauser
description: Kuidas kasutada Orion Browser'i, et kaitsta oma privaatsust Macis ja iPhone'is?
---

![cover](assets/cover.webp)



## Sissejuhatus



Olukorras, kus enamik brausereid kogub massiliselt meie isikuandmeid, muutub privaatsussõbraliku brauseri valik otsustavaks. Chrome domineerib 65% maailmaturust, kuid selle ärimudel põhineb teie sirvimisandmete ärakasutamisel. Safari on küll integreeritud Apple'i ökosüsteemi, kuid tal puuduvad täiustatud kaitsefunktsioonid ja ta ei toeta paindlikult kolmanda osapoole laiendusi.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Veebibrauserite turu jaotus: Chrome domineerib üle 65% turuosaga, järgnevad Safari, Edge ja Firefox*



**Orion Browser** on uuenduslik alternatiiv Apple'i kasutajatele. See Kagi poolt välja töötatud brauser ühendab WebKit-mootori kiiruse ja nulltelemeetria filosoofia. Erinevalt konkurentidest ei saada Orion andmeid kaugserveritesse ning blokeerib 99,9% reklaame ja jälgimisseadmeid, sealhulgas YouTube'i.



Selle unikaalne omadus? Orion on **väike** WebKit** brauser, mis suudab installeerida Chrome'i **ja** Firefoxi laiendusi, pakkudes mõlemast maailmast parimat. Selline ühilduvus koos mälukulu 2 kuni 3 korda väiksema mälutarbimisega kui teised brauserid ja sujuv integratsioon Apple'i ökosüsteemiga (iCloud, võtmehoidja) teevad sellest ideaalse valiku privaatsust tagavatele Mac'i ja iPhone'i kasutajatele.



## Miks valida Orion Browser?



### Peamised eelised



**Maksimaalne kaitse kohe karbist välja**: Orion blokeerib vaikimisi 99,9% reklaamidest (sh YouTube'i) ja kõik esimese osapoole ja kolmandate osapoolte jälgimisseadmed. Selle tehnoloogia ühendab WebKit'i intelligentse jälgimise vältimise ja EasyPrivacy nimekirjad maksimaalse tõhususe saavutamiseks. Ainulaadne funktsioon: Orion blokeerib sõrmejälgede skriptid **eelselt**, muutes jälgimise sõna otseses mõttes võimatuks - radikaalsem lähenemine kui teised brauserid, mis püüavad andmeid ainult "maskeerida".



**Nulltõendatav telemeetria**: Orion kasutab radikaalset lähenemist privaatsusele, kuna telemetria on algselt null. Erinevalt teistest brauseritest, mis teevad käivitamisel sadu võrgupäringuid (IP-eksponent, brauseri sõrmejälg, isikuandmed), ei "helista" Orion kunagi koju. See põhimõtteline erinevus välistab täielikult tahtmatu andmete lekkimise ohu.



**Väljapaistev jõudlus**: Orion põhineb WebKit'i optimeeritud versioonil, mis võrdub või isegi ületab Safari kiiruse poolest Macil. Kiirusmõõtja 2.0/2.1 testid asetavad selle järjekindlalt esikohale Apple Silicon protsessoritel. Natiivne reklaamide blokeerimine kiirendab lehekülje laadimist veelgi 20-40%.



**Universaalne laiendustugi**: Orion võimaldab paigaldada laiendusi Chrome'i veebipoest **ja** Mozilla Add-ons'ist. WebEhenduste tugi on praegu eksperimentaalne, eesmärk on 100% ühilduvus beetaversioonis. Saate kasutada paljusid populaarseid laiendusi, nagu uBlock Origin, Bitwarden, isegi iPhone'is - see on iOS-i puhul maailma esimene võimalus, kuigi mõned neist ei pruugi ideaalselt toimida.



### Piirangud, millest tuleb olla teadlik





- Piiratud kättesaadavus**: Praegu reserveeritud macOS ja iOS/iPadOS jaoks. Linuxi versioon on jõudmas arenduse verstapostini (Milestone 2 2025), kuid avalik build ei ole saadaval. Windows ja Android ei ole ressursside puudumise tõttu arenduses.
- Suletud lähtekood**: Kuigi mõned komponendid on avatud lähtekoodiga, jääb Orion valdavalt omandis olevaks, mis on eraelu puutumatuse kogukonnas vaidluse objektiks.
- Eksperimentaalsed laiendused**: Laienduste tugi on endiselt beeta-staadiumis, kus esineb sageli vastuolusid. Laiendused võivad mõjutada jõudlust ja mõned ei tööta üldse.
- WebKit turvalisus**: Erinevalt Chromiumist ei paku WebKit nii tugevat saitidevahelist protsesside isoleerimist, mis võib teatud stsenaariumides tekitada turvariske.
- Blokeerimiskatsed**: Orioni tulemused veebireklaami testides on tahtlikult kehvad (26-35%), kuna Kagi peab neid teste "põhimõtteliselt vigaseks". Tegelik tõhusus igapäevases kasutuses on palju parem.



## Orion Brauseri paigaldamine



### MacOSis



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*Kagi koduleht, mis tutvustab Orion Browser'i kui "reklaamivaba brauserit täieliku privaatsuskaitse ja universaalse laienduste toetusega "*





- Mine [kagi.com/orion](https://kagi.com/orion/)
- Klõpsake nupule "**Download Orion for macOS**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Orion Brauseri allalaadimisleht, mis näitab macOS ja iOS versiooni kättesaadavust, koos linkidega App Store'ile*





- Avage allalaaditud `.dmg`-faili
- Lohistage Orioni rakendus rakenduste kausta
- Esimesel käivitamisel palub macOS teil kinnitada avamist



**Alternatiivsed kodupruudid**:


```bash
brew install --cask orion
```



### IPhone'is/iPadis





- Avage **App Store**
- Otsi "**Orion Browser by Kagi**"
- Installi tasuta rakendus (iOS 15+ ühildub)



### Esialgne konfiguratsioon



Esimesel käivitamisel juhendab Orion teid mitme sammu kaudu:



**1. Tervituskuva


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Orion Brauseri tervitusekraan, kus on esile toodud peamised funktsioonid: kiirem sirvimine, telemeetria puudumine, reklaamide blokeerimine ja laienduste tugi*



**2. Interface** kohandamine


![Options de personnalisation](assets/fr/05.webp)


*Kohandamisekraan võimaldab teil konfigureerida vahekaartide ja Interface välimust vastavalt oma eelistustele*





- Andmete import**: Liigutage hõlpsasti lemmikud ja paroolid Safarist, Chrome'ist või Firefoxist
- ICloudi sünkroonimine**: Aktiveerige, et leida oma lemmikud ja vahekaardid kõigis oma Apple'i seadmetes



**3. Paigaldamine mobiilseadmetesse**


![Installation sur iOS](assets/fr/06.webp)


*Installeerimisekraan iOS-i puhul, mis näitab QR-koodi Orion Browser'i kiireks allalaadimiseks App Store'ist*



**4. Interface teretulnud ja olulised vahendid



![Page d'accueil Orion](assets/fr/07.webp)


*Orion Browser Interface avaleht: noolega on näidatud kolm peamist tööriista, mis on kättesaadavad otse Address ribalt*



Kui konfiguratsioon on lõpule viidud, avastate Orioni lihtsustatud Interface koos **kolme olulise tööriistaga** (näidatud noolega):





- Kilp 🛡️**: Kuvab privaatsusaruande koos blokeeritud elementide arvuga praegusel lehel
- Pintsel 🖌️**: Lehekülje kuvamise kohandamine (teema, font, häiriva Elements eemaldamine)
- Käik ⚙️**: Veebilehe spetsiifiliste parameetrite seadistamine (õigused, blokeerimine jne.)



Need tööriistad on alati saadaval ja võimaldavad teil kontrollida oma sirvimiskogemust iga saidi kohta eraldi.



**Tähtis**: Orion on tasuta ja ei nõua registreerimist ega konto loomist.



![Orion+ dans les préférences](assets/fr/08.webp)


*Orion+ tellimuse ekraan eelistustes, mis pakub valikulist tellimust arenduse toetamiseks*



**Orion+ (valikuline)**: Kagi pakub projektiarenduse toetamiseks Orion+ (5 $/kuu, 50 $/aasta või 150 $ kogu eluaeg). See vabatahtlik tellimus võimaldab:




- Suhtlemine otse arendusmeeskonnaga
- Mõjutage brauseri arengut vastavalt oma vajadustele
- Juurdepääs uusimate eksperimentaalsete funktsioonidega öistele versioonidele
- Kasuta uusimat WebKit mootorit
- Saage tagasisidefoorumis eristav märk



Orion+ tagab projekti sõltumatuse: "Teie rahaline panus aitab meil jääda sõltumatuks ja pidada oma lubadust saada parimaks brauseriks meie kasutajate jaoks". Just see kasutajate rahastamise mudel hoiab Orioni reklaamivabana ja telemeetriavaba.



## Konfigureerimine maksimaalse konfidentsiaalsuse tagamiseks



### Olulised parameetrid



Juurdepääs eelistustele on **Orion → Eelistused** (või ⌘,):



**1. Otsing - privaatne otsingumootor**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Vaikimisi otsingumootori konfiguratsioon: DuckDuckGo on valitud maksimaalse privaatsuse tagamiseks*





- Vaikimisi mootor**: Valige **DuckDuckGo**, **Startpage** või **Kagi** optimaalse privaatsuse tagamiseks (vältige Google/Bing)
- Otsingusoovitused**: Lülitage need välja, et vältida klahvivajutuste lekkimist otsingumootori serveritesse



**2. Privaatsus - üldine** kaitse



![Content Blocker dans les préférences](assets/fr/12.webp)


*Orioni privaatsusseaded, mis näitavad sisu blokeerija 119 156 aktiivset reeglit, jälgimisseadete eemaldamise võimalusi ja kohandatud kasutajaagenti*



**Vaikimisi aktiivne sisublokeerija**:




- EasyList**: 119k+ reklaami blokeerimise reeglit
- EasyPrivacy**: Kaitse jälgimise eest
- Filtrite nimekirjade haldamine**: Lisada täiendavaid nimekirju (Hagezi soovitatav)



**Privaatsusvalikud**:




- Eemaldage URL-idelt jälgijad**: "Ainult privaatseks sirvimiseks" puhastab kopeeritud lingid
- Jagage õnnetusaruandeid**: "Pärast nõusoleku küsimist" austab teie nõusolekut
- Kohandatud kasutajaagent**: Saab muuta, et vältida teatud blokeeringuid



![YouTube avec Privacy Report](assets/fr/10.webp)


*Näide YouTube'i vaatamisest Orioniga: reklaam ei ole nähtav ja privaatsusaruanne näitab paljusid blokeeritud Elements*



**3. Veebisaidi seaded - kontroll saidi kaupa**



![Website Settings pour YouTube](assets/fr/11.webp)


*YouTube'i veebisaidi seaded, mis näitavad ühilduvusvalikuid, sisu blokeerimist ja saidispetsiifilisi õigusi*



**Pikajuurdepääs**: Klõpsake Address riba hammasratast ⚙️, et reguleerida:




- Ühilduvusrežiim**: Lahendab kuvaprobleemid, peatades laiendused
- Sisublokaatorid**: Vajaduse korral deaktiveerige blokeerimine konkreetse saidi jaoks
- JavaScript/Küpsised**: Granulaarset kontrolli saidi kaupa
- Õigused**: Kaamera, mikrofon, asukoht individuaalselt konfigureeritud



**4. Täiustatud kohandatud filtrid** (vt allpool)



**Looge kohandatud filtrid** (Privaatsus → Filtrite nimekirjade haldamine → Kohandatud filtrid):



**Ühendatud süntaks** (Adblock Plus'iga ühilduv):




- `reddit.com##.promotedlink`: Peidab sponsorlusega Redditi postitused
- `||||ads.example.com^`: Blokeerib täielikult reklaamdomeeni
- `@@|||site-utile.com^`: Luuakse erand saidi jaoks



**Tipp: Külastage [FilterLists.com](https://filterlists.com), kus on tuhandeid kasutusvalmis spetsialiseeritud nimekirju.



### Soovitatavad laiendused



Orion toetab algselt Chrome'i ja Firefoxi laiendusi. Paigaldage need otse ametlikest poodidest:



**Esentsiaalid**:




- uBlock Origin**: Lisab granuleeritud kontrolli algupärasele blokeerijale
- Bitwarden**: Avatud lähtekoodiga paroolihaldur
- ClearURLs**: Kustutab URL-i jälgimisparameetrid



**Võimalik**:




- LocalCDN**: Teenindab jagatud raamatukogusid lokaalselt
- Cookie AutoDelete**: Kustutab küpsised automaatselt pärast vahekaartide sulgemist
- NoScript**: Täielik kontroll JavaScripti täitmise üle (edasijõudnud kasutajad)



Paigaldada:




- Külastage [chrome.google.com/webstore](https://chrome.google.com/webstore) või [addons.mozilla.org](https://addons.mozilla.org)
- Klõpsake "Lisa Chrome'ile/Firefoxile"
- Orion peatab ja installib laienduse automaatselt



**Ohutus**: Kuna laienduste tugi on eksperimentaalne, ei pruugi paljud laiendused korralikult töötada või võivad mõjutada jõudlust. Probleemi korral (sait ei tööta enam, aeglus) lülitage laiendused ükshaaval välja, et tuvastada selle allikas.



## Igapäevane kasutamine



### Interface ja ainulaadsed omadused




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Orioni pintsli menüü ekraani kohandamiseks: kirjasuurus, teema (hele/tume), kleepuvate pealkirjade deaktiveerimine ja häirivate Elements* eemaldamine



**Pintslitööriist: täiustatud kohandamine**



Orioni **pintsli** tööriist on ainulaadne funktsioon, mis võimaldab teil kohandada iga veebisaidi kuvamist:



**Teemavalikud**:




- Vahetage iga saidi jaoks heleda ja tumeda teema vahel
- Automaatne kohandamine teie süsteemi eelistustega



**Tüpograafiline kontroll**:




- Kirjasuurus**: Reguleerige loetavust A- ja A+ nuppude abil
- Kirjastiil**: Muuda kirjatüüpi (vaikimisi või kohandatud)



**Interface puhastamine**:




- Lülita kleepuvad päised**: Eemaldab pealkirjad, mis jäävad kerimisel ülevalt alla kinni
- Kustuta Elements**: Eemaldage lõplikult tüütu Elements (reklaamid, hüpikaknad, küpsiste bännerid)
  - Klõpsake "+ Erase", seejärel valige peidetav objekt
  - Väga kasulik püsivate reklaamide või visuaalse jälgimise Elements saitidel



**Püsivus**: Kõik need seaded salvestatakse domeeni kohta ja neid rakendatakse automaatselt uuesti järgmisel külastusel.



**Täiustatud vahekaartide haldamine**:




- Vertikaalsed vahekaardid**: Aktiveerimine menüüriba kaudu (Tabs on the Side funktsioon)
- Kompaktsed vahekaardid**: Eelistustes → Registrid → paigutus "Kompaktne", et säästa ruumi
- Registrite rühmad**: Korraldage oma seansse teemade kaupa
- Mitu profiili**: Looge eraldi identiteedid menüüriba kaudu (funktsioon "Profiilid") täiesti isoleeritud andmetega



**Low Power Mode**: See iPhone'ist inspireeritud režiim peatab automaatselt mitteaktiivsed vahekaardid pärast 5 minutit ja võib vähendada energiatarbimist kuni 90%. Aktiveerige see Macil Orioni menüüriba kaudu või iOSi seadetes.



**Eesitatud tööriistad** (Redigeerimise menüü ja muud):




- Edit Text on Page**: muuta ajutiselt mis tahes teksti (menüü Edit)
- Luba Copy & Paste**: Ümbersõltub kopeerimispiirangutest (menüü "Edit")
- Kopeeri puhas link**: Jälgimisparameetrite eemaldamiseks klõpsake lingil paremal hiireklõpsuga
- Fookusrežiim**: häireteta, täisekraaniline navigeerimine
- Pilt pildis**: Videote vaatamine hõljuvas aknas
- Avatud Interneti-arhiivis**: Otsene juurdepääs arhiveeritud versioonidele
- Privaatsusaruanne**: Klõpsake kilbil 🛡️, et näha lehekülgede kaupa blokeeritud elemente



### Privaatse sirvimise haldamine



Orioni privaatne navigatsioon (⌘⇧N) pakub:




- Küpsiste ja seansside täielik isoleerimine
- Automaatne kustutamine sulgemisel
- Ajalugu ja vahemälu deaktiveerimine
- Tõhustatud kaitse sõrmejälgede võtmise vastu



**Tipp**: Täpsema jaotuse jaoks looge **eraldi profiilid** menüüriba kaudu (funktsioon Profiilid). Iga profiil kuvatakse Dockis eraldi rakendustena, mille seaded, laiendused ja andmed on täielikult isoleeritud.



### Jõudluse optimeerimine ja privaatsus



Et Orion oleks kiire ja privaatne:




- Laiendused**: Piirake rangelt miinimumini (võib vähendada jõudlust)
- Madala energiatarbimise režiim**: Aktiveeri pikkade seansside jaoks (90% säästu võimalik)
- Privaatsusaruanne**: Klõpsake kilbil 🛡️, et näha blokeeringuid reaalajas
- Visuaalne kohandamine**: Kasutage 🖌️ pintslit, et kohandada ekraani ja eemaldada häiriv Elements
- Kopeeri puhas link**: Ilma jälgimisseadmeteta linkide kopeerimiseks paremklikk
- Eraldi profiilid**: Kasutage oma tegevuse jaotamiseks spetsiaalseid profiile
- Veebisaidi seaded**: Klõpsake hammasratast ⚙️, et kohandada õigusi saidi kaupa
- Regulaarne puhastamine**: Tühjendage vahemälu Orioni kaudu → Tühjendage sirvimisandmed



## Võrdlus alternatiividega



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Versus Safari**: Orion pakub täiustatud blokeerija ja laienduste toega paremat kaitset, säilitades samal ajal WebKiti jõudluse.



**Versus Chrome**: võrratu privaatsus ilma ühilduvust ohustamata, tänu Chrome'i laienduste toetusele.



**Versus Firefox**: Kiirem Macil, Interface intuitiivsem, kuid vähem granuleeritud kontroll ja mitte avatud lähtekoodiga.



**Versus Brave**: Sarnane filosoofia, kuid Orion väldib krüpto/BAT-konflikte ja pakub paremat Apple'i integratsiooni.



## Soovituslikud kasutusjuhud



**Ideaalne**:




- Apple'i kasutajad otsivad rohkem privaatsust kui Safari
- Inimesed, kes soovivad blokeerida kõik reklaamid (sealhulgas YouTube'i) ilma laiendusteta
- Arendajad, kes vajavad WebKit devtools koos integreeritud privaatsuskaitsega
- IPhone'i kasutajad soovivad töölaua laiendusi mobiilis (ainulaadne uuendus)
- Spetsialistid, kes peavad oma tegevusi killustama (mitu profiili)
- Mobiilikasutajad, kes otsivad paremat aku haldamist (Low Power Mode)



**Vältida, kui**:




- Sa kasutad peamiselt Windows/Linuxi (versioon puudub)
- Täielik avatud lähtekood on teie ohumudeli jaoks hädavajalik
- Te sõltute konkreetsetest laiendustest, mis ei pruugi töötada
- Teil on vaja platvormideülest sünkroniseerimist väljaspool Apple'i ökosüsteemi
- Te eelistate tõestatud, stabiilset lahendust (püsiv beeta staatus alates 2021. aastast)



## Tähelepanu ja ohutus



### Ainulaadsed turvaelemendid



**Revolutsiooniline sõrmejälgede vastane kaitse**: Orion on ainus brauser, mis blokeerib täielikult sõrmejälgede skriptide täitmise enne, kui need saavad teie süsteemi skaneerida. See "skripti ei käivitata = sõrmejälgede võtmine ei ole võimalik" lähenemisviis on parem kui teiste brauserite poolt kasutatavad traditsioonilised maskeerimismeetodid.



** Läbipaistev valge nimekiri**: (browserbench.org, wizzair.com), mille blokeerimine on automaatselt välja lülitatud, et vältida tõrkeid. Selline läbipaistvus võimaldab kasutajatel täpselt mõista, millal ja miks blokeeringut leevendatakse.



**Auditeerimata laiendused**: Chrome/Firefoxi laienduste toetamine toob kaasa täiendavaid riske, kuna need laiendused ei ole mõeldud WebKiti jaoks ja neid ei ole spetsiaalselt selle keskkonna jaoks auditeeritud.



### Hooldus ja uuendused





- Automaatsed uuendused**: Orion uuendab macOS-i automaatselt Sparkle'i kaudu
- Haavatavuse jälgimine**: Kontrollida korrapäraselt turvaparanduste kohta käivaid märkusi
- Vigadest teatamine**: Kasutage [orionfeedback.org](https://orionfeedback.org) probleemide teatamiseks




## Kokkuvõte



Orion Browser on märkimisväärne samm edasi privaatsuse tagamisel macOS-is ja iOS-is. Selle telemeetria nullilähedane lähenemine koos ülitõhusa natiivse blokeerija ja unikaalse universaalsete laienduste toetusega teeb sellest suurepärase valiku privaatsustundlikele Apple'i kasutajatele.



**Tähtis**: Orion on alates 2021. aastast püsivas beetaversioonis, mille laienduste ühilduvuse piirangud ja WebKitile omased riskid on olemas. Hinnake neid kompromisse vastavalt oma ohumudelile.



Igapäevaseks kasutamiseks Macis või iPhone'is on see tõenäoliselt parim kompromiss konfidentsiaalsuse, jõudluse ja kasutusmugavuse vahel, mis on Apple'i ökosüsteemis saadaval, tingimusel, et nõustute selle piirangutega.



Pidage meeles: teie privaatsuse kaitsmine ei sõltu ainult teie brauserist. Optimaalse veebiturvalisuse saavutamiseks ühendage Orion parimate tavadega (tugevad paroolid, 2FA, vajadusel VPN).



## Ressursid ja toetus



### Ametlikud dokumendid




- Ametlik veebileht**: [kagi.com/orion](https://kagi.com/orion/)
- Täielik KKK**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Ühenduse foorum**: [community.kagi.com](https://community.kagi.com)
- Vigade jälgimine**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Avatud lähtekoodiga komponendid
- Blogi Kagi**: [blog.kagi.com](https://blog.kagi.com) - Uudised ja uuendused



### Soovitatavad kontrollkatsed



Pärast konfigureerimist testige oma seadistust:




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - sõrmejälgede testimine
- [DNS lekete test](https://www.dnsleaktest.com/) - DNS lekete kontrollimine
- [BrowserLeaks](https://browserleaks.com/) - Täielik privaatsustesti komplekt



### Plan ₿ Network alternatiivid


Maksimaalse kaitse tagamiseks konsulteerige meie teiste juhenditega:




- [Firefox hardened](https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Täiustatud multiplatvormiline konfiguratsioon
- [Tor Browser](https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Täielik võrgu anonüümsus
- [Mullvad Browser](https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Maksimaalne sõrmejälgede kaitse



Kui soovite rohkem teada saada brauserite ajaloost ja toimimisest ning peamistest digitaalsetest objektidest teie igapäevaelus, siis kutsun teid avastama meie uut tasuta koolituskursust SCU 202, mis on saadaval Plan ₿ Network:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
