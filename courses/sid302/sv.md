---
name: Liquid Bootcamp Essentials
goal: Få en omfattande förståelse för Liquid Network- och Elements-projekten och lär dig hur du implementerar avancerade lösningar inom konfidentiella transaktioner, tokenisering och decentraliserad nätverksarkitektur.
objectives: 

  - Förstå grunderna i Liquid-arkitekturen och dess förhållande till Bitcoin.
  - Lär dig att konfigurera och använda Liquid-noder med hjälp av Elements-programvaran.
  - Utforska användningen av konfidentiella transaktioner och utfärdande av tillgångar på Liquid Network.
  - Förstå de affärsmässiga och tekniska aspekterna av Liquid för tillämpningar på kapitalmarknader.

---

# Introduktion till Liquid-nätverket


Ge dig ut på en utbildningsresa som är utformad för att ge en djup förståelse för Liquid Network och Elements-projektet. Detta bootcamp kombinerar teori och praktik för att lära dig de tekniska, arkitektoniska och affärsmässiga grunderna som krävs för att implementera och utnyttja Liquid:s funktioner. Från konfidentiella transaktioner till ekosystemdesign är den här kursen idealisk för dem som vill utöka sin kunskap om avancerade verktyg inom Bitcoin-ekosystemet.


Med presentationer av branschexperter täcker kursen ämnen som Liquid-arkitektur, tokeniseringsapplikationer, tekniska koncept för Elements och innovativa användningsfall som Breez SDK. Kursen är utformad för att vara tillgänglig för nybörjare och användare på mellannivå, men erbjuder också värde för erfarna utvecklare som vill behärska Liquid som en plattform för att optimera sina projekt.

+++

# Inledning


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Kursöversikt


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Välkommen till Liquid Bootcamp, en omfattande utbildning som är utformad för att förse dig med kunskap och färdigheter för att effektivt utnyttja Liquid Network och Elements-projektet. Den här kursen erbjuder en omfattande utforskning av Liquid:s särdrag, inklusive Confidential Transactions, tillgångsutgivning och dess federerade nätverksarkitektur, samtidigt som den introducerar de grundläggande koncepten för Elements, programvaran som driver Liquid.


Under hela boot campet kommer du att utforska de praktiska tillämpningarna av Liquid Network, från att sätta upp och driva noder till att förstå dess användning i Bitcoin:s kapitalmarknader och tokenisering. Med presentationer från branschexperter kommer du också att få insikter i avancerade ämnen som HTLC, Breez SDK och Blockstream AMP-projektet.


Denna bootcamp genomfördes ursprungligen som ett personligt evenemang, enligt ett strukturerat schema (som visas på bilden) utformat för livesessioner. För den här kursanpassningen har dock innehållet omorganiserats för att bättre passa ett onlineformat och underlätta studenternas förståelse. Den nya ordningen säkerställer en logisk progression från grundläggande begrepp till mer avancerade och tekniska ämnen, vilket maximerar inlärningsupplevelsen.


Denna resa är strukturerad för att tillgodose deltagare med olika nivåer av expertis och erbjuder en blandning av teoretisk kunskap och praktisk erfarenhet. I slutet av detta boot camp kommer du att ha en gedigen förståelse för Liquid:s arkitektur, dess integration med Bitcoin och hur du använder dess innovativa funktioner för att bygga och optimera finansiella lösningar.


Dyk in i Liquid-sidokedjans värld och frigör dess fulla potential just nu!

# Grundläggande


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid Arkitektur


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network:s arkitektur och modell för samförstånd


