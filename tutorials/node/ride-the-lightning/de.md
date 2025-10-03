---
name: Ride The Lightning (RTL)
description: Verwenden Sie Ride The Lightning (RTL), um Ihren Lightning-Knoten zu verwalten
---
![cover](assets/cover.webp)


## 1. Einführung



**Ride The Lightning (RTL)** ist eine vollständige Interface-Webanwendung zur Verwaltung eines Lightning Network-Knotens. Diese selbst gehostete Webanwendung bietet ein Lightning-**"Cockpit"**, das über Ihren Browser zugänglich ist. RTL funktioniert mit allen wichtigen Lightning-Implementierungen (LND, Core Lightning/CLN und Eclair) und gibt Ihnen die volle Kontrolle über Ihren Knoten und Ihre Kanäle. RTL ist Open-Source (MIT-Lizenz) und kostenlos und standardmäßig in viele schlüsselfertige Node-Lösungen (RaspiBlitz, MyNode, Umbrel, etc.) integriert.



**Ohne ein grafisches Interface können Lightning-Knoten nur über benutzerfreundliche CLI-Befehle verwaltet werden. RTL vereinfacht diese Vorgänge mit einem ergonomischen Interface. Hier sind die** **Hauptanwendungen**:





- Betrachten Sie Ihre Kanäle und Knoten - Das Dashboard zeigt den On-Chain-Saldo, die Lightning-Liquidität (lokal/fern), den Synchronisierungsstatus, den Knoten-Alias und mehr an. Sie können Ihre Kanalliste, Kapazität, lokale/ferne Verteilung und den Status anzeigen. RTL bietet kontextabhängige Dashboards, um die Aktivitäten aus verschiedenen Blickwinkeln zu analysieren.





- **Blitzschnelle Kanalverwaltung** - Öffnen und schließen Sie Kanäle mit wenigen Klicks. Mit RTL können Sie sich mit einem Peer verbinden und einen Kanal ohne einen Befehl öffnen. Sie können Routing-Gebühren anpassen, den Kontostand einsehen oder eine zirkuläre Umschichtung einleiten, um Fonds zwischen Kanälen neu zu verteilen.





- **Verfolgen und Ausführen von Zahlungen** - RTL verwaltet Lightning-Transaktionen: Senden Sie Zahlungen über Rechnungen, generate Rechnungen zu empfangen, verfolgen Sie Transaktionen (Zahlungen, Routing) mit detailliertem Verlauf. Interface analysiert auch das Routing, um zu sehen, welche Zahlungen durch Ihren Knotenpunkt laufen.





- **Wallet On-Chain-Verwaltung und -Sicherung** - Auf der Registerkarte On-Chain können Sie generate-Adressen verwalten und Transaktionen senden. RTL macht es einfach, Kanäle zu speichern, indem es die SCB-Datei für LND exportiert, mit automatischer Aktualisierung für jede Kanaländerung.



Kurz gesagt, RTL ist ein **leistungsfähiges Dashboard für den Lightning Network** und bietet einen pädagogischen Interface für die Steuerung Ihres Knotens auf einer täglichen Basis. Dieses Tutorial führt Sie durch die Installation und Verwendung, um Ihre Kanäle und Zahlungen zu verwalten.



## 2. Technischer Betrieb von RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Bevor wir zur Sache kommen, ist es nützlich, kurz zu verstehen, **wie RTL mit Ihrem Lightning-Knoten** auf technischer Ebene interagiert.



**Allgemeine Architektur:** RTL ist eine Webanwendung, die mit Node.js (Backend) und Angular (Frontend) erstellt wurde. Konkret läuft RTL als kleiner lokaler Webserver (standardmäßig auf Port 3000), der über seine APIs mit Ihrer Lightning-Implementierung in Dialog tritt. Abhängig von der Art der :





- Mit **LND** verwendet RTL die REST-API von LND (Port 8080), um Lightning-Befehle auszuführen. Die Verbindung ist durch TLS gesichert und erfordert die **admin macaroon**-Datei von LND zur Authentifizierung.





