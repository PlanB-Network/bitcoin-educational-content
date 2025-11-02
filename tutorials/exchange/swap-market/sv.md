---
name: SwapMarket
description: Bitcoin och Lightning swap services aggregator
---

![cover](assets/cover.webp)



Överföring av medel mellan Bitcoin On-Chain och Lightning Network kräver i allmänhet antingen manuell öppning av Lightning-kanaler (tekniskt och kostsamt) eller användning av centraliserade swapplattformar med KYC. SwapMarket erbjuder ett alternativ: Trustless atomära swappar via konkurrenskraftiga leverantörer, utan KYC.



Innovation: även om leverantörerna är mellanhänder garanterar HTLC (*Hash Time Locked Contracts*) matematiskt att dina medel förblir under din kontroll. Sammanslagningen av flera leverantörer (Boltz, ZEUS Swaps, Eldamar, Middle Way) skapar priskonkurrens. Interface webb öppen källkod själv värd.



## Vad är SwapMarket?



SwapMarket är en aggregator med öppen källkod som lanserades 2024 och fungerar som en jämförelsefunktion för Bitcoin/Lightning-swapleverantörer. Användaren jämför direkt villkoren (avgifter, likviditet, limiter) och väljer den optimala leverantören.



### Teknisk arkitektur



**Frontend på klientsidan**: 100% klientapplikation (Fork Boltz Web App) hostad på GitHub Pages. Koden körs i webbläsaren utan backend-server. Historik lagras lokalt (cookies/cache). Offentlig och granskningsbar källkod.



**Upptäckt av leverantör** : Hard-kodad lista i `src/configs/Mainnet.ts`. Nya leverantörer läggs till via Pull Request eller e-post.



**Oberoende backends**: Varje leverantör driver sin egen Boltz-backend. Interface frågar API:erna i realtid för att jämföra offerter direkt.



**HTLC Atomic Swaps**: Hash Time Locked Contracts garanterar atomicitet: antingen genomförs swappen eller så återfår varje part sina medel. Motpartsrisk elimineras matematiskt.



### Filosofi



SwapMarket minskar centraliseringen genom att skapa konkurrens mellan leverantörer om avgifter och likviditet. Ingen KYC, öppen källkod, självvärd kod, multiplicering av oberoende operatörer för att undvika enskilda misslyckanden.



## Huvudsakliga egenskaper



### Leverantörens marknadsplats



Interface visar alla aktiva leverantörer: leverantörens namn, tillämpade avgifter (procent och/eller fasta), lägsta/maximala tillgängliga belopp och swapptyper som stöds. Programmet ställer direkta frågor till API:erna för varje leverantör som refereras till i konfigurationsfilen för att hämta offerter i realtid. Konkurrensen mellan leverantörerna garanterar optimala priser, i allmänhet omkring 0,5% för standardswappar.



### Dubbelriktade swappar



**Swap-in (On-Chain → Blixt)**: Konvertera On-Chain BTC till Lightning satoshis. Användningsfall: driva en mobil Wallet Lightning, få inkommande kapacitet på en nod eller ha omedelbar likviditet.



**Byt ut (Lightning → On-Chain)**: Konvertera Lightning satoshis till On-Chain BTC. Användningsfall: dumpa Wallet Lightning till Cold-lagring eller ombalansera likviditeten mellan lager.



### Säkerhet och återhämtning



**Trustless Atomic Swaps: HTLC garanterar att antingen Exchange fullföljs i sin helhet eller att varje part får tillbaka sin insats. Motpartsrisken är matematiskt eliminerad.



**Inlösenmekanism**: Varje swap har ett utgångsdatum (TIMELOCK). Om swappen misslyckas återbetalas pengarna automatiskt efter utgången. Användaren behåller alltid möjligheten att återkräva sina bitcoins.



** Återställningsnycklar **: SwapMarket låter dig exportera återställningsnycklar för pågående byten. I händelse av ett problem, kan dessa nycklar användas för att slutföra eller avbryta ett byte från någon enhet.



