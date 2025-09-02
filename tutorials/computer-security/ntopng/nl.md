---
name: Ntopng
description: Bewaak je netwerk met ntopng
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian Duchemin gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## I. Presentatie



**Of het nu is om de netwerkfluïditeit te controleren, om een duidelijk beeld te krijgen van het gebruik of voor prestatiestatistieken, netwerkflow monitoring is een belangrijk onderdeel van een bedrijfsnetwerk**. Het helpt anticiperen op veranderingen in de infrastructuur en helpt de gebruikskwaliteit voor gebruikers te garanderen (ook bekend als QoE voor *Kwaliteit van Ervaring*, in tegenstelling tot QoS).



Hiervoor zijn vele technieken en software/protocollen beschikbaar. Netflow, bijvoorbeeld, ontwikkeld door Cisco, kan gebruikt worden om IP stroomstatistieken van een Interface op te halen, maar het gebruik is beperkt tot compatibele apparatuur.



Daarom ga ik in deze tutorial **Ntop** introduceren en laten zien hoe je het in je infrastructuur kunt gebruiken om je netwerkgebruik in de gaten te houden.



Ntop is open source software die op elke Linux-machine geïnstalleerd kan worden. Het is gratis en kan de volgende gegevens verzamelen:





- Bandbreedtegebruik
- Belangrijkste klanten
- Belangrijkste bestemmingen
- Gebruikte protocollen
- Gebruikte toepassingen
- Gebruikte poorten
- Enz.



Nu omgedoopt tot **Ntopng (New Generation)**, biedt het veel basisfuncties gratis. Er is ook een commerciële versie beschikbaar, waarmee geconfigureerde waarschuwingen kunnen worden geëxporteerd naar SIEM-software of verkeer kan worden gefilterd met regels die direct vanuit de controleregel zijn gedefinieerd.



## II. Vereisten



De installatie van een Ntopsonde verschilt afhankelijk van de apparatuur en de omgeving. Ik ga je hier dus geen stap-voor-stap handleiding geven, maar zal de verschillende mogelijkheden schetsen.



### A. Boordmodus



Als je een pfSense, OPNSense of Endian firewall in productie hebt, of zelfs een Linux werkstation met NFTables, goed nieuws! Je kunt Ntopng direct installeren en beginnen met het monitoren van je interfaces.



Het voordeel van deze techniek is dat er geen extra hardware nodig is. Aan de andere kant verhoogt het het gebruik van bronnen, dus zorg ervoor dat je voldoende hardware of een VM van voldoende grootte hebt (minimaal 2 cores en 2BG RAM).



### B. TAP/SPAN-modus



Een **tap** is **een netwerkapparaat dat het verkeer dat er doorheen gaat dupliceert en naar een ander apparaat stuurt.** Het voordeel van dit apparaat is dat het geen aanpassing aan de bestaande infrastructuur vereist en overal geplaatst kan worden om specifieke netwerksecties te monitoren, of tussen de core switch en de edge router om verkeer van/naar het internet te analyseren.



Het grote nadeel van dit soort apparatuur zijn de kosten. In de huidige Gigabit netwerken kan een passieve tap het netwerkverkeer niet goed afvangen, dus heb je een actief apparaat nodig dat rond de €200 (minimaal) kost.



De **SPAN** modus, ook bekend als **port mirroring**, wordt gebruikt door een switch om verkeer door te sturen van de ene poort naar de andere. Dit is veruit mijn voorkeursmethode, omdat het eenvoudig in te stellen is en, net als tap, je een deel van het netwerk of het hele netwerk naar believen kunt monitoren. Er zijn echter twee nadelen: de switch moet deze functie integreren en het gebruik ervan kan de processorbelasting op de switch verhogen.



### C. Routermodus



Het is perfect mogelijk om een router onder Linux te mounten en er ntopng op te installeren. Het enige nadeel van deze methode is dat het je netwerk zal wijzigen, ofwel de interne adressering, ofwel de adressering tussen je "echte" router en degene die je toevoegt.