Liquid Network är en federerad sidokedja byggd på Elements:s kodbas, utformad för att utöka Bitcoin:s kapacitet samtidigt som den förlitar sig på dess grundläggande säkerhet. Till skillnad från Bitcoin:s [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work) fungerar Liquid enligt en federerad [konsensusmodell](https://planb.academy/resources/glossary/consensus). Nätverket upprätthålls av en globalt distribuerad grupp av medlemmar, inklusive börser, handelsbord och infrastrukturleverantörer. Från dessa medlemmar väljs femton "funktionärer" ut för att agera som blocksignatörer.


Dessa funktionärer producerar [block](https://planb.academy/resources/glossary/block) i en deterministisk rundgång, där ett nytt block genereras varje minut. Denna exakta timing står i kontrast till Bitcoin:s probabilistiska tiominutersintervall. För att ett block ska vara giltigt krävs signaturer från minst 11 av de 15 funktionärerna (en tröskel på två tredjedelar plus en). Denna mekanism ger Liquid "two-block finality", vilket innebär att när en [transaktion](https://planb.academy/resources/glossary/transaction-tx) har bekräftats två gånger (cirka två minuter) är det matematiskt omöjligt att omorganisera kedjan. Denna snabbhet och säkerhet är avgörande för arbitrage, automatiserad handel och snabb avveckling mellan börser.


Federationen är dynamisk. Genom protokollet Dynamic Federation (Dynafed) kan nätverket rotera funktionärer eller uppdatera parametrar utan att det krävs en hård [fork](https://planb.academy/resources/glossary/fork). Detta gör att systemet kan utvecklas och ersätta hårdvara eller medlemmar sömlöst samtidigt som kontinuerlig drift upprätthålls.


### Confidential Transactions och kapitalförvaltning


Ett utmärkande drag för Liquid är dess inbyggda stöd för Confidential Transactions (CT) och flera tillgångar. I den huvudsakliga Bitcoin-kedjan är alla transaktionsdetaljer - avsändare, mottagare och belopp - offentliga. I Liquid använder CT kryptografiska åtaganden för att dölja tillgångstyp och belopp från den offentliga liggaren samtidigt som nätverket kan verifiera att transaktionen är giltig (dvs. att ingen [inflation](https://planb.academy/resources/glossary/inflation) har skett). Endast de deltagare som innehar de dolda nycklarna kan se de specifika värdena, vilket ger en nivå av kommersiell integritet som är nödvändig för institutioner som flyttar stora positioner.


Liquid behandlar alla tillgångar som "infödda" medborgare i [blockkedjan](https://planb.academy/resources/glossary/blockchain). Detta inkluderar Liquid Bitcoin (LBTC), stablecoins som USDT och security tokens. Att utfärda en tillgång kräver inte komplexa smarta kontrakt; det är en grundläggande funktion i protokollet.


#### Reglerade tillgångar och AMP

För tillgångar som kräver efterlevnad, t.ex. säkerhetstoken, använder Liquid Blockstream Asset Management Platform (AMP). Detta introducerar ett tillståndspliktigt lager där transaktioner kräver en andra signatur från en auktoriseringsserver. Detta gör det möjligt för emittenter att genomdriva regler - till exempel vitlistning eller KYC-krav - på en detaljerad nivå, vilket kombinerar effektiviteten hos en blockkedja med de regulatoriska kontrollerna av traditionell finansiering.


### Two-Way Peg och säkerhetsinfrastruktur


Förbindelsen mellan Liquid och Bitcoin upprätthålls genom en tvåvägs peg. För att "pegga in" skickar en användare Bitcoin till en genererad adress på mainchain. Dessa medel är låsta i 102 bekräftelser (ungefär 17 timmar) för att eliminera omorganiseringsrisker. När det har bekräftats präglas ett motsvarande belopp av LBTC på Liquid-sidokedjan.


"Peg-out"-processen gör det möjligt för användare att lösa in LBTC mot Bitcoin. Detta kräver förbränning av LBTC och en kryptografisk auktorisering från federationen. För att förhindra stöld kontrolleras peg-outs strikt av Peg-out Authorization Keys (PAKs) som innehas av federationsmedlemmar. Dessutom kan medel swappas direkt via tredjepartsleverantörer som SideSwap, vilket kringgår avvecklingsfördröjningen för snabbare likviditet.


#### Säkerhetsmoduler för maskinvara (HSM)

Säkerheten upprätthålls strikt genom hårdvara. Funktionärer förvarar inte [privata nycklar](https://planb.academy/resources/glossary/private-key) på vanliga servrar, utan använder i stället HSM:er (Hardware Security Modules). Dessa enheter är lufttäta från värdserverns logik och programmerade med strikta regler. En HSM vägrar t.ex. att signera ett block om dess höjd inte är större än det föregående, vilket förhindrar att historiken skrivs om. Den här "adversariala" säkerhetsmodellen förutsätter att värdservern kan äventyras, vilket gör att nycklarna förblir säkra även om den fysiska platsen utsätts för intrång.


## Grundläggande om Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Grunden för Liquid


Elements är en blockkedjeplattform med öppen källkod som härrör från Bitcoin:s kärnkodbas. Den utökar Bitcoin:s funktionalitet genom att möjliggöra sidokedjor - oberoende blockkedjor som kan överföra tillgångar till och från Bitcoin. Medan Bitcoin Core driver Bitcoin-nätverket är Elements mjukvarumotorn bakom Liquid Network och andra anpassade sidokedjor.


Relationen är okomplicerad: Liquid är en specifik "instans" av en Elements-sidokedja, konfigurerad för produktionsanvändning med en federerad konsensusmodell. Utvecklare som är bekanta med Bitcoin kommer att tycka att Elements är intuitivt, eftersom det behåller samma RPC-gränssnitt (Remote Procedure Call) och kommandoradsstruktur (`elements-cli`, `elements-d`, `elements-qt`). Den viktigaste skillnaden ligger i konfigurationen: genom att ställa in `chain=liquidv1` ansluts en [nod](https://planb.academy/resources/glossary/node) till huvudnätverket Liquid, medan `chain=elementsregtest` skapar en lokal regressionstestmiljö där utvecklare kan generate block direkt och testa utan externa beroenden.


#### Emission av tillgångar

En utmärkande egenskap hos Elements är utfärdande av tillgångar. Till skillnad från Ethereum, där tokens är komplexa smarta kontrakt, är tillgångar i Elements förstklassiga medborgare som skapas via ett enkelt RPC-kommando (`issueasset`).


- Unika identifierare:** Varje tillgång får ett unikt hexadecimalt ID på 64 tecken.
- Reissuance Tokens:** Emittenter kan valfritt skapa reissuance tokens, som ger innehavaren rätt att prägla mer av tillgången senare (användbart för stablecoins eller security tokens).
- Tillgångsregister:** Eftersom hex-ID:n inte är läsbara för människor mappar Blockstream Asset Registry dessa ID:n till namn och tickers (t.ex. "USDT"), liknande en DNS för tillgångar.


### Sekretess via Confidential Transactions


Elements hanterar en av de främsta begränsningarna med publika blockkedjor: bristen på kommersiell integritet. På Bitcoin är varje transaktionsbelopp synligt för hela världen. Elements introducerar **Confidential Transactions (CT)**, som kryptografiskt döljer beloppet och tillgångstypen samtidigt som nätverket kan verifiera transaktionens giltighet.


Detta uppnås med hjälp av **Pedersen Commitments** och **Range Proofs**.


- Pedersen Commitments** ersätter det synliga beloppet med ett kryptografiskt åtagande. På grund av homomorf kryptering kan validatorer kontrollera att *Input Commitments = Output Commitments + Fees* utan att någonsin se de faktiska värdena.
- Range Proofs** förhindrar en användare från att skapa pengar ur tomma intet (t.ex. genom att använda negativa tal) genom att matematiskt bevisa att det dolda värdet är ett positivt heltal inom ett giltigt intervall.


För en utomstående betraktare visar en konfidentiell transaktion giltiga in- och utgångar men döljer *vad* som skickas och *hur mycket*. Endast avsändaren och mottagaren (som har de hemliga nycklarna) kan se data i klartext.


### Utveckling och arbetsflöde för RPC


Interaktion med en Elements-nod sker främst genom dess JSON-RPC-gränssnitt. Detta gör att applikationer skrivna i Python, JavaScript eller Go kan kommunicera med blockkedjan.



- Inställning:** En utvecklare startar vanligtvis i `regtest`-läge. Detta möjliggör omedelbar generering av block (`generateblock`) för att bekräfta transaktioner omedelbart, vilket kringgår blocktiden på 1 minut i det levande nätverket.
- Kommandon:** Standard Bitcoin-kommandon som `getblockchaininfo` är tillgängliga, tillsammans med Elements-specifika kommandon som `dumpblindingkey` (för revision av CT) eller `pegin` (för att flytta BTC till sidokedjan).
- Aliaser:** För att hantera flera noder (t.ex. en "sändare" och en "mottagare" för testning) använder utvecklare ofta skalalias som "e1-cli" och "e2-cli" som pekar på olika datakataloger och simulerar ett [peer-to-peer-nätverk](https://planb.academy/resources/glossary/peertopeer-p2p) på en enda maskin.


Denna arkitektur gör det möjligt för utvecklare att bygga sofistikerade finansiella applikationer - till exempel värdepappersplattformar eller privata betalningsgateways - med hjälp av de robusta och välbekanta verktygen i Bitcoin-ekosystemet.


## Anslutning av Bitcoin-skikt


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Cross-Layer Infrastruktur och HTLC


Bitcoin-ekosystemet har utvecklats till en flerskiktsarkitektur, där Mainchain tillhandahåller avveckling, Lightning erbjuder hastighet och Liquid möjliggör avancerade tillgångsfunktioner. För att flytta värde mellan dessa lager utan centraliserade mellanhänder krävs en pålitlig kryptografisk primitiv: [Hash](https://planb.academy/resources/glossary/hash-function) Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


En HTLC skapar en villkorad [betalningskanal](https://planb.academy/resources/glossary/payment-channel) som länkar samman oberoende system atomiskt. Den fungerar genom två primära begränsningar: ett **hashlås** och ett **tidslås**.


- Hash Lock:** Pengar kan spenderas omedelbart om mottagaren avslöjar en hemlig "förbild" som matchar en specifik kryptografisk hash.
- Tidlåset:** Om mottagaren inte avslöjar hemligheten inom en viss tid (blockhöjd) kan den ursprungliga avsändaren återkräva pengarna.


Denna struktur med dubbla vägar garanterar säkerheten. I en swap över flera lager används samma hashlås i båda nätverken. När mottagaren avslöjar hemligheten för att göra anspråk på medel i ett lager (t.ex. Liquid) blir hemligheten synlig för avsändaren, som sedan kan använda den för att göra anspråk på motsvarande medel i det andra lagret (t.ex. Lightning). Denna kryptografiska bindning garanterar att bytet antingen lyckas för båda parter eller misslyckas för båda, vilket eliminerar risken för att en part förlorar pengar medan den andra vinner dem.


### Uppgradering av Taproot och MuSig2


Äldre HTLC:er ([SegWit](https://planb.academy/resources/glossary/segwit) v0) fungerade bra men led av integritets- och effektivitetsbrister. De krävde publicering av hela [skriptlogiken](https://planb.academy/resources/glossary/script) on-chain, vilket gjorde swap-transaktioner lätt identifierbara för blockchain-analytiker och dyrare på grund av deras datastorlek. Införandet av [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) och MuSig2-protokollet har revolutionerat denna arkitektur.


Taproot möjliggör **Key Aggregation** via MuSig2. Istället för att avslöja ett komplext skript med flera [offentliga nycklar](https://planb.academy/resources/glossary/public-key) låter MuSig2 swapdeltagarna kombinera sina nycklar till en enda aggregerad offentlig nyckel.


- Cooperative "Key Path":** Om båda parter samtycker till swappen (den "lyckliga vägen") undertecknar de transaktionen tillsammans. För nätverket ser detta identiskt ut som en vanlig betalning med en enda signatur. Den tar minimalt med blockutrymme i anspråk och avslöjar absolut ingen information om villkoren för swappen.
- "Script Path":** Om en part inte svarar eller är illvillig avslöjas det underliggande scriptet (som innehåller hash-/tidslås) först då. Detta är organiserat i ett [Merkle-träd](https://planb.academy/resources/glossary/merkle-tree), vilket gör att den ärliga parten endast kan avslöja den specifika gren som behövs för att återvinna medel och hålla resten av kontraktslogiken dold.


### Praktiskt genomförande: Liquid-Blixtbyten


I praktiken möjliggör dessa protokoll ett sömlöst utbyte mellan Bitcoin:s lager. Ett typiskt Liquid-till-Lightning-byte börjar med att en kund begär ett byte från en tjänsteleverantör. Kunden tillhandahåller en [Lightning-faktura](https://planb.academy/resources/glossary/invoice-lightning), och leverantören låser motsvarande Liquid Bitcoin (L-BTC) till en Taproot-aktiverad HTLC-adress.


Atomiteten verkställs när betalningen avvecklas. För att göra anspråk på L-BTC måste tjänsteleverantören ha preimage. De får denna preimage endast när de framgångsrikt betalar kundens Lightning-faktura. I samma ögonblick som Lightning-betalningen slutförs avslöjas förbilden, vilket gör det möjligt för leverantören att låsa upp Liquid-medlen.


#### Wallet-abstraktion och UTXO-hantering

För slutanvändare är denna komplexitet helt abstraherad. Moderna plånböcker som Aqua hanterar nyckelgenerering, fakturaskapande och signeringsprocesser i bakgrunden. Användaren "betalar" helt enkelt en Lightning-faktura med sitt Liquid-saldo. Bakom kulisserna hanterar tjänsten [UTXO](https://planb.academy/resources/glossary/utxo)-konsolidering och sveper regelbundet små, ej begärda eller återbetalade utgångar för att upprätthålla [wallet](https://planb.academy/resources/glossary/wallet)-effektiviteten och minimera avgiftspåverkan under perioder med hög trafik.


## Liquid Network Översikt


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Arkitektur och samförstånd


Liquid Network fungerar som en federerad sidokedja byggd på kodbasen **Elements**. Medan Elements - en fork av Bitcoin Core - tillhandahåller mjukvarufundamentet, är Liquid implementeringen av produktionsnätverket. Till skillnad från Bitcoin:s Proof-of-Work, som förlitar sig på konkurrenskraftiga [mining](https://planb.academy/resources/glossary/mining), använder Liquid en **Federated Consensus**-modell.


Nätverket upprätthålls av femton globalt distribuerade "funktionärer" Dessa enheter driver specialiserade servrar som utför två kritiska roller:

1.  **Blockproduktion:** Funktionärer turas om att skapa block i ett deterministiskt round-robin-schema, vilket genererar ett nytt block exakt varje minut.

2.  **Blocksignering:** För att ett block ska vara giltigt måste det signeras av minst 11 av de 15 funktionärerna.


Detta tröskelvärde på 11 av 15 säkerställer att nätverket kan tolerera fel på upp till fyra noder utan att stanna. Den främsta fördelen med denna avvägning är **deterministisk finalitet**. Medan Bitcoin handlar om sannolikheter uppnår Liquid säkerhet för avveckling efter två block (cirka två minuter). När ett block har en enda bekräftelse ovanpå sig kan kedjan inte omorganiseras, vilket gör den mycket effektiv för arbitrage och snabb avveckling.


### Confidential Transactions och inhemska tillgångar


Liquid:s utmärkande egenskap är standardanvändningen av **Confidential Transactions (CT)**. På Bitcoin mainchain är avsändare, mottagare och belopp offentliga. Liquid förbättrar detta genom att kryptografiskt dölja beloppet och tillgångstypen, medan avsändarens och mottagarens adresser förblir synliga för verifiering.


För att säkerställa att en användare inte kan trycka pengar (t.ex. genom att skicka negativa belopp) använder Liquid **Pedersen Commitments** och **Range Proofs**. Dessa kryptografiska primitiver gör det möjligt för nätverket att verifiera att *Inputs = Outputs + Fees* och att alla värden är positiva heltal, utan att någonsin avslöja de specifika siffrorna i den offentliga huvudboken. Endast de deltagare som innehar blindnycklarna kan se de dekrypterade uppgifterna.


#### Emission av tillgångar

Liquid behandlar alla tillgångar som "inbyggda" Oavsett om det är Liquid Bitcoin (L-BTC), ett stablecoin som USDT eller ett värdepapper token, delar de alla samma arkitektur. Att utfärda en tillgång kräver inga smarta kontrakt - bara ett enkelt RPC-samtal.


- Oreglerade tillgångar:** Kan emitteras utan tillstånd av vem som helst.
- Reglerade tillgångar:** Med hjälp av Blockstream Asset Management Platform (AMP) kan emittenter genomdriva efterlevnadsregler (som KYC / AML) genom att kräva en andra signatur från en auktoriseringsserver innan en tillgång kan flyttas.


### Den dubbelriktade pinnen och den dynamiska federationen


Bryggan mellan Bitcoin och Liquid är **Two-Way Peg**. Den gör det möjligt för användare att flytta BTC till sidokedjan (Peg-in) och tillbaka till mainchain (Peg-out).


**Peg-in-processen:**

Detta är tillståndslöst. En användare skickar BTC till en federationskontrollerad adress. För att skydda mot omorganisationer av Bitcoin-blockkedjan måste dessa medel vänta på **102 bekräftelser** (ca 17 timmar) innan motsvarande L-BTC präglas på sidokedjan.


**Peg-out-processen:**

För att återvända till Bitcoin bränns L-BTC. För att förhindra stöld av de underliggande Bitcoin-reserverna är dock peg-outs inte helt automatiserade. De kräver auktorisering från en medlem som innehar en **Peg-Out Authorization Key (PAK)**. Själva Bitcoin-medlen är säkrade i en wallet med 11 av 15 multisignaturer, med nycklar som hålls i hårdvarusäkerhetsmoduler (HSM) som är air-gapped från funktionärernas huvudservrar.


**Dynamiska federationen (Dynafed):**

För att säkerställa lång livslängd använder Liquid Dynafed, ett protokoll som gör det möjligt för nätverket att rotera funktionärer eller uppdatera parametrar utan en hård fork. Om en funktionär behöver bytas ut sänder nätverket ut en övergångstransaktion. Efter en överlappningsperiod på två veckor tar den nya konfigurationen över, vilket gör att federationen kan utvecklas sömlöst samtidigt som den upprätthåller kontinuerlig drifttid.


## Ekosystem och kapitalmarknader


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Affärsstrategi och ekosystem


Liquid är mer än en teknisk sidokedja; det är ett affärsfokuserat infrastrukturlager som är utformat för att hantera de komplexa kraven på kapitalmarknaderna som Bitcoin mainchain inte kan stödja effektivt. Medan [Lightning Network](https://planb.academy/resources/glossary/lightning-network) optimerar för högfrekventa betalningar av lågt värde, riktar Liquid in sig på överföringar av högt värde, emission av tillgångar och avveckling mellan börser.


Ekosystemet drivs av **Liquid Federation**, ett konsortium bestående av cirka 73 företag, däribland börser, handelsplatser och infrastrukturleverantörer. Denna samarbetsmodell speglar traditionella finansiella clearinghus men fungerar med större transparens och betydligt kortare avvecklingstider (2 minuter jämfört med T+2 dagar).


### Tokenisering av Real-World Assets (RWA)


Kärnan i Liquid:s affärsidé är "Tokenization" - att representera verkligt värde (aktier, obligationer, mining-kontrakt) som digitala tokens på blockkedjan. Detta ger tre primära fördelar:

1.  **24/7 Global Markets:** Avskaffande av banktider och geografiska begränsningar.

2.  **Driftseffektivitet:** Eliminering av avstämningsfel genom en delad, oföränderlig huvudbok.

3.  **Atomic Settlement:** Minskar motpartsrisken genom att säkerställa att leverans sker samtidigt med betalning.


#### Reglerade tillgångar och AMP

De flesta institutionella tillgångar kan inte handlas utan tillstånd på grund av juridiska krav. **Asset Management Platform (AMP)** är den tekniska standard som upprätthåller dessa regler.


- Whitelisting:** Emittenter kan begränsa innehav och handel till KYC-verifierade adresser.
- Multisig Control:** Åtgärder för efterlevnad (som att frysa stulna medel eller återutfärda förlorade tokens) hanteras via multisignaturauktorisation, vilket säkerställer att ingen enskild anställd kan agera ensidigt.


Denna infrastruktur är live idag. Plattformar som **Stalker** tillhandahåller end-to-end-tokeniseringstjänster i Europa, medan **Sideswap** fungerar som en decentraliserad börs och wallet utan förvaring, vilket möjliggör peer-to-peer-handel med tillgångar som **Blockstream Mining Note (BMN)** och tokeniserade MicroStrategy-aktier (CMSTR).


### Framgång i den verkliga världen: Fallstudien Mayfell


Det mest övertygande beviset på Liquid:s användbarhet kommer från **Mayfell** i Mexiko. På en marknad där traditionell finansiering förlitar sig på pappersskuldebrev - som är utsatta för förlust, bedrägeri och långsam bearbetning - flyttade Mayfell hela infrastrukturen till Liquid.



- Skala:** Över 25.000 skuldebrev utfärdade, motsvarande **1,5 miljarder dollar+** i värde.
- Sekretess:** Med Liquid:s Confidential Transactions är lånebeloppen endast synliga för långivaren och låntagaren, vilket bevarar den kommersiella integriteten samtidigt som revisorer kan verifiera huvudbokens integritet.
- Påverkan:** Genom att ansluta långivare som inte är banker till globala kapitalmarknader via blockchain minskade Mayfell kostnaderna och utökade tillgången till kredit för mexikanska små och medelstora företag, vilket visar att Liquid:s värdeförslag sträcker sig långt bortom spekulativ handel.


### Strategisk positionering jämfört med andra kedjor


Liquid konkurrerar på en fullsatt marknad av tokeniseringsplattformar (Ethereum, Solana, etc.), men har tydliga strategiska fördelar:


- Regleringsklarhet:** Liquid använder Bitcoin (L-BTC) som sin ursprungliga tillgång. Den har inte en förminerad token eller en ICO, vilket undviker riskerna med "oregistrerad säkerhet" som plågar andra L1-blockkedjor.
- Stabilitet:** Till skillnad från Ethereums kontomodell där misslyckade transaktioner fortfarande ger upphov till gasavgifter, är Liquid:s UTXO-modell deterministisk och tillförlitlig för verksamhetskritiska finansiella data.
- Sekretess:** Standardkonfidentialitet är ett krav för de flesta finansinstitut, en funktion som Liquid erbjuder inbyggt och som offentliga kedjor kämpar för att implementera utan komplexa tillägg.


För utvecklare erbjuder detta ekosystem en tydlig möjlighet: att bygga de verktyg (instrumentpaneler, plånböcker, compliance-integrationer) som överbryggar traditionell finansiering med Bitcoin:s säkra avvecklingslager.


## Blockström AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Tillåten tillgångskontroll på Liquid


Blockstream AMP (Asset Management Platform) fungerar som ett kritiskt infrastrukturlager på Liquid Network, utformat speciellt för emittenter av reglerade digitala värdepapper och stablecoins. Medan Liquid tillhandahåller ett tillståndslöst baslager med inbyggd tillgångsutgivning, kräver reglerade enheter ofta strikt tillsyn och efterlevnadsfunktioner. AMP överbryggar detta gap genom att införa ett tillåtet kontrollager över specifika tillgångar utan att offra integritetsfördelarna med Liquid:s Confidential Transactions.


Plattformens kärnvärde bygger på två primära funktioner: omfattande insyn i emittenten och transaktionsauktorisering. Till skillnad från vanliga Liquid-tillgångar där belopp och typer är blinded för alla utom deltagarna, gör AMP-tillgångar det möjligt för emittenten att upprätthålla en helt unblinded revisionsspår. Denna transparens är viktig för lagstadgad rapportering och interna revisioner. Dessutom tillämpar AMP en strikt auktoriseringsmodell genom en medsigneringsmekanism. Varje överföring av en AMP-tillgång kräver en signatur från AMP-servern. Detta gör det möjligt för emittenter att genomdriva komplexa regler off-chain - som att frysa konton, vitlista ackrediterade investerare eller införa överföringsgränser - som effektivt fungerar som en centraliserad grindvakt i ett decentraliserat nätverk.


#### Operativa avvägningar

Denna arkitektur medför specifika avvägningar. Systemet är beroende av AMP-serverns tillgänglighet; om servern fungerar som medsignatur och går offline pausas likviditeten i tillgångarna. Dessutom måste investerare acceptera att emittenten har full insyn i deras innehav, samtidigt som integriteten mellan användarna upprätthålls. Denna modell är idealisk för kompatibla säkerhetstoken men olämplig för censurresistenta [kryptovalutor](https://planb.academy/resources/glossary/cryptocurrency).


### Arkitekturens utvecklings- och integrationsvägar


AMP:s ekosystem övergår för närvarande från sin första iteration till en mer flexibel, interoperabel "version 2"-arkitektur. Det äldre systemet krävde att emittenter skulle upprätthålla helt synkroniserade Elements-noder och tvingade utvecklare att förlita sig starkt på den monolitiska Green SDK. Detta var visserligen funktionellt, men skapade höga tekniska inträdeshinder och begränsade wallet-val.


Nästa generations arkitektur förenklar dessa krav i grunden genom att flytta komplexiteten till servern. I den nya modellen sköter AMP-servern det tunga arbetet med att konstruera transaktioner, välja UTXO och beräkna avgifter. Den presenterar utfärdaren med en delvis signerad Elements-transaktion (PSET) som helt enkelt kräver en signatur. Detta tillvägagångssätt med "smart server, dum wallet" eliminerar behovet för emittenter att köra fullständiga noder och möjliggör användning av hårdvaruplånböcker och standardinställningar för multisignaturer för likviditetshantering.


För utvecklare innebär denna utveckling att man rör sig bort från proprietära SDK:er mot standarddeskriptorer och PSET-arbetsflöden. Plånböcker kan nu registrera multisignaturdeskriptorer med AMP-servern för att fastställa auktoriseringsrättigheter. Detta anpassar AMP-utvecklingen till bredare Bitcoin wallet-standarder, vilket gör integrationen tillgänglig för alla applikationer som kan hantera PSBT / PSET-format. Utvecklare som bygger idag uppmuntras att använda verktyg som Liquid Wallet Kit (LWK), som stöder dessa moderna, deskriptorbaserade arkitekturer, vilket säkerställer att deras applikationer är framtidssäkrade för de nya AMP-standarderna.


### Ekosystemet Liquid Wallet och konfidentialitet


Att bygga applikationer på Liquid kräver navigering i en mer komplex stack än standard Bitcoin-utveckling på grund av funktioner som inbyggda tillgångar och Confidential Transactions. Ekosystemet stöds av en skiktad arkitektur: lågnivåbibliotek som `secp256k1-zkp` hanterar kryptografiska primitiver, medan verktygssatser på högre nivå hanterar wallet-logik.


Historiskt sett har Green Development Kit (GDK) utgjort en omfattande men rigid lösning. Det moderna alternativet är Liquid Wallet Kit (LWK), som erbjuder ett modulärt tillvägagångssätt. LWK separerar problem i olika lådor - hanterar deskriptorer, signering och hårdvarukommunikation oberoende av varandra - vilket ger utvecklare flexibiliteten att bygga anpassade lösningar utan att behöva ta hänsyn till kostnaderna för ett monolitiskt bibliotek.


#### Hantering Confidential Transactions

Den mest distinkta utmaningen i detta ekosystem är att hantera blindingens livscykel. I Liquid krypteras transaktionsutgångar med hjälp av ECDH-nyckelutbyte (Elliptic Curve Diffie-Hellman). En avsändare använder mottagarens offentliga nyckel för att kryptera tillgångsbelopp och typer, vilket genererar ett räckviddsbevis som verifierar transaktionens giltighet utan att avslöja värden.


För att en wallet ska fungera måste den lyckas vända denna process. När en wallet upptäcker en inkommande transaktion försöker den avblinda utmatningen med hjälp av sin privata avblindningsnyckel. Om den delade hemligheten matchar kan wallet dekryptera värdet och lägga till det i användarens saldo. Denna process är beräkningsintensiv och kräver exakt hantering av blindningsfaktorer för att säkerställa att transaktioner är matematiskt balanserade, en komplexitet som verktyg som LWK syftar till att abstrahera bort för utvecklaren.


# Teknisk


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Nodeless


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Introduktion till Breez Liquid SDK


Breez Liquid SDK är en självförvaltande verktygslåda med öppen källkod som är utformad för att överbrygga klyftan mellan Liquid Network och det bredare Bitcoin-ekosystemet. Dess primära uppdrag är att abstrahera komplexiteten i Lightning Network-nodhantering och atomära swappar, så att utvecklare kan bygga friktionsfria finansiella applikationer.


Kärnlogiken är byggd med en "mobile-first"-filosofi och är skriven i Rust för prestanda och säkerhet, men den använder UniFFI (Unified Foreign Function Interface) för att tillhandahålla inbyggda bindningar för Kotlin, Swift, Python, C#, Dart och Flutter. Detta säkerställer att utvecklare kan integrera Bitcoin-funktionalitet i sin önskade miljö utan att hantera kryptografiska operationer på låg nivå.


**Transaktionstyper som stöds: **

SDK arbetar med Liquid som sin "hemmabas" Det utmärker sig i tre specifika operationer:

1.  **Liquid-till-Liquid:** Direkta on-chain-överföringar.

2.  **Liquid-till-Lightning:** Betalning av Lightning-fakturor med Liquid-medel.

3.  **Liquid-till-Bitcoin:** Byte av medel direkt till Bitcoin mainchain.


*SDK:n stöder inte direkta Lightning-till-Lightning- eller Bitcoin-till-Bitcoin-transaktioner. Det är strikt ett Liquid-centrerat verktyg.*


### Betalningsarkitekturer: Submarine Swaps


För att uppnå interoperabilitet mellan Liquid, Lightning och Bitcoin utan centraliserade förvaringsinstitut förlitar sig Breez på **Submarine Swaps**. Dessa är atomära operationer där en transaktion antingen slutförs framgångsrikt på båda nätverken eller misslyckas på båda, vilket säkerställer att medel aldrig går förlorade under transitering.


#### Lightning Send (Submarine Swap)

När en användare betalar en Lightning-faktura sänder SDK en "lock-up"-transaktion på Liquid Network. Detta sätter effektivt pengarna i spärr. Swapleverantören (Boltz) upptäcker detta, betalar Lightning-fakturan och använder sedan betalningens förbild (det kryptografiska kvittot) för att göra anspråk på de låsta Liquid-medlen.


#### Blixten tar emot (omvänt ubåtsbyte)

Att ta emot Lightning är den omvända processen. Användaren genererar en faktura och swapleverantören låser medel på Lightning Network. SDK övervakar denna process via WebSockets. När låset har bekräftats utför SDK automatiskt en claim-transaktion för att flytta motsvarande medel till användarens Liquid wallet.


#### Tvärkedja Bitcoin

För Liquid-till-Bitcoin-överföringar använder arkitekturen en "dual-swap"-mekanism. Lock-up-transaktioner sker på båda kedjorna samtidigt. Avsändaren gör anspråk på medel på Bitcoin, medan mottagaren gör anspråk på medel på Liquid. Detta möjliggör förtroendefri överbryggning utan beroende av federated peg-outs eller centraliserade utbyten.


### Utvecklare Interface och automatiserad hantering


Breez SDK förenklar utvecklarens upplevelse genom att kondensera komplexa finansiella flöden till en standardiserad trestegsprocess: ** Anslut, förbered och utför**.


1.  **Connect:** Initialiserar wallet, synkroniserar med blockkedjan med hjälp av Liquid Wallet Kit (LWK) och upprättar WebSocket-anslutningar för övervakning i realtid.

2.  **Prepare:** Innan du sätter in pengar beräknar och returnerar detta steg alla tillhörande nätverksavgifter och swapkostnader, så att användargränssnittet kan presentera en tydlig total för användaren.

3.  **Execute:** Detta steg konstruerar transaktionen, sänder ut den och initierar bytet.


#### Automatiserade säkerhetsmekanismer

En av SDK:s mest kritiska funktioner är **Automatiserad återbetalningshantering**. I händelse av ett nätverksfel eller en icke samarbetsvillig motpart kan medel teoretiskt sett fastna i ett tidslåst kontrakt. SDK abstraherar återhämtningslogiken helt och hållet. Den övervakar tillståndet för varje swap; om en swap misslyckas eller tidsbegränsas, konstruerar och sänder SDK automatiskt återbetalningstransaktionen för att återföra medel till användarens wallet.


Dessutom hanterar SDK **Metadata Resolution**. Den sammanfogar off-chain swap-data (som tillhandahålls av Boltz swapper) med on-chain transaktionshistorik. Detta säkerställer att användarens transaktionshistorik är läsbar för människor och visar fakturadetaljer och betalningssammanhang snarare än bara råa hexadecimala transaktionshashar.


# Sista avsnittet


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Recensioner & betyg


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Slutlig tentamen


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Slutsats


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>