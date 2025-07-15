---
name: Kraken - Företag
description: Skapa och hantera ett Kraken-företagskonto
---
![cover](assets/cover.webp)


Kraken är en av världens mest välkända Exchange-plattformar för kryptovalutor. De erbjuder en mängd olika tjänster som är skräddarsydda för företag som vill integrera Bitcoin i sin ekonomiska förvaltning.


I denna handledning kommer vi att täcka processen för att skapa ett Kraken-företagskonto, köpa och sälja bitcoins, hantera transaktioner för redovisningsändamål och sätta in och ta ut euro och bitcoins. Syftet är att ge dig grundläggande kunskaper, oavsett om du överväger att integrera Bitcoin i ditt kassaflöde eller acceptera Bitcoin som betalningsmedel.


Om du är intresserad av att integrera Bitcoin i ditt företag rekommenderar jag också att du tar del av vår kompletta teoretiska utbildning i ämnet:


https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a

## 1 - Skapa ett företagskonto för Kraken


Det första steget i att använda Kraken för att hantera ditt företags ekonomi är naturligtvis att skapa ett konto. Här ska vi inte skapa ett konto för privatpersoner utan ett företagskonto, som inte bara säkerställer regelefterlevnad utan också erbjuder specialanpassade funktioner som redovisningsexport.


