---
name: Canaan Avalon Nano 3S
description: Uw ASIC Avalon configureren voor solomining of Miner pooling
---

![cover](assets/cover.webp)



In deze tutorial bekijken we hoe je de Canaan Avalon Nano 3S instelt, voor eenvoudig thuisgebruik van Miner.



Tot nu toe waren ASIC (*Application Specific Integrated Circuit*) machines die speciaal ontworpen waren om een bepaalde taak uit te voeren - in dit geval Hash berekening (SHA-256) voor Miner of Bitcoin - bijzonder ongeschikt voor huishoudelijk gebruik. De geluidsoverlast, de warmte die wordt gegenereerd en de noodzaak om je elektrische installatie aan te passen om de enorme kracht van deze apparaten te ondersteunen, weerhielden de meesten van ons ervan om mee te doen.



Vandaag de dag heeft Canaan, een van de toonaangevende fabrikanten van ASIC machines, besloten om de markt van particulieren die thuis Miner willen, aan te pakken door een reeks producten aan te bieden die relatief stil zijn en zeer eenvoudig te installeren (plug & play).



Deze apparaten worden op de markt gebracht als een extra verwarming in het geval van de **Avalon Nano 3S (140W)**, of als een miniverwarming met een vermogen van **800W** in het geval van de **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Houd er rekening mee dat het prijsverschil met traditionele kachels met een gelijkwaardig vermogen je in de meeste gevallen niet in staat stelt om financiële winst te maken. De satoshis die worden gegenereerd door de activiteit van Mining zullen dit prijsverschil nooit compenseren, tenzij je toegang hebt tot gratis (overtollige) of zeer goedkope elektriciteit.



Naar mijn mening moeten deze apparaten meer gezien worden als een eenvoudige manier om thuis Miner te maken voor degenen die dat om persoonlijke redenen willen doen: *niet-KYC Satss krijgen / de "loterij" meespelen door te solomineren / deelnemen aan Hashrate decentralisatie enz..*., terwijl je **als bonus** profiteert van de warmte die wordt opgewekt om je kamer te verwarmen in de winter. Maar niet als een manier om geld te besparen in de meeste gevallen tenminste (Westerse landen).



## Unboxing en functies



Laten we eerst eens kijken wat er in de doos van de Avalon Nano 3S zit.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Zodra je de doos hebt geopend, vind je een kartonnen hoes met daarin een WIFI-ontvanger die je, zoals we later zullen zien, moet aansluiten op de USB-poort van het apparaat om verbinding te maken met je lokale netwerk. Ook zit er een handleiding bij en een metalen pin om het apparaat terug te zetten naar de fabrieksinstellingen als dat nodig is.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Als alles uit de doos is, hebben we het volgende bij de hand: het apparaat zelf natuurlijk, de gebruikershandleiding, de WIFI-ontvanger, de eerder genoemde metalen tip en de Supply voeding van het apparaat. De meegeleverde creditcard is volgens ons niet het vermelden waard.



![image](assets/fr/05.webp)



Hieronder vindt u een tabel met een overzicht van de algemene technische specificaties van de Nano 3S :



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Inschakelen en verbinding maken met het lokale netwerk



Plaats uw Avalon Nano 3 S na het uitpakken indien mogelijk op een relatief open plek zodat de warmte kan circuleren. Plaats vervolgens de kleine WIFI-ontvangermodule zoals hieronder afgebeeld:



![image](assets/fr/06.webp)


Steek vervolgens de USB-C stekker van de Supply in de USB-C poort van het apparaat om het van stroom te voorzien.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Het apparaat start op en het Avalon Nano logo verschijnt op het scherm, gevolgd door een "mobiele telefoon" logo met de woorden "Gelieve het netwerk te configureren met de Avalon Family App".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Ga hiervoor naar de store van je mobiele applicatie, zoek en download de **Avalon Family** applicatie.



![image](assets/fr/11.webp)


Zodra het geïnstalleerd is, open je het door rechtsboven op "Overslaan" te klikken, vervolgens op de knop "Toevoegen" en ten slotte op "Zoeken". Zorg ervoor dat Bluetooth is ingeschakeld op je smartphone, zodat de detectie van het apparaat soepel verloopt.



![image](assets/fr/12.webp)


Zodra het apparaat is gedetecteerd door de applicatie, klik je erop en kies je "Verbinden". Je komt dan op het scherm waar je de gegevens van je WIFI-verbinding kunt invoeren.


![image](assets/fr/13.webp)


Zodra het apparaat is verbonden met je lokale netwerk, ziet het scherm er nu zo uit:



![image](assets/fr/14.webp)



Het toont een "fictieve" Hashrate, omdat er nog geen pool is geconfigureerd, en de tijd, datum, stroom en IP Address van het apparaat - erg handig als je de Interface van het apparaat wilt benaderen via een PC en browser (hierover later meer).



![image](assets/fr/15.webp)




## Aansluiten op een Mining pool



**Dit onderdeel is gemeenschappelijk voor de Nano 3s en Mini 3, aangezien de processen strikt identiek zijn**.



Of we nu willen "solomineren" of Miner "poolen", we zullen verbinding moeten maken met een Mining pool. In feite is ons apparaat niets meer dan een Hash-maker zonder bewustzijn van het Bitcoin netwerk. Door het aan te sluiten op een pool, krijgt het toegang tot het Bitcoin netwerk en kan het bloksjablonen ontvangen om mee te werken.



