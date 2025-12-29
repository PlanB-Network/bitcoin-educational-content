---
name: PearPass
description: Krijg weer controle over uw wachtwoorden met een lokale, peer-to-peer, cloud-vrije wachtwoordmanager
---

![cover](assets/cover.webp)



In een tijd waarin elk individu tientallen, zelfs honderden online accounts beheert, is de beveiliging van logins een centraal onderwerp geworden in IT-beveiliging. Sociale netwerken, berichtensystemen, professionele diensten, financiële platforms: elk van deze toegangen berust op een geheim waarvan het compromitteren ernstige gevolgen voor uw leven kan hebben.



En toch, ondanks het groeiende aantal aanvallen, blijven slechte praktijken wijdverspreid onder de bevolking: zwakke wachtwoorden, hergebruikte wachtwoorden, wachtwoorden opgeslagen in duidelijke tekst of ongeveer gememoriseerde wachtwoorden. Om deze problemen op te lossen zonder het dagelijks leven ingewikkelder te maken, is de oplossing het gebruik van een wachtwoordmanager.



Er bestaan al tientallen wachtwoordmanagers en Plan ₿ Academy biedt voor de meeste daarvan een tutorial. Maar in deze tutorial wil ik er één introduceren die zich duidelijk onderscheidt van de rest wat betreft hoe het werkt: **PearPass**.



**PearPass is een open-source, local-first, peer-to-peer wachtwoordmanager ontworpen om gebruikers totale controle over hun gegevens te geven



![Image](assets/fr/01.webp)



## Waarom kiezen voor PearPass?



Een wachtwoordmanager is een softwareprogramma dat al je wachtwoorden op een veilige manier genereert, opslaat en organiseert. In plaats van wachtwoorden te onthouden of te hergebruiken, hoef je maar één geheim te beschermen: het hoofdwachtwoord, dat je hele kluis versleutelt. Deze aanpak maakt het mogelijk om unieke, lange, willekeurige wachtwoorden te gebruiken voor elke service, waardoor het risico op vergeten en compromitteren wordt verkleind en de impact van een mogelijk lek wordt beperkt. Vandaag de dag is het een basis IT-hulpmiddel dat iedereen zou moeten gebruiken.



Er zijn twee hoofdcategorieën wachtwoordbeheerders. Aan de ene kant is er alleen lokale software, die erg veilig is omdat de gegevens nooit op een centrale server worden opgeslagen, maar niet erg praktisch omdat je je gegevens niet gemakkelijk kunt synchroniseren tussen verschillende apparaten (computer, smartphone, tablet...). Cloud-gebaseerde wachtwoordmanagers daarentegen slaan je gegevens op hun servers op en synchroniseren ze met al je apparaten. Hun belangrijkste voordeel is gemak, maar ze brengen een compromis met zich mee op het gebied van veiligheid, omdat je wachtwoorden worden opgeslagen op infrastructuren waar je geen controle over hebt.



PearPass breekt bewust met beide modellen. Het positioneert zichzelf tussen lokale managers en cloudoplossingen: het maakt synchronisatie van je wachtwoorden mogelijk, terwijl het garandeert dat ze nooit op externe servers worden opgeslagen. Als gevolg hiervan worden al uw referenties lokaal opgeslagen op uw apparaten en is de synchronisatie tussen meerdere machines uitsluitend peer-to-peer. Deze architectuur elimineert de single points of failure die geassocieerd worden met gecentraliseerde databases: er zijn geen servers om te compromitteren en geen infrastructuur van derden om toegang te krijgen tot je referenties. De communicatie tussen je apparaten is end-to-end versleuteld, zodat alleen de sleutels die jij in je bezit hebt toegang geven tot de gegevens.



![Image](assets/fr/02.webp)



