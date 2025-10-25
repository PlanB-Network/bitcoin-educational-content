---
name: Tailscale
description: Fortgeschrittenes Tailscale-Tutorial
---
![cover](assets/cover.webp)



## 1. Einführung



Tailscale ist ein VPN der nächsten Generation, das ein verschlüsseltes Mesh-Netzwerk zwischen Ihren Geräten schafft. Es ermöglicht Ihnen, entfernte Maschinen so zu verbinden, als wären sie im selben lokalen Netzwerk, ohne komplexe Konfiguration oder Portöffnung.



Beim Self-Hosting weist Tailscale jedem Gerät eine feste private IP in einem virtuellen Netzwerk zu und bietet so einen stabilen Zugang zu Ihren Diensten, auch wenn sich Ihre öffentliche IP ändert. Dies bedeutet, dass Sie Ihre Server aus der Ferne verwalten können, ohne Ihre Dienste direkt dem Internet auszusetzen.



**Hauptanwendungen:**




- Verwalten eines persönlichen Servers von außen
- Verwalte Umbrel/Lightning-Knoten schneller als Tor
- Sicherer Zugang zu einem Raspberry Pi oder NAS
- Verbindung zu Ihren Diensten über SSH oder HTTP ohne komplexe Netzwerkkonfiguration



Dieser einfache Ansatz ermöglicht es Self-Hostern, sicher auf ihre Dienste zuzugreifen und dabei die Fallstricke herkömmlicher VPNs zu vermeiden.



## 2. Wie Tailscale funktioniert



Im Gegensatz zu herkömmlichen VPNs, die den gesamten Datenverkehr über einen zentralen Server leiten, schafft Tailscale ein Mesh-Netzwerk, in dem Geräte direkt miteinander kommunizieren. Der zentrale Server kümmert sich nur um die Authentifizierung und Schlüsselverteilung, ohne die Nutzerdaten zu sehen.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Abbildung 1: Traditionelles VPN mit Hub-and-Spoke-Architektur, bei dem der gesamte Datenverkehr über einen zentralen Server* läuft



Auf der Grundlage von WireGuard generiert jedes Gerät seine eigenen kryptografischen Schlüssel. Der Koordinierungsserver verteilt die öffentlichen Schlüssel an die Knoten, die dann direkt untereinander verschlüsselte End-to-End-Tunnel aufbauen. Um Firewalls zu überwinden, verwendet Tailscale NAT-Traversal und als letzten Ausweg DERP-Relays, die die Verschlüsselung aufrechterhalten.



![VPN maillé (mesh)](assets/fr/02.webp)


*Abbildung 2: Tailscale Mesh-Netzwerk, in dem Geräte direkt miteinander kommunizieren*



Die gesamte Kommunikation wird mit WireGuard verschlüsselt. Tailscale sieht nur die Metadaten (Verbindungen), aber niemals den Inhalt des Austauschs. Für mehr Souveränität ermöglicht Headscale, dass der Koordinierungsserver selbst gehostet wird.



**Sicherheit und Vertraulichkeit:** Dank WireGuard ist die gesamte Kommunikation auf Tailscale Ende-zu-Ende verschlüsselt. Tailscale kann Ihren Datenverkehr nicht lesen - nur Ihre Geräte haben die notwendigen privaten Schlüssel. Der Dienst sieht nur Metadaten: IP-Adressen, Gerätenamen, Zeitstempel der Verbindung und Peer-to-Peer-Verbindungsprotokolle (ohne Inhalt).



Diese Architektur ist jedoch von Tailscale Inc. für die Netzwerkkoordination abhängig. Um diese Abhängigkeit zu beseitigen, bietet Headscale eine Open-Source-Alternative an, die es Ihnen ermöglicht, den Kontrollserver selbst zu hosten und gleichzeitig die offiziellen Tailscale-Clients zu nutzen, um so die vollständige Souveränität über Ihre Netzwerkinfrastruktur zu gewährleisten, allerdings auf Kosten einer technisch aufwendigeren Konfiguration.



