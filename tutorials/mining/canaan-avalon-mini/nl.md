---
name: Canaan Avalon Mini 3
description: Uw ASIC Avalon configureren voor solomining of Miner pooling
---

![cover](assets/cover.webp)



In deze tutorial bekijken we hoe je de Canaan Avalon Mini 3 instelt, voor eenvoudig thuisgebruik van Miner.



Tot nu toe waren ASIC (*Application Specific Integrated Circuit*) machines die speciaal ontworpen waren om een bepaalde taak uit te voeren - in dit geval Hash berekening (SHA-256) voor Miner of Bitcoin - bijzonder ongeschikt voor huishoudelijk gebruik. De geluidsoverlast, de warmte die wordt gegenereerd en de noodzaak om je elektrische installatie aan te passen om de enorme kracht van deze apparaten te ondersteunen, weerhielden de meesten van ons ervan om mee te doen.



Vandaag de dag heeft Canaan, een van de toonaangevende fabrikanten van ASIC machines, besloten om de markt van particulieren die thuis Miner willen, aan te pakken door een reeks producten aan te bieden die relatief stil zijn en zeer eenvoudig te installeren (plug & play).



Deze apparaten worden op de markt gebracht als een extra verwarming in het geval van de **Avalon Nano 3S (140W)**, of als een miniverwarming met een vermogen van **800W** in het geval van de **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Houd er rekening mee dat het prijsverschil met traditionele kachels met een gelijkwaardig vermogen je in de meeste gevallen niet in staat stelt om financiële winst te maken. De satoshis die worden gegenereerd door de activiteit van Mining zullen dit prijsverschil nooit compenseren, tenzij je toegang hebt tot gratis (overtollige) of zeer goedkope elektriciteit.



Naar mijn mening moeten deze apparaten meer gezien worden als een eenvoudige manier om thuis Miner te maken voor degenen die dat om persoonlijke redenen willen doen: *niet-KYC Satss krijgen / de "loterij" meespelen door te solomineren / deelnemen aan Hashrate decentralisatie enz..*., terwijl je **als bonus** profiteert van de warmte die wordt opgewekt om je kamer te verwarmen in de winter. Maar niet als een manier om geld te besparen in de meeste gevallen tenminste (Westerse landen).



## Unboxing en functies



### Avalon Nano 3S



Laten we eerst eens kijken wat er in de doos van de Avalon Mini 3 zit.



![image](assets/fr/24.webp)



Als je de doos opent, ligt de gebruiksaanwijzing recht voor je, maar nog belangrijker is dat de WIFI-ontvangermodule verborgen zit onder de ronde witte sticker links van de gebruiksaanwijzing. Die heb je later nodig.



![image](assets/fr/25.webp)



Onder het schuimblok zit het apparaat, en zodra het uit de doos is gehaald, de Supply voedingseenheid.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Inschakelen en verbinding maken met het lokale netwerk



Plaats uw Avalon Mini 3 na het uitpakken indien mogelijk op een relatief open plek, zodat de warmte goed kan circuleren. Steek vervolgens eerst de kleine WIFI-ontvangermodule in de USB-poort aan de onderkant van het apparaat, sluit de Supply aan en zorg ervoor dat de aan/uit-knop in stand "1" staat.



![image](assets/fr/28.webp)



Zodra deze stappen zijn voltooid, gaat het LED-scherm van het apparaat branden en toont het het "Bluetooth"-symbool, wat aangeeft dat het klaar is om te worden verbonden met je lokale netwerk via de Avalon Family-toepassing.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Ga hiervoor naar de store van je mobiele applicatie, zoek en download de **Avalon Family** applicatie.



![image](assets/fr/11.webp)


Zodra het geïnstalleerd is, open je het door rechtsboven op "Overslaan" te klikken, vervolgens op de knop "Toevoegen" en ten slotte op "Zoeken". Zorg ervoor dat Bluetooth is ingeschakeld op je smartphone, zodat de detectie van het apparaat soepel verloopt.



![image](assets/fr/12.webp)


Zodra het apparaat is gedetecteerd door de applicatie, klik je erop en kies je "Verbinden". Je komt dan op het scherm waar je de gegevens van je WIFI-verbinding kunt invoeren.


![image](assets/fr/13.webp)


Eenmaal verbonden met uw lokale netwerk, zal uw Mini 3 informatie weergeven zoals IP Address, tijd, Hashrate en elektrisch vermogen.



Hieronder vind je een overzichtstabel met de algemene technische specificaties van de Mini 3:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Aansluiten op een Mining pool



**Dit onderdeel is gemeenschappelijk voor de Nano 3s en Mini 3 apparaten, aangezien de processen strikt identiek zijn **



