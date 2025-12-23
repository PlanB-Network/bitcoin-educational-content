---
name: Bitwarden
description: Hoe stel je een wachtwoordmanager in?
---
![cover](assets/cover.webp)


In het digitale tijdperk moeten we een groot aantal online accounts beheren voor verschillende aspecten van ons dagelijks leven, zoals bankieren, financiële platforms, e-mails, bestandsopslag, gezondheid, administratie, sociale netwerken, videogames, enz.


Om onszelf te authenticeren op elk van deze accounts, gebruiken we een identificatiecode, vaak een e-mail Address, vergezeld van een wachtwoord. Geconfronteerd met de onmogelijkheid om een groot aantal unieke wachtwoorden te onthouden, zou je in de verleiding kunnen komen om hetzelfde wachtwoord te hergebruiken of een gemeenschappelijke basis lichtjes aan te passen om het gemakkelijk te kunnen onthouden. Deze praktijken brengen de veiligheid van je accounts echter ernstig in gevaar.


Het eerste principe voor wachtwoorden is om ze niet te hergebruiken. Elke online account moet worden beschermd door een uniek wachtwoord dat volledig verschillend is van de andere. Dit is belangrijk omdat, als een aanvaller erin slaagt om een van je wachtwoorden te kraken, je niet wilt dat ze toegang hebben tot al je accounts. Een uniek wachtwoord voor elk account isoleert potentiële aanvallen en beperkt hun bereik. Als je bijvoorbeeld hetzelfde wachtwoord gebruikt voor een videogame-platform en voor je e-mail en dat wachtwoord wordt gecompromitteerd via een phishingsite die gerelateerd is aan het gameplatform, dan kan de aanvaller gemakkelijk toegang krijgen tot je e-mail en de controle over al je andere online accounts overnemen.


Het tweede essentiële principe is de sterkte van het wachtwoord. Een wachtwoord wordt als sterk beschouwd als het moeilijk te brute forceren is, dat wil zeggen, te raden door vallen en opstaan. Dit betekent dat je wachtwoorden zo willekeurig mogelijk moeten zijn, lang moeten zijn en een verscheidenheid aan tekens moeten bevatten (kleine letters, hoofdletters, cijfers en symbolen).


Het toepassen van deze twee beveiligingsprincipes voor wachtwoorden (uniekheid en robuustheid) kan moeilijk zijn in het dagelijks leven, omdat het bijna onmogelijk is om een uniek, willekeurig en sterk wachtwoord te onthouden voor al onze accounts. Dit is waar de wachtwoordmanager om de hoek komt kijken.


Een wachtwoordmanager genereert sterke wachtwoorden en slaat deze veilig op, zodat je toegang hebt tot al je online accounts zonder dat je ze afzonderlijk hoeft te onthouden. Je hoeft maar één wachtwoord te onthouden, het hoofdwachtwoord, waarmee je toegang hebt tot al je opgeslagen wachtwoorden in de manager. Het gebruik van een wachtwoordmanager verhoogt je online veiligheid omdat het hergebruik van wachtwoorden voorkomt en systematisch willekeurige wachtwoorden genereert. Maar het vereenvoudigt ook je dagelijkse gebruik van je accounts door de toegang tot je gevoelige informatie te centraliseren.

In deze tutorial onderzoeken we hoe je een wachtwoordmanager kunt instellen en gebruiken om je online beveiliging te verbeteren. Ik laat je kennismaken met Bitwarden en in een andere tutorial bekijken we een andere oplossing, KeePass.

https://planb.academy/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Waarschuwing: Een wachtwoordmanager is geweldig voor het opslaan van wachtwoorden, maar **je moet er nooit de Mnemonic zin van je Bitcoin Wallet in opslaan!** Onthoud dat een Mnemonic zin uitsluitend in een fysieke vorm moet worden opgeslagen, zoals een stuk papier of metaal.


