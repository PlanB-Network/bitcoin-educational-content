---
name: COLDCARD Mk4
description: En guide för att ställa in och använda en COLDCARD Mk4 med Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Hårdvara wallet** är fysiska enheter som är gjorda enbart för att lagra Bitcoin:s privata nyckel på ett säkert sätt. De lagrar de privata nycklarna offline, vilket innebär att hackare inte kan nå dem via internet. Medan **software wallets** huvudsakligen används för vardagliga transaktioner, används **hardware wallets** ofta för att lagra större mängder bitcoins säkert under lång tid. När du gör en Bitcoin-transaktion med hjälp av **hardware wallets** kan wallet signera transaktionerna inuti enheten, så den privata nyckeln exponeras aldrig för internetanslutna miljöer.


I denna handledning kommer vi att utforska en av de mest populära hårdvaru-wallet:orna som produceras av Coinkite, Coldcard Mk4. Vi kommer att ta en titt på hur man ställer in och använder denna hårdvaru-wallet för att utföra Bitcoin-transaktioner.


## Coldcard Mk4 Översikt


Coldcard Mk4 är en Bitcoin-endast hårdvara wallet tillverkad av Coinkite. Denna enhet är utrustad med en skärm, ett numeriskt tangentbord och ett skyddande skjutbart lock. Dessutom erbjuder enheten flera sätt att ansluta och interagera, inklusive USB-C, luftgapad drift med ett MicroSD-kort, NFC och ett virtuellt diskläge. Mk4 innehåller också avancerade säkerhetsfunktioner som BIP39 passphrase och trick-PIN-koder, vilket ger användarna större kontroll och skydd över sin Bitcoin.


## Inledande installation: PIN-kod och ord mot nätfiske


