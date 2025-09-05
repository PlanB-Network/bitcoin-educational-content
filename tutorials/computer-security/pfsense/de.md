---
name: pfSense
description: Installieren von Pfsense
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian BURNEL, veröffentlicht auf [IT-Connect](https://www.it-connect.fr/). Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext des Autors wurden wesentliche Änderungen vorgenommen, um das Tutorial auf den neuesten Stand zu bringen.*



___



![Image](assets/fr/027.webp)



## I. Präsentation



pfSense ist ein freies Open-Source-Betriebssystem, das jeden Computer, dedizierten Server oder jede Hardware-Appliance in einen leistungsstarken, hoch konfigurierbaren Router und eine Firewall verwandelt. Basierend auf FreeBSD und bekannt für seine stabile, robuste Netzwerkarchitektur, setzt pfSense seit über fünfzehn Jahren den Standard für Open-Source-Firewalls für Unternehmen, Kommunen und anspruchsvolle Privatanwender.



Seine Hauptfunktionen haben sich im Laufe der Jahre erheblich weiterentwickelt und sind mit jeder neuen Version verbessert worden. Bis heute bietet pfSense:





- Vollständige, zentralisierte Verwaltung über ein modernes, intuitives und sicheres Interface Web-Interface.
- Leistungsstarke Stateful-Firewall mit erweiterter NAT-Unterstützung (einschließlich NAT-T) und granularer Regelverwaltung.
- Native Multi-WAN-Unterstützung, die die Aggregation oder Redundanz von Internetverbindungen ermöglicht.
- Integrierter DHCP-Server und -Relay.
- Hohe Verfügbarkeit durch CARP-Protokoll für Failover und die Möglichkeit, pfSense-Cluster zu konfigurieren.
- Lastausgleich zwischen mehreren Verbindungen oder Servern.
- Vollständige VPN-Unterstützung: IPsec, OpenVPN und WireGuard (ersetzt das inzwischen veraltete L2TP).
- Konfigurierbares Captive Portal für die Zugangskontrolle von Gästen, insbesondere in öffentlichen oder Hotelumgebungen.



pfSense verfügt auch über ein erweiterbares Paketsystem, das es einfach macht, erweiterte Funktionen wie einen transparenten Proxy (Squid), URL-Filterung oder IDS/IPS (Snort oder Suricata) direkt aus dem Interface Web hinzuzufügen.



pfSense wird nur für 64-Bit-Plattformen vertrieben, in Übereinstimmung mit den aktuellen FreeBSD-Empfehlungen. Es kann auf Standard-Hardware (PCs, Rack-Server) oder auf eingebetteten Plattformen mit geringem Stromverbrauch wie Netgate-Appliances oder bestimmten Low-Profile-x86-Boxen installiert werden, die weitaus leistungsfähiger sind als ältere Alix-Boxen.



Schließlich ist zu beachten, dass pfSense mindestens zwei physische Netzwerkschnittstellen benötigt: eine für den externen Bereich (WAN) und eine für das interne Netzwerk (LAN). Je nach Komplexität Ihrer Infrastruktur (DMZ, VLAN, mehrere WANs) können mehrere zusätzliche Schnittstellen erforderlich sein, um die Fähigkeiten von pfSense voll auszuschöpfen.



## II. Bild herunterladen



Die letzte stabile Version von pfSense, zum Zeitpunkt der Erstellung dieses Tutorials, ist 2.8 (veröffentlicht im Juni 2025). Sie können das ISO-Image oder die an Ihre Hardwareumgebung angepasste Installationsdatei direkt von der offiziellen Website herunterladen:





- [pfSense herunterladen](https://www.pfsense.org/download/)



Das Download-Portal ermöglicht Ihnen die Auswahl von:





- Architektur (im Allgemeinen **AMD64** für alle moderne Hardware).
- Imagetyp (**Installer USB Memstick** für die Installation über einen USB-Stick, **ISO Installer** für das Brennen oder die virtuelle Bearbeitung).
- Der nächstgelegene Download-Mirror, um die Übertragungsgeschwindigkeit zu optimieren.



Für diejenigen, die pfSense in einer virtualisierten Umgebung (Proxmox, VMware ESXi, VirtualBox...) einsetzen wollen, ist auch ein **OVA** Image verfügbar. Diese gebrauchsfertige virtuelle Maschine vereinfacht die Installation und Erstkonfiguration erheblich. Stellen Sie lediglich sicher, dass Sie die zugewiesenen Ressourcen (CPU, RAM, Netzwerkschnittstellen) entsprechend der erwarteten Last und Ihrer Netzwerktopologie anpassen.



Wir empfehlen, vor der Installation die Integrität der heruntergeladenen Datei zu überprüfen, indem Sie die auf der offiziellen Download-Seite angegebene **SHA256** überprüfen. Dadurch wird sichergestellt, dass das Image nicht verändert oder beschädigt wurde.



## III. Einrichtung



In diesem Beispiel wird die Installation auf einer virtuellen Maschine mit VirtualBox durchgeführt. Das Verfahren ist auf einer physischen Maschine oder einem anderen Hypervisor identisch, mit Ausnahme der Verwaltung virtueller Geräte.



### 1. Mindestanforderungen an die Hardware



Für einen Standardeinsatz empfehlen wir:





- mindestens 1 GB RAM** (2 GB oder mehr werden empfohlen, um zusätzliche Pakete oder ZFS-Unterstützung zu ermöglichen).
- 8 GB Festplattenspeicher** (20 GB oder mehr sind für fortgeschrittene Konfigurationen vorzuziehen, insbesondere wenn Sie einen Proxy-Cache, IDS/IPS oder detaillierte Protokolle installieren).
- Mindestens zwei virtuelle Netzwerkschnittstellen** (eine für das WAN, eine für das LAN). Fügen Sie diese in VirtualBox vor dem Start zu den VM-Einstellungen hinzu.



### 2. Start des Installationsprogramms



Binden Sie das heruntergeladene ISO-Image als virtuelles optisches Laufwerk in VirtualBox ein, oder stecken Sie den USB-Stick ein, wenn Sie auf einem physischen Rechner installieren. Beim Start wird ein Boot-Menü angezeigt:



Wenn Sie keine Optionen auswählen, wird pfSense nach ein paar Sekunden automatisch mit den Standardoptionen gestartet. Drücken Sie die Taste "**Enter**", um den normalen Startvorgang einzuleiten.



![Image](assets/fr/027.webp)



Wenn das Hauptmenü erscheint, drücken Sie kurz die Taste "**I**", um die Installation zu starten.



![Image](assets/fr/001.webp)



### 3. Erste Einstellungen des Installationsprogramms



Auf dem ersten Bildschirm können Sie einige regionale Parameter einstellen, z. B. die Schriftart und die Zeichenkodierung. Diese Einstellungen sind in bestimmten Fällen nützlich (nicht standardisierte Tastaturen, serielle Bildschirme, orientalische Sprachen). Für die meisten Installationen sollten Sie die Standardwerte beibehalten und "**Diese Einstellungen übernehmen**" wählen.



![Image](assets/fr/002.webp)



### 4. Wahl des Installationsmodus



Wählen Sie "**Quick/Easy Install**", um eine automatische Installation mit den empfohlenen Optionen durchzuführen. Diese Methode löscht die ausgewählte Festplatte und konfiguriert pfSense mit der Standardpartitionierung.



![Image](assets/fr/003.webp)



Es erscheint eine Warnung, die darauf hinweist, dass alle Daten auf dem Datenträger gelöscht werden. Bestätigen Sie mit "**OK**".



Das Installationsprogramm kopiert dann die erforderlichen Dateien auf die Festplatte. Je nach Hardware kann dies einige Sekunden bis einige Minuten dauern.



### 5. Auswahl des Kerns



Wenn das Installationsprogramm Sie auffordert, den Kernel-Typ auszuwählen, lassen Sie "**Standard Kernel**" ausgewählt. Dieser generische Kernel eignet sich perfekt für Standardinstallationen, ob auf einem PC, Server oder einer VM.



### 6. Ende der Installation und Neustart



Sobald die Installation abgeschlossen ist, wählen Sie "**Reboot**", um Ihren Rechner auf Ihrer neuen pfSense-Instanz neu zu starten.



**Wichtiger Hinweis**: Entfernen Sie das ISO-Image oder ziehen Sie den Installations-USB-Stick ab, bevor Sie das System neu starten, um zu vermeiden, dass das Installationsprogramm beim nächsten Start neu gestartet wird.



## IV. Erstmaliges Starten der pfSense



Bei der ersten Inbetriebnahme muss pfSense so konfiguriert werden, dass es seine Netzwerkschnittstellen (WAN, LAN, DMZ, VLANs, etc.) erkennt und korrekt zuordnet. Eine sorgfältige Identifizierung Ihrer Netzwerkkarten ist unerlässlich, um Konfigurationsfehler zu vermeiden, die Ihnen den Zugang zum Interface Web verwehren oder Ihre Firewall funktionsunfähig machen könnten.



Beim Start erkennt pfSense automatisch alle verfügbaren Netzwerkschnittstellen und listet sie auf, wobei die MAC Address für jede Schnittstelle angegeben wird. Dies macht es einfach, zwischen ihnen zu unterscheiden.



### 1. VLANs



Die erste Frage betrifft die Konfiguration von VLANs. In diesem Stadium werden wir bei einer Grundkonfiguration keine VLANs aktivieren. Drücken Sie also die Taste "**N**", um diesen Schritt zu überspringen.



![Image](assets/fr/004.webp)



### 2. WAN und LAN Interface Assignment



pfSense fordert Sie dann auf, zu definieren, welcher Interface für den WAN (Internetzugang) verwendet werden soll. Sie können wählen zwischen:





- Geben Sie den Interface-Namen manuell ein (empfohlen für virtuelle Umgebungen).
- Verwenden Sie die automatische Erkennung, indem Sie "**A**" drücken. Diese Option ist auf einem physischen Host nützlich, vorausgesetzt, Ihre Netzwerkkabel sind angeschlossen und die Verbindungen sind aktiv.



![Image](assets/fr/005.webp)



In diesem Beispiel wird das WAN manuell konfiguriert. Geben Sie den genauen Namen des Interface ein. Bei einer Intel-Karte lautet der Name unter FreeBSD oft "**em0**", er kann aber je nach Hardware variieren. Eine Realtek-Karte wird zum Beispiel oft als "**re0**" angezeigt.



![Image](assets/fr/006.webp)



Wiederholen Sie den gleichen Vorgang, um das Interface-LAN zu definieren. Hier verwenden wir "**em1**".



pfSense bestätigt, dass das Interface LAN sowohl die Firewall als auch NAT aktiviert, um Ihr internes Netzwerk zu schützen und die Address Übersetzung zu verwalten.



Wenn Sie über andere physische Schnittstellen verfügen, können Sie in diesem Stadium zusätzliche Schnittstellen (DMZ, Wi-Fi, spezifische VLANs) konfigurieren. Jeder logische Interface erfordert eine entsprechende Netzwerkkarte oder einen virtuellen Interface. Für die Erstkonfiguration beschränken wir uns auf WAN und LAN.



Nach Abschluss der Zuweisungen zeigt die pfSense eine übersichtliche Zusammenfassung der Entsprechungen zwischen physikalischen Schnittstellen und zugewiesenen Rollen an. Bestätigen Sie mit "**Y**".



### 3. PfSense-Konsole



Wenn dieser Schritt abgeschlossen ist, erscheint das Hauptmenü der pfSense-Konsole. Es bietet mehrere nützliche Optionen für die direkte Administration, wie das Zurücksetzen des Web-Passworts, den Neustart, das Neuladen der Konfiguration oder die Neuzuweisung von Schnittstellen.



![Image](assets/fr/007.webp)



Sie werden auch eine Zusammenfassung der aktuellen Netzwerkeinstellungen sehen, einschließlich der Standard-IP Address des Interface LAN, normalerweise **192.168.1.1**. Dies ist die Address, die Sie in Ihrem Browser eingeben müssen, um auf das Interface Verwaltungsweb zuzugreifen.



**Hinweis**: Wenn Ihr internes Netzwerk einen anderen Address-Bereich verwendet, wählen Sie im Menü "**2)** Interface(s) IP Address einstellen", um eine für Ihre Umgebung geeignete IP Address zuzuweisen.



Wenn Ihr Interface WAN mit einer DHCP-konfigurierten Box oder einem Modem verbunden ist, wird pfSense automatisch eine öffentliche IP Address beziehen. Sie sollten daher von einem sofortigen Internetzugang profitieren, indem Sie einen Client mit dem pfSense Interface LAN verbinden.



## V. Erster Zugang zu Interface Web



Sobald die Erstinbetriebnahme abgeschlossen und die Netzwerkschnittstellen konfiguriert sind, können Sie auf das pfSense Interface Web zugreifen, um Ihre Konfiguration zu finalisieren und fein abzustimmen.



### 1. Erste Verbindung



Schließen Sie einen Computer an den LAN-Port (oder das virtuelle Interface LAN in Ihrem Hypervisor) an und weisen Sie ihm ggf. eine IP Address im gleichen Bereich zu (standardmäßig verteilt pfSense automatisch eine Address über DHCP im LAN).



Gehen Sie in Ihrem Browser zu dem von der Konsole angegebenen Address (standardmäßig `https://192.168.1.1`). Beachten Sie, dass pfSense HTTPS sogar für die erste Verbindung benötigt - erwarten Sie also eine Warnung über ein selbstsigniertes Zertifikat, die Sie ignorieren können, indem Sie eine Ausnahme hinzufügen.



Der Anmeldebildschirm erscheint. Die Standard-Anmeldedaten sind:




- Benutzername:** `admin`
- Passwort:** `pfsense`



Diese Bezeichner werden während des Erstkonfigurationsassistenten geändert.



## VI. Einrichtungsassistent



Bei der ersten Verbindung fordert pfSense Sie auf, dem **Setup Wizard** zu folgen. Wir empfehlen Ihnen dringend, diesen zu verwenden, um sicherzustellen, dass alle wichtigen Parameter korrekt definiert sind.



### 1. Allgemeine Parameter



Sie können:




- Geben Sie einen Hostnamen und eine lokale Domäne an (Beispiel: `pfsense` und `lan.local`).
- Definieren Sie DNS-Server und wählen Sie, ob pfSense den DNS Ihres ISP oder einen externen Dienst (Cloudflare, OpenDNS, Quad9...) verwenden soll.



### 2. Zeitzone



Geben Sie die Zeitzone Ihres Standorts an, damit Protokolle und Zeitpläne konsistent sind (z. B. "Europa/Paris").



### 3. WAN-Konfiguration



Konfigurieren Sie die WAN-Verbindung:




- Die Standardeinstellung ist **DHCP** (ausreichend, wenn Sie sich hinter einer Box befinden).
- Wenn Sie eine feste IP haben, geben Sie die Parameter (statische IP, Maske, Gateway, DNS) manuell ein.
- Definieren Sie bei Bedarf ein VLAN oder eine PPPoE-Authentifizierung (bei einigen ISPs üblich).



### 4. LAN-Konfiguration



Der Assistent schlägt vor, das Standard-LAN-Subnetz zu ändern. Wenn Sie einen bestimmten Adressierungsplan haben, ist jetzt der richtige Zeitpunkt, ihn anzupassen.



### 5. Administratorkennwort ändern



Sichern Sie Ihre pfSense, indem Sie sofort ein sicheres Passwort für den Benutzer `admin` festlegen.



## VII. Überprüfung und Aktualisierung



Vergewissern Sie sich vor dem Einsatz Ihrer Firewall, dass Sie die neueste Version von:





- Gehen Sie zu **System > Update**.
- Wählen Sie den Aktualisierungskanal (normalerweise **Stabil**).
- Suchen Sie nach Aktualisierungen und wenden Sie diese an.



Es ist ratsam, Update-Benachrichtigungen zu aktivieren, damit Sie über Sicherheitspatches informiert werden.



## VIII. Abspeichern der Konfiguration



Bevor Sie größere Änderungen vornehmen, sollten Sie eine Sicherungsrichtlinie einführen:





- Gehen Sie zu **Diagnose > Sicherung und Wiederherstellung**.
- Laden Sie eine Kopie der aktuellen Konfiguration (`config.xml`) herunter.
- Bewahren Sie sie an einem sicheren Ort auf (verschlüsselter externer Datenträger).



Für unternehmenskritische Umgebungen sollten Sie eine automatische Konfigurationssicherung auf einem externen Server oder über ein programmiertes Skript in Betracht ziehen.



## IX. Bewährte Praktiken nach der Installation



So beenden Sie Ihren Einsatz in aller Ruhe:





- Ändern Sie die Firewall-Regeln**: pfSense erlaubt standardmäßig den gesamten ausgehenden Verkehr im LAN und blockiert den eingehenden Verkehr im WAN. Passen Sie diese Regeln nach Bedarf an.
- Konfigurieren Sie den sicheren Fernzugriff**: Aktivieren Sie bei Bedarf den Zugriff auf Interface web vom WAN aus nur über VPN oder mit IP-Beschränkungen.
- Benachrichtigungen aktivieren**: Konfigurieren Sie einen SMTP-Server für den Empfang von Benachrichtigungen (Ausfälle, Aktualisierungen, Fehler).
- Installieren Sie nützliche Erweiterungen**: zum Beispiel IDS/IPS (Snort, Suricata), Proxy (Squid), DNS-Filterung (pfBlockerNG).



Ihre pfSense Firewall ist nun einsatzbereit und kann Ihr Netzwerk schützen. Dank der Flexibilität und der aktiven Community verfügen Sie über ein leistungsstarkes, skalierbares Tool, das sich an Ihre zukünftigen Anforderungen anpassen kann (Multi-WAN, VLAN, Site-to-Site-VPN, Captive Portal usw.).



Konsultieren Sie regelmäßig die offizielle Dokumentation ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)), um neue Funktionen zu entdecken und sicherzustellen, dass Ihre Konfiguration aktuell und sicher ist.