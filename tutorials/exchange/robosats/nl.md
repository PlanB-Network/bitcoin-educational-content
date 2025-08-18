---
name: Robosats

description: Hoe Robosats gebruiken
---

![cover](assets/cover.webp)


RoboSats (https://learn.robosats.com/) is een eenvoudige manier om Exchange Bitcoin voor nationale munteenheden privé te gebruiken. Het vereenvoudigt de peer-to-peer ervaring en maakt gebruik van lightning hold facturen om de vereisten voor bewaring en vertrouwen te minimaliseren.


![video](https://youtu.be/XW_wzRz_BDI)


## Gids


**Noot:** Deze gids is van Bitocin Q&A (https://bitcoiner.guide/robosats/). Alle eer aan hem, je kunt hem [hier] steunen (https://bitcoiner.guide/contribute); BitcoinQ&A is ook een Bitcoin mentor. Neem contact met hem op voor mentorschap!


![image](assets/0.webp)


RoboSats - Een eenvoudige en private Lightning-gebaseerde P2P Exchange


## Voordat u begint


### Dingen die je moet weten


| Jargon       | Definition                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Your automatically generated private trade identity. Do not re-use the same robot more than once as this can degrade your privacy.                                                             |
| Token        | A string of random characters used to generate your unique robot.                                                                                                                              |
| Maker        | A user who creates an offer to buy or sell Bitcoin.                                                                                                                                            |
| Taker        | A user who takes another user up on their offer to buy or sell Bitcoin.                                                                                                                        |
| Bond         | An amount of Bitcoin locked up by both peers as a pledge to play fair and complete their part of the trade. Bonds are typically 3% of the total trade amount and are powered by Hodl Invoices. |
| Trade Escrow | Used by the seller as a method of holding the trade amount of Bitcoin, again using Hodl Invoices.                                                                                              |
| Fees         | RoboSats charges 0.2% of the trade amount, which is split between both maker and taker. The taker pays 0.175% and the maker pays 0.025%.                                                       |

## Dingen die je moet hebben


### Een bliksem Wallet


RoboSats is Lightning native, dus je hebt een Lightning Wallet nodig om de obligatie te financieren en de gekochte Sats als koper te ontvangen. Je moet voorzichtig zijn bij het kiezen van je Wallet, want door de technologie die gebruikt wordt om RoboSats te laten functioneren, zijn ze niet allemaal compatibel.


Als je een node runner bent, is Zeus verreweg de beste optie. Als je geen eigen node hebt, raad ik je Phoenix aan, een cross-platform mobiele Wallet met eenvoudige installatie en toegang tot Lightning. Phoenix werd gebruikt bij de productie van deze gids.


### Sommige Bitcoin


Kopers en verkopers moeten een obligatie financieren voordat er een transactie kan plaatsvinden. Dit is meestal een heel klein bedrag (~3% van het handelsbedrag), maar het is niettemin een vereiste.


Gebruik je RoboSats om je eerste Sats te kopen? Waarom leen je een vriend niet het kleine bedrag dat nodig is om te beginnen? Als je alleen vliegt, zijn hier een paar andere goede opties om aan een paar noKYC Sats te komen om te beginnen.


### Toegang tot RoboSats


Uiteraard moet je toegang krijgen tot RoboSats! Er zijn vier manieren waarop je dit kunt doen:


1. Via Tor Browser (aanbevolen!)

2. Via een gewone webbrowser (Niet aanbevolen!)

3. Via de Android APK

4. Je eigen klant


Als je de Tor-browser nog niet kent, lees dan hier meer en download hem [hier](https://www.torproject.org/download/).


Een korte opmerking voor iOS-gebruikers die RoboSats via Tor vanaf hun telefoon willen benaderen. onion Browser' is geen Tor Browser. Gebruik in plaats daarvan Orbot + Safari en Orbot + DuckDuckGo.


## Bitcoin kopen


De volgende stappen werden uitgevoerd in mei 2023 met versie 0.5.0, benaderd via de Tor browser. De stappen zouden identiek moeten zijn voor gebruikers die RoboSats benaderen via de Android APK.


Op het moment van schrijven is RoboSats nog volop in ontwikkeling, dus de Interface kan in de toekomst wat veranderen, maar de basisstappen die nodig zijn om de handel te voltooien zouden grotendeels ongewijzigd moeten blijven.


**Noot:** wanneer je RoboSats voor het eerst laadt, krijg je deze landingspagina te zien. Klik op Start.


![image](assets/2.webp)


generate je token en bewaar deze ergens veilig, zoals een versleutelde notitie-app of wachtwoordmanager. Deze token kan worden gebruikt om je tijdelijke Robot ID terug te krijgen als je browser of app halverwege een transactie wordt afgesloten.


![image](assets/3.webp)


Maak kennis met je nieuwe Robot-identiteit en klik op Doorgaan.


![image](assets/4.webp)


Klik op Aanbiedingen om door het orderboek te bladeren. Bovenaan de pagina kun je vervolgens filteren op jouw voorkeuren. Let op de obligatiepercentages en de premie ten opzichte van het gemiddelde Exchange tarief.



- Kies 'Kopen
- Kies je valuta
- Kies je betaalmethode(s)


![image](assets/5.webp)


**Noot:** klik op de aanbieding die je wilt aannemen. Voer het bedrag in (in de door jou gekozen fiatvaluta) dat je van de verkoper wilt kopen, controleer vervolgens de details en klik op 'Bestelling opnemen'.


Als de verkoper niet online is (aangegeven met een rode stip op zijn profielfoto), zie je een waarschuwing dat de transactie langer kan duren dan normaal. Als je doorgaat en de verkoper gaat niet op tijd verder, krijg je 50% van het obligatiebedrag vergoed voor je verspilde tijd.


![image](assets/6.webp)


Vervolgens moet je je handelsobligatie vastzetten door de Invoice op het scherm te betalen. Dit is een Invoice die in je Wallet wordt bevroren. Het wordt alleen in rekening gebracht als je jouw deel van de handel niet voltooit.


![image](assets/7.webp)


Scan de QR-code in je Lightning Wallet en betaal de Invoice.


![image](assets/8.webp)


Maak vervolgens in je Bliksem Wallet generate een Invoice voor het getoonde bedrag en plak dit in de daarvoor bestemde ruimte.


![image](assets/9.webp)


Wacht tot de verkoper zijn handelsbedrag heeft vergrendeld. Wanneer dit gebeurt, gaat RoboSats automatisch naar de volgende stap waar het chatvenster wordt geopend. Zeg hallo en vraag de verkoper om zijn fiat betalingsinformatie. Eenmaal gegeven, stuur de betaling via de gekozen methode en bevestig dit in RoboSats. Alle chat in RoboSats is PGP gecodeerd, wat betekent dat alleen jij en je handelspartner de berichten kunnen lezen.


![image](assets/10.webp)


Zodra de verkoper de ontvangst van de betaling bevestigt, geeft RoboSats de betaling automatisch vrij met behulp van de eerder verstrekte Invoice.


![image](assets/11.webp)


Wanneer de Invoice is betaald, is de transactie voltooid en is je obligatie ontgrendeld. Je ziet dan een transactieoverzicht.


![image](assets/12.webp)


Controleer op je Lightning Wallet of de Sats zijn aangekomen.


![image](assets/13.webp)


## Extra functies


Naast het voor de hand liggende kopen en verkopen van Bitcoin, heeft RoboSats nog een paar andere functies waar je van op de hoogte moet zijn.

Robot Garage


Wil je meerdere transacties tegelijkertijd uitvoeren, maar wil je niet dezelfde identiteit delen? Geen probleem! Klik op de tab Robot, generate een extra Robot en maak of neem je volgende order.


![image](assets/14.webp)


### Orders maken


Je kunt niet alleen het aanbod van iemand anders aannemen, maar ook je eigen aanbod creëren en wachten tot een andere Robot naar je toe komt.



- Open de pagina Maken.
- Bepaal of u Bitcoin wilt kopen of verkopen.
- Voer het bedrag en de valuta in waarmee je wilt kopen/verkopen.
- Voer de betalingsmethode(s) in die je wilt gebruiken.
- Voer het percentage 'Premie boven marktprijs' in dat je bereid bent te accepteren. Merk op dat dit een negatief getal kan zijn om te bieden met een korting ten opzichte van de huidige marktprijs.
- Klik op Order maken.
- Betaal de Lightning Invoice om je Maker Bond te vergrendelen.
- Je bestelling staat nu live. Ga rustig zitten en wacht tot iemand je bestelling accepteert.


![image](assets/15.webp)


### On-Chain Uitbetalingen


RoboSats richt zich op Lightning, maar kopers hebben wel de optie om hun Sats te ontvangen op een On-Chain Bitcoin Address. Kopers kunnen deze optie selecteren nadat ze hun obligatie hebben vergrendeld. Na het selecteren van On-Chain krijgt de koper een overzicht van de kosten te zien. De extra kosten voor deze service omvatten:



- Een swapvergoeding geïnd door RoboSats - Deze vergoeding is dynamisch en verschuift afhankelijk van hoe druk het Bitcoin netwerk is.
- Een Mining vergoeding voor de uitbetalingstransactie - Dit is instelbaar door de koper.


![image](assets/16.webp)


### P2P Wissels


RoboSats stelt gebruikers in staat om de Sats in of uit hun Lightning Wallet te wisselen. Klik gewoon op de ruilknop bovenaan de aanbiedingenpagina om de huidige ruilaanbiedingen te bekijken.


Als koper van een 'Swap In'-aanbieding stuur je On-Chain Bitcoin naar de collega en ontvang je Sats terug, minus de geadverteerde vergoedingen en/of premies, naar je Lightning Wallet. Als koper van een 'Swap Out'-aanbieding, stuur je Sats via Lightning en ontvang je Bitcoin, minus eventuele vergoedingen en/of premies, naar je On-Chain Address. Gebruikers van Samourai of Sparrow wallet kunnen ook gebruikmaken van de verstekfunctie om een ruil te voltooien.


RoboSats swapaanbiedingen kunnen ook gepinde alternatieven voor Bitcoin bevatten, waaronder RBTC, LBTC en WBTC. Je moet uiterst voorzichtig zijn als je met deze tokens werkt, omdat ze allemaal verschillende nadelen hebben. Bitcoin is geen Bitcoin!


![image](assets/17.webp)


### Voer uw eigen RoboSats-client uit


Knooppuntbeheerders van Umbrel, Citadel en Start9 kunnen hun eigen RoboSats-client rechtstreeks op hun knooppunt installeren. De voordelen hiervan zijn



- Dramatisch snellere laadtijden.
- Veiliger: je bepaalt zelf welke RoboSats-clientapp je gebruikt.
- Krijg veilig toegang tot RoboSats vanaf elke browser/apparaat. Je hoeft TOR niet te gebruiken als je op je lokale netwerk zit of VPN gebruikt: je node backend zorgt voor de torificatie die nodig is voor anonimisering.
- Hiermee bepaal je met welke P2P marktcoördinator je verbinding maakt (standaard robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)


![image](assets/18.webp)


## FAQ


### Kan ik worden opgelicht?


Als je als koper de fiat hebt gestuurd die nodig is voor jouw deel van de handel, maar de verkoper geeft de Sats niet aan je vrij, dan kun je een geschil openen. Als je tijdens dit geschilproces aan de arbiters van RoboSats kunt bewijzen dat je de fiat hebt verzonden, worden de geblokkeerde fondsen en de handelsgarantie van de verkoper aan jou vrijgegeven.

Hoe annuleer ik een transactie?


Je kunt een transactie annuleren na het plaatsen van je obligatie door te klikken op de knop Samenwerken Annuleren in het transactiemenu. Als je handelspartner de transactie wil annuleren, zijn er geen kosten aan verbonden. Maar als je handelspartner de transactie wil voltooien en je gaat toch door en annuleert, dan ben je je transactieobligatie kwijt.


### Werkt RoboSats met betaalmethode 'X'?


Er zijn geen beperkingen op betaalmethoden in RoboSats. Als je geen aanbiedingen ziet in de door jou gewenste methode, maak dan je eigen aanbieding met deze methode!


![image](assets/19.webp)


### Wat leert RoboSats over mij als ik het gebruik?


Als je RoboSats gebruikt via Tor of de Android app, helemaal niets! Lees hier meer.



- Tor beschermt je netwerkprivacy.
- PGP-codering houdt je handelschat privé.
- Geen accounts betekent één Robot per transactie. Dit betekent dat RoboSats niet meerdere transacties kan correleren aan een enkele entiteit.


Er zijn echter enkele beperkingen! Lightning is redelijk privé als verzender, maar niet als ontvanger. Als u naar uw eigen Lightning-knooppunt ontvangt, wordt uw knooppunt-ID gedeeld in uw facturen. Dit knooppunt-ID geeft iedereen met kennis daarvan een startpunt om te proberen uw On-Chain activiteit te koppelen. Dit geldt ook als een gebruiker ervoor kiest om zijn handel via een On-Chain uitbetaling te ontvangen.


Om dit te beperken, kunnen gebruikers kiezen voor een oplossing zoals een Proxy Wallet voor Lightning of CoinJoin voor On-Chain.


### Federatie


Op dit moment is er één RoboSats-coördinator die wordt aangestuurd door het RoboSats-ontwikkelteam. In Bitcoin zorgt elke vorm van centralisatie voor een gemakkelijker doelwit voor overheden of regelgevers die misschien niet zo dol zijn op een specifieke dienst.


Omdat RoboSats een Open Source project is, kan iedereen de code overnemen en zijn eigen coördinator starten. Hoewel dit het risico enigszins wegneemt van een enkel doelwit, fragmenteert het ook een toch al dunne liquiditeitsmarkt.


Het RoboSats-team realiseert zich dit en is begonnen aan een gefedereerd model. Als eindgebruiker zou dit niet veel moeten veranderen aan de hierboven getoonde handelsstroom, maar er zullen extra weergaven of schermen ontstaan om verschillende coördinatoren toe te voegen of te verwijderen.


EINDE van gids

https://bitcoiner.guide/robosats/