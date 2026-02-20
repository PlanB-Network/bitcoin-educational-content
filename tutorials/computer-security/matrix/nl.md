---
name: Matrix
description: Een handleiding voor het begrijpen, configureren en gebruiken van Matrix, het veilige, open en gedecentraliseerde communicatieplatform.
---

![cover](assets/cover.webp)



## Wat is Matrix?



Matrix is een **decentraal communicatieprotocol** dat is ontworpen om de uitwisseling van berichten, bestanden en audio/video-oproepen tussen gebruikers en applicaties mogelijk te maken, zonder afhankelijk te zijn van een centrale onderneming. In tegenstelling tot traditionele berichtenplatforms is Matrix een **open infrastructuur**, vergelijkbaar met e-mail: iedereen kan een server kiezen of er zelf een beheren, terwijl de mogelijkheid om met de rest van het netwerk uit te wisselen behouden blijft.



Matrix onderscheidt zich door drie fundamentele principes:



### Een protocol, geen toepassing



Matrix is geen applicatie zoals WhatsApp of Telegram.


Het is een gestandaardiseerde taal die veel applicaties kunnen gebruiken.


Met andere woorden, een grote verscheidenheid aan Element-software, FluffyChat, Cinny, Nheko en anderen, bieden toegang tot hetzelfde Matrix-netwerk.



Dit garandeert totale vrijheid: verandering van toepassing zonder verlies van contacten, diversiteit van interfaces, onafhankelijkheid van één leverancier.



![capture](assets/fr/03.webp)



### Een gedecentraliseerd, gefedereerd netwerk



De structuur van Matrix is gebaseerd op **federatie**, een model waarin meerdere onafhankelijke servers met elkaar samenwerken.


Elke server (genaamd _homeserver_) kan gebruikers en chatrooms hosten en berichten synchroniseren met andere servers op het netwerk.


Dus :





- geen enkele entiteit controleert het hele systeem;
- een server kan verdwijnen zonder de rest van het netwerk te beïnvloeden;
- elke organisatie of persoon kan zijn eigen ruimte beheren.



Dit model zorgt voor **hoge veerkracht** en weerspiegelt de waarden van technologische soevereiniteit.



![capture](assets/fr/03.webp)



### Een veilig, versleuteld systeem



Matrix ondersteunt **end-to-end-encryptie (E2EE)** voor privéuitwisselingen en versleutelde groepen.


Berichten kunnen alleen worden gelezen door deelnemers, niet door tussenliggende servers.


Deze aanpak maakt het mogelijk om te communiceren zonder de inhoud van uitwisselingen bloot te stellen aan een derde partij, met behoud van de transparantie van het protocol en de mogelijkheid om een eigen server te hosten.



![capture](assets/fr/05.webp)



### Unieke interoperabiliteit



Een van de belangrijkste troeven van Matrix is de mogelijkheid om als **brug tussen verschillende communicatiesystemen** te fungeren. Dankzij _bruggen_ is het mogelijk om :





- Telegram
- WhatsApp
- Signal
- Boodschapper
- Slack
- Discord
- IRC, XMPP, enz.



Dit maakt het mogelijk om gemeenschappen te verenigen die verspreid zijn over verschillende platformen, terwijl de controle over de infrastructuur behouden blijft.



![capture](assets/fr/06.webp)



## Hoe werkt Matrix?



In dit hoofdstuk wordt de interne structuur van het Matrix-netwerk gepresenteerd om te begrijpen hoe gebruikers, servers en toepassingen binnen dit gedecentraliseerde ecosysteem op elkaar inwerken. Matrix is gebaseerd op drie essentiële elementen: _homeservers_, identiteiten en _clients_ die worden gebruikt om te communiceren.



### Servers: homeservers



Matrix draait op onafhankelijke servers die _homeservers_ worden genoemd.


Elke homeserver beheert :





