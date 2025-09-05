---
name: LibreWolf
description: Kuidas kasutada LibreWolfi privaatsusbrauserit
---

![cover](assets/cover.webp)



Iga klõps, iga otsing, iga külastatud veebileht: teie veebilehitsejast on saanud keerukas nuhk, mis toidab ülemaailmset kaubanduslikku jälgimissüsteemi. Google Chrome, mida kasutab üle 3 miljardi inimese, muudab teie igapäevase sirvimise reklaamigigigantide jaoks tulutoovateks andmeteks. Isegi Firefox, vaatamata oma "eetilise" brauseri mainele, aktiveerib vaikimisi telemeetria mehhanismid, mis edastavad teie sirvimisharjumusi Mozillale.



See reaalsus tõstatab olulise küsimuse: kas Internetis on ikka veel võimalik vabalt surfata, ilma et meid pidevalt jälgitaks ja profileeritaks? Õnneks on vastus jaatav, tänu kogukonnaprojektidele, mis seavad kasutaja taas oma murede keskmesse.



LibreWolf kehastab seda digitaalse vastupanu filosoofiat. Sõltumatute arendajate kogukonna mõttetera muudab Firefoxi tõeliseks kaitsekilbiks veebivalve vastu. Seal, kus kaubanduslikud brauserid püüavad teie tähelepanu rahaks teha, teeb LibreWolf vastupidi: teeb teid jälgijatele nähtamatuks, säilitades samal ajal sujuva ja kaasaegse sirvimiskogemuse.



Selles õpetuses avastame, kuidas LibreWolf võib muuta teie veebis surfamise viisi, pakkudes tugevat kaitset jälgimise vastu, ilma et oleks vaja ohverdada jõudlust või veebiühilduvust.



![LIBREWOLF](assets/fr/01.webp)


*Veebibrauserite turuosa: Chrome domineerib 65% turuosaga, järgnevad Safari ja Edge. Selline domineerimine tekitab küsimusi veebi mitmekesisuse ja privaatsuse kohta*



## LibreWolfi tutvustamine



**FreeWolf** on avatud lähtekoodiga veebibrauser, mis on tuletatud Mozilla Firefoxist ning mida arendab ja hooldab vaba tarkvara entusiastide sõltumatu kogukond. Selle peamine eesmärk on pakkuda sirvimist, mis keskendub kasutaja privaatsusele, turvalisusele ja vabadusele.



Konkreetselt öeldes kasutab LibreWolf Firefoxi Gecko mootorit, kuid selle filosoofia erineb radikaalselt: kui Firefox peab tasakaalustama privaatsust ja kasutusmugavust, siis LibreWolf valib vaikimisi privaatsuse. Projekt eemaldab kõik, mis võib teie privaatsust rikkuda (telemetria, andmekogumine, sponsoreeritud moodulid), integreerides samal ajal täiustatud turvasätted.



### Eesmärgid: eraelu puutumatus ja vabadus



LibreWolfi eesmärk on maksimeerida kaitset jälgimise ja sõrmejälgede võtmise vastu, suurendades samal ajal brauseri turvalisust. Selle peamised eesmärgid on järgmised:





- Kõrvaldage Firefoxis kogu telemeetria ja andmete kogumine**
- Lülita välja funktsioonid, mis on vastuolus kasutaja vabadusega**, nagu näiteks patenteeritud DRM-moodulid
- Rakendage algusest peale privaatsus-/turvasätteid** ja konkreetseid parandusi
- Ühenduse areng tagab läbipaistvuse ja sõltumatuse** ärihuvidest



Lühidalt, LibreWolf esitleb end kui "Firefoxi, nagu see oleks olnud, kui privaatsus oleks esmatähtis" - brauser, mis austab teid vaikimisi, ilma et oleks vaja täiendavat seadistamist.



### Peamised omadused



LibreWolf pakub algusest peale mitmeid privaatsusele suunatud funktsioone:



