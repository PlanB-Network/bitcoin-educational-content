---
name: Seedkeeper
description: Hur säkerhetskopierar jag min wallet Bitcoin med Seedkeeper-smartkortet?
---

![cover](assets/cover.webp)



Seedkeeper är ett smartkort som utvecklats av Satochip, ett belgiskt företag som specialiserar sig på hårdvarulösningar för att hantera och skydda digitala hemligheter. Satochip är känt för sitt utbud av smartkort för Bitcoin-ekosystemet och har designat Seedkeeper som ett alternativ till traditionella metoder för att lagra minnesfraser.



Rent konkret är Seedkeeper ett multifunktionellt, EAL6-certifierat smartkort med en säker processor och ett manipulationsskyddat minne (ett s.k. "Secure Element"). Som namnet antyder är dess roll att lagra Bitcoin wallet mnemonics och lösenord på ett krypterat och skyddat sätt. Med Seedkeeper kan du generate, importera, organisera och spara dina hemligheter direkt i kortets säkra komponent.



Enligt min mening har Seedkeeper två huvudsakliga användningsområden, som vi kommer att utforska i 2 separata tutorials:




- Bitcoin** lagring av minnesfraser: istället för att skriva ner dina 12 eller 24 ord på papper kan du importera dem till smartkortet och skydda dem med en PIN-kod.
- Lösenordshantering**: du kan använda generate starka lösenord via Seedkeeper-applikationen och lagra dem direkt på smartkortet, vilket ger dig en bekväm och lättanvänd lösenordshanterare offline.



