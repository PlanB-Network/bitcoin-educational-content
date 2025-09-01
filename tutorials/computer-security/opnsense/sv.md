---
name: OPNsense
description: Hur installerar och konfigurerar jag en OPNsense-brandvägg?
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian BURNEL publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___



## I. Presentation



I den här handledningen tar vi en titt på OPNsense brandvägg med öppen källkod. Vi tittar på dess huvudfunktioner, förutsättningarna och hur man installerar den här FreeBSD-baserade lösningen.



Innan vi sätter igång bör du veta att **OPNsense och pfSense båda är brandväggar med öppen källkod** baserade på FreeBSD. Vi kan säga att pfSense är OPNsense's storebror på sätt och vis, eftersom den senare är en Fork som skapades 2015. Slutligen är det viktigt att påpeka att **OPNsense sedan 2017 har bytt till HardenedBSD istället för FreeBSD**. HardenedBSD är en förbättrad version av FreeBSD, med avancerade säkerhetsfunktioner



OPNsense utmärker sig genom sin modernare användar-Interface och **mer frekventa uppdateringskadens**. Faktum är att OPNsense uppdateringsschema innehåller två större utgåvor per år, som uppdateras varannan vecka eller så (vilket resulterar i mindre utgåvor). Denna uppföljning är mycket intressant i jämförelse med pfSense, om vi tittar på community-versionerna av dessa lösningar.



![Image](assets/fr/050.webp)



## II. OPNsense-funktioner



OPNsense är ett operativsystem som är utformat för att fungera som en brandvägg och router, även om funktionerna är många och kan utökas genom att installera ytterligare paket. Det är lämpligt för produktionsanvändning och används främst för nätverkssäkerhet och flödeshantering.



### A. Huvudsakliga egenskaper



Här är några av OPNsense's viktigaste funktioner:





- Brandvägg och NAT**: OPNsense tillhandahåller avancerad stateful brandväggsfunktionalitet med stateful filtrering samt NAT-funktioner (Network Address Translation).





- DNS/DHCP**: OPNsense kan konfigureras för att hantera DNS- och DHCP-tjänster i nätverket. Den kan fungera som en DHCP-server, men kan också användas som en DNS-resolver för maskiner i det lokala nätverket. Dnsmasq är också integrerat som standard.





- VPN**: OPNsense stöder flera VPN-protokoll, inklusive IPsec, OpenVPN och WireGuard, vilket möjliggör säkra anslutningar för fjärråtkomst till mobila arbetsstationer eller sammankoppling av webbplatser.





- Webbproxy**: OPNsense innehåller en webbproxy för att kontrollera och filtrera internetåtkomst. Den kan också användas för att filtrera innehåll och hantera nätverksåtkomst.





- Hantering av bandbredd (QoS)**: OPNsense erbjuder QoS-hanteringsfunktioner (Quality of Service) för att prioritera nätverkstrafik och bättre hantera nätverksbandbredd.





- Captive portal**: Med den här funktionen kan du hantera användarnas åtkomst till nätverket via en autentiseringssida (lokal bas, vouchers etc.). Det är en funktion som ofta används för offentliga Wi-Fi-nätverk.





- IDS/IPS**: OPNsense integrerar Suricata för att erbjuda funktioner för upptäckt och förebyggande av intrång (IDS/IPS) för att skydda nätverket mot attacker.





- Hög tillgänglighet (CARP)**: OPNsense har stöd för CARP (*Common Address Redundancy Protocol*) för hög tillgänglighet mellan flera OPNsense-brandväggar, vilket säkerställer att tjänsten förblir aktiv även vid maskinvarufel.





- Rapportering och övervakning**: OPNsense tillhandahåller rapporterings- och övervakningsverktyg i realtid för att spåra nätverksprestanda (med NetFlow) och upptäcka potentiella problem tack vare skapandet av loggar. Detta inkluderar grafik. Verktyget Monit är integrerat i OPNsense och möjliggör övervakning av själva brandväggen.



### B. Ytterligare paket



Detta är bara en översikt över de funktioner som OPNsense erbjuder. Med hjälp av **paketkatalogen** som finns tillgänglig från OPNsense-administrationen Interface kan du dessutom **berika brandväggen med ytterligare funktioner**. Dessa inkluderar en ACME-klient, en Wazuh-agent, NTP Chrony-tjänsten och Caddy som en omvänd proxy.



![Image](assets/fr/051.webp)



## III. Förutsättningar för OPNsense



Först och främst måste du bestämma var du ska installera OPNsense. Det finns flera möjliga lösningar, inklusive installation på:





- En hypervisor som en virtuell maskin, oavsett om det är Hyper-V, Proxmox, VMware ESXi etc.
- En maskin som ett *bare-metal*-system. Det kan vara en minidator som fungerar som brandvägg.



