---
name: Mullvad Browser
description: Kuidas kasutada Mullvad Browser'i privaatsuse tagamiseks
---

![cover](assets/cover.webp)



Maailmas, kus digitaalne jälgimine on muutumas igapäevaeluks, ei ole eraelu puutumatuse kaitsmine internetis kunagi varem olnud nii oluline. Ettevõtted kasutavad teie jälgimiseks keerulisi meetodeid:





- Kolmanda osapoole küpsised**: väikesed failid, mida välised saidid hoiavad, et teid ühelt saidilt teisele jälgida
- Sõrmejälg**: kogub teie brauseri ja seadme unikaalseid omadusi (ekraani resolutsioon, paigaldatud fondid, pluginad jne), et teid ilma küpsisteta tuvastada
- Jälgimisskriptid**: nähtamatud JavaScript-koodid, mis analüüsivad teie sirvimiskäitumist (klõpsud, kerimine, ajakulu)
- IP Address analüüs**: geograafiline asukoht ja teie Interneti-teenuse pakkuja tuvastamine



Seejärel kombineeritakse need andmed, et luua üksikasjalikud profiilid teie veebikäitumise kohta, ning neid kasutatakse rahaks, sageli teie teadmata. See tõstatab põhiküsimuse: kuidas saab internetis surfata, säilitades samal ajal oma anonüümsuse ja konfidentsiaalsuse?



Vastus peitub suuresti teie valitud veebilehitsejas. See vahend, mida me iga päev kasutame teabele juurdepääsuks, ostude tegemiseks või suhtlemiseks, mängib otsustavat rolli meie isikuandmete kaitsmisel. Kahjuks on populaarsed veebilehitsejad, nagu Google Chrome (mis omab umbes 65% maailmaturust), loodud ärimudelitele, mis põhinevad kasutajate andmete massilisel kogumisel.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser paistab silma erakordselt tõhusa jälgimisseadmete blokeerimise poolest, mis ületab kaugelt tarbijate brauserid*



Selle väljakutsega silmitsi seistes on esile kerkimas uued tegijad, kellel on teistsugune filosoofia: nad seavad eraelu puutumatuse oma disaini keskmesse. Mullvad Browser paistab nende seast silma kui uuenduslik lahendus, mis ühendab parima privaatsuskaitse sujuva ja kättesaadava sirvimiskogemusega.



Erinevalt traditsioonilistest brauseritest, mis püüavad teie andmete kogumise abil teie kasutuskogemust isikupärastada, kasutab Mullvad Browser vastupidist lähenemist: muudab kõik selle kasutajad veebilehtedel identseks, muutes seega individuaalse jälgimise praktiliselt võimatuks.



Selles õpetuses avastame koos, kuidas Mullvad Browser võib muuta teie Interneti-levimise viisi, pakkudes teile tugevat kaitset jälgimise eest, ilma et see kaotaks kasutusmugavuse.




## Mullvad Browser'i tutvustamine



**Mullvad Browser** on privaatsusele keskendunud veebibrauser, mis on välja töötatud koostöös Tor Projectiga ja mida levitab tasuta Rootsi ettevõte Mullvad VPN. See 2023. aasta aprillis käivitatud brauser on **"Tor Browser ilma Tor-võrguta "**, mis on loodud selleks, et minimeerida veebipõhist jälgimist ja sõrmejälgede võtmist, võimaldades kasutajatel sirvida pigem usaldusväärse VPN-i kui Tor-võrgu kaudu.



Mullvad Browser on tasuta, avatud lähtekoodiga brauser, mis põhineb Firefox ESR-il (Mozilla Firefoxi pikaajaline versioon) ja mida Tor Projecti eksperdid on karastanud. Konkreetselt öeldes sisaldab ta enamikku **kaitsefunktsioone Tor Browserist**, kuid **ei suunata liiklust Tor-võrgu kaudu**. Selle asemel saavad (ja peaksid) kasutajad selle siduda usaldusväärse krüpteeritud VPN-iga, et anonüümseks muuta oma IP Address.



