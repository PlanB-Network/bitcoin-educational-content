---
name: BTCPay server - Umbrel
description: Installatie en gebruik van BTCPay Server op Umbrel om Bitcoin en Lightning te accepteren
---

![cover](assets/cover.webp)



In het Bitcoin ecosysteem vormt het accepteren van betalingen een grote uitdaging voor handelaren en bedrijven. Traditionele oplossingen, of ze nu bankieren (creditcards, Stripe, PayPal) of zelfs Bitcoin (BitPay, Coinbase Commerce), leggen tussenpersonen op die aanzienlijke kosten in rekening brengen, uw gevoelige bedrijfsgegevens verzamelen en uw transacties naar believen kunnen blokkeren of censureren. Deze afhankelijkheid druist in tegen Bitcoin's fundamentele principes van decentralisatie, vertrouwelijkheid en financiële soevereiniteit.



BTCPay Server is in opkomst als het open-source antwoord op dit probleem. Deze self-hosted betalingsverwerker verandert je eigen Bitcoin node in een professionele infrastructuur, zonder tussenpersoon, zonder extra verwerkingskosten en zonder in te boeten op privacy. BTCPay Server is ontwikkeld door een wereldwijde gemeenschap van bijdragers sinds 2017 en stelt je in staat om Bitcoin en Lightning betalingen direct in je wallets te ontvangen, waarbij je te allen tijde de volledige controle over je fondsen behoudt.



Traditioneel vereist de installatie van BTCPay Server geavanceerde technische vaardigheden: Linux-serverconfiguratie, beheersing van Docker, SSL-certificaatbeheer en netwerkbeveiliging. Umbrel revolutioneert deze aanpak met een one-click installatie die direct geïntegreerd is met uw Bitcoin en Lightning node. Deze vereenvoudiging maakt wat voorheen voorbehouden was aan ervaren technici toegankelijk voor iedereen.



**Belangrijk om te begrijpen**: BTCPay Server op Umbrel werkt standaard alleen op uw lokale netwerk. U kunt facturen maken, Lightning en Bitcoin betalingen accepteren en uw boekhouding beheren vanaf elk apparaat dat verbonden is met uw thuisnetwerk (computer, smartphone, tablet). Deze configuratie is ideaal voor het factureren van persoonlijke diensten, het beheren van face-to-face betalingen of het gebruik van BTCPay Server vanaf uw lokale netwerk. Aan de andere kant, om BTCPay Server te integreren in een online winkel die publiek toegankelijk is op het internet, zal een extra configuratie met publieke blootstelling nodig zijn (we zullen deze kwestie behandelen aan het einde van de tutorial).



Deze handleiding neemt u mee door de volledige installatie van BTCPay Server op Umbrel, het configureren van uw Bitcoin wallet en Lightning knooppunt, het aanmaken en betalen van facturen en het beheren van de boekhoudkundige rapportering. U zult ontdekken hoe u BTCPay Server efficiënt kunt gebruiken op uw lokale netwerk, en daarna kijken we naar oplossingen voor publieke weergave als u het wilt integreren met een e-commerce site.



## Vereisten



