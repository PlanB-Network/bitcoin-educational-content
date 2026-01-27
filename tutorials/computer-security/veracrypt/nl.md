---
name: VeraCrypt
description: Hoe kan ik eenvoudig een opslagapparaat versleutelen?
---
![cover](assets/cover.webp)


Tegenwoordig is het belangrijk om een strategie te implementeren om de toegankelijkheid, veiligheid en back-up van je bestanden te garanderen, zoals je persoonlijke documenten, foto's of belangrijke projecten. Het verlies van deze gegevens kan rampzalig zijn.


Om deze problemen te voorkomen, raad ik je aan om meerdere back-ups van je bestanden op verschillende media te bewaren. Een veelgebruikte strategie in de computerwereld is de "3-2-1" back-up strategie, die de bescherming van je bestanden garandeert:


- 3 **kopieën** van je bestanden;
- Opgeslagen op minstens **2** verschillende soorten media;
- Met ten minste **1** kopie op een externe locatie.


Met andere woorden, het is aan te raden om je bestanden op 3 verschillende locaties op te slaan, met behulp van media van verschillende aard, zoals je computer, een externe Hard schijf, een USB-stick of een online opslagdienst. En tot slot betekent het hebben van een offsite kopie dat je een back-up moet hebben die buiten je huis of bedrijf is opgeslagen. Dit laatste punt helpt om het totale verlies van je bestanden te voorkomen in het geval van lokale rampen zoals brand of overstromingen. Een externe kopie, ver weg van je huis of bedrijf, zorgt ervoor dat je gegevens overleven, onafhankelijk van lokale risico's.


Om deze 3-2-1 back-upstrategie eenvoudig te implementeren, kun je kiezen voor een online opslagoplossing, door automatisch of periodiek de bestanden van je computer te synchroniseren met die in je cloud. Onder deze online back-upoplossingen zijn er natuurlijk die van de grote digitale bedrijven die je kent: Google Drive, Microsoft OneDrive of Apple iCloud. Dit zijn echter niet de beste oplossingen om je privacy te beschermen. In een eerdere tutorial heb ik je kennis laten maken met een alternatief dat je documenten versleutelt voor betere privacy: Proton Drive.


https://planb.academy/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Door deze strategie van lokale en cloudback-ups toe te passen, profiteert u al van twee verschillende soorten media voor uw gegevens, waarvan één offsite. Om de 3-2-1 strategie compleet te maken, hoeft u alleen maar een extra kopie toe te voegen. Wat ik je aanraad is om je gegevens die lokaal en in de cloud staan periodiek te exporteren naar een fysiek medium, zoals een USB-stick of een externe Hard schijf. Op deze manier, zelfs als de servers van je online opslagoplossing worden vernietigd en je computer tegelijkertijd uitvalt, heb je nog steeds deze derde kopie op een extern medium om je gegevens niet te verliezen.

![VeraCrypt](assets/notext/01.webp)

Maar het is ook belangrijk om na te denken over de beveiliging van je gegevensopslag om ervoor te zorgen dat niemand anders dan jij of je dierbaren er toegang toe hebben. Zowel lokale als online gegevens zijn normaal gesproken beveiligd. Op je computer heb je waarschijnlijk een wachtwoord ingesteld en de Hard schijven van moderne computers zijn vaak standaard versleuteld. Wat betreft je online opslag (cloud), heb ik je in de vorige tutorial laten zien hoe je je account kunt beveiligen met een sterk wachtwoord en twee-factor authenticatie. Maar voor je derde kopie die is opgeslagen op een fysieke drager, is de enige beveiliging het fysieke bezit ervan. Als een inbreker erin slaagt om je USB-stick of je externe Hard schijf te stelen, kunnen ze gemakkelijk toegang krijgen tot al je gegevens.

![VeraCrypt](assets/notext/02.webp)

Om dit risico te voorkomen, is het raadzaam om je fysieke medium te versleutelen. Bij elke poging om toegang te krijgen tot de gegevens, moet je dus een wachtwoord invoeren om de inhoud te ontsleutelen. Zonder dit wachtwoord is het onmogelijk om toegang te krijgen tot de gegevens, waardoor je persoonlijke bestanden zijn beveiligd, zelfs in het geval van diefstal van je USB-stick of je externe Hard schijf.

