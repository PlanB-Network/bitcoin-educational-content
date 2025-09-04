---
name: Jade

description: Så här konfigurerar du din JADE-enhet
---

![image](assets/cover.webp)


## Instruktionsvideo


![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)

Blockstream Jade - Mobile Bitcoin Hardware Wallet FULL TUTORIAL av BTCsession


## Fullständig skrivguide


![image](assets/cover2.webp)


### Förkunskapskrav


1. Ladda ner den senaste versionen av Blockstream Green.


2. Installera den här drivrutinen för att se till att Jade känns igen av din dator.


### Inställning av skrivbord


![full guide](https://youtu.be/0fPVzsyL360)


Öppna Blockstream Green och klicka sedan på Blockstream-logotypen under Enheter.


![image](assets/1.webp)


Anslut Jade till skrivbordet med hjälp av den medföljande USB-kabeln.


**Note:** Om Jade inte känns igen av datorn, se till att nödvändiga drivrutiner är installerade och kontrollera om det kan bero på ett problem med USB-behörigheter.


När din Jade visas i Green, uppdatera Jade genom att klicka på Sök efter uppdateringar och välj den senaste firmwareversionen. Använd skrollhjulet eller växla på Jade för att bekräfta och fortsätta med uppdateringen. Kontrollera att din Jade fortfarande visar knappen "Initialize", annars måste du vänta med att uppgradera Jade tills efter att du har konfigurerat den. Använd bakåtknappen för att komma till den här skärmen om det behövs.


![image](assets/2.webp)


När du har uppdaterat Jades firmware väljer du Setup Jade på det nätverk och den säkerhetspolicy som du vill använda.


**Tips:** Säkerhetspolicyn finns under Typ på inloggningsskärmen som visas nedan. Om du är osäker på om du ska välja Singlesig eller Multisig Shield kan du läsa vår guide [här](https://help.blockstream.com/hc/en-us/articles/4403642609433)


![image](assets/3.webp)


Välj sedan att skapa en ny Wallet och välj 12 ord till generate för din återställningsfras. Om du klickar på Advanced får du möjlighet att välja en återställningsfras på 12 eller 24 ord.


![image](assets/4.webp)


Spela in återställningsfrasen offline på papper (eller genom att använda en särskild enhet för säkerhetskopiering av återställningsfrasen för extra säkerhet). Använd sedan hjulet eller växeln på toppen av din Jade för att verifiera din återställningsfras. Detta steg säkerställer att du har skrivit ner den korrekt.


![image](assets/5.webp)


Ange och bekräfta din sexsiffriga PIN-kod. Denna används för att låsa upp Blockstream Jade varje gång du loggar in på din Wallet.


![image](assets/6.webp)


Nu väljer du helt enkelt Gå till Wallet i Green:s skrivbordsapp och du kommer att se din Wallet öppen på Blockstream Green. Blockstream Jade kommer också att visa att den är redo! Du kan nu använda din Jade för att skicka och ta emot Bitcoin-transaktioner.


![image](assets/7.webp)


När du är klar med att använda din Wallet kopplar du bort Blockstream Jade från din enhet. Nästa gång du vill använda Wallet på Blockstream Jade ansluter du bara din enhet igen och följer anvisningarna.


källa: https://help.blockstream.com/hc/en-us/articles/17478506300825


### Bilaga A - Verifiering av nedladdningsfilen för Green Wallet


Att verifiera nedladdningen innebär att kontrollera att den fil du laddat ner inte har ändrats sedan den släpptes av utvecklaren.


Vi gör detta genom att kontrollera att signaturen (som produceras av utvecklarens privata nyckel) tillsammans med den nedladdade filen och utvecklarens offentliga nyckel ger ett SANT resultat när den passerar genom gpg -verify-funktionen. Jag ska visa dig hur du gör det härnäst.


Först hämtar vi signeringsnyckeln:


För Linux öppnar du terminalen och kör det här kommandot (du ska bara kopiera och klistra in texten och inkludera citattecknen):


```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```


För Mac gör du samma sak, förutom att du måste ladda ner och installera GPG Suite först.


För Windows gör du samma sak, förutom att du måste ladda ner och installera GPG4Win först.


Du får ett meddelande som säger att den offentliga nyckeln har importerats.


![image](assets/9.webp)


Den här bilden har ett tomt alt-attribut; dess filnamn är image-3-1024x162.webp


Därefter måste vi hämta filen som innehåller Hash för programvaran. Den är lagrad på Blockstreams GitHub-sida. Gå först till deras informationssida här och klicka på länken för "desktop". Det kommer att ta till den senaste versionssidan på GitHub och där ser du en länk till filen SHA256SUMS.asc, som är ett textdokument som innehåller Blockstreams publicerade Hash av programmet vi laddade ner.


![image](assets/10.webp)


GitHub:


![image](assets/11.webp)


Det är inte nödvändigt, men efter att ha sparat på disken bytte jag namn på "SHA256SUMS.asc" till "SHA256.txt" för att lättare kunna öppna filen på Mac med textredigeraren. Detta var innehållet i filen:


![image](assets/12.webp)


Den text vi är ute efter finns högst upp. Beroende på vilken fil vi laddade ner finns det en motsvarande Hash-utdata som vi kommer att jämföra med senare.


Den nedre delen av dokumentet innehåller den signatur som gjorts på meddelandet ovan - det är en två i en fil.


Ordningen spelar ingen roll, men innan vi kontrollerar Hash ska vi kontrollera att Hash-meddelandet är äkta (dvs. inte har manipulerats).


Öppna terminalen. Du måste vara i rätt katalog där filen SHA256SUMS.asc laddades ner. Förutsatt att du laddade ner den till katalogen "Downloads", för Linux och Mac, byt till katalogen så här (skiftlägeskänslig):


```bash
cd Downloads
```


Naturligtvis måste du trycka på <enter> efter dessa kommandon. I Windows öppnar du CMD (kommandotolken) och skriver samma sak (även om det inte är skiftlägeskänsligt).


För Windows och Mac måste du redan ha laddat ner GPG4Win respektive GPG Suite enligt tidigare instruktioner. För Linux kommer gpg med operativsystemet. Skriv det här kommandot från Terminal (eller CMD för Windows):


```bash
gpg --verify SHA256SUMS.asc
```


Den exakta stavningen av filnamnet (i rött) kan vara annorlunda den dag du hämtar filen, så se till att kommandot stämmer överens med filnamnet som hämtas. Du bör få den här utdatan och ignorera varningen om den betrodda signaturen - det betyder bara att du inte manuellt har sagt till datorn att du litar på den offentliga nyckel som vi importerade tidigare.


![image](assets/13.webp)


Den här bilden har ett tomt alt-attribut; dess filnamn är image-4-1024x165.webp


Detta resultat bekräftar att signaturen är bra, och vi är säkra på att den privata nyckeln för "info@greenaddress.it" signerade data (Hash-rapporten).


Nu ska vi Hash vår nedladdade zip-fil och jämföra utdata som publicerats. Observera att i SHA256SUMS.asc-filen finns det en bit text som säger "Hash: SHA512" vilket förvirrar mig, eftersom filen tydligt har SHA256-utgångar inom, så jag kommer att ignorera det.


För Mac och Linux öppnar du terminalen och navigerar till den plats där zip-filen laddades ner (förmodligen måste du skriva "cd Downloads" igen, såvida du inte har stängt terminalen sedan dess). Förresten kan du alltid kontrollera vilken katalog du befinner dig i genom att skriva PWD ("print working directory"), och om allt detta är främmande kan det vara bra att titta på en snabb YouTube-video genom att söka på "how to navigate the Linux/Mac/Windows file system".


För att hämta filen, skriv så här:


```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```


Du bör kontrollera exakt vad din fil heter och ändra den blå texten ovan om det behövs.


Du kommer att få en utdata som denna (din kommer att skilja sig om filen är annorlunda än min):


![image](assets/14.webp)


Jämför sedan visuellt Hash-utdata med vad som finns i filen SHA256SUMS.asc. Om de matchar, då -> SUCCESS! Vi gratulerar er.


källa: https://armantheparman.com/jade/


### Använder det på Sparrow


Om du redan vet hur du ska använda Sparrow är det som vanligt:


**Note:** det är samma process med Specter till exempel


Ladda ner Sparrow med hjälp av länken som finns här.


![image](assets/14.5.webp)


Klicka på Nästa för att följa installationsguiden och lära dig mer om de olika anslutningsalternativen.


![image](assets/15.webp)


Välj önskad server och välj sedan Create New Wallet.


![image](assets/16.webp)


Ange ett namn för din Wallet och klicka på Skapa Wallet.


![image](assets/17.webp)


Välj önskad policy och skripttyper och välj sedan Connected Hardware Wallet.


**Om du tidigare har använt Blockstream Jade som en Singlesig Wallet med Blockstream Green och vill se dina transaktioner i Sparrow, se till att skripttypen matchar kontotypen som innehåller dina medel i Green. Du kommer också att behöva matcha avledningssökvägen också.


![image](assets/18.webp)


Koppla in din Blockstream Jade och klicka på Scan. Du kommer sedan att uppmanas att ange din PIN-kod på Jade.


**Tips:** Innan du ansluter din Jade, se till att Blockstream Green-appen inte är öppen. Om Green är öppen kan detta orsaka problem med att din Jade upptäcks i Sparrow.


![image](assets/19.webp)


Välj Import Keystore för att importera den offentliga nyckeln för standardkontot eller välj pilen för att manuellt välja den härledningssökväg som du vill använda.


![image](assets/20.webp)


När den önskade nyckeln har importerats klickar du på Apply.


![image](assets/21.webp)


Du har nu framgångsrikt konfigurerat din Wallet och du kan börja ta emot, lagra och spendera din Bitcoin med hjälp av Sparrow och Blockstream Jade.


**Anmärkning:** Om du tidigare använde Jade med Blockstream Green som en Multisig Shield Wallet, ska du inte förvänta dig att din nya Sparrow wallet visar samma saldo - det är olika plånböcker. För att få tillgång till din Multisig Shield Wallet igen, anslut helt enkelt din Jade tillbaka till Blockstream Green.


![image](assets/22.webp)


källa: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-


### Green app


om du är mer en mobil guide kan du använda den med Blockstream Green



- Så här ställer du in Blockstream Jade med Green | Blockstream Jade - https://youtu.be/7aacxnc6DHg
- Hur man tar emot Bitcoin till en Jade Wallet | Blockstream Jade - https://youtu.be/CVtcDdiPqLA