För att komma igång kan Coldcard Mk4 köpas direkt från [Coinkites webbplats] (https://store.coinkite.com/store). Köpare kan också välja att betala med fiatvaluta eller Bitcoin. Dessutom behöver du ett MicroSD-kort (4 GB är tillräckligt) och en strömkälla som kan anslutas via USB-C-kabel (Coldcard Mk4 har endast en USB-C-strömingångsport). Observera att eftersom Mk4 inte har något inbyggt batteri måste den vara ansluten till strömkällan hela tiden när den används.


Du kommer att få din Mk4 i en väska som är skyddad mot manipulation. Vänligen se till att påsen inte har äventyrats. Om du upptäcker något som kan vara ett problem, till exempel skador eller revor på påsen, kan du informera Coinkite genom att skicka ett e-postmeddelande till support@coinkite.com. Dessutom kan du också hitta ett 12-siffrigt nummer på den manipuleringssäkra påsen, som vi kommer att hänvisa till som Mk4:s påsnummer. Detta påsnummer kommer att användas senare för att verifiera att enheten inte har manipulerats under leveransen och att den kommer direkt från Coinkite. Väsknumret lagras säkert i Cold-kortets secure element med hjälp av OTP (One-Time-Programmable) flashminne, vilket innebär att det inte kan ändras när det väl har programmerats. När du slår på enheten för första gången måste numret som visas på skärmen matcha det som står på väskan. Detta säkerställer att den Mk4 du har fått är den ursprungliga enheten från fabriken och inte har bytts ut eller modifierats. Även om denna verifiering endast bekräftar enhetens integritet vid första påslagningen, fortsätter secure element att skydda dina privata nycklar, PIN-kod och passphrase, vilket gör det extremt svårt för någon som manipulerar att äventyra din Bitcoin. Dessutom kommer god praxis, som att säkra dina wallet-relaterade data på rätt sätt, att vara till nytta för den övergripande säkerheten för själva Cold-kortet. För ytterligare information kan du hänvisa till den här [artikeln] (https://blog.coinkite.com/understanding-mk4-security-model/) som utarbetar Cold-korts säkerhetsmodell.


Knappsatsen består av 10 sifferknappar, en OK-knapp (`✓`) och en avbryt-knapp (`✕`). Vissa numeriska knappar kan också användas för navigering: `5` för att navigera uppåt (`^`), `7` för att navigera åt vänster (`<`), `8` för att navigera nedåt (`˅`) och `9` för att navigera åt höger (`>`).


![01](assets/en/01.webp)


Om det inte finns några problem med förpackningen kan du öppna påsen. Mk4 levereras med ett wallet backup-kort som kan användas för att lagra information om enhetens PIN-kod, ord mot nätfiske och seedphrase. Följ följande steg för initialisering:


1. Förbered ett papper och en penna.

2. Anslut Mk4 till en strömkälla (USB-C-kabel) och sätt i MicroSD-kortet.

3. När enheten slås på för första gången visas ett meddelande på skärmen om Coldcards försäljnings- och användarvillkor. Navigera nedåt och tryck sedan på `✓` för att fortsätta.

4. Därefter kommer ett 12-siffrigt nummer att visas på skärmen. Kontrollera detta nummer mot numret på säkerhetsväskan och den extra kopian av väsknumret som fanns i säkerhetsväskan för att säkerställa att enheten inte har manipulerats. Om numren inte stämmer överens ska du omedelbart kontakta Coinkite support innan du fortsätter. Annars trycker du på `✓` för att fortsätta.


![02](assets/en/02.webp)


5. Välj "Välj PIN-kod".

6. Navigera nedåt medan du läser instruktionerna för att gå vidare till nästa steg.


![03](assets/en/03.webp)


7. På Mk4 skapar du och anger PIN-koden (måste vara 2 till 6 tecken lång) och skriver ner den, tryck sedan på `✓` för att fortsätta.

8. Skriv ner de två ord som visas på skärmen. Det här är anti-phishing-orden. Tryck på `✓` för att fortsätta.


![04](assets/en/04.webp)


9. Skapa och ange PIN-suffixet (eller resten av PIN-koden, måste vara 2 till 6 tecken lång) och skriv ner det. Tryck på `✓` för att fortsätta.

10. Ange ditt PIN-prefix på nytt. Tryck på `✓` för att fortsätta.


![05](assets/en/05.webp)


11. Kontrollera om orden för att motverka nätfiske är desamma som de du skrev i steg 8. Tryck på `✓` för att fortsätta.

12. Ange ditt PIN-suffix (eller resten av PIN-koden) igen. Tryck på `✓` för att fortsätta.


![06](assets/en/06.webp)


13. Din Mk4:s PIN-kod och anti-phishing-ord är nu framgångsrikt skapade och lagrade av enheten.


![07](assets/en/07.webp)


Observera att Mk4 alltid kommer att be dig att ange din PIN-kod varje gång du slår på enheten. Utan denna PIN-kod kan du inte komma åt ditt Coldcard Mk4. Se därför till att du skapar tillräcklig säkerhetskopia för PIN-koden och anti-phishing-ord.


## Konfigurera din Wallet


Nästa steg är att konfigurera din wallet. Det finns tre sätt att göra detta på:


- Skapa en ny wallet (standard)
- Skapa en ny wallet med tärningsslag
- Importera en wallet


### Skapa en ny wallet (standard)


För att skapa en ny wallet gör du helt enkelt följande steg.


1. Välj `Nya Wallet` (eller `Nya Seed Words`) > Välj `12 Ord` eller `24 Ord (standard)` beroende på vad du föredrar.


![08](assets/en/08.webp)


2. Enheten kommer att generera 12 eller 24 ord som din seedphrase baserat på ditt val. Navigera nedåt medan du noggrant skriver ner varje ord i rätt ordning. Tryck sedan på `✓` för att fortsätta.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Enheten kommer att be dig att verifiera din seedphrase genom att ställa frågorna i en slumpmässig ordning (t.ex. `Ord 1 är?`, sedan `Ord 5 är?`, sedan `Ord 12 är?`, och så vidare) och det kommer att finnas tre ordval för varje fråga. Se anteckningen från steg 2 och välj orden korrekt (genom att trycka på `1`, `2` eller `3`, beroende på vilket som motsvarar rätt ord) för att slutföra wallet-skapelsen.


![09](assets/en/09.webp)


4. Mk4 kommer sedan att fråga om du vill aktivera NFC/Tap eller inte. För närvarande väljer du `✕` för detta alternativ. Detta kan ändras i inställningarna i framtiden.

5. Slutligen kommer Mk4 också att visa om du vill inaktivera USB-porten (som kan användas för dataöverföring utan luftkonditionering). För närvarande väljer du `✓` för detta alternativ. Detta kan ändras i inställningarna i framtiden.

6. Skärmen kommer nu att visa huvudmenyn med "Klar att signera" högst upp. Detta markerar slutförandet av skapandeprocessen för wallet.


![10](assets/en/10.webp)


### Skapa en ny wallet med tärningsslag


Alternativt kan du också välja att generera den nya seedphrase med entropi. Gör det om du inte litar på Mk4:s nygenererade seedphrase.


Förfarandet på Coldcard Mk4 är följande:


1. Välj `Nya Wallet` (eller `Nya Seed Words`) > Välj `12 Word Dice Roll` eller `24 Word Dice Roll` beroende på vad du föredrar.

2. Du kommer att bli ombedd att ange resultatet av dina tärningskast. Varje tärningskast tillför slumpmässighet till wallet-skapandeprocessen, vilket säkerställer att din seedphrase genereras på ett helt säkert och oförutsägbart sätt. Minsta antal kast är 50 för seedphrase med 12 ord och 99 för seedphrase med 24 ord. Tryck på `✓` när du har matat in minst 99 tärningskastvärden.


![11](assets/en/11.webp)


3. Enheten kommer att generera 12 eller 24 ord som din seedphrase baserat på ditt val. Navigera nedåt medan du noggrant skriver ner varje ord i rätt ordning. Tryck sedan på `✓` för att fortsätta.

4. Enheten kommer att be dig att verifiera din seedphrase genom att ställa frågorna i slumpmässig ordning (t.ex. "Ord 1 är", sedan "Ord 5 är", sedan "Ord 12 är", och så vidare) och det kommer att finnas tre ordval för varje fråga. Se anteckningen från steg 3 och välj orden korrekt (genom att trycka på `1`, `2` eller `3`, beroende på vilket som motsvarar rätt ord) för att slutföra wallet-skapelsen.


![12](assets/en/12.webp)


5. Mk4 kommer sedan att fråga om du vill aktivera NFC/Tap eller inte. För närvarande väljer du `✕` för detta alternativ. Detta kan ändras i inställningarna i framtiden.

6. Slutligen kommer Mk4 också att visa om du vill inaktivera USB-porten (som kan användas för dataöverföring utan luftkonditionering). För närvarande väljer du `✓` för detta alternativ. Detta kan ändras i inställningarna i framtiden.

7. Skärmen kommer nu att visa huvudmenyn med `Ready to Sign` högst upp. Detta markerar slutförandet av skapandeprocessen för wallet.


![13](assets/en/13.webp)


### Importera en wallet


Det sista alternativet är att du importerar en wallet. Det kan du göra om du vill återställa en wallet från en seedphrase som du redan har. Du kan följa dessa steg:


1. Välj `Importera befintlig`.

2. Välj "24 ord", "18 ord" eller "12 ord", beroende på antalet ord i din seedphrase.


![14](assets/en/14.webp)


3. Coldcard Mk4 kommer sedan att fråga dig vad varje ord är i ordningsföljd. För varje ord, navigera nedåt eller uppåt tills du hittar det skrivna prefixet för varje ord. Enheten kommer att begränsa möjligheterna tills du kan hitta rätt ord. Gör på samma sätt med de övriga orden.

4. För det sista ordet kommer Coldcard Mk4 endast att visa en begränsad mängd möjliga ord. Om det inte finns några matchningar kan du ha matat in orden felaktigt. I annat fall väljer du det ord som matchar det på din seedphrase.


![15](assets/en/15.webp)


5. Mk4 kommer sedan att fråga om du vill aktivera NFC/Tap eller inte. För närvarande väljer du `✕` för detta alternativ. Detta kan ändras i inställningarna i framtiden.

6. Slutligen kommer Mk4 också att visa om du vill inaktivera USB-porten (som kan användas för dataöverföring utan luftkonditionering). För närvarande väljer du `✓` för detta alternativ. Detta kan ändras i inställningarna i framtiden.

7. Skärmen kommer nu att visa huvudmenyn med "Klar att signera" högst upp. Detta markerar slutförandet av skapandeprocessen för wallet.


![16](assets/en/16.webp)


Observera att seedphrase är den enda åtkomsten för att återställa din wallet. Skapa en säkerhetskopia av din seedphrase och förvara den på en säker plats. **Inte dina nycklar, inte dina mynt**, den som har din seedphrase har tillgång till dina bitcoins!


## Konfigurera din passphrase


En av de bästa metoderna i Bitcoin är att använda en passphrase. passphrase fungerar som det 13:e eller 25:e ordet i tillägg till seedphrase. Det som gör det annorlunda är att du kan välja vilken fras du vill, medan seedphrase väljs från en förutbestämd lista med 2048 ord. När du har konfigurerat din wallet kommer du som standard att börja med en wallet med en tom passphrase. För att ställa in en icke-tom passphrase gör du helt enkelt följande steg:


1. Gå till `Passphrase`.

2. Navigera ner för att läsa beskrivningen om passphrase, tryck sedan på `✓` för att fortsätta.

3. Välj `Editera fras`.


![17](assets/en/17.webp)


4. Ange din passphrase:


   - Tryck på `1` (bokstäver), `2` (siffror) eller `3` (symboler) för att välja teckentyp.
   - Tryck på `4` för att växla mellan små och stora bokstäver (kan endast användas vid inmatning av bokstäver).
   - Navigera med hjälp av `^` eller `˅` för att välja karaktär för din passphrase.
   - Navigera med hjälp av `<` eller `>` för att flytta mellan tecken. Du kan också använda `>` för att lägga till mellanslag.
   - Tryck på `✕` för att radera tecknen.
   - Tryck på `✓` när du är klar med redigeringen av passphrase.

5. De andra alternativen har dessutom följande funktioner:


   - Med "Lägg till ord" eller "Lägg till siffror" kan du lägga till bokstäver/siffror till den passphrase som du för närvarande redigerar.
   - Tryck på `Clear ALL` för att återställa den passphrase som du för närvarande redigerar.
   - Tryck på `CANCEL` för att gå tillbaka till huvudmenyn.

6. Skriv ner din passphrase som säkerhetskopia.

7. Tryck på `APPLY` för att få tillgång till wallet med den passphrase som du just har ställt in.

8. Mk4 kommer då att visa ett 8 tecken långt fingeravtryck för huvudnyckeln. Detta kan betraktas som wallet:s "ID". Skriv ner detta fingeravtryck och tryck på `✓` för att fortsätta.


![18](assets/en/18.webp)


9. Nu kommer wallet att visa huvudmenyn för wallet med den passphrase som du har matat in.

10. Det är viktigt att notera att en wallet inte kommer att tala om för dig att du har matat in fel passphrase, eftersom varje passphrase motsvarar varje egen wallet med en unik identitet (huvudnyckelns fingeravtryck). Därför är det bra att ange samma passphrase igen och kontrollera om det ger samma wallet-fingeravtryck, så att du kan vara säker på att du har angett det korrekt. För att göra det, utför steg 11 till 14.

11. På huvudmenyn väljer du `Restore Master` och trycker sedan på `✓`. Du är nu tillbaka i huvudmenyn för wallet med den tomma passphrase.


![19](assets/en/19.webp)


12. Gå till `Passphrase` igen och tryck sedan på `✓` för att fortsätta.

13. Skriv in den passphrase som du skrev ner i steg 6 och tryck sedan på "TILLÄMPA".

14. Kontrollera fingeravtrycket för den 8 tecken långa huvudnyckeln mot det fingeravtryck som du skrev ner i steg 8. Om de båda fingeravtrycken inte matchar kan du ha skrivit felaktiga tecken. Du kan välja en ny passphrase istället och upprepa processen från steg 1. Men om båda fingeravtrycken matchar betyder det att du har matat in passphrase på rätt sätt.

15. wallet med din valda passphrase är klar att användas.


## Exportera Wallet till Sparrow


Precis som andra hårdvaru-wallet kan Coldcard Mk4 inte användas på egen hand. Det måste anslutas till en mjukvaru-wallet som fungerar som ett gränssnitt. Med programvaran wallet kan du se ditt saldo, skapa transaktioner och hantera adresser, medan Cold-kortet säkert signerar dessa transaktioner utan att någonsin exponera dina privata nycklar.


I denna handledning kommer vi att använda Sparrow Wallet som gränssnitt. Proceduren för att exportera wallet är som följer:


1. Kontrollera att du har satt i ett MicroSD-kort i Mk4.

2. Utför stegen i "Konfigurera din passphrase" på wallet med den passphrase som du vill exportera. Om du vill exportera wallet med den tomma passphrase kan du hoppa över detta steg.

3. Gå till `Avancerat/Verktyg` > Välj `Exportera Wallet` > Välj `Generisk JSON` > Bläddra ner när du läser instruktionerna och tryck sedan på `✓`.


![20](assets/en/20.webp)


4. Mk4 har nu skapat en fil med formatet `.json` på MicroSD-kortet.


![21](assets/en/21.webp)


5. Ta ut MicroSD-kortet från Cold-kortet och sätt in det i den enhet där Sparrow Wallet är installerad.

6. Öppna Sparrow Wallet.

7. Klicka på `File`


![22](assets/en/22.webp)


Klicka sedan på `Ny Wallet`


![23](assets/en/23.webp)


Ange sedan namnet för wallet


![24](assets/en/24.webp)


Därefter klickar du på `Create Wallet`


![25](assets/en/25.webp)


8. Välj `Script Type`.


![26](assets/en/26.webp)


9. I avsnittet Keystore väljer du `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Leta efter Coldcard och klicka på `Importera fil...`.


![28](assets/en/28.webp)


11. Välj den fil som skapades i steg 4 (den med formatet `.json`).


![29](assets/en/29.webp)


12. På Mk4, återgå till huvudmenyn och navigera till `Advanced/Tools` > `View Identity`. Kontrollera att det fingeravtryck som visas på Mk4:s skärm matchar det på Sparrow Wallet (huvudfingeravtrycket i avsnittet Keystore)

13. Klicka på knappen `Apply` längst ner till höger.


![30](assets/en/30.webp)


14. Alternativt kan du också lägga till ett lösenord för den exporterade wallet. Detta lösenord krävs varje gång du öppnar programmet Sparrow Wallet för att komma åt wallet. Om du glömmer lösenordet i framtiden kan du helt enkelt upprepa steg 1-13 och välja ett nytt lösenord.


![31](assets/en/31.webp)


15. wallet är nu framgångsrikt exporterad och redo att användas.


![32](assets/en/32.webp)


## Ta emot bitcoin


Nu ska vi lära oss hur man tar emot Bitcoin med hjälp av Mk4. Denna process är ganska enkel eftersom du inte behöver använda själva Mk4-enheten. Så länge du redan har exporterat din wallet till Sparrow kan du ta emot Bitcoin direkt via Sparrow Wallet. Följ dessa steg för att ta emot bitcoins med Mk4:


1. Öppna Sparrow Wallet.

2. Välj `Open Wallet` > Välj den wallet-fil som du vill ta emot bitcoin till > Ange lösenordet som är kopplat till den wallet.


![33](assets/en/33.webp)


3. I Sparrow:s gränssnitt klickar du på fliken `Receive` på vänster sida av gränssnittet.


![34](assets/en/34.webp)


4. En adress tillsammans med en QR-kod kommer att visas högst upp. Du kan kopiera och klistra in adressen eller skanna QR-koden med den wallet som du använder för att skicka bitcoin till Sparrow Wallet. Alternativt kan du skriva in en etikett för de bitcoin du tar emot.


![35](assets/en/35.webp)


5. När du har skickat bitcoins klickar du på fliken `Transactions` på vänster sida av gränssnittet i Sparrow:s gränssnitt. Du kommer att se en ny post högst upp i transaktionshistoriken, som motsvarar den transaktion du just gjorde.


![36](assets/en/36.webp)


6. Du kan också navigera på fliken `UTXOs` på vänster sida av gränssnittet för att se de bitcoin du just fått.


![37](assets/en/37.webp)


## Skicka bitcoin


Till skillnad från att ta emot bitcoins kräver utgifterna för bitcoins som är kopplade till ditt Cold-kort att du använder Cold-kortet för att signera transaktionerna. Proceduren för att skicka bitcoins med Mk4 är som följer:


1. Sätt i MicroSD-kortet i den enhet där din Sparrow Wallet är installerad.

2. Öppna Sparrow Wallet.

3. Välj `Open Wallet` > Välj den wallet-fil som du vill använda för att skicka bitcoins med > Ange lösenordet som är associerat med den wallet.


![38](assets/en/38.webp)


4. I Sparrow:s gränssnitt klickar du på fliken `Send` till vänster i gränssnittet.


![39](assets/en/39.webp)


5. På fliken `Pay to` anger du den adress du vill skicka bitcoins till.

6. Lägg till en etikett för transaktionen.

7. Ange det belopp i bitcoins som du vill skicka.

8. Ange avgiften genom att växla mellan `Range` eller skriv in en siffra direkt i `Fee`-delen.


![40](assets/en/40.webp)


9. Klicka på `Create Transaction` i det nedre högra hörnet.


![41](assets/en/41.webp)


10. Du kommer till en ny transaktionsflik vars namn är den etikett som du angav i steg 6. Klicka på `Finalize Transaction for Signing`.


![42](assets/en/42.webp)


11. Klicka på `Save Transaction` och spara transaktionen på MicroSD-kortet. Byt namn på filen om det behövs. I detta steg sparas transaktionen som en PSBT-fil.


![43](assets/en/43.webp)


12. Ta ut MicroSD-kortet och sätt in det i din Coldcard Mk4.

13. Slå på din Mk4 genom att ansluta den till en strömkälla.

14. Ange din PIN-kod.

15. Gå till `Passphrase` och ange passphrase för den wallet som du vill använda för att skicka bitcoins med. Om du vill använda wallet med den tomma passphrase hoppar du över det här steget.

16. Se till att huvudnyckelns fingeravtryck är detsamma som på din Sparrow Wallet. Du kan kontrollera detta på Sparrow Wallet:s flik `Inställningar` på vänster sida av gränssnittet. Tryck sedan på `✓` på din Mk4 för att fortsätta. Detta tar dig till huvudmenyn.

17. På Mk4:s huvudmeny väljer du "Klar att signera". På skärmen visas ett meddelande med texten "OKAY TO SEND". Kontrollera att beloppet för de bitcoins du vill skicka och den mottagande adressen är korrekta. Tryck på `✓` för att bekräfta eller `✕` för att avbryta.

18. Om det finns flera PSBT-filer att välja mellan kommer Mk4 att visa meddelandet "Välj PSBT-fil som ska signeras". Tryck på `✓` för att fortsätta. Välj sedan den PSBT-fil som du vill signera genom att navigera nedåt eller uppåt. Utför steg 17 för den transaktionen.


![44](assets/en/44.webp)


19. Mk4 visar nu meddelandet `PSBT Signed` tillsammans med namnet på filen med den signerade PSBT. Tryck på `✓` för att fortsätta.

20. Ta ut MicroSD-kortet från Cold-kortet och sätt in det i den enhet där Sparrow Wallet är installerad.

21. På Sparrow Wallet klickar du på `Load Transaction`.


![45](assets/en/45.webp)


22. Välj filen med samma namn som den som skapades i steg 19.


![46](assets/en/46.webp)


23. Klicka på `Broadcast Transaction`.


![47](assets/en/47.webp)


24. Din transaktion har skickats och den håller på att behandlas. Du kan gå till fliken `Transaktioner` för att se bekräftelsestatus för din transaktion.


![48](assets/en/48.webp)


## Uppgradering av firmware


### Kontrollera din firmware-version


Coldcard Mk4:s firmware kan alltid uppgraderas till en nyare version. För att kontrollera om din Mk4 har uppgraderats till den senaste versionen eller inte, utför följande steg:

1. Slå på din Mk4 genom att ansluta den till en strömkälla.

2. Ange din PIN-kod.

3. Gå till "Avancerat/Verktyg" > Välj "Uppgradera firmware" > Välj "Visa version".


![49](assets/en/49.webp)


Kontrollera den version som visas på Mk4:s skärm mot den som finns på [Coinkites webbplats] (https://coldcard.com/downloads). Om versionen skiljer sig åt kan du uppgradera den fasta programvaran till den nyare versionen.


![50](assets/en/50.webp)


### Uppgradering av din firmware


Gör så här om du vill uppgradera den fasta programvaran till den senaste versionen:


1. Sätt i MicroSD-kortet i din bärbara dator/PC.

2. Gå till [Coinkites webbplats] (https://coldcard.com/downloads) och ladda ner den senaste firmware till ditt MicroSD-kort (den röda knappen till höger om Mk4-bilden med versionsnumret på).


![51](assets/en/51.webp)


Du kan också ladda ner andra versioner genom att klicka på `All Files on Mk4` och utforska den version du vill ladda ner. Den nedladdade filen kommer att vara i `.dfu`-format.


![52](assets/en/52.webp)


3. Ta ut MicroSD-kortet och sätt in det i din Mk4.

4. Slå på din Mk4 genom att ansluta den till en strömkälla.

5. Ange din PIN-kod.

6. Gå till `Avancerat/Verktyg` > Välj `Uppgradera Firmware` > Välj `Från MicroSD` > Bläddra nedåt när du läser instruktionerna och tryck sedan på `✓`.


![53](assets/en/53.webp)


7. Välj filen `.dfu` som du hämtade i steg 2.

8. Coldcard Mk4 kommer att visa ett meddelande "Installera den här nya firmware". Bläddra nedåt medan du läser instruktionerna och tryck sedan på `✓`.


![54](assets/en/54.webp)


9. Vänta tills Mk4 har slutfört installationen av den nya inbyggda programvaran. Koppla inte bort strömkällan under installationen.

10. När detta är klart startar Mk4 om sig själv. Du kan ange din PIN-kod och utföra stegen "Kontrollera din firmwareversion" för att kontrollera om firmware har uppgraderats eller inte.


## Avancerade funktioner


### Ändra din PIN-kod


Om du vill ändra din PIN-kod för inloggning, gör du så här:


1. Förbered en penna och ett papper.

2. Slå på din Mk4 genom att ansluta den till en strömkälla.

3. Ange din PIN-kod.

4. Gå till "Inställningar" > Välj "Inloggningsinställningar" > Välj "Ändra huvud-PIN

5. Navigera nedåt medan du läser meddelandet och tryck sedan på `✓` för att fortsätta.


![55](assets/en/55.webp)


6. Ange din gamla PIN-kod.

7. Ange ditt nya PIN-kodprefix (måste vara 2 till 6 tecken långt) och skriv ner det.

8. Mk4 kommer nu att visa två nya anti-phishing-ord, skriv ner dem och tryck sedan på `✓` för att fortsätta.

9. Ange din nya PIN-kod (eller resten av PIN-koden, måste vara 2 till 6 tecken lång) och skriv ner den.


![56](assets/en/56.webp)


10. Ange ditt nya PIN-kodprefix igen.

11. Kontrollera om anti-phishing-orden stämmer överens med dem du skrev i steg 8.

12. Ange din nya PIN-kod (eller resten av PIN-koden).


![57](assets/en/57.webp)


13. Din PIN-kod har ändrats med framgång.


### PIN-koder för trick - Lägg till nytt trick


En Trick-PIN är en alternativ PIN-kod som skiljer sig från den som du använder för att ställa in din Coldcard Mk4 för första gången. När du slår på din Mk4 kan du mata in trick-PIN-koden/-koderna istället för din huvud-PIN-kod för att utlösa vissa åtgärder. För att konfigurera trick-PIN i Mk4 kan du göra följande steg:


1. Förbered en penna och ett papper.

2. Slå på din Mk4 genom att ansluta den till en strömkälla.

3. Ange din PIN-kod.

4. Gå till "Inställningar" > Välj "Inloggningsinställningar" > Välj "Trick PIN-koder" > Välj "Lägg till nytt trick".


![58](assets/en/58.webp)


5. Ange ditt PIN-kodprefix (måste vara 2 till 6 tecken långt) och skriv ner det.

6. Mk4 kommer nu att visa två nya anti-phishing-ord, skriv ner dem och tryck sedan på `✓` för att fortsätta.

7. Ange din trick-PIN-suffix (eller resten av PIN-koden, måste vara 2 till 6 tecken lång) och skriv ner den.


![59](assets/en/59.webp)


8. Navigera nedåt eller uppåt för att välja den åtgärd som du vill koppla till den trick-PIN som du just har skapat. Listan över åtgärder är:


    - `Brick Self`, när detta väljs kommer din Mk4:s chips att förstöras efter att PIN-koden har slagits in, vilket gör din Mk4 oanvändbar permanent.
    - `Wipe Seed`, kan du välja mellan följande åtgärder:
      - "Torka och starta om": seed raderas och Cold-kortet startas om efter att PIN-koden har angetts.
      - "Tyst radering": seed raderas tyst, men Cold-kortet kommer att fungera som om PIN-koden har angetts felaktigt.
      - `Torka -> Wallet`: seed torkas tyst, och Cold-kortet tar dig in i ett tvång wallet.
    - `Duress Wallet`, när den är vald kommer din Mk4 att leda till en duress wallet efter att PIN-koden har angetts.
    - `Login Countdown`, kan du välja mellan följande åtgärder:
      - `Torka och räkna ner`: seed torkas omedelbart, sedan börjar Mk4 visa en nedräkning.
      - `Nedräkning och tegelsten`: Nedräkningen börjar och Mk4 murar sig själv efter att tiden har gått ut.
      - "Bara nedräkning": Mk4 påbörjar nedräkningen och startar om sig själv när tiden har gått ut.
    - `Look Blank`, när den är vald, efter att trick-PIN har angetts, agerar Cold-kortet som om seedphrase är raderad, men det är faktiskt fortfarande i minnet.
    - `Just Reboot`, när den är vald kommer Coldcard att starta om sig själv efter att PIN-koden har angetts.
    - `Delta Mode`, Denna avancerade funktion är avsedd för erfarna användare och är utformad för att skydda mot allvarliga hot, t.ex. tvång av någon med insiderkunskap. När Delta-läget är aktiverat verkar COLDCARD öppna den riktiga wallet, vilket gör att angriparen kan bläddra och bekräfta att den ser äkta ut. I hemlighet blockeras dock all transaktionssignering, så att inga bitcoin kan skickas. Den inaktiverar också åtkomst till seed-frasen, och alla försök att visa den kommer att radera den helt. För att få den falska wallet att se mer övertygande ut måste Trick PIN-koden som används för Delta Mode börja med samma siffror som den riktiga PIN-koden (så att den visar samma anti-phishing-ord) men sluta annorlunda.
    - `Policy Unlock`, när detta väljs kommer Single Signer Spending Policy (SSSP) att inaktiveras efter att trick-PIN har angetts.
    - `Policy Unlock & Wipe`, när den väljs, låtsas den inaktivera SSSP men den kommer att radera seedphrase i processen.

9. När du har valt den åtgärd som du vill koppla till trick-PIN:en bekräftar du ditt val genom att trycka på `✓`. Din trick-PIN är nu konfigurerad.

10. I "Inställningar" > "Inloggningsinställningar" > "Trick-PIN-koder" kan du se en lista över de trick-PIN-koder du har skapat och de åtgärder som är kopplade till dem. Du kan välja att konfigurera om trick-PIN-koderna och de åtgärder som är kopplade till dem. Du kan också dölja eller ta bort dem genom att markera PIN-koden och sedan välja "Dölj trick" eller "Ta bort trick".


![60](assets/en/60.webp)


### Trick-PIN-koder - lägg till om det är fel


Alternativt kan du lägga till en åtgärd "Lägg till om fel" som utlöses efter att fel PIN-kod har angetts ett visst antal gånger. Du kan konfigurera detta genom att utföra följande steg:


1. Slå på din Mk4 genom att ansluta den till en strömkälla.

2. Ange din PIN-kod.

3. Gå till "Inställningar" > Välj "Inloggningsinställningar" > Välj "Trick-PIN-koder" > Välj "Lägg till om fel".


![61](assets/en/61.webp)


4. Mk4 kommer att visa ett meddelande om denna inställning. Navigera nedåt medan du läser igenom förklaringen och tryck sedan på `✓` för att fortsätta.

5. Ange det antal felaktiga försök som krävs för att utlösa åtgärden. Obs: Det maximala antalet försök är `12`. Detta beror på att Mk4 är utformad så att när fel PIN-kod anges `13` gånger kommer enheten att blockera sig själv, vilket gör den oanvändbar permanent. När du har matat in numret trycker du på `✓` för att fortsätta.

6. Navigera uppåt eller nedåt för att välja åtgärd. De tillgängliga åtgärderna är följande:


   - `Wipe, Stop`: seedphrase raderas och enheten visar "Seed is wiped, Stop."
   - `Radera och starta om`: seedphrase raderas och enheten startas om utan något meddelande.
   - "Tyst radering": seedphrase raderas tyst och enheten beter sig som ett försök med fel PIN-kod (inget uppenbart raderingsmeddelande).
   - `Brick Self`: Enheten är permanent avaktiverad och visar bara "Bricked"
   - "Sista chansen": seedphrase raderas men du får ett sista PIN-försök; ange fel PIN-kod igen och enheten kommer att brickas.
   - "Bara starta om": Enheten startar helt enkelt om och inget annat ändras.

Välj den åtgärd du vill tillämpa och tryck på `✓` för att fortsätta


![62](assets/en/62.webp)


7. Du kommer tillbaka till katalogen `Inställningar > Inloggningsinställningar > Trick PINs`. Under `Trick PINs:` hittar du listan över trick-pins tillsammans med `WRONG PIN`-åtgärd. Du kan också dölja eller ta bort den genom att markera PIN-koden och sedan välja `Hide Trick` eller `Delete Trick`.


![63](assets/en/63.webp)



## Slutsats


Denna handledning har gett en guide om hur man ställer in Mk4, hur man utför Bitcoin-transaktioner med Mk4 och hur man använder några avancerade funktioner i Mk4. Den erbjuder säkra och flexibla sätt att lagra och hantera dina bitcoins. Dess design säkerställer att privata nycklar aldrig lämnar enheten, medan funktioner som passphrase, trick-PIN-koder och transaktioner med luftgap ger användarna full kontroll över sin säkerhetsinställning. Den kan kopplas ihop med Sparrow Wallet för en användarvänlig upplevelse av att skapa, signera och hantera Bitcoin-transaktioner utan att kompromissa med integritet eller säkerhet.


Om du vill utforska andra funktioner kan du kontrollera dokumentationen på Coinkites webbplats [här] (https://coldcard.com/docs/). Jag hoppas att du tycker att denna handledning är till nytta när du använder ditt Coldcard Mk4. Tack så mycket och på återseende nästa gång!