- Mit **Core Lightning (CLN)** verwendet RTL entweder die REST-API, die von *c-lightning-REST* bereitgestellt wird, oder eine **Zugriffsrune** über das Plugin `commando`. Lösungen wie Umbrel konfigurieren diese Elements automatisch.





- Mit **Eclair** verbindet sich RTL mit der Eclair REST API unter Verwendung des konfigurierten Authentifizierungspassworts.



**Konfiguration und Sicherheit:** RTL wird über eine JSON-Datei (`RTL-Config.json`) konfiguriert, in der Sie den Web-Port, das Zugangspasswort und die Verbindungsinformationen zu Ihrem Knoten festlegen. Das Interface-Web ist durch ein Login/Passwort geschützt (Standard-Passwort kann geändert werden) und unterstützt 2FA. Standardmäßig läuft RTL als lokales HTTP (`http://localhost:3000`), aber für den Fernzugriff sollten Sie immer eine sichere Verbindung verwenden (HTTPS über Reverse-Proxy, Tor oder VPN).



Kurz gesagt, RTL ist eine zusätzliche Komponente, die sich über sichere APIs mit Ihrem Knoten verbindet, entsprechende Zugriffstoken benötigt und ihre eigene Sicherheits-Layer bietet. Diese modulare Architektur ermöglicht es Ihnen sogar, **mehrere Lightning-Knoten mit einer einzigen RTL-Instanz** zu verwalten.



## 3. RTL-Installation



Da RTL als Open-Source-Software vertrieben wird, gibt es mehrere Möglichkeiten, es auf Ihrem System zu installieren. In diesem Abschnitt werden wir zwei Hauptansätze behandeln: die manuelle Installation und die Installation über Umbrel.



### Manuelle Methode



Die manuelle Installation ist geeignet, wenn Sie eine feinkörnige Kontrolle behalten möchten oder wenn Sie RTL in eine benutzerdefinierte Konfiguration integrieren. Die folgenden Schritte gelten für einen LND-Knoten mit Linux (z. B. Raspberry Pi oder VPS mit Ubuntu/Debian), sind aber für CLN/Eclair ähnlich.



**Voraussetzung:** Stellen Sie sicher, dass Sie einen **synchronisierten** Bitcoin-Knoten und einen funktionierenden Lightning-Knoten (LND, CLN oder Eclair) auf dem Rechner haben. RTL enthält keinen Lightning-Knoten an sich, sondern stellt eine Verbindung zu einem bestehenden Knoten her. Sie müssen außerdem **Node.js** installiert haben (Version 14+ empfohlen). Sie können dies mit `node -v` überprüfen oder Node von der offiziellen Seite (https://nodejs.org/en/download/) oder Ihrem Paketmanager installieren.



Die wichtigsten Installationsphasen sind:



**RTL-Code herunterladen**: Klonen Sie das offizielle RTL-GitHub-Repository in ein Verzeichnis Ihrer Wahl. Zum Beispiel:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Installieren Sie die Abhängigkeiten**: RTL ist eine Node.js-Anwendung, daher müssen Sie die erforderlichen Module installieren. Führen Sie im RTL-Ordner den Befehl :



```bash
npm install --omit=dev --legacy-peer-deps
```



Dieser Befehl installiert die erforderlichen NPM-Pakete (ohne Berücksichtigung der Entwicklungsabhängigkeiten). Die Option `--legacy-peer-deps` wird empfohlen, um mögliche Konflikte mit Node-Abhängigkeiten zu vermeiden.



**RTL-Config**: Sobald die Abhängigkeiten vorhanden sind, bereiten Sie die Konfigurationsdatei vor. Kopieren Sie die Datei `Sample-RTL-Config.json` im Stammverzeichnis des Projekts und benennen Sie sie in `RTL-Config.json` um. Öffnen Sie die Datei in Ihrem :





- **UI-Passwort**: Wählen Sie ein sicheres Passwort und geben Sie es in `multiPass` ein (anstelle des Standard-Passworts `"password"`).
- **Port**: Standardmäßig `3000`. Sie können ihn ändern, wenn dieser Port auf Ihrem Rechner bereits belegt ist.
- **Node**: Im Abschnitt `nodes[0]` stellen Sie die Parameter für Ihren Knoten ein:
     - lnNode": ein beschreibender Name für Ihren Knoten (z. B. "LND Node Maison").
     - lnImplementation`: `"LND"` (oder `"CLN"`/`"ECL"` je nach Fall).
     - Unter `Authentifizierung`:
       - macaroonPath`: Geben Sie den vollständigen Pfad zu dem Ordner an, der LND's macaroon admin enthält.
       - configPath": Pfad zur Konfigurationsdatei des Knotens (LND.conf" für LND).
     - Unter `Einstellungen`:
       - fiatConversion": Setzen Sie diesen Wert auf "true", wenn Sie eine Umrechnung in eine Fiat-Währung wünschen.
       - `unannouncedChannels`: auf `true` gesetzt, um unangekündigte Kanäle zu sehen.
       - themeColor" und "themeMode": Interface-Anpassung.
       - channelBackupPath`: Pfad für LND-Kanalsicherungen.
       - lnServerUrl": URL Ihres Lightning-Knotens (z. B. `https://127.0.0.1:8080`).



