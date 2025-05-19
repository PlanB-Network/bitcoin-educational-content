---
name: Tor webbläsare
description: Hur använder man Tor Browser?
---
![cover](assets/cover.webp)


Som namnet antyder är en webbläsare en programvara som används för att navigera på Internet. Den fungerar som en port mellan användarens dator och webben och översätter koden på webbplatser till interaktiva och läsbara sidor. Valet av webbläsare är mycket viktigt, eftersom det inte bara påverkar din surfupplevelse utan också din säkerhet och integritet på nätet.


Var försiktig så att du inte blandar ihop webbläsaren med sökmotorn. Webbläsaren är den programvara som du använder för att komma åt Internet (som Chrome eller Firefox), medan sökmotorn är en tjänst, som till exempel Google eller Bing, som hjälper dig att hitta information online.


Idag är Google Chrome den överlägset mest använda webbläsaren. Den står för cirka 65% av den globala marknaden år 2024. Chrome uppskattas för sin snabbhet och prestanda, men det är inte nödvändigtvis det bästa valet för alla, särskilt inte om du prioriterar integritet. Chrome tillhör Google, ett företag som är känt för att samla in och analysera enorma mängder data om sina användare. Och deras interna webbläsare är faktiskt kärnan i deras övervakningsstrategi. Den här programvaran är en central komponent i de flesta av dina onlineinteraktioner. Att bemästra datainsamling i din webbläsare är en viktig fråga för Google.

![TOR BROWSER](assets/notext/01.webp)

