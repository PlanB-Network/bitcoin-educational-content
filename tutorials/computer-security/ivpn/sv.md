---
name: IVPN
description: Konfigurera ett VPN som betalats med bitcoins
---
![cover](assets/cover.webp)


Ett VPN ("*Virtual Private Network*") är en tjänst som upprättar en säker och krypterad anslutning mellan din telefon eller dator och en fjärrserver som hanteras av VPN-leverantören.


När du ansluter till ett VPN omdirigeras din internettrafik tekniskt sett genom en krypterad tunnel till VPN-servern. Denna process gör det svårt för tredje part, såsom Internetleverantörer (ISP) eller skadliga aktörer, att fånga upp eller läsa dina data. VPN-servern fungerar sedan som en mellanhand som ansluter till den tjänst du vill använda för din räkning. Den tilldelar en ny IP Address till din anslutning, vilket hjälper till att dölja din riktiga IP Address från de webbplatser du besöker. Men i motsats till vad vissa onlineannonser kan föreslå, kan du inte surfa anonymt på internet genom att använda ett VPN, eftersom det kräver en form av förtroende för VPN-leverantören som kan se all din trafik.

![IVPN](assets/fr/01.webp)

Fördelarna med att använda ett VPN är många. För det första skyddar det integriteten för din onlineaktivitet från internetleverantörer eller regeringar, förutsatt att VPN-leverantören inte delar din information. För det andra säkrar det dina data, särskilt när du är ansluten till offentliga Wi-Fi-nätverk, som är sårbara för MITM-attacker (man-in-the-middle). För det tredje gör ett VPN att du kan kringgå geografiska begränsningar och censur genom att dölja din IP Address och få tillgång till innehåll som annars inte skulle vara tillgängligt eller blockerat i din region.


Som du kan se flyttar VPN risken för trafikobservation till VPN-leverantören. När du väljer din VPN-leverantör är det därför viktigt att överväga de personuppgifter som krävs för registrering. Om leverantören ber om information som ditt telefonnummer, e-post Address, bankkortsuppgifter, eller ännu värre, din post Address, ökar risken för att din identitet associeras med din trafik. I händelse av att leverantören utsätts för intrång eller ett rättsligt beslag skulle det vara lätt att koppla samman din trafik med dina personuppgifter. Därför rekommenderas att du väljer en leverantör som inte kräver några personuppgifter och som accepterar anonyma betalningar, t.ex. med bitcoins.


I den här handledningen presenterar jag en enkel, effektiv och prisvärd VPN-lösning som inte kräver någon personlig information för att användas.


## Introduktion till IVPN


IVPN är en VPN-tjänst som är utformad speciellt för användare som söker en form av integritet. Till skillnad från populära VPN-leverantörer som ofta marknadsförs på YouTube, sticker IVPN ut för sin transparens, säkerhet och respekt för integritet.

IVPN:s integritetspolicy är strikt: ingen personlig information krävs vid registrering. Du kan öppna ett konto utan att ange e-post Address, namn eller telefonnummer. För betalning är det inte nödvändigt att ange kreditkortsuppgifter, eftersom IVPN accepterar betalningar i bitcoins (onchain och Lightning). Dessutom hävdar IVPN att de inte för några aktivitetsloggar, vilket innebär att din internettrafik i teorin inte registreras av företaget.