**Starten Sie den RTL-Server**: Führen Sie im RTL-Ordner den Befehl :



```bash
node rtl
```



Die Anwendung wird gestartet und kann unter `http://localhost:3000` aufgerufen werden.



**(Optional) Führen Sie RTL als Dienst aus**: Zum automatischen Starten erstellen Sie eine systemd :



Um dies zu tun:




- Öffnen Sie ein Terminal auf Ihrem Rechner.
- Erstellen Sie eine neue Servicedatei mit dem folgenden Befehl (ersetzen Sie `nano` durch Ihren bevorzugten Editor):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Kopieren Sie den nachstehenden Inhalt und fügen Sie ihn in diese Datei ein:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Ersetzen Sie `/path/to/RTL/rtl` durch den tatsächlichen Pfad zur `rtl`-Datei auf Ihrem Rechner und `<Ihr_Benutzer>` durch Ihren Linux-Benutzernamen.
- Speichern und schließen Sie die Datei.
- Laden Sie die systemd-Konfiguration neu:


```bash
sudo systemctl daemon-reload
```




- Aktivieren und starten Sie den RTL-Dienst:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL wird nun bei jedem Neustart des Rechners automatisch gestartet. Sie können seinen Status mit überprüfen:


```bash
sudo systemctl status RTL
```



### Installation über Umbrella



Wenn Sie [Umbrel](https://getumbrel.com) verwenden, ist die RTL-Installation viel einfacher:





- Zugang zu Interface Umbrel (normalerweise über `http://umbrel.local`)
- Besuchen Sie den **App Store**
- Suche nach "Ride The Lightning"



**Wichtiger Hinweis: Es gibt zwei separate RTL-Anwendungen im Umbrel App Store:**




- **Ride The Lightning** (für LND): zur Verwendung mit dem Standard-Blitzknoten von Umbrel (LND).
- **Ride The Lightning (Core Lightning)**: nur verwenden, wenn Sie die Anwendung *Core Lightning* auf Umbrel installiert haben und diesen Knoten mit RTL verwalten möchten.



*Jede RTL-Version ist für den Dialog mit der entsprechenden Implementierung (LND oder Core Lightning) vorkonfiguriert. Wenn Sie Ihren Lightning-Knoten nicht geändert haben, wählen Sie einfach die klassische LND-Version*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Klicken Sie auf **Installieren**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Wichtig:** Nach der Installation zeigt RTL einen Bildschirm mit dem Standardpasswort an. **Kopieren und speichern Sie dieses Passwort** - Sie benötigen es, um sich bei Interface RTL anzumelden. Dieses Passwort wird bei jedem Start von RTL angezeigt, bis Sie die Option "Nicht mehr anzeigen" aktivieren.



Umbrel kümmert sich automatisch um :




- RTL herunterladen und konfigurieren
- Konfigurieren des Zugriffs auf den Lightning-Knoten
- Verwalten von Aktualisierungen
- Sicherung des Zugangs zu Interface



Nach der Installation erscheint die Anwendung in deinem *Apps* Menü auf Umbrel. Klicken Sie auf **Ride The Lightning**, um sie zu starten.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Auf dem Anmeldebildschirm geben Sie das Passwort ein, das Sie zuvor kopiert haben. Sobald Sie eingeloggt sind, ist der Interface Web-RTL direkt über das Umbrel-Dashboard zugänglich, ohne dass eine zusätzliche Konfiguration erforderlich ist!



## 4. Einführung und Verwendung von Interface RTL



Jetzt, wo RTL in Betrieb ist, wollen wir das Interface-Web und seine wichtigsten Funktionen erkunden. Wir werden die verschiedenen Abschnitte der Anwendung durchgehen, um Ihnen einen vollständigen Überblick zu geben.



### Das Hauptbedienfeld



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Sobald Sie sich anmelden, gelangen Sie zum **Haupt-Dashboard**, das Ihnen einen Überblick über Ihren Lightning-Knoten gibt. Auf dieser Seite sind die wichtigsten Informationen zusammengefasst:




- Ihr gesamtes Lightning-Guthaben
- On-Chain-Saldo verfügbar
- Die Aufschlüsselung Ihrer Liquidität (eingehend/ausgehend)
- Schneller Zugang zum Senden und Empfangen von Satss über Ihren Lightning-Knoten



### Fondsverwaltung On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Mit der Registerkarte **On-Chain** können Sie Ihre Bitcoins direkt auf der Hauptkette verwalten:




- Saldoanzeige in verschiedenen Einheiten (Sats, BTC, USD)
- Vollständige Liste der Transaktionen
- Address Generation Taproot (P2TR), P2SH (NP2WKH) oder Bech32 (P2WKH)
- UTXO Verwaltung, Empfang und Versand von Bitcoins



### Lightning: detaillierte Darstellung der Untermenüs



Interface RTL verfügt über ein Seitenmenü, das Lightning Network gewidmet ist und alle wesentlichen Funktionen für die Verwaltung Ihres Knotens zusammenfasst. Hier sind die Details der einzelnen Untermenüs, in der Reihenfolge des Screenshots:



#### 1. Peers/Kanäle



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



In diesem Untermenü können Sie :




- Zeigen Sie die Liste Ihrer verbundenen Peers und der offenen oder wartenden Lightning-Kanäle an.
- Hinzufügen eines neuen Peers (Verbindung zu einem anderen Lightning-Knoten).
- Öffnen, schließen oder verwalten Sie bestehende Kanäle.
- Anzeige von Details zu jedem Kanal: Kapazität, lokale/ferne Salden, Status, Handelsverlauf, Saldenbewertung usw.



#### 2. Transaktionen



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



In diesem Untermenü können Sie :




- Blitzzahlungen senden (über Invoice).
- generate und Verwaltung von Rechnungen, um Zahlungen zu erhalten.
- Sie können die gesamte Historie der gesendeten und empfangenen Zahlungen mit Details (Betrag, Datum, Status, Gebühren, Anzahl der Auslassungen usw.) einsehen.



#### 3. Weiterleitung



Dieses Untermenü zeigt an:




- Zahlungen, die von Ihrem Knotenpunkt für andere Lightning Network-Benutzer weitergeleitet werden.
- Routing-Statistiken: Anzahl der weitergeleiteten Transaktionen, verdiente Gebühren, aufgetretene Fehler.
- Exportierbarer Verlauf für erweiterte Analysen.



#### 4. Abgrenzungen



Dieses Untermenü bietet :




- Detaillierte Berichte über die Aktivitäten Ihres Lightning-Knotens.
- Diagramme und Tabellen zu Kanälen, Zahlungen, Gebühren, Kapazitäten usw.
- Tools zum besseren Verständnis der Leistung Ihres Knotens.



#### 5. Graph Lookup



In diesem Untermenü können Sie :




- Erkunden Sie die Topologie des Lightning Network.
- Suche nach bestimmten Knotenpunkten oder Kanälen.
- Holen Sie Informationen über die Konnektivität und die Gesamtkapazität des Netzes ein.



#### 6. Unterschreiben/Bestätigen



Dieses Untermenü bietet :




- Die Möglichkeit, eine Nachricht mit dem Schlüssel des eigenen Knotens zu signieren (Nachweis von Ownership).
- Signaturprüfung zur Authentifizierung von Nachrichten von anderen Knotenpunkten.



#### 7. Sicherung



Dieses Untermenü ist der Sicherung gewidmet:




- Exportieren Sie die Kanalsicherungsdatei (SCB für LND).
- Stellen Sie bei Bedarf die Konfiguration oder die Kanäle wieder her.
- Tipps zur Sicherung Ihrer Backups.



#### 8. Knoten/Netzwerk



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



In diesem Untermenü finden Sie :




- Eine vollständige Übersicht über den Status Ihres Lightning-Knotens: Alias, Version, Farbe, Synchronisationsstatus.
- Statistiken über Kanäle (aktiv, wartend, geschlossen), Gesamtkapazität, Konnektivität.
- Informationen über den globalen Lightning Network und die Position des eigenen Knotens darin.



### Dienstleistungen: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz ist ein datenschutzfreundlicher Exchange-Dienst, der Bitcoins zwischen Lightning Network und Blockchain Bitcoin (On-Chain) umwandelt. Er bietet zwei Arten von Operationen an: Reverse Submarine Swap (**Swap Out**) und Submarine Swap (**Swap In**).



#### Swap Out (Reverse Submarine Swap)



Swap Out wandelt die auf dem Lightning Network verfügbaren Satss in On-Chain Bitcoins um. Dieser Mechanismus ist nützlich, wenn einem Knoten die eingehende Kapazität ausgeht oder wenn Sie Gelder von einem On-Chain Address zurückholen wollen. Der Prozess funktioniert wie folgt:




- Der Benutzer wählt einen Betrag aus, der umgetauscht werden soll
- Der Knoten sendet eine Blitzzahlung an Boltz
- In Exchange blockiert Boltz einen entsprechenden Betrag in On-Chain-Bitcoins
- Sobald die Transaktion bestätigt wurde, kann der Nutzer das Geld einfordern, indem er ein beim Tausch verwendetes Geheimnis preisgibt



Bei diesem Verfahren handelt es sich nicht um ein Verwahrungsverfahren, bei dem Boltz die Gelder des Nutzers nie einbehält.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (U-Boot Swap)



Mit Swap In hingegen können On-Chain-Mittel in den Lightning Network reinjiziert werden. Dies ist besonders nützlich für die Wiederherstellung der Ausgangskapazität auf Ihren Kanälen. Das Verfahren ist wie folgt:




- Der Nutzer sendet Bitcoins an einen bestimmten, von Boltz generierten Address
- Diese Gelder können von Boltz nur freigegeben werden, wenn er einen vom Nutzerknoten generierten Lightning Invoice bezahlt
- Sobald der Invoice bezahlt ist, stehen die Mittel auf dem Blitzkanal zur Verfügung und erhöhen die Produktionskapazität des Knotens



![Configuration d'un swap-in](assets/fr/12.webp)



Diese beiden Mechanismen ermöglichen es, die Liquidität des Lightning-Kanals effizient zu verwalten und gleichzeitig die Hoheit des Nutzers über seine Gelder zu erhalten.



### Konfiguration und Anpassung



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Auf der Registerkarte **Knotenkonfiguration** können Sie Ihre Erfahrungen anpassen:




- Aktivierung von unangekündigten Kanälen
- Anpassen der Verkaufsanzeige
- Block explorer-Konfiguration
- Einstellen des Interface



### Dokumentation und Hilfe



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Schließlich bietet der Bereich **Hilfe** eine umfassende Dokumentation zu :




- Erstmalige Konfiguration
- Peer- und Kanalmanagement
- Zahlungen und Transaktionen
- Backups und Wiederherstellungen
- Berichte und Statistiken
- Unterschriften und Überprüfungen
- Knoten- und Anwendungsparameter



Mit diesem umfassenden Interface können Sie Ihren Lightning-Knoten effizient verwalten, von grundlegenden Vorgängen bis hin zu erweiterten Funktionen, alles in einem intuitiven, gut organisierten Interface.



## 5. Erweiterte Anwendungsfälle & Sicherheit



In diesem Abschnitt erfahren Sie, was Sie wissen müssen, um mit RTL weiterzukommen und Ihren Lightning-Knoten zu sichern:



### Überwachung und Fehlerbehebung



Um Ihren Knoten zu überwachen, können Sie RTL-Daten (Protokolle, CSV) exportieren und sie in Tools wie Grafana anzeigen. Im Falle eines Problems (blockierte Zahlung, inaktiver Kanal) konsultieren Sie die LND/CLN-Protokolle und verwenden Sie die Diagnosebefehle (`lncli listchannels`, `lncli pendingchannels`, usw.). RTL bietet auch Interface-Protokolle zur Überwachung von Routing-Ereignissen an.



### Sicherer Fernzugriff



Setzen Sie RTL niemals direkt im Internet aus. Geben Sie den Vorzug vor :




- **VPN** (z. B. Tailscale) für privaten, verschlüsselten Zugang
- **Tor** für sicheren, anonymen Zugang
- **Reverse Proxy HTTPS** (Nginx/Caddy) nur, wenn Sie wissen, wie man es konfiguriert



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Gute Sicherheitspraktiken





- **Schützen Sie Ihren Zugang**: Geben Sie niemals admin.macaroon oder Ihr RTL-Passwort weiter. Schränken Sie die Berechtigungen für sensible Dateien ein.
- **Regelmäßige Backups**: Exportieren Sie die Channel-Backup-Datei (SCB) nach jeder Änderung und speichern Sie sie außerhalb des Knotens.
- **Updates**: Halten Sie RTL, Ihren Node und Umbrel mit den neuesten Sicherheitskorrekturen auf dem neuesten Stand.
- **Vertraulichkeit**: Anonymisieren Sie Protokolle und Bildschirmfotos, bevor Sie sie weitergeben. Geben Sie Ihre Bilanzen oder Peer-Listen niemals öffentlich bekannt.
- **Einzelzugang**: RTL ist nicht mehrbenutzerfähig. Geben Sie den Admin-Zugang nicht frei. Verwenden Sie für den Nur-Lese-Zugriff ggf. einen speziellen Makaroon.



Durch die Anwendung dieser Grundsätze können Sie die Risiken stark einschränken und die Kontrolle über Ihren Lightning-Knoten behalten.



## 7. Schlussfolgerung



**Ride The Lightning** ist ein unverzichtbares Werkzeug für die effektive Verwaltung eines Bitcoin/Lightning-Knotens, egal ob Sie Anfänger oder fortgeschrittener Benutzer sind. Es bietet ein klares Interface für die Kontrolle Ihrer Kanäle, Zahlungen und den Zustand des Knotens und vertieft gleichzeitig Ihr Verständnis von Lightning Network.



RTL zeichnet sich durch seine Kompatibilität mit mehreren Implementierungen, seine fortgeschrittenen Funktionen (Rebalancing, Swaps, Berichte) und seinen pädagogischen Ansatz aus. Für einfache Bedürfnisse reichen der Interface Umbrel oder ein Wallet Mobile aus, aber RTL ist für ein aktives, optimiertes Knotenmanagement absolut sinnvoll.



Weitere Informationen finden Sie hier:




- Offizielle RTL-Website: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Technische Diskussionen, Projektankündigungen, Feedback und Bildungsressourcen
- **Umbrel Community Forum**: [community.getumbrel.com](https://community.getumbrel.com) - Offizielles Forum mit eigener Bitcoin/Lightning-Sektion, Anleitungen und Lösungen für allgemeine Probleme
- **Lightning Network-Entwickler**: [github.com/lightning](https://github.com/lightning) - Offizielles GitHub-Repository, um die Entwicklung zu verfolgen und Quellcode beizusteuern
- **Stack Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Technische Q&A mit Entwicklern und fortgeschrittenen Benutzern



Kurz gesagt, RTL gibt Ihnen die volle Kontrolle über Ihren Lightning-Knoten in einem modernen, voll ausgestatteten Interface.



**Quellen :** Offizielle RTL-Website; RTL GitHub; Umbrel App Store; Umbrel Community; Plan B Network Ressourcen.



Um Ihr Verständnis für die Funktionsweise des Lightning Network zu vertiefen, empfehle ich Ihnen auch diesen kostenlosen Kurs zu besuchen:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb