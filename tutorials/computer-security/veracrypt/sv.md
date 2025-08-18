---
name: VeraCrypt
description: Hur krypterar jag en lagringsenhet på ett enkelt sätt?
---
![cover](assets/cover.webp)


Nuförtiden är det viktigt att implementera en strategi för att säkerställa tillgänglighet, säkerhet och säkerhetskopiering av dina filer, till exempel dina personliga dokument, foton eller viktiga projekt. Att förlora dessa data kan vara katastrofalt.


För att förhindra dessa problem råder jag dig att göra flera säkerhetskopior av dina filer på olika medier. En vanlig strategi inom databehandling är säkerhetskopieringsstrategin "3-2-1", som säkerställer att dina filer skyddas:


- 3** kopior av dina filer;
- Sparas på minst **2** olika typer av media;
- Med minst **1** kopia som förvaras utanför webbplatsen.


Med andra ord är det lämpligt att lagra dina filer på tre olika platser med hjälp av olika typer av media, t.ex. din dator, en extern Hard-enhet, ett USB-minne eller en lagringstjänst online. Och slutligen, att ha en extern kopia innebär att du bör ha en säkerhetskopia lagrad utanför ditt hem eller företag. Den här sista punkten hjälper dig att undvika total förlust av dina filer vid lokala katastrofer som bränder eller översvämningar. En extern kopia, långt från ditt hem eller företag, säkerställer att dina data överlever oberoende av lokala risker.


För att enkelt implementera denna 3-2-1 backup-strategi kan du välja en online-lagringslösning genom att automatiskt eller periodiskt synkronisera filerna från din dator med dem i ditt moln. Bland dessa online-backup-lösningar finns det uppenbarligen de från stora digitala företag som du känner till: Google Drive, Microsoft OneDrive eller Apple iCloud. Dessa är dock inte de bästa lösningarna för att skydda din integritet. I en tidigare handledning introducerade jag dig till ett alternativ som krypterar dina dokument för bättre integritet: Proton Drive.


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Genom att använda den här strategin med lokal säkerhetskopiering och molnbaserad säkerhetskopiering har du redan två olika typer av media för dina data, varav en är extern. För att slutföra 3-2-1-strategin behöver du helt enkelt lägga till ytterligare en kopia. Det jag råder dig att göra är helt enkelt att regelbundet exportera dina data som finns lokalt och i ditt moln till ett fysiskt medium, som ett USB-minne eller en extern Hard-enhet. På så sätt har du, även om servrarna i din online-lagringslösning förstörs och din dator går sönder samtidigt, fortfarande denna tredje kopia på ett externt medium för att inte förlora dina data.

![VeraCrypt](assets/notext/01.webp)

Men det är också viktigt att tänka på säkerheten för din datalagring för att säkerställa att ingen annan än du eller dina nära och kära kan komma åt den. Både lokala data och online-data är normalt säkra. På din dator har du förmodligen satt upp ett lösenord, och Hard-enheterna i moderna datorer är ofta krypterade som standard. När det gäller din onlinelagring (molnet) visade jag dig i den tidigare handledningen hur du skyddar ditt konto med ett starkt lösenord och tvåfaktorsautentisering. Men när det gäller din tredje kopia som lagras på ett fysiskt medium är den enda säkerheten dess fysiska innehav. Om en inbrottstjuv lyckas stjäla ditt USB-minne eller din externa Hard-enhet kan han eller hon enkelt komma åt alla dina data.

![VeraCrypt](assets/notext/02.webp)

För att förhindra denna risk är det lämpligt att kryptera ditt fysiska medium. Varje försök att komma åt data kräver således att ett lösenord anges för att dekryptera innehållet. Utan detta lösenord är det omöjligt att komma åt uppgifterna, vilket skyddar dina personliga filer även om ditt USB-minne eller din externa Hard-enhet skulle bli stulen.

![VeraCrypt](assets/notext/03.webp)

I den här handledningen visar jag dig hur du enkelt krypterar ett externt lagringsmedium med VeraCrypt, ett verktyg med öppen källkod.


## Introduktion till VeraCrypt


VeraCrypt är en programvara med öppen källkod som finns tillgänglig på Windows, macOS och Linux, vilket gör att du kan kryptera dina data på olika sätt och på olika medier.

![VeraCrypt](assets/notext/04.webp)

Den här programvaran gör det möjligt att skapa och underhålla krypterade volymer i farten, vilket innebär att dina data automatiskt krypteras innan de sparas och dekrypteras innan de läses. Denna metod säkerställer att dina filer förblir skyddade även om ditt lagringsmedium skulle stjälas. VeraCrypt krypterar inte bara filer utan även filnamn, metadata, mappar och till och med det lediga utrymmet på ditt lagringsmedium.


VeraCrypt kan användas för att kryptera filer lokalt eller hela partitioner, inklusive systemdisken. Det kan också användas för att helt kryptera ett externt medium som ett USB-minne eller en disk som vi kommer att se i den här handledningen.


