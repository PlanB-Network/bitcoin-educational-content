---
name: be-BOP
description: Praktische gids voor het te gelde maken van uw bedrijf met be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** is een e-commerce platform ontworpen voor ondernemers die online en offline willen verkopen, in volledige autonomie, terwijl ze betalingen accepteren in Bitcoin, via een bankrekening en in contanten. De oplossing is ook nuttig voor elk type organisatie die donaties wil inzamelen of haar verschillende activiteiten te gelde wil maken.



De oplossing is eenvoudig, licht en autonoom. Het maakt de creatie van een online winkel mogelijk, zelfs in een omgeving waar traditionele financiële diensten beperkt of afwezig zijn. **be-BOP** is ontworpen om efficiënt te werken met of zonder toegang tot banken, met Bitcoin als betalingsinfrastructuur.



In deze tutorial nemen we je stap voor stap mee door:





- Maak uw eerste online winkel met **be-BOP**
- Personaliseer je vitrine en je producten
- Beschikbare betalingsmethoden configureren
- Begrijp de beste manieren om effectief online te verkopen met **be-BOP**



Deze tutorial vereist geen geavanceerde technische vaardigheden. Het is bedoeld voor ontwikkelaars, maar ook voor ambachtslieden, handelaren, coöperaties of ondernemers die op een soevereine en veerkrachtige manier met digitale handel willen beginnen.



## Voorwaarden om be-BOP op uw eigen server te installeren



Voordat je be-BOP gaat installeren, moet je ervoor zorgen dat je over de volgende technische infrastructuur beschikt. Deze Elements zijn essentieel voor een goede werking van het platform:



### S3-compatibele opslag



be-BOP gebruikt een opslagsysteem om bestanden (zoals productafbeeldingen) te beheren. Dit vereist toegang tot een S3-service, zoals:





