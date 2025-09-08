---
name: Tapsigner
description: Konfigurera och använda en Tapsigner med Nunchuk
---
![cover](assets/cover.webp)


En Hardware Wallet är en elektronisk enhet som är avsedd för hantering och säkerhet av en Bitcoin Wallet:s privata nycklar. Till skillnad från mjukvaruplånböcker (eller Hot-plånböcker) som installeras på maskiner för allmänt bruk som ofta är anslutna till Internet, möjliggör hårdvaruplånböcker fysisk isolering av privata nycklar, vilket minskar riskerna för hackning och stöld.


Huvudsyftet med en Hardware Wallet är att minimera enhetens funktioner för att minska dess attackyta. En mindre attackyta innebär också färre potentiella attackvektorer, dvs. färre svaga punkter i systemet som angripare kan utnyttja för att komma åt bitcoins.


Vi rekommenderar att du använder en Hardware Wallet för att säkra dina bitcoins, särskilt om du innehar betydande belopp, oavsett om det är i absolut värde eller som en andel av dina totala tillgångar.


Hårdvaruplånböcker används i kombination med en Wallet-hanteringsprogramvara på en dator eller smartphone. Denna programvara hanterar skapandet av transaktioner, men den kryptografiska signatur som krävs för att validera dessa transaktioner görs enbart inom Hardware Wallet. Detta innebär att de privata nycklarna aldrig exponeras för en potentiellt sårbar miljö.


Hårdvaruplånböcker erbjuder dubbelt skydd för användaren: å ena sidan skyddar de dina bitcoins mot fjärråttacker genom att hålla de privata nycklarna offline, och å andra sidan erbjuder de i allmänhet bättre fysiskt motstånd mot försök att extrahera nycklarna. Och det är just på dessa två säkerhetskriterier som man kan bedöma och rangordna de olika modellerna som finns på marknaden.


I den här handledningen föreslår jag att du upptäcker en av dessa lösningar: Tapsigner av Coinkite.


## Introduktion till Tapsigner


Tapsigner är en Hardware Wallet designad i form av ett NFC-kort av företaget Coinkite, även känt för att producera Coldcards.


![TAPSIGNER NUNCHUK](assets/notext/01.webp)


Tapsignern gör det möjligt att lagra ett par bestående av en privat huvudnyckel och en chain code i enlighet med BIP32, för att härleda ett träd av kryptografiska nycklar. Dessa nycklar kan användas för att signera transaktioner genom att placera Tapsigner mot en telefon eller en NFC-kortläsare.

Detta NFC-kort säljs för $19,99, vilket är mycket prisvärt jämfört med andra hårdvaruplånböcker som finns på marknaden. På grund av sitt format erbjuder Tapsigner dock inte lika många alternativ som andra enheter. Det finns uppenbarligen inget batteri, ingen kamera eller en micro SD-kortläsare, eftersom det är ett kort. Enligt min mening är dess största nackdel avsaknaden av en skärm på Hardware Wallet, vilket gör den mer sårbar för vissa typer av fjärråttacker. Detta tvingar faktiskt användaren att signera blint och lita på vad de ser på sin datorskärm.


Trots sina begränsningar kan Tapsigner vara intressant på grund av sitt reducerade pris. Denna Wallet kan särskilt användas för att förbättra säkerheten för en spenderande Wallet utöver en sparande Wallet som skyddas av en Hardware Wallet utrustad med en skärm. Det är också en bra lösning för dem som har små mängder bitcoins och inte vill investera hundra euro i en mer sofistikerad enhet. Dessutom kan användningen av Tapsigner i Multisig-konfigurationer, eller potentiellt i Wallet-system med tidslås i framtiden, erbjuda intressanta fördelar.


## Hur köper man en Tapsigner?