Du kan också köpa **en OPNsense rackmonterbar apparat** via vår webbutik.



Du måste ta hänsyn till de maskinvaruresurser som krävs för att köra OPNsense. Detta beskrivs närmare på [den här dokumentationssidan] (https://docs.opnsense.org/manual/hardware.html).



**Minsta och rekommenderade resurser för produktion: **



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Slutligen beror **dina resurskrav framför allt på antalet anslutningar som ska hanteras**, och därmed på **dina bandbreddskrav**. Dessutom måste du **ha i åtanke de tjänster som kommer att aktiveras och användas** (proxy, intrångsdetektering, etc.) eftersom de kan vara CPU- och/eller RAM-krävande.



Du behöver också ISO-avbildningen för OPNsense-installationen, som du kan hämta från [den officiella webbplatsen] (https://opnsense.org/download/). För installation på en virtuell dator väljer du "**dvd**" som avbildningstyp för att få en ISO-avbildning (och gör vad du vill med den...). För installation via en startbar USB-nyckel, välj alternativet "**vga**" för att få en "**.img**"-fil.



![Image](assets/fr/048.webp)



Du behöver också en dator för att administrera och testa OPNsense.



## IV. Målkonfiguration



Vårt mål är att





- Skapa ett internt virtuellt nätverk (192.168.10.0/24 - LAN)**, som kan komma åt Internet via OPNsense-brandväggen. För produktionsanvändning kan detta vara ditt lokala nätverk, kabel och/eller Wi-Fi.
- Aktivera och konfigurera NAT** så att virtuella datorer i det interna virtuella nätverket kan komma åt Internet
- Aktivera och konfigurera DHCP-servern på OPNsense** för att distribuera en IP-konfiguration till framtida maskiner som är anslutna till det interna virtuella nätverket
- Konfigurera brandväggen** så att den endast tillåter utgående flöden från LAN till WAN i HTTP (80) och HTTPS (443).
- Konfigurera brandväggen** så att det virtuella LAN:et kan använda OPNsense som DNS-resolver (53).



Om du använder Hyper-V-plattformen kommer du att få följande bild:



![Image](assets/fr/033.webp)



## V. Installera OPNsense-brandväggen



### A. Förbereda den startbara USB-nyckeln



Det första steget är att förbereda installationsmediet: **den startbara USB-nyckeln med OPNsense**. Detta är naturligtvis valfritt om du arbetar i en virtuell miljö, men i vilket fall som helst måste du ladda ner ISO-bilden för OPNsense-installationen.



Efter nedladdningen får du **ett arkiv som innehåller en bild i formatet ".img"**. Du kan **skapa ett startbart USB-minne** med olika applikationer, inklusive **balenaEtcher**: ultraenkelt att använda. Dessutom kommer programmet att känna igen bilden i arkivet, så du behöver inte dekomprimera den i förväg.





- [Ladda ner balenaEtcher] (https://etcher.balena.io/)



När programmet är installerat väljer du din bild, ditt USB-minne och klickar sedan på "Flash! Vänta ett ögonblick.



![Image](assets/fr/049.webp)



Nu är du redo att installera.



### B. Installera OPNsense-systemet



Starta maskinen som är värd för OPNsense. Du bör se en välkomstsida som liknar den nedan. Under några sekunder kommer den skärm som visas att vara synlig i fönstret. Låt processen gå sin gilla gång...



![Image](assets/fr/019.webp)



OPNsense-bilden laddas in i maskinen så att systemet kan nås i "**live**"-läge, dvs. tillfälligt lagrat i minnet.



![Image](assets/fr/025.webp)



Då kommer du till en Interface som liknar den nedan. Logga in med inloggning "**installer**" och lösenord "**opnsense**". Observera att tangentbordet är **QWERTY** för tillfället. Nu ska vi **starta installationsprocessen för OPNsense**.



![Image](assets/fr/026.webp)



En ny guide visas på skärmen. Det första steget är att välja den tangentbordslayout som motsvarar din konfiguration. För ett AZERTY-tangentbord väljer du alternativet "**French (accent keys)**" i listan och dubbelklickar sedan på**.



![Image](assets/fr/027.webp)



Det andra steget är att välja den uppgift som ska utföras. Här ska vi utföra en installation med hjälp av filsystemet **ZFS**. Placera dig på raden "**Install (ZFS)**" och bekräfta med **Enter**.



![Image](assets/fr/028.webp)



I det tredje steget väljer du "**stripe**" eftersom vår maskin är utrustad med **enbart en disk**: det finns ingen möjlighet till redundans för att säkra brandväggens lagring och dess data. Detta är särskilt relevant vid installation på en fysisk maskin för att skydda mot maskinvarufel på en disk, via RAID-principen.



![Image](assets/fr/029.webp)



I det fjärde steget trycker du bara på **Enter** för att bekräfta.



![Image](assets/fr/030.webp)



Bekräfta slutligen genom att välja "**YES**" och sedan trycka på **Enter**.



![Image](assets/fr/031.webp)



Nu måste du vänta medan OPNsense installeras... Denna process tar cirka 5 minuter.



![Image](assets/fr/032.webp)



När installationen är klar kan vi ändra lösenordet "**root**" innan vi startar om. Välj "**Root Password**", tryck på **Enter** och ange lösenordet "**root**" två gånger.



![Image](assets/fr/020.webp)



Välj slutligen "**Complete Install**" och tryck på **Enter**. Ta tillfället i akt att **mata ut disken från VM:ns DVD-enhet**. I VM-inställningarna kan du också ställa in den första uppstarten till disk.



![Image](assets/fr/021.webp)



Den virtuella maskinen kommer att starta om och ladda OPNsense-systemet från disken, eftersom vi just har installerat det. Logga in med kontot "root" i konsolen och ditt nya lösenord (annars är standardlösenordet "**opnsense**").



### D. Länka samman nätverksgränssnitt



Skärmen som visas nedan kommer att visas. Välj "**1**" och tryck på **Enter** för att associera maskinens nätverkskort med OPNsense-gränssnitten.



![Image](assets/fr/022.webp)



Först ber guiden dig att konfigurera länkaggregering och VLAN. Ange "**n**" för att vägra, och bekräfta varje gång ditt svar med **Enter**. Därefter måste du tilldela de två gränssnitten "**hn0**" och "**hn1**" till **WAN** och **LAN**. I princip motsvarar "**hn0**" WAN och den andra Interface motsvarar LAN.



Så här fungerar det:



![Image](assets/fr/023.webp)



Vi har nu:





- Interface **LAN** associerat med nätverkskortet "**hn1**" och med OPNsense standard IP Address, dvs. **192.168.1.1/24**.
- Interface **WAN** associerad med nätverkskortet "**hn0**" och med en IP Address hämtad via **DHCP** i det lokala nätverket (tack vare vår externa virtuella switch).



Som standard är OPNsense-administrationen Interface endast åtkomlig från LAN Interface, av uppenbara säkerhetsskäl. Du måste därför ansluta till brandväggens LAN Interface för att utföra administration. Om detta inte är möjligt kan du tillfälligt administrera OPNsense från WAN. Detta innebär att brandväggsfunktionen inaktiveras.



Detta gör du genom att växla till shell-läge med alternativet "**8**" och köra följande kommando:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Tillgång till OPNsense Interface-hanteringssystemet



OPNsense Administration Interface kan nås via HTTPS, med hjälp av IP Address i LAN** Interface (eller WAN). Din webbläsare kommer att ta dig till en inloggningssida. Logga in med kontot "root" och lösenordet som du valde tidigare.



![Image](assets/fr/034.webp)



Vänta några sekunder... Du kommer att uppmanas att följa en guide för att utföra den grundläggande konfigurationen. Klicka på "**Nästa**" för att fortsätta.



![Image](assets/fr/036.webp)



Det första steget är att definiera värdnamnet, domännamnet, välja språk och definiera den eller de DNS-servrar som ska användas för namnupplösning. Om du behåller alternativet "**Enable Resolver**" kan brandväggen användas som en DNS-resolver, vilket är användbart för maskinerna i vårt virtuella LAN.



![Image](assets/fr/037.webp)



Fortsätt till nästa steg. Guiden ger dig möjlighet att **definiera en NTP-server för synkronisering av datum och tid**, även om det redan finns servrar konfigurerade som standard. Dessutom är det viktigt att välja den tidszon som motsvarar din geografiska plats (om du inte har särskilda krav).



![Image](assets/fr/038.webp)



Sedan kommer ett viktigt steg: **konfigurera Interface WAN**. För närvarande är den konfigurerad i DHCP och kommer att förbli i detta konfigurationsläge, såvida du inte vill ställa in en statisk IP Address.



![Image](assets/fr/039.webp)



På konfigurationssidan för Interface WAN måste du avmarkera alternativet "**Blockera åtkomst till privata nätverk via WAN**" om nätverket på WAN-sidan använder privat adressering. Detta kommer förmodligen att vara fallet om du driver ett labb, och kan därför hindra dig från att komma åt Internet.



![Image](assets/fr/040.webp)



Därefter kan du **definiera ett "root"**-lösenord, men det är valfritt eftersom vi redan har gjort det.



![Image](assets/fr/041.webp)



Fortsätt till slutet för att starta omladdningen av konfigurationen. Om du behöver fortsätta att ta kontroll via WAN startar du om kommandot ovan när processen är klar.



![Image](assets/fr/042.webp)



Det är allt som finns att säga!



![Image](assets/fr/035.webp)



### E. DHCP-konfiguration



Vårt mål är att använda OPNsense DHCP-server för att distribuera IP-adresser på det virtuella LAN. För att göra detta måste vi komma åt den här menyplatsen:



```
Services > ISC DHCPv4 > [LAN]
```



**Som du ser är DHCP redan aktiverat som standard på LAN ** Om du inte är intresserad av den här tjänsten bör du inaktivera den. Även om den redan är aktiverad och vi vill använda den, är det viktigt att se över konfigurationen.



Om det behövs kan du ändra intervallet för IP-adresser som ska distribueras: **192.168.10.10** till **192.168.10.245**, beroende på aktuella inställningar.



![Image](assets/fr/046.webp)



Vi kan också se att fälten "**DNS servers**", "**Gateway**", "**Domain name**" etc. är tomma som standard. Faktum är att det finns ett automatiskt arv av vissa alternativ och standardvärden för dessa olika fält. För DNS-servern kommer t.ex. IP Address i Interface LAN att distribueras, vilket gör att OPNsense-brandväggen kan användas som DNS-resolver.



Spara konfigurationen efter eventuella ändringar, om det behövs.



![Image](assets/fr/047.webp)



För att testa DHCP-servern måste du ansluta en maskin till din brandväggs LAN-nätverk.



Denna maskin måste få en IP Address från OPNsense DHCP-server, och vår maskin måste ha tillgång till nätverket. Internetåtkomst måste fungera. Observera att om du har inaktiverat brandväggsfunktionen för att komma åt OPNsense från WAN, kommer detta att inaktivera NAT, vilket hindrar dig från att komma åt webben.



**Anmärkning**: aktuella utfärdade DHCP-avtal är synliga från OPNsense-administrationen Interface. För att göra detta, gå till följande plats: **Tjänster > ISC DHCPv4 > Hyresavtal**.



![Image](assets/fr/045.webp)



### F. Konfigurera NAT- och brandväggsregler



Den goda nyheten är att vi nu kan komma åt OPNsense-administrationen Interface från LAN.



```
https://192.168.1.10
```



Efter att ha loggat in på OPNsense, låt oss upptäcka NAT-konfigurationen. Gå till den här platsen: **Brandvägg > NAT > Utgående**. Här kan du välja mellan automatisk (standard) och manuell skapande av utgående NAT-regler.



Välj automatiskt läge via alternativet "**Automatisk generering av utgående NAT-regler**" och klicka på "**Spara**" (i princip är den här konfigurationen redan den aktiva). I det automatiska läget skapar OPNsense själv en NAT-regel för vart och ett av dina nätverk.



![Image](assets/fr/043.webp)



För närvarande kan alla datorer som är anslutna till det virtuella LAN:et "**192.168.10.0/24**" komma åt Internet utan begränsningar. Vårt mål är dock att begränsa åtkomsten till WAN till HTTP- och HTTPS-protokoll samt DNS på brandväggens Interface LAN.



Så vi måste skapa brandväggsregler ... Bläddra i menyn på följande sätt: **Brandvägg > Regler > LAN**.



**Som standard finns det två regler för att godkänna all utgående LAN-trafik, i IPv4 och IPv6**. Avaktivera dessa två regler genom att klicka på pilen Green längst till vänster, i början av varje rad.



Skapa sedan tre nya regler för att auktorisera **LAN-nätverket** (dvs. "**LAN-nätverket**") till:





- nå alla destinationer med hjälp av **HTTP**.
- nå alla destinationer med **HTTPS**.
- begära **OPNsense** på dess **Interface LAN** (dvs. "**LAN Address**"), via **DNS-protokollet** (detta innebär att brandväggen används som DNS), annars auktorisera din DNS-resolver via dess IP Address.



Detta ger följande resultat:



![Image](assets/fr/044.webp)



Allt som återstår är att klicka på "**Apply changes**" för att flytta över de nya brandväggsreglerna till produktionen. **Observera att alla flöden som inte uttryckligen är auktoriserade kommer att blockeras som standard



LAN-maskinen kan komma åt Internet med hjälp av HTTP och HTTPS. Alla andra protokoll kommer att blockeras.



![Image](assets/fr/018.webp)



## IV. Slutsatser



Genom att följa den här guiden kan du installera OPNsense och komma igång direkt. OPNsense erbjuder ett brett utbud av funktioner för att säkra och hantera din nätverkstrafik på ett effektivt sätt och är lämplig för användning i professionella miljöer.



Den här installationen är bara början: utforska gärna menyerna och konfigurera andra funktioner för att anpassa OPNsense till dina behov.