Om dit mogelijk te maken, vertrouwt PearPass, zoals de naam al aangeeft, op **Pears**, een peer-to-peer technologie-ecosysteem dat is toegewijd aan het creëren en uitvoeren van serverloze toepassingen. Pears biedt de uitvoeringsomgeving, distributiemechanismen en netwerklagen die nodig zijn om volledig gedecentraliseerde toepassingen uit te voeren, die in staat zijn om direct te synchroniseren tussen peers, zonder enige centrale infrastructuur. In het geval van PearPass biedt Pears apparaatontdekking, versleutelde verbindingsopbouw en wachtwoordkluis-synchronisatie tussen uw machines. Deze aanpak zorgt ervoor dat PearPass functioneel, veerkrachtig en onafhankelijk van enige externe autoriteit blijft.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Naast deze innovatieve architectuur is PearPass volledig open-source en zijn alle functies gratis. De software is ook onafhankelijk gecontroleerd door Secfault Security. Naast de specifieke architectuur, biedt PearPass natuurlijk alle klassieke functies die verwacht worden van een goede wachtwoordmanager, die we in de loop van deze tutorial zullen ontdekken.



Kortom, waar traditionele wachtwoordmanagers u vragen om een bedrijf en zijn servers te vertrouwen, gebruikt PearPass een logica van soevereiniteit: geen cloud, geen gecentraliseerde accounts, geen tussenpersonen. U behoudt de exclusieve controle over uw referenties, terwijl u profiteert van synchronisatie tussen uw apparaten.



## Hoe installeer ik PearPass?



PearPass is beschikbaar op alle platforms: Windows, Linux, macOS, Android, iOS en browserextensies. Je hoeft Pears niet op je machine te installeren: PearPass werkt op zichzelf.



### Installatie op Windows



