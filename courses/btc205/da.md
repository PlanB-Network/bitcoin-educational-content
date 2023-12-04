---
name: Peer-to-Peer Bitcoin Købs- og Salgsløsning
goal: Udforsk ikke-KYC-løsninger til køb og salg af Bitcoin
objectives:
  - Forstå de forskellige typer KYC, deres risici og fordele
  - Forstå fordelene ved peer-to-peer-køb
  - Implementer den løsning, der passer til dine behov
  - Forbedr styringen af dine UTXO'er (KYC og ikke-KYC)
---

# En rejse ind i verdenen af ikke-KYC

Pierre tilbyder os denne kursus, der dykker ned i de forskellige eksisterende løsninger til køb og salg af bitcoins peer-to-peer. Peer-to-peer-køb er helt lovligt og tillader mere anonymitet, da disse løsninger ikke er KYC. KYC (Know Your Customer) er en regel fra markedets reguleringsmyndigheder (AMF), der kræver identifikation fra kunden, der ønsker at købe eller sælge bitcoin. Disse regler sigter mod at forhindre hvidvaskning af penge, finansiering af terrorisme og skatteunddragelse. På trods af risikoen for betydelige konsekvenser for brugeren har KYC til formål at forsvare og beskytte brugeren, selvom det modsatte ofte observeres.

Vi vil derfor udforske de forskellige typer KYC (fuld KYC-type Frankrig, KYC Light-type Schweiz og ikke-KYC-type peer-to-peer). Pierre vil præsentere mere end 6 løsninger, så du vil have alle kortene på hånden for at opdage, hvilken der passer til dig. Hvis du ønsker en KYC-løsning, skal du vide, at de er til stede i BTC 102-kurset.

+++

# Introduktion

