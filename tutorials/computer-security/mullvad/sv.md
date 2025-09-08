---
name: Mullvad VPN
description: Konfigurera ett VPN som betalats med bitcoins
---
![cover](assets/cover.webp)


Ett VPN ("*Virtual Private Network*") är en tjänst som upprättar en säker och krypterad anslutning mellan din telefon eller dator och en fjärrserver som hanteras av en VPN-leverantör.


När du ansluter till ett VPN omdirigeras din internettrafik tekniskt sett genom en krypterad tunnel till VPN-servern. Denna process gör det svårt för tredje part, såsom Internetleverantörer (ISP) eller skadliga aktörer, att fånga upp eller läsa dina data. VPN-servern fungerar sedan som en mellanhand som ansluter till den tjänst du vill använda för din räkning. Den tilldelar en ny IP Address till din anslutning, vilket hjälper till att dölja din riktiga IP Address från de webbplatser du besöker. Men i motsats till vad vissa onlineannonser kan föreslå, kan du inte surfa anonymt på internet genom att använda ett VPN, eftersom det kräver en viss nivå av förtroende för VPN-leverantören som kan se all din trafik.

![MULLVAD VPN](assets/fr/01.webp)

Fördelarna med att använda ett VPN är många. För det första skyddar det integriteten för din onlineaktivitet från internetleverantörer eller regeringar, förutsatt att VPN-leverantören inte delar din information. För det andra säkrar det dina data, särskilt när du är ansluten till offentliga Wi-Fi-nätverk, som är sårbara för MITM-attacker ("**man-in-the-middle**"). För det tredje gör ett VPN att du kan kringgå geografiska begränsningar och censur genom att dölja din IP Address och få tillgång till innehåll som annars inte skulle vara tillgängligt eller blockerat i din region.


Som du kan se flyttar VPN risken för trafikobservation till VPN-leverantören. När du väljer din VPN-leverantör är det därför viktigt att överväga de personuppgifter som krävs för registrering. Om leverantören ber om information som ditt telefonnummer, e-post Address, bankkortsuppgifter, eller ännu värre, din post Address, ökar risken för att din identitet kopplas till din trafik. I händelse av att leverantören utsätts för intrång eller ett rättsligt beslag skulle det vara lätt att koppla samman din trafik med dina personuppgifter. Därför rekommenderas att du väljer en leverantör som inte kräver någon personlig information och som accepterar anonyma betalningar, till exempel med bitcoins.


I den här handledningen kommer jag att presentera en enkel, effektiv och prisvärd VPN-lösning som inte kräver någon personlig information för att användas.


## Introduktion till Mullvad VPN

Mullvad VPN är en svensk tjänst som utmärker sig genom sin Commitment-strategi för användarnas integritet. Till skillnad från vanliga VPN-leverantörer kräver Mullvad inga personuppgifter vid registreringen. Det finns inget behov av att tillhandahålla ett e-post Address, telefonnummer eller namn; istället tilldelar Mullvad dig ett anonymt kontonummer som används för betalning och åtkomst till tjänsten. Dessutom hävdar Mullvad att de inte för några aktivitetsloggar som passerar genom deras servrar.

![MULLVAD VPN](assets/notext/02.webp)

För betalning är det inte nödvändigtvis nödvändigt att ange kreditkortsinformation, eftersom Mullvad accepterar Bitcoin-betalningar (endast på kedjan på deras officiella webbplats, men det finns en inofficiell metod för att betala via Lightning). De accepterar också kontantbetalningar via posten.


