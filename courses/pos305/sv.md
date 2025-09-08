---
name: Bitcoin och BTC Pay Server
goal: Installera BTC Pay Server för ditt företag
objectives: 

  - Förstå vad btcpayserver är.
  - Självhantera och konfigurera BTC Pay Server.
  - Använd btcpayserver i din dagliga verksamhet.

---

# Bitcoin och BTCPay-server


Detta är en introduktionskurs om BTCPay Server Operator, skriven av Alekos och Bas, som anpassades för Plan ₿ Course Format av melontwist och asi0.


EN OAVSLUTAD HISTORIA


"Det här är lögn, mitt förtroende för dig är förbrukat, jag ska göra dig obsolet".


Producerad av BTCPay Server Foundation


+++

# Inledning


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Kursöversikt


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Välkommen till kursen POS 305 på BTCPay Server!


Målet med den här utbildningen är att lära dig hur du installerar, konfigurerar och använder BTCPay Server inom ditt företag eller din organisation. BTCPay Server är en öppen källkodslösning som gör att du kan behandla Bitcoin-betalningar självständigt, säkert och kostnadseffektivt. Den här kursen riktar sig främst till avancerade användare som vill behärska självhosting av BTCPay Server för fullständig integration i sin dagliga verksamhet.


**Avsnitt 1: Introduktion till BTCPay Server**

Vi börjar med en allmän presentation av BTCPay Server, inklusive inloggningsskärmen, hantering av användarkonton och skapandet av en ny butik. Denna introduktion kommer att hjälpa dig att förstå BTCPay Server Interface och förstå de grundläggande funktioner som behövs för att börja använda detta verktyg.


**Avsnitt 2: Introduktion till att säkra Bitcoin-nycklar**

Säkerheten för dina Bitcoin-medel är mycket viktig. I det här avsnittet kommer vi att utforska genereringen av kryptografiska nycklar, användningen av hårdvaruplånböcker för att säkra dessa nycklar och hur man interagerar med dina nycklar via BTCPay Server. Du kommer också att lära dig hur du konfigurerar en BTCPay Server Lightning Wallet för att optimera dina transaktioner.


**Avsnitt 3: BTCPay Server Interface**

Denna del kommer att guida dig genom BTCPay Server-användaren Interface. Du kommer att lära dig hur du navigerar i instrumentpanelen, konfigurerar butiks- och serverinställningar, hanterar betalningar och drar nytta av integrerade plugins. Målet är att ge dig de verktyg som krävs för att anpassa din installation efter dina specifika behov.


**Avsnitt 4: Konfigurera BTCPay Server**

Slutligen kommer vi att fokusera på den praktiska installationen av BTCPay Server i olika miljöer. Oavsett om du använder LunaNode, Voltage eller en Umbrel-nod kommer du att lära dig de viktigaste stegen för att distribuera och konfigurera din BTCPay Server, med hänsyn till specifikationerna för varje miljö.


Är du redo att bemästra BTCPay Server och få ditt företag att växa? Låt oss gå!


## Kritikerna hyllar Author's Bitcoin och BTCPay Server


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Låt oss börja med att förstå vad BTCPay Server är och dess ursprung. Vi värdesätter transparens och vissa standarder för att skapa förtroende i Bitcoin-utrymmet.

Ett projekt i rymden bröt mot dessa värden. BTCPay Servers huvudutvecklare, Nicolas Dorier, tog detta personligt och lovade att göra dem obsoleta. Här är vi, många år senare, och arbetar mot denna framtid, helt öppen källkod, varje dag.


> Det här är lögn, mitt förtroende för dig är förbrukat, jag ska göra dig obsolet.
> Nicolas Dorier

Efter Nicolas ord var det dags att börja bygga. En betydande mängd arbete gick in i det vi nu kallar BTCPay Server. Fler människor ville bidra till denna ansträngning. De mest igenkännliga är r0ckstardev, MrKukks, Pavlenex och den första handlaren som använde programvaran, astupidmoose.


Vad innebär öppen källkod och vad ingår i ett sådant projekt?


FOSS står för Free & Open-Source Software. Det förstnämnda avser villkor som gör det möjligt för vem som helst att kopiera, ändra och till och med distribuera versioner (även för vinst) av programvaran. Det senare innebär att källkoden delas öppet och att allmänheten uppmuntras att bidra och förbättra den.

Detta lockar erfarna användare som är entusiastiska över att bidra till den programvara som de redan använder och får värde av, vilket i slutändan visar sig vara mer framgångsrikt än proprietär programvara. Det är förenligt med Bitcoin:s etos att "information längtar efter att vara fri" Det sammanför passionerade människor som bildar en gemenskap och är helt enkelt roligare. Precis som Bitcoin är FOSS oundvikligt.


### Innan vi börjar


Denna kurs består av flera delar. Många kommer att tas om hand av din klasslärare, Demomiljöer som du får tillgång till, en hostad server för dig själv och eventuellt ett domännamn. Om du genomför den här kursen på egen hand bör du vara medveten om att de miljöer som är märkta som DEMO inte kommer att vara tillgängliga för dig.

OBS! Om du följer den här kursen i ett klassrum kan servernamnen skilja sig åt beroende på hur klassrummet ser ut. Variablerna i Servernamn kan därför vara annorlunda.


### Kursens struktur


Varje kapitel har mål och kunskapsbedömningar. I den här kursen går vi igenom vart och ett av dessa och ger en sammanfattning av de viktigaste funktionerna i slutet av varje lektionsblock (dvs. kapitel). Illustrationer används för att ge visuell feedback och förstärka nyckelbegrepp i en visuell aspekt. Målen anges i början av varje lektionsblock. Dessa mål går längre än en checklista. De ger dig en guide till en ny uppsättning färdigheter. Kunskapsbedömningarna blir successivt mer utmanande, allteftersom installationen av din BTCPay-server är klar.


### Vad får studenterna med sig från kursen?


Med BTCPay Server-kursen kan en student förstå de grundläggande principerna, tekniska och icke-tekniska, för Bitcoin. Den omfattande utbildningen i att använda Bitcoin genom BTCPay Server gör det möjligt för studenterna att driva sin egen Bitcoin-infrastruktur.


### Viktiga webbadresser eller kontaktmöjligheter


BTCPay Server Foundation, som gjorde det möjligt för Alekos och Bas att skriva den här kursen, ligger i Tokyo, Japan. BTCPay Server-stiftelsen kan nås via den angivna webbplatsen.



- https://foundation.btcpayserver.org
- Gå med i de officiella chattkanalerna: https://chat.btcpayserver.org


## Introduktion till Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Förståelse för Bitcoin via klassrumsövning


Det här är en klassrumsövning, så om du själv går kursen kan du inte utföra den, men du kan ändå gå igenom den här övningen. För att slutföra denna uppgift krävs minst 9 till 11 personer.


Övningen startar efter att du har tittat på BBC:s introduktion "How Bitcoin and the Blockchain works".


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Denna övning kräver minst nio deltagare. Den här övningen syftar till att ge en fysisk förståelse för hur Bitcoin fungerar. Genom att spela varje roll i nätverket kommer du att få ett interaktivt och lekfullt sätt att lära dig. Denna övning involverar inte Lightning Network.


### Exempel: Kräver 9 / 11 personer


Rollerna är:



- 1 Kund
- 1 köpman
- 7 till 9 Bitcoin noder


**Installationen går till på följande sätt:**


Kunderna köper en produkt från butiken med Bitcoin.


**Scenario 1 - Traditionellt banksystem**