**Für eine detaillierte Erklärung der inneren Funktionsweise von Tailscale, einschließlich Control-Plane-Management, NAT-Traversal und DERP-Relais, empfehlen wir den ausgezeichneten Artikel** [How Tailscale Works] (https://tailscale.com/blog/how-tailscale-works) **auf dem offiziellen Blog. Dieser Artikel erklärt ausführlich die technischen Konzepte, die Tailscale so leistungsfähig machen.**



## 3. Installation von Tailscale



Tailscale läuft auf **den meisten gängigen** Betriebssystemen (Windows, macOS, Linux, iOS, Android). Die Installation soll auf allen Plattformen "schnell und einfach" sein. Beginnen wir mit einem Blick auf Interface und die Erstellung eines Kontos und gehen dann weiter zu den Installationsverfahren für verschiedene Umgebungen.



### 3.1 Erstellung eines Tailscale-Kontos



Gehen Sie zu [https://tailscale.com/](https://tailscale.com/) und klicken Sie auf die Schaltfläche "Erste Schritte" oben rechts auf der Seite.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Die Tailscale-Homepage erklärt das Konzept und bietet einen kostenlosen Start*



Um Tailscale zu nutzen, müssen Sie zunächst ein Konto über einen Identitätsanbieter erstellen:



![Page de connexion Tailscale](assets/fr/04.webp)


*Wahl des Identitätsanbieters für die Verbindung zu Tailscale (Google, Microsoft, GitHub, Apple, usw.)*



Nach dem Einloggen fragt Tailscale Sie nach einigen Informationen über Ihren Verwendungszweck:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Formular zum besseren Verständnis Ihres Anwendungsfalls (privat oder beruflich)*



Sobald Sie Ihr Konto erstellt haben, können Sie Tailscale auf Ihren Geräten installieren:



![Ajout du premier appareil](assets/fr/07.webp)


*Mit Tailscale können Sie die Anwendung auf verschiedenen Systemen installieren*



### 3.2 Installation auf verschiedenen Plattformen





- **Unter Windows und macOS:** Laden Sie einfach die grafische Anwendung von der offiziellen Tailscale-Website herunter und installieren Sie sie (.msi-Datei auf Windows, .dmg-Datei auf Mac). Nach der Installation startet die Anwendung einen grafischen Interface, mit dem Sie sich (über einen Browser) mit Ihrem Tailscale-Konto verbinden können, um den Rechner zu authentifizieren.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Anschließen eines MacBook an die Heckklappe*



![Connexion réussie](assets/fr/09.webp)


*Bestätigung, dass das Gerät mit dem Tailscale*-Netzwerk verbunden ist





- **Unter Linux (Debian, Ubuntu, etc.):** Sie haben mehrere Möglichkeiten. Die einfachste Methode ist, das offizielle Installationsskript auszuführen: zum Beispiel unter Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Dieses Skript wird das offizielle Tailscale-Repository hinzufügen und das Paket installieren. Sie können auch [manuell das APT-Repository hinzufügen] (https://pkgs.tailscale.com) oder normale Snap- oder apt-Pakete verwenden. Nach der Installation wird daemon `tailscaled` im Hintergrund laufen. Sie müssen dann den Knoten **authentifizieren** (siehe Interface CLI vs. Web unten). Bei anderen Distributionen (Fedora, Arch...) ist das Paket auch über die Standard-Repositories oder das universelle Installationsskript verfügbar. Für einen Headless-Server verwenden Sie CLI: zum Beispiel `sudo tailscale up --auth-key <key>`, wenn Sie einen vorgenerierten Authentifizierungsschlüssel verwenden, oder einfach `tailscale up` für eine interaktive Anmeldung (die eine URL zur Authentifizierung des Geräts bereitstellt).





- Auf ARM-basierten Systemen (Raspberry Pi, etc.): Wir sind in der Regel auf Linux, also der gleiche Ansatz wie oben (Skript oder Paket). Beachten Sie, dass Tailscale die ARM32/ARM64-Architektur ohne Probleme unterstützt. Viele Nutzer installieren Tailscale auf dem Raspberry Pi OS über apt oder auf leichtgewichtigen Distributionen (DietPi, etc.), um überall auf ihren Pi zugreifen zu können.





- Auf iOS und Android: **Tailscale** bietet **offizielle** mobile Anwendungen. Installieren Sie einfach *Tailscale* aus dem [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) oder dem [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Schritte zur Installation von Tailscale auf dem iPhone: Willkommen, Datenschutz, Benachrichtigungen, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Mit Tailnet verbinden, Konto auswählen und auf dem iPhone bestätigen*



Sobald die App installiert ist, werden Sie beim ersten Start aufgefordert, sich über den gewählten Anbieter (Google, Apple ID, Microsoft usw., je nachdem, was Sie für Tailscale verwenden) zu authentifizieren - es ist das gleiche Verfahren wie auf anderen Plattformen, in der Regel eine Weiterleitung zu einer OAuth-Webseite. Danach erstellt die mobile App das VPN (auf iOS müssen Sie das VPN-Konfigurations-Add-on akzeptieren). Die App kann dann im Hintergrund ausgeführt werden, so dass Sie von überall aus auf Ihr Tailnet zugreifen können. *Bitte beachten Sie:* Auf dem Handy können Sie nur **ein aktives VPN zur gleichen Zeit** haben - stellen Sie also sicher, dass Sie kein anderes VPN zur gleichen Zeit verbunden haben, sonst kann Tailscale sein eigenes nicht aufbauen. Auf Android können Sie ein separates Arbeitsprofil einrichten, wenn Sie bestimmte Anwendungen isolieren möchten (z. B. ein Profil mit Tailscale aktiv für eine bestimmte App).



### 3.3 Hinzufügen mehrerer Geräte und Validierung



Sobald Ihr erstes Gerät verbunden ist, fordert Tailscale Sie auf, weitere Geräte zu Ihrem Netzwerk hinzuzufügen:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface zeigt das erste angeschlossene Gerät an und wartet auf weitere Geräte*



Wenn Sie mehrere Geräte hinzugefügt haben, können Sie überprüfen, ob sie miteinander kommunizieren können:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Bestätigung, dass die Geräte über ping* miteinander kommunizieren können



Tailscale schlägt dann zusätzliche Konfigurationen vor, um Ihr Erlebnis zu verbessern:



![Suggestions de configuration](assets/fr/14.webp)


*Vorschläge für die Einrichtung von DNS, die gemeinsame Nutzung von Geräten und die Verwaltung des Zugangs*



### 3.4 Dashboard für die Verwaltung



Über die Webadministrationskonsole können Sie alle angeschlossenen Geräte anzeigen und verwalten:



![Tableau de bord des machines](assets/fr/15.webp)


*Liste der angeschlossenen Geräte mit deren Eigenschaften und Status*



**Interface Web vs. Interface CLI:** Tailscale bietet zwei sich ergänzende Möglichkeiten der Interaktion mit dem Netzwerk: die **Interface Web-Administration** und den **Command-line Client (CLI)**.





- **Interface Web (Admin-Konsole)**: Diese Web-Konsole ist unter [https://login.tailscale.com](https://login.tailscale.com) erreichbar und ist das zentrale Dashboard für Ihr Tailscale-Netzwerk. Sie listet alle Geräte (*Maschinen*), ihren Online-/Offline-Status, ihre Tailscale-IP-Adressen und mehr auf. Hier können Sie Geräte **verwalten** (umbenennen, Schlüssel ablaufen lassen, Routen autorisieren, einen Knoten deaktivieren), **Benutzer** (im organisatorischen Kontext) verwalten und Sicherheitsregeln (ACLs) definieren. Hier können Sie auch globale Optionen wie MagicDNS, Tags oder Autorisierungsschlüssel (vor generate Autorisierungsschlüssel für das automatische Hinzufügen von Geräten) konfigurieren. Interface Web ist sehr praktisch, um sich einen Überblick zu verschaffen und Änderungen vorzunehmen, die über den Koordinierungsserver an alle Knoten weitergegeben werden. *Beispiel:* Die





- **Interface Kommandozeile (CLI):** Der `tailscale` Befehl ist in CLI auf jedem Gerät verfügbar, auf dem Tailscale installiert ist. Mit diesem CLI können Sie alles lokal machen: Verbinden (`tailscale up`), den Status überprüfen (`tailscale status`, um zu sehen, welche Peers verbunden sind), debuggen (`tailscale ping <ip>`), und so weiter. Einige Funktionen sind sogar **exklusiv für CLI** oder noch fortgeschrittener, zum Beispiel:





  - `tailscale up --advertise-routes=192.168.0.0/24`, um eine Subnetz-Route anzukündigen,
  - tailscale up --advertise-exit-node", um Ihren Rechner als Exit-Node vorzuschlagen,
  - `tailscale set --accept-routes=true` (oder `--exit-node=<IP>`), um eine Route zu konsumieren oder einen Exit-Node zu verwenden,
  - `tailscale ip -4`, um die Tailscale-IP des Geräts anzuzeigen,
  - tailscale lock/unlock" (bei Verwendung von *tailnet-lock*, erweiterte Sicherheitsfunktion),
  - oder "tailscale file send <node>", um **Taildrop** (Dateiübertragung zwischen Geräten) zu verwenden.


CLI ist sehr nützlich auf Servern ohne Interface-Grafik und für das Skripting bestimmter Aktionen. **Unterschiede bei der Verwendung:** Die meisten grundlegenden Konfigurationen können entweder über das Web oder über den CLI vorgenommen werden. Das Hinzufügen eines Geräts zum Beispiel erfolgt entweder durch Eingabeaufforderung über die Konsole oder durch Ausführen von "tailscale up" auf dem Gerät und Validierung über das Web. Auch das Umbenennen eines Geräts kann über die Konsole oder mit "tailscale set --hostname" erfolgen. **Zusammenfassend lässt sich sagen, dass die Web-Konsole ideal für die globale Netzwerkadministration ist (insbesondere bei mehreren Rechnern/Benutzern), während CLI für die feinkörnige Steuerung eines bestimmten Rechners, für Automatisierungsskripte oder für die Verwendung auf einem System ohne GUI praktisch ist.**



## 4. Verwendung von Tailscale auf Umbrel



Umbrel ist eine beliebte Self-Hosting-Plattform (vor allem für Bitcoin/Lightning-Knoten und andere selbst gehostete Dienste, die über den App Store angeboten werden). Um Umbrel zu installieren und zu konfigurieren, empfehlen wir Ihnen, unserem Tutorial zu folgen:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Der gemeinsame Einsatz von Umbrel und Tailscale ist ein besonders interessanter Anwendungsfall, da Umbrel nativ ein einfach zu implementierendes Tailscale-Modul integriert. Hier erfahren Sie, wie sich Tailscale in Umbrel integriert und was es bringt:



### 4.1 Installation und Konfiguration des Regenschirms





- **Installation von Tailscale auf Umbrel:** Umbrel hat eine offizielle Tailscale-Anwendung in seinem App Store. Die Installation könnte nicht einfacher sein:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Tailscale-Anwendungsseite im Umbrel App Store*



Öffnen Sie auf dem Interface Web Umbrel den App Store, suchen Sie nach **Tailscale** und klicken Sie auf *Installieren*. Ein paar Sekunden später ist die Anwendung auf dem Umbrel installiert. Wenn Sie sie öffnen, zeigt Umbrel eine Seite an, die es Ihnen ermöglicht, Ihren Knoten mit Tailscale zu verbinden.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Anschlussbildschirm in Umbrels Interface* (Tailscale)



Klicken Sie einfach **auf "Anmelden "**, was Sie auf die Tailscale-Authentifizierungsseite weiterleiten wird:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Verbindung zu Tailscale über einen Identitätsanbieter*



Sie können sich über Ihr Tailscale-Konto (Google/GitHub/etc.) authentifizieren oder Ihre E-Mail eingeben. Bei Umbrel bittet Interface Sie normalerweise, [https://login.tailscale.com](https://login.tailscale.com) zu besuchen und sich einzuloggen - dies authentifiziert die Umbrel Tailscale App.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Bestätigung, dass das Umbrel-Gerät mit dem Tailscale-Netzwerk verbunden ist*



Sobald dies geschehen ist, ist Ihr Umbrel "in" Ihrem Tailscale-Netzwerk und erscheint auf Ihrer Konsole mit einem Namen (z.B. *umbrel*). Sie können dann auf die IP Address Ihrer Geräte klicken, um sie zu kopieren, die IPv6 Address oder Ihren MagicDNS abzurufen, der mit Ihrem Gerät verbunden ist.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Die Tailscale-Administrationskonsole zeigt mehrere angeschlossene Geräte, darunter Umbrel*




### 4.2 Fernzugriff auf die Umbrel-Dienste



Sobald Umbrel mit Tailscale verbunden ist, **kannst du von überall auf Interface Umbrel und die darauf laufenden Anwendungen zugreifen, als ob du dich im lokalen Netzwerk befindest**. Dies ist einer der Hauptvorteile gegenüber Tor.



Der Zugang ist denkbar einfach: Anstatt `umbrel.local` zu verwenden (was nur in Ihrem lokalen Netzwerk funktioniert), verwenden Sie die Tailscale IP Address (`http://100.x.y.z`) von Umbrel direkt von jedem Gerät aus, das mit Ihrem Tailnet verbunden ist. Dies funktioniert unabhängig davon, wo Sie sich befinden oder welche Internetverbindung Sie nutzen (4G, öffentliches Wi-Fi, Firmennetzwerk).



**Beispiele für von Umbrel gehostete Anwendungen, die über Tailscale zugänglich sind:**





- **Interface main Umbrel**: Greifen Sie auf Ihr Umbrel-Dashboard zu, indem Sie einfach `http://100.x.y.z` in Ihren Browser eingeben
- **Bitcoin-Knoten**: Verwalten Sie Ihren Bitcoin-Knoten ohne Latenz, sehen Sie sich die Synchronisation und Statistiken an
- **Lightning-Knoten**: Nutzen Sie ThunderHub, RTL oder andere Lightning-Management-Schnittstellen mit sofortiger Reaktionsfähigkeit
- **Mempool**: Anzeige von Bitcoin-Transaktionen und Mempool ohne Tor-Verzögerungen
- **noStrudel**: Zugang zu Ihren Nostr-Diensten, die auf Umbrel gehostet werden



**Verbinden Sie externe Geldbörsen mit Ihrem Bitcoin oder Lightning-Knoten über Tailscale**



Tailscale ermöglicht auch, dass Ihre Bitcoin und Lightning Wallets, die auf anderen Geräten installiert sind, sich direkt mit Ihrem Umbrel-Knoten verbinden können:





- **Sparrow wallet (Bitcoin)**: Dieses externe Wallet Bitcoin kann direkt mit dem Electrum-Server von Umbrel verbunden werden, indem das Tailscale IP Address verwendet wird:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Konfiguration eines privaten Electrum-Servers in Sparrow wallet mit Umbrels Tailscale IP Address*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Liste der Electrum-Server-Aliase in Sparrow mit Umbrel Tailscale IP Address*



Lesen Sie unsere vollständige Anleitung zur Konfiguration von Sparrow wallet mit Ihrem Bitcoin-Knoten:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- **Zeus (Lightning)**: Dieser Wallet mobile Lightning kann sich mit Ihrem Lightning-Knoten auf Umbrel verbinden. Anstatt den Endpunkt als `.onion' zu konfigurieren, stelle einfach die Tailscale IP deines Umbrel und den Lightning API Port ein. Die Verbindung wird im Vergleich zu Tor augenblicklich sein.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Konfiguration von Zeus zur Verbindung mit dem Lightning-Knoten über den Tailscale* IP Address



Wie Sie Zeus mit Ihrem Lightning-Knoten konfigurieren, erfahren Sie in unserem ausführlichen Tutorial:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Um mehr über das Lightning Network und seine Funktionsweise bei Umbrel zu erfahren, besuchen Sie die Website:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Vorteile gegenüber Tor



Umbrel bietet von Haus aus einen Fernzugriff über Tor an (indem es `.onion'-Adressen für seine Webdienste bereitstellt). Während Tor den Vorteil der Vertraulichkeit (Anonymität) hat und keine Registrierung erfordert, finden viele Nutzer **Tor langsam und instabil** für den alltäglichen Gebrauch (Seiten laden langsam, Timeouts, etc.) - *"Umbrel über Tor ist so langsam "* beschweren sich einige.



Tailscale bietet eine allgemein **schnellere Verbindung mit niedriger Latenz**, da der Datenverkehr direkt (oder über einen schnellen Relay) läuft, anstatt durch 3 Tor-Knoten zu springen. Darüber hinaus bietet Tailscale ein "lokales Netzwerk"-Erlebnis: Es werden private IPs verwendet und Anwendungen können direkt gemappt werden (z.B. SMB-Netzlaufwerk auf \100.x.y.z).



Allerdings hat Tor den Vorteil, dass es dezentralisiert und "out of the box" auf Umbrel ist, während Tailscale das Vertrauen in eine dritte Partei (oder das Hosting von Headscale) erfordert. Tor ist auch nützlich für den clientlosen Zugang (von jedem Tor-Browser aus kann man die Umbrel-Benutzeroberfläche konsultieren, während Tailscale den auf dem zugreifenden Gerät installierten Client erfordert).



**Zusammenfassend lässt sich sagen, dass Tailscale bei interaktiver Nutzung (Lightning Wallets, häufige Webschnittstellen) im Vergleich zu Tor einen deutlichen Komfort und eine höhere Geschwindigkeit bietet, allerdings um den Preis einer leichten Abhängigkeit von außen. Viele Leute nutzen *beides*: Tailscale im Alltag und Tor als Ausweichlösung oder um den Zugang mit jemandem zu teilen, ohne ihn in ihr VPN einzuladen.**



### 4.4 Sicherheit



Durch die Verwendung von Tailscale mit Umbrel vermeiden Sie, Umbrel dem Internet auszusetzen. Der Umbrel-Knoten ist nur für Ihre anderen authentifizierten Geräte im Tailnet zugänglich, was die Angriffsfläche erheblich reduziert (kein offener Port für Fremde, kein Risiko eines Angriffs auf den Webdienst über das Internet).



Die Kommunikation wird verschlüsselt (WireGuard), zusätzlich zu jeder Verschlüsselung, die Ihre Dienste bereits vornehmen (z.B. ist sogar internes HTTP im Tunnel). Sie können immer noch Tailscale ACLs anwenden, um z.B. zu verhindern, dass ein bestimmtes Tailnet-Gerät auf Umbrel zugreift, wenn Sie das Netz partitionieren wollen. Umbrel selbst merkt den Unterschied nicht - es denkt, dass es lokal bedient wird.



---

Zum Abschluss dieses Abschnitts: Die Integration von Tailscale auf Umbrel erfordert nur wenige Klicks und verbessert **die Zugänglichkeit** Ihres selbst gehosteten Knotens erheblich. Sie werden in der Lage sein, Umbrel und seine Dienste von jedem Ort aus zu verwalten, sicher und effizient, als ob Sie zu Hause wären. Dies ist eine besonders nützliche Lösung für Echtzeitanwendungen (Lightning), die unter der Tor-Latenz leiden, oder generell für jeden Selfhoster, der eine einfache private Verbindung sucht. Alles ohne **einen einzigen Port** auf deinem Rechner freizugeben und ohne komplizierte Netzwerkkonfiguration.



## 5. Erweiterte Verwaltung und Anwendungsfälle



### 5.1 Erweiterte Funktionen von Tailscale



**Netzwerkverwaltung:** Über die Administrationskonsole (login.tailscale.com) können Sie Ihre Geräte verwalten, Verbindungen einsehen und Zugriffsregeln konfigurieren.



**MagicDNS:** Löst automatisch Gerätenamen auf (z.B. `raspberrypi.tailnet.ts.net`), um sich keine IP-Adressen merken zu müssen.



**ACL und Zugriffskontrolle:** Definieren Sie über JSON-Regeln genau, wer auf was in Ihrem Netzwerk zugreifen darf, ideal für die Isolierung bestimmter Geräte oder die Einschränkung des Zugriffs auf bestimmte Dienste.



**Mit der Gerätefreigabe können Sie jemanden zum Zugriff auf einen bestimmten Rechner einladen, ohne ihm Zugriff auf Ihr gesamtes Netzwerk zu gewähren.**



**Subnetz-Router:** Eine Tailscale-Maschine kann als Gateway für ein ganzes Subnetz fungieren und ermöglicht den Zugriff auf Nicht-Tailscale-Geräte (IoT, Drucker, etc.) über eine einzige konfigurierte Maschine.



**Ausgangsknoten:** Verwenden Sie einen Rechner als Internet-Gateway, um mit seiner IP zu gehen. Nützlich für öffentliches Wi-Fi oder zur Umgehung geografischer Beschränkungen.



**Taildrop:** Eine sichere Alternative zu AirDrop, die es Ihnen ermöglicht, Dateien zwischen Ihren Tailscale-Geräten zu übertragen, unabhängig von deren Plattform oder Standort. Im Gegensatz zu AirDrop, das auf das Apple-Ökosystem und räumliche Nähe beschränkt ist, funktioniert Taildrop zwischen all Ihren Geräten (Windows, Mac, Linux, Android, iOS), auch wenn sie sich in verschiedenen Ländern befinden. Die Dateien werden direkt zwischen den Geräten mit Ende-zu-Ende-Verschlüsselung übertragen, ohne einen zentralen Server zu passieren. Verwenden Sie je nach System die Befehlszeile "taildrop file cp" oder die grafische Anwendung Interface.



### 5.2 Vergleich mit anderen Lösungen



**Vs OpenVPN:** Tailscale ist viel einfacher zu konfigurieren (keine zu öffnenden Ports, keine Zertifikatsverwaltung), erfordert aber die Abhängigkeit von einem Drittanbieterdienst. OpenVPN ist vollständig steuerbar, erfordert aber mehr Fachwissen.



**Als direkter Konkurrent arbeitet ZeroTier mit Layer 2 (Ethernet) und ermöglicht Broadcast/Multicast, während Tailscale mit Layer 3 (IP) arbeitet. ZeroTier bietet eine größere Netzwerkflexibilität, während Tailscale die Einfachheit der Nutzung bevorzugt.**



**Vs Tor:** Tor bietet Anonymität, die Tailscale nicht bietet, ist aber viel langsamer. Tor ist dezentralisiert und erfordert kein Konto, während Tailscale schneller ist und eine LAN-ähnliche Erfahrung bietet.



**Vs WireGuard manuell:** Tailscale automatisiert die gesamte Schlüssel- und Verbindungsverwaltung, die Sie bei WireGuard raw manuell durchführen müssen. Es ist im Wesentlichen WireGuard + ein vereinfachtes Management Layer.



Zusammenfassend lässt sich sagen, dass sich Tailscale als moderne, auf Einfachheit ausgerichtete Lösung positioniert, die ideal für den persönlichen Gebrauch und kleine Teams ist. Für Puristen, die die totale Kontrolle wollen, bietet Headscale eine Alternative für das Selbst-Hosting.



## 6. Schlussfolgerung



**Tailscale-Vorteile:** Tailscale bietet mehrere Vorteile für das Selbst-Hosting:





- **Einfachheit und Leistung** - Schnelle Installation auf allen Plattformen ohne komplexe Netzwerkkonfiguration. Der Datenverkehr folgt dem direktesten Weg zwischen Ihren Rechnern (P2P Mesh), mit der Leistung des WireGuard-Protokolls und ohne zentralen Server zur Begrenzung des Durchsatzes.
- **Sicherheit und Flexibilität** - Ende-zu-Ende-Verschlüsselung, reduzierte Angriffsfläche und erweiterte Funktionen (ACL, SSO/MFA-Authentifizierung). Funktioniert auch hinter NATs oder unterwegs, mit Subnetz-Routern und Exit-Knoten zur Anpassung des Netzwerks an Ihre Bedürfnisse.



**Grenzen:** Denken Sie auch daran:





- **Externe Abhängigkeit** - In seiner Standardversion ist der Dienst von der Infrastruktur von Tailscale Inc. abhängig. Diese Abhängigkeit kann über Headscale (selbstgehostete Alternative) umgangen werden.
- **Andere Einschränkungen** - Teilweise geschlossener Quellcode, Einschränkungen der kostenlosen Version für bestimmte fortgeschrittene Anwendungen, keine Unterstützung für Layer 2 (Broadcast/Multicast) und Notwendigkeit eines Internetzugangs zum Verbindungsaufbau.



**Tailscale ist ideal für einzelne Selbsthoster und kleine Teams, Entwickler, die Zugang zu verteilten Ressourcen benötigen, VPN-Einsteiger und mobile Nutzer. Für Unternehmen, die eine vollständige Kontrolle benötigen, können andere Lösungen wie Headscale oder WireGuard direkt vorzuziehen sein.**



**Erkunden Sie Headscale für vollständiges Self-Hosting, API und DevOps-Integrationen (Terraform) oder Alternativen wie Innernet (ähnlich, aber vollständig selbst gehostet) und Netmaker.**



Tailscale ist dank seiner Einfachheit und Effizienz ein unverzichtbares Werkzeug für das Selbst-Hosting. Es macht Ihre private Infrastruktur so zugänglich, als wäre sie in der Cloud, während Sie die Kontrolle zu Hause behalten.



## 7. Nützliche Ressourcen



### Offizielle Dokumentation





- **Tailscale Dokumentationszentrum**: [docs.tailscale.com](https://docs.tailscale.com) - Vollständige englische Dokumentation, Installationsanleitungen, Tutorials und technische Referenzen.
- **Wie Tailscale funktioniert**: [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) - Detaillierter Artikel, der die Funktionsweise von Tailscale erklärt.
- **Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Verfolgung von Updates und neuen Funktionen.



### Praktische Leitfäden





- **Homelab-Tutorials**: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Spezielle Anleitungen für das Selbsthosten.
- **Konfigurieren eines Exit Nodes**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Ausführliche Anleitung zur Konfiguration von Exit Nodes.
- **Taildrop** verwenden: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Übertragen Sie Dateien zwischen Tailscale-Geräten.



### Vergleiche





- **Tailscale vs. andere Lösungen**: [tailscale.com/compare](https://tailscale.com/compare) - Detaillierte Vergleiche mit anderen VPN- und Netzwerklösungen (ZeroTier, OpenVPN, etc.).



### Gemeinschaft





- **Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Diskussionen, Fragen und Feedback.
- **GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Kunden-Quellcode, wo Sie die Entwicklung verfolgen und Probleme melden können.
- **Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Gemeinschaft von Benutzern und Entwicklern.



Tailscale bietet regelmäßig neue Inhalte und Funktionen. Besuchen Sie den [offiziellen Blog] (https://tailscale.com/blog/) für die neuesten Nachrichten und Fallstudien.