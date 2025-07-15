---
name: pfSense
description: Installera Pfsense
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian BURNEL publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Stora ändringar har gjorts i författarens originaltext för att uppdatera handledningen.*



___



![Image](assets/fr/027.webp)



## I. Presentation



pfSense är ett kostnadsfritt operativsystem med öppen källkod som förvandlar vilken dator, dedikerad server eller hårdvaruappliance som helst till en högpresterande och konfigurerbar router och brandvägg. PfSense baseras på FreeBSD och är känt för sin stabila och robusta nätverksarkitektur. I över femton år har pfSense satt standarden för brandväggar med öppen källkod för företag, lokala myndigheter och krävande hemanvändare.



Dess huvudfunktioner har utvecklats avsevärt under åren och har förbättrats med varje ny version. Hittills erbjuder pfSense :





- Komplett, centraliserad administration via en modern, intuitiv och säker Interface-webb Interface.
- Högpresterande stateful-brandvägg med avancerat NAT-stöd (inklusive NAT-T) och detaljerad regelhantering.
- Native multi-WAN-stöd, vilket möjliggör aggregering eller redundans av Internetanslutningar.
- Integrerad DHCP-server och relä.
- Hög tillgänglighet tack vare CARP-protokollet för failover och möjligheten att konfigurera pfSense-kluster.
- Lastbalansering mellan flera anslutningar eller servrar.
- Fullständigt VPN-stöd: IPsec, OpenVPN och WireGuard (ersätter L2TP, som nu är föråldrat).
- Konfigurerbar captive portal för åtkomstkontroll för gäster, särskilt i offentliga miljöer eller hotellmiljöer.



pfSense har också ett utbyggbart paketsystem som gör det enkelt att lägga till avancerade funktioner som en transparent proxy (Squid), URL-filtrering eller IDS/IPS (Snort eller Suricata) direkt från Interface-webben.



pfSense distribueras endast för 64-bitars plattformar, i enlighet med gällande FreeBSD-rekommendationer. Det kan installeras på standardhårdvara (PC, rackservrar) eller på inbäddade plattformar med låg effekt, t.ex. Netgate-apparater eller vissa x86-boxar med låg profil, som är mycket kraftfullare än äldre Alix-boxar.



Slutligen är det värt att komma ihåg att pfSense kräver minst två fysiska nätverksgränssnitt: ett som är dedikerat till den externa zonen (WAN) och ett som är dedikerat till det interna nätverket (LAN). Beroende på komplexiteten i din infrastruktur (DMZ, VLAN, flera WAN) kan det krävas flera ytterligare gränssnitt för att dra full nytta av dess funktioner.



## II. Ladda ner bild



Den senaste stabila versionen av pfSense, vid tidpunkten för att skriva denna handledning, är 2.8 (släppt i juni 2025). Du kan ladda ner ISO-bilden eller installationsfilen som är anpassad till din hårdvarumiljö direkt från den officiella webbplatsen :