- Ställ upp:
  - Se diagram/förklaringar i bifogade Figjam - [Aktivitetsschema] (https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Be tre frivilliga studenter att spela rollerna som kund (Alice), handlare (Bob) och bank.
- Spela upp händelseförloppet:
  - Kund - surfar i butiken på nätet och hittar en vara för 25 USD som han eller hon vill ha och meddelar handlaren att han eller hon vill köpa den
  - Säljaren - begär betalning.
  - Kund - skickar kortinformation till handlaren
  - Säljföretaget - vidarebefordrar information till banken (identifierar både sin egen och identiteten/informationen) och begär betalning av
  - Banken samlar in information om kunden och säljföretaget (Alice och Bob) och kontrollerar att kundens saldo är tillräckligt.
  - Drar av 25 USD från Alice:s konto, lägger till 24 USD på Bob:s konto, tar 1 USD för tjänsten
  - Säljföretaget får tummen upp av banken och skickar varan till kunden.
- Kommentarer:
  - Bob och Alice måste ha en relation med en bank.
  - Bank samlar in identifierande information om både Bob och Alice.
  - Bank tar ett skärsår.
  - Banken måste vara betrodd att alltid ha hand om varje deltagares pengar.


**Scenario 2 - Bitcoin-system**



- Ställ upp:
  - Se diagram/förklaringar i bifogade Figjam - [Aktivitetsschema] (https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Ersätt banken med nio studenter som ska spela rollen som en dator (Bitcoin Nodes/Miners) i ett nätverk som ska ersätta banken.
- Var och en av de 9 datorerna har en fullständig historik över alla tidigare transaktioner som någonsin gjorts (vilket innebär korrekta saldon utan förfalskningar), samt en uppsättning regler:
  - Verifiera att transaktionen är korrekt signerad (thekeyfitsthelock)
  - Sänder och tar emot giltiga transaktioner till motparter i nätverket, kastar ut ogiltiga (inklusive alla som försöker spendera samma pengar två gånger)
- Uppdatera/lägga till poster med jämna mellanrum med nya transaktioner som tas emot från en "slumpmässig" dator, förutsatt att allt innehåll är giltigt (obs: vi ignorerar för tillfället Proof of Work-komponenten i allt detta, för enkelhetens skull), annars avvisar vi dessa och fortsätter som tidigare tills nästa "slumpmässiga" dator skickar en uppdatering
  - Rätt belopp belönades om innehållet var giltigt.
- Spela upp händelseförloppet:
  - Kund - surfar i butiken online och hittar en vara för 25 USD som de vill ha, och informerar handlaren om att de vill köpa
  - Säljaren - begär betalning genom att skicka en Invoice/Address från sin Wallet till kunden.
  - Kund - konstruerar en transaktion (skickar BTC till ett värde av 25 USD till en Address som tillhandahålls av handlaren) och sänder den till Bitcoin-nätverket.
- Datorer - tar emot transaktionen och verifierar den:
  - Det finns minst $ 25 av BTC i Address som skickas från
  - Transaktionen är korrekt signerad ("upplåst" av kunden)
  - Om så inte är fallet kommer transaktionen inte att spridas genom nätverket, och om så är fallet sprids den och hålls i väntan.
  - Handlare kan kontrollera att transaktionen är pågående och väntar.
- En dator väljs "slumpmässigt" ut för att föreslå att den föreslagna transaktionen slutförs genom att sända "ett block" som innehåller den; om den checkar ut får de en BTC-belöning.
  - VALFRI/AVANCERAD - i stället för att slumpmässigt välja en dator, simulera Mining genom att låta datorerna slå tärningar tills något förutbestämt resultat inträffar (t.ex. den som först slår dubbelsexor väljs)
  - Den kan också spela upp vad som skulle hända om två datorer vinner ungefär samtidigt, vilket resulterar i en kedjesplit.
  - Datorer kontrollerar giltigheten, uppdaterar/lägger till poster i sina huvudböcker om reglerna är uppfyllda och sänder transaktionsblocket till kollegor.
  - Den slumpmässigt utvalda datorn får en belöning för att ha föreslagit ett giltigt block.
  - Transaktionen med Merchant Checks slutfördes, vilket innebär att pengarna togs emot och varan skickades till kunden.
- Kommentarer:
  - Observera att det inte fanns något behov av en befintlig bankrelation.
  - Ingen tredje part behövs för att underlätta; ersätts av kod/incitament.
  - Ingen datainsamling av någon utanför den direkta Exchange, och endast den nödvändiga mängden får utbytas mellan deltagarna (t.ex. frakt Address).
  - Det krävs inget förtroende mellan personerna (förutom den handlare som skickar varan), vilket på många sätt liknar ett kontantköp.
  - Pengarna ägs direkt av individerna.
  - Bitcoin Ledger avbildas i dollar för enkelhetens skull, men i verkligheten är det BTC.
  - Vi simulerar att en enda transaktion sänds, men i verkligheten väntar flera transaktioner i nätverket och blocken innehåller tusentals transaktioner samtidigt. Noderna kontrollerar också att inga transaktioner med dubbelt spenderande pågår (jag skulle kassera alla utom en i det här fallet).
- Otrohetsscenarier:
  - Vad händer om kunden inte hade 25 BTC dollar?
    - De skulle inte kunna skapa transaktionen eftersom "upplåsning" och "Ownership" är samma sak, och datorer kontrollerar att transaktionen är korrekt signerad; annars avvisar de den
  - Vad händer om den slumpmässigt utvalda datorn försöker "ändra Ledger"?
    - Blockeringen skulle avvisas, eftersom alla andra datorer har en fullständig historik och skulle märka förändringen, som bryter mot en av deras regler.
    - Random Computer skulle inte få någon belöning och inga transaktioner från deras block skulle slutföras.


## Bedömning av kunskap


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Diskussion i klassrummet


Diskutera några förenklingar som gjordes i klassrumsövningen under det andra scenariot och beskriv vad det faktiska Bitcoin-systemet gör mer i detalj.


### KA Genomgång av ordförråd


Definiera följande nyckelbegrepp som introducerades i föregående avsnitt:



- Nod
- Mempool
- Svårighetsgrad Mål
- Block


**Diskutera betydelsen av några ytterligare termer i grupp:**


Blockchain, Transaktion, Double-Spend, Byzantine Generals' Problem, Mining, Proof of Work (PoW), Hash Funktion, Block reward, Blockchain, Längsta kedjan, 51%-attack, Utgång, Utgångslås, Förändring, Satoshis, Offentlig/privat nyckel, Address, Kryptografi med offentlig nyckel, Digital signatur, Wallet


# Vi presenterar BTCPay Server


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Förstå inloggningsskärmen för BTCPay Server


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Arbeta med BTCPay Server


Syftet med detta kursblock är att få en allmän förståelse för programvaran BTCPay Server. I en delad miljö rekommenderas det att du följer instruktörens demonstration och hänvisar till BTCPay Server Coursebook för att följa med läraren. Du kommer att lära dig hur du skapar en Wallet genom flera metoder. Exemplen inkluderar Hot Wallet-installationer och hårdvaruplånböcker anslutna via BTCPay Server Vault. Dessa mål inträffar i Demo-miljön, som visas och ges tillgång till av din kursinstruktör.


Om du följer den här kursen själv kan du hitta en lista över tredjepartsvärdar för demo-ändamål på https://directory.btcpayserver.org/filter/hosts. Vi avråder starkt från att använda dessa tredjepartsalternativ som produktionsmiljöer; de tjänar dock rätt syfte för att introducera användningen av Bitcoin och BTCPay Server.


Som BTCPay Server rockstar-trainee kanske du har tidigare erfarenhet av att konfigurera en Bitcoin-nod. Den här kursen är särskilt anpassad till BTCPay Server Software stack.


Många av alternativen i BTCPay Server finns i en eller annan form i annan Bitcoin Wallet-relaterad programvara.


### Inloggningsskärm för BTCPay-server


När du välkomnas till Demo-miljön ombeds du att "Logga in" eller "Skapa ditt konto" Serveradministratörer kan av säkerhetsskäl inaktivera funktionen för att skapa nya konton. BTCPay Servers logotyper och knappfärger kan ändras eftersom BTCPay Server är programvara med öppen källkod. En tredjepartsvärd kan vitmärka programvaran och ändra hela utseendet.


![image](assets/en/0.webp)


### Fönstret Skapa ett konto


För att skapa konton på BTCPay Server krävs giltiga Address-strängar för e-post; example@email.com skulle vara en giltig sträng för e-post.


Lösenordet måste vara minst 8 tecken långt och innehålla bokstäver, siffror och tecken. När du har angett lösenordet en gång måste du verifiera att lösenordet är detsamma som det som skrevs in i det första lösenordsfältet.


När både e-post- och lösenordsfälten är korrekt ifyllda klickar du på knappen "Skapa konto". Detta sparar e-postadressen och lösenordet på instruktörens BTCPay Server-instans.


![image](assets/en/1.webp)


**!Obs!**


Om du följer den här kursen på egen hand kommer du sannolikt att skapa det här kontot på en tredjepartsvärd; därför betonar vi återigen att dessa inte ska användas som produktionsmiljöer utan endast i utbildningssyfte.


### Skapande av konto av BTCPays serveradministratör


Administratören för BTCPay Server-instansen kan också skapa konton för BTCPay Server. Administratören för BTCPay Server-instansen kan klicka på "Serverinställningar" (1), klicka på fliken "Användare" (2) och klicka på knappen "+ Lägg till användare" (3) längst upp till höger på fliken Användare. I mål (4.3) kommer du att lära dig mer om administratörens kontroll av konton.


![image](assets/en/2.webp)


Som administratör behöver du användarens e-post Address och ställa in ett standardlösenord. Av säkerhetsskäl rekommenderar vi att administratören informerar användaren om att ändra lösenordet innan kontot används. Om administratören inte anger något lösenord och SMTP har konfigurerats på servern kommer användaren att få ett e-postmeddelande med en inbjudningslänk för att skapa sitt konto och ange ett lösenord själv.


### Exempel


Om du följer kursen med en instruktör ska du följa den länk som instruktören tillhandahåller och skapa ditt konto i demomiljön. Se till att din e-postadress Address och ditt lösenord sparas på ett säkert sätt; du behöver dessa inloggningsuppgifter för resten av demomålen i den här kursen.


Din instruktör kan ha samlat in e-postmeddelandet Address i förväg och skickat en inbjudningslänk före den här övningen. Kontrollera din e-post om du blir tillsagd att göra det.


När du går kursen utan instruktör skapar du ditt konto med hjälp av demomiljön för BTCPay Server; gå till


https://Mainnet.demo.btcpayserver.org/login.


Detta konto ska endast användas för demonstration/utbildning och aldrig för affärsändamål.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig följande:



- Så här skapar du ett konto på en hostad server via Interface.
- Hur en serveradministratör manuellt kan lägga till användare i serverinställningarna.


### Bedömning av kunskap


#### KA Konceptuell granskning


Ge skäl till varför det är en dålig idé att använda en demoserver för produktionsändamål.


## Hantera användarkonto(n)


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Kontohantering på BTCPay-server


När en butiksägare har skapat sitt konto kan de hantera det längst ner till vänster i BTCPay Server UI. Under knappen Konto finns det flera inställningar på högre nivå.



- Mörkt/ljust läge.
- Dölj känslig information - växla.
- Hantera konto.


![image](assets/en/3.webp)


### Mörkt och ljust läge


Användare av BTCPay Server kan välja mellan en version av användargränssnittet i ljust eller mörkt läge. Sidor som vänder sig till kunder kommer inte att ändras. De använder de inställningar som kunden föredrar när det gäller mörkt eller ljust läge.


### Dölj känslig information Toggle


Knappen Hide Sensitive Info ger en snabb och enkel Layer av säkerhet. När du behöver använda din BTCPay Server, men det kan finnas människor som lurar över axeln på dig i ett offentligt utrymme, slå på Hide Sensitive Info, så kommer alla värden i BTCPay Server att döljas. Man kanske kan titta över din axel, men kan inte längre se de värden du har att göra med.


### Hantera konto


När användarkontot har skapats är det här du hanterar lösenord, 2FA eller API-nycklar.


### Hantera konto - Konto


Uppdatera eventuellt ditt konto med en annan e-post Address. För att säkerställa att din e-postadress Address är korrekt kan du med BTCPay Server skicka ett verifieringsmeddelande. Klicka på spara om användaren anger ett nytt e-postmeddelande Address och bekräftar att verifieringen fungerade. Användarnamnet förblir detsamma som i det tidigare e-postmeddelandet.


En användare kan välja att radera hela sitt konto. Detta kan göras genom att klicka på knappen Ta bort på fliken Konto.


![image](assets/en/4.webp)


**!Obs!**


När du har ändrat e-postadressen ändras inte användarnamnet för kontot. Den tidigare angivna e-postadressen Address kommer att förbli inloggningsnamnet.


### Hantera konto - Lösenord


En student kanske vill ändra sitt lösenord. Det kan han göra genom att gå till fliken Lösenord. Här måste han eller hon skriva in sitt gamla lösenord och kan ändra det till ett nytt.


![image](assets/en/5.webp)


### Tvåfaktorsautentisering (2fa)


För att begränsa konsekvenserna av ett stulet lösenord kan du använda tvåfaktorsautentisering (2FA), en relativt ny säkerhetsmetod. Du kan aktivera tvåfaktorsautentisering via Hantera konto och fliken för tvåfaktorsautentisering. Du måste genomföra ett andra steg efter att du har loggat in med ditt användarnamn och lösenord.


BTCPay Server stöder två metoder för att aktivera 2FA: appbaserad 2FA (Authy, Google, Microsoft Authenticators) eller via säkerhetsenheter (FIDO2 eller LNURL Auth).


### Tvåfaktorsautentisering - App-baserad


Baserat på din mobiltelefons operativsystem (Android eller iOS) kan du välja mellan följande appar;


1. Ladda ner en tvåfaktorsautentisering.


   - Authy för [Android] (https://play.google.com/store/apps/details?id=com.authy.authy) eller [iOS] (https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator för [Android] (https://play.google.com/store/apps/details?id=com.azure.authenticator) eller [iOS] (https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator för [Android] (https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) eller [iOS] (https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Efter nedladdning och installation av Authenticator-appen.


   - Skanna QR-koden som tillhandahålls av BTCPay Server
   - Eller ange den nyckel som genererats av BTCPay Server manuellt i din Authenticator-app.

3. Authenticator-appen kommer att ge dig en unik kod. Ange den unika koden i BTCPay Server för att verifiera installationen och klicka på Verifiera för att slutföra processen.


![image](assets/en/6.webp)


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig följande:



- Alternativ för kontohantering och de olika sätten att hantera ett konto på en BTCPay Server-instans.
- Så här ställer du in appbaserad 2FA.


### Bedömning av kunskap


#### KA Konceptuell granskning


Beskriv hur appbaserad 2FA hjälper till att skydda ditt konto.


## Skapa en ny butik


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Skapa din butiksguide


När en ny användare loggar in på BTCPay Server är miljön tom och behöver en första butik. Introduktionsguiden för BTCPay Server ger användaren möjlighet att "Skapa din butik" (1). En butik kan ses som ett hem för dina Bitcoin-behov. En ny BTCPay Server-nod kommer att börja med att synkronisera Bitcoin Blockchain (2). Beroende på vilken infrastruktur du kör BTCPay Server på kan det ta allt från några timmar till några dagar. Instansens aktuella version visas i det nedre högra hörnet av ditt BTCPay Server-gränssnitt. Detta är användbart för referens vid felsökning.


![image](assets/en/7.webp)


### Skapa din butiksguide


När du följer den här kursen kommer du att börja med en skärm som skiljer sig något från föregående sida. Eftersom din instruktör har förberett demomiljön har Bitcoin Blockchain synkroniserats tidigare, och därför kommer du inte att se nodernas synkroniseringsstatus.


En användare kan välja att radera hela sitt konto. Detta kan göras genom att klicka på knappen Ta bort på fliken Konto.


![image](assets/en/8.webp)


**!Obs!**


BTCPay Server-konton kan skapa ett obegränsat antal butiker. Varje butik är en Wallet eller ett "hem".


### Exempel


Börja med att klicka på "Skapa din butik".


![image](assets/en/9.webp)


Detta kommer att skapa ditt första hem och instrumentpanel för att använda BTCPay Server.


(1) Efter att ha klickat på "Skapa din butik" kommer BTCPay Server att kräva att du namnger butiken; detta kan vara något användbart för dig.


![image](assets/en/10.webp)


(2) En standardvaluta för butiken måste ställas in härnäst, antingen en fiatvaluta eller en valuta denominerad i Bitcoin eller Sats. För demomiljön kommer vi att ställa in den till USD.


![image](assets/en/11.webp)


(3) Som en sista parameter i butiksinställningen kräver BTCPay Server att du ställer in en "Preferred price source" för att jämföra Bitcoin:s pris mot det aktuella fiat-priset så att din butik visar rätt Exchange-kurs mellan Bitcoin och den butiksinställda fiat-valutan. Vi kommer att hålla oss till standardvärdet i demoexemplet och ställa in detta till Kraken Exchange. BTCPay Server använder Kraken API för att kontrollera Exchange-kurserna.


![image](assets/en/12.webp)


(4) Nu när dessa butiksparametrar har ställts in klickar du på knappen Skapa och BTCPay Server skapar din första butiks instrumentpanel, där guiden fortsätter.


![image](assets/en/13.webp)


Gratulerar, du har skapat din första butik och därmed är övningen avslutad.


![image](assets/en/14.webp)


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig:



- Skapa butik och konfigurera en standardvaluta, kombinerat med inställningar för priskälla.
- Varje "butik" är ett nytt hem som är separerat från andra butiker på den här installationen av BTCPay Server.


# Introduktion till att säkra Bitcoin-nycklar


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Förståelse av generering av Bitcoin-nycklar


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Hur genererar man Bitcoin-nycklar?


Bitcoin plånböcker, när de skapas, skapa en så kallad "seed". I det sista målet skapade du en "seed", Serien av ord som genereras tidigare är också känd som Mnemonic-fraser. seed används för att härleda individuella Bitcoin-nycklar och används för att skicka eller ta emot Bitcoin. seed-fraser ska aldrig delas med tredje part eller icke betrodda kollegor.


seed-generationen utförs enligt den industristandard som kallas "Hierarchical Deterministic" (HD)-ramverket.


![image](assets/en/15.webp)


### Adresser


BTCPay Server är byggd för att generate en ny Address. Detta lindrar problemet med återanvändning av offentliga nycklar eller Address. Att använda samma offentliga nyckel gör det mycket enkelt att spåra hela din betalningshistorik. Att tänka på nycklar som kuponger för engångsbruk skulle förbättra din integritet avsevärt. Vi använder också Bitcoin-adresser, förväxla inte dessa med offentliga nycklar.


En Address härleds från den publika nyckeln genom en "hashingalgoritm" De flesta plånböcker och transaktioner visar dock adresser snarare än de offentliga nycklarna. Adresser är i allmänhet kortare än publika nycklar och börjar vanligtvis med `1`, `3` eller `bc1`, medan publika nycklar börjar med `02`, `03` eller `04`.



- Adresser som börjar med `1.....` är fortfarande mycket vanliga adresser. Som nämndes i kapitlet "Skapa en ny butik" är detta äldre adresser. Den här Address-typen är avsedd för P2PKH-transaktioner. P2Pkh använder Base58-kodning, vilket gör Address skiftlägeskänslig. Dess struktur är baserad på den publika nyckeln med en extra siffra som identifierare.



- Adresser som börjar med `bc1...` håller långsamt på att bli mycket vanliga adresser. Dessa är kända som (infödda) SegWit-adresser. Dessa erbjuder en bättre avgiftsstruktur än de andra nämnda adresserna. Native SegWit-adresser använder Bech32-kodning och tillåter endast små bokstäver.



- Adresser som börjar med `3...` används ofta fortfarande av börser för insättningsadresser. Dessa adresser nämns i kapitlet "Skapa en ny butik", omslutna eller kapslade SegWit-adresser. De kan dock också fungera som en "Multisig Address". När de används som en SegWit Address finns det vissa besparingar på transaktionsavgifter, återigen mindre än Native SegWit. P2SH-adresser använder Base58-kodning. Detta gör den fallkänslig, som den äldre Address.



- Adresser som börjar med `2...` är Testnet-adresser. De är avsedda att ta emot Testnet Bitcoin (tBTC). Du bör aldrig blanda ihop detta och skicka Bitcoin till dessa adresser. För utvecklingsändamål kan du generate en Testnet Wallet. Det finns flera kranar online för att få Testnet Bitcoin. Köp aldrig Testnet Bitcoin. Testnet Bitcoin är minerad. Detta kan vara en anledning för en utvecklare att använda Regtest istället. Detta är en lekplatsmiljö för utvecklare, som saknar vissa nätverkskomponenter. Bitcoin är dock mycket användbar för utvecklingsändamål.


### Offentliga nycklar


Offentliga nycklar används mindre ofta i praktiken idag. Med tiden har Bitcoin-användare ersatt dem med adresser istället. De finns fortfarande kvar och används fortfarande ibland. Publika nycklar är i allmänhet mycket längre strängar än adresser. Precis som med adresser börjar de med en specifik identifierare.



- För det första är `02...` och `03...` mycket vanliga identifikatorer för offentliga nycklar kodade i SEC-format. Dessa kan bearbetas och omvandlas till adresser för mottagning, användas för att skapa multi-sig-adresser eller för att verifiera en signatur. Tidiga Bitcoin-transaktioner använde publika nycklar som en del av P2PK-transaktioner.



- HD-plånböcker använder dock en annan struktur. `xpub...`, `ypub...` eller `zpub...` kallas för utökade publika nycklar, eller xpubs. Dessa nycklar används för att härleda många publika nycklar som en del av HD Wallet. Eftersom din xpub innehåller uppgifter om hela din historik, dvs. tidigare och framtida transaktioner, ska du aldrig dela den med någon som inte är betrodd.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig följande:



- Skillnaderna mellan adresser och datatyper för publika nycklar samt fördelarna med att använda adresser i stället för publika nycklar.


### Bedömning av kunskap


Beskriv fördelen med att använda nya adresser för varje transaktion jämfört med Address återanvändning eller metoder med publika nycklar.


## Säkra nycklar med en Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Förvaring av Bitcoin-nycklar


Efter att ha genererat en seed-fras kräver listan med 12-24 ord som genereras i den här boken ordentlig säkerhetskopiering och säkerhet, eftersom dessa ord är det enda sättet att återfå åtkomst till en Wallet. HD-plånbokens struktur och hur den genererar adresser deterministiskt med hjälp av en enda seed innebär att alla dina skapade adresser kommer att säkerhetskopieras med hjälp av denna enda lista med Mnemonic-ord, som representerar din seed eller återställningsfras.


Håll din återställningsfras säker. Om någon får tillgång till den, särskilt med skadligt uppsåt, kan de flytta dina pengar. Hålla seed säker och säker, samtidigt som du kommer ihåg att det är ömsesidigt mellan dem. Det finns flera metoder för att lagra Bitcoin privata nycklar, var och en med sina egna fördelar och nackdelar, när det gäller säkerhet, integritet, bekvämlighet och fysisk lagring. På grund av vikten av privata nycklar tenderar Bitcoin-användare att lagra och förvara dessa nycklar på ett säkert sätt i "egen förvaring" snarare än att använda "förvaringstjänster" som banker. Beroende på användaren måste de använda antingen en Cold-lagringslösning eller en Hot Wallet.


### Hot och Cold lagring av Bitcoin nycklar


Vanligtvis är Bitcoin-plånböcker denominerade i en Hot Wallet eller en Cold Wallet. De flesta avvägningar ligger i bekvämlighet, användarvänlighet och säkerhetsrisker. Var och en av dessa metoder kan också ses i en depåförvaringslösning. Avvägningarna här är dock mestadels säkerhets- och integritetsbaserade och går utanför ramen för den här kursen.


### Hot Wallet


Hot-plånböcker är det mest praktiska sättet att interagera med Bitcoin via mobil-, webb- eller skrivbordsprogramvara. Wallet är alltid ansluten till internet, vilket gör det möjligt för användare att skicka eller ta emot Bitcoin. Detta är dock också dess svaghet; Wallet, eftersom den alltid är online, är nu mer sårbar för attacker från hackare eller skadlig kod på din enhet. I BTCPay Server lagrar Hot-plånböckerna de privata nycklarna i instansen. Alla som har åtkomst till din BTCPay Server-butik kan potentiellt stjäla pengar från denna Address om de är illvilliga. När BTCPay Server körs i en värdmiljö bör du alltid överväga detta i din säkerhetsprofil och helst inte använda en Hot Wallet i ett sådant fall. När BTCPay Server installeras på hårdvara som ägs och säkras av dig sänks riskprofilen avsevärt, men den försvinner aldrig helt.


### Cold Wallet


Privatpersoner flyttar sin Bitcoin till en Cold Wallet eftersom den kan isolera de privata nycklarna från internet och därmed skydda dem från potentiella onlinehot. Genom att ta bort internetanslutningen från ekvationen minskar risken för skadlig kod, spionprogram och SIM-byten. Cold-lagring anses vara överlägsen Hot-lagring vad gäller säkerhet och autonomi, förutsatt att tillräckliga försiktighetsåtgärder vidtas för att förhindra att de privata nycklarna i Bitcoin går förlorade. Cold-lagring är mest lämplig för stora mängder Bitcoin, som inte är avsedda att användas ofta på grund av Wallet-installationens komplexitet.


Det finns olika metoder för att lagra Bitcoin-nycklar i Cold-lagring, från pappersplånböcker till hjärnplånböcker, hårdvaruplånböcker eller, från början, en Wallet-fil. De flesta plånböcker använder BIP 39 för att generate seed frasen. Men inom Bitcoin Core-programvaran har man ännu inte nått konsensus om hur den ska användas. Bitcoin Core-programvaran kommer fortfarande att generate en Wallet.dat-fil, som du måste lagra på en säker offlineplats.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig:



- Skillnaderna mellan Hot- och Cold-plånböckerna när det gäller funktionalitet och deras avvägningar.


### Kunskapsbedömning Konceptuell granskning



- Vad är en Wallet?



- Vad är skillnaden mellan plånböckerna Hot och Cold?



- Beskriv vad som menas med att "generera en Wallet"?


## Använda tangenterna på din Bitcoin


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay Server Wallet


BTCPay Server består av följande standardfunktioner enligt Wallet:



- Transaktioner
- Skicka
- Ta emot
- Rescan
- Dra betalningar
- Utbetalningar
- PSBT
- Allmänna inställningar


### Transaktioner


Administratörer kan se de inkommande och utgående transaktionerna för On-Chain Wallet som är anslutna till den här specifika butiken i transaktionsvyn. Varje transaktion har en distinktion mellan de mottagna och skickade beloppen. Mottagna kommer att vara Green och utgående transaktioner kommer att vara röda. I transaktionsvyn för BTCPay Server ser administratörerna också en uppsättning standardetiketter.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Hur man skickar


BTCPay-serverns sändningsfunktion skickar transaktioner från din BTCPay-server On-Chain Wallet. BTCPay Server tillåter flera sätt att signera dina transaktioner för att spendera pengar. En transaktion kan signeras med;



- Hardware Wallet
- Plånböcker som stöder PSBT
- HD:s privata nyckel eller återställningsfrön.
- Hot Wallet


#### Hardware Wallet


BTCPay Server har inbyggt Hardware Wallet-stöd, så att du kan använda din Hardware Wallet med BTCPay Vault utan att läcka information till appar eller servrar från tredje part. Hardware Wallet-integrationen i BTCPay Server gör att du kan importera din Hardware Wallet och spendera inkommande medel med en enkel bekräftelse på din enhet. Dina privata nycklar lämnar aldrig enheten och alla medel valideras mot din Full node, vilket säkerställer att ingen data läcker ut.


#### Signering med en Wallet som stöder PSBT


PSBT (Partiellt signerade Bitcoin-transaktioner) är ett utbytesformat för Bitcoin-transaktioner som fortfarande behöver signeras fullständigt. PSBT stöds i BTCPay Server och kan signeras med kompatibla hårdvaru- och mjukvaruplånböcker.


Konstruktionen av en fullständigt signerad Bitcoin-transaktion går igenom följande steg:



- En PSBT byggs upp med specifika in- och utgångar, men inga signaturer
- Den exporterade PSBT kan importeras av en Wallet som stöder detta format
- Transaktionsdata kan inspekteras och signeras med hjälp av Wallet
- Den signerade PSBT-filen exporteras från Wallet och importeras med BTCPay Server
- BTCPay Server producerar den sista Bitcoin-transaktionen
- Du verifierar resultatet och sänder det till nätverket


#### Signering med privat nyckel för HD eller Mnemonic seed


Om du har skapat en Wallet innan du använder BTCPay Server kan du spendera pengarna genom att ange din privata nyckel i ett lämpligt fält. Ange en korrekt "AccountKeyPath" i Wallet> Inställningar; annars kan du inte spendera.


#### Signera med en Hot Wallet


Om du skapade en ny Wallet när du konfigurerade din butik och aktiverade den som en Hot Wallet, kommer den automatiskt att använda den seed som lagras på en server för att signera.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) är en Bitcoin-protokollfunktion som gör att du kan ersätta en tidigare sänd transaktion (medan den fortfarande är obekräftad). Detta gör det möjligt att slumpa fram din Wallet:s transaktionsfingeravtryck eller ersätta det med en högre avgiftssats för att flytta transaktionen högre upp i kön för bekräftelse (Mining). Detta kommer effektivt att ersätta den ursprungliga transaktionen eftersom den högre avgiftssatsen kommer att prioriteras, och när den har bekräftats kommer den att ogiltigförklara den ursprungliga transaktionen (inga dubbla utgifter).


Tryck på knappen "Advanced Settings" för att visa alternativen för RBF.


![image](assets/en/16.webp)



- Randomize för högre integritet, gör att transaktionen kan ersättas automatiskt för randomisering av transaktionens fingeravtryck.
- Ja, flagga transaktion för RBF och ersättas uttryckligen (ersätts inte som standard, endast genom input)
- Nej, låt inte transaktionen bytas ut.


### Val av mynt


Coin selection är en avancerad integritetshöjande funktion som gör att du kan välja mynt du vill spendera när du skapar en transaktion. Du kan till exempel betala med mynt som kommer direkt från en conjoin-mix.


Myntval fungerar naturligt med Wallet:s etikettfunktion. Detta gör att du kan märka inkommande medel för smidigare UTXO-hantering och utgifter.


BTCPay Server stöder BIP-329 för etiketthantering. Om du överför från en Wallet som stöder BIP-329 och har ställt in etiketter, kommer BTCPay Server att känna igen och importera dem automatiskt. Vid migrering av servrar kan den här informationen också exporteras och importeras till den nya miljön.


### Hur man tar emot


När du klickar på mottagningsknappen i BTCPay Server genereras en oanvänd Address som kan användas för att ta emot betalningar. Administratörer kan också generate en ny Address genom att skapa en ny "Invoice"


BTCPay Server kommer alltid att uppmana dig att generate följande tillgängliga Address för att förhindra återanvändning av Address. Efter att ha klickat på "generate nästa tillgängliga BTC Address" genererade BTCPay Server en ny Address och QR. Det låter dig också direkt ställa in en etikett till Address för bättre hantering av dina adresser.


![image](assets/en/17.webp)


![image](assets/en/18.webp)


#### Skanna om


Rescan-funktionen förlitar sig på Bitcoin Core 0.17.0:s "Scantxoutset" för att skanna det aktuella tillståndet för Blockchain (kallad UTXO Set) för mynt som tillhör det konfigurerade härledningsschemat. En Wallet-återskanning tar itu med två vanliga problem som BTCPay Server-användare ofta stöter på.


1. Gap limit-problem - De flesta tredjepartsplånböcker är lätta plånböcker som delar en nod mellan många användare. Lätta och Full node-beroende plånböcker begränsar antalet (vanligtvis 20) adresser utan saldo som de spårar på Blockchain för att förhindra prestandaproblem. BTCPay Server genererar en ny Address för varje Invoice. Med ovanstående i åtanke, efter att BTCPay Server har genererat 20 obetalda fakturor i följd, slutar den externa Wallet att hämta transaktionerna, förutsatt att inga nya transaktioner inträffade. Din externa Wallet kommer inte att visa dem när fakturor betalas den 21:a, 22:a osv. Å andra sidan spårar BTCPay Server Wallet internt alla Address som den genererar, tillsammans med en betydligt högre gapgräns. Den förlitar sig inte på en tredje part och kan alltid visa ett korrekt saldo.

2. Lösningen med gap-limit - Om din [externa/existerande Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) tillåter konfiguration av gap-limit är den enkla lösningen att öka den. Majoriteten av plånböckerna tillåter dock inte detta. De enda plånböckerna som för närvarande stöder konfigurering av gap-limit som vi känner till är Electrum, Wasabi och Sparrow wallet. Tyvärr är det troligt att du kommer att stöta på problem med många andra plånböcker. För bästa användarupplevelse och integritet bör du överväga att använda BTCPay-serverns interna Wallet istället för externa plånböcker.


#### BTCPay Server använder "mempoolfullrbf=1"


BTCPay Server använder "mempoolfullrbf=1"; vi har lagt till detta som standard i din BTCPay Server-konfiguration. Men vi har också gjort det till en funktion som du själv kan inaktivera. Utan "mempoolfullrbf=1", om en kund dubbelspenderar en betalning med en transaktion som inte signalerar RBF, skulle handlaren veta det först efter bekräftelse.


En administratör kanske vill välja bort den här inställningen. Med följande sträng kan du ändra standardinställningen.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```


### BTCPay Server Wallet inställningar


Wallet-inställningar i BTCPay Server ger en tydlig och kortfattad översikt över Wallet:s allmänna inställningar. Alla dessa inställningar är förifyllda om Wallet skapades med BTCPay Server.


![image](assets/en/19.webp)


Wallet-inställningar i BTCPay Server ger en tydlig och koncis översikt över din Wallet:s allmänna inställningar. Alla dessa inställningar är förifyllda om Wallet skapades med BTCPay Server. BTCPay Servers Wallet-inställningar börjar med Wallet-statusen. Är det en Watch-only eller en Hot Wallet? Beroende på Wallet-typen kan åtgärderna variera, inklusive att skanna om Wallet för saknade transaktioner, ta bort gamla transaktioner från historiken, registrera Wallet för betalningslänkar eller ersätta och ta bort den aktuella Wallet som är kopplad till butiken. I BTCPay Servers Wallet-inställningar kan administratörer ställa in en etikett för Wallet för bättre Wallet-hantering. Här kommer administratören också att kunna se avledningsschema, kontonyckel (xpub), fingeravtryck och nyckelstig. Betalningar i Wallet-inställningar har endast två huvudinställningar. Betalningen är ogiltig om transaktionen inte bekräftas inom (inställda minuter) efter att Invoice har löpt ut. Betrakta Invoice som bekräftad när betalningstransaktionen har X antal bekräftelser. Administratörer kan också ställa in en växling för att visa rekommenderade avgifter på betalningsskärmen eller ställa in ett mål för manuell bekräftelse i antalet block.


![image](assets/en/20.webp)


**!Obs!**


Om du följer den här kursen på egen hand kommer du sannolikt att skapa det här kontot på en tredjepartsvärd. Därför föreslår vi återigen att dessa inte ska användas som produktionsmiljöer, utan endast för utbildningsändamål.


### Exempel


#### Ställ in en Bitcoin Wallet i BTCPay Server


BTCPay Server erbjuder två metoder för att sätta upp en Wallet. Ett sätt är att importera en befintlig Bitcoin Wallet. Importen kan göras genom att ansluta en Hardware Wallet, importera en Wallet-fil, ange en utökad publik nyckel, skanna en Wallet:s QR-kod eller, minst fördelaktigt, ange en tidigare skapad Wallet recovery seed för hand. I BTCPay Server är det också möjligt att skapa en ny Wallet. Det finns två möjliga sätt att konfigurera BTCPay Server vid generering av en ny Wallet.


Alternativet Hot Wallet i BTCPay Server möjliggör funktioner som "PayJoin" eller "Liquid". Det finns dock en nackdel: den återställnings-seed som genereras för denna Wallet kommer att lagras på servern, där vem som helst med adminkontroll kan hämta den. Eftersom din privata nyckel härleds från din återställnings-seed kan en illvillig aktör få tillgång till dina nuvarande och framtida medel!


För att minska denna risk i BTCPay Server kan en administratör ställa in värdet i Serverinställningar > Policyer > "Tillåt icke-admins att skapa Hot-plånböcker för sina butiker" till "nej", eftersom det är standardvärdet. För att förbättra säkerheten för dessa Hot-plånböcker bör serveradministratören aktivera 2FA-autentisering på konton som tillåts ha Hot-plånböcker. Att lagra privata nycklar på en offentlig server är en farlig metod och medför betydande risker. Vissa av dem liknar Lightning Network-riskerna (se nästa kapitel för Lightning Network-risker).


Det andra alternativet som BTCPay Server erbjuder för att generera en ny Wallet är genom att skapa en Watch-only wallet. BTCPay Server kommer att generate dina privata nycklar en gång. Efter att användaren har bekräftat att han eller hon har skrivit ner sin seed-fras kommer BTCPay Server att radera de privata nycklarna från servern. Som ett resultat har din butik nu en Watch-only wallet ansluten till den. För att spendera de medel som mottagits på din Watch-only wallet, se kapitlet Hur man skickar, antingen genom att använda BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction), eller, minst rekommenderat, manuellt tillhandahålla din seed-fras.


Du skapade en ny "Store" i den sista delen. Installationsguiden fortsätter med att fråga om du vill "Konfigurera en Wallet" eller "Konfigurera en Lightning-nod". I det här exemplet kommer du att följa guiden "Konfigurera en Wallet" (1).


![image](assets/en/21.webp)


Efter att ha klickat på "Konfigurera en Wallet" fortsätter guiden med att fråga hur du vill fortsätta; BTCPay Server erbjuder nu möjligheten att ansluta en befintlig Bitcoin Wallet till din nya butik. Om du inte har en Wallet föreslår BTCPay Server att du skapar en ny. Detta exempel följer stegen för att "skapa en ny Wallet" (2). Följ stegen för att lära dig hur du "ansluter en befintlig Wallet" (1).


![image](assets/en/22.webp)


**!Obs!**


Om du går den här kursen i ett klassrum, observera att det aktuella exemplet och seed som vi har genererat endast är avsedda för utbildningsändamål. Det bör aldrig finnas någon betydande mängd annat än vad som krävs under övningarna på dessa adresser.


(1) Fortsätt guiden "Ny Wallet" genom att klicka på knappen "Skapa en ny Wallet".


![image](assets/en/23.webp)


(2) När du klickar på "Skapa en ny Wallet" kommer nästa fönster i guiden att ge alternativen "Hot Wallet" och "Watch-only wallet" Om du följer med en instruktör är din miljö en delad Demo, och du kan bara skapa en Watch-only wallet. Lägg märke till skillnaden mellan de två figurerna nedan. När du befinner dig i Demo-miljön och följer med instruktören skapar du en "Watch-only wallet" och fortsätter med guiden "Ny Wallet".


![image](assets/en/24.webp)


![image](assets/en/25.webp)


(3) Fortsätter du med den nya Wallet-guiden är du nu i avsnittet Skapa BTC Watch-only wallet. Här får vi ställa in Wallet: s "Address-typ" BTCPay Server låter dig välja din föredragna Address-typ; när den här kursen skrivs rekommenderas det fortfarande att använda bech32-adresser. Du kan lära dig mer i detalj om adresser i det första kapitlet i den här delen.



- SegWit (bech32)
  - Inhemska SegWit-adresser börjar med `bc1q`.
  - Exempel: `bc1qXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Arv
  - Legacy-adresser är adresser som börjar med siffran "1".
  - Exempel: `15e15hXXXXXXXXXXXXXXXXXXXXXX`
- Taproot (för avancerade användare)
  - Taproot adresser börjar med `bc1p`.
  - Exempel: `bc1pXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit inplastad
  - SegWit-adresser börjar med `3`.
  - Exempel: `37BBXXXXXXXXXXXXXXX`


Välj SegWit (rekommenderas) som din föredragna Wallet Address-typ.


![image](assets/en/26.webp)


(4) När du ställer in parametern för Wallet tillåter BTCPay Server användarna att ställa in en valfri passphrase via BIP39; se till att bekräfta ditt lösenord.


![image](assets/en/27.webp)


(5) När du har ställt in Wallet:s Address-typ och eventuellt ställt in några avancerade alternativ klickar du på Skapa och BTCPay Server kommer att generate din nya Wallet. Observera att detta är det sista steget innan du genererar din seed-fras. Se till att du bara gör detta i en miljö där någon kanske inte kan stjäla seed-frasen genom att titta på din skärm.


![image](assets/en/28.webp)


(6) På följande skärm i guiden visar BTCPay Server dig Recovery seed-frasen för din nyligen genererade Wallet; dessa är nycklarna till att återställa din Wallet och signera transaktioner. BTCPay Server genererar en seed-fras med 12 ord. Dessa ord kommer att raderas från servern efter den här inställningsskärmen. Denna Wallet är specifikt en Watch-only wallet. Det rekommenderas att inte lagra denna seed-fras digitalt eller med fotografisk bild. Användare kan endast gå vidare i guiden om de aktivt bekräftar att de skrivit ner sin seed-fras.


![image](assets/en/29.webp)


(7) Efter att ha klickat på Done och säkrat den nyligen genererade Bitcoin seed-frasen kommer BTCPay Server att uppdatera din butik med den bifogade nya Wallet och är redo att ta emot betalningar. I användaren Interface, i den vänstra navigeringsmenyn, märker du hur Bitcoin nu är markerad och aktiverad under Wallet.


![image](assets/en/30.webp)


### Exempel: Skriva ner en seed-fras


Det här är ett särskilt säkert tillfälle att använda Bitcoin. Som tidigare nämnts är det bara du som ska ha tillgång till eller kunskap om din seed-fras. När du följer med en instruktör och ett klassrum ska den genererade seed endast användas i den här kursen. Alltför många faktorer, inklusive nyfikna ögon från klasskamrater, osäkra system och andra, gör att dessa nycklar endast är pedagogiska och opålitliga. De nycklar som genereras bör dock fortfarande lagras för kursexempel.


Den första metoden vi kommer att använda i den här situationen, som också är den minst säkra, är att skriva ner seed-frasen i rätt ordning. Ett seed-fras-kort ingår i kursmaterialet som tillhandahålls studenten eller kan hittas på BTCPay Server GitHub. Vi kommer att använda detta kort för att skriva ner de ord som genererades i föregående steg. Se till att skriva ner dem i rätt ordning. När du har skrivit ner dem, kontrollera dem mot vad som gavs av programvaran för att se till att du skrev ner dem i rätt ordning. När du har skrivit ner det klickar du på kryssrutan som anger att du har skrivit ner din seed-fras korrekt.


### Exempel: Lagring av en seed-fras på en Hardware Wallet


I den här kursen tar vi upp hur man lagrar en seed-fras på en Hardware Wallet. Att följa den här kursen med en instruktör kan ibland inkludera en sådan enhet. I kursen har handledningsmaterialet sammanställt en lista över hårdvaruplånböcker som skulle vara lämpliga för denna övning.


Vi kommer att använda BTCPay Server-valv och en Blockstream Jade Hardware Wallet i det här exemplet.


Du kan också följa med i en videoguide om hur du ansluter en Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Ladda ner BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Se till att du laddar ner rätt filer för ditt specifika system. Windows-användare ska ladda ner paketet [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), Mac-användare ska ladda ner [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) och Linux-användare ska ladda ner [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


När du har installerat BTCPay Server Vault startar du programmet genom att klicka på ikonen på skrivbordet. När BTCPay Server Vault är korrekt installerat och startas för första gången kommer det att be om tillstånd att användas med webbapplikationer. Den kommer att be om att få tillgång till den specifika BTCPay Server som du arbetar med. Acceptera dessa villkor. BTCPay Server Vault kommer nu att söka efter hårdvaruenheten. När enheten har hittats kommer BTCPay Server att känna igen att Vault körs och har hämtat din enhet.


**!Obs!**


Ge inte dina SSH-nycklar eller ditt serveradministratörskonto till någon annan än administratörer när du använder en Hot Wallet. Alla som har tillgång till dessa konton kommer att ha tillgång till medlen i Hot Wallet.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig följande:



- Transaktionsvyn av Bitcoin Wallet och dess olika kategoriseringar.
- Olika alternativ finns tillgängliga när du skickar från en Bitcoin Wallet, från hårdvara till Hot plånböcker.
- Problemet med gapgränsen som uppstår när man använder de flesta plånböcker och hur man löser detta.
- Hur man generate en ny Bitcoin Wallet inom BTCPay Server, inklusive lagring av nycklarna i en Hardware Wallet och säkerhetskopiering av återställningsfrasen.


I det här målet har du lärt dig hur man generate en ny Bitcoin Wallet inom BTCPay Server. Vi har ännu inte gått in på hur man säkrar eller använder dessa nycklar. I en snabb översikt över detta mål har du lärt dig hur du ställer in den första butiken. Du har lärt dig hur man generate en Bitcoin Recovery seed-fras.


### Kunskapsbedömning Praktisk genomgång


Beskriv en metod för att generera nycklar och ett system för att säkra dem, tillsammans med avvägningarna/riskerna med säkerhetssystemet.


## BTCPay Server Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


När en serveradministratör skapar en ny BTCPay Server-instans kan de konfigurera en Lightning Network-implementering, t.ex. LND, Core Lightning eller Eclair; se delen Konfigurera BTCPay Server för mer detaljerade installationsinstruktioner.


Om du följer med i ett klassrum fungerar anslutningen av en Lightning-nod till din BTCPay Server via en anpassad nod. En användare som inte är serveradministratör på BTCPay Server kommer inte att kunna använda den interna Lightning-noden som standard. Detta är för att skydda serverägaren från att förlora sina medel. Serveradministratörer kan installera ett plugin för att ge åtkomst till sin Lightning-nod via LNBank, men detta ligger utanför ramen för den här boken. Mer information om LNBank finns på den officiella sidan för insticksprogrammet.


### Anslut intern nod (serveradministratör)


Serveradministratören kan använda BTCPay Servers interna Lightning Node. Oavsett Lightning-implementering är det samma sak att ansluta till den interna Lightning-noden.


Gå till en tidigare installationsbutik och klicka på "Lightning" Wallet i den vänstra menyn. BTCPay Server ger två inställningsmöjligheter: att använda den interna noden (endast serveradministratör som standard) eller en anpassad nod (extern anslutning). Serveradministratörer kan klicka på alternativet "Använd intern nod". Det finns inget behov av ytterligare konfiguration. Klicka på knappen "spara" och notera meddelandet "BTC Lightning-noden uppdaterad". Butiken har nu framgångsrikt fått Lightning Network-funktioner.


### Anslut extern nod (serveranvändare/butiksägare)


Som standard får butiksägare inte använda serveradministratörens Lightning Node. Anslutningen måste göras till en extern nod, antingen en nod som ägs av butiksägaren innan en BTCPay-server konfigureras, ett LNBank-plugin om det görs tillgängligt av serveradministratören eller en förvaringslösning som Alby.


Gå till en tidigare installerad butik och klicka på "Lightning" under plånböcker i den vänstra menyn. Eftersom butiksägare inte får använda den interna noden som standard är det här alternativet grått. Att använda en anpassad nod är det enda alternativet som är tillgängligt som standard för butiksägare.


BTCPay Server kräver anslutningsinformation; den förtillverkade (eller depåförvaringslösningen) kommer att leverera denna information specifikt anpassad till en Lightning-implementering. Inom BTCPay Server kan butiksägare använda följande anslutningar;



- C-blixt via TCPellerUnixdomänocketanslutning.
- Blixtsnabb laddning via HTTPS
- Eclair via HTTPS
- LND via REST-proxy
- LNDhub via REST API


![image](assets/en/31.webp)


Klicka på "testa anslutning" för att säkerställa att du har angett anslutningsuppgifterna korrekt. När anslutningen har bekräftats vara bra klickar du på "Spara" och BTCPay Server visar att butiken har uppdaterats med en Lightning Node.


### Hantering av intern Lightning-nod LND (Serveradministratör)


Efter att ha anslutit den interna Lightning-noden kommer serveradministratörer att märka nya plattor på instrumentpanelen som är särskilt avsedda för Lightning-information.



- Balans mellan blixtar
- BTC i kanaler
  - BTC-öppningskanaler
  - BTC lokalt saldo
  - BTC-saldo på distans
  - BTC stänger kanaler
- BTC On-Chain
  - BTC bekräftat
  - BTC obekräftat
  - BTC reserverad
- Blixttjänster
  - Ride the Lightning (RTL).


Genom att klicka antingen på Ride the Lightning-logotypen i rutan "Lightning-tjänster" eller på "Lightning" under plånböckerna i vänstermenyn kan serveradministratörer nå RTL för hantering av Lightning-noder.


**Notera!


Anslutning av den interna Lightning Noden misslyckas - Om den interna anslutningen misslyckas, bekräfta:


1. Bitcoin On-Chain-noden är helt synkroniserad

2. Den interna blixtnoden är "Aktiverad" under "Blixt" > "Inställningar" > "BTC blixtinställningar"


Om du inte kan ansluta till din Lightning-nod kan du försöka starta om din server eller läsa mer information i BTCPay Server officiella dokumentation; https://docs.btcpayserver.org/Troubleshooting/. Du kan inte acceptera Lightning-betalningar i din butik förrän din Lightning-nod visas som "Online". Försök att testa din Lightning-anslutning genom att klicka på länken "Public Node Info".


### Blixt Wallet


Inom alternativet Lightning Wallet i den vänstra menyraden hittar serveradministratörer enkel åtkomst till RTL, deras Public node Info och Lightning-inställningar som är specifika för deras BTCPay Server-butik.


#### Intern nodinformation


Serveradministratörer kan klicka på den interna nodinformationen för att se serverns status (Online/Offline) och anslutningssträng för Clearnet eller Tor.


![image](assets/en/32.webp)


#### Ändra anslutning


För att ändra den externa Lightning-noden, gå till "Lightning Settings" och klicka på "Change connection" (bredvid "Public Node info"). Detta återställer den befintliga inställningen. Ange de nya noduppgifterna, klicka på Spara och butiken uppdateras i enlighet med detta.


![image](assets/en/33.webp)


#### Tjänster


Om serveradministratören bestämmer sig för att installera flera tjänster för Lightning-implementeringen kommer de att listas här. Med en standardimplementering av LND kommer administratörerna att ha Ride The Lightning (RTL) som ett standardverktyg för nodhantering.


#### BTC Lightning Wallet inställningar


Efter att ha lagt till Lightning-noden i butiken i ett tidigare steg kan butiksägare fortfarande välja att avaktivera den för sin butik genom att använda reglaget längst upp i Lightning-inställningarna.


![image](assets/en/34.webp)


#### Lightning Betalningsalternativ


Butiksägare kan ställa in följande parametrar för att förbättra Lightning-upplevelsen för sina kunder.



- Visa belopp för blixtbetalning i Satoshis.
- Lägg till hopptips för privata kanaler till Lightning Invoice.
- Unifiera On-Chain- och Lightning-betalnings-URL/QR-koder i kassan.
- Ange en beskrivningsmall för blixtfakturor.


#### LNURL


Butiksägare kan välja att antingen använda eller inte använda LNURL. En Lightning Network URL, eller LNURL, är en föreslagen standard för interaktioner mellan Lightning Payer och betalningsmottagaren. I korthet är en LNURL en bech32-kodad URL med LNURL som prefix. Lightning Wallet förväntas avkoda URL:en, kontakta URL:en och invänta ett JSON-objekt med ytterligare instruktioner, framför allt en tagg som definierar LNURL:ens beteende.



- Aktivera LNURL
- LNURL Klassiskt läge
  - För Wallet-kompatibilitet, Bech32-kodad (klassisk) vs cleartext URL (kommande)
- Tillåt betalningsmottagaren att lämna en kommentar.


### Exempel 1


#### Anslut till Lightning med den interna noden (administratör)


Det här alternativet är endast tillgängligt om du är administratör för den här instansen eller om administratören har ändrat standardinställningarna så att användarna kan använda den interna blixtnoden.


Som administratör klickar du på Lightning Wallet i den vänstra menyraden. BTCPay Server kommer att be dig att välja ett av två alternativ för att ansluta en Lightning-nod: en intern nod eller en anpassad extern nod. Klicka på "Använd intern nod" och klicka sedan på "Spara"


#### Hantering av din Lightning-nod (RTL)


Efter anslutning till den interna Lightning-noden kommer BTCPay Server att uppdateras och visa meddelandet "BTC Lightning-noden uppdaterad", vilket bekräftar att du nu har anslutit Lightning till din butik.


Hantering av lightning-noden är en uppgift för serveradministratören. Detta innebär följande:


- Hantera transaktion
- Hantering av likviditet
  - Inkommande likviditet
  - Utgående likviditet
- Hantering av kollegor och kanaler
  - Anslutna kollegor
  - Kanalavgifter
  - Kanalens status
- Gör ofta säkerhetskopior av kanaltillstånden.
- Kontroll av routingrapporter
- Alternativt kan du använda tjänster som Loop.


All hantering av Lightning-noder görs som standard med RTL (förutsatt att du kör på en LND-implementering). Administratörer kan klicka på sin Lightning Wallet i BTCPay Server och hitta en knapp för att öppna RTL. Huvudinstrumentpanelen i BTCPay Server är nu uppdaterad med Lightning Network Tiles, inklusive snabb åtkomst till RTL.


### Exempel 2


#### Anslut till blixtnedslag med Alby


När du ansluter dig till en depåbank som Alby bör butiksägare först skapa ett konto och besöka https://getalby.com/


![image](assets/en/35.webp)


När du har skapat Alby-kontot går du till din BTCPay Server-butik.


Steg 1: Klicka på "Set up a Lightning node" på Dashboard eller på "Lightning" under wallets.


![image](assets/en/36.webp)


Steg 2: Sätt in dina Wallet-anslutningsuppgifter som tillhandahålls av Alby. Klicka på Wallet på instrumentpanelen i Alby. Här hittar du "Wallet Connection Credentials". Kopiera dessa autentiseringsuppgifter. Klistra in autentiseringsuppgifterna från Alby i fältet Connection configuration i BTCPay Server.


![image](assets/en/37.webp)


Steg 3: När du har gett BTCPay Server anslutningsuppgifterna klickar du på knappen "Test Connection" för att säkerställa att anslutningen fungerar korrekt. Lägg märke till meddelandet "Connection to lightning node successful" högst upp på skärmen. Detta bekräftar att allt fungerar som förväntat.


![image](assets/en/38.webp)


Steg 4: Klicka på "Spara" och din butik är nu ansluten till en Lightning-nod av Alby.


![image](assets/en/39.webp)


**!Obs!**


Lita aldrig på ett förvaringsinstitut Lightning-lösning med mer värde än du är villig att förlora.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig:



- Så här ansluter du en intern eller extern Lightning-nod
- Innehållet i och funktionen hos olika blixtrelaterade plattor i Dashboard
- Så här konfigurerar du Lightning Wallet med hjälp av Voltage Surge eller Alby


### Kunskapsbedömning Praktisk genomgång


Beskriv några av de olika alternativen för att ansluta en Lightning Wallet till din butik.


# BTCPay-server Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Översikt över instrumentpanelen


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server är ett modulärt programvarupaket. Det finns dock standarder som varje BTCPay Server måste följa, och dessa standarder kommer att styra interaktionen mellan administratören och användarna. Vi börjar med instrumentpanelen. Huvudingångspunkten för varje BTCPay Server efter inloggning. Instrumentpanelen ger en översikt över din butiks prestanda, Wallet:s aktuella saldo och transaktionerna från de senaste 7 dagarna. Eftersom det är en modulär vy kan plugins använda den här vyn till sin fördel och skapa sina brickor på instrumentpanelen. För den här kursen kommer vi bara att diskutera standardplugins och appar, tillsammans med deras respektive vyer, i hela BTCPay Server.


### Instrumentpanelens plattor


I huvudvyn på BTCPay Server-instrumentpanelen finns ett par standardplattor tillgängliga. Dessa plattor är utformade för att butiksägaren eller administratören snabbt ska kunna hantera sin butik i en översikt.



- Wallet balans
- Transaktionsaktivitet
- Lightning Balance (om Lightning är aktiverat i butiken)
- Lightning Services (om Lightning är aktiverat i butiken)
- Nyligen genomförda transaktioner.
- Senaste fakturorna
- Nuvarande aktiva Crowdfundings
- Butiksresultat / bästsäljande artiklar.


### Wallet balans


Wallet:s balansplatta ger en snabb översikt över din Wallet:s medel och prestanda. Det kan visas i antingen BTC eller Fiat-valuta i en vecko-, månads- eller årsgraf.


![image](assets/en/40.webp)


### Transaktionsaktivitet


Bredvid rutan Wallet Saldo visar BTCPay Server en snabb översikt över väntande utbetalningar, antalet transaktioner under de senaste 7 dagarna och om din butik har utfärdat några återbetalningar. Om du klickar på knappen Hantera kommer du till hanteringen av väntande utbetalningar (läs mer om utbetalningar i kapitlet BTCPay Server - Betalningar).


![image](assets/en/41.webp)


### Balans mellan blixtar


Detta syns endast när Lightning är aktiverat.


När administratören har tillåtit Lightning Network-åtkomst har BTCPay Server-instrumentpanelen nu en ny kakelplatta med din Lightning-nodinformation. Hur mycket BTC som finns i kanaler, hur detta balanseras lokalt eller på distans (inkommande eller utgående likviditet), om kanaler stängs eller öppnas och hur mycket Bitcoin som hålls On-Chain på Lightning-noden.


![image](assets/en/42.webp)


### Blixttjänster


Detta syns bara när blixten är aktiv.


Förutom att se ditt Lightning-saldo på BTCPay Server-instrumentpanelen kommer administratörer också att se brickan för Lightning Services. Här kan administratörer hitta snabbknappar för verktyg som de använder för att hantera sin Lightning-nod; till exempel är Ride the Lightning ett av standardverktygen med BTCPay Server för Lightning-nodhantering.


![image](assets/en/43.webp)


### Nyligen genomförda transaktioner


Kaklet Recent Transactions visar din butiks senaste transaktioner. Med ett klick kan administratören för BTCPay Server-instansen nu se den senaste transaktionen och se om den behöver uppmärksammas.


![image](assets/en/44.webp)


### Senaste fakturorna


Kakelplattan Recent Invoices visar de 6 senaste fakturorna som genererats av din BTCPay-server, inklusive status och Invoice-belopp. Kakeln innehåller också en "Visa alla"-knapp för att enkelt få tillgång till hela Invoice-översikten.


![image](assets/en/45.webp)


### Försäljningsställen och crowdfundings


Eftersom BTCPay Server levererar en uppsättning standardplugins eller appar är Point Of Sale och Crowdfund de två viktigaste pluginsna i BTCPay Server. Med varje butik och Wallet kan en BTCPay Server-användare generate så många försäljningsställen eller Crowdfunds som de tycker passar. Var och en kommer att skapa en ny instrumentpanelplatta som visar plugin-programmens prestanda.


![image](assets/en/46.webp)


Lägg märke till den lilla skillnaden mellan en Point of Sale- och Crowdfund-kakelplatta. Administratören ser de mest sålda artiklarna i Point of Sales-rutan. I Crowdfund-rutan blir detta Top Perks. Båda plattorna har snabbknappar för att hantera respektive app och visa de senaste fakturorna som skapats av toppartiklar eller toppförmåner.


![image](assets/en/47.webp)


**!?Note!?**


Saldografer och senaste transaktioner är endast tillgängliga för betalningsmetoderna On-Chain. Information om saldon och transaktioner för Lightning Network finns på att-göra-listan. Från och med BTCPay Server Version 1.6.0 finns grundläggande Lightning Network-saldon tillgängliga.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig följande:



- Den grundläggande layouten med brickor på huvudlandningssidan kallas Dashboard.
- En grundläggande förståelse för innehållet i varje kakelplatta.


### Granskning av kunskapsbedömning


Lista så många brickor från minnet som du kan från Dashboard.


## BTCPay Server - Butiksinställningar


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


Inom programvaran BTCPay Server känner vi till två typer av inställningar. BTCPay Server Butiksspecifika inställningar, inställningsknappen som finns i den vänstra menyraden under Instrumentpanelen, och BTCPay Server-inställningar, som finns längst ner i menyraden, precis ovanför Konto. De serverspecifika inställningarna för BTCPay Server kan endast ses av serveradministratörer.


Butiksinställningarna består av många flikar för att kategorisera varje uppsättning inställningar.



- Allmänt
- Priser
- Utseende på kassan
- Åtkomsttokens
- Användare
- Roller
- Webhooks
- Utbetalningsprocessorer
- E-postmeddelanden
- Formulär


### Allmänt


På fliken Allmänna inställningar anger butiksägare standardvärden för varumärke och betalning. Vid den första installationen av butiken angavs ett butiksnamn; detta kommer att återspeglas i de allmänna inställningarna under Butiksnamn. Här kan butiksägaren också ställa in sin webbplats så att den matchar varumärket och ett butiks-ID som administratören kan känna igen i databasen.


#### Varumärkesprofilering


Eftersom BTCPay Server är FOSS kan en butiksägare göra anpassad branding för att matcha sin butik. Ställ in varumärkesfärgen, lagra ditt varumärkes logotyper och lägg till anpassad CSS för offentliga / kundinriktade sidor (fakturor, betalningsförfrågningar, dra betalningar)


#### Betalning


I betalningsinställningarna kan butiksägare ange butikens standardvaluta (antingen Bitcoin eller valfri fiatvaluta).


#### Tillåt vem som helst att skapa fakturor


Den här inställningen är avsedd för utvecklare eller byggare ovanpå BTCPay Server. När den här inställningen är aktiverad för din butik tillåter den omvärlden att skapa fakturor på din BTCPay Server-instans.


#### Lägg till extra avgift (nätverksavgift) på fakturor


En funktion inom BTCPay för att skydda handlare från Dust-attacker eller kunder från att ådra sig en hög kostnad i avgifter senare när handlaren behöver flytta en stor mängd Bitcoin på en gång. Till exempel skapade kunden en Invoice för 20 $ och betalade den delvis genom att betala 1 $ 20 gånger tills Invoice var helt betald. Handlaren har nu en större transaktion, vilket ökar Mining-kostnaden om handlaren bestämmer sig för att flytta dessa medel senare. Som standard tillämpar BTCPay en extra nätverkskostnad på det totala Invoice-beloppet för att täcka den kostnaden för handlaren när Invoice betalas i flera transaktioner. BTCPay erbjuder flera alternativ för att anpassa den här skyddsfunktionen. Du kan tillämpa en nätverksavgift:



- Endast om kunden gör mer än en betalning för Invoice (I exemplet ovan, om kunden skapade en Invoice för 20\$ och betalade 1\$, är den totala betalningen för Invoice nu 19\$ + nätverksavgiften. Nätverksavgiften tillkommer efter den första betalningen)
- På varje betalning (inklusive den första betalningen, i vårt exempel blir summan 20 USD + nätverksavgift direkt, även på den första betalningen)
- Never add network fee (avaktiverar nätverksavgiften helt och hållet)


Det skyddar visserligen mot Dust-transaktioner, men kan också ge en negativ bild av företaget om det inte kommuniceras på rätt sätt. Kunderna kanske har ytterligare frågor och tror att du tar ut för mycket i avgift.


#### Invoice förfaller om inte hela beloppet har betalats efter?


Invoice-timern är inställd på 15 minuter som standard. Timern fungerar som en skyddsmekanism mot volatilitet, eftersom den låser Bitcoin-beloppet enligt Bitcoin-till-fiat Exchange-priserna. Om kunden inte betalar Invoice inom den definierade perioden anses Invoice ha löpt ut. Invoice anses vara "betald" så snart transaktionen är synlig på Blockchain (med noll bekräftelser) och är "slutförd" när den når det antal bekräftelser som handlaren har definierat (vanligtvis 1-6). Timern är anpassningsbar i minuter.


#### Betrakta Invoice som betald även om det betalda beloppet är X% lägre än förväntat?


När en kund använder en Exchange Wallet för att betala direkt för en Invoice tar Exchange ut en liten avgift. Detta innebär att en sådan Invoice inte anses vara helt färdigställd. Invoice markeras som "delvis betald". Du kan ställa in procentsatsen här om en handlare vill acceptera underbetalda fakturor.


### Priser


I BTCPay Server, när en Invoice genereras, behöver den alltid det mest uppdaterade och korrekta Bitcoin-till-fiat-priset. När en ny butik skapas i BTCPay Server ombeds administratörerna att ange vilken priskälla de föredrar. När butiken har skapats kan butiksägarna när som helst ändra priskällan på den här fliken.


#### Avancerad skriptning av rate-regler


Används främst av power users. Om den är aktiverad kan butiksägare skapa skript kring prisbeteende och hur de ska ta betalt av sina kunder.


#### Testning


En snabb testplats för dina önskade valutapar. Den här funktionen innehåller också möjligheten att kontrollera standardvalutapar via en REST-fråga.


### Utseende på kassan


Fliken Checkout Appearance börjar med Invoice-specifika inställningar och en standardbetalningsmetod och aktiverar specifika betalningsmetoder när de angivna kraven är uppfyllda.


#### Invoice inställningar


Standardbetalningsmetoder. BTCPay-servern erbjuder i sin standardkonfiguration tre alternativ.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain & Blixt)


Vi kan ställa in parametrar för vår butik, där en kund endast kommer att interagera med Lightning när priset är mindre än X belopp, och vice versa för On-Chain-transaktioner, när X är större än Y, alltid presentera betalningsalternativet On-Chain.


![image](assets/en/48.webp)


#### Checka ut


Från och med BTCPay Server release 1.7 introducerades en ny Checkout Interface, Checkout V2. Sedan version 1.9 standardiserades kan administratörer och butiksägare fortfarande ställa in kassan till den tidigare versionen. Genom att använda växlingen "Använd den klassiska kassan" kan en butiksägare återställa butiken till sin tidigare kassaupplevelse. BTCPay Server har också en utvald uppsättning förinställningar för onlinehandel eller en butiksupplevelse.


![image](assets/en/49.webp)


När en kund interagerar med butiken och genererar en Invoice finns det en utgångstid för Invoice. Som standard ställer BTCPay Server in detta på 5 minuter, och administratörer kan justera det efter eget önskemål. Kassasidan kan anpassas ytterligare genom att kontrollera följande parametrar:



- Fira betalningen genom att visa konfetti
- Visa butikshuvudet (namn och logotyp)
- Visa knappen "Betala i Wallet"
- Unify On-Chain och off-chain betalningar URL/QRs
- Visa belopp för blixtbetalningar i Satoshis
- Automatisk detektering av språk i kassan


![image](assets/en/50.webp)


När Autodetektera språk inte är inställt kommer BTCPay Server som standard att visa engelska. En butiksägare kan ändra denna standard till det språk han eller hon föredrar.


![image](assets/en/51.webp)


Klicka på rullgardinsmenyn så kan butiksägare ange en anpassad HTML-titel som ska visas på kassasidan.


![image](assets/en/52.webp)


För att säkerställa att kunderna känner till sin betalningsmetod kan en butiksägare uttryckligen ställa in sin kassa så att användarna alltid måste välja önskad betalningsmetod. När Invoice har betalats tillåter BTCPay Server kunden att återvända till webbshoppen. Butiksägare kan ställa in att denna omdirigering ska tillämpas automatiskt efter att kunden har betalat.


![image](assets/en/53.webp)


#### Offentligt kvitto


I inställningarna för offentliga kvitton kan butiksägaren göra kvittosidorna offentliga och visa betalningslistan på kvittosidan och QR-koden så att kunden enkelt kan komma åt den.


![image](assets/en/54.webp)


### Åtkomsttokens


Access-tokens används för att koppla ihop med vissa e-handelsintegrationer eller specialbyggda integrationer.


![image](assets/en/55.webp)


### Användare


Butiksanvändare är där butiksägaren kan hantera sina anställda, deras konton och åtkomst till butiken. När personalen har skapat sina konton kan butiksägaren lägga till specifika användare i butiken som gästanvändare eller ägare. För att ytterligare definiera personalens roll, se nästa avsnitt om "BTCPay Server Butiksinställningar - Roller"


![image](assets/en/56.webp)


### Roller


En butiksägare kanske inte tycker att användarens standardroller är tillräckligt viktiga. I inställningarna för anpassade roller kan en butiksägare definiera de exakta behoven för varje roll i sin verksamhet.


(1) För att skapa en ny roll klickar du på knappen "+ Lägg till roll".


![image](assets/en/57.webp)


(2) Ange ett rollnamn, t.ex. "Kassörska".


![image](assets/en/58.webp)


(3) Konfigurera de individuella behörigheterna för rollen.



- Modifiera dina butiker.
- Hantera Exchange-konton som är kopplade till dina butiker.
  - Visa Exchange-konton som är kopplade till dina butiker.
- Hantera dina betalningar.
- Skapa dragbetalningar.
  - Skapa icke-godkända pull-betalningar.
- Ändra fakturor.
  - Visa fakturor.
  - Skapa en Invoice.
  - Skapa fakturor från de blixtnoder som är kopplade till dina butiker.
- Visa dina butiker.
  - Visa fakturor.
  - Se dina betalningsansökningar.
  - Ändra butikernas webhooks.
- Ändra dina betalningsförfrågningar.
  - Se dina betalningsansökningar.
- Använd de blixtnoder som är kopplade till dina butiker.
  - Visa de blixtfakturor som är kopplade till dina butiker.
  - Skapa fakturor från de blixtnoder som är kopplade till dina butiker.
- Sätt in pengar på Exchange-konton som är kopplade till dina butiker.
- Ta ut pengar från Exchange-konton till din butik.
- Handla med pengar på din butiks Exchange-konton.


När rollen skapas är namnet fast och kan inte ändras efter att den har varit i redigeringsläge.


![image](assets/en/59.webp)


### Webhooks


Inom BTCPay Server är det ganska enkelt att skapa en ny "Webhook". I BTCPay Server Store settings - Webhooks-fliken kan en butiksägare enkelt skapa en ny webhook genom att klicka på "+ Create Webhook". Webhooks gör det möjligt för BTCPay Server att skicka HTTP-händelser relaterade till din butik till andra servrar eller e-handelsintegrationer.


![image](assets/en/60.webp)


Du är nu i vyn för att skapa en Webhook. Se till att du känner till din nyttolast-URL och klistra in den i din BTCPay-server. Medan du klistrade in URL: n för nyttolasten, under den visar webhook-hemligheten. Kopiera webhook-hemligheten och ange den på slutpunkten. När allt har ställts in kan du växla i BTCPay Server till "Automatisk omleverans" BTCPay Server kommer att försöka omleverera en misslyckad leverans efter 10 sekunder, 1 minut och upp till 6 gånger efter 10 minuter. Du kan växla mellan varje händelse eller ange händelserna för dina behov. Se till att aktivera webhook och tryck på knappen "Add webhook" för att spara den.


![image](assets/en/61.webp)


Webhooks är inte avsedda att vara kompatibla med Bitpay API. Det finns två separata IPN:er (i BitPay-termer: "Instant Payment Notifications") i BTCPay Server.



- Webhookp
- Meddelanden


Använd endast Notification URL när du skapar fakturor via Bitpay API.


### Utbetalningsprocessorer


Utbetalningsprocessorer arbetar tillsammans med konceptet Utbetalningar i BTCPay Server. En utbetalningsaggregator för att samla flera transaktioner och skicka dem på en gång. Med utbetalningsprocessorer kan en butiksägare automatisera de batchade utbetalningarna. BTCPay Server erbjuder två metoder för automatiserade utbetalningar: On-Chain och off-chain (LN).


Butiksägaren kan klicka på och konfigurera båda utbetalningsprocessorerna separat. En butiksägare kanske bara vill köra On-Chain-processorn en gång var X:e timme, medan off-chain-processorn kanske körs med några minuters mellanrum. För On-Chain kan du också ställa in ett mål för vilket block det ska inkluderas. Som standard är detta inställt på 1 (eller nästa tillgängliga block). Observera att inställningen av off-chain-utbetalningsprocessorn endast har intervalltimern och inget blockmål. Lightning Network-betalningar är omedelbara.


![image](assets/en/62.webp)

![image](assets/en/63.webp)


Butiksägare kan endast konfigurera On-Chain-processorn om de har en Hot Wallet ansluten till sin butik.


![image](assets/en/64.webp)


När du har konfigurerat en utbetalningsprocessor kan du snabbt ta bort eller ändra den genom att gå tillbaka till fliken Utbetalningsprocessor i BTCPay Server Store-inställningarna.


**Anmärkning**


Utbetalningsprocessor On-Chain - Utbetalningsprocessorn On-Chain kan endast fungera i en butik som är konfigurerad med en Hot Wallet ansluten. Om ingen Hot Wallet är ansluten har BTCPay-servern inte Wallet-nycklarna och kommer inte att kunna behandla utbetalningar automatiskt.


### E-postmeddelanden


BTCPay Server kan använda e-postmeddelanden för aviseringar eller, när det är korrekt inställt, för att återställa konton som skapats på instansen. Som standard skickar BTCPay Server inte ett e-postmeddelande när t.ex. lösenordet förloras.


![image](assets/en/65.webp)


Innan en butiksägare kan ställa in e-postregler för att utlösa specifika händelser i sin butik måste de först ställa in några grundläggande e-postinställningar. BTCPay Server kräver dessa inställningar för att skicka e-postmeddelanden för händelser relaterade till din butik eller för återställning av lösenord.


BTCPay Server gjorde det enklare att fylla i denna information genom att använda alternativet "Snabb ifyllning":



- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid


Genom att använda alternativet snabb ifyllning kommer BTCPay Server att fylla i fälten för SMTP-servern och porten. Nu behöver butiksägaren bara fylla i sina referenser, inklusive en e-post Address, inloggning (som vanligtvis är lika med din e-post Address) och deras lösenord. Det avancerade alternativet i e-postinställningarna för BTCPay Server är att inaktivera säkerhetskontroller för TLS-certifikat; som standard är detta aktiverat.


![image](assets/en/66.webp)


Med e-postregler kan en butiksägare ställa in specifika händelser så att de utlöser e-postmeddelanden till specifika e-postadresser.



- Invoice Skapad
- Invoice Erhållen betalning
- Invoice Bearbetning
- Invoice Utgått
- Invoice avgjord
- Invoice Ogiltig
- Invoice Betalning reglerad


Om kunden har angett ett e-postmeddelande Address kan dessa utlösare också skicka informationen till kunden. Butiksägare kan förifylla ämnesraden för att klargöra varför det här e-postmeddelandet inträffade och vad som utlöste det.


![image](assets/en/67.webp)


### Formulär


Eftersom BTCPay Server inte samlar in några data kanske en butiksägare vill lägga till ett anpassat formulär i sin kassaupplevelse; på så sätt kan butiksägaren samla in ytterligare information från sin kund. BTCPay Server Form Builder består av två delar: en visuell och en mer avancerad kodvy av formulären.


När du skapar ett nytt formulär öppnar BTCPay Server ett nytt fönster där du får grundläggande information om vad du vill att ditt nya formulär ska fråga om. Först måste butiksägaren ange ett tydligt namn för det nya formuläret; detta namn kan inte ändras efter att det har ställts in.


![image](assets/en/68.webp)


När butiksägaren har gett formuläret ett namn kan du också vrida omkopplaren för "Tillåt formulär för allmän användning" till ON, så att Green tänds. Detta säkerställer att formuläret används på alla platser som vänder sig till kunder. Om en butiksägare till exempel skapar en separat Invoice som inte finns på försäljningsstället, kanske de ändå vill samla in information från kunden. Den här växlingen gör det möjligt att samla in den informationen.


![image](assets/en/69.webp)


Varje formulär börjar med minst 1 nytt formulärfält. En butiksägare kan välja vilken typ av fält det ska vara.



- Text
- Antal
- Lösenord
- E-post
- URL
- Telefonnummer
- Datum
- Dolda fält
- Fieldset
- Ett textområde för öppna kommentarer.
- Väljare för alternativ


Varje typ kommer med sina parametrar att fylla i. Butiksägaren kan ställa in dem efter eget tycke och smak. Under det första skapade fältet kan butiksägaren lägga till nya fält i formuläret.


![image](assets/en/70.webp)


#### Avancerade anpassade formulär


BTCPay Server låter dig också bygga formulär i kod. JSON, i synnerhet. Istället för att titta på redigeraren kan butiksägare klicka på CODE-knappen precis bredvid redigeraren och komma in i koden för sina formulär. I en fältdefinition kan endast följande fält ställas in; värdena för fälten lagras i metadata för Invoice:


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

Fältnamnet representerar det JSON-egenskapsnamn som lagrar det användartillhandahållna värdet i Invoice:s metadata. Vissa välkända namn kan tolkas och modifieras för att justera Invoice:s inställningar.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Du kan förfylla fälten i en Invoice automatiskt genom att lägga till frågesträngar i formulärets URL, t.ex. "?your_field=value".


Här är några exempel på användningsområden för denna funktion:



- Hjälp med användarens inmatning: Förhandsifyll fält med känd kundinformation för att göra det enklare för dem att fylla i formuläret. Om du till exempel redan känner till en kunds e-postadress Address kan du förifylla e-postfältet för att spara tid åt dem.
- Personalisering: Anpassa formuläret baserat på kundens preferenser eller segmentering. Om du till exempel har olika kundnivåer kan du förfylla formuläret med relevanta uppgifter, till exempel deras medlemsnivå eller specifika erbjudanden.
- Spårning: Spåra källan till kundbesök med hjälp av dolda fält och förifyllda värden. Du kan t.ex. skapa länkar med förifyllda utm_media-värden för varje marknadsföringskanal (t.ex. Twitter, Facebook, e-post). Detta hjälper dig att analysera effektiviteten i dina marknadsföringsinsatser.
- A/B-testning: Fyll i fälten med olika värden för att testa olika formulärversioner, så att du kan optimera användarupplevelsen och konverteringsgraden.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig följande:



- Layout och funktioner för flikarna i butiksinställningarna
- En mängd olika alternativ för att finjustera hanteringen av underliggande Exchange-priser, delbetalningar, små underbetalningar med mera.
- Anpassa utseendet på kassan, inklusive prisberoende huvudkedja vs. Lightning-aktivering på fakturor.
- Hantera nivåer för butiksåtkomst och behörigheter för olika roller.
- Konfigurera automatiserade e-postmeddelanden och deras triggers
- Skapa anpassade formulär för att samla in ytterligare kundinformation i kassan.


### Kunskapsbedömningar


#### KA granskning


Vad är skillnaden mellan Store Settings och Server Settings?


#### KA Hypotetisk


Beskriv några alternativ som du kan välja i Checkout Appearance > Invoice Settings, och varför.


## BTCPay Server - Serverinställningar


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server består av två olika inställningsvyer. Den ena är avsedd för butiksinställningar och den andra för serverinställningar. Den senare är endast tillgänglig för serveradministratörer och inte för butiksägare. Serveradministratörer kan lägga till användare, skapa anpassade roller, konfigurera e-postservern, ställa in policyer, köra underhållsuppgifter, kontrollera alla tjänster som är kopplade till BTCPay Server, ladda upp filer till servern eller kontrollera loggar.


### Användare


Som nämndes i föregående avsnitt kan serveradministratörer bjuda in användare till sin server genom att lägga till dem på fliken Användare.


### Anpassade roller för hela servern


BTCPay Server har två typer av anpassade roller: butiksspecifika anpassade roller och serveromfattande anpassade roller i BTCPay Server-inställningarna. Båda har en liknande uppsättning behörigheter; men om den ställs in via fliken BTCpay Serverinställningar - Roller kommer den tillämpade rollen att vara serveromfattande och gälla för flera butiker. Lägg märke till en "Server-wide"-tagg för de anpassade rollerna i Serverinställningar.


![image](assets/en/71.webp)


### Anpassade roller för hela servern


Behörighetsuppsättning för anpassade roller för hela servern;



- Modifiera dina butiker.
- Hantera Exchange-konton som är kopplade till dina butiker.
  - Visa Exchange-konton som är kopplade till dina butiker.
- Hantera dina betalningar.
- Skapa dragbetalningar.
  - Skapa icke-godkända pull-betalningar.
- Ändra fakturor.
  - Visa fakturor.
  - Skapa en Invoice.
  - Skapa fakturor från de blixtnoder som är kopplade till dina butiker.
- Visa dina butiker.
  - Visa fakturor.
  - Se dina betalningsansökningar.
  - Ändra butikernas webhooks.
- Ändra dina betalningsförfrågningar.
  - Se dina betalningsansökningar.
- Använd de blixtnoder som är kopplade till dina butiker.
  - Visa de blixtfakturor som är kopplade till dina butiker.
  - Skapa fakturor från de blixtnoder som är kopplade till dina butiker.
- Sätt in pengar på Exchange-konton som är kopplade till dina butiker.
- Ta ut pengar från Exchange-konton till din butik.
- Handla med pengar på din butiks Exchange-konton.


**!?Note!?**


När rollen skapas är namnet fast och kan inte ändras efter att den har varit i redigeringsläge.


### E-post


De serveromfattande e-postinställningarna liknar dem i de butiksspecifika e-postinställningarna. Den här inställningen hanterar dock inte bara utlösare för butiker eller administratörsloggar, utan även utlösare för andra händelser. Denna e-postinställning gör också lösenordsåterställning tillgänglig på BTCPay Server vid inloggning. Det fungerar på samma sätt som de butiksspecifika inställningarna; administratörer kan snabbt fylla i sina e-postparametrar och ange sina e-postuppgifter, så att servern kan skicka e-post.


![image](assets/en/72.webp)


### Policys


Policyadministratörer för BTCPay Server kan ange olika inställningar för ämnen som inställningar för befintliga användare, inställningar för nya användare, inställningar för meddelanden och inställningar för underhåll. Dessa är avsedda för att registrera nya användare som administratörer eller vanliga användare, eller för att dölja BTCPay Server från sökmotorer genom att lägga till den i serverhuvudet.


![image](assets/en/73.webp)


#### Befintlig användare Inställningar


De alternativ som finns här är skilda från anpassade roller. Dessa ytterligare behörigheter kan göra en butik eller dess ägare sårbar för attacker. Policyer som kan läggas till för befintliga användare:



- Tillåt icke-administratörer att använda den interna Lightning-noden i sina butiker.
  - Detta skulle göra det möjligt för butiksägare att använda serveradministratörens Lightning-nod och därmed hans medel! Se upp, detta är inte en lösning för att ge tillgång till Lightning.
- Tillåt icke-administratörer att skapa Hot-plånböcker för sina butiker.
  - Detta skulle göra det möjligt för alla med ett konto på din BTCPay Server-instans att skapa Hot-plånböcker och lagra deras återvinning seed på administratörens server. Detta kan göra administratören ansvarig för att hålla tredje parts medel!
- Tillåt icke-administratörer att importera Hot-plånböcker för sina butiker.
  - I likhet med det tidigare ämnet om att skapa Hot-plånböcker tillåter denna policy import av en Hot Wallet, med samma faror som nämns i avsnittet om att skapa Hot-plånböcker.


![image](assets/en/74.webp)


#### Nya användarinställningar


Vi kan ställa in några viktiga inställningar för att hantera nya användare som kommer till servern. Vi kan ställa in ett bekräftelsemeddelande för nya registreringar, inaktivera skapande av nya användare via inloggningsskärmen och begränsa icke-administratörers åtkomst till skapande av användare via API.



- Kräv ett bekräftelsemeddelande för registrering.
  - Serveradministratören måste ha installerat en e-postserver.
- Inaktivera registrering av nya användare på servern
- Inaktivera åtkomst för icke-administratörer till API-slutpunkten för skapande av användare.


Som standard har BTCPay Server aktiverat "Inaktivera registrering av nya användare på servern" och stängt av icke-administratörers åtkomst till API-slutpunkten för skapande av användare. Detta är av säkerhetsskäl, så att slumpmässiga personer som snubblar över din BTCPay-inloggning inte kan skapa konton.


![image](assets/en/75.webp)


#### Inställningar för aviseringar


![image](assets/en/76.webp)


#### Inställningar för underhåll


BTCPay Server är ett Open Source-projekt som lever på GitHub. När BTCPay Server släpper en ny version av programvaran kan administratörer få ett meddelande om att en ny version finns tillgänglig. Administratörer kanske också vill undvika att sökmotorer (t.ex. Google, Yahoo och DuckDuckGo) indexerar BTCPay Server-domänen. Eftersom BTCPay Server är FOSS kan utvecklare över hela världen vilja skapa nya funktioner. BTCPay Server har en experimentell funktion som, när den är aktiverad, gör det möjligt för administratörer att använda funktioner som inte är avsedda för produktion utan snarare för teständamål.



- Kontrollera utgåvor på GitHub och meddela när en ny BTCPay Server-version är tillgänglig.
- Avråda sökmotorer från att indexera denna webbplats
- Aktivera experimentella funktioner.


![image](assets/en/77.webp)


#### Plugins


BTCPay Server kan lägga till plugins och utöka sin funktionsuppsättning. Plugins laddas som standard från BTCPay Server plugin-builder repository. En administratör kan dock välja att se plugins i ett Pre-release-tillstånd, och om plugin-utvecklaren tillåter det kan serveradministratören nu installera betaversioner av plugins.


![image](assets/en/78.webp)


##### Inställningar för anpassning


En standarddistribution av BTCPay Server kommer att vara tillgänglig via den domän som ställdes in under installationen. En serveradministratör kan dock ändra rotdomänen och visa en av de skapade apparna från en specifik butik. Serveradministratören kan också mappa specifika domäner till specifika appar.



- Visa appen på webbplatsens rot
  - Visar en lista över möjliga appar som kan visas på rotdomänen.


![image](assets/en/79.webp)



- Mappa specifika domäner till specifika appar.
  - När du klickar på för att konfigurera en specifik domän för specifika appar kan administratören konfigurera så många domäner som pekar på specifika appar som behövs.


![image](assets/en/80.webp)


#### Blockutforskare


BTCPay Server kommer som standard med Mempool.space som sin Block explorer för transaktioner. När BTCPay Server genererar en ny Invoice och en transaktion är knuten till den kan butiksägaren klicka för att öppna transaktionen. BTCPay Server kommer som standard att peka mot Mempool.space som Block explorer, men en serveradministratör kan ändra detta till önskat alternativ.


![image](assets/en/81.webp)


### Tjänster


Fliken "Inställningar för BTCPay Server: Tjänster" är en översikt över de komponenter som din BTCPay-server använder. De tjänster som din BTCPay Server exponerar kan variera beroende på distributionsmetod.


En BTCPay-serveradministratör kan klicka på "Se information" bakom varje tjänst för att öppna den och ställa in specifika inställningar.


![image](assets/en/82.webp)


#### LND (gRPC)


BTCPay exponerar LND:s GRPC-tjänst för extern konsumtion; du hittar anslutningsinformation i den här specifika inställningsmenyn; kompatibla plånböcker listas här. BTCPay Server tillhandahåller också en QR-kod för anslutning, som kan skannas och tillämpas i en mobil Wallet.


Serveradministratörer kan öppna fler detaljer för att se.



- Information om värden
- Användning av SSL
- Macaron
- AdminMacaroon
- FakturaMacaroon
- ReadonlyMacaroon
- GRPC SSL-chiffersvit (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay exponerar LND:s REST-tjänst för extern konsumtion; du hittar anslutningsinformation här; kompatibla plånböcker listas här. Bland de kompatibla plånböckerna finns Joule, Alby och ZeusLN. BTCPay Server tillhandahåller en QR-kod för anslutning, som kan skannas och användas i en kompatibel Wallet.



- REST URI
- Macaron
- AdminMacaroon
- FakturaMacaroon
- ReadonlyMacaroon


#### LND seed Backup


LND seed-säkerhetskopian är användbar för att återställa medel från din LND Wallet i händelse av serverkorruption. Eftersom Lightning-noden är en Hot-Wallet kan du hitta den konfidentiella seed-informationen på den här sidan.


LND dokumenterar återhämtningsprocessen. Se https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md för dokumentation.


#### Ride The Lightning


Ride the Lightning är ett Lightning-nodhanteringsverktyg byggt som programvara med öppen källkod. BTCPay Server använder RTL som komponent för hantering av Lightning-noder i sin stack. BTCPay Server-administratörer kan nå RTL via Serverinställningar - fliken Tjänster eller genom att klicka på Lightning Wallet.


#### Full node P2P


Serveradministratörer kanske vill ansluta sin Bitcoin-nod till en mobil Wallet. På den här sidan finns information om hur du fjärransluter till din Full node via P2P-protokollet. När den här kursen skrivs listar BTCPay Server Blockstream Green- och Wasabi-plånböcker som kompatibla plånböcker. BTCPay Server tillhandahåller en QR-kod för anslutning, som kan skannas och användas i en kompatibel Wallet.


#### Full node RPC


På den här sidan finns information om hur du fjärransluter till din Full node via RPC-protokollet.


#### SSH


SSH används för underhållsändamål. BTCPay Server visar det första anslutningskommandot för att nå din server och offentliga SSH-nycklar som är auktoriserade att ansluta till din server. Serveradministratörer kanske vill inaktivera SSH-ändringar via BTCPay Server-gränssnittet.


#### Dynamisk DNS


Dynamisk DNS gör att du kan ha ett stabilt DNS-namn som pekar på din server, även om din IP Address ändras regelbundet. Detta rekommenderas om du är värd för BTCPay Server hemma och vill ha en tydlig domän för att komma åt din server.


Observera att du måste konfigurera din NAT- och BTCPay Server-installation korrekt för att få HTTPS-certifikatet.


### Tema


BTCPay Server levereras som standard med två teman: Ljusa och mörka lägen. Dessa kan bytas genom att klicka på Konto längst ned till vänster och växla mellan mörkt tema och ljust tema. BTCPay Server-administratörer kan lägga till sitt eget tema genom att tillhandahålla ett anpassat CSS-tema.


Administratörer kan utöka Light/Dark-temat genom att lägga till sin egen anpassade CSS eller ställa in sitt anpassade tema som en fullständig anpassning.


![image](assets/en/83.webp)


#### Servervarumärke


Serveradministratörer kan ändra BTCPay Server-varumärket genom att ställa in ett varumärke för hela servern för ditt företag. Eftersom BTCPay Server är FOSS kan serveradministratörer vitmärka programvaran och anpassa utseendet så att det passar deras verksamhet.


![image](assets/en/84.webp)


### Underhåll


Som serveradministratör förväntar sig dina användare att du tar väl hand om servern. På fliken Underhåll i BTCPay Server kan administratören utföra en del viktigt underhåll. Ställ in domännamnet till BTCPay Server-instansen, starta om eller städa upp servern. Möjligen viktigast av allt, kör uppdateringar.


BTCPay Server är ett projekt med öppen källkod och uppdateras ofta. Varje ny version meddelas antingen via dina BTCPay Server-meddelanden eller på de officiella kanalerna som BTCPay Server kommunicerar via.


![image](assets/en/85.webp)


#### Domännamn


När BTCPay Server har konfigurerats kanske en administratör vill byta bort sin ursprungliga domän. På fliken Underhåll kan administratören ändra domänen. Efter att ha klickat på bekräfta och ställt in rätt DNS-poster på domänen uppdateras och startas BTCPay Server om för att återgå till den nya domänen.


![image](assets/en/86.webp)


#### Omstart


Starta om BTCPay Server och relaterade tjänster.


![image](assets/en/87.webp)


#### Ren


BTCPay Server körs med Docker-komponenter; med uppdateringar kan det finnas rester av Docker-bilder, temp-filer etc. Serveradministratörer kan frigöra utrymme genom att köra Clean-skriptet.


![image](assets/en/88.webp)


#### Uppdatering


Det är det viktigaste alternativet på fliken Underhåll. BTCPay Server är byggd av samhället, och därför är dess uppdateringscykler mer frekventa än de flesta programvaruprodukter. När BTCPay Server har en ny release kommer administratörer att meddelas i deras meddelandecenter. Genom att klicka på uppdateringsknappen kommer BTCPay Server att kontrollera GitHub för den senaste versionen, uppdatera servern och starta om. Innan uppdatering rekommenderas serveradministratörer alltid att läsa de utgivningsanteckningar som distribueras via de officiella kanalerna för BTCPay Server.


![image](assets/en/89.webp)


### Loggar


Att ställas inför ett problem är aldrig roligt. I det här dokumentet beskrivs det vanligaste arbetsflödet och de vanligaste stegen för att effektivt identifiera och lösa problemet, antingen på egen hand eller med hjälp från samhället.


Att identifiera problemet är avgörande.


#### Replikering av problemet


Försök först och främst att avgöra när problemet uppstår. Försök att replikera problemet. Försök att uppdatera och starta om servern för att verifiera att du kan reproducera problemet. Om det bättre beskriver ditt problem, ta en skärmdump.


##### Uppdatering av servern


Kontrollera din version av BTCPay Server om den är mycket äldre än den [senaste versionen] (https://github.com/btcpayserver/btcpayserver/releases) av BTCPay Server. Uppdatering av din server kan lösa problemet.


##### Starta om servern


Omstart av servern är ett enkelt sätt att lösa många av de vanligaste problemen med BTCPay-servern. Du kan behöva SSH till din server så att du kan starta om den.


##### Starta om en tjänst


Du kanske bara behöver starta om en viss tjänst i din BTCPay Server-distribution för vissa problem, t.ex. omstart av letsencrypt-containern för att förnya SSL-certifikatet.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Använd docker ps för att hitta namnet på en annan tjänst som du vill starta om.


#### Tittar igenom loggarna


Loggar kan ge en viktig del av informationen. I följande stycken kommer vi att beskriva hur man får logginformation för olika delar av BTCPay.


##### BTCPay-loggar


Sedan v1.0.3.8 kan du enkelt komma åt BTCPay Server-loggar från frontend. Om du är serveradministratör går du till Serverinställningar > Loggar och öppnar loggfilen. Om du inte vet vad ett visst fel i loggarna betyder kan du nämna det när du felsöker.


Om du vill ha mer detaljerade loggar och använder en Docker-distribution kan du visa loggar för specifika Docker-containrar med hjälp av kommandoraden. Se dessa [instruktioner för att ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) till en instans av BTCPay som körs på en VPS.


På nästa sida finns en allmän lista över de containernamn som används för BTCPay Server.


Kör kommandona nedan för att skriva ut loggar efter behållarnamn. Byt ut behållarnamnet för att visa andra behållarloggar.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Det finns några sätt att komma åt dina LND-loggar när du använder Docker. Logga först in som root:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Alternativt kan du snabbt skriva ut loggar genom att använda behållarens ID (endast de första unika ID-tecken behövs, t.ex. de två tecknen längst till vänster):


```bash
docker logs 'add your container ID'
```


Om du av någon anledning behöver fler stockar


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Du kommer att se något i stil med


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


För att få tillgång till okomprimerade loggar av dessa loggar, gör `cat LND.log` eller om du vill ha en annan, använd `cat LND.log.15`.


Om du vill komma åt komprimerade loggar i `.gzip` använder du `gzip -d LND.log.16.gz` (i det här fallet kommer vi åt `LND.log.16.gz`). Detta bör ge dig en ny fil, där du kan göra `cat LND.log.16`. Om ovanstående inte fungerar kan du behöva installera gzip först med `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Alternativt kan du använda detta:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Du kan också få logginformation med kommandot c-lightning CLI.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin Loggar för noder


Förutom att [titta på loggar](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) för din bitcoind-container kan du också använda något av [bitcoin-cli-kommandona](https://developer.Bitcoin.org/reference/RPC/index.html)


[(öppnar nytt fönster)](https://developer.Bitcoin.org/reference/RPC/index.html) för att få information från din Bitcoin-nod. BTCPay innehåller ett skript som gör att du enkelt kan kommunicera med din Bitcoin-nod.


I mappen btcpayserver-docker hämtar du Blockchain-informationen med hjälp av din nod:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Filer


BTCPay Server har ett lokalt filsystem som gör det möjligt att ladda upp butikstillgångar (produkter), logotyper och varumärkesprofilering direkt till servern. Serverns filsystem är endast tillgängligt för serveradministratörer; butiksägare kan ladda upp sina logotyper eller varumärken på butiksnivå.


När serveradministratören befinner sig på fliken File Storage är det möjligt att ladda upp direkt till din server eller ändra fillagringsleverantören till ett lokalt filsystem eller Azure Blob Storage.


![image](assets/en/90.webp)


![image](assets/en/91.webp)


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig följande:



- Skillnaden mellan Store- och Server-inställningar, i synnerhet när det gäller användare, roller och e-postmeddelanden
- Ange serverövergripande policyer för användning och skapande av Lightning eller Bitcoin Hot Wallet, registrering av nya användare och e-postmeddelanden.
- Hur man lägger till anpassade teman (istället för de enkla ljusa/mörka alternativen) samt skapar anpassade logotyper
- Utför enkla underhållsuppgifter för servern via det GUI som tillhandahålls
- Felsöka problem, inklusive att hämta information för någon av Docker-containrarna eller din nod
- Hantera fillagring


### Bedömning av kunskap


#### KA Konceptuell granskning


Vad är skillnaden mellan roller som tilldelas via server- och butiksinställningar, och vad beskriver en potentiell användning av det ena framför det andra?


#### KA Praktisk granskning


Beskriv några möjliga användningsfall som är aktiverade på fliken Policies.


#### KA Praktisk granskning


Beskriv några åtgärder som en administratör rutinmässigt kan göra på fliken Maintenance.


## BTCPay Server - Betalningar


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


En Invoice är ett dokument som säljaren utfärdar till en köpare för att ta emot betalning.


I BTCPay Server representerar en Invoice ett dokument som måste betalas inom ett definierat tidsintervall till en fast Exchange-ränta. Fakturor har utgångsdatum eftersom de låser Exchange-kursen inom en viss tidsram, vilket skyddar mottagaren från prisfluktuationer.


Kärnan i BTCPay Server är förmågan att fungera som ett Bitcoin Invoice-hanteringssystem. En Invoice är ett viktigt verktyg för att spåra och hantera mottagna betalningar.


Om du inte använder en inbyggd [Wallet](https://docs.btcpayserver.org/Wallet/) för att ta emot betalningar manuellt visas alla betalningar inom en butik på sidan Fakturor. Den här sidan sorterar betalningar efter datum och fungerar som en central resurs för Invoice-hantering och felsökning av betalningar.


![image](assets/en/92.webp)


### Allmänt


#### Invoice status


Tabellen nedan listar och beskriver standard Invoice-statusarna i BTCPay, tillsammans med förslag på vanliga åtgärder. Åtgärderna är bara rekommendationer. Det är upp till användarna att definiera det bästa tillvägagångssättet för deras användningsfall och verksamhet.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Invoice detaljer


Informationssidan för Invoice innehåller all information som är relaterad till en Invoice.


Invoice-information skapas automatiskt baserat på Invoice-status, Exchange-frekvens etc. Produktinformation skapas automatiskt om Invoice skapades med produktinformation, t.ex. i Point of Sale-appen.


#### Invoice filtrering


Fakturor kan filtreras via snabbfiltren som finns bredvid sökknappen eller de avancerade filtren, som kan växlas genom att klicka på länken (Hjälp) högst upp. Användare kan filtrera fakturor efter butik, order-ID, artikel-ID, status eller datum.


#### Invoice export


BTCPay Server-fakturor kan exporteras i CSV- eller JSON-format. För mer information om Invoice export och redovisning.


#### Återbetalning av en Invoice


Om du av någon anledning vill göra en återbetalning kan du enkelt skapa en återbetalning från vyn Invoice.


#### Arkivering av fakturor


Som ett resultat av att BTCPay Server inte har någon Address återanvändningsfunktion är det vanligt att se många utgångna fakturor på din butiks Invoice-sida. För att dölja dem från din vy, välj dem i listan och markera dem som arkiverade. Fakturor som har markerats som arkiverade tas inte bort. Betalning till en arkiverad Invoice kommer fortfarande att upptäckas av din BTCPay-server (paidLate-status). Du kan visa butikens arkiverade fakturor när som helst genom att välja arkiverade fakturor i rullgardinsmenyn för sökfilter.


#### Standardvaluta


Butikens standardvaluta, som ställdes in i guiden för att skapa butiken.


#### Tillåt vem som helst att skapa en Invoice


Du bör aktivera det här alternativet om du vill tillåta omvärlden att skapa fakturor i din butik. Det här alternativet är bara användbart om du använder betalningsknappen eller om du utfärdar fakturor via API eller en HTML-webbplats från tredje part. PoS-appen är förhandsauktoriserad och kräver inte att denna inställning är aktiverad för att en slumpmässig besökare ska kunna öppna din POS-butik och skapa en Invoice.


#### Lägg till en extra avgift (nätverksavgift) till Invoice



- Endast om kunden gör mer än en betalning för Invoice
- På varje betalning
- Lägg aldrig till en nätverksavgift


#### Invoice förfaller om inte hela beloppet har betalats efter ... Protokoll.


Invoice:s timer är inställd på 15 minuter som standard. Timern fungerar som en skyddsmekanism mot volatilitet, eftersom den låser kryptovalutabeloppet baserat på krypto-till-fiat-kurserna. Om kunden inte betalar Invoice inom den definierade perioden anses Invoice ha löpt ut. Invoice anses vara "betald" så snart transaktionen är synlig på Blockchain (med noll bekräftelser) och anses vara "slutförd" när den når det antal bekräftelser som handlaren har definierat (vanligtvis 1-6). Timern är anpassningsbar.


#### Betrakta Invoice som betald även om det betalda beloppet är ..% lägre än förväntat.


I en situation där en kund använder en Exchange Wallet för att betala direkt för en Invoice, tar Exchange en liten avgift. Detta innebär att en sådan Invoice inte anses vara helt färdigställd. Invoice markeras som "delvis betald" Om en handlare vill acceptera underbetalda fakturor kan du ställa in procentsatsen här


### Förfrågningar


Betalningsförfrågningar är en funktion som gör det möjligt för BTCPay-butiksägare att skapa långlivade fakturor. Pengar betalas enligt betalningsbegäran med Exchange-taxan som gäller vid betalningstillfället. Detta gör att användare kan göra betalningar när det passar dem utan att behöva förhandla eller verifiera Exchange-priser med butiksägaren vid betalningstillfället.


Användare kan betala för förfrågningar i delbetalningar. Betalningsbegäran förblir giltig tills den betalas i sin helhet eller om butiksägaren kräver en utgångstid. Adresser återanvänds aldrig. En ny Address genereras varje gång användaren klickar på betala för att skapa en Invoice för betalningsbegäran.


Butiksägare kan skriva ut betalningsförfrågningar (eller exportera Invoice-data) för bokföring och redovisning. BTCPay märker automatiskt fakturor som Betalningsförfrågningar i din butiks Invoice-lista.


#### Anpassa dina betalningsförfrågningar



- Invoice Belopp - Ange begärt betalningsbelopp
- Denominering - Visa begärt belopp i Fiat eller kryptovaluta
- Betalningskvantitet - Tillåt endast enstaka betalningar eller delbetalningar
- Expiration Time - Tillåt betalningar fram till ett visst datum eller utan förfallodag
- Beskrivning - Textredigerare, datatabeller, inbäddning av foton och videor
- Utseende - Färg och stil med CSS-teman


![image](assets/en/93.webp)


#### Skapa en betalningsbegäran


I menyn till vänster går du till Betalningsuppdrag och klickar på "Skapa betalningsuppdrag".


![image](assets/en/94.webp)


Ange namn på begäran, belopp, visad valör, associerad butik, utgångstid och beskrivning (valfritt)


Markera alternativet Tillåt betalningsmottagaren att skapa fakturor i sitt valörnummer om du vill tillåta delbetalningar.


Klicka på Save & View för att granska din betalningsbegäran.


BTCPay skapar en URL för betalningsbegäran. Dela den här URL:en för att visa din betalningsbegäran. Behöver du flera av samma begäran? Du kan duplicera betalningsbegäranden med hjälp av alternativet Clone i huvudmenyn.


![image](assets/en/95.webp)


**VARNING**


Betalningsbegäran är butiksberoende, vilket innebär att varje betalningsbegäran associeras med en butik när den skapas. Se till att ha en Wallet ansluten till din butik som betalningsbegäran tillhör.


#### Betald förfrågan


Betalningsmottagaren och uppdragsgivaren kan se status för betalningsuppdraget efter att betalningen har skickats. Statusen visas som Settled om hela betalningen har mottagits. Om endast delbetalningar har gjorts visas det återstående saldot under Amount Due.


![image](assets/en/96.webp)


#### Anpassa betalningsförfrågningar


Innehållet i beskrivningen kan redigeras med hjälp av betalningsbegärans textredigerare. Båda alternativen är tillgängliga om du vill använda ytterligare färgteman eller anpassad CSS-styling.


Icke-tekniska användare kan använda ett [bootstrap-tema] (https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Ytterligare anpassning kan göras genom att tillhandahålla ytterligare CSS-kod, som visas nedan.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Dra betalningar


Traditionellt delar en mottagare med sig av sin Bitcoin Address för att göra en Bitcoin-betalning, och avsändaren skickar senare pengar till denna Address. Ett sådant system kallas Push-betalning, eftersom avsändaren initierar betalningen medan mottagaren kanske inte är tillgänglig, och skickar betalningen till mottagaren.


Men vad sägs om att vända på rollen?


Vad händer om avsändaren, i stället för att skicka betalningen, låter mottagaren dra betalningen vid en tidpunkt som mottagaren finner lämplig? Det är detta som är konceptet med en Pull-betalning. Detta möjliggör flera nya tillämpningar, t.ex:



- En prenumerationstjänst (där abonnenten tillåter att tjänsten drar in pengar var x:e tid)
- Återbetalningar (där handlaren tillåter kunden att dra tillbaka återbetalningspengarna till sin Wallet när de anser det lämpligt)
- Tidsbaserad fakturering för frilansare (där den som anställer låter frilansaren dra pengar till sin Wallet när tiden rapporteras)
- Patronage (där patronen låter mottagaren ta ut pengar varje månad för att fortsätta stödja deras arbete)
- Automatisk försäljning (där en kund till en Exchange skulle tillåta en Exchange att dra pengar från sin Wallet för att sälja varje månad automatiskt)
- System för uttag från saldo (där en tjänst med hög volym låter användare begära uttag från sitt saldo, kan tjänsten sedan enkelt samla alla utbetalningar till många användare med fasta intervall)


### Utbetalningar


Utbetalningsfunktionen är kopplad till funktionen [Pull Payments] (https://docs.btcpayserver.org/PullPayments/). Med den här funktionen kan du skapa utbetalningar i din BTCPay. Med den här funktionen kan du behandla pull-betalningar (återbetalningar, löneutbetalningar eller uttag).


#### Exempel 1: Återbetalning


Låt oss börja med exemplet med återbetalningen. Kunden har köpt en vara i din butik, men måste tyvärr returnera den. De vill ha en återbetalning. Inom BTCPay kan du skapa en [Återbetalning] (https://docs.btcpayserver.org/Refund/) och förse kunden med länken för att göra anspråk på sina pengar. När kunden har angett sitt Address och gjort anspråk på pengarna kommer de att visas i avsnittet Utbetalningar.


Den första statusen den har är Väntar på godkännande. Butikspersonal kan kontrollera om flera väntar, och efter att ha gjort valet använder du knappen Åtgärder.


Alternativ på åtgärdsknappen



- Godkänna utvalda utbetalningar
- Godkänna och skicka utvalda utbetalningar
- Avbryt valda utbetalningar


Nästa steg är att godkänna och skicka utvalda utbetalningar, eftersom vi vill återbetala kunden. Kontrollera kundens Address, som visar beloppet och om vi vill att avgifterna ska subtraheras från återbetalningen eller inte. När du har slutfört kontrollerna är det enda återstående steget att signera transaktionen.


Kunden blir nu uppdaterad på sidan Claiming. Han kan följa transaktionen eftersom han får en länk till en Block explorer och sin transaktion. När transaktionen har bekräftats ändras dess status till "Slutförd".


#### Exempel 2: Lön


Låt oss nu gå in på löneutbetalningen, eftersom denna styrs inifrån butiken och inte enligt kundens begäran. Det underliggande konceptet är detsamma; det utnyttjar pull-betalningar. Men istället för att skapa en återbetalning kommer vi att göra en [Pull Payment] (https://docs.btcpayserver.org/PullPayments/).


Gå till fliken Pull Payments i din BTCPay-server. Klicka på knappen Skapa Pull-betalning längst upp till höger.


Nu är vi i skapandet av utbetalningen, ge den ett namn och önskat belopp i vald valuta. Fyll i beskrivningen så att den anställde vet vad det handlar om. Nästa del liknar återbetalningar. Den anställde fyller i Destination Address och det belopp han vill göra anspråk på från den här utbetalningen. Han kan besluta att göra det till två separata anspråk, till olika adresser, eller till och med delvis anspråk över blixtnedslag.


Om det finns flera väntande utbetalningar kan du samla dessa för att signeras och skickas ut. När utbetalningarna har signerats flyttas de till fliken Pågående och visar Transaktionen. När utbetalningen har godkänts av nätverket flyttas den till fliken Slutförd. Fliken Slutfört är enbart för historiska ändamål. Den innehåller de bearbetade utbetalningarna och de transaktioner som hör till den


### Dra betalningar


#### Koncept


När en avsändare konfigurerar en Pull-betalning kan de konfigurera ett antal egenskaper:



- Dragningsförfrågan Namn
- Ett gränsbelopp
- En enhet (t.ex. BTC, SAT, USD)
- Betalningsmetoder
  - BTC On-Chain
  - BTC off-chain
- Beskrivning
- Anpassad CSS
- Slutdatum (valfritt för Lightning Network BOLT11)


Efter detta kan avsändaren dela pull-betalningen med mottagaren via en länk, så att mottagaren kan skapa en utbetalning. Mottagaren väljer själv sin utbetalning:



- Vilken betalningsmetod du ska använda
- Vart ska pengarna skickas


När en utbetalning har skapats kommer den att räknas av mot pull-betalningens gräns för den aktuella perioden. Avsändaren kommer sedan att godkänna utbetalningen genom att ställa in den hastighet som utbetalningen ska skickas med och fortsätta med betalningen.


För avsändaren tillhandahåller vi en lättanvänd metod för att gruppera flera utbetalningar från [BTCPay Internal Wallet] (https://docs.btcpayserver.org/Wallet/).


#### Greenfield API


BTCPay Server tillhandahåller ett fullständigt API till både avsändaren och mottagaren som dokumenteras på sidan `/docs` i din instans. (eller på dokumentationswebbplatsen https://docs.btcpayserver.org)


Eftersom vårt API exponerar alla funktioner för pull-betalningar kan en avsändare automatisera betalningar efter sina egna behov.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig följande:



- Djupgående förståelse av BTCPay Servers Invoice-statusar samt åtgärder som kan utföras på dem
- Anpassa och hantera Invoice-mekanismer med förlängd livslängd, så kallade Requests.
- De ytterligare flexibla betalningsmöjligheterna som öppnas med BTCPay Servers unika Pull Payment-funktion, särskilt vid hantering av återbetalningar och löneutbetalningar.


### Bedömning av kunskap


#### KA Konceptuell granskning


Vilka är skillnaderna mellan fakturor och betalningsanmodan, och vad kan vara ett bra skäl till att använda den senare?


#### KA Konceptuell granskning


Hur utökar pull-betalningar vad som vanligtvis kan göras On-Chain? Beskriv några användningsfall som de möjliggör.


## BTCPay-serverns standardinsticksprogram


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Standardplugins och appar


BTCPay Server levereras med en standarduppsättning av plugins (appar) som kan förvandla BTCPay Server till en betalningsgateway för e-handel. Med tillägg av en Point Of Sale, Crowdfund-plattform och en enkel Pay-knapp blir BTCPay Server en lösning som är lätt att distribuera.


### Försäljningsställe


En av standardpluginsen för BTCPay Server är Point of Sale (PoS). Med PoS-pluginet kan en butiksägare skapa en webbshop direkt från BTCPay Server; butiksägaren behöver inte e-handelslösningar från tredje part för att driva en webbshop. Den webbaserade PoS-appen gör det möjligt för användare med fysiska butiker att enkelt acceptera Bitcoin, utan avgifter eller en tredje part, direkt i sin Wallet. PoS kan enkelt visas på surfplattor eller andra enheter som stöder webbsurfning. Användare kan enkelt skapa en genväg på hemskärmen för att snabbt komma åt webbappen.


#### Så här skapar du en ny Point of Sale


BTCPay Server gör det möjligt för butiksägare att snabbt skapa en försäljningsställe i flera layouter. BTCPay Server inser att inte alla butiker är e-handel, och inte alla butiker är en bar eller restaurang, och den levereras med flera standardinställningar för din PoS.


När butiksägaren klickar på "Point of Sale" i sin vänstra menyrad kommer BTCPay Server nu att fråga efter ett namn; detta namn kommer att synas i den vänstra menyraden. Klicka på Create för att skapa PoS.


![image](assets/en/97.webp)


#### Uppdatera den nyligen skapade kassan


När du har skapat en ny PoS kan du på följande skärm uppdatera din Point of Sale och lägga till varor i din butik.


##### Appens namn


Det namn som ges här till din försäljningspunkt kommer att synas i huvudmenyn på BTCPay-servern.


##### Visa titel


Allmänheten kommer att se titeln eller namnet på din butik när de besöker den. BTCPay Server namnger som standard din butik "Tea shop" Ersätt detta med din butiks namn.


![image](assets/en/98.webp)


#### Välj stil för försäljningsstället


BTCPay Server kan visa sin Point of Sale på flera sätt.



- Produktlista
  - En butiksvy där kunderna bara kan köpa 1 produkt åt gången.
- Produktlista med kundvagn.
  - En butiksvy där kunderna kan köpa flera varor samtidigt och få en översikt över kundvagnen till höger på skärmen.
- Endast knappsats
  - Ingen produktlista, bara ett tangentbord för direktfakturering.
- Print display (utskrivbar produktlista med QR)
  - Om du inte alltid kan visa din produktlista digitalt behöver du en "offline"-lösning för produkter; BTCPay Server har en utskriftsdisplay för att fungera som en offlinebutik.


![image](assets/en/99.webp)


#### Point Of Sale Style - Produktlista


![image](assets/en/100.webp)


#### Point of Sale-stil - Produktlista + kundvagn


![image](assets/en/101.webp)


#### Point Of Sale Style - endast knappsats


![image](assets/en/102.webp)


#### Point of Sale Style - Display för utskrift


![image](assets/en/103.webp)


#### Valuta


Butiksägaren kan ange en annan valuta för sin Point of Sale än den övergripande inställda standardvalutan. Butikens standardvaluta kommer automatiskt att fylla i detta fält.


#### Beskrivning


Berätta för världen om din butik; vad säljer du och för hur mycket? Allt som förklarar din butik hamnar här.


![image](assets/en/104.webp)


#### Produkter


När en försäljningsplats skapas lägger en standard BTCPay Server till ett par artiklar i butiken som referens. Klicka på knappen Redigera på något av standardobjekten för att bättre förstå varje möjligt alternativ för ett objekt.


När du skapar en ny produkt i din butik består den av följande fält;



- Titel
- Pris (fast, lägsta eller anpassat)
- URL för bild
- Beskrivning
- Inventarieförteckning
- ID
- Köp knapptext.
- Aktivera/Desaktivera


När butiksägaren har fyllt i alla nya produktfält klickar du på spara och du kommer att märka att avsnittet Produkter i Point of Sale nu fylls i. Spara alltid i det övre högra hörnet av skärmen för att förhindra att butiksägare tappar bort sina framsteg när de lägger till produkter.


Butiksägare kan också använda "Raw Editor" för att konfigurera sina produkter. Raw Editor kräver en grundläggande förståelse för JSON-strukturer.


![image](assets/en/105.webp)


#### Checka ut


BTCPay Server möjliggör små PoS-specifika kassaanpassningar. Butiksägaren kan ställa in texten "Köp för x" eller begära specifika kunddata genom att lägga till dem i formulären.


#### Tips


Endast vissa butiker behöver möjligheten till Tips på sin försäljning. Butiksägare kan slå på eller av detta som de anser passar för deras butik. Om butiken använder tips som är aktiverade kan butiksägaren ställa in texten i fältet för de tips de vill ha. BTCPay Server-tips fungerar baserat på ett procentuellt belopp. Butiksägare kan lägga till flera procentsatser, åtskilda med kommatecken.


#### Rabatter


Som butiksägare kanske du vill ge kunden en anpassad rabatt i kassan; reglaget för Rabatter blir tillgängligt i din butiks kassa. Detta avråds dock starkt från att använda självutcheckningssystem.


#### Anpassade betalningar


När alternativet Custom Payments är aktiverat kan kunden ange ett fast pris som är lika med eller högre än den ursprungliga Invoice som genererats av butiken.


#### Ytterligare alternativ


När du har ställt in allt för din Point of Sale finns det några extra alternativ kvar. Butiksägare kan enkelt bädda in sin PoS genom en Iframe eller bädda in en betalningsknapp som länkar till en specifik butiksartikel. För att stilisera den nyss skapade PoS-butiken kan ägare lägga till anpassad CSS längst ner i de ytterligare alternativen.


#### Ta bort den här appen


Om butiksägaren helt vill ta bort försäljningsstället från sin BTCPay Server, längst ner i uppdateringen av PoS, kan butiksägare klicka på knappen Radera den här appen för att helt förstöra sin PoS-app. När du klickar på "Ta bort den här appen" kommer BTCPay Server att be om bekräftelse genom att skriva `DELETE` och bekräfta genom att klicka på Delete-knappen. Efter borttagningen återgår butiksägaren till BTCPay Servers instrumentpanel.


### BTCPay Server - Crowdfund


Bredvid Point of Sale-plugin har BTCPay Server möjlighet att skapa en crowdfund. Precis som alla andra Crowdfund-plattformar kan butiksägare sätta ett mål, skapa förmåner för bidrag och anpassa det efter deras behov.


#### Så här startar du en ny crowdfund


Klicka på Crowdfund-plugin via huvudmenyn till vänster på din BTCPay Server, under Plugin-sektionen. BTCPay Server kommer nu att begära ett namn för Crowdfund; detta namn kommer också att visas i det vänstra menyfältet.


![image](assets/en/106.webp)


#### Uppdatera den nyligen skapade kassan


När appen har fått ett namn blir nästa skärm att uppdatera appen så att den får ett sammanhang.


#### Appens namn


Namnet som ges till din Crowdfund kommer att synas i huvudmenyn på BTCPay Server.


#### Visa titel


Titeln ges till Crowdfund för allmänheten.


#### Tagline


Ge crowdfundaren en one-liner för att känna igen vad insamlingen handlar om.


![image](assets/en/107.webp)


#### URL för utvald bild


Varje crowdfund har sin huvudbild, den banner som du känner igen direkt. Den här bilden kan lagras på din server om du har administrativa rättigheter. Administratörer kan ladda upp under BTCPay Serverinställningar - Filer. När du är butiksägare måste bilden laddas upp till webben via en tredjepartsvärd (till exempel Imgur).


#### Gör Crowdfund offentligt


Med den här knappen blir din crowdfund offentlig och därmed synlig för omvärlden. För teständamål eller för att se om ditt tema tillämpas korrekt, behåll denna inställning på OFF under den period då crowdfundingen byggs upp.


#### Beskrivning


Berätta för världen om din Crowdfund. Vad samlar du in pengar till? Allt som förklarar din crowdfund går här.


![image](assets/en/108.webp)


#### Crowdfunding Mål


Sätt upp ett mål för vad insamlaren ska tjäna till projektet och vilken valuta målet ska vara i. Se till att om dina mål är satta mellan datum, inkludera dessa mål- och slutdatum under Mål i crowdfund.


![image](assets/en/109.webp)


#### Förmåner


Förmåner kan avsevärt förbättra dina crowdfunding-insatser. Detta beror på att förmåner ger människor ett sätt att delta i din kampanj. De utnyttjar både själviska och välvilliga motivationer. Och de låter dig komma åt dina supportrars utgifter, inte bara deras filantropiska handväska - du kan gissa vilket som är mer betydelsefullt.


Att skapa en ny förmån består av följande fält.



- Titel
- Pris (fast, lägsta eller anpassat)
- URL för bild
- Beskrivning
- Inventarieförteckning
- ID
- Köp knapptext.
- Aktivera/Desaktivera


När butiksägaren har fyllt i alla fält för den nya förmånen klickar du på spara och du kommer att märka att avsnittet Förmåner i Crowdfunds nu fylls i.


![image](assets/en/110.webp)


### BTCPay Server - Försäljningsställe


#### Bidrag


Butiksägare kan välja hur förmåner ska visas, hur de ska sorteras eller till och med rangordna dem mot andra förmåner. Men när Crowdfunds-målen har uppnåtts kanske butiksägaren vill stoppa donationerna till den här insamlingen. Därför kan han växla på "Tillåt inte ytterligare bidrag efter att målet har nåtts". Detta kommer att förhindra Crowdfund från att acceptera donationer.


##### Crowdfunding-beteende


Crowdfunds standard räknar endast fakturor som skapats med Crowdfund mot målet. Det kan dock finnas fall där butiksägaren vill att alla fakturor som görs i den här butiken ska räknas mot crowdfundingen.


#### Ytterligare alternativ för kundanpassning


BTCpay Server erbjuder ett par extra anpassningar. Lägg till ljud, animationer eller till och med diskussionstrådar till Crowdfund. Butiksägare kan också ändra utseendet och känslan av Crowdfund genom att ange sin egen anpassade CSS.


#### Ta bort den här appen


Om butiksägaren vill ta bort Crowdfund helt från sin BTCPay Server, längst ner i uppdateringen av Crowdfund, kan de klicka på knappen "Ta bort den här appen" för att helt ta bort sin Crowdfund-app. När du klickar på "Ta bort den här appen" kommer BTCPay Server att be om bekräftelse genom att skriva `DELETE` och bekräfta genom att klicka på Delete-knappen. Efter borttagningen återgår butiksägaren till BTCPay Servers instrumentpanel.


### BTCPay Server - Betalningsknapp


Enkelt inbäddningsbar HTML och mycket anpassningsbara betalningsknappar gör det möjligt för butiksägare att ta emot tips och donationer. I den vänstra menyraden på BTCPay Server, under avsnittet Plugins, kan butiksägare klicka på "Betalningsknapp" och klicka på Aktivera för att skapa en betalningsknapp.


#### Allmänna inställningar


I de allmänna inställningarna för betalningsknappen kan butiksägare ställa in



- Standardpris
- Standardvaluta
- Standard betalningsmetod
  - Använd standard för lagring
  - BTC On-Chain
  - BTC off-chain (blixtnedslag)
  - BTC off-chain (LNURL-pay)
- Beskrivning av utcheckning
- Order-ID


#### Visningsalternativ


BTCPay Server's Pay-knapp kan konfigureras för att passa olika stilar. Knapparna kan ha ett fast eller anpassat belopp, som antingen visas med ett skjutreglage eller plus- och minusknappar.


#### Använd modal


När du skapar betalningsknappen kan butiksägare välja hur den ska bete sig när en kund klickar på den och visa den i en modal eller som en ny sida.


**!?Note!?**


Varning för detta: Betalningsknappen ska endast användas för dricks och donationer


Att använda betalningsknappen för e-handelsintegrationer rekommenderas inte eftersom användaren kan ändra orderrelevant information. För e-handel bör du använda vårt Greenfield API. Om den här butiken hanterar kommersiella transaktioner rekommenderar vi att du skapar en separat butik innan du använder betalningsknappen.


#### Anpassa texten på betalningsknappen


Som standard står det "Betala med BTCPay" på BTCPay Servers betalningsknapp. Butiksägare kan ställa in den här texten efter eget önskemål och ändra BTCPay Server-logotypen till sin egen. Ställ in texten genom att använda "Pay Button Text" och klistra in bild-URL:en under "Pay Button Image URL".


##### Bildstorlek


Storleken på bilden i knappen kan bara ställas in på tre standardvärden.



- 146x40px
- 168x46px
- 209x57px


#### Knapptyp


BTCPay Server känner till tre tillstånd för betalningsknappen.



- Fast belopp
  - Det tidigare inställda priset finns i knappens allmänna inställningar.
- Anpassat belopp
  - BTCPay Server's Pay-knapp har + och - växlar för att ställa in ett anpassat pris.
  - När du använder det anpassade beloppet kommer BTCPay Server att begära ett Min, Max och hur gradvis det ska öka.
  - Knapparna kan ställas in på "Använd enkel inmatningsstil", vilket innebär att +/-reglagen tas bort.
  - Fäst knappen inline där knappen och reglagen visas inline.
- Skjutreglaget
  - På samma sätt som det anpassade beloppet är det dock visuellt annorlunda eftersom det har ett reglage istället för +/- reglagen.
  - När du använder skjutreglaget kommer BTCPay Server att begära en Min, Max och hur gradvis den ska öka.


**!?Note!?**


Betalningsknappen kan tas bort längst upp i varningsbeskrivningen.


#### Betalningsaviseringar


Server IPN (Instant Payment Notification) är utformad för webhooks och kan konfigureras med en URL till efterköpsdata.


#### Notifieringar via e-post


När en betalning har gjorts kan BTCPay Server meddela butiksägaren.


#### Omdirigering av webbläsare


När kunden slutför köpet kommer han att omdirigeras till den här länken om den har ställts in av butiksägaren.


#### Avancerade alternativ för betalningsknapp


Ange ytterligare parametrar för frågesträngen som ska läggas till på utcheckningssidan när Invoice har skapats. Till exempel skulle `lang=da-DK` ladda kassasidan på danska som standard.


#### Använd app som slutpunkt


Du kan direkt koppla betalningsknappen till ett objekt i någon av de PoS- eller Crowdfund-appar som du har använt tidigare.


Butiksägare kan klicka på rullgardinsmenyn och välja önskad app; när appen är vald kan butiksägaren lägga till den artikel som behöver länkas.


#### Genererad kod


Eftersom BTCPay Servers betalningsknapp är en HTML-kod som är lätt att bädda in, visar BTCPay Server den genererade koden som ska kopieras till en webbplats längst ner efter att betalningsknappen har konfigurerats.


Butiksägare kan kopiera den genererade koden till sin webbplats, och betalningsknappen från BTCPay Server är direkt aktiv på deras webbplats.


#### Betalningsaviseringar


Server IPN (Instant Payment Notification) är utformad för webhooks och kan konfigureras med en URL för att lägga upp köpdata.


#### Notifieringar via e-post


När en betalning görs kan BTCPay Server meddela butiksägaren.


#### Omdirigering av webbläsare


När kunden slutför köpet kommer han att omdirigeras till den här länken om den har ställts in av butiksägaren.


#### Avancerade alternativ för betalningsknapp


Ange ytterligare parametrar för frågesträngen som ska läggas till på utcheckningssidan när Invoice har skapats. Till exempel skulle `lang=da-DK` ladda kassasidan på danska som standard.


#### Använd app som slutpunkt


Du kan direkt koppla betalningsknappen till ett objekt i någon av de PoS- eller Crowdfund-appar som du har använt tidigare. Butiksägare kan klicka på rullgardinsmenyn och välja önskad app. När appen har valts kan butiksägaren lägga till det objekt som ska länkas.


#### Genererad kod


Eftersom BTCPay Servers betalningsknapp är en HTML-kod som är lätt att bädda in, visar BTCPay Server den genererade koden som ska kopieras till en webbplats längst ner efter att betalningsknappen har konfigurerats. Butiksägare kan kopiera den genererade koden till sin webbplats, och betalningsknappen från BTCPay Server är direkt aktiv på deras webbplats.


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig:



- Så här använder du BTCPay Servers integrerade PoS-plugin för att enkelt skapa en anpassad butik
- Så här använder du BTCPay Servers integrerade Crowdfund-plugin för att enkelt skapa en anpassad crowdfund-app
- Generera kod för en anpassad betalknapp med hjälp av tillägget Pay Button


### Bedömning av kunskap


#### KA granskning


Vilka är de tre inbyggda plugins som levereras som standard med BTCPay Server? Beskriv med några ord hur de kan användas.


# Konfigurera BTCPay-servern


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Grundläggande förståelse för installation av BTCPay Server i en LunaNode-miljö


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Installera BTCPay-servern på en hostad enhet (LunaNode)


Dessa steg ger all nödvändig information för att komma igång med att använda BTCPay Server på LunaNode. Det finns många alternativ för att distribuera programvaran.

Du kan hitta alla detaljer om BTCPay Server på https://docs.btcpayserver.org.


#### Var ska vi börja?


I den här delen kommer du att bekanta dig med LunaNode som värdleverantör, lära dig om de första stegen för att använda din BTCPay-server och lära dig hur du använder Lightning Network. När vi har gått igenom alla steg kan du köra en webbshop eller crowdfund-plattform som accepterar Bitcoin!


Detta är ett av många sätt att distribuera BTCPay Server. Läs vår dokumentation för mer information.


https://docs.btcpayserver.org.


### BTCPay Server - LunaNode-distribution


#### Utplacering av LunaNode


Gå först till LunaNode.com:s webbplats, där vi skapar ett nytt konto. Klicka på Sign Up uppe till höger eller använd guiden Get Started på hemsidan.


![image](assets/en/111.webp)


Efter att du har skapat ditt nya konto skickar LunaNode ett verifieringsmejl. När du har verifierat kontot, jämfört med Voltage, får du omedelbart möjlighet att fylla på ditt kontosaldo. Detta saldo är nödvändigt för att täcka serverutrymmet och värdkostnaderna.


![image](assets/en/112.webp)


#### Lägg till kredit på ditt LunaNode-konto


När du har klickat på "Sätt in kredit" får du ställa in hur mycket du vill fylla på ditt konto med och hur du vill betala för det. LunaNode och BTCPay Server kommer att kosta mellan $ 10 och $ 20 per månad.

Jämfört med Voltage.cloud får du full tillgång till din Virtual Private Server (VPS), vilket gör att du kan ha mer kontroll över din server. När du har skapat ditt nya konto skickar LunaNode ett verifieringsmejl.

När du har verifierat kontot, jämfört med Voltage, får du omedelbart möjlighet att fylla på ditt kontosaldo. Detta saldo är nödvändigt för att täcka kostnaderna för serverutrymme och hosting.


#### Hur distribuerar jag en ny server?


I den här guiden kommer vi att leda dig genom installationsprocessen genom att skapa en uppsättning API-nycklar och använda BTCPay Server-startprogrammet som utvecklats av LunaNode.


I din LunaNode-instrumentpanel klickar du på API längst upp till höger. Detta öppnar upp en ny sida. Vi behöver bara ställa in ett namn för API-nyckeln. Resten sköts av LunaNode och tas inte upp i den här guiden. Klicka på knappen Create API Credential.

När du har skapat API-autentiseringsuppgifterna får du en lång sträng med bokstäver och tecken. Detta är din API-nyckel.


![image](assets/en/113.webp)


#### Hur distribuerar jag en ny server?


Det finns två delar till dessa referenser, API-nyckel och API-ID; vi behöver båda. Innan vi går in på nästa steg, låt oss öppna en andra flik i webbläsaren och gå till https://launchbtcpay.lunanode.com/


Här kommer du att bli ombedd att ange din API-nyckel och API-ID. Detta är för att du ska veta att det är du som har tillhandahållit den nya servern. API-nyckeln bör fortfarande vara öppen i din tidigare flik; om du bläddrar ner i tabellen nedan hittar du API-ID.


Du kan gå tillbaka till sidan med Launcher, fylla i fälten med din API-nyckel och ditt ID och klicka på fortsätt.


![image](assets/en/114.webp)


I nästa steg kan du ange ett domännamn. Om du redan äger en domän och vill använda den för BTCPay Server, se till att du också lägger till DNS-posten (kallas en "A"-post) på din domän. Om du inte äger en domän använder du istället den domän som LunaNode tillhandahåller (du kan ändra detta senare i inställningarna för BTCPay Server) och klickar på Fortsätt.


Läs mer om hur du ställer in eller ändrar en DNS-post för BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Starta BTCPay-servern på LunaNode


Efter att ha tagit stegen tidigare kan vi ställa in alla alternativ för vår nya server. Här kommer vi att välja Bitcoin (BTC) som vår stödda valuta. Vi kan också ställa in ett e-postmeddelande för att få meddelanden om krypteringscertifikat för förnyelseändamål, vilket är valfritt.


Den här guiden syftar till att ställa in en Mainnet-miljö (Bitcoin i verkligheten); LunaNode låter dig dock också ställa in den till Testnet eller Regtest för utvecklingsändamål. Vi kommer att lämna det på Mainnet-alternativet för den här guiden.


Du kan välja din Lightning-implementering. LunaNode erbjuder två olika implementationer, LND och Core Lightning. I den här guiden kommer vi att använda LND. Det finns få men verkliga skillnader i båda implementationerna; för mer om detta rekommenderar vi att du läser den omfattande dokumentationen: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/115.webp)


LunaNode erbjuder flera planer för virtuella maskiner (VM). Dessa skiljer sig åt när det gäller prisintervall och serverspecifikationer. I den här guiden räcker det med en m2-plan, men om du har valt mer än bara Bitcoin som valuta bör du överväga att använda minst en m4.


Påskynda den inledande Blockchain-synkroniseringen; detta är valfritt och beror på dina behov. Det finns avancerade alternativ, till exempel att ställa in ett Lightning Alias, peka på en specifik GitHub-version eller ställa in SSH-nycklar; inget av detta kommer att behandlas i den här guiden.


När du har fyllt i formuläret måste du klicka på Launch VM, och Lunanode börjar skapa din nya VM, inklusive BTCPay Server installerad på den. Denna process tar ett par minuter; när din server är klar ger LunaNode dig länken till din nya BTCPay-server.


Efter skapandeprocessen klickar du på länken till din BTCPay-server; här kommer du att bli ombedd att skapa ett administratörskonto.


![image](assets/en/116.webp)


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig:



- Skapa och finansiera ett konto på LunaNode
- Använda BTCPay Server Launcher för att skapa din egen server


### Bedömning av kunskap


#### KA Konceptuell granskning


Beskriv några av skillnaderna mellan att köra en instans av BTCPay Server på en VPS och att skapa ett konto på en hostad instans.


## Installera BTCPay Server i en Voltage-miljö


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Du kommer att bekanta dig med Voltage.cloud som värdleverantör, lära dig om de första stegen för att använda din BTCPay-server och lära dig hur du använder Lightning Network. Efter att vi har gått igenom alla steg kan du driva en webbshop eller crowdfund-plattform som accepterar Bitcoin!


Detta är ett av många sätt att distribuera BTCPay Server. Läs vår dokumentation för mer information.

https://docs.btcpayserver.org.


### BTCPay Server - Spänning.moln-distribution


Först går du till webbplatsen Voltage.cloud och registrerar dig för ett nytt konto. När du skapar ett konto kan du registrera dig för en 7-dagars gratis provperiod. Klicka antingen på Sign Up uppe till höger eller använd "Prova en gratis 7-dagars provperiod" på deras hemsida.


![image](assets/en/117.webp)


När du har skapat ett konto klickar du på knappen "NODES" på din instrumentpanel. När vi har valt Nodes och skapat en ny nod får vi presenterat de möjliga nodernas Voltage-erbjudanden. Eftersom den här guiden också kommer att täcka Lightning Network, vid Voltage, måste vi först välja vår Lightning-implementering innan vi skapar en BTCPay-server. Klicka på LightningNode.


![image](assets/en/118.webp)


Här måste du välja vilken typ av Lightning-nod du vill ha. Voltage har en mängd olika alternativ för din belysningsinstallation. Detta är annorlunda när du distribuerar med till exempel LunaNode. För avsikten med denna guide räcker det med en Lite Node. Läs mer om skillnaderna i Voltage.cloud.


![image](assets/en/119.webp)


Ge din nod ett namn, ange ett lösenord och säkra lösenordet. Om lösenordet försvinner förlorar du åtkomst till dina säkerhetskopior och Voltage kan inte återställa det. Skapa noden och Voltage visar dig hur det går. Voltage har skapat din Lightning Node. Vi kan nu skapa BTCPay Server-instansen och få direkt åtkomst till Lightning Network.


Klicka på Nodes längst upp till vänster på instrumentpanelen. Här kan du ställa in nästa del av din BTCPay Server-instans. Klicka på "skapa ny" när du är i noderöversikten. Du får en liknande skärm som tidigare. Nu, istället för Lightning Node, väljer vi BTCPay Server.


Voltage visar dig geolokaliseringen av din BTCPay-server, som är hostad i US West-regionen. Här ser du också kostnaden för att vara värd för servern. Klicka på Skapa och ge din BTCPay-server ett namn. Aktivera Lightning och Voltage visar dig Lightning-noden som skapades i föregående steg. Klicka på Create och Voltage skapar en BTCPay Server-instans.


![image](assets/en/120.webp)


När du har tryckt på create visar Voltage ett standardanvändarnamn och ett standardlösenord. Dessa liknar ditt tidigare inställda lösenord i Voltage. Klicka på knappen Logga in på konto för att omdirigera dig till din BTCPay-server.


Välkommen till din nya BTCPay Server-instans. Eftersom vi redan har ställt in Lightning i skapandeprocessen visar det att Lightning redan är aktiverat!


### Sammanfattning av färdigheter


I detta kapitel har du lärt dig:



- Skapa ett konto på Voltage.cloud
- Steg för att få BTCPay Server att köras tillsammans med en Lightning-nod på kontot


### Bedömning av kunskap


#### KA Konceptuell granskning


Vilka är de viktigaste skillnaderna mellan Voltage- och LunaNode-konfigurationerna?


## Installera BTCPay Server på en Umbrel-nod


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


I slutet av dessa steg kan du acceptera blixtbetalningar till din BTCPay-butik i ditt lokala nätverk. Den här processen gäller även om du driver en umbrel-nod i en restaurang eller ett företag. Om du vill ansluta den här butiken till en offentlig webbplats följer du övningen Avancerat för att exponera din umbrel-nod för allmänheten.


https://umbrel.com/


![image](assets/en/121.webp)


### BTCPay Server - Umbrel-distribution


När din Umbrel-nod har synkroniserats helt med Bitcoin Blockchain går du till Umbrel App Store och söker efter BTCPay Server under Apps.


![image](assets/en/122.webp)


Klicka på BTCPay Server för att se appens detaljer. När detaljerna för BTCPay Server är öppna visar det nedre högra hörnet kraven för att appen ska fungera korrekt. Det visar att det krävs en Bitcoin och Lightning-nod. Om du inte har installerat Lightning-noden på din Umbrel klickar du på Installera. Denna process kan ta ett par minuter.


![image](assets/en/123.webp)


Efter att ha installerat din Lightning Node:


1. Klicka på Öppna i appens detaljer eller på Appen i Umbrels instrumentpanel.

2. Klicka på setup a new node; du kommer att få se 24 ord för återställning av din lightning node.

3. Skriv ner dessa.


![image](assets/en/124.webp)


Umbrel kommer att be om verifiering av de ord som just skrivits ner. När Lightning-noden är konfigurerad, gå tillbaka till Umbrel App Store och leta upp BTCPay Server. Klicka på installationsknappen och Umbrel kommer att visa om de nödvändiga komponenterna är installerade och att BTCPay Server kräver åtkomst till dessa komponenter. Efter installationen klickar du på Open uppe till höger i App details eller öppnar BTCPay Server via din Umbrels instrumentpanel.


Umbrel kommer att be om verifiering av de ord som just skrivits ner.


![image](assets/en/125.webp)


**!?Note!?**


Se till att förvara dessa på ett säkert ställe, på samma sätt som du tidigare lärt dig när du förvarar nycklar.


När Lightning-noden är konfigurerad, gå tillbaka till Umbrel App Store och leta upp BTCPay Server. Klicka på installationsknappen och Umbrel kommer att visa om de nödvändiga komponenterna är installerade och att BTCPay Server kräver åtkomst till dessa komponenter.


![image](assets/en/126.webp)


Efter installationen klickar du på Öppna längst upp till höger i appdetaljerna eller öppnar BTCPay Server via din Umbrels-instrumentpanel.


![image](assets/en/127.webp)


### Sammanfattning av färdigheter


I detta avsnitt har du lärt dig:



- Steg för att installera BTCPay Server med Lightning-funktionalitet på en Umbrel-nod


### Bedömning av kunskap


#### KA Konceptuell granskning


Hur skiljer sig upplägget på Umbrel från de två tidigare värdalternativen?


# Sista avsnittet


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Recensioner & betyg

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Slutsats av kursen


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>