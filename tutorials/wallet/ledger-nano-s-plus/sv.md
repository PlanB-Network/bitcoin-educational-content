---
name: Ledger Nano S Plus
description: Inställning och användning av Ledger Nano S Plus
---
![cover](assets/cover.webp)


En Hardware Wallet är en elektronisk enhet som är avsedd att hantera och säkra de privata nycklarna för en Bitcoin Wallet. Till skillnad från mjukvaruplånböcker (eller Hot-plånböcker) som installeras på maskiner för allmänt bruk som ofta är anslutna till Internet, möjliggör hårdvaruplånböcker fysisk isolering av privata nycklar, vilket minskar riskerna för hackning och stöld.


Huvudmålet med en Hardware Wallet är att minimera enhetens funktioner så mycket som möjligt för att minska dess attackyta. En mindre attackyta innebär också färre potentiella attackvektorer, dvs. färre svagheter i systemet som angripare kan utnyttja för att komma åt bitcoins.


Vi rekommenderar att du använder en Hardware Wallet för att säkra dina bitcoins, särskilt om du innehar betydande belopp, oavsett om det är i absolut värde eller som en andel av dina totala tillgångar.


Hårdvaruplånböcker används i kombination med en Wallet-hanteringsprogramvara på en dator eller smartphone. Denna programvara hanterar skapandet av transaktioner, men den kryptografiska signatur som krävs för att validera dessa transaktioner görs endast inom Hardware Wallet. Detta innebär att de privata nycklarna aldrig exponeras för en potentiellt sårbar miljö.


Hårdvaruplånböcker erbjuder dubbelt skydd för användaren: å ena sidan skyddar de dina bitcoins mot fjärråttacker genom att hålla de privata nycklarna offline, och å andra sidan erbjuder de i allmänhet bättre fysiskt motstånd mot försök att extrahera nycklarna. Och det är just på dessa två säkerhetskriterier som man kan bedöma och rangordna de olika modellerna som finns på marknaden.


I den här handledningen föreslår jag att du upptäcker en av dessa lösningar: ** Ledger Nano S Plus **.


![NANO S PLUS LEDGER](assets/notext/01.webp)


## Introduktion till Ledger Nano S Plus


Ledger Nano S Plus är en Hardware Wallet som tillverkas av det franska företaget Ledger och marknadsförs till ett pris av 79 €.


![NANO S PLUS LEDGER](assets/notext/02.webp)


Nano S Plus är utrustad med ett CC EAL6+-certifierat chip ("*secure element*"), som ger dig ett avancerat skydd mot fysiska attacker på hårdvaran. Skärmen och knapparna styrs direkt av detta chip. En kritik som ofta framförs är att koden för detta chip inte är öppen källkod, vilket kräver ett visst förtroende för integriteten hos denna komponent. Trots detta granskas detta element av oberoende experter.


När det gäller användning fungerar Ledger Nano S Plus enbart via en trådbunden USB-C-anslutning.


Ledger skiljer sig från sina konkurrenter genom sitt alltid mycket snabba införande av nya Bitcoin-funktioner, som till exempel Taproot eller Miniscript, vilket är mycket uppskattat.

Efter att ha testat den tycker jag att Ledger Nano S Plus är en utmärkt instegsmodell till Hardware Wallet. Den erbjuder en hög säkerhetsnivå till ett rimligt pris. Dess största nackdel jämfört med andra enheter i samma prisklass är det faktum att firmware-koden inte är öppen källkod. Skärmen på Nano S Plus är också relativt liten jämfört med dyrare modeller, till exempel Ledger Flex eller Coldcard Q1. Trots detta är dess Interface mycket väl utformad: trots sina två knappar och lilla skärm är den fortfarande lätt att använda, inklusive för avancerade funktioner som BIP39 passphrase. Ledger Nano S Plus har inget batteri, Air-gap-anslutning, kamera eller micro SD-port, men det är ganska normalt för den här prisklassen.


