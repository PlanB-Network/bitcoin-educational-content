---
name: Lynis
description: Utför en säkerhetsgranskning av en Linux-dator med Lynis
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Fares CHELLOUG publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___



## I. Presentation



**I den här handledningen kommer vi att lära oss att utföra en säkerhetsrevision på en Linux-maskin med Lynis! För de av er som inte känner till **Lynis,** är det ett litet kommandoradsverktyg som analyserar din servers konfiguration och ger rekommendationer för att **förbättra säkerheten för din maskin.**



Lynis är ett verktyg med öppen källkod från CISOFY, ett företag som specialiserar sig på **systemrevision och härdning**. Om du vill göra framsteg när det gäller att härda Linux och populära tjänster (SSH, Apache2, etc.) är Lynis din allierade! Lynis berättar inte bara vad som går fel, utan ger också rekommendationer för att peka dig i rätt riktning (och spara tid).



**Lynis** fungerar med de flesta Linux-distributioner, inklusive: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis riktar sig till Linux / UNIX-användare, men är också **macOS**-kompatibelt. Mycket snabb att installera, det finns ingen beroendehantering på paketnivå.



Det används för en mängd olika ändamål:





- Säkerhetsrevisioner
- Test av efterlevnad (PCI, HIPAA och SOX)
- Tuffare systemkonfigurationer
- Upptäckt av sårbarheter



Verktyget används av ett stort antal användare, bland annat systemadministratörer, IT-revisorer och pentesters. För analyser baseras verktyget på standarder som **CIS Benchmark, NIST, NSA, OpenSCAP** och på officiella rekommendationer från **Debian, Gentoo, Red Hat**.



