---
name: ArkadeOS
description: Complete gids voor de Arkade-portfolio en het Ark-protocol
---

![cover](assets/cover.webp)



Het Bitcoin netwerk staat voor een grote uitdaging: schaalbaarheid. Hoewel de hoofdlaag (laag 1) ongeëvenaarde veiligheid en decentralisatie biedt, kan het slechts een beperkt aantal transacties per seconde verwerken. Lightning Network heeft zich ontpopt als een veelbelovende second-layer (laag 2) oplossing, die snelle, goedkope betalingen mogelijk maakt. Lightning legt echter zijn eigen beperkingen op: kanaalbeheer, de behoefte aan inkomende liquiditeit en een technische complexiteit die nieuwe gebruikers kan afschrikken.



Dit is de achtergrond van **Ark**, een nieuw laag 2 protocol ontworpen om een vereenvoudigde gebruikerservaring te bieden zonder soevereiniteit op te offeren. **ArkadeOS** (of Arkade) is de eerste grote implementatie van dit protocol en biedt een Bitcoin portfolio van de volgende generatie.



Deze tutorial leidt u door de wereld van Arkade. We onderzoeken hoe het Arkade protocol werkt, hoe je de Arkade wallet installeert en configureert, en hoe je het gebruikt om bitcoins direct, vertrouwelijk en zonder de gebruikelijke Lightning Network wrijvingen te versturen en ontvangen.



## Het Ark-protocol begrijpen



Voordat we in het gebruik van Arkade duiken, is het essentieel om de belangrijkste concepten van het Ark-protocol te begrijpen. Ark is geen aparte blockchain, maar een intelligent coördinatiemechanisme bovenop Bitcoin.



### Het VTXO-concept


Het hart van Ark is de **VTXO** (Virtual UTXO). Een VTXO is een UTXO die nog niet is gepubliceerd op de Bitcoin blockchain: het bestaat buiten de hoofdketen (off-chain), maar wordt ondersteund door transacties die vooraf zijn ondertekend op de blockchain.



In tegenstelling tot een saldo op een gecentraliseerde beurs, is een VTXO echt van jou. Je hebt een cryptografisch bewijs waarmee je op elk moment de corresponderende echte bitcoins op de blockchain kunt claimen, zelfs als de Ark-server verdwijnt. Met VTXO's kunt u direct waarde overdragen tussen gebruikers zonder te wachten op blokbevestigingen.



### De rol van de ASP (Ark Service Provider)


Het Ark-protocol werkt volgens een client-servermodel. De server wordt **ASP** (Ark Service Provider) genoemd. De ASP speelt de rol van dirigent:




- Het zorgt voor de nodige liquiditeit voor het netwerk.
- Het coördineert transacties tussen gebruikers.
- Het organiseert afwikkelingsrondes op de blockchain.



Het is cruciaal om op te merken dat ASP **on-custodial** is. Het bezit nooit je privésleutels, noch kan het je geld stelen. Haar rol is puur technisch en logistiek. Als een ASP je transacties censureert of uitvalt, kun je altijd je geld terugkrijgen via een eenzijdige exitprocedure.



### Rondes en privacy


Transacties op Ark worden afgerond in batches die **Ronden** worden genoemd. Periodiek (bijvoorbeeld elke paar seconden) verzamelt de ASP alle lopende transacties en verankert ze op de Bitcoin blockchain in een enkele geoptimaliseerde transactie.


Dit mechanisme biedt twee grote voordelen:




- Schaalbaarheid**: Een enkele on-chain transactie kan duizenden off-chain betalingen valideren, wat de kosten voor gebruikers drastisch verlaagt.
- Vertrouwelijkheid**: Elke ronde fungeert als een **CoinJoin**. Geld van alle deelnemers wordt gemengd in een gemeenschappelijke pool voordat het wordt herverdeeld in de vorm van nieuwe VTXO's. Dit verbreekt de link tussen zender en ontvanger. Dit verbreekt de link tussen zender en ontvanger, waardoor het extreem moeilijk, zo niet onmogelijk, wordt voor een buitenstaander om betalingen te traceren.



## Presentatie ArkadeOS



ArkadeOS is de concrete toepassing die het Ark-protocol beschikbaar maakt voor het grote publiek. Het is ontwikkeld door Ark Labs en is een compleet ecosysteem dat bestaat uit een portfolio (Wallet), een server (Operator) en ontwikkelaarstools.



