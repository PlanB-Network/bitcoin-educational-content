---
name: Aegis Authenticator
description: Hoe kunt u Aegis Authenticator gebruiken om uw accounts te beveiligen met dubbele verificatie?
---

![cover](assets/cover.webp)



Tegenwoordig is twee-factor authenticatie (2FA) essentieel voor het beveiligen van online accounts. Naast het wachtwoord voegt het een tweede factor toe (vaak een 6-cijferige code) die na 30 seconden verloopt, wat het hackers aanzienlijk moeilijker maakt. Het gebruik van een speciale TOTP-applicatie (*Time-based One-Time Password*) is veiliger dan sms, die kan worden gekaapt door SIM-swapping aanvallen.



Niet alle authenticatietoepassingen zijn echter gelijk. Veel propriëtaire oplossingen (Google Authenticator, Authy, enz.) brengen problemen met zich mee: ze zijn propriëtair en closed-source (onmogelijk om hun beveiliging te controleren), integreren soms reclametrackers, bieden geen versleutelde back-up van je codes en kunnen zelfs het exporteren van je accounts verhinderen om je in hun ecosysteem te vergrendelen.



Aegis Authenticator daarentegen presenteert zichzelf als een gratis en ethisch alternatief voor deze applicaties. Aegis is een gratis, veilige, open-source applicatie voor het beheren van je tweestapsverificatie tokens op Android. De ontwikkeling ervan richt zich op essentiële functies die andere apps niet bieden, zoals robuuste versleuteling van lokale gegevens en de mogelijkheid van veilige back-ups. Al met al biedt Aegis een lokale, controleerbare oplossing voor tweevoudige authenticatie, ideaal voor iedereen die de volledige controle over zijn 2FA-codes wil behouden.



## Maak kennis met Aegis Authenticator



Aegis Authenticator is een open-source 2FA-applicatie voor Android, uitgebracht onder de GPL v3-licentie. Het onderscheidt zich door zijn "privacy by design" filosofie: de applicatie werkt volledig offline en vereist geen verbinding met een externe service. Als gevolg hiervan blijven je tokens lokaal opgeslagen op je apparaat, in een veilige kluis waarvan alleen jij de sleutel hebt.



### Belangrijkste kenmerken



**Gecodeerde kluis:** al uw OTP-codes worden opgeslagen in een AES-256 gecodeerde kluis (GCM-modus), beschermd door een door de gebruiker gedefinieerd hoofdwachtwoord. Je kunt deze kluis ontgrendelen via een wachtwoord of biometrische gegevens (vingerafdruk, gezichtsherkenning) voor extra gemak. Zonder wachtwoord zouden de gegevens onversleuteld zijn, dus we raden je ten zeerste aan er een in te stellen.



**Geavanceerde organisatie:** Aegis houdt uw vele 2FA accounts goed georganiseerd. U kunt uw items alfabetisch of in de volgorde van uw keuze sorteren, ze groeperen op categorie (bijv. Persoonlijk, Werk, Sociaal) zodat u ze gemakkelijk terugvindt, en aan elk item een persoonlijk pictogram toewijzen. Er is een zoekbalk voorzien om een dienst of account onmiddellijk op naam te vinden.



**Gecodeerde lokale back-ups:** Om ervoor te zorgen dat u nooit de toegang tot uw accounts verliest, biedt Aegis automatische back-ups van uw safe. Deze zijn versleuteld (via een wachtwoord) en kunnen worden opgeslagen op de locatie van uw keuze (interne opslag, cloudmap, enz.). De applicatie kan je accountdatabase ook handmatig exporteren, naar wens in versleuteld of onversleuteld formaat. Het importeren van accounts uit andere 2FA-toepassingen is net zo eenvoudig (Aegis ondersteunt import uit Authy, Google Authenticator, FreeOTP, andOTP, enz.)



**Veiligheid en privacy:** de applicatie is standaard volledig offline. Het heeft geen netwerkrechten nodig - wat betekent dat het geen gegevens naar de buitenwereld verstuurt en geen advertentietrackers of gedragsanalysemodules bevat. Aegis toont geen advertenties en vereist geen gebruikersaccount: zodra het is geïnstalleerd, werkt het zonder registratie. Omdat de broncode openbaar is op GitHub, kan de gemeenschap het vrij controleren, waardoor de afwezigheid van kwaadaardige of verborgen functionaliteiten wordt gegarandeerd.