Of we nu willen "solomineren" of Miner "poolen", we zullen verbinding moeten maken met een Mining pool. In feite is ons apparaat niets meer dan een Hash-maker zonder bewustzijn van het Bitcoin netwerk. Door het met een pool te verbinden, krijgt het toegang tot het Bitcoin netwerk en kan het bloksjablonen ontvangen om aan te werken.



### De toepassing gebruiken om verbinding te maken met een Mining pool



Selecteer het apparaat in de Avalon Family toepassing zoals hieronder getoond. Je wordt dan automatisch gevraagd om het beheerderswachtwoord van het apparaat te wijzigen. Klik op "OK" als je dit wilt doen, of op annuleren om het standaard toegangswachtwoord "admin" te laten staan.


![image](assets/fr/16.webp)


Selecteer vervolgens "Instellingen" en vervolgens "Poolconfiguratie" en voer de parameters in voor de 3 gevraagde pools.


Pools #2 en #3 fungeren als back-ups voor het geval er één uitvalt, zodat je Miner niet voor niets werkt. Standaard zal Hashrate worden toegewezen aan pool #1



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



Typ hiervoor in de zoekbalk van de browser het IP Address van het apparaat dat op het onderstaande scherm wordt getoond, in ons voorbeeld **192.168.144.6**



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



We hebben nu onze Miner thuis aangesloten op ons lokale netwerk en onze Hashrate gericht op pools of Minings. Laten we nu de essentiële functies van onze machine ontdekken via de Avalon Family applicatie.



Klik in het hoofdmenu van de Avalon familieapplicatie op het pictogram dat overeenkomt met de Avalon Mini 3. U komt direct in het menu voor het beheren van de bedrijfsmodi. U komt direct in het menu voor het beheren van de bedrijfsmodi.



er zijn 3 opties beschikbaar: modus "Verwarmen", modus "Mining" of modus "Nacht".





- In de modus "Heater" heb je 2 vermogensniveaus "Eco" of "Super".


Het "Eco"-niveau komt overeen met een verwarmingsvermogen van 500 W voor een Hashrate van ongeveer 25 Th/s en 40 dB voor het geluidsniveau.


Het "Super" niveau komt overeen met een uitgangsvermogen van 650 W bij ongeveer 30Th/s en 45 dB. In deze modus kun je een maximale omgevingstemperatuur instellen waarboven het apparaat niet meer werkt.



![image](assets/fr/36.webp)




- In de "Mining" modus werkt het apparaat op maximale snelheid, zonder de mogelijkheid om een doeltemperatuur in te stellen (afgezien van de ingebouwde oververhittingslimiet natuurlijk). Het doel is om de prestaties van de Miner optimaal te benutten. Hier benadert het uitgangsvermogen 800 W bij ongeveer 37,5 Th/s en een geluidsniveau van 50-55 dB.



![image](assets/fr/37.webp)


Tot slot werkt uw Mini 3 in de "Nacht"-modus op de laagst mogelijke snelheid met een minimum aan geluid. 400 W, 20 Th/s en ongeveer 33 dB.



Ook hier kun je een doeltemperatuur instellen waarboven het apparaat in de inactieve modus gaat en Miner stopt. Als de temperatuur daalt, zal het apparaat opnieuw opstarten en de verwarming en Miner hervatten. In deze modus zijn de display-LED's standaard uitgeschakeld, maar je kunt ervoor kiezen om ze in te schakelen als dat nodig is om de kamer in het donker te verlichten, zoals een nachtlampje (zie onderstaande foto).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Tot slot kun je spelen met de LED's van je Avalon via het menu "Display". Je kunt ervoor kiezen om door de relevante bedrijfsinformatie te scrollen, de tijd weer te geven of zelfs een aangepaste (gepixelde) afbeelding.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Net als bij de Avalon Nano 3S kun je in het menu "Instellingen" het beheerderswachtwoord, de zwembadinstellingen, de filterverstopping (aan de onderkant van het apparaat) controleren, contact opnemen met ondersteuning of de logboeken van het apparaat bekijken.



![image](assets/fr/42.webp)



Nogmaals, het filter aan de onderkant van het apparaat kan worden gereinigd met een stofzuiger, hoe regelmatiger hoe beter.



We zijn aan het einde gekomen van deze tutorial, waarin we hebben geleerd hoe we onze Avalon Mini 3 op ons lokale netwerk kunnen aansluiten, hoe we onze Hashrate op Mining pools kunnen richten en hoe we door opties en instellingen kunnen navigeren met behulp van de Avalon Family applicatie.



Bekijk voor meer informatie onze handleiding over de kleinere versie van de Avalon: de Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6