---
name: Blixt

description: Mobil LN Nod Wallet
---

![presentation](assets/blixt_intro_en.webp)


## En kraftfull BTC/Lightning-nod i fickan, var du än befinner dig


Jag skulle vilja presentera en intressant och kraftfull ny BTC/LN mobilnod och Wallet - Blixt. Namnet kommer från svenska och betyder "blixt".

Om du aldrig använt Bitcoin Lightning Network, innan du börjar, läs [denna enkla förklaringsanalogi om Lightning Network (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).


## VIKTIGA ASPEKTER:


### 1. Blixt är en privat nod, INTE en routningsnod! Ha detta i åtanke.


Det betyder att alla LN-kanaler i Blixt kommer att vara oannonserade för LN-grafen (så kallade privata kanaler). Det betyder att DENNA NODE INTE kommer att göra routing av andra betalningar genom Blixt-noden. [Läs mer om privata och offentliga kanaler här](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).


Blixt mobilnod är INTE för routing, jag upprepar. Det är främst för att kunna hantera dina egna LN-kanaler och göra dina LN-betalningar privat, när du behöver.


Blixt mobilnod måste vara online och synkroniserad ENDAST INNAN du ska göra dina transaktioner. Det är därför du kommer att se en ikon på toppen som indikerar synkroniseringsstatusen. Det tar bara några ögonblick, beroende på hur lång tid du har hållit den offline och synkroniserar LN-grafen igen.


### 2. Blixt använder LND (aezeed) som Wallet backend, så försök inte att importera andra typer av Bitcoin plånböcker till den.


[Här har du förklarat typerna av plånböcker](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Så om du tidigare hade en LND-nod kan du importera seed och backup.channels till Blixt, [som det förklaras i den här guiden](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).


### 3. Blixt viktiga länkar (vänligen bokmärk dem):



- [Blixt Github repository](https://github.com/hsjoberg/blixt-Wallet) | [Github Releases](https://github.com/hsjoberg/blixt-Wallet/releases) (ladda ner apk-filen direkt)
- [Blixt Features page](https://blixtwallet.github.io/features) - förklarar en efter en varje egenskap och funktionalitet.
- [Blixt FAQ-sida](https://blixtwallet.github.io/faq) - Lista över frågor och svar och felsökning av Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demos, videohandledning, extra guider och användningsfall för Blixt
- [A4-flyer för utskrift] (https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) med de första stegen i användningen av Blixt, på olika språk.
- Blixt erbjuder också en fullt fungerande demo direkt på [dess webbplats](https://blixtwallet.com) eller på en dedikerad [webbversion](https://blixt-Wallet-git-master-hsjoberg.vercel.app/), för att få en fullständig erfarenhetstestning innan du börjar använda Blixt i den verkliga världen.
- [Geyser crowdfunding-sida] (https://geyser.fund/project/blixt) - donera Sats som du vill för att stödja projektet
- [Telegram supportgrupp] (https://t.me/blixtwallet)


# Viktiga funktioner tillgängliga


## Neutrino-nod


Blixt ansluter som standard till Blixts server för att synkronisera block och index med Neutrino (SPV-läge för Simplified Payment Verification), men användaren kan också ansluta till sin egen nod. Det är förvånande att se att synkronisering av en SPV-nod tar mindre än 5 minuter, i mitt fall på Android 11, för att vara redo att använda Full node Wallet (On-Chain och LN).


## Komplett nod för icke-vårdnadshavare


Användaren kan hantera sina egna kanaler med en lättanvänd Interface och med tillräckligt med information för att få en bra upplevelse. I den övre vänstra lådmenyn kan du gå till Lightning-kanalerna för att börja öppna med andra noder, som du vill. Glöm inte att aktivera Tor i inställningarna. Det är mycket bättre för integriteten och även för att som en mobil nod, om du ändrar din internetanslutning / clearnet IP ofta, kan dina kamrater störas. Med Tor-nodens URI kommer du alltid att ha samma privata identifierare oavsett din plats / IP.


## Säkerhetskopiera/återskapa en LND-nod


En kraftfull, lätthanterlig och användbar funktion är att återställa andra döda LND-noder, med bara 24-ordslistan seed och filen channels.backup. [Här är en guide om hur man återställer döda Umbrel-noder i Blixt i händelse av SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)


Användaren har också möjlighet att spara Blixt-kanalens säkerhetskopia på Google Drive och/eller lokalt lagringsutrymme på sin egen mobila enhet (för att senare flytta den till en säker plats, bort från telefonen).


Återställningsprocessen är ganska enkel: sätt in 24-word seed, lägg till säkerhetskopian (tidigare kopierad till mobilminnet) och klicka på återställning. Det kommer att ta lite tid att synkronisera och skanna alla block för dina tidigare transaktioner. Kanalerna stängs automatiskt och pengarna återförs till din On-Chain Wallet (se menyn längst upp till vänster i lådan - On-Chain).


**Note** Om du tidigare hade öppna kanaler med din gamla nod bakom Tor måste du först aktivera Tor-alternativet (och starta om programmet) från menyinställningarna. På så sätt kommer stängningen inte att misslyckas och/eller alternativet för tvingad stängning kommer inte att användas.


Kom ihåg att säkerhetskopiera dina LN-kanaler efter att du har öppnat och/eller stängt kanaler. Det tar bara några sekunder att vara säker. Senare kan du flytta säkerhetskopian till en säker plats borta från din mobila enhet.

För att testa din seed i ett restaureringsscenario, innan du lägger till pengar, använder du helt enkelt samma 24-ords seed (aezeed) i BlueWallet. Om den genererade BTC Address är densamma i Blixt är du redo att köra. Du behöver inte använda BlueWallet efter det, du kan helt enkelt ta bort den testade Wallet för restaurering.


## Inbyggd Tor


När du har aktiverat den kommer applikationen att starta om bakom Tor-nätverket. Från och med nu kan du i menyinställningarna se ditt nod-ID med en lök Address, så att andra noder kan öppna kanaler till din lilla Blixt-mobilnod. Eller låt oss säga att du har din egen nod hemma och vill ha små kanaler med din Blixt-mobilnod. En perfekt kombination.


## Dunder LSP - Liquidity Service Provider (leverantör av likviditetstjänster)


En enkel och fantastisk funktion som erbjuder nya användare möjligheten att börja acceptera BTC på Lightning Network omedelbart, utan att behöva sätta in pengar On-Chain och sedan öppna LN-kanaler.


För nya användare är detta goda nyheter eftersom de ska kunna börja från början, direkt på LN. För att göra detta skapar du helt enkelt en LN Invoice från huvudskärmen på "ta emot" -knappen, anger belopp, beskrivning etc. och betalar från en annan Wallet. Blixt kommer att öppna en kanal på upp till 400k Sats per mottagen transaktion. Du kan öppna flera kanaler om det behövs.


Ett intressant och användbart fall är följande: låt oss säga att ditt första mottagna belopp är 200k. Blixt kommer att öppna en 400k Sats-kanal med redan 200k (minus öppningsavgifter) på din sida, men eftersom du fortfarande har 200k "utrymme" tillgängligt kan du få mer. Så nästa betalning, låt oss säga 100k, kommer att anlända direkt via denna kanal, utan ytterligare avgifter, och du har fortfarande 100k utrymme att ta emot mer.


Men om du väljer att ta emot, låt oss säga, 300k för den tredje betalningen, kommer det att skapa en annan ny 400k-kanal och skjuta dessa 300k till din sida.


Om det finns för många förfrågningar kan Blixt-noden justera kanalens kapacitet under öppningen.


## Automatisk kanalöppning


I inställningarna kan användaren aktivera det här alternativet och få en automatiserad tjänst som öppnar kanaler med de bästa noderna och rutterna baserat på det tillgängliga saldot i On-Chain Wallet i Blixt-applikationen. Detta är en fördelaktig funktion för nya användare som inte är säkra på vilken nod de ska öppna en kanal med och/eller hur de ska öppna en LN-kanal. Det är som en autopilot för LN.


** Kom ihåg:** detta alternativ används endast en gång, när du skapar din nya Blixt Wallet, och är aktiverat som standard. Så om den nya användaren skannar On-Chain QR-koden på huvudskärmen och sätter in sin första Sats till den Address, kommer Blixt automatiskt att öppna en kanal med dessa Sats, med Blixt offentliga nod.


## Tjänster för inkommande likviditet


Funktion tillägnad handlare som behöver mer inkommande likviditet, enkel att använda. För att göra detta väljer du helt enkelt en av likviditetsleverantörerna från listan, betalar det belopp du vill ha för kanalen och anger ditt nod-ID, och därifrån öppnas en kanal till din Blixt-nod.


## Kontaktlistor


Användbar funktion om du vill ha en hållbar lista över mottagare som du handlar med för det mesta. Denna lista kan bestå av LNURL:er, Lightning-adresser eller framtida statisk betalningsinformation/fakturor. För närvarande kan denna lista inte sparas utanför applikationen, men det finns planer på att ha ett alternativ för att exportera den.


## LNURL och blixt Address


Fullt stöd för LNURL. Du kan betala till LNURL, LN-auth, LN-chan begäran med LNURL.

Du kan skicka till vilken LN Address som helst och även lägga till den i din kontaktlista.

Från och med vers. 0.6.9 är det möjligt att ta emot till din egen LN Address _@blixtwallet.com_ typ, genom [Blixt Lightning Box] (https://github.com/hsjoberg/lightning-box) -funktionen.


## Keysend


En mycket kraftfull funktion som få mobila plånböcker har. Du kan skicka pengar direkt genom en kanal eller peka på en annan nod och lägga till ett meddelande om det behövs. Det är som en hemlig chatt över LN. Denna funktion är mycket användbar för att visa meddelanden på Amboss.space-affischtavlan ([här är en guide om denna Amboss-affischtavla](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).


## Signering av meddelande


Mycket användbart verktyg för att signera meddelanden med din Blixt-nods privata nyckel, autentiseringsmeddelanden och så vidare. Mycket få mobila plånböcker har den här funktionen, nästan ingen.


## Betalningar i flera kanaler - Multi-Path Payments (MPP)


Användbar funktion för LN-betalningar, så att du kan dela upp en LN-betalning i flera delar, över flera kanaler. Det är ett bra sätt att balansera likviditeten i nätverket och förbättra integriteten.


## Blixtsnabb webbläsare


En serie tjänster från tredje part med LN, organiserade i en enkel, tillgänglig och användarvänlig webbläsare. Det är också ett bra sätt att marknadsföra företag som accepterar BTC på LN. Detta är en funktion som kommer att vidareutvecklas i framtiden. För närvarande fungerar det inte bakom Tor, så att surfa på dessa applikationer kommer att vara i klart (clearnet).


## Utforskare av timmerstockar


Detta är ett kraftfullt verktyg för att kontrollera LND-loggar och statusen för din nod i allmänhet. Det finns ett alternativ för att spara loggfilen. Det är mycket användbart att ha dessa loggar till hands om du behöver hjälp av en utvecklare med att identifiera vissa problem.


## Säkerhet


För att öka säkerheten för din Wallet/nod kan du i programinställningarna ange möjligheten att starta programmet med en PIN-kod och/eller ett fingeravtryck.


## On-Chain Wallet


Denna funktion är lite dold, i lådmenyn längst upp till vänster. Eftersom den inte används ofta av en LN-användare är den inte synlig på huvudskärmen. Men det är okej, du kan ha den på en separat Wallet där du kan hantera adresser och se transaktionsloggen, genom att importera din seed på Sparrow till exempel. Kanske i framtiden kommer Blixt Wallet också att innehålla en funktion för att hantera UTxOs. Men för tillfället använder du ENDAST denna On-Chain Wallet för att öppna eller stänga kanaler på LN.


## Specialfunktioner



- Med vers. 0.6.9 introducerades "persistent mode" som gör det möjligt för användaren att köra Blixt som en LN-nod som alltid är online, vilket håller LND-tjänsterna vid liv och LN Wallet redo att ta emot/sända när som helst.
- Enkla Taproot-kanaler - gör det möjligt att öppna Taproot-kanaler för mer integritet och avancerade funktioner
- Nollbekräftelsekanaler med Blixt Dunder LSP
- Speedloader ("LN channel sync") - Detta innebär att alla kanaler kommer att synkroniseras snabbt vid start, för bättre vägval. Även om det är lite irriterande att du måste se synkroniseringsskärmen i början, kommer det att säkerställa att Wallet känner till alla kanaler och betalningarna blir snabbare och mer tillförlitliga.
- Översatt till 25+ språk!


## "Påskägg"


Ja, i Blixt-applikationen finns det några dolda funktioner, små saker som gör applikationen charmig och aktiverar roliga/intressanta åtgärder och svar.

Tips: försök klicka två gånger på Blixt-logotypen i lådan 🙂 Jag ska låta dig upptäcka resten.


# Blixt Kom igång Steg-för-steg-guide


**Tips:** som ny LN-användare, om du börjar använda Blixt LN Node, måste du först veta vad Lightning Network är och hur det fungerar, åtminstone på grundläggande nivå. [Här har vi sammanställt en enkel lista med resurser om Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Vänligen läs dem först.


Att köra en fullständig LN-nod på en mobil enhet är inte en lätt uppgift och kan ta en del utrymme (min 600 MB) och minne. Vi rekommenderar att du har en bra mobil enhet som är uppdaterad och använder minst Android 11 som operativsystem.


När du öppnar Blixt kommer skärmen "Välkommen" att ge dig några alternativ:


![Demo Blixt 01](assets/blixt_t01.webp)


I det övre högra hörnet ser du 3 prickar som aktiverar en meny med:



- "enable Tor" - användaren kan börja med Tor-nätverket, speciellt om man vill återställa en gammal LND-nod som kördes med Tor-peers.
- "Ställ in Bitcoin-nod" - om användaren vill ansluta till sin egen nod direkt, för att synkronisera blocken via Neutrino, kan göra det direkt från välkomstskärmen. Det här alternativet är också bra om din internetanslutning eller Tor inte är så stabil att du kan ansluta till standard Bitcoin-noden (node.blixtwallet.com).


## Första steget - Skapa en ny Wallet


Om du väljer att "skapa en ny Wallet" kommer du att omdirigeras direkt till huvudskärmen för Blixt Wallet.


Detta är din "cockpit" och även "Main LN Wallet", så var medveten om att den endast visar balansen i din LN Wallet. Wallet i kedjan visas separat (se C).


![Demo Blixt 02](assets/blixt_t02.webp)


A - Blixt blockerar ikonen för synkroniseringsindikator. Detta är det viktigaste för en LN nod: att vara synkroniserad med nätverket. Om den ikonen fortfarande fungerar betyder det att din nod INTE ÄR KLAR! Så ha tålamod, speciellt för den första initiala synkroniseringen. Det kan ta upp till 6-8 minuter, beroende på din enhet och internetanslutning.


Du kan klicka på den och se status för synkroniseringen:


![Demo Blixt 03](assets/blixt_t03.webp)


Du kan också klicka på knappen "Show LND Log" (A) om du vill se och läsa mer tekniska detaljer i LND-loggen i realtid. Är mycket användbart för felsökning och för att lära sig mer om hur LN fungerar.


B - Här kan du komma åt alla Blixt-inställningar, och det är många! Blixt erbjuder många rika funktioner och alternativ för att hantera din LN-nod som ett proffs. Alla dessa alternativ förklaras i detalj i ["Blixt Features Page - Options Menu"](https://blixtwallet.github.io/features#blixt-options).


C - Här har du menyn "Magic Drawer", som också förklaras i detalj här. Här finns "Onchain Wallet" (B), Lightning Channels (C), Contacts, Channels status icon (A), Keysend (D).


![Demo Blixt 04](assets/blixt_t04.webp)


D - Är hjälpmenyn, med länkar till FAQ / Guides-sidan, kontakta utvecklaren, Github-sidan och Telegram supportgrupp.


E - Ange din första BTC Address, där du kan sätta in din första testning Sats. DETTA ÄR VALFRITT! Om du sätter in direkt i den Address, öppnar en LN-kanal mot Blixt Node. Det betyder att du kommer att se din deponerade Sats, gå in i en annan onchain-transaktion (tx), för att öppna den LN-kanalen. Du kan kontrollera det i Blixt onchain Wallet (se punkt C) genom att klicka på TX-menyn längst upp till höger.


![Demo Blixt 05](assets/blixt_t05.webp)


Som du kan se i Onchain Transaction Log är stegen mycket detaljerade som anger vart Sats går (insättning, öppen, stängd kanal)


**Rekommendation:** efter att ha testat flera situationer kom vi till slutsatsen att det är mycket bättre effektivt att öppna kanaler mellan 1 och 5 M Sats. Mindre kanaler tenderar att tömmas snabbt och betala en högre % av avgifterna jämfört med större kanaler.


F - Ange ditt huvudsakliga Lightning Wallet-saldo. Detta är INTE ditt totala Blixt Wallet-saldo, det representerar endast de Sats du har i Blixtkanaler, tillgängliga för att skicka. Som tidigare angivits är Onchain Wallet separat. Tänk på denna aspekt. Onchain Wallet är separat av en viktig anledning: den används främst för att öppna / stänga LN-kanaler.


Ok så nu satte du in några Sats i den onchain Address som visas på huvudskärmen. Det rekommenderas att när du gör det, att hålla din Blixt-app online och aktiv ett tag tills BTC tx tas av gruvarbetarna i det första blocket.


Efter det kan det ta upp till 20-30 minuter tills det är helt bekräftat och kanalen är öppen och du kommer att se den i Magic Drawer - Lightning Channels som aktiv. Även den lilla färgade pricken på toppen av lådan, om det är Green, kommer att indikera att din LN-kanal är online och redo att användas för att skicka Sats över LN.


Address och det välkomstmeddelande som visas försvinner. Det är inte längre nödvändigt att öppna en automatisk kanal nu. Du kan också avaktivera alternativet i menyn Inställningar.


Det är dags att gå vidare och testa andra funktioner och alternativ för att öppna LN-kanaler.


Låt oss nu öppna en annan kanal med en annan node peer. Blixt community sätter ihop [en lista över bra noder att börja använda med Blixt.](https://github.com/hsjoberg/blixt-Wallet/issues/1033)


### Procedur för att öppna en normal oannonserad (privat) LN-kanal i din Blixt mobilnod


Detta är mycket enkelt, det krävs bara några få steg och lite tålamod:



- Gå till [Blixt Community list](https://github.com/hsjoberg/blixt-Wallet/issues/1033) med bra kollegor
- Välj en nod och klicka på länken i dess namntitel, så öppnas dess Amboss-sida
- Klicka för att visa QR-koden för noden URI Address


![Demo Blixt 06](assets/blixt_t06.webp)


Öppna nu Blixt och gå till den övre lådan - Lightning Channels och klicka på "+" -knappen


![Demo Blixt 07](assets/blixt_t07.webp)


Klicka nu på (A)-kameran för att skanna QR-koden från Amboss-sidan och nodinformationen kommer att fyllas i. Lägg till beloppet för Sats för den kanal du vill ha och välj sedan avgiftssatsen för tx. Du kan låta den vara automatisk (B) för en snabbare bekräftelse eller justera den manuellt genom att skjuta på knappen. Du kan också trycka länge på numret och redigera det som du vill.


Lägg inte mindre än 1 sat/vbyte ! Vanligtvis är det bättre att [konsultera Mempool-avgifterna] (https://Mempool.space/) innan du öppnar en kanal och väljer en lämplig avgift.


Klar, klicka nu bara på knappen "öppen kanal" och vänta på 3 bekräftelser, det tar vanligtvis 30 minuter (1 block aprox var 10: e minut).


När det är bekräftat kommer du att se kanalen aktiv i ditt avsnitt "Lightning Channels".


## Andra steget - skaffa mer inkommande likviditet


Ok, så nu har vi en LN-kanal med endast OUTBOUND-likviditet. Det betyder att vi bara kan SÄNDA, vi kan fortfarande inte MOTTA Sats över LN. Varför inte? Läste du de guider som anges i början? Har ni inte? Gå tillbaka och läs dem. Det är mycket viktigt att förstå hur LN-kanalerna fungerar.


![Demo Blixt 08](assets/blixt_t08.webp)


Som du kan se i det här exemplet har kanalen som öppnas med den första insättningen inte för mycket INBOUND-likviditet ("Kan ta emot") men har mycket OUTBOUND-likviditet ("Kan skicka").


Så vilka alternativ har du, om du vill få mer Sats över LN?



- Spendera lite Sats från befintlig kanal. Ja, LN är ett betalningsnätverk för Bitcoin, som huvudsakligen används för att spendera din Sats snabbare, billigare, privat och enkelt. LN är INTE ett hodlingssätt, för det har du onchain Wallet.
- Byt ut några Sats, tillbaka till din onchain Wallet, med hjälp av en submarin bytestjänst. På detta sätt spenderar du inte din Sats, utan ger den tillbaka till din egen onchain Wallet. Här kan du se några metoder i detalj, på [Blixt Guides Page](https://blixtwallet.github.io/guides).
- Öppna en INBOUND-kanal från vilken LSP-leverantör som helst. Här är en videodemo om [hur man använder LNBig LSP för att öppna en inkommande kanal] (https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). Det innebär att du betalar en liten avgift för en TOM kanal (på din sida) och att du kommer att kunna ta emot mer Sats till den kanalen. Om du är en handlare som tar emot mer än spenderar är det ett bra alternativ. Även om du köper Sats över LN, använder Robosats eller någon annan LN Exchange.
- Öppna en Dunder-kanal, med Blixt-nod eller någon annan Dunder LSP-leverantör. En Dunder-kanal är ett enkelt sätt att få lite INBOUND-likviditet, men samtidigt sätter du in lite Sats i den kanalen. Det är också bra eftersom det kommer att öppna kanalen med en [UTXO] (https://en.Bitcoin.it/wiki/UTXO) som inte är från din Blixt Wallet. Det lägger till lite integritet.

Är också bra eftersom, om du inte har Sats i en onchain Wallet, för att öppna en normal LN-kanal, men du har dem i en annan LN Wallet, kan du bara betala från den andra Wallet genom LN öppningen och insättningen (på din sida) av den Dunder-kanalen. [Mer detaljer om hur Dunder fungerar och hur du driver din egen server här.](https://github.com/hsjoberg/dunder-lsp)


![Demo Blixt 09](assets/blixt_t09.webp)


Här följer stegen för hur du aktiverar öppning av en Dunder-kanal:



- Gå till Inställningar, i avsnittet "Experiment" aktivera rutan för "Aktivera Dunder LSP".
- När du gjort det, gå tillbaka upp till "Lightning Network" sektionen och du kommer att se att det dykt upp alternativet "Set Dunder LSP Server". Där är som standard inställt "https://dunder.blixtwallet.com" men du kan ändra det med någon annan Dunder LSP-leverantör Address. [Här är en Blixt community list](https://github.com/hsjoberg/blixt-Wallet/issues/1033) med noder som kan tillhandahålla Dudner LSP-kanaler för din Blixt.
- Nu kan du gå till huvudskärmen och klicka på "Receive" -knappen. Följ sedan den här proceduren som förklaras [i den här guiden] (https://blixtwallet.github.io/guides#guide-lsp).


Ok, så efter att Dunder-kanalen har bekräftats (tar några minuter) kommer du att ha 2 LN-kanaler: en öppnad initialt med autopilot (kanal A) och en med mer inkommande likviditet, öppnad med Dunder (kanal B).


![Demo Blixt 10](assets/blixt_t10.webp)


Bra, nu är du redo att skicka och ta emot tillräckligt med Sats över LN!


## Tredje steget - Procedur för återställning av noden


Så låt oss nu diskutera hur man återställer en Blixt Wallet eller någon annan LND kraschad nod. Det här är lite mer tekniskt, men var uppmärksam. Är inte det Hard.


** Påminnelse:** tidigare skrev jag en dedikerad guide med flera alternativ [hur man återställer en kraschad LND-nod](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), där jag också nämnde metoden att använda Blixt som snabb återställningsprocess, med hjälp av seed + channel.backup-filen från din döda LND-nod. Jag skrev också en guide för hur du återställer din Blixt-nod eller migrerar din Blixt till en annan enhet, [här](https://blixtwallet.github.io/faq#blixt-restore).


![Demo Blixt 11](assets/blixt_t11.webp)


Men låt oss förklara i enkla steg denna process. Som du kan se i bilden ovan finns det två saker du bör göra för att återställa din tidigare Blixt/LND-nod:



- övre rutan är där du måste fylla i alla 24 ord från din seed (gammal/död nod)
- längst ner finns två knappalternativ för att infoga / ladda upp filen channel.backup, som tidigare sparats från din gamla Blixt/LND-nod. Det kan vara från en lokal fil (du laddar upp den till din enhet tidigare) eller kan vara från en Google Drive / iCloud-fjärrplats. Blixt har det här alternativet för att spara säkerhetskopian av dina kanaler direkt till en Google / iCloud-enhet. Se mer information på [Blixt Features Page] (https://blixtwallet.github.io/features#blixt-options).


Ändå att nämna, om du tidigare inte hade några öppna LN-kanaler, finns det inget behov av att ladda upp någon channels.backup-fil. Sätt bara in de 24 orden seed och tryck på återställningsknappen.


Glöm inte att aktivera Tor, från den övre 3-punktsmenyn, som vi förklarade i kapitlet "Första steget" i den här guiden. Det är fallet när du ENDAST hade Tor-kollegor och inte kunde kontaktas via clearnet (domän / IP). Annars är det inte nödvändigt.


En annan användbar funktion är att ställa in en specifik Bitcoin-nod från den övre menyn. Som standard synkroniserar den block från node.blixtwallet.com (neutrino-läge) men du kan ställa in vilken annan Bitcoin-nod som helst som tillhandahåller neutrino-synkronisering.


Så när du har fyllt i dessa alternativ och tryckt på återställningsknappen kommer Blixt först att börja synkronisera blocken via Neutrino som vi förklarade i kapitlet "Första steget" i den här guiden. Så ha tålamod och titta på återställningsprocessen på huvudskärmen genom att klicka på synkroniseringsikonen.


![Demo Blixt 12](assets/blixt_t12.webp)


Som du kan se i det här exemplet visar det att Bitcoin-blocken är 100% synkroniserade (A) och att återställningsprocessen är i gång (B). Det betyder att LN-kanalerna som du hade tidigare kommer att stängas och pengarna återställas till din Blixt onchain Wallet.


Den här processen tar tid! Ha därför tålamod och försök att hålla din Blixt aktiv och online. Den första synkroniseringen kan ta upp till 6-8 minuter och stängningen av kanalerna kan ta upp till 10-15 minuter. Så det är bäst att du har enheten väl laddad.


När den här processen har startat kan du kontrollera i Magic Drawer - Lightning Channels, statusen för var och en av dina tidigare kanaler, som visar att de är i "väntan på att stänga" -status. När varje kanal är stängd kan du se den stängande tx i onchain Wallet (se Magic Drawer - Onchain) och öppna tx-menyloggen.


![Demo Blixt 13](assets/blixt_t13.webp)


Det kan också vara bra att kontrollera och lägga till om de inte finns där, dina tidigare peers som du hade i din gamla LN-nod. Så gå till menyn Inställningar, ner till "Lightning Network" och ange alternativet "Visa Lightning Peers".


![Demo Blixt 14](assets/blixt_t14.webp)


I avsnittet ser du de peers du är ansluten i det ögonblicket och du kan lägga till fler, bättre att lägga till de du hade kanaler tidigare. Gå bara till Amboss-sidan, sök efter dina peer-noder alias eller nodeID och skanna deras nod URI.


![Demo Blixt 15](assets/blixt_t15.webp)


Som du kan se i bilden ovan finns det 3 aspekter:


A - representerar clearnet-noden Address URI (domän/IP)


B - representerar Tor-löknoden Address URI (.onion)


C - är QR-koden som ska skannas med din Blixt-kamera eller kopieringsknappen.


Den här noden Address URI måste du lägga till i din peers-lista. Så var medveten om att det inte räcker med bara nodens aliasnamn eller nodeID.


Nu kan du gå till Magic Drawer (menyn längst upp till vänster) - Lightning Channels, och du kan se vid vilken löptidsblockhöjd pengarna kommer att återföras till din onchain Address.


![Demo Blixt 16](assets/blixt_t16.webp)


Det blocknummer 764272 är när medlen kommer att kunna användas i din Bitcoin onchain Address. Och det kan ta upp till 144 block från det 1: a bekräftelseblocket tills de släpps. Så kontrollera det i [Mempool] (https://Mempool.space/).


Och så är det med det. Vänta bara tålmodigt tills alla kanaler är stängda och pengarna tillbaka till din onchain Wallet.


## Fjärde steget - Anpassning


Det här kapitlet handlar om anpassning och om att lära känna Blixt Node bättre. Jag kommer inte att beskriva alla tillgängliga funktioner, de är för många och har redan förklarats på [Blixt Features Page] (https://blixtwallet.github.io/features).


Men jag kommer att peka på några av de nödvändiga för att gå vidare med att använda din Blixt och få en bra upplevelse.


### A - Namn (NamnBeskrivning)


![Demo Blixt 17](assets/blixt_t17.webp)


[The NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) är en standard för att förmedla "mottagarens namn" i BOLT11-fakturor.


Detta kan vara vilket namn som helst och kan ändras när som helst.


Detta alternativ är verkligen användbart i olika fall, när du vill skicka ett namn tillsammans med Invoice-beskrivningen, så att mottagaren kan få en ledtråd från vem som fick dessa Sats. Detta är helt valfritt och även på betalningsskärmen måste användaren kryssa i rutan för att ange att aliasnamnet ska skickas.


Här är ett exempel på hur det ser ut när du använder [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![Demo Blixt 18](assets/blixt_t18.webp)


Detta är ett annat exempel på att skicka till en annan Wallet-app som stöder NameDesc:


![Demo Blixt 19](assets/blixt_t19.webp)


### B - Backup LN-kanaler och seed-ord


Detta är en mycket viktig funktion!


När du har öppnat eller stängt en LN-kanal bör du göra en säkerhetskopia. Det kan göras manuellt genom att spara en liten fil på den lokala enheten (vanligtvis i nedladdningsmappen) eller genom att använda ett Google Drive- eller iCloud-konto.


![Demo Blixt 20](assets/blixt_t20.webp)


Gå till Blixt-inställningar - Wallet-avsnittet. Där har du möjlighet att spara alla viktiga data för din Blixt Wallet:



- "Visa Mnemonic" - kommer att visa de 24 orden seed för att skriva ner dem
- "Ta bort Mnemonic från enheten" - detta är valfritt och använd det endast om du verkligen vill ta bort seed-orden från din enhet. Detta kommer INTE att torka din Wallet, bara seed. Men var medveten om! Det finns inget sätt att återställa dem om du inte skrev ner dem först.
- "Export channel backup" - det här alternativet sparar en liten fil på din lokala enhet, vanligtvis i mappen "downloads", varifrån du kan ta den och flytta den utanför din enhet för säker förvaring.
- "Verifiera kanalbackup" - det här är ett bra alternativ om du använder Google Drive eller iCloud för att kontrollera integriteten för säkerhetskopian som görs på distans.
- "Google drive channel backup" - sparar säkerhetskopian på din personliga Google-disk. Filen är krypterad och lagras i ett separat förvar än dina vanliga Google-filer. Så det finns inga problem som kan läsas av någon. Hur som helst är den filen helt värdelös utan seed-orden, så ingen kan ta dina pengar från den filen bara.


Jag skulle rekommendera följande för detta avsnitt:



- använd en lösenordshanterare för att säkert lagra din seed och säkerhetskopieringsfil. [KeePass](https://keepass.info/) eller Bitwarden är mycket bra för det och kan användas på flera plattformar och själv värd eller offline.
- GÖR BACKUP VARJE GÅNG du öppnar eller stänger en kanal. Den filen uppdateras med kanalinformationen. Det finns inget behov av att göra det efter varje transaktion du har gjort på LN. Kanalbackupen lagrar inte den informationen, den lagrar bara kanalens status.


![Demo Blixt 21](assets/blixt_t21.webp)


## Slutsats


Ok, det finns många andra fantastiska funktioner som Blixt erbjuder, jag kommer att låta dig upptäcka dem en efter en och ha kul.


Denna app är verkligen underskattad, främst för att den inte stöds av någon VC-finansiering, är samhällsdriven, byggd med kärlek och passion för Bitcoin och Lightning Network.


Denna mobila LN-nod, Blixt är ett mycket kraftfullt verktyg i händerna på många användare, om de vet hur man använder det väl. Tänk dig att du går runt i världen med en LN-nod i din egen ficka och ingen kommer att veta det.


Och inte talar om alla andra rika funktioner som följer med, som mycket få eller inga andra Wallet-appar kan erbjuda.


Jag hoppas att du tycker om att använda den. Personligen älskar jag den och den är mycket användbar för mig (se här ett användningsfall där denna Wallet är ett utmärkt verktyg).


GLAD Bitcoin BLIXTNEDSLAG!


Må ₿ITCOIN vara med dig!


**Disclaimer:** Jag får inte betalt eller stöd på något sätt av utvecklarna av den här appen. Jag skrev den här guiden eftersom jag såg att intresset för den här Wallet-appen ökar och nya användare fortfarande inte förstår hur man börjar med den. Även för att hjälpa Hampus (huvudutvecklaren) med dokumentation om hur man använder denna nod Wallet. Jag har inget annat intresse av att främja denna LN-app, förutom att driva framåt antagandet av Bitcoin och LN. Detta är det enda sättet!