- de gebruikersaccounts die het host,
- privégesprekken en lounges waaraan deze gebruikers deelnemen,
- synchronisatie met andere netwerkservers.



Alle homeservers die zijn aangesloten op het Matrix-netwerk wisselen automatisch berichten en gebeurtenissen uit gedeelde huiskamers uit. Bijvoorbeeld:





- een gebruiker die is geregistreerd op server A kan chatten met een gebruiker op server B,
- een salon kan worden verspreid over tientallen servers,
- niemand heeft controle over een salon of een gemeenschap als geheel.



Dit model is zeer veerkrachtig en stelt elke organisatie of individu in staat om zijn eigen infrastructuur te beheren.



### Matrix herkenningstekens



Elke gebruiker heeft een unieke identificatie, **MXID** (_Matrix ID_) genaamd, die lijkt op een adres:



```bash
@nomdutilisateur:serveur.xyz
```



Het bestaat uit :





- een gebruikersnaam, voorafgegaan door **@**
- de naam van de server waarop de account is aangemaakt, voorafgegaan door **:**



Voorbeelden:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Deze identificatie maakt communicatie met elke andere Matrix-gebruiker mogelijk, ongeacht de server van herkomst.



### Matrix clients (toepassingen)



Als u Matrix wilt gebruiken, moet u verbinding maken met een toepassing genaamd **client Matrix**.



De bekendste zijn :





- Element (web, mobiel, desktop)
- FluffyChat (mobiel)
- Cinny (minimalistisch web/desktop)
- Nheko (bureaublad)



Deze toepassingen zijn slechts interfaces voor :





- om berichten te bekijken,
- tekst, afbeeldingen of bestanden verzenden,
- deel te nemen aan beurzen of deze te organiseren,
- audio-/videogesprekken voeren.



Alle applicaties communiceren met servers via hetzelfde gestandaardiseerde protocol.



### Kamers en privéberichten (DM)



In Matrix vinden uitwisselingen plaats in **kamers** :





- een kamer kan openbaar of privé zijn
- er kunnen twee mensen in of duizenden
- het kan worden gedeeld door meerdere servers
- het heeft een unieke identificatiecode die begint met **!**



Privéberichten zijn gewoon chatruimtes met twee deelnemers, vaak **DM (Direct Messages)** genoemd.



De synchronisatie van de salons vindt in realtime plaats tussen de deelnemende servers, wat zorgt voor een naadloze ervaring met behoud van decentralisatie.



## Waarom Matrix gebruiken?



Matrix is niet alleen een alternatief voor gecentraliseerde berichtensystemen: het is een technologie die voorziet in echte behoeften op het gebied van digitale soevereiniteit, beveiliging en interoperabiliteit. Er zijn veel redenen waarom steeds meer mensen, bedrijven en instellingen voor dit protocol kiezen om te communiceren.



### Krijg weer controle over je communicatie



De meeste berichtenplatforms werken volgens een gecentraliseerd model: één speler beheert servers, toegang, gegevens en gebruiksregels. Dit model impliceert een totale afhankelijkheid van de leverancier.


Matrix pakt het anders aan.


Iedereen kan kiezen waar hij zijn account wil hosten of zelfs zijn eigen server inzetten. Geen enkele entiteit is in de positie om een gebruiker te blokkeren, opdringerige identificatie te eisen of een beleidswijziging op te leggen.


Deze architectuur geeft autonomie terug aan zowel individuen als organisaties. Communicatie is niet langer gebaseerd op vertrouwen in een bedrijf, maar op een open, gedocumenteerd en controleerbaar protocol.



### Veilige, versleutelde communicatie



Matrix ondersteunt end-to-endencryptie voor privégesprekken en -groepen. Dit mechanisme zorgt ervoor dat alleen deelnemers berichten kunnen lezen, zelfs als deze via servers van derden in de federatie lopen.



Het protocol maakt gebruik van het Megolm/Olm-algoritme, dat speciaal is ontworpen om sterke beveiliging te bieden in gedistribueerde omgevingen met meerdere apparaten.



