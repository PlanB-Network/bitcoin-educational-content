---
name: LibreWolf
description: Hoe de LibreWolf privacy-browser te gebruiken
---

![cover](assets/cover.webp)



Elke klik, elke zoekopdracht, elke bezochte site: uw webbrowser is een geavanceerde verklikker geworden die een wereldwijd commercieel bewakingssysteem voedt. Google Chrome, dat door meer dan 3 miljard mensen wordt gebruikt, zet je dagelijkse surfgedrag om in lucratieve gegevens voor de reclamereuzen. Zelfs Firefox, ondanks zijn reputatie als "ethische" browser, activeert standaard telemetriemechanismen die je surfgedrag doorgeven aan Mozilla.



Deze realiteit roept een essentiële vraag op: is het nog mogelijk om vrij op het internet te surfen zonder voortdurend bespioneerd en geprofileerd te worden? Gelukkig is het antwoord ja, dankzij gemeenschapsprojecten die de gebruiker weer centraal stellen.



LibreWolf belichaamt deze filosofie van digitaal verzet. Als geesteskind van een gemeenschap van onafhankelijke ontwikkelaars verandert deze browser Firefox in een echt schild tegen online toezicht. Waar commerciële browsers geld proberen te verdienen aan uw aandacht, doet LibreWolf het tegenovergestelde: u onzichtbaar maken voor trackers terwijl u een vloeiende, moderne browse-ervaring behoudt.



In deze tutorial ontdekken we hoe LibreWolf de manier waarop je op het web surft kan veranderen, door robuuste bescherming tegen tracking te bieden zonder aan prestaties of webcompatibiliteit in te boeten.



![LIBREWOLF](assets/fr/01.webp)


*Marktaandeel webbrowsers: Chrome domineert met 65% van de markt, gevolgd door Safari en Edge. Deze dominantie roept vragen op over webdiversiteit en privacy*



## Even voorstellen: LibreWolf



**FreeWolf** is een open-source webbrowser afgeleid van Mozilla Firefox, ontwikkeld en onderhouden door een onafhankelijke gemeenschap van liefhebbers van vrije software. Het belangrijkste doel is om browsen aan te bieden die gericht zijn op privacy, veiligheid en vrijheid van de gebruiker.



Concreet gebruikt LibreWolf de Gecko-engine van Firefox, maar met een radicaal andere filosofie: waar Firefox een evenwicht moet vinden tussen privacy en gebruiksgemak, kiest LibreWolf standaard voor privacy. Het project verwijdert alles wat inbreuk zou kunnen maken op je privacy (telemetrie, gegevensverzameling, gesponsorde modules) terwijl het verbeterde beveiligingsinstellingen integreert.



### Doelstellingen: privacy en vrijheid



LibreWolf heeft als doel de bescherming tegen tracking en fingerprinting te maximaliseren en tegelijkertijd de browserbeveiliging te verbeteren. De belangrijkste doelstellingen zijn:





- Alle telemetrie en gegevensverzameling** in Firefox elimineren
- Functies uitschakelen die indruisen tegen de vrijheid van de gebruiker**, zoals propriëtaire DRM-modules
- Privacy-/beveiligingsinstellingen** en specifieke patches vanaf het begin toepassen
- Gemeenschapsontwikkeling garandeert transparantie en onafhankelijkheid** van commerciële belangen



Kortom, LibreWolf presenteert zichzelf als "Firefox zoals het zou zijn geweest als privacy de hoogste prioriteit had" - een browser die je standaard respecteert, zonder dat er extra configuratie nodig is.



### Belangrijkste kenmerken



LibreWolf biedt vanaf het begin een reeks privacy-georiënteerde functies:



**Geen telemetrie of gegevensverzameling:** In tegenstelling tot Chrome of Firefox, die bepaalde gebruiksstatistieken verzenden, verzamelt LibreWolf helemaal niets van uw browsen. Geen crashrapporten, geen gebruikersonderzoeken, geen gesponsorde suggesties.



**LibreWolf integreert de uBlock Origin extensie, een van de beste ad blockers en trackers op de markt. Standaard filtert LibreWolf agressief alles wat je online zou kunnen volgen (opdringerige advertenties, tracking scripts, cryptocurrency Mining).



**Standaard privé-zoekmachine:** LibreWolf gebruikt standaard DuckDuckGo als eerste zoekmachine, die geen geschiedenis van je zoekopdrachten bijhoudt. Andere privacy-georiënteerde alternatieven (Searx, Qwant, Whoogle) zijn ook beschikbaar.