![VeraCrypt](assets/notext/03.webp)

In deze tutorial laat ik je zien hoe je eenvoudig een extern opslagmedium kunt versleutelen met VeraCrypt, een open-source tool.


## Inleiding tot VeraCrypt


VeraCrypt is open-source software voor Windows, macOS en Linux waarmee je gegevens op verschillende manieren en op verschillende media kunt versleutelen.

![VeraCrypt](assets/notext/04.webp)

Met deze software kunnen versleutelde volumes on the fly worden aangemaakt en onderhouden, wat betekent dat je gegevens automatisch worden versleuteld voordat ze worden opgeslagen en ontsleuteld voordat ze worden gelezen. Deze methode zorgt ervoor dat je bestanden beschermd blijven, zelfs in het geval van diefstal van je opslagmedium. VeraCrypt versleutelt niet alleen bestanden, maar ook bestandsnamen, metagegevens, mappen en zelfs de vrije ruimte op je opslagmedium.


VeraCrypt kan worden gebruikt om bestanden lokaal of hele partities te versleutelen, inclusief de systeemschijf. Het kan ook worden gebruikt om een extern medium zoals een USB-stick of een schijf volledig te versleutelen, zoals we in deze tutorial zullen zien.


Een groot voordeel van VeraCrypt ten opzichte van propriëtaire oplossingen is dat het volledig open source is, wat betekent dat de code door iedereen kan worden geverifieerd.


## Hoe installeer je VeraCrypt?


Ga naar [de officiële website van VeraCrypt](https://www.veracrypt.fr/en/Downloads.html) op het tabblad "*Downloads*".

![VeraCrypt](assets/notext/05.webp)

Download de versie die geschikt is voor jouw besturingssysteem. Als je Windows gebruikt, kies dan "*EXE Installer*".

![VeraCrypt](assets/notext/06.webp)

Kies de taal voor uw Interface.

![VeraCrypt](assets/notext/07.webp)

Accepteer de voorwaarden van de licentie.

![VeraCrypt](assets/notext/08.webp)

Selecteer "*Installeren*".

![VeraCrypt](assets/notext/09.webp)

Kies ten slotte de map waarin de software wordt geïnstalleerd en klik vervolgens op de knop "*Install*".

![VeraCrypt](assets/notext/10.webp)

Wacht tot de installatie voltooid is.

![VeraCrypt](assets/notext/11.webp)

De installatie is voltooid.

![VeraCrypt](assets/notext/12.webp)

Als je wilt, kun je een donatie doen in bitcoins om de ontwikkeling van deze open-source tool te steunen.

![VeraCrypt](assets/notext/13.webp)

## Hoe versleutel je een opslagapparaat met VeraCrypt?


Bij de eerste lancering kom je aan bij deze Interface:

![VeraCrypt](assets/notext/14.webp)

Om het opslagapparaat van je keuze te versleutelen, begin je met het aan te sluiten op je machine. Zoals je later zult zien, zal het proces van het creëren van een nieuw versleuteld volume op een USB-stick of een Hard schijf veel langer duren als het apparaat al gegevens bevat die je niet wilt verwijderen. Daarom raad ik aan om een lege USB-stick te gebruiken of het apparaat vooraf leeg te maken om het versleutelde volume aan te maken, om tijd te besparen.


Klik in VeraCrypt op het tabblad "*Volumes*".

![VeraCrypt](assets/notext/15.webp)

Ga dan naar het menu "*Create New Volume...*".

![VeraCrypt](assets/notext/16.webp)

Selecteer in het nieuwe venster dat wordt geopend de optie "*Encrypt a non-system partition/drive*" en klik op "*Next*".

![VeraCrypt](assets/notext/17.webp)

Je moet dan kiezen tussen "*Standaard VeraCrypt-volume*" en "*Verborgen VeraCrypt-volume*". Met de eerste optie maak je een standaard gecodeerd volume op je apparaat. Met de optie "*Verborgen VeraCrypt-volume*" kun je een verborgen volume maken binnen een standaard VeraCrypt-volume. Met deze methode kun je het bestaan van dit verborgen volume ontkennen in geval van dwang. Als iemand je bijvoorbeeld fysiek dwingt om je apparaat te ontsleutelen, kun je alleen het standaardgedeelte ontsleutelen om de aanvaller tevreden te stellen, maar het verborgen gedeelte niet onthullen. In mijn voorbeeld zal ik het houden bij een standaard volume.

![VeraCrypt](assets/notext/18.webp)

Klik op de volgende pagina op de knop "*Selecteer apparaat...*".

![VeraCrypt](assets/notext/19.webp)

Er wordt een nieuw venster geopend waarin je de partitie van je opslagapparaat kunt selecteren uit de lijst met beschikbare schijven op je machine. Normaal gesproken wordt de partitie die je wilt versleutelen weergegeven onder een regel met de titel "*Removable Disk N*". Nadat je de juiste partitie hebt geselecteerd, klik je op de knop "*OK*".

![VeraCrypt](assets/notext/20.webp)

De geselecteerde ondersteuning verschijnt in het vak. Je kunt nu op de knop "*Volgende*" klikken. veraCrypt](assets/notext/21.webp)

