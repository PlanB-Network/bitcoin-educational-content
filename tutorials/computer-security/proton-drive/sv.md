---
name: Proton Drive
description: Implementering av backup
---
![cover](assets/cover.webp)


I dag är det viktigt att ha en strategi för att säkerställa tillgänglighet, säkerhet och säkerhetskopiering av dina personliga filer, t.ex. personliga dokument, foton eller viktiga projekt. Att förlora dessa data kan vara katastrofalt.


För att förhindra dessa problem rekommenderar jag att du gör flera säkerhetskopior av dina filer på olika medier. En vanlig strategi inom databehandling är "3-2-1"-backupstrategin, som säkerställer att dina filer skyddas:


- 3** kopior av dina filer;
- Sparas på minst **2** olika typer av media;
- Med minst **1** kopia som förvaras utanför webbplatsen.


Med andra ord är det lämpligt att lagra dina filer på tre olika platser med hjälp av olika typer av media, t.ex. din dator, en extern Hard-enhet, ett USB-minne eller en lagringstjänst online. Och slutligen, att ha en extern kopia innebär att du bör ha en säkerhetskopia lagrad utanför ditt hem eller företag. Den här sista punkten hjälper dig att undvika total förlust av dina filer vid lokala katastrofer som bränder eller översvämningar. En extern kopia, långt från ditt hem eller företag, säkerställer att dina data överlever oavsett lokala risker.


För att underlätta implementeringen av 3-2-1 backup-strategin kan du använda en lagringstjänst online. Dessa lösningar, som ofta kallas "moln", erbjuder ytterligare skydd genom att lagra dina data på säkra servrar som är tillgängliga från vilken enhet som helst. Termen "moln" hänvisar helt enkelt till lagring av data på externa servrar.


Många använder lagringslösningar från stora digitala företag: Google Drive, Microsoft OneDrive eller Apple iCloud.

![PROTON DRIVE](assets/notext/01.webp)

Dessa lösningar är praktiska för daglig användning och säkerställer tillgängligheten till dina data, men de garanterar inte sekretess. I den här handledningen föreslår jag att du upptäcker en annan lösning, lika lätt att använda som Big Techs lagringsverktyg, men med ytterligare åtgärder för att skydda din integritet. Denna lösning är Proton Drive, online-lagringsverktyget från det schweiziska företaget Proton. Vi kommer också att se hur man enkelt kan implementera en 3-2-1-strategi som är lämplig för daglig användning.


## Introduktion till Proton Drive

Proton Drive är en spännande lösning för lagring online eftersom den kombinerar användarvänlighet med säkerhet för dina filer. Till skillnad från traditionella molntjänster från teknikjättar genomför Proton Drive åtgärder för att skydda din integritet. Det säkerställer end-to-end-kryptering för alla dina filer, vilket innebär att inte ens Protons team kan komma åt dina data. Dessutom är Proton Drive öppen källkod, vilket gör det möjligt för oberoende experter att fritt granska programvarans kod.

![PROTON DRIVE](assets/notext/02.webp)

Protons affärsmodell bygger på ett prenumerationssystem, vilket är betryggande eftersom det indikerar att företaget finansieras utan att nödvändigtvis utnyttja sina användares data. I den här handledningen kommer jag att förklara hur man använder gratisversionen av Proton Drive, men det finns också flera prenumerationsnivåer som erbjuder fler funktioner. Denna affärsmodell är att föredra framför ett gratissystem i stil med Big Tech, vilket kan leda till att man undrar om våra personuppgifter används i vinstsyfte. Detta verkar inte vara fallet med Proton.


Proton Drive erbjuder mycket mer än enkla lagringsalternativ; det gör det också möjligt att dela, redigera och samarbeta om dokument online med redigeringsverktyg, liknande Googles programvarusvit.


