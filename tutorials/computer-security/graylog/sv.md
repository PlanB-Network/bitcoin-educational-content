---
name: Graylog
description: Centralisera och analysera dina loggar på ett enkelt sätt
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian BURNEL publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___



## Driftsättning av Graylog på Debian 12



### I. Presentation



Graylog är en "log sink"-lösning med öppen källkod som är utformad för att centralisera, lagra och analysera loggar från dina maskiner och nätverksenheter i realtid. I den här handledningen lär vi oss hur man installerar gratisversionen av Graylog på en Debian 12-maskin!



I ett informationssystem genererar varje **server**, oavsett om den kör **Linux** eller **Windows**, och varje **nätverksenhet** (switch, router, brandvägg etc...) ** sina egna loggar**, som lagras lokalt. Med loggar som lagras lokalt på varje maskin är händelseanalys och korrelation mycket svårt... Det är här **Graylog** kommer in i bilden. Den kommer att fungera som en **loggsänka**, vilket innebär att **alla dina maskiner kommer att skicka sina loggar** (till exempel via syslog). Graylog kommer sedan att **lagra och indexera dessa loggar**, samtidigt som du kan utföra globala sökningar och skapa varningar.



Graylog är ett analys- och övervakningsverktyg som gör det lättare att identifiera misstänkta beteenden och olika problem (stabilitet, prestanda etc.).




![Image](assets/fr/034.webp)



** Notera: gratisversionen, **Graylog Open**, är inte en SIEM som Wazuh är, särskilt eftersom den saknar verkliga intrångsdetekteringsfunktioner.



### II. Förkunskapskrav



**stack Graylog** bygger på **flera komponenter** som vi kommer att behöva installera och konfigurera. Här installerar vi alla komponenter på samma server, men det är möjligt att skapa kluster baserat på flera noder och fördela rollerna över flera servrar. I den här handledningen installerar vi **Graylog 6.1**, den senaste versionen hittills.





- MongoDB 7**, den aktuella rekommenderade versionen för Graylog (minst 5.0.7, högst 7.x)
- OpenSearch**, en Fork med öppen källkod för Elasticsearch skapad av Amazon (minst 1.1.x, högst 2.15.x)
- OpenJDK 17**