*Källa: [gs.statcounter.com [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*


Det finns flera stora familjer av webbläsare, var och en baserad på en specifik renderingsmotor. Webbläsare som Google Chrome, Microsoft Edge, Brave, Opera eller Vivaldi är alla etablerade på Chromium-webbläsaren, en lätt och öppen källkodsversion av Chrome som utvecklats av Google. Alla dessa webbläsare använder renderingsmotorn Blink, som är en Fork av WebKit, som i sin tur härstammar från KHTML. Chromiums dominans på marknaden gör webbläsare som härrör från den särskilt effektiva, eftersom webbutvecklare tenderar att optimera sina webbplatser främst för Blink.


Safari, Apples webbläsare, använder WebKit, som också kommer från KHTML.


Å andra sidan förlitar sig webbläsare som Mozilla Firefox, LibreWolf och Tor Browser på Gecko, en annan renderingsmotor som ursprungligen kommer från webbläsaren Netscape.


Att välja rätt webbläsare beror på dina behov. Men om du åtminstone är bekymrad över din integritet, och därmed din säkerhet, rekommenderar jag att du använder Firefox för allmän användning och Tor Browser för ännu mer integritet. I den här handledningen kommer jag att visa dig hur du enkelt kommer igång med Tor Browser.

![TOR BROWSER](assets/notext/02.webp)


## Introduktion till Tor Browser


Tor Browser är en webbläsare som är särskilt utformad för säker och så privat Internetnavigering som möjligt. Webbläsaren är baserad på Firefox och därmed på renderingsmotorn Gecko.

Tor Browser använder Tor-nätverket för att kryptera och dirigera din trafik genom flera reläservrar innan den överförs till destinationen. Denna process med routing i flera lager, känd som "*onion routing*", hjälper till att dölja din riktiga IP Address, vilket gör det svårt att identifiera din plats och dina onlineaktiviteter. Det går dock långsammare att surfa än med en vanlig webbläsare som inte använder Tor-nätverket, eftersom det är indirekt.

Till skillnad från andra webbläsare har Tor Browser särskilda funktioner för att förhindra spårning av dina aktiviteter på nätet, t.ex. genom att isolera varje besökt webbplats och automatiskt radera cookies och historik när du stänger webbläsaren. Den är också utformad för att minimera riskerna med fingeravtryck genom att alla användare ser så lika ut som möjligt som de webbplatser som besöks.


Du kan mycket väl använda Tor Browser för att komma åt en standardwebbplats (`.com`, `.org`, etc.). I det här fallet anonymiseras din trafik genom att passera genom flera Tor-noder innan du når en utgångsnod som kommunicerar med den slutliga webbplatsen på clearnet.

![TOR BROWSER](assets/notext/03.webp)

Du kan också använda Tor Browser för att komma åt dolda tjänster (adresser som slutar på `.onion`). I det här scenariot förblir all trafik inom Tor-nätverket, utan en utgångsnod, vilket garanterar total integritet för både användaren och destinationsservern. Det här arbetssättet används framför allt för att komma åt det som ibland kallas "*dark web*", en del av Internet som inte indexeras av traditionella sökmotorer.

![TOR BROWSER](assets/notext/04.webp)


## Vad är skillnaden mellan Tor-nätverket och Tor-webbläsaren?


Tor-nätverket och Tor-webbläsaren är två skilda saker som inte bör förväxlas, men de kompletterar varandra. Tor-nätverket är en global infrastruktur av reläservrar, som drivs av användare, som anonymiserar internettrafik genom att skicka den genom flera noder innan den dirigeras till sin slutdestination. Detta är den berömda onion-routingen.


Tor-webbläsaren är å andra sidan en särskild webbläsare som är utformad för att underlätta åtkomsten till detta nätverk på ett enkelt sätt. Den integrerar som standard alla nödvändiga inställningar för att ansluta till Tor-nätverket och använder en modifierad version av Firefox för att ge en bekant surfupplevelse samtidigt som den maximerar integritet och säkerhet.


Tor-nätverket används inte bara av Tor-webbläsaren. Det kan användas av olika program och applikationer för att säkra deras kommunikation. Det är t.ex. möjligt att aktivera kommunikation via Tor-nätverket på din Bitcoin-nod för att dölja din IP Address för andra användare och förhindra att din internetleverantör övervakar din Bitcoin-relaterade trafik.

Sammanfattningsvis är Tor-nätverket den infrastruktur som ger oss integritet när vi surfar på internet, och Tor Browser är den programvara som gör att vi kan använda nätverket som en del av vår webbsökning.


## Hur installerar jag Tor Browser?


Tor Browser finns tillgänglig för Windows, Linux och macOS för datorer, samt för Android på smartphones. För att installera Tor Browser på din dator, besök [den officiella Tor Project-webbplatsen] (https://www.torproject.org/).

![TOR BROWSER](assets/notext/05.webp)

Klicka på knappen "*Download Tor Browser*".

![TOR BROWSER](assets/notext/06.webp)

Välj den version som är lämplig för ditt operativsystem.

![TOR BROWSER](assets/notext/07.webp)

Klicka på den körbara filen för att starta installationen och välj sedan ditt språk.

![TOR BROWSER](assets/notext/08.webp)

Välj den mapp där programvaran ska installeras och klicka sedan på knappen "*Install*".

![TOR BROWSER](assets/notext/09.webp)

Vänta tills installationen är klar.

![TOR BROWSER](assets/notext/10.webp)

Klicka till sist på knappen "*Finish*".

![TOR BROWSER](assets/notext/11.webp)


## Hur använder jag Tor Browser?


Tor Browser används som en vanlig webbläsare.

![TOR BROWSER](assets/notext/12.webp)

När webbläsaren startas första gången visas en sida där du uppmanas att ansluta till Tor-nätverket. Klicka bara på knappen "*Connect*" för att upprätta anslutningen.

![TOR BROWSER](assets/notext/13.webp)

Om du vill att programmet automatiskt ska ansluta till Tor-nätverket när du använder det i framtiden markerar du alternativet "*Alltid ansluta automatiskt*".

![TOR BROWSER](assets/notext/14.webp)

När du är ansluten till Tor-nätverket kommer du till startsidan.

![TOR BROWSER](assets/notext/15.webp)

För att göra en sökning på Internet skriver du bara in din fråga i sökfältet och trycker på "*enter*".

![TOR BROWSER](assets/notext/16.webp)

Sedan får du resultaten från din sökmotor på samma sätt som med andra webbläsare.

![TOR BROWSER](assets/notext/17.webp)

Med alternativet "*Onionize*" på DuckDuckGo kan du använda sökmotorn via dess dolda tjänst på Tor-nätverket, genom att komma åt dess `.onion` Address.

![TOR BROWSER](assets/notext/18.webp)


## Hur konfigurerar jag Tor Browser?


Längst upp på webbläsarens skärm hittar du ett alternativ för att importera dina favoriter. Detta gör att du automatiskt kan integrera bokmärkena från din gamla webbläsare till Tor Browser.

![TOR BROWSER](assets/notext/19.webp)

Du har också möjlighet att lägga till nya bokmärken genom att klicka på stjärnikonen längst upp till höger på den webbsida du besöker.

![TOR BROWSER](assets/notext/20.webp)

I menyn till höger har du tillgång till olika alternativ.

![TOR BROWSER](assets/notext/21.webp)The "*New identity*" button allows you to change your Tor identity. Specifically, this enables you to start a new user session on Tor, meaning changing your IP address and resetting cookies and open sessions.

![TOR BROWSER](assets/notext/22.webp)

I menyn "*Bokmärken*" kan du hantera dina bokmärken.

![TOR BROWSER](assets/notext/23.webp)

"*History*" ger dig tillgång till din webbhistorik om du har aktiverat den i inställningarna.

![TOR BROWSER](assets/notext/24.webp)

I menyn "*Add-ons and themes*" kan du anpassa utseendet på din webbläsare eller lägga till tillägg. Eftersom Tor Browser är baserad på Mozilla Firefox kan du använda teman och tillägg som finns för Firefox.

![TOR BROWSER](assets/notext/25.webp)

Slutligen ger knappen "*Settings*" dig tillgång till inställningarna för din webbläsare.

![TOR BROWSER](assets/notext/26.webp)

På fliken "*General*" i inställningarna finns det olika alternativ som gör att du kan anpassa Tor Browser-användaren Interface.

![TOR BROWSER](assets/notext/27.webp)

På fliken "*Home*" kan du välja att ändra den standardsida som visas när du öppnar Tor Browser och när du öppnar nya flikar.

![TOR BROWSER](assets/notext/28.webp)

På fliken "*Search*" kan du välja sökmotor. Tor Browser använder som standard DuckDuckGo, en sökmotor som fokuserar på att skydda användarnas integritet, men du kan också välja till exempel Google eller Startpage.

![TOR BROWSER](assets/notext/29.webp)

Du kan också ställa in genvägar i din sökmotor.

![TOR BROWSER](assets/notext/30.webp)

Du kan t.ex. skriva "*@wikipedia*" följt av ditt sökord, t.ex. "*Bitcoin*", i webbläsarens sökfält.

![TOR BROWSER](assets/notext/31.webp)

Denna funktion utför sedan en sökning efter din term direkt på Wikipedia-webbplatsen.

![TOR BROWSER](assets/notext/32.webp)

Du kan alltså skapa andra anpassade genvägar för olika webbplatser.


På fliken "*Privacy & Security*" hittar du sedan alla inställningar som rör integritet och säkerhet.

![TOR BROWSER](assets/notext/33.webp)

Du har möjlighet att behålla eller radera din webbhistorik.

![TOR BROWSER](assets/notext/34.webp)

Du kan också hantera de åtkomstbehörigheter som du ger till olika webbplatser.

![TOR BROWSER](assets/notext/35.webp)

För att öka den övergripande säkerheten i din webbläsare kan du i lägena "*Safer*" och "*Safest*" justera webbfunktioner och skript som körs av de webbplatser du besöker. Detta minimerar riskerna för att utnyttja sårbarheter, men det kommer också att påverka visningen och interaktiviteten på webbplatserna i gengäld. ![TOR BROWSER](assets/notext/36.webp) Du hittar andra säkerhetsalternativ, inklusive en blockering av farligt innehåll och HTTPS-only-läget, som säkerställer att anslutningar till webbplatser konsekvent respekterar detta protokoll. ![TOR BROWSER](assets/notext/37.webp) Slutligen, på fliken "*Connection*", hittar du alla inställningar som är relaterade till anslutning till Tor-nätverket. Det är här du kan konfigurera en brygga för att komma åt Tor från regioner där dess åtkomst kan censureras. ![TOR BROWSER](assets/notext/38.webp) Så där ja, nu är du redo att navigera på Internet på ett säkrare och mer privat sätt! Om integritet online är ett ämne som intresserar dig, rekommenderar jag också att du upptäcker den här andra handledningen på Mullvad VPN:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8