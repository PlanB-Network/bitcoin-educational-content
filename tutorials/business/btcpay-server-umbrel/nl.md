---
name: BTCPAY SERVER - Parel
description: BTCPAY SERVER installeren en gebruiken op Umbrel om Bitcoin en Lightning te accepteren
---

![cover](assets/cover.webp)



In het Bitcoin ecosysteem vormt het accepteren van betalingen een grote uitdaging voor zowel handelaren als bedrijven. Traditionele oplossingen, of ze nu bankieren (creditcards, Stripe, PayPal) of zelfs Bitcoin (BitPay, Coinbase Commerce), leggen tussenpersonen op die aanzienlijke kosten in rekening brengen, uw gevoelige bedrijfsgegevens verzamelen en uw transacties naar believen kunnen BLOCK of censureren. Deze afhankelijkheid druist in tegen Bitcoin's fundamentele principes van decentralisatie, vertrouwelijkheid en financiële soevereiniteit.



BTCPAY SERVER is in opkomst als het open-source antwoord op dit probleem. Deze self-hosted betalingsverwerker verandert je eigen Bitcoin node in een professionele infrastructuur, zonder tussenpersoon, zonder extra verwerkingskosten en zonder compromissen op het gebied van privacy. BTCPAY SERVER is sinds 2017 ontwikkeld door een wereldwijde gemeenschap van bijdragers en stelt je in staat om Bitcoin en Lightning betalingen direct in je portemonnee te ontvangen, waarbij je te allen tijde de volledige controle over je fondsen behoudt.



Traditioneel vereist het installeren van BTCPAY SERVER geavanceerde technische vaardigheden: Linux server configuratie, Docker beheersing, SSL certificaat beheer en netwerk beveiliging. Umbrel revolutioneert deze aanpak met een één-klik installatie die direct geïntegreerd is met uw Bitcoin en LIGHTNING NODE. Deze vereenvoudiging maakt wat voorheen voorbehouden was aan ervaren technici toegankelijk voor iedereen.



**Belangrijk om te begrijpen**: BTCPAY SERVER op Umbrel werkt standaard alleen op uw lokale netwerk. U kunt facturen maken, Lightning- en Bitcoin-betalingen accepteren en uw boekhouding beheren vanaf elk apparaat dat verbonden is met uw thuisnetwerk (computer, smartphone, tablet). Deze configuratie is ideaal voor het factureren van persoonlijke diensten, het beheren van directe betalingen of het gebruik van BTCPAY SERVER vanaf uw lokale netwerk. Aan de andere kant, om BTCPAY SERVER te integreren in een online winkel die publiek toegankelijk is op het internet, is een extra configuratie met publieke blootstelling nodig (we behandelen dit aan het einde van de tutorial).



Deze tutorial neemt je mee door de complete installatie van BTCPAY SERVER op Umbrel, het configureren van je Bitcoin Wallet en LIGHTNING NODE, het maken en betalen van facturen, en het beheren van boekhoudrapportages. U komt te weten hoe u BTCPAY SERVER effectief kunt gebruiken op uw lokale netwerk, en daarna bespreken we oplossingen voor openbare weergave als u het wilt integreren met een e-commerce site.



## Vereisten



