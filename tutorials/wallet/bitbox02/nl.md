---
name: BitBox02

description: Een BitBox02 instellen en gebruiken
---

![cover](assets/cover.webp)


De BitBox02 (https://bitbox.swiss/) is een fysieke Wallet van Zwitserse makelij, speciaal ontworpen voor het beveiligen van je Bitcoins. Enkele van de belangrijkste kenmerken zijn eenvoudige back-up en herstel met behulp van een microSD-kaart, een minimalistisch en discreet ontwerp en uitgebreide ondersteuning voor Bitcoin.


![device](assets/1.webp)


Het biedt geavanceerde beveiliging, ontworpen door experts, met een dubbel chipontwerp dat een beveiligde chip bevat. De broncode is volledig gecontroleerd door beveiligingsonderzoekers en is volledig open-source. De BitBox02 wordt geleverd met een eenvoudige maar krachtige BitBoxApp, die zorgt voor een veilig beheer van uw Bitcoins. Het ondersteunt Full node voor Bitcoin en zorgt voor end-to-end versleutelde communicatie tussen de app en het apparaat. De BitBox02 is gemaakt in Zwitserland en heeft een positieve reputatie opgebouwd onder zijn gebruikers.


![video](https://youtu.be/sB4b2PbYaj0)


Hier zijn de Wallet specificaties:



- Connectiviteit: USB-C
- Compatibiliteit: Windows 7 en hoger, macOS 10.13 en hoger, Linux, Android
- Invoer: Capacitieve aanraaksensoren
- Microcontroller: ATSAMD51J20A; 120 Mhz 32-bit Cortex-M4F; True random number generator
- Beveiligde chip: ATECC608B; True random number generator (NIST SP 800-90A/B/C)
- Beeldscherm: 128 x 64 px witte OLED
- Materiaal: Polycarbonaat
- Afmetingen: 54,5 x 25,4 x 9,6 mm inclusief USB-C-stekker
- Gewicht: Apparaat 12 g; met verpakking en accessoires 160 g


Download gegevensbladen op hun website https://bitbox.swiss/bitbox02/


## Hoe gebruik je de BitBox02 Hardware Wallet


### De BitBox02 instellen


De BitBox02 heeft een USB-C aansluiting aan de behuizing. Als je computer de gewone USB-poort gebruikt, moet je de adapter gebruiken die bij het apparaat wordt geleverd.


Sluit het aan op je computer en het apparaat wordt ingeschakeld (nog niet doen).


Het heeft sensoren boven en onder, en het zal je vragen om de boven- of onderkant aan te raken om het scherm te oriënteren zoals jij dat wilt.


![image](assets/2.webp)


### De BitBox02-app downloaden


Ga naar https://shiftcrypto.ch/ en klik op de link "App" bovenaan om naar de downloadpagina te gaan:


![image](assets/3.webp)


Klik op de blauwe knop Downloaden:


![image](assets/4.webp)


Zie Appendix A om de download te verifiëren (het maakt het complexer, maar aanbevolen, vooral als je veel Bitcoin opslaat).


Na het downloaden kunt u het bestand uitpakken. Op een mac dubbelklik je gewoon op het gedownloade bestand en er verschijnt een BitBox App-pictogram in je downloadmap. Je kunt het naar je bureaublad slepen (of waar dan ook) voor gemakkelijke toegang.


Dubbelklik op de app om hem uit te voeren (hij wordt niet "geïnstalleerd").


Op de Mac zal je computer nanny je een waarschuwing geven. Negeer deze gewoon en klik op "openen":


![image](assets/5.webp)


Je ziet dan dit:


![image](assets/6.webp)


Sluit het apparaat aan op de computer.


Er wordt een koppelcode weergegeven. Controleer of ze overeenkomen en raak dan de sensor aan om het vinkje te selecteren. Ga dan terug naar het scherm en de knop Doorgaan wordt voor je beschikbaar.


![image](assets/7.webp)


Je hebt dan de optie om een nieuwe seed te maken, of een seed te herstellen. Ik demonstreer het maken van een nieuwe seed (het is belangrijk om de seed die je hebt gemaakt ook te herstellen om de kwaliteit van je back-up te testen, voordat je Bitcoin op de Wallet laadt).


![image](assets/8.webp)


Het apparaat werd geleverd met een microSD-kaart. Plaats hem als je dat nog niet hebt gedaan.


![image](assets/9.webp)


Geef je apparaat een naam en klik op Doorgaan.


![image](assets/10.webp)


Je wordt dan gevraagd om een wachtwoord in te stellen voor het apparaat. Dit is geen onderdeel van je seed. Het is ook geen passphrase (dat is onderdeel van je seed). Het is gewoon een wachtwoord om het apparaat te vergrendelen. Wanneer je het apparaat inschakelt, wordt je telkens gevraagd dit wachtwoord in te voeren. Je mag 10 keer achter elkaar falen voordat het apparaat zichzelf van alle geheugen wist, dus wees voorzichtig. De animatie op het scherm leert je hoe je het apparaat moet bedienen om het wachtwoord in te stellen.


![image](assets/11.webp)


Lees het volgende scherm en vink elk vakje aan, ga dan verder.


![image](assets/12.webp)

![image](assets/13.webp)

![image](assets/14.webp)


En zo ziet de Wallet eruit als hij klaar is voor gebruik.


![image](assets/15.webp)


### NIET ZO SNEL!!!


Het is heel vreemd, maar de BitBox02 vertelt ons dat we klaar zijn om het apparaat te gebruiken, maar het heeft ons niet gepromoot om de seed woorden op te schrijven! De ENIGE back-up die we hebben is het bestand dat is opgeslagen op de microSD-kaart. Dit is onvoldoende. Deze opslagapparaten gaan niet eeuwig mee (door "bitrot"). We hebben een papieren back-up nodig, en duplicaten, bewaard in een kluis (zoals uitgelegd in de algemene hoe-te-gebruiken-hardware-wallets gids)


Om onze seed zin te krijgen en op te schrijven, ga je naar het tabblad "apparaat beheren" aan de linkerkant en klik je op "herstelwoorden weergeven"


![image](assets/16.webp)


Je kunt dan de bevestiging doorlopen en het apparaat zal je de woorden presenteren. Schrijf ze netjes op en laat niemand de woorden zien.


![image](assets/17.webp)


Daarna kun je op het tabblad Bitcoin aan de linkerkant klikken om je ontvangstadressen te krijgen.


![image](assets/18.webp)


Het laat er één tegelijk zien, maar het laat je tenminste kiezen welke Address je wilt gebruiken uit de eerste 20:


![image](assets/19.webp)


Als je op de blauwe knop klikt, wordt de volledige Address getoond en wordt je gevraagd om te controleren of de Address overeenkomt met de weergave op het scherm. Dit is een goede manier om te controleren of er geen malware op je computer staat die je misleidt om Bitcoin naar de Address van een aanvaller te sturen.


![image](assets/20.webp)


Om Bitcoin naar deze Wallet te sturen, kun je de Address kopiëren en plakken in de opnamepagina van de Exchange waar je munten zijn. Ik raad je aan om eerst een klein testbedrag te sturen, en dan te oefenen met het uitgeven naar de Exchange of naar de tweede Address in je Wallet.


Voor grotere hoeveelheden stel ik voor dat je een passphrase maakt (zie hieronder). De originele Wallet (geen passphrase) kan gebruikt worden als je lok Wallet (er moet een redelijke hoeveelheid in zitten om het een geloofwaardige lok te laten zijn).


### Verbinding maken met een knooppunt


De BitBox02 maakt automatisch verbinding met een knooppunt. Laten we eens kijken waar hij verbinding mee maakt. Klik op de instellingentab aan de linkerkant en dan op "je eigen Full node verbinden".


![image](assets/21.webp)


En hier kunnen we zien dat het verbinding maakt met het knooppunt van shiftcrypto. Niet geweldig. We hebben al onze Bitcoin adressen aan hen verraden, en onze IP Address (niet de seed natuurlijk; ze kunnen onze adressen/balansen zien, maar ze niet uitgeven). We kunnen onze eigen node details op deze pagina invoeren (buiten het bereik van deze gids), of we kunnen betere software gebruiken zoals Sparrow Bitcoin Wallet, Electrum Desktop Wallet, of Specter Desktop. Ik zal Sparrow Bitcoin Wallet later in de gids demonstreren.


![image](assets/22.webp)


Een passphrase toevoegen


Nu we het apparaat hebben ingesteld met de BitBox02 App (en onze adressen hebben onthuld, onvermijdelijk met deze Hardware Wallet), kunnen we een passphrase toevoegen aan onze seed zin. Hierdoor kunnen we een nieuwe Wallet aanmaken met dezelfde seed en ShiftCrypto zal onze nieuwe adressen nooit te zien krijgen. We verbinden deze Wallet alleen met onze eigen software.


### passphrase inschakelen


Zet nu de passphrase functie aan (maar we stellen nog geen passphrase in). Ga naar het tabblad "apparaat beheren" en klik op "passphrase inschakelen" (rode cirkel hieronder).


![image](assets/23.webp)


Lees de stappen door..


![image](assets/24.webp)

![image](assets/25.webp)

![image](assets/26.webp)


Koppel nu het apparaat los en sluit de BitBox02 App af


EINDE van de bitbox02 sectie door Parman.


Je divice is nu volledig operationeel en kan worden gebruikt op elke desktopoplossing zoals Specter, Sparrow en met de bitbox Interface.