## Inleiding tot Bitwarden


Bitwarden is een wachtwoordmanager die geschikt is voor zowel beginners als gevorderden. Het biedt talloze voordelen. Allereerst is Bitwarden een multiplatformoplossing, wat betekent dat je het kunt gebruiken als mobiele app, webapplicatie, browserextensie en desktopsoftware.

![BITWARDEN](assets/notext/01.webp)

Met Bitwarden kun je je wachtwoorden online opslaan en synchroniseren op al je apparaten, terwijl je end-to-end versleuteling met je hoofdwachtwoord garandeert. Hierdoor heb je bijvoorbeeld toegang tot je wachtwoorden op zowel je computer als je smartphone, met synchronisatie tussen de twee. Omdat uw wachtwoorden versleuteld zijn, blijven ze ontoegankelijk voor iedereen, inclusief Bitwarden, zonder de decoderingssleutel die uw hoofdwachtwoord is.


Bovendien is Bitwarden open-source, wat betekent dat de software kan worden gecontroleerd door onafhankelijke experts. Wat betreft de prijs biedt Bitwarden drie plannen:


- Een gratis versie die we in deze tutorial zullen verkennen. Hoewel het gratis is, biedt het een beveiligingsniveau dat gelijkwaardig is aan dat van de betaalde versies. Je kunt een onbeperkt aantal wachtwoorden opslaan en zoveel apparaten synchroniseren als je wilt;
- Een premium versie voor $10 per jaar met extra functies zoals bestandsopslag, back-up van bankpasjes, de mogelijkheid om 2FA in te stellen met een fysieke beveiligingssleutel en toegang tot TOTP 2FA-verificatie rechtstreeks met Bitwarden;
- En een gezinsplan voor $40 per jaar dat de voordelen van de premium versie uitbreidt naar zes verschillende gebruikers.

![BITWARDEN](assets/notext/02.webp)

Naar mijn mening zijn deze prijzen redelijk. De gratis versie is een uitstekende optie voor beginners, en de premium versie biedt een zeer goede prijs-kwaliteitverhouding in vergelijking met andere wachtwoordmanagers op de markt, terwijl het meer functies biedt. Daarnaast is het feit dat Bitwarden open-source is een groot voordeel. Daarom is het een interessant compromis, vooral voor beginners.

Een andere functie van Bitwarden is de mogelijkheid om uw wachtwoordmanager zelf te hosten als u bijvoorbeeld thuis een NAS hebt. Door deze configuratie in te stellen, worden uw wachtwoorden niet opgeslagen op de servers van Bitwarden, maar op uw eigen servers. Dit geeft u volledige controle over de beschikbaarheid van uw wachtwoorden. Deze optie vereist echter een rigoureus back-upbeheer om verlies van toegang te voorkomen. Daarom is self-hosting van Bitwarden meer geschikt voor gevorderde gebruikers en zullen we dit in een andere tutorial bespreken.

## Hoe maak ik een Bitwarden-account aan?