En stor fördel med VeraCrypt jämfört med proprietära lösningar är att det är helt öppen källkod, vilket innebär att dess kod kan verifieras av vem som helst.


## Hur installerar jag VeraCrypt?


Gå till [den officiella VeraCrypt-webbplatsen](https://www.veracrypt.fr/en/Downloads.html) på fliken "*Downloads*".

![VeraCrypt](assets/notext/05.webp)

Ladda ner den version som passar för ditt operativsystem. Om du använder Windows väljer du "*EXE Installer*".

![VeraCrypt](assets/notext/06.webp)

Välj språk för din Interface.

![VeraCrypt](assets/notext/07.webp)

Acceptera villkoren för licensen.

![VeraCrypt](assets/notext/08.webp)

Välj "*Install*".

![VeraCrypt](assets/notext/09.webp)

Slutligen väljer du den mapp där programvaran ska installeras och klickar sedan på knappen "*Install*".

![VeraCrypt](assets/notext/10.webp)

Vänta tills installationen är klar.

![VeraCrypt](assets/notext/11.webp)

Installationen är klar.

![VeraCrypt](assets/notext/12.webp)

Om du vill kan du göra en donation i bitcoins för att stödja utvecklingen av detta verktyg med öppen källkod.

![VeraCrypt](assets/notext/13.webp)

## Hur krypterar jag en lagringsenhet med VeraCrypt?


Vid första uppskjutningen kommer du till denna Interface:

![VeraCrypt](assets/notext/14.webp)

För att kryptera den lagringsenhet du väljer börjar du med att ansluta den till din maskin. Som du kommer att se senare kommer processen att skapa en ny krypterad volym på ett USB-minne eller en Hard-enhet att ta mycket längre tid om enheten redan innehåller data som du inte vill radera. Därför rekommenderar jag att du använder ett tomt USB-minne eller tömmer enheten i förväg för att skapa den krypterade volymen, för att spara tid.


Klicka på fliken "*Volumes*" i VeraCrypt.

![VeraCrypt](assets/notext/15.webp)

Sedan på menyn "* Skapa ny volym ... *".

![VeraCrypt](assets/notext/16.webp)

I det nya fönstret som öppnas väljer du alternativet "*Encrypt a non-system partition/drive*" och klickar på "*Next*".

![VeraCrypt](assets/notext/17.webp)

Du kommer då att behöva välja mellan "*Standard VeraCrypt-volym*" och "*Dold VeraCrypt-volym*". Det första alternativet skapar en standardkrypterad volym på din enhet. Alternativet "* Dold VeraCrypt-volym *" gör det möjligt att skapa en dold volym inom en standard VeraCrypt-volym. Med den här metoden kan du förneka att den dolda volymen existerar om du utsätts för tvång. Om någon till exempel fysiskt tvingar dig att dekryptera din enhet kan du dekryptera endast standarddelen för att tillfredsställa aggressorn men inte avslöja den dolda delen. I mitt exempel kommer jag att hålla mig till en standardvolym.

![VeraCrypt](assets/notext/18.webp)

På följande sida klickar du på knappen "*Select Device...*".

![VeraCrypt](assets/notext/19.webp)

Ett nytt fönster öppnas där du kan välja partitionen på din lagringsenhet från listan över diskar som är tillgängliga på din maskin. Normalt kommer den partition som du vill kryptera att listas under en rad med titeln "*Removable Disk N*". När du har valt rätt partition klickar du på knappen "*OK*".

![VeraCrypt](assets/notext/20.webp)

Den valda supporten visas i rutan. Du kan nu klicka på knappen "*Nästa*". ![VeraCrypt](tillgångar/notext/21.webp)

Därefter måste du välja mellan alternativen "* Skapa krypterad volym och formatera den*" eller "* Kryptera partition på plats*". Som nämnts tidigare kommer det första alternativet att permanent radera all data på ditt USB-minne eller Hard-enhet. Välj detta alternativ endast om enheten är tom, annars förlorar du alla data som finns på den. Om du vill behålla befintliga data kan du tillfälligt överföra dem till en annan plats, välja "*Create encrypted volume and format it*" för en snabbare process som raderar allt, eller välja "*Encrypt partition in place*". Det här sista alternativet gör det möjligt att kryptera volymen utan att radera de data som redan finns, men processen blir mycket längre. I det här exemplet, eftersom mitt USB-minne är tomt, väljer jag "*Create encrypted volume and format it*", det alternativ som raderar allt.

![VeraCrypt](assets/notext/22.webp)

Därefter får du möjlighet att välja krypteringsalgoritm och Hash-funktionen. Om du inte har särskilda behov rekommenderar jag att du behåller standardalternativen. Klicka på "*Nästa*" för att fortsätta.

![VeraCrypt](assets/notext/23.webp)

Kontrollera att den angivna storleken för din volym är korrekt, så att du krypterar hela det tillgängliga utrymmet på USB-minnet och inte bara en del. När du har verifierat detta klickar du på "*Nästa*".

![VeraCrypt](assets/notext/24.webp)

I det här skedet måste du ange ett lösenord för att kryptera och dekryptera din enhet. Det är viktigt att välja ett starkt lösenord för att förhindra att en angripare kan dekryptera ditt innehåll med brute force-attacker. Lösenordet ska vara slumpmässigt, så långt som möjligt och innehålla flera olika typer av tecken. Jag råder dig att välja ett slumpmässigt lösenord med minst 20 tecken, inklusive gemener, versaler, siffror och symboler.


Jag råder dig också att spara ditt lösenord i en lösenordshanterare. Det gör det lättare att komma åt och eliminerar risken för att glömma bort det. I vårt specifika fall är en lösenordshanterare att föredra framför ett pappersmedium. Vid ett inbrott kan visserligen din lagringsenhet bli stulen, men lösenordet i hanteringen kan inte hittas av angriparen, vilket förhindrar åtkomst till uppgifterna. Om din lösenordshanterare däremot blir stulen, krävs det fortfarande fysisk tillgång till enheten för att kunna utnyttja lösenordet och få tillgång till uppgifterna.


För mer information om hantering av lösenord rekommenderar jag att du läser den här andra fullständiga handledningen:


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Ange ditt lösenord i de 2 angivna fälten och klicka sedan på "*Nästa*". ![VeraCrypt](tillgångar/notext/25.webp)

VeraCrypt kommer sedan att fråga dig om du planerar att lagra filer som är större än 4 GiB i den krypterade volymen. Denna fråga gör det möjligt för programmet att välja det lämpligaste filsystemet. I allmänhet används FAT-systemet eftersom det är kompatibelt med de flesta operativsystem, men det innebär en maximal filstorleksgräns på 4 GiB. Om du behöver hantera större filer kan du välja exFAT-systemet.

![VeraCrypt](assets/notext/26.webp)

Därefter kommer du till en sida där du kan ange generate, en slumpmässig nyckel. Den här nyckeln är viktig eftersom den kommer att användas för att kryptera och dekryptera dina data. Den kommer att lagras i en specifik del av dina media, som är säkrad med det lösenord du tidigare fastställt. För att generate en stark krypteringsnyckel behöver VeraCrypt entropi. Det är därför programvaran ber dig att flytta musen slumpmässigt över fönstret; dessa rörelser används sedan för att generate nyckeln. Fortsätt att flytta musen tills entropimätaren är helt fylld. Klicka sedan på "*Format*" för att börja skapa den krypterade volymen.

![VeraCrypt](assets/notext/27.webp)

Vänta tills formateringen är klar. Detta kan ta lång tid för stora volymer.

![VeraCrypt](assets/notext/28.webp)

Du kommer sedan att få en bekräftelse.

![VeraCrypt](assets/notext/29.webp)

## Hur använder jag en krypterad enhet med VeraCrypt?


För tillfället är din media krypterad och du kan därför inte öppna den. För att dekryptera det, gå till VeraCrypt.

![VeraCrypt](assets/notext/30.webp)

Välj en enhetsbeteckning från listan. Jag valde till exempel "*L:*".

![VeraCrypt](assets/notext/31.webp)

Klicka på knappen "*Select Device...*".

![VeraCrypt](assets/notext/32.webp)

Välj den krypterade volymen på ditt media från listan över alla diskar på din maskin och klicka sedan på knappen "*OK*".

![VeraCrypt](assets/notext/33.webp)

Du kan se att din volym är väl utvald.

![VeraCrypt](assets/notext/34.webp)

Klicka på knappen "*Mount*".

![VeraCrypt](assets/notext/35.webp)

Ange det lösenord som valdes när volymen skapades och klicka sedan på "*OK*".

![VeraCrypt](assets/notext/36.webp)

Du kan se att din volym nu är dekrypterad och tillgänglig på enhetsbeteckningen "*L:*".

![VeraCrypt](assets/notext/37.webp)

För att komma åt den, öppna din filutforskare och gå till enheten "*L:*" (eller en annan bokstav beroende på vilken du valde i de föregående stegen). ![VeraCrypt](tillgångar/notext/38.webp)

När du har lagt till dina personliga filer på mediet klickar du helt enkelt på knappen "*Dismount*" för att kryptera volymen igen.

![VeraCrypt](assets/notext/39.webp)

Din volym visas inte längre under bokstaven "*L:*". Den är därmed krypterad igen.

![VeraCrypt](assets/notext/40.webp)

Du kan nu ta bort ditt lagringsmedium.


Grattis, du har nu ett krypterat medium för att lagra dina personuppgifter på ett säkert sätt och har därmed en komplett 3-2-1-strategi utöver kopian på din dator och din lagringslösning online.


Om du vill stödja utvecklingen av VeraCrypt kan du också göra en donation i bitcoins [på denna sida] (https://www.veracrypt.fr/en/Donation.html).