Kasutajakogemuse poolest meenutab Mullvad Browser klassikalist brauserit, pakkudes sujuvat navigeerimist. See on tasuta saadaval Windowsis, macOSis ja Linuxis (mobiiliversioon puudub). Selle kasutamiseks ei pea olema Mullvad VPN-i tellija; siiski **Mullvad Browser'i kasutamine ilma IP-d maskeerimata ei taga täielikku anonüümsust** - seega on väga soovitatav kasutada seda koos usaldusväärse VPN-iga.



### Eesmärgid: privaatsus ja jälgimisvastane võitlus



Mullvad brauseri väljatöötamisel on silmas peetud ühte peamist eesmärki: **kasutaja privaatsuse kaitsmine** internetis ja vastase võitlemine levinud jälgimis- ja profileerimismeetodite vastu. Selle peamised eesmärgid on järgmised:





- Vähendage järsult reklaami jälgimist ja jälgimist** veebisaitide ja reklaamiagentuuride poolt. Mullvad Browser blokeerib vaikimisi kolmandate osapoolte jälgimisseadmed, jälgimisküpsised ja sõrmejälje skriptid, mis võivad teid tuvastada.





- Standardiseerige oma brauseri sõrmejälg**, et **"sulanduda rahva hulka "**. Sõrmejälg on nagu unikaalne "isikutunnistus", mis on loodud teie brauseri kõigi omaduste kombineerimisel. Mullvad Browser tagab, et kõigil kasutajatel on täpselt sama "isikutunnistus", mistõttu on võimatu neid individuaalselt eristada.





- Pakub kohest kaitset ilma täiendavate pikendusteta**. Mullvad Browser on "kasutusvalmis" konfiguratsiooniga: kasutaja ei pea paigaldama hulgaliselt laiendusi ega muutma mingeid seadistusi, et olla kaitstud.





- Ärge ohverdage jõudlust või ergonoomikat** rohkem kui vaja. Tori marsruutimise puudumisel pakub Mullvad Browser palju kiiremat sirvimist kui Tor Browser, lähenedes tavalise brauseri jõudlusele koos VPN-iga.



### Mullvad Browser'i peamised funktsioonid



Mullvad Browser sisaldab mitmeid **turbe- ja privaatsusfunktsioone**, mis on otseselt inspireeritud Tor Browserist:





- Privaatne sirvimine kogu aeg:** Privaatne sirvimisrežiim on vaikimisi aktiveeritud ja seda ei saa deaktiveerida. **Es ei salvestata ajalugu, küpsiseid ega vahemälu ühest seansist teise**. Niipea, kui sulgete Mullvad Browser'i, kustutatakse kõik sirvimisandmed.





- Tõhustatud kaitse sõrmejälgede võtmise vastu:** Brauser rakendab rangeid seadistusi, et takistada digitaalset sõrmejälgede võtmist. See hõlmab järgmist:
 - Kasutajaagendi** ja brauseri versiooni standardimine
 - Kõigi kasutajate ajavööndiks on seatud UTC**
 - Letterboxing**: tehnika, mis lisab automaatselt hallid marginaalid veebilehtede ümber, et ühtlustada ekraanisuurust ja vältida tuvastamist ekraani mõõtmete järgi
 - Blokeeritud sõrmejälgede APId**: Canvas (2D joonistamine), WebGL (3D graafika) ja AudioContext (helitöötlus) tehnoloogiad on keelatud, sest need võivad avaldada unikaalseid üksikasju teie riistvara kohta
 - Standardiseeritud süsteemifontid**, et vältida tuvastamist paigaldatud fontide järgi





- Jälgijate ja reklaami blokeerimine:** Mullvad Browser integreerib algselt **uBlock Origin** laienduse (eelinstallitud) koos täiendavate kaitselistidega, et blokeerida **kolmandate osapoolte jälgijad, reklaamskriptid ja muu pahatahtlik sisu**. Selle kaitsega kaasneb **Esimesi isoleerimine**: tehnika, mis salvestab küpsised iga veebisaidi jaoks eraldi "pottidesse", mis takistab ühel veebisaidil lugeda teise saidi poolt hoiustatud küpsiseid.