Om deze tutorial te kunnen volgen, moet Umbrel correct geïnstalleerd en geconfigureerd zijn. Als je dat nog niet gedaan hebt, bekijk dan onze tutorial over de installatie van Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Uw Bitcoin Core node moet volledig gesynchroniseerd zijn met de blockchain (100% in Umbrel's Bitcoin applicatie). Deze initiële synchronisatie duurt meestal tussen de 3 dagen en 2 weken, afhankelijk van uw hardware en internetverbinding.



Om directe Lightning-betalingen te accepteren, moet u ook LND (Lightning Network Daemon) op Umbrel installeren. Bekijk onze tutorial over het installeren en configureren van LND op Umbrel als je deze functie wilt inschakelen.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Laat ten minste 50 GB vrije schijfruimte voor BTCPay Server, haar databases en Lightning gegevens. Een stabiele internetverbinding via ethernetkabel wordt sterk aanbevolen om verbroken verbindingen te voorkomen.



## BTCPay server installeren op Umbrel



Ga vanuit de Umbrel interface (`umbrel.local`) naar de App Store en zoek naar "BTCPay Server" in de Bitcoin categorie.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klik op Installeren. Umbrel controleert automatisch of Bitcoin Core en LND zijn geïnstalleerd en start dan de implementatie (2-5 minuten).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Eenmaal geïnstalleerd, open je de applicatie. Je moet een beheerdersaccount aanmaken met sterke referenties.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Zodra uw account is aangemaakt, zal BTCPay Server u onmiddellijk vragen om uw eerste winkel op te zetten. Kies een bedrijfsnaam en selecteer een referentievaluta (EUR, USD of BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Toegang tot BTCPay Server op uw lokaal netwerk



BTCPay Server is toegankelijk vanaf elk apparaat op uw lokale netwerk (WiFi of Ethernet). Toegang vanaf uw browser naar :



```url
http://umbrel.local
```



Of rechtstreeks naar :



```url
http://umbrel.local:3003
```



**Remote toegang met Tailscale**: Om toegang te krijgen tot de BTCPay Server van overal ter wereld, gebruik je Tailscale. Met deze veilige VPN kunt u verbinding maken met uw Umbrel alsof u zich op uw lokale netwerk bevindt. Bekijk onze tutorial over Tailscale op Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Uw Bitcoin portfolio configureren



Om betalingen te accepteren, moet u een Bitcoin wallet configureren. BTCPay Server toont configuratieopties in het dashboard.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Om wallet Bitcoin te configureren, ga naar "Portemonnees" > "Bitcoin".



Je hebt twee opties: rechtstreeks een nieuwe portefeuille aanmaken in BTCPay, of een bestaande portefeuille importeren. Voor het importeren zijn verschillende methoden beschikbaar:




- Sluit hardware wallet** aan (aanbevolen): Importeer je publieke sleutels via de Vault-toepassing
- wallet bestand importeren** (aanbevolen): Upload een geëxporteerd bestand uit je portfolio
- Uitgebreide openbare sleutel invoeren**: Voer uw XPub/YPub/ZPub handmatig in
- Scan wallet QR code** : Scan een QR code van BlueWallet, Cobo Vault, Passport of Specter DIY
- Voer wallet seed** in (niet aanbevolen) : Voer uw 12- of 24-woord herstelzin in



![Options de création de portefeuille](assets/fr/06.webp)



Voor deze tutorial gaan we een nieuwe Hot wallet aanmaken: de private sleutel wordt dus opgeslagen op onze Umbrel server. In dit geval raden we je sterk aan om het geld regelmatig naar een koude wallet te verplaatsen, om te voorkomen dat er grote bedragen op de server worden opgeslagen.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Eenmaal geconfigureerd, bevestigt BTCPay Server dat uw wallet klaar is om on-chain betalingen te accepteren.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Lightning Network activeren



Om onmiddellijke Lightning betalingen te aanvaarden, ga naar Wallets > Lightning. Dan, aangezien uw LND node al op zijn plaats staat op Umbrel, klikt u gewoon op de "Opslaan" knop om de verbinding tussen uw BTCPay Server en uw Lightning node te valideren.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Facturen maken en betalen



Navigeer in de BTCPay Server interface naar Facturen > Invoice aanmaken. Voer het bedrag in, voeg een optionele beschrijving toe en klik op Maken.



![Création d'une nouvelle facture](assets/fr/10.webp)



U kunt dan op de knop "Afrekenen" klikken om de factuur weer te geven. BTCPay genereert dan een factuur met een verenigde QR-code (BIP21) die het Bitcoin adres en de Lightning-factuur bevat.



![Détails de la facture générée](assets/fr/11.webp)



Je klant kan de QR-code scannen met elke compatibele wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Zodra de factuur is betaald, wordt deze binnen enkele seconden "Vereffend" voor Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Beheer en opvolging van betalingen



In het gedeelte "Rapportage", tabblad "Facturen", vind je een volledige geschiedenis van je facturen met datum, bedrag, status en betaalmethode. Je kunt het indien nodig exporteren.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Winkelconfiguratie



Met BTCPay Server kunt u meerdere winkels met verschillende parameters beheren. Elke winkel vertegenwoordigt een afzonderlijke bedrijfsentiteit: e-commercewinkel, fysiek verkooppunt of facturering van diensten.



In de winkelinstellingen vind je verschillende belangrijke secties:



![Paramètres du magasin](assets/fr/15.webp)





- Algemene instellingen**: Winkelnaam, referentievaluta (BTC, EUR, USD), vervaltijd factuur (standaard 15 minuten), aantal vereiste blockchainbevestigingen
- Koersen**: Configuratie van wisselkoersbronnen en fiat/Bitcoin conversies
- Afrekenen**: Pas het uiterlijk van uw afrekenpagina's aan (logo, kleuren, persoonlijke berichten)
- E-mailinstellingen**: Configuratie van e-mailmeldingen voor ontvangen betalingen
- Toegangsmunten**: Beheer van API tokens voor e-commerce integraties (WooCommerce, Shopify, etc.)
- Gebruikers**: Gebruikerstoegang tot de winkel beheren met verschillende machtigingsniveaus (Eigenaar, Gast)
- Webhooks**: Webhook configuratie voor real-time synchronisatie met uw boekhoud- of ERP-systeem



BTCPay Server biedt ook een sectie Plugins om de functionaliteit uit te breiden met e-commerce integraties, point-of-sale systemen en extra tools.



![Gestion des plugins](assets/fr/16.webp)



## Voordelen en beperkingen van lokaal gebruik



**Voordelen van BTCPay Server ten opzichte van Umbrel** :




- Totale soevereiniteit: exclusieve controle over privésleutels en fondsen, geen enkele derde partij kan je betalingen bevriezen of censureren
- Aanzienlijke besparingen: slechts Bitcoin netwerkkosten (een paar cent op Lightning) vs. 2-3% op traditionele processors
- Maximale vertrouwelijkheid: geen registratie, identiteitsverificatie of het delen van gegevens met andere bedrijven
- Open-source architectuur garandeert transparantie, controleerbaarheid en duurzaamheid via een grote gemeenschap van ontwikkelaars
- Eenvoudige installatie via Umbrel, zonder geavanceerde technische vaardigheden



**Belangrijke beperkingen** :




- Alleen lokaal netwerk**: BTCPay Server op Umbrel is alleen toegankelijk vanaf uw thuisnetwerk. Perfect voor face-to-face facturering, freelance diensten of kleine fysieke bedrijven, maar ongeschikt voor publiek toegankelijke online winkels.
- Volledige technische verantwoordelijkheid: node-onderhoud, regelmatige back-ups, connectiviteitsbewaking
- Lightning liquiditeitsbeheer: openen en beheren van kanalen met voldoende inkomende capaciteit
- Ondersteuning beperkt tot communitydocumentatie en forums, waarvoor meer autonomie nodig is dan voor een commerciële afdeling klantenservice



Deze beperking van het lokale netwerk is het grootste obstakel voor de integratie van BTCPay Server in een e-commercewinkel, waar klanten toegang moeten kunnen krijgen tot betaalpagina's vanaf elke plek op het internet.



## Beste praktijken en veiligheid



Activeer automatische Umbrel-back-ups en bewaar een kopie op externe media (USB-stick, harde schijf, versleutelde cloud). Bewaar uw Bitcoin zaden (herstelzinnen) op een veilige, fysiek gescheiden plaats. Maak een back-up van LND's channel.backup bestand voor Bliksemherstel.



Controleer regelmatig de synchronisatie van Bitcoin Core, Lightning-kanalen en BTCPay Server-respons. Een eenvoudige wekelijkse test: generate en betaal een rekening voor een paar satoshis. Houd Umbrel up-to-date (beveiligingspatches, verbeteringen). Maak een back-up voor grote updates. Voor professioneel gebruik, overweeg externe monitoring (UptimeRobot) met e-mail/SMS waarschuwingen.



## BTCPay Server openbaar maken voor een online winkel



Om BTCPay Server te integreren in een webgebaseerde e-commercewinkel (WooCommerce, Shopify, enz.), moeten uw klanten de betalingspagina's overal kunnen openen, niet alleen op uw lokale netwerk.



**Oplossing: Nginx Proxy Manager**



U kunt BTCPay Server publiekelijk blootstellen met behulp van Nginx Proxy Manager (beschikbaar in de Umbrel App Store). Deze oplossing vereist :




- Een domeinnaam (klassiek of gratis via DuckDNS, No-IP, Afraid.org)
- Poort doorsturen (poorten 80 en 443) configureren op je router
- Installatie van Nginx Proxy Manager, die automatisch SSL-certificaten beheert



Deze configuratie stelt je server bloot aan het internet en vereist extra waakzaamheid (sterke wachtwoorden, 2FA, regelmatige updates). We zullen een speciale tutorial voorbereiden waarin deze volledige procedure wordt beschreven.



## Conclusie



BTCPay Server on Umbrel combineert de kracht van het Bitcoin knooppunt met de eenvoud van Umbrel om een self-hosted professionele betalingsinfrastructuur te creëren die voor iedereen toegankelijk is. Deze financiële soevereiniteit komt met een onderhoudsverantwoordelijkheid, maar Umbrel vereenvoudigt de operationele last enorm in vergelijking met de voordelen: eliminatie van verwerkingskosten, bescherming van uw privacy, weerstand tegen censuur en totale controle over uw fondsen.



Het gebruik van het lokale netwerk omvat al een groot aantal toepassingen: facturering voor freelance diensten, betalingen in persoon, kleine fysieke winkels, of gewoon leren en experimenteren met Bitcoin en Lightning in een gecontroleerde omgeving. Voor e-commerce behoeften die publieke blootstelling vereisen, bestaat de Nginx Proxy Manager oplossing, maar deze vereist aanvullende technische configuratie, die we in een speciale tutorial zullen uitwerken.



Of u nu een bedrijf runt, een beginnend project of gewoon aan het experimenteren bent, BTCPay Server op Umbrel biedt volledige financiële autonomie. Het pad begint met uw eerste winkel, uw eerste factuur, uw eerste betaling die rechtstreeks in uw soevereine infrastructuur wordt ontvangen.



## Bronnen



### Officiële documentatie




- [Officiële BTCPay Server website](https://btcpayserver.org)
- [Complete BTCPay Server documentatie](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Documentatie van Tailscale](https://tailscale.com/kb)


### Gemeenschap en ondersteuning




- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Forum Paraplu](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)