Bezoek [de Bitwarden-website](https://bitwarden.com/) en klik op "*Get Started*".

![BITWARDEN](assets/notext/03.webp)

Begin met het invoeren van je e-mail Address en je naam of bijnaam.

![BITWARDEN](assets/notext/04.webp)

Vervolgens moet je je hoofdwachtwoord instellen. Zoals we in de inleiding zagen, is dit wachtwoord erg belangrijk omdat het je toegang geeft tot al je andere opgeslagen wachtwoorden in de manager. Het brengt twee risico's met zich mee: verlies en compromittering. Als je de toegang tot dit wachtwoord verliest, heb je geen toegang meer tot al je referenties. Als je wachtwoord wordt gestolen, heeft de aanvaller toegang tot al je accounts.


Om het risico op verlies te minimaliseren, raad ik aan om een fysieke back-up van je hoofdwachtwoord op papier te maken en deze op een veilige plaats te bewaren. Indien mogelijk, Seal deze back-up in een veilige envelop om er regelmatig zeker van te zijn dat niemand anders er toegang tot heeft.


Om compromittering van je hoofdwachtwoord te voorkomen, moet het extreem robuust zijn. Het moet zo lang mogelijk zijn, veel verschillende tekens gebruiken en willekeurig gekozen worden. In 2024 zijn de minimumaanbevelingen voor een veilig wachtwoord 13 tekens, inclusief cijfers, kleine letters en hoofdletters, en symbolen, op voorwaarde dat het wachtwoord echt willekeurig is. Ik raad echter aan om te kiezen voor een wachtwoord van ten minste 20 tekens, inclusief alle mogelijke soorten tekens, om de veiligheid langer te waarborgen.


Voer je hoofdwachtwoord in het daarvoor bestemde vak in en bevestig het in het volgende vak.

![BITWARDEN](assets/notext/05.webp)

Als je wilt, kun je een hint toevoegen aan je hoofdwachtwoord. Ik raad het echter af om dit te doen, omdat de hint geen betrouwbare herstelmethode biedt voor het geval je je wachtwoord verliest en zelfs nuttig kan zijn voor aanvallers die proberen je wachtwoord te raden of te brute-forcen. Als algemene regel geldt: maak geen openbare hints die de veiligheid van uw hoofdwachtwoord in gevaar kunnen brengen.

![BITWARDEN](assets/notext/06.webp)

Klik vervolgens op de knop "*Een account aanmaken*".

![BITWARDEN](assets/notext/07.webp)

U kunt nu inloggen op uw nieuwe Bitwarden-account. Voer uw e-mailadres Address in.

![BITWARDEN](assets/notext/08.webp)

Typ vervolgens je hoofdwachtwoord.

![BITWARDEN](assets/notext/09.webp)

Je bent nu op het web Interface van je wachtwoordmanager.

![BITWARDEN](assets/notext/10.webp)

## Hoe stel ik Bitwarden in?


Om te beginnen zullen we onze e-mail Address bevestigen. Klik op "*Verstuur e-mail*".

![BITWARDEN](assets/notext/11.webp)

Klik vervolgens op de knop die u per e-mail hebt ontvangen.

![BITWARDEN](assets/notext/12.webp)

Log ten slotte opnieuw in.

![BITWARDEN](assets/notext/13.webp)

Eerst en vooral raad ik je sterk aan om twee-factor authenticatie (2FA) in te stellen om je wachtwoordmanager te beveiligen. U hebt de keuze tussen het gebruik van een TOTP-applicatie of een fysieke beveiligingssleutel. Als u 2FA activeert, wordt u elke keer dat u inlogt op uw Bitwarden-account niet alleen gevraagd om uw hoofdwachtwoord, maar ook om een bewijs van uw tweede authenticatiefactor. Dit is een extra Layer van beveiliging, vooral handig in het geval dat uw papieren back-up van het hoofdwachtwoord gecompromitteerd is.


Als je niet zeker weet hoe je deze 2FA apparaten moet instellen en gebruiken, raad ik je aan om deze 2 andere tutorials te volgen:


https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.academy/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Ga hiervoor naar het tabblad "*Security*" in het menu "*Settings*".

![BITWARDEN](assets/notext/14.webp)

Klik vervolgens op het tabblad "Aanmelden in twee stappen".

![BITWARDEN](assets/notext/15.webp)

Hier kan je de 2FA methode kiezen die je verkiest. Ik kies bijvoorbeeld voor 2FA met een TOTP-toepassing door op de knop "*Beheer*" te klikken.

![BITWARDEN](assets/notext/16.webp)

Bevestig je hoofdwachtwoord.

![BITWARDEN](assets/notext/17.webp)

Scan dan de QR-code met je 2FA-toepassing.

![BITWARDEN](assets/notext/18.webp)

Voer de 6-cijferige code in die vermeld staat op uw 2FA-toepassing en klik vervolgens op de knop "*Aanzetten*". bITWARDEN](assets/notext/19.webp)