Voor de eindgebruiker heeft Arkade de vorm van een elegante, intuïtieve web wallet (PWA - Progressive Web App). Het verbergt de cryptografische complexiteit van VTXO's en rondes achter een vertrouwde interface. Met Arkade heb je een adres om te ontvangen, een knop om te verzenden en een transactiegeschiedenis, net als een klassieke wallet, maar met de kracht van Ark's directheid en vertrouwelijkheid.



## Installatie en configuratie



Omdat Arkade een Progressive Web App is, is het bijzonder eenvoudig te installeren en hoeft er niet per se een traditionele applicatiewinkel aan te pas te komen.



### Toegang en installatie


Je hebt rechtstreeks toegang tot Arkade vanuit elke moderne webbrowser (Chrome, Safari, Brave) op computer of mobiel.





- Bezoek de officiële website van de applicatie: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



U wordt begroet door een reeks introductieschermen die u kennis laten maken met de belangrijkste concepten van Arkade: een nieuw ecosysteem voor Bitcoin, het belang van zelfbewaring en de voordelen van batchtransacties.



![arkade onboarding](assets/fr/02.webp)





- Op Android (Chrome/Brave)** : Druk op het browsermenu (drie puntjes) en selecteer "Applicatie installeren" of "Toevoegen aan beginscherm".
- Op iOS (Safari)**: Druk op de deelknop (vierkantje met pijltje naar boven) en kies "Op beginscherm".



Eenmaal geïnstalleerd start Arkade op als een native applicatie, schermvullend en zonder adresbalk.



### Portfolio maken


Bij de eerste start wordt je gevraagd om je portfolio te configureren.





- Klik op **"Nieuw Wallet aanmaken"**.



![create wallet](assets/fr/03.webp)





- De wallet wordt onmiddellijk aangemaakt. In tegenstelling tot traditionele Bitcoin wallets, gebruikt **Arkade geen 12- of 24-woord herstelzin**. In plaats daarvan genereert Arkade automatisch een **private sleutel** in Nostr (nsec) formaat, die wordt gebruikt om een back-up te maken van uw wallet en deze te herstellen. Vergeet niet om deze sleutel onmiddellijk op te slaan (zie volgende paragraaf).





- Je ziet het scherm "Je nieuwe wallet is live!", dat bevestigt dat je wallet klaar is voor gebruik. Klik op **"GO TO WALLET"** om naar de hoofdinterface te gaan.



Eenmaal in je wallet, ga je naar de hoofdinterface van Arkade. Hier vind je je saldo, knoppen voor het verzenden en ontvangen van geld, en een "Apps" tab die toegang geeft tot geïntegreerde applicaties zoals Boltz (Lightning exchange), LendaSat en LendaSwap (leendiensten), en Fuji Money (synthetische activa).



![wallet interface](assets/fr/04.webp)



### Verbinding met ASP


Standaard is het portfolio automatisch geconfigureerd om verbinding te maken met de officiële Arkade Labs ASP. U kunt controleren met welke server u verbonden bent door naar **Instellingen** > **Over** te gaan. Daar ziet u het serveradres (momenteel `https://arkade.computer`).



In de huidige versie van Arkade (Beta) is het niet mogelijk om de ASP-server handmatig aan te passen. De applicatie maakt automatisch verbinding met de officiële Arkade Labs ASP. In de toekomst kunnen gebruikers mogelijk kiezen tussen verschillende ASP's op basis van hun voorkeuren, maar deze functie is nog niet beschikbaar.



### Een back-up maken van je privésleutel


**Arkade gebruikt een privésleutel in Nostr (nsec) formaat als back-up- en herstelmethode. Om een back-up te maken van uw privésleutel :





- Ga naar **Instellingen** op het hoofdscherm.
- Selecteer **"Back-up en privacy"**.
- Je ziet je **private key** weergegeven in `nsec...` formaat. Deze lange reeks karakters is je enige manier om je wallet te herstellen.
- Druk op **"COPY NSEC TO CLIPBOARD"** om je privésleutel te kopiëren.
- Bewaar deze sleutel op een veilige plek**: schrijf hem op papier, sla hem op in een veilige wachtwoordmanager of gebruik een andere back-upmethode die bij u past.
- Arkade biedt ook de optie **"Schakel Nostr-back-ups in"**. Deze functie gebruikt het Nostr-protocol (een gedecentraliseerd netwerk) om automatisch een back-up te maken van bepaalde gegevens van uw wallet in versleutelde vorm naar Nostr relais. Dit vergemakkelijkt de synchronisatie tussen meerdere apparaten en biedt een eenvoudiger herstel van de status van uw wallet.



