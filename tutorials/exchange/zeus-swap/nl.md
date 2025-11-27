---
name: Zeus Wissel
description: Niet-custodiale Exchange dienst tussen On-Chain en Lightning Network bitcoins
---

![cover](assets/cover.webp)



Het Bitcoin ecosysteem presenteert een dualiteit: het hoofdnetwerk (On-Chain) biedt maximale veiligheid, terwijl Lightning Network directe transacties mogelijk maakt. Deze twee-Layer architectuur creëert een praktische uitdaging: hoe kunnen fondsen efficiënt worden overgedragen tussen deze twee lagen zonder gecentraliseerde tussenpersonen?



Het probleem is concreet: je ontvangt een Lightning-betaling maar wilt deze bewaren in Cold opslag, of omgekeerd, je hebt On-Chain bitcoins maar hebt Lightning-liquiditeit nodig. Traditionele oplossingen omvatten het handmatig openen/sluiten van Lightning-kanalen (duur en technisch) of gecentraliseerde platforms die KYC vereisen.



Zeus Swap lost dit probleem op met een geautomatiseerde, niet-betaalbare Exchange service. Ontwikkeld door Zeus LSP, kunt u On-Chain bitcoins bidirectioneel omzetten in Lightning satoshis, zonder uw fondsen toe te vertrouwen aan een tussenpersoon. Het proces maakt gebruik van atomaire contracten (HTLC) die garanderen dat de Exchange wordt voltooid of geannuleerd.



De innovatie ligt in de eenvoud: slechts een paar klikken voor een Exchange die je financiële soevereiniteit behoudt, zonder registratie of KYC.



## Wat is Zeus Swap?



Zeus Swap is een liquiditeit Exchange dienst ontwikkeld door Zeus LSP die atomaire swaps tussen het hoofdnetwerk Bitcoin en Lightning Network mogelijk maakt. Het is een technische infrastructuur die gebruik maakt van onderzeese swaps en omgekeerde swaps om tweerichtingsconversies tussen On-Chain BTC en Lightning-satoshi's mogelijk te maken, terwijl het niet-custodiale karakter van de operatie behouden blijft.



### Technische architectuur



Zeus Swap maakt gebruik van Boltz' open-source Bitcoin/Lightning atomic swap technologie. Het protocol gebruikt Hash Time Locked Contracts (HTLC): contracten die fondsen vergrendelen met twee voorwaarden voor vrijgave (onthulling van een cryptografisch geheim of verstrijken van de tijd).



Voor een onderzeese swap (On-Chain → Lightning) stuurt de gebruiker bitcoins naar een Address waarin de Hash van een Lightning Invoice is opgenomen. Zeus LSP ontgrendelt deze tegoeden alleen door de corresponderende Invoice te betalen, waarbij de pre-image wordt onthuld die de bitcoins automatisch ontgrendelt. Dit mechanisme garandeert atomiciteit.



Voor een omgekeerde swap (Lightning → On-Chain) betaalt de gebruiker een Lightning Invoice van Zeus LSP, waarbij een pre-image wordt onthuld waarmee een voorbereide Bitcoin transactie kan worden vrijgegeven aan de Address van bestemming.



Voor meer informatie over hoe de Lightning Network werkt, kun je onze speciale cursus bekijken:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Bedrijfsmodel



Zeus LSP treedt op als market maker en handhaaft On-Chain en Lightning liquiditeit om swaps te honoreren. Voor swaps past Zeus een variabele vergoeding toe (gewoonlijk 0,1% tot 0,5%, afhankelijk van richting en voorwaarden) plus Bitcoin's Mining vergoeding, transparant weergegeven voorafgaand aan validatie.



Als Lightning Service Provider optimaliseert Zeus de kosten dankzij zijn expertise in het on-demand openen van kanalen, efficiënte routing en liquiditeitsoplossingen op maat.



### Integratie