När det gäller [prissättning] (https://proton.me/pricing) erbjuder den kostnadsfria versionen upp till 5 GB lagringsutrymme och innehåller grundläggande funktioner. För att utöka kapaciteten till 200 GB lagringsutrymme finns en särskild prenumeration på Proton Drive tillgänglig för 4 € per månad. Proton Unlimited-paketet, å andra sidan, erbjuder för 10 € per månad ett lagringsutrymme på upp till 500 GB på Proton Drive, förutom att inkludera alla Protons betaltjänster, till exempel VPN och lösenordshanterare, samt ytterligare fördelar med gratisverktyg (e-post och kalender).

![PROTON DRIVE](assets/notext/03.webp)

## Hur skapar jag ett Proton-konto?


Om du ännu inte har ett Proton-konto måste du skapa ett. Jag hänvisar dig till vår Proton Mail-handledning där vi förklarar i detalj hur du skapar ett gratis Proton-konto och ställer in det:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![PROTON DRIVE](assets/notext/04.webp)

## Hur ställer man in Proton Drive?


När du är inloggad på din Proton-mail klickar du på ikonen med fyra små rutor längst upp till vänster på skärmen.

![PROTON DRIVE](assets/notext/05.webp)

Klicka sedan på "*Drive*".

![PROTON DRIVE](assets/notext/06.webp)

Du befinner dig nu på din Proton Drive.

![PROTON DRIVE](assets/notext/07.webp)

## Hur använder man Proton Drive?

För att lägga till filer på din Proton Drive, när du enbart använder webbversionen (vi kommer att diskutera användningen av den lokala versionen senare), behöver du bara dra och släppa dina dokument direkt till Interface. ![PROTON DRIVE](assets/notext/08.webp) Du kan sedan hitta ditt dokument på startsidan. ![PROTON DRIVE](assets/notext/09.webp) För att lägga till ett nytt objekt klickar du på knappen "*Ny*" längst upp till vänster på skärmen. ![PROTON DRIVE](assets/notext/10.webp) Funktionen "*Ladda upp fil*" öppnar din lokala filutforskare, så att du kan välja och importera nya dokument till Proton Drive, precis som du skulle göra genom att dra och släppa. ![PROTON DRIVE](assets/notext/11.webp) Med "*Upload folder*" kan du importera en hel mapp. ![PROTON DRIVE](assets/notext/12.webp) "*Ny mapp*" gör att du kan skapa en mapp för att bättre organisera dina dokument på Proton Drive. ![PROTON DRIVE](assets/notext/13.webp) Klicka på det här alternativet och tilldela mappen ett namn. ![PROTON DRIVE](assets/notext/14.webp) Då hittar du den direkt på startsidan för Proton Drive. ![PROTON DRIVE](assets/notext/15.webp) Slutligen kan du med "*Nytt dokument*" skapa ett nytt textdokument direkt i Proton Drive. ![PROTON DRIVE](assets/notext/16.webp) Genom att klicka på den öppnas ett nytt tomt dokument. ![PROTON DRIVE](assets/notext/17.webp) Du kan skriva i det och redigera det. ![PROTON DRIVE](assets/notext/18.webp) Om du klickar på knappen "*Share*" längst upp till höger kan du dela dokumentet. ![PROTON DRIVE](assets/notext/19.webp) Du behöver bara ange e-postadressen till den bidragsgivare som du vill ge tillgång till dokumentet, antingen i skrivskyddat läge eller med redigeringsrättigheter. ![PROTON DRIVE](assets/notext/20.webp) Om du går tillbaka till din Proton Drive kan du se att dokumentet har sparats framgångsrikt. ![PROTON DRIVE](assets/notext/21.webp) Under fliken "*Shared*" hittar du de dokument som du har delat med andra. ![PROTON DRIVE](assets/notext/22.webp) Och på fliken "*Shared with me*" kan du se de dokument som andra har delat med dig. ![PROTON DRIVE](assets/notext/23.webp) Slutligen, på fliken "*Trash*" kan du hitta dina nyligen raderade dokument. ![PROTON DRIVE](assets/notext/24.webp) De flesta inställningar för din Proton Drive är integrerade i ditt Proton-konto. För detaljerade instruktioner om hur du konfigurerar ditt konto uppmanar jag dig att läsa denna handledning:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Hur installerar jag Proton Drive-programvaran?

Proton Drive erbjuder också programvara som gör det möjligt att synkronisera dina lokala filer med ditt lagringsutrymme online. Denna funktion underlättar och automatiserar implementeringen av vår 3-2-1 backup-strategi. Med Proton Drive-programvaran får du två synkroniserade kopior av dina filer: en på din dator och den andra på Protons servrar, vilket uppfyller kriterierna för två medietyper och säkerhetskopiering utanför webbplatsen. Du behöver helt enkelt skapa en tredje kopia, som vi kommer att ställa in senare.

För att använda programvaran klickar du på fliken "*Datorer*" på ditt Proton Drive-konto och väljer den knapp som motsvarar ditt operativsystem för att fortsätta med nedladdningen.

![PROTON DRIVE](assets/notext/25.webp)

När du har installerat måste du logga in för att låsa upp ditt konto och sedan klicka på "*Sign in*".

![PROTON DRIVE](assets/notext/26.webp)

Välj de lokala filer som du vill synkronisera med din Proton Drive.

![PROTON DRIVE](assets/notext/27.webp)

Jag har t.ex. bara valt mappen "*Proton Backup*". Klicka sedan på knappen "*Continue*".

![PROTON DRIVE](assets/notext/28.webp)

Du kommer då till programvaran Interface, som liknar webbapplikationen.

![PROTON DRIVE](assets/notext/29.webp)

Från och med nu kommer du att ha en mapp med namnet "*Proton Drive*" lokalt på din dator, där alla dina dokument som lagras på Proton online samlas. Om du lägger till en fil i den här mappen från din dator kommer du automatiskt att hitta den på startsidan för webbapplikationen Proton Drive, och vice versa. För de mappar som du valde att synkronisera under programinstallationen kan du också hitta dem online genom att gå till avsnittet "*Datorer*" i Proton Drive och sedan välja din dator.

![PROTON DRIVE](assets/notext/30.webp)

Alla dina filer säkerhetskopieras och synkroniseras alltså både lokalt på din dator och på Proton Drives onlineservrar.


## Hur gör jag en säkerhetskopia av Proton Drive?


Om du har följt de föregående stegen har du nu två olika platser för säkerhetskopiering av dina viktiga filer. För att slutföra vår 3-2-1 backup-strategi måste vi lägga till en tredje kopia.

Jag föreslår att du utför denna extra säkerhetskopiering på ett externt medium, t.ex. en extern Hard-enhet eller ett USB-minne. Beroende på hur intensiv din användning är ställer du in en lämplig uppdateringsfrekvens för säkerhetskopieringen (veckovis, månadsvis, halvårsvis ...). Vid varje valt intervall måste du ladda ner hela din Proton Drive för att säkerhetskopiera data på det valda externa mediet. På så sätt kommer du, även om din dator skulle bli stulen och Protons servrar samtidigt förstöras, att ha säker tillgång till dina filer tack vare kopian på USB-minnet.


För att göra detta, gå till din Proton Drive.

![PROTON DRIVE](assets/notext/31.webp)

Välj alla dina filer.

![PROTON DRIVE](assets/notext/32.webp)

Klicka sedan på den lilla pilen för att ladda ner dem.

![PROTON DRIVE](assets/notext/33.webp)

Vi kommer sedan att upprepa operationen med våra filer synkroniserade från vår dator.

![PROTON DRIVE](assets/notext/34.webp)

Du kommer då att hitta .zip-filer i dina nedladdningar. Anslut bara det externa medium du väljer till din dator och överför sedan dessa filer till det.

![PROTON DRIVE](assets/notext/35.webp)

Om du är orolig för att detta USB-minne kan bli stulet kan du överväga att kryptera det med programvara som VeraCrypt (vi kommer snart att göra en handledning om denna programvara).


Grattis, du har nu en mycket robust 3-2-1 backup-strategi som gör att du drastiskt kan minska risken för att förlora tillgången till dina personliga dokument, oavsett omständigheterna. Genom att välja Proton Drive för dina onlinebackuper drar du också nytta av end-to-end-kryptering, vilket garanterar skyddet av din integritet.


Om du vill veta mer om hur du säkrar din närvaro på nätet och undviker hackning rekommenderar jag också att du läser vår detaljerade handledning om lösenordshanteraren Bitwarden:


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9