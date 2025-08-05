---
name: Satochip
description: Konfigurera och använda ett Satochip-smartkort
---
![cover](assets/cover.webp)


En Hardware Wallet är en elektronisk enhet som är avsedd att hantera och säkra de privata nycklarna för en Bitcoin Wallet. Till skillnad från mjukvaruplånböcker (eller Hot-plånböcker) som installeras på maskiner för allmänt bruk som ofta är anslutna till Internet, möjliggör hårdvaruplånböcker fysisk isolering av privata nycklar, vilket minskar riskerna för hackning och stöld.


Huvudsyftet med en Hardware Wallet är att minimera enhetens funktioner för att minska dess attackyta. En mindre attackyta innebär också färre potentiella attackvektorer, dvs. färre svagheter i systemet som angripare kan utnyttja för att komma åt bitcoins.


Vi rekommenderar att du använder en Hardware Wallet för att säkra dina bitcoins, särskilt om du innehar betydande belopp, oavsett om det är i absolut värde eller som en andel av dina totala tillgångar.


Hårdvaruplånböcker används i kombination med Wallet-hanteringsprogramvara på en dator eller smartphone. Denna programvara hanterar skapandet av transaktioner, men den kryptografiska signatur som krävs för att validera dessa transaktioner görs enbart inom Hardware Wallet. Detta innebär att de privata nycklarna aldrig exponeras för en potentiellt sårbar miljö.


Hårdvaruplånböcker erbjuder dubbelt skydd för användaren: å ena sidan skyddar de dina bitcoins mot fjärråttacker genom att hålla de privata nycklarna offline, och å andra sidan erbjuder de i allmänhet bättre fysiskt motstånd mot försök att extrahera nycklarna. Och det är just på dessa två säkerhetskriterier som man kan bedöma och rangordna de olika modellerna som finns på marknaden.


I den här handledningen föreslår jag att du upptäcker en av dessa lösningar: Satochip.


## Introduktion till Satochip


Satochip är en Hardware Wallet i form av ett kort med ett *EAL6+*-certifierat chip, vilket är en mycket hög säkerhetsstandard (*NXP JCOP*). Den tillverkas av ett belgiskt företag.


![SATOCHIP](assets/notext/01.webp)


Detta smarta kort säljs för 25 euro, vilket är mycket överkomligt jämfört med andra hårdvaruplånböcker på marknaden. Chipet är ett säkert element som garanterar mycket god motståndskraft mot fysiska attacker. Dessutom är dess kod öppen källkod (*AGPLv3*).

På grund av sitt format erbjuder Satochip dock inte lika många alternativ som annan hårdvara. Det finns naturligtvis inget batteri, ingen kamera och inte heller någon micro SD-kortläsare, eftersom det är ett kort. Dess största nackdel, enligt min mening, är avsaknaden av en skärm på Hardware Wallet, vilket gör den mer sårbar för vissa typer av fjärrattacker. Detta tvingar faktiskt användaren att signera blint och lita på vad de ser på sin datorskärm.


Trots sina begränsningar är Satochip fortfarande intressant på grund av sitt reducerade pris. Denna Wallet kan framför allt användas för att förbättra säkerheten för en spenderande Wallet utöver en sparande Wallet som skyddas av en Hardware Wallet utrustad med en skärm. Den utgör också en bra lösning för dem som innehar små mängder bitcoins och inte vill investera hundra euro i en mer sofistikerad enhet. Dessutom kan användningen av Satochips i Multisig-konfigurationer, eller potentiellt i Wallet-system med tidslås i framtiden, erbjuda intressanta fördelar.


Satochip-företaget erbjuder också två andra produkter. Det finns Satodime, som är ett innehavarkort som är utformat för att lagra bitcoins offline, men som inte tillåter transaktioner. Det är en slags pappers-Wallet som är mycket säkrare, som till exempel kan användas för att göra en gåva. Slutligen finns Seedkeeper, som är en Mnemonic frashanterare. Den kan användas för att på ett säkert sätt spara våra seed utan att de direkt noteras på ett papper.


## Hur köper man en Satochip?


