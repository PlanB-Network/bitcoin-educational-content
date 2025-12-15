---
name: Windows 11
description: Automatische installatie van Microsoft Windows 11 via configuratiebestand
---
![cover](assets/cover.webp)


In deze zelfstudie leren we hoe je Windows 11 automatisch installeert met een andere methode dan het standaard installatieproces van Windows.


## Downloaden!


Het eerste wat je nodig hebt is een installatiebestand. De veiligste en meest betrouwbare plaats om het te downloaden is rechtstreeks van de officiële website van Microsoft.


Ga gewoon naar de onderstaande koppeling en volg de instructies om het [Windows 11 ISO-bestand] (https://www.microsoft.com/en-us/software-download/windows11) te downloaden


![Image](assets/en/02.webp)


Als je op de downloadpagina bent, scroll je naar beneden naar de sectie voor het downloaden van het ISO-bestand.


![Image](assets/en/01.webp)


َEn kies de juiste versie.


![Image](assets/en/03.webp)


Klik na het selecteren van Windows 11 op de knop Bevestigen.


In deze stap kan het enkele seconden duren om de aanvraag te verwerken, waarna je de volgende pagina te zien krijgt:


![Image](assets/en/04.webp)


Nadat je de aanvraag hebt bevestigd, moet je de taal van je voorkeur kiezen.


![Image](assets/en/05.webp)


Nadat je de taal hebt geselecteerd en op de knop Bevestigen hebt geklikt, wordt de aanvraag verwerkt. Deze stap kan enkele seconden duren.


Zodra de aanvraag succesvol is verwerkt, zie je een pagina met de downloadlink voor het .iso-bestand. Klik op de knop 64-bits downloaden om het downloaden te starten.


Het bestand is ongeveer 5,5 GB groot en de gegenereerde link is 24 uur geldig.


## Automatisering!


In dit stadium moeten we wijzigingen aanbrengen in de standaard Windows-installatie. In dit stadium bepalen we met behulp van Unattended install welke onderdelen worden geïnstalleerd, zonder dat de gebruiker daar achteraf iets voor hoeft te doen. In feite wordt bij deze methode een XML-bestand gebruikt om de installatiestappen en de geïnstalleerde services in Windows te configureren. Met andere woorden, het gebruik van het bestand Unattended.xml creëert een automatiseringsproces tijdens de installatie, waardoor het niet nodig is om meerdere opties te selecteren en de vervelende stappen die meestal nodig zijn tijdens de installatie worden vermeden. Deze methode is een ongebruikelijke maar standaardmethode die door Microsoft is geïntroduceerd. Meer informatie is beschikbaar op [officiële website van Microsoft](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Er zijn verschillende tools beschikbaar op het internet voor het genereren van Unattended bestanden. Sommige zijn online, andere offline. Een van de online tools voor het maken van dit bestand is [deze website] (https://schneegans.de/windows/unattend-generator). Na het openen krijgen we de volgende pagina te zien:


![Image](assets/en/06.webp)


Zoals bovenaan de pagina vermeld, kan deze methode worden gebruikt voor het installeren van Windows 10 en 11. In de eerste stap selecteren we de Windows-taal. Als we een tweede of zelfs een derde taal moeten toevoegen aan de lijst met Windows display- en toetsenbord talen, kunnen we het vak hieronder gebruiken:


![Image](assets/en/07.webp)


In de volgende stap selecteren we de gewenste locatie.


![Image](assets/en/08.webp)


In dit stadium kunnen we ook de processorarchitectuur voor de computer specificeren. In deze stap kunnen we:

1. Beslis of je de beveiligingsfuncties van Windows, zoals TPM en Secure Boot, wilt negeren. De Secure Boot-functie zorgt ervoor dat als er tijdens het opstartproces met Windows-kernbestanden wordt geknoeid, het probleem wordt gedetecteerd en de uitvoering ervan wordt voorkomen. Deze functie helpt ook om het systeem te beschermen tegen het installeren van schadelijke updates op Windows. Het inschakelen van de optie om deze functies te omzeilen is soms onvermijdelijk op bepaalde computers, vooral oudere modellen. Over het algemeen wordt echter aanbevolen om functies zoals Secure Boot ingeschakeld te laten.

2. Negeer de vereiste van een internetverbinding om het proces te voltooien. Dit is handig in situaties waarin een bekabelde LAN-verbinding niet beschikbaar is, omdat in de meeste gevallen de draadloze kaart nog niet wordt herkend tijdens de installatie van Windows en internettoegang via de kabel vereist is. Door deze optie te activeren worden problemen met deze stap opgelost.


In de volgende stap kunnen we een naam kiezen voor de computer.


![Image](assets/en/09.webp)


We kunnen Windows ook een naam laten kiezen voor het systeem. In deze stap kunnen we het type Windows selecteren, gecomprimeerd of ongecomprimeerd, of Windows de juiste versie laten bepalen op basis van de specificaties van de computer. In dit stadium kan ook de tijdzone worden ingesteld.


De volgende stap betreft de partitie-instellingen:


![Image](assets/en/10.webp)


In dit stadium kunnen we het partitietype voor de installatie van Windows opgeven, evenals de vereiste instellingen voor de installatie van de Windows Recovery Environment. Door de eerste optie te selecteren, worden de partitieselectie en partitionering uitgesteld tot het moment van installatie van Windows en tijdens de installatie worden deze vragen gesteld net zoals bij de normale installatiemethode.


In deze stap selecteren we de versie van Windows die we willen installeren:


![Image](assets/en/11.webp)


Als er een productsleutel beschikbaar is, kan die ook in dit stadium worden ingevoerd.


De volgende stap is het configureren van de Windows aanmeldaccount:


![Image](assets/en/12.webp)


## Account vergaderingen


In dit stadium:


1. We kunnen een naam en wachtwoord instellen voor de beheerdersaccount. Het is ook mogelijk om meerdere gebruikers- of beheerdersaccounts aan te maken.

2. Hier geven we aan bij welk account we ons de eerste keer na de installatie van Windows moeten aanmelden. De verschillende opties voor dit gedeelte worden weergegeven in de afbeelding.

3. Als je niet wilt dat er accounts worden aangemaakt, maak dan alle accounts leeg en selecteer deze optie. In dit geval wordt u na de installatie van Windows automatisch aangemeld bij het Windows Administrator-account.


De volgende stap is het configureren van wachtwoord- en hostbestandinstellingen:


![Image](assets/en/13.webp)


In dit stadium bepalen we of wachtwoorden een vervalperiode moeten hebben. Daarnaast bevat dit gedeelte beveiligingsinstellingen met betrekking tot mislukte aanmeldpogingen, die kunnen worden in- of uitgeschakeld op basis van je behoeften.


Onderaan deze sectie staan instellingen voor de weergave van bestanden. Geen van deze opties zijn beschikbaar tijdens een standaard Windows-installatie en moeten na de installatie worden geconfigureerd. Met de methode voor installatie zonder toezicht zijn deze instellingen wel gemakkelijk toegankelijk.


De volgende stap is het configureren van de beveiligingsinstellingen van Windows:


![Image](assets/en/14.webp)


## Beveiligingsinstellingen


In dit stadium:


1. Windows Defender kan worden in- of uitgeschakeld. Deze functie werkt als beveiligingssoftware in Windows en helpt de uitvoering van kwaadaardige bestanden, bepaalde netwerkaanvallen en meer te voorkomen.

2. Automatische Windows-updates kunnen worden uitgeschakeld. Dit is een van de meest voorkomende uitdagingen voor Windows gebruikers!

3. Met dit onderdeel kun je UAC (User Account Control) in- of uitschakelen. Deze functie voorkomt dat verdachte toepassingen worden uitgevoerd met verhoogde lees- en schrijfrechten.

4. Deze functie wordt door Windows gebruikt om mogelijk schadelijke software te detecteren.

5. Ondersteuning voor lange paden in Windows-toepassingen, zoals PowerShell en andere, in- of uitschakelen.

6. Remote Desktop in- of uitschakelen voor externe toegang tot het systeem.


Afhankelijk van de gebruikte Windows-versie worden sommige van deze functies wel of niet ondersteund.


De volgende stap is het configureren van de pictogrammen:


![Image](assets/en/15.webp)


In deze sectie:


1. Bureaubladpictogrammen worden weergegeven en kunnen naar wens worden toegevoegd of verwijderd.

2. Er worden startmenupictogrammen weergegeven, die ook kunnen worden toegevoegd of verwijderd op basis van de vereisten.

3. In dit gedeelte kan worden geconfigureerd of virtualisatiegereedschappen al dan niet worden geïnstalleerd. Deze optie is specifiek voor Windows 11 en geldt niet voor Windows 10.


De volgende stap is het configureren van de Wi-Fi-instellingen:


![Image](assets/en/16.webp)


In dit gedeelte kunnen de Wi-Fi-netwerkinstellingen worden geconfigureerd. Zoals eerder vermeld, wordt de Wi-Fi-kaart in de meeste gevallen niet herkend tijdens de installatie van Windows, dus verbinding maken tijdens de installatie is meestal niet mogelijk. Door dit gedeelte te configureren, kan het systeem echter verbinding maken met het internet als de draadloze kaart wordt gedetecteerd.


De volgende stap betreft een belangrijke instelling:


![Image](assets/en/17.webp)


In dit gedeelte geven we aan of informatie over systeemproblemen wel of niet naar Microsoft moet worden gestuurd.


De volgende stap is het configureren van standaardtoepassingen:


![Image](assets/en/18.webp)


## Standaard software in-/uitschakelen


In dit gedeelte kunnen we toepassingen kiezen die we niet standaard willen installeren. We kunnen er bijvoorbeeld voor kiezen om Cortana of Copilot niet te installeren.


De volgende stap betreft de beveiligingsinstellingen met betrekking tot het uitvoeren van applicaties:


![Image](assets/en/19.webp)


Door WDAC-instellingen toe te passen, kan de uitvoering van bepaalde toepassingen worden voorkomen.


Nadat de gewenste instellingen zijn toegepast, kan het gegenereerde XML-bestand worden gedownload:


![Image](assets/en/20.webp)


Door op Download XML File te klikken, wordt het autounattend.xml bestand gedownload. Om dit bestand te gebruiken, koppel je de gedownloade ISO op een USB-stick, plaats je het autounattend.xml-bestand in de hoofdmap en ga je verder met de Windows-installatie.


Een van de beschikbare tools voor het maken van een opstartbaar USB-station is Rufus. Rufus kan een opstartbare Windows installatie flash drive maken, met een gegeven Windows installatie ISO bestand. Het is snel en eenvoudig, je kunt het [hier] downloaden (https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


In deze software klikken we op Start nadat we het gewenste USB-station en het juiste ISO-bestand hebben geselecteerd.


![Image](assets/en/22.webp)


In dit stadium schakelen we alle opties uit, omdat het inschakelen van deze opties conflicten kan veroorzaken bij het gebruik van het gegenereerde Unattend-bestand. Nadat de bestanden naar de USB drive zijn gekopieerd, plaatsen we het autounattend.xml bestand in de root directory:


![Image](assets/en/23.webp)


Op dit punt is het USB-station klaar voor gebruik om Windows automatisch te installeren en kan de installatie worden gestart met dit station.


## ISO bewerken


Als je Windows op een virtuele machine moet installeren, kun je software gebruiken om ISO-bestanden te maken en te bewerken. Een dergelijke software is AnyBurn. Na het uitpakken van de inhoud van het ISO-bestand dat je hebt gedownload van de Microsoft-website, plaats je het autounattend.xml-bestand in de hoofdmap. Maak vervolgens met AnyBurn een nieuwe ISO met de bijgewerkte inhoud.


AnyBurn is een multifunctionele software voor het werken met ISO-bestanden. Het biedt verschillende functies voor het omgaan met ISO-bestanden, waaronder het maken van opstartbare ISO-images; [hier](https://www.anyburn.com/download.php) is de originele website.


Selecteer op de hoofdpagina van de software "Afbeelding maken van bestand/map":


![Image](assets/en/24.webp)


Op de volgende pagina selecteer je alle bestanden die uit de ISO zijn gehaald, samen met het autounattend.xml bestand.


![Image](assets/en/25.webp)


In deze stap configureren we de instellingen om het ISO-bestand bootable te maken:


![Image](assets/en/26.webp)


In dit stadium moet het pad naar het bestand bootfix.bin worden ingesteld om de ISO bootable te maken. Dit bestand bevindt zich in de root van de ISO, in de bootmap. Het wordt ook aanbevolen om zowel de ISO9660 als de UDF opties in te schakelen in het gedeelte Eigenschappen.


![Image](assets/en/27.webp)


Na deze stap kun je op Volgende klikken om het ISO-bestand te maken. Dit bestand kan worden gebruikt in virtualisatiesoftware zoals Oracle VirtualBox. Hieronder vind je een tutorial over VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65