**Belangrijk**: Nostr-back-ups zijn alleen een **comfort** functie. Ze vervangen niet de back-up van uw nsec-sleutel. Nostr-relais garanderen geen permanente gegevensopslag. Uw nsec-privésleutel blijft uw enige gegarandeerde manier om uw fondsen terug te krijgen.



![backup private key](assets/fr/05.webp)




## Arkade gebruiken



Zodra je je wallet hebt ingesteld, ben je klaar om de mogelijkheden van Arkade te verkennen. De interface is ontworpen om de verschillende soorten Bitcoin betalingen (On-chain, Lightning, Ark) naadloos te verenigen.



### Geld ontvangen



Om uw portefeuille te financieren, drukt u op **"Ontvangen"**. Arkade biedt drie ontvangstmethoden:





- Ark betaling**: Als de verzender ook Arkade gebruikt, deel dan je Ark-adres voor een directe, vertrouwelijke en vrijwel gratis overboeking.
- Kettingstorting (Instappen)**: Gebruik het Bitcoin adres (`bc1p...`) om te ontvangen van een klassieke wallet of een beurs. Wacht op bevestiging (~10 min) voordat het geld wordt omgezet in VTXO's.
- Lightning-swap**: Genereer een Lightning-factuur en betaal deze vanaf een externe wallet Lightning. Het geld komt direct binnen via een automatische swap.



![receive amount](assets/fr/06.webp)



Het ontvangstscherm toont alle beschikbare opties: QR-code, Ark-adres, Bitcoin-adres (BIP21) en Lightning-factuur. Houd voor Lightning-betalingen de applicatie open tijdens de transactie.



![receive confirmation](assets/fr/07.webp)



### Geld sturen



Om geld te versturen, drukt u op **"Verzenden"** en plakt u het adres van de ontvanger of scant u de QR-code. Arkade detecteert automatisch het vereiste type betaling:





- Ark** betaling: Naar een Ark-adres is de overboeking direct, privé en vrijwel gratis (0 SATS-kosten). De ontvanger hoeft niet online te zijn.
- Lightning** betaling: Scan een Lightning-factuur (`lnbc...`) en Arkade voert automatisch een swap uit. De ASP betaalt de factuur voor u en debiteert uw Arkade-saldo.
- On-chain betaling**: Naar een klassiek Bitcoin adres (`bc1q...` of `bc1p...`) initieert Arkade een "Collaborative Output" die in de volgende on-chain ronde wordt opgenomen.



Controleer de details in het scherm "Transactie ondertekenen" en bevestig vervolgens met **"TAP TO SIGN"**.



![send payment](assets/fr/08.webp)



**Huidige beperking (Beta)**: VTXO's die minder dan 24 uur geleden zijn aangemaakt, kunnen niet worden gebruikt voor on-chain uitgangen. Als je een foutmelding krijgt, wacht dan tot je VTXO's "volwassen" zijn.



**on-chain uitvoer vertrouwelijkheid**: Het onderstaande voorbeeld toont een [Ark uitvoer transactie op mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). We observeren een verdeelde invoer naar 4 verschillende uitgangen, zoals een CoinJoin. Voor een externe waarnemer is het onmogelijk om te bepalen welke hoeveelheid bij welke gebruiker hoort.



![transaction ark mempool](assets/fr/11.webp)



## Geavanceerde functies



### Vervalbeheer VTXO


Een technisch kenmerk van het Ark protocol is dat VTXO's een **gelimiteerde levensduur** hebben. Deze tijdsbeperking is inherent aan het ontwerp van het protocol. De verlooptijd is instelbaar door elke ASP server; op de officiële Arkade Labs ASP is deze periode ongeveer **4 weken (≈30 dagen)**.



**Door deze beperking kan de Ark-server de liquiditeit efficiënt beheren en VTXO's van inactieve gebruikers opruimen. Na afloop kan de Ark-server technisch gezien de resterende fondsen in de VTXO-structuur opeisen.



