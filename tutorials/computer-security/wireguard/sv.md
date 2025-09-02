---
name: WireGuard
description: Konfigurera WireGuard VPN på Debian och Windows
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian BURNEL publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___



## I. Presentation



I den här handledningen lär vi oss hur man konfigurerar ett VPN baserat på WireGuard, en gratis VPN-lösning med öppen källkod som ökar prestandan utan att försumma säkerheten.



WireGuard är en relativt ny lösning, som har funnits tillgänglig som en stabil version sedan mars 2020, och har haft äran att integreras direkt i **Linux-kärnan sedan version 5.6**. Detta hindrar inte att den är tillgänglig från äldre Linux-distributioner som använder en annan version av kärnan. Jämfört med lösningar som OpenVPN och IPSec är WireGuard enklare att använda och mycket snabbare, som vi kommer att se i slutet av den här artikeln.



Några viktiga punkter om WireGuard:





- Enkelt, lättviktigt och ultraeffektivt!
- Endast UDP-funktion (vilket kan vara en nackdel när man passerar vissa brandväggar)
- Arbetar enligt en peer-to-peer-modell snarare än en klient-server-modell
- Autentisering med nyckel Exchange, enligt samma princip som SSH med privata/offentliga nycklar
- Användning av flera algoritmer: symmetrisk kryptering med ChaCha20, meddelandeautentisering med Poly1305, samt andra som Curve25519, BLAKE2 och SipHash24
- Stödjer både IPv4 och IPv6
- Flera plattformar: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (och implementerat i ProtonVPN)
- Endast 4.000 rader kod, jämfört med hundratusentals för andra lösningar



För den kryptografiska delen är de olika algoritmer som används handplockade, granskade på flera sätt och undersökta av säkerhetsforskare som är specialiserade inom området.