Tekniskt sett har Seedkeeper en kapacitet på 8192 bytes, vilket gör att den kan lagra minst 50 separata hemligheter (det exakta antalet beror på deras storlek och de metadata som är kopplade till varje hemlighet). Seedkeeper kan nås antingen [via en smartkortsläsare ansluten](https://satochip.io/accessories/) till en dator, eller via mobilapplikationen med NFC-anslutning. Hela systemet fungerar i offline-läge, utan internetanslutning, vilket garanterar en begränsad attackyta.



![Image](assets/fr/001.webp)



En särskilt intressant funktion är möjligheten att duplicera innehållet i en Seedkeeper till en annan för att skapa en säkerhetskopia. I den här guiden visar vi dig hur du gör just det.



Seedkeeper är också mycket intressant i kombination med wallet:s statslösa hårdvara, t.ex. SeedSigner eller Spectre DIY. I det här fallet behöver man inte använda Satochips klient på datorn eller mobiltelefonen. Seedkeeper håller seed i sin secure element och kan användas direkt med signeringsenheten, vilket eliminerar behovet av en QR-kod i pappersformat. Jag kommer inte att utveckla detta specifika användningsfall i den här handledningen, eftersom det är föremål för en annan dedikerad handledning :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Vilket användningsområde för Seedkeeper?



I den här handledningen kommer jag bara att hantera användningsfall relaterade till Bitcoin, eftersom det är vad den här handledningen handlar om. Vi kommer inte att gå in på lösenordshanteringsfunktionen, som kommer att bli föremål för en annan handledning.



Jämfört med en enkel pappersbackup av den mnemotekniska frasen har användningen av en Seedkeeper flera fördelar:





- Stöldskyddad:** seed i din wallet är inte tillgänglig i klartext. För att få ut den måste du känna till Seedkeeper PIN-koden. En tjuv som får tag på enheten kan inte göra något med den utan denna kod.





- Fördela risken på två faktorer:** Du kan dela upp säkerheten mellan en digital och en fysisk faktor. Om du t.ex. lagrar PIN-koden för Seedkeeper i din lösenordshanterare behöver du både tillgång till lösenordshanteraren och ett fysiskt innehav av smartkortet för att få tag på seed (en betydligt mindre sannolikhet för attack).





- Centraliserad hantering:** Seedkeeper underlättar hanteringen av flera frön från olika portföljer.





- Enkla säkerhetskopior:** duplicera helt enkelt krypterade säkerhetskopior till andra SeedKeepers.



Det finns dock ett antal nackdelar jämfört med en enkel pappersbackup av dina seed:





- Priset:** är visserligen blygsamt (ca 25 euro) men ändå högre än för ett pappersark.





- Beroende av en generell datorenhet:** För att komma in i och hantera seed krävs en dator eller smartphone, vilket innebär att din mnemonic passerar genom en maskin med en mycket bredare attackyta än wallet-hårdvara. Detta kan utgöra en risk om maskinen äventyras. Det är därför jag inte rekommenderar att man använder Seedkeeper för att lagra seed för en wallet-hårdvara (förutom vid statslös användning utan dator, som med SeedSigner). wallet-hårdvarans roll är just att lagra seed i en minimalistisk, mycket säker miljö. Genom att manuellt skriva in din seed på din vanliga dator är den inte längre begränsad till wallet-hårdvaran: den hamnar också på en allmän maskin som utsätts för flera attackvektorer. Så det är bättre att använda Seedkeeper för en varm wallet än för en kall (förutom SeedSigner / stateless wallet-hårdvara).





- Risken för förlust kopplad till PIN-koden:** Den direkta otillgängligheten av seed, till skillnad från en pappersbackup, ger visserligen ett skydd mot fysisk stöld. Men som alltid är säkerhet en balansgång mellan risken för stöld och risken för förlust. Om din säkerhetskopia kräver en PIN-kod kommer förlusten av denna kod att göra det omöjligt att återställa din minnesfras och därmed få tillgång till dina bitcoins.



Med tanke på dessa fördelar och nackdelar anser jag att de bästa användningsområdena för Seedkeeper (bortsett från dess lösenordshanteringsfunktion) är, å ena sidan, att lagra frön från dina **programvaruportföljer**, eftersom de redan finns på din telefon eller dator, eller från din skärmlösa wallet-hårdvara som Satochip, och å andra sidan, att använda den i kombination med statslös wallet-hårdvara som SeedSigner, där den verkligen kommer till sin rätt.



Ett annat särskilt intressant användningsområde för Seedkeeper är möjligheten att på ett säkert och tillförlitligt sätt säkerhetskopiera portföljernas *Descriptors*.



## 2. Hur skaffar jag en Seedkeeper?



Det finns två huvudsakliga sätt att få tag på din Seedkeeper. Du kan [köpa den direkt från Satochips officiella butik](https://satochip.io/product/seedkeeper/) eller från en auktoriserad återförsäljare. Men eftersom [Seedkeeper-appleten är öppen källkod](https://github.com/Toporin/Seedkeeper-Applet) har du också möjlighet att installera den själv på [ett tomt smartkort](https://satochip.io/product/blank-javacard-for-diy-project/).



Om du vill använda Seedkeepers backupfunktion behöver du naturligtvis köpa två smartcards.



## 3. Installera Seedkeeper-klienten



I den här handledningen säkerhetskopierar vi vår seed-portfölj på vår Seedkeeper. Det första steget är att installera programvaran på din dator eller smartphone. På en PC måste du [ladda ner den senaste versionen av Satochip-Utils] (https://github.com/Toporin/Satochip-Utils/releases). På mobilen finns Seedkeeper-applikationen tillgänglig på [Google Play Store] (https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) samt på [Apple App Store] (https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Initialisering av seedkeeper



Starta programmet och klicka på knappen "*Click & Scan*".



![Image](assets/fr/003.webp)



Du kommer att bli ombedd att ange en PIN-kod för din Seedkeeper. Eftersom det här är ett nytt kort har ingen PIN-kod ännu definierats. Ange valfri kod för att hoppa över detta steg och klicka sedan på "*Nästa*".



![Image](assets/fr/004.webp)



Placera sedan kortet på baksidan av din smartphone. Programmet kommer att upptäcka att Seedkeeper ännu inte har initialiserats och uppmanar dig att ange PIN-koden för ditt smarta kort, som ska vara mellan 4 och 16 tecken lång. För optimal säkerhet ska du välja ett starkt lösenord som är så långt som möjligt, slumpmässigt och består av en mängd olika tecken. PIN-koden är den enda barriären mot fysisk tillgång till din återställningsfras.



**Kom också ihåg att spara denna PIN-kod nu**, till exempel i en lösenordshanterare eller på ett separat fysiskt medium. I det senare fallet får du aldrig förvara mediet som innehåller PIN-koden på samma plats som din Seedkeeper, annars blir denna säkerhet värdelös. Det är viktigt att ha en tillförlitlig backup: utan PIN-koden kommer du inte att kunna återställa de hemligheter som finns lagrade på din Seedkeeper.



![Image](assets/fr/005.webp)



Bekräfta din PIN-kod en gång till.



![Image](assets/fr/006.webp)



Din Seedkeeper är nu initialiserad. Du kan låsa upp den genom att ange den PIN-kod som du just har ställt in.



![Image](assets/fr/007.webp)



Du kommer nu till sidan för hantering av ditt smartkort.



![Image](assets/fr/008.webp)



## 5. Registrera en seed på Seedkeeper



När din Seedkeeper är upplåst klickar du på "*+*"-knappen.



![Image](assets/fr/009.webp)



Välj "Importera hemlighet*". Med alternativet "*Generate secret*" kan du skapa en ny minnesfras direkt i programmet.



![Image](assets/fr/010.webp)



I vårt fall vill vi spara seed i vår portfölj. Klicka på "*Mnemonic*".



![Image](assets/fr/011.webp)



Tilldela denna hemlighet en "*Label*" så att den lätt kan identifieras om du lagrar flera uppgifter i din Seedkeeper.



![Image](assets/fr/012.webp)



Ange sedan din återställningsfras i det angivna fältet. Om du vill kan du också lägga till en passphrase BIP39 eller dina *Descriptors*. Klicka sedan på "Importera*".



![Image](assets/fr/013.webp)



*Den mnemonik som visas i den här bilden är fiktiv och tillhör inte någon. Det är bara ett exempel. Avslöja aldrig din egen minnesregel för någon, annars kommer dina bitcoins att bli stulna



Placera din Seedkeeper på baksidan av din smartphone.



![Image](assets/fr/014.webp)



Din seed har registrerats.



![Image](assets/fr/015.webp)



## 6. Få tillgång till din seed på Seedkeeper



Om du vill kontrollera din mnemoniska fras, ta upp din Seedkeeper och klicka på knappen "*Click & Scan*".



![Image](assets/fr/016.webp)



Ange din PIN-kod och tryck sedan på "*Nästa*".



![Image](assets/fr/017.webp)



Placera din Seedkeeper på baksidan av din smartphone.



![Image](assets/fr/018.webp)



Detta tar dig till en lista över alla dina registrerade hemligheter. I det här exemplet vill jag visa seed för min portfölj "*Blockstream App*", så jag klickar på den.



![Image](assets/fr/019.webp)



Tryck på knappen "*Reveal*".



![Image](assets/fr/020.webp)



Skanna din Seedkeeper igen.



![Image](assets/fr/021.webp)



Din tidigare inspelade minnesfras visas nu på skärmen.



![Image](assets/fr/022.webp)



## 7. Säkerhetskopiering av Seedkeeper



Vi ska nu göra en säkerhetskopia av min Seedkeeper på en andra Seedkeeper så att vi har två kopior. Denna redundans kan vara en del av en strategi för att säkra dina bitcoins: till exempel att lagra din fras på två separata platser för att begränsa fysiska risker, eller anförtro en kopia till en betrodd släkting som en del av en arvsplan.



För att göra detta tar du med dig din andra Seedkeeper (kom ihåg att identifiera en av de två med ett märke på den för att undvika förväxling). Börja med att initiera den, enligt beskrivningen i steg 4 i denna handledning. Välj ett starkt lösenord igen. Beroende på din strategi kan du välja ett annat lösenord eller behålla samma.



![Image](assets/fr/023.webp)



Öppna programmet, klicka på "*Click & Scan*", ange lösenordet för din Seedkeeper n°1 (källa) och skanna den sedan.



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



Det är allt som behövs! Nu vet du hur du använder Seedkeeper för att spara den mnemoniska frasen för en Bitcoin wallet. I en framtida handledning kommer vi att titta på hur du använder Seedkeeper för att lagra dina lösenord. Jag inbjuder dig också att upptäcka dess kombinerade användning med SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

I den här handledningen har vi nämnt ***Descriptors*** i din Bitcoin-portfölj flera gånger. Vet du inte vad de är? I så fall rekommenderar jag att du tar vår kostnadsfria CYP 201-utbildningskurs, som går in på djupet i detalj om alla mekanismer som är involverade i att driva HD-portföljer!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f