**Modern Interface:** Aegis heeft een keurig Material Design, met ondersteuning voor donkere thema's (inclusief een AMOLED-modus) en zelfs een optionele tegelweergave om je codes als rasters weer te geven. Interface is overzichtelijk, zonder franje en voorkomt als veiligheidsmaatregel het vastleggen van codes op het scherm.



## Installatie



Omdat Aegis Authenticator open source is, geven de ontwikkelaars de voorkeur aan privacy-vriendelijke distributiekanalen. Er zijn twee manieren om het te installeren:



### Via F-Droid (aanbevolen)



De veiligste en gemakkelijkste manier is via F-Droid, de gratis alternatieve winkel. Als F-Droid nog niet op je telefoon is geïnstalleerd, download het dan eerst van de officiële website [F-Droid.org] (https://f-droid.org). Vervolgens :





- Open F-Droid en zorg ervoor dat je je repositories hebt bijgewerkt om de nieuwste lijst met applicaties te krijgen
- Zoek naar "Aegis Authenticator" in F-Droid. De officiële applicatie zou moeten verschijnen (uitgever: Beem Development)
- Start de installatie door op Install te drukken. Aangezien Aegis een van de door F-Droid geverifieerde applicaties is, profiteer je van een betrouwbare en veilige download



Installeren via F-Droid biedt het voordeel van het ontvangen van automatische applicatie-updates zodra deze worden uitgebracht. Bovendien garandeert F-Droid dat de applicatie vrij is van ongewenste propriëtaire componenten.



### Via GitHub (ondertekende APK)



Als je de applicatie liever installeert zonder via een winkel te gaan, kun je de officiële APK rechtstreeks downloaden van de GitHub-pagina van het project. Op de Aegis repository ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), ga naar de Releases sectie waar stabiele versies worden gepubliceerd.





- Download de nieuwste APK-versie
- Voordat je de APK installeert, moet je ervoor zorgen dat je de installatie van applicaties van onbekende bronnen op je apparaat hebt geautoriseerd (in Android-instellingen)
- De APK op GitHub is ondertekend door de ontwikkelaar met dezelfde sleutel als op F-Droid



Na handmatige installatie zal de applicatie identiek functioneren. Houd er rekening mee dat updates niet automatisch zullen zijn: je zult GitHub regelmatig moeten controleren op nieuwe versies.



### Google Play Store vs F-Droid



Aegis Authenticator is beschikbaar in zowel de Google Play Store als F-Droid, zodat je kunt kiezen uit verschillende installatiemethoden:



**Google Play Store:**




- automatische updates geïntegreerd in het Android-systeem
- ✅ Eenvoudige, vertrouwde installatie
- zelfde ondertekende APK als op andere kanalen



**F-Droid (aanbevolen) :**




- gratis en open source winkel
- ✅ Reproduceerbare en controleerbare constructie
- geen Google-service nodig
- ✅ Respect voor de filosofie van vrije software



De keuze tussen deze twee opties hangt af van je voorkeuren met betrekking tot het Google-ecosysteem. Als je van eenvoud houdt, is de Play Store ideaal. Als je een meer privacy-vriendelijke aanpak wilt, onafhankelijk van Google-diensten, dan is F-Droid de betere keuze.



## Eerste configuratie



Wanneer Aegis voor de eerste keer wordt opgestart, wordt een initiële configuratieprocedure voorgesteld om je 2FA-code veilig te stellen:



![Configuration initiale Aegis](assets/fr/01.webp)



*Initieel Aegis-configuratieproces: welkomstscherm, beveiligingskeuzes, definitie hoofdwachtwoord en voltooiing*



### Een hoofdwachtwoord instellen



Aegis zal je eerst vragen om een hoofdwachtwoord te kiezen. Dit wachtwoord wordt gebruikt om al je authenticatietokens die in de kluis zijn opgeslagen te versleutelen. We raden u sterk aan om een sterk, uniek wachtwoord in te stellen dat alleen u kent.