Vervolgens moet je kiezen tussen de opties "*Sleutel versleuteld volume en formatteer het*" of "*Encrypt partition in place*". Zoals eerder vermeld, zal de eerste optie alle gegevens op je USB-stick of Hard schijf permanent verwijderen. Kies deze optie alleen als je apparaat leeg is; anders verlies je alle gegevens die erop staan. Als je bestaande gegevens wilt behouden, kun je ze tijdelijk ergens anders onderbrengen, kies "*Sleutel versleuteld volume en formatteer het*" voor een sneller proces dat alles wist, of kies voor "*Encrypt partition in place*". Met deze laatste optie kun je het volume versleutelen zonder de reeds aanwezige gegevens te wissen, maar het proces zal veel langer duren. Voor dit voorbeeld, aangezien mijn USB-stick leeg is, selecteer ik "*Sleutel versleuteld volume en formatteer het*", de optie die alles wist.

![VeraCrypt](assets/notext/22.webp)

Vervolgens heb je de mogelijkheid om het versleutelingsalgoritme en de Hash functie te kiezen. Tenzij je specifieke behoeften hebt, raad ik je aan om de standaardopties te behouden. Klik op "*Next*" om verder te gaan.

![VeraCrypt](assets/notext/23.webp)

Zorg ervoor dat de aangegeven grootte voor uw volume correct is, om de volledige beschikbare ruimte op de USB-stick te versleutelen, en niet slechts een deel. Klik na controle op "*Next*".

![VeraCrypt](assets/notext/24.webp)

In dit stadium moet je een wachtwoord instellen om je apparaat te versleutelen en te ontsleutelen. Het is belangrijk om een sterk wachtwoord te kiezen om te voorkomen dat een aanvaller je inhoud kan ontsleutelen met brute force-aanvallen. Het wachtwoord moet willekeurig zijn, zo lang mogelijk en verschillende soorten tekens bevatten. Ik raad je aan om te kiezen voor een willekeurig wachtwoord van ten minste 20 tekens, waaronder kleine letters, hoofdletters, cijfers en symbolen.


Ik raad je ook aan om je wachtwoord op te slaan in een wachtwoordmanager. Dit maakt het gemakkelijker om toegang te krijgen en elimineert het risico op vergeten. Voor ons specifieke geval is een wachtwoordmanager te verkiezen boven een papieren drager. In het geval van een inbraak kan je opslagapparaat weliswaar worden gestolen, maar het wachtwoord in de manager kan niet worden gevonden door de aanvaller, waardoor toegang tot de gegevens wordt voorkomen. Omgekeerd, als je wachtwoordmanager gecompromitteerd is, is fysieke toegang tot het apparaat nog steeds nodig om het wachtwoord te achterhalen en toegang te krijgen tot de gegevens.


