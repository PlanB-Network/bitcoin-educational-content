---
name: Ntopng
description: Övervaka ditt nätverk med ntopng
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian Duchemin publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___



## I. Presentation



**Oavsett om det handlar om att kontrollera nätverkets fluiditet, få en tydlig bild av användningen eller för prestandastatistik är övervakning av nätverksflödet en viktig del av ett företagsnätverk**. Det hjälper till att förutse förändringar i infrastrukturen och säkerställer användarkvaliteten för användarna (även känt som QoE för *Quality of Experience*, i motsats till QoS).



För att göra detta finns det många tekniker och program/protokoll tillgängliga. Netflow, som utvecklats av Cisco, kan t.ex. användas för att hämta statistik över IP-flöden från en Interface, men användningen är begränsad till kompatibel utrustning.



Därför ska jag i den här handledningen introducera **Ntop** och visa hur du använder det i din infrastruktur för att hålla ett öga på din nätverksanvändning.



Ntop är en programvara med öppen källkod som kan installeras på alla Linux-maskiner. Den är kostnadsfri och kan samla in följande data:





- Utnyttjande av bandbredd
- Huvudsakliga kunder
- Huvudsakliga destinationer
- Använda protokoll
- Använda applikationer
- Portar som används
- Och så vidare.



Den har nu bytt namn till **Ntopng (New Generation)** och erbjuder många grundläggande funktioner kostnadsfritt. Det finns också en kommersiell version som gör det möjligt att exportera konfigurerade varningar till programvara av SIEM-typ eller filtrera trafik med regler som definieras direkt från proben.



## II. Förkunskapskrav



Installationen av en Ntop-probe skiljer sig åt beroende på utrustning och miljö. Därför kommer jag inte att ge dig en steg-för-steg-guide här, utan bara beskriva de olika möjligheterna.



### A. Inbyggt läge



Om du har en pfSense-, OPNSense- eller Endian-brandvägg i produktion, eller till och med en Linux-arbetsstation med NFTables, goda nyheter! Du kan installera Ntopng direkt och börja övervaka dina gränssnitt.



Fördelen med den här tekniken är att den inte kräver någon extra maskinvara. Å andra sidan ökar resursutnyttjandet, så se till att du har tillräcklig maskinvara eller en VM av tillräcklig storlek (minst 2 kärnor och 2BG RAM).



### B. TAP / SPAN-läge



En **tap** är **en nätverksenhet som duplicerar den trafik som passerar genom den och skickar den till en annan enhet.** Fördelen med den här enheten är att den inte kräver någon modifiering av den befintliga infrastrukturen och kan placeras var som helst för att övervaka specifika nätverksdelar, eller mellan core-switchen och edge-routern för att analysera trafik till/från Internet.



Den stora nackdelen med denna typ av utrustning är dess kostnad. I dagens Gigabit-nätverk kan en passiv tap inte fånga upp nätverkstrafiken ordentligt, så du behöver en aktiv enhet som kostar runt 200 euro (minimum).



Läget **SPAN**, även känt som **port mirroring**, används av en switch för att vidarebefordra trafik från en port till en annan. Det här är den metod jag föredrar, eftersom den är enkel att installera och, precis som tap, gör att du kan övervaka en del av nätverket eller hela nätverket när du vill. Det finns dock två nackdelar: switchen måste integrera den här funktionen och dess användning kan öka processorbelastningen på switchen.



### C. Router-läge



Det är fullt möjligt att montera en router under Linux och installera ntopng på den. Den enda nackdelen med den här metoden är att den kommer att ändra ditt nätverk, antingen dess interna adressering eller adresseringen mellan din "riktiga" router och den du lägger till.



Obs: för läsare av artikeln [Skapa en Wifi-router med Raspberry Pi och RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) är det fullt möjligt att installera ntopng på din Rpi för att få korrekt statistik!



### D. Bryggläge



Ett intressant alternativ är att använda **en Linux-maskin i bryggläge.** Placerad mellan två utrustningar gör detta att all trafik kan fångas upp utan att behöva ingripa i konfigurationen av infrastrukturen eller dess utrustning. Eftersom en gammal maskin kan göra jobbet kan kostnaden för denna metod också vara attraktiv. Observera att för att vara optimal bör enheten ha tre nätverkskort, två i bryggläge, ett för att komma åt Interface och SSH. Det är möjligt att använda bara två kort, men då kommer även enhetens administrationstrafik att fångas upp...



Så det är **detta sista läge som jag ska använda**. Av praktiska skäl kommer jag att använda virtuella maskiner för demonstrationen, men metoden förblir densamma för användning på fysiska maskiner.



## III. Förberedelse av sond med Interface-brygga



För proben väljer jag en **Debian 11**-maskin med minimal installation.



