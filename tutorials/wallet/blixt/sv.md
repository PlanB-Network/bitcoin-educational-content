---
name: Blixt Wallet
description: Hur börjar man använda en kraftfull LN-nod på din mobil?
---
![cover](cover.webp)


Denna guide är tillägnad alla nya användare som vill börja använda Bitcoin Lightning Network (LN) på ett GRATIS OPEN SOURCE, FULLSTÄNDIGT NON-CUSTODIAL sätt.


Med [Blixt Wallet] (https://blixtwallet.com/), en komplett LN-nod i din mobil, var du än befinner dig.


Om du aldrig använt Bitcoin Lightning Network, innan du börjar, [läs den här enkla förklaringen analogi om Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## VIKTIGA ASPEKTER:



- Blixt är en privat nod, INTE en routingnod! Tänk på det: Det betyder att alla LN-kanaler i Blixt kommer att vara oannonserade för LN-grafen (så kallade privata kanaler). Det betyder att DENNA NOD INTE kommer att göra routing av andra betalningar genom Blixt-noden. Denna Blixt-nod är INTE för routing, jag upprepar. Det är främst för att kunna hantera dina egna LN-kanaler och göra dina LN-betalningar privat, när du behöver. Denna Blixt-nod är nödvändig för att vara online och synkroniserad ENDAST INNAN du ska göra dina transaktioner. Det är därför du kommer att se en ikon på toppen som indikerar synkroniseringsstatusen. Det tar bara några ögonblick, beroende på hur mycket tid du har hållit den offline.



- Blixt använder LND (aezeed) som Wallet backend, så försök inte att importera andra typer av Bitcoin plånböcker till den. [Här har du förklarat typerna av Wallet Mnemonic frön](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Och här är [en mer omfattande lista över alla typer av plånböcker](https://walletsrecovery.org/). Så om du tidigare hade en LND-nod kan du importera seed och backup.channels till Blixt, [som det förklaras i den här guiden](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- I slutet av denna guide hittar du ett särskilt avsnitt med ["tips och tricks"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt viktiga länkar - se dem i slutet av denna guide, vänligen bokmärk dem.


---

## Blixt - Första kontakten


Så ... Darths mamma bestämde sig för att börja använda LN med Blixt. Hard beslut, men klokt. Blixt är bara för smarta människor och de som verkligen vill lära sig mer, djup användning av LN.


![blixt](assets/en/01.webp)


Darth varnade sin mamma:


"*Mamma, om du börjar använda Blixt LN Node måste du först veta vad Lightning Network är och hur det fungerar, åtminstone på grundläggande nivå. [Här har jag sammanställt en enkel lista med resurser om Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Vänligen läs dem först.*"


Darth's Mom läste resurserna och gjorde sitt första steg: installerade Blixt på sin helt nya Android-enhet. Blixt finns också för iOS och macOS (stationär). Men de är inte för Darths mamma... Ändå rekommenderas det att använda en nyare version av Android, minst 9 eller 10 för bättre kompatibilitet och upplevelse. Att köra en fullständig LN-nod på en mobil enhet är inte en lätt uppgift och kan ta lite utrymme (min 600 MB) och minne.


När du öppnar Blixt kommer skärmen "Välkommen" att ge dig några alternativ:


![blixt](assets/en/02.webp)


I det övre högra hörnet ser du 3 prickar som aktiverar en meny med:



- "enable Tor" - användaren kan börja med Tor-nätverket, speciellt om man vill återställa en gammal LND-nod som kördes med Tor-peers.
- "Ställ in Bitcoin-nod" - om användaren vill ansluta till sin egen nod direkt, för att synkronisera blocken via Neutrino, kan göra det direkt från välkomstskärmen. Det här alternativet är också bra om din internetanslutning eller Tor inte är så stabil att du kan ansluta till standard Bitcoin-noden (node.blixtwallet.com).
- Snart kommer det att läggas till språk där, så att användaren kan börja direkt med ett språk som är bekvämt. Om du vill bidra till detta open source-projekt med översättningar till andra språk, [vänligen gå med här](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### ALTERNATIV A - Skapa en ny Wallet


Om du väljer att "skapa en ny Wallet" kommer du att omdirigeras direkt till huvudskärmen för Blixt Wallet.


Detta är din "cockpit" och även "Main LN Wallet", så var medveten om att den endast visar balansen i din LN Wallet. Wallet i kedjan visas separat (se C).


![blixt](assets/en/03.webp)


A - Ikon för synkroniseringsindikator för Blixt-block. Detta är det viktigaste för en LN-nod: att vara synkroniserad med nätverket. Om den ikonen fortfarande fungerar betyder det att din nod INTE ÄR KLAR! Så ha tålamod, särskilt för den första initiala synkroniseringen. Det kan ta upp till 6-8 minuter, beroende på din enhet och internetanslutning.


Du kan klicka på den och se status för synkroniseringen:


![blixt](assets/en/04.webp)


Du kan också klicka på knappen "Show LND Log" (A) om du vill se och läsa mer tekniska detaljer i LND-loggen i realtid. Är mycket användbart för felsökning och för att lära sig mer om hur LN fungerar.


B - Här kan du komma åt alla Blixt-inställningar, och det är många! Blixt erbjuder många rika funktioner och alternativ för att hantera din LN-nod som ett proffs. Alla dessa alternativ förklaras i detalj i "[Blixt Features Page](https://blixtwallet.github.io/features#blixt-options) - Options Menu".


C - Här har du menyn "Magic Drawer", [förklaras också i detalj här](https://blixtwallet.github.io/features#blixt-drawer). Här finns "Onchain Wallet" (B), Lightning Channels (C), Contacts, Channels status icon (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Är hjälpmenyn, med länkar till FAQ / Guides-sidan, kontakta utvecklaren, Github-sidan och Telegram supportgrupp.


E - Ange din första BTC Address, där du kan sätta in din första testning Sats. DETTA ÄR VALFRITT! Om du sätter in direkt i den Address, öppnar en LN-kanal mot Blixt Node. Det betyder att du kommer att se din deponerade Sats, gå in i en annan onchain-transaktion (tx), för att öppna den LN-kanalen. Du kan kontrollera det i Blixt onchain Wallet (se punkt C) genom att klicka på TX-menyn längst upp till höger.


![blixt](assets/en/06.webp)


Som du kan se i Onchain Transaction Log är stegen mycket detaljerade och anger vart Sats går (insättning, öppen, stängd kanal).


REKOMMENDATION:


Efter att ha testat flera situationer kom vi fram till att det är mycket mer effektivt att öppna kanaler mellan 1 och 5 M Sats. Mindre kanaler tenderar att tömmas snabbt och betala en högre % av avgifterna jämfört med större kanaler.


F - Ange ditt huvudsakliga Lightning Wallet-saldo. Detta är INTE ditt totala Blixt Wallet-saldo, det representerar endast de Sats du har i Lightning Channels, tillgängliga för att skicka. Som tidigare angivits är Onchain Wallet separat. Tänk på denna aspekt. Onchain Wallet är separat av en viktig anledning: den används främst för att öppna / stänga LN-kanaler.


Ok så nu deponerade Darths mamma några Sats i den onchain Address som visas på huvudskärmen. Det rekommenderas att när du gör det, att hålla din Blixt-app online och aktiv ett tag tills BTC tx tas av gruvarbetarna i det första blocket.


Efter det kan det ta upp till 20-30 minuter tills det är helt bekräftat och kanalen är öppen och du kommer att se den i Magic Drawer - Lightning Channels som aktiv. Även den lilla färgade pricken på toppen av lådan, om det är Green, kommer att indikera att din LN-kanal är online och redo att användas för att skicka Sats över LN.


Address och välkomstmeddelandet som visas kommer att försvinna. Det är inte längre nödvändigt att öppna en automatisk kanal nu. Du kan också avaktivera alternativet i menyn Inställningar.


Det är dags att gå vidare och testa andra funktioner och alternativ för att öppna LN-kanaler.


Låt oss nu öppna en annan kanal med en annan node peer. Blixt community satte ihop [en lista över bra noder att börja använda med Blixt] (https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Förfarande för att öppna en LN-kanal i Blixt**


Detta är mycket enkelt, det krävs bara några få steg och lite tålamod:



- Kom med på [Blixt Community](https://github.com/hsjoberg/blixt-Wallet/issues/1033):s lista över kollegor
- Välj en nod och klicka på länken i dess namntitel, så öppnas dess Amboss-sida
- Klicka för att visa QR-koden för nodens URI Address


![blixt](assets/en/07.webp)


Öppna Blixt och gå till den övre lådan - Lightning Channels och klicka på "+" -knappen


![blixt](assets/en/08.webp)


Klicka nu på (A)-kameran för att skanna QR-koden från Amboss-sidan och nodinformationen kommer att fyllas i. Lägg till beloppet för Sats för den kanal du vill ha och välj sedan avgiftssatsen för tx. Du kan låta den vara automatisk (B) för en snabbare bekräftelse eller justera den manuellt genom att skjuta på knappen. Du kan också trycka länge på numret och redigera det som du vill.


Lägg inte mindre än 1 sat/vbyte ! Vanligtvis är det bättre att konsultera [Mempool avgifter] (https://Mempool.space/) innan du öppnar en kanal och välja en lämplig avgift.


Klar, klicka nu bara på knappen "öppen kanal" och vänta på 3 bekräftelser, det tar vanligtvis 30 minuter (1 block aprox var 10: e minut).


När det är bekräftat kommer du att se kanalen aktiv i ditt avsnitt "Lightning Channels".


---

## Blixt - Andra kontakten


Ok, så nu har vi en LN-kanal med endast OUTBOUND-likviditet. Det betyder att vi bara kan SÄNDA, vi kan fortfarande inte MOTTA Sats över LN.


![blixt](assets/en/09.webp)


Hur så? Har du läst de guider som anges i början? Nej, det har jag inte Gå tillbaka och läs dem. Det är mycket viktigt att förstå hur LN-kanalerna fungerar.


![blixt](assets/en/10.webp)


Som du kan se i det här exemplet har kanalen som öppnas med den första insättningen inte för mycket INBOUND-likviditet ("Kan ta emot") men har mycket OUTBOUND-likviditet ("Kan skicka").


Så vilka alternativ har du om du vill ta emot mer Sats än LN?



- Spendera några Sats från befintlig kanal. Ja, LN är ett betalningsnätverk för Bitcoin, som huvudsakligen används för att spendera din Sats snabbare, billigare, privat och enkelt. LN är INTE ett hodlingssätt, för det har du onchain Wallet.



- Byt ut några Sats, tillbaka till din onchain Wallet, med hjälp av en submarin bytestjänst. På detta sätt spenderar du inte din Sats, utan ger den tillbaka till din egen onchain Wallet. Här kan du se i detalj några metoder, på [Blixt Guides Page](https://blixtwallet.github.io/guides).



- Öppna en INBOUND-kanal från vilken LSP-leverantör som helst. Här är en videodemo om hur du använder LNBig LSP för att öppna en inkommande kanal. Det betyder att du betalar en liten avgift för en TOM kanal (på din sida) och du kommer att kunna ta emot mer Sats till den kanalen. Om du är en handlare som får mer än att spendera är det ett bra alternativ. Även om du köper Sats över LN, använder Robosats eller någon annan LN Exchange.



- Öppna en Dunder-kanal, med Blixt-nod eller någon annan Dunder LSP-leverantör. En Dunder-kanal är ett enkelt sätt att få lite INBOUND-likviditet, men samtidigt sätter du in lite Sats i den kanalen. Det är också bra eftersom det kommer att öppna kanalen med en [UTXO] (https://en.Bitcoin.it/wiki/UTXO) som inte är från din Blixt Wallet. Det ger lite integritet. Det är också bra eftersom, om du inte har Sats i en onchain Wallet, för att öppna en normal LN-kanal, men du har dem i en annan LN Wallet, kan du bara betala från den andra Wallet genom LN öppningen och insättningen (på din sida) av den Dunder-kanalen. [Mer detaljer om hur Dunder fungerar och hur du driver din egen server här](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Här är stegen för att aktivera öppning av en Dunder-kanal:



- Gå till Inställningar, i avsnittet "Experiment" aktivera rutan för "Aktivera Dunder LSP".
- När du gjort det, gå tillbaka upp till "Lightning Network" sektionen och du kommer att se att det dykt upp alternativet "Set Dunder LSP Server". Där är som standard inställd "https://dunder.blixtwallet.com" men du kan ändra den med någon annan Dunder LSP-leverantör Address. [Här är en Blixt community list](https://github.com/hsjoberg/blixt-Wallet/issues/1033) med noder som kan tillhandahålla Dudner LSP-kanaler för din Blixt.
- Nu kan du gå till huvudskärmen och klicka på "Receive" -knappen. Följ sedan denna procedur [förklaras i den här guiden] (https://blixtwallet.github.io/guides#guide-lsp).


OK, så efter att Dunder-kanalen har bekräftats (tar några minuter) kommer du att ha två LN-kanaler: en öppnad initialt med autopilot (kanal A) och en med mer inkommande likviditet, öppnad med Dunder (kanal B).


![blixt](assets/en/12.webp)


Bra, nu är du redo att skicka och ta emot tillräckligt med Sats över LN!


GLAD Bitcoin BLIXTNEDSLAG!


---

## Blixt - Tredje kontakten


Kom ihåg att det i kapitel ett "Första kontakt" fanns två alternativ på välkomstskärmen:


- [Alternativ A] (https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Skapa en ny Wallet
- Alternativ B - Återställa Wallet


Så låt oss nu diskutera hur man återställer en Blixt Wallet eller någon annan LND kraschad nod. Det här är lite mer tekniskt, men var uppmärksam. Är inte det Hard.


### ALTERNATIV B - Återställa Wallet


Tidigare skrev jag en dedikerad guide om [hur man återställer en kraschad Umbrel-nod] (https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), där jag också nämnde metoden att använda Blixt som snabb återställningsprocess, med hjälp av seed + channel.backup-filen från Umbrel.


Jag har också skrivit en guide om hur du återställer din Blixt-nod eller migrerar din Blixt till en annan enhet, [här](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Men låt oss förklara i enkla steg denna process. Som du kan se i bilden ovan finns det två saker du bör göra för att återställa din tidigare Blixt/LND-nod:



- den översta rutan är där du måste fylla i alla 24 orden från din seed (gammal/död nod)
- längst ner finns två knappalternativ för att infoga / ladda upp filen channel.backup, som tidigare sparats från din gamla Blixt/LND-nod. Det kan vara från en lokal fil (du laddar upp den till din enhet tidigare) eller kan vara från en Google Drive / iCloud-fjärrplats. Blixt har det här alternativet för att spara dina kanalers säkerhetskopia direkt till en Google / iCloud-enhet. Se mer information på [Blixt Features Page] (https://blixtwallet.github.io/features#blixt-options).


Ändå att nämna, om du tidigare inte hade några öppna LN-kanaler, finns det inget behov av att ladda upp någon channels.backup-fil. Sätt bara in de 24 orden seed och tryck på återställningsknappen.


Glöm inte att aktivera Tor, från den övre menyn med 3 prickar, som vi förklarade i avsnittet Alternativ A. Det är fallet när du ENDAST hade Tor-kollegor och inte kunde kontaktas via clearnet (domän / IP). Annars är det inte nödvändigt.


En annan användbar funktion är att ställa in en specifik Bitcoin-nod från den övre menyn. Som standard synkroniserar den block från node.blixtwallet.com (neutrino-läge) men du kan ställa in vilken annan Bitcoin-nod som helst som tillhandahåller neutrino-synkronisering.


Så när du har fyllt i dessa alternativ och tryckt på återställningsknappen kommer Blixt först att börja synkronisera blocken via Neutrino som vi förklarade i kapitlet Första kontakten. Så ha tålamod och titta på återställningsprocessen på huvudskärmen genom att klicka på synkroniseringsikonen.


![blixt](assets/en/14.webp)


Som du kan se i det här exemplet visar det att Bitcoin-blocken är 100% synkroniserade (A) och att återställningsprocessen är i gång (B). Det betyder att LN-kanalerna som du hade tidigare kommer att stängas och pengarna återställas till din Blixt onchain Wallet.


Den här processen tar tid! Ha därför tålamod och försök att hålla din Blixt aktiv och online. Den första synkroniseringen kan ta upp till 6-8 minuter och stängningen av kanalerna kan ta upp till 10-15 minuter. Så det är bäst att du har enheten väl laddad.


När den här processen har startat kan du kontrollera i Magic Drawer - Lightning Channels, statusen för var och en av dina tidigare kanaler, som visar att de är i "väntan på att stänga" -status. När varje kanal är stängd kan du se den stängande tx i onchain Wallet (se Magic Drawer - Onchain) och öppna upp tx-menyloggen.


![blixt](assets/en/15.webp)


Det kan också vara bra att kontrollera och lägga till om de inte finns där, dina tidigare peers som du hade i din gamla LN-nod. Så gå till menyn Inställningar, ner till "Lightning Network" och ange alternativet "Visa Lightning Peers".


![blixt](assets/en/16.webp)


Inuti avsnittet ser du de kamrater du är anslutna i det ögonblicket och du kan lägga till fler, bättre att lägga till de du hade kanaler tidigare. Gå bara till [Amboss-sidan] (https://amboss.space/), sök efter dina peer-noder alias eller nodeID och skanna deras nod URI.


![blixt](assets/en/17.webp)


Som du kan se i bilden ovan finns det 3 aspekter:


A - representerar clearnet-noden Address URI (domän/IP)


B - representerar Tor-löknoden Address URI (.onion)


C - är QR-koden som ska skannas med din Blixt-kamera eller kopieringsknappen.


Den här noden Address URI måste du lägga till i din peers-lista. Så var medveten om att det inte räcker med bara nodens aliasnamn eller nodeID.


Nu kan du gå till Magic Drawer (menyn längst upp till vänster) - Lightning Channels, och du kan se vid vilken löptidsblockhöjd pengarna kommer att återföras till din onchain Address.


![blixt](assets/en/18.webp)


Det blocknummer 764272 är när medlen kommer att kunna användas i din Bitcoin onchain Address. Och det kan ta upp till 144 block från det 1: a bekräftelseblocket tills de släpps. [Så kontrollera det i Mempool](https://Mempool.space/).


Och så är det med det. Vänta bara tålmodigt tills alla kanaler är stängda och pengarna tillbaka till din onchain Wallet.


👉 **Sekret återställningsmetod :**


Det finns en annan metod för att återställa din Blixt LND-nod utan att ens stänga kanalerna. Men är dold från vanliga noob-användare, eftersom den här metoden ENDAST är för dem som vet vad de gör.


Om du behöver migrera din befintliga (fungerande) Blixt-nod till en annan ny enhet, utan att stänga de befintliga LN-kanalerna, måste du göra dessa steg:



- Vi antar att du redan har sparat Blixt Wallet seed (24 ord aezeed)
- På den gamla enheten, gå till "Inställningar" - felsökningsavsnitt - "Kompakt LND-databas". Detta steg är valfritt men rekommenderas om du vill ha en mindre storlek på filen channel.db. Vanligtvis är den ganska stor, beroende på din nodaktivitet. Detta kommer att starta om Blixt och komprimera db-filstorleken.
- När du har startat om går du till "Inställningar" och ändrar ditt vanliga aliasnamn till "Hampus". Detta kommer att aktivera de dolda alternativen, endast för avancerade användare.
- Gå långt ner till avsnittet "Debug" och du kommer att se ett nytt alternativ "Exportera channel.db-fil". VARNING! När du gör den här exporten kommer den befintliga Blixt LN-noden att inaktiveras på den här gamla enheten och exportera hela noddatabasen (channel.db) redo att importeras till en ny enhet.
- Denna db-fil kommer att sparas i en särskild mapp på din gamla enhet (Dokument eller Nedladdningar) och därifrån måste du flytta den som den är till din nya enhet. Du kan t.ex. använda [LocalSend FOSS app] (https://github.com/localsend/localsend) för att överföra filen direkt mellan enheter.
- I det här ögonblicket MÅSTE din gamla Blixt förbli stängd. ÖPPNA DEN INTE IGEN!
- När du har överfört filen channel.db till den nya enheten startar du den nya installationen av Blixt och väljer "Restore Wallet" på den första skärmen.
- På knappen där det står "Välj SCB-fil" tryck länge (INTE enkelt klick!) Och då ser du alternativet att välja en channel.db-fil där du sparar den lokalt i den nya enheten. Om du bara enkelt trycker på den knappen kommer den som standard att använda en SCB-fil (med stängningskanaler), det fungerar inte för live-kanaler med full säkerhetskopiering.
- Skriv de 24 orden seed och klicka sedan på "Återställ"
- Du kommer att se att Blixt börjar synkronisera med Neutrino. Du kan också titta på synkroniseringsloggarna.
- HÅLL I MINNET! Försök att hålla Blixt öppet hela tiden under denna fas! Låt den inte gå i viloläge eller stänga appskärmen. Det kan störa den initiala synkroniseringen och du måste göra det igen. Vänta tålmodigt, det tar inte mer än några minuter.
- När den första blocksynkroniseringen är klar kommer den snabbt att skanna dina tidigare Wallet-adresser och sedan kommer dina kanaler att vara tillbaka online, levande och väl.
- Tyvärr är det inte möjligt (ännu) att återställa tidigare betalningshistorik och kontakter. Men det är inte så viktigt i alla fall.


Och KLART! Nu har du en helt återställd Blixt LN nod. Det kan också fungera med andra LND-säkerhetskopior (Umbrel, Raspiblitz etc.) om du tidigare sparade korrekt channel.db-filen. Så Blixt kan bokstavligen rädda alla LND döda noder.


---

## Blixt - Fjärde kontakten


Det här kapitlet handlar om anpassning och om att lära känna Blixt Node bättre. Jag kommer inte att beskriva alla tillgängliga funktioner, de är för många och har redan förklarats på [Blixt Features Page] (https://blixtwallet.github.io/features).


Men jag kommer att peka på några av de nödvändiga för att gå vidare med att använda din Blixt och få en bra upplevelse.


### A - Namn (NamnBeskrivning)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) är en standard för att förmedla "mottagarens namn" i BOLT11-fakturor.


Detta kan vara vilket namn som helst och kan ändras när som helst.


Detta alternativ är verkligen användbart i olika fall, när du vill skicka ett namn tillsammans med Invoice-beskrivningen, så att mottagaren kan få en ledtråd från vem som fick dessa Sats. Detta är helt valfritt och även på betalningsskärmen måste användaren kryssa i rutan för att ange att aliasnamnet ska skickas.


Här är ett exempel på hur det ser ut när du använder [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Detta är ett annat exempel på att skicka till en annan Wallet-app som stöder NameDesc:


![blixt](assets/en/21.webp)


### B - Blixtlåda


Från och med den nya v0.6.9-420 [nyligen meddelad] (https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420) introducerade Blixt en ny kraftfull funktion för Lightning Address i Blixt.


Den här nya funktionen är valfri och är inte PÅ som standard!


För tillfället körs standard LN Box av Blixt-servern och erbjuder en @blixtwallet.com LN Address. Men ALLA med en offentlig LND-nod kan köra Lightning Box-servern och erbjuda LN Address för sin egen domän, självförvaring.


Just nu vidarebefordrar Blixt-servern endast de betalningar som skickas till LN-adresser @blixtwallet.com till de Blixt-användare som ställer in sin LN Address. Användare måste sätta sin Blixt-nod Wallet i "persistent mode" för att kunna ta emot dessa betalningar till sina @blixtwallet.com LN-adresser.


Se videodemonstrationen i release notes om hur du konfigurerar din LN Address i Blixt.


Denna LN Address implementerad i Blixt Wallet app, är som en chatt över LN, omedelbar och rolig, stöder också [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (lägga till ett aliasnamn till en betalning). Du kan lägga till i kontaktlistan alla dina vanliga LN-adresser som du använder ofta och ha dem till hands för att chatta. Nu kan Blixt betraktas som en fullständig LN chattapp 😂😂.


En annan användbar funktion är det fulla stödet från LUD-18 (som också [Stacker.News](https://stacker.news/r/DarthCoin) och andra stöder det).


![blixt](assets/en/22.webp)


Som du kan se på skärmdumpen ovan, när du skickade från ett Stacker News-konto, visade den snyggt logotypen + LN Address + meddelandet. Samma sätt fungerar för att skicka från Blixt, du kan bifoga din Blixt LN Address eller helt enkelt lägga till aliasnamnet (tidigare inställt i Blixt-inställningarna) eller till och med båda.


Detta alternativ från LUD-18 kan vara användbart även för prenumerationstjänster, där användaren kan skicka ett specifikt alias (är INTE ditt nodalias eller ditt riktiga namn!) och baserat på det kan du registreras eller få tillbaka ett specifikt meddelande eller något annat. Att bifoga ett aliasnamn ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ kommentar ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) till en LN-betalning kan ha flera användningsområden!


Här är koden för [Lightning Box] (https://github.com/hsjoberg/lightning-box) om du kör den för dig själv, för din familj och dina vänner, på din egen nod.


Här kan du också köra [LSP Dunder-servern] (https://github.com/hsjoberg/dunder-lsp) för Blixt mobila noder och erbjuda likviditet för Blixt-användare om du har en bra publik LN-nod (fungerar endast med LND).


### C - Backup LN-kanaler och seed-ord


Detta är en mycket viktig funktion!


När du har öppnat eller stängt en LN-kanal bör du göra en säkerhetskopia. Det kan göras manuellt genom att spara en liten fil på den lokala enheten (vanligtvis i nedladdningsmappen) eller genom att använda ett Google Drive- eller iCloud-konto.


![blixt](assets/en/23.webp)


Gå till Blixt Inställningar - Wallet avsnitt. Där har du möjlighet att spara alla viktiga data för din Blixt Wallet:



- "Visa Mnemonic" - kommer att visa de 24 orden seed för att skriva ner dem
- "Ta bort Mnemonic från enheten" - detta är valfritt och använd det endast om du verkligen vill ta bort seed-orden från din enhet. Detta kommer INTE att torka din Wallet, bara seed. Men var medveten om detta! Det finns inget sätt att återställa dem om du inte skrev ner dem först.
- "Export channel backup" - det här alternativet sparar en liten fil på din lokala enhet, vanligtvis i mappen "downloads", varifrån du kan ta den och flytta den utanför din enhet för säker förvaring.
- "Verifiera kanalbackup" - det här är ett bra alternativ om du använder Google Drive eller iCloud för att kontrollera integriteten för säkerhetskopian som görs på distans.
- " Google drive channel backup" - sparar säkerhetskopian på din personliga Google-enhet. Filen är krypterad och lagras i ett separat förvar än dina vanliga Google-filer. Så det finns inga problem som kan läsas av någon. Hur som helst är den filen helt värdelös utan seed-orden, så ingen kan ta dina pengar från den filen bara.


Jag skulle rekommendera följande för detta avsnitt:



- använd en lösenordshanterare för att säkert lagra din seed och säkerhetskopieringsfil. KeePass eller Bitwarden är mycket bra för det och kan användas på flera plattformar och själv värd eller offline.
- GÖR BACKUP VARJE GÅNG du öppnar eller stänger en kanal. Den filen uppdateras med kanalinformationen. Det finns inget behov av att göra det efter varje transaktion du har gjort på LN. Kanalbackupen lagrar inte den informationen, den lagrar bara kanalens status.


![blixt](assets/en/24.webp)


---

## Blixt - Tips och tricks


### FALL 1 - PROBLEM MED SYNKRONISERING


"_Mitt Blixt synkroniseras inte... Min Blixt visar inte saldot... Min Blixt kan inte öppna kanaler... Jag försökte återställa den i en annan enhet ... etc_"


Alla dessa problem börjar med att DIN ENHET INTE SYNKRONISERAR PÅ RÄTT SÄTT. Vänligen förstå denna viktiga aspekt: Blixt är en mobil LND-nod som använder Neutrino för att synkronisera / läsa blocken.



- Här är en mindre teknisk förklaring från [Bitcoin Magazine] (https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Här är mer tekniska resurser från [Bitcoin Optech] (https://bitcoinops.org/en/topics/compact-block-filters/)
- Så här kan du aktivera Neutrino på din egen hemnod och servera blockfilter för din mobilnod, från [Docs Lightning Engineering] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


PÅMINNELSE: Att använda Neutrino över clearnet är helt säkert, din IP eller xpub läcker inte ut. Du läser bara block från en fjärrnod med neutrino. Det är allt. Allt annat görs på din lokala enhet.


Så det finns INGEN BEHOV att använda det med Tor. Tor kommer att lägga till en enorm latens på din synkroniseringsprocess och kommer att göra din Blixt mycket instabil. Om du verkligen vill använda över Tor, var säker på vad du gör och ha en bra anslutning och tålamod. Samma sak gäller för att använda ett VPN. Var försiktig med vilken latens som ges till dig från det VPN.


Du kan testa latensen för en neutrinoserver genom att helt enkelt pinga den, från en dator eller från din mobil.


![blixt](assets/en/25.webp)


Detta är en vanlig ping till neutrino-servern europe.blixtwallet.com, detta visar att anslutningen är mycket bra med en svarstid på avg 50ms och en TTL på 51. Svarstiden kan variera men inte för mycket. TTL måste vara stabil.


Om dessa värden är högre än 100-150 ms kommer din synkroniseringsprocess att bli inaktuell eller ännu värre, det kan orsaka stängda kanaler hos motparter! Ignorera inte denna aspekt.


Utan en korrekt synkronisering kan du inte heller se rätt balans eller så kommer dina LN-kanaler inte att komma online och fungera. Oavsett hur många giga ultra terra mbps du har nedladdningshastigheten DET ÄR INTE MATTER. Det spelar roll tidssvaret och TTL (tid att leva).


Detta är som ett allmänt fall för LATAM-användare. Jag vet inte vad som händer där nere, men ni har en fruktansvärd anslutning med pingar på över 200 ms som kan störa alla synkroniseringar.


Så vad är lösningen för dessa desperata användare?



- sluta använda Blixt med Tor. Är helt värdelös
- du kan använda ett VPN men välj det klokt och övervaka hela tiden ping. Använd en som är närmare din geografiska plats. Avstånd betyder mer ms-svarstid, kom ihåg det.
- välj klokt dina neutrino-peers, här är en lista över välkända offentliga neutrino-servrar:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Ett annat sätt är att välja en från denna lista över noder som meddelar "kompakta filter" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Välj en som ligger närmare din geografiska plats.


Ett annat sätt (det bästa sättet) är att ansluta till en lokal community-nod, som drivs av en vän eller grupp som du känner, och som erbjuder neutrinoanslutning. [Här är instruktionerna för hur du gör det.](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Deras nod kommer inte att påverkas på något sätt, de behöver bara en stabil och offentlig anslutning.


Det finns ett behov av fler neutrinoservrar i LATAM-regionen, för en bättre och snabb synkronisering. Så vänligen organisera dig själv, med din lokala Bitcoin-community och bestäm vem och var som kör en Bitcoin Core + Neutrino för eget bruk. Med bara en offentlig IP är det tillräckligt. Om du inte har tillgång till en offentlig IP kan du använda en VPS-IP och göra wireguard-tunnel till din hemnod. På så sätt omdirigerar du all trafik till din lokala VPS-IP utan att avslöja någon privat information om din hemnod.


### FALL 2 - ALDRIG AVSLUTA SYNKRONISERINGEN


"_Mitt Blixt har bra anslutning till neutrino-servern men har fastnat i synkroniseringen._"


#### Tidsserver


Ibland använder människor olika gamla enheter eller är inte korrekt anslutna till en tidsserver. Neutrino synkroniserar ok tills de faktiska blocken som inte motsvarar verklig lokal tid nås. Du kommer att se i Blixt LND-loggar ett fel som säger att "blockets tidsstämpel är långt ifrån framtiden" eller något relaterat till "header passerar inte sanity check".


Snabb lösning: ställ in rätt tid och datum för din enhet och starta om Blixt.


#### Litet utrymme på enheten


Ibland när man använder en gammal enhet, med lite utrymme, kan den nå en tröskelgräns och fastna. Ju mer du använder den här mobila LND-noden, desto större blir neutrino-filerna och även filen channel.db.


Snabb lösning: Gå till Blixt Options - Debug section - Välj "stop LND and delete neutrino files". Det kommer att starta om appen och starta en ny synkronisering. Ibland kan den här snabbkorrigeringen reparera även skadad data. Tänk på att det kommer att ta lite tid, mellan 1 och 3 minuter att helt synkronisera igen. Det raderar INTE befintliga fonder eller kanaler, men ja, efter resynkronisering kan det utlösa en omskanning av dina Bitcoin-adresser och det kan ta längre tid.


Nästa steg är att kontrollera hur mycket data som fortfarande är upptagen. Du kan se detta i Android App info - data. Om det fortfarande är större än 400-500 MB kan du komprimera LND-filerna. Så gå till Blixt Options - Debug-sektionen - Välj "Compact DB LND". Starta om Blixt-appen om den inte gör det automatiskt. Komprimeringen sker vid uppstart och är bara en gång. Nu kommer du att se att Blixt-data är mer eller mindre upptagna.


#### Beständigt läge


Ibland öppnar folk inte Blixt på länge, så det är alldeles för gammalt för synkronisering. Men de förväntar sig att bli synkroniserade direkt när de öppnar det.


Ha tålamod och titta på det översta snurrande hjulet. Alternativt kan du gå till Options - See Node Info och se om är synkad till kedja och synkad till graf markerad som "true". Utan det "sanna" omnämnandet kan du inte använda Blixt korrekt, du kan inte se saldot korrekt, du kan inte se LN-kanalerna online, du kan inte göra betalningar.


Snabb lösning: Det finns ett kraftfullt alternativ för att "hålla liv" i din Blixt-nod. Gå till Alternativ - Experiment - Välj "Aktivera ihållande läge". Det kommer att starta om din Blixt och sätta LND-tjänsten i ihållande läge, vilket innebär att den alltid kommer att vara aktiv och hålla synkroniseringen online, även om du byter till en annan app eller helt enkelt stänger Blixt (inte tvinga stänga eller döda uppgiften). Du kan hålla det så hela dagen om du har en stabil anslutning och du behöver använda Blixt flera gånger. Det kommer inte att förbruka för mycket batteri.


### FALL 3 - JAG VILL MIGRERA TILL EN ANNAN ENHET


OK om detta scenario skrev jag en omfattande guide på [FAQ-sidan](https://blixtwallet.github.io/faq#blixt-restore): med 2 alternativ, snabb (kooperativ stängning av kanaler före migrering) och långsam (tvinga stänga kanaler eftersom den gamla enheten är död).


Men jag vill här upprepa några viktiga aspekter och lägga till ett nytt "hemligt" förfarande.


PÅMINNELSE:



- Gör alltid en säkerhetskopia av dina kanalers status (SCB) EFTER varje gång du öppnar eller stänger en kanal. Det tar bara några sekunder att göra det.
- Behåll inte de gamla SCB-filerna, för att inte bli förvirrad och återställa dem. De är helt värdelösa och kan utlösa ett straffrättsligt förfarande om du återställer dem. Använd alltid den senaste versionen av filen SCB om du fortsätter att återställa.
- Spara SCB-filen (är en krypterad text med tillägget .bin) från din enhet på en säker plats. Du kan använda [LocalSend] (https://github.com/localsend/localsend) för att flytta filen till en dator eller annan enhet.
- Spara även seed för din Blixt Wallet på en säker plats, t.ex. en offline lösenordshanterare/krypterad USB.


Hemlig metod: Hur man migrerar Blixt-nod utan att stänga de befintliga kanalerna. För detta måste du läsa noggrant det föregående avsnittet "Tredje kontakt" i den här guiden om "Återställ Wallet".


Denna procedur DET ÄR INTE FÖR NOOBS, det är bara för avancerade användare! Det är därför det inte är allmänt öppet och jag rekommenderar att du bara gör det med hjälp av Blixt devs eller mitt stöd. Vänligen ignorera inte detta råd.


### CASE 4 - VILKA PEERS SKA MAN ANVÄNDA FÖR ATT ÖPPNA KANALER?


Som jag skrev i [Blixt guides page](https://blixtwallet.github.io/guides) finns det många sätt att öppna kanaler med denna mobila LND nod. Men några viktiga aspekter skulle jag vilja påminna dig om här:



- öppna med välkända LSP-noder och med community vouched peers. [Se här en lista](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- öppna inte med slumpmässiga Tor-noder. De är värdelösa och du kommer bara att få problem med att inte kunna göra betalningar. Oavsett hur bra din vän "the node runner" är med en skitig Tor-nod i en djungel, kommer den aldrig att ge dig de bästa rutterna för en mobil privat nod. Du öppnar inte kanaler med någon bara för att han är din vän. Det här är inte Facebook! Du öppnar en kanal för: bra rutter, små avgifter, tillgänglighet.
- det finns inget behov av att öppna ett skit ton små kanaler, 2-3 eller max 4, men med en bra mängd Sats. Öppna inte små kanaler, är helt värdelösa. Mindre än 200k för en mobil har inte mycket användning.
- kom ihåg LSP: erna som erbjuder inkommande kanaler och JIT-kanaler (just in time). De är mycket användbara eftersom du inte behöver använda någon av dina UTXO: er, du kan betala öppningskanalen med medel som du redan har i andra LN plånböcker, stapla och förbereda dem för att en större kanal ska öppnas. Du bör använda dessa JIT-kanaler till din fördel. [Jag har förklarat i den här guiden](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) fler alternativ för kamrater för privata noder som Blixt. Också [här i den här guiden publicerad på SN](https://stacker.news/items/679242/r/DarthCoin) Jag förklarade hur man hanterar likviditeten för privata mobilnoder.


---

## Slutsats


OK, det finns många andra fantastiska funktioner som Blixt erbjuder, jag kommer att låta dig upptäcka dem en efter en och ha kul.


Den här appen är verkligen underskattad, främst för att den inte stöds av någon VC-finansiering, är samhällsdriven, byggd med kärlek och passion för Bitcoin och Lightning Network.


Den här mobila LN-noden, Blixt, är ett mycket kraftfullt verktyg i händerna på många användare, om de vet hur man använder det på rätt sätt. Tänk dig att du går runt i världen med en LN-nod i din egen ficka och ingen kommer att veta det.


Och jag pratar inte om alla andra rika funktioner som följer med, som mycket få eller inga andra Wallet-appar kan erbjuda.


Under tiden finns här alla länkar om denna fantastiska Bitcoin Lightning Node:



- [Blixt officiella hemsida](https://blixtwallet.com/)
- [Blixt Github-sida] (https://github.com/hsjoberg/blixt-Wallet/)
- [Blixt Features page](https://blixtwallet.github.io/features) - förklarar en efter en varje egenskap och funktionalitet.
- [Blixt FAQ-sida](https://blixtwallet.github.io/faq) - Lista över frågor och svar och felsökning av Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demos, videohandledning, extra guider och användningsfall för Blixt
- Ladda ner: [Android Play Store] (https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS] (https://testflight.apple.com/join/EXvGhRzS) | [APK direkt nedladdning] (https://github.com/hsjoberg/blixt-Wallet/releases)
- [Telegramgrupp för direkt stöd] (https://t.me/blixtwallet)
- [Twitter] (https://twitter.com/BlixtWallet)
- [Geyser crowdfunding-sida] (https://geyser.fund/project/blixt) - donera Sats som du vill för att stödja projektet
- [LNURL Chatt Blixt](https://chat.blixtwallet.com/) - anonym LN chatt
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - promovideo (du kan testa din 1:a användning av LN)
- [A4-flyer med första stegen i användningen av Blixt, på olika språk] (https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt erbjuder också en fullt fungerande demo](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) direkt på sin webbplats eller på en dedikerad version webb, för att få en fullständig erfarenhetstestning innan du börjar använda i den verkliga världen.


---
**DISCLAIMER:**


*Jag får inte betalt eller stöd på något sätt av utvecklarna av den här appen. Jag skrev den här guiden eftersom jag såg att intresset för den här Wallet-appen ökar och nya användare fortfarande inte förstår hur man börjar med den. Också för att hjälpa Hampus (huvudutvecklaren) med dokumentation om hur man använder den här noden Wallet.*


*Jag har inget annat intresse av att marknadsföra denna LN-app, förutom att driva på antagandet av Bitcoin och LN. Detta är det enda sättet!


---