Om deze tutorial te kunnen volgen, moet Umbrel correct geïnstalleerd en geconfigureerd zijn. Als je dat nog niet gedaan hebt, bekijk dan onze tutorial over de installatie van Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Uw Bitcoin core knooppunt moet volledig gesynchroniseerd zijn met Blockchain (100% in Umbrel's Bitcoin toepassing). Deze initiële synchronisatie duurt meestal tussen de 3 dagen en 2 weken, afhankelijk van uw hardware en internetverbinding.



Om directe Lightning-betalingen te accepteren, moet u ook LND (Lightning Network Daemon) op Umbrel installeren. Bekijk onze tutorial over het installeren en configureren van LND op Umbrel als je deze functie wilt inschakelen.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Zorg voor minstens 50 GB vrije schijfruimte voor BTCPAY SERVER, de databases en Lightning-gegevens. Een stabiele internetverbinding via ethernetkabel wordt sterk aanbevolen om onderbrekingen te voorkomen.



## BTCPAY SERVER installeren op paraplu



Ga vanuit Umbrel Interface (`umbrel.local`) naar de App Store en zoek naar "BTCPAY SERVER" in de categorie Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klik op Installeren. Umbrel controleert automatisch of Bitcoin core en LND geïnstalleerd zijn en begint dan met de installatie (2-5 minuten).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Eenmaal geïnstalleerd, open je de applicatie. Je moet een beheerdersaccount aanmaken met sterke referenties.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Zodra je account is aangemaakt, vraagt BTCPAY SERVER je meteen om je eerste winkel op te zetten. Kies een professionele naam en selecteer een referentievaluta (EUR, USD of BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Toegang tot BTCPAY SERVER op uw lokale netwerk



BTCPAY SERVER is toegankelijk vanaf elk apparaat op je lokale netwerk (WiFi of Ethernet). Toegang via uw browser tot :



```url
http://umbrel.local
```



Of rechtstreeks naar :



```url
http://umbrel.local:3003
```



**Toegang op afstand met Tailscale**: Om overal ter wereld toegang te krijgen tot BTCPAY SERVER, gebruik je Tailscale. Met deze veilige VPN kun je verbinding maken met je Umbrel alsof je op je lokale netwerk zit. Zie onze tutorial over Tailscale op Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Uw Bitcoin portfolio configureren



Om betalingen te accepteren, moet je een Bitcoin Wallet configureren. BTCPAY SERVER toont de configuratieopties in het dashboard.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Om Wallet Bitcoin te configureren, ga naar "Portemonnees" > "Bitcoin".



Je hebt twee opties: rechtstreeks een nieuwe portefeuille aanmaken in BTCPay, of een bestaande portefeuille importeren. Voor het importeren zijn verschillende methoden beschikbaar:




- Maak verbinding met Hardware Wallet** (aanbevolen): Importeer je publieke sleutels via de Vault-toepassing
- Wallet bestand importeren** (aanbevolen): Upload een geëxporteerd bestand uit je portfolio
- Uitgebreide openbare sleutel invoeren**: Voer uw XPub/YPub/ZPub handmatig in
- Scan Wallet QR code** : Scan een QR-code van BlueWallet, Cobo Vault, Passport of Specter DIY
- Wallet seed** invoeren (niet aanbevolen) : Voer uw 12- of 24-woord herstelzin in



![Options de création de portefeuille](assets/fr/06.webp)



Voor deze tutorial gaan we een nieuwe Hot Wallet aanmaken: de private sleutel wordt dus opgeslagen op onze Umbrel server. In dit geval raden we je sterk aan om het geld regelmatig te verplaatsen naar een Cold Wallet om te voorkomen dat er grote bedragen op de server worden opgeslagen.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Eenmaal geconfigureerd, bevestigt BTCPAY SERVER dat uw Wallet klaar is om On-Chain-betalingen te accepteren.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Lightning Network activeren



Om directe Lightning-betalingen te accepteren, ga je naar Portemonnees > Lightning. Aangezien je LND-knooppunt al op zijn plaats zit op Umbrel, klik je op de knop "Opslaan" om de verbinding tussen je BTCPAY SERVER en je LIGHTNING NODE te valideren.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Facturen maken en betalen



Navigeer in Interface BTCPAY SERVER naar Facturen > Maken Invoice. Voer het bedrag in, voeg een optionele omschrijving toe en klik op Aanmaken.



![Création d'une nouvelle facture](assets/fr/10.webp)



U kunt dan klikken op de "Afrekenen" knop om de Invoice weer te geven. BTCPay genereert dan een Invoice met een verenigde QR code (BIP21) die de Bitcoin Address en de Lightning Invoice bevat.



![Détails de la facture générée](assets/fr/11.webp)



Je klant kan de QR-code scannen met elke compatibele Wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Na betaling wordt de Invoice binnen enkele seconden "verrekend" voor Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Beheer en opvolging van betalingen



In het gedeelte "Rapportage", tabblad "Facturen", vind je een volledige geschiedenis van je facturen, met datum, bedrag, status en betaalmethode. Je kunt het indien nodig exporteren.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Winkelconfiguratie



Met BTCPAY SERVER kunt u meerdere winkels met verschillende parameters beheren. Elke winkel vertegenwoordigt een afzonderlijke bedrijfsentiteit: e-commercewinkel, fysiek verkooppunt of facturering van diensten.



In de winkelinstellingen vind je verschillende belangrijke secties:



![Paramètres du magasin](assets/fr/15.webp)





- Algemene instellingen**: Winkelnaam, referentievaluta (BTC, EUR, USD), Invoice vervaltijd (standaard 15 minuten), aantal vereiste Blockchain bevestigingen
- Tarieven**: Configuratie van Exchange koersbronnen en fiat/Bitcoin conversies
- Afrekenen**: Pas het uiterlijk van uw afrekenpagina's aan (logo, kleuren, persoonlijke berichten)
- E-mailinstellingen**: Configuratie van e-mailmeldingen voor ontvangen betalingen
- Toegangsmunten**: API token beheer voor e-commerce integraties (WooCommerce, Shopify, etc.)
- Gebruikers**: Gebruikerstoegang tot de winkel beheren met verschillende machtigingsniveaus (Eigenaar, Gast)
- Webhooks**: Webhook configuratie voor real-time synchronisatie met uw boekhoud- of ERP-systeem



BTCPAY SERVER biedt ook een Plugins sectie om de functionaliteit uit te breiden met e-commerce integraties, point-of-sale systemen en aanvullende tools.



![Gestion des plugins](assets/fr/16.webp)



## Voordelen en beperkingen van lokaal gebruik



**Voordelen van BTCPAY SERVER op Umbrel** :




- Totale soevereiniteit: exclusieve controle over privésleutels en fondsen, geen enkele derde partij kan je betalingen bevriezen of censureren
- Aanzienlijke besparingen: slechts Bitcoin netwerkkosten (een paar cent op Lightning) vs. 2-3% op traditionele processors
- Maximale vertrouwelijkheid: geen registratie, identiteitsverificatie of het delen van gegevens met andere bedrijven
- Open-source architectuur garandeert transparantie, controleerbaarheid en duurzaamheid via een grote gemeenschap van ontwikkelaars
- Eenvoudige installatie via Umbrel, zonder geavanceerde technische vaardigheden



**Belangrijke beperkingen** :




- Alleen lokaal netwerk**: BTCPAY SERVER op Umbrel is alleen toegankelijk vanaf uw thuisnetwerk. Perfect voor face-to-face facturering, freelance diensten of kleine fysieke bedrijven, maar ongeschikt voor online winkels die publiekelijk toegankelijk zijn op het internet.
- Volledige technische verantwoordelijkheid: node-onderhoud, regelmatige back-ups, connectiviteitsbewaking
- Lightning liquiditeitsbeheer: openen en beheren van kanalen met voldoende inkomende capaciteit
- Ondersteuning beperkt tot communitydocumentatie en forums, waarvoor meer autonomie nodig is dan voor een commerciële afdeling klantenservice



Deze LAN-beperking is het grootste obstakel voor het integreren van BTCPAY SERVER in een e-commerce winkel, waar klanten vanaf elke plek op het internet toegang moeten kunnen krijgen tot betaalpagina's.



## Beste praktijken en veiligheid



Activeer automatische Umbrel back-ups en bewaar een kopie op externe media (USB-stick, Hard schijf, versleutelde cloud). Bewaar je Bitcoin zaden (herstelzinnen) op een veilige, fysiek gescheiden plaats. Bewaar het bestand LND channel.backup voor Bliksemherstel.



Controleer regelmatig de Bitcoin core synchronisatie, Lightning kanalen en BTCPAY SERVER respons. Een eenvoudige wekelijkse test: generate en betaal een rekening voor een paar satoshis. Houd Umbrel up-to-date (beveiligingspatches, verbeteringen). Maak een back-up voor grote updates. Overweeg voor professioneel gebruik externe monitoring (UptimeRobot) met e-mail/SMS-waarschuwingen.



## BTCPAY SERVER publiekelijk tonen voor een online winkel



Om BTCPAY SERVER te integreren in een webgebaseerde e-commerce winkel (WooCommerce, Shopify, etc.), moeten je klanten overal toegang kunnen krijgen tot de betaalpagina's, niet alleen vanaf je lokale netwerk.



**Oplossing: Nginx Proxy Manager**



Je kunt BTCPAY SERVER openbaar maken met Nginx Proxy Manager (beschikbaar in de Umbrel App Store). Deze oplossing vereist :




- Een domeinnaam (klassiek of gratis via DuckDNS, No-IP, Afraid.org)
- Poort doorsturen (poorten 80 en 443) configureren op je router
- Installatie van Nginx Proxy Manager, die automatisch SSL-certificaten beheert



Deze configuratie stelt je server bloot aan het internet en vereist extra waakzaamheid (sterke wachtwoorden, 2FA, regelmatige updates). We zullen een speciale tutorial voorbereiden waarin deze volledige procedure wordt beschreven.



## Conclusie



BTCPAY SERVER op Umbrel combineert de kracht van het Bitcoin knooppunt met de eenvoud van Umbrel om een zelf gehoste professionele betalingsinfrastructuur te creëren die voor iedereen toegankelijk is. Deze financiële soevereiniteit komt met een onderhoudsverantwoordelijkheid, maar Umbrel vereenvoudigt de operationele last enorm in vergelijking met de voordelen: eliminatie van verwerkingskosten, bescherming van je privacy, weerstand tegen censuur en totale controle over je fondsen.



Het gebruik van het lokale netwerk omvat al een breed scala aan toepassingen: facturering voor freelance diensten, persoonlijke betalingen, kleine fysieke winkels, of gewoon leren en experimenteren met Bitcoin en Lightning in een gecontroleerde omgeving. Voor e-commerce behoeften die publieke blootstelling vereisen, bestaat de Nginx Proxy Manager oplossing, maar die vereist aanvullende technische configuratie, die we in een speciale tutorial zullen uitwerken.



Of je nu een bedrijf runt, een beginnend project hebt of gewoon aan het experimenteren bent, BTCPAY SERVER op Umbrel biedt volledige financiële autonomie. Het pad begint met een eerste winkel, een eerste Invoice, een eerste betaling direct in je soevereine infrastructuur.



## Bronnen



### Officiële documentatie




- [BTCPAY SERVER officiële website](https://btcpayserver.org)
- [Volledige BTCPAY SERVER documentatie](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Documentatie van Tailscale](https://tailscale.com/kb)


### Gemeenschap en ondersteuning




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Forum Paraplu](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)