Mullvad VPN utmärker sig också genom sin transparens och säkerhet. Deras programvara är öppen källkod och de genomgår regelbundet oberoende säkerhetsrevisioner för att bedöma sina applikationer och infrastruktur, vars resultat [publiceras på deras webbplats] (https://mullvad.net/fr/blog/tag/audits). Företaget bakom Mullvad är baserat i Sverige, ett land som är känt för sina strikta integritetslagar. De använder uteslutande servrar som de själva driver och eliminerar därmed de risker som är förknippade med att använda molntjänster från tredje part, såsom hyperscalers AWS, Google Cloud eller Microsoft Azure.


När det gäller funktioner erbjuder Mullvad allt man förväntar sig av en bra VPN-klient, inklusive en kill switch som skyddar din trafik om VPN kopplas bort, ett alternativ för att inaktivera VPN för specifika applikationer och möjligheten att dirigera din trafik genom flera VPN-servrar.


Naturligtvis kostar den här kvaliteten på tjänsterna, men ett rimligt pris är ofta en indikator på kvalitet och ärlighet. Det kan signalera att företaget har en affärsmodell utan att behöva sälja dina personuppgifter till tredje part. Mullvad VPN erbjuder ett fast pris på 5 euro per månad, användbart på upp till 5 olika enheter.

![MULLVAD VPN](assets/notext/03.webp)

Till skillnad från vanliga VPN-leverantörer har Mullvad en modell för att köpa åtkomsttid till tjänsten snarare än en återkommande, automatisk prenumeration. Du gör helt enkelt en engångsbetalning i bitcoins för den valda varaktigheten. Om du till exempel köper ett års åtkomst kan du använda tjänsten under den perioden, varefter du måste återvända till Mullvads webbplats för att förnya din åtkomsttid.

Jämfört med IVPN, en annan högkvalitativ VPN-leverantör, är Mullvad något mer ekonomiskt. Till exempel, även när man väljer ett treårigt köp med IVPN, uppgår månadskostnaden till cirka € 5,40. IVPN erbjuder dock några ytterligare tjänster och har också en billigare plan än Mullvads (Standardplanen), men den är begränsad till endast 2 enheter och utesluter "multi-hop" -protokollet.

Jag genomförde också några informella hastighetstester för att jämföra IVPN och Mullvad. Även om IVPN visade en liten överlägsenhet när det gäller prestanda, var hastigheterna hos Mullvad fortfarande mycket tillfredsställande. Jämfört med vanliga VPN-leverantörer visade sig IVPN och Mullvad vara minst lika effektiva, om inte överlägsna i vissa fall.


## Hur installerar jag Mullvad VPN på en dator?


Gå till [Mullvads officiella webbplats] (https://mullvad.net/en/download/) och klicka på menyn "*Downloads*".

![MULLVAD VPN](assets/notext/04.webp)

För Windows- eller macOS-användare, ladda ner programvaran direkt från webbplatsen och följ instruktionerna från installationsguiden för att slutföra installationen.

![MULLVAD VPN](assets/notext/05.webp)

Linux-användare kan hitta instruktioner som är specifika för deras distribution i avsnittet ["*Linux*"](https://mullvad.net/en/download/vpn/linux).

![MULLVAD VPN](assets/notext/06.webp)

När installationen är klar måste du ange ditt konto-ID. Vi kommer att se hur du får fram detta i följande avsnitt av denna handledning.


## Hur installerar jag Mullvad VPN på en smartphone?


Ladda ner Mullvad VPN från din appbutik, oavsett om det är [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) för iOS-användare, [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) för Android eller [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). Om du använder Android har du också möjlighet att ladda ner filen `.apk` direkt från [Mullvads webbplats](https://mullvad.net/en/download/vpn/android).

![MULLVAD VPN](assets/notext/07.webp)

Vid första användningen av appen kommer du att loggas ut. Du måste ange ditt konto-ID för att aktivera tjänsten.

![MULLVAD VPN](assets/notext/08.webp)

Låt oss nu gå vidare till att aktivera Mullvad på dina enheter.


## Hur betalar jag för och aktiverar Mullvad VPN?


Gå till [Mullvads officiella webbplats] (https://mullvad.net/) och klicka på knappen "*Get Started*".

![MULLVAD VPN](assets/notext/09.webp)

Klicka på knappen "*generate kontonummer*".

![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.

![MULLVAD VPN](assets/notext/11.webp)

Klicka sedan på knappen "*Lägg till tid på ditt konto*".

![MULLVAD VPN](assets/notext/12.webp)

Du kommer då till inloggningssidan för ditt konto. Ange ditt kontonummer och klicka sedan på knappen "*Logga in*".

![MULLVAD VPN](assets/notext/13.webp)

Välj din betalningsmetod. Jag rekommenderar att du betalar i bitcoins, eftersom du får 10% rabatt, vilket sänker kostnaden till 4,50 € per månad. Om du föredrar att betala via Lightning kommer jag att tillhandahålla en alternativ metod i följande del.

![MULLVAD VPN](assets/notext/14.webp)

Klicka på knappen "*Skapa en engångsbetalning Address*".

![MULLVAD VPN](assets/notext/15.webp)

Betala sedan med din Bitcoin Wallet det belopp som anges till den mottagande Address som du har fått.

![MULLVAD VPN](assets/notext/16.webp)

Det kan ta några minuter innan webbplatsen upptäcker din betalning, efter att transaktionen har bekräftats. När betalningen har registrerats av Mullvad kommer längden på din prenumeration att visas längst upp till vänster på sidan, istället för "*Ingen tid kvar*".

![MULLVAD VPN](assets/notext/17.webp)

Du kan sedan ange ditt kontonummer i programvaran för att aktivera VPN.

![MULLVAD VPN](assets/notext/18.webp)

För att aktivera VPN på din mobilapplikation är processen exakt densamma. Du behöver bara ange ditt kontonummer.

![MULLVAD VPN](assets/notext/19.webp)

## Hur betalar jag för Mullvad VPN med Lightning?


Som du har förstått accepterar Mullvad ännu inte betalningar via Lightning Network. Tack vare en rekommendation från [Lounès](https://x.com/louneskmt) upptäckte jag dock en informell tjänst som gör att du kan kringgå denna begränsning. Denna tjänst, som finns på [vpn.sovereign.engineering](https://vpn.sovereign.engineering/), accepterar dina betalningar på Lightning och ger dig en giltig plan för Mullvad i gengäld.

![MULLVAD VPN](assets/notext/20.webp)

Du har två olika alternativ på den här webbplatsen: du kan lita på webbplatsansvarig och ange ditt kontonummer direkt och sedan klicka på "*Logga in*" för att ditt Mullvad-paket ska valideras automatiskt. Eller så kan du klicka på "*Heck yeah!*"-knappen för att köpa en kupong i Lightning, som du sedan kan använda på den officiella Mullvad-webbplatsen för att få ditt paket. ![MULLVAD VPN](assets/notext/21.webp) I båda fallen kommer du sedan att bli ombedd att välja varaktigheten för ditt paket. Du kan välja mellan 6 månader och 1 år. ![MULLVAD VPN](assets/notext/22.webp) Klicka sedan på knappen "*Top-up with Lightning*". ![MULLVAD VPN](assets/notext/23.webp) För att slutföra köpet betalar du Invoice med din Lightning Wallet. ![MULLVAD VPN](assets/notext/24.webp) Om du valde att köpa en Voucher väljer du "*Voucher*" på Mullvads webbplats bland de betalningsmetoder som finns tillgängliga på ditt konto. Ange sedan Voucher-numret som du fick från vpn.sovereign.engineering-webbplatsen i den angivna rutan. ![MULLVAD VPN](assets/notext/25.webp) ## Hur använder och konfigurerar jag Mullvad VPN?


Nu när du har ett aktivt konto och har angett ditt kontonummer i Mullvads programvara eller app kan du njuta fullt ut av tjänsterna i ditt VPN. ![MULLVAD VPN](assets/notext/26.webp) För att koppla bort från VPN klickar du bara på knappen "*Disconnect*". ![MULLVAD VPN](assets/notext/27.webp) Den lilla röda pilen bredvid "*Disconnect*"-knappen gör att du kan byta server utan att ändra den aktuella platsen. ![MULLVAD VPN](assets/notext/28.webp) Om du vill byta stad för din VPN-server klickar du på "*Switch location*" för att välja en ny plats. ![MULLVAD VPN](assets/notext/29.webp) Längst upp på skärmen ser du din enhets smeknamn samt den återstående tiden för ditt paket. ![MULLVAD VPN](assets/notext/30.webp) Genom att klicka på ikonen för den lilla mannen får du tillgång till detaljerad information om ditt konto. ![MULLVAD VPN](assets/notext/31.webp) Klicka på kugghjulet för att komma åt inställningarna. ![MULLVAD VPN](assets/notext/32.webp) I menyn "*User Interface settings*" kan du anpassa inställningarna för din programvara, inklusive Interface-språket och dess beteende på ditt system. ![MULLVAD VPN](assets/notext/33.webp) I menyn "*VPN settings*" hittar du alternativ som är relaterade till ditt VPN. Jag rekommenderar att du aktiverar alternativen "*Launch app on start-up*" och "*Auto-connect*" så att din VPN-anslutning startar automatiskt när din maskin startar.

![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.

![MULLVAD VPN](assets/notext/35.webp)

Slutligen kan du i menyn "*Split tunneling*" välja specifika program på din dator för vilka internettrafiken inte kommer att ledas genom VPN.

![MULLVAD VPN](assets/notext/36.webp)

För att få en översikt över ditt Mullvad-konto och hantera de olika anslutna enheterna kan du klicka på menyn "*Enheter*" på webbplatsen.

![MULLVAD VPN](assets/notext/37.webp)

Och där har du det, du är nu utrustad för att njuta av Mullvad VPN fullt ut. Om du är intresserad av att upptäcka en annan VPN-leverantör som liknar Mullvad, både när det gäller funktioner och prissättning, rekommenderar jag också att du tittar på vår handledning om IVPN:


https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68