Authenticatie met twee factoren is met succes ingesteld op je account.

![BITWARDEN](assets/notext/20.webp)

Als je nu weer probeert in te loggen bij je manager, moet je eerst je hoofdwachtwoord invoeren en daarna de dynamische 6-cijferige code die door je 2FA-applicatie wordt gegenereerd. Zorg ervoor dat je altijd toegang hebt tot deze dynamische code; zonder deze code kun je je wachtwoorden niet herstellen.

![BITWARDEN](assets/notext/21.webp)

In de instellingen heb je ook de mogelijkheid om je manager aan te passen in het tabblad "*Voorkeuren*". Hier kun je de duur voordat je manager automatisch vergrendelt aanpassen, evenals de taal en het thema van de Interface.

![BITWARDEN](assets/notext/22.webp)

Ik raad sterk aan om de lengte van de wachtwoorden die Bitwarden genereert aan te passen. Standaard is de lengte ingesteld op 14 tekens, wat onvoldoende kan zijn voor optimale veiligheid. Nu je een manager hebt om al je wachtwoorden te onthouden, kun je er net zo goed gebruik van maken om hele sterke wachtwoorden te gebruiken.


Ga hiervoor naar het menu "*Generator*".

![BITWARDEN](assets/notext/23.webp)

Hier kunt u de lengte van uw wachtwoorden verhogen tot 40 en het vakje aanvinken om symbolen toe te voegen.

![BITWARDEN](assets/notext/24.webp)

## Hoe beveilig je je accounts met Bitwarden?


Nu je wachtwoordmanager is geconfigureerd, kun je beginnen met het opslaan van de gegevens voor je online accounts. Om een nieuw item toe te voegen, klik je direct op de knop "*Nieuw item*" of op de knop "*Nieuw*" rechtsboven in het scherm en vervolgens op "*item*".

![BITWARDEN](assets/notext/25.webp)

In het formulier dat wordt geopend, begint u met het bepalen van de aard van het item dat moet worden opgeslagen. Om aanmeldingsgegevens op te slaan, kies je de optie "*Login*" uit het vervolgkeuzemenu.

![BITWARDEN](assets/notext/26.webp)

Voer in het veld "*Naam*" een beschrijvende naam in voor je referenties. Dit maakt het makkelijker om je wachtwoorden op te zoeken en te organiseren, vooral als je er veel hebt. Als je bijvoorbeeld je referenties voor de Plan ₿ Academy site wilt opslaan, kun je dit item een naam geven die het direct herkenbaar maakt bij toekomstige zoekopdrachten.

![BITWARDEN](assets/notext/27.webp)

Met de optie "*Map*" kun je je referenties indelen in mappen. Op dit moment hebben we er nog geen aangemaakt, maar ik zal je later laten zien hoe je dat doet.

![BITWARDEN](assets/notext/28.webp)

Voer in het veld "*Gebruikersnaam*" je gebruikersnaam in, meestal je e-mail Address. bITWARDEN](assets/notext/29.webp)

Vervolgens kun je in het veld "*Wachtwoord*" je wachtwoord invoeren. Ik raad echter sterk aan om Bitwarden generate een lang, willekeurig en uniek wachtwoord voor je te laten maken. Zo weet je zeker dat je een sterk wachtwoord hebt. Om deze functie te gebruiken, klikt u op het pictogram met de dubbele pijl boven het in te vullen veld.

![BITWARDEN](assets/notext/30.webp)

Je kunt zien dat je wachtwoord is gegenereerd.

![BITWARDEN](assets/notext/31.webp)

In het veld "*URI 1*" kun je de domeinnaam van de website invoeren.

![BITWARDEN](assets/notext/32.webp)

