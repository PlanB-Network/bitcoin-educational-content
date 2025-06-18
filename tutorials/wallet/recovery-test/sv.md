---
name: Återhämtningstest
description: Hur testar du dina säkerhetskopior för att säkerställa att du inte förlorar dina bitcoins?
---
![cover](assets/cover.webp)


När du skapar en Bitcoin Wallet ombeds du att anteckna en Mnemonic-fras, som vanligtvis består av 12 eller 24 ord. Denna fras gör att du kan återfå åtkomst till dina bitcoins vid förlust, skada eller stöld av enheten som är värd för din Wallet. Innan du börjar använda din nya Bitcoin Wallet är det mycket viktigt att du verifierar giltigheten av denna Mnemonic-fras. Det bästa sättet att göra detta är genom att utföra ett återställningstest.


Detta test innebär att man simulerar en Wallet-återställning innan man sätter in några bitcoins i den. Så länge Wallet är tom simulerar vi en situation där enheten som innehåller våra nycklar går förlorad, och allt vi har kvar är vår Mnemonic-fras för att försöka återfå våra bitcoins.


![RECOVERY TEST](assets/notext/01.webp)


## Vad är syftet?


Denna testprocess gör att du kan verifiera att den fysiska säkerhetskopian av din Mnemonic-fras, oavsett om den är på papper eller metall, är funktionell. Ett misslyckande under detta återställningstest signalerar ett fel i säkerhetskopian av frasen och sätter därmed dina bitcoins i riskzonen. Å andra sidan, om testet lyckas, bekräftar det att din Mnemonic-fras är fullt fungerande, och du kan sedan säkra bitcoins med sinnesfrid med hjälp av denna Wallet.


Att utföra en torrkörning av återställningstestet har en dubbel fördel. Det ger dig inte bara möjlighet att kontrollera noggrannheten i din Mnemonic-fras, utan det ger dig också möjlighet att bekanta dig med Wallet-återställningsprocessen. På så sätt upptäcker du potentiella svårigheter innan du ställs inför en verklig situation. Den dag du faktiskt behöver återställa din Wallet kommer du att vara mindre stressad, eftersom du redan känner till processen, vilket minskar risken för fel. Det är därför det är viktigt att inte försumma detta teststeg och att ta den tid som krävs för att göra det på rätt sätt.


## Vad är ett återhämtningstest?


Processen för testet är ganska enkel:


- Efter att ha skapat din nya Bitcoin Wallet, och innan du sätter in dina första satoshis, anteckna en vittnesinformation som en xpub, den första mottagande Address, eller till och med huvudnyckelns fingeravtryck;
- Ta sedan avsiktligt bort den fortfarande tomma Wallet, till exempel genom att återställa din Hardware Wallet till fabriksinställningarna;
- Simulera sedan en återställning av din Wallet med hjälp av endast pappersbackuperna av din Mnemonic-fras och din passphrase om du använder en sådan;
- Kontrollera slutligen om vittnesinformationen matchar den för den regenererade Wallet. Om informationen matchar kan du vara säker på att din fysiska säkerhetskopia är tillförlitlig och du kan sedan skicka dina första bitcoins till denna Wallet.

Var försiktig, under ett återställningstest måste **du använda samma enhet som är avsedd för din slutliga Wallet**, för att inte öka attackytan för din Wallet. Om du till exempel skapar en Wallet på en Trezor Safe 5, se till att du utför återställningstestet på samma Trezor Safe 5. Det är viktigt att du inte anger din återställningsfras i någon annan programvara, eftersom detta skulle äventyra säkerheten som tillhandahålls av din Hardware Wallet, även om Wallet fortfarande är tom.


## Hur utför man ett återställningstest?


I den här handledningen kommer jag att förklara hur man utför ett återställningstest på en Bitcoin Software Wallet, med Sparrow Wallet (för en Hot Wallet). Processen förblir dock densamma för alla andra typer av enheter. Återigen, **om du använder en Hardware Wallet ska du inte utföra återställningstestet på Sparrow Wallet** (se föregående avsnitt).


Jag har precis skapat en ny Hot Wallet på Sparrow Wallet. För tillfället har jag ännu inte skickat några bitcoins till den. Den är tom.


