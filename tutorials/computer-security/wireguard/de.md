---
name: WireGuard
description: Einrichtung von WireGuard VPN unter Debian und Windows
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian BURNEL, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___



## I. Präsentation



In diesem Tutorial erfahren Sie, wie Sie ein VPN auf Basis von WireGuard konfigurieren, einer kostenlosen Open-Source-VPN-Lösung, die die Leistung steigert, ohne die Sicherheit zu vernachlässigen.



WireGuard ist eine relativ neue Lösung, die seit März 2020 als stabile Version verfügbar ist und die Ehre hat, seit Version 5.6** direkt in den **Linux-Kernel integriert zu sein. Dies schließt nicht aus, dass sie von älteren Linux-Distributionen, die eine andere Version des Kernels verwenden, zugänglich ist. Im Vergleich zu Lösungen wie OpenVPN und IPSec ist WireGuard einfacher zu bedienen und viel schneller, wie wir am Ende dieses Artikels sehen werden.



Einige wichtige Punkte über WireGuard:





- Einfach, leicht und äußerst effizient!
- Nur UDP-Betrieb (was beim Durchqueren bestimmter Firewalls ein Nachteil sein kann)
- Arbeitet mit einem Peer-to-Peer- statt mit einem Client-Server-Modell
- Authentifizierung durch Schlüssel Exchange, nach dem gleichen Prinzip wie SSH mit privaten/öffentlichen Schlüsseln
- Verwendung mehrerer Algorithmen: symmetrische Verschlüsselung mit ChaCha20, Nachrichtenauthentifizierung mit Poly1305, sowie andere wie Curve25519, BLAKE2 und SipHash24
- Unterstützt sowohl IPv4 als auch IPv6
- Multiplattform: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (und implementiert in ProtonVPN)
- Nur 4.000 Zeilen Code, im Vergleich zu Hunderttausenden bei anderen Lösungen



Für den kryptografischen Teil werden die verschiedenen verwendeten Algorithmen handverlesen, auf verschiedene Weise geprüft und von auf diesem Gebiet spezialisierten Sicherheitsforschern untersucht.



