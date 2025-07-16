---
name: RoninDojo v2
description: Installera din RoninDojo v2 Bitcoin-nod på en Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)


***VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är vissa funktioner i RoninDojo, såsom Whirlpool, inte längre i drift. Det är dock möjligt att dessa verktyg kan återinföras eller återlanseras på olika sätt under de kommande veckorna. Eftersom RoninDojo-koden fanns på Samourais GitLab, som också beslagtogs, är det för närvarande inte möjligt att ladda ner koden på distans. RoninDojo-teamen arbetar sannolikt med att publicera koden på nytt.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> Använd Bitcoin med sekretess.

I en tidigare handledning hade vi redan förklarat proceduren för installation och användning av RoninDojo v1. Under det senaste året har RoninDojo-teamen dock lanserat version 2 av sin implementering, vilket markerade en betydande vändpunkt i programvarans arkitektur. Faktum är att de flyttade bort från Linux Manjaro-distributionen till förmån för Debian. Följaktligen erbjuder de inte längre en förkonfigurerad bild för automatisk installation på Raspberry Pi. Men det finns fortfarande en metod för att fortsätta med en manuell installation. Detta är vad jag använde för min egen nod, och sedan dess har RoninDojo v2 fungerat underbart på min Raspberry Pi 4. Jag erbjuder därför en ny handledning om hur man manuellt installerar RoninDojo v2 på en Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## Innehållsförteckning:


- Vad är RoninDojo?
- Vilken hårdvara ska jag välja för att installera RoninDojo v2?
- Hur monterar man Raspberry Pi 4?
- Hur installerar man RoninDojo v2 på en Raspberry Pi 4?
- Hur använder man sin RoninDojo v2-nod?


## Vad är RoninDojo?

Dojo är ursprungligen en fullständig Bitcoin-nodimplementering, baserad på Bitcoin Core, och utvecklad av Samourais Wallet-team. Den här lösningen kan installeras på vilken utrustning som helst. Till skillnad från andra Core-implementeringar har Dojo optimerats specifikt för att integreras med Android-applikationsmiljön i Samourai Wallet. RoninDojo är ett verktyg som är utformat för att underlätta installation och hantering av en Dojo, liksom olika andra kompletterande verktyg. Kort sagt, RoninDojo berikar den grundläggande implementeringen av Dojo genom att integrera en mängd ytterligare verktyg, samtidigt som installationen och hanteringen förenklas.


