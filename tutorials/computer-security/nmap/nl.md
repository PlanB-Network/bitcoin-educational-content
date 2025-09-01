---
name: Nmap
description: Master Nmap voor het in kaart brengen van netwerken en scannen op kwetsbaarheden
---

![cover](assets/cover.webp)



*Deze tutorial is gebaseerd op originele inhoud van Mickael Dorigny gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er zijn wijzigingen aangebracht in de oorspronkelijke tekst.*



___



Welkom bij deze inleidende tutorial over Nmap, ontworpen voor iedereen die deze krachtige netwerkscantool onder de knie wil krijgen. Het doel is om je te voorzien van de fundamentele kennis die je nodig hebt om Nmap dagelijks effectief te gebruiken.



Nmap is een veelzijdig hulpprogramma dat veel gebruikt wordt door IT-, netwerk- en cyberbeveiligingsprofessionals voor diagnostiek, netwerkontdekking en beveiligingsaudits. Deze tutorial is bedoeld voor mensen die nieuw zijn op dit gebied en de basisbeginselen van Nmap willen leren. Een basiskennis van systeem- en netwerkbeheer wordt aanbevolen.



U leert de basis van Nmap, hoe u poortscans kunt uitvoeren, actieve hosts op een netwerk kunt identificeren, serviceversies en besturingssystemen kunt detecteren, kwetsbaarheden kunt scannen en nog veel meer. Elk deel bevat gedetailleerde uitleg en praktische voorbeelden om het gebruik van Nmap in verschillende contexten onder de knie te krijgen.



Aan het eind van deze tutorial heb je een goed begrip van Nmap en kun je het effectief gebruiken om de beveiliging en het beheer van je netwerken te verbeteren. Veel leesplezier.



## 1 - Inleiding tot Nmap: Wat is Nmap?



### I. Presentatie



In dit eerste deel bekijken we de Nmap netwerkscantool. We bekijken de belangrijkste Elements die je moet weten over deze tool en hoe het in het algemeen werkt. Dit zal ons helpen om de rest van de tutorial beter te begrijpen.



### II. Introductie van het hulpprogramma Nmap



Nmap, voor _Network Mapper_, is een gratis, open-source hulpprogramma dat wordt gebruikt voor **netwerkontdekking, mapping en beveiligingsauditing**. Het kan ook worden gebruikt voor andere taken zoals **netwerkinventarisatie, diagnostiek of toezicht**.



Het kan bepalen of hosts op een gericht netwerk actief en bereikbaar zijn, welke netwerkservices zijn blootgesteld, welke versies en technologieën in gebruik zijn en andere nuttige analyse-informatie. Nmap kan gebruikt worden om een enkele service op een specifieke machine te scannen, of over grote delen van het netwerk, tot het hele internet.



Nmap heeft vele sterke punten:





- Krachtig en flexibel**: Nmap kan grote netwerken scannen en geavanceerde detectietechnieken gebruiken. Het ondersteunt UDP, TCP, ICMP, IPv4 en IPv6 en kan versiedetectie, kwetsbaarheidsscans of protocol-specifieke interacties uitvoeren. De architectuur is modulair, met name dankzij NSE (Nmap Scripting Engine) scripts, die we later in deze tutorial zullen bekijken.
- Gebruiksgemak**: officiële documentatie is overvloedig en van de hoogste kwaliteit. Er zijn ook talloze community resources beschikbaar om je op weg te helpen.
- Populariteit en lange levensduur**: Nmap is al sinds 1998 een referentie op dit gebied. De huidige versie, op het moment van deze update, is 7.95. Hoewel er andere tools bestaan voor specifieke taken, blijft Nmap een must-have voor het in kaart brengen en analyseren van netwerken.



**Nmap in de bioscoop**



Nmap is een van de weinige beveiligingstools die een zekere bekendheid heeft verworven bij het grote publiek. Het komt voor in de film _Matrix Reloaded_, in een symbolische scène waarin Trinity het gebruikt om een systeem te hacken:



![nmap-image](assets/fr/01.webp)



matrix: Reloaded scène met Nmap



Hij verschijnt ook in andere cinematografische werken.



**Feedback



Als systeembeheerder en daarna cybersecurity auditor en pentester, **gebruik ik Nmap bijna dagelijks** en ik raad het **regelmatig** aan systeembeheerders aan die hun controle over netwerken willen versterken en hun diagnostische mogelijkheden willen verbeteren.



### III. Werking op hoog niveau



Nmap is beschikbaar voor Linux, Windows en macOS. Het is voornamelijk geschreven in C, C++ en Lua (voor NSE-scripts). Het wordt voornamelijk gebruikt op de commandoregel, hoewel grafische interfaces zoals Zenmap ook beschikbaar zijn. We raden je echter sterk aan om te beginnen met de commandoregel om beter te begrijpen hoe het werkt.



Een eenvoudig voorbeeld:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Dit commando wordt later in detail uitgelegd. In deze tutorial gebruiken we Nmap op Linux, maar het gebruik is vergelijkbaar op andere systemen. Onder Windows vertrouwt Nmap op de **Npcap** bibliotheek (ter vervanging van het nu verouderde WinPcap) om netwerkpakketten op te vangen en te injecteren.



Nmap wordt gebruikt als een conventionele binary, zoals `ls` of `ip`. Voor sommige geavanceerde functies zijn verhoogde rechten nodig, omdat de tool soms pakketten op onconventionele manieren manipuleert om specifieke reacties op doelsystemen uit te lokken (met name voor service of detectie van kwetsbaarheden).



### IV. Gevolgen van het gebruik van Nmap



Voordat je Nmap gebruikt, is het essentieel om je bewust te zijn van de potentiële impact op netwerken en systemen:





- Het kan **duizenden of zelfs miljoenen pakketten** in korte tijd versturen, waardoor bepaalde netwerkinfrastructuren verzadigd kunnen raken.
- Het kan generate **misvormde of niet-standaard** pakketten, die waarschijnlijk bepaalde apparatuur (vooral industriële systemen) verstoren.
- Het kan **aanval-achtig gedrag** produceren, wat waarschuwingen kan triggeren in beveiligingssystemen (firewalls, IDS/IPS, etc.).



Over het algemeen is **Nmap een zeer spraakzaam hulpmiddel**, omdat het veel verkeer genereert om zoveel mogelijk informatie te verzamelen. Het is daarom aan te raden om volledig te begrijpen hoe het werkt voordat je het gebruikt op gevoelige of productieomgevingen.



### V. Conclusie



Deze sectie introduceert Nmap en zijn belangrijkste functies. We hebben gezien dat het een essentieel, krachtig en flexibel hulpmiddel is om netwerken in kaart te brengen. We hebben ook besproken hoe het werkt en welke voorzorgsmaatregelen je moet nemen als je het gebruikt, om de scène te zetten voor de volgende delen van de tutorial.



## 2 - Waarom Nmap gebruiken?



### I. Presentatie



In dit gedeelte kijken we naar de belangrijkste toepassingen van het netwerkscantool Nmap. We zullen zien dat het een tool is die veel gebruikt wordt in vele contexten en beroepen, en dat het zeker een nuttige vaardigheid is om het in je gereedschapskist te hebben en te weten hoe je het moet beheersen.



### II. Nmap gebruiken voor diagnostiek en toezicht