Die offizielle Website des Projekts: [wireguard.com](https://www.wireguard.com/)



Sind Sie nach dem Lesen dieser Einführung von dieser Lösung überzeugt? Dann müssen Sie nur noch weiter lesen!



## II. Diagramm des WireGuard-Labors



Bevor ich Ihnen mein Labor für die Einrichtung von WireGuard vorstelle, sollten Sie wissen, dass Sie sich vorstellen können, ** WireGuard zu verwenden, um zwei entfernte Infrastrukturen miteinander zu verbinden**, aber auch um **einen entfernten Client mit einer Infrastruktur wie einem Firmennetzwerk oder Ihrem Heimnetzwerk zu verbinden**. Dies ist im gleichen Sinne wie bei OpenVPN, wie wir kürzlich im Tutorial "[OpenVPN auf Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)" gesehen haben.



Wenn der WireGuard nicht direkt auf dem Router oder der Firewall eingerichtet ist, wie es mit OpenWRT denkbar ist, müssen Sie eine Portweiterleitung einrichten, damit der Datenstrom das WireGuard-Paar erreicht.



![Image](assets/fr/034.webp)



Jetzt erzähle ich Ihnen von meinem Labor und davon, was wir heute einrichten werden.



Ich werde einen Debian-11-Rechner als WireGuard-Server und einen Windows-Client als WireGuard-VPN-Client verwenden. Obwohl es ein wenig irreführend ist, von einer Client-Server-Beziehung zu sprechen, da **WireGuard auf einem "Peer-to-Peer "**-Modell arbeitet. Das ist ein wenig irreführend, wenn Sie versuchen, eine "Client-to-Site"-Verbindung einzurichten. Nehmen wir stattdessen an, dass ich zwei Paare oder **zwei WireGuard-Verbindungspunkte** haben werde, wenn Sie so wollen: einen unter Debian 11 und den anderen unter Windows.



Diese beiden Paare können in beide Richtungen miteinander kommunizieren, was bedeutet, dass ich von meinem Windows-Rechner aus auf das entfernte LAN des Debian 11-Rechners zugreifen kann und umgekehrt: alles hängt von der Konfiguration des Tunnels und der Firewall des WireGuard-Peers ab.



In diesem Beispiel werde ich mich auf den folgenden Fall konzentrieren: **Ich möchte von meinem Windows Peer 1, der mit meinem Heimnetzwerk verbunden ist, auf mein Firmennetzwerk zugreifen, um über den WireGuard VPN-Tunnel auf die Server der Firma zuzugreifen**. Dies ergibt das folgende Diagramm:



![Image](assets/fr/035.webp)



Bezogen auf die IP-Adressen ergibt dies:





- Heimnetzwerk**: 192.168.1.0/24
- Firmennetzwerk**: 192.168.100.0/24
- WireGuard-Tunnelnetzwerk**: 192.168.110.0/24


+ IP Address von Peer 1 (Windows) im Tunnel: 192.168.110.2/24


+ IP Address von Peer 2 (Debian) im Tunnel: 192.168.110.121/24



Das war's schon! Jetzt geht es an die Konfiguration!



**Hinweis: Standardmäßig arbeitet der WireGuard im UDP-Modus auf **Port 51820**.



## III Installation und Konfiguration des WireGuard-Servers



Ich werde in dieser Anleitung die Begriffe "Client" für den Windows-Rechner und "Server" für den Debian-Rechner verwenden, denn obwohl es sich um ein Peer-to-Peer-System handelt, scheint dies sinnvoller zu sein.



### A. Installation des WireGuard unter Debian 11



Das WireGuard-Installationspaket ist in den offiziellen Debian 11-Repositories verfügbar, so dass wir nur noch den Paket-Cache aktualisieren und es installieren müssen:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Der WireGuard-Server wird zusammen mit verschiedenen Tools installiert, die den Zugriff auf nützliche Befehle zur Verwaltung der Konfiguration ermöglichen.



### B. Installieren eines Interface WireGuard



Mit dem **Befehl "wg "** müssen wir generate einen privaten Schlüssel und einen öffentlichen Schlüssel erstellen, die für die Authentifizierung zwischen zwei Paaren, d. h. dem Server und einem Client (der ebenfalls ein Schlüsselpaar benötigt), unerlässlich sind.



Wir erstellen den privaten Schlüssel "**/etc/wireguard/wg-private.key**" und den öffentlichen Schlüssel "**/etc/wireguard/wg-public.key**" mit dieser Befehlsfolge:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Der Wert des öffentlichen Schlüssels wird in der Konsole zurückgegeben. In der Konfigurationsdatei des WireGuard müssen wir **den Wert unseres privaten Schlüssels** hinzufügen. Um diesen Wert abzurufen, geben Sie den folgenden Befehl ein und kopieren Sie den Wert:



```
sudo cat /etc/wireguard/wg-private.key
```



Es ist an der Zeit, eine Konfigurationsdatei in "**/etc/wireguard/**" zu erstellen. Wir können diese Datei z. B. "**wg0.conf**" nennen, wenn wir davon ausgehen, dass das mit WireGuard verbundene Interface-Netzwerk "wg0" sein wird, nach dem gleichen Prinzip wie z. B. "eth0".



```
sudo nano /etc/wireguard/wg0.conf
```



In dieser Datei müssen wir zunächst den folgenden Inhalt hinzufügen (wir werden später darauf zurückkommen, um ihn zu vervollständigen):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Die Sektion `[Interface]` wird verwendet, um den Serverteil zu deklarieren. Hier sind einige Informationen:





- Address**: die IP Address des Interface WireGuard innerhalb des VPN-Tunnels (anderes Subnetz als das entfernte LAN)
- SaveConfig**: Die Konfiguration wird so lange gespeichert (und geschützt), wie das Interface aktiv ist
- ListenPort**: Der Listening-Port des WireGuard. In diesem Fall ist 51820 der Standardport, aber Sie können ihn gerne anpassen
- PrivateKey**: der Wert des privaten Schlüssels unseres Servers (*wg-private.key*)



Speichern Sie die Datei und schließen Sie sie. Mit dem Befehl "**wg-quick**" können wir diesen Interface durch Angabe seines Namens (wg0, da die Datei wg0.conf heißt) starten:



```
sudo wg-quick up wg0
```



Wenn Sie die IP-Adressen Ihres Debian-11-Servers auflisten, sehen Sie einen neuen Interface mit dem Namen "wg0" und der in der Konfigurationsdatei definierten IP Address:



```
ip a
```



![Image](assets/fr/027.webp)



Im gleichen Sinne können wir die Interface-Konfiguration "wg0" mit dem Befehl "wg show" anzeigen:



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Schließlich müssen wir die automatische Inbetriebnahme unseres Interface wg0 WireGuard aktivieren:



```
sudo systemctl enable wg-quick@wg0.service
```



Für den Moment lassen wir die Konfiguration der WireGuard-Serverseite beiseite.



### C. IP-Weiterleitung einschalten



Damit unser Debian-11-Rechner in der Lage ist, **Pakete zwischen verschiedenen Netzwerken (wie ein Router)** weiterzuleiten, d. h. zwischen dem VPN-Netzwerk und dem lokalen Netzwerk, müssen wir [IP Forwarding] (https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/) aktivieren. Standardmäßig ist diese Funktion deaktiviert.



Ändern Sie diese Konfigurationsdatei:



```
sudo nano /etc/sysctl.conf
```



Fügen Sie die folgende Richtlinie am Ende der Datei hinzu und speichern Sie:



```
net.ipv4.ip_forward = 1
```



Mehr gibt es nicht zu sagen.



### D. IP-Masquerade aktivieren



Damit unser Server die Pakete korrekt weiterleiten kann und das entfernte LAN für den Windows-Rechner zugänglich ist, müssen wir IP Masquerade auf unserem Debian-Server aktivieren. Dies ist eine Art NAT-Aktivierung. Ich werde diese Konfiguration auf der Linux-Firewall über UFW durchführen, mit der ich vertraut bin ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Wenn Sie UFW noch nicht haben und es einrichten wollen (Sie können auch Nftables verwenden), installieren Sie zunächst:



```
sudo apt install ufw
```



Zunächst müssen Sie SSH aktivieren, um die Kontrolle über den entfernten Server nicht zu verlieren (passen Sie die Portnummer an):



```
sudo ufw allow 22/tcp
```



Port 51820 in UDP muss ebenfalls autorisiert werden, da wir ihn für WireGuard verwenden (passen Sie die Portnummer erneut an):



```
sudo ufw allow 51820/udp
```



Als Nächstes fahren wir mit der Konfiguration fort, um die IP-Masquerade zu aktivieren. Dazu müssen wir den Namen des Interface, der mit dem lokalen Netzwerk verbunden ist, herausfinden. Wenn Sie den Namen nicht kennen, führen Sie "ip a" aus, um den Namen der Karte zu erfahren. In meinem Fall ist es die Karte "**ens192**".



![Image](assets/fr/036.webp)



Wir werden diese Informationen verwenden. Bearbeiten Sie die folgende Datei:



```
sudo nano /etc/ufw/before.rules
```



Fügen Sie diese Zeilen am Ende der Datei hinzu, um **die IP-Masquerade auf dem Interface ens192** (passen Sie den Interface-Namen an) innerhalb der POSTROUTING-Zeichenkette der NAT-Tabelle unserer lokalen Firewall zu aktivieren:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Das Bild zeigt:



![Image](assets/fr/037.webp)



Lassen Sie diese Konfigurationsdatei geöffnet und fahren Sie mit dem nächsten Schritt fort 😉 



### E. Linux-Firewall-Konfiguration für WireGuard



In derselben Konfigurationsdatei geben wir das Unternehmensnetzwerk "192.168.100.0/24" an, damit wir es kontaktieren können. Hier sind die beiden Regeln, die hinzugefügt werden müssen (idealerweise nach dem Abschnitt "*# ok icmp code for FORWARD*", um die Regeln zusammenzufassen):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Wenn Sie nur einen Host zulassen wollen, zum Beispiel "192.168.100.11", ist das ganz einfach:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Nun können Sie die Datei speichern und schließen. Nun müssen Sie nur noch UFW aktivieren und den Dienst neu starten, um die Änderungen zu übernehmen:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Der erste Teil der Konfiguration des Debian-Servers ist nun abgeschlossen.



## IV. WireGuard-Client für Windows



Der WireGuard-Client ist für Windows, macOS, Android, etc. verfügbar. Das sind großartige Neuigkeiten. Alle Downloads sind auf dieser Seite verfügbar: [WireGuard-Client](https://www.wireguard.com/install/). In diesem Beispiel werde ich den Client unter Windows einrichten. Um den WireGuard-Client unter Linux einzurichten, folgen Sie demselben Prinzip wie bei der Erstellung der Datei wg0.conf auf dem Debian-Rechner (ohne all das NAT usw.).



### A. Installieren des WireGuard-Windows-Clients



Sobald Sie die ausführbare Datei oder das MSI-Paket heruntergeladen haben, ist die Installation ganz einfach: Starten Sie einfach das Installationsprogramm, und... voilà, es ist fertig 🙂 



![Image](assets/fr/038.webp)



### B. Erstellen Sie ein WireGuard-Profil



Öffnen Sie zunächst die Software, um einen neuen Tunnel zu erstellen. Klicken Sie dazu auf den Pfeil rechts neben der Schaltfläche "**Tunnel hinzufügen**" und klicken Sie auf die Schaltfläche "**Leeren Tunnel hinzufügen**".



![Image](assets/fr/028.webp)



Ein Konfigurationsfenster wird geöffnet. Jedes Mal, wenn eine neue Tunnelkonfiguration erstellt wird, generiert der WireGuard ein privates/öffentliches Schlüsselpaar speziell für diese Konfiguration. **In dieser Konfiguration müssen wir die "Gegenstelle", d.h. den entfernten Server, angeben:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Wir müssen diese Konfiguration vervollständigen, insbesondere um die IP Address auf diesem Interface (*Address*) zu deklarieren, aber auch um den entfernten WireGuard-Server über einen [Peer]-Block zu deklarieren. Das folgende Bild soll Sie an die Konfigurationsdatei erinnern, die wir auf der Linux-Serverseite erstellt haben.



Beginnen wir mit dem `[Interface]`-Block und fügen die IP Address "**192.168.110.2**" hinzu; denken Sie daran, dass der Server die IP Address "**192.168.110.121**" in diesem Netzwerksegment hat. Dies ergibt:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Als nächstes müssen wir den "Peer"-Block mit drei Eigenschaften deklarieren, was zu dieser Konfiguration führt:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



In Bildern:



![Image](assets/fr/029.webp)



**Ein paar Erklärungen zum [Peer]-Block:





- PublicKey**: dies ist der öffentliche Schlüssel des WireGuard Debian 11 Servers (Sie können seinen Wert mit dem Befehl "*sudo wg*" erhalten)
- AllowedIPs**: dies sind die IP-Adressen / Subnetze, die über dieses WireGuard VPN-Netzwerk zugänglich sind, in diesem Fall das Subnetz, das für mein WireGuard VPN (*192.168.110.0/24*) und mein entferntes LAN (*192.168.100.0/24*) spezifisch ist
- Endpunkt**: dies ist die IP Address des Debian 11-Hosts, da dies unser WireGuard-Verbindungspunkt ist (Sie müssen die öffentliche IP Address angeben)



Geben Sie schließlich in das Feld "**Name**" einen Namen ein (ohne Leerzeichen) und kopieren Sie den öffentlichen Schlüssel des Clients, da wir ihn auf dem Server deklarieren müssen. Klicken Sie auf "**Registrieren**".



### C. Client auf dem WireGuard-Server deklarieren



Es ist an der Zeit, zum Debian-Server zurückzukehren, um den "**Peer**", d.h. unseren Windows-PC, in der WireGuard-Konfiguration zu deklarieren. Zunächst müssen wir **den Interface "wg0"** stoppen, um seine Konfiguration zu ändern:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Ändern Sie nun die zuvor erstellte Konfigurationsdatei:



```
sudo nano /etc/wireguard/wg0.conf
```



In dieser Datei müssen wir nach dem `[Interface]`-Block einen `[Peer]`-Block deklarieren:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Dieser [Peer]-Block enthält den öffentlichen Schlüssel des Windows 10-PCs (**PublicKey**) und die IP Address des Interface des PCs (**AllowedIPs**): Der Server wird in diesem WireGuard-Tunnel nur kommunizieren, um den Windows-Client zu kontaktieren, daher der Wert "**192.168.110.2/32**".



Nun muss die Datei nur noch gespeichert werden (*Strg+O, dann Enter, dann STRG+X über Nano*). Starten Sie Interface "wg0" neu:



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Um zu überprüfen, ob die Peer-Deklaration funktioniert, können Sie diesen Befehl verwenden:



```
sudo wg show
```



Sobald der entfernte Host seine WireGuard-Verbindung aufgebaut hat, wird seine IP Address auf den Wert "Endpunkt" verschoben.



![Image](assets/fr/033.webp)



Schließlich sichern wir die Konfigurationsdateien, um den Root-Zugriff zu begrenzen:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Erste WireGuard-Verbindung



Nun, da die Konfiguration fertig ist, können wir sie vom Windows-PC aus einleiten. Klicken Sie dazu im "**WireGuard**"-Client auf die Schaltfläche "**Aktivieren**": Die Verbindung wird **von "Aus" auf "Ein "** geändert, aber das bedeutet nicht, dass sie funktioniert. Es hängt alles davon ab, ob Ihre Konfiguration korrekt ist oder nicht. **Wenn die Verbindung hergestellt ist, kommunizieren unsere beiden Maschinen über den Interface WireGuard, der auf beiden Seiten konfiguriert ist!



![Image](assets/fr/030.webp)



Falls ein Problem auftritt, wird dies in der Registerkarte "**Logbuch**" angezeigt. Die beiden Hosts werden regelmäßig Exchange-Pakete senden, um den Status der Verbindung zu überprüfen, daher die Meldungen "*Empfang von Keepalive-Paket von Peer 1*".



![Image](assets/fr/031.webp)



Wenn die Registerkarte "**Journal**" des WireGuard eine Meldung wie die folgende anzeigt, müssen Sie überprüfen, ob die auf beiden Seiten angegebenen öffentlichen Schlüssel korrekt sind.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Von meinem entfernten PC aus kann ich die IP Address meines Interface WireGuard auf der Serverseite anpingen, ebenso wie einen Host in meinem entfernten LAN.



![Image](assets/fr/032.webp)



### E. Leistung: OpenVPN vs. WireGuard



Von meinem Remote-PC, der mit meinem WireGuard VPN verbunden ist, konnte ich auf einen Dateiserver zugreifen und eine Datei über [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/) übertragen, um die Übertragungsrate zu sehen. **Mit WireGuard erreiche ich maximal etwa 45 Mb/s, was großartig ist, da ich über WiFi verbunden bin



![Image](assets/fr/025.webp)



Unter den gleichen Bedingungen, aber diesmal über eine OpenVPN-Verbindung (in UDP), mit dem gleichen Betrieb, ist der Durchsatz völlig anders: etwa 3 MB/s. Der Unterschied ist offensichtlich!



![Image](assets/fr/026.webp)



Das ist interessant, denn wenn Sie z. B. von einer WiFi-Verbindung zu einer 4G/5G-Verbindung wechseln, erfolgt die Wiederherstellung der Verbindung so schnell, dass die Unterbrechung nicht sichtbar ist.



### F. Bonus: voller Tunnel WireGuard



Bei der aktuellen Konfiguration fließt ein Teil des Datenverkehrs durch das VPN und der Rest durch die Internetverbindung des Kunden, einschließlich des Internetsurfens. Wenn wir in den WireGuard **Volltunnelmodus** wechseln wollen, so dass alles durch den VPN-Tunnel läuft, müssen wir einige Änderungen an unserer Konfiguration vornehmen....



Zuerst müssen Sie das Paket "resolvconf" auf der:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Sobald dies geschehen ist, müssen Sie das Profil "wg0.conf" auf dem Debian-Rechner ändern: Stoppen Sie Interface, ändern Sie es und starten Sie neu.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Als nächstes fügen wir **im Block `[Interface]` den zu verwendenden DNS-Server hinzu**. In meinem Fall ist es der Domain-Controller meines Labors, aber wir könnten auch Bind9 auf dem Debian-Rechner installieren, um einen lokalen Resolver zu haben.



```
DNS = 192.168.100.11
```



Speichern Sie die Datei, und starten Sie Interface neu:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Schließlich müssen Sie in der Tunnelkonfiguration auf der Windows 10-Arbeitsstation den Abschnitt "AllowedIPs" ändern, um anzugeben, dass alles durch den Tunnel laufen muss. Ersetzen Sie:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Von:



```
AllowedIPs = 0.0.0.0/0
```



Wie Sie sehen können, wird dadurch auch die Option "**Tötungsschalter*" aktiviert.



![Image](assets/fr/040.webp)



Schließlich nutzte ich diesen vollen Tunnel, um einen kleinen Strömungstest durchzuführen, dessen Ergebnisse unten dargestellt sind:



![Image](assets/fr/039.webp)



Die Konfiguration von WireGuard ist recht einfach und leicht zu verstehen und vor allem zu warten. **WireGuard gilt als die Zukunft der VPNs**, wir sollten es also im Auge behalten! Wir können auch sehen, dass der Vorteil in Bezug auf die Leistung erheblich ist, was ein großer Vorteil für WireGuard im Vergleich zu OpenVPN ist.



Zusätzliche Dokumentation:





- [Mann - Kommando wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Mann - Befehl wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**Ihr WireGuard VPN ist eingerichtet und läuft! Herzlichen Glückwunsch!