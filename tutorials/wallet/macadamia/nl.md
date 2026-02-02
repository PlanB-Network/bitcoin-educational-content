---
name: Macadamia Wallet
description: Cashu mobiel wallet voor anonieme en directe BTC-betalingen
---

![cover](assets/cover.webp)



Macadamia Wallet is een iOS mobiele wallet die het Cashu protocol implementeert, een Chaumiaans ecash systeem dat volledig anonieme Bitcoin betalingen mogelijk maakt. Dankzij blinde handtekeningen kan geen enkele waarnemer je stortingen aan je uitgaven linken, wat een vertrouwelijkheid biedt die vergelijkbaar is met die van fysiek geld.



In deze tutorial bekijken we hoe je Macadamia installeert en configureert, je eerste Cashu-transacties uitvoert (Mint, Send, Receive, Melt) en meerdere mints beheert om je geld veilig te stellen.



## Wat is Macadamia Wallet?



### Het Cashu-protocol



Cashu gebruikt blinde handtekeningen, uitgevonden door David Chaum: je stort bitcoins bij een "munt"-server, die equivalente tokens in satoshis uitgeeft. De munt ondertekent deze tokens zonder de inhoud ervan te zien, waardoor het onmogelijk is om een token aan een gebruiker te koppelen. Uitwisselingen zijn off-chain, peer-to-peer en totaal ondoorzichtig - zelfs de munt kan niet nagaan wie wie betaalt.



Macadamia is een open source wallet iOS ontwikkeld in Swift/SwiftUI. Het werkt zonder account of KYC, uw tokens worden lokaal opgeslagen en beschermd door een seed zin. Code is controleerbaar op GitHub en tokens zijn interoperabel met andere Cashu wallets (Minibits, Cashu.me).



### Bewaarmodel en compromis