### De toepassing gebruiken om verbinding te maken met een Mining pool



Selecteer het apparaat in de Avalon Family-toepassing zoals hieronder weergegeven. Je wordt dan automatisch gevraagd om het beheerderswachtwoord van het apparaat te wijzigen. Klik op "OK" als je dit wilt doen, of op annuleren om het standaard toegangswachtwoord "admin" te laten staan.


![image](assets/fr/16.webp)


Selecteer vervolgens "Instellingen" en vervolgens "Poolconfiguratie" en voer de parameters in voor de 3 gevraagde pools.


Pools #2 en #3 zullen dienen als back-ups in het geval dat één van hen faalt, zodat je Miner niet voor niets werkt. Standaard wordt Hashrate naar pool #1 gestuurd



In ons geval kiezen we:




- 1 - Openbaar zwembad,
- 2 - CkPool,
- 3 - Oceaan.



![image](assets/fr/17.webp)



Voor meer details over hoe je verbinding maakt met een Mining pool, kun je deze tutorials raadplegen:



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Samengevat hebben we het volgende nodig





- de pool Address, meestal **stratum+tcp://xxxxxxxx:port**.





- de naam van de "werker" die bestaat uit *uw Bitcoin Address* en het *pseudo* dat u kiest voor uw apparaat, waarbij de 2 worden gescheiden door een *dot*, bijvoorbeeld:**bc1qxxxxxxxxxxx.MonAvalonNano3S**





- het wachtwoord, dat meestal altijd "**x**" is



Klik op "Opslaan" zodra de zwembadgegevens zijn ingevoerd.



![image](assets/fr/18.webp)


Start het apparaat opnieuw op volgens de instructies en wacht een paar minuten tot je Hashrate op het gewenste zwembad (#1) is gericht.



### De browser gebruiken om verbinding te maken met een Mining pool



Je kunt ook verbinding maken met een Mining pool en, meer in het algemeen, toegang krijgen tot het Interface beheersysteem van je apparaat via je favoriete browser.



Typ hiervoor in de zoekbalk van de browser het IP Address van het apparaat dat op het onderstaande scherm wordt weergegeven, in ons voorbeeld **192.168.144.6**



![image](assets/fr/15.webp)



De volgende pagina verschijnt en vraagt je om de Avalon Family applicatie te openen en de QR-code te scannen die bij de applicatie wordt weergegeven.



![image](assets/fr/20.webp)



Open de applicatie en klik op de 3 streepjes rechtsboven en vervolgens op scannen. Scan de QR-code van de browser, voer het beheerderswachtwoord van de applicatie in en klik op OK.



![image](assets/fr/21.webp)



Hier ben je op de webpagina waarmee je kunt communiceren met je Avalon. Het is meer een dashboard om de statistieken van de machine weer te geven dan een manier om hem te configureren.



Maar de zwembadinstellingen zijn nog steeds toegankelijk op deze manier, door te klikken op **"Pool Config"** in de rechterbenedenhoek.



![image](assets/fr/22.webp)



Op dezelfde manier als bij de mobiele applicatie kun je hier je zwembadparameters invoeren.



![image](assets/fr/23.webp)



## Bedien je apparaat via de Avalon Family app



We hebben nu onze Miner thuis aangesloten op ons lokale netwerk en onze Hashrate gericht op pools of Minings. Laten we nu de essentiële functies van onze machine ontdekken via de Avalon Family-toepassing.



Klik in de Avalon gezinstoepassing op het pictogram dat overeenkomt met de Avalon Nano 3S.


vervolgens krijg je 3 menu's te zien: "Werkmodus", "Lichtregeling" en "Instellingen". Klik eerst op "Werkmodus". Je krijgt dan 3 energiestanden voor je machine.



**Laag**: geeft je ongeveer 3 Th/s Hashrate voor 70W stroomverbruik


**Medium**: levert ongeveer 4,5 Th/s Hashrate op voor 100W stroomverbruik


**High**: geeft je ongeveer 6 Th/s Hashrate bij een maximaal verbruik van 140W



![image](assets/fr/31.webp)


Laten we een stapje terug doen en het menu "Lichtregeling" verkennen. Dit is puur cosmetisch. Er zijn een heleboel opties beschikbaar voor het variëren van kleur, intensiteit, warmte, het uitschakelen van de LED's van het apparaat 's nachts, enzovoort. Het is gemakkelijk om het zelf uit te vinden.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Het laatste menu dat voor ons beschikbaar is, is het menu "Instellingen" dat we al hebben gezien voor het verbinden met onze Mining pools. Hier kun je je pools beheren, het beheerderswachtwoord van het apparaat wijzigen en verschillende statistieken bekijken, zoals de vervaldatum van de garantie, de zuiverheid van de filters of hoe je contact kunt opnemen met support in geval van een storing.



![image](assets/fr/35.webp)


Voor onderhoud en om het filter zo schoon mogelijk te houden, raden we aan een stofzuiger te gebruiken en regelmatig de luchtinlaten en -uitlaten te stofzuigen om verstopping te voorkomen.



We zijn aan het einde gekomen van deze tutorial, waarin we hebben geleerd hoe we onze Avalon Nano 3 S op ons lokale netwerk kunnen aansluiten, hoe we onze Hashrate op Mining pools kunnen richten en hoe we door opties en instellingen kunnen navigeren met behulp van de Avalon Family applicatie.



Bekijk voor meer informatie onze handleiding over de superieure versie van de Avalon: de Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7