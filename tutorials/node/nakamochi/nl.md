---
name: Nakamochi
description: Node draaien eenvoudig gemaakt - Hoe de Nakamochi Bitcoin- en Lightning-node te configureren en gebruiken.
---

![image](assets/cover.webp)

Het runnen van je eigen Bitcoin en Lightning Full node hoeft niet langer een complexe taak te zijn die alleen is voorbehouden aan technische experts. Traditioneel vereiste het opzetten en beheren van nodes diepgaande kennis van cryptografie, netwerken en softwareontwikkeling. Nakamochi verandert dat door nodes toegankelijk te maken voor iedereen, ongeacht de technische achtergrond.


Met Nakamochi kan iedereen vanuit huis een node opzetten en beheren, wat volledige privacy en financiële onafhankelijkheid mogelijk maakt. Het runnen van een Full node beveiligt niet alleen je eigen transacties, maar draagt ook bij aan de kracht van het Bitcoin netwerk. Een gedecentraliseerd en veerkrachtig Bitcoin netwerk vertrouwt op een brede distributie van nodes om de veiligheid en onafhankelijkheid te garanderen.


### Inhoudsopgave



- Wat is Nakamochi en hoe werkt het?
- Nakamochi opzetten
- Over de Lightning Network
- Kanalen openen en transacties doen in de Lightning Network



## Wat is Nakamochi en hoe werkt het?


Nakamochi is een Full node die alleen Bitcoin ondersteunt en zowel Bitcoin als Lightning netwerken. Het bevat een geïntegreerde Bitcoin en Lightning Wallet, waardoor gebruikers een veilig, zelf soeverein Bitcoin knooppunt kunnen draaien terwijl ze profiteren van de snelheid en lage transactiekosten van de Lightning Network.