**Om uw VTXO's actief te houden, moeten ze "ververst" worden voordat ze verlopen. Verversen bestaat uit het deelnemen aan een nieuwe "ronde" waarbij uw VTXO's die bijna verlopen zijn, worden omgeruild voor nieuwe VTXO's met een nieuwe volledige geldigheidsperiode (≈30 dagen op Arkade Labs ASP).



Het Arkade portfolio beheert dit proces automatisch: de applicatie controleert voortdurend de status van uw VTXO's en vernieuwt ze automatisch een paar dagen voordat ze verlopen. Zolang u uw applicatie regelmatig opent (minstens één keer per week), blijven uw VTXO's automatisch actief.



**Als u uw portefeuille langer dan 4 weken niet opent, zullen uw VTXO's vervallen. U verliest uw fondsen echter niet: u behoudt de mogelijkheid om ze terug te krijgen via een **unilaterale uitstap** (zie volgende sectie). Deze procedure is duurder en trager, maar zorgt ervoor dat uw fondsen recupereerbaar blijven.



De noodzaak om de applicatie regelmatig te openen maakt Arkade tot een **"Hot Wallet"** ontworpen voor dagelijkse uitgaven, geen kluis voor langetermijnsparen. Om bitcoins op te slaan zonder ze lang te gebruiken, kies je beter voor een koude wallet hardware.



**Controleer de status van uw VTXO's**: Je kunt de status van je VTXO's controleren in **Instellingen** > **Geavanceerd**. Zie "Volgende vernieuwing" om te zien wanneer de volgende automatische vernieuwing zal plaatsvinden, en "Virtuele munten" om een gedetailleerde lijst van al je VTXO's met hun vervaldatum te zien.



![vtxo management](assets/fr/09.webp)



### Unilateraal vertrek



Unilateral exit is een **fundamentele cryptografische garantie** van het Ark protocol dat ervoor zorgt dat je je geld terugkrijgt, zelfs als de ASP verdwijnt, je transacties censureert of weigert mee te werken. Technisch gezien zijn je VTXO's **voorafgetekende Bitcoin transacties** die van jou zijn. In een absoluut noodgeval kun je deze transacties uitzenden op de Bitcoin blockchain om je fondsen terug te krijgen zonder toestemming van iemand.



**Hoe werkt het? Het proces verloopt in twee stappen. Eerst **Uitrollen**: je zendt de vooraf ondertekende transacties die je VTXO's vormen sequentieel uit in de transactieboom. Dan de **Finalisatie**: zodra de timelocks verlopen zijn (meestal 24 uur), haal je je bitcoins op van een standaardadres.



**Huidige status in Arkade**: In de bètaversie is er nog geen knop of eenvoudige gebruikersinterface voor eenzijdige uitvoer. Deze functionaliteit vereist momenteel het gebruik van de Arkade SDK en technische kennis van TypeScript programmeren.



**Zelfs als de procedure niet met één druk op de knop toegankelijk is, is de cryptografische garantie er. Je VTXO's bevatten vooraf ondertekende transacties die rechtmatig van jou zijn. Het is deze technische garantie die Ark tot een **non-custodial** protocol maakt: zelfs in het ergste geval blijven uw fondsen technisch herstelbaar. Een vereenvoudigde interface zal waarschijnlijk worden toegevoegd in toekomstige versies van Arkade.



## Voordelen en beperkingen



Om Arkade in de juiste context te plaatsen, zullen we de huidige sterke en zwakke punten samenvatten.



### Hoogtepunten




- Gebruikerservaring (UX)**: Geen kanaalbeheer, inkomende capaciteit of complexe kanaalback-ups zoals bij Lightning. Gewoon installeren en gebruiken.
- Privacy** : De standaard CoinJoin architectuur biedt een veel hoger niveau van anonimiteit dan standaard on-chain of Lightning transacties.
- Interoperabiliteit**: Betaal elke Bitcoin QR code (On-chain of Lightning) vanuit één enkele interface.



### Beperkingen




- Jong protocol**: Ark is een zeer recente technologie. Er kunnen bugs in zitten. Het is raadzaam om Ark niet te gebruiken om bedragen op te slaan waarvan het verlies kritiek zou zijn.
- ASP-afhankelijkheid**: Hoewel het niet verplicht is, is het systeem afhankelijk van de beschikbaarheid van ASP voor vloeibaarheid. Als de ASP offline is, kun je niet langer direct transacties uitvoeren (alleen je on-chain fondsen uitvoeren).
- Alleen Hot Wallet** : De noodzaak om de toepassing regelmatig te openen om VTXO's te verversen is niet geschikt voor koude opslag (Cold Opslag).



