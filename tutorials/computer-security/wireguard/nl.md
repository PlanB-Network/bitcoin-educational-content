---
name: WireGuard
description: WireGuard VPN instellen op Debian en Windows
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian BURNEL gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## I. Presentatie



In deze tutorial leren we hoe we een VPN kunnen configureren op basis van WireGuard, een gratis, open-source VPN-oplossing die de prestaties verhoogt zonder de beveiliging te verwaarlozen.



WireGuard is een relatief recente oplossing, die beschikbaar is als stabiele release sinds maart 2020, en heeft de eer om direct geïntegreerd te zijn in de **Linux kernel sinds versie 5.6**. Dit verhindert niet dat het toegankelijk is vanuit oudere Linux-distributies die een andere versie van de kernel gebruiken. Vergeleken met oplossingen zoals OpenVPN en IPSec is WireGuard eenvoudiger te gebruiken en veel sneller, zoals we aan het einde van dit artikel zullen zien.



Enkele belangrijke punten over WireGuard:





- Eenvoudig, lichtgewicht en ultra-efficiënt!
- Alleen UDP (wat een nadeel kan zijn bij het passeren van bepaalde firewalls)
- Werkt op een peer-to-peer in plaats van client-server model
- Authenticatie via sleutel Exchange, volgens hetzelfde principe als SSH met privé/publieke sleutels
- Gebruik van verschillende algoritmen: symmetrische encryptie met ChaCha20, berichtverificatie met Poly1305 en andere zoals Curve25519, BLAKE2 en SipHash24
- Ondersteunt zowel IPv4 als IPv6
- Multi-platform: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (en geïmplementeerd in ProtonVPN)
- Slechts 4000 regels code, vergeleken met honderdduizenden voor andere oplossingen



Voor het cryptografische gedeelte worden de verschillende gebruikte algoritmen met de hand geselecteerd, op verschillende manieren gecontroleerd en onderzocht door gespecialiseerde beveiligingsonderzoekers.