Projektet finns tillgängligt på denna Address på **Github** :





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Ladda ner Lynis från CISOFY] (https://cisofy.com/lynis/#download)



I den här steg-för-steg-handledningen kommer jag att **använda en VPS som kör Debian 12** och jag kommer att koncentrera mig på SSH-delen, eftersom jag vill kontrollera dess konfiguration och förbättra den.



## II. Nedladdning och installation



Det finns flera sätt att ladda ner och installera Lynis. Välj det sätt du föredrar från listan nedan.



### A. Installation från Debians arkiv



Detta installationsläge gör att du kan använda kommandot **lynis** var som helst i systemet, till skillnad från installation från källkod, där du måste befinna dig i katalogen.



Anslut till din server via SSH och ange följande kommandon för att installera Lynis :



```
sudo apt-get update
sudo apt-get install lynis -y
```



Det här är vad du får:



![Image](assets/fr/024.webp)



### B. Ladda ner från den officiella webbplatsen



Du kan också ladda ner den från Cisofys webbplats:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Det här är vad du får:



![Image](assets/fr/032.webp)



Därefter packar vi upp arkivet med hjälp av följande kommando:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Det här är vad du får:



![Image](assets/fr/020.webp)



Låt oss gå till mappen **lynis**:



```
cd lynis
```



Vi kan kontrollera om det finns uppdateringar med följande kommando:



```
./lynis update info
```



Det här är vad du får:



![Image](assets/fr/023.webp)



### C. Ladda ner från GitHub



Vi laddar ner **Lynis** från det officiella GitHub-arkivet med följande kommando (*git* måste finnas på din dator):



```
git clone https://github.com/CISOfy/lynis.git
```



Det här är vad du får:



![Image](assets/fr/060.webp)



## III. Användning av Lynis



Lynis finns på vår maskin, så låt oss lära oss hur man använder den!



### A. Huvudreglage och alternativ



Om du vill visa tillgängliga kommandon skriver du in följande kommando:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
./lynis
```



Det här är vad du får:



![Image](assets/fr/039.webp)



Och du får också följande alternativ:



![Image](assets/fr/040.webp)



För att visa alla tillgängliga kommandon, ange följande kommando:



```
sudo lynis show
```



Det här är vad du får:



![Image](assets/fr/022.webp)



Om du vill visa alla alternativ måste du trycka på :



```
sudo lynis show options
```



Det här är vad du får:



![Image](assets/fr/021.webp)



I resten av den här artikeln kommer vi att lära oss hur du använder vissa alternativ.



### B. Genomföra systemrevisionen



Vi kommer att be **Lynis** att granska vårt system och visa vad som är korrekt konfigurerat och vad som kan förbättras. För att göra detta anger du följande kommando:



```
sudo lynis audit system
# ou
./lynis audit system
```



Om du inte är inloggad som root när du kör det här kommandot kommer verktyget som standard att köras med den inloggade användarens privilegier. Vissa tester kommer inte att köras i detta sammanhang:



![Image](assets/fr/052.webp)



Här är de tester som inte kommer att utföras i detta läge:



![Image](assets/fr/051.webp)



När kommandot har utförts startar analysen. Vänta bara ett ögonblick.



I slutet av granskningen får du detta (vi kan se att **Lynis** korrekt har identifierat **Debian 12**-systemet och kommer att använda **Debian-plugin** för analysen):



![Image](assets/fr/017.webp)



Därefter kommer Lynis att lista en uppsättning punkter som motsvarar allt han har kontrollerat i vårt system. Detta är organiserat efter kategori, som vi kommer att se. Det är också värt att notera att en färgkod används för att markera rekommendationer:





- Röd** för kritiska Elements eller bästa praxis som inte respekteras (t.ex. ett paket som saknas), dvs. din server respekterar inte denna punkt
- Gul** för förslag eller delvis efterlevnad av rekommendationen (låt oss säga att det är ett plus att följa en punkt som är markerad med denna färg (icke-prioriterad))
- Green** för punkter där din serverkonfiguration är kompatibel
- Vit**, när den är neutral



Här kan vi se att Lynis rekommenderar att du installerar **fail2ban**:



![Image](assets/fr/057.webp)



I avsnittet "**Start och tjänster**" ser vi att tjänsteskyddet via *systemd* kan förbättras. På den positiva sidan är Grub2 närvarande och det finns inga problem med behörigheter på :



![Image](assets/fr/029.webp)



Sedan har du avsnitten "**Kernel**" och "**Minne och processer**":



![Image](assets/fr/037.webp)



Därefter avsnittet "**Användare, grupper och autentisering**". Verktyget informerar oss om en varning om behörigheterna i katalogen "**/etc/sudoers.d**". För tillfället vet vi inte mer, men vi kommer att kunna se vad rekommendationen är i slutet av analysen.



![Image](assets/fr/049.webp)



Här är vad du kan hitta i avsnitten "**Shells", "Files Systems" och "USB Devices"**. Vi kan bland annat se att det finns förslag på monteringspunkter och att USB-enheter för närvarande är tillåtna på den här maskinen.



![Image](assets/fr/048.webp)



Därefter avsnitten: "**Name services", "Ports and packages", "Networking".** Här anges att paket som inte längre används kan rensas bort och att det inte finns något verktyg som kan hantera automatiska uppdateringar.



![Image](assets/fr/058.webp)



Vi kan se att en brandvägg är aktiverad (och ja, det finns iptables!). Dessutom kan vi se att den har hittat oanvända regler och att en Apache-webbserver är installerad.



![Image](assets/fr/055.webp)



Detta följs av en analys av själva webbservern, eftersom tjänsten har identifierats.



Vi kan se att den har hittat konfigurationsfiler för **Nginx**, och att för SSL/TLS-delen är **ciphers** konfigurerade med användning av ett protokoll som skulle vara osäkert. Å andra sidan är logghanteringen korrekt enligt Lynis.



![Image](assets/fr/038.webp)



SSH-tjänsten finns på min VPS-server. Dess konfiguration analyseras av Lynis. Det måste sägas att SSH-säkerheten lätt kan förbättras! Vi kommer att återkomma till detta område i detalj när vi har fått rekommendationerna.



![Image](assets/fr/026.webp)



Här är avsnitten **"SNMP Support", "Databases", "PHP", "Squid Support", "LDAP Services", "Logging and files"**.



Det finns ett riktigt viktigt förslag om logghantering: det rekommenderas starkt att du inte bara lagrar loggar lokalt på din maskin. Om maskinen skulle skadas av en angripare är det troligt att han skulle försöka radera sina spår... Så vi måste externalisera loggarna.



![Image](assets/fr/050.webp)



Här har vi granskningen av sårbara tjänster, kontohantering, schemalagda uppgifter och NTP-synkronisering.det indikeras att nivån är låg på banner- och identifieringsdelen: det här är förståeligt, om du visar systemversionen ger det en indikation till en potentiell angripare. Detta är standardinställningen.



Det skulle vara intressant att aktivera **auditd** för att få loggar i händelse av **forensisk** analys. **NTP** kontrolleras också, eftersom det är att föredra att ha system i tid för att kunna söka i loggar på ett effektivt sätt, vilket förenklar sökningen.



![Image](assets/fr/036.webp)



Lynis tittar sedan på kryptografiska Elements, virtualisering, containrar och säkerhetsramverk. Vissa avsnitt är tomma eftersom det inte finns någon korrespondens med den analyserade maskinen. Vi kan dock se att jag har två utgångna SSL-certifikat och att jag inte har aktiverat **SELinux**.



![Image](assets/fr/027.webp)



Även här finns det utrymme för förbättringar: det finns ingen antivirus- eller antimalwareskanner, och vi har förslag på filbehörigheter.



![Image](assets/fr/028.webp)



Därefter fokuserar Lynis på att strama upp konfigurationen av Linux-kärnan (inklusive regler för IPv4-stacken) samt hanteringen av Linux-maskinens "Home"-kataloger.



![Image](assets/fr/035.webp)



Vi har kommit till slutet av analysen... Den här sista punkten visar att vi skulle ha allt att vinna på att ha ClamAV på den här maskinen.



![Image](assets/fr/030.webp)



## IV. Rekommendationer



Efter revisionen är det dags att läsa och analysera rekommendationerna. Det är här vi får rekommendationerna och förklaringarna för vart och ett av de tester som Lynis har utfört.



Ta SSH-rekommendationerna till exempel. ** För varje förslag hittar du den rekommenderade parametern och en länk som förklarar säkerhetspunkten ** Det är upp till dig att bestämma, beroende på sammanhang och användning.



Låt oss ta en titt på några exempel på rekommendationer som direkt återspeglar de punkter som lyfts fram under hela revisionen...



### A. Exempel på rekommendationer





- Som vi såg tidigare är NTP viktigt för tidsstämpling av loggar:



![Image](assets/fr/043.webp)





- Lynis föreslår också att man installerar paketet **apt-listbugs** för att få information om kritiska buggar under paketinstallationer via **apt.**



![Image](assets/fr/041.webp)





- Verktyget föreslår att vi installerar **needrestart för att kunna** se vilka processer som använder en gammal version av biblioteket och behöver startas om.



![Image](assets/fr/054.webp)





- I detta förslag föreslås att **fail2ban** installeras för att automatiskt blockera värdar som inte lyckas autentisera sig (särskilt brute force).



![Image](assets/fr/044.webp)





- För att förstärka systemtjänster rekommenderar han att vi kör kommandot blue för varje tjänst på vår maskin.



![Image](assets/fr/056.webp)





- Han föreslår att man sätter utgångsdatum för alla lösenord till skyddade konton.



![Image](assets/fr/031.webp)





- I det här förslaget föreslås att man anger minimi- och maximivärden för hur gammalt ett lösenord ska vara. Detta säkerställer bland annat att lösenord byts ut regelbundet.



![Image](assets/fr/042.webp)





- Vi rekommenderar att du använder separata partitioner för att begränsa effekterna av problem med diskutrymmet på en partition.



![Image](assets/fr/047.webp)





- Denna rekommendation föreslår att USB-lagring och firewire inaktiveras för att förhindra dataläckage



![Image](assets/fr/033.webp)





- För att uppfylla denna rekommendation behöver du bara installera och konfigurera **unnatended-upgrade**, t.ex.



![Image](assets/fr/053.webp)



### B. Installera rekommenderade paket



För att förbättra systemkonfigurationen kommer vi att installera några paket på maskinen: några som rekommenderas av Lynis, några som jag personligen rekommenderar.



Du kommer att ha en bra grund att arbeta vidare på om du bara lägger lite tid på att konfigurera dem. För att göra detta, se IT-Connect-webbplatsen, andra artiklar på webben och verktygsdokumentation.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Lite information om de installerade paketen :





- Clamav** är ett antivirusprogram.
- unattend-upgrades** gör det möjligt för dig att hantera dina uppdateringar automatiskt och till och med starta om maskinen eller automatiskt rensa bort gamla paket, det är helt konfigurerbart.
- rkhunter** är ett anti-rootkit som skannar ditt filsystem.
- Fail2ban** kommer att basera sig på dina loggfiler enligt vad du ger den att läsa och den kommer att fungera med **iptables**, till exempel för att förbjuda IP-adresser som försöker "brute force" din server i SSH.



### C. Rekommendationer för SSH



Låt oss ta en titt på SSH-rekommendationerna. De är listade nedan. Oroa dig inte, vi kommer omedelbart att förklara hur du kan förbättra konfigurationen.



![Image](assets/fr/034.webp)



Låt oss ta en närmare titt på min nuvarande **SSH**-konfiguration i :**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Den konfiguration som föreslås nedan kan fortfarande optimeras, men ger dig en bra grund. *Observera att jag har tagit bort ett antal kommentarer för att öka läsbarheten*.



Vi kommer att :





- Ändra SSH-anslutningsport (glöm standard 22)
- Öka loggarnas ordrikhetsnivå, från **INFO till VERBOSE**
- Ställ in **LoginGraceTime** till **2 minuter**



Om ingen anslutningsinformation matas in inom två minuter kopplas anslutningen bort.





- Aktivera **striktaModer**



Anger om "sshd" ska kontrollera lägen och ägare för användarens filer samt användarens hemkatalog innan en anslutning valideras. Detta är normalt önskvärt, eftersom nybörjare ibland av misstag lämnar sin katalog eller sina filer fullt tillgängliga för alla. Standardinställningen är "yes".





- Ställ in **MaxAuthtries** till 3



Detta representerar antalet misslyckade autentiseringsförsök innan kommunikationen avslutas.





- Ställ in **MaxSessions** till 2



Detta representerar det maximala antalet samtidiga sessioner.





- Aktivera autentisering med offentlig nyckel



```
PubkeyAuthentication yes
```





- Behåll lösenordsautentisering :



```
PasswordAuthentication yes
```



Förbjud tomma lösenord och **Kerberos**-autentisering, samt **direkt rotautentisering**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Se till att du har "**PermitRootLogin no", om det är lika med "yes" är det "absolut ondska"**.





- Förbjud omdirigering av TCP-anslutning



```
AllowTcpForwarding no
```



Anger om TCP-omdirigeringar är tillåtna, med "yes" som standardinställning. Observera: Om du inaktiverar TCP-videresändningar ökar inte säkerheten om användare har tillgång till ett skal, eftersom de fortfarande kan konfigurera sina egna verktyg för omdirigering.





- Förhindra X11-omdirigering



```
X11Forwarding no
```



Anger om X11-omdirigeringar accepteras, med "nej" som standardinställning. Observera: även om X11-omdirigeringar är inaktiverade ökar inte säkerheten eftersom användare fortfarande kan konfigurera sina egna omdirigeringar. X11-omdirigering inaktiveras automatiskt om **UseLogin** väljs.





- Ställ in timeout för kommunikation mellan klienten och sshd



```
ClientAliveInterval  300
```



Definierar en timeout i sekunder, efter vilken sshd-tjänsten skickar ett meddelande med en begäran om svar från klienten om inga data tas emot från klienten. Som standard är det här alternativet inställt på "0", vilket innebär att dessa meddelanden inte skickas till klienten. Endast version 2 av SSH-protokollet stöder detta alternativ.



```
ClientAliveCountMax 0
```



Enligt [dokumentationen (*man page*) för sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html) betyder det här alternativet följande: "Ställer in antalet hold-meddelanden (se ovan) som ska skickas utan svar från klienten för **sshd**. Om detta tröskelvärde nås medan hold-meddelandena har skickats, kopplar **sshd** bort klienten och avslutar sessionen. Det är viktigt att notera att dessa hold-meddelanden skiljer sig mycket från alternativet **KeepAlive** (nedan). Connection hold-meddelanden skickas genom den krypterade tunneln och är därför inte förfalskningsbara. Connection hold på TCP-nivå som aktiveras av **KeepAlive** är förfalskningsbart. Connection hold-mekanismen är av intresse när klienten eller servern behöver veta om anslutningen är inaktiv."





- Förhindra informationsspridning genom att inaktivera **motd, banner, lastlog**



```
PrintMotd no
```



Anger om sshd ska visa innehållet i filen "/etc/motd" när en användare loggar in i interaktivt läge. På vissa system kan detta innehåll också visas av skalet, via /etc/profile eller en liknande fil. Standardvärdet är "yes".



```
Banner none
```



Det är värt att notera att det i vissa jurisdiktioner kan vara en förutsättning för rättsligt skydd att skicka ett meddelande före autentisering. Innehållet i den angivna filen överförs till fjärranvändaren innan anslutningsbehörighet ges. Det här alternativet måste konfigureras, eftersom inget meddelande visas som standard.



I bilder ger detta :



![Image](assets/fr/019.webp)



### D. Revisionspoäng



Slutligen, låt oss inte glömma att kontrollera **Lynis revisionsresultat**! Vi ser att **min härdningspoäng är 63** och att rapportfilen kan ses i "**/var/log/lynis-report.dat**". Det finns också en fil "**/var/log/lynis.log**".



**Med andra ord, ju högre poäng, desto bättre! Du måste därför arbeta med din konfiguration för att uppnå högsta möjliga poäng, samtidigt som du låter din maskin och dina hostade tjänster fungera normalt (vilket innebär att du måste utföra funktionstester).



![Image](assets/fr/046.webp)



Låt oss ta en titt på resultaten på min andra server, där jag har lagt ner lite mer tid på att härda! Så det är normalt att poängen är högre (**76**).



![Image](assets/fr/045.webp)



## V. Lynis automatiserad planering



**Lynis** erbjuder också möjligheten att köra sina kontroller via en schemalagd uppgift. Det finns faktiskt alternativet **"--cronjob"**, som kommer att köra alla Lynis-tester utan behov av validering eller användaråtgärder. Du kan då mycket enkelt skapa ett skript som kommer att köra **Lynis** och lägga utdata i en tidsstämplad fil med namnet på servern i fråga. Här är en fil av den här typen som du kan lägga i mappen */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



Variabeln **"AUDITOR_NAME"** är helt enkelt en variabel som vi anger i alternativet **"--auditor"** i **Lynis** så att det här namnet visas i rapporten:



![Image](assets/fr/059.webp)



Vi kommer också att skapa några kontextuella variabler som hjälper oss att organisera oss bättre, t.ex. värdnamn och datum för att namnge rapporten och tidsstämpla den, och sökvägen till den mapp där vi vill lägga våra rapporter.



## VI. Slutsatser



Lynis är ett mycket praktiskt verktyg som hjälper dig att spara tid och bli mer effektiv när du vill veta mer om konfigurationen av en Linux-server, särskilt när det gäller säkerhet. Glöm dock inte att varje ändring måste testas innan den tillämpas i produktionen, med hänsyn till din egen användning och ditt sammanhang.



Du kommer förmodligen inte att använda samma konfiguration för en VPS som är exponerad mot nätet, där du bara behöver en SSH-anslutning (eftersom du är den enda personen som ansluter), till skillnad från en **bastion** eller **scheduler** som kommer att behöva multiplicera **SSH.**-anslutningar



När du har fått en konfiguration som passar dig när det gäller härdning är det lämpligt att använda ett automatiseringsverktyg så att du inte behöver göra om uppgifterna manuellt, eftersom det skulle vara tidskrävande och felbenäget. Du kan till exempel använda **: Puppet, Chef, Ansible, etc ... **



Glöm inte att kommunicera med dina team före implementeringen: du måste få dem att förstå varför du gör dessa förändringar, inte bara berätta för dem att du gör dem. I slutändan handlar det om att sprida god praxis, och det ökar dina chanser att lyckas.



Slutligen kan du också jämföra **Lynis** med andra verktyg, av vilka det finns flera. Om du vill gå mot centraliserad hantering och samtidigt behålla öppen källkod rekommenderar jag verktyget [Wazuh] (https://wazuh.com/).



**Den här handledningen är över, ha kul med Lynis!