**Ei telemetriat ega andmete kogumist:** Erinevalt Chrome'ist või Firefoxist, mis saadavad teatud kasutusstatistikat, ei kogu LibreWolf teie sirvimisest absoluutselt mitte midagi. Ei mingeid krahhiaruandeid, ei mingeid kasutajauuringuid, ei mingeid sponsoreeritud soovitusi.



**LibreWolf integreerib uBlock Origin laiendust, mis on üks parimaid reklaamiblokeerijaid ja jälgimisseadmeid turul. Vaikimisi filtreerib LibreWolf agressiivselt välja kõik, mis võib teid internetis jälgida (pealetükkivad reklaamid, jälgimisskriptid, krüptoraha Mining).



**Erimuslik otsingumootor:** LibreWolf kasutab vaikimisi DuckDuckGo't kui esialgset otsingumootorit, mis ei säilita teie päringute ajalugu. Teised privaatsusele suunatud alternatiivid (Searx, Qwant, Whoogle) on samuti saadaval.



**Tugevdatud sõrmejälgede kaitse:** sõrmejälgede tuvastamine võimaldab brauseri unikaalset tuvastamist selle konfiguratsiooni kaudu, isegi ilma küpsiste kasutamiseta. Selle vastu võitlemiseks aktiveerib LibreWolf RFP (Resist Fingerprinting) tehnoloogia Tor projektist, et muuta teie brauser võimalikult üldiseks. Testid näitavad, et standardne Firefox on ~90% unikaalne selliste tööriistade puhul nagu coveryourtracks.eff.org, võrreldes ainult ~10-20% LibreWolfi puhul (need arvud on soovituslikud ja võivad varieeruda vastavalt tarkvara ja riistvara konfiguratsioonile ning paigaldatud laiendustele).



![LIBREWOLF](assets/fr/07.webp)