- Seansi lähtestamise nupp:** Sarnaselt Tor Brauseri nupuga "Uus identiteet" pakub Mullvad Browser nuppu, mille abil saab **suurelt taaskäivitada brauseri uue, tühja seansiga**.





- Reguleeritavad turvatasemed:** Saate seadetes reguleerida turvataset (*Normaalne*, *Safer*, *Safest*), nagu ka Tor Browseris.



## Sisseehitatud laiendused vaikimisi



Mullvad Browser sisaldab **kolme eelinstalleeritud laiendust**, mis moodustavad selle jälgimisvastase kaitse tuuma. **Et tohi neid kunagi eemaldada või nende konfiguratsioone muuta**, sest see muudaks teid Mullvad Browser'i kasutajate seas ainulaadseks:



### **uBlock Origin**


See reklaami- ja jälgimisblokeerija laiendus on eelnevalt konfigureeritud **optimeeritud filtrite nimekirjadega**, et blokeerida:




- Pealetükkiv reklaam
- Kolmanda osapoole jälgimisseadmed, mis koguvad teie andmeid
- Pahatahtlikud skriptid
- Käitumise jälgimine Elements



uBlock Origin Mullvad Browseris kasutab standardiseeritud parameetreid, et tagada, et kõik kasutajad blokeerivad täpselt sama Elements, säilitades seega digitaalsete jalajälgede ühtsuse.



### **NoScript**


NoScript töötab taustal, et hallata brauseri **turvalisuse taset**. See:




- Kontrollib JavaScripti** täitmist vastavalt valitud tasemele (normaalne/ kõige turvalisem/ kõige turvalisem)
- Filtreerib XSS** (Cross-Site Scripting) rünnakud automaatselt välja
- Blokeerib ohtliku** aktiivse sisu mitte-HTTPS-saitidel
- Selle ikoon on vaikimisi peidetud, kuid seda saab kuvada "Tööriistariba kohandamise" kaudu



### **Mullvad Browser** laiendus


See Mullvad-spetsiifiline laiendus pakub erinevaid funktsioone sõltuvalt sellest, kas olete Mullvad VPN-i klient või mitte:



#### **Kui Mullvad VPN tellimus:**




- Põhiline ühenduse kontroll**: näitab teie praegust avalikku IP-aadressi ja mõningaid andmeid ühenduse kohta
- Privaatsussoovitused**: näpunäited turvasätete parandamiseks (DNS, ainult HTTPS, otsingumootor)
- WebRTC** kontroll: IP Address lekete vältimiseks lubada/välja lülitada
- Saab kustutada ilma mõju** teie digitaalsele jalajäljele, kui te ei kasuta Mullvad VPN-i



#### **Mullvad VPN-i tellimisega:**


Laiendus avab oma täieliku potentsiaali koos täiustatud funktsioonidega:





- Integreeritud SOCKS5 proxy**: ühe klõpsuga ühendus Mullvad VPN serveri proxy'ga
 - Fikseeritud IP Address**: erinevalt VPN-st, mis võib muuta oma IP Address, tagab proxy alati sama väljund Address
 - Automaatne kill switch**: kui VPN katkestab ühenduse, blokeeritakse brauseri liiklus koheselt
 - IPv6 tugi**: IPv6 ühenduvus isegi siis, kui teie VPN-ühendus ei ole lubatud





- Multihop (topelt VPN)**: võimalus muuta proxy asukohta, et luua tunneli sees tunneli
 - Teie liiklus läbib kõigepealt teie VPN-serveri, seejärel "hüppab" teise Mullvadi serverisse
 - Kasutage erinevat lokaliseerimist ainult brauseri jaoks





- Täiustatud ühenduse seire**: VPN-i oleku, ühendatud serveri ja DNS-lekke tuvastamine reaalajas





- Juurdepääs Mullvad Leta**: privaatne otsingumootor, mis on reserveeritud tellijatele (kuigi Mullvad ei soovita seda oma kontoga korrelatsiooni tõttu)



Need kolm laiendust töötavad koos, et luua ühtne kaitse ökosüsteem, kus iga kasutaja saab kasu täpselt samadest kaitsemeetmetest ilma kohandamisvõimaluseta, mis kahjustaks kollektiivset anonüümsust.