Ronin erbjuder också [en node-in-box-lösning, kallad "*Tanto*"](https://ronindojo.io/en/products), en enhet med RoninDojo redan installerad på ett system som monterats av deras team. Tanto är ett betalt alternativ, vilket kan vara intressant för dem som föredrar att undvika tekniska komplikationer. Men eftersom källkoden för RoninDojo är öppen är det också möjligt att distribuera den på din egen hårdvara. Detta alternativ, mer ekonomiskt, kräver dock några ytterligare manipuleringar, som vi kommer att täcka i denna handledning.

RoninDojo är en Dojo, vilket gör det möjligt att enkelt integrera Whirlpool CLI i din Bitcoin-nod för att ge bästa möjliga CoinJoin-upplevelse. Med Whirlpool CLI blir det möjligt att kontinuerligt remixa dina bitcoins, 24 timmar om dygnet, 7 dagar i veckan, utan att din persondator behöver vara påslagen.


Utöver Whirlpool CLI innehåller RoninDojo en mängd olika verktyg för att förbättra din Dojos funktioner. Bland dessa analyserar Boltzmann-kalkylatorn sekretessnivån för dina transaktioner, Electrum-servern gör det möjligt att ansluta dina Bitcoin-plånböcker till din nod och Mempool-servern gör att du kan se dina transaktioner lokalt utan att läcka information.


Jämfört med andra nodlösningar som Umbrel är RoninDojo tydligt inriktad på On-Chain-lösningar och integritetsverktyg. Till skillnad från Umbrel stöder RoninDojo inte konfigurering av en Lightning-nod eller integrering av mer generalistiska serverapplikationer. Även om RoninDojo erbjuder färre mångsidiga verktyg än Umbrel, har den alla väsentliga funktioner för att hantera din On-Chain-aktivitet.


Om du inte behöver generalistiska funktioner eller funktioner relaterade till Lightning Network som Umbrel erbjuder, och du letar efter en enkel, stabil nod med viktiga verktyg som Whirlpool eller Mempool, kan RoninDojo vara den perfekta lösningen. Medan Umbrel tenderar att bli en mini multitasking-server inriktad på Lightning Network och mångsidighet, fokuserar RoninDojo, i linje med filosofin i Samourai Wallet, på grundläggande verktyg för användarnas integritet.


Nu när vi har beskrivit RoninDojo, låt oss tillsammans se hur man ställer in den här noden.


## Vilken hårdvara ska man välja för att installera RoninDojo v2?

RoninDojo erbjuder en bild för automatisk installation av sin programvara på en [RockPro64] (https://ronindojo.io/en/download). Vår handledning fokuserar dock på den manuella installationsproceduren på en Raspberry Pi 4. Även om Raspberry Pi 5 nyligen har lanserats, och denna handledning teoretiskt sett borde vara kompatibel med den nya modellen, har jag ännu inte haft möjlighet att testa den personligen, och jag har inte hittat någon feedback från communityn. Så snart jag får tag på Pi 5 och kompatibla komponenter kommer jag att uppdatera den här handledningen för att hålla dig informerad. Under tiden rekommenderar jag att du prioriterar Pi 4, eftersom den fungerar perfekt för min nod.

För egen del kör jag RoninDojo på en Raspberry Pi med 8 GB RAM-minne. Även om vissa communitymedlemmar har lyckats få det att fungera på enheter med endast 4 GB RAM, har jag inte testat den här konfigurationen själv. Med tanke på den lilla prisskillnaden verkar det klokt att välja 8 GB RAM-versionen. Detta kan också visa sig vara användbart om du planerar att återanvända din Raspberry Pi för andra användningsområden i framtiden.

Det är viktigt att notera att RoninDojo-teamen har rapporterat frekventa problem relaterade till fodralet och SSD-adaptern. Jag har själv ställts inför dessa problem. **Därför rekommenderas det starkt att undvika fodral som är utrustade med en USB-kabel för din nods SSD.** Föredra istället ett lagringsexpansionskort som är speciellt utformat för din Raspberry Pi:


![storage expansion card RPI4](assets/notext/1.webp)


För att lagra Bitcoin Blockchain behöver du en SSD som är kompatibel med det lagringsexpansionskort du har valt. För närvarande (februari 2024) befinner vi oss i en övergångsfas. Det förväntas att 1 TB-diskar om några månader inte längre kommer att vara tillräckliga för att lagra den växande storleken på Blockchain, särskilt med tanke på de olika applikationer som du planerar att integrera i din nod. Vissa rekommenderar därför att man investerar i en 2 TB SSD för att få sinnesro på lång sikt. Men med den nedåtgående trenden i SSD-priser år efter år föreslår andra att man nöjer sig med en 1 TB-disk, som bör räcka i ett eller två år, och hävdar att kostnaden för 2 TB-modeller förmodligen kommer att ha minskat när den blir föråldrad. Valet beror alltså på dina personliga preferenser. Om du planerar att behålla din RoninDojo under en längre tid och vill undvika tekniska problem under de kommande åren, verkar en 2 TB SSD vara det klokaste alternativet, eftersom det ger dig en bekväm marginal för framtiden.


Dessutom behöver du olika små komponenter:


- Ett hölje med fläkt som rymmer Raspberry Pi och expansionskortet för lagringsutrymme. Kit som innehåller både SSD-expansionskortet och ett kompatibelt hölje finns tillgängliga online;
- En strömkabel för din Raspberry Pi;
- Ett micro SD-kort på minst 16 GB (även om 8 GB tekniskt sett skulle kunna räcka, är prisskillnaden mellan 8 och 16 GB-kort ofta försumbar);
- En RJ45 Ethernet-kabel för nätverksanslutning.


![node material](assets/notext/2.webp)


## Hur monterar man Raspberry Pi 4?

Monteringen av din nod kommer att variera beroende på vald hårdvara, särskilt typen av hölje. Den allmänna beskrivningen av de steg som ska följas förblir dock i stort sett densamma vid monteringen.

Börja med att installera din SSD på lagringsexpansionskortet och se till att de två låsskruvarna på baksidan sitter fast.


![assembly1](assets/notext/3.webp)


Anslut sedan din Raspberry Pi till expansionskortet.


![assembly2](assets/notext/4.webp)


Anslut också fläkten till Raspberry Pi.


![assembly3](assets/notext/5.webp)


Anslut de olika komponenterna och var noga med att använda rätt stift, se manualen för din låda. Chassitillverkare erbjuder ofta videohandledning för att hjälpa dig med monteringen. I mitt fall har jag ett extra expansionskort som är utrustat med en på/av-knapp. Detta är inte nödvändigt för att skapa en Bitcoin-nod. Jag använder det främst för att ha en strömbrytare.


Om du, som jag, har ett expansionskort som är utrustat med en av/på-knapp, glöm inte att installera den lilla bygeln "Auto Power On". Detta gör att din nod startar automatiskt så snart den slås på. Den här funktionen är särskilt användbar vid strömavbrott, eftersom den gör att noden startar om av sig själv utan manuell åtgärd från din sida.


![assembly4](assets/notext/6.webp)


Innan du sätter in all maskinvara i höljet är det viktigt att kontrollera att din Raspberry Pi, lagringsexpansionskortet och fläkten fungerar som de ska genom att slå på dem.


![assembly5](assets/notext/7.webp)


Installera slutligen din Raspberry Pi i dess hölje. Tänk på att du i ett senare steg kommer att behöva sätta i micro SD-kortet i lämplig port på Raspberry Pi. Om ditt fodral är utrustat med en öppning som gör att du kan sätta i SD-kortet utan att behöva öppna det (som är fallet med mitt som illustreras på bilden), kan du fortsätta att stänga fodralet nu. Men om ditt hölje inte har direkt tillgång till micro SD-porten måste du vänta tills du har förberett micro SD-kortet för att sätta in det innan du slutför monteringen.


![assembly6](assets/notext/8.webp)


## Hur installerar man RoninDojo v2 på en Raspberry Pi 4?


### Steg 1: Förbered den startbara micro SD-enheten

När du har monterat din hårdvara är nästa steg att installera RoninDojo. För detta kommer vi att förbereda ett startbart micro SD-kort från din dator genom att bränna lämplig diskavbildning på den.

Du behöver använda programvaran _**Raspberry Pi Imager**_, som är utformad för att underlätta nedladdning, konfigurering och skrivning av operativsystem på ett micro SD-kort för användning med en Raspberry Pi. Börja med att installera den här programvaran på din PC:


- För Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- För Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- För Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg


När programvaran har installerats öppnar du den och sätter i ditt micro SD-kort i din dator. Från Raspberry Pi Imager Interface, välj "VÄLJ OS":


![choose OS](assets/notext/9.webp)


Gå sedan till menyn `Raspberry Pi OS (other)`:


![choose OS others](assets/notext/10.webp)


Välj operativsystemet med namnet `Raspberry Pi OS (Legacy, 64-bit) Lite`, som är `0,3 GB` stort:


![choose OS Legacy Lite](assets/notext/11.webp)


När du har valt operativsystem kommer du att omdirigeras till huvudmenyn i Raspberry Pi Imager. Klicka på `CHOOSE STORAGE`:


![choose storage](assets/notext/12.webp)


Välj ditt micro SD-kort:


![choose micro sd](assets/notext/13.webp)


När du har valt operativsystem och micro SD-kort klickar du på `NEXT`:


![choose next](assets/notext/14.webp)


Ett nytt fönster visas. Välj `EDIT CONFIGURATION`:


![edit settings](assets/notext/15.webp)


I detta fönster går du till fliken `GENERAL` och gör följande inställningar (som är mycket viktiga för att det ska fungera):


- Aktivera alternativet och tilldela `RoninDojo` som värdnamn;
- Aktivera `Set username and password`, ange `pi` som användarnamn, välj ett lösenord och anteckna denna information, eftersom den kommer att behövas senare. Dessa uppgifter är tillfälliga och kommer att raderas efteråt;
- Avaktivera `Konfigurera Wi-Fi`;
- Aktivera `Set locale settings` och välj din tidszon samt den tangentbordstyp som motsvarar din dator;


![general settings](assets/notext/16.webp)


På fliken SERVICES klickar du på rutan `Enable SSH` och väljer `Use a password for authentication`:


![services settings](assets/notext/17.webp)


Se också till att telemetri är inaktiverat på fliken "OPTIONS":


![options settings](assets/notext/18.webp)


Klicka på `SAVE`:


![settings save](assets/notext/19.webp)

Bekräfta genom att klicka på `YES` för att börja skapa det startbara micro SD-kortet:

![settings yes](assets/notext/20.webp)


Du kommer att få ett meddelande om att alla data på micro SD-kortet kommer att raderas. Bekräfta genom att klicka på `YES` för att starta processen:


![overwrite micro SD](assets/notext/21.webp)


Vänta tills programmet har förberett ditt micro SD-kort:


![writing micro SD](assets/notext/22.webp)


När meddelandet om att processen är avslutad visas kan du ta ut micro SD-kortet ur datorn:


![writing micro SD completed](assets/notext/23.webp)


### Steg 2: Slutför montering av noden

Du kan nu sätta in micro SD-kortet i lämplig port på din Raspberry Pi.


![micro SD](assets/notext/24.webp)


Anslut sedan din Raspberry Pi till din router med Ethernet-kabeln. Slutligen slår du på noden genom att ansluta strömkabeln och trycka på strömknappen (om det finns en sådan i din installation).


### Steg 3: Upprätta en SSH-anslutning med noden

Först måste du ta reda på IP Address för din nod. Du har möjlighet att använda ett verktyg som _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ eller _[Angry IP Scanner](https://angryip.org/)_, eller kontrollera administrationen Interface för din router. IP Address bör vara i formen `192.168.1.??`. **För alla följande kommandon ska du ersätta `[IP]` med den faktiska IP Address för din nod**, (ta bort parenteserna).


Starta en terminal.


För att ta bort en möjlig nyckel som redan är associerad med IP Address för din nod, kör kommandot:

`ssh-keygen -R [IP]`.


Ett fel efter detta kommando är inte allvarligt; det betyder helt enkelt att nyckeln inte finns i din lista över kända värdar (vilket är ganska troligt). Om till exempel nodens IP-adress är `192.168.1.40`, blir kommandot: `ssh-keygen -R 192.168.1.40`.


Därefter upprättar du en SSH-anslutning till din nod genom att utföra kommandot:

`ssh pi@[IP]`.

Ett meddelande visas om värdens äkthet: `Äktheten för värden '[IP]' kan inte fastställas.` Detta indikerar att äktheten för den enhet du försöker ansluta till inte kan verifieras eftersom det saknas en känd publik nyckel. När du ansluter via SSH till en ny värd för första gången visas alltid det här meddelandet. Du måste svara `yes` för att lägga till den publika nyckeln i din lokala katalog, vilket förhindrar att detta varningsmeddelande visas vid framtida SSH-anslutningar till den här noden. Skriv därför `yes` och tryck på `enter` för att bekräfta.

Du kommer då att bli ombedd att ange ditt lösenord, det som du tidigare angav som tillfälligt i steg 1. Validera med `enter`. Du kommer då att vara ansluten till din nod via SSH.


Här följer en sammanfattning av de kommandon som ska utföras:


- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- "Ja
- Ange det tillfälliga lösenordet och bekräfta.


### Steg 4: Uppdatering och förberedelser

Du är nu ansluten till din nod via en SSH-session. På din terminal bör kommandotolken vara: `pi@RoninDojo:~ $`. Till att börja med uppdaterar du listan över tillgängliga paket och installerar uppdateringar för befintliga paket med följande kommando:

`sudo apt update && sudo apt upgrade -y`


När uppdateringarna är klara fortsätter du att installera *Git* och *Dialog* med hjälp av kommandot:

`sudo apt installera git dialog -y`


Klona sedan `master'-grenen i _RoninOS_ Git-förvaret genom att köra:

`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`


Kör skriptet `customize-image.sh` med kommandot:

`cd /opt/RoninOS/ && sudo ./customize-image.sh`


**Det är viktigt att låta skriptet köras utan avbrott och att tålmodigt invänta slutet av processen**, som tar ca 10 minuter. När meddelandet `Setup is complete` visas kan du gå vidare till nästa steg.


### Steg 5: Starta RoninOS

Starta RoninOS med kommandot:

`sudo systemctl start ronin-setup`


Visa raderna i loggfilen med kommandot:

`tail -f /home/ronindojo/.logs/setup.logs`


I det här skedet är det viktigt att låta RoninOS starta och vänta på att den** ska köra klart. Detta tar ungefär 40 minuter. När `All RoninDojo feature installations complete!` visas kan du gå vidare till steg 6.


### Steg 6: Gå till RoninUI och ändra autentiseringsuppgifter

När du har slutfört installationen och vill ansluta till noden via en webbläsare måste du se till att din dator är ansluten till samma lokala nätverk som noden. Om du använder ett VPN på din dator ska du tillfälligt inaktivera det. För att komma åt noden Interface i din webbläsare, skriv in i URL-fältet:


- Direkt IP Address för din nod, till exempel `192.168.1.??`;
- Eller skriv `ronindojo.local`.


När du är på RoninUI:s hemsida kommer du att uppmanas att starta installationen. För att göra detta klickar du på knappen "Låt oss börja".


![lets start](assets/notext/25.webp)


I detta skede presenterar RoninUI ditt `root`-lösenord för dig. Det är viktigt att hålla det säkert. Du kan välja en fysisk säkerhetskopia, på papper, eller spara det i en [lösenordshanterare] (https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-1562bd55930f).


![root password](assets/notext/26.webp)


När du har sparat lösenordet för root markerar du rutan "I have backed up Root user credentials" och klickar på "Continue" för att fortsätta.


![confirm root password](assets/notext/27.webp)


Nästa steg är att skapa ett användarlösenord som kommer att användas både för att komma åt RoninUI-webben Interface och för att upprätta SSH-sessioner med din nod. Välj ett starkt lösenord och se till att spara det på ett säkert sätt. Du måste ange lösenordet två gånger innan du klickar på `Finish` för att validera. När det gäller användarnamnet rekommenderar vi att du behåller standardvalet, `ronindojo`. Om du bestämmer dig för att ändra det, kom ihåg att justera kommandona i följande steg i enlighet med detta.


![user credentials](assets/notext/28.webp)


När dessa åtgärder är slutförda väntar du på att noden ska initieras. Du kommer då att komma åt RoninUI-webben Interface. Du är nästan i slutet av processen, bara några små steg kvar!

![Ronin UI](assets/notext/29.webp)


### Steg 7: Ta bort tillfälliga autentiseringsuppgifter

Öppna en ny terminal på din dator och upprätta en SSH-anslutning till din nod med följande kommando:

`SSH ronindojo@[IP]`


Om till exempel IP Address för din nod är `192.168.1.40`, kommer det lämpliga kommandot att vara:

`SSH ronindojo@192.168.1.40`


Om du ändrade ditt användarnamn under föregående steg och ersatte standardanvändarnamnet (`ronindojo`) med ett annat, se till att använda det nya namnet i kommandot. Om du t.ex. valde `planb` som användarnamn och IP Address är `192.168.1.40`, blir kommandot som ska anges följande:

`SSH planb@192.168.1.40`

Du kommer att bli ombedd att ange användarlösenordet. Ange det och tryck sedan på `enter` för att validera. Du kommer då att få tillgång till RoninCLI Interface. Använd piltangenterna på tangentbordet för att navigera till alternativet `Exit RoninDojo` och tryck på `enter` för att välja det.

![RoninCLI](assets/notext/30.webp)


Nu befinner du dig på din nods terminal med en kommandotolk som liknar: `ronindojo@RoninDojo:~ $`. För att ta bort den tillfälliga användaren som skapades under konfigurationen av det startbara micro SD-kortet, ange följande kommando och tryck på `enter`:

`sudo deluser --remove-home pi`


Du kommer att uppmanas att bekräfta ditt användarlösenord. Ange det och bekräfta genom att trycka på `enter`. Vänta tills åtgärden är klar och använd sedan kommandot `exit` för att lämna terminalen.


Gratulerar till den här tjänsten! Din RoninDojo v2-nod är nu konfigurerad och redo att användas. Den kommer att påbörja sin IBD (*Initial Block Download*), fortsätta att ladda ner och verifiera Bitcoin Blockchain från Genesis-blocket. Detta steg innebär att hämta alla Bitcoin-transaktioner som gjorts sedan den 3 januari 2009 och tar lite tid. När Blockchain är helt nedladdad kommer indexeraren att fortsätta att komprimera databasen. IBD:s varaktighet kan variera avsevärt. Din RoninDojo-nod kommer att vara i full drift när denna process är klar.


** Om du migrerar från en gammal RoninDojo v1-nod** till den här nya versionen med den här handledningen och behåller samma SSD, bör din nod automatiskt upptäcka och återanvända befintliga data på disken, vilket gör att du inte behöver utföra IBD igen. I det här fallet behöver du bara vänta på att din nod ska synkronisera med de senaste blocken.


### Steg 8: "veth* fix"

Om du stöter på en bugg med din RoninDojo v2 på Raspberry Pi, där din nod efter en problemfri installation plötsligt blir oåtkomlig via SSH men återhämtar sig efter en enkel omstart, måste du följa detta steg 8. Det här vanliga felet kan enkelt åtgärdas med en lösning som utvecklats av communityn: "_veth fix_". Denna mindre korrigering avhjälper permanent de plötsliga frånkopplingarna. Så här gör du för att tillämpa den.


Öppna en ny terminal på din dator och upprätta en SSH-anslutning till din nod med följande kommando:

`SSH ronindojo@[IP]`


Om till exempel nodens IP Address är `192.168.1.40`, är det lämpliga kommandot följande:

`SSH ronindojo@192.168.1.40`


Du kommer att uppmanas att ange användarens lösenord. Ange det och tryck på `enter` för att validera. Du kommer då att få tillgång till RoninCLI Interface. Använd tangentbordets pilar för att navigera till alternativet `Exit RoninDojo` och tryck på `enter` för att välja det.


Nu befinner du dig på din nods terminal med en kommandotolk som liknar: `ronindojo@RoninDojo:~ $`. För att tillämpa veth*-fixen skriver du följande kommando och trycker på `enter`:

`sudo nano /etc/dhcpcd.conf`


Bekräfta lösenordet igen och tryck på `enter`.


Du kommer då till filen `dhcpcd.conf`. Du måste kopiera följande text, se till att få med asterisken, och lägga till den längst ner i filen:

"förneka gränssnitt veth


Det gör du genom att flytta dig längst ner i filen med nedåtpilen på tangentbordet och sedan använda högerklicket på musen för att klistra in texten på en egen rad.


När du har lagt till texten trycker du på `ctrl X` för att börja avsluta, följt av `ctrl Y` för att bekräfta att ändringarna sparats och tryck på `enter` för att avsluta och återgå till kommandotolken. För att säkerställa att ändringen har tillämpats korrekt öppnar du filen `dhcpcd.conf` igen med hjälp av lämpligt kommando.


För att slutföra tillämpningen av korrigeringen, starta om din nod genom att köra:

`sudo starta om nu`


Nu kan du stänga din terminal. Låt RoninDojo starta om under den tid som krävs, varefter du bör kunna återansluta via webbläsarens grafiska Interface. Denna process bör åtgärda den uppkomna buggen.


## Hur använder man sin RoninDojo v2-nod?


### Ansluta din Wallet-programvara till Electrs

Den första användningen av din nyinstallerade och synkroniserade nod kommer att vara att sända dina transaktioner till Bitcoin-nätverket. Du kommer förmodligen att vilja ansluta dina olika plånböcker till din nod för att kunna sända dina transaktioner konfidentiellt. Du kan göra detta genom Electrum Rust Server (electrs). Denna applikation är vanligtvis förinstallerad på din RoninDojo-nod. Om inte, kan du installera den manuellt via RoninCLI Interface i `Applikationer > Hantera applikationer > Installera Electrum Server`.


För att hämta Tor Address för din Electrum Server, från RoninUI-webben Interface, gå till:

`Pairing > Electrum server > Pair now`

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

Du måste sedan ange `Hostname` Address som slutar på `.onion` i din Wallet-programvara, tillsammans med port `50001`. ![värdnamn](tillgångar/notext/33.webp)

Till exempel på Sparrow wallet, gå helt enkelt till fliken:

`Fil > Inställningar > Server > Private Electrum`


![Sparrow](assets/notext/34.webp)


### Ansluta din Wallet-programvara till Samourai Dojo

Som ett alternativ till att använda Electrs kan du med Dojo ansluta din kompatibla Software Wallet direkt till din RoninDojo-nod. Plånböcker som Samourai Wallet och Sentinel erbjuder denna funktionalitet.


För att upprätta anslutningen behöver du bara skanna QR-koden för din Dojo. För att komma åt denna QR-kod via RoninUI, navigera till:

"Para ihop > Samourai Dojo > Para ihop nu

![Samourai Dojo](assets/notext/35.webp)

För att koppla din Samourai Wallet till din Dojo skannar du helt enkelt den här QR-koden under installationen av appen:


![Samourai Wallet connection](assets/notext/36.webp)


Om du redan hade en Samourai Wallet innan du satte upp din Ronin Dojo, är det nödvändigt att säkerhetskopiera din Wallet, avinstallera och sedan installera om Samourai Wallet-appen innan du återställer din Wallet. När du startar den ominstallerade appen kommer du att ha möjlighet att ansluta till en ny Dojo. **Se till att du har säkerhetskopian av din Samourai Wallet i dina filer och verifiera giltigheten för din passphrase via `Inställningar > Felsökning > passphrase`. Det är också viktigt att ha en läsbar säkerhetskopia av din återställningsfras och din passphrase. För mer precision i denna operation rekommenderas att du följer denna detaljerade handledning: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).


### Använda din egen Mempool.space Block explorer

En Block explorer omvandlar råinformationen från Bitcoin Blockchain till ett strukturerat och lättläst format. Med verktyg som *Mempool.space* är det möjligt att analysera transaktioner, söka efter specifika adresser eller till och med konsultera de genomsnittliga avgiftsnivåerna för nätverkets mempooler i realtid.


Att använda blockutforskare online innebär dock risker för din integritet och innebär förtroende för de uppgifter som tillhandahålls av tredje part. Genom att använda dessa tjänster utan att gå igenom din egen nod kan du faktiskt oavsiktligt avslöja information om dina transaktioner och måste förlita dig på riktigheten i den information som presenteras av webbplatsägaren.

För att minska dessa risker rekommenderas att du använder din egen instans av *Mempool.space* via Tor-nätverket, direkt på din nod. Denna lösning säkerställer att din integritet bevaras och att dina data är autonoma.

För att göra detta, börja med att installera *Mempool Space Visualizer* från RoninUI. På webben Interface, gå till fliken `Dashboard` och klicka på `Manage` under `Mempool Space`:

`Dashboard > Mempool Space > Hantera`

![Manage mempool](assets/notext/37.webp)

Klicka sedan på knappen `Install Mempool visualizer`:

![install mempool](assets/notext/38.webp)

Bekräfta ditt användarlösenord:

![password mempool](assets/notext/39.webp)

Vänta tills installationen är klar och klicka sedan igen på knappen "Hantera":

![Mempool Manage](assets/notext/40.webp)

Du kommer att få en `.onion`-länk för att komma åt din egen instans av *Mempool.space* via Tor-nätverket.

![Mempool link](assets/notext/41.webp)

Jag råder dig att spara den här länken i dina favoriter i Tor-webbläsaren eller lägga till den i Tor Browser-appen på din smartphone för enkel och säker åtkomst från var som helst. Om du ännu inte har Tor-webbläsaren kan du ladda ner den här: [https://www.torproject.org/download/](https://www.torproject.org/download/)

![Mempool Tor](assets/notext/42.webp)


### Använd Whirlpool för att blanda dina bitcoins

Din RoninDojo-nod integrerar också _WhirlpoolCLI_, en kommandorads-Interface som möjliggör automatisering av Whirlpool coinjoins, och _WhirlpoolGUI_, en grafisk Interface som är utformad för att interagera med _WhirlpoolCLI_.


För att utföra en CoinJoin via Whirlpool krävs att den applikation som används är aktiv för att utföra remixer. Detta villkor kan vara begränsande för dem som vill uppnå höga nivåer av anonsets. Den enhet som är värd för applikationen som integrerar Whirlpool måste vara påslagen kontinuerligt. Detta innebär att för att delta i remixer 24 timmar om dygnet måste din dator eller smartphone vara påslagen med Samourai eller Sparrow öppen kontinuerligt. En lösning på denna begränsning är att använda _WhirlpoolCLI_ på en maskin som alltid är på, till exempel en Bitcoin-nod, så att dina mynt kan remixas utan avbrott och utan att behöva hålla en annan enhet påslagen.


En detaljerad handledning är under utarbetande för att vägleda dig steg för steg genom processen att sammanfoga Samourai Wallet och RoninDojo v2, från A till Ö.


För en djupare förståelse av CoinJoin och dess användning på Bitcoin, uppmanar jag dig också att läsa den här andra artikeln: Förstå och använda CoinJoin på Bitcoin, där jag beskriver allt du behöver veta om den här tekniken.


https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

### Använda Whirlpool Stat Tool (WST)


Efter att ha utfört coinjoins med Whirlpool är det användbart att exakt utvärdera den sekretessnivå som uppnåtts för dina blandade UTXO. För att göra detta kan du använda Python-verktyget *Whirlpool Stat Tool*. Med det här verktyget kan du mäta både de prospektiva och retrospektiva poängen för dina UTXO:er, samtidigt som du analyserar deras spridningshastighet i poolen.


För att fördjupa din förståelse för beräkningsmekanismerna för dessa anonsets rekommenderar jag att du läser artikeln: REMIX - Whirlpool, som beskriver hur dessa index fungerar.


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



För att komma åt WST-verktyget, gå till RoninCLI. För att göra detta öppnar du en terminal på din dator och upprättar en SSH-anslutning till din nod med hjälp av följande kommando:

`SSH ronindojo@[IP]`


Om till exempel nodens IP Address är `192.168.1.40`, är det lämpliga kommandot följande:

`SSH ronindojo@192.168.1.40`


Om du ändrade ditt användarnamn i steg 6 och ersatte standardanvändarnamnet (`ronindojo`) med ett annat, ska du se till att använda det nya namnet i kommandot. Om du t.ex. valde `planb` som användarnamn och IP Address är `192.168.1.40`, skulle kommandot vara följande

`SSH planb@192.168.1.40`


Du kommer att bli ombedd att ange användarlösenordet. Ange det och tryck på `enter` för att validera. Du kommer då att få tillgång till RoninCLI Interface. Använd piltangenterna på tangentbordet för att navigera till menyn `Samourai Toolkit` och tryck på `enter` för att välja den:


![Samourai Toolkit](assets/notext/43.webp)


Välj sedan `Whirlpool Stat Tool`:


![WST](assets/notext/44.webp)


Efter initiering av WST kommer verktyget att fortsätta med sin automatiska installation. Vänta under detta steg. Användarinstruktionerna kommer att rulla igenom. När installationen är klar, tryck på valfri tangent för att komma till WST-terminalen:


![WST commands](assets/notext/45.webp)


Följande kommandotolk kommer att visas:

`wst#/tmp>`


Om du vill lämna denna Interface och återgå till RoninCLI-menyn, tryck bara Enter:

"Avsluta


Först är det nödvändigt att konfigurera proxyn för att använda Tor, för att säkerställa integritet när du extraherar data från OXT. Ange kommandot:

`socks5 127.0.0.1:9050`


Fortsätt sedan med att ladda ner poolinformationen som innehåller din transaktion:

"Ladda ner 0001

Ersätt `0001` med valörkoden för den pool som du är intresserad av. Valörkoderna är som följer på WST:


- Pool 0,5 bitcoins: `05`
- Pool 0,05 bitcoins: `005``
- Pool 0,01 bitcoins: `001`
- Pool 0,001 bitcoins: `0001`


Efter nedladdningen laddar du data genom att ersätta `0001` med din pools kod i det här kommandot: `ladda 0001`


![WST loading](assets/notext/46.webp)


Vänta tills inläsningen är klar, vilket kan ta några minuter. När uppgifterna har laddats, för att få veta anonset-poängen för ditt mynt, kör kommandot `score` följt av din txid (utan parenteserna):

`score [txid]`


![WST score](assets/notext/47.webp)


WST kommer sedan att visa den retrospektiva poängen (_Backward-looking metrics_), följt av den prospektiva poängen (_Forward-looking metrics_). Förutom anonset-poängen kommer WST också att ange spridningshastigheten för din transaktion inom poolen, i förhållande till dess anonset.


**Det är viktigt att notera att den prospektiva poängen för ditt mynt bör beräknas från txid i din initiala mix, och inte från din senaste mix. Omvänt, den retrospektiva poängen för en UTXO beräknas från txid för den senaste cykeln.**


### Använda Boltzmanns kalkylator

Boltzmann-räknaren är ett verktyg för att analysera en Bitcoin-transaktion, och erbjuder möjligheten att mäta dess entropinivå bland andra avancerade mätvärden. Dessa data ger en kvantifierad bedömning av integriteten i en transaktion och hjälper till att identifiera potentiella brister. Det här verktyget är redan integrerat i din RoninDojo-nod, vilket gör det enkelt att komma åt och använda.


Innan vi beskriver hur Boltzmannkalkylatorn används är det viktigt att förstå innebörden av dessa indikatorer, deras beräkningsmetod och deras användbarhet. Även om de kan tillämpas på alla Bitcoin-transaktioner är dessa indikatorer särskilt användbara för att bedöma kvaliteten på en CoinJoin-transaktion.


**Den första indikatorn** som programmet beräknar är det totala antalet möjliga kombinationer, som anges under "nb combinations" i verktyget. Baserat på värdena för de berörda UTXO:erna kvantifierar denna indikator antalet sätt på vilka ingångar kan associeras med utgångar. Med andra ord bestämmer den antalet rimliga tolkningar som en transaktion kan generate ha. En CoinJoin som är strukturerad enligt Whirlpool 5x5-modellen ger till exempel `1496` möjliga kombinationer:

![combinations](assets/notext/50.webp)

Kredit: KYCP


**Den andra indikatorn** som beräknas är en transaktions entropi, som betecknas "entropi". När en transaktion har ett stort antal möjliga kombinationer är det ofta mer relevant att hänvisa till dess entropi. Denna definieras som den binära logaritmen av antalet möjliga kombinationer. Här är den formel som används:


- $E$: transaktionens entropi;
- $C$: antalet möjliga kombinationer för transaktionen.

$$E = \log_2(C)$$$


Inom matematiken motsvarar den binära logaritmen (bas 2-logaritmen) den omvända operationen av att höja 2 till en potens. Med andra ord är den binära logaritmen för $x$ den exponent som 2 måste höjas till för att erhålla $x$. Därför uttrycks denna indikator i bitar. Låt oss ta exemplet att beräkna entropin för en CoinJoin-transaktion som är strukturerad enligt Whirlpool 5x5-modellen, som, som tidigare nämnts, erbjuder ett antal möjliga kombinationer på `1496`:

$$ C = 1496 $$

$$ E = \log_2(1496) $$

$$ E \approx 10.5469 \text{ bits}$$$


Denna CoinJoin-transaktion uppvisar således en entropi på 10,5469 bitar, vilket anses vara mycket tillfredsställande. Ju högre detta värde är, desto fler olika tolkningar kan göras av transaktionen, vilket ökar dess sekretessnivå.


Låt oss ta ytterligare ett exempel med en mer konventionell transaktion, med en ingång och två utgångar: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

I fallet med denna transaktion är den enda möjliga tolkningen: `(inp 0) > (Outp 0 ; Outp 1)`. Följaktligen är dess entropi fastställd till `0`:

$$ C = 1 $$

$$ E = \log_2(1) $$

$$ E \approx 0 \text{ bitar}$$$

**Den tredje indikatorn** som tillhandahålls av Boltzmann Calculator heter "Wallet Efficiency". Denna indikator bedömer transaktionens effektivitet genom att jämföra den med den optimala transaktion som kan tänkas i en identisk uppställning. Detta leder oss till att diskutera begreppet maximal entropi, vilket motsvarar den högsta entropi som en specifik transaktionsstruktur teoretiskt kan uppnå. För en Whirlpool 5x5 CoinJoin-struktur sätts således den maximala entropin till "10,5469". Transaktionens effektivitet beräknas sedan genom att denna maximala entropi konfronteras med den faktiska entropin för den analyserade transaktionen. Formeln som används är följande:


- $ER$: transaktionens faktiska entropi, uttryckt i bitar;
- $EM$: den högsta möjliga entropin för en viss transaktionsstruktur, även den i bitar;
- $Ef$: transaktionens effektivitet, i bitar.

$$Ef = ER - EM$$$ $$Ef = 10,5469 - 10,5469$$$

$$Ef = 0 \text{ bits}$$$


Denna indikator uttrycks också som en procentsats och dess formel är då:


- $CR$: antalet faktiska möjliga kombinationer;
- $CM$: det maximala antalet möjliga kombinationer med samma struktur;
- $Ef$: effektiviteten uttryckt i procent.

$$Ef = \frac{CR}{CM}$$$

$$Ef = \frac{1496}{1496}$$$

$$Ef = 100\%$$$


En effektivitet på "100%" innebär således att transaktionen maximerar sin integritetspotential baserat på dess struktur.


**Den fjärde indikatorn**, entropidensiteten, ger ett perspektiv på entropin i förhållande till varje in- eller utdata i transaktionen. Denna indikator är användbar för att utvärdera och jämföra effektiviteten i transaktioner av olika storlek. För att beräkna den dividerar man helt enkelt transaktionens totala entropi med det totala antalet in- och utgångar som är inblandade. Vi tar exemplet med en Whirlpool 5x5 CoinJoin:


- $ED$: entropitätheten uttryckt i bitar;
- $E$: transaktionens entropi uttryckt i bitar;
- $T$: det totala antalet inmatningar och utmatningar i transaktionen.

$$T = 5 + 5 = 10$$

$$ED = \frac{E}{T}$$$

$$ED = \frac{10.5469}{10}$$$

$$ED = 1,054 \text{ bitar}$$$

**Den femte informationen** som Boltzmann Calculator levererar är en tabell över sannolikheter för matchning mellan in- och utgångar. Denna tabell anger, genom "Boltzmann-poängen", sannolikheten för att en specifik ingång är ansluten till en given utgång. Om vi tar exemplet med en Whirlpool CoinJoin, skulle sannolikhetstabellen belysa chanserna för koppling mellan varje ingång och utgång, vilket ger ett kvantitativt mått på tvetydigheten eller förutsägbarheten av associationer i transaktionen:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Här är det tydligt att varje inmatning har lika stor chans att associeras med vilken utmatning som helst, vilket förstärker transaktionens tvetydighet och integritet. När det gäller en enkel transaktion med en enda inmatning och två utmatningar är situationen dock annorlunda:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Här ser vi att sannolikheten för att varje output ska komma från input 0 är 100%. En lägre sannolikhet innebär alltså större integritet genom att de direkta kopplingarna mellan inmatning och utmatning försvagas.


**Den sjätte informationen** är antalet deterministiska länkar, kompletterat med förhållandet mellan dessa länkar. Denna indikator visar hur många kopplingar mellan inputs och outputs i den analyserade transaktionen som är odiskutabla, med 100% sannolikhet. Förhållandet ger i sin tur ett perspektiv på vikten av dessa deterministiska länkar inom transaktionens totala länkar.


En Whirlpool-typ CoinJoin-transaktion har t.ex. inga deterministiska länkar och visar därför en indikator och ett förhållande på 0 %. I vår andra undersökta transaktion (med en ingång och två utgångar) sätts å andra sidan indikatorn till 2 och förhållandet når 100 %. En nollindikator signalerar således utmärkt integritet tack vare avsaknaden av direkta och obestridliga kopplingar mellan in- och utdata.


**Hur kommer man åt Boltzmann-kalkylatorn på RoninDojo?**

För att komma åt verktyget *Boltzmann Calculator*, gå till RoninCLI. För att göra detta öppnar du en terminal på din dator och upprättar en SSH-anslutning till din nod med följande kommando: `SSH ronindojo@[IP]`


Om t.ex. nodens IP Address är `192.168.1.40`, blir det lämpliga kommandot följande:

`SSH ronindojo@192.168.1.40`


Om du ändrade ditt användarnamn i steg 6 och ersatte standardanvändarnamnet (`ronindojo`) med ett annat, ska du se till att använda det nya namnet i kommandot. Om du t.ex. valde `planb` som användarnamn och IP Address är `192.168.1.40`, skulle kommandot vara följande

`SSH planb@192.168.1.40`


Du kommer att bli ombedd att ange användarlösenordet. Ange det och tryck sedan på `enter` för att validera. Du kommer då att få tillgång till RoninCLI Interface. Använd pilarna på tangentbordet för att navigera till menyn `Samourai Toolkit` och tryck på `enter` för att välja den:


![Samourai Toolkit](assets/notext/43.webp)


Välj sedan `Boltzmann Calculator`:


![boltzmann](assets/notext/49.webp)


Du kommer då till programvarans startsida:


![boltzmann home](assets/notext/51.webp)


Ange txid för den transaktion som du vill studera och tryck på `enter`:


![boltzmann txid](assets/notext/52.webp)


Kalkylatorn ger dig sedan alla de indikatorer som vi tidigare har diskuterat:


![boltzmann result](assets/notext/53.webp)


### Andra funktioner i din RoninDojo v2

Din RoninDojo-nod integrerar olika andra funktioner. I synnerhet har du möjlighet att skanna specifik information för att ta hänsyn till den. Till exempel, ibland kanske din Samourai Wallet, ansluten till RoninDojo, inte visar de bitcoins du faktiskt har. Om balansen indikerar 0 medan du är säker på att ha bitcoins i denna Wallet, kan flera skäl förklara denna situation, till exempel ett fel i derivationsvägarna. Men en av orsakerna kan också vara att din nod inte övervakar dina adresser ordentligt. För att lösa detta problem kan du se till att din nod verkligen följer din `xpub` med hjälp av _xpub tool_. För att komma åt detta verktyg via RoninUI, följ sökvägen:

underhåll > XPUB Tool


Ange den `xpub` som orsakar problemet och klicka på `Check`-knappen för att verifiera denna information:

![xpub tool](assets/notext/54.webp)

Se till att alla transaktioner är korrekt listade. Det är också viktigt att kontrollera att den avledningstyp som används matchar den som finns i din Wallet. Om så inte är fallet, klicka på `Retype` och välj sedan mellan `BIP44`, `BIP49` eller `BIP84` beroende på dina behov.

Utöver detta verktyg är fliken `Underhåll` i RoninUI full av andra användbara funktioner:


- Transaktionsverktyg*: Gör det möjligt att granska detaljerna i en viss transaktion;
- Address-verktyg*: Gör det möjligt att bekräfta spårningen av en viss Address av din Dojo;
- Skanna block på nytt*: Tvingar noden att utföra en ny skanning av ett specificerat blockintervall.


Fliken `Push Tx` är en annan intressant funktion i RoninUI, som möjliggör sändning av en signerad transaktion i Bitcoin-nätverket. Transaktionen måste anges i hexadecimal form.


När det gäller de andra flikarna som finns tillgängliga på din RoninUI-panel:


- `Applikationer`: Här finns Whirlpool-applikationen, och den kommer säkert att användas för att integrera nya applikationer i framtiden;
- `Loggar`: Ger tillgång till programvarans händelseloggar i realtid;
- systeminformation: Ger allmän information om noden, t.ex. CPU-temperatur, användning av lagringsutrymme eller RAM-data. Du hittar också alternativen `Reboot` och `Shut down` för att starta om eller stänga av noden;
- `Inställningar`: Här kan du ändra ditt användarlösenord.


Så där ja! Tack för att du följde denna handledning till slutet. Om du tyckte om det uppmuntrar jag dig att dela det på sociala medier. Om du har möjlighet kan du dessutom överväga att stödja de utvecklare som gör dessa gratis programvaror med öppen källkod tillgängliga för vårt samhälle med en donation: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). För att fördjupa din kunskap om RoninDojo och upptäcka fler resurser rekommenderar jag starkt att du konsulterar länkarna till de externa resurser som nämns nedan.


**Externa resurser:**


- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)