Enligt min mening är Ledger Nano S Plus ett bra alternativ för att säkra din Bitcoin Wallet, och är lämplig för både nybörjare och avancerade användare. Men i den här prisklassen föredrar jag personligen Trezor Safe 3, som erbjuder ungefär samma alternativ. Fördelen med Trezor, enligt min mening, är i hanteringen av dess säkra element: Mnemonic-frasen och nycklarna hanteras uteslutande av öppen källkod, men drar fortfarande nytta av chipets skydd. Nackdelen med Trezor är att de ibland är mycket långsamma med att implementera nya funktioner till skillnad från Ledger.


## Hur köper jag en Ledger Nano S Plus?


Ledger Nano S Plus finns tillgänglig för försäljning [på den officiella webbplatsen](https://shop.Ledger.com/products/Ledger-nano-s-plus). Om du vill köpa den i en fysisk butik kan du också hitta [listan över certifierade återförsäljare](https://www.Ledger.com/reseller) på Ledger:s webbplats.


## Förkunskapskrav


När du har fått din Ledger Nano är det första steget att kontrollera förpackningen för att säkerställa att den inte har öppnats. Om den är skadad kan det tyda på att Hardware Wallet har äventyrats och kanske inte är äkta.


Vid öppnandet bör du hitta följande föremål i lådan:


- Ledger Nano S Plus;
- En USB-C till USB-A-kabel;
- En användarmanual;
- Kort för att skriva ner din Mnemonic-fras.


För denna handledning behöver du 2 programvaruapplikationer: Ledger Live för att initiera Ledger, och Sparrow wallet för att hantera din Bitcoin Wallet. Ladda ner [Ledger Live] (https://www.Ledger.com/Ledger-live) och [Sparrow wallet] (https://sparrowwallet.com/download/) från deras officiella webbplatser.


![NANO S PLUS LEDGER](assets/notext/03.webp)

För dessa två program rekommenderar jag starkt att du kontrollerar både deras äkthet (med GnuPG) och deras integritet (via Hash) innan du installerar dem på din dator. Om du inte är säker på hur du gör det kan du följa den här andra handledningen:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Hur initialiserar man en Ledger Nano?


Anslut din Nano till din dator där Ledger Live och Sparrow wallet är installerade. För att navigera på din Ledger använder du vänsterknappen för att gå till vänster och högerknappen för att gå till höger. För att välja eller bekräfta ett alternativ trycker du på båda knapparna samtidigt.


![NANO S PLUS LEDGER](assets/notext/04.webp)


Bläddra igenom de olika introduktionssidorna och klicka sedan på de 2 knapparna för att börja.


![NANO S PLUS LEDGER](assets/notext/05.webp)


Välj alternativet "*Setup as a new device*".


![NANO S PLUS LEDGER](assets/notext/06.webp)


Välj den PIN-kod som ska användas för att låsa upp din Ledger. Detta är därför ett skydd mot obehörig fysisk åtkomst. Denna PIN-kod spelar ingen roll vid härledningen av din Wallet:s kryptografiska nycklar. Även utan tillgång till denna PIN-kod kan du alltså få tillgång till dina bitcoins om du har din Mnemonic-fras med 24 ord.


![NANO S PLUS LEDGER](assets/notext/07.webp)


Vi rekommenderar att du väljer en 8-siffrig PIN-kod som är så slumpmässig som möjligt. Se också till att spara den här koden på en annan plats än där din Ledger Nano S Plus lagras (t.ex. i en lösenordshanterare).


Använd knapparna för att flytta över siffrorna och välj sedan varje siffra genom att klicka på båda knapparna samtidigt.


![NANO S PLUS LEDGER](assets/notext/08.webp)


Ange din PIN-kod en gång till för att bekräfta den.


![NANO S PLUS LEDGER](assets/notext/09.webp)


Din Nano innehåller instruktioner om hur du hanterar din återställningsfras.


**Den här Mnemonic-frasen ger full och obegränsad tillgång till alla dina bitcoins**. Alla som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till din Ledger. Med 24-ordsfrasen kan du återställa åtkomsten till dina bitcoins i händelse av förlust, stöld eller skada på din Ledger Nano. Det är därför mycket viktigt att spara och förvara den på ett säkert ställe.


Du kan skriva ner det på pappret som medföljer din Ledger, eller för mer säkerhet rekommenderar jag att du graverar det på ett medium av rostfritt stål för att skydda mot risker för bränder, översvämningar eller kollapser.


Du kan bläddra i dessa instruktioner och hoppa över sidor genom att klicka på högerknappen.


![NANO S PLUS LEDGER](assets/notext/10.webp)

Ledger kommer att skapa din Mnemonic-fras med hjälp av sin slumptalsgenerator. Se till att du inte blir observerad under denna operation. Skriv ner de ord som Ledger tillhandahåller på det fysiska medium du väljer. Beroende på din säkerhetsstrategi kan du överväga att göra flera fullständiga fysiska kopior av frasen (men det är viktigt att du inte delar upp den). Det är viktigt att hålla orden numrerade och i sekventiell ordning.

***Självklart ska du aldrig dela dessa ord på internet, i motsats till vad jag gör i den här handledningen. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas efter handledningen.***


![NANO S PLUS LEDGER](assets/notext/11.webp)


För att gå till nästa ord klickar du på högerknappen.


![NANO S PLUS LEDGER](assets/notext/12.webp)


När alla ord har noterats klickar du på knapparna 2 för att gå vidare till nästa steg.


![NANO S PLUS LEDGER](assets/notext/13.webp)


Klicka på de två knapparna "*Confirm your Recovery phrase*" och välj sedan orden i din Mnemonic-fras i deras ordning för att bekräfta att du har noterat dem korrekt. Använd vänster- och högerknapparna för att navigera mellan alternativen och välj sedan rätt ord genom att klicka på de 2 knapparna. Fortsätt med detta till det 24:e ordet.


![NANO S PLUS LEDGER](assets/notext/14.webp)


Om den fras du bekräftar matchar exakt den som Ledger gav dig i föregående steg kan du fortsätta. Om inte, indikerar det att din fysiska säkerhetskopia av Mnemonic-frasen är felaktig och att du måste starta om processen.


![NANO S PLUS LEDGER](assets/notext/15.webp)


Och där har du det, din seed har skapats korrekt på din Ledger Nano S Plus. Innan du fortsätter att skapa en ny Bitcoin Wallet från denna seed, låt oss utforska enhetens inställningar tillsammans.


## Hur ändrar jag inställningarna för din Ledger?


För att komma åt inställningarna, håll ned knapparna 2 i några sekunder.


![NANO S PLUS LEDGER](assets/notext/16.webp)


Klicka på menyn "*Inställningar*".


![NANO S PLUS LEDGER](assets/notext/17.webp)


Välj sedan "*Generellt*".


![NANO S PLUS LEDGER](assets/notext/18.webp)


I menyn "*Language*" kan du ändra språket i teckenfönstret.


![NANO S PLUS LEDGER](assets/notext/19.webp)


I menyn "*Brightness*" kan du justera ljusstyrkan på skärmen. Vi är inte intresserade av resten av de allmänna inställningarna för tillfället.


![NANO S PLUS LEDGER](assets/notext/20.webp)


Gå nu till avsnittet "*Säkerhet*"-inställningar.


![NANO S PLUS LEDGER](assets/notext/21.webp)


med "*Change PIN*" kan du ändra din PIN-kod.

![NANO S PLUS LEDGER](assets/notext/22.webp)

"*passphrase*" gör att du kan ställa in en BIP39 passphrase. passphrase är ett valfritt lösenord som, i kombination med din återställningsfras, ger ytterligare en Layer säkerhet för din Wallet.


![NANO S PLUS LEDGER](assets/notext/23.webp)


För närvarande genereras din Wallet från en Mnemonic-fras som består av 24 ord. Denna återställningsfras är mycket viktig eftersom den gör det möjligt för dig att återställa alla nycklar i din Wallet om den skulle gå förlorad. Den utgör dock en enda punkt av misslyckande (SPOF). Om den äventyras är dina bitcoins i fara. Det är här passphrase kommer in i bilden. Det är ett valfritt lösenord, som du kan välja godtyckligt, som läggs till Mnemonic-frasen för att förbättra Wallet:s säkerhet.


passphrase ska inte förväxlas med PIN-koden. Den spelar en roll i härledningen av dina kryptografiska nycklar. Den fungerar tillsammans med Mnemonic-frasen och ändrar seed som nycklarna genereras från. Även om någon får tag på din 24-ordsfras, utan passphrase, kan de således inte komma åt dina pengar. Genom att använda en passphrase skapas i princip en ny Wallet med distinkta nycklar. Om passphrase modifieras (även något) kommer generate att bli en annan Wallet.


passphrase är ett mycket kraftfullt verktyg för att förbättra säkerheten för dina bitcoins. Det är dock mycket viktigt att förstå hur det fungerar innan du implementerar det, för att undvika att förlora åtkomsten till din Wallet. Det är därför jag råder dig att konsultera den här andra handledningen om du vill ställa in en passphrase på din Ledger:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

I menyn "*PIN lock*" kan du konfigurera och aktivera automatisk låsning av din Ledger efter en bestämd tid av inaktivitet.


![NANO S PLUS LEDGER](assets/notext/24.webp)


I menyn "*Skärmsläckare*" kan du justera viloläget för din Ledger Nano. Observera att skärmsläckaren inte kräver PIN-inmatning vid uppvaknandet, såvida inte alternativet "*PIN-lås*" är aktiverat för att motsvara viloläget. Denna funktion är särskilt användbar för Ledger Nano X-enheter som är utrustade med ett batteri, för att minska deras energiförbrukning.


![NANO S PLUS LEDGER](assets/notext/25.webp)


Slutligen kan du i menyn "*Reset device*" återställa din Ledger. Fortsätt endast med denna återställning om du är säker på att den inte innehåller några nycklar som säkrar bitcoins, eftersom du permanent kan förlora tillgången till dina pengar. Det här alternativet kan vara användbart för att utföra ett tomt återställningstest, men jag kommer att prata om detta lite mer senare.


![NANO S PLUS LEDGER](assets/notext/26.webp)

## Hur installerar man Bitcoin-applikationen?


Börja med att starta programvaran Ledger Live på din dator, anslut sedan och lås upp din Ledger Nano. I Ledger Live, gå till menyn "*My Ledger*". Du kommer att bli ombedd att godkänna åtkomst till din Nano.


![NANO S PLUS LEDGER](assets/notext/27.webp)


Bekräfta åtkomst på din Ledger genom att klicka på de två knapparna.


![NANO S PLUS LEDGER](assets/notext/28.webp)


Först, på Ledger Live, se till att "*Äkthetskontroll*" visas. Detta bekräftar att din enhet är äkta.


![NANO S PLUS LEDGER](assets/notext/29.webp)


Om den fasta programvaran för din Ledger Nano inte är uppdaterad kommer Ledger Live automatiskt att erbjuda dig att uppdatera den. Om det behövs, klicka på "*Uppdatera firmware*", sedan på "*Installera uppdatering*" för att starta installationen. På din Ledger klickar du på de två knapparna för att bekräfta och väntar sedan under installationen.


Slutligen kommer vi att lägga till Bitcoin-applikationen. För att göra detta, på Ledger Live, klicka på knappen "*Install*" bredvid "*Bitcoin (BTC)*".


![NANO S PLUS LEDGER](assets/notext/30.webp)


Programmet kommer att installeras på din Nano.


![NANO S PLUS LEDGER](assets/notext/31.webp)


Från och med nu behöver du inte längre programvaran Ledger Live för den regelbundna hanteringen av din Wallet. Du kan ibland återvända till den för att uppdatera den fasta programvaran när nya versioner finns tillgängliga. För allt annat kommer vi att använda Sparrow wallet, som är ett mycket mer omfattande verktyg för att effektivt hantera en Bitcoin Wallet.


![NANO S PLUS LEDGER](assets/notext/32.webp)


## Hur ställer man in en ny Bitcoin Wallet med Sparrow?


Öppna Sparrow wallet och hoppa över introduktionssidorna för att komma till startskärmen. Kontrollera att du är korrekt ansluten till en nod genom att titta på omkopplaren längst ned till höger på skärmen.


![NANO S PLUS LEDGER](assets/notext/33.webp)


Jag rekommenderar starkt att du använder din egen Bitcoin-nod. I den här handledningen använder jag en offentlig nod (gul) eftersom jag befinner mig på Testnet, men för normal användning är det bättre att välja en lokal Bitcoin Core (Green) eller en Electrum-server ansluten till en fjärrnod (blå).


Klicka på menyn "*File*" och sedan på "*New Wallet*".


![NANO S PLUS LEDGER](assets/notext/34.webp)


Välj ett namn för denna Wallet och klicka sedan på "*Create Wallet*".


![NANO S PLUS LEDGER](assets/notext/35.webp)


I rullgardinsmenyn "*Script Type*" väljer du vilken typ av script som ska användas för att säkra dina bitcoins. Jag rekommenderar att du väljer "*Taproot*", eller om det inte finns tillgängligt, "*Native SegWit*".


![NANO S PLUS LEDGER](assets/notext/36.webp)

Klicka på knappen "*Connected Hardware Wallet*".

![NANO S PLUS LEDGER](assets/notext/37.webp)


Om du inte redan har gjort det, anslut din Ledger Nano S Plus till datorn, lås upp den med din PIN-kod och öppna sedan programmet "*Bitcoin*" genom att klicka på de 2 knapparna en gång på Bitcoin-logotypen.


*I den här handledningen använder jag applikationen Bitcoin Testnet, men proceduren är densamma för Mainnet.*


![NANO S PLUS LEDGER](assets/notext/38.webp)


På Sparrow klickar du på knappen "*Scan*".


![NANO S PLUS LEDGER](assets/notext/39.webp)


Klicka sedan på "*Importera Keystore*".


![NANO S PLUS LEDGER](assets/notext/40.webp)


Du kan nu se detaljerna för din Wallet, inklusive den utökade publika nyckeln för ditt första konto. Klicka på knappen "*Apply*" för att slutföra skapandet av Wallet.


![NANO S PLUS LEDGER](assets/notext/41.webp)


Välj ett starkt lösenord för att säkra åtkomsten till Sparrow wallet. Detta lösenord säkerställer åtkomsten till dina Wallet-data på Sparrow, vilket hjälper till att skydda dina offentliga nycklar, adresser, etiketter och transaktionshistorik mot obehörig åtkomst.


Jag råder dig att spara det här lösenordet i en lösenordshanterare så att du inte glömmer det.


![NANO S PLUS LEDGER](assets/notext/42.webp)


Och där har du det, din Wallet är nu skapad!


![NANO S PLUS LEDGER](assets/notext/43.webp)


Innan du tar emot dina första bitcoins i din Wallet, **råder jag dig starkt att utföra ett återställningstest**. Anteckna en referensinformation, t.ex. din xpub, och återställ sedan din Ledger Nano medan Wallet fortfarande är tom. Försök sedan att återställa din Wallet på Ledger med hjälp av dina pappersbackuper. Kontrollera att den xpub som genereras efter återställningen matchar den som du ursprungligen noterade. Om så är fallet kan du vara säker på att dina pappersbackuper är tillförlitliga.


Om du vill veta mer om hur du utför ett återställningstest rekommenderar jag att du läser den här andra handledningen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hur tar man emot bitcoins med Ledger Nano?


Klicka på fliken "*Receive*".


![NANO S PLUS LEDGER](assets/notext/44.webp)


Anslut din Ledger Nano S Plus till datorn, lås upp den med din PIN-kod och öppna sedan programmet "*Bitcoin*".


![NANO S PLUS LEDGER](assets/notext/45.webp)

Innan du använder den Address som tillhandahålls av Sparrow wallet, verifiera den på din Ledger:s skärm. Denna metod gör att du kan bekräfta att den Address som visas på Sparrow inte är bedräglig och att Hardware Wallet verkligen har den privata nyckel som krävs för att spendera de bitcoins som säkrats med denna Address senare. Detta hjälper dig att undvika flera typer av attacker.

För att utföra denna verifiering klickar du på knappen "*Display Address*".


![NANO S PLUS LEDGER](assets/notext/46.webp)


Kontrollera att den Address som visas på din Ledger stämmer överens med den som anges på Sparrow wallet. Vi rekommenderar också att du utför denna verifiering precis innan du ger din Address till avsändaren, för att vara säker på att den är giltig. Du kan använda knapparna för att visa hela Address.


![NANO S PLUS LEDGER](assets/notext/47.webp)


Klicka sedan på "*Approve*" om adresserna verkligen är identiska.


![NANO S PLUS LEDGER](assets/notext/48.webp)


Du kan lägga till en "*Label*" för att beskriva källan till de bitcoins som kommer att säkras med denna Address. Detta är en bra praxis som hjälper dig att hantera dina UTXO:er bättre.


![NANO S PLUS LEDGER](assets/notext/49.webp)


För mer information om märkning rekommenderar jag dig också att kolla in den här andra handledningen:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Du kan sedan använda denna Address för att ta emot bitcoins.


![NANO S PLUS LEDGER](assets/notext/50.webp)


## Hur skickar man bitcoins med Ledger Nano?


Nu när du har fått din första Sats i din Wallet säkrad med Nano S Plus, kan du också spendera dem! Anslut din Ledger till din dator, lås upp den, starta Sparrow wallet och gå sedan till fliken "*Send*" för att skapa en ny transaktion.


![NANO S PLUS LEDGER](assets/notext/51.webp)


Om du vill göra "*coin control*", dvs. specifikt välja vilka UTXO:er som ska användas i transaktionen, går du till fliken "*UTXO*". Välj de UTXO:er du vill spendera och klicka sedan på "*Send Selected*". Du kommer att omdirigeras till samma skärm som på fliken "*Send*", men med dina UTXO:er redan valda för transaktionen.


![NANO S PLUS LEDGER](assets/notext/52.webp)


Ange destinationen Address. Du kan också ange flera adresser genom att klicka på knappen "*+ Lägg till*".


![NANO S PLUS LEDGER](assets/notext/53.webp)


Notera en "*Label*" för att komma ihåg syftet med denna utgift.


![NANO S PLUS LEDGER](assets/notext/54.webp)


Välj det belopp som ska skickas till denna Address.


![NANO S PLUS LEDGER](assets/notext/55.webp)


Justera transaktionsavgiften efter rådande marknadsläge.


![NANO S PLUS LEDGER](assets/notext/56.webp)

Kontrollera att alla inställningar för din transaktion är korrekta och klicka sedan på "*Create Transaction*".

![NANO S PLUS LEDGER](assets/notext/57.webp)


Om du tycker att allt ser bra ut klickar du på "*Finalize Transaction for Signing*".


![NANO S PLUS LEDGER](assets/notext/58.webp)


Klicka på "*Signera*".


![NANO S PLUS LEDGER](assets/notext/59.webp)


Klicka på "*Sign*" bredvid din Ledger Nano S Plus.


![NANO S PLUS LEDGER](assets/notext/60.webp)


Kontrollera transaktionsinställningarna på skärmen på din Ledger, inklusive mottagarens mottagande Address, det skickade beloppet och avgiftsbeloppet.


![NANO S PLUS LEDGER](assets/notext/61.webp)


Om du tycker att allt ser bra ut trycker du på de två knapparna på "*Signera transaktion*" för att signera.


![NANO S PLUS LEDGER](assets/notext/62.webp)


Din transaktion är nu signerad. Dubbelkolla att allt ser bra ut för dig och klicka sedan på "*Broadcast Transaction*" för att sända den i Bitcoin-nätverket.


![NANO S PLUS LEDGER](assets/notext/63.webp)


Du hittar den under fliken "*Transaktioner*" i Sparrow wallet.


![NANO S PLUS LEDGER](assets/notext/64.webp)


Grattis, nu har du fått koll på den grundläggande användningen av Ledger Nano S Plus med Sparrow wallet! I en framtida handledning kommer vi att se hur man använder Ledger med Liana för att utnyttja Miniscript.


Om du tyckte att den här handledningen var till hjälp skulle jag uppskatta om du kunde lämna tummen upp nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du kollar in den här fullständiga handledningen om Ledger Flex:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a