---
name: Nmap
description: Master Nmap för nätverkskartläggning och sårbarhetsscanning
---

![cover](assets/cover.webp)



*Denna handledning är baserad på originalinnehåll av Mickael Dorigny publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar har gjorts i originaltexten.*



___



Välkommen till den här introduktionen till Nmap, som är avsedd för alla som vill lära sig att använda detta kraftfulla verktyg för nätverksskanning. Målet är att ge dig de grundläggande kunskaper du behöver för att använda Nmap effektivt i vardagen.



Nmap är ett mångsidigt verktyg som ofta används av IT-, nätverks- och cybersäkerhetspersonal för diagnostik, nätverksupptäckt och säkerhetsgranskning. Denna handledning vänder sig till dig som är ny inom dessa områden och vill lära dig grunderna i Nmap. Grundläggande kunskaper i system- och nätverksadministration rekommenderas.



Du får lära dig grunderna i Nmap, hur du utför portskanningar, identifierar aktiva värdar i ett nätverk, upptäcker serviceversioner och operativsystem, utför sårbarhetsskanningar och mycket mer. Varje avsnitt innehåller detaljerade förklaringar och praktiska exempel som hjälper dig att behärska användningen av Nmap i olika sammanhang.



I slutet av denna handledning kommer du att ha en gedigen förståelse för Nmap och kunna använda det effektivt för att förbättra säkerheten och hanteringen av dina nätverk. Njut av din läsning.



## 1 - Introduktion till Nmap: Vad är Nmap?



### I. Presentation



I det här första avsnittet tar vi en titt på nätverksskanningsverktyget Nmap. Vi tittar på de viktigaste Elements som du behöver veta om det här verktyget och hur det fungerar i allmänhet. Detta kommer att hjälpa oss att bättre förstå resten av handledningen.



### II. Introduktion av Nmap-verktyget



Nmap, som står för _Network Mapper_, är ett kostnadsfritt verktyg med öppen källkod som används för **nätverksupptäckt, kartläggning och säkerhetsgranskning**. Det kan också användas för andra uppgifter, t.ex. **nätverksinventering, diagnostik eller övervakning**.



Det kan avgöra om värdarna i ett visst nätverk är aktiva och nåbara, vilka nätverkstjänster som är exponerade, vilka versioner och tekniker som används och annan användbar analysinformation. Nmap kan användas för att skanna en enda tjänst på en specifik maskin eller över stora delar av nätverket, upp till hela Internet.



Nmaps styrkor är många:





- Kraftfull och flexibel**: Nmap kan skanna stora nätverk och använda avancerade detekteringstekniker. Den stöder UDP, TCP, ICMP, IPv4 och IPv6 och kan utföra versionsdetektering, sårbarhetsskanningar eller protokollspecifika interaktioner. Dess arkitektur är modulär, särskilt tack vare NSE-skript (Nmap Scripting Engine), som vi kommer att titta på senare i denna handledning.
- Användarvänlighet**: Den officiella dokumentationen är riklig och av högsta kvalitet. Det finns också många resurser tillgängliga för att hjälpa dig att komma igång.
- Popularitet och lång livslängd**: Nmap har varit en referens inom sitt område sedan 1998. Den aktuella versionen, vid tidpunkten för den här uppdateringen, är 7.95. Även om det finns andra verktyg för specifika uppgifter är Nmap fortfarande ett måste för kartläggning och analys av nätverk.



**Nmap på bio**



Nmap är ett av de få säkerhetsverktyg som har fått en viss berömmelse bland allmänheten. Det förekommer i filmen _Matrix Reloaded_, i en emblematisk scen där Trinity använder det för att hacka sig in i ett system:



![nmap-image](assets/fr/01.webp)



matris: Reloaded-scen med Nmap



Han förekommer också i andra filmverk.



**Återkoppling



Som systemadministratör och sedan cybersäkerhetsrevisor och pentester **använder jag Nmap nästan dagligen** och jag **rekommenderar** det regelbundet till systemadministratörer som vill stärka sin kontroll över nätverk och förbättra sina diagnostiska möjligheter.



### III. Drift på hög nivå



Nmap finns tillgängligt för Linux, Windows och macOS. Det är huvudsakligen skrivet i C, C++ och Lua (för NSE-skript). Det används huvudsakligen på kommandoraden, även om grafiska gränssnitt som Zenmap också finns tillgängliga. Vi rekommenderar dock starkt att du börjar med kommandoraden för att bättre förstå hur det fungerar.



Ett enkelt exempel:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Detta kommando kommer att förklaras i detalj senare. I den här handledningen kommer vi att använda Nmap på Linux, men dess användningsområden är liknande på andra system. Under Windows förlitar sig Nmap på biblioteket **Npcap** (som ersätter det nu föråldrade WinPcap) för att fånga och injicera nätverkspaket.



Nmap används på samma sätt som ett konventionellt binärt program, t.ex. `ls` eller `ip`. Vissa avancerade funktioner kan kräva utökade rättigheter, eftersom verktyget ibland manipulerar paket på okonventionella sätt för att framkalla specifika reaktioner på målsystem (särskilt för att upptäcka tjänster eller sårbarheter).



### IV. Konsekvenser av att använda Nmap



Innan du använder Nmap är det viktigt att du är medveten om dess potentiella inverkan på nätverk och system:





- Den kan skicka **tusentals eller till och med miljontals paket** på kort tid, vilket kan mätta vissa nätverksinfrastrukturer.
- Det kan generate **missbildade eller icke-standardiserade** paket, som sannolikt kommer att störa viss utrustning (särskilt industriella system).
- Det kan producera **attackliknande beteende**, vilket kan utlösa varningar i säkerhetssystem (brandväggar, IDS/IPS, etc.).



Generellt sett är **Nmap ett mycket pratsamt verktyg**, eftersom det genererar mycket trafik för att extrahera så mycket information som möjligt. Det är därför lämpligt att till fullo förstå hur det fungerar innan du använder det i känsliga miljöer eller produktionsmiljöer.



### V. Slutsats



Detta avsnitt introducerar Nmap och dess huvudfunktioner. Vi har sett att det är ett viktigt, kraftfullt och flexibelt verktyg för nätverkskartläggning. Vi har också diskuterat hur det fungerar och vilka försiktighetsåtgärder du måste vidta när du använder det, för att skapa förutsättningar för följande delar av handledningen.



## 2 - Varför använda Nmap?



### I. Presentation



I det här avsnittet tar vi en titt på de viktigaste användningsområdena för nätverksskanningsverktyget Nmap. Vi kommer att se att det är ett verktyg som används i många sammanhang och yrken, och att det definitivt är en användbar färdighet att ha det i din verktygslåda och veta hur man behärskar det.



### II. Användning av Nmap för diagnostik och övervakning