Zeus Wallet integreert de service, waardoor wisselen mogelijk is zonder Interface Bitcoin/Lightning te verlaten. Dit elimineert de wrijving van kopiëren en plakken tussen toepassingen.



Het onafhankelijke Interface web blijft toegankelijk voor alle portemonnees en garandeert maximale flexibiliteit in het gebruik.



## Belangrijkste kenmerken



### Bidirectionele swaps



Zeus Swap biedt twee soorten Exchange:



**Submarine swaps (On-Chain → Lightning)**: injecteer Lightning liquiditeit vanuit je Bitcoin reserves, handig om een mobiele Wallet of Lightning node te voeden zonder handmatig kanalen te openen.



**Reverse swaps (Lightning → On-Chain)**: Lightning-satoshis omzetten in On-Chain bitcoins voor opslag op lange termijn, zodat dure kanaalsluitingen vermeden worden.



### Gebruikersinterfaces



**Interface web** (swaps.zeuslsp.com): vereenvoudigde ervaring zonder registratie, begeleid proces met realtime weergave van kosten en status.



**Zeus Wallet integratie**: directe swaps vanuit de applicatie, automatisch beheer van facturen en adressen, waardoor afhandelingsfouten worden geëlimineerd.



### Veiligheid en herstel



Elke ruil genereert een unieke Contract met onveranderlijke parameters: Hash Bliksem, time-out, restitutie Address. Bij storing automatisch herstel via de Address, onafhankelijk van Zeus LSP.



**Zeus Swaps Reddingssleutel**: tijdens een On-Chain → Lightning swap genereert Zeus automatisch een universele herstelsleutel ter vervanging van de oude individuele restitutiebestanden. Deze unieke sleutel werkt op elk apparaat en voor alle swaps die ermee zijn gemaakt. Het is cruciaal om deze sleutel te downloaden en op te slaan op een veilige locatie om je geld terug te kunnen krijgen in het geval van een mislukte swap.



### Netwerkoptimalisatie



Zeus Swap past automatisch verlooptijden en Mining vergoedingen aan op basis van netwerkomstandigheden. Zeus-gebruikers profiteren van geavanceerde opties: keuze van LSP, aangepaste vertragingen, compatibiliteit met andere diensten (Boltz).



## Installatie en gebruik



### Toegangsmethoden



**Interface web** (swaps.zeuslsp.com): universele oplossing die compatibel is met alle portemonnees, geen installatie vereist, ideaal voor incidenteel gebruik.



**Zeus app** (iOS/Android): geïntegreerde ervaring die Wallet en swaps combineert, geschikt voor regelmatige gebruikers.



Bekijk onze Zeus-handleiding voor meer informatie over deze complete Wallet :



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Webconfiguratie



**On-Chain → Lightning**: Het proces begint met het configureren van de swap op het Interface web Zeus Swap. De gebruiker kan de pijl tussen de velden On-Chain en Lightning gebruiken om de richting van de wissel om te keren.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: selectie van bedrag (Sats 50.000 → Sats 49.648 na kosten) met transparante weergave van netwerkkosten (Sats 302) en Zeus-dienst (Sats 50).*



Tijdens het proces biedt Zeus je aan om de universele herstelsleutel te downloaden:



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Downloaddialoog voor de Zeus Swaps Rescue Key - een universele sleutel die de oude individuele vergoedingsbestanden vervangt*



Als je al een sleutel hebt, kun je die met Zeus controleren:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface om de geldigheid van een bestaande Zeus Swaps Rescue Key* te controleren



Eenmaal geconfigureerd, genereert Zeus het Bitcoin depot Address en geeft de instructies weer:



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Swap voltooiingspagina: QR-code en Bitcoin Address voor het verzenden van 50.000 Satss, met herinnering aan vervaldatum van 24 uur*



De swap wacht dan op bevestiging van Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Status "Transactie in Mempool" - wacht op Bitcoin bevestiging om de ruil af te ronden*



