---
name: Seedkeeper - Lösenordshanterare
description: Hur sparar du dina lösenord med Seedkeeper-smartkortet?
---

![cover](assets/cover.webp)



Seedkeeper är ett smartkort som utvecklats av Satochip, ett belgiskt företag som specialiserar sig på hårdvarulösningar för att hantera och skydda digitala hemligheter. Satochip är känt för sitt utbud av smartkort för Bitcoin-ekosystemet och tänkte sig Seedkeeper som ett alternativ till traditionella metoder för att lagra minnesfraser och andra digitala hemligheter.



Rent konkret är Seedkeeper ett multifunktionellt, EAL6-certifierat smartkort med en säker processor och ett manipulationsskyddat minne (ett så kallat "Secure Element"). Som namnet antyder är dess roll att lagra Bitcoin-portföljens mnemonik och lösenord på ett krypterat och skyddat sätt. Med Seedkeeper kan du generate, importera, organisera och spara dina hemligheter direkt i kortets säkra komponent.



Enligt min mening har Seedkeeper två huvudsakliga användningsområden, som vi kommer att utforska i 2 separata tutorials:




- Bitcoin** lagring av minnesfraser: istället för att skriva ner dina 12 eller 24 ord på papper kan du importera dem till smartkortet och skydda dem med en PIN-kod.
- Lösenordshantering**: du kan använda generate starka lösenord via Seedkeeper-applikationen och lagra dem direkt på smartkortet, vilket ger dig en bekväm och lättanvänd lösenordshanterare offline.