- [Ladda ner pfSense] (https://www.pfsense.org/download/)



Nedladdningsportalen gör att du kan välja :





- Arkitektur (i allmänhet **AMD64** för all modern hårdvara).
- Typ av bild (**Installer USB Memstick** för installation via USB-minne, **ISO Installer** för bränning eller virtuell redigering).
- Närmaste nedladdningsspegel för att optimera överföringshastigheten.



För dem som vill distribuera pfSense i en virtualiserad miljö (Proxmox, VMware ESXi, VirtualBox ...) finns också en **OVA**-bild tillgänglig. Den här färdiga virtuella maskinen förenklar installationen och den första konfigurationen avsevärt. Se bara till att du justerar de tilldelade resurserna (CPU, RAM, nätverksgränssnitt) enligt den förväntade belastningen och din nätverkstopologi.



Före installation rekommenderar vi att du kontrollerar integriteten hos den nedladdade filen genom att verifiera **SHA256** som tillhandahålls på den officiella nedladdningssidan. Detta säkerställer att bilden inte har ändrats eller korrumperats.



## III. Installation



I det här exemplet utförs installationen på en virtuell maskin som kör VirtualBox. Proceduren är helt identisk på en fysisk maskin eller någon annan hypervisor, med undantag för hanteringen av virtuella enheter.



### 1. Minimikrav för hårdvara



För en standarddistribution rekommenderar vi :





- minst 1 GB RAM** (2 GB eller mer rekommenderas för att aktivera ytterligare paket eller ZFS-stöd).
- 8 GB diskutrymme** (20 GB eller mer är att föredra för mer avancerade konfigurationer, särskilt om du installerar en proxy-cache, IDS/IPS eller detaljerade loggar).
- Minst två virtuella nätverksgränssnitt** (ett för WAN och ett för LAN). I VirtualBox lägger du till dem i VM-inställningarna före start.



### 2. Start av installationsprogrammet



Montera den nedladdade ISO-bilden som en virtuell optisk enhet i VirtualBox, eller sätt i USB-nyckeln om du installerar på en fysisk maskin. Vid uppstart visas en startmeny:



Om du inte väljer några alternativ kommer pfSense automatiskt att starta med standardalternativen efter några sekunder. Tryck på "**Enter**"-knappen för att starta den normala uppstarten.



![Image](assets/fr/027.webp)



När huvudmenyn visas trycker du snabbt på knappen "**I**" för att starta installationen.



![Image](assets/fr/001.webp)



### 3. Initiala installatörsinställningar



På den första skärmen kan du ställa in några regionala parametrar, t.ex. teckensnitt och teckenkodning. Dessa inställningar är användbara i särskilda fall (icke-standardiserade tangentbord, seriella skärmar, orientaliska språk). För de flesta installationer behåller du standardvärdena och väljer "**Accept these Settings**".



![Image](assets/fr/002.webp)



### 4. Val av installationssätt



Välj "**Quick/Easy Install**" för att köra en automatiserad installation med de rekommenderade alternativen. Med den här metoden raderas den valda disken och pfSense konfigureras med standardpartitioneringen.



![Image](assets/fr/003.webp)



En varning visas som anger att alla data på disken kommer att raderas. Bekräfta med "**OK**".



Installationsprogrammet kopierar sedan de nödvändiga filerna till disken. Beroende på din maskinvara kan detta ta från några sekunder till några minuter.



### 5. Urval av kärnor



När installationsprogrammet uppmanar dig att välja kärntyp ska du låta "**Standard Kernel**" vara valt. Denna generiska kärna är perfekt lämpad för standarddistributioner, oavsett om det är på en PC, server eller VM.



### 6. Avsluta installationen och starta om



När installationen är klar väljer du "**Reboot**" för att starta om din maskin på din nya pfSense-instans.



**Viktigt**: Ta bort ISO-imagen eller koppla bort USB-nyckeln för installation innan du startar om, för att undvika att installationsprogrammet startas om nästa gång du startar.



## IV. Starta pfSense för första gången



Vid första uppstarten måste pfSense konfigureras för att känna igen och korrekt tilldela sina nätverksgränssnitt (WAN, LAN, DMZ, VLAN, etc.). En noggrann identifiering av dina nätverkskort är nödvändig för att undvika konfigurationsfel som kan göra att du inte får tillgång till Interface-webben eller att din brandvägg inte fungerar.



När pfSense startas upptäcker och listar den automatiskt alla tillgängliga nätverksgränssnitt och anger MAC Address för varje gränssnitt. Detta gör det enkelt att skilja mellan dem.



### 1. VLAN



Den första frågan gäller konfigurationen av VLAN. I det här skedet, för en grundläggande konfiguration, kommer vi inte att aktivera några VLAN. Tryck därför på tangenten "**N**" för att hoppa över detta steg.



![Image](assets/fr/004.webp)



### 2. WAN och LAN Interface Assignment



pfSense uppmanar dig sedan att definiera vilken Interface som ska användas för WAN (Internetåtkomst). Du kan välja mellan :





- Ange Interface-namnet manuellt (rekommenderas för virtuella miljöer).
- Använd automatisk detektering genom att trycka på "**A**". Det här alternativet är användbart på en fysisk host, förutsatt att nätverkskablarna är anslutna och länkarna är aktiva.



![Image](assets/fr/005.webp)



I det här exemplet konfigurerar vi WAN manuellt. Ange det exakta namnet på Interface. För ett Intel-kort kommer namnet ofta att vara "**em0**" under FreeBSD, men det kan variera beroende på maskinvaran. Till exempel kommer ett Realtek-kort ofta att visas som "**re0**".



![Image](assets/fr/006.webp)



Upprepa samma procedur för att definiera Interface LAN. Här använder vi "**em1**".



pfSense bekräftar att Interface LAN aktiverar både brandvägg och NAT för att skydda ditt interna nätverk och hantera Address-översättning.



Om du har andra fysiska gränssnitt kan du konfigurera ytterligare gränssnitt (DMZ, Wi-Fi, specifika VLAN) i det här skedet. Varje logisk Interface kräver ett motsvarande nätverkskort eller en virtuell Interface. För den inledande konfigurationen begränsar vi oss till WAN och LAN.



När tilldelningarna har slutförts visar pfSense en tydlig sammanfattning av överensstämmelsen mellan de fysiska gränssnitten och de tilldelade rollerna. Bekräfta med "**Y**".



### 3. PfSense-konsol



När detta steg är slutfört visas huvudmenyn för pfSense-konsolen. Den erbjuder flera användbara alternativ för direkt administration, t.ex. återställning av webblösenordet, omstart, omladdning av konfigurationen eller omfördelning av gränssnitt.



![Image](assets/fr/007.webp)



Du ser också en sammanfattning av aktuella nätverksinställningar, inklusive Interface LAN:s standard-IP Address, vanligtvis **192.168.1.1**. Detta är den Address som du måste ange i din webbläsare för att komma åt Interface:s administrationswebb.



**Anmärkning**: Om ditt interna nätverk använder ett annat Address-område väljer du "**2)** Ställ in Interface(s) IP Address" i menyn för att tilldela en IP Address som passar din miljö.



Om din Interface WAN är ansluten till en DHCP-konfigurerad box eller modem, kommer pfSense som standard automatiskt att hämta en offentlig IP Address. Du bör därför dra nytta av omedelbar internetåtkomst genom att ansluta en klient till pfSense Interface LAN.



## V. Första åtkomst till Interface webben



När den första uppstarten har slutförts och nätverksgränssnitten har konfigurerats kan du gå in på pfSense Interface-webben för att slutföra och finjustera konfigurationen.



### 1. Initial anslutning



Anslut en dator till LAN-porten (eller det virtuella Interface LAN:et i din hypervisor) och tilldela den en IP Address i samma intervall om det behövs (som standard distribuerar pfSense automatiskt en Address via DHCP på LAN:et).



I din webbläsare går du till den Address som anges av konsolen (som standard `https://192.168.1.1`). Observera att pfSense kräver HTTPS även för den första anslutningen - så förvänta dig en varning om självsignerat certifikat, som du kan ignorera genom att lägga till ett undantag.



Inloggningsskärmen visas. Standardautentiseringsuppgifterna är :




- Användarnamn:** `admin`
- Lösenord:** `pfsense`



Dessa identifierare kommer att ändras under den första konfigurationsguiden.



## VI. Installationsguiden



Vid första anslutningen uppmanar pfSense dig att följa dess **Setup Wizard**. Vi rekommenderar starkt att du använder den för att säkerställa att alla viktiga parametrar är korrekt definierade.



### 1. Allmänna parametrar



Du kan :




- Ange ett värdnamn och en lokal domän (exempel: `pfsense` och `lan.local`).
- Definiera DNS-servrar och välj om pfSense ska använda din internetleverantörs DNS eller en extern tjänst (Cloudflare, OpenDNS, Quad9...).



### 2. Tidszon



Ange tidszonen för din webbplats så att loggar och scheman är konsekventa (t.ex. "Europa/Paris").



### 3. WAN-konfiguration



Konfigurera WAN-anslutningen :




- Standardvärdet är **DHCP** (tillräckligt om du befinner dig bakom en låda).
- Om du har en fast IP anger du parametrarna (statisk IP, mask, gateway, DNS) manuellt.
- Definiera vid behov ett VLAN eller PPPoE-autentisering (vanligt hos vissa ISP:er).



### 4. LAN-konfiguration



Guiden föreslår att du ändrar LAN:s standardundernät. Om du har en specifik adresseringsplan är det dags att anpassa den nu.



### 5. Ändra lösenord för administratör



Säkra din pfSense genom att omedelbart ställa in ett starkt lösenord för användaren `admin`.



## VII. Verifiering och uppdateringar



Innan du installerar brandväggen ska du se till att du har den senaste versionen av :





- Gå till **System > Uppdatera**.
- Välj uppdateringskanal (vanligtvis **Stable**).
- Sök efter uppdateringar och använd dem.



Det är en bra idé att aktivera uppdateringsmeddelanden för att hålla dig informerad om säkerhetsuppdateringar.



## VIII. Spara konfigurationen



Innan du gör några större förändringar bör du införa en policy för säkerhetskopiering:





- Gå till **Diagnostik > Säkerhetskopiering och återställning**.
- Hämta en kopia av den aktuella konfigurationen (`config.xml`).
- Förvara den på en säker plats (krypterad extern media).



För verksamhetskritiska miljöer bör du överväga automatisk säkerhetskopiering av konfigurationen på en extern server eller via ett programmerat skript.



## IX. Bästa praxis efter installationen



För att avsluta din utplacering med sinnesfrid :





- Ändra brandväggsregler**: som standard tillåter pfSense all utgående trafik på LAN och blockerar inkommande trafik på WAN. Justera dessa regler efter behov.
- Konfigurera säker fjärråtkomst**: om så krävs, aktivera åtkomst till Interface webb från WAN endast via VPN eller med IP-begränsningar.
- Enable notifications**: konfigurera en SMTP-server för att ta emot aviseringar (fel, uppdateringar, fel).
- Installera användbara tillägg**: t.ex. IDS/IPS (Snort, Suricata), proxy (Squid), DNS-filtrering (pfBlockerNG).



Din pfSense-brandvägg är nu igång och redo att skydda ditt nätverk. Tack vare dess flexibilitet och aktiva community har du ett kraftfullt, skalbart verktyg som kan anpassas till dina framtida behov (multi-WAN, VLAN, site-to-site VPN, captive portal etc.).



Läs den officiella dokumentationen ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) regelbundet för att upptäcka nya funktioner och se till att din konfiguration är uppdaterad och säker.