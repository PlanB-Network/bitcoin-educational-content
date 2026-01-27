---
name: Konfigurera din första Lightning-nod
goal: Förstå, installera, konfigurera och använda en Lightning-nod
objectives: 


  - Förstå rollen och syftet med en Lightning-nod.
  - Identifiera de olika programvarulösningar som finns tillgängliga.
  - Installera och konfigurera en Lightning-nod (LND).
  - Anslut ett utgiftskonto.
  - Känn till riskerna med att använda en Lightning-nod.


---

# Ditt första steg mot autonomi på Lightning



Du har redan förvärvat din första sats, säkrat dina självförvarade medel och distribuerat en Bitcoin-nod för att vara suverän i din on-chain-användning. Nästa steg är att få samma autonomi på Lightning: det är just syftet med den här kursen.



LNP202 riktar sig till användare på mellannivå och guidar dig steg för steg genom driftsättningen av din första Lightning-nod, utan avancerade tekniska färdigheter.



Du får lära dig hur du installerar LND på Umbrel, öppnar och hanterar dina kanaler, övervakar din nod och ansluter en mobil wallet, så att du kan njuta av en upplevelse som kan jämföras med den hos en depå wallet, samtidigt som du behåller total kontroll över dina fonder.



+++


# Inledning


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Kursöversikt


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 är en praktisk kurs som är utformad för att göra dig autonom på Lightning genom att driva din egen nod. Målet är enkelt: börja med en Bitcoin-nod som redan finns på plats, distribuera LND på Umbrel, säkra den ordentligt, öppna och hantera dina första kanaler och använd sedan din nod dagligen från en mobil wallet. Den här kursen förutsätter att du redan har tagit BTC 202, eftersom jag antar att din Bitcoin-nod på Umbrel är på plats och synkroniserad. Vi kommer inte att gå tillbaka till hur man sätter upp en Bitcoin-nod här.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

För en bättre förståelse av Lightnings interna mekanik rekommenderas också kursen LNP 201, även om den inte är ett förkunskapskrav för den här kursen:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

I den första delen av denna LNP202-kurs tar vi en titt på vad en Lightning-nod egentligen är, hur den skiljer sig från en enkel wallet och varför en personlig nod är det enda sättet att använda Lightning utan att delegera din sats till en betrodd tredje part. Avsnittet avslutas med ett strategiskt val: vilken lösning är rätt för dig, från de enklaste tillvägagångssätten till den klassiska Lightning-noden, den som vi kommer att implementera i den här kursen.



I del 2 av kursen installerar du LND på Umbrel och sätter sedan på plats de element som förhindrar de mest kostsamma misstagen: en realistisk backup-strategi och skydd mot fusk via ett vakttorn. När dessa grunder är på plats öppnar du din första kanal, så att du kan börja betala på Lightning med din egen infrastruktur.



Så du förstår: i den här LNP202-kursen kommer vi att konfigurera en Lightning-nod i plug-and-play-läge via Umbrel, snarare än den klassiska kommandoradsstrategin, för att göra den lämplig för mellanliggande användare. Om du föredrar en kommandoradsinstallation rekommenderar jag att du följer handledningen nedan. Andra, mer avancerade, kommandoradsorienterade Lightning-kurser är också under förberedelse.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Del 3 tar dig sedan från en nod som fungerar till en som du vet hur du ska kontrollera. Du börjar med att bestämma din Lightning-nods operatörsprofil (konsument, handlare eller router) och tar sedan itu med ett komplett programvarupaket för hantering för att spåra dina kanaler och agera rent på din topologi. Slutligen kommer du att ta itu med en mycket viktig Lightning-punkt: hur man får inkommande likviditet, oavsett om det är via betalda eller kooperativa lösningar.



Del 4 kommer att fokusera på vardaglig användning. Du kommer att sätta upp en anslutning mellan din nod och en mobilkund, så att du kan betala och hämta ut pengar helt enkelt från din smartphone, utan att ge upp egenvården. Vi tittar först på en nätverksstrategi via *Tailscale*, sedan på en protokollstrategi via *Nostr Wallet Connect*, med deras respektive fördelar och avvägningar. Kursen avslutas med ett slutkapitel som ger dig rätt vanor för att upprätthålla din självbevarelsedrift, både operativt och pedagogiskt.



Om du följer den här LNP202-kursen i rätt ordning kommer du i slutet av den att ha en komplett konfiguration för din Lightning-nod, funktionell för daglig användning och framför allt under kontroll.




## Förståelse för Lightning-noder


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Innan du startar din egen nod går vi i det här kapitlet kort igenom den grundläggande teorin bakom Lightning Network. Det är verkligen viktigt att förstå de mekanismer som är inblandade, eftersom detta gör det möjligt för dig att identifiera risker och anta god praxis för att begränsa dem. Jag kommer dock inte att gå in i detalj här, eftersom det inte är huvudsyftet med den här kursen. Om du vill gå djupare in i ämnet rekommenderar jag starkt att du läser Fanis Michalakis LNP 201-kurs, som är en referens inom området:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Vad är en Lightning-nod?



Låt oss gå tillbaka till grunderna: innan vi definierar vad en nod är, måste vi förstå vad Lightning Network är. Det är ett toppskiktsprotokoll, byggt ovanpå Bitcoin, utformat för att möjliggöra BTC-transaktioner utanför kedjan som är snabba (med nästan omedelbar slutgiltighet) och i allmänhet billiga. "Offchain" innebär att transaktioner som utförs på Lightning inte är avsedda att visas på Bitcoin:s huvudsakliga blockkedja. Lightning är också ett partiellt svar på den ökande användningen av Bitcoin och på trängsel i onchain, vilket väcker oro för systemets skalbarhet.



För att fungera förlitar sig Lightning på att betalningskanaler öppnas mellan deltagarna, inom vilka transaktioner kan genomföras nästan omedelbart, ofta med minimala avgifter, utan att de behöver registreras en efter en på Bitcoin-blockkedjan. Dessa kanaler kan förbli öppna under mycket lång tid och kräver endast transaktioner i kedjan när de öppnas och stängs.



En Lightning-nod är en deltagare i Lightning-nätverket, som öppnar kanaler och gör betalningar med andra noder. Konkret är en Lightning-nod en mjukvara som körs på en dator och som implementerar Lightning Network-protokollet. Exempel på detta är LND, Core Lightning eller Eclair. Den här programvarans huvudsakliga roll är att:




- ansluta till en Bitcoin-nod för att få information från huvudblockkedjan;
- skapa och hantera dubbelriktade betalningskanaler med andra noder;
- utbyta meddelanden med hela Lightning-nätverket.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: en viktig distinktion



På Bitcoin (onchain) hänvisar "*wallet*" till programvara som hanterar dina privata nycklar, beräknar ditt saldo från dina UTXO och bygger dina transaktioner. Denna wallet kan vara baserad på din egen Bitcoin-nod eller på någon annans, men idag är nodens roll och rollen för wallet i kedjan tydligt åtskilda.



På Lightning är det svårare att återanvända den här typen av vokabulär utan att skapa förvirring. Termen "*Lightning wallet*" är ganska vag, eftersom det i verkligheten inte finns något sådant som en verkligt självförvaltande Lightning wallet, såvida den inte är baserad på en nod. Endast två situationer är därför möjliga:



- För att ha en riktig Lightning-nod (dvs. icke-frihetsberövande): den programvara du använder (t.ex. en mobilapp som Phoenix eller en LND-instans på Umbrel) kör faktiskt en nod, och du har faktiskt nycklarna för att hämta dina bitcoins. I det här fallet är din "*Lightning wallet*" egentligen bara ett användargränssnitt ovanpå en Lightning-nod, oavsett om den är inbäddad eller fjärrstyrd.



- Att använda en depåtjänst: du använder en applikation som visar dig ett saldo i sats på Lightning, men i bakgrunden finns medlen på en leverantörs nod (t.ex. Wallet of Satoshi). Du har varken nycklar eller kontroll över kanalerna. Ditt saldo är bara en bokföringspost i företagets databas. Det är jämförbart med att lämna dina bitcoins på en utbytesplattform, med alla tillhörande risker. I det här fallet är din "*Lightning wallet*" bara en tillgång till ett konto som hanteras av en operatör som i sin tur driver en riktig Lightning-nod.



Så det finns inget mellanting när det gäller Lightning: antingen har du en nod (även en inbäddad sådan) så att du är i egen vårdnad, eller så har du inte det, så att ett företag äger din sats. Men som vi kommer att se i de följande kapitlen kan dessa två användningsområden ibland vara svåra att skilja åt. Phoenix är till exempel en mobilapplikation som innehåller en riktig Lightning-nod, men användaren är inte nödvändigtvis medveten om det, eftersom den fullständiga komplexiteten i dess funktion är nästan helt dold.



### En påminnelse om hur Lightning Network fungerar



I det här avsnittet ska jag ge dig en snabb påminnelse om hur Lightning fungerar. Återigen, om du vill ha en mer djupgående presentation av de teoretiska begreppen, uppmanar jag dig att ta en titt på den dedikerade LNP 201-kursen.



#### Betalningskanaler: öppna, uppdatera och stänga



Kärnan i Lightning-nätverket är baserat på dubbelriktade betalningskanaler. En kanal kan öppnas (d.v.s. skapas), uppdateras när Lightning-transaktioner äger rum och sedan slutligen stängas. Ur onchain-synvinkel är en kanal inget annat än en 2/2 multisignaturutgång.



![Image](assets/fr/002.webp)



Ur Lightnings synvinkel är det en betalningskanal med likviditet som delas mellan de två deltagarna.



![Image](assets/fr/003.webp)





- Öppna en kanal:**



Två noder bestämmer sig för att öppna en kanal. En av dem överför bitcoins i en transaktion i kedjan som kallas *finansieringstransaktion*. Denna transaktion skapar en utgång baserad på ett 2-av-2 multisignaturskript, vilket innebär att spendera dessa medel på Bitcoin kräver signatur från båda noderna i kanalen. Innan den här transaktionen utfärdas ber den part som tillhandahåller medlen den andra att underteckna en *uttagstransaktion*, som inte utfärdas på kedjan, men som gör det möjligt för den att återfå sina medel i händelse av problem.



![Image](assets/fr/004.webp)





- Commitment transaktioner:**



Kanalens tillstånd (dvs. fördelningen av sats mellan A och B) representeras av en *commitment transaction*, som är känd för båda noderna men som inte omedelbart sänds ut på blockkedjan. Denna transaktion beskriver hur kanalens medel ska omfördelas på kedjan enligt de betalningar som gjorts på Lightning.



Vid varje Lightning-betalning signerar de två noderna ett nytt tillstånd som ersätter det tidigare. Det gamla tillståndet återkallas tack vare en mekanism med återkallningsnyckel: om en av deltagarna försöker sända ett gammalt tillstånd kan den andra återfå hela beloppet som straff.



Den viktiga idén här är att det alltid finns en signerad Bitcoin-transaktion, som inte sänds ut i kedjan, som bevaras av noderna och som möjliggör omfördelning av varandras sats enligt de betalningar som gjorts på Lightning Network.



![Image](assets/fr/005.webp)





- Stängning av kanal:**



En kanal kan stängas rent via en kooperativ stängning, när båda parter är överens om kanalens slutliga tillstånd, eller ensidigt (en påtvingad stängning) om en av deltagarna upphör att samarbeta eller blir oåtkomlig. I samtliga fall sker stängningen i form av en onchain-transaktion som spenderar 2/2-utgången och fördelar pengarna mellan deltagarna enligt kanalens senast giltiga tillstånd.



![Image](assets/fr/006.webp)



Lightning fungerar därmed som ett sekundärt lager förankrat på Bitcoin: endast vissa händelser (öppning och stängning av kanaler) visas på huvudblockkedjan. Mellanliggande betalningar förblir utanför kedjan.



Innan vi går vidare, här är två viktiga begrepp för att förstå hur man hanterar en Lightning-kanal:




- Liquidity*: den mängd sats som finns tillgänglig på ena sidan av kanalen;
- *Kapacitet*: det är det totala belopp som är låst i 2/2 multisig-utgången, dvs. summan av likviditeten på båda sidor av kanalen.



#### Ett nätverk av kanaler och likviditet



En kanal är inte bara till för betalningar mellan två noder: den är en del av ett globalt nätverk av sammankopplade kanaler. Din nod kan dirigera betalningar för andra användare genom sina egna kanaler, och du kan skicka sats till en Lightning-nod som du inte har någon direkt kanal med, så länge som en giltig väg kan hittas mellan dina två noder.



Varje nod känner, via skvallerprotokollet, till en karta över detta nätverk: vilka kanaler som finns, vilka noder som är anslutna med en dubbelriktad kanal och vilka kapaciteter som är publicerade. För att skicka en betalning till en mottagare utan en direktkanal beräknar din nod en rutt som består av flera hopp: din nod → nod X → nod Y → mottagarnod. Vid varje hopp passerar betalningen en kanal som måste ha tillräcklig likviditet i betalningsriktningen.



![Image](assets/fr/007.webp)