De officiële projectwebsite: [wireguard.com](https://www.wireguard.com/)



Ben je na het lezen van deze inleiding overtuigd van deze oplossing? Dan hoef je alleen nog maar verder te lezen!



## II. Lab WireGuard-diagram



Voordat ik mijn lab voor het instellen van WireGuard presenteer, moet je weten dat je je kunt voorstellen om WireGuard te gebruiken om twee infrastructuren op afstand met elkaar te verbinden**, maar ook om een client op afstand te verbinden met een infrastructuur zoals een bedrijfsnetwerk of je thuisnetwerk**. Dit is in dezelfde geest als met OpenVPN, zoals we onlangs hebben gezien in de tutorial "[OpenVPN op Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Als WireGuard niet direct op de router of firewall is ingesteld, zoals denkbaar is met OpenWRT, dan moet je port forwarding instellen zodat de stroom het WireGuard paar bereikt.



![Image](assets/fr/034.webp)



Nu zal ik je vertellen over mijn lab en wat we vandaag gaan doen.



Ik ga een Debian 11 machine gebruiken als de WireGuard server en een Windows client als de WireGuard VPN client. Hoewel het een beetje misleidend is om te spreken over een client-server relatie, omdat **WireGuard werkt op een "peer-to-peer"** model. Dat is een beetje een verkeerde benaming wanneer u een "client-to-site" verbinding probeert op te zetten. Laten we in plaats daarvan zeggen dat ik twee paren ga hebben of **twee WireGuard verbindingspunten** als je dat liever hebt: één onder Debian 11 en de andere onder Windows.



Deze twee paren kunnen in beide richtingen met elkaar communiceren, wat betekent dat ik vanaf mijn Windows machine toegang heb tot het remote LAN van de Debian 11 machine, en vice versa: het hangt allemaal af van de configuratie van de tunnel en de firewall van de WireGuard peer.



In dit voorbeeld richt ik me op het volgende geval: **vanuit mijn Windows Peer 1 verbonden met mijn thuisnetwerk, wil ik toegang krijgen tot mijn bedrijfsnetwerk om toegang te krijgen tot de servers van het bedrijf via de WireGuard VPN tunnel**. Dit geeft het volgende diagram:



![Image](assets/fr/035.webp)



In termen van IP-adressen geeft dit:





- Thuisnetwerk**: 192.168.1.0/24
- Bedrijfsnetwerk**: 192.168.100.0/24
- WireGuard tunnelnetwerk**: 192.168.110.0/24


+ IP Address van Peer 1 (Windows) in de tunnel: 192.168.110.2/24


+ IP Address van Peer 2 (Debian) in de tunnel: 192.168.110.121/24



Dat is alles! Laten we beginnen met de configuratie!



**Opmerking: standaard werkt WireGuard in UDP-modus op **poort 51820**.



## III WireGuard serverinstallatie en configuratie



Ik ga de termen "client" voor de Windows machine en "server" voor de Debian machine gebruiken in deze tutorial, omdat het zinvoller lijkt, ook al is het peer-to-peer.



### A. WireGuard installeren op Debian 11



Het WireGuard-installatiepakket is beschikbaar in de officiële Debian 11-repositories, dus we hoeven alleen maar de pakketcache bij te werken en het te installeren:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Het WireGuard servergedeelte wordt geïnstalleerd, samen met diverse tools die toegang geven tot handige commando's voor het beheren van de configuratie.



### B. Een Interface WireGuard installeren



Met het **commando "wg"** moeten we een private sleutel en een publieke sleutel generate maken: essentieel voor authenticatie tussen twee paren, namelijk de server en een client (die ook een sleutelpaar nodig heeft).



We maken de privésleutel "**/etc/wireguard/wg-private.key**" en de publieke sleutel "**/etc/wireguard/wg-public.key**" met deze opdrachtvolgorde:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



De waarde van de publieke sleutel wordt teruggegeven in de console. In het WireGuard configuratiebestand moeten we **de waarde van onze private key** toevoegen. Om deze waarde op te halen, voert u het onderstaande commando in en kopieert u de waarde:



```
sudo cat /etc/wireguard/wg-private.key
```



Het is tijd om een configuratiebestand aan te maken in "**/etc/wireguard/**". We kunnen dit bestand bijvoorbeeld "**wg0.conf**" noemen, als we denken dat het Interface netwerk dat geassocieerd is met WireGuard "wg0" zal zijn, volgens hetzelfde principe als bijvoorbeeld "eth0".



```
sudo nano /etc/wireguard/wg0.conf
```



In dit bestand moeten we eerst de volgende inhoud toevoegen (we komen later terug om het aan te vullen):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Sectie `[Interface]` wordt gebruikt om het servergedeelte te declareren. Hier is wat informatie:





- Address**: het IP Address van de Interface WireGuard binnen de VPN-tunnel (ander subnet dan het LAN op afstand)
- SaveConfig**: de configuratie wordt opgeslagen (en beschermd) zolang de Interface actief is
- ListenPort**: De luisterpoort van WireGuard. In dit geval is 51820 de standaardpoort, maar u kunt deze aanpassen
- PrivateKey**: de waarde van de privésleutel van onze server (*wg-private.key*)



Sla het bestand op en sluit het. Met het "**wg-quick**" commando kunnen we deze Interface starten door zijn naam op te geven (wg0, aangezien het bestand wg0.conf heet):



```
sudo wg-quick up wg0
```



Als je de IP adressen van je Debian 11 server opsomt, zie je een nieuwe Interface genaamd "wg0" met het IP Address gedefinieerd in het config bestand:



```
ip a
```



![Image](assets/fr/027.webp)



In dezelfde geest kunnen we de Interface "wg0" configuratie weergeven met het "wg show" commando:



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Tot slot moeten we het automatisch opstarten van onze Interface wg0 WireGuard activeren:



```
sudo systemctl enable wg-quick@wg0.service
```



Op dit moment laten we de configuratie van de serverkant van WireGuard buiten beschouwing.



### C. IP-forwarding inschakelen



Om ervoor te zorgen dat onze Debian 11 machine pakketten kan **routeren tussen verschillende netwerken (zoals een router)**, bijvoorbeeld tussen het VPN-netwerk en het lokale netwerk, moeten we [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/) inschakelen. Standaard is deze functie uitgeschakeld.



Wijzig dit configuratiebestand:



```
sudo nano /etc/sysctl.conf
```



Voeg de volgende richtlijn toe aan het einde van het bestand en sla op:



```
net.ipv4.ip_forward = 1
```



Dat is alles.



### D. IP-maskerade inschakelen



Om ervoor te zorgen dat onze server pakketten correct routeert en het externe LAN toegankelijk is voor de Windows machine, moeten we IP Masquerade activeren op onze Debian server. Dit is een soort NAT activering. Ik ga deze configuratie uitvoeren op de Linux firewall via UFW, die ik gewend ben te gebruiken ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Als je nog geen UFW hebt en het wilt instellen (je kunt ook Nftables gebruiken), begin dan met het installeren van:



```
sudo apt install ufw
```



Allereerst moet je SSH inschakelen om de controle over de externe server niet te verliezen (pas het poortnummer aan):



```
sudo ufw allow 22/tcp
```



Poort 51820 in UDP moet ook geautoriseerd zijn, omdat we die gebruiken voor WireGuard (pas ook hier het poortnummer aan):



```
sudo ufw allow 51820/udp
```



Vervolgens gaan we verder met de configuratie om IP-masquerade in te schakelen. Om dit te doen, moeten we de naam achterhalen van de Interface die verbonden is met het lokale netwerk. Als je de naam niet weet, voer dan "ip a" uit om de naam van de kaart te zien. In mijn geval is het de "**ens192**" kaart.



![Image](assets/fr/036.webp)



We gaan deze informatie gebruiken. Bewerk het volgende bestand:



```
sudo nano /etc/ufw/before.rules
```



Voeg deze regels toe aan het einde van het bestand om **IP-masquerade in te schakelen op de Interface ens192** (pas de Interface naam aan) binnen de POSTROUTING string van de NAT tabel van onze lokale firewall:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



De afbeelding toont:



![Image](assets/fr/037.webp)



Houd dit configuratiebestand open en ga verder met de volgende stap. 😉



### E. Linux firewall configuratie voor WireGuard



Nog steeds in hetzelfde configuratiebestand gaan we het bedrijfsnetwerk "192.168.100.0/24" declareren zodat we er contact mee kunnen maken. Hier zijn de twee regels die toegevoegd moeten worden (idealiter na de "*# ok icmp code for FORWARD*" sectie om de regels te groeperen):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Als je slechts één host wilt autoriseren, bijvoorbeeld "192.168.100.11", dan is dat eenvoudig:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Nu kunt u het bestand opslaan en sluiten. Het enige dat nog moet gebeuren is UFW activeren en de service herstarten om onze wijzigingen toe te passen:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Het eerste deel van de configuratie van de Debian-server is nu voltooid.



## IV. WireGuard-client voor Windows



De WireGuard-client is beschikbaar voor Windows, macOS, Android, enz... Dit is geweldig nieuws. Alle downloads zijn beschikbaar op deze pagina: [WireGuard Client](https://www.wireguard.com/install/). In dit voorbeeld ga ik de client instellen op Windows. Om de WireGuard-client op Linux in te stellen, volg je hetzelfde principe als voor het maken van het wg0.conf bestand op de Debian machine (zonder alle NAT, etc.).



### A. De WireGuard Windows-client installeren



Zodra je het uitvoerbare bestand of het MSI-pakket hebt gedownload, is de installatie eenvoudig: start het installatieprogramma en...voilà, klaar! 🙂



![Image](assets/fr/038.webp)



### B. Een WireGuard-profiel aanmaken



Begin met het openen van de software om een nieuwe tunnel aan te maken. Klik hiervoor op de pijl rechts van de knop "**Tunnel toevoegen**" en klik op de knop "**Lege tunnel toevoegen**".



![Image](assets/fr/028.webp)



Er wordt een configuratievenster geopend. Elke keer dat er een nieuwe tunnelconfiguratie wordt aangemaakt, genereert WireGuard een privésleutel/publiek sleutelpaar dat specifiek is voor deze configuratie. **In deze configuratie moeten we de "peer" aangeven, dat wil zeggen de server op afstand:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



We moeten deze configuratie voltooien, in het bijzonder om het IP Address op deze Interface (*Address*) te declareren, maar ook om de remote WireGuard server te declareren via een [Peer] blok. De afbeelding hieronder zou je moeten herinneren aan het configuratiebestand dat we aan de Linux serverkant hebben gemaakt.



Laten we beginnen met het `[Interface]` blok en het IP Address "**192.168.110.2**" toevoegen; onthoud dat de server het IP Address "**192.168.110.121**" heeft op dit netwerksegment. Dit geeft:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Vervolgens moeten we het blok "Peer" declareren met drie eigenschappen, wat resulteert in deze configuratie:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



In beeld:



![Image](assets/fr/029.webp)



**Een paar verklaringen over het [Peer] blok:





- PublicKey**: dit is de publieke sleutel van de WireGuard Debian 11 server (u kunt de waarde ervan verkrijgen met het "*sudo wg*" commando)
- AllowedIPs**: dit zijn de IP-adressen / subnetten die toegankelijk zijn via dit WireGuard VPN-netwerk, in dit geval het subnet dat specifiek is voor mijn WireGuard VPN (*192.168.110.0/24*) en mijn LAN op afstand (*192.168.100.0/24*)
- Eindpunt**: dit is het IP Address van de Debian 11 host, aangezien dit ons WireGuard verbindingspunt is (je moet het publieke IP Address specificeren)



Voer tenslotte een naam in het veld "**Naam**" in (zonder spaties) en kopieer en plak de publieke sleutel van de client, omdat we die op de server moeten declareren. Klik op "**Register**".



### C. Client op WireGuard-server declareren



Het is tijd om terug te gaan naar de Debian server om de "**Peer**", d.w.z. onze Windows PC, aan te geven in de WireGuard configuratie. Allereerst moeten we de Interface "wg0"** stoppen om zijn configuratie aan te passen:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Wijzig vervolgens het eerder aangemaakte configuratiebestand:



```
sudo nano /etc/wireguard/wg0.conf
```



In dit bestand moeten we na het `[Interface]` blok een `[Peer]` blok declareren:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Dit [Peer] blok bevat de publieke sleutel van de Windows 10 PC (**PublicKey**) en het IP Address van de Interface van de PC (**AllowedIPs**): de server zal in deze WireGuard tunnel alleen communiceren om contact te maken met de Windows client, vandaar de waarde "**192.168.110.2/32**".



Het enige wat overblijft is het bestand opslaan (*CTRL+O dan Enter dan CTRL+X via Nano*). Start Interface "wg0" opnieuw:



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Om te controleren of de peer-declaratie werkt, kun je dit commando gebruiken:



```
sudo wg show
```



Zodra de externe host zijn WireGuard-verbinding heeft opgezet, zal zijn IP Address worden verplaatst naar de "endpoint" waarde.



![Image](assets/fr/033.webp)



Tenslotte zullen we de configuratiebestanden beveiligen om root-toegang te beperken:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Eerste WireGuard-verbinding



Nu de configuratie klaar is, kunnen we deze starten vanaf de Windows PC. Om dit te doen, klik je in de "**WireGuard**" client op de "**Activate**" knop: de verbinding zal **veranderen van "Off" naar "On"**, maar dat betekent niet dat het zal werken. Het hangt ervan af of je configuratie correct is of niet. **Als de verbinding tot stand is gebracht, communiceren onze twee machines via de Interface WireGuard die aan elke kant is geconfigureerd!



![Image](assets/fr/030.webp)



In het geval van een probleem zal dit zichtbaar zijn op het tabblad "**Logboek**". De twee hosts Exchange pakketten regelmatig om de status van de verbinding te controleren, vandaar de "*Receiving keepalive packet from peer 1*" berichten.



![Image](assets/fr/031.webp)



Als het tabblad "**Journaal**" van WireGuard een bericht weergeeft zoals hieronder, dan moet u controleren of de publieke sleutels die aan beide zijden zijn opgegeven, correct zijn.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Vanaf mijn externe PC kan ik het IP Address van mijn Interface WireGuard aan de serverzijde pingen, evenals een host op mijn externe LAN.



![Image](assets/fr/032.webp)



### E. Prestaties: OpenVPN vs WireGuard



Vanaf mijn externe PC die verbonden is met mijn WireGuard VPN, kon ik toegang krijgen tot een bestandsserver en een bestand overdragen via [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), om de overdrachtssnelheid te zien. **Met WireGuard maximaliseer ik rond de 45 Mb/s, wat geweldig is, omdat ik op WiFi zit



![Image](assets/fr/025.webp)



Onder dezelfde omstandigheden, maar via een OpenVPN verbinding (in UDP) dit keer, met dezelfde werking, is de doorvoer totaal anders: rond de 3 MB/s. Het verschil is duidelijk!



![Image](assets/fr/026.webp)



Dit is interessant, want als je bijvoorbeeld overschakelt van een WiFi-verbinding naar een 4G/5G-verbinding, zal de herverbinding zo snel zijn dat de onderbreking niet zichtbaar is.



### F. Bonus: volledige tunnel WireGuard



Met de huidige configuratie stroomt een deel van het verkeer via het VPN en de rest via de internetverbinding van de klant, inclusief surfen op het internet. Als we willen overschakelen naar WireGuard **full tunnel mode**, zodat alles door de VPN-tunnel gaat, moeten we een paar wijzigingen aanbrengen in onze configuratie....



Eerst moet je het pakket "resolvconf" installeren op de:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Zodra dit is gedaan, moet je het "wg0.conf" profiel op de Debian machine aanpassen: stop Interface, pas het aan en start opnieuw op.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Vervolgens **in het `[Interface]` blok voegen we de te gebruiken DNS server toe**. In mijn geval is dat de domeincontroller van mijn lab, maar we kunnen ook Bind9 op de Debian machine installeren om een lokale resolver te hebben.



```
DNS = 192.168.100.11
```



Sla het bestand op en start Interface opnieuw op:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Ten slotte moet je in de tunnelconfiguratie op het Windows 10 werkstation de sectie "AllowedIPs" aanpassen om aan te geven dat alles door de tunnel moet. Vervangen:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Door:



```
AllowedIPs = 0.0.0.0/0
```



Je kunt zien dat dit ook de optie "**Kill switch*" inschakelt.



![Image](assets/fr/040.webp)



Tot slot heb ik van deze volle tunnel gebruik gemaakt om een kleine flowtest uit te voeren, waarvan de resultaten hieronder staan:



![Image](assets/fr/039.webp)



De configuratie van WireGuard is vrij eenvoudig en gemakkelijk te begrijpen en vooral te onderhouden. **WireGuard wordt beschouwd als de toekomst van VPN's**, dus we kunnen het maar beter goed in de gaten houden! We kunnen ook zien dat het voordeel aanzienlijk is op het gebied van prestaties, wat een enorm voordeel is voor WireGuard in vergelijking met OpenVPN.



Aanvullende documentatie:





- [Man - Commando wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Commando wg-snel](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**Uw WireGuard VPN werkt! Gefeliciteerd!