Gå till den officiella webbplatsen [kraken.com] (https://www.kraken.com/) och klicka på knappen "*Sign Up*".


![KRAKEN](assets/fr/01.webp)


På registreringssidan väljer du fliken "*Business*" bland kontoalternativen för att ange att ett företagskonto ska skapas.


![KRAKEN](assets/fr/02.webp)


Ange din professionella e-post Address och välj ett säkert lösenord. När du har fyllt i dessa uppgifter klickar du på "*Skapa ett konto*" för att slutföra registreringen.


![KRAKEN](assets/fr/03.webp)


När du har lämnat dina uppgifter kommer Kraken att skicka ett e-postmeddelande om aktivering.


![KRAKEN](assets/fr/04.webp)


Öppna detta e-postmeddelande och klicka på "*Activate Account*" eller ange den 6-siffriga koden för att aktivera ditt konto.


![KRAKEN](assets/fr/05.webp)


## 2 - Verifiering av företagskonto


När du har skapat ditt konto måste du slutföra KYC (*Know Your Customer*)-verifieringsprocessen för företagskonton. Detta steg gör det möjligt för Kraken att verifiera ditt företags legitimitet och efterlevnad av finansiella regler.


Klicka på knappen "*Fortsätt*".


![KRAKEN](assets/fr/06.webp)


Vänligen fyll i nödvändig information om ditt företag.


![KRAKEN](assets/fr/07.webp)


Du kommer också att behöva ladda upp flera dokument som rör ditt företag.


![KRAKEN](assets/fr/08.webp)


När du har fyllt i alla avsnitt och skickat de nödvändiga dokumenten klickar du på "*Submit*" för att skicka din verifieringsbegäran. Det kan ta upp till två veckor att behandla din begäran. För att påskynda processen, se till att du tillhandahåller alla nödvändiga dokument från början.


## 3 - Kontosäkerhet


När ditt konto har verifierats kommer du att få tillgång till plattformen där du erbjuds två gränssnitt:




- Kraken**: En förenklad Interface med viktiga funktioner.
- Kraken Pro**: En avancerad Interface med ytterligare funktioner, särskilt för handel.


Om ditt mål enbart är att köpa och sälja Bitcoin ska du välja den förenklade Interface. Du kommer alltid att ha möjlighet att byta till den avancerade Interface senare om det behövs.


![KRAKEN](assets/fr/09.webp)


Först och främst är det mycket viktigt att säkra ditt konto för att förhindra obehörig åtkomst. Förutom det starka lösenordet som fastställs vid registreringen kommer vi att implementera dubbel autentisering. Det innebär att varje gång du loggar in på ditt Kraken-konto behöver du inte bara ditt lösenord utan också en andra autentiseringsfaktor, som kan vara en fysisk nyckel eller en kod som genereras av en autentiseringsapplikation.


Gå till din kontoikon och klicka på "*Säkerhet*".


![KRAKEN](assets/fr/10.webp)


I 2FA-alternativen kan du välja att använda en fysisk säkerhetsnyckel som en andra faktor.


![KRAKEN](assets/fr/11.webp)


För mer information om hur du använder den här typen av enhet, se vår dedikerade handledning :


https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Det andra alternativet är att använda en autentiseringsapplikation som Google Authenticator eller Authy. Dessa applikationer generate en dynamisk 6-siffrig kod som du måste ange varje gång du loggar in.


![KRAKEN](assets/fr/12.webp)


För att aktivera denna metod, skanna QR-koden med den applikation du väljer på din smartphone och ange sedan den 6-siffriga kod som genereras.


![KRAKEN](assets/fr/13.webp)


För mer information om autentiseringsapplikationer kan du också läsa denna handledning :


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Därunder har du också tillgång till avancerade inställningar, inklusive möjligheten att ställa in flera olika 2FA. Kraken erbjuder avancerad säkerhetsdelegering via 2FA. Med den här funktionen kan du skapa olika 2FA-nivåer för olika åtgärder, till exempel inloggning, ordervalidering och fonduttag. Detta gör det möjligt att till exempel ge en revisor tillgång till vissa funktioner utan att tillåta honom eller henne att ta ut pengar. Här är alternativen:




- Huvudnyckeln** fungerar som en återställningsmekanism som ska användas om du inte kan komma åt din vanliga 2FA-metod för att logga in;
- **2FA för finansiering** kräver ytterligare autentisering för alla uttagstransaktioner eller när du skapar en insättning Address, vilket stärker säkerheten för dina medel;
- Med **2FA för handel** införs en 2FA för varje transaktion som utförs på kontot.


![KRAKEN](assets/fr/14.webp)


Med dessa avancerade alternativ kan du definiera olika behörighetsnivåer inom din organisation.


## 4 - Insättning och uttag av fiat-valuta


När ditt konto har verifierats och säkrats kan du sätta in pengar i euro (eller i din lokala valuta). Du kan också göra uttag i enlighet med dina affärsbehov.


För att sätta in euro, gå till avsnittet "*Transfer*".


![KRAKEN](assets/fr/15.webp)


Välj "*Euro*" i rutan "*Asset*" och bekräfta för att få de uppgifter som behövs för att göra en betalning från ditt företags bankkonto. Du kan också välja att betala med kreditkort.


![KRAKEN](assets/fr/16.webp)


För att ta ut euro från ditt Kraken-konto, följ samma process men använd fliken "*Withdraw*".


![KRAKEN](assets/fr/17.webp)


## 5 - Insättning och uttag av bitcoins


För att sätta in bitcoins på ditt Kraken-konto, gå tillbaka till avsnittet "*Transfer*". I rutan "*Asset*" väljer du "*BTC*" och bekräftar sedan för att ta emot Address som du måste skicka bitcoins till från din självförvarade Wallet.


![KRAKEN](assets/fr/18.webp)


För att ta ut bitcoins från ditt Kraken-konto till en självförvarad Wallet, klicka på fliken "*Withdraw*".


![KRAKEN](assets/fr/19.webp)


Ange din Wallet Address och bekräfta sedan åtgärden med din 2FA.


## 6 - Köpa och sälja bitcoins


Kraken erbjuder olika handelsgränssnitt, vart och ett utformat för att möta specifika behov. För professionell, avancerad hantering rekommenderas Kraken Pro. För enklare transaktioner räcker det med Krakens standard Interface. För att ändra Interface, klicka på de små prickarna längst upp till höger på skärmen:


![KRAKEN](assets/fr/20.webp)


På standard Interface, för att köpa Bitcoin, börja med att klicka på "*Buy*" på hemsidan.


![KRAKEN](assets/fr/21.webp)


Ange det belopp som du vill köpa och bekräfta åtgärden. Om en 2FA är konfigurerad för den här åtgärden anger du den 6-siffriga kod som tillhandahålls av din autentiseringsapplikation.


För att sälja Bitcoin, klicka på "*Sälj*".


![KRAKEN](assets/fr/22.webp)


Ange det belopp som ska säljas och bekräfta transaktionen.


Du kan också Exchange dina bitcoins för andra kryptovalutor, till exempel stablecoins, för att minska din exponering för Bitcoin fluktuationer. För att göra det klickar du på "*Konvertera*".


![KRAKEN](assets/fr/23.webp)


Välj belopp, välj den kryptovaluta du vill få och bekräfta sedan transaktionen.


För dessa transaktioner kan du välja mellan olika ordertyper: *Marknad*, *Limit* eller *Stop-Loss*:




- Marknad* : Tillåter omedelbart köp till aktuellt marknadspris;
- Begränsa*: Låter dig ange ett inköpspris, och ordern kommer endast att utföras om marknadspriset når detta belopp;
- Stop-Loss* : Säljer automatiskt när kursen når ett visst tröskelvärde.


## 7 - Transaktionshantering och redovisning


Som företag kommer du förmodligen att behöva exportera detaljer om dina Kraken-transaktioner för redovisningsändamål. Kraken erbjuder verktyg för att underlätta export av transaktionshistorik och ger en detaljerad bild av dina Wallet.


För att få en förenklad bild av din transaktionshistorik, gå till menyn "*Transaktioner*".


![KRAKEN](assets/fr/24.webp)


För mer detaljerad export för bokföringsändamål, gå till inställningarna under fliken "*Dokument*".


![KRAKEN](assets/fr/25.webp)


Klicka på "*Create export file*" och välj vilken typ av export du vill ha. I det här exemplet kommer jag att exportera transaktionshistoriken.


![KRAKEN](assets/fr/26.webp)


Du kan sedan ange alla detaljer som är nödvändiga för din situation:




- Information som ska ingå i exporten ;
- Datum att ta hänsyn till ;
- Exchange par ska inkluderas;
- Filens exportformat (PDF eller CSV).


![KRAKEN](assets/fr/27.webp)


## 8 - Användningsområden för företaget


Beroende på ditt företags mål och struktur kan användningen av Kraken variera.


### Köpa bitcoins för kontanter


**Mål:** Diversifiera bolagets kassaflöde genom att investera i Bitcoin.


**Steg att följa:**




- Sätt in euro på Kraken från företagets bankkonto;
- Använd dessa euro för att köpa Bitcoin;
- Förvara bitcoins på plattformen eller ta ut dem för att säkra dem i självförvaring;
- Exportera transaktionshistorik efter behov.


### Acceptera Bitcoin som betalningsmedel


**Mål:** Erbjud ditt företag möjligheten att acceptera Bitcoin som betalningsmedel för dina produkter eller tjänster.


**Steg att följa:**




- Integrera ett Bitcoin-betalningssystem. För små företag kan det räcka med en enkel Wallet-programvara, eller så kan du välja specialiserade lösningar som Swiss Bitcoin Pay eller BTCPay Server för att integrera Bitcoin som ett betalningsalternativ på din webbplats eller vid försäljningsstället;
- Överför betalningar som mottagits i bitcoins till ditt Kraken-konto;
- Beroende på din finansiella strategi kan du sälja de bitcoins du fått för euro, behålla dem för potentiell framtida värdeökning eller välja en kombination av båda;
- Förvara bitcoins på plattformen eller ta ut dem för självförvaring. Du kan också ta ut euro till ditt bankkonto;
- Exportera transaktionshistorik efter behov.


För en mer djupgående titt på detta ämne rekommenderar jag denna omfattande utbildningskurs om att integrera Bitcoin i företag, som i detalj täcker att lägga till kassaflöde, acceptera Bitcoin-betalningar och redovisning :


https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a