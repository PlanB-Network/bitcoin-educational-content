---
name: Aqua
description: Bitcoin, Lightning och Liquid i en enda Wallet
---
![cover](assets/cover.webp)


Aqua är en mobilapplikation som gör det enkelt att skapa en Hot Wallet för Bitcoin och Liquid, och erbjuder också möjligheten att använda Lightning utan komplexiteten i att hantera en nod, tack vare integrerade swappar. Det gör det också möjligt att hantera USDT-stablecoins på olika nätverk.


Aqua-appen utvecklades av JAN3-företaget under ledning av Samson Mow och utformades ursprungligen specifikt för behoven hos användare i Latinamerika, även om den är lämplig för alla användare över hela världen. Den är särskilt intressant för nybörjare och för dem som dagligen använder Bitcoin för sina betalningar.


I den här handledningen ska vi ta reda på hur man använder Aqua:s många funktioner. Men innan vi gör det, låt oss ta en stund att förstå vad en Sidechain är på Bitcoin och hur Liquid fungerar, så att vi fullt ut kan förstå värdet av Aqua.


![AQUA](assets/fr/01.webp)


## Vad är en Sidechain?


Bitcoin-protokollet har avsiktliga tekniska begränsningar som bidrar till att upprätthålla nätverkets decentralisering och säkerställa att säkerheten fördelas mellan alla användare. Dessa begränsningar kan dock ibland frustrera användare, särskilt under överbelastning på grund av en hög volym av samtidiga transaktioner. Debatten om Bitcoin:s skalbarhet har länge delat gemenskapen, särskilt under Blocksize War. Sedan denna episod är det allmänt erkänt inom Bitcoin-communityn att skalbarhet måste säkerställas genom off-chain-lösningar på andra Layer-system. Dessa lösningar inkluderar sidokedjor, som fortfarande är relativt okända och lite använda jämfört med andra system som Lightning Network.


En Sidechain är en oberoende Blockchain som fungerar parallellt med den huvudsakliga Bitcoin Blockchain. Den använder Bitcoin som en kontoenhet, tack vare en mekanism som kallas "*two-way peg*". Detta system gör det möjligt att låsa bitcoins på huvudkedjan för att reproducera deras värde på Sidechain, där de cirkulerar i form av tokens som backas upp av de ursprungliga bitcoins. Dessa tokens behåller normalt samma värde som de bitcoins som är låsta på huvudkedjan, och processen kan vändas för att återfå medel på Bitcoin.


Syftet med sidokedjor är att erbjuda ytterligare funktioner eller tekniska förbättringar, t.ex. snabbare transaktioner, lägre avgifter eller stöd för smarta kontrakt. Dessa innovationer kan inte alltid implementeras direkt på Bitcoin Blockchain utan att äventyra dess decentralisering eller säkerhet. Sidokedjor gör det därför möjligt att testa och utforska nya lösningar samtidigt som Bitcoin:s integritet bevaras. Dessa protokoll kräver dock ofta kompromisser, särskilt när det gäller decentralisering och säkerhet, beroende på vilken styrmodell och konsensusmekanism som väljs.


## Vad är Liquid?


Liquid är en federerad Sidechain-överlagring för Bitcoin, utvecklad av Blockstream för att förbättra transaktionshastighet, integritet och funktionalitet. Den använder en bilateral förankringsmekanism etablerad på en federation för att låsa bitcoins på huvudkedjan och skapa Liquid-bitcoins (L-BTC) i gengäld, tokens som cirkulerar på Liquid medan de förblir uppbackade av de ursprungliga bitcoins.


![AQUA](assets/fr/02.webp)


Liquid Network förlitar sig på en federation av deltagare, bestående av erkända enheter från Bitcoin-ekosystemet, som validerar block och hanterar bilateral pegging. Förutom L-BTC möjliggör Liquid även utgivning av andra digitala tillgångar, såsom USDT stablecoin och andra kryptovalutor.


![AQUA](assets/fr/03.webp)


## Installera Aqua-applikationen


Det första steget är naturligtvis att ladda ner Aqua-applikationen. Gå till din applikationsbutik:



