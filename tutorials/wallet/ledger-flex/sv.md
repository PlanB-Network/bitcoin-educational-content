---
name: Ledger Flex
description: Konfigurera och använda Ledger Flex
---
![cover](assets/cover.webp)


En Hardware Wallet är en elektronisk enhet som är avsedd att hantera och säkra de privata nycklarna för en Bitcoin Wallet. Till skillnad från mjukvaruplånböcker (eller Hot-plånböcker) som installeras på maskiner för allmänt bruk som ofta är anslutna till Internet, möjliggör hårdvaruplånböcker fysisk isolering av privata nycklar, vilket minskar riskerna för hackning och stöld.


Huvudmålet med en Hardware Wallet är att minimera enhetens funktioner för att minska dess attackyta. Mindre attackyta innebär också färre potentiella attackvektorer, dvs. färre svaga punkter i systemet som angripare kan utnyttja för att komma åt bitcoins.


Vi rekommenderar att du använder en Hardware Wallet för att säkra dina bitcoins, särskilt om du innehar betydande belopp, oavsett om det är i absolut värde eller som en andel av dina totala tillgångar.


Hårdvaruplånböcker används i kombination med Wallet-hanteringsprogramvara på en dator eller smartphone. Denna programvara hanterar skapandet av transaktioner, men den kryptografiska signatur som krävs för att validera dessa transaktioner görs endast inom Hardware Wallet. Detta innebär att de privata nycklarna aldrig exponeras för en potentiellt sårbar miljö.


Hårdvaruplånböcker erbjuder dubbelt skydd för användaren: å ena sidan skyddar de dina bitcoins mot fjärråttacker genom att hålla de privata nycklarna offline, och å andra sidan erbjuder de i allmänhet bättre fysiskt motstånd mot försök att extrahera nycklarna. Och det är just på dessa två säkerhetskriterier som man kan bedöma och rangordna de olika modellerna som finns på marknaden.


I den här handledningen föreslår jag att du upptäcker en av dessa lösningar: **Ledger Flex**.


![LEDGER FLEX](assets/notext/01.webp)


## Introduktion till Ledger Flex


Ledger Flex är en Hardware Wallet som tillverkas av det franska företaget Ledger och marknadsförs till ett pris av 249 €.


![LEDGER FLEX](assets/notext/02.webp)


Den har en stor E Ink-pekskärm, en svartvit displayteknik. Det är samma teknik som används i elektroniska läsare. E Ink-skärmen ger en tydlig och läsbar display, även i starkt solljus, och förbrukar mycket lite energi, eller ingen alls när skärmen är statisk. Den fungerar genom att använda mikrokapslar som innehåller svarta och vita pigmentpartiklar. När en elektrisk laddning appliceras flyttar sig de svarta eller vita partiklarna till skärmens yta, vilket gör att text eller bilder kan formas.

Ledger Flex är utrustad med ett CC EAL6+-certifierat "secure element"-chip, vilket ger dig avancerat skydd mot fysiska attacker på hårdvaran. Skärmen styrs direkt av detta chip. En vanlig kritikpunkt är att koden för detta chip inte är öppen källkod, vilket kräver en viss nivå av förtroende för integriteten hos denna komponent. Detta element granskas dock av oberoende experter.


När det gäller användning erbjuder Ledger Flex flera anslutningsmöjligheter: Bluetooth, USB-C och NFC. Den stora skärmen gör det enkelt att verifiera dina transaktionsuppgifter. Ledger sticker också ut från sina konkurrenter med sitt snabba införande av nya Bitcoin-funktioner, som till exempel Miniscript.


Efter att ha testat den är jag imponerad av produktens kvalitet. Användarupplevelsen är utmärkt och enheten är intuitiv. Det är en utmärkt Hardware Wallet. Det har dock två stora nackdelar enligt min mening: oförmågan att verifiera chipets kod och naturligtvis dess pris, vilket är betydligt högre än konkurrenterna. Som jämförelse säljs den mest avancerade modellen från Foundation för 199 dollar, Coinkites för 219,99 dollar, medan den senaste Trezor, som också är utrustad med en stor pekskärm, erbjuds för 169 euro.


## Hur köper man en Ledger Flex?


Ledger Flex finns att köpa [på den officiella webbplatsen](https://shop.Ledger.com/pages/Ledger-flex). Om du vill köpa den i en fysisk butik kan du också hitta [listan över certifierade återförsäljare](https://www.Ledger.com/reseller) på Ledger:s webbplats.


## Förkunskapskrav


När du har fått din Ledger Flex är det första steget att undersöka förpackningen för att säkerställa att den inte har öppnats.


![LEDGER FLEX](assets/notext/03.webp)


Ledger:s förpackning ska innehålla 2 förseglingsremsor. Om dessa remsor saknas eller är skadade kan det tyda på att Hardware Wallet har äventyrats och kanske inte är äkta.


![LEDGER FLEX](assets/notext/04.webp)


Vid öppnandet bör du hitta följande föremål i lådan:


- Ledger Flex;
- En USB-C-kabel;
- En användarmanual;
- Kort för att skriva ner din Mnemonic-fras.


![LEDGER FLEX](assets/notext/05.webp)


För den här handledningen behöver du 2 programvaror: Ledger Live för att initiera Ledger Flex, och Sparrow Wallet för att hantera din Bitcoin Wallet. Ladda ner [Ledger Live](https://www.Ledger.com/Ledger-live) och [Sparrow Wallet](https://sparrowwallet.com/download/) från deras officiella webbplatser.


![LEDGER FLEX](assets/notext/06.webp)

Vi kommer snart att erbjuda en handledning om hur man verifierar äktheten och integriteten hos programvara som du laddar ner. Jag rekommenderar starkt att du gör det här för Ledger Live och Sparrow.

## Hur initialiserar jag en Ledger Flex med Ledger Live?


Slå på din Ledger Flex genom att trycka på höger sidoknapp i några sekunder.


![LEDGER FLEX](assets/notext/07.webp)


Bläddra igenom de olika introduktionssidorna.


![LEDGER FLEX](assets/notext/08.webp)


Välj alternativet "*Set up without Ledger Live*" och klicka sedan på knappen "*Skip Ledger Live*".


![LEDGER FLEX](assets/notext/09.webp)


Du kommer då att bli ombedd att välja ett namn för din Ledger. Klicka på "*Set name*" och ange sedan det namn du vill ha.


![LEDGER FLEX](assets/notext/10.webp)


Välj PIN-koden för din enhet, som kommer att användas för att låsa upp din Ledger. Detta är därför ett skydd mot obehörig fysisk åtkomst. Denna PIN-kod spelar ingen roll vid härledningen av din Wallet:s kryptografiska nycklar. Även om du inte har tillgång till PIN-koden kan du alltså få tillgång till dina bitcoins om du har din Mnemonic-fras med 24 ord.


Vi rekommenderar att du väljer en 8-siffrig PIN-kod som är så slumpmässig som möjligt. Se också till att spara den här koden på en annan plats än där din Ledger Flex lagras (till exempel i en lösenordshanterare).


![LEDGER FLEX](assets/notext/11.webp)


Ange din PIN-kod en gång till för att bekräfta den.


![LEDGER FLEX](assets/notext/12.webp)


Du kommer sedan att uppmanas att välja mellan att återställa en befintlig Wallet eller skapa en ny. I den här handledningen går vi igenom hur du skapar en ny Wallet från grunden, så välj alternativet "*Set up as a new Ledger*" för att skapa en ny Mnemonic-fras.


![LEDGER FLEX](assets/notext/13.webp)


Din Flex kommer att ge instruktioner om hur du hanterar din återställningsfras.


**Den här Mnemonic-frasen ger fullständig och obegränsad tillgång till alla dina bitcoins**. Alla som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till din Ledger. Frasen på 24 ord gör det möjligt att återställa åtkomsten till dina bitcoins vid förlust, stöld eller skada på din Ledger Flex. Det är därför mycket viktigt att spara och förvara den på en säker plats.


Du kan skriva ner det på pappret som medföljer din Ledger, eller för extra säkerhet rekommenderar jag att du graverar det på ett medium av rostfritt stål för att skydda mot risker för bränder, översvämningar eller kollapser.


Du kan bläddra i dessa instruktioner och hoppa över sidor genom att peka på skärmen.


![LEDGER FLEX](assets/notext/14.webp)

Ledger kommer att skapa din Mnemonic-fras med hjälp av sin slumptalsgenerator. Se till att du inte blir observerad under denna operation. Skriv ner de ord som Ledger tillhandahåller på det fysiska medium du väljer. Beroende på din säkerhetsstrategi kan du överväga att göra flera fullständiga fysiska kopior av frasen (men viktigast av allt, dela inte upp den). Det är viktigt att hålla orden numrerade och i sekventiell ordning.

***Självklart ska du aldrig dela dessa ord på internet, i motsats till vad jag gör i den här handledningen. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.***


![LEDGER FLEX](assets/notext/15.webp)


För att gå till nästa ordgrupp, klicka på knappen "*Nästa*". När alla ord har antecknats klickar du på knappen "*Done*" för att gå vidare till nästa steg.


![LEDGER FLEX](assets/notext/16.webp)


Klicka på knappen "*Startbekräftelse*" och välj sedan orden i din Mnemonic-fras i deras ordning för att bekräfta att du har noterat dem korrekt. Fortsätt med denna procedur till det 24:e ordet.


![LEDGER FLEX](assets/notext/17.webp)


Om den fras du bekräftar exakt matchar den som Flex gav dig i föregående steg kan du fortsätta. Om inte, indikerar detta att din fysiska säkerhetskopia av Mnemonic-frasen är felaktig och att du måste starta om processen.


![LEDGER FLEX](assets/notext/18.webp)


Och där har du det, din seed har skapats korrekt på din Ledger Flex. Innan du fortsätter att skapa en ny Bitcoin Wallet från denna seed, låt oss utforska enhetsinställningarna tillsammans.


## Hur ändrar jag inställningarna för din Ledger?


För att låsa och låsa upp din Ledger trycker du på sidoknappen. Du ombeds då att ange den PIN-kod som du ställde in i föregående steg.


![LEDGER FLEX](assets/notext/19.webp)


För att komma åt inställningarna klickar du på kugghjulssymbolen längst ned till vänster på din enhet.


![LEDGER FLEX](assets/notext/20.webp)


I menyn "*Namn*" kan du ändra namnet på din Ledger.


![LEDGER FLEX](assets/notext/21.webp)


I "*Om denna Ledger*" hittar du information om din Flex.


![LEDGER FLEX](assets/notext/22.webp)


I menyn "*Låsskärm*" har du möjlighet att ändra bilden som visas på låsskärmen genom att välja "*Anpassa låsskärmsbild*". Tack vare enhetens E Ink-skärmteknik är det möjligt att hålla skärmen ständigt påslagen utan att batteriet förbrukas. E Ink-skärmar förbrukar inte energi för att upprätthålla en statisk bild. De förbrukar dock energi när bilden ändras.

I undermenyn "*Auto-lock*" kan du konfigurera och aktivera automatisk låsning av din Ledger efter en viss tid av inaktivitet.

![LEDGER FLEX](assets/notext/23.webp)


I menyn "*Sounds*" kan du slå på eller av ljuden i din Flex. Och i menyn "Language" kan du ändra displayens språk.


![LEDGER FLEX](assets/notext/24.webp)


Genom att klicka på högerpilen kan du komma åt andra inställningar. "*Change PIN*" ger dig möjlighet att ändra din PIN-kod.


![LEDGER FLEX](assets/notext/25.webp)


Med menyerna "*Bluetooth*" och "*NFC*" kan du hantera denna kommunikation.


![LEDGER FLEX](assets/notext/26.webp)


I "*Battery*" kan du särskilt ställa in en automatisk avstängning av Ledger.


![LEDGER FLEX](assets/notext/27.webp)


Avsnittet "*Advanced*" ger dig tillgång till mer sofistikerade säkerhetsinställningar. Vi rekommenderar att du låter alternativet "*PIN shuffle*" vara aktiverat för att öka säkerheten. Det är också i den här menyn som du kan konfigurera en BIP39 passphrase.


![LEDGER FLEX](assets/notext/28.webp)


passphrase är ett valfritt lösenord som, i kombination med återställningsfrasen, ger ytterligare Layer säkerhet för din Wallet.


För närvarande genereras din Wallet från en Mnemonic-fras som består av 24 ord. Denna återställningsfras är mycket viktig, eftersom den gör att du kan återställa alla nycklar i din Wallet om den skulle gå förlorad. Den utgör dock en enda felkälla (single point of failure, SPOF). Om den äventyras är bitcoins i fara. Det är här passphrase kommer in i bilden. Det är ett valfritt lösenord, som du kan välja godtyckligt, som läggs till Mnemonic-frasen för att stärka Wallet:s säkerhet.


passphrase ska inte förväxlas med PIN-koden. Den spelar en roll i härledningen av dina kryptografiska nycklar. Den fungerar tillsammans med Mnemonic-frasen och modifierar seed som nycklarna genereras från. Även om någon får tag på din 24-ordsfras kan de alltså inte komma åt dina pengar utan passphrase. Genom att använda en passphrase skapas i princip en ny Wallet med distinkta nycklar. Om passphrase modifieras (även något) kommer generate att bli en annan Wallet.


passphrase är ett mycket kraftfullt verktyg för att förbättra säkerheten för dina bitcoins. Det är dock mycket viktigt att förstå hur det fungerar innan du implementerar det, för att undvika att förlora åtkomsten till din Wallet. Jag kommer att förklara hur man använder passphrase i en annan dedikerad handledning.


![LEDGER FLEX](assets/notext/29.webp)


passphrase är ett mycket kraftfullt verktyg för att stärka säkerheten för dina bitcoins. Det är dock viktigt att förstå hur det fungerar innan du implementerar det, för att undvika att förlora åtkomsten till din Wallet. Det är därför jag förklarar allt i en dedikerad handledning:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Slutligen kan du på den sista inställningssidan återställa din Ledger. Fortsätt bara med denna återställning om du är säker på att den inte innehåller några nycklar som säkrar bitcoins, eftersom du permanent kan förlora tillgången till dina pengar.

![LEDGER FLEX](assets/notext/30.webp)


## Hur installerar man Bitcoin-applikationen?


Börja med att starta Ledger Live-programvaran på din dator, anslut sedan och lås upp din Ledger Flex.


![LEDGER FLEX](assets/notext/31.webp)


I Ledger Live går du till menyn "*My Ledger*". Du kommer att bli ombedd att godkänna åtkomst till din Flex.


![LEDGER FLEX](assets/notext/32.webp)


Bekräfta åtkomsten på din Ledger genom att klicka på knappen "*Allow*".


![LEDGER FLEX](assets/notext/33.webp)


Först, om den fasta programvaran i din Ledger Flex inte är uppdaterad, kommer Ledger Live automatiskt att erbjuda att uppdatera den. Om tillämpligt, klicka på "*Uppdatera firmware*", sedan på "*Installera uppdatering*" för att starta installationen.


![LEDGER FLEX](assets/notext/34.webp)


På din Ledger klickar du på knappen "*Install*" och väntar sedan under installationen.


![LEDGER FLEX](assets/notext/35.webp)


Den fasta programvaran för din Ledger Flex är nu uppdaterad.


![LEDGER FLEX](assets/notext/36.webp)


Om du vill kan du ändra bakgrundsbild för låsskärmen på din Ledger Flex. För att göra detta, klicka på "*Add >*".


![LEDGER FLEX](assets/notext/37.webp)


Klicka på knappen "*Ladda upp från datorn*" och välj din bakgrundsbild från dina foton.


![LEDGER FLEX](assets/notext/38.webp)


Du kan beskära din bild.


![LEDGER FLEX](assets/notext/39.webp)


Välj en kontrast bland de olika alternativen och klicka sedan på "*Bekräfta kontrast*".


![LEDGER FLEX](assets/notext/40.webp)


Klicka på knappen "*Ladda bild*" på din Flex.


![LEDGER FLEX](assets/notext/41.webp)


Om du är nöjd med bilden klickar du på "*Keep*" för att ställa in den som bakgrundsbild på din låsskärm.


![LEDGER FLEX](assets/notext/42.webp)


Slutligen kommer vi att lägga till Bitcoin-applikationen. För att göra detta, på Ledger Live, klicka på knappen "*Install*" bredvid "*Bitcoin (BTC)*".


![LEDGER FLEX](assets/notext/43.webp)


Programmet kommer att installeras på din Flex.


![LEDGER FLEX](assets/notext/44.webp)


Från och med nu behöver du inte längre programvaran Ledger Live för den regelbundna hanteringen av din Wallet. Du kan återvända till den ibland för att uppdatera den fasta programvaran när nya versioner finns tillgängliga. För allt annat kommer vi att använda Sparrow Wallet, som är ett mycket mer omfattande verktyg för effektiv hantering av en Bitcoin Wallet.


## Hur ställer man in en ny Bitcoin Wallet med Sparrow?

Öppna Sparrow Wallet och hoppa över introduktionssidorna för att komma till startskärmen. Kontrollera att du är korrekt ansluten till en nod genom att titta på omkopplaren längst ned till höger på skärmen.

![LEDGER FLEX](assets/notext/45.webp)


Jag rekommenderar starkt att du använder din egen Bitcoin-nod. I den här handledningen använder jag en offentlig nod (gul) eftersom jag befinner mig på Testnet, men för normal användning är det bättre att välja en lokal Bitcoin Core (Green) eller en Electrum-server ansluten till en fjärrnod (blå).


Klicka på menyn "*File*" och sedan på "*New Wallet*".


![LEDGER FLEX](assets/notext/46.webp)


Välj ett namn för denna Wallet och klicka sedan på "*Create Wallet*".


![LEDGER FLEX](assets/notext/47.webp)


I rullgardinsmenyn "*Script Type*" väljer du vilken typ av script som ska användas för att säkra dina bitcoins. Jag rekommenderar att du väljer "*Taproot*", eller om det inte finns tillgängligt, "*Native SegWit*".


![LEDGER FLEX](assets/notext/48.webp)


Klicka på knappen "*Connected Hardware Wallet*".


![LEDGER FLEX](assets/notext/49.webp)


Anslut din Ledger Flex till datorn, lås upp den med din PIN-kod och öppna sedan programmet "*Bitcoin*". I den här handledningen använder jag applikationen "*Bitcoin Testnet*", men proceduren är densamma för Mainnet.


![LEDGER FLEX](assets/notext/50.webp)


På Sparrow klickar du på knappen "*Scan*".


![LEDGER FLEX](assets/notext/51.webp)


Klicka sedan på "*Importera Keystore*".


![LEDGER FLEX](assets/notext/52.webp)


Du kan nu se detaljerna för din Wallet, inklusive den utökade publika nyckeln för ditt första konto. Klicka på knappen "*Apply*" för att slutföra skapandet av Wallet.


![LEDGER FLEX](assets/notext/53.webp)


Välj ett starkt lösenord för att säkra åtkomsten till Sparrow Wallet. Detta lösenord säkerställer åtkomsten till dina Wallet-data på Sparrow, vilket hjälper till att skydda dina offentliga nycklar, adresser, etiketter och transaktionshistorik mot obehörig åtkomst.


Jag råder dig att spara det här lösenordet i en lösenordshanterare så att du inte glömmer det.


![LEDGER FLEX](assets/notext/54.webp)


Och där har du det, din Wallet är nu skapad!


![LEDGER FLEX](assets/notext/55.webp)

Innan du får dina första bitcoins i din Wallet rekommenderar jag starkt att du utför ett återställningstest med torrkörning. Anteckna en referensinformation, t.ex. din xpub, och återställ sedan din Ledger Flex medan Wallet fortfarande är tom. Försök därefter att återställa din Wallet på Ledger med hjälp av dina pappersbackuper. Kontrollera att den xpub som genereras efter återställningen matchar den som du ursprungligen noterade. Om så är fallet kan du vara säker på att dina pappersbackuper är tillförlitliga.


## Hur tar man emot bitcoins med Ledger Flex?


Klicka på fliken "*Receive*".


![LEDGER FLEX](assets/notext/56.webp)


Anslut din Ledger Flex till datorn, lås upp den med din PIN-kod och öppna sedan programmet "*Bitcoin*".


![LEDGER FLEX](assets/notext/57.webp)


Innan du använder den Address som tillhandahålls av Sparrow Wallet ska du verifiera den på skärmen på din Ledger Flex. Denna metod gör att du kan bekräfta att Address som visas på Sparrow inte är bedräglig och att Ledger verkligen har den privata nyckel som krävs för att spendera bitcoins som säkrats med denna Address senare.


För att utföra denna verifiering klickar du på knappen "*Display Address*".


![LEDGER FLEX](assets/notext/58.webp)


Kontrollera att den Address som visas på din Ledger Flex stämmer överens med den som anges på Sparrow Wallet. Vi rekommenderar också att du utför denna verifiering precis innan du ger din Address till avsändaren, för att vara säker på att den är giltig.


![LEDGER FLEX](assets/notext/59.webp)


Du kan lägga till en "*Label*" för att beskriva källan till de bitcoins som kommer att säkras med denna Address. Detta är en bra praxis som hjälper dig att bättre hantera dina UTXO:er.


![LEDGER FLEX](assets/notext/60.webp)


För mer information om märkning rekommenderar jag dig också att kolla in den här andra handledningen:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Du kan sedan använda denna Address för att ta emot bitcoins.


![LEDGER FLEX](assets/notext/61.webp)


## Hur skickar jag bitcoins med Ledger Flex?


Nu när du har fått dina första Sats i din Wallet säkrad med Flex, kan du också spendera dem! Anslut din Ledger till din dator, lås upp den, starta Sparrow Wallet och gå sedan till fliken "*Send*" för att skapa en ny transaktion.


![LEDGER FLEX](assets/notext/62.webp)


Om du vill göra "*coin control*", det vill säga specifikt välja vilka UTXO:er som ska användas i transaktionen, går du till fliken "*UTXO:er*". Välj de UTXO:er du vill spendera och klicka sedan på "*Send Selected*". Du kommer att omdirigeras till samma skärm som på fliken "*Send*", men med dina UTXO:er redan valda för transaktionen.

![LEDGER FLEX](assets/notext/63.webp)

Ange destinationen Address. Du kan också ange flera adresser genom att klicka på knappen "*+ Lägg till*".


![LEDGER FLEX](assets/notext/64.webp)


Notera en "*Label*" för att komma ihåg syftet med denna kostnad.


![LEDGER FLEX](assets/notext/65.webp)


Välj det belopp som ska skickas till denna Address.


![LEDGER FLEX](assets/notext/66.webp)


Justera avgiftssatsen för din transaktion enligt den aktuella marknaden.


![LEDGER FLEX](assets/notext/67.webp)


Kontrollera att alla inställningar för din transaktion är korrekta och klicka sedan på "*Create Transaction*".


![LEDGER FLEX](assets/notext/68.webp)


Om allt är till belåtenhet klickar du på "*Finalize Transaction for Signing*".


![LEDGER FLEX](assets/notext/69.webp)


Klicka på "*Signera*".


![LEDGER FLEX](assets/notext/70.webp)


Klicka på "*Sign*" bredvid din Ledger Flex.


![LEDGER FLEX](assets/notext/71.webp)


Kontrollera transaktionsinställningarna på skärmen på din Flex, inklusive mottagarens mottagande Address, det skickade beloppet och avgiftsbeloppet.


![LEDGER FLEX](assets/notext/72.webp)


För att signera håller du fingret på knappen "*Håll för att signera*".


![LEDGER FLEX](assets/notext/73.webp)


Din transaktion är nu signerad. Klicka på "*Broadcast Transaction*" för att sända den i Bitcoin-nätverket.


![LEDGER FLEX](assets/notext/74.webp)


Du hittar den under fliken "*Transaktioner*" i Sparrow Wallet.


![LEDGER FLEX](assets/notext/75.webp)


Gratulerar, du har nu lärt dig den grundläggande användningen av Ledger Flex med Sparrow Wallet! I en framtida handledning kommer vi att se hur man använder Ledger Flex med Liana för att utnyttja Miniscript.


Om du tyckte att den här handledningen var till hjälp skulle jag uppskatta tummen upp nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!