## Installation och åtkomst



### Interface webb



SwapMarket kräver ingen installation. Åtkomst sker via webbläsare genom att besöka https://swapmarket.github.io. För maximal sekretess, använd Brave, Firefox med tillägg för antispårning eller LibreWolf. Tor Browser rekommenderas för nätverksanonymitet.



Ingen registrering, e-post eller identitetsverifiering krävs.



### Självhanterande (valfritt)



För tekniska användare som vill eliminera beroendet av den officiella domänen GitHub Pages kan SwapMarket köras lokalt :



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**via Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Applikationen kommer att vara tillgänglig på `http://localhost:3000`. Självhosting garanterar total kontroll över Interface, eliminerar risken för censur av den officiella domänen och gör det möjligt att granska källkoden innan den körs.



### Inledande konfiguration



**Wallet Blixten**: Se till att du har en fungerande Wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). För inbyten kommer du att generate en Lightning Invoice. För utväxling betalar du en Lightning Invoice.



**Wallet On-Chain**: För swap-ins behöver du en Wallet Bitcoin On-Chain för att skicka pengar. För utväxling, förbered en Bitcoin som tar emot Address.



**Möjlighet till valfri konfiguration**: SwapMarket lagrar swap historia och preferenser i webbläsarens cookies. Inget konto skapande krävs.



## Tillgång till inställningar och Rescue Key



Innan du gör dina första byten rekommenderar vi starkt att du laddar ner din **Rescue Key**. Med den här nödnyckeln kan du få tillbaka dina pengar om det uppstår ett tekniskt problem eller om du förlorar åtkomsten till din enhet.



### Parametrar för åtkomst



På SwapMarkets huvudsida klickar du på kugghjulsikonen (⚙️) längst upp till höger på Interface, bredvid bytesformuläret.



![Accès aux paramètres](assets/fr/01.webp)



### Sidinställningar



Sidan Settings (Inställningar) öppnas och visar flera konfigurationsalternativ:





- Valör**: Val mellan BTC eller Sats
- Decimalavgränsare**: Decimalavgränsare (, eller .)
- Ljud- och webbläsarmeddelanden**: Ljud- och webbläsarmeddelanden
- Räddningsnyckel** : Ladda ner återställningsnyckeln
- Loggar**: Visa, ladda ner eller radera loggar



![Page Settings](assets/fr/02.webp)



### Ladda ner Rescue Key



Klicka på knappen **Download** bredvid "Rescue Key".



**Viktiga punkter** :




- Rescue Key är en **one-stop emergency key** som fungerar för alla dina framtida swappar
- Förvara denna nyckel på en **säker och permanent** plats (lösenordshanterare, digitalt kassaskåp)
- I händelse av ett swap-problem (timeout, tekniskt fel) kan du med hjälp av denna nyckel återfå dina pengar



## Skapa en swap steg för steg



### Byt ut: Blixt → Bitcoin



Det här första exemplet visar hur man konverterar Lightning satoshis till On-Chain bitcoins.



**Steg 1: Byt konfiguration



Välj swapformuläret på huvudsidan :




- LIGHTNING** (övre fältet): Ange det belopp du vill skicka i Sats Lightning (exempel: 30.000 Sats)
- Bitcoin** (nedre fältet): Det belopp du kommer att få visas automatiskt efter att avgifterna har dragits av (exempel: Sats 29 320)



I det nedre fältet klistrar du in din **mottagande Bitcoin Address** där du vill ta emot pengarna. Kontrollera denna Address noggrant.



Standardleverantören är vanligtvis Boltz Exchange. Nätverksavgifter och leverantörsavgifter visas tydligt.



![Configuration swap-out](assets/fr/03.webp)



**Steg 2: Val av leverantör**



Klicka på rullgardinsmenyn för leverantör (standard: "Boltz Exchange") för att visa alla tillgängliga likviditetsleverantörer.