![RECOVERY TEST](assets/notext/02.webp)


Jag har noggrant noterat min Mnemonic-fras på 12 ord på ett papper. Och eftersom jag vill öka säkerheten för denna Wallet har jag också skapat en BIP39 passphrase som jag har sparat på ett annat papper:


```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```


```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```


***Självklart ska du aldrig dela din Mnemonic-fras och din passphrase på internet, till skillnad från vad jag gör i den här handledningen. Detta exempel Wallet kommer inte att användas och kommer att raderas i slutet av handledningen.***


Jag kommer nu att anteckna ett vittnesinformation från min Wallet på ett utkast. Du kan välja olika uppgifter, till exempel den första mottagande Address, xpuben eller huvudnyckelns fingeravtryck. Personligen rekommenderar jag att du väljer den första mottagande Address. Detta gör att du kan verifiera att du kan hitta den fullständiga första avledningsvägen som leder till denna Address.


På Sparrow klickar du på fliken "*Addresser*".


![RECOVERY TEST](assets/notext/03.webp)


Anteckna sedan på ett papper den allra första mottagningen Address av din Wallet. I mitt exempel är Address:


```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```


När du har antecknat informationen går du till menyn "*File*" och väljer sedan "*Delete Wallet*". Jag påminner dig än en gång om att din Bitcoin Wallet måste vara tom innan du fortsätter med denna operation.


![RECOVERY TEST](assets/notext/04.webp)


Om din Wallet verkligen är tom, bekräfta borttagningen av din Wallet.


![RECOVERY TEST](assets/notext/05.webp)


Nu måste du upprepa skapandeprocessen för Wallet, men använda våra pappersbackuper. Klicka på menyn "*File*" och sedan på "*New Wallet*".


![RECOVERY TEST](assets/notext/06.webp)


Ange namnet på din Wallet igen.


![RECOVERY TEST](assets/notext/07.webp)


I menyn "*Script Type*" måste du välja samma skripttyp som den Wallet du tidigare raderade.


![RECOVERY TEST](assets/notext/08.webp)


Klicka sedan på knappen "*Ny eller importerad Software Wallet*".


![RECOVERY TEST](assets/notext/09.webp)


Välj rätt antal ord för din seed.


![RECOVERY TEST](assets/notext/10.webp)


Ange din Mnemonic-fras i programvaran. Om meddelandet "*Invalid Checksum*" visas innebär det att säkerhetskopian av din Mnemonic-fras är felaktig. Du kommer då att behöva börja skapa din Wallet från början, eftersom ditt återställningstest har misslyckats.


![RECOVERY TEST](assets/notext/11.webp)


Om du har en passphrase, som i mitt fall, ska du också ange den.


![RECOVERY TEST](assets/notext/12.webp)


Klicka på "*Create Keystore*" och sedan på "*Import Keystore*".


![RECOVERY TEST](assets/notext/13.webp)


Slutligen klickar du på knappen "*Apply*".


![RECOVERY TEST](assets/notext/14.webp)


Du kan nu återgå till fliken "*Addresser*".


![RECOVERY TEST](assets/notext/15.webp)


Kontrollera slutligen att den första mottagande Address stämmer överens med den som du noterade som vittne i ditt utkast.


![RECOVERY TEST](assets/notext/16.webp)


Om de mottagande adresserna matchar är ditt återställningstest framgångsrikt och du kan använda din nya Bitcoin Wallet. Om de inte matchar kan detta tyda på antingen ett fel i valet av skripttyp, vilket gör att härledningsvägen blir felaktig, eller ett problem med säkerhetskopian av din Mnemonic-fras eller din passphrase. I båda fallen rekommenderar jag starkt att du börjar om från början och skapar en ny Bitcoin Wallet från början för att undvika alla risker. Den här gången ska du vara noga med att notera Mnemonic-frasen utan fel.

Grattis, du är nu igång med att genomföra ett återställningstest! Jag råder dig att generalisera denna process för att skapa alla dina Bitcoin plånböcker. Om du tyckte att den här handledningen var till hjälp skulle jag uppskatta om du kunde lämna tummen upp nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!