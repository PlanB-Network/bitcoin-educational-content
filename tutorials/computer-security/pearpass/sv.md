---
name: PearPass
description: Återta kontrollen över dina lösenord med en lokal, peer-to-peer, molnfri lösenordshanterare
---

![cover](assets/cover.webp)



I en tid när varje individ hanterar dussintals, till och med hundratals onlinekonton, har säkerheten för inloggningar blivit en central fråga inom IT-säkerhet. Sociala nätverk, meddelandesystem, professionella tjänster, finansiella plattformar: var och en av dessa åtkomster är beroende av en hemlighet, vars avslöjande kan få allvarliga konsekvenser för ditt liv.



Trots detta, och trots ökningen av attacker, är dåliga rutiner fortfarande mycket utbredda bland befolkningen: svaga lösenord, återanvända lösenord, lösenord som lagras i klartext eller som bara memoreras ungefärligt. För att lösa dessa problem utan att komplicera vardagen är lösningen att använda en lösenordshanterare.



Dussintals lösenordshanterare finns redan, och Plan ₿ Academy erbjuder en handledning för de flesta av dem. Men i den här handledningen skulle jag vilja presentera dig för en som tydligt sticker ut från resten när det gäller hur den fungerar: **PearPass**.



**PearPass är en peer-to-peer-lösenordshanterare, local-first och öppen källkod, utformad för att ge användaren full kontroll över sina data.**



![Image](assets/fr/01.webp)



## Varför välja PearPass?



En lösenordshanterare är en programvara som genererar, lagrar och organiserar alla dina lösenord på ett säkert sätt. I stället för att memorera eller återanvända lösenord har du bara en hemlighet att skydda: huvudlösenordet, som krypterar hela ditt kassaskåp. Det här tillvägagångssättet gör det möjligt att använda unika, långa och slumpmässiga lösenord för varje tjänst, vilket minskar både risken för att glömma och kompromissa, samtidigt som det begränsar effekterna av en eventuell läcka. Idag är det ett grundläggande IT-verktyg som alla borde använda.



Det finns två huvudkategorier av lösenordshanterare. Å ena sidan finns det endast lokal programvara, vilket är mycket säkert eftersom data aldrig lagras på en central server, men inte särskilt praktiskt, eftersom det inte tillåter dig att enkelt synkronisera dina referenser mellan flera enheter (dator, smartphone, surfplatta ...). Å andra sidan lagrar molnbaserade lösenordshanterare dina inloggningsuppgifter på sina servrar och synkroniserar dem mellan alla dina enheter. Deras främsta fördel är bekvämligheten, men de innebär en kompromiss när det gäller säkerhet, eftersom dina lösenord lagras på infrastrukturer som du inte har någon kontroll över.



PearPass bryter medvetet med båda modellerna. Den positionerar sig mellan lokala hanterare och molnlösningar: den möjliggör synkronisering av dina lösenord, samtidigt som den garanterar att de aldrig lagras på fjärrservrar. Som ett resultat lagras alla dina referenser lokalt på dina enheter, och synkronisering mellan flera maskiner är uteslutande peer-to-peer. Den här arkitekturen eliminerar de enskilda felkällor som är förknippade med centraliserade databaser: det finns inga servrar att kompromissa med och ingen infrastruktur från tredje part som kan komma åt dina inloggningsuppgifter. Kommunikationen mellan dina enheter är krypterad från början till slut, vilket säkerställer att endast de nycklar du har tillgång till ger åtkomst till data.



![Image](assets/fr/02.webp)



För att göra detta möjligt förlitar sig PearPass, som namnet antyder, på **Pears**, ett ekosystem för peer-to-peer-teknik som är dedikerat till skapande och exekvering av serverlösa applikationer. Pears tillhandahåller den exekveringsmiljö, de distributionsmekanismer och de nätverkslager som behövs för att köra helt decentraliserade applikationer, som kan synkroniseras direkt mellan peers utan någon central infrastruktur. När det gäller PearPass tillhandahåller Pears enhetsupptäckt, krypterad anslutningsetablering och synkronisering av lösenordsvalv mellan dina maskiner. Detta tillvägagångssätt säkerställer att PearPass förblir funktionell, motståndskraftig och oberoende av någon extern myndighet.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Utöver denna innovativa arkitektur är PearPass helt öppen källkod och alla dess funktioner är kostnadsfria. Programvaran har också granskats oberoende av Secfault Security. Förutom sin specifika arkitektur erbjuder PearPass naturligtvis alla de klassiska funktioner som förväntas av en bra lösenordshanterare, vilket vi kommer att upptäcka under hela denna handledning.



Kort sagt, där traditionella lösenordshanterare ber dig att lita på ett företag och dess servrar, antar PearPass en suveränitetslogik: inget moln, inga centraliserade konton, inga mellanhänder. Du behåller exklusiv kontroll över dina referenser, samtidigt som du drar nytta av synkronisering mellan dina enheter.



