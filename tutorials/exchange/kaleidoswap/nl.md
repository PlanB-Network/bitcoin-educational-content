---
name: KaleidoSwap
description: Gids voor gevorderden voor het verhandelen van RGB activa op Lightning Network met KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap is een geavanceerde open-source desktopapplicatie die de kloof overbrugt tussen het RGB Protocol en Lightning Network. Het dient als een uitgebreide interface voor het beheren van RGB Lightning Nodes, interactie met RGB Lightning Service Providers (LSP's) via de LSPS1 specificatie en het uitvoeren van atomaire swaps van RGB activa.


KaleidoSwap stelt gebruikers in staat om volledige controle over hun sleutels en gegevens te behouden. Door gebruik te maken van het client-side validatie paradigma van RGB, maakt het private en schaalbare smart contracts bovenop Bitcoin mogelijk. Deze tutorial duikt in de geavanceerde functies van KaleidoSwap en leidt u door de fijne kneepjes van "gekleurd" UTXO beheer, kanaalliquiditeit voor specifieke activa en het taker-maker handelsmodel, zodat u volledig gebruik kunt maken van dit krachtige gedecentraliseerde uitwisselingsprotocol.


## Installatie


KaleidoSwap biedt kant-en-klare binaries voor de belangrijkste besturingssystemen, maar voor geavanceerde gebruikers zorgt het bouwen vanaf de broncode ervoor dat u de nieuwste code gebruikt met uw specifieke configuraties.


### Binaries downloaden


Je kunt de laatste release voor jouw besturingssysteem downloaden van de [officiële website](https://kaleidoswap.com/) of de [GitHub releases pagina](https://github.com/kaleidoswap/desktop-app/releases).


### Installatiemethoden


1.  **Windows**: Download het installatieprogramma `.exe` en voer het uit.

2.  **macOS**: Download het bestand `.dmg`, open het en sleep KaleidoSwap naar je map Toepassingen.

3.  **Linux**: Download het `.AppImage` of `.deb` bestand en installeer/loop het.



## Opties voor knooppuntinstellingen


Wanneer je KaleidoSwap voor het eerst opstart, krijg je het **Connectiescherm** te zien. Dit is de eerste stap in het configureren van je omgeving.


![Node Selection Screen](assets/en/01.webp)


Je moet kiezen hoe je verbinding wilt maken met de RGB Lightning Network. Deze keuze heeft invloed op je mate van controle en privacy.


### Optie 1: lokaal knooppunt (aanbevolen voor zelfbehoud)


**Voor volledige controle en privacy**, draai een node direct op je machine, zie de voordelen hieronder:


- Zelfbehoud**: Jij hebt de sleutels in handen. Geen enkele derde partij kan uw geld bevriezen of uw transacties censureren.
- Privacy**: Je gegevens blijven op je apparaat.
- Onafhankelijkheid**: Geen afhankelijkheid van externe dienstverleners.


Als je **Local Node** selecteert, kom je in het instellingenscherm waar je een nieuwe wallet kunt aanmaken of een bestaande kunt herstellen.


![Local Node Setup Screen](assets/en/02.webp)


### Optie 2: Remote Node


Maak verbinding met een RGB Lightning Node op afstand (zelf gehost op een VPS of een gehoste provider).


- Voordelen**: Geen gebruik van lokale bronnen, 24/7 beschikbaarheid.
- Afweging**: Vereist vertrouwen in de host of beheer van een externe server.


![Remote Node Setup Screen](assets/en/03.webp)


**KaleidoSwap is ontworpen om zelf-custody mogelijk te maken.** We raden sterk aan om je eigen node te draaien - ofwel lokaal (optie 1) of door zelf een node op afstand te hosten - om de censuurbestendige eigenschappen van Bitcoin en RGB volledig te benutten.


## Een Wallet maken


KaleidoSwap beheert zowel Bitcoin als RGB middelen. Het wallet creatieproces initialiseert een sleutelbewaarplaats die je on-chain fondsen en je Lightning kanaaltoestanden beveiligt.


Dit is het gedetailleerde proces:

1. Open KaleidoSwap en selecteer **Local Node**.

2. Klik op **Nieuw Wallet aanmaken**.

3. **Account instellen**: Voer een **Accountnaam** in en selecteer het **Netwerk** (bijv. Bitcoin Mainnet, Testnet, Signet).

4. **Geavanceerde configuratie** (optioneel): Als u een krachtige gebruiker bent, kunt u aangepaste RPC eindpunten, Indexer URL's of Proxy-instellingen configureren onder "Geavanceerde instellingen".

5. Klik op **Doorgaan**.

6. **Wachtwoord**: Stel een sterk wachtwoord in om uw wallet bestand lokaal te versleutelen.

7. **Recovery Phrase**: Schrijf uw seed zin op en bewaar hem veilig.


    - Kritisch**: Deze zin is nodig om uw on-chain fondsen en node-identiteit terug te krijgen.
    - Waarschuwing**: **Bliksemkanaaltoestanden kunnen niet volledig hersteld worden van alleen de seed**. Je moet ook Static Channel Backups (SCB) onderhouden om in kanalen geblokkeerde fondsen te herstellen.


![Wallet Creation Screen](assets/en/04.webp)



## Dashboard Overzicht


Zodra je wallet is aangemaakt, kom je op het hoofdscherm **Dashboard**.


![KaleidoSwap Dashboard](assets/en/05.webp)


opmerking: De schermafbeelding hierboven toont een wallet die al gefinancierd is en actieve kanalen heeft. Een nieuwe wallet toont nul saldi en geen actieve kanalen totdat je hem financiert._


## Uw Wallet financieren


Om met RGB activa te werken, moet je je wallet financieren. KaleidoSwap ondersteunt het storten van zowel Bitcoin als RGB activa via on-chain transacties of de Lightning Network.


### Bitcoin storten


1. Klik op **Betalen** in het menu Snelle acties.

2. Selecteer **BTC** in de lijst met activa.


![Select BTC Asset](assets/en/06.webp)


3. Kies je stortingsmethode: **On-chain** of **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- On-chain**: Scan de QR-code of kopieer het adres om Bitcoin vanaf een andere wallet te verzenden.
- Bliksem**: Genereer een factuur voor het gewenste bedrag.


![BTC On-chain Deposit](assets/en/08.webp)


### RGB activa & gekleurde UTXO's storten


Om RGB activa (zoals USDT) te ontvangen, moet je specifieke UTXO's beschikbaar hebben om "gekleurd" te worden (een activum toegewezen krijgen).


1. Klik op **Deposit** en selecteer het RGB activum (bijv. USDT). **Belangrijk**: Als dit de **eerste keer** is dat uw knooppunt deze specifieke activa ontvangt, **laat dan het veld ID van de activa leeg**. Als je een ID invoert voor een onbekend activum, zal het knooppunt een foutmelding geven omdat het het nog niet herkent.

2. Kies **On-chain** of **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Ontvangstmodi op de ketting: Getuige vs. Verblind


Wanneer u RGB assets on-chain ontvangt, hebt u twee privacymodi:



- Blind ontvangen (aanbevolen voor privacy)**: Je geeft een "blinded" UTXO aan de verzender. Je vraagt de verzender om activa te sturen naar een bestaande UTXO die je bezit, maar je versluiert de werkelijke UTXO identificatie. Dit biedt betere privacy.
- Getuige ontvangen**: Je geeft een standaard Bitcoin adres op. Je vraagt de verzender een *nieuwe* UTXO voor je aan te maken door de activa naar dat adres te sturen. Hierdoor kunnen de RGB activa direct worden gekoppeld aan de nieuwe UTXO die door de transactie wordt aangemaakt.


#### Bliksemdeposito


Voor Lightning-deposito's volstaat generate een factuur. Het RGB activum wordt naar u gerouteerd via uw open kanalen.


![USDT Lightning Invoice](assets/en/10.webp)



## Kanalen openen met RGB Assets


Om RGB activa over de Lightning Network te routeren, heb je een kanaal nodig met voldoende liquiditeit en activatoewijzing. De eenvoudigste manier om te beginnen is **Koop een kanaal** van een LSP (Lightning Service Provider).


### Een kanaal kopen bij Kaleido LSP


1. Ga naar het tabblad **Kanalen**. Je ziet opties voor "Kanaal openen" (handmatig) of "Kanaal kopen" (LSP).

2. Klik op **Koop kanaal**.


![Channels Dashboard](assets/en/11.webp)


3. **Verbind met LSP**: De app maakt verbinding met de standaard Kaleido LSP. Deze provider biedt inkomende liquiditeit en ondersteunt RGB asset routing.


![Connect to LSP](assets/en/12.webp)


4. **Kanaal configureren**:


    - Capaciteit**: Selecteer de totale Bitcoin capaciteit voor het kanaal.
    - RGB toewijzing**: Kies het RGB activum (bijv. USDT) dat u wilt kunnen ontvangen of verzenden. Het LSP zal ervoor zorgen dat het kanaal is geconfigureerd om deze asset te ondersteunen.


![Configure Channel](assets/en/13.webp)



    - RGB Toewijzing**: Kies het RGB activum (bijv. USDT) dat u wilt kunnen ontvangen of verzenden. Het LSP zal ervoor zorgen dat het kanaal is geconfigureerd om dit middel te ondersteunen.


![RGB Allocation](assets/en/14.webp)


5.  **Betaling**: Je moet een vergoeding betalen aan de LSP voor het openen van het kanaal en het verschaffen van liquiditeit. U kunt betalen met **Lightning** of **On-chain** Bitcoin. De betaling kan worden gedaan vanaf uw interne KaleidoSwap wallet of een externe wallet.


![Complete Payment](assets/en/15.webp)


6. Zodra de betaling is bevestigd, zal het LSP de transactie voor het openen van het kanaal starten. Er verschijnt een scherm **Order voltooid**.


![Order Completed](assets/en/16.webp)


7. Na bevestiging op de blockchain is je kanaal actief en klaar voor RGB overdrachten.



## Handel: Model nemer nemer


De handelsmotor van KaleidoSwap werkt op basis van een **Taker-Maker model**. U kunt activa handmatig ruilen met een gelijke of een Market Maker (LSP) gebruiken.


### Ruilen met een Market Maker (LSP)


Dit is de meest gebruikelijke manier van handelen. U treedt op als de **Taker** en voert orders uit tegen de beschikbare liquiditeit die wordt verschaft door de LSP (**Maker**).


1. Navigeer naar het tabblad **Handel** en selecteer **Market Maker**.

2. **Voer Bedrag** in: Voer het bedrag in van Bitcoin dat je wilt verzenden (of het activum dat je wilt ontvangen). De interface toont de geschatte wisselkoers en kosten.


![Market Maker Swap](assets/en/17.webp)


3. **Bevestig ruil**: Bekijk de details, waaronder de wisselkoers en het exacte bedrag dat u zult ontvangen. Klik op **Wissel bevestigen**.


![Confirm Swap](assets/en/18.webp)


4. **Verwerking**: De swap wordt atomair uitgevoerd op de Lightning Network. Er verschijnt een statusscherm dat aangeeft dat de wissel in behandeling is.


![Swap Pending](assets/en/19.webp)


5. **Succes**: Zodra de HTLC's zijn vereffend, is de swap voltooid en bevinden de activa zich in uw kanaal.


![Swap Success](assets/en/20.webp)



## Ontwikkelaar API


Voor ontwikkelaars die bovenop KaleidoSwap bouwen, stelt de applicatie een API beschikbaar die ondersteuning biedt:



- RGB LSPS1**: Voor geautomatiseerde liquiditeitsdiensten.
- Swap API**: Voor programmatische handel en market making.
- WebSocket**: Voor realtime marktgegevensabonnementen.


Raadpleeg de [API Documentatie] (https://docs.kaleidoswap.com/api/introduction) voor volledige eindpunten en specificaties.


## Conclusie


KaleidoSwap stelt u in staat om de privacy en schaalbaarheid van RGB activa op de Lightning Network te benutten. Door de gekleurde UTXO's en de toewijzing van kanaalactiva te begrijpen, kunt u dit krachtige gedecentraliseerde uitwisselingsprotocol volledig benutten.