- [För Android] (https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [För Apple] (https://apps.apple.com/us/app/Aqua-Wallet/id6468594241).

![AQUA](assets/fr/04.webp)


För Android-användare har du också möjlighet att installera applikationen via filen `.apk` [tillgänglig på deras GitHub] (https://github.com/AquaWallet/Aqua-Wallet/releases).


![AQUA](assets/fr/05.webp)


Starta programmet och kryssa sedan i rutan "*Jag har läst och godkänt användarvillkoren och sekretesspolicyn*".


![AQUA](assets/fr/06.webp)


## Skapa din Wallet på Aqua


Klicka på knappen "*Create Wallet*".


![AQUA](assets/fr/07.webp)


Och voilà, din Wallet är redan skapad!


![AQUA](assets/fr/08.webp)


Men först och främst, eftersom detta är en självförvarad Wallet, är det absolut nödvändigt att göra en fysisk säkerhetskopia av din Mnemonic. **Den här Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins**. Vem som helst som har denna Mnemonic kan stjäla dina pengar, även utan fysisk tillgång till din telefon.


Det gör att du kan återställa åtkomsten till dina bitcoins i händelse av förlust, stöld eller sönderslagning av din telefon. Det är därför mycket viktigt att spara det noggrant på ett fysiskt medium (inte digitalt) och förvara det på en säker plats. Du kan skriva ner det på ett papper, eller för extra säkerhet, om detta är en stor Wallet, skulle jag rekommendera att gravera det på ett rostfritt stålstöd för att skydda det från risken för brand, översvämning eller kollaps (för en Hot Wallet som är utformad för att säkra en liten mängd bitcoins är en enkel pappersbackup förmodligen tillräcklig).


Detta gör du genom att klicka på menyn Inställningar.


![AQUA](assets/fr/09.webp)


Klicka sedan på "*Visa seed-fras*". Gör en fysisk säkerhetskopia av denna 12-ordsfras.


![AQUA](assets/fr/10.webp)


I samma inställningsmeny kan du också ändra programspråket och den fiat-valuta som används.


![AQUA](assets/fr/11.webp)


Innan du får dina första bitcoins i din Wallet, ** rekommenderar jag starkt att du utför ett tomt återställningstest**. Anteckna viss referensinformation, till exempel din xpub eller första mottagande Address, och radera sedan din Wallet i Aqua-appen medan den fortfarande är tom. Försök sedan återställa din Wallet på Aqua med hjälp av dina pappersbackuper. Kontrollera att cookieinformationen som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga. Om du vill veta mer om hur du utför en teståterställning kan du läsa den här andra handledningen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Du kan inte se det på min skärm eftersom jag använder en emulator, men i inställningarna hittar du ett alternativ för att låsa appen med ett biometriskt autentiseringssystem. Jag rekommenderar starkt att du aktiverar den här säkerhetsfunktionen eftersom vem som helst som har tillgång till din olåsta telefon utan den kan stjäla dina bitcoins. Du kan använda Face ID på iOS eller ditt fingeravtryck på Android. Om dessa metoder misslyckas under autentiseringen kan du fortfarande komma åt appen med hjälp av telefonens PIN-kod.


## Ta emot bitcoins på Aqua


Nu när din Wallet är konfigurerad är du redo att ta emot din första Sats! Klicka helt enkelt på knappen "*Receive*" i menyn "*Wallet*".


![AQUA](assets/fr/12.webp)


Du kan välja att ta emot bitcoins på kedjan, på Liquid eller via Lightning.


![AQUA](assets/fr/13.webp)


För onchain-transaktioner kommer Aqua att generate en specifik mottagande Address där du kan ta emot din Sats.


![AQUA](assets/fr/14.webp)


På samma sätt, genom att välja Liquid, kommer Aqua att ge dig en Liquid Address.


![AQUA](assets/fr/15.webp)


Om du föredrar att ta emot pengar via Lightning måste du först ange önskat belopp.


![AQUA](assets/fr/16.webp)


Klicka sedan på "*generate Invoice*".


![AQUA](assets/fr/17.webp)


Aqua kommer att skapa en Invoice för att ta emot pengar från en Lightning Wallet. Observera att till skillnad från alternativen onchain och Liquid kommer medel som tas emot via Lightning automatiskt att konverteras till L-BTC på Liquid med hjälp av Boltz-verktyget, eftersom Aqua inte är en Lightning-nod. Den här processen gör att du kan ta emot och skicka pengar via Lightning, men utan att någonsin lagra dina bitcoins på Lightning.


![AQUA](assets/fr/18.webp)


Personligen kommer jag att börja med att skicka bitcoins via Lightning till Aqua. När transaktionen har slutförts med den Invoice som tillhandahålls får vi en bekräftelse.


![AQUA](assets/fr/19.webp)


För att följa bytets utveckling, gå tillbaka till din Wallet:s hemsida och klicka på kontot "*L2 Bitcoin*", som listar Lightning (via byte) och Liquid-transaktioner.


![AQUA](assets/fr/20.webp)


Här kan du se din transaktion och ditt L-BTC-saldo.


![AQUA](assets/fr/21.webp)


## Bitcoin byter till Aqua


Nu när du har tillgångar i din Aqua Wallet kan du byta ut dem direkt från appen, antingen för att överföra dem till huvud Bitcoin Blockchain eller till Liquid. Du kan också konvertera dina bitcoins till USDT stablecoin (eller andra). För att göra det, gå till menyn "*Marketplace*".


![AQUA](assets/fr/22.webp)


Klicka på "*Swaps*".


![AQUA](assets/fr/23.webp)


I rutan "*Överför från*" väljer du den tillgång du vill handla med. För närvarande äger jag bara L-BTC, så det är vad jag väljer.


![AQUA](assets/fr/24.webp)


I rutan "*Transfer to*" väljer du måltillgången för ditt byte. För min del valde jag USDT på Liquid Network.


![AQUA](assets/fr/25.webp)


Ange det belopp som du vill konvertera.


![AQUA](assets/fr/26.webp)


Bekräfta genom att klicka på "*Fortsätt*".


![AQUA](assets/fr/27.webp)


Kontrollera att du är nöjd med inställningarna för bytet och bekräfta sedan genom att dra i knappen "*Swap*" längst ned på skärmen.


![AQUA](assets/fr/28.webp)


Ditt byte är nu bekräftat.


![AQUA](assets/fr/29.webp)


När vi tittar tillbaka på vår Wallet kan vi se att vi nu har USDT på Liquid.


![AQUA](assets/fr/30.webp)


## Skicka bitcoins med Aqua


Nu när du har bitcoins i din Aqua Wallet kan du skicka dem. Klicka på knappen "*Sänd*".


![AQUA](assets/fr/31.webp)


Välj den tillgång du vill skicka eller välj det nätverk som ska utföra transaktionen. För min del kommer jag att skicka bitcoins via Lightning.


![AQUA](assets/fr/32.webp)


Därefter anger du den information som behövs för att skicka betalningen: för onchain- eller Liquid-bitcoins måste du ange en mottagande Address; för Lightning krävs en Invoice. Du kan klistra in den här informationen direkt i fältet eller använda QR-kodikonen för att öppna din kamera och skanna Address eller Invoice. Klicka sedan på "*Fortsätt*".


![AQUA](assets/fr/33.webp)


Klicka på "*Continue*" igen om all information verkar korrekt.


![AQUA](assets/fr/34.webp)


Aqua ger dig sedan en sammanfattning av transaktionen. Kontrollera att all information är korrekt, inklusive destinationen Address, avgifter och belopp. För att bekräfta transaktionen, skjut på knappen "*Slide to send*" längst ned på skärmen.


![AQUA](assets/fr/35.webp)


Du kommer sedan att få en bekräftelse på försändelsen.


![AQUA](assets/fr/36.webp)


Så nu vet du hur du använder Aqua-appen för att ta emot och spendera pengar på Bitcoin, Lightning och Liquid, allt från en enda Interface.


Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du kollar in den här andra omfattande handledningen om Blockstream Green-mobilappen, som är en annan intressant lösning för att ställa in din Liquid Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a