Opmerking: voor lezers van het artikel [Maak een Wifi-router met Raspberry Pi en RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) is het perfect mogelijk om ntopng op je Rpi te installeren om nauwkeurige statistieken te krijgen!



### D. Brugmodus



Een interessant alternatief is het gebruik van **een Linux machine in bridge mode.** Geplaatst tussen twee apparaten, maakt dit het mogelijk om al het verkeer vast te leggen zonder in te hoeven grijpen in de configuratie van de infrastructuur of de apparatuur. Aangezien een oude machine de klus kan klaren, kunnen de kosten van deze methode ook aantrekkelijk zijn. Merk op dat om optimaal te zijn, het apparaat drie netwerkkaarten moet hebben, twee in bridge-modus, één voor toegang tot Interface en SSH. Het is mogelijk om slechts twee kaarten te gebruiken, maar dan wordt het beheerverkeer van het apparaat ook opgevangen...



Het is dus **deze laatste modus die ik ga gebruiken**. Om praktische redenen gebruik ik virtuele machines voor de demonstratie, maar de methode blijft hetzelfde voor gebruik op fysieke machines.



## III. Sondevoorbereiding met Interface brug



Voor de sonde kies ik een **Debian 11** machine in minimale installatie.



Eerste stap, altijd hetzelfde, de:



```
apt-get update && apt-get upgrade
```



Installeer dan het pakket **bridge-utils**, waarmee we onze bridge kunnen maken:



```
apt-get install bridge-utils
```



Eenmaal geïnstalleerd is het eerste dat we moeten onthouden de huidige naam van onze netwerkkaarten. Onder Debian kan deze naam verschillende vormen aannemen en die hebben we nodig voor de configuratie.



Een eenvoudig **ip add** commando geeft een uitvoer met deze informatie:



![Image](assets/fr/016.webp)



Hier zie ik 3 interfaces:





- Lo**: dit is de loopback Interface; het is een virtuele Interface die over de apparatuur "loopt". In principe wordt deze Interface, waarvan de Address 127.0.0.1 is (hoewel elke Address in 127.0.0.0/8 volstaat, omdat dit bereik voor dit doel gereserveerd is) gebruikt om contact te maken met de apparatuur zelf. Als je een website op je werkstation hebt geïnstalleerd (bijvoorbeeld met WAMPP), heb je waarschijnlijk ooit de "*localhost*" Address gebruikt om contact te maken met de apparatuur zelf Address gebruikt om de site op je eigen machine weer te geven. Deze hostnaam is geassocieerd met Address 127.0.0.1 en dus met de Interface loopback.
- ens33**: dit is mijn eerste Interface, die hier een Address kreeg van mijn DHCP
- ens36**: mijn tweede Interface



Nu ik alle informatie heb, kan ik het */etc/network/interfaces* bestand aanpassen om mijn bridge te maken. Hier is hoe het er momenteel uitziet (kan variëren):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Het eerste deel betreft mijn loopback Interface, die ik niet zal aanraken, gevolgd door de Interface ens33. De wijzigingen betreffen het toevoegen van mijn tweede Interface (ens36) en het configureren van de bridge met deze twee interfaces:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Hier volgen enkele verklaringen van deze eerste wijzigingen:





- auto *Interface***: zal automatisch Interface "starten" bij het opstarten van het systeem
- iface *Interface* inet manual**: om de Interface zonder IP Address te gebruiken. Zoals het sleutelwoord "static" om een statische IP Address te definiëren of "dhcp" om dynamische adressering te gebruiken



De aanpassingen gaan door:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Ook hier een paar verklaringen:





- iface br0 inet static**: hier heb ik mijn Interface bridge (*br0*) met een statische Address gedefinieerd.
- Address, netmask, gateway**: adresseringsinformatie voor de kaart
- bridge_ports**: interfaces die in de bridge moeten worden opgenomen
- bridge_stp**: het Spanning Tree protocol wordt gebruikt bij het onderling verbinden van schakelaars om redundante links te detecteren en lussen te vermijden. Aangezien een bridge kan worden ingevoegd tussen twee netwerkpaden, kan het de bron van een lus zijn, vandaar de mogelijkheid om dit protocol in te schakelen. Ik heb het hier niet nodig, dus ik schakel het uit.