Satochip finns till försäljning [på den officiella webbplatsen](https://satochip.io/product/satochip/). Om du vill köpa den i en fysisk butik kan du också hitta [listan över certifierade återförsäljare](https://satochip.io/resellers/) på Satochips webbplats.


För att interagera med din Wallet-hanteringsprogramvara erbjuder Satochip två möjligheter: genom NFC-kommunikation eller via en smartkortsläsare. För NFC-alternativet måste du se till att din maskin är kompatibel med denna teknik eller skaffa en extern NFC-läsare. Satochip arbetar med standardfrekvensen 13,56 MHz. Annars kan du också köpa en smartkortsläsare. Du kan hitta en sådan på Satochips webbplats eller någon annanstans.


![SATOCHIP](assets/notext/02.webp)


## Hur ställer man in en Satochip med Sparrow?


När du har fått din Satochip är det första steget att undersöka förpackningen för att säkerställa att den inte har öppnats. Satochip-förpackningen ska innehålla en förseglingsklisterlapp. Om detta klistermärke saknas eller är skadat kan det tyda på att smartkortet har äventyrats och kanske inte är äkta.

![SATOCHIP](assets/notext/03.webp)

Du kommer att hitta Satochip inuti.


![SATOCHIP](assets/notext/04.webp)


För att hantera Wallet, i denna handledning, föreslår jag att du använder Sparrow. Om du ännu inte har programvaran kan du [besöka den officiella webbplatsen för att ladda ner den](https://sparrowwallet.com/download/). Du kan också kolla in vår handledning om Sparrow wallet (kommer snart).


![SATOCHIP](assets/notext/05.webp)


Sätt in din Satochip i smartkortläsaren eller placera den på NFC-läsaren och anslut läsaren till din dator där Sparrow är öppen.


![SATOCHIP](assets/notext/06.webp)


Öppna Sparrow wallet och se till att du är korrekt ansluten till en Bitcoin-nod. För att göra detta, kontrollera krysset längst ner till höger: det ska vara gult om du är ansluten till en offentlig nod, Green för en anslutning till Bitcoin Core, eller blått för Electrum.


![SATOCHIP](assets/notext/07.webp)


På Sparrow wallet klickar du på fliken "*File*".


![SATOCHIP](assets/notext/08.webp)


Sedan på menyn "*Ny Wallet*".


![SATOCHIP](assets/notext/09.webp)


Välj ett namn för din Wallet och klicka sedan på "*Create Wallet*".


![SATOCHIP](assets/notext/10.webp)


Klicka på knappen "*Connected Hardware Wallet*".


![SATOCHIP](assets/notext/11.webp)


Klicka på knappen "*Scan...*".


![SATOCHIP](assets/notext/12.webp)


Din Satochip bör visas. Klicka på "*Importera Keystore*".


![SATOCHIP](assets/notext/13.webp)


Därefter måste du ange en PIN-kod för att låsa upp din Satochip. Välj ett starkt lösenord, mellan 4 och 16 tecken. Gör en säkerhetskopia av detta lösenord.


Tänk på att detta lösenord inte är en passphrase. Detta innebär att även utan detta lösenord kommer din Mnemonic-fras att göra det möjligt för dig att återimportera din Wallet till programvara vid behov. Lösenordet används endast för att säkra åtkomsten till själva Satochip. Det motsvarar den PIN-kod som finns på andra hårdvaruplånböcker.


När lösenordet har angetts klickar du igen på knappen "*Import Keystore*".


![SATOCHIP](assets/notext/14.webp)


Anteckna lösenordet igen och klicka sedan på knappen "*Initialize*".


![SATOCHIP](assets/notext/15.webp)


Du kommer då till fönstret för att skapa din Mnemonic-fras. Klicka på knappen "*generate Ny*".


![SATOCHIP](assets/notext/16.webp)

Gör en eller flera fysiska kopior av din återställningsfras genom att skriva ner den på ett pappers- eller metallmedium. Var medveten om att denna fras ger full tillgång till dina bitcoins utan något ytterligare skydd. Om någon skulle upptäcka den kan de därför omedelbart stjäla dina bitcoins, även utan tillgång till din Satochip eller dess PIN-kod. Det är därför viktigt att säkra dessa säkerhetskopior. Dessutom gör denna fras att du kan återfå tillgång till dina bitcoins i händelse av förlust, skada på Satochip eller om du glömmer din PIN-kod.

![SATOCHIP](assets/notext/17.webp)


Din Bitcoin Wallet har skapats framgångsrikt.


![SATOCHIP](assets/notext/18.webp)


Klicka igen på knappen "*Import Keystore*".


![SATOCHIP](assets/notext/19.webp)


Din Wallet är nu skapad. Dina privata nycklar är nu lagrade på smartkortet i din Satochip. Klicka på knappen "*Apply*" för att fortsätta.


![SATOCHIP](assets/notext/20.webp)


Vi rekommenderar att du ställer in ett extra lösenord för att säkra den offentliga information som hanteras av Sparrow wallet, utöver PIN-koden för din Satochip. Detta lösenord kommer att säkerställa säkerheten för åtkomst till Sparrow wallet, vilket hjälper till att skydda dina offentliga nycklar, adresser och transaktionshistorik mot obehörig åtkomst.


![SATOCHIP](assets/notext/21.webp)


Ange ditt lösenord i de två fälten och klicka sedan på knappen "*Set Password*".


![SATOCHIP](assets/notext/22.webp)


Och där har du det, din Satochip är nu konfigurerad på Sparrow wallet.


![SATOCHIP](assets/notext/23.webp)


Nu när din Wallet är skapad kan du koppla bort din Satochip. Förvara den på en säker plats!


## Hur tar man emot bitcoins med Satochip?


När du är i din Wallet klickar du på fliken "*Receive*".


![SATOCHIP](assets/notext/24.webp)


Sparrow wallet genererar en Address för din Wallet. För andra hårdvaruplånböcker rekommenderas det vanligtvis att klicka på "*Display Address*" för att verifiera Address direkt på enhetens skärm. Tyvärr är detta alternativ inte tillgängligt med Satochip, men se till att använda det för dina andra plånböcker.


![SATOCHIP](assets/notext/25.webp)


Du kan lägga till en "*Label*" för att beskriva källan till de bitcoins som kommer att säkras med denna Address. Detta är en bra praxis som hjälper dig att bättre hantera dina UTXO:er.


![SATOCHIP](assets/notext/26.webp)


För mer information om märkning rekommenderar jag också att du tittar på den här andra handledningen:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Du kan sedan använda denna Address för att ta emot bitcoins.


![SATOCHIP](assets/notext/27.webp)

## Hur skickar jag Bitcoins med Satochip?

Nu när du har fått dina första Sats i din säkra Wallet med Satochip kan du också spendera dem! Anslut din Satochip till din dator, starta Sparrow wallet och gå sedan till fliken "*Sänd*" för att skapa en ny transaktion.


![SATOCHIP](assets/notext/28.webp)


Om du vill utföra myntkontroll, dvs. specifikt välja vilka UTXO som ska användas i transaktionen, ska du gå till fliken "*UTXO*". Välj de UTXO som du vill använda och klicka sedan på "*Send Selected*". Du kommer att omdirigeras till samma skärm som på fliken "*Send*", men med dina UTXO:er redan valda för transaktionen.


![SATOCHIP](assets/notext/29.webp)


Ange destinationen Address. Du kan också ange flera adresser genom att klicka på knappen "*+ Lägg till*".


![SATOCHIP](assets/notext/30.webp)


Notera en "*Label*" för att komma ihåg syftet med denna utgift.


![SATOCHIP](assets/notext/31.webp)


Välj det belopp som ska skickas till denna Address.


![SATOCHIP](assets/notext/32.webp)


Justera avgiftssatsen för din transaktion enligt den aktuella marknaden.


![SATOCHIP](assets/notext/33.webp)


Se till att alla parametrar för din transaktion är korrekta och klicka sedan på "*Create Transaction*".


![SATOCHIP](assets/notext/34.webp)


Om allt är till belåtenhet klickar du på "*Finalize Transaction for Signing*".


![SATOCHIP](assets/notext/35.webp)


Klicka på "*Signera*".


![SATOCHIP](assets/notext/36.webp)


Klicka på "*Signera*" igen bredvid ditt Satochip.


![SATOCHIP](assets/notext/37.webp)


Ange PIN-koden för din Satochip och klicka sedan på "*Sign*" igen för att signera din transaktion.


![SATOCHIP](assets/notext/38.webp)


Din transaktion är nu signerad. Klicka på "*Broadcast Transaction*" för att sända den till Bitcoin-nätverket.


![SATOCHIP](assets/notext/39.webp)


Du hittar den under fliken "*Transaktioner*" i Sparrow wallet.


![SATOCHIP](assets/notext/40.webp)


Grattis, du vet nu hur man använder Satochip! Om du tyckte att den här handledningen var till hjälp skulle jag uppskatta en tumme upp nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!