**⚠️ Waarschuwing:** vergeet dit wachtwoord niet - als u het verliest, worden uw versleutelde 2FA-codes ontoegankelijk (er is geen achterdeur). Aegis zal je vragen het wachtwoord twee keer in te voeren ter bevestiging.



### Biometrische ontgrendeling inschakelen (optioneel)



Als je Android-apparaat is uitgerust met een vingerafdruklezer of een andere biometrische sensor, zal Aegis je vragen om biometrische ontgrendeling te activeren. Deze optie is optioneel maar erg praktisch: hiermee kun je de applicatie snel ontgrendelen met je vingerafdruk of gezicht, in plaats van elke keer het wachtwoord in te typen.



Merk op dat biometrische gegevens een toegevoegd gemak zijn: je hoofdwachtwoord is nog steeds vereist als de biometrische gegevens worden gewijzigd of als het apparaat opnieuw wordt opgestart.



### Applicatie-instellingen ontdekken



Als je eenmaal in de toepassing bent (de hoofdpagina Interface is in eerste instantie leeg), maak jezelf dan vertrouwd met de beschikbare configuratieopties. Ga naar de instellingen via het vervolgkeuzemenu rechtsboven in het scherm (drie verticale stippen) en selecteer "Instellingen".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface hoofd Aegis leeg bij start, toegang tot parametermenu en overzicht van beschikbare opties*



Het instellingenmenu van Aegis groepeert een aantal belangrijke onderdelen:





- **Uiterlijk**: Thema (licht, donker, AMOLED), taal en andere visuele instellingen aanpassen
- **Gedrag**: Configureer het gedrag van de toepassing bij interactie met de lijst met items
- **Pictogrammensets**: beheer en importeer pictogrammensets om de look en feel van je accounts aan te passen
- **Beveiliging**: Instellingen voor versleuteling, biometrische ontgrendeling, automatische vergrendeling en andere beveiligingsparameters
- **Back-ups**: Configureer automatische back-ups naar een locatie van uw keuze
- **Importeren en exporteren**: Back-ups importeren uit andere verificatietoepassingen en uw Aegis-kluis handmatig exporteren
- **Auditlogboek**: Gedetailleerd logboek van alle belangrijke gebeurtenissen in de applicatie



Met deze overzichtelijke organisatie kunt u Aegis configureren volgens uw voorkeuren en beveiligingsbehoeften.



## Een 2FA-account toevoegen



Nu Aegis is geconfigureerd, gaan we verder met het belangrijkste: het toevoegen van uw twee-factor accounts. Het proces is eenvoudig en Aegis biedt verschillende methoden om uw verificatiecodes te integreren.



### De drie beschikbare optelmethoden



Vanuit het hoofdscherm van Aegis Interface druk je op de **+** knop rechtsonder om de opties voor het toevoegen te openen. Je hebt drie opties:





- **Scan QR-code**: Scan rechtstreeks de QR-code die wordt weergegeven door de webservice
- **Afbeelding scannen**: Scan een QR-code van een afbeelding die is opgeslagen op uw apparaat
- **Handmatig invoeren**: 2FA-accountgegevens handmatig invoeren



### Praktijkvoorbeeld: Bitwarden configureren



Laten we het concrete voorbeeld nemen van 2FA activering op Bitwarden om het proces te illustreren:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Voorbeeld van 2FA activering op Bitwarden: Interface web met verificatieopties en Aegis aanbeveling*





- **Inloggen en instellingen openen**: Log in op uw Bitwarden-account en ga naar de instellingen, tabblad "Beveiliging"
- **Providers sectie**: Ga naar de sectie "Providers" en klik op "Beheren" in de sectie "Authenticator app"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Volledig proces voor het toevoegen van een account: QR-code weergegeven door de service, geheime sleutel zichtbaar en verificatiecode ingevoerd*





- **Scan de QR-code**: Er wordt een pop-upvenster geopend met de QR-code en geheime sleutel
- In **Aegis**: Gebruik "Scan QR-code" om informatie automatisch vast te leggen
- **Verificatie**: Voer de 6-cijferige code gegenereerd door Aegis in het veld "Verificatiecode" in
- **Activering**: Klik op "Aanzetten" om activering te voltooien