**Graylog-servern** körs på **Debian 12**, men installation är möjlig på andra distributioner, inklusive via Docker. Den virtuella maskinen är utrustad med **8 GB RAM** och **256 GB diskutrymme**, för att ha tillräckligt med resurser för alla komponenter (annars kan detta ha en betydande inverkan på prestanda). Jag ger dock detta som en grov guide, eftersom **storleken på Graylog-arkitekturen beror på mängden information som ska bearbetas**. Graylog kan bearbeta 30 MB eller 300 MB data per dag, såväl som 300 GB data per dag... Det är en **skalbar lösning** som kan hantera **terabytes med loggar** (se [den här sidan](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Källa: Graylog



Innan du påbörjar konfigurationen ska du tilldela Graylog-maskinen en statisk IP Address och installera de senaste uppdateringarna. Var noga med att ställa in den lokala maskinens tidszon och definiera en NTP-server för synkronisering av datum och tid. Här är kommandot som ska köras:



```
sudo timedatectl set-timezone Europe/Paris
```



**Note: **OpenSearch-installationen är valfri** om du använder **Graylog Data Node** istället.



### III Steg-för-steg-installation av Graylog



Låt oss börja med att uppdatera paketcachen och installera de verktyg vi behöver för det som komma skall.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Installera MongoDB



När det är gjort börjar vi installera MongoDB. Ladda ner GPG-nyckeln som motsvarar MongoDB-arkivet:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Lägg sedan till MongoDB 6-repository på Debian 12-maskinen:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Nu ska vi uppdatera paketcachen och försöka installera MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB kan inte installeras eftersom ett beroende saknas: **libssl1.1**. Vi måste installera det här paketet manuellt innan vi kan fortsätta, eftersom Debian 12 inte har det i sina arkiv.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Vi ska hämta DEB-paketet med namnet "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (senaste versionen) med kommandot **wget** och sedan installera det med kommandot **dpkg**. Detta ger följande två kommandon:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Starta om MongoDB-installationen:



```
sudo apt-get install -y mongodb-org
```



Starta sedan om MongoDB-tjänsten och aktivera den så att den startar automatiskt när Debian-servern startas.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



När MongoDB är installerat kan vi gå vidare till att installera nästa komponent.



#### B. Installera OpenSearch



Låt oss gå vidare till att installera OpenSearch på servern. Följande kommando lägger till signaturnyckeln för OpenSearch-paket:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Lägg sedan till OpenSearch-repository så att vi kan ladda ner paketet med **apt** efteråt:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Uppdatera din paketcache:



```
sudo apt-get update
```



Sedan **installerar du OpenSearch** och ser till att **definiera standardlösenordet för din instants Admin**-konto. Här är lösenordet "**IT-Connect2024!**", men ersätt detta värde med ett starkt lösenord. **Undvik svaga lösenord** som "**P@ssword123**" och använd minst **8 tecken** med minst ett tecken av varje typ (gemener, versaler, siffror och specialtecken), annars kommer ett felmeddelande att visas i slutet av installationen. **Detta är en förutsättning sedan OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Vänligen ha tålamod under installationen...



När du är klar kan du ta en stund för att utföra minimikonfigurationen. Öppna konfigurationsfilen i YAML-format:



```
sudo nano /etc/opensearch/opensearch.yml
```



När filen är öppen kan du ställa in följande alternativ:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Den här OpenSearch-konfigurationen är utformad för att konfigurera en enda nod. Här följer några förklaringar av de olika parametrar som vi använder:





- cluster.name: graylog**: denna parameter namnger OpenSearch-klustret med namnet "**graylog**".
- node.name: ${HOSTNAME}**: nodnamnet ställs in dynamiskt så att det matchar namnet på den lokala Linux-maskinen. Även om vi bara har en nod är det viktigt att namnge den korrekt.
- sökväg.data: /var/lib/opensearch**: den här sökvägen anger var OpenSearch lagrar sina data på den lokala datorn, i det här fallet i "**/var/lib/opensearch**".
- sökväg.loggar: /var/log/opensearch**: denna sökväg definierar var OpenSearchs loggfiler lagras, här i "**/var/log/opensearch**".
- discovery.type: single-node**: denna parameter konfigurerar OpenSearch för att arbeta med en enda nod, därav valet av alternativet "**single-node**".
- network.host: 127.0.0.1**: den här konfigurationen säkerställer att OpenSearch bara lyssnar på sin lokala Interface-slinga, vilket är tillräckligt eftersom den finns på samma server som Graylog.
- action.auto_create_index: false**: genom att inaktivera automatisk indexskapande kommer OpenSearch inte automatiskt att skapa ett index när ett dokument skickas utan ett befintligt index.
- plugins.security.disabled: true**: detta alternativ avaktiverar OpenSearchs säkerhetsplugin, vilket innebär att det inte kommer att finnas någon autentisering, åtkomsthantering eller kommunikationskryptering. Den här inställningen sparar tid när Graylog konfigureras, men bör undvikas i produktion (se [denna sida](https://opensearch.org/docs/1.0/security-plugin/index/)).



Vissa alternativ finns redan, så du behöver bara ta bort "#" för att aktivera dem och sedan ange ditt värde. Om du inte kan hitta ett alternativ kan du deklarera det direkt i slutet av filen.



![Image](assets/fr/023.webp)



Spara och stäng den här filen.



#### C. Konfigurera Java (JVM)



Du måste konfigurera den Java Virtual Machine som OpenSearch använder för att kunna justera hur mycket minne tjänsten kan använda. Redigera följande konfigurationsfil:



```
sudo nano /etc/opensearch/jvm.options
```



Med den konfiguration som används här startar **OpenSearch med 4 GB allokerat minne och kan växa upp till 4 GB**, så det blir ingen minnesvariation under drift. Här tar konfigurationen hänsyn till det faktum att den virtuella maskinen har totalt **8 GB RAM**. Båda parametrarna måste ha samma värde. Detta innebär att man ersätter raderna:



```
-Xms1g
-Xmx1g
```



Med dessa rader:



```
-Xms4g
-Xmx4g
```



Här är en bild av den modifiering som ska göras:



![Image](assets/fr/022.webp)



Stäng den här filen efter att du har sparat den.



Dessutom måste vi kontrollera konfigurationen av parametern "**max_map_count**" i Linux-kärnan. Den definierar gränsen för minnesområden som mappas per process, för att tillgodose behoven i vår applikation. **OpenSearch**, liksom Elasticsearch**, rekommenderar att detta värde sätts till "262144" för att undvika fel i minneshanteringen.



I princip är värdet redan korrekt på en nyinstallerad Debian 12-maskin. Men låt oss kontrollera. Kör det här kommandot:



```
cat /proc/sys/vm/max_map_count
```



Om du får ett annat värde än "**262144**" ska du köra följande kommando, annars är det inte nödvändigt.



```
sudo sysctl -w vm.max_map_count=262144
```



Slutligen aktiverar du OpenSearch autostart och startar den tillhörande tjänsten.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Om du visar din systemstatus bör du se en Java-process med 4 GB RAM.



```
top
```



![Image](assets/fr/029.webp)



Nästa steg: den efterlängtade installationen av Graylog!



#### D. Installera Graylog



För att **installera Graylog 6.1** i dess senaste version, kör följande 4 kommandon för att **ladda ner och installera Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



När detta är gjort måste vi göra några ändringar i Graylogs konfiguration innan vi försöker starta den.



Låt oss börja med att konfigurera dessa två alternativ:





- password_secret**: Denna parameter används för att definiera en nyckel som används av Graylog för att säkra lagringen av användarlösenord (i samma anda som en saltningsnyckel). Denna nyckel måste vara **unik** och **slumpmässig**.
- root_password_sha2**: denna parameter motsvarar standardlösenordet för administratören i Graylog. Det lagras som en Hash SHA-256.



Vi börjar med att generera en nyckel på 96 tecken för parametern **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Kopiera det returnerade värdet och öppna sedan konfigurationsfilen för Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Klistra in nyckeln i parametern **password_secret**, så här:



![Image](assets/fr/027.webp)



Spara och stäng filen.



Därefter måste du ange lösenordet för kontot "**admin**" som skapats som standard. I konfigurationsfilen måste lösenordets Hash lagras, vilket innebär att det måste beräknas. I exemplet nedan anges Hash för lösenordet "**LogsWells@**": anpassa värdet till ditt lösenord.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Kopiera det erhållna värdet som utdata (utan bindestrecket i slutet av raden).



Öppna konfigurationsfilen för Graylog igen:



```
sudo nano /etc/graylog/server/server.conf
```



Klistra in värdet i alternativet **root_password_sha2** på följande sätt:



![Image](assets/fr/026.webp)



När du ändå är inne i konfigurationsfilen, ställ in alternativet "**http_bind_address**". Ange "**0.0.0.0:9000**" så att Graylogs Interface-webb kan nås på port **9000**, via valfri server IP Address.



![Image](assets/fr/024.webp)



Ställ sedan in alternativet "**elasticsearch_hosts**" till `http://127.0.0.1:9200` för att deklarera vår lokala OpenSearch-instans. Detta är nödvändigt eftersom vi inte använder en **Graylog Data Node**. Och utan detta alternativ kommer det inte att vara möjligt att gå längre...



![Image](assets/fr/025.webp)



Spara och stäng filen.



Detta kommando aktiverar Graylog så att det startar automatiskt vid nästa start och startar omedelbart Graylog-servern.



```
sudo systemctl enable --now graylog-server
```



När detta är gjort kan du försöka ansluta till Graylog från en webbläsare. Ange serverns IP Address (eller namn) och port 9000.



**För din information:**



För inte så länge sedan dök ett autentiseringsfönster liknande det nedan upp när du först loggade in på Graylog. Du var tvungen att ange din inloggning "**admin**" och ditt lösenord. Och sedan blev man obehagligt överraskad när man upptäckte att anslutningen inte fungerade.



![Image](assets/fr/031.webp)



Det var nödvändigt att gå tillbaka till kommandoraden på Graylog-servern och titta i loggarna. Vi kunde då se att **för den första anslutningen** är det nödvändigt att **använda ett tillfälligt lösenord**, som anges i loggarna.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Sedan fick man försöka igen med användaren "**admin**" och det tillfälliga lösenordet, och då gick det att logga in!



**Detta är inte längre fallet. Allt du behöver göra är att logga in med ditt administratörskonto och lösenordet som konfigurerats på kommandoraden



![Image](assets/fr/033.webp)



**Välkommen till Graylogs Interface!



![Image](assets/fr/019.webp)



#### E. Graylog: skapa ett nytt administratörskonto



I stället för att använda det administratörskonto som Graylog skapar kan du skapa ditt eget personliga administratörskonto. Klicka på menyn "**System**", sedan på "**Användare och team**" för att klicka på knappen "**Skapa användare**". Fyll sedan i formuläret och tilldela administratörsrollen till ditt konto.



![Image](assets/fr/020.webp)



Ett personligt konto kan innehålla ytterligare information, t.ex. för- och efternamn och e-post Address, till skillnad från ett vanligt administratörskonto. Dessutom ger det bättre spårbarhet när varje person arbetar med ett namngivet konto.



## Skicka loggar till Graylog med rsyslog



### I. Presentation



I den här andra delen lär vi oss hur man konfigurerar en Linux-maskin så att den skickar sina loggar till en Graylog-server. För att göra detta installerar och konfigurerar vi Rsyslog på systemet.



### II. Konfigurera Graylog för att ta emot Linux-loggar



Vi börjar med att konfigurera Graylog. Det finns tre steg att slutföra:





- Skapandet av en **Input** för att skapa en ingångspunkt som gör det möjligt för Linux-maskiner att **sända Syslog-loggar via UDP**.
- Skapandet av ett nytt **Index** för att lagra och **indexera alla Linux-loggar**.
- Skapande av en **Stream** för att **routa** de loggar som tas emot av Graylog till det nya Linux-indexet.



#### A. Skapa en ingång för Syslog



Logga in på Graylog Interface, klicka på "**System**" i menyn och sedan på "**Inputs**". I rullgardinsmenyn väljer du "**Syslog UDP**" och klickar sedan på knappen "**Lansera ny ingång**". Det går också att skapa en TCP Syslog Input, men då krävs ett TLS-certifikat: ett plus för säkerheten, men det behandlas inte i den här artikeln.



![Image](assets/fr/001.webp)



En guide kommer att visas på skärmen. Börja med att ge denna Input ett namn, till exempel "**Graylog_UDP_Rsyslog_Linux**" och välj en port. Som standard är porten "**514**", men du kan anpassa den. Här är porten "**12514**" vald.



![Image](assets/fr/016.webp)



Du kan också markera alternativet "**Store full message**" för att lagra hela loggmeddelandet i Graylog. Klicka på "**Starta inmatning**".



![Image](assets/fr/017.webp)



Den nya ingången har skapats och är nu aktiv. Graylog kan nu ta emot Syslog-loggar på port 12514/UDP, men vi är inte klara med konfigurationen av applikationen ännu.



![Image](assets/fr/018.webp)


**En enda ingång kan användas för att lagra loggar från flera Linux-maskiner.



#### B. Skapa ett nytt Linux-index



Vi behöver skapa ett index i Graylog för att lagra loggar från Linux-maskiner. Ett **index** i Graylog är en lagringsstruktur som innehåller de loggar som tagits emot, dvs. de meddelanden som tagits emot. Graylog använder OpenSearch som lagringsmotor och meddelanden indexeras för att möjliggöra snabba och effektiva sökningar.



I Graylog klickar du på "**System**" i menyn och sedan på "**Indices**". På den nya sidan som visas klickar du på "**Create index set**".



![Image](assets/fr/005.webp)



Namnge indexet, t.ex. "**Linux Index**", lägg till en beskrivning och ett prefix innan du bekräftar. Här kommer vi att **lagra alla Linux-loggar i det här indexet**. Det är också möjligt att skapa specifika index för att lagra endast vissa loggar (endast [SSH]-loggar (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), loggar från webbtjänster etc.).



![Image](assets/fr/006.webp)



Nu måste vi skapa en ny ström för att dirigera meddelanden till detta index.



#### C. Skapa en ström



För att skapa en ny stream, klicka på "**Streams**" i Graylogs huvudmeny. Klicka sedan på knappen "**Create stream**" till höger. I fönstret som visas namnger du strömmen, t.ex. "**Linux Stream**" och väljer indexet "**Linux Index**" i fältet "**Index Set**". Bekräfta ditt val.



**Meddelanden som motsvarar denna ström kommer också att inkluderas i "**Default Stream**", såvida du inte markerar alternativet "**Remove matches from 'Default Stream'**".



![Image](assets/fr/002.webp)



Klicka sedan på knappen "**Add stream rule**" i dina ånginställningar för att lägga till en ny regel för routning av meddelanden. Om du inte hittar det här fönstret, klicka på "**Streams**" i menyn och sedan på raden som motsvarar din stream, klicka på "**More**" och sedan på "**Manage Rules**".



Välj typen "**match input**" och välj den tidigare skapade **Rsyslog input in UDP**. Bekräfta med knappen "**Create Rule**". Alla meddelanden till vår nya ingång kommer nu att skickas till Index för Linux.



![Image](assets/fr/003.webp)



Din nya ström bör visas i listan och den bör vara i tillståndet "**Running**". Meddelandebandbredden visar "**0 msg/s**", eftersom vi för närvarande inte skickar några loggar till Rsyslog UDP-ingången. Om du vill visa en ströms loggar klickar du bara på dess namn.



![Image](assets/fr/004.webp)



**Allt är klart på Graylog-sidan**. Nästa steg är att konfigurera Linux-maskinen.



### III. Installera och konfigurera Rsyslog på Linux



Logga in på Linux-maskinen, antingen lokalt eller på distans, och använd ett användarkonto med behörighet att höja sina privilegier (via sudo). Annars kan du använda kontot "root" direkt.



#### A. Installera paketet Rsyslog



Börja med att uppdatera paketcachen och installera paketet med namnet "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Kontrollera sedan servicestatusen. I de flesta fall är den redan igång.



```
sudo systemctl status rsyslog
```



#### B. Konfigurera Rsyslog



Rsyslog har en huvudkonfigurationsfil som finns här:



```
/etc/rsyslog.conf
```



Dessutom används katalogen "**/etc/rsyslog.d/**" för att lagra ytterligare konfigurationsfiler för Rsyslog. I huvudkonfigurationsfilen finns ett Include-direktiv för att importera alla "**.conf**"-filer som finns i den här katalogen. Detta gör det möjligt att ha ytterligare filer för att konfigurera Rsyslog utan att ändra huvudfilen.



I den här katalogen måste du använda siffror för att definiera laddningsordningen, eftersom filerna laddas i alfabetisk ordning. Om du lägger till ett numeriskt prefix kan du hantera prioriteten mellan flera konfigurationsfiler. Här har vi bara en ytterligare fil, så det är inget problem.



I den här katalogen skapar vi en fil som heter "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



I den här filen, infoga den här raden:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Så här tolkar du den här raden:





- `*.*`: innebär att alla Syslog-loggar från Linux-maskinen skickas till Graylog.
- `@`: anger att transporten sker med UDP. Du måste ange "**@@**" för att växla till TCP.
- `192.168.10.220:12514`: anger Address för Graylog-servern och den port som loggar skickas till (motsvarar Input).
- `RSYSLOG_SyslogProtocol23Format`: motsvarar formatet på de meddelanden som ska skickas till Graylog.



När du är klar sparar du filen och startar om Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Efter denna åtgärd bör de första meddelandena anlända till din Graylog-server!



### IV. Visning av Linux-loggar i Graylog



Från Graylog kan du klicka på "**Streams**" och välja din nya ström för att visa relaterade meddelanden. Alternativt kan du klicka på "**Search**" och välja din Steam för att starta en sökning.



Här är några av de viktigaste egenskaperna hos Interface:



**1** - Välj den period för vilken meddelanden ska visas. Som standard visas meddelanden från de senaste 5 minuterna.



**2** - Välj den eller de strömmar som ska visas.



**3** - Aktivera automatisk uppdatering av meddelandelistan (t.ex. var 5:e sekund). Annars är den statisk och du måste uppdatera den manuellt.



**4** - Klicka på förstoringsglaset för att starta sökningen efter att du har ändrat period, ström eller filter.



**5** - Inmatningsfält för att ange dina sökfilter. Här anger jag "**source:srv\-docker**" för att bara visa loggarna från den nya maskinen som jag just har installerat Rsyslog på.



Loggar skickas av Linux-maskinen:



![Image](assets/fr/015.webp)



### V. Identifiera ett SSH-anslutningsfel



Graylogs styrka ligger i dess förmåga att indexera loggar och göra det möjligt att utföra sökningar enligt olika kriterier: källmaskin, Timestamp, meddelandeinnehåll etc. Vi skulle kunna försöka identifiera misslyckade SSH-anslutningar.



Från en fjärrdator (t.ex. Graylog-servern) försöker du ansluta till Linux-servern som du just har konfigurerat Rsyslog på. Du kan till exempel göra så här



```
ssh [email protected]
```



Ange sedan avsiktligt ett felaktigt **användarnamn** och **lösenord** för att **generate anslutningsfel**. I filen "**/var/log/auth.log**" kommer detta att leda till generate-loggmeddelanden som liknar följande:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Du bör hitta dessa meddelanden på Graylog.



I Graylog kan du använda följande sökfilter för att endast visa matchande meddelanden:



```
message:Failed password AND application_name:sshd
```



Om du har flera servrar och vill analysera loggarna för en viss server, anger du dess namn i tillägget:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Här är en översikt över resultatet på en maskin där jag genererade flera anslutningsfel, vid olika tidpunkter på dagen:



![Image](assets/fr/009.webp)



Misslyckade anslutningsförsök görs från maskinen med IP Address "**192.168.10.199**". Om du vill veta mer om aktiviteten hos den här värden kan du **söka efter den här IP Address**. Graylog kommer att mata ut alla loggar där denna IP Address refereras till, på alla värdar (för vilka loggsändning är konfigurerad).



I detta fall kan det filter som ska användas vara:



```
message:"192.168.10.199"
```



Vi får ytterligare resultat (inte förvånande, eftersom vi inte filtrerar på SSH-applikationen):



![Image](assets/fr/008.webp)



### VI. Slutsatser



Genom att följa denna handledning bör du kunna konfigurera en Linux-maskin så att den skickar sina loggar till en Graylog-server. På så sätt kommer du att kunna centralisera loggarna från dina Linux-värdar i din loggsänka!



Om du vill gå ännu längre kan du överväga att skapa instrumentpaneler och varningar för att få meddelanden när en avvikelse upptäcks.



![Image](assets/fr/007.webp)