Första steget, alltid samma sak, uppdatera:



```
apt-get update && apt-get upgrade
```



Installera sedan paketet **bridge-utils**, som gör det möjligt för oss att skapa vår bro:



```
apt-get install bridge-utils
```



Efter installationen är det första vi bör notera det aktuella namnet på våra nätverkskort. Under Debian kan detta namn ta flera former, och vi behöver det för konfigurationen.



Ett enkelt **ip add**-kommando ger en utdata med denna information:



![Image](assets/fr/016.webp)



Här ser jag 3 gränssnitt:





- Lo**: detta är loopback Interface; det är en virtuell Interface som "loopar" över utrustningen. I grund och botten används denna Interface, vars Address är 127.0.0.1 (även om vilken Address som helst i 127.0.0.0/8 duger, eftersom detta intervall är reserverat för detta ändamål) för att kontakta själva utrustningen. Om du har installerat en webbplats på din arbetsstation (t.ex. med WAMPP) har du förmodligen använt "*localhost*" Address någon gång för att visa webbplatsen som finns på din egen maskin. Detta värdnamn är associerat med Address 127.0.0.1 och därför med Interface loopback.
- ens33**: detta är min första Interface, som fick en Address här från min DHCP
- ens36**: min andra Interface



Nu när jag har all information kan jag ändra filen */etc/network/interfaces* för att skapa min brygga. Så här ser det ut för närvarande (kan variera):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Den första delen gäller min loopback Interface, som jag inte kommer att röra, följt av Interface ens33. Modifieringarna innebär att jag lägger till min andra Interface (ens36) och konfigurerar bryggan med dessa två gränssnitt:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Här följer några förklaringar till dessa första förändringar:





- auto *Interface***: "startar" Interface automatiskt vid systemstart
- iface *Interface* inet manual**: för att använda Interface utan någon IP Address. Som nyckelordet "static" för att definiera en statisk IP Address eller "dhcp" för att använda dynamisk adressering



Modifieringarna fortsätter:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Här igen, några förklaringar:





- iface br0 inet static**: här har jag definierat min Interface-brygga (*br0*) med en statisk Address.
- Address, nätmask, gateway**: information om kortadressering
- bridge_ports**: gränssnitt som ska ingå i bryggan
- bridge_stp**: Spanning Tree-protokollet används vid sammankoppling av switchar för att upptäcka redundanta länkar och undvika loopar. Eftersom en brygga kan sättas in mellan två nätverksvägar kan den vara källan till en loop, därav möjligheten att aktivera detta protokoll. Jag behöver det inte här, så jag inaktiverar det.



Spara ändringarna och starta om nätverket:



```
systemctl restart networking
```



För att kontrollera ändringarna kan du visa resultatet av kommandot **ip** add igen:



![Image](assets/fr/021.webp)


Du kan tydligt se **min nya Interface "*br0*" med IP Address som jag har tilldelat den.** Förresten kan du också se att mina två fysiska gränssnitt verkligen är "UP", men inte har någon IP Address.



## IV. Installera NtopNG



Nu när vår probe kan sniffa trafik mellan mitt nätverk och routern återstår bara att installera ntopng. För att göra detta ändrar du först filen */etc/apt/sources.list* och lägger till **contrib** i slutet av varje rad som börjar med **deb** eller **deb-src**.



Som standard innehåller paketkällor endast paket som följer DFSG (*Debian Free Sotftware Guidelines*), identifierade med nyckelordet **main**. Du kan även lägga till dessa källor:





- contrib**: paket som innehåller DFSG-kompatibel programvara, men som använder beroenden som inte är en del av **main**-grenen
- non-free**: innehåller paket som inte är DFSG-kompatibla



Exempel på en rad i /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Så jag kommer bara att lägga till ordet **contrib** till rader som dessa.