*EFF testleht [Cover Your Tracks](https://coveryourtracks.eff.org/) nupuga TEST YOUR BROWSER. Seda lehekülge kasutatakse jälgimis- ja sõrmejälgede vastase kaitse hindamiseks



![LIBREWOLF](assets/fr/08.webp)


*Cover Your Tracks testi tulemus. Kuvatakse teade "teil on tugev kaitse veebi jälgimise vastu", mis näitab LibreWolf.* kaitse tõhusust



**LibreWolf aktiveerib vaikimisi ranged turvasätted. Firefoxi tõhustatud jälgimiskaitse on viidud rangele tasemele, et blokeerida tuhandeid jälgimisseadmeid, kolmandate osapoolte küpsiseid ja pahatahtlikku sisu. Samuti aktiveerib see saidi ja küpsiste isoleerimise (*Total Cookie Protection*), et jaotada andmed iga domeeni jaoks ning piirab WebRTC-d (piirates *ICE-kandidaate* ja marsruutimist proxy kaudu, kui proxy on olemas), et vähendada IP Address lekke ohtu.



**Siire mootori uuendused:** Projekt jälgib Firefoxi arenguid väga täpselt: LibreWolf põhineb alati Firefoxi viimasel stabiilsel versioonil ja hooldajad püüavad uue versiooni välja anda 24-72 tunni jooksul pärast iga Firefoxi ametliku versiooni ilmumist.



## Eelised ja puudused



### Eelised





- Ei telemetriat ega soovimatuid ühendusi:** LibreWolf ei edasta kasutusandmeid, tagades teie privaatsuse täieliku austamise.





- Avatud lähtekoodiga ja kogukonnapõhine:** Projekt on 100% avatud lähtekoodiga ja seda hooldavad vabatahtlikud. Selline sõltumatus tagab, et ükski reklaamimudel ei mõjuta arengut.





- Eelnevalt konfigureeritud privaatsuse tagamiseks:** LibreWolf säästab teie väärtuslikku aega: pole vaja tunde kulutada Firefoxi seadete karmistamisele, kõik on juba valmis.





- Native ad blocker/tracker:** uBlock Origin on standardselt integreeritud, nii et sa ei pea midagi tegema, et kaitsta end reklaamide ja vigade eest.





- Suurepärane sõrmejälgede vastane kaitse:** Tänu RFP-le ja arvukatele privaatsusseadetele vähendab LibreWolf drastiliselt teie unikaalset digitaalset jalajälge veebis.





- Parem jõudlus ja väiksem kaal:** Telemetria ja teatud mittevajalike funktsioonide eemaldamisega saab LibreWolf olla veidi kiirem ja vähem energiat tarbiv kui tavaline Firefox.



### Puudused ja piirangud





- Sisseehitatud automaatsed uuendused puuduvad:** LibreWolf ei uuenda ennast ise. See on teie ülesanne paigaldada uued versioonid kohe, kui need ilmuvad, et olla turvaline.





- Vähenenud ühilduvus teatud teenustega:** Väga rangete seadete tõttu võib LibreWolfil tekkida probleeme teatud veebilehtedel. Netflix ja Disney+ voogedastusplatvormid ei tööta, kuna LibreWolf lülitab Widevine DRM-i vaikimisi välja.





- Ei ole sisseehitatud anonüümset võrku:** Erinevalt Tor Browserist ei suunata LibreWolf ise liiklust Tori või VPN-i kaudu. Kui vajate võrgu anonüümsust, peate käsitsi konfigureerima proxy/VPN-i.





- Mittepüsivad küpsised ja seansid (vaikimisi):** Konfidentsiaalsuse huvides kustutab LibreWolf küpsised, ajaloo ja saidi andmed iga kord, kui sulgete oma brauseri. Te peate iga kord uuesti oma kontodesse sisse logima.





- Ei ole mobiiliversiooni ega pilves sünkroniseerimist:** LibreWolf on saadaval ainult lauaarvutis (Windows, Linux, macOS). Puudub mobiilirakendus ja seega ka kontode või järjehoidjate sünkroniseerimine pilve kaudu.



## LibreWolfi paigaldamine



**Official website:** [librewolf.net](https://librewolf.net)



LibreWolf on saadaval kõikidele peamistele töölaua operatsioonisüsteemidele: Linux, Windows ja macOS. LibreWolfi allalaadimiseks külastage ametlikku veebisaiti:



![LIBREWOLF](assets/fr/02.webp)


*LibreWolfi koduleht (librewolf.net), millel on brauseri logo, sinine nupp paigaldamiseks ning lähtekoodi ja dokumentatsiooni lingid. Suur sinine nool osutab nupule Install*



Klõpsake nupule "Paigaldamine", et pääseda ligi oma operatsioonisüsteemi üksikasjalikele juhistele:



![LIBREWOLF](assets/fr/03.webp)


*LibreWolf.* operatsioonisüsteemi valikulehekülg allalaadimiseks



Paigaldamine erineb sõltuvalt teie operatsioonisüsteemist:



### Linuxis


LibreWolf pakub koostisi paljudele distributsioonidele. Debian/Ubuntu ja derivaatide puhul on saadaval ametlik APT repositoorium. Alternatiivina on LibreWolf avaldatud Flatpak'is Flathubis:


```
flatpak install flathub io.gitlab.librewolf-community
```



### Windowsis


Laadige paigaldaja (.exe) alla ametlikust veebisaidist või kasutage:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### MacOSis


LibreWolf on saadaval .dmg paketina Macile. Laadige plaadikujutis alla ametlikult veebilehelt ja lohistage LibreWolfi rakendus oma rakenduste kausta. Teise võimalusena saate selle paigaldada Homebrew kaudu.




## Konfigureerimine ja esmakordne kasutamine



Esimesel käivitamisel märkate tuttavat Firefoxi Interface, kuid see on rohkem kärbitud: avalehel on ainult otsinguriba ja puuduvad sponsorisoovitused. Tööriistaribal näete uBlock Origin'i ikooni - märk sellest, et blokeerija on aktiivne.



![LIBREWOLF](assets/fr/04.webp)


*LibreWolfi koduleht koos laienduste ja menüüga. Sinine nool paremas ülemises nurgas näitab menüü ikooni (kolm horisontaalset riba)



LibreWolf laadib teie leheküljed automaatselt "ranges" (jälgimisvastases) režiimis ja vaikimisi otsingumootoriks on DuckDuckGo. Võite proovida külastada jälgimise testsaiti (nt amiunique.org), et jälgida avatud jalajälge - see peaks olema palju üldisem kui tavalise brauseriga.



### Privaatsuse seaded



LibreWolf on juba optimaalselt konfigureeritud privaatsuse tagamiseks. Menüüst → Valikud → Privaatsus ja turvalisus näete, et LibreWolf on seadistatud täiustatud jälgimiskaitse režiimi: Strict. See režiim blokeerib:




- Saitidevahelised jälgimisseadmed
- Kolmanda osapoole küpsised
- Tuntud jälgimise sisu
- Cryptomining
- Digitaalsed sõrmejälgede detektorid



![LIBREWOLF](assets/fr/05.webp)


*LibreWolf.* turvasätteid näitav vahekaart Turvalisus ja privaatsus



WebRTC on välja lülitatud (IP-lekete vältimiseks) ja küpsiste täielik kaitse on sisse lülitatud. Telemetria ja Firefoxi küsitlused on täielikult välja lülitatud.



### Küpsiste ja ajaloo haldamine



Vaikimisi kustutab LibreWolf küpsised ja kohaliku salvestusruumi iga kord sulgemisel. Kui see käitumine häirib teid, saate seda seadistada jaotises Privaatsus ja turvalisus → Küpsised ja saidi andmed, eemaldades märkuse "Kustuta küpsised ja saidi andmed LibreWolfi sulgemisel".



![LIBREWOLF](assets/fr/06.webp)


*Sama lehekülg veidi allapoole, näidates võimalust küpsiste kustutamiseks, kui brauser on suletud*



### Kasulike laienduste lisamine



Põhimõtteliselt ei soovita LibreWolfis mittevajalike laienduste lisamist, kuna iga laiendus võib olla jälgimisvektor. Sellegipoolest võivad mõned mainekad laiendused teie kasutuskogemust parandada:




- Firefox Multi-Account Containers** (Mozilla poolt) jaotatud sirvimise jaoks
- Decentralyes** või **LocalCDN** ühiste raamatukogude kohalikuks teenindamiseks



Eriti vältige "tasuta VPN-i" laiendusi või kahtlasi proxysid - uBlock Origin katab juba 99% teie vajadustest.



## Igapäevane kasutamine



### Igapäevane veebi sirvimine


Kasutage LibreWolfi oma igapäevaseks internetitegevuseks. Peamine erinevus võrreldes teiste brauseritega on see, et te jätate palju vähem reklaami jälgi. Tänu uBlocki filtreerimisnimekirjadele kaovad paljudel saitidel "küpsiste vastuvõtmine" bännerid.



### Kasutage eraviisilisi vahekaarte, et jaotada


Kuigi LibreWolf kustutab kõik sessiooni lõpus, võib olla kasulik avada privaatne brauseriaken (Ctrl+Shift+P) teatud ülesannete jaoks sessiooni ajal, et eraldada konkreetne identiteet.



### Kasutage ära mitme konto konteinereid


Multi-Account Containers laienduse paigaldamine aitab teil oluliselt segmenteerida oma tegevusi veekindlatesse silodesse. Näiteks saate määratleda konteineri "Banking" oma pangasaitide jaoks, konteineri "Social Networks" Facebooki/Twitteri jaoks jne. Igal konteineril on oma küpsised, seansid ja isoleeritud salvestusruumid. Igal konteineril on oma küpsised, seansid ja isoleeritud salvestusruumid.



### Saitide kaupa täpsustatud õiguste haldamine


LibreWolf võimaldab teil kontrollida saitidele antud õigusi (asukoht, kaamera, mikrofon, teavitused) juhtumipõhiselt. Andke õigusi ainult nendele saitidele, mida te usaldate ja kus see on vajalik.



## Parimad tavad LibreWolfiga



1. **Hoidke LibreWolfi ajakohasena:** Kontrollige saidilt regulaarselt uusi versioone, eriti pärast stabiilset Firefoxi väljalaskmist.



2. **Vältige isikliku identiteedi ja privaatse sirvimise segunemist:** Ideaaljuhul ei tohiks te sisse logida oma isiklike kontodega samal seansil, kus teete tundlikku uurimistööd.



3. ** Ärge koormake LibreWolfi üle üleliigsete laiendustega:** Iga paigaldatud laiendus võib tekitada turvariske või sõrmejälgi.



4. **Kasutage lisaks VPN-i või Tor proxy'd:** LibreWolf ei tee teid ISP jaoks anonüümseks. Võrgu anonüümsuse tagamiseks võite kasutada LibreWolfi usaldusväärse VPN-i taga.



5. **Säästke oma olulised andmed:** järjehoidjad, paroolid, kui need on salvestatud lokaalselt. Kaaluge pigem välist paroolihaldurit (KeePassXC, Bitwarden) kui brauseri põhilist paroolihaldurit.



## Võrdlus teiste brauseritega



LibreWolf on osa privaatsusele orienteeritud brauserite "tööriistakastist":



**LibreWolf vs. Firefox:** LibreWolf saabub juba karastatud ja ilma igasuguse telemeetriata. Firefoxi eeliseks on endiselt mitme seadmega sünkroniseerimine ja väga suur kasutajaskond, kuid LibreWolfi konfidentsiaalsuse taseme saavutamiseks on vaja käsitsi konfigureerida.



**Brave kasutab Chrome/Chromium koodi ja integreerib ärimudeli oma vabatahtliku reklaamiprogrammi kaudu. LibreWolf, olles Firefoxi kogukonna Fork, säilitab Mozilla vaba ökosüsteemi ja ei ole seotud Google'iga.



**LibreWolf vs Tor Browser:** Tor Browser on asendamatu anonüümsuse tagamiseks võimsa jälgimise ees, kuid see on aeglane ja ebamugav igapäevases kasutuses. LibreWolf on klassikalise veebi igapäevaseks sirvimiseks palju kiirem ja praktilisem.



**LibreWolf vs Mullvad Browser:** Mullvad Browser läheb standardiseerimise osas veelgi kaugemale, kuid selle arvelt väheneb kasutusmugavus (sisselogimisküpsise säilitamine on võimatu). LibreWolf saavutab tasakaalu: väga privaatne, kuid igapäevaselt kasutatav.



## Kokkuvõte



LibreWolf on suurepärane lahendus neile, kes otsivad ülimalt privaatset "igapäevast" brauserit, ilma et nad läheksid nii kaugele kui Tor'i äärmine anonüümsus. See on ideaalne valik aktivistidele, ajakirjanikele, arendajatele või võimekatele kasutajatele, kes soovivad klassikalist veebilehitsemist (kiire, ühilduv kaasaegsete saitidega), kuid samas põgenevad reklaami jälgimise ja Big Techi eest.



Kuigi sellel on teatud piirangud (puuduvad automaatsed uuendused, vähene ühilduvus teatud teenustega), on LibreWolf väärtuslik vahend kõigi nende arsenalis, kes soovivad taastada kontrolli oma digitaalse privaatsuse üle. Selle kasutusmugavus ja vaikimisi konfiguratsioon muudavad selle tarkaks valikuks privaatsust teadvustavatele kasutajatele.



## Ressursid



### Ametlikud dokumendid




- [LibreWolf ametlikul kodulehel](https://librewolf.net)
- [lähtekood Codebergil](https://codeberg.org/librewolf)
- [Ametlik KKK](https://librewolf.net/docs/faq)



### Juhendid ja võrdlused




- [Privaatsusjuhised](https://www.privacyguides.org/en/desktop-browsers/)
- [Võrdlevad privaatsust testid](https://privacytests.org)



### Ühenduse toetus




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)