Dit maakt het mogelijk om :





- gevoelige gesprekken beschermen,
- onbevoegde toegang te voorkomen (zelfs vanaf de hostserver),
- vertrouwelijkheid op lange termijn te bewaren.



Encryptie is geen optie: het is een kernonderdeel van het protocol.



### Niet langer afhankelijk van één applicatie



Matrix is geen toepassing, maar een protocol.



Deze diversiteit aan klanten garandeert :





- een keuze aangepast aan individuele behoeften,
- de mogelijkheid om Matrix op elk type apparaat te gebruiken,
- geen afhankelijkheid van één software.



Als een klant ongeschikt is of niet langer wordt onderhouden, selecteer je gewoon een andere: de account blijft normaal functioneren.



### Federeren en verbinden van verschillende gemeenschappen



Federation zorgt ervoor dat verschillende servers samenwerken terwijl ze onafhankelijk worden beheerd.


Dus :





- een organisatie kan haar eigen homeserver beheren,
- individuen kunnen lid worden van openbare servers,
- kunnen allemaal met elkaar communiceren alsof ze op hetzelfde platform zitten.



Deze flexibiliteit maakt het mogelijk om communicatieruimtes te maken die aangepast zijn aan elke behoefte: teams, verenigingen, gemeenschappen, instellingen of open source projecten.



Matrix is vooral populair in technische kringen, activistische collectieven, onderzoekers, overheden en in toenemende mate in Bitcoin gemeenschappen.



### Unieke interoperabiliteit in het berichtenlandschap



Een van de belangrijkste troeven van Matrix is de mogelijkheid om uitwisselingen **uit te breiden** dankzij bruggen die :





- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- en vele andere platforms



Matrix wordt zo een verbindende laag voor communicatie die verschillende gemeenschappen samenbrengt die verspreid zijn over verschillende toepassingen.



Deze interoperabiliteit vermindert fragmentatie en vereenvoudigt samenwerking.



### Een vrij, open en duurzaam protocol



Het Matrix-protocol is volledig open source en transparant ontwikkeld.


Dit biedt verschillende voordelen:





- een voortdurende evolutie van de standaard,
- de mogelijkheid voor iedereen om de code te controleren,
- onafhankelijkheid van commerciële of politieke veranderingen,
- veerkracht op lange termijn.



In tegenstelling tot propriëtaire berichtensystemen hangt de toekomst van Matrix niet af van één bedrijf, maar van een wereldwijde gemeenschap en een open standaard.



## Hoe maak ik een Matrix-account?



Het aanmaken van een Matrix-account is eenvoudig en vereist geen technische vaardigheden. Gebruikers kunnen zich bij een bestaande server aanmelden, een login aanmaken en direct beginnen met chatten. In dit gedeelte worden de belangrijkste stappen beschreven.



### Kies een server (openbaar of privé)



Matrix is een federatief netwerk: er zijn talrijke servers (homeservers) die door verschillende organisaties, gemeenschappen of personen worden beheerd. De keuze van de server bepaalt alleen _waar_ het account wordt gehost, maar staat communicatie met het hele netwerk niet in de weg.


**Er zijn twee opties beschikbaar:**



### - Een openbare server gebruiken



Dit is de eenvoudigste oplossing.


Voorbeelden van populaire servers:





- _matrix.org_ (de bekendste)
- _envs.net_
- thematische community-servers (techniek, privacy, open source...)



Deze servers zijn geschikt voor beginnende gebruikers die zich snel willen registreren.



### - Een privéserver gebruiken



Ideaal voor :





- een organisatie,
- een gezin,
- een open source project,
- een werkteam,
- of voor soeverein, zelf gehost gebruik.



In dit geval moet iemand de server beheren (Synapse, Dendrite, Conduit...).


Welke server je ook kiest, gebruikers kunnen met elkaar praten dankzij federatie.