### Handmatig details toevoegen



Als je de QR-code liever niet scant, gebruik dan de optie "Handmatig invoeren". Op het formulier kunt u :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Proces voor het toevoegen van een nieuw 2FA-account: Interface leeg, opties toevoegen, handmatig invulformulier en account succesvol toegevoegd*





- **Naam**: Naam van de service (bijv. Bitwarden, GitHub...)
- **Emittent**: De emittent (vaak identiek aan de naam)
- **Groep**: Optioneel, om uw accounts per categorie te ordenen
- **Opmerking**: Persoonlijke opmerkingen over deze rekening
- **Geheim**: De geheime sleutel die door de service wordt geleverd (standaard gemaskeerd)
- **Geavanceerd**: Geavanceerde parameters (algoritme, periode, aantal cijfers)



Zodra het account is toegevoegd, verschijnt het in je lijst met de huidige code en een tijdsindicator die de resterende tijd voor verlenging aangeeft.



### Universele compatibiliteit



Aegis is compatibel met alle diensten die de TOTP en HOTP standaarden gebruiken, inclusief vrijwel alle sites die 2FA aanbieden: sociale netwerken, banken, wachtwoordmanagers, cryptoplatforms, enz.



### Entree organisatie



Als je eenmaal meerdere accounts hebt toegevoegd, zul je de organisatorische tools van Aegis waarderen:





- **Aangepaste sortering:** Standaard worden accounts in alfabetische volgorde weergegeven, maar u kunt de volgorde handmatig wijzigen
- **Groepen en categorieën:** Maak groepen om je persoonlijke accounts te scheiden van je zakelijke accounts, of groepeer ze op soort dienst (bankieren, e-mail, sociale netwerken, enz.)
- **Aangepaste pictogrammen:** Aegis probeert automatisch een geschikt pictogram toe te wijzen als dat beschikbaar is, anders kun je kiezen uit veel algemene pictogrammen of een afbeelding importeren
- **Snel zoeken:** Met de zoekbalk bovenaan kun je een paar letters typen om direct overeenkomende items te filteren



Door een item aan te raken, wordt de OTP-code op ware grootte weergegeven (als deze verborgen was) en kun je deze met een lange druk op de knop naar het klembord kopiëren - handig om te plakken in de applicatie waarmee je verbinding wilt maken.



## Beveiliging en back-ups



Met beveiliging in het hart van Aegis is het belangrijk om te begrijpen hoe uw 2FA-codes worden beschermd en hoe u ervoor kunt zorgen dat ze blijven bestaan in het geval van een probleem.



### Beveiligingsarchitectuur



**Robuuste encryptie**: Al je codes worden opgeslagen in een versleutelde kluis met behulp van het **AES-256 algoritme in GCM-modus**, gecombineerd met je hoofdwachtwoord. Sleutelafleiding is gebaseerd op **scrypt**, wat verbeterde bescherming biedt tegen brute-force aanvallen.



**Veilig ontgrendelen** : Het hoofdwachtwoord is nodig om je gegevens te ontsleutelen. Biometrie (optioneel) gebruikt de **Android Secure Keystore** en TEE (Trusted Execution Environment) om de coderingssleutel te beschermen.



**Minimale rechten**: Aegis werkt standaard offline en vereist alleen toegang tot de camera (QR-scan), biometrie en vibrator. Er worden geen gegevens verzameld of gedeeld.



### Back-up opties



Aegis biedt verschillende back-upstrategieën voor verschillende beveiligings- en gebruiksbehoeften:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface compleet met toegevoegd account, back-upwaarschuwing, automatische back-upinstellingen en back-upstrategieën*



**1. Automatische lokale back-ups**




