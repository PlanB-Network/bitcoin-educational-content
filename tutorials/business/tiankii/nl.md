---
name: Tiankii
description: Bliksempakket met tools voor retailers en consumenten
---

![cover](assets/cover.webp)



In het Bitcoin ecosysteem blijft het een grote uitdaging voor bedrijven en particulieren om betalingen in realtime te accepteren. Traditionele oplossingen vereisen vaak geavanceerde technische kennis, een complexe infrastructuur om te onderhouden, of vereisen dat fondsen worden bewaard door tussenpersonen. Deze situatie belemmert de massale adoptie van Bitcoin als een alledaagse valuta, ondanks de belofte van de technologische vooruitgang van Lightning Network.



Tiankii, een Salvoriaans bedrijf geboren in 2021, reageert op dit probleem door een toegankelijke, modulaire Bitcoin infrastructuur aan te bieden. In plaats van de adoptie van een gesloten ecosysteem te forceren, biedt Tiankii een suite van onderling verbonden tools waarmee iedereen Bitcoin Lightning in zijn bedrijf kan integreren zonder de controle over zijn fondsen op te offeren.



## Wat is Tiankii?



### Oorsprong en filosofie



Tiankii - een Nahuatl term die "openluchtmarkt toegankelijk voor iedereen" betekent - is de eerste 100% Bitcoin start-up in El Salvador. Het bedrijf werd opgericht door Darvin Otero na de goedkeuring van Bitcoin als wettig betaalmiddel van het land en heeft als doel Bitcoin te transformeren van een opslagplaats van waarde tot een verhandelbare valuta voor dagelijkse aankopen. In tegenstelling tot custodial platforms, kiest Tiankii voor een niet-custodial benadering waarbij gebruikers de controle over hun fondsen behouden en de infrastructuur enkel dient als technische tussenpersoon.



### Technische architectuur



Tiankii is gepositioneerd als een aanbieder van Bitcoin-as-a-Service infrastructuur gebaseerd op Lightning Network. Deze second-layer technologie maakt bijna onmiddellijke transacties mogelijk met verwaarloosbare kosten, waardoor microbetalingen en alledaagse aankopen mogelijk worden.



De architectuur is gebaseerd op drie pijlers:



**Lightning-eerst**: Geef systematisch de voorkeur aan het Lightning-netwerk vanwege de snelheid en lagere kosten, met behoud van on-chain transactieondersteuning voor grote bedragen.



**Open standaarden**: Gebruik van LNURL om betalingsverzoeken te automatiseren, Lightning Address voor leesbare e-mail-ID's en Bolt Card voor interoperabele NFC-betalingen.



**wallet-agnostische modulariteit**: Mogelijkheid om verschillende Lightning portfolio's (LNbits, Blink, BlueWallet) of je eigen node aan te sluiten, wat maximale flexibiliteit biedt afhankelijk van het vereiste expertiseniveau en autonomie.



## Tiankii ecosysteem gereedschappen



### Bitcoin POS - Betaalterminal in winkels



De applicatie verandert een smartphone of tablet in een Lightning-terminal. De verkoper voert het bedrag in de lokale valuta in en de app genereert een Lightning QR-code of accepteert een Bolt-kaart. Transacties worden direct commissievrij gecrediteerd, met automatische conversies in meer dan 150 valuta, fooienbeheer en verkoopgeschiedenis.



### Merchant Dashboard - Uniform verkoopbeheer



Interface web gecentraliseerd om zijn wallet Lightning aan te sluiten, transacties in realtime te volgen, facturen uit te schrijven en generate boekhoudkundige rapporten op te stellen. Het platform voegt alle kanalen samen: betalingen in de winkel (POS), online verkoop (e-commerce plug-ins) of API integraties. Betalingen komen samen op de gekozen wallet.



### Bitcoin contactloze kaart (Bolt kaart)



De NFC Bolt kaart vertegenwoordigt Tiankii's belangrijkste innovatie in het democratiseren van Bitcoin voor het grote publiek. Met deze kaart, die werkt als een contactloze bankpas, kun je Bitcoin Lightning aankopen betalen door simpelweg op een compatibele terminal te tikken.



In tegenstelling tot traditionele bewaaroplossingen volgt deze kaart een open standaard die interoperabiliteit garandeert. Gebruikers kunnen de kaart koppelen aan hun eigen wallet via de IBI-applicatie, waardoor ze hun privésleutels en volledige controle over de bijbehorende fondsen behouden. Betaling duurt slechts een seconde, zonder dat je je smartphone hoeft te pakken of een actieve internetverbinding hoeft te hebben op het moment van betaling.