## Mullvad Browser'i eelised ja puudused



### Eelised





- Suurepärane privaatsuskaitse vaikimisi:** Mullvad Browser rakendab algusest peale väga rangeid privaatsusseadeid, ilma et oleks vaja käsitsi konfigureerida.





- Parem jõudlus kui Tor Browser:** Onioni marsruutimise puudumisel on Mullvad Browser klassikalise veebi sirvimise puhul **nähtavalt kiirem ja reageerimisvõimelisem** kui Tor Browser.





- Tuttav Interface lihtsus:** Mullvad Browser põhineb Firefoxi Interface-l. Kui olete harjunud Firefoxi või isegi Tor Browseriga, siis ei tunne te end kohatuna.





- Usaldusväärne koostöö ja auditeeritud kood:** Mullvad Browser saab kasu Tor Projecti kogemustest ja kogu lähtekood on kättesaadav välisauditiks.



### Puudused





- Ilma VPN-ita ei ole võrgu anonüümsust:** Kõige olulisem on see, et **Mullvad Browser ei peida oma IP Address ise** (nagu kõik teised brauserid, välja arvatud Tor Browser). Teie IP Address on nagu teie "posti Address" internetis: see paljastab teie asukoha ja teie Interneti-teenusepakkuja. Seetõttu sõltub see **suures osas VPNist** (virtuaalne privaatvõrk), et seda olulist teavet varjata.





- Mobiiliversioon puudub:** Praeguseks on Mullvad Browser saadaval ainult PC-l (Windows, Mac, Linux).





- Ei ühildu teatud harjumustega:** **püsiv privaatne režiim** tähendab, et seanssi ei saa hoida ühest kasutusest teise. Veebikontoga ei ole võimalik jääda ühest seansist teise ühendatud.





- Piiratud funktsioonid:** Et säilitada sõrmejälgede ühtsust, on Mullvad Browseris **keelatud mitmed Firefoxis olevad funktsioonid** ja need ei ole mõeldud kohandamiseks.



## Mullvad Browser'i paigaldamine