En tot slot kun je in het veld "*Noten*" indien nodig extra details toevoegen.

![BITWARDEN](assets/notext/33.webp)

Als je klaar bent met het invullen van al deze velden, klik je op de knop "*Opslaan*".

![BITWARDEN](assets/notext/34.webp)

Uw identificatiecode verschijnt nu in uw Bitwarden-manager.

![BITWARDEN](assets/notext/35.webp)

Door erop te klikken, krijg je toegang tot de details en kun je ze wijzigen.

![BITWARDEN](assets/notext/36.webp)

Door op de drie kleine puntjes aan de rechterkant te klikken, heb je snel toegang om het wachtwoord of de identificatie te kopiëren.

![BITWARDEN](assets/notext/37.webp)

Gefeliciteerd, je hebt met succes je eerste wachtwoord opgeslagen in je manager! Als je je identificaties beter wilt organiseren, kun je specifieke mappen maken. Klik hiervoor op de knop "*New*" rechtsboven in het scherm en selecteer vervolgens "*Folder*".

![BITWARDEN](assets/notext/38.webp)

Voer een naam in voor je map.

![BITWARDEN](assets/notext/39.webp)

Klik vervolgens op "*Opslaan*".

![BITWARDEN](assets/notext/40.webp)

Je map verschijnt nu in je manager.

![BITWARDEN](assets/notext/41.webp)

Je kunt een map aan een identifier toewijzen wanneer je deze aanmaakt, zoals we eerder hebben gedaan, of door een bestaande identifier te wijzigen. Door bijvoorbeeld op mijn identifier voor Plan ₿ Academy te klikken, kan ik ervoor kiezen om deze in de map "*Bitcoin*" te classificeren.

![BITWARDEN](assets/notext/42.webp)

Op deze manier kun je je wachtwoordmanager zo structureren dat het makkelijker is om je identificaties terug te vinden. Je kunt ze organiseren met mappen zoals persoonlijk, professioneel, banken, e-mails, sociale netwerken, abonnementen, winkelen, administratie, streaming, opslag, reizen, gezondheid, enz.

Als u liever alleen de webversie van Bitwarden gebruikt, is het heel goed mogelijk om het daarbij te houden. Ik raad je dan aan om je wachtwoordmanager toe te voegen aan de favorieten van je browser voor gemakkelijke toegang en om phishing-risico's te vermijden. Bitwarden biedt echter ook een volledig scala aan clients waarmee je je manager op verschillende apparaten kunt gebruiken en het dagelijks gebruik ervan kunt vereenvoudigen. Ze bieden met name een mobiele app, een browserextensie en desktopsoftware. Laten we eens kijken hoe je ze samen kunt instellen.


![BITWARDEN](assets/notext/43.webp)


## Hoe gebruikt u de Bitwarden browserextensie?


Als je wilt, kun je eerst de browserextensie instellen. Deze extensie werkt als een verkleinde versie van je manager en biedt je de mogelijkheid om nieuwe wachtwoorden automatisch op te slaan, generate suggesties voor veilige wachtwoorden te geven en automatisch je gegevens in te vullen op inlogpagina's van websites.


Het dagelijks gebruik van deze extensie is erg handig, maar het kan ook nieuwe aanvalsvectoren openen. Sommige cyberbeveiligingsexperts raden daarom af om browserextensies voor wachtwoordbeheerders te gebruiken. Als je er echter voor kiest om de Bitwarden-extensie te gebruiken, lees je hier hoe je te werk moet gaan:


