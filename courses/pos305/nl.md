---
name: Bitcoin en BTC-betaalserver
goal: Installeer BTC Pay Server voor uw bedrijf
objectives: 

  - Begrijp wat btcpayserver is.
  - BTC Pay Server zelf hosten en configureren.
  - Gebruik btcpayserver in je dagelijkse activiteiten.

---

# Bitcoin en BTCPay-server


Dit is een inleidende cursus over BTCPay Server Operator, geschreven door Alekos en Bas, die werd aangepast voor het Plan ₿ Course Format door melontwist en asi0.


EEN ONVOLTOOID VERHAAL


"Dit zijn leugens, mijn vertrouwen in jou is gebroken, ik zal je overbodig maken".


Geproduceerd door BTCPay Server Foundation


+++

# Inleiding


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Cursus Overzicht


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Welkom bij de POS 305 cursus op BTCPay Server!


Het doel van deze training is om u te leren hoe u BTCPay Server kunt installeren, configureren en gebruiken binnen uw bedrijf of organisatie. BTCPay Server is een open-source oplossing waarmee u Bitcoin betalingen autonoom, veilig en kosteneffectief kunt verwerken. Deze cursus is vooral gericht op gevorderde gebruikers die het zelf hosten van BTCPay Server onder de knie willen krijgen voor volledige integratie in hun dagelijkse werkzaamheden.


**Deel 1: Inleiding tot BTCPay Server**

We beginnen met een algemene presentatie van BTCPay Server, inclusief het inlogscherm, gebruikersaccountbeheer en het aanmaken van een nieuwe winkel. Deze inleiding zal u helpen de BTCPay Server Interface te begrijpen en de basisfuncties te begrijpen die nodig zijn om deze tool te beginnen gebruiken.


**Deel 2: Inleiding tot het beveiligen van Bitcoin sleutels**

De beveiliging van uw Bitcoin fondsen is erg belangrijk. In deze sectie zullen we het genereren van cryptografische sleutels, het gebruik van hardware wallets om deze sleutels te beveiligen, en de interactie met uw sleutels via BTCPay Server onderzoeken. U zult ook leren hoe u een BTCPay Server Lightning Wallet kunt configureren om uw transacties te optimaliseren.


**Deel 3: BTCPay Server Interface**

Dit deel leidt u door de BTCPay Server gebruiker Interface. U zult leren hoe u door het dashboard kunt navigeren, winkel- en serverinstellingen kunt configureren, betalingen kunt beheren en gebruik kunt maken van geïntegreerde plugins. Het doel is om u te voorzien van de tools die nodig zijn om uw installatie aan te passen aan uw specifieke behoeften.


**Deel 4: BTCPay server configureren**

Tot slot richten we ons op de praktische installatie van BTCPay Server in verschillende omgevingen. Of u nu LunaNode, Voltage of een Umbrel node gebruikt, u leert de essentiële stappen om uw BTCPay Server te implementeren en te configureren, rekening houdend met de specifieke kenmerken van elke omgeving.


Klaar om BTCPay Server onder de knie te krijgen en uw bedrijf te laten groeien? Laten we beginnen!


## Lovende kritieken voor Author's Bitcoin en BTCPay Server


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Laten we beginnen met te begrijpen wat BTCPay Server is en waar het vandaan komt. Wij hechten waarde aan transparantie en bepaalde standaarden om vertrouwen te vormen in de Bitcoin ruimte.

Een project in de ruimte brak deze waarden. De hoofdontwikkelaar van BTCPay Server, Nicolas Dorier, nam dit persoonlijk en deed de belofte om ze te vervangen. Hier zijn we dan, vele jaren later, en we werken aan deze toekomst, volledig open-source, elke dag.


> Dit zijn leugens, mijn vertrouwen in jou is gebroken, ik zal je overbodig maken.
> Nicolas Dorier

Na de woorden van Nicolas was het tijd om te gaan bouwen. Er ging een aanzienlijke hoeveelheid werk zitten in wat we nu BTCPay Server noemen. Meer mensen wilden bijdragen aan deze inspanning. De meest herkenbare zijn r0ckstardev, MrKukks, Pavlenex, en de eerste merchant die de software gebruikte, astupidmoose.


Wat betekent open source en wat komt er kijken bij zo'n project?


FOSS staat voor Free & Open-Source Software. Het eerste verwijst naar termen die iedereen toestaan om versies van de software te kopiëren, aan te passen en zelfs te verspreiden (zelfs met winstoogmerk). Het tweede verwijst naar het openlijk delen van de broncode, waardoor het publiek wordt aangemoedigd om bij te dragen en de code te verbeteren.

Dit trekt ervaren gebruikers aan die enthousiast zijn om bij te dragen aan de software die ze al gebruiken en waar ze waarde uit halen, wat uiteindelijk succesvoller blijkt te zijn in de adoptie dan propriëtaire software. Het is in overeenstemming met het Bitcoin ethos dat "informatie vrij wil zijn" Het brengt gepassioneerde mensen samen die een gemeenschap vormen en het is gewoon leuker. Net als Bitcoin is FOSS onvermijdelijk.


### Voordat we beginnen


Deze cursus bestaat uit meerdere onderdelen. Veel wordt verzorgd door je klasseleraar, Demo omgevingen waar je toegang tot krijgt, een gehoste server voor jezelf en eventueel een domeinnaam. Als je deze cursus zelfstandig afrondt, houd er dan rekening mee dat de omgevingen met het label DEMO niet voor jou beschikbaar zijn.

NB. Als je deze cursus in een klaslokaal volgt, kunnen de servernamen verschillen afhankelijk van de inrichting van het klaslokaal. Variabelen in Servernamen kunnen hierdoor afwijken.


### Cursusstructuur


Elk hoofdstuk heeft doelstellingen en kennistoetsen. In deze cursus behandelen we elk van deze doelstellingen en geven we een samenvatting van de belangrijkste kenmerken aan het einde van elk lesblok (d.w.z. hoofdstuk). Illustraties worden gebruikt om visuele feedback te geven en belangrijke concepten visueel te versterken. Aan het begin van elk lesblok worden doelen gesteld. Deze doelstellingen gaan verder dan een checklist. Ze geven je een leidraad voor nieuwe vaardigheden. De kennisevaluaties worden geleidelijk uitdagender naarmate de setup van uw BTCPay-server voltooid is.


### Wat krijgen studenten bij de cursus?


Met de BTCPay Server Cursus kan een student de basisprincipes, technisch en niet-technisch, van Bitcoin begrijpen. De uitgebreide training in het gebruik van Bitcoin door BTCPay Server zal studenten in staat stellen hun eigen Bitcoin infrastructuur te beheren.


### Belangrijke webadressen of contactmogelijkheden


De BTCPay Server Foundation, die Alekos en Bas in staat stelde om deze cursus te schrijven, bevindt zich in Tokio, Japan. De BTCPay Server Foundation kan worden bereikt via de genoemde website.



- https://foundation.btcpayserver.org
- Ga naar de officiële chatkanalen: https://chat.btcpayserver.org


## Inleiding tot Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Bitcoin begrijpen via klassikale oefening


Dit is een klassikale oefening, dus als je deze cursus zelf volgt, kun je hem niet uitvoeren, maar je kunt deze oefening wel doorlopen. Om deze opdracht uit te voeren zijn minimaal 9 tot 11 mensen nodig.


De oefening begint na het bekijken van de inleiding "Hoe Bitcoin en de Blockchain werken" door de BBC.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Voor deze oefening zijn minimaal negen deelnemers nodig. Deze oefening is bedoeld om fysiek te begrijpen hoe Bitcoin werkt. Door elke rol in het netwerk te spelen, leer je op een interactieve en speelse manier. Bij deze oefening is Lightning Network niet betrokken.


### Voorbeeld: Vereist 9 / 11 personen


De rollen zijn:



- 1 Klant
- 1 Koopman
- 7 tot 9 Bitcoin knooppunten


**Instellen gaat als volgt:**


Klanten kopen een product in de winkel met Bitcoin.


**Scenario 1 - Traditioneel banksysteem**