## Hur installerar jag PearPass?



PearPass finns tillgänglig på alla plattformar: Windows, Linux, macOS, Android, iOS och webbläsartillägg. Det finns inget behov av att installera Pears på din maskin: PearPass fungerar på egen hand.



### Installation i Windows



På Windows levereras PearPass som en klassisk installatör. Gå till [den officiella nedladdningssidan](https://pass.pears.com/download) och klicka sedan på knappen `Download Windows installer`.



När filen har laddats ner öppnar du installationsprogrammet och följer de steg som anges av guiden. Programmet kan sedan nås från "Startmenyn" eller via en genväg på skrivbordet.



![Image](assets/fr/03.webp)



### Installation på macOS



På macOS distribueras PearPass som en diskavbildning (`.dmg`). Gå till [den officiella nedladdningssidan](https://pass.pears.com/download) och välj den version som motsvarar din Macs arkitektur (Intel eller Apple Silicon). Efter nedladdningen öppnar du filen `.dmg` och startar programmet från mappen `Applications`.



Vid första uppstarten visar macOS ett säkerhetsmeddelande som anger att programmet kommer från Internet: bekräfta bara för att fortsätta.



### Installation på Linux



På Linux finns PearPass tillgängligt i formatet `.AppImage`, vilket garanterar bred kompatibilitet med de flesta distributioner utan några specifika beroenden. Ladda ner filen `.AppImage` från [den officiella nedladdningssidan](https://pass.pears.com/download) och starta den sedan direkt genom att dubbelklicka.



Beroende på din miljö kan du behöva göra filen körbar via filegenskaper (högerklicka) eller med kommandot `chmod +x`. När PearPass har auktoriserats startar den som en fristående applikation.



### Installation av webbläsartillägg



PearPass erbjuder ett webbläsartillägg för automatisk inloggning och snabb åtkomst till ditt kassaskåp när du surfar på webben. Tillägget är för närvarande tillgängligt för Google Chrome och kompatibla webbläsare. För att installera det, gå till [den officiella nedladdningssidan](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



När du har lagt till det kan du fästa det i verktygsfältet för snabb åtkomst. För att aktivera tillägget krävs sedan en länk till PearPass-programmet som är installerat lokalt på din dator (vi återkommer till detta senare i handledningen).



### Installation på iOS och Android



På iPhone och Android laddar du helt enkelt ner applikationen från din appbutik:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Förutom dessa klassiska installationsmetoder är det också möjligt att ladda ner programvaran direkt från GitHub-arkiv, för varje :




- [Skrivbord](https://github.com/tetherto/pearpass-app-desktop);
- [Mobil](https://github.com/tetherto/pearpass-app-mobile);
- [Webbläsartillägg](https://github.com/tetherto/pearpass-app-browser-extension).



När PearPass har installerats på en eller flera plattformar kan du gå vidare till den inledande konfigurationen. I den här handledningen börjar vi med att konfigurera programvaran på skrivbordet och synkroniserar den sedan med webbläsartillägget och mobilapplikationen.



## Hur skapar jag ett PearPass kassaskåp?



När du först startar PearPass på din dator guidar programmet dig genom två steg: att ställa in ditt huvudlösenord och sedan skapa ditt första kassaskåp.



### Ange huvudlösenord



När programmet först startas upp på skrivbordet klickar du på knappen "Hoppa över" och sedan på "Fortsätt" för att gå igenom introduktionsskärmen och nå konfigurationssteget för huvudlösenordet.



![Image](assets/fr/06.webp)



Därefter kommer det viktiga steget att välja ditt huvudlösenord. Som vi såg i inledningen är detta lösenord mycket viktigt, eftersom det ger dig tillgång till alla dina andra lösenord som sparats på hanteraren. Tekniskt sett används det för att härleda de kryptografiska nycklar som används för att kryptera dina data.



Huvudlösenordet medför två huvudsakliga risker: förlust och kompromettering. Om du förlorar åtkomsten till detta lösenord kommer du inte längre att kunna komma åt dina inloggningsuppgifter. PearPass lagrar nämligen aldrig ditt huvudlösenord: **om det går förlorat, är dina inloggningsuppgifter förlorade för alltid**. Det finns ingen återställningsmekanism. Omvänt, om detta lösenord komprometteras och en angripare får tillgång till en av dina enheter, kommer denne att kunna få tillgång till samtliga dina konton.



För att begränsa risken för förlust kan du göra en fysisk säkerhetskopia av ditt huvudlösenord, t.ex. på papper, och förvara den på en säker plats. Försegla helst denna säkerhetskopia i ett kuvert så att du med jämna mellanrum kan kontrollera att den inte har öppnats. Däremot ska du aldrig göra en digital säkerhetskopia av lösenordet.



För att minska risken för intrång måste ditt huvudlösenord vara starkt. Det ska vara så långt som möjligt, innehålla ett stort antal olika tecken och väljas på ett slumpmässigt sätt. År 2025 är minimirekommendationerna minst 13 tecken, inklusive stora och små bokstäver, siffror och symboler, förutsatt att lösenordet är slumpmässigt. Jag skulle dock rekommendera ett lösenord på minst 20 tecken, om inte mer, med alla typer av tecken, för att säkerställa en mer varaktig säkerhetsnivå.



Ange ditt huvudlösenord i det angivna fältet, bekräfta det en gång till och klicka sedan på knappen "Fortsätt".



![Image](assets/fr/07.webp)



Du kommer då att omdirigeras till inloggningsskärmen: ange ditt huvudlösenord för att kontrollera att allt fungerar korrekt.



![Image](assets/fr/08.webp)



### Skapa ditt första kassaskåp



När du har loggat in kommer PearPass att uppmana dig att skapa ditt första kassaskåp. Ett kassaskåp är en krypterad behållare där dina lösenord, ID, säkra anteckningar och annan information lagras. Varje kassaskåp är isolerat och kan identifieras med ett distinkt namn, så att du kan organisera dina data enligt dina användningsområden (personligt, professionellt, specifika projekt ...).



Klicka på knappen `Create a new vault` (Skapa ett nytt valv).



![Image](assets/fr/09.webp)



Välj ett namn för valvet och klicka sedan på `Create a new vault` igen för att slutföra skapandet.



![Image](assets/fr/10.webp)



Ditt kassaskåp är omedelbart redo att användas. Du kan börja lägga till lösenord, inloggningar eller säkra anteckningar direkt.



![Image](assets/fr/11.webp)



## Hur lägger jag till en inloggning i PearPass?



När du har skapat ditt kassaskåp kan du börja spara dina föremål i det. PearPass stöder registrering av många typer av föremål:




- inloggning till en webbplats eller tjänst ;
- identitet: din personliga information för att snabbt fylla i formulär, men också för att lagra identitetshandlingar direkt i PearPass ;
- kreditkort: dina kreditkortsuppgifter för snabbare betalning när du handlar online;
- Wi-Fi: Lösenord för dina Wi-Fi-nätverk ;
- PassPhrase: hemlig fras som består av flera ord (varning: Jag avråder starkt från att använda den för wallet Bitcoin minnesfraser);
- notera: skapa säkra anteckningar ;
- custom: med den här funktionen kan du skapa en egen elementtyp som är anpassad till dina specifika behov.



Börja med att öppna PearPass och logga in med ditt huvudlösenord.



![Image](assets/fr/12.webp)



Välj det kassaskåp där du vill spara identifieraren.



![Image](assets/fr/13.webp)



På startsidan klickar du på knappen för att lägga till ett nytt objekt, beroende på vilken typ av information du vill registrera. I mitt fall vill jag lägga till en inloggning för mitt konto på Plan ₿ Academy:s webbplats, så jag klickar på knappen "Skapa en inloggning".



![Image](assets/fr/14.webp)



När du har valt vilken typ av objekt du vill lägga till visas ett formulär där du kan ange den information som är kopplad till tjänsten i fråga. Beroende på dina behov kan du ange tjänstens namn, inloggning, lösenord och, om så krävs, webbplatsens adress och ytterligare anteckningar.



PearPass har också en lösenordsgenerator, så att du kan skapa ett starkt lösenord direkt från formuläret. För att använda den, klicka på ikonen som representerar tre små prickar i fältet `Lösenord`, välj önskad längd och klicka sedan på `Insätt lösenord`.



När alla fält har fyllts i klickar du på knappen `Spara` för att spara identifieraren i kassaskåpet.



![Image](assets/fr/15.webp)



Identifieraren är nu sparad. Den visas i listan över objekt i det valda kassaskåpet och kan visas genom att klicka på den.



![Image](assets/fr/16.webp)



Du kan enkelt ändra ett element genom att klicka på det och sedan på knappen `Edit`. Du kan också ta bort det genom att klicka på de tre små prickarna längst upp till höger i gränssnittet och sedan på `Delete element`.



![Image](assets/fr/22.webp)



På mobilen förblir logiken densamma, även om gränssnittet har anpassats. När du har loggat in väljer du önskat kassaskåp, trycker på `+`-knappen, väljer vilken typ av objekt som ska skapas och fyller sedan i nödvändig information.



![Image](assets/fr/17.webp)



## Hur organiserar man PearPass?



Som vi såg i de tidigare avsnitten kan du med PearPass skapa flera olika valv. Detta gör det möjligt att separera olika användningsområden och utgör en första organisationsnivå för din lösenordshanterare. Från startsidan kan du enkelt växla från ett valv till ett annat genom att klicka på pilen längst upp till vänster i gränssnittet.



![Image](assets/fr/18.webp)



Ett annat sätt att organisera dina lösenord, även inom ett valv, är att skapa mappar. För att göra detta klickar du på symbolen `+` i gränssnittets vänstra kolumn bredvid `All Folders` och anger sedan namnet på den mapp du vill skapa.



![Image](assets/fr/19.webp)



Du kan sedan lagra de identifierare som du vill, antingen direkt när du skapar ett objekt eller senare genom att klicka på "Redigera". Allt du behöver göra är att välja önskad mapp i det övre vänstra hörnet av formuläret.



![Image](assets/fr/20.webp)



När du har öppnat ett objekt, t.ex. en inloggning, kan du klicka på stjärnikonen längst upp till höger i gränssnittet för att lägga till det bland dina favoriter. Favoriter kan snabbt hittas i en dedikerad mapp, utöver deras basmapp.



![Image](assets/fr/21.webp)



Slutligen finns det ett sökfält högst upp i gränssnittet, så att du snabbt kan hitta det objekt du letar efter, även om ditt valv innehåller många identifierare.



## Hur synkroniserar jag PearPass på min mobil?



Nu när du har ett fungerande valv med objekt som lagras på din dator vill du förmodligen komma åt dina lösenord från din smartphone eller annan enhet. PearPass låter dig synkronisera din chef på flera maskiner på ett säkert sätt med hjälp av Pears. Låt oss ta reda på hur.



Börja med att logga in på källmaskinen (t.ex. din dator) med hjälp av ditt huvudlösenord. När du är på startsidan klickar du på knappen "Lägg till en enhet" längst ner till höger i gränssnittet.



![Image](assets/fr/23.webp)



PearPass genererar sedan en inbjudningslänk, även tillgänglig som en QR-kod, för att synkronisera det valda valvet på den enhet du väljer.



![Image](assets/fr/24.webp)



Om du vill synkronisera på din mobila enhet måste du först installera programmet och sedan starta det. Du kommer att bli ombedd att skapa ett huvudlösenord för din mobila hanterare. Du kan välja att använda samma lösenord som på din dator eller ett annat. Följ i alla fall samma rekommendationer: ett starkt, slumpmässigt lösenord sparat på ett fysiskt medium.



![Image](assets/fr/25.webp)



Du kan sedan aktivera biometrisk autentisering om du vill, så att du inte behöver ange ditt huvudlösenord manuellt varje gång du låser upp din mobil.



![Image](assets/fr/26.webp)



Ange ditt huvudlösenord på nytt och klicka sedan på knappen "Fortsätt".



![Image](assets/fr/27.webp)



Välj alternativet `Load a vault`, klicka sedan på `Scan QR Code` och skanna QR-koden för inbjudan som visas av PearPass på din källmaskin (datorn).



![Image](assets/fr/28.webp)



Dina valv på din dator och din mobil är nu synkroniserade. Varje ID som läggs till på en enhet kommer att lagras säkert och replikeras på den andra.



![Image](assets/fr/29.webp)



På mobil kan du även, om du vill, aktivera automatisk ifyllning av fält. För att göra detta, gå till `Settings > Advanced` och klicka sedan på knappen `Set as Default` i avsnittet `Autofill`.



![Image](assets/fr/30.webp)



## Hur synkroniserar jag PearPass med webbläsartillägget?



Att ha en lösenordshanterare som är synkroniserad mellan din dator och din smartphone är redan mycket praktiskt, men att integrera den direkt i din webbläsare är ännu mer praktiskt. För att göra det, börja med att [lägga till det officiella PearPass-tillägget i din webbläsare](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Från PearPass-programvaran som är installerad på din lokala maskin, gå till "Inställningar > Avancerat" och aktivera sedan alternativet "Aktivera webbläsartillägg".



![Image](assets/fr/32.webp)



PearPass genererar en token parningsfil. Kopiera den.



![Image](assets/fr/33.webp)



Öppna sedan PearPass-tillägget i din webbläsare, klistra in token-parningen och klicka på knappen `Verify`, följt av `Complete`.



![Image](assets/fr/34.webp)



Din lösenordshanterare är nu synkroniserad med webbläsartillägget.



![Image](assets/fr/35.webp)



Du kan nu använda den för att enkelt ansluta till dina olika webbkonton.



![Image](assets/fr/36.webp)



Nu vet du hur du använder lösenordshanteraren PearPass. Utöver detta verktyg är den dagliga digitala säkerheten beroende av att lämpliga lösningar används på rätt sätt. Om du vill lära dig hur du skapar en säker, stabil och effektiv personlig digital miljö, inbjuder jag dig att upptäcka vår utbildningskurs som är avsedd för detta ämne:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1