**Belangrijk**: Cashu werkt op basis van een custodiaal model. Munten zijn beloftes om te betalen (IOU's) ondersteund door de Bitcoin reserves van de Munt. Als de Munt verdwijnt, verliezen uw tokens hun waarde. Dit is het compromis voor maximale vertrouwelijkheid.



Gebruik Macadamia als een fysieke wallet: alleen kleine hoeveelheden. Verdeel je fondsen over meerdere mints om het risico te verdunnen.



## Belangrijkste kenmerken



Macadamia implementeert de vier fundamentele operaties van het Cashu-protocol. **Mint** zet uw satoshis om in tokens via een Lightning-factuur. **Verstuur** laat je tokens gratis versturen via QR code of link, volledig off-chain. *met *Receive** kun je tokens ontvangen of generate een Lightning-factuur. **Smelten** betaalt een Lightning-factuur door uw tokens te vernietigen.



wallet ondersteunt het beheer van meerdere munten tegelijkertijd. Je kunt tokens tussen verschillende mints uitwisselen via Lightning.



## Ondersteunde platforms



Macadamia is alleen beschikbaar op iOS 17 of hoger voor iPhone en iPad. De native Swift/SwiftUI-toepassing biedt een optimale integratie met het Apple ecosysteem.



Het Cashu protocol garandeert interoperabiliteit tussen wallets. U kunt uw seed zin herstellen in andere toepassingen zoals Minibits op Android of Nutstash op desktop.



De huidige versie wordt gedistribueerd via TestFlight. Gebruik alleen kleine hoeveelheden met deze bètaversie.



## Installatie



Macadamia is momenteel beschikbaar via TestFlight, het bètatestprogramma van Apple. Hier lees je hoe je het installeert:



### Installatie via TestFlight



**Stap 1: Download TestFlight**



Als je de TestFlight app nog niet op je apparaat hebt, zoek dan naar "TestFlight" in de App Store en installeer hem. TestFlight is de officiële applicatie van Apple voor het testen van bètaversies van iOS-applicaties.



**Stap 2: Doe mee aan het bètaprogramma van Macadamia** (in het Frans)



Zodra TestFlight is geïnstalleerd, volgt u deze uitnodigingslink vanaf uw iPhone of iPad: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



De link zal automatisch TestFlight openen en je aanbieden om Macadamia Wallet te installeren. Druk op "Accepteren" en vervolgens op "Installeren" om het downloaden te starten. De applicatie weegt ongeveer tien megabyte en het duurt slechts een paar seconden om te installeren.



![Installation TestFlight](assets/fr/01.webp)



### Belangrijke informatie over bètaversies



Macadamia bevindt zich nog in de actieve ontwikkelingsfase. TestFlight-versies worden regelmatig bijgewerkt en kunnen nieuwe functies introduceren of bugs corrigeren. Zoals bij elke bètaversie kunnen er echter storingen optreden. **We raden je sterk aan om alleen kleine hoeveelheden** te gebruiken, waarvan je accepteert dat deze verloren kunnen gaan in het geval van een technisch probleem.



Macadamia verzamelt geen gebruikersgegevens volgens het weergegeven privacybeleid. Controleer bij het installeren of de ontwikkelaar cypherbase UG is.



## Eerste configuratie



Bij de eerste keer opstarten genereert Macadamia een BIP-39 zin van 12 woorden. Schrijf ze op een veilige plek op - nooit als schermafbeelding. Met deze woorden kun je je wallet opnieuw maken en je tokens uitgeven.



![Configuration initiale](assets/fr/02.webp)



Volg de vier stappen: welkom, voorwaarden accepteren, seed zin opslaan en definitieve bevestiging.



![Interface principale](assets/fr/03.webp)



Zodra de configuratie is voltooid, presenteert Macadamia drie hoofdtabbladen. **Wallet** geeft uw saldo en transactiegeschiedenis weer. **Mints** laat u uw Cashu-servers beheren. **Instellingen** geeft toegang tot instellingen en uw seed zin.



![Ajout d'un mint](assets/fr/04.webp)



U moet nu een mint configureren, d.w.z. een Cashu server die uw tokens zal uitgeven. Ga naar de tab "Mints", tik op "Add new Mint URL" en voer het adres van de door u gekozen munt in (bijv. mint.cubabitcoin.org). Kijk op bitcoinmints.com of cashu.space voor gerenommeerde publieke munten. Valideer alleen munten waarvan je de reputatie hebt gecontroleerd, aangezien zij de bewaring van jouw satoshis zullen hebben.



## Dagelijks gebruik



### Aanmaken van nieuwe tokens (Munt)



Om je wallet Macadamia met ecash te voeden, moet je een "Munt"-operatie uitvoeren (om tokens te creëren). Druk op "Ontvangen" en kies dan de optie "Lightning". Voer het gewenste bedrag in (bijvoorbeeld 1000 sats), selecteer de te gebruiken munt en generate de Lightning-factuur.



![Opération Mint](assets/fr/05.webp)



Betaal de Lightning-factuur met uw gebruikelijke wallet (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Cashu tokens verschijnen onmiddellijk in je saldo na betaling.



### Verzend tokens



Om Cashu-munten naar een andere gebruiker te sturen, raak je de knop "Verzenden" aan op het hoofdscherm en selecteer je "Ecash". Voer het te versturen bedrag in (bijv. 50 sats) en voeg indien nodig een beschrijvende memo toe.



![Envoi Ecash](assets/fr/07.webp)



Deel de QR-code of gegenereerde tekst via iMessage, Signal of Telegram. De ontvanger claimt het geld onmiddellijk en gratis.



### Token ontvangen



Om Cashu tokens te ontvangen die door een andere gebruiker zijn verzonden, raak je "Ontvangen" aan en selecteer je "Ecash". Scan de token QR-code of plak de ontvangen token link.



![Réception Ecash](assets/fr/08.webp)



Raak "Redeem" aan om token te claimen.



### Bliksem (Smelt) betalingen



Om een Lightning-factuur te betalen met uw Cashu-munten, raakt u "Verzenden" aan en selecteert u "Lightning". Plak een BOLT11-factuur die u wilt betalen.



![Paiement Lightning](assets/fr/11.webp)



De munt vernietigt uw tokens en voert de Lightning-betaling uit. U kunt dus voor elke Lightning-service betalen met behoud van uw anonimiteit.



### Wissel tussen mints



Wanneer je tokens ontvangt van een munt die je niet hebt geconfigureerd, biedt Macadamia je verschillende opties om deze tokens te beheren.



![Swap inter-mints](assets/fr/09.webp)



Voeg de nieuwe munt toe of ruil de tokens met een bestaande munt. De swap gebruikt Lightning als een brug om je geld anoniem over te maken.



### Geavanceerd beheer van meerdere muntsoorten



Macadamia biedt geavanceerde tools om meerdere mints tegelijk te beheren en je fondsen strategisch toe te wijzen.



![Gestion multi-mints](assets/fr/10.webp)



"Distribute Funds" verdeelt automatisch je saldo volgens percentages (bijv. 50/50). met "Transfer" kun je handmatig geld overboeken tussen mints om je risico's te spreiden.



## Voordelen en beperkingen



**Highlights** :





- Maximale vertrouwelijkheid**: Onvindbare transacties, zelfs door de munt. Geen blockchain metadata, spoorloze peer-to-peer uitwisselingen.
- Snel en gratis**: Gratis onmiddellijke overschrijvingen binnen een munt, ideaal voor microbetalingen.
- Interoperabiliteit**: gestandaardiseerde Cashu tokens voor gebruik met andere compatibele wallets (Minibits, Nutstash).
- Eenvoud**: Interface iOS native is toegankelijk voor beginners terwijl het controleerbaar blijft (open source).



**Constraints** :





- Bewaringsmodel**: muntvertrouwen vereist. Als een munt verdwijnt, verliezen uw munten hun waarde.
- alleen iOS**: Geen Android/desktop versie. Cashu interoperabiliteit maakt toegang via andere wallets mogelijk, maar de optimale ervaring blijft iOS.
- Afhankelijkheid van Mint**: Mint offline = niet in staat om transacties uit te voeren die haar tussenkomst vereisen (Mint, Melt).
- Opkomende technologie** : Actieve ontwikkeling, mogelijke bugs, evoluerende standaarden.



## Beste praktijken





- Diversifieer uw munten**: Verdeel je chips over verschillende gerenommeerde mints om het risico te verkleinen.
- Bedrag beperken**: Gebruik Macadamia als een fysieke wallet voor dagelijkse betalingen, niet als een kluis.
- Beveilig je seed**: Bewaar je 12-woorden zin op papier op een veilige plek. Test de restauratie af en toe.
- Controleer mints**: Raadpleeg cashu.space en communityforums voordat u een mint toevoegt. Kies mints met een goede uptime en een goede reputatie.
- VPN of Tor**: Verberg je IP met VPN/Tor voor maximale netwerkprivacy.
- Word lid van de community**: Telegram/Discord Cashu groepen voor updates, mint aanbevelingen en best practices.



## Conclusie



Macadamia Wallet brengt de eigenschappen van fysiek geld naar digitaal Bitcoin. Door Chaum en Lightning blinde handtekeningen te combineren, biedt het een elegante oplossing voor vertrouwelijkheid van transacties. De native iOS interface maakt geavanceerde cryptografische technologie toegankelijk terwijl het open source en interoperabel blijft met het Cashu ecosysteem.



Het custodial model vereist waakzaamheid en goede beveiligingspraktijken. Op de juiste manier gebruikt, wordt Macadamia een hulpmiddel van onschatbare waarde voor alledaagse betalingen die anonimiteit vereisen, als aanvulling op niet-custodiale spaarportemonnees.



## Bronnen



### Officiële documentatie




- Officiële website: [macadamia.cash](https://macadamia.cash)
- Macadamia FAQ: [macadamia.cash/faq](https://macadamia.cash/faq)
- GitHub broncode: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Cashu documentatie




- Technische documentatie: [docs.cashu.space](https://docs.cashu.space)
- Lijst van publieke munten: [bitcoinmints.com](https://bitcoinmints.com)
- Officiële protocolwebsite: [cashu.space](https://cashu.space)



### Gemeenschap




- Telegram Cashu-groep: [t.me/cashu_ecash](https://t.me/cashu_ecash)