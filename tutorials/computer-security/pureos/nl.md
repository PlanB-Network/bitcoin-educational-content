---
name: PureOS
description: De Linux-distributie die je controle geeft over je digitale leven.
---

![cover](assets/cover.webp)



Het beschermen van persoonlijke informatie in het digitale tijdperk is een topprioriteit voor elke internetgebruiker. Bedrijven, organisaties en zelfs besturingssystemen zijn nuttige informatiebronnen om je profiel en levensstijl te bepalen. Het kiezen van het juiste besturingssysteem is de eerste stap in het versterken van je online privacy. In deze tutorial bekijken we PureOS, een Linux-distributie die gericht is op privacy.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Aan de slag met PureOS



PureOS is een op Debian gebaseerd besturingssysteem, ontwikkeld door Purism. PureOS is geschikt voor zowel IT-professionals als gebruikers die op zoek zijn naar een eenvoudige, gebruiksvriendelijke distributie. Het is uniek omdat het *Free Software* is en zich richt op de bescherming van de persoonlijke gegevens van zijn gebruikers door het opzetten van een framework gebaseerd op de privacy, vrijheid, veiligheid en stabiliteit die Debian biedt.



### Waarom kiezen voor PureOS?





- Eenvoudig, intuïtief Interface**: GNOME biedt een duidelijke Interface desktop, ontworpen om eenvoudig te gebruiken te zijn, zelfs voor mensen die niet vertrouwd zijn met de commandoregel.





- Gratis**: net als de meeste Linux-distributies is PureOS volledig gratis te gebruiken. Er is echter een maandelijks abonnement beschikbaar om ontwikkelaars te ondersteunen.





- Beveiliging en stabiliteit**: De architectuur en besturingsmodus van PureOS maken het een zeer veilige distributie, die gegevensbescherming en systeemstabiliteit garandeert.





- Documentatie en actieve gemeenschap**: PureOS heeft duidelijke, toegankelijke documentatie en een betrokken, responsieve community, waardoor het eenvoudig is om problemen op te lossen en het systeem stap voor stap te leren.



## Installatie en configuratie



Het installeren en configureren van PureOS op je computer vereist de volgende minimalistische functies:




- Een USB-sleutel van minstens 8 GB om het systeem te flashen.
- 4 GB RAM.
- 30 GB vrije ruimte op uw Hard schijf.