Deze oplossing is met name toegankelijk voor mensen die niet bekend zijn met smartphones en biedt een toegankelijke toegang tot de Bitcoin economie.



### IBI App - Interface individueel Bitcoin



De IBI-toepassing (Individueel Bitcoin Interface) is ontworpen voor particulieren die Bitcoin Lightning dagelijks willen gebruiken. Het belangrijkste voordeel ligt in het genereren van een gepersonaliseerde Address Lightning, een betalingsidentificatie die leesbaar is in e-mailformaat (voorbeeld: alice@ibi.me).



Deze identificatie vereenvoudigt de ontvangst van betalingen drastisch: de verzender hoeft niet voor elke transactie een nieuwe generate factuur te maken, maar kan gewoon het Lightning-adres invoeren. Met de interface kun je ook je Bolt-kaart beheren (activeren, deactiveren, uitgavenlimieten), verschillende Lightning-wallets koppelen en betalingen doen door QR-codes te scannen.



### Plugins voor e-commerce



Gebruiksklare integraties voor WooCommerce, Shopify en Cloudbeds. Installeert in enkele minuten om Bitcoin Lightning toe te voegen aan de kassa. Voordelen: geen commissie (vs. 2-3% creditcards), onmiddellijke verrekening, wereldwijde toegang, geen terugboekingen. Betalingen komen direct binnen op de aangesloten wallet van de verkoper.



### Bitcoin API en hulpmiddelen voor ontwikkelaars



De Tiankii SDK maakt het mogelijk om Bitcoin Lightning te integreren in bestaande applicaties zonder een eigen node te onderhouden. API handelt het aanmaken van facturen, betalingsverificatie en bulkmailings af via een robuuste infrastructuur die gehost wordt op Google Cloud. Command Center completeert het aanbod voor organisaties met Address Lightning op aangepaste domeinen, bulkbetalingen en gecentraliseerd beheer van NFC-terminals en -kaarten.



## Installatie en eerste stappen



### Essentiële voorwaarden



Het gebruik van Tiankii vereist geen complexe technische vereisten. De applicaties werken via een webbrowser op een smartphone, tablet of computer. Er is geen native applicatie-installatie nodig: alles wat je nodig hebt is internettoegang en een recente browser om toegang te krijgen tot IBI of het Merchant Dashboard.



**Voor privégebruikers (IBI App)**: Er is geen voorafgaande wallet Lightning nodig. Wanneer je een account aanmaakt, configureert Tiankii automatisch een werkende Address Lightning via de [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), een nodeloze implementatie die op de achtergrond gebruikmaakt van het Liquid netwerk. Je kunt onmiddellijk betalingen ontvangen en verzenden zonder enige technische configuratie. Deze oplossing vereenvoudigt de toegang voor beginners drastisch, terwijl het zelfbeveiligend blijft.



**Voor verkopers (Merchant Dashboard)** : De aansluiting van een bestaande wallet Lightning is verplicht om Point of Sale terminals te gebruiken en betalingen te ontvangen. Tiankii ondersteunt veel oplossingen: mobiele wallets (Blink, Strike), zelf gehoste oplossingen (LNbits, LND/CLN node) of web wallets (Alby). Gedetailleerde verbindingshandleidingen zijn beschikbaar in het gedeelte Bronnen van deze handleiding.



### Voor particuliere klanten: IBI App



**Account aanmaken



Ga naar accounts.ibi.me om je account aan te maken. Op deze pagina kun je kiezen uit twee accounttypen: "Persoonlijk gebruik" voor individueel gebruik, of "Zakelijk gebruik" voor commercieel gebruik. Kies "Persoonlijk gebruik" om toegang te krijgen tot de tools voor het ontvangen en verzenden van betalingen in Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Nadat je "Persoonlijk gebruik" hebt geselecteerd, word je automatisch doorgestuurd naar go.ibi.me om je registratie te voltooien. Dit kan via e-mail, telefoonnummer of met behulp van uw Google, Microsoft of Twitter account. Eenmaal aangemaakt, heb je direct toegang tot je IBI interface, waarbij je Lightning Address al operationeel is.



![Création du compte](assets/fr/02.webp)



**Interface main**



De IBI-interface toont je saldo in satoshis en lokale valuta (USD). Met drie knoppen kun je communiceren: "Ontvangen" om betalingen te ontvangen, "Scannen" om een QR-code te scannen en "Verzenden" om satoshis te versturen.



![Interface IBI](assets/fr/03.webp)



**Betaling ontvangen**