Op Windows wordt PearPass geleverd als een klassiek installatieprogramma. Ga naar [de officiële downloadpagina] (https://pass.pears.com/download) en klik vervolgens op de knop `Download Windows-installer`.



Zodra het bestand is gedownload, opent u het installatieprogramma en volgt u de stappen die door de wizard worden aangegeven. De toepassing is vervolgens toegankelijk via het `Startmenu` of via een snelkoppeling op het bureaublad.



![Image](assets/fr/03.webp)



### Installatie op macOS



Op macOS wordt PearPass gedistribueerd als een schijfimage (`.dmg`). Ga naar [de officiële downloadpagina](https://pass.pears.com/download) en kies de versie die overeenkomt met de architectuur van je Mac (Intel of Apple Silicon). Open na het downloaden het `.dmg` bestand en start het programma vanuit de map `Applications`.



Bij de eerste keer opstarten toont macOS een beveiligingsbericht dat aangeeft dat het programma van het internet komt: bevestig gewoon om door te gaan.



### Installatie op Linux



Op Linux is PearPass beschikbaar in `.AppImage` formaat, wat brede compatibiliteit garandeert met de meeste distributies zonder specifieke afhankelijkheden. Download het `.AppImage` bestand van [de officiële downloadpagina](https://pass.pears.com/download) en start het direct door te dubbelklikken.



Afhankelijk van uw omgeving moet u het bestand mogelijk uitvoerbaar maken via bestandseigenschappen (rechtsklik) of met het commando `chmod +x`. Eenmaal geautoriseerd start PearPass op als een stand-alone applicatie.



### Installatie browserextensie



PearPass biedt een browserextensie voor automatisch inloggen en snelle toegang tot je kluis terwijl je op het web surft. De extensie is momenteel beschikbaar voor Google Chrome en compatibele browsers. Ga om het te installeren naar [de officiële downloadpagina](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Eenmaal toegevoegd, kunt u het vastmaken aan de werkbalk voor snelle toegang. Het activeren van de extensie vereist vervolgens een koppeling met de PearPass applicatie die lokaal op uw computer is geïnstalleerd (we komen hier later in de tutorial op terug).



### Installatie op iOS en Android



Op iPhone en Android download je de applicatie gewoon in je app store:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Naast deze klassieke installatiemethoden is het ook mogelijk om de software rechtstreeks van GitHub repositories te downloaden, voor elke :




- [Desktop](https://github.com/tetherto/pearpass-app-desktop);
- [Mobiel](https://github.com/tetherto/pearpass-app-mobile);
- [Browserextensie] (https://github.com/tetherto/pearpass-app-browser-extension).



Zodra PearPass is geïnstalleerd op een of meer platforms, kunt u verder gaan met de eerste configuratie. In deze tutorial zullen we beginnen met het configureren van de software op de desktop en vervolgens synchroniseren met de browserextensie en de mobiele applicatie.



## Hoe maak ik een PearPass kluis aan?



Wanneer u PearPass voor het eerst start op uw computer, leidt de applicatie u door twee stappen: het instellen van uw hoofdwachtwoord en vervolgens het maken van uw eerste safe.



### Hoofdwachtwoord instellen



Wanneer de toepassing voor het eerst wordt opgestart op het bureaublad, klik dan op de knop `Skip` en vervolgens op `Continue` om door het introductiescherm te gaan en bij de configuratie van het hoofdwachtwoord te komen.



![Image](assets/fr/06.webp)



Vervolgens komt de belangrijke stap van het kiezen van je hoofdwachtwoord. Zoals we in de inleiding zagen, is dit wachtwoord erg belangrijk, omdat het je toegang geeft tot al je andere wachtwoorden die zijn opgeslagen op de manager. Technisch gezien wordt het gebruikt om de cryptografische sleutels af te leiden die worden gebruikt om je gegevens te versleutelen.



Het hoofdwachtwoord brengt twee risico's met zich mee: verlies en compromittering. Als u de toegang tot dit wachtwoord verliest, heeft u geen toegang meer tot uw inloggegevens. PearPass bewaart uw hoofdwachtwoord nooit: **Als het verloren gaat, zijn uw inloggegevens permanent verloren**. Er is geen herstelmechanisme. Omgekeerd, als dit wachtwoord gecompromitteerd is en een aanvaller toegang krijgt tot een van uw apparaten, zal hij of zij toegang hebben tot al uw accounts.



Om het risico op verlies te beperken, kun je een fysieke back-up van je hoofdwachtwoord maken, bijvoorbeeld op papier, en deze op een veilige plek bewaren. Idealiter verzegel je deze back-up in een envelop zodat je regelmatig kunt controleren of er geen toegang tot is geweest. Maak daarentegen nooit een digitale back-up van dit wachtwoord.



Om het risico op compromittering te verkleinen, moet je hoofdwachtwoord sterk zijn. Het moet zo lang mogelijk zijn, een breed scala aan tekens bevatten en echt willekeurig gekozen worden. In 2025 zijn de minimumaanbevelingen ten minste 13 tekens inclusief hoofdletters en kleine letters, cijfers en symbolen, op voorwaarde dat het wachtwoord willekeurig is. Ik zou echter een wachtwoord aanraden van ten minste 20 tekens, zo niet meer, met alle soorten tekens om een duurzamer beveiligingsniveau te garanderen.



Voer je hoofdwachtwoord in het daarvoor bestemde veld in, bevestig het een tweede keer en klik dan op de knop `Doorgaan`.



![Image](assets/fr/07.webp)



Vervolgens wordt u doorgestuurd naar het inlogscherm: voer uw hoofdwachtwoord in om te controleren of alles correct werkt.



![Image](assets/fr/08.webp)



### Maak je eerste kluis



Zodra u bent ingelogd, zal PearPass u vragen om uw eerste safe aan te maken. Een safe is een versleutelde container waarin uw wachtwoorden, ID's, beveiligde notities en andere informatie worden opgeslagen. Elke safe is geïsoleerd en kan worden geïdentificeerd met een aparte naam, zodat u uw gegevens kunt organiseren op basis van uw gebruik (persoonlijk, professioneel, specifieke projecten...).



Klik op de knop `Een nieuwe kluis maken`.



![Image](assets/fr/09.webp)



Kies een naam voor deze kluis en klik dan nogmaals op `Een nieuwe kluis maken` om het aanmaken af te ronden.



![Image](assets/fr/10.webp)



Je kluis is meteen klaar voor gebruik. Je kunt meteen beginnen met het toevoegen van wachtwoorden, logins of beveiligde notities.



![Image](assets/fr/11.webp)



## Hoe voeg ik een login toe aan PearPass?



Zodra u uw kluis heeft aangemaakt, kunt u beginnen met het opslaan van uw items erin. PearPass ondersteunt de registratie van vele soorten items:




- inloggen op een site of service ;
- identiteit: uw persoonlijke gegevens om snel formulieren in te vullen, maar ook om identiteitsdocumenten direct in PearPass op te slaan;
- creditcard: je creditcardnummers voor snellere betaling bij online winkelen;
- Wi-Fi: wachtwoorden voor je Wi-Fi-netwerken ;
- PassPhrase: geheime zin samengesteld uit meerdere woorden (waarschuwing: ik raad het gebruik voor wallet Bitcoin geheugenzinnen sterk af);
- opmerking: beveiligde notities maken ;
- aangepast: met deze functie kun je een aangepast elementtype maken, aangepast aan je specifieke behoeften.



Begin met het openen van PearPass en log in met uw hoofdwachtwoord.



![Image](assets/fr/12.webp)



Selecteer de safe waarin je deze identifier wilt opslaan.



![Image](assets/fr/13.webp)



Op de startpagina klik je op de knop om een nieuw item toe te voegen, afhankelijk van het type informatie dat je wilt vastleggen. In mijn geval wil ik een login toevoegen voor mijn account op de Plan ₿ Academy website: dus klik ik op de `Maak een Login` knop.



![Image](assets/fr/14.webp)



Zodra je het type item hebt geselecteerd dat je wilt toevoegen, verschijnt er een formulier waarmee je de informatie kunt invoeren die bij de service in kwestie hoort. Afhankelijk van je behoeften kun je de naam van de service, de login, het wachtwoord en, indien nodig, het adres van de website en extra notities invoeren.



PearPass heeft ook een wachtwoordgenerator, waarmee u direct vanaf het formulier een sterk wachtwoord kunt maken. Om deze te gebruiken klikt u op het pictogram met de drie kleine puntjes in het veld `Wachtwoord`, kiest u de gewenste lengte en klikt u vervolgens op `Wachtwoord invoegen`.



Als alle velden zijn ingevuld, klikt u op de knop `Opslaan` om de identificatiecode op te slaan in de kluis.



![Image](assets/fr/15.webp)



De identificatiecode wordt nu opgeslagen. Hij verschijnt in de lijst met items in de geselecteerde kluis en kan worden bekeken door erop te klikken.



![Image](assets/fr/16.webp)



Je kunt een element eenvoudig wijzigen door erop te klikken en vervolgens op de knop `Edit`. Je kunt het ook verwijderen door op de drie kleine puntjes rechtsboven in de interface te klikken en vervolgens op `Element verwijderen`.



![Image](assets/fr/22.webp)



Op mobiel blijft de logica hetzelfde, hoewel de interface is aangepast. Selecteer na het inloggen de gewenste kluis, tik op de `+` knop, kies het type item dat moet worden aangemaakt en vul vervolgens de benodigde informatie in.



![Image](assets/fr/17.webp)



## Hoe organiseer ik PearPass?



Zoals we in de vorige secties hebben gezien, kunt u met PearPass verschillende kluizen aanmaken. Dit maakt het mogelijk om verschillende toepassingen te scheiden en vormt een eerste niveau van organisatie voor uw wachtwoordmanager. Vanaf de startpagina kunt u eenvoudig overschakelen van de ene kluis naar de andere door te klikken op de pijl linksboven in de interface.



![Image](assets/fr/18.webp)



Een andere manier om je wachtwoorden te organiseren, zelfs binnen een kluis, is door mappen aan te maken. Om dit te doen, klik je in de linkerkolom van de interface op het `+` symbool naast `Alle mappen` en voer je de naam in van de map die je wilt aanmaken.



![Image](assets/fr/19.webp)



Je kunt dan de identifiers van je keuze opslaan, direct bij het maken van een item, of later door op `Bewerken` te klikken. Het enige wat je hoeft te doen is de gewenste map te selecteren in de linkerbovenhoek van het formulier.



![Image](assets/fr/20.webp)



Na het openen van een item, zoals een aanmelding, kun je op het sterpictogram rechtsboven in de interface klikken om het toe te voegen aan je favorieten. Favorieten zijn snel terug te vinden in een speciale map, naast hun basismap.



![Image](assets/fr/21.webp)



Tot slot is er een zoekbalk bovenaan de interface, zodat je snel het item kunt vinden dat je zoekt, zelfs als je kluis veel identifiers bevat.



## Hoe synchroniseer ik PearPass op mijn mobiel?



Nu je een werkende kluis hebt met items die zijn opgeslagen op je computer, wil je waarschijnlijk je wachtwoorden openen vanaf je smartphone of een ander apparaat. Met PearPass kunt u uw manager op meerdere machines veilig synchroniseren met Pears. Laten we eens kijken hoe.



Om te beginnen logt u op de bronmachine (bijvoorbeeld uw computer) in op uw kluis met uw hoofdwachtwoord. Klik op de startpagina op de knop `Add a Device` rechtsonder in de interface.



![Image](assets/fr/23.webp)



PearPass genereert dan een uitnodigingslink, ook beschikbaar als QR-code, om de geselecteerde kluis te synchroniseren op het apparaat van uw keuze.



![Image](assets/fr/24.webp)



Als je wilt synchroniseren op je mobiele apparaat, installeer dan eerst de applicatie en start deze op. Je wordt gevraagd om een hoofdwachtwoord aan te maken voor je mobiele manager. Je kunt hetzelfde wachtwoord gebruiken als op je computer, of een ander. Volg in alle gevallen dezelfde aanbevelingen: een sterk, willekeurig wachtwoord opgeslagen op een fysieke drager.



![Image](assets/fr/25.webp)



Je kunt dan desgewenst biometrische verificatie activeren om te voorkomen dat je elke keer dat je je mobiel ontgrendelt handmatig je hoofdwachtwoord moet invoeren.



![Image](assets/fr/26.webp)



Voer je hoofdwachtwoord opnieuw in en klik op de knop `Doorgaan`.



![Image](assets/fr/27.webp)



Selecteer de `Load a vault` optie, klik dan op `Scan QR Code` en scan de uitnodiging QR code die wordt weergegeven door PearPass op uw bronmachine (de computer).



![Image](assets/fr/28.webp)



Je kluizen op je computer en je mobiel zijn nu gesynchroniseerd. Elke ID die op het ene apparaat wordt toegevoegd, wordt veilig opgeslagen en gerepliceerd op het andere apparaat.



![Image](assets/fr/29.webp)



Op mobiele telefoons kun je het automatisch vullen van velden ook activeren. Ga hiervoor naar `Instellingen > Geavanceerd` en klik vervolgens op de knop `Instellen als standaard` in het gedeelte `Autovullen`.



![Image](assets/fr/30.webp)



## Hoe synchroniseer ik PearPass met de browserextensie?



Een wachtwoordmanager hebben die gesynchroniseerd is tussen je computer en je smartphone is al erg praktisch, maar het direct integreren in je browser is nog praktischer. Om dit te doen, begint u met [de officiële PearPass-extensie toe te voegen aan uw browser] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Vanuit de PearPass software die op uw lokale machine is geïnstalleerd, gaat u naar `Instellingen > Geavanceerd` en activeert u de optie `Browserextensie activeren`.



![Image](assets/fr/32.webp)



PearPass genereert een token koppelingsbestand. Kopieer het.



![Image](assets/fr/33.webp)



Open dan de PearPass extensie in je browser, plak de token koppeling erin en klik op de `Verifieer` knop, gevolgd door `Voltooi`.



![Image](assets/fr/34.webp)



Uw wachtwoordmanager is nu gesynchroniseerd met de browserextensie.



![Image](assets/fr/35.webp)



Je kunt het nu gebruiken om eenvoudig verbinding te maken met je verschillende webaccounts.



![Image](assets/fr/36.webp)



Nu weet u hoe u de PearPass wachtwoordmanager moet gebruiken. Naast deze tool is de dagelijkse digitale veiligheid afhankelijk van het juiste gebruik van de juiste oplossingen. Als u wilt leren hoe u een veilige, stabiele en efficiënte persoonlijke digitale omgeving opzet, nodig ik u uit om onze training over dit onderwerp te ontdekken:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1