Mullvad Browser on saadaval tasuta Windowsile, macOSile ja Linuxile. Selle installimiseks minge [Mullvadi ametlikule veebisaidile](https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Mullvad Brauseri ametlik koduleht koos allalaadimisnupuga, mis on esile tõstetud.*



![MULLVAD BROWSER](assets/fr/03.webp)



*Valige oma operatsioonisüsteem Mullvad Browser.* allalaadimise lehel



Klõpsake oma operatsioonisüsteemile vastaval nupul **"Download "**.



Linuxi puhul saate valida erinevate vormingute vahel sõltuvalt teie distributsioonist. Kui allalaadimine on lõpetatud:



### Windowsis


Käivitage allalaaditud .exe fail ja järgige paigaldusjuhiseid.



### MacOSis


Avage allalaetud `.dmg` fail ja lohistage rakendus Mullvad Browser oma rakenduste kausta.



### Linuxis


Kaevake arhiiv `.tar.xz` oma valitud kataloogi ja käivitage fail `start-mullvad-browser.desktop`.



## Konfigureerimine ja esmakordne kasutamine



Kui käivitate Mullvad Browser'i esimest korda, näete Interface, mis on väga sarnane Tor Browser'ile. Brauser on privaatsuse jaoks eelkonfigureeritud ja ei vaja mingeid erimuudatusi.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Mullvad Brauseri avaleht koos laiendustega, luudade ikoon generate uue identiteedi ja rakenduse menüüga üleval paremal.*



**Tähtis:** Mullvad Browser ei maskeeri vaikimisi teie IP Address. Täieliku kaitse tagamiseks soovitame tungivalt kasutada paralleelselt VPN-i. Võite kasutada Mullvad VPN-i või mõnda muud usaldusväärset VPN-teenust.



Brauser sisaldab ka **DNS-over-HTTPS (DoH)**, mis kasutab Mullvadi DNS-teenust: see tehnoloogia krüpteerib teie DNS-päringud (saitide nimede tõlkimine IP-aadressideks), et teie Interneti-teenuse pakkuja ei saaks teie külastatud saite jälgida.



### Ohutusseaded



Turvalisuse taset saate reguleerida, klõpsates paremal üleval **rakenduse menüüs** (kolm horisontaalset riba), seejärel **"Seaded "** ja seejärel vahekaardil **"Privaatsus ja turvalisus "**. Kerige alla jaotisele **"Turvalisus "**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Turvatasemete valik: nooled näitavad teed rakenduse menüüst vahekaardile "Privaatsus ja turvalisus", kus on turvavalikud*



Mullvad Browser pakub kolme turvataset:





- Normaalne** (praegune vaikimisi tase): Kõik brauseri ja veebisaidi funktsioonid on lubatud





- Turvalisem**: Lülitab välja sageli ohtlikud veebisaitide funktsioonid, mis võivad viia mõne veebisaidi funktsionaalsuse kadumiseni:
 - JavaScript on keelatud mitte-HTTPS-saitidel
 - Mõned kirjatüübid ja matemaatilised sümbolid on välja lülitatud
 - Heli ja video (HTML5 meedia) ning WebGL on "kliki mängimiseks"





- Kõige ohutum**: Võimaldab ainult staatiliste veebilehtede ja põhiteenuste jaoks vajalikke veebisaitide funktsioone:
 - JavaScript on vaikimisi kõigi saitide puhul välja lülitatud
 - Mõned kirjatüübid, ikoonid, pildid ja matemaatilised sümbolid on välja lülitatud
 - Heli ja video (HTML5 meedia) ning WebGL on "kliki mängimiseks"



### Uue seansi nupp



Tühja seansiga taaskäivitamiseks ilma brauserit sulgemata klõpsake luuda ikoonil või kasutage rakenduse menüüd > **"Uus seanss "**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Funktsioon "Identiteedi lähtestamine", et taaskäivitada brauser täiesti uue seansiga*



## Igapäevane kasutamine



### Tavaline navigeerimine



Mullvad Browser käitub nagu klassikaline brauser igapäevaseks sirvimiseks. Kõik veebilehed on kättesaadavad nagu tavaliselt, kuid lisaväärtuseks on täiustatud kaitse jälgimise vastu.



### Küpsiste haldamine ja sisselogimine



Püsiva privaatse režiimi tõttu peate oma kontodega iga kord uuesti ühenduma, kui logite sisse. See on hind, mida maksate maksimaalse konfidentsiaalsuse eest.



### Laiendused



Mullvad Browser võimaldab tehniliselt paigaldada täiendavaid laiendusi Firefoxi kataloogist, kuid **on oluline mõista selle mõju**. Iga lisatud laiendus muudab teie digitaalset jalajälge ja eristab teid teistest Mullvad Brauseri kasutajatest, mis on vastuolus brauseri põhiprintsiibiga: kõik kasutajad peavad olema identsed.



Nagu Mullvad selgitab: *"Mõnikord on parem, kui puudub konkreetne kaitse, kui on üks. Soovides suurendada privaatsust internetis, paigaldate laiendusi, mis lõppkokkuvõttes muudavad teid veelgi nähtavamaks. "*



Kui otsustate siiski laiendusi paigaldada, olge teadlik, et loote unikaalse sõrmejälje, mida saab kasutada teie jälgimiseks veebisaitide vahel. Maksimaalse kaitse tagamiseks on kõige parem jääda kolme eelinstalleeritud laienduse juurde, mis on kõigile kasutajatele identsed.



## Parimad tavad Mullvad Browseriga



1. **Kasutage alati VPN-i: Mullvad Browser ei maskeeri teie IP-aadressi. VPN on täielikuks anonüümsuseks hädavajalik.



2. **Mitte kohandage brauserit**: Vältige seadete muutmist või laienduste lisamist, sest see võib teid identifitseeritavaks muuta.



3. **Kasutage uue seansi nuppu**: Erinevate tegevuste vahel kasutage seansside jaotamiseks nullimisfunktsiooni.



4. **Valige oma vajadustele kõige paremini vastav turvatase**:




   - Normaalne (soovitatav)**: Igapäevaseks sirvimiseks. Pakub juba praegu suurepärast kaitset, säilitades samal ajal veebisaitide funktsionaalsuse. See on parim tasakaal 95% kasutajate jaoks.
   - Turvalisem**: Kui külastate tundmatuid või potentsiaalselt ohtlikke saite või kui soovite täiendavat kaitset avalikes WiFi-võrkudes. Mõne saidi puhul võib esineda tõrkeid.
   - Kõige turvalisem**: Reserveeritud kõrge riskiga olukordade jaoks (uuriv ajakirjandus, tundlik side, vaenulikud keskkonnad). Enamik moodsaid saite läheb katki, kuid see on maksimaalse turvalisuse hind.



5. **Regulaarselt kontrollige uuendusi**: Hoidke oma brauseri ajakohasena koos viimaste turvaparandustega.



6. **Kasutage privaatsussõbralikke otsingumootoreid**: Google'i asemel valige DuckDuckGo, Startpage või Searx.



7. **Võimaldab ainult HTTPS-režiimi**: Veenduge, et seadetes on turvaliste ühenduste sundimiseks sisse lülitatud režiim "Ainult HTTPS".



8. **Mitte muutke ühtegi täiustatud seadistust**: Erinevalt teistest brauseritest on Mullvad Browser loodud nii, et KÕIGIL kasutajatel on täpselt sama konfiguratsioon. Seadete muutmine `about:config`is või uBlock Origin/NoScript-seadete muutmine muudaks teid unikaalseks ja muudaks brauseri anonüümsuse täielikult olematuks.



## Soovitatav DNS-konfiguratsioon



Mullvad Browser integreerib automaatselt Mullvad DNS-over-HTTPS. Kui kasutate Mullvad VPN-i, soovitab laiendus teil **välja lülitada Mullvad DoH**, kuna on kiirem kasutada oma VPN-serveri DNS-serverit. Kui te ei kasuta Mullvad VPN-i, jätke Mullvad DoH sisse lülitatud, et vältida DNS-i jälgimist teie Interneti-teenuse pakkuja poolt.



## Kokkuvõte



Mullvad Browser on suurepärane lahendus neile, kes otsivad privaatsussõbralikku veebilehitsemist ilma Tor-võrgu jõudluspiiranguteta. Koos kvaliteetse VPN-iga pakub see tugevat kaitset veebipõhise jälgimise ja jälgimise eest.



Kuigi sellel on teatud piirangud (puudub mobiiliversioon, mittepüsivad seansid), on Mullvad Browser väärtuslik vahend kõigi nende arsenalis, kes soovivad oma digitaalse privaatsuse üle kontrolli taastada. Selle kasutusmugavus ja vaikimisi konfiguratsioon teevad sellest targa valiku privaatsust teadvustavatele kasutajatele, olgu need siis algajad või kogenud kasutajad.



## Ressursid



### Ametlikud dokumendid




- [Mullvad Browser'i ametlik veebileht](https://mullvad.net/fr/browser)
- [Mullvad Brauseri allalaadimisleht](https://mullvad.net/en/download/browser)
- [Üksikasjalikud tehnilised näitajad](https://mullvad.net/en/browser/Hard-facts)
- [Mullvad Browser Extension](https://mullvad.net/en/help/mullvad-browser-extension)



### Juhendid ja selgitused




- [Miks privaatsus on oluline](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor ilma Torita: Mullvad Browser kontseptsioon](https://mullvad.net/en/browser/tor-without-tor)
- [Kuidas valida privaatsussõbralik veebilehitseja](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Brauseri sõrmejälgede mõistmine](https://mullvad.net/en/browser/browser-fingerprinting)



### Toetus ja abi




- [Mullvad Browser Help Center](https://mullvad.net/en/help/tag/mullvad-browser)
- [Esimesed sammud privaatsuse tagamiseks internetis](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Ühenduse ressursid




- [Mullvad Browser Guide - Privaatsusjuhised](https://www.privacyguides.org/en/desktop-browsers/)
- [Ühenduse arutelud](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)