Na bevestiging wordt de ruil automatisch voltooid:



![Swap réussi](assets/fr/06.webp)



*Bevestiging van succes: 49.648 Sats ontvangen op Lightning na aftrek van netwerk- en servicekosten*



### De Zeus-app gebruiken



**Lightning → On-Chain**: De Zeus-toepassing biedt een geïntegreerde ervaring voor omgekeerde swaps (Lightning tot Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Zeus hoofdscherm met Lightning (69.851 Sats) en On-Chain (38.018 Sats) balansen, toegang tot ruilen via het zijmenu*



![Configuration du swap reverse](assets/fr/08.webp)



*Interface omgekeerde ruil maken: 50.000 Sats Lightning → 49.220 Sats On-Chain, met netwerkkosten (530 Sats) en service (250 Sats) duidelijk weergegeven. Gebruikers kunnen handmatig een Bitcoin ontvangende Address, of generate een automatisch van de Wallet Zeus invoeren via de "generate On-Chain Address" knop.*



![Finalisation du swap mobile](assets/fr/09.webp)



*Afrondingsschermen: Lightning Invoice betalingsscherm met "BETAL DIT Invoice", bevestiging van succesvolle Lightning-betaling in 9,96 seconden, en saldooverzicht met de 49.162 Sats die op bevestiging wachten*



### Bewaking en beveiliging



Elke swap heeft een unieke identificatie met realtime tracering. Volledige voortgangsweergave, automatische waarschuwingen voor vervaldatums. Automatische laadaanbevelingen op basis van netwerkomstandigheden.



## Voordelen en beperkingen



### Voordelen





- Eenvoud**: Wisselen in een paar klikken vs. handmatige kanaalmanipulatie
- Non-custodial**: geen KYC, geen rekening, geld nooit toevertrouwd aan een derde partij
- Transparantie**: kosten expliciet weergegeven vóór validatie (0,1% tot 0,5% + minage afhankelijk van gebruikerstests - controleer huidige kosten bij elke swap)
- Mobiele integratie**: native ervaring in Zeus Wallet



### Beperkingen





- Vervaltermijnen**: 24-48 uur maximaal, mislukking als Bitcoin niet op tijd bevestigd is
- Bedraglimieten**: minimum 25.000 Sats, Zeus LSP liquiditeit variabel volgens voorwaarden
- Traceert On-Chain**: HTLC scripts mogelijk identificeerbaar door Blockchain analyse
- Bevestiging vereist**: minimaal 10 minuten voor Bitcoin validatie



## Beste praktijken



### Timing en kosten





- Let op Mempool.space voor tijden van lage congestie
- Geef de voorkeur aan weekends en daluren om Mining kosten te beperken
- Bereken winstgevendheid: kleine bedragen vs. directe kanaalopening



### Beveiliging





- Controleer de Bitcoin adressen zorgvuldig (kopiëren-plakken aanbevolen)
- Maak een back-up van de Zeus Swaps herstelsleutel**: download de herstelsleutel en bewaar deze op een veilige plaats
- Document: Contract ID, restitutie Address, vervaldatum
- Gebruik de juiste Mining vergoedingen voor tijdige bevestiging



### Gebruiksstrategie





- Balans On-Chain/Lightning liquiditeit naar wens
- Zeus Swap voor eenmalige aanpassingen, directe kanalen voor permanente behoeften



## Vergelijking met andere swapservices



### Zeus Swap vs Boltz Exchange



Zeus Swap gebruikt de backend-technologie van Boltz, maar brengt enkele cruciale verbeteringen aan:



**Zeus Swap voordelen** :




- Interface verenigd**: native integratie in Zeus Wallet vs Interface webtechniek Boltz
- WebSocket API**: realtime updates vs. handmatig pollen
- Geautomatiseerd beheer**: automatische facturering en Address beheer
- Mobiele ondersteuning**: alleen optimalisatie voor smartphone vs. desktop
- Swagger-documentatie**: complete REST API voor ontwikkelaars



**Boltz blijft voordelig** voor totale onafhankelijkheid en gebruik met elke Bitcoin/Lightning opstelling.



Zeus Swap transformeert bewezen Boltz-technologie in een mainstream gebruikerservaring, vergelijkbaar met het verschil tussen een ruw protocol en een gebruiksvriendelijke applicatie.



### Zeus Swap vs Phoenix/Breez (geïntegreerde swaps)



Phoenix en Breez integreren transparante swapfunctionaliteiten die de technische complexiteit voor de eindgebruiker verbergen. Phoenix gebruikt een automatisch swap-in/swap-out systeem waarbij de gebruiker geen expliciet onderscheid maakt tussen Bitcoin lagen: hij "stuurt naar een Bitcoin Address" en de applicatie handelt de swap op de achtergrond af.



Deze ultra-gesimplificeerde aanpak is perfect geschikt voor beginners, maar beperkt het begrip en de controle over de bewerkingen. Zeus Swap gebruikt een meer educatieve filosofie: gebruikers begrijpen dat ze tussen twee verschillende lagen wisselen, waardoor ze geleidelijk hun begrip van het Layer Bitcoin ecosysteem ontwikkelen.



## Gedetailleerde vergelijking van vergoedingen en limieten (2024)



⚠️ **Waarschuwing**: Vergoedingen kunnen in de loop van de tijd variëren, afhankelijk van marktomstandigheden en service-updates. Controleer altijd de kosten die worden weergegeven in de Interface voordat u een ruil valideert.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap biedt een balans tussen gebruiksgemak en technische controle: toegankelijker dan Boltz, flexibeler dan Phoenix/Breez, met een strikte non-custodial aanpak.



## Conclusie



Zeus Swap vertegenwoordigt een belangrijke innovatie in het Bitcoin ecosysteem, en lost op elegante wijze de uitdaging van interoperabiliteit tussen het hoofdnetwerk en Lightning Network op. Door de cryptografische robuustheid van atomaire swaps te combineren met een toegankelijke gebruikerservaring, democratiseert deze dienst Bitcoin dual-Layer beheer zonder afbreuk te doen aan de principes van financiële soevereiniteit.



De niet-custodiale architectuur van Zeus Swap, geërfd van de bewezen Boltz-technologie, zorgt ervoor dat uw fondsen gedurende het hele swap-proces onder uw exclusieve controle blijven. Deze benadering respecteert de geest van Bitcoin en biedt tegelijkertijd het gebruikersgemak dat nodig is voor mainstream acceptatie. Transparante prijzen en het ontbreken van KYC-processen versterken deze unieke waardepropositie.



Voor de moderne Bitcoin gebruiker is Zeus Swap een strategisch hulpmiddel om de verdeling van liquiditeit naar behoefte te optimaliseren: On-Chain veilige opslag voor langetermijnsparen, Lightning beschikbaarheid voor dagelijkse uitgaven en microtransacties. Deze flexibiliteit verandert Bitcoin beheer van een technische beperking in een concurrentievoordeel.



De toekomstige evolutie van Zeus Swap, ondersteund door het ervaren Zeus LSP team en de Boltz open-source gemeenschap, belooft verdere verbeteringen op het gebied van kosten, verwerkingstijden en gebruikerservaring. Deze dienst maakt deel uit van de bredere trend naar volwassenheid van de Bitcoin infrastructuur, waarbij technische geavanceerdheid transparant wordt voor de eindgebruiker.



## Bronnen



### Officiële documentatie




- [Zeus Swap - Webportaal](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobiele toepassing](https://zeusln.app)
- [Blog Zeus - Aankondigingen en tutorials](https://blog.zeusln.com)
- [Zeus technische documentatie](https://docs.zeusln.app)



### Gemeenschap en ondersteuning




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)