IVPN är också [helt öppen källkod](https://github.com/ivpn), gällande deras mjukvara, applikationer och till och med deras hemsida, vilket tillåter vem som helst att verifiera och granska deras kod. De genomgår också oberoende säkerhetsrevisioner varje år, vars resultat publiceras på deras webbplats.


IVPN använder sig uteslutande av egenhyrda servrar, vilket eliminerar riskerna med att använda molntjänster från tredje part, såsom AWS, Google Cloud eller Microsoft Azure.


Tjänsten erbjuder många avancerade funktioner, till exempel multi-hop, som dirigerar trafik genom flera servrar i olika jurisdiktioner för att förbättra anonymiteten. IVPN integrerar också en tracker och annonsblockerare, och erbjuder möjligheten att välja mellan olika VPN-protokoll.


Naturligtvis kostar denna kvalitet på tjänsterna, men ett adekvat pris är ofta en indikator på kvalitet och ärlighet. Det kan signalera att företaget har en affärsmodell utan behov av att sälja personuppgifter. IVPN erbjuder sedan 2 typer av planer: Standardplanen, som tillåter anslutning av upp till 2 enheter, och Pro-planen, som tillåter upp till 7 anslutningar och inkluderar "*Multi-hop*"-protokollet som dirigerar din trafik genom flera servrar.


Till skillnad från vanliga VPN-leverantörer fungerar IVPN enligt en modell där man köper åtkomsttid till tjänsten, snarare än en återkommande prenumeration. Du betalar i bitcoins en gång för den valda varaktigheten. Om du till exempel köper ett års åtkomst kan du använda tjänsten under den perioden, varefter du måste återvända till IVPN:s webbplats för att köpa mer åtkomsttid.


IVPN-priserna](https://www.ivpn.net/en/pricing/) är progressiva beroende på den köpta åtkomsttiden. Här är priserna för Standard-planen:


- 1 vecka: $2
- 1 månad: $6
- 1 år: $60
- 2 år: $100
- 3 år: $140


Och för Pro-planen:


- 1 vecka: $4
- 1 månad: $10
- 1 år: $100
- 2 år: $160
- 3 år: $220


## Hur installerar jag IVPN på en dator?

Ladda ner [den senaste versionen av programvaran](https://www.ivpn.net/en/apps-windows/) för ditt operativsystem och fortsätt sedan med installationen genom att följa stegen i installationsguiden. ![IVPN](tillgångar/notext/02.webp)

För Linux-användare, se de instruktioner som är specifika för din distribution som finns på [denna sida] (https://www.ivpn.net/en/apps-linux/).

![IVPN](assets/notext/03.webp)

När installationen är klar måste du ange ditt konto-ID. Vi kommer att se hur du får det i de följande avsnitten i denna handledning.

![IVPN](assets/notext/04.webp)

## Hur installerar jag IVPN på en smartphone?


Ladda ner IVPN från din appbutik, oavsett om det är [AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683) för iOS-användare, [Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client) för Android eller [F-Droid](https://f-droid.org/en/packages/net.ivpn.client). Om du använder Android har du också möjlighet att ladda ner `.apk` filen direkt från [IVPN:s webbplats](https://www.ivpn.net/en/apps-android/).

![IVPN](assets/notext/05.webp)

Vid första användningen av appen kommer du att loggas ut. Du måste ange ditt konto-ID för att aktivera tjänsten.

![IVPN](assets/notext/06.webp)

Låt oss nu gå vidare till att aktivera IVPN på dina enheter.


## Hur betalar jag för och aktiverar IVPN?


Gå till IVPN:s officiella webbplats [på betalningssidan] (https://www.ivpn.net/en/pricing/).

![IVPN](assets/notext/07.webp)

Välj den plan som bäst passar dina behov. För denna handledning kommer vi att välja Standard-planen, som gör att vi kan aktivera VPN på vår dator och smartphone, till exempel.

![IVPN](assets/notext/08.webp)

IVPN kommer sedan att skapa ditt konto. Du behöver inte ange några personuppgifter. Det är endast ditt konto-ID som gör att du kan logga in. Det fungerar ungefär som en accessnyckel. Spara det på ett säkert ställe som till exempel i din lösenordshanterare. Du kan också göra en papperskopia.

![IVPN](assets/notext/09.webp)

På samma sida väljer du hur länge du vill abonnera på tjänsten.

![IVPN](assets/notext/10.webp)

Välj sedan din betalningsmetod. För min del kommer jag att göra betalningen via Lightning Network, så jag klickar på "* Bitcoin *" -knappen.

![IVPN](assets/notext/11.webp)

Kontrollera att allt är som du vill ha det och klicka sedan på knappen "*Pay with Lightning*".

![IVPN](assets/notext/12.webp)

En Lightning Invoice kommer att presenteras för dig på deras BTCPay-server. Skanna QR-koden med din Lightning Wallet och fortsätt med betalningen.

![IVPN](assets/notext/13.webp) Once the invoice is paid, click on the "*Return to IVPN*" button.

![IVPN](assets/notext/14.webp)

Ditt konto visas nu som "*Active*", och du kan se det datum fram till vilket din tillgång till VPN är giltig. Efter det här datumet måste du förnya din betalning.

![IVPN](assets/notext/15.webp)

För att aktivera din anslutning via IVPN på din dator, kopiera bara ditt konto-ID.

![IVPN](assets/notext/16.webp)

Och klistra in den i programvaran som du tidigare laddade ner.

![IVPN](assets/notext/17.webp)

Klicka sedan på knappen "*Login*".

![IVPN](assets/notext/18.webp)

Klicka på bocken för att aktivera VPN-anslutningen, och vips är din dators internettrafik krypterad och dirigeras via en IVPN-server.

![IVPN](assets/notext/19.webp)

För din smartphone är proceduren identisk. Klistra in ditt konto-ID eller skanna QR-koden som är kopplad till ditt IVPN-konto som finns tillgängligt på webbplatsen. Klicka sedan på bocken för att upprätta anslutningen.

![IVPN](assets/notext/20.webp)

## Hur använder och konfigurerar jag IVPN?


När det gäller användning och inställningar är det ganska enkelt. Från huvudpanelen Interface kan du aktivera eller avaktivera anslutningen genom att klicka på bockmarkeringen.

![IVPN](assets/notext/21.webp)

Du har också möjlighet att pausa ditt VPN under en viss tid.

![IVPN](assets/notext/22.webp)

Genom att klicka på den aktuella servern kan du välja en annan server bland de tillgängliga.

![IVPN](assets/notext/23.webp)

Det är också möjligt att aktivera eller avaktivera den integrerade brandväggen samt anti-tracker-funktionen.

![IVPN](assets/notext/24.webp)

För att komma åt ytterligare inställningar, klicka på ikonen för inställningar.

![IVPN](assets/notext/25.webp)

På fliken "*Account*" hittar du inställningar som är relaterade till ditt konto.

![IVPN](assets/notext/26.webp)

På fliken "*General*" finns det flera klientinställningar. Jag råder dig att markera alternativen "*Starta vid inloggning*" och "*Vid start*" i avsnittet "*Autoconnect*" för att automatiskt upprätta anslutningen till VPN när du startar din maskin.

![IVPN](assets/notext/27.webp)

På fliken "*Connection*" hittar du olika alternativ som är relaterade till anslutningen. Det är här du kan ändra det VPN-protokoll som används.

![IVPN](assets/notext/28.webp)

På fliken "*IVPN Firewall*" kan du aktivera brandväggen systematiskt vid start av datorn, vilket säkerställer att ingen anslutning upprättas utanför VPN.

![IVPN](assets/notext/29.webp)

Fliken "*Split Tunnel*" ger möjlighet att utesluta viss programvara från VPN-anslutningen. Program som läggs till här kommer att fortsätta att fungera med en normal internetanslutning även när VPN är aktiverat.

![IVPN](assets/notext/30.webp)

På fliken "*WiFi control*" har du möjlighet att konfigurera specifika åtgärder beroende på vilka nätverk du är ansluten till. Du kan t.ex. ange ditt hemnätverk som "*Trusted*" och konfigurera VPN så att det inte aktiveras på det här nätverket, men automatiskt aktiveras på alla andra WiFi-nätverk.

![IVPN](assets/notext/31.webp)

I menyn "*AntiTracker*" väljer du blockeringsprofilen för din anti-tracker. Detta är utformat för att blockera annonser, skadlig kod och dataspårare genom att blockera förfrågningar till spårningstjänster medan du surfar på Internet. Detta förbättrar din integritet genom att förhindra företag från att samla in och sälja dina surfdata. Ett "*Hardcore Mode*" är också tillgängligt för att helt blockera alla domäner som ägs av Google och Meta, liksom alla beroende tjänster.

![IVPN](assets/notext/32.webp)

Och där har du det, du är nu utrustad för att njuta fullt ut av IVPN. Om du också vill förbättra säkerheten för dina onlinekonton genom att använda en lokal lösenordshanterare, så inbjuder jag dig att kolla in vår handledning om KeePass, en gratis lösning med öppen källkod:


https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Om du är intresserad av att upptäcka en annan VPN-leverantör som liknar IVPN, både när det gäller funktioner och prissättning, rekommenderar jag också att du tittar på vår handledning om Mullvad:


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8