## Vergelijking: Arkade vs Bliksem vs Cashu



Om de positionering van Arkade beter te begrijpen, vergelijken we het met de andere twee grote schaalbaarheidsoplossingen.



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** is het ideale compromis: de eenvoud en vertrouwelijkheid van Cashu, maar met de soevereiniteit (niet-vrijblijvend) van Lightning.



## Ondersteuning en hulp



Als u problemen ondervindt of vragen hebt tijdens het gebruik van Arkade, biedt de applicatie verschillende ondersteuningsopties:





- Ga naar **Instellingen** > **Ondersteuning**.
- Je vindt verschillende opties:
  - Klantenondersteuning**: Krijg hulp bij je portfolio, meld bugs of stel vragen.
  - Veilig chatten**: Je gesprekken zijn veilig en privé en de geschiedenis wordt tussen sessies bewaard.
  - Bugrapporten**: Meld alle problemen die je tegenkomt, inclusief stappen om ze te reproduceren.
  - Volg de voortgang**: Houd uw supporttickets en conversaties altijd bij.



![support](assets/fr/10.webp)



Het Arkade-team is ook actief op Telegram via het @arkade_os-kanaal voor ondersteuning en integratiemogelijkheden.



## Belangrijke opmerking: Toepassing in bèta



**⚠️ Arkade is momenteel in Openbare Beta op de mainnet Bitcoin**. Hoewel de applicatie functioneel is met echte bitcoins, is het belangrijk om bepaalde voorzorgsmaatregelen te nemen.



### Aanbevelingen voor gebruik




- Gebruik kleine bedragen**: Vermijd het opslaan van grote bedragen op Arkade. Gebruik deze wallet voor je dagelijkse uitgaven en bewaar je spaargeld op een koude wallet hardware.
- Mogelijke bugs en beperkingen**: Zoals bij elke toepassing die actief wordt ontwikkeld, kan Arkade bugs of onverwacht gedrag vertonen. Meld eventuele problemen via geïntegreerde ondersteuning.
- Snelle evolutie** : De applicatie en het protocol worden voortdurend verbeterd. Sommige functies kunnen veranderen of worden toegevoegd in toekomstige versies.



### Huidige bekende beperkingen




- 24-uurs vertraging op VTXO's** : Nieuw aangemaakte VTXO's kunnen niet onmiddellijk worden gebruikt voor on-chain uitgangen.
- ASP uniek**: Het is nog niet mogelijk om de ASP-server in de toepassing te wijzigen.
- Technische eenzijdige uitvoer**: Nog geen vereenvoudigde interface voor eenzijdige uitvoer (SDK vereist).



Het team van Arkade Labs werkt er actief aan om deze beperkingen in toekomstige versies te versoepelen.



## Conclusie



ArkadeOS betekent een belangrijke doorbraak in het Bitcoin ecosysteem. Door het Ark protocol te implementeren, bewijst het dat het mogelijk is om gebruiksgemak te verenigen met de fundamentele principes van Bitcoin: vertrouw niet, verifieer.



Hoewel Arkade nog in de kinderschoenen staat, biedt het een fascinerende glimp van hoe de toekomst van Bitcoin betalingen eruit zou kunnen zien: direct, privé en toegankelijk voor iedereen zonder technische vereisten. Het is het perfecte hulpmiddel voor uw dagelijkse uitgaven, als aanvulling op uw veilige spaaroplossing (Cold Wallet).



We moedigen u aan om Arkade te testen met kleine hoeveelheden om dit nieuwe protocol zelf te ontdekken. Het ecosysteem ontwikkelt zich snel en Arkade loopt voorop in deze innovatie.



## Bronnen



Raadpleeg de officiële bronnen voor meer informatie:





- Arkade** website: [arkadeos.com](https://arkadeos.com)
- Documentatie**: [docs.arkadeos.com] (https://docs.arkadeos.com)
- Ark** protocol: [ark-protocol.org] (https://ark-protocol.org)
- Broncode** : [GitHub Arkade](https://github.com/arkade-os)