Ga eerst naar [de officiële Bitwarden downloadpagina](https://bitwarden.com/download/#downloads-web-browser).


![BITWARDEN](assets/notext/44.webp)


Kies uw browser uit de lijst. In dit voorbeeld gebruik ik Firefox, dus ik ben doorgestuurd naar de officiële Bitwarden-extensie in de Add-ons Store van Firefox. De procedure is vergelijkbaar voor andere browsers.


![BITWARDEN](assets/notext/45.webp)


Klik op de knop "*Toevoegen aan Firefox*".


![BITWARDEN](assets/notext/46.webp)


U kunt Bitwarden dan aan uw extensiebalk vastmaken zodat u er gemakkelijk bij kunt. Klik op de extensie om in te loggen.


![BITWARDEN](assets/notext/47.webp)


Voer uw e-mail Address in.


![BITWARDEN](assets/notext/48.webp)


Dan je hoofdwachtwoord.


![BITWARDEN](assets/notext/49.webp)


En voer tot slot de 6-cijferige code van je verificatie-app in.


![BITWARDEN](assets/notext/50.webp)


U bent nu verbonden met uw Bitwarden manager via de browserextensie.


![BITWARDEN](assets/notext/51.webp)


Als ik bijvoorbeeld terug ga naar de Plan ₿ Academy site en probeer in te loggen op mijn account, kun je zien dat de Bitwarden extensie geïntegreerd in de browser de inlogvelden herkent en me automatisch aanbiedt om de identificatiecode te selecteren die ik eerder heb opgeslagen.


![BITWARDEN](assets/notext/52.webp)

Als ik deze identificatiecode selecteer, vult Bitwarden de inlogvelden voor me in. Deze functie van de extensie maakt het mogelijk om snel verbinding te maken met websites, zonder de noodzaak om inloggegevens te kopiëren en te plakken vanuit de Bitwarden webapplicatie of software.

![BITWARDEN](assets/notext/53.webp)

De extensie is ook ontworpen om het aanmaken van nieuwe accounts te detecteren. Als er bijvoorbeeld een nieuw account wordt aangemaakt op Plan ₿ Academy, stelt Bitwarden automatisch voor om de nieuwe identificatiecode op te slaan.

![BITWARDEN](assets/notext/54.webp)

Door op de suggestie te klikken die verschijnt, wordt de extensie geopend. Hiermee kan ik de details van de nieuwe identifier invoeren en generate een sterk, uniek wachtwoord geven.

![BITWARDEN](assets/notext/55.webp)

Nadat je de informatie hebt ingevuld en op "*Opslaan*" hebt geklikt, slaat de extensie de gegevens op.

![BITWARDEN](assets/notext/56.webp)

Vervolgens vult de extensie automatisch onze gegevens in de juiste velden op de website in.

![BITWARDEN](assets/notext/57.webp)

## Hoe gebruik je Bitwarden software?


Om de Bitwarden desktop software te installeren, gaat u eerst naar [de downloadpagina](https://bitwarden.com/download/#downloads-desktop). Selecteer en download de versie die overeenkomt met uw besturingssysteem.

![BITWARDEN](assets/notext/58.webp)

Zodra de download is voltooid, gaat u verder met de installatie van de software op uw computer. Bij de eerste start van de Bitwarden software moet u uw gegevens invoeren om uw wachtwoordmanager te ontgrendelen.

![BITWARDEN](assets/notext/59.webp)

Vervolgens kom je op de homepage van je manager. De Interface is bijna hetzelfde als op de webapplicatie.

![BITWARDEN](assets/notext/60.webp)

## Hoe gebruik je de Bitwarden-applicatie?


Om toegang te krijgen tot uw wachtwoorden vanaf uw telefoon, kunt u de mobiele applicatie Bitwarden installeren. Ga eerst naar [de downloadpagina](https://bitwarden.com/download/#downloads-mobile) en scan met uw smartphone de QR-code die bij uw besturingssysteem hoort.

![BITWARDEN](assets/notext/61.webp)

Download en installeer de officiële mobiele applicatie van Bitwarden. Voer bij de eerste opening van de applicatie uw gegevens in om toegang te krijgen tot uw wachtwoordmanager.

![BITWARDEN](assets/notext/62.webp)

Eenmaal verbonden kun je al je wachtwoorden direct vanuit de applicatie raadplegen en beheren.

![BITWARDEN](assets/notext/63.webp)

Om de beveiliging van je applicatie te verbeteren, raad ik je aan om naar de instellingen te gaan en PIN-bescherming te activeren. Dit voegt een extra Layer beveiliging toe in geval van verlies of diefstal van je telefoon.

![BITWARDEN](assets/notext/64.webp)

## Hoe maak ik een back-up van Bitwarden?

Om er zeker van te zijn dat u nooit toegang verliest tot uw wachtwoorden, zelfs niet in het geval van verlies van uw hoofdwachtwoord of een ramp op de Bitwarden-servers, adviseer ik u om regelmatig een versleutelde back-up van uw beheerder te maken op een extern medium.


Het idee is om al uw Bitwarden-gegevens te versleutelen met een wachtwoord dat verschilt van uw hoofdwachtwoord en deze versleutelde back-up op te slaan op een USB-stick of een Hard-schijf die u bijvoorbeeld thuis bewaart. U kunt dan een fysieke kopie van het ontcijferingswachtwoord bewaren op een andere locatie dan waar het back-upmedium is opgeslagen. Je kunt bijvoorbeeld de USB-stick thuis bewaren en de fysieke kopie van het versleutelingswachtwoord toevertrouwen aan een vertrouwde vriend.


Deze methode zorgt ervoor dat zelfs als je back-upmedium wordt gestolen, je gegevens ontoegankelijk blijven zonder het decoderingswachtwoord. Op dezelfde manier kan je vriend geen toegang krijgen tot je gegevens zonder het fysieke medium.


Als er echter een probleem optreedt, kunt u het wachtwoord en het externe medium gebruiken om weer toegang te krijgen tot uw gegevens, onafhankelijk van Bitwarden. Dus zelfs als de Bitwarden-servers worden vernietigd, hebt u nog steeds de mogelijkheid om uw wachtwoorden op te halen.


Daarom adviseer ik je om deze back-ups regelmatig uit te voeren, zodat ze altijd je meest recente gegevens bevatten. Om je vriend, die een kopie van het coderingswachtwoord heeft, niet lastig te vallen met elke nieuwe back-up, kun je dit wachtwoord opslaan in je wachtwoordbeheerder. Dit is niet bedoeld als back-up, aangezien je vriend al een fysieke kopie heeft, maar eerder om je toekomstige exportprocedures te vereenvoudigen.


Het exporteren is heel eenvoudig: ga naar de sectie "*Tools*" van uw Bitwarden manager en selecteer "*Kluis exporteren*".

![BITWARDEN](assets/notext/65.webp)

Kies voor het formaat "*.json (Encrypted)*".

![BITWARDEN](assets/notext/66.webp)

Selecteer vervolgens de optie "*Wachtwoord beveiligd*".

![BITWARDEN](assets/notext/67.webp)

Hier is het belangrijk om een sterk, uniek en willekeurig gegenereerd wachtwoord te kiezen om de back-up te versleutelen. Dit zorgt ervoor dat, zelfs in het geval van diefstal van je versleutelde back-up, het onmogelijk is voor een aanvaller om deze te ontsleutelen door middel van brute kracht.

![BITWARDEN](assets/notext/68.webp)

Klik op "*Bevestig formaat*" en voer je masterwachtwoord in om verder te gaan met exporteren.

![BITWARDEN](assets/notext/69.webp)

Zodra het exporteren is voltooid, vindt u uw versleutelde back-upbestand in uw downloads. Breng het over naar een veilig extern opslagapparaat, zoals een USB-stick of een Hard-station. Herhaal deze handeling regelmatig, afhankelijk van uw gebruik. U kunt de back-up bijvoorbeeld elke week of elke maand vernieuwen, afhankelijk van uw behoeften.