- Configureer een bestemmingsmap naar keuze
- Aanpasbare frequentie (na elke verandering, dagelijks, enz.)
- Met wachtwoord beveiligde versleutelde bestanden (.aesvault)
- Compatibel met gesynchroniseerde mappen (Nextcloud, Dropbox, enz.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Back-up map selectieproces: bestandsverkenner, doelmap en toegangsrechten*



**2. Android** cloudback-ups




- Optionele integratie met Android back-upsysteem
- Alleen beschikbaar voor gecodeerde kluizen (beveiliging behouden)
- Transparante back-up met andere Android-gegevens
- Automatisch herstellen bij apparaatwissel



**3. Handmatig** export




- Exporteer op aanvraag via **Instellingen > Importeren & Exporteren**
- Keuze uit versleuteld (aanbevolen) of leeg formaat
- Handig voor migraties of incidentele back-ups



### Goede veiligheidspraktijken





- Bewaar meerdere back-upversies om corruptie te voorkomen
- **Test** je back-ups regelmatig door te proberen ze terug te zetten
- Bewaar uw door de service geleverde herstelcodes afzonderlijk
- Je **hoofdwachtwoord** is nog steeds vereist, zelfs bij cloudback-ups
- **Beveilig je hoofdwachtwoord**: gebruik een uniek, sterk wachtwoord dat is opgeslagen in een wachtwoordmanager
- Houd je applicatie **up-to-date** met de nieuwste beveiligingspatches
- Activeer **automatisch vergrendelen** in de instellingen om de toegang tot de applicatie te beveiligen
- Schakel **screenshots** uit (standaardoptie) om te voorkomen dat je codes worden onderschept
- Gebruik biometrische gegevens spaarzaam: geef de voorkeur aan wachtwoorden voor kritieke toegangen



## Vergelijking met andere toepassingen



Hoe verhoudt Aegis zich tot andere populaire verificatietoepassingen?



### Aegis vs Google Authenticator



**Aegis :**




- open source en controleerbaar
- lokale gecodeerde back-up
- geavanceerde organisatie (groepen, pictogrammen, zoeken)
- ✅ Geen gegevensverzameling
- alleen Android



**Google Authenticator :**




- beschikbaar op Android en iOS
- ✅ Cloud synchronisatie (sinds 2023)
- gesloten broncode
- beperkte functionaliteit
- potentiële gegevensverzameling via Google



### Aegis vs Authy



**Aegis :**




- open bron
- geen account nodig
- code export mogelijk
- totale gegevenscontrole
- geen native synchronisatie met meerdere apparaten



**Authy :**




- synchronisatie met meerdere apparaten
- beschikbaar op Android en iOS
- gesloten broncode
- ❌ Telefoonnummer vereist
- kan geen codes exporteren
- ❌ Desktoptoepassingen verwijderd in maart 2024



Aegis blinkt uit voor Android-gebruikers die waarde hechten aan transparantie, lokale beveiliging en volledige controle over hun gegevens. Alternatieven zoals Authy zijn beter geschikt als je absoluut automatische synchronisatie met meerdere apparaten nodig hebt.




## Conclusie



Aegis Authenticator is een uitstekende oplossing voor wie op zoek is naar een privacy-vriendelijke, veilige en transparante 2FA-applicatie. De open-source aanpak, gecombineerd met robuuste encryptie en een nette Interface, maakt het een eersteklas keuze voor het beveiligen van je online accounts.



Hoewel Aegis beperkt is tot Android en native cloudsynchronisatie mist, maakt het deze beperkingen meer dan goed met zijn "privacy by design"-filosofie en totale gegevenscontrole. Voor gebruikers die zich zorgen maken over hun digitale privacy, biedt Aegis een geloofwaardig en krachtig alternatief voor de dominante propriëtaire oplossingen op de markt.



De beveiliging van uw online accounts hoeft niet afhankelijk te zijn van de goodwill van commerciële bedrijven. Met Aegis behoudt u de controle over uw verificatiecodes, in een digitale kluis waarvan alleen u de sleutel heeft.



## Bronnen



### Officiële websites




- **Officiële website**: [getaegis.app](https://getaegis.app/) - Aanvraagpresentatie en download
- **Broncode**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Officiële GitHub repository
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Installatie via de gratis winkel



### Technische documentatie




- **Vault documentatie**: [Vault design](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Technische beschrijving van encryptie en veilige architectuur
- **Officiële FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Antwoorden op veelgestelde vragen
- **Project wiki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Volledige gebruikersdocumentatie