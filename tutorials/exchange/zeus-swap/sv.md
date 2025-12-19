---
name: Zeus Swap
description: Icke frihetsberövande Exchange-tjänst mellan On-Chain och Lightning Network bitcoins
---

![cover](assets/cover.webp)



Bitcoin-ekosystemet är tudelat: huvudnätverket (On-Chain) erbjuder maximal säkerhet, medan Lightning Network möjliggör omedelbara transaktioner. Denna två-Layer-arkitektur skapar en praktisk utmaning: hur kan medel överföras effektivt mellan dessa två lager utan centraliserade mellanhänder?



Problemet är konkret: du får en Lightning-betalning men vill behålla den i Cold-lagring, eller omvänt, du har On-Chain-bitcoins men behöver Lightning-likviditet. Traditionella lösningar innebär manuell öppning/stängning av Lightning-kanaler (kostsamt och tekniskt) eller centraliserade plattformar som kräver kundkännedom.



Zeus Swap löser detta problem med en automatiserad Exchange-tjänst utan förmyndare. Den har utvecklats av Zeus LSP och gör att du kan konvertera On-Chain bitcoins till Lightning satoshis i båda riktningarna, utan att anförtro dina medel till en mellanhand. Processen använder atomkontrakt (HTLC) som garanterar att Exchange antingen kommer att slutföras eller avbrytas.



Innovationen ligger i dess enkelhet: bara några klick för en Exchange som bevarar din finansiella suveränitet, utan krav på registrering eller kundkännedom.



## Vad är Zeus Swap?



Zeus Swap är en Exchange-likviditetstjänst som utvecklats av Zeus LSP och som möjliggör atomära swappar mellan Bitcoin-huvudnätverket och Lightning Network. Det är en teknisk infrastruktur som använder submarina swappar och omvända swappar för att underlätta tvåvägskonvertering mellan On-Chain BTC och Lightning satoshis, samtidigt som operationens icke-frihetsberövande karaktär bevaras.



### Teknisk arkitektur



Zeus Swap använder Boltz öppna källkod Bitcoin/Lightning atomic swap-teknik. Protokollet använder Hash Time Locked Contracts (HTLC): kontrakt som låser medel med två frigöringsvillkor (avslöjande av en kryptografisk hemlighet eller tidsutgång).



För ett ubåtsbyte (On-Chain → Lightning) skickar användaren bitcoins till en Address som innehåller Hash i en Lightning Invoice. Zeus LSP låser upp dessa medel endast genom att betala motsvarande Invoice och avslöja förbilden som automatiskt låser upp bitcoins. Denna mekanism garanterar atomicitet.



För en omvänd swap (Lightning → On-Chain) betalar användaren en Lightning Invoice från Zeus LSP, vilket avslöjar en förbild som möjliggör frisläppandet av en förberedd Bitcoin-transaktion till destinationen Address.



För mer information om hur Lightning Network fungerar, ta en titt på vår dedikerade kurs :



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Affärsmodell



Zeus LSP fungerar som market maker och upprätthåller On-Chain och Lightning-likviditet för att honorera swappar. För swappar tillämpar Zeus en rörlig avgift (vanligtvis 0,1 % till 0,5 % beroende på riktning och villkor) plus Bitcoin:s Mining-avgift, som visas transparent före validering.



Som Lightning Service Provider optimerar Zeus kostnaderna tack vare sin expertis inom kanalöppning på begäran, effektiv routing och skräddarsydda likviditetslösningar.



### Integration



Zeus Wallet integrerar tjänsten nativt, vilket möjliggör byten utan att lämna Interface Bitcoin/Lightning. Detta eliminerar friktionen med att kopiera och klistra in mellan applikationer.



Den oberoende Interface-webben förblir tillgänglig för alla plånböcker, vilket garanterar maximal flexibilitet vid användning.



## Huvudsakliga egenskaper



### Dubbelriktade swappar



Zeus Swap erbjuder två typer av Exchange:



** Ubåtsbyten (On-Chain → Lightning)**: injicera Lightning-likviditet från dina Bitcoin-reserver, användbart för att mata en mobil Wallet- eller Lightning-nod utan att manuellt öppna kanaler.



**Reverse swaps (Lightning → On-Chain)**: konvertera Lightning satoshis till On-Chain bitcoins för långtidsförvaring, vilket undviker kostsamma kanalstängningar.



### Användargränssnitt



**Interface web** (swaps.zeuslsp.com): förenklad upplevelse utan registrering, guidad process med realtidsvisning av avgifter och status.



**Zeus Wallet integration**: swappar direkt från applikationen, automatisk hantering av fakturor och adresser, vilket eliminerar hanteringsfel.



### Säkerhet och återhämtning



Varje swap genererar en unik Contract med oföränderliga parametrar: Hash Lightning, timeout, återbetalning Address. I händelse av fel, automatisk återställning via Address som tillhandahålls, oberoende av Zeus LSP.