![introduktion af Rogzy](https://youtu.be/3AHeKLTK7Sg)

## Forklaring og type af KYC

![forklaring af KYC-typer](https://youtu.be/kDhXoPU1KtM)

KYC, eller "Know Your Customer", er en reguleringsstandard, der kræver indsamling af private kundeoplysninger, såsom deres fysiske adresse, identifikation eller bankoplysninger. Denne praksis er almindelig på mæglerplatforme, der kan kræve en komplet KYC, herunder detaljerede oplysninger som identifikation, et foto, bevis for adresse, lønsedler osv.
Hovedformålet med KYC er at bekæmpe hvidvaskning af penge, finansiering af terrorisme og skatteunddragelse. Det er en lov, der er indført af AMF (Autorité des marchés financiers), den franske markedsregulerende myndighed. Imidlertid fører anvendelsen af KYC til centralisering af meget følsomme databaser, der indeholder personlige brugeroplysninger. Disse oplysninger, der har en vis værdi, kan sælges til ondsindede enheder.
Derudover kræver udvekslingsplatforme ofte en overdreven mængde personlige oplysninger, hvilket sætter brugerne i fare og øger overholdelsesomkostningerne. Disse reguleringsomkostninger kan afskrække franske virksomheder og skade deres konkurrenceevne på internationalt plan.

Der er tre typer KYC, herunder fuld KYC, der kræver en komplet og reguleret indsamling af oplysninger for at få adgang til tjenesten. I Schweiz tillader et alternativ kaldet "KYC light" køb og salg af bitcoins uden at give identifikation, så længe købsbeløbet ikke overstiger 1000 euro pr. dag. Løsninger som Relay tillader brugen af denne metode.

I denne sammenhæng kan schweiziske myndigheder få adgang til bankoplysninger for at undersøge personer, der anses for at være i risiko. Bitcoin-leveringsadresser er også sporbar gennem banksystemet. KYC light betragtes generelt som enklere og mindre omkostningsfuld end det franske system.

I Frankrig kræver køb af bitcoins online, at der sendes penge til en tredjepart via SEPA-overførsel eller Paypal. For dem, der prioriterer anonymitet, sikkerhed og privatliv, er der også muligheder for kontantkøb af bitcoins. For små mængder er køb af bitcoins kontant en simpel og lovlig mulighed.
For at kunne sælge 100 euro PLT af bitcoin dagligt til hvem som helst, er regulering af AMF (Financial Markets Authority) nødvendig. I Frankrig gælder denne regulering primært for enkeltpersoner, der udfører betydelige transaktionsvolumener. De to andre metoder til at købe bitcoin inkluderer brugen af ​​automatiske pengeautomater (ATM'er) og udvekslinger mellem venner. ATM'er er reguleret og kræver identifikation for transaktioner over 500 euro. Udveksling mellem venner tilbyder derimod en mere diskret eksponering for bitcoin.

Disse reguleringsforanstaltninger er på plads for at bekæmpe finansiering af terrorisme, skatteunddragelse og hvidvaskning af penge. Bitcoin, som en fuldt sporbar database, gør hvidvaskning af penge særlig vanskelig. Brugen af ​​Bitcoin af kriminelle kan spores, hvilket gør Bitcoin til et ineffektivt redskab til hvidvaskning af penge.

Det er vigtigt at bemærke, at denne træning præsenterer forskellige alternativer samt værktøjer, der kan bruges til ondsindede eller ikke-ondsinde formål. Derudover giver den forklaringer på, hvordan ordrebøger fungerer mellem makers (ordreudbydere) og takers (ordremodtagere).

Det er også vigtigt at bemærke, at de præsenterede oplysninger her ikke anbefaler nogen bestemt løsning. Den præsenterer blot de tilgængelige muligheder for en bedre forståelse af emnet. Hvis du har yderligere spørgsmål om Bitcoin, skal du ikke tøve med at konsultere online ressourcer som www.découvrebitcoin.com.

## Sammenligning af peer-to-peer købs- og salgsløsninger

![Sammenligning af peer-to-peer købs- og salgsløsninger](https://youtu.be/HiwSjN04Mz0)

P2P-løsninger til køb af Bitcoin: Bisq, RoboSat, LNP2PBot, Peach og HodlHodl

At købe Bitcoin peer-to-peer (P2P) er en foretrukken mulighed for investorer, der ønsker at undgå centraliserede udvekslingsplatforme. Denne del af kurset undersøger forskellige P2P-løsninger, herunder Bisq, RoboSat, LNP2PBot, Peach og HodlHodl.

Sammenligning af fordele og ulemper ved forskellige løsninger

Hver P2P-løsning har sine egne fordele og ulemper. Vi giver et overblik over de vigtigste funktioner i hver løsning nedenfor.

### Bisq

[Bisq](https://bisq.network/) er en ikke-kustodial P2P-løsning, der har et DAO (Decentralized Autonomous Organization) system og bruger multisign til tvistehåndtering. Dens kode er åben kilde, hvilket bidrager til dens robusthed og beskyttelse af brugerens privatliv.

| Fordele                                       | Ulemper                                                                                                 |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| - P2P-løsning, ikke-kustodial, multisign, DAO | - Applikationen er ret tung og ikke særlig brugervenlig, kun tilgængelig på computer                      |
| - Robust og sikker                            | - Købs- og salgsbegrænsninger samt kontohåndtering med signaturer er tveæggede sværd.                     |
| - Åben kilde                                  |                                                                                                         |

### RoboSat

[RoboSat](https://learn.robosats.com/) er en nem at bruge, hurtig løsning, der fungerer under TOR og kræver ikke en konto. Den er åben kilde og bruger Lightning Network til at muliggøre hurtige transaktioner.

| Fordele                                               | Ulemper                                                                 |
| ----------------------------------------------------- | ----------------------------------------------------------------------- |
| - Nem at bruge                                        | - Protokollen er skrøbelig med en enkelt koordinator                     |
| - Lave transaktionsgebyrer                            | - Kræver teknisk viden og forståelse for privatliv                       |
| - Bruger Lightning Network til hurtige transaktioner | - Umbrell-applikationen giver mulighed for at administrere ens egen klientinstans |
| - Åben kilde                                          |                                                                         |

### LNP2PBot
[LNP2PBot](https://lnp2pbot.com/) er tilgængelig via Telegram til ikke-KYC Bitcoin-køb. Den tilbyder hurtige transaktioner gennem Lightning Network og lave gebyrer.
| Fordele                                            | Ulemper                                                                                      |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| - Tilgængelig via Telegram                         | - Mindre robust og sikker end andre løsninger                                               |
| - Hurtige transaktioner gennem Lightning Network    | - Mindre hurtig og mindre brugervenlig end Robosat                                          |
| - Lave transaktionsgebyrer                         | - Kan være forbundet med brugerens Telegram-identitet                                       |
| - Intern konflikthåndtering                        | - Mangel på likviditet og skrøbelighed i applikationen                                       |
| - Fælles forslag til at begrænse tillidsproblemet   | - LNP2Pbot skal betroes at håndtere konflikter                                              |

### Peach

[Peach](https://peachbitcoin.com/) er en mobilapplikation dedikeret til Bitcoin-handel. Den skiller sig ud ved sin enkelhed og kræver ikke oprettelse af en konto for at fungere. Handler er hurtige, selv uden brug af Lightning Network. Derudover fremskynder meddelelser på telefoner transaktionsprocessen.

| Fordele                                              | Ulemper                                                                                      |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| - Forenklet brug: ingen kontooprettelse er nødvendig | - Sikkerhed og robusthed: da Peach er knyttet til et firma, har det potentielle svagheder i sikkerhed. |
| - Hurtighed i transaktioner                          | - Manglende Lightning Network: denne teknologi, der tillader hurtigere Bitcoin-transaktioner, bruges ikke af Peach. |
| - Meddelelser: de fremskynder transaktionsprocessen  |                                                                                              |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) er en ikke-kustodial løsning til Bitcoin-udveksling. Den tilbyder mange fordele såsom stærk likviditet, muligheden for private handler, et henvisningssystem samt konti med handelshistorik og et vurderingssystem. Dog er handler forbundet med brugerens e-mailadresse og digitale identitet, som opbevares hos HodlHodl. Derudover er HodlHodls kildekode ikke offentligt tilgængelig, og applikationen kan ikke bruges med Tor.

| Fordele                                                                                               | Ulemper                                                                                                                |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| - Ikke-kustodial: brugeren beholder besiddelsen af deres private nøgler.                               | - Opbevaring af personlige oplysninger: brugerens e-mailadresse og digitale identitet opbevares af HodlHodl.           |
| - Likviditet: HodlHodl tilbyder et bredt udvalg af udvekslingsmuligheder.                               | - Lukket kildekode: HodlHodls kode er ikke offentligt tilgængelig.                                                       |
| - Mulighed for private handler: brugeren kan vælge, hvem de vil handle med.                            | - Inkompatibilitet med Tor: HodlHodl kan ikke bruges med dette privatlivsfokuserede netværk.                           |
| - Henvisningssystem: HodlHodl belønner mund-til-mund.                                                    | - Mulighed for tvungen KYC: i visse situationer kan HodlHodl kræve identifikationsoplysninger for at hente midler.     |
| - Handelshistorik og vurderingssystem: disse funktioner gør det muligt at evaluere pålideligheden af andre brugere. |                                                                                                                        |

## Konklusion om P2P-løsninger
I oversigt har hver P2P-løsning sine fordele og ulemper. Bisq anses for at være den mest robuste og sikre, men mindre brugervenlig. RoboSat er open source, men mindre robust end Bisq. LNP2PBot er mindre robust og sikker end andre løsninger, mindre hurtig og mindre brugervenlig end RoboSat, men mere end Bisq. Peach er den nemmeste og hurtigste applikation til at købe Bitcoin uden KYC, men der er et firma bag, så der er svagheder med hensyn til sikkerhed og robusthed. HodlHodl er et protokol styret af et firma og lukket kildekode, så der er svagheder med hensyn til sikkerhed og robusthed, og det er lidt mere kompliceret end Peach.
God gammeldags kontant ansigt til ansigt er stadig en løsning til små beløb.

Udover P2P-løsninger er der andre muligheder for kryptobørs. kycnot.me tilbyder tjenester som VPN, VPS, SMS osv. Bitrefil giver dig mulighed for at købe gavekort. Hver løsning på [kycnotme](https://kycnot.me/) præsenteres med sine positive og negative punkter.

# Tutorials om P2P købs-/salgsløsninger

## Robosats

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) er et open source-projekt udviklet af Reckless Satoshi til privat udveksling af Bitcoins til nationale valutaer. Det forenkler peer-to-peer-oplevelsen og bruger Lightning-fakturaer til at minimere behovet for opbevaring og tillid. For at bruge det, skal vi bruge Tor, et anonymt kommunikationsnetværk.

Det første, du skal gøre, er at downloade Tor. Du kan finde det på GitHub eller direkte på den officielle hjemmeside på følgende adresse: tor.org/download.
Når Tor er downloadet og installeret:

- Tryk på "Connect" for at etablere forbindelsen.
- Gå til [robosats onion-adressen](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Kopier tokenet for at gemme din identitet.

Her er trinnene til at købe bitcoins med Robosats:

- Tjek ordrebogen, du kan filtrere efter valuta og betalingsmetode - for eksempel, køb bitcoin i euro med Revolut.
- Inden du køber, skal du tjekke tilbuddets udløb, prisen i euro og præmien (du kan også filtrere tilbud efter præmie).
- Vælg helst et tilbud med en aktiv bruger og med en præmie lavere end gennemsnittet.
- Tjek ordresammendraget med beløbet, betalingsmetoden, præmien, ordre-ID'et og udløbsdatoen.
- Du kan modtage dine satoshis på en Bitcoin-adresse med en swap-out-gebyr (fra LN til BTC-onchain) på ca. 1% (du kan ændre on-chain mining-gebyrer).
- Ellers opret en faktura med en LN-tegnebog fra denne [liste](https://learn.robosats.com/docs/wallets/) og kopier fakturaen til Robosats.
- Kontakt sælgeren via krypteret chat for at diskutere fiat-betaling.

Nu lad os se trinnene til at sælge bitcoins på Robosats:

- Tilpas dit tilbud ved at vælge betalingsmetode, præmie, udløbstid osv.
- Fidelity Bond Size svarer til et sikkerhedsdepositum på BISC. Sæt 15% eller 10% af sikkerhedsdeposita for at opfordre den anden part til at være fair.
- Lås satoshis for at bekræfte oprettelsen af ordren og undgå spam.
Hvis nogen accepterer dit salgstilbud, skal du diskutere med modparten for at fortsætte med fiat-betaling. Når betalingen er foretaget, er handlen fuldført, og satoshierne er solgt!
## BISQ: peer-to-peer købsløsning

[Bisq](https://bisq.network/) er en decentraliseret udvekslingsplatform for digitale aktiver, primært Bitcoin. Den tillader direkte, sikre og private transaktioner mellem brugere over hele verden uden behov for en mellemmand.

🚨 Vær venlig at udvise forsigtighed, når du bruger Bisq, da det er en avanceret løsning. Det er måske ikke egnet til begyndere. Sørg for at have noget erfaring og forståelse, inden du begynder. 🚨

Vi ser nærmere på denne løsning, her er tutorial videoer:

![del 1](https://tube.nuagelibre.fr/videos/watch/b3885ea9-23e9-4b58-aa3f-401348da85a1)

![del 2](https://tube.nuagelibre.fr/videos/watch/53276305-70d6-4c7f-9df9-e100a82eee16)

For de mere ressourcestærke, her er en kortfattet guide, der beskriver de væsentlige trin:

1. Download og installer: Besøg Bisq's hjemmeside og download applikationen. Installer den på dit system.
2. Konfigurer betalingsmetode: Åbn applikationen og gå til "Konto". Tilføj detaljerne for din betalingsmetode.
3. Finansier din Bisq Wallet: Klik på "Midler" og "Modtag midler" for at få din Bisq-adresse. Send Bitcoins til denne adresse.
4. Foretag en transaktion: Klik på "Køb/Salg" og vælg den ønskede transaktion. Følg instruktionerne for at fuldføre transaktionen.

## 5. Bekræft modtagelse:

Når du har modtaget betalingen, bekræft det i Bisq-applikationen. Dette frigiver Bitcoin fra escrow. Husk altid at kontrollere alle transaktionsdetaljer og kun handle med betroede parter.

Her er en komplet guide, der vil guide dig gennem alle trinene til brug af Bisq.

Bisq er et decentraliseret og sikkert netværk, der respekterer din private ejendom. Det er ikke-kustodialt, hvilket betyder, at du altid ejer dine midler. Derudover bruger Bisq en token, BSQ, der giver dig mulighed for at betale lavere transaktionsgebyrer og opfordrer til din deltagelse i Decentralized Autonomous Organization (DAO). For at beskytte sælgere under Bitcoin-fiat-transaktioner har Bisq implementeret et system med signaturer og kontolimitter. Som køber skal du opnå en underskrevet konto for at øge dit købsloft. Signaturen er også en måde at verificere handlendes historie på og sikre transaktionssikkerhed.

For at installere Bisq og sikkerhedskopiere dine data, skal du følge disse enkle trin:

- Gå til bisc.network hjemmesiden for at downloade softwaren (Skærmbillede af download-siden)
- Verificer integriteten af softwaren ved hjælp af værktøjer som dem, der leveres af Loïc Morel til Windows-brugere.
- Når installatøren er verificeret, start Bisq, giv nødvendige tilladelser og accepter brugsbetingelserne. (Skærmbillede af brugsbetingelserne)
- Bisq vil oprette forbindelse til Bitcoin-netværket og sig selv via Tor, hvilket kan tage lidt tid.
- Konfigurer din betalingskonto og sikkerhedskopier din Secure Identifier (SID) wallet for at forhindre tab eller tyveri. (Skærmbillede af kontokonfigurationssiden)
- Opret også en adgangskode til at kryptere dine oplysninger.

Afhængigt af dit operativsystem vil Bisq-data blive gemt på forskellige placeringer. Du kan finde dem i mappen "Data Directory". Vær forsigtig, hvis du sletter denne mappe, vil alle dine Bisq-data gå tabt.
For at gendanne dine data ved hjælp af en sikkerhedskopi:

- Kopier sikkerhedskopimappen til placeringen 'bruger/applikation support/BISQ'.
- Rename mappen til sikkerhedskopiering til 'BISQ'.
- Genstart Bisq, og alle dine data bør blive gendannet.

Inden du køber eller sælger Bitcoin på Bisq, er det afgørende at oprette din betalingskonto. For eksempel kan du oprette en konto i din nationale valuta, såsom en SEPA-konto, en REVOLUT-konto eller en PAYPAL-konto.
For at oprette din REVOLUT-konto:

- Tilføj en konto og vælg REVOLUT fra listen over muligheder. (Skærmbillede af listen over kontomuligheder)
- Du kan vælge forskellige valutaer: euro, britiske pund, amerikanske dollar eller schweiziske franc.
- Den maksimale transaktionsvarighed er en dag, og købsgrænsen er 0,25 Bitcoin.
- Brug dit personlige REVOLUT-kontonavn for at undgå forvirring.
- Sørg for at signere dine konti og etablere købsgrænser for øget sikkerhed.

For at købe Bitcoin på BISQ:

- Gå til "Køb" -afsnittet, hvor du kan vælge forskellige markeder. (Skærmbillede af "Køb" -afsnittet)
- For at drage fordel af reducerede gebyrer anbefaler vi at købe BSQ, som du kan købe med Bitcoin.
- Du kan vælge mellem forskellige tilbud baseret på pris, mængde, betalingsmetode osv.
- For at købe BSQ skal du først indbetale Bitcoin på din tegnebog.
- Vælg et tilbud med en lav præmie og lav mængde til køb af BSQ.
- BISQ verificerer tilbuddets gyldighed og forbindelsen til peeren.
- Hvis sælgeren ikke er forbundet, skal du vælge en anden.
- Kontroller tilbuddet og accepter en præmie på 5%.
- Bekræft gebyrerne og BSQ-udvekslingen og vent derefter på transaktionsbekræftelse for at købe Bitcoins med BSQ.

For at sælge Bitcoin på BISQ:

- Opret et nyt tilbud i fanen "Sælg". (Skærmbillede af fanen "Sælg")
- Du kan vælge at angive antallet af Bitcoins, der skal sælges, eller det beløb i euro, du ønsker at modtage.
- Du kan angive en præmie som en procentdel over markedsprisen.
- Du kan oprette et salgsinterval eller overlade valget til køberen.
- Du kan også angive en pris for at stoppe tilbuddet.
- Vælg det mindste indbetalingsbeløb og transaktionsgebyrer.
- Finansier ordren ved at indbetale de Bitcoins, der skal sælges, indbetalingsbeløbet og gebyrerne.
- Når du har oprettet tilbuddet, skal du vente på, at en køber vises.

Når køberen har indbetalt transaktionen på BISQ, sendes Bitcoins automatisk til køberen, og du modtager pengene. Kontoen verificeres og signeres efter en transaktion med en signeret konto.

## LNP2PBOT

![LNp2pbot tutorial](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) er en beskedplatform, der med hjælp fra [Lnp2pbot](https://lnp2pbot.com/) -botten giver dig mulighed for at købe og sælge bitcoins hurtigt og nemt. Sådan gør du:

For at købe Bitcoins via LNP2PBOT-botten på Telegram, skal du følge disse trin:

- Start med at gå til Twitter-kontoen for Lnp2pbot-botten og klik på linket i bioen. (Skærmbillede af Lnp2pbot Twitter-kontoen og linket i bioen)
- I Telegram skal du bruge kommandoerne "/buy" eller "/sell" for at oprette købs- eller salgsordrer. (Skærmbillede af brugen af ​​kommandoerne "/buy" eller "/sell")
- Få adgang til P2P Lightning-kanalen for at finde købs- og salgstilbud i henhold til dine kriterier. (Skærmbillede af P2P Lightning-kanalen)
- Opret et købstilbud ved hjælp af Lnp2pbot-botten og kommandoen "/buy".
- Vælg den valuta, du ønsker, angiv beløbet, prisen (med en præmie, hvis ønsket) og vælg din betalingsmetode.
- Vent, indtil en potentiel sælger kontakter dig.

Hvis du vil sælge Bitcoins via Revolut, skal du gøre følgende:

- Klik på 'sell Satoshi' for at åbne en meddelelse på LNP2PBot. (Skærmbillede af muligheden 'sell Satoshi')
- Modtag en Lightning-faktura for at betale for at sælge Satoshis. (Skærmbillede af Lightning-fakturaen)
- Vent på, at køberen sender en faktura med satoshis for at modtage betalingerne.
- Etablér direkte kontakt med køberen via Telegram for at aftale betalingsmetoden og udveksle nødvendig information.
- Valider transaktionen med en note.

Hvis du vil købe Bitcoins ved at sende en LN-faktura, skal du følge disse trin:

- Kopier fakturaen og send den til botten for at købe Satoshi.
- Kontakt sælgeren for at afslutte købet af bitcoins.
- I tilfælde af et problem, foreslå at vente eller prøve at annullere.
- Annuller tilbuddet og søg efter et nyt, hvis det er nødvendigt.
- Vælg et tilbud, der accepterer øjeblikkelig CPA for at købe Satoshi.
- Send fakturaen og vent på sælgerens betalingsbekræftelse.
- Når betalingen er foretaget, send bekræftelsen til botten.
- Vent på validering af modtagelse af euro og afsendelse af satoshis fra sælgeren.

Ved at bruge disse metoder kan du købe og sælge bitcoins på Telegram sikkert.

## Peach Bitcoin

site: https://peachbitcoin.com/

Vi ser nærmere på denne løsning i BTC 205, der tilbydes af @pivi\_. Her er tutorialvideoerne:

![peach](https://youtu.be/ziwhv9KqVkM)

[Peach](https://peachbitcoin.com/) er en schweizisk mobilapplikation, der giver dig mulighed for at købe og sælge bitcoins peer-to-peer. Denne brugervenlige løsning tilbyder en intuitiv grænseflade, der er ideel til kryptotransaktioner.

Peach-applikationens grænseflade består af fire faner: køb, sælg, historik og indstillinger. (Skærmbillede af applikationens grænseflade)
At købe bitcoins på Peach er forenklet. For at komme i gang skal du oprette et tilbud. Dette er muligt ved at få adgang til fanen "køb". (Skærmbillede af fanen "køb") Derefter kan du gennemse de tilgængelige tilbud ved at swipe, indtil du finder et, der passer til dig. De accepterede betalingsmetoder er forskellige, herunder bankoverførsel, online tegnebog, gavekort og lokal mulighed. (Skærmbillede af tilgængelige betalingsmetoder)

Når du har valgt et tilbud, kan du chatte med sælgeren via applikationens integrerede chat. (Skærmbillede af applikationens chat) Efter betaling, bekræftet af sælgeren, er transaktionen fuldført. Bitcoins sendes derefter til køberen, der modtager en meddelelse, der bekræfter modtagelsen af midlerne. (Skærmbillede af meddelelsen om bitcoin-modtagelse)

Peach er en ikke-kustodial applikation, hvilket betyder, at bitcoins forbliver i din besiddelse i hele processen. Eventuelle potentielle tvister håndteres dog centralt. Det er derfor vigtigt at sikkerhedskopiere transaktionsoplysninger og personlige oplysninger ved hjælp af Backup-funktionen. (Skærmbillede af Backup-funktionen)

Da Peach stadig er i betaversion, kan der opstå nogle fejl. Det anbefales at kontrollere alle oplysninger, inden en transaktion afsluttes.

Samlet set tilbyder Peach-mobilapplikationen en tilgængelig løsning til køb og salg af bitcoins peer-to-peer. Sikker og optimal brug af Peach er nøglen til vellykkede transaktioner.

## Hold Hodl
[HodlHodl](https://hodlhodl.com/) er en decentraliseret Bitcoin-markedsplads, der prioriterer brugerens kontrol og sikkerhed. I modsætning til traditionelle børser fungerer den på en peer-to-peer-model, der tillader direkte udveksling mellem brugere. Med sit multisignatur-escrowsystem garanterer Hodl Hodl sikkerheden af midler under transaktioner. Platformen understøtter også forskellige betalingsmetoder og tilbyder handelsmuligheder som kontrakter for forskel (CFD).
![hodlhodl tutorial](https://youtu.be/BDH9jE7kpD8)

I denne vejledning forklarer vi, hvordan man køber og sælger bitcoins peer-to-peer på HodlHodl-platformen.

Før du begynder at bruge HodlHodl-platformen, er der nogle forberedende trin, der er nødvendige:

- Åbn HodlHodl-webstedet.
- Opret en konto ved hjælp af en e-mail-adresse for at holde styr på dine transaktioner.
- Læs sikkerhedsvejledningen omhyggeligt, inden du begynder at handle.
- Bemærk, at platformen ikke er open source og beholder nogle af dine personlige oplysninger.

Her er processen, der skal følges for at foretage et køb på HodlHodl-platformen:

- Brug filterfunktionen til at finde tilbud, der passer til dig.
- Klik på det tilbud, der interesserer dig.
- Udfyld de nødvendige felter for at acceptere kontrakten.
- I vores eksempel brugte vi Revolut som betalingsmetode.

Opsætning af multisig-kontrakten for transaktionen udføres som følger på HodlHodl:

- Når tilbuddet er accepteret, foretag betalingen via den valgte metode (i vores tilfælde Revolut).
- Opret en multisig-kontrakt ved at generere en adgangskode.
- Vent på, at bitcoins bliver deponeret på multisig-adressen.
- Vælg antallet af bekræftelser for kontrakten.
- Foretag den aftalte betaling til sælgeren og bekræft det på HodlHodl.
- Hav tålmodighed, da depositumets varighed kan være lang, afhængigt af den anvendte bank.
- Vent på sælgerens bekræftelse, før du frigiver bitcoins efter købet.

Oprettelse af et tilbud om at købe eller sælge bitcoins på HodlHodl udføres som følger:

- På HodlHodl-webstedet angiv frigivelsesadressen for købstilbud.
- Indtast beløbet, prisen og betalingsmetoden.
- Du kan også tilføje valgfrie funktioner som transaktionsgrænser eller en titel til tilbuddet.
- Når tilbuddet er oprettet, kan du se, redigere, duplikere eller slette det, som du ønsker.

## Bonus: Side Shift.AI

![SideShift AI](https://youtu.be/xG8Wc1Ti5b8)

Her er en kort vejledning til brug af [SideShift AI](https://sideshift.ai/), et meget nyttigt værktøj til at konvertere shitcoins til bitcoin. Det er det ideelle værktøj for dem, der har lukket alle deres personlige børser. Der kræves ikke et ordresystem, og der er likviditet tilgængelig. Bemærk dog, at der er et transaktionsgebyr på 2,5%.

Hvis du har købt kryptovalutaer på en KYC-måde, anbefales det at bruge Monero til at konvertere disse kryptovalutaer til bitcoin. Monero tilbyder større privatliv end Bitcoin. For øget sikkerhed anbefales også CoinJoin-operationen. CoinJoin blander dine transaktioner med dem fra andre brugere for at komplicere sporingen af dine transaktioner.

Jeg vil også gerne introducere dig for et open-source-værktøj til køb og salg af bitcoins. Dette værktøj giver dig mulighed for at vælge mellem mange blockchain-netværk. Indtast blot din Bitcoin-adresse og vælg det beløb, du ønsker at sende. Der er ikke behov for at oprette en konto eller tilslutte din tegnebog til værktøjet. Du kan bruge en fast kurs til at sende eller modtage et bestemt beløb. Derudover tillader dette værktøj også salg af bitcoins i bytte for USDC.

### Støt os
Dette kursus, samt alt indholdet tilgængeligt på dette universitet, er blevet tilbudt til dig gratis af vores fællesskab. For at støtte os kan du dele det med andre, blive medlem af universitetet og endda bidrage til dets udvikling via GitHub. På hele holdets vegne, tak!

### Kursusvurdering

Et vurderingssystem for kurset vil snart blive integreret i denne nye e-læringsplatform! I mellemtiden takker vi dig meget for at have taget kurset, og hvis du nød det, bedes du overveje at dele det med andre.

# Gå videre

## Interview med Steph fra Peach Bitcoin

![interview med Steph](https://youtu.be/LRGKD8qNSXw)

Her er en sammenfatning af interviewet:

Peach Bitcoin er en ikke-kustodial mobilapplikation, der muliggør peer-to-peer køb og salg af Bitcoin. I øjeblikket består Peach Bitcoin-teamet, der er baseret i Schweiz, af otte medlemmer og arbejder på at udvikle applikationen til også at fungere som en tegnebog. Peach Bitcoins unikke model er baseret på en centraliseret virksomhedsstruktur, samtidig med at den opretholder en decentral ordrebog. Derudover tilbyder applikationen en mulighed for kontanttransaktioner under personlige møder.

En af de vigtigste fordele ved Peach Bitcoin er det sikkerhedsniveau, den tilbyder brugerne. Deskrow-systemet med multisignatur og tidslås er designet til at håndtere tvister og sikre transaktionssikkerhed. Derudover har Peach Bitcoin prioriteret adgang til multisignaturpengene, hvilket giver mulighed for at overføre bitcoins til køberen i tilfælde af ondsindet adfærd fra sælgeren. Virksomheden planlægger at integrere alle europæiske valutaer samt andre betalingsmetoder, når den lanceres i åben beta i januar.

Idéen til Peach Bitcoin kom fra grundlæggerens personlige erfaring i Bitcoin-industrien. Efter at have opdaget Bitcoin i 2017 og deltage i flere møder og konferencer blev hun en Bitcoin-maksimalist og så muligheden for at skabe en platform, hvor Bitcoin-brugere kunne mødes og handle med kontanter. Derudover inkluderer applikationen en krypteret chat til kommunikation med andre brugere og bevare brugerens anonymitet.

I øjeblikket udvikler Peach Bitcoin flere funktioner for at gøre det nemmere for sælgere, herunder oprettelse af en API til sælgere, en platform til store sælgere og integration af BTC Pay Server til at automatisere overførsler. Applikationen vil blive lanceret i åben beta i januar 2023.

Afslutningsvis understreger grundlæggeren af Peach Bitcoin vigtigheden af konkurrence i Bitcoin-økosystemet, da det, der er godt for Bitcoin, er gavnligt for alle. Hun opfordrer også til mangfoldighed og inklusion i Bitcoin-industrien og ud over det.

## Interview med Pierre

![interview med Pierre](https://youtu.be/COoezuJncm8)
Her er en sammenfatning af interviewet:

Dette interview afslutter Bitcoin 205-uddannelsen, som omhandler emnet peer-to-peer Bitcoin-købsløsninger. Organiseret af Pierre, har denne uddannelse til formål at oplyse det fransktalende publikum om de tekniske løsninger til peer-to-peer Bitcoin-køb, et område der hidtil har været forsømt. Takket være de fremskridt, der er gjort, er det nu muligt at købe og bruge Bitcoin og samtidig bevare sin privatlivets fred, selv med en simpel telefon og Telegram-applikationen.

En af de fremhævede metoder er brugen af CoinJoin med Samouraï til at forbedre sikkerheden. Denne løsning minimerer risikoen ved, at centraliserede enheder har personlige oplysninger om Bitcoin-brugere. Det anbefales at købe Bitcoins på en ikke-kyc-måde, en metode der forbedrer anonymiteten. Derudover tilbyder nogle handelsplatforme som Kraken lavere udbetalingsgebyrer end andre, hvilket er i overensstemmelse med Bitcoin-principperne.
Bisq, Robosat og Peach præsenteres som demokratiske løsninger for Bitcoin-handel. Peach fremhæves især for sin nemme adgang som en mobilapplikation. Der er dog udfordringer, der skal overvindes, herunder regulering af kryptovaluta og behovet for at respektere visse grænser for at undgå overdreven regulering.
Brugen af Bitcoin-hæveautomater diskuteres også, da de repræsenterer en økonomisk metode til at skaffe ikke-KYC-bitcoins. Afhængigt af lokale regler kan disse automater installeres derhjemme eller på offentlige steder og kan bruges til at tilbyde bitcoins til kære eller til betaling på barer.

Uddannelsen lægger vægt på vigtigheden af ​​uddannelse i forståelsen af ​​Bitcoin. Det antydes, at Bitcoin kan tilbyde en løsning i tilfælde af recession eller hyperinflation, og at det er vigtigt at øge bevidstheden om dets potentiale, før det er for sent. Derudover understreges det, at adskillelsen mellem stat og valuta er lige så essentiel som adskillelsen mellem stat og religion.

Konklusionen er, at Bitcoin præsenteres som en decentraliseret valuta, der kræver offentlig uddannelse og åbenhed for at blive fuldt forstået og brugt. Uddannelsen sigter mod at hjælpe deltagerne med at forstå de forskellige peer-to-peer-købsløsninger og bruge disse værktøjer til at forbedre deres anonymitet og sikkerhed, når de bruger Bitcoin.

## Bonusartikel om privatliv

En fantastisk [artikel](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) af Loïc Morel om KYC og identifikation.
Denne dybdegående artikel udforsker udfordringerne og løsningerne for at bevare privatlivet ved erhvervelse og brug af bitcoins. Loïc afkonstruerer nogle misforståelser om KYC (Know Your Customer) identifikation, detaljerer risiciene forbundet med denne proces og tilbyder teknikker til at opretholde transaktionsanonymitet. Det er et must-read for dem, der ønsker at forstå nuancerne i privatlivets verden inden for Bitcoin og lære, hvordan man bruger værktøjer som CoinJoin, Stonewall og PayJoin til at sløre transaktionssporing og beskytte deres privatliv.