**Versterkte bescherming tegen vingerafdrukken:** Door vingerafdrukken kan een browser uniek worden geïdentificeerd via zijn configuratie, zelfs zonder cookies. Om dit tegen te gaan, activeert LibreWolf RFP-technologie (Resist Fingerprinting) van het Tor-project, om je browser zo generiek mogelijk te maken. Tests tonen aan dat een standaard Firefox ~90% uniek is op tools zoals coveryourtracks.eff.org, vergeleken met slechts ~10-20% voor LibreWolf (deze cijfers zijn indicatief en kunnen variëren afhankelijk van software- en hardwareconfiguratie en geïnstalleerde extensies).



![LIBREWOLF](assets/fr/07.webp)


*EFF-testpagina [Cover Your Tracks] (https://coveryourtracks.eff.org/) met de knop TEST YOUR BROWSER. Deze pagina wordt gebruikt om de bescherming tegen trackers en fingerprinting te evalueren



![LIBREWOLF](assets/fr/08.webp)


*Testresultaat Cover Your Tracks. Het bericht "U hebt een sterke bescherming tegen webtracking" wordt weergegeven, wat de effectiviteit van de LibreWolf.* bescherming laat zien



**LibreWolf activeert standaard strenge beveiligingsinstellingen. Firefox's Verbeterde Trackingbescherming wordt op het niveau Streng gezet om duizenden trackers, cookies van derden en schadelijke inhoud te blokkeren. Het activeert ook site- en cookie-isolatie (*Total Cookie Protection*) om gegevens voor elk domein te partitioneren, en beperkt WebRTC (beperking van *ICE-kandidaten* en routering via proxy wanneer een proxy aanwezig is) om het risico van IP Address-lekkage te beperken.



**Snelle engine-updates:** Het project volgt de ontwikkelingen van Firefox op de voet: LibreWolf is altijd gebaseerd op de laatste stabiele versie van Firefox, en de beheerders streven ernaar om binnen 24 tot 72 uur na elke officiële Firefox-release een nieuwe versie uit te brengen.



## Voor- en nadelen



### Voordelen





- Geen telemetrie of ongewenste verbindingen:** LibreWolf verzendt geen gebruiksgegevens, waardoor uw privacy volledig wordt gerespecteerd.





- Open-source en gebaseerd op de gemeenschap:** Het project is 100% open-source en wordt onderhouden door vrijwilligers. Deze onafhankelijkheid garandeert dat geen enkel reclamemodel de ontwikkeling zal beïnvloeden.





- Vooraf geconfigureerd voor privacy:** LibreWolf bespaart u kostbare tijd: u hoeft geen uren te besteden aan het harden van Firefox-instellingen, alles is al gedaan.





- Native ad blocker/tracker:** uBlock Origin is standaard geïntegreerd, dus je hoeft niets te doen om jezelf te beschermen tegen advertenties en bugs.





- Uitstekende bescherming tegen vingerafdrukken:** Dankzij RFP en talrijke privacy-instellingen vermindert LibreWolf drastisch je unieke digitale voetafdruk op het web.





- Verbeterde prestaties en lichter gewicht:** Door telemetrie en bepaalde niet-essentiële functies te verwijderen, kan LibreWolf iets sneller en minder energieverslindend zijn dan standaard Firefox.



### Nadelen en beperkingen





- Geen ingebouwde automatische updates:** LibreWolf werkt zichzelf niet bij. Het is aan jou om nieuwe versies te installeren zodra ze uitkomen, om veilig te blijven.





- Verminderde compatibiliteit met bepaalde diensten:** Door de zeer strikte instellingen kan LibreWolf problemen ondervinden op bepaalde websites. Netflix en Disney+ streaming platforms zullen niet werken, omdat LibreWolf standaard de Widevine DRM uitschakelt.





- Geen ingebouwd anoniem netwerk:** In tegenstelling tot Tor Browser routeert LibreWolf zelf geen verkeer via Tor of een VPN. Als je netwerkanonimiteit nodig hebt, moet je handmatig een proxy/VPN configureren.





- Niet-persistente cookies en sessies (standaard):** Om redenen van vertrouwelijkheid verwijdert LibreWolf cookies, geschiedenis en sitegegevens elke keer dat u uw browser sluit. U moet elke keer dat u inlogt opnieuw inloggen op uw accounts.





- Geen mobiele versie of cloudsynchronisatie:** LibreWolf is alleen beschikbaar op de desktop (Windows, Linux, macOS). Er is geen mobiele applicatie en dus ook geen synchronisatie van accounts of bladwijzers via een cloud.



## LibreWolf installeren



**Officiële website:** [librewolf.net](https://librewolf.net)



LibreWolf is beschikbaar voor alle grote desktopbesturingssystemen: Linux, Windows en macOS. Ga naar de officiële website om LibreWolf te downloaden:



![LIBREWOLF](assets/fr/02.webp)


*De startpagina van LibreWolf (librewolf.net) toont het browserlogo, een blauwe knop Installeren en de koppelingen Broncode en Documentatie. Een grote blauwe pijl wijst naar de knop Installeren*



Klik op de knop "Installatie" voor gedetailleerde instructies voor je besturingssysteem:



![LIBREWOLF](assets/fr/03.webp)


*Besturingssysteem selectie pagina voor LibreWolf.* download



De installatie verschilt afhankelijk van je besturingssysteem:



### Op Linux


LibreWolf biedt builds voor veel distributies. Op Debian/Ubuntu en afgeleiden is een officiële APT repository beschikbaar. Als alternatief is LibreWolf gepubliceerd in Flatpak op Flathub:


```
flatpak install flathub io.gitlab.librewolf-community
```



### Op Windows


Download het installatieprogramma (.exe) van de officiële website of gebruik de:




- Chocolade:** `choco install librewolf`
- WinGet:** `winget installeer librewolf`



### Op macOS


LibreWolf is beschikbaar als een .dmg pakket voor Mac. Download de schijfimage van de officiële website en sleep de LibreWolf-toepassing naar je map Toepassingen. Je kunt het ook installeren via Homebrew.




## Configuratie en eerste gebruik



Bij de eerste keer opstarten zul je de bekende Firefox Interface opmerken, behalve dat het meer gestript is: de startpagina bevat alleen de zoekbalk en geen gesponsorde suggesties. Je ziet het uBlock Origin-pictogram in de werkbalk - een teken dat de blocker actief is.



![LIBREWOLF](assets/fr/04.webp)


*LibreWolf startpagina met extensies en menu. Een blauwe pijl in de rechterbovenhoek geeft het menupictogram aan (drie horizontale balken)



LibreWolf laadt uw pagina's automatisch in "strikte" (anti-tracking) modus, en de standaard zoekmachine zal DuckDuckGo zijn. Je kunt proberen een trackingtestsite te bezoeken (bijv. amiunique.org) om de blootgelegde footprint te observeren - deze zou veel algemener moeten zijn dan met een standaardbrowser.



### Privacy-instellingen



LibreWolf is al optimaal geconfigureerd voor privacy. In Menu → Opties → Privacy & Beveiliging zie je dat LibreWolf is ingesteld op de modus Verbeterde Trackingbescherming: Strict. Deze modus blokkeert:




- Inter-site trackers
- Cookies van derden
- Bekende tracking-inhoud
- Cryptomining
- Digitale vingerafdrukdetectoren



![LIBREWOLF](assets/fr/05.webp)


*Tabblad Beveiliging en privacy toont de beveiligingsinstellingen van LibreWolf.*



WebRTC is uitgeschakeld (om IP-lekken te voorkomen) en Total Cookie Protection is ingeschakeld. Telemetrie en Firefox-onderzoeken zijn volledig uitgeschakeld.



### Beheer van cookies en geschiedenis



Standaard verwijdert LibreWolf cookies en lokale opslag telkens als het wordt afgesloten. Als dit gedrag je stoort, kun je het aanpassen in Privacy & Beveiliging → Cookies en sitegegevens door "Cookies en sitegegevens verwijderen bij het sluiten van LibreWolf" uit te vinken.



![LIBREWOLF](assets/fr/06.webp)


*Dezelfde pagina iets verder naar beneden, met de optie om cookies te verwijderen als de browser wordt afgesloten*



### Nuttige extensies toevoegen



Uit principe raadt LibreWolf het toevoegen van onnodige extensies af, omdat elke extensie een volgvector kan zijn. Desalniettemin kunnen sommige goede extensies uw ervaring verbeteren:




- Firefox Multi-Account Containers** (door Mozilla) voor gecompartimenteerd browsen
- Decentraleyes** of **LocalCDN** om gemeenschappelijke bibliotheken lokaal te bedienen



Vermijd vooral "gratis VPN"-extensies of dubieuze proxies - uBlock Origin dekt al 99% van je behoeften.



## Dagelijks gebruik



### Dagelijks surfen op het web


Gebruik LibreWolf voor uw dagelijkse internetactiviteiten. Het grote verschil met andere browsers is dat u veel minder reclamesporen achterlaat. Accepteer cookie"-banners verdwijnen op veel sites dankzij de filterlijsten van uBlock.



### Gebruik privétabbladen om te compartimenteren


Hoewel LibreWolf alles aan het einde van de sessie verwijdert, kan het handig zijn om een privé browservenster (Ctrl+Shift+P) te openen voor bepaalde taken tijdens de sessie, om zo een specifieke identiteit af te schermen.



### Profiteer van containers met meerdere accounts


Het installeren van de uitbreiding Multi-Account Containers kan je enorm helpen bij het segmenteren van je activiteiten in waterdichte silo's. Je kunt bijvoorbeeld een "Banking" container definiëren voor je banksites, een "Social Networks" container voor Facebook/Twitter, enz. Elke container heeft zijn eigen cookies, sessies en geïsoleerde opslag. Elke container heeft zijn eigen cookies, sessies en geïsoleerde opslag.



### Verfijnd rechtenbeheer per site


Met LibreWolf kunt u per geval bepalen welke rechten u aan sites geeft (Locatie, Camera, Microfoon, Meldingen). Geef alleen rechten aan sites die u vertrouwt en waar dat nodig is.



## Beste praktijken met LibreWolf



1. **Houd LibreWolf up-to-date:** Controleer de site regelmatig op nieuwe versies, vooral na een stabiele Firefox-release.



2. **Vermijd het vermengen van persoonlijke identiteit en privé browsen:** Idealiter log je niet in met je persoonlijke accounts op dezelfde sessie waar je gevoelig onderzoek doet.



3. **Overlaad LibreWolf niet met overbodige extensies:** Elke extensie die u installeert kan risico's voor beveiliging of fingerprinting met zich meebrengen.



4. **Gebruik daarnaast een VPN of Tor proxy:** LibreWolf maakt je niet anoniem voor je ISP. Voor netwerkanonimiteit kun je LibreWolf achter een vertrouwde VPN gebruiken.



5. **Bewaar uw belangrijke gegevens:** Bladwijzers, wachtwoorden indien lokaal opgeslagen. Overweeg een externe wachtwoordmanager (KeePassXC, Bitwarden) in plaats van de standaard wachtwoordmanager van de browser.



## Vergelijking met andere browsers



LibreWolf maakt deel uit van de "gereedschapskist" van privacy-georiënteerde browsers:



**LibreWolf vs. Firefox:** LibreWolf wordt al gehard en zonder telemetrie geleverd. Firefox behoudt het voordeel van synchronisatie met meerdere apparaten en een zeer groot gebruikersbestand, maar vereist handmatige configuratie om het vertrouwelijkheidsniveau van LibreWolf te bereiken.



**Brave gebruikt Chrome/Chromium-code en integreert een bedrijfsmodel via zijn optionele advertentieprogramma. LibreWolf is een Fork gemeenschap voor Firefox, behoudt Mozilla's vrije ecosysteem en heeft geen banden met Google.



**LibreWolf vs Tor Browser:** Tor Browser is onvervangbaar voor anonimiteit in het gezicht van krachtige surveillance, maar het is traag en ongemakkelijk in het dagelijks gebruik. LibreWolf, voor dagelijks browsen op het klassieke web, is veel sneller en praktischer.



**LibreWolf vs Mullvad Browser:** Mullvad Browser gaat nog verder in standaardisatie, maar ten koste van verminderde bruikbaarheid (onmogelijk om een login-cookie te bewaren). LibreWolf heeft een evenwicht gevonden: zeer privé, maar dagelijks bruikbaar.



## Conclusie



LibreWolf is een uitstekende oplossing voor diegenen die op zoek zijn naar een ultraprivate "alledaagse" browser zonder de extreme anonimiteit van Tor. Het is een ideale keuze voor activisten, journalisten, ontwikkelaars of power users die klassiek willen surfen op het web (snel, compatibel met moderne sites) en tegelijkertijd willen ontsnappen aan advertentietracking en Big Tech.



Hoewel het bepaalde beperkingen heeft (geen automatische updates, verminderde compatibiliteit met bepaalde diensten), is LibreWolf een waardevol hulpmiddel in het arsenaal van iedereen die weer controle wil krijgen over zijn digitale privacy. Het gebruiksgemak en de standaardconfiguratie maken het een verstandige keuze voor privacybewuste gebruikers.



## Bronnen



### Officiële documentatie




- [LibreWolf officiële website](https://librewolf.net)
- [Broncode op Codeberg](https://codeberg.org/librewolf)
- [Officiële FAQ](https://librewolf.net/docs/faq)



### Gidsen en vergelijkingen




- [Privacyrichtlijnen] (https://www.privacyguides.org/en/desktop-browsers/)
- [Vergelijkende privacytests](https://privacytests.org)



### Steun van de gemeenschap




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)