Likviditeten i en kanal är därför inte symmetrisk: den ena sidan kan vara tungt belastad, medan den andra är nästan tom. Att hantera denna likviditet, dvs. att veta var sats finns och i vilken riktning de kan flöda, är en av de viktigaste aspekterna av driften av en Lightning-nod. Vi kommer att titta närmare på det i de praktiska kapitlen framöver.



#### HTLC: transportera betalning utan att bli rånad



För att möjliggöra att betalningar kan passera mellanliggande noder utan behov av förtroende använder Lightning smarta kontrakt som kallas *HTLC* (*Hashed Time-Locked Contracts*). Enkelt uttryckt gör ett HTLC överföringen av pengar beroende av att en hemlighet avslöjas och innehåller en tidsbegränsning för att skydda avsändaren i händelse av att transaktionen misslyckas. Varje betalning är därför beroende av att en förbild (en hemlighet vars hash motsvarar ett överenskommet värde) presenteras. Om den slutliga mottagaren tillhandahåller denna förbild kan han eller hon göra anspråk på medlen, vilket i sin tur gör det möjligt för varje mellanliggande nod att återfå sina egna medel.



![Image](assets/fr/008.webp)



Jag ska bespara dig de tekniska detaljerna om hur HTLC fungerar, eftersom de inte är väsentliga för syftet med denna kurs. Du hittar en djupgående förklaring i teorikursen LNP 201. Kom bara ihåg att HTLC möjliggör atomära utbyten: antingen är överföringen klar och ingen skadas i routingen, eller så misslyckas den och varje deltagare återfår sina initiala medel. Det finns inget mellanting.



### De viktigaste implementationerna av Lightning-noden



Precis som med Bitcoin finns det flera implementeringar av Lightning-protokollet. Ett antal oberoende team utvecklar sina egna versioner, som alla är driftskompatibla eftersom de följer samma specifikationer (BOLT:erna). Här är de viktigaste implementationerna som används idag.



#### LND (*Lightning Network Daemon*)



LND är en komplett implementation av Lightning-protokollet, skriven i Go och utvecklad av Lightning Labs.



![Image](assets/fr/009.webp)



#### Core Lightning (*CLN*)



Core Lightning (tidigare *C-Lightning*) är den implementation som utvecklats av Blockstream. Den är skriven i C, med vissa komponenter i Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair är en implementation skriven i Scala och utvecklad av det franska företaget ACINQ. ACINQ driver en av de viktigaste routingnoderna i Lightning-nätverket med Eclair och använder denna implementation som mjukvarubas för sina egna produkter, till exempel applikationen Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) är ett utvecklingskit för Rust som underhålls av Spiral (Block, ex-Square). Det är inte en färdig daemon som LND eller CLN, utan ett bibliotek för utvecklare som vill integrera Lightning direkt i sina applikationer.



![Image](assets/fr/012.webp)



I den här LNP202-kursen kommer vi främst att koncentrera oss på LND: den implementering som oftast används i nyckelfärdiga lösningar för privatkunder, till exempel Umbrel.



Så mycket för denna korta påminnelse om hur Lightning fungerar. Återigen, om det finns några begrepp som du inte förstår, eller om du vill fördjupa dig lite innan du omsätter dem i praktiken, är Fanis Michalakis kurs den viktigaste referensen i ämnet:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Varför driva en egen Lightning-nod?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Det är ganska enkelt att svara på den här frågan, eftersom den är retorisk: utan en egen nod använder du inte längre Lightning på riktigt, utan bara illusionen av Lightning över ett företags infrastruktur.



Att använda en Lightning custodial wallet innebär att bitcoins tekniskt sett tillhör det företag som driver noden. Du har inte de privata nycklarna och du kontrollerar inte kanalerna. Ditt wallet-saldo är bara en rad i en tjänsteleverantörs databas. Denna situation är förvisso mycket bekväm för nybörjare, och användarupplevelsen är ofta flytande, men den grundläggande frågan är: vad är fördelen med att använda Bitcoin och Lightning om du i slutändan avstår från just de aspekter som skiljer dem från traditionella valutor och banker?



Bitcoin:s två huvudsakliga värdeförslag är monetär suveränitet (att inte längre vara beroende av en central myndighet för utgivning och innehav) och censurmotstånd (omöjligheten för en tredje part att förhindra eller filtrera betalningar). Ett förvaringssystem på Lightning går direkt mot båda dessa mål: du kan inte kontrollera plattformens interna penningmängd, och per definition kan en operatör som innehar alla medel och alla kanaler censurera, försena, prioritera eller blockera dina betalningar. Under dessa förhållanden kan vi legitimt fråga oss själva: **Vad är poängen med att använda bitcoin via Lightning om det kommer att reproducera samma mönster av tillit och beroende som med traditionella statliga valutasystem**.



> Vad som behövs är ett elektroniskt betalningssystem som bygger på kryptografiska bevis i stället för förtroende, vilket gör det möjligt för två villiga parter att handla direkt med varandra utan att det behövs en betrodd tredje part.
*Satoshi Nakamoto, Bitcoin Vitbok


Bortsett från filosofin är de mer konkreta nackdelarna för dig följande. För det första har du inget sätt att verifiera att företaget faktiskt innehar de bitcoins som motsvarar de saldon som visas. Det kan fungera med fraktionerad reserv, bli hackat, gå i konkurs eller helt enkelt försvinna. I det här fallet är du bara en annan borgenär, utan någon verklig garanti för att du får tillbaka dina pengar.



För det andra är företaget föremål för regleringsrisker: förelägganden, frysning av medel, begäran om att blockera användare eller transaktioner, förstärkt övervakning eller till och med direkt förbud mot verksamhet i vissa jurisdiktioner. Varje begränsning som tynger tjänsteleverantören återspeglas mekaniskt på dig.



När det gäller sekretess är situationen inte bättre. En depåoperatör ser alla dina flöden: belopp, frekvenser, mottagare, saldon, utgiftsvanor. I kombination med information som tillhandahålls av applikationen och eventuellt den underliggande kedjeanalysen på Bitcoin kan denna information ge en mycket exakt profil av din finansiella aktivitet. Återigen är det långt ifrån Bitcoin:s mål att minska den finansiella övervakningen.



Den goda nyheten är att det idag inte längre är förbehållet tekniska experter att driva en egen Lightning-nod, vilket det kan ha varit i slutet av 2010-talet. Det finns relativt enkla lösningar för hemanvändare, som vi kommer att förklara i detalj i nästa kapitel.




## Välja rätt lösning för jobbet


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Idag är det möjligt att ha en användarupplevelse som ligger mycket nära den för en Lightning custodial wallet, samtidigt som man förblir i egen vårdnad. Syftet med det här kapitlet är att hjälpa dig att välja den väg som passar din profil bäst.



### Alternativ 1: Använd inte Lightning direkt



Den första lösningen är helt enkelt att inte använda Lightning nativt, utan att använda en Bitcoin eller Liquid wallet som innehåller atomic swaps. Till exempel använder Aqua- eller Bull Bitcoin Wallet-applikationer den här metoden genom att göra det möjligt för dig att betala Lightning-fakturor utan att själv driva en Lightning-nod, samtidigt som du förblir i självförvar.



Principen är enkel: dina medel finns i Bitcoin, antingen on-chain eller Liquid, och du får tillgång till dem via en wallet där du har nycklarna på traditionellt sätt. När du skannar en Lightning-faktura initierar din wallet en transaktion (on-chain eller Liquid) till en atomic swap-tjänst. Denna tjänst hanterar sedan Lightning-betalningen genom sin egen nod, med hjälp av de bitcoins du tillhandahöll on-chain eller via Liquid. Som ett resultat behöver du inte hantera några Lightning-kanaler själv, men du kan fortfarande betala Lightning-fakturor sömlöst.



![Image](assets/fr/013.webp)



Den stora fördelen med detta tillvägagångssätt, jämfört med en konventionell Lightning-depå wallet, är att du alltid har 100% kontroll över dina medel. Bitcoins finns i din onchain eller Liquid wallet, med din egen mnemoniska fras. Även under bytet förblir du i besittning av dina medel, eftersom bytet är atomärt. Den bygger på en kryptografisk mekanism som säkerställer att det bara finns två möjliga utfall: antingen lyckas bytet helt och hållet, eller så misslyckas det och tjänsten kan inte tillägna sig dina medel.