Voor meer informatie over het beheren van wachtwoorden raad ik je aan om deze andere complete tutorial te lezen:


https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Voer je wachtwoord in de 2 daarvoor bestemde velden in en klik dan op "*Next*". veraCrypt] (activa/notext/25.webp)

VeraCrypt zal je dan vragen of je van plan bent om bestanden groter dan 4 GiB op te slaan in het versleutelde volume. Met deze vraag kan de software het meest geschikte bestandssysteem selecteren. Over het algemeen wordt het FAT-systeem gebruikt omdat dit compatibel is met de meeste besturingssystemen, maar het legt een maximale bestandsgrootte van 4 GB op. Als je grotere bestanden moet beheren, kun je kiezen voor het exFAT-systeem.

![VeraCrypt](assets/notext/26.webp)

Vervolgens kom je op een pagina waar je generate een willekeurige sleutel kunt geven. Deze sleutel is belangrijk, want hij wordt gebruikt om je gegevens te versleutelen en te ontsleutelen. Hij wordt opgeslagen in een specifieke sectie van je media, zelf beveiligd door het wachtwoord dat je eerder hebt ingesteld. Om generate een sterke coderingssleutel te maken, heeft VeraCrypt entropie nodig. Daarom vraagt de software je om je muis willekeurig over het venster te bewegen; deze bewegingen worden dan gebruikt om de sleutel generate te maken. Blijf de muis bewegen totdat de entropiemeter volledig gevuld is. Klik dan op "*Format*" om het versleutelde volume aan te maken.

![VeraCrypt](assets/notext/27.webp)

Wacht tot het formatteren klaar is. Dit kan lang duren voor grote volumes.

![VeraCrypt](assets/notext/28.webp)

Je ontvangt dan een bevestiging.

![VeraCrypt](assets/notext/29.webp)

## Hoe gebruik je een versleutelde schijf met VeraCrypt?


Op dit moment zijn je media versleuteld en kun je ze daarom niet openen. Ga naar VeraCrypt om het te decoderen.

![VeraCrypt](assets/notext/30.webp)

Selecteer een stationsletter uit de lijst. Ik heb bijvoorbeeld "*L:*" gekozen.

![VeraCrypt](assets/notext/31.webp)

Klik op de knop "*Selecteer apparaat...*".

![VeraCrypt](assets/notext/32.webp)

Selecteer in de lijst met alle schijven op je machine het versleutelde volume op je media en klik vervolgens op de knop "*OK*".

![VeraCrypt](assets/notext/33.webp)

Je kunt zien dat je volume goed geselecteerd is.

![VeraCrypt](assets/notext/34.webp)

Klik op de knop "*Mount*".

![VeraCrypt](assets/notext/35.webp)

Voer het wachtwoord in dat is gekozen tijdens het aanmaken van het volume en klik vervolgens op "*OK*".

![VeraCrypt](assets/notext/36.webp)

Je kunt zien dat je volume nu is gedecodeerd en toegankelijk is op de stationsletter "*L:*".

![VeraCrypt](assets/notext/37.webp)

Om toegang te krijgen, open je de bestandsverkenner en ga je naar het station "*L:*" (of een andere letter, afhankelijk van de letter die je in de vorige stappen hebt gekozen). veraCrypt](assets/notext/38.webp)

Nadat je je persoonlijke bestanden hebt toegevoegd aan de media, klik je gewoon op de knop "*Dismount*" om het volume opnieuw te coderen.

![VeraCrypt](assets/notext/39.webp)

Je volume verschijnt niet meer onder de letter "*L:*". Het is dus opnieuw gecodeerd.

![VeraCrypt](assets/notext/40.webp)

U kunt nu uw opslagmedia verwijderen.


Gefeliciteerd, je hebt nu een versleuteld medium om je persoonlijke gegevens veilig op te slaan, dus je hebt een complete 3-2-1 strategie naast de kopie op je computer en je online opslagoplossing.


Als je de ontwikkeling van VeraCrypt wilt steunen, kun je ook een donatie doen in bitcoins [op deze pagina](https://www.veracrypt.fr/en/Donation.html).