Ga naar de [PureOS official website](https://pureos.net/) en download vervolgens de ISO image van het besturingssysteem volgens de architectuur van je machine.



Om PureOS te installeren, moet je een opstartbare USB-sleutel maken met flashsoftware zoals [Balena Etcher] (https://www.balena.io/etcher).



In drie eenvoudige stappen krijg je een USB-stick die is opgestart met het PureOS-besturingssysteem.





- Sluit de USB-stekker aan en start de gedownloade Balena-software.
- Selecteer dan de PureOS ISO image
- Kies de USB-stick als uitvoerapparaat, klik dan op de knop **Flash** en wacht tot het proces is voltooid.



![0_01](assets/fr/01.webp)



Zodra de USB-sleutel is opgestart, herstart je de computer waarop je PureOS wilt installeren.



Open tijdens het opstarten het BIOS door op de `ESC`, `F9` of `F11` toets te drukken, afhankelijk van je machine. Selecteer de USB-stick als opstartapparaat en druk vervolgens op `ENTER` om te bevestigen.



### Opstartscherm



PureOS biedt verschillende opties voor het opstarten van het besturingssysteem. Kies de optie **Test of Installeer PureOS** om de installatie van het besturingssysteem te starten.



![0_02](assets/fr/02.webp)



Stel de taal en toetsenbordindeling in die je op je computer wilt gebruiken.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Verleen of weiger toegang tot je **geografische locatie** aan applicaties voor gepersonaliseerde aanbevelingen op basis van je gebied.



![0_05](assets/fr/05.webp)



U kunt verbinding maken met uw bestaande **NextCloud**-account om gegevens op te halen die gekoppeld zijn aan de Office-suite die u op een ander systeem gebruikt.



![0_06](assets/fr/06.webp)



Er wordt een tutorial gegeven, maar je kunt het venster sluiten als je deze stap wilt overslaan.



![0_08](assets/fr/08.webp)



### De installatie starten



Klik op het **Activiteiten** menu en verken de applicaties en tools die voorgeïnstalleerd zijn op het systeem. Klik op **Installeer PureOS** om de installatie te starten



![0_09](assets/fr/09.webp)



Stel de systeemtaal en toetsenbordindeling naar wens in en configureer vervolgens de Hard schijfpartitioneringsmodus.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Je hebt twee opties om je Hard schijf te partitioneren:




- Wis schijf**: Voor een volledige installatie van PureOS, waarbij alle reeds bestaande gegevens op je Hard schijf worden gewist.



![0_14](assets/fr/14.webp)





- Handmatig partitioneren** om je eigen scores te maken



⚠️ Wanneer je handmatig partities aanmaakt voor je besturingssysteem, zorg er dan voor dat je een partitie van minimaal 2 GB toewijst voor PureOS en een andere partitie voor gegevens.



![0_15](assets/fr/15.webp)



Activeer **schijfcodering** als je je gegevens wilt beveiligen. Voer een sterk, complex wachtwoord in.



Koppel een gebruiker aan je besturingssysteem door een gebruikersnaam en een alfanumeriek wachtwoord van minstens 20 tekens te definiëren om de beveiliging van je gegevens te versterken.



![0_16](assets/fr/16.webp)



Controleer de instellingen die je hebt gemaakt en wijzig ze indien nodig.



![0_17](assets/fr/17.webp)



Klik op **Installeren** en vervolgens op **Installeer nu** om te bevestigen dat PureOS is geïnstalleerd op je computer.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Wanneer de installatie is voltooid, vinkt u het vakje **Nu herstarten** aan om uw computer opnieuw op te starten en bevestigt u dit:




- De taal.
- Indeling toetsenbord.
- Uw NextCloud-account (optioneel).



![0_25](assets/fr/25.webp)



## Updates



Voordat je PureOS gaat gebruiken, is het essentieel om je systeem bij te werken. Hierdoor profiteer je van de nieuwste functies en beveiligingspatches en ben je verzekerd van meer stabiliteit.





- Update via Interface grafiek**:


Open de toepassing **Software** en ga vervolgens naar het tabblad **Updates**. Beschikbare updates worden automatisch weergegeven. Klik op **Download** en vervolgens op **Installeer** zodra het downloaden is voltooid.





- Update via terminal**:


Open de terminal en voer het volgende commando in om de lijst met beschikbare pakketten bij te werken:



```shell
sudo apt update
```



Voer je wachtwoord in en bevestig. Installeer vervolgens de updates met:



```shell
sudo apt full-upgrade
```



## PureOS voor ontwikkeling



PureOS bevat standaard niet alle tools die nodig zijn voor ontwikkeling.


Je kunt ze snel installeren met het volgende commando:



```shell
sudo apt install build-essential git curl
```



Dit zal de **Git** en **Curl** compilatiegereedschappen installeren, handig in de meeste ontwikkelomgevingen.



## PureOS-omgeving



PureOS onderscheidt zich door zijn innovatieve benadering van echte convergentie: één enkel besturingssysteem zorgt voor een soepele, naadloze werking op verschillende apparaten, waaronder laptops, tablets, mini-pc's en smartphones.



PureOS toepassingen zijn ontworpen om adaptief te zijn: ze passen zich automatisch aan aan de schermgrootte en invoermodus (aanraken of toetsenbord/muis). De GNOME webbrowser past bijvoorbeeld zijn Interface dynamisch aan om een optimale ervaring te bieden op zowel mobiele als desktop apparaten.



PureOS bevat ook de **LibreOffice** office suite, die:





- Writer**: een complete tekstverwerker voor het maken en bewerken van documenten.
- Calc**: een krachtig spreadsheetprogramma voor het beheren van je gegevens en berekeningen.
- Impress**: een hulpmiddel om professionele presentaties te maken.



Met deze gratis suite kun je efficiënt werken zonder afhankelijk te zijn van bedrijfseigen software.



PureOS biedt een uniforme, veilige en flexibele omgeving, gebaseerd op een 100% open source distributie die volledige controle en strikt respect voor privacy garandeert. De echte convergentie maakt het mogelijk om applicaties te maken die compatibel zijn met verschillende soorten apparaten, zoals computers, tablets en smartphones, zonder dat er complexe aanpassingen nodig zijn.



Met native toegang tot essentiële tools, robuuste package managers en een rijk open-source ecosysteem, vereenvoudigt PureOS het ontwikkelen, testen en implementeren van applicaties in een veilige omgeving. De stabiele architectuur en Commitment tot vertrouwelijkheid maken het een betrouwbaar platform voor een verscheidenheid aan toepassingen, waaronder Blockchain ontwikkeling, rapid prototyping of productieomgevingen.



Ontdek onze cursus over het versterken van je beveiliging en het beschermen van je digitale privacy.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1