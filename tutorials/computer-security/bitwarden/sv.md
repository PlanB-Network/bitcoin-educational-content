---
name: Bitvarden
description: Hur ställer man in en lösenordshanterare?
---
![cover](assets/cover.webp)


I den digitala tidsåldern måste vi hantera en mängd onlinekonton som täcker olika aspekter av vårt dagliga liv, inklusive bank, finansiella plattformar, e-post, fillagring, hälsa, administration, sociala nätverk, videospel etc.


För att autentisera oss på vart och ett av dessa konton använder vi en identifierare, ofta en e-post Address, tillsammans med ett lösenord. Eftersom det är omöjligt att komma ihåg ett stort antal unika lösenord kan det vara frestande att återanvända samma lösenord eller ändra en gemensam bas något för att lättare komma ihåg det. Dessa metoder äventyrar dock allvarligt säkerheten för dina konton.


Den första principen för lösenord är att inte återanvända dem. Varje onlinekonto bör skyddas av ett unikt lösenord som är helt skilt från de andra. Det här är viktigt eftersom du inte vill att en angripare ska ha tillgång till alla dina konton om han eller hon lyckas komma över ett av dina lösenord. Genom att ha ett unikt lösenord för varje konto isolerar du potentiella attacker och begränsar deras omfattning. Om du t.ex. använder samma lösenord för en videospelplattform och för din e-post, och det lösenordet avslöjas via en nätfiskesida som är relaterad till spelplattformen, kan angriparen enkelt komma åt din e-post och ta kontroll över alla dina andra onlinekonton.


Den andra viktiga principen är lösenordets styrka. Ett lösenord anses vara starkt om det är svårt att brute force, det vill säga att gissa genom försök och misstag. Det innebär att dina lösenord måste vara så slumpmässiga som möjligt, långa och innehålla en mängd olika tecken (små och stora bokstäver, siffror och symboler).


Att tillämpa dessa två principer för lösenordssäkerhet (unikhet och robusthet) kan visa sig vara svårt i vardagen, eftersom det är nästan omöjligt att memorera ett unikt, slumpmässigt och starkt lösenord för alla våra konton. Det är här lösenordshanteraren kommer in i bilden.


En lösenordshanterare genererar och lagrar starka lösenord på ett säkert sätt, vilket gör att du kan komma åt alla dina onlinekonton utan att behöva memorera dem individuellt. Du behöver bara komma ihåg ett lösenord, huvudlösenordet, som ger dig tillgång till alla dina sparade lösenord i hanteringen. Att använda en lösenordshanterare förbättrar din säkerhet online eftersom den förhindrar återanvändning av lösenord och systematiskt genererar slumpmässiga lösenord. Men det förenklar också din dagliga användning av dina konton genom att centralisera åtkomsten till din känsliga information.

I den här handledningen kommer vi att utforska hur man ställer in och använder en lösenordshanterare för att förbättra din online-säkerhet. Jag kommer att presentera dig för Bitwarden, och i en annan handledning kommer vi att titta på en annan lösning som heter KeePass.

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Varning: En lösenordshanterare är bra för att lagra lösenord, men **du ska aldrig lagra din Bitcoin Wallet:s Mnemonic-fras i den!** Kom ihåg att en Mnemonic-fras uteslutande ska sparas i ett fysiskt format, som en bit papper eller metall.


## Introduktion till Bitwarden


Bitwarden är en lösenordshanterare som passar både nybörjare och avancerade användare. Den erbjuder många fördelar. Först och främst är Bitwarden en lösning för flera plattformar, vilket innebär att du kan använda den som en mobilapp, webbapplikation, webbläsartillägg och skrivbordsprogramvara.

![BITWARDEN](assets/notext/01.webp)

Med Bitwarden kan du spara dina lösenord online och synkronisera dem på alla dina enheter, samtidigt som du säkerställer end-to-end-kryptering med ditt huvudlösenord. Detta gör att du till exempel kan komma åt dina lösenord på både din dator och smartphone, med synkronisering mellan de två. Eftersom dina lösenord är krypterade förblir de otillgängliga för alla, inklusive Bitwarden, utan dekrypteringsnyckeln som är ditt huvudlösenord.


