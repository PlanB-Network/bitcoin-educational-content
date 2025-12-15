---
name: LNbits Server
description: Installation und Konfiguration eines selbst gehosteten LNbits-Servers auf Ubuntu VPS mit Phoenixd oder auf Umbrel
---

![cover](assets/cover.webp)



LNbits ist eine Open-Source-Webschnittstelle, die jedes Lightning-Backend (LND, Core Lightning, Phoenixd) in eine vollständige Serviceplattform verwandelt. Diese selbst gehostete Lösung ermöglicht es Ihnen, mehrere Lightning-Portfolios isoliert zu verwalten, Verkaufsstellen einzurichten, Spendensysteme oder Abrechnungsdienste zu erstellen und dabei die vollständige Kontrolle über Ihre Mittel zu behalten.



Dieses Tutorial behandelt zwei Installationsansätze: **VPS Ubuntu mit Phoenixd** (leichtgewichtige Lösung ohne einen vollständigen Bitcoin-Knoten) und **Umbrel** (Integration mit Ihrem vorhandenen LND-Knoten). Im Gegensatz zum allgemeinen LNbits-Tutorial der Plan ₿ Academy, das Konzepte und Erweiterungen behandelt, konzentriert sich dieser Leitfaden auf schrittweise technische Installationsverfahren.



## Was ist LNbits?



LNbits ist ein in Python (FastAPI) entwickeltes Lightning-Buchhaltungssystem, das sich mit einem bestehenden Backend (LND, Core Lightning, Phoenixd) verbindet. Im Gegensatz zu herkömmlichen Lightning-Knoten bietet LNbits eine zugängliche Schnittstelle für die Verwaltung mehrerer isolierter Portfolios mit eigenen API-Schlüsseln. Sie können Unterkonten für Ihre Familie, Mitarbeiter oder Projekte einrichten, ohne ihnen Zugriff auf alle Ihre Gelder zu geben.



Die entkoppelte Architektur speichert Informationen in SQLite (Standard) oder PostgreSQL (Produktion), während die Mittel weiterhin von Ihrem Lightning-Backend verwaltet werden. Diese Trennung garantiert Portabilität: Sie können von Phoenixd zu LND migrieren, ohne Ihre Benutzerdaten zu verlieren.



## Wesentliche Merkmale



LNbits bietet ein vielseitiges **Erweiterungssystem**: TPoS (Point of Sale), Paywall (Monetarisierung von Inhalten), Events (Ticketing), LndHub (Server für BlueWallet), Bolt Cards (NFC-Zahlungen), Split Payments (automatische Verteilung) und User Manager (Benutzerverwaltung mit Authentifizierung).



Das **Dashboard** zeigt Echtzeit-Salden, Transaktionshistorie und Abrechnungstools an. Jeder wallet hat eine eindeutige URL, die seine API-Schlüssel enthält und den Zugriff ohne herkömmliche Anmeldung ermöglicht. Das dreistufige API-Schlüsselsystem** (Admin, Rechnung, schreibgeschützt) bietet eine granulare Kontrolle der Berechtigungen für sichere Integrationen.



LNbits implementiert **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) und unterstützt **Lightning Address**, was die Kompatibilität mit modernen Lightning-Wallets garantiert und die Bereitstellung professioneller Dienste erleichtert.



## Unterstützte Plattformen



**Ubuntu VPS**: Leichte Lösung ohne vollen Bitcoin-Knoten. Voraussetzungen: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + Domänenname für die öffentliche Darstellung erforderlich (LNURL-Dienste).



**Umbrel**: Einfache Installation aus dem App Store. Voraussetzung: funktionsfähiger Umbrel-Knoten mit synchronisiertem LND und offenen Kanälen. Automatische Konfiguration.



Nachstehend finden Sie Links zu unseren Umbrel- und Umbrel LND-Tutorials:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installation auf Ubuntu VPS mit Phoenixd



### Schritt 1: Absicherung des VPS-Servers



**Vor jeder Installation** müssen Sie Ihren Ubuntu-VPS-Server nach den Regeln der Kunst absichern. Dieser Schritt ist **kritisch**, um Ihre Infrastruktur und Ihre Lightning-Gelder zu schützen.