Ett modalt fönster öppnas och visar en jämförelsetabell:




- Status**: Green-indikator om leverantören är aktiv
- Alias**: Leverantörens namn (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Avgift**: Avgifter som tas ut av leverantören (i allmänhet mellan 0,49% och 0,5%)
- Max Swap**: Högsta belopp som accepteras för en swap



Jämför avgifter och maxbelopp och välj sedan den leverantör som passar dig bäst.



**Vänligen notera**: I Interface för val av leverantör visas inte **minimibeloppen** för varje leverantör. Denna information visas endast i Interface för skapande av swap efter att en leverantör har valts. Minimi- och maximibelopp kan variera från leverantör till leverantör och kan ändras över tid. **Kontrollera alltid dessa gränser vid tidpunkten för din swap**: om det belopp du vill swappa ligger utanför en leverantörs gränser kan du välja en annan leverantör som är mer lämplig för din transaktion.



![Sélection du provider](assets/fr/04.webp)



**Steg 3: Skapande av swap och betalning med blixt**



Klicka på den gula **"CREATE ATOMIC SWAP"**-knappen. SwapMarket kommer att generate en **Lightning Invoice** (BOLT11) för dig att betala från din Wallet Lightning.



Sidan visar :




- Swap-ID**: Unik identifierare för swap (exempel: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap skapad, inväntar betalning)
- QR-kod**: Skanna den med din Wallet Lightning
- Invoice Lightning**: Teckensträng som börjar med "lnbc" (exempel: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Betala denna Invoice från din Wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). Det exakta beloppet som ska betalas visas (exempel: 30 000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Steg 4: Bekräftelse och godkännande**



När Lightning-betalningen har bekräftats tar SwapMarket omedelbart emot din betalning och leverantören sänder Bitcoin-transaktionen till din Address.



Statusen ändras till **"Invoice.settled"** (Invoice betald) och ett bekräftelsemeddelande visas.



Dina On-Chain bitcoins kommer att vara tillgängliga så snart transaktionen har bekräftats (vanligtvis inom några minuter till några timmar, beroende på de Mining avgifter som leverantören väljer).



![Confirmation swap-out](assets/fr/06.webp)



Du kan klicka på **"OPEN CLAIM TRANSACTION"** för att se Bitcoin-transaktionen på en Blockchain explorer.



### Byt in: Bitcoin → Blixt



Det här andra exemplet visar hur man konverterar On-Chain bitcoins till Lightning satoshis.



**Steg 1: Byt konfiguration



Välj swapformuläret på huvudsidan :




- Bitcoin** (övre fältet): Ange det belopp som du vill skicka i Sats Bitcoin (exempel: 63 400 Sats)
- LIGHTNING** (nedre fältet): Det belopp som du kommer att få visas automatiskt efter avdrag för avgifter (exempel: 62 884 Sats)



I det nedre fältet klistrar du in en Lightning** Invoice (BOLT11) som genererats från din Wallet Lightning, eller använder din LNURL Address om din Wallet stöder det.



![Configuration swap-in](assets/fr/07.webp)



**Steg 2: Rädda nyckelkontroll**



När du har klickat på **"CREATE ATOMIC SWAP"** visas ett modalt fönster där du ombeds att verifiera din Rescue Key.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz räddningsnyckel**: Eftersom du redan har laddat upp din återställningsnyckel under den första konfigurationen (se föregående avsnitt) klickar du på knappen **"VERIFY EXISTING KEY"** för att importera den nyckel du har sparat.



Välj den tidigare nedladdade Rescue Key-filen. Efter en lyckad verifiering går Interface automatiskt vidare till nästa steg.



**Steg 3: Bitcoin** deponering Address



SwapMarket genererar nu en **unik Bitcoin Address** som innehåller HTLC Contract kopplad till din Lightning Invoice.



Sidan visar :




- Bytes-ID**: Unik identifierare (exempel: 1kGmB6JyGqU4)
- Status** : "Invoice.set" (Invoice inställd, inväntar betalning Bitcoin)
- QR-kod**: Bitcoin depå Address
- Bitcoin** Address: Börjar vanligen med "bc1p..." (exempel: bc1p5mvtwxapjkds...9d4n9f)
- Varning i gult** : "Se till att din transaktion bekräftas inom ~24 timmar efter skapandet av denna swap!"



Denna period på ~24 timmar är **timeout** för HTLC Contract. Om din Bitcoin-transaktion inte bekräftas inom denna tidsram kommer bytet att misslyckas och du måste använda din Rescue Key för att få tillbaka dina pengar.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Du kan kopiera Address genom att klicka på knappen **"Address"**, eller skanna QR-koden direkt från din Wallet On-Chain.



**Steg 4: Skicka bitcoins**



Från din Wallet Bitcoin On-Chain, skicka **exakt** det belopp som anges (t.ex. 63 400 Sats) till den Address som genererats.



**Viktigt**: Använd lämpliga Mining-avgifter för att garantera snabb bekräftelse. Om avgiften är för låg och transaktionen ligger kvar i Mempool efter tidsgränsen (~24h) kommer bytet att misslyckas.



När transaktionen har skickats upptäcker SwapMarket att den är i Mempool och visar :




- Status** : "transaktion.Mempool"
- Meddelande**: "Transaktionen är i Mempool - Väntar på bekräftelse för att slutföra swappen"



![Transaction en mempool](assets/fr/10.webp)



**Steg 5: Bekräftelse och mottagning med blixt**



Så snart Bitcoin-transaktionen får sin första bekräftelse betalar leverantören automatiskt din Lightning Invoice. Du får omedelbart satoshis på din Wallet Lightning.



Statusen ändras till **"transaction.claim.pending"**, och ett bekräftelsemeddelande visas:



![Confirmation swap-in](assets/fr/11.webp)



Dina Lightning satoshis finns omedelbart tillgängliga i din Wallet.



## Fördelar och begränsningar



### Fördelar



**Rate competition**: Sammanslagningen av leverantörer skapar en naturlig konkurrens som drar ner avgifterna (0,49% till 0,5%).



**Konfidentialitet**: Ingen KYC, Interface 100% på klientsidan (ingen överföring av personuppgifter), kompatibel med Tor Browser.



** Inte vårdnadshavare**: HTLC garanterar matematiskt exklusiv kontroll över dina medel. Antingen lyckas swappen eller så får du tillbaka dina bitcoins.



**Open source self-hostable**: granskningsbar offentlig kod som kan distribueras lokalt för maximalt motstånd mot censur.



### Begränsningar



**Begränsad likviditet**: Begränsat antal aktiva leverantörer (Boltz, Eldamar, MiddleWay beroende på period). Maximala belopp kan vara begränsade.



**Utgångstid**: Timeout från 24h till 48h. Om On-Chain-transaktionen inte bekräftas före utgången krävs manuell återställning.



**Interface centralisering**: Även om den kan hostas själv, hostas den officiella Interface på GitHub Pages. Om GitHub censurerar repot kommer åtkomst via swapmarket.github.io att blockeras (lösning: självhosting).



**On-Chain spår**: HTLC-skript är potentiellt identifierbara genom avancerad Blockchain-analys.



## Bästa praxis



### Säker konfiguration



**Ladda ner din räddningsnyckel**: Innan du gör dina första swappar ska du ladda ner din räddningsnyckel från Inställningar (se avsnittet ovan). Denna unika nyckel kommer att fungera för alla dina framtida swappar, så att du kan få tillbaka dina pengar om det skulle uppstå problem.



**Använd Tor Browser**: För maximal sekretess, få tillgång till SwapMarket via Tor Browser för att dölja din IP Address.



** Överväg självhosting **: För tekniska användare, kör din egen SwapMarket instans eliminerar beroendet av den officiella GitHub Pages domän.



### Optimering av byten



**Håll ett öga på Mempool**: Kontrollera Mempool.space före en swap-in. Välj tider med låg aktivitet för att minimera Mining-kostnaderna.



**Kontrollera adresser**: För utväxling, kontrollera noggrant din mottagande Address. Använd kopiera och klistra in och kontrollera de första 5 och de sista 5 tecknen.



**Testa med små mängder**: Börja med den minsta tillåtna mängden (25 000 till 50 000 Sats). Öka gradvis när du behärskar processen.



**Dokumentera dina swappar**: Anteckna varje swaps ID, inlösen Address och utgångsdatum. Denna information underlättar spårning och återställning i händelse av ett tekniskt problem.



### Strategi för användning



**Balansera ditt kassaflöde**: Använd SwapMarket för att justera din fördelning mellan On-Chain (sparande, långsiktig säkerhet) och Lightning (dagliga utgifter, omedelbara betalningar) enligt dina verkliga behov.



** Beräkna lönsamhet**: För permanenta Lightning-likviditetsbehov, jämför den kumulativa kostnaden för upprepade swappar jämfört med att öppna en Lightning-kanal direkt. SwapMarket utmärker sig för engångsjusteringar, inte nödvändigtvis för stora regelbundna flöden.



## SwapMarket vs Boltz: Vad är skillnaden?



### Boltz: Teknik kontra service



**Boltz är en teknik med öppen källkod** (`boltz-backend` på GitHub) som implementerar atomära byten via HTLC mellan Bitcoin, Lightning och Liquid.



**Kritisk punkt**: Alla SwapMarket-leverantörer (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) distribuerar sin egen instans av Boltz backend. Den underliggande tekniken är därför identisk. En sårbarhet i Boltz backend skulle potentiellt påverka alla leverantörer, men systemets öppna källkod möjliggör granskning av samhället.



**Boltz Exchange** är en enskild tjänst som drivs av Boltz-teamet, medan **SwapMarket** samlar flera leverantörer som alla använder Boltz-teknik, vilket skapar en konkurrenskraftig prissättningsmiljö.



Se våra handledningar för Boltz och Zeus Swap för mer information:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Viktiga skillnader



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarket fördelar**: Priskonkurrens, diversifiering av backend-instanser, jämförelse i realtid.



**Tekniska alternativ** (inte kompatibla med SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Dessa lösningar använder sina egna implementeringar av undervattensbyten.



**Rekommendation**: Använd Boltz Exchange för enkelhetens skull eller SwapMarket för att optimera kostnaderna genom konkurrens. Båda är likvärdiga i fråga om säkerhet (HTLC är inte frihetsberövande).



## Slutsats



SwapMarket underlättar Bitcoin/Lightning-utbyten genom att samla flera leverantörer till en enda Interface. HTLC-arkitekturen garanterar swapparnas icke-frihetsberövande karaktär, avsaknaden av KYC bevarar konfidentialiteten och den självhanterliga koden med öppen källkod förstärker motståndet mot censur.



Konkurrens mellan leverantörer förbättrar priserna och multiplicerar likviditetskällor. För att optimera två-Layer-hanteringen (On-Chain-besparingar, Lightning-kostnader) är SwapMarket ett praktiskt verktyg som bevarar finansiell suveränitet och sekretess.



## Resurser



### Officiell dokumentation




- [SwapMarket - Webbapplikation] (https://swapmarket.github.io)
- [GitHub SwapMarket] (https://github.com/SwapMarket/swapmarket.github.io)
- [Teknisk dokumentation] (https://docs.boltz.Exchange/)
- [Guide för självhosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Relaterade projekt




- [Boltz Exchange](https://boltz.Exchange) - Original atombytesservice
- [ZEUS Swaps](https://zeusln.com) - Leverantör av Lightning Swaps