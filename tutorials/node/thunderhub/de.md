---
name: ThunderHub
description: Interface Blitzknotenverwaltung Web LND
---
![cover](assets/cover.webp)



## Einführung



ThunderHub ist ein **Open-Source-Manager für Lightning-Knoten (LND)** und bietet einen intuitiven Interface, der von jedem Gerät oder Browser aus zugänglich ist.



**Hauptmerkmale:**




- **Überwachung**: Globale Übersicht über Salden, Kanäle, Transaktionen, Routing-Statistiken
- **Verwaltung**: Öffnen/Schließen von Kanälen, eingehende/ausgehende Zahlungen, Kanalausgleich
- **Integrationen**: LNURL-Unterstützung, Swaps über Boltz, Amboss-Backup
- **Interface responsive**: Kompatibel mit Mobil-, Tablet- und Desktop-Geräten mit dunklen/hellen Themen



ThunderHub lässt sich problemlos mit **Umbrel**, **Voltage**, **RaspiBlitz** und **MyNode** integrieren und vereinfacht so die tägliche Verwaltung Ihres Knotens.



**ThunderHub eignet sich besonders für Betreiber, die ein ergonomisches Interface für die Verwaltung ihrer Kanäle, die Steuerung der Liquidität (Rebalancing), die Überwachung von Transaktionen und die Integration von Drittanbieterdiensten wie Amboss suchen. Die Sicherheit wird über eine lokale oder Tor-Verbindung gewährleistet.**



Wenn Sie noch keinen Blitzknoten haben, empfehlen wir Ihnen, unser LND Umbrella-Tutorial zu befolgen:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Einrichtung



ThunderHub kann auf verschiedene Arten installiert werden, abhängig von Ihrer Lightning-Node-Hosting-Umgebung. Ob Sie eine schlüsselfertige Lösung (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, etc.) oder eine manuelle Installation verwenden, ThunderHub ist oft ohne großen Aufwand verfügbar. Im Folgenden beschreiben wir zwei gängige Ansätze: über den Umbrel App Store und über eine manuelle Installation (für einen Server oder eine selbst gehostete Distribution).



### Installation über Umbrella



Umbrel integriert ThunderHub in seinen **App Store**, was die Installation extrem einfach macht. Sie brauchen keine Kommandozeile oder manuelle Konfiguration: alles wird über Interface Umbrel erledigt. Folgen Sie einfach diesen Schritten:





- **Öffne das Umbrel Dashboard**: Verbinde dich mit dem Interface Web deines Umbrel-Knotens (z.B. `http://umbrel.local` in deinem lokalen Netzwerk, oder über sein `.onion` Address, wenn du Tor benutzt).
- **Zugriff auf den App Store**: Klicken Sie im Hauptmenü von Umbrel auf "App Store" (oder "App"). Suchen Sie in der Liste der verfügbaren Anwendungen nach **ThunderHub**.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Installieren Sie ThunderHub**: Klicken Sie auf die ThunderHub-Anwendung und dann auf die Schaltfläche "Installieren". Bestätigen Sie, wenn nötig. Umbrel wird ThunderHub automatisch herunterladen und auf Ihrem Knoten installieren.





- **Starten Sie die Anwendung**: Sobald die Installation abgeschlossen ist (einige zehn Sekunden), erscheint ThunderHub auf Ihrer Startseite. Klicken Sie auf das Symbol, um es zu öffnen. ThunderHub wird in Ihrem Browser gestartet.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Wichtig:** Wenn ThunderHub zum ersten Mal geöffnet wird, zeigt es automatisch das **Standardpasswort** an, das für die Anmeldung erforderlich ist. Mit der Option "Nicht mehr anzeigen" können Sie diese Anzeige für zukünftige Verbindungen ausblenden. **Wir raten Ihnen dringend zu:**




- Speichern Sie dieses Passwort sofort **in Ihrem Passwort-Manager**
- Kopieren Sie es zur Verwendung im nächsten Schritt
- Aktivieren Sie die Option "Nicht mehr anzeigen", sobald das Kennwort gespeichert wurde



![Page de connexion de ThunderHub](assets/fr/03.webp)



Sie werden dann zur Anmeldeseite weitergeleitet, auf der Sie das Passwort eingeben müssen, das Sie im vorherigen Schritt kopiert haben, um das Interface zu entsperren.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel kümmert sich im Hintergrund darum, ThunderHub mit LND-Verbindungsinformationen (TLS-Zertifikat, Administrationsmakro, etc.) zu versorgen, so dass Sie keine zusätzliche Konfiguration vornehmen müssen. Mit nur wenigen Klicks können Sie ThunderHub auf Ihrem Umbrel-Knoten einrichten und betreiben.



### Manuelle Installation (selbstgehostet, ohne Umbrel)



Für Benutzer außerhalb von Umbrel (z.B. auf einem persönlichen Server, einem Raspberry Pi mit RaspiBlitz oder einer *Einzelplatzinstallation*) erfordert die Installation von ThunderHub ein paar zusätzliche Schritte. Im Folgenden beschreiben wir die Installation aus dem Quellcode und die Konfiguration gemäß der [offiziellen ThunderHub-Dokumentation] (https://docs.thunderhub.io).



#### Einrichtung



**Voraussetzungen:** Vergewissern Sie sich, dass Ihr System die Mindestanforderungen gemäß der [Dokumentation Setup] (https://docs.thunderhub.io/setup) erfüllt:




- **Node.js** Version 18 oder höher
- **npm** installiert
- Zugang zu LND-Authentifizierungsdateien :
  - LND TLS-Zertifikat (`tls.cert`)
  - LND-Verwaltungsmakkaron (`admin.macaroon`)
  - LND gRPC-Dienst Address (Hostname:Port) (Standardwert "127.0.0.1:10009" lokal)



**1. Rufen Sie den ThunderHub-Code ab:** Klonen Sie das GitHub-Repository des Projekts wie in der [Installationsdokumentation] (https://docs.thunderhub.io/installation) beschrieben:



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. Installieren Sie die Abhängigkeiten und erstellen Sie die Anwendung:**



```bash
npm install
npm run build
```



Diese Befehle installieren alle erforderlichen Module und kompilieren dann die Anwendung (ThunderHub ist in TypeScript/React geschrieben).



**3. Späteres Update:** ThunderHub bietet mehrere Methoden für zukünftige Updates:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Konfiguration (Einrichtung)



**1. Hauptkonfigurationsdatei:** Erstellen Sie eine `.env.local`-Datei im Stammverzeichnis des ThunderHub-Ordners, um die Konfiguration anzupassen (dies verhindert, dass Ihre Einstellungen bei Aktualisierungen überschrieben werden). Hauptvariablen gemäß der [Setup-Dokumentation] (https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Konfiguration der Serverkonten:** Erstellen Sie die in `ACCOUNT_CONFIG_PATH` angegebene YAML-Datei:



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Fernzugriff:** Um eine Verbindung zu einem entfernten LND-Knoten herzustellen, fügen Sie die Datei `LND.conf` hinzu:



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Sicherheit:** Beim ersten Start versteckt ThunderHub **automatisch** das `masterPassword` und alle Account-Passwörter in der YAML-Datei, um zu vermeiden, dass Passwörter im Klartext auf dem Server liegen.



**5. ThunderHub starten:**



```bash
npm start
```



Standardmäßig lauscht der Server auf Port 3000. Greifen Sie auf `http://localhost:3000` (oder `http://ip-serveur:3000` aus dem lokalen Netz) zu.



**6. Docker-Alternative:** ThunderHub bietet offizielle Docker-Images:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Die Anmeldeseite von ThunderHub wird angezeigt. Wählen Sie das konfigurierte Konto und geben Sie das Passwort ein, um auf das Dashboard zuzugreifen.



**Installation auf anderen Distributionen:** Vorgefertigte Node-Distributionen (RaspiBlitz, MyNode, Start9, etc.) bieten im Allgemeinen native ThunderHub-Unterstützung über ihre jeweiligen Administrationsschnittstellen.



**Für weitere Informationen:** Konsultieren Sie die vollständige offizielle Dokumentation:




- **Installation:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Konfiguration:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



In diesen Ressourcen werden erweiterte Optionen wie SSO-Konten, verschlüsselte Makronen, TOR-Konfiguration und vieles mehr beschrieben.



Sobald ThunderHub installiert und zugänglich ist, können Sie alle seine Funktionen nutzen. Im folgenden Abschnitt werfen wir einen Blick auf den Interface ThunderHub und seine verschiedenen Registerkarten, um Sie durch seine Verwendung zu führen.



## Interface-Präsentation



Interface ThunderHub ist um ein Hauptmenü herum aufgebaut (das normalerweise in der linken Seitenspalte angezeigt wird), das mehrere Hauptabschnitte umfasst. Jeder Bereich entspricht einem Aspekt der Verwaltung Ihres Lightning-Knotens. Gehen wir sie der Reihe nach durch:





- **Home** - Home-Registerkarte mit allgemeinem Dashboard (Überblick über Ihren Knoten und Schnellaktionen).
- **Dashboard** - Anpassbares Dashboard mit Widgets und erweiterten Metriken.
- **Peers** - Lightning Peer Management (Verbindungen zu anderen Knoten).
- **Channels** - Detaillierte Verwaltung von Lightning-Kanälen.
- **Rebalance** - Instrument zum Kanalausgleich (Rundzahlungen).
- **Transaktionen** - Blitzzahlungshistorie (LN Transaktionen).
- **Weiterleitungen** - Routing-Statistiken (von Ihrem Knoten weitergeleitete Zahlungen).
- **Kette** - Node's On-Chain Portfolio (On-Chain BTC: UTXOs, Transaktionen).
- **Amboss** - Integration mit Amboss (Knotenüberwachung, Backups, usw.).
- **Tools** - Verschiedene Tools (Backups, signierte Nachrichten, Makronen, Berichte usw.).
- **Tausch** - On-Chain/Lightning-Tauschfunktionen über Boltz.
- **Stats** - Erweiterte Statistiken und Leistungsmetriken für Knoten.



*(Hinweis: Je nach ThunderHub-Version können einige Abschnitte leicht abweichende Überschriften oder zusätzliche Funktionen haben, aber die allgemeinen Grundsätze bleiben gleich)*



### Home (Allgemeines Bedienfeld)



Die Registerkarte **Home** von ThunderHub ist die Startseite, die nach der Anmeldung angezeigt wird. Sie enthält das **Allgemeine Dashboard**, das einen **globalen Überblick** über den Status Ihres Lightning-Knotens bietet und **schnelle Aktionen** für Routinevorgänge vorschlägt. Hier finden Sie die üblichen Informationen:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Guthaben und Kapazitäten:** Oben auf der Seite zeigt ThunderHub Ihre verfügbaren Guthaben an. Hier sehen Sie normalerweise den On-Chain-Saldo (Bitcoin On-Chain im Wallet des Knotens, symbolisiert durch ein Anchor ⚓) und den Blitz-Saldo (die Kapazitäten Ihrer Kanäle, symbolisiert durch einen Blitz Bolt ⚡). So sehen Sie sofort, wie viel Geld Sie in On-Chain und Lightning haben. Wenn Sie mehrere Konten oder Kanäle haben, vergewissern Sie sich, dass Sie auf dem richtigen Kanal sind (z. B. Mainnet gegenüber Testnet).





- **Schlüsselstatistiken:** Das Dashboard kann einige globale Metriken für Ihren Knoten anzeigen, z. B. die Anzahl der offenen Kanäle, die Anzahl der angeschlossenen Peers, verdiente Routing-Gebühren (falls zutreffend) usw. Es ist eine Zusammenfassung der jüngsten Aktivitäten und des Zustands des Knotens.





- **Quick Actions:** Das Dashboard enthält Schaltflächen, mit denen die häufigsten Aufgaben schnell ausgeführt werden können, ohne durch Menüs navigieren zu müssen. Zu diesen Schnellaktionen gehören:





- **Geist**: Richten Sie einen benutzerdefinierten Lightning Address über Amboss ein.
- **Spende**: Machen Sie eine Spende über Lightning.
- **Anmelden/Zu**: Verbinden Sie sich mit Ihrem Amboss-Konto (Quick Connect) und gehen Sie direkt zu Amboss.space, um die Informationen Ihres Knotens einzusehen.
- **Address**: Geben Sie einen Lightning Address ein, um eine Zahlung zu leisten.
- **Öffnen**: Öffnet einen neuen Lightning-Kanal. Wenn Sie darauf klicken, öffnet sich ein Formular zur Eingabe der URI des entfernten Knotens, für den der Kanal geöffnet werden soll, des Betrags und ggf. der maximalen On-Chain-Gebühr, die verwendet werden soll.
- **Dekodieren**: Dekodieren Sie eine Lightning Invoice oder LNURL, um Details vor der Zahlung anzuzeigen.
- **LNURL**: Verarbeiten Sie LNURLs für Lightning-Zahlungen oder -Abhebungen.
- **LnMarkets Anmeldung**: Anmeldung bei LnMarkets für den Handel.



Mit diesen Schnellaktionen können Sie die häufigsten Vorgänge direkt von der Startseite aus durchführen, ohne durch die verschiedenen Registerkarten der Interface navigieren zu müssen.



Kurz gesagt, das ThunderHub-Dashboard gibt Ihnen einen **schnellen Überblick** über Ihren Knoten und lässt Sie die häufigsten Operationen (Senden/Empfangen, Öffnen eines Kanals) mit einem einzigen Klick ausführen. Es ist der ideale Ausgangspunkt für die alltägliche Verwaltung.



### Dashboard



Der Bereich **Dashboard** ist von der Registerkarte Home getrennt und bietet ein erweitertes, anpassbares Dashboard. In diesem Bereich können Sie eine benutzerdefinierte Ansicht mit spezifischen Widgets erstellen, die Ihren Bedürfnissen als Knotenbetreiber entsprechen.





- **Anpassbare Widgets:** Im Gegensatz zur Startseite, die ein festes Layout hat, können Sie im Dashboard genau auswählen, welche Elements angezeigt werden sollen und wie sie organisiert werden.



![Dashboard sans widgets activés](assets/fr/06.webp)



Wenn keine Widgets aktiviert sind, erscheint die Meldung "No Widgets Enabled!" (Keine Widgets aktiviert) mit einer Schaltfläche "Settings" (Einstellungen) für den Zugriff auf die Anpassungsparameter.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



In den Einstellungen können Sie aus einer breiten Palette von Widgets wählen, die in Kategorien unterteilt sind: "Lightning - Info", "Lightning - Tabelle", "Lightning - Grafik", usw. Jedes Widget kann einzeln mit den Schaltflächen "Anzeigen/Ausblenden" aktiviert oder deaktiviert werden.



![Bas de la page des paramètres](assets/fr/08.webp)



Am Ende der Einstellungen finden Sie die Schaltfläche "Zum Dashboard", um zum Dashboard zurückzukehren, und die Schaltfläche "Widgets zurücksetzen", um die Standardanzeige zurückzusetzen.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Einmal konfiguriert, kann Ihr Dashboard verschiedene Diagramme und Metriken anzeigen: Blitzzahlungsdiagramme, Anzahl der ausgestellten Rechnungen, Weiterleitungsstatistiken, detaillierte Salden usw.





- **Erweiterte Metriken:** Greifen Sie auf detailliertere Statistiken über die Leistung Ihres Knotens zu, mit Diagrammen und Echtzeitdaten.





- **Konfigurierbare Übersicht:** Passen Sie die Anzeige an, egal ob Sie ein Gelegenheitsnutzer oder ein professioneller Anwender sind, der mehrere Routing-Kanäle verwaltet.





- **Modulare Interface:** Fügen Sie je nach Bedarf Widgets hinzu oder entfernen Sie sie: Vorwärtsdiagramme, Liquiditätsmetriken, Warnungen zum Knotenzustand usw.



Dieser Bereich ist besonders nützlich für fortgeschrittene Benutzer, die bestimmte Metriken überwachen oder sich einen technischen Überblick über ihren Lightning-Knoten verschaffen möchten. Er ergänzt den Bereich "Home", indem er mehr Flexibilität und Kontrolle darüber bietet, wie die Informationen angezeigt werden.



### Gleichaltrige



Der Abschnitt **Peers** listet alle Lightning-Knoten auf, die derzeit mit Ihrem Knoten als Peers verbunden sind. Ein **Peer** ist eine direkte Knoten-zu-Knoten-Verbindung auf dem Lightning Network. Ihr Knoten kann auch ohne einen offenen Kanal mit Peers verbunden sein (z. B. nur mit Exchange-Klatschinformationen im Netzwerk), oder natürlich impliziert jeder offene Kanal automatisch einen verbundenen Peer.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Auf der Registerkarte "Peers" sehen Sie :





- **Informationsspalten:** Das Interface zeigt nützliche Details wie den Synchronisationsstatus, den Verbindungstyp (Clearnet oder Tor), Ping, empfangene/gesendete Satoshis und das Volumen der ausgetauschten Daten an.
- Hinzufügen eines Peers: Mit ThunderHub können Sie über die Schaltfläche **"Hinzufügen"** in der oberen rechten Ecke manuell eine Verbindung zu einem neuen Peer herstellen. Sie müssen die URI des Knotens eingeben (Format `<public_key>@<socket>`). Nach der Validierung sendet ThunderHub den entsprechenden Befehl `lncli connect`. Wenn der Knoten online und erreichbar ist, wird er zu Ihrer Liste der Peers hinzugefügt.



### Kanäle



Die Registerkarte **Kanäle** ist das Herzstück der Lightning-Kanalverwaltung. Es ist wahrscheinlich der Bereich, den Sie am häufigsten konsultieren werden. Hier werden **alle Ihre Lightning-Kanäle** mit ihren Details angezeigt, und Sie können Verwaltungsaktionen für diese Kanäle durchführen.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Die folgenden Informationen finden Sie auf der Seite Kanäle:





- **Ansicht der Kanalliste:** Jeder offene (oder geöffnete/geschlossene) Kanal wird aufgelistet, in der Regel mit dem Alias des entfernten Knotens, der gesamten Kanalkapazität und einem farbigen Balken, der die Verteilung der lokalen gegenüber der entfernten Liquidität darstellt. ThunderHub verwendet einen Farbcode (oft blau/Green) oder einen Prozentsatz, um das Gleichgewicht des Kanals anzuzeigen: z. B. blau für Ihren lokalen Anteil, Green für den entfernten Anteil. Wenn ein Kanal perfekt ausgeglichen ist (50/50), zeigt der Balken die Hälfte jeder Farbe an. So können Sie auf einen Blick erkennen, welche Kanäle unausgewogen sind (alles blau = fast alles lokal, alles Green = fast alles fern).





- **Informationsspalten:** Das Interface zeigt detaillierte Spalten an, einschließlich Status, verfügbare Aktionen, Peer-Info, Kanal-ID, Kapazität, Aktivität, Gebühren und Saldo mit grafischer Liquiditätsanzeige.





- **Anzeigekonfiguration:** Über ein Zahnrad in der oberen rechten Ecke können Sie die Kanalanzeige Ihren Wünschen entsprechend anpassen.





- **Status:** Sie sehen auch Statusanzeigen - z. B. "Aktiv" (der Kanal ist offen und betriebsbereit), "Offline" (der Peer ist getrennt, so dass der Kanal vorübergehend unbrauchbar ist), "Ausstehend" (für Eröffnungen oder Schließungen, die von On-Chain bestätigt werden müssen).





- **Aktionen in einem Kanal:** Für jeden Kanal bietet ThunderHub Aktionsschaltflächen (oft in Form von Symbolen):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- **Gebühren bearbeiten:** Mit der Interface "Update Channel Policy" können Sie alle Kanalparameter anpassen: Grundgebühr, Gebührensatz (in ppm), CLTV Delta, Max HTLC und Min HTLC. Auf diese Weise können Sie Ihre Gebührenrichtlinien individuell pro Kanal anpassen, mit dem Ziel, Routing-Verkehr anzuziehen (oder abzuschrecken). *(Hinweis: ThunderHub ist kein Ersatz für ein automatisches Gebührenmanagement-Tool, aber für die manuelle Anpassung ist es sehr effektiv)*
- Schließkanal (*Close*): Der Interface "Close Channel" lässt Ihnen die Wahl zwischen einem **kooperativen Abschluss** (Standard) oder einem **erzwungenen Abschluss** (*Force Close*), indem Sie die Gebühren (in Sats/vByte) festlegen. **Wichtig:** Bevorzugen Sie, wenn möglich, immer den kooperativen Abschluss, um On-Chain-Abwicklungsverzögerungen und höhere Gebühren zu vermeiden. ThunderHub teilt Ihnen mit, ob die Gegenstelle online ist (kooperativ möglich) oder nicht. Im Falle eines erzwungenen Abschlusses müssen Sie diesen bestätigen, da er unumkehrbar ist und eine umfassende Transaktion mit einer Zeitsperre auslöst (im Allgemeinen 144 Blöcke oder ~1 Tag bei Bitcoin Mainnet).
- **Einen neuen Kanal öffnen:** Um einen neuen Kanal zu öffnen, klicken Sie auf das Zahnrad oben rechts auf der Seite "Kanäle" und wählen Sie dann "Öffnen". Sie können dann einen Kanal zu einem neuen oder bestehenden Peer einrichten. Der Vorteil dieser Seite ist, dass Sie eine Liste Ihrer bestehenden Channels vor sich haben, die Ihnen bei der Entscheidung helfen kann, wo Sie einen neuen Channel eröffnen wollen.



Kurz gesagt, der Bereich Kanäle gibt Ihnen **eine feine Kontrolle über jeden Kanal**. Hier steuern Sie die Liquiditätszuweisung, entscheiden, welche Kanäle beibehalten oder geschlossen werden sollen, und legen Ihre Routing-Parameter pro Kanal fest. ThunderHub bietet ein klares Interface für diese wichtigen Knotenverwaltungsvorgänge.



### Neugewichtung



Die Registerkarte **Ausgleich** ist dem **Kanalausgleich** gewidmet. Beim Ausgleich (oder *Neubalancieren*) wird die Verteilung der Mittel zwischen Ihren ausgehenden und eingehenden Kanälen neu angepasst, indem eine **Rundzahlung** von einem Ihrer Kanäle zu einem anderen Ihrer Kanäle über den Lightning Network vorgenommen wird. Auf diese Weise können Sie, ohne neue Gelder einzubringen, Liquidität von einem zu vollen auf einen zu leeren Kanal verlagern, wodurch Ihre Kanäle nützlicher werden (ein ausgeglichener Kanal kann sowohl Zahlungen senden als auch empfangen).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub vereinfacht diesen Vorgang, der sonst auf der Kommandozeile mühsam wäre, erheblich. Hier erfahren Sie, wie Sie den Abschnitt "Rebalance" verwenden:





- **Anfängliche Kanalansicht:** Beim Aufrufen von Rebalance zeigt ThunderHub eine Liste Ihrer Kanäle mit einem Balanceindikator für jeden Kanal an (ähnlich dem auf der Seite Kanäle). Sie können sofort sehen, welche Kanäle aus dem Gleichgewicht geraten sind. ThunderHub kann die Kanäle in der Reihenfolge der zunehmenden Ausgewogenheit sortieren, so dass die am stärksten unausgewogenen Kanäle ganz oben in der Liste stehen (0,0 bedeutet vollständig lokal oder ferngesteuert).





- **Peer-Auswahl:** Das Interface macht es einfach, ausgehende und eingehende Peers für den Ausgleich auszuwählen.





- **Parametereinstellungen:** Sie können einstellen:
  - Die **höchste Gebühr** (in Sats und ppm), die Sie zu zahlen bereit sind
  - Der **Betrag für die Neugewichtung** mit der Option "Fest" oder "Ziel"
- **Zu vermeidende Knoten** beim Routing
- **Maximale Versuchszeit** für die Routenfindung





- Wählen Sie den Kanal **Quelle**: Wählen Sie zunächst den **Ausgangskanal (Quelle)**, d. h. den Kanal, von dem Sie zu viel lokale Liquidität haben, um ihn zu verschieben. In der Praxis ist dies ein Kanal, bei dem Ihr lokaler Anteil hoch ist (> 50 %). Stellen wir uns einen A-Kanal mit 1.000.000 Satss vor, von denen 900.000 lokal sind - ein guter Kandidat, um Satss woanders hin zu schicken. Wenn Sie auf diesen A-Kanal als "ausgehend" klicken, markiert ThunderHub ihn als Quelle.





- Wählen Sie **Zielkanal**: Als Nächstes wählen Sie den **Zielkanal**, der Liquidität erhalten soll. In der Regel wird dies ein Kanal sein, bei dem es umgekehrt ist - die meisten Mittel befinden sich auf der anderen Seite (z. B. nur 100.000 lokale Satss von 1.000.000). ThunderHub sortiert nach der Auswahl des Quellkanals die anderen Kanäle in umgekehrter Reihenfolge (abnehmende Ausgewogenheit), um die komplementärsten Kanäle zu ermitteln. Wählen Sie einen B-Kanal, der auf der lokalen Seite Platz hat. ThunderHub zeigt dann deutlich an, welche beiden Kanäle ausgewählt wurden (Quelle A und Ziel B).





- **Gebührenhöhe und -toleranz festlegen:** Ein Formular ermöglicht Ihnen die Eingabe von :





  - Der **Betrag**, der wieder ausgeglichen werden soll (in Sats). Häufig wird ein Betrag gewählt, der dem entspricht, was beide Kanäle bei \~50/50 ausgleichen würde. ThunderHub kann z. B. die Hälfte der überschüssigen Kapazität des Quellkanals vorfüllen.
  - Die **höchste Gebühr**, die Sie für diesen Vorgang zu zahlen bereit sind (optional). Diese Gebühr wird in Sats ausgedrückt (Gesamtkosten für die Weiterleitung). Wenn Sie dieses Feld leer lassen, wird ThunderHub unabhängig von den Kosten nach einem Weg suchen, was im Allgemeinen nicht ratsam ist (es ist besser, eine Grenze festzulegen, z. B. 10 Sats für einen kleinen Ausgleich oder einen Höchstwert für ppm).





- **Route finden:** Klicken Sie auf die Schaltfläche, um eine Route zu finden. ThunderHub fragt den LND ab, um eine Route von Ihrem Quellkanal durch das Netzwerk zu Ihrem eigenen Zielkanal zu berechnen. Wenn er eine mögliche Route findet, die Ihren Gebührenkriterien entspricht, zeigt er sie mit Details zu den Sprüngen und den Gebührenkosten an. Zum Beispiel könnte es anzeigen, dass es einen 3-Hop-Pfad mit insgesamt 2 Sats an Gebühren gefunden hat.





- **Rebalance starten:** Wenn Sie mit der vorgeschlagenen Route zufrieden sind, klicken Sie auf **Balance Channel**. ThunderHub initiiert dann eine Umlaufzahlung über LND. Wenn die Zahlung erfolgreich ist, erhalten Sie eine Erfolgsmeldung, und die Salden der Kanäle A und B werden in Echtzeit geändert. ThunderHub aktualisiert die Saldenanzeige für diese Kanäle (im Idealfall sind sie grüner als zuvor, was auf einen besseren Saldo hinweist).





- **Anpassungen und Iterationen:** Wenn beim ersten Versuch keine Route gefunden wird (oder wenn sie zu teuer ist), können Sie die Parameter anpassen:





  - Versuchen Sie es mit einem kleineren Betrag (manchmal geht eine teilweise Neugewichtung durch, während eine große Menge fehlschlägt).
  - Erhöhen Sie die Höchstgebühr schrittweise, aber achten Sie darauf, dass Sie nicht mehr Gebühren zahlen, als es wert ist.
  - Verwenden Sie die Schaltfläche **Eine andere Route suchen**, falls verfügbar, um eine Alternative auszuprobieren.
  - Versuchen Sie es mit einem anderen Paar Kanäle, wenn es wirklich brenzlig wird.



ThunderHub macht den Prozess sehr **intuitiv und visuell**. In nur 4 Schritten (Ausgangskanal auswählen, Eingangskanal auswählen, Betrag, bestätigen) können Sie tun, was früher komplexe manuelle Befehle erforderte. Das Tool ist von unschätzbarem Wert für die Aufrechterhaltung eines ausgewogenen Knotens, die Verbesserung Ihrer Routing-Leistung und Erfahrung (einfacheres Senden und Empfangen von Zahlungen über alle Ihre Kanäle).



Schließlich ist zu beachten, dass ein Rebalance Routing-Kosten verbraucht (die an Zwischenknoten gezahlt werden), es ist also eine **Investition**, um Ihren Knoten flüssiger zu machen. Setzen Sie sie sinnvoll ein, z. B. um einen Kanal zu einem von Ihnen häufig genutzten Dienst zu unterstützen (eingehende Liquidität) oder um einen großen Routing-Kanal auszugleichen. Mit ThunderHub können Sie dies **einfach und effizient** tun.



### Transaktionen



Der Abschnitt **Transaktionen** in ThunderHub entspricht der **Lightning**-Transaktionshistorie Ihres Knotens, d. h. Zahlungen und Rechnungen, die über die Kanäle gezahlt oder empfangen wurden. Es handelt sich um eine Art Kontoauszug für Ihre LN-Operationen.



![Historique des transactions Lightning](assets/fr/14.webp)



Auf dieser Registerkarte finden Sie :





- **Invoice-Diagramm:** In der oberen rechten Ecke zeigt ein Diagramm die Entwicklung der eingegangenen Rechnungen im Laufe der Zeit, so dass Sie die Aktivität Ihres Knotens visualisieren können.





- Eine chronologische Liste aller Lightning-Transaktionen, die *von* oder *an* Ihrem Knoten vorgenommen wurden. Jeder Eintrag kann anzeigen:





  - Art des Vorgangs: **Zahlung gesendet** (ausgehende Zahlung) oder **Zahlung empfangen** (eingehend, über einen bezahlten Invoice).
  - Der Betrag in Sats.
  - Datum/Uhrzeit.
  - Zahlungs-ID (Hash oder RHash-Vorabbild) oder Kommentar (wenn Sie einen Vermerk zu Invoice hinzugefügt haben).
  - Status: **erledigt**, oder möglicherweise **in Bearbeitung**/*gescheitert* (z. B. eine Zahlung, die auf eine Lösung wartet, aber im Allgemeinen bearbeitet LND dies schnell, so dass es hier im Vergleich zu On-Chain-Transaktionen wenig "ausstehend" gibt).



Kurz gesagt, der Abschnitt "Transaktionen" dient als **LN-Aktivitätsprotokoll**. Er ist sehr nützlich, um zu überprüfen, ob eine Zahlung eingegangen ist, wie viele Gebühren sie gekostet hat oder um den Verlauf Ihrer Lightning-Transaktionen zu verfolgen. In Verbindung mit dem Abschnitt "Forwards" (siehe nächste Seite) haben Sie einen vollständigen Überblick über das Geld, das Ihren Knoten durchlaufen hat.



### Stürmer



Die Registerkarte **Weiterleiten** ist der **Weiterleitungsaktivität** Ihres Knotens gewidmet, d. h. den Zahlungen, die **durch Ihre Kanäle geleitet** werden (wenn Sie als Vermittlungsknoten auf dem Lightning Network fungieren). Wenn Sie Ihren Knoten als Routing-Knoten betreiben, ist dies ein wichtiger Abschnitt zur Verfolgung Ihrer Leistung.



![Statistiques de routage Lightning](assets/fr/15.webp)



In Forwards präsentiert ThunderHub :





- **Filter und Anzeigeoptionen:** Oben rechts können Sie mit den Filtern die Daten nach Tag/Woche/Monat/Jahr sortieren und zwischen grafischer und tabellarischer Anzeige wählen.





- **Aktivitätsmeldung:** Wenn während des ausgewählten Zeitraums kein Routing durchgeführt wurde, zeigt der Interface "Keine Weiterleitungen für diesen Zeitraum" an, wie in diesem Beispiel gezeigt.





- Eine **Tabelle der letzten Weiterleitungen**: Jeder Eintrag entspricht einer Zahlung, die über Ihren Knoten **weitergeleitet** wurde. Für jede Weiterleitung sehen wir im Allgemeinen :





  - Timestamp,
  - den weitergeleiteten Betrag (in Sats),
  - die **Gebühr** für diese Weiterleitung (in Sats ist dies die Differenz zwischen dem, was Sie auf dem eingehenden Kanal erhalten und auf dem ausgehenden Kanal gesendet haben),
  - die verwendeten eingehenden und ausgehenden Kanäle (oft durch den Peer-Alias oder die Kanal-ID identifiziert).
  - status (normalerweise *erledigt* oder Fehlschlag, wenn eine Weiterleitung auf dem Weg fehlgeschlagen ist).





- **Aggregierte Statistiken**: ThunderHub berechnet Summen und Statistiken über einen bestimmten Zeitraum (z. B. die letzten 24 Stunden oder 7 Tage usw., manchmal konfigurierbar) und zeigt sie oben auf der Seite an.



Kurz gesagt, der Bereich Forwards bietet einen **Echtzeitüberblick über die Routing-Aktivitäten Ihres Lightning-Knotens**. In Verbindung mit den Abschnitten Channels und Rebalance bildet dies ein komplettes Paket zur Optimierung Ihres Knotens: Channels/Rebalance für die Liquidität, Forwards für die Beobachtung der Ergebnisse (Flows und Gewinne).



### Kette



Der Abschnitt **Kette** entspricht der Bitcoin On-Chain Portfolioverwaltung Ihres LND Knotens. Mit diesem Interface können Sie Bitcoin-Fonds anzeigen und verwalten, die zum Öffnen von Kanälen oder zum Empfangen von Fonds aus geschlossenen Kanälen verwendet werden.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



In Chain finden Sie :





- Saldo On-Chain: **Zeigt den gesamten verfügbaren BTC-Saldo in Wallet LND an.**





- **Liste der UTXOs:** Anzeige aller nicht ausgegebenen Ausgaben (UTXO) mit Betrag, Bestätigungen, Address und Format für jede Ausgabe.





- **Transaktionshistorie:** Detaillierte Tabelle aller Bitcoin-Transaktionen mit Art (Ein-/Ausgang), Datum, Betrag, Gebühren, Bestätigungen, Einschlussblock, Adressen und txid.



### Amboss



ThunderHub ist mit der **Amboss**-Plattform (amboss.space) integriert, die detaillierte Informationen über Lightning-Knoten, einen Liquiditätsmarktplatz und nützliche Funktionen wie verschlüsselte Kanalsicherung und Verfügbarkeitsüberwachung bietet.



![Intégration Amboss avec ses options](assets/fr/17.webp)



In ThunderHub können Sie im Amboss-Bereich Ihren Knoten mit Ihrem Amboss-Konto **verknüpfen**:





- **Ghost Address:** Richten Sie einen **personalisierten Lightning Address** für Ihren Knotenpunkt ein, um eingehende Zahlungen zu erleichtern.





- Automatische Kanal-Backups:** Die wichtigste Funktion für verschlüsselte Kanal-Backups** (SCB-Dateien) auf Amboss. Aktivieren Sie **Amboss Auto Backup = Ja** in den Einstellungen, um bei jedem Kanalwechsel automatisch verschlüsselte Backup-Updates zu senden. Im Falle eines Ausfalls können Sie Ihre Gelder dank dieser externen Sicherung wiederherstellen.





- **Gesundheitschecks:** Aktivieren Sie **Amboss Healthcheck = Ja**, damit Ihr Knoten regelmäßig Pings an Amboss sendet. Sie erhalten eine Warnung, wenn Ihr Knoten offline zu sein scheint.





- **Weitere Funktionen:** Automatischer Balance-Push, **Magma/Hydro**-Integration (Liquiditätsmarktplatz) und Zugang zu detaillierten Leistungsstatistiken.



Die Amboss-Integration fügt ein wesentliches **Sicherheits-Layer** mit automatischer externer Sicherung und Verfügbarkeitsüberwachung hinzu, die direkt von ThunderHub aus zugänglich ist.



### Werkzeuge



Im Abschnitt **Tools** sind verschiedene fortgeschrittene Tools für die Verwaltung Ihres Knotens zusammengefasst. Hier sind die wichtigsten Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Backups:** Verwalten Sie manuell Ihre Channel-Backups (SCB). Mit ThunderHub können Sie **die komplette Sicherungsdatei** Ihrer Kanäle herunterladen (Option "Sicherung aller Kanäle -> Download"). Bewahren Sie diese Datei `channel-all.bak` an einem sicheren Ort auf - sie ist für die Wiederherstellung Ihrer Mittel im Falle eines Absturzes unerlässlich. Sie können auch eine Sicherungsdatei **importieren**, wenn Sie einen Knoten neu einrichten.





- **Buchhaltung:** Exporttool für Finanzberichte einschließlich der verdienten/bezahlten Gebühren und der in einem bestimmten Zeitraum weitergeleiteten Mengen.
- **Signierte Nachrichten:** Signieren oder verifizieren Sie Nachrichten mit Ihrem Knoten, um Ownership Ihres Lightning-Knotens durch eine kryptografische Signatur nachzuweisen.
- Makronen (Abschnitt "Bäckerei"):** Verwalten Sie LND** Makronen, um einen individuellen Zugang zu erstellen. Die Interface "Bäckerei" ermöglicht es Ihnen, jede Berechtigung genau auszuwählen: "Peers hinzufügen oder entfernen", "Kettenadressen erstellen", "Rechnungen erstellen", "Makronen erstellen", "Schlüssel ableiten", "Zugangsschlüssel erhalten", "Kettentransaktionen erhalten", "Rechnungen erhalten", "Wallet-Informationen erhalten", "Zahlungen abrufen", "Peers abrufen", "Rechnungen bezahlen", "Zugangskennungen widerrufen", "An Kettenadressen senden", "Bytes signieren", "Nachrichten signieren", "daemon stoppen", "Bytesignatur überprüfen", "Nachrichten überprüfen" usw. Jede Berechtigung kann einzeln mit den Schaltflächen "Ja/Nein" aktiviert werden, um ein maßgeschneidertes Makkaron zu erstellen.
- **Systeminformationen:** Anzeige der Wallet-Version und der aktivierten RPCs.



Kurz gesagt, der Bereich Tools vereint erweiterte Verwaltungsfunktionen - Backups, Buchhaltung, Sicherheit und Zugriffsmanagement - in einem einheitlichen Interface.



### Tauschen Sie



Auf der Registerkarte **Swap** von ThunderHub können Sie Lightning-Satoshis über den Boltz-Dienst in Bitcoin On-Chain tauschen. Diese Funktion ist nützlich, um überschüssige Lightning-Liquidität in den Kanal "abzuladen", ohne einen Kanal zu schließen.



![Interface de swap via Boltz](assets/fr/19.webp)



Das Verfahren ist einfach:





- **Betrag**: Definieren Sie den umzutauschenden Betrag
- **Address**: Eingabe Bitcoin Empfang Address
- **Ausführung**: ThunderHub kommuniziert mit Boltz, um die Exchange automatisch zu verarbeiten



**Vorteile:**




- Nicht-verwahrende Dienstleistung (keine Barverwahrung)
- Erhalten Sie Ihre bestehenden Kanäle
- Einfach zu bedienender integrierter Interface



Boltz erhebt eine kleine Provision und Sie zahlen die übliche Bitcoin-Transaktionsgebühr. ThunderHub zeigt alle Kosten vor der Bestätigung an.



### Statistiken



Der Bereich **Stats** von ThunderHub bietet **erweiterte Statistiken** zu Ihrem Lightning-Knoten, um die Leistung zu analysieren und das Routing zu optimieren.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Dieser Abschnitt ist für die Optimierung Ihrer Kosten, die Ermittlung erfolgreicher Kanäle und die Planung des Ausbaus Ihres Knotens unerlässlich.



## Schlussfolgerung



**ThunderHub** hat sich als unverzichtbares Werkzeug für die einfache Verwaltung eines Lightning **LND**-Knotens etabliert. Dieser moderne Interface bietet alle wesentlichen Funktionen: Kanalmanagement, Zahlungen, Überwachung, mit erweiterten Funktionen wie automatisches Rebalancing und Amboss-Integration.



**Schlüsselvorteile:**




- Interface schlank und intuitiv
- Leistungsstarke Tools (Rebalance, Boltz-Swaps, automatische Backups)
- Kompatibel mit Umbrel, Voltage, RaspiBlitz und anderen Distributionen



ThunderHub demokratisiert die erweiterte Verwaltung von Lightning-Knoten und macht zugänglich, was zuvor komplexe technische Befehle erforderte. Egal, ob Sie ein Anfänger oder ein erfahrener Operator sind, mit ThunderHub können Sie Ihren Lightning-Knoten über einen modernen, umfassenden Interface effizient verwalten.



## Ressourcen



**Offizielle Links:**




- **Offizielle Website:** [thunderhub.io](https://thunderhub.io)
- **Dokumentation:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **GitHub-Quellcode:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)