**Zeus Swaps Rescue Key**: under ett On-Chain → Lightning-byte genererar Zeus automatiskt en universell återställningsnyckel som ersätter de gamla individuella återbetalningsfilerna. Den här unika nyckeln fungerar på alla enheter och för alla byten som skapas med den. Det är viktigt att ladda ner och spara den här nyckeln på en säker plats för att kunna återfå dina pengar i händelse av ett swapfel.



### Optimering av nätverk



Zeus Swap justerar automatiskt utgångstider och Mining-avgifter enligt nätverksförhållandena. Zeus-användare drar nytta av avancerade alternativ: val av LSP, anpassade fördröjningar, kompatibilitet med andra tjänster (Boltz).



## Installation och användning



### Metoder för åtkomst



**Interface web** (swaps.zeuslsp.com): Universallösning som är kompatibel med alla plånböcker, ingen installation krävs, perfekt för tillfällig användning.



**Zeus app** (iOS/Android): integrerad upplevelse som kombinerar Wallet och swappar, lämplig för vanliga användare.



Se vår Zeus-handledning för att lära dig mer om denna kompletta Wallet :



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Webbkonfiguration



**On-Chain → Blixten**: Processen börjar med att konfigurera bytet på Interface-webben Zeus Swap. Användaren kan använda pilen mellan fälten On-Chain och Lightning för att vända riktningen på bytet.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: val av belopp (Sats 50 000 → Sats 49 648 efter avgifter) med transparent visning av nätavgifter (Sats 302) och Zeus-tjänst (Sats 50).*



Under processen erbjuder Zeus dig att ladda ner den universella återställningsnyckeln :



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Nedladdningsdialog för Zeus Swaps Rescue Key - en universalnyckel som ersätter de gamla individuella ersättningsfilerna*



Om du redan har en nyckel kan du kontrollera den med Zeus:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface för att kontrollera giltigheten för en befintlig Zeus Swaps Rescue Key*



När Zeus har konfigurerats genererar den Bitcoin-depån Address och visar instruktionerna :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Sidan för slutförande av byte: QR-kod och Bitcoin Address för att skicka 50 000 Satss, med påminnelse om 24 timmars utgångsdatum*



Swappen väntar sedan på bekräftelse från Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Status "Transaktion i Mempool" - inväntar bekräftelse från Bitcoin för att slutföra swappen*



När detta bekräftats genomförs bytet automatiskt:



![Swap réussi](assets/fr/06.webp)



*Bekräftelse på framgång: 49.648 Sats mottagna på Lightning efter avdrag för nät- och serviceavgifter*



### Använda Zeus-appen