Dessutom är Bitwarden öppen källkod, vilket innebär att programvaran kan granskas av oberoende experter. När det gäller prissättning erbjuder Bitwarden tre planer:


- En gratisversion som vi kommer att utforska i den här handledningen. Även om det är gratis ger det en säkerhetsnivå som motsvarar den för de betalda versionerna. Du kan lagra ett obegränsat antal lösenord och synkronisera så många enheter som du vill;
- En premiumversion för 10 USD per år som innehåller ytterligare funktioner som fillagring, säkerhetskopiering av bankkort, möjlighet att ställa in 2FA med en fysisk säkerhetsnyckel och tillgång till TOTP 2FA-autentisering direkt med Bitwarden;
- Och en familjeplan för 40 USD per år som utökar fördelarna med premiumversionen till sex olika användare.

![BITWARDEN](assets/notext/02.webp)

Enligt min mening är dessa priser rimliga. Gratisversionen är ett utmärkt alternativ för nybörjare, och premiumversionen ger mycket bra valuta för pengarna jämfört med andra lösenordshanterare på marknaden, samtidigt som den erbjuder fler funktioner. Dessutom är det faktum att Bitwarden är öppen källkod en stor fördel. Därför är det en intressant kompromiss, särskilt för nybörjare.

En annan funktion i Bitwarden är möjligheten att själv vara värd för din lösenordshanterare om du till exempel äger en NAS hemma. Genom att ställa in denna konfiguration lagras inte dina lösenord på Bitwardens servrar utan på dina egna servrar. Detta ger dig fullständig kontroll över tillgängligheten av dina lösenord. Detta alternativ kräver dock noggrann backup-hantering för att undvika förlust av åtkomst. Därför är Bitwardens självhosting mer lämpad för avancerade användare, och vi kommer att diskutera det i en annan handledning.

## Hur skapar jag ett Bitwarden-konto?