Resten av stegen finns listade på [NtopNG]-webbplatsen (https://packages.ntop.org/apt/) där du, för Debian 11, måste lägga till Ntop-källorna för framtida installation. Detta tillägg automatiseras genom att använda en:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Sedan kommer den faktiska installationsfasen:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Det första kommandot raderar cacheminnet för pakethanteraren apt. Det andra kommer att uppdatera paketlistan och det tredje kommer att installera NtopNG.



Efter installationen är **NtopNG-programvaran direkt tillgänglig på port 3000 i Debian-maskinen**. Så för mig är det `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



NtopNG hemsida



Standardinloggningen och lösenordet visas, så allt du behöver göra är att ange dem!



## V. Användning av NtopNG



När du loggar in första gången är det första du blir ombedd att göra att ändra standardlösenordet för administratören och språket. Tyvärr är franska inte ett av dem.



Du kommer sedan fram till instrumentpanelen:



![Image](assets/fr/023.webp)



NtopNG instrumentpanel



Vänj dig inte vid den här! Om du lägger märke till den gula rutan längst upp på skärmen ser du meningen: "*Licensen löper ut 04:57*". Som standard startar installationen en testversion av den fullständiga versionen av NtopNG, men under en (mycket) begränsad tid. När denna "nedräkning" har uppnåtts aktiveras *community*-versionen och instrumentpanelen ändras:



![Image](assets/fr/024.webp)



Ny instrumentpanel för NtopNG:s community



Det första du ska göra är att **kontrollera att rätt Interface lyssnar**. I det övre vänstra hörnet finns en rullgardinslista med tillgängliga gränssnitt där du kan välja den Interface som vi är intresserade av här: br0



![Image](assets/fr/025.webp)



Interface urval



I det nya fönstret visas "Top Flaw Talkers", dvs. de enheter som kommunicerar mest. Här har jag bara två stationer som visas:



![Image](assets/fr/026.webp)



** Källvärdar visas till vänster, destinationer till höger ** Detta gör att du kan visualisera användningen av den totala bandbredden för varje värd och få en övergripande bild av nätverkstrafiken. Det är inte illa, men vi kan gå längre...



Om jag t.ex. klickar på "*Hosts*" får jag upp en graf som visar strömförbrukningen för sändning och mottagning för varje host i mitt nätverk. Här kan jag till exempel se att 192.168.1.37 ensam står för 80% av min trafik:



![Image](assets/fr/027.webp)



Om jag klickar på IP Address för värden i fråga omdirigeras jag till en sammanfattningssida:



![Image](assets/fr/028.webp)



Jag kan till exempel se att det är en VMWare-maskin (genom att känna igen JA:et på min MAC Address), att den heter DESKTOP-GHEBGV1 (så det är säkert en Windows-värd) OCH jag har **statistik över mottagna och skickade paket samt mängden data**.



Du kommer också att märka en ny meny högst upp i denna sammanfattning. Jag föreslår att du klickar på "**Apps**" för att se vad som driver så mycket trafik:



![Image](assets/fr/017.webp)


Ha, det ser ut som om vi har ett svar! På grafen till vänster, ** ser vi att 76,6% av dess trafik kommer från ... Windows Update**, så den här värden laddar ner uppdateringar!



NtopNG använder en teknik som kallas DPI för *Deep Packet Inspection*, vilket gör det möjligt att kategorisera varje nätverksflöde och definiera applikationen (eller familjen av applikationer) bakom det.



För att demonstrera detta startar jag en YouTube-video på min host:



![Image](assets/fr/018.webp)



**Trafiken identifierades och kategoriserades omedelbart!



Observera: av uppenbara skäl kan den här typen av programvara ge upphov till integritetsfrågor, så var noga med att använda den under rätt förhållanden. Observera också att det är möjligt att **anonymisera resultat**, alternativet finns i **Inställningar > Inställningar > Övrigt** och heter "**Mask Host IP Address**".



## VI. Detektioner och varningar



NtopNG kan också utfärda säkerhetsvarningar för vissa flöden. Dessa finns i menyn **Alerts**, på vänster banner. Här har jag till exempel totalt 2851 varningar, indelade i olika allvarlighetsgrader: Notice (meddelande), Warning (varning) och Error (fel).



![Image](assets/fr/019.webp)



Låt oss ta en titt på varningarna med hög kritikalitet, jag har 17 av dem!



Om du klickar på den här figuren får du upp detaljerna i varningarna. Det finns inget alarmerande här, det är ett falskt positivt resultat, nedladdningen av uppdateringar kategoriseras som en binär filöverföring i en HTTP-ström, vilket verkligen kan innebära en attack.



![Image](assets/fr/020.webp)



Men eftersom jag använder gratisversionen kan jag inte utesluta domäner eller värdar som är källan till varningar, så du måste hålla ett öga på dem för att undvika att missa något mycket mer oroande. NtopNG kommer att generate varningar i händelse av:





- Nedladdning av binär fil via HTTP
- Misstänkt DNS-trafik
- Använda en port som inte är standard
- Detektering av SQL-injektioner
- Skript på flera webbplatser (XSS)
- Och så vidare.



## VII. Slutsatser



I den här handledningen har vi sett **hur man ställer in en probe med NtopNG** som gör det möjligt för oss att **analysera vår nätverkstrafik** för att visualisera protokollanvändning och beläggningen för varje värd, men också upptäcka misstänkt trafik.



Tyvärr kan jag inte täcka alla funktioner och möjligheter i den här artikeln, men känn dig fri att utforska!



Den här lösningen kan implementeras permanent i ett företags infrastruktur. NtopNG kan också exportera resultat till en InfluxDB-databas, vilket gör att du kan skapa dina egna instrumentpaneler med ett tredjepartsverktyg som Graphana.