Sla de wijzigingen op en start het netwerk opnieuw op:



```
systemctl restart networking
```



Om de wijzigingen te controleren, geeft u het resultaat van de opdracht **ip** add opnieuw weer:



![Image](assets/fr/021.webp)


Je kunt duidelijk **mijn nieuwe Interface "*br0*" zien met het IP Address dat ik eraan toegewezen heb.** Overigens kun je ook zien dat mijn twee fysieke interfaces inderdaad "UP" zijn, maar geen IP Address hebben.



## IV. NtopNG installeren



Nu onze probe in staat is om verkeer tussen mijn netwerk en de router te sniffen, hoeft alleen nog ntopng geïnstalleerd te worden. Om dit te doen, moet je eerst het */etc/apt/sources.list* bestand aanpassen en **contrib** toevoegen aan het einde van elke regel die begint met **deb** of **deb-src**.



Standaard bevatten pakketbronnen alleen pakketten die voldoen aan de DFSG (*Debian Free Sotftware Guidelines*), geïdentificeerd met het sleutelwoord **main**. U kunt deze bronnen ook toevoegen:





- contrib**: pakketten die DFSG-conforme software bevatten, maar afhankelijkheden gebruiken die geen deel uitmaken van de **main** tak
- non-free**: bevat pakketten die niet DFSG-compatibel zijn



Voorbeeld van een regel in /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Dus voeg ik het woord **contrib** toe aan regels als deze.