Tapsigner finns att köpa [på Coinkites officiella webbplats](https://store.coinkite.com/store/category/tapsigner). Om du vill köpa den i en fysisk butik kan du också hitta [listan över certifierade återförsäljare](https://coinkite.com/resellers) på webbplatsen.


Du behöver också en telefon som är kompatibel med NFC-kommunikation eller en USB-enhet som kan läsa NFC-kort på standardfrekvensen 13,56 MHz.


## Hur initierar man en Tapsigner med Nunchuk?


När du har fått din Tapsigner är det första steget att undersöka förpackningen för att säkerställa att den inte har öppnats. Om paketet är skadat kan det tyda på att kortet har äventyrats och kanske inte är äkta. CoinKite kommer att leverera din Tapsigner med ett fodral som blockerar radiovågor. Se till att det finns med i ditt paket.


![TAPSIGNER NUNCHUK](assets/notext/02.webp)


För att hantera Wallet kommer vi att använda mobilappen **Nunchuk Wallet**. Se till att din smartphone är NFC-kompatibel och ladda sedan ner Nunchuk från [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) eller direkt via dess [`.apk`-fil](https://github.com/nunchuk-io/nunchuk-android/releases).


![TAPSIGNER NUNCHUK](assets/notext/03.webp)

Om du använder Nunchuk för första gången kommer appen att uppmana dig att skapa ett konto. I den här handledningen är det inte nödvändigt att skapa ett konto. Välj därför "*Fortsätt som gäst*" för att fortsätta utan ett konto.

![TAPSIGNER NUNCHUK](assets/notext/04.webp)


Klicka sedan på "*Unassisted Wallet*".


![TAPSIGNER NUNCHUK](assets/notext/05.webp)


Klicka sedan på knappen "*Jag utforskar på egen hand*".


![TAPSIGNER NUNCHUK](assets/notext/06.webp)


När du är i Nunchuk klickar du på knappen "*+*" bredvid fliken "*Keys*".


![TAPSIGNER NUNCHUK](assets/notext/07.webp)


Välj "*Lägg till NFC-nyckel*".


![TAPSIGNER NUNCHUK](assets/notext/08.webp)


Klicka sedan på "*Add TAPSIGNER*".


![TAPSIGNER NUNCHUK](assets/notext/09.webp)


Klicka på "*Continue*" och placera sedan ditt Tapsigner NFC-kort mot din smartphone.


![TAPSIGNER NUNCHUK](assets/notext/10.webp)


Om din Tapsigner är ny kommer Nunchuk att erbjuda sig att initiera den. Klicka på "*Yes*".


![TAPSIGNER NUNCHUK](assets/notext/11.webp)


Du måste nu välja hur du generate din master chain code.


Tapsigner använder BIP32-standarden. Detta innebär att härledningen av dina kryptografiska nycklar som säkrar dina bitcoins inte förlitar sig på en Mnemonic-fras som BIP39-plånböcker, utan direkt på den privata huvudnyckeln och huvud chain code. Dessa 2 Elements passerar genom HMAC-funktionen för att på ett deterministiskt och hierarkiskt sätt härleda resten av dina Wallet.


Den privata huvudnyckeln genereras direkt av TRNG (*True Random Number Generator*) som är integrerad i din Tapsigner. Master chain code måste å andra sidan tillhandahållas från utsidan. I detta steg har du ett val: låt Nunchuk generate den automatiskt genom att klicka på "*Automatic*", eller generate den själv genom att välja "*Advanced*" och ange den i det angivna fältet.


![TAPSIGNER NUNCHUK](assets/notext/12.webp)


Därefter måste du välja en PIN-kod. I fältet "*Starting PIN*" anger du den PIN-kod som står på baksidan av din Tapsigner.


![TAPSIGNER NUNCHUK](assets/notext/13.webp)


Välj en PIN-kod för att säkra fysisk åtkomst till din Tapsigner. Denna PIN-kod spelar ingen roll i återställningsprocessen för Wallet. Dess enda funktion är att låsa upp din Tapsigner så att du kan signera transaktioner. Se till att spara PIN-koden för att undvika att glömma den. Klicka på "*Fortsätt*" för att fortsätta.


![TAPSIGNER NUNCHUK](assets/notext/14.webp)

Placera nu ditt Tapsigner-kort på baksidan av telefonen för att initiera den.

![TAPSIGNER NUNCHUK](assets/notext/15.webp)


Nunchuk kommer sedan att generate återställningsfilen för din Wallet, som gör att du kan återfå tillgång till dina bitcoins om du förlorar ditt NFC-kort. Den här filen är krypterad med säkerhetskopieringskoden som står på baksidan av din Tapsigner. För att återfå dina bitcoins behöver du absolut den här filen samt koden för att dekryptera den. Det är därför viktigt att göra en papperskopia av den här koden, för om du tappar bort ditt NFC-kort kommer tillgången till den här koden också att gå förlorad, eftersom den bara är skriven på kortet för tillfället. Se till att också skapa flera säkerhetskopior av din krypterade återställningsfil.


![TAPSIGNER NUNCHUK](assets/notext/16.webp)


Välj ett namn för din Wallet.


![TAPSIGNER NUNCHUK](assets/notext/17.webp)


Grunden för din Wallet är nu lagd. För att verifiera äktheten hos dinapsigner kan du när som helst klicka på knappen "*Kör hälsokontroll*".


![TAPSIGNER NUNCHUK](assets/notext/18.webp)


Ange din PIN-kod.


![TAPSIGNER NUNCHUK](assets/notext/19.webp)


Placera sedan ditt kort på baksidan av din telefon.


![TAPSIGNER NUNCHUK](assets/notext/20.webp)


## Hur skapar man en Wallet på en Tapsigner?


Tillbaka på Nunchuk-hemsidan kan du se att din Tapsigner är registrerad bland de tillgängliga signeringsenheterna.


![TAPSIGNER NUNCHUK](assets/notext/21.webp)


Du behöver nu generate nycklarna för din Bitcoin Wallet. Detta gör du genom att klicka på knappen "*+*" till höger om fliken "*Wallets*".


![TAPSIGNER NUNCHUK](assets/notext/22.webp)


Klicka på "*Create new Wallet*".


![TAPSIGNER NUNCHUK](assets/notext/23.webp)


Välj sedan alternativet "*Skapa en ny Wallet med hjälp av befintliga nycklar*".


![TAPSIGNER NUNCHUK](assets/notext/24.webp)


Välj ett namn för din Wallet och klicka sedan på "*Fortsätt*".


![TAPSIGNER NUNCHUK](assets/notext/25.webp)


Välj din Tapsigner som signeringsenhet för den här nya nyckeluppsättningen och klicka sedan på "*Continue*".


![TAPSIGNER NUNCHUK](assets/notext/26.webp)


Om allt är till belåtenhet bekräftar du skapandet.


![TAPSIGNER NUNCHUK](assets/notext/27.webp)

Du kan sedan spara konfigurationsfilen för din Wallet. Den här filen innehåller endast dina publika nycklar, vilket innebär att även om någon kommer åt den kan de inte stjäla dina bitcoins. De kan dock följa alla dina transaktioner. Därför utgör den här filen endast en risk för din integritet. I vissa fall kan den vara avgörande för att återställa din Wallet.

![TAPSIGNER NUNCHUK](assets/notext/28.webp)


Och där har du det, din Wallet är framgångsrikt skapad!


![TAPSIGNER NUNCHUK](assets/notext/29.webp)


När du inte använder din Tapsigner, kom ihåg att förvara den i det fodral som tillhandahålls av Coinkite, som blockerar radiovågor för att skydda mot obehöriga avläsningar.


## Hur tar man emot bitcoins på Tapsigner?


För att ta emot bitcoins, klicka på din Wallet.


![TAPSIGNER NUNCHUK](assets/notext/30.webp)


Använd sedan den genererade Address för att ta emot bitcoins. Om du tidigare har tagit emot bitcoins på denna Wallet måste du klicka på knappen "*Receive*" för att generate en ny tom mottagande Address.


![TAPSIGNER NUNCHUK](assets/notext/31.webp)


När avsändarens transaktion har sänts kommer du att se den på din Wallet.


![TAPSIGNER NUNCHUK](assets/notext/32.webp)


Klicka på "*Visa mynt*".


![TAPSIGNER NUNCHUK](assets/notext/33.webp)


Välj din nya UTXO.


![TAPSIGNER NUNCHUK](assets/notext/34.webp)


Klicka på "*+*" bredvid "*Tags*" för att lägga till en etikett på din UTXO. Detta är en bra praxis, eftersom det hjälper dig att komma ihåg ursprunget till dina mynt och optimera din integritet för framtida utgifter.


![TAPSIGNER NUNCHUK](assets/notext/35.webp)


Välj en befintlig tagg eller skapa en ny och klicka sedan på "*Spara*". Du har också möjlighet att skapa "*samlingar*" för att organisera dina mynt på ett mer strukturerat sätt.


![TAPSIGNER NUNCHUK](assets/notext/36.webp)


## Hur skickar jag bitcoins med Tapsigner?


Nu när du har bitcoins i din Wallet kan du också skicka dem. För att göra detta klickar du på den Wallet du vill ha.


![TAPSIGNER NUNCHUK](assets/notext/37.webp)


Klicka på knappen "*Sänd*".


![TAPSIGNER NUNCHUK](assets/notext/38.webp)


Välj det belopp som ska skickas och klicka sedan på "*Fortsätt*".


![TAPSIGNER NUNCHUK](assets/notext/39.webp)


Lägg till en "*not*" till din framtida transaktion för att komma ihåg dess syfte.


![TAPSIGNER NUNCHUK](assets/notext/40.webp)

Därefter anger du manuellt mottagarens Address i det angivna fältet.

![TAPSIGNER NUNCHUK](assets/notext/41.webp)


Du kan också skanna en QR-kod kodad med Address genom att klicka på ikonen längst upp till höger på skärmen.


![TAPSIGNER NUNCHUK](assets/notext/42.webp)


Klicka på knappen "*Create Transaction*".


![TAPSIGNER NUNCHUK](assets/notext/43.webp)


Kontrollera detaljerna i din transaktion och klicka sedan på knappen "*Signera*" bredvid din Tapsigner.


![TAPSIGNER NUNCHUK](assets/notext/44.webp)


Ange din PIN-kod för att låsa upp den.


![TAPSIGNER NUNCHUK](assets/notext/45.webp)


Placera sedan Tapsigner på baksidan av din smartphone.


![TAPSIGNER NUNCHUK](assets/notext/46.webp)


Din transaktion är nu signerad. Kontrollera en sista gång att allt är korrekt och klicka sedan på "*Broadcast Transaction*" för att sända den på Bitcoin-nätverket.


![TAPSIGNER NUNCHUK](assets/notext/47.webp)


Din transaktion väntar nu på bekräftelse.


![TAPSIGNER NUNCHUK](assets/notext/48.webp)


## Hur återfår man Wallet i händelse av förlust av tapsignern?


Om du har förlorat din Tapsigner kan du återfå din Wallet med hjälp av den kod som anges på kortets baksida. Det är därför viktigt att spara denna kod separat från Tapsignern, för om kortet försvinner försvinner också tillgången till denna kod. Du kommer också att behöva den krypterade säkerhetskopian av Wallet.


För återhämtning kommer vi att använda Nunchuk-appen, men kom ihåg att detta innebär att du tillfälligt säkrar dina medel i en Hot Wallet. Om din Tapsigner säkrade betydande belopp bör du överväga att följa samma återställningsprocess med ett nytt Coldcard istället.


Öppna Nunchuk-appen och klicka på "*+*"-knappen bredvid "*Keys*"-fliken.


![TAPSIGNER NUNCHUK](assets/notext/49.webp)


Välj "*Lägg till NFC-nyckel*".


![TAPSIGNER NUNCHUK](assets/notext/50.webp)


Välj alternativet "* Återställ TAPSIGNER-nyckel från säkerhetskopia *".


![TAPSIGNER NUNCHUK](assets/notext/51.webp)


Du omdirigeras sedan till din enhets filutforskare. Leta upp och välj den krypterade backup-filen för din Wallet. Namnet på denna fil börjar normalt med `backup...`.


![TAPSIGNER NUNCHUK](assets/notext/52.webp)


Ange lösenordet som dekrypterar backupfilen. Detta lösenord motsvarar det som ursprungligen noterades på baksidan av din Tapsigner.


![TAPSIGNER NUNCHUK](assets/notext/53.webp)

Välj sedan ett namn för din återhämtning Wallet.

![TAPSIGNER NUNCHUK](assets/notext/54.webp)


Du har nu återfått åtkomsten till dina bitcoins. Din Wallet hanteras nu som en Hot Wallet som är synlig på fliken "*Keys*" i Nunchuk-appen. Därefter måste du skapa en ny uppsättning kryptografiska nycklar i avsnittet "*Wallets*" genom att associera den här nyckeln med den. För att göra detta kan du följa stegen igen i delen "*Hur man skapar en Wallet på en Tapsigner?*" i denna handledning.


![TAPSIGNER NUNCHUK](assets/notext/55.webp)


Om du har förlorat din Tapsigner rekommenderar jag starkt att du omedelbart överför dina bitcoins till en annan Wallet som du äger, helst skyddad av en Hardware Wallet. Den Tapsigner som du har förlorat kan faktiskt potentiellt vara i fel händer. Det är därför viktigt att tömma den Wallet som du just har återfått och att sluta använda den.


Grattis, du har nu kommit igång med att använda Tapsigner! Om du tyckte att den här handledningen var till hjälp skulle jag uppskatta det om du kunde lämna tummen upp nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!