Nmap kan användas för nätverksdiagnostik och, mer allmänt, för övervakning. På samma sätt som en ping kan användas för att avgöra om två värdar kommunicerar, kan Nmap användas för att snabbt avgöra om en värd är aktiv eller om en viss tjänst är i drift. Tack vare [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") kan vi få exakta uppgifter om en värds svarstid, den väg som paketen tar, det svar som en viss tjänst ger osv.



Följande kommando och resultat kan t.ex. användas för att snabbt ta reda på om en webbserver på host **192.168.1.18** är aktiv och svarar korrekt:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Använd Nmap för att hämta webbtjänststatus från en fjärrserver



Så att använda Nmap går längre än det berömda "ping-testet" under felsöknings- eller diagnostiska faser. Vi kommer senare att se att det finns flera metoder som används av Nmap för att identifiera vilken tjänst som lyssnar på en viss port, inklusive dess version.



### III. Använda Nmap för nätverksmappning



Som _Network Mapper_ är kartläggning av nätverk huvudsyftet med detta verktyg. Det kan användas inom ett lokalt nätverk, eller över flera nätverk, subnät och VLAN, för att lista alla nåbara värdar och tjänster. Nmap gör denna uppgift mycket snabbare och mer effektiv än någon manuell metod.



Följande kommando kan t.ex. användas för att snabbt identifiera aktiva värdar i nätverket **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Observera: alternativet `-sP` är föråldrat och har ersatts av `-sn`.*



![nmap-image](assets/fr/03.webp)



*Använda Nmap för att upptäcka nåbara värdar i ett nätverk*



Vi kommer senare att se att det finns flera metoder som används av Nmap för att avgöra om en värd kan betraktas som "aktiv", även om den inte på förhand exponerar några tjänster.



### IV. Använda Nmap för att utvärdera en filtreringspolicy



Nmap har fördelen av att vara faktabaserad: dess resultat gör det möjligt att fastställa konkreta resultat, till skillnad från alla arkitekturdokument eller filtreringspolicyer. Det är ett viktigt verktyg för att bedöma hur effektivt informationssystemet är uppdelat, eftersom det gör det möjligt att **verifiera om filtreringspolicyn faktiskt tillämpas**.



I ett företagsnätverk kräver bästa praxis att systemen är segmenterade efter roll, kritikalitet eller plats. Filtreringsregler (ofta implementerade via brandväggar) måste begränsa kommunikationen mellan zonerna. Men dessa konfigurationer är ofta komplexa och felbenägna.



Så för att validera att policyn har respekterats finns det inget bättre än ett konkret test. Du kan t.ex. kontrollera att känsliga administrationstjänster (SSH, WinRM, MSSQL, MySQL etc.) inte är åtkomliga från en användarzon.



Användningen av **Nmap för att testa filtreringspolicyn** bör vara systematisk innan en sådan policy sätts i produktion. Tyvärr försummas denna kontroll ofta.



Enligt min erfarenhet går många konfigurationsfel obemärkta förbi om det inte finns några valideringstester. Ett enkelt fel i ett IP-intervall eller en regelövervakning kan göra att en förmodat isolerad zon blir sårbar.



### V. Använda Nmap för säkerhetsgranskning och penetrationstestning



Nmap har **många användbara funktioner för säkerhetsbedömning**, penetrationstestning (pentests) och tyvärr även för angripare.



Funktioner för nätverksupptäckt är avgörande för en angripare som behöver förstå nätverkstopologin efter en första kompromettering. Men Nmap erbjuder mycket mer än så: det integrerar en skriptmotor, varav **många är avsedda för sårbarhetsdetektering**.



Det här kommandot kan t.ex. användas för att kontrollera om en FTP-tjänst tillåter en anonym anslutning utan att du behöver ansluta manuellt:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Använda ett NSE-skript för att kontrollera anonym FTP-autentisering via Nmap.*



Nmap sårbarhetsdetektering är ett av de första stegen i en revision eller ett penetrationstest. Det gör att du snabbt kan identifiera vissa svaga punkter och optimera dina analysinsatser.



Men var försiktig: **verktyg för sårbarhetsskanning har sina begränsningar**. Nmap täcker bara en bråkdel av hoten och garanterar inte att ett system är säkert om inga problem upptäcks. Det är därför viktigt att **förstå hur de skript som används fungerar** och inte enbart förlita sig på deras omdöme.



### VI. Slutsatser



Vi har sett att om man behärskar Nmap kan man täcka ett brett spektrum av användningsområden, från diagnostik och övervakning till kartläggning, utvärdering av säkerhetspolicy och sårbarhetsskanning. I nästa avsnitt kommer vi att gå till botten med det hela och installera Nmap.




## 3 - Installera och konfigurera Nmap



### I. Presentation



I det här avsnittet lär vi oss hur du installerar nätverksskanningsverktyget Nmap på Linux och Windows OS. I slutet av det här avsnittet har vi allt vi behöver för att börja använda Nmap för framtida moduler. Slutligen kommer vi att se vilka privilegier det kan kräva när det används och varför.



### II. Installera Nmap under Linux



Nmap utformades ursprungligen för att köras på GNU/Linux-operativsystem. Som ett resultat av detta, och tack vare dess långa livslängd och popularitet, hittar du det i alla officiella arkiv för de stora Unix-distributionerna. I den här handledningen kommer jag att använda ett Debian-baserat operativsystem [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Men du kan använda det på exakt samma sätt från en klassisk Debian, CentOS, Red Hat eller vad som helst!



Under Debian kan du använda följande kommando för att kontrollera att Nmap finns i dina aktuella arkiv:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Svaret här indikerar tydligt att paketet "nmap" finns i arkiven (här, de av Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Från och med nu kan du installera Nmap via de vanliga installationskommandona, inget avväpnande för tillfället 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



För att kontrollera att Nmap är korrekt installerat visar vi dess version:



```
nmap --version
```



Här är det förväntade resultatet:



![nmap-image](assets/fr/05.webp)



resultat av att visa den aktuella versionen av Nmap._ _



Notera att biblioteket "libpcap" (_Packet Capture Library_) och dess version finns med i denna visning. "libpcap" används också av Wireshark och används av Nmap för att skapa och manipulera paket och lyssna på nätverkstrafik.



### III Installera Nmap på Windows



För att installera på ett Windows-operativsystem börjar du med att ladda ner binärfilen från den officiella webbplatsen (och ingen annan!):





- Nmap nedladdningssida på den officiella webbplatsen: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Du måste sedan ladda ner binärfilen med namnet `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



nmap för Windows installation binär nedladdningssida



När du har denna binärfil på ditt system är det bara att köra den för att installera Nmap. Det här är en enkel installation och du kan lämna alla alternativ som standard.



Min reflex är att avmarkera rutan "zenmap (GUI Frontend)". Det här är en grafisk Interface för Nmap som jag inte använder och som inte kommer att tas upp i den här handledningen, men du får gärna prova den när du har lärt dig kommandoradsverktyget Nmap!



![nmap-image](assets/fr/07.webp)



valfritt bortval av Zenmap vid installation av Nmap på Windows



I slutet av Nmap-installationen föreslås en andra installation: den av biblioteket "Npcap":



![nmap-image](assets/fr/08.webp)



installation av biblioteket "Npcap" vid installation av Nmap under Windows



Detta är det bibliotek som Nmap förlitar sig på för att hantera nätverkskommunikation, dvs. bygga, skicka och ta emot nätverkspaket. Du har förmodligen redan stött på det här biblioteket om du använder Wireshark på Windows, eftersom det också använder det och kräver installation.



Precis som med Linux kan du kontrollera att Nmap är installerat genom att öppna en kommandotolk eller en [Powershell]-terminal (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") och skriva följande kommando:



```
nmap --version
```



Här är det förväntade resultatet:



![nmap-image](assets/fr/09.webp)



resultat av att visa den aktuella versionen av Nmap._ _



Nmap är nu installerat på Windows. Du kan använda det på exakt samma sätt som på Linux genom att följa den här handledningen.



### IV. Lokala behörigheter krävs för att använda Nmap



Men förresten, när du använder Nmap, **är det nödvändigt att ha förhöjda lokala behörigheter på systemet? **det beror på**.



I sin mycket grundläggande form, dvs. utan att gå särskilt långt i användningen av dess alternativ, kräver Nmap inte nödvändigtvis privilegierade rättigheter. Du kommer dock snart att inse att det är bättre att använda Nmap i ett privilegierat sammanhang ("root" under Linux, "administrator" eller motsvarande under Windows) för att kunna utnyttja dess fulla potential, med risk för att få ett felmeddelande som detta:



![nmap-image](assets/fr/10.webp)



felmeddelande under Linux när Nmap-alternativ kräver root-rättigheter



Oavsett om du använder Linux eller Windows finns det många fall där Nmap kommer att be dig om privilegierad åtkomst. De främsta orsakerna är följande (icke uttömmande lista):





- Konstruera "råa" nätverkspaket**: Nmap kan använda ett brett spektrum av skanningsmetoder, inklusive avancerad paketmanipulation och paketkonstruktion. Detta är till exempel fallet när vi vill utföra TCP SYN-skanningar, som inte respekterar den klassiska _trevägshandskakningen_ i TCP-utbyten. För att göra detta måste Nmap använda andra funktioner än de som är inbyggda i operativsystem, som bara vet hur man respekterar god praxis i nätverkskommunikation (det anropar biblioteken "Npcap" och "libcap" som ses ovan). Det är för att Nmap inte gör saker på det "vanliga" sättet som den kan härleda viss information om operativsystem, tjänster och vissa sårbarheter.





- Lyssna på nätverkstrafik**: vissa av Nmaps alternativ kräver att den lyssnar på nätverket för att kunna hämta viss information. Denna åtgärd anses vara känslig på operativsystem, eftersom den också gör det möjligt att lyssna på kommunikationen från andra applikationer på systemet. Precis som Wireshark behöver Nmap särskilda behörigheter för att göra detta, vilka är lättare att få genom att vara direkt i en privilegierad session.





- Lyssna på privilegierade portar**: På operativsystem sägs portar från 0 till 1024 (TCP såväl som UDP) vara privilegierade, dvs. de är på något sätt reserverade för mycket specifika användningsområden och därför skyddade. Även om detta är ett något föråldrat skäl idag, är det fortfarande nödvändigt att ha vissa privilegier för att lyssna på dessa portar, vilket Nmap kan behöva göra beroende på hur det kommer att användas.





- Skicka UDP-paket:** På samma sätt kräver lyssnande på en nätverksapplikation på UDP-portar (ett statslöst protokoll) privilegierade rättigheter på operativsystemen. En privilegierad session krävs därför om du vill utföra en UDP-sökning, för vilken Nmap måste lyssna efter ett svar för att kunna analysera svaren på dess sökningar.




För att vara mer exakt är det möjligt, åtminstone under Linux, att köra Nmap med alla dess funktioner och alternativ utan att faktiskt vara root. Detta uppnås genom att bevilja rätt _kapaciteter_ till binärfilen. Detta kräver dock avancerad manipulation och är kanske inte lika praktiskt som att köra Nmap direkt med privilegier. Det här tillvägagångssättet är dessutom mindre vanligt och kan orsaka säkerhetsproblem om det är felkonfigurerat.



Detta är dock lite av en avvikelse från vår Nmap-handledning, så vi avstår från det för tillfället.



I resten av den här handledningen ska du anta att Nmap alltid körs som "root" (från ett skal som "root" eller via kommandot "sudo") eller i en administratörsterminal under Windows, även om detta inte anges. Annars kan du uppleva subtila men märkbara skillnader från handledningen.



### V. Slutsats



Nu är det klart! Nmap är nu installerat på vårt operativsystem och redo att användas, utan ytterligare konfigurering. Detta avsnitt avslutar introduktionen och presentationen av Nmap. Jag hoppas att det har fått det att vattnas i munnen på dig och att du är ivrig att börja öva.



På ett mer allvarligt sätt har vi nu en bättre uppfattning om vad kartläggningsverktyget Nmap är och vilka dess vanligaste användningsområden är, liksom dess begränsningar. Låt oss gå vidare!




## 4 - TCP- och UDP-portskanningar med Nmap



### I. Presentation



I det här avsnittet lär vi oss att utföra våra första portskanningar med hjälp av nätverksskanningsverktyget Nmap. Vi kommer att se hur man använder det för att sammanställa en lista över nätverkstjänster som exponeras på en värd, oavsett om de använder TCP- eller UDP-protokoll.



Från och med nu ska du komma ihåg att endast skanna värdar i en kontrollerad miljö som du har uttryckligt tillstånd för.





- Som en påminnelse: [Brottsbalken: Kapitel III: Angrepp på system för automatisk databehandling] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Om du inte har en till hands**, rekommenderar jag följande gratislösningar, som är precis vad du behöver!





- [Hack The Box] (https://app.hackthebox.com/ "Hack The Box")**: Hacking-utbildningsplattformen Hack The Box tillhandahåller ständigt sårbara system som du kan attackera efter eget gottfinnande. Flera hundra system finns tillgängliga, men en förnyad pool med 20 maskiner erbjuds gratis året runt, med åtkomst via en OpenVPN VPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Denna plattform erbjuder många avsiktligt sårbara system för nedladdning, som kan användas via VirtualBox (även en gratis lösning) eller på andra sätt. När du har laddat ner finns det inget behov av VPN - allt är lokalt.




Det står dig också fritt att **skapa en virtuell maskin** på ditt favoritoperativsystem och installera olika tjänster på den som testmål. Fördelen här är att du också kommer att kunna se vad som händer på serversidan under en skanning, särskilt med Wireshark, och ha en hand i den lokala brandväggen när vi gör mer avancerade tester.



Nu går vi till det praktiska!



### II. Skanning av en värds TCP-portar via Nmap



#### A. Första TCP-portskanningen med Nmap



Vi ska nu göra våra första skanningar via Nmap. Vårt mål här är enkelt: vi vill ta reda på vilka tjänster som exponeras av den webbserver vi just har distribuerat, för att se om det finns något oväntat, till exempel en administrationstjänst som inte borde vara tillgänglig, eller exponeringen av en port för en applikation som vi trodde var avaktiverad.



I mitt exempel har den värd som ska skannas IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Här är ett möjligt resultat. Vi ser en klassisk Nmap-retur med mycket information:



![nmap-image](assets/fr/11.webp)



resultat av en enkel TCP-scanning utförd med Nmap._ _



En snabb titt på det här resultatet visar att portarna TCP/22 och TCP/80 är tillgängliga på den här värden.



Som standard, och om du inte säger åt den att göra det, kommer Nmap bara att skanna TCP-portar.



#### B. Förstå resultaten av en enkel Nmap-sökning



Vi måste dock gå ett steg längre för att förstå utdata: varje rad är viktig, dels för att veta vad som just har gjorts, dels för att kunna tolka själva skanningsresultaten på rätt sätt.



Den första raden är i huvudsak en påminnelse om skanningsversion och datum (trots allt användbart för loggning och arkivering!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Den andra raden visar början av skanningsresultaten för värden "debian.home (192.168.1.19)". Den här informationen kommer att vara användbar när vi börjar skanna flera värdar samtidigt:



```
Nmap scan report for debian.home (192.168.1.19)
```



På den tredje raden står det att värden i fråga är "Up", dvs. aktiv:



```
Host is up (0.00022s latency).
```



Slutligen informerar Nmap oss om att 998 TCP-portar som identifierats som stängda inte visas i:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Detta sparar oss nästan 1.000 rader med utdata som ser ut som:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Tack till honom för att han besparade oss detta!



Varför 998 "stängda" portar? Om man lägger till de 2 öppna portarna blir det 1000, och det är det antal portar som Nmap kommer att skanna i sin standardkonfiguration, inte de 65535 befintliga TCP-portarna! Vi kommer senare att se att detta är helt och hållet och enkelt anpassningsbart. Men om den utvalda värden har en tjänst som lyssnar på en ganska exotisk port, kommer denna "standard" skanning inte att avslöja den.



Efter denna information hittar vi det som är mest intressant: en tabell som är organiserad enligt de tre kolumnerna "PORT - STATE - SERVICE":





- Den första kolumnen "PORT" anger helt enkelt den port/det protokoll som avses, och här är det viktigt att titta på om det är en TCP-port (`<port>/tcp`) eller UDP (`<port>/udp`).





- Kolumnen "STATE" anger statusen för den nätverkstjänst som upptäckts på den här porten och som bestämts av Nmap på grundval av det erhållna svaret. Detta kan vara "open", "closed", "filtered" eller "unknown". Vi kommer senare att se hur Nmap skiljer mellan dessa olika tillstånd.





- Kolumnen "SERVICE" anger den tjänst som exponeras på porten i fråga. Observera dock att vi inte har använt aktiva alternativ för tjänsteupptäckt här. Nmap förlitar sig på en lokal referens mellan en port/ett protokoll och den förmodade tilldelade tjänsten: filen "/etc/services"




Om du tittar på filen "/etc/services" på ett Linux-system hittar du en länk "port/protocol - service" som liknar den som visas av Nmap:



![nmap-image](assets/fr/12.webp)



extraherar innehållet i filen "/etc/services" under Linux



Det är viktigt att förstå att Nmap för närvarande inte har utfört någon aktiv tjänsteupptäckt. Det skulle till exempel inte ha varit möjligt att identifiera SSH-tjänsten bakom en TCP/80-port om så hade varit fallet. Därav vikten av att veta hur man använder rätt alternativ - det kommer snart!



Att veta hur man tolkar Nmaps utdata är en viktig del av att bemästra verktyget. Den goda nyheten är att utdata i stort sett kommer att vara densamma, oavsett vilka alternativ du använder.



#### C. Under huven: nätverksanalys via Wireshark



Om du tittar noga på vad som händer i nätverket Interface hos värden som skannar servern, eller på själva servern, kommer Nmaps åtgärder att bli mycket tydligare. Det är vad vi kommer att göra här.



Det jag kan visa dig här är bara en del av det som syns i Wireshark. Om du vill gå längre får du gärna göra en nätverksinspelning själv under en skanning och sedan bläddra igenom vad som har fångats.



I det här testet finns min skanningsvärd (192.168.1.18) och min målvärd (192.168.1.19) i samma lokala nätverk.



Nmap börjar med att ta reda på om målvärden är aktiv i det lokala nätverket genom att skicka en ARP-begäran. Om den får ett svar vet den att värden är aktiv och påbörjar sin nätverksskanning:



![nmap-image](assets/fr/13.webp)



_ARP-begäran utfärdad av Nmap för att avgöra om en målvärd finns i det lokala nätverket._



Om den värd som ska skannas finns i ett fjärranslutet nätverk börjar Nmap med att skicka en ping-begäran och försöker nå några av de mest exponerade portarna (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



ping-begäran utfärdad av Nmap för att avgöra om en målvärd är nåbar i ett fjärrnätverk



Om den får ett svar på något av dessa tester anser den att målet är aktivt.



När Nmap har fastställt att målet är aktivt försöker den lösa upp dess domännamn med DNS-servern som är konfigurerad på nätverkskortet:



![nmap-image](assets/fr/15.webp)



dNS-upplösning på mål för Nmap-sökning



Nu när Nmap har identifierat sitt mål och vet att det är aktivt, börjar det sin TCP-portskanning:



![nmap-image](assets/fr/16.webp)



tCP SYN-paketsändning och RST/ACK-mottagning under Nmap-sökning



För att göra detta kommer det, på varje TCP-port i sitt standardintervall, att **sända TCP SYN-paket och vänta på svar**. I skärmdumpen ovan får den TCP RST/ACK-paket från den skannade servern, vilket betyder "gå vidare, här finns inget att se" - med andra ord är dessa portar stängda. Som vi såg i resultatet kommer detta att vara fallet för de flesta av de portar som skannas. Med två undantag:



![nmap-image](assets/fr/17.webp)



svar på ett TCP SYN-paket som skickas på port 22, aktivt på skanningsmålet



I skärmdumpen ovan ser vi ett TCP SYN/ACK-paket som skickas av målvärden**. Porten är aktiv och exponerar en tjänst. Nmap bekräftar mottagandet av svaret och avslutar sedan anslutningen (TCP RST/ACK). **Det var så den visste att port TCP/22 var aktiv**.



Vi har här sett att Nmap respekterar "trevägshandskakningen" vid skanning av ett TCP-nätverk. Av prestandaskäl är det möjligt att be den att inte svara på serverns retur, vilket sparar flera tusen paket när man skannar ett stort nätverk. Men vi kommer att titta på dessa alternativ och optimeringar senare i handledningen.



Vi har nu en bättre uppfattning om hur man gör en TCP-sökning och vad som faktiskt händer när den utförs. Vi har också sett att Nmap som standard utför en TCP-portskanning på ett begränsat antal portar.



### III. Skanna UDP-portar med Nmap



#### A. Första UDP-portskanningen med Nmap



Låt oss nu se hur man skannar en värds UDP-portar. Som vi har sett kommer Nmap som standard alltid att skanna TCP-portar. Detta kan innebära att vi missar en hel del information om vi inte är medvetna om det.



Som en påminnelse: i det här testet befinner sig min skanningsvärd (192.168.1.18) och min målvärd (192.168.1.19) i samma lokala nätverk.



```
nmap -sU 192.168.1.19
```



Här har den erhållna returen samma format som för en TCP-sökning, men de aktiva tjänster som visas är i `<port>/UDP`, enligt begäran!



![nmap-image](assets/fr/18.webp)







Alternativet "-sU" används för att tala om för Nmap att du vill arbeta med UDP, i stället för TCP som är standard.



Förresten kommer du förmodligen att märka att Nmap kräver "root"-rättigheter för UDP-skanningar, som nämnts tidigare i handledningen.



obs: Sedan de senaste versionerna av Nmap rekommenderas det alltid att köra UDP-scanningar med administratörsbehörighet för att säkerställa tillförlitliga resultat, eftersom vissa funktioner kräver rå åtkomst till nätverksuttag



UDP-skanningar kan ta mycket lång tid (1100 sekunder för att skanna 1000 portar i mitt exempel), på grund av avsaknaden av "trevägshandskakning" i UDP, vilket innebär att Nmap väntar på ett svar för varje UDP-paket som skickas och fastställer porten som "stängd" endast om det inte kommer något svar efter en viss tid (timeout). Detta svar från skannade värdar är inte systematiskt och är ofta begränsat när det gäller antalet svar per sekund för att undvika vissa förstärkningsattacker. Detta står i kontrast till TCP, där det kommer ett omedelbart svar från den skannade värden, oavsett om porten är öppen eller stängd. Vi kommer senare att se hur man optimerar detta.



En annan svårighet med UDP är **att tjänster inte alltid svarar på inkommande paket**, helt enkelt för att det inte alltid är nödvändigt och det är principen för UDP. När detta är fallet, och ingen ICMP "port unreachable" tas emot, markeras tjänsten som "öppen|filtrerad" av Nmap, vilket visas i skärmdumpen ovan.



#### B. Under huven: nätverksanalys via Wireshark



Precis som med vår TCP-sökning ska vi titta närmare på vad som händer på nätverksnivå under en UDP-sökning med hjälp av en Wireshark-analys. Nmaps beteende för att avgöra om en värd är aktiv är detsamma.



Den enda verkliga skillnaden vid skanning av UDP är att Nmap inte väntar på en "trevägshandskakning", eftersom denna mekanism inte finns i UDP (statslöst protokoll):



![nmap-image](assets/fr/19.webp)



sändning av uDP-paket och mottagning av ICMP (port inte nåbar) under Nmap-sökning



På skärmdumpen ovan kan vi se att Nmap skickar ett stort antal UDP-paket och får ett ICMP-paket "Destination unreachable (Port unreachable)" som svar på de flesta av dem. Detta är normalt, eftersom det är det lämpliga svar som definieras av [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") när en UDP-port inte kan nås:



![nmap-image](assets/fr/20.webp)







Låt oss ta en närmare titt på denna Wireshark-fångst, som visar **de tre möjliga scenarierna** i UDP:



![nmap-image](assets/fr/21.webp)



nätverksinspelning under en UDP-sökning på olika portar med Nmap._



De tre fallen är följande:





- Den första Exchange består av paketen nr. 3, 4 och 8, 9. Nmap skickar UDP-paket på den klassiska SNMP-porten och **konstruerar därför protokollkonforma paket i förväg**. Därefter erhålls ett svar från servern (paket nr 8 och 9). Resultat: Nmap har fått ett svar, tjänsten är "öppen".





- Den andra Exchange består av paketen 6 och 7. Nmap skickar ett "tomt" UDP-paket (utan protokollstruktur) till port UDP/165 och får ett ICMP-paket som svar: "Destination kan inte nås (Port kan inte nås)". Resultat: Nmap har fått ett (negativt) svar, värden är uppe, men tjänsten som den försökte nå är inte i drift på den här porten, som kommer att markeras som "stängd".





- Den sista Exchange består av paket nr 12: Nmap skickar ett "tomt" UDP-paket till port UDP/1235. Det kommer inget svar, inte ens en uttrycklig vägran från den skannade värden. Resultat: Nmap markerar porten som "öppen|filtrerad", eftersom den inte kan avgöra om detta beror på att det finns en brandvägg som är konfigurerad att inte svara, eller på en aktiv UDP-tjänst som ändå inte returnerar något svar (inte obligatoriskt i UDP).




Här är resultatet som visas av Nmap efter dessa tre fall:



![nmap-image](assets/fr/22.webp)



möjliga resultat av en UDP-sökning utförd via Nmap._



Vi har nu en bättre uppfattning om hur man gör en UDP-sökning och vad som faktiskt händer när den utförs. Hittills har vi bara använt Nmap på ett mycket enkelt sätt, utan att egentligen bestämma vilka portar som ska skannas, men det kommer att förändras!



### IV. Finjustera portskanning med Nmap



#### A. Påminnelse om Nmaps standardbeteende



Som vi har sett väljer Nmap själv det antal och de portar som ska skannas om du inte anger några alternativ. Detta är den "standardkonfiguration" som används av Nmap när du inte berättar exakt vad den ska göra. Dessa standardalternativ är utformade för att ge en uppfattning om de viktigaste portarna som exponeras, dessa väljs efter exponeringsfrekvens (vanligaste eller mest frekventa portar) snarare än i numerisk ordning (port 1, 2, 3, etc.) och även för att undvika att starta en skanning av de 65535 möjliga portarna om du inte anger lämpliga alternativ, vilket skulle vara för långt och ordrikt för ett "standard"-användningsfall.



**Hur väljs dessa portar ut?



De 1000 portar som skannas i standardläget väljs utifrån hur ofta de förekommer. Denna statistik underhålls av Nmap och uppdateras på samma sätt som själva binärprogrammet och dess skript (moduler). Du kan själv se denna statistik i filen "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



extraherad från filen "/usr/shares/nmap/nmap-services"._



Här, i den tredje kolumnen, ser vi något som ser ut som sannolikheter (mellan 0 och 1) eller en procentuell fördelning. Detta är frekvensen för förekomsten av varje port/protokoll-par. Vi kan se att de mest välkända portarna (FTP, SSH, TELNET och SMTP i det här utdraget) har ett mycket högre värde än de andra.



#### B. Ange exakt målportar för en Nmap-sökning



Men i den verkliga världen kan vi behöva skanna endast en specifik port, eller flera portar, eller ett specifikt intervall av portar. Nmap gör det enkelt att göra just detta, på ett enhetligt sätt för både UDP- och TCP-scanningar.



**Skanna en specifik port via Nmap**



Om vi vill skanna en enda port, och inte 1000, kan vi ange denna port via Nmaps alternativ "-p" eller "--port":



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Som ett resultat blir skanningen naturligtvis mycket snabbare och Nmap skickar bara ut de paket som behövs för att upptäcka om värden är aktiv och sedan om den angivna porten är nåbar. Detta sparar tid om du bara vill köra ett snabbt test för att se om webbtjänsten på din showcase-webbplats fortfarande är uppe.



**Skanning av flera portar via Nmap**



På samma sätt kan vi ange flera portar till Nmap genom att använda samma alternativ och sammanfoga de angivna portarna med ett kommatecken:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Oavsett ordning kommer Nmap att kontrollera alla dessa portar, och bara de på den utvalda värden. Du kommer att märka i Nmaps utdata att den **explicit berättar för oss alla portar och deras status**, även om de är "stängda". Till skillnad från standardbeteendet, där denna fullständiga utdata skulle ha tagit upp alldeles för mycket utrymme:



![nmap-image](assets/fr/24.webp)



*Resultatet av en Nmap TCP-scanning på de angivna portarna.*



**Skanna en rad olika portar



Om antalet portar som du vill skanna är för stort kan du ange dem per intervall, t.ex:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Naturligtvis kan du blanda och matcha som du vill, till exempel:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Skanning av TCP- och UDP-portar



Du kan också utföra UDP- och TCP-sökningar samtidigt på utvalda portar:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



I det sista exemplet ser du att "U:" anger en UDP-port och "T:" anger en TCP-port. Här är ett möjligt resultat av den här typen av skanning:



![nmap-image](assets/fr/25.webp)



*Resultatet av en TCP- och UDP-portskanning med Nmap.*



Det är ett intressant sätt att anpassa dina skanningar!



**Skanna alla portar



Slutligen är det möjligt att ange mycket större eller mindre intervall till Nmap. Vi har sett att den standardlista som väljs av Nmap innehåller 1000 portar. Vi kan också be om de 100 vanligaste portarna, eller de 200 vanligaste, med hjälp av alternativet "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Slutligen kan vi be den att skanna alla möjliga portar (alla 65535) med hjälp av notationen "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Det senare tar längre tid, särskilt med UDP, men du är säker på att inte missa några öppna portar.



*Observera: Alternativet "-p-" är den rekommenderade metoden för att skanna alla TCP-portar. För UDP-sökningar är det lämpligt att begränsa antalet portar av prestandaskäl, eftersom fullständiga sökningar av alla UDP-portar kan ta mycket lång tid.*



Senare i handledningen kommer vi att se hur man optimerar hastigheten på Nmap-skanningar för att passa våra behov, vilket kommer att vara särskilt användbart för skanningar på alla TCP- och UDP-portar.



### V. Slutsats



I det här avsnittet har vi äntligen fått lite praktisk övning, så vi vet nu **hur man använder Nmap på ett grundläggande sätt för att skanna en värds TCP- och UDP-portar**. Vi har också tittat i detalj på vad som händer på nätverksnivå och **hur Nmap avgör om en TCP- eller UDP-port är aktiv eller inte**. Slutligen vet vi hur vi kan välja de portar vi vill skanna och **vad Nmaps standardalternativ faktiskt gör**. I det följande kommer vi att återanvända denna kunskap och tillämpa den för att skanna ett helt nätverk, inklusive global kartläggning och nätverksupptäckt.




## 5 - Kartläggning och upptäckt av nätverk med Nmap



### I. Presentation



I det här avsnittet lär vi oss hur du använder nätverksskanningsverktyget Nmap för att kartlägga ditt nätverk. Vi kommer att se hur effektivt det kan vara i denna uppgift, genom dess olika alternativ. Slutligen tittar vi på olika sätt att ange målen för våra skanningar till Nmap.



Vi kommer framför allt att använda det vi lärde oss i föregående avsnitt om hur Nmap avgör om en värd är aktiv och nåbar.



Som nämndes i introduktionen till Nmap är detta en Network Mapper. Som sådant är det det perfekta verktyget för att upprätta en lista över tillgängliga värdar i ett nätverk, oavsett om det är lokalt eller fjärrstyrt.



**Författarens återkomst:**



Som cybersäkerhetsrevisor och pentester använder jag faktiskt Nmap systematiskt när jag utför interna penetrationstester för att ta reda på var jag är, vilka mina grannar är i det lokala nätverket och vilka andra nätverk som är tillgängliga, liksom de system som finns i dem. Mitt mål är enkelt: att kartlägga nätverket, bestämma storleken på informationssystemet och framför allt skissa upp dess attackyta.



Nätverkskartläggning kan också vara användbart i samband med nätverksdiagnostik, övervakning och tillgångskartläggning (är du verkligen säker på att ditt informationssystem endast består av det som finns i Active Directory eller i din GLPI/OCS-inventering? Det kan också användas för att upptäcka förekomsten av skugg-IT i ditt informationssystem.



### II. Använda Nmap för att skanna ett nätverksområde



#### A. Upptäcka ett nätverk med en Nmap-sökning



Vi skulle nu vilja gå ett steg längre och analysera hela vårt lokala nätverk. Inget kunde vara enklare: allt vi behöver göra är att återanvända de kommandon vi såg i föregående avsnitt, men ange en CIDR istället för en enkel IP Address.



CIDR (**Classless Inter Domain Routing**) är den "klassiska" beteckningen för att ange ett nätverksområde och dess utsträckning (med hjälp av masken). Till exempel är "192.168.0.0/24" en "översättning" av den decimala masknotationen "255.255.255.0".



Om du vill använda Nmap genom att ange en CIDR kan du göra på följande sätt:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Det är också möjligt att ange flera värdar, flera nätverk eller ett intervall, på samma sätt som med portar i föregående avsnitt:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Här är ett exempel på de resultat vi kan få när vi kör en sökning i ett nätverk:



![nmap-image](assets/fr/26.webp)



resultat av en Nmap-sökning för att kartlägga flera nätverk



I synnerhet ser vi flera aktiva värdar, och varje värdavsnitt börjar med en rad som den här:



```
Nmap scan report for <name> (<IP>)
```



Detta gör att vi tydligt kan se vilken host som följande resultat avser. Den allra sista raden är också viktig:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Vi vet att Nmap upptäckte 5 aktiva värddatorer i de nätverk som skannades.



#### B. Under huven: nätverksanalys via Wireshark



Vi ska nu titta närmare på vad som händer på nätverksnivå under en nätverksupptäckt som utförs via Nmap.



Som vi såg i föregående avsnitt använder Nmap som standard ARP-protokollet för att upptäcka förekomsten av värdar i det lokala nätverket:



![nmap-image](assets/fr/27.webp)



aRP-paket som fångas upp när ett lokalt nätverk skannas med Nmap och dess standardalternativ



Den kan därmed upptäcka i stort sett alla värddatorer i det lokala nätverket, eftersom svaret på en ARP-begäran i allmänhet kommer från alla värddatorer som är aktiva i nätverket och inte verkar misstänkta på något sätt.



För fjärrnätverk använder Nmap en kombination av tekniker:



![nmap-image](assets/fr/28.webp)



iCMP- och TCP-paket som fångas upp vid skanning av ett fjärrnätverk med Nmap och dess standardalternativ



För att vara mer exakt använder Nmap ett ICMP-ekopaket (det klassiska fallet med pinging) och ett ICMP Timestamp-paket, som vanligtvis används för att beräkna paketets transittid. Förhoppningen är att få svar från värdar i fjärrnätverk.



Men det är mer än så. Du kan se i Wireshark-fångsten ovan att **TCP SYN**-paket systematiskt skickas på TCP/443-portar för varje potentiell värd i de nätverk som ska skannas, liksom **TCP ACK**-paket på TCP/80-porten.



**Varför skicka TCP-paket till portar som en del av nätverksupptäckten?



Genom att skicka ett SYN-paket till en viss port kan Nmap ** avgöra om en tjänst lyssnar på den porten**. Om en värd svarar på ett SYN-paket med ett SYN/ACK-paket indikerar detta att den är aktiv och att en tjänst lyssnar på den porten. Nmap prövar därför lyckan på den här tjänsten, **även om inget svar på pingen har erhållits**.



Genom att skicka ett ACK-paket till en viss port kan Nmap **avgöra om det finns en brandvägg på den värden**. Om en värd svarar på ett ACK-paket med ett RST-paket (Reset) indikerar detta att det förmodligen finns en brandvägg på den värden som blockerar oönskad trafik. Värden avslöjar därmed sin närvaro i nätverket, även om den inte har svarat på andra förfrågningar.



Det är dock viktigt att notera att brandväggsdetektering med den här tekniken kanske inte är helt tillförlitlig i alla fall. Vissa värdar kan generate RST-svar av andra skäl än att det finns en brandvägg, t.ex. på grund av specifik konfiguration av tjänster eller operativsystem. Dessutom kan moderna brandväggar konfigureras så att de inte svarar på den här typen av identifieringsförsök.



Vi har nu kommit en bra bit på vägen och kan utföra grundläggande nätverksupptäckt. Vi kommer nu att titta på några fler alternativ som ger oss större kontroll över Nmaps beteende.



### III. Nätverksupptäckt utan portskanning med Nmap



Som du kanske har märkt utför Nmap som standard **en portskanning efter att ha upptäckt en aktiv värd**, vilket ger en enorm mängd paket och väntan på svar till vår skanning. Om du har 5 värdar i ditt nätverk kommer Nmap att försöka kontrollera statusen för cirka 5 000 portar, vilket kommer att ta längre tid.



Det är dock möjligt att använda Nmaps alternativ för att utföra **enbart en upptäckt av aktiva värdar** i ett nätverk, utan att upptäcka deras tjänster.



Om vi bara vill veta vilka värdar som är nåbara, utan någon information om de tjänster och portar som de exponerar, kan vi använda alternativet "-sn" för att utföra **enbart en skanning med ICMP Echo (ping) och ARP-förfrågningar**. Med andra ord, inaktivera portskanning helt och hållet:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Här är resultatet av en Nmap-nätverksupptäckt som utfördes utan portskanning:



![nmap-image](assets/fr/29.webp)



Resultat av en nätverksupptäckt utan portskanning med Nmap.



Vi har redan nämnt de möjliga begränsningarna med att använda enbart ICMP för host discovery (för fjärrnätverk). Det är därför Nmap också använder några trick som kan avslöja förekomsten av en brandvägg eller en specifik tjänst på värddatorer. Med hjälp av alternativ kan vi återanvända dessa trick och till och med utöka dem, utan att behöva börja om med en fullständig portskanning av varje värd som upptäcks.



För att göra detta använder vi alternativen "-PS" (TCP SYN) och "-PA" (TCP ACK), som gör det möjligt för oss att ange de portar vi vill ansluta till som en del av vår host discovery, samt alternativet "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Den här skanningen säkerställer redan att värdidentifieringen är lite mer fullständig än med standardalternativen.



Vi börjar få ganska omfattande kommandon som använder flera alternativ. Detta beror på att vi vet hur Nmap fungerar och begränsningarna i dess "standard"-alternativ, som ibland kan få oss att slösa tid eller missa viktiga Elements. Det är hela poängen med att ta sig tid att bemästra det!



För att beskriva alternativen i vår senaste order:





- "`-sn`: inaktiverar portskanning för varje aktiv värd som upptäckts av Nmap.





- "`-PP`: aktiverar ICMP-eko (ping-sökning) för att upptäcka värdar.





- "`-PS <PORT>`": skicka ett TCP SYN-paket på den eller de angivna portarna för att upptäcka en aktiv tjänst som avslöjar närvaron av en värd som inte har svarat på pingen.





- "`-PA <PORT>`": skicka ett TCP ACK-paket på den eller de portar som anges för att upptäcka en aktiv brandvägg som avslöjar att det finns en värd som inte har svarat på pingen.




I exemplet ovan anger jag de portar som jag anser vara de mest exponerade i mina Nmap-sammanhang för alternativet "-PS". Dessa olika portar kommer sedan att testas på varje värd, inte för att se om tjänsten de är värd för verkligen är aktiv, utan för att se om detta gör det möjligt för oss att upptäcka en värd som inte har svarat på vårt ICMP Echo medan den fortfarande är aktiv (via ett svar från tjänsten eller värdens brandvägg).



Här är vad som kan ses i en nätverksinspelning som tagits vid tidpunkten för en sådan skanning, i det här fallet ett utdrag på en enda målvärd:



![nmap-image](assets/fr/30.webp)



paket som skickas av Nmap under avancerad nätverksupptäckt, utan portskanning



Vi hittar våra TCP SYN-paket, vårt TCP ACK på port TCP/80 och vårt ICMP-eko. Nmap kommer att utföra alla dessa tester för varje värd som är målet för vår nätverksupptäcktssökning.



### IV. Använda en fil med tillgångar som mål med Nmap



Att specificera mål kan snabbt visa sig vara komplicerat i verkliga informationssystem, som ibland kan bestå av dussintals eller hundratals nätverk, subnät och VLAN. Därför är det enklare att använda en fil som källa för Nmap än att ange dem en och en på kommandoraden.



Till att börja med skapar du en enkel fil som innehåller en post per rad:



![nmap-image](assets/fr/31.webp)



fil som innehåller ett mål (värd eller nätverk) per rad



Därefter kan vi använda alla de Nmap-alternativ som vi har sett hittills och ange alternativet "-iL <path/file>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap kommer då att inkludera alla mål som finns i vår fil i sin sökning.



Om du vill vara säker på att alla dina mål tas med i beräkningen kan du använda alternativet "-sL -n". Nmap kommer då bara att tolka CIDR:erna och värdarna i filen och visa dem för dig, utan att skicka några paket över nätverket:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Detta säkerställer att listan över värddatorer som ska skannas är korrekt.



Ett sista viktigt tips som jag vill dela med mig av gäller **uteslutning av värd eller nätverk som en del av en skanning**. Detta behov av att utesluta en värd kan vara nödvändigt i ett antal fall, särskilt om vi vill vara säkra på att **en känslig komponent i informationssystemet inte störs eller störs av våra skanningar**.



Vanliga exempel på sådana behov är när ett företag äger utrustning för industri (PLC) eller sjukvård. Sådan utrustning är ibland dåligt utformad och inte alls avsedd att ta emot dåligt formaterade paket, eller för många av dem. Av uppenbara skäl som tillgänglighet eller affärsmässiga/mänskliga risker är det att föredra att utesluta dem från testning.



För att utesluta IP-adresser eller nätverk från vår sökning kan vi använda Nmaps alternativ "--exclude", till exempel:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



I det här exemplet skannar jag nätverket "192.168.1.0/24" men utesluter värden "192.168.1.140" som finns där. Inga paket kommer att skickas av Nmap till den här värden. Ett annat exempel med subnätsexkludering:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



På samma sätt skannar jag det stora nätverket "10.0.0.0/16", men nätverket "10.0.100.0/24" kommer inte att skannas. Återigen rekommenderar jag att du använder alternativet "-sL -n" för att få en mycket tydlig bild av vilka värdar som kommer att skannas och vilka som kommer att uteslutas från skanningen, särskilt om du arbetar i ett känsligt sammanhang.



### V. Upptäckt av nätverk och portskanning



Vi kan nu kombinera det vi har lärt oss i det här avsnittet med det vi lärde oss i det föregående avsnittet om alternativ för portskanning. Som standard har vi sett att Nmap kommer att skanna de 1000 mest frekventa portarna på varje aktiv värd som den upptäcker. Vi har sett hur vi kan förhindra detta beteende om vi inte vill ha det, men vi kan kontrollera det helt och hållet och till och med utöka det om det passar våra behov.



Följande kommando kontrollerar t.ex. om det finns en lyssnande tjänst på port TCP/22 på varje skannad värd:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap kommer först att utföra en nätverksupptäckt för att lista de aktiva värdarna och för var och en av dem kontrollera att en tjänst finns på port TCP/22.



På samma sätt kan vi utföra en fullständig genomsökning av alla TCP-portar på varje värd som upptäckts i nätverket "192.168.0.0/24", till exempel med undantag för värden "192.168.0.4":



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Det står dig fritt att kombinera alla de alternativ som vi har lärt oss hittills för att passa dina egna behov.



### VI. Slutsatser



I det här avsnittet har vi sett hur man använder Nmap för att kartlägga nätverket med hjälp av olika alternativ. Vi har nu en finjusterad förståelse av målen för våra skanningar, liksom Nmaps portskanningsbeteende och värdupptäcktsmetod. Och viktigast av allt, vi vet vad Nmaps standardbeteende och begränsningar är, och hur man använder dess huvudalternativ för att gå vidare.



I nästa avsnitt tittar vi på mekanismerna och alternativen för att upptäcka de versioner av tjänster och operativsystem som skannas av Nmap.




## 6 - Detektering av service- och operativsystemversioner med Nmap



### I. Presentation



I det här avsnittet lär vi oss hur man använder Nmap för att upptäcka och exakt detektera versionerna av tjänster och operativsystem som används av skannade värddatorer. Vi tar en detaljerad titt på hur Nmap utför denna uppgift, samt på verktygets begränsningar för att bättre förstå och tolka dess resultat.



Som vi har sett i tidigare avsnitt av den här handledningen kommer Nmap som standard inte att se efter vilken tjänst som är exponerad på de portar som den skannar och anser vara öppna. Så om du lyssnar på en webbtjänst på port TCP/22 kommer Nmap att fortsätta att rapportera den som öppen, men som en `SSH`-tjänst. Detta beror på att den använder en [databas] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) lokalt i ditt system för att leta efter en relation mellan en port/ett protokoll och namnet på en tjänst (filen `/etc/services/`).



I de flesta fall kommer [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) att ge dig rätt information, eftersom det är sällsynt i en produktionsmiljö att hitta sådana fall. De återstående fallen kommer dock att vara situationer där en klassisk tjänst ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, etc.) exponeras på en icke-klassisk port (t.ex. 2022 för en SSH-tjänst), i vilket fall Nmap inte kommer att hitta en matchning i sin lokala databas, eller en som inte stämmer överens med verkligheten, och du kommer att gå miste om viktig information.



Lyckligtvis erbjuder Nmap mycket exakta alternativ och mekanismer för att upptäcka vilken exakt tjänst som kan gömma sig bakom en öppen port. Det finns till och med en databas med frågor och signaturer för att identifiera exakta tekniker och versioner. Förutom tjänster kan Nmap också identifiera den teknik som används och dess version.



Det är vad vi ska titta på i det här avsnittet.



### II. Hur man upptäcker en teknik eller version



#### A. Påminnelse om hur man identifierar en teknik eller version



Identifiering av en teknik och en version innebär att man hämtar namnet på den tjänst, CMS, applikation eller programvara som lyssnar på den aktuella porten. En webbsida hanteras t.ex. av ett CMS (`WordPress`), körs av en webbtjänst (`Apache`, IIS, Nginx) och hostas av en server (Linux eller Windows). Men hur vet man vilken webbtjänst som körs?



Den klassiska metoden för att ta reda på denna information är _banner grabbing_, vilket helt enkelt innebär att man letar upp var tjänsten i fråga visar denna information och läser av data. Mycket ofta visar tjänsterna i sin standardkonfiguration eller bearbetning sitt namn och till och med sin version som det första svaret efter en anslutning.



![nmap-image](assets/fr/32.webp)



visa en version så snart en TCP-anslutning upprättas av en FTP-tjänst



Här ser vi att en enkel TCP-anslutning till denna tjänst via `telnet` resulterar i ett TCP-paket som innehåller dess teknik och version.



När du har fått en uppfattning om vilken typ av tjänst du har att göra med kan du också skicka specifika kommandon eller förfrågningar till den tjänsten för att få ut information från den. Dessa förfrågningar/kommandon kan också skickas i blindo (utan att vara säker på att det är rätt typ av tjänst), i hopp om att någon av dem ska framkalla ett svar från tjänsten i fråga.



I andra, mer avancerade fall, är det nödvändigt att skicka specifika paket för att orsaka en reaktion, t.ex. ett fel, som ger detaljerad information om den version eller teknik som används.



Som du kan föreställa dig kommer Nmap att använda alla dessa tekniker för att försöka identifiera den exakta typen av tjänst som finns på en port, samt namnet på dess teknik och version.



#### B. Förstå Nmap-prober och matchningar



För att utföra alla dessa kontroller på varje skannad port använder Nmap en lokal databas som uppdateras ofta (precis som den binära filen eller dess moduler). Detta är en textfil på flera tusen rader: `/usr/share/nmap/nmap-service-probes`.



Den här filen består av ett stort antal poster som alla är organiserade kring två huvudriktlinjer:





- `Probe`: detta är definitionen av det paket som Nmap kommer att skicka i ett försök att framkalla en reaktion från den tjänst som ska identifieras. Tänk på det som ett blint försök som _Hello? Guten Tag? Hallå? Um... Buenos Dias kanske?_. Så snart den utvalda tjänsten får en probe som den förstår (dvs. som talar rätt protokoll) kommer den att svara Nmap, som då får bekräftelse på vilken typ av tjänst det är.





- Match": detta är reguljära uttryck som Nmap tillämpar på det erhållna svaret. Om en HTTP GET-begäran har framkallat ett svar från tjänsten kommer den att tillämpa dussintals reguljära uttryck på detta svar för att identifiera förekomsten av till exempel ordet `Apache`, `Nginx`, `Microsoft IIS`, etc.




Det finns några andra direktiv för specifika fall, men de viktigaste för att förstå hur Nmap fungerar och anpassa dess användning är dessa. För att göra den här teoridelen mer konkret, här är ett exempel:



![nmap-image](assets/fr/33.webp)



exempel på en sond i Nmaps fil `/usr/share/nmap/nmap-service-probes`



På den första raden i detta exempel ser vi en lättförståelig Probe med namnet `GetRequest`. Detta är ett TCP-paket som innehåller en tom HTTP GET-begäran till webbtjänstens rot med HTTP/1.0, följt av en radmatning och en tom rad.



Raden `ports` talar om för Nmap till vilken port den här proben ska skickas. Detta gör att du kan prioritera tester och spara tid.



Slutligen har vi två exempel på `match`. Det första kategoriserar t.ex. den skannade webbtjänsten som `ajp13` om det reguljära uttrycket på den här raden matchar det mottagna tjänstesvaret.



För att hjälpa dig att förstå hur Probes kan se ut följer här en lista över några av de Probes som du hittar i den här filen (det finns 188 stycken när den här handledningen skrivs).



![nmap-image](assets/fr/34.webp)



exempel på flera prober som används av Nmap och som finns i filen `/usr/share/nmap/nmap-service-probes`._



De två första (kallade `NULL` och `GenericLines`) är av särskilt intresse här, eftersom de helt enkelt skickar ett tomt TCP-paket eller ett paket som innehåller en radbrytning. Servertjänster meddelar ofta sig själva exakt så snart en anslutning tas emot, utan någon specifik åtgärd, kommando eller begäran från klienten.



Här är fallet med en något mer komplex _match_:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Det exakta reguljära uttrycket finns här mellan `m|` och `|`, som avgränsar alla reguljära uttryck i den här filen. Ta dig tid att läsa hela det här exemplet. Du kommer att märka ett urval i det reguljära uttrycket: `([\d.]+)`, som används för att isolera en version. I det här exemplet definieras även andra Elements, t.ex. produktnamnet `p/nginx/`, den hämtade versionen `v/$1/` och CPE med versionen `cpe:/a:igor_sysoev:nginx:$1/`.



En CPE (Common Platform Enumeration) är ett standardiserat notationssystem som används för att identifiera och beskriva programvara och maskinvara. Formatet möjliggör effektivare hantering av sårbarheter och säkerhetskonfigurationer, och framför allt ett enhetligt sätt att representera dem, oavsett vilken produkt det handlar om. Här är två exempel på CPE: `cpe:/o:microsoft:windows_8.1:r1` och `cpe:/a:apache:http_server:2.4.35`



Här identifierar vi tydligt deras typer `o` för OS, `a` för applikation, leverantör, produkt och versioner.



Så i händelse av en _matchning_ med ett av dessa reguljära uttryck hämtar vi inte bara namnet på tjänsten utan också dess version och exakta CPE, vilket gör det lättare att hitta CVE:er som påverkar den här versionen. Du hittar den här informationen i Nmaps standardutdata, och du kommer att se att den är mycket användbar för andra ändamål som vi kommer att ta upp i några avsnitt.



Den exakta syntaxen för _matches_ och, mer allmänt, för direktiven i filen `/usr/share/nmap/nmap-service-probes` slutar inte där och kan verka ganska komplicerad om du inte är van vid att manipulera Nmap och dess resultat. Du bör dock åtminstone komma ihåg dess existens och allmänna funktion, vilket kommer att vara praktiskt senare när du vill förstå eller felsöka ett resultat, anpassa en skanning eller till och med bidra till Nmap-utvecklingen.



### III. Använda Nmap för att upptäcka versioner



Nu ska vi använda all denna komplexa _Probe_- och _Match_-mekanik via ett enkelt alternativ: `-sV`. Detta säger helt enkelt till Nmap: försök att ta reda på exakt vilka tjänster och versioner av portar som du har angett som öppna.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Här är ett komplett exempel på resultatet av ett sådant kommando:



![nmap-image](assets/fr/35.webp)



resultat av Nmaps versionsdetektering av applikationer som exponeras i nätverket



Här kan vi se att Nmap har lyckats identifiera alla versioner av nätverkstjänster som exponeras av det här målet, och visar denna information i en ny kolumn "VERSION". Det är möjligt att se ganska exakt information, till och med ner till operativsystemet, om denna information är en del av den återställda signaturen.



För att i detalj förstå vad som händer under en sårbarhetssökning kan vi använda alternativet `--version-trace`. Detta ger en vy i felsökningsläge som visar den _Probe_ som ledde till upptäckten:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Därför har vi mycket information att gå igenom. Försök att identifiera rader som börjar med `Service scan Hard match`. Du kommer då att se rader som dessa:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Vi kan tydligt se vilka _Probes_ som användes för att upptäcka tekniken och versionen (i det här fallet _Probes_ `NULL` och `GetRequest`), samt den information som hämtades.



### IV. Behärskning av tester och noggrannhet vid upptäckt



Vi ska nu gå tillbaka till ett direktiv i filen `/usr/share/nmap/nmap-service-probes` som vi inte tittade på tidigare:



![nmap-image](assets/fr/36.webp)



probes `rarity`-direktiv i filen `/usr/share/nmap/nmap-service-probes`._



Detta direktiv används för att ange hur sällsynt (dvs. prioritet/sannolikhet) en _Probe_ är. Denna notation från 1 till 9 gör att du kan kontrollera fullständigheten i den analys som utförs av Nmap när _Probes_ skickas. I Nmaps "notationssystem" ger en sällsynthet på 1 information i de allra flesta fall, medan en sällsynthet på 8 eller 9 representerar ett mycket speciellt fall, specifikt för en konfiguration eller tjänst som sällan förekommer.



För att vara tydligare kommer Nmap i ett standardfall att skicka de _Probes_ som har en sällsynthet från 1 till 7 till varje tjänst som ska identifieras. För att ge dig en bättre uppfattning om fördelningen av _Probes_ efter _rarity_, här är deras antal:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Det kan verka kontraintuitivt, det finns fler `rarity` 8 och 9 än resten. Detta beror just på att raritet 1-prober är generiska och fungerar i de flesta fall, oavsett tjänst (kom ihåg `NULL`-proben som helt enkelt skickar ett tomt TCP-paket). Medan de mer komplexa sonderna är nästan unika per tjänst.



Om vi manuellt vill hantera de prober som vi vill använda i vår versionsskanning kan vi använda alternativet `--version-intensity`. Här är två exempel:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Som avslutning på detta ämne, här är ett exempel på _Probe_ 9 och 8:



![nmap-image](assets/fr/37.webp)



exempel på Probe vid raritet 8 och 9 i filen `/usr/share/nmap/nmap-service-probes`._



Dessa två _Probes_ upptäcker Quake1- och Quake2-servrar (videospel). Intressant för den nostalgiska sidan, men troligen inte till någon större nytta i vardagen.



Beroende på dina behov av precision eller snabbhet, kom ihåg att denna "sällsynthetsprincip" finns och kan påverka resultatet.



### V. Använda Nmap för att upptäcka operativsystem



Vi ska nu titta på hur Nmap kan hjälpa oss att upptäcka operativsystemen för värdar som skannas och upptäcks i ett nätverk. För att göra detta använder du Nmaps alternativ `-O` (för `OS Scan`).



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Här är ett exempel på resultaten. Här säger Nmap att det förmodligen är ett Linux OS och erbjuder oss olika statistik om dess exakta version.



![nmap-image](assets/fr/38.webp)



detektering av sannolikheten för identifiering av ett operativsystem med Nmap



För att uppnå detta kommer Nmap att använda en mängd tekniker som fungerar på ett mycket liknande sätt som _Probes_ och _Matches_ för teknik- och versionsdetektering. Den största skillnaden är att Nmap kommer att använda parametrar på ganska "låg nivå" för ICMP, TCP, UDP och andra protokoll. Här är två testexempel för detektering av ett Microsoft Windows 11-operativsystem:



![nmap-image](assets/fr/39.webp)



exempel på tester som utförts av Nmap för att upptäcka ett Windows 11 OS



Låt oss inse det, dessa tester är mycket svåra att tolka, och vi kommer inte att försöka förstå dem på djupet inom ramen för en inledande Nmap-handledning. Om du vill gräva djupare i ämnet finns filen som innehåller denna information i `/usr/share/nmap/nmap-os-db`.



Du måste dock vara medveten om att OS-detektering är mer en sannolikhet som fastställs av Nmap än en säkerhet.



### VI. Slutsatser



I det här avsnittet har vi lärt oss hur man använder Nmaps alternativ för att upptäcka teknik, versioner och operativsystem för skannade värdar och tjänster. Vi har nu en god förståelse för hur Nmap går tillväga för att få den här informationen på distans. Vi har också gått igenom alternativen för att hantera ordrikedom och testnoggrannhet, samt verktygets begränsningar i dessa ämnen.



I nästa avsnitt lär vi oss hur vi använder Nmaps NSE-skript för att utföra en säkerhetsanalys av vårt informationssystem. Ta dig tid att läsa om de senaste avsnitten om du behöver, och tveka inte att öva och gräva i verktygets tarmar själv för att bättre behärska det vi har lärt oss hittills.




## 7 - Säkerhetsanalys: upptäcka sårbarheter



### I. Presentation



I det här avsnittet lär vi oss att använda nätverksskanningsverktyget Nmap för att upptäcka och analysera sårbarheter i de mål som vi skannar. Vi kommer särskilt att titta på de olika alternativ som finns för att utföra denna uppgift och studera gränserna för verktygets kapacitet för att bättre förstå och tolka dess resultat.



I det här första avsnittet tar vi en titt på Nmaps sårbarhetsskanner och ser hur man använder de grundläggande alternativen för sårbarhetsdetektering. I de följande avsnitten tittar vi närmare på hur den här funktionen fungerar och hur den kan anpassas.



### II. Använda Nmap för att upptäcka sårbarheter



Vi vill nu använda nätverksskannern Nmap för att upptäcka sårbarheter i tjänsterna och systemen i vårt informationssystem. Detta innebär att Nmap, förutom att upptäcka aktiva värdar, räkna upp exponerade tjänster och upptäcka versioner och tekniker, kommer att leta efter sårbarheter.



För att uppnå detta förlitar sig Nmap på NSE-skript (_Nmap Scripting Engine_), som kan ses som moduler som möjliggör en granulär testmetod.



Med rätt alternativ ber vi Nmap att använda sina olika NSE-skript på varje tjänst som upptäcks, vilket gör att vi kan upptäcka:





- Konfigurationsfel ;





- Ytterligare och mer avancerad version och OS-upptäckter ;





- Kända sårbarheter (CVE) ;





- Svaga identifierare ;





- Karakteristiska Elements för en infektion av skadlig kod ;





- Möjligheter att neka tjänster ;





- Och så vidare.




Som du kan se utökar NSE-skript avsevärt Nmaps kapacitet när det gäller de nätverksoperationer som den kan utföra. Och detta för att utföra mycket mer avancerade uppgifter än någonsin tidigare. Den goda nyheten är att dessa funktioner, som vanligt, kan användas helt enkelt via ett alternativ och i ett standardkontext. Detta är vad vi kommer att se härnäst.



### III. Exempel på en sårbarhetsanalys



NSE-skript kan användas när du använder Nmap för att skanna en enda port på en värd, alla tjänster på den värden eller alla tjänster som upptäcks i flera nätverk. Vi kan därför använda de alternativ som vi kommer att se i alla de sammanhang som vi har studerat hittills.



För att aktivera sårbarhetssökning via en Nmap-sökning måste vi använda alternativet `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Kom ihåg att som standard, om du inte anger något, kommer Nmap bara att skanna de 1000 vanligaste portarna. Den kommer inte att upptäcka sårbarheter på de mer exotiska portar som dina mål kan exponera.



Innan du använder denna funktionalitet på ett produktionsinformationssystem, uppmanar jag dig att fortsätta läsa handledningen. I de följande avsnitten tittar vi på hur du bättre kan kontrollera effekterna och typerna av tester som kommer att köras.



Genom att återanvända det vi har lärt oss tidigare kan vi till exempel vara mer omfattande och skanna alla TCP-portar på ett mål:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Här är resultatet av en Nmap-sökning med hjälp av NSE-skript:



![nmap-image](assets/fr/40.webp)



exempel på resultatet av en sårbarhetssökning på en värd via Nmap._



Här visas ytterligare information som är av intresse i samband med en sårbarhetsanalys:





- FTP-tjänsten kan nås anonymt och skyddas inte av autentisering. NSE-skriptet som ansvarar för den här verifieringen berättar det för oss och visar till och med en del av FTP-tjänstens trädstruktur. Här ser vi att vi har tillgång till katalogen `C` i Windows-systemet!





- Det NSE-skript som ansvarar för avancerad hämtning av webbtjänster visar sidans titel, vilket ger oss en bättre uppfattning om vad webbtjänsten är värd för.





- Vi har också en minianalys av SMB-tjänstens konfiguration (skripten `smb2-time`, `smb-security-mode` och `smb2-security-mode`). Informationen visas på ett lite annorlunda sätt efter resultatet av nätverksskanningen för att göra den mer lättläst. I synnerhet visar denna information att det saknas SMB Exchange-signaturer. Denna svaghet i konfigurationen gör att målet kan användas i en SMB Relay-attack, en anmärkningsvärd säkerhetsbrist som ofta utnyttjas i intrångs-/cyberattacktester.




Naturligtvis är detta bara ett exempel. Nmap har NSE-skript för många tjänster, inriktade på ett brett spektrum av sårbarheter. Vi kommer att titta närmare på dessa möjligheter i nästa avsnitt.



Som avslutning på denna introduktion till sårbarhetsscanning följer här ett komplett kommando för nätverksupptäckt, scanning av TCP-portar, versions- och sårbarhetsdetektering:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Här är ett kommando som börjar se ut som mer realistiska Nmap-användningsfall!



### IV. Förstå Nmaps begränsningar när det gäller sårbarhetsskanning



Låt oss vara tydliga: Nmap kan inte utföra ett fullständigt penetrationstest av ditt informationssystem eller simulera en Red Team-operation. Det har flera begränsningar som du måste vara medveten om om du inte ska få en falsk känsla av säkerhet:





- Begränsad täckning**: även om Nmaps NSE-skript är kraftfulla kan deras testtäckning vara begränsad jämfört med andra specialiserade verktyg för upptäckt av sårbarheter. Vissa sårbarheter kanske inte täcks av de NSE-skript som finns tillgängliga, t.ex. Active Directory-sårbarheter, exponering av känsliga data eller mer avancerade fall av sårbara webbapplikationer.





- Sårbarhetens komplexitet**: vissa typer av sårbarheter kan vara svåra att upptäcka med hjälp av NSE-skript på grund av deras komplexitet. Till exempel kan sårbarheter som kräver komplex interaktion med en fjärrtjänst kanske inte upptäckas effektivt av Nmap (som i fallet med överdrivna behörigheter i en fildelning eller ett behörighetskontrollfel i en webbapplikation).





- Passiv detektering**: Nmap fokuserar främst på aktiva skanningar för att upptäcka sårbarheter, vilket innebär att den kanske inte effektivt upptäcker potentiella sårbarheter utan att upprätta en aktiv anslutning till målvärdarna. Sårbarheter som inte manifesterar sig under en aktiv skanning kan därför missas (som i fallet med en kodinjektion i en webbapplikation).





- Beroende av uppdateringar**: Nmaps [databas](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) med NSE-skript utvecklas ständigt, men det kan gå en tid mellan upptäckten av en ny sårbarhet och tillägget av ett motsvarande skript till Nmap. Därför kanske Nmap inte alltid är uppdaterat med de senaste sårbarheterna.





- Falska positiva och falska negativa resultat**: Som med alla säkerhetsverktyg kan Nmaps NSE-skript ge falska positiva resultat (falska varningar om sårbarheter) eller falska negativa resultat (verkliga sårbarheter som inte upptäcks). Detta är något man bör ha i åtanke när man analyserar Nmap-resultat.




Så det är viktigt att förstå vad Nmap gör och inte gör, och likaså att veta hur man tolkar dess resultat. I synnerhet har vi sett under hela denna handledning att standardalternativ kan leda till att vi missar viktiga Elements som kan avslöjas med noggrann användning.



Oavsett om du är nätverkssystemadministratör, säkerhetsingenjör eller CISO kan du med hjälp av Nmap få en överblick över säkerhetsstatusen i ett informationssystem. Det här är ett viktigt första steg för att säkra ett system, som kan utföras regelbundet av IT-teamet. Det bör dock inte ersätta ingripanden och råd från [cybersäkerhets]experter (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), som kan avslöja svagheter på ett mycket mer omfattande sätt än Nmap.



### V. Slutsats



I detta första avsnitt av modul 3 har vi introducerat sårbarhetssökning via Nmap. Vi vet nu hur man använder huvudalternativet för att utföra den här uppgiften, men vi känner också till gränserna för övningen. I nästa avsnitt ska vi titta närmare på den här funktionaliteten och använda NSE-skript för att tiofaldiga Nmaps kraft.



## 8 - Använda Nmaps NSE-skript



### I. Presentation



I det här avsnittet tar vi en djupgående titt på NSE-skript (_Nmap Scripting Engine_). Vi tittar särskilt på varför de är en av de stora styrkorna med det här verktyget, hur de fungerar och hur man bläddrar bland och använder de många befintliga skripten.



Detta avsnitt är en fortsättning på den föregående handledningen, där vi lärde oss att använda Nmaps funktioner för sårbarhetssökning på ett grundläggande sätt. Vi kommer nu att titta närmare på hur [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) fungerar i detta avseende, så att vi återigen kan utföra mer exakta och kontrollerade skanningar.



### II. Konceptet med Nmap NSE-skript



Nmaps NSE-skript gör att du kan utöka dess funktioner på ett mycket flexibelt sätt. De är skrivna i LUA, ett skriptspråk som är lättare att hantera och komma åt än C eller C# som används av Nmap. Fördelen med att använda ett LUA-skript med Nmap i stället för ett fristående verktyg är att vi kan dra nytta av Nmaps exekveringshastighet och standardfunktioner (upptäckt av värd, port och version etc.).



Skripten är indelade i kategorier och ett och samma manus kan tillhöra flera kategorier:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Tekniskt sett anges de kategorier som ett manus tillhör direkt i dess kod.



![nmap-image](assets/fr/41.webp)



nSE-skriptkategorier `ftp-anon`._



Detta exempel visar en del av koden för NSE-skriptet `ftp-anon.nse`, vars exekvering vi såg i föregående avsnitt.



### III. Förteckning över befintliga NSE-skript



Som standard finns Nmaps NSE-skript i katalogen `/usr/share/nmap/scripts/`, utan någon specifik trädstruktur eller hierarki. Här följer en översikt över innehållet i den här katalogen:



![nmap-image](assets/fr/42.webp)



extraherar innehållet i katalogen `/usr/share/nmap/scripts/` som innehåller NSE-skript._



Den här katalogen innehåller över 5 000 NSE-skript. I de flesta fall innehåller den första delen av skriptnamnet det protokoll eller den kategori som det tillhör. Detta gör att vi kan sortera listan, till exempel om vi vill lista alla skript som riktar sig till FTP-tjänsten:



![nmap-image](assets/fr/43.webp)



lista över NSE Nmap-skript med namn som börjar med `ftp-`._



Nmap erbjuder egentligen inte något alternativ för att bläddra bland och lista sina NSE-skript; du kan använda kommandot `--script-help` följt av namnet på en kategori eller ett ord:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Utdata blir dock namnet på varje skript och dess beskrivning, vilket inte är optimalt om sökningen ger flera dussin skript:



![nmap-image](assets/fr/44.webp)



resultatet av att använda Nmaps `--script-help`-kommando



Enligt min mening är den mest effektiva metoden att använda de klassiska Linux-kommandona i katalogen `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Bläddra gärna igenom koden för de moduler som talar till dig för att bättre förstå hur ett NSE-skript fungerar.



### IV. Använda Nmaps NSE-skript



Nu ska vi lära oss att utföra sårbarhetsskanningar genom att noggrant välja ut de NSE-skript som vi är intresserade av.



#### A. Välj manus per kategori



Till att börja med kan vi välja att köra alla skript som hör till en viss kategori. Vi måste ange denna kategori eller dessa kategorier till Nmap med argumentet `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Det första kommandot är motsvarigheten till kommandot `nmap -sC`. Som standard kommer Nmap att välja skript i kategorin `default`, men det är bara för argumentets skull. Nästa kommando kommer till exempel att använda alla skript i kategorin `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Som vi har sett gör vissa kategorier det möjligt för oss att snabbt identifiera vad de relaterade NSE-skript gör (`discovery`, `vuln`, `exploit`), medan andra definierar risknivån, detekteringen eller stabiliteten för det utförda testet. Om vi befinner oss i ett känsligt sammanhang och inte har en bra uppfattning om de olika åtgärder som utförs av vårt skriptval kan vi välja att kombinera urvalen för att bara välja de skript som finns i kategorierna `discovery` och `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Om du absolut och uttryckligen vill utesluta skript från kategorierna `dos` och `intrusive` kan du använda följande notation:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Observera att om man specificerar uteslutningsvillkor enligt ovan kommer det att leda till att alla andra kategorier som inte uttryckligen utesluts används. För att vara mer rättvis kan vi till exempel ange:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Här följer några exempel på hur du kan hantera NSE-skript per kategori, särskilt när du använder Nmap för sårbarhetsanalys i verkliga sammanhang.



#### B. Välj skript som en enhet



Vi kan också välja att utföra ett enda specifikt test under en analys, ett test som motsvarar ett NSE-skript. För att göra detta måste vi ange namnet på skriptet i parametern `-script <name>`. Vi tar skriptet `ftp-anon.nse` som exempel:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Vi får då ett mycket exakt resultat:



![nmap-image](assets/fr/45.webp)



resultatet av att använda NSE-skriptet `ftp-anon` på en FTP-port via Nmap._



Vi ser resultatet av att köra skriptet `ftp-anon` på port 21, och ingen annan port, eftersom vi angav alternativet `-p 21`. Vi kunde också ha utfört en grundläggande portskanning och kört NSE-skriptet `ftp-anon` endast på de FTP-tjänster som upptäcktes:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Nmap skulle alltså ha utfört detta anonyma anslutningstest även om den hade hittat en FTP-tjänst på en annan port.



Om du vill ha en kort beskrivning av vad ett NSE-skript gör kan du använda alternativet `--script-help` som nämns ovan:



![nmap-image](assets/fr/46.webp)



hjälp visa resultat för NSE-skript `sshv1`._



Kort sagt, vi kan återigen återanvända alla de alternativ, tjänster, versioner och tekniker för nätverksupptäckt som vi har använt hittills!



#### C. Hantering av skriptargument



När du använder Nmap kommer du att stöta på vissa NSE-skript som kräver inmatningsargument för att fungera korrekt. Vi ska nu titta på hur man skickar argument till dessa skript via Nmaps alternativ.



Som exempel kan vi ta skriptet `ssh-brute`, som gör att du kan utföra en brute force-attack på SSH-tjänsten.



En klassisk brute force-attack består i att testa flera lösenord (ibland miljontals) i ett försök att autentisera ett visst konto. Genom att försöka med så många lösenord satsar angriparen på sannolikheten att användaren har använt ett svagt lösenord i den lösenordsordbok som används för attacken.



Det här skriptet har "standardalternativ" som vi kan anpassa så att de passar vårt sammanhang. I samband med denna attack kan vi till exempel förse Nmap med listan över användare och lösenordsordlistan som ska användas. Så vitt jag vet är det inte möjligt att enkelt lista de argument som krävs för ett skript, så det mest pålitliga sättet är att besöka den officiella Nmap-webbplatsen. En direktlänk till dokumentationen för ett NSE-skript kan erhållas som svar på alternativet `--script-help`:



![nmap-image](assets/fr/47.webp)







Genom att klicka på den angivna länken kommer vi till denna webbsida på webbplatsen [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



lista över argument som kan skickas till Nmaps NSE-skript `ssh-brute`



Här har vi en tydlig bild av de argument som kan användas, varav de viktigaste i vårt sammanhang är `passdb` (fil som innehåller en lista med lösenord) och `userdb` (fil som innehåller en lista med användare). Dokumentationen här hänvisar till interna Nmap-bibliotek, eftersom dessa brute force-mekanismer och tillhörande alternativ är gemensamma för att användas enhetligt i flera skript (`ssh-brute`, `mysql-brute`, `mssql-brute`, etc.) och därför kommer att ha mer eller mindre samma argument:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Som du kan se i det sista kommandot kan vi ange de nödvändiga argumenten till ett Nmap-skript med hjälp av alternativet `--scripts-args key=value,key=value`. Här är ett möjligt resultat av Nmap-utdata när du utför en SSH-brute force via NSE-skriptet `ssh-brute`:



![nmap-image](assets/fr/49.webp)



resultatet av SSH-bruteforce-körning via Nmap._



Som du kan se inleds informationen som genereras av NSE-skript med `NSE: [skriptnamn]` i den interaktiva utmatningen (terminalutmatningen), vilket gör den lättare att hitta. Inom den vanliga visningen av Nmap-resultat har vi helt enkelt en sammanfattning som anger om svaga identifierare har upptäckts eller inte (inklusive lösenord, kom ihåg).



För att gå ett steg längre och påminna dig om att allt detta kan användas utöver alla de alternativ vi redan har tittat på, här är ett kommando som kommer att upptäcka nätverket `10.10.10.0/24`, skanna de 2000 mest frekventa TCP-portarna och köra en anonym åtkomstsökning på FTP-tjänster och en brute force-kampanj på SSH-tjänster:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Detta är bara ett exempel på de många tillgängliga skripten och deras alternativ. Men nu har vi fått en bättre uppfattning om hur man hanterar NSE-skript, om de kräver argument och hur man skickar dessa argument till Nmap.



### V. Slutsats



I det här avsnittet har vi lärt oss hur man använder Nmaps NSE-skript för att utföra olika uppgifter. Jag uppmanar dig att ta dig tid att upptäcka de olika kategorierna av skript och skripten själva, för att se hur många tester de kan automatisera.



I flera avsnitt nu har vi samlat på oss mer eller mindre avancerade alternativ för upptäckt, skanning och uppräkning. Vid det här laget bör du vara medveten om att Nmaps utdata och resultatvisning börjar bli ganska omfattande, ibland till och med för mångordig för vår terminal. I nästa avsnitt ska vi lära oss hur vi kan hantera denna utdata, särskilt genom att lagra den i filer i olika format.






## 9 - Hantering av utdata från Nmap




### I. Presentation



I det här avsnittet tittar vi på utdata som produceras av Nmap, och i synnerhet på de olika alternativen för att formatera utdata. Vi kommer att se att Nmap kan producera flera utdataformat för att passa olika behov, och att detta också är en av de stora styrkorna med detta verktyg.



Som standard erbjuder Nmap en detaljerad vy över resultaten av de skanningar och tester som utförs. Detta inkluderar värdar och tjänster som skannats, de som upptäckts som tillgängliga, specifikationerna för öppna portar, deras status och version. Dessutom är detaljer om NSE-skript också tillgängliga i terminalutmatningen. Dessa utdata kan dock snabbt bli omfattande, även med tydlig formatering av informationen, vilket kan göra det svårt att hitta exakt information i resultaten.



### II. Behärska Nmap-utdataformat



#### A. Spara skanningsresultat i en textfil



För att göra saker och ting enklare gör [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) det mycket enkelt att spara utdata i en textfil. Detta kan vara användbart för arkivering, jämförelse med andra tester, men också för att bläddra i utdata med specialiserade ordbehandlingsverktyg eller skriptspråk, som Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, etc. För att lagra Nmaps standardutdata i en textfil kan vi använda alternativet `-oN <filnamn>` (N:et i "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Det är ingen överraskning, eftersom Nmap kommer att visa sin vanliga standardutdata i vår terminal, men också i den angivna filen.



#### B. generate Nmap-utdata i komprimerat format



Det finns också ett andra utdataformat i "text"-stilen som lätt kan tolkas av en människa: "greppable"-formatet.



Detta format skapades för att ge en "kondenserad" bild av Nmap-utdata, strukturerad på ett sådant sätt att det underlättar bearbetning med verktyg som `grep`. Låt oss titta på ett exempel på denna typ av utdata:



![nmap-image](assets/fr/50.webp)



nmap nätverkssökning och utdata i "greppbart" format._



Här har jag utfört en nätverksupptäckt samt en portskanning och en analys av tekniker och versioner i ett /24-nätverk och sedan lagrat utdata i en fil i "greppbart" format. Jag får en fil som innehåller 2 rader per aktiv host:





- Den första raden berättar för mig att den och den värden är _Upp_;





- En andra rad berättar vilka portar som har skannats, deras status och den teknik- och versionsinformation som hämtats i ett mycket specifikt format: `<port>/<status/<protokoll>//<tjänst>//<version>/,`




Denna formatering med en fast avgränsare möjliggör snabb bearbetning med ordbehandlingsverktyg som `grep`, eller skript- och programmeringsspråk. Med följande kommando kan jag till exempel enkelt hämta information om värden `10.10.10.5` i händelse av en enorm skanning utförd av Nmap vars utdata skulle vara svår att bläddra i:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Omvänt kan jag också enkelt lista alla värdar som har port 21 öppen, eftersom portar och IP finns på samma rad:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



För att generate ska kunna visa sådana utdata måste vi använda alternativet `-oG <filnamn>.gnmap` (G:et i "grep"). Av gammal vana använder jag tillägget `.gnmap` här för en sådan fil, men du får gärna använda det du vill:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Det här formatet kan användas för en mängd olika ändamål och är särskilt användbart för snabb skriptning/sortering. Ändå tenderar det att överges till förmån för det format som vi ska titta på härnäst.



observera: Greppbarhetsformatet `-oG` har officiellt utgått sedan Nmap 7.90. Det kan fortfarande användas för kompatibilitetsändamål. Det kan fortfarande användas för kompatibilitetsändamål, men det rekommenderas att du använder XML- eller normalformatet för all utveckling eller automatiserad parsning



#### C. XML-format för Nmap-utdata



Det sista formatet som är värt att nämna i denna handledning är XML. Till skillnad från de två föregående formaten är detta format inte utformat för att läsas av människor, utan av andra verktyg eller skript.



XML (_eXtensible Markup Language_) är ett märkspråk som används för att lagra och transportera data och som erbjuder en hierarkisk struktur via anpassade taggar.



Inom Nmap används XML-formatet för generate detaljerade rapporter om de skanningar som utförts, inklusive information om värdar, portar och sårbarheter som upptäckts, samt ytterligare information som inte visas i standardutdata från Nmap.



För att generate en utdatafil i XML-format måste vi använda alternativet `-oX` ("O" från "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Resultatet är Nmaps standardutdata i din terminal samt en fil i XML-format i din aktuella katalog.



XML-formatet är naturligtvis inte utformat för att läsas och tolkas av människor. Men om du vill göra skript eller automatiserad analys av det här formatet av Nmap-utdata måste du ändå ha en uppfattning om de taggar och den struktur som används. Här är till exempel en del av innehållet i den XML-fil som skapats av Nmap, som visar skanningsresultaten för 1 värd:



![nmap-image](assets/fr/51.webp)



exempel på en XML-post för 1 värd under en Nmap-sökning



Det finns mycket information här, och vi är särskilt intresserade av de två öppna portarna:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Vi förstår att detta format kommer att underlätta den automatiska analysen av resultaten, eftersom varje del av informationen är prydligt ordnad i en dedikerad, namngiven tagg eller attribut. I synnerhet hittar vi en del information som vi inte har stött på tidigare: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Vi nämnde kort CPE i avsnitt 2 i modul 2, och den här informationen bestäms i matchningar under versionsdetektering. Nmap använder sina mekanismer för tjänste-, teknik- och versionsdetektering för att hitta den associerade CPE:n.



Detta gör att vi kan återanvända denna information med de databaser och applikationer som använder den. Jag tänker särskilt på NVD-databasen, som refererar till CVE. För varje CVE innehåller den de CPE:er som påverkas av sårbarheten. Här är ett exempel på en CVE som rör `a:microsoft:internet_information_services:7.5` från NVD-databasen:



![nmap-image](assets/fr/52.webp)



förekomst av en CPE i uppgifterna om en CVE i NVD-databasen



Vi har nu en bättre förståelse för fördelarna med detta format, som erbjuder en mycket tydlig informationsstruktur och innehåller alla data som samlas in eller bearbetas av Nmap.



Som en reflex sparar jag systematiskt mina Nmap-sökningar i alla tre formaten på en gång. Detta möjliggörs av alternativet `-oA <namn>` ("A" för "All"), som skapar en fil med namnet `<namn>.nmap`, en fil med namnet `<namn>.xml` och en fil med namnet `<namn>.gnmap`. På det här sättet är jag säker på att jag inte kommer att få slut på något när jag behöver gå tillbaka till resultaten.



Med dessa tre format bör du ha allt du behöver för att spara och så småningom bearbeta Nmap-resultat på ett automatiserat sätt. Vi kommer att använda XML-formatet igen i nästa avsnitt, när vi tittar på hur vi använder Nmap med andra säkerhetsverktyg.



#### III. Generera en HTML-rapport från en Nmap-sökning



XML-formatet erbjuder många möjligheter, inte minst att fungera som grund för att generera en rapport i HTML-format, som blir mer visuellt tilltalande att bläddra i.



För att omvandla en Nmap-fil i XML-format till en webbsida använder vi verktyget `xsltproc`, som vi först måste installera:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



När verktyget har installerats behöver du bara förse det med XML-filen som ska konverteras och namnet på HTML-rapporten som ska genereras:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Som ett resultat kommer vi att ha hela vår skanning snyggt strukturerad, med till och med några färger och klickbara länkar i innehållsförteckningen!



![nmap-image](assets/fr/53.webp)



utdrag från en Nmap-scanningsrapport i HTML-format som genererats av xsltproc._



I stort sett innehåller den XML-fil som sparas av Nmap en referens till en annan fil i XSL-format:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Konvertering till HTML är därför en funktion som tillhandahålls och underlättas av Nmap, där `xsltproc` är ett vanligt och erkänt verktyg för att utföra denna uppgift (som inte ingår i Nmaps verktygssvit).



XSLT (_Extensible Stylesheet Language Transformations_) är en delmängd av XSL som gör att XML-data kan visas på en webbsida och "omvandlas", parallellt med XSL-stilar, till läsbar, formaterad information i HTML-format.



källa: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Informationsnivån i rapporten motsvarar den i Nmaps XML-format och är högre än den i terminalens standardutdata (_interactive output_).



### IV. Hantering av Nmaps ordrikhetsnivå



Vi ska nu ta en titt på några alternativ för Debugger Nmap eller för att följa dess framsteg.



Det första alternativet vi bör nämna är alternativet `-v`, som ökar Nmaps ordrikedom. Här är ett exempel:



![nmap-image](assets/fr/54.webp)



nmapps verbala utdata med hjälp av alternativet `-v`._



Vid en skanning som riktar in sig på många värdar och portar blir terminalutmatningen svår att utnyttja på grund av den mängd information som visas. Av denna anledning bör detta alternativ användas i kombination med de tidigare nämnda alternativen, som gör att du kan lagra Nmaps standardutdata i en fil. Information som är relaterad till användningen av verbosity kommer inte att inkluderas i denna utdatafil. Som du kan se i exemplet ovan kan du med hjälp av denna verbositet följa Nmaps åtgärder och upptäckter på ett tydligt och direkt sätt. Vid längre skanningar där datavisningen kan dröja, undviker du att vara blind för Nmaps aktuella aktivitet och vet att saker och ting går framåt och i vilken takt. Om du vill öka ordrikedomen ytterligare en nivå kan du använda alternativet `-vv`.



För att ytterligare spåra Nmaps aktivitet under dess skanning kan du använda alternativet `--packet-trace`. Med alternativet `-v` får vi en live-logg över alla öppna portar som upptäckts av Nmap, medan vi med det här alternativet får en logglinje för varje paket som skickas till en port. Detta ger naturligtvis en mycket utförlig utdata, men möjliggör detaljerad övervakning av Nmaps aktivitet, här är ett exempel:



![nmap-image](assets/fr/55.webp)



detaljerad övervakning av Nmap-aktivitet via `--packet-trace`._



Denna information kommer inte heller att registreras i den utdatafil som produceras av Nmap om alternativen `-oN`, `-oG`, `-oX` eller `-oA` används.



Slutligen erbjuder Nmap också två felsökningsalternativ: `-d` och `-dd`. Dessa alternativ fungerar på samma sätt som `-v`, men lägger till ytterligare teknisk information, t.ex. en sammanfattning av de tekniska parametrarna i början av skanningen:



![nmap-image](assets/fr/56.webp)



tidsinställningsalternativ visas i Nmaps felsökningsvy



I de kommande avsnitten kommer vi att titta närmare på alternativen för "Timing" och varför det är viktigt att känna till dem.



Slutligen, om du bara vill ha en grundläggande, syntetisk översikt över hur Nmap-sökningen fortskrider, kan du använda alternativet `--stats-every 5s`. "5s" betyder här 5 sekunder och kan ändras för att passa dina behov. Detta är den frekvens med vilken vi kommer att få feedback från Nmap om dess framsteg:



![nmap-image](assets/fr/57.webp)



information som visas av Nmaps alternativ `--stats-every`



I synnerhet kan vi få en procentandel av framstegen, samt en indikation på vilken fas den befinner sig i: host discovery-fas via [ping] (https://www.it-connect.fr/le-ping-pour-les-debutants/), discovery-fas av exponerade TCP-portar, etc. Denna information kan också erhållas i terminalutmatningen genom att trycka på "Enter" under en skanning.



Nmap är dock inte särskilt bra på att uppskatta hur lång tid en uppgift kommer att ta, inte minst eftersom det inte vet i förväg hur många värdar och tjänster det måste skanna.



### V. Slutsats



I det här avsnittet har vi tittat på ett antal alternativ för att spara Nmap-scanningsresultat i olika filformat. Detta kommer att vara mycket praktiskt, eftersom skanningsresultat i realistiska sammanhang kan ta upp hundratals eller till och med tusentals rader! Vi har också sett hur man ökar Nmaps ordrikhetsnivå för felsökning eller för att få en lägesrapport om skanningen.



XML-formatet kommer att vara särskilt användbart i nästa avsnitt, där vi tittar på några verktyg som kan arbeta med Nmap-resultat.




## 10 - Använda Nmap tillsammans med andra säkerhetsverktyg



### I. Presentation



I det här avsnittet tar vi en titt på några av de klassiska användningsområdena för Nmap tillsammans med andra säkerhetsverktyg med fri och öppen källkod. I synnerhet kommer vi att använda det vi har lärt oss i de tidigare avsnitten för att ytterligare förbättra Nmaps kraft och effektivitet.



Möjligheten att spara Nmap-scanningsresultat i XML gör att data blir kompatibla med en mängd andra verktyg. Eftersom nästan alla programmerings- och skriptspråk idag har bibliotek som kan tolka XML, blir det mycket enklare att bearbeta dessa data. Ett antal verktyg, särskilt de som är inriktade på offensiv säkerhet, har funktioner för att bearbeta XML-formatet som genereras av Nmap. Låt oss ta en närmare titt.



Jag kommer att nämna några offensiva verktyg utan att i detalj gå in på hur de används eller hur de fungerar. Jag förutsätter att läsaren känner till deras grundläggande användning och att de redan är i drift. Detta avsnitt kommer att vara av särskilt intresse för yrkesverksamma inom [cybersäkerhet] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), personer under utbildning eller de som har beslutat sig för att fördjupa sig i ämnet.



### II. Importera Nmap-resultat till Metasploit



Det första verktyget vi ska titta på för att återanvända Nmap-data i offensiv säkerhets- och sårbarhetsforskning är Metasploit.



Metasploit är ett ramverk för exploateringar och attacker. Det är en gratis lösning och ett erkänt verktyg som innehåller ett stort antal moduler skrivna i Ruby eller Python. Dessa gör det möjligt att utnyttja sårbarheter, utföra attacker, generera bakdörrar, hantera callbacks (C&C eller kommunikations- och kontrollfunktioner) och använda allt på ett enhetligt sätt.



I synnerhet kan detta välkända och allmänt använda operativsystem arbeta med en postgreSQL [databas] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) där värdar, portar, tjänster, autentiseringsinformation och mer lagras.





- Officiell Metasploit-dokumentation: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Det är här Nmap och dess utdata kommer in i bilden, eftersom XML-formatet för Nmap-utdata enkelt kan importeras till Metasploits databas för att fylla på dess databas med värdar och tjänster, som sedan snabbt kan utses till mål för den ena eller andra attacken.



Väl i mitt interaktiva Metasploit-skal börjar jag med att skapa en arbetsyta, ett slags utrymme som är specifikt för min miljö för dagen:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



När min arbetsyta har skapats måste vi validera att kommunikationen med databasen fungerar:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Slutligen kan vi använda Metasploit `db_import`-kommandot för att importera vår Nmap-sökning i XML-format:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Så här ser resultatet ut när alla dessa kommandon har utförts:



![nmap-image](assets/fr/58.webp)



importera en Nmap-scanning i XML-format till Metasploit-databasen



Här kan du se att varje värd importeras tillsammans med sina tjänster. Dessa data kan sedan visas via kommandot `services` eller `services -p <port>` för en specifik tjänst:



![nmap-image](assets/fr/59.webp)



lista över tjänster som importeras från XML-filen till Metasploit-databasen



Slutligen kan vi snabbt och enkelt återanvända dessa data i en modul tack vare alternativet `-R`, som kommer att "konvertera" listan över tjänster som erhålls som indata för direktivet `RHOSTS`, som används för att ange målen för den attack som ska utföras. Här är ett exempel med modulen `ssh_login`, som gör att du kan utföra en brute force-attack på [SSH]-tjänster (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



använda alternativet `services -R` för att importera de tjänster som angetts som mål för attacken



Detta är bara ett litet exempel på vad som kan göras med Nmap-data i Metasploit, men det ger dig en liten uppfattning om hur snabbt och enkelt denna information kan återanvändas som en del av ett penetrationstest, sårbarhetsskanning eller cyberattack. Det är också värt att nämna att Nmap kan köras direkt från Metasploit för att importera resultaten till databasen (kommando `db_nmap`), ett annat intressant ämne att täcka!



### III. Använda Nmap med Aquatones webbskanner



Det andra verktyget som jag vill presentera i det här avsnittet om att återanvända Nmap-resultat för offensiv säkerhets- och sårbarhetsanalys är Aquatone.



Aquatone är en webbskanner som är utformad för att effektivt utforska webbapplikationer i ett nätverk. Den erbjuder avancerade funktioner för upptäckt av webbtjänster, identifiering av subdomäner, portanalys och fingeravtryck av webbapplikationer. Allt presenteras tydligt och koncist i HTML-, JSON- och textrapporter för enkel analys av webbsäkerhet.



Precis som med Metasploit kan Aquatone direkt bearbeta Nmaps XML-format och använda det som ett mål för skanning. I synnerhet kan det bara extrahera de värdar och tjänster som är av intresse (webbtjänster) från alla data som en Nmap-rapport kan innehålla.





- Verktygslänk: [Github - Michenriksen/aquatone] (https://github.com/michenriksen/aquatone)




För att använda Nmaps XML-utdata med Aquatone skickar du helt enkelt XML-filen i en pipe som kommer att användas av Aquatone. Här är ett exempel:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Aquatone utför normalt portdiscovery på värdar för att hitta webbtjänster, men i det här sammanhanget förlitar man sig enbart på resultaten från Nmap, som redan har utfört denna operation, vilket sparar tid:



![nmap-image](assets/fr/61.webp)



använda Nmap-resultat i XML-format med `aquatone`._



För er information följer här ett utdrag ur den rapport som Aquatone har tagit fram:



![nmap-image](assets/fr/62.webp)



exempel på en "aquatone"-rapport



Personligen använder jag ofta Aquatone för att få en snabb överblick över vilka typer av webbplatser som finns i nätverket, särskilt tack vare dess skärmdumpfunktionalitet.



Även här sparar det tid att ha en komplett Nmap-rapport i XML-format och gör det enkelt att återanvända den i ett annat verktyg.



### IV. Slutsatser



Dessa två exempel visar tydligt att Nmaps XML-format gör det enkelt för andra verktyg att använda resultaten, eftersom det är ett strukturerat och lättanvänt dataformat. Det finns många andra verktyg som kan bearbeta dessa resultat, t.ex. automatiserade rapporteringsverktyg, grafiska presentationer eller mer komplexa, egenutvecklade sårbarhetsskannrar.



Naturligtvis kan du också utveckla egna skript och verktyg i Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) eller något annat språk med ett XML-parsingbibliotek för att manipulera och återanvända Nmap-resultatdata som du vill.



Detta avsnitt avslutar handledningsmodulen om mer avancerad användning av Nmap, i synnerhet för sårbarhetssökning med hjälp av NSE-skript.



Nästa avsnitt av handledningen kommer bland annat att fokusera på några ytterligare, mer tekniska bästa metoder och tips om de specifika skanningar som Nmap kan utföra. Vi kommer också att ta en titt på alternativ för optimering av skanningsprestanda, som är särskilt användbara vid skanning av stora nätverk.




## 11 - Förbättra prestanda för nätverkssökning



### I. Presentation



I det här kapitlet lär vi oss hur man optimerar hastigheten på nätverksskanningar som utförs med Nmap genom att använda olika specifika alternativ. Framför allt lär vi oss mer om Nmaps inre funktioner, från _timeout_-hantering till verktygets försparade konfigurationer.



Nu när vi har tagit en ordentlig titt på Nmaps funktioner ska vi ta itu med odjuret och dess kraft. Om du någonsin har använt verktyget i stora nätverk har du förmodligen märkt att vissa skanningar kan ta lång tid, trots verktygets kraft. Och det finns goda skäl till det: ett enkelt `nmap`-kommando med några få alternativ kan generate miljontals paket med hundratusentals potentiella system och tjänster som mål.



Dessutom kan vissa konfigurationer av nätverksutrustning avsiktligt införa en lägre hastighet (antal paket per sekund), med risk för att dina paket avvisas eller att din IP Address förbjuds av säkerhetsskäl.



Beroende på sammanhanget kan det vara värt att försöka optimera allt detta, vilket vi kommer att se i det här kapitlet.



I vilket fall som helst kan du kontrollera standardvärdena för de parametrar vi ska titta på, samt om de alternativ du ska använda har beaktats på rätt sätt, via Nmap debug (alternativ `-d` i ett tidigare kapitel):



![nmap-image](assets/fr/63.webp)



visa alternativ för tidsinställning via Nmaps alternativ `-d`._



### II. Hantera hastigheten för Nmap-skanningar



#### A. Hantering av parallellisering



Som standard använder Nmap parallellisering i sina skanningar för att optimera dem, och alla parametrar som den använder kan ändras via olika alternativ. De fall där det faktiskt är nödvändigt att ändra dessa parametrar är dock ganska sällsynta, så vi kommer inte att gå in på dem i detalj i denna handledning:





- `--min-hostgroup/max-hostgroup <size>`: storlek på parallella host scan-grupper.





- `--min-parallelism/max-parallelism <numprobes>`: parallellisering av Probes.





- `--scan-delay/--max-scan-delay <time>`: justerar fördröjningen mellan sonderna.




Du ska bara veta att de finns och kan användas.



#### B. Hantering av antalet paket per sekund



Som standard justerar Nmap själv antalet paket per sekund som skickas beroende på nätverkets respons. Det är dock möjligt att tvinga fram den här inställningen genom att definiera det högsta och/eller lägsta värde som ska följas när det gäller antal paket per sekund. Denna inställning görs med hjälp av alternativen `--min-rate <nummer>` och `--max-rate <nummer>` där `nummer` representerar ett antal paket per sekund. Exempel på detta:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Med dessa alternativ kan du justera hastigheten på skanningarna efter dina specifika behov, antingen för att påskynda processen eller för att begränsa den bandbredd som används. Det senare fallet (begränsa hastigheten på skanningar) är det som troligen leder dig till dessa alternativ, särskilt om du upplever nätverksfördröjning när du använder Nmap (vilket är ganska sällsynt).



### III. Hantering av felaktiga anslutningar och timeouts



En annan parameter som vi kan spela med för att optimera hastigheten på Nmap-sökningar (eller garantera större noggrannhet) är _timeout_ och _retry_.



För _timeouts_ är detta **no response timeout** efter vilken Nmap slutar vänta på ett svar och betraktar tjänsten eller värden som oåtkomlig. För _retry_ är detta **antalet på varandra följande försök till en operation** som Nmap kommer att utföra innan den går vidare.



På samma sätt som vid parallellisering kan hantering av _timeout_ och _retry_ tillämpas på värd- eller tjänsteupptäcktsfaserna:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: anger round-trip-tiden för en Exchange. Även denna parameter beräknas och anpassas i realtid under skanningen. Det är osannolikt att du kommer att behöva använda den, eftersom Nmap beräknar den här tiden i farten enligt nätverksreaktionen.





- `--max-retries <number>`: begränsar antalet retransmissioner av ett paket under portskanning. Som standard kan Nmap göra upp till 10 omförsök för en enda tjänst, särskilt om den hittar fördröjningar eller förluster på nätverksnivå, men i de flesta fall utförs bara ett.





- `--host-timeout <time>`: anger den maximala tid som Nmap kommer att spendera på en värd för alla sina operationer, inklusive portskanning, tjänstdetektering och alla andra operationer som är relaterade till den värden. Om detta tidsintervall överskrids utan något svar eller **avslutade åtgärder** kommer Nmap att överge denna värd utan att visa några resultat om den och gå vidare till nästa i listan. Detta gör att du kan styra den maximala tid som Nmap spenderar på en viss värd, undvika att fastna på motsträviga värdar och optimera den totala skanningstiden.




I mitt dagliga arbete använder jag alternativen `--max-retries` och `--host-timeout` för att optimera mina skanningar:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Dessa parametrar ger ytterligare flexibilitet när det gäller att anpassa skanningsbeteendet till specifika behov och nätverksförhållanden. Du måste dock vara medveten om deras konsekvenser när det gäller belastning på skannade värdar och potentiell förlust av noggrannhet.



### IV. Användning av förberedda konfigurationer



De olika alternativen som vi har sett i det här kapitlet kan användas individuellt eller som en del av de färdiga konfigurationer som Nmap erbjuder. Alternativet som gör det möjligt att använda dessa _mallar_ (konfigurationsmallar) är `-T <nummer>` eller `-T <namn>`. Det finns 5 användbara nivåer av _mallar_:



```
-T<0-5>: Set timing template (higher is faster)
```



Som standard använder Nmap _template_ 3 (_normal_), vilket i allmänhet är tillräckligt.



För egen del arbetar jag i allmänhet i sammanhang där jag behöver vara ganska snabb (samtidigt som jag är så komplett som möjligt) och jag använder ofta alternativet `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Så här ser debug-informationen för den här skanningen ut:



![nmap-image](assets/fr/64.webp)



användning av `-T4` setup under en Nmap-scanning



### V. Slutsats



I det här kapitlet har vi tittat på olika tekniker och alternativ som du kan använda för att hantera Nmaps kraft, aggressivitet och prestanda. Dessa alternativ är särskilt användbara vid skanning av stora nätverk, och mer sällan för smygändamål.



I nästa kapitel tar vi en titt på några bästa metoder för att använda Nmap och säkerställa dess säkerhet.




## 12 - Datasäkerhet och sekretess vid användning av Nmap



### I. Presentation



I det här kapitlet tar vi upp ett antal goda rutiner som ska tillämpas när det gäller säkerhet och framför allt sekretess för data som produceras, bearbetas och lagras av Nmap.



Användningen av Nmap i ett informationssystem kan snabbt kategoriseras som en offensiv åtgärd. Följaktligen måste ett antal försiktighetsåtgärder vidtas för att agera inom en rättslig ram, samtidigt som säkerheten för de avsedda målen, de insamlade uppgifterna och det system som används för skanningen garanteras.



### II. Erhållande av lämpliga tillstånd



Innan du skannar ett nätverk eller system måste du se till att du har erhållit lämpliga behörigheter. Att skanna system efter sårbarheter (NSE-skript) utan tillstånd kan vara olagligt och kan få rättsliga följder, särskilt om säkerhet i informationssystem inte ingår i ditt officiella ansvarsområde.





- Som en påminnelse: [Brottsbalken: Kapitel III: Angrepp på system för automatisk databehandling] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Skydd av känsliga uppgifter



De resultat som Nmap producerar kan betraktas som känsliga, särskilt när de innehåller information om svagheter i informationssystemet som kan utnyttjas av en angripare. Men även när de rör system som inte är tillgängliga för alla (t.ex. känsliga informationssystem inom industri, sjukvård eller [backup] informationssystem (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Vi har också sett att, beroende på vilka NSE-skript som används, kan NSE-skanningsresultaten från [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) också innehålla identifierare.



En illvillig person som lyckas få tillgång till dessa skanningsresultat kommer således att ha tillgång till en karta över informationssystemet och en mängd teknisk information, utan att själv ha utfört dessa åtgärder, med risk för att bli upptäckt.



Det är därför viktigt att se till att inte samla in eller lagra känslig information på ett olämpligt sätt när du använder Nmap, inklusive, men inte begränsat till, följande:





- Kryptera utdata: Om du behöver lagra eller överföra resultaten av dina Nmap-sökningar ska du se till att kryptera dem för att skydda datakonfidentialiteten. Detta förhindrar obehörig avlyssning av känslig information. Helst bör data krypteras så snart de lämnar det system som användes för att utföra skanningen (ett ZIP-arkiv krypterat med ett starkt lösenord är en mycket bra början).





- Konfigurera åtkomstkontroller: se till att endast behöriga personer har tillgång till resultaten av dina Nmap-sökningar där de kommer att lagras. Konfigurera lämpliga åtkomstkontroller för att skydda känslig information från obehörig åtkomst.





- Vaksamhet vid datahantering: När du överför, kopierar eller bearbetar skanningsdata, se till att du håller datasäkerheten under strikt kontroll. Detta innebär: låt dem inte ligga och skräpa i katalogen "Download" på en arbetsstation som är ansluten till Internet, låt dem inte passera genom din interna HTTP-fil Exchange-applikation, lämna inte Notepad öppet utan att låsa arbetsstationen under lunchrasten, etc.




### IV. Hantering av aggressiva skanningar



Som vi har sett i den här handledningen kan Nmap vara mycket utförlig på nätverksnivå. Den kan också skicka paket som inte är korrekt formaterade och som inte strikt respekterar protokollstrukturen i de nätverksramar och paket som den genererar. Alla dessa åtgärder kan påverka vissa system och tjänster, ibland till den grad att de orsakar funktionsfel eller mättnad av system- och nätverksresurser.



För att undvika incidenter måste du behärska Nmaps beteende och veta hur du anpassar det till det sammanhang där det används, med hjälp av de olika alternativ som diskuteras i den här handledningen. Vi kommer inte nödvändigtvis att använda Nmap på samma sätt i ett informationssystem som innehåller industriell [hårdvara] (https://www.it-connect.fr/actualites/actu-materiel/) som i ett användarnätverk som består av Windows-system som skyddas av en lokal brandvägg eller i en nätverkskärna.



Förhoppningsvis har de olika lektionerna i den här handledningen lärt dig hur du behärskar och analyserar Nmaps beteende, men det bästa sättet att lära sig är att göra. Se därför till att du är bekant med de Nmap-alternativ som du kommer att använda.



### V. Skydd av skanningssystemet



I det första kapitlet såg vi att Nmap i de flesta fall måste köras som "root" eller lokal administratör. Detta beror på att programmet utför nätverksoperationer, ibland på en ganska låg nivå, via nätverksbibliotek som kräver höga och riskfyllda behörigheter med tanke på systemets stabilitet eller andra programs sekretess.



Därför kan Nmap ses som en känslig komponent i det system där den är installerad. Se till att använda den senaste versionen av Nmap, eftersom äldre versioner kan innehålla kända säkerhetsproblem. Genom att använda en uppdaterad version kan du minimera de risker som är förknippade med att använda verktyget.



Om du har valt att använda Nmap inte via en session som `root`, utan genom att ge specifika privilegier till en privilegierad användare så att han har allt han behöver för att använda Nmap (`sudo` eller _capabilities_), bör du vara medveten om att Nmap kan användas som en del av en fullständig förhöjning av privilegier:



![nmap-image](assets/fr/65.webp)



höjning av Nmap-privilegier via `sudo`._



Här använder jag Nmap-kommandot genom `sudo`, men det gör att jag kan få ett interaktivt skal som `root` på systemet, vilket inte var det ursprungliga målet.



Det är också mycket olämpligt att installera Nmap på system som inte är utformade för att utföra nätverksskanningar. Jag tänker särskilt på servrar eller arbetsstationer. Å ena sidan skulle detta lägga till en potentiell vektor för privilegiehöjning, men framför allt skulle det ge angriparen enkel tillgång till ett offensivt verktyg.



Slutligen måste säkerheten i det system som används för skanning säkerställas på ett mer övergripande plan, så att det inte i sig blir en vektor för intrång eller informationsläckage. Som systemadministratör är det bättre att använda ett dedikerat system, helst med begränsad livslängd, i stället för den egna arbetsstationen.



### VI. Slutsatser



Sammanfattningsvis bör du se till att du behärskar Nmap ordentligt innan du använder det i verkliga förhållanden eller under produktionsförhållanden och vara vaksam när du bearbetar och hanterar dess resultat. Det vore synd att orsaka skada, läcka data eller underlätta en kompromettering, när det ursprungliga tillvägagångssättet syftar till att förbättra ditt företags säkerhet.



## 13 - Portskanning via TCP: SYN, Connect och FIN



### I. Presentation



I detta och nästa kapitel tittar vi närmare på de olika typerna av TCP-scanning som finns i Nmap, med början med de vanligaste: SYN-, Connect- och FIN-skanningar.



Som du kanske har märkt erbjuder Nmap flera alternativ för TCP-scanningar:



![nmap-image](assets/fr/66.webp)



skanningstekniker som finns tillgängliga i Nmap._ _



Tanken är att vi ska förklara några av dessa metoder och hjälpa dig att förstå skillnaderna, fördelarna och begränsningarna med dem. Du kommer att se att beroende på sammanhanget eller vad du vill veta är det bättre att välja det ena eller det andra alternativet.



### II. TCP SYN-sökning eller "Half Open-sökning



Den första typen av TCP-skanning som vi ska titta på är `TCP SYN Scan`, även känd som `Half Open Scan`. Om du kommer ihåg de nätverksskanningar vi gjorde efter våra första portskanningar, är detta den typ av skanning som används som standard av [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) när den körs med root-rättigheter.



Översättningen kommer att hjälpa dig att förstå hur denna skanning fungerar. Faktum är att en TCP SYN-sökning skickar ett TCP SYN-paket till varje målport, vilket är det första paketet som skickas av en klient (den som begär att upprätta en anslutning) som en del av den berömda _Trevägs handskakning_ TCP. Om porten är öppen på målservern, med en tjänst som körs bakom den, skickar servern normalt tillbaka ett TCP SYN/ACK-paket för att validera klientens SYN och initiera TCP-anslutningen. Detta svar har formen av ett TCP-paket med SYN- och ACK-flaggorna inställda på 1, vilket gör att vi kan bekräfta att porten är öppen och leder till en tjänst.



Om porten däremot är stängd skickar servern ett `TCP`-paket till oss med flaggorna RST och ACK inställda på 1 för att avsluta anslutningsbegäran, så att vi vet att ingen tjänst verkar vara aktiv bakom den här porten:



![nmap-image](assets/fr/67.webp)



tCP SYN Scan beteendediagram för öppna och stängda portar



För att få en mer konkret bild av `TCP SYN Scan` utförde jag en skanning av port TCP/80 till en värd som hade en aktiv webbserver på den här porten. När vi kör en nätverksskanning med Wireshark kan vi se följande flöde (skanningskälla: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



nätverksinspelning under en TCP SYN-sökning efter en öppen port



På den första raden ser vi att skanningskällan skickar ett TCP-paket till värden `10.10.10.203` på port TCP/80. I detta TCP-paket är SYN-flaggan satt till 1 för att indikera att detta är en begäran om initiering av en TCP-anslutning.



På den andra raden ser vi att målet svarar med ett `TCP SYN/ACK`, vilket innebär att det accepterar att initiera en anslutning och därmed att ta emot strömmar på port TCP/80. Vi kan därför dra slutsatsen att port TCP/80 är öppen och att en webbserver finns på den skannade servern.



Vår värd skickar sedan tillbaka ett RST-paket för att stänga anslutningen, vilket gör att den skannade värden inte behöver hålla en öppen TCP-anslutning i väntan på svar. Om en skanning görs på många portar kan det leda till ett "denial of service" om TCP-anslutningar inte stängs, eftersom antalet anslutningar som väntar på svar som servern kan upprätthålla blir för stort (se [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



I Wireshark kommer du att kunna se statusen för TCP-flaggor för varje test vi utför. Detta kommer att visa om paketet är ett SYN-, SYN/ACK-, ACK-, etc. paket:



![nmap-image](assets/fr/69.webp)



visa ett pakets TCP-flaggor i Wireshark (TCP SYN här)



Omvänt körde jag samma test mellan de två maskinerna, men den här gången skannade jag en TCP/81-port där ingen tjänst är aktiv (skanningskälla: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



nätverksinspelning under en TCP SYN-sökning för en stängd port



Den skannade värden returnerar en `TCP RST/ACK` som svar på min `TCP SYN` när porten inte är öppen.



Som nämnts är TCP SYN Scan standardläget när Nmap körs från en privilegierad terminal, och det kan tvingas fram med alternativet `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




Av snabbhetsskäl är `TCP SYN Scan` den skanning som används mest. Å andra sidan kan en klients misslyckande med att slutföra _Tree Way Handshake_ (dvs. att inte skicka ACK efter serverns SYN/ACK) verka misstänkt om det observeras alltför många gånger på en server eller från samma källa i nätverket. Det normala beteendet hos en klient efter att ha tagit emot ett TCP SYN/ACK-paket som svar på en TCP SYN är att skicka en bekräftelse (ACK) och sedan starta Exchange.



Ändå ger den en något snabbare skanning, eftersom den inte bryr sig om att skicka en ACK för varje positivt svar. Fördelen med SYN Scan är dess snabbhet, eftersom endast ett paket skickas per port som ska skannas, på bekostnad av en större chans att upptäckas.



Dessutom kan TCP SYN scan upptäcka om en port är filtrerad (skyddad) av en brandvägg. Faktum är att en brandvägg framför målvärden kan upptäckas genom hur den beter sig när den tar emot ett TCP SYN-paket på en port som den är tänkt att skydda. Den svarar helt enkelt inte. Men som vi har sett kommer det i båda fallen (öppen eller stängd port) ett svar från värden. Detta tredje beteende kommer att avslöja förekomsten av en brandvägg mellan den skannade värden och den maskin som kör skanningen. Här är resultatet som Nmap kan returnera när en skannad port filtreras av en brandvägg:



![nmap-image](assets/fr/71.webp)



nmap-visning vid skanning av en filtrerad port



När vi gör en nätverksinspelning vid skanningstillfället kan vi faktiskt se att inget svar ges:



![nmap-image](assets/fr/72.webp)



nätverksinspelning under en TCP SYN-sökning för en port som filtreras av en brandvägg



Skillnaden mellan en stängd port och en filtrerad port är följande: en filtrerad port är en port som skyddas av en brandvägg, medan en stängd port är en port där ingen tjänst körs och som därför inte kan bearbeta våra TCP-paket. Vissa typer av TCP-sökningar, t.ex. TCP SYN-sökningen, kan upptäcka om en port är filtrerad, medan andra typer av sökningar inte kan det.



### III. TCP Connect-sökning eller Full Open-sökning



Den andra typen av TCP-scanning är `TCP Connect scan`, även känd som _Full Open Scan_. Den fungerar på samma sätt som TCP SYN-scanningen, men den här gången returneras ett `TCP ACK` efter ett positivt svar från servern (ett SYN/ACK). Det är därför den kallas "Full Open", eftersom anslutningen är helt öppen och initieras på varje port som öppnas under skanningen, vilket respekterar TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



tCP Connect Scan beteendediagram för öppna och stängda portar



Här är vad som kan ses passera genom nätverket under en `TCP Connect scan` som riktar in sig på en öppen port:



![nmap-image](assets/fr/74.webp)



nätverkssniffning under en TCP Connect-sökning efter en öppen port



Vi kan se att det första TCP-paketet som skickas är en `TCP SYN` som skickas av klienten, och servern svarar sedan med en `TCP SYN/ACK`, vilket indikerar att porten är öppen och har en aktiv tjänst. För att simulera en legitim klient hela vägen kommer Nmap sedan att skicka en `TCP ACK` tillbaka till servern. Omvänt, när du skannar en stängd port:



![nmap-image](assets/fr/75.webp)



nätverksinspelning under en TCP Connect-sökning efter en stängd port



Observera att serverns svar på vårt `SYN`-paket återigen är ett `TCP RST/ACK`-paket, så vi kan dra slutsatsen att porten är stängd och att inga tjänster körs på den.



När du använder Nmap används alternativet `-sT` (`scan Connect`) för att utföra en TCP Connect Scan. Observera att när Nmap används från en session utan behörighet är detta standardläget för TCP-scanning:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



`TCP Connect Scan` simulerar en mer legitim anslutningsbegäran, med ett beteende som mest liknar en lambdaklients, så det är svårare att upptäcka en skanning på ett minskat antal portar. Den är dock långsammare, eftersom den initierar alla TCP-anslutningar på den skannade maskinens öppna portar.



En Nmap-sökning av 10 000 portar kommer fortfarande att vara lätt att upptäcka om tjänster för upptäckt och skydd mot nätverksintrång (IDS, IPS, EDR) är installerade. När en angripare vill hålla en låg profil tenderar han att fokusera på ett litet antal strategiskt utvalda portar, t.ex. 445 (SMB) eller 80 (HTTP), som ofta är öppna på servrar och utgör vanliga sårbarheter.



Eftersom TCP Connect Scan förväntar sig ett svar i båda fallen kan den också upptäcka förekomsten av en brandvägg som kan filtrera portar på målvärden.



### IV. TCP FIN-sökning eller "Stealth Scan



TCP FIN Scan, även känd som _Stealth Scan_, använder beteendet hos en klient som avslutar en TCP-anslutning för att upptäcka en öppen port.



I TCP innebär "end of session" att ett TCP-paket skickas med FIN-flaggan inställd på 1. I en normal Exchange upphör servern med all kommunikation med klienten (inget svar). Om servern inte har någon aktiv TCP-anslutning med klienten skickar den ett `RST/ACK`. Vi kan därför skilja mellan öppna och stängda portar genom att skicka `TCP FIN`-paket till en uppsättning portar:



![nmap-image](assets/fr/76.webp)



beteendediagram för tCP FIN-sökning för öppna och stängda portar



Jag fångade återigen nätverket under en _Stealth scan_ och det här är vad du ser när den skannade porten är öppen:



![nmap-image](assets/fr/77.webp)



nätverksinspelning under en TCP FIN-sökning efter en öppen port



Vi kan se att klienten skickar ett eller två paket för att avsluta en TCP-anslutning och att servern inte svarar. Den accepterar helt enkelt att anslutningen är avslutad och slutar kommunicera.



Så här ser det ut nu när vi skannar en stängd port:



![nmap-image](assets/fr/78.webp)



nätverksinspelning under en TCP FIN-sökning för en stängd port



Vi ser att servern skickar tillbaka ett `TCP RST/ACK`-paket, så det finns en skillnad i beteende mellan en öppen och en stängd port, och vi kan lista de öppna portarna på en server genom att skicka ett TCP FIN-paket. Med Nmap används alternativet `-sF` (`scan FIN`) för att utföra en TCP FIN-sökning:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan fungerar inte på Windows-värdar, eftersom operativsystemet tenderar att ignorera TCP FIN-paket när de skickas till portar som inte är öppna. Så om du kör en TCP FIN Scan på en Windows-värd får du intrycket att alla portar är stängda.



Därför är det viktigt att känna till flera olika skanningsmetoder och förstå skillnaden mellan dem.



Eftersom TCP FIN inte väntar på svar i något av fallen kommer den inte att kunna upptäcka om det finns en brandvägg mellan målvärden och skanningskällan.



Här är ett exempel på resultatet av Nmaps TCP FIN-sökning:



![nmap-image](assets/fr/79.webp)



resultat av en TCP FIN-sökning med Nmap._ _



Faktum är att ett uteblivet svar från värden på en viss port kan betyda att porten är filtrerad, men också att den är öppen och aktiv.



Den här skanningen kallas "stealth", eftersom den inte generate mycket trafik och i allmänhet inte orsakar loggning i de berörda systemen. Den kan användas för att diskret upptäcka portar i ett nätverk utan att utlösa några larm. Men som nämnts ovan kan dess effektivitet variera beroende på målsystemet, liksom dess diskretion beroende på konfigurationen av säkerhetsutrustningen.



### V. Slutsats



Så långt det första av två kapitel om de olika TCP-skanningstyperna som Nmap erbjuder! I nästa kapitel tittar vi på TCP-skanningstyperna XMAS, Null och ACK, som fungerar på olika sätt för att upptäcka öppna portar på en värd.





## 14 - Portskanning via TCP: XMAS, Null och ACK



### I. Presentation



I det här avsnittet fortsätter vi att utforska de olika TCP-skanningsmetoder som Nmap erbjuder. Här tittar vi på metoderna `XMAS`, `Null` och `ACK`, som använder TCP-specifika funktioner för att hämta information om de portar och tjänster som är öppna på ett visst mål.



### II. TCP XMAS-skanning



XMAS Scan TCP är lite ovanligt eftersom det inte alls simulerar normalt användar- eller maskinbeteende i ett nätverk. Faktum är att XMAS Scan skickar TCP-paket med flaggorna `URG` (Urgent), `PSH` (Push) och `FIN` (Finish) inställda på 1, för att kringgå vissa brandväggar eller filtreringsmekanismer.



Namnet XMAS kommer från det faktum att det är ovanligt att se dessa flaggor aktiverade. När alla tre flaggorna är aktiverade samtidigt i ett TCP-paket ser det ut som en upplyst julgran:



![nmap-image](assets/fr/80.webp)



tCP-flaggor som används i XMAS-scanning



Utan att gå in i detalj på dessa flaggors roll här är det viktigt att veta att när man skickar ett paket med dessa tre flaggor aktiverade kommer en aktiv tjänst bakom målporten inte att returnera några paket. Å andra sidan, om porten är stängd, får vi ett TCP RST/ACK-paket. Vi kan nu skilja mellan beteendet hos en öppen och en stängd port när vi listar portar på en maskin:



![nmap-image](assets/fr/81.webp)



tCP XMAS Scan beteendediagram för öppna och stängda portar



Enligt samma logik visar en nätverksskanning på port TCP/80 på en värd med en aktiv webbserver följande beteende när en öppen port upptäcks (skanningskälla `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



nätverksinspelning under en TCP XMAS-sökning efter en öppen port



Vi kan se att skanningskällan skickar två TCP XMAS-paket (med flaggorna `FIN`, `PSH` och `URG` inställda på 1) till värden `10.10.10.203` och att det inte kommer någon retur från målet, vilket indikerar att porten är öppen. Omvänt, när du utför en `TCP XMAS Scan` på en stängd port, observeras följande resultat:



![nmap-image](assets/fr/83.webp)



nätverksinspelning under en TCP XMAS-sökning för en stängd port



Svaret på vårt TCP-paket är då ett `TCP RST/ACK`, vilket indikerar att porten är stängd. Om du vill använda den här tekniken med Nmap kan du med alternativet `-sX` (`scan XMAS`) utföra en TCP XMAS-scanning:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Det är viktigt att notera att TCP XMAS-skanningen inte kan upptäcka brandväggar som kan finnas mellan målet och skanningsmaskinen, till skillnad från vissa andra typer av skanning som TCP SYN eller Connect. En aktiv brandvägg mellan de två värdarna kommer att säkerställa att ingen TCP-retur görs om den port som är målet är filtrerad (dvs. skyddad av brandväggen). I händelse av ett uteblivet svar är det därför omöjligt att veta om porten är skyddad av brandväggen eller öppen och aktiv. Du bör också vara medveten om att vissa applikationer eller operativsystem, t.ex. Windows, kan förvränga resultaten av denna typ av skanning, precis som TCP FIN-skanningen.



obs: stödet för XMAS/FIN/NULL-skanningar på de senaste versionerna av Windows är fortfarande begränsat, och resultaten kan vara inkonsekventa på denna typ av mål. (Uppdatering 2025)



### III. TCP Null-sökning



I motsats till TCP XMAS scan skickar TCP Null scan TCP-scanpaket med alla flaggor inställda på 0. Även detta är ett beteende som aldrig förekommer i en normal Exchange mellan maskiner, eftersom det inte specificeras i RFC som beskriver TCP-protokollet att skicka ett TCP-paket utan flagga. Det är därför det kan upptäckas lättare.



Precis som TCP XMAS-sökningen kan den här sökningen störa vissa brandväggar eller filtreringsmoduler och låta paket passera igenom:



![nmap-image](assets/fr/84.webp)



tCP Null Scan-beteendediagram för öppna och stängda portar



Så här ser det ut i nätverket under en TCP Null-sökning på en öppen port:



![nmap-image](assets/fr/85.webp)



nätverksinspelning under en TCP Null-sökning efter en öppen port



Skanningsmaskinen skickar ett flagglöst paket (`[<None>]` i Wireshark) utan något svar från servern. Omvänt, när målporten är stängd:



![nmap-image](assets/fr/86.webp)



nätverksinspelning under en TCP Null-sökning för en stängd port



För att utföra en TCP Null-sökning med Nmap använder du helt enkelt alternativet `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Eftersom svaret är identiskt när en port är öppen och när en brandvägg är aktiv (ingen återkoppling från servern i båda fallen) kan TCP Null scan inte upptäcka om det finns en brandvägg. Dessutom kan brandväggen till och med förfalska resultatet genom att antyda att en port är öppen, eftersom den inte svarar på TCP-paket utan flaggor, trots att porten är filtrerad. Detta är viktig information att vara medveten om när man använder skanningar som inte kan skilja mellan en öppen och en filtrerad (brandväggsskyddad) port, t.ex. `TCP Null`, `XMAS` eller `FIN` skanningar, för att vara konsekvent i tolkningen av de erhållna resultaten.



### IV. TCP ACK-sökning



TCP ACK-sökningen används för att upptäcka förekomsten av en brandvägg på målvärden eller mellan målet och skanningskällan.



Till skillnad från andra skanningar försöker TCP ACK-skanningen inte identifiera vilka portar som är öppna på värden, utan snarare om ett filtreringssystem är aktivt, och svarar för varje port med `filtered` eller `unfiltered`. Vissa TCP-sökningar, t.ex. `TCP SYN` eller `TCP Connect`, kan göra båda samtidigt, medan andra, t.ex. `TCP FIN` eller `TCP XMAS`, inte kan avgöra om det finns någon filtrering alls. Det är därför TCP ACK-scanningen kan vara användbar:



![nmap-image](assets/fr/87.webp)



beteendediagram för tCP ACK Scan för filtrerade och ofiltrerade portar



Vi använder Nmaps `-sA`-alternativ för att utföra den här typen av skanning. Här är resultatet av en TCP ACK-sökning om porten är filtrerad, dvs. blockerad och skyddad av en brandvägg:



![nmap-image](assets/fr/88.webp)



nmap-visning under TCP ACK Scan._



Exempel på resultat för en host med brandvägg och en utan. Nmap returnerar `filtered` på portarna TCP/80 och TCP/81 hos värden `10.10.10.203`. Vid en nätverksanalys via Wireshark ser beteendet ut enligt följande:



![nmap-image](assets/fr/89.webp)



nätverksinspelning under en TCP ACK-sökning för en port som inte filtreras av en brandvägg



Målmaskinen returnerar ingenting om det finns en brandvägg.



Om du vill starta den här skanningen med Nmap använder du alternativet `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Slutsats



Vi har tittat på tre olika metoder för att skanna via TCP utöver de som redan presenterats. Dessa olika metoder ska användas under mycket specifika förhållanden och sammanhang, särskilt i samband med penetrationstester eller Red Team-operationer, under vilka begrepp som diskretion är närvarande.



## 15 - Nmap CheatSheet - Sammanfattning av självstudiekommandon



### I. Presentation



Här är en kort sammanfattning av Nmaps många kommandon och användningsområden, så att du snabbt kan hitta och återanvända dem i vardagen.



### II. Nmap: CheatSheet IT-Connect



Här är en checklista över de kommandon som presenteras. Den här sidan gör det enkelt att hitta de vanligaste användningsområdena för Nmap.





- Portskanning




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Upptäcka aktiva värdar




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



obs: Alternativet `-sP` har varit föråldrat i flera år och bör ersättas av `-sn`. (Uppdatering 2025)_ _



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Versionsdetektering




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE-skript: letar efter sårbarheter




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Hantering av Nmap-utdata




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Optimering av prestanda




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Typer av TCP-scanning




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Jag hoppas att du tycker att dessa kommandon är användbara. Glöm inte att anpassa målet för dina skanningar till ditt sammanhang och att hänvisa till den officiella dokumentationen för att fullt ut behärska de tester som utförs.



### III. Slutsatser



Handledningen för Nmap är nu klar. Du har nu de grunder du behöver för att använda detta omfattande och kraftfulla verktyg. Vi rekommenderar starkt att du övar på kontrollerade miljöer (Hack The Box, VulnHub, virtuella maskiner) innan du använder det i produktion.



Det finns mycket kvar att utforska när det gäller verktygets inre funktioner och avancerade egenskaper. Men om du behärskar de kommandon och begrepp som presenteras här kommer du att kunna använda Nmap på ett säkert och relevant sätt.