Nmap kan gebruikt worden voor netwerkdiagnose en, in bredere zin, voor monitoring. Net zoals een ping gebruikt kan worden om te bepalen of twee hosts communiceren, kan Nmap gebruikt worden om snel te bepalen of een host actief is, of een bepaalde dienst operationeel is. Dankzij [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") kunnen we precieze gegevens verkrijgen over de reactietijd van een host, de route die pakketten afleggen, de respons van een specifieke dienst, enzovoort.



Het volgende commando en resultaat kunnen bijvoorbeeld gebruikt worden om snel uit te vinden of een webserver op host **192.168.1.18** actief is en correct reageert:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Gebruik Nmap om de webservicestatus op te vragen van een externe server.*



Het gebruik van Nmap gaat dus verder dan de bekende "ping test" tijdens debuggen of diagnostische fases. We zullen later zien dat er verschillende methoden zijn die Nmap gebruikt om te identificeren welke service luistert op een bepaalde poort, inclusief de versie.



### III. Nmap gebruiken om netwerken in kaart te brengen



Als _Network Mapper_ is het in kaart brengen van netwerken het hoofddoel van dit hulpmiddel. Het kan worden gebruikt binnen een lokaal netwerk of over meerdere netwerken, subnetten en VLAN's om een lijst te maken van alle bereikbare hosts en services. Nmap maakt deze taak veel sneller en efficiënter dan elke handmatige methode.



Het volgende commando kan bijvoorbeeld gebruikt worden om snel actieve hosts op het **192.168.1.0/24** netwerk te identificeren:



```
nmap -sn 192.168.1.0/24
```



*Opmerking: de `-sP` optie is verouderd en vervangen door `-sn`.*



![nmap-image](assets/fr/03.webp)



*Nmap gebruiken om bereikbare hosts op een netwerk te ontdekken*



We zullen later zien dat er verschillende methoden zijn die door Nmap worden gebruikt om te bepalen of een host als "actief" kan worden beschouwd, zelfs als het a priori geen diensten blootstelt.



### IV. Nmap gebruiken om een filterbeleid te evalueren



Nmap heeft het voordeel dat het feitelijk is: de resultaten maken het mogelijk om concrete bevindingen vast te stellen, in tegenstelling tot welk architectuurdocument of filterbeleid dan ook. Het is een belangrijk hulpmiddel om de effectiviteit van de compartimentering van informatiesystemen te beoordelen, omdat het je in staat stelt om **te controleren of het filterbeleid daadwerkelijk wordt toegepast**.



In een bedrijfsnetwerk schrijft best practice voor dat systemen gesegmenteerd moeten worden op basis van hun rol, kriticiteit of locatie. Filterregels (vaak geïmplementeerd via firewalls) moeten de communicatie tussen zones beperken. Maar deze configuraties zijn vaak complex en foutgevoelig.



Om te valideren dat het beleid wordt nageleefd, gaat er dus niets boven een concrete test. Je kunt bijvoorbeeld controleren of gevoelige beheerdiensten (SSH, WinRM, MSSQL, MySQL, enz.) niet toegankelijk zijn vanuit een gebruikerszone.



Het gebruik van **Nmap om het filterbeleid** te testen zou systematisch moeten gebeuren voordat zo'n beleid in productie wordt genomen. Helaas wordt deze controle vaak verwaarloosd.



Mijn ervaring is dat veel configuratiefouten onopgemerkt blijven door het ontbreken van validatietests. Een eenvoudige fout in een IP-bereik of een regelovertreding kan een zogenaamd geïsoleerde zone kwetsbaar maken.



### V. Nmap gebruiken voor beveiligingsaudits en penetratietests



Nmap heeft **veel nuttige functies voor beveiligingsbeoordeling**, penetratietesten (pentests) en helaas ook voor aanvallers.



Netwerkontdekkingsfuncties zijn cruciaal voor een aanvaller, die de netwerktopologie moet begrijpen na een eerste compromittering. Maar Nmap biedt veel meer dan dit: het integreert een scripting engine, **waarvan er veel zijn gewijd aan het opsporen van kwetsbaarheden**.



Dit commando kan bijvoorbeeld gebruikt worden om te controleren of een FTP service een anonieme verbinding toestaat, zonder handmatig te verbinden:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Een NSE-script gebruiken om te controleren op anonieme FTP-authenticatie via Nmap.*



Nmap kwetsbaarheidsdetectie is een van de eerste stappen in een audit of penetratietest. Hiermee kunt u snel bepaalde zwakke punten identificeren en uw analyse-inspanningen optimaliseren.



Maar let op: **tools om kwetsbaarheden te scannen hebben hun beperkingen**. Nmap dekt slechts een fractie van de bedreigingen en garandeert niet dat een systeem veilig is als er geen problemen worden gedetecteerd. Het is daarom essentieel om **te begrijpen hoe de gebruikte scripts werken** en niet alleen op hun oordeel te vertrouwen.



### VI. Conclusie



We hebben gezien dat het beheersen van Nmap een breed scala aan gebruikssituaties kan omvatten, van diagnostiek en monitoring tot mapping, evaluatie van het beveiligingsbeleid en het scannen op kwetsbaarheden. In de volgende sectie gaan we tot de kern en installeren we Nmap.




## 3 - Nmap installeren en configureren



### I. Presentatie



In deze sectie leren we hoe we de Nmap netwerkscan tool kunnen installeren op Linux en Windows OS. Aan het einde van deze sectie hebben we alles wat we nodig hebben om Nmap te gaan gebruiken voor toekomstige modules. Tot slot zullen we zien welke privileges het nodig heeft bij gebruik en waarom.



### II. Nmap installeren onder Linux



Nmap is oorspronkelijk ontworpen om op GNU/Linux besturingssystemen te draaien. Als gevolg hiervan, en dankzij zijn lange levensduur en populariteit, vind je het in alle officiële repositories van de grote Unix distributies. In deze tutorial gebruik ik een Debian-gebaseerd besturingssysteem [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Maar je kunt het op precies dezelfde manier gebruiken als een klassieke Debian, CentOS, Red Hat of wat dan ook!



Onder Debian kunt u het volgende commando gebruiken om te controleren of Nmap aanwezig is in uw huidige repositories:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Het antwoord hier geeft duidelijk aan dat het "nmap" pakket bestaat in de repositories (hier die van Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Vanaf nu kun je Nmap installeren via de gebruikelijke installatiecommando's, voorlopig niets ontwapenends 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Om te controleren of Nmap correct is geïnstalleerd, geven we de versie weer:



```
nmap --version
```



Hier is het verwachte resultaat:



![nmap-image](assets/fr/05.webp)



resultaat van het weergeven van de huidige versie van Nmap._



Let op de aanwezigheid in dit scherm van de "libpcap" (_Packet Capture Library_) bibliotheek en de versie ervan. Ook gebruikt door Wireshark, wordt "libpcap" gebruikt door Nmap om pakketten aan te maken en te manipuleren en te luisteren naar netwerkverkeer.



### III Nmap installeren op Windows



Om op een Windows-besturingssysteem te installeren, download je eerst de binary van de officiële site (en geen andere!):





- Nmap downloadpagina op de officiële website: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Vervolgens moet je het binaire bestand met de naam `nmap-<VERSIE>-setup.exe` downloaden:



![nmap-image](assets/fr/06.webp)



nmap voor Windows installatie binaire downloadpagina



Zodra je deze binary op je systeem hebt staan, kun je hem gewoon uitvoeren om Nmap te installeren. Dit is een eenvoudige installatie en je kunt alle opties als standaard laten.



Mijn reflex is om het vakje "zenmap (GUI Frontend)" uit te vinken. Dit is een grafische Interface voor Nmap die ik niet gebruik en die niet wordt behandeld in deze tutorial, maar voel je vrij om het uit te proberen als je de Nmap commandoregeltool onder de knie hebt!



![nmap-image](assets/fr/07.webp)



optionele deselectie van Zenmap bij installatie van Nmap op Windows



Aan het einde van de Nmap installatie wordt een tweede installatie voorgesteld: die van de "Npcap" bibliotheek:



![nmap-image](assets/fr/08.webp)



installatie van de "Npcap"-bibliotheek bij de installatie van Nmap onder Windows



Dit is de bibliotheek waarop Nmap vertrouwt om de netwerkcommunicatie te beheren, d.w.z. het bouwen, verzenden en ontvangen van netwerkpakketten. Je bent deze bibliotheek waarschijnlijk al tegengekomen als je Wireshark op Windows gebruikt, aangezien deze er ook gebruik van maakt en installatie vereist.



Net als bij Linux kun je valideren dat Nmap is geïnstalleerd door een Command Prompt of een [Powershell] terminal (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") te openen en het volgende commando in te typen:



```
nmap --version
```



Hier is het verwachte resultaat:



![nmap-image](assets/fr/09.webp)



resultaat van het weergeven van de huidige versie van Nmap._



Nmap is nu geïnstalleerd op Windows. Je kunt het op precies dezelfde manier gebruiken als op Linux, door deze tutorial te volgen.



### IV. Lokale privileges vereist om Nmap te gebruiken



Maar trouwens, als je Nmap gebruikt, **is het dan nodig om verhoogde lokale rechten op het systeem te hebben?** Het antwoord is: **het hangt ervan af**.



In zijn basisvorm, d.w.z. zonder erg ver te gaan in het gebruik van zijn opties, heeft Nmap niet per se privileged rechten nodig. Je zult je echter al snel realiseren dat het beter is om Nmap in een bevoorrechte context te gebruiken ("root" onder Linux, "administrator" of gelijkwaardig onder Windows) om het volledig te kunnen gebruiken, met het risico op een foutmelding zoals deze:



![nmap-image](assets/fr/10.webp)



foutmelding onder Linux wanneer Nmap-opties rootrechten vereisen._



Of het nu op Linux of Windows is, er zijn veel gevallen waarin Nmap je om bevoorrechte toegang zal vragen. De belangrijkste redenen zijn de volgende (niet-uitputtende lijst):





- Construeren van "ruwe" netwerkpakketten**: Nmap is in staat om een breed scala aan scanmethodes uit te voeren, inclusief geavanceerde pakketmanipulatie en -constructie. Dit is bijvoorbeeld het geval wanneer we TCP SYN scans willen uitvoeren, die de klassieke _Three-way handshake_ van TCP uitwisselingen niet respecteren. Om dit te doen, moet Nmap andere functies gebruiken dan die van besturingssystemen, die alleen weten hoe ze goede praktijken in netwerkcommunicatie moeten respecteren (het doet een beroep op de "Npcap" en "libcap" bibliotheken hierboven). Omdat Nmap dingen niet op de "standaard" manier doet, is het in staat om bepaalde informatie over besturingssystemen, services en bepaalde kwetsbaarheden af te leiden.





- Luisteren naar netwerkverkeer**: sommige opties van Nmap vereisen dat het naar het netwerk luistert om bepaalde informatie op te halen. Deze actie wordt als gevoelig beschouwd op besturingssystemen, omdat het je ook toestaat om mee te luisteren met de communicatie van andere applicaties op het systeem. Net als Wireshark heeft Nmap hiervoor specifieke privileges nodig, die makkelijker te verkrijgen zijn door direct in een geprivilegieerde sessie te zitten.





- Luisteren op geprivilegieerde poorten**: op besturingssystemen worden poorten van 0 tot 1024 (zowel TCP als UDP) geprivilegieerd genoemd, dat wil zeggen dat ze op de een of andere manier gereserveerd zijn voor zeer specifiek gebruik en daarom beschermd zijn. Hoewel dit tegenwoordig een enigszins verouderde reden is, is het nog steeds nodig om bepaalde privileges te hebben om op deze poorten te luisteren, wat Nmap mogelijk moet doen, afhankelijk van hoe het gebruikt zal worden.





- UDP-pakketten versturen:** Ook het luisteren naar een netwerktoepassing op UDP-poorten (een stateloos protocol) vereist privileges op besturingssystemen. Een bevoorrechte sessie is daarom nodig als u een UDP-scan wilt uitvoeren, waarvoor Nmap moet luisteren naar een antwoord om de antwoorden op zijn scans te analyseren.




Om precies te zijn is het mogelijk, tenminste onder Linux, om Nmap met al zijn functies en opties uit te voeren zonder root te zijn. Dit wordt bereikt door de juiste _capaciteiten_ aan de binary toe te kennen. Dit vereist echter geavanceerde manipulatie en is misschien niet zo praktisch als Nmap direct draaien met privileges. Deze aanpak is ook minder gebruikelijk en kan veiligheidsproblemen opleveren als het verkeerd geconfigureerd is.



Dit wijkt echter een beetje af van onze Nmap-tutorial, dus daar zien we voorlopig vanaf.



Ga er voor de rest van deze tutorial van uit dat Nmap altijd als "root" wordt uitgevoerd (vanuit een shell als "root" of via het commando "sudo"), of in een administrator terminal onder Windows, zelfs als dit niet wordt aangegeven. Anders kunt u subtiele maar merkbare verschillen ervaren met de zelfstudie.



### V. Conclusie



En klaar is kees! Nmap is nu geïnstalleerd op ons besturingssysteem en klaar voor gebruik, zonder verdere configuratie. Dit deel sluit de introductie en presentatie van Nmap af. Ik hoop dat het je heeft doen watertanden en dat je staat te popelen om te beginnen met oefenen.



Op een serieuzere noot, we hebben nu een beter idee van wat de Nmap mapping tool is en wat de meest voorkomende toepassingen zijn, maar ook de beperkingen. Laten we verder gaan!




## 4 - TCP- en UDP-poortscans met Nmap



### I. Presentatie



In dit gedeelte leren we hoe we onze eerste poortscans kunnen uitvoeren met het netwerkscanprogramma Nmap. We zullen zien hoe we het kunnen gebruiken om een lijst samen te stellen van netwerkservices die op een host aanwezig zijn, of ze nu TCP of UDP protocollen gebruiken.



Denk er vanaf nu aan om alleen hosts in een gecontroleerde omgeving te scannen waarvoor je expliciet toestemming hebt.





- Ter herinnering: [Wetboek van Strafrecht: Hoofdstuk III: Aanvallen op geautomatiseerde gegevensverwerkende systemen] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Als je er geen bij de hand hebt**, raad ik de volgende gratis oplossingen aan, die zijn precies wat je nodig hebt!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Hacking training platform, Hack The Box biedt voortdurend kwetsbare systemen die je naar eigen inzicht kunt aanvallen. Er zijn enkele honderden systemen beschikbaar, maar een vernieuwde pool van 20 machines wordt het hele jaar door gratis aangeboden, met toegang via een OpenVPN VPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Dit platform biedt talloze opzettelijk kwetsbare systemen om te downloaden, die kunnen worden gebruikt via VirtualBox (ook een gratis oplossing) of andere middelen. Eenmaal gedownload is er geen VPN nodig - alles is lokaal.




Het staat je ook vrij om **een virtuele machine** te maken op je favoriete besturingssysteem en daar verschillende services op te installeren als testdoelen. Het voordeel hiervan is dat je ook kunt zien wat er aan de serverkant gebeurt tijdens een scan, vooral met Wireshark, en dat je een handje hebt in de lokale firewall als we meer geavanceerde tests doen.



Laten we praktisch worden!



### II. De TCP-poorten van een host scannen via Nmap



#### A. Eerste TCP-poortscan met Nmap



We gaan nu onze eerste scans uitvoeren via Nmap. Ons doel hier is eenvoudig: we willen uitzoeken welke services worden blootgesteld door de webserver die we zojuist hebben geïmplementeerd, om te zien of er iets onverwachts is, zoals een beheerservice die niet toegankelijk zou moeten zijn, of de blootstelling van een poort van een applicatie waarvan we dachten dat die buiten gebruik was gesteld.



In mijn voorbeeld heeft de te scannen host het IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Hier is een mogelijk resultaat. We zien een klassieke Nmap terugkomst met veel informatie:



![nmap-image](assets/fr/11.webp)



resultaten van een eenvoudige TCP-scan uitgevoerd met Nmap._



Als we even naar dit resultaat kijken, zien we dat de poorten TCP/22 en TCP/80 toegankelijk zijn op deze host.



Standaard, en als je dat niet aangeeft, zal Nmap alleen TCP poorten scannen.



#### B. De resultaten van een eenvoudige Nmap-scan begrijpen



Laten we echter een stap verder gaan om deze uitvoer te begrijpen: elke regel is belangrijk, ten eerste om te weten wat er zojuist is gedaan en ten tweede om de scanresultaten zelf goed te interpreteren.



De eerste regel is in wezen een herinnering aan de scanversie en -datum (handig voor het loggen en archiveren tenslotte!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



De tweede regel toont de scanresultaten voor de host "debian.home (192.168.1.19)". Deze informatie is handig als we meerdere hosts tegelijk gaan scannen:



```
Nmap scan report for debian.home (192.168.1.19)
```



De derde regel vertelt ons dat de host in kwestie "Up" is, dus actief:



```
Host is up (0.00022s latency).
```



Tot slot informeert Nmap ons dat 998 TCP-poorten die als gesloten zijn geïdentificeerd, niet worden weergegeven in de:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Dit bespaart ons bijna 1000 regels uitvoer die eruit zien als:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Bedankt dat hij ons dit bespaard heeft!



Waarom 998 "gesloten" poorten? Met de 2 open poorten erbij is dat 1000, en dat is het aantal poorten dat Nmap zal scannen in zijn standaardconfiguratie, niet de 65535 bestaande TCP poorten! We zullen later zien dat dit volledig en eenvoudig aan te passen is. Maar als de beoogde host een service heeft die luistert op een nogal exotische poort, zal deze "standaard" scan dit niet ontdekken.



Na deze informatie vinden we wat het meest interessant is: een tabel georganiseerd volgens de drie kolommen "PORT - STATE - SERVICE":





- De eerste kolom "PORT" geeft eenvoudigweg de doelpoort/het doelprotocol aan en het is hier belangrijk om te kijken of het een TCP-poort (`<port>/tcp`) of UDP (`<port>/udp`) is.





- De kolom "STATE" geeft de status aan van de netwerkdienst die op deze poort is ontdekt en door Nmap is bepaald op basis van het verkregen antwoord. Dit kan "open", "closed", "filtered" of "unknown" zijn. We zullen later zien hoe Nmap onderscheid maakt tussen deze verschillende toestanden.





- De kolom "SERVICE" geeft de dienst aan die beschikbaar is op de betreffende poort. Merk echter op dat we hier geen actieve service discovery opties hebben gebruikt. Nmap vertrouwt op een lokale verwijzing tussen een poort/protocol en de vermoedelijk toegewezen dienst: het bestand "/etc/services




Als je het bestand "/etc/services" op een Linux systeem bekijkt, vind je een link "port/protocol - service" die lijkt op de link die door Nmap wordt weergegeven:



![nmap-image](assets/fr/12.webp)



haalt de inhoud van het bestand "/etc/services" onder Linux op



Het is belangrijk om te begrijpen dat Nmap op dit moment geen actieve service discovery heeft uitgevoerd. Het zou bijvoorbeeld niet in staat zijn geweest om de SSH service achter een TCP/80 poort te identificeren als dit het geval was geweest. Vandaar het belang om te weten hoe de juiste opties te gebruiken - het komt eraan!



Weten hoe je de uitvoer van Nmap moet interpreteren is een belangrijk onderdeel van het beheersen van de tool. Het goede nieuws is dat deze uitvoer grotendeels hetzelfde zal zijn, welke opties je ook gebruikt.



#### C. Onder de motorkap: netwerkanalyse via Wireshark



Als je goed kijkt naar wat er gebeurt op het netwerk Interface van de host die de server scant, of op dat van de server zelf, worden de acties van Nmap veel duidelijker. Dat is wat we hier gaan doen.



Wat ik je hier kan laten zien is slechts een deel van wat zichtbaar is in Wireshark. Als je verder wilt gaan, voel je dan vrij om zelf een netwerk capture te doen tijdens een scan, en blader dan door wat er is vastgelegd.



In deze test bevinden mijn scanhost (192.168.1.18) en mijn doelhost (192.168.1.19) zich op hetzelfde lokale netwerk.



Nmap begint met het uitzoeken of de doelhost actief is op het lokale netwerk door een ARP-verzoek te sturen. Als het een antwoord ontvangt, weet het dat de host actief is en begint het met zijn netwerkscan:



![nmap-image](assets/fr/13.webp)



_ARP-verzoek van Nmap om te bepalen of een doelhost aanwezig is op het lokale netwerk._



Als de te scannen host zich op een extern netwerk bevindt, begint Nmap met het sturen van een ping verzoek en probeert een aantal van de meest blootgestelde poorten (TCP/80, TCP/443) te bereiken:



![nmap-image](assets/fr/14.webp)



ping-verzoek van Nmap om te bepalen of een doelhost bereikbaar is op een netwerk op afstand



Als het een reactie krijgt op een van deze tests, beschouwt het het doelwit als actief.



Zodra Nmap heeft vastgesteld dat het doel actief is, probeert het de domeinnaam op te lossen met de DNS server die op de netwerkkaart is geconfigureerd:



![nmap-image](assets/fr/15.webp)



dNS-resolutie op Nmap-scan-doel



Nu Nmap zijn doel heeft geïdentificeerd en weet dat het actief is, begint het met zijn TCP poort scan:



![nmap-image](assets/fr/16.webp)



tCP SYN pakket verzenden en RST/ACK ontvangen tijdens Nmap scan



Om dit te doen, zal het op elke TCP poort in zijn standaardbereik ** TCP SYN pakketten verzenden en wachten op een antwoord**. In de bovenstaande schermafbeelding ontvangt het TCP RST/ACK pakketten van de gescande server, wat betekent "ga verder, hier is niets te zien" - met andere woorden, deze poorten zijn gesloten. Zoals we in het resultaat zagen, is dit het geval voor de meeste gescande poorten. Met twee uitzonderingen:



![nmap-image](assets/fr/17.webp)



antwoord op een TCP SYN-pakket verzonden op poort 22, actief op het scandoel



In de bovenstaande schermafbeelding zien we een TCP SYN/ACK pakket verzonden door de doelhost**. De poort is actief en stelt een service bloot. Nmap bevestigt de ontvangst van het antwoord en beëindigt dan de verbinding (TCP RST/ACK). **Zo wist hij dat poort TCP/22 actief was**.



We hebben hier gezien dat Nmap de "Three Way Handshake" respecteert bij het scannen van een TCP netwerk. Om prestatieredenen is het mogelijk om het te vragen om niet te reageren op het terugsturen van de server, waardoor enkele duizenden pakketten bespaard worden bij het scannen van een groot netwerk. Maar we zullen deze opties en optimalisaties later in de tutorial bekijken.



We hebben nu een beter idee van hoe we een TCP-scan moeten uitvoeren en wat er gebeurt als deze wordt uitgevoerd. We hebben ook gezien dat Nmap standaard een TCP poortscan uitvoert op een beperkt aantal poorten.



### III. UDP-poorten scannen met Nmap



#### A. Eerste UDP-poortscan met Nmap



Laten we nu eens kijken hoe we de UDP-poorten van een host kunnen scannen. Zoals we hebben gezien, zal Nmap standaard altijd TCP poorten scannen. Dit kan betekenen dat we veel informatie missen als we ons er niet van bewust zijn.



Ter herinnering, voor deze test bevinden mijn scan host (192.168.1.18) en mijn doel host (192.168.1.19) zich op hetzelfde lokale netwerk.



```
nmap -sU 192.168.1.19
```



Hier heeft het verkregen resultaat hetzelfde formaat als voor een TCP-scan, maar de weergegeven actieve services zijn in `<port>/UDP`, zoals gevraagd!



![nmap-image](assets/fr/18.webp)



resultaat van een eenvoudige UDP-scan uitgevoerd met Nmap._



De "-sU" optie wordt gebruikt om Nmap te vertellen dat je op UDP wilt werken, in plaats van TCP zoals standaard is.



Overigens zul je waarschijnlijk merken dat Nmap "root"-rechten nodig heeft voor UDP-scans, zoals eerder in de tutorial vermeld.



opmerking: Sinds de laatste versies van Nmap is het altijd aanbevolen om UDP-scans uit te voeren met beheerdersrechten om betrouwbare resultaten te garanderen, omdat sommige functies onbewerkte toegang tot netwerk sockets vereisen._



UDP scans kunnen erg lang duren (1100 seconden om 1000 poorten te scannen in mijn voorbeeld), vanwege de afwezigheid van de "Three Way Handshake" in UDP, wat betekent dat Nmap wacht op een antwoord voor elk UDP pakket dat verzonden wordt en de poort pas als "gesloten" zal beschouwen als er na een bepaalde tijd (timeout) geen antwoord komt. Dit antwoord van gescande hosts is niet systematisch en is vaak beperkt in termen van het aantal antwoorden per seconde, om bepaalde versterkingsaanvallen te voorkomen. Dit in tegenstelling tot TCP, waar er een onmiddellijk antwoord is van de gescande host, of de poort nu open of gesloten is. We zullen later zien hoe we dit kunnen optimaliseren.



Een tweede moeilijkheid met UDP is **dat services niet altijd reageren op binnenkomende pakketten**, simpelweg omdat dit niet altijd nodig is en het het principe van UDP is. Wanneer dit het geval is en er geen ICMP "port unreachable" wordt ontvangen, wordt de service gemarkeerd als "open|filtered" door Nmap, zoals te zien is in de schermafbeelding hierboven.



#### B. Onder de motorkap: netwerkanalyse via Wireshark



Laten we, net als bij onze TCP-scan, eens kijken wat er op netwerkniveau gebeurt tijdens een UDP-scan met behulp van een Wireshark-analyse. Het gedrag van Nmap bij het bepalen of een host actief is, is hetzelfde.



Het enige echte verschil bij het scannen van UDP is dat Nmap niet wacht op een "Three Way Handshake", omdat dit mechanisme niet bestaat in UDP (stateless protocol):



![nmap-image](assets/fr/19.webp)



uDP pakketoverdracht en ICMP ontvangst (poort onbereikbaar) tijdens Nmap scan



We kunnen op de bovenstaande schermafbeelding zien dat Nmap een groot aantal UDP pakketten verstuurt en als antwoord op de meeste pakketten een ICMP "Destination unreachable (Port unreachable)" pakket ontvangt. Dit is normaal, want het is het gepaste antwoord gedefinieerd door [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") wanneer een UDP poort onbereikbaar is:



![nmap-image](assets/fr/20.webp)



uittreksel uit RFC 1122._



Laten we eens kijken naar deze Wireshark-capture, die **de drie mogelijke scenario's** in UDP laat zien:



![nmap-image](assets/fr/21.webp)



netwerk vastleggen tijdens een UDP-scan op verschillende poorten met Nmap._



De drie gevallen zijn als volgt:





- Het eerste Exchange bestaat uit de pakketten nr. 3, 4 en 8, 9. Nmap verstuurt UDP-pakketten op de klassieke SNMP-poort en **construeert daarom vooraf protocolconforme pakketten**. Vervolgens krijgt het een antwoord van de server (pakketten 8 en 9). Resultaat: Nmap heeft een antwoord ontvangen, de service is "open".





- De tweede Exchange bestaat uit de pakketten 6 en 7. Nmap stuurt een "leeg" UDP pakket (zonder protocolstructuur) naar poort UDP/165, en ontvangt een ICMP pakket als antwoord: "Destination unreachable (Poort onbereikbaar)". Resultaat: Nmap heeft een (negatief) antwoord ontvangen, de host is up, maar de service die het probeerde te bereiken is niet operationeel op deze poort, die wordt gemarkeerd als "gesloten".





- De laatste Exchange bestaat uit pakket nr. 12: Nmap stuurt een "leeg" UDP pakket naar poort UDP/1235. Er is geen antwoord, zelfs geen expliciete weigering van de gescande host. Er is geen antwoord, zelfs geen expliciete weigering van de gescande host. Resultaat: Nmap markeert de poort als "open|filtered", omdat het niet kan zeggen of dit komt door de aanwezigheid van een firewall, die geconfigureerd is om niet te reageren, of door een actieve UDP-service die toch geen antwoord terugstuurt (niet verplicht in UDP).




Hier is het resultaat dat wordt weergegeven door Nmap na deze drie gevallen:



![nmap-image](assets/fr/22.webp)



mogelijke resultaten van een UDP-scan uitgevoerd via Nmap._



We hebben nu een beter idee van hoe we een UDP scan moeten uitvoeren en wat er eigenlijk gebeurt als deze wordt uitgevoerd. Tot nu toe hebben we Nmap op een heel eenvoudige manier gebruikt, zonder echt te beslissen welke poorten we gaan scannen, maar dat gaat nu veranderen!



### IV. Verfijn het scannen van poorten met Nmap



#### A. Herinnering aan het standaardgedrag van Nmap



Zoals we hebben gezien, kiest Nmap zelf het aantal en de poorten om te scannen als je geen opties opgeeft. Dit is de "standaard" configuratie die Nmap gebruikt als je het niet precies vertelt wat het moet doen. Deze standaardopties zijn ontworpen om een idee te geven van de belangrijkste poorten die worden blootgesteld, deze worden geselecteerd op frequentie van blootstelling (meest voorkomende of frequente poorten) in plaats van in numerieke volgorde (poort 1, 2, 3, enz.) en ook om te voorkomen dat een scan van de 65535 mogelijke poorten wordt gestart als je niet de juiste opties opgeeft, wat te lang en te veel woorden zou zijn voor een "standaard" gebruikssituatie.



**Hoe worden deze poorten gekozen?



De 1000 poorten die in de standaardmodus worden gescand, worden gekozen op basis van hoe vaak ze voorkomen. Deze statistieken worden onderhouden door Nmap en bijgewerkt op dezelfde manier als de binary zelf en zijn scripts (modules). Je kunt deze statistieken zelf bekijken in het bestand "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



uitgepakt uit het bestand "/usr/shares/nmap/nmap-services"._



Hier, in de derde kolom, zien we wat lijkt op waarschijnlijkheden (tussen 0 en 1) of een procentuele verdeling. Dit is de frequentie waarmee elk poort/protocol paar voorkomt. We kunnen zien dat de bekendste poorten (FTP, SSH, TELNET en SMTP in dit extract) een veel hogere waarde hebben dan de andere.



#### B. Precies doelpoorten opgeven voor een Nmap-scan



In de echte wereld kan het echter nodig zijn om alleen een specifieke poort te scannen, of meerdere poorten, of een specifiek bereik van poorten. Nmap maakt het makkelijk om precies dat te doen, op een uniforme manier voor zowel UDP als TCP scans.



**Scan een specifieke poort via Nmap**



Als we een enkele poort willen scannen, en niet 1000, dan kunnen we deze poort specificeren via Nmap's "-p" of "--port" optie:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Als gevolg hiervan zal de scan natuurlijk veel sneller gaan en zal Nmap alleen de pakketten uitzenden die nodig zijn om te detecteren of de host actief is en vervolgens of de gespecificeerde poort bereikbaar is. Dit bespaart tijd als je een snelle test wilt uitvoeren om te zien of de webservice op je showcase site nog steeds actief is.



**Scan meerdere poorten via Nmap**



Op dezelfde manier kunnen we meerdere poorten naar Nmap specificeren, door dezelfde optie te gebruiken en de gespecificeerde poorten aan elkaar te koppelen met een komma:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Ongeacht de volgorde, zal Nmap al deze poorten controleren, en alleen die op de doelhost. U zult merken in de uitvoer van Nmap dat het **expliciet alle poorten en hun status** vertelt, zelfs als ze "gesloten" zijn. In tegenstelling tot het standaard gedrag, waar deze complete uitvoer veel te veel ruimte in beslag zou nemen:



![nmap-image](assets/fr/24.webp)



*Resultaat van een Nmap TCP-scan op de aangegeven poorten.*



**Scan een reeks poorten



Als het aantal poorten dat je wilt scannen te groot is, kun je ze per bereik opgeven, bijvoorbeeld:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Natuurlijk kun je naar eigen inzicht mixen en matchen, bijvoorbeeld:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**TCP- en UDP-poort scannen



Je kunt ook tegelijkertijd UDP- en TCP-scans uitvoeren op geselecteerde poorten:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Je zult in dit laatste voorbeeld de aanwezigheid van "U:" opmerken om een UDP poort aan te geven en "T:" om een TCP poort aan te geven. Hier is een mogelijke uitvoer van dit type scan:



![nmap-image](assets/fr/25.webp)



*Resultaat van een TCP- en UDP-poortscan met Nmap.*



Dat is nog eens een interessante manier om je scans aan te passen!



**Scan alle poorten



Tenslotte is het mogelijk om veel grotere of kleinere bereiken aan Nmap te geven. We hebben gezien dat de standaardlijst die Nmap selecteert 1000 poorten bevat. We kunnen ook vragen om de top 100 meest voorkomende poorten, of de top 200, met de optie "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Tenslotte kunnen we het vragen om alle mogelijke poorten te scannen (alle 65535), met de "-p-" notatie:



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Dit laatste zal langer duren, vooral met UDP, maar je zult er zeker van zijn dat je geen open poorten mist.



*Opmerking: De optie "-p-" is de aanbevolen methode voor het scannen van alle TCP-poorten. Voor UDP scans is het raadzaam om het aantal poorten te beperken om prestatieredenen, omdat complete scans van alle UDP poorten erg lang kunnen duren.*



Later in de tutorial zullen we zien hoe we de snelheid van Nmap scans kunnen optimaliseren voor onze behoeften, wat vooral handig zal zijn voor scans op alle TCP en UDP poorten.



### V. Conclusie



In dit gedeelte hebben we eindelijk wat praktijkervaring opgedaan, zodat we nu weten **hoe we Nmap op een eenvoudige manier kunnen gebruiken om de TCP- en UDP-poorten van een host te scannen**. We hebben ook in detail gekeken naar wat er gebeurt op netwerkniveau en **hoe Nmap bepaalt of een TCP of UDP poort actief is of niet**. Tot slot weten we hoe we de poorten die we willen scannen fijn moeten selecteren en **wat de standaardopties van Nmap eigenlijk doen**. In wat volgt zullen we deze kennis hergebruiken en toepassen op het scannen van een heel netwerk, inclusief global mapping en network discovery.




## 5 - Netwerk in kaart brengen en ontdekken met Nmap



### I. Presentatie



In dit gedeelte leren we hoe we het Nmap netwerk scan programma kunnen gebruiken om je netwerk in kaart te brengen. We zullen zien hoe effectief het kan zijn in deze taak, door middel van de verschillende opties. Tot slot bekijken we verschillende manieren om de doelen van onze scans aan Nmap op te geven.



In het bijzonder zullen we gebruik maken van wat we in de vorige sectie hebben geleerd over hoe Nmap bepaalt of een host actief en bereikbaar is.



Zoals vermeld in de inleiding van Nmap, is dit een Network Mapper. Als zodanig is het de perfecte tool voor het opstellen van een lijst van toegankelijke hosts op een netwerk, lokaal of op afstand.



**Terugkeer van de auteur:**



Als cyberbeveiligingsauditor en pentester gebruik ik Nmap systematisch bij het uitvoeren van interne penetratietests om uit te zoeken waar ik ben, wie mijn buren zijn op het lokale netwerk en welke andere netwerken toegankelijk zijn, evenals de systemen die zich daarop bevinden. Mijn doel is eenvoudig: het netwerk in kaart brengen, de omvang van het informatiesysteem bepalen en vooral het aanvalsoppervlak ervan schetsen.



Het in kaart brengen van netwerken kan ook nuttig zijn in het kader van netwerkdiagnostiek, toezicht, het in kaart brengen van bedrijfsmiddelen (weet je echt zeker dat je IS alleen bestaat uit wat er in de Active Directory of in je GLPI/OCS Inventory staat? Het kan ook worden gebruikt om de aanwezigheid van schaduw-IT in je informatiesysteem op te sporen.



### II. Nmap gebruiken om een netwerkbereik te scannen



#### A. Een netwerk ontdekken met een Nmap-scan



We willen nu naar een hogere versnelling schakelen en ons hele lokale netwerk analyseren. Niets is eenvoudiger: we hoeven alleen maar de commando's uit de vorige sectie te hergebruiken, maar dan met een CIDR in plaats van een eenvoudig IP Address.



Een CIDR (**Classless Inter Domain Routing**) is de "klassieke" notatie voor het specificeren van een netwerkbereik en de omvang ervan (met behulp van het masker). 192.168.0.0/24" is bijvoorbeeld een "vertaling" van de decimale maskernotatie "255.255.255.0".



Om Nmap te gebruiken door een CIDR op te geven, kunnen we het als volgt gebruiken:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Het is ook mogelijk om, net als bij poorten in de vorige sectie, meerdere hosts, meerdere netwerken of een bereik op te geven:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Hier is een voorbeeld van de resultaten die we zouden kunnen krijgen bij het uitvoeren van een scan op een netwerk:



![nmap-image](assets/fr/26.webp)



resultaten van een Nmap-scan om verschillende netwerken in kaart te brengen



In het bijzonder zien we verschillende actieve hosts en elke hostsectie begint met een regel als deze:



```
Nmap scan report for <name> (<IP>)
```



Hierdoor kunnen we duidelijk zien naar welke host de volgende resultaten verwijzen. De allerlaatste regel is ook belangrijk:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



We weten dat Nmap op de gescande netwerken 5 actieve hosts ontdekte.



#### B. Onder de motorkap: netwerkanalyse via Wireshark



We gaan nu nader bekijken wat er op netwerkniveau gebeurt tijdens een netwerkdetectie via Nmap.



Zoals we in de vorige sectie zagen, zal Nmap standaard het ARP protocol gebruiken om de aanwezigheid van hosts op het lokale netwerk te detecteren:



![nmap-image](assets/fr/27.webp)



aRP-pakketten vastgelegd tijdens het scannen van een lokaal netwerk met Nmap en de standaardopties ervan



Het is dus in staat om vrijwel alle hosts op het lokale netwerk te detecteren, omdat het antwoord op een ARP-verzoek over het algemeen door alle hosts die actief zijn op het netwerk wordt gegeven en er op geen enkele manier verdacht uitziet.



Voor netwerken op afstand gebruikt Nmap een combinatie van technieken:



![nmap-image](assets/fr/28.webp)



iCMP- en TCP-pakketten die worden vastgelegd tijdens het scannen van een netwerk op afstand met Nmap en de standaardopties ervan



Om precies te zijn gebruikt Nmap een ICMP echo pakket (het klassieke geval van pingen) en een ICMP Timestamp pakket, meestal gebruikt om de transittijd van pakketten te berekenen. Het hoopt een antwoord te krijgen van hosts op netwerken op afstand.



Maar er is meer aan de hand. Je kunt in de Wireshark capture hierboven zien dat **TCP SYN** pakketten systematisch worden verzonden op TCP/443 poorten van elke potentiële host op de te scannen netwerken, evenals **TCP ACK** pakketten op TCP/80 poorten.



**Waarom TCP pakketten naar poorten sturen als onderdeel van netwerkontdekking?



Door een SYN pakket naar een gegeven poort te sturen, kan Nmap **bepalen of er een service op die poort luistert**. Als een host antwoordt op een SYN pakket met een SYN/ACK pakket, geeft dit aan dat het actief is en dat er een service luistert op die poort. Nmap probeert daarom zijn geluk op deze service, **zelfs als er geen antwoord op de ping is verkregen**.



Door een ACK pakket naar een bepaalde poort te sturen, kan Nmap **bepalen of er een firewall aanwezig is op die host**. Als een host antwoordt op een ACK pakket met een RST (Reset) pakket, dan geeft dit aan dat er waarschijnlijk een firewall aanwezig is op die host die ongevraagd verkeer blokkeert. De host verraadt dus zijn aanwezigheid op het netwerk, zelfs als hij niet op andere verzoeken heeft gereageerd.



Het is echter belangrijk om op te merken dat firewall detectie met behulp van deze techniek niet in alle gevallen perfect betrouwbaar is. Sommige hosts kunnen generate RST antwoorden om andere redenen dan de aanwezigheid van een firewall, zoals een specifieke dienst of besturingssysteemconfiguratie. Bovendien kunnen moderne firewalls geconfigureerd worden om niet te reageren op detectiepogingen van dit type.



We hebben nu een lange weg afgelegd en kunnen een basis netwerk ontdekken. We gaan nu een paar opties bekijken die ons meer controle geven over het gedrag van Nmap.



### III. Netwerk ontdekken zonder poorten te scannen met Nmap



Zoals je misschien hebt gemerkt, voert Nmap standaard **een poortscan uit na het ontdekken van een actieve host**, wat een enorme hoeveelheid pakketten en wachten op antwoorden toevoegt aan onze scan. Als je 5 hosts op je netwerk hebt, zal Nmap proberen de status van ongeveer 5.000 poorten te controleren, wat langer zal duren.



Het is echter mogelijk om de opties van Nmap te gebruiken om **alleen een ontdekking van actieve hosts** op een netwerk uit te voeren, zonder hun diensten te ontdekken.



Als we alleen willen weten welke hosts bereikbaar zijn, zonder informatie over de diensten en poorten die ze aanbieden, dan kunnen we de optie "-sn" gebruiken om **alleen een scan uit te voeren met ICMP Echo (ping) en ARP-verzoeken**. Met andere woorden, schakel het scannen van poorten helemaal uit:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Hier is het resultaat van een Nmap netwerk ontdekking uitgevoerd zonder het scannen van poorten:



![nmap-image](assets/fr/29.webp)



Resultaat van een netwerkontdekking zonder poorten te scannen met Nmap.



We hebben het al gehad over de mogelijke beperkingen van het gebruik van ICMP alleen voor het vinden van hosts (voor netwerken op afstand). Daarom gebruikt Nmap ook een paar trucs die de aanwezigheid van een firewall of specifieke dienst op hosts kunnen verraden. Met behulp van opties kunnen we deze trucs hergebruiken en zelfs uitbreiden, zonder opnieuw te hoeven beginnen met een complete poortscan van elke ontdekte host.



Om dit te doen, gebruiken we de opties "-PS" (TCP SYN) en "-PA" (TCP ACK), waarmee we de poorten kunnen specificeren die we willen gebruiken als onderdeel van onze host discovery, evenals de optie "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Deze scan zorgt er al voor dat de hostontdekking iets completer is dan met de standaardopties.



We beginnen behoorlijk uitgebreide commando's te krijgen, waarbij we meerdere opties gebruiken. Dit komt omdat we weten hoe Nmap werkt en wat de beperkingen zijn van de "standaard" opties, waardoor we soms tijd verliezen of belangrijke Elements missen. Dat is het hele punt van de tijd nemen om het onder de knie te krijgen!



De opties van onze laatste bestelling beschrijven:





- "`-sn`: schakelt het scannen van poorten uit voor elke actieve host die door Nmap is ontdekt.





- "`-PP`: Schakelt ICMP-echo (ping-scan) in voor het ontdekken van hosts.





- "`-PS <PORT>`": stuur een TCP SYN pakket op de aangegeven poort(en) om een actieve dienst te detecteren die de aanwezigheid van een host verraadt die niet heeft gereageerd op de ping.





- "`-PA <PORT>`": stuur een TCP ACK pakket op de aangegeven poort(en) om een actieve firewall te detecteren die de aanwezigheid van een host verraadt die niet heeft gereageerd op de ping.




In het bovenstaande voorbeeld geef ik voor de "-PS" optie de poorten op die volgens mij het meest worden blootgesteld in mijn Nmap contexten. Deze verschillende poorten worden dan op elke host getest, niet om te zien of de service die ze hosten echt actief is, maar om te zien of dit ons in staat stelt om een host te ontdekken die niet heeft gereageerd op onze ICMP Echo terwijl hij nog steeds actief is (via een antwoord van de service of de firewall van de host).



Dit is wat er te zien is in een netwerk capture genomen op het moment van zo'n scan, in dit geval een extract op een enkele doelhost:



![nmap-image](assets/fr/30.webp)



pakketten verzonden door Nmap tijdens geavanceerde netwerkdetectie, zonder scannen van poorten



We vinden onze TCP SYN pakketten, onze TCP ACK op poort TCP/80 en onze ICMP echo. Nmap voert al deze tests uit voor elke host die het doelwit is van onze netwerkzoekscan.



### IV. Een bestand met bedrijfsmiddelen gebruiken om te targeten met Nmap



Het specificeren van doelen kan al snel complex blijken in echte informatiesystemen, die soms uit tientallen of honderden netwerken, subnetten en VLAN's kunnen bestaan. Daarom is het eenvoudiger om een bestand als bron voor Nmap te gebruiken dan om ze een voor een op de commandoregel te specificeren.



Maak om te beginnen een eenvoudig bestand met één invoer per regel:



![nmap-image](assets/fr/31.webp)



bestand met één doel (host of netwerk) per regel



Vervolgens kunnen we alle Nmap opties gebruiken die we tot nu toe hebben gezien en de "-iL <pad/bestand>" optie specificeren:



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap zal dan alle doelen in ons bestand in de scan opnemen.



Als je er zeker van wilt zijn dat al je doelen worden meegenomen, kun je de optie "-sL -n" gebruiken. Nmap zal dan alleen de CIDR's en hosts in het bestand interpreteren en aan je tonen, zonder pakketten over het netwerk te sturen:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Dit zorgt ervoor dat de lijst met te scannen hosts accuraat is.



Een laatste belangrijke tip die ik met jullie wil delen betreft **host of netwerk uitsluiten als onderdeel van een scan**. De noodzaak om een host uit te sluiten kan in een aantal gevallen nodig zijn, vooral als we er zeker van willen zijn dat **een gevoelig onderdeel van het informatiesysteem niet wordt verstoord of verstoord door onze scans**.



Veel voorkomende voorbeelden van dergelijke behoeften zijn wanneer een bedrijf industriële (PLC) of gezondheidszorgapparatuur bezit. Dergelijke apparatuur is soms slecht ontworpen en helemaal niet bedoeld om slecht geformatteerde pakketten, of te veel pakketten, te ontvangen. Om voor de hand liggende redenen van beschikbaarheid of bedrijfs-/mensenrisico is het beter om ze uit te sluiten van testen.



Om IP-adressen of netwerken uit te sluiten van onze scan, kunnen we de optie "--exclude" van Nmap gebruiken, bijvoorbeeld:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



In dit voorbeeld scan ik het netwerk "192.168.1.0/24" maar sluit ik de host "192.168.1.140" die zich daar bevindt uit. Nmap zal geen pakketten naar deze host sturen. Een ander voorbeeld met subnet uitsluiting:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Op dezelfde manier scan ik het grote netwerk "10.0.0.0/16", maar het netwerk "10.0.100.0/24" wordt niet gescand. Nogmaals, ik raad aan om de "-sL -n" optie te gebruiken om een heel duidelijk beeld te krijgen van welke hosts gescand zullen worden en welke uitgesloten zullen worden van de scan, vooral als je in een gevoelige context werkt.



### V. Netwerkontdekking en poortscannen



We kunnen nu combineren wat we in deze sectie hebben geleerd met wat we in de vorige sectie hebben geleerd over poortscan opties. We hebben gezien dat Nmap standaard de 1000 meest voorkomende poorten scant op elke actieve host die het ontdekt. We hebben gezien hoe we dit gedrag kunnen voorkomen als we het niet willen, maar we kunnen het volledig controleren en zelfs uitbreiden als het aan onze behoeften voldoet.



Het volgende commando controleert bijvoorbeeld op de aanwezigheid van een luisterende service op poort TCP/22 op elke gescande host:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap zal eerst een netwerkzoektocht uitvoeren om de actieve hosts op te sommen en voor elk van hen controleren of er een service aanwezig is op poort TCP/22.



Op dezelfde manier kunnen we een volledige scan uitvoeren van alle TCP poorten op elke host die ontdekt is op het "192.168.0.0/24" netwerk, met uitzondering van host "192.168.0.4" bijvoorbeeld:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Je bent vrij om alle opties die we tot nu toe hebben geleerd te combineren om aan je eigen behoeften te voldoen.



### VI. Conclusie



In dit gedeelte hebben we gezien hoe we Nmap kunnen gebruiken om het netwerk in kaart te brengen met verschillende opties. We hebben nu een verfijnd begrip van de doelen van onze scans, evenals Nmap's poortscan gedrag en host discovery methode. En het belangrijkste, we weten wat het standaard gedrag en de beperkingen van Nmap zijn en hoe we de belangrijkste opties kunnen gebruiken om verder te gaan.



In de volgende sectie zullen we kijken naar de mechanismen en opties voor het ontdekken van de versies van services en besturingssystemen die door Nmap worden gescand.




## 6 - Service- en besturingssysteemversies detecteren met Nmap



### I. Presentatie



In dit gedeelte leren we hoe we Nmap kunnen gebruiken om de versies van services en besturingssystemen die door gescande hosts worden gebruikt te ontdekken en nauwkeurig te detecteren. We zullen in detail bekijken hoe Nmap deze taak volbrengt en wat de beperkingen van de tool zijn om de resultaten beter te begrijpen en te interpreteren.



Zoals we in de vorige secties van deze tutorial hebben gezien, kijkt Nmap standaard niet welke service is blootgesteld op de poorten die het scant en als open beschouwt. Dus als je luistert naar een webservice op poort TCP/22, zal Nmap deze blijven rapporteren als open, maar als een `SSH` service. Dit komt omdat het een [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) lokaal op je systeem gebruikt om te zoeken naar een relatie tussen een poort/protocol en de naam van een service (het `/etc/services/` bestand).



In de meeste gevallen zal [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) je de juiste informatie geven, omdat het in een productieomgeving zeldzaam is om zulke gevallen te vinden. De resterende gevallen zullen echter situaties zijn waar een klassieke dienst ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, enz.) wordt blootgesteld op een niet-klassieke poort (bijvoorbeeld 2022 voor een SSH dienst), in welk geval Nmap geen overeenkomst zal vinden in zijn lokale database, of een die niet overeenkomt met de werkelijkheid, en je belangrijke informatie zult missen.



Gelukkig biedt Nmap zeer nauwkeurige opties en mechanismen om te ontdekken welke exacte service zich achter een open poort verbergt. Het heeft zelfs een database met queries en handtekeningen om exacte technologieën en versies te identificeren. Naast services kan Nmap ook de gebruikte technologie en de versie ervan identificeren.



Dat is waar we in dit gedeelte naar zullen kijken.



### II. Hoe een technologie of versie detecteren



#### A. Herinnering aan hoe je een technologie of versie identificeert



Om een technologie en een versie te identificeren, moet de naam van de service, CMS, applicatie of software die op de beoogde poort luistert, worden achterhaald. Een webpagina wordt bijvoorbeeld beheerd door een CMS (`WordPress`), uitgevoerd door een webservice (`Apache`, IIS, Nginx) en gehost door een server (Linux of Windows). Maar hoe weet je welke webservice draait?



De klassieke methode om deze informatie te achterhalen is _banner grabbing_, wat simpelweg bestaat uit het lokaliseren waar de dienst in kwestie deze informatie weergeeft en de gegevens lezen. Heel vaak, in hun standaardconfiguratie of verwerking, tonen services hun naam en zelfs hun versie als de eerste reactie na een verbinding.



![nmap-image](assets/fr/32.webp)



een versie weergeven zodra een TCP-verbinding wordt gemaakt door een FTP-service



Hier zien we dat een eenvoudige TCP-verbinding met deze service via `telnet` resulteert in een TCP-pakket dat de technologie en versie bevat.



Als je eenmaal een idee hebt met wat voor soort service je te maken hebt, kun je ook specifieke commando's of verzoeken naar die service sturen om er informatie uit te halen. Deze verzoeken/commando's kunnen ook blindelings worden verstuurd (zonder er zeker van te zijn dat het om het juiste type service gaat), in de hoop dat één ervan een reactie van de service in kwestie zal uitlokken.



In andere, meer geavanceerde gevallen is het nodig om specifieke pakketten te versturen om een reactie te veroorzaken, zoals een foutmelding, die gedetailleerde informatie geeft over de gebruikte versie of technologie.



Zoals je je kunt voorstellen, zal Nmap al deze technieken gebruiken om te proberen het exacte type dienst dat op een poort wordt gehost te identificeren, evenals de naam van de technologie en de versie.



#### B. Nmap controleregels en matches begrijpen



Om al deze controles op elke gescande poort uit te voeren, gebruikt Nmap een lokale database die regelmatig wordt bijgewerkt (net als de binary of zijn modules). Dit is een tekstbestand van enkele duizenden regels: `/usr/share/nmap/nmap-service-probes`.



Dit bestand bestaat uit talloze items, allemaal georganiseerd rond twee belangrijke richtlijnen:





- De `Probe`: dit is de definitie van het pakket dat Nmap zal sturen in een poging een reactie uit te lokken van de te identificeren dienst. Zie het als een blinde poging zoals _Hello? Guten Tag? Hallo? Um... Buenos Dias misschien?_. Zodra de doeldienst een probe ontvangt die het begrijpt (d.w.z. het juiste protocol spreekt), zal het reageren naar Nmap, die dan bevestiging heeft van het type dienst dat het is.





- Match": dit zijn reguliere expressies die Nmap toepast op het verkregen antwoord. Als het versturen van een HTTP GET verzoek een antwoord van de service heeft uitgelokt, zal het tientallen reguliere expressies toepassen op dit antwoord om de aanwezigheid van bijvoorbeeld het woord `Apache`, `Nginx`, `Microsoft IIS`, enz. te identificeren.




Er zijn een paar andere directives voor specifieke gevallen, maar de belangrijkste om te begrijpen hoe Nmap werkt en het gebruik ervan aan te passen zijn deze. Om dit theoriegedeelte concreter te maken, is hier een voorbeeld:



![nmap-image](assets/fr/33.webp)



voorbeeld van een Probe in Nmap's `/usr/share/nmap/nmap-service-probes` bestand



In de eerste regel van dit voorbeeld zien we een eenvoudig te begrijpen Probe met de naam `GetRequest`. Dit is een TCP pakket dat een leeg HTTP GET verzoek naar de webservice root bevat met HTTP/1.0, gevolgd door een line feed en een lege regel.



De `ports` regel vertelt Nmap naar welke poort deze Probe gestuurd moet worden. Hiermee kun je tests prioriteren en tijd besparen.



Tot slot hebben we twee voorbeelden van `match`. De eerste zal bijvoorbeeld de gescande webservice categoriseren als `ajp13` als de reguliere expressie in deze regel overeenkomt met het ontvangen serviceantwoord.



Om je te helpen begrijpen hoe Probes eruit kunnen zien, is hier een lijst van enkele Probes die je in dit bestand kunt vinden (er zijn er 188 op het moment dat ik deze tutorial schrijf).



![nmap-image](assets/fr/34.webp)



voorbeeld van verschillende Probes die door Nmap worden gebruikt en aanwezig zijn in het bestand `/usr/share/nmap/nmap-service-probes`._



De eerste twee (genaamd `NULL` en `GenericLines`) zijn hier van bijzonder belang, omdat ze simpelweg een leeg TCP pakket sturen of een pakket dat een regeleinde bevat. Server diensten kondigen zichzelf vaak precies aan zodra een verbinding wordt ontvangen, zonder een specifieke actie, commando of verzoek van de client.



Hier is het geval van een iets complexere _match_:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



De exacte reguliere expressie staat hier tussen de `m|` en de `|`, die elke reguliere expressie in dit bestand afbakent. Neem de tijd om dit hele voorbeeld te lezen. Je zult een selectie zien in de reguliere expressie: `([\d.]+)`, gebruikt om een versie te isoleren. Dit voorbeeld definieert ook andere Elements zoals de productnaam `p/nginx/`, de opgehaalde versie `v/$1/` en de CPE met versie `cpe:/a:igor_sysoev:nginx:$1/`.



Een CPE (Common Platform Enumeration) is een gestandaardiseerd notatiesysteem dat wordt gebruikt om software en hardware te identificeren en te beschrijven. Dit formaat maakt een efficiënter beheer van kwetsbaarheden en beveiligingsconfiguraties mogelijk, en vooral een uniforme manier om ze weer te geven, ongeacht het product in kwestie. Hier zijn twee voorbeelden van CPE: `cpe:/o:microsoft:windows_8.1:r1` en `cpe:/a:apache:http_server:2.4.35`



Hier identificeren we duidelijk hun types `o` voor OS, `a` voor applicatie, leverancier, product en versies.



Dus, in het geval van een _match_ met een van deze reguliere expressies, zullen we niet alleen de naam van de service ophalen, maar ook de versie en exacte CPE, wat het makkelijker maakt om CVE's te vinden die deze versie beïnvloeden. Je vindt deze informatie in de standaard uitvoer van Nmap en je zult zien dat het erg nuttig is voor andere doeleinden die we in een paar secties zullen behandelen.



De exacte syntaxis van _matches_ en, meer in het algemeen, van de directives in het `/usr/share/nmap/nmap-service-probes` bestand stopt daar niet, en kan vrij complex lijken als je niet gewend bent om Nmap en zijn resultaten te manipuleren. Je zou echter op zijn minst het bestaan en de algemene werking ervan moeten onthouden, wat later van pas kan komen als je een resultaat wilt begrijpen of debuggen, een scan wilt aanpassen of zelfs wilt bijdragen aan de ontwikkeling van Nmap.



### III. Nmap gebruiken om versies te detecteren



Nu gaan we al deze complexe _Probe_ en _Match_ mechanica gebruiken via een simpele optie: `-sV`. Dit vertelt Nmap simpelweg: probeer precies uit te vinden welke services en versies van poorten je als open hebt ingesteld.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Hier is een compleet voorbeeld van het resultaat van een dergelijk commando:



![nmap-image](assets/fr/35.webp)



resultaten van Nmap's versiedetectie van applicaties die zijn blootgesteld op het netwerk



Hier kunnen we zien dat Nmap erin geslaagd is om alle versies van netwerkservices te identificeren die door dit doelwit worden aangeboden, en deze informatie weergeeft in een nieuwe `VERSIE` kolom. Het is mogelijk om vrij precieze informatie te zien, zelfs tot op het besturingssysteem, als deze informatie onderdeel is van de herstelde handtekening.



Om in detail te begrijpen wat er gebeurt tijdens een kwetsbaarheidsscan, kunnen we de `--version-trace` optie gebruiken. Dit geeft een debug-modus weer, die de _Probe_ toont die tot de detectie heeft geleid:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Als gevolg daarvan hebben we veel informatie om te sorteren. Probeer regels te vinden die beginnen met `Service scan Hard match`. Je ziet dan regels als deze:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



We kunnen duidelijk zien welke _Probes_ werden gebruikt om de technologie en versie te detecteren (in dit geval de `NULL` en `GetRequest` _Probes_), evenals de opgehaalde informatie.



### IV. Testen en detectienauwkeurigheid beheersen



We gaan nu terug naar een richtlijn in het `/usr/share/nmap/nmap-service-probes` bestand waar we eerder niet naar hebben gekeken:



![nmap-image](assets/fr/36.webp)



probes `rarity` richtlijn in het `/usr/share/nmap/nmap-service-probes`._ bestand



Deze richtlijn wordt gebruikt om de zeldzaamheid (d.w.z. prioriteit/waarschijnlijkheid) van een _Probe_ aan te geven. Met deze notatie van 1 tot 9 kun je de volledigheid van de analyse controleren die Nmap uitvoert bij het verzenden van _Probes_. In het "notatiesysteem" van Nmap geeft een zeldzaamheid van 1 informatie in de overgrote meerderheid van de gevallen, terwijl een zeldzaamheid van 8 of 9 een heel speciaal geval vertegenwoordigt, specifiek voor een configuratie of service die zelden voorkomt.



Om duidelijker te zijn, in het standaardgeval stuurt Nmap naar elke dienst die geïdentificeerd moet worden de _Probes_ die een zeldzaamheid hebben van 1 tot 7. Om je een beter idee te geven van de verdeling van _Probes_ per _rariteit_, zie je hier hun aantal:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Het lijkt misschien contra-intuïtief, maar er zijn meer `rariteit` 8 en 9 dan de rest. Dit is juist omdat Probes van zeldzaamheid 1 generiek zijn en in de meeste gevallen werken, ongeacht de service (denk aan de `NULL` Probe die simpelweg een leeg TCP pakket stuurt). Terwijl de meer complexe Probes bijna uniek zijn per service.



Als we de controleregels die we in onze versiescan willen gebruiken handmatig willen beheren, kunnen we de `--version-intensity` optie gebruiken. Hier zijn twee voorbeelden:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Om dit onderwerp af te sluiten, is hier een voorbeeld van _Probe_ 9 en 8:



![nmap-image](assets/fr/37.webp)



voorbeelden van sonde bij zeldzaamheid 8 en 9 in het bestand `/usr/share/nmap/nmap-service-probes`._



Deze twee _Probes_ detecteren Quake1 en Quake2 servers (het videospel). Interessant voor de nostalgische kant, maar waarschijnlijk niet van veel nut in het dagelijks leven.



Afhankelijk van je behoefte aan precisie of snelheid, moet je onthouden dat dit `rariteitsprincipe` bestaat en het resultaat kan beïnvloeden.



### V. Nmap gebruiken om besturingssystemen te detecteren



We zullen nu bekijken hoe Nmap ons kan helpen bij het detecteren van de besturingssystemen van hosts die gescand en gedetecteerd zijn op een netwerk. Om dit te doen, gebruik je de `-O` (voor `OS Scan`) optie van Nmap.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Hier is een voorbeeld van de resultaten. Hier vertelt Nmap ons dat het waarschijnlijk een Linux OS is en geeft ons verschillende statistieken over de exacte versie.



![nmap-image](assets/fr/38.webp)



detectie van de waarschijnlijkheid van identificatie van een besturingssysteem door Nmap



Om dit te bereiken, zal Nmap een groot aantal technieken gebruiken die op een vergelijkbare manier werken als _Probes_ en _Matches_ voor technologie- en versiedetectie. Het belangrijkste verschil is dat Nmap vrij "low-level" parameters van ICMP, TCP, UDP en andere protocollen zal gebruiken. Hier zijn twee testvoorbeelden voor het detecteren van een Microsoft Windows 11-besturingssysteem:



![nmap-image](assets/fr/39.webp)



voorbeelden van tests uitgevoerd door Nmap om een Windows 11 OS te detecteren



Laten we eerlijk zijn, deze tests zijn erg moeilijk te interpreteren en we gaan niet proberen om ze diepgaand te begrijpen in de context van een inleidende Nmap tutorial. Als je dieper op het onderwerp wilt ingaan, is het bestand met deze informatie `/usr/share/nmap/nmap-os-db`.



Je moet je er echter van bewust zijn dat OS-detectie meer een waarschijnlijkheid is die door Nmap is vastgesteld dan een zekerheid.



### VI. Conclusie



In dit gedeelte hebben we geleerd hoe we de opties van Nmap kunnen gebruiken om de technologieën, versies en besturingssystemen van gescande hosts en services te detecteren. We hebben nu een goed begrip van hoe Nmap deze informatie op afstand verkrijgt. We hebben ook de opties voor het beheren van verbositeit en testnauwkeurigheid bekeken, evenals de beperkingen van de tool op deze onderwerpen.



In de volgende sectie leren we hoe we de NSE scripts van Nmap kunnen gebruiken om een beveiligingsanalyse van ons informatiesysteem uit te voeren. Neem de tijd om de laatste secties te herlezen als dat nodig is, en aarzel niet om zelf te oefenen en in de ingewanden van de tool te duiken om beter onder de knie te krijgen wat we tot nu toe hebben geleerd.




## 7 - Beveiligingsanalyse: kwetsbaarheden detecteren



### I. Presentatie



In dit gedeelte leren we hoe we het Nmap netwerk scan programma kunnen gebruiken om kwetsbaarheden op de doelen van onze scans te detecteren en analyseren. In het bijzonder bekijken we de verschillende opties die beschikbaar zijn om deze taak uit te voeren en bestuderen we de grenzen van de mogelijkheden van het hulpprogramma om de resultaten beter te begrijpen en te interpreteren.



In dit eerste deel bekijken we de kwetsbaarhedenscanner van Nmap en bekijken we hoe we de basisopties voor het detecteren van kwetsbaarheden kunnen gebruiken. In de volgende secties gaan we dieper in op hoe deze functie werkt en hoe deze kan worden aangepast.



### II. Nmap gebruiken om kwetsbaarheden op te sporen



We willen nu de Nmap netwerkscanner gebruiken om kwetsbaarheden op te sporen in de diensten en systemen van ons informatiesysteem. Dit betekent dat Nmap, naast het ontdekken van actieve hosts, het opsommen van blootgestelde services en het detecteren van versies en technologieën, zal zoeken naar kwetsbaarheden.



Om dit te bereiken vertrouwt Nmap op NSE (_Nmap Scripting Engine_) scripts, die kunnen worden gezien als modules die een granulaire aanpak van testen mogelijk maken.



Met de juiste opties zullen we Nmap vragen om zijn verschillende NSE-scripts te gebruiken op elke ontdekte service, waardoor we:





- Configuratiefouten ;





- Extra en meer geavanceerde versie en OS ontdekkingen ;





- Bekende kwetsbaarheden (CVE's) ;





- Zwakke identificatoren ;





- Kenmerkende Elements van een malware-infectie ;





- Denial of service-mogelijkheden ;





- Enz.




Zoals je kunt zien, breiden NSE scripts de mogelijkheden van Nmap aanzienlijk uit wat betreft de netwerkbewerkingen die het kan uitvoeren. En dit om veel geavanceerdere taken uit te voeren dan ooit tevoren. Het goede nieuws is dat, zoals gebruikelijk, deze mogelijkheden eenvoudig kunnen worden gebruikt via een optie en in een standaardcontext. Dit is wat we hierna zullen zien.



### III. Voorbeeld van een kwetsbaarheidsscan



NSE scripts kunnen worden gebruikt wanneer Nmap wordt gebruikt om een enkele poort op een host te scannen, alle services op die host of alle services die op meerdere netwerken worden gedetecteerd. We kunnen de opties die we gaan zien dus gebruiken in alle contexten die we tot nu toe hebben bestudeerd.



Om het scannen op kwetsbaarheden in te schakelen via een Nmap scan, moeten we de `-sC` optie gebruiken:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Onthoud dat standaard, als je niets specificeert, Nmap alleen de 1000 meest voorkomende poorten zal scannen. Het zal geen kwetsbaarheden detecteren op de meer exotische poorten die je doelwitten kunnen blootstellen.



Voordat je deze functionaliteit gebruikt op een productie-informatiesysteem, nodig ik je uit om de tutorial verder te lezen. In de volgende secties bekijken we hoe we de impact en de soorten tests die worden uitgevoerd beter kunnen controleren.



Door te hergebruiken wat we eerder hebben geleerd, kunnen we bijvoorbeeld uitgebreider zijn en alle TCP-poorten van een doelwit scannen:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Hier is het resultaat van een Nmap-scan met NSE-scripts:



![nmap-image](assets/fr/40.webp)



voorbeeld van de resultaten van een kwetsbaarhedenscan op een host via Nmap._



Hier zien we de weergave van aanvullende informatie die van belang is in de context van een kwetsbaarheidsanalyse:





- De FTP service is anoniem toegankelijk en wordt niet beschermd door authenticatie. Het NSE-script dat deze verificatie uitvoert, vertelt ons dit en toont zelfs een deel van de boomstructuur van de FTP-service. Hier zien we dat we toegang hebben tot de `C` directory van het Windows systeem!





- Het NSE-script dat verantwoordelijk is voor het geavanceerd ophalen van webdiensten geeft de paginatitel weer, zodat we een beter idee krijgen van wat de webdienst host.





- We hebben ook een mini-analyse van de SMB-serviceconfiguratie (scripts `smb2-time`, `smb-security-mode` en `smb2-security-mode`). De informatie wordt een beetje anders weergegeven, na het resultaat van de netwerkscan, om het gemakkelijker leesbaar te maken. In het bijzonder geeft deze informatie de afwezigheid van SMB Exchange handtekeningen aan. Dit zwakke punt in de configuratie maakt het mogelijk om het doelwit te gebruiken in een SMB Relay aanval, een opmerkelijke beveiligingsfout die vaak wordt uitgebuit in inbraak/cyberaanval tests.




Dit is natuurlijk maar één voorbeeld. Nmap heeft NSE-scripts voor veel services, gericht op een breed scala aan kwetsbaarheden. In de volgende sectie gaan we dieper in op deze mogelijkheden.



Om deze inleiding tot het scannen op kwetsbaarheden af te ronden, volgt hier een compleet commando voor het ontdekken van netwerken, het scannen van TCP-poorten, versie- en kwetsbaarheidsdetectie:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Hier is een commando dat begint te lijken op meer realistische Nmap-gebruiksgevallen!



### IV. De beperkingen van Nmap bij het scannen op kwetsbaarheden begrijpen



Laten we duidelijk zijn: Nmap is niet in staat om een volledige penetratietest van je informatiesysteem uit te voeren of een Red Team operatie te simuleren. Het heeft verschillende beperkingen waar je je bewust van moet zijn om geen vals gevoel van veiligheid te krijgen:





- Beperkte dekking**: hoewel de NSE-scripts van Nmap krachtig zijn, kan hun testdekking beperkt zijn in vergelijking met andere gespecialiseerde tools voor het opsporen van kwetsbaarheden. Sommige kwetsbaarheden worden mogelijk niet gedekt door de beschikbare NSE-scripts, zoals kwetsbaarheden in Active Directory, blootstelling van gevoelige gegevens of meer geavanceerde gevallen van kwetsbare webapplicaties.





- Complexiteit van de kwetsbaarheid**: bepaalde soorten kwetsbaarheden kunnen moeilijk te detecteren zijn met NSE-scripts vanwege hun complexiteit. Bijvoorbeeld, kwetsbaarheden die complexe interactie vereisen met een service op afstand kunnen mogelijk niet effectief worden gedetecteerd door Nmap (zoals in het geval van overmatige toestemmingen in een bestandsdeling of een fout in de toestemmingscontrole van een webtoepassing).





- Passieve detectie**: Nmap richt zich voornamelijk op actieve scans om kwetsbaarheden te detecteren, wat betekent dat het potentiële kwetsbaarheden niet effectief kan detecteren zonder een actieve verbinding met de doelhosts tot stand te brengen. Kwetsbaarheden die zich niet manifesteren tijdens een actieve scan kunnen daarom worden gemist (zoals in het geval van een code-injectie in een webapplicatie).





- Afhankelijkheid van updates**: Nmap's [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) van NSE scripts is voortdurend in ontwikkeling, maar er kan een vertraging zitten tussen de ontdekking van een nieuwe kwetsbaarheid en de toevoeging van een bijbehorend script aan Nmap. Als gevolg daarvan is Nmap niet altijd up-to-date met de nieuwste kwetsbaarheden.





- Valse positieven en valse negatieven**: zoals bij elk beveiligingshulpmiddel kunnen de NSE-scripts van Nmap valse positieven (valse kwetsbaarheidswaarschuwingen) of valse negatieven (echte kwetsbaarheden die niet worden gedetecteerd) produceren. Dit is iets om in gedachten te houden bij het analyseren van Nmap resultaten.




Het is dus belangrijk om te begrijpen wat Nmap wel en niet doet, en ook om te weten hoe de resultaten geïnterpreteerd moeten worden. In het bijzonder hebben we in deze tutorial gezien dat standaardopties ertoe kunnen leiden dat we belangrijke Elements over het hoofd zien, die ontdekt kunnen worden met zorgvuldig gebruik.



Of je nu een netwerksysteembeheerder, een beveiligingsengineer of zelfs een CISO bent, het gebruik van Nmap geeft je een overzicht van de beveiligingsstatus van een informatiesysteem. Dit is een belangrijke eerste stap in het beveiligen van een systeem, die regelmatig kan worden uitgevoerd door het IT-team. Het mag echter niet in de plaats komen van de tussenkomst en het advies van [cybersecurity] experts (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), die veel uitgebreider zwakke plekken kunnen blootleggen dan Nmap.



### V. Conclusie



In dit eerste deel van module 3 hebben we het scannen op kwetsbaarheden via Nmap geïntroduceerd. We weten nu hoe we de hoofdoptie moeten gebruiken om deze taak uit te voeren, maar we kennen ook de grenzen van de oefening. In het volgende deel gaan we dieper in op deze functionaliteit en gebruiken we NSE-scripts om de kracht van Nmap te vertienvoudigen.



## 8 - De NSE-scripts van Nmap gebruiken



### I. Presentatie



In dit gedeelte gaan we dieper in op NSE (_Nmap Scripting Engine_) scripts. In het bijzonder bekijken we waarom ze een van de sterke punten van deze tool zijn, hoe ze werken en hoe je de vele bestaande scripts kunt doorzoeken en gebruiken.



Dit onderdeel is een vervolg op de vorige tutorial, waarin we hebben geleerd hoe we de functies van Nmap voor het scannen van kwetsbaarheden op een eenvoudige manier kunnen gebruiken. We gaan nu dieper in op hoe [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) in dit opzicht werkt, zodat we weer preciezere en meer gecontroleerde scans kunnen uitvoeren.



### II. Het concept van Nmap NSE-scripts



Met de NSE scripts van Nmap kun je de mogelijkheden op een zeer flexibele manier uitbreiden. Ze zijn geschreven in LUA, een scripttaal die eenvoudiger te hanteren en te gebruiken is dan de C of C# die Nmap gebruikt. Het voordeel van het gebruik van een LUA script met Nmap in plaats van een stand-alone tool is dat het ons in staat stelt om te profiteren van Nmap's snelheid van uitvoering en standaard functies (host, poort en versie ontdekking, etc.).



Deze scripts zijn gerangschikt per categorie, en één script kan tot meer dan één categorie behoren:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Technisch gezien worden de categorieën waartoe een script behoort direct in de code aangegeven.



![nmap-image](assets/fr/41.webp)



nSE script categorieën `ftp-anon`._



Dit voorbeeld toont een deel van de code van het NSE script `ftp-anon.nse`, waarvan we de uitvoering zagen in de vorige sectie.



### III. Lijst van bestaande NSE-scripts



Standaard staan de NSE scripts van Nmap in de `/usr/share/nmap/scripts/` directory, zonder specifieke boomstructuur of hiërarchie. Hier is een overzicht van de inhoud van deze map:



![nmap-image](assets/fr/42.webp)



haalt de inhoud uit de `/usr/share/nmap/scripts/` directory met NSE scripts._



Deze map bevat meer dan 5.000 NSE-scripts. In de meeste gevallen bevat het eerste deel van de scriptnaam het protocol of de categorie waartoe het behoort. Hierdoor kunnen we de lijst sorteren, bijvoorbeeld als we alle scripts willen weergeven die gericht zijn op de FTP-service:



![nmap-image](assets/fr/43.webp)



lijst van NSE Nmap scripts met namen die beginnen met `ftp-`._



Nmap biedt niet echt een optie om de NSE scripts te doorzoeken en op te sommen; je kunt het commando `-script-help` gebruiken gevolgd door de naam van een categorie of een woord:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



De uitvoer zal echter de naam van elk script en zijn beschrijving zijn, wat niet optimaal is als de zoekopdracht tientallen scripts oplevert:



![nmap-image](assets/fr/44.webp)



resultaat van het gebruik van het `-cript-help` commando van Nmap



Naar mijn mening is de meest effectieve methode het gebruik van de klassieke Linux commando's in de `/usr/share/nmap/scripts/` map:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Blader gerust door de code van de modules die u aanspreken om beter te begrijpen hoe een NSE-script werkt.



### IV. De NSE-scripts van Nmap gebruiken



Nu gaan we leren hoe we kwetsbaarheden kunnen scannen door zorgvuldig de NSE-scripts te selecteren waarin we geïnteresseerd zijn.



#### A. Scripts per categorie selecteren



Om te beginnen kunnen we ervoor kiezen om alle scripts uit te voeren die tot een specifieke categorie behoren. We moeten deze categorie of categorieën aangeven bij Nmap met het argument `--script <categorie>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Dit eerste commando is het equivalent van het `nmap -sC` commando. Standaard selecteert Nmap scripts in de `default` categorie, maar dat is alleen voor het argument. Het volgende commando zal bijvoorbeeld alle scripts in de `discovery` categorie gebruiken:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Zoals we hebben gezien, kunnen we met sommige categorieën snel identificeren wat de gerelateerde NSE-scripts doen (`discovery`, `vuln`, `exploit`), terwijl andere het risiconiveau, de detectie of de stabiliteit van de uitgevoerde test definiëren. Als we ons in een gevoelige context bevinden en geen goed inzicht hebben in de verschillende acties die door onze scriptselectie worden uitgevoerd, kunnen we ervoor kiezen om de selecties te combineren om alleen die scripts te kiezen die in de categorieën `discovery` en `safe` vallen:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Als je scripts absoluut en expliciet wilt uitsluiten van de `dos` en `intrusive` categorieën, kun je de volgende notatie gebruiken:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Merk op dat het specificeren van uitsluitingsvoorwaarden zoals hierboven zal resulteren in het gebruik van alle andere categorieën die niet expliciet zijn uitgesloten. Om eerlijker te zijn, zouden we bijvoorbeeld kunnen specificeren:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Hier zijn enkele voorbeelden van hoe om te gaan met NSE-scripts per categorie, vooral bij het gebruik van Nmap voor kwetsbaarhedenanalyse in een echte context.



#### B. Scripts als eenheid selecteren



We kunnen er ook voor kiezen om één specifieke test uit te voeren tijdens een analyse, een test die overeenkomt met een NSE-script. Hiervoor moeten we de naam van het script opgeven in de `-script <naam>` parameter. Als voorbeeld nemen we het `ftp-anon.nse` script:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



We hebben dan een zeer nauwkeurig resultaat:



![nmap-image](assets/fr/45.webp)



resultaat van het gebruik van het NSE `ftp-anon` script op een FTP poort via Nmap._



We zien het resultaat van het uitvoeren van het `ftp-anon` script op poort 21, en geen andere poort, omdat we de `-p 21` optie hebben opgegeven. We hadden ook een basis poortscan kunnen uitvoeren, waarbij het `ftp-anon` NSE script alleen op de ontdekte FTP services werd uitgevoerd:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Dus Nmap zou deze anonieme verbindingstest ook hebben uitgevoerd als het een FTP service op een andere poort had gevonden.



Voor een korte beschrijving van wat een NSE script doet, kun je de `-script-help` optie gebruiken die hierboven is genoemd:



![nmap-image](assets/fr/46.webp)



help resultaat weergeven voor NSE-script `sshv1`._



Kortom, we kunnen alle netwerkzoekopties, services, versies en technologieën die we tot nu toe hebben gebruikt opnieuw gebruiken!



#### C. Scriptargumenten beheren



Tijdens het gebruik van Nmap zult u bepaalde NSE-scripts tegenkomen die invoerargumenten nodig hebben om correct te functioneren. We zullen nu bekijken hoe je argumenten aan deze scripts kunt doorgeven via de opties van Nmap.



Laten we als voorbeeld het `ssh-brute` script nemen, waarmee je een brute force aanval kunt uitvoeren op de SSH service.



Een klassieke brute force aanval bestaat uit het testen van meerdere wachtwoorden (soms miljoenen) in een poging om zich te authenticeren voor een specifieke account. Door zoveel wachtwoorden te proberen, gokt de aanvaller op de waarschijnlijkheid dat de gebruiker een zwak wachtwoord heeft gebruikt in het wachtwoordwoordenboek dat voor de aanval is gebruikt.



Dit script heeft "standaard" opties, die we kunnen aanpassen aan onze context. In de context van deze aanval kunnen we Nmap bijvoorbeeld voorzien van de lijst met gebruikers en het te gebruiken wachtwoordwoordenboek. Voor zover ik weet, is het niet mogelijk om eenvoudig een lijst te maken van de argumenten die nodig zijn voor een script, dus de meest betrouwbare manier is om de officiële website van Nmap te bezoeken. Een directe link naar de documentatie voor een NSE script kan worden verkregen als antwoord op de `-script-help` optie:



![nmap-image](assets/fr/47.webp)



resultaat van het weergeven van hulp voor het NSE `ssh-brute` script met een link naar nmap.org._



Door op de aangegeven link te klikken, komen we op deze webpagina van de site [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



lijst met argumenten die kunnen worden doorgegeven aan het NSE-script `ssh-brute` van Nmap



Hier hebben we een duidelijk overzicht van de argumenten die gebruikt kunnen worden, de belangrijkste in onze context zijn `passdb` (bestand met een lijst wachtwoorden) en `userdb` (bestand met een lijst gebruikers). De documentatie hier verwijst naar interne Nmap bibliotheken, aangezien deze brute kracht mechanismen en bijbehorende opties wederzijds zijn om uniform gebruikt te worden in verschillende scripts (`ssh-brute`, `mysql-brute`, `mssql-brute`, etc.) en daarom min of meer dezelfde argumenten zullen hebben:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Zoals je in dit laatste commando kunt zien, kunnen we de benodigde argumenten voor een Nmap script opgeven met de `--scripts-args key=value,key=value` optie. Hier is een mogelijk resultaat van de Nmap uitvoer bij het uitvoeren van een SSH brute force via het `ssh-brute` NSE script:



![nmap-image](assets/fr/49.webp)



resultaat van SSH bruteforce-uitvoering via Nmap._



Zoals je kunt zien, wordt de informatie die door NSE scripts wordt gegenereerd voorafgegaan door `NSE: [scriptnaam]` in de interactieve uitvoer (terminal uitvoer), waardoor het makkelijker te vinden is. Binnen de gebruikelijke weergave van Nmap resultaten, hebben we simpelweg een samenvatting die aangeeft of er zwakke identifiers zijn ontdekt (inclusief wachtwoorden, onthoud dit).



Om nog een stapje verder te gaan, en om je eraan te herinneren dat dit allemaal gebruikt kan worden naast alle opties die we al bekeken hebben, is hier een commando dat het `10.10.10.0/24` netwerk ontdekt, de 2000 meest voorkomende TCP poorten scant en een anonieme toegangszoektocht uitvoert op FTP diensten en een brute force campagne op SSH diensten:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Dit is slechts één voorbeeld van de vele beschikbare scripts en hun opties. Maar we hebben nu een beter idee van hoe we met NSE-scripts moeten omgaan, of ze argumenten nodig hebben en hoe we deze argumenten aan Nmap moeten doorgeven.



### V. Conclusie



In dit gedeelte hebben we geleerd hoe we de NSE scripts van Nmap kunnen gebruiken om verschillende taken uit te voeren. Ik nodig je uit om de tijd te nemen om de verschillende categorieën scripts en de scripts zelf te ontdekken, om te zien hoeveel tests ze kunnen automatiseren.



We zijn nu al een aantal secties bezig met het verzamelen van meer of minder geavanceerde discovery, scan en opsomming opties. Inmiddels zou je je ervan bewust moeten zijn dat de uitvoer en resultatenweergave van Nmap behoorlijk uitgebreid begint te worden, soms zelfs te langdradig voor onze terminal. In de volgende sectie zullen we leren hoe we deze uitvoer kunnen beheersen, in het bijzonder door het op te slaan in bestanden in verschillende formaten.






## 9 - Nmap uitvoergegevens beheren




### I. Presentatie



In dit gedeelte kijken we naar de uitvoer die Nmap produceert, en in het bijzonder naar de verschillende opties om deze uitvoer te formatteren. We zullen zien dat Nmap verschillende uitvoerformaten kan produceren om aan verschillende behoeften te voldoen, en dat dit ook een van de sterke punten van dit gereedschap is.



Standaard biedt Nmap een gedetailleerde weergave van de resultaten van de scans en tests die het uitvoert. Dit omvat gescande hosts en services, degene die als toegankelijk worden gedetecteerd, de details van open poorten, hun status en versie. Daarnaast zijn details van NSE scripts ook beschikbaar in de terminal uitvoer. Deze uitvoer kan echter snel volumineus worden, zelfs met duidelijke opmaak van de informatie, waardoor het moeilijk kan zijn om precieze informatie in de resultaten te vinden.



### II. Nmap uitvoerformaten onder de knie krijgen



#### A. Scanresultaten opslaan in een tekstbestand



Om het makkelijker te maken, maakt [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) het erg makkelijk om de uitvoer op te slaan in een tekstbestand. Dit kan handig zijn voor archivering, vergelijking met andere testen, maar ook voor het doorbladeren van deze uitvoer met gespecialiseerde tekstverwerkingsprogramma's of scripttalen, zoals Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, etc. Om de standaard uitvoer van Nmap in een tekstbestand op te slaan, kunnen we de `-oN <filename>` optie gebruiken (de "N" in "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Geen verrassing dus, want Nmap toont zijn gebruikelijke standaard uitvoer in onze terminal, maar ook in het gespecificeerde bestand.



#### B. generate Nmap-uitvoer in verkort formaat



Er is ook een tweede uitvoerindeling in de "tekst"-stijl die gemakkelijk door een mens kan worden geïnterpreteerd: de "greppable"-indeling.



Dit formaat is gemaakt om een "verkorte" weergave van de Nmap uitvoer te geven, zodanig gestructureerd dat het makkelijker te verwerken is door gereedschappen als `grep`. Laten we eens kijken naar een voorbeeld van dit type uitvoer:



![nmap-image](assets/fr/50.webp)



nmap netwerkscan en uitvoer in "greppable" formaat._



Hier heb ik een netwerkdetectie uitgevoerd, evenals een poortscan en een analyse van technologieën en versies op een /24 netwerk, en vervolgens de uitvoer opgeslagen in een bestand in "greppable" formaat. Ik eindig met een bestand dat 2 regels per actieve host bevat:





- De eerste regel vertelt me dat die en die host _Up_ is;





- Een tweede regel vertelt me welke poorten zijn gescand, hun status en de technologie- en versie-informatie die is opgehaald in een heel specifiek formaat: `<poort>/<status/<protocol>//<service>//<versie>/,`




Deze opmaak met een vast scheidingsteken maakt snelle verwerking mogelijk door tekstverwerkingsprogramma's zoals `grep`, of script- en programmeertalen. Het volgende commando stelt me bijvoorbeeld in staat om eenvoudig informatie op te halen over host `10.10.10.5` in het geval van een enorme scan uitgevoerd door Nmap waarvan de uitvoer moeilijk door te bladeren zou zijn:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Omgekeerd kan ik ook gemakkelijk een lijst maken van alle hosts die poort 21 open hebben staan, omdat poorten en IP op dezelfde regel staan:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Om zulke uitvoer te generate, moeten we de `-oG <filename>.gnmap` optie gebruiken (de "G" in "grep"). Uit gewoonte gebruik ik hier de `.gnmap` extensie voor zo'n bestand, maar voel je vrij om te kiezen wat je wilt:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Dit formaat kan voor verschillende doeleinden worden gebruikt en is vooral handig voor snel scripten/sorteren. Desondanks wordt het steeds minder gebruikt ten gunste van het formaat dat we hierna zullen bekijken.



opmerking: het `-oG` greppable formaat is officieel vervallen sinds Nmap 7.90. Het kan nog steeds worden gebruikt voor compatibiliteit. Het kan nog steeds worden gebruikt voor compatibiliteitsdoeleinden, maar het wordt aanbevolen om het XML- of normale formaat te gebruiken voor ontwikkeling of geautomatiseerde parsing._



#### C. XML-indeling voor Nmap-uitvoer



Het laatste formaat dat het vermelden waard is in deze tutorial is XML. In tegenstelling tot de vorige twee formaten, is deze niet ontworpen om door mensen gelezen te worden, maar door andere tools of scripts.



XML (_eXtensible Markup Language_) is een opmaaktaal die wordt gebruikt om gegevens op te slaan en te transporteren en die een hiërarchische structuur biedt via aangepaste tags.



Binnen Nmap wordt het XML-formaat gebruikt om generate gedetailleerde rapporten te maken van de uitgevoerde scans, inclusief informatie over gedetecteerde hosts, poorten en kwetsbaarheden, en aanvullende informatie die niet wordt weergegeven in de standaard Nmap uitvoer.



Om een generate uitvoerbestand in XML formaat te maken, moeten we de `-oX` optie gebruiken ("O" van "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Het resultaat is de standaard uitvoer van Nmap in je terminal, evenals een bestand in XML-formaat in je huidige map.



Natuurlijk is het XML-formaat niet ontworpen om door mensen gelezen en geïnterpreteerd te worden. Niettemin, als je scripts of geautomatiseerde analyses wilt doen op dit formaat van Nmap uitvoer, moet je toch een idee hebben van de gebruikte tags en structuur. Hier is bijvoorbeeld een deel van de inhoud van het XML-bestand dat door Nmap is gemaakt en dat de scanresultaten voor 1 host toont:



![nmap-image](assets/fr/51.webp)



voorbeeld van een XML record voor 1 host tijdens een Nmap scan



Er staat hier veel informatie en we zijn vooral geïnteresseerd in de twee open poorten:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



We begrijpen dat dit formaat het automatisch ontleden van resultaten zal vergemakkelijken, omdat elk stukje informatie netjes is geordend in een speciale tag of attribuut met naam. In het bijzonder vinden we een stukje informatie dat we nog niet eerder zijn tegengekomen: de CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



We hebben de CPE kort genoemd in sectie 2 van module 2, en deze informatie wordt bepaald in matches tijdens versie detectie. Nmap gebruikt zijn service-, technologie- en versiedetectiemechanismen om de bijbehorende CPE te vinden.



Hierdoor kunnen we deze informatie hergebruiken in de databases en applicaties die er gebruik van maken. Ik denk in het bijzonder aan de NVD database, die verwijst naar CVE's. Voor elke CVE bevat het de CPE's waarop de kwetsbaarheid betrekking heeft. Hier is een voorbeeld van een CVE betreffende `a:microsoft:internet_information_services:7.5` uit de NVD database:



![nmap-image](assets/fr/52.webp)



aanwezigheid van een CPE in de details van een CVE in het NVD-gegevensbestand



We hebben nu een beter begrip van de voordelen van deze indeling, die een zeer duidelijke structuur van informatie biedt en alle gegevens bevat die door Nmap zijn verzameld of verwerkt.



Als reflex sla ik mijn Nmap scans systematisch in alle drie de formaten tegelijk op. Dit wordt mogelijk gemaakt door de `-oA <naam>` optie ("A" voor "Alle"), die een `<naam>.nmap` bestand, een `<naam>.xml` bestand en een `<naam>.gnmap` bestand aanmaakt. Op deze manier weet ik zeker dat ik niets tekort kom als ik de resultaten nog eens moet bekijken.



Met deze drie formaten zou je alles moeten hebben wat je nodig hebt om Nmap resultaten op een geautomatiseerde manier op te slaan en uiteindelijk te verwerken. We zullen het XML formaat weer gaan gebruiken in de volgende sectie, wanneer we kijken naar het gebruik van Nmap met andere beveiligingstools.



#### III. Een HTML-rapport genereren van een Nmap-scan



Het XML-formaat biedt veel mogelijkheden, niet in het minst om als basis te dienen voor het genereren van een rapport in HTML-formaat, dat visueel aantrekkelijker is om door te bladeren.



Om een Nmap-bestand in XML-formaat om te zetten in een webpagina, gebruiken we het hulpprogramma `xsltproc`, dat we eerst moeten installeren:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Zodra deze tool geïnstalleerd is, geef je het XML-bestand dat geconverteerd moet worden en de naam van het HTML-rapport dat gegenereerd moet worden:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Als resultaat hebben we onze hele scan mooi gestructureerd, met zelfs een paar kleuren en klikbare links in de inhoudsopgave!



![nmap-image](assets/fr/53.webp)



uittreksel van een Nmap-scanrapport in HTML-indeling, gegenereerd door xsltproc._



In grote lijnen bevat het XML-bestand dat door Nmap wordt opgeslagen een verwijzing naar een ander bestand in XSL-indeling:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Conversie naar HTML is daarom een functie die geleverd en gefaciliteerd wordt door Nmap, waarbij `xsltproc` een veelgebruikt en erkend gereedschap is om deze taak uit te voeren (dat niet uit de Nmap tool suite komt).



XSLT (_Extensible Stylesheet Language Transformations_) is een subset van XSL waarmee XML-gegevens op een webpagina kunnen worden weergegeven en, parallel aan XSL-stijlen, kunnen worden "getransformeerd" in leesbare, opgemaakte informatie in HTML-formaat.



bron: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Het informatieniveau in het rapport is gelijk aan dat van het XML-formaat van Nmap en hoger dan dat van de standaard terminaluitvoer (_interactive output_).



### IV. Het verbositeitsniveau van Nmap beheren



We zullen nu een paar opties bekijken voor Debugger Nmap of voor het bijhouden van de voortgang.



De eerste optie die we moeten noemen is de `-v` optie, die de verbositeit van Nmap verhoogt. Hier is een voorbeeld:



![nmap-image](assets/fr/54.webp)



nmap's uitgebreide uitvoer met de `-v`._ optie



Bij een scan die gericht is op veel hosts en poorten, wordt de terminaluitvoer moeilijk te exploiteren door de hoeveelheid informatie die wordt weergegeven. Daarom moet deze optie worden gebruikt in combinatie met de opties die eerder zijn gezien, waarmee de standaard uitvoer van Nmap in een bestand kan worden opgeslagen. Informatie gerelateerd aan het gebruik van verbositeit wordt niet opgenomen in dit uitvoerbestand. Zoals je in het bovenstaande voorbeeld kunt zien, kun je met deze verbositeit de acties en ontdekkingen van Nmap duidelijk en direct volgen. Voor langere scans waarbij het weergeven van gegevens lang kan duren, voorkomt dit dat je blind bent voor de huidige activiteit van Nmap en weet dat dingen vorderen en in welk tempo. Om de verbositeit met nog een niveau te verhogen, kun je de `-vv` optie gebruiken.



Om de activiteit van Nmap tijdens het scannen verder te volgen, kun je de `--packet-trace` optie gebruiken. Met de `-v` optie krijgen we een live log van alle open poorten die door Nmap zijn ontdekt, terwijl we met deze optie een logregel krijgen voor elk pakket dat naar een poort wordt gestuurd. Dit produceert natuurlijk een zeer uitgebreide uitvoer, maar staat gedetailleerde monitoring van Nmap's activiteit toe, hier is een voorbeeld:



![nmap-image](assets/fr/55.webp)



gedetailleerde monitoring van Nmap-activiteit via `--packet-trace`._



Nogmaals, deze informatie wordt niet opgenomen in het uitvoerbestand dat door Nmap wordt geproduceerd als de `-oN`, `-oG`, `-oX` of `-oA` opties worden gebruikt.



Ten slotte biedt Nmap ook twee debug-opties: `-d` en `-dd`. Deze opties gedragen zich hetzelfde als de `-v` verbosity optie, maar voegen extra technische informatie toe, zoals een samenvatting van de technische parameters aan het begin van de scan:



![nmap-image](assets/fr/56.webp)



timingopties worden weergegeven in de debugweergave van Nmap



In de volgende paragrafen bekijken we wat de "Timing" opties zijn en waarom het de moeite waard is om ze te kennen.



Tenslotte, als je alleen een eenvoudig, synthetisch overzicht wilt hebben van de voortgang van de Nmap scan, kun je de `--stats-every 5s` optie gebruiken. De "5s" betekent hier 5 seconden en kan aangepast worden naar wens. Dit is de frequentie waarmee we feedback krijgen van Nmap over de voortgang:



![nmap-image](assets/fr/57.webp)



informatie die wordt weergegeven door de `--stats-every` optie van Nmap



In het bijzonder kunnen we een percentage van de voortgang krijgen, evenals een indicatie van de fase waarin het zich bevindt: ontdekkingsfase van de host via [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), ontdekkingsfase van blootgestelde TCP-poorten, enzovoort. Deze informatie kan ook worden verkregen in de terminaluitvoer door op "Enter" te drukken tijdens een scan.



Nmap is echter niet erg goed in het schatten hoe lang een taak zal duren, niet in de laatste plaats omdat het niet van tevoren weet hoeveel hosts en services het moet scannen.



### V. Conclusie



In dit onderdeel hebben we gekeken naar een aantal opties voor het opslaan van Nmap scanresultaten in verschillende bestandsformaten. Dit is erg handig, want in realistische contexten kunnen scanresultaten honderden of zelfs duizenden regels beslaan! We hebben ook gezien hoe we het verbositeitsniveau van Nmap kunnen verhogen om te debuggen of om een scanvoortgangsrapport te verkrijgen.



Het XML formaat zal vooral handig zijn in de volgende sectie, waar we een paar tools bekijken die met Nmap resultaten kunnen werken.




## 10 - Nmap gebruiken met andere beveiligingsgereedschappen



### I. Presentatie



In deze sectie bekijken we een aantal klassieke toepassingen van Nmap met andere vrije en open source beveiligingsgereedschappen. In het bijzonder gebruiken we wat we geleerd hebben in de vorige secties om de kracht en efficiëntie van Nmap verder te verbeteren.



De mogelijkheid om Nmap scanresultaten op te slaan in XML maakt de gegevens compatibel met een groot aantal andere tools. Omdat bijna alle programmeer- en scripttalen tegenwoordig bibliotheken hebben die XML kunnen parsen, is het veel eenvoudiger om deze gegevens te verwerken. Een aantal tools, met name die gericht zijn op offensieve beveiliging, hebben functies voor het verwerken van het XML-formaat dat door Nmap wordt gegenereerd. Laten we het eens van dichterbij bekijken.



Ik ga een paar offensieve hulpmiddelen noemen zonder echt in detail te treden over hoe ze gebruikt worden of hoe ze werken. Ik ga ervan uit dat de lezer bekend is met hun basisgebruik en dat ze al operationeel zijn. Dit gedeelte zal vooral interessant zijn voor [cybersecurity] professionals (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), mensen in opleiding of mensen die besloten hebben zich in het onderwerp te verdiepen.



### II. Nmap resultaten importeren in Metasploit



De eerste tool die we gaan bekijken voor het hergebruiken van Nmap-gegevens in offensief onderzoek naar beveiliging en kwetsbaarheden is Metasploit.



Metasploit is een exploit- en aanvalsraamwerk. Het is een gratis oplossing en een erkend hulpmiddel dat een groot aantal modules bevat die in Ruby of Python zijn geschreven. Hiermee kunnen kwetsbaarheden worden uitgebuit, aanvallen worden uitgevoerd, backdoors worden gegenereerd, callbacks worden beheerd (C&C of Communication and Control functies) en alles kan uniform worden gebruikt.



In het bijzonder kan dit bekende en veelgebruikte besturingsraamwerk werken met een postgreSQL [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) waarin hosts, poorten, diensten, authenticatie-informatie en meer worden opgeslagen.





- Officiële Metasploit-documentatie: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Dit is waar Nmap en zijn uitvoer in het spel komen, omdat het XML-formaat van de Nmap-uitvoer gemakkelijk kan worden geïmporteerd in de database van Metasploit om de database van hosts en services te vullen, die dan snel kunnen worden aangewezen als doelwitten voor deze of gene aanval.



Eenmaal in mijn Metasploit interactive shell, begin ik met het creëren van een werkruimte, een soort ruimte die specifiek is voor mijn omgeving van die dag:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Nadat mijn werkruimte is gemaakt, moeten we valideren dat de communicatie met de database operationeel is:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Tenslotte kunnen we het Metasploit `db_import` commando gebruiken om onze Nmap scan in XML formaat te importeren:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Hier is het resultaat van het uitvoeren van al deze commando's:



![nmap-image](assets/fr/58.webp)



een Nmap-scan in XML-formaat importeren in de Metasploit-database



Hier kun je zien dat elke host is geïmporteerd, samen met de bijbehorende services. Deze gegevens kunnen vervolgens worden weergegeven via het commando `services` of `services -p <port>` voor een specifieke service:



![nmap-image](assets/fr/59.webp)



lijst van diensten geïmporteerd uit het XML-bestand in de Metasploit database



Tenslotte kunnen we deze gegevens snel en eenvoudig hergebruiken in een module dankzij de `-R` optie, die de lijst van services die we hebben verkregen als invoer voor de `RHOSTS` directief, die wordt gebruikt om de doelen van de uit te voeren aanval te specificeren, zal "converteren". Hier is een voorbeeld met de `ssh_login` module, waarmee je een brute force aanval kunt uitvoeren op [SSH] services (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



gebruik de `services -R` optie om de diensten te importeren die zijn gespecificeerd als het doel van de aanval



Dit is slechts een klein voorbeeld van wat er gedaan kan worden met Nmap data in Metasploit, maar het geeft je een klein idee van hoe snel en gemakkelijk deze informatie hergebruikt kan worden als onderdeel van een penetratietest, kwetsbaarheidsscan of cyberaanval. Het is ook de moeite waard om te vermelden dat Nmap direct vanuit Metasploit kan worden uitgevoerd om de resultaten in de database te importeren (commando `db_nmap`), nog een interessant onderwerp om te behandelen!



### III. Nmap gebruiken met de Aquatone webscanner



Het tweede gereedschap dat ik wil introduceren in dit gedeelte over het hergebruiken van Nmap resultaten voor offensieve beveiliging en kwetsbaarheden analyse is Aquatone.



Aquatone is een webscanner die is ontworpen om efficiënt webapplicaties op een netwerk te onderzoeken. Het biedt geavanceerde functies voor het ontdekken van webservices, identificatie van subdomeinen, poortanalyse en fingerprinting van webapplicaties. Alles duidelijk en beknopt gepresenteerd in HTML, JSON en tekstrapporten voor eenvoudige webbeveiligingsanalyse.



Net als met Metasploit kan Aquatone het XML-formaat van Nmap direct verwerken en gebruiken als doel om te scannen. In het bijzonder kan het alleen de interessante hosts en services (webservices) uit alle gegevens halen die een Nmap rapport kan bevatten.





- Tool link: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Om de XML uitvoer van Nmap te gebruiken met Aquatone, stuur je gewoon het XML bestand in een pipe die door Aquatone wordt geconsumeerd. Hier is een voorbeeld:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Waar Aquatone normaal gesproken port discovery uitvoert op hosts om webservices te vinden, zal het in deze context alleen vertrouwen op de resultaten van Nmap, die deze operatie al heeft uitgevoerd, waardoor tijd wordt bespaard:



![nmap-image](assets/fr/61.webp)



met Nmap-resultaten in XML-formaat met `aquatone`._



Ter informatie volgt hier een uittreksel uit het rapport van Aquatone:



![nmap-image](assets/fr/62.webp)



voorbeeld van een `aquatone` rapport



Persoonlijk gebruik ik Aquatone vaak om een snel overzicht te krijgen van de soorten websites die op het netwerk aanwezig zijn, vooral dankzij de screenshot-functionaliteit.



Ook hier geldt dat het hebben van een compleet Nmap rapport in XML formaat tijd bespaart en het makkelijk hergebruikt in een ander hulpmiddel.



### IV. Conclusie



Deze twee voorbeelden laten duidelijk zien dat het XML-formaat van Nmap het makkelijk maakt voor andere tools om de resultaten te gebruiken, omdat het een gestructureerd, gebruiksvriendelijk gegevensformaat is. Er zijn veel andere tools die deze resultaten kunnen verwerken, zoals geautomatiseerde rapportagetools, grafische weergaven of complexere, eigen kwetsbaarhedenscanners.



Natuurlijk kun je ook je eigen scripts en tools ontwikkelen in Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) of een andere taal met een XML-parsingbibliotheek om Nmap-resultaatgegevens naar eigen inzicht te manipuleren en hergebruiken.



Dit deel brengt ons aan het einde van de tutorialmodule over geavanceerder gebruik van Nmap, in het bijzonder voor het scannen op kwetsbaarheden via NSE-scripts.



Het volgende deel van de tutorial zal zich onder andere richten op een aantal aanvullende, meer technische best practices en tips over de specifieke scans die Nmap kan uitvoeren. We zullen ook kijken naar opties om de scanprestaties te optimaliseren, die vooral handig zijn bij het scannen van grote netwerken.




## 11 - Netwerkscanprestaties verbeteren



### I. Presentatie



In dit hoofdstuk leren we hoe we de snelheid van netwerkscans uitgevoerd met Nmap kunnen optimaliseren door gebruik te maken van verschillende specifieke opties. In het bijzonder zullen we meer leren over de innerlijke werking van Nmap, van _timeout_ beheer tot de vooraf opgeslagen configuraties van de tool.



Nu we de functies van Nmap goed hebben bekeken, laten we het beest en zijn kracht eens onder de knie krijgen. Als je de tool ooit hebt gebruikt op grote netwerken, heb je waarschijnlijk gemerkt dat sommige scans lang kunnen duren, ondanks de kracht van de tool. En met een goede reden: een simpel `nmap` commando met een paar opties kan generate miljoenen pakketten gericht op honderdduizenden potentiële systemen en diensten.



Bovendien kunnen sommige netwerkapparatuurconfiguraties opzettelijk een lagere snelheid (aantal pakketten per seconde) opleggen, met het risico dat je pakketten worden geweigerd of je IP Address om veiligheidsredenen wordt geweigerd.



Afhankelijk van de context kan het de moeite waard zijn om te proberen dit alles te optimaliseren, zoals we in dit hoofdstuk zullen zien.



In ieder geval kun je via de Nmap debug (optie `-d` gezien in een vorig hoofdstuk) de standaardwaarden van de parameters die we gaan bekijken controleren, evenals of de opties die je gaat gebruiken correct zijn meegenomen:



![nmap-image](assets/fr/63.webp)



timingopties bekijken via de `-d` optie van Nmap._



### II. De snelheid van Nmap-scans beheren



#### A. Parallellisatie beheren



Standaard gebruikt Nmap parallellisatie in zijn scans om ze te optimaliseren, en alle parameters die het gebruikt kunnen worden aangepast via verschillende opties. De gevallen waarin het echt nodig is om deze parameters aan te passen zijn echter vrij zeldzaam, dus daar gaan we in deze tutorial niet in detail op in:





- `--min-hostgroup/max-hostgroup <size>`: grootte van parallelle hostscangroepen.





- `--min-parallelism/max-parallelism <numprobes>`: parallellisatie van sondes.





- `-scan-delay/--max-scan-delay <tijd>`: past de vertraging tussen de controleregels aan.




Weet gewoon dat ze bestaan en gebruikt kunnen worden.



#### B. Het aantal pakketten per seconde beheren



Standaard past Nmap zelf het aantal pakketten per seconde dat het verstuurt aan op basis van de netwerkrespons. Maar het is mogelijk om deze instelling te forceren door de hoge en/of minimale waarde te definiëren die gevolgd moet worden in termen van aantal pakketten per seconde. Deze instelling wordt gemaakt met de opties `--min-rate <number>` en `--max-rate <number>` waarbij `number` een aantal pakketten per seconde voorstelt. Voorbeeld:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Met deze opties kun je de snelheid van de scans aanpassen aan je specifieke behoeften, om het proces te versnellen of om de gebruikte bandbreedte te beperken. Het laatste geval (het beperken van de snelheid van scans) is degene die je waarschijnlijk naar deze opties zal leiden, vooral als je last hebt van netwerklatentie bij het gebruik van Nmap (wat vrij zeldzaam is).



### III. Beheer van verbindingsfouten en time-outs



Een andere parameter waar we mee kunnen spelen om de snelheid van Nmap scans te optimaliseren (of een grotere nauwkeurigheid te garanderen) betreft _timeout_ en _retry_.



Voor _timeouts_ is dit de **no response timeout** waarna Nmap zal stoppen met wachten op een antwoord en de service of host als onbereikbaar zal beschouwen. Voor _retry_ is dit het **aantal opeenvolgende pogingen voor een bewerking** dat Nmap zal uitvoeren voordat hij verder gaat.



Net als bij parallellisatie kan _timeout_ en _retry_ beheer worden toegepast op de host of dienst zoekfasen:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: specificeert de rondetijd van een Exchange. Nogmaals, deze parameter wordt berekend en aangepast tijdens het scannen. Het is onwaarschijnlijk dat je deze hoeft te gebruiken, omdat Nmap deze tijd on the fly berekent aan de hand van de netwerkreactie.





- `--max-retries <aantal>`: beperkt het aantal heruitzendingen van een pakket tijdens het scannen van een poort. Standaard kan Nmap tot 10 herhalingen uitvoeren voor een enkele service, vooral als het latenties of verliezen op netwerkniveau vindt, maar in de meeste gevallen wordt er maar één uitgevoerd.





- `--host-timeout <time>`: specificeert de maximale tijd die Nmap op een host zal doorbrengen voor al zijn operaties, inclusief het scannen van poorten, service detectie en alle andere operaties met betrekking tot die host. Als dit tijdsinterval wordt overschreden zonder antwoord of **voltooiing van bewerkingen**, zal Nmap deze host verlaten zonder resultaten weer te geven en doorgaan naar de volgende in zijn lijst. Dit stelt je in staat om de maximale tijd die Nmap doorbrengt op een bepaalde host te controleren, waardoor voorkomen wordt dat je vast komt te zitten op recalcitrante hosts en de algehele scantijd wordt geoptimaliseerd.




In mijn dagelijkse werk gebruik ik de `--max-retries` en `--host-timeout` opties om mijn scans te optimaliseren:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Deze parameters bieden extra flexibiliteit om het scangedrag aan te passen aan specifieke behoeften en netwerkomstandigheden. Je moet je echter bewust zijn van hun implicaties in termen van belasting van gescande hosts en mogelijk verlies van nauwkeurigheid.



### IV. Gebruik van voorbereide configuraties



De verschillende opties die we in dit hoofdstuk hebben gezien, kunnen afzonderlijk worden gebruikt of als onderdeel van de kant-en-klare configuraties die Nmap aanbiedt. De optie die het mogelijk maakt om deze _templates_ (configuratiesjablonen) te gebruiken is `-T <nummer>` of `-T <naam>`. Er zijn 5 bruikbare _templates_ niveaus:



```
-T<0-5>: Set timing template (higher is faster)
```



Standaard gebruikt Nmap _template_ 3 (_normal_), wat over het algemeen voldoende is.



Zelf werk ik over het algemeen in contexten waarin ik redelijk snel moet zijn (en toch zo compleet mogelijk moet blijven) en gebruik ik vaak de `-T4` optie.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Hier is wat de debug-informatie voor deze scan ons laat zien:



![nmap-image](assets/fr/64.webp)



gebruik van `-T4` setup tijdens een Nmap scan



### V. Conclusie



In dit hoofdstuk hebben we gekeken naar verschillende technieken en opties die je kunt gebruiken om de kracht, agressiviteit en prestaties van Nmap te beheren. Deze opties zijn vooral handig bij het scannen van grote netwerken, en minder vaak voor stealth doeleinden.



In het volgende hoofdstuk kijken we naar een aantal best practices voor het gebruik van Nmap en het waarborgen van de veiligheid.




## 12 - Gegevensbeveiliging en vertrouwelijkheid bij gebruik van Nmap



### I. Presentatie



In dit hoofdstuk bekijken we een aantal goede praktijken die moeten worden toegepast met betrekking tot de beveiliging en vooral de vertrouwelijkheid van gegevens die door Nmap worden geproduceerd, verwerkt en opgeslagen.



Het gebruik van Nmap binnen een informatiesysteem kan al snel worden gecategoriseerd als een offensieve actie. Daarom moeten er een aantal voorzorgsmaatregelen worden genomen om binnen een wettelijk kader te handelen en tegelijkertijd de veiligheid van de beoogde doelen, de verzamelde gegevens en het systeem dat voor de scan wordt gebruikt, te garanderen.



### II. De juiste autorisaties verkrijgen



Voordat u een netwerk of systeem scant, moet u ervoor zorgen dat u de juiste autorisaties hebt verkregen. Het scannen van systemen op kwetsbaarheden (`NSE scripts`) zonder autorisatie kan illegaal zijn en kan juridische gevolgen hebben, vooral als de beveiliging van informatiesystemen niet tot je officiële takenpakket behoort.





- Ter herinnering: [Wetboek van Strafrecht: Hoofdstuk III: Aanvallen op geautomatiseerde gegevensverwerkende systemen] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Gevoelige gegevens beschermen



De resultaten die door Nmap worden geproduceerd kunnen als gevoelig worden beschouwd, vooral wanneer ze informatie bevatten over zwakke plekken in het informatiesysteem die door een aanvaller zouden kunnen worden uitgebuit. Maar ook wanneer ze betrekking hebben op systemen die niet voor iedereen toegankelijk zijn (bijvoorbeeld gevoelige, industriële, gezondheidszorg of [back-up] informatiesystemen (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



We hebben ook gezien dat, afhankelijk van de gebruikte NSE scripts, de NSE scanresultaten van [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) ook identifiers kunnen bevatten.



Zo heeft een kwaadwillende die toegang krijgt tot deze scanresultaten een kaart van het informatiesysteem en een schat aan technische informatie bij de hand, zonder dat hij deze handelingen zelf heeft uitgevoerd, met het risico om ontdekt te worden.



Het is daarom belangrijk om ervoor te zorgen dat gevoelige informatie niet ongepast wordt verzameld of opgeslagen bij het gebruik van Nmap, inclusief, maar niet beperkt tot, het volgende:





- Uitvoergegevens versleutelen: als u de resultaten van uw Nmap scans moet opslaan of verzenden, zorg er dan voor dat u ze versleutelt om de vertrouwelijkheid van de gegevens te beschermen. Dit voorkomt onbevoegde onderschepping van gevoelige informatie. Idealiter worden gegevens versleuteld zodra ze het systeem verlaten dat gebruikt is om de scan uit te voeren (een ZIP-archief versleuteld met een sterk wachtwoord is een heel goed begin).





- Stel toegangscontroles in: zorg ervoor dat alleen bevoegde mensen toegang hebben tot de resultaten van uw Nmap-scans, waar ze worden opgeslagen. Stel de juiste toegangscontroles in om gevoelige informatie te beschermen tegen ongeautoriseerde toegang.





- Waakzaamheid bij het omgaan met gegevens: wanneer je scangegevens doorgeeft, kopieert of verwerkt, zorg er dan voor dat je de gegevensbeveiliging onder strikte controle houdt. Dit betekent: laat ze niet rondslingeren in de `Download` map van een werkstation dat verbonden is met het internet, laat ze niet door je interne HTTP file Exchange applicatie lopen, laat je kladblok niet openstaan zonder het werkstation te vergrendelen tijdens je lunchpauze, etc.




### IV. Omgaan met agressieve scans



Zoals we door deze tutorial heen hebben gezien, kan Nmap erg langdradig zijn op netwerkniveau. Het kan ook pakketten versturen die niet goed geformatteerd zijn en die niet strikt de protocolstructuur respecteren in de netwerkframes en pakketten die het genereert. Al deze acties kunnen invloed hebben op bepaalde systemen en diensten, soms tot het punt dat het storingen of verzadiging van systeem- en netwerkbronnen veroorzaakt.



Om incidenten te voorkomen, moet je het gedrag van Nmap onder de knie krijgen en weten hoe je het aanpast aan de context waarin het wordt gebruikt, door middel van de verschillende opties die in deze tutorial worden besproken. We zullen Nmap niet noodzakelijkerwijs op dezelfde manier gebruiken op een informatiesysteem met industriële [hardware] (https://www.it-connect.fr/actualites/actu-materiel/) als in een gebruikersnetwerk dat bestaat uit Windows systemen die beschermd worden door een lokale firewall of in een netwerkkern.



Hopelijk hebben de verschillende lessen in deze tutorial je geleerd hoe je het gedrag van Nmap kunt beheersen en analyseren, maar de beste manier om te leren is door het te doen. Zorg er dus voor dat je bekend bent met de Nmap opties die je gaat gebruiken.



### V. Het scansysteem beschermen



In het eerste hoofdstuk hebben we gezien dat Nmap in de meeste gevallen als `root` of lokale beheerder gedraaid moet worden. Dit komt omdat het netwerkoperaties uitvoert, soms op een vrij laag niveau, via netwerkbibliotheken, die hoge en risicovolle rechten vereisen vanuit het oogpunt van systeemstabiliteit of de vertrouwelijkheid van andere applicaties.



Hierdoor kan Nmap gezien worden als een gevoelig onderdeel van het systeem waarop het geïnstalleerd is. Zorg ervoor dat u de laatste versie van Nmap gebruikt, omdat oudere versies bekende beveiligingslekken kunnen bevatten. Door een actuele versie te gebruiken, kunt u de risico's van het gebruik van de tool minimaliseren.



Als je ervoor gekozen hebt om Nmap niet via een sessie als `root` te gebruiken, maar door specifieke privileges toe te kennen aan een bevoorrechte gebruiker zodat hij alles heeft wat hij nodig heeft om Nmap te gebruiken (`sudo` of _capabilities_), wees je er dan van bewust dat Nmap gebruikt kan worden als onderdeel van een complete elevation of privilege:



![nmap-image](assets/fr/65.webp)



verhoging van Nmap-rechten via `sudo`._



Hier gebruik ik het Nmap commando via `sudo`, maar dit stelt me in staat om een interactieve shell als `root` op het systeem te krijgen, wat niet het oorspronkelijke doel was.



Het is ook zeer af te raden om Nmap te installeren op systemen die niet ontworpen zijn om netwerkscans uit te voeren. Ik denk in het bijzonder aan servers of werkstations. Aan de ene kant zou dit een potentiële vector voor privilege elevation toevoegen, maar bovenal zou het de aanvaller moeiteloos toegang geven tot een offensieve tool.



Tot slot moet de beveiliging van het systeem dat gebruikt wordt voor het scannen in het algemeen worden gewaarborgd, zodat het zelf geen vector wordt voor inbraak of het lekken van informatie. Als systeembeheerder is het beter om een speciaal systeem te gebruiken, idealiter met een beperkte levensduur, in plaats van je eigen werkstation.



### VI. Conclusie



Concluderend, zorg ervoor dat je Nmap goed beheerst voordat je het in de praktijk of in productieomstandigheden gebruikt en wees waakzaam bij het verwerken en beheren van de resultaten. Het zou zonde zijn om schade te veroorzaken, gegevens te lekken of een compromittering te faciliteren, wanneer de initiële aanpak gericht is op het verbeteren van de beveiliging van uw bedrijf.



## 13 - Poortscans via TCP: SYN, Connect en FIN



### I. Presentatie



In dit en het volgende hoofdstuk gaan we dieper in op de verschillende typen TCP scans die beschikbaar zijn in Nmap, te beginnen met de meest gebruikte: SYN, Connect en FIN scans.



Zoals je misschien hebt gemerkt, biedt Nmap verschillende opties voor TCP scans:



![nmap-image](assets/fr/66.webp)



scantechnieken die beschikbaar zijn in Nmap._



Het idee hier is om een aantal van deze methoden uit te leggen, om je te helpen hun verschillen, voordelen en beperkingen te begrijpen. Je zult zien dat het, afhankelijk van de context of van wat je wilt weten, beter is om voor de ene of de andere optie te kiezen.



### II. TCP SYN-scan of "Half Open scan



Het eerste type TCP scan dat we gaan bekijken is de `TCP SYN Scan`, ook bekend als de `Half Open Scan`. Als je je de netwerkscans herinnert die we deden na onze eerste poortscans, is dit het type scan dat standaard door [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) wordt gebruikt als het met rootrechten wordt uitgevoerd.



De vertaling zal je helpen begrijpen hoe deze scan werkt. In feite zal een TCP SYN scan een TCP SYN pakket sturen naar iedere doelpoort, wat het eerste pakket is dat verstuurd wordt door een client (degene die vraagt om een verbinding op te zetten) als onderdeel van de beroemde TCP driewegs handdruk. Normaal gesproken, als de poort open is op de doelserver, met een dienst die erachter draait, stuurt de server een TCP SYN/ACK pakket terug om de SYN van de client te valideren en de TCP verbinding te initialiseren. Dit antwoord heeft de vorm van een TCP pakket met de SYN en ACK vlaggen op 1, waardoor we kunnen bevestigen dat de poort open is en naar een service leidt.



Aan de andere kant, als de poort gesloten is, zal de server ons een `TCP` pakket sturen met de RST en ACK vlaggen op 1 om het verbindingsverzoek te beëindigen, zodat we weten dat er geen dienst actief lijkt te zijn achter deze poort:



![nmap-image](assets/fr/67.webp)



tCP SYN Scan gedragsdiagram voor open en gesloten poorten



Om een concreter beeld te krijgen van de `TCP SYN Scan`, voerde ik een scan uit van poort TCP/80 naar een host die een actieve webserver op deze poort had. Door een netwerkscan uit te voeren met Wireshark, kunnen we de volgende stroom zien (scan bron: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



netwerkopname tijdens een TCP SYN-scan voor een open poort



Op de eerste regel zien we dat de scanbron een TCP pakket naar host `10.10.10.203` op poort TCP/80 stuurt. In dit TCP pakket is de SYN vlag op 1 gezet om aan te geven dat dit een TCP verbindingsinitialisatie verzoek is.



Dan, op de tweede regel, zien we dat het doelwit antwoordt met een `TCP SYN/ACK`, wat betekent dat het accepteert om een verbinding te initialiseren en dus om streams te ontvangen op poort TCP/80. We kunnen dus concluderen dat poort TCP/80 open is en dat er een webserver aanwezig is op de gescande server.



Onze host stuurt dan een RST pakket terug om de verbinding te sluiten, waardoor de gescande host geen open TCP verbinding hoeft te onderhouden die wacht op een antwoord. In het geval van een scan op veel poorten, kan het niet sluiten van TCP verbindingen leiden tot een denial of service, omdat het aantal verbindingen dat wacht op antwoord dat de server kan onderhouden verzadigd raakt (zie [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



In Wireshark kun je de status van TCP-flags zien voor elke test die we uitvoeren. Dit laat zien of het pakket een SYN, SYN/ACK, ACK, etc. pakket is:



![nmap-image](assets/fr/69.webp)



de TCP-flags van een pakket bekijken in Wireshark (TCP SYN hier)



Omgekeerd voerde ik dezelfde test uit tussen de twee machines, maar dit keer scande ik een TCP/81 poort waarop geen service actief is (scanbron: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



netwerkopname tijdens een TCP SYN-scan voor een gesloten poort



De gescande host stuurt een `TCP RST/ACK` terug als antwoord op mijn `TCP SYN` als de poort niet open is.



Zoals gezegd, wanneer Nmap vanaf een geprivilegieerde terminal wordt uitgevoerd, is TCP SYN Scan de standaardmodus en deze kan worden geforceerd via de `-sS` (`scan SYN`) optie:



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




De `TCP SYN Scan` is de meest gebruikte scan vanwege de snelheid. Aan de andere kant kan het falen van een client om de _Three Way Handshake_ af te ronden (d.w.z. het niet versturen van de ACK na de SYN/ACK van de server) verdacht lijken als het te vaak wordt waargenomen op een server of van dezelfde bron op het netwerk. Het normale gedrag van een client na het ontvangen van een TCP SYN/ACK pakket als antwoord op een TCP SYN is om een `bevestiging` (ACK) te sturen en dan de Exchange te starten.



Desalniettemin biedt het een iets snellere scan, omdat het niet de moeite neemt om een ACK te sturen voor elk positief antwoord. Het voordeel van SYN Scan is de snelheid, omdat er maar één pakket wordt verzonden per te scannen poort, ten koste van een grotere kans op detectie.



Daarnaast kan TCP SYN scan detecteren of een poort wordt gefilterd (beschermd) door een firewall. In feite kan een firewall voor de doelhost gedetecteerd worden door de manier waarop het zich gedraagt wanneer het een TCP SYN pakket ontvangt op een poort die het geacht wordt te beschermen. Hij reageert gewoon niet. Echter, zoals we hebben gezien, is er in beide gevallen (open of gesloten poort) een reactie van de host. Dit derde gedrag onthult de aanwezigheid van een firewall tussen de gescande host en de machine die de scan uitvoert. Hier is het resultaat dat Nmap kan teruggeven wanneer een gescande poort wordt gefilterd door een firewall:



![nmap-image](assets/fr/71.webp)



nmap-weergave bij het scannen van een gefilterde poort



Wanneer we een netwerk capture uitvoeren tijdens het scannen, kunnen we eigenlijk zien dat er geen antwoord wordt gegeven:



![nmap-image](assets/fr/72.webp)



netwerkopname tijdens een TCP SYN-scan voor een poort die door een firewall wordt gefilterd



Het verschil tussen een gesloten poort en een gefilterde poort is als volgt: een gefilterde poort is een poort die beschermd wordt door een firewall, terwijl een gesloten poort een poort is waarop geen service draait en die daarom onze TCP pakketten niet kan verwerken. Sommige typen TCP scans, zoals de TCP SYN scan, kunnen detecteren of een poort gefilterd is, terwijl andere typen dat niet kunnen.



### III. TCP Connect-scan of volledig open scan



Het tweede type TCP scan is de `TCP Connect scan`, ook bekend als _Full Open Scan_. Deze werkt op dezelfde manier als de TCP SYN scan, maar retourneert dit keer een `TCP ACK` na een positief antwoord van de server (een SYN/ACK). Daarom heet het `Full Open', omdat de verbinding volledig wordt geopend en gestart op elke poort die tijdens de scan wordt geopend, waardoor de TCP _Three Way Handshake_ wordt gerespecteerd:



![nmap-image](assets/fr/73.webp)



tCP Connect Scan-gedragdiagram voor open en gesloten poorten



Hier is te zien wat er over het netwerk gaat tijdens een `TCP Connect scan` gericht op een open poort:



![nmap-image](assets/fr/74.webp)



netwerk snuiven tijdens een TCP Connect scan voor een open poort



We kunnen zien dat het eerste TCP pakket dat verzonden wordt een `TCP SYN` is, verzonden door de client, en de server zal dan antwoorden met een `TCP SYN/ACK`, wat aangeeft dat de poort open is en een actieve dienst host. Om een legitieme client helemaal te simuleren, stuurt Nmap dan een `TCP ACK` terug naar de server. Omgekeerd, bij het scannen van een gesloten poort:



![nmap-image](assets/fr/75.webp)



netwerk vastleggen tijdens een TCP Connect-scan voor een gesloten poort



Merk op dat het antwoord van de server op ons `SYN` pakket wederom een `TCP RST/ACK` pakket is, dus we kunnen concluderen dat de poort gesloten is en dat er geen diensten op draaien.



Bij gebruik van Nmap wordt de `-sT` (`scan Connect`) optie gebruikt om een TCP Connect Scan uit te voeren. Merk op dat wanneer Nmap wordt gebruikt vanuit een ongeprivilegieerde sessie, dit de standaard TCP scanmodus is:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



De `TCP Connect Scan` simuleert een meer legitiem verbindingsverzoek, met gedrag dat het meest lijkt op dat van een lambda client, dus het is moeilijker om een scan op een kleiner aantal poorten te ontdekken. Het is echter langzamer, omdat het elke TCP verbinding volledig initialiseert op de open poorten van de gescande machine.



Een Nmap scan van 10.000 poorten zal nog steeds makkelijk te detecteren zijn als er netwerk intrusion detection en protection services (IDS, IPS, EDR) geïnstalleerd zijn. Als een aanvaller zich gedeisd wil houden, zal hij zich richten op een klein aantal strategisch gekozen poorten, zoals 445 (SMB) of 80 (HTTP), die vaak open staan op servers en veel voorkomende kwetsbaarheden bevatten.



Aangezien TCP Connect Scan in beide gevallen een antwoord verwacht, kan het ook de aanwezigheid van een firewall detecteren die poorten op de doelhost filtert.



### IV. TCP FIN-scan of "Stealth Scan



De `TCP FIN Scan`, ook bekend als _Stealth Scan_, gebruikt het gedrag van een cliënt die een TCP-verbinding beëindigt om een open poort te detecteren.



In TCP betekent einde sessie het versturen van een TCP pakket met de FIN vlag op 1. In een normale Exchange stopt de server alle communicatie met de client (geen antwoord). Als de server geen actieve TCP verbinding heeft met de client, stuurt hij een `RST/ACK`. We kunnen dus onderscheid maken tussen open en gesloten poorten door `TCP FIN` pakketten naar een set poorten te sturen:



![nmap-image](assets/fr/76.webp)



tCP FIN scan gedrag diagram voor open en gesloten poorten



Ik heb het netwerk opnieuw opgenomen tijdens een _Stealth scan_ en dit is wat je ziet als de gescande poort open is:



![nmap-image](assets/fr/77.webp)



netwerkvastlegging tijdens een TCP FIN-scan voor een open poort



We kunnen zien dat de client één of twee pakketten stuurt om een TCP verbinding te beëindigen en dat de server niet reageert. Hij accepteert simpelweg het einde van de verbinding en stopt met communiceren.



Dit is wat we nu zien als we een gesloten poort scannen:



![nmap-image](assets/fr/78.webp)



netwerk vastleggen tijdens een TCP FIN-scan voor een gesloten poort



We zien dat de server een `TCP RST/ACK` pakket terugstuurt, dus er is een verschil in gedrag tussen een open en een gesloten poort, en we zijn in staat om een lijst te maken van de open poorten op een server door een TCP FIN pakket te sturen. Met Nmap wordt de `-sF` (`scan FIN`) optie gebruikt om een TCP FIN scan uit te voeren:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan werkt niet op Windows hosts, omdat het besturingssysteem TCP FIN pakketten negeert als ze naar poorten worden gestuurd die niet open zijn. Dus als je een TCP FIN Scan uitvoert op een Windows host, krijg je de indruk dat alle poorten gesloten zijn.



Daarom is het belangrijk om bekend te zijn met verschillende scanmethoden en het verschil ertussen te begrijpen.



Aangezien de TCP FIN in beide gevallen niet wacht op een antwoord, zal het niet in staat zijn om de aanwezigheid van een firewall tussen de doelhost en de scanbron te detecteren.



Hier is een voorbeeld van het TCP FIN scanresultaat van Nmap:



![nmap-image](assets/fr/79.webp)



resultaten van een TCP FIN-scan door Nmap._



In feite kan een non-respons van de host op een bepaalde poort betekenen dat de poort gefilterd is, maar ook dat hij open en actief is.



Deze scan wordt "stealth" genoemd, omdat hij niet generate veel verkeer genereert en over het algemeen geen logging veroorzaakt in de systemen waarop hij gericht is. Hij kan worden gebruikt om onopvallend poorten op een netwerk te ontdekken zonder alarm te slaan. Echter, zoals hierboven vermeld, kan de effectiviteit variëren afhankelijk van het doelsysteem, net als de discretie afhankelijk van de configuratie van de beveiligingsapparatuur.



### V. Conclusie



Tot zover het eerste van twee hoofdstukken over de verschillende TCP scantypes die Nmap aanbiedt! In het volgende hoofdstuk zullen we kijken naar de XMAS, Null en ACK TCP scan types, die op verschillende manieren werken om open poorten op een host te detecteren.





## 14 - Poortscans via TCP: XMAS, Null en ACK



### I. Presentatie



In dit gedeelte gaan we verder met het verkennen van de verschillende TCP scan methodes die Nmap biedt. Hier zullen we kijken naar de `XMAS`, `Null` en `ACK` methodes, die TCP-specifieke eigenschappen gebruiken om informatie op te halen over de poorten en services die open staan op een gegeven doel.



### II. TCP XMAS-scan



De XMAS Scan TCP is een beetje ongebruikelijk omdat het geen normaal gedrag van gebruikers of machines op een netwerk simuleert. In feite stuurt XMAS Scan TCP pakketten met de vlaggen `URG` (Urgent), `PSH` (Push) en `FIN` (Finish) op 1, om bepaalde firewalls of filtermechanismen te omzeilen.



De naam XMAS komt van het feit dat het ongebruikelijk is om deze vlaggen aan te zien. Wanneer alle drie de vlaggen tegelijk aan staan in een TCP pakket, ziet het eruit als een verlichte kerstboom:



![nmap-image](assets/fr/80.webp)



tCP-vlaggen gebruikt in XMAS-scan



Zonder hier in detail te treden over de rol van deze vlaggen, is het belangrijk om te weten dat bij het versturen van een pakket met deze drie vlaggen ingeschakeld, een actieve dienst achter de doelpoort geen pakketten zal terugsturen. Aan de andere kant, als de poort gesloten is, zullen we een TCP RST/ACK pakket ontvangen. We kunnen nu onderscheid maken tussen het gedrag van een open en een gesloten poort bij het opsommen van poorten op een machine:



![nmap-image](assets/fr/81.webp)



tCP XMAS Scan-gedragdiagram voor open en gesloten poorten



Nog steeds volgens dezelfde logica, laat een netwerkscan op poort TCP/80 van een host met een actieve webserver het volgende gedrag zien bij het detecteren van een open poort (scanbron `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



netwerkvastlegging tijdens een TCP XMAS-scan voor een open poort



We kunnen zien dat de scanbron twee TCP XMAS pakketten (met vlaggen `FIN`, `PSH` en `URG` ingesteld op 1) naar host `10.10.10.203` stuurt en dat er geen antwoord van het doel komt, wat aangeeft dat de poort open is. Wanneer daarentegen een `TCP XMAS Scan` wordt uitgevoerd op een gesloten poort, wordt het volgende resultaat waargenomen:



![nmap-image](assets/fr/83.webp)



netwerkvastlegging tijdens een TCP XMAS-scan voor een gesloten poort



Het antwoord op ons TCP pakket is dan een `TCP RST/ACK`, wat aangeeft dat de poort gesloten is. Om deze techniek met Nmap te gebruiken, kun je met de `-sX` (`scan XMAS`) optie een TCP XMAS Scan uitvoeren:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Het is belangrijk om op te merken dat de TCP XMAS scan niet in staat is om firewalls te detecteren die zich tussen het doel en de scanmachine kunnen bevinden, in tegenstelling tot sommige andere scantypes zoals TCP SYN of Connect. Een actieve firewall tussen de twee hosts zal ervoor zorgen dat er geen TCP terugkomt als de doelpoort wordt gefilterd (d.w.z. beschermd door de firewall). In het geval van een non-respons is het daarom onmogelijk om te weten of de poort beschermd is door de firewall of open en actief is. Je moet je er ook van bewust zijn dat, net als bij de TCP FIN-scan, bepaalde toepassingen of besturingssystemen zoals Windows de resultaten van dit type scan kunnen verstoren.



opmerking: ondersteuning voor XMAS/FIN/NULL-scans op recente versies van Windows blijft beperkt en de resultaten kunnen inconsistent zijn op dit type doelwit. (Update 2025)_



### III. TCP nulscan



In tegenstelling tot TCP XMAS scan, zal TCP Null scan TCP scan pakketten versturen met alle vlaggen op 0. Ook dit is gedrag dat nooit gevonden zal worden in een normale Exchange tussen machines, omdat het versturen van een TCP pakket zonder vlag niet gespecificeerd is in de RFC die het TCP protocol beschrijft. Daarom kan het gemakkelijker worden gedetecteerd.



Net als de TCP XMAS scan kan deze scan bepaalde firewalls of filtermodules verstoren, waardoor pakketten doorgelaten worden:



![nmap-image](assets/fr/84.webp)



tCP Null Scan gedragsdiagram voor open en gesloten poorten



Dit is wat er op het netwerk te zien is tijdens een TCP Null scan op een open poort:



![nmap-image](assets/fr/85.webp)



netwerkopname tijdens een TCP Null-scan voor een open poort



De scanmachine stuurt een vlagloos pakket (`[<None>]` in Wireshark) zonder antwoord van de server. Omgekeerd, als de doelpoort gesloten is:



![nmap-image](assets/fr/86.webp)



netwerkopname tijdens een TCP Null-scan voor een gesloten poort



Om een TCP Null scan uit te voeren met Nmap, gebruik je simpelweg de `-sN` (`scan Null`) optie:



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Aangezien de reactie wanneer een poort open is en wanneer een firewall actief is (geen server feedback in beide gevallen) identiek is, is TCP Null scan niet in staat om de aanwezigheid van een firewall te detecteren. Sterker nog, de firewall kan zelfs het resultaat vervalsen door te suggereren dat een poort open is, aangezien het niet reageert op TCP pakketten zonder vlaggen, ook al is de poort gefilterd. Dit is belangrijke informatie om bewust van te zijn bij het gebruik van scans die geen onderscheid kunnen maken tussen een open en een gefilterde (door een firewall beschermde) poort, zoals `TCP Null`, `XMAS` of `FIN` scans, om consistent te blijven in de interpretatie van de verkregen resultaten.



### IV. TCP ACK-scan



De TCP ACK scan wordt gebruikt om de aanwezigheid van een firewall op de doelhost of tussen het doel en de scanbron te detecteren.



In tegenstelling tot andere scans, probeert de TCP ACK scan niet te identificeren welke poorten open staan op de host, maar eerder of er een filtersysteem actief is, en antwoordt voor elke poort met `gefilterd` of `ongefilterd`. Sommige TCP scans, zoals `TCP SYN` of `TCP Connect`, kunnen beide tegelijk doen, terwijl andere, zoals `TCP FIN` of `TCP XMAS`, helemaal niet kunnen bepalen of er gefilterd wordt. Daarom kan de TCP ACK scan nuttig zijn:



![nmap-image](assets/fr/87.webp)



tCP ACK Scan-gedragdiagram voor gefilterde en ongefilterde poorten



We gebruiken de `-sA` optie van Nmap om dit type scan uit te voeren. Hier is het resultaat van een TCP ACK scan als de poort gefilterd is, d.w.z. geblokkeerd en beschermd door een firewall:



![nmap-image](assets/fr/88.webp)



nmap-weergave tijdens TCP ACK Scan._



Voorbeeldresultaat voor een host met een firewall en een zonder. Nmap geeft `gefilterd` op poorten TCP/80 en TCP/81 van host `10.10.10.203`. Bij een netwerkanalyse via Wireshark is het gedrag als volgt:



![nmap-image](assets/fr/89.webp)



netwerkopname tijdens een TCP ACK-scan voor een poort die niet door een firewall wordt gefilterd



De doelmachine geeft niets terug als er een firewall aanwezig is.



Om deze scan met Nmap te starten, gebruik je de `-sA` (`scan ACK`) optie:



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Conclusie



We hebben gekeken naar drie verschillende methoden om te scannen via TCP, naast de methoden die al zijn gepresenteerd. Deze verschillende methoden moeten worden gebruikt in zeer specifieke omstandigheden en contexten, met name in de context van penetratietesten of Red Team operaties, waarbij noties van discretie aanwezig zijn.



## 15 - Nmap CheatSheet - Samenvatting van zelfstudieopdrachten



### I. Presentatie



Hier is een korte samenvatting van de vele commando's en gebruikssituaties van Nmap, zodat je ze snel kunt vinden en hergebruiken in het dagelijks gebruik.



### II. Nmap: Spiekbriefje IT-Connect



Hier is een cheatsheet van de gepresenteerde commando's. Deze pagina maakt het gemakkelijk om de meest voorkomende toepassingen van Nmap te vinden.





- Poortscan




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Actieve hosts ontdekken




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



opmerking: De optie `-sP` is al enkele jaren verouderd en moet worden vervangen door `-sn`. (Update 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Versiedetectie




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE-scripts: op zoek naar kwetsbaarheden




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Nmap uitvoerbeheer




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Prestatieoptimalisatie




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- TCP-scan typen




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Ik hoop dat je deze commando's nuttig vindt. Vergeet niet om het doel van je scans aan te passen aan je context en om de officiële documentatie te raadplegen om de uitgevoerde tests volledig onder de knie te krijgen.



### III. Conclusie



De Nmap tutorial is nu voltooid. Je hebt nu de basis die je nodig hebt om deze uitgebreide en krachtige tool te gebruiken. We raden je sterk aan om te oefenen op gecontroleerde omgevingen (Hack The Box, VulnHub, virtuele machines) voordat je het in productie gebruikt.



Er valt nog veel te ontdekken over de innerlijke werking en geavanceerde mogelijkheden van de tool. Echter, beheersing van de commando's en concepten die hier worden gepresenteerd zullen je in staat stellen om Nmap met vertrouwen en relevantie te gebruiken.