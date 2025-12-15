---
name: Ente Auth
description: Een open-source, end-to-end versleutelde 2FA-authenticator
---
![cover](assets/cover.webp)



Twee-factor authenticatie (2FA) is onmisbaar geworden voor het beveiligen van onze online accounts. Naast je gebruikelijke wachtwoord heb je een tijdelijke code nodig, meestal gegenereerd door een speciale applicatie. Dit mechanisme, bekend als TOTP (Time-Based One-Time Password), garandeert dat zelfs als je wachtwoord gecompromitteerd is, een aanvaller geen toegang kan krijgen tot je account zonder deze tweede factor, die elke 30 seconden wordt vernieuwd.



Het kiezen van de juiste authenticatietoepassing is echter niet triviaal. Google Authenticator, hoewel populair, heeft grote beperkingen: propriëtaire code die onmogelijk te controleren is, synchronisatie zonder end-to-end encryptie en het risico van totaal verlies van codes in het geval van een probleem met je telefoon. Andere oplossingen, zoals Authy, vereisen een telefoonnummer en garanderen geen volledige vertrouwelijkheid.



**Ente Auth** onderscheidt zich als een modern, veilig alternatief. Deze gratis, open source, cross-platform applicatie, ontwikkeld door het team achter [Ente Photos](https://ente.io), biedt end-to-end versleutelde cloud back-ups en naadloze synchronisatie tussen al je apparaten. In tegenstelling tot propriëtaire oplossingen geeft Ente Auth je volledige controle over je verificatiecodes zonder je privacy in gevaar te brengen.



In deze tutorial laten we je stap voor stap zien hoe je Ente Auth installeert en gebruikt, en waarom deze oplossing verschilt van traditionele authenticators.



## Ente Auth introduceren



Ente Auth is ontwikkeld door het team achter Ente Photos, een end-to-end versleutelde en privacy-vriendelijke foto-opslagdienst. Trouw aan de Ente-filosofie ("Ente" betekent "mijn" in het Maleis, wat staat voor controle over je gegevens), is Ente Auth ontworpen om gebruikers weer volledige controle te geven over hun twee-factor authenticatiecodes.



### Belangrijkste kenmerken



**Standaard TOTP-codes**: Ente Auth genereert tijdelijke codes die compatibel zijn met de meeste diensten (GitHub, Google, Binance, ProtonMail, etc.). Je kunt zoveel 2FA-accounts toevoegen als je nodig hebt en de applicatie berekent de codes op basis van de opgegeven geheimen.



**End-to-end versleutelde cloudback-up**: Je codes worden veilig online opgeslagen. Alleen jij kunt ze decoderen - de coderingssleutel is afgeleid van je wachtwoord en is alleen bij jou bekend. Ente (de server) heeft geen kennis van je geheimen, of zelfs van je accounttitels, omdat alles aan de clientkant wordt versleuteld met behulp van een zero-knowledge architectuur.



**Synchronisatie met meerdere apparaten**: U kunt Ente Auth op meerdere apparaten installeren (smartphone, tablet, computer) en op al deze apparaten toegang krijgen tot uw codes. Alle wijzigingen worden automatisch en direct doorgegeven aan uw andere apparaten via de versleutelde cloud, wat u veel flexibiliteit geeft in uw dagelijkse werk.



**Minimalistische, intuïtieve Interface**: De applicatie biedt een gestroomlijnde Interface, eenvoudig te leren, zelfs voor niet-technische gebruikers. 2FA-accounts worden weergegeven met de naam van de service, uw login en de 6-cijferige code, die in realtime wordt bijgewerkt. Ente Auth geeft ook de volgende code een paar seconden van tevoren weer om te voorkomen dat u wordt verrast door een verlopen code.



**Open source en gecontroleerd**: De broncode van Ente Auth is [openbaar op GitHub](https://github.com/ente-io/auth) onder de AGPL v3.0 licentie. Elke ontwikkelaar kan het controleren op fouten of ongewenst gedrag. De geïmplementeerde cryptografie is het onderwerp geweest van een [onafhankelijke externe audit](https://ente.io/blog/cryptography-audit/), een garantie voor de ernst van de beveiliging van de applicatie.



### Voordelen en beperkingen



**Voordelen:**




- Ontworpen privacy met end-to-endencryptie
- Veilige synchronisatie tussen al je apparaten
- Controleerbare open broncode
- Interface duidelijke, intuïtieve gebruiker Interface
- Automatische back-up om verlies van codes te voorkomen
- Beschikbaar op alle platforms (mobiel en desktop)



**Limieten:**




- Internetverbinding vereist voor synchronisatie
- Gevorderde gebruikers geven misschien de voorkeur aan 100% offline oplossingen zoals Aegis (alleen Android)
- Relatief recent vergeleken met gevestigde oplossingen



## Installatie



Ente Auth is beschikbaar op de meeste populaire platforms. Je kunt de applicatie downloaden van [de officiële website](https://ente.io/auth) of van de officiële stores.



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth downloadpagina met alle beschikbare platforms*



### Android


Je hebt verschillende opties:




- **Google Play Store**: Zoek naar "Ente Auth" voor klassieke installatie
- **F-Droid**: Beschikbaar uit de Android open-source applicatiecatalogus, met de garantie van geverifieerde constructie en zonder merkgebonden inhoud
- **Handmatige installatie**: APK-bestanden kunnen worden gedownload van de [GitHub-pagina van het project](https://github.com/ente-io/auth/releases) met geïntegreerde melding van nieuwe versies



### iOS (iPhone/iPad)


Installeer Ente Auth rechtstreeks vanuit de Apple App Store door te zoeken naar de naam van de app. Het iOS-programma kan ook worden uitgevoerd op Macs met Apple Silicon-chips (M1/M2) via de Mac App Store.



### Computers (Windows, macOS, Linux)


Ente Auth biedt native desktop applicaties. Bezoek [ente.io/download](https://ente.io/download) of de [Releases sectie van GitHub](https://github.com/ente-io/auth/releases) :





- **Windows**: Er wordt een EXE-installatieprogramma meegeleverd
- **macOS**: DMG-schijfimage slepen en neerzetten in Toepassingen
- **Linux**: Verschillende formaten beschikbaar (AppImage portable, .deb voor Debian/Ubuntu, .rpm voor Fedora/Red Hat)



**Noot:** Deze handleiding is gebaseerd op Ente Auth v4.4.4 en hoger. Eerdere versies kunnen kleine Interface verschillen hebben.



### Interface web


Zonder installatie hebt u toegang tot uw codes via [auth.ente.io](https://auth.ente.io) vanuit elke browser. Interface web is beperkt tot het bekijken van codes (handig voor het oplossen van problemen), omdat voor het toevoegen van accounts om veiligheidsredenen de mobiele of desktopapplicatie nodig is.



## Eerste configuratie



### Account aanmaken



Wanneer je Ente Auth voor het eerst start, heb je twee opties:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Ente Auth-homescherm met opties voor het aanmaken van een account*



**Met account (aanbevolen)**: Kies "Account aanmaken" en voer je e-mail Address en een wachtwoord in. **Belangrijk**: dit wachtwoord dient als hoofdwachtwoord voor het versleutelen van je gegevens. Kies een sterk, uniek wachtwoord, want er is geen conventionele resetprocedure zonder gegevensverlies. Als je het vergeet, zijn je versleutelde gegevens onherstelbaar.



**Offline-modus**: Selecteer "Gebruik zonder back-ups" om de applicatie lokaal zonder cloud te gebruiken. In deze modus blijven je codes op het apparaat staan, maar moet je ze handmatig exporteren om te voorkomen dat je ze kwijtraakt.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Verificatieproces via e-mail en genereren van 24-woord herstelsleutel*



Er kan om een e-mailverificatie worden gevraagd om het aanmaken van een account te valideren en herstel op een nieuw apparaat mogelijk te maken. Ente Auth zal je ook voorzien van een 24-woorden herstelsleutel (gebaseerd op de BIP39-methode). **Het is absoluut noodzakelijk dat u deze sleutel** op een veilige plaats bewaart: het is uw enige manier om uw gegevens te herstellen als u uw wachtwoord vergeet.



### Lokale veiligheid



Ik raad sterk aan om lokale beveiliging met een code of biometrie in te schakelen. Ga naar **Instellingen → Beveiliging → Vergrendelscherm** en configureer :





- **Biometrische ontgrendeling**: Face ID, vingerafdruk afhankelijk van de mogelijkheden van je apparaat
- Toepassingsspecifieke pincode/wachtwoord
- **Vertraging bij automatisch vergrendelen**: bijv. "Onmiddellijk" of na 30 seconden inactiviteit



Deze bescherming voorkomt onbevoegde toegang tot je codes als iemand toegang krijgt tot je ontgrendelde telefoon. Merk op dat deze vergrendeling een extra barrière is: je gegevens blijven end-to-end versleuteld, zelfs zonder deze bescherming.



## 2FA-accounts toevoegen



### Standaardprocedure



Om een nieuw 2FA-account toe te voegen, nemen we het concrete voorbeeld van het activeren van 2FA op Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Ente Auth's hoofd Interface klaar om eerste 2FA* account toe te voegen



**Servicezijde (Bull Bitcoin)**: Log in op uw Bull Bitcoin account, ga naar de beveiligingsinstellingen en schakel twee-factor authenticatie in.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* menu veiligheidsinstellingen



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Optie om authenticatie met twee factoren in te schakelen op Bull Bitcoin*



De service toont dan een QR-code die je kunt scannen met je authenticatietoepassing:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*QR-code gegenereerd door Bull Bitcoin om te scannen met uw authenticator*



**In Ente Auth**: Klik op "Voer een instelsleutel in" en scan vervolgens de QR-code die Bull Bitcoin weergeeft. Ente Auth herkent het account automatisch en vult de velden in.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Bull Bitcoin accountgegevens configureren in Ente Auth*



Je kunt de naam van de service en je login aanpassen zodat het gemakkelijker te vinden is. Geavanceerde instellingen (SHA1-algoritme, 30s periode, 6 cijfers) zijn over het algemeen standaard correct.



**Service-validatie**: Ga terug naar Bull Bitcoin en voer de door Ente Auth gegenereerde 6-cijferige code in om de activering te voltooien.



![Saisie du code 2FA](assets/fr/09.webp)



*Voer de door Ente Auth gegenereerde code in om de activering van 2FA* te valideren



![2FA activée](assets/fr/10.webp)



*Bevestiging van succesvolle 2FA activering op Bull Bitcoin*



**Back-up codes**: Bull Bitcoin voorziet u van herstelcodes. **Bewaar ze op een veilige plaats, los van uw authenticator.**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Optie voor generate noodback-upcodes op Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Lijst met herstelcodes om op een veilige plaats te bewaren*



### Organisatie en beheer



Ente Auth biedt verschillende praktische functies:



**Snel kopiëren**: Druk op de code om deze automatisch naar het klembord te kopiëren.



**Contextgevoelige acties**: Houd ingedrukt (of klik met de rechtermuisknop op het bureaublad) om een item te bewerken, verwijderen, delen of vast te zetten.



**Tags en zoeken**: Organiseer je accounts met tags (persoonlijk/professioneel, per servicecategorie) en gebruik de zoekbalk om snel te filteren.



![Création d'un tag](assets/fr/17.webp)



*Tag-aanmaakproces: contextueel menu en aanmaakdialoog*



![Tag appliqué](assets/fr/18.webp)



*Tag "Bitcoin" succesvol toegepast op Bull Bitcoin* account



**Automatische pictogrammen**: Elk item kan worden geïllustreerd met het logo van de service, dankzij de integratie van het pictogrammenpakket [Simple Icons] (https://simpleicons.org/).



**Tijdelijk veilig delen**: Met beveiligd delen, een unieke Ente Auth-functie, kunt u een 2FA-code naar een collega sturen zonder het onderliggende geheim te onthullen. generate een versleutelde link die maximaal 2, 5 of 10 minuten geldig is - de ontvanger ziet de code in realtime, maar kan deze niet exporteren of toegang krijgen tot accountgegevens. Deze methode is ideaal voor technische ondersteuning of tijdelijke samenwerking en biedt een beveiligingsniveau dat niet mogelijk is met een eenvoudige schermafbeelding of sms.



![Partage sécurisé](assets/fr/19.webp)



*Interface tijdelijk veilig delen: kies duur (5 min)*



**Veilige export/import**: Met Ente Auth kunt u uw codes exporteren naar andere toepassingen of importeren vanuit Google Authenticator en andere oplossingen. De export vindt plaats via een versleuteld bestand of een QR-code, waardoor de overdraagbaarheid van uw gegevens wordt gegarandeerd zonder dat dit ten koste gaat van de beveiliging.



**BIP39 herstelsleutel**: De applicatie genereert automatisch een 24-woorden herstelzin volgens de BIP39 (Bitcoin Improvement Proposal) standaard, identiek aan cryptocurrency wallets. Deze zin is je ultieme herstelsleutel, waarmee je al je codes kunt herstellen, zelfs als je je hoofdwachtwoord vergeet.



## Configuratie en instellingen



Ente Auth biedt talloze aanpassingsopties die toegankelijk zijn via de instellingen van de applicatie:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Overzicht van beschikbare parameters in Ente Auth*



### Account- en gegevensbeheer



![Paramètres de sécurité](assets/fr/14.webp)



*Geavanceerde beveiligingsopties: e-mailverificatie, PIN-code, actieve sessies*



Met de beveiligingsinstellingen kunt u :




- E-mailverificatie inschakelen voor nieuwe verbindingen
- Activeer paswoord
- Bekijk actieve sessies op uw verschillende apparaten
- Een pincode of biometrische gegevens instellen



### Interface en gebruiksopties



![Paramètres généraux](assets/fr/15.webp)



*Interface parameters en toepassingsaanpassingen*



Algemene instellingen zijn onder andere :




- **Taal**: Interface meertalig
- **Beeldscherm**: Grote pictogrammen, compacte modus
- **Privacy**: Verberg codes, snel zoeken
- **Telemetrie**: Foutrapportage (kan worden uitgeschakeld)



## Back-up en synchronisatie



### Hoe encryptie werkt



Wanneer je een account toevoegt met een verbonden Ente account, versleutelt de applicatie deze gevoelige gegevens onmiddellijk lokaal met behulp van je moedersleutel (afgeleid van je wachtwoord). De versleutelde gegevens worden vervolgens naar de Ente-server verzonden voor opslag.



Dankzij dit mechanisme is er altijd een end-to-end versleutelde cloudback-up van uw codes beschikbaar. Als je je apparaat verliest, installeer je Ente Auth gewoon opnieuw en maak je opnieuw verbinding: de applicatie zal automatisch al je codes downloaden en decoderen.



### Synchronisatie met meerdere apparaten



Als je Ente Auth zowel op je smartphone als op je computer gebruikt, verschijnen toevoegingen of wijzigingen op het ene apparaat binnen enkele seconden op het andere. Deze synchronisatie verloopt via Ente's cloud, maar omdat de gegevens end-to-end versleuteld zijn, ziet de server alleen onleesbare versleutelde inhoud.



![Synchronisation mobile](assets/fr/16.webp)



*Synchronisatiedemo: hetzelfde Bull Bitcoin account toegankelijk op mobiel en desktop*



Synchronisatie is naadloos: installeer Ente Auth op uw smartphone, log in met uw gegevens en al uw 2FA-codes (hier Bull Bitcoin) verschijnen automatisch. Het voorbeeld hierboven toont een perfecte synchronisatie tussen desktop en mobiel - dezelfde Bull Bitcoin code is toegankelijk op beide apparaten.



Wat betreft vertrouwelijkheid: noch Ente, noch derden hebben toegang tot je 2FA-geheimen. Zelfs metadata (tags, notities, servicenamen) worden versleuteld voordat ze worden verzonden. Deze zero-knowledge architectuur zorgt ervoor dat alleen jij je codes kunt ontcijferen.



### Offline gebruik



Voor synchronisatie is internet nodig, maar Ente Auth werkt perfect offline op elk apparaat, omdat alle gegevens lokaal worden opgeslagen. Offline wijzigingen worden in een wachtrij geplaatst en gesynchroniseerd zodra de verbinding is hersteld.



## Veiligheid en privacy



### Cryptografische garanties



Ente Auth is gebaseerd op robuuste end-to-end versleuteling met een zero-knowledge architectuur. Uw codes worden versleuteld met een sleutel die alleen u bezit, afgeleid van uw hoofdwachtwoord met behulp van geavanceerde functies voor sleutelafleiding.



**Nul-kennis architectuur:** Ente heeft geen fysieke toegang tot uw gegevens. Zelfs metagegevens (servicenamen, tags, notities) worden aan de clientzijde versleuteld voordat ze worden verzonden. Deze aanpak zorgt ervoor dat, in het geval van een aanval op uw servers of een verzoek van de overheid, Ente alleen gecodeerde gegevens kan vrijgeven die niet kunnen worden gelezen zonder uw wachtwoord.



**Lokale codering**: Het versleutelingsproces vindt volledig plaats op uw apparaat voordat het naar de cloud wordt verzonden. De servers van Ente ontvangen en bewaren alleen versleutelde gegevens, waardoor onbevoegde toegang onmogelijk is, zelfs voor servicebeheerders.



### Transparantie en audits



Aangezien de code [open source](https://github.com/ente-io/auth) is, kan de gemeenschap de afwezigheid van achterdeurtjes verifiëren. Ente heeft [meerdere externe audits](https://ente.io/blog/cryptography-audit/) laten uitvoeren om de veiligheid van de implementatie te valideren:





- **Cure53** (Duitsland): Controle van applicatie- en cryptografische beveiliging
- **Symbolic Software** (Frankrijk): Gespecialiseerde cryptografische expertise
- **Fallible** (India): Penetratietests en kwetsbaarheidsanalyse



Deze onafhankelijke audits, uitgevoerd door erkende bedrijven, garanderen dat de cryptografische implementatie van Ente Auth voldoet aan de beste beveiligingspraktijken en geen kritieke fouten bevat.



### Privacybeleid



Ente Auth hanteert een [voorbeeldig privacybeleid] (https://ente.io/privacy/) dat is gebaseerd op minimale gegevensverzameling. Alleen informatie die strikt noodzakelijk is voor de werking van de service wordt bewaard: uw e-mail Address voor verificatie en accountherstel.



**Geen tracking of telemetrie**: In tegenstelling tot de meeste applicaties verzamelt Ente Auth geen gebruiksgegevens, geen identificerende crashgegevens en geen gedragsinformatie. De applicatie werkt zonder opdringerige reclame of analytische trackers.



**GDPR-naleving**: Ente voldoet volledig aan de Europese Algemene Verordening Gegevensbescherming. Je hebt te allen tijde het recht om je gegevens in te zien, te corrigeren of te verwijderen. Data export] (https://ente.io/take-control/) is slechts een klik verwijderd, en het permanent verwijderen van je account verwijdert al je gegevens van de servers.



**Gedecentraliseerde, veilige opslag**: Uw versleutelde gegevens worden gerepliceerd op 3 verschillende providers, in 3 verschillende landen, waardoor optimale beschikbaarheid wordt gegarandeerd en afhankelijkheid van één cloudprovider wordt voorkomen.



Het bedrijfsmodel van Ente is gebaseerd op de betaalde service Ente Photos, waardoor we Ente Auth **gratis en zonder beperkingen** kunnen aanbieden zonder je privacy in gevaar te brengen door je gegevens te gelde te maken. Deze aanpak garandeert de duurzaamheid van de service zonder afhankelijk te zijn van advertenties of de doorverkoop van persoonlijke gegevens.



## Vergelijking met andere oplossingen



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth onderscheidt zich als een van de weinige oplossingen die alle voordelen combineert: transparantie van de broncode, versleutelde cloudback-up en platformoverkoepelende synchronisatie.



## Aanbevolen gebruikssituaties



### Individuele gebruikers



Ente Auth is ideaal voor veiligheidsbewuste personen die systematisch 2FA activeren. Je hoeft je geen zorgen meer te maken dat je je codes kwijtraakt als je van telefoon wisselt, of dat je moet kiezen tussen gemak en veiligheid.



### Gebruik voor gezinnen en meerdere apparaten



De app komt het best tot zijn recht als je meerdere apparaten gebruikt. Je kunt je codes opslaan op smartphones en tablets, of bepaalde familiecodes (Netflix, familiecloud) synchroon en veilig delen.



### Professioneel gebruik



Voor teams die gevoelige accounts beheren, vergemakkelijkt Ente Auth de samenwerking terwijl de beveiliging behouden blijft, dankzij de geavanceerde functies voor delen die zijn geïntegreerd in het gedeelte "Organisatie en beheer".



## Beste praktijken





- **Bewaar je noodcodes**: Bewaar de herstelcodes die door elke service worden geleverd uit de buurt van je telefoon.





- **Gebruik een sterk hoofdwachtwoord**: Je Ente Auth masterwachtwoord moet uniek en robuust zijn, omdat het al je codes beschermt.





- **Activeer lokale beveiliging**: PIN of biometrie configureren om ongeoorloofde fysieke toegang te voorkomen.





- **Niet te veel aanpassen**: Vermijd geavanceerde aanpassingen die de synchronisatie in gevaar kunnen brengen.





- **Houd de applicatie up-to-date**: Updates corrigeren beveiligingslekken en verbeteren de functionaliteit.





- **Test herstel**: Controleer af en toe of je je codes kunt herstellen op een ander apparaat.



## Conclusie



Ente Auth is een moderne, uitgebreide oplossing voor twee-factor authenticatie. Door beveiliging, transparantie en gebruiksgemak te combineren, voldoet deze open source applicatie aan de behoeften van veeleisende gebruikers zonder aan gebruiksgemak in te boeten.



In tegenstelling tot propriëtaire oplossingen die je opsluiten in een ondoorzichtig ecosysteem, geeft Ente Auth je de controle terug over je verificatiegegevens terwijl het je beschermt tegen onopzettelijk verlies dankzij de versleutelde back-ups.



Of je nu een individu bent die zijn persoonlijke accounts wil beveiligen, of een team dat zakelijke toegang beheert, Ente Auth is een slimme keuze voor het moderniseren van je benadering van digitale beveiliging zonder de privacy in gevaar te brengen.



## Hulpmiddelen en ondersteuning



### Officiële documentatie




- **Officiële website**: [ente.io/auth](https://ente.io/auth)
- **Helpcentrum**: [help.ente.io/auth](https://help.ente.io/auth)
- **Technische blog**: [ente.io/blog](https://ente.io/blog)



### Broncode en transparantie




- **GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- **Cryptografie-audit**: [ente.io/blog/cryptografie-audit](https://ente.io/blog/cryptography-audit)



### Gemeenschap




- **Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**: [r/enteio](https://reddit.com/r/enteio)