Je Nakamochi node wordt beheerd via een mobiele app, [BitBanana (Android)](https://bitbanana.app) en [Zeus (iOS)](https://bitbanana.app), zodat je hem overal gemakkelijk kunt besturen. Deze apps fungeren als een afstandsbediening voor uw node, zodat u direct kunt betalen met Bitcoin of Lightning, transacties kunt beheren, kanalen kunt openen of sluiten, saldi kunt controleren en de prestaties van uw node kunt controleren.



## Nakamochi instellen duurt slechts 5 minuten


### Stap 1: Aansluiten en beginnen


1. Sluit Nakamochi aan op voeding en Wi-Fi.

2. Klik op **"Nieuw Wallet instellen"** en sla je 24-woord herstelzin veilig op.

3. Gebruik een app voor knooppuntbeheer (Zeus of BitBanana) om verbinding te maken met je Nakamochi:

4. Open de app en scan de QR-code die op je Nakamochi staat.

5. Stel voor extra veiligheid een pincode in op je apparaat.


![image](assets/en/01.webp)

_Sluit aan op stroom en schrijf uw 24-woorden herstelzin op_


![image](assets/en/02.webp)

_Wacht tot de blockchain is bijgewerkt_


![image](assets/en/03.webp)

_Stel een nieuwe wallet in op het Lightning-tabblad_


![image](assets/en/04.webp)

_Scan de QR-code met de Node Management-app_


![image](assets/en/05.webp)

_Stel een pincode in voor extra veiligheid_


**Opmerking:** _Laat uw Nakamochi-node synchroniseren met de blockchain. Dit proces kan enige tijd duren, afhankelijk van uw internetverbinding._



## Over de Lightning Network


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

De Bitcoin Lightning Network revolutioneert Bitcoin transacties door ze sneller, goedkoper en efficiënter te maken. Hij is perfect voor dagelijks gebruik en maakt bijna onmiddellijke betalingen met minimale kosten mogelijk, ideaal voor microtransacties zoals het kopen van een kopje koffie of het afhandelen van frequente kleine aankopen.

Door off-chain te gebruiken, is Lightning ontworpen om te schalen en duizenden transacties per seconde te ondersteunen zonder de hoofd Blockchain van Bitcoin te overbelasten. Dit maakt het een belangrijke speler in de evolutie van Bitcoin naar een praktisch, wereldwijd betalingssysteem.

Privacy is een ander voordeel, want transacties op Lightning worden via privé betaalkanalen geleid in plaats van direct op de Blockchain geregistreerd te worden. Dit zorgt voor een meer discrete manier om transacties uit te voeren, terwijl de robuuste beveiliging van de Bitcoin behouden blijft.



#### Betalingskanalen uitgelegd


De Lightning Network werkt via betaalkanalen, dit zijn verbindingen tussen twee partijen die meerdere transacties mogelijk maken zonder direct contact met de Blockchain. Wanneer een kanaal open is, wordt het saldo tussen de twee partijen bijgewerkt op deze tweede Layer Lightning-oplossing voor elke transactie. Wanneer een kanaal open is, wordt het saldo tussen de twee partijen bijgewerkt op deze tweede Layer Lightning-oplossing voor elke transactie, wat zorgt voor snelle, goedkope betalingen. Alleen het openen en sluiten van het kanaal wordt geregistreerd On-Chain, waardoor er minder congestie is op Bitcoin Blockchain. Dit ontwerp zorgt voor schaalbaarheid en privacy, omdat individuele transacties niet geregistreerd worden op het openbare Ledger.


**Voorbeeld:** Alice en Bob openen een kanaal door Bitcoin eraan toe te wijzen. Alice stuurt Bitcoins naar Bob, en hun off-chain balansen worden onmiddellijk bijgewerkt zonder een On-Chain record. Als Alice dan Charlie betaalt, en Alice heeft geen direct kanaal naar Charlie, kan de betaling worden omgeleid via het kanaal van Bob om Charlie te bereiken. Routing via tussenliggende knooppunten zorgt voor betalingen, zelfs zonder directe verbindingen, wat het netwerk zeer efficiënt maakt.



## Kanalen openen en transacties doen in de Lightning Network


Zodra je Nakamochi is ingesteld en verbonden met een node management app, kun je beginnen met het gebruik van de Lightning Network door kanalen te openen en transacties te doen.


### Kanalen openen op Zeus (iOS):


1. Ga naar het tabblad **"Kanalen"** (onderste menu).

2. Klik op de **"+"** om een nieuw kanaal te openen.

3. Scan of voer de pubkey in van het knooppunt waarmee je verbinding wilt maken.

4. Voer het vergrendelde bedrag in (kies met je peer of gebruik het minimale vaste bedrag voor bekende nodes).

5. Klik op **"Kanaal openen"**.


![image](assets/en/06.webp)

_ZEUS Schermafbeelding_


Voor meer informatie: [Kanalen | Zeus Documentatie](https://docs.zeusln.app/)


### Kanalen openen op BitBanana (Android):


1. Open het hamburgermenu (links).

2. Ga naar **"Kanalen"**.

3. Klik op de **"+"** om een nieuw kanaal toe te voegen/te openen.

4. Scan of plak de pubkey.

5. Voer het vergrendelde bedrag in (kies met je peer of gebruik het minimale vaste bedrag voor bekende nodes).


![image](assets/en/07.webp)

_Bitbanana Screenshot_


Voor meer informatie: [BitBanana](https://bitbanana.com)


Zodra je kanaal open is, kunnen er betalingen doorheen worden gerouteerd naar andere deelnemers in het netwerk. Saldi worden off-chain aangepast, waardoor transacties vrijwel direct plaatsvinden en minimale kosten met zich meebrengen.

Als je een chatroom niet meer nodig hebt, kun je deze sluiten. Deze actie vereffent het eindsaldo tussen jou en je leeftijdsgenoot en registreert het On-Chain. Idealiter zijn beide partijen het eens en online voor een "coöperatieve sluiting" (sneller en minder kosten in tegenstelling tot een "gedwongen sluiting" met een niet reagerende/offline peer).

In het algemeen raden we aan om kanalen open te laten om kosten te besparen en de betrouwbaarheid en efficiëntie van het netwerk te verhogen. Door kanalen open te houden, minimaliseer je On-Chain transactiekosten, voorkom je downtime voor kanaalherverbindingen en behoud je een stabiele routeringscapaciteit voor naadloze betalingsverwerking. Deze aanpak bevordert een robuust en veerkrachtig netwerk, terwijl de algehele gebruikerservaring verbetert en de operationele overhead vermindert.



### Handige koppelingen



- [Over Nakamochi](https://nakamochi.io/)
- [Abonneer je op de nieuwsbrief van Nakamochi](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)