Gå till [Bitwardens webbplats] (https://bitwarden.com/) och klicka på "*Get Started*".

![BITWARDEN](assets/notext/03.webp)

Börja med att ange din e-post Address samt ditt namn eller smeknamn.

![BITWARDEN](assets/notext/04.webp)

Därefter måste du ställa in ditt huvudlösenord. Som vi såg i inledningen är detta lösenord mycket viktigt eftersom det ger dig tillgång till alla dina andra sparade lösenord i hanteringen. Det innebär två huvudsakliga risker: förlust och kompromettering. Om du förlorar ditt lösenord kommer du inte längre att kunna komma åt alla dina uppgifter. Om ditt lösenord blir stulet kommer angriparen att kunna komma åt alla dina konton.


För att minimera risken för förlust rekommenderar jag att du gör en fysisk säkerhetskopia av ditt huvudlösenord på papper och förvarar det på en säker plats. Om möjligt, Seal denna säkerhetskopia i ett säkert kuvert för att regelbundet säkerställa att ingen annan har tillgång till den.


För att ditt huvudlösenord inte ska kunna röjas måste det vara extremt robust. Det ska vara så långt som möjligt, innehålla en mängd olika tecken och väljas slumpmässigt. År 2024 är minimirekommendationerna för ett säkert lösenord 13 tecken inklusive siffror, små och stora bokstäver samt symboler, förutsatt att lösenordet verkligen är slumpmässigt. Jag rekommenderar dock att man väljer ett lösenord med minst 20 tecken, inklusive alla möjliga typer av tecken, för att garantera säkerheten under längre tid.


Ange ditt huvudlösenord i den avsedda rutan och bekräfta det i följande ruta.

![BITWARDEN](assets/notext/05.webp)

Om du vill kan du lägga till en ledtråd för ditt huvudlösenord. Jag avråder dock från att göra det, eftersom ledtråden inte ger någon tillförlitlig metod för återställning om du tappar bort ditt lösenord och till och med kan vara användbar för angripare som försöker gissa eller brute force ditt lösenord. Som en allmän regel bör du undvika att skapa offentliga ledtrådar som kan äventyra säkerheten för ditt huvudlösenord.

![BITWARDEN](assets/notext/06.webp)

Klicka sedan på knappen "*Create an account*".

![BITWARDEN](assets/notext/07.webp)

Du kan nu logga in på ditt nya Bitwarden-konto. Ange din e-postadress Address.

![BITWARDEN](assets/notext/08.webp)

Skriv sedan in ditt huvudlösenord.

![BITWARDEN](assets/notext/09.webp)

Du befinner dig nu på webbsidan Interface för din lösenordshanterare.

![BITWARDEN](assets/notext/10.webp)

## Hur ställer man in Bitwarden?


Till att börja med ska vi bekräfta vår e-post Address. Klicka på "*Send Email*".

![BITWARDEN](assets/notext/11.webp)

Klicka sedan på knappen som du fått via e-post.

![BITWARDEN](assets/notext/12.webp)

Logga slutligen in igen.

![BITWARDEN](assets/notext/13.webp)

Först och främst rekommenderar jag starkt att du ställer in tvåfaktorsautentisering (2FA) för att säkra din lösenordshanterare. Du kan välja mellan att använda en TOTP-applikation eller en fysisk säkerhetsnyckel. Genom att aktivera 2FA kommer du varje gång du loggar in på ditt Bitwarden-konto att bli ombedd att inte bara ange ditt huvudlösenord utan även bevisa din andra autentiseringsfaktor. Detta är ytterligare en Layer av säkerhet, särskilt användbar i händelse av att din pappersbackup av huvudlösenordet äventyras.


Om du är osäker på hur du ställer in och använder dessa 2FA-enheter rekommenderar jag att du följer dessa två andra handledningar:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Detta gör du genom att gå till fliken "*Säkerhet*" i menyn "*Inställningar*".

![BITWARDEN](assets/notext/14.webp)

Klicka sedan på fliken "*Tvåstegsinloggning*".

![BITWARDEN](assets/notext/15.webp)

Här kan du välja den 2FA-metod du föredrar. Till exempel väljer jag 2FA med en TOTP-ansökan genom att klicka på knappen "*Manage*".

![BITWARDEN](assets/notext/16.webp)

Bekräfta ditt huvudlösenord.

![BITWARDEN](assets/notext/17.webp)

Skanna sedan QR-koden med din 2FA-applikation.

![BITWARDEN](assets/notext/18.webp)

Ange den 6-siffriga kod som anges i din 2FA-applikation och klicka sedan på knappen "*Turn on*". ![BITWARDEN](assets/notext/19.webp)

Tvåfaktorsautentisering har framgångsrikt ställts in på ditt konto.

![BITWARDEN](assets/notext/20.webp)

Om du nu försöker logga in på din manager igen måste du först ange ditt huvudlösenord och sedan den dynamiska sexsiffriga kod som genereras av din 2FA-applikation. Se till att du alltid har tillgång till den här dynamiska koden; utan den kan du inte återställa dina lösenord.

![BITWARDEN](assets/notext/21.webp)

I inställningarna har du också möjlighet att anpassa din manager under fliken "*Preferences*". Här kan du ändra hur lång tid det ska gå innan din manager låses automatiskt, samt språk och tema för Interface.

![BITWARDEN](assets/notext/22.webp)

Jag rekommenderar starkt att du justerar längden på de lösenord som genereras av Bitwarden. Som standard är längden inställd på 14 tecken, vilket kan vara otillräckligt för optimal säkerhet. Nu när du har en manager för att komma ihåg alla dina lösenord kan du lika gärna dra nytta av det för att använda mycket starka lösenord.


Gå till menyn "*Generator*" för att göra detta.

![BITWARDEN](assets/notext/23.webp)

Här kan du öka längden på dina lösenord till 40 och kryssa i rutan för att inkludera symboler.

![BITWARDEN](assets/notext/24.webp)

## Hur säkrar du dina konton med Bitwarden?


Nu när din lösenordshanterare är konfigurerad kan du börja lagra inloggningsuppgifterna för dina onlinekonton. För att lägga till ett nytt objekt klickar du direkt på knappen "*Nytt objekt*" eller på knappen "*Nytt*" längst upp till höger på skärmen och sedan på "*objekt*".

![BITWARDEN](assets/notext/25.webp)

I det formulär som öppnas börjar du med att bestämma vilken typ av objekt som ska sparas. För att lagra inloggningsuppgifter väljer du alternativet "*Login*" i rullgardinsmenyn.

![BITWARDEN](assets/notext/26.webp)

I fältet "*Name*" anger du ett beskrivande namn för dina inloggningsuppgifter. Detta gör det lättare att söka efter och organisera dina lösenord, särskilt om du har ett stort antal. Om du till exempel vill spara dina inloggningsuppgifter för PlanB Network-webbplatsen kan du namnge det här objektet på ett sätt som gör att du omedelbart känner igen det under dina framtida sökningar.

![BITWARDEN](assets/notext/27.webp)

Med alternativet "*Folder*" kan du klassificera dina referenser i mappar. För närvarande har vi inte skapat några, men jag ska visa dig hur du gör det senare.

![BITWARDEN](assets/notext/28.webp)

I fältet "*Username*" anger du ditt användarnamn, som vanligtvis är din e-post Address. ![BITWARDEN](tillgångar/notext/29.webp)

Därefter kan du ange ditt lösenord i fältet "*Password*". Jag rekommenderar dock starkt att du låter Bitwarden generate skapa ett långt, slumpmässigt och unikt lösenord åt dig. Detta säkerställer att du har ett starkt lösenord. För att använda denna funktion klickar du på dubbelpilen ovanför fältet som ska fyllas i.

![BITWARDEN](assets/notext/30.webp)

Du kan se att ditt lösenord har genererats.

![BITWARDEN](assets/notext/31.webp)

I fältet "*URI 1*" kan du ange webbplatsens domännamn.

![BITWARDEN](assets/notext/32.webp)

Och slutligen kan du i fältet "*Notes*" lägga till ytterligare information om det behövs.

![BITWARDEN](assets/notext/33.webp)

När du har fyllt i alla dessa fält klickar du på knappen "*Spara*".

![BITWARDEN](assets/notext/34.webp)

Din identifierare visas nu i din Bitwarden-hanterare.

![BITWARDEN](assets/notext/35.webp)

Genom att klicka på den kan du komma åt dess detaljer och ändra dem.

![BITWARDEN](assets/notext/36.webp)

Genom att klicka på de tre små prickarna till höger får du snabb tillgång till att kopiera lösenordet eller identifieraren.

![BITWARDEN](assets/notext/37.webp)

Grattis, du har nu sparat ditt första lösenord i din manager! Om du vill organisera dina identifierare bättre kan du skapa specifika mappar. För att göra detta klickar du på knappen "*New*" längst upp till höger på skärmen och väljer sedan "*Folder*".

![BITWARDEN](assets/notext/38.webp)

Ange ett namn för mappen.

![BITWARDEN](assets/notext/39.webp)

Klicka sedan på "*Spara*".

![BITWARDEN](assets/notext/40.webp)

Din mapp visas nu i din manager.

![BITWARDEN](assets/notext/41.webp)

Du kan tilldela en mapp till en identifierare när du skapar den, som vi gjorde tidigare, eller genom att ändra en befintlig identifierare. Om jag till exempel klickar på min identifierare för PlanB Network kan jag sedan välja att klassificera den i mappen "*Bitcoin*".

![BITWARDEN](assets/notext/42.webp)

På så sätt kan du strukturera din lösenordshanterare så att det blir lättare att hitta dina identifierare. Du kan organisera dem med mappar som personliga, professionella, banker, e-post, sociala nätverk, prenumerationer, shopping, administration, streaming, lagring, resor, hälsa etc.

Om du föredrar att bara använda webbversionen av Bitwarden är det fullt möjligt att hålla sig till den. Jag rekommenderar då att du lägger till din lösenordshanterare i webbläsarens favoriter för enkel åtkomst och för att undvika phishing-risker. Bitwarden erbjuder dock också ett komplett utbud av klienter som gör att du kan använda din manager på olika enheter och förenkla den dagliga användningen. De erbjuder särskilt en mobilapp, ett webbläsartillägg och skrivbordsprogramvara. Låt oss se hur du konfigurerar dem tillsammans.


![BITWARDEN](assets/notext/43.webp)


## Hur använder man webbläsartillägget Bitwarden?


Först kan du ställa in webbläsartillägget om du vill. Det här tillägget fungerar som en reducerad version av din manager och ger dig möjlighet att automatiskt spara nya lösenord, generate-förslag på säkra lösenord och automatiskt fylla i dina uppgifter på inloggningssidor på webbplatser.


Den dagliga användningen av detta tillägg är extremt bekvämt, men det kan också öppna nya attackvektorer. Vissa cybersäkerhetsexperter avråder därför från att använda webbläsartillägg för lösenordshanterare. Men om du väljer att använda Bitwarden-tillägget, här är hur du ska gå vidare:


Börja med att gå till [den officiella nedladdningssidan för Bitwarden] (https://bitwarden.com/download/#downloads-web-browser).


![BITWARDEN](assets/notext/44.webp)


Välj din webbläsare från listan som tillhandahålls. I det här exemplet använder jag Firefox, så jag omdirigeras till det officiella Bitwarden-tillägget i Firefox Add-ons Store. Proceduren är ganska lik för andra webbläsare.


![BITWARDEN](assets/notext/45.webp)


Klicka på knappen "*Add to Firefox*".


![BITWARDEN](assets/notext/46.webp)


Du kan sedan fästa Bitwarden i din förlängningsbar för enkel åtkomst. Klicka på tillägget för att logga in.


![BITWARDEN](assets/notext/47.webp)


Ange din e-postadress Address.


![BITWARDEN](assets/notext/48.webp)


Sedan ditt huvudlösenord.


![BITWARDEN](assets/notext/49.webp)


Och slutligen anger du den 6-siffriga koden från din autentiseringsapp.


![BITWARDEN](assets/notext/50.webp)


Du är nu ansluten till din Bitwarden-hanterare via webbläsartillägget.


![BITWARDEN](assets/notext/51.webp)


Om jag till exempel går tillbaka till PlanB Networks webbplats och försöker logga in på mitt konto, kan du se att Bitwarden-tillägget som är integrerat i webbläsaren känner igen inloggningsfälten och automatiskt erbjuder mig att välja den identifierare som jag tidigare sparat.


![BITWARDEN](assets/notext/52.webp)

Om jag väljer den här identifieraren fyller Bitwarden i inloggningsfälten åt mig. Den här funktionen i tillägget gör det möjligt att snabbt ansluta till webbplatser utan att behöva kopiera och klistra in inloggningsuppgifter från Bitwardens webbapplikation eller programvara.

![BITWARDEN](assets/notext/53.webp)

Tillägget är också utformat för att upptäcka skapandet av nya konton. Till exempel, när du skapar ett nytt konto på PlanB Network, föreslår Bitwarden automatiskt att du sparar den nya identifieraren.

![BITWARDEN](assets/notext/54.webp)

Genom att klicka på det här förslaget som visas öppnas tillägget. Det låter mig ange detaljerna för den nya identifieraren och generate ett starkt, unikt lösenord.

![BITWARDEN](assets/notext/55.webp)

När du har fyllt i informationen och klickat på "*Save*" sparar tillägget inloggningsuppgifterna.

![BITWARDEN](assets/notext/56.webp)

Sedan fyller tillägget automatiskt i våra inloggningsuppgifter i lämpliga fält på webbplatsen.

![BITWARDEN](assets/notext/57.webp)

## Hur använder man Bitwardens programvara?


För att installera Bitwardens skrivbordsprogramvara, börja med att gå till [nedladdningssidan] (https://bitwarden.com/download/#downloads-desktop). Välj och ladda ner den version som motsvarar ditt operativsystem.

![BITWARDEN](assets/notext/58.webp)

När nedladdningen är klar fortsätter du med installationen av programvaran på din dator. Vid den första starten av Bitwarden-programvaran måste du ange dina inloggningsuppgifter för att låsa upp din lösenordshanterare.

![BITWARDEN](assets/notext/59.webp)

Därefter kommer du till din chefs hemsida. Interface är nästan densamma som i webbapplikationen.

![BITWARDEN](assets/notext/60.webp)

## Hur använder man Bitwarden-applikationen?


För att komma åt dina lösenord från din telefon kan du installera mobilapplikationen Bitwarden. Börja med att gå till [nedladdningssidan] (https://bitwarden.com/download/#downloads-mobile) och använd din smartphone för att skanna QR-koden som motsvarar ditt operativsystem.

![BITWARDEN](assets/notext/61.webp)

Ladda ner och installera Bitwardens officiella mobilapplikation. När applikationen öppnas första gången anger du dina inloggningsuppgifter för att låsa upp åtkomsten till din lösenordshanterare.

![BITWARDEN](assets/notext/62.webp)

När du är ansluten kan du se och hantera alla dina lösenord direkt från programmet.

![BITWARDEN](assets/notext/63.webp)

För att öka säkerheten i din applikation rekommenderar jag att du går in i inställningarna och aktiverar PIN-skydd. Detta ger en extra Layer säkerhet om du skulle förlora eller stjäla din telefon.

![BITWARDEN](assets/notext/64.webp)

## Hur säkerhetskopierar jag Bitwarden?

För att säkerställa att du aldrig förlorar tillgång till dina lösenord, även i händelse av att du förlorar ditt huvudlösenord eller en katastrof som påverkar Bitwardens servrar, rekommenderar jag dig att regelbundet utföra en krypterad säkerhetskopia av din chef på ett externt medium.


Tanken är att kryptera alla dina Bitwarden-uppgifter med ett lösenord som skiljer sig från ditt huvudlösenord och att spara den krypterade säkerhetskopian på ett USB-minne eller en Hard-enhet som du till exempel har hemma hos dig. Du kan sedan förvara en fysisk kopia av dekrypteringslösenordet på en annan plats än där säkerhetskopieringsmediet förvaras. Du kan t.ex. förvara USB-minnet hemma och överlåta den fysiska kopian av krypteringslösenordet till en betrodd vän.


Den här metoden säkerställer att även om ditt backupmedium blir stulet kommer dina data att förbli otillgängliga utan dekrypteringslösenordet. På samma sätt kommer din vän inte att kunna komma åt dina data utan att ha det fysiska mediet.


I händelse av problem kan du dock använda lösenordet och det externa mediet för att återfå tillgång till dina inloggningsuppgifter, oberoende av Bitwarden. Även om Bitwardens servrar skulle förstöras har du alltså fortfarande möjlighet att återfå dina lösenord.


Därför råder jag dig att göra dessa säkerhetskopior regelbundet så att de alltid innehåller dina senaste inloggningsuppgifter. För att slippa besvära din vän, som har en kopia av krypteringslösenordet, med varje ny säkerhetskopia kan du spara detta lösenord i din lösenordshanterare. Detta är inte avsett som en säkerhetskopia, eftersom din vän redan har en fysisk kopia, utan snarare för att förenkla dina framtida exportförfaranden.


För att fortsätta med exporten är det ganska enkelt: gå till avsnittet "*Tools*" i din Bitwarden-hanterare och välj sedan "*Export vault*".

![BITWARDEN](assets/notext/65.webp)

För format väljer du "*.json (krypterad)*".

![BITWARDEN](assets/notext/66.webp)

Välj sedan alternativet "*Password protected*".

![BITWARDEN](assets/notext/67.webp)

Här är det viktigt att välja ett starkt, unikt och slumpmässigt genererat lösenord för att kryptera säkerhetskopian. Detta säkerställer att det, även vid stöld av din krypterade säkerhetskopia, kommer att vara omöjligt för en angripare att dekryptera den med brute force.

![BITWARDEN](assets/notext/68.webp)

Klicka på "*Confirm format*" och ange ditt huvudlösenord för att fortsätta med exporten.

![BITWARDEN](assets/notext/69.webp)

När exporten är klar hittar du din krypterade säkerhetskopia bland dina nedladdningar. Överför den till en säker extern lagringsenhet, t.ex. ett USB-minne eller en Hard-enhet. Upprepa denna åtgärd med jämna mellanrum beroende på din användning. Du kan t.ex. förnya säkerhetskopian varje vecka eller varje månad, beroende på dina behov.