### Stap voor stap een account aanmaken



Aangezien Matrix een open protocol is, is het toegankelijk voor verschillende toepassingen.


Zoals hierboven beschreven bieden ze verschillende interfaces en functionaliteiten, afhankelijk van de vereisten:





- Element**: de meest complete client, beschikbaar op alle platforms.
- FluffyChat**: eenvoudig, modern en ideaal voor mobiele apparaten.
- Nheko**: lichtgewicht, ergonomische client voor pc's.
- SchildiChat**: Element-variant met ergonomische verbeteringen.
- NeoChat**: geïntegreerd in het KDE-ecosysteem.



De keuze van de client heeft geen invloed op de account: ze werken allemaal met elke Matrix-server.



### Klassieke stappen :





- Open de gekozen toepassing. In ons geval doen we dit met [Element](app.element.io).
- Selecteer "Een account aanmaken".



![cover-kali](assets/fr/10.webp)



Om het eenvoudig te houden, kun je een Matrix-account aanmaken via **Google, Facebook, Apple, GitHub of GitLab**. Deze services weten alleen dat hun account is gebruikt om toegang te krijgen tot Matrix: dit wordt een **sociale verbinding** genoemd.



Voor meer vertrouwelijkheid kun je je ook handmatig registreren door een **gebruikersnaam**, een **wachtwoord** en een **e-mailadres** te kiezen.



Afhankelijk van de gekozen server kan een **captcha** vereist zijn, evenals acceptatie van de **gebruiksvoorwaarden**.



Zodra de registratie is gevalideerd, wordt er een bevestigingse-mail verzonden.


Klik op de koppeling om je account te activeren en ga naar de webapplicatie (Element) om deel te nemen aan je eerste Matrix-gesprekken.



![cover-kali](assets/fr/11.webp)



Je hebt nu een account en gebruikt de webversie van Element.



## Voeg uw eerste contact toe



Als u met iemand op Matrix wilt communiceren, hoeft u alleen zijn volledige identificatiecode te weten, **Matrix ID** genaamd.



Voorbeeld:



`@alice:matrix.org @bened:monserveur.bj`



### Een contactpersoon toevoegen



Om vrienden uit te nodigen voor je groepschat, klik je op de `i` cirkel in de rechterbovenhoek. Dit opent het rechterpaneel. Klik op "Mensen" om de lijst met leden in deze kamer weer te geven: jullie zouden op dit moment de enige aanwezigen moeten zijn.



![cover-kali](assets/fr/12.webp)



Klik op 'Uitnodigen voor deze ruimte' boven aan de lijst met personen. Er wordt een prompt geopend waarmee je je vrienden kunt uitnodigen om zich bij jou in Matrix aan te sluiten. Als ze al zijn aangemeld bij Matrix, voer je hun Matrix-ID in. Als dat niet het geval is, voer je hun e-mailadres in en worden ze uitgenodigd.



Er is geen "vrienden"-systeem: een contact is gewoon een persoon met wie een gesprek is begonnen.



![cover-kali](assets/fr/13.webp)



De persoon die je hebt uitgenodigd kan de uitnodiging accepteren of weigeren. Als ze accepteren, zou je ze in de kamer moeten zien. Hoe meer, hoe beter!



![cover-kali](assets/fr/14.webp)



### Je eigen server opzetten



Matrix komt pas echt tot zijn recht in combinatie met een persoonlijke server.


Door je eigen homeserver te implementeren, kun je :





- volledige controle over gegevens behouden,
- zijn eigen gebruiksregels bepalen,
- meerdere accounts hosten (vrienden, team, community),
- en zorgen voor maximale veerkracht in het geval van beperkingen of censuur.



**Beschikbare oplossingen:**





- Synapse**: de historische en meest complete implementatie.
- Dendrite**: lichter, krachtiger en ontworpen voor de toekomst van het protocol.
- Conduit**: een minimalistische variant die eenvoudig te implementeren is.