Tekniskt sett har Seedkeeper en kapacitet på 8192 bytes, vilket gör att den kan lagra minst 50 separata hemligheter (det exakta antalet beror på deras storlek och de metadata som är kopplade till varje hemlighet). Seedkeeper kan nås antingen [via en smartkortsläsare ansluten](https://satochip.io/accessories/) till en dator, eller via mobilapplikationen med NFC-anslutning. Hela systemet fungerar i offline-läge, utan internetanslutning, vilket garanterar en begränsad attackyta.



![Image](assets/fr/001.webp)



En särskilt intressant funktion är möjligheten att duplicera innehållet i en Seedkeeper till en annan för att skapa en säkerhetskopia. I den här guiden visar vi dig hur du gör just det.



I den här handledningen kommer vi bara att täcka användningen av SeedKeeper för traditionella lösenord, på samma sätt som en lösenordshanterare. Om du vill använda SeedKeeper för att spara Bitcoin wallet mnemoniska fraser, vänligen se denna andra handledning:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Hur skaffar jag en Seedkeeper?



Det finns två huvudsakliga sätt att få tag på din Seedkeeper. Du kan [köpa den direkt från Satochips officiella butik](https://satochip.io/product/seedkeeper/) eller från en auktoriserad återförsäljare. Men eftersom [Seedkeeper-appleten är öppen källkod](https://github.com/Toporin/Seedkeeper-Applet) har du också möjlighet att installera den själv på [ett tomt smartkort](https://satochip.io/product/blank-javacard-for-diy-project/).



Om du vill använda Seedkeepers backupfunktion behöver du naturligtvis köpa två smartcards.



## 2. Installera Seedkeeper-klienten



Det första steget är att installera programvaran på din dator eller smartphone. På en PC behöver du [ladda ner den senaste versionen av Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). För mobiler finns Seedkeeper-programmet tillgängligt i [Google Play Store] (https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) och i [Apple App Store] (https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Initialisering av seedkeeper



Starta programmet och klicka på knappen "*Click & Scan*".



![Image](assets/fr/003.webp)



Du kommer att bli ombedd att ange en PIN-kod för din Seedkeeper. Eftersom det här är ett nytt kort har ingen PIN-kod ännu definierats. Ange valfri kod för att hoppa över detta steg och klicka sedan på "*Nästa*".



![Image](assets/fr/004.webp)



Placera sedan kortet på baksidan av din smartphone. Applikationen kommer att upptäcka att Seedkeeper ännu inte har initialiserats och uppmanar dig att ange PIN-koden för ditt smarta kort, som är mellan 4 och 16 tecken lång. För optimal säkerhet bör du välja en robust PIN-kod som är så lång som möjligt, slumpmässig och består av många olika tecken. PIN-koden är den enda barriären mot fysisk åtkomst till dina lösenord.



**Kom också ihåg att spara denna PIN-kod nu**, till exempel i en lösenordshanterare eller på ett separat fysiskt medium. I det senare fallet får du aldrig förvara mediet som innehåller PIN-koden på samma plats som din Seedkeeper, annars blir denna säkerhet värdelös. Det är viktigt att ha en tillförlitlig backup: utan PIN-koden kommer du inte att kunna återställa de hemligheter som finns lagrade på din Seedkeeper.



![Image](assets/fr/005.webp)



Bekräfta din PIN-kod en gång till.



![Image](assets/fr/006.webp)



Din Seedkeeper är nu initialiserad. Du kan låsa upp den genom att ange den PIN-kod som du just har ställt in.



![Image](assets/fr/007.webp)



Du kommer nu till sidan för hantering av ditt smartkort.



![Image](assets/fr/008.webp)



## 4. Spara lösenord på Seedkeeper



När din Seedkeeper är upplåst klickar du på "*+*"-knappen.



![Image](assets/fr/009.webp)



Välj "Generera hemlighet*". Med alternativet "*Importera en hemlighet*" kan du spara en befintlig hemlighet (t.ex. ett lösenord som du har skapat tidigare).



![Image](assets/fr/010.webp)



I vårt fall vill vi spara ett lösenord. Klicka på "*Lösenord*".



![Image](assets/fr/011.webp)



Tilldela denna hemlighet en "*Label*" så att den lätt kan identifieras om du lagrar flera olika uppgifter i din Seedkeeper. Du kan också lägga till en identifierare som är kopplad till lösenordet och webbadressen till webbplatsen.



![Image](assets/fr/012.webp)



Välj längd och parametrar för ditt lösenord och klicka sedan på "*Generate*" och sedan på "*Import*".



![Image](assets/fr/013.webp)



Placera din Seedkeeper på baksidan av din smartphone.



![Image](assets/fr/014.webp)



Ditt lösenord har registrerats.



![Image](assets/fr/015.webp)



## 5. Få tillgång till ditt Seedkeeper-lösenord



Om du vill kontrollera ditt lösenord tar du fram din Seedkeeper och klickar på knappen "*Click & Scan*".



![Image](assets/fr/016.webp)



Ange din PIN-kod och tryck sedan på "*Nästa*".



![Image](assets/fr/017.webp)



Placera din Seedkeeper på baksidan av din smartphone.



![Image](assets/fr/018.webp)



Då kommer du till en lista över alla dina registrerade hemligheter. I det här exemplet vill jag visa lösenordet för mitt Plan ₿ Academy-konto, så jag klickar på det.



![Image](assets/fr/019.webp)



Tryck på knappen "*Reveal*".



![Image](assets/fr/020.webp)



Skanna din Seedkeeper igen.



![Image](assets/fr/021.webp)



Ditt tidigare sparade lösenord visas nu på skärmen. Du kan kopiera det och använda det på den aktuella webbplatsen.



![Image](assets/fr/022.webp)



## 6. Säkerhetskopiering av Seedkeeper



Vi kommer nu att göra en säkerhetskopia av min Seedkeeper på en andra Seedkeeper så att vi har två kopior. Denna redundans kan vara en del av en strategi för att säkra dina viktigaste lösenord: till exempel förvara dina Seedkeepers på två olika platser för att begränsa fysiska risker, eller anförtro en kopia till en betrodd släkting.



För att göra detta tar du med dig din andra Seedkeeper (kom ihåg att identifiera en av de två med ett märke på den för att undvika förväxling). Börja med att initiera den, enligt beskrivningen i steg 3 i denna handledning. Välj återigen en stark PIN-kod. Beroende på din strategi kan du välja en annan PIN-kod eller behålla samma.



![Image](assets/fr/023.webp)



Öppna programmet, klicka på "*Click & Scan*", ange PIN-koden för din Seedkeeper n°1 (källa) och skanna den sedan.



![Image](assets/fr/024.webp)



Du kommer då till startsidan, med en lista över dina hemligheter. Klicka på de tre små prickarna längst upp till höger i gränssnittet.



![Image](assets/fr/025.webp)



Välj "*Make a backup*" och tryck sedan på "*Start*".



![Image](assets/fr/026.webp)



Ange PIN-koden för ditt backup-kort (Seedkeeper n°2).



![Image](assets/fr/027.webp)



Skanna sedan kortet.



![Image](assets/fr/028.webp)



Gör samma sak med huvudkortet (Seedkeeper n°1) och klicka sedan på "*Make a backup*".



![Image](assets/fr/029.webp)



Din Seedkeeper n°2 innehåller nu alla de hemligheter som finns lagrade på Seedkeeper n°1.



![Image](assets/fr/030.webp)



Du kan skanna din Seedkeeper n°2 för att kontrollera att hemligheterna har kopierats.



![Image](assets/fr/031.webp)



Det är allt som behövs! Nu vet du hur du använder Seedkeeper för att lagra dina lösenord. I en framtida handledning kommer vi att titta på hur man använder Seedkeeper för att säkerhetskopiera en Bitcoin wallet. Jag inbjuder dig också att upptäcka dess kombinerade användning med SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356