Druk op "Ontvangen" om satoshis te ontvangen. De applicatie genereert automatisch een QR-code en toont uw gepersonaliseerde Address Lightning (nom@ibi.me formaat). Deel dit adres of de QR-code met de verzender: het geld komt onmiddellijk op je IBI-rekening terecht.



![Réception avec Lightning Address](assets/fr/04.webp)



Zodra je saldo is gecrediteerd, kun je deze satoshis gebruiken om betalingen te doen.



**Betaling verzenden**



Om satoshis te verzenden, druk je op "Verzenden". Je kunt een Lightning QR-code scannen of rechtstreeks een Lightning Address-bestemming invoeren.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Voer het gewenste bedrag in satoshis in, controleer het gelijkwaardige bedrag in lokale valuta en bevestig de betaling.



![Confirmation du montant](assets/fr/07.webp)



Een succesmelding bevestigt de verzending met details: verzonden bedrag, transactiekosten en ontvanger.



![Paiement réussi](assets/fr/08.webp)



**Rekeningbeheer



In Instellingen kunt u uw Bitcoin NFC-kaarten (Bolt Kaarten) beheren. Via de interface kunt u uw kaarten activeren, deactiveren of uitgavenlimieten instellen.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Voor verkopers: Merchant Dashboard en POS



**Zakelijke account aanmaken



Ga naar accounts.ibi.me om je account aan te maken. Selecteer "Zakelijk gebruik" om toegang te krijgen tot de Merchant tools. Dit type account geeft toegang tot het Merchant Dashboard en betaalautomaten.



Nadat je "Zakelijk gebruik" hebt geselecteerd, word je automatisch doorgestuurd naar het Merchant Dashboard (pay.tiankii.com). Dit brengt u naar de bedrijfsbeheerinterface met het bijhouden van inkomsten, transacties en betalingshulpmiddelen. Om te beginnen met het accepteren van betalingen, moet u eerst uw wallet Lightning aansluiten door op de link bovenaan de pagina te klikken (zie pijl op afbeelding).



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning**-aansluiting



Cruciale stap bij het activeren van uw verkooppunt: uw wallet Lightning aansluiten om betalingen te ontvangen. De interface biedt verschillende aansluitmogelijkheden. Let op: sommige opties (Bitcoin Onchain en Lightning Network) zijn nog in ontwikkeling en worden grijs weergegeven op de interface.



![Options de connexion wallet](assets/fr/12.webp)



Voor deze tutorial gebruiken we de Lightning Address verbinding, compatibel met Chivo, Blink Wallet en Strike. Voer je Lightning Address in (nom@domaine.com formaat), bijvoorbeeld van LN Markets, Alby of een andere compatibele leverancier.



![Saisie de la Lightning Address](assets/fr/13.webp)



Zodra je bent ingelogd, is je account operationeel. Je kunt nu de POS openen of terugkeren naar het dashboard om andere instellingen te configureren.



![Connexion réussie](assets/fr/14.webp)



*betaallinks** *bet betaallinks



Het menu "Betalingshulpmiddelen" geeft toegang tot "Betalingsverzoek", waarmee je betaallinks kunt maken en beheren. Deze functie is handig voor het genereren van gepersonaliseerde betaallinks die per e-mail of bericht worden verzonden: donaties, eenmalige betalingen, meerdere betalingen of zelfs paywalls om inhoud te beschermen. Je kunt verschillende soorten links maken om aan je zakelijke behoeften te voldoen.



![Liens de paiement](assets/fr/15.webp)



**Sales terminal configuratie**



Om in-store betalingen te accepteren, ga je naar het menu "Verkoopterminal" vanuit "Betaaltools". In dit gedeelte kun je je POS-terminals aanmaken en beheren (het aantal terminals hangt af van je plan, zie Freemium vs. Business-plannen hieronder). Klik op "Openen" om de POS-interface in je browser te openen.



![Gestion des terminaux](assets/fr/16.webp)




**Een verkoop genereren**



De POS-terminal toont een numeriek toetsenblok voor het invoeren van het verkoopbedrag. Voer het bedrag in je lokale valuta in (bijv. 500 sats komt overeen met 630,74 ARS) en druk vervolgens op "OK" om te bevestigen.



![Saisie du montant](assets/fr/17.webp)



De applicatie genereert direct een Lightning QR-code en een Lightning Address voor betaling. Klanten kunnen de QR-code scannen met hun wallet of hun Bolt-kaart gebruiken op een NFC-terminal.



![QR code de paiement](assets/fr/18.webp)



Zodra de betaling is ontvangen, verschijnt er een bevestigingsscherm met het ontvangen bedrag in lokale valuta en satoshis. Je kunt een ontvangstbewijs per e-mail sturen, het ticket afdrukken of direct een nieuwe verkoop starten.