Den officiella webbplatsen för projektet: [wireguard.com](https://www.wireguard.com/)



Är du övertygad om denna lösning efter att ha läst denna introduktion? Allt som återstår att göra är att läsa vidare!



## II. Lab WireGuard-diagram



Innan jag presenterar mitt labb för att konfigurera WireGuard bör du veta att du kan tänka dig att **använda WireGuard för att sammankoppla två fjärrinfrastrukturer**, men också för att **ansluta en fjärrklient till en infrastruktur som ett företagsnätverk eller ditt hemnätverk**. Detta är i samma anda som med OpenVPN, som vi nyligen såg i handledningen "[OpenVPN på Synology] (https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Om WireGuard inte är konfigurerad direkt på routern eller brandväggen, vilket är tänkbart med OpenWRT, måste du konfigurera port vidarebefordran så att flödet når WireGuard-paret.



![Image](assets/fr/034.webp)



Nu ska jag berätta om mitt labb och vad vi ska sätta upp idag.



Jag kommer att använda en Debian 11-maskin som WireGuard-server och en Windows-klient som WireGuard VPN-klient. Även om det är lite missvisande att prata om ett klient-server-förhållande, eftersom **WireGuard fungerar på en "peer-to-peer"**-modell. Det är lite missvisande när du försöker skapa en "klient-till-plats"-anslutning. Låt oss istället säga att jag kommer att ha två par eller **två WireGuard-anslutningspunkter** om du föredrar det: en under Debian 11 och den andra under Windows.



Dessa två par kan kommunicera med varandra i båda riktningarna, vilket innebär att jag från min Windows-maskin kan komma åt Debian 11-maskinens fjärr-LAN och vice versa: allt beror på konfigurationen av tunneln och WireGuard-peerens brandvägg.



I det här exemplet kommer jag att fokusera på följande fall: **från min Windows Peer 1 som är ansluten till mitt hemnätverk vill jag komma åt mitt företagsnätverk för att komma åt företagets servrar via WireGuard VPN-tunneln**. Detta ger följande diagram:



![Image](assets/fr/035.webp)



I termer av IP-adresser ger detta:





- Hemnätverk**: 192.168.1.0/24
- Företagsnätverk**: 192.168.100.0/24
- WireGuard tunnel nätverk**: 192.168.110.0/24


+ IP Address för Peer 1 (Windows) i tunneln: 192.168.110.2/24


+ IP Address för Peer 2 (Debian) i tunneln: 192.168.110.121/24



Det är allt som finns att säga! Låt oss komma igång med konfigurationen!



**Anmärkning: som standard arbetar WireGuard i UDP-läge på **port 51820**.



## III Installation och konfiguration av WireGuard-server



Jag kommer att använda termerna "klient" för Windows-maskinen och "server" för Debian-maskinen i den här handledningen, för även om det är peer-to-peer verkar det mer meningsfullt.



### A. Installera WireGuard på Debian 11



Installationspaketet för WireGuard finns tillgängligt i de officiella Debian 11-arkiven, så allt vi behöver göra är att uppdatera paketcachen och installera det:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



WireGuard-serverdelen kommer att installeras tillsammans med olika verktyg som ger tillgång till användbara kommandon för att hantera konfigurationen.



### B. Installera en Interface WireGuard



Med kommandot **"wg"** måste vi generate en privat nyckel och en offentlig nyckel: nödvändigt för autentisering mellan två par, dvs. servern och en klient (som också behöver ett nyckelpar).



Vi kommer att skapa den privata nyckeln "**/etc/wireguard/wg-private.key**" och den offentliga nyckeln "**/etc/wireguard/wg-public.key**" med denna kommandosekvens:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Värdet på den publika nyckeln kommer att returneras i konsolen. I WireGuards konfigurationsfil måste vi **lägga till värdet för vår privata nyckel**. För att hämta detta värde, ange kommandot nedan och kopiera värdet:



```
sudo cat /etc/wireguard/wg-private.key
```



Nu är det dags att skapa en konfigurationsfil i "**/etc/wireguard/**". Vi kan till exempel namnge den här filen "**wg0.conf**", om vi tror att Interface-nätverket som är kopplat till WireGuard kommer att vara "wg0", enligt samma princip som till exempel "eth0".



```
sudo nano /etc/wireguard/wg0.conf
```



I den här filen måste vi först lägga till följande innehåll (vi kommer tillbaka för att komplettera det senare):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Avsnittet `[Interface]` används för att deklarera serverdelen. Här är lite information:





- Address**: IP Address för Interface WireGuard inom VPN-tunneln (annat subnät än fjärr-LAN:et)
- SaveConfig**: konfigurationen lagras (och skyddas) så länge Interface är aktiv
- LyssnaPort**: WireGuards lyssningsport. I det här fallet är 51820 standardporten, men du är välkommen att anpassa den
- PrivateKey**: värdet på vår servers privata nyckel (*wg-private.key*)



Spara filen och stäng den. Med kommandot "**wg-quick**" kan vi starta den här Interface genom att ange dess namn (wg0, eftersom filen heter wg0.conf):



```
sudo wg-quick up wg0
```



Om du listar IP-adresserna på din Debian 11-server ser du en ny Interface med namnet "wg0" med IP Address som definieras i konfigurationsfilen:



```
ip a
```



![Image](assets/fr/027.webp)



I samma anda kan vi visa Interface:s konfiguration "wg0" via kommandot "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Slutligen måste vi aktivera den automatiska uppstarten av vår Interface wg0 WireGuard:



```
sudo systemctl enable wg-quick@wg0.service
```



För tillfället lämnar vi konfigurationen av WireGuards serversida åt sidan.



### C. Aktivera IP-vidarebefordran



För att vår Debian 11-maskin ska kunna **dirigera paket mellan olika nätverk (som en router)**, dvs. mellan VPN-nätverket och det lokala nätverket, måste vi aktivera [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Som standard är den här funktionen inaktiverad.



Ändra denna konfigurationsfil:



```
sudo nano /etc/sysctl.conf
```



Lägg till följande direktiv i slutet av filen och spara:



```
net.ipv4.ip_forward = 1
```



Det är allt som finns att säga.



### D. Aktivera IP-masquerade



För att vår server ska kunna dirigera paket korrekt och för att det lokala fjärrnätverket ska vara tillgängligt för Windows-maskinen måste vi aktivera IP Masquerade på vår Debian-server. Detta är en slags NAT-aktivering. Jag kommer att utföra den här konfigurationen på Linux-brandväggen genom UFW, som jag är van att använda ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Om du inte redan har UFW och vill konfigurera det (du kan också använda Nftables), börja med att installera:



```
sudo apt install ufw
```



Först och främst måste du aktivera SSH så att du inte tappar kontrollen över fjärrservern (anpassa portnumret):



```
sudo ufw allow 22/tcp
```



Port 51820 i UDP måste också vara auktoriserad, eftersom vi använder den för WireGuard (återigen, anpassa portnumret):



```
sudo ufw allow 51820/udp
```



Därefter fortsätter vi med konfigurationen för att aktivera IP-maskerad. För att göra detta måste vi hämta namnet på den Interface som är ansluten till det lokala nätverket. Om du inte vet namnet, kör "ip a" för att se namnet på kortet. I mitt fall är det kortet "**ens192**".



![Image](assets/fr/036.webp)



Vi kommer att använda denna information. Redigera följande fil:



```
sudo nano /etc/ufw/before.rules
```



Lägg till dessa rader i slutet av filen för att **aktivera IP-maskerad på Interface ens192** (anpassa Interface-namnet) inom POSTROUTING-strängen i vår lokala brandväggs NAT-tabell:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Bilden visar:



![Image](assets/fr/037.webp)



Håll den här konfigurationsfilen öppen och fortsätt till nästa steg. 😉



### E. Konfiguration av Linux-brandvägg för WireGuard



Fortfarande i samma konfigurationsfil kommer vi att deklarera företagsnätverket "192.168.100.0/24" så att vi kan kontakta det. Här är de två regler som ska läggas till (helst efter avsnittet "*# ok icmp-kod för FORWARD*" för att gruppera reglerna tillsammans):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Om du bara vill auktorisera en värd, t.ex. "192.168.100.11", är det enkelt:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Nu kan du spara filen och stänga den. Allt som återstår är att aktivera UFW och starta om tjänsten för att tillämpa våra ändringar:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Den första delen av konfigurationen av Debian-servern är nu klar.



## IV. WireGuard-klient för Windows



WireGuard-klienten är tillgänglig för Windows, macOS, Android, etc... Det här är fantastiska nyheter. Alla nedladdningar finns tillgängliga på den här sidan: [WireGuard-klient](https://www.wireguard.com/install/). I det här exemplet kommer jag att konfigurera klienten på Windows. För att konfigurera WireGuard-klienten på Linux, följ samma princip som för att skapa wg0.conf-filen på Debian-maskinen (utan all NAT, etc.).



### A. Installera WireGuards Windows-klient



När du har laddat ner den körbara filen eller MSI-paketet är installationen enkel: starta bara installationsprogrammet och ... voilà, det är klart!



![Image](assets/fr/038.webp)



### B. Skapa en WireGuard-profil



Börja med att öppna programvaran för att skapa en ny tunnel. Detta gör du genom att klicka på pilen till höger om knappen "**Add tunnel**" och sedan på knappen "**Add empty tunnel**".



![Image](assets/fr/028.webp)



Ett konfigurationsfönster öppnas. Varje gång en ny tunnelkonfiguration skapas genererar WireGuard ett privat/offentligt nyckelpar som är specifikt för denna konfiguration. **I den här konfigurationen måste vi ange "peer", dvs. fjärrservern:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Vi måste slutföra den här konfigurationen, i synnerhet för att deklarera IP Address på den här Interface (*Address*), men också för att deklarera WireGuard-fjärrservern via ett [Peer]-block. Bilden nedan bör påminna dig om konfigurationsfilen som vi skapade på Linux-serversidan.



Vi börjar med blocket `[Interface]` och lägger till IP Address "**192.168.110.2**"; kom ihåg att servern har IP Address "**192.168.110.121**" i det här nätverkssegmentet. Detta ger:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Därefter måste vi deklarera blocket "Peer" med tre egenskaper, vilket resulterar i denna konfiguration:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



I bilder:



![Image](assets/fr/029.webp)



**Några förklaringar om [Peer]-blocket:





- PublicKey**: detta är den publika nyckeln för WireGuard Debian 11-servern (du kan få fram dess värde med kommandot "*sudo wg*")
- AllowedIPs**: detta är de IP-adresser/undernät som är tillgängliga via detta WireGuard VPN-nätverk, i detta fall det undernät som är specifikt för mitt WireGuard VPN (*192.168.110.0/24*) och mitt fjärr-LAN (*192.168.100.0/24*)
- Endpoint**: detta är IP Address för Debian 11-värden, eftersom detta är vår WireGuard-anslutningspunkt (du måste ange den offentliga IP Address)



Slutligen anger du ett namn i fältet "**Name**" (utan mellanslag) och kopierar och klistrar in klientens publika nyckel, eftersom vi måste deklarera den på servern. Klicka på "**Register**".



### C. Deklarera klient på WireGuard-server



Det är dags att återvända till Debian-servern för att deklarera "**Peer**", dvs. vår Windows-dator, i WireGuard-konfigurationen. Först och främst måste vi **stoppa Interface "wg0"** för att kunna ändra dess konfiguration:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Därefter ändrar du den tidigare skapade konfigurationsfilen:



```
sudo nano /etc/wireguard/wg0.conf
```



I den här filen, efter blocket `[Interface]`, måste vi deklarera ett block `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Detta [Peer]-block innehåller Windows 10-datorns offentliga nyckel (**PublicKey**) och IP Address för datorns Interface (**AllowedIPs**): servern kommer att kommunicera i denna WireGuard-tunnel endast för att kontakta Windows-klienten, därav värdet "**192.168.110.2/32**".



Allt som återstår är att spara filen (*CTRL+O sedan Enter sedan CTRL+X via Nano*). Starta om Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Om du vill kontrollera att peer-deklarationen fungerar kan du använda det här kommandot:



```
sudo wg show
```



När fjärrvärden har upprättat sin WireGuard-anslutning flyttas dess IP Address upp till värdet "endpoint".



![Image](assets/fr/033.webp)



Slutligen ska vi säkra konfigurationsfilerna för att begränsa root-åtkomst:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Första WireGuard-anslutningen



Nu när konfigurationen är klar kan vi initiera den från Windows PC. För att göra detta, i "**WireGuard**" -klienten, klicka på "**Activate**" -knappen: anslutningen kommer ** att ändras från "Off" till "On"**, men det betyder inte att den kommer att fungera. Allt beror på om din konfiguration är korrekt eller inte. **När anslutningen är upprättad kommunicerar våra två maskiner via Interface WireGuard som konfigurerats på vardera sidan!



![Image](assets/fr/030.webp)



Om ett problem uppstår kommer detta att synas på fliken "**Logbook**". De två värdarna skickar regelbundet Exchange-paket för att kontrollera anslutningens status, därav meddelandena "*Receiving keepalive packet from peer 1*".



![Image](assets/fr/031.webp)



Om WireGuards flik "**Journal**" visar ett meddelande som det nedan, måste du kontrollera att de offentliga nycklar som deklarerats på båda sidor är korrekta.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Från min fjärrdator kan jag pinga IP Address för min Interface WireGuard på serversidan, samt en värd på mitt fjärr-LAN.



![Image](assets/fr/032.webp)



### E. Prestanda: OpenVPN vs WireGuard



Från min fjärr-PC ansluten till min WireGuard VPN kunde jag komma åt en filserver och överföra en fil via [SMB] (https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), för att se överföringshastigheten. ** Med WireGuard maxar jag till cirka 45 Mb/s, vilket är bra eftersom jag är på WiFi



![Image](assets/fr/025.webp)



Under samma förhållanden, men via en OpenVPN-anslutning (i UDP) den här gången, med samma operation, är genomströmningen helt annorlunda: cirka 3 MB/s. Skillnaden är uppenbar!



![Image](assets/fr/026.webp)



Det här är intressant, för om du till exempel byter från en WiFi-anslutning till en 4G/5G-anslutning kommer återanslutningen att vara så snabb att avbrottet inte syns.



### F. Bonus: full tunnel WireGuard



Med den nuvarande konfigurationen flödar en del av trafiken genom VPN och resten genom kundens internetanslutning, inklusive internetsurfning. Om vi vill byta till WireGuards **full tunnel-läge**, så att allt passerar genom VPN-tunneln, måste vi göra några ändringar i vår konfiguration....



Först måste du installera paketet "resolvconf" på:



```
sudo apt-get update
sudo apt-get install resolvconf
```



När detta har gjorts måste du ändra profilen "wg0.conf" på Debian-maskinen: stoppa Interface, ändra den och starta om.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Därefter, **i blocket `[Interface]`, lägger vi till den DNS-server som ska användas**. I mitt fall är det mitt labbs domänkontrollant, men vi kan också installera Bind9 på Debian-maskinen för att ha en lokal resolver.



```
DNS = 192.168.100.11
```



Spara filen och starta sedan om Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Slutligen, i tunnelkonfigurationen på Windows 10-arbetsstationen, måste du ändra avsnittet "AllowedIPs" för att ange att allt måste passera genom tunneln. Ersätta:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Av:



```
AllowedIPs = 0.0.0.0/0
```



Du kan se att detta även aktiverar alternativet "**Kill switch*".



![Image](assets/fr/040.webp)



Slutligen utnyttjade jag den fulla tunneln för att utföra ett litet flödestest, vars resultat visas nedan:



![Image](assets/fr/039.webp)



WireGuards konfiguration är ganska enkel och lätt att förstå, och framför allt att underhålla. **WireGuard anses vara framtiden för VPN**, så det är bäst att vi håller ett öga på det! Vi kan också se att fördelen är betydande när det gäller prestanda, vilket är en enorm fördel för WireGuard jämfört med OpenVPN.



Ytterligare dokumentation:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Kommando wg-quick] (https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**Ditt WireGuard VPN är igång och fungerar! Vi gratulerar dig!