- Opzetten:
  - Zie de diagrammen/uitleg in de bijgevoegde Figjam - [Activiteitenschema] (https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Laat drie student-vrijwilligers de rollen van klant (Alice), handelaar (Bob) en bank spelen.
- Speel de volgorde van de gebeurtenissen na:
  - Klant - bladert online door de winkel en vindt een artikel voor $25 dat hij wil hebben en laat de verkoper weten dat hij het wil kopen
  - Handelaar - vraagt om betaling.
  - Klant - stuurt kaartinformatie naar Merchant
  - Merchant - stuurt informatie naar de Bank (met identificatie van zowel de eigen als de identiteit/informatie), met het verzoek tot betaling van
  - De bank verzamelt informatie over de klant en de Merchant (Alice en Bob) en controleert of het saldo van de klant voldoende is.
  - Trekt \$25 af van de rekening van Alice, voegt \$24 toe aan de rekening van Bob, neemt \$1 voor de dienst
  - De Merchant krijgt een duim omhoog van de Bank en verzendt het item naar de klant.
- Opmerkingen:
  - Bob en Alice moeten een relatie hebben met een bank.
  - De bank verzamelt identificerende informatie over zowel Bob als Alice.
  - Bank neemt een snee.
  - De bank moet erop kunnen vertrouwen dat ze te allen tijde het geld van elke deelnemer bewaart.


**Scenario 2 - Bitcoin Systeem**



- Opzetten:
  - Zie de diagrammen/uitleg in de bijgevoegde Figjam - [Activiteitenschema] (https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Vervang de Bank door negen studenten die de rol spelen van een Computer (Bitcoin Nodes/Miners) in een netwerk om de Bank te vervangen.
- Elk van de 9 computers heeft een volledig historisch overzicht van alle transacties die ooit hebben plaatsgevonden (dus nauwkeurige balansen zonder vervalsingen), evenals een aantal regels:
  - Controleer of de transactie correct is ondertekend (thekeyfitsthelock)
  - Geldige transacties uitzenden en ontvangen naar peers in het netwerk, ongeldige transacties weggooien (inclusief transacties die hetzelfde geld twee keer proberen uit te geven)
- Update/toevoeg records periodiek met nieuwe transacties ontvangen van "willekeurige" computer op voorwaarde dat alle inhoud geldig is (opmerking: we negeren, voor nu, de Proof of Work component van dit alles, voor de eenvoud), anders verwerpen we deze en gaan we verder zoals voorheen totdat de volgende "willekeurige" computer een update stuurt
  - Het juiste bedrag werd beloond als de inhoud geldig was.
- Speel de volgorde van de gebeurtenissen na:
  - Klant - bladert online door de winkel en vindt een artikel voor $25 dat hij wil hebben en laat de verkoper weten dat hij het wil kopen
  - Merchant vraagt om betaling door de klant een Invoice/Address van zijn Wallet te sturen.
  - Klant- construeert een transactie (waarbij $25 aan BTC naar een Address gestuurd wordt die door de Handelaar voorzien is) en zendt die naar het Bitcoin Netwerk.
- Computers: ontvangen de transactie en verifiëren deze:
  - Er wordt minstens $25 aan BTC in de Address verzonden van
  - De transactie is correct ondertekend ("ontgrendeld" door de klant)
  - Als dat niet het geval is, dan wordt de transactie niet gepropageerd door het netwerk, en als dat wel het geval is, dan wordt de transactie gepropageerd en in afwachting gehouden.
  - Handelaren kunnen controleren of de transactie in behandeling is en wacht.
- Eén computer wordt "willekeurig" gekozen om voor te stellen de voorgestelde transactie af te ronden door "een blok" uit te zenden dat de transactie bevat; als het klopt, ontvangen ze een BTC-beloning.
  - OPTIONEEL/GEAVANCEERD - in plaats van willekeurig een computer te kiezen, kun je Mining simuleren door computers te laten dobbelen totdat er een vooraf bepaalde uitkomst is (bijv. de eerste die dubbel zessen gooit wordt geselecteerd)
  - Het kan ook uitspelen wat er zou gebeuren als twee Computers ongeveer tegelijkertijd winnen, wat resulteert in een kettingsplitsing.
  - Computers controleren de geldigheid, updaten/toevoegen records aan hun grootboeken als aan de regels wordt voldaan en zenden het transactieblok uit naar peers.
  - De willekeurig gekozen computer ontvangt een beloning voor het voorstellen van een geldig blok.
  - De transactie van de Merchant-cheques is voltooid; het geld is dus ontvangen en het artikel is naar de klant verzonden.
- Opmerkingen:
  - Merk op dat een bestaande bankrelatie niet nodig was.
  - Geen derde partij nodig om te faciliteren; vervangen door code/prikkels.
  - Geen gegevensverzameling door iemand buiten de directe Exchange, en alleen de noodzakelijke hoeveelheid mag worden uitgewisseld tussen deelnemers (bijv. verzending Address).
  - Er is geen vertrouwen nodig tussen de mensen (behalve de Merchant die het item verstuurt), in veel opzichten zoals bij een contante aankoop.
  - Het geld is direct eigendom van de individuen.
  - De Bitcoin Ledger is voor de eenvoud afgebeeld in dollars, maar in werkelijkheid is het BTC.
  - We simuleren dat een enkele transactie wordt uitgezonden, maar in werkelijkheid zijn er meerdere transacties in behandeling in het netwerk, en blokken bevatten duizenden transacties tegelijk. Knooppunten controleren ook of er geen dubbele transacties in behandeling zijn (ik zou in dit geval alle transacties op één na negeren).
- Valsspeelscenario's:
  - Wat als de klant geen $25 BTC had?
    - Ze zouden de transactie niet kunnen aanmaken omdat "ontgrendelen" en "Ownership" hetzelfde zijn, en computers controleren of de transactie correct is ondertekend; anders wijzen ze het af
  - Wat als de willekeurig gekozen computer probeert "de Ledger te veranderen"?
    - De blokkade zou worden geweigerd, omdat elke andere computer een complete geschiedenis heeft en de verandering zou opmerken, wat een van hun regels schendt.
    - Random Computer zou geen beloning krijgen en er zouden geen transacties van hun blok worden afgerond.


## Kennisbeoordeling


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Discussie in de klas


Bespreek enkele oversimplificaties die gemaakt zijn in de klassikale oefening onder het tweede scenario en beschrijf wat het werkelijke Bitcoin systeem in meer detail doet.


### KA Woordenschat beoordeling


Definieer de volgende kernbegrippen die in het vorige hoofdstuk zijn geïntroduceerd:



- Knooppunt
- Mempool
- Moeilijkheidsdoel
- Blok


**Bespreek als groep de betekenis van enkele aanvullende termen:**


Blockchain, Transactie, Dubbele besteding, Byzantijns Generaalsprobleem, Mining, Proof of Work (PoW), Hash Functie, Block reward, Blockchain, Langste keten, 51%-aanval, Uitgang, Uitgangsslot, Verandering, Satoshis, Publieke/private sleutel, Address, Cryptografie met publieke sleutel, Digitale handtekening, Wallet


# Introductie van BTCPay Server


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Inlogscherm BTCPay-server begrijpen


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Werken met BTCPay Server


Het doel van dit cursusblok is om een algemeen begrip te krijgen van de BTCPay Server software. In een gedeelde omgeving, is het aanbevolen om de demonstratie van de instructeur te volgen en het BTCPay Server Coursebook te raadplegen om mee te volgen met de docent. U leert hoe u een Wallet kunt creëren via verschillende methoden. Voorbeelden zijn Hot Wallet setups en hardware wallets verbonden via BTCPay Server Vault. Deze doelstellingen komen voor in de Demo-omgeving, die wordt weergegeven en waartoe u toegang krijgt van uw cursusleider.


Als u deze cursus zelf volgt, kunt u een lijst van hosts van derden voor demo-doeleinden vinden op https://directory.btcpayserver.org/filter/hosts. We raden sterk af om deze opties van derden te gebruiken als productieomgevingen; ze dienen echter het juiste doel om het gebruik van Bitcoin en BTCPay Server te introduceren.


Als BTCPay Server rockstar trainee heb je misschien al ervaring met het opzetten van een Bitcoin node. Deze cursus is specifiek afgestemd op de BTCPay Server Software stack.


Veel van de opties in BTCPay Server bestaan al in een of andere vorm in andere Bitcoin Wallet-gerelateerde software.


### BTCPay server login scherm


Als je welkom wordt geheten in de Demo omgeving, wordt je gevraagd om 'Inloggen' of 'Maak je account aan' Server beheerders kunnen de functie van het creëren van nieuwe accounts uitschakelen om veiligheidsredenen. BTCPay Server logo's en knopkleuren kunnen worden veranderd omdat BTCPay Server Open Source Software is. Een derde partij host kan de software white-label en het hele uiterlijk veranderen.


![image](assets/en/001.webp)


### Venster Account aanmaken


Rekeningen aanmaken op de BTCPay Server vereist geldige Email Address strings; example@email.com zou een geldige string zijn voor Email.


Het wachtwoord moet minstens 8 tekens lang zijn, inclusief letters, cijfers en tekens. Nadat u het wachtwoord eenmaal hebt ingesteld, moet u controleren of het wachtwoord hetzelfde is als wat in het eerste wachtwoordveld is getypt.


Wanneer de Email en Password velden correct zijn ingevuld, klik dan op de 'Create Account' knop. Dit zal de e-mail en het wachtwoord opslaan op de BTCPay-serverinstantie van de instructeur.


![image](assets/en/002.webp)


**Let op!**


Als je deze cursus zelfstandig volgt, wordt het aanmaken van dit account waarschijnlijk gedaan op een host van een derde partij; daarom benadrukken we nogmaals dat deze niet moeten worden gebruikt als productieomgeving, maar alleen voor trainingsdoeleinden.


### Rekening aanmaken door BTCPay Server Administrator


De beheerder van de BTCPay Server Instance kan ook accounts aanmaken voor BTCPay Server. De beheerder van de BTCPay-serverinstantie kan klikken op 'Serverinstellingen' (1), klikken op de tab 'Gebruikers' (2) en klikken op de knop '+ Gebruiker toevoegen' (3) in de rechterbovenhoek van de tab 'Gebruikers'. In Objectief (4.3), zal u meer leren over de beheerderscontrole van Accounts.


![image](assets/en/003.webp)


Als beheerder heb je de e-mail Address van de gebruiker nodig en stel je een standaardwachtwoord in. Om veiligheidsredenen wordt aanbevolen dat de beheerder de gebruiker informeert om dit wachtwoord te wijzigen voordat het account wordt gebruikt. Als de beheerder geen wachtwoord instelt en SMTP is geconfigureerd op de server, ontvangt de gebruiker een e-mail met een uitnodigingslink om zelf een account aan te maken en een wachtwoord in te stellen.


### Voorbeeld


Als je de cursus volgt met een instructeur, volg dan de link van de instructeur en maak je account aan op de Demo omgeving. Zorg ervoor dat je e-mail Address en wachtwoord veilig zijn opgeslagen; je hebt deze inloggegevens nodig voor de rest van de demodoelen in deze cursus.


Het kan zijn dat je docent de e-mail Address van tevoren heeft verzameld en een uitnodigingslink heeft gestuurd voor deze oefening. Controleer je e-mail als dit wordt aangegeven.


Als u de cursus volgt zonder instructeur, maak dan uw account aan via de BTCPay Server demo-omgeving; ga naar


https://Mainnet.demo.btcpayserver.org/login.


Deze account mag alleen worden gebruikt voor demonstratie-/trainingsdoeleinden en nooit voor zakelijke doeleinden.


### Vaardigheden


In dit onderdeel heb je het volgende geleerd:



- Hoe maak je een account aan op een gehoste server via de Interface.
- Hoe een serverbeheerder handmatig gebruikers kan toevoegen in de serverinstellingen.


### Kennisbeoordeling


#### KA Conceptueel overzicht


Geef redenen waarom het gebruik van een Demo Server een slecht idee is voor productiedoeleinden.


## Gebruikersaccount(s) beheren


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Rekeningbeheer op de BTCPay-server


Nadat een winkeleigenaar zijn account heeft aangemaakt, kan hij deze beheren in de linkerbenedenhoek van de BTCPay Server UI. Onder de knop Account zijn er meerdere instellingen op hoger niveau.



- Donker/Licht-modus.
- Verberg gevoelige informatie.
- Account beheren.


![image](assets/en/004.webp)


### Modus Donker en Licht


Gebruikers van BTCPay Server kunnen kiezen tussen een Light of Dark mode versie van de UI. Klantgerichte pagina's veranderen niet. Zij gebruiken de door de klant gewenste instellingen met betrekking tot de donkere of lichte modus.


### Verberg gevoelige informatie Toggle


De Hide Sensitive Info knop biedt een snelle en eenvoudige Layer beveiliging. Wanneer u uw BTCPay Server moet bedienen, maar er kunnen mensen over uw schouder meekijken in een openbare ruimte, zet dan Hide Sensitive Info aan, en alle waarden in BTCPay Server zullen verborgen zijn. Men kan misschien over uw schouder meekijken, maar kan niet langer de waarden zien waarmee u bezig bent.


### Account beheren


Zodra de gebruikersaccount is aangemaakt, kun je hier wachtwoorden, 2FA of API-sleutels beheren.


### Account beheren - Account


Werk optioneel uw account bij met een andere E-mail Address. Om ervoor te zorgen dat uw e-mail Address correct is, kunt u met BTCPay Server een verificatie e-mail sturen. Klik op opslaan als de gebruiker een nieuwe e-mail Address instelt en bevestigt dat de verificatie werkte. De gebruikersnaam blijft hetzelfde als de vorige e-mail.


Een gebruiker kan beslissen om zijn hele account te verwijderen. Dit kan worden gedaan door op de knop Verwijderen te klikken op het tabblad Account.


![image](assets/en/005.webp)


**Let op!**


Na het wijzigen van het e-mailadres, verandert de gebruikersnaam voor het account niet. De eerder gegeven e-mail Address blijft de aanmeldnaam.


### Account beheren - Wachtwoord


Een leerling wil misschien zijn wachtwoord wijzigen. Hij kan dit doen door naar het tabblad Wachtwoord te gaan. Hier moet hij zijn oude wachtwoord intypen en kan hij het wijzigen in een nieuw wachtwoord.


![image](assets/en/006.webp)


### Authenticatie met twee factoren (2fa)


Om de gevolgen van een gestolen wachtwoord te beperken, kun je twee-factor authenticatie (2FA) gebruiken, een relatief nieuwe beveiligingsmethode. Je kunt twee-factor-authenticatie activeren via Account beheren en het tabblad voor twee-factor-authenticatie. Je moet een tweede stap doorlopen nadat je je hebt aangemeld met je gebruikersnaam en wachtwoord.


BTCPay Server ondersteunt twee methoden om 2FA in te schakelen: app-gebaseerde 2FA (Authy, Google, Microsoft Authenticators) of via beveiligingsapparaten (FIDO2 of LNURL Auth).


### Authenticatie met twee factoren - App-gebaseerd


Op basis van het besturingssysteem van je mobiele telefoon (Android of iOS) kunnen gebruikers kiezen uit de volgende apps;


1. Download een twee-factor authenticator.


   - Authy voor [Android](https://play.google.com/store/apps/details?id=com.authy.authy) of [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator voor [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) of [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator voor [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) of [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Na het downloaden en installeren van de Authenticator App.


   - Scan de QR Code voorzien door BTCPay Server
   - Of voer de gegenereerde sleutel door BTCPay Server handmatig in uw Authenticator app in.

3. De Authenticator app zal u voorzien van een unieke code. Voer de unieke code in BTCPay Server in om de setup te verifiëren en klik op verifiëren om het proces te voltooien.


![image](assets/en/007.webp)


### Vaardigheden


In dit onderdeel heb je het volgende geleerd:



- Opties voor accountbeheer en de verschillende manieren om een account te beheren op een BTCPay Server instance.
- Hoe app-gebaseerde 2FA instellen.


### Kennisbeoordeling


#### KA Conceptueel overzicht


Beschrijf hoe app-gebaseerde 2FA helpt om je account te beveiligen.


## Een nieuwe winkel maken


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Maak je winkelwizard


Wanneer een nieuwe gebruiker inlogt in BTCPay Server, is de omgeving leeg en heeft deze een eerste winkel nodig. De introductie wizard van BTCPay Server zal de gebruiker de optie geven om 'Maak uw winkel' (1). Een winkel kan worden gezien als een thuis voor uw Bitcoin behoeften. Een nieuwe BTCPay Server Node zal beginnen met het synchroniseren van de Bitcoin Blockchain (2). Afhankelijk van de infrastructuur waarop u BTCPay Server draait, kan dit variëren van een paar uur tot een paar dagen. De huidige versie van de instantie wordt weergegeven in de rechterbenedenhoek van uw BTCPay Server UI. Dit is handig als referentie bij het oplossen van problemen.


![image](assets/en/008.webp)


### Maak je winkelwizard


Het volgen van deze cursus begint met een iets ander scherm dan op de vorige pagina. Aangezien uw instructeur de Demo omgeving heeft voorbereid, is de Bitcoin Blockchain al eerder gesynchroniseerd, en daarom ziet u de synchronisatiestatus van de nodes niet.


Een gebruiker kan beslissen om zijn hele account te verwijderen. Dit kan worden gedaan door op de knop Verwijderen te klikken op het tabblad Account.


![image](assets/en/009.webp)


**Let op!**


BTCPay Server accounts kunnen een onbeperkt aantal winkels aanmaken. Elke winkel is een Wallet of "thuis".


### Voorbeeld


Klik eerst op "Maak je winkel".


![image](assets/en/010.webp)


Dit zal uw eerste Home en dashboard creëren voor het gebruik van BTCPay Server.


(1) Nadat u op "Creëer uw winkel" hebt geklikt, zal BTCPay Server u vragen om de winkel een naam te geven; dit kan om het even wat zijn.


![image](assets/en/011.webp)


(2) Vervolgens moet een standaard winkelvaluta worden ingesteld, ofwel een fiatvaluta of een valuta die in Bitcoin of Sats is uitgedrukt. Voor de demo-omgeving stellen we deze in op USD.


![image](assets/en/012.webp)


(3) Als laatste parameter bij het instellen van de winkel, vereist BTCPay Server dat u een "Voorkeur prijsbron" instelt om de prijs van Bitcoin te vergelijken met de huidige fiatprijs, zodat uw winkel de juiste Exchange koers weergeeft tussen Bitcoin en de door de winkel ingestelde fiatvaluta. We houden ons aan de standaard in het Demo-voorbeeld en stellen dit in op de Kraken Exchange. BTCPay Server gebruikt de Kraken API om de Exchange koersen te controleren.


![image](assets/en/013.webp)


(4) Nu deze winkelparameters zijn ingesteld, klikt u op de knop Aanmaken en BTCPay Server zal het dashboard van uw eerste winkel aanmaken, waar de wizard verder zal gaan.


![image](assets/en/014.webp)


Gefeliciteerd, je hebt je eerste winkel gemaakt en hiermee is deze oefening afgerond.


![image](assets/en/015.webp)


### Vaardigheden


In dit gedeelte heb je geleerd:



- Winkel aanmaken en een standaardvaluta configureren, gecombineerd met voorkeuren voor prijsbronnen.
- Elke "winkel" is een nieuwe thuis gescheiden van andere winkels op deze installatie van BTCPay Server.


# Inleiding tot het beveiligen van Bitcoin sleutels


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Inzicht in het genereren van Bitcoin sleutels


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Wat komt er kijken bij het genereren van Bitcoin sleutels?


Bitcoin portemonnees creëren een zogenaamde "seed". In het laatste doel heb je een "seed" aangemaakt. De reeks woorden die hiervoor gegenereerd zijn, worden ook wel Mnemonic zinnen genoemd. De seed wordt gebruikt om individuele Bitcoin Sleutels af te leiden en wordt gebruikt om Bitcoin te verzenden of te ontvangen. seed zinnen mogen nooit gedeeld worden met derden of niet-vertrouwde peers.


De seed generatie wordt uitgevoerd volgens de industriestandaard die bekend staat als het "Hierarchical Deterministic" (HD) raamwerk.


![image](assets/en/016.webp)


### Adressen


BTCPay Server is gebouwd om generate een nieuwe Address. Dit vermindert het probleem van hergebruik van publieke sleutels of Address. Het gebruik van dezelfde publieke sleutel maakt het volgen van uw gehele betalingsgeschiedenis erg gemakkelijk. Sleutels beschouwen als vouchers voor eenmalig gebruik zou uw privacy aanzienlijk verbeteren. We gebruiken ook Bitcoin adressen, verwar deze niet met publieke sleutels.


Een Address wordt via een "hashing algoritme" afgeleid van de publieke sleutel De meeste portemonnees en transacties zullen echter Adressen weergeven in plaats van die publieke sleutels. Adressen zijn over het algemeen korter dan publieke sleutels en beginnen meestal met een `1`, `3`, of `bc1`, terwijl publieke sleutels beginnen met `02`, `03`, of `04`.



- Adressen die beginnen met `1.....` zijn nog steeds veel voorkomende adressen. Zoals vermeld in het hoofdstuk "Een nieuwe winkel aanmaken", zijn dit oude adressen. Dit Address type is bedoeld voor P2PKH transacties. P2Pkh gebruikt Base58 codering, waardoor de Address hoofdlettergevoelig is. De structuur is gebaseerd op de publieke sleutel met een extra cijfer als identificatie.



- Adressen die beginnen met `bc1...` verhuizen langzaam naar de meest voorkomende adressen. Deze staan bekend als (native) SegWit adressen. Deze bieden een betere tariefstructuur dan de andere genoemde adressen. Native SegWit adressen gebruiken Bech32 codering en laten alleen kleine letters toe.



- Adressen die beginnen met `3...` worden vaak nog gebruikt door exchanges voor stortingsadressen. Deze adressen worden genoemd in het hoofdstuk "Een nieuwe winkel aanmaken", ingepakte of geneste SegWit adressen. Ze kunnen echter ook functioneren als een "Multisig Address". Bij gebruik als SegWit Address zijn er enige besparingen op transactiekosten, maar ook weer minder dan bij Native SegWit. P2SH Adressen gebruiken Base58 codering. Dit maakt het case Sensitive, net als het oude Address.



- Adressen die beginnen met `2...` zijn Testnet adressen. Ze zijn bedoeld om Testnet Bitcoin (tBTC) te ontvangen. Je mag dit nooit door elkaar halen en Bitcoin naar deze adressen sturen. Voor ontwikkelingsdoeleinden kun je generate een Testnet Wallet. Er zijn meerdere kranen online om Testnet Bitcoin te krijgen. Koop nooit Testnet Bitcoin. Testnet Bitcoin wordt gedolven. Dit kan een reden zijn voor een ontwikkelaar om in plaats daarvan Regtest te gebruiken. Dit is een speelomgeving voor ontwikkelaars, die bepaalde netwerkcomponenten mist. Bitcoin is echter zeer bruikbaar voor ontwikkelingsdoeleinden.


### Openbare sleutels


Publieke sleutels worden tegenwoordig in de praktijk minder vaak gebruikt. Na verloop van tijd hebben Bitcoin gebruikers ze vervangen door Adressen. Ze bestaan nog steeds en worden nog steeds af en toe gebruikt. Publieke sleutels zijn over het algemeen veel langere strings dan adressen. Net als bij adressen beginnen ze met een specifieke identificatie.



- Ten eerste, `02...` en `03...` zijn erg standaard publieke sleutel identifiers gecodeerd in SEC formaat. Deze kunnen verwerkt worden en omgezet worden in adressen voor ontvangst, gebruikt worden voor het aanmaken van multi-sig adressen, of om een handtekening te verifiëren. Vroeg-dag Bitcoin transacties gebruikten publieke sleutels als onderdeel van P2PK transacties.



- HD wallets gebruiken echter een andere structuur. `xpub...`, `ypub...` of `zpub...` worden uitgebreide publieke sleutels genoemd, of xpubs. Deze sleutels worden gebruikt om vele publieke sleutels af te leiden als onderdeel van de HD Wallet. Omdat je xpub de gegevens bevat van je hele geschiedenis, dus van transacties in het verleden en in de toekomst, moet je deze nooit delen met niet-vertrouwde partijen.


### Vaardigheden


In dit onderdeel heb je het volgende geleerd:



- De verschillen tussen adressen en openbare sleutels en de voordelen van het gebruik van adressen in plaats van openbare sleutels.


### Kennisbeoordeling


Beschrijf het voordeel van het gebruik van nieuwe adressen voor elke transactie in vergelijking met hergebruik van Address of openbare sleutelmethoden.


## Sleutels beveiligen met een Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Bitcoin sleutels opslaan


Na het genereren van een seed zin, vereist de lijst van 12 - 24 woorden gegenereerd in dit boek de juiste back-ups en beveiliging, omdat deze woorden de enige manier zijn om de toegang tot een Wallet te herstellen. De structuur van HD wallets en hoe het adressen deterministisch genereert door gebruik te maken van een enkele seed, betekent dat al je aangemaakte adressen gebackupt worden met deze ene lijst van Mnemonic woorden, die je seed of herstelzin vertegenwoordigt.


Houd uw herstelzin veilig. Als iemand toegang heeft, specifiek met kwade bedoelingen, kunnen ze je fondsen verplaatsen. De seed veilig bewaren, terwijl je ook onthoudt dat het wederzijds is. Er zijn verschillende methodes voor het opslaan van Bitcoin private sleutels, elk met zijn eigen voor- en nadelen, in termen van veiligheid, privacy, gemak en fysieke opslag. Vanwege het belang van de private sleutels zijn Bitcoin gebruikers geneigd om deze sleutels op te slaan en veilig te bewaren in "self-custody" in plaats van gebruik te maken van "custodial" diensten zoals banken. Afhankelijk van de gebruiker moeten ze een Cold opslagoplossing of een Hot Wallet gebruiken.


### Hot en Cold opslag van Bitcoin sleutels


Gewoonlijk worden Bitcoin portemonnees aangeduid in een Hot Wallet of een Cold Wallet. De meeste afwegingen liggen in gemak, gebruiksgemak en veiligheidsrisico's. Elk van deze methoden kan ook worden gezien in een bewaaroplossing. De afwegingen zijn hier echter meestal gebaseerd op beveiliging en privacy en vallen buiten het bestek van deze cursus.


### Hot Wallet


Hot wallets zijn de handigste manier van interactie met Bitcoin via mobiele, web- of desktopsoftware. De Wallet is altijd verbonden met het internet, waardoor gebruikers Bitcoin kunnen verzenden of ontvangen. Dit is echter ook de zwakte; omdat de Wallet altijd online is, is deze kwetsbaarder voor aanvallen van hackers of malware op uw apparaat. In BTCPay Server, slaan Hot wallets de private sleutels op in de instantie. Iedereen die toegang heeft tot uw BTCPay Server kan mogelijk geld stelen van deze Address als ze kwaadwillend zijn. Wanneer BTCPay Server draait in een gehoste omgeving, moet u dit altijd overwegen in uw beveiligingsprofiel en bij voorkeur geen Hot Wallet gebruiken in een dergelijk geval. Wanneer BTCPay Server is geïnstalleerd op hardware die uw eigendom is en door u is beveiligd, wordt het risicoprofiel aanzienlijk lager, maar het verdwijnt nooit helemaal.


### Cold Wallet


Particulieren verhuizen hun Bitcoin naar een Cold Wallet omdat deze de privésleutels kan isoleren van het internet, waardoor ze beschermd zijn tegen potentiële online bedreigingen. Het verwijderen van de internetverbinding vermindert het risico op malware, spyware en SIM-swaps. Cold opslag wordt verondersteld superieur te zijn aan Hot opslag voor veiligheid en autonomie, op voorwaarde dat er voldoende voorzorgsmaatregelen worden genomen om verlies van de Bitcoin private sleutels te voorkomen. Cold opslag is het meest geschikt voor grote hoeveelheden Bitcoin, die niet bedoeld zijn om vaak uitgegeven te worden vanwege de complexiteit van de Wallet opstelling.


Er zijn verschillende methodes om Bitcoin sleutels in Cold op te slaan, van papieren wallets tot brain wallets, hardware wallets of, vanaf het begin, een Wallet bestand. De meeste wallets gebruiken BIP 39 om generate de seed zin. Binnen de Bitcoin Core software is er echter nog geen consensus bereikt over het gebruik ervan. Bitcoin Core-software zal nog steeds generate een Wallet.dat-bestand aanmaken, dat je op een veilige offline locatie moet opslaan.


### Vaardigheden


In dit gedeelte heb je geleerd:



- De verschillen tussen Hot en Cold portemonnees wat betreft functionaliteit en hun afwegingen.


### Kennisbeoordeling Conceptuele beoordeling



- Wat is een Wallet?



- Wat is het verschil tussen Hot en Cold portemonnees?



- Beschrijf wat wordt bedoeld met "een Wallet genereren"?


## Uw Bitcoin-toetsen gebruiken


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay server Wallet


BTCPay Server bestaat uit de volgende standaard Wallet functies:



- Transacties
- Stuur
- Ontvang
- Opnieuw scannen
- Betalingen trekken
- Uitbetalingen
- PSBT
- Algemene instellingen


### Transacties


Beheerders kunnen de inkomende en uitgaande transacties voor de On-Chain Wallet die verbonden zijn met deze specifieke winkel zien in het transacties overzicht. Elke transactie heeft een onderscheid tussen de ontvangen en verzonden bedragen. Ontvangen is Green en uitgaande transacties zijn rood. In het BTCPay Server transactieweergave, zullen beheerders ook een set standaard labels zien.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Hoe verzenden


De verzendfunctie van de BTCPay-server verzendt transacties van uw BTCPay-server On-Chain Wallet. BTCPay Server staat meerdere manieren toe om uw transacties te ondertekenen om geld uit te geven. Een transactie kan worden ondertekend met;



- Hardware Wallet
- Portemonnees die PSBT ondersteunen
- HD-privésleutel of herstelzaden.
- Hot Wallet


#### Hardware Wallet


BTCPay Server heeft ingebouwde Hardware Wallet ondersteuning, waardoor u uw Hardware Wallet kunt gebruiken met BTCPay Vault zonder informatie te lekken naar apps of servers van derden. De Hardware Wallet integratie in BTCPay Server stelt u in staat om uw Hardware Wallet te importeren en inkomende fondsen uit te geven met een eenvoudige bevestiging op uw apparaat. Uw privésleutels verlaten nooit het apparaat en alle fondsen worden gevalideerd met uw Full node, zodat er geen gegevens lekken.


#### Ondertekenen met een Wallet ondersteunende PSBT


PSBT (Partially Signed Bitcoin Transactions) is een uitwisselingsformaat voor Bitcoin transacties die nog volledig ondertekend moeten worden. PSBT wordt ondersteund in BTCPay Server en kan ondertekend worden met compatibele hardware en software wallets.


De constructie van een volledig ondertekende Bitcoin transactie doorloopt de volgende stappen:



- Een PSBT wordt geconstrueerd met specifieke in- en uitgangen, maar geen handtekeningen
- De geëxporteerde PSBT kan worden geïmporteerd door een Wallet die dit formaat ondersteunt
- De transactiegegevens kunnen worden geïnspecteerd en ondertekend met de Wallet
- Het ondertekende PSBT bestand wordt geëxporteerd van de Wallet en geïmporteerd met de BTCPay Server
- BTCPay Server produceert de laatste Bitcoin transactie
- Je controleert het resultaat en zendt het uit naar het netwerk


#### Ondertekenen met HD Private Key of Mnemonic seed


Als u een Wallet hebt aangemaakt voordat u BTCPay Server hebt gebruikt, kunt u het geld uitgeven door uw private key in een geschikt veld in te voeren. Stel een juist "AccountKeyPath" in Wallet> Instellingen; anders kunt u niet uitgeven.


#### Ondertekenen met een Hot Wallet


Als je een nieuwe Wallet hebt aangemaakt bij het opzetten van je winkel en deze hebt ingeschakeld als Hot Wallet, zal deze automatisch de seed gebruiken die op een server is opgeslagen om te ondertekenen.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) is een Bitcoin protocolfunctie waarmee je een eerder uitgezonden transactie kunt vervangen (terwijl die nog onbevestigd is). Dit maakt het mogelijk om de vingerafdruk van een Wallet transactie willekeurig te maken of te vervangen door een hogere vergoeding om de transactie hoger in de wachtrij van bevestiging (Mining) prioriteit te plaatsen. Dit vervangt effectief de originele transactie, omdat de hogere vergoeding voorrang krijgt en zodra deze bevestigd is, wordt de originele transactie ongeldig (geen dubbele uitgave).


Druk op de knop "Geavanceerde instellingen" om de RBF opties te bekijken.


![image](assets/en/017.webp)



- Randomiseren voor meer privacy, maakt het mogelijk om de transactie automatisch te vervangen voor het randomiseren van de vingerafdruk van de transactie.
- Ja, transactie markeren voor RBF en expliciet vervangen (Niet standaard vervangen, alleen door invoer)
- Nee, sta niet toe dat de transactie wordt vervangen.


### Munt selectie


Muntselectie is een geavanceerde privacyverbeterende functie waarmee je munten kunt selecteren die je wilt uitgeven bij het maken van een transactie. Bijvoorbeeld betalen met munten die vers uit een samenvoegingsmix komen.


Munt selectie werkt van nature met de Wallet labels functie. Hiermee kun je inkomend geld labelen voor een soepeler Wallet beheer en besteding.


BTCPay Server ondersteunt BIP-329 voor labelbeheer. Als u overgaat van een Wallet die BIP-329 ondersteunt en labels heeft ingesteld, zal BTCPay Server deze automatisch herkennen en importeren. Bij het migreren van servers, kan deze informatie ook geëxporteerd en geïmporteerd worden in de nieuwe omgeving.


### Hoe ontvangen?


Wanneer u klikt op de ontvangst knop in BTCPay Server, genereert het een ongebruikte Address die kan worden gebruikt om betalingen te ontvangen. Beheerders kunnen ook generate een nieuwe Address door het creëren van een nieuwe "Invoice."


BTCPay Server zal u altijd vragen om generate de volgende beschikbare Address om hergebruik van Address te voorkomen. Na het klikken op "generate volgende beschikbare BTC Address," genereert BTCPay Server een nieuwe Address en QR. U kunt ook direct een Label op de Address instellen voor een beter beheer van uw adressen.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Opnieuw scannen


De Rescan-functie vertrouwt op Bitcoin Core 0.17.0's "Scantxoutset" om de huidige staat van de Blockchain (UTXO Set genoemd) te scannen op munten die behoren tot het geconfigureerde afleidingsschema. Een Wallet rescan pakt twee veel voorkomende problemen aan die BTCPay Server gebruikers vaak tegenkomen.


1. Gap limiet probleem - De meeste wallets van derden zijn light wallets die een node delen met veel gebruikers. Light en Full node-afhankelijke wallets beperken het aantal (meestal 20) adressen zonder saldo dat ze bijhouden op de Blockchain om prestatieproblemen te voorkomen. BTCPay Server genereert een nieuwe Address voor elke Invoice. Met het bovenstaande in gedachten, nadat BTCPay Server 20 opeenvolgende onbetaalde facturen heeft gegenereerd, stopt de externe Wallet met het ophalen van de transacties, ervan uitgaande dat er geen nieuwe transacties hebben plaatsgevonden. Je externe Wallet zal ze niet meer tonen als de facturen betaald zijn op de 21ste, 22ste, enz. Aan de andere kant, intern, volgt de BTCPay Server Wallet elke Address die het genereert, samen met een aanzienlijk hogere gap-limiet. Het is niet afhankelijk van een derde partij en kan altijd een correct saldo laten zien.

2. De gap-limiet oplossing - Als je [externe/bestaande Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) gap-limiet configuratie toestaat, is de eenvoudige oplossing om deze te verhogen. De meeste portemonnees staan dit echter niet toe. De enige wallets die op dit moment gap-limit configuratie ondersteunen waar wij van op de hoogte zijn, zijn Electrum, Wasabi en Sparrow wallet. Helaas zul je waarschijnlijk een probleem tegenkomen met veel andere wallets. Voor de beste gebruikerservaring en privacy, overweeg het gebruik van de interne Wallet van de BTCPay Server in plaats van externe wallets.


#### BTCPay Server gebruikt "mempoolfullrbf=1"


BTCPay Server gebruikt "mempoolfullrbf=1"; we hebben dit als standaard toegevoegd aan uw BTCPay Server setup. We hebben er echter ook een functie van gemaakt die u zelf kunt uitschakelen. Zonder "mempoolfullrbf=1", als een klant een betaling dubbel uitvoert met een transactie die geen RBF signaleert, zou de Handelaar dit pas weten na bevestiging.


Een beheerder kan deze instelling uitschakelen. Met de volgende string kunt u de standaardinstelling wijzigen.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### BTCPay server Wallet instellingen


Wallet instellingen binnen BTCPay Server geven een duidelijk en beknopt overzicht van de algemene instellingen van uw Wallet. Al deze instellingen zijn vooraf ingevuld als de Wallet is aangemaakt met BTCPay Server.


![image](assets/en/020.webp)


Wallet instellingen binnen BTCPay Server geven een duidelijk en beknopt overzicht van de algemene instellingen van uw Wallet. Al deze instellingen zijn vooraf ingevuld als de Wallet werd aangemaakt met BTCPay Server. De Wallet instellingen van BTCPay Server beginnen met de Wallet status. Is het een Watch-only of een Hot Wallet? Afhankelijk van het Wallet type, kunnen de acties variëren, inclusief het opnieuw scannen van de Wallet voor ontbrekende transacties, het verwijderen van oude transacties uit de geschiedenis, het registreren van de Wallet voor betaallinks, of het vervangen en verwijderen van de huidige Wallet die aan de winkel is gekoppeld. In de Wallet instellingen van BTCPay Server, kunnen beheerders een Label voor de Wallet instellen voor een beter Wallet beheer. Hier kan de beheerder ook het afleidingsschema, de rekeningsleutel (xpub), vingerafdruk en het sleutelpad zien. Betalingen in Wallet instellingen hebben slechts twee hoofdinstellingen. De betaling is ongeldig als de transactie niet binnen (ingestelde minuten) na het verlopen van Invoice bevestigd wordt. Beschouw de Invoice als bevestigd wanneer de betalingstransactie X aantal bevestigingen heeft. Beheerders kunnen ook een toggle instellen om aanbevolen kosten weer te geven op het betaalscherm of een handmatig bevestigingsdoel instellen in het aantal blokken.


![image](assets/en/021.webp)


**Let op!**


Als je deze cursus zelfstandig volgt, wordt het aanmaken van dit account waarschijnlijk gedaan op een host van een derde partij. Daarom raden we nogmaals aan om deze niet als productieomgeving te gebruiken, maar alleen voor trainingsdoeleinden.


### Voorbeeld


#### Een Bitcoin Wallet instellen in BTCPay Server


BTCPay Server biedt twee methoden voor het opzetten van een Wallet. De ene manier is om een bestaande Bitcoin Wallet te importeren. Het importeren kan gedaan worden door een Hardware Wallet aan te sluiten, een Wallet bestand te importeren, een Extended public key in te voeren, een Wallet QR code te scannen, of, het minst gunstige, een eerder aangemaakte Wallet herstel seed met de hand in te voeren. In BTCPay Server, is het ook mogelijk om een nieuwe Wallet te creëren. Er zijn twee mogelijke manieren om BTCPay Server te configureren bij het genereren van een nieuwe Wallet.


De Hot Wallet optie in BTCPay Server maakt functies zoals 'PayJoin' of 'Liquid' mogelijk. Er is echter een nadeel: de seed herstel die gegenereerd is voor deze Wallet zal opgeslagen worden op de server, waar iedereen met admin controle het kan ophalen. Aangezien je private sleutel is afgeleid van je herstel-seed, zou een kwaadwillende toegang kunnen krijgen tot je huidige en toekomstige fondsen!


Om dit risico in BTCPay Server te beperken, kan een beheerder de waarde in Serverinstellingen > Beleid > "Sta niet-admins toe om Hot wallets te creëren voor hun winkels" op "nee" zetten, aangezien dit de standaardwaarde is. Om de veiligheid van die Hot-portefeuilles te verbeteren, moet de serverbeheerder 2FA-authenticatie inschakelen op accounts die Hot-portefeuilles mogen hebben. Het opslaan van private sleutels op een publieke server is een gevaarlijke praktijk en brengt aanzienlijke risico's met zich mee. Sommige zijn vergelijkbaar met Lightning Network risico's (zie het volgende hoofdstuk voor Lightning Network risico's).


De tweede optie die BTCPay Server biedt bij het genereren van een nieuwe Wallet is het creëren van een Watch-only wallet. BTCPay Server zal uw private sleutels eenmaal generate. Nadat de gebruiker bevestigt zijn seed zin te hebben opgeschreven, zal BTCPay Server de private sleutels van de server wissen. Als resultaat heeft uw winkel nu een Watch-only wallet verbonden. Om de ontvangen fondsen uit te geven op uw Watch-only wallet, zie hoofdstuk Hoe te verzenden, ofwel door BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction) te gebruiken, of, het minst aanbevolen, handmatig uw seed zin te geven.


In het laatste deel heb je een nieuwe 'Store' aangemaakt. De installatiewizard gaat verder met de vraag om "Een Wallet op te zetten" of "Een Lightning-knooppunt op te zetten". In dit voorbeeld volg je het proces van de "Instellen van een Wallet" wizard (1).


![image](assets/en/022.webp)


Nadat u op "Een Wallet instellen" hebt geklikt, vraagt de wizard hoe u verder wilt gaan; BTCPay Server biedt nu de optie om een bestaande Bitcoin Wallet te verbinden met uw nieuwe winkel. Als u geen Wallet heeft, stelt BTCPay Server voor om een nieuwe aan te maken. Dit voorbeeld volgt de stappen voor "een nieuwe Wallet aanmaken" (2). Volg de stappen om te leren hoe je "een bestaande Wallet aansluit" (1).


![image](assets/en/023.webp)


**Let op!**


Als je deze cursus in een klaslokaal volgt, houd er dan rekening mee dat het huidige voorbeeld en de seed die we hebben gegenereerd alleen voor educatieve doeleinden zijn. Er mag nooit iets anders dan nodig zijn in de oefeningen op deze adressen.


(1) Ga verder met de "Nieuwe Wallet" wizard door op de knop "Een nieuwe Wallet aanmaken" te klikken.


![image](assets/en/024.webp)


(2) Nadat je op "Maak een nieuwe Wallet" hebt geklikt, geeft het volgende venster in de wizard de opties "Hot Wallet" en "Watch-only wallet" Als je met een instructeur meeloopt, is je omgeving een gedeelde Demo, en kun je alleen een Watch-only wallet aanmaken. Let op het verschil tussen de twee figuren hieronder. Als je in de Demo omgeving bent en de instructeur volgt, maak dan een "Watch-only wallet" aan en ga verder met de "Nieuwe Wallet" wizard.


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Ga verder met de nieuwe Wallet wizard en je bent nu in de sectie Creëer BTC Watch-only wallet. Hier moeten we het Wallet "Address type" instellen BTCPay Server laat u toe om uw voorkeurs Address type te kiezen; bij het schrijven van deze cursus, is het nog steeds aanbevolen om bech32 adressen te gebruiken. U kunt meer in detail leren over adressen in het eerste hoofdstuk van dit deel.



- SegWit (bech32)
  - Native SegWit adressen beginnen met `bc1q`.
  - Voorbeeld: `bc1qXXXXXXXXXXXXXXXXXX`
- Erfenis
  - Legacy-adressen zijn adressen die beginnen met het getal `1`.
  - Voorbeeld: `15e15hXXXXXXXXXXXXXX`
- Taproot (voor gevorderde gebruikers)
  - Taproot adressen beginnen met `bc1p`.
  - Voorbeeld: `bc1pXXXXXXXXXXXXXXXXXXXX`
- SegWit verpakt
  - SegWit ingepakte adressen beginnen met `3`.
  - Voorbeeld: `37BBXXXXXXXXXXX`


Kies SegWit (aanbevolen) als voorkeurstype Wallet Address.


![image](assets/en/027.webp)


(4) Bij het instellen van de parameter voor de Wallet, laat BTCPay Server de gebruikers toe om een optionele passphrase in te stellen via BIP39; zorg ervoor dat u uw wachtwoord bevestigt.


![image](assets/en/028.webp)


(5) Na het instellen van het Wallet type Address en eventueel het instellen van enkele geavanceerde opties, klik op Create, en BTCPay Server zal generate uw nieuwe Wallet. Merk op dat dit de laatste stap is voor het genereren van uw seed zin. Zorg ervoor dat u dit alleen doet in een omgeving waar iemand niet in staat is om de seed zin te stelen door naar uw scherm te kijken.


![image](assets/en/029.webp)


(6) In het volgende scherm van de wizard, toont BTCPay Server u de Recovery seed phrase voor uw nieuw gegenereerde Wallet; dit zijn de sleutels om uw Wallet te herstellen en transacties te ondertekenen. BTCPay Server genereert een seed zin van 12 woorden. Deze woorden zullen worden gewist van de server na dit setup scherm. Deze Wallet is specifiek een Watch-only wallet. Het is aan te raden om deze seed zin niet digitaal of fotografisch op te slaan. Gebruikers mogen alleen verder gaan in de wizard als ze actief erkennen dat ze hun seed zin hebben opgeschreven.


![image](assets/en/030.webp)


(7) Na het klikken op Klaar en het beveiligen van de nieuw gegenereerde Bitcoin seed zin, zal BTCPay Server uw winkel updaten met de bijgevoegde nieuwe Wallet en is klaar om betalingen te ontvangen. In de Gebruiker Interface, in het linker navigatiemenu, merk op hoe Bitcoin nu is gemarkeerd en geactiveerd onder Wallet.


![image](assets/en/031.webp)


### Voorbeeld: Een seed zin opschrijven


Dit is een bijzonder veilig moment om Bitcoin te gebruiken. Zoals eerder vermeld, mag alleen jij toegang hebben tot of kennis hebben van je seed zin. Aangezien je een instructeur en klas volgt, mag de seed die gegenereerd is alleen in deze cursus gebruikt worden. Te veel factoren, waaronder nieuwsgierige blikken van klasgenoten, onveilige systemen en andere, maken deze sleutels alleen educatief en onbetrouwbaar. De gegenereerde sleutels moeten echter wel bewaard worden voor cursusvoorbeelden.


De eerste methode die we in deze situatie zullen gebruiken, die ook de minst veilige is, is het opschrijven van de seed zin in de juiste volgorde. Een seed zinnenkaart is inbegrepen in het cursusmateriaal dat aan de student wordt gegeven of kan worden gevonden op de BTCPay Server GitHub. We zullen deze kaart gebruiken om de woorden op te schrijven die in de vorige stap zijn gegenereerd. Zorg ervoor dat je ze in de juiste volgorde opschrijft. Nadat je ze hebt opgeschreven, controleer je ze met wat de software heeft gegeven om er zeker van te zijn dat je ze in de juiste volgorde hebt opgeschreven. Als je ze hebt opgeschreven, klik dan op het selectievakje om aan te geven dat je de seed zin correct hebt opgeschreven.


### Voorbeeld: Een seed frase opslaan op een Hardware Wallet


In deze cursus behandelen we het opslaan van een seed frase op een Hardware Wallet. Het volgen van deze cursus met een instructeur kan soms zo'n apparaat bevatten. In de cursus is in het gidsmateriaal een lijst opgenomen van hardware wallets die geschikt zouden zijn voor deze oefening.


In dit voorbeeld gebruiken we BTCPay Server vault en een Blockstream Jade Hardware Wallet.


Je kunt ook een videogids volgen over het aansluiten van een Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Download BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Zorg ervoor dat u de juiste bestanden download voor uw specifieke systeem. Windows-gebruikers moeten het pakket [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe) downloaden, Mac-gebruikers moeten het pakket [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) downloaden en Linux-gebruikers moeten het pakket [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz) downloaden


Na de installatie van BTCPay Server Vault, start u de software door te klikken op het pictogram op uw bureaublad. Wanneer BTCPay Server Vault correct is geïnstalleerd en voor de eerste keer wordt opgestart, zal het toestemming vragen om te worden gebruikt met Web Applications. Het zal vragen om toegang te verlenen tot de specifieke BTCPay Server waarmee u werkt. Accepteer deze voorwaarden. BTCPay Server Vault zal nu zoeken naar het hardware-apparaat. Zodra het apparaat is gevonden, zal BTCPay Server herkennen dat Vault is gestart en uw apparaat heeft opgehaald.


**Let op!**


Geef uw SSH-sleutels of serverbeheeraccount aan niemand anders dan beheerders wanneer u een Hot Wallet gebruikt. Iedereen met toegang tot deze accounts heeft toegang tot de fondsen in de Hot Wallet.


### Vaardigheden


In dit onderdeel heb je het volgende geleerd:



- Het transactieoverzicht van de Bitcoin Wallet en zijn verschillende categorisaties.
- Er zijn verschillende opties beschikbaar bij het verzenden vanaf een Bitcoin Wallet, van hardware tot Hot wallets.
- Het probleem met de gap-limiet bij het gebruik van de meeste wallets en hoe dit te verhelpen.
- Hoe generate een nieuwe Bitcoin Wallet binnen BTCPay Server, inclusief het opslaan van de sleutels in een Hardware Wallet en het maken van een back-up van de herstelzin.


In deze doelstelling heb je geleerd hoe je generate een nieuwe Bitcoin Wallet binnen BTCPay Server kunt aanmaken. We zijn nog niet ingegaan op hoe je die sleutels beveiligt of gebruikt. In een kort overzicht van deze doelstelling, heb je geleerd hoe je de eerste winkel opzet. Je hebt geleerd hoe je generate een Bitcoin herstel seed zin moet maken.


### Kennisbeoordeling Praktijkbeoordeling


Beschrijf een methode om sleutels te genereren en een schema om ze te beveiligen, samen met de afwegingen/risico's van het beveiligingssysteem.


## BTCPay server Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Wanneer een server administrator een nieuwe BTCPay Server instantie voorziet, kunnen ze een Lightning Network implementatie opzetten, zoals LND, Core Lightning of Eclair; zie Deel BTCPay Server configureren voor meer gedetailleerde installatie-instructies.


Als u een klaslokaal volgt, werkt het verbinden van een Lightning knooppunt met uw BTCPay Server via een Custom knooppunt. Een gebruiker die geen serverbeheerder is op BTCPay Server zal standaard niet in staat zijn om het interne Lightning knooppunt te gebruiken. Dit is om de server eigenaar te beschermen tegen het verliezen van hun fondsen. Server beheerders kunnen een plugin installeren om toegang te verlenen tot hun Lightning node via LNBank; dit valt buiten het bereik van dit boek. Raadpleeg de officiële pluginpagina voor meer informatie over LNBank.


### Verbind intern knooppunt (serverbeheerder)


De Server Administrator kan de interne Lightning Node van BTCPay Server gebruiken. Ongeacht de Lightning implementatie, verbinding maken met de interne Lightning node is hetzelfde.


Ga naar een vorige setup store, en klik op de "Lightning" Wallet in het linker menu. BTCPay Server geeft twee instellingsmogelijkheden: het interne knooppunt gebruiken (standaard alleen serverbeheerder) of een aangepast knooppunt (externe verbinding). Server beheerders kunnen klikken op de "Gebruik interne node" optie. Er is geen verdere configuratie nodig. Klik op de knop "Opslaan" en zie de melding "BTC Lightning-knooppunt bijgewerkt". De winkel heeft nu met succes Lightning Network mogelijkheden.


### Verbind extern knooppunt (eigenaar servergebruiker/winkel)


Standaard mogen winkeleigenaars de Lightning Node van de serverbeheerder niet gebruiken. De verbinding moet worden gemaakt met een extern knooppunt, ofwel een knooppunt dat eigendom is van de winkeleigenaar voor het opzetten van een BTCPay Server, een LNBank plugin indien beschikbaar gemaakt door de serverbeheerder, of een custodian oplossing zoals Alby.


Ga naar een eerder ingestelde winkel en klik op "Lightning" onder wallets in het linkermenu. Omdat winkeleigenaren standaard geen gebruik mogen maken van het interne knooppunt, is deze optie grijs weergegeven. Het gebruik van een aangepast knooppunt is de enige optie die standaard beschikbaar is voor winkeleigenaren.


BTCPay Server vereist verbindingsinformatie; de kant-en-klare (of custodian) oplossing zal deze informatie leveren die specifiek is afgestemd op een Lightning-implementatie. Binnen de BTCPay Server kunnen winkeleigenaars de volgende verbindingen gebruiken;



- C-lightning via TCPofUnixdomainsocketverbinding.
- Bliksem opladen via HTTPS
- Eclair via HTTPS
- LND via de REST proxy
- LNDhub via de REST API


![image](assets/en/032.webp)


Klik op "test verbinding" om ervoor te zorgen dat je de verbindingsgegevens correct hebt ingevoerd. Nadat is bevestigd dat de verbinding goed is, klikt u op 'Opslaan', en BTCPay Server toont dat de winkel is bijgewerkt met een Lightning Node.


### Beheer interne Lightning-node LND (serverbeheerder)


Na het aansluiten van de interne Lightning Node, zullen serverbeheerders nieuwe tegels opmerken op het Dashboard, specifiek voor Lightning-informatie.



- Bliksem evenwicht
- BTC in kanalen
  - BTC openingskanalen
  - Lokaal saldo BTC
  - BTC saldo op afstand
  - BTC sluit kanalen
- BTC On-Chain
  - BTC bevestigd
  - BTC onbevestigd
  - BTC gereserveerd
- Bliksemdiensten
  - Rijd de bliksem (RTL).


Door te klikken op het Ride the Lightning-logo in de tegel "Lightning services" of op "Lightning" onder wallets in het linkermenu, kunnen serverbeheerders RTL bereiken voor het beheer van Lightning-knooppunten.


**Noot!**


Verbinding met interne Lightning Node mislukt - Als de interne verbinding mislukt, bevestig dan:


1. Het knooppunt Bitcoin On-Chain is volledig gesynchroniseerd

2. Het interne bliksemknooppunt is "Ingeschakeld" onder "Lightning" > "Instellingen" > "BTC Lightning-instellingen"


Als u geen verbinding kunt maken met uw Lightning-node, kunt u proberen uw server opnieuw op te starten of meer details lezen in de officiële documentatie van BTCPay Server; https://docs.btcpayserver.org/Troubleshooting/. U kunt geen Lightning-betalingen accepteren in uw winkel totdat uw Lightning-node "Online" verschijnt. Probeer uw Lightning verbinding te testen door te klikken op de "Public Node Info" link.


### Bliksem Wallet


Binnen de Lightning Wallet optie in de linker menubalk, zullen server beheerders gemakkelijk toegang vinden tot RTL, hun Publieke node Info, en Lightning instellingen specifiek voor hun BTCPay Server winkel.


#### Interne knooppuntinformatie


Serverbeheerders kunnen op de interne node-info klikken om hun serverstatus (Online/Offline) en verbindingsteken voor Clearnet of Tor te bekijken.


![image](assets/en/033.webp)


#### Verbinding wijzigen


Om het externe Lightning-knooppunt te wijzigen, ga je naar "Lightning-instellingen" en klik je op "Verbinding wijzigen" (naast "Openbare knooppuntinfo"). Hierdoor wordt de bestaande instelling gereset. Voer de nieuwe node-informatie in, klik op Opslaan en de winkel wordt bijgewerkt.


![image](assets/en/034.webp)


#### Diensten


Als de serverbeheerder besluit om meerdere diensten voor de Lightning-implementatie te installeren, dan worden ze hier vermeld. Met een standaard LND implementatie hebben beheerders Ride The Lightning (RTL) als standaard tool voor knooppuntbeheer.


#### BTC Lightning Wallet instellingen


Na het toevoegen van het Lightning-knooppunt aan de winkel in een eerdere stap, kunnen winkeleigenaren er nog steeds voor kiezen om het knooppunt voor hun winkel te deactiveren met behulp van de knop bovenaan de Lightning-instellingen.


![image](assets/en/035.webp)


#### Lightning Betalingsopties


Winkeliers kunnen de volgende parameters instellen om de Lightning-ervaring voor hun klanten te verbeteren.



- Bliksembetalingsbedragen in Satoshis weergeven.
- Voeg hop hints voor privékanalen toe aan de Lightning Invoice.
- On-Chain en Lightning betalings URL/QR codes samenvoegen bij het afrekenen.
- Stel een beschrijvingssjabloon in voor bliksemfacturen.


#### LNURL


Winkeliers kunnen ervoor kiezen om de LNURL wel of niet te gebruiken. Een Lightning Network URL, of LNURL, is een voorgestelde standaard voor interacties tussen Lightning Payer en begunstigde. Kort gezegd is een LNURL een bech32 gecodeerde URL voorafgegaan door LNURL. Van de Lightning Wallet wordt verwacht dat hij de URL decodeert, contact maakt met de URL en wacht op een JSON object met verdere instructies, met name een tag die het gedrag van de LNURL definieert.



- LNURL inschakelen
- LNURL Klassieke modus
  - Voor Wallet compatibiliteit, Bech32 gecodeerd (klassiek) vs cleartext URL (aankomend)
- Laat de begunstigde een opmerking doorgeven.


### Voorbeeld 1


#### Verbinding maken met Lightning met het interne knooppunt (beheerder)


Deze optie is alleen beschikbaar als je de beheerder van deze instantie bent of als de beheerder de standaardinstellingen heeft gewijzigd zodat gebruikers het interne bliksemknooppunt kunnen gebruiken.


Klik als beheerder op de Lightning Wallet in de linker menubalk. BTCPay Server zal u vragen om een van de twee opties voor het aansluiten van een Lightning Node te selecteren: een intern knooppunt of een aangepast extern knooppunt. Klik op "Gebruik intern knooppunt" en klik dan op "Opslaan"


#### Je Lightning-knooppunt beheren (RTL)


Na het verbinden met de interne Lightning node, zal BTCPay Server updaten en een melding tonen "BTC Lightning node updated", wat bevestigt dat u nu Lightning heeft verbonden met uw winkel.


Het beheren van het bliksemknooppunt is een taak voor de serverbeheerder. Dit houdt het volgende in:


- Transactie beheren
- Liquiditeit beheren
  - Inkomende liquiditeit
  - Uitgaande liquiditeit
- Managen van collega's en kanalen
  - Aangesloten collega's
  - Kanaalkosten
  - Kanaalstatus
- Regelmatig back-ups maken van de kanaaltoestanden.
- Routingrapporten controleren
- Je kunt ook diensten zoals Loop gebruiken.


Alle Lightning node management wordt standaard gedaan met RTL (ervan uitgaande dat je op een LND implementatie draait). Beheerders kunnen op hun Lightning Wallet in BTCPay Server klikken en een knop vinden om RTL te openen. Het hoofddashboard van BTCPay Server is nu bijgewerkt met de Lightning Network tegels, inclusief snelle toegang tot RTL.


### Voorbeeld 2


#### Maak verbinding met bliksem met Alby


Als u verbinding wilt maken met een beheerder zoals Alby, moeten winkeleigenaars eerst een account aanmaken en naar https://getalby.com/ gaan


![image](assets/en/036.webp)


Na het aanmaken van de Alby account, ga naar uw BTCPay Server store.


Stap 1: Klik op 'Een Lightning-knooppunt instellen' op het Dashboard of op 'Lightning' onder wallets.


![image](assets/en/037.webp)


Stap 2: Voer uw Wallet verbindingsgegevens in die u van Alby heeft gekregen. Klik op het Dashboard van Alby op Wallet. Hier vind je "Wallet Connection Credentials". Kopieer deze gegevens. Plak de referenties van Alby in het veld Verbindingsconfiguratie in BTCPay Server.


![image](assets/en/038.webp)


Stap 3: Na het verstrekken van de BTCPay Server met de verbindingsgegevens, klikt u op de knop "Verbinding testen" om ervoor te zorgen dat de verbinding goed werkt. Let op het bericht "Verbinding met bliksemknooppunt geslaagd" bovenaan uw scherm. Dit bevestigt dat alles werkt zoals verwacht.


![image](assets/en/039.webp)


Stap 4: Klik op "Opslaan" en je winkel is nu verbonden met een Lightning-knooppunt van Alby.


![image](assets/en/040.webp)


**Let op!**


Vertrouw nooit meer waarde toe aan een Lightning-bewaaroplossing dan je bereid bent te verliezen.


### Vaardigheden


In dit gedeelte heb je geleerd:



- Hoe sluit je een intern of extern Lightning-knooppunt aan?
- De inhoud en functie van verschillende bliksem-gerelateerde tegels in het Dashboard
- Hoe Lightning Wallet configureren met Voltage Surge of Alby


### Kennisbeoordeling Praktijkbeoordeling


Beschrijf enkele van de verschillende opties voor het aansluiten van een Lightning Wallet op uw winkel.


# BTCPay server Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Overzicht dashboard


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server is een modulair softwarepakket. Er zijn echter standaarden waaraan elke BTCPay Server moet voldoen, en deze standaarden zullen de interactie tussen de beheerder en gebruikers bepalen. Beginnend met het Dashboard. Het belangrijkste ingangspunt van elke BTCPay Server na het inloggen. Het Dashboard geeft een overzicht van de prestaties van uw winkel, het huidige saldo van de Wallet en de transacties van de laatste 7 dagen. Omdat het een modulaire weergave is, kunnen Plugins deze weergave in hun voordeel gebruiken en hun eigen tegels op het Dashboard maken. Voor deze cursus zullen we alleen standaard plugins en apps bespreken, samen met hun respectievelijke views, in BTCPay Server.


### Dashboard-tegels


Binnen de hoofdweergave van het BTCPay Server dashboard zijn een aantal standaard tegels beschikbaar. Deze tegels zijn ontworpen voor de winkeleigenaar of beheerder om hun winkel snel te beheren in één overzicht.



- Wallet balans
- Transactieactiviteit
- Lightning Balance (als Lightning is ingeschakeld in de winkel)
- Lightning Services (als Lightning is ingeschakeld in de winkel)
- Recente transacties.
- Recente facturen
- Huidige actieve crowdfunds
- Winkelprestaties / best verkopende artikelen.


### Wallet balans


De Wallet balanstegel geeft een snel overzicht van de fondsen en prestaties van je Wallet. Het kan worden bekeken in BTC of Fiat-valuta in een wekelijkse, maandelijkse of jaarlijkse grafiek.


![image](assets/en/041.webp)


### Transactieactiviteit


Naast de Wallet Balance tegel, toont BTCPay Server een snel overzicht van uitbetalingen in afwachting, het aantal transacties in de laatste 7 dagen, en of uw winkel terugbetalingen heeft uitgegeven. Als u op de knop Beheren klikt, komt u in het beheer voor uitbetalingen in afwachting (meer informatie over uitbetalingen in BTCPay Server - hoofdstuk Betalingen).


![image](assets/en/042.webp)


### Bliksem evenwicht


Dit is alleen zichtbaar wanneer Lightning is geactiveerd.


Wanneer de Administrator Lightning Network toegang heeft toegestaan, heeft het BTCPay Server dashboard nu een nieuwe tegel met uw Lightning node informatie. Hoeveel BTC er in kanalen zit, hoe dit lokaal of op afstand wordt gebalanceerd (inkomende of uitgaande liquiditeit), of kanalen worden gesloten of geopend, en hoeveel Bitcoin er wordt gehouden On-Chain op de lightning node.


![image](assets/en/043.webp)


### Bliksemdiensten


Dit is alleen zichtbaar wanneer de bliksem actief is.


Naast het zien van uw Lightning saldo op het BTCPay Server dashboard, zullen beheerders ook de tegel voor Lightning Services zien. Hier kunnen beheerders snelknoppen vinden voor tools die ze gebruiken om hun Lightning-node te beheren; Ride the Lightning is bijvoorbeeld een van de standaard tools met BTCPay Server voor het beheer van Lightning-node.


![image](assets/en/044.webp)


### Recente transacties


De tegel Recente transacties toont de meest recente transacties van uw winkel. Met één klik kan de beheerder van de BTCPay Server instance nu de laatste transactie zien en zien of er aandacht aan moet worden besteed.


![image](assets/en/045.webp)


### Recente facturen


De tegel Recente facturen toont de 6 laatste facturen die zijn gegenereerd door uw BTCPay Server, inclusief status en Invoice bedrag. De tegel bevat ook een "View all" knop om gemakkelijk toegang te krijgen tot het volledige Invoice overzicht.


![image](assets/en/046.webp)


### Point Of Sale en crowdfunds


Aangezien BTCPay Server een set standaard plugins of apps levert, zijn Point Of Sale en Crowdfund de twee belangrijkste plugins van BTCPay Server. Met elke winkel en Wallet, kan een BTCPay Server gebruiker generate zoveel Point Of Sales of Crowdfunds gebruiken als hij nodig acht. Elk zal een nieuwe dashboardtegel creëren die de prestaties van de plugins toont.


![image](assets/en/047.webp)


Let op het kleine verschil tussen een Point of Sale en Crowdfund tegel. De beheerder ziet de best verkochte items in de Verkooppunttegel. In de Crowdfund-tegel wordt dit Top Perks. Beide tegels hebben sneltoetsen om de respectievelijke app te beheren en recente facturen te bekijken die zijn aangemaakt door top items of top perks.


![image](assets/en/048.webp)


**Let op!**


Saldo grafieken en recente transacties zijn alleen beschikbaar voor On-Chain betaalmethoden. Informatie over Lightning Network saldi en transacties staat op de to-do lijst. Vanaf BTCPay Server Versie 1.6.0, zijn basis Lightning Network balansen beschikbaar.


### Vaardigheden


In dit onderdeel heb je het volgende geleerd:



- De kernlay-out van tegels op de hoofdpagina staat bekend als het Dashboard.
- Een basiskennis van de inhoud van elke tegel.


### Beoordeling van kennis


Maak een lijst van zoveel mogelijk tegels uit het Dashboard.


## BTCPay server - Winkelinstellingen


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


Binnen de BTCPay Server-software kennen we twee soorten instellingen. BTCPay Server Store-specifieke instellingen, de instellingen knop te vinden in de linker menubalk onder het Dashboard, en BTCPay Server instellingen, te vinden aan de onderkant van de menubalk, direct boven Account. De BTCPay Server-specifieke instellingen kunnen alleen worden bekeken door Serverbeheerders.


De winkelinstellingen bestaan uit vele tabbladen om elke set instellingen te categoriseren.



- Algemeen
- Tarieven
- Afrekenen
- Toegangsmunten
- Gebruikers
- Rollen
- Webhooks
- Uitbetalingsverwerkers
- E-mails
- Formulieren


### Algemeen


Op het tabblad Algemene instellingen kunnen winkeleigenaars hun merknaam en standaardinstellingen voor betalingen instellen. Bij de eerste installatie van de winkel is een winkelnaam opgegeven; deze wordt weergegeven in de Algemene instellingen onder Winkelnaam. Hier kan de winkeleigenaar ook instellen dat de website overeenkomt met de huisstijl en een winkel-ID opgeven die de beheerder kan herkennen in de database.


#### Branding


Aangezien BTCPay Server FOSS is, kan een winkeleigenaar de branding aanpassen aan zijn winkel. Stel de merkkleur in, sla de logo's van uw merk op en voeg aangepaste CSS toe voor openbare/klantgerichte pagina's (Facturen, Betalingsverzoeken, Pull-betalingen)


#### Betaling


In de betalingsinstellingen kunnen winkeleigenaars de standaardvaluta van hun winkel instellen (Bitcoin of een andere fiatvaluta).


#### Iedereen toestaan om facturen te maken


Deze instelling is bedoeld voor ontwikkelaars of bouwers bovenop BTCPay Server. Met deze instelling ingeschakeld voor uw winkel, staat het de buitenwereld toe om facturen te creëren op uw BTCPay Server instance.


#### Extra kosten (netwerkkosten) toevoegen aan facturen


Een functie binnen BTCPay om handelaren te beschermen tegen Dust aanvallen of klanten tegen hoge kosten in kosten later wanneer de handelaar een groot bedrag aan Bitcoin in één keer moet verplaatsen. Bijvoorbeeld, de klant creëerde een Invoice voor 20$ en betaalde deze gedeeltelijk, waarbij hij 20 keer 1$ betaalde tot de Invoice volledig betaald was. De handelaar heeft nu een grotere transactie, wat de Mining kosten verhoogt als de handelaar besluit om deze fondsen later te verplaatsen. BTCPay past standaard een extra netwerkkost toe op het totale Invoice bedrag om deze kost voor de handelaar te dekken wanneer de Invoice in meerdere transacties wordt betaald. BTCPay biedt verschillende opties om deze beschermingsfunctie aan te passen. U kunt een netwerkvergoeding toepassen:



- Alleen als de klant meer dan één betaling voor de Invoice doet (In het bovenstaande voorbeeld, als de klant een Invoice voor 20$ heeft gemaakt en 1$ heeft betaald, is de totale Invoice nu 19$ + de netwerkkosten. De netwerkvergoeding wordt toegepast na de eerste betaling)
- Bij elke betaling (inclusief de eerste betaling, in ons voorbeeld is het totaal meteen 20$ + netwerkkosten, zelfs bij de eerste betaling)
- Voeg nooit netwerkkosten toe (schakelt de netwerkkosten volledig uit)


Hoewel het bescherming biedt tegen Dust transacties, kan het ook een negatief effect hebben op bedrijven als het niet goed wordt gecommuniceerd. Klanten kunnen aanvullende vragen hebben en denken dat je hen te veel in rekening brengt.


#### Invoice vervalt als het volledige bedrag niet is betaald na?


De Invoice timer is standaard ingesteld op 15 minuten. De timer dient als een beschermingsmechanisme tegen volatiliteit, omdat het Bitcoin-bedrag wordt vergrendeld volgens de Bitcoin-naar-fiat Exchange-tarieven. Als de klant de Invoice niet binnen de vastgestelde periode betaalt, wordt de Invoice als vervallen beschouwd. De Invoice wordt als "betaald" beschouwd zodra de transactie zichtbaar is op de Blockchain (met nul bevestigingen), en is "compleet" wanneer het aantal bevestigingen is bereikt dat de verkoper heeft gedefinieerd (meestal 1-6). De timer is instelbaar per minuut.


#### Beschouw de Invoice als betaald, zelfs als het betaalde bedrag X% lager is dan verwacht?


Wanneer een klant een Exchange Wallet gebruikt om direct voor een Invoice te betalen, neemt de Exchange een kleine vergoeding. Dit betekent dat zo'n Invoice niet als volledig voltooid wordt beschouwd. De Invoice wordt gemarkeerd als "gedeeltelijk betaald". U kunt hier het percentage instellen als een merchant te weinig betaalde facturen wil accepteren.


### Tarieven


In BTCPay Server, wanneer een Invoice wordt gegenereerd, heeft het altijd de meest up-to-date en accurate Bitcoin-to-fiat prijs nodig. Bij het creëren van een nieuwe winkel in BTCPay Server, worden beheerders gevraagd om hun favoriete prijsbron in te stellen. Nadat de winkel is opgezet, kunnen winkeleigenaars hun prijsbron op elk moment wijzigen in dit tabblad.


#### Geavanceerde scripts voor tariefregels


Voornamelijk gebruikt door power users. Als deze optie is ingeschakeld, kunnen winkeleigenaars scripts maken voor prijsgedrag en het in rekening brengen van kosten aan hun klanten.


#### Testen


Een snelle testplaats voor je favoriete valutaparen. Deze functie bevat ook de mogelijkheid om standaard valutaparen te controleren via een REST-query.


### Afrekenen


Het tabblad Afrekenen begint met Invoice-specifieke instellingen en een standaard betaalmethode, en schakelt specifieke betaalmethoden in wanneer aan de ingestelde vereisten is voldaan.


#### Invoice instellingen


Standaard betaalmethoden. De BTCPay Server biedt in zijn standaardconfiguratie drie opties.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain & Lightning)


We kunnen parameters instellen voor onze winkel, waarbij een klant alleen interactie heeft met Lightning als de prijs lager is dan X bedrag, en andersom voor On-Chain transacties, als X groter is dan Y, altijd de On-Chain betaaloptie presenteren.


![image](assets/en/049.webp)


#### Kassa


Vanaf BTCPay Server release 1.7, werd een nieuwe Checkout Interface, Checkout V2, geïntroduceerd. Sinds release 1.9 werd gestandaardiseerd, kunnen beheerders en winkeleigenaars nog steeds de kassa instellen op de vorige release. Door gebruik te maken van de toggle "Gebruik de klassieke checkout", kan de winkeleigenaar de winkel terugzetten naar de vorige checkout ervaring. BTCPay Server heeft ook een selecte set voorinstellingen voor online handel of een in-store ervaring.


![image](assets/en/050.webp)


Wanneer een klant interageert met de winkel en een Invoice genereert, is er een verlooptijd voor de Invoice. Standaard stelt BTCPay Server dit in op 5 minuten, maar beheerders kunnen dit aanpassen aan hun voorkeur. De afrekenpagina kan verder worden aangepast door de volgende parameters aan te vinken:



- Vier de betaling door confetti te laten zien
- De koptekst van de winkel weergeven (naam en logo)
- Toon de knop "Betalen in Wallet
- On-Chain en off-chain betalingen URL/QR's samenvoegen
- Bliksembetalingsbedragen in Satoshis weergeven
- Automatische taaldetectie bij het afrekenen


![image](assets/en/051.webp)


Wanneer Automatisch de taal detecteren niet is ingesteld, zal BTCPay Server standaard Engels weergeven. De winkeleigenaar kan deze standaardtaal wijzigen in de taal van zijn voorkeur.


![image](assets/en/052.webp)


Klik op de vervolgkeuzelijst en winkeleigenaars kunnen een aangepaste HTML-titel instellen die wordt weergegeven op de afrekenpagina.


![image](assets/en/053.webp)


Om er zeker van te zijn dat klanten hun betaalmethode kennen, kan een winkeleigenaar expliciet instellen dat gebruikers bij het afrekenen altijd hun voorkeursbetaalmethode moeten kiezen. Zodra de Invoice is betaald, laat BTCPay Server de klant terugkeren naar de webwinkel. Winkeleigenaren kunnen instellen dat deze redirect automatisch wordt toegepast nadat de klant heeft betaald.


![image](assets/en/054.webp)


#### Openbare ontvangst


Binnen de instellingen voor openbare kassabonnen kan een winkeleigenaar de kassabonpagina's openbaar maken, zodat de betaallijst op de kassabonpagina wordt weergegeven en de QR-code voor de klant gemakkelijk toegankelijk is.


![image](assets/en/055.webp)


### Toegangsmunten


Toegangsmunten worden gebruikt voor het koppelen met bepaalde e-commerce-integraties of op maat gemaakte integraties.


![image](assets/en/056.webp)


### Gebruikers


Winkelgebruikers zijn waar de winkeleigenaar zijn medewerkers, hun accounts en toegang tot de winkel kan beheren. Nadat personeelsleden hun account hebben aangemaakt, kan de winkeleigenaar specifieke gebruikers toevoegen aan de winkel als gastgebruiker of eigenaar. Om de rol van de medewerker verder te definiëren, raadpleeg de volgende sectie "BTCPay Server Winkelinstellingen - Rollen"


![image](assets/en/057.webp)


### Rollen


Een winkeleigenaar vindt de standaardrollen van de gebruiker misschien niet belangrijk genoeg. In de instellingen voor aangepaste rollen kan een winkeleigenaar de exacte behoeften voor elke rol in zijn bedrijf definiëren.


(1) Om een nieuwe rol aan te maken, klik je op de knop "+ Rol toevoegen".


![image](assets/en/058.webp)


(2) Voer een rolnaam in, bijvoorbeeld "Kassier".


![image](assets/en/059.webp)


(3) Configureer de individuele rechten voor de rol.



- Pas je winkels aan.
- Beheer Exchange-accounts die aan je winkels zijn gekoppeld.
  - Exchange-accounts bekijken die aan uw winkels zijn gekoppeld.
- Beheer je pull-betalingen.
- Maak pull-betalingen.
  - Maak niet-goedgekeurde pull-betalingen aan.
- Facturen wijzigen.
  - Facturen bekijken.
  - Maak een Invoice.
  - Maak facturen aan vanuit de bliksemknooppunten die aan je winkels zijn gekoppeld.
- Bekijk je winkels.
  - Facturen bekijken.
  - Je betalingsverzoeken bekijken.
  - Wijzig de webhooks van winkels.
- Je betalingsverzoeken wijzigen.
  - Je betalingsverzoeken bekijken.
- Gebruik de bliksemknooppunten die bij je winkels horen.
  - Bekijk de bliksemfacturen die aan je winkels zijn gekoppeld.
  - Maak facturen aan vanuit de bliksemknooppunten die aan je winkels zijn gekoppeld.
- Stort geld op Exchange-rekeningen die aan uw winkels zijn gekoppeld.
- Geld opnemen van Exchange-rekeningen naar uw winkel.
- Verhandel geld op de Exchange rekeningen van je winkel.


Als de rol wordt aangemaakt, staat de naam vast en kan deze niet meer worden gewijzigd als de rol in de bewerkingsmodus staat.


![image](assets/en/060.webp)


### Webhooks


Binnen BTCPay Server is het redelijk eenvoudig om een nieuwe "Webhook" te maken. In de BTCPay Server Store-instellingen - tabblad Webhooks, kan een winkeleigenaar gemakkelijk een nieuwe webhook aanmaken door te klikken op de "+ Webhook aanmaken". Met webhooks kan BTCPay Server HTTP-gebeurtenissen met betrekking tot uw winkel naar andere servers of e-commerce-integraties sturen.


![image](assets/en/061.webp)


Je bent nu in de weergave voor het creëren van een Webhook. Zorg ervoor dat u uw Payload URL kent en plak deze in uw BTCPay Server. Terwijl je de payload URL hebt geplakt, wordt daaronder het webhook geheim weergegeven. Kopieer het webhook geheim en geef het op het eindpunt. Wanneer alles is ingesteld, kunt u in BTCPay Server overschakelen naar "Automatic redelivery" BTCPay Server zal proberen om elke mislukte levering opnieuw te leveren na 10 seconden, 1 minuut, en tot 6 keer na 10 minuten. U kunt schakelen tussen elke gebeurtenis of de gebeurtenissen specificeren voor uw behoeften. Zorg ervoor dat u de webhook inschakelt en klik op de knop "Webhook toevoegen" om het op te slaan.


![image](assets/en/062.webp)


Webhooks zijn niet bedoeld om compatibel te zijn met de Bitpay API. Er zijn twee afzonderlijke IPN's (in BitPay termen: "Instant Payment Notifications") in BTCPay Server.



- Webhookp
- Meldingen


Gebruik de URL Melding alleen als je facturen maakt via de Bitpay API.


### Uitbetalingsverwerkers


Payout processors werken samen met het Payouts concept in BTCPay Server. Een uitbetalings aggregator kan meerdere transacties bundelen en ze in één keer versturen. Met uitbetalingsverwerkers kan een winkeleigenaar de gebundelde uitbetalingen automatiseren. BTCPay Server biedt twee methoden van geautomatiseerde uitbetalingen: On-Chain en off-chain (LN).


De winkeleigenaar kan beide uitbetalingsverwerkers afzonderlijk aanklikken en configureren. Een winkeleigenaar wil de On-Chain-processor misschien maar één keer per X uur laten draaien, terwijl de off-chain-processor misschien om de paar minuten draait. Voor On-Chain kun je ook een doel instellen voor welk blok het moet worden opgenomen. Standaard is dit ingesteld op 1 (of het eerstvolgende beschikbare blok). Merk op dat het instellen van de off-chain uitbetalingsprocessor alleen de intervaltimer heeft en geen blokdoel. Lightning Network uitbetalingen zijn onmiddellijk.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Winkeliers kunnen de On-Chain-processor alleen configureren als ze een Hot Wallet op hun winkel hebben aangesloten.


![image](assets/en/065.webp)


Na het instellen van een Payout processor, kunt u deze snel verwijderen of wijzigen door terug te keren naar de Payout processor tab in BTCPay Server Store instellingen.


**Noot**


Uitbetalingsverwerker On-Chain - De On-Chain uitbetalingsverwerker kan enkel werken op een winkel die geconfigureerd is met een Hot Wallet aangesloten. Als er geen Hot Wallet is aangesloten, houdt de BTCPay Server de Wallet sleutels niet bij en zal hij uitbetalingen niet automatisch kunnen verwerken.


### E-mails


BTCPay Server kan e-mails gebruiken voor meldingen of, indien correct ingesteld, om accounts te herstellen die zijn aangemaakt op de instantie. Standaard stuurt BTCPay Server geen e-mail wanneer het wachtwoord bijvoorbeeld verloren is.


![image](assets/en/066.webp)


Voordat een winkeleigenaar e-mailregels kan instellen om specifieke gebeurtenissen in zijn winkel te triggeren, moet hij eerst een aantal basisinstellingen voor e-mail instellen. BTCPay Server heeft deze instellingen nodig om e-mails te sturen voor gebeurtenissen met betrekking tot uw winkel of voor het resetten van wachtwoorden.


BTCPay Server heeft het makkelijker gemaakt om deze informatie in te vullen door gebruik te maken van de "Quick Fill" Optie:



- Gmail.com
- Yahoo.nl
- Mailgun
- Kantoor365
- SendGrid


Door de quick fill optie te gebruiken, zal BTCPay Server de velden voor de SMTP server en poort vooraf invullen. Nu hoeft de winkeleigenaar enkel zijn referenties in te vullen, inclusief een Email Address, Login (wat meestal gelijk is aan uw email Address), en zijn wachtwoord. De geavanceerde optie in de BTCPay Server e-mail instellingen is om TLS Certificaat beveiligingscontroles uit te schakelen; standaard is dit ingeschakeld.


![image](assets/en/067.webp)


Met e-mailregels kan een winkeleigenaar specifieke gebeurtenissen instellen om e-mails naar specifieke e-mailadressen te triggeren.



- Invoice Gemaakt
- Invoice Betaling ontvangen
- Invoice Verwerking
- Invoice Vervallen
- Invoice Geregeld
- Invoice Ongeldig
- Invoice Betaling afgewikkeld


Als de klant een Address e-mail heeft opgegeven, kunnen deze triggers de informatie ook naar de klant sturen. Winkeliers kunnen de onderwerpregel vooraf invullen om duidelijk te maken waarom deze e-mail is verzonden en wat de trigger was.


![image](assets/en/068.webp)


### Formulieren


Aangezien BTCPay Server geen gegevens verzamelt, wil de winkeleigenaar misschien een aangepast formulier toevoegen aan zijn kassa-ervaring; op deze manier kan de winkeleigenaar extra informatie van zijn klant verzamelen. BTCPay Server Form builder bestaat uit twee delen: een visuele en een meer geavanceerde codeweergave van de formulieren.


Bij het creëren van een nieuw formulier, opent BTCPay Server een nieuw venster waarin basisinformatie wordt gevraagd over wat u wilt dat uw nieuwe formulier vraagt. Eerst moet de winkeleigenaar een duidelijke naam geven voor zijn nieuwe formulier; deze naam kan niet meer worden veranderd nadat hij is ingesteld.


![image](assets/en/069.webp)


Nadat de winkeleigenaar het formulier een naam heeft gegeven, kun je ook de schakelaar voor "Formulier toestaan voor publiek gebruik" op ON zetten, waarna het Green wordt. Dit zorgt ervoor dat het formulier op elke klantgerichte locatie wordt gebruikt. Als een winkeleigenaar bijvoorbeeld een apart Invoice formulier aanmaakt dat niet in zijn verkooppunt gebruikt wordt, wil hij misschien toch informatie van de klant verzamelen. Met deze schakelaar kan die informatie worden verzameld.


![image](assets/en/070.webp)


Elk formulier begint met minstens 1 nieuw formulierveld. Een winkeleigenaar kan kiezen welk type veld het moet worden.



- Tekst
- Aantal
- Wachtwoord
- E-mail
- URL
- Telefoonnummers
- Datum
- Verborgen velden
- Veldset
- Een tekstgebied voor open opmerkingen.
- Optiekeuzeknop


Elk type heeft zijn eigen parameters om in te vullen. De winkeleigenaar kan deze naar wens instellen. Onder het eerste veld kunnen winkeleigenaars nieuwe velden toevoegen aan dit formulier.


![image](assets/en/071.webp)


#### Geavanceerde aangepaste formulieren


Met BTCPay Server kunt u ook formulieren in code bouwen. JSON, in het bijzonder. In plaats van naar de editor te kijken, kunnen winkeleigenaars op de knop CODE naast de editor klikken en in de code van hun formulieren duiken. In een velddefinitie kunnen alleen de volgende velden worden ingesteld; de waarden van de velden worden opgeslagen in de metadata van de Invoice:


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

De veldnaam staat voor de JSON eigenschapsnaam die de door de gebruiker opgegeven waarde opslaat in de metadata van de Invoice. Sommige bekende namen kunnen worden geïnterpreteerd en aangepast om de instellingen van de Invoice aan te passen.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Je kunt de velden van een Invoice automatisch voorvullen door query strings toe te voegen aan de URL van het formulier, zoals "?your_field=value".


Hier zijn enkele gebruikssituaties voor deze functie:



- Gebruikersinvoer ondersteunen: Vul velden vooraf in met bekende klantgegevens om het invullen van het formulier te vergemakkelijken. Als u bijvoorbeeld het e-mailadres van een klant Address al weet, kunt u het e-mailveld al invullen om tijd te besparen.
- Personalisatie: Pas het formulier aan op basis van klantvoorkeuren of segmentatie. Als je bijvoorbeeld verschillende klantniveaus hebt, kun je het formulier vooraf vullen met relevante gegevens, zoals hun lidmaatschapsniveau of specifieke aanbiedingen.
- Volgen: Traceer de bron van klantbezoeken met behulp van verborgen velden en vooraf ingevulde waarden. U kunt bijvoorbeeld links maken met vooraf ingevulde utm_media-waarden voor elk marketingkanaal (bijv. Twitter, Facebook, E-mail). Dit helpt u bij het analyseren van de effectiviteit van uw marketinginspanningen.
- A/B-testen: Vul velden vooraf in met verschillende waarden om verschillende formulierversies te testen, zodat je de gebruikerservaring en conversiepercentages kunt optimaliseren.


### Vaardigheden


In dit onderdeel heb je het volgende geleerd:



- De indeling en functies van de tabbladen in de winkelinstellingen
- Een groot aantal opties voor het nauwkeurig afhandelen van onderliggende Exchange tarieven, gedeeltelijke betalingen, kleine onderbetalingen en meer.
- Pas het uiterlijk van de kassa aan, inclusief prijsafhankelijke hoofdketen versus Lightning-inschakeling op facturen.
- Beheer toegangs- en machtigingsniveaus voor verschillende rollen.
- Geautomatiseerde e-mails en hun triggers configureren
- Maak aangepaste formulieren om extra klantgegevens te verzamelen bij het afrekenen.


### Kennis Beoordelingen


#### KA-overzicht


Wat is het verschil tussen Store Settings en Server Settings?


#### KA Hypothetisch


Beschrijf enkele opties die je zou kunnen selecteren in Uiterlijk bij afrekenen > Invoice Instellingen, en waarom.


## BTCPay Server - Serverinstellingen


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server bestaat uit twee verschillende instellingsweergaven. De ene is gewijd aan winkelinstellingen en de andere aan serverinstellingen. De laatste is alleen beschikbaar voor serverbeheerders en niet voor winkeleigenaars. Serverbeheerders kunnen gebruikers toevoegen, aangepaste rollen creëren, de e-mailserver configureren, beleidslijnen instellen, onderhoudstaken uitvoeren, alle diensten controleren die aan BTCPay Server zijn gekoppeld, bestanden uploaden naar de server of logs controleren.


### Gebruikers


Zoals vermeld in het vorige deel, kunnen serverbeheerders gebruikers uitnodigen voor hun server door ze toe te voegen aan het tabblad Gebruikers.


### Serverwijde aangepaste rollen


BTCPay Server heeft twee soorten aangepaste rollen: winkelspecifieke aangepaste rollen en serverwijde aangepaste rollen in de instellingen van BTCPay Server. Beide hebben een gelijkaardige set van permissies, maar indien ingesteld via de BTCPay Server Instellingen - tabblad Rollen, zal de toegepaste rol server-breed zijn en van toepassing zijn op meerdere winkels. Merk op dat er een "Server-wide" tag is toegevoegd aan de aangepaste rollen in Server settings.


![image](assets/en/072.webp)


### Serverwijde aangepaste rollen


Serverwijde aangepaste rollen toestemmingen ingesteld;



- Pas je winkels aan.
- Beheer Exchange-accounts gekoppeld aan uw winkels.
  - Exchange-accounts bekijken die aan uw winkels zijn gekoppeld.
- Beheer je pull-betalingen.
- Maak pull-betalingen.
  - Maak niet-goedgekeurde pull-betalingen aan.
- Facturen wijzigen.
  - Facturen bekijken.
  - Maak een Invoice.
  - Maak facturen aan vanuit de bliksemknooppunten die aan je winkels zijn gekoppeld.
- Bekijk je winkels.
  - Facturen bekijken.
  - Je betalingsverzoeken bekijken.
  - Wijzig de webhooks van winkels.
- Je betalingsverzoeken wijzigen.
  - Je betalingsverzoeken bekijken.
- Gebruik de bliksemknooppunten die bij je winkels horen.
  - Bekijk de bliksemfacturen die aan je winkels zijn gekoppeld.
  - Maak facturen aan vanuit de bliksemknooppunten die aan je winkels zijn gekoppeld.
- Stort geld op Exchange-rekeningen die aan uw winkels zijn gekoppeld.
- Geld opnemen van Exchange rekeningen naar uw winkel.
- Verhandel geld op de Exchange-rekeningen van je winkel.


**Let op!**


Als de rol wordt aangemaakt, staat de naam vast en kan deze niet meer worden gewijzigd als de rol in de bewerkingsmodus staat.


### E-mail


De serverwijde e-mailinstellingen lijken op die in de winkelspecifieke e-mailinstellingen. Deze instelling behandelt echter niet alleen triggers voor winkels of beheerderslogs, maar ook triggers voor andere gebeurtenissen. Deze e-mailinstelling maakt ook wachtwoordherstel beschikbaar op BTCPay Server bij het inloggen. Het werkt op dezelfde manier als de winkel-specifieke instellingen; beheerders kunnen snel hun e-mail parameters invullen en hun e-mailgegevens invoeren, waardoor de server e-mails kan versturen.


![image](assets/en/073.webp)


### Beleid


BTCPay Server beleidsbeheerders kunnen verschillende instellingen instellen op onderwerpen zoals Bestaande gebruiker instellingen, Nieuwe gebruiker instellingen, Kennisgeving instellingen en Onderhoud instellingen. Deze zijn bedoeld voor het registreren van nieuwe gebruikers als beheerders of gewone gebruikers, of voor het verbergen van de BTCPay Server voor zoekmachines door het toe te voegen aan de header van uw server.


![image](assets/en/074.webp)


#### Bestaande gebruiker Instellingen


De opties die hier beschikbaar zijn, staan los van aangepaste rollen. Deze extra rechten kunnen een winkel of de eigenaar ervan kwetsbaar maken voor aanvallen. Beleidsregels die kunnen worden toegevoegd aan bestaande gebruikers:



- Sta niet-admins toe om het interne Lightning knooppunt te gebruiken in hun winkels.
  - Hierdoor kunnen winkeleigenaars het Lightning-knooppunt van de serverbeheerder gebruiken en dus ook zijn geld! Let op, dit is geen oplossing om toegang te geven tot Lightning.
- Sta niet-admins toe om Hot-portefeuilles aan te maken voor hun winkels.
  - Dit zou iedereen met een account op uw BTCPay Server instance toelaten om Hot-wallets te creëren en hun herstel seed op te slaan op de server van de beheerder. Dit zou de beheerder aansprakelijk kunnen maken voor het houden van fondsen van derden!
- Sta niet-admins toe om Hot-portefeuilles te importeren voor hun winkels.
  - Vergelijkbaar met het vorige onderwerp over het maken van Hot wallets, staat dit beleid het importeren van een Hot Wallet toe, met dezelfde gevaren die genoemd zijn in het onderdeel over het maken van Hot wallets.


![image](assets/en/075.webp)


#### Nieuwe gebruikersinstellingen


We kunnen een aantal belangrijke instellingen maken om nieuwe gebruikers op de server te beheren. We kunnen een bevestigingsmail instellen voor nieuwe registraties, het aanmaken van nieuwe gebruikers via het inlogscherm uitschakelen en de toegang voor niet-beheerders tot het aanmaken van gebruikers via de API beperken.



- Een bevestigingsmail voor registratie vereist.
  - De serverbeheerder moet een e-mailserver hebben ingesteld.
- Registratie van nieuwe gebruikers op de server uitschakelen
- Schakel de toegang van niet-admins tot het API-eindpunt voor het aanmaken van gebruikers uit.


Standaard heeft BTCPay Server "Nieuwe gebruikersregistratie op de server uitschakelen" aangezet en de toegang voor niet-admins tot de API endpoint voor het aanmaken van gebruikers uitgeschakeld. Dit is voor de veiligheid, zodat willekeurige mensen die uw BTCPay login tegenkomen geen accounts kunnen aanmaken.


![image](assets/en/076.webp)


#### Instellingen meldingen


![image](assets/en/077.webp)


#### Onderhoudsinstellingen


BTCPay Server is een Open Source project dat leeft op GitHub. Wanneer BTCPay Server een nieuwe versie van de software uitbrengt, kunnen beheerders worden geïnformeerd dat er een nieuwe versie beschikbaar is. Beheerders kunnen ook willen voorkomen dat zoekmachines (zoals Google, Yahoo en DuckDuckGo) het BTCPay Server domein indexeren. Aangezien BTCPay Server FOSS is, kunnen ontwikkelaars wereldwijd nieuwe functies creëren. BTCPay Server heeft een experimentele functie die, wanneer ingeschakeld, beheerders toestaat om functies te gebruiken die niet bedoeld zijn voor productie, maar eerder voor testdoeleinden.



- Controleer releases op GitHub en stel u op de hoogte wanneer er een nieuwe BTCPay Server-versie beschikbaar is.
- Ontmoedig zoekmachines om deze site te indexeren
- Experimentele functies inschakelen.


![image](assets/en/078.webp)


#### Plugins


BTCPay Server kan plugins toevoegen en zijn functies uitbreiden. De plugins worden standaard geladen vanuit de BTCPay Server plugin-bouwer repository. Een beheerder kan er echter voor kiezen om plugins in een Pre-release status te zien, en als de ontwikkelaar van de plugin het toestaat, kan de serverbeheerder nu bètaversies van plugins installeren.


![image](assets/en/079.webp)


##### Aanpassingsinstellingen


Een standaard BTCPay Server implementatie zal toegankelijk zijn via het domein dat werd ingesteld tijdens de installatie. Een serverbeheerder kan echter het hoofddomein opnieuw toewijzen en een van de gemaakte apps van een specifieke winkel weergeven. De server administrator kan ook specifieke domeinen toewijzen aan specifieke apps.



- De app weergeven op de root van de website
  - Geeft een lijst weer met mogelijke apps die op het hoofddomein kunnen worden weergegeven.


![image](assets/en/080.webp)



- Koppel specifieke domeinen aan specifieke apps.
  - Wanneer u klikt om een specifiek domein in te stellen voor specifieke apps, kan de beheerder zoveel domeinen instellen die naar specifieke apps wijzen als nodig is.


![image](assets/en/081.webp)


#### Blokverkenners


BTCPay Server wordt standaard geleverd met Mempool.space als Block explorer voor transacties. Wanneer BTCPay Server een nieuwe Invoice genereert en er een transactie aan gekoppeld is, kan de winkeleigenaar klikken om de transactie te openen. BTCPay Server zal standaard naar Mempool.space wijzen als een Block explorer; een serverbeheerder kan dit echter wijzigen in de optie van hun voorkeur.


![image](assets/en/082.webp)


### Diensten


Het tabblad "BTCPay Server instellingen: Services" tabblad is een overzicht van de componenten die uw BTCPay Server gebruikt. De diensten die uw BTCPay-server blootstelt kunnen variëren afhankelijk van de implementatiemethode.


Een BTCPay Server Administrator kan klikken op de "Zie informatie" achter elke dienst om deze te openen en specifieke instellingen in te stellen.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay stelt de GRPC-service van LND open voor gebruik van buitenaf; u vindt verbindingsinformatie in dit specifieke instellingenmenu; compatibele wallets staan hier vermeld. BTCPay Server biedt ook een QR-code voor verbinding, die kan worden gescand en toegepast in een mobiele Wallet.


Serverbeheerders kunnen meer details bekijken.



- Gegevens gastheer
- Gebruik van SSL
- Macaroon
- AdminMacaroon
- FactuurMacaroon
- Alleen-lezenMacaroon
- GRPC SSL-cijfersuite (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay stelt LND's REST service bloot voor externe consumptie; u vindt de verbindingsinformatie hier; compatibele wallets zijn hier opgesomd. Onder de compatibele wallets zijn Joule, Alby en ZeusLN. BTCPay Server biedt een QR-code voor verbinding, die kan worden gescand en toegepast in een compatibele Wallet.



- REST URI
- Macaroon
- AdminMacaroon
- FactuurMacaroon
- Alleen-lezenMacaroon


#### LND seed Back-up


De LND seed back-up is handig voor het herstellen van geld van uw LND Wallet in het geval van een servercorruptie. Aangezien het Lightning-knooppunt een Hot-Wallet is, kunt u de vertrouwelijke seed informatie op deze pagina vinden.


LND documenteert het herstelproces. Zie https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md voor documentatie.


#### Berijd de bliksem


Ride the Lightning is een Lightning node management tool gebouwd als Open Source software. BTCPay Server gebruikt RTL als de Lightning node management component in zijn stack. BTCPay Server beheerders kunnen RTL bereiken via de Server instellingen - Services tab of door te klikken op de Lightning Wallet.


#### Full node P2P


Serverbeheerders willen misschien hun Bitcoin knooppunt verbinden met een mobiele Wallet. Deze pagina geeft informatie over hoe u op afstand verbinding kunt maken met uw Full node via het P2P protocol. Bij het schrijven van deze cursus vermeldt BTCPay Server Blockstream Green en Wasabi wallets als compatibele wallets. BTCPay Server biedt een QR-code voor verbinding, die kan worden gescand en toegepast in een compatibele Wallet.


#### Full node RPC


Deze pagina geeft informatie om op afstand verbinding te maken met uw Full node via het RPC protocol.


#### SSH


SSH wordt gebruikt voor onderhoudsdoeleinden. BTCPay Server toont het initiële verbindingscommando om uw server te bereiken en SSH publieke sleutels die geautoriseerd zijn om verbinding te maken met uw server. Server beheerders kunnen SSH wijzigingen uitschakelen via de BTCPay Server UI.


#### Dynamisch DNS


Dynamic DNS laat u toe om een stabiele DNS naam te hebben die naar uw server wijst, zelfs als uw IP Address regelmatig verandert. Dit wordt aanbevolen als u BTCPay Server thuis host en een duidelijk domein wenst om toegang te krijgen tot uw Server.


Merk op dat u uw NAT en BTCPay Server installatie goed moet configureren om het HTTPS certificaat te krijgen.


### Thema


BTCPay Server wordt standaard geleverd met twee thema's: Lichte en Donkere modi. Deze kunnen worden omgeschakeld door te klikken op Account linksonder en te wisselen tussen Dark en Light thema. BTCPay Server beheerders kunnen hun eigen thema toevoegen door een aangepast CSS thema te voorzien.


Beheerders kunnen het Light/Dark-thema uitbreiden door hun eigen aangepaste CSS toe te voegen of door hun eigen thema als volledig aangepast in te stellen.


![image](assets/en/084.webp)


#### Server branding


Serverbeheerders kunnen de BTCPay Server branding veranderen door een serverbrede branding van uw bedrijf in te stellen. Aangezien BTCPay Server FOSS is, kunnen serverbeheerders de software white-label maken en het uiterlijk aanpassen aan hun bedrijf.


![image](assets/en/085.webp)


### Onderhoud


Als serverbeheerder verwachten uw gebruikers dat u goed voor de server zorgt. In het tabblad Onderhoud van BTCPay Server kan de beheerder een aantal essentiële onderhoudswerkzaamheden uitvoeren. Stel de domeinnaam in op de BTCPay Server instance, herstart of ruim de server op. Misschien wel het belangrijkste, updates uitvoeren.


BTCPay Server is een Open Source project en wordt regelmatig bijgewerkt. Elke nieuwe release wordt aangekondigd via uw BTCPay Server Kennisgevingen of op de officiële kanalen waarmee BTCPay Server communiceert.


![image](assets/en/086.webp)


#### Domeinnaam


Nadat BTCPay Server is ingesteld, wil een beheerder misschien zijn oorspronkelijke Domein wijzigen. In de Onderhoud tab, kan de beheerder het Domein veranderen. Na het klikken op bevestigen en het instellen van de juiste DNS records op het domein, update en herstart BTCPay Server om terug te keren naar het nieuwe domein.


![image](assets/en/087.webp)


#### Herstart


Herstart BTCPay Server en gerelateerde diensten.


![image](assets/en/088.webp)


#### Schoon


BTCPay Server draait met Docker componenten; met updates, kunnen er restjes van Docker images, temp bestanden, enz. zijn. Serverbeheerders kunnen ruimte vrijmaken door het Clean script uit te voeren.


![image](assets/en/089.webp)


#### Update


Het is de belangrijkste optie in de onderhoudstab. BTCPay Server is gebouwd door de gemeenschap en daarom zijn de updatecycli frequenter dan de meeste softwareproducten. Wanneer BTCPay Server een nieuwe release heeft, zullen beheerders op de hoogte worden gebracht in hun notificatiecentrum. Door te klikken op de update knop, zal BTCPay Server GitHub controleren voor de laatste release, de server updaten en opnieuw opstarten. Alvorens bij te werken, wordt serverbeheerders altijd aangeraden om de release notes te lezen die via de officiële kanalen van BTCPay Server worden verspreid.


![image](assets/en/090.webp)


### Logboeken


Een probleem is nooit leuk. Dit document geeft een overzicht van de meest voorkomende workflow en stappen om je probleem efficiënt te identificeren en op te lossen, zelfstandig of met hulp van de community.


Het probleem identificeren is cruciaal.


#### Het probleem repliceren


Probeer eerst en vooral te bepalen wanneer het probleem zich voordoet. Probeer het probleem te reproduceren. Probeer uw server bij te werken en opnieuw op te starten om te controleren of u het probleem kunt reproduceren. Als dit het probleem beter beschrijft, maak dan een schermafbeelding.


##### De server bijwerken


Controleer uw versie van BTCPay Server als deze veel ouder is dan de [laatste versie](https://github.com/btcpayserver/btcpayserver/releases) van BTCPay Server. Het updaten van uw server kan het probleem oplossen.


##### De server opnieuw opstarten


Het herstarten van uw server is een gemakkelijke manier om veel van de meest voorkomende BTCPay Server problemen op te lossen. Het kan zijn dat je moet SSH-en naar je server om hem opnieuw op te starten.


##### Een service herstarten


Het is mogelijk dat u enkel een bepaalde dienst in uw BTCPay Server implementatie moet herstarten voor sommige problemen, zoals het herstarten van de letsencrypt container om het SSL certificaat te vernieuwen.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Gebruik docker ps om de naam te vinden van een andere service die je opnieuw wilt starten.


#### In de logboeken kijken


Logboeken kunnen een essentieel stuk informatie verschaffen. In de volgende paragrafen zullen we beschrijven hoe u de loginformatie voor verschillende onderdelen van BTCPay kunt verkrijgen.


##### BTCPay Logboeken


Sinds v1.0.3.8 hebt u gemakkelijk toegang tot de BTCPay serverlogs vanaf de frontend. Als je een serverbeheerder bent, ga dan naar Serverinstellingen > Logs en open het logbestand. Als je niet weet wat een bepaalde fout in de logs betekent, vermeld het dan bij het oplossen van problemen.


Als u meer gedetailleerde logs wilt en een Docker-implementatie gebruikt, kunt u logs van specifieke Docker-containers bekijken via de opdrachtregel. Zie deze [instructies om te ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) in een instantie van BTCPay die draait op een VPS.


Op de volgende pagina, een algemene lijst van de containernamen die worden gebruikt voor BTCPay Server.


Voer de onderstaande commando's uit om logs op containernaam af te drukken. Vervang de containernaam om andere containerlogs te bekijken.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Er zijn een paar manieren om toegang te krijgen tot uw LND logs als u Docker gebruikt. Log eerst in als root:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Je kunt ook snel logs afdrukken door de container-ID te gebruiken (alleen de eerste unieke ID-tekens zijn nodig, zoals de twee tekens die het verst naar links staan):


```bash
docker logs 'add your container ID'
```


Als je om wat voor reden dan ook meer logboeken nodig hebt


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


U ziet iets als


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Om ongecomprimeerde logs van die logs te openen, doe je `cat LND.log` of als je een andere wilt, gebruik je `cat LND.log.15`.


Om gecomprimeerde logs in `.gzip` te openen, gebruik je `gzip -d LND.log.16.gz` (in dit geval openen we `LND.log.16.gz`). Dit zou je een nieuw bestand moeten geven, waar je `cat LND.log.16` kunt doen. Als het bovenstaande niet werkt, moet je misschien eerst gzip installeren met `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Je kunt ook dit gebruiken:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Je kunt ook loginformatie opvragen met het c-lightning CLI commando.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin knooppuntlogboeken


Naast [logs bekijken](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) van uw bitcoind container, kunt u ook gebruik maken van de [bitcoin-cli commando's](https://developer.Bitcoin.org/reference/RPC/index.html)


[(opent nieuw venster)](https://developer.Bitcoin.org/reference/RPC/index.html) om informatie te verkrijgen van uw Bitcoin knooppunt. BTCPay bevat een script waarmee u gemakkelijk kunt communiceren met uw Bitcoin knooppunt.


Haal in de map btcpayserver-docker de Blockchain informatie op met je knooppunt:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Bestanden


BTCPay Server heeft een lokaal bestandssysteem, waardoor het mogelijk is om winkel (product) activa, logo's en branding rechtstreeks naar de server te uploaden. Het bestandssysteem van de server is alleen toegankelijk voor Server Administrators; winkeleigenaars kunnen hun logo's of branding uploaden op winkelniveau.


Wanneer de serverbeheerder zich op het tabblad Bestandsopslag bevindt, is het mogelijk om direct te uploaden naar je server of de bestandsopslagprovider te wijzigen in een lokaal bestandssysteem of Azure Blob Storage.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Vaardigheden


In dit onderdeel heb je het volgende geleerd:



- Het verschil tussen Store- en Server-instellingen, in het bijzonder met betrekking tot Gebruikers, Rollen en E-mails
- Stel serverbreed beleid in voor Lightning of Bitcoin Hot Wallet gebruik en aanmaken, registratie van nieuwe gebruikers en e-mailmeldingen.
- Hoe aangepaste thema's toe te voegen (in plaats van de eenvoudige licht/donker-opties) en aangepaste logo's te maken
- Eenvoudige onderhoudstaken voor de server uitvoeren via de meegeleverde GUI
- Problemen oplossen, waaronder het ophalen van details voor een van de Docker-containers of je knooppunt
- Bestandsopslag beheren


### Kennisbeoordeling


#### KA Conceptueel overzicht


Wat is het verschil tussen Rollen die worden toegewezen via Server- en Store-instellingen en wat is een mogelijk nut van de een ten opzichte van de ander?


#### KA Praktijkoverzicht


Beschrijf enkele mogelijke gebruikssituaties die zijn ingeschakeld op het tabblad Policies.


#### KA Praktijkoverzicht


Beschrijf enkele acties die een beheerder routinematig kan uitvoeren op het tabblad Onderhoud.


## BTCPay Server - Betalingen


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Een Invoice is een document dat de verkoper afgeeft aan een koper om de betaling te innen.


In BTCPay Server vertegenwoordigt een Invoice een document dat moet worden betaald binnen een bepaald tijdsinterval tegen een vaste Exchange koers. Facturen hebben een vervaldatum omdat ze de Exchange koers vastzetten binnen een bepaalde tijd, waardoor de ontvanger beschermd wordt tegen prijsschommelingen.


De kern van BTCPay Server is de mogelijkheid om op te treden als een Bitcoin Invoice beheersysteem. Een Invoice is een essentieel hulpmiddel voor het bijhouden en beheren van ontvangen betalingen.


Tenzij u een ingebouwde [Wallet] (https://docs.btcpayserver.org/Wallet/) gebruikt om handmatig betalingen te ontvangen, worden alle betalingen binnen een winkel getoond op de Facturen pagina. Deze pagina sorteert betalingen cumulatief op datum en dient als een centrale bron voor Invoice beheer en het oplossen van betalingsproblemen.


![image](assets/en/093.webp)


### Algemeen


#### Invoice statussen


In de onderstaande tabel worden de standaard Invoice statussen in BTCPay opgesomd en beschreven, samen met de voorgestelde veelvoorkomende acties. Acties zijn slechts aanbevelingen. Het is aan gebruikers om te bepalen wat de beste actie is voor hun gebruik en bedrijf.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Invoice details


De Invoice detailpagina bevat alle informatie met betrekking tot een Invoice.


Invoice informatie wordt automatisch aangemaakt op basis van Invoice status, Exchange tarief, enz. Productinformatie wordt automatisch aangemaakt als de Invoice is aangemaakt met productinformatie, zoals in de Point of Sale app.


#### Invoice filteren


Facturen kunnen worden gefilterd via de snelfilters naast de zoekknop of de geavanceerde filters, die kunnen worden geselecteerd door op de link (Help) bovenaan te klikken. Gebruikers kunnen facturen filteren op winkel, order-ID, artikel-ID, status of datum.


#### Invoice export


BTCPay Server Facturen kunnen worden geëxporteerd in CSV of JSON formaat. Voor meer informatie over Invoice export en boekhouding.


#### Terugbetaling van een Invoice


Als je om wat voor reden dan ook een terugbetaling wilt doen, kun je gemakkelijk een terugbetaling aanmaken vanuit het Invoice overzicht.


#### Facturen archiveren


Als gevolg van de geen Address hergebruik functie van BTCPay Server, is het gebruikelijk om veel verlopen facturen te zien op de Invoice pagina van uw winkel. Om ze te verbergen, selecteert u ze in de lijst en markeert u ze als gearchiveerd. Facturen die als gearchiveerd zijn gemarkeerd, worden niet verwijderd. Betaling op een gearchiveerde Invoice zal nog steeds gedetecteerd worden door uw BTCPay Server (paidLate status). U kunt de gearchiveerde facturen van de winkel op elk gewenst moment bekijken door gearchiveerde facturen te selecteren in de zoekfilter dropdown.


#### Standaardvaluta


De standaardvaluta van de winkel, die werd ingesteld tijdens de wizard voor het aanmaken van de winkel.


#### Iedereen toestaan om een Invoice aan te maken


Je moet deze optie inschakelen als je wilt dat de buitenwereld facturen kan maken in je winkel. Deze optie is alleen handig als je de betaalknop gebruikt of als je facturen uitgeeft via API of een HTML-website van derden. De PoS-app is vooraf geautoriseerd en vereist niet dat deze instelling is ingeschakeld voor een willekeurige bezoeker om je POS-winkel te openen en een Invoice aan te maken.


#### Extra kosten (netwerkkosten) toevoegen aan de Invoice



- Alleen als de klant meer dan één betaling doet voor de Invoice
- Bij elke betaling
- Voeg nooit netwerkkosten toe


#### Invoice vervalt als het volledige bedrag niet is betaald na ... Minuten.


De Invoice timer is standaard ingesteld op 15 minuten. De timer dient als een beschermingsmechanisme tegen volatiliteit, omdat het cryptocurrency bedrag wordt vergrendeld op basis van de crypto-to-fiat tarieven. Als de klant de Invoice niet binnen de vastgestelde periode betaalt, wordt de Invoice als vervallen beschouwd. De Invoice wordt als "betaald" beschouwd zodra de transactie zichtbaar is op de Blockchain (met nul bevestigingen), en wordt als "compleet" beschouwd wanneer het het aantal bevestigingen heeft bereikt dat de handelaar heeft gedefinieerd (meestal 1-6). De timer is aanpasbaar.


#### Beschouw de Invoice als betaald, zelfs als het betaalde bedrag ..% lager is dan verwacht.


In een situatie waarin een klant een Exchange Wallet gebruikt om direct voor een Invoice te betalen, neemt de Exchange een kleine vergoeding. Dit betekent dat zo'n Invoice niet als volledig voltooid wordt beschouwd. De Invoice wordt gemarkeerd als "gedeeltelijk betaald" Als een merchant te weinig betaalde facturen wil accepteren, kun je hier het percentage instellen


### Verzoeken


Betalingsverzoeken zijn een functie waarmee BTCPay-winkeliers facturen met een lange levensduur kunnen aanmaken. Fondsen worden betaald volgens het betalingsverzoek met behulp van de Exchange koers die van kracht is op het moment van betaling. Dit stelt gebruikers in staat om betalingen te doen wanneer het hen uitkomt, zonder te hoeven onderhandelen of de Exchange tarieven te verifiëren met de winkeleigenaar op het moment van betaling.


Gebruikers kunnen verzoeken in gedeeltelijke betalingen betalen. Het betalingsverzoek blijft geldig totdat het volledig is betaald of als de winkeleigenaar een verlooptijd vereist. Adressen worden nooit hergebruikt. Een nieuwe Address wordt gegenereerd elke keer als de gebruiker op betalen klikt om een Invoice aan te maken voor het betalingsverzoek.


Winkeliers kunnen betalingsverzoeken afdrukken (of Invoice gegevens exporteren) voor het bijhouden van gegevens en de boekhouding. BTCPay labelt facturen automatisch als betalingsverzoeken in de Invoice-lijst van uw winkel.


#### Uw betalingsverzoeken aanpassen



- Invoice Bedrag - Stel gevraagd betalingsbedrag in
- Denominatie - Toon Aangevraagde Bedrag in Fiat of Cryptocurrency
- Betalingsaantal - Alleen afzonderlijke betalingen of gedeeltelijke betalingen toestaan
- Vervaldatum - Betalingen toestaan tot een datum of zonder vervaldatum
- Beschrijving - Teksteditor, gegevenstabellen, foto's en video's insluiten
- Uiterlijk - Kleur en stijl met CSS-thema's


![image](assets/en/094.webp)


#### Een betalingsverzoek maken


Ga in het linkermenu naar Betalingsverzoek en klik op "Betalingsverzoek aanmaken".


![image](assets/en/095.webp)


Geef de naam van het verzoek, het bedrag, de denominatie, de bijbehorende winkel, de vervaltijd en de beschrijving (optioneel)


Selecteer de optie Laat begunstigde facturen maken in hun denominatie als je gedeeltelijke betalingen wilt toestaan.


Klik op Opslaan & bekijken om je betalingsverzoek te bekijken.


BTCPay creëert een URL voor het betalingsverzoek. Deel deze URL om uw betalingsverzoek te bekijken. Meerdere van dezelfde aanvragen nodig? U kunt betalingsverzoeken dupliceren met de kloonoptie in het hoofdmenu.


![image](assets/en/096.webp)


**WAARSCHUWING**


Betalingsverzoeken zijn winkelafhankelijk, wat betekent dat elk betalingsverzoek tijdens het aanmaken aan een winkel wordt gekoppeld. Zorg ervoor dat er een Wallet is verbonden met de winkel waar het betaalverzoek bij hoort.


#### Betaald verzoek


De begunstigde en de aanvrager kunnen de status van het betalingsverzoek bekijken nadat de betaling is verzonden. De status verschijnt als Geregeld als de betaling volledig is ontvangen. Als er slechts gedeeltelijke betalingen zijn gedaan, geeft het Verschuldigde bedrag het resterende saldo weer.


![image](assets/en/097.webp)


#### Betalingsverzoeken aanpassen


De inhoud van de beschrijving kan worden bewerkt met de teksteditor van het betalingsverzoek. Beide opties zijn beschikbaar als je extra kleurenthema's of aangepaste CSS-styling wilt gebruiken.


Niet-technische gebruikers kunnen een [bootstrap theme] (https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes) gebruiken. Verdere aanpassingen kunnen worden gedaan door extra CSS-code op te geven, zoals hieronder wordt getoond.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Betalingen trekken


Traditioneel deelt een ontvanger zijn Bitcoin Address om een Bitcoin betaling te doen, en de verzender stuurt later geld naar deze Address. Een dergelijk systeem wordt een Push-betaling genoemd, omdat de verzender de betaling initieert terwijl de ontvanger mogelijk niet beschikbaar is en de betaling naar de ontvanger pusht.


Maar hoe zit het met het omdraaien van de rol?


Wat als de verzender de betaling niet pusht, maar de ontvanger toestaat om de betaling te ontvangen op een moment dat de ontvanger goeddunkt? Dit is het concept van een Pull-betaling. Dit maakt verschillende nieuwe toepassingen mogelijk, zoals:



- Een abonnementsdienst (waarbij de abonnee de dienst toestaat om elke x hoeveelheid tijd geld op te nemen)
- Restituties (waarbij de winkelier de klant toestaat om het restitutiegeld naar hun Wallet te trekken wanneer zij dat willen)
- Facturering op basis van tijd voor freelancers (waarbij de persoon die inhuurt de freelancer geld laat opnemen in zijn Wallet als de tijd wordt gerapporteerd)
- Mecenaat (waarbij de mecenas de ontvanger toestaat om elke maand geld op te nemen om hun werk te blijven steunen)
- Automatisch verkopen (waarbij een klant van een Exchange toestaat dat een Exchange geld van zijn Wallet haalt om elke maand automatisch te verkopen)
- Saldo-opnamesysteem (waarbij een dienst met hoge volumes gebruikers toestaat om opnames van hun saldo aan te vragen, de dienst kan dan gemakkelijk alle uitbetalingen batchgewijs naar veel gebruikers op vaste intervallen sturen)


### Uitbetalingen


De uitbetalingsfunctionaliteit is gekoppeld aan de functie [Pull Payments] (https://docs.btcpayserver.org/PullPayments/). Deze functie laat u toe om uitbetalingen te creëren binnen uw BTCPay. Met deze functie kunt u pull-betalingen verwerken (terugbetalingen, uitbetalingen van salarissen of opnames).


#### Voorbeeld 1: Terugbetaling


Laten we beginnen met het voorbeeld van de terugbetaling. De klant heeft een artikel gekocht in je winkel, maar moet het helaas terugsturen. Ze willen een terugbetaling. Binnen BTCPay, kunt u een [Terugbetaling] (https://docs.btcpayserver.org/Refund/) aanmaken en de klant de link geven om hun geld op te eisen. Zodra de klant zijn Address heeft ingevuld en het geld heeft geclaimd, zal het worden weergegeven in de Payouts sectie.


De eerste status is In afwachting van goedkeuring. Winkelbedienden kunnen controleren of er meerdere wachten en na het maken van de selectie gebruik je de knop Acties.


Opties op de actieknop



- Geselecteerde uitbetalingen goedkeuren
- Goedkeuren en verzenden van geselecteerde uitbetalingen
- Annuleer geselecteerde uitbetalingen


De volgende stap is het goedkeuren & verzenden van geselecteerde uitbetalingen, omdat we de klant willen terugbetalen. Controleer de Address van de klant, waarop het bedrag staat en of we willen dat de kosten van de terugbetaling worden afgetrokken of niet. Zodra je de controles hebt uitgevoerd, is het ondertekenen van de transactie de enige resterende stap.


De klant wordt nu bijgewerkt op de claimpagina. Hij kan de transactie volgen via een link naar een Block explorer en zijn transactie. Zodra de transactie is bevestigd, verandert de status in 'Voltooid'.


#### Voorbeeld 2: Salaris


Laten we nu eens kijken naar de uitbetaling van salarissen, aangezien deze vanuit de winkel wordt aangestuurd en niet op verzoek van de klant. Het onderliggende concept is hetzelfde; het maakt gebruik van pull-betalingen. Maar in plaats van een terugbetaling maken we een [Pull Payment] (https://docs.btcpayserver.org/PullPayments/).


Ga naar de tab Pull Betalingen in uw BTCPay server. Klik in de rechterbovenhoek op de knop "Create Pull Payment".


Nu zijn we bij het aanmaken van de Payout, geef het een naam en het gewenste bedrag in de gekozen valuta. Vul de Omschrijving in, zodat de werknemer weet waar het over gaat. Het volgende gedeelte is vergelijkbaar met terugbetalingen. De werknemer vult de Bestemming Address in en het bedrag dat hij van deze Payout wil claimen. Hij kan besluiten om er 2 aparte claims van te maken, naar verschillende adressen, of zelfs een gedeeltelijke claim over de bliksem.


Als er meerdere uitbetalingen in de wachtrij staan, kun je deze per batch ondertekenen en versturen. Zodra de uitbetalingen zijn ondertekend, worden ze verplaatst naar het tabblad In uitvoering en wordt de Transactie weergegeven. Als de uitbetaling door het netwerk is geaccepteerd, gaat deze naar het tabblad Voltooid. Het tabblad Voltooid is puur voor historische doeleinden. Het bevat de verwerkte uitbetalingen en de transacties die erbij horen


### Betalingen trekken


#### Concept


Wanneer een verzender een Pull-betaling configureert, kan hij een aantal eigenschappen configureren:



- Pull verzoek Naam
- Een limietbedrag
- Een eenheid (zoals BTC, SAT, USD)
- Betaalmethoden
  - BTC On-Chain
  - BTC off-chain
- Beschrijving
- Aangepaste CSS
- Einddatum (optioneel voor Lightning Network BOLT11)


Hierna kan de verzender de pull-betaling via een link delen met de ontvanger, zodat deze een uitbetaling kan aanmaken. De ontvanger kiest zijn uitbetaling:



- Welke betaalmethode gebruiken
- Waar het geld naartoe sturen


Zodra een uitbetaling is aangemaakt, telt deze mee voor de limiet van de pull-betaling voor de huidige periode. De verzender zal dan de uitbetaling goedkeuren door het tarief in te stellen waartegen de uitbetaling zal worden verzonden en doorgaan met de betaling.


Voor de verzender voorzien we een gebruiksvriendelijke methode om meerdere uitbetalingen van de [BTCPay Internal Wallet] (https://docs.btcpayserver.org/Wallet/) te batchen.


#### Greenfield API


BTCPay Server biedt een volledige API aan zowel de verzender als de ontvanger die is gedocumenteerd in de `/docs` pagina van uw instantie. (of op de documentatie website https://docs.btcpayserver.org)


Omdat onze API de volledige mogelijkheden van pull-betalingen blootlegt, kan een verzender betalingen automatiseren volgens zijn eigen behoeften.


### Vaardigheden


In dit onderdeel heb je het volgende geleerd:



- Diepgaand begrip van de Invoice statussen van BTCPay Server, evenals de acties die erop kunnen worden uitgevoerd
- Invoice mechanismen met verlengde levensduur, bekend als Verzoeken, aanpassen en beheren.
- De extra flexibele betalingsmogelijkheden die de unieke Pull Payment-functie van BTCPay Server biedt, in het bijzonder bij het afhandelen van terugbetalingen en salarisbetalingen.


### Kennisbeoordeling


#### KA Conceptueel overzicht


Wat zijn enkele verschillen tussen facturen en betalingsverzoeken en wat kan een goede reden zijn om de laatste te gebruiken?


#### KA Conceptueel overzicht


Hoe breiden pull-betalingen uit ten opzichte van wat doorgaans On-Chain kan worden gedaan? Beschrijf enkele use cases die ze mogelijk maken.


## BTCPay server standaard plugins


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Standaard plugins en apps


BTCPay server wordt geleverd met een standaardset plugins (apps) die BTCPay Server kunnen veranderen in een e-commerce betalingsgateway. Met de toevoegingen van een verkooppunt, crowdfundplatform en een gemakkelijke betaalknop wordt BTCPay Server een eenvoudig te implementeren oplossing.


### Verkooppunt


Een van de standaard plugins van BTCPay Server is Point of Sale (PoS). Met de PoS-plugin kan een winkeleigenaar een webshop rechtstreeks vanuit BTCPay Server creëren; de winkeleigenaar heeft geen e-commerce-oplossingen van derden nodig om een webshop te runnen. De webgebaseerde PoS-app stelt gebruikers met fysieke winkels in staat om eenvoudig Bitcoin te accepteren, zonder kosten of een derde partij, direct in hun Wallet. De PoS kan eenvoudig worden weergegeven op tablets of andere apparaten die webbrowsen ondersteunen. Gebruikers kunnen eenvoudig een snelkoppeling naar het beginscherm maken om snel toegang te krijgen tot de webapp.


#### Een nieuw verkooppunt maken


Met BTCPay Server kunnen winkeleigenaars snel een verkooppunt in meerdere lay-outs maken. BTCPay Server erkent dat niet elke winkel e-commerce is, en niet elke winkel is een bar of restaurant, en het komt met meerdere standaard opstellingen voor uw PoS.


Wanneer de winkeleigenaar op "Point of Sale" klikt in zijn linkermenubalk, zal BTCPay Server nu om een naam vragen; deze naam zal zichtbaar zijn in de linkermenubalk. Klik op Aanmaken om de PoS aan te maken.


![image](assets/en/098.webp)


#### Werk het nieuwe verkooppunt bij


Nadat je een nieuwe kassa hebt gemaakt, kun je in het volgende scherm je kassa bijwerken en items voor je winkel toevoegen.


##### Naam app


De naam die u hier geeft aan uw verkooppunt zal zichtbaar zijn in het hoofdmenu van de BTCPay Server.


##### Titel weergeven


Het publiek zal de titel of naam van uw winkel zien wanneer ze deze bezoeken. BTCPay Server geeft uw winkel standaard de naam "Theewinkel" Vervang dit door de naam van uw winkel.


![image](assets/en/099.webp)


#### Stijl verkooppunt kiezen


BTCPay Server kan zijn Point Of Sale op meerdere manieren weergeven.



- Productlijst
  - Een winkelweergave waarbij klanten slechts 1 product tegelijk kunnen kopen.
- Productlijst met een winkelwagentje.
  - Een winkelweergave waarin klanten meerdere artikelen tegelijk kunnen kopen en rechts op hun scherm een overzicht van hun winkelwagentje krijgen.
- Alleen toetsenbord
  - Geen productlijst, alleen een toetsenbord voor directe facturering.
- Printweergave (afdrukbare productlijst met QR)
  - Als u uw productlijst niet altijd digitaal kunt weergeven, hebt u een "offline" oplossing voor producten nodig; BTCPay Server heeft een afdrukweergave om te functioneren als een offline winkel.


![image](assets/en/100.webp)


#### Verkooppuntstijl - Productenlijst


![image](assets/en/101.webp)


#### Verkooppuntstijl - Productenlijst + Winkelwagen


![image](assets/en/102.webp)


#### Point Of Sale-stijl - alleen toetsenbord


![image](assets/en/103.webp)


#### Point Of Sale stijl - Print display


![image](assets/en/104.webp)


#### Valuta


De winkeleigenaar kan een andere valuta instellen voor zijn verkooppunt dan de algemeen ingestelde standaardvaluta. De standaardvaluta van de winkel wordt automatisch ingevuld in dit veld.


#### Beschrijving


Vertel de wereld over je winkel; wat verkoop je en voor hoeveel? Alles wat je winkel uitlegt hoort hier thuis.


![image](assets/en/105.webp)


#### Producten


Wanneer een verkooppunt wordt gecreëerd, voegt een standaard BTCPay-server een aantal items toe aan de winkel ter referentie. Klik op de knop Bewerken op een van de standaard items om elke mogelijke optie voor een item beter te begrijpen.


Een nieuw product maken in je winkel bestaat uit de volgende velden;



- Titel
- Prijs (vast, minimum of aangepast)
- Afbeelding URL
- Beschrijving
- Inventaris
- ID
- Knoptekst kopen.
- Inschakelen/uitschakelen


Zodra de winkeleigenaar alle nieuwe productvelden heeft ingevuld, klik je op Opslaan en je zult zien dat de sectie Producten in het Verkooppunt nu gevuld wordt. Sla altijd op in de rechterbovenhoek van je scherm om te voorkomen dat winkeleigenaren hun voortgang kwijtraken tijdens het toevoegen van producten.


Winkeliers kunnen ook de "Raw Editor" gebruiken om hun producten te configureren. De Raw Editor vereist een basiskennis van JSON-structuren.


![image](assets/en/106.webp)


#### Kassa


BTCPay Server maakt kleine PoS-specifieke aanpassingen aan de kassa mogelijk. De winkeleigenaar kan de tekst "Koop voor x" instellen of specifieke klantgegevens opvragen door deze toe te voegen aan de formulieren.


#### Tips


Alleen sommige winkels hebben de optie voor Tips over hun verkopen nodig. Winkeleigenaren kunnen dit naar eigen inzicht in- of uitschakelen voor hun winkel. Als de winkel fooien gebruikt die aanstaan, kan de winkeleigenaar de tekst in het veld voor de fooien instellen. BTCPay Server fooien werken op basis van een percentage. Winkeliers kunnen meerdere percentages toevoegen, gescheiden door komma's.


#### Kortingen


Als winkeleigenaar wil je de klant misschien een aangepaste korting geven bij het afrekenen; de toggle voor Kortingen wordt beschikbaar bij het afrekenen van je winkel. Dit wordt echter sterk afgeraden als je zelfkassasystemen gebruikt.


#### Aangepaste betalingen


Als de optie Aangepaste betalingen is ingeschakeld, kan de klant een vaste prijs invoeren die gelijk is aan of hoger is dan de oorspronkelijke Invoice die door de winkel is gegenereerd.


#### Extra opties


Nadat je alles hebt ingesteld voor je Point of Sale, blijven er nog wat extra opties over. Winkeleigenaren kunnen hun PoS eenvoudig insluiten via een Iframe of een betaalknop insluiten die naar een specifiek winkelitem linkt. Om de zojuist gemaakte PoS-winkel te stylen, kunnen eigenaars aangepaste CSS toevoegen onderaan de extra opties.


#### Verwijder deze app


Als de winkeleigenaar het verkooppunt volledig wil verwijderen van zijn BTCPay Server, kunnen winkeleigenaars onderaan het updaten van de PoS klikken op de knop "Delete this app" om hun PoS app volledig te vernietigen. Wanneer u klikt op "Delete this app", zal BTCPay Server om bevestiging vragen door `DELETE` in te typen en te bevestigen door te klikken op de knop Delete. Na het verwijderen keert de winkeleigenaar terug naar het BTCPay Server dashboard.


### BTCPay Server - Crowdfund


Naast de Point of Sale plugin heeft BTCPay Server de optie om een crowdfund aan te maken. Net als elk ander crowdfundplatform kunnen winkeleigenaren een doel instellen, extraatjes voor bijdragen creëren en het aanpassen aan hun behoeften.


#### Hoe zet je een nieuw crowdfund op?


Klik op de Crowdfund plugin via het hoofdmenu aan de linkerkant van uw BTCPay Server, onder de Plugin sectie. BTCPay Server zal nu een naam vragen voor het Crowdfund; deze naam zal ook worden weergegeven in de linker menubalk.


![image](assets/en/107.webp)


#### Werk het nieuwe verkooppunt bij


Zodra de App een naam heeft gekregen, is het volgende scherm om de App bij te werken zodat deze context heeft.


#### Naam app


De naam die aan uw Crowdfund is gegeven zal zichtbaar zijn in het hoofdmenu van BTCPay Server.


#### Titel weergeven


De titel wordt gegeven aan het Crowdfund voor het publiek.


#### Tagline


Geef het crowdfund een one-liner om te laten zien waar de inzamelingsactie over gaat.


![image](assets/en/108.webp)


#### Aanbevolen afbeelding URL


Elk crowdfund heeft zijn hoofdafbeelding, die ene banner die je direct herkent. Deze afbeelding kan worden opgeslagen op je server als je Administratieve rechten hebt. Admins kunnen uploaden onder de BTCPay Server instellingen - Bestanden. Als je een winkeleigenaar bent, moet de afbeelding worden geüpload naar het web via een externe host (bijvoorbeeld Imgur).


#### Crowdfund openbaar maken


Deze toggle zorgt ervoor dat je Crowdfund openbaar wordt en dus zichtbaar voor de buitenwereld. Voor testdoeleinden of om te zien of je thema correct wordt toegepast, houd je deze instelling op OFF voor de periode van het bouwen van het crowdfund.


#### Beschrijving


Vertel de wereld over je Crowdfund. Waarvoor zamel je geld in? Alles wat je crowdfund uitlegt moet hier.


![image](assets/en/109.webp)


#### Crowdfund doel


Stel een doel in voor wat de fondsenwerver moet verdienen voor het project en in welke valuta het doel moet worden uitgedrukt. Zorg ervoor dat als je doelen tussen datums zijn ingesteld, je deze doel- en einddatums opneemt onder Doelen in crowdfund.


![image](assets/en/110.webp)


#### Extra's


Perks kunnen je crowdfundinginspanningen aanzienlijk verbeteren. Dit komt omdat perks mensen een manier geven om deel te nemen aan je campagne. Ze spelen in op zowel egoïstische als welwillende motivaties. En ze geven je toegang tot de uitgaven van je supporters, niet alleen tot hun filantropische portemonnee -- je kunt wel raden wat belangrijker is.


Een nieuw perk aanmaken bestaat uit de volgende velden.



- Titel
- Prijs (vast, minimum of aangepast)
- Afbeelding URL
- Beschrijving
- Inventaris
- ID
- Knoptekst kopen.
- Inschakelen/uitschakelen


Zodra de winkeleigenaar alle velden van de nieuwe perk heeft ingevuld, klik je op Opslaan en zie je dat het onderdeel Perks in de Crowdfunds nu wordt ingevuld.


![image](assets/en/111.webp)


### BTCPay Server - Verkooppunt


#### Bijdragen


Winkeliers kunnen kiezen hoe ze de Perks willen weergeven, hoe ze worden gesorteerd en zelfs hoe ze worden gerangschikt ten opzichte van andere Perks. Maar als de doelen van Crowdfunds zijn bereikt, willen winkeleigenaars misschien dat er geen donaties meer naar deze fondsenwerving gaan. Daarom kan hij "Sta geen extra bijdragen toe na het bereiken van het doel" inschakelen. Hierdoor zal het Crowdfund geen donaties meer accepteren.


##### Crowdfund gedrag


Standaard telt Crowdfund alleen facturen die met Crowdfund zijn gemaakt mee voor het doel. Het kan echter voorkomen dat de winkeleigenaar wil dat alle facturen die in deze winkel zijn gemaakt meetellen voor het crowdfund.


#### Extra opties voor aanpassing


BTCpay Server biedt een aantal extra aanpassingen. Voeg geluiden, animaties of zelfs discussies toe aan het Crowdfund. Winkeleigenaren kunnen ook het uiterlijk van het Crowdfund aanpassen door hun eigen aangepaste CSS in te voeren.


#### Verwijder deze app


Als de winkeleigenaar het Crowdfund volledig wil verwijderen van zijn BTCPay Server, kunnen ze onderaan het updaten van het Crowdfund klikken op de knop "Delete this app" om hun Crowdfund app volledig te verwijderen. Bij het klikken op "Delete this app", zal BTCPay Server om bevestiging vragen door `DELETE` in te typen en te bevestigen door te klikken op de Delete knop. Na het verwijderen keert de winkeleigenaar terug naar het BTCPay Server dashboard.


### BTCPay server - Betaalknop


Gemakkelijk embeddable HTML en zeer aanpasbare betaalknoppen stellen winkeleigenaars in staat om fooien en donaties te ontvangen. In de linkermenubalk van BTCPay Server, onder de sectie Plugins, kunnen winkeleigenaars klikken op "Betaalknop" en klikken op Inschakelen om een betaalknop te maken.


#### Algemene instellingen


Binnen de Algemene instellingen voor de betaalknop kunnen winkeleigenaren het volgende instellen



- Standaardprijs
- Standaardvaluta
- Standaard betaalmethode
  - Standaard opslaan gebruiken
  - BTC On-Chain
  - BTC off-chain (Bliksem)
  - BTC off-chain (LNURL-betaling)
- Afrekenen beschrijving
- Bestel ID


#### Weergaveopties


De betaalknop van BTCPay Server kan worden geconfigureerd voor verschillende stijlen. Buttons kunnen een vast of aangepast bedrag hebben, dat wordt weergegeven met een schuifregelaar of plus en min toggles.


#### Modaal gebruiken


Bij het maken van de betaalknop kunnen winkeleigenaren het gedrag kiezen wanneer een klant erop klikt en deze in een modal of als nieuwe pagina weergeven.


**Let op!**


Waarschuwing: De betaalknop mag alleen worden gebruikt voor fooien en donaties


Het gebruik van de betaalknop voor e-commerce integraties wordt niet aanbevolen omdat de gebruiker orderrelevante informatie kan wijzigen. Voor e-commerce moet je onze Greenfield API gebruiken. Als deze winkel commerciële transacties verwerkt, raden we aan een aparte winkel te maken voordat je de betaalknop gebruikt.


#### Tekst betaalknop aanpassen


Standaard staat er op de betaalknop van BTCPay Server "Pay With BTCPay". Winkeliers kunnen deze tekst naar eigen wens instellen en het BTCPay Server logo veranderen in hun eigen logo. Stel de tekst in met behulp van de "Pay Button Text" en plak de URL van de afbeelding onder de "Pay Button Image URL".


##### Grootte afbeelding


De grootte van de afbeelding in de knop kan slechts op drie standaardwaarden worden ingesteld.



- 146x40px
- 168x46px
- 209x57px


#### Type knop


BTCPay Server kent drie toestanden voor de Betalingsknop.



- Vast bedrag
  - De vorige ingestelde prijs staat in de algemene instellingen van de knop.
- Aangepast bedrag
  - De betaalknop van BTCPay Server heeft + en - knoppen om een aangepaste prijs in te stellen.
  - Bij het gebruik van het aangepaste bedrag, zal BTCPay Server vragen om een Min, Max, en hoe geleidelijk het moet toenemen.
  - Knoppen kunnen worden ingesteld op "Gebruik eenvoudige invoerstijl". Hierdoor verdwijnen de +/- knoppen.
  - Pas knop inline aan waar knop en toggles inline verschijnen.
- Schuifregelaar
  - Vergelijkbaar met de aangepaste hoeveelheid, maar visueel anders omdat het een schuifregelaar heeft in plaats van de +/- toggles.
  - Wanneer u de glijder gebruikt, zal de BTCPay server vragen om een minimum, maximum en hoe geleidelijk het moet toenemen.


**Let op!**


De knop Betaling kan bovenaan de waarschuwingsbeschrijving worden verwijderd.


#### Betalingsmeldingen


Server IPN (Instant Payment Notification) is ontworpen voor webhooks en kan worden geconfigureerd met een URL voor gegevens na aankoop.


#### E-mailmeldingen


Wanneer een betaling is gedaan, kan BTCPay Server de winkeleigenaar verwittigen.


#### Browser omleiden


Wanneer de klant de aankoop afrondt, wordt hij doorgestuurd naar deze link als dit is ingesteld door de winkeleigenaar.


#### Geavanceerde Betalingsknop Opties


Specificeer extra query string parameters die moeten worden toegevoegd aan de afrekenpagina zodra de Invoice is aangemaakt. Bijvoorbeeld, `lang=da-DK` zal de afrekenpagina standaard in het Deens laden.


#### App als eindpunt gebruiken


Je kunt de betaalknop direct koppelen aan een item in een van de PoS- of Crowdfund-apps die je eerder hebt gebruikt.


Winkeliers kunnen op het dropdownmenu klikken en de gewenste app selecteren. Zodra de app is geselecteerd, kan de winkelier het item toevoegen dat moet worden gekoppeld.


#### Gegenereerde code


Aangezien de betaalknop van BTCPay Server een gemakkelijk insluitbare HTML is, toont BTCPay Server de gegenereerde code om te kopiëren naar een website onderaan na het configureren van de betaalknop.


Winkeliers kunnen de gegenereerde code kopiëren naar hun website en de betaalknop van BTCPay Server is direct actief op hun website.


#### Betalingsmeldingen


Server IPN (Instant Payment Notification) is ontworpen voor webhooks en kan worden geconfigureerd met een URL om aankoopgegevens te posten.


#### E-mailmeldingen


Wanneer een betaling wordt gedaan, kan BTCPay Server de winkeleigenaar verwittigen.


#### Browser omleiden


Wanneer de klant de aankoop afrondt, wordt hij doorgestuurd naar deze link als dit is ingesteld door de winkeleigenaar.


#### Geavanceerde Betalingsknop Opties


Specificeer extra query string parameters die moeten worden toegevoegd aan de afrekenpagina zodra de Invoice is aangemaakt. Bijvoorbeeld, `lang=da-DK` zal de afrekenpagina standaard in het Deens laden.


#### App als eindpunt gebruiken


Je kunt de betaalknop direct koppelen aan een artikel in een van de PoS- of Crowdfund-apps die je eerder hebt gebruikt. Winkeliers kunnen op het uitklapmenu klikken en de gewenste app selecteren. Zodra de app is geselecteerd, kan de winkeleigenaar het item toevoegen dat moet worden gekoppeld.


#### Gegenereerde code


Aangezien de betaalknop van BTCPay Server een gemakkelijk insluitbare HTML is, toont BTCPay Server de gegenereerde code om te kopiëren naar een website onderaan na het configureren van de betaalknop. Winkeliers kunnen de gegenereerde code kopiëren naar hun website en de betaalknop van BTCPay Server is direct actief op hun website.


### Vaardigheden


In dit gedeelte heb je geleerd:



- Hoe de geïntegreerde PoS-plugin van BTCPay Server gebruiken om gemakkelijk een aangepaste winkel te maken
- Hoe de geïntegreerde Crowdfund-plugin van BTCPay Server gebruiken om gemakkelijk een aangepaste crowdfund-app te maken
- Code genereren voor een aangepaste betaalknop met de Betaalknop-plugin


### Kennisbeoordeling


#### KA-overzicht


Wat zijn de drie ingebouwde plugins die standaard worden geleverd met BTCPay Server? Beschrijf in een paar woorden hoe ze gebruikt kunnen worden.


# BTCPay server configureren


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Basiskennis van het installeren van BTCPay Server op een LunaNode-omgeving


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Installatie van BTCPay-server op gehoste omgeving (LunaNode)


Deze stappen geven u alle nodige informatie om aan de slag te gaan met BTCPay Server op LunaNode. Er zijn veel opties om de software te implementeren.

U kunt alle details van BTCPay Server vinden op https://docs.btcpayserver.org.


#### Waar beginnen we?


In dit deel maakt u kennis met LunaNode als hostingprovider, leert u over de eerste stappen van het gebruik van uw BTCPay Server en leert u hoe u Lightning Network kunt gebruiken. Nadat we alle stappen hebben doorlopen, kun je een webshop of crowdfundplatform draaien dat Bitcoin accepteert!


Dit is een van de vele manieren om BTCPay Server te implementeren. Lees onze documentatie voor meer details.


https://docs.btcpayserver.org.


### BTCPay server - LunaNode inzet


#### LunaNode inzet


Ga eerst naar de website van LunaNode.com, waar we een nieuw account zullen aanmaken. Klik rechtsboven op Aanmelden of gebruik de Get Started wizard op hun homepage.


![image](assets/en/112.webp)


Nadat je een nieuw account hebt aangemaakt, stuurt LunaNode een verificatiemail. Zodra je het account hebt geverifieerd, krijg je in vergelijking met Voltage direct de optie om je accountsaldo op te waarderen. Dit saldo is nodig om de serverruimte en hostingkosten te dekken.


![image](assets/en/113.webp)


#### Krediet toevoegen aan je LunaNode-account


Zodra je op "Tegoed storten" hebt geklikt, kun je instellen met hoeveel je je account wilt opwaarderen en hoe je ervoor wilt betalen. LunaNode en BTCPay Server kosten tussen de $ 10 en $ 20 per maand.

Vergeleken met Voltage.cloud krijgt u volledige toegang tot uw Virtual Private Server (VPS), waardoor u meer controle heeft over uw server. Nadat u uw nieuwe account hebt aangemaakt, stuurt LunaNode een verificatiemail.

Zodra u de account verifieert, in vergelijking met Voltage, krijgt u onmiddellijk de optie om uw accountsaldo op te waarderen. Dit saldo is nodig om de serverruimte en hostingkosten te dekken.


#### Hoe zet ik een nieuwe server in?


In deze gids zullen we u door het installatieproces leiden door een set API sleutels aan te maken en de BTCPay Server launcher te gebruiken, ontwikkeld door LunaNode.


Klik in je LunaNode dashboard rechtsboven op API. Dit opent een nieuwe pagina. We hoeven alleen een Naam voor de API-sleutel in te stellen. De rest wordt geregeld door LunaNode en wordt niet behandeld in deze gids. Klik op de knop Create API Credential.

Na het aanmaken van de API-referenties krijg je een lange reeks letters en tekens. Dit is je API-sleutel.


![image](assets/en/114.webp)


#### Hoe zet ik een nieuwe server in?


Deze gegevens bestaan uit twee delen: de API-sleutel en de API-ID; we hebben ze allebei nodig. Voordat we naar de volgende stap gaan, openen we een tweede tabblad in de browser en gaan we naar https://launchbtcpay.lunanode.com/


Hier wordt je gevraagd om je API-sleutel en API-ID op te geven. Dit is om je te laten weten dat jij degene bent die deze nieuwe server heeft geleverd. De API-sleutel zou nog steeds open moeten staan in je vorige tabblad; als je naar beneden scrolt in de tabel hieronder, vind je de API-ID.


Je kunt teruggaan naar de pagina met de Launcher, de velden met je API-sleutel en ID invullen en op Doorgaan klikken.


![image](assets/en/115.webp)


In de volgende stap kunt u een domeinnaam opgeven. Als u al een domein bezit en deze wilt gebruiken voor BTCPay Server, zorg er dan voor dat u ook het DNS record (een `A` record genoemd) op uw domein toevoegt. Als u geen domein bezit, gebruik dan het LunaNode domein (u kunt dit later veranderen in de BTCPay Server instellingen) en klik op Doorgaan.


Lees meer over het instellen of wijzigen van een DNS record voor BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Start BTCPay Server op LunaNode


Na het uitvoeren van de voorgaande stappen, kunnen we alle opties voor onze nieuwe server instellen. Hier selecteren we Bitcoin (BTC) als onze ondersteunde valuta. We kunnen ook een e-mail instellen om meldingen te ontvangen over versleutelingscertificaten voor vernieuwingsdoeleinden, wat optioneel is.


Deze gids richt zich op het opzetten van een Mainnet omgeving (echte Bitcoin); LunaNode staat je echter ook toe om het in te stellen op Testnet of Regtest voor ontwikkelingsdoeleinden. Voor deze gids laten we de Mainnet optie staan.


Je kunt je Lightning-implementatie kiezen. LunaNode biedt twee verschillende implementaties, LND en Core Lightning. Voor deze gids nemen we LND. Er zijn weinig maar echte verschillen in beide implementaties; voor meer hierover raden we je aan de uitgebreide documentatie te lezen: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode biedt meerdere Virtual Machine (VM) plannen. Deze verschillen qua prijsklasse en serverspecificaties. Voor deze handleiding is een m2-plan voldoende; als je echter meer dan alleen Bitcoin als valuta hebt geselecteerd, overweeg dan om minimaal een m4 te gebruiken.


De initiële Blockchain synchronisatie versnellen; dit is optioneel en hangt af van je behoeften. Er zijn geavanceerde opties, zoals het instellen van een Lightning Alias, het verwijzen naar een specifieke GitHub release, of het instellen van SSH sleutels; geen van deze worden in deze gids behandeld.


Na het invullen van het formulier, moet u klikken op Launch VM, en Lunanode zal beginnen met het creëren van uw nieuwe VM, inclusief BTCPay Server erop geïnstalleerd. Dit proces duurt een paar minuten; zodra uw server klaar is, geeft LunaNode u de link naar uw nieuwe BTCPay Server.


Na het creatieproces, klik op de link naar uw BTCPay Server; hier zal u gevraagd worden om een Administrator account aan te maken.


![image](assets/en/117.webp)


### Vaardigheden


In dit gedeelte heb je geleerd:



- Een account aanmaken en financieren op LunaNode
- De BTCPay Server Launcher gebruiken om uw eigen server te maken


### Kennisbeoordeling


#### KA Conceptueel overzicht


Beschrijf enkele van de verschillen tussen het draaien van een instantie van BTCPay Server op een VPS vs. het creëren van een account op een gehoste instantie.


## BTCPay Server installeren op een Voltage-omgeving


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


U raakt vertrouwd met Voltage.cloud als hostingprovider, leert over de eerste stappen van het gebruik van uw BTCPay Server en leert hoe u Lightning Network kunt gebruiken. Nadat we alle stappen hebben doorlopen, kunt u een webshop of crowdfundplatform draaien dat Bitcoin accepteert!


Dit is een van de vele manieren om BTCPay Server te implementeren. Lees onze documentatie voor meer details.

https://docs.btcpayserver.org.


### BTCPay Server - Voltage.cloud inzet


Ga eerst naar de website Voltage.cloud en meld u aan voor een nieuwe account. Wanneer u een account aanmaakt, kunt u zich aanmelden voor een gratis proefperiode van 7 dagen. Klik rechtsboven op Aanmelden of gebruik de optie "Probeer een gratis 7-daagse proefversie" op de startpagina.


![image](assets/en/118.webp)


Nadat je een account hebt aangemaakt, klik je op de knop `NODES` op je dashboard. Zodra we Nodes hebben geselecteerd en een nieuwe node hebben aangemaakt, krijgen we de mogelijke aanbiedingen van Voltage te zien. Aangezien deze gids ook de Lightning Network zal behandelen, moeten we bij Voltage eerst onze Lightning-implementatie kiezen voordat we een BTCPay Server aanmaken. Klik op LightningNode.


![image](assets/en/119.webp)


Hier moet je kiezen wat voor soort Lightning node je wilt. Voltage heeft verschillende opties voor je verlichtingsinstallatie. Dit is anders wanneer u bijvoorbeeld LunaNode gebruikt. Voor deze handleiding volstaat een Lite Node. Lees meer over de verschillen in Voltage.cloud.


![image](assets/en/120.webp)


Geef uw node een naam, stel een wachtwoord in en beveilig dit wachtwoord. Als dit wachtwoord verloren gaat, verliest u de toegang tot uw back-ups en kan Voltage het niet herstellen. Maak de node aan en Voltage toont u de voortgang. Voltage heeft uw Lightning Node aangemaakt. We kunnen nu de BTCPay Server instance aanmaken en direct toegang krijgen tot de Lightning Network.


Klik op Nodes links bovenaan je dashboard. Hier kunt u het volgende deel van uw BTCPay Server instance instellen. Klik op "create new" zodra je in het nodes overzicht bent. Je krijgt een soortgelijk scherm als voorheen. Nu kiezen we BTCPay Server in plaats van Lightning Node.


Voltage toont u de geolocatie van uw BTCPay-server, die wordt gehost in de regio US West. Hier ziet u ook de kosten voor het hosten van de server. Klik op Create en geef uw BTCPay-server een naam. Schakel Lightning in en Voltage toont u het Lightning-knooppunt dat u in de vorige stap hebt gemaakt. Klik op Create en Voltage creëert een BTCPay Server instance.


![image](assets/en/121.webp)


Nadat u op Aanmaken hebt geklikt, geeft Voltage u de standaard gebruikersnaam en het standaard wachtwoord. Deze zijn vergelijkbaar met uw vorige wachtwoord in Voltage. Klik op de knop Inloggen op account om u door te verwijzen naar uw BTCPay-server.


Welkom bij uw nieuwe BTCPay Server instantie. Omdat we Lightning al hebben ingesteld in het creatieproces, is Lightning al ingeschakeld!


### Vaardigheden


In dit hoofdstuk heb je geleerd:



- Een account aanmaken op Voltage.cloud
- Stappen om BTCPay Server te laten draaien samen met een Lightning node op de account


### Kennisbeoordeling


#### KA Conceptueel overzicht


Wat zijn enkele belangrijke verschillen tussen de Voltage- en LunaNode-opstellingen?


## BTCPay Server installeren op een Umbrel knooppunt


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Aan het einde van deze stappen, kunt u bliksem betalingen accepteren naar uw BTCPay winkel op uw lokale netwerk. Dit proces is ook van toepassing als je een umbrel node in een restaurant of bedrijf runt. Als je deze winkel wilt verbinden met een publieke website, volg dan de Geavanceerde oefening om je umbrel node bloot te stellen aan het publiek.


https://umbrel.com/


![image](assets/en/122.webp)


### BTCPay Server - Inzet Umbrel


Nadat uw Umbrel knooppunt volledig gesynchroniseerd is met de Bitcoin Blockchain, gaat u naar de Umbrel App Store en zoekt u naar BTCPay Server onder Apps.


![image](assets/en/123.webp)


Klik op BTCPay Server om de details van de app te zien. Als de details voor BTCPay Server open zijn, zie je rechtsonder de vereisten om de app goed te laten werken. Het laat zien dat het een Bitcoin en Lightning node vereist. Als je de Lightning Node nog niet op je Umbrel hebt geïnstalleerd, klik dan op Installeren. Dit proces kan een paar minuten duren.


![image](assets/en/124.webp)


Na de installatie van je lightning Node:


1. Klik op openen in de app details of op de App in het Umbrels dashboard.

2. Klik op setup a new node; je krijgt 24 woorden te zien voor herstel van je bliksemknooppunt.

3. Schrijf deze op.


![image](assets/en/125.webp)


Umbrel zal vragen om verificatie van de zojuist opgeschreven woorden. Nadat het Lightning knooppunt is ingesteld, ga je terug naar de Umbrel App Store en zoek je BTCPay Server. Klik op de installatieknop, en Umbrel zal laten zien of de vereiste componenten zijn geïnstalleerd en dat BTCPay Server toegang vereist tot deze componenten. Klik na de installatie op Openen in de rechterbovenhoek van de App details of open BTCPay Server via uw Umbrels dashboard.


Umbrel vraagt om verificatie van de zojuist opgeschreven woorden.


![image](assets/en/126.webp)


**Let op!**


Zorg ervoor dat je deze op een veilige plaats opbergt, zoals eerder geleerd bij het opbergen van sleutels.


Nadat het Lightning knooppunt is ingesteld, keert u terug naar de Umbrel App Store en zoekt u BTCPay Server. Klik op de installatieknop en Umbrel zal laten zien of de vereiste componenten zijn geïnstalleerd en dat BTCPay Server toegang tot deze componenten vereist.


![image](assets/en/127.webp)


Klik na de installatie op Openen in de rechterbovenhoek van de App details of open BTCPay Server via uw Umbrels dashboard.


![image](assets/en/128.webp)


### Vaardigheden


In dit gedeelte heb je geleerd:



- Stappen om BTCPay Server met Lightning functionaliteit te installeren op een Umbrel knooppunt


### Kennisbeoordeling


#### KA Conceptueel overzicht


Hoe verschilt de setup op Umbrel van de vorige twee gehoste opties?


# Laatste Sectie


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Beoordelingen

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusie van de cursus


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>