![Paiement encaissé](assets/fr/19.webp)



**Monitoring en beheer**



Alle transacties worden bijgehouden in uw Merchant Dashboard. Je kunt de inkomsten per periode, het totale aantal verkopen en een gedetailleerde geschiedenis voor je boekhouding bijhouden.



De interface Instellingen biedt verschillende configuratietabbladen. Op het tabblad "Algemene instellingen" kun je je merchant profiel en meldingen beheren. Op het tabblad "Gebruikers" kunt u toegang tot het Merchant Dashboard voor uw team toevoegen en beheren (multi-user beheer volgens uw plan). Het tabblad "Ontwikkelwerkruimte" geeft toegang tot API sleutels voor geavanceerde integraties, terwijl je met "Abonnement" je abonnement kunt beheren.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs Zakelijke plannen



Tiankii biedt twee pakketten voor het Merchant Dashboard. Het **Freemium** plan (gratis) is geschikt voor start-ups met beperkingen: één verkooppunt, één gebruiker, maandelijks volume beperkt tot 1.000 USD en geen toegang tot e-commerce connectors. Het **Business**-plan (0,5% kosten per transactie) biedt onbeperkte terminals, onbeperkte gebruikers, onbeperkt volume, toegang tot WooCommerce/Shopify/Cloudbeds-plugins en exclusieve WhatsApp-meldingen.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Voordelen en beperkingen



### Hoogtepunten



**Zelfbehoud**: U behoudt uw privésleutels en volledige controle over uw fondsen. Geen risico op bevriezing van uw account of faillissement van het platform van een derde partij.



**Eenvoud**: Lightning Address als e-mailadres, NFC-betalingen met een simpele tik, intuïtieve interface zonder technische kennis.



**Compleet ecosysteem**: Tools voor alle profielen (particulieren, detailhandelaren, ontwikkelaars) met modulaire integraties om aan uw behoeften te voldoen.



**Professionele naleving**: Veilige cloudhosting, PCI-DSS-compliance, Salvadoraanse regelgeving.



### Beperkingen



**Beperkingen**: Permanente wallet-verbinding vereist, liquiditeitsbeheer voor grote volumes, risico op storing als ontvanger offline is. Tiankii verzacht deze aspecten met geïntegreerde LSP's.



**SaaS-afhankelijkheid**: Als Tiankii niet beschikbaar is, is het genereren van facturen tijdelijk onmogelijk (je geld blijft wel veilig).



**Privacy**: Tiankii kan metadata van transacties observeren (bedragen, data). Minder privé dan een zelf gehoste oplossing zoals BTCPay Server.



## Conclusie



Tiankii illustreert hoe een goed ontworpen infrastructuur de technische barrières kan wegnemen die een massale adoptie van Bitcoin als dagelijkse valuta in de weg staan. Door de kracht van Lightning Network te combineren met een niet-verplichte aanpak en toegankelijke tools, biedt het ecosysteem een evenwichtige weg tussen financiële soevereiniteit en gebruiksgemak.



Voor winkeliers biedt Tiankii de mogelijkheid om transactiekosten drastisch te verlagen en tegelijkertijd toegang te krijgen tot een nieuw klantenbestand. Voor consumenten veranderen Lightning Address en NFC-kaarten Bitcoin in een praktische valuta, zonder technische complexiteit.



Hoewel een wijdverspreide toepassing van Bitcoin een uitdaging blijft die opleiding en tijd vergt, tonen infrastructuren zoals Tiankii aan dat de technische hulpmiddelen al bestaan. De missie om betalingen via Bitcoin te vereenvoudigen is niet langer een verre visie, maar een realiteit die toegankelijk is voor iedereen die bereid is de sprong te wagen.



## Bronnen



### Officiële documentatie




- [Officiële website van Tiankii](https://tiankii.com)
- [Tiankii Helpcentrum](https://help.tiankii.com)
- [IBI-toepassing](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Commando Centrum](https://cc.ibi.me)



### Wallet verbindingsgeleiders




- [Verbind LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [BlueWallet aansluiten (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Sluit Alby Wallet aan](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Verbind Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Gemeenschap




- [Lightning Network Plus](https://lightningnetwork.plus) - Bliksem leermiddel
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvadoriaans initiatief voor circulaire economie Bitcoin



### Verwant gereedschap




- [Blink Wallet](https://blink.sv) - Wallet Lightning-compatibel aanbevolen
- [LNbits](https://lnbits.com) - Zelf gehoste wallet oplossing
- [Standaard Bolt-kaart](https://github.com/boltcard) - Technische specificaties voor NFC-kaarten