De flesta portföljer som erbjuder denna typ av funktionalitet förlitar sig på [Boltz](https://boltz.exchange/) för den tekniska delen av swappen.



Denna lösning erbjuder också intressanta fördelar när det gäller sekretess, särskilt i kombination med Liquid. För en nybörjare är det också mycket enkelt att konfigurera och spara: en klassisk minnesfras, inga kanaler, ingen likviditet att balansera...



Å andra sidan har detta tillvägagångssätt sina begränsningar. För det första är det inte oföränderligt: du är beroende av swapptjänstens tillgänglighet och goodwill. Om den inte längre vill behandla ditt konto eller upphör med sin verksamhet kan du inte längre betala blixtfakturor genom den. Sedan har vi de inte obetydliga avgifterna: du betalar både transaktionsavgifterna för onchain eller Liquid och swapservicens provision. Om onchain-avgifterna stiger kraftigt kan det också bli mycket dyrt att använda Lightning.



Så för tillfällig användning är det fortfarande acceptabelt, men för en mycket aktiv Lightning-användare är det bättre att göra saker rätt med en riktig Lightning-nod.



### Alternativ 2: Inbyggda Lightning-noder



Den andra kategorin av lösningar baseras på Lightning-noder som bäddas in direkt i en mobilapplikation. Phoenix Wallet var banbrytande i denna modell och är fortfarande ett riktmärke. Idag finns det andra projekt som erbjuder jämförbara metoder, till exempel Zeus (i inbäddat läge) eller BitKit.



Idén är enkel: applikationen kör faktiskt en Lightning-nod, men alla komplexa operationer hanteras automatiskt i bakgrunden. Du har ett "*Lightning wallet*"-gränssnitt med en minnesfras för säkerhetskopiering, du ser ett saldo och betalar fakturor, men du hanterar inte kanaler, likviditet eller de flesta parametrar.



![Image](assets/fr/014.webp)



Dessa lösningar är alltid självförvarade. Nycklarna som kontrollerar medlen är generated och lagras på din telefon, och säkerhetskopiering sker via en seed eller motsvarande mekanism. Du har inte bara ett konto hos en tjänsteleverantör, du äger faktiskt bitcoins som är låsta i kanaler som tillhör dig och inte kan stjälas.



Fördelarna med LN:s inbyggda noder är många:




- extremt lätt att installera och använda;
- användarupplevelse som ligger nära den för en förvaringsblixt wallet, men med egen förvaring;
- ingen manuell hantering av kanaler eller likviditet;
- relativt enkel säkerhetskopiering.



Men dessa inbäddade wallet har också betydande begränsningar. För det första, när det gäller sekretess, har tjänsteoperatören (t.ex. ACINQ i fallet med Phoenix) en ganska detaljerad bild av de flöden som passerar genom din nod: belopp, frekvenser, mottagare, även om detta kommer att förbättras, särskilt med det gradvisa antagandet av *Trampoline Nodes*. För det andra är du starkt beroende av denna operatör som din huvudsakliga Lightning-peer. Om ACINQ-noden blir otillgänglig (i fallet med Phoenix), om företaget utsätts för regulatoriskt tryck eller ändrar sin affärsmodell, kan din användarupplevelse försämras avsevärt eller till och med äventyras.



Slutligen kommer denna enkelhet till ett pris. Inbäddade LN-nodtjänster tar i allmänhet ut specifika avgifter på insättningar, uttag eller vissa kanalhanteringsoperationer. Enligt min mening är den här modellen vettig när det gäller den tjänst som erbjuds, men för intensiv användning kan den vara mycket dyrare än en välskött konventionell Lightning-nod.



### Alternativ 3: den klassiska Lightning-noden



Den tredje lösningen, den som vi kommer att titta närmare på i den här LNP202-kursen, är att driva en konventionell Lightning-nod på en dedikerad server eller enhet.



Med "klassisk" menar jag att du själv installerar och konfigurerar en Lightning-implementering (t.ex. LND) ovanpå din egen Bitcoin-nod. Du väljer dina peers, öppnar dina kanaler, hanterar din inkommande och utgående likviditet och ställer in dina policyer för routningsavgifter.



När det gäller suveränitet är det den bästa lösningen. Du är inte längre beroende av ett specifikt företag för dina kanaler eller betalningar: om en peer censurerar dig eller stänger en kanal kan du öppna en annan med en annan nod. Om en tjänst försvinner finns dina sats kvar i de kanaler du kontrollerar, och du kan ta hem dem i kedjan. Du kan också optimera dina långsiktiga kostnader: när dina kanaler är rätt dimensionerade och hanterade kan den totala kostnaden för betalningar bli mycket låg.



När det gäller sekretess är du självklart underkastad begränsningarna i Lightnings egen modell, men du lämnar inte över hela din verksamhet till en enda operatör.



Att sätta upp en klassisk Lightning-nod är däremot uppenbarligen mer komplext: du måste installera, konfigurera, underhålla, övervaka uppdateringar, förstå logiken i kanaler och avgiftspolicyer, hantera kanaler och kassaflöde, och så vidare. Felkonfiguration, slarvig säkerhetskopiering eller slarvig hantering kan lättare leda till att sats går förlorad. Noden måste också köras kontinuerligt.



Det är just den vägen jag föreslår att du följer i den här kursen, där jag följer med dig varje steg på vägen för att begränsa riskerna och strukturera din strategi.



### Vilken lösning för vilken användarprofil?



För att välja rätt lösning för din Lightning-användarprofil måste du ta hänsyn till två faktorer: hur ofta du använder Lightning och hur intresserad du är av teknisk hantering.



Om du inte gör många Lightning-betalningar ibland, men ändå vill kunna betala LN-fakturor från din telefon då och då, utan att ge upp självförvaltarskap: en Bitcoin eller Liquid wallet med swap-funktionalitet är förmodligen det bästa alternativet. Du behåller äganderätten till dina medel, hanterar inga noder och accepterar något högre avgifter i utbyte mot enkelhet.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Om du använder Lightning ganska regelbundet och vill ha fördelarna med en riktig nod, men inte vill lägga tid på att hantera kanaler, avgifter eller infrastruktur, är en mobil inbäddad Lightning-nod en bra lösning. Du behåller kontrollen över dina medel, UX förblir mycket tillgängligt och all komplexitet är dold, till priset av ett markant beroende av en operatör.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Om du är en medelgod eller avancerad användare, villig att investera tid i att förstå och hantera din infrastruktur och vill ha maximal kontroll över dina kanaler, likviditet och kostnader: en klassisk serverbaserad Lightning-nod är rätt väg att gå. Det är den mest krävande lösningen, men också den som är mest förenlig med Bitcoin:s idé om suveränitet.




# Skapa din första Lightning-nod


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Installera LND med Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Nu när vi har gått igenom grunderna i Lightning och de lösningar som finns tillgängliga är det dags att komma igång med arbetet. För att gå den här kursen behöver du en Bitcoin-nod som är synkroniserad med Umbrel. Den här kursen LNP202 är en fortsättning på BTC 202. Om du ännu inte har en Bitcoin-nod uppmanar jag dig att gå den här andra kursen och sedan komma tillbaka hit när din nod har synkroniserats. Jag rekommenderar starkt att du läser den, eftersom jag inte kommer att gå in i detalj på dess drift, konfiguration och säkerhetsåtgärder.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

I det här första kapitlet ska vi titta på hur du installerar LND på din Umbrel. Umbrel fungerar på ett sätt som gör det här steget mycket enkelt, eftersom allt du behöver göra är att installera ett program.



Från startsidan öppnar du `App Store` längst ner på gränssnittet.



![Image](assets/fr/015.webp)



I sökfältet skriver du in `Lightning Node` och klickar sedan på applikationen.



![Image](assets/fr/016.webp)



Klicka sedan på knappen `Install` för att starta installationen.



![Image](assets/fr/017.webp)



På startsidan klickar du på programmet för att öppna det och väljer sedan `Setup a new node`.



![Image](assets/fr/018.webp)



Du har fått en minnesfras på 24 ord. Förvara den på ett säkert ställe. I nästa kapitel ska vi titta närmare på hur du återfår åtkomsten till din Lightning-nod (det är en mycket mer komplex process än för en enkel Bitcoin wallet), men kom ihåg att den här frasen spelar en avgörande roll och måste sparas med största omsorg.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Spara den här frasen på samma sätt som en vanlig minnesfras: på ett fysiskt medium (papper eller metall) som förvaras på en säker plats, och klicka sedan på knappen `NEXT`.



![Image](assets/fr/019.webp)



Skriv sedan in orden i meningen för att kontrollera att du har skrivit ner dem korrekt.



![Image](assets/fr/020.webp)



Ett varningsmeddelande kommer att påminna dig om att applikationen är i betaversion och att Lightning Network fortfarande är en experimentell teknik. Självklart ska du aldrig binda belopp till din Lightning-nod som du inte är beredd att förlora.



Du kommer då till din Lightning-nods huvudgränssnitt. Till vänster hittar du din Bitcoin onchain wallet som finns på din nod. Det här är generated från den 24 ord långa fras som du just har sparat.



I mitten hittar du din Lightning wallet. Den representerar faktiskt dina utgående kontanter, dvs. de bitcoins du äger inom dina Lightning-kanaler.



Till höger ser du flera viktiga delar av informationen om din nod:




- Antalet anslutningar och öppna kanaler;
- Ditt totala utgående kassaflöde, dvs. vad du teoretiskt sett kan spendera på Lightning;
- Din totala inkommande likviditet, d.v.s. vad du teoretiskt kan ta emot på Lightning.



![Image](assets/fr/021.webp)



Låt oss börja med att anpassa vår nod. Klicka på de tre små prickarna längst upp till höger i gränssnittet och sedan på `Avancerade inställningar`. I undermenyn `Personalization` kan du definiera ett offentligt namn för din nod (undvik att använda ditt riktiga namn) och välja dess färg.



![Image](assets/fr/046.webp)



Klicka sedan på den gröna knappen `SAVE AND RESTART` för att starta om noden och tillämpa ändringarna.



Din Lightning-nod är nu redo att öppna sina första kanaler för att göra betalningar. Men först, låt oss ta en titt på hur du skyddar din sats!



## Spara din Lightning-nod


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Innan du skickar din första sats till din nod är det viktigt att förstå hur säkerhetskopieringen fungerar och vilka risker som är förknippade med den. Till skillnad från en enkel Bitcoin-portfölj på kedjan är det ganska komplicerat att säkerhetskopiera en Lightning-nod: fel strategi kan leda till permanent förlust av dina medel. I det här kapitlet tittar vi på vad som verkligen behöver säkerhetskopieras och hur Umbrel hanterar den här processen med LND.



I den här kursen kommer vi att använda implementeringen LND (*Lightning Network Daemon*). Även om principerna är liknande för de andra implementeringarna är de återställningsfiler och procedurer som jag kommer att prata om specifika för LND.



### Vad ska jag spara på en Lightning-nod?



På en Lightning-nod räcker det inte att spara seed och hoppas att allt ska återgå till det normala. Flera element spelar olika roller, så det är viktigt att skilja mellan dem.



#### seed (*aezeed*)



När du initierar LND får du en seed med 24 ord. Detta är ett LND-specifikt format som kallas "*aezeed*". Det är inte en klassisk seed BIP39, även om det ser ut som en sådan. Från denna seed härleder LND de privata nycklarna till din onchain wallet som är associerad med Lightning-noden, dvs. de adresser till vilka du kan ta emot eller till vilka du kan återföra bitcoins efter kanalstängningar.



![Image](assets/fr/019.webp)



Denna seed kan därför användas för att återskapa onchain wallet som är associerad med din nod, och för att hämta medel som redan har återförts onchain (t.ex. efter en kanalstängning). Å andra sidan är seed inte tillräckligt för att återställa dina Lightning-kanaler som fortfarande är öppna, eftersom den inte innehåller nödvändig information om dina kanalers status.



#### Kanalens databas (`channel.db`)



LND lagrar den detaljerade statusen för dina kanaler i en databas med namnet `channel.db`. Denna databas innehåller:




- listan över dina öppna kanaler;
- dina kollegor och deras identifierare;
- de sista commitment transaction för varje kanal (de successiva tillstånd som definierar vem som äger vad i kanalen och gör det möjligt att återfå medel i kedjan om det uppstår problem);
- den information som behövs för att straffa en peer som försöker sända ut en gammal rapport.



Problemet med den här databasen är att den ständigt förändras: varje betalning, varje routing, varje öppning eller stängning av en kanal ändrar dess innehåll. Det är därför en konventionell säkerhetskopia (t.ex. en periodisk kopia av din `channel.db`) är farlig. Om du återställer en för gammal version av `channel.db` och återmonterar noden med detta föråldrade tillstånd, kan dina peers anse att du sänder ett gammalt kanaltillstånd. I detta fall föreskriver protokollet en bestraffning: din peer kan återfå hela beloppet av kanalens medel, som om du hade försökt fuska.



I praktiken är alltså `channel.db` inte ett backup-medium i sig. Det är det levande tillståndet för din nod. Den enda situation där det är meningsfullt att använda den för att återställa noden är när du återställer databasen direkt från en maskin som just har gått sönder (t.ex. en disk som fortfarande är läsbar). I det här fallet återställer du det senaste tillståndet och kan starta om LND på en annan maskin baserat på den här databasen, i trygg förvissning om att det här tillståndet är så uppdaterat som möjligt eftersom den gamla maskinen inte längre körs. En annan situation där den här metoden kan fungera som en relevant säkerhetskopia är i en konfiguration med två diskar, med en dynamisk, permanent kopia från den ena till den andra. Denna typ av konfiguration är dock mer komplex att implementera.



Men att göra regelbundna kopior av `channel.db` och lagra dem som säkerhetskopior som ska återställas senare är en mycket dålig idé: den dag du använder dem riskerar du att straffa dig själv och förlora alla dina sats.



#### Säkerhetskopiering av statisk kanal (SCB)



För att göra katastrofåterställning möjlig har LND infört mekanismen *Static Channel Backup* (SCB). Detta är en speciell fil, ofta kallad `channel.backup`, som innehåller statisk information om dina kanaler: vilka dina kamrater är, hur du kontaktar dem och vilka dina kanaler är.



Den här filen innehåller inte detaljerad kanalstatus eller uppdateringshistorik. Det tillåter dig inte att öppna kanaler igen i exakt det tillstånd de var i, eller att fortsätta driva denna Lightning-nod. Snarare är dess roll att fungera som en ankarpunkt för att be dina kamrater att hjälpa dig att stänga alla dina kanaler rent och därmed få din sats onchain, på nycklar som du kan hämta tack vare seed. Så till skillnad från filen `channel.db`, som modifieras med varje betalning eller routing, uppdateras SCB-filen endast när en kanal öppnas eller stängs.



Vid återvinning via SCB är processen följande:




- Du återställer din seed (*aezeed*), som återskapar din wallet i kedjan som är associerad med Lightning-noden;
- Du förser LND med din senaste SCB;
- LND använder SCB för att hitta listan över dina kollegor och de kanaler du har med dem;
- Den kontaktar varje peer, berättar för dem att du har drabbats av en dataförlust och ber dem att "tvångsstänga" din kanal med dem, så att du kan återställa din onchain-andel.



Tanken är att dina kollegor, som märker att du rapporterar en förlust av data, kommer att sända sin sista commitment transaction och stänga force-kanalen. När dessa transaktioner har bekräftats dyker dina pengar upp igen i din onchain-portfölj (länkad till seed).



Denna återställningsmekanism är dock inte perfekt. För det första återställer den faktiskt inte din Lightning-nod, eftersom alla kanaler kommer att stängas. Du måste då bygga en ny Lightning-nod från grunden. För det andra garanterar det inte 100% återhämtning, även om det avsevärt ökar chanserna att återställa dina onchain-saldon i händelse av ett problem. Det här återställningsprotokollet är faktiskt beroende av dina kollegors samarbete och tillgänglighet: om en av dem är offline, har förlorat sina egna data eller vägrar att samarbeta kan dina medel förbli blockerade eller till och med gå förlorade permanent. Därför är det viktigt att inte hålla kanaler öppna på din Lightning-nod med oåtkomliga peers under långa tidsperioder. Om du drabbas av en dataförlust vid den tidpunkten och peern förblir onåbar kommer återhämtning via SCB att vara omöjlig, och dina pengar kommer att förbli förlorade tills peern kommer tillbaka online (kanske för alltid).



Sammanfattningsvis vilar en bra Lightning backup-strategi på LND på tre pelare:




- Din seed (*aezeed*), för onchain-lagret;
- Tillförlitlig automatisk SCB-backup;
- Bra kanalhantering genom att välja pålitliga motparter och i förebyggande syfte stänga de som ofta är omöjliga att nå.



### Hur hanterar Umbrel säkerhetskopieringen av din LND-nod?



Umbrel erbjuder en förenklad backup-mekanism för LND-noden, baserad just på SCB. Tanken är att bespara dig besväret med att manipulera den här filen själv, göra en säkerhetskopia av den och automatisera processen så långt det är möjligt.



När du skapar din nod på Umbrel får du en seed som spelar en dubbel roll:




- den härleder din Bitcoin på kedjan wallet som är associerad med din Lightning-nod;
- används för att härleda en backupidentifierare och krypteringsnyckel som används för fjärrbackuper av SCB.



Tack vare denna mekanism gör Umbrel automatiskt en krypterad säkerhetskopia av din SCB och lagrar den på sina servrar via Tor. SCB lagras krypterat tack vare en nyckel som härrör från din seed. Så i händelse av dataförlust är allt du behöver göra att återskapa en Bitcoin och Lightning-nod på Umbrel, på samma eller en annan maskin, och sedan ange din seed. Du kommer då att kunna hämta den senaste SCB-statusen från Umbrel-servrarna, dekryptera den och påbörja processen med att återfå dina medel.



Dessa säkerhetskopior krypteras lokalt av din nod innan de skickas, vilket garanterar sekretessen för dina data: Umbrel kan inte läsa innehållet i SCB. Överföringen sker via Tor, vilket förhindrar att din IP-adress läcker ut. Dessutom lägger din Umbrel till brus i trafiken (slumpmässig utfyllnad och falska säkerhetskopior som skickas med oregelbundna intervall) för att förhindra att servern kan dra slutsatser om exakt när du öppnar eller stänger en kanal.



Den största fördelen med den här metoden är att den avsevärt förenklar säkerhetskopieringen av Lightning-noden: du behöver bara säkerhetskopiera din seed en gång under nodinitialiseringen. Detta medför en viss risk, eftersom det bara är en säkerhetskopia av SCB, men för rimliga belopp är det en acceptabel kompromiss.



### Bästa praxis för att begränsa risken för förlust



Även med Umbrel som backup kan några enkla och bra metoder kraftigt minska risken för att förlora sats:





- Övervaka dina kollegors tillgänglighet:



Om en viktig kanal ofta är associerad med en oåtkomlig eller instabil peer är det säkrare att stänga den helt medan noden fortfarande fungerar. Ett förebyggande samarbete eller en påtvingad stängning eliminerar en potentiell källa till problem i händelse av SCB-återställning.





- Undvik att koncentrera för mycket likviditet till okända motparter:



Ju större kanal en peer har med dig, desto viktigare är det att vara pålitlig. Välj seriösa, välanslutna och aktiva noder, så att en eventuell framtida återhämtning via SCB kan ske smidigt.





- Komplettera Umbrel med lokala säkerhetskopior:



Förutom Umbrel:s automatiska säkerhetskopiering kan du också spara en krypterad kopia av din SCB-fil (`channel.backup`) på externa medier och uppdatera den regelbundet. Helst bör du förnya den varje gång du öppnar eller stänger en kanal. Detta ger dig en reservlösning om Umbrel:s automatiska säkerhetskopieringstjänst av någon anledning inte skulle vara tillgänglig.





- Hantera din seed på rätt sätt



Din seed Umbrel återställer inte bara din wallet i kedjan, utan tar även fram krypteringsnyckeln för säkerhetskopior. En angripare med tillgång till den skulle därför kunna starta en återställning och överföra dina pengar till sin egen wallet, utan att ens ha fysisk tillgång till din nod.



Så om du behöver återställa din nod men inte längre har din seed kommer du inte att kunna återställa någonting: alla dina sats kommer att gå förlorade. Det är därför mycket viktigt att du sparar din seed med största omsorg, endast på fysiska medier (papper eller metall), och att du förvarar den på en säker plats. Mer information om hur du hanterar en seed finns i den här handledningen:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Hur sparar jag min Lightning-nod på Umbrel?



Nu när du har förstått hur teorin fungerar, låt oss komma ner till det väsentliga. Från din Lightning Node-applikation (som faktiskt är LND) klickar du på de tre små prickarna i det övre högra hörnet.



![Image](assets/fr/022.webp)



Det finns tre element av intresse här för säkerhetskopian:




- Kontrollera att alternativet `Automatiska säkerhetskopior` är aktiverat. Detta kommer automatiskt att skicka din krypterade SCB till Umbrel:s servrar.
- Du kan sedan välja om du vill skicka via Tor eller clearnet, med hjälp av alternativet `Backup over Tor`. Som förklarats i de tidigare avsnitten rekommenderar jag starkt att du använder Tor för att bevara din sekretess.
- Slutligen finns det en knapp "Ladda ner kanalens backup-fil", som låter dig ladda ner en "kanal.backup"-fil, dvs. en krypterad ögonblicksbild av din SCB, till din dator. Detta gör att du kan göra ytterligare lokala säkerhetskopior då och då, utöver de som automatiskt skickas till Umbrel-servrar.



Nu vet du hur du skyddar din Lightning-nods sats från dataförlust. I nästa kapitel tittar vi på hur du skyddar din nod mot fuskförsök.




## Watchtower: roll och upplägg


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



I Lightning är varje kanal baserad på en sekvens av successiva tillstånd, representerade av opublicerade commitment transaction. Vid varje Lightning-betalning eller routing bygger de två deltagarna i kanalen ett nytt par commitment transaction, vilket återspeglar den aktuella fördelningen av medel i kanalen. Gamla commitment transaction blir föråldrade.



Om en av parterna publicerar ett inaktuellt tillstånd har den andra parten rätt att sanktionera det och återkräva hela beloppet av kanalens medel. I det här kapitlet tar vi en kort titt på hur den här mekanismen fungerar och förklarar sedan hur du sätter upp ett ***watchtower***: ett system för att skydda din Lightning-nod från eventuella fuskförsök.



### Förstå hur vakttorn fungerar


Vid varje given tidpunkt har varje part i kanalen en commitment transaction som, om den publiceras, skulle göra det möjligt för dem att stänga kanalen och återfå sin andel av medlen. Denna process är känd som *forced closure*. Men om de försöker publicera en äldre commitment transaction, som motsvarar ett tidigare tillstånd i kanalen där den innehöll fler sats, skulle denna transaktion betraktas som ett försök till fusk. I detta fall kan motparten använda återkallningsnyckeln som är associerad med detta äldre tillstånd för att återfå hela beloppet av medel i kanalen, medan fuskaren tillfälligt blockeras av tidslåset.


Detta system innebär att publicering av ett gammalt tillstånd, dvs. försök att fuska, är mycket riskabelt: om den andra parten ser denna transaktion på mempoolen eller på blockchain innan tidslåset löper ut, kan de använda återkallningsnyckeln och återfå alla medel. **Säkerheten i din Lightning-kanal beror därför på din förmåga att upptäcka ett fuskförsök inom det tidsfönster som tidslåset innebär**.



#### Varför är vakttorn nödvändiga?



Påföljdsmekanismen fungerar bara om den skadelidande har möjlighet att göra det:




- övervaka varje nytt Bitcoin-block för att se om en kanal commitment transaction har publicerats;
- avgöra om denna transaktion motsvarar det senaste giltiga tillståndet eller ett återkallat tillstånd;
- i händelse av en återkallad status, att sända den lagliga transaktionen i tid, med hjälp av återkallningsnyckeln för att återfå alla medel innan tidslåset löper ut.



![Image](assets/fr/023.webp)



I ett idealiskt scenario är din Lightning-nod online 24/7, den är synkroniserad och övervakar kontinuerligt blockkedjan. Av den anledningen kan den på egen hand upptäcka ett fuskförsök och reagera. I praktiken kan dock en personlig Lightning-nod stängas av, särskilt vid ett långvarigt strömavbrott eller fel på internetanslutningen.



Det är just under dessa perioder av driftstopp som risken blir verklig: om en oärlig peer publicerar en gammal status medan din nod är offline, och tidslåset löper ut utan någon reaktion från dig, blir fusket effektivt. Du förlorar en del av eller alla dina pengar i kanalen.



Watchtowers infördes för att minska denna risk. Ett vakttorn är en extern tjänst som övervakar blockkedjan för din räkning, söker efter eventuell publicering av en gammal status på en av dina kanaler och, om det behövs, automatiskt sänder strafftransaktionen för din räkning. Så även om din Lightning-nod förblir offline under en längre period, så länge det vakttorn du använder är i drift, kommer det att kunna skydda dina medel genom att övervaka eventuella fuskförsök och tillämpa motsvarande straff, så snart det upptäcker ett.



#### Hur ett vakttorn fungerar



Ett vakttorn är utformat för att minimera den information som det får om dina kanaler, samtidigt som det ger det möjlighet att agera i händelse av ett problem:




- För varje nytt kanaltillstånd med en peer förbereder din nod en potentiell strafftransaktion i förväg. Om denna peer skulle fuska skulle denna transaktion göra det möjligt för dig att återfå alla medel i kanalen;
- Din nod krypterar sedan denna strafftransaktion med TXID för motsvarande commitment transaction (den som skulle användas om den som fuskar skulle försöka sig på ett bedrägeri). Så länge ingen stängning sker kan vakttornet inte dekryptera den här transaktionen, eftersom det inte helt känner till TXID för fusktransaktionen;
- Din nod skickar ett paket till vakttornet som innehåller den krypterade strafftransaktionen och halva TXID för den potentiella fusktransaktionen.



Eftersom TXID som överförs till vakttornet är ofullständigt kan det inte dekryptera rättvisetransaktionen. Det kan dock övervaka blockkedjan för ett TXID som matchar den del som det äger. Om den upptäcker en sådan transaktion försöker den sedan använda det fullständiga TXID för den transaktionen för att dekryptera din strafftransaktion. Om dekrypteringen lyckas vet den att det är ett fuskförsök och publicerar omedelbart strafftransaktionen åt dig.



![Image](assets/fr/024.webp)



Vakttornet har därför ingen insyn i detaljerna i dina kanaler: varken dina kollegors identitet, saldon eller transaktionernas struktur. Det ser bara krypterade paket. Den enda information den kan utläsa är hur snabbt era kanaler uppdateras, eftersom den får ett paket för varje nytt tillstånd, men inte kan veta vad det innehåller. I händelse av fusk kommer den säkert att upptäcka kanalinformationen genom att dekryptera strafftransaktionen, men din sats kommer åtminstone att sparas.



Denna mekanism bygger på en kompromiss: du delegerar möjligheten att publicera en för-signerad strafftransaktion till vakttornet, men denna transaktion förblir helt ogenomskinlig för vakttornet tills något fusk äger rum. Vakttornet kan varken ändra mottagarna eller avleda medlen, eftersom det bara har en transaktion som redan har undertecknats, med utgångarna frysta till din fördel. Det kan inte heller känna till detaljerna i en kanal i en legitim tvingad eller kooperativ stängning, eftersom TXID:erna inte matchar. Å andra sidan är Watchtower fortfarande en minimal betrodd tredje part: du måste lita på att den är online och att den korrekt sänder din rättvisetransaktion när du behöver den.



#### Att bli ett vakttorn



I teorin kan vilken Lightning-nod som helst fungera som ett vakttorn för andra noder (om de använder samma implementering, t.ex. LND), samtidigt som den själv skyddas av andra noder som spelar denna roll åt den. I följande praktiska avsnitt visar jag dig hur du ställer in den här enkla mekanismen på din LND under Umbrel.


Som en följd av detta kan en intressant strategi vara att komma överens med betrodda bitcoiner-vänner om att agera som varandras vakttorn. Du övervakar deras kanaler och de övervakar dina.



### Hitta ett altruistiskt vakttorn



Om du inte känner någon i din omgivning som kan tillhandahålla en vakttornstjänst finns det ett antal altruistiska offentliga vakttorn som du kan ansluta till. I den här LNP202-kursen föreslår jag till exempel att du ansluter till den vakttornstjänst som erbjuds gemensamt av LN+ och Voltage, som är ett vakttorn för LND.


Här har du inloggningsuppgifterna:



- Via Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Via clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

För att tacka dem för att tillhandahålla denna gratis vakttornstjänst, [du kan göra en donation via Lightning](https://lightningnetwork.plus/donation).


Nu när vi använder en altruistisk vakttornstjänst ska vi se hur vi konfigurerar den på vår LND-nod under Umbrel.


### Sätta upp ett vakttorn


I programmet `Lightning Node` klickar du på de tre prickarna längst upp till höger i gränssnittet och väljer sedan `Avancerade inställningar`.


![Image](assets/fr/025.webp)


Gå sedan till menyn `Watchtower`.


![Image](assets/fr/026.webp)



Aktivera alternativet `Watchtower Client` och klicka sedan på knappen `SAVE AND RESTART NODE`. Vänta tills LND startas om.


![Image](assets/fr/027.webp)


När omstarten är klar går du tillbaka till samma meny och anger ID för det altruistiska vakttorn som du väljer i det angivna fältet. Klicka sedan på knappen "ADD" för att bekräfta. Du kan också justera parametern `Watchtower Client Sweep Fee Rate`: det här är den avgiftssats du är villig att betala för en möjlig rättvisetransaktion som sänds av vakttornet. Det finns inget behov av att välja en alltför hög ränta, men du bör också undvika en ränta som är för låg, annars kommer den juridiska transaktionen inte att bekräftas i tid.


Starta om noden med hjälp av knappen `SAVE AND RESTART NODE` för att tillämpa dessa ändringar.


![Image](assets/fr/028.webp)



Om du återvänder till samma meny ser du att din Lightning-nod nu skyddas av det vakttorn som du just har lagt till.



![Image](assets/fr/029.webp)



Ett altruistiskt vakttorn är i allmänhet tillräckligt, särskilt om du inte placerar stora summor pengar på din Lightning-nod och om du hanterar din nod väl (låt den inte vara avstängd för länge). För ännu större säkerhet kan du också lägga till flera genom att upprepa samma process.



## Öppna din första Lightning-kanal


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Om du har kommit så här långt vet du redan att en Lightning-nod utan kanal är lite som en tom wallet: den finns, men den är värdelös. För att kunna skicka eller ta emot betalningar måste din nod vara ansluten till minst en annan nod i Lightning-nätverket via en kanal. I framtiden rekommenderar vi starkt att du öppnar flera kanaler, av skäl som rör motståndskraft och effektivitet i routingen. I de följande kapitlen kommer vi också att titta på hur du hanterar dina likvida tillgångar, optimerar din kanaltopologi och använder mer avancerade verktyg än det grundläggande LND-gränssnittet på Umbrel.



Men i det här inledande kapitlet är syftet helt enkelt att förstå hur du väljer en bra Lightning-peer, var du hittar den information du behöver för att välja dina peers och slutligen hur du öppnar din första kanal via det grundläggande LND-gränssnittet.



### Hur väljer man en bra Lightning peer?



När du öppnar en kanal måste du välja en peer: en annan Lightning-nod som din nod kommer att vara direkt ansluten till via en kanal. Detta val av peer är viktigt, eftersom det kommer att ha en direkt inverkan på:




- gör det lättare för dina betalningar att hitta rätt;
- tillförlitligheten hos dina kanaler över tid;
- dina routingkostnader.



Det finns ingen perfekt matchning för alla, men det finns ett antal tillförlitliga kriterier för att identifiera bra kandidater.



#### 1. Anslutningsbarhet för noder



En bra peer är en nod som är väl ansluten till Lightning-nätverket. Det betyder inte bara att den har ett stort antal kanaler (även om det kan vara en indikator), utan framför allt att den är ansluten till andra tillförlitliga noder och har en tillräckligt central position i nätverksgrafen.



En väl ansluten nod ökar dina chanser att hitta en effektiv väg till de flesta betalningsdestinationer. Det minskar också antalet mellanliggande noder som behövs, vilket håller kostnaderna nere.



Omvänt kan det begränsa dina möjligheter om du öppnar din första kanal till en isolerad eller svagt ansluten nod: du kan betala den här personen, men det blir mycket svårare att betala resten av nätverket.



#### 2. Kapitalisering och kanalkapacitet



En bra peer är också en tillräckligt kapitaliserad nod. Detta visas av dess totala kanalkapacitet (summan av sats som avsatts till alla dess kanaler) och dess genomsnittliga kanalkapacitet (det är ofta bättre att ha ett fåtal välkapitaliserade kanaler än många små).



En nod med löjlig kapacitet, eller vars kanaler alla är små, kommer inte att kunna dirigera betalningar med stora belopp, vilket resulterar i fel i dirigeringen för dig.



#### 3. Principer för kostnadsföring



Varje nod sätter sina egna routingavgifter (`basavgift` och `avgiftssats`). En bra peer kommer inte att ta ut orimliga avgifter för strategiska kanaler. För en första kanal är det bäst att välja en nod med ganska måttliga avgifter, så att du inte missgynnar dina egna betalningar.



Kom ihåg att dina egna routingavgifter också påverkar hur andra uppfattar dig som peer: en nod som ständigt ändrar sina avgifter eller inför absurda kostnader är sällan uppskattad.



#### 4. Stabilitet och senioritet



Peer-stabilitet är ett mycket viktigt kriterium. En bra nod har hög upptid (den är mycket sällan offline), den håller sina kanaler öppna under lång tid och den öppnar/stänger inte kanaler hela tiden utan anledning.



Gamla och fortfarande aktiva kanaler är en bra signal: de tyder på att relationen är lönsam för peer, att noden vet hur den ska förvalta sitt kapital och att den inte stänger när som helst, så att du inte behöver fortsätta betala onchain-avgifter för stängning och återöppning.



Omvänt kan en kollega som ofta är offline, eller som snabbt stänger kanaler, vara en källa till problem för dig och till extra kostnader för att öppna nya kanaler.



Även med dessa kriterier kommer du inte att göra ett perfekt val första gången. Det är normalt: den verkliga kvaliteten på en peer avslöjas genom dess användning. Så det är viktigt att:




- övervaka kanalaktivitet (routade volymer, tillgänglighet etc.);
- stänga kanaler som inte tjänar något syfte eller vars användare alltför ofta är offline;
- omfördela ditt kapital till bättre konkurrenter över tiden.



Tanken är inte att öppna och stänga kanaler varje dag (vilket skulle vara dyrt i onchain-kostnader), utan att gradvis utveckla din topologi för att konvergera mot en uppsättning pålitliga, välanslutna peers som är kompatibla med dina behov.



### Hur hittar jag en kollega?



För att tillämpa dessa kriterier behöver du verktyg som ger insyn i Lightning-nätverket. Det finns flera utforskare och tjänster tillgängliga för att göra detta. Bland de mest kända Lightning-exploratorerna finns [1ML](https://1ml.com/) och [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Här föreslår jag dock att du använder [Lightning Terminal-verktyget från Lightning Labs] (https://terminal.lightning.engineering/), som ger en rangordning (visserligen baserad på delvis subjektiva kriterier) av de Lightning-noder som anses vara mest relevanta för att öppna en kanal.



![Image](assets/fr/030.webp)



Problemet med de mycket stora blixtnoderna högst upp i denna ranking är att de flesta inte accepterar kanalöppningar under mycket höga belopp. Många tillämpar också strikta peer management-policyer, vilket kan leda till att din kanal stängs. Å andra sidan har dessa noder i allmänhet inget behov av inkommande likviditet, med tanke på deras antal anslutningar.



Jag skulle därför råda dig att arbeta dig nedåt i rankningen för att hitta en nod som är väl ansluten, pålitlig och tillräckligt central i nätverksgrafen, utan att vara överdrivet stor. Här har jag till exempel identifierat Lightning-noden på stacker.news, som är mycket väl ansluten, har hög kapacitet och intar en central position i nätverksgrafen.



![Image](assets/fr/031.webp)



En annan intressant strategi är att öppna en kanal till en nod som är i behov av inkommande likviditet, till exempel en handlare du känner, en förening eller ett samhälle. Denna strategi har tre fördelar:




- Eftersom den valda enheten behöver inkommande likviditet kommer den logiskt sett att ha mindre incitament att stänga din kanal utan anledning;
- Dess ekonomiska aktivitet ökar chanserna för routing på denna kanal, och därmed för att ta ut vissa avgifter;
- Du gör ekosystemet en tjänst och ger ett värdefullt bidrag till andra bitcoinanvändare.



När du har identifierat en relevant nod kan du hämta dess Node ID. Detta är helt enkelt en sammankoppling av nodens publika nyckel, en `@`-separator, dess IP- eller Tor-adress och den port som används. Detta ID är lättillgängligt från nodens profil i alla Lightning explorer.



### Öppna din första kanal via LND



Nu när vi har identifierat noden med vilken vi ska öppna vår första kanal, behöver vi sats för att låsa in den. För att göra detta måste du mata Bitcoin på kedjan wallet som är associerad med din LND.



Från huvudgränssnittet LND, leta upp din `Bitcoin Wallet` och klicka sedan på `Deposit`-knappen. En mottagningsadress i kedjan är då generated: skicka sats till den. Hur mycket du behöver överföra beror på vilken kapacitet du vill tilldela din första kanal, men kom ihåg att du behöver skicka något mer än den avsedda kapaciteten. Om du till exempel vill öppna en 500 000 sats-kanal ska du inte skicka exakt 500 000 sats, utan ett högre belopp.



![Image](assets/fr/032.webp)



När transaktionen har sänts visas den i gränssnittet. Vänta på bekräftelse innan du öppnar kanalen. Du ser en grön pil bredvid den när den är bekräftad.



![Image](assets/fr/033.webp)



Bläddra ner till huvudgränssnittet och klicka sedan på "+ OPEN CHANNEL".



![Image](assets/fr/034.webp)



Ange `Node ID` för den nod du vill öppna en kanal med, ange beloppet du vill låsa in och justera sedan den inledande transaktionsavgiften enligt läget på onchain-avgiftsmarknaden. Se naturligtvis till att du har tillräckliga medel i din LND onchain-portfölj i förväg.



När alla parametrar har ställts in klickar du på knappen "Öppna kanal".



![Image](assets/fr/035.webp)



Vänta på att öppningstransaktionen ska bekräftas på kedjan. Din första kanal är nu officiellt i drift: grattis!



Du kan se att för tillfället är 100 % av kanalens likviditet på min sida: det är normalt, eftersom jag är den som öppnade kanalen. I takt med att betalningar och routing utvecklas kommer den här fördelningen att förändras, men kanalens totala kapacitet kommer alltid att vara densamma.



![Image](assets/fr/036.webp)



Nu när du har en kanal kan du göra dina första Lightning-betalningar, förutsatt att den valda noden är korrekt ansluten till nätverket. I senare kapitel kommer vi naturligtvis att titta på hur du kan ställa in en mer bekväm metod för att betala Lightning-fakturor från din mobil. Men nu ska vi prova att göra en första betalning direkt från LND till Umbrel.



För att göra detta, i avsnittet `Lightning Wallet`, klicka på knappen `SEND` och klistra sedan in fakturan som ska ställas.



![Image](assets/fr/037.webp)



Fakturabeloppet visas. Bekräfta betalningen genom att klicka på knappen "SEND".



![Image](assets/fr/038.webp)



Om en giltig rutt hittas bör din första Lightning-betalning lyckas.



![Image](assets/fr/039.webp)



Om vi sedan tittar på fördelningen av likviditeten i kanalen ser vi att min peer nu har 5 002 sats på sin sida. Detta motsvarar de 5 000 sats av betalningen som jag just gjorde, som han dirigerade till mottagarens nod. De ytterligare 2 sats representerar de routningsavgifter jag betalade, eftersom mottagaren fick exakt 5 000 sats.



![Image](assets/fr/040.webp)



För att förbättra tillförlitligheten i våra betalningar kommer det uppenbarligen att vara nödvändigt att öppna upp andra kanaler. Beroende på våra mål måste vi också hitta ett sätt att göra inkommande likviditet tillgänglig så att vi kan ta emot betalningar på Lightning. Detta kommer att vara ämnet för nästa avsnitt.



# Hantera din Lightning-nod


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Definiera din profil som nodoperatör


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Nu när din Lightning-nod är igång är nästa steg att definiera din traderprofil. Det här är ett viktigt val eftersom det avgör din strategi för kanalöppning, vilken typ av peers du föredrar och hur du hanterar likviditet.



På Lightning, för att detta ska fungera, behöver du likviditet i rätt riktning. Utgående likviditet motsvarar din betalningsförmåga (sats tillgänglig på din sida av kanalerna). Inkommande likviditet motsvarar din kapacitet att ta emot (sats tillgängligt på dina kollegors sida). Med andra ord kokar din profil ner till en enkel fråga: för det mesta, lämnar dina sats din nod, eller kommer de in i den?



### Konsumenten



Det här är profilen för de allra flesta användare. Du använder din nod för att göra Lightning-betalningar: för att köpa varor och tjänster, betala räkningar, skicka dricks - kort sagt, för att använda Lightning som ett snabbt betalningsmedel. Å andra sidan får du lite från Lightning, eller bara marginellt, till exempel några få donationer, återbetalningar mellan vänner eller några mikrobetalningar.



Den här profilen är lättast att hantera, eftersom ditt främsta behov är att kunna betala. I praktiken innebär det att du behöver utgående likviditet. När du har öppnat en eller flera kanaler av rätt storlek till stabila, välanslutna noder kommer dina utgående betalningar mekaniskt att flytta likviditet till andra sidan av dina kanaler. Det är just den här rörelsen som naturligt skapar en rimlig mängd inkommande likviditet. Som ett resultat, även om du inte vill ta emot på regelbunden basis, kommer du fortfarande att kunna ta emot då och då utan att implementera en komplex strategi. Så du behöver inte oroa dig för din inkommande likviditet.



I den här LNP202-kursen kommer vi att fokusera på den här "konsument"-nodoperatörsprofilen, eftersom det är den som motsvarar nästan alla Bitcoin-användare på Lightning.



### Återförsäljaren



Handlaren är på sätt och vis motsatsen till konsumenten. Här är huvudsyftet inte att betala, utan att samla in. Ett företag, en tjänsteleverantör, en webbutik eller ett försäljningsställe som accepterar Lightning kommer att få många inkommande betalningar och göra relativt få utgående betalningar från den här noden.



Denna profil är mer krävande, eftersom en nekad betalning på Lightning potentiellt innebär en förlorad försäljning. Prioriteten blir därför inkommande likviditet. Om din nod inte har tillräckligt med inkommande likviditet kommer dina kunder att se sina betalningar misslyckas, även om de har pengarna, helt enkelt för att det inte finns någon väg för att få likviditeten till dig i rätt riktning.



Den stora utmaningen för handlaren kommer också från den naturliga utvecklingen av kanaler. Om allt du gör är att ta emot kommer dina kanaler gradvis att fyllas upp på din sida. Så du behöver mekanismer för att upprätthålla och förnya din inkommande likviditet.



Det finns dock ett enklare fall: den blandade konsument-/handlarprofilen. Om du samlar in pengar på Lightning, men också spenderar på Lightning (affärsutgifter, betalningar till leverantörer eller till och med personliga utgifter), återskapar dina utgående betalningar naturligtvis inkommande. Hanteringen blir smidigare, eftersom flödena tar ut varandra, och du behöver inte använda artificiella mekanismer som enbart är utformade för att återfå inkommande likviditet.



### Router



Routern är en specifik profil. Den använder inte sin Lightning-nod för att betala eller inkassera, utan för att dirigera andras betalningar och inkassera avgifter. Målet är att vara en användbar, tillförlitlig och ekonomiskt konkurrenskraftig rutt inom Lightning-grafen.



För att vara ärlig med dig är det en mer komplex verksamhet att vara en router på Lightning än det ser ut, och lönsamhet är svår att uppnå. Först och främst är det dyrt att öppna och stänga kanaler i kedjekostnader. För att routera effektivt måste du ofta justera din topologi, testa, stänga underpresterande kanaler, öppna nya och regelbundet ombalansera din likviditet. För det andra är konkurrensen stenhård: stora, etablerade noder tar naturligtvis en stor del av trafiken och det är svårt att få fotfäste utan att binda upp betydande kapital i väl tilltagna kanaler.



Det finns också ett högt driftskrav. En routingnod måste vara extremt stabil, övervakad, ha ordentlig säkerhetskopia och hanteras rigoröst. Du måste övervaka kanalens prestanda, anpassa din avgiftspolicy, upprätthålla en balanserad likviditet, hantera peers och snabbt lösa tekniska problem. Den här nivån av engagemang kan vara intressant som en teknisk hobby eller som ett bidrag till infrastrukturen, men om ditt mål helt enkelt är att använda Lightning på ett suveränt sätt är det sällan relevant att börja routa för att tjäna pengar. Det är därför som denna LNP202-kurs inte täcker denna profil på djupet.



### Placera dig själv på en tydlig plats innan du går vidare



Om du passar in i konsumentprofilen kommer din prioritet att vara att kunna betala på ett tillförlitligt sätt med enkel hantering. Om du är en handlare är din prioritet att kunna betala utan att misslyckas, vilket innebär en strategi för att skaffa inkommande likviditet. Om du överväger routing måste du se det som en krävande, ekonomiskt osäker och tidskrävande aktivitet.



Genom att definiera den här profilen nu kan du undvika en klassisk fallgrop: att tillämpa en kanalstrategi som är utformad för en handlare eller router, när du helt enkelt är en användare som vill betala.



## Använda en Lightning-nodhanterare


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



I den föregående delen av denna LNP202-utbildningskurs använde vi det grundläggande gränssnittet för applikationen `Lightning Node` på Umbrel. Detta gränssnitt är tillräckligt för viktiga operationer (kontrollera saldon, visa kontantfördelning, öppna och stänga kanaler), men det är avsiktligt mycket förenklat. Denna enkelhet begränsar de tillgängliga alternativen och ger inte tillgång till många av de avancerade funktionerna i din LND-nod. Av denna anledning kommer vi nu att använda en annan, mer omfattande programvara för Lightning-nodhantering.



Denna extra programvara kommer helt enkelt att vara ett kompletterande hanteringsgränssnitt för din nod. Det innebär att du kan fortsätta att använda gränssnittet "Lightning Node" parallellt och till och med använda flera olika om du vill. Det är helt enkelt olika sätt att interagera med samma Lightning-nod.



Bland de mest kända mjukvaruprogrammen är:




- [Alby Hub] (https://albyhub.com/);
- [Ride The Lightning] (https://www.ridethelightning.info/);
- [ThunderHub] (https://thunderhub.io/).



Alla tre är bra lösningar. Om du vill kan du testa alla tre med din nod innan du väljer den som passar dig bäst. Personligen använder jag ThunderHub av gammal vana och för att det verkar mer komplett än de andra. Det är det verktyget jag kommer att presentera i den här utbildningen, men du kan också välja något av de andra två alternativen. Vi har en särskild handledning för vart och ett av dessa program på Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Installera ThunderHub



Alla dessa program kan installeras mycket enkelt från Umbrel App Store. Som jag sa, vi kommer att använda ThunderHub här, men om du vill testa en annan senare, kommer proceduren att vara liknande.



![Image](assets/fr/041.webp)



Umbrel ger dig ett standardlösenord för åtkomst till ThunderHub. Kopiera det: du kommer att behöva det direkt. Kom också ihåg att spara det i din lösenordshanterare, eftersom du kommer att bli ombedd att ange det varje gång du öppnar programvaran.



![Image](assets/fr/042.webp)



Klicka på "Logga in" och klistra sedan in lösenordet från Umbrel för att logga in.



![Image](assets/fr/043.webp)



Du kommer då till startsidan för ThunderHub, som visar den viktigaste informationen om din Lightning-nod.



![Image](assets/fr/044.webp)



Till att börja med rekommenderar jag att du aktiverar tvåfaktorsautentisering (2FA). I inställningarna klickar du helt enkelt på "Aktivera" bredvid "Aktivera 2FA" och följer sedan den vanliga processen.



![Image](assets/fr/045.webp)



### Använd ThunderHub



ThunderHub är relativt lätt att lära sig. Alla menyer är åtkomliga från gränssnittets vänstra kolumn. För att sammanfatta, här är vad var och en gör:




- home: översikt över noder, balanser och snabba åtgärder;
- instrumentpanel: anpassningsbar instrumentpanel med widgetar och mätvärden;
- peers: visa och hantera anslutningar till andra Lightning-noder;
- kanaler": fullständig kanalhantering (likviditet, avgifter, stängning etc.);
- rebalance": ett verktyg för att ombalansera kanaler via cirkulära betalningar;
- transaktioner: historik över skickade och mottagna blixtbetalningar;
- forwards`: routingstatistik och kostnader generated för din nod;
- `Kedja`: Bitcoin onchain-portfölj (UTXO och transaktioner);
- gW-201-integration för övervakning och backup;
- `Tools`: avancerade verktyg (säkerhetskopior, rapporter, macaroons, signaturer, etc.);
- byte: Blixtsnabba/kedjeförsedda byten via Boltz;
- `Stats`: övergripande statistik och prestanda för din Lightning-nod.



Med den här uppsättningen funktioner har du alla verktyg du behöver för att hantera din Lightning-nod på ett effektivt sätt. Det är inte nödvändigt att behärska varje alternativ i detalj direkt: vi kommer att utforska dem gradvis under hela kursen. Men om du vill lära dig mer om programvaran på djupet kan du ta en titt på vår handledning ThunderHub:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Den meny vi är mest intresserade av här är `Kanaler`. Den ger en detaljerad bild av alla kanaler i din nod, med deras likviditetsfördelning. I synnerhet kan du se vilka kanaler som är öppna i `Open`, vilka som väntar på att öppnas eller stängas i `Pending` och vilka som redan är stängda i `Closed`.



![Image](assets/fr/047.webp)



För en viss kanal kan du klicka på peerens namn eller kanal-ID för att öppna dess Amboss-sida och få mer information. Du kan också klicka på pennikonen för att ändra kanalens parametrar, inklusive den avgiftspolicy som tillämpas på kanalen om din nod dirigerar betalningar till din peers nod.



![Image](assets/fr/048.webp)



Om du använder din Lightning-nod huvudsakligen som en "konsument" behöver du inte ändra dessa avgifter: du kan behålla standardvärdena. Om du å andra sidan vill förstå bättre hur routningsavgifter fungerar på Lightning rekommenderar jag LNP 201-utbildning, och i synnerhet kapitel 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Genom att klicka på det lilla krysset bredvid en peer kan du initiera stängningen av en kanal. Om du till exempel märker att en peer regelbundet är inaktiv kan det vara lämpligt att stänga den här kanalen för att omfördela ditt kapital till en mer tillförlitlig peer.



Du har då två alternativ. Det första, och alltid att föredra, är kooperativ stängning. Genom att bekräfta den här åtgärden ber din nod din peer att stänga kanalen gemensamt. Om han accepterar kan du sända onchain-stängningstransaktionen och återfå din andel av pengarna. Fördelarna med den här metoden är att du väljer onchain-avgifterna för transaktionen, vilket undviker onödiga kostnader, och att pengarna återvinns snabbare utan någon tidslåsning.



![Image](assets/fr/049.webp)



Det andra alternativet är påtvingad stängning. I det här fallet ber du inte om motpartens samtycke utan sänder direkt ut den sista commitment transaction som du har i din ägo. Jag skulle inte rekommendera den här metoden om det inte är en sista utväg, till exempel om motparten systematiskt vägrar kooperativa stängningar eller inte längre svarar. Tvångsstängning har två stora nackdelar: avgifterna är ofta mycket höga, eftersom de har fastställts i förväg för att förutse en ökning av avgifterna i kedjan, och det finns en fördröjning i att återfå pengarna, eftersom de blockeras av en tidslåsning. Denna tidslåsning ger din peer tid att reagera i händelse av ett fuskförsök (vilket uppenbarligen inte är fallet här, men du måste ändå vänta).



![Image](assets/fr/050.webp)



Slutligen, för att öppna en ny kanal, gå till menyn `Home` och klicka på `Open a Channel` i avsnittet `Liquidity`. Du kommer då att kunna ange ID för den valda noden, kanalens kapacitet, den önskade Lightning-routingavgiften och onchain-avgiften för öppningstransaktionen.



![Image](assets/fr/051.webp)



Det här är de viktigaste åtgärderna du behöver utföra på ThunderHub. Vi kommer att upptäcka andra funktioner allt eftersom vi går vidare i denna LNP202-kurs.



## Anskaffning av inkommande likviditet


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Som du kan se är det inte särskilt komplicerat att ha utgående likviditet för att göra betalningar på Lightning. Det är bara att på eget initiativ öppna kanaler till andra noder och börja skicka sats. Å andra sidan är det mer komplicerat att ha inkommande likviditet för att ta emot betalningar på Lightning, eftersom du antingen behöver andra noder för att öppna kanaler till dig, eller så måste du flytta likviditeten själv genom att göra betalningar.



Om du har en "konsumentprofil" behöver du i allmänhet inte oroa dig för inkommande likviditet. Din användning av Lightning-noden kommer att vara övervägande betalningsorienterad, snarare än inbetalning. Genom att helt enkelt göra några Lightning-betalningar kommer du naturligt att skapa inkommande likviditet över tid.



Om du däremot har en "merchant"-profil är situationen den omvända: du kommer huvudsakligen att samla in betalningar och göra få av dem. Så du kan inte enbart förlita dig på dina egna betalningar för inkommande likviditet. Det blir därför nödvändigt för andra Lightning-noder att öppna kanaler till dina. Men hur kan detta uppnås? Hur får man andra operatörer att binda kapital åt en? Det är just det vi ska utforska i det här kapitlet.



### Köp av inkommande likviditet



Som du kan förvänta dig är det mest effektiva sättet att få någon att agera att betala dem. För inkommande likviditet till din Lightning-nod är principen exakt densamma. Det enklaste sättet att få kanaler till din nod är att betala för tjänsten och den kapitalbindning som är inblandad.



Om du är ett företag eller en återförsäljare innebär det här tillvägagångssättet att du snabbt kan få tillförlitliga kanaler för att ta emot betalningar från dina kunder utan friktion.



Det finns många sätt att köpa inkommande likviditet. Den som jag personligen använder och rekommenderar är Amboss:s [Magma] (https://magma.amboss.tech/) plattform. Den är mycket enkel att använda, det går snabbt att öppna en kanal och priserna är i allmänhet rimliga. Magma fungerar som en marknadsplats med makers och takers, men version 2 har kraftigt förenklat upplevelsen: skapa helt enkelt en begäran, betala priset via Lightning, och Magma matchar den automatiskt med det bästa tillgängliga erbjudandet. Efter sex onchain-bekräftelser är din kanal med inkommande likviditet igång. Så här fungerar det:



Gå till [Magmas webbplats] (https://magma.amboss.tech/buy), i avsnittet `Buy Channels`.



![Image](assets/fr/052.webp)



Om du vill kan du skapa ett konto för att spåra dina köp, men det är inte obligatoriskt. Om du inte skapar ett konto kommer Magma helt enkelt att förse dig med ett sessions-ID, som gör det möjligt för dig att hämta dina inköp vid ett senare tillfälle.



Väl på webbplatsen fyller du i den information som krävs för att köpa likviditet. Välj "One Time" för ett engångsköp och ange sedan det belopp som du är villig att betala för inkommande likviditet. Ju högre belopp som betalas, desto större kapacitet har kanalen som öppnas för din nod. En uppskattning av kanalens kapacitet visas nedan: detta är en approximation, eftersom det slutliga beloppet beror på det bästa erbjudandet som Magma hittar, vilket ibland är högre, ibland lägre.



![Image](assets/fr/053.webp)



Ange sedan ditt nod-ID. Du hittar det till exempel i menyn `Node ID` i applikationen `Lightning Node` på Umbrel.



![Image](assets/fr/054.webp)



När all information har fyllts i klickar du på knappen "Granska och öppna order".



![Image](assets/fr/055.webp)



Om du inte har skapat ett konto kommer Magma att förse dig med en sessionsnyckel och en backup-fil. Förvara dessa två saker på ett säkert ställe, eftersom de gör det möjligt för dig att hämta beställningen vid ett senare tillfälle eller att spåra dess status i händelse av problem. När du har sparat filen klickar du på knappen "Betala med Lightning".



![Image](assets/fr/056.webp)



Magma skickar sedan generates en blixtfaktura på det belopp du har valt. Du måste betala den. Om du redan har kanaler på din Lightning-nod kan du betala direkt från den, eller använda en annan extern Lightning wallet.



![Image](assets/fr/057.webp)



När betalningen har gjorts visas transaktionen som behandlad i Magma-gränssnittet.



![Image](assets/fr/058.webp)



Efter några minuter behandlas begäran: en kanal med sats öppnas till din Lightning-nod. När öppningstransaktionen har bekräftats på kedjan får du tillgång till motsvarande inkommande likviditet.



![Image](assets/fr/059.webp)



Magma är också integrerat direkt i ThunderHub. På fliken `Home`, bläddra ner till avsnittet `Liquidity` och klicka på `Buy Inbound Liquidity`. Allt du behöver göra är att ange önskat belopp och bekräfta. Du behöver inte betala några fakturor manuellt, eftersom ThunderHub automatiskt tar hand om betalningen från din nod.



![Image](assets/fr/060.webp)



Om du är handlare är den här typen av tjänst särskilt lämplig, eftersom den gör det möjligt för dig att snabbt få en stor mängd inkommande likviditet från pålitliga noder, vilket garanterar att dina kunder kommer att kunna betala dig utan problem. Om du å andra sidan är en privatperson eller om du inte vill betala för inkommande likviditet finns det också gratislösningar. Låt oss ta en titt.



### Kooperativ inkommande likviditet



Om du inte är handlare, men ändå behöver lite inkommande likviditet (till exempel för att ladda din nod vid uppstart, medan du väntar på att vissa betalningar ska göras) behöver du inte nödvändigtvis betala för det. En av de lösningar jag föredrar är att samarbeta med andra nodoperatörer som också behöver inkommande likviditet, för att öppna Lightning-kanaler för varandra. På så sätt ger öppnandet av en kanal dig utgående likviditet, samtidigt som du får inkommande likviditet, kostnadsfritt (modulo onchain-avgifter för öppnandet).



Du kan naturligtvis ordna detta direkt med andra bitcoiners. Det finns dock en plattform som är dedikerad till denna typ av cirkulära öppningar: [Lightning Network +] (https://lightningnetwork.plus/). Principen är inte att öppna två kanaler mellan samma personer, utan att skapa cirkulära öppningar med minst tre deltagare, eller ännu fler.



Låt oss ta ett exempel för att förstå hur Lightning Network + fungerar:




- En nodoperatör, kallad `A`, publicerar ett meddelande om att han vill öppna en sats-kanal med 1 miljon sats med två andra personer;
- Annonsen förblir aktiv tills ytterligare deltagare tillkommer;
- Senare ansluter sig två operatörer, "B" och "C", till "A"-nodens tillkännagivande. Triangeln är nu komplett och öppningsfasen kan börja.
- Noden "A" öppnar en kanal till noden "B";
- Noden `B` öppnar en kanal till noden `C`;
- Noden "C" öppnar en kanal till noden "A".



I slutet av operationen har varje nod 1 miljon sats i utgående likviditet och 1 miljon sats i inkommande likviditet. Detta system kan utvidgas till att omfatta fyra eller fem deltagare.



Det finns naturligtvis ingen teknisk mekanism som kan garantera att en deltagare faktiskt öppnar den kanal som de har åtagit sig att skapa. Det är därför plattformen har inrättat ett ryktessystem, baserat på positiva recensioner när operatörer uppfyller sina åtaganden. Och i värsta fall, om du stöter på någon som inte samarbetar, kommer du inte att ha förlorat några pengar: du har helt enkelt missat en möjlighet till inkommande likviditet.



Denna lösning är särskilt lämplig för en "konsumentprofil", eftersom den gör det möjligt för dig att få inkommande likviditet gratis, samtidigt som du ansluter din nod till andra små operatörer. Om du däremot är handlare är detta tillvägagångssätt i allmänhet inte relevant: varje sat av inkommande likviditet kräver att du blockerar en sat av utgående likviditet, och dina stora behov av inkommande likviditet skulle då innebära att du binder för mycket kapital.



För att använda Lightning Network+ har du två alternativ: antingen använder du den applikation som är integrerad i Umbrel, eller så använder du den klassiska webbplatsen och skapar ett konto genom att logga in från din nod. Jag rekommenderar det senare, eftersom den integrerade applikationen inte erbjuder hela utbudet av tillgängliga funktioner.



Gå till webbplatsen [Lightning Network +](https://lightningnetwork.plus/) och klicka på knappen `Login` längst upp till höger i gränssnittet.



![Image](assets/fr/061.webp)



För att autentisera dig måste du signera meddelandet med hjälp av din Lightning-nods privata nyckel. Med ThunderHub är denna operation mycket enkel. Börja med att kopiera det meddelande som visas av LN+.



![Image](assets/fr/062.webp)



I ThunderHub går du till fliken `Tools` och klickar sedan på `Sign`-knappen i avsnittet `Messages`.



![Image](assets/fr/063.webp)



Klistra in autentiseringsmeddelandet från LN+ och klicka sedan på `Signera`.



![Image](assets/fr/064.webp)



ThunderHub signerar sedan detta meddelande med din nods privata nyckel. Kopiera signaturen generated.



![Image](assets/fr/065.webp)



Klistra in denna signatur i motsvarande fält på LN+-webbplatsen och klicka sedan på "Logga in".



![Image](assets/fr/066.webp)



Du är nu ansluten till LN+ med din Lightning-nod. Denna process gör det möjligt för LN+ att verifiera att du är den rättmätiga ägaren till den nod du gör anspråk på på deras plattform.



![Image](assets/fr/067.webp)



Om du vill kan du anpassa din LN+-profil, till exempel genom att lägga till en kort biografi.



För att delta i din första cirkulära kanalöppning, gå till menyn `Swaps` högst upp i gränssnittet. Här hittar du alla byten som för närvarande är tillgängliga, beroende på din nods egenskaper.



![Image](assets/fr/068.webp)



För att gå med i ett befintligt byteserbjudande klickar du bara på det och registrerar dig. På LN+ kan dock skaparen av ett byte införa vissa villkor för deltagarna, till exempel ett minsta antal kanaler eller en minsta total nodkapacitet. Det är därför möjligt, särskilt under de första dagarna, att få erbjudanden kommer att vara tillgängliga för din nod. I mitt fall fanns det inga erbjudanden tillgängliga för min nod, trots att några kanaler redan var öppna. Så jag skapade min egen swap, och du kan göra detsamma om du är i samma situation.



Klicka på "Starta Liquidity Swap" och ange sedan parametrarna för ditt erbjudande:




- Välj det totala antalet deltagare (3, 4 eller 5);
- Ange antalet kanaler som ska öppnas (se till att du har minst detta antal i din onchain wallet);
- Definiera kanalens öppettid. Detta är den period under vilken deltagarna kommer överens om att inte stänga dem;
- Till höger kan du ange begränsningar för deltagarna: minsta antal kanaler, minsta totala kapacitet och vilken typ av anslutning som accepteras.



När alla parametrar har ställts in klickar du på knappen "Starta Liquidity Swap".



![Image](assets/fr/069.webp)



Ditt byteserbjudande har nu skapats. Nu behöver du bara vänta på att andra nodoperatörer ska registrera sig. Om dina villkor inte är alltför restriktiva bör detta inte ta alltför lång tid. Kom ihåg att övervaka statusen för ditt byte under de timmar eller dagar som följer.



![Image](assets/fr/070.webp)



Alla swap-platser har tagits: vi går nu vidare till kanalöppningsfasen. Varje deltagare kan se, från sitt LN+-gränssnitt, till vilken nod han måste öppna en Lightning-kanal.



![Image](assets/fr/084.webp)



På din sida öppnar du kanalen med hjälp av nod-ID:t som tillhandahålls av LN+ och respekterar det belopp som anges. Som vi har sett i tidigare kapitel kan du göra detta antingen via ThunderHub, med en annan Lightning Node Manager eller direkt från det grundläggande Lightning Node-applikationsgränssnittet.



![Image](assets/fr/085.webp)



När öppningen har startats kan du se att den visas i avsnittet med väntande kanaler. I mitt fall är det kanalen med noden `Plebian_fr`.



![Image](assets/fr/086.webp)



Du kan sedan återvända till LN+ för att bekräfta att du har påbörjat kanalöppningen. Klicka bara på knappen "Kanalöppning påbörjad".



![Image](assets/fr/087.webp)



När alla andra deltagare också har öppnat den kanal som de har engagerat sig i, kom ihåg att ge dem en positiv recension.



![Image](assets/fr/088.webp)



Om det uppstår problem eller förseningar kan du kontakta dina kollegor direkt via kommentarsfältet längst ner på sidan.



![Image](assets/fr/089.webp)



Vissa deltagare kanske vill ombalansera de cirkulära kanalerna redan från början genom att göra en betalning till sig själva. Detta säkerställer en balanserad fördelning av kontanter i varje kanal. Om du har en "konsument"-profil är detta inte nödvändigt, men du kan antingen göra denna ombalansering själv om du vill, eller tillfälligt sätta dina kanalavgifter till noll för att göra det enklare för den peer som vill göra det. Ibland vill ingen göra det.



![Image](assets/fr/090.webp)




# Frigör potentialen i din Lightning-nod


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Anslut en mobil wallet via Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Nu har du en väl ansluten Lightning-nod med både inkommande och utgående likviditet. Så du är redo att använda din Lightning-nod i verkliga livet. Hittills har vi alltid använt gränssnitt direkt på Umbrel, antingen applikationen `Lightning Node` eller gränssnittet `ThunderHub`. Dessa verktyg fungerar för att skicka och ta emot betalningar, men är uppenbarligen inte optimerade för vardagliga Lightning-betalningar. Gränssnittet är utformat för användning på en dator, opraktiskt på en smartphone, och kräver också en anslutning till samma nätverk för att fungera korrekt (även om det är tekniskt möjligt att ansluta på distans via Tor).



I praktiken är det vi bitcoinanvändare letar efter ett klassiskt Lightning wallet-gränssnitt på en smartphone: möjligheten att skanna fakturor via QR-kod och ett enkelt gränssnitt för att betala och ta ut sats pengar. Det är precis vad vi kommer att implementera i det här och nästa kapitel. Den allmänna idén är att ha en mobil Lightning wallet-applikation på din smartphone, som kan användas var som helst (inte bara i ditt lokala nätverk) men som i bakgrunden förlitar sig på din egen Lightning-nod för att skicka och ta emot betalningar.



### Vilka är lösningarna för att ansluta en mobil kund?



Idag finns det flera sätt att göra detta på, både när det gäller mobilapplikationen och typen av anslutning mellan din nod och denna applikation. De tre huvudsakliga anslutningslägena är:




- via ***Tor***;
- via VPN ***Tailscale***;
- via ***Nostr Wallet Connect***.



För några år sedan brukade jag ansluta via ***Tor***, men jag slutade snabbt: antalet misslyckanden och kommunikationsförseningarna var alldeles för stora. I teorin fungerar det, men i praktiken var användarupplevelsen katastrofal. Jag skulle därför vilja avråda från detta tillvägagångssätt.



Det alternativ jag då valde var att använda ett ***Tailscale*** VPN för att säkerställa kommunikationen mellan mobilapplikationen och noden. Denna lösning fungerar mycket bra: även på mobilnät med låg genomströmning går mina betalningar alltid igenom utan problem. Det här är den metod som jag ska introducera först i det här kapitlet, med Zeus-applikationen.



I nästa kapitel tittar vi på en annan, nyare lösning, som också fungerar mycket bra: ***Nostr Wallet Connect***. Den här gången använder vi Alby Go-applikationen för att presentera ett alternativ, även om Zeus också är kompatibel med NWC om du vill.



### Installera och konfigurera Tailscale



För den här första metoden behöver vi Tailscale. Detta är en VPN-lösning baserad på WireGuard, som gör att du säkert kan ansluta enheter som är spridda över Internet, samtidigt som du automatiskt hanterar kryptering, autentisering och NAT-traversal. Enkelt uttryckt är det som om alla dina enheter var anslutna till samma LAN som din router, även om de kan vara var som helst på Internet.



För att använda den måste du först skapa ett konto. Gå till Tailscale:s webbplats och klicka sedan på knappen `Get Started`.



![Image](assets/fr/071.webp)



Välj sedan en identitetsleverantör för ditt Tailscale-konto. Personligen använde jag ett av mina GitHub-konton för att logga in.



![Image](assets/fr/072.webp)



När du har loggat in kommer du att få några frågor om din användning. Besvara dem kortfattat för att fortsätta.



![Image](assets/fr/073.webp)



Tailscale erbjuder sig sedan att installera en klient på din maskin. För tillfället är det inte vad vi är intresserade av: gå direkt till Umbrel och installera Tailscale-applikationen från App Store.



![Image](assets/fr/074.webp)



När applikationen öppnas klickar du på "Logga in" och följer sedan autentiseringsprocessen med samma metod som när du skapade ditt konto.



![Image](assets/fr/075.webp)



Klicka på `Connect` för att bekräfta. Din Umbrel är nu ansluten till ditt VPN-nätverk.



![Image](assets/fr/076.webp)



Ladda sedan ner Tailscale-applikationen till din smartphone och logga in med samma konto. Observera: på Android är det inte möjligt att använda två VPN samtidigt. För att Tailscale ska fungera måste du inaktivera alla andra aktiva VPN. Varje gång du vill använda din Lightning-nod via Zeus måste du dessutom aktivera Tailscale VPN, annars kommer anslutningen inte att upprättas.



![Image](assets/fr/077.webp)



På Tailscale-platsen, nu när minst två klienter är anslutna, kan du komma åt administrationskonsolen med en lista över alla dina enheter som är anslutna till nätverket och deras Tailscale IP-adresser.



![Image](assets/fr/078.webp)



### Anslut Zeus



Installera Zeus-applikationen på din telefon. När den öppnas väljer du "Avancerad inställning" och sedan "Skapa eller anslut en wallet".



![Image](assets/fr/079.webp)



I avsnittet `Wallet interface` väljer du `LND (REST)`. Ange sedan Tailscale-adressen för din Umbrel, som du kan hitta från din Tailscale-instrumentpanel eller direkt i Tailscale-applikationen på Umbrel. För porten anger du `8080`.



![Image](assets/fr/080.webp)



Zeus ber dig sedan att tillhandahålla en `Macaroon`. Detta är en auktorisering token som gör att du exakt kan definiera de rättigheter som beviljas en applikation (i detta fall Zeus) för att interagera med din Lightning-nod. Det är möjligt att generate en macaroon från ThunderHub, i menyn `Tools`, undermenyn `Bakery`, men för detta ändamål är det enklaste sättet att hämta den direkt från applikationen `Lightning Node`.



Klicka på de tre små prickarna längst upp till höger i gränssnittet och sedan på `Connect Wallet`. Välj `REST (lokalt nätverk)`. Du kommer då att kunna kopiera en macaroon med rätt rättigheter.



![Image](assets/fr/081.webp)



Klistra in den i motsvarande fält i Zeus och klicka sedan på knappen `SAVE WALLET CONFIG`.



![Image](assets/fr/082.webp)



Du kan nu komma åt din Lightning-nod från Zeus-appen. Det innebär att du kan generate fakturor för att ta emot betalningar direkt på din Lightning-nod från din smartphone, och även betala Lightning-fakturor var du än befinner dig.



![Image](assets/fr/083.webp)



Tips: Tailscale är inte begränsad till att använda din Lightning-nod på distans. Den låter dig komma åt alla Umbrel:s verktyg från annan programvara, även på distans. Du kan till exempel använda IP-adressen Tailscale i din Umbrel för att ansluta din Bitcoin-nod (via Electrs eller Fulcrum) till Sparrow Wallet, utan att gå via Tor. Återigen undviker detta den långsamhet som är inbyggd i Tor. Installera helt enkelt Tailscale-klienten på din dator och anslut den till ditt nätverk.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

I nästa kapitel tittar vi på ett annat, lika effektivt sätt att ansluta en mobil klient till din Lightning-nod: Nostr Wallet Connect. Vi kommer att använda en annan applikation än Zeus (även om Zeus också är kompatibel med NWC), nämligen Alby Go.



## Anslut en mobil wallet via NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Om du inte är övertygad om Tailscale-anslutningen, eller om det verkar för krångligt att hantera ett dubbelt VPN, föreslår det här kapitlet ett annat sätt att använda en mobil fjärrklient för att betala för och ta emot sats via din Lightning-nod: ***Nostr Wallet Anslut***.



I det här exemplet kommer vi att använda mobilapplikationen Alby Go, som är mycket väl utformad och särskilt lätt att lära sig. Med det sagt kan du också använda Zeus eller någon annan NWC-kompatibel mobilapplikation. Du hittar en lista över kompatibla applikationer på [the `awesome-nwc` GitHub repository] (https://github.com/getAlby/awesome-nwc).



### Hur fungerar Nostr Wallet Connect?



Nostr Wallet Connect är ett standardiserat protokoll som gör det möjligt för en applikation eller webbplats att utlösa åtgärder på en avlägsen Lightning-nod, utan att upprätta en direkt nätverksanslutning till den noden (ingen API LND exponerad, ingen VPN, ingen `.onion`-tjänst ...). NWC definierar hur en applikation formulerar en avsikt (t.ex. `pay_intece`) och tar emot resultatet.



Det fungerar ganska enkelt. Du initierar en session genom att skanna en QR-kod eller via en deeplink `nostr+walletconnect:`. Den här strängen innehåller sessionsparametrarna och en auktoriseringshemlighet. När applikationen sedan vill betala serialiserar den begäran, krypterar den och publicerar den som en händelse på ett Nostr-relä. Noden läser händelsen på reläet, dekrypterar den, kontrollerar att författaren är auktoriserad för den här sessionen, utför betalningen och returnerar sedan ett krypterat svar (framgång med preimage eller fel). Reläet fungerar bara som en transportförmedlare: det kan inte läsa innehållet, men det kan observera tidpunkten och frekvensen för förfrågningar.



Jämfört med en anslutning via Tailscale eller Tor är den största fördelen med NWC att din nod inte är direkt nåbar från utsidan. Detta förenklar mobil användning avsevärt: din nod behöver inte acceptera inkommande anslutningar, den behöver bara kunna kommunicera med ett relä. Å andra sidan introducerar du ett funktionellt beroende av Nostr-reläer: om de inte är tillgängliga försämras upplevelsen. Även om meddelanden är krypterade kan reläet observera en viss nivå av aktivitetsmetadata.



Skillnaden i säkerhetsmodeller är också viktig. Med Tailscale eller Tor exponerar du direkt åtkomst till din nod (via API eller LND) som skyddas av mycket känsliga hemligheter. Detta är kraftfullt, eftersom du kan administrera allt, men det är också en attackyta på lägre nivåer. Med NWC är åtkomsten mer tillämpningsbar: du delegerar en session token som endast godkänner vissa åtgärder.



### Installera Alby Hub på din Lightning-nod



Tidigare fanns det en applikation som var särskilt avsedd för NWC-anslutningar i Umbrel App Store, men tyvärr är den inte längre tillgänglig. Du måste nu använda Alby Hub för att upprätta den här typen av anslutning. För att göra detta börjar du med att installera Alby Hub-applikationen direkt från butiken.



![Image](assets/fr/091.webp)



När du öppnar programmet hoppar du över de inledande skärmarna och klickar sedan på knappen `Get Started (LND)`. Det är viktigt att kontrollera att det står `LND`, inte `LDK`, inom parentes. Om `LND` visas betyder det att Alby Hub korrekt har upptäckt din befintliga Lightning-nod och kommer att konfigurera sig själv som gränssnitt för den. Om däremot `LDK` visas, indikerar det att Alby Hub inte har upptäckt din nod och är på väg att skapa en ny, vilket inte är syftet här.



![Image](assets/fr/092.webp)



Du kommer sedan att bli ombedd att skapa ett Alby-konto. För användning som är begränsad till NWC är detta inte nödvändigt, men du kanske vill göra det om du vill dra nytta av Alby:s specifika tjänster. Om inte, klicka på `Möjligen senare` för att fortsätta.



![Image](assets/fr/093.webp)



Välj sedan ett starkt, unikt lösenord. Detta kommer att skydda åtkomsten till Alby Hub på din nod. Kom ihåg att spara det i din lösenordshanterare.



![Image](assets/fr/094.webp)



Nu kommer du till gränssnittet för Alby Hub. Du behöver inte gå igenom hela konfigurationsprocessen, såvida du inte vill använda den som huvudhanterare för din Lightning-nod. Som vi såg tidigare kan Alby Hub i själva verket ersätta användningen av ThunderHub för administrationen av din nod. Om du vill ta reda på mer om Alby Hub:s alternativ kan du ta en titt på vår dedikerade handledning:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Gå till menyn `Connections`.



![Image](assets/fr/095.webp)



Här kan du se alla program som kan ansluta till din Lightning-nod via NWC. Bland dessa finns Zeus, som redan nämnts i föregående kapitel. Här kommer vi att använda Alby Go. Klicka på Alby Go och sedan på knappen `Connect to Alby Go` för att starta anslutningsprocessen.



![Image](assets/fr/096.webp)



### Installera och ansluta Alby Go



Installera applikationen Alby Go på din smartphone:




- [Google Play Store] (https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store] (https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore] (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



I Alby Hub konfigurerar du de rättigheter som du vill ge till Alby Go-programmet på din Lightning-nod. Du kan t.ex. ställa in utgiftsgränser per period, ett utgångsdatum för NWC-länken eller lämna total kontroll. När du har ställt in parametrarna klickar du på knappen `Nästa`.



![Image](assets/fr/097.webp)



Alby Hub generate:ar sedan en QR-kod för att upprätta NWC-anslutningen mellan din Lightning-nod och Alby Go.



![Image](assets/fr/098.webp)



I Alby Go-applikationen, när den först öppnas, klickar du på `Connect Wallet` och skannar sedan QR-koden som tillhandahålls av Alby Hub.



![Image](assets/fr/099.webp)



Välj ett namn för att identifiera denna wallet. Du har nu fjärråtkomst till din Lightning-nod via Alby Go. Du kan generate fakturor för att ta emot sats på din nod, eller ställa Lightning-fakturor direkt med den.



![Image](assets/fr/100.webp)



Jag skickade t.ex. 1543 sats från gränssnittet Alby Go.



![Image](assets/fr/101.webp)



Om jag går till det grundläggande gränssnittet för min Lightning-nod på Umbrel kan jag se att den här betalningen verkligen har gjorts av min nod.



![Image](assets/fr/102.webp)



Nu vet du hur du enkelt kan använda din Lightning-nod var du än befinner dig.



## Långvarig autonomi på Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Vi har nu kommit till slutet av denna praktiska LNP202-kurs. Du har nu de grunder du behöver för att använda Lightning Network på ett suveränt sätt: du förstår den verkliga rollen för en nod, avvägningarna mellan olika tillvägagångssätt och du har satt upp en LND-instans på Umbrel med en konsekvent säkerhetskopierings- och skyddsstrategi. Du har också öppnat dina första kanaler, lärt dig hur du hanterar likviditet och hur du gör dina betalningar tillförlitliga på daglig basis.



Ur driftssynpunkt bör din nod nu gå in i en underhållsrytm. Det viktigaste är att övervaka den (drifttid, synkronisering, kanalstatus, betalningsfel etc.), tillämpa de uppdateringar som erbjuds av Umbrel när stabila versioner finns tillgängliga och regelbundet kontrollera att dina säkerhetskopior och din vakttornskonfiguration fortfarande är aktiva.



När det gäller kanaler bör du ha en pragmatisk inställning: behåll de som är användbara för dig, stäng de som är permanent inaktiva eller associerade med instabila kollegor och omfördela gradvis ditt kapital mot en mer robust topologi.



**En av de vanligaste fallgroparna i det här skedet är att avsätta för mycket kapital till din Lightning-nod. Tänk på att din Lightning-nod är mycket mindre säker än en hårdvaru-wallet, och att tillgången på medel som avsatts till dina kanaler är beroende av säkerhetskopieringsmekanismer som fortfarande är ofullkomliga. Det är därför mycket viktigt att hålla sig till rimliga belopp, som du har råd att förlora i händelse av ett problem, och alltid hålla majoriteten av din sats på en onchain-hårdvarug wallet.



När det gäller verktyg rekommenderar jag att du är nyfiken och uppmärksam på nya utvecklingar. I det här utbildningstillfället upptäckte vi flera av dem, oavsett om det gäller att hantera din nod, dess anslutning eller fjärranvändning för att göra betalningar. Lightning är dock ett särskilt dynamiskt område. Varje år dyker det upp nya och relevanta verktyg, och många nya applikationer dyker också upp på Umbrel. Om du håller dig uppdaterad om dessa nya utvecklingar kan du upptäcka mer kraftfulla eller mer praktiska lösningar än de som presenteras i den här kursen.



På utbildningsfronten, om du inte redan har gjort det, rekommenderar jag starkt att du går Fanis Michalakis teorikurs LNP 201, som handlar om hur Lightning Network fungerar. Den kommer att hjälpa dig att bättre förstå de manipulationer som utförs i denna LNP202-kurs, och ge dig större förtroende för den dagliga hanteringen av din nod.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

På ett annat sätt, men lika viktigt för din bitcoinresa, rekommenderar jag också Ludovic Lars utmärkta kurs om historien bakom skapandet av Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Men innan du går vidare kan du skriva en recension av denna LNP202-kurs och naturligtvis ta examen för att bekräfta att du har förstått allt dess innehåll.



# Sista delen


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Recensioner & betyg


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Slutlig examination


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Slutsats


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>