**Vereisten:**





- een domeinnaam,
- een machine of een VPS,
- minimale vaardigheden op het gebied van systeembeheer.



Zelfs als het een beetje configuratie vereist, maakt het beheren van je eigen server Matrix tot een soevereine en duurzame tool.



### Deelnemen aan je eerste handelsbeurzen



Matrix leunt zwaar op _kamers_ (huiskamers).


Er zijn openbare, particuliere, gemeenschaps-, technische, lokale en internationale beurzen.



**Drie manieren om lid te worden van een salon:**



1. **Via een uitnodigingslink** (vaak in de vorm van een `matrix.to` URL).


2. **Zoek naar de naam van de salon** in de applicatie.


3. **Door het volledige show-ID** in te voeren, bijv:


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Eenmaal lid, gedraagt de chatroom zich als een klassieke nieuwsgroep, met geschiedenis, encryptie, bestanden, reacties en audio/video-oproepen, afhankelijk van de gebruikte client.



![capture](assets/fr/09.webp)



## Verder gaan



Als je de basis eenmaal onder de knie hebt, biedt Matrix een groot aantal geavanceerde mogelijkheden. Of je nu andere berichtensystemen wilt koppelen, je eigen server wilt hosten of een community wilt organiseren, het ecosysteem is zeer uitgebreid.



### Bruggen (WhatsApp, Telegram, Signal, enz.)



Een bridge verbindt Matrix met andere berichtensystemen.


Hiermee kun je berichten verzenden en ontvangen van :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Slap**
- IRC** (IRC)
- en vele anderen



### Wat bruggen kunnen doen





- Centraliseer al je gesprekken in Matrix
- Een open interface bieden voor interactie met bedrijfseigen diensten
- Beheer een multiplatform-community vanaf één locatie



Sommige bruggen zijn officieel, andere vanuit de gemeenschap.


Afhankelijk van de afdeling kunnen ze :





- een persoonlijke server,
- een extra configuratie,
- of het gebruik van een bestaande openbare brug.



### Matrix gebruiken voor een Bitcoin organisatie, gemeenschap of project



Matrix is niet alleen een persoonlijk hulpmiddel.


Het kan worden gebruikt om werkgroepen te structureren, lokale gemeenschappen te organiseren of projectcommunicatie te beheren.



**Gebruiksvoorbeelden:**





- Open-sourcegemeenschappen
- Bitcoin en Lightning ecosysteemprojecten
- Groepen studenten of ontwikkelaars
- Burgerorganisaties
- Onafhankelijke media
- Lokale groepen en verenigingen



**Waarom is dit interessant?





- 100% open-source** tool
- Soevereine en gedecentraliseerde** communicatie
- Ruimtes georganiseerd in **lounges**, **subgroepen**, **privélounges**, enz.
- Integreren met Nextcloud, GitLab, Mattermost of aangepaste bots
- Verfijnd beheer van machtigingen en moderatie



Matrix wordt dan een communicatiepijler voor elke structuur die onafhankelijk wil blijven van de grote gecentraliseerde platforms.



## Conclusie



Matrix is een moderne, open en veilige oplossing voor real-time communicatie en biedt een gedecentraliseerd alternatief voor traditionele platforms. Dankzij de federatieve architectuur en geavanceerde versleutelingsprotocollen behoudt de gebruiker de controle over zijn gegevens en geniet hij tegelijkertijd van een soepele, interoperabele ervaring. Of het nu gaat om persoonlijk, professioneel of gemeenschappelijk gebruik, Matrix biedt een robuust en schaalbaar kader voor het bouwen van communicatieomgevingen die zijn aangepast aan de hedendaagse behoeften.



Als je meer wilt weten en alle functies van Matrix wilt ontdekken, kun je de officiële documentatie hier raadplegen:


[https://matrix.org/docs/](https://matrix.org/docs/)