- [MinIO](https://min.io/) zelf gehost
- Amazon S3 (AWS)
- Objectopslag van Scaleway



Je moet een emmer configureren en de volgende informatie opgeven:





- S3_BUCKET**: emmernaam
- S3_ENDPOINT_URL**: toegangslink naar je S3-service
- S3_KEY_ID** en S3_KEY_SECRET: uw toegangscodes
- S3_REGION**: de regio van uw S3-service



### MongoDB database in ReplicaSet modus



be-BOP gebruikt MongoDB om winkel-, gebruikers-, product- en andere gegevens op te slaan.



Je hebt twee opties:





- Installeer MongoDB lokaal met **ReplicaSet-modus ingeschakeld**
- Gebruik een online service zoals **MongoDB Atlas**



Je hebt de volgende variabelen nodig:





- MONGODB_URL**: databaseverbinding Address
- MONGODB_DB**: databasenaam



## Node.js-omgeving



be-BOP werkt met Node.js. Zorg ervoor dat je **Node.js** versie 18 of hoger hebt en **Corepack** hebt ingeschakeld (nodig om pakketmanagers zoals pnpm te beheren). Het commando dat je moet uitvoeren is `corepack enable`



### Git LFS geïnstalleerd



Sommige bronnen (zoals grote afbeeldingen) worden beheerd via Git LFS (Large File Storage). Zorg ervoor dat Git LFS geïnstalleerd is op je machine met het `git lfs install` commando. Als deze voorwaarden eenmaal aanwezig zijn, ben je klaar om verder te gaan met de volgende stap: het downloaden en configureren van be-BOP.



**Noot:** Een technische handleiding voor het implementeren van software is beschikbaar in een aparte handleiding.



## Een Superbeheerder-account maken



De allereerste keer dat be-BOP wordt opgestart, wordt er een **Super Admin** account aangemaakt. Dit account heeft alle autorisaties die nodig zijn om backofficefuncties te beheren. Volg deze stappen om een account aan te maken:





- Ga naar `uwresiteweb/admin/login`
- Maak een super-admin account aan met een veilige login en wachtwoord



Met dit account heb je toegang tot alle backofficefuncties. Eenmaal aangemaakt kun je inloggen door je gebruikersnaam en wachtwoord in te voeren.



![login](assets/fr/001.webp)



## Back-Office configuratie en beveiliging



Voordat u uw Interface back-office verbinding configureert, moet u een unieke Hash aanmaken. Dit biedt bescherming tegen kwaadwillenden die proberen de verbindingslink naar uw Interface admin te stelen.



Om Hash aan te maken, ga naar `/admin/Settings`. In de sectie gewijd aan beveiliging (bijv. "Admin Hash"), definieer een unieke string (Hash). Eenmaal geregistreerd, zal de URL van de backoffice worden aangepast (bijv. `/admin-yourhash/login`) om de toegang te beperken voor onbevoegden.



![hash-login](assets/fr/002.webp)



2.2. Activeer de onderhoudsmodus (indien nodig)



Nog steeds in /admin/Settings, (Instellingen > Algemeen via Interface afbeeldingen) controleer de optie "onderhoudsmodus inschakelen" onderaan de pagina.



![maintenance-mode](assets/fr/003.webp)



Indien nodig kun je een lijst met geautoriseerde IPv4-adressen opgeven (gescheiden door komma's) om toegang tot de frontoffice mogelijk te maken tijdens onderhoud. De backoffice blijft toegankelijk voor beheerders.



![ip-bebop](assets/fr/004.webp)



## Communicatie instellen



Om be-BOP meldingen te laten versturen (bv. voor bestellingen, registraties of systeemberichten), moet u minstens één communicatiemethode configureren. Er zijn twee opties beschikbaar: e-mail (SMTP) of Nostr.



### SMTP-configuratie (e-mail)



be-BOP kan e-mails versturen via een SMTP-server. U hebt hiervoor geldige SMTP-referenties nodig, die vaak worden geleverd door een e-mailservice (bijv. Mailgun, Gmail, enz.).



Dit is wat je moet weten:



SMTP_HOST: SMTP server Address (bijv. smtp.mailgun.org)



SMTP_PORT: de te gebruiken poort (vaak 587 of 465)



SMTP_USER: je gebruikersnaam (meestal een e-mail Address)



SMTP_PASSWORD: je wachtwoord of API-sleutel



SMTP_FROM: de e-mail Address die wordt weergegeven als de afzender




### Nostr-configuratie



be-BOP maakt het mogelijk om meldingen te versturen via het Nostr-protocol, een gedecentraliseerde berichteninfrastructuur. Om dit te doen, moet u generate of Supply een Nostr private sleutel (NSEC). U kunt deze sleutel direct generate maken via de Interface van be-BOP, in de sectie gewijd aan Nostr. Als deze Elements correct geconfigureerd zijn, kan be-BOP automatisch berichten en waarschuwingen naar uw gebruikers sturen.



## Compatibele betalingsmethoden



be-BOP is compatibel met verschillende betaaloplossingen, zodat u uw klanten meer flexibiliteit kunt bieden. Dit is wat u nodig hebt om de betaalmethode in te stellen die het beste bij u past.



### Bitcoin Onchain



met be-BOP kunt u Bitcoin betalingen rechtstreeks op de Blockchain (On-Chain) accepteren, eenvoudig en veilig.



**Configuratiestappen:**





- Ga naar het **Betalingsinstellingen** menu
- Klik op **Bitcoin Nodeloos** om On-Chain betalingsparameters te openen.
- Vul de volgende velden in:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Tip:** Om uw uitgebreide publieke sleutel (Zpub) te verkrijgen, kunt u de geavanceerde instellingen van uw Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter, etc.) raadplegen. Zorg ervoor dat uw Wallet **niet alleen-lezen** is als u transactiegeschiedenis wilt gebruiken.



### Lightning Network



be-BOP kan ook direct Bitcoin betalingen accepteren dankzij Lightning Network. Er zijn momenteel twee configuratieopties beschikbaar:



**Phoenixd**



Ga naar het menu `Betalingsinstellingen` en klik op `Phoenixd`



![phoenixd](assets/fr/006.webp)



Je moet dan **het wachtwoord of de token-authenticatie** invoeren die je verbindt met je Phoenixd-instance, een backend ontwikkeld door Acinq waarmee je Lightning-betalingen kunt beheren met je eigen node, maar zonder de complexiteit van het beheren van betaalkanalen.



**Zwitserse Bitcoin betalen**



Als je niet zelf een Lightning-node wilt beheren, **Swiss Bitcoin Pay** is een kant-en-klare, eenvoudig te configureren oplossing die ideaal is om te beginnen met het accepteren van Lightning-betalingen zonder complexe infrastructuur.



Configuratiestappen:





- Klik in het menu "Betaalinstellingen" op `Zwitserse Bitcoin Pay`
- Log in op je Zwitserse Bitcoin Pay account (of maak er een aan als je er nog geen hebt).
- Voer de API-sleutel in die door Bitcoin Pay is geleverd en klik vervolgens op "Opslaan"



Eenmaal ingesteld, zal be-BOP automatisch generate Lightning facturen voor uw klanten maken en ontvangt u betalingen direct op uw Zwitserse Bitcoin Pay account. Deze oplossing is ideaal voor gebruikers die de technische complexiteit van een persoonlijk knooppunt willen vermijden en toch snelle, goedkope betalingen willen accepteren.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Naast Bitcoin kunt u met be-BOP ook contante betalingen accepteren via PayPal, een bekende en veelgebruikte internationale oplossing.



Configuratiestappen:





- Ga naar het menu `Betalingsinstellingen
- Klik op `PayPal
- Voer in uw Paypal-account (gedeelte ontwikkelaar) de `Client ID` en de `Secret` in
- Selecteer de valuta van je keuze (bijv. **USD**, **EUR**, **XOF**, etc.)
- Klik op `opslaan



![paypal](assets/fr/008.webp)



**Noot:** U moet een zakelijke PayPal-rekening hebben om generate te kunnen gebruiken. U kunt ze verkrijgen via de portal [ontwikkelaar] (https://developer.paypal.com)



### SumUp



De software integreert nu de **SumUp** betaaloplossing, waardoor u eenvoudig, veilig en efficiënt creditcardbetalingen kunt accepteren. Om van deze functionaliteit te kunnen profiteren, is een eerste configuratie vereist. Hieronder vindt u de te volgen stappen, genummerd voor een duidelijke en geleidelijke implementatie:





- Begin met het invoeren van uw **API Key**, een vertrouwelijke sleutel die door SumUp is verstrekt toen u uw ontwikkelaarsaccount aanmaakte. Hiermee wordt een veilige verbinding tot stand gebracht tussen uw SumUp account en de software.
- Vul het `Merchant Code` veld in met de unieke code die uw bedrijf identificeert binnen het SumUp platform. Deze code is essentieel voor het koppelen van transacties aan uw bedrijf.
- Kies in het veld `Currency` de hoofdvaluta die je gebruikt voor je transacties (bijv. **EUR**, **USD**, **CDF**, etc.).
- Zodra alle velden correct zijn ingevuld, klikt u op de knop `Opslaan` om uw instellingen op te slaan. Het systeem zal dan de koppeling met uw SumUp account tot stand brengen en uw software is klaar om betalingen te accepteren.



![payment-sumup](assets/fr/009.webp)



Na deze configuratie zal de **SumUp** integratie actief en operationeel zijn, waardoor u snel kunt uitbetalen en uw transacties direct vanuit de software kunt volgen.



### Streep



be-BOP biedt ook volledige integratie met **Stripe**, een van de populairste platforms voor online betalingen. Met Stripe kunt u online betalingen accepteren via creditcard, digitale Wallet en verschillende andere betaalmethoden. Zo activeert u het:





- Voer de **geheime sleutel** in die is opgegeven in het Stripe dashboard.
- Vul het **Public Key** veld in, ook geleverd door Stripe.
- Selecteer de **hoofdvaluta**.
- Sla de configuratie op en klik vervolgens op `Opslaan`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Let op:** Het is van essentieel belang om het btw-stelsel te kennen dat van toepassing is op uw activiteit (bijvoorbeeld: verkoop met btw in het land van de verkoper, vrijstelling met rechtvaardiging of verkoop tegen het btw-tarief van het land van de koper) om de factureringsopties in **be-BOP** correct te configureren.



## Valuta-configuratie



**be-BOP** biedt geavanceerd valutabeheer en is aangepast aan omgevingen met meerdere valuta en specifieke boekhoudvereisten. Om consistentie in financiële operaties en rapportage te garanderen, is het essentieel om de verschillende valuta's die in het systeem worden gebruikt op de juiste manier te configureren. Hier volgen de stappen voor deze configuratie:





- Selecteer de **hoofdvaluta** (`hoofdvaluta`)
- Selecteer `secundaire valuta
- Definieer **referentievaluta** (`Prijsreferentievaluta`)
- Vermeld `Boekhoudkundige valuta



Zodra alle valuta's correct zijn geconfigureerd, zorgt de software voor automatische en nauwkeurige conversie van transacties in meerdere valuta's, terwijl de boekhoudkundige consistentie strikt wordt gehandhaafd.



![settings-currencies](assets/fr/011.webp)



## Configuratie van hersteltoegang via e-mail of Nostr



Nog steeds in `/admin/settings`, via de **ARM** module, zorg ervoor dat het super-admin account een **email Address** of een **recovery pub** bevat, om de procedure te vergemakkelijken als je je wachtwoord vergeten bent.



![settings-users](assets/fr/012.webp)



## Taalinstellingen



De software biedt meertalige mogelijkheden om zich aan te passen aan een internationaal publiek en de gebruikerservaring te verbeteren. Om de meertalige functionaliteit te activeren, is het belangrijk om de beschikbare talen te configureren en een **standaardtaal** te definiëren.



![settings-languages](assets/fr/13.webp)



## Interface en identiteitsconfiguratie in be-BOP



**be-BOP** biedt ontwerpers alle hulpmiddelen die ze nodig hebben om een website te ontwerpen. De eerste stap is het openen van de `/Admin > Merch > Layout` sectie in de instellingen. Begin met het configureren van de **Top Bar**, de **Navbar** en de **Footer**.



### Le Top Bar



Met de configuratie **Top Bar** kun je de visuele identiteit van je software personaliseren door belangrijke informatie direct op de eerste regel van de Interface weer te geven. Dit versterkt de merkherkenning en biedt gebruikers een duidelijke context.



#### Configuratiestappen:





- Voer in het veld `merknaam` de naam van je bedrijf, organisatie of product in. Deze naam verschijnt bovenaan de Interface en vertegenwoordigt je belangrijkste visuele identiteit.
- Vermeld de websitetitel**: de gekozen titel moet het doel van het platform samenvatten. Deze titel kan in de header of in het browsertabblad verschijnen.
- Website beschrijving toevoegen**: hier kun je een korte beschrijving van je initiatief invoeren. Deze beschrijving helpt bij het contextualiseren van de tool voor gebruikers en kan ook worden gebruikt voor SEO-doeleinden.



Zodra deze informatie is ingevoerd, wordt in de **Top Bar** een duidelijke, professionele en samenhangende presentatie van uw oplossing weergegeven.



#### Koppelingen in de bovenste balk



Met de sectie `Links` van de Topbalk kunt u snelkoppelingen toevoegen naar belangrijke pagina's in uw applicatie of op externe sites. Deze links worden direct in de bovenbalk weergegeven en bieden je gebruikers snelle, gestructureerde toegang.



#### Configuratiestappen:





- Linknaam invoeren (Tekst)**: voer in het veld `Tekst` de naam of het label van de link in zoals deze zal verschijnen (bijv. Home, Contact, Help...).
- Link Address (Url)** aangeven: voer in het `Url` veld de volledige Address van de doelpagina in (intern of extern).
- Voeg indien nodig andere links toe**: in elke configuratieregel kun je een extra link toevoegen met de velden `Tekst` en `Url`.
- Links opslaan**: zodra alle links zijn ingevoerd, klik je op de knop "Link toevoegen aan bovenbalk" om ze op te slaan.



Met deze configuratie kunt u duidelijke, vloeiende en toegankelijke navigatie bieden door de verschillende secties van uw website of naar aanvullende bronnen.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



In de **Navbar** kunt u het hoofdnavigatiemenu van uw be-BOP configureren, dat meestal aan de zijkant of bovenkant van de Interface staat. Dit menu leidt gebruikers naar de verschillende pagina's en functies van de toepassing. De linkconfiguratie is eenvoudig en intuïtief. Zo werkt het:





- Linknaam invoeren (`Tekst`)**: begin op de configuratieregel met het invullen van het veld `Tekst`. Dit komt overeen met de naam van de link die wordt weergegeven in de navigatiebalk (voorbeelden: *Dashboard*, *Gebruikers*, *Instellingen*...).
- Voer de link Address (`Url`)** in: naast het `Tekst` veld staat het `Url` veld. Voer in dit veld de Address in van de pagina waarnaar de link moet verwijzen. Dit kan een interne route zijn of een link naar een externe pagina.
- Voeg meerdere links toe indien nodig**: onder de eerste regel zijn nieuwe `Tekst` en `Url` velden beschikbaar voor het toevoegen van zoveel links als nodig. Elke regel vertegenwoordigt een extra navigatielink.
- Links opslaan**: als je alle Elements hebt ingevoerd, klik je op de knop `Navellink toevoegen` om de resultaten op te slaan en weer te geven in de navigatiebalk.



Deze configuratie zorgt voor een efficiënte structurering van de toegang tot verschillende onderdelen van de software, waardoor de ergonomie en de gebruikerservaring verbeteren.



![navbar](assets/fr/015.webp)



### De voettekst



In de **Voetregel** kun je de voettekst van je software aanpassen door nuttige informatie of links toe te voegen. Voordat je de links configureert, moet je eerst een specifieke optie activeren:





- De weergave van het label "Powered by be-BOP"** inschakelen: activeer de knop `Display Powered by be-BOP` om dit label in de voettekst weer te geven.
- Voer de naam van de link in (`Tekst`)**: vul het `Tekst` veld in, dat overeenkomt met de tekst van de link in de voettekst (voorbeelden: *Voorwaarden*, *Privacy*, *Contact*...).
- Link Address aangeven (`Url`)**: voer in het veld `Url` de Address van de doelpagina in (intern of extern).
- Voeg indien nodig meer links toe**: gebruik de extra regels om zoveel links te maken als je wilt.
- Links opslaan**: klik op de knop "Voettekstlink toevoegen" om links op te slaan.



![footer](assets/fr/016.webp)



### Visuele personalisatie



**⚠️ Vergeet niet de logo's voor de lichte en donkere thema's in te stellen, evenals de favicon, via** `Admin > Merch > Afbeeldingen`.



Zo pas je het uiterlijk en de sfeer van je site aan:



#### Ga naar het gedeelte Foto's



Menu `Admin` > `Merch` > `Foto's`.



#### Een nieuwe afbeelding toevoegen



Klik op `New Picture`.



#### Selecteer een lokaal bestand



Klik op `Kies bestanden` en selecteer een image van je Hard schijf.



#### Selecteer het bestand dat u wilt importeren



Dubbelklik op de afbeelding die moet worden geïmporteerd (licht logo, donker logo of favicon).



#### De afbeelding een naam geven



Vul het veld `Naam van de afbeelding` in.



#### Afbeelding toevoegen



Klik op `Toevoegen` om het importeren af te ronden.



![pictures](assets/fr/017.webp)



### Identiteit verkoper instellen



#### Identiteit instellingen



Dit gedeelte is toegankelijk via `Admin > Identity` (of `Settings > Identity`) en laat je de administratieve en juridische informatie van je bedrijf configureren.



#### Juridische informatie





- Bedrijfsnaam**: officiële bedrijfsnaam.
- Bedrijfs-ID**: wettelijke identificatiecode of registratienummer (RCCM, SIRET...).



#### Bedrijf Address





- Straat**: post Address (straat, nummer...).
- Land**: land.
- Staat**: provincie of regio.
- Stad**: city.
- Postcode**: postcode.



#### Contactgegevens





- E-mail**: professionele e-mail Address.
- Telefoon**: telefoonnummer bedrijf.



#### Bankrekening





- Naam rekeninghouder**: naam van de rekeninghouder.
- Rekeninghouder Address**: Address van de houder.
- IBAN**: Internationaal bankrekeningnummer.
- BIC**: SWIFT/BIC code.



![bank-account](assets/fr/019.webp)



#### Facturering





- Klik op `Vul met hoofdwinkelgegevens` om de gegevens vooraf in te vullen.
- Issuer information Very-top-right**: veld voor juridische/fiscale informatie zichtbaar op facturen.
- Klik op `Update` om de wijzigingen op te slaan.



**Noot:** je kunt ook extra informatie invoeren die op de Invoice moet worden weergegeven, afhankelijk van je behoeften.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Fysieke winkel Address



Voor degenen met een fysieke winkel, voeg een specifieke volledige Address toe in `Admin > Instellingen > Identiteit` of een speciale sectie. Hierdoor kan het worden weergegeven op officiële documenten en in de voettekst indien nodig.



![seller-id](assets/fr/021.webp)



## Productbeheer



### Een nieuw product maken



Ga naar `Admin > Merch > Producten` om een product toe te voegen of te wijzigen. Vul de volgende velden in:



#### Basisinformatie





- Productnaam**: naam van het product (bijv. *BOP T-shirt limited edition*).
- Slug**: URL-identifier zonder spaties (bijvoorbeeld `tshirt-bop-edition-limitee`).
- Alias** *(optioneel)*: handig om snel toe te voegen aan het winkelmandje via een speciaal veld.



![product-config](assets/fr/028.webp)



#### Prijzen





- Prijsbedrag**: productprijs (bijv. `25,00`).
- Prijsvaluta**: valuta (EUR, USD, BTC, enz.).
- Speciale producten**:
  - dit is een gratis product.
  - dit is een betaal-wat-je-wilt product.



#### Productopties





- Enkelvoudig product (`standalone`)**: slechts één toevoeging mogelijk per bestelling (bijv. donatie, toegangsbewijs).
- Product met variaties**:
  - Controleer `Standalone` niet.
  - Vink `Product heeft lichte variaties (geen voorraadverschil)` aan.
  - Toevoegen:
    - Naam** (bijv. *Grootte*),
    - Waarden** (bijv.: S, M, L, XL),
    - Prijsverschillen** indien van toepassing (bijv.: `+2 USD` voor XL).



![product-details](assets/fr/029.webp)



## Voorraadbeheer



### Geavanceerde opties bij het maken van een product (Voorraad, Levering, Tickets, enz.)



#### Product met beperkte voorraad



Als je product niet in onbeperkte hoeveelheden beschikbaar is, vink dan `Het product heeft een beperkte voorraad` aan. Dit activeert het automatisch bijhouden van de resterende hoeveelheden. Zodra dit vakje is aangevinkt, verschijnt er een veld om de **beschikbare voorraad** aan te geven.



Het systeem beheert:





- Gereserveerde voorraad** → nog niet betaalde producten in manden
- Verkochte voorraad** → reeds gekochte producten



**Reserveringstijd winkelmandje**: Wanneer een klant een product toevoegt aan zijn winkelmandje, wordt het "gereserveerd" voor een beperkte tijd. U kunt deze tijd aanpassen in: `Admin > Config > Winkelwagenreservering` (waarde in minuten)



#### Product dat moet worden geleverd?



Vink `Het product heeft een fysieke component die naar de Address van de klant wordt verzonden` aan. Dit is handig voor alle producten die fysiek worden verzonden (boeken, t-shirts, etc.)



#### Andere opties





- Ticket**: vink aan als het product een ticket voor een evenement is
- Reservering**: controleer of dit een reserveringsslot is (bijv.: sessie, afspraak)



![product-options](assets/fr/030.webp)



### Actie-instellingen (onder)



Dit gedeelte bepaalt **waar** en **hoe** het product kan worden bekeken en gekocht:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Vink alleen de kanalen aan die je wilt gebruiken.



## CMS-pagina's en widgets maken en aanpassen



### Verplichte CMS pagina's



Ga naar `Admin > Merch > CMS`. Je ziet een lijst met bestaande pagina's en kunt nieuwe toevoegen met **Voeg CMS pagina toe**.



CMS pagina's zijn belangrijk voor:





- Informeer je bezoekers (bijv. gebruiksvoorwaarden)
- Voldoen aan de wet (bijv. privacybeleid)
- Bepaalde winkeleigenschappen uitleggen (bijv. IP-verzameling, 0% btw)



Je kunt naar wens andere pagina's toevoegen:





- Over ons / Wie we zijn
- Steun ons / Donaties
- FAQ
- Neem contact op met
- enz.



**Tip: Klik op elke link of icoon om de **inhoud**, **titel** of **zichtbaarheid** van elke pagina aan te passen.



### Lay-out en grafische Elements



Ga naar: `Admin > Merch > Layout`. Je kunt de visuele Elements van je site aanpassen:



![product-options](assets/fr/032.webp)



#### Bovenste balk





- Links wijzigen of verwijderen (bijv. HOME, OVER ONS,...)
- Navigatie tussen belangrijke secties van de site



#### Navbar (hoofdnavigatiebalk)





- Aanwezig in het grijze gebied onder de bovenste balk
- Bevat snelle toegang tot: `Config`, `Betalingsinstellingen`, `Transactie`, `Node Beheer`, `Widgets`, enz.
- Alleen bestuurders



#### Voettekst





- Bewerkbaar vanuit `Admin > Merch > Layout`
- Bevat: contactinformatie, nuttige links, wettelijke kennisgevingen...



#### Visuals aanpassen



Ga naar: `Admin > Merch > Afbeeldingen`



U kunt:





- Wijzig het **hoofdlogo**
- Opmaak wijzigen of toevoegen **afbeeldingen**



#### Beschrijving



Ook aanpasbaar in `Foto's`, hiermee kun je een **samenvatting of slogan** weergeven in de kop- of voettekst, afhankelijk van het thema.



**Noot:** hiermee kun je het uiterlijk aanpassen aan je merkidentiteit (educatief, commercieel of community).



### Widgets integreren in CMS pagina's



Widgets** verrijken je CMS-pagina's met dynamische of visuele Elements.



#### Widgets maken



Ga naar: `Admin > Widgets`



Voorbeelden van beschikbare widgets:





- Uitdagingen**: uitdagingen of missies
- Tags**: categorieën of trefwoorden
- Schuifbalken**: afbeeldingscarrousels
- Specificaties**: Specificaties tabellen
- Formulieren**: formulieren (contact, feedback, enz.)
- Countdowns**: timers
- Galerijen**: afbeeldingsgalerijen
- Leaderboards**: klassementen van gebruikers



![widgets](assets/fr/033.webp)



#### Integratie in CMS pagina's



Gebruik **shortcodes** in de inhoud van uw CMS pagina's:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Huidige parameters**:





- `slug`: unieke widget identifier
- `display=img-1`: productspecifieke afbeelding
- `breedte`, `hoogte`, `fit`: afbeeldingsafmetingen en -stijl
- autoplay=3000`: tijd in ms tussen twee dia's



**Voordelen**:





- Eenvoudig invoegen (kopiëren en plakken)
- Dynamisch: elke wijziging aan de widget wordt automatisch gereflecteerd
- Geen ontwikkelaar nodig



## Orderbeheer en rapportage



### Bestelling volgen



Om bestellingen uit het verleden te bekijken en te beheren, gaat u naar: `Admin > Transactie > Bestellingen`



Hier vindt u de **volledige lijst van bestellingen** die op uw site zijn geplaatst.



![orders](assets/fr/034.webp)



#### Visualisatie en zoeken



Met de Interface kun je bestellingen zoeken en filteren op verschillende criteria:





- bestelnummer: bestelnummer
- product alias: product identificatie of naam
- betalingsmiddel": gebruikte betalingsmethode (kaart, crypto, enz.)
- `Email`: e-mailadres van de klant



Met deze filters kun je snel zoeken en gericht beheren.



#### Details van elke bestelling



Door op een bestelling te klikken, krijg je toegang tot een compleet bestand met:





- Bestelde producten
- Informatie voor klanten
- Levering Address (indien van toepassing)
- Eventuele notities bij de bestelling



#### Mogelijke acties op een order



U kunt:





- Bestelling bevestigen (indien in behandeling)
- Een bestelling annuleren (bij een probleem of een verzoek van een klant)
- **labels** toevoegen (voor interne organisatie)
- Raadpleeg / voeg **interne notities** toe



**Opmerking:** Dit onderdeel is essentieel voor een goede logistiek en klantrelatie.



### Rapportage en export



Verkoop- en betalingsstatistieken bekijken:


beheerder > Instellingen > Rapportage



![reporting](assets/fr/035.webp)



Hier vind je een overzicht van je bedrijf in de vorm van **maandelijkse en jaarlijkse rapporten**.



#### Inhoud rapporteren



De rapporten zijn onderverdeeld in secties:





- Order Detail**: aantal orders, status (bevestigd, geannuleerd, in behandeling), evolutie
- Productgegevens**: verkochte producten, hoeveelheden, populaire producten
- Detail betalingen**: geïnde bedragen, uitsplitsing naar betalingsmethode



#### Gegevensexport



Elke sectie bevat een knop **Export CSV**, waarmee je:





- Gegevens downloaden in CSV-formaat
- Open ze in Excel, Google Sheets, enz.
- Archivering voor administratief of boekhoudkundig gebruik
- Gebruik ze voor interne rapporten



**Aantekening:** ideaal voor het bijhouden van prestaties, boekhouding en presentaties.



## Nostr Messaging configuratie (optioneel)



![nostr-config](assets/fr/036.webp)



Het platform ondersteunt het **Nostr** protocol voor bepaalde geavanceerde functies:





- Gedecentraliseerde meldingen
- Inloggen zonder wachtwoord
- Interface lichte administratie



### De privésleutel van Nostr genereren en toevoegen



Ga naar:


admin > Nodebeheer > Nostr





- Klik op **Creëer nsec** als je er nog geen hebt.
- Het systeem kan generate automatisch uitvoeren.
- Je kunt ook een bestaande sleutel gebruiken (bijvoorbeeld van Damus of Amethyst).



Volgende:





- Kopieer de `nsec` sleutel
- Voeg het toe aan je `.env.local` (of `.env`) bestand: ```env NOSTR_PRIVATE_KEY=UwNsecIciKey



### Functies geactiveerd met Nostr



Eenmaal geconfigureerd zijn er verschillende functies beschikbaar:



**Meldingen via Nostr**





- Waarschuwingen versturen voor bestellingen, betalingen of systeemgebeurtenissen
- Voor beheerders of gebruikers



**Interface lichte administratie**





- Toegankelijk via een Nostr-client
- Maakt snel, mobiel beheer mogelijk



**Connectie zonder wachtwoord**





- Inloggen via beveiligde link (verzonden via Nostr)
- Meer veiligheid en soepelheid voor de gebruiker



## Ontwerp en thema-aanpassing



Om het uiterlijk van je winkel aan te passen aan je grafische charter, ga je naar: `Admin > Merch > Thema`



Hier vindt u alle opties voor het **maken** en **configureren** van een aangepast thema.



### Een thema maken



![theme](assets/fr/037.webp)



Bij het maken of wijzigen van een thema kun je:





- Kleuren**: voor knoppen, achtergronden, tekst, links, enz.
- Lettertypen**: keuze uit lettertypen voor titels, paragrafen, menu's
- Grafische stijlen**: randen, marges, spatiëring, blokvormen



### Aanpasbare secties



Elk deel van de site kan onafhankelijk worden aangepast:





- Koptekst**: bovenste navigatiebalk
- Body**: hoofdinhoud
- Footer**: onderaan de pagina



**Noot:** deze granulariteit zorgt voor consistentie tussen de visuals van de site en de identiteit van je merk.



### Thema activering



Zodra het thema is geconfigureerd:





- Klik op **Opslaan**
- Activeer het als het **hoofdthema** van de winkel



**Let op:** het actieve thema is het thema dat zichtbaar is voor bezoekers.



## E-mailsjablonen configureren



Met het platform kun je de e-mails personaliseren die automatisch naar gebruikers worden verzonden. Ga naar: `Admin > Instellingen > Sjablonen`



![emails-templates](assets/fr/038.webp)



### Sjablonen maken/bewerken



Elke e-mail (orderbevestiging, vergeten wachtwoord, enz.) heeft:





- Onderwerp**: het onderwerp van de e-mail (bijv. "Uw bestelling is gevalideerd")
- HTML-lichaam**: HTML-inhoud die in de e-mail wordt weergegeven



**Noot:** je kunt naar wens tekst, afbeeldingen, links, enz. invoegen.



### Dynamische variabelen gebruiken



Om e-mails dynamisch te maken, voegt u variabelen in zoals:





- `{orderNumber}}`: vervangen door het werkelijke ordernummer
- `{invoiceLink}}`: link naar de Invoice
- `{websiteLink}}`: URL van uw website



**Noot:** deze tags worden automatisch vervangen wanneer ze worden verzonden.



### Tips voor gevorderden





- Maak e-mails die **responsief** zijn, zodat ze gemakkelijk gelezen kunnen worden op mobiele apparaten
- **Actieknoppen** toevoegen (betalen, downloaden, bestelling volgen)
- Test je e-mails door ze naar jezelf te sturen voordat je ze publiceert



## Specifieke tags en widgets configureren



### Tag beheer



Tags kunnen worden gebruikt om je inhoud te structureren en te verrijken. Om ze te openen: `Admin > Widgets > Tag`



![tags-config](assets/fr/039.webp)



### Een tag maken



Vul de volgende velden in:





- Tagnaam**: weergegeven tagnaam
- Slug**: unieke identificatie (geen spaties of accenten)
- Tag Family**: groepeert tags per categorie



![targsconfig](assets/fr/040.webp)



#### Beschikbare gezinnen:





- scheppers`: auteurs of producenten
- detailhandelaren: verkopers of verkooppunten
- tijdelijk`: perioden of data
- gebeurtenissen: geassocieerde gebeurtenissen



### Optionele velden



Deze velden kunnen worden gebruikt om een tag te verrijken alsof het een inhoudspagina is:





- Titel
- Ondertitel
- Korte** inhoud
- Volledige inhoud** (in het Frans)
- CTA's** (actieknoppen)



### Tags gebruiken



Tags kunnen zijn:





- Toegewezen aan producten
- Geïntegreerd in CMS pagina's met een tag: [Tag=slug?display=var-1]



## Configuratie van downloadbare bestanden



Om downloadbare documenten aan te bieden aan uw klanten: `Admin > Merch > Bestanden`



### Een bestand toevoegen



1. Klik op **Nieuw bestand**


2. Inform:




   - Bestandsnaam** (bijv. *Installatiegids*)
   - Te uploaden bestand** (PDF, afbeelding, Word...)



**Noot:** zodra toegevoegd, genereert het platform automatisch een **permanente link**.



### De link gebruiken



Deze link kan vervolgens worden ingevoegd in:





- CMS** pagina (als tekstlink of knop)
- Een **e-mailclient** (via een sjabloon)
- Een **productblad** (bijvoorbeeld een handleiding downloaden)



Het is ideaal voor het leveren van *gebruikershandleidingen, technische handleidingen, productbladen...* zonder dat externe hosting nodig is.



## Nostr-bot



Het platform biedt geavanceerde integratie met het **Nostr** protocol, via een geautomatiseerde bot.



Ga naar: knooppunt Beheer > Nostr



### Belangrijkste kenmerken



#### Beheer van relais





- **relays** die door de bot worden gebruikt toevoegen of verwijderen
- Optimaliseer het **bereik** en de **betrouwbaarheid** van verzonden berichten



#### Automatisch introductiebericht





- Activeer een automatisch bericht bij **eerste gebruikersinteractie**
- Ideaal voor:
  - Je service presenteren
  - Stuur een nuttige link (bijv. FAQ, contact, bestelling)



#### Certificering van uw `npub





- Voeg een **logo** en een **publieke naam** toe
- Link naar een **geverifieerd webdomein**
- Vergroot de geloofwaardigheid en herkenbaarheid van uw Nostr-identiteit



### Nostr-bot gebruikssituaties





- **bestellingsbevestigingen** naar u verzenden
- Automatisch reageren op **gebeurtenissen (bijv. nieuwe bestelling)**
- Een **centrale interactie met klanten** creëren



## Overbelasting van vertaallabels



be-BOP is meertalig (FR, EN, ES...), maar u kunt de vertalingen aanpassen aan uw behoeften.



Ga hiervoor naar: `Instellingen > Taal`



### Laden en bewerken



Vertaalbestanden zijn in JSON. Je kunt:





- Download** taalbestanden
- Bestaande teksten wijzigen**
- Je eigen vertalingen toevoegen**



Link naar originele bestanden:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Voorbeeld:** vervang `Toevoegen aan winkelwagentje` door `Ajouter au panier` of `Acheter`.



## Teamwork & verkooppunt (POS)



### Beheer van gebruikers- en toegangsrechten



#### Rollen maken



Ga naar: `Admin > Instellingen > ARM`



Klik op **Een rol aanmaken** om een rol aan te maken (bijvoorbeeld `Super Admin`, `POS`, `Ticketcontroleur`).



Elke rol bevat:





- schrijftoegang**: schrijftoegang
- leestoegang**: leestoegang
- verboden toegang**: secties interdites



#### Gebruiker aanmaken



Voeg in hetzelfde menu `Admin > Instellingen > ARM` een gebruiker toe met:





- inloggen
- alias
- e-mail herstel
- (optioneel) `recovery npub` voor verbinding via Nostr



Een eerder gedefinieerde rol toewijzen.



![pos-users](assets/fr/045.webp)



Alleen-lezen** gebruikers zien menu's in *italic* en kunnen de inhoud niet wijzigen.



## POS-configuratie (Point of Sale)



### De POS-rol toewijzen



Om een gebruiker toegang te geven tot het POS, wijs je de rol `Point of Sale (POS)` toe in: `Admin > Config > ARM`



Hij kan verbinding maken via de beveiligde URL: `/pos` of `/pos/touch`



### POS-specifieke functies



Be-BOP biedt een Interface gewijd aan fysieke verkoop (winkel, evenement, enz.).



#### Snelle toevoeging via alias



In `/cart` kun je met een veld een product toevoegen:





- Door het scannen van een **barcode** (ISBN, EAN13)
- Door handmatig een **product alias** in te voeren



**Noot:** het product wordt automatisch toegevoegd aan het winkelmandje.



#### Wijze van betaling



POS ondersteunt:





- Soorten
- Creditcard
- Lightning Network (crypto)
- Andere volgens configuratie



Er zijn twee geavanceerde opties beschikbaar:





- BTW-vrijstelling**: van toepassing op rechtvaardiging (NGO's, buitenlanders...)
- Geschenkkorting**: uitzonderlijke korting met verplichte opmerking



#### Weergave aan clientzijde



De URL `/pos/session` is bedoeld voor een **secundair scherm** (HDMI, tablet...):



Poster:





- Producten in bewerking
- Totaal bedrag
- Wijze van betaling
- Toegepaste kortingen



**Noot:** de klant volgt de bestelling live, terwijl de verkoper deze registreert op `/pos`.



### Samenvatting POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Bedankt voor het aandachtig volgen van deze handleiding.