**Blixt → On-Chain**: Zeus-applikationen erbjuder en integrerad upplevelse för omvända swappar (Lightning till Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Zeus huvudskärm visar saldon för Lightning (69 851 Sats) och On-Chain (38 018 Sats), tillgång till swappar via sidomenyn*



![Configuration du swap reverse](assets/fr/08.webp)



*Interface skapande av omvänd swap: 50.000 Sats Lightning → 49.220 Sats On-Chain, med nätavgifter (530 Sats) och service (250 Sats) tydligt angivna. Användare kan antingen manuellt ange en Bitcoin som tar emot Address, eller generate en automatiskt från Wallet Zeus via knappen "generate On-Chain Address".*



![Finalisation du swap mobile](assets/fr/09.webp)



*Skärmar för slutförande: Betalningsskärm för Lightning Invoice med "BETALA DENNA Invoice", bekräftelse på lyckad Lightning-betalning på 9,96 sekunder och saldoutdrag med 49 162 Sats som väntar på bekräftelse*



### Övervakning och säkerhet



Varje swap har en unik identifierare med spårning i realtid. Fullständig förloppsvisning, automatiska varningar för utgångsdatum. Automatiska laddningsrekommendationer beroende på nätförhållandena.



## Fördelar och begränsningar



### Fördelar





- Enkelhet**: Byte med några klick jämfört med manuell kanalmanipulation
- Icke frihetsberövande**: ingen kundkännedom, inget konto, medel aldrig anförtrodda till en tredje part
- Transparens**: avgifterna visas tydligt före validering (0,1% till 0,5% + minimiavgift beroende på användartester - kontrollera aktuella avgifter vid varje swap)
- Mobilintegration**: inbyggd upplevelse i Zeus Wallet



### Begränsningar





- Utgångstider**: högst 24-48 timmar, misslyckande om Bitcoin inte bekräftas i tid
- Beloppsgränser**: minst 25 000 Sats, Zeus LSP likviditet varierande beroende på villkor
- Spårar On-Chain**: HTLC-skript som potentiellt kan identifieras genom Blockchain-analys
- Bekräftelse krävs**: minst 10 minuter för validering av Bitcoin



## Bästa praxis



### Tidplan och kostnader





- Håll koll på Mempool.space under perioder med låg trängsel
- Föredra helger och lågtrafik för att minska kostnaderna för Mining
- Beräkna lönsamhet: små belopp kontra öppning av direktkanal



### Säkerhet





- Kontrollera Bitcoin-adresserna noggrant (kopiera och klistra in rekommenderas)
- Säkerhetskopiera Zeus Swaps Rescue Key**: ladda ner och förvara återställningsnyckeln på en säker plats
- Dokument: Contract ID, återbetalning Address, utgångsdatum
- Använd lämpliga Mining-avgifter för snabb bekräftelse



### Strategi för användning





- Balansera On-Chain/Lightning-likviditet för att passa dina behov
- Zeus Swap för engångsjusteringar, direktkanaler för permanenta behov



## Jämförelse med andra swap-tjänster



### Zeus Swap vs Boltz Exchange



Zeus Swap använder Boltz backend-teknik, men gör några viktiga förbättringar:



**Zeus Swap-förmåner** :




- Interface unified**: inbyggd integration i Zeus Wallet vs Interface webbteknik Boltz
- WebSocket API**: uppdateringar i realtid jämfört med manuell polling
- Automatiserad hantering**: automatisk fakturering och Address-hantering
- Mobilsupport**: endast optimering för smartphones jämfört med datorer
- Swagger-dokumentation**: komplett REST API för utvecklare



**Boltz förblir fördelaktigt** för totalt oberoende och användning med alla Bitcoin/Lightning-installationer.



Zeus Swap omvandlar beprövad Boltz-teknik till en vanlig användarupplevelse, jämförbar med skillnaden mellan ett råprotokoll och en användarvänlig applikation.



### Zeus Swap vs Phoenix/Breez (integrerade swappar)



Phoenix och Breez integrerar transparenta swap-funktioner som döljer den tekniska komplexiteten för slutanvändaren. Phoenix använder ett automatiskt swap-in/swap-out-system där användaren inte uttryckligen skiljer mellan Bitcoin-lager: han "skickar till en Bitcoin Address" och applikationen hanterar bytet i bakgrunden.



Detta ultraförenklade tillvägagångssätt passar perfekt för nybörjare, men begränsar förståelsen och kontrollen av verksamheten. Zeus Swap har en mer pedagogisk filosofi: användarna förstår att de byter mellan två olika lager och utvecklar gradvis sin förståelse för ekosystemet Two-Layer Bitcoin.



## Detaljerad jämförelse av avgifter och limiter (2024)



⚠️ **Varning**: Avgifterna kan variera över tid beroende på marknadsförhållanden och serviceuppdateringar. Kontrollera alltid avgifterna som visas i Interface innan du validerar en swap.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap erbjuder en balans mellan användarvänlighet och teknisk kontroll: mer lättillgänglig än Boltz, mer flexibel än Phoenix/Breez, med en strikt icke-frihetsberövande metod.



## Slutsats



Zeus Swap representerar en betydande innovation i Bitcoin-ekosystemet och löser på ett elegant sätt utmaningen med interoperabilitet mellan huvudnätverket och Lightning Network. Genom att kombinera den kryptografiska robustheten hos atomära swappar med en tillgänglig användarupplevelse demokratiserar denna tjänst Bitcoin dual-Layer-hantering utan att kompromissa med principerna för finansiell suveränitet.



Zeus Swaps icke-förvaltande arkitektur, som är ett arv från Boltz beprövade teknik, säkerställer att dina medel förblir under din exklusiva kontroll under hela swapprocessen. Detta tillvägagångssätt respekterar andan i Bitcoin samtidigt som det erbjuder den användarvänlighet som krävs för mainstream adoption. Pristransparens och avsaknad av KYC-processer förstärker detta unika värdeerbjudande.



För den moderna Bitcoin-användaren är Zeus Swap ett strategiskt verktyg för att optimera fördelningen av likviditet efter behov: On-Chain säker lagring för långsiktiga besparingar, Lightning-tillgänglighet för dagliga utgifter och mikrotransaktioner. Denna flexibilitet omvandlar Bitcoin-hantering från en teknisk begränsning till en konkurrensfördel.



Den framtida utvecklingen av Zeus Swap, med stöd av det erfarna Zeus LSP-teamet och Boltz open source-community, lovar fortsatta förbättringar när det gäller kostnader, behandlingstider och användarupplevelse. Denna tjänst är en del av den bredare trenden mot mognad av Bitcoin-infrastrukturen, där teknisk sofistikering blir transparent för slutanvändaren.



## Resurser



### Officiell dokumentation




- [Zeus Swap - Webbportal](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobilapplikation] (https://zeusln.app)
- [Blog Zeus - Meddelanden och handledning](https://blog.zeusln.com)
- [Teknisk dokumentation för Zeus](https://docs.zeusln.app)



### Gemenskap och stöd




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus] (https://t.me/ZeusLN)
- [GitHub Zeus] (https://github.com/ZeusLN)