De rest van de stappen staat op de [NtopNG] site (https://packages.ntop.org/apt/) waar, voor Debian 11, de Ntop bronnen moeten worden toegevoegd voor toekomstige installatie. Deze toevoeging is geautomatiseerd door gebruik te maken van een:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Dan komt de eigenlijke installatiefase:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Het eerste commando verwijdert de cache van de apt package manager. Het tweede zal de pakketlijst bijwerken en het derde zal NtopNG installeren.



Na de installatie is de **NtopNG software direct beschikbaar op poort 3000 van de Debian machine**. Dus voor mij is het `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



NtopNG startpagina



De standaard login en wachtwoord worden getoond, dus je hoeft ze alleen maar in te voeren!



## V. NtopNG gebruiken



Wanneer je voor het eerst inlogt, is het eerste wat je wordt gevraagd om te doen het standaard beheerderswachtwoord en de standaard taal te wijzigen. Helaas zit Frans daar niet bij.



Dan kom je op het dashboard:



![Image](assets/fr/023.webp)



NtopNG dashboard



Wen er maar niet aan! Als je het gele vakje bovenaan het scherm ziet, zie je de zin: "*Licentie verloopt in 04:57*". Standaard start de installatie een proefversie van de volledige versie van NtopNG, maar voor een (zeer) beperkte tijd. Zodra deze "countdown" is bereikt, wordt de *community* versie geactiveerd en verandert het dashboard:



![Image](assets/fr/024.webp)



Nieuw NtopNG-community dashboard



Het eerste wat je moet doen is **controleren of de juiste Interface luistert**. Linksboven in een drop-down lijst met beschikbare interfaces kun je de Interface selecteren waarin we hier geïnteresseerd zijn: br0



![Image](assets/fr/025.webp)



Interface selectie



Het nieuwe venster toont de "Top Flaw Talkers", d.w.z. de apparaten die het meest communiceren. Hier worden slechts twee stations weergegeven:



![Image](assets/fr/026.webp)



**Bron hosts verschijnen aan de linkerkant, bestemmingen aan de rechterkant ** Hierdoor kun je het gebruik van de totale bandbreedte door elke host visualiseren en krijg je een algemeen beeld van het netwerkverkeer. Dat is niet slecht, maar we kunnen verder gaan...



Als ik bijvoorbeeld op "*Hosts*" klik, krijg ik een grafiek te zien die het zendende en ontvangende stroomverbruik van elke host op mijn netwerk laat zien. Hier kan ik bijvoorbeeld zien dat 192.168.1.37 alleen al goed is voor 80% van mijn verkeer:



![Image](assets/fr/027.webp)



Als ik op het IP Address van de host in kwestie klik, word ik doorgestuurd naar een overzichtspagina:



![Image](assets/fr/028.webp)



Ik kan bijvoorbeeld zien dat het een VMWare machine is (door de JA van mijn MAC Address te herkennen), dat het DESKTOP-GHEBGV1 heet (dus zeker een Windows host) EN ik heb **statistieken van ontvangen en verzonden pakketten, evenals de hoeveelheid gegevens**.



Je ziet ook een nieuw menu bovenaan dit overzicht. Ik stel voor dat je klikt op "**Apps**" om te zien wat zoveel verkeer genereert:



![Image](assets/fr/017.webp)


Ha, het lijkt erop dat we een antwoord hebben! Op de grafiek links, **zien we dat 76,6% van het verkeer afkomstig is van ... Windows Update**, dus deze host downloadt updates!



NtopNG gebruikt een technologie genaamd DPI voor *Deep Packet Inspection*, waardoor het elke netwerkstroom kan categoriseren en de applicatie (of familie van applicaties) erachter kan definiëren.



Om dit te demonstreren, start ik een YouTube-video op mijn host:



![Image](assets/fr/018.webp)



**Het verkeer werd onmiddellijk herkend en gecategoriseerd!



Opmerking: om voor de hand liggende redenen kan dit soort software privacyproblemen veroorzaken, dus wees voorzichtig om het onder de juiste omstandigheden te gebruiken. Merk ook op dat het mogelijk is om **resultaten te anonimiseren**, de optie is te vinden in **Instellingen > Voorkeuren > Misc** en heet "**Mask Host IP Address**".



## VI. Detecties en waarschuwingen



NtopNG kan ook beveiligingswaarschuwingen geven voor bepaalde feeds. Deze kunnen worden gevonden in het **Alerts** menu, op de linker banner. Hier heb ik bijvoorbeeld een totaal van 2851 waarschuwingen, verdeeld in verschillende ernstgraden: Kennisgeving, Waarschuwing en Fout.



![Image](assets/fr/019.webp)



Laten we eens kijken naar de waarschuwingen voor hoge kriticiteit, ik heb er 17!



Als je op deze figuur klikt, krijg je de details van de waarschuwingen te zien. Er is hier niets alarmerends aan de hand, het is een fout-positieve, de download van updates wordt gecategoriseerd als een binaire bestandsoverdracht in een HTTP-stream, wat inderdaad een aanval zou kunnen betekenen.



![Image](assets/fr/020.webp)



Omdat ik de gratis versie gebruik, kan ik echter geen domeinen of hosts uitsluiten die de bron zijn van waarschuwingen, dus je zult ze in de gaten moeten houden om te voorkomen dat je iets veel verontrustenders mist. NtopNG zal generate waarschuwingen geven in het geval van:





- Binair bestand downloaden via HTTP
- Verdacht DNS-verkeer
- Een niet-standaard poort gebruiken
- Detectie van SQL-injectie
- Cross-Site Scripting (XSS)
- Enz.



## VII. Conclusie



In deze tutorial hebben we gezien **hoe we een probe met NtopNG** kunnen instellen zodat we **het netwerkverkeer** kunnen analyseren om het protocolgebruik en de bezetting van elke host te visualiseren, maar ook om verdacht verkeer te detecteren.



Helaas kan ik in dit artikel niet alle functies en mogelijkheden behandelen, maar ga gerust op onderzoek uit!



Deze oplossing kan op permanente basis worden geïmplementeerd binnen een bedrijfsinfrastructuur. NtopNG kan ook resultaten exporteren naar een InfluxDB-database, zodat je je eigen dashboards kunt maken met een tool van derden zoals Graphana.