Hier finden Sie eine detaillierte Anleitung, die Ihnen den Einstieg erleichtert: **[Erste Ubuntu-Serverkonfiguration - Schritt-für-Schritt-Anleitung](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** von Daniel P. Costas.



Dieser Leitfaden behandelt die Benutzerkonfiguration, sicheres SSH, Firewall (UFW), fail2ban, automatische Updates und bewährte Verfahren zur Systemsicherheit.



### Schritt 2: Installation von Phoenixd



Sobald Ihr Server sicher ist, müssen Sie Phoenixd installieren und konfigurieren. Die Plan ₿ Academy bietet ein umfassendes Tutorial, das die Installation, die seed-Generierung und die Konfiguration des systemd-Dienstes behandelt:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Sobald Phoenixd läuft (überprüfen Sie das mit `./phoenix-cli getinfo`), notieren Sie sich das **HTTP-Passwort** in `~/.phoenix/phoenix.conf` - Sie brauchen es, um LNbits mit Phoenixd zu verbinden.



### LNbits-Einsatz



UV installieren und LNbits klonen:


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigurieren Sie das Phoenixd-Backend:


```bash
cp .env.example .env && nano .env
```



Zu `.env` hinzufügen:


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Testen Sie mit `uv run lnbits --host 0.0.0.0 --port 5000` und erstellen Sie einen systemd-Dienst mit `Wants=phoenixd.service`.



## Ersteinrichtung und erste Nutzung



### SuperUser-Aktivierung



Aktivieren Sie die Administratorschnittstelle in `.env`:


```
LNBITS_ADMIN_UI=true
```



Starten Sie LNbits neu (`sudo systemctl restart lnbits`) und fragen Sie die SuperUser-ID ab:


```bash
cat ~/lnbits/data/.super_user
```



Gehen Sie zu `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` für das Administrationspanel. Im Menü "Server" können Sie Finanzierungsquellen, Erweiterungen und Benutzerkonten konfigurieren.



### Sichere Kontoerstellung



**Wichtig für die öffentliche Nutzung**: Wenn Sie Ihre LNbits-Instanz auf einem öffentlichen Domain-Namen ausstellen, der über das Internet zugänglich ist, ist es **kritisch**, die freie Erstellung von Benutzerkonten zu deaktivieren.



Gehen Sie in der SuperUser-Verwaltungsoberfläche auf "Einstellungen" und dann auf den Abschnitt "Benutzerverwaltung". Dort finden Sie die Option "Erstellung neuer Benutzer zulassen".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Für eine öffentliche Ausstellung mit Domainname** :




- Sie müssen die Option "Anlegen neuer Benutzer zulassen" deaktivieren**
- Ohne diesen Schutz kann jeder im Internet ein Konto auf Ihrer Instanz erstellen
- Ein Angreifer könnte ohne Ihr Wissen Konten erstellen und die Liquidität Ihres Lightning-Knotens nutzen
- Sie müssen die Benutzerkonten manuell über die SuperUser-Schnittstelle erstellen



**Nur für den lokalen Gebrauch** :




- Diese Option ist weniger wichtig, wenn Ihre Instanz nur lokal zugänglich ist (http://localhost:5000)
- Die Deaktivierung dieser Option ist jedoch eine gute allgemeine Sicherheitspraxis



Nach der Konfiguration kann nur der SuperUser-Administrator über die Schnittstelle "Benutzer" neue Benutzerkonten erstellen. Dieser Ansatz garantiert die vollständige Kontrolle darüber, wer auf Ihre Lightning-Infrastruktur zugreifen und Ihre Mittel verwenden kann.



### Öffnen des ersten Kanals



Phoenixd verwaltet die Kanäle automatisch über Auto-Liquidität. Erstellen Sie eine Lightning-Rechnung von ~30.000 sats von LNbits und bezahlen Sie sie von einem anderen wallet. Phoenixd eröffnet automatisch einen Kanal zu ACINQ. Die Eröffnungsgebühr (~20-23k sats) wird abgezogen, der Restsaldo (~7-10k sats) erscheint nach der on-chain Bestätigung.



Prüfen Sie den Status mit `./phoenix-cli getinfo`. Dann erwägen Sie, die automatische Liquidität zu deaktivieren (`auto-liquidity=off` in `phoenix.conf`), um Kanalöffnungen zu kontrollieren.



### Öffentliche Anzeige und HTTPS



**Wichtig**: HTTPS obligatorisch für die öffentliche Anzeige (API-Schlüsselsicherheit + LNURL-Kompatibilität). Überspringen Sie diesen Schritt nur für den lokalen Gebrauch.



**Caddy (empfohlen)**: automatisches SSL. sudo apt install -y caddy`, editiere `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Starten Sie neu: `sudo systemctl restart caddy`.



**Nginx** : Mehr Kontrolle. Installieren Sie `nginx certbot python3-certbot-nginx`, erstellen Sie `/etc/nginx/sites-available/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Aktivieren: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Zu `.env` hinzufügen: `FORWARDED_ALLOW_IPS=*`



## Installation des Schirms



### Bereitstellung über den App Store



Gehe in den Umbrel App Store, suche nach "LNbits" und klicke auf "Installieren".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel prüft automatisch, ob Abhängigkeiten erforderlich sind. LNbits benötigt Lightning Node (LND), um zu funktionieren. Wenn Ihr Lightning Node bereits in Betrieb ist, klicken Sie zur Bestätigung auf "LNbits installieren".



![Dépendances LNbits](assets/fr/02.webp)



Umbrel lädt das Docker-Image herunter, konfiguriert automatisch die Verbindungen mit LND und startet den Container (2-5 Minuten). Die Installation findet vollständig im Hintergrund statt.



### Anfängliche SuperUser-Konfiguration



Beim ersten Start fordert LNbits Sie auf, das SuperUser-Administratorkonto zu erstellen. Geben Sie einen Benutzernamen und ein sicheres Passwort ein, um den Zugriff auf die Administrationsoberfläche zu schützen.



![Configuration SuperUser](assets/fr/03.webp)



**Wichtig**: Dieses SuperUser-Konto hat volle Rechte auf Ihrer LNbits-Instanz. Wählen Sie ein starkes Passwort und bewahren Sie es sicher auf.



Sobald Sie ein Konto erstellt haben, werden Sie automatisch zur Hauptverwaltungsoberfläche weitergeleitet. Umbrel hat LND bereits als Ihre Finanzierungsquelle eingerichtet - alle Blitzzahlungen werden über Ihre bestehenden Kanäle abgewickelt.



### Zugang zur Administratoroberfläche



Klicken Sie im Menü auf der linken Seite auf "Einstellungen", um auf die vollständige Verwaltungsoberfläche zuzugreifen.



![Interface Settings](assets/fr/04.webp)



Im Abschnitt "Wallets Management" werden wichtige Informationen zu Ihrer Konfiguration angezeigt:




- Funding Source** : LndBtcRestWallet (direkte Verbindung zu Ihrem LND Umbrel-Knoten)
- Node Balance** : Gesamte verfügbare Liquidität in Ihren Lightning-Kanälen
- LNbits-Saldo**: Dem LNbits-System zugewiesene Mittel (ursprünglich 0 sats)



Sie können nun direkt die Liquidität Ihres Umbrel-Knotens für alle von Ihnen erstellten LNbits-Brieftaschen nutzen. Es ist keine zusätzliche Konfiguration erforderlich - LNbits ist einsatzbereit und läuft.



### Benutzerverwaltung



Eine der leistungsstärksten Funktionen von LNbits ist die Möglichkeit, mehrere unabhängige Benutzer zu erstellen, jeder mit Passwort-Authentifizierung und isolierten Wallets. Diese Architektur ermöglicht es, die Liquidität Ihres Umbrel-Knotens zu nutzen und gleichzeitig völlig isolierte Unterkonten für verschiedene Zwecke anzubieten: Unternehmen, Familie, Mitarbeiter, Projekte, usw.



Klicken Sie im Seitenmenü auf "Benutzer", um zur Benutzerverwaltung zu gelangen. Klicken Sie auf "KONTO ERSTELLEN", um einen neuen Benutzer hinzuzufügen.



![Gestion des utilisateurs](assets/fr/05.webp)



Füllen Sie das Formular zur Benutzererstellung aus:




- Benutzername**: Login-Benutzername (Beispiel: "satoshi")
- Passwort festlegen**: Aktivieren Sie diese Option, um ein Authentifizierungskennwort festzulegen
- Passwort** und **Passwortwiederholung**: Legen Sie das Passwort für diesen Benutzer fest



![Création utilisateur satoshi](assets/fr/06.webp)



Optionale Felder (Nostr Public Key, E-Mail, Vorname, Nachname) können für eine minimale Konfiguration leer gelassen werden. Klicken Sie zur Bestätigung auf "KONTO ERSTELLEN".



![Confirmation utilisateur créé](assets/fr/07.webp)



Ihr neuer Benutzer erscheint nun in der Liste der Benutzer mit seiner eindeutigen Kennung und seinem Benutzernamen.



![Liste des utilisateurs](assets/fr/08.webp)



**Wichtiger Hinweis**: Jeder Benutzer kann sich völlig unabhängig mit seinem eigenen Passwort anmelden. Der SuperUser-Administrator behält die volle Kontrolle über die Administrationsoberfläche.



### Benutzer wallet-Verwaltung



Nachdem der Benutzer "satoshi" angelegt wurde, müssen Sie ihm einen wallet-Blitz zuweisen. Klicken Sie auf das wallet-Symbol (zweites Symbol) für den betreffenden Benutzer und dann auf "NEUES WALLET ERSTELLEN".



![Gestion des wallets](assets/fr/09.webp)



Ein Dialogfeld fordert Sie auf, das wallet zu benennen. Geben Sie einen beschreibenden Namen ein (z. B. "Wallet von Satoshi") und wählen Sie die Anzeigewährung (CUC, USD, EUR usw.).



![Création wallet](assets/fr/10.webp)



Klicken Sie auf "CREATE". LNbits erzeugt sofort einen funktionierenden wallet Lightning für diesen Benutzer.



![Confirmation wallet créé](assets/fr/11.webp)



Sie sehen nun die beiden vorhandenen Geldbörsen: die automatisch erstellte Standard-wallet "LNbits wallet" und die neue "Wallet von Satoshi". Zur Vereinfachung der Benutzererfahrung können Sie die Standard-wallet löschen, indem Sie auf das Löschsymbol (roter Mülleimer) klicken.



![Wallet final unique](assets/fr/12.webp)



Der "satoshi"-Benutzer hat jetzt einen einzigen, eindeutig identifizierten wallet. Jeder wallet-Benutzer arbeitet völlig autonom, während er die Liquidität des zugrunde liegenden LND-Knotens nutzt.



**Schlüsselkonzept**: Alle diese Wallets teilen sich die globale Liquidität Ihres Umbrel-Knotens. Sie erstellen keine neuen Lightning-Kanäle für jeden wallet - LNbits fungiert als intelligente Buchhaltungsschicht, die die Zuweisung von Mitteln innerhalb Ihrer bestehenden Lightning-Infrastruktur verwaltet. Das ist die Stärke von LNbits' Multi-wallet-System.



### Benutzeranmeldung



Melden Sie sich vom SuperUser-Konto ab (Symbol oben rechts) und kehren Sie zur Anmeldeseite von LNbits zurück. Sie können sich nun mit den Anmeldedaten des neuen Benutzers anmelden.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Geben Sie den zuvor festgelegten Benutzernamen ("satoshi") und das Passwort ein und klicken Sie dann auf "LOGIN". Der Benutzer erhält direkten Zugang zu seinem persönlichen wallet, völlig isoliert von der Verwaltungsschnittstelle.



### Interface von wallet Benutzer



Einmal eingeloggt, hat der Nutzer Zugriff auf seine komplette wallet Lightning-Oberfläche.



![Interface wallet utilisateur](assets/fr/14.webp)



Die Schnittstelle hat folgende Merkmale:




- Aktueller Saldo**: Wird in sats und in der gewählten Währung (in diesem Beispiel CUC) angezeigt
- Wichtigste Aktionen**: ANFRAGE EINFÜGEN, RECHNUNG ERSTELLEN, QR-Symbol (Schnellscan)
- Transaktionshistorie** : Vollständige Liste aller Zahlungen und Quittungen
- Rechte Seitenwand**: Konfigurations- und Zugriffsoptionen



### Mobiler Zugang zum wallet



Das rechte Seitenpanel bietet eine besonders praktische Funktion: den mobilen Zugriff auf den wallet. Klappen Sie den Abschnitt "Mobiler Zugriff" aus, um die verfügbaren Optionen zu entdecken.



![Mobile Access](assets/fr/15.webp)



LNbits bietet mehrere Möglichkeiten, diesen wallet auf einem Smartphone zu verwenden:



**Option 1: Kompatible mobile Anwendungen




- Laden Sie **Zeus** oder **BlueWallet** aus dem App Store oder Google Play herunter
- Aktivieren Sie die Erweiterung **LndHub** in LNbits für diesen wallet
- Scannen Sie den LndHub QR-Code mit der mobilen App, um das wallet zu verbinden



**Option 2: Direkter Zugriff über den mobilen Browser**




- Der QR-Code, der in "Mit QR-Code zum Telefon exportieren" angezeigt wird, enthält die vollständige URL des wallet mit integrierter Authentifizierung
- Scannen Sie diesen QR-Code mit Ihrem Smartphone, um wallet direkt in Ihrem mobilen Browser zu öffnen
- Seite für schnellen Zugriff zum Startbildschirm hinzufügen



**Wichtige Sicherheit**: Diese URL enthält die API-Schlüssel für den vollständigen Zugang zu wallet. Geben Sie sie niemals öffentlich weiter. Behandeln Sie diesen QR-Code wie Ihre privaten Bitcoin-Schlüssel - jeder, der diesen QR-Code scannt, erhält vollen Zugang zu wallet.



Diese mobile Funktion verwandelt Ihre LNbits Umbrel-Instanz in einen veritablen Lightning wallet-Server für Sie und Ihre Freunde, wobei Sie dank Ihres selbst gehosteten Knotens die vollständige Hoheit über Ihr Geld behalten.



### Gemeinsamer Benutzerzugang



Der Hauptanwendungsfall für diese Mehrbenutzerkonfiguration ist die **Teilung von Geldbörsen mit Ihrer Familie oder Ihrem engen Kreis**. Sobald Sie einen Benutzer mit einem speziellen wallet (wie "satoshi" in unserem Beispiel) erstellt haben, können Sie diese Anmeldedaten mit vertrauenswürdigen Mitgliedern Ihres Haushalts teilen.



**Zugangssicherheit auf Umbrel**: Der Zugang zu Ihrer LNbits-Instanz auf Umbrel ist natürlich geschützt, da er nur über :




- In Ihrem lokalen Netzwerk** : Mitglieder Ihres Haushalts, die mit demselben WiFi/Ethernet-Netzwerk verbunden sind, können auf die Instanz zugreifen
- Über VPN**: Wenn Sie ein VPN wie Tailscale auf Ihrem Umbrel-Server konfigurieren, können autorisierte Benutzer einen sicheren Fernzugriff erhalten



Dieser doppelte Schutz (Netzzugang + Benutzerauthentifizierung) macht die Option "Erstellung neuer Benutzer zulassen" bei Umbrel weniger kritisch. Nur Personen, die bereits Zugang zu Ihrem Netzwerk oder VPN haben, können die Login-Schnittstelle erreichen.



**Typisches Szenario**: Sie erstellen ein "Papa"-Konto, ein "Mama"-Konto, ein "Business"-Konto und so weiter. Jedes Familienmitglied hat seinen eigenen isolierten wallet Lightning, profitiert aber von der gemeinsamen Liquidität Ihres Umbrel-Knotens. Teilen Sie einfach den Benutzernamen und das Passwort mit - der Benutzer kann sich dann von jedem Gerät in Ihrem lokalen Netzwerk oder über Ihr Tailscale VPN verbinden. Bitte lesen Sie unser Tailscale-Tutorial für weitere Informationen:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Verfügbare Erweiterungen erforschen



Kehren Sie zur SuperUser-Oberfläche zurück und rufen Sie das Menü "Erweiterungen" auf der linken Seite auf, um das gesamte Ökosystem der LNbits-Erweiterungen zu entdecken.



![Extensions disponibles](assets/fr/16.webp)



LNbits bietet einen umfangreichen Katalog von Erweiterungen, die Ihre Instanz in eine echte Lightning-Services-Plattform verwandeln:





- Jukebox**: sats-betriebenes Jukebox-System (Spotify-Zahlungen)
- Support-Tickets**: Bezahltes Support-System (Sie erhalten eine Antwort auf Ihre Fragen)
- TPoS**: Sicheres, mobiles Point-of-Sale-Terminal für Einzelhändler
- User Manager**: erweiterte Benutzer- und wallet-Verwaltung (die wir gerade verwendet haben)
- Veranstaltungen**: Verkauf und Entwertung von Veranstaltungstickets
- LNURLD-Geräte**: Point-of-Sale-Management, Geldautomaten, angeschlossene Switches
- SMTP**: Ermöglicht Benutzern das Versenden von E-Mails und das Sammeln von Satellitendaten
- Boltcards**: Programmierung von NFC-Karten für Lightning-Tap-to-Pay-Zahlungen
- NostrNip5**: Erstellen Sie NIP5-Adressen für Ihre Domains
- Aufgeteilte Zahlungen**: Automatische Verteilung von Zahlungen auf mehrere Geldbörsen



Jede Erweiterung wird mit einem einzigen Klick von dieser Schnittstelle aus aktiviert. Mit "FREE" gekennzeichnete Erweiterungen sind kostenlos, während einige als "PAID"-Versionen erhältlich sind. Durchsuchen Sie den Katalog, um die Erweiterungen zu finden, die Ihren Bedürfnissen entsprechen - sei es für die Geschäftswelt, das Familienmanagement oder zum Experimentieren mit den Funktionen des Lightning Network.



## Vorteile und Grenzen



**Vorteile**: Finanzielle Souveränität (vollständige Kontrolle über Fonds/Schlüssel/Daten), architektonische Flexibilität (verlustfreie VPS→full node-Migration), professionelles Erweiterungssystem, intuitive Benutzeroberfläche.



**Einschränkungen** : Software in der Beta-Phase (Vorsicht bei den Beträgen), Sicherheit unter der Verantwortung des Administrators, URLs mit sensiblen API-Schlüsseln (HTTPS obligatorisch), Mehrbenutzer-Verwaltung impliziert die Verantwortung der Aufsichtsperson.



## Bewährte Praktiken



**Backups**: Phoenixd Seed/LND Anmeldeinformationen, LNbits-Datenbank, .env-Dateien. Täglich automatisieren, nicht auf dem Produktionsserver, verschlüsselt. Testen Sie Wiederherstellungen regelmäßig.



**Wartung**: Prüfen Sie regelmäßig, ob Updates verfügbar sind (LNbits, Lightning-Backend, Betriebssystem). Prüfen Sie immer die Versionshinweise vor größeren Updates.





- Auf Umbrel**: Der App Store benachrichtigt Sie automatisch über neue Versionen. Synchronisieren Sie Erweiterungen über "Erweiterungen verwalten" > "Alle aktualisieren". Überprüfen Sie die Einbeziehung der SQLite-Datenbank in die automatischen Umbrel-Backups.
- Auf VPS**: Aktualisieren Sie manuell mit `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Systemprotokolle überwachen: `sudo journalctl -u lnbits -f`.



## Schlussfolgerung



LNbits Self-Hosting bietet einen konkreten Weg zur finanziellen Souveränität von Lightning. VPS+Phoenixd bietet eine leichtgewichtige Lösung für schnelle Dienste, Umbrel volle Integration mit bestehenden Bitcoin Knoten. Die skalierbare Architektur ermöglicht die Entwicklung vom einfachen wallet für mehrere Nutzer bis hin zu anspruchsvollen Geschäftsanwendungen.



Selbst-Hosting bedeutet Verantwortung: Seeds sichern, Zugang schützen, mit bescheidenen Beträgen beginnen. Mit diesen Vorsichtsmaßnahmen wird LNbits zu einer robusten Lösung für die Lightning Economy, während Dezentralisierung und Autonomie erhalten bleiben.



## Ressourcen



### Offizielle Dokumentation




- [LNbits-Dokumentation](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Offizielle Installationsanleitung](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Gemeinschaftsleitfäden




- [Erstkonfiguration eines Ubuntu-Servers](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) von Daniel P. Costas (Schritt-für-Schritt-Anleitung zur VPS-Sicherheit)
- [LNbits + Phoenixd-Installation auf Ubuntu VPS](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) von Daniel P. Costas (vollständige Anleitung)
- [LNbits Server auf Clearnet] (https://ereignishorizont.xyz/lnbits-server/